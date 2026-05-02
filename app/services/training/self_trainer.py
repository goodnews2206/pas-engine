"""
PAS Self-Trainer

After every TRAINING_THRESHOLD calls, the configured LLM (via the provider
abstraction) reads recent transcripts for a brokerage, identifies what
worked vs. what didn't, and writes improved scripts back into the
brokerage's training_config. The engine loads these on the next call.

Training loop:
  1. Pull last N completed calls with transcripts
  2. Split by outcome (booked / not_booked)
  3. LLM analyses patterns and writes improved prompts
  4. Store result in brokerages.training_config + log to training_logs
  5. Increment training_version

The engine uses training_config.booking_prompt and training_config.objection_system_prompt
as drop-in replacements for the defaults — only if they exist.
"""

import json
import logging
from datetime import datetime, timezone

from app.db.supabase_client import get_supabase
from app.services.llm.factory import get_provider

logger = logging.getLogger("pas.trainer")

TRAINING_THRESHOLD = 25   # retrain after every N calls
MAX_TRANSCRIPTS = 30      # transcripts to feed the LLM (context budget)

_ANALYSIS_SYSTEM = """You are a conversion optimisation analyst for a real estate AI phone agent.
You will receive transcripts of real calls — some that ended in a booked property viewing,
some that did not.

Your job:
1. Identify patterns in successful calls (what language, what pace, what pivots worked)
2. Identify the most common failure point (which state/question caused drop-offs)
3. Identify the top 3 objections and how they were handled
4. Write an improved BOOKING_PROMPT (the line that asks the lead to book a viewing)
5. Write improved OBJECTION_SYSTEM_PROMPT (instructions for the objection-handling LLM call)

Rules for the prompts you write:
- Sound natural and human, not salesy
- Be concise — the booking prompt should be one sentence
- The objection prompt should be ≤120 words of instructions

Respond with valid JSON only — no prose outside the JSON block:
{
  "insights": {
    "calls_analyzed": <int>,
    "booked": <int>,
    "not_booked": <int>,
    "booking_rate": <float 0-1>,
    "top_dropout_state": "<GREETING|INTENT|BUDGET|TIMELINE|BOOKING>",
    "common_objections": ["<obj1>", "<obj2>", "<obj3>"],
    "what_works": "<one sentence>",
    "what_doesnt": "<one sentence>"
  },
  "booking_prompt": "<improved booking question>",
  "objection_system_prompt": "<improved objection handler instructions>"
}"""


async def maybe_train(brokerage_id: str, current_call_count: int) -> bool:
    """
    Called after each call. Triggers training when the threshold is crossed.
    Returns True if training ran.
    """
    if current_call_count == 0 or current_call_count % TRAINING_THRESHOLD != 0:
        return False

    logger.info(f"Training threshold reached for {brokerage_id} at {current_call_count} calls")
    await run_training(brokerage_id)
    return True


async def run_training(brokerage_id: str) -> dict:
    """
    Run a full training cycle for one brokerage.
    Returns the new training_config dict.
    """
    logger.info(f"Starting self-training for brokerage={brokerage_id}")

    transcripts = _fetch_recent_transcripts(brokerage_id, limit=MAX_TRANSCRIPTS)
    if len(transcripts) < 5:
        logger.info(f"Not enough transcripts ({len(transcripts)}) to train — skipping")
        return {}

    booked = [t for t in transcripts if t["outcome"] == "booked"]
    not_booked = [t for t in transcripts if t["outcome"] != "booked"]

    user_message = _build_analysis_prompt(booked, not_booked)

    provider = get_provider()
    if provider is None:
        logger.warning("No LLM provider available — skipping training")
        return {}

    try:
        raw = await provider.chat(
            system=_ANALYSIS_SYSTEM,
            user=user_message,
            max_tokens=800,
            temperature=0.3,
            purpose="training",
        )
        raw = raw.strip()
        # Strip markdown code fences if the model wrapped the JSON
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        result = json.loads(raw)

        # Schema validation — reject silently malformed training output
        # rather than saving corrupted prompts to the DB
        required_keys = {"insights", "booking_prompt", "objection_system_prompt"}
        if not required_keys.issubset(result.keys()):
            logger.error(f"Training output missing required keys: {required_keys - result.keys()}")
            return {}
        booking_prompt = result.get("booking_prompt", "")
        objection_prompt = result.get("objection_system_prompt", "")
        if not isinstance(booking_prompt, str) or len(booking_prompt) < 10:
            logger.error("Training produced invalid booking_prompt — discarding")
            return {}
        if not isinstance(objection_prompt, str) or len(objection_prompt) < 10:
            logger.error("Training produced invalid objection_system_prompt — discarding")
            return {}

    except Exception as e:
        logger.error(f"[{provider.name}] training analysis failed: {e}")
        return {}

    training_config = {
        "booking_prompt": result["booking_prompt"],
        "objection_system_prompt": result["objection_system_prompt"],
        "insights": result.get("insights", {}),
        "trained_at": datetime.now(timezone.utc).isoformat(),
    }

    _save_training_config(brokerage_id, training_config, result.get("insights", {}))
    logger.info(f"Training complete for {brokerage_id} | rate={result.get('insights', {}).get('booking_rate', '?')}")
    return training_config


def _fetch_recent_transcripts(brokerage_id: str, limit: int) -> list:
    try:
        db = get_supabase()
        result = (
            db.table("calls")
            .select("outcome, transcript, duration_seconds")
            .eq("brokerage_id", brokerage_id)
            .eq("call_status", "completed")
            .not_.is_("transcript", "null")
            .order("start_time", desc=True)
            .limit(limit)
            .execute()
        )
        return result.data or []
    except Exception as e:
        logger.error(f"Failed to fetch transcripts for training: {e}")
        return []


def _build_analysis_prompt(booked: list, not_booked: list) -> str:
    def fmt(calls: list, label: str) -> str:
        if not calls:
            return f"--- {label}: none ---"
        parts = [f"--- {label} ({len(calls)} calls) ---"]
        for i, c in enumerate(calls[:15], 1):  # cap per category
            parts.append(f"\n[Call {i}]\n{c.get('transcript', '(no transcript)')}")
        return "\n".join(parts)

    return (
        f"Total calls: {len(booked) + len(not_booked)}\n\n"
        + fmt(booked, "BOOKED — viewing confirmed")
        + "\n\n"
        + fmt(not_booked, "NOT BOOKED — lead dropped off")
    )


def _save_training_config(brokerage_id: str, training_config: dict, insights: dict):
    try:
        db = get_supabase()
        # Increment training_version
        brokerage = (
            db.table("brokerages").select("training_version").eq("id", brokerage_id).limit(1).execute()
        )
        current_version = (brokerage.data[0].get("training_version") or 0) if brokerage.data else 0
        new_version = current_version + 1

        db.table("brokerages").update({
            "training_config": training_config,
            "training_version": new_version,
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }).eq("id", brokerage_id).execute()

        # Log to training_logs
        db.table("training_logs").insert({
            "brokerage_id": brokerage_id,
            "version": new_version,
            "calls_analyzed": insights.get("calls_analyzed", 0),
            "booking_rate": insights.get("booking_rate"),
            "insights": insights,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }).execute()

        logger.info(f"Training config saved | brokerage={brokerage_id} | version={new_version}")
    except Exception as e:
        logger.error(f"Failed to save training config: {e}")
