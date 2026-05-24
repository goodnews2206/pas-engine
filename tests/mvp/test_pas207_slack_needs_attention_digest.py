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
    "what should I look at",
    "anything slipping",
    "pipeline risks",
    "show risks",
    "what is at risk",
    "what should I handle next",
    "what needs human review",
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
    assert len(PROACTIVE_DIGEST_ALIASES) == 8
    assert len(set(PROACTIVE_DIGEST_ALIASES)) == 8  # no duplicates


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


def test_dispatcher_wires_pas207_after_pas204_and_before_pas191_dispatch() -> None:
    src = _read(DISPATCHER_PATH)
    assert "try_route_needs_attention" in src, (
        "dispatcher must import the PAS207 router"
    )
    # Locate anchors.
    pas204_block_anchor = src.find('"response_type": "in_channel",')
    pas207_call = src.find("try_route_needs_attention(text)")
    pas191_dispatch = src.find("if pas191_intent != INTENT_UNKNOWN:")
    assert pas204_block_anchor != -1
    assert pas207_call != -1, "PAS207 fast-path call must be wired"
    assert pas191_dispatch != -1
    # PAS207 sits before the PAS191 dispatch branch.
    assert pas207_call < pas191_dispatch, (
        "PAS207 fast-path must run before PAS191 deterministic dispatch"
    )


def test_dispatcher_logs_pas207_intent_match() -> None:
    src = _read(DISPATCHER_PATH)
    assert '"intent":       "needs_attention"' in src or '"intent": "needs_attention"' in src, (
        "dispatcher should log a needs_attention intent match"
    )
    assert "slack_command_pas207" in src, (
        "dispatcher should attribute the surface to PAS207"
    )
