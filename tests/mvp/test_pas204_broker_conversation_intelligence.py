"""
PAS204 — Broker conversation intelligence tests.

Coverage:

  * Catalogue: 300+ questions, 22 intents, every entry
    classifies to its expected intent on the canonical text.

  * Classifier: typo / shorthand / fragment handling; mutation
    tokens (pause/resume/push/remove) never bind any intent.

  * Response voice: token -> human translation is deterministic;
    every closed-vocab token has a translation; forbidden
    live-routing tokens never appear in any rendered response;
    no PII / no production brokerage UUIDs.

  * Conversation surface: build_broker_response returns the
    closed envelope; data-dependent intents flag
    no_data_available=True; evidence-grounded intents fold in
    PAS201 digest content when supplied.

  * Source-surface invariants: no banned imports (twilio /
    slack_sdk / openai / anthropic / dotenv / supabase /
    state machine / outbound Slack notification client); no
    forbidden status literals; no live-mutation /
    outbound-messaging identifiers; PAS191 INTENT_CODES tuple
    unchanged at 15.

  * Runner: small-slice simulation completes, structured
    report carries every required key, pass-rate >= 0.95.

  * Readiness gate: exit 0 / verdict=READY.
"""

from __future__ import annotations

import ast
import json
import pathlib
import re
import subprocess
import sys

import pytest


_REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


from app.services.slack.broker_conversation_intents import (  # noqa: E402
    INTENT_CODES,
    INTENT_FALLBACK_CLARIFY,
    match_broker_intent,
)
from app.services.slack.broker_conversation_surface import (  # noqa: E402
    build_broker_response,
)
from app.services.slack.broker_question_catalogue import (  # noqa: E402
    BROKER_QUESTION_CATALOGUE,
    CATEGORIES,
    question_count,
)
from app.services.slack.broker_response_voice import (  # noqa: E402
    FORBIDDEN_OUTPUT_TOKENS,
    NEXT_STEP_SUGGESTIONS_BY_INTENT,
    TOKEN_TRANSLATIONS,
    next_step_suggestions,
    response_for_intent,
    translate_token,
    translate_tokens,
)


def _read(relpath: str) -> str:
    return (_REPO_ROOT / relpath).read_text(encoding="utf-8")


# ──────────────────────────────────────────────────────────────────
# Catalogue invariants
# ──────────────────────────────────────────────────────────────────

def test_catalogue_has_at_least_300_questions():
    assert question_count() >= 300


def test_catalogue_uses_only_closed_intent_codes():
    for q in BROKER_QUESTION_CATALOGUE:
        assert q["intent"] in INTENT_CODES, q


def test_catalogue_uses_only_closed_categories():
    for q in BROKER_QUESTION_CATALOGUE:
        assert q["category"] in CATEGORIES, q


def test_every_intent_is_represented_in_catalogue():
    seen = {q["intent"] for q in BROKER_QUESTION_CATALOGUE}
    for code in INTENT_CODES:
        assert code in seen, code


# ──────────────────────────────────────────────────────────────────
# Classifier accuracy
# ──────────────────────────────────────────────────────────────────

def test_classifier_matches_every_catalogue_entry():
    mismatches = []
    for q in BROKER_QUESTION_CATALOGUE:
        result = match_broker_intent(q["text"])
        if result["intent"] != q["intent"]:
            mismatches.append(
                (q["text"], q["intent"], result["intent"], result["score"])
            )
    assert not mismatches, "classifier mismatches:\n  " + "\n  ".join(
        f"{t!r} expected={e} got={g} score={s}"
        for t, e, g, s in mismatches[:20]
    )


@pytest.mark.parametrize("text", [
    "",                          # empty
    "   ",                       # whitespace
    "uhhh",                      # one-token noise
    "yo",                        # casual one-token
    "?",                         # punctuation only
    "test",                      # bare keyword
])
def test_classifier_returns_fallback_for_unclassifiable(text):
    result = match_broker_intent(text)
    assert result["intent"] == INTENT_FALLBACK_CLARIFY


@pytest.mark.parametrize("text", [
    "leeds today",
    "lds today",
    "hot leeds",
    "how mny leeds today",
    "any new leeds today",
])
def test_classifier_tolerates_typos(text):
    # NB: bare "leeds" alone is intentionally ambiguous — without
    # a temporal / qualifier token it should fall back rather than
    # invent context.
    result = match_broker_intent(text)
    assert result["intent"] != INTENT_FALLBACK_CLARIFY


def test_classifier_does_not_bind_mutation_tokens():
    # Mutation commands must continue to flow through PAS191's
    # exact-command branch. They must never resolve to a PAS204
    # broker intent.
    for mut in ("pause", "resume", "push 123 Main St $500k",
                "remove 123 Main St"):
        result = match_broker_intent(mut)
        # Either fallback_clarify or an unrelated intent that
        # would never trigger a mutation — what matters is the
        # intent set itself never includes a mutation.
        assert result["intent"] in INTENT_CODES
        # The catch-all proves the matcher is bounded.
        assert result["intent"] not in (
            "apply_recommendation", "deploy_strategy",
            "switch_strategy_live",
        )


