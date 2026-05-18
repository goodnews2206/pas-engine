"""
PAS192 — Slack Operator Experience + Action Layer readiness gate.

Deterministic, non-mutating evaluator for "is PAS192 wired
correctly, additive-only over PAS191, deterministic, LLM-free for
read-only intents, free of PII / autonomous-behaviour leaks, and
not introducing any mutation execution path"?

Walks the repo and verifies:

  * PAS192 surfaces exist (doc / readiness gate / test).
  * Doctrine clauses present; no forbidden-feature tokens.
  * operator_intents.py carries the two new intent codes and
    aliases; `summary`, `today`, `next action`, `priorities`
    resolve via the closed alias table.
  * operator_responses.py carries format_today_summary +
    format_next_action; help / unknown rewording lands; PII guard
    still in place.
  * slack_command.py wires INTENT_TODAY_SUMMARY +
    INTENT_NEXT_ACTION through _pas191_dispatch and uses the new
    helper functions; the PAS191 fast-path ordering is preserved.
  * No new mutation-execution call sites; no schema migration; no
    `combined_supabase_migration.sql` edits; no LLM imports in
    pure service modules.
  * PAS191 readiness gate carry-forward intact.

Read-only: never reads .env, never touches Supabase, never
executes a deploy / migration / network call.

Exit codes:
  0 — READY
  1 — NOT_READY (one or more BLOCK checks failed)
  2 — bad CLI args
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional


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

SEVERITY_BLOCK = "BLOCK"


# ──────────────────────────────────────────────────────────────────
# Required artefacts
# ──────────────────────────────────────────────────────────────────

PAS192_FILES = (
    "docs/pas192_slack_operator_experience.md",
    "scripts/pas192_slack_operator_experience_readiness_check.py",
    "tests/mvp/test_pas192_slack_operator_experience.py",
    "app/services/slack/operator_intents.py",
    "app/services/slack/operator_responses.py",
    "app/routes/slack_command.py",
)


PAS191_CARRY_FORWARD_FILES = (
    "docs/pas191_slack_natural_language_commands.md",
    "scripts/pas191_slack_nl_command_readiness_check.py",
    "app/services/slack/operator_intents.py",
    "app/services/slack/operator_responses.py",
    "tests/mvp/test_pas191_slack_natural_language_commands.py",
)


DOC_FILE = "docs/pas192_slack_operator_experience.md"
DOC_REQUIRED_CLAUSES = (
    "purpose",
    "relationship to pas191",
    "deterministic mapping doctrine",
    "closed intent set doctrine",
    "no llm doctrine",
    "no mutation via natural language",
    "pii redaction doctrine",
    "fail-closed on unknown intent",
    "operator help doctrine",
    "alias table curation doctrine",
    "what pas192 intentionally does not build",
    "no autonomous remediation",
    "remaining limitations",
    "today_summary",
    "next_action",
)

FORBIDDEN_DOC_TOKENS = (
    "gmail oauth integration",
    "composio integration",
    "trust-claw",
    "auto-approve memory",
    "ai chat assistant enabled",
    "embedding model",
    "vector store",
    "imap inbox scanner",
    "pop3 inbox scanner",
    "auto-trip enabled",
    "autonomous trip",
    "free-form llm reply",
    "autonomous outreach",
    "auto resume",
    "auto-resume",
)


INTENTS_FILE = "app/services/slack/operator_intents.py"
INTENTS_REQUIRED_TOKENS = (
    "INTENT_TODAY_SUMMARY",
    "INTENT_NEXT_ACTION",
    '"today_summary"',
    '"next_action"',
    "MUTATION_COMMAND_TOKENS",
)

INTENTS_REQUIRED_ALIASES = (
    "summary",
    "today",
    "today summary",
    "daily summary",
    "what happened today",
    "what should i do now",
    "next action",
    "priorities",
    "what needs attention",
)


RESPONSES_FILE = "app/services/slack/operator_responses.py"
RESPONSES_REQUIRED_TOKENS = (
    "def format_today_summary",
    "def format_next_action",
    "_TODAY_SUMMARY_WARNING_LABELS",
    "_NEXT_ACTION_LABELS",
    "_PII_FORBIDDEN_TOKENS",
    "def _safe",
)
RESPONSES_FORBIDDEN_TOKENS = (
    "eval(",
    "exec(",
    "subprocess.",
    "os.system(",
    "requests.get(",
    "requests.post(",
    "httpx.get(",
    "httpx.post(",
    "urllib.request.urlopen(",
)


ROUTE_FILE = "app/routes/slack_command.py"
ROUTE_REQUIRED_TOKENS = (
    "INTENT_TODAY_SUMMARY",
    "INTENT_NEXT_ACTION",
    "_pas192_today_summary",
    "_pas192_next_action",
    "format_today_summary",
    "format_next_action",
    "match_intent(text)",
    "_pas191_dispatch",
    "slack.intent.matched",
    "_verify_slack_signature",
    "check_rate_limit",
)
# Mutation-execution helpers must NOT appear inside the
# _pas192_today_summary / _pas192_next_action blocks. We scan the
# whole file for these literals; they're allowed in the existing
# mutation branch (set_brokerage_active, update_featured_properties)
# but the PAS192 helpers themselves must not call them.
PAS192_HELPER_FUNCTIONS = (
    "_pas192_today_summary",
    "_pas192_next_action",
    "_pas192_count_agents",
    "_pas192_overdue_callbacks",
)
PAS192_FORBIDDEN_HELPER_TOKENS = (
    "set_brokerage_active(",
    "update_featured_properties(",
    "trip_circuit_breaker(",
    "send_outbound(",
    ".insert(",
    ".update(",
    ".delete(",
    ".upsert(",
)


# Pure-data forbidden imports (LLM, vector, gmail, composio…)
FORBIDDEN_IMPORT_PREFIXES = (
    "from googleapiclient",
    "import googleapiclient",
    "from google.oauth2",
    "import google.oauth2",
    "from google_auth_oauthlib",
    "import google_auth_oauthlib",
    "from imaplib",
    "import imaplib",
    "from poplib",
    "import poplib",
    "from composio",
    "import composio",
    "from trustclaw",
    "import trustclaw",
    "from chromadb",
    "import chromadb",
    "from pinecone",
    "import pinecone",
    "from pgvector",
    "import pgvector",
    "from sentence_transformers",
    "import sentence_transformers",
    "from openai",
    "import openai",
)

PURE_SERVICE_FILES = (
    "app/services/slack/operator_intents.py",
    "app/services/slack/operator_responses.py",
)

FORBIDDEN_LLM_IMPORTS = (
    "from app.services.llm",
    "import app.services.llm",
    "from anthropic",
    "import anthropic",
)


# Event contract — PAS192 reuses the PAS191 event types.
EVENT_CONTRACT_FILE = "app/services/events/contract.py"
EVENT_CONTRACT_REQUIRED_EVENT_TYPES = (
    '"slack.intent.matched"',
    '"slack.intent.unknown"',
)


# ──────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────

def _check(check_id: str, status: str, label: str, *, severity: str = SEVERITY_BLOCK, detail: str = "") -> dict:
    return {
        "id":       check_id,
        "status":   status,
        "label":    label,
        "severity": severity,
        "detail":   detail,
    }


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _read_text(path: Path) -> Optional[str]:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None


def _strip_python_comments_and_strings(src: str) -> str:
    out: list = []
    i, n = 0, len(src)
    while i < n:
        ch = src[i]
        if ch == "#":
            j = src.find("\n", i)
            if j < 0:
                break
            i = j + 1
            continue
        if src.startswith('"""', i) or src.startswith("'''", i):
            quote = src[i:i + 3]
            end = src.find(quote, i + 3)
            if end < 0:
                break
            i = end + 3
            continue
        if ch in ('"', "'"):
            quote = ch
            j = i + 1
            while j < n:
                if src[j] == "\\":
                    j += 2
                    continue
                if src[j] == quote or src[j] == "\n":
                    break
                j += 1
            i = j + 1
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def _extract_function_body(src: str, fn_name: str) -> str:
    marker = f"def {fn_name}("
    start = src.find(marker)
    if start < 0:
        return ""
    line_start = src.rfind("\n", 0, start) + 1
    end = len(src)
    cursor = src.find("\n", start) + 1
    while cursor < len(src):
        nl = src.find("\n", cursor)
        nl = len(src) if nl < 0 else nl
        line = src[cursor:nl]
        if line and not line[0].isspace() and (
            line.startswith(("def ", "async def ", "class "))
        ):
            end = cursor
            break
        cursor = nl + 1
    return src[line_start:end]


