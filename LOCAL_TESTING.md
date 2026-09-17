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

## Retheme verification (2026-09-16)

- Chrome review at 375×812, 768×1024, and 1440×1000: event details, sponsor artwork, and team layout render without horizontal overflow.
- Keyboard checks: visible skip-link focus, focus moves to main content below the fixed header, and the mobile navigation opens/closes with Enter. The Discord link is reachable with Tab and has a visible focus outline.
- No browser console warnings/errors observed; logo and portrait images loaded.
- Local schedule labels retain UTC and add the browser's locale/timezone. Checked Pacific, Eastern, Tokyo, and Kiritimati (next-day rollover), plus an unavailable-Intl fallback. Without JavaScript, the original UTC schedule remains readable.
- Canonical and social URLs use the production domain from `CNAME`; the preview image becomes available at its production URL when this change is deployed.

## Social preview card

The homepage's Open Graph and Twitter metadata share an opaque 1200×630 PNG at `img/sunshinectf26-social.png`. Edit `img/sunshinectf26-social.svg` and regenerate with:

```sh
sh scripts/render-social-card.sh
```

The renderer requires `rsvg-convert`, fontconfig, and `woff2_decompress`. It uses the bundled fonts and existing homepage logo; temporary fonts/cache are removed afterward. Commit the generated PNG so hosting requires no rendering dependencies.

Check image dimensions/opacity, title and description agreement, and that the September 26–28 dates and 14:00 UTC schedule match the event. The metadata follows https://ogp.me/; only the PNG is advertised to social crawlers. Test a fresh link after deployment: existing platform unfurls may retain cached metadata or images.

## Event participation additions (2026-09-16)

- Source checks: https://2026.sunshinectf.org/ confirms in-person kickoff, closing-ceremony awards, and the Monday online finish; `/rules` confirms team participation and private Discord reporting. https://bsidesorlando.org/ confirms September 26 and Full Sail University. The category list matches the five published category leads.
- The supplied BSides artwork is stored unchanged at `img/bsides-orlando-2026.png` (940×470).
- Chrome visual review at 375, 768, and 1440 pixels covered conference artwork, schedule, and participation steps; no horizontal overflow or console warnings/errors observed. Keyboard focus reached the conference/registration and rules links. Exactly two local-time labels remain.
- HTML parsing, asset references, existing link preservation, and unchanged team roster/social metadata checks passed.

Layout refinement: use a centered 520px logo above a full-width event panel. At 992px and wider, dates and challenge details form internal columns; conference copy and art sit side by side. Participation uses three columns from 768px. Checked 375/768/1024/1440px for overflow and exactly two local-time labels, with desktop/mobile visual review. All visible text remains unchanged from the prior copy refinement.
