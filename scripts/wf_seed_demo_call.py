"""
PAS132 — YC demo seed: insert one richer call into Supabase.

Creates a single `calls` row + a chronological set of `pas_events` rows
that exercise the demo conversation:

    Lead: "Hi, I'm looking to buy a home."
    Lead: "My budget is around 500,000 dollars."
    Lead: "I want to move within the next month."
    Lead: "I don't want to book right now."
    Lead: "Can you call me tomorrow morning instead?"

After insert, fetches the workflow envelope through the same runtime the
admin and portal endpoints use, so the seeded data is verified against
the live read path (not just the raw rows).

Idempotent: re-running detects an existing call_id + events and reports
without re-inserting.

Usage (from project root, .env loaded):
    python scripts/wf_seed_demo_call.py
"""

import os
import sys
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from app.db.supabase_client import init_supabase, get_supabase
from app.services.intelligence.queries import events_for_call
from app.services.workflows.runtime import get_or_build_workflow_for_call

# ── Demo identity ────────────────────────────────────────────────────────────
CALL_ID       = "SIM-YC-W26-CALLBACK-001"
BROKERAGE_ID  = "orvn-realty"
PHONE_NUMBER  = "web_demo"
SOURCE        = "simulation"

# Anchor time: a fixed past moment so timestamps are stable across re-runs.
# Using "now - 1 minute" so the call shows up at the top of recency-sorted
# dashboards but isn't dated in the future.
_NOW          = datetime.now(timezone.utc)
_T0           = _NOW - timedelta(minutes=1)


def _ts(offset_seconds: int) -> str:
    return (_T0 + timedelta(seconds=offset_seconds)).isoformat()


# Each entry: (event_type, offset_seconds, state, payload, severity)
# `state` lines up with the conversation FSM at the moment of the event.
# `payload` shape matches what the mapper reads (see app/services/workflows/mapper.py).
DEMO_EVENTS = [
    # 1. Call begins
    ("call.started",            0,  "GREETING",
     {"source": SOURCE},                                                     "info"),

    # 2. PAS leaves greeting and enters intent capture
    ("state.transition",        1,  "INTENT",
     {"from": "GREETING", "to": "INTENT"},                                   "info"),

    # 3. Intent extracted: buying
    ("lead.extracted",          4,  "INTENT",
     {"field": "intent",   "value": "buying",
      "trigger_excerpt": "I'm looking to buy a home"},                       "info"),

    # 4. Move to budget capture
    ("state.transition",        6,  "BUDGET",
     {"from": "INTENT", "to": "BUDGET"},                                     "info"),

    # 5. Budget extracted: $500k
    ("lead.extracted",          9,  "BUDGET",
     {"field": "budget",   "value": "$500k",
      "trigger_excerpt": "around 500,000 dollars"},                          "info"),

    # 6. Move to timeline capture
    ("state.transition",        11, "TIMELINE",
     {"from": "BUDGET", "to": "TIMELINE"},                                   "info"),

    # 7. Timeline extracted: next month
    ("lead.extracted",          14, "TIMELINE",
     {"field": "timeline", "value": "next month",
      "trigger_excerpt": "move within the next month"},                      "info"),

    # 8. Move to booking
    ("state.transition",        16, "BOOKING",
     {"from": "TIMELINE", "to": "BOOKING"},                                  "info"),

    # 9. Lead pivots to callback before booking is offered
    ("callback.requested",      25, "BOOKING",
     {"from_state": "BOOKING",
      "trigger_excerpt": "call me tomorrow morning"},                        "info"),

    # 10. Call ends with a qualified callback outcome
    ("call.ended_with_callback", 28, "DONE",
     {"outcome": "qualified_callback_requested",
      "preferred_time_normalized": "tomorrow_morning",
      "callback_confirmed": True,
      "best_number_confirmed": True},                                        "info"),
]


def _print(msg: str) -> None:
    print(msg, flush=True)


def _ensure_brokerage_exists(db) -> bool:
    try:
        rows = (
            db.table("brokerages")
            .select("id")
            .eq("id", BROKERAGE_ID)
            .limit(1)
            .execute()
            .data or []
        )
        return bool(rows)
    except Exception as e:
        _print(f"[FATAL] brokerage lookup failed: {type(e).__name__}: {e}")
        return False


def _existing_call(db) -> dict:
    try:
        rows = (
            db.table("calls")
            .select("id, brokerage_id, source, created_at")
            .eq("id", CALL_ID)
            .limit(1)
            .execute()
            .data or []
        )
        return rows[0] if rows else {}
    except Exception as e:
        _print(f"[WARN] calls lookup failed: {type(e).__name__}: {e}")
        return {}


def _insert_call(db) -> bool:
    row = {
        "id":            CALL_ID,
        "brokerage_id":  BROKERAGE_ID,
        "phone_number":  PHONE_NUMBER,
        "source":        SOURCE,
        "start_time":    _T0.isoformat(),
        "call_status":   "completed",
        "outcome":       "qualified_callback_requested",
    }
    try:
        db.table("calls").insert(row).execute()
        return True
    except Exception as e:
        _print(f"[FATAL] calls insert failed: {type(e).__name__}: {e}")
        return False


