---
name: Clawbrowser Integration
description: Full CLI reference and usage guide for Clawbrowser fingerprint-managed browser
version: 1.0.0
---

# Clawbrowser — AI Agent Integration

## Overview

Clawbrowser is a fingerprint-managed browser providing unique browser identities and proxy routing. Connect via standard CDP (Chrome DevTools Protocol) using Playwright or Puppeteer. All fingerprint spoofing and proxy routing is transparent.

## CLI Reference

```bash
clawbrowser --fingerprint=<profile_id>                          # Launch with profile
clawbrowser --fingerprint=<profile_id> --remote-debugging-port=9222  # With CDP
clawbrowser --fingerprint=<profile_id> --headless               # Headless mode
clawbrowser                                                      # Vanilla (no fingerprint)
clawbrowser --list                                               # List profiles
clawbrowser --fingerprint=<profile_id> --regenerate             # New identity, keep state
```

## Output Modes

- **Default**: Clean status messages only
- **JSON** (`--output=json`): Machine-parseable events, wait for `{"event":"ready"}`
- **Verbose** (`--verbose`): Full Chromium logs

## Profile Management

Each profile = unique fingerprint + separate proxy + isolated browser state (cookies, localStorage, history). Run multiple simultaneously on different ports.

## Rules

- Reuse profile IDs for session continuity
- Do NOT override fingerprint properties via CDP
- One proxy per session — no mid-session rotation
- Use descriptive profile IDs (e.g., `us_residential_1`)