# ──────────────────────────────────────────────────────────────────
# Response voice
# ──────────────────────────────────────────────────────────────────

def test_translate_token_is_deterministic():
    for tok in TOKEN_TRANSLATIONS:
        assert translate_token(tok) == translate_token(tok)
        assert translate_token(tok) == TOKEN_TRANSLATIONS[tok]


def test_translate_unknown_token_returns_empty():
    assert translate_token("definitely_not_a_pas_token") == ""
    assert translate_token("") == ""
    assert translate_token(None) == ""  # type: ignore


def test_translate_tokens_skips_unknown():
    out = translate_tokens(("SIMULATION_ONLY", "garbage", "lineage_intact"))
    assert len(out) == 2


def test_every_intent_has_a_response_builder():
    for intent in INTENT_CODES:
        body = response_for_intent(intent)
        assert isinstance(body, str)
        assert len(body) >= 40


def test_every_intent_has_next_step_suggestions():
    for intent in INTENT_CODES:
        suggestions = next_step_suggestions(intent)
        assert isinstance(suggestions, tuple)
        assert len(suggestions) >= 1


def test_every_response_avoids_forbidden_live_routing_tokens():
    for intent in INTENT_CODES:
        body = response_for_intent(intent).lower()
        for tok in FORBIDDEN_OUTPUT_TOKENS:
            assert tok not in body, f"{intent}: {tok!r}"


def test_every_response_avoids_pii_shaped_tokens():
    phone_patterns = (
        re.compile(r"\b\d{3}[\s.\-]\d{3}[\s.\-]\d{4}\b"),
        re.compile(r"\(\d{3}\)\s*\d{3}[\s.\-]?\d{4}"),
    )
    prod_patterns = (
        re.compile(r"\bbrokerage_id\s*=\s*[\"']?[0-9a-fA-F\-]{8,}[\"']?"),
        re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"),
    )
    for intent in INTENT_CODES:
        body = response_for_intent(intent)
        for pat in phone_patterns + prod_patterns:
            assert not pat.search(body), f"{intent}: matched {pat.pattern!r}"


def test_translation_table_covers_every_pas201_evidence_strength():
    for strength in ("strong", "moderate", "weak", "blocked"):
        assert translate_token(strength) != ""


# ──────────────────────────────────────────────────────────────────
# Conversation surface
# ──────────────────────────────────────────────────────────────────

_RESPONSE_REQUIRED_KEYS = (
    "intent", "score", "response_text", "suggested_next",
    "evidence_grounded", "no_data_available", "clarifying_question",
)


def test_build_broker_response_returns_closed_envelope():
    out = build_broker_response("how many leads today")
    for k in _RESPONSE_REQUIRED_KEYS:
        assert k in out


def test_build_broker_response_flags_no_data_available():
    out = build_broker_response("how many leads today")
    assert out["no_data_available"] is True
    assert out["intent"] != INTENT_FALLBACK_CLARIFY


def test_build_broker_response_returns_fallback_with_clarifier_for_ambiguous():
    out = build_broker_response("hmm idk maybe")
    assert out["intent"] == INTENT_FALLBACK_CLARIFY
    assert out["clarifying_question"] is not None


def test_build_broker_response_skips_clarifier_for_one_word():
    out = build_broker_response("yo")
    assert out["intent"] == INTENT_FALLBACK_CLARIFY
    assert out["clarifying_question"] is None


def test_build_broker_response_evidence_grounded_for_digest_intent():
    fake_evidence = {
        "evidence_strength": "strong",
        "operator_summary": {
            "highlights": ["safety_outcome_clean", "lineage_intact"],
        },
    }
    out = build_broker_response("simulation digest", evidence=fake_evidence)
    assert out["evidence_grounded"] is True
    # Body should now contain a human translation of "strong".
    assert "Strong" in out["response_text"] or "strong" in out["response_text"].lower()


def test_build_broker_response_does_not_assert_live_routing():
    for q in BROKER_QUESTION_CATALOGUE[:50]:
        out = build_broker_response(q["text"])
        body = out["response_text"].lower()
        for tok in FORBIDDEN_OUTPUT_TOKENS:
            assert tok not in body
        for ph in ("now live", "live deployment", "we just routed",
                   "i just called", "live call active"):
            assert ph not in body


def test_build_broker_response_never_invents_lead_data():
    # For every data-dependent intent, the body should never
    # claim a specific count or name. We assert by checking the
    # body does not contain pure number tokens that would
    # represent counts (e.g., "12 leads", "47%").
    n_pattern = re.compile(r"\b\d+\s+(leads?|callbacks?|bookings?|appointments?)\b")
    pct_pattern = re.compile(r"\b\d+%")
    for q in BROKER_QUESTION_CATALOGUE[:50]:
        out = build_broker_response(q["text"])
        body = out["response_text"]
        assert not n_pattern.search(body), (q["text"], body)
        assert not pct_pattern.search(body), (q["text"], body)


