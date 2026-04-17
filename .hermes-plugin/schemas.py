CLAWBROWSER_LAUNCH = {
    "name": "clawbrowser_launch",
    "description": (
        "Launch a Clawbrowser fingerprint-managed browser profile with CDP "
        "(Chrome DevTools Protocol) enabled for automation. Creates a new "
        "fingerprint on first use, reuses cached identity on subsequent launches. "
        "Use this when you need a browser with a unique identity and proxy routing."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "profile_id": {
                "type": "string",
                "description": (
                    "Fingerprint profile ID. Use descriptive names like "
                    "'us_residential_1' or 'de_scraper_main'. Reusing an ID "
                    "restores the same identity, cookies, and session state."
                ),
            },
            "port": {
                "type": "integer",
                "description": "CDP remote debugging port (default: 9222)",
            },
            "headless": {
                "type": "boolean",
                "description": "Launch in headless mode (default: false)",
            },
        },
        "required": ["profile_id"],
    },
}

CLAWBROWSER_LIST_PROFILES = {
    "name": "clawbrowser_list_profiles",
    "description": (
        "List all locally cached Clawbrowser fingerprint profiles. Each profile "
        "represents a unique browser identity with its own fingerprint, proxy, "
        "cookies, and session state."
    ),
    "parameters": {
        "type": "object",
        "properties": {},
    },
}

CLAWBROWSER_CONNECT_INFO = {
    "name": "clawbrowser_connect_info",
    "description": (
        "Get connection details and code snippets for connecting to a running "
        "Clawbrowser instance via CDP. Returns Playwright (Python/Node.js) and "
        "Puppeteer connection code. The browser must already be running."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "port": {
                "type": "integer",
                "description": "CDP port the browser is listening on (default: 9222)",
            },
            "library": {
                "type": "string",
                "enum": ["playwright-python", "playwright-node", "puppeteer"],
                "description": "Which library/language to generate connection code for",
            },
        },
    },
}

CLAWBROWSER_REGENERATE = {
    "name": "clawbrowser_regenerate",
    "description": (
        "Regenerate the fingerprint for an existing Clawbrowser profile. "
        "Assigns a new browser identity (canvas, WebGL, navigator, etc.) "
        "while preserving cookies, localStorage, history, and bookmarks."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "profile_id": {
                "type": "string",
                "description": "The profile ID to regenerate",
            },
        },
        "required": ["profile_id"],
    },
}
