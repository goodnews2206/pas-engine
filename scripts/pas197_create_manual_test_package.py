"""
PAS197 — Create a manual-test package from an approved
recommendation review.

Reads a PAS195 recommendation JSON and a PAS196 review JSON. If
the review approves the recommendation for manual test, writes a
structured manual-test package under reports/simulations/. The
package is SIMULATION_ONLY and cannot route a live call.

Safety doctrine (enforced by tests and the readiness gate):

  * Output carries status=READY_FOR_MANUAL_TEST,
    allowed_environment=SIMULATION_ONLY,
    live_behavior_changed=False.
  * Never imports twilio, slack_sdk, openai, anthropic, dotenv,
    supabase, or the live state machine.
  * Never reads .env, never opens a network connection.
  * Never writes outside reports/simulations/.

Exit codes:
  0 — package written.
  2 — bad CLI args, unreadable input, unwritable output dir, or
       contract violation.
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


from app.services.simulation.manual_test_package import (  # noqa: E402
    ManualTestPackageValidationError,
    build_manual_test_package,
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
        prog="pas197_create_manual_test_package",
        description=(
            "PAS197 — Build a manual-test package from a PAS195 "
            "CANDIDATE recommendation and an APPROVED_FOR_MANUAL_TEST "
            "PAS196 review. Package is SIMULATION_ONLY."
        ),
    )
    p.add_argument("--recommendation", required=True,
                   help="path to a PAS195 recommendation JSON report")
    p.add_argument("--review", required=True,
                   help="path to a PAS196 review envelope JSON")
    p.add_argument("--output-dir", default=str(_REPO_ROOT / REPORTS_SUBDIR),
                   help="directory to write the package JSON into")
    p.add_argument("--summary-only", action="store_true",
                   help="do not write a JSON file; print summary only")
    p.add_argument("--json", action="store_true",
                   help="print the full package payload as JSON to stdout")
    return p


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_package(out_dir: Path, payload: dict) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = payload.get("created_at", _now_iso()).replace(":", "").replace("-", "")
    name = f"pas197_manual_test_package_{ts}_{payload['package_id']}.json"
    fp = out_dir / name
    fp.write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return fp


def _print_summary(pkg: dict, written_path: Optional[Path]) -> None:
    print(
        f"[PAS197] package_id={pkg['package_id']} "
        f"recommendation_id={pkg['recommendation_id']} "
        f"review_id={pkg['review_id']} "
        f"strategy={pkg['strategy_id']} "
        f"status={pkg['status']} "
        f"environment={pkg['allowed_environment']} "
        f"live_behavior_changed={pkg['live_behavior_changed']}"
    )
    print(f"[PAS197] test_plan: {', '.join(pkg['test_plan'])}")
    print(f"[PAS197] success_metrics: {', '.join(pkg['success_metrics'])}")
    print(f"[PAS197] rollback_notes: {', '.join(pkg['rollback_notes'])}")
    print(f"[PAS197] safety_notes: {', '.join(pkg['safety_notes'])}")
    if written_path is not None:
        print(f"[PAS197] package written: {written_path}")


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
    rev_path = Path(args.review)
    if not rev_path.is_file():
        print(f"error: --review path not a file: {rev_path}",
              file=sys.stderr)
        return 2

    try:
        recommendation = _read_json(rec_path)
    except Exception as e:
        print(f"error: cannot read recommendation: {type(e).__name__}",
              file=sys.stderr)
        return 2
    try:
        review = _read_json(rev_path)
    except Exception as e:
        print(f"error: cannot read review: {type(e).__name__}",
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
        pkg = build_manual_test_package(
            recommendation,
            review,
            created_at=_now_iso(),
        )
    except ManualTestPackageValidationError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    written_path: Optional[Path] = None
    if not args.summary_only:
        written_path = _write_package(out_dir, pkg)

    _print_summary(pkg, written_path)

    if args.json:
        print(json.dumps(pkg, indent=2, sort_keys=True))

    return 0


if __name__ == "__main__":
    sys.exit(main())
