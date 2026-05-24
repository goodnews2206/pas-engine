"""
PAS208 — Proactive recommendations readiness gate.

Deterministic, read-only evaluator confirming PAS208 is wired
correctly:

  * PAS208 files exist (module / CLI / tests / readiness / doc).
  * The recommendations module exposes the documented public
    surface (Recommendation, RecommendationDigest,
    build_recommendations, apply_decision, closed vocabularies).
  * Module has no mutation calls (insert/update/delete/upsert/rpc).
  * Module has no execute/dispatch/send_real/auto_apply identifiers.
  * Module has no Twilio / Slack outbound / openai / anthropic /
    smtplib / apscheduler / celery / supabase imports.
  * Closed vocabularies are present and sized correctly:
      RECOMMENDED_ACTION_TYPES has 10 entries
      APPROVAL_STATES has 4 entries
      SIGNAL_TO_ACTION_TYPE covers every PAS205 signal type
  * Every emitted Recommendation has live_behavior_changed=False
    and operator_required=True (asserted textually and via runtime
    sanity probe).
  * CLI defaults are safe — no live DB, no scheduler.
  * No PAS208 SQL migration committed.
  * combined_supabase_migration.sql not present.
  * No secret-shaped tokens in any PAS208 file.
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
from typing import Iterable, List, Optional, Tuple


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


_REPO_ROOT_DEFAULT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


VERDICT_READY     = "READY"
VERDICT_NOT_READY = "NOT_READY"


PAS208_FILES: Tuple[str, ...] = (
    "app/services/proactive/recommendations.py",
    "scripts/pas208_run_proactive_recommendations_demo.py",
    "scripts/pas208_proactive_recommendations_readiness_check.py",
    "tests/mvp/test_pas208_proactive_recommendations.py",
    "docs/pas208_proactive_recommendations.md",
)


MODULE_REL_PATH = "app/services/proactive/recommendations.py"
CLI_REL_PATH    = "scripts/pas208_run_proactive_recommendations_demo.py"
DOC_REL_PATH    = "docs/pas208_proactive_recommendations.md"


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
    "supabase",
)


FORBIDDEN_EXECUTOR_TOKENS: Tuple[str, ...] = (
    "def execute",
    "def dispatch",
    "def send_real_",
    "def auto_apply",
    "def auto_promote",
    "def post_to_slack",
    "def route_lead_live",
)


FORBIDDEN_OUTBOUND_TOKENS: Tuple[str, ...] = (
    "send_slack_message",
    "twilio_client",
    "requests.post",
    "httpx.post",
    "send_sms",
    "send_email",
    "combined_supabase_migration",
    "schedule_job",
    "worker.start",
)


REQUIRED_PUBLIC_SYMBOLS: Tuple[str, ...] = (
    "RECOMMENDED_ACTION_TYPES",
    "APPROVAL_STATES",
    "TERMINAL_APPROVAL_STATES",
    "SIGNAL_TO_ACTION_TYPE",
    "Recommendation",
    "RecommendationDigest",
    "build_recommendation",
    "build_recommendations",
    "apply_decision",
    "to_machine_json",
    "to_broker_report",
)


REQUIRED_DOC_CLAUSES: Tuple[str, ...] = (
    "PAS208",
    "operator",
    "approval",
    "read-only",
    "candidate",
)


SECRET_SHAPED_PATTERNS: Tuple[str, ...] = (
    r"\bAKIA[0-9A-Z]{16}\b",
    r"\bsk_live_[A-Za-z0-9]{16,}\b",
    r"\bSG\.[A-Za-z0-9_\-]{16,}\.[A-Za-z0-9_\-]{16,}\b",
    r"\bAC[0-9a-f]{32}\b",
    r"\bSK[0-9a-f]{32}\b",
)


EXPECTED_ACTION_TYPE_COUNT = 10
EXPECTED_APPROVAL_STATE_COUNT = 4


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
    return [
        Check(
            name=f"file exists: {rel}",
            passed=(repo_root / rel).is_file(),
            detail="" if (repo_root / rel).is_file() else "missing",
        )
        for rel in PAS208_FILES
    ]


def check_module_public_surface(repo_root: Path) -> List[Check]:
    src = _read(repo_root / MODULE_REL_PATH)
    return [
        Check(f"module exposes {sym}", sym in src, "missing symbol")
        for sym in REQUIRED_PUBLIC_SYMBOLS
    ]


def check_module_has_no_mutation(repo_root: Path) -> List[Check]:
    src = _read(repo_root / MODULE_REL_PATH)
    return [
        Check(
            name=f"module has no '{token}' call",
            passed=(token not in src),
            detail="" if token not in src else f"found '{token}'",
        )
        for token in FORBIDDEN_MUTATION_TOKENS
    ]


def check_module_has_no_executor_identifiers(repo_root: Path) -> List[Check]:
    src = _read(repo_root / MODULE_REL_PATH)
    return [
        Check(
            name=f"module has no executor identifier '{token}'",
            passed=(token not in src),
            detail="" if token not in src else f"found '{token}'",
        )
        for token in FORBIDDEN_EXECUTOR_TOKENS
    ]


def check_module_has_no_forbidden_imports(repo_root: Path) -> List[Check]:
    src = _read(repo_root / MODULE_REL_PATH)
    if not src:
        return [Check("module source readable", False, "could not read")]
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        return [Check("module parses", False, str(e))]

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

    return [
        Check(
            name=f"module does not import '{module}'",
            passed=module not in found,
            detail="" if module not in found else f"module imports {module}",
        )
        for module in FORBIDDEN_IMPORT_MODULES
    ]


def check_module_has_no_outbound_tokens(repo_root: Path) -> List[Check]:
    src = _read(repo_root / MODULE_REL_PATH)
    return [
        Check(
            name=f"module has no outbound token '{token}'",
            passed=(token not in src),
            detail="" if token not in src else f"module mentions '{token}'",
        )
        for token in FORBIDDEN_OUTBOUND_TOKENS
    ]


def check_closed_vocabulary_sizes(repo_root: Path) -> List[Check]:
    """Vocabulary sizes must match the spec, verified by importing
    the module rather than parsing source — that way drift in any
    direction (over OR under count) is caught with one assertion.
    """
    out: List[Check] = []
    try:
        # Force module reload-friendly import.
        sys.path.insert(0, str(repo_root))
        from app.services.proactive.recommendations import (
            APPROVAL_STATES,
            RECOMMENDED_ACTION_TYPES,
            SIGNAL_TO_ACTION_TYPE,
        )
        from app.services.proactive.observer_models import SIGNAL_TYPES
    except Exception as e:
        return [Check("can import PAS208 module", False, str(e))]

    out.append(Check(
        name=f"RECOMMENDED_ACTION_TYPES has exactly {EXPECTED_ACTION_TYPE_COUNT} entries",
        passed=(len(RECOMMENDED_ACTION_TYPES) == EXPECTED_ACTION_TYPE_COUNT),
        detail=f"found {len(RECOMMENDED_ACTION_TYPES)}",
    ))
    out.append(Check(
        name="RECOMMENDED_ACTION_TYPES has no duplicates",
        passed=(len(RECOMMENDED_ACTION_TYPES) == len(set(RECOMMENDED_ACTION_TYPES))),
        detail="",
    ))
    out.append(Check(
        name=f"APPROVAL_STATES has exactly {EXPECTED_APPROVAL_STATE_COUNT} entries",
        passed=(len(APPROVAL_STATES) == EXPECTED_APPROVAL_STATE_COUNT),
        detail=f"found {len(APPROVAL_STATES)}",
    ))
    out.append(Check(
        name="every PAS205 signal_type has a SIGNAL_TO_ACTION_TYPE entry",
        passed=all(s in SIGNAL_TO_ACTION_TYPE for s in SIGNAL_TYPES),
        detail="",
    ))
    out.append(Check(
        name="every mapped action_type is in RECOMMENDED_ACTION_TYPES",
        passed=all(a in RECOMMENDED_ACTION_TYPES for a in SIGNAL_TO_ACTION_TYPE.values()),
        detail="",
    ))
    return out


def check_runtime_invariants(repo_root: Path) -> List[Check]:
    """Runtime sanity probe — actually call the builder and assert
    every emitted Recommendation carries live_behavior_changed=False
    and operator_required=True.
    """
    out: List[Check] = []
    try:
        sys.path.insert(0, str(repo_root))
        from app.services.proactive.observer import observe
        from app.services.proactive.recommendations import (
            APPROVAL_CANDIDATE,
            build_recommendations,
        )
        from app.services.slack.proactive_digest_intent import build_demo_snapshot
        snap = build_demo_snapshot()
        digest = observe(snap)
        rd = build_recommendations(digest)
    except Exception as e:
        return [Check("runtime probe builds recommendations", False, str(e))]

    out.append(Check(
        name="all recommendations live_behavior_changed=False",
        passed=all(r.live_behavior_changed is False for r in rd.recommendations),
        detail="",
    ))
    out.append(Check(
        name="all recommendations operator_required=True",
        passed=all(r.operator_required is True for r in rd.recommendations),
        detail="",
    ))
    out.append(Check(
        name="all recommendations start in CANDIDATE",
        passed=all(r.approval_status == APPROVAL_CANDIDATE for r in rd.recommendations),
        detail="",
    ))
    out.append(Check(
        name="digest carries phase=PAS208",
        passed=(rd.phase == "PAS208"),
        detail=f"found {rd.phase!r}",
    ))
    out.append(Check(
        name="digest live_behavior_changed=False",
        passed=(rd.live_behavior_changed is False),
        detail="",
    ))
    return out


def check_no_new_migration(repo_root: Path) -> List[Check]:
    migrations_dir = repo_root / "migrations"
    return [
        Check(
            name="no PAS208 SQL migration files committed",
            passed=not (migrations_dir.exists() and any(
                p.name.lower().startswith("pas208") for p in migrations_dir.iterdir()
            )),
            detail="",
        ),
        Check(
            name="combined_supabase_migration.sql not present at repo root",
            passed=not (repo_root / "combined_supabase_migration.sql").exists(),
            detail="",
        ),
    ]


def check_no_secrets(repo_root: Path) -> List[Check]:
    out: List[Check] = []
    for rel in PAS208_FILES:
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


def check_cli_invariants(repo_root: Path) -> List[Check]:
    src = _read(repo_root / CLI_REL_PATH)

    # CLI must not contain mutation chain on supabase clients.
    db_mutation_re = re.compile(
        r"\.table\([^)]*\)\.(insert|update|delete|upsert|rpc)\("
    )
    db_mutation_hit = db_mutation_re.search(src)
    return [
        Check(
            name="CLI imports build_recommendations and apply_decision",
            passed=("build_recommendations" in src and "apply_decision" in src),
            detail="CLI must invoke PAS208 module",
        ),
        Check(
            name="CLI does not call db mutation verbs",
            passed=(db_mutation_hit is None),
            detail="" if db_mutation_hit is None else
                   f"found '{db_mutation_hit.group(0)}'",
        ),
        Check(
            name="CLI does not import scheduler/worker modules",
            passed=all(t not in src for t in (
                "import apscheduler", "from apscheduler",
                "import celery",      "from celery",
            )),
            detail="",
        ),
        Check(
            name="CLI does not call Twilio or send_slack_message",
            passed=all(t not in src for t in (
                "twilio_client", "send_slack_message",
                "send_sms",      "send_email",
            )),
            detail="",
        ),
    ]


# ──────────────────────────────────────────────────────────────────
# Runner.
# ──────────────────────────────────────────────────────────────────


def run_all_checks(repo_root: Path) -> List[Check]:
    checks: List[Check] = []
    checks.extend(check_files_exist(repo_root))
    checks.extend(check_module_public_surface(repo_root))
    checks.extend(check_module_has_no_mutation(repo_root))
    checks.extend(check_module_has_no_executor_identifiers(repo_root))
    checks.extend(check_module_has_no_forbidden_imports(repo_root))
    checks.extend(check_module_has_no_outbound_tokens(repo_root))
    checks.extend(check_closed_vocabulary_sizes(repo_root))
    checks.extend(check_runtime_invariants(repo_root))
    checks.extend(check_no_new_migration(repo_root))
    checks.extend(check_no_secrets(repo_root))
    checks.extend(check_doc_clauses(repo_root))
    checks.extend(check_cli_invariants(repo_root))
    return checks


def render_report(checks: List[Check], repo_root: Path) -> dict:
    passed = sum(1 for c in checks if c.passed)
    total = len(checks)
    verdict = VERDICT_READY if passed == total else VERDICT_NOT_READY
    return {
        "phase":        "PAS208",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "repo_root":    str(repo_root),
        "verdict":      verdict,
        "passed":       passed,
        "total":        total,
        "checks":       [c.to_dict() for c in checks],
    }


def _parse_args(argv: List[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="PAS208 — Readiness gate for operator-approval recommendations.",
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
        print(f"PAS208 readiness: {report['verdict']} ({report['passed']}/{report['total']} passed)")
        return 0 if report["verdict"] == VERDICT_READY else 1

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0 if report["verdict"] == VERDICT_READY else 1

    print(f"PAS208 readiness: {report['verdict']} ({report['passed']}/{report['total']} passed)")
    for c in checks:
        flag = "PASS" if c.passed else "FAIL"
        suffix = f" — {c.detail}" if c.detail and not c.passed else ""
        print(f"  [{flag}] {c.name}{suffix}")
    return 0 if report["verdict"] == VERDICT_READY else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
