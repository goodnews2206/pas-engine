"""
Tests for app.services.intelligence.sanitize and the pure helper in queries.py.

Pytest-compatible. Also runnable directly:
    python tests/intelligence/test_queries_sanitize.py

The DB-touching functions in queries.py (recent_events, events_for_call,
callback_events) are not exercised here — they require a live Supabase
connection. Their failure path (returns []) is exercised at integration
time. We test only the pure helper _bounded_limit / _bounded_offset.
"""

import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

from app.services.intelligence.queries import (
    DEFAULT_LIMIT,
    MAX_LIMIT,
    _bounded_limit,
    _bounded_offset,
)
from app.services.intelligence.sanitize import sanitize_event_for_portal


# ───────────── _bounded_limit ─────────────

def test_bounded_limit_caps_at_100():
    assert _bounded_limit(500) == MAX_LIMIT
    assert _bounded_limit(101) == MAX_LIMIT


def test_bounded_limit_passes_through_in_range():
    assert _bounded_limit(50) == 50
    assert _bounded_limit(1) == 1


def test_bounded_limit_rejects_zero_and_negative():
    assert _bounded_limit(0) == DEFAULT_LIMIT
    assert _bounded_limit(-5) == DEFAULT_LIMIT


def test_bounded_limit_rejects_non_int():
    assert _bounded_limit(None) == DEFAULT_LIMIT
    assert _bounded_limit("50") == DEFAULT_LIMIT
    assert _bounded_limit(3.5) == DEFAULT_LIMIT


def test_bounded_offset_safe_defaults():
    assert _bounded_offset(None) == 0
    assert _bounded_offset(-1) == 0
    assert _bounded_offset(10) == 10


# ───────────── sanitize_event_for_portal ─────────────

def test_sanitize_drops_forbidden_payload_fields():
    row = {
        "event_type": "objection.detected",
        "payload": {
            "category": "has_agent",
            "text": "raw text from caller",
            "raw_text": "another raw blob",
            "trigger_excerpt": "callback excerpt",
            "detail_excerpt": "error detail",
            "message": "provider message",
        },
    }
    cleaned = sanitize_event_for_portal(row)
    assert cleaned["event_type"] == "objection.detected"
    p = cleaned["payload"]
    assert p == {"category": "has_agent"}
    assert "text" not in p
    assert "raw_text" not in p
    assert "trigger_excerpt" not in p
    assert "detail_excerpt" not in p
    assert "message" not in p


def test_sanitize_drops_secret_like_keys():
    row = {
        "event_type": "system.error",
        "payload": {
            "service": "calcom",
            "api_key": "sk-abc",
            "twilio_auth_token": "secret",
            "user_password": "hunter2",
            "x_admin_key": "xx",
            "authorization": "Bearer xx",
        },
    }
    cleaned = sanitize_event_for_portal(row)
    p = cleaned["payload"]
    assert p == {"service": "calcom"}


def test_sanitize_drops_top_level_secrets():
    row = {
        "event_type": "call.started",
        "api_key": "sk-leak",
        "authorization": "Bearer xx",
        "payload": {},
    }
    cleaned = sanitize_event_for_portal(row)
    assert "api_key" not in cleaned
    assert "authorization" not in cleaned


def test_sanitize_keeps_safe_top_level_fields():
    row = {
        "event_type": "call.started",
        "event_category": "call",
        "event_source": "call_logger",
        "severity": "info",
        "state": "GREETING",
        "call_id": "CA123",
        "lead_id": "lead-1",
        "brokerage_id": "remax-miami",
        "agent_id": "agent-1",
        "provider": None,
        "created_at": "2026-05-03T10:00:00Z",
        "payload": {"source": "inbound"},
        "internal_note": "should be dropped — not on safe-list",
    }
    cleaned = sanitize_event_for_portal(row)
    for k in (
        "event_type", "event_category", "event_source", "severity", "state",
        "call_id", "lead_id", "brokerage_id", "agent_id", "provider", "created_at",
    ):
        assert k in cleaned
    assert "internal_note" not in cleaned
    assert cleaned["payload"] == {"source": "inbound"}


def test_sanitize_drops_long_freeform_strings():
    long_str = "x" * 500
    row = {
        "event_type": "lead.extracted",
        "payload": {"field": "intent", "value": "buying", "blob": long_str},
    }
    cleaned = sanitize_event_for_portal(row)
    p = cleaned["payload"]
    assert p["field"] == "intent"
    assert p["value"] == "buying"
    assert "blob" not in p


def test_sanitize_keeps_short_value_strings():
    row = {
        "event_type": "lead.extracted",
        "payload": {"field": "budget", "value": "$500k"},
    }
    cleaned = sanitize_event_for_portal(row)
    assert cleaned["payload"] == {"field": "budget", "value": "$500k"}


def test_sanitize_recurses_into_nested_dicts():
    row = {
        "event_type": "system.error",
        "payload": {
            "service": "calcom",
            "context": {
                "category": "timeout",
                "secret_key": "leaked",
                "message": "drop me",
            },
        },
    }
    cleaned = sanitize_event_for_portal(row)
    ctx = cleaned["payload"]["context"]
    assert ctx == {"category": "timeout"}


def test_sanitize_recurses_into_list_of_dicts():
    row = {
        "event_type": "call.ended",
        "payload": {
            "objections_detected": [
                {"category": "has_agent", "count": 1, "text": "drop"},
                {"category": "cost", "count": 2, "raw_text": "drop"},
            ],
        },
    }
    cleaned = sanitize_event_for_portal(row)
    items = cleaned["payload"]["objections_detected"]
    assert items == [
        {"category": "has_agent", "count": 1},
        {"category": "cost", "count": 2},
    ]


def test_sanitize_non_dict_input_returns_empty():
    assert sanitize_event_for_portal(None) == {}
    assert sanitize_event_for_portal("string") == {}
    assert sanitize_event_for_portal(123) == {}
    assert sanitize_event_for_portal([]) == {}


def test_sanitize_payload_missing_returns_no_payload_key():
    row = {"event_type": "call.started"}
    cleaned = sanitize_event_for_portal(row)
    assert "payload" not in cleaned
    assert cleaned["event_type"] == "call.started"


def test_sanitize_does_not_mutate_input():
    payload = {"category": "has_agent", "text": "leak"}
    row = {"event_type": "objection.detected", "payload": payload}
    sanitize_event_for_portal(row)
    # Input still has the dropped fields.
    assert payload == {"category": "has_agent", "text": "leak"}


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
