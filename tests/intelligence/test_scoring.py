"""
Tests for app.services.intelligence.scoring.

Pytest-compatible. Also runnable directly:
    python tests/intelligence/test_scoring.py
"""

import os
import sys
from datetime import datetime, timedelta, timezone

# Allow `from app...` when run directly (no pytest collector to set sys.path).
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

from app.services.intelligence.scoring import (
    SCORING_VERSION,
    callback_priority_score,
    readiness_score,
)

NOW = datetime(2026, 5, 3, 12, 0, 0, tzinfo=timezone.utc)


def _evt(event_type, payload=None, created_at=None, provider=None):
    return {
        "event_type": event_type,
        "payload": payload or {},
        "created_at": (created_at or NOW).isoformat(),
        "provider": provider,
    }


# ───────────── readiness_score ─────────────

def test_readiness_empty_inputs_returns_cold():
    r = readiness_score({}, [])
    assert r["score"] == 0
    assert r["label"] == "Cold"
    assert r["version"] == SCORING_VERSION


def test_readiness_none_inputs_safe():
    r = readiness_score(None, None)
    assert r["score"] == 0
    assert r["label"] == "Cold"


def test_readiness_dnc_status_clamps_to_zero():
    r = readiness_score({"status": "do_not_call", "intent": "buying", "budget": "$500k"}, [])
    assert r["score"] == 0
    assert r["label"] == "Do Not Contact"


def test_readiness_dnc_objection_clamps_to_zero():
    events = [_evt("objection.detected", {"category": "remove"})]
    r = readiness_score({"intent": "buying", "budget": "$500k"}, events)
    assert r["score"] == 0
    assert r["label"] == "Do Not Contact"


def test_readiness_not_interested_objection_clamps():
    events = [_evt("objection.detected", {"category": "not_interested"})]
    r = readiness_score({"intent": "buying"}, events)
    assert r["label"] == "Do Not Contact"


def test_readiness_intent_only_is_cold():
    r = readiness_score({"intent": "buying"}, [])
    # +15 intent +5 active = 20 → Cold
    assert r["score"] == 20
    assert r["label"] == "Cold"


def test_readiness_intent_budget_timeline_is_nurture():
    r = readiness_score(
        {"intent": "buying", "budget": "$500k", "timeline": "3 months"},
        [],
    )
    # +15 +5 +15 +10 = 45 → Nurture
    assert r["score"] == 45
    assert r["label"] == "Nurture"


def test_readiness_urgent_timeline_adds_ten():
    r = readiness_score(
        {"intent": "buying", "budget": "$500k", "timeline": "2 weeks"},
        [],
    )
    # +15 +5 +15 +10 +10 (urgent) = 55 → Qualified
    assert r["score"] == 55
    assert r["label"] == "Qualified"


def test_readiness_callback_requested_changes_label_at_50_69_band():
    events = [_evt("callback.requested")]
    r = readiness_score(
        {"intent": "buying", "budget": "$500k", "timeline": "2 weeks"},
        events,
    )
    # 55 (above) + 10 callback = 65 → Callback Needed (because callback flag is set)
    assert r["score"] == 65
    assert r["label"] == "Callback Needed"


def test_readiness_booking_confirmed_makes_ready_for_agent():
    events = [_evt("booking.attempted"), _evt("booking.confirmed")]
    r = readiness_score(
        {"intent": "buying", "budget": "$500k", "timeline": "2 weeks", "email": "x@y.com"},
        events,
    )
    # intent 15 + active 5 + budget 15 + timeline 10 + urgent 10 + email 5
    # + booking.attempted 10 + booking.confirmed 25 = 95
    assert r["score"] == 95
    assert r["label"] == "Ready for Agent"


def test_readiness_booked_outcome_floors_score():
    r = readiness_score({"outcome": "booked"}, [])
    assert r["score"] >= 90
    assert r["label"] == "Ready for Agent"


def test_readiness_transferred_outcome_floors_score():
    r = readiness_score({"outcome": "transferred"}, [])
    assert r["score"] >= 90
    assert r["label"] == "Ready for Agent"


def test_readiness_booking_failed_subtracts():
    base = readiness_score({"intent": "buying", "budget": "$500k"}, [])
    with_fail = readiness_score(
        {"intent": "buying", "budget": "$500k"},
        [_evt("booking.failed")],
    )
    assert with_fail["score"] == base["score"] - 5


def test_readiness_score_clamped_to_100():
    events = [
        _evt("booking.attempted"),
        _evt("booking.confirmed"),
        _evt("callback.requested"),
    ]
    lead = {
        "intent": "buying", "budget": "$500k", "timeline": "1 week",
        "email": "a@b.com", "best_number_confirmed": True,
    }
    r = readiness_score(lead, events)
    assert r["score"] == 100


