"""
PAS201 — Simulation evidence digest readiness gate.

Deterministic, read-only evaluator for "is PAS201 wired correctly,
additive-only over PAS200, deterministic, free of
Twilio/Slack/Supabase/state-machine/LLM dependencies, free of
forbidden status literals or live-mutation identifiers,
structurally bounded to SIMULATION_ONLY, and not introducing any
new SQL migration?"

Walks the repo and verifies:

  * PAS201 surfaces exist (doc / readiness gate / CLI / service /
    test).
  * Digest service exposes the public entry points
    (build_evidence_digest, EvidenceDigestValidationError,
    EVIDENCE_STRENGTH_VALUES, CLAIMABLE_NOW_VOCAB,
    NOT_CLAIMABLE_YET_VOCAB).
  * Service + CLI source string-constants do not contain the
    forbidden status literals APPROVED / APPLIED / AUTO_APPLIED /
    LIVE / DEPLOYED.
  * Service + CLI do not carry live-mutation identifier names.
  * Service + CLI do not import twilio, Slack, OpenAI, Anthropic,
    Supabase, dotenv, or the live state machine.
  * Runtime smoke: build_evidence_digest on a synthetic clean
    six-artefact chain returns the required keys, phase=PAS201,
    allowed_environment=SIMULATION_ONLY,
    live_behavior_changed=False, evidence_strength=strong,
    integrity all-True.
  * No new SQL migration introduced under scripts/ whose filename
    carries "pas201".
  * combined_supabase_migration.sql is not committed on this
    branch.
  * No secret-shaped tokens in any PAS201 file.
  * CLI refuses to write outside reports/simulations/.
  * The readiness gate itself never reads .env / hits the network.
  * PAS193..PAS200 carry-forward intact.

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


PAS201_FILES = (
    "docs/pas201_simulation_evidence_digest.md",
    "scripts/pas201_evidence_digest_readiness_check.py",
    "scripts/pas201_build_simulation_evidence_digest.py",
    "tests/mvp/test_pas201_evidence_digest.py",
    "app/services/simulation/evidence_digest.py",
)


PAS200_CARRY_FORWARD_FILES = (
    "docs/pas200_behavioral_evaluation.md",
    "scripts/pas200_behavioral_evaluation_readiness_check.py",
    "scripts/pas200_evaluate_runtime_behavior.py",
    "tests/mvp/test_pas200_behavioral_evaluation.py",
    "app/services/simulation/behavioral_evaluation.py",
)


PAS199_CARRY_FORWARD_FILES = (
    "docs/pas199_runtime_inspection.md",
    "scripts/pas199_runtime_inspection_readiness_check.py",
    "scripts/pas199_inspect_runtime_lineage.py",
    "tests/mvp/test_pas199_runtime_inspection.py",
    "app/services/simulation/runtime_inspection.py",
)


PAS198_CARRY_FORWARD_FILES = (
    "docs/pas198_manual_test_runtime.md",
    "scripts/pas198_manual_test_runtime_readiness_check.py",
    "scripts/pas198_run_manual_test_runtime.py",
    "tests/mvp/test_pas198_manual_test_runtime.py",
    "app/services/simulation/manual_test_runtime.py",
)


PAS197_CARRY_FORWARD_FILES = (
    "docs/pas197_manual_test_package.md",
    "scripts/pas197_manual_test_package_readiness_check.py",
    "scripts/pas197_create_manual_test_package.py",
    "tests/mvp/test_pas197_manual_test_package.py",
    "app/services/simulation/manual_test_package.py",
)


PAS196_CARRY_FORWARD_FILES = (
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
)


SECRET_SHAPE_REGEXES = (
    re.compile(r"AKIA[0-9A-Z]{12,}"),
    re.compile(r"xox[bp]-[0-9A-Za-z\-]{10,}"),
    re.compile(r"sk_(live|test)_[A-Za-z0-9]{16,}"),
    re.compile(r"\bAC[0-9a-fA-F]{32}\b"),
    re.compile(r"\bSK[0-9a-fA-F]{32}\b"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
)


DOC_FILE = "docs/pas201_simulation_evidence_digest.md"
DOC_REQUIRED_CLAUSES = (
    "purpose",
    "what pas201 proves",
    "what pas201 does not prove",
    "claimable",
    "still not claimable",
    "future pas202",
    "digest",
    "evidence",
    "operator",
    "safety",
    "simulation_only",
    "demo",
    "investor",
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

def check_pas201_files_present(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in PAS201_FILES:
        ok = (Path(repo_root) / rel).is_file()
        out.append(_check(
            f"files:exists:{rel}",
            "PASS" if ok else "FAIL",
            f"PAS201 artefact present: {rel}",
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
    for rel in PAS201_FILES:
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
        "app/services/simulation/evidence_digest.py",
        "scripts/pas201_build_simulation_evidence_digest.py",
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
        "app/services/simulation/evidence_digest.py",
        "scripts/pas201_build_simulation_evidence_digest.py",
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


def check_required_entry_points_present(repo_root: str) -> List[dict]:
    src = _read_text(
        Path(repo_root) / "app/services/simulation/evidence_digest.py",
    ) or ""
    names = _collect_identifier_names(src)
    required = (
        ("entry_point:build_evidence_digest",
         "build_evidence_digest",
         "digest entry point"),
        ("entry_point:EvidenceDigestValidationError",
         "EvidenceDigestValidationError",
         "digest validation error class"),
        ("entry_point:EVIDENCE_STRENGTH_VALUES",
         "EVIDENCE_STRENGTH_VALUES",
         "evidence strength vocabulary"),
        ("entry_point:CLAIMABLE_NOW_VOCAB",
         "CLAIMABLE_NOW_VOCAB",
         "claimable-now vocabulary"),
        ("entry_point:NOT_CLAIMABLE_YET_VOCAB",
         "NOT_CLAIMABLE_YET_VOCAB",
         "not-claimable-yet vocabulary"),
        ("entry_point:OPERATOR_HIGHLIGHTS",
         "OPERATOR_HIGHLIGHTS",
         "operator highlights vocabulary"),
        ("entry_point:DIGEST_REQUIRED_KEYS",
         "DIGEST_REQUIRED_KEYS",
         "digest required key tuple"),
        ("entry_point:ARTIFACT_INTEGRITY_KEYS",
         "ARTIFACT_INTEGRITY_KEYS",
         "artifact integrity key tuple"),
    )
    return [
        _check(
            cid,
            "PASS" if name in names else "FAIL",
            f"evidence_digest exposes {desc}",
            detail="" if name in names else f"name {name!r} missing",
        )
        for (cid, name, desc) in required
    ]


def check_required_status_constants_present(repo_root: str) -> List[dict]:
    src = _read_text(
        Path(repo_root) / "app/services/simulation/evidence_digest.py",
    ) or ""
    consts = _collect_string_constants(src)
    required = (
        ("status:phase_pas201",
         "PAS201", "PAS201 phase identifier"),
        ("status:simulation_only_present",
         "SIMULATION_ONLY", "SIMULATION_ONLY environment"),
        ("status:required_recommendation_status",
         "CANDIDATE", "required recommendation status"),
        ("status:required_review_new_status",
         "APPROVED_FOR_MANUAL_TEST", "required review new_status"),
        ("status:required_package_status",
         "READY_FOR_MANUAL_TEST", "required package status"),
        ("status:required_runtime_status",
         "EXECUTED", "required runtime status"),
        ("status:required_inspection_phase",
         "PAS199", "required inspection phase"),
        ("status:required_behavioral_phase",
         "PAS200", "required behavioural-evaluation phase"),
        ("status:evidence_strength_strong",
         "strong", "evidence strength: strong"),
        ("status:evidence_strength_moderate",
         "moderate", "evidence strength: moderate"),
        ("status:evidence_strength_weak",
         "weak", "evidence strength: weak"),
        ("status:evidence_strength_blocked",
         "blocked", "evidence strength: blocked"),
    )
    return [
        _check(
            cid,
            "PASS" if tok in consts else "FAIL",
            f"evidence_digest declares {desc}",
            detail="" if tok in consts else f"string constant {tok!r} missing",
        )
        for (cid, tok, desc) in required
    ]


def check_no_secret_shapes(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in PAS201_FILES:
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
            if "pas201" in name and (
                name.endswith(".sql") or "migrate" in name
            ):
                bad.append(entry.name)
    return [_check(
        "no_new_migration",
        "FAIL" if bad else "PASS",
        "PAS201 introduces no SQL migration",
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
    fp = Path(repo_root) / "scripts" / "pas201_build_simulation_evidence_digest.py"
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


def check_digest_smoke(repo_root: str) -> List[dict]:
    out: List[dict] = []
    sys.path.insert(0, repo_root)
    try:
        from app.services.simulation.behavioral_evaluation import (  # type: ignore
            build_behavioral_evaluation,
        )
        from app.services.simulation.manual_test_runtime import (  # type: ignore
            execute_manual_test_runtime,
        )
        from app.services.simulation.runtime_inspection import (  # type: ignore
            build_inspection,
        )
        from app.services.simulation.evidence_digest import (  # type: ignore
            DIGEST_ENVIRONMENT_SIMULATION_ONLY,
            DIGEST_REQUIRED_KEYS,
            build_evidence_digest,
        )
        rec = {
            "recommendation_id":    "pas195-rec-smoke",
            "status":               "CANDIDATE",
            "operator_required":    True,
            "recommended_strategy": "callback_first",
            "rejected_strategy":    "assertive",
            "recommendation_type":  "promote_strategy",
            "confidence_level":     "high",
            "pass_rate_threshold":  0.95,
            "phase":                "PAS195",
        }
        rev = {
            "review_id":             "pas196-rev-smoke",
            "recommendation_id":     "pas195-rec-smoke",
            "previous_status":       "CANDIDATE",
            "new_status":            "APPROVED_FOR_MANUAL_TEST",
            "live_behavior_changed": False,
            "actor_type":            "operator",
            "actor_id_token":        "op_smokesmoke",
            "reason_token":          "operator_approved_for_manual_test",
            "reviewed_at":           "2026-05-22T00:00:00Z",
            "operator_required":     True,
            "phase":                 "PAS196",
        }
        pkg = {
            "package_id":            "pas197-pkg-smoke",
            "phase":                 "PAS197",
            "recommendation_id":     "pas195-rec-smoke",
            "review_id":             "pas196-rev-smoke",
            "strategy_id":           "callback_first",
            "status":                "READY_FOR_MANUAL_TEST",
            "live_behavior_changed": False,
            "allowed_environment":   "SIMULATION_ONLY",
            "test_plan":             [],
            "success_metrics":       [],
            "rollback_notes":        [],
            "safety_notes":          [],
            "created_at":            "2026-05-22T00:00:00Z",
        }
        rt   = execute_manual_test_runtime(pkg, created_at="2026-05-22T00:00:00Z")
        insp = build_inspection(rec, rev, pkg, rt, generated_at="2026-05-22T00:00:00Z")
        beh  = build_behavioral_evaluation(
            rt, generated_at="2026-05-22T00:00:00Z", inspection=insp,
        )
        d = build_evidence_digest(
            rec, rev, pkg, rt, insp, beh,
            generated_at="2026-05-22T00:00:00Z",
        )
        missing = [k for k in DIGEST_REQUIRED_KEYS if k not in d]
        out.append(_check(
            "digest:required_keys",
            "PASS" if not missing else "FAIL",
            "digest carries every required key",
            detail=("missing: " + ", ".join(missing)) if missing else "",
        ))
        out.append(_check(
            "digest:allowed_environment_simulation_only",
            "PASS" if d["allowed_environment"] == DIGEST_ENVIRONMENT_SIMULATION_ONLY else "FAIL",
            "digest allowed_environment is SIMULATION_ONLY",
            detail="" if d["allowed_environment"] == DIGEST_ENVIRONMENT_SIMULATION_ONLY else f"got {d['allowed_environment']!r}",
        ))
        out.append(_check(
            "digest:live_behavior_changed_false",
            "PASS" if d["live_behavior_changed"] is False else "FAIL",
            "digest live_behavior_changed is False",
            detail="" if d["live_behavior_changed"] is False else "value not False",
        ))
        out.append(_check(
            "digest:digest_id_shape",
            "PASS" if str(d["digest_id"]).startswith("pas201-dgst-") else "FAIL",
            "digest_id carries pas201 prefix",
            detail=str(d["digest_id"]),
        ))
        out.append(_check(
            "digest:phase_pas201",
            "PASS" if d["phase"] == "PAS201" else "FAIL",
            "digest phase is PAS201",
            detail="" if d["phase"] == "PAS201" else f"got {d['phase']!r}",
        ))
        out.append(_check(
            "digest:strong_evidence_on_callback_first_chain",
            "PASS" if d["evidence_strength"] == "strong" else "FAIL",
            "evidence_strength is strong on synthetic clean chain",
            detail="" if d["evidence_strength"] == "strong" else f"got {d['evidence_strength']!r}",
        ))
        integ_all_true = all(d["artifact_integrity"].values())
        out.append(_check(
            "digest:artifact_integrity_all_true",
            "PASS" if integ_all_true else "FAIL",
            "artifact_integrity all-True on clean chain",
            detail="" if integ_all_true else json.dumps(
                d["artifact_integrity"], sort_keys=True,
            )[:200],
        ))
    except Exception as e:
        out.append(_check(
            "digest:smoke",
            "FAIL",
            "evidence_digest module importable and runnable",
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
        "PAS201 readiness checker never reads .env / touches DB / hits network",
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
    checks.extend(check_pas201_files_present(repo_root))
    checks.extend(_check_carry_forward(repo_root, "pas200", PAS200_CARRY_FORWARD_FILES))
    checks.extend(_check_carry_forward(repo_root, "pas199", PAS199_CARRY_FORWARD_FILES))
    checks.extend(_check_carry_forward(repo_root, "pas198", PAS198_CARRY_FORWARD_FILES))
    checks.extend(_check_carry_forward(repo_root, "pas197", PAS197_CARRY_FORWARD_FILES))
    checks.extend(_check_carry_forward(repo_root, "pas196", PAS196_CARRY_FORWARD_FILES))
    checks.extend(_check_carry_forward(repo_root, "pas195", PAS195_CARRY_FORWARD_FILES))
    checks.extend(_check_carry_forward(repo_root, "pas194", PAS194_CARRY_FORWARD_FILES))
    checks.extend(_check_carry_forward(repo_root, "pas193", PAS193_CARRY_FORWARD_FILES))
    checks.extend(check_no_banned_imports(repo_root))
    checks.extend(check_no_forbidden_status_literals(repo_root))
    checks.extend(check_no_forbidden_identifiers(repo_root))
    checks.extend(check_required_entry_points_present(repo_root))
    checks.extend(check_required_status_constants_present(repo_root))
    checks.extend(check_no_secret_shapes(repo_root))
    checks.extend(check_no_new_migration(repo_root))
    checks.extend(check_no_combined_migration_committed(repo_root))
    checks.extend(check_doc_clauses(repo_root))
    checks.extend(check_runner_writes_only_reports(repo_root))
    checks.extend(check_digest_smoke(repo_root))
    checks.extend(check_self_no_env_or_network(repo_root))

    agg = _aggregate(checks)
    return {
        "phase":            "PAS201",
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


REPORT_FILENAME = "pas201_simulation_evidence_digest_readiness_report.json"


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="pas201_evidence_digest_readiness_check",
        description=(
            "PAS201 — Simulation Evidence Digest readiness gate. "
            "Read-only. Never reads .env, never touches Supabase, "
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
        f"[PAS201] verdict={report['verdict']} "
        f"blockers={report['blocker_count']} "
        f"info={report['info_count']} "
        f"checks={report['check_count']} "
        f"pass={report['pass_count']} "
        f"fail={report['fail_count']}"
    )
    actions = report.get("operator_actions") or []
    if actions:
        print("[PAS201] operator actions:")
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
