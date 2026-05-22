"""
PAS203 — Slack read-only evidence digest command tests.

Coverage:

  * Intent matcher:
      - spec-required phrases all match
      - case / whitespace / trailing punctuation normalised
      - unrelated text does not match
      - empty text does not match
      - mutation tokens (pause/resume/push/remove) do not match
      - PAS191 INTENT_CODES tuple still has exactly 15 entries
        (carry-forward — PAS203 must not extend it)

  * Digest loader:
      - finds the lexicographically newest matching file
      - returns None on missing directory
      - returns None on directory with no matching files
      - rejects non-PAS201 digests with ValueError
      - rejects non-SIMULATION_ONLY digests
      - rejects live_behavior_changed=True digests
      - rejects malformed JSON
      - rejects digest files matching prefix but with malformed
        names (defence-in-depth)

  * Response formatter:
      - delegates to PAS202 format_digest_for_slack on a valid
        digest
      - returns the bounded fallback when digest is None
      - refuses any forbidden live-routing token in output
      - is deterministic for a fixed digest

  * Full route helper:
      - matching alias + present digest -> formatted response
      - matching alias + missing digest -> fallback
      - non-matching text -> None (dispatcher fall-through)
      - never writes anything

  * Slack-safety invariants (no PII, no production brokerage IDs,
    no live routing wording, no Slack/Twilio/Supabase imports):
      - response carries no phone-shaped tokens
      - response carries no production brokerage UUIDs
      - response carries no forbidden live-routing wording
      - module source carries no banned imports

  * Help-line additions are bounded:
      - SIMULATION_DIGEST_HELP_LINES are short, plain, and
        non-empty

  * Carry-forward:
      - PAS191/PAS192 tests still pass (smoke import)
      - PAS202 format_digest_for_slack still importable and used

  * Readiness gate:
      - exit 0 / verdict=READY
      - JSON envelope valid
"""

from __future__ import annotations

import ast
import json
import pathlib
import re
import subprocess
import sys
import tempfile

import pytest


_REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


from app.services.slack.simulation_digest_intent import (  # noqa: E402
    DIGEST_FILENAME_PREFIX,
    FORBIDDEN_OUTPUT_TOKENS,
    INTENT_SIMULATION_DIGEST,
    MISSING_DIGEST_FALLBACK_MESSAGE,
    REPORTS_SUBDIR,
    SIMULATION_DIGEST_ALIASES,
    SIMULATION_DIGEST_HELP_LINES,
    alias_count,
    find_latest_digest_path,
    format_simulation_digest_response,
    list_aliases,
    load_digest,
    match_simulation_digest_intent,
    try_route_simulation_digest,
)
from app.services.simulation.behavioral_evaluation import (  # noqa: E402
    build_behavioral_evaluation,
)
from app.services.simulation.evidence_digest import (  # noqa: E402
    build_evidence_digest,
)
from app.services.simulation.evidence_digest_surface import (  # noqa: E402
    format_digest_for_slack,
)
from app.services.simulation.manual_test_runtime import (  # noqa: E402
    execute_manual_test_runtime,
)
from app.services.simulation.runtime_inspection import (  # noqa: E402
    build_inspection,
)


def _read(relpath: str) -> str:
    return (_REPO_ROOT / relpath).read_text(encoding="utf-8")


# ──────────────────────────────────────────────────────────────────
# Fixtures
# ──────────────────────────────────────────────────────────────────

REC_ID     = "pas195-rec-9a9566a11d621684"
REVIEW_ID  = "pas196-rev-deadbeefcafebabe"
PACKAGE_ID = "pas197-pkg-2b7c50e63bf5fb88"
GEN_AT     = "2026-05-22T08:30:00Z"


