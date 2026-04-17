---
description: Regenerate a Clawbrowser fingerprint profile (new identity, preserves cookies/history)
argument-hint: "<profile_id>"
allowed-tools: ["Bash(clawbrowser:*)", "Bash(./clawbrowser:*)", "Bash(./Chromium.app/*:*)"]
---

## Your Task

Regenerate the fingerprint for an existing Clawbrowser profile. This assigns a new browser identity while preserving cookies, localStorage, and history.

If no profile ID is provided in the arguments, ask the user which profile to regenerate.

Detect the platform and run:

- **macOS**: `./Chromium.app/Contents/MacOS/Chromium --fingerprint=<profile_id> --regenerate`
- **Linux**: `./clawbrowser --fingerprint=<profile_id> --regenerate`

Report the result to the user.
