"""
PAS208 — Run the operator-approval recommendation layer over a
seeded PAS205 snapshot, exercise the four-state approval machine,
and write the resulting artifact under reports/recommendations/.

The CLI is end-to-end runnable on a laptop with no Supabase
reachability and no production credentials. It uses the same
deterministic seeded snapshot the PAS207 demo uses, runs the
PAS205 observer, builds a PAS208 RecommendationDigest, and then
applies a fixed sequence of operator decisions to demonstrate the
approval state machine. None of those decisions cause any side
effect — they just produce new frozen Recommendation values.

Strict invariants:

  * No Supabase reads.
  * No Twilio, no Slack outbound, no email, no scheduler.
  * Writes exactly one JSON artifact under
    reports/recommendations/.
  * `live_behavior_changed=False` on every emitted object.

Exit codes:
  0 — artifact written
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
from app.services.proactive.recommendations import (  # noqa: E402
    APPROVAL_APPROVED_FOR_MANUAL_REVIEW,
    APPROVAL_DEFERRED,
    APPROVAL_REJECTED,
    Recommendation,
    apply_decision,
    build_recommendations,
    to_broker_report,
    to_machine_json,
)
from app.services.slack.proactive_digest_intent import (  # noqa: E402
    build_demo_snapshot,
)


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


REPORTS_SUBDIR = Path("reports") / "recommendations"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# Deterministic operator decisions: a rotating sequence that
# exercises every terminal state at least once while leaving most
# recommendations in CANDIDATE. The CLI demonstrates the state
# machine without claiming to know operator intent.
_DECISION_CYCLE = (
    APPROVAL_APPROVED_FOR_MANUAL_REVIEW,
    APPROVAL_REJECTED,
    APPROVAL_DEFERRED,
)


def _exercise_decisions(
    recommendations: List[Recommendation],
    operator_ref:    str,
    decided_at:      str,
) -> List[Recommendation]:
    """Apply a fixed cycle of decisions to the first three
    recommendations and leave the rest as CANDIDATE.
    """
    out: List[Recommendation] = []
    for idx, rec in enumerate(recommendations):
        if idx < len(_DECISION_CYCLE):
            decision = _DECISION_CYCLE[idx]
            out.append(
                apply_decision(
                    rec,
                    decision,
                    operator_ref=operator_ref,
                    reason=f"demo decision {decision}",
                    decided_at=decided_at,
                )
            )
        else:
            out.append(rec)
    return out


def _build_report(operator_ref: str, decided_at: str) -> dict:
    snapshot = build_demo_snapshot()
    signal_digest = observe(snapshot)
    rec_digest = build_recommendations(signal_digest)
    exercised = _exercise_decisions(list(rec_digest.recommendations), operator_ref, decided_at)

    # Render machine JSON of the *exercised* sequence by manually
    # building the dict — to_machine_json renders only what's on
    # the RecommendationDigest, and we want to show the post-
    # decision view for the demo artifact.
    machine = to_machine_json(rec_digest)
    machine["recommendations"] = [
        {
            "recommendation_id":        r.recommendation_id,
            "signal_id":                r.signal_id,
            "signal_type":              r.signal_type,
            "severity":                 r.severity,
            "subject_type":             r.subject_type,
            "subject_ref":              r.subject_ref,
            "recommended_action_type":  r.recommended_action_type,
            "approval_status":          r.approval_status,
            "reason":                   r.reason,
            "evidence":                 dict(r.evidence or {}),
            "created_at":               r.created_at,
            "decided_at":               r.decided_at,
            "decided_by":               r.decided_by,
            "decision_reason":          r.decision_reason,
            "operator_required":        r.operator_required,
            "live_behavior_changed":    r.live_behavior_changed,
        }
        for r in exercised
    ]

    return {
        "phase":                  "PAS208",
        "allowed_environment":    "SIMULATION_ONLY",
        "live_behavior_changed":  False,
        "generated_at":           _now_iso(),
        "observed_at":            signal_digest.observed_at,
        "source_digest_id":       signal_digest.digest_id,
        "operator_ref":           operator_ref,
        "broker_report":          to_broker_report(rec_digest),
        "digest":                 machine,
    }


def _write_report(repo_root: Path, report: dict) -> Path:
    reports_dir = repo_root / REPORTS_SUBDIR
    reports_dir.mkdir(parents=True, exist_ok=True)
    stamp = report["generated_at"].replace(":", "").replace("-", "")
    filename = f"pas208_proactive_recommendations_demo_{stamp}.json"
    path = reports_dir / filename
    path.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def _parse_args(argv: List[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "PAS208 — Build the operator-approval recommendation digest "
            "from a seeded PAS205 snapshot and write it under "
            "reports/recommendations/."
        ),
    )
    p.add_argument(
        "--operator-ref",
        default="demo-operator",
        help="Operator identifier recorded alongside each exercised decision.",
    )
    p.add_argument(
        "--no-write",
        action="store_true",
        help="Do not write a report file; print to stdout only.",
    )
    p.add_argument(
        "--summary-only",
        action="store_true",
        help="Print only the broker-readable summary.",
    )
    return p.parse_args(argv)


def main(argv: List[str]) -> int:
    args = _parse_args(argv)
    decided_at = _now_iso()
    report = _build_report(args.operator_ref, decided_at)

    if not args.no_write:
        try:
            written = _write_report(_REPO_ROOT, report)
        except OSError as e:
            print(f"PAS208: failed to write report ({e})", file=sys.stderr)
            return 2
    else:
        written = None

    if args.summary_only:
        print(report["broker_report"])
        return 0

    print(report["broker_report"])
    print("")
    digest = report["digest"]
    print(f"phase: {digest['phase']}")
    print(f"recommendations: {len(digest['recommendations'])}")
    # Re-tally status counts from the exercised list so the
    # printed view reflects the demo decisions.
    status_tally: dict = {}
    for r in digest["recommendations"]:
        status_tally[r["approval_status"]] = status_tally.get(r["approval_status"], 0) + 1
    print(f"counts_by_status: {status_tally}")
    print(f"live_behavior_changed: {digest['live_behavior_changed']}")
    if written is not None:
        print(f"report: {written.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
