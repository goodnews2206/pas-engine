"""
PAS209 — Compose the full proactive stack end-to-end on a seeded
PAS205 snapshot: observer → recommendations → operator approval →
bounded action proposal package. Writes a JSON artifact under
reports/proposals/.

The CLI is end-to-end runnable on a laptop with no Supabase
reachability and no production credentials. The "operator
approval" step is a deterministic cycle that approves the first
N recommendations so PAS209 always has something concrete to
package. Nothing in this CLI sends, schedules, or mutates.

Strict invariants:

  * No Supabase reads, no Twilio call, no Slack outbound, no
    email, no scheduler.
  * Writes exactly one JSON artifact under reports/proposals/.
  * Every emitted proposal carries required_human_review=True,
    allowed_channel='MANUAL_ONLY', live_behavior_changed=False.

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


from app.services.proactive.action_proposals import (  # noqa: E402
    build_proposal_package,
    to_broker_report,
    to_machine_json,
)
from app.services.proactive.observer import observe  # noqa: E402
from app.services.proactive.recommendations import (  # noqa: E402
    APPROVAL_APPROVED_FOR_MANUAL_REVIEW,
    Recommendation,
    RecommendationDigest,
    apply_decision,
    build_recommendations,
)
from app.services.slack.proactive_digest_intent import (  # noqa: E402
    build_demo_snapshot,
)


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


REPORTS_SUBDIR = Path("reports") / "proposals"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _approve_first_n(
    rd:           RecommendationDigest,
    n:            int,
    operator_ref: str,
    decided_at:   str,
) -> RecommendationDigest:
    """Approve the first ``n`` recommendations for manual review;
    leave the rest in CANDIDATE. Pure transformation — returns a
    new RecommendationDigest.
    """
    out: List[Recommendation] = []
    for idx, rec in enumerate(rd.recommendations):
        if idx < n:
            out.append(
                apply_decision(
                    rec,
                    APPROVAL_APPROVED_FOR_MANUAL_REVIEW,
                    operator_ref=operator_ref,
                    reason="demo approval for PAS209 packaging",
                    decided_at=decided_at,
                )
            )
        else:
            out.append(rec)
    return RecommendationDigest(
        digest_id              = rd.digest_id,
        generated_at           = rd.generated_at,
        source_digest_id       = rd.source_digest_id,
        observed_at            = rd.observed_at,
        phase                  = rd.phase,
        allowed_environment    = rd.allowed_environment,
        live_behavior_changed  = rd.live_behavior_changed,
        recommendations        = tuple(out),
        counts_by_status       = rd.counts_by_status,
        counts_by_action_type  = rd.counts_by_action_type,
    )


def _build_report(
    operator_ref: str,
    decided_at:   str,
    approve_n:    int,
) -> dict:
    snapshot = build_demo_snapshot()
    signal_digest = observe(snapshot)
    rec_digest = build_recommendations(signal_digest)
    approved_digest = _approve_first_n(
        rec_digest, approve_n, operator_ref, decided_at,
    )
    package = build_proposal_package(approved_digest)
    machine = to_machine_json(package)

    return {
        "phase":                 "PAS209",
        "allowed_environment":   "SIMULATION_ONLY",
        "live_behavior_changed": False,
        "generated_at":          _now_iso(),
        "observed_at":           signal_digest.observed_at,
        "operator_ref":          operator_ref,
        "n_approved":            approve_n,
        "source_signal_digest_id":         signal_digest.digest_id,
        "source_recommendation_digest_id": rec_digest.digest_id,
        "package":               machine,
        "broker_report":         to_broker_report(package),
    }


def _write_report(repo_root: Path, report: dict) -> Path:
    reports_dir = repo_root / REPORTS_SUBDIR
    reports_dir.mkdir(parents=True, exist_ok=True)
    stamp = report["generated_at"].replace(":", "").replace("-", "")
    filename = f"pas209_action_proposals_demo_{stamp}.json"
    path = reports_dir / filename
    path.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def _parse_args(argv: List[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "PAS209 — Compose the proactive stack end-to-end: PAS205 "
            "observer → PAS208 recommendations → operator approval → "
            "PAS209 bounded action proposal package."
        ),
    )
    p.add_argument(
        "--operator-ref", default="demo-operator",
        help="Operator identifier recorded on each approved recommendation.",
    )
    p.add_argument(
        "--approve-n", type=int, default=3,
        help="Approve the first N recommendations so PAS209 has something "
             "concrete to package (default: 3).",
    )
    p.add_argument(
        "--no-write", action="store_true",
        help="Do not write a report file; print to stdout only.",
    )
    p.add_argument(
        "--summary-only", action="store_true",
        help="Print only the broker-readable summary.",
    )
    return p.parse_args(argv)


def main(argv: List[str]) -> int:
    args = _parse_args(argv)
    if args.approve_n < 0:
        print("PAS209: --approve-n must be >= 0", file=sys.stderr)
        return 2

    decided_at = _now_iso()
    report = _build_report(args.operator_ref, decided_at, args.approve_n)

    if not args.no_write:
        try:
            written = _write_report(_REPO_ROOT, report)
        except OSError as e:
            print(f"PAS209: failed to write report ({e})", file=sys.stderr)
            return 2
    else:
        written = None

    if args.summary_only:
        print(report["broker_report"])
        return 0

    print(report["broker_report"])
    print("")
    pkg = report["package"]
    print(f"phase: {pkg['phase']}")
    print(f"proposals: {len(pkg['proposals'])}")
    print(f"approved_n: {args.n_approved if hasattr(args, 'n_approved') else args.approve_n}")
    print(f"live_behavior_changed: {pkg['live_behavior_changed']}")
    if written is not None:
        print(f"report: {written.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
