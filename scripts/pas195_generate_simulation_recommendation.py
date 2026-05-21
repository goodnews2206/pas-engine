"""
PAS195 — Generate a CANDIDATE strategy recommendation from
simulation evidence.

Either runs the PAS194 comparison fresh or reads an existing
comparison report file, then emits a single CANDIDATE
recommendation for operator review. Never autonomously applies
the recommendation. Never mutates production state.

Safety doctrine (enforced by tests and the readiness gate):

  * Output `status` is always "CANDIDATE".
  * Output `operator_required` is always True.
  * Never imports twilio, slack_sdk, openai, anthropic, dotenv,
    supabase, or the live state machine.
  * Never reads .env, never opens a network connection.
  * Never writes outside reports/simulations/.

Exit codes:
  0 — recommendation generated.
  2 — bad CLI args / unreadable input / unwritable output dir.
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


from app.services.simulation.scenarios import SCENARIOS  # noqa: E402
from app.services.simulation.strategies import STRATEGIES  # noqa: E402
from app.services.simulation.comparison import (  # noqa: E402
    build_comparison_report,
    compare_strategies,
)
from app.services.simulation.recommendations import (  # noqa: E402
    DEFAULT_PASS_RATE_THRESHOLD,
    generate_recommendation,
)


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


REPORTS_SUBDIR = Path("reports") / "simulations"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _read_comparison_from_disk(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    return json.loads(raw)


def _build_fresh_comparison(seed: int) -> dict:
    rows = compare_strategies(STRATEGIES, SCENARIOS)
    return build_comparison_report(
        rows, SCENARIOS,
        generated_at=_now_iso(),
        seed=seed,
    )


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="pas195_generate_simulation_recommendation",
        description=(
            "PAS195 — Generate a CANDIDATE strategy recommendation "
            "from PAS194 simulation evidence. Operator review "
            "required before any downstream action."
        ),
    )
    p.add_argument("--from-report", default="",
                   help="path to an existing PAS194 comparison report JSON")
    p.add_argument("--pass-rate-threshold", type=float,
                   default=DEFAULT_PASS_RATE_THRESHOLD,
                   help="minimum pass_rate for recommendation (default 0.95)")
    p.add_argument("--seed", type=int, default=0,
                   help="seed for fresh PAS194 comparison (ignored if --from-report)")
    p.add_argument("--output-dir", default=str(_REPO_ROOT / REPORTS_SUBDIR),
                   help="directory to write the recommendation JSON into")
    p.add_argument("--summary-only", action="store_true",
                   help="do not write a JSON report file; print summary only")
    p.add_argument("--json", action="store_true",
                   help="print the full recommendation payload as JSON to stdout")
    return p


def _write_report(out_dir: Path, payload: dict) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = payload.get("generated_at", _now_iso()).replace(":", "").replace("-", "")
    name = f"pas195_recommendation_{ts}_{payload['recommendation_id']}.json"
    fp = out_dir / name
    fp.write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return fp


def _print_summary(rec: dict, written_path: Optional[Path]) -> None:
    print(
        f"[PAS195] type={rec['recommendation_type']} "
        f"status={rec['status']} "
        f"operator_required={rec['operator_required']} "
        f"confidence={rec['confidence_level']} "
        f"recommended={rec['recommended_strategy']} "
        f"rejected={rec['rejected_strategy']} "
        f"threshold={rec['pass_rate_threshold']}"
    )
    ev = rec.get("evidence_summary") or {}
    disqualified = ev.get("disqualified_strategies") or []
    if disqualified:
        print(f"[PAS195] disqualified: {', '.join(disqualified)}")
    tied = ev.get("tied_safe_strategies") or []
    if tied:
        print(f"[PAS195] tied at top: {', '.join(tied)}")
    print(f"[PAS195] safety: {rec['safety_notes']}")
    if written_path is not None:
        print(f"[PAS195] recommendation written: {written_path}")


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as e:
        return 2 if e.code not in (0, None) else int(e.code or 0)

    if args.pass_rate_threshold < 0.0 or args.pass_rate_threshold > 1.0:
        print("error: --pass-rate-threshold must be in [0.0, 1.0]",
              file=sys.stderr)
        return 2

    try:
        out_dir = Path(args.output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"error: cannot create output dir {args.output_dir}: {type(e).__name__}",
              file=sys.stderr)
        return 2

    if args.from_report:
        path = Path(args.from_report)
        if not path.is_file():
            print(f"error: --from-report path not a file: {path}",
                  file=sys.stderr)
            return 2
        try:
            comparison = _read_comparison_from_disk(path)
        except Exception as e:
            print(f"error: cannot read {path}: {type(e).__name__}",
                  file=sys.stderr)
            return 2
    else:
        comparison = _build_fresh_comparison(int(args.seed))

    rec = generate_recommendation(
        comparison,
        pass_rate_threshold=float(args.pass_rate_threshold),
        generated_at=_now_iso(),
    )

    written_path: Optional[Path] = None
    if not args.summary_only:
        written_path = _write_report(out_dir, rec)

    _print_summary(rec, written_path)

    if args.json:
        print(json.dumps(rec, indent=2, sort_keys=True))

    return 0


if __name__ == "__main__":
    sys.exit(main())
