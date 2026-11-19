import os
import re
import time
import uuid
import threading
import shutil
import sys
import yt_dlp
from flask import Flask, request, jsonify, render_template, send_file, abort
from flask_cors import CORS

# --- PyInstaller Resource Path Fixer ---
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

app = Flask(__name__, template_folder=resource_path("templates"))
CORS(app)

# --- Handle Downloads Folder (Saved next to the EXE) ---
if getattr(sys, 'frozen', False):
    EXE_DIR = os.path.dirname(sys.executable)
else:
    EXE_DIR = os.path.dirname(os.path.abspath(__file__))

DOWNLOAD_DIR = os.path.join(EXE_DIR, "downloads")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# --- Find FFmpeg ---
local_ffmpeg = os.path.join(EXE_DIR, "ffmpeg.exe")
bundled_ffmpeg = resource_path("ffmpeg.exe")

if os.path.exists(local_ffmpeg):
    FFMPEG_PATH = local_ffmpeg
elif os.path.exists(bundled_ffmpeg):
    FFMPEG_PATH = bundled_ffmpeg
else:
    FFMPEG_PATH = shutil.which("ffmpeg")

HAS_FFMPEG = FFMPEG_PATH is not None


class DownloadManager:
    def __init__(self):
        self.jobs = {}
        self.lock = threading.Lock()
        self.cancelled = set()

    def start(self, url, format_id, mode, title_hint=""):
        job_id = uuid.uuid4().hex[:12]
        with self.lock:
            self.jobs[job_id] = {
                "id": job_id,
                "url": url,
                "format_id": format_id,
                "mode": mode,
                "title": title_hint or "Preparing…",
                "status": "queued",
                "percent": 0.0,
                "downloaded": 0,
                "total": 0,
                "speed": 0.0,
                "eta": None,
                "filename": None,
                "filepath": None,
                "error": None,
                "created": time.time(),
            }
        t = threading.Thread(target=self._run, args=(job_id,), daemon=True)
        t.start()
        return job_id

    def cancel(self, job_id):
        with self.lock:
            if job_id in self.jobs:
                self.cancelled.add(job_id)
                self.jobs[job_id]["status"] = "cancelled"
                filepath = self.jobs[job_id].get("filepath")
                if filepath and os.path.exists(filepath):
                    try:
                        os.remove(filepath)
                    except:
                        pass

    def snapshot(self):
        with self.lock:
            jobs = []
            for j in self.jobs.values():
                jobs.append({k: v for k, v in j.items() if k != "filepath"})
            jobs.sort(key=lambda x: x["created"], reverse=True)
            return jobs

    def get(self, job_id):
        with self.lock:
            j = self.jobs.get(job_id)
            return dict(j) if j else None

    def _progress_hook(self, job_id, d):
        with self.lock:
            if job_id in self.cancelled:
                raise Exception("Cancelled by user")

            j = self.jobs.get(job_id)
            if not j:
                return
            if d.get("status") == "downloading":
                j["status"] = "downloading"
                total = d.get("total_bytes") or d.get("total_bytes_estimate") or 0
                downloaded = d.get("downloaded_bytes") or 0
                j["total"] = total
                j["downloaded"] = downloaded
                j["percent"] = (downloaded / total * 100.0) if total else 0.0
                j["speed"] = d.get("speed") or 0.0
                j["eta"] = d.get("eta")
                fn = d.get("filename") or d.get("info_dict", {}).get("title")
                if fn:
                    j["title"] = os.path.splitext(os.path.basename(fn))[0]
            elif d.get("status") == "finished":
                j["status"] = "merging"
                j["percent"] = 100.0
                fn = d.get("filename")
                if fn:
                    j["title"] = os.path.splitext(os.path.basename(fn))[0]

    def _run(self, job_id):
        with self.lock:
            job = self.jobs[job_id]
            url = job["url"]
            fmt = job["format_id"]
            mode = job["mode"]

        if mode == "audio":
            fmt_selector = fmt
        else:
            if HAS_FFMPEG:
                fmt_selector = f"{fmt}+bestaudio/{fmt}"
            else:
                fmt_selector = fmt

        ydl_opts = {
            "format": fmt_selector,
            "outtmpl": os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s"),
            "merge_output_format": "mp4",
            "ignoreerrors": False,
            "quiet": True,
            "noprogress": True,
            "progress_hooks": [lambda d: self._progress_hook(job_id, d)],
        }
        
        if HAS_FFMPEG:
            ydl_opts["ffmpeg_location"] = FFMPEG_PATH
            ydl_opts["postprocessor_args"] = {"merger": ["-movflags", "+faststart"]}

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                base, _ = os.path.splitext(filename)
                actual_path = None
                for ext in [".mp4", ".webm", ".mkv", ".m4a", ".opus", ".mp3"]:
                    candidate = base + ext
                    if os.path.exists(candidate):
                        actual_path = candidate
                        break
                if not actual_path:
                    downloads = info.get("requested_downloads", [])
                    if downloads:
                        actual_path = downloads[0].get("filepath")

            with self.lock:
                j = self.jobs[job_id]
                if j["status"] == "cancelled":
                    if actual_path and os.path.exists(actual_path):
                        os.remove(actual_path)
                    return

                if actual_path and os.path.exists(actual_path):
                    j["status"] = "finished"
                    j["percent"] = 100.0
                    j["filepath"] = actual_path
                    j["filename"] = os.path.basename(actual_path)
                    j["total"] = os.path.getsize(actual_path)
                    j["downloaded"] = j["total"]
                    j["speed"] = 0.0
                    j["eta"] = 0
                else:
                    j["status"] = "error"
                    j["error"] = "File not found after download"
        except Exception as e:
            with self.lock:
                j = self.jobs.get(job_id)
                if j:
                    if j["status"] == "cancelled":
                        return
                    j["status"] = "error"
                    j["error"] = str(e)


