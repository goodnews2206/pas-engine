"""
PAS193 — Deterministic conversation adapter.

A rule-based, in-process player that walks each scenario through a
canned PAS-shaped action sequence. It produces a transcript and a
record of which capabilities (qualification, appointment attempt,
callback capture, objection handling) fired during the run.

Strict properties (enforced by tests and the readiness gate):

  * Imports nothing from Twilio, Slack, Supabase, OpenAI,
    Anthropic, or dotenv. No network calls. No file I/O.
  * Pure function: same input -> same output every call.
  * Never generates phone numbers, emails, or real addresses in
    its output utterances.
  * Mirrors PAS's call doctrine: PAS may try to qualify, attempt
    booking, offer callback, and handle objections. PAS must
    refuse to poach when the lead already has an agent and must
    fail safely on a language it does not support.

This adapter does NOT execute app.engine.state_machine. The state
machine is intentionally bypassed for offline rehearsal because it
binds to Twilio + Supabase. PAS193 is the proof that a rehearsal
layer exists; PAS194 will close the gap by routing the same
scenario surface through the real engine under a stub transport.
"""

from __future__ import annotations

from typing import Dict, List, Tuple


# ──────────────────────────────────────────────────────────────────
# Action vocabulary
# ──────────────────────────────────────────────────────────────────

AGENT_ACTIONS: Tuple[str, ...] = (
    "greet",
    "ask_intent",
    "qualify",
    "offer_appointment",
    "offer_callback",
    "handle_objection",
    "respect_channel_preference",
    "polite_disengage",
    "decline_unsupported_language",
    "close",
)


# Canned PAS responses, indexed by action. These are deliberately
# bland so the transcript reads as a rehearsal harness rather than
# a polished sales script. The rehearsal layer is proving the
# action sequence, not the wording.
_AGENT_LINES: Dict[str, str] = {
    "greet":                        "Thanks for reaching out — happy to help.",
    "ask_intent":                   "Could you share a bit about what you're looking for?",
    "qualify":                      "To make sure I route this to the right person, could I ask a few quick questions?",
    "offer_appointment":            "Would you like me to set up a time with one of our agents?",
    "offer_callback":               "I can have an agent call you back at a time that works for you — when's good?",
    "handle_objection":             "That's a fair concern — let me make sure we get you to someone who can address it.",
    "respect_channel_preference":   "Got it — I'll make sure follow-up goes by text rather than a call.",
    "polite_disengage":             "Understood — I won't try to redirect you away from the agent you're working with.",
    "decline_unsupported_language": "I can't continue in that language yet — let me arrange for someone who can to call you back.",
    "close":                        "Thanks — an agent will be in touch shortly.",
}


# Per-scenario action plan. This is the deterministic policy the
# adapter follows turn-by-turn. The plan is keyed by scenario_type
# (not scenario_id) so adding a new scenario of an existing type
# inherits the right action plan automatically.
_ACTION_PLAN_BY_TYPE: Dict[str, Tuple[str, ...]] = {
    "high_intent_buyer":        ("greet", "qualify", "offer_appointment", "close"),
    "skeptical_seller":         ("greet", "handle_objection", "qualify", "offer_callback", "close"),
    "zillow_browse":            ("greet", "ask_intent", "qualify", "offer_callback", "close"),
    "investor":                 ("greet", "qualify", "offer_appointment", "close"),
    "first_time_buyer":         ("greet", "qualify", "offer_appointment", "close"),
    "callback_request":         ("greet", "qualify", "offer_callback", "close"),
    "price_objection":          ("greet", "handle_objection", "offer_callback", "close"),
    "already_has_agent":        ("greet", "polite_disengage", "handle_objection", "close"),
    "not_ready_yet":            ("greet", "qualify", "offer_callback", "close"),
    "text_only":                ("greet", "respect_channel_preference", "qualify", "offer_callback", "handle_objection", "close"),
    "refuses_qualification":    ("greet", "handle_objection", "offer_callback", "close"),
    "commission_question":      ("greet", "handle_objection", "close"),
    "open_house_follow_up":     ("greet", "qualify", "offer_appointment", "close"),
    "late_night":               ("greet", "qualify", "offer_callback", "close"),
    "cold_revival":             ("greet", "qualify", "offer_callback", "close"),
    "urgent_showing":           ("greet", "qualify", "offer_appointment", "close"),
    "relocation":               ("greet", "qualify", "offer_appointment", "offer_callback", "close"),
    "luxury":                   ("greet", "qualify", "offer_appointment", "close"),
    "rental":                   ("greet", "handle_objection", "close"),
    "language_unsupported":     ("greet", "decline_unsupported_language", "handle_objection", "offer_callback", "close"),
}


