# Clawbrowser

Fingerprint-managed browser for AI agents. Unique browser identities, proxy routing, and CDP automation — all transparent to the agent.

## Supported Platforms

| Platform | Config |
|----------|--------|
| Claude Code | `.claude-plugin/` |
| Hermes Agent | `.hermes-plugin/` |

## Install

```
/plugin marketplace add PGoski/testb            # Claude Code (step 1)
/plugin install clawbrowser@clawbrowser         # Claude Code (step 2)
hermes install github.com/PGoski/testb          # Hermes
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
├── .claude-plugin/              # Claude Code marketplace
│   └── marketplace.json
├── plugins/
│   └── clawbrowser/
│       └── .claude-plugin/
│           └── plugin.json      # References ../../SKILL.md
└── .hermes-plugin/              # Hermes Agent integration
    ├── plugin.yaml
    ├── __init__.py
    ├── schemas.py
    └── tools.py
```
