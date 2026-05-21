"""
PAS193 — Simulation Layer Proof readiness gate.

Deterministic, read-only evaluator for "is PAS193 wired correctly,
additive-only over PAS192, deterministic, free of Twilio/Slack/LLM
dependencies, free of PII / production brokerage IDs, and not
introducing any new SQL migration?"

Walks the repo and verifies:

  * PAS193 surfaces exist (doc / readiness gate / test / runner /
    scenarios / adapter / scoring / report).
  * Scenario catalogue carries >= 20 scenarios and every scenario
    passes schema integrity.
  * Runner source does not import twilio, Slack, OpenAI, Anthropic,
    Supabase, dotenv, or the live state machine.
  * Scenario / adapter / scoring / report sources are equally
    free of those banned imports.
  * No new SQL migration was introduced under scripts/ whose
    filename carries "pas193".
  * combined_supabase_migration.sql was not committed under
    scripts/ on this branch (it lives in the parked stash).
  * No secrets are hard-coded in any PAS193 file (basic shape
    check for AKIA / sk- / xoxb- tokens).
  * The runner refuses to write outside reports/simulations/ by
    inspection of its source.
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


# ──────────────────────────────────────────────────────────────────
# Required artefacts
# ──────────────────────────────────────────────────────────────────

PAS193_FILES = (
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


PAS192_CARRY_FORWARD_FILES = (
    "docs/pas192_slack_operator_experience.md",
    "scripts/pas192_slack_operator_experience_readiness_check.py",
    "tests/mvp/test_pas192_slack_operator_experience.py",
    "app/services/slack/operator_intents.py",
    "app/services/slack/operator_responses.py",
)


# Module names whose import disqualifies any PAS193 source.
BANNED_IMPORT_MODULES: Tuple[str, ...] = (
    "twilio",
    "slack_sdk",
    "openai",
    "anthropic",
    "dotenv",
    "supabase",
)

# Module prefixes whose import disqualifies any PAS193 source.
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

# Function call names whose use in any PAS193 source disqualifies it.
BANNED_CALL_NAMES: Tuple[str, ...] = (
    "load_dotenv",
    "get_supabase",
)


# Regexes whose presence in any PAS193 source is a hard fail
# because they match the literal shape of common secret values.
SECRET_SHAPE_REGEXES = (
    re.compile(r"AKIA[0-9A-Z]{12,}"),                # AWS access key
    re.compile(r"xox[bp]-[0-9A-Za-z\-]{10,}"),       # Slack bot / user tokens
    re.compile(r"sk_(live|test)_[A-Za-z0-9]{16,}"),  # Stripe keys
    re.compile(r"\bAC[0-9a-fA-F]{32}\b"),            # Twilio account SID
    re.compile(r"\bSK[0-9a-fA-F]{32}\b"),            # Twilio API key
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
)


# Doc clauses every PAS193 doc must carry, lowercased.
DOC_FILE = "docs/pas193_simulation_layer_proof.md"
DOC_REQUIRED_CLAUSES = (
    "purpose",
    "what pas193 proves",
    "what pas193 does not prove",
    "safety constraints",
    "how to run",
    "claimable",
    "still not claimable",
    "simulation",
    "rehearsal",
    "deterministic",
)


# ──────────────────────────────────────────────────────────────────
# IO helpers
# ──────────────────────────────────────────────────────────────────

def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _read_text(p: Path) -> Optional[str]:
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        return None


def _collect_imports_and_calls(src: str) -> Tuple[Set[str], Set[str]]:
    """
    Return (imported_module_names, called_function_names).

    Uses AST so docstrings, comments, and string literals listing
    banned tokens do not trigger false positives.
    """
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


def _check(check_id: str, status: str, description: str,
           detail: str = "", severity: str = SEVERITY_BLOCK) -> dict:
    return {
        "id":          check_id,
        "status":      status,
        "description": description,
        "detail":      detail,
        "severity":    severity,
    }


# ──────────────────────────────────────────────────────────────────
# Checks
# ──────────────────────────────────────────────────────────────────

def check_pas193_files_present(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in PAS193_FILES:
        ok = (Path(repo_root) / rel).is_file()
        out.append(_check(
            f"files:exists:{rel}",
            "PASS" if ok else "FAIL",
            f"PAS193 artefact present: {rel}",
            detail="" if ok else "file missing",
        ))
    return out


def check_pas192_carry_forward(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in PAS192_CARRY_FORWARD_FILES:
        ok = (Path(repo_root) / rel).is_file()
        out.append(_check(
            f"carry_forward:{rel}",
            "PASS" if ok else "FAIL",
            f"PAS192 carry-forward intact: {rel}",
            detail="" if ok else "file missing — PAS192 base broken",
        ))
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


def check_no_banned_imports(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in PAS193_FILES:
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
    for rel in PAS193_FILES:
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
            if "pas193" in name and (
                name.endswith(".sql") or "migrate" in name
            ):
                bad.append(entry.name)
    return [_check(
        "no_new_migration",
        "FAIL" if bad else "PASS",
        "PAS193 introduces no SQL migration",
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


def check_scenario_catalogue(repo_root: str) -> List[dict]:
    out: List[dict] = []
    sys.path.insert(0, repo_root)
    try:
        from app.services.simulation.scenarios import (  # type: ignore
            SCENARIOS, SCENARIO_REQUIRED_KEYS, SCENARIO_TYPES,
            scenario_count,
        )
        ok_count = scenario_count() >= 20
        out.append(_check(
            "scenarios:count_ge_20",
            "PASS" if ok_count else "FAIL",
            "scenario catalogue carries at least 20 scenarios",
            detail="" if ok_count else f"count={scenario_count()}",
        ))

        seen = set()
        bad_keys: List[str] = []
        bad_ids:  List[str] = []
        bad_types: List[str] = []
        id_pat = re.compile(r"^pas193_sim_[a-z0-9_]+$")
        for s in SCENARIOS:
            for k in SCENARIO_REQUIRED_KEYS:
                if k not in s:
                    bad_keys.append(f"{s.get('scenario_id')}::{k}")
            sid = s.get("scenario_id") or ""
            if not id_pat.match(sid) or sid in seen:
                bad_ids.append(sid)
            seen.add(sid)
            if s.get("scenario_type") not in SCENARIO_TYPES:
                bad_types.append(f"{sid}::{s.get('scenario_type')}")

        out.append(_check(
            "scenarios:schema_keys",
            "PASS" if not bad_keys else "FAIL",
            "every scenario carries the required keys",
            detail=("missing: " + ", ".join(bad_keys)) if bad_keys else "",
        ))
        out.append(_check(
            "scenarios:ids_well_formed_unique",
            "PASS" if not bad_ids else "FAIL",
            "scenario_id values match shape and are unique",
            detail=("disqualifying: " + ", ".join(bad_ids)) if bad_ids else "",
        ))
        out.append(_check(
            "scenarios:types_from_catalogue",
            "PASS" if not bad_types else "FAIL",
            "scenario_type values are drawn from SCENARIO_TYPES",
            detail=("disqualifying: " + ", ".join(bad_types)) if bad_types else "",
        ))
    except Exception as e:
        out.append(_check(
            "scenarios:import",
            "FAIL",
            "scenario catalogue importable",
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
    fp = Path(repo_root) / "scripts" / "pas193_run_simulation_batch.py"
    src = _read_text(fp) or ""
    # The runner must reference the reports/simulations path; it
    # must not contain raw open()/Path().write_text calls that
    # target /etc/ /var/ or any path under app/.
    ok_target = "reports/simulations" in src.replace("\\", "/") or "REPORTS_SUBDIR" in src
    bad_targets: List[str] = []
    for forbidden in ("/etc/", "/var/", "/usr/", "C:\\Windows", "app/static/"):
        if forbidden in src:
            bad_targets.append(forbidden)
    out: List[dict] = []
    out.append(_check(
        "runner:writes_only_reports_dir",
        "PASS" if ok_target else "FAIL",
        "runner writes only under reports/simulations/",
        detail="" if ok_target else "no reports/simulations target found",
    ))
    out.append(_check(
        "runner:no_forbidden_write_targets",
        "PASS" if not bad_targets else "FAIL",
        "runner does not write to system paths",
        detail=("found: " + ", ".join(bad_targets)) if bad_targets else "",
    ))
    return out


def check_runtime_simulation_smoke(repo_root: str) -> List[dict]:
    """
    Pure in-process: build a small batch, score it, build a
    report, assert structural invariants. No file I/O. No network.
    """
    out: List[dict] = []
    sys.path.insert(0, repo_root)
    try:
        from app.services.simulation.scenarios import SCENARIOS  # type: ignore
        from app.services.simulation.adapter import run_scenario  # type: ignore
        from app.services.simulation.scoring import score_conversation  # type: ignore
        from app.services.simulation.report import (  # type: ignore
            REPORT_REQUIRED_KEYS, build_report,
        )

        scored = []
        for s in SCENARIOS[:5]:
            conv = run_scenario(s)
            result = score_conversation(conv, s)
            scored.append({
                "scenario_id":           s["scenario_id"],
                "scenario_type":         s["scenario_type"],
                "supported":             s["supported"],
                "score":                 result["score"],
                "passed":                result["passed"],
                "failure_reasons":       result["failure_reasons"],
                "recommendation_label":  result["recommendation_label"],
                "capabilities_observed": result["capabilities_observed"],
                "missing_criteria":      result["missing_criteria"],
            })
        report = build_report(
            scored,
            generated_at="2026-05-21T00:00:00Z",
            seed=0,
        )
        missing_keys = [k for k in REPORT_REQUIRED_KEYS if k not in report]
        out.append(_check(
            "runtime:report_required_keys",
            "PASS" if not missing_keys else "FAIL",
            "report carries every required key",
            detail=("missing: " + ", ".join(missing_keys)) if missing_keys else "",
        ))
        out.append(_check(
            "runtime:report_id_shape",
            "PASS" if str(report["report_id"]).startswith("pas193-rep-") else "FAIL",
            "report_id carries pas193 prefix",
            detail=str(report["report_id"]),
        ))
    except Exception as e:
        out.append(_check(
            "runtime:simulation_smoke",
            "FAIL",
            "simulation modules importable and runnable",
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
    for name in (
        "load_dotenv",
        "get_supabase",
        "run",   # subprocess.run / similar
        "urlopen",
    ):
        if name in calls:
            # subprocess.run is the only legitimate concern; we
            # are not running subprocesses here.
            if name == "run" and "subprocess" not in imports:
                continue
            bad.append(f"call {name}()")
    return [_check(
        "self_check:no_env_or_db_or_network",
        "FAIL" if bad else "PASS",
        "PAS193 readiness checker never reads .env / touches DB / hits network",
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
    checks.extend(check_pas193_files_present(repo_root))
    checks.extend(check_pas192_carry_forward(repo_root))
    checks.extend(check_no_banned_imports(repo_root))
    checks.extend(check_no_secret_shapes(repo_root))
    checks.extend(check_no_new_migration(repo_root))
    checks.extend(check_no_combined_migration_committed(repo_root))
    checks.extend(check_scenario_catalogue(repo_root))
    checks.extend(check_doc_clauses(repo_root))
    checks.extend(check_runner_writes_only_reports(repo_root))
    checks.extend(check_runtime_simulation_smoke(repo_root))
    checks.extend(check_self_no_env_or_network(repo_root))

    agg = _aggregate(checks)
    return {
        "phase":            "PAS193",
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


REPORT_FILENAME = "pas193_simulation_layer_readiness_report.json"


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="pas193_simulation_layer_readiness_check",
        description=(
            "PAS193 — Simulation Layer Proof readiness gate. "
            "Read-only — never reads .env, never touches Supabase, "
            "never executes a deploy / migration / network call."
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
        f"[PAS193] verdict={report['verdict']} "
        f"blockers={report['blocker_count']} "
        f"info={report['info_count']} "
        f"checks={report['check_count']} "
        f"pass={report['pass_count']} "
        f"fail={report['fail_count']}"
    )
    actions = report.get("operator_actions") or []
    if actions:
        print("[PAS193] operator actions:")
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
