"""
PAS196 — Record an operator review against a PAS195 CANDIDATE
recommendation.

Reads a PAS195 recommendation JSON report from disk, validates the
requested review action against the closed status machine, and
writes a bounded review envelope under reports/simulations/.
Never autonomously applies, deploys, or otherwise changes live
behaviour.

Safety doctrine (enforced by tests and the readiness gate):

  * Output envelope carries operator_required=True and
    live_behavior_changed=False.
  * Reason and actor tokens are drawn from closed vocabularies.
  * Never imports twilio, slack_sdk, openai, anthropic, dotenv,
    supabase, or the live state machine.
  * Never reads .env, never opens a network connection.
  * Never writes outside reports/simulations/.

Exit codes:
  0 — review recorded; envelope written.
  2 — bad CLI args, unreadable input, unwritable output dir, or
       contract violation in the review request.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional


_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


from app.services.simulation.recommendation_review import (  # noqa: E402
    ACTOR_TYPES,
    REASON_TOKENS,
    REVIEW_ACTIONS,
    ReviewValidationError,
    submit_review,
)


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


REPORTS_SUBDIR = Path("reports") / "simulations"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="pas196_review_simulation_recommendation",
        description=(
            "PAS196 — Record an operator review against a PAS195 "
            "CANDIDATE recommendation. Never autonomously applies "
            "or deploys the recommendation."
        ),
    )
    p.add_argument("--recommendation", required=True,
                   help="path to a PAS195 recommendation JSON report")
    p.add_argument("--action", required=True,
                   choices=sorted(REVIEW_ACTIONS.keys()),
                   help="review action to record")
    p.add_argument("--actor-id-token", required=True,
                   help="opaque operator token (op_*) or auto_expiry")
    p.add_argument("--reason-token", required=True, choices=REASON_TOKENS,
                   help="closed-vocabulary reason token")
    p.add_argument("--actor-type", default="operator", choices=ACTOR_TYPES,
                   help="operator (default) or automated_expiry")
    p.add_argument("--output-dir", default=str(_REPO_ROOT / REPORTS_SUBDIR),
                   help="directory to write the review envelope into")
    p.add_argument("--summary-only", action="store_true",
                   help="do not write a JSON envelope file; print summary only")
    p.add_argument("--json", action="store_true",
                   help="print the full envelope as JSON to stdout")
    return p


def _write_envelope(out_dir: Path, payload: dict) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = payload.get("reviewed_at", _now_iso()).replace(":", "").replace("-", "")
    name = f"pas196_recommendation_review_{ts}_{payload['review_id']}.json"
    fp = out_dir / name
    fp.write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return fp


def _print_summary(env: dict, written_path: Optional[Path]) -> None:
    print(
        f"[PAS196] review_id={env['review_id']} "
        f"recommendation_id={env['recommendation_id']} "
        f"previous={env['previous_status']} new={env['new_status']} "
        f"actor_type={env['actor_type']} "
        f"reason={env['reason_token']} "
        f"operator_required={env['operator_required']} "
        f"live_behavior_changed={env['live_behavior_changed']}"
    )
    if written_path is not None:
        print(f"[PAS196] review envelope written: {written_path}")


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as e:
        return 2 if e.code not in (0, None) else int(e.code or 0)

    rec_path = Path(args.recommendation)
    if not rec_path.is_file():
        print(f"error: --recommendation path not a file: {rec_path}",
              file=sys.stderr)
        return 2
    try:
        recommendation = json.loads(rec_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"error: cannot read recommendation: {type(e).__name__}",
              file=sys.stderr)
        return 2

    try:
        out_dir = Path(args.output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"error: cannot create output dir {args.output_dir}: {type(e).__name__}",
              file=sys.stderr)
        return 2

    try:
        envelope = submit_review(
            recommendation,
            args.action,
            actor_id_token=args.actor_id_token,
            reason_token=args.reason_token,
            reviewed_at=_now_iso(),
            actor_type=args.actor_type,
        )
    except ReviewValidationError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    written_path: Optional[Path] = None
    if not args.summary_only:
        written_path = _write_envelope(out_dir, envelope)

    _print_summary(envelope, written_path)

    if args.json:
        print(json.dumps(envelope, indent=2, sort_keys=True))

    return 0


if __name__ == "__main__":
    sys.exit(main())