def _candidate_recommendation() -> dict:
    return {
        "recommendation_id":    REC_ID,
        "status":               "CANDIDATE",
        "operator_required":    True,
        "recommended_strategy": "callback_first",
        "rejected_strategy":    "assertive",
        "recommendation_type":  "promote_strategy",
        "confidence_level":     "high",
        "pass_rate_threshold":  0.95,
        "phase":                "PAS195",
    }


def _approved_review() -> dict:
    return {
        "review_id":             REVIEW_ID,
        "recommendation_id":     REC_ID,
        "previous_status":       "CANDIDATE",
        "new_status":            "APPROVED_FOR_MANUAL_TEST",
        "live_behavior_changed": False,
        "actor_type":            "operator",
        "actor_id_token":        "op_demo0001",
        "reason_token":          "operator_approved_for_manual_test",
        "reviewed_at":           "2026-05-21T12:06:02Z",
        "operator_required":     True,
        "phase":                 "PAS196",
    }


def _ready_package() -> dict:
    return {
        "package_id":            PACKAGE_ID,
        "phase":                 "PAS197",
        "recommendation_id":     REC_ID,
        "review_id":             REVIEW_ID,
        "strategy_id":           "callback_first",
        "status":                "READY_FOR_MANUAL_TEST",
        "live_behavior_changed": False,
        "allowed_environment":   "SIMULATION_ONLY",
        "test_plan":             [],
        "success_metrics":       [],
        "rollback_notes":        [],
        "safety_notes":          [],
        "created_at":            "2026-05-21T12:22:47Z",
    }


def _build_digest() -> dict:
    rec = _candidate_recommendation()
    rev = _approved_review()
    pkg = _ready_package()
    rt = execute_manual_test_runtime(pkg, created_at="2026-05-22T04:00:00Z")
    insp = build_inspection(rec, rev, pkg, rt, generated_at=GEN_AT)
    beh = build_behavioral_evaluation(
        rt, generated_at=GEN_AT, inspection=insp,
    )
    return build_evidence_digest(
        rec, rev, pkg, rt, insp, beh, generated_at=GEN_AT,
    )


