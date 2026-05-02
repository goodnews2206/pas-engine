"""
Call Summary Generator — produces a concise, structured summary of each call
for the brokerage's Slack channel and call record.

Routes through the LLM provider abstraction (factory.get_provider) so the
underlying model (Claude, OpenAI, …) is swappable via LLM_PROVIDER. Falls
back to a deterministic template summary if no provider is available or
the call fails — summary generation must never break call finalization.
"""

import logging

from app.db.event_logger import log_event_bg
from app.services.llm.factory import get_provider

logger = logging.getLogger("pas.summary")

_SYSTEM = """You summarise real estate qualification calls for a brokerage's internal dashboard.
Write 2–4 sentences. Be direct and factual. No filler.
Cover: what the lead said they want, any objections raised, the outcome, and next step."""


async def generate_call_summary(
    transcript: str,
    outcome: str,
    lead: dict,
    duration_seconds: int,
) -> str:
    name = lead.get("name") or "Lead"
    intent = lead.get("intent") or "unknown intent"
    budget = lead.get("budget") or "not specified"
    timeline = lead.get("timeline") or "not specified"
    slot = lead.get("booking_slot") or ""

    user_msg = (
        f"Call outcome: {outcome}\n"
        f"Lead: {name} | Intent: {intent} | Budget: {budget} | Timeline: {timeline}\n"
        + (f"Viewing booked for: {slot}\n" if slot else "")
        + f"Duration: {duration_seconds}s\n\n"
        f"Transcript:\n{transcript or '(no transcript)'}"
    )

    provider = get_provider()
    if provider is None:
        logger.warning("No LLM provider available — using template summary")
        return _template_summary(outcome, lead)

    try:
        text = await provider.chat(
            system=_SYSTEM,
            user=user_msg,
            max_tokens=200,
            temperature=0.2,
            purpose="summary",
        )
        return text or _template_summary(outcome, lead)
    except Exception as e:
        logger.warning(f"[{provider.name}] summary failed, using template: {e}")
        log_event_bg(
            "provider.failed",
            event_category="llm",
            event_source="call_summary",
            provider=provider.name,
            severity="warning",
            payload={
                "purpose": "summary",
                "error_class": type(e).__name__,
                "message_excerpt": str(e)[:300],
            },
        )
        return _template_summary(outcome, lead)


def _template_summary(outcome: str, lead: dict) -> str:
    name = lead.get("name") or "Lead"
    intent = lead.get("intent") or "unknown"
    budget = lead.get("budget") or "not specified"
    timeline = lead.get("timeline") or "not specified"
    slot = lead.get("booking_slot")

    result = (
        f"{name} called regarding {intent}. Budget: {budget}. Timeline: {timeline}. "
        f"Outcome: {outcome.replace('_', ' ')}."
    )
    if slot:
        result += f" Viewing booked for {slot}."
    return result
