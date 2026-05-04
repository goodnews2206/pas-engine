"""
PAS Engine -- Full Simulation
Runs 4 complete call scenarios through the real state machine.
No mocks. Real engine logic.
"""

import asyncio
import json
import sys
import io
from datetime import datetime, timezone
from app.engine.state_machine import PASEngine, LeadData, State

# Force UTF-8 output on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

DIVIDER = "=" * 70
THIN    = "-" * 70

# ---- BROKERAGE CONFIGS -------------------------------------------------------

BROKERAGE_DEMO = {
    "id": "remax-miami",
    "name": "RE/MAX Miami",
    "agent_name": "Alex",
    "agent_phone": "+13055550101",
    "twilio_number": "+13055550100",
    "slack_webhook_url": None,
    "featured_properties": [],
    "training_config": None,
    "fallback_phone": None,
    "active": True,
    "training_version": 0,
}

BROKERAGE_TRAINED = {
    "id": "coldwell-miami",
    "name": "Coldwell Banker Miami",
    "agent_name": "Jordan",
    "agent_phone": "+13055550201",
    "twilio_number": "+13055550200",
    "slack_webhook_url": None,
    "featured_properties": [
        {"address": "421 Brickell Ave Unit 3B", "price": "$480,000"},
        {"address": "88 SW 7th St", "price": "$320,000"},
    ],
    "training_config": {
        "booking_prompt": (
            "We have agents who specialize exactly in what you're looking for -- "
            "would you like me to schedule a no-obligation consultation this week?"
        ),
        "objection_system_prompt": "",
    },
    "fallback_phone": None,
    "active": True,
    "training_version": 3,
}

# ---- HELPERS -----------------------------------------------------------------

def header(title):
    print(f"\n{DIVIDER}")
    print(f"  {title}")
    print(DIVIDER)

def step(speaker, text, state=None):
    state_tag = f"  [state={state}]" if state else ""
    icon = "LEAD" if speaker == "LEAD" else "PAS "
    print(f"\n  [{icon}]{state_tag}")
    print(f"  {THIN}")
    for chunk in [text[i:i+65] for i in range(0, len(text), 65)]:
        print(f"    {chunk}")

async def run_scenario(title, call_sid, brokerage, lead_context, turns, show_data=True):
    header(title)
    engine = PASEngine(call_sid=call_sid, lead_context=lead_context, brokerage=brokerage)

    greeting = engine.get_greeting()
    step("PAS ", greeting, engine.state.current.name)

    for turn_input in turns:
        step("LEAD", turn_input, engine.state.current.name)
        response, done = await engine.process_input(turn_input)
        step("PAS ", response, engine.state.current.name)
        if done:
            break

    print(f"\n  {THIN}")
    print(f"  OUTCOME    : {engine.get_outcome().upper()}")
    print(f"  FINAL STATE: {engine.state.current.name}")

    if show_data:
        lead = engine.state.lead.__dict__
        print(f"\n  LEAD DATA CAPTURED (-> saved to `leads` table):")
        for k, v in lead.items():
            if v and v not in ("inbound", "outbound", False, ""):
                print(f"    {k:25s}: {v}")

    print(f"\n  TRANSCRIPT LOG ({len(engine.state.transcript_log)} entries):")
    for e in engine.state.transcript_log:
        ts = e['ts'][11:19]
        state_name = e['state'].name if hasattr(e['state'], 'name') else str(e['state'])
        print(f"    [{ts}] [{e['speaker'].upper():4}] [{state_name:10}] {e['text'][:60]}")

    meta = engine.get_metadata()
    print(f"\n  CALL METADATA (-> saved to `calls` table):")
    print(f"    call_sid         : {call_sid}")
    print(f"    duration_seconds : {meta['duration_seconds']}")
    print(f"    is_outbound      : {meta['is_outbound']}")
    print(f"    final_state      : {meta['final_state']}")
    print(f"    outcome          : {engine.get_outcome()}")

    return engine


