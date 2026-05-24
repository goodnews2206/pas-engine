"""
Slack Command Interface — brokerages control PAS in plain English.

Setup: Create a Slack app → Slash Commands → point /pas to POST /slack/command
       Add the Signing Secret to the brokerage record in Supabase.

Supported commands (natural language, the configured LLM interprets them):
  /pas pause                          → stop making outbound calls
  /pas resume                         → start making outbound calls
  /pas push 123 Main St, $500k, 3bed  → add a featured property
  /pas remove 123 Main St             → remove a featured property
  /pas calls today                    → summary of today's calls
  /pas hot leads                      → leads booked in last 7 days
  /pas stats                          → conversion rate + totals
"""

import hashlib
import hmac
import json
import logging
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path  # PAS203-A — locate reports/simulations/ digest dir.

from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse

from app.db.brokerage_store import (
    get_brokerage_by_slack_team,
    set_brokerage_active,
    update_featured_properties,
)
from app.db.event_logger import log_event_bg
from app.db.supabase_client import get_supabase
from app.services.llm.factory import get_provider
from app.services.notifications.slack_client import send_slack_message
# PAS191 — Bounded Slack natural-language operator commands.
# Deterministic fast-path: closed alias table → closed intent code →
# safe formatter. NO LLM for these 12 read-only intents.
from app.services.slack.operator_intents import (
    INTENT_BOOKINGS_TODAY,
    INTENT_CALLBACKS_DUE,
    INTENT_CALLS_TODAY,
    INTENT_CALLS_WEEK,
    INTENT_HEALTH,
    INTENT_HELP,
    INTENT_INCIDENTS,
    INTENT_LEADS_TODAY,
    INTENT_NEXT_ACTION,
    INTENT_PAUSED_STATUS,
    INTENT_POLICY,
    INTENT_QUEUE,
    INTENT_RESPONSE_RATE,
    INTENT_STATS,
    INTENT_TODAY_SUMMARY,
    INTENT_UNKNOWN,
    match_intent,
)
from app.services.slack import operator_responses as pas191_responses
# PAS203-A — read-only simulation evidence digest intent. Pure
# string output: no Slack API call, no digest generation, no
# simulation execution, no filesystem writes.
from app.services.slack.simulation_digest_intent import (
    try_route_simulation_digest,
)
# PAS204-A — broker conversation intelligence. Pure string output:
# no Slack API call, no simulation execution, no filesystem writes.
# Fires only when PAS191 returns INTENT_UNKNOWN, so PAS191 commands
# (stats, calls today, leads today, response rate, summary,
# priorities, help) take precedence.
from app.services.slack.broker_conversation_surface import (
    build_broker_response,
)
# PAS204-C — deterministic typo / shorthand normalization +
# demo / rehearsal data labeling. Both are pure, read-only,
# bounded-vocabulary helpers. Mutation tokens (pause/resume/
# push/remove) flow through the normalizer unchanged.
from app.services.slack.fuzzy_command_normalizer import (
    normalize_fuzzy_command,
)
from app.services.slack.demo_data_detector import (
    VERDICT_DEMO_DETECTED,
    detect_demo_signals,
)
# PAS207 — read-only proactive needs-attention digest intent. Pure
# string output: no Slack API call, no DB write, no simulation
# execution, no filesystem writes. Owns a closed set of 8 phrases
# that the PAS191 next-action carry-forward test deliberately
# excludes.
from app.services.slack.proactive_digest_intent import (
    try_route_needs_attention,
)

router = APIRouter()
logger = logging.getLogger("pas.slack_cmd")

_INTENT_SYSTEM = """You interpret plain-English commands from a real estate brokerage manager
controlling their AI calling assistant (PAS).

Classify the command into exactly one action and return JSON only — no prose.

Actions:
  pause          → {"action": "pause"}
  resume         → {"action": "resume"}
  push_property  → {"action": "push_property", "property": {"address": "...", "price": "...", "beds": "...", "notes": "..."}}
  remove_property→ {"action": "remove_property", "address": "..."}
  query_calls    → {"action": "query_calls", "period": "today|week|month"}
  query_leads    → {"action": "query_leads", "filter": "hot|all|not_booked"}
  query_stats    → {"action": "query_stats"}
  unknown        → {"action": "unknown"}"""


router = APIRouter()


# ───────────── WEBHOOK ENTRY POINT ─────────────

