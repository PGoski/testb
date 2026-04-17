---
description: Generate Playwright or Puppeteer code to connect to a running Clawbrowser instance
argument-hint: "[--port PORT] [--lang python|node] [--lib playwright|puppeteer]"
---

## Your Task

Generate connection code for a running Clawbrowser CDP instance.

**Parse arguments:**
- `--port`: CDP port (default: `9222`)
- `--lang`: `python` or `node` (default: `python`)
- `--lib`: `playwright` or `puppeteer` (default: `playwright`)

**Generate the appropriate snippet:**

For **Playwright (Python)**:
```python
from playwright.async_api import async_playwright

async with async_playwright() as p:
    browser = await p.chromium.connect_over_cdp("http://127.0.0.1:<port>")
    page = browser.contexts[0].pages[0]
    await page.goto("https://example.com")
    content = await page.content()
```

For **Playwright (Node.js)**:
```javascript
const { chromium } = require('playwright');

const browser = await chromium.connectOverCDP('http://127.0.0.1:<port>');
const page = browser.contexts()[0].pages()[0];
await page.goto('https://example.com');
```

For **Puppeteer**:
```javascript
const puppeteer = require('puppeteer');

const browser = await puppeteer.connect({ browserURL: 'http://127.0.0.1:<port>' });
const [page] = await browser.pages();
await page.goto('https://example.com');
```

Present the code to the user and remind them:
- Do NOT override fingerprint properties via CDP — Clawbrowser handles all spoofing at the engine level
- The browser must already be running (use `/clawbrowser:launch` first)
