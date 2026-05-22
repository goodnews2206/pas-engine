"""
PAS203-B — Deployed evidence digest readiness gate.

Deterministic, read-only evaluator for "is at least one bounded
SIMULATION_ONLY PAS201 digest artifact committed under
reports/simulations/ so that the deployed PAS203 Slack surface
returns a real digest summary instead of the missing-digest
fallback?"

Walks the repo and verifies:

  * At least one file matching the PAS203 loader's strict
    filename regex
    (`pas201_simulation_evidence_digest_<ts>_pas201-dgst-<hex>.json`)
    exists under reports/simulations/.
  * That file parses as JSON.
  * That file carries phase == "PAS201".
  * That file carries allowed_environment == "SIMULATION_ONLY".
  * That file carries live_behavior_changed == False.
  * That file carries no PII-shaped tokens (phone, email, SSN).
  * That file carries no production brokerage UUIDs.
  * That file carries no secret-shaped tokens.
  * The PAS203 loader (find_latest_digest_path + load_digest)
    accepts the file end-to-end on a clean import.

This gate is intentionally tiny and additive: it does not assert
anything about PAS193-PAS202 carry-forward (those are owned by
their own gates). Its single responsibility is "did a bounded
digest artefact ship?"

Exit codes:
  0 — READY
  1 — NOT_READY
  2 — bad CLI args
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional, Tuple


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


_REPO_ROOT_DEFAULT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)


VERDICT_READY     = "READY"
VERDICT_NOT_READY = "NOT_READY"
SEVERITY_BLOCK    = "BLOCK"


REPORTS_SUBDIR = "reports/simulations"

_DIGEST_FILENAME_RE = re.compile(
    r"^pas201_simulation_evidence_digest_"
    r"[0-9TZ]{8,32}_"
    r"pas201-dgst-[0-9a-f]{8,32}"
    r"\.json$"
)


_PII_PATTERNS: Tuple[Tuple[str, "re.Pattern[str]"], ...] = (
    ("phone_3-3-4",    re.compile(r"\b\d{3}[\s.\-]\d{3}[\s.\-]\d{4}\b")),
    ("phone_parens",   re.compile(r"\(\d{3}\)\s*\d{3}[\s.\-]?\d{4}")),
    ("phone_intl",     re.compile(r"\+\d[\d\s.\-]{6,14}\d")),
    ("email",          re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")),
    ("ssn",            re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
)


_PROD_ID_PATTERNS: Tuple[Tuple[str, "re.Pattern[str]"], ...] = (
    ("uuid_v4_like",     re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b")),
    ("brokerage_id_eq",  re.compile(r"brokerage_id\s*=\s*[\"']?[0-9a-fA-F\-]{8,}[\"']?")),
)


_SECRET_PATTERNS: Tuple[Tuple[str, "re.Pattern[str]"], ...] = (
    ("aws_key",       re.compile(r"AKIA[0-9A-Z]{12,}")),
    ("slack_token",   re.compile(r"xox[bp]-[0-9A-Za-z\-]{10,}")),
    ("stripe_key",    re.compile(r"sk_(live|test)_[A-Za-z0-9]{16,}")),
    ("twilio_account", re.compile(r"\bAC[0-9a-fA-F]{32}\b")),
    ("twilio_secret", re.compile(r"\bSK[0-9a-fA-F]{32}\b")),
    ("pem_key",       re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
)


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _check(check_id: str, status: str, description: str,
           detail: str = "", severity: str = SEVERITY_BLOCK) -> dict:
    return {
        "id":          check_id,
        "status":      status,
        "description": description,
        "detail":      detail,
        "severity":    severity,
    }


def _find_digests(repo_root: Path) -> List[Path]:
    d = repo_root / REPORTS_SUBDIR
    if not d.is_dir():
        return []
    out: List[Path] = []
    for entry in d.iterdir():
        if not entry.is_file():
            continue
        if _DIGEST_FILENAME_RE.match(entry.name):
            out.append(entry)
    out.sort(key=lambda x: x.name, reverse=True)
    return out


def _check_artifact(path: Path) -> List[dict]:
    out: List[dict] = []
    rel = path.name
    try:
        raw = path.read_text(encoding="utf-8")
    except Exception as e:
        out.append(_check(
            f"artifact:readable:{rel}",
            "FAIL",
            f"{rel} is readable",
            detail=type(e).__name__,
        ))
        return out
    out.append(_check(
        f"artifact:readable:{rel}",
        "PASS",
        f"{rel} is readable",
    ))
    try:
        digest = json.loads(raw)
    except Exception as e:
        out.append(_check(
            f"artifact:json_parses:{rel}",
            "FAIL",
            f"{rel} parses as JSON",
            detail=type(e).__name__,
        ))
        return out
    out.append(_check(
        f"artifact:json_parses:{rel}",
        "PASS",
        f"{rel} parses as JSON",
    ))
    out.append(_check(
        f"artifact:phase_pas201:{rel}",
        "PASS" if digest.get("phase") == "PAS201" else "FAIL",
        f"{rel} carries phase=PAS201",
        detail=str(digest.get("phase")),
    ))
    out.append(_check(
        f"artifact:env_simulation_only:{rel}",
        "PASS" if digest.get("allowed_environment") == "SIMULATION_ONLY" else "FAIL",
        f"{rel} carries allowed_environment=SIMULATION_ONLY",
        detail=str(digest.get("allowed_environment")),
    ))
    out.append(_check(
        f"artifact:live_behavior_changed_false:{rel}",
        "PASS" if digest.get("live_behavior_changed") is False else "FAIL",
        f"{rel} carries live_behavior_changed=False",
        detail=str(digest.get("live_behavior_changed")),
    ))

    pii_hits = []
    for name, pat in _PII_PATTERNS:
        if pat.search(raw):
            pii_hits.append(name)
    out.append(_check(
        f"artifact:no_pii:{rel}",
        "FAIL" if pii_hits else "PASS",
        f"{rel} contains no PII-shaped tokens",
        detail=", ".join(pii_hits) if pii_hits else "",
    ))

    prod_hits = []
    for name, pat in _PROD_ID_PATTERNS:
        if pat.search(raw):
            prod_hits.append(name)
    out.append(_check(
        f"artifact:no_production_brokerage_ids:{rel}",
        "FAIL" if prod_hits else "PASS",
        f"{rel} contains no production brokerage UUIDs",
        detail=", ".join(prod_hits) if prod_hits else "",
    ))

    sec_hits = []
    for name, pat in _SECRET_PATTERNS:
        if pat.search(raw):
            sec_hits.append(name)
    out.append(_check(
        f"artifact:no_secret_shapes:{rel}",
        "FAIL" if sec_hits else "PASS",
        f"{rel} contains no secret-shaped tokens",
        detail=", ".join(sec_hits) if sec_hits else "",
    ))

    return out


def check_loader_smoke(repo_root: str) -> List[dict]:
    out: List[dict] = []
    sys.path.insert(0, repo_root)
    try:
        from app.services.slack.simulation_digest_intent import (  # type: ignore
            find_latest_digest_path,
            load_digest,
        )
        d = Path(repo_root) / REPORTS_SUBDIR
        latest = find_latest_digest_path(d)
        if latest is None:
            out.append(_check(
                "loader:finds_latest_digest_path",
                "FAIL",
                "PAS203 loader finds at least one committed digest under reports/simulations/",
                detail="no matching file",
            ))
            return out
        out.append(_check(
            "loader:finds_latest_digest_path",
            "PASS",
            "PAS203 loader finds at least one committed digest under reports/simulations/",
            detail=str(latest.name),
        ))
        try:
            digest = load_digest(latest)
            out.append(_check(
                "loader:load_digest_accepts_committed_artifact",
                "PASS",
                f"PAS203 loader accepts {latest.name} end-to-end",
            ))
            out.append(_check(
                "loader:digest_strong_environment_simulation_only",
                "PASS" if digest.get("allowed_environment") == "SIMULATION_ONLY" else "FAIL",
                "loaded digest carries allowed_environment=SIMULATION_ONLY",
            ))
            out.append(_check(
                "loader:digest_live_behavior_changed_false",
                "PASS" if digest.get("live_behavior_changed") is False else "FAIL",
                "loaded digest carries live_behavior_changed=False",
            ))
        except Exception as e:
            out.append(_check(
                "loader:load_digest_accepts_committed_artifact",
                "FAIL",
                f"PAS203 loader accepts {latest.name} end-to-end",
                detail=f"{type(e).__name__}: {str(e)[:200]}",
            ))
    except Exception as e:
        out.append(_check(
            "loader:smoke",
            "FAIL",
            "simulation_digest_intent module importable",
            detail=type(e).__name__,
        ))
    return out


def evaluate(repo_root: str) -> dict:
    root = Path(repo_root)
    checks: List[dict] = []

    digests = _find_digests(root)
    checks.append(_check(
        "artifact:at_least_one_digest_committed",
        "PASS" if digests else "FAIL",
        "at least one PAS201 digest artefact exists under reports/simulations/",
        detail=f"found {len(digests)}",
    ))
    if not digests:
        # Nothing more to do — every per-artifact check would
        # cascade off a missing file.
        agg_block = True
    else:
        for fp in digests:
            checks.extend(_check_artifact(fp))
        agg_block = False
        del agg_block  # silence unused

    checks.extend(check_loader_smoke(repo_root))

    blockers = [
        c for c in checks
        if c["status"] == "FAIL" and c.get("severity") == SEVERITY_BLOCK
    ]
    verdict = VERDICT_NOT_READY if blockers else VERDICT_READY
    return {
        "phase":            "PAS203-B",
        "generated_at":     _now_iso(),
        "verdict":          verdict,
        "ready":            verdict == VERDICT_READY,
        "blocker_count":    len(blockers),
        "info_count":       0,
        "check_count":      len(checks),
        "pass_count":       sum(1 for c in checks if c["status"] == "PASS"),
        "fail_count":       sum(1 for c in checks if c["status"] == "FAIL"),
        "checks":           checks,
        "operator_actions": [
            f"[{c.get('severity') or SEVERITY_BLOCK}] {c['id']} — {c.get('detail') or 'see report'}."
            for c in checks if c["status"] == "FAIL"
        ],
    }


REPORT_FILENAME = "pas203b_deployed_digest_readiness_report.json"


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="pas203b_deployed_digest_readiness_check",
        description=(
            "PAS203-B — Deployed Evidence Digest Artifact readiness "
            "gate. Read-only. Confirms at least one bounded "
            "SIMULATION_ONLY PAS201 digest artefact ships with the "
            "repository so the deployed PAS203 Slack surface returns "
            "a real digest, not the missing-digest fallback."
        ),
    )
    p.add_argument("--repo-root", default=_REPO_ROOT_DEFAULT)
    p.add_argument("--output",    default=REPORT_FILENAME)
    p.add_argument("--json",      action="store_true")
    p.add_argument("--summary-only", action="store_true")
    p.add_argument("--strict",    action="store_true")
    return p


def _print_summary(report: dict) -> None:
    print(
        f"[PAS203-B] verdict={report['verdict']} "
        f"blockers={report['blocker_count']} "
        f"info={report['info_count']} "
        f"checks={report['check_count']} "
        f"pass={report['pass_count']} "
        f"fail={report['fail_count']}"
    )
    actions = report.get("operator_actions") or []
    if actions:
        print("[PAS203-B] operator actions:")
        for a in actions[:25]:
            print(f"  - {a}")
        if len(actions) > 25:
            print(f"  ... and {len(actions) - 25} more (see report file)")


def _write_report(path: str, payload: dict) -> None:
    try:
        Path(path).write_text(
            json.dumps(payload, indent=2, sort_keys=True),
            encoding="utf-8",
        )
    except Exception as e:
        print(
            f"  [warn] failed to write report at {path}: "
            f"{type(e).__name__}",
            file=sys.stderr,
        )


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as e:
        return 2 if e.code not in (0, None) else int(e.code or 0)

    repo_root = os.path.abspath(args.repo_root or _REPO_ROOT_DEFAULT)
    if not os.path.isdir(repo_root):
        print(f"error: --repo-root not a directory: {repo_root}",
              file=sys.stderr)
        return 2

    report = evaluate(repo_root)

    if not args.summary_only:
        _write_report(args.output, report)

    _print_summary(report)

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))

    return 0 if report["verdict"] == VERDICT_READY else 1


if __name__ == "__main__":
    sys.exit(main())
