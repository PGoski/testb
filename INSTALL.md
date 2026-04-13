# Clawbrowser Installation

## Step 1: Download

Download the correct binary for your platform from the [v1.0.0 release](https://github.com/PGoski/testb/releases/tag/v1.0.0):

| Platform    | Asset                    |
|-------------|--------------------------|
| Linux x64   | `cb-linux-x64.tar.gz`   |
| Linux ARM64 | `cb-linux-arm64.tar.gz` |
| macOS ARM64 | `cb-macos-arm64.tar.gz` |

```bash
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)
case "$ARCH" in x86_64) ARCH="x64";; aarch64|arm64) ARCH="arm64";; esac

curl -L -o clawbrowser.tar.gz \
  "https://github.com/PGoski/testb/releases/download/v1.0.0/cb-${OS}-${ARCH}.tar.gz"
```

## Step 2: Extract

Extract the archive into your workspace directory:

```bash
tar xzf clawbrowser.tar.gz -C /workspace
rm clawbrowser.tar.gz
```

## Step 3: Verify the binary launches

> **Human action required.** This step may need manual intervention — the agent cannot complete it autonomously. Ask the user to run the command and confirm the result.

Run:

```bash
./clawbrowser --version
```

If the version prints successfully, skip ahead to Step 4.

### macOS — Gatekeeper block

The first launch will likely be blocked by Gatekeeper with a dialog: *"clawbrowser cannot be opened because it is from an unidentified developer."*

Ask the user to do one of the following:

**Option A — System Settings (requires user interaction):**

1. Open **System Settings > Privacy & Security**.
2. Scroll to the **Security** section — there will be a message about `clawbrowser` being blocked.
3. Click **Allow Anyway**.
4. Run `./clawbrowser --version` again and confirm the prompt.

**Option B — Remove quarantine attribute:**

```bash
xattr -d com.apple.quarantine /workspace/clawbrowser
```

Then re-run `./clawbrowser --version`.

### Linux — Permission denied

If the binary is not executable after extraction, ask the user to run:

```bash
chmod +x /workspace/clawbrowser
```

Then re-run `./clawbrowser --version`.

---

After the user confirms a successful version output, proceed to Step 4.

## Step 4: Configure API Key

The API key is **required**. All operations that contact the Clawbrowser backend (fingerprint generation, proxy assignment, profile creation) will fail without it.

Get your key at [clawbrowser.ai/dashboard](https://clawbrowser.ai/dashboard), then configure it:

```bash
./clawbrowser config set api_key <your_api_key>
```

The key is stored in `~/.clawbrowser/config` and used for all subsequent commands.

## Step 5: Verify installation

```bash
./clawbrowser --fingerprint=test_profile --remote-debugging-port=9222 --output=json
```

You should see:

```json
{"event":"profile_loaded","profile_id":"test_profile"}
{"event":"proxy_verified"}
{"event":"fingerprint_verified"}
{"event":"cdp_ready","url":"ws://127.0.0.1:9222"}
{"event":"ready"}
```

If the `ready` event appears, the installation is complete. See [SKILL.md](SKILL.md) for full usage and CLI reference.