def test_build_broker_response_translates_pas200_jargon_when_relevant():
    # When evidence carries technical highlights, the rendered
    # body should include their translations (not the raw token).
    fake_evidence = {
        "evidence_strength": "strong",
        "operator_summary": {
            "highlights": ["behavioral_low_friction_observed"],
        },
    }
    out = build_broker_response("simulation digest", evidence=fake_evidence)
    body = out["response_text"]
    assert "behavioral_low_friction_observed" not in body
    assert "smooth" in body.lower() or "didn't push" in body.lower()


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
    "app.services.slack.operator_intents",     # must not modify it
    "app.services.slack.operator_responses",   # must not modify it
    "app.routes.slack_command",
    "app.engine.state_machine",
    "app.engine",
    "app.services.notifications",
)
_BANNED_CALLS = ("load_dotenv", "get_supabase")


_PAS204_PRODUCTION_FILES = (
    "app/services/slack/broker_question_catalogue.py",
    "app/services/slack/broker_conversation_intents.py",
    "app/services/slack/broker_response_voice.py",
    "app/services/slack/broker_conversation_surface.py",
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


@pytest.mark.parametrize("relpath", _PAS204_PRODUCTION_FILES)
def test_forbidden_status_literals_absent(relpath):
    consts = _string_constants(_read(relpath))
    for tok in _FORBIDDEN_STATUS_LITERALS:
        assert tok not in consts, f"{relpath} carries {tok!r}"


@pytest.mark.parametrize("relpath", _PAS204_PRODUCTION_FILES)
def test_forbidden_identifiers_absent(relpath):
    names = _identifier_names(_read(relpath))
    for tok in _FORBIDDEN_IDENTIFIERS:
        assert tok not in names, f"{relpath} carries identifier {tok!r}"


@pytest.mark.parametrize("relpath", _PAS204_PRODUCTION_FILES)
def test_no_banned_imports_in_pas204_file(relpath):
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


def test_pas191_intent_codes_unchanged():
    from app.services.slack.operator_intents import INTENT_CODES as PAS191_INTENT_CODES
    assert len(PAS191_INTENT_CODES) == 15


def test_pas204_intent_codes_do_not_collide_with_pas191():
    from app.services.slack.operator_intents import INTENT_CODES as PAS191_INTENT_CODES
    # PAS204 may name its intents anything; we just assert that
    # no PAS204 intent string equals a PAS191 one (which would
    # be confusing in event logs).
    overlap = set(INTENT_CODES) & set(PAS191_INTENT_CODES)
    assert not overlap, f"PAS204/PAS191 intent collision: {overlap}"


# ──────────────────────────────────────────────────────────────────
# Runner
# ──────────────────────────────────────────────────────────────────

_RUNNER = _REPO_ROOT / "scripts" / "pas204_run_broker_question_simulations.py"


def test_runner_small_slice_summary_only():
    proc = subprocess.run(
        [
            sys.executable, str(_RUNNER),
            "--questions", "10",
            "--variants",  "10",
            "--summary-only",
        ],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "[PAS204] runs=" in proc.stdout
    assert "pass_rate=" in proc.stdout


def test_runner_full_report_payload_carries_required_keys(tmp_path):
    proc = subprocess.run(
        [
            sys.executable, str(_RUNNER),
            "--questions", "5",
            "--variants",  "5",
            "--summary-only",
            "--json",
        ],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert proc.returncode == 0
    payload_str = proc.stdout[proc.stdout.find("{"):]
    payload = json.loads(payload_str)
    for k in (
        "phase", "generated_at", "total_questions", "total_runs",
        "pass_count", "pass_rate", "typo_failure_rate",
        "jargon_leak_rate", "false_claim_count", "weakest_intents",
        "recommended_prompt_improvements", "top_failed_examples",
        "allowed_environment", "live_behavior_changed",
    ):
        assert k in payload, k
    assert payload["phase"] == "PAS204"
    assert payload["allowed_environment"] == "SIMULATION_ONLY"
    assert payload["live_behavior_changed"] is False


def test_runner_small_slice_pass_rate_high():
    # Quick functional confidence — on the canonical text only
    # ("identity" variant) every question must classify and
    # render a clean response.
    from scripts.pas204_run_broker_question_simulations import (  # noqa: E402
        run_simulations,
    )
    result = run_simulations(questions_limit=308, variants_limit=1)
    assert result["pass_rate"] >= 0.99, result


# ──────────────────────────────────────────────────────────────────
# Readiness gate
# ──────────────────────────────────────────────────────────────────

_GATE = _REPO_ROOT / "scripts" / "pas204_broker_conversation_readiness_check.py"


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
    assert payload["phase"] == "PAS204"
    assert payload["verdict"] == "READY"
    assert payload["ready"] is True
    assert payload["fail_count"] == 0
    assert payload["check_count"] > 0


# ──────────────────────────────────────────────────────────────────
# Doc invariants
# ──────────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────────
# Dispatcher integration (PAS204-A)
# ──────────────────────────────────────────────────────────────────
#
# These tests inspect app/routes/slack_command.py source — the
# established PAS191 / PAS192 / PAS203 pattern — to assert that
# PAS204 is wired into the real dispatcher correctly and that
# the wiring is additive, non-mutating, and preserves the
# decision order PAS203 -> PAS204 (defer-to-PAS191) -> PAS191
# -> LLM.

_SLACK_CMD_REL = "app/routes/slack_command.py"


def _slack_cmd_src() -> str:
    return _read(_SLACK_CMD_REL)


def test_dispatcher_imports_pas204_helper():
    src = _slack_cmd_src()
    assert "from app.services.slack.broker_conversation_surface" in src
    assert "build_broker_response" in src


def test_dispatcher_calls_build_broker_response():
    src = _slack_cmd_src()
    assert "build_broker_response(text" in src


def test_dispatcher_pas204_block_after_pas203_fast_path():
    src = _slack_cmd_src()
    pas203_pos = src.find("try_route_simulation_digest(text")
    pas204_pos = src.find("build_broker_response(text")
    assert pas203_pos >= 0, "PAS203 dispatch missing"
    assert pas204_pos >= 0, "PAS204 dispatch missing"
    assert pas203_pos < pas204_pos, (
        "PAS204 dispatch must come AFTER PAS203 fast-path"
    )


def test_dispatcher_pas204_block_before_pas191_dispatch():
    src = _slack_cmd_src()
    pas204_pos = src.find("build_broker_response(text")
    pas191_dispatch_pos = src.find("_pas191_dispatch(pas191_intent")
    assert pas204_pos >= 0
    assert pas191_dispatch_pos >= 0
    assert pas204_pos < pas191_dispatch_pos, (
        "PAS204 dispatch must come BEFORE PAS191's _pas191_dispatch"
    )


def test_dispatcher_pas204_block_defers_to_pas191_match():
    # PAS204 must not race ahead of PAS191's matcher. The block
    # must be gated on `pas191_intent == INTENT_UNKNOWN`.
    src = _slack_cmd_src()
    pas204_pos = src.find("build_broker_response(text")
    # Walk back ~600 chars and look for the guard.
    window = src[max(0, pas204_pos - 800):pas204_pos]
    assert "pas191_intent == INTENT_UNKNOWN" in window, (
        "PAS204 dispatch must be gated on pas191_intent == INTENT_UNKNOWN"
    )


def test_dispatcher_pas204_block_logs_intent_event():
    src = _slack_cmd_src()
    assert "slack_command_pas204" in src


def _pas204_block(src: str) -> str:
    start = src.find("PAS204-A — Broker conversation intelligence")
    end = src.find("if pas191_intent != INTENT_UNKNOWN:")
    assert start >= 0, "PAS204-A block marker missing"
    assert end > start, "PAS191 dispatch marker missing or out of order"
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


def test_dispatcher_pas204_block_carries_no_write_calls():
    block = _pas204_block(_slack_cmd_src())
    for tok in _DISPATCHER_WRITE_TOKENS:
        assert tok not in block, (
            f"PAS204 dispatch block contains write call {tok!r}"
        )


_DISPATCHER_EXECUTION_TOKENS = (
    "execute_manual_test_runtime(",
    "build_evidence_digest(",
    "build_inspection(",
    "build_behavioral_evaluation(",
    "build_manual_test_package(",
    "run_scenario_under_strategy(",
    "compare_strategies(",
    "run_simulations(",
)


def test_dispatcher_pas204_block_does_not_execute_simulations():
    block = _pas204_block(_slack_cmd_src())
    for tok in _DISPATCHER_EXECUTION_TOKENS:
        assert tok not in block, (
            f"PAS204 dispatch block contains execution call {tok!r}"
        )


def test_dispatcher_pas204_block_returns_in_channel_response():
    block = _pas204_block(_slack_cmd_src())
    assert "JSONResponse" in block
    assert "in_channel" in block


def test_pas191_intents_take_precedence_over_pas204():
    # The dispatcher logic is "PAS204 fires only when
    # pas191_intent == INTENT_UNKNOWN". Verify that every
    # PAS191 command listed in the spec's guardrail returns a
    # non-UNKNOWN intent from PAS191's matcher (so the
    # dispatcher will route to PAS191, not PAS204).
    from app.services.slack.operator_intents import (
        INTENT_UNKNOWN as PAS191_UNKNOWN,
    )
    from app.services.slack.operator_intents import (
        match_intent as pas191_match,
    )
    for cmd in (
        "stats", "calls today", "leads today", "response rate",
        "summary", "next action", "priorities", "help",
        "callbacks", "bookings today", "queue", "incidents",
        "policy", "health", "are we paused",
    ):
        result = pas191_match(cmd)
        assert result["intent"] != PAS191_UNKNOWN, (
            f"PAS191 command {cmd!r} unexpectedly returned UNKNOWN "
            f"-- PAS204 would intercept it"
        )


def test_pas204_responds_to_broker_question_hot_leads():
    out = build_broker_response("hot leads")
    assert out["intent"] == "hot_leads_summary"
    assert out["response_text"]
    assert out["suggested_next"]


def test_pas204_responds_to_typo_leeds_today():
    out = build_broker_response("leeds today")
    assert out["intent"] == "leads_today_count"


def test_pas204_responds_to_beginner_question_with_clarifier_or_intent():
    out = build_broker_response("how do i use this thing")
    # Either classified to an intent, or fell back with a
    # clarifying question — both are valid PAS204 responses.
    if out["intent"] == "fallback_clarify":
        assert out["clarifying_question"] is not None
    else:
        assert out["intent"] in INTENT_CODES
    assert out["response_text"]


def test_pas203_phrases_resolve_to_simulation_digest_intent():
    # The dispatcher's PAS203 fast-path fires before PAS204, so
    # PAS203 phrases never reach PAS204. We assert this here at
    # the helper level by re-using PAS203's own router.
    from pathlib import Path
    from app.services.slack.simulation_digest_intent import (
        try_route_simulation_digest,
    )
    with __import__("tempfile").TemporaryDirectory() as tmp:
        tp = Path(tmp)
        out = try_route_simulation_digest("simulation digest", tp)
        assert out is not None  # PAS203 owns this phrase


def test_pas204_does_not_match_mutation_commands():
    # Mutation commands never resolve to a PAS204 intent.
    for mut in ("pause", "resume", "push 123 Main St $500k",
                "remove 123 Main St"):
        out = build_broker_response(mut)
        assert out["intent"] == "fallback_clarify"


def test_pas204_response_carries_no_internal_jargon():
    for q in BROKER_QUESTION_CATALOGUE[:30]:
        out = build_broker_response(q["text"])
        body = out["response_text"]
        for tok in FORBIDDEN_OUTPUT_TOKENS:
            assert tok not in body.lower()
        # PAS internal closed-vocab tokens should never appear
        # in broker-facing output verbatim.
        for raw in ("behavioral_low_friction_observed",
                    "behavioral_low_trust_observed",
                    "runtime_pass_rate_100_percent",
                    "safety_outcome_clean",
                    "lineage_intact",
                    "artifact_integrity_complete"):
            assert raw not in body, (q["text"], raw)


def test_pas204_response_carries_suggested_next_step():
    for q in BROKER_QUESTION_CATALOGUE[:30]:
        out = build_broker_response(q["text"])
        assert out["suggested_next"]
        assert all(isinstance(s, str) and s.strip()
                   for s in out["suggested_next"])


def test_dispatcher_still_invokes_pas191_after_pas204():
    src = _slack_cmd_src()
    # Carry-forward — PAS191's match_intent and dispatch must
    # both still appear and still wire to _pas191_dispatch.
    assert "match_intent(text)" in src
    assert "_pas191_dispatch" in src


# ──────────────────────────────────────────────────────────────────
# PAS204-B onboarding + fallback polish
# ──────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("phrase", [
    "how do i use this thing",
    "how do i even use this thing",
    "how do i use pas",
    "what can pas do",
    "what can you do",
    "help me use pas",
    "where do i start",
    "how should i start",
    "how do i even fuckin use this thing",
    "i don't know what to ask",
    "what should i ask you",
    "how does this thing work",
    "getting started",
    "how do i begin",
])
def test_onboarding_phrases_map_to_onboarding_intent(phrase):
    result = match_broker_intent(phrase)
    assert result["intent"] == "onboarding_help", (
        f"{phrase!r} resolved to {result['intent']!r}"
    )


def test_onboarding_response_starts_with_start_here_phrasing():
    out = build_broker_response("how do i use this thing")
    assert out["intent"] == "onboarding_help"
    body = out["response_text"]
    # The onboarding response leads with an instructional tone.
    lower = body.lower()
    assert "start here" in lower or "start" in lower
    # It mentions the kinds of things PAS can answer.
    assert (
        "leads" in lower and "callbacks" in lower
        and ("recommend" in lower or "respond" in lower)
    )


def test_onboarding_response_acknowledges_crm_data_dependency():
    out = build_broker_response("how do i use pas")
    body = out["response_text"].lower()
    # Acknowledges "if CRM is connected" / "if not connected".
    assert "crm" in body
    assert "connected" in body or "not connected" in body


def test_onboarding_intent_carries_suggested_next_steps():
    out = build_broker_response("what can pas do")
    assert out["intent"] == "onboarding_help"
    assert out["suggested_next"]
    assert len(out["suggested_next"]) >= 1


def test_fallback_response_no_longer_says_didnt_catch_that():
    # PAS204-B replaces the old "I didn't catch that one..."
    # wording with a friendlier "I can help, but I need a
    # little more direction." opener.
    out = build_broker_response("hmm idk maybe")
    assert out["intent"] == "fallback_clarify"
    body = out["response_text"]
    assert "didn't catch that" not in body.lower()
    assert "I can help" in body or "i can help" in body.lower()


def test_fallback_response_lists_useful_examples():
    out = build_broker_response("hmm idk maybe")
    body = out["response_text"]
    # PAS204-C: fallback is intentionally short with three
    # concrete inline example prompts (not the long bullet
    # list PAS204-B shipped). Three quoted examples = 6
    # quote marks. Test bounds the floor.
    examples_count = body.count('"')
    assert examples_count >= 6, body
    # Each spec example appears.
    assert "hot leads" in body
    assert "leads today" in body
    assert "what should I do next" in body


def test_pas204_b_humanized_digest_translation_table_available():
    # The PAS204-B polish adds humanised translations for the
    # PAS200/PAS201 closed-vocab tokens. They must be present
    # in the PAS204 response-voice translation table OR in
    # PAS202's translation table. We assert the PAS204 voice
    # table covers the user-spec tokens.
    expected = {
        "runtime_pass_rate_100_percent",
        "safety_outcome_clean",
        "lineage_intact",
        "artifact_integrity_complete",
        "behavioral_low_friction_observed",
        "behavioral_good_pacing_observed",
        "behavioral_low_trust_observed",
        "behavioral_callback_continuity_observed",
        "no_live_behavior_change_anywhere_in_lineage",
    }
    missing = [t for t in expected if t not in TOKEN_TRANSLATIONS]
    assert not missing, f"missing humanised translations: {missing}"


def test_digest_slack_output_carries_no_raw_internal_tokens():
    # Smoke test that exercises the PAS202 humanised Slack
    # output through the digest the test-pas204 build helper
    # already provides via PAS199 (build_inspection) etc. We
    # build a fake evidence dict and pass it through
    # build_broker_response with the evidence digest intent.
    from app.services.simulation.behavioral_evaluation import (
        build_behavioral_evaluation,
    )
    from app.services.simulation.evidence_digest import (
        build_evidence_digest,
    )
    from app.services.simulation.evidence_digest_surface import (
        format_digest_for_slack,
    )
    from app.services.simulation.manual_test_runtime import (
        execute_manual_test_runtime,
    )
    from app.services.simulation.runtime_inspection import (
        build_inspection,
    )
    rec = {
        "recommendation_id": "pas195-rec-pas204b",
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
        "review_id": "pas196-rev-pas204b",
        "recommendation_id": "pas195-rec-pas204b",
        "previous_status": "CANDIDATE",
        "new_status": "APPROVED_FOR_MANUAL_TEST",
        "live_behavior_changed": False,
        "actor_type": "operator",
        "actor_id_token": "op_pas204b1234",
        "reason_token": "operator_approved_for_manual_test",
        "reviewed_at": "2026-05-22T00:00:00Z",
        "operator_required": True,
        "phase": "PAS196",
    }
    pkg = {
        "package_id": "pas197-pkg-pas204b",
        "phase": "PAS197",
        "recommendation_id": "pas195-rec-pas204b",
        "review_id": "pas196-rev-pas204b",
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
    slack_out = format_digest_for_slack(digest)
    # PAS204-B requires zero raw internal underscore-tokens in
    # the Slack output.
    raw_tokens = (
        "runtime_pass_rate_100_percent",
        "safety_outcome_clean",
        "lineage_intact",
        "artifact_integrity_complete",
        "behavioral_low_friction_observed",
        "behavioral_low_trust_observed",
        "behavioral_callback_continuity_observed",
        "no_live_behavior_change_anywhere_in_lineage",
        "lineage_inspectable_end_to_end",
        "automated_promotion_to_runtime_strategy_pending",
        "review_digest_then_decide_pilot_step",
    )
    for tok in raw_tokens:
        assert tok not in slack_out, (
            f"PAS202 Slack output leaked raw token {tok!r} — "
            f"PAS204-B requires humanisation"
        )
    # And the humanised translations are present.
    assert (
        "rehearsal" in slack_out.lower()
        or "evidence trail" in slack_out.lower()
    )


# ──────────────────────────────────────────────────────────────────
# PAS204-C — Fuzzy command recovery + demo data labeling
# ──────────────────────────────────────────────────────────────────

from app.services.slack.fuzzy_command_normalizer import (  # noqa: E402
    alias_count as fuzzy_alias_count,
    is_protected_token,
    list_aliases as fuzzy_list_aliases,
    normalize_fuzzy_command,
)
from app.services.slack.demo_data_detector import (  # noqa: E402
    SIGNAL_BROKERAGE_ENVIRONMENT_LABEL,
    SIGNAL_BROKERAGE_MARKED_DEMO,
    SIGNAL_ROW_CALL_TYPE_SIMULATED,
    SIGNAL_ROW_METADATA_SEED_BATCH,
    SIGNAL_ROW_PHONE_SEED_CONVENTION,
    SIGNAL_ROW_SOURCE_SIMULATED,
    VERDICT_DEMO_DETECTED,
    VERDICT_NO_DEMO_SIGNAL,
    VERDICT_UNKNOWN,
    detect_demo_signals,
)
from app.services.slack.operator_responses import (  # noqa: E402
    format_stats,
)


# ── fuzzy normalizer ─────────────────────────────────────────────

@pytest.mark.parametrize("raw,expected_norm", [
    ("leeds today",       "leads today"),
    ("leed today",        "leads today"),
    ("lds today",         "leads today"),
    ("hott leeds",        "hot leads"),
    ("callbak today",     "callback today"),
    ("respnse speed",     "response speed"),
    ("digst",             "digest"),
    ("saafe to use",      "safe to use"),
    ("uze this thng",     "use this thing"),
    ("zillw leads",       "zillow leads"),
    ("stat",              "stats"),
    ("response rat",      "response rate"),
])
def test_fuzzy_normalizer_rewrites_known_typos(raw, expected_norm):
    assert normalize_fuzzy_command(raw) == expected_norm


@pytest.mark.parametrize("text", [
    "pause",
    "resume",
    "push 123 Main St",
    "remove 123 Main St",
    "Pause",
    "RESUME",
    "pasue",  # typo of pause — still must NOT be rewritten
])
def test_fuzzy_normalizer_does_not_touch_mutation_tokens(text):
    out = normalize_fuzzy_command(text)
    # Mutation tokens (and their typos) flow through unchanged so
    # the PAS191 exact-command branch keeps owning them.
    assert text.split()[0] == out.split()[0]


def test_fuzzy_normalizer_preserves_unknown_tokens():
    out = normalize_fuzzy_command("how many widgets did we sell")
    # No alias for "widgets" / "sell" — pass through unchanged.
    assert out == "how many widgets did we sell"


def test_fuzzy_normalizer_handles_empty_and_non_string():
    assert normalize_fuzzy_command("") == ""
    assert normalize_fuzzy_command("   ") == ""
    assert normalize_fuzzy_command(None) == ""  # type: ignore
    assert normalize_fuzzy_command(123) == ""   # type: ignore


def test_fuzzy_normalizer_preserves_surrounding_punctuation():
    # "leeds today?" -> "leads today?" (trailing ? preserved)
    out = normalize_fuzzy_command("leeds today?")
    assert out == "leads today?"


def test_fuzzy_normalizer_alias_count_bounded():
    n = fuzzy_alias_count()
    assert 20 <= n <= 200


def test_fuzzy_normalizer_alias_table_has_no_self_loops():
    # No alias should map a canonical token to itself.
    for key in fuzzy_list_aliases():
        out = normalize_fuzzy_command(key)
        assert out != key, f"self-loop alias: {key!r} -> {out!r}"


def test_is_protected_token_covers_mutation_set():
    for t in ("pause", "resume", "push", "remove",
              "Pause", "RESUME"):
        assert is_protected_token(t)
    for t in ("hot", "leads", "callback"):
        assert not is_protected_token(t)


@pytest.mark.parametrize("raw,expected_intent", [
    ("leeds today",     "leads_today_count"),
    ("leed today",      "leads_today_count"),
    ("lds today",       "leads_today_count"),
    ("hott leeds",      "hot_leads_summary"),
    ("callbak today",   "callback_requests"),
    ("respnse speed",   "response_speed"),
    ("digst",           "evidence_digest_summary"),
    ("zillw leads",     "zillow_lead_handling"),
])
def test_full_pipeline_normalize_then_classify(raw, expected_intent):
    # The dispatcher applies normalize_fuzzy_command BEFORE the
    # classifier sees the text. We replicate that here.
    normalized = normalize_fuzzy_command(raw)
    out = build_broker_response(normalized)
    assert out["intent"] == expected_intent, (
        f"{raw!r} -> norm {normalized!r} -> got intent "
        f"{out['intent']!r}, expected {expected_intent!r}"
    )


# ── shortened fallback ───────────────────────────────────────────

def test_fallback_is_short():
    out = build_broker_response("hmm idk maybe")
    body = out["response_text"]
    # PAS204-C reduces the long bullet-list fallback to a single
    # sentence with three example prompts. Bound the length so
    # any future regression bloats it back up.
    assert len(body) <= 200, f"fallback got long again: {len(body)}"
    assert "I can help" in body
    assert "leads today" in body
    assert "hot leads" in body
    assert "what should I do next" in body


def test_fallback_no_longer_lists_six_examples():
    out = build_broker_response("hmm idk maybe")
    body = out["response_text"]
    # The old fallback listed 6 hyphen-bullet examples. PAS204-C
    # collapses them to a single inline list.
    assert body.count("\n- ") == 0
    assert body.count("\n• ") == 0


# ── demo data detector ───────────────────────────────────────────

def test_detector_returns_unknown_when_no_inputs():
    out = detect_demo_signals()
    assert out["verdict"] == VERDICT_UNKNOWN
    assert out["signals"] == ()


def test_detector_returns_no_demo_signal_for_real_brokerage():
    brokerage = {"id": "real-brokerage", "name": "Acme Realty"}
    out = detect_demo_signals(brokerage=brokerage)
    assert out["verdict"] == VERDICT_NO_DEMO_SIGNAL
    assert out["signals"] == ()


def test_detector_fires_on_brokerage_is_demo_flag():
    out = detect_demo_signals(brokerage={"id": "x", "is_demo": True})
    assert out["verdict"] == VERDICT_DEMO_DETECTED
    assert SIGNAL_BROKERAGE_MARKED_DEMO in out["signals"]


def test_detector_fires_on_brokerage_environment_label():
    out = detect_demo_signals(
        brokerage={"id": "x", "environment": "rehearsal"},
    )
    assert out["verdict"] == VERDICT_DEMO_DETECTED
    assert SIGNAL_BROKERAGE_ENVIRONMENT_LABEL in out["signals"]


def test_detector_fires_on_row_source_simulated():
    rows = [{"id": 1, "source": "simulated"}]
    out = detect_demo_signals(rows=rows)
    assert out["verdict"] == VERDICT_DEMO_DETECTED
    assert SIGNAL_ROW_SOURCE_SIMULATED in out["signals"]


def test_detector_fires_on_row_call_type_simulated():
    rows = [{"id": 1, "call_type": "simulated"}]
    out = detect_demo_signals(rows=rows)
    assert out["verdict"] == VERDICT_DEMO_DETECTED
    assert SIGNAL_ROW_CALL_TYPE_SIMULATED in out["signals"]


def test_detector_fires_on_row_metadata_seed_batch():
    rows = [{"id": 1, "metadata": {"seed_batch": "demo-001"}}]
    out = detect_demo_signals(rows=rows)
    assert out["verdict"] == VERDICT_DEMO_DETECTED
    assert SIGNAL_ROW_METADATA_SEED_BATCH in out["signals"]


def test_detector_fires_on_row_phone_seed_convention():
    rows = [{"id": 1, "phone_number": "+15555550199"}]
    out = detect_demo_signals(rows=rows)
    assert out["verdict"] == VERDICT_DEMO_DETECTED
    assert SIGNAL_ROW_PHONE_SEED_CONVENTION in out["signals"]


def test_detector_does_not_fire_on_normal_phone():
    rows = [{"id": 1, "phone_number": "+15035551212"}]
    out = detect_demo_signals(rows=rows)
    assert out["verdict"] == VERDICT_NO_DEMO_SIGNAL


def test_detector_does_not_falsely_label_production_data():
    # Real brokerage + real-looking rows -> no_demo_signal.
    brokerage = {"id": "real-id", "name": "Acme Realty"}
    rows = [
        {"id": 1, "source": "twilio_webhook", "call_type": "outbound",
         "phone_number": "+15035551212", "metadata": {}},
        {"id": 2, "source": "twilio_webhook", "call_type": "outbound",
         "phone_number": "+15035551213"},
    ]
    out = detect_demo_signals(brokerage=brokerage, rows=rows)
    assert out["verdict"] == VERDICT_NO_DEMO_SIGNAL
    assert out["signals"] == ()


# ── format_stats demo-aware rendering ────────────────────────────

def test_format_stats_legacy_call_unchanged():
    # Without demo_verdict, format_stats produces the exact
    # pre-PAS204-C output.
    out = format_stats({"total": 100, "completed": 80, "booked": 20})
    assert "*All-time stats*" in out
    assert "Total calls: 100" in out
    assert "Demo stats" not in out
    assert "Note:" not in out


def test_format_stats_with_demo_detected_uses_demo_header():
    out = format_stats(
        {"total": 35, "completed": 22, "booked": 5},
        demo_verdict=VERDICT_DEMO_DETECTED,
    )
    assert "Demo stats" in out
    assert "rehearsal data" in out
    assert "Total calls: 35" in out
    assert "Completed: 22" in out
    assert "Booked: 5" in out


def test_format_stats_with_no_demo_signal_uses_real_header():
    out = format_stats(
        {"total": 35, "completed": 22, "booked": 5},
        demo_verdict=VERDICT_NO_DEMO_SIGNAL,
    )
    # Real brokerage with real data: identical to legacy output,
    # no demo label, no conservative note.
    assert "*All-time stats*" in out
    assert "Demo stats" not in out
    assert "Note:" not in out


def test_format_stats_with_unknown_adds_conservative_note():
    out = format_stats(
        {"total": 35, "completed": 22, "booked": 5},
        demo_verdict=VERDICT_UNKNOWN,
    )
    assert "*All-time stats*" in out
    assert "Demo stats" not in out
    assert "verify whether this environment" in out


# ── dispatcher wiring (PAS204-C) ─────────────────────────────────

def test_dispatcher_imports_pas204c_helpers():
    src = _read("app/routes/slack_command.py")
    assert "from app.services.slack.fuzzy_command_normalizer" in src
    assert "normalize_fuzzy_command" in src
    assert "from app.services.slack.demo_data_detector" in src
    assert "detect_demo_signals" in src


def test_dispatcher_calls_normalize_before_matchers():
    src = _read("app/routes/slack_command.py")
    norm_pos = src.find("normalize_fuzzy_command(text)")
    pas203_pos = src.find("try_route_simulation_digest(text")
    pas191_match_pos = src.find("match_intent(text)")
    assert norm_pos >= 0, "normalize_fuzzy_command call missing"
    assert pas203_pos >= 0
    assert pas191_match_pos >= 0
    assert norm_pos < pas203_pos < pas191_match_pos, (
        "normalize_fuzzy_command must fire BEFORE PAS203 and PAS191"
    )


def test_dispatcher_passes_demo_verdict_to_format_stats():
    src = _read("app/routes/slack_command.py")
    # The INTENT_STATS branch must call detect_demo_signals and
    # forward demo_verdict to format_stats.
    assert "detect_demo_signals(" in src
    assert "demo_verdict" in src


def test_doc_present_and_carries_required_clauses():
    doc = _read("docs/pas204_broker_conversation_intelligence.md").lower()
    for clause in (
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
    ):
        assert clause in doc, f"doc missing clause {clause!r}"
