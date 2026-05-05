"""
Lead Alert Dispatcher (PAS134) — orchestrates the email + Slack lead
alert that fires when a call ends in a sales-critical outcome.

This is the single shared implementation called by every call-finalisation
path (simulate, websocket). It is intentionally thin — it picks the
destinations off the brokerage record, asks the formatter for content,
then awaits each transport independently so a failure in one cannot
block the other.

Resolution priority for destinations (forward-compatible with PAS133):
    Email recipients
        1. brokerage.notification_config.email   (list[str], preferred)
        2. brokerage.owner_email                 (legacy single string)
    Slack webhook
        1. brokerage.notification_config.slack_webhook
        2. brokerage.slack_webhook_url           (legacy top-level field)

Never raises. Logs a single summary line per call. Caller may still
wrap the call in their own try/except as defence-in-depth — the
finalisation path must not be affected by notification failures.
"""

import logging
from typing import Optional

from app.config import get_settings
from app.services.notifications.email_sender import send_email_notification
from app.services.notifications.formatter import format_lead_notification
from app.services.notifications.slack_sender import send_slack_notification

logger = logging.getLogger("pas.lead_alerts")


def _resolve_email_recipients(brokerage: dict) -> list[str]:
    nc = (brokerage.get("notification_config") or {}) if brokerage else {}
    raw = nc.get("email")
    if isinstance(raw, list):
        return [e.strip() for e in raw if isinstance(e, str) and e.strip()]
    if isinstance(raw, str) and raw.strip():
        return [raw.strip()]
    owner = (brokerage.get("owner_email") or "").strip()
    return [owner] if owner else []


def _resolve_slack_webhook(brokerage: dict) -> str:
    nc = (brokerage.get("notification_config") or {}) if brokerage else {}
    return (
        (nc.get("slack_webhook") or "").strip()
        or (brokerage.get("slack_webhook_url") or "").strip()
    )


def _build_workflow_url(call_sid: str) -> str:
    base = (get_settings().BASE_URL or "").rstrip("/")
    if not base or not call_sid:
        return ""
    return f"{base}/dashboard/calls/{call_sid}"


async def dispatch_lead_notification(
    *,
    call_sid: str,
    brokerage: dict,
    outcome: str,
    lead: Optional[dict] = None,
) -> dict:
    """
    Format and send the lead alert. Returns a small status dict for the
    caller's logging — never raises.

    The status dict shape:
        {
            "skipped":          bool,    # True when both destinations were missing
            "email_ok":         bool,
            "email_recipients": int,
            "slack_ok":         bool,
            "slack_configured": bool,
        }
    """
    brokerage = brokerage or {}
    recipients = _resolve_email_recipients(brokerage)
    webhook = _resolve_slack_webhook(brokerage)

    status = {
        "skipped": False,
        "email_ok": False,
        "email_recipients": len(recipients),
        "slack_ok": False,
        "slack_configured": bool(webhook),
    }

    if not recipients and not webhook:
        status["skipped"] = True
        logger.info(
            f"[{call_sid}] lead alert skipped — no email or Slack configured "
            f"for brokerage={brokerage.get('id')}"
        )
        return status

    try:
        notif = format_lead_notification({
            "call_id": call_sid,
            "brokerage_id": brokerage.get("id"),
            "outcome": outcome,
            "lead": lead or {},
            "workflow_url": _build_workflow_url(call_sid),
        })
    except Exception as e:
        # Defensive — formatter is pure and shouldn't raise, but a malformed
        # call_data dict shouldn't break the finalisation path.
        logger.warning(f"[{call_sid}] lead alert format failed: {e}")
        return status

    if recipients:
        try:
            status["email_ok"] = await send_email_notification(
                to=recipients,
                subject=notif["subject"],
                body=notif["email_body"],
            )
        except Exception as e:
            logger.warning(f"[{call_sid}] lead alert email leg failed: {e}")

    if webhook:
        try:
            status["slack_ok"] = await send_slack_notification(
                webhook_url=webhook,
                message=notif["slack_message"],
            )
        except Exception as e:
            logger.warning(f"[{call_sid}] lead alert slack leg failed: {e}")

    logger.info(
        f"[{call_sid}] lead alert | outcome={outcome} | "
        f"email_recipients={status['email_recipients']} "
        f"email_ok={status['email_ok']} | "
        f"slack_configured={status['slack_configured']} "
        f"slack_ok={status['slack_ok']}"
    )
    return status
