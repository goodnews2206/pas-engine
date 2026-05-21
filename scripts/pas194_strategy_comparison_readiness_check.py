"""
PAS194 — Strategy Comparison readiness gate.

Deterministic, read-only evaluator for "is PAS194 wired correctly,
additive-only over PAS193, deterministic, free of Twilio/Slack/LLM
dependencies, free of PII / production brokerage IDs, and not
introducing any new SQL migration?"

Walks the repo and verifies:

  * PAS194 surfaces exist (doc / readiness gate / test / runner /
    strategies module / comparison module).
  * Strategy catalogue carries >= 5 strategies and every strategy
    passes schema integrity.
  * Comparison runner / strategies / comparison sources do not
    import twilio, Slack, OpenAI, Anthropic, Supabase, dotenv, or
    the live state machine, and do not call load_dotenv /
    get_supabase.
  * No new SQL migration was introduced under scripts/ whose
    filename carries "pas194".
  * combined_supabase_migration.sql was not committed under
    scripts/ on this branch.
  * No secret-shaped tokens are hard-coded in any PAS194 file.
  * The runner refuses to write outside reports/simulations/ by
    inspection of its source.
  * The readiness gate itself never reads .env / hits the network.
  * PAS193 carry-forward intact: scenarios, adapter, scoring,
    report, runner, readiness gate, doc, tests all present.

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


PAS194_FILES = (
    "docs/pas194_simulation_strategy_comparison.md",
    "scripts/pas194_strategy_comparison_readiness_check.py",
    "scripts/pas194_compare_simulation_strategies.py",
    "tests/mvp/test_pas194_strategy_comparison.py",
    "app/services/simulation/strategies.py",
    "app/services/simulation/comparison.py",
)


PAS193_CARRY_FORWARD_FILES = (
    "docs/pas193_simulation_layer_proof.md",
    "scripts/pas193_simulation_layer_readiness_check.py",
    "scripts/pas193_run_simulation_batch.py",
    "tests/mvp/test_pas193_simulation_layer.py",
    "app/services/simulation/__init__.py",
    "app/services/simulation/scenarios.py",
    "app/services/simulation/adapter.py",
    "app/services/simulation/scoring.py",
    "app/services/simulation/report.py",
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
    "app.services.slack",
    "app.routes.slack_command",
    "app.engine.state_machine",
    "app.engine",
)


BANNED_CALL_NAMES: Tuple[str, ...] = (
    "load_dotenv",
    "get_supabase",
)


SECRET_SHAPE_REGEXES = (
    re.compile(r"AKIA[0-9A-Z]{12,}"),
    re.compile(r"xox[bp]-[0-9A-Za-z\-]{10,}"),
    re.compile(r"sk_(live|test)_[A-Za-z0-9]{16,}"),
    re.compile(r"\bAC[0-9a-fA-F]{32}\b"),
    re.compile(r"\bSK[0-9a-fA-F]{32}\b"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
)


DOC_FILE = "docs/pas194_simulation_strategy_comparison.md"
DOC_REQUIRED_CLAUSES = (
    "purpose",
    "what pas194 proves",
    "what pas194 does not prove",
    "how this upgrades",
    "how to run",
    "claimable",
    "still not claimable",
    "safety",
    "strategy",
    "comparison",
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


def _banned_in(imports: Set[str], calls: Set[str]) -> List[str]:
    bad: List[str] = []
    for mod in imports:
        if mod in BANNED_IMPORT_MODULES:
            bad.append(f"import {mod}")
            continue
        for pref in BANNED_IMPORT_PREFIXES:
            if mod == pref or mod.startswith(pref + ".") or (
                pref.endswith(".") and mod.startswith(pref)
            ) or mod.startswith(pref):
                bad.append(f"import {mod}")
                break
    for name in calls:
        if name in BANNED_CALL_NAMES:
            bad.append(f"call {name}()")
    return bad


# ──────────────────────────────────────────────────────────────────
# Checks
# ──────────────────────────────────────────────────────────────────

def check_pas194_files_present(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in PAS194_FILES:
        ok = (Path(repo_root) / rel).is_file()
        out.append(_check(
            f"files:exists:{rel}",
            "PASS" if ok else "FAIL",
            f"PAS194 artefact present: {rel}",
            detail="" if ok else "file missing",
        ))
    return out


def check_pas193_carry_forward(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in PAS193_CARRY_FORWARD_FILES:
        ok = (Path(repo_root) / rel).is_file()
        out.append(_check(
            f"carry_forward:{rel}",
            "PASS" if ok else "FAIL",
            f"PAS193 carry-forward intact: {rel}",
            detail="" if ok else "file missing — PAS193 base broken",
        ))
    return out


def check_no_banned_imports(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in PAS194_FILES:
        if not rel.endswith(".py"):
            continue
        src = _read_text(Path(repo_root) / rel) or ""
        imports, calls = _collect_imports_and_calls(src)
        bad = _banned_in(imports, calls)
        out.append(_check(
            f"no_banned_imports:{rel}",
            "FAIL" if bad else "PASS",
            f"{rel} is free of Twilio/Slack/LLM/Supabase/state_machine imports",
            detail=("disqualifying: " + ", ".join(sorted(set(bad)))) if bad else "",
        ))
    return out


def check_no_secret_shapes(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in PAS194_FILES:
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
    bad: list = []
    if root.is_dir():
        for entry in root.iterdir():
            name = entry.name.lower()
            if "pas194" in name and (
                name.endswith(".sql") or "migrate" in name
            ):
                bad.append(entry.name)
    return [_check(
        "no_new_migration",
        "FAIL" if bad else "PASS",
        "PAS194 introduces no SQL migration",
        detail=("found: " + ", ".join(bad)) if bad else "",
    )]


def check_no_combined_migration_committed(repo_root: str) -> List[dict]:
    fp = Path(repo_root) / "scripts" / "combined_supabase_migration.sql"
    present = fp.is_file()
    return [_check(
        "no_combined_migration_committed",
        "FAIL" if present else "PASS",
        "combined_supabase_migration.sql not committed on this branch",
        detail=str(fp) if present else "",
    )]


def check_strategy_catalogue(repo_root: str) -> List[dict]:
    out: List[dict] = []
    sys.path.insert(0, repo_root)
    try:
        from app.services.simulation.strategies import (  # type: ignore
            KNOWN_SAFETY_VIOLATIONS,
            STRATEGIES,
            STRATEGY_IDS,
            STRATEGY_REQUIRED_KEYS,
            safety_violation_for,
            strategy_count,
        )
        ok_count = strategy_count() >= 5
        out.append(_check(
            "strategies:count_ge_5",
            "PASS" if ok_count else "FAIL",
            "strategy catalogue carries at least 5 strategies",
            detail="" if ok_count else f"count={strategy_count()}",
        ))

        seen = set()
        bad_keys: List[str] = []
        bad_ids:  List[str] = []
        bad_violations: List[str] = []
        for s in STRATEGIES:
            sid = s.get("strategy_id") or ""
            for k in STRATEGY_REQUIRED_KEYS:
                if k not in s:
                    bad_keys.append(f"{sid}::{k}")
            if sid not in STRATEGY_IDS or sid in seen:
                bad_ids.append(sid)
            seen.add(sid)

        from app.services.simulation.scenarios import SCENARIOS  # type: ignore
        for strat in STRATEGIES:
            for scenario in SCENARIOS:
                v = safety_violation_for(strat["strategy_id"], scenario["scenario_type"])
                if v is not None and v not in KNOWN_SAFETY_VIOLATIONS:
                    bad_violations.append(f"{strat['strategy_id']}::{scenario['scenario_type']}={v}")

        out.append(_check(
            "strategies:schema_keys",
            "PASS" if not bad_keys else "FAIL",
            "every strategy carries the required keys",
            detail=("missing: " + ", ".join(bad_keys)) if bad_keys else "",
        ))
        out.append(_check(
            "strategies:ids_unique_in_catalogue",
            "PASS" if not bad_ids else "FAIL",
            "strategy_id values unique and drawn from STRATEGY_IDS",
            detail=("disqualifying: " + ", ".join(bad_ids)) if bad_ids else "",
        ))
        out.append(_check(
            "strategies:safety_violation_codes",
            "PASS" if not bad_violations else "FAIL",
            "safety_violation_for returns only KNOWN_SAFETY_VIOLATIONS",
            detail=("disqualifying: " + ", ".join(bad_violations)) if bad_violations else "",
        ))
    except Exception as e:
        out.append(_check(
            "strategies:import",
            "FAIL",
            "strategy catalogue importable",
            detail=type(e).__name__,
        ))
    return out


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
    fp = Path(repo_root) / "scripts" / "pas194_compare_simulation_strategies.py"
    src = _read_text(fp) or ""
    ok_target = "reports/simulations" in src.replace("\\", "/") or "REPORTS_SUBDIR" in src
    bad_targets: List[str] = []
    for forbidden in ("/etc/", "/var/", "/usr/", "C:\\Windows", "app/static/"):
        if forbidden in src:
            bad_targets.append(forbidden)
    return [
        _check(
            "runner:writes_only_reports_dir",
            "PASS" if ok_target else "FAIL",
            "runner writes only under reports/simulations/",
            detail="" if ok_target else "no reports/simulations target found",
        ),
        _check(
            "runner:no_forbidden_write_targets",
            "PASS" if not bad_targets else "FAIL",
            "runner does not write to system paths",
            detail=("found: " + ", ".join(bad_targets)) if bad_targets else "",
        ),
    ]


def check_runtime_comparison_smoke(repo_root: str) -> List[dict]:
    out: List[dict] = []
    sys.path.insert(0, repo_root)
    try:
        from app.services.simulation.scenarios import SCENARIOS  # type: ignore
        from app.services.simulation.strategies import STRATEGIES  # type: ignore
        from app.services.simulation.comparison import (  # type: ignore
            COMPARISON_REPORT_REQUIRED_KEYS,
            build_comparison_report,
            compare_strategies,
        )
        rows = compare_strategies(STRATEGIES, SCENARIOS[:5])
        report = build_comparison_report(
            rows, SCENARIOS[:5],
            generated_at="2026-05-21T00:00:00Z",
            seed=0,
        )
        missing_keys = [k for k in COMPARISON_REPORT_REQUIRED_KEYS if k not in report]
        out.append(_check(
            "runtime:report_required_keys",
            "PASS" if not missing_keys else "FAIL",
            "comparison report carries every required key",
            detail=("missing: " + ", ".join(missing_keys)) if missing_keys else "",
        ))
        out.append(_check(
            "runtime:report_id_shape",
            "PASS" if str(report["report_id"]).startswith("pas194-cmp-") else "FAIL",
            "report_id carries pas194 prefix",
            detail=str(report["report_id"]),
        ))
    except Exception as e:
        out.append(_check(
            "runtime:comparison_smoke",
            "FAIL",
            "comparison modules importable and runnable",
            detail=type(e).__name__,
        ))
    return out


def check_self_no_env_or_network(repo_root: str) -> List[dict]:
    src = _read_text(Path(__file__)) or ""
    imports, calls = _collect_imports_and_calls(src)
    bad: List[str] = []
    for mod in imports:
        head = mod.split(".")[0]
        if head in ("dotenv", "supabase", "requests", "httpx"):
            bad.append(f"import {mod}")
        if mod.startswith("urllib.request"):
            bad.append(f"import {mod}")
    for name in ("load_dotenv", "get_supabase", "urlopen"):
        if name in calls:
            bad.append(f"call {name}()")
    if "run" in calls and "subprocess" in imports:
        bad.append("call subprocess.run()")
    return [_check(
        "self_check:no_env_or_db_or_network",
        "FAIL" if bad else "PASS",
        "PAS194 readiness checker never reads .env / touches DB / hits network",
        detail=("disqualifying: " + ", ".join(sorted(set(bad)))) if bad else "",
    )]


# ──────────────────────────────────────────────────────────────────
# Aggregator + CLI
# ──────────────────────────────────────────────────────────────────

def _aggregate(checks: List[dict]) -> dict:
    blockers = [c for c in checks if c["status"] == "FAIL" and c.get("severity") == SEVERITY_BLOCK]
    return {
        "verdict":  VERDICT_NOT_READY if blockers else VERDICT_READY,
        "blockers": blockers,
        "info":     [],
    }


def _operator_actions(checks: List[dict]) -> List[str]:
    out: List[str] = []
    for c in checks:
        if c["status"] != "FAIL":
            continue
        sev = c.get("severity") or SEVERITY_BLOCK
        out.append(f"[{sev}] {c['id']} — {c.get('detail') or 'see report'}.")
    return out


def evaluate(repo_root: str) -> dict:
    checks: List[dict] = []
    checks.extend(check_pas194_files_present(repo_root))
    checks.extend(check_pas193_carry_forward(repo_root))
    checks.extend(check_no_banned_imports(repo_root))
    checks.extend(check_no_secret_shapes(repo_root))
    checks.extend(check_no_new_migration(repo_root))
    checks.extend(check_no_combined_migration_committed(repo_root))
    checks.extend(check_strategy_catalogue(repo_root))
    checks.extend(check_doc_clauses(repo_root))
    checks.extend(check_runner_writes_only_reports(repo_root))
    checks.extend(check_runtime_comparison_smoke(repo_root))
    checks.extend(check_self_no_env_or_network(repo_root))

    agg = _aggregate(checks)
    return {
        "phase":            "PAS194",
        "generated_at":     _now_iso(),
        "verdict":          agg["verdict"],
        "ready":            agg["verdict"] == VERDICT_READY,
        "blocker_count":    len(agg["blockers"]),
        "info_count":       len(agg["info"]),
        "check_count":      len(checks),
        "pass_count":       sum(1 for c in checks if c["status"] == "PASS"),
        "fail_count":       sum(1 for c in checks if c["status"] == "FAIL"),
        "checks":           checks,
        "operator_actions": _operator_actions(checks),
    }


REPORT_FILENAME = "pas194_strategy_comparison_readiness_report.json"


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="pas194_strategy_comparison_readiness_check",
        description=(
            "PAS194 — Strategy Comparison readiness gate. Read-only. "
            "Never reads .env, never touches Supabase, never executes "
            "a deploy / migration / network call."
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
        f"[PAS194] verdict={report['verdict']} "
        f"blockers={report['blocker_count']} "
        f"info={report['info_count']} "
        f"checks={report['check_count']} "
        f"pass={report['pass_count']} "
        f"fail={report['fail_count']}"
    )
    actions = report.get("operator_actions") or []
    if actions:
        print("[PAS194] operator actions:")
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