@router.post("/command")
async def slack_command(request: Request):
    """
    Receives Slack slash command POST.
    Verifies signature, parses intent with Claude, executes action.
    Responds within 3 seconds (Slack requirement).
    """
    body_bytes = await request.body()
    body_str = body_bytes.decode("utf-8")

    # Parse form data (Slack sends application/x-www-form-urlencoded)
    from urllib.parse import parse_qs
    params = {k: v[0] for k, v in parse_qs(body_str).items()}

    team_id = params.get("team_id", "")
    text = params.get("text", "").strip()
    # PAS204-C — deterministic typo / shorthand normalization
    # BEFORE PAS203 / PAS191 / PAS204 matchers see the text.
    # Pure function, bounded alias table. Mutation tokens
    # (pause/resume/push/remove) are explicitly excluded.
    text = normalize_fuzzy_command(text)
    response_url = params.get("response_url", "")

    # Look up brokerage by Slack workspace
    brokerage = get_brokerage_by_slack_team(team_id)
    if not brokerage:
        return JSONResponse({"text": "⚠️ This Slack workspace isn't linked to a PAS brokerage account."})

    # Verify Slack signature — reject if secret not configured (no silent bypass)
    signing_secret = brokerage.get("slack_signing_secret", "")
    if not signing_secret:
        logger.warning(f"Slack command rejected — no signing_secret set for brokerage {brokerage['id']}")
        return Response(status_code=403)
    if not _verify_slack_signature(request, body_bytes, signing_secret):
        logger.warning(f"Slack signature mismatch for brokerage {brokerage['id']}")
        return Response(status_code=403)

    # PAS-SECURITY-02 — per-brokerage rate limit. Conservative
    # default (30/min/brokerage). Failure isolation: limiter
    # outage never blocks production traffic.
    try:
        from app.services.security.rate_limit import (
            check_rate_limit,
        )
        _rl_verdict = check_rate_limit(
            surface="slack_command",
            brokerage_id=brokerage.get("id") if isinstance(brokerage, dict) else None,
            actor_type="TENANT",
        )
        if not _rl_verdict.get("allowed"):
            return JSONResponse({
                "text": "⚠️ Slack command rate limit reached. Please wait a moment and retry.",
            })
    except Exception:
        pass

    if not text:
        return JSONResponse({
            "text": (
                "👋 *PAS Command Interface*\n"
                "Try: `pause`, `resume`, `push 123 Main St $500k`, "
                "`calls today`, `hot leads`, `stats`"
            )
        })

    logger.info(f"Slack command | brokerage={brokerage['id']} | text={text!r}")

    # PAS203-A — Read-only simulation evidence digest fast-path.
    # Closed alias table → PAS202 Slack rendering of the latest
    # PAS201 digest on disk (or a bounded fallback if none exists).
    # NEVER writes to disk, NEVER generates a digest, NEVER executes
    # a simulation. Returns None for non-matching text — the
    # PAS191 / LLM paths below run unchanged in that case. Mutation
    # commands (pause/resume/push/remove) do not match any alias.
    _pas203_reports_dir = (
        Path(__file__).resolve().parents[2] / "reports" / "simulations"
    )
    pas203_resp = try_route_simulation_digest(text, _pas203_reports_dir)
    if pas203_resp is not None:
        log_event_bg(
            "slack.intent.matched",
            event_category="ops",
            event_source="slack_command",
            severity="info",
            payload={
                "brokerage_id": brokerage["id"],
                "intent":       "simulation_digest",
                "surface":      "slack_command_pas203",
            },
        )
        return JSONResponse({"text": pas203_resp, "response_type": "in_channel"})

    # PAS191 — Deterministic natural-language fast-path. Closed
    # alias table → closed intent code → safe formatter. NO LLM,
    # NO autonomous decisioning, NO mutation. Mutation commands
    # (pause / resume / push / remove) are explicitly NOT bound
    # by match_intent(); they continue to flow through the
    # exact-command branch via the LLM intent parser below.
    pas191 = match_intent(text)
    pas191_intent = pas191.get("intent") or INTENT_UNKNOWN

    # PAS207-B — Read-only proactive needs-attention digest. Closed
    # alias set (16 phrases) plus a bounded per-token typo map
    # (riska→risks, pipline→pipeline, sliping→slipping, attn→
    # attention, revw→review, humen→human) and trailing-filler
    # strip ("rn", "today", "now", "please").
    #
    # The fast-path fires BEFORE PAS204 so messy operator phrases
    # like "pipeline riska" or "anything slipping rn" route to the
    # proactive observer instead of being captured by PAS204's
    # safety/trust scorer (which keys on tokens like "risk" /
    # "risky"). It also fires BEFORE the PAS191 dispatch branch so
    # the PAS207-owned phrase "what needs attention" reaches the
    # proactive observer rather than PAS191's next_action.
    #
    # PAS207's alias table deliberately excludes PAS191 next_action
    # phrases ("next action", "priorities", "next steps", "top
    # priorities", "what should i do now", "what should i focus
    # on"), so those continue to dispatch through PAS191 unchanged.
    # PAS207 never writes to disk, never sends a Slack message,
    # never calls Twilio, never mutates the DB.
    pas207_resp = try_route_needs_attention(text)
    if pas207_resp is not None:
        log_event_bg(
            "slack.intent.matched",
            event_category="ops",
            event_source="slack_command",
            severity="info",
            payload={
                "brokerage_id": brokerage["id"],
                "intent":       "needs_attention",
                "surface":      "slack_command_pas207",
            },
        )
        return JSONResponse({"text": pas207_resp, "response_type": "in_channel"})

    # PAS204-A — Broker conversation intelligence. Pure string
    # output: no Slack API call, no simulation execution, no
    # filesystem writes. Fires ONLY when PAS191 returned
    # INTENT_UNKNOWN, so PAS191 commands (stats / calls today /
    # leads today / response rate / summary / priorities / help)
    # take precedence. Mutation commands (pause/resume/push/remove)
    # never match a PAS204 alias and continue to flow through the
    # LLM exact-command path below.
    if pas191_intent == INTENT_UNKNOWN:
        pas204_env = build_broker_response(text)
        pas204_intent = pas204_env.get("intent")
        # Fire when PAS204 has a real classification OR when it
        # fell back but the text was rich enough that PAS204
        # offered a clarifying question. Single-token noise
        # ("yo", "uhhh") leaves clarifying_question=None and
        # falls through to the LLM path below unchanged.
        pas204_fires = (
            pas204_intent != "fallback_clarify"
            or pas204_env.get("clarifying_question") is not None
        )
        if pas204_fires:
            log_event_bg(
                "slack.intent.matched",
                event_category="ops",
                event_source="slack_command",
                severity="info",
                payload={
                    "brokerage_id": brokerage["id"],
                    "intent":       str(pas204_intent),
                    "surface":      "slack_command_pas204",
                },
            )
            body = pas204_env.get("response_text") or ""
            cq = pas204_env.get("clarifying_question")
            if cq:
                body = body + "\n\n" + cq
            suggestions = pas204_env.get("suggested_next") or ()
            if suggestions:
                body = body + "\n\n_Suggested next:_\n" + "\n".join(
                    f"- {s}" for s in suggestions
                )
            return JSONResponse({
                "text":          body,
                "response_type": "in_channel",
            })

    if pas191_intent != INTENT_UNKNOWN:
        log_event_bg(
            "slack.intent.matched",
            event_category="ops",
            event_source="slack_command",
            severity="info",
            payload={
                "brokerage_id": brokerage["id"],
                "intent":       pas191_intent,
                "surface":      "slack_command_pas191",
            },
        )
        result_text = await _pas191_dispatch(pas191_intent, brokerage)
        return JSONResponse({"text": result_text, "response_type": "in_channel"})

    intent = await _parse_intent(text)
    action = intent.get("action", "unknown")
    result_text = await _execute_action(action, intent, brokerage)

    return JSONResponse({"text": result_text, "response_type": "in_channel"})