def _write_digest_file(
    tp: pathlib.Path,
    *,
    timestamp: str = "20260522T080000Z",
    digest_id_suffix: str = "1111111111111111",
    overrides: dict = None,
) -> pathlib.Path:
    digest = _build_digest()
    if overrides:
        digest.update(overrides)
    digest["digest_id"] = f"pas201-dgst-{digest_id_suffix}"
    name = (
        f"pas201_simulation_evidence_digest_{timestamp}_"
        f"{digest['digest_id']}.json"
    )
    fp = tp / name
    fp.write_text(
        json.dumps(digest, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return fp


# ──────────────────────────────────────────────────────────────────
# Intent matcher
# ──────────────────────────────────────────────────────────────────

_SPEC_REQUIRED_PHRASES = (
    "simulation digest",
    "evidence digest",
    "show simulation evidence",
    "what did the simulation prove",
    "rehearsal evidence",
    "strategy evidence",
)


@pytest.mark.parametrize("phrase", _SPEC_REQUIRED_PHRASES)
def test_spec_required_phrases_match(phrase):
    assert match_simulation_digest_intent(phrase) is True


@pytest.mark.parametrize("phrase", [
    "Simulation Digest",
    "SIMULATION DIGEST",
    "  simulation digest  ",
    "simulation digest?",
    "simulation digest.",
    "simulation digest!",
    "simulation  digest",
    "what did the simulation prove?",
    "What Did The Simulation Prove?",
])
def test_phrase_normalisation_matches(phrase):
    assert match_simulation_digest_intent(phrase) is True


@pytest.mark.parametrize("phrase", [
    "stats",
    "summary",
    "calls today",
    "what should i do now",
    "show queue",
    "completely unrelated text",
    "",
    "   ",
    "digest",  # too vague — not in alias table
    "show",
    "evidence",  # not in alias table
])
def test_unrelated_text_does_not_match(phrase):
    assert match_simulation_digest_intent(phrase) is False


@pytest.mark.parametrize("phrase", [None, 123, [], {}])
def test_non_string_input_does_not_match(phrase):
    assert match_simulation_digest_intent(phrase) is False


@pytest.mark.parametrize("phrase", [
    "pause",
    "resume",
    "push something",
    "remove something",
])
def test_mutation_tokens_do_not_match(phrase):
    # Defensive: PAS191 routes these on the exact-command branch.
    # PAS203's matcher must not capture them.
    assert match_simulation_digest_intent(phrase) is False


def test_alias_count_under_thirty_to_keep_set_bounded():
    # Sanity: keep the alias surface small. Adding new aliases is
    # a deliberate code change, not an explosion.
    assert 6 <= alias_count() <= 30


def test_alias_set_includes_every_spec_required_phrase():
    aliases = set(list_aliases())
    for phrase in _SPEC_REQUIRED_PHRASES:
        assert phrase in aliases


def test_pas191_intent_codes_still_have_exactly_fifteen_entries():
    # Carry-forward — PAS191 / PAS192 tests assert this strictly.
    # PAS203 must not extend INTENT_CODES.
    from app.services.slack.operator_intents import INTENT_CODES
    assert len(INTENT_CODES) == 15


def test_simulation_digest_intent_code_is_distinct_from_pas191_codes():
    from app.services.slack.operator_intents import INTENT_CODES
    assert INTENT_SIMULATION_DIGEST not in INTENT_CODES


# ──────────────────────────────────────────────────────────────────
# Digest loader
# ──────────────────────────────────────────────────────────────────

def test_loader_finds_lexicographically_newest_matching_file():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        _write_digest_file(tp, timestamp="20260101T000000Z",
                           digest_id_suffix="aaaaaaaaaaaaaaaa")
        _write_digest_file(tp, timestamp="20260601T000000Z",
                           digest_id_suffix="bbbbbbbbbbbbbbbb")
        _write_digest_file(tp, timestamp="20260301T000000Z",
                           digest_id_suffix="cccccccccccccccc")
        latest = find_latest_digest_path(tp)
        assert latest is not None
        assert "20260601T000000Z" in latest.name
        assert "bbbbbbbbbbbbbbbb" in latest.name


def test_loader_returns_none_on_missing_directory():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp) / "does_not_exist"
        assert find_latest_digest_path(tp) is None


def test_loader_returns_none_on_empty_directory():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        assert find_latest_digest_path(tp) is None


def test_loader_ignores_non_pas201_files():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        (tp / "not_a_digest.json").write_text("{}", encoding="utf-8")
        (tp / "pas198_manual_test_runtime_X.json").write_text("{}", encoding="utf-8")
        assert find_latest_digest_path(tp) is None


def test_loader_ignores_malformed_pas201_filenames():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        # Prefix matches but the rest is not the expected shape.
        (tp / f"{DIGEST_FILENAME_PREFIX}garbage.json").write_text(
            "{}", encoding="utf-8",
        )
        assert find_latest_digest_path(tp) is None


def test_load_digest_accepts_valid_pas201_file():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        fp = _write_digest_file(tp)
        digest = load_digest(fp)
        assert digest["phase"] == "PAS201"


def test_load_digest_rejects_non_pas201_phase():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        fp = _write_digest_file(tp, overrides={"phase": "PAS200"})
        with pytest.raises(ValueError):
            load_digest(fp)


def test_load_digest_rejects_non_simulation_only_environment():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        fp = _write_digest_file(tp,
                                overrides={"allowed_environment": "PRODUCTION"})
        with pytest.raises(ValueError):
            load_digest(fp)


def test_load_digest_rejects_live_behavior_changed_true():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        fp = _write_digest_file(tp,
                                overrides={"live_behavior_changed": True})
        with pytest.raises(ValueError):
            load_digest(fp)


def test_load_digest_rejects_malformed_json():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        fp = tp / "pas201_simulation_evidence_digest_20260101T000000Z_pas201-dgst-aaaaaaaaaaaaaaaa.json"
        fp.write_text("this is not json", encoding="utf-8")
        with pytest.raises(ValueError):
            load_digest(fp)


def test_load_digest_rejects_missing_file():
    with pytest.raises(ValueError):
        load_digest(pathlib.Path("/tmp/does_not_exist_pas203_test.json"))


# ──────────────────────────────────────────────────────────────────
# Response formatter
# ──────────────────────────────────────────────────────────────────

def test_response_delegates_to_pas202_on_valid_digest():
    digest = _build_digest()
    out_via_pas203 = format_simulation_digest_response(digest)
    out_via_pas202 = format_digest_for_slack(digest)
    assert out_via_pas203 == out_via_pas202


def test_response_returns_bounded_fallback_when_digest_missing():
    out = format_simulation_digest_response(None)
    assert out == MISSING_DIGEST_FALLBACK_MESSAGE


def test_response_is_deterministic():
    digest = _build_digest()
    a = format_simulation_digest_response(digest)
    b = format_simulation_digest_response(digest)
    assert a == b


def test_response_never_contains_forbidden_tokens():
    digest = _build_digest()
    out = format_simulation_digest_response(digest).lower()
    for tok in FORBIDDEN_OUTPUT_TOKENS:
        assert tok not in out


def test_fallback_message_never_contains_forbidden_tokens():
    out = MISSING_DIGEST_FALLBACK_MESSAGE.lower()
    for tok in FORBIDDEN_OUTPUT_TOKENS:
        assert tok not in out


def test_response_rejects_non_pas201_digest_via_pas202_validator():
    bad = _build_digest()
    bad["phase"] = "PAS199"
    with pytest.raises(ValueError):
        format_simulation_digest_response(bad)


# ──────────────────────────────────────────────────────────────────
# Full route helper
# ──────────────────────────────────────────────────────────────────

def test_route_matches_alias_with_present_digest():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        _write_digest_file(tp)
        out = try_route_simulation_digest("simulation digest", tp)
        assert out is not None
        assert "*PAS201 digest*" in out
        assert "SIMULATION_ONLY" in out


def test_route_matches_alias_with_missing_digest_returns_fallback():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        out = try_route_simulation_digest("simulation digest", tp)
        assert out == MISSING_DIGEST_FALLBACK_MESSAGE


def test_route_unrelated_text_returns_none():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        _write_digest_file(tp)
        assert try_route_simulation_digest("stats", tp) is None
        assert try_route_simulation_digest("calls today", tp) is None
        assert try_route_simulation_digest("", tp) is None


def test_route_with_corrupt_digest_returns_fallback():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        fp = tp / f"{DIGEST_FILENAME_PREFIX}20260101T000000Z_pas201-dgst-aaaaaaaaaaaaaaaa.json"
        fp.write_text("not json", encoding="utf-8")
        out = try_route_simulation_digest("simulation digest", tp)
        assert out == MISSING_DIGEST_FALLBACK_MESSAGE


def test_route_never_writes_to_reports_directory():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        fp = _write_digest_file(tp)
        files_before = sorted(p.name for p in tp.iterdir())
        try_route_simulation_digest("simulation digest", tp)
        try_route_simulation_digest("what did the simulation prove", tp)
        try_route_simulation_digest("rehearsal evidence", tp)
        files_after = sorted(p.name for p in tp.iterdir())
        assert files_before == files_after


def test_route_does_not_mutate_digest_on_disk():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        fp = _write_digest_file(tp)
        before = fp.read_bytes()
        try_route_simulation_digest("simulation digest", tp)
        after = fp.read_bytes()
        assert before == after


# ──────────────────────────────────────────────────────────────────
# Slack-safety invariants
# ──────────────────────────────────────────────────────────────────

_PHONE_RES = (
    re.compile(r"\b\d{3}[\s.\-]\d{3}[\s.\-]\d{4}\b"),
    re.compile(r"\(\d{3}\)\s*\d{3}[\s.\-]?\d{4}"),
)

_PROD_ID_RES = (
    re.compile(r"\bbrokerage_id\s*=\s*[\"']?[0-9a-fA-F\-]{8,}[\"']?"),
    re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"),
)


def test_response_contains_no_phone_numbers():
    out = format_simulation_digest_response(_build_digest())
    for pat in _PHONE_RES:
        assert not pat.search(out)


def test_response_contains_no_production_brokerage_ids():
    out = format_simulation_digest_response(_build_digest())
    for pat in _PROD_ID_RES:
        assert not pat.search(out)


def test_fallback_message_contains_no_pii():
    out = MISSING_DIGEST_FALLBACK_MESSAGE
    for pat in _PHONE_RES + _PROD_ID_RES:
        assert not pat.search(out)


# ──────────────────────────────────────────────────────────────────
# Source-surface invariants
# ──────────────────────────────────────────────────────────────────

_FORBIDDEN_STATUS_LITERALS = ("APPROVED", "APPLIED", "AUTO_APPLIED",
                              "LIVE", "DEPLOYED")
_FORBIDDEN_IDENTIFIERS = (
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

_BANNED_IMPORT_HEADS = ("twilio", "slack_sdk", "openai", "anthropic",
                        "dotenv", "supabase")
_BANNED_IMPORT_PREFIXES = (
    "app.services.slack.operator_intents",  # we must not modify it
    "app.services.slack.operator_responses",  # we must not modify it
    "app.routes.slack_command",
    "app.engine.state_machine",
    "app.engine",
    "app.services.notifications",  # outbound senders
)
_BANNED_CALLS = ("load_dotenv", "get_supabase")


# Strict banned-imports scan: production service file only.
# The readiness gate (`scripts/pas203_slack_evidence_digest_readiness_check.py`)
# legitimately imports PAS191's operator_intents inside a single
# carry-forward check to assert INTENT_CODES is still exactly 15
# entries — that import is a read-only AST inspection, never
# wired into a request path.
_PAS203_FILES_FOR_STRICT_IMPORT_SCAN = (
    "app/services/slack/simulation_digest_intent.py",
)


_PAS203_FILES_FOR_FORBIDDEN_LITERAL_SCAN = (
    "app/services/slack/simulation_digest_intent.py",
)


def _string_constants(src: str):
    out = set()
    try:
        tree = ast.parse(src)
    except Exception:
        return out
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            out.add(node.value)
    return out


def _identifier_names(src: str):
    out = set()
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


def _imports_and_calls(src: str):
    imports, calls = set(), set()
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module)
        elif isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Name):
                calls.add(func.id)
            elif isinstance(func, ast.Attribute):
                calls.add(func.attr)
    return imports, calls


