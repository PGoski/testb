import logging
from pathlib import Path
from . import schemas, tools

logger = logging.getLogger(__name__)


def _clawbrowser_context(session_id, user_message, is_first_turn, **kwargs):
    """Inject Clawbrowser guidance on first turn if the user mentions browsers."""
    if not is_first_turn:
        return None

    keywords = ["clawbrowser", "fingerprint", "browser profile", "cdp", "anti-detect"]
    msg_lower = user_message.lower()
    if not any(kw in msg_lower for kw in keywords):
        return None

    return {
        "context": (
            "Clawbrowser is available. Key rules:\n"
            "- Launch profiles with clawbrowser_launch, reuse profile IDs for session continuity\n"
            "- Do NOT override fingerprint properties via CDP — Clawbrowser handles spoofing at engine level\n"
            "- Use --output=json to detect when the browser is ready\n"
            "- One proxy per session — proxy does not rotate mid-session"
        ),
    }


def register(ctx):
    """Wire Clawbrowser tools, hooks, and skills."""
    ctx.register_tool(
        name="clawbrowser_launch",
        toolset="clawbrowser",
        schema=schemas.CLAWBROWSER_LAUNCH,
        handler=tools.clawbrowser_launch,
    )
    ctx.register_tool(
        name="clawbrowser_list_profiles",
        toolset="clawbrowser",
        schema=schemas.CLAWBROWSER_LIST_PROFILES,
        handler=tools.clawbrowser_list_profiles,
    )
    ctx.register_tool(
        name="clawbrowser_connect_info",
        toolset="clawbrowser",
        schema=schemas.CLAWBROWSER_CONNECT_INFO,
        handler=tools.clawbrowser_connect_info,
    )
    ctx.register_tool(
        name="clawbrowser_regenerate",
        toolset="clawbrowser",
        schema=schemas.CLAWBROWSER_REGENERATE,
        handler=tools.clawbrowser_regenerate,
    )

    ctx.register_hook("pre_llm_call", _clawbrowser_context)

    # Register bundled skill
    skills_dir = Path(__file__).parent / "skills"
    for child in sorted(skills_dir.iterdir()):
        skill_md = child / "SKILL.md"
        if child.is_dir() and skill_md.exists():
            ctx.register_skill(child.name, skill_md)

    logger.info("Clawbrowser plugin registered")
