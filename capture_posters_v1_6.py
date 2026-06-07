"""
Local-use helper for v1.6 poster screenshot automation.
Requires Playwright on your own machine:

    pip install playwright
    playwright install

Then run:
    python capture_posters_v1_6.py
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
SITE_ROOT = ROOT.as_uri() + '/'
PAGES = [
    ('new-and-updated.html', 'assets/images/new-and-updated.png'),
    ('back-in-rotation.html', 'assets/images/back-in-rotation.png'),
]
VIEWPORT = {"width": 1400, "height": 2200}

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport=VIEWPORT, device_scale_factor=1)
    for html_name, out_name in PAGES:
        page.goto(SITE_ROOT + html_name, wait_until='networkidle')
        page.screenshot(path=str(ROOT / out_name), full_page=True)
        print(f'Saved {out_name}')
    browser.close()
