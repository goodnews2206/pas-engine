"""
Leakage Detection — find where the brokerage is leaking money.

Pure function. Returns one category string from CATEGORIES.

Priority-ordered classification — the first matching rule wins. The order
is intentional: provider failures upstream of a booking are the most
expensive leak, scheduling failures next, etc.
"""

from datetime import datetime, timedelta, timezone
from typing import Optional

CATEGORIES = (
    "source_leakage",
    "response_leakage",
    "qualification_leakage",
    "callback_leakage",
    "scheduling_leakage",
    "provider_leakage",
    "no_leak_detected",
)

_PROVIDER_NEAR_BOOKING_WINDOW = timedelta(minutes=5)
_LEAD_TERMINAL_STATUSES = {"booked", "transferred", "closed"}
_QUALIFY_FIELDS = ("intent", "budget", "timeline")
_PROVIDER_FAILURE_TYPES = {"provider.failed", "system.error"}
_BOOKING_PROVIDERS = {"calcom", "twilio"}


def _parse_iso(s):
    if not s or not isinstance(s, str):
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return None


def _events_of(events, event_type):
    return [e for e in events or [] if (e or {}).get("event_type") == event_type]


def _has_event(events, event_type) -> bool:
    return any((e or {}).get("event_type") == event_type for e in events or [])


def _has_provider_failure_near_booking(events) -> bool:
    booking_attempts = _events_of(events, "booking.attempted")
    if not booking_attempts:
        return False
    provider_fails = [
        e for e in events or []
        if (e or {}).get("event_type") in _PROVIDER_FAILURE_TYPES
        and ((e or {}).get("provider") or "").lower() in _BOOKING_PROVIDERS
    ]
    if not provider_fails:
        return False
    for ba in booking_attempts:
        ba_t = _parse_iso(ba.get("created_at"))
        if not ba_t:
            continue
        for pf in provider_fails:
            pf_t = _parse_iso(pf.get("created_at"))
            if not pf_t:
                continue
            if abs((pf_t - ba_t).total_seconds()) <= _PROVIDER_NEAR_BOOKING_WINDOW.total_seconds():
                return True
    return False


def _stale_callback(lead_row, events, now=None) -> bool:
    cb_evts = _events_of(events, "callback.requested")
    if not cb_evts:
        return False
    if (lead_row or {}).get("status") in _LEAD_TERMINAL_STATUSES:
        return False
    if now is None:
        now = datetime.now(timezone.utc)
    latest = max(
        (
            _parse_iso(e.get("created_at"))
            for e in cb_evts
            if _parse_iso(e.get("created_at"))
        ),
        default=None,
    )
    if latest is None:
        # Unparseable timestamp → soft signal, not a hard call
        return False
    return (now - latest) > timedelta(hours=24)


def _has_qualification(lead_row, events) -> bool:
    lead = lead_row or {}
    for f in _QUALIFY_FIELDS:
        v = lead.get(f)
        if isinstance(v, str) and v.strip():
            return True
    for e in events or []:
        if (e or {}).get("event_type") == "lead.extracted":
            payload = (e or {}).get("payload") or {}
            if payload.get("field") in _QUALIFY_FIELDS:
                v = payload.get("value")
                if isinstance(v, str) and v.strip():
                    return True
    return False


def detect_leakage(
    lead_row: Optional[dict],
    call_row: Optional[dict],
    events: Optional[list],
    now=None,
) -> str:
    """
    Priority-ordered leakage classification. First match wins.
    Always returns one of CATEGORIES.
    """
    lead = lead_row or {}
    call = call_row or {}
    evts = events or []

    if _has_provider_failure_near_booking(evts):
        return "provider_leakage"

    if _has_event(evts, "booking.failed") and not _has_event(evts, "booking.confirmed"):
        return "scheduling_leakage"

    if _stale_callback(lead, evts, now=now):
        return "callback_leakage"

    call_started = _has_event(evts, "call.started")
    call_ended = _has_event(evts, "call.ended") or _has_event(evts, "call.ended_with_callback")
    if call_started and call_ended and not _has_qualification(lead, evts):
        return "qualification_leakage"

    outcome = call.get("outcome") or lead.get("outcome")
    if (
        _has_event(evts, "call.ended")
        and outcome == "not_booked"
        and not _has_event(evts, "objection.detected")
        and not _has_event(evts, "callback.requested")
    ):
        return "response_leakage"

    if _has_event(evts, "call.failed"):
        source = (call.get("source") or "inbound").lower()
        if source == "inbound" and not _has_event(evts, "lead.extracted"):
            return "source_leakage"

    return "no_leak_detected"
