"""
PAS207 — Slack proactive needs-attention digest readiness gate.

Deterministic, read-only evaluator confirming PAS207 is wired
correctly:

  * PAS207 files exist (intent service / tests / readiness / doc).
  * The intent service exposes the documented public surface
    (INTENT_NEEDS_ATTENTION / PROACTIVE_DIGEST_ALIASES /
    try_route_needs_attention).
  * The intent service has no mutation calls (insert/update/
    delete/upsert/rpc).
  * The intent service has no Twilio, Slack outbound, openai,
    anthropic, smtplib, scheduler, or worker imports.
  * The intent service has no outbound messaging tokens
    (send_slack_message, twilio_client, requests.post, ...).
  * No PAS207 SQL migration committed.
  * combined_supabase_migration.sql is not touched.
  * No secret-shaped tokens in any PAS207 file.
  * Dispatcher imports the PAS207 router and calls
    try_route_needs_attention BEFORE the PAS191 deterministic
    dispatch branch.
  * Doc carries the required clauses.

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
from typing import List, Optional, Tuple


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


_REPO_ROOT_DEFAULT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


VERDICT_READY     = "READY"
VERDICT_NOT_READY = "NOT_READY"


PAS207_FILES: Tuple[str, ...] = (
    "app/services/slack/proactive_digest_intent.py",
    "scripts/pas207_slack_needs_attention_readiness_check.py",
    "tests/mvp/test_pas207_slack_needs_attention_digest.py",
    "docs/pas207_slack_needs_attention_digest.md",
)


INTENT_REL_PATH     = "app/services/slack/proactive_digest_intent.py"
DISPATCHER_REL_PATH = "app/routes/slack_command.py"
DOC_REL_PATH        = "docs/pas207_slack_needs_attention_digest.md"


FORBIDDEN_MUTATION_TOKENS: Tuple[str, ...] = (
    ".insert(",
    ".update(",
    ".delete(",
    ".upsert(",
    ".rpc(",
)


FORBIDDEN_IMPORT_MODULES: Tuple[str, ...] = (
    "twilio",
    "slack_sdk",
    "openai",
    "anthropic",
    "smtplib",
    "apscheduler",
    "celery",
    "schedule",
)


FORBIDDEN_OUTBOUND_TOKENS: Tuple[str, ...] = (
    "send_slack_message",
    "twilio_client",
    "requests.post",
    "httpx.post",
    "send_sms",
    "send_email",
    "combined_supabase_migration",
    "auto_apply",
    "deploy_",
    "schedule_job",
    "worker.start",
)


REQUIRED_DOC_CLAUSES: Tuple[str, ...] = (
    "PAS207",
    "needs attention",
    "read-only",
    "Slack",
)


PAS207_REQUIRED_PUBLIC_SYMBOLS: Tuple[str, ...] = (
    "INTENT_NEEDS_ATTENTION",
    "PROACTIVE_DIGEST_ALIASES",
    "match_needs_attention_intent",
    "try_route_needs_attention",
    "format_needs_attention_response",
    "build_demo_snapshot",
)


SECRET_SHAPED_PATTERNS: Tuple[str, ...] = (
    r"\bAKIA[0-9A-Z]{16}\b",
    r"\bsk_live_[A-Za-z0-9]{16,}\b",
    r"\bSG\.[A-Za-z0-9_\-]{16,}\.[A-Za-z0-9_\-]{16,}\b",
    r"\bAC[0-9a-f]{32}\b",
    r"\bSK[0-9a-f]{32}\b",
)


# ──────────────────────────────────────────────────────────────────
# Check primitive.
# ──────────────────────────────────────────────────────────────────


class Check:
    __slots__ = ("name", "passed", "detail")

    def __init__(self, name: str, passed: bool, detail: str = "") -> None:
        self.name = name
        self.passed = passed
        self.detail = detail

    def to_dict(self) -> dict:
        return {"name": self.name, "passed": self.passed, "detail": self.detail}


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


# ──────────────────────────────────────────────────────────────────
# Individual checks.
# ──────────────────────────────────────────────────────────────────


def check_files_exist(repo_root: Path) -> List[Check]:
    out: List[Check] = []
    for rel in PAS207_FILES:
        p = repo_root / rel
        out.append(Check(
            name=f"file exists: {rel}",
            passed=p.is_file(),
            detail="" if p.is_file() else "missing",
        ))
    return out


def check_intent_public_surface(repo_root: Path) -> List[Check]:
    src = _read(repo_root / INTENT_REL_PATH)
    return [
        Check(f"intent exposes {sym}", sym in src, "missing symbol")
        for sym in PAS207_REQUIRED_PUBLIC_SYMBOLS
    ]


def check_intent_no_mutation(repo_root: Path) -> List[Check]:
    src = _read(repo_root / INTENT_REL_PATH)
    return [
        Check(
            name=f"intent has no '{token}' call",
            passed=(token not in src),
            detail="" if token not in src else f"found '{token}'",
        )
        for token in FORBIDDEN_MUTATION_TOKENS
    ]


def check_intent_no_forbidden_imports(repo_root: Path) -> List[Check]:
    src = _read(repo_root / INTENT_REL_PATH)
    out: List[Check] = []
    if not src:
        return [Check("intent source readable", False, "could not read")]
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        return [Check("intent parses", False, str(e))]

    found: set = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".")[0]
                if root in FORBIDDEN_IMPORT_MODULES:
                    found.add(root)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                root = node.module.split(".")[0]
                if root in FORBIDDEN_IMPORT_MODULES:
                    found.add(root)

    for module in FORBIDDEN_IMPORT_MODULES:
        out.append(Check(
            name=f"intent does not import '{module}'",
            passed=module not in found,
            detail="" if module not in found else f"intent imports {module}",
        ))
    return out


def check_intent_no_outbound_tokens(repo_root: Path) -> List[Check]:
    src = _read(repo_root / INTENT_REL_PATH)
    return [
        Check(
            name=f"intent has no outbound token '{token}'",
            passed=(token not in src),
            detail="" if token not in src else f"intent mentions '{token}'",
        )
        for token in FORBIDDEN_OUTBOUND_TOKENS
    ]


def check_intent_alias_count(repo_root: Path) -> List[Check]:
    """The spec fixes PAS207 to exactly 8 phrases. The readiness
    gate refuses to drift that count silently.
    """
    src = _read(repo_root / INTENT_REL_PATH)
    matches = re.findall(r'"\s*[a-z][a-z \'\-]+\s*"', src)
    # Heuristic: count entries inside the PROACTIVE_DIGEST_ALIASES tuple
    # by locating the tuple literal then counting comma-separated strings.
    m = re.search(
        r"PROACTIVE_DIGEST_ALIASES[^=]*=\s*\((?P<body>[^)]*)\)", src, re.DOTALL
    )
    if not m:
        return [Check("intent declares PROACTIVE_DIGEST_ALIASES tuple", False,
                      "could not locate tuple literal")]
    body = m.group("body")
    entries = re.findall(r'"([^"]+)"', body)
    return [
        Check(
            name="intent alias tuple has exactly 8 entries",
            passed=(len(entries) == 8),
            detail=f"found {len(entries)}",
        ),
        Check(
            name="intent alias tuple has no duplicates",
            passed=(len(entries) == len(set(entries))),
            detail="",
        ),
    ]


def check_dispatcher_wiring(repo_root: Path) -> List[Check]:
    src = _read(repo_root / DISPATCHER_REL_PATH)
    pas207_call = src.find("try_route_needs_attention(text)")
    pas191_dispatch = src.find("if pas191_intent != INTENT_UNKNOWN:")
    return [
        Check(
            name="dispatcher imports try_route_needs_attention",
            passed=("from app.services.slack.proactive_digest_intent import" in src
                    and "try_route_needs_attention" in src),
            detail="dispatcher must wire PAS207",
        ),
        Check(
            name="dispatcher calls try_route_needs_attention",
            passed=(pas207_call != -1),
            detail="dispatcher must invoke PAS207 fast-path",
        ),
        Check(
            name="PAS207 fast-path sits before PAS191 deterministic dispatch",
            passed=(pas207_call != -1 and pas191_dispatch != -1
                    and pas207_call < pas191_dispatch),
            detail="PAS207 must fire before PAS191 dispatch branch",
        ),
        Check(
            name="dispatcher logs needs_attention intent match",
            passed=("needs_attention" in src and "slack_command_pas207" in src),
            detail="dispatcher must attribute the PAS207 surface",
        ),
    ]


def check_no_new_migration(repo_root: Path) -> List[Check]:
    migrations_dir = repo_root / "migrations"
    out: List[Check] = []
    out.append(Check(
        name="no PAS207 SQL migration files committed",
        passed=not (migrations_dir.exists() and any(
            p.name.lower().startswith("pas207") for p in migrations_dir.iterdir()
        )),
        detail="",
    ))
    out.append(Check(
        name="combined_supabase_migration.sql not present at repo root",
        passed=not (repo_root / "combined_supabase_migration.sql").exists(),
        detail="",
    ))
    return out


def check_no_secrets_in_pas207_files(repo_root: Path) -> List[Check]:
    out: List[Check] = []
    for rel in PAS207_FILES:
        text = _read(repo_root / rel)
        if not text:
            continue
        leaks: List[str] = []
        for pattern in SECRET_SHAPED_PATTERNS:
            if re.search(pattern, text):
                leaks.append(pattern)
        out.append(Check(
            name=f"no secret-shaped tokens in {rel}",
            passed=not leaks,
            detail="" if not leaks else f"matched: {leaks}",
        ))
    return out


def check_doc_clauses(repo_root: Path) -> List[Check]:
    text = _read(repo_root / DOC_REL_PATH)
    return [
        Check(
            name=f"doc contains required clause '{clause}'",
            passed=(clause.lower() in text.lower()),
            detail="",
        )
        for clause in REQUIRED_DOC_CLAUSES
    ]


def check_pas191_carry_forward(repo_root: Path) -> List[Check]:
    """The PAS207 alias tuple must NOT contain any PAS191
    next-action phrase.
    """
    src = _read(repo_root / INTENT_REL_PATH)
    m = re.search(
        r"PROACTIVE_DIGEST_ALIASES[^=]*=\s*\((?P<body>[^)]*)\)", src, re.DOTALL
    )
    body = m.group("body") if m else ""
    pas191_phrases = (
        "next action",
        "next actions",
        "next steps",
        "priorities",
        "top priorities",
        "what should i do now",
        "what should i do",
        "what do i do now",
        "what should i focus on",
        "show priorities",
        "what's the priority",
        "what is the priority",
    )
    leaks: List[str] = []
    for phrase in pas191_phrases:
        if f'"{phrase}"' in body:
            leaks.append(phrase)
    return [Check(
        name="PAS207 alias tuple does not absorb any PAS191 next_action phrase",
        passed=not leaks,
        detail="" if not leaks else f"PAS191 leak: {leaks}",
    )]


# ──────────────────────────────────────────────────────────────────
# Runner.
# ──────────────────────────────────────────────────────────────────


def run_all_checks(repo_root: Path) -> List[Check]:
    checks: List[Check] = []
    checks.extend(check_files_exist(repo_root))
    checks.extend(check_intent_public_surface(repo_root))
    checks.extend(check_intent_no_mutation(repo_root))
    checks.extend(check_intent_no_forbidden_imports(repo_root))
    checks.extend(check_intent_no_outbound_tokens(repo_root))
    checks.extend(check_intent_alias_count(repo_root))
    checks.extend(check_dispatcher_wiring(repo_root))
    checks.extend(check_no_new_migration(repo_root))
    checks.extend(check_no_secrets_in_pas207_files(repo_root))
    checks.extend(check_doc_clauses(repo_root))
    checks.extend(check_pas191_carry_forward(repo_root))
    return checks


def render_report(checks: List[Check], repo_root: Path) -> dict:
    passed = sum(1 for c in checks if c.passed)
    total = len(checks)
    verdict = VERDICT_READY if passed == total else VERDICT_NOT_READY
    return {
        "phase":        "PAS207",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "repo_root":    str(repo_root),
        "verdict":      verdict,
        "passed":       passed,
        "total":        total,
        "checks":       [c.to_dict() for c in checks],
    }


def _parse_args(argv: List[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="PAS207 — Readiness gate for the Slack needs-attention digest.",
    )
    p.add_argument("--repo-root", type=str, default=_REPO_ROOT_DEFAULT)
    p.add_argument("--summary-only", action="store_true")
    p.add_argument("--json", action="store_true")
    return p.parse_args(argv)


def main(argv: List[str]) -> int:
    args = _parse_args(argv)
    repo_root = Path(args.repo_root).resolve()
    checks = run_all_checks(repo_root)
    report = render_report(checks, repo_root)

    if args.summary_only:
        print(f"PAS207 readiness: {report['verdict']} ({report['passed']}/{report['total']} passed)")
        return 0 if report["verdict"] == VERDICT_READY else 1

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0 if report["verdict"] == VERDICT_READY else 1

    print(f"PAS207 readiness: {report['verdict']} ({report['passed']}/{report['total']} passed)")
    for c in checks:
        flag = "PASS" if c.passed else "FAIL"
        suffix = f" — {c.detail}" if c.detail and not c.passed else ""
        print(f"  [{flag}] {c.name}{suffix}")
    return 0 if report["verdict"] == VERDICT_READY else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
