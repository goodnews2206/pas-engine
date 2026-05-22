"""
PAS202 — Read-only operator viewer for the PAS201 simulation
evidence digest.

Reads a PAS201 digest JSON from disk and renders it for an
operator. By default prints the multi-line plain-text rendering;
flags switch to structured JSON, Slack-safe markdown, or both at
once. Can optionally write the structured operator-summary JSON
under reports/simulations/ for handoff to a teammate or auditor.

This is strictly a presentation layer. The viewer:

  * never imports twilio, slack_sdk, openai, anthropic, dotenv,
    supabase, or the live state machine
  * never reads .env, never opens a network connection
  * never sends a message to anyone
  * never mutates anything
  * writes only under reports/simulations/ (and only when
    explicitly requested via --write-summary)

Exit codes:
  0 — viewer ran cleanly.
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


from app.services.simulation.evidence_digest_surface import (  # noqa: E402
    EvidenceDigestSurfaceValidationError,
    format_digest_as_text,
    format_digest_for_slack,
    format_operator_summary,
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
        prog="pas202_view_simulation_evidence_digest",
        description=(
            "PAS202 — Read-only operator viewer for a PAS201 "
            "simulation evidence digest. Never mutates systems, "
            "never sends messages, never routes traffic."
        ),
    )
    p.add_argument("--digest", required=True,
                   help="path to a PAS201 digest JSON")
    p.add_argument("--output-dir",
                   default=str(_REPO_ROOT / REPORTS_SUBDIR),
                   help="directory to write the operator-summary "
                        "JSON into (only used with --write-summary)")
    p.add_argument("--json", action="store_true",
                   help="print the structured operator summary as JSON")
    p.add_argument("--slack", action="store_true",
                   help="print the Slack-safe markdown rendering")
    p.add_argument("--write-summary", action="store_true",
                   help="write the operator-summary JSON to the "
                        "output dir (read-only, simulation-only)")
    return p


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_summary(out_dir: Path, payload: dict, digest_id: str) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = _now_iso().replace(":", "").replace("-", "")
    name = f"pas202_evidence_digest_operator_summary_{ts}_{digest_id}.json"
    fp = out_dir / name
    fp.write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return fp


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as e:
        return 2 if e.code not in (0, None) else int(e.code or 0)

    digest_path = Path(args.digest)
    if not digest_path.is_file():
        print(f"error: --digest path not a file: {digest_path}",
              file=sys.stderr)
        return 2

    try:
        digest = _read_json(digest_path)
    except Exception as e:
        print(f"error: cannot read digest: {type(e).__name__}",
              file=sys.stderr)
        return 2

    try:
        summary = format_operator_summary(digest)
    except EvidenceDigestSurfaceValidationError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    # Default rendering is plain text.
    if not args.json and not args.slack:
        print(format_digest_as_text(digest))

    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))

    if args.slack:
        print(format_digest_for_slack(digest))

    if args.write_summary:
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
        written = _write_summary(out_dir, summary, summary["digest_id"])
        print(f"[PAS202] operator-summary written: {written}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
