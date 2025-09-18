#!/usr/bin/env python3
"""
Simple local development server for SunshineCTF website.
This script serves the website locally so that absolute paths work correctly.
"""

import http.server
import socketserver
import os
import sys
import webbrowser
from pathlib import Path

# Configuration
PORT = 8000
HOST = 'localhost'

def main():
    # Change to the script's directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Check if index.html exists
    if not (script_dir / 'index.html').exists():
        print("Error: index.html not found in current directory")
        sys.exit(1)
    
    # Create a custom handler that serves index.html for root path
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.path = '/index.html'
            return super().do_GET()
    
    # Start the server
    try:
        with socketserver.TCPServer((HOST, PORT), CustomHandler) as httpd:
            url = f"http://{HOST}:{PORT}"
            print(f"SunshineCTF local server starting...")
            print(f"Server running at: {url}")
            print(f"Serving directory: {script_dir}")
            print("\nPress Ctrl+C to stop the server")
            print("-" * 50)
            
            # Try to open the browser automatically
            try:
                webbrowser.open(url)
                print(f"Opened {url} in your default browser")
            except Exception as e:
                print(f"Could not open browser automatically: {e}")
                print(f"Please manually open: {url}")
            
            print("-" * 50)
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\nServer stopped by user")
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"Error: Port {PORT} is already in use")
            print("Try running: lsof -ti:8000 | xargs kill")
            print("Or use a different port by modifying the PORT variable in this script")
        else:
            print(f"Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
