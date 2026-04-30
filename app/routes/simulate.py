"""
POST /simulate-call — text-in / text-out PAS simulation.

No Twilio, Deepgram, or ElevenLabs required. Uses the real PASEngine
state machine end-to-end. Logs to Supabase when available.

Designed for:
  - Sales demos (show the full call flow without a live phone number)
  - QA / regression testing of call logic
  - Building demo UIs on top of the PAS API

Session lifecycle:
  1. POST with no call_sid (or unknown call_sid) → creates session, returns greeting + call_sid
  2. POST with call_sid + message → processes turn, returns PAS response
  3. When done=true → session is cleaned up; final state logged to Supabase

Request body:
  {
    "brokerage_id": "remax-miami",       # optional, defaults to "demo"
    "call_sid":     "SIM-xxx",           # optional on first request
    "lead": {                            # optional — pre-fills context for outbound-style flow
      "name":         "John Smith",
      "phone_number": "+13055551234",
      "email":        "john@example.com",
      "intent":       "buying",
      "budget":       "$400k",
      "timeline":     "3 months"
    },
    "message": "Yeah sure I have a minute"   # the lead's spoken text
  }

Response:
  {
    "call_sid":          "SIM-ABC123",
    "response":          "Are you looking to buy, sell, or rent?",
    "state":             "INTENT",
    "lead_data":         { ... },
    "outcome":           "pending",
    "done":              false,
    "transfer_requested": false
  }
"""

import logging
import uuid
from datetime import datetime, timezone
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.db.brokerage_store import get_brokerage_by_id
from app.db.call_logger import create_call_record, update_call_outcome
from app.db.lead_memory import upsert_lead, mark_booked
from app.engine.state_machine import PASEngine
from app.services.summary.call_summary import generate_call_summary

router = APIRouter()
logger = logging.getLogger("pas.simulate")

# In-process session store: call_sid → PASEngine
# Fine for single-instance Railway deployment (standard for MVP).
_sessions: dict[str, PASEngine] = {}
_MAX_SESSIONS = 200  # safety cap — old sessions get evicted at limit


class SimulateLead(BaseModel):
    name: str = ""
    phone_number: str = ""
    email: str = ""
    intent: str = ""
    budget: str = ""
    timeline: str = ""


class SimulateRequest(BaseModel):
    brokerage_id: str = "demo"
    call_sid: Optional[str] = None
    lead: SimulateLead = SimulateLead()
    message: str = ""


@router.post("/simulate-call")
async def simulate_call(body: SimulateRequest):
    """
    Run one turn of a simulated PAS call.

    First call (no call_sid): starts a session and returns the PAS greeting.
    Subsequent calls (same call_sid + a message): processes the lead's message.
    """
    brokerage_id = body.brokerage_id or "demo"
    call_sid = body.call_sid

    # ── NEW SESSION ──────────────────────────────────────────────────────────
    if not call_sid or call_sid not in _sessions:
        call_sid = call_sid or f"SIM-{uuid.uuid4().hex[:12].upper()}"

        # Evict oldest sessions if at limit (simple FIFO — fine for demo scale)
        if len(_sessions) >= _MAX_SESSIONS:
            oldest = next(iter(_sessions))
            _sessions.pop(oldest, None)
            logger.warning(f"Session cap reached — evicted {oldest}")

        brokerage = get_brokerage_by_id(brokerage_id)

        lead = body.lead
        lead_context = None
        if lead.phone_number or lead.name or lead.intent:
            lead_context = {
                "name": lead.name,
                "phone_number": lead.phone_number or "simulated",
                "email": lead.email,
                "intent": lead.intent,
                "budget": lead.budget,
                "timeline": lead.timeline,
                "source": "simulation",
            }

        engine = PASEngine(
            call_sid=call_sid,
            lead_context=lead_context,
            brokerage=brokerage,
        )
        _sessions[call_sid] = engine

        # Log call start (non-blocking — failure doesn't kill the response)
        phone = (lead.phone_number or "simulated") if lead else "simulated"
        await _safe_create_record(call_sid, phone, lead.email, brokerage_id)

        greeting = engine.get_greeting()
        engine._log("pas", greeting)

        logger.info(f"[{call_sid}] Simulation session started | brokerage={brokerage_id}")
        return _build_response(call_sid, engine, greeting, done=False)

    # ── EXISTING SESSION ─────────────────────────────────────────────────────
    engine = _sessions[call_sid]

    if not body.message.strip():
        raise HTTPException(status_code=400, detail="message is required for existing sessions")

    try:
        response, done = await engine.process_input(body.message)
    except Exception as e:
        logger.error(f"[{call_sid}] Engine error: {e}", exc_info=True)
        response = (
            "I'm sorry, I ran into a technical issue. "
            "Let me connect you with one of our agents."
        )
        done = True

    transfer_requested = bool(engine.pending_transfer)

    if done or transfer_requested:
        await _finalize_session(call_sid, engine)

    return _build_response(call_sid, engine, response, done, transfer_requested)


