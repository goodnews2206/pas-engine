"""
SMS notifications via Twilio Messaging.
Used for booking confirmations and reminders.
"""

import logging

from twilio.rest import Client

from app.config import get_settings

logger = logging.getLogger("pas.sms")


def _twilio_client():
    s = get_settings()
    return Client(s.TWILIO_ACCOUNT_SID, s.TWILIO_AUTH_TOKEN)


async def send_booking_confirmation_sms(phone: str, name: str, slot_readable: str):
    body = (
        f"Hi {name or 'there'} — your property viewing with ORVN Realty is confirmed "
        f"for {slot_readable}. "
        "Your agent will reach out shortly with details. "
        "Reply STOP to opt out."
    )
    await _send_sms(phone, body)


async def send_reminder_sms(phone: str, name: str, slot_readable: str, hours_before: int):
    body = (
        f"Hi {name or 'there'}, reminder: your property viewing with ORVN Realty is "
        f"{'tomorrow' if hours_before == 24 else 'in 1 hour'} — {slot_readable}. "
        "Reply STOP to opt out."
    )
    await _send_sms(phone, body)


async def _send_sms(to: str, body: str):
    try:
        s = get_settings()
        client = _twilio_client()
        msg = client.messages.create(
            to=to,
            from_=s.TWILIO_PHONE_NUMBER,
            body=body,
        )
        logger.info(f"SMS sent to {to} | sid={msg.sid}")
    except Exception as e:
        logger.error(f"SMS send failed to {to}: {e}")
