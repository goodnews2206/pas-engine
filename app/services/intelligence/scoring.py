"""
Lead Readiness + Callback Priority — deterministic V1 scoring.

Pure functions. No DB, no network, no LLM. Inputs are plain dicts so the
algorithms can be unit-tested without any external state.

Outputs always carry a `version` field so future iterations can A/B compare.
"""

from datetime import datetime, timedelta, timezone
from typing import Optional

SCORING_VERSION = "v1"

# DNC clamps — these always return label="Do Not Contact" with score=0.
_DNC_OBJECTION_CATEGORIES = {"remove", "not_interested"}
_DNC_LEAD_STATUSES = {"do_not_call"}

# Timeline urgency keywords (treated case-insensitively).
_URGENT_TIMELINE_KEYWORDS = (
    "day", "week", "1 month", "one month", "asap", "immediate",
)

# Normalised callback time buckets (see state_machine._normalize_callback_time).
_TODAY_TIME_NORMS = {
    "today_morning", "today_afternoon", "today_evening", "today_later",
    "tonight", "morning", "afternoon", "evening",
}
_TOMORROW_TIME_NORMS = {
    "tomorrow", "tomorrow_morning", "tomorrow_afternoon", "tomorrow_evening",
}
_NEXT_WEEK_NORMS = {"next_week"}

_URGENCY_WORDS = ("asap", "today", "urgent", "now", "right away", "immediately")


# ───────────── helpers ─────────────

def _safe_str(v) -> str:
    if isinstance(v, str):
        return v.strip()
    if v is None or isinstance(v, bool):
        return ""
    return str(v).strip()


def _has_event_type(events, event_type: str) -> bool:
    return any((e or {}).get("event_type") == event_type for e in events or [])


def _objection_categories(events) -> set:
    cats = set()
    for e in events or []:
        if (e or {}).get("event_type") == "objection.detected":
            payload = (e or {}).get("payload") or {}
            cat = payload.get("category")
            if cat:
                cats.add(cat)
    return cats


def _parse_iso(s):
    if not s or not isinstance(s, str):
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return None


def _lead_age_hours(lead_row: dict, now=None):
    created = _parse_iso(lead_row.get("created_at"))
    if not created:
        return None
    if now is None:
        now = datetime.now(timezone.utc)
    return max(0.0, (now - created).total_seconds() / 3600.0)


def _events_in_last_24h(events, now=None) -> int:
    if now is None:
        now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=24)
    n = 0
    for e in events or []:
        ts = _parse_iso((e or {}).get("created_at"))
        if ts and ts >= cutoff:
            n += 1
    return n


# ───────────── readiness ─────────────

def readiness_score(lead_row: Optional[dict], events: Optional[list]) -> dict:
    """
    Score 0-100 + label. lead_row may be None (treated as empty).
    events is a list of pas_events rows for this lead/call.

    Hard clamps that override the score:
      - lead.status == 'do_not_call' or DNC objection → 0 / Do Not Contact
      - outcome in {'transferred','booked'} → score floored at 90
    """
    lead = lead_row or {}
    evts = events or []

    if lead.get("status") in _DNC_LEAD_STATUSES:
        return {"score": 0, "label": "Do Not Contact", "version": SCORING_VERSION}
    if _objection_categories(evts) & _DNC_OBJECTION_CATEGORIES:
        return {"score": 0, "label": "Do Not Contact", "version": SCORING_VERSION}

    score = 0

    intent = _safe_str(lead.get("intent")).lower()
    if intent:
        score += 15
        if intent in ("buying", "selling"):
            score += 5

    if _safe_str(lead.get("budget")):
        score += 15

    timeline = _safe_str(lead.get("timeline")).lower()
    if timeline:
        score += 10
        if any(kw in timeline for kw in _URGENT_TIMELINE_KEYWORDS):
            score += 10

    if _safe_str(lead.get("email")):
        score += 5

    if lead.get("best_number_confirmed") is True:
        score += 5

    if _has_event_type(evts, "booking.attempted"):
        score += 10
    if _has_event_type(evts, "booking.confirmed"):
        score += 25
    if _has_event_type(evts, "booking.failed"):
        score -= 5

    if _has_event_type(evts, "callback.requested"):
        score += 10

    if lead.get("outcome") in ("transferred", "booked"):
        score = max(score, 90)

    score = max(0, min(100, score))

    callback_requested = _has_event_type(evts, "callback.requested")
    return {
        "score": score,
        "label": _readiness_label(score, callback_requested),
        "version": SCORING_VERSION,
    }


def _readiness_label(score: int, callback_requested: bool) -> str:
    if score <= 24:
        return "Cold"
    if score <= 49:
        return "Nurture"
    if score <= 69:
        return "Callback Needed" if callback_requested else "Qualified"
    return "Ready for Agent"


# ───────────── callback priority ─────────────

def callback_priority_score(
    lead_row: Optional[dict],
    callback_event: Optional[dict],
    events: Optional[list],
    now=None,
) -> dict:
    """
    Score the urgency of a callback. Inputs:
      - lead_row: leads table row (dict)
      - callback_event: the originating callback.requested pas_events row
      - events: full event history for this lead (for 24h activity bonus)
      - now: optional datetime override for deterministic tests
    """
    lead = lead_row or {}
    cb = callback_event or {}
    evts = events or []

    score = 0

    norm_time = _safe_str(lead.get("preferred_callback_time_normalized")).lower()
    if norm_time in _TODAY_TIME_NORMS:
        score += 30
    elif norm_time in _TOMORROW_TIME_NORMS:
        score += 20
    elif norm_time in _NEXT_WEEK_NORMS:
        score += 5

    if _safe_str(lead.get("intent")):
        score += 10
    if _safe_str(lead.get("budget")):
        score += 10

    timeline = _safe_str(lead.get("timeline")).lower()
    if timeline and any(kw in timeline for kw in _URGENT_TIMELINE_KEYWORDS):
        score += 15

    if lead.get("best_number_confirmed") is True:
        score += 10

    age_hours = _lead_age_hours(lead, now=now)
    if age_hours is not None:
        if age_hours < 2:
            score += 15
        elif age_hours < 24:
            score += 5

    activity = _events_in_last_24h(evts, now=now)
    score += min(5, activity)

    reason = _safe_str(lead.get("callback_reason")).lower()
    cb_payload = (cb or {}).get("payload") or {}
    excerpt = _safe_str(cb_payload.get("trigger_excerpt")).lower()
    haystack = reason + " " + excerpt
    if any(w in haystack for w in _URGENCY_WORDS):
        score += 15

    score = max(0, min(100, score))
    return {
        "score": score,
        "priority": _priority_label(score),
        "version": SCORING_VERSION,
    }


def _priority_label(score: int) -> str:
    if score <= 24:
        return "Low"
    if score <= 49:
        return "Medium"
    if score <= 74:
        return "High"
    return "Urgent"
