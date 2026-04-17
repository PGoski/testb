# Clawbrowser

Fingerprint-managed browser for AI agents. Unique browser identities, proxy routing, and CDP automation — all transparent to the agent.

## Supported Platforms

| Platform | Config |
|----------|--------|
| Claude Code | `.claude-plugin/` |
| Hermes Agent | `.hermes-plugin/` |

## Install

```
/plugin install github.com/PGoski/testb        # Claude Code
hermes install github.com/PGoski/testb         # Hermes
```

Or paste this into your AI agent chat:

```
Check file and install https://raw.githubusercontent.com/PGoski/testb/refs/heads/main/INSTALL.md
```

## Repo Structure

```
├── SKILL.md                     # Shared skill — full CLI reference & usage guide
├── INSTALL.md                   # Installation instructions
├── README.md
├── .claude-plugin/              # Claude Code integration
│   └── plugin.json
└── .hermes-plugin/              # Hermes Agent integration
    ├── plugin.yaml
    ├── __init__.py
    ├── schemas.py
    └── tools.py
```
