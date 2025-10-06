import yt_dlp
import os

# ===== USER INPUT =====
playlist_url = input("Enter YouTube playlist URL: ")
download_path = input("Enter download folder path (or leave empty for current folder): ")
if download_path.strip() == "":
    download_path = os.getcwd()
# ======================

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # highest quality video + audio
    'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # save path and filename
    'merge_output_format': 'mp4',  # merge video + audio into mp4
    'ignoreerrors': True,  # skip failed downloads
    'noplaylist': False,   # download entire playlist
    'progress_hooks': [lambda d: print(f"{d['status']} - {d.get('filename','')}")],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print("All downloads completed!")