@pytest.mark.parametrize("relpath", _PAS203_FILES_FOR_FORBIDDEN_LITERAL_SCAN)
def test_forbidden_status_literals_absent(relpath):
    consts = _string_constants(_read(relpath))
    for tok in _FORBIDDEN_STATUS_LITERALS:
        assert tok not in consts, (
            f"{relpath} carries forbidden status literal {tok!r}"
        )


@pytest.mark.parametrize("relpath", _PAS203_FILES_FOR_FORBIDDEN_LITERAL_SCAN)
def test_forbidden_identifiers_absent(relpath):
    names = _identifier_names(_read(relpath))
    for tok in _FORBIDDEN_IDENTIFIERS:
        assert tok not in names, (
            f"{relpath} carries forbidden identifier {tok!r}"
        )


@pytest.mark.parametrize("relpath", _PAS203_FILES_FOR_STRICT_IMPORT_SCAN)
def test_no_banned_imports_in_pas203_file(relpath):
    imports, calls = _imports_and_calls(_read(relpath))
    for mod in imports:
        head = mod.split(".")[0]
        assert head not in _BANNED_IMPORT_HEADS, f"{relpath} imports {mod}"
        for pref in _BANNED_IMPORT_PREFIXES:
            assert not (mod == pref or mod.startswith(pref + ".")), (
                f"{relpath} imports {mod}"
            )
    for c in calls:
        assert c not in _BANNED_CALLS, f"{relpath} calls {c}()"