# ───────────── INTENT PARSING ─────────────

async def _parse_intent(text: str) -> dict:
    provider = get_provider()
    if provider is None:
        logger.warning("No LLM provider available — Slack intent set to unknown")
        return {"action": "unknown"}
    try:
        raw = await provider.chat(
            system=_INTENT_SYSTEM,
            user=text,
            max_tokens=150,
            temperature=0,
            purpose="slack_intent",
        )
        return json.loads(raw.strip())
    except Exception as e:
        logger.error(f"[{provider.name}] intent parsing failed: {e}")
        log_event_bg(
            "provider.failed",
            event_category="llm",
            event_source="slack_command",
            provider=provider.name,
            severity="warning",
            payload={
                "purpose": "slack_intent",
                "error_class": type(e).__name__,
                "message_excerpt": str(e)[:300],
            },
        )
        return {"action": "unknown"}


# ───────────── ACTION HANDLERS ─────────────

async def _execute_action(action: str, intent: dict, brokerage: dict) -> str:
    brokerage_id = brokerage["id"]
    agent_name = brokerage.get("agent_name", "Alex")

    if action == "pause":
        ok = set_brokerage_active(brokerage_id, False)
        return "⏸️ PAS is now *paused*. No outbound calls will be made." if ok else "❌ Failed to pause — check Supabase connection."

    if action == "resume":
        ok = set_brokerage_active(brokerage_id, True)
        return f"▶️ PAS is *active* again. {agent_name} will resume calling leads." if ok else "❌ Failed to resume."

    if action == "push_property":
        prop = intent.get("property", {})
        if not prop.get("address"):
            return "⚠️ I couldn't find a property address in that command. Try: `push 123 Main St $500k 3bed`"
        current = brokerage.get("featured_properties", [])
        current.append(prop)
        ok = update_featured_properties(brokerage_id, current)
        addr = prop.get("address", "")
        return f"🏠 Added *{addr}* to featured properties. {agent_name} will mention it on relevant calls." if ok else "❌ Failed to update properties."

    if action == "remove_property":
        addr = intent.get("address", "").lower()
        current = brokerage.get("featured_properties", [])
        updated = [p for p in current if addr not in p.get("address", "").lower()]
        if len(updated) == len(current):
            return f"⚠️ Couldn't find a property matching *{addr}* in the featured list."
        ok = update_featured_properties(brokerage_id, updated)
        return f"🗑️ Removed *{addr}* from featured properties." if ok else "❌ Failed to update."

    if action == "query_calls":
        return await _query_calls(brokerage_id, intent.get("period", "today"))

    if action == "query_leads":
        return await _query_leads(brokerage_id, intent.get("filter", "hot"))

    if action == "query_stats":
        return await _query_stats(brokerage_id)

    return (
        "🤔 I didn't understand that command. Try:\n"
        "`pause` · `resume` · `push [address]` · `remove [address]`\n"
        "`calls today` · `hot leads` · `stats`"
    )