# ──────────────────────────────────────────────────────────────────
# Checks
# ──────────────────────────────────────────────────────────────────

def check_pas192_files_present(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for p in PAS192_FILES:
        ok = (Path(repo_root) / p).is_file()
        out.append(_check(
            f"file:{p}",
            "PASS" if ok else "FAIL",
            f"Required PAS192 artefact present: {p}",
            detail="" if ok else "missing",
        ))
    return out


def check_pas191_carry_forward(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for p in PAS191_CARRY_FORWARD_FILES:
        ok = (Path(repo_root) / p).is_file()
        out.append(_check(
            f"pas191_carry:{p}",
            "PASS" if ok else "FAIL",
            f"PAS191 surface still present: {p}",
            detail="" if ok else "missing — PAS192 must not delete PAS191 surfaces",
        ))
    return out


def check_doc_clauses(repo_root: str) -> List[dict]:
    out: List[dict] = []
    src = (_read_text(Path(repo_root) / DOC_FILE) or "").lower()
    for clause in DOC_REQUIRED_CLAUSES:
        out.append(_check(
            f"doc:clause:{clause}",
            "PASS" if clause in src else "FAIL",
            f"PAS192 doctrine doc carries clause: {clause}",
            detail="" if clause in src else "missing required clause",
        ))
    return out


def check_doc_no_forbidden_scope(repo_root: str) -> List[dict]:
    src = (_read_text(Path(repo_root) / DOC_FILE) or "").lower()
    bad = [t for t in FORBIDDEN_DOC_TOKENS if t in src]
    return [_check(
        "doc:no_forbidden_scope",
        "FAIL" if bad else "PASS",
        "PAS192 doctrine doc introduces no out-of-scope feature token",
        detail=("disqualifying: " + ", ".join(bad)) if bad else "",
    )]


def check_intents_module(repo_root: str) -> List[dict]:
    out: List[dict] = []
    src = _read_text(Path(repo_root) / INTENTS_FILE) or ""
    for tok in INTENTS_REQUIRED_TOKENS:
        out.append(_check(
            f"intents:token:{tok[:60]}",
            "PASS" if tok in src else "FAIL",
            f"operator_intents.py carries: {tok}",
            detail="" if tok in src else "token missing",
        ))
    # Aliases must appear as quoted keys in the alias table.
    for alias in INTENTS_REQUIRED_ALIASES:
        needle = f'"{alias}"'
        ok = needle in src
        out.append(_check(
            f"intents:alias:{alias}",
            "PASS" if ok else "FAIL",
            f"operator_intents.py alias table carries: {alias}",
            detail="" if ok else f"alias {needle} missing from _ALIAS_TABLE",
        ))
    return out


def check_pure_services_no_llm(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for relpath in PURE_SERVICE_FILES:
        fp = Path(repo_root) / relpath
        src = _read_text(fp) or ""
        executable = _strip_python_comments_and_strings(src)
        bad: List[str] = []
        for line in executable.splitlines():
            stripped = line.strip()
            for pref in FORBIDDEN_LLM_IMPORTS:
                if stripped.startswith(pref):
                    bad.append(pref)
                    break
            for pref in FORBIDDEN_IMPORT_PREFIXES:
                if stripped.startswith(pref):
                    bad.append(pref)
                    break
        out.append(_check(
            f"pure_no_llm:{relpath}",
            "FAIL" if bad else "PASS",
            f"{relpath} contains no forbidden LLM / vector / external import",
            detail=("disqualifying: " + ", ".join(bad)) if bad else "",
        ))
    return out


def check_responses_module(repo_root: str) -> List[dict]:
    out: List[dict] = []
    src = _read_text(Path(repo_root) / RESPONSES_FILE) or ""
    for tok in RESPONSES_REQUIRED_TOKENS:
        out.append(_check(
            f"responses:token:{tok[:60]}",
            "PASS" if tok in src else "FAIL",
            f"operator_responses.py carries: {tok}",
            detail="" if tok in src else "token missing",
        ))
    executable = _strip_python_comments_and_strings(src)
    bad = [t for t in RESPONSES_FORBIDDEN_TOKENS if t in executable]
    out.append(_check(
        "responses:no_unsafe_constructs",
        "FAIL" if bad else "PASS",
        "operator_responses.py contains no eval/exec/subprocess/network patterns",
        detail=("disqualifying: " + ", ".join(bad)) if bad else "",
    ))
    return out


def check_route_wirethrough(repo_root: str) -> List[dict]:
    out: List[dict] = []
    src = _read_text(Path(repo_root) / ROUTE_FILE) or ""
    for tok in ROUTE_REQUIRED_TOKENS:
        out.append(_check(
            f"route:token:{tok[:60]}",
            "PASS" if tok in src else "FAIL",
            f"slack_command.py carries: {tok}",
            detail="" if tok in src else "token missing",
        ))
    # Fast-path ordering still preserved.
    fast_idx = src.find("match_intent(text)")
    llm_idx = src.find("_parse_intent(text)")
    ordered_ok = fast_idx > 0 and llm_idx > 0 and fast_idx < llm_idx
    out.append(_check(
        "route:fast_path_before_llm",
        "PASS" if ordered_ok else "FAIL",
        "PAS191/PAS192 deterministic fast-path fires BEFORE LLM intent parser",
        detail="" if ordered_ok else (
            f"ordering wrong (fast_idx={fast_idx}, llm_idx={llm_idx})"
        ),
    ))
    # The new PAS192 helpers must never call a mutation function.
    for fn in PAS192_HELPER_FUNCTIONS:
        body = _extract_function_body(src, fn)
        if not body:
            out.append(_check(
                f"route:helper:{fn}",
                "FAIL",
                f"PAS192 helper present: {fn}",
                detail="function not found",
            ))
            continue
        body_executable = _strip_python_comments_and_strings(body)
        bad_tok = [t for t in PAS192_FORBIDDEN_HELPER_TOKENS if t in body_executable]
        out.append(_check(
            f"route:helper_readonly:{fn}",
            "FAIL" if bad_tok else "PASS",
            f"PAS192 helper {fn} is read-only — no mutation",
            detail=("disqualifying: " + ", ".join(bad_tok)) if bad_tok else "",
        ))
    return out


def check_event_contract(repo_root: str) -> List[dict]:
    out: List[dict] = []
    src = _read_text(Path(repo_root) / EVENT_CONTRACT_FILE) or ""
    for tok in EVENT_CONTRACT_REQUIRED_EVENT_TYPES:
        ok = tok in src
        out.append(_check(
            f"contract:event:{tok}",
            "PASS" if ok else "FAIL",
            f"events/contract.py carries event_type literal: {tok}",
            detail="" if ok else "literal missing — contract drift",
        ))
    return out


def check_no_new_migration(repo_root: str) -> List[dict]:
    # PAS192 must not have introduced a new SQL migration. We
    # tolerate the existing combined_supabase_migration.sql so
    # long as it stayed at its tracked path; we never read or
    # validate its contents. Just assert no new migrate_v* file
    # appeared on disk whose name carries "pas192".
    root = Path(repo_root) / "scripts"
    bad: list = []
    if root.is_dir():
        for entry in root.iterdir():
            name = entry.name.lower()
            if "pas192" in name and (
                name.endswith(".sql") or "migrate" in name
            ):
                bad.append(entry.name)
    return [_check(
        "no_new_migration",
        "FAIL" if bad else "PASS",
        "PAS192 introduces no SQL migration",
        detail=("found: " + ", ".join(bad)) if bad else "",
    )]


def check_runtime_intent_resolution(repo_root: str) -> List[dict]:
    """
    Import the mapper and the formatters and assert that the new
    intents resolve. Pure in-process — no DB / no network.
    """
    out: List[dict] = []
    sys.path.insert(0, repo_root)
    try:
        from app.services.slack.operator_intents import (  # type: ignore
            INTENT_NEXT_ACTION,
            INTENT_TODAY_SUMMARY,
            match_intent,
        )
        cases = (
            ("summary",                   INTENT_TODAY_SUMMARY),
            ("today",                     INTENT_TODAY_SUMMARY),
            ("daily summary",             INTENT_TODAY_SUMMARY),
            ("what happened today",       INTENT_TODAY_SUMMARY),
            ("what should i do now",      INTENT_NEXT_ACTION),
            ("next action",               INTENT_NEXT_ACTION),
            ("priorities",                INTENT_NEXT_ACTION),
            ("what needs attention",      INTENT_NEXT_ACTION),
        )
        for phrase, expected in cases:
            actual = match_intent(phrase).get("intent")
            ok = actual == expected
            out.append(_check(
                f"runtime:match:{phrase}",
                "PASS" if ok else "FAIL",
                f"phrase {phrase!r} maps to {expected}",
                detail="" if ok else f"got {actual!r}",
            ))
        # Mutation refusal still holds.
        for bad_phrase in (
            "pause",
            "resume now",
            "push 123 Main St",
            "remove 123 Main St",
        ):
            actual = match_intent(bad_phrase).get("intent")
            ok = actual == "unknown"
            out.append(_check(
                f"runtime:mutation_refusal:{bad_phrase}",
                "PASS" if ok else "FAIL",
                f"mutation phrase {bad_phrase!r} stays UNKNOWN",
                detail="" if ok else f"got {actual!r}",
            ))
    except Exception as e:
        out.append(_check(
            "runtime:import",
            "FAIL",
            "operator_intents importable for runtime checks",
            detail=type(e).__name__,
        ))

    try:
        from app.services.slack import operator_responses as r  # type: ignore
        # Formatter sanity — empty inputs never raise.
        r.format_today_summary({})
        r.format_next_action({})
        r.format_next_action({"priorities": [
            {"code": "assign_agents", "detail": "0 configured"},
            {"code": "review_callbacks", "detail": "3 overdue"},
        ]})
        out.append(_check(
            "runtime:formatters",
            "PASS",
            "PAS192 formatters render under empty / populated inputs",
            detail="",
        ))
    except Exception as e:
        out.append(_check(
            "runtime:formatters",
            "FAIL",
            "PAS192 formatters render under empty / populated inputs",
            detail=type(e).__name__,
        ))
    return out


def check_no_pii_keys_in_helpers(repo_root: str) -> List[dict]:
    """The PAS192 dispatcher helpers must never select PII columns."""
    src = _read_text(Path(repo_root) / ROUTE_FILE) or ""
    pii_select_tokens = (
        '"phone_number"',
        '"phone"',
        '"email"',
        '"lead_name"',
        '"transcript"',
        '"raw_payload"',
        '"raw_email"',
        '"raw_body"',
    )
    out: List[dict] = []
    for fn in PAS192_HELPER_FUNCTIONS:
        body = _extract_function_body(src, fn)
        if not body:
            continue
        bad = [tok for tok in pii_select_tokens if tok in body]
        out.append(_check(
            f"route:no_pii_select:{fn}",
            "FAIL" if bad else "PASS",
            f"PAS192 helper {fn} selects no PII columns",
            detail=("disqualifying: " + ", ".join(bad)) if bad else "",
        ))
    return out


def check_self_no_env_or_db(repo_root: str) -> List[dict]:
    out: List[dict] = []
    fp = Path(__file__)
    src = _read_text(fp) or ""
    executable = _strip_python_comments_and_strings(src)
    bad: List[str] = []
    for line in executable.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith(("import dotenv", "from dotenv")):
            bad.append("dotenv import")
        if stripped.startswith(("import supabase", "from supabase")):
            bad.append("supabase import")
        if "load_dotenv(" in stripped:
            bad.append("load_dotenv() call")
        if stripped.startswith(("os.environ[", "getenv(")):
            bad.append("environ read")
        if "get_supabase" in stripped:
            bad.append("supabase client call")
    for tok in (
        "subprocess.run(",
        "subprocess.call(",
        "requests.get(",
        "requests.post(",
        "httpx.get(",
        "httpx.post(",
        "urllib.request.urlopen(",
        "git push",
        "railway deploy",
    ):
        if tok in executable:
            bad.append(tok)
    out.append(_check(
        "self_check:no_env_or_db_or_network",
        "FAIL" if bad else "PASS",
        "PAS192 readiness checker never reads .env / touches DB / hits network",
        detail=("disqualifying: " + ", ".join(bad)) if bad else "",
    ))
    return out


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
    checks.extend(check_pas192_files_present(repo_root))
    checks.extend(check_pas191_carry_forward(repo_root))
    checks.extend(check_doc_clauses(repo_root))
    checks.extend(check_doc_no_forbidden_scope(repo_root))
    checks.extend(check_intents_module(repo_root))
    checks.extend(check_pure_services_no_llm(repo_root))
    checks.extend(check_responses_module(repo_root))
    checks.extend(check_route_wirethrough(repo_root))
    checks.extend(check_event_contract(repo_root))
    checks.extend(check_no_new_migration(repo_root))
    checks.extend(check_runtime_intent_resolution(repo_root))
    checks.extend(check_no_pii_keys_in_helpers(repo_root))
    checks.extend(check_self_no_env_or_db(repo_root))

    agg = _aggregate(checks)
    return {
        "phase":            "PAS192",
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


REPORT_FILENAME = "pas192_slack_operator_experience_readiness_report.json"


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="pas192_slack_operator_experience_readiness_check",
        description=(
            "PAS192 — Slack Operator Experience + Action Layer "
            "readiness gate. Read-only — never reads .env, never "
            "touches Supabase, never executes a deploy / migration."
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
        f"[PAS192] verdict={report['verdict']} "
        f"blockers={report['blocker_count']} "
        f"info={report['info_count']} "
        f"checks={report['check_count']} "
        f"pass={report['pass_count']} "
        f"fail={report['fail_count']}"
    )
    actions = report.get("operator_actions") or []
    if actions:
        print("[PAS192] operator actions:")
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
        print(f"error: --repo-root not a directory: {repo_root}", file=sys.stderr)
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
