"""
PAS206 — Read-only Supabase snapshot adapter readiness gate.

Deterministic, read-only evaluator confirming PAS206 is wired
correctly:

  * All PAS206 files exist (adapter / CLI / tests / readiness / doc).
  * Adapter source has no mutation methods (insert/update/delete/upsert/rpc).
  * Adapter source has no Twilio / Slack outbound / scheduler / worker imports.
  * Adapter declares the read_only=True invariant.
  * Adapter handles missing tables safely (try/except + STATUS_UNAVAILABLE).
  * Adapter exposes load_snapshot() and SupabaseSnapshotResult.
  * CLI defaults to stub mode and refuses --live without explicit
    operator acknowledgement.
  * No PAS206 SQL migration committed.
  * combined_supabase_migration.sql is not touched.
  * No secret-shaped tokens in any PAS206 file.
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
from typing import Iterable, List, Optional, Tuple


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


_REPO_ROOT_DEFAULT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


VERDICT_READY     = "READY"
VERDICT_NOT_READY = "NOT_READY"


PAS206_FILES: Tuple[str, ...] = (
    "app/services/proactive/supabase_snapshot_adapter.py",
    "scripts/pas206_run_observer_from_supabase_snapshot.py",
    "scripts/pas206_supabase_snapshot_readiness_check.py",
    "tests/mvp/test_pas206_supabase_snapshot_adapter.py",
    "docs/pas206_supabase_snapshot_adapter.md",
)


ADAPTER_REL_PATH = "app/services/proactive/supabase_snapshot_adapter.py"
CLI_REL_PATH     = "scripts/pas206_run_observer_from_supabase_snapshot.py"
DOC_REL_PATH     = "docs/pas206_supabase_snapshot_adapter.md"


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


FORBIDDEN_TOKENS_IN_ADAPTER: Tuple[str, ...] = (
    "combined_supabase_migration",
    "auto_apply",
    "send_real_",
    "deploy_",
    "schedule_job",
    "worker.start",
)


REQUIRED_DOC_CLAUSES: Tuple[str, ...] = (
    "PAS206",
    "read-only",
    "Supabase",
    "snapshot",
)


SECRET_SHAPED_PATTERNS: Tuple[str, ...] = (
    r"\bAKIA[0-9A-Z]{16}\b",                       # AWS access key
    r"\bsk_live_[A-Za-z0-9]{16,}\b",               # Stripe live key
    r"\bSG\.[A-Za-z0-9_\-]{16,}\.[A-Za-z0-9_\-]{16,}\b",  # SendGrid
    r"\bAC[0-9a-f]{32}\b",                         # Twilio Account SID
    r"\bSK[0-9a-f]{32}\b",                         # Twilio API SID
)


# ──────────────────────────────────────────────────────────────────
# Result builders.
# ──────────────────────────────────────────────────────────────────


class Check:
    __slots__ = ("name", "passed", "detail")

    def __init__(self, name: str, passed: bool, detail: str = "") -> None:
        self.name = name
        self.passed = passed
        self.detail = detail

    def to_dict(self) -> dict:
        return {"name": self.name, "passed": self.passed, "detail": self.detail}


# ──────────────────────────────────────────────────────────────────
# Individual checks.
# ──────────────────────────────────────────────────────────────────


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def check_files_exist(repo_root: Path) -> List[Check]:
    out: List[Check] = []
    for rel in PAS206_FILES:
        p = repo_root / rel
        out.append(Check(
            name=f"file exists: {rel}",
            passed=p.is_file(),
            detail="" if p.is_file() else "missing",
        ))
    return out


def check_adapter_has_no_mutation_methods(repo_root: Path) -> List[Check]:
    src = _read_text(repo_root / ADAPTER_REL_PATH)
    out: List[Check] = []
    for token in FORBIDDEN_MUTATION_TOKENS:
        out.append(Check(
            name=f"adapter has no '{token}' call",
            passed=(token not in src),
            detail="" if token not in src else f"found '{token}' in adapter source",
        ))
    return out


def check_adapter_has_no_forbidden_imports(repo_root: Path) -> List[Check]:
    src = _read_text(repo_root / ADAPTER_REL_PATH)
    out: List[Check] = []
    if not src:
        out.append(Check("adapter source readable", False, "could not read adapter file"))
        return out
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        out.append(Check("adapter parses", False, str(e)))
        return out

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
            name=f"adapter does not import '{module}'",
            passed=module not in found,
            detail="" if module not in found else f"adapter imports {module}",
        ))
    return out


def check_adapter_has_no_forbidden_tokens(repo_root: Path) -> List[Check]:
    src = _read_text(repo_root / ADAPTER_REL_PATH)
    out: List[Check] = []
    for token in FORBIDDEN_TOKENS_IN_ADAPTER:
        out.append(Check(
            name=f"adapter has no token '{token}'",
            passed=(token not in src),
            detail="" if token not in src else f"adapter mentions '{token}'",
        ))
    return out


def check_adapter_read_only_invariant(repo_root: Path) -> List[Check]:
    src = _read_text(repo_root / ADAPTER_REL_PATH)
    return [
        Check(
            name="adapter declares read_only field",
            passed=("read_only:" in src or "read_only " in src),
            detail="" if "read_only" in src else "no read_only invariant",
        ),
        Check(
            name="adapter sets read_only=True default",
            passed=("read_only:           bool = True" in src
                    or "read_only: bool = True" in src
                    or "read_only           = True" in src),
            detail="adapter must default read_only to True",
        ),
    ]


def check_adapter_safe_missing_table_handling(repo_root: Path) -> List[Check]:
    src = _read_text(repo_root / ADAPTER_REL_PATH)
    return [
        Check(
            name="adapter wraps queries in try/except",
            passed=("except Exception" in src),
            detail="adapter must broadly catch read failures",
        ),
        Check(
            name="adapter marks unavailable sources",
            passed=("STATUS_UNAVAILABLE" in src and "unavailable_sources" in src),
            detail="adapter must expose unavailable_sources",
        ),
        Check(
            name="adapter exposes source_status mapping",
            passed=("source_status" in src),
            detail="adapter must report per-source status",
        ),
    ]


def check_adapter_exposes_public_surface(repo_root: Path) -> List[Check]:
    src = _read_text(repo_root / ADAPTER_REL_PATH)
    return [
        Check("adapter defines load_snapshot",
              "def load_snapshot(" in src,
              "missing load_snapshot entry point"),
        Check("adapter defines SupabaseSnapshotResult",
              "class SupabaseSnapshotResult" in src,
              "missing result envelope class"),
        Check("adapter declares allowed sources tuple",
              "ALLOWED_SOURCES" in src,
              "missing ALLOWED_SOURCES vocabulary"),
        Check("adapter uses select-only query verbs",
              ".select(" in src,
              "adapter must call .select()"),
    ]


def _cli_has_db_mutation(src: str) -> Optional[str]:
    """Detect Supabase-style mutation calls in the CLI source.

    We scan for the supabase-py chain verbs but ignore innocuous
    Python uses of the same names (e.g. `sys.path.insert`, dict
    `.update`). Mutation calls on a real Supabase client look like
    `client.table(name).insert(...)` or `.upsert(...)` etc.
    """
    db_mutation_patterns = (
        r"\.table\([^)]*\)\.insert\(",
        r"\.table\([^)]*\)\.update\(",
        r"\.table\([^)]*\)\.delete\(",
        r"\.table\([^)]*\)\.upsert\(",
        r"\.table\([^)]*\)\.rpc\(",
        r"\.rpc\(",
        r"\.upsert\(",
    )
    for pattern in db_mutation_patterns:
        m = re.search(pattern, src)
        if m:
            return m.group(0)
    return None


def check_cli_default_is_stub(repo_root: Path) -> List[Check]:
    src = _read_text(repo_root / CLI_REL_PATH)
    cli_mutation = _cli_has_db_mutation(src)
    return [
        Check("CLI defaults to stub mode",
              "default=True" in src and "--stub" in src,
              "CLI must default to --stub"),
        Check("CLI gates --live behind explicit acknowledgement",
              "--i-understand-this-is-readonly" in src,
              "CLI must require an explicit live-read acknowledgement"),
        Check("CLI imports load_snapshot",
              "load_snapshot" in src,
              "CLI must invoke the adapter"),
        Check("CLI does not call db mutation verbs",
              cli_mutation is None,
              f"CLI contains DB mutation call '{cli_mutation}'" if cli_mutation else ""),
    ]


def check_no_new_migration(repo_root: Path) -> List[Check]:
    migrations_dir = repo_root / "migrations"
    out: List[Check] = []
    out.append(Check(
        name="no PAS206 SQL migration files committed",
        passed=not (migrations_dir.exists() and any(
            p.name.lower().startswith("pas206") for p in migrations_dir.iterdir()
        )),
        detail="",
    ))
    out.append(Check(
        name="combined_supabase_migration.sql not present at repo root",
        passed=not (repo_root / "combined_supabase_migration.sql").exists(),
        detail="",
    ))
    return out


def check_no_secrets_in_pas206_files(repo_root: Path) -> List[Check]:
    out: List[Check] = []
    for rel in PAS206_FILES:
        text = _read_text(repo_root / rel)
        if not text:
            continue
        leaks: List[str] = []
        for pattern in SECRET_SHAPED_PATTERNS:
            if re.search(pattern, text):
                leaks.append(pattern)
        out.append(Check(
            name=f"no secret-shaped tokens in {rel}",
            passed=not leaks,
            detail="" if not leaks else f"matched patterns: {leaks}",
        ))
    return out


def check_doc_clauses(repo_root: Path) -> List[Check]:
    text = _read_text(repo_root / DOC_REL_PATH)
    out: List[Check] = []
    for clause in REQUIRED_DOC_CLAUSES:
        out.append(Check(
            name=f"doc contains required clause '{clause}'",
            passed=(clause.lower() in text.lower()),
            detail="",
        ))
    return out


def check_adapter_does_not_touch_engine(repo_root: Path) -> List[Check]:
    src = _read_text(repo_root / ADAPTER_REL_PATH)
    forbidden = ("app.engine", "state_machine", "from app.services.outbound")
    out: List[Check] = []
    for token in forbidden:
        out.append(Check(
            name=f"adapter does not reference '{token}'",
            passed=(token not in src),
            detail="" if token not in src else f"adapter mentions {token}",
        ))
    return out


# ──────────────────────────────────────────────────────────────────
# Runner.
# ──────────────────────────────────────────────────────────────────


def run_all_checks(repo_root: Path) -> List[Check]:
    checks: List[Check] = []
    checks.extend(check_files_exist(repo_root))
    checks.extend(check_adapter_has_no_mutation_methods(repo_root))
    checks.extend(check_adapter_has_no_forbidden_imports(repo_root))
    checks.extend(check_adapter_has_no_forbidden_tokens(repo_root))
    checks.extend(check_adapter_read_only_invariant(repo_root))
    checks.extend(check_adapter_safe_missing_table_handling(repo_root))
    checks.extend(check_adapter_exposes_public_surface(repo_root))
    checks.extend(check_cli_default_is_stub(repo_root))
    checks.extend(check_no_new_migration(repo_root))
    checks.extend(check_no_secrets_in_pas206_files(repo_root))
    checks.extend(check_doc_clauses(repo_root))
    checks.extend(check_adapter_does_not_touch_engine(repo_root))
    return checks


def render_full_report(checks: List[Check], repo_root: Path) -> dict:
    passed = sum(1 for c in checks if c.passed)
    total = len(checks)
    verdict = VERDICT_READY if passed == total else VERDICT_NOT_READY
    return {
        "phase":           "PAS206",
        "generated_at":    datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "repo_root":       str(repo_root),
        "verdict":         verdict,
        "passed":          passed,
        "total":           total,
        "checks":          [c.to_dict() for c in checks],
    }


def _parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "PAS206 — Readiness gate for the read-only Supabase "
            "snapshot adapter."
        ),
    )
    parser.add_argument("--repo-root", type=str, default=_REPO_ROOT_DEFAULT)
    parser.add_argument("--summary-only", action="store_true",
                        help="Print a one-line verdict summary only.")
    parser.add_argument("--json", action="store_true",
                        help="Print the full report as JSON.")
    return parser.parse_args(argv)


def main(argv: List[str]) -> int:
    args = _parse_args(argv)
    repo_root = Path(args.repo_root).resolve()
    checks = run_all_checks(repo_root)
    report = render_full_report(checks, repo_root)

    if args.summary_only:
        print(f"PAS206 readiness: {report['verdict']} ({report['passed']}/{report['total']} passed)")
        return 0 if report["verdict"] == VERDICT_READY else 1

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0 if report["verdict"] == VERDICT_READY else 1

    print(f"PAS206 readiness: {report['verdict']} ({report['passed']}/{report['total']} passed)")
    for c in checks:
        flag = "PASS" if c.passed else "FAIL"
        suffix = f" — {c.detail}" if c.detail and not c.passed else ""
        print(f"  [{flag}] {c.name}{suffix}")
    return 0 if report["verdict"] == VERDICT_READY else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