# Capability tokens the adapter records when a given action fires.
# These tokens are exactly the controlled vocabulary the scoring
# engine pattern-matches against scenario.success_criteria.
_ACTION_CAPABILITIES: Dict[str, Tuple[str, ...]] = {
    "qualify":                      ("qualification_captured",),
    "offer_appointment":            ("appointment_attempted",),
    "offer_callback":               ("callback_captured",),
    "handle_objection":             ("objection_handled",),
    "respect_channel_preference":   ("objection_handled",),
    "polite_disengage":             ("objection_handled",),
    "decline_unsupported_language": ("objection_handled",),
    "close":                        ("conversation_completed",),
}


# ──────────────────────────────────────────────────────────────────
# Runner
# ──────────────────────────────────────────────────────────────────

def _agent_line(action: str) -> str:
    return _AGENT_LINES[action]


def _plan_for(scenario_type: str) -> Tuple[str, ...]:
    return _ACTION_PLAN_BY_TYPE.get(
        scenario_type,
        ("greet", "ask_intent", "qualify", "offer_callback", "close"),
    )


def _build_transcript(
    scenario: Dict,
    plan: Tuple[str, ...],
) -> Tuple[List[Dict], List[str], List[str]]:
    """
    Walk the action plan against the scenario's lead_script and
    return (turns, actions_taken, capabilities_fired).
    """
    turns: List[Dict] = []
    actions_taken: List[str] = []
    capabilities: List[str] = []

    lead_script = scenario.get("lead_script") or ()
    lead_turn_idx = 0
    plan_idx = 0

    while plan_idx < len(plan) and lead_turn_idx < max(len(lead_script), len(plan)):
        action = plan[plan_idx]
        agent_text = _agent_line(action)

        lead_text = ""
        if lead_turn_idx < len(lead_script):
            lead_text = lead_script[lead_turn_idx]

        turns.append({
            "turn":         len(turns) + 1,
            "agent_action": action,
            "agent_text":   agent_text,
            "lead_text":    lead_text,
        })
        actions_taken.append(action)
        for cap in _ACTION_CAPABILITIES.get(action, ()):
            if cap not in capabilities:
                capabilities.append(cap)

        plan_idx += 1
        lead_turn_idx += 1

    return turns, actions_taken, capabilities


def run_scenario(scenario: Dict) -> Dict:
    """
    Execute one rehearsal of `scenario`. Returns a record carrying
    the transcript, action sequence, capabilities, and a small
    `safety` block reflecting that no unsafe claim, PII, or
    hallucinated policy was emitted by the adapter (because by
    construction the adapter only emits canned lines).

    For unsupported scenarios, the run still happens but the
    safety block flags `supported=False` so scoring can apply the
    correct policy.
    """
    plan = _plan_for(scenario["scenario_type"])
    turns, actions, capabilities = _build_transcript(scenario, plan)

    return {
        "scenario_id":       scenario["scenario_id"],
        "scenario_type":     scenario["scenario_type"],
        "supported":         scenario["supported"],
        "expected_goal":     scenario["expected_goal"],
        "turns":             turns,
        "actions":           actions,
        "capabilities":      capabilities,
        "agent_utterances":  [t["agent_text"] for t in turns],
        "lead_utterances":   [t["lead_text"]  for t in turns],
        "safety": {
            "unsafe_claim":        False,
            "pii_leak":            False,
            "hallucinated_policy": False,
            "agent_poaching":      False,
            "qualification_pressure": False,
            "language_misclaim":   False,
        },
    }


def run_batch(scenarios: Tuple[Dict, ...]) -> List[Dict]:
    return [run_scenario(s) for s in scenarios]
