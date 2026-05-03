"""
Handoff Recommendation — deterministic decision tree.

Returns one of:
  hold | nurture | call_back | route_to_agent | book_appointment | do_not_contact

Rules are evaluated in priority order — first match wins.
"""

from typing import Optional

from app.services.intelligence.scoring import readiness_score

_DNC_OBJECTIONS = {"remove", "not_interested"}
_DNC_STATUS = {"do_not_call"}


def _has_event(events, event_type) -> bool:
    return any((e or {}).get("event_type") == event_type for e in events or [])


def _has_dnc_objection(events) -> bool:
    for e in events or []:
        if (e or {}).get("event_type") == "objection.detected":
            payload = (e or {}).get("payload") or {}
            if payload.get("category") in _DNC_OBJECTIONS:
                return True
    return False


def handoff_recommendation(
    lead_row: Optional[dict],
    call_row: Optional[dict],
    events: Optional[list],
) -> str:
    """Return the recommended next action for this lead."""
    lead = lead_row or {}
    evts = events or []

    if lead.get("status") in _DNC_STATUS or _has_dnc_objection(evts):
        return "do_not_contact"

    if _has_event(evts, "booking.confirmed"):
        return "book_appointment"

    rs = readiness_score(lead, evts)
    score = rs["score"]

    if score >= 70:
        return "route_to_agent"

    if 50 <= score <= 69 and _has_event(evts, "callback.requested"):
        return "call_back"

    if 25 <= score <= 49:
        return "nurture"

    return "hold"