# ───────────── DB QUERIES ─────────────

async def _query_calls(brokerage_id: str, period: str) -> str:
    try:
        db = get_supabase()
        interval = {"today": "1 day", "week": "7 days", "month": "30 days"}.get(period, "1 day")
        result = (
            db.table("calls")
            .select("outcome, call_status, phone_number, start_time")
            .eq("brokerage_id", brokerage_id)
            .gte("start_time", f"now() - interval '{interval}'")
            .execute()
        )
        rows = result.data or []
        total = len(rows)
        booked = sum(1 for r in rows if r["outcome"] == "booked")
        not_booked = total - booked
        pct = round(booked * 100 / total, 1) if total else 0
        label = {"today": "today", "week": "this week", "month": "this month"}.get(period, "today")
        return (
            f"📞 *Calls {label}*\n"
            f"Total: {total} · Booked: {booked} · Not booked: {not_booked}\n"
            f"Conversion: {pct}%"
        )
    except Exception as e:
        return f"❌ Couldn't fetch call data: {e}"


async def _query_leads(brokerage_id: str, filter_type: str) -> str:
    try:
        db = get_supabase()
        query = db.table("leads").select("name, phone_number, intent, budget, last_booked_at").eq("brokerage_id", brokerage_id)
        if filter_type == "hot":
            query = query.gte("last_booked_at", "now() - interval '7 days'")
        elif filter_type == "not_booked":
            query = query.is_("last_booked_at", "null")
        result = query.order("updated_at", desc=True).limit(10).execute()
        rows = result.data or []
        if not rows:
            return f"No leads found for filter: {filter_type}."
        lines = [f"*{r.get('name') or r['phone_number']}* — {r.get('intent','?')} | {r.get('budget','?')}" for r in rows]
        label = {"hot": "🔥 Hot leads (booked in last 7 days)", "not_booked": "📋 Leads not yet booked", "all": "📋 Recent leads"}.get(filter_type, "Leads")
        return f"{label}\n" + "\n".join(lines)
    except Exception as e:
        return f"❌ Couldn't fetch leads: {e}"


# ───────────── PAS191 — BOUNDED NATURAL-LANGUAGE DISPATCH ─────────────

# PostgREST treats `.gte()` / `.lt()` filter values as literals — SQL
# expressions like `now() - interval '1 day'` are NOT evaluated. The two
# helpers below compute the cutoff Python-side so today / week filters
# behave as advertised. Always UTC and timezone-aware so the ISO string
# round-trips cleanly through PostgREST.

def _pas191_cutoff_iso(days_back: int) -> str:
    """ISO-formatted UTC cutoff `now - days_back days`. Deterministic."""
    return (datetime.now(timezone.utc) - timedelta(days=days_back)).isoformat()


def _pas191_now_iso() -> str:
    """ISO-formatted UTC `now()` for lt/gt filters (e.g. overdue)."""
    return datetime.now(timezone.utc).isoformat()


