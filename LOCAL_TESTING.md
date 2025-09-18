# Local Testing Guide

This guide explains how to test the SunshineCTF website locally.

## Problem

The website uses absolute paths (starting with `/`) for CSS, JavaScript, and image resources. When opening `index.html` directly in a browser using the `file://` protocol, these resources fail to load because there's no web server to serve them.

## Solution

Use the provided Python script to serve the website locally with a proper HTTP server.

## Quick Start

1. **Run the local server:**
   ```bash
   python3 serve.py
   ```
   
   Or if you prefer:
   ```bash
   ./serve.py
   ```

2. **The server will:**
   - Start on `http://localhost:8000`
   - Automatically open your browser to the site
   - Serve all resources with correct paths

3. **Stop the server:**
   - Press `Ctrl+C` in the terminal

## What the Script Does

- Serves the website using Python's built-in HTTP server
- Handles absolute paths correctly (e.g., `/css/style.css` → `./css/style.css`)
- Automatically opens your browser to the local site
- Provides clear status messages and error handling

## Troubleshooting

- **Port already in use:** If port 8000 is busy, modify the `PORT` variable in `serve.py`
- **Browser doesn't open:** Manually navigate to `http://localhost:8000`
- **Resources not loading:** Make sure you're accessing via `http://localhost:8000`, not opening the file directly

## Requirements

- Python 3 (usually pre-installed on Linux/macOS)
- No additional packages required
