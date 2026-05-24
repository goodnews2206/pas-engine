"""
PAS205 — Run the read-only proactive observer against a seeded
in-memory demo snapshot, write the digest under
reports/simulations/, and print the human summary.

Strict invariants:

  * Demo data is hard-coded, deterministic, and PII-free.
  * No Supabase reads (PAS205 has no DB adapter yet — PAS206 will
    add a read-only snapshot adapter).
  * No Twilio, no Slack outbound, no email.
  * Writes a single JSON artefact under reports/simulations/.

Exit codes:
  0 — digest written
  2 — bad CLI args or write failure
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import List


_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


from app.services.proactive.observer import observe  # noqa: E402
from app.services.proactive.observer_digest import (  # noqa: E402
    to_broker_report,
    to_machine_json,
    to_slack_summary,
)
from app.services.proactive.observer_models import (  # noqa: E402
    ObservedAgent,
    ObservedBooking,
    ObservedCall,
    ObservedCallback,
    ObservedLead,
    ObservedSnapshot,
)


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


REPORTS_SUBDIR = Path("reports") / "simulations"


# Fixed "now" so demo output is bit-for-bit reproducible.
DEMO_OBSERVED_AT = "2026-05-23T14:00:00Z"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _build_demo_snapshot() -> ObservedSnapshot:
    """A hand-crafted snapshot that exercises every PAS205 rule.

    No PII, no real names, no production refs — only synthetic
    `L-###` / `C-###` / `B-###` / `K-###` / `A-###` identifiers.
    """
    leads = (
        # Brand-new lead, unassigned, still inside grace window.
        ObservedLead(
            lead_ref="L-001",
            created_at="2026-05-23T13:59:50Z",
            assigned_agent_ref=None,
            source="zillow",
        ),
        # Lead with no first response, well past 5-minute target.
        ObservedLead(
            lead_ref="L-002",
            created_at="2026-05-23T13:30:00Z",
            assigned_agent_ref="A-002",
            source="facebook",
        ),
        # Stale lead — 3 days idle.
        ObservedLead(
            lead_ref="L-003",
            created_at="2026-05-20T09:00:00Z",
            first_response_at="2026-05-20T09:02:00Z",
            last_activity_at="2026-05-20T09:30:00Z",
            assigned_agent_ref="A-001",
            source="realtor",
        ),
        # Unassigned, past first-response target.
        ObservedLead(
            lead_ref="L-004",
            created_at="2026-05-23T13:40:00Z",
            assigned_agent_ref=None,
            source="organic",
        ),
        # High-value lead waiting.
        ObservedLead(
            lead_ref="L-005",
            created_at="2026-05-23T13:55:00Z",
            assigned_agent_ref="A-003",
            source="referral",
            value_tier="high",
        ),
        # After-hours lead still waiting.
        ObservedLead(
            lead_ref="L-006",
            created_at="2026-05-23T02:10:00Z",
            assigned_agent_ref="A-002",
            source="zillow",
            after_hours=True,
        ),
        # Lead flagged for human review.
        ObservedLead(
            lead_ref="L-007",
            created_at="2026-05-23T13:00:00Z",
            first_response_at="2026-05-23T13:01:00Z",
            last_activity_at="2026-05-23T13:30:00Z",
            assigned_agent_ref="A-001",
            source="organic",
            needs_human_review=True,
        ),
        # Lead with repeated failed calls.
        ObservedLead(
            lead_ref="L-008",
            created_at="2026-05-23T12:00:00Z",
            first_response_at="2026-05-23T12:02:00Z",
            last_activity_at="2026-05-23T12:45:00Z",
            assigned_agent_ref="A-001",
            source="zillow",
        ),
    )

    calls = (
        ObservedCall(call_ref="C-001", lead_ref="L-008",
                     started_at="2026-05-23T12:05:00Z",
                     outcome="failed", attempt_index=1),
        ObservedCall(call_ref="C-002", lead_ref="L-008",
                     started_at="2026-05-23T12:20:00Z",
                     outcome="failed", attempt_index=2),
        ObservedCall(call_ref="C-003", lead_ref="L-008",
                     started_at="2026-05-23T12:40:00Z",
                     outcome="failed", attempt_index=3),
    )

    bookings = (
        # Failed-to-confirm booking.
        ObservedBooking(
            booking_ref="B-001",
            lead_ref="L-007",
            proposed_at="2026-05-24T17:00:00Z",
            confirmation_state="failed",
            last_attempt_at="2026-05-23T13:45:00Z",
        ),
        # Healthy confirmed booking — should produce no signal.
        ObservedBooking(
            booking_ref="B-002",
            lead_ref="L-003",
            proposed_at="2026-05-25T15:00:00Z",
            confirmation_state="confirmed",
        ),
    )

    callbacks = (
        # Overdue callback (40 minutes past schedule).
        ObservedCallback(
            callback_ref="K-001",
            lead_ref="L-005",
            requested_at="2026-05-23T12:00:00Z",
            scheduled_at="2026-05-23T13:20:00Z",
            state="pending",
        ),
        # Healthy on-time callback (still in the future).
        ObservedCallback(
            callback_ref="K-002",
            lead_ref="L-002",
            requested_at="2026-05-23T13:30:00Z",
            scheduled_at="2026-05-23T14:30:00Z",
            state="pending",
        ),
    )

    # All agents present, at least one available — so the
    # "no_agent_available" rule should NOT fire on the demo data.
    agents = (
        ObservedAgent(agent_ref="A-001", available=True),
        ObservedAgent(agent_ref="A-002", available=False),
        ObservedAgent(agent_ref="A-003", available=True),
    )

    return ObservedSnapshot(
        observed_at=DEMO_OBSERVED_AT,
        leads=leads,
        calls=calls,
        bookings=bookings,
        callbacks=callbacks,
        agents=agents,
    )


def _build_report(repo_root: Path) -> dict:
    snapshot = _build_demo_snapshot()
    digest = observe(snapshot)
    machine = to_machine_json(digest)
    slack_summary = to_slack_summary(digest)
    broker_report = to_broker_report(digest)
    return {
        "phase":                 "PAS205",
        "allowed_environment":   "SIMULATION_ONLY",
        "live_behavior_changed": False,
        "generated_at":          _now_iso(),
        "observed_at":           digest.observed_at,
        "digest":                machine,
        "human": {
            "slack_summary": slack_summary,
            "broker_report": broker_report,
        },
        "demo_snapshot": {
            "leads":     len(snapshot.leads),
            "calls":     len(snapshot.calls),
            "bookings":  len(snapshot.bookings),
            "callbacks": len(snapshot.callbacks),
            "agents":    len(snapshot.agents),
        },
    }


def _write_report(repo_root: Path, report: dict) -> Path:
    reports_dir = repo_root / REPORTS_SUBDIR
    reports_dir.mkdir(parents=True, exist_ok=True)
    stamp = report["generated_at"].replace(":", "").replace("-", "")
    filename = f"pas205_proactive_observer_demo_{stamp}.json"
    path = reports_dir / filename
    path.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "PAS205 — Run the read-only proactive observer against a "
            "seeded demo snapshot and emit the needs-attention digest."
        ),
    )
    parser.add_argument(
        "--summary-only",
        action="store_true",
        help="Print only the slack-style human summary, no JSON path.",
    )
    parser.add_argument(
        "--no-write",
        action="store_true",
        help="Do not write a report file; print to stdout only.",
    )
    args = parser.parse_args(argv)

    repo_root = _REPO_ROOT
    report = _build_report(repo_root)

    if not args.no_write:
        try:
            written = _write_report(repo_root, report)
        except OSError as e:
            print(f"PAS205 demo: failed to write report ({e})", file=sys.stderr)
            return 2
    else:
        written = None

    summary = report["human"]["slack_summary"]
    digest = report["digest"]
    signals_count = len(digest["signals"])

    if args.summary_only:
        print(summary)
        return 0

    print(summary)
    print("")
    print(f"signals: {signals_count}")
    print(f"by severity: {digest['counts_by_severity']}")
    if written is not None:
        print(f"report: {written.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
