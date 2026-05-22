"""
PAS199 — Inspect a complete PAS lineage and emit a bounded,
operator-facing inspection artefact.

Reads four artefacts from disk:

    --recommendation  : PAS195 recommendation JSON
    --review          : PAS196 review JSON
    --package         : PAS197 manual-test package JSON
    --runtime         : PAS198 runtime JSON
    --compare-runtime : (optional) a second PAS198 runtime JSON

Validates the joins, summarises the runtime / safety / capability
/ transcript surface, and writes the inspection artefact under
reports/simulations/. The inspection is strictly read-only and
cannot mutate any system.

Safety doctrine (enforced by tests and the readiness gate):

  * Output carries phase=PAS199,
    allowed_environment=SIMULATION_ONLY,
    live_behavior_changed=False.
  * Never imports twilio, slack_sdk, openai, anthropic, dotenv,
    supabase, or the live state machine.
  * Never reads .env, never opens a network connection.
  * Never writes outside reports/simulations/.

Exit codes:
  0 — inspection written.
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


from app.services.simulation.runtime_inspection import (  # noqa: E402
    RuntimeInspectionValidationError,
    build_inspection,
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
        prog="pas199_inspect_runtime_lineage",
        description=(
            "PAS199 — Read-only inspection of a PAS lineage "
            "(PAS195 -> PAS196 -> PAS197 -> PAS198). Optional second "
            "PAS198 runtime is diffed against the primary runtime. "
            "Inspection is SIMULATION_ONLY and cannot mutate any system."
        ),
    )
    p.add_argument("--recommendation", required=True,
                   help="path to a PAS195 recommendation JSON")
    p.add_argument("--review", required=True,
                   help="path to a PAS196 review envelope JSON")
    p.add_argument("--package", required=True,
                   help="path to a PAS197 manual-test package JSON")
    p.add_argument("--runtime", required=True,
                   help="path to a PAS198 runtime JSON")
    p.add_argument("--compare-runtime", default=None,
                   help="optional second PAS198 runtime JSON to diff "
                        "against --runtime")
    p.add_argument("--output-dir",
                   default=str(_REPO_ROOT / REPORTS_SUBDIR),
                   help="directory to write the inspection JSON into")
    p.add_argument("--summary-only", action="store_true",
                   help="do not write a JSON file; print summary only")
    p.add_argument("--json", action="store_true",
                   help="print the full inspection payload as JSON")
    return p


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_inspection(out_dir: Path, payload: dict) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = payload.get("generated_at", _now_iso()).replace(":", "").replace("-", "")
    name = f"pas199_runtime_inspection_{ts}_{payload['inspection_id']}.json"
    fp = out_dir / name
    fp.write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return fp


def _print_summary(insp: dict, written_path: Optional[Path]) -> None:
    lin  = insp.get("lineage_summary") or {}
    rt   = insp.get("runtime_summary") or {}
    safe = insp.get("safety_summary") or {}
    caps = insp.get("capability_summary") or {}
    tr   = insp.get("transcript_summary") or {}
    integ = insp.get("artifact_integrity") or {}
    comp = insp.get("comparison")

    print(
        f"[PAS199] inspection_id={insp['inspection_id']} "
        f"phase={insp['phase']} "
        f"environment={insp['allowed_environment']} "
        f"live_behavior_changed={insp['live_behavior_changed']}"
    )
    print(
        f"[PAS199] lineage strategy={lin.get('strategy_id')} "
        f"rec={lin.get('recommendation_id')} "
        f"rev={lin.get('review_id')} "
        f"pkg={lin.get('package_id')} "
        f"rt={lin.get('runtime_id')} "
        f"intact={lin.get('lineage_intact')}"
    )
    print(
        f"[PAS199] runtime strategy={rt.get('executed_strategy')} "
        f"execution_status={rt.get('execution_status')} "
        f"scenarios_executed={rt.get('scenarios_executed')} "
        f"pass_rate={rt.get('pass_rate')} "
        f"average_score={rt.get('average_score')}"
    )
    print(
        f"[PAS199] safety outcome={safe.get('outcome')} "
        f"auto_fail_count={safe.get('auto_fail_count')} "
        f"unsafe_count={safe.get('unsafe_output_count')} "
        f"halluc_count={safe.get('hallucinated_policy_count')} "
        f"pii_count={safe.get('pii_leak_count')}"
    )
    print(
        f"[PAS199] capability_rates "
        f"qualification={caps.get('qualification_captured_rate')} "
        f"objection={caps.get('objection_handled_rate')} "
        f"callback={caps.get('callback_captured_rate')} "
        f"booking={caps.get('booking_attempted_rate')}"
    )
    print(
        f"[PAS199] transcript scenarios={tr.get('scenario_count')} "
        f"total_turns={tr.get('total_turns')} "
        f"agent_turns={tr.get('agent_turns')} "
        f"lead_turns={tr.get('lead_turns')}"
    )
    failed_integrity = [k for k, v in integ.items() if v is False]
    print(
        f"[PAS199] artifact_integrity ok={len(integ) - len(failed_integrity)}"
        f"/{len(integ)}"
        + (f" failed={','.join(failed_integrity)}" if failed_integrity else "")
    )
    if comp is not None:
        sd = comp.get("safety_delta") or {}
        td = comp.get("transcript_size_delta") or {}
        print(
            f"[PAS199] comparison runtime_b={comp.get('compared_runtime_id')} "
            f"pass_rate_delta={comp.get('pass_rate_delta')} "
            f"average_score_delta={comp.get('average_score_delta')} "
            f"safety_outcome_changed={sd.get('outcome_changed')} "
            f"auto_fail_delta={sd.get('auto_fail_count_delta')} "
            f"total_turns_delta={td.get('total_turns_delta')} "
            f"flipped={len(comp.get('flipped_scenarios') or [])}"
        )
    if written_path is not None:
        print(f"[PAS199] inspection written: {written_path}")


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as e:
        return 2 if e.code not in (0, None) else int(e.code or 0)

    paths = {
        "--recommendation": Path(args.recommendation),
        "--review":         Path(args.review),
        "--package":        Path(args.package),
        "--runtime":        Path(args.runtime),
    }
    for flag, p in paths.items():
        if not p.is_file():
            print(f"error: {flag} path not a file: {p}", file=sys.stderr)
            return 2

    compare_path: Optional[Path] = None
    if args.compare_runtime:
        compare_path = Path(args.compare_runtime)
        if not compare_path.is_file():
            print(
                f"error: --compare-runtime path not a file: "
                f"{compare_path}",
                file=sys.stderr,
            )
            return 2

    try:
        recommendation = _read_json(paths["--recommendation"])
        review         = _read_json(paths["--review"])
        package        = _read_json(paths["--package"])
        runtime        = _read_json(paths["--runtime"])
        compare_rt: Optional[dict] = None
        if compare_path is not None:
            compare_rt = _read_json(compare_path)
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
        insp = build_inspection(
            recommendation, review, package, runtime,
            generated_at=_now_iso(),
            compare_runtime=compare_rt,
        )
    except RuntimeInspectionValidationError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    written_path: Optional[Path] = None
    if not args.summary_only:
        written_path = _write_inspection(out_dir, insp)

    _print_summary(insp, written_path)

    if args.json:
        print(json.dumps(insp, indent=2, sort_keys=True))

    return 0


if __name__ == "__main__":
    sys.exit(main())
