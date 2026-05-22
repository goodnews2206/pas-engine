"""
PAS203 — Slack read-only evidence digest command readiness gate.

Deterministic, read-only evaluator for "is PAS203 wired
correctly, additive-only over PAS191/PAS192/PAS202, free of
Twilio/Slack/Supabase/state-machine dependencies, free of
forbidden status literals or live-mutation/messaging identifiers,
strictly read-only over reports/simulations/, and not modifying
PAS191's INTENT_CODES tuple?"

Walks the repo and verifies:

  * PAS203 surfaces exist (doc / readiness gate / service / test).
  * Service exposes the public entry points
    (INTENT_SIMULATION_DIGEST, SIMULATION_DIGEST_ALIASES,
    SIMULATION_DIGEST_HELP_LINES, MISSING_DIGEST_FALLBACK_MESSAGE,
    match_simulation_digest_intent, find_latest_digest_path,
    load_digest, format_simulation_digest_response,
    try_route_simulation_digest, FORBIDDEN_OUTPUT_TOKENS).
  * Service source string-constants do not contain the forbidden
    status literals APPROVED / APPLIED / AUTO_APPLIED / LIVE /
    DEPLOYED.
  * Service does not carry live-mutation or outbound-messaging
    identifier names.
  * Service does not import twilio, slack_sdk, openai, anthropic,
    supabase, dotenv, the live state machine, or the outbound
    Slack-notification client (the path is read-only by
    construction).
  * Service does not modify PAS191 by importing
    operator_intents or operator_responses.
  * Runtime smoke: build a synthetic digest, format it through
    the PAS203 surface, and confirm output carries SIMULATION_ONLY
    + evidence_strength tokens and no forbidden live-routing
    tokens.
  * Missing-digest path returns the bounded fallback.
  * PAS191's INTENT_CODES tuple still has exactly 15 entries
    (carry-forward).
  * No new SQL migration introduced under scripts/ whose filename
    carries "pas203".
  * combined_supabase_migration.sql is not committed on this
    branch.
  * No secret-shaped tokens in any PAS203 file.
  * Slack path writes nothing (the loader does not call any
    `write_text`, `mkdir`, or similar mutating helper).
  * The readiness gate itself never reads .env / hits the network.
  * PAS193..PAS202 carry-forward intact.

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
import tempfile
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


PAS203_FILES = (
    "docs/pas203_slack_evidence_digest_command.md",
    "scripts/pas203_slack_evidence_digest_readiness_check.py",
    "tests/mvp/test_pas203_slack_evidence_digest_command.py",
    "app/services/slack/simulation_digest_intent.py",
)


PAS202_CARRY_FORWARD_FILES = (
    "docs/pas202_evidence_digest_surface.md",
    "scripts/pas202_evidence_digest_surface_readiness_check.py",
    "scripts/pas202_view_simulation_evidence_digest.py",
    "tests/mvp/test_pas202_evidence_digest_surface.py",
    "app/services/simulation/evidence_digest_surface.py",
)


PAS201_CARRY_FORWARD_FILES = (
    "docs/pas201_simulation_evidence_digest.md",
    "scripts/pas201_evidence_digest_readiness_check.py",
    "scripts/pas201_build_simulation_evidence_digest.py",
    "tests/mvp/test_pas201_evidence_digest.py",
    "app/services/simulation/evidence_digest.py",
)


PAS192_CARRY_FORWARD_FILES = (
    "app/services/slack/operator_intents.py",
    "app/services/slack/operator_responses.py",
    "tests/mvp/test_pas192_slack_operator_experience.py",
)


PAS191_CARRY_FORWARD_FILES = (
    "tests/mvp/test_pas191_slack_natural_language_commands.py",
)


BANNED_IMPORT_MODULES: Tuple[str, ...] = (
    "twilio",
    "slack_sdk",
    "openai",
    "anthropic",
    "dotenv",
    "supabase",
)


# PAS203 must not import PAS191's intent / response modules
# (otherwise an accidental edit there could ripple into PAS203
# behaviour and vice-versa). It also must not import the outbound
# Slack notification client.
BANNED_IMPORT_PREFIXES: Tuple[str, ...] = (
    "twilio.",
    "slack_sdk.",
    "openai.",
    "anthropic.",
    "dotenv.",
    "supabase.",
    "app.services.slack.operator_intents",
    "app.services.slack.operator_responses",
    "app.routes.slack_command",
    "app.engine.state_machine",
    "app.engine",
    "app.services.notifications",
)


BANNED_CALL_NAMES: Tuple[str, ...] = (
    "load_dotenv",
    "get_supabase",
    "send_slack_message",
    "post_to_slack",
)


# Filesystem-write call names PAS203 must never make. The Slack
# path is strictly read-only.
WRITE_CALL_NAMES: Tuple[str, ...] = (
    "write_text",
    "write_bytes",
    "mkdir",
    "makedirs",
    "touch",
    "rename",
    "unlink",
    "rmdir",
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
)


SECRET_SHAPE_REGEXES = (
    re.compile(r"AKIA[0-9A-Z]{12,}"),
    re.compile(r"xox[bp]-[0-9A-Za-z\-]{10,}"),
    re.compile(r"sk_(live|test)_[A-Za-z0-9]{16,}"),
    re.compile(r"\bAC[0-9a-fA-F]{32}\b"),
    re.compile(r"\bSK[0-9a-fA-F]{32}\b"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
)


DOC_FILE = "docs/pas203_slack_evidence_digest_command.md"
DOC_REQUIRED_CLAUSES = (
    "purpose",
    "what pas203 proves",
    "what pas203 does not prove",
    "claimable",
    "still not claimable",
    "future pas204",
    "slack",
    "digest",
    "operator",
    "safety",
    "simulation_only",
    "read-only",
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

def check_pas203_files_present(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in PAS203_FILES:
        ok = (Path(repo_root) / rel).is_file()
        out.append(_check(
            f"files:exists:{rel}",
            "PASS" if ok else "FAIL",
            f"PAS203 artefact present: {rel}",
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


# Strict scan target: the production service file alone is bound
# by the strictest banned-import rules. The readiness gate and
# the test file legitimately import PAS191's operator_intents to
# verify the carry-forward invariant (INTENT_CODES count == 15);
# those imports are read-only AST inspections, not runtime
# coupling, and would never ship into a request path.
_STRICT_NO_BANNED_IMPORT_FILES = (
    "app/services/slack/simulation_digest_intent.py",
)


def check_no_banned_imports(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in _STRICT_NO_BANNED_IMPORT_FILES:
        src = _read_text(Path(repo_root) / rel) or ""
        imports, calls = _collect_imports_and_calls(src)
        bad = _banned_in(imports, calls)
        out.append(_check(
            f"no_banned_imports:{rel}",
            "FAIL" if bad else "PASS",
            f"{rel} is free of Twilio/Slack/LLM/Supabase/state_machine/operator_intents/operator_responses imports",
            detail=("disqualifying: " + ", ".join(sorted(set(bad)))) if bad else "",
        ))
    return out


def check_no_forbidden_status_literals(repo_root: str) -> List[dict]:
    targets = ("app/services/slack/simulation_digest_intent.py",)
    out: List[dict] = []
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
    targets = ("app/services/slack/simulation_digest_intent.py",)
    out: List[dict] = []
    for rel in targets:
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


def check_no_write_calls_in_service(repo_root: str) -> List[dict]:
    rel = "app/services/slack/simulation_digest_intent.py"
    src = _read_text(Path(repo_root) / rel) or ""
    _, calls = _collect_imports_and_calls(src)
    bad = sorted(name for name in WRITE_CALL_NAMES if name in calls)
    return [_check(
        f"no_write_calls:{rel}",
        "FAIL" if bad else "PASS",
        f"{rel} is strictly read-only (no filesystem write calls)",
        detail=("disqualifying: " + ", ".join(bad)) if bad else "",
    )]


def check_required_entry_points_present(repo_root: str) -> List[dict]:
    src = _read_text(
        Path(repo_root) / "app/services/slack/simulation_digest_intent.py",
    ) or ""
    names = _collect_identifier_names(src)
    required = (
        ("entry_point:INTENT_SIMULATION_DIGEST",
         "INTENT_SIMULATION_DIGEST", "intent code constant"),
        ("entry_point:SIMULATION_DIGEST_ALIASES",
         "SIMULATION_DIGEST_ALIASES", "alias tuple"),
        ("entry_point:SIMULATION_DIGEST_HELP_LINES",
         "SIMULATION_DIGEST_HELP_LINES", "help-line additions"),
        ("entry_point:MISSING_DIGEST_FALLBACK_MESSAGE",
         "MISSING_DIGEST_FALLBACK_MESSAGE", "fallback message"),
        ("entry_point:FORBIDDEN_OUTPUT_TOKENS",
         "FORBIDDEN_OUTPUT_TOKENS", "forbidden output tokens"),
        ("entry_point:match_simulation_digest_intent",
         "match_simulation_digest_intent", "intent matcher"),
        ("entry_point:find_latest_digest_path",
         "find_latest_digest_path", "loader"),
        ("entry_point:load_digest",
         "load_digest", "digest reader/validator"),
        ("entry_point:format_simulation_digest_response",
         "format_simulation_digest_response", "response builder"),
        ("entry_point:try_route_simulation_digest",
         "try_route_simulation_digest", "full route helper"),
    )
    return [
        _check(
            cid,
            "PASS" if name in names else "FAIL",
            f"simulation_digest_intent exposes {desc}",
            detail="" if name in names else f"name {name!r} missing",
        )
        for (cid, name, desc) in required
    ]


def check_required_alias_phrases_present(repo_root: str) -> List[dict]:
    src = _read_text(
        Path(repo_root) / "app/services/slack/simulation_digest_intent.py",
    ) or ""
    consts = _collect_string_constants(src)
    required = (
        "simulation digest",
        "evidence digest",
        "show simulation evidence",
        "what did the simulation prove",
        "rehearsal evidence",
        "strategy evidence",
    )
    out: List[dict] = []
    for phrase in required:
        present = phrase in consts
        out.append(_check(
            f"alias:{phrase.replace(' ', '_')}",
            "PASS" if present else "FAIL",
            f"alias table carries phrase {phrase!r}",
            detail="" if present else "phrase missing",
        ))
    return out


def check_pas191_intent_codes_unchanged(repo_root: str) -> List[dict]:
    sys.path.insert(0, repo_root)
    try:
        from app.services.slack.operator_intents import INTENT_CODES  # type: ignore
        ok = len(INTENT_CODES) == 15
        return [_check(
            "carry_forward:pas191_intent_codes_count",
            "PASS" if ok else "FAIL",
            "PAS191 INTENT_CODES tuple unchanged (exactly 15 entries)",
            detail="" if ok else f"got {len(INTENT_CODES)} entries",
        )]
    except Exception as e:
        return [_check(
            "carry_forward:pas191_intent_codes_count",
            "FAIL",
            "PAS191 INTENT_CODES tuple importable",
            detail=type(e).__name__,
        )]


def check_no_secret_shapes(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in PAS203_FILES:
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
            if "pas203" in name and (
                name.endswith(".sql") or "migrate" in name
            ):
                bad.append(entry.name)
    return [_check(
        "no_new_migration",
        "FAIL" if bad else "PASS",
        "PAS203 introduces no SQL migration",
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


def check_intent_smoke(repo_root: str) -> List[dict]:
    out: List[dict] = []
    sys.path.insert(0, repo_root)
    try:
        from app.services.simulation.behavioral_evaluation import (  # type: ignore
            build_behavioral_evaluation,
        )
        from app.services.simulation.evidence_digest import (  # type: ignore
            build_evidence_digest,
        )
        from app.services.simulation.manual_test_runtime import (  # type: ignore
            execute_manual_test_runtime,
        )
        from app.services.simulation.runtime_inspection import (  # type: ignore
            build_inspection,
        )
        from app.services.slack.simulation_digest_intent import (  # type: ignore
            FORBIDDEN_OUTPUT_TOKENS,
            MISSING_DIGEST_FALLBACK_MESSAGE,
            format_simulation_digest_response,
            match_simulation_digest_intent,
            try_route_simulation_digest,
        )
        # Build a synthetic clean digest
        rec = {
            "recommendation_id": "pas195-rec-readiness-smoke",
            "status": "CANDIDATE",
            "operator_required": True,
            "recommended_strategy": "callback_first",
            "rejected_strategy": "assertive",
            "recommendation_type": "promote_strategy",
            "confidence_level": "high",
            "pass_rate_threshold": 0.95,
            "phase": "PAS195",
        }
        rev = {
            "review_id": "pas196-rev-readiness-smoke",
            "recommendation_id": "pas195-rec-readiness-smoke",
            "previous_status": "CANDIDATE",
            "new_status": "APPROVED_FOR_MANUAL_TEST",
            "live_behavior_changed": False,
            "actor_type": "operator",
            "actor_id_token": "op_readinesssmoke",
            "reason_token": "operator_approved_for_manual_test",
            "reviewed_at": "2026-05-22T00:00:00Z",
            "operator_required": True,
            "phase": "PAS196",
        }
        pkg = {
            "package_id": "pas197-pkg-readiness-smoke",
            "phase": "PAS197",
            "recommendation_id": "pas195-rec-readiness-smoke",
            "review_id": "pas196-rev-readiness-smoke",
            "strategy_id": "callback_first",
            "status": "READY_FOR_MANUAL_TEST",
            "live_behavior_changed": False,
            "allowed_environment": "SIMULATION_ONLY",
            "test_plan": [],
            "success_metrics": [],
            "rollback_notes": [],
            "safety_notes": [],
            "created_at": "2026-05-22T00:00:00Z",
        }
        rt = execute_manual_test_runtime(pkg, created_at="2026-05-22T00:00:00Z")
        insp = build_inspection(rec, rev, pkg, rt, generated_at="2026-05-22T00:00:00Z")
        beh = build_behavioral_evaluation(
            rt, generated_at="2026-05-22T00:00:00Z", inspection=insp,
        )
        digest = build_evidence_digest(
            rec, rev, pkg, rt, insp, beh, generated_at="2026-05-22T00:00:00Z",
        )

        # match smoke
        out.append(_check(
            "intent:matches_simulation_digest",
            "PASS" if match_simulation_digest_intent("simulation digest") else "FAIL",
            "match_simulation_digest_intent('simulation digest') is True",
        ))
        out.append(_check(
            "intent:matches_what_did_the_simulation_prove",
            "PASS" if match_simulation_digest_intent(
                "what did the simulation prove?"
            ) else "FAIL",
            "match_simulation_digest_intent normalises trailing '?'",
        ))
        out.append(_check(
            "intent:rejects_unrelated_text",
            "PASS" if not match_simulation_digest_intent("stats") else "FAIL",
            "match_simulation_digest_intent rejects unrelated text",
        ))

        # response smoke
        slack_out = format_simulation_digest_response(digest)
        out.append(_check(
            "response:includes_simulation_only_marker",
            "PASS" if "SIMULATION_ONLY" in slack_out else "FAIL",
            "response carries SIMULATION_ONLY marker",
        ))
        out.append(_check(
            "response:includes_evidence_strength_marker",
            "PASS" if digest["evidence_strength"] in slack_out else "FAIL",
            "response carries evidence_strength token",
        ))
        bad = [t for t in FORBIDDEN_OUTPUT_TOKENS if t in slack_out.lower()]
        out.append(_check(
            "response:no_forbidden_tokens",
            "PASS" if not bad else "FAIL",
            "response carries no forbidden live-routing tokens",
            detail=", ".join(bad) if bad else "",
        ))

        # missing-digest smoke
        out.append(_check(
            "response:missing_digest_returns_fallback",
            "PASS" if format_simulation_digest_response(None) == MISSING_DIGEST_FALLBACK_MESSAGE else "FAIL",
            "missing digest returns bounded fallback string",
        ))

        # try_route smoke with empty directory
        with tempfile.TemporaryDirectory() as tmp:
            tp = Path(tmp)
            out_text = try_route_simulation_digest("simulation digest", tp)
            out.append(_check(
                "route:missing_digest_returns_fallback",
                "PASS" if out_text == MISSING_DIGEST_FALLBACK_MESSAGE else "FAIL",
                "try_route_simulation_digest returns fallback when dir empty",
            ))
            out.append(_check(
                "route:unrelated_returns_none",
                "PASS" if try_route_simulation_digest("stats", tp) is None else "FAIL",
                "try_route_simulation_digest returns None for unrelated text",
            ))
            # Ensure nothing was created.
            files_after = list(tp.iterdir())
            out.append(_check(
                "route:never_writes_to_reports_directory",
                "PASS" if files_after == [] else "FAIL",
                "try_route_simulation_digest writes nothing to disk",
                detail=", ".join(f.name for f in files_after) if files_after else "",
            ))
    except Exception as e:
        out.append(_check(
            "intent:smoke",
            "FAIL",
            "simulation_digest_intent module importable and runnable",
            detail=type(e).__name__,
        ))
    return out


def check_dispatcher_wiring(repo_root: str) -> List[dict]:
    """
    PAS203-A — verify slack_command.py imports and invokes the
    PAS203 helper, that the dispatch block carries no filesystem
    writes or simulation-execution calls, and that PAS191's
    match_intent invocation is preserved (i.e., the wiring is
    additive, not destructive).
    """
    rel = "app/routes/slack_command.py"
    src = _read_text(Path(repo_root) / rel)
    out: List[dict] = []
    if src is None:
        out.append(_check(
            "dispatcher:source_readable",
            "FAIL",
            f"{rel} is readable",
            detail="file missing or unreadable",
        ))
        return out

    out.append(_check(
        "dispatcher:imports_pas203_helper",
        "PASS" if (
            "from app.services.slack.simulation_digest_intent" in src
            and "try_route_simulation_digest" in src
        ) else "FAIL",
        f"{rel} imports try_route_simulation_digest from PAS203",
    ))

    pas203_pos = src.find("try_route_simulation_digest(text")
    pas191_pos = src.find("match_intent(text)")
    out.append(_check(
        "dispatcher:calls_try_route_simulation_digest",
        "PASS" if pas203_pos >= 0 else "FAIL",
        f"{rel} calls try_route_simulation_digest(text, ...)",
    ))
    out.append(_check(
        "dispatcher:pas191_match_intent_still_called",
        "PASS" if pas191_pos >= 0 else "FAIL",
        f"{rel} still calls match_intent(text) (PAS191 carry-forward)",
    ))
    out.append(_check(
        "dispatcher:pas203_branch_fires_before_pas191",
        "PASS" if (
            pas203_pos >= 0 and pas191_pos >= 0 and pas203_pos < pas191_pos
        ) else "FAIL",
        f"{rel} PAS203 dispatch fires BEFORE PAS191 fast-path",
        detail="" if (pas203_pos < pas191_pos and pas203_pos >= 0) else (
            f"pas203_pos={pas203_pos}, pas191_pos={pas191_pos}"
        ),
    ))

    out.append(_check(
        "dispatcher:logs_pas203_surface_event",
        "PASS" if "slack_command_pas203" in src else "FAIL",
        f"{rel} logs slack.intent.matched with PAS203 surface",
    ))

    out.append(_check(
        "dispatcher:emits_simulation_digest_intent_token",
        "PASS" if (
            '"simulation_digest"' in src or "'simulation_digest'" in src
        ) else "FAIL",
        f"{rel} emits simulation_digest intent token in log payload",
    ))

    # Slice the PAS203 block and verify no writes / no execution.
    start = src.find("PAS203-A — Read-only simulation evidence digest")
    end = src.find("PAS191 — Deterministic natural-language fast-path")
    block_ok = start >= 0 and end > start
    out.append(_check(
        "dispatcher:pas203_block_present",
        "PASS" if block_ok else "FAIL",
        f"{rel} carries a marked PAS203-A dispatch block",
        detail="" if block_ok else f"start={start}, end={end}",
    ))
    block = src[start:end] if block_ok else ""

    write_tokens = (
        ".write_text(",
        ".write_bytes(",
        ".mkdir(",
        ".touch(",
        ".rename(",
        ".unlink(",
        ".rmdir(",
        "os.makedirs(",
        "shutil.copy(",
        "shutil.move(",
    )
    bad_writes = [t for t in write_tokens if t in block]
    out.append(_check(
        "dispatcher:pas203_block_no_writes",
        "PASS" if not bad_writes else "FAIL",
        f"{rel} PAS203 dispatch block carries no filesystem write calls",
        detail=", ".join(bad_writes) if bad_writes else "",
    ))

    exec_tokens = (
        "execute_manual_test_runtime(",
        "build_evidence_digest(",
        "build_inspection(",
        "build_behavioral_evaluation(",
        "build_manual_test_package(",
        "run_scenario_under_strategy(",
        "compare_strategies(",
    )
    bad_execs = [t for t in exec_tokens if t in block]
    out.append(_check(
        "dispatcher:pas203_block_no_simulation_execution",
        "PASS" if not bad_execs else "FAIL",
        f"{rel} PAS203 dispatch block carries no simulation-execution calls",
        detail=", ".join(bad_execs) if bad_execs else "",
    ))

    out.append(_check(
        "dispatcher:pas203_block_returns_in_channel_response",
        "PASS" if (
            "JSONResponse" in block and "in_channel" in block
        ) else "FAIL",
        f"{rel} PAS203 dispatch returns JSONResponse with response_type=in_channel",
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
        "PAS203 readiness checker never reads .env / touches DB / hits network",
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
    checks.extend(check_pas203_files_present(repo_root))
    checks.extend(_check_carry_forward(repo_root, "pas202", PAS202_CARRY_FORWARD_FILES))
    checks.extend(_check_carry_forward(repo_root, "pas201", PAS201_CARRY_FORWARD_FILES))
    checks.extend(_check_carry_forward(repo_root, "pas192", PAS192_CARRY_FORWARD_FILES))
    checks.extend(_check_carry_forward(repo_root, "pas191", PAS191_CARRY_FORWARD_FILES))
    checks.extend(check_no_banned_imports(repo_root))
    checks.extend(check_no_forbidden_status_literals(repo_root))
    checks.extend(check_no_forbidden_identifiers(repo_root))
    checks.extend(check_no_write_calls_in_service(repo_root))
    checks.extend(check_required_entry_points_present(repo_root))
    checks.extend(check_required_alias_phrases_present(repo_root))
    checks.extend(check_pas191_intent_codes_unchanged(repo_root))
    checks.extend(check_no_secret_shapes(repo_root))
    checks.extend(check_no_new_migration(repo_root))
    checks.extend(check_no_combined_migration_committed(repo_root))
    checks.extend(check_doc_clauses(repo_root))
    checks.extend(check_intent_smoke(repo_root))
    checks.extend(check_dispatcher_wiring(repo_root))
    checks.extend(check_self_no_env_or_network(repo_root))

    agg = _aggregate(checks)
    return {
        "phase":            "PAS203",
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


REPORT_FILENAME = "pas203_slack_evidence_digest_readiness_report.json"


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="pas203_slack_evidence_digest_readiness_check",
        description=(
            "PAS203 — Slack Read-Only Evidence Digest readiness gate. "
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
        f"[PAS203] verdict={report['verdict']} "
        f"blockers={report['blocker_count']} "
        f"info={report['info_count']} "
        f"checks={report['check_count']} "
        f"pass={report['pass_count']} "
        f"fail={report['fail_count']}"
    )
    actions = report.get("operator_actions") or []
    if actions:
        print("[PAS203] operator actions:")
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