# ──────────────────────────────────────────────────────────────────
# Help-line additions
# ──────────────────────────────────────────────────────────────────

def test_help_lines_are_short_and_bounded():
    assert isinstance(SIMULATION_DIGEST_HELP_LINES, tuple)
    assert 1 <= len(SIMULATION_DIGEST_HELP_LINES) <= 6
    for line in SIMULATION_DIGEST_HELP_LINES:
        assert isinstance(line, str)
        assert 0 < len(line) <= 160


def test_help_lines_reference_spec_required_phrases():
    text = "\n".join(SIMULATION_DIGEST_HELP_LINES).lower()
    assert "simulation digest" in text
    assert "what did the simulation prove" in text


# ──────────────────────────────────────────────────────────────────
# Readiness gate
# ──────────────────────────────────────────────────────────────────

_GATE = _REPO_ROOT / "scripts" / "pas203_slack_evidence_digest_readiness_check.py"


def test_readiness_gate_runs_clean_summary_only():
    proc = subprocess.run(
        [sys.executable, str(_GATE), "--summary-only"],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "verdict=READY" in proc.stdout


def test_readiness_gate_json_envelope_valid():
    proc = subprocess.run(
        [sys.executable, str(_GATE), "--summary-only", "--json"],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert proc.returncode == 0
    payload_str = proc.stdout[proc.stdout.find("{"):]
    payload = json.loads(payload_str)
    assert payload["phase"] == "PAS203"
    assert payload["verdict"] == "READY"
    assert payload["ready"] is True
    assert payload["fail_count"] == 0
    assert payload["check_count"] > 0


# ──────────────────────────────────────────────────────────────────
# Module surface — REPORTS_SUBDIR constant
# ──────────────────────────────────────────────────────────────────

def test_reports_subdir_is_reports_simulations():
    assert REPORTS_SUBDIR == "reports/simulations"


# ──────────────────────────────────────────────────────────────────
# Doc invariants
# ──────────────────────────────────────────────────────────────────

def test_doc_present_and_carries_required_clauses():
    doc = _read("docs/pas203_slack_evidence_digest_command.md").lower()
    for clause in (
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
    ):
        assert clause in doc, f"doc missing clause {clause!r}"


# ──────────────────────────────────────────────────────────────────
# Dispatcher integration (PAS203-A)
# ──────────────────────────────────────────────────────────────────
#
# These tests inspect app/routes/slack_command.py source — the
# established PAS191 / PAS192 pattern — to assert that PAS203 is
# wired into the real dispatcher correctly and that the wiring
# itself carries no writes, no simulation execution, and does not
# disturb PAS191's match_intent invocation.

_SLACK_CMD_REL = "app/routes/slack_command.py"


def _slack_cmd_src() -> str:
    return _read(_SLACK_CMD_REL)


def test_dispatcher_imports_pas203_helper():
    src = _slack_cmd_src()
    assert "from app.services.slack.simulation_digest_intent" in src
    assert "try_route_simulation_digest" in src


def test_dispatcher_calls_try_route_simulation_digest():
    src = _slack_cmd_src()
    assert "try_route_simulation_digest(" in src


def test_dispatcher_pas203_branch_fires_before_pas191():
    src = _slack_cmd_src()
    pas203_pos = src.find("try_route_simulation_digest(text")
    pas191_pos = src.find("match_intent(text)")
    assert pas203_pos >= 0, "PAS203 dispatch call missing"
    assert pas191_pos >= 0, "PAS191 match_intent(text) call missing"
    assert pas203_pos < pas191_pos, (
        "PAS203 dispatch must fire BEFORE PAS191's match_intent"
    )


def test_dispatcher_pas203_branch_logs_intent_event():
    src = _slack_cmd_src()
    # The integration logs the intent through log_event_bg with
    # the PAS203 surface token.
    assert "slack_command_pas203" in src
    # The intent name is the closed-vocab string this surface emits.
    assert '"simulation_digest"' in src or "'simulation_digest'" in src


def test_dispatcher_uses_repo_root_reports_dir():
    src = _slack_cmd_src()
    # slack_command.py lives at app/routes/ so the repo root is
    # two parents up.
    assert "parents[2]" in src
    assert '"reports"' in src or "'reports'" in src
    assert '"simulations"' in src or "'simulations'" in src


def _pas203_block(src: str) -> str:
    """Slice the PAS203 dispatch block out of the dispatcher."""
    start = src.find("PAS203-A — Read-only simulation evidence digest")
    end = src.find("PAS191 — Deterministic natural-language fast-path")
    assert start >= 0, "PAS203 block marker missing"
    assert end > start, "PAS191 block marker missing or out of order"
    return src[start:end]


_DISPATCHER_WRITE_TOKENS = (
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


def test_dispatcher_pas203_block_carries_no_write_calls():
    block = _pas203_block(_slack_cmd_src())
    for tok in _DISPATCHER_WRITE_TOKENS:
        assert tok not in block, (
            f"PAS203 dispatch block contains write call {tok!r}"
        )


_DISPATCHER_EXECUTION_TOKENS = (
    "execute_manual_test_runtime(",
    "build_evidence_digest(",
    "build_inspection(",
    "build_behavioral_evaluation(",
    "build_manual_test_package(",
    "run_scenario_under_strategy(",
    "compare_strategies(",
)


def test_dispatcher_pas203_block_does_not_execute_runtime():
    block = _pas203_block(_slack_cmd_src())
    for tok in _DISPATCHER_EXECUTION_TOKENS:
        assert tok not in block, (
            f"PAS203 dispatch block contains execution call {tok!r}"
        )


def test_dispatcher_pas203_block_returns_in_channel_response():
    # The PAS203 block must wrap the helper string in a JSONResponse
    # with response_type='in_channel' so it surfaces to the channel
    # the same way PAS191 / PAS192 responses do.
    block = _pas203_block(_slack_cmd_src())
    assert "JSONResponse" in block
    assert "in_channel" in block


def test_route_helper_does_not_match_mutation_commands_on_dispatcher_path():
    # Direct functional assertion: even with a present digest on
    # disk, mutation tokens never resolve to the PAS203 branch.
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        _write_digest_file(tp)
        for mut in ("pause", "resume", "push 123 Main St $500k 3bed",
                    "remove 123 Main St"):
            assert try_route_simulation_digest(mut, tp) is None


def test_pas191_match_intent_still_returns_unknown_for_digest_phrases():
    # Carry-forward — even after PAS203 wiring, PAS191's matcher
    # must not start binding the new phrases. The dispatcher
    # decision order is PAS203 fast-path -> PAS191 fast-path.
    from app.services.slack.operator_intents import (
        INTENT_UNKNOWN,
        match_intent,
    )
    for phrase in _SPEC_REQUIRED_PHRASES:
        result = match_intent(phrase)
        assert result["intent"] == INTENT_UNKNOWN, (
            f"PAS191 should not bind {phrase!r}; got {result['intent']!r}"
        )


def test_dispatcher_still_invokes_pas191_match_intent_after_pas203():
    # Carry-forward — PAS191 fast-path must still exist and still
    # be the second dispatch.
    src = _slack_cmd_src()
    assert "match_intent(text)" in src
    assert "_pas191_dispatch" in src
