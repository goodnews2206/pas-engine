"""
Email Sender (PAS134) — generic outbound email via Resend.

Distinct from app.services.notifications.email_client which holds the
lead-facing booking-confirmation / reminder templates. This module is
the simple, brokerage-facing transport used by lead alerts.

Contract:
    send_email_notification(to: list[str], subject: str, body: str) -> bool
        - One HTTPS POST to Resend's /emails endpoint per call.
        - Sends body as both plain text and a minimal <pre>-wrapped HTML
          version so it renders cleanly in any inbox.
        - Skips silently (returns False) when RESEND_API_KEY is unset or
          when `to` is empty.
        - Never raises. Logs failures and returns False.
"""

import html
import logging
from typing import Sequence

import httpx

from app.config import get_settings

logger = logging.getLogger("pas.email_sender")

_RESEND_API_URL = "https://api.resend.com/emails"
_HTTP_TIMEOUT_SECONDS = 8.0


async def send_email_notification(
    to: Sequence[str],
    subject: str,
    body: str,
) -> bool:
    """
    Send a single notification email to one or more recipients.

    Returns True only on a 2xx response from Resend. Any other outcome
    (missing key, empty recipients, network failure, non-2xx response)
    is logged at a non-fatal level and reported as False — the caller
    must never crash because notifications failed.
    """
    settings = get_settings()

    if not settings.RESEND_API_KEY:
        logger.info("email_sender: RESEND_API_KEY not set — skipping send")
        return False

    recipients = [r.strip() for r in (to or []) if isinstance(r, str) and r.strip()]
    if not recipients:
        logger.info("email_sender: no recipients — skipping send")
        return False

    if not subject:
        subject = "PAS notification"

    text_body = body or ""
    html_body = (
        "<div style=\"font-family:sans-serif;max-width:560px;margin:auto\">"
        f"<pre style=\"white-space:pre-wrap;font-family:inherit;font-size:14px;line-height:1.5\">"
        f"{html.escape(text_body)}"
        "</pre>"
        "<p style=\"margin-top:32px;color:#999;font-size:12px\">PAS by ORVN Labs</p>"
        "</div>"
    )

    payload = {
        "from": settings.FROM_EMAIL,
        "to": recipients,
        "subject": subject,
        "text": text_body,
        "html": html_body,
    }

    try:
        async with httpx.AsyncClient(timeout=_HTTP_TIMEOUT_SECONDS) as client:
            resp = await client.post(
                _RESEND_API_URL,
                headers={
                    "Authorization": f"Bearer {settings.RESEND_API_KEY}",
                    "Content-Type": "application/json",
                },
                json=payload,
            )
        if 200 <= resp.status_code < 300:
            try:
                resend_id = resp.json().get("id")
            except Exception:
                resend_id = None
            logger.info(
                f"email_sender: sent | recipients={len(recipients)} | "
                f"subject={subject!r} | resend_id={resend_id}"
            )
            return True
        # Non-2xx — Resend returns a JSON error body; surface a short snippet.
        snippet = (resp.text or "")[:200]
        logger.error(
            f"email_sender: HTTP {resp.status_code} from Resend | "
            f"recipients={len(recipients)} | body={snippet!r}"
        )
        return False
    except Exception as e:
        logger.error(f"email_sender: send failed (recipients={len(recipients)}): {e}")
        return False
