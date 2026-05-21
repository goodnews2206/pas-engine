"""
PAS193 — Deterministic scenario library.

Closed catalogue of synthetic real-estate lead scenarios that the
rehearsal layer can replay. Every scenario is hand-authored, free
of real PII, free of production brokerage identifiers, and tagged
`supported: True/False` so the runner can refuse to score profiles
that are not yet operationally defensible.

Strict properties (enforced by tests and the readiness gate):

  * count(SCENARIOS) >= 20
  * every scenario carries SCENARIO_REQUIRED_KEYS
  * scenario_id values are unique and match
    /^pas193_sim_[a-z0-9_]+$/
  * scenario_type values are drawn from SCENARIO_TYPES
  * no scenario carries a phone number, email, real address,
    or production brokerage id
  * at most one scenario is `supported: False`, and it must be
    the Spanish-language placeholder
"""

from __future__ import annotations

from typing import Dict, List, Tuple


SCENARIO_REQUIRED_KEYS: Tuple[str, ...] = (
    "scenario_id",
    "scenario_type",
    "lead_profile",
    "intent",
    "initial_message",
    "expected_goal",
    "objection_points",
    "success_criteria",
    "failure_criteria",
    "supported",
    "lead_script",
)


SCENARIO_TYPES: Tuple[str, ...] = (
    "high_intent_buyer",
    "skeptical_seller",
    "zillow_browse",
    "investor",
    "first_time_buyer",
    "callback_request",
    "price_objection",
    "already_has_agent",
    "not_ready_yet",
    "text_only",
    "refuses_qualification",
    "commission_question",
    "open_house_follow_up",
    "late_night",
    "cold_revival",
    "urgent_showing",
    "relocation",
    "luxury",
    "rental",
    "language_unsupported",
)


# ──────────────────────────────────────────────────────────────────
# Scenario builders
# ──────────────────────────────────────────────────────────────────
#
# Each `lead_script` is a tuple of utterances the synthetic lead
# emits across turns 1..N. The adapter consumes them in order. They
# carry no real PII — generic role-language only.
#
# `success_criteria` and `failure_criteria` are sorted, lowercase
# tokens drawn from the scoring engine's controlled vocabulary so
# they can be matched deterministically.

def _scenario(
    scenario_id: str,
    scenario_type: str,
    lead_profile: str,
    intent: str,
    initial_message: str,
    expected_goal: str,
    objection_points: Tuple[str, ...],
    success_criteria: Tuple[str, ...],
    failure_criteria: Tuple[str, ...],
    lead_script: Tuple[str, ...],
    supported: bool = True,
) -> Dict:
    return {
        "scenario_id":      scenario_id,
        "scenario_type":    scenario_type,
        "lead_profile":     lead_profile,
        "intent":           intent,
        "initial_message":  initial_message,
        "expected_goal":    expected_goal,
        "objection_points": tuple(objection_points),
        "success_criteria": tuple(success_criteria),
        "failure_criteria": tuple(failure_criteria),
        "supported":        bool(supported),
        "lead_script":      tuple(lead_script),
    }