manager = DownloadManager()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/parse", methods=["POST"])
def parse_url():
    data = request.get_json()
    url = data.get("url", "").strip()
    if not url:
        return jsonify({"error": "Please enter a URL"}), 400

    ydl_opts = {"quiet": True, "extract_flat": "in_playlist", "skip_download": True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as e:
        return jsonify({"error": f"Parsing failed: {str(e)}"}), 500

    if info.get("_type") in ("playlist", "multi_video"):
        entries = info.get("entries", [])
        playlist = []
        for i, entry in enumerate(entries):
            if entry is None:
                continue
            vid = entry.get("id")
            if not vid:
                raw_url = entry.get("url") or ""
                m = re.search(r"(?:v=|youtu\.be/|/shorts/|/embed/)([A-Za-z0-9_-]{11})", raw_url)
                if m:
                    vid = m.group(1)
            playlist.append({
                "index": i,
                "id": vid,
                "title": entry.get("title", "Unknown Title"),
                "url": entry.get("url") or (f"https://www.youtube.com/watch?v={vid}" if vid else ""),
                "thumbnail": "",
            })
        return jsonify({
            "type": "playlist",
            "title": info.get("title", "Playlist"),
            "count": len(playlist),
            "entries": playlist,
        })
    return get_formats_for_video(url)


@app.route("/api/video-info", methods=["POST"])
def video_info():
    data = request.get_json()
    url = data.get("url", "").strip()
    if not url:
        return jsonify({"error": "Missing url"}), 400

    ydl_opts = {"quiet": True, "skip_download": True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as e:
        return jsonify({"error": f"Failed: {str(e)}"}), 500

    thumb = info.get("thumbnail") or ""
    if not thumb and info.get("thumbnails"):
        for t in reversed(info["thumbnails"]):
            if t and t.get("url"):
                thumb = t["url"]
                break

    return jsonify({
        "url": url,
        "title": info.get("title", "Unknown"),
        "thumbnail": thumb,
        "duration": info.get("duration"),
    })


@app.route("/api/formats", methods=["POST"])
def get_formats():
    data = request.get_json()
    url = data.get("url", "").strip()
    if not url:
        return jsonify({"error": "Please provide the video URL"}), 400
    return get_formats_for_video(url)


def get_formats_for_video(url):
    ydl_opts = {"quiet": True, "skip_download": True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as e:
        return jsonify({"error": f"Failed to get formats: {str(e)}"}), 500

    formats = info.get("formats", [])
    video_formats, audio_formats = [], []
    seen_video, seen_audio = set(), set()
    
    best_audio_id = None
    best_audio_abr = 0

    for f in formats:
        vcodec = f.get("vcodec", "none")
        acodec = f.get("acodec", "none")
        if vcodec == "none" and acodec != "none":
            abr = f.get("abr") or 0
            if abr > 0:
                if best_audio_id is None or abr > best_audio_abr:
                    best_audio_id = f.get("format_id")
                    best_audio_abr = abr

    STANDARD_HEIGHTS = [144, 240, 360, 480, 720, 1080, 1440, 2160, 4320]

    def get_standard_quality_label(height):
        if not height:
            return "?"
        closest = min(STANDARD_HEIGHTS, key=lambda x: abs(x - height))
        if abs(closest - height) <= 30 or height > 4320:
            return f"{closest}p"
        else:
            return f"{closest}p HD"

    for f in formats:
        vcodec = f.get("vcodec", "none")
        acodec = f.get("acodec", "none")
        fmt_id = f.get("format_id")
        ext = f.get("ext", "")
        height = f.get("height", 0)
        fps = f.get("fps")

        if vcodec != "none":
            quality_label = get_standard_quality_label(height)
            key = (quality_label, ext, fps, acodec != "none")
            if key in seen_video:
                continue
            seen_video.add(key)
            
            has_audio = acodec != "none"

            video_formats.append({
                "format_id": fmt_id,
                "ext": ext,
                "resolution": quality_label,
                "height": height,
                "fps": fps,
                "vcodec": vcodec,
                "acodec": acodec,
                "has_audio": has_audio,
                "note": f.get("format_note", ""),
            })
        elif acodec != "none" and vcodec == "none":
            key = (f.get("abr") or 0, ext, acodec.split(".")[0])
            if key in seen_audio:
                continue
            seen_audio.add(key)
            audio_formats.append({
                "format_id": fmt_id,
                "ext": ext,
                "abr": f.get("abr"),
                "acodec": acodec,
                "note": f.get("format_note", ""),
            })

    video_formats.sort(key=lambda x: (x["height"] or 0), reverse=True)
    audio_formats.sort(key=lambda x: (x["abr"] or 0), reverse=True)

    return jsonify({
        "type": "video",
        "title": info.get("title", "Unknown"),
        "thumbnail": info.get("thumbnail", ""),
        "duration": info.get("duration"),
        "webpage_url": info.get("webpage_url", url),
        "video_formats": video_formats,
        "audio_formats": audio_formats,
        "best_audio_id": best_audio_id,
        "has_ffmpeg": HAS_FFMPEG,
    })


@app.route("/api/download/start", methods=["POST"])
def download_start():
    data = request.get_json()
    url = data.get("url", "").strip()
    format_id = data.get("format_id", "").strip()
    mode = data.get("mode", "video")
    title_hint = data.get("title", "")
    if not url or not format_id:
        return jsonify({"error": "Missing url or format_id"}), 400

    job_id = manager.start(url, format_id, mode, title_hint)
    return jsonify({"job_id": job_id})


@app.route("/api/download/cancel/<job_id>", methods=["POST"])
def download_cancel(job_id):
    manager.cancel(job_id)
    return jsonify({"success": True})


@app.route("/api/download/status", methods=["GET"])
def download_status():
    return jsonify({"jobs": manager.snapshot()})


@app.route("/api/download/file/<job_id>", methods=["GET"])
def download_file(job_id):
    job = manager.get(job_id)
    if not job:
        abort(404)
    if job["status"] != "finished" or not job.get("filepath"):
        abort(400)
    return send_file(job["filepath"], as_attachment=True, download_name=job["filename"])


if __name__ == "__main__":
    if HAS_FFMPEG:
        print(f"✅ Found FFmpeg at: {FFMPEG_PATH}")
    else:
        print("❌ WARNING: FFmpeg not found! Merging video and audio will fail.")
        print("   Will fallback to downloading video-only or audio-only.")
        
    app.run(debug=True, port=5000, threaded=True)