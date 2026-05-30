"""
PAS209 — Bounded action-proposal package readiness gate.

Deterministic, read-only evaluator confirming PAS209 is wired
correctly:

  * PAS209 files exist (module / CLI / tests / readiness / doc).
  * The module exposes the documented public surface
    (ActionProposal, ActionProposalPackage, build_proposal,
    build_proposal_package, closed vocabularies).
  * Module has no mutation calls (insert/update/delete/upsert/rpc).
  * Module has no execute/dispatch/send_real/auto_apply identifiers.
  * Module has no Twilio / Slack outbound / openai / anthropic /
    smtplib / apscheduler / celery / supabase imports (asserted
    via AST walk).
  * Closed vocabularies are present and sized correctly:
      ALLOWED_CHANNELS == ('MANUAL_ONLY',)
      _PROPOSAL_TEMPLATES has one entry per PAS208 action type
      Every emitted proposal carries required_human_review=True,
      allowed_channel='MANUAL_ONLY', live_behavior_changed=False
      (runtime sanity probe).
  * CLI defaults are safe — no scheduler, no live network.
  * No PAS209 SQL migration committed.
  * combined_supabase_migration.sql not present.
  * No secret-shaped tokens in any PAS209 file.
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


PAS209_FILES: Tuple[str, ...] = (
    "app/services/proactive/action_proposals.py",
    "scripts/pas209_run_action_proposals_demo.py",
    "scripts/pas209_action_proposals_readiness_check.py",
    "tests/mvp/test_pas209_action_proposals.py",
    "docs/pas209_action_proposals.md",
)


MODULE_REL_PATH = "app/services/proactive/action_proposals.py"
CLI_REL_PATH    = "scripts/pas209_run_action_proposals_demo.py"
DOC_REL_PATH    = "docs/pas209_action_proposals.md"


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
    "ALLOWED_CHANNEL_MANUAL_ONLY",
    "ALLOWED_CHANNELS",
    "ActionProposal",
    "ActionProposalPackage",
    "build_proposal",
    "build_proposal_package",
    "to_machine_json",
    "to_broker_report",
)


REQUIRED_DOC_CLAUSES: Tuple[str, ...] = (
    "PAS209",
    "manual",
    "read-only",
    "proposal",
    "rollback",
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
    return [
        Check(
            name=f"file exists: {rel}",
            passed=(repo_root / rel).is_file(),
            detail="" if (repo_root / rel).is_file() else "missing",
        )
        for rel in PAS209_FILES
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


def check_closed_vocabulary_invariants(repo_root: Path) -> List[Check]:
    out: List[Check] = []
    try:
        sys.path.insert(0, str(repo_root))
        from app.services.proactive.action_proposals import (
            ALLOWED_CHANNELS,
            ALLOWED_CHANNEL_MANUAL_ONLY,
            _PROPOSAL_TEMPLATES,
        )
        from app.services.proactive.recommendations import (
            RECOMMENDED_ACTION_TYPES,
        )
    except Exception as e:
        return [Check("can import PAS209 module", False, str(e))]

    out.append(Check(
        name="ALLOWED_CHANNELS == ('MANUAL_ONLY',)",
        passed=(ALLOWED_CHANNELS == (ALLOWED_CHANNEL_MANUAL_ONLY,)),
        detail=f"found {ALLOWED_CHANNELS!r}",
    ))
    out.append(Check(
        name="ALLOWED_CHANNEL_MANUAL_ONLY == 'MANUAL_ONLY'",
        passed=(ALLOWED_CHANNEL_MANUAL_ONLY == "MANUAL_ONLY"),
        detail="",
    ))
    out.append(Check(
        name="every PAS208 action_type has a PAS209 template",
        passed=all(a in _PROPOSAL_TEMPLATES for a in RECOMMENDED_ACTION_TYPES),
        detail="",
    ))
    out.append(Check(
        name="PAS209 templates do not exceed PAS208 vocabulary",
        passed=set(_PROPOSAL_TEMPLATES).issubset(set(RECOMMENDED_ACTION_TYPES)),
        detail="",
    ))
    # Each template must have non-empty draft + at least one safety
    # and one rollback note.
    structural_ok = all(
        isinstance(t, tuple) and len(t) == 3
        and isinstance(t[0], str) and t[0].strip()
        and isinstance(t[1], tuple) and len(t[1]) >= 1
        and isinstance(t[2], tuple) and len(t[2]) >= 1
        for t in _PROPOSAL_TEMPLATES.values()
    )
    out.append(Check(
        name="every PAS209 template has draft + safety + rollback",
        passed=structural_ok,
        detail="",
    ))
    return out


def check_runtime_invariants(repo_root: Path) -> List[Check]:
    """Runtime sanity probe — actually build a package and assert
    every proposal carries the hard invariants.
    """
    out: List[Check] = []
    try:
        sys.path.insert(0, str(repo_root))
        from app.services.proactive.action_proposals import (
            ALLOWED_CHANNEL_MANUAL_ONLY,
            build_proposal_package,
        )
        from app.services.proactive.observer import observe
        from app.services.proactive.recommendations import (
            APPROVAL_APPROVED_FOR_MANUAL_REVIEW,
            RecommendationDigest,
            apply_decision,
            build_recommendations,
        )
        from app.services.slack.proactive_digest_intent import build_demo_snapshot
        snap = build_demo_snapshot()
        digest = observe(snap)
        rd = build_recommendations(digest)
        # Approve the first three so PAS209 has something to package.
        new_recs = list(rd.recommendations)
        for i in range(min(3, len(new_recs))):
            new_recs[i] = apply_decision(
                new_recs[i], APPROVAL_APPROVED_FOR_MANUAL_REVIEW,
                operator_ref="readiness-probe",
            )
        rd2 = RecommendationDigest(
            digest_id=rd.digest_id, generated_at=rd.generated_at,
            source_digest_id=rd.source_digest_id, observed_at=rd.observed_at,
            phase=rd.phase, allowed_environment=rd.allowed_environment,
            live_behavior_changed=rd.live_behavior_changed,
            recommendations=tuple(new_recs),
            counts_by_status=rd.counts_by_status,
            counts_by_action_type=rd.counts_by_action_type,
        )
        pkg = build_proposal_package(rd2)
    except Exception as e:
        return [Check("runtime probe builds proposal package", False, str(e))]

    out.append(Check(
        name="package phase=PAS209",
        passed=(pkg.phase == "PAS209"),
        detail=f"found {pkg.phase!r}",
    ))
    out.append(Check(
        name="package live_behavior_changed=False",
        passed=(pkg.live_behavior_changed is False),
        detail="",
    ))
    out.append(Check(
        name="all proposals required_human_review=True",
        passed=all(p.required_human_review is True for p in pkg.proposals),
        detail="",
    ))
    out.append(Check(
        name="all proposals allowed_channel=MANUAL_ONLY",
        passed=all(p.allowed_channel == ALLOWED_CHANNEL_MANUAL_ONLY for p in pkg.proposals),
        detail="",
    ))
    out.append(Check(
        name="all proposals live_behavior_changed=False",
        passed=all(p.live_behavior_changed is False for p in pkg.proposals),
        detail="",
    ))
    out.append(Check(
        name="every proposal has non-empty safety_notes",
        passed=all(len(p.safety_notes) >= 1 for p in pkg.proposals),
        detail="",
    ))
    out.append(Check(
        name="every proposal has non-empty rollback_notes",
        passed=all(len(p.rollback_notes) >= 1 for p in pkg.proposals),
        detail="",
    ))
    return out


def check_no_new_migration(repo_root: Path) -> List[Check]:
    migrations_dir = repo_root / "migrations"
    return [
        Check(
            name="no PAS209 SQL migration files committed",
            passed=not (migrations_dir.exists() and any(
                p.name.lower().startswith("pas209") for p in migrations_dir.iterdir()
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
    for rel in PAS209_FILES:
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
    db_mutation_re = re.compile(
        r"\.table\([^)]*\)\.(insert|update|delete|upsert|rpc)\("
    )
    db_mutation_hit = db_mutation_re.search(src)
    return [
        Check(
            name="CLI imports build_proposal_package",
            passed=("build_proposal_package" in src),
            detail="CLI must invoke PAS209 module",
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
    checks.extend(check_closed_vocabulary_invariants(repo_root))
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
        "phase":        "PAS209",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "repo_root":    str(repo_root),
        "verdict":      verdict,
        "passed":       passed,
        "total":        total,
        "checks":       [c.to_dict() for c in checks],
    }


def _parse_args(argv: List[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="PAS209 — Readiness gate for bounded action proposals.",
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
        print(f"PAS209 readiness: {report['verdict']} ({report['passed']}/{report['total']} passed)")
        return 0 if report["verdict"] == VERDICT_READY else 1

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0 if report["verdict"] == VERDICT_READY else 1

    print(f"PAS209 readiness: {report['verdict']} ({report['passed']}/{report['total']} passed)")
    for c in checks:
        flag = "PASS" if c.passed else "FAIL"
        suffix = f" — {c.detail}" if c.detail and not c.passed else ""
        print(f"  [{flag}] {c.name}{suffix}")
    return 0 if report["verdict"] == VERDICT_READY else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
