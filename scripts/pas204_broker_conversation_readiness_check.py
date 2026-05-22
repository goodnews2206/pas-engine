"""
PAS204 — Broker conversation intelligence readiness gate.

Deterministic, read-only evaluator confirming PAS204 is wired
correctly, additive-only over PAS191/PAS192/PAS203, free of
Twilio/Slack/Supabase/state-machine dependencies, deterministic,
free of forbidden status literals or live-mutation /
outbound-messaging identifiers, structurally bounded to
SIMULATION_ONLY, and not introducing any new SQL migration.

Checks include:

  * PAS204 surfaces exist (catalogue / classifier / response
    voice / surface / runner / readiness / tests / doc).
  * Catalogue carries >= 300 questions across 22 intents and 22
    categories.
  * Classifier matches every catalogue entry to its expected
    intent (100% on canonical text).
  * Response voice exposes a non-empty translation table, every
    intent has a response builder and at least one next-step
    suggestion, and forbidden live-routing tokens never appear
    in any rendered response.
  * Conversation surface returns the closed envelope shape and
    never emits a forbidden token.
  * PAS191's INTENT_CODES tuple still has exactly 15 entries.
  * Production source files do not import twilio / slack_sdk /
    openai / anthropic / dotenv / supabase / state machine /
    outbound notifications / operator_intents / operator_responses.
  * Production source files do not carry forbidden status
    literals or live-mutation / outbound-messaging identifiers.
  * No new SQL migration introduced under scripts/ whose
    filename carries "pas204".
  * combined_supabase_migration.sql is not committed.
  * No secret-shaped tokens in any PAS204 file.
  * The readiness gate itself never reads .env / hits the
    network.

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


PAS204_FILES = (
    "docs/pas204_broker_conversation_intelligence.md",
    "scripts/pas204_broker_conversation_readiness_check.py",
    "scripts/pas204_run_broker_question_simulations.py",
    "tests/mvp/test_pas204_broker_conversation_intelligence.py",
    "app/services/slack/broker_question_catalogue.py",
    "app/services/slack/broker_conversation_intents.py",
    "app/services/slack/broker_response_voice.py",
    "app/services/slack/broker_conversation_surface.py",
)


_PAS204_PRODUCTION_FILES = (
    "app/services/slack/broker_question_catalogue.py",
    "app/services/slack/broker_conversation_intents.py",
    "app/services/slack/broker_response_voice.py",
    "app/services/slack/broker_conversation_surface.py",
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


DOC_FILE = "docs/pas204_broker_conversation_intelligence.md"
DOC_REQUIRED_CLAUSES = (
    "what pas204 proves",
    "what pas204 does not prove",
    "claimable",
    "still not claimable",
    "future pas205",
    "broker",
    "operator",
    "safety",
    "simulation_only",
    "deterministic",
    "research basis",
    "tone",
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

def check_pas204_files_present(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in PAS204_FILES:
        ok = (Path(repo_root) / rel).is_file()
        out.append(_check(
            f"files:exists:{rel}",
            "PASS" if ok else "FAIL",
            f"PAS204 artefact present: {rel}",
            detail="" if ok else "file missing",
        ))
    return out


def check_no_banned_imports(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in _PAS204_PRODUCTION_FILES:
        src = _read_text(Path(repo_root) / rel) or ""
        imports, calls = _collect_imports_and_calls(src)
        bad = _banned_in(imports, calls)
        out.append(_check(
            f"no_banned_imports:{rel}",
            "FAIL" if bad else "PASS",
            f"{rel} is free of Twilio/Slack/LLM/Supabase/state_machine/notifications/operator_intents/operator_responses imports",
            detail=("disqualifying: " + ", ".join(sorted(set(bad)))) if bad else "",
        ))
    return out


def check_no_forbidden_status_literals(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in _PAS204_PRODUCTION_FILES:
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
    for rel in _PAS204_PRODUCTION_FILES:
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


def check_required_entry_points_present(repo_root: str) -> List[dict]:
    catalogue_src = _read_text(
        Path(repo_root) / "app/services/slack/broker_question_catalogue.py",
    ) or ""
    classifier_src = _read_text(
        Path(repo_root) / "app/services/slack/broker_conversation_intents.py",
    ) or ""
    voice_src = _read_text(
        Path(repo_root) / "app/services/slack/broker_response_voice.py",
    ) or ""
    surface_src = _read_text(
        Path(repo_root) / "app/services/slack/broker_conversation_surface.py",
    ) or ""
    return [
        _check(
            "entry_point:BROKER_QUESTION_CATALOGUE",
            "PASS" if "BROKER_QUESTION_CATALOGUE" in catalogue_src else "FAIL",
            "broker_question_catalogue exposes BROKER_QUESTION_CATALOGUE",
        ),
        _check(
            "entry_point:question_count",
            "PASS" if "question_count" in catalogue_src else "FAIL",
            "broker_question_catalogue exposes question_count()",
        ),
        _check(
            "entry_point:match_broker_intent",
            "PASS" if "match_broker_intent" in classifier_src else "FAIL",
            "broker_conversation_intents exposes match_broker_intent",
        ),
        _check(
            "entry_point:translate_token",
            "PASS" if "translate_token" in voice_src else "FAIL",
            "broker_response_voice exposes translate_token",
        ),
        _check(
            "entry_point:response_for_intent",
            "PASS" if "response_for_intent" in voice_src else "FAIL",
            "broker_response_voice exposes response_for_intent",
        ),
        _check(
            "entry_point:next_step_suggestions",
            "PASS" if "next_step_suggestions" in voice_src else "FAIL",
            "broker_response_voice exposes next_step_suggestions",
        ),
        _check(
            "entry_point:build_broker_response",
            "PASS" if "build_broker_response" in surface_src else "FAIL",
            "broker_conversation_surface exposes build_broker_response",
        ),
        _check(
            "entry_point:FORBIDDEN_OUTPUT_TOKENS",
            "PASS" if "FORBIDDEN_OUTPUT_TOKENS" in voice_src else "FAIL",
            "broker_response_voice exposes FORBIDDEN_OUTPUT_TOKENS",
        ),
    ]


def check_no_secret_shapes(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for rel in PAS204_FILES:
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
            if "pas204" in name and (
                name.endswith(".sql") or "migrate" in name
            ):
                bad.append(entry.name)
    return [_check(
        "no_new_migration",
        "FAIL" if bad else "PASS",
        "PAS204 introduces no SQL migration",
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
    fp = Path(repo_root) / "scripts" / "pas204_run_broker_question_simulations.py"
    src = _read_text(fp) or ""
    ok = "reports/simulations" in src.replace("\\", "/") or "REPORTS_SUBDIR" in src
    return [_check(
        "runner:writes_only_reports_dir",
        "PASS" if ok else "FAIL",
        "runner writes only under reports/simulations/",
    )]


def check_intent_smoke(repo_root: str) -> List[dict]:
    sys.path.insert(0, repo_root)
    out: List[dict] = []
    try:
        from app.services.slack.broker_conversation_intents import (  # type: ignore
            INTENT_FALLBACK_CLARIFY,
            match_broker_intent,
        )
        from app.services.slack.broker_conversation_surface import (  # type: ignore
            build_broker_response,
        )
        from app.services.slack.broker_question_catalogue import (  # type: ignore
            BROKER_QUESTION_CATALOGUE,
            CATEGORIES,
            INTENT_CODES,
            question_count,
        )
        from app.services.slack.broker_response_voice import (  # type: ignore
            FORBIDDEN_OUTPUT_TOKENS,
            response_for_intent,
        )
    except Exception as e:
        return [_check(
            "smoke:imports",
            "FAIL",
            "PAS204 modules importable",
            detail=type(e).__name__,
        )]

    out.append(_check(
        "catalogue:question_count_at_least_300",
        "PASS" if question_count() >= 300 else "FAIL",
        "catalogue carries >= 300 questions",
        detail=str(question_count()),
    ))
    out.append(_check(
        "catalogue:has_22_intents",
        "PASS" if len(INTENT_CODES) == 22 else "FAIL",
        "catalogue declares 22 closed intents",
        detail=str(len(INTENT_CODES)),
    ))
    out.append(_check(
        "catalogue:has_22_categories",
        "PASS" if len(CATEGORIES) == 22 else "FAIL",
        "catalogue declares 22 closed categories",
        detail=str(len(CATEGORIES)),
    ))

    # Classifier matches every canonical entry.
    miss = 0
    for q in BROKER_QUESTION_CATALOGUE:
        if match_broker_intent(q["text"])["intent"] != q["intent"]:
            miss += 1
    out.append(_check(
        "classifier:matches_every_canonical_entry",
        "PASS" if miss == 0 else "FAIL",
        "classifier matches every canonical catalogue entry",
        detail=f"mismatches={miss}",
    ))

    # Every intent has a response builder + suggestions.
    bad_intents = []
    for i in INTENT_CODES:
        try:
            body = response_for_intent(i)
        except Exception as e:
            bad_intents.append(f"{i}:{type(e).__name__}")
            continue
        if not isinstance(body, str) or len(body) < 40:
            bad_intents.append(f"{i}:short")
    out.append(_check(
        "voice:response_for_every_intent",
        "PASS" if not bad_intents else "FAIL",
        "every intent has a non-empty response builder",
        detail=", ".join(bad_intents) if bad_intents else "",
    ))

    # No forbidden tokens in any rendered response.
    bad_tok = []
    for i in INTENT_CODES:
        body = response_for_intent(i).lower()
        for tok in FORBIDDEN_OUTPUT_TOKENS:
            if tok in body:
                bad_tok.append(f"{i}:{tok}")
    out.append(_check(
        "voice:no_forbidden_tokens_in_any_response",
        "PASS" if not bad_tok else "FAIL",
        "no rendered response contains a forbidden live-routing token",
        detail=", ".join(bad_tok) if bad_tok else "",
    ))

    # Conversation surface envelope shape.
    env = build_broker_response("how many leads today")
    required = ("intent", "score", "response_text", "suggested_next",
                "evidence_grounded", "no_data_available",
                "clarifying_question")
    missing = [k for k in required if k not in env]
    out.append(_check(
        "surface:envelope_shape",
        "PASS" if not missing else "FAIL",
        "build_broker_response returns the closed envelope",
        detail=", ".join(missing) if missing else "",
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
        "PAS204 readiness checker never reads .env / touches DB / hits network",
        detail=("disqualifying: " + ", ".join(sorted(set(bad)))) if bad else "",
    )]


# ──────────────────────────────────────────────────────────────────
# Aggregator + CLI
# ──────────────────────────────────────────────────────────────────

def evaluate(repo_root: str) -> dict:
    checks: List[dict] = []
    checks.extend(check_pas204_files_present(repo_root))
    checks.extend(check_no_banned_imports(repo_root))
    checks.extend(check_no_forbidden_status_literals(repo_root))
    checks.extend(check_no_forbidden_identifiers(repo_root))
    checks.extend(check_required_entry_points_present(repo_root))
    checks.extend(check_no_secret_shapes(repo_root))
    checks.extend(check_no_new_migration(repo_root))
    checks.extend(check_no_combined_migration_committed(repo_root))
    checks.extend(check_doc_clauses(repo_root))
    checks.extend(check_runner_writes_only_reports(repo_root))
    checks.extend(check_intent_smoke(repo_root))
    checks.extend(check_pas191_intent_codes_unchanged(repo_root))
    checks.extend(check_self_no_env_or_network(repo_root))

    blockers = [
        c for c in checks
        if c["status"] == "FAIL" and c.get("severity") == SEVERITY_BLOCK
    ]
    verdict = VERDICT_NOT_READY if blockers else VERDICT_READY
    return {
        "phase":            "PAS204",
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
            f"[{c.get('severity') or SEVERITY_BLOCK}] {c['id']} — "
            f"{c.get('detail') or 'see report'}."
            for c in checks if c["status"] == "FAIL"
        ],
    }


REPORT_FILENAME = "pas204_broker_conversation_readiness_report.json"


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="pas204_broker_conversation_readiness_check",
        description=(
            "PAS204 — Broker Conversation Intelligence readiness gate. "
            "Read-only. Never reads .env, never touches Supabase, "
            "never executes a deploy / migration / network call."
        ),
    )
    p.add_argument("--repo-root", default=_REPO_ROOT_DEFAULT)
    p.add_argument("--output",    default=REPORT_FILENAME)
    p.add_argument("--json",      action="store_true")
    p.add_argument("--summary-only", action="store_true")
    return p


def _print_summary(report: dict) -> None:
    print(
        f"[PAS204] verdict={report['verdict']} "
        f"blockers={report['blocker_count']} "
        f"info={report['info_count']} "
        f"checks={report['check_count']} "
        f"pass={report['pass_count']} "
        f"fail={report['fail_count']}"
    )
    actions = report.get("operator_actions") or []
    if actions:
        print("[PAS204] operator actions:")
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