async def _pas191_dispatch(intent: str, brokerage: dict) -> str:
    """
    Closed dispatcher for the 12 read-only PAS191 intents.

    No LLM. No mutation. No SQL constructed from user text.
    Every branch routes to a helper that returns a small dict of
    counts which the safe formatter turns into a Slack-safe string.
    On any exception, the formatter emits a generic error message
    (class name only, no internal message echo).
    """
    brokerage_id = brokerage["id"]
    try:
        if intent == INTENT_STATS:
            data = _pas191_stats(brokerage_id)
            # PAS204-C — label rehearsal/demo data clearly when
            # the brokerage record carries a demo marker. The
            # detector returns "no_demo_signal" for real
            # production brokerages, in which case we preserve
            # the legacy stats header by passing None.
            demo = detect_demo_signals(brokerage=brokerage)
            demo_verdict_arg = (
                demo["verdict"]
                if demo["verdict"] == VERDICT_DEMO_DETECTED
                else None
            )
            return pas191_responses.format_stats(
                data, demo_verdict=demo_verdict_arg,
            )
        if intent == INTENT_CALLS_TODAY:
            data = _pas191_calls(brokerage_id, "today")
            return pas191_responses.format_calls_today(data)
        if intent == INTENT_CALLS_WEEK:
            data = _pas191_calls(brokerage_id, "week")
            return pas191_responses.format_calls_week(data)
        if intent == INTENT_RESPONSE_RATE:
            data = _pas191_response_rate(brokerage_id)
            return pas191_responses.format_response_rate(data)
        if intent == INTENT_BOOKINGS_TODAY:
            data = _pas191_bookings_today(brokerage_id)
            return pas191_responses.format_bookings_today(data)
        if intent == INTENT_CALLBACKS_DUE:
            data = _pas191_callbacks_due(brokerage_id)
            return pas191_responses.format_callbacks_due(data)
        if intent == INTENT_QUEUE:
            data = _pas191_queue(brokerage_id)
            return pas191_responses.format_queue(data)
        if intent == INTENT_INCIDENTS:
            data = _pas191_incidents(brokerage_id)
            return pas191_responses.format_incidents(data)
        if intent == INTENT_POLICY:
            data = _pas191_policy(brokerage_id)
            return pas191_responses.format_policy(data)
        if intent == INTENT_HEALTH:
            data = _pas191_health()
            return pas191_responses.format_health(data)
        if intent == INTENT_PAUSED_STATUS:
            return pas191_responses.format_paused_status(
                {"active": brokerage.get("is_active")}
            )
        if intent == INTENT_HELP:
            return pas191_responses.format_help()
        if intent == INTENT_LEADS_TODAY:
            data = _pas191_leads_today(brokerage_id)
            return pas191_responses.format_leads_today(data)
        # PAS192 — operator-experience intents.
        if intent == INTENT_TODAY_SUMMARY:
            data = _pas192_today_summary(brokerage)
            return pas191_responses.format_today_summary(data)
        if intent == INTENT_NEXT_ACTION:
            data = _pas192_next_action(brokerage)
            return pas191_responses.format_next_action(data)
    except Exception as e:
        return pas191_responses.format_error(intent, type(e).__name__)
    return pas191_responses.format_unknown()


def _pas191_stats(brokerage_id: str) -> dict:
    try:
        db = get_supabase()
        result = (
            db.table("calls")
            .select("outcome, call_status")
            .eq("brokerage_id", brokerage_id)
            .execute()
        )
        rows = result.data or []
        total = len(rows)
        booked = sum(1 for r in rows if r.get("outcome") == "booked")
        completed = sum(1 for r in rows if r.get("call_status") == "completed")
        return {"total": total, "completed": completed, "booked": booked}
    except Exception:
        return {"total": 0, "completed": 0, "booked": 0}


def _pas191_calls(brokerage_id: str, period: str) -> dict:
    try:
        db = get_supabase()
        days_back = 1 if period == "today" else 7
        result = (
            db.table("calls")
            .select("outcome, call_status")
            .eq("brokerage_id", brokerage_id)
            .gte("start_time", _pas191_cutoff_iso(days_back))
            .execute()
        )
        rows = result.data or []
        total = len(rows)
        booked = sum(1 for r in rows if r.get("outcome") == "booked")
        return {
            "total":      total,
            "booked":     booked,
            "not_booked": total - booked,
        }
    except Exception:
        return {"total": 0, "booked": 0, "not_booked": 0}


def _pas191_response_rate(brokerage_id: str) -> dict:
    try:
        db = get_supabase()
        result = (
            db.table("calls")
            .select("call_status")
            .eq("brokerage_id", brokerage_id)
            .execute()
        )
        rows = result.data or []
        total = len(rows)
        completed = sum(1 for r in rows if r.get("call_status") == "completed")
        return {"total": total, "completed": completed}
    except Exception:
        return {"total": 0, "completed": 0}


