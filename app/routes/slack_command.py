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
    INTENT_PAUSED_STATUS,
    INTENT_POLICY,
    INTENT_QUEUE,
    INTENT_RESPONSE_RATE,
    INTENT_STATS,
    INTENT_UNKNOWN,
    match_intent,
)
from app.services.slack import operator_responses as pas191_responses

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

    # PAS191 — Deterministic natural-language fast-path. Closed
    # alias table → closed intent code → safe formatter. NO LLM,
    # NO autonomous decisioning, NO mutation. Mutation commands
    # (pause / resume / push / remove) are explicitly NOT bound
    # by match_intent(); they continue to flow through the
    # exact-command branch via the LLM intent parser below.
    pas191 = match_intent(text)
    pas191_intent = pas191.get("intent") or INTENT_UNKNOWN
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
            return pas191_responses.format_stats(data)
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
        interval = "1 day" if period == "today" else "7 days"
        result = (
            db.table("calls")
            .select("outcome, call_status")
            .eq("brokerage_id", brokerage_id)
            .gte("start_time", f"now() - interval '{interval}'")
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
            .gte("start_time", "now() - interval '1 day'")
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
            .lt("due_at", "now()")
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
        result = (
            db.table("leads")
            .select("id, last_call_at")
            .eq("brokerage_id", brokerage_id)
            .gte("created_at", "now() - interval '1 day'")
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
            .gte("created_at", "now() - interval '1 day'")
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
