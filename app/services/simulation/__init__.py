"""
PAS193 — Simulation Layer Proof.

Deterministic, offline rehearsal layer for PAS lead conversations.
Never imports Twilio, Slack, or live LLM clients. Never reads .env,
never touches Supabase, never mutates production brokerage state.

Public surface:
    SCENARIOS, SUPPORTED_SCENARIOS, UNSUPPORTED_SCENARIOS,
    SCENARIO_INDEX, scenario_count                — scenarios
    run_scenario, run_batch                       — adapter
    score_conversation, ScoreResult, FAILURE_*    — scoring
    build_report, REPORT_REQUIRED_KEYS            — report
"""

from app.services.simulation.scenarios import (  # noqa: F401
    SCENARIOS,
    SCENARIO_INDEX,
    SUPPORTED_SCENARIOS,
    UNSUPPORTED_SCENARIOS,
    SCENARIO_REQUIRED_KEYS,
    SCENARIO_TYPES,
    scenario_count,
)
from app.services.simulation.adapter import (  # noqa: F401
    AGENT_ACTIONS,
    run_scenario,
    run_batch,
)
from app.services.simulation.scoring import (  # noqa: F401
    FAILURE_REASONS,
    RECOMMENDATION_LABELS,
    ScoreResult,
    score_conversation,
)
from app.services.simulation.report import (  # noqa: F401
    REPORT_REQUIRED_KEYS,
    build_report,
)
