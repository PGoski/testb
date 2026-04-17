---
description: Launch a Clawbrowser fingerprint profile with CDP for automation
argument-hint: "[profile_id] [--port PORT] [--headless]"
allowed-tools: ["Bash(clawbrowser:*)", "Bash(./clawbrowser:*)", "Bash(./Chromium.app/*:*)"]
---

## Context

- OS: !`uname -s`
- Architecture: !`uname -m`
- Existing profiles: !`clawbrowser --list 2>/dev/null || echo "clawbrowser not in PATH — check local directory"`

## Your Task

Launch a Clawbrowser instance with a fingerprint profile and CDP enabled for agent automation.

**Parse the user's arguments:**
- If a profile ID is provided, use it. Otherwise, ask the user for one.
- If `--port` is specified, use that port. Default: `9222`.
- If `--headless` is specified, add the `--headless` flag.

**Determine the binary path:**
- On macOS: look for `./Chromium.app/Contents/MacOS/Chromium` or `Chromium.app` in common locations
- On Linux: look for `./clawbrowser` or `clawbrowser` in PATH

**Launch command pattern:**
```
<binary> --fingerprint=<profile_id> --remote-debugging-port=<port> --output=json [--headless]
```

Monitor the JSON output. Once you see `{"event":"ready"}`, report success to the user with the CDP URL.

If any error events appear, report the error and suggest fixes based on the error message.
