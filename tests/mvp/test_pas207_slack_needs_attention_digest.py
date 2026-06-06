"""
PAS207 — Slack read-only proactive needs-attention digest tests.

Coverage:

  * Every spec phrase maps to needs_attention.
  * try_route_needs_attention returns a non-empty broker-friendly
    string on match and None on non-match.
  * Renderer carries no closed-vocab technical tokens
    (callback_overdue, lead_unassigned, ...).
  * Renderer never mentions PAS internals (PAS205 / PAS207 /
    SIMULATION_ONLY / live_behavior_changed).
  * Snapshot provider is injectable; default is the deterministic
    demo snapshot.
  * Empty-pipeline snapshot returns the bounded no-signals message.
  * PAS191 carry-forward — the closed alias table does NOT contain
    next_action / priorities / next_steps / top priorities / what
    should i do now / what should i focus on.
  * Module source has no Twilio / Slack outbound / scheduler /
    worker / DB mutation imports or tokens.
  * Dispatcher integration: the wiring exists between the PAS204
    block and the PAS191 dispatch block.
  * Combined with the existing PAS203 simulation-digest aliases,
    PAS207 aliases do not collide.
"""

from __future__ import annotations

import ast
import pathlib
import re
import sys
from typing import List

import pytest


_REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


from app.services.proactive.observer_digest import FORBIDDEN_OUTPUT_TOKENS  # noqa: E402
from app.services.proactive.observer_models import ObservedSnapshot  # noqa: E402
from app.services.slack.operator_intents import _ALIAS_TABLE  # noqa: E402
from app.services.slack.proactive_digest_intent import (  # noqa: E402
    EMPTY_DIGEST_MESSAGE,
    INTENT_NEEDS_ATTENTION,
    PROACTIVE_DIGEST_ALIASES,
    build_demo_snapshot,
    format_needs_attention_response,
    match_needs_attention_intent,
    try_route_needs_attention,
)
from app.services.slack.simulation_digest_intent import (  # noqa: E402
    SIMULATION_DIGEST_ALIASES,
)


SPEC_PHRASES = (
    "what needs attention",
    "what need attention",          # PAS207-B — verb-agreement typo
    "what needs my attention",
    "what should I look at",
    "what should I look into",
    "anything slipping",
    "anything falling through",
    "anything at risk",
    "pipeline risks",
    "pipeline risk",
    "show pipeline risks",
    "show risks",
    "what is at risk",
    "what's at risk",
    "what should I handle next",
    "what needs human review",
)


# Phrases that exercise the PAS207-B bounded fuzzy recovery
# (per-token typo correction + trailing-filler strip + smart
# quote folding). Every one of these must route to PAS207.
PAS207B_FUZZY_PHRASES = (
    "anything slipping?",
    "anything slipping rn",
    "anything slipping today",
    "anything slipping now",
    "anything sliping",            # typo: sliping -> slipping
    "anything slippin",            # typo: slippin -> slipping
    "pipeline riska",              # typo: riska -> risks
    "pipeline riska?",
    "pipline risks",               # typo: pipline -> pipeline
    "pipleine risks",              # typo: pipleine -> pipeline
    "pipline riska",               # both typos
    "pipeline risks today",        # trailing filler
    "what needs attn",             # typo: attn -> attention
    "what needs atention",         # typo: atention -> attention
    "what needs humen review",     # typo: humen -> human
    "what needs human revw",       # typo: revw -> review
    "what’s at risk",         # curly apostrophe
    "WHAT'S AT RISK",              # case + straight apostrophe
)


# ──────────────────────────────────────────────────────────────────
# Phrase mapping
# ──────────────────────────────────────────────────────────────────


@pytest.mark.parametrize("phrase", SPEC_PHRASES)
def test_every_spec_phrase_matches_needs_attention(phrase: str) -> None:
    assert match_needs_attention_intent(phrase) is True


@pytest.mark.parametrize("phrase", SPEC_PHRASES)
def test_every_spec_phrase_routes_via_try_route(phrase: str) -> None:
    out = try_route_needs_attention(phrase)
    assert isinstance(out, str)
    assert out.strip() != ""


def test_matcher_is_case_and_punctuation_insensitive() -> None:
    for variant in (
        "What Needs Attention",
        "WHAT NEEDS ATTENTION!",
        "what needs attention?",
        "  what needs attention  ",
    ):
        assert match_needs_attention_intent(variant) is True


