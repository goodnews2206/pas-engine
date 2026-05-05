"""
Slack Sender (PAS134) — simple text-only Slack messages via Incoming Webhook.

Distinct from app.services.notifications.slack_client which renders rich
Block Kit call summaries and agent reminders. This module is the simple,
single-line transport used by lead alerts.

Contract:
    send_slack_notification(webhook_url: str, message: str) -> bool
        - One HTTPS POST to the Incoming Webhook URL per call.
        - Sends a plain {"text": message} body — Slack will render
          newlines and basic mrkdwn (*bold*, links, etc.).
        - Skips silently (returns False) when webhook_url or message is empty.
        - Never raises. Logs failures and returns False.
"""

import logging

import httpx

logger = logging.getLogger("pas.slack_sender")

_HTTP_TIMEOUT_SECONDS = 6.0


async def send_slack_notification(webhook_url: str, message: str) -> bool:
    """
    Post a single text-only message to a Slack Incoming Webhook.

    Returns True only on 2xx (Slack returns 200 + body 'ok' on success).
    Any other outcome is logged and reported as False.
    """
    if not webhook_url or not isinstance(webhook_url, str):
        logger.info("slack_sender: empty webhook_url — skipping send")
        return False
    if not message:
        logger.info("slack_sender: empty message — skipping send")
        return False

    try:
        async with httpx.AsyncClient(timeout=_HTTP_TIMEOUT_SECONDS) as client:
            resp = await client.post(webhook_url, json={"text": message})
        if 200 <= resp.status_code < 300:
            logger.info("slack_sender: sent")
            return True
        snippet = (resp.text or "")[:200]
        logger.error(
            f"slack_sender: HTTP {resp.status_code} from Slack | body={snippet!r}"
        )
        return False
    except Exception as e:
        logger.error(f"slack_sender: send failed: {e}")
        return False
