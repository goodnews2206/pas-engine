"""
PAS194 — Strategy comparison CLI.

Runs the PAS193 scenario catalogue under every PAS194 strategy and
writes a structured comparison report under reports/simulations/.

Safety doctrine (enforced by tests and the readiness gate):

  * Never imports twilio, slack_sdk, openai, anthropic, dotenv,
    supabase, or the live state machine.
  * Never reads .env, never opens a network connection.
  * Never writes outside reports/simulations/.

Exit codes:
  0 — batch completed; report written.
  2 — bad CLI args / unwritable output dir.
  3 — batch finished but at least one (strategy, scenario)
       auto-failed (use --strict to enable; default still 0).
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


from app.services.simulation.scenarios import SCENARIOS, scenario_count  # noqa: E402
from app.services.simulation.strategies import (  # noqa: E402
    STRATEGIES,
    STRATEGY_IDS,
    STRATEGY_INDEX,
)
from app.services.simulation.comparison import (  # noqa: E402
    build_comparison_report,
    compare_strategies,
)


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
    return [SCENARIOS[i % n] for i in range(count)]


def _filter_strategies(ids: Optional[List[str]]) -> list:
    if not ids:
        return list(STRATEGIES)
    out = []
    for sid in ids:
        if sid not in STRATEGY_INDEX:
            raise ValueError(f"unknown strategy_id: {sid!r}")
        out.append(STRATEGY_INDEX[sid])
    return out


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="pas194_compare_simulation_strategies",
        description=(
            "PAS194 — Compare PAS conversation strategies against "
            "the PAS193 scenario catalogue. Offline only. Never "
            "calls Twilio, Slack, or Supabase."
        ),
    )
    p.add_argument("--count", type=int, default=scenario_count(),
                   help="number of scenarios per strategy (default: full catalogue)")
    p.add_argument("--strategies", default="",
                   help="comma-separated strategy_id list; default: all")
    p.add_argument("--seed", type=int, default=0,
                   help="seed for the deterministic report_id")
    p.add_argument("--output-dir", default=str(_REPO_ROOT / REPORTS_SUBDIR),
                   help="directory to write the report JSON into")
    p.add_argument("--summary-only", action="store_true",
                   help="do not write a JSON report file; print summary only")
    p.add_argument("--json", action="store_true",
                   help="print the full report payload as JSON to stdout")
    p.add_argument("--strict", action="store_true",
                   help="exit non-zero if any (strategy, scenario) auto-failed")
    return p


def _write_report(out_dir: Path, payload: dict) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = payload.get("generated_at", _now_iso()).replace(":", "").replace("-", "")
    name = f"pas194_strategy_comparison_{ts}_{payload['report_id']}.json"
    fp = out_dir / name
    fp.write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return fp


def _print_summary(report: dict, written_path: Optional[Path]) -> None:
    print(
        f"[PAS194] strategies={report['strategy_count']} "
        f"scenarios={report['scenario_count']} "
        f"best={report['best_strategy']} "
        f"worst={report['worst_strategy']}"
    )
    print("[PAS194] per-strategy metrics:")
    for sid in sorted(report["per_strategy_metrics"].keys()):
        m = report["per_strategy_metrics"][sid]
        print(
            f"  - {sid:15s} pass={m['pass_rate']:<6} "
            f"avg={m['average_score']:<6} "
            f"book={m['booking_attempt_rate']:<6} "
            f"call={m['callback_capture_rate']:<6} "
            f"obj={m['objection_handling_rate']:<6}"
        )
    print(f"[PAS194] recommendation: {report['recommendation']}")
    if written_path is not None:
        print(f"[PAS194] report written: {written_path}")


def _count_auto_fails(rows_by_strategy: dict) -> int:
    n = 0
    for rows in rows_by_strategy.values():
        for r in rows:
            if r["score"] == 0 and not r["passed"]:
                n += 1
    return n


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as e:
        return 2 if e.code not in (0, None) else int(e.code or 0)

    if args.count < 0:
        print("error: --count must be >= 0", file=sys.stderr)
        return 2

    try:
        out_dir = Path(args.output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"error: cannot create output dir {args.output_dir}: {type(e).__name__}",
              file=sys.stderr)
        return 2

    strategy_ids = [s.strip() for s in args.strategies.split(",") if s.strip()]
    try:
        strategies = _filter_strategies(strategy_ids or None)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    scenarios = _pick_scenarios(args.count)
    rows_by_strategy = compare_strategies(strategies, scenarios)
    report = build_comparison_report(
        rows_by_strategy, scenarios,
        generated_at=_now_iso(), seed=int(args.seed),
    )

    written_path: Optional[Path] = None
    if not args.summary_only:
        written_path = _write_report(out_dir, report)

    _print_summary(report, written_path)

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))

    if args.strict and _count_auto_fails(rows_by_strategy) > 0:
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