def test_readiness_score_clamped_to_zero_floor():
    # booking.failed alone with no positive signals must not go negative.
    r = readiness_score({}, [_evt("booking.failed")])
    assert r["score"] == 0
    assert r["label"] == "Cold"


# ───────────── callback_priority_score ─────────────

def test_callback_priority_empty_returns_low():
    r = callback_priority_score({}, {}, [], now=NOW)
    assert r["score"] == 0
    assert r["priority"] == "Low"
    assert r["version"] == SCORING_VERSION


def test_callback_priority_today_window_is_high_band():
    lead = {"preferred_callback_time_normalized": "today_evening"}
    r = callback_priority_score(lead, {}, [], now=NOW)
    # +30 today
    assert r["score"] == 30
    assert r["priority"] == "Medium"


def test_callback_priority_tomorrow_window():
    lead = {"preferred_callback_time_normalized": "tomorrow_morning"}
    r = callback_priority_score(lead, {}, [], now=NOW)
    assert r["score"] == 20
    assert r["priority"] == "Low"


def test_callback_priority_next_week_minimal():
    lead = {"preferred_callback_time_normalized": "next_week"}
    r = callback_priority_score(lead, {}, [], now=NOW)
    assert r["score"] == 5


def test_callback_priority_intent_budget_timeline_stack():
    lead = {
        "preferred_callback_time_normalized": "today_evening",
        "intent": "buying",
        "budget": "$500k",
        "timeline": "2 weeks",
        "best_number_confirmed": True,
    }
    r = callback_priority_score(lead, {}, [], now=NOW)
    # 30 + 10 + 10 + 15 (urgent timeline) + 10 (number) = 75 → Urgent
    assert r["score"] == 75
    assert r["priority"] == "Urgent"


def test_callback_priority_lead_age_under_2h_bonus():
    created = (NOW - timedelta(hours=1)).isoformat()
    lead = {
        "preferred_callback_time_normalized": "today_morning",
        "created_at": created,
    }
    r = callback_priority_score(lead, {}, [], now=NOW)
    # 30 + 15 (age < 2h) = 45
    assert r["score"] == 45
    assert r["priority"] == "Medium"


def test_callback_priority_lead_age_under_24h_bonus():
    created = (NOW - timedelta(hours=10)).isoformat()
    lead = {
        "preferred_callback_time_normalized": "today_morning",
        "created_at": created,
    }
    r = callback_priority_score(lead, {}, [], now=NOW)
    # 30 + 5 = 35
    assert r["score"] == 35


def test_callback_priority_24h_activity_capped_at_5():
    events = [_evt("state.transition", created_at=NOW - timedelta(hours=1)) for _ in range(20)]
    lead = {"preferred_callback_time_normalized": "today_morning"}
    r = callback_priority_score(lead, {}, events, now=NOW)
    # 30 + 5 (activity cap) = 35
    assert r["score"] == 35


def test_callback_priority_urgency_word_in_reason():
    lead = {
        "preferred_callback_time_normalized": "today_morning",
        "callback_reason": "this is urgent please call ASAP",
    }
    r = callback_priority_score(lead, {}, [], now=NOW)
    # 30 + 15 = 45
    assert r["score"] == 45


def test_callback_priority_urgency_word_in_event_excerpt():
    lead = {"preferred_callback_time_normalized": "today_morning"}
    cb = _evt("callback.requested", {"trigger_excerpt": "I need help right now"})
    r = callback_priority_score(lead, cb, [], now=NOW)
    assert r["score"] >= 45


def test_callback_priority_clamped_to_100():
    lead = {
        "preferred_callback_time_normalized": "today_morning",
        "intent": "buying",
        "budget": "$500k",
        "timeline": "1 week",
        "best_number_confirmed": True,
        "callback_reason": "ASAP",
        "created_at": (NOW - timedelta(minutes=30)).isoformat(),
    }
    events = [_evt("state.transition", created_at=NOW - timedelta(hours=1)) for _ in range(10)]
    r = callback_priority_score(lead, {}, events, now=NOW)
    assert r["score"] == 100
    assert r["priority"] == "Urgent"


# ───────────── standalone runner ─────────────

if __name__ == "__main__":
    failures = 0
    funcs = [v for k, v in list(globals().items()) if k.startswith("test_") and callable(v)]
    for fn in funcs:
        try:
            fn()
            print(f"PASS {fn.__name__}")
        except AssertionError as e:
            failures += 1
            print(f"FAIL {fn.__name__}: {e}")
        except Exception as e:
            failures += 1
            print(f"ERROR {fn.__name__}: {type(e).__name__}: {e}")
    print(f"\n{len(funcs) - failures}/{len(funcs)} passed")
    sys.exit(1 if failures else 0)