def _pas191_bookings_today(brokerage_id: str) -> dict:
    try:
        db = get_supabase()
        result = (
            db.table("calls")
            .select("outcome")
            .eq("brokerage_id", brokerage_id)
            .eq("outcome", "booked")
            .gte("start_time", _pas191_cutoff_iso(1))
            .execute()
        )
        rows = result.data or []
        return {"booked_count": len(rows)}
    except Exception:
        return {"booked_count": 0}


def _pas191_callbacks_due(brokerage_id: str) -> dict:
    try:
        db = get_supabase()
        pending = (
            db.table("callbacks")
            .select("id")
            .eq("brokerage_id", brokerage_id)
            .eq("status", "pending")
            .execute()
        )
        pending_count = len(pending.data or [])
        overdue = (
            db.table("callbacks")
            .select("id")
            .eq("brokerage_id", brokerage_id)
            .eq("status", "pending")
            .lt("due_at", _pas191_now_iso())
            .execute()
        )
        overdue_count = len(overdue.data or [])
        return {"pending_count": pending_count, "overdue_count": overdue_count}
    except Exception:
        return {"pending_count": 0, "overdue_count": 0}


def _pas191_queue(brokerage_id: str) -> dict:
    try:
        db = get_supabase()
        result = (
            db.table("pending_calls")
            .select("id")
            .eq("brokerage_id", brokerage_id)
            .eq("status", "pending")
            .execute()
        )
        size = len(result.data or [])
    except Exception:
        size = 0
    worker_state = "off"
    try:
        import os
        if os.environ.get("PENDING_CALLS_WORKER_ENABLED") == "true":
            worker_state = "on"
    except Exception:
        worker_state = "off"
    return {"queue_size": size, "worker_state": worker_state}


def _pas191_incidents(brokerage_id: str) -> dict:
    try:
        db = get_supabase()
        result = (
            db.table("pas_incidents")
            .select("severity, status")
            .eq("brokerage_id", brokerage_id)
            .eq("status", "open")
            .execute()
        )
        rows = result.data or []
        sev: dict = {"critical": 0, "high": 0, "medium": 0, "low": 0}
        for r in rows:
            s = (r.get("severity") or "").lower()
            if s in sev:
                sev[s] += 1
        return {"open_count": len(rows), "severity_counts": sev}
    except Exception:
        return {"open_count": 0, "severity_counts": {}}


def _pas191_policy(brokerage_id: str) -> dict:
    breaker_state = "unknown"
    cutover_state = "unknown"
    security_gate = "unknown"
    try:
        from app.services.operator.circuit_breaker_policy import (
            should_block_new_outbound_for_brokerage,
        )
        blocked = should_block_new_outbound_for_brokerage(brokerage_id)
        breaker_state = "tripped" if blocked else "ok"
    except Exception:
        breaker_state = "unknown"
    try:
        db = get_supabase()
        result = (
            db.table("pas_cutover_approvals")
            .select("status")
            .eq("brokerage_id", brokerage_id)
            .order("created_at", desc=True)
            .limit(1)
            .execute()
        )
        rows = result.data or []
        cutover_state = (rows[0].get("status") if rows else "none") or "none"
    except Exception:
        cutover_state = "unknown"
    try:
        import os
        security_gate = "enforced" if os.environ.get("PAS_SECURITY_GATE") == "on" else "default"
    except Exception:
        security_gate = "unknown"
    return {
        "breaker_state": breaker_state,
        "cutover_state": cutover_state,
        "security_gate": security_gate,
    }


def _pas191_leads_today(brokerage_id: str) -> dict:
    """
    Closed read-only query for the leads_today intent.

    Counts, scoped to the brokerage and to "today":
      new_leads      — rows in `leads` with created_at >= today
      call_eligible  — subset of new_leads with last_call_at IS NULL
      pending_queue  — rows in the pending-call queue created today

    No PII columns are selected (we never touch phone_number / name /
    email). Every query is wrapped: on any exception, the helper
    returns zeros so the Slack response stays stable.
    """
    new_leads = 0
    call_eligible = 0
    pending_queue = 0
    try:
        db = get_supabase()
        cutoff = _pas191_cutoff_iso(1)
        result = (
            db.table("leads")
            .select("id, last_call_at")
            .eq("brokerage_id", brokerage_id)
            .gte("created_at", cutoff)
            .execute()
        )
        rows = result.data or []
        new_leads = len(rows)
        call_eligible = sum(1 for r in rows if not r.get("last_call_at"))
    except Exception:
        new_leads = 0
        call_eligible = 0
    try:
        db = get_supabase()
        q = (
            db.table("pending_calls")
            .select("id")
            .eq("brokerage_id", brokerage_id)
            .gte("created_at", _pas191_cutoff_iso(1))
            .execute()
        )
        pending_queue = len(q.data or [])
    except Exception:
        pending_queue = 0
    return {
        "new_leads":     new_leads,
        "call_eligible": call_eligible,
        "pending_queue": pending_queue,
    }


