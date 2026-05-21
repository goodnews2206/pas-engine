"""
PAS196 — Simulation Recommendation Review readiness gate.

Deterministic, read-only evaluator for "is PAS196 wired correctly,
additive-only over PAS195, deterministic, free of Twilio/Slack/LLM
dependencies, free of forbidden status literals or live-mutation
identifiers, and not introducing any new SQL migration?"

Walks the repo and verifies:

  * PAS196 surfaces exist (doc / readiness gate / CLI / service /
    test).
  * Review service + CLI do not import twilio, Slack, OpenAI,
    Anthropic, Supabase, dotenv, or the live state machine, and
    do not call load_dotenv / get_supabase.
  * Review service + CLI do not carry forbidden status literals
    APPROVED / APPLIED / AUTO_APPLIED / LIVE / DEPLOYED (the
    literal status APPROVED_FOR_MANUAL_TEST is allowed; the gate
    checks string constants for exact matches via AST).
  * Review service + CLI do not carry forbidden live-mutation
    identifier names.
  * Status machine exposes the expected allowed transitions and
    rejects all others.
  * Runtime smoke: submit_review on a synthetic CANDIDATE
    recommendation returns operator_required=True,
    live_behavior_changed=False.
  * No new SQL migration introduced under scripts/ whose filename
    carries "pas196".
  * combined_supabase_migration.sql is not committed on this
    branch.
  * No secret-shaped tokens in any PAS196 file.
  * CLI refuses to write outside reports/simulations/.
  * The readiness gate itself never reads .env / hits the network.
  * PAS193 / PAS194 / PAS195 carry-forward intact.

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


PAS196_FILES = (
    "docs/pas196_simulation_recommendation_review.md",
    "scripts/pas196_simulation_recommendation_review_readiness_check.py",
    "scripts/pas196_review_simulation_recommendation.py",
    "tests/mvp/test_pas196_simulation_recommendation_review.py",
    "app/services/simulation/recommendation_review.py",
)


PAS195_CARRY_FORWARD_FILES = (
    "docs/pas195_simulation_recommendation_layer.md",
    "scripts/pas195_simulation_recommendation_readiness_check.py",
    "scripts/pas195_generate_simulation_recommendation.py",
    "tests/mvp/test_pas195_simulation_recommendations.py",
    "app/services/simulation/recommendations.py",
)


PAS194_CARRY_FORWARD_FILES = (
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


# Status string literals that must never appear as exact string
# constants in the PAS196 surface. APPROVED_FOR_MANUAL_TEST is
# allowed because it's a distinct value; the AST check matches
# string constants exactly, so partial matches do not trip the
# gate.
FORBIDDEN_STATUS_LITERALS: Tuple[str, ...] = (
    "APPROVED",
    "APPLIED",
    "AUTO_APPLIED",
    "LIVE",
    "DEPLOYED",
)


# Identifier names that signal an autonomous-apply / live-mutation
# code path. These must not appear as function definitions,
# attribute accesses, or bare names in PAS196 source.
FORBIDDEN_IDENTIFIERS: Tuple[str, ...] = (
    "apply_recommendation",
    "deploy_strategy",
    "switch_strategy_live",
    "auto_apply",
    "auto_promote",
    "force_promote",
    "live_apply",
    "auto_deploy",
)


SECRET_SHAPE_REGEXES = (
    re.compile(r"AKIA[0-9A-Z]{12,}"),
    re.compile(r"xox[bp]-[0-9A-Za-z\-]{10,}"),
    re.compile(r"sk_(live|test)_[A-Za-z0-9]{16,}"),
    re.compile(r"\bAC[0-9a-fA-F]{32}\b"),
    re.compile(r"\bSK[0-9a-fA-F]{32}\b"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
)


DOC_FILE = "docs/pas196_simulation_recommendation_review.md"
DOC_REQUIRED_CLAUSES = (
    "purpose",
    "what pas196 proves",
    "what pas196 does not prove",
    "claimable",
    "still not claimable",
    "future pas197",
    "review",
    "operator",
    "safety",
    "transition",
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

def check_pas196_files_present(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in PAS196_FILES:
        ok = (Path(repo_root) / rel).is_file()
        out.append(_check(
            f"files:exists:{rel}",
            "PASS" if ok else "FAIL",
            f"PAS196 artefact present: {rel}",
            detail="" if ok else "file missing",
        ))
    return out


def _check_carry_forward(repo_root: str, label: str,
                        files: Tuple[str, ...]) -> List[dict]:
    out: List[dict] = []
    for rel in files:
        ok = (Path(repo_root) / rel).is_file()
        out.append(_check(
            f"carry_forward:{label}:{rel}",
            "PASS" if ok else "FAIL",
            f"{label.upper()} carry-forward intact: {rel}",
            detail="" if ok else f"file missing — {label} base broken",
        ))
    return out


def check_no_banned_imports(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in PAS196_FILES:
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


def check_no_forbidden_status_literals(repo_root: str) -> List[dict]:
    out: List[dict] = []
    targets = (
        "app/services/simulation/recommendation_review.py",
        "scripts/pas196_review_simulation_recommendation.py",
    )
    for rel in targets:
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
    targets = (
        "app/services/simulation/recommendation_review.py",
        "scripts/pas196_review_simulation_recommendation.py",
    )
    for rel in targets:
        src = _read_text(Path(repo_root) / rel) or ""
        names = _collect_identifier_names(src)
        bad = sorted(n for n in FORBIDDEN_IDENTIFIERS if n in names)
        out.append(_check(
            f"no_forbidden_identifiers:{rel}",
            "FAIL" if bad else "PASS",
            f"{rel} carries no live-mutation identifiers",
            detail=("disqualifying: " + ", ".join(bad)) if bad else "",
        ))
    return out


def check_no_secret_shapes(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in PAS196_FILES:
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
            if "pas196" in name and (
                name.endswith(".sql") or "migrate" in name
            ):
                bad.append(entry.name)
    return [_check(
        "no_new_migration",
        "FAIL" if bad else "PASS",
        "PAS196 introduces no SQL migration",
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


def check_status_machine_shape(repo_root: str) -> List[dict]:
    out: List[dict] = []
    sys.path.insert(0, repo_root)
    try:
        from app.services.simulation.recommendation_review import (  # type: ignore
            ALLOWED_STATUSES,
            ALLOWED_TRANSITIONS,
            REVIEW_ACTIONS,
            STATUS_APPROVED_FOR_MANUAL_TEST,
            STATUS_CANDIDATE,
            STATUS_EXPIRED,
            STATUS_REJECTED,
            is_allowed_transition,
        )
        expected_statuses = {
            STATUS_CANDIDATE,
            STATUS_APPROVED_FOR_MANUAL_TEST,
            STATUS_REJECTED,
            STATUS_EXPIRED,
        }
        ok_statuses = set(ALLOWED_STATUSES) == expected_statuses
        out.append(_check(
            "status_machine:allowed_statuses",
            "PASS" if ok_statuses else "FAIL",
            "ALLOWED_STATUSES exactly the four documented values",
            detail="" if ok_statuses else f"got {ALLOWED_STATUSES}",
        ))

        expected_pairs = {
            (STATUS_CANDIDATE,                STATUS_APPROVED_FOR_MANUAL_TEST),
            (STATUS_CANDIDATE,                STATUS_REJECTED),
            (STATUS_CANDIDATE,                STATUS_EXPIRED),
            (STATUS_APPROVED_FOR_MANUAL_TEST, STATUS_EXPIRED),
        }
        ok_pairs = set(ALLOWED_TRANSITIONS) == expected_pairs
        out.append(_check(
            "status_machine:allowed_transitions",
            "PASS" if ok_pairs else "FAIL",
            "ALLOWED_TRANSITIONS exactly the four documented pairs",
            detail="" if ok_pairs else f"got {set(ALLOWED_TRANSITIONS)}",
        ))

        # Spot-check negative cases.
        bad_pairs = (
            (STATUS_REJECTED, STATUS_APPROVED_FOR_MANUAL_TEST),
            (STATUS_EXPIRED, STATUS_CANDIDATE),
            (STATUS_APPROVED_FOR_MANUAL_TEST, STATUS_CANDIDATE),
            (STATUS_CANDIDATE, STATUS_CANDIDATE),
        )
        spot_ok = all(not is_allowed_transition(*p) for p in bad_pairs)
        out.append(_check(
            "status_machine:negative_spotchecks",
            "PASS" if spot_ok else "FAIL",
            "negative transition spot-checks all return False",
            detail="" if spot_ok else "some forbidden transition was allowed",
        ))

        actions_ok = set(REVIEW_ACTIONS.keys()) == {
            "approve-manual-test", "reject", "expire",
        }
        out.append(_check(
            "status_machine:review_actions",
            "PASS" if actions_ok else "FAIL",
            "REVIEW_ACTIONS exactly the three CLI actions",
            detail="" if actions_ok else f"got {set(REVIEW_ACTIONS.keys())}",
        ))
    except Exception as e:
        out.append(_check(
            "status_machine:import",
            "FAIL",
            "recommendation_review module importable",
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
    fp = Path(repo_root) / "scripts" / "pas196_review_simulation_recommendation.py"
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


def check_runtime_review_smoke(repo_root: str) -> List[dict]:
    out: List[dict] = []
    sys.path.insert(0, repo_root)
    try:
        from app.services.simulation.recommendation_review import (  # type: ignore
            REVIEW_ENVELOPE_REQUIRED_KEYS,
            STATUS_CANDIDATE,
            submit_review,
        )
        rec = {
            "recommendation_id": "pas195-rec-smoke",
            "status": STATUS_CANDIDATE,
        }
        env = submit_review(
            rec,
            "reject",
            actor_id_token="op_smoke0001",
            reason_token="operator_rejected_unsafe",
            reviewed_at="2026-05-21T00:00:00Z",
        )
        missing = [k for k in REVIEW_ENVELOPE_REQUIRED_KEYS if k not in env]
        out.append(_check(
            "runtime:envelope_required_keys",
            "PASS" if not missing else "FAIL",
            "envelope carries every required key",
            detail=("missing: " + ", ".join(missing)) if missing else "",
        ))
        out.append(_check(
            "runtime:operator_required_true",
            "PASS" if env["operator_required"] is True else "FAIL",
            "envelope operator_required is True",
            detail="" if env["operator_required"] is True else "operator_required not True",
        ))
        out.append(_check(
            "runtime:live_behavior_changed_false",
            "PASS" if env["live_behavior_changed"] is False else "FAIL",
            "envelope live_behavior_changed is False",
            detail="" if env["live_behavior_changed"] is False else "live_behavior_changed not False",
        ))
        out.append(_check(
            "runtime:review_id_shape",
            "PASS" if str(env["review_id"]).startswith("pas196-rev-") else "FAIL",
            "review_id carries pas196 prefix",
            detail=str(env["review_id"]),
        ))
    except Exception as e:
        out.append(_check(
            "runtime:review_smoke",
            "FAIL",
            "recommendation_review module importable and runnable",
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
        "PAS196 readiness checker never reads .env / touches DB / hits network",
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
    checks.extend(check_pas196_files_present(repo_root))
    checks.extend(_check_carry_forward(repo_root, "pas195", PAS195_CARRY_FORWARD_FILES))
    checks.extend(_check_carry_forward(repo_root, "pas194", PAS194_CARRY_FORWARD_FILES))
    checks.extend(_check_carry_forward(repo_root, "pas193", PAS193_CARRY_FORWARD_FILES))
    checks.extend(check_no_banned_imports(repo_root))
    checks.extend(check_no_forbidden_status_literals(repo_root))
    checks.extend(check_no_forbidden_identifiers(repo_root))
    checks.extend(check_no_secret_shapes(repo_root))
    checks.extend(check_no_new_migration(repo_root))
    checks.extend(check_no_combined_migration_committed(repo_root))
    checks.extend(check_status_machine_shape(repo_root))
    checks.extend(check_doc_clauses(repo_root))
    checks.extend(check_runner_writes_only_reports(repo_root))
    checks.extend(check_runtime_review_smoke(repo_root))
    checks.extend(check_self_no_env_or_network(repo_root))

    agg = _aggregate(checks)
    return {
        "phase":            "PAS196",
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


REPORT_FILENAME = "pas196_simulation_recommendation_review_readiness_report.json"


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="pas196_simulation_recommendation_review_readiness_check",
        description=(
            "PAS196 — Simulation Recommendation Review readiness "
            "gate. Read-only. Never reads .env, never touches "
            "Supabase, never executes a deploy / migration / "
            "network call."
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
        f"[PAS196] verdict={report['verdict']} "
        f"blockers={report['blocker_count']} "
        f"info={report['info_count']} "
        f"checks={report['check_count']} "
        f"pass={report['pass_count']} "
        f"fail={report['fail_count']}"
    )
    actions = report.get("operator_actions") or []
    if actions:
        print("[PAS196] operator actions:")
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
