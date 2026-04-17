# Clawbrowser Plugin for Claude Code

Launch and manage fingerprint-managed browser profiles directly from Claude Code. Connect AI agents to Clawbrowser via CDP (Chrome DevTools Protocol) with unique browser identities and proxy routing.

## Commands

| Command | Description |
|---------|-------------|
| `/clawbrowser:launch` | Launch a browser profile with CDP enabled |
| `/clawbrowser:list-profiles` | List all local fingerprint profiles |
| `/clawbrowser:connect` | Generate Playwright/Puppeteer connection code |
| `/clawbrowser:regenerate` | Regenerate a profile's fingerprint |

## Skills

- **Clawbrowser Integration** — Loaded automatically when discussing Clawbrowser, browser fingerprinting, or CDP automation. Provides full CLI reference and usage guidance.

## Prerequisites

- Clawbrowser binary installed ([installation guide](https://github.com/PGoski/testb/blob/main/INSTALL.md))
- API key from [clawbrowser.ai/dashboard](https://clawbrowser.ai/dashboard)

## Installation

Copy the `cb-plugin` directory into your Claude Code plugins path, or install from the marketplace if available.
