# Clawbrowser Installation

> **Agent: do NOT use a browser to fetch URLs in this guide. Use `curl` in the terminal for all downloads.**

## Step 1: Detect platform and download

> **Agent: do NOT ask the user which platform they are on.** Run the script below — it auto-detects the OS and architecture.

Run this single script to detect the platform and download the correct binary:

```bash
OS=$(uname -s)
ARCH=$(uname -m)
case "$OS" in Linux) OS="linux";; Darwin) OS="macos";; esac
case "$ARCH" in x86_64) ARCH="x64";; aarch64|arm64) ARCH="arm64";; esac
echo "Detected platform: ${OS}-${ARCH}"

curl -L -o clawbrowser.tar.gz \
  "https://github.com/PGoski/testb/releases/download/v1.0.0/cb-${OS}-${ARCH}.tar.gz"
```

Available assets on the [v1.0.0 release](https://github.com/PGoski/testb/releases/tag/v1.0.0):

| Platform    | Asset                    |
|-------------|--------------------------|
| Linux x64   | `cb-linux-x64.tar.gz`   |
| Linux ARM64 | `cb-linux-arm64.tar.gz` |
| macOS ARM64 | `cb-macos-arm64.tar.gz` |

## Step 2: Extract

Extract the archive into the current directory:

```bash
tar xzf clawbrowser.tar.gz
rm clawbrowser.tar.gz
```

On macOS this will produce a `Chromium.app` bundle. On Linux this will produce a `clawbrowser` binary.

## Step 3: Clawbrowser Skill

Download the [SKILL.md](https://github.com/PGoski/testb/blob/main/SKILL.md) file and install it as a skill for your agent. This skill provides the agent with full usage instructions and CLI reference for Clawbrowser.

```bash
curl -L -o SKILL.md \
  "https://raw.githubusercontent.com/PGoski/testb/main/SKILL.md"
```

Then install the skill in your agent's configuration so it can be used alongside the browser.

## Step 4: Verify the binary launches

> **Human action required.** This step may need manual intervention — the agent cannot complete it autonomously. Ask the user to run the command and confirm the result.

### macOS

```bash
./Chromium.app/Contents/MacOS/Chromium --version
```

If blocked by Gatekeeper (*"cannot be opened because it is from an unidentified developer"*), ask the user to do one of the following:

**Option A — System Settings (requires user interaction):**

1. Open **System Settings > Privacy & Security**.
2. Scroll to the **Security** section — there will be a message about `Chromium` being blocked.
3. Click **Allow Anyway**.
4. Re-run the version command and confirm the prompt.

**Option B — Remove quarantine attribute:**

```bash
xattr -rd com.apple.quarantine Chromium.app
```

Then re-run the version command.

### Linux

```bash
./clawbrowser --version
```

If permission denied, run:

```bash
chmod +x ./clawbrowser
```

Then re-run `./clawbrowser --version`.

---

After the user confirms a successful version output, proceed to Step 5.

## Step 5: Configure API Key

The API key is **required**. All operations that contact the Clawbrowser backend (fingerprint generation, proxy assignment, profile creation) will fail without it.

Ask the user in chat for their Clawbrowser API key. They can get it at [clawbrowser.ai/dashboard](https://clawbrowser.ai/dashboard).

Once the user provides the key, write the config file directly:

```bash
mkdir -p ~/.clawbrowser
cat > ~/.clawbrowser/config <<EOF
{
  "api_key": "<user_provided_api_key>"
}
EOF
```

> **Do NOT run the browser binary to set the API key.** Write the config file directly as shown above.

## Step 6: Verify installation

```bash
# macOS
./Chromium.app/Contents/MacOS/Chromium --fingerprint=test_profile --remote-debugging-port=9222 --output=json

# Linux
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

If the `ready` event appears, the installation is complete.
