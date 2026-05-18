"""
PAS191 — Bounded Slack natural-language operator commands readiness gate.

Deterministic, non-mutating evaluator for "is PAS191 wired
correctly, additive-only, deterministic, LLM-free for read-only
intents, and free of PII / autonomous-behaviour leaks?".

Walks the repo and verifies:

  * PAS191 surfaces exist (doc / readiness gate / mapper service /
    response formatter / test file).
  * Doctrine clauses present; no forbidden-feature tokens.
  * operator_intents.py: 12 closed intent codes + alias table +
    mutation refusal + no LLM / autonomous-execution imports.
  * operator_responses.py: per-intent formatters present + PII
    forbidden-token guard present + no LLM / network imports.
  * slack_command.py: deterministic fast-path wired BEFORE the
    LLM intent parser; mutation commands NOT routed to
    match_intent(); existing signature verification + rate-limit
    invariants preserved.
  * Event contract carries the 2 PAS191 event types.
  * No Gmail / google-auth / IMAP / POP3 / Composio / TrustClaw /
    embedding / vector / openai imports in any PAS191 surface.
  * Memory Review surface untouched.
  * Worker remains OFF by default.
  * PAS160-PAS190 + PAS-SECURITY-01/02/03/04 readiness scripts
    still on disk.

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

PAS191_FILES = (
    "docs/pas191_slack_natural_language_commands.md",
    "scripts/pas191_slack_nl_command_readiness_check.py",
    "app/services/slack/operator_intents.py",
    "app/services/slack/operator_responses.py",
    "tests/mvp/test_pas191_slack_natural_language_commands.py",
)


PRIOR_PHASE_FILES = (
    "scripts/pas160_mvp_sequence_check.py",
    "scripts/pas161_lead_ingestion_readiness_check.py",
    "scripts/pas162_pending_calls_readiness_check.py",
    "scripts/pas163_candidate_pipeline_readiness_check.py",
    "scripts/pas164_email_ingestion_readiness_check.py",
    "scripts/pas165_email_auth_dedupe_readiness_check.py",
    "scripts/pas166_email_dedupe_policy_readiness_check.py",
    "scripts/pas167_email_secret_reaper_readiness_check.py",
    "scripts/pas168_email_secret_rotation_readiness_check.py",
    "scripts/pas169_crypto_roundtrip_check.py",
    "scripts/pas169_launch_readiness_check.py",
    "scripts/pas_launch_integrity_check.py",
    "scripts/pas170_operator_survival_readiness_check.py",
    "scripts/pas171_external_pilot_readiness_check.py",
    "scripts/pas172_pilot_operations_readiness_check.py",
    "scripts/pas173_brokerage_operator_readiness_check.py",
    "scripts/pas174_operator_audit_readiness_check.py",
    "scripts/pas175_audit_integrity_readiness_check.py",
    "scripts/pas176_audit_chain_readiness_check.py",
    "scripts/pas177_tenant_audit_verification_readiness_check.py",
    "scripts/pas178_audit_window_chain_readiness_check.py",
    "scripts/pas179_controlled_learning_readiness_check.py",
    "scripts/pas180_learning_review_readiness_check.py",
    "scripts/pas181_manual_test_harness_readiness_check.py",
    "scripts/pas182_adaptive_memory_bridge_readiness_check.py",
    "scripts/pas183_onboarding_product_readiness_check.py",
    "scripts/pas184_pilot_experience_readiness_check.py",
    "scripts/pas186_final_cutover_readiness_check.py",
    "scripts/pas187_fleet_cutover_readiness_check.py",
    "scripts/pas188_operational_scaling_readiness_check.py",
    "scripts/pas189_operational_wirethrough_readiness_check.py",
    "scripts/pas190_final_wirethrough_readiness_check.py",
    "scripts/pas_security_01_hardening_readiness_check.py",
    "scripts/pas_security_02_rate_limit_scanner_readiness_check.py",
    "scripts/pas_security_03_admin_webhook_ci_readiness_check.py",
    "scripts/pas_security_04_operator_reveal_https_readiness_check.py",
)


MEMORY_REVIEW_FILES = (
    "app/services/memory/review.py",
    "app/services/memory/review_stats.py",
    "app/services/memory/review_export.py",
    "app/services/memory/review_actors.py",
    "app/services/memory/review_alerts.py",
    "app/services/memory/operator_console.py",
)


DOC_REQUIRED_CLAUSES = (
    ("docs/pas191_slack_natural_language_commands.md", (
        ("purpose",                       ("purpose",)),
        ("relationship-to-pas190",        ("relationship to pas190",)),
        ("deterministic-mapping-doctrine",("deterministic mapping doctrine",)),
        ("closed-intent-set-doctrine",    ("closed intent set doctrine",)),
        ("no-llm-doctrine",               ("no llm doctrine",)),
        ("no-mutation-via-nl-doctrine",   ("no mutation via natural language",)),
        ("pii-redaction-doctrine",        ("pii redaction doctrine",)),
        ("fail-closed-on-unknown",        ("fail-closed on unknown intent",)),
        ("operator-help-doctrine",        ("operator help doctrine",)),
        ("alias-table-curation-doctrine", ("alias table curation doctrine",)),
        ("intentionally-does-not-build",  ("intentionally does not build",)),
        ("no-autonomous-remediation",     ("no autonomous remediation",)),
        ("no-gmail",                      ("no gmail",)),
        ("composio",                      ("composio",)),
        ("remaining-limitations",         ("remaining limitations",)),
    )),
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
)


SERVICE_FILES = (
    "app/services/slack/operator_intents.py",
    "app/services/slack/operator_responses.py",
    "app/routes/slack_command.py",
)


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


# Forbidden in operator_intents.py AND operator_responses.py only —
# these surfaces must be pure-data / pure-function. The route file
# (slack_command.py) legitimately imports the LLM provider for the
# FALLBACK path, so it is excluded from this stricter scan.
FORBIDDEN_LLM_IMPORTS = (
    "from app.services.llm",
    "import app.services.llm",
    "from anthropic",
    "import anthropic",
)

PURE_SERVICE_FILES = (
    "app/services/slack/operator_intents.py",
    "app/services/slack/operator_responses.py",
)


# Mapper module invariants.
INTENTS_FILE = "app/services/slack/operator_intents.py"
INTENTS_REQUIRED_TOKENS = (
    "INTENT_STATS",
    "INTENT_CALLS_TODAY",
    "INTENT_CALLS_WEEK",
    "INTENT_RESPONSE_RATE",
    "INTENT_BOOKINGS_TODAY",
    "INTENT_CALLBACKS_DUE",
    "INTENT_QUEUE",
    "INTENT_INCIDENTS",
    "INTENT_POLICY",
    "INTENT_HEALTH",
    "INTENT_PAUSED_STATUS",
    "INTENT_HELP",
    "INTENT_LEADS_TODAY",
    "INTENT_UNKNOWN",
    "def match_intent",
    "def list_supported_intents",
    "def alias_count",
    "MUTATION_COMMAND_TOKENS",
    "_ALIAS_TABLE",
)
INTENTS_FORBIDDEN_TOKENS = (
    "eval(",
    "exec(",
    "subprocess.",
    "os.system(",
    "compile(",
    "re.compile(",
    "while True:",
    "asyncio.create_task(",
    "threading.Thread(",
    "threading.Timer(",
)


# Response-formatter module invariants.
RESPONSES_FILE = "app/services/slack/operator_responses.py"
RESPONSES_REQUIRED_TOKENS = (
    "def format_stats",
    "def format_calls_today",
    "def format_calls_week",
    "def format_response_rate",
    "def format_bookings_today",
    "def format_callbacks_due",
    "def format_queue",
    "def format_incidents",
    "def format_policy",
    "def format_health",
    "def format_paused_status",
    "def format_help",
    "def format_unknown",
    "def format_error",
    "def format_leads_today",
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


# Route wire-through invariants.
ROUTE_FILE = "app/routes/slack_command.py"
ROUTE_REQUIRED_TOKENS = (
    "from app.services.slack.operator_intents import",
    "from app.services.slack import operator_responses as pas191_responses",
    "match_intent(text)",
    "_pas191_dispatch",
    "slack.intent.matched",
    "INTENT_UNKNOWN",
    # Preserved security invariants:
    "_verify_slack_signature",
    "signing_secret",
    # PAS-SECURITY-02 rate-limit invariant preserved:
    "check_rate_limit",
)
ROUTE_FORBIDDEN_TOKENS = (
    # No new mutation hooks via match_intent path. Pause / resume
    # remain on the existing LLM-then-action branch.
    "match_intent(text).get(\"action\")",
    # No raw operator text echoed back to the LLM via PAS191 path.
    "logger.info(f\"slack pas191 raw text",
)


# Event-contract invariants.
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


# ──────────────────────────────────────────────────────────────────
# Checks
# ──────────────────────────────────────────────────────────────────

def check_pas191_files_present(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for p in PAS191_FILES:
        ok = (Path(repo_root) / p).is_file()
        out.append(_check(
            f"file:{p}",
            "PASS" if ok else "FAIL",
            f"Required PAS191 artefact present: {p}",
            detail="" if ok else "missing",
        ))
    return out


def check_prior_phases_intact(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for p in PRIOR_PHASE_FILES:
        ok = (Path(repo_root) / p).is_file()
        out.append(_check(
            f"prior_phase:{p}",
            "PASS" if ok else "FAIL",
            f"Prior-phase readiness script intact: {p}",
            detail="" if ok else "missing — PAS191 must not delete",
        ))
    return out


def check_memory_review_intact(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for p in MEMORY_REVIEW_FILES:
        ok = (Path(repo_root) / p).is_file()
        out.append(_check(
            f"memory_review:{p}",
            "PASS" if ok else "FAIL",
            f"Memory Review file present: {p}",
            detail="" if ok else "Memory Review file deleted — PAS191 must not touch",
        ))
    return out


def check_worker_off_by_default(repo_root: str) -> List[dict]:
    p = Path(repo_root) / "app" / "services" / "ingestion" / "worker.py"
    src = _read_text(p) or ""
    ok = (
        '_ENV_FLAG_ENABLED_LITERAL = "true"' in src
        or "_ENV_FLAG_ENABLED_LITERAL = 'true'" in src
    )
    return [_check(
        "worker:off_by_default",
        "PASS" if ok else "FAIL",
        "Pending-call worker is OFF by default",
        detail="" if ok else "missing strict enable-literal constant",
    )]


def check_doc_required_clauses(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for relpath, clauses in DOC_REQUIRED_CLAUSES:
        fp = Path(repo_root) / relpath
        src = _read_text(fp) or ""
        lower = src.lower()
        for name, phrases in clauses:
            present = any(p in lower for p in phrases)
            out.append(_check(
                f"doc:{relpath}:clause:{name}",
                "PASS" if present else "FAIL",
                f"{relpath} carries clause: {name}",
                detail="" if present else f"missing any of: {', '.join(phrases)}",
            ))
    return out


def check_doc_no_forbidden_scope(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for relpath, _ in DOC_REQUIRED_CLAUSES:
        fp = Path(repo_root) / relpath
        src = (_read_text(fp) or "").lower()
        bad: List[str] = [t for t in FORBIDDEN_DOC_TOKENS if t in src]
        out.append(_check(
            f"doc_scope:{relpath}",
            "FAIL" if bad else "PASS",
            f"{relpath} introduces no out-of-scope feature token",
            detail=("disqualifying: " + ", ".join(bad)) if bad else "",
        ))
    return out


def check_service_no_forbidden_imports(repo_root: str) -> List[dict]:
    out: List[dict] = []
    for relpath in SERVICE_FILES:
        fp = Path(repo_root) / relpath
        src = _read_text(fp) or ""
        executable = _strip_python_comments_and_strings(src)
        bad: List[str] = []
        for line in executable.splitlines():
            stripped = line.strip()
            for pref in FORBIDDEN_IMPORT_PREFIXES:
                if stripped.startswith(pref):
                    bad.append(pref)
                    break
        out.append(_check(
            f"service_imports:{relpath}",
            "FAIL" if bad else "PASS",
            f"{relpath} contains no forbidden import",
            detail=("disqualifying: " + ", ".join(bad)) if bad else "",
        ))
    return out


def check_pure_services_no_llm(repo_root: str) -> List[dict]:
    """operator_intents.py / operator_responses.py must NOT import LLM."""
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
        out.append(_check(
            f"pure_no_llm:{relpath}",
            "FAIL" if bad else "PASS",
            f"{relpath} does NOT import any LLM provider",
            detail=("disqualifying: " + ", ".join(bad)) if bad else "",
        ))
    return out


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
    executable = _strip_python_comments_and_strings(src)
    bad = [t for t in INTENTS_FORBIDDEN_TOKENS if t in executable]
    out.append(_check(
        "intents:no_unsafe_constructs",
        "FAIL" if bad else "PASS",
        "operator_intents.py contains no eval/exec/regex/threading/autonomous patterns",
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
    bad = [t for t in ROUTE_FORBIDDEN_TOKENS if t in src]
    out.append(_check(
        "route:no_unsafe_wirethrough",
        "FAIL" if bad else "PASS",
        "slack_command.py PAS191 wire-through does not bind mutations or echo raw text",
        detail=("disqualifying: " + ", ".join(bad)) if bad else "",
    ))
    # Fast-path ordering: PAS191 match_intent(text) call must
    # appear BEFORE the existing LLM call _parse_intent(text).
    fast_idx = src.find("match_intent(text)")
    llm_idx = src.find("_parse_intent(text)")
    ordered_ok = fast_idx > 0 and llm_idx > 0 and fast_idx < llm_idx
    out.append(_check(
        "route:fast_path_before_llm",
        "PASS" if ordered_ok else "FAIL",
        "PAS191 deterministic fast-path fires BEFORE LLM intent parser",
        detail="" if ordered_ok else (
            f"ordering wrong (fast_idx={fast_idx}, llm_idx={llm_idx})"
        ),
    ))
    return out


def check_event_contract_has_pas191_types(repo_root: str) -> List[dict]:
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
        "PAS191 readiness checker never reads .env / touches DB / hits network",
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
    checks.extend(check_pas191_files_present(repo_root))
    checks.extend(check_prior_phases_intact(repo_root))
    checks.extend(check_memory_review_intact(repo_root))
    checks.extend(check_worker_off_by_default(repo_root))
    checks.extend(check_doc_required_clauses(repo_root))
    checks.extend(check_doc_no_forbidden_scope(repo_root))
    checks.extend(check_service_no_forbidden_imports(repo_root))
    checks.extend(check_pure_services_no_llm(repo_root))
    checks.extend(check_intents_module(repo_root))
    checks.extend(check_responses_module(repo_root))
    checks.extend(check_route_wirethrough(repo_root))
    checks.extend(check_event_contract_has_pas191_types(repo_root))
    checks.extend(check_self_no_env_or_db(repo_root))

    agg = _aggregate(checks)
    return {
        "phase":            "PAS191",
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


REPORT_FILENAME = "pas191_slack_nl_command_readiness_report.json"


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="pas191_slack_nl_command_readiness_check",
        description=(
            "PAS191 — Bounded Slack natural-language operator "
            "commands readiness gate. Read-only — never reads "
            ".env, never touches Supabase, never executes a "
            "deploy / migration."
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
        f"[PAS191] verdict={report['verdict']} "
        f"blockers={report['blocker_count']} "
        f"info={report['info_count']} "
        f"checks={report['check_count']} "
        f"pass={report['pass_count']} "
        f"fail={report['fail_count']}"
    )
    actions = report.get("operator_actions") or []
    if actions:
        print("[PAS191] operator actions:")
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
