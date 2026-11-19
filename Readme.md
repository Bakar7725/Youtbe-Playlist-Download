📜 License
This project is licensed under the MIT License.

text
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
💡 Author
Bakar7725

🐙 GitHub: @Bakar7725

📧 Email: abug4201@gmail.com

🌟 Show Your Support
If this project helped you, please give it a ⭐ on GitHub! It means a lot and helps others discover the project.

text

2. Install dependencies
bash
pip install -r requirements.txt
3. Run the app
bash
python launcher.py
✅ Your browser will automatically open to http://127.0.0.1:<random-port>.
✅ FFmpeg will be downloaded automatically on first run if missing.

📦 Building the Standalone .exe (Windows)
To create a portable .exe that runs on any PC without Python installed:

1. Install PyInstaller
bash
pip install pyinstaller
2. Make sure ffmpeg.exe is in the project folder
The app will auto-download it on first run, OR

Download manually from gyan.dev (ffmpeg-release-essentials.zip).

Place ffmpeg.exe in the same folder as app.py.

3. Run the build command
bash
pyinstaller --noconfirm --onefile --console --add-data "templates;templates" --add-data "ffmpeg.exe;." launcher.py
4. Get your EXE
Your portable .exe will be located in the dist/ folder.

Copy launcher.exe anywhere (Desktop, USB, another PC).

Double-click it. A downloads/ folder will be created next to the EXE.

5. Final EXE behavior
✅ Auto-launches your default browser

✅ Auto-selects a free port (no port conflicts)

✅ Bundles FFmpeg inside (no installation needed)

✅ Saves videos next to the EXE

🛠️ Tech Stack
Layer	Technology
Backend	Python, Flask, Flask-Cors
Downloader Engine	yt-dlp
Media Processing	FFmpeg (auto-downloaded)
Frontend	HTML, CSS, Vanilla JavaScript
Packaging	PyInstaller
📁 Folder Structure
text
Youtbe-Playlist-Download/
├── Exe/
│   └── launcher.exe        # Prebuilt Windows executable (download directly)
├── app.py                  # Flask backend + download manager
├── launcher.py             # Startup script (dynamic port + browser opener)
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── .gitignore              # Git ignore rules
└── templates/
    └── index.html          # Full frontend UI
Note: The following are auto-generated and not included in the repo:

ffmpeg.exe (auto-downloaded on first run)

downloads/ (videos are saved here at runtime)

build/, dist/, *.spec (PyInstaller build artifacts)

🔧 Configuration
Port Configuration
The app uses a dynamic port by default (finds any free port starting from 5000). If you want to force a specific port, edit launcher.py:

python
# Change this line:
app.run(host="127.0.0.1", port=PORT, debug=False, threaded=True)

# To this:
app.run(host="127.0.0.1", port=5000, debug=False, threaded=True)
FFmpeg Location
The app searches for FFmpeg in this order:

ffmpeg.exe next to the app

Bundled inside the EXE (if compiled)

System PATH

Downloads from gyan.dev if not found

🐛 Troubleshooting
"FFmpeg is not installed" error
The app should auto-download FFmpeg on first run.

If it fails, manually download ffmpeg-release-essentials.zip from gyan.dev and extract ffmpeg.exe next to app.py.

"Port 5000 already in use"
This is handled automatically. The app will pick a random free port.

Check the console output to see which port was selected.

Downloads folder location
When running python launcher.py from source: downloads/ is created in the project folder.

When running launcher.exe: downloads/ is created next to the EXE.

Windows Defender warning on EXE
PyInstaller EXEs are sometimes flagged because they are unsigned.

Click "More info" → "Run anyway".

⚠️ Disclaimer
This tool is for educational purposes only. Please respect copyright laws and only download content you have permission to download (e.g., your own uploads, public domain content, or Creative Commons licensed videos).

The author is not responsible for any misuse of this tool.

📜 License
This project is licensed under the MIT License.

text
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
💡 Author
Bakar7725

🐙 GitHub: @Bakar7725

📧 Email: abug4201@gmail.com

🌟 Show Your Support
If this project helped you, please give it a ⭐ on GitHub! It means a lot and helps others discover the project.

text

---
