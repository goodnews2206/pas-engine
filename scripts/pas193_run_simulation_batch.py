"""
PAS193 — Simulation batch runner.

Deterministic CLI that walks the scenario library, runs each
through the offline adapter, scores it, builds a report, and
writes the report to disk under reports/simulations/.

Safety doctrine (enforced by the readiness gate and tests):

  * Never imports twilio.
  * Never imports any Slack client or webhook helper.
  * Never imports supabase / dotenv / openai / anthropic.
  * Never reads .env.
  * Never makes a network call.
  * Never writes outside reports/simulations/.
  * Never inserts into or mutates any database.

Exit codes:
  0 — batch completed; report written.
  2 — bad CLI args / unwritable output dir.
  3 — batch finished but at least one safety auto-fail fired
       (use --strict to enable; default still exits 0).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional


# We add the repo root to sys.path so this CLI runs the same way
# whether invoked from the repo root or from scripts/.
_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


from app.services.simulation.scenarios import (  # noqa: E402
    SCENARIOS,
    scenario_count,
)
from app.services.simulation.adapter import run_scenario  # noqa: E402
from app.services.simulation.scoring import score_conversation  # noqa: E402
from app.services.simulation.report import build_report  # noqa: E402


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


REPORTS_SUBDIR = Path("reports") / "simulations"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _pick_scenarios(count: int) -> list:
    if count <= 0:
        return []
    n = scenario_count()
    out = []
    for i in range(count):
        out.append(SCENARIOS[i % n])
    return out


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="pas193_run_simulation_batch",
        description=(
            "PAS193 — Run a deterministic batch of simulated lead "
            "conversations. Offline only. Never calls Twilio, "
            "Slack, or Supabase."
        ),
    )
    p.add_argument("--count", type=int, default=20,
                   help="number of rehearsals to run (default: 20)")
    p.add_argument("--seed", type=int, default=0,
                   help="seed for the deterministic report_id")
    p.add_argument("--output-dir", default=str(_REPO_ROOT / REPORTS_SUBDIR),
                   help="directory to write the report JSON into")
    p.add_argument("--summary-only", action="store_true",
                   help="do not write a JSON report file; print summary only")
    p.add_argument("--json", action="store_true",
                   help="print the full report payload as JSON to stdout")
    p.add_argument("--strict", action="store_true",
                   help="exit non-zero if any rehearsal triggered an auto-fail")
    return p


def _write_report(out_dir: Path, payload: dict) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = payload.get("generated_at", _now_iso()).replace(":", "").replace("-", "")
    name = f"pas193_simulation_batch_{ts}_{payload['report_id']}.json"
    fp = out_dir / name
    fp.write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return fp


def _print_summary(report: dict, written_path: Optional[Path]) -> None:
    print(
        f"[PAS193] runs={report['total_simulations']} "
        f"pass_rate={report['pass_rate']} "
        f"avg_score={report['average_score']} "
        f"booking_rate={report['booking_attempt_rate']} "
        f"callback_rate={report['callback_capture_rate']} "
        f"objection_rate={report['objection_handling_rate']}"
    )
    top = report.get("top_failure_modes") or []
    if top:
        print("[PAS193] top failure modes:")
        for entry in top[:5]:
            print(f"  - {entry['reason']}: {entry['count']}")
    best = report.get("best_performing_scenario_types") or []
    worst = report.get("worst_performing_scenario_types") or []
    if best:
        print("[PAS193] best scenario types:")
        for entry in best[:3]:
            print(f"  + {entry['scenario_type']} (avg {entry['average_score']})")
    if worst:
        print("[PAS193] worst scenario types:")
        for entry in worst[:3]:
            print(f"  - {entry['scenario_type']} (avg {entry['average_score']})")
    if written_path is not None:
        print(f"[PAS193] report written: {written_path}")


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as e:
        return 2 if e.code not in (0, None) else int(e.code or 0)

    if args.count < 0:
        print("error: --count must be >= 0", file=sys.stderr)
        return 2

    out_dir = Path(args.output_dir)
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"error: cannot create output dir {out_dir}: {type(e).__name__}",
              file=sys.stderr)
        return 2

    picked = _pick_scenarios(args.count)
    scored: list = []
    auto_fail_count = 0
    for scenario in picked:
        conv = run_scenario(scenario)
        result = score_conversation(conv, scenario)
        if result["score"] == 0 and not result["passed"]:
            auto_fail_count += 1
        scored.append({
            "scenario_id":           scenario["scenario_id"],
            "scenario_type":         scenario["scenario_type"],
            "supported":             scenario["supported"],
            "score":                 result["score"],
            "passed":                result["passed"],
            "failure_reasons":       result["failure_reasons"],
            "recommendation_label":  result["recommendation_label"],
            "capabilities_observed": result["capabilities_observed"],
            "missing_criteria":      result["missing_criteria"],
        })

    report = build_report(scored, generated_at=_now_iso(), seed=int(args.seed))

    written_path: Optional[Path] = None
    if not args.summary_only:
        written_path = _write_report(out_dir, report)

    _print_summary(report, written_path)

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))

    if args.strict and auto_fail_count > 0:
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
