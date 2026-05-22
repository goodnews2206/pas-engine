"""
PAS198 — Run a bounded manual-test runtime against a PAS197
manual-test package.

Reads a PAS197 package JSON. If the package satisfies the PAS198
contract (READY_FOR_MANUAL_TEST + SIMULATION_ONLY +
live_behavior_changed=False), executes the package's recommended
strategy against the closed PAS193 scenario catalogue and writes a
structured runtime artefact under reports/simulations/. The
runtime is SIMULATION_ONLY and cannot route a live call.

Safety doctrine (enforced by tests and the readiness gate):

  * Output carries status=EXECUTED,
    allowed_environment=SIMULATION_ONLY,
    live_behavior_changed=False.
  * Never imports twilio, slack_sdk, openai, anthropic, dotenv,
    supabase, or the live state machine.
  * Never reads .env, never opens a network connection.
  * Never writes outside reports/simulations/.

Exit codes:
  0 — runtime executed.
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


from app.services.simulation.manual_test_runtime import (  # noqa: E402
    ManualTestRuntimeValidationError,
    execute_manual_test_runtime,
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
        prog="pas198_run_manual_test_runtime",
        description=(
            "PAS198 — Execute a PAS197 manual-test package in a "
            "bounded SIMULATION_ONLY runtime. Produces a transcript "
            "bundle, runtime evaluation, capability summary, and "
            "safety outcome. Never routes a live call."
        ),
    )
    p.add_argument("--package", required=True,
                   help="path to a PAS197 manual-test package JSON")
    p.add_argument("--output-dir", default=str(_REPO_ROOT / REPORTS_SUBDIR),
                   help="directory to write the runtime JSON into")
    p.add_argument("--summary-only", action="store_true",
                   help="do not write a JSON file; print summary only")
    p.add_argument("--json", action="store_true",
                   help="print the full runtime payload as JSON to stdout")
    return p


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_runtime(out_dir: Path, payload: dict) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = payload.get("created_at", _now_iso()).replace(":", "").replace("-", "")
    name = f"pas198_manual_test_runtime_{ts}_{payload['runtime_id']}.json"
    fp = out_dir / name
    fp.write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return fp


def _print_summary(rt: dict, written_path: Optional[Path]) -> None:
    safety = rt.get("safety_outcome") or {}
    score  = rt.get("runtime_score") or {}
    caps   = rt.get("capability_summary") or {}
    print(
        f"[PAS198] runtime_id={rt['runtime_id']} "
        f"package_id={rt['package_id']} "
        f"strategy={rt['executed_strategy']} "
        f"status={rt['status']} "
        f"execution_status={rt['execution_status']} "
        f"environment={rt['allowed_environment']} "
        f"live_behavior_changed={rt['live_behavior_changed']}"
    )
    print(
        f"[PAS198] scenarios_executed={len(rt['executed_scenarios'])} "
        f"pass_rate={score.get('pass_rate')} "
        f"average_score={score.get('average_score')}"
    )
    print(
        f"[PAS198] capability_rates "
        f"qualification={caps.get('qualification_captured_rate')} "
        f"objection={caps.get('objection_handled_rate')} "
        f"callback={caps.get('callback_captured_rate')} "
        f"booking={caps.get('booking_attempted_rate')}"
    )
    print(
        f"[PAS198] safety_outcome={safety.get('outcome')} "
        f"auto_fail_count={safety.get('auto_fail_count')} "
        f"auto_fail_reasons={','.join(safety.get('auto_fail_reasons') or []) or '-'}"
    )
    if written_path is not None:
        print(f"[PAS198] runtime written: {written_path}")


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as e:
        return 2 if e.code not in (0, None) else int(e.code or 0)

    pkg_path = Path(args.package)
    if not pkg_path.is_file():
        print(f"error: --package path not a file: {pkg_path}",
              file=sys.stderr)
        return 2

    try:
        package = _read_json(pkg_path)
    except Exception as e:
        print(f"error: cannot read package: {type(e).__name__}",
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
        rt = execute_manual_test_runtime(
            package,
            created_at=_now_iso(),
        )
    except ManualTestRuntimeValidationError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    written_path: Optional[Path] = None
    if not args.summary_only:
        written_path = _write_runtime(out_dir, rt)

    _print_summary(rt, written_path)

    if args.json:
        print(json.dumps(rt, indent=2, sort_keys=True))

    return 0


if __name__ == "__main__":
    sys.exit(main())
