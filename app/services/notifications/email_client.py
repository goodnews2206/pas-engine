"""
Email notifications via Resend (resend.com).
Uses httpx — no extra library needed.
Silently skips if RESEND_API_KEY is not configured.
"""

import logging

import httpx

from app.config import get_settings

logger = logging.getLogger("pas.email")

RESEND_API_URL = "https://api.resend.com/emails"


async def send_booking_confirmation_email(
    to: str,
    name: str,
    slot_readable: str,
    intent: str,
    budget: str,
    timeline: str,
):
    s = get_settings()
    if not s.RESEND_API_KEY:
        logger.info("RESEND_API_KEY not set — skipping email confirmation")
        return

    subject = "Your Property Viewing is Confirmed — ORVN Realty"
    html = f"""
    <div style="font-family:sans-serif;max-width:560px;margin:auto">
      <h2 style="color:#1a1a1a">You're booked, {name or 'there'}!</h2>
      <p>Your property viewing with <strong>ORVN Realty</strong> is confirmed.</p>
      <table style="border-collapse:collapse;width:100%;margin:24px 0">
        <tr><td style="padding:8px 0;color:#555">Date &amp; Time</td>
            <td style="padding:8px 0;font-weight:bold">{slot_readable}</td></tr>
        <tr><td style="padding:8px 0;color:#555">Looking to</td>
            <td style="padding:8px 0">{intent or '—'}</td></tr>
        <tr><td style="padding:8px 0;color:#555">Budget</td>
            <td style="padding:8px 0">{budget or '—'}</td></tr>
        <tr><td style="padding:8px 0;color:#555">Timeline</td>
            <td style="padding:8px 0">{timeline or '—'}</td></tr>
      </table>
      <p style="color:#555">Your agent will be in touch before the viewing.
         If you need to reschedule, just reply to this email.</p>
      <p style="margin-top:32px;color:#999;font-size:12px">ORVN Realty · Powered by PAS</p>
    </div>
    """

    await _send_email(to=to, subject=subject, html=html)


async def send_reminder_email(to: str, name: str, slot_readable: str, hours_before: int):
    s = get_settings()
    if not s.RESEND_API_KEY:
        return

    when = "tomorrow" if hours_before == 24 else "in 1 hour"
    subject = f"Reminder: Your Property Viewing is {when.title()} — ORVN Realty"
    html = f"""
    <div style="font-family:sans-serif;max-width:560px;margin:auto">
      <h2 style="color:#1a1a1a">Just a reminder, {name or 'there'}</h2>
      <p>Your property viewing with <strong>ORVN Realty</strong> is <strong>{when}</strong>
         — <strong>{slot_readable}</strong>.</p>
      <p style="color:#555">Your agent will meet you at the property. See you soon!</p>
      <p style="margin-top:32px;color:#999;font-size:12px">ORVN Realty · Powered by PAS</p>
    </div>
    """
    await _send_email(to=to, subject=subject, html=html)


async def _send_email(to: str, subject: str, html: str):
    s = get_settings()
    try:
        async with httpx.AsyncClient(timeout=8.0) as client:
            resp = await client.post(
                RESEND_API_URL,
                headers={
                    "Authorization": f"Bearer {s.RESEND_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "from": s.FROM_EMAIL,
                    "to": to,
                    "subject": subject,
                    "html": html,
                },
            )
            resp.raise_for_status()
            logger.info(f"Email sent to {to} | id={resp.json().get('id')}")
    except Exception as e:
        logger.error(f"Email send failed to {to}: {e}")
