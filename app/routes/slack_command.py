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

    if not text:
        return JSONResponse({
            "text": (
                "👋 *PAS Command Interface*\n"
                "Try: `pause`, `resume`, `push 123 Main St $500k`, "
                "`calls today`, `hot leads`, `stats`"
            )
        })

    logger.info(f"Slack command | brokerage={brokerage['id']} | text={text!r}")

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
