# 🎬 YouTube Playlist Downloader

## 📝 Description
A simple Python script to download entire YouTube playlists in the highest available quality. The script automatically merges video and audio streams into MP4 format.

## ✨ Features
- 📥 Downloads complete YouTube playlists
- 🏆 Automatic quality selection (best video + best audio)
- 🔄 Converts to MP4 format
- ⚠️ Error handling for failed downloads
- 📊 Progress tracking
- 📁 Customizable download location

## 🛠 Requirements
- Python 3.6 or higher
- yt-dlp library

## 📥 Installation Steps

### 1. Install Python
- Download Python from: https://www.python.org/downloads/
- During installation, **check "Add Python to PATH"**
- Verify installation: Open Command Prompt and type `python --version`

### 2. Install yt-dlp
Open Command Prompt/Terminal and run:


### 3. Download the Script
- Save the Python script as `youtube_downloader.py`
- Keep it in a folder where you want to manage your downloads

## 🚀 How to Use

### Step 1: Run the Script


### Step 2: Provide Input
- **Playlist URL**: Paste the full YouTube playlist URL
  - Example: `https://www.youtube.com/playlist?list=PLabc123...`
- **Download Path**: 
  - Press Enter to use current folder
  - Or type full path: `C:\Users\YourName\Videos`

### Step 3: Wait for Completion
- The script will show progress for each video
- Downloads will be saved as MP4 files
- "All downloads completed!" message when finished

## ⚠️ Important Notes
- 🌐 Requires stable internet connection
- ⏱️ Download time depends on playlist size and video quality
- 💾 Videos are saved as: `Video Title.mp4`
- ❌ Failed downloads are automatically skipped
- 💿 Make sure you have sufficient disk space

## 📋 Example Usage

Enter YouTube playlist URL: https://www.youtube.com/playlist?list=P...............
Enter download folder path (or leave empty for current folder): C:\YouTubeDownloads

## 🔧 Troubleshooting
- ❌ If you get "python not found" error, Python is not in PATH
- ❌ If pip command fails, try `pip3 install yt-dlp`
- ❌ Ensure the playlist URL is correct and public
- ❌ Check folder permissions if download fails
- ❌ Make sure you have write permissions in the download folder

## 📞 Support
If you encounter any issues:
1. Ensure all requirements are installed correctly
2. Check your internet connection
3. Verify the playlist URL is accessible
4. Make sure you have enough storage space

Happy Downloading! 🎉