"""
PAS132 demo-scenario integration check.

Feeds the canonical YC demo conversation through the deterministic
mapper and prints the resulting workflow envelope. No Supabase, no
network — exercises the same code path the runtime layer hits after
fetching pas_events.

Run from project root:
    python scripts/wf_sim_check.py
"""

import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from app.services.workflows.mapper import map_events_to_workflow
from app.services.workflows.sanitize import sanitize_workflow_for_audience


def _ev(et, ts, **kw):
    payload = kw.pop("payload", {})
    return {
        "event_type": et,
        "created_at": ts,
        "call_id": "SIM-DEMO132",
        "lead_id": "lead-demo",
        "brokerage_id": "demo",
        "payload": payload,
    }


def main():
    # The PART 6 demo scenario, replayed as the events PAS would have logged:
    #   "Hi, I'm looking to buy a home."
    #   "My budget is around 500,000 dollars."
    #   "I want to move within the next month."
    #   "I don't want to book right now."
    #   "Can you call me tomorrow morning instead?"
    events = [
        _ev("call.started",     "2026-05-04T10:00:00+00:00"),
        _ev("state.transition", "2026-05-04T10:00:01+00:00",
            payload={"from": "GREETING", "to": "INTENT"}),
        _ev("lead.extracted",   "2026-05-04T10:00:04+00:00",
            payload={"field": "intent", "value": "buying"}),
        _ev("state.transition", "2026-05-04T10:00:06+00:00",
            payload={"from": "INTENT", "to": "BUDGET"}),
        _ev("lead.extracted",   "2026-05-04T10:00:09+00:00",
            payload={"field": "budget", "value": "$500k"}),
        _ev("state.transition", "2026-05-04T10:00:11+00:00",
            payload={"from": "BUDGET", "to": "TIMELINE"}),
        _ev("lead.extracted",   "2026-05-04T10:00:14+00:00",
            payload={"field": "timeline", "value": "next month"}),
        _ev("state.transition", "2026-05-04T10:00:16+00:00",
            payload={"from": "TIMELINE", "to": "BOOKING"}),
        # Lead requests callback instead of booking.
        _ev("callback.requested", "2026-05-04T10:00:25+00:00",
            payload={"from_state": "BOOKING",
                     "trigger_excerpt": "call me tomorrow morning"}),
        _ev("call.ended_with_callback", "2026-05-04T10:00:28+00:00",
            payload={"outcome": "qualified_callback_requested",
                     "preferred_time_normalized": "tomorrow_morning",
                     "callback_confirmed": True,
                     "best_number_confirmed": True}),
    ]

    folded = map_events_to_workflow(events)
    print("== RAW (admin-equivalent) ==")
    print(f"workflow_status:   {folded['workflow_status']}")
    print(f"current_step:      {folded['current_step']}")
    print(f"leak_detected_at:  {folded['leak_detected_at']}")
    print(f"events_count:      {folded['events_count']}")
    print()
    for s in folded["steps"]:
        print(f"  [{s['order_index']:>2}] {s['key']:<22} {s['status']:<10}  "
              f"{s.get('event_type') or '-':<26}  {s['label']}")

    # Audience-translated envelopes for sanity-check.
    envelope = {
        "workflow_id": "derived:SIM-DEMO132",
        "call_id": "SIM-DEMO132",
        "lead_id": "lead-demo",
        "brokerage_id": "demo",
        "workflow_type": "lead_response",
        **folded,
        "version": "v1",
    }

    print("\n== PORTAL VIEW ==")
    portal = sanitize_workflow_for_audience(envelope, audience="portal")
    print(json.dumps(portal, indent=2, default=str)[:1500])

    # Assertions — match what the YC demo expects.
    keys = {s["key"]: s for s in folded["steps"]}
    expected = [
        ("lead_received",      "completed"),
        ("pas_calling",        "completed"),
        ("intent_captured",    "completed"),
        ("budget_captured",    "completed"),
        ("timeline_captured",  "completed"),
        # Lead pivoted to a callback before PAS asked the calendar — so
        # the booking branch was reached but never executed. Skipped.
        ("booking_attempted",  "skipped"),
        ("booking_confirmed",  "skipped"),
        ("callback_requested", "completed"),
        ("followup_scheduled", "completed"),
        ("completed",          "completed"),
    ]
    print("\n== DEMO ASSERTIONS ==")
    failed = 0
    for k, want in expected:
        got = keys[k]["status"]
        ok = got == want
        line = f"  {'PASS' if ok else 'FAIL'}  {k:<22} expected={want:<10} got={got}"
        if not ok:
            failed += 1
        print(line)
    if folded["workflow_status"] != "completed":
        failed += 1
        print(f"  FAIL  workflow_status      expected=completed   got={folded['workflow_status']}")
    else:
        print(f"  PASS  workflow_status      expected=completed   got=completed")
    if folded["current_step"] != "completed":
        failed += 1
        print(f"  FAIL  current_step         expected=completed   got={folded['current_step']}")
    else:
        print(f"  PASS  current_step         expected=completed   got=completed")
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