# ───────────── PAS192 — OPERATOR-EXPERIENCE DISPATCH ─────────────
#
# Both helpers below are READ-ONLY. They aggregate counts from the
# same closed surfaces PAS191 already reads (`calls`, `leads`,
# `agents`, `pending_calls`, `callbacks`, `pas_incidents`,
# `PENDING_CALLS_WORKER_ENABLED` env). They never write, never
# trigger autonomous remediation, and never echo PII. Every query
# is wrapped — on any failure the aggregate falls back to zeros /
# empty so the Slack surface stays stable.

# Allow-list of warning codes the today_summary helper may emit.
# Mirrors _TODAY_SUMMARY_WARNING_LABELS in operator_responses.py.
_PAS192_TODAY_WARNING_CODES = (
    "no_agents",
    "queue_backed_up",
    "worker_off",
    "low_response_rate",
    "no_bookings",
    "no_calls",
    "no_leads",
    "incidents_open",
    "paused",
)

_PAS192_LOW_RESPONSE_RATE_PCT = 30.0
_PAS192_QUEUE_BACKLOG_THRESHOLD = 25


def _pas192_count_agents(brokerage_id: str) -> int:
    try:
        db = get_supabase()
        result = (
            db.table("agents")
            .select("id")
            .eq("brokerage_id", brokerage_id)
            .execute()
        )
        return len(result.data or [])
    except Exception:
        return 0


def _pas192_overdue_callbacks(brokerage_id: str) -> int:
    try:
        db = get_supabase()
        result = (
            db.table("callbacks")
            .select("id")
            .eq("brokerage_id", brokerage_id)
            .eq("status", "pending")
            .lt("due_at", _pas191_now_iso())
            .execute()
        )
        return len(result.data or [])
    except Exception:
        return 0


def _pas192_today_summary(brokerage: dict) -> dict:
    """
    Aggregate today's operator wrap. Returns a closed envelope
    consumed by operator_responses.format_today_summary.
    """
    brokerage_id = brokerage["id"]
    calls = _pas191_calls(brokerage_id, "today")
    leads = _pas191_leads_today(brokerage_id)
    rr    = _pas191_response_rate(brokerage_id)
    bookings_today = _pas191_bookings_today(brokerage_id).get("booked_count", 0)
    queue_state    = _pas191_queue(brokerage_id)
    agents_count   = _pas192_count_agents(brokerage_id)
    incidents      = _pas191_incidents(brokerage_id)

    total = int(rr.get("total") or 0)
    completed = int(rr.get("completed") or 0)
    response_rate_pct = (completed * 100.0 / total) if total else 0.0

    warnings: list = []
    if agents_count == 0:
        warnings.append("no_agents")
    queue_size = int(queue_state.get("queue_size") or 0)
    worker_state = str(queue_state.get("worker_state") or "off")
    if queue_size >= _PAS192_QUEUE_BACKLOG_THRESHOLD:
        warnings.append("queue_backed_up")
    if worker_state != "on" and queue_size > 0:
        warnings.append("worker_off")
    calls_total = int(calls.get("total") or 0)
    if calls_total == 0:
        warnings.append("no_calls")
    else:
        if response_rate_pct < _PAS192_LOW_RESPONSE_RATE_PCT:
            warnings.append("low_response_rate")
    if int(leads.get("new_leads") or 0) == 0:
        warnings.append("no_leads")
    if bookings_today == 0:
        warnings.append("no_bookings")
    if int(incidents.get("open_count") or 0) > 0:
        warnings.append("incidents_open")
    if brokerage.get("is_active") is False:
        warnings.append("paused")

    # Defence-in-depth: only allow-listed codes pass through.
    warnings = [w for w in warnings if w in _PAS192_TODAY_WARNING_CODES]

    return {
        "new_leads":       int(leads.get("new_leads") or 0),
        "calls_total":     calls_total,
        "calls_connected": completed,
        "bookings":        int(bookings_today),
        "response_rate":   response_rate_pct,
        "pending_queue":   queue_size,
        "warnings":        warnings,
    }