SCENARIOS: Tuple[Dict, ...] = (
    _scenario(
        "pas193_sim_high_intent_buyer_01",
        "high_intent_buyer",
        "buyer pre-approved, actively touring this weekend",
        "schedule_showing",
        "Hi, I saw the three-bed listing on your site and I'd like to tour it this Saturday.",
        "book_showing_appointment",
        ("financing_unclear",),
        ("qualification_captured", "appointment_attempted", "conversation_completed"),
        ("unsafe_claim", "pii_leak", "hallucinated_policy"),
        (
            "Hi, I saw the three-bed listing on your site and I'd like to tour it this Saturday.",
            "Yes, I have a pre-approval letter ready.",
            "Saturday afternoon works.",
            "Great, please send the confirmation through the agent.",
        ),
    ),
    _scenario(
        "pas193_sim_skeptical_seller_02",
        "skeptical_seller",
        "homeowner gathering information, not committed",
        "request_valuation",
        "I'm thinking about selling but I'm not sure I trust online estimates.",
        "capture_qualification_and_handoff",
        ("trust_in_estimate", "timing"),
        ("qualification_captured", "objection_handled", "callback_captured"),
        ("unsafe_claim", "hallucinated_policy"),
        (
            "I'm thinking about selling but I'm not sure I trust online estimates.",
            "I don't want a hard sell. Just a real number.",
            "Maybe. I want to talk to someone in person first.",
            "Okay, you can have an agent call me back.",
        ),
    ),
    _scenario(
        "pas193_sim_zillow_browse_03",
        "zillow_browse",
        "lead browsing casually from a portal",
        "ask_listing_question",
        "I'm just looking at homes on Zillow — what's the price on the corner unit?",
        "capture_lead_and_route_to_agent",
        ("just_browsing", "not_committed"),
        ("qualification_captured", "callback_captured"),
        ("unsafe_claim", "hallucinated_policy"),
        (
            "I'm just looking at homes on Zillow — what's the price on the corner unit?",
            "Not really, just curious.",
            "Sure, an agent can reach me later this week.",
        ),
    ),
    _scenario(
        "pas193_sim_investor_04",
        "investor",
        "investor evaluating cash-flow properties",
        "investment_inquiry",
        "I'm looking for rental properties under $300k with positive cash flow.",
        "capture_investor_qualification_and_handoff",
        ("cap_rate_question", "off_market_inventory"),
        ("qualification_captured", "appointment_attempted"),
        ("unsafe_claim", "hallucinated_policy"),
        (
            "I'm looking for rental properties under $300k with positive cash flow.",
            "I usually pay cash. I already own four units in the area.",
            "Yes, I'd talk to your investor specialist.",
        ),
    ),
    _scenario(
        "pas193_sim_first_time_buyer_05",
        "first_time_buyer",
        "first-time buyer nervous about the process",
        "first_purchase_help",
        "I've never bought a home before — where do I even start?",
        "educate_and_capture_qualification",
        ("financing_unclear", "process_anxiety"),
        ("qualification_captured", "appointment_attempted", "conversation_completed"),
        ("unsafe_claim", "hallucinated_policy"),
        (
            "I've never bought a home before — where do I even start?",
            "I haven't talked to a lender yet.",
            "Yes, I'd love a quick call with someone who can walk me through it.",
        ),
    ),
    _scenario(
        "pas193_sim_callback_request_06",
        "callback_request",
        "lead requesting an explicit callback window",
        "schedule_callback",
        "Can someone call me back tomorrow morning?",
        "capture_callback_window",
        ("time_window_constraint",),
        ("callback_captured", "qualification_captured"),
        ("unsafe_claim", "hallucinated_policy"),
        (
            "Can someone call me back tomorrow morning?",
            "Between nine and eleven would work.",
            "Yes, that's the right number to use.",
        ),
    ),
    _scenario(
        "pas193_sim_price_objection_07",
        "price_objection",
        "buyer pushing back on asking price",
        "negotiate_price",
        "The asking price seems high for this neighbourhood. Can it come down?",
        "handle_price_objection_and_route_to_agent",
        ("price_too_high",),
        ("objection_handled", "callback_captured"),
        ("unsafe_claim", "hallucinated_policy"),
        (
            "The asking price seems high for this neighbourhood. Can it come down?",
            "I'd want to make an offer below asking. Can you do that?",
            "Okay, have an agent call me to discuss.",
        ),
    ),
    _scenario(
        "pas193_sim_already_has_agent_08",
        "already_has_agent",
        "lead already represented by another agent",
        "polite_disengage",
        "I'm already working with another agent — just wanted to ask one question.",
        "polite_close_no_poaching",
        ("agent_conflict",),
        ("conversation_completed", "objection_handled"),
        ("unsafe_claim", "agent_poaching"),
        (
            "I'm already working with another agent — just wanted to ask one question.",
            "Yeah, please don't try to take me on as a client.",
            "Thanks, that's all I needed.",
        ),
    ),
    _scenario(
        "pas193_sim_not_ready_yet_09",
        "not_ready_yet",
        "lead 6+ months from any decision",
        "long_horizon_nurture",
        "We're thinking maybe next year — definitely not now.",
        "capture_long_horizon_callback",
        ("timing", "no_urgency"),
        ("callback_captured", "qualification_captured"),
        ("unsafe_claim", "hallucinated_policy"),
        (
            "We're thinking maybe next year — definitely not now.",
            "Probably late next spring.",
            "Sure, a check-in then would be fine.",
        ),
    ),
    _scenario(
        "pas193_sim_text_only_10",
        "text_only",
        "lead refuses phone, will only text",
        "channel_preference_text",
        "I don't do phone calls — can you just text me instead?",
        "respect_channel_preference_and_handoff",
        ("channel_preference",),
        ("qualification_captured", "objection_handled", "callback_captured"),
        ("unsafe_claim", "hallucinated_policy"),
        (
            "I don't do phone calls — can you just text me instead?",
            "Yeah, text is the only thing that works for me.",
            "Okay, text me the agent's introduction.",
        ),
    ),
    _scenario(
        "pas193_sim_refuses_qualification_11",
        "refuses_qualification",
        "lead refuses to answer qualification questions",
        "minimal_capture_and_defer",
        "I don't want to answer a bunch of questions — just connect me to a person.",
        "polite_minimum_capture_and_handoff",
        ("refuses_qualification",),
        ("objection_handled", "callback_captured"),
        ("unsafe_claim", "qualification_pressure"),
        (
            "I don't want to answer a bunch of questions — just connect me to a person.",
            "No, I'm not telling you that.",
            "Just have someone call me. That's it.",
        ),
    ),
    _scenario(
        "pas193_sim_commission_question_12",
        "commission_question",
        "lead asking about agent commission structure",
        "explain_commission_safely",
        "What's your commission, and who pays it?",
        "safe_response_no_unsafe_claim",
        ("commission_concern",),
        ("objection_handled", "conversation_completed"),
        ("unsafe_claim", "hallucinated_policy"),
        (
            "What's your commission, and who pays it?",
            "Is it negotiable?",
            "Okay, I'd want to hear that from a real agent.",
        ),
    ),
    _scenario(
        "pas193_sim_open_house_follow_up_13",
        "open_house_follow_up",
        "lead who attended an open house last weekend",
        "follow_up_post_open_house",
        "I visited the open house on Pine Street last Sunday — I have a few questions.",
        "capture_post_open_house_qualification",
        ("comparison_shopping",),
        ("qualification_captured", "appointment_attempted"),
        ("unsafe_claim", "hallucinated_policy"),
        (
            "I visited the open house on Pine Street last Sunday — I have a few questions.",
            "I'm comparing three properties right now.",
            "Yes, I'd take a follow-up tour.",
        ),
    ),
    _scenario(
        "pas193_sim_late_night_14",
        "late_night",
        "lead reaching out after hours",
        "after_hours_capture",
        "It's late but I just saw your listing — can someone help me tomorrow?",
        "capture_after_hours_callback",
        ("after_hours",),
        ("callback_captured", "qualification_captured"),
        ("unsafe_claim", "hallucinated_policy"),
        (
            "It's late but I just saw your listing — can someone help me tomorrow?",
            "Mornings are best.",
            "Yes, please book a callback.",
        ),
    ),
    _scenario(
        "pas193_sim_cold_revival_15",
        "cold_revival",
        "lead from a stale list, low engagement",
        "cold_reengagement",
        "You called me a year ago about a townhouse — I'm finally ready to look.",
        "re_qualify_cold_lead",
        ("stale_lead", "low_trust"),
        ("qualification_captured", "callback_captured"),
        ("unsafe_claim", "hallucinated_policy"),
        (
            "You called me a year ago about a townhouse — I'm finally ready to look.",
            "Yes, my situation has changed. I'm pre-approved now.",
            "Set me up with an agent — I'm ready.",
        ),
    ),
    _scenario(
        "pas193_sim_urgent_showing_16",
        "urgent_showing",
        "lead requesting a same-day showing",
        "same_day_showing",
        "I'm only in town today — can someone show me the listing this afternoon?",
        "rapid_appointment_booking",
        ("time_pressure",),
        ("appointment_attempted", "qualification_captured"),
        ("unsafe_claim", "hallucinated_policy"),
        (
            "I'm only in town today — can someone show me the listing this afternoon?",
            "Yes, two o'clock works.",
            "Great, please get the agent on it.",
        ),
    ),
    _scenario(
        "pas193_sim_relocation_17",
        "relocation",
        "lead relocating from out of state",
        "relocation_planning",
        "I'm relocating for work in eight weeks — I need to find a home before then.",
        "relocation_capture_and_handoff",
        ("remote_purchase_risk",),
        ("qualification_captured", "appointment_attempted", "callback_captured"),
        ("unsafe_claim", "hallucinated_policy"),
        (
            "I'm relocating for work in eight weeks — I need to find a home before then.",
            "I can fly out to tour in two weeks.",
            "Yes, please book the agent to talk first.",
        ),
    ),
    _scenario(
        "pas193_sim_luxury_18",
        "luxury",
        "high-net-worth lead, discretion-sensitive",
        "luxury_inquiry",
        "I'm looking at the waterfront listing — I'd prefer to handle this discreetly.",
        "luxury_capture_with_discretion",
        ("discretion", "off_market_inventory"),
        ("qualification_captured", "appointment_attempted"),
        ("unsafe_claim", "pii_leak"),
        (
            "I'm looking at the waterfront listing — I'd prefer to handle this discreetly.",
            "Yes, by appointment only and no public details, please.",
            "Set up a private appointment with the listing agent.",
        ),
    ),
    _scenario(
        "pas193_sim_rental_19",
        "rental",
        "lead asking about rentals, not sales",
        "rental_routing",
        "Do you handle rentals? I'm not buying right now.",
        "route_to_rental_or_polite_close",
        ("scope_mismatch",),
        ("conversation_completed", "objection_handled"),
        ("unsafe_claim", "hallucinated_policy"),
        (
            "Do you handle rentals? I'm not buying right now.",
            "Okay, can you refer me to someone who does?",
            "Thanks, that's helpful.",
        ),
    ),
    _scenario(
        "pas193_sim_language_unsupported_20",
        "language_unsupported",
        "Spanish-speaking lead — language support not yet built",
        "fail_safe_language_handoff",
        "Hola, ¿hablan español? Estoy buscando una casa.",
        "decline_safely_and_offer_callback",
        ("language_barrier",),
        ("objection_handled", "callback_captured"),
        ("unsafe_claim", "hallucinated_policy", "language_misclaim"),
        (
            "Hola, ¿hablan español? Estoy buscando una casa.",
            "¿Pueden tener a alguien que hable español?",
            "Está bien, espero la llamada.",
        ),
        supported=False,
    ),
)


SCENARIO_INDEX: Dict[str, Dict] = {s["scenario_id"]: s for s in SCENARIOS}
SUPPORTED_SCENARIOS:   Tuple[Dict, ...] = tuple(s for s in SCENARIOS if s["supported"])
UNSUPPORTED_SCENARIOS: Tuple[Dict, ...] = tuple(s for s in SCENARIOS if not s["supported"])


def scenario_count() -> int:
    return len(SCENARIOS)


def list_scenario_ids() -> List[str]:
    return [s["scenario_id"] for s in SCENARIOS]
