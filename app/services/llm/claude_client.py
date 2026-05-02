"""
Objection handler — provider-agnostic.

The file is named claude_client.py for backwards compatibility with existing
imports (`from app.services.llm.claude_client import handle_objection`), but
it no longer talks to Anthropic directly. It routes every call through
`app.services.llm.factory.get_provider()` so the underlying LLM (Claude,
OpenAI, …) is swappable via the LLM_PROVIDER env var without touching the
state machine.

Constraints preserved from the original Claude wrapper:
- max_tokens: 100
- temperature: 0.2
- 2 sentences max
- Always steers back toward booking
- Safe canned fallback if no provider is available or the call fails
"""

import logging

from app.db.event_logger import log_event_bg
from app.services.llm.factory import get_provider

logger = logging.getLogger("pas.llm")


OBJECTION_SYSTEM_PROMPT = """You are a professional real estate AI assistant handling a live phone call.
Your ONLY job is to respond to objections and steer the conversation back toward booking a consultation.

Rules:
- Respond in 1-2 sentences maximum
- Be warm, direct, and non-pushy
- Acknowledge the objection briefly, then pivot back
- Never argue or pressure
- End with a soft question that reopens the conversation

Output ONLY the response text. No preamble. No explanation."""

# Canned response used when no LLM provider is available or the call fails.
# Kept identical to the previous Claude wrapper so behavior is unchanged.
_FALLBACK_RESPONSE = (
    "I completely understand — there's no pressure at all. "
    "Would it be okay if I just asked one more quick question before you go?"
)


async def handle_objection(
    objection: str,
    current_state: str,
    lead_context: dict,
    system_prompt_override: str = None,
) -> str:
    """
    Takes the lead's objection and returns a short rebuttal.
    Falls back to a safe canned response if no provider is configured or
    the underlying API call fails.
    """
    context_str = ""
    if lead_context.get("intent"):
        context_str = f"They're interested in {lead_context['intent']}."
    if lead_context.get("budget"):
        context_str += f" Budget: {lead_context['budget']}."

    user_prompt = (
        f"Lead said: \"{objection}\"\n"
        f"Conversation stage: {current_state}\n"
        f"{context_str}\n\n"
        "Respond to this objection and guide them back toward scheduling a consultation."
    )

    provider = get_provider()
    if provider is None:
        logger.warning("No LLM provider available — using canned objection response")
        return _FALLBACK_RESPONSE

    try:
        text = await provider.chat(
            system=system_prompt_override or OBJECTION_SYSTEM_PROMPT,
            user=user_prompt,
            max_tokens=100,
            temperature=0.2,
            purpose="objection",
        )
        logger.info(f"[{provider.name}] objection response: {text!r}")
        return text or _FALLBACK_RESPONSE

    except Exception as e:
        logger.error(f"[{provider.name}] objection call failed: {e}")
        log_event_bg(
            "provider.failed",
            event_category="llm",
            event_source="claude_client",
            provider=provider.name,
            severity="warning",
            payload={
                "purpose": "objection",
                "error_class": type(e).__name__,
                "message_excerpt": str(e)[:300],
            },
        )
        return _FALLBACK_RESPONSE
