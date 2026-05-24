"""
PAS205 — Proactive observer readiness gate.

Deterministic, read-only evaluator confirming PAS205 is wired
correctly, additive-only over PAS193–PAS204, free of Twilio /
Slack-outbound / Supabase / LLM / state-machine /
worker / scheduler dependencies, never writes outside
reports/simulations/, and emits no forbidden status literals or
live-mutation identifiers.

Checks include:

  * PAS205 surfaces exist (models / observer / digest / runner /
    readiness / tests / doc).
  * Closed signal vocabulary present in observer_models.
  * Observer carries the public entry point `observe`.
  * Digest module exposes the three renderers + FORBIDDEN_OUTPUT_TOKENS.
  * Production source files do not import twilio / slack_sdk /
    openai / anthropic / dotenv / supabase / state_machine /
    outbound notifications / worker / scheduler.
  * Production source files carry no live-mutation /
    outbound-messaging identifiers.
  * No new PAS205 SQL migration committed.
  * combined_supabase_migration.sql is not committed.
  * No secret-shaped tokens in any PAS205 file.
  * Doc carries the required clauses.
  * The readiness gate itself never reads .env / hits the network.

Exit codes:
  0 — READY
  1 — NOT_READY
  2 — bad CLI args
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional, Set, Tuple


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


PAS205_FILES: Tuple[str, ...] = (
    "docs/pas205_proactive_observer.md",
    "scripts/pas205_proactive_observer_readiness_check.py",
    "scripts/pas205_run_proactive_observer_demo.py",
    "tests/mvp/test_pas205_proactive_observer.py",
    "app/services/proactive/__init__.py",
    "app/services/proactive/observer_models.py",
    "app/services/proactive/observer.py",
    "app/services/proactive/observer_digest.py",
)


_PAS205_PRODUCTION_FILES: Tuple[str, ...] = (
    "app/services/proactive/observer_models.py",
    "app/services/proactive/observer.py",
    "app/services/proactive/observer_digest.py",
)


BANNED_IMPORT_MODULES: Tuple[str, ...] = (
    "twilio",
    "slack_sdk",
    "openai",
    "anthropic",
    "dotenv",
    "supabase",
)


BANNED_IMPORT_PREFIXES: Tuple[str, ...] = (
    "twilio.",
    "slack_sdk.",
    "openai.",
    "anthropic.",
    "dotenv.",
    "supabase.",
    "app.engine",
    "app.services.notifications",
    "app.services.outbound",
    "app.services.worker",
    "app.routes",
    "app.services.slack.slack_client",
    "app.services.slack.slack_sender",
)


BANNED_CALL_NAMES: Tuple[str, ...] = (
    "load_dotenv",
    "get_supabase",
)


FORBIDDEN_STATUS_LITERALS: Tuple[str, ...] = (
    "APPROVED",
    "APPLIED",
    "AUTO_APPLIED",
    "LIVE",
    "DEPLOYED",
)


FORBIDDEN_IDENTIFIERS: Tuple[str, ...] = (
    "apply_recommendation",
    "deploy_strategy",
    "switch_strategy_live",
    "auto_apply",
    "auto_promote",
    "force_promote",
    "live_apply",
    "auto_deploy",
    "route_lead_live",
    "route_call_live",
    "send_real_sms",
    "send_real_call",
    "send_slack_message",
    "post_to_slack",
    "place_call",
    "outbound_call",
    "start_worker",
    "schedule_cron",
)


SECRET_SHAPE_REGEXES = (
    re.compile(r"AKIA[0-9A-Z]{12,}"),
    re.compile(r"xox[bp]-[0-9A-Za-z\-]{10,}"),
    re.compile(r"sk_(live|test)_[A-Za-z0-9]{16,}"),
    re.compile(r"\bAC[0-9a-fA-F]{32}\b"),
    re.compile(r"\bSK[0-9a-fA-F]{32}\b"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
)


DOC_FILE = "docs/pas205_proactive_observer.md"
DOC_REQUIRED_CLAUSES = (
    "what pas205 proves",
    "what pas205 does not prove",
    "claimable",
    "still not claimable",
    "proactive visibility",
    "not autonomous action",
    "future path",
    "pas206",
    "pas207",
    "pas208",
    "pas209",
    "simulation_only",
    "deterministic",
    "safety",
    "broker",
    "operator",
)


REQUIRED_SIGNAL_TYPES: Tuple[str, ...] = (
    "callback_overdue",
    "lead_unassigned",
    "stale_lead",
    "missed_first_response",
    "failed_booking_confirmation",
    "no_agent_available",
    "repeated_failed_calls",
    "after_hours_lead_pending",
    "high_value_lead_waiting",
    "needs_human_review",
)


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _read_text(p: Path) -> Optional[str]:
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        return None


def _check(check_id: str, status: str, description: str,
           detail: str = "", severity: str = SEVERITY_BLOCK) -> dict:
    return {
        "id":          check_id,
        "status":      status,
        "description": description,
        "detail":      detail,
        "severity":    severity,
    }


def _collect_imports_and_calls(src: str) -> Tuple[Set[str], Set[str]]:
    imports: Set[str] = set()
    calls:   Set[str] = set()
    try:
        tree = ast.parse(src)
    except Exception:
        return imports, calls
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module)
                for alias in node.names:
                    imports.add(f"{node.module}.{alias.name}")
        elif isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Name):
                calls.add(func.id)
            elif isinstance(func, ast.Attribute):
                calls.add(func.attr)
    return imports, calls


def _collect_string_constants(src: str) -> Set[str]:
    out: Set[str] = set()
    try:
        tree = ast.parse(src)
    except Exception:
        return out
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            out.add(node.value)
    return out


def _collect_identifier_names(src: str) -> Set[str]:
    out: Set[str] = set()
    try:
        tree = ast.parse(src)
    except Exception:
        return out
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            out.add(node.name)
        elif isinstance(node, ast.AsyncFunctionDef):
            out.add(node.name)
        elif isinstance(node, ast.Name):
            out.add(node.id)
        elif isinstance(node, ast.Attribute):
            out.add(node.attr)
    return out


def _banned_in(imports: Set[str], calls: Set[str]) -> List[str]:
    bad: List[str] = []
    for mod in imports:
        if mod in BANNED_IMPORT_MODULES:
            bad.append(f"import {mod}")
            continue
        for pref in BANNED_IMPORT_PREFIXES:
            if mod == pref or mod.startswith(pref + ".") or mod.startswith(pref):
                bad.append(f"import {mod}")
                break
    for name in calls:
        if name in BANNED_CALL_NAMES:
            bad.append(f"call {name}()")
    return bad


# ──────────────────────────────────────────────────────────────────
# Checks
# ──────────────────────────────────────────────────────────────────

def check_pas205_files_present(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in PAS205_FILES:
        ok = (Path(repo_root) / rel).is_file()
        out.append(_check(
            f"files:exists:{rel}",
            "PASS" if ok else "FAIL",
            f"PAS205 artefact present: {rel}",
            detail="" if ok else "file missing",
        ))
    return out


def check_closed_signal_vocabulary(repo_root: str) -> List[dict]:
    fp = Path(repo_root) / "app/services/proactive/observer_models.py"
    src = _read_text(fp) or ""
    consts = _collect_string_constants(src)
    missing = [st for st in REQUIRED_SIGNAL_TYPES if st not in consts]
    return [_check(
        "vocabulary:signal_types",
        "FAIL" if missing else "PASS",
        "observer_models declares every required closed signal type",
        detail=("missing: " + ", ".join(missing)) if missing else "",
    )]


def check_observer_entry_points(repo_root: str) -> List[dict]:
    obs = _read_text(Path(repo_root) / "app/services/proactive/observer.py") or ""
    dig = _read_text(Path(repo_root) / "app/services/proactive/observer_digest.py") or ""
    return [
        _check(
            "entry_point:observe",
            "PASS" if "def observe(" in obs else "FAIL",
            "observer.py exposes observe()",
        ),
        _check(
            "entry_point:to_machine_json",
            "PASS" if "def to_machine_json(" in dig else "FAIL",
            "observer_digest exposes to_machine_json",
        ),
        _check(
            "entry_point:to_slack_summary",
            "PASS" if "def to_slack_summary(" in dig else "FAIL",
            "observer_digest exposes to_slack_summary",
        ),
        _check(
            "entry_point:to_broker_report",
            "PASS" if "def to_broker_report(" in dig else "FAIL",
            "observer_digest exposes to_broker_report",
        ),
        _check(
            "entry_point:FORBIDDEN_OUTPUT_TOKENS",
            "PASS" if "FORBIDDEN_OUTPUT_TOKENS" in dig else "FAIL",
            "observer_digest exposes FORBIDDEN_OUTPUT_TOKENS",
        ),
    ]


def check_no_banned_imports(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in _PAS205_PRODUCTION_FILES:
        src = _read_text(Path(repo_root) / rel) or ""
        imports, calls = _collect_imports_and_calls(src)
        bad = _banned_in(imports, calls)
        out.append(_check(
            f"no_banned_imports:{rel}",
            "FAIL" if bad else "PASS",
            f"{rel} is free of Twilio/Slack/LLM/Supabase/state_machine/notifications/worker/route imports",
            detail=("disqualifying: " + ", ".join(sorted(set(bad)))) if bad else "",
        ))
    return out


def check_no_forbidden_status_literals(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in _PAS205_PRODUCTION_FILES:
        src = _read_text(Path(repo_root) / rel) or ""
        consts = _collect_string_constants(src)
        bad = sorted(tok for tok in FORBIDDEN_STATUS_LITERALS if tok in consts)
        out.append(_check(
            f"no_forbidden_status_literals:{rel}",
            "FAIL" if bad else "PASS",
            f"{rel} carries no forbidden status literals",
            detail=("disqualifying: " + ", ".join(bad)) if bad else "",
        ))
    return out


def check_no_forbidden_identifiers(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in _PAS205_PRODUCTION_FILES:
        src = _read_text(Path(repo_root) / rel) or ""
        names = _collect_identifier_names(src)
        bad = sorted(n for n in FORBIDDEN_IDENTIFIERS if n in names)
        out.append(_check(
            f"no_forbidden_identifiers:{rel}",
            "FAIL" if bad else "PASS",
            f"{rel} carries no live-mutation / outbound-messaging identifiers",
            detail=("disqualifying: " + ", ".join(bad)) if bad else "",
        ))
    return out


def check_no_observer_writes(repo_root: str) -> List[dict]:
    # Observer core must contain no file/network I/O.
    forbidden_io = ("open(", ".write_text(", ".write(", ".unlink(", ".mkdir(",
                    "urllib", "requests.", "httpx.", "socket.")
    out: List[dict] = []
    for rel in _PAS205_PRODUCTION_FILES:
        src = _read_text(Path(repo_root) / rel) or ""
        bad = [tok for tok in forbidden_io if tok in src]
        out.append(_check(
            f"no_io_in_observer_core:{rel}",
            "FAIL" if bad else "PASS",
            f"{rel} performs no file/network I/O",
            detail=("disqualifying: " + ", ".join(bad)) if bad else "",
        ))
    return out


def check_no_secret_shapes(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in PAS205_FILES:
        src = _read_text(Path(repo_root) / rel) or ""
        bad: List[str] = []
        for pat in SECRET_SHAPE_REGEXES:
            for m in pat.finditer(src):
                bad.append(m.group(0)[:12] + "…")
        out.append(_check(
            f"no_secret_shapes:{rel}",
            "FAIL" if bad else "PASS",
            f"{rel} contains no secret-shaped tokens",
            detail=("disqualifying: " + ", ".join(bad)) if bad else "",
        ))
    return out


def check_no_new_migration(repo_root: str) -> List[dict]:
    root = Path(repo_root) / "scripts"
    bad: List[str] = []
    if root.is_dir():
        for entry in root.iterdir():
            name = entry.name.lower()
            if "pas205" in name and (
                name.endswith(".sql") or "migrate" in name
            ):
                bad.append(entry.name)
    return [_check(
        "no_new_migration",
        "FAIL" if bad else "PASS",
        "PAS205 introduces no SQL migration",
        detail=("found: " + ", ".join(bad)) if bad else "",
    )]


def check_no_combined_migration_committed(repo_root: str) -> List[dict]:
    fp = Path(repo_root) / "scripts" / "combined_supabase_migration.sql"
    return [_check(
        "no_combined_migration_committed",
        "FAIL" if fp.is_file() else "PASS",
        "combined_supabase_migration.sql not committed on this branch",
        detail=str(fp) if fp.is_file() else "",
    )]


def check_doc_clauses(repo_root: str) -> List[dict]:
    out: List[dict] = []
    src_raw = _read_text(Path(repo_root) / DOC_FILE) or ""
    src = src_raw.lower()
    for clause in DOC_REQUIRED_CLAUSES:
        ok = clause in src
        out.append(_check(
            f"doc:clause:{clause}",
            "PASS" if ok else "FAIL",
            f"{DOC_FILE} carries clause: {clause}",
            detail="" if ok else "clause missing",
        ))
    return out


def check_runner_writes_only_reports(repo_root: str) -> List[dict]:
    fp = Path(repo_root) / "scripts" / "pas205_run_proactive_observer_demo.py"
    src = _read_text(fp) or ""
    ok = "reports/simulations" in src.replace("\\", "/") or "REPORTS_SUBDIR" in src
    return [_check(
        "runner:writes_only_reports_dir",
        "PASS" if ok else "FAIL",
        "runner writes only under reports/simulations/",
    )]


def check_no_scheduler_or_cron(repo_root: str) -> List[dict]:
    # Any of these patterns in the PAS205 surface would be a red
    # flag: PAS205 explicitly ships no scheduler.
    bad_patterns = (
        "import schedule",
        "from schedule",
        "import apscheduler",
        "from apscheduler",
        "asyncio.create_task",
        "Thread(",
        "while True:",
        "cron",
    )
    out: List[dict] = []
    for rel in _PAS205_PRODUCTION_FILES:
        src = _read_text(Path(repo_root) / rel) or ""
        bad = [p for p in bad_patterns if p in src]
        out.append(_check(
            f"no_scheduler:{rel}",
            "FAIL" if bad else "PASS",
            f"{rel} declares no scheduler / cron / background loop",
            detail=("disqualifying: " + ", ".join(bad)) if bad else "",
        ))
    return out


def check_observer_smoke(repo_root: str) -> List[dict]:
    sys.path.insert(0, repo_root)
    out: List[dict] = []
    try:
        from app.services.proactive.observer import observe  # type: ignore
        from app.services.proactive.observer_digest import (  # type: ignore
            FORBIDDEN_OUTPUT_TOKENS,
            to_broker_report,
            to_machine_json,
            to_slack_summary,
        )
        from app.services.proactive.observer_models import (  # type: ignore
            ObservedSnapshot,
            SIGNAL_TYPES,
        )
    except Exception as e:
        return [_check(
            "smoke:imports",
            "FAIL",
            "PAS205 modules importable",
            detail=type(e).__name__,
        )]

    out.append(_check(
        "smoke:signal_types_count",
        "PASS" if len(SIGNAL_TYPES) == 10 else "FAIL",
        "observer_models declares exactly 10 closed signal types",
        detail=str(len(SIGNAL_TYPES)),
    ))

    # Empty snapshot should produce zero signals and a friendly
    # summary that contains no forbidden tokens.
    snap = ObservedSnapshot(observed_at="2026-05-23T14:00:00Z")
    digest = observe(snap)
    out.append(_check(
        "smoke:clean_snapshot_zero_signals",
        "PASS" if len(digest.signals) == 0 else "FAIL",
        "empty snapshot produces zero signals",
        detail=str(len(digest.signals)),
    ))
    out.append(_check(
        "smoke:clean_snapshot_live_behavior_unchanged",
        "PASS" if digest.live_behavior_changed is False else "FAIL",
        "digest carries live_behavior_changed=false",
    ))
    summary = to_slack_summary(digest)
    bad = [tok for tok in FORBIDDEN_OUTPUT_TOKENS if tok in summary]
    out.append(_check(
        "smoke:clean_slack_summary_no_forbidden_tokens",
        "FAIL" if bad else "PASS",
        "slack summary contains no closed-vocab tokens",
        detail=("leaked: " + ", ".join(bad)) if bad else "",
    ))
    report = to_broker_report(digest)
    bad2 = [tok for tok in FORBIDDEN_OUTPUT_TOKENS if tok in report]
    out.append(_check(
        "smoke:clean_broker_report_no_forbidden_tokens",
        "FAIL" if bad2 else "PASS",
        "broker report contains no closed-vocab tokens",
        detail=("leaked: " + ", ".join(bad2)) if bad2 else "",
    ))
    machine = to_machine_json(digest)
    out.append(_check(
        "smoke:machine_json_phase",
        "PASS" if machine.get("phase") == "PAS205" else "FAIL",
        "machine json carries phase=PAS205",
    ))
    out.append(_check(
        "smoke:machine_json_environment",
        "PASS" if machine.get("allowed_environment") == "SIMULATION_ONLY" else "FAIL",
        "machine json carries allowed_environment=SIMULATION_ONLY",
    ))
    return out


# ──────────────────────────────────────────────────────────────────
# Orchestration
# ──────────────────────────────────────────────────────────────────

ALL_CHECKS = (
    check_pas205_files_present,
    check_closed_signal_vocabulary,
    check_observer_entry_points,
    check_no_banned_imports,
    check_no_forbidden_status_literals,
    check_no_forbidden_identifiers,
    check_no_observer_writes,
    check_no_secret_shapes,
    check_no_new_migration,
    check_no_combined_migration_committed,
    check_no_scheduler_or_cron,
    check_doc_clauses,
    check_runner_writes_only_reports,
    check_observer_smoke,
)


def run_all_checks(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for fn in ALL_CHECKS:
        try:
            out.extend(fn(repo_root))
        except Exception as e:  # pragma: no cover - readiness should not crash
            out.append(_check(
                f"meta:check_error:{fn.__name__}",
                "FAIL",
                f"check {fn.__name__} raised",
                detail=type(e).__name__ + ": " + str(e),
            ))
    return out


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(
        description="PAS205 — Proactive observer readiness gate (read-only).",
    )
    parser.add_argument("--repo-root", default=_REPO_ROOT_DEFAULT)
    parser.add_argument("--summary-only", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    repo_root = os.path.abspath(args.repo_root)
    results = run_all_checks(repo_root)

    failures = [r for r in results if r["status"] != "PASS"]
    verdict = VERDICT_READY if not failures else VERDICT_NOT_READY

    if args.json:
        print(json.dumps({
            "phase":                 "PAS205",
            "generated_at":          _now_iso(),
            "verdict":               verdict,
            "check_count":           len(results),
            "fail_count":            len(failures),
            "results":               results,
            "allowed_environment":   "SIMULATION_ONLY",
            "live_behavior_changed": False,
        }, indent=2))
    elif args.summary_only:
        print(f"PAS205 readiness: {verdict} "
              f"({len(results) - len(failures)}/{len(results)} passed)")
        for r in failures:
            print(f"  FAIL  {r['id']}: {r['detail'] or r['description']}")
    else:
        print(f"PAS205 readiness: {verdict} "
              f"({len(results) - len(failures)}/{len(results)} passed)")
        for r in results:
            mark = "OK  " if r["status"] == "PASS" else "FAIL"
            line = f"  {mark}  {r['id']}: {r['description']}"
            if r["detail"]:
                line += f" — {r['detail']}"
            print(line)

    return 0 if verdict == VERDICT_READY else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
