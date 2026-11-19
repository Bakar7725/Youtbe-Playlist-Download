# 🎥 YouTube Playlist Downloader (Portable Desktop App)

A lightweight, portable Flask-based video downloader that runs in your browser. It supports YouTube playlists, automatically downloads FFmpeg if needed, merges high-quality audio/video streams (up to 4K), and can be compiled into a single standalone `.exe` for Windows.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)
![Flask](https://img.shields.io/badge/flask-3.0+-red.svg)
![yt-dlp](https://img.shields.io/badge/yt--dlp-latest-orange.svg)

---

## 📖 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start-for-developers)
- [Building the EXE](#-building-the-standalone-exe-windows)
- [Tech Stack](#️-tech-stack)
- [Folder Structure](#-folder-structure)
- [Troubleshooting](#-troubleshooting)
- [Disclaimer](#️-disclaimer)
- [License](#-license)
- [Author](#-author)

---

## ✨ Features

- 📋 **Playlist Support:** Analyze and download entire YouTube playlists or single videos.
- 🎬 **High-Quality Merging:** Automatically downloads the best audio track and merges it with high-res video (up to 4K) using FFmpeg.
- ⚙️ **Auto FFmpeg Installer:** Don't have FFmpeg? No problem. The app will download it silently on the first run.
- 🚀 **Smart Port Selection:** If port 5000 is busy, the app automatically finds a free port.
- 📦 **Portable `.exe`:** Can be compiled into a single `.exe` for Windows — no Python required on the target machine.
- ⏱️ **Real-time Progress:** Live progress bars with speed, ETA, and a cancel button.
- 🎨 **Clean UI:** Modern dark-themed interface with drag-and-drop playlist support.
- 🔀 **Drag & Drop:** Drag any video from the playlist directly into the main panel to load its formats.

---

## 🚀 Quick Start (For Developers)

### Prerequisites
- Python 3.9 or higher
- Internet connection (for FFmpeg auto-download on first run)

### 1. Clone the repository
```bash
git clone https://github.com/Bakar7725/Youtbe-Playlist-Download.git
cd Youtbe-Playlist-Download
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python launcher.py
```

✅ Your browser will automatically open to `http://127.0.0.1:<random-port>`.
✅ FFmpeg will be downloaded automatically on first run if missing.

---

## 📦 Building the Standalone `.exe` (Windows)

To create a portable `.exe` that runs on any PC **without Python installed**:

### 1. Install PyInstaller
```bash
pip install pyinstaller
```

### 2. Make sure `ffmpeg.exe` is in the project folder
- The app will auto-download it on first run, OR
- Download manually from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/) (`ffmpeg-release-essentials.zip`).
- Place `ffmpeg.exe` in the same folder as `app.py`.

### 3. Run the build command
```bash
pyinstaller --noconfirm --onefile --console --add-data "templates;templates" --add-data "ffmpeg.exe;." launcher.py
```

### 4. Get your EXE
- Your portable `.exe` will be located in the `dist/` folder.
- Copy `launcher.exe` anywhere (Desktop, USB, another PC).
- Double-click it. A `downloads/` folder will be created **next to the EXE**.

### 5. Final EXE behavior
- ✅ Auto-launches your default browser
- ✅ Auto-selects a free port (no port conflicts)
- ✅ Bundles FFmpeg inside (no installation needed)
- ✅ Saves videos next to the EXE

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python, Flask, Flask-Cors |
| **Downloader Engine** | yt-dlp |
| **Media Processing** | FFmpeg (auto-downloaded) |
| **Frontend** | HTML, CSS, Vanilla JavaScript |
| **Packaging** | PyInstaller |

---

## 📁 Folder Structure

```text
Youtbe-Playlist-Download/
├── app.py                  # Flask backend + download manager
├── launcher.py             # Startup script (dynamic port + browser opener)
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── .gitignore              # Git ignore rules
└── templates/
    └── index.html          # Full frontend UI
```

**Note:** The following are auto-generated and **not** included in the repo:
- `ffmpeg.exe` (auto-downloaded on first run)
- `downloads/` (videos are saved here at runtime)
- `build/`, `dist/`, `*.spec` (PyInstaller build artifacts)

---

## 🔧 Configuration

### Port Configuration
The app uses a **dynamic port** by default (finds any free port starting from 5000). If you want to force a specific port, edit `launcher.py`:

```python
# Change this line:
app.run(host="127.0.0.1", port=PORT, debug=False, threaded=True)

# To this:
app.run(host="127.0.0.1", port=5000, debug=False, threaded=True)
```

### FFmpeg Location
The app searches for FFmpeg in this order:
1. `ffmpeg.exe` next to the app
2. Bundled inside the EXE (if compiled)
3. System PATH
4. Downloads from `gyan.dev` if not found

---

## 🐛 Troubleshooting

### "FFmpeg is not installed" error
- The app should auto-download FFmpeg on first run.
- If it fails, manually download `ffmpeg-release-essentials.zip` from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/) and extract `ffmpeg.exe` next to `app.py`.

### "Port 5000 already in use"
- This is handled automatically. The app will pick a random free port.
- Check the console output to see which port was selected.

### Downloads folder location
- When running `python launcher.py` from source: `downloads/` is created in the project folder.
- When running `launcher.exe`: `downloads/` is created **next to the EXE**.

### Windows Defender warning on EXE
- PyInstaller EXEs are sometimes flagged because they are unsigned.
- Click **"More info"** → **"Run anyway"**.

---

## ⚠️ Disclaimer

This tool is for **educational purposes only**. Please respect copyright laws and only download content you have permission to download (e.g., your own uploads, public domain content, or Creative Commons licensed videos).

The author is not responsible for any misuse of this tool.

---

## 📜 License

This project is licensed under the **MIT License**.

```text
MIT License

Copyright (c) 2026 Bakar7725

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 💡 Author

**Bakar7725**

- 🐙 GitHub: [@Bakar7725](https://github.com/Bakar7725)
- 

---

## 🌟 Show Your Support

If this project helped you, please give it a ⭐ on GitHub! It means a lot and helps others discover the project.
