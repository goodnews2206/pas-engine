"""
PAS200 — Evaluate the behavioural quality of a PAS198 runtime.

Reads a PAS198 runtime artefact (and optionally a PAS199 inspection
artefact), produces the structured PAS200 behavioural-evaluation
artefact, and writes it under reports/simulations/. The evaluation
is strictly read-only and SIMULATION_ONLY; it cannot mutate any
system, re-execute any runtime, or promote any strategy.

Safety doctrine (enforced by tests and the readiness gate):

  * Output carries phase=PAS200,
    allowed_environment=SIMULATION_ONLY,
    live_behavior_changed=False.
  * Never imports twilio, slack_sdk, openai, anthropic, dotenv,
    supabase, or the live state machine.
  * Never reads .env, never opens a network connection.
  * Never writes outside reports/simulations/.

Exit codes:
  0 — evaluation written.
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


from app.services.simulation.behavioral_evaluation import (  # noqa: E402
    BehavioralEvaluationValidationError,
    build_behavioral_evaluation,
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
        prog="pas200_evaluate_runtime_behavior",
        description=(
            "PAS200 — Behavioural-quality evaluation of a PAS198 "
            "runtime artefact. Optional PAS199 inspection cross-"
            "references the lineage. Evaluation is SIMULATION_ONLY "
            "and cannot mutate any system."
        ),
    )
    p.add_argument("--runtime", required=True,
                   help="path to a PAS198 runtime JSON artefact")
    p.add_argument("--inspection", default=None,
                   help="optional PAS199 inspection JSON for cross-"
                        "reference")
    p.add_argument("--output-dir",
                   default=str(_REPO_ROOT / REPORTS_SUBDIR),
                   help="directory to write the evaluation JSON into")
    p.add_argument("--summary-only", action="store_true",
                   help="do not write a JSON file; print summary only")
    p.add_argument("--json", action="store_true",
                   help="print the full evaluation payload as JSON")
    return p


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_evaluation(out_dir: Path, payload: dict) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = payload.get("generated_at", _now_iso()).replace(":", "").replace("-", "")
    name = (
        f"pas200_behavioral_evaluation_{ts}_"
        f"{payload['behavioral_evaluation_id']}.json"
    )
    fp = out_dir / name
    fp.write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return fp


def _print_summary(ev: dict, written_path: Optional[Path]) -> None:
    agg = ev.get("aggregate_scores") or {}
    integ = ev.get("artifact_integrity") or {}
    failed_integ = [k for k, v in integ.items() if v is False]
    print(
        f"[PAS200] behavioral_evaluation_id={ev['behavioral_evaluation_id']} "
        f"phase={ev['phase']} "
        f"environment={ev['allowed_environment']} "
        f"live_behavior_changed={ev['live_behavior_changed']}"
    )
    print(
        f"[PAS200] runtime_id={ev['runtime_id']} "
        f"inspection_id={ev.get('inspection_id') or '-'} "
        f"transcript_hash={ev['transcript_hash'][:16]}..."
    )
    print(
        f"[PAS200] aggregate_scores "
        f"pressure={agg.get('pressure_score')} "
        f"pacing={agg.get('pacing_score')} "
        f"continuity={agg.get('continuity_score')} "
        f"trust={agg.get('trust_score')} "
        f"friction={agg.get('friction_score')}"
    )
    print(
        f"[PAS200] scenarios={len(ev.get('scenario_summaries') or [])} "
        f"turn_annotations={len(ev.get('turn_annotations') or [])} "
        f"behavioral_flags={','.join(ev.get('behavioral_flags') or []) or '-'}"
    )
    print(
        f"[PAS200] artifact_integrity ok="
        f"{len(integ) - len(failed_integ)}/{len(integ)}"
        + (f" failed={','.join(failed_integ)}" if failed_integ else "")
    )
    if written_path is not None:
        print(f"[PAS200] evaluation written: {written_path}")


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as e:
        return 2 if e.code not in (0, None) else int(e.code or 0)

    rt_path = Path(args.runtime)
    if not rt_path.is_file():
        print(f"error: --runtime path not a file: {rt_path}", file=sys.stderr)
        return 2

    insp_path: Optional[Path] = None
    if args.inspection:
        insp_path = Path(args.inspection)
        if not insp_path.is_file():
            print(
                f"error: --inspection path not a file: {insp_path}",
                file=sys.stderr,
            )
            return 2

    try:
        runtime = _read_json(rt_path)
        inspection: Optional[dict] = None
        if insp_path is not None:
            inspection = _read_json(insp_path)
    except Exception as e:
        print(f"error: cannot read inputs: {type(e).__name__}",
              file=sys.stderr)
        return 2

    try:
        out_dir = Path(args.output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(
            f"error: cannot create output dir {args.output_dir}: "
            f"{type(e).__name__}",
            file=sys.stderr,
        )
        return 2

    try:
        ev = build_behavioral_evaluation(
            runtime,
            generated_at=_now_iso(),
            inspection=inspection,
        )
    except BehavioralEvaluationValidationError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    written_path: Optional[Path] = None
    if not args.summary_only:
        written_path = _write_evaluation(out_dir, ev)

    _print_summary(ev, written_path)

    if args.json:
        print(json.dumps(ev, indent=2, sort_keys=True))

    return 0


if __name__ == "__main__":
    sys.exit(main())
