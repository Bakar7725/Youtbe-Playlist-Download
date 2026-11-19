import threading
import webbrowser
import time
import sys
import os
import socket
from app import app

def find_free_port():
    """Ask the OS for an available port."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    port = s.getsockname()[1]
    s.close()
    return port

# Get a free port dynamically
PORT = find_free_port()

def open_browser():
    # Wait 1.5 seconds to make sure Flask is running
    time.sleep(1.5)
    webbrowser.open(f"http://127.0.0.1:{PORT}")

if __name__ == "__main__":
    # Start the browser opener in a separate thread
    threading.Thread(target=open_browser, daemon=True).start()
    
    # Start Flask app on the free port we found
    app.run(host="127.0.0.1", port=PORT, debug=False, threaded=True)