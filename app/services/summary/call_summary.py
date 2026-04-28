"""
Call Summary Generator — uses Claude to produce a concise, structured summary
of each call for the brokerage's Slack channel and call record.
Falls back to a template summary if Claude is unavailable.
"""

import logging

import anthropic

from app.config import get_settings

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
    try:
        settings = get_settings()
        client = anthropic.AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)

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

        resp = await client.messages.create(
            model="claude-haiku-4-5-20251001",  # fast + cheap for summaries
            max_tokens=200,
            temperature=0.2,
            system=_SYSTEM,
            messages=[{"role": "user", "content": user_msg}],
        )
        return resp.content[0].text.strip()

    except Exception as e:
        logger.warning(f"Claude summary failed, using template: {e}")
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
