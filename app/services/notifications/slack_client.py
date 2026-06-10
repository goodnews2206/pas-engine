"""
Slack Client — sends structured call summaries to a brokerage's Slack channel
via their configured Incoming Webhook URL.

No Slack SDK needed — just an HTTPS POST.
"""

import logging

import httpx

from app.services.security.pii_safety import redact_pii, sanitize_slack_payload

logger = logging.getLogger("pas.slack")


def _safe_err(err: Exception, webhook_url: str) -> str:
    """PAS211I: scrub the webhook URL (a bearer-secret) and any secret-shaped
    token out of an exception string before it is logged."""
    msg = str(err)
    if webhook_url:
        msg = msg.replace(webhook_url, "[slack-webhook]")
    return redact_pii(msg)


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
    # PAS211I: strip secret-shaped tokens from the payload before it leaves PAS.
    # Lead contact details (name/phone/email) are an intentional operational
    # handoff and are preserved; only secret-like values are redacted.
    safe_blocks = sanitize_slack_payload(blocks)
    try:
        async with httpx.AsyncClient(timeout=6.0) as client:
            resp = await client.post(webhook_url, json={"blocks": safe_blocks})
            resp.raise_for_status()
            logger.info("Slack message sent")
    except Exception as e:
        # PAS211I: never let the webhook URL or a token reach the logs via the
        # exception string (httpx echoes the request URL on errors).
        logger.error(f"Slack send failed: {_safe_err(e, webhook_url)}")
