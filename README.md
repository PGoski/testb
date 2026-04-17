# Clawbrowser

Fingerprint-managed browser for AI agents. Unique browser identities, proxy routing, and CDP automation — all transparent to the agent.

## Supported Platforms

| Platform | Config |
|----------|--------|
| Claude Code | `.claude-plugin/` |
| Hermes Agent | `.hermes-plugin/` |

## Install

Paste this into your AI agent chat:

```
Check file and install https://raw.githubusercontent.com/PGoski/testb/refs/heads/main/INSTALL.md
```

## Repo Structure

```
├── SKILL.md                     # Shared skill — full CLI reference & usage guide
├── INSTALL.md                   # Installation instructions
├── README.md
├── .claude-plugin/              # Claude Code integration
│   ├── plugin.json
│   └── commands/
│       ├── launch.md
│       ├── list-profiles.md
│       ├── connect.md
│       └── regenerate.md
├── .hermes-plugin/              # Hermes Agent integration
│   ├── plugin.yaml
│   ├── __init__.py
│   ├── schemas.py
│   ├── tools.py
│   └── skills/
│       └── clawbrowser/
│           └── SKILL.md
└── cb/                          # Pre-built binaries
```
