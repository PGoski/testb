---
name: Clawbrowser Integration
description: Use this skill when the user asks about Clawbrowser, fingerprint-managed browsers, browser fingerprinting, CDP browser automation with identity management, launching browser profiles, proxy routing, or connecting AI agents to anti-detect browsers. Trigger phrases include "clawbrowser", "fingerprint profile", "browser identity", "CDP connect", "anti-detect browser".
version: 1.0.0
---

# Clawbrowser — AI Agent Integration

## Overview

Clawbrowser is a fingerprint-managed browser providing unique browser identities and proxy routing. AI agents connect via standard CDP (Chrome DevTools Protocol) using Playwright or Puppeteer. All fingerprint spoofing and proxy routing is transparent — agents interact with a normal browser.

## Quick Start

### 1. Set API Key

```bash
export CLAWBROWSER_API_KEY=clawbrowser_xxxxx
```

Or write the config file:

```bash
mkdir -p ~/.clawbrowser
cat > ~/.clawbrowser/config <<EOF
{
  "api_key": "clawbrowser_xxxxx"
}
EOF
```

### 2. Launch Browser with a Fingerprint Profile

```bash
clawbrowser --fingerprint=my_agent_profile --remote-debugging-port=9222
```

On first use, Clawbrowser detects the profile doesn't exist, calls the backend API to generate a fingerprint, saves it locally, and launches with full identity spoofing and proxy routing.

Subsequent launches with the same profile ID reuse the cached fingerprint — same identity, same cookies, same session state.

### 3. Connect Your Agent

**Playwright (Python):**

```python
from playwright.async_api import async_playwright

async with async_playwright() as p:
    browser = await p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    page = browser.contexts[0].pages[0]
    await page.goto("https://example.com")
    content = await page.content()
```

**Playwright (Node.js):**

```javascript
const { chromium } = require('playwright');

const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const page = browser.contexts()[0].pages()[0];
await page.goto('https://example.com');
```

**Puppeteer:**

```javascript
const puppeteer = require('puppeteer');

const browser = await puppeteer.connect({ browserURL: 'http://127.0.0.1:9222' });
const [page] = await browser.pages();
await page.goto('https://example.com');
```

## CLI Reference

```bash
# Launch with fingerprint profile
clawbrowser --fingerprint=<profile_id>

# Launch with CDP port for automation
clawbrowser --fingerprint=<profile_id> --remote-debugging-port=9222

# Launch in headless mode
clawbrowser --fingerprint=<profile_id> --headless

# Launch vanilla (no fingerprint, no proxy)
clawbrowser

# List all local profiles
clawbrowser --list

# Regenerate a fingerprint (new identity, preserves cookies/history)
clawbrowser --fingerprint=<profile_id> --regenerate
```

## Stdout Modes

### Default (clean)
Suppresses Chromium noise. Only outputs clawbrowser status messages.

### JSON mode (for machine consumption)
```bash
clawbrowser --fingerprint=my_agent_profile --output=json
```

Parse the `ready` event to know when the browser is available:
```json
{"event":"ready"}
```

### Verbose mode (debugging)
```bash
clawbrowser --fingerprint=my_agent_profile --verbose
```

## Multi-Profile Management

Each profile is a complete browser identity with unique fingerprint, separate proxy, and isolated browser state. Run multiple profiles simultaneously on different ports:

```bash
clawbrowser --fingerprint=agent_us_1 --remote-debugging-port=9222 &
clawbrowser --fingerprint=agent_de_1 --remote-debugging-port=9223 &
clawbrowser --fingerprint=agent_uk_1 --remote-debugging-port=9224 &
```

## Important Rules for AI Agents

- **Reuse profiles** for session continuity — cookies and login state persist across launches
- **Use `--output=json`** to programmatically detect when the browser is ready
- **One proxy per session** — proxy does not rotate mid-session
- **Do NOT override fingerprint properties via CDP** — Clawbrowser handles all spoofing at the engine level. CDP-level overrides create detectable inconsistencies
- **Use descriptive profile IDs** like `us_residential_1`, `de_scraper_main`

## Error Handling

Monitor stdout or JSON events for errors. On error, the process exits with a non-zero exit code:

```
[clawbrowser] Error: CLAWBROWSER_API_KEY not set
[clawbrowser] Error: cannot reach fingerprint API
[clawbrowser] Error: proxy connection failed
[clawbrowser] Error: fingerprint verification failed
[clawbrowser] Error: out of credits, please top up at clawbrowser.ai
```
