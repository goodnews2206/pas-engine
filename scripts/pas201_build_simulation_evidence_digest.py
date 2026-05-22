"""
PAS201 — Build the simulation evidence digest.

Reads the six bounded artefacts that comprise a complete PAS
simulation lineage (PAS195 recommendation, PAS196 review, PAS197
manual-test package, PAS198 runtime, PAS199 inspection, PAS200
behavioural evaluation) and emits the PAS201 evidence digest
under `reports/simulations/`. The digest is strictly read-only
and SIMULATION_ONLY; it cannot mutate any system, re-execute any
runtime, or promote any strategy.

Safety doctrine (enforced by tests and the readiness gate):

  * Output carries phase=PAS201,
    allowed_environment=SIMULATION_ONLY,
    live_behavior_changed=False.
  * Never imports twilio, slack_sdk, openai, anthropic, dotenv,
    supabase, or the live state machine.
  * Never reads .env, never opens a network connection.
  * Never writes outside reports/simulations/.

Exit codes:
  0 — digest written.
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


from app.services.simulation.evidence_digest import (  # noqa: E402
    EvidenceDigestValidationError,
    build_evidence_digest,
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
        prog="pas201_build_simulation_evidence_digest",
        description=(
            "PAS201 — Build the simulation evidence digest from "
            "PAS195 / PAS196 / PAS197 / PAS198 / PAS199 / PAS200 "
            "artefacts. Digest is SIMULATION_ONLY and cannot mutate "
            "any system."
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
    p.add_argument("--inspection", required=True,
                   help="path to a PAS199 inspection JSON")
    p.add_argument("--behavioral-evaluation", required=True,
                   help="path to a PAS200 behavioural evaluation JSON")
    p.add_argument("--output-dir",
                   default=str(_REPO_ROOT / REPORTS_SUBDIR),
                   help="directory to write the digest JSON into")
    p.add_argument("--summary-only", action="store_true",
                   help="do not write a JSON file; print summary only")
    p.add_argument("--json", action="store_true",
                   help="print the full digest payload as JSON")
    return p


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_digest(out_dir: Path, payload: dict) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = payload.get("generated_at", _now_iso()).replace(":", "").replace("-", "")
    name = (
        f"pas201_simulation_evidence_digest_{ts}_"
        f"{payload['digest_id']}.json"
    )
    fp = out_dir / name
    fp.write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return fp


def _print_summary(d: dict, written_path: Optional[Path]) -> None:
    rt   = d.get("runtime_summary")     or {}
    insp = d.get("inspection_summary")  or {}
    beh  = d.get("behavioral_summary")  or {}
    op   = d.get("operator_summary")    or {}
    integ = d.get("artifact_integrity") or {}
    failed = [k for k, v in integ.items() if v is False]
    print(
        f"[PAS201] digest_id={d['digest_id']} "
        f"phase={d['phase']} "
        f"strategy={d['strategy_id']} "
        f"environment={d['allowed_environment']} "
        f"live_behavior_changed={d['live_behavior_changed']}"
    )
    print(
        f"[PAS201] evidence_strength={d['evidence_strength']} "
        f"recommended_next_action={op.get('recommended_next_action')}"
    )
    print(
        f"[PAS201] runtime pass_rate={rt.get('pass_rate')} "
        f"average_score={rt.get('average_score')} "
        f"safety={rt.get('safety_outcome')} "
        f"auto_fail_count={rt.get('auto_fail_count')}"
    )
    print(
        f"[PAS201] inspection lineage_intact={insp.get('lineage_intact')} "
        f"integrity={insp.get('artifact_integrity_pass_ratio')}"
    )
    print(
        f"[PAS201] behavioral evaluation_id={beh.get('behavioral_evaluation_id')} "
        f"flags={','.join(beh.get('behavioral_flags') or []) or '-'}"
    )
    print(
        f"[PAS201] artifact_integrity ok="
        f"{len(integ) - len(failed)}/{len(integ)}"
        + (f" failed={','.join(failed)}" if failed else "")
    )
    print(
        f"[PAS201] highlights: {', '.join(op.get('highlights') or []) or '-'}"
    )
    print(
        f"[PAS201] claimable_now: {', '.join(d.get('claimable_now') or [])}"
    )
    print(
        f"[PAS201] not_claimable_yet: "
        f"{', '.join(d.get('not_claimable_yet') or [])}"
    )
    if written_path is not None:
        print(f"[PAS201] digest written: {written_path}")


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as e:
        return 2 if e.code not in (0, None) else int(e.code or 0)

    paths = {
        "--recommendation":        Path(args.recommendation),
        "--review":                Path(args.review),
        "--package":               Path(args.package),
        "--runtime":               Path(args.runtime),
        "--inspection":            Path(args.inspection),
        "--behavioral-evaluation": Path(args.behavioral_evaluation),
    }
    for flag, p in paths.items():
        if not p.is_file():
            print(f"error: {flag} path not a file: {p}", file=sys.stderr)
            return 2

    try:
        recommendation = _read_json(paths["--recommendation"])
        review         = _read_json(paths["--review"])
        package        = _read_json(paths["--package"])
        runtime        = _read_json(paths["--runtime"])
        inspection     = _read_json(paths["--inspection"])
        beval          = _read_json(paths["--behavioral-evaluation"])
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
        digest = build_evidence_digest(
            recommendation, review, package, runtime, inspection, beval,
            generated_at=_now_iso(),
        )
    except EvidenceDigestValidationError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    written_path: Optional[Path] = None
    if not args.summary_only:
        written_path = _write_digest(out_dir, digest)

    _print_summary(digest, written_path)

    if args.json:
        print(json.dumps(digest, indent=2, sort_keys=True))

    return 0


if __name__ == "__main__":
    sys.exit(main())
