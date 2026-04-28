"""
Slack Client — sends structured call summaries to a brokerage's Slack channel
via their configured Incoming Webhook URL.

No Slack SDK needed — just an HTTPS POST.
"""

import logging

import httpx

logger = logging.getLogger("pas.slack")


async def send_call_summary(webhook_url: str, summary: str, outcome: str, lead: dict, duration_seconds: int):
    if not webhook_url:
        return

    outcome_emoji = "✅" if outcome == "booked" else "❌"
    outcome_label = "BOOKED" if outcome == "booked" else "NOT BOOKED"

    name = lead.get("name") or "Unknown"
    phone = lead.get("phone_number", "")
    email = lead.get("email", "") or "—"
    intent = lead.get("intent", "") or "—"
    budget = lead.get("budget", "") or "—"
    timeline = lead.get("timeline", "") or "—"
    slot = lead.get("booking_slot", "")
    minutes = duration_seconds // 60
    seconds = duration_seconds % 60

    blocks = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": f"{outcome_emoji} Call Summary — {outcome_label}"}
        },
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": f"*Lead*\n{name}"},
                {"type": "mrkdwn", "text": f"*Phone*\n{phone}"},
                {"type": "mrkdwn", "text": f"*Email*\n{email}"},
                {"type": "mrkdwn", "text": f"*Duration*\n{minutes}m {seconds}s"},
                {"type": "mrkdwn", "text": f"*Looking to*\n{intent}"},
                {"type": "mrkdwn", "text": f"*Budget*\n{budget}"},
                {"type": "mrkdwn", "text": f"*Timeline*\n{timeline}"},
                {"type": "mrkdwn", "text": f"*Viewing booked*\n{slot or '—'}"},
            ]
        },
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"*Summary*\n{summary}"}
        },
        {"type": "divider"},
    ]

    await _post_to_slack(webhook_url, blocks)


async def send_agent_reminder(webhook_url: str, agent_name_or_mention: str, lead: dict, slot_readable: str):
    """Notify the agent in Slack about the upcoming viewing appointment."""
    if not webhook_url:
        return

    name = lead.get("name") or "a prospect"
    phone = lead.get("phone_number", "")
    intent = lead.get("intent", "") or "property"
    budget = lead.get("budget", "")
    notes = lead.get("property_interest", "")

    text = (
        f"📅 *New Viewing Booked* — {agent_name_or_mention}\n\n"
        f"*Client:* {name} ({phone})\n"
        f"*When:* {slot_readable}\n"
        f"*Looking to:* {intent}"
        + (f" | Budget: {budget}" if budget else "")
        + (f"\n*Notes:* {notes}" if notes else "")
    )

    blocks = [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": text}
        }
    ]
    await _post_to_slack(webhook_url, blocks)


async def send_slack_message(webhook_url: str, text: str):
    """Simple text message — used for command responses."""
    if not webhook_url:
        return
    await _post_to_slack(webhook_url, [{"type": "section", "text": {"type": "mrkdwn", "text": text}}])


async def _post_to_slack(webhook_url: str, blocks: list):
    try:
        async with httpx.AsyncClient(timeout=6.0) as client:
            resp = await client.post(webhook_url, json={"blocks": blocks})
            resp.raise_for_status()
            logger.info("Slack message sent")
    except Exception as e:
        logger.error(f"Slack send failed: {e}")
