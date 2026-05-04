"""
Tests for app.services.workflows.mapper — the deterministic
pas_events → workflow folder.

No DB. No FastAPI. No network. Pure-function tests of the mapping rules
described in PAS132 PART 1.

Pytest-compatible. Also runnable directly:
    python tests/workflows/test_mapper.py
"""

import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

from app.services.workflows.mapper import map_events_to_workflow


def _ev(event_type, ts="2026-05-04T10:00:00+00:00", **kw):
    """Build a minimal pas_events row for the mapper."""
    payload = kw.pop("payload", {})
    state = kw.pop("state", None)
    return {
        "event_type": event_type,
        "created_at": ts,
        "state": state,
        "payload": payload,
        **kw,
    }


def _by_key(steps):
    return {s["key"]: s for s in steps}


# ───────────── shape contracts ─────────────

def test_empty_events_returns_pending_skeleton():
    out = map_events_to_workflow([])
    keys = [s["key"] for s in out["steps"]]
    assert keys == [
        "lead_received", "pas_calling", "intent_captured", "budget_captured",
        "timeline_captured", "booking_attempted", "booking_confirmed",
        "callback_requested", "followup_scheduled", "completed",
    ]
    assert out["workflow_status"] == "pending"
    assert out["current_step"] == "lead_received"  # first pending
    assert out["leak_detected_at"] is None
    assert out["events_count"] == 0


def test_categories_are_correct():
    by_key = _by_key(map_events_to_workflow([])["steps"])
    assert by_key["lead_received"]["category"] == "detect"
    assert by_key["pas_calling"]["category"] == "detect"
    assert by_key["intent_captured"]["category"] == "decide"
    assert by_key["booking_attempted"]["category"] == "act"
    assert by_key["booking_confirmed"]["category"] == "outcome"


def test_unknown_event_types_are_ignored():
    out = map_events_to_workflow([_ev("nonsense.event")])
    assert out["workflow_status"] == "pending"


# ───────────── happy paths ─────────────

def test_call_started_marks_lead_received_and_pas_calling():
    out = map_events_to_workflow([_ev("call.started")])
    by_key = _by_key(out["steps"])
    assert by_key["lead_received"]["status"] == "completed"
    assert by_key["pas_calling"]["status"] == "running"
    assert out["workflow_status"] == "running"
    assert out["current_step"] == "pas_calling"


def test_state_transitions_advance_decide_steps():
    events = [
        _ev("call.started", ts="2026-05-04T10:00:00+00:00"),
        _ev("state.transition", ts="2026-05-04T10:00:01+00:00", payload={"from": "GREETING", "to": "INTENT"}),
        _ev("state.transition", ts="2026-05-04T10:00:05+00:00", payload={"from": "INTENT", "to": "BUDGET"}),
        _ev("state.transition", ts="2026-05-04T10:00:10+00:00", payload={"from": "BUDGET", "to": "TIMELINE"}),
    ]
    by_key = _by_key(map_events_to_workflow(events)["steps"])
    assert by_key["pas_calling"]["status"] == "completed"
    assert by_key["intent_captured"]["status"] == "completed"
    assert by_key["budget_captured"]["status"] == "completed"
    assert by_key["timeline_captured"]["status"] == "running"


def test_lead_extracted_completes_field_step():
    events = [
        _ev("call.started"),
        _ev("lead.extracted", payload={"field": "intent", "value": "buying"}),
        _ev("lead.extracted", payload={"field": "budget", "value": "$500k"}),
    ]
    by_key = _by_key(map_events_to_workflow(events)["steps"])
    assert by_key["intent_captured"]["status"] == "completed"
    assert by_key["budget_captured"]["status"] == "completed"
    # Lead.extracted should not bleed into other steps:
    assert by_key["timeline_captured"]["status"] in ("pending", "running")
    # safe_metadata should carry the extracted scalar value:
    assert by_key["intent_captured"]["safe_metadata"].get("value") == "buying"


def test_booking_confirmed_path_completes_workflow():
    events = [
        _ev("call.started"),
        _ev("state.transition", payload={"from": "TIMELINE", "to": "BOOKING"}),
        _ev("booking.attempted"),
        _ev("booking.confirmed", payload={"slot": "tomorrow_morning"}),
        _ev("call.ended", payload={"outcome": "booked"}),
    ]
    out = map_events_to_workflow(events)
    by_key = _by_key(out["steps"])
    assert by_key["booking_attempted"]["status"] == "completed"
    assert by_key["booking_confirmed"]["status"] == "completed"
    assert by_key["callback_requested"]["status"] == "skipped"
    assert by_key["followup_scheduled"]["status"] == "skipped"
    assert by_key["completed"]["status"] == "completed"
    assert out["workflow_status"] == "completed"
    assert out["leak_detected_at"] is None


