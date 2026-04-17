---
description: List all local Clawbrowser fingerprint profiles
allowed-tools: ["Bash(clawbrowser:*)", "Bash(./clawbrowser:*)", "Bash(./Chromium.app/*:*)"]
---

## Your Task

List all locally cached Clawbrowser fingerprint profiles.

Detect the platform and run the appropriate command:

- **macOS**: `./Chromium.app/Contents/MacOS/Chromium --list`
- **Linux**: `./clawbrowser --list`

If the binary is not found locally, try `clawbrowser --list` from PATH.

Present the results to the user in a clean format.
