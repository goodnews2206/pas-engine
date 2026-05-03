"""
Tests for app.services.intelligence.leakage.detect_leakage.

Pytest-compatible. Also runnable directly:
    python tests/intelligence/test_leakage.py
"""

import os
import sys
from datetime import datetime, timedelta, timezone

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

from app.services.intelligence.leakage import detect_leakage

NOW = datetime(2026, 5, 3, 12, 0, 0, tzinfo=timezone.utc)


def _evt(event_type, payload=None, created_at=None, provider=None):
    return {
        "event_type": event_type,
        "payload": payload or {},
        "created_at": (created_at or NOW).isoformat(),
        "provider": provider,
    }


def test_empty_inputs_no_leak():
    assert detect_leakage({}, {}, [], now=NOW) == "no_leak_detected"


def test_none_inputs_safe():
    assert detect_leakage(None, None, None, now=NOW) == "no_leak_detected"


def test_provider_failure_near_booking_wins():
    events = [
        _evt("booking.attempted", created_at=NOW),
        _evt("provider.failed", provider="calcom", created_at=NOW + timedelta(minutes=1)),
    ]
    assert detect_leakage({}, {}, events, now=NOW) == "provider_leakage"


def test_provider_failure_not_near_booking_does_not_match():
    events = [
        _evt("booking.attempted", created_at=NOW),
        _evt("provider.failed", provider="calcom", created_at=NOW + timedelta(minutes=30)),
        _evt("booking.failed", created_at=NOW),
    ]
    # 30min apart — outside the 5min window. Falls through to scheduling_leakage.
    assert detect_leakage({}, {}, events, now=NOW) == "scheduling_leakage"


def test_booking_failed_no_confirm_is_scheduling_leak():
    events = [_evt("booking.attempted"), _evt("booking.failed")]
    assert detect_leakage({}, {}, events, now=NOW) == "scheduling_leakage"


def test_booking_failed_then_confirmed_is_not_scheduling_leak():
    events = [_evt("booking.failed"), _evt("booking.confirmed")]
    # Falls through; no other leak triggers from these events alone.
    assert detect_leakage({}, {}, events, now=NOW) == "no_leak_detected"


def test_stale_callback_is_callback_leak():
    events = [
        _evt("callback.requested", created_at=NOW - timedelta(hours=25)),
    ]
    lead = {"status": "nurture"}
    assert detect_leakage(lead, {}, events, now=NOW) == "callback_leakage"


def test_recent_callback_not_yet_leak():
    events = [
        _evt("callback.requested", created_at=NOW - timedelta(hours=2)),
    ]
    assert detect_leakage({"status": "nurture"}, {}, events, now=NOW) == "no_leak_detected"


def test_callback_completed_lead_status_is_not_leak():
    events = [_evt("callback.requested", created_at=NOW - timedelta(hours=48))]
    assert detect_leakage({"status": "booked"}, {}, events, now=NOW) == "no_leak_detected"


def test_call_started_ended_no_qualification_is_qualification_leak():
    events = [_evt("call.started"), _evt("call.ended")]
    assert detect_leakage({}, {}, events, now=NOW) == "qualification_leakage"


def test_qualification_present_in_lead_avoids_qualification_leak():
    events = [_evt("call.started"), _evt("call.ended")]
    lead = {"intent": "buying"}
    # Falls through. Outcome is None, no objection, no callback — does not trigger
    # response_leakage either (which requires outcome=='not_booked').
    assert detect_leakage(lead, {}, events, now=NOW) == "no_leak_detected"


def test_qualification_extracted_event_avoids_qualification_leak():
    events = [
        _evt("call.started"),
        _evt("lead.extracted", {"field": "intent", "value": "buying"}),
        _evt("call.ended"),
    ]
    assert detect_leakage({}, {}, events, now=NOW) == "no_leak_detected"


def test_callback_ended_path_also_satisfies_call_ended():
    events = [_evt("call.started"), _evt("call.ended_with_callback")]
    # No qualification → still qualification_leakage (the helper accepts either).
    assert detect_leakage({}, {}, events, now=NOW) == "qualification_leakage"


def test_response_leakage_when_engaged_but_not_booked():
    events = [_evt("call.started"), _evt("call.ended")]
    lead = {"intent": "buying", "budget": "$500k", "timeline": "3 months"}
    call = {"outcome": "not_booked"}
    assert detect_leakage(lead, call, events, now=NOW) == "response_leakage"


def test_response_leak_blocked_by_objection():
    events = [
        _evt("call.started"),
        _evt("call.ended"),
        _evt("objection.detected", {"category": "has_agent"}),
    ]
    lead = {"intent": "buying", "budget": "$500k", "timeline": "3 months"}
    call = {"outcome": "not_booked"}
    assert detect_leakage(lead, call, events, now=NOW) == "no_leak_detected"


def test_source_leak_inbound_failed_no_extraction():
    events = [_evt("call.failed")]
    call = {"source": "inbound"}
    assert detect_leakage({}, call, events, now=NOW) == "source_leakage"


def test_source_leak_skipped_when_extraction_present():
    events = [
        _evt("call.failed"),
        _evt("lead.extracted", {"field": "intent", "value": "buying"}),
    ]
    call = {"source": "inbound"}
    # Won't classify as source_leakage; falls through.
    assert detect_leakage({"intent": "buying"}, call, events, now=NOW) == "no_leak_detected"


def test_priority_order_provider_beats_scheduling():
    events = [
        _evt("booking.attempted", created_at=NOW),
        _evt("provider.failed", provider="calcom", created_at=NOW),
        _evt("booking.failed", created_at=NOW),
    ]
    # Both provider and scheduling would match; provider_leakage takes priority.
    assert detect_leakage({}, {}, events, now=NOW) == "provider_leakage"


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
