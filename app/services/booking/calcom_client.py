"""
Cal.com Booking Integration

Triggered ONLY in BOOKING state after lead confirms.
Uses Cal.com v2 API to create a booking.
"""

import logging
from datetime import datetime, timedelta, timezone

import httpx

from app.config import get_settings

logger = logging.getLogger("pas.booking")
settings = get_settings()

CALCOM_API_BASE = "https://api.cal.com/v2"


async def book_appointment(
    phone: str,
    name: str,
    notes: str,
    email: str = "",
) -> dict:
    """
    Creates a Cal.com booking for the next available slot.
    Returns {"success": bool, "booking_url": str, "booking_id": str}
    """
    try:
        # Step 1: Get next available slot
        slot = await _get_next_available_slot()
        if not slot:
            logger.error("No available slots found in Cal.com")
            return {"success": False, "error": "no_slots"}

        # Step 2: Create booking
        headers = {
            "Authorization": f"Bearer {settings.CALCOM_API_KEY}",
            "Content-Type": "application/json",
            "cal-api-version": "2024-08-13",
        }

        payload = {
            "eventTypeId": settings.CALCOM_EVENT_TYPE_ID,
            "start": slot["start"],
            "attendee": {
                "name": name,
                "email": email or f"lead+{phone.replace('+', '')}@orvnlabs.com",
                "timeZone": "America/New_York",
                "phoneNumber": phone,
                "language": "en",
            },
            "metadata": {
                "source": "PAS_VOICE",
                "notes": notes,
                "phone": phone,
            }
        }

        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.post(
                f"{CALCOM_API_BASE}/bookings",
                headers=headers,
                json=payload
            )
            resp.raise_for_status()
            data = resp.json()

        booking_id = data.get("data", {}).get("id", "")
        booking_url = data.get("data", {}).get("meetingUrl", "")

        logger.info(f"Cal.com booking created | id={booking_id} | slot={slot['start']}")
        return {
            "success": True,
            "booking_id": str(booking_id),
            "booking_url": booking_url,
            "slot": slot["start"],
        }

    except httpx.HTTPStatusError as e:
        logger.error(f"Cal.com HTTP error: {e.response.status_code} — {e.response.text}")
        return {"success": False, "error": f"http_{e.response.status_code}"}
    except Exception as e:
        logger.error(f"Cal.com booking failed: {e}", exc_info=True)
        return {"success": False, "error": str(e)}


async def _get_next_available_slot() -> dict | None:
    """
    Fetches the next available 15-min slot from Cal.com.
    Looks 7 days ahead starting from tomorrow.
    """
    headers = {
        "Authorization": f"Bearer {settings.CALCOM_API_KEY}",
        "cal-api-version": "2024-08-13",
    }

    start_time = (datetime.now(timezone.utc) + timedelta(hours=2)).isoformat()
    end_time = (datetime.now(timezone.utc) + timedelta(days=7)).isoformat()

    params = {
        "eventTypeId": settings.CALCOM_EVENT_TYPE_ID,
        "startTime": start_time,
        "endTime": end_time,
        "timeZone": "America/New_York",
    }

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(
                f"{CALCOM_API_BASE}/slots",
                headers=headers,
                params=params
            )
            resp.raise_for_status()
            data = resp.json()

        # data.data is a dict of date → [{"start": "...", "end": "..."}]
        slots_by_date = data.get("data", {})
        for date_key in sorted(slots_by_date.keys()):
            day_slots = slots_by_date[date_key]
            if day_slots:
                return day_slots[0]  # First available slot

        return None

    except Exception as e:
        logger.error(f"Cal.com slot fetch failed: {e}")
        return None
