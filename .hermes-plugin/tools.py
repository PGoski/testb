import json
import os
import platform
import shutil
import subprocess


def _find_binary():
    """Locate the clawbrowser binary."""
    # Check PATH first
    which = shutil.which("clawbrowser")
    if which:
        return which

    system = platform.system()
    if system == "Darwin":
        candidates = [
            "./Chromium.app/Contents/MacOS/Chromium",
            os.path.expanduser("~/Chromium.app/Contents/MacOS/Chromium"),
        ]
    else:
        candidates = [
            "./clawbrowser",
            os.path.expanduser("~/clawbrowser"),
        ]

    for path in candidates:
        if os.path.isfile(path) and os.access(path, os.X_OK):
            return path

    return None


def clawbrowser_launch(args: dict, **kwargs) -> str:
    """Launch a Clawbrowser profile with CDP enabled."""
    profile_id = args.get("profile_id", "").strip()
    if not profile_id:
        return json.dumps({"error": "No profile_id provided"})

    binary = _find_binary()
    if not binary:
        return json.dumps({
            "error": "Clawbrowser binary not found",
            "hint": "Install from https://github.com/PGoski/testb/blob/main/INSTALL.md",
        })

    port = args.get("port", 9222)
    headless = args.get("headless", False)

    cmd = [
        binary,
        f"--fingerprint={profile_id}",
        f"--remote-debugging-port={port}",
        "--output=json",
    ]
    if headless:
        cmd.append("--headless")

    try:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        # Read events until ready or error (timeout after 30s)
        import select
        import time

        events = []
        deadline = time.monotonic() + 30

        while time.monotonic() < deadline:
            remaining = deadline - time.monotonic()
            ready, _, _ = select.select([proc.stdout], [], [], min(remaining, 1.0))
            if ready:
                line = proc.stdout.readline()
                if not line:
                    break
                line = line.strip()
                if line:
                    try:
                        event = json.loads(line)
                        events.append(event)
                        if event.get("event") == "ready":
                            return json.dumps({
                                "status": "running",
                                "profile_id": profile_id,
                                "cdp_url": f"http://127.0.0.1:{port}",
                                "pid": proc.pid,
                                "events": events,
                            })
                        if "error" in event.get("event", "").lower():
                            proc.terminate()
                            return json.dumps({
                                "error": f"Launch failed: {line}",
                                "events": events,
                            })
                    except json.JSONDecodeError:
                        events.append({"raw": line})

            if proc.poll() is not None:
                break

        # Timeout or process exited
        stderr = proc.stderr.read() if proc.stderr else ""
        if proc.poll() is not None and proc.returncode != 0:
            return json.dumps({
                "error": f"Process exited with code {proc.returncode}",
                "stderr": stderr,
                "events": events,
            })

        return json.dumps({
            "error": "Timeout waiting for browser ready event",
            "events": events,
        })

    except Exception as e:
        return json.dumps({"error": f"Failed to launch: {e}"})


def clawbrowser_list_profiles(args: dict, **kwargs) -> str:
    """List all local fingerprint profiles."""
    binary = _find_binary()
    if not binary:
        return json.dumps({
            "error": "Clawbrowser binary not found",
            "hint": "Install from https://github.com/PGoski/testb/blob/main/INSTALL.md",
        })

    try:
        result = subprocess.run(
            [binary, "--list"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode != 0:
            return json.dumps({
                "error": f"Exit code {result.returncode}",
                "stderr": result.stderr.strip(),
            })
        return json.dumps({
            "profiles": result.stdout.strip(),
        })
    except Exception as e:
        return json.dumps({"error": f"Failed to list profiles: {e}"})


def clawbrowser_connect_info(args: dict, **kwargs) -> str:
    """Return CDP connection details and code snippets."""
    port = args.get("port", 9222)
    library = args.get("library", "playwright-python")
    cdp_url = f"http://127.0.0.1:{port}"

    snippets = {
        "playwright-python": (
            "from playwright.async_api import async_playwright\n\n"
            "async with async_playwright() as p:\n"
            f'    browser = await p.chromium.connect_over_cdp("{cdp_url}")\n'
            "    page = browser.contexts[0].pages[0]\n"
            '    await page.goto("https://example.com")\n'
            "    content = await page.content()"
        ),
        "playwright-node": (
            "const { chromium } = require('playwright');\n\n"
            f"const browser = await chromium.connectOverCDP('{cdp_url}');\n"
            "const page = browser.contexts()[0].pages()[0];\n"
            "await page.goto('https://example.com');"
        ),
        "puppeteer": (
            "const puppeteer = require('puppeteer');\n\n"
            f"const browser = await puppeteer.connect({{ browserURL: '{cdp_url}' }});\n"
            "const [page] = await browser.pages();\n"
            "await page.goto('https://example.com');"
        ),
    }

    return json.dumps({
        "cdp_url": cdp_url,
        "websocket_url": f"ws://127.0.0.1:{port}",
        "library": library,
        "code": snippets.get(library, snippets["playwright-python"]),
        "warning": (
            "Do NOT override fingerprint properties via CDP — "
            "Clawbrowser handles all spoofing at the engine level."
        ),
    })


def clawbrowser_regenerate(args: dict, **kwargs) -> str:
    """Regenerate fingerprint for an existing profile."""
    profile_id = args.get("profile_id", "").strip()
    if not profile_id:
        return json.dumps({"error": "No profile_id provided"})

    binary = _find_binary()
    if not binary:
        return json.dumps({
            "error": "Clawbrowser binary not found",
            "hint": "Install from https://github.com/PGoski/testb/blob/main/INSTALL.md",
        })

    try:
        result = subprocess.run(
            [binary, f"--fingerprint={profile_id}", "--regenerate"],
            capture_output=True,
            text=True,
            timeout=15,
        )
        if result.returncode != 0:
            return json.dumps({
                "error": f"Exit code {result.returncode}",
                "stderr": result.stderr.strip(),
            })
        return json.dumps({
            "status": "regenerated",
            "profile_id": profile_id,
            "output": result.stdout.strip(),
        })
    except Exception as e:
        return json.dumps({"error": f"Failed to regenerate: {e}"})
