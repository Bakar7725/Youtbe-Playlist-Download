# 🎥 YouTube Playlist Downloader (Portable Desktop App)

A lightweight, portable Flask-based video downloader that runs in your browser. It supports YouTube playlists, automatically downloads FFmpeg if needed, merges high-quality audio/video streams (up to 4K), and can be compiled into a single standalone `.exe` for Windows.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)
![Flask](https://img.shields.io/badge/flask-3.0+-red.svg)
![yt-dlp](https://img.shields.io/badge/yt--dlp-latest-orange.svg)

---

## ⬇️ Download

> 🚀 **Ready to use — no installation required!**
>
> **[📥 Download launcher.exe (Windows)](https://github.com/Bakar7725/Youtbe-Playlist-Download/raw/main/Exe/launcher.exe)**
>
> *Portable standalone executable. FFmpeg is bundled inside. Just double-click and go.*
>
> **Requirements:** Windows 10 or 11. No Python, no setup.

---

## 📖 Table of Contents

- [Download](#️-download)
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
