"""
Tests for app.services.intelligence.recommendations.handoff_recommendation.

Pytest-compatible. Also runnable directly:
    python tests/intelligence/test_recommendations.py
"""

import os
import sys
from datetime import datetime, timezone

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

from app.services.intelligence.recommendations import handoff_recommendation

NOW = datetime(2026, 5, 3, 12, 0, 0, tzinfo=timezone.utc)


def _evt(event_type, payload=None):
    return {
        "event_type": event_type,
        "payload": payload or {},
        "created_at": NOW.isoformat(),
    }


def test_dnc_status_returns_do_not_contact():
    assert handoff_recommendation({"status": "do_not_call"}, {}, []) == "do_not_contact"


def test_remove_objection_returns_do_not_contact():
    events = [_evt("objection.detected", {"category": "remove"})]
    assert handoff_recommendation({"intent": "buying"}, {}, events) == "do_not_contact"


def test_not_interested_objection_returns_do_not_contact():
    events = [_evt("objection.detected", {"category": "not_interested"})]
    assert handoff_recommendation({}, {}, events) == "do_not_contact"


def test_booking_confirmed_returns_book_appointment():
    events = [_evt("booking.confirmed")]
    assert handoff_recommendation({"intent": "buying"}, {}, events) == "book_appointment"


def test_high_readiness_returns_route_to_agent():
    # Score 70+ via booking.attempted + intent + budget + timeline + email
    events = [_evt("booking.attempted")]
    lead = {
        "intent": "buying",
        "budget": "$500k",
        "timeline": "2 weeks",
        "email": "a@b.com",
        "best_number_confirmed": True,
    }
    # Expected score = 15 + 5 + 15 + 10 + 10 (urgent) + 5 + 5 + 10 = 75 → route_to_agent
    assert handoff_recommendation(lead, {}, events) == "route_to_agent"


def test_mid_readiness_with_callback_returns_call_back():
    events = [_evt("callback.requested")]
    lead = {
        "intent": "buying",
        "budget": "$500k",
        "timeline": "3 months",
    }
    # Score = 15+5+15+10+10 = 55 → callback band → call_back
    assert handoff_recommendation(lead, {}, events) == "call_back"


def test_mid_readiness_without_callback_returns_hold():
    # Mid-band (50-69) with no callback event → falls through both the
    # call_back branch (needs callback.requested) and the nurture branch
    # (needs <50). Recommendation is 'hold'.
    # Score = intent 15 + active 5 + budget 15 + timeline 10 + urgent 10 = 55
    lead = {
        "intent": "buying",
        "budget": "$500k",
        "timeline": "2 weeks",
    }
    assert handoff_recommendation(lead, {}, []) == "hold"


def test_low_mid_readiness_returns_nurture():
    # 25-49 band: intent + budget + timeline non-urgent = 45
    lead = {
        "intent": "buying",
        "budget": "$500k",
        "timeline": "3 months",
    }
    # Above is actually 45 (15+5+15+10) → nurture
    assert handoff_recommendation(lead, {}, []) == "nurture"


def test_intent_only_is_hold():
    # Score 20 → Cold → hold
    assert handoff_recommendation({"intent": "exploring"}, {}, []) == "hold"


def test_empty_inputs_safe_default_hold():
    assert handoff_recommendation({}, {}, []) == "hold"


def test_none_inputs_safe_default_hold():
    assert handoff_recommendation(None, None, None) == "hold"


def test_dnc_overrides_booking_confirmed():
    # Booking confirmed but lead is DNC → DNC wins.
    events = [_evt("booking.confirmed"), _evt("objection.detected", {"category": "remove"})]
    assert handoff_recommendation({}, {}, events) == "do_not_contact"


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
