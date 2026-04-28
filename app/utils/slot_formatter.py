"""
Formats a Cal.com ISO 8601 slot timestamp into natural speech.
e.g. "2026-04-29T15:00:00Z" → "Wednesday, April 29th at 3 PM"
"""

from datetime import datetime, timezone


def format_slot_for_speech(iso_slot: str) -> str:
    try:
        dt = datetime.fromisoformat(iso_slot.replace("Z", "+00:00")).astimezone(
            timezone.utc
        )
        day_name = dt.strftime("%A")
        month = dt.strftime("%B")
        date_num = dt.day
        suffix = (
            "th"
            if 11 <= date_num <= 13
            else {1: "st", 2: "nd", 3: "rd"}.get(date_num % 10, "th")
        )
        hour = dt.strftime("%I %p").lstrip("0")  # "3 PM", no leading zero
        return f"{day_name}, {month} {date_num}{suffix} at {hour}"
    except Exception:
        return "your scheduled time"