def test_callback_path_marks_branch_taken():
    events = [
        _ev("call.started"),
        _ev("state.transition", payload={"from": "GREETING", "to": "INTENT"}),
        _ev("callback.requested", payload={"from_state": "INTENT"}),
        _ev("call.ended_with_callback", payload={"preferred_time_normalized": "tomorrow_morning",
                                                  "callback_confirmed": True}),
    ]
    out = map_events_to_workflow(events)
    by_key = _by_key(out["steps"])
    assert by_key["callback_requested"]["status"] == "completed"
    assert by_key["followup_scheduled"]["status"] == "completed"
    assert by_key["booking_confirmed"]["status"] == "skipped"
    assert by_key["completed"]["status"] == "completed"
    assert out["workflow_status"] == "completed"


# ───────────── leak / warning rules ─────────────

def test_booking_failed_records_leak_without_failing_workflow():
    events = [
        _ev("call.started"),
        _ev("booking.attempted"),
        _ev("booking.failed", payload={"error": "calcom 502"}),
    ]
    out = map_events_to_workflow(events)
    by_key = _by_key(out["steps"])
    assert by_key["booking_attempted"]["status"] == "warning"
    assert out["leak_detected_at"] == "booking_failed"
    # Workflow is still running (no terminal event yet):
    assert out["workflow_status"] == "running"


def test_call_failed_marks_workflow_failed():
    events = [
        _ev("call.started"),
        _ev("call.failed"),
    ]
    out = map_events_to_workflow(events)
    by_key = _by_key(out["steps"])
    assert by_key["completed"]["status"] == "failed"
    assert out["workflow_status"] == "failed"


def test_terminal_warning_after_booking_fail_then_callback():
    events = [
        _ev("call.started"),
        _ev("booking.attempted"),
        _ev("booking.failed"),
        _ev("callback.requested"),
        _ev("call.ended_with_callback"),
    ]
    out = map_events_to_workflow(events)
    by_key = _by_key(out["steps"])
    assert by_key["booking_attempted"]["status"] == "warning"
    assert by_key["callback_requested"]["status"] == "completed"
    assert by_key["completed"]["status"] == "completed"
    # Leak present + terminal event present = workflow-level warning.
    assert out["workflow_status"] == "warning"


# ───────────── current_step rules ─────────────

def test_current_step_prefers_latest_running():
    events = [
        _ev("call.started"),
        _ev("state.transition", payload={"from": "GREETING", "to": "INTENT"}),
        _ev("state.transition", payload={"from": "INTENT", "to": "BUDGET"}),
    ]
    out = map_events_to_workflow(events)
    assert out["current_step"] == "budget_captured"  # latest running


def test_current_step_falls_back_to_warning():
    # Once we transition past GREETING the pas_calling step completes; with
    # all earlier decide/act steps either skipped or warning, current_step
    # falls through to the warning step (booking_attempted).
    events = [
        _ev("call.started"),
        _ev("state.transition", payload={"from": "GREETING", "to": "BOOKING"}),
        _ev("booking.attempted"),
        _ev("booking.failed"),
    ]
    out = map_events_to_workflow(events)
    assert out["current_step"] == "booking_attempted"


# ───────────── system signals ─────────────

def test_provider_failed_only_increments_signal_counter():
    events = [
        _ev("call.started"),
        _ev("provider.failed", payload={"provider": "calcom"}),
        _ev("provider.failed", payload={"provider": "anthropic"}),
    ]
    out = map_events_to_workflow(events)
    assert out["system_signals"]["provider_failed_count"] == 2
    # Provider failures alone should not flip the workflow to failed;
    # the call may still complete normally.
    assert out["workflow_status"] != "failed"


# ───────────── runner ─────────────

if __name__ == "__main__":
    fns = [v for k, v in list(globals().items()) if k.startswith("test_") and callable(v)]
    failures = 0
    for fn in fns:
        name = fn.__name__
        try:
            fn()
            print(f"  PASS {name}")
        except AssertionError as e:
            failures += 1
            print(f"  FAIL {name} -- {e}")
        except Exception as e:
            failures += 1
            print(f"  FAIL {name} -- {type(e).__name__}: {e}")
    print(f"\n{len(fns) - failures}/{len(fns)} passed")
    sys.exit(0 if failures == 0 else 1)