def test_matcher_returns_false_for_non_aliases() -> None:
    for phrase in (
        "",
        "stats",
        "calls today",
        "pause",
        "hot leads",
        "next action",
        "priorities",
        "what should i focus on",
        "summarize the day",
    ):
        assert match_needs_attention_intent(phrase) is False


def test_try_route_returns_none_for_non_match() -> None:
    assert try_route_needs_attention("stats") is None
    assert try_route_needs_attention("") is None
    assert try_route_needs_attention("next action") is None


# ──────────────────────────────────────────────────────────────────
# PAS191 carry-forward safety
# ──────────────────────────────────────────────────────────────────


def test_pas207_does_not_steal_pas191_next_action_phrases() -> None:
    forbidden = (
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
    for phrase in forbidden:
        assert phrase not in PROACTIVE_DIGEST_ALIASES, (
            f"PAS207 must not own PAS191 phrase '{phrase}'"
        )
        assert match_needs_attention_intent(phrase) is False, (
            f"PAS207 matcher leaked on PAS191 phrase '{phrase}'"
        )


def test_pas207_carry_forward_pas191_next_action_still_owns_those_phrases() -> None:
    # Sanity: PAS191's alias table still routes the next-action
    # phrases. PAS207 must not silently delete or shadow them.
    assert _ALIAS_TABLE.get("next action") == "next_action"
    assert _ALIAS_TABLE.get("priorities") == "next_action"
    assert _ALIAS_TABLE.get("what should i focus on") == "next_action"


def test_pas207_does_not_collide_with_pas203_simulation_aliases() -> None:
    pas203 = set(SIMULATION_DIGEST_ALIASES)
    pas207 = set(PROACTIVE_DIGEST_ALIASES)
    overlap = pas203 & pas207
    assert not overlap, f"PAS207 / PAS203 alias overlap: {overlap}"


# ──────────────────────────────────────────────────────────────────
# Output safety
# ──────────────────────────────────────────────────────────────────


def test_demo_snapshot_response_has_no_closed_vocab_tokens() -> None:
    out = try_route_needs_attention("what needs attention")
    assert out is not None
    lower = out.lower()
    for token in FORBIDDEN_OUTPUT_TOKENS:
        assert token not in lower, f"forbidden token '{token}' in output"


def test_demo_snapshot_response_does_not_mention_pas_internals() -> None:
    out = try_route_needs_attention("what needs attention")
    assert out is not None
    for internal in (
        "PAS205",
        "PAS206",
        "PAS207",
        "SIMULATION_ONLY",
        "live_behavior_changed",
        "signal_id",
        "signal_type",
        "severity",
    ):
        assert internal not in out, f"output leaked internal '{internal}'"


def test_empty_pipeline_returns_bounded_empty_message() -> None:
    empty = ObservedSnapshot(observed_at="2026-05-24T05:00:00Z")
    out = format_needs_attention_response(empty)
    assert out == EMPTY_DIGEST_MESSAGE
    assert "Nothing" in out
    assert "I have not taken any action" in out


def test_snapshot_provider_is_injectable() -> None:
    captured = {"called": False}

    def provider():
        captured["called"] = True
        return ObservedSnapshot(observed_at="2026-05-24T05:00:00Z")

    out = try_route_needs_attention("what needs attention", snapshot_provider=provider)
    assert captured["called"] is True
    assert out == EMPTY_DIGEST_MESSAGE


def test_default_snapshot_is_deterministic() -> None:
    s1 = build_demo_snapshot()
    s2 = build_demo_snapshot()
    assert s1 == s2
    assert s1.observed_at == s2.observed_at


def test_intent_constant_matches_spec_value() -> None:
    assert INTENT_NEEDS_ATTENTION == "needs_attention"


def test_alias_table_size_matches_spec() -> None:
    # PAS207-B expanded the canonical alias set to 16 entries.
    assert len(PROACTIVE_DIGEST_ALIASES) == 16
    assert len(set(PROACTIVE_DIGEST_ALIASES)) == 16  # no duplicates


# ──────────────────────────────────────────────────────────────────
# Source invariants
# ──────────────────────────────────────────────────────────────────


PAS207_INTENT_PATH = (
    _REPO_ROOT / "app" / "services" / "slack" / "proactive_digest_intent.py"
)
DISPATCHER_PATH = _REPO_ROOT / "app" / "routes" / "slack_command.py"


def _read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def test_intent_source_has_no_twilio_or_slack_outbound_imports() -> None:
    src = _read(PAS207_INTENT_PATH)
    tree = ast.parse(src)
    forbidden = {"twilio", "slack_sdk", "openai", "anthropic", "smtplib"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".")[0]
                assert root not in forbidden, (
                    f"PAS207 intent imports forbidden module: {alias.name}"
                )
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                root = node.module.split(".")[0]
                assert root not in forbidden, (
                    f"PAS207 intent imports forbidden module: {node.module}"
                )


def test_intent_source_has_no_db_mutation_methods() -> None:
    src = _read(PAS207_INTENT_PATH)
    for token in (".insert(", ".update(", ".delete(", ".upsert(", ".rpc("):
        assert token not in src, f"PAS207 intent contains '{token}'"


def test_intent_source_has_no_outbound_messaging_calls() -> None:
    src = _read(PAS207_INTENT_PATH)
    for token in (
        "send_slack_message",
        "twilio_client",
        "requests.post",
        "httpx.post",
        "send_sms",
        "send_email",
    ):
        assert token not in src, f"PAS207 intent mentions outbound token '{token}'"


def test_intent_source_has_no_scheduler_or_worker_tokens() -> None:
    src = _read(PAS207_INTENT_PATH)
    for token in (
        "apscheduler",
        "celery",
        "cron",
        "schedule_job",
        "worker.start",
    ):
        assert token not in src, f"PAS207 intent mentions scheduler/worker '{token}'"


def test_intent_source_does_not_touch_migration_artifact() -> None:
    src = _read(PAS207_INTENT_PATH)
    assert "combined_supabase_migration" not in src


def test_dispatcher_wires_pas207_after_pas191_match_before_pas204_and_dispatch() -> None:
    """PAS207-B — Dispatcher precedence:

        PAS203 fast-path
        PAS191 match
        PAS207 fast-path        ← new position (was after PAS204)
        PAS204 fast-path
        PAS191 dispatch
        LLM fallback

    Moving PAS207 ahead of PAS204 fixes the production collision
    where "pipeline riska" was captured by PAS204's safety/trust
    scorer (keys on tokens like "risk" / "risky").
    """
    src = _read(DISPATCHER_PATH)
    # PAS210 — the PAS207 needs-attention surface is now dispatched through the
    # live snapshot bridge (build_needs_attention_bridge), which wraps the
    # PAS207 matcher/renderer internally. Dispatcher precedence is unchanged.
    assert "build_needs_attention_bridge" in src, (
        "dispatcher must wire the PAS207 router (via the PAS210 bridge)"
    )
    pas203_call    = src.find("try_route_simulation_digest(text, _pas203_reports_dir)")
    pas191_match   = src.find("pas191 = match_intent(text)")
    pas207_call    = src.find("build_needs_attention_bridge(text")
    pas204_call    = src.find("build_broker_response(text)")
    pas191_dispatch = src.find("if pas191_intent != INTENT_UNKNOWN:")
    assert pas203_call    != -1, "PAS203 fast-path missing"
    assert pas191_match   != -1, "PAS191 match call missing"
    assert pas207_call    != -1, "PAS207 fast-path missing"
    assert pas204_call    != -1, "PAS204 broker conversation missing"
    assert pas191_dispatch != -1, "PAS191 dispatch branch missing"
    assert pas203_call    < pas191_match,   "PAS203 must run before PAS191 match"
    assert pas191_match   < pas207_call,    "PAS191 match must run before PAS207 fast-path"
    assert pas207_call    < pas204_call,    "PAS207 must run before PAS204 to avoid safety/trust collision"
    assert pas204_call    < pas191_dispatch, "PAS204 must run before PAS191 dispatch"
    # Only one PAS207 fast-path remains in the file (no stale copy
    # left behind from the move).
    assert src.count("build_needs_attention_bridge(text") == 1


# ──────────────────────────────────────────────────────────────────
# PAS207-B — Bounded fuzzy phrase recovery
# ──────────────────────────────────────────────────────────────────


@pytest.mark.parametrize("phrase", PAS207B_FUZZY_PHRASES)
def test_pas207b_fuzzy_phrase_routes_to_pas207(phrase: str) -> None:
    assert match_needs_attention_intent(phrase) is True, (
        f"PAS207-B fuzzy phrase should match: {phrase!r}"
    )
    out = try_route_needs_attention(phrase)
    assert isinstance(out, str) and out.strip(), (
        f"PAS207-B fuzzy phrase produced empty output: {phrase!r}"
    )


def test_pas207b_typo_recovery_does_not_capture_unrelated_safety_questions() -> None:
    """The bounded typo map deliberately fixes only specific stems.
    Unrelated PAS204 safety/trust questions ("is pas safe to use",
    "are you trustworthy", ...) must still fall through PAS207.
    """
    pas204_safety_phrases = (
        "is pas safe to use",
        "is pas safe",
        "are you safe",
        "are you trustworthy",
        "do you ever embarrass us",
        "is this approved",
        "is this risky",                 # token "risky" — PAS204 safety
        "is pas risky",
    )
    for phrase in pas204_safety_phrases:
        assert match_needs_attention_intent(phrase) is False, (
            f"PAS207 absorbed a PAS204 safety/trust phrase: {phrase!r}"
        )
        assert try_route_needs_attention(phrase) is None, (
            f"PAS207 routed a PAS204 safety/trust phrase: {phrase!r}"
        )


def test_pas207b_does_not_steal_pas191_or_pas203_known_phrases() -> None:
    """PAS191 next_action / priorities / next_steps phrases and
    PAS203's simulation_digest phrases must remain on their own
    surfaces even with the expanded matcher.
    """
    for phrase in (
        "next action",
        "next actions",
        "next steps",
        "priorities",
        "top priorities",
        "what should i do now",
        "what should i focus on",
        "what's the priority",
        "stats",
        "calls today",
        "leads today",
        "summary",
        "hot leads",
        "simulation digest",
        "show the digest",
        "evidence digest",
    ):
        assert match_needs_attention_intent(phrase) is False, (
            f"PAS207-B leaked on {phrase!r}"
        )
        assert try_route_needs_attention(phrase) is None


def test_pas207b_does_not_capture_mutation_commands() -> None:
    for phrase in (
        "pause",
        "resume",
        "push 123 Main St $500k 3 bed",
        "remove 123 Main St",
    ):
        assert match_needs_attention_intent(phrase) is False
        assert try_route_needs_attention(phrase) is None


def test_pas207b_token_typo_map_is_closed_and_bounded() -> None:
    """Sanity check: import the typo map directly and confirm it
    contains only the documented stems. A broader map would risk
    absorbing unrelated phrases.
    """
    from app.services.slack.proactive_digest_intent import _TOKEN_TYPO_MAP
    expected = {
        "riska":    "risks",
        "pipline":  "pipeline",
        "pipleine": "pipeline",
        "sliping":  "slipping",
        "slippin":  "slipping",
        "attn":     "attention",
        "atention": "attention",
        "revw":     "review",
        "humen":    "human",
    }
    assert dict(_TOKEN_TYPO_MAP) == expected


def test_pas207b_trailing_filler_strip_is_closed_and_bounded() -> None:
    from app.services.slack.proactive_digest_intent import _TRAILING_FILLER_TOKENS
    assert set(_TRAILING_FILLER_TOKENS) == {"rn", "today", "now", "please"}


def test_pas207b_normaliser_does_not_force_risk_plural_globally() -> None:
    """The token map must NOT rewrite the bare singular "risk" to
    "risks" globally — that would break the canonical aliases
    "what is at risk" and "pipeline risk".
    """
    from app.services.slack.proactive_digest_intent import _TOKEN_TYPO_MAP
    assert "risk" not in _TOKEN_TYPO_MAP
    assert match_needs_attention_intent("what is at risk") is True
    assert match_needs_attention_intent("pipeline risk") is True


def test_dispatcher_logs_pas207_intent_match() -> None:
    src = _read(DISPATCHER_PATH)
    assert '"intent":       "needs_attention"' in src or '"intent": "needs_attention"' in src, (
        "dispatcher should log a needs_attention intent match"
    )
    assert "slack_command_pas207" in src, (
        "dispatcher should attribute the surface to PAS207"
    )
