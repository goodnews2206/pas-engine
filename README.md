# PAS — Performative AI SuperStaff
## ORVN Labs | Voice Qualification Engine MVP

A deterministic orchestration engine that handles real estate lead qualification calls end-to-end: answers the phone, asks 5 qualification questions, handles objections via Claude, books via Cal.com, and logs everything to Supabase.

---

## Architecture

```
Twilio (inbound call)
  │
  ▼
POST /twilio/voice  ← FastAPI webhook
  │  returns TwiML with <Stream> WebSocket URL
  ▼
WebSocket /ws/media-stream/{call_sid}
  │
  ├─── mulaw audio → Deepgram (streaming STT)
  │                      │
  │               transcript events
  │                      │
  │                      ▼
  │              PAS State Machine
  │          (GREETING→INTENT→BUDGET→TIMELINE→BOOKING→CLOSING)
  │                      │
  │              objection? → Claude API (max 100 tokens)
  │                      │
  │              booking? → Cal.com API
  │                      │
  │              log → Supabase
  │                      │
  │               response text
  │                      │
  ├─── ElevenLabs TTS (mulaw output)
  │
  ▼
Twilio plays audio to caller
```

---

## Data Flow: Call Start → End

1. **Call arrives** → Twilio POSTs to `/twilio/voice`
2. **DB record created** → Supabase `calls` table, status=`active`
3. **TwiML returned** → instructs Twilio to open WebSocket media stream
4. **WebSocket opens** → `/ws/media-stream/{call_sid}`
5. **Greeting synthesized** → ElevenLabs → audio queued immediately
6. **Audio streams in** → Twilio sends base64 mulaw in media events
7. **Deepgram receives audio** → streams back transcripts
8. **PAS Engine processes transcript** → runs through state machine
9. **State: GREETING** → any response advances to INTENT
10. **State: INTENT** → extracts buy/sell/rent → advances to BUDGET
11. **State: BUDGET** → extracts dollar amount → advances to TIMELINE
12. **State: TIMELINE** → extracts timeframe → advances to BOOKING
13. **State: BOOKING** → asks for consent → calls Cal.com on yes
14. **State: CLOSING** → confirms booking → call ends
15. **Objection detected** (any state) → Claude generates rebuttal → resumes state
16. **WebSocket closes** → outcome + transcript written to Supabase
17. **Twilio status callback** → POST `/twilio/status` → duration finalized

---

## Setup: Local Development

### Prerequisites
- Python 3.11+
- ffmpeg installed (`brew install ffmpeg` on Mac)
- ngrok for local tunneling

### Steps

```bash
# 1. Clone and enter the project
cd pas-engine

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env with your API keys

# 5. Set up Supabase schema
# Go to Supabase → SQL Editor → paste contents of scripts/schema.sql → Run

# 6. Start the server
uvicorn app.main:app --reload --port 8000

# 7. Expose locally with ngrok
ngrok http 8000
# Copy the https URL, e.g. https://abc123.ngrok.io
# Set BASE_URL=https://abc123.ngrok.io in your .env
# Restart uvicorn

# 8. Configure Twilio
# Go to: Twilio Console → Phone Numbers → your number → Voice
# Set Webhook URL: https://abc123.ngrok.io/twilio/voice  (POST)
# Set Status Callback: https://abc123.ngrok.io/twilio/status  (POST)

# 9. Call your Twilio number. PAS answers.
```

---

## Deployment: Railway

```bash
# 1. Install Railway CLI
npm install -g @railway/cli
railway login

# 2. Initialize project
railway init
# Select "Empty Project"

# 3. Add all environment variables
# Railway Dashboard → your project → Variables → paste all from .env

# 4. Deploy
railway up

# 5. Get your public URL
railway domain
# Copy URL → set as BASE_URL variable in Railway

# 6. Update Twilio webhook URLs to your Railway URL
# Twilio Console → Phone Numbers → Voice webhook → https://your-app.up.railway.app/twilio/voice
```

Railway automatically detects `nixpacks.toml` and installs ffmpeg.

---

## Required API Keys & Where to Get Them

| Service | Where | Notes |
|---|---|---|
| Twilio | console.twilio.com | Buy a phone number |
| Deepgram | console.deepgram.com | nova-2-phonecall model |
| ElevenLabs | elevenlabs.io | Get voice ID from Voice Library |
| Anthropic | console.anthropic.com | claude-sonnet-4 |
| Supabase | supabase.com | Create new project, use service key |
| Cal.com | cal.com/settings/developer | Create API key, get event type ID |

---

## Environment Variables

See `.env.example` for full list. All are required.

---

## Supabase Aggregation Queries

All queries are in `scripts/schema.sql` (commented out at bottom).

Quick reference:
```sql
-- Total bookings this month
SELECT COUNT(*) FROM calls
WHERE outcome = 'booked'
AND start_time >= DATE_TRUNC('month', NOW());

-- Conversion rate
SELECT
  ROUND(COUNT(*) FILTER (WHERE outcome = 'booked') * 100.0 /
  NULLIF(COUNT(*) FILTER (WHERE call_status = 'completed'), 0), 2) AS conversion_pct
FROM calls;
```

---

## State Machine Reference

```
GREETING  → Did they pick up and respond? Yes → INTENT
INTENT    → buy/sell/rent extracted? Yes → BUDGET | retry (max 2) → BUDGET
BUDGET    → dollar amount detected? Yes → TIMELINE | retry (max 2) → TIMELINE
TIMELINE  → timeframe detected? Yes → BOOKING | forced → BOOKING
BOOKING   → lead says yes → Cal.com → CLOSING
            lead says no → CLOSING (not_booked)
CLOSING   → any response → DONE
OBJECTION → (any state) objection detected → Claude rebuttal → resume state
```

---

## Latency Budget

| Stage | Target | Implementation |
|---|---|---|
| STT (Deepgram) | 200–400ms | `nova-2-phonecall`, `endpointing=300` |
| Engine processing | <50ms | Pure Python, no I/O except on objection |
| TTS (ElevenLabs) | 200–400ms | `eleven_turbo_v2` model |
| **Total** | **<900ms** | |

Objection path (Claude) adds ~500ms — acceptable since it's non-linear.

---

## Definition of Done ✓

- [ ] Real call connects via Twilio
- [ ] PAS asks all 5 questions (intent, budget, timeline, booking consent, closing)
- [ ] Objection handled by Claude with rebuttal
- [ ] Cal.com appointment booked
- [ ] Call record in Supabase with outcome + transcript