async def main():
    print(f"\n{'#'*70}")
    print(f"  PAS ENGINE -- FULL CALL SIMULATION")
    print(f"  Run at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'#'*70}")

    # -------------------------------------------------------------------------
    # SCENARIO 1: INBOUND -- BUYER -- HAPPY PATH --> BOOKED
    # -------------------------------------------------------------------------
    await run_scenario(
        title="SCENARIO 1 | Inbound | Buyer | Happy Path --> BOOKED",
        call_sid="CA-SIM-001",
        brokerage=BROKERAGE_DEMO,
        lead_context=None,
        turns=[
            "Yeah sure I have a minute.",
            "I'm looking to buy, actually.",
            "My budget is around $400k.",
            "I'm looking to move in the next 3 months.",
            "Yeah, go ahead and book it.",
            "Three bedrooms would be ideal if possible.",
        ]
    )

    # -------------------------------------------------------------------------
    # SCENARIO 2: OUTBOUND -- PRE-FILLED CRM DATA -- FEATURED PROPERTY
    # -------------------------------------------------------------------------
    await run_scenario(
        title="SCENARIO 2 | Outbound | Pre-filled CRM | Featured Property --> BOOKED",
        call_sid="CA-SIM-002",
        brokerage=BROKERAGE_TRAINED,
        lead_context={
            "phone_number": "+13055551234",
            "name": "Marcus Williams",
            "email": "marcus@email.com",
            "intent": "buying",
            "budget": "$450k-$500k",
            "timeline": "2 months",
            "source": "outbound",
        },
        turns=[
            "Yes, this is Marcus.",
            "Yes please, book it.",
            "I'd prefer weekend viewings.",
        ]
    )

    # -------------------------------------------------------------------------
    # SCENARIO 3: INBOUND -- HARD OBJECTION -- NOT BOOKED
    # -------------------------------------------------------------------------
    await run_scenario(
        title="SCENARIO 3 | Inbound | Hard Objection --> NOT BOOKED",
        call_sid="CA-SIM-003",
        brokerage=BROKERAGE_DEMO,
        lead_context=None,
        turns=[
            "Yeah sure.",
            "I'm interested in buying.",
            "I already have an agent actually.",
            "I already have an agent, stop calling.",
        ]
    )

    # -------------------------------------------------------------------------
    # SCENARIO 4: RETURNING CALLER -- AI QUESTION -- TRANSFER REQUEST
    # -------------------------------------------------------------------------
    await run_scenario(
        title="SCENARIO 4 | Returning Caller | AI Question + Transfer Request",
        call_sid="CA-SIM-004",
        brokerage=BROKERAGE_DEMO,
        lead_context={
            "phone_number": "+13055559999",
            "name": "Priya Shah",
            "intent": "buying",
            "budget": "$350k",
            "timeline": "6 months",
            "source": "returning",
        },
        turns=[
            "Hi, yeah it's Priya.",
            "Wait -- are you a real person or AI?",
            "Let me speak to a human please.",
        ]
    )

    # ---- SCENARIO 5: BUDGET RETRY LOGIC -------------------------------------
    await run_scenario(
        title="SCENARIO 5 | Inbound | Budget Confusion --> Max Retries --> Advance",
        call_sid="CA-SIM-005",
        brokerage=BROKERAGE_DEMO,
        lead_context=None,
        turns=[
            "Sure, I have a minute.",
            "Looking to buy.",
            "I'm not really sure about budget honestly.",   # attempt 1 -- retry
            "I don't know, maybe depends on the market.",  # attempt 2 -- retry
            "Hmm I really can't say right now.",           # attempt 3 -- MAX_ATTEMPTS hit, advance anyway
            "I want to move within 6 months.",
            "No, maybe not right now.",                    # decline booking
        ]
    )

    # ---- DATA LAYER ----------------------------------------------------------
    print(f"\n{DIVIDER}")
    print("  DATA LAYER -- 5 TABLES, WHAT SAVES WHERE")
    print(DIVIDER)

    tables = [
        {
            "table": "brokerages",
            "trigger": "Admin POST /admin/brokerages -- one row per tenant forever",
            "fields": "id, name, agent_name, twilio_phone, api_key, training_config (JSONB), call_count, training_version",
            "sample": {"id": "remax-miami", "call_count": 142, "training_version": 3, "active": True},
        },
        {
            "table": "agents",
            "trigger": "Brokerage admin adds human agents -- one row per agent",
            "fields": "brokerage_id, name, phone, specialties[], areas[], status, total_assigned, close_rate (auto-computed)",
            "sample": {"name": "Sarah J.", "specialties": ["buying","luxury"], "status": "available", "close_rate": "34.50"},
        },
        {
            "table": "leads",
            "trigger": "Upserted after EVERY call -- unique per (brokerage_id, phone_number)",
            "fields": "phone_number, brokerage_id, name, intent, budget, timeline, notes, total_calls, last_booked_at",
            "sample": {"phone_number": "+13055551234", "total_calls": 3, "last_booked_at": "2026-04-28T06:31:00Z"},
        },
        {
            "table": "calls",
            "trigger": "Created on call start (Twilio SID as PK), finalized on hangup",
            "fields": "id (CallSid), brokerage_id, outcome, summary, transcript (full text), duration_seconds, agent_id",
            "sample": {"id": "CA-SIM-001", "outcome": "booked", "duration_seconds": 87},
        },
        {
            "table": "training_logs",
            "trigger": "Every 25 completed calls -- Claude rewrites prompts",
            "fields": "brokerage_id, version, booking_rate, calls_analyzed, insights (JSONB)",
            "sample": {"version": 3, "booking_rate": "34.20", "top_dropout_state": "BUDGET"},
        },
    ]

    for t in tables:
        print(f"\n  TABLE : {t['table']}")
        print(f"  WHEN  : {t['trigger']}")
        print(f"  FIELDS: {t['fields']}")
        print(f"  SAMPLE: {json.dumps(t['sample'])}")

    # ---- BROKERAGE / AGENT ROUTING -------------------------------------------
    print(f"\n{DIVIDER}")
    print("  BROKERAGE --> AGENT ROUTING ALGORITHM")
    print(DIVIDER)
    print("""
  On booking OR warm transfer request:

  STEP 1  Query agents WHERE brokerage_id=X AND status='available'
  STEP 2  Score each agent:
            +3  specialties contains lead.intent     (e.g. "buying")
            +2  areas contains lead property area
            +1  languages contains lead language
            TIE -> highest close_rate wins
  STEP 3  Assign winner:
            agent.status = 'busy'
            call.agent_id = winner.id
            SMS to agent phone: "New booking -- Name, intent, budget, slot"
            Slack @mention in brokerage channel
  STEP 4  No agents available:
            -> fallback: brokerage.fallback_phone forwarding
            -> or: "An agent will call you back within the hour"
  STEP 5  After appointment closes:
            Admin POST /agents/{id}/close
            total_closed++ -> close_rate auto-recalculates in DB
  """)

    # ---- THE FULL LOOP -------------------------------------------------------
    print(f"\n{DIVIDER}")
    print("  THE FULL PAS LOOP (every call, from PSTN to database)")
    print(DIVIDER)
    print("""
  [1] PHONE RINGS
      Caller dials brokerage Twilio number
      OR PAS dials out via POST /outbound/call

  [2] TWILIO -> POST /twilio/voice
      IF answering machine detected  -> leave voicemail -> END
      IF brokerage.active == False   -> hang up -> END
      ELSE                           -> return TwiML with WebSocket URL

  [3] WEBSOCKET OPENS  /ws/media-stream/{CallSid}
      Load brokerage config from Supabase (or demo fallback)
      Check leads table: is this a returning caller? -> load memory
      Create PASEngine(call_sid, lead_context, brokerage)
      Create call record in Supabase (status=active)

  [4] REAL-TIME AUDIO LOOP (concurrent async tasks)
      Twilio streams mulaw audio via WebSocket
        -> decoded base64 bytes -> audio queue
      Deepgram WebSocket receives audio -> returns transcript
        -> engine.process_input(transcript)
        -> PASEngine returns (response_text, done_flag)
      ElevenLabs TTS converts response_text -> mulaw audio
        -> encoded base64 -> sent back to Twilio -> caller hears it

  [5] STATE MACHINE STEPS (inside process_input)
      Each input checked in order:
        a. Is it an AI question?    -> disclose + redirect to current Q
        b. Is it a transfer request? -> pending_transfer=True, say "hold on"
        c. Is it a general question? -> defer to agent + ask current Q
        d. Is it a hard objection?  -> Claude rebuttal (max 2x then END)
        e. ELSE                     -> route to current state handler

      State handlers:
        GREETING  -> detect confusion/decline -> advance to INTENT
        INTENT    -> extract buy/sell/rent    -> advance to BUDGET
        BUDGET    -> extract amount via regex -> advance to TIMELINE
                     (max 2 retries before advancing with "not specified")
        TIMELINE  -> extract timeframe        -> advance to BOOKING
                     (tease featured property if brokerage has listings)
        BOOKING   -> "yes" -> Cal.com API -> book slot -> CLOSING
                     "no"  -> not_booked -> CLOSING
                     soft objection (cost?) -> reassure -> re-ask
        CLOSING   -> capture final notes      -> DONE
        DONE      -> call ends

      Outbound pre-fill: if intent/budget/timeline already in lead_context,
        those states are SKIPPED automatically (_skip_if_prefilled)

  [6] CALL ENDS (WebSocket close + Twilio status callback)
      Finalize call: outcome, duration, status in `calls` table
      Upsert lead memory in `leads` table (phone+brokerage unique key)
      Claude generates 2-4 sentence summary (haiku model, fast)
      Slack summary posted to brokerage webhook
      IF booked:
        Best-fit agent assigned (scoring algorithm above)
        SMS to agent + Slack @mention
        SMS/email confirmation to lead

  [7] SELF-TRAINING (every 25 calls)
      Fetch last 30 completed calls with transcripts
      Claude (sonnet) analyzes: what worked, what didn't, dropout states
      Returns JSON: new booking_prompt + objection_system_prompt
      Saved to brokerages.training_config
      training_version++
      All future calls for this brokerage use the new prompts
  """)

    # ---- WHAT IS PAS? --------------------------------------------------------
    print(f"\n{DIVIDER}")
    print("  WHAT IS PAS? -- APP, AGENT, OR WHAT")
    print(DIVIDER)
    print("""
  PAS is a VOICE AGENT PLATFORM -- specifically:

  AS INFRASTRUCTURE:
    FastAPI backend (headless -- no frontend)
    Real-time WebSocket audio pipeline (Twilio <-> Deepgram <-> ElevenLabs)
    Multi-tenant SaaS (one engine, many isolated brokerages)
    Supabase for persistence, Cal.com for booking, Slack for comms

  AS AN AI AGENT:
    Deterministic state machine (not a freeform LLM chatbot)
    Claude is called ONLY for objection handling + summaries + training
    The conversation flow itself is rule-based and predictable
    This is intentional -- real estate calls need consistency, not creativity

  AS A PRODUCT:
    White-label voice AI for real estate brokerages
    Each brokerage gets their own agent name, phone number, Slack workspace
    Brokerage admins manage it via REST API or /pas Slack slash commands
    It self-improves: Claude rewrites its own scripts based on real call data

  IT IS NOT:
    A frontend app or dashboard (purely API + Slack)
    A general-purpose AI agent (scoped to: qualify -> book -> notify)
    A single-tenant system (built for many brokerages from day one)

  DEPLOYMENT PATH:
    Local dev  -> uvicorn (as running now)
    Production -> Railway (nixpacks.toml + Procfile already configured)
    Inbound    -> Twilio number points to https://yourapp.com/twilio/voice
    Outbound   -> Brokerage POSTs to /outbound/call with their API key
  """)

    print(f"\n{'#'*70}")
    print("  SIMULATION COMPLETE")
    print(f"{'#'*70}\n")


asyncio.run(main())