def _existing_event_count(db) -> int:
    try:
        res = (
            db.table("pas_events")
            .select("id", count="exact")
            .eq("call_id", CALL_ID)
            .limit(1)
            .execute()
        )
        return res.count or 0
    except Exception as e:
        _print(f"[WARN] pas_events count failed: {type(e).__name__}: {e}")
        return 0


def _insert_events(db) -> int:
    inserted = 0
    for event_type, off, state, payload, severity in DEMO_EVENTS:
        category = "call" if event_type.startswith(("call.", "state.")) else "lead"
        if event_type in ("callback.requested", "call.ended_with_callback"):
            category = "call"
        row = {
            "event_type":     event_type,
            "event_category": category,
            "event_source":   "seed_script",
            "severity":       severity,
            "brokerage_id":   BROKERAGE_ID,
            "call_id":        CALL_ID,
            "state":          state,
            "payload":        payload,
            "created_at":     _ts(off),
        }
        try:
            db.table("pas_events").insert(row).execute()
            inserted += 1
        except Exception as e:
            _print(f"[FATAL] pas_events insert failed at {event_type}: {type(e).__name__}: {e}")
            return inserted
    return inserted


def _summarise_workflow(env: dict) -> None:
    _print(f"workflow_status:     {env.get('workflow_status')}")
    _print(f"current_step:        {env.get('current_step')}")
    _print(f"leak_detected_at:    {env.get('leak_detected_at')}")
    _print(f"events_count:        {env.get('events_count')}")
    _print("steps:")
    for s in env.get("steps", []):
        _print(
            f"  [{s.get('order_index'):>2}] {s.get('key'):<22} "
            f"{s.get('status'):<10}  {s.get('label')}"
        )


def main() -> int:
    _print("== PAS132 demo seed ==")
    _print(f"target call_id:      {CALL_ID}")
    _print(f"target brokerage_id: {BROKERAGE_ID}")
    _print(f"anchor time (UTC):   {_T0.isoformat()}")
    _print("")

    try:
        init_supabase()
    except Exception as e:
        # Don't print the env values — only the failure type.
        _print(f"[FATAL] Supabase client init failed: {type(e).__name__}")
        return 2

    db = get_supabase()

    if not _ensure_brokerage_exists(db):
        _print(
            f"[FATAL] brokerage_id={BROKERAGE_ID!r} not found in `brokerages`. "
            "FK on calls.brokerage_id will reject the insert. "
            "Seed the brokerage row first."
        )
        return 3

    existing_call = _existing_call(db)
    if existing_call:
        _print(f"[idempotent] calls row already exists for {CALL_ID}; not re-inserting.")
    else:
        if not _insert_call(db):
            return 4
        _print(f"[ok] inserted calls row {CALL_ID}")

    pre_existing = _existing_event_count(db)
    if pre_existing >= len(DEMO_EVENTS):
        _print(f"[idempotent] {pre_existing} pas_events already exist for {CALL_ID}; not re-inserting.")
        inserted_now = 0
    elif pre_existing > 0:
        _print(
            f"[WARN] {pre_existing} partial events exist for {CALL_ID}; "
            "skipping insert to avoid duplicates. Delete the partial set first if needed."
        )
        inserted_now = 0
    else:
        inserted_now = _insert_events(db)
        _print(f"[ok] inserted {inserted_now} pas_events for {CALL_ID}")

    # ── Verification: read back via the same query layer the dashboards use.
    persisted_events = events_for_call(CALL_ID, brokerage_id=BROKERAGE_ID)
    _print("")
    _print(f"verified pas_events count (post-insert): {len(persisted_events)}")

    workflow = get_or_build_workflow_for_call(
        CALL_ID, brokerage_id=BROKERAGE_ID, audience="admin"
    )
    _print("")
    _print("== workflow envelope (admin view) ==")
    _summarise_workflow(workflow)

    # ── Final report block (the user-facing required output).
    _print("")
    _print("== REPORT ==")
    _print(f"1. call_id:                {CALL_ID}")
    _print(f"2. inserted_event_count:   {inserted_now}  "
           f"(persisted_total={len(persisted_events)})")
    _print(f"3. workflow_status:        {workflow.get('workflow_status')}")
    _print("4. steps_summary:")
    for s in workflow.get("steps", []):
        _print(f"   - {s.get('key'):<22} {s.get('status')}")

    # Fail loud if the workflow didn't reach the expected demo shape.
    expected = {
        "lead_received":      "completed",
        "pas_calling":        "completed",
        "intent_captured":    "completed",
        "budget_captured":    "completed",
        "timeline_captured":  "completed",
        "booking_attempted":  "skipped",
        "booking_confirmed":  "skipped",
        "callback_requested": "completed",
        "followup_scheduled": "completed",
        "completed":          "completed",
    }
    got = {s.get("key"): s.get("status") for s in workflow.get("steps", [])}
    mismatches = [(k, expected[k], got.get(k)) for k in expected if got.get(k) != expected[k]]
    if mismatches:
        _print("")
        _print("[WARN] workflow shape did not fully match demo expectations:")
        for k, want, have in mismatches:
            _print(f"   - {k}: expected={want} got={have}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