# ── HELPERS ──────────────────────────────────────────────────────────────────

def _build_response(
    call_sid: str,
    engine: PASEngine,
    response: str,
    done: bool,
    transfer_requested: bool = False,
) -> dict:
    return {
        "call_sid": call_sid,
        "response": response,
        "state": engine.state.current.value,
        "lead_data": engine.state.lead.__dict__,
        "outcome": engine.get_outcome(),
        "done": done,
        "transfer_requested": transfer_requested,
    }


async def _safe_create_record(
    call_sid: str,
    phone: str,
    email: str,
    brokerage_id: str,
):
    try:
        await create_call_record(
            call_sid=call_sid,
            phone_number=phone,
            email=email,
            source="simulated",
            brokerage_id=brokerage_id,
        )
    except Exception as e:
        logger.warning(f"[{call_sid}] Could not create call record (Supabase may be offline): {e}")


async def _finalize_session(call_sid: str, engine: PASEngine):
    """Persist call outcome to Supabase and clean up the in-memory session."""
    _sessions.pop(call_sid, None)

    outcome = engine.get_outcome()
    transcript = engine.get_full_transcript()
    metadata = engine.get_metadata()
    metadata["source"] = "simulated"

    duration = metadata.get("duration_seconds", 0)

    # Generate summary (Claude Haiku — fast; falls back gracefully if key missing)
    summary = None
    try:
        lead_data = metadata.get("lead", {})
        summary = await generate_call_summary(
            transcript=transcript,
            outcome=outcome,
            lead=lead_data,
            duration_seconds=duration,
        )
    except Exception as e:
        logger.warning(f"[{call_sid}] Summary generation skipped: {e}")

    try:
        await update_call_outcome(
            call_sid=call_sid,
            outcome=outcome,
            transcript=transcript,
            metadata=metadata,
            summary=summary,
            call_status="completed",
            duration_seconds=duration,
        )
        logger.info(f"[{call_sid}] Simulation finalized | outcome={outcome} | duration={duration}s")
    except Exception as e:
        logger.warning(f"[{call_sid}] Could not finalize call record: {e}")

    # Persist lead memory so the brokerage's CRM-style Leads tab reflects the call.
    # Mirrors the behaviour of the live inbound flow.
    try:
        lead_data = metadata.get("lead", {}) or {}
        phone = lead_data.get("phone_number") or ""
        brokerage_id = getattr(engine, "brokerage_id", None)
        if phone and phone != "simulated" and brokerage_id and brokerage_id != "demo":
            updates = {
                "name":         lead_data.get("name") or "",
                "email":        lead_data.get("email") or "",
                "intent":       lead_data.get("intent") or "",
                "budget":       lead_data.get("budget") or "",
                "timeline":     lead_data.get("timeline") or "",
                "last_call_at": datetime.now(timezone.utc).isoformat(),
            }
            updates = {k: v for k, v in updates.items() if v}
            upsert_lead(brokerage_id, phone, updates)
            if outcome == "booked":
                mark_booked(brokerage_id, phone)
    except Exception as e:
        logger.warning(f"[{call_sid}] Lead memory upsert skipped: {e}")