def _pas192_next_action(brokerage: dict) -> dict:
    """
    Rank up to three operational priorities the operator can act
    on next. Order is fixed (see below); the dispatcher returns
    the closed priority codes in priority order and the formatter
    renders the matching labels.
    """
    brokerage_id = brokerage["id"]
    priorities: list = []

    agents_count = _pas192_count_agents(brokerage_id)
    if agents_count == 0:
        priorities.append({
            "code":   "assign_agents",
            "detail": "0 configured",
        })

    overdue = _pas192_overdue_callbacks(brokerage_id)
    if overdue > 0:
        priorities.append({
            "code":   "review_callbacks",
            "detail": f"{overdue} overdue",
        })

    if brokerage.get("is_active") is False:
        priorities.append({
            "code":   "resume_pas",
            "detail": "paused",
        })

    incidents = _pas191_incidents(brokerage_id)
    open_count = int(incidents.get("open_count") or 0)
    if open_count > 0:
        priorities.append({
            "code":   "resolve_incidents",
            "detail": f"{open_count} open",
        })

    leads = _pas191_leads_today(brokerage_id)
    call_eligible = int(leads.get("call_eligible") or 0)
    if call_eligible > 0:
        priorities.append({
            "code":   "follow_up_leads",
            "detail": f"{call_eligible} call eligible",
        })

    queue_state = _pas191_queue(brokerage_id)
    queue_size = int(queue_state.get("queue_size") or 0)
    worker_state = str(queue_state.get("worker_state") or "off")
    if queue_size > 0 and worker_state != "on":
        priorities.append({
            "code":   "start_worker",
            "detail": f"{queue_size} queued",
        })
    elif queue_size >= _PAS192_QUEUE_BACKLOG_THRESHOLD:
        priorities.append({
            "code":   "review_queue",
            "detail": f"{queue_size} pending",
        })

    rr = _pas191_response_rate(brokerage_id)
    rr_total = int(rr.get("total") or 0)
    rr_completed = int(rr.get("completed") or 0)
    if rr_total > 0:
        pct = rr_completed * 100.0 / rr_total
        if pct < _PAS192_LOW_RESPONSE_RATE_PCT:
            priorities.append({
                "code":   "review_response_rate",
                "detail": f"{round(pct, 1)}% pickup",
            })

    calls = _pas191_calls(brokerage_id, "today")
    not_booked = int(calls.get("not_booked") or 0)
    if not_booked > 0 and int(calls.get("booked") or 0) == 0:
        priorities.append({
            "code":   "review_failed_bookings",
            "detail": f"{not_booked} calls without booking",
        })

    return {"priorities": priorities[:3]}


def _pas191_health() -> dict:
    db_state = "unknown"
    try:
        db = get_supabase()
        if db is None:
            db_state = "down"
        else:
            db_state = "up"
    except Exception:
        db_state = "down"
    import os
    worker = "on" if os.environ.get("PENDING_CALLS_WORKER_ENABLED") == "true" else "off"
    twilio = "configured" if os.environ.get("TWILIO_AUTH_TOKEN") else "missing"
    return {"db": db_state, "worker": worker, "twilio": twilio}


# ───────────── DB QUERIES (existing LLM-path helpers) ─────────────

async def _query_stats(brokerage_id: str) -> str:
    try:
        db = get_supabase()
        result = db.table("calls").select("outcome, call_status").eq("brokerage_id", brokerage_id).execute()
        rows = result.data or []
        total = len(rows)
        booked = sum(1 for r in rows if r["outcome"] == "booked")
        completed = sum(1 for r in rows if r["call_status"] == "completed")
        pct = round(booked * 100 / completed, 1) if completed else 0
        return (
            f"📊 *All-time stats*\n"
            f"Total calls: {total} · Completed: {completed}\n"
            f"Booked: {booked} · Conversion rate: {pct}%"
        )
    except Exception as e:
        return f"❌ Couldn't fetch stats: {e}"


# ───────────── SIGNATURE VERIFICATION ─────────────

def _verify_slack_signature(request: Request, body: bytes, signing_secret: str) -> bool:
    try:
        timestamp = request.headers.get("X-Slack-Request-Timestamp", "")
        if abs(time.time() - int(timestamp)) > 300:
            return False  # replay attack guard
        sig_basestring = f"v0:{timestamp}:{body.decode('utf-8')}"
        expected = "v0=" + hmac.new(
            signing_secret.encode(), sig_basestring.encode(), hashlib.sha256
        ).hexdigest()
        received = request.headers.get("X-Slack-Signature", "")
        return hmac.compare_digest(expected, received)
    except Exception:
        return False
