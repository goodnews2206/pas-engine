-- ─────────────────────────────────────────────────────────────────
-- PAS — Migration v5
-- Adds the universal pas_events table for day-one event tracking.
-- Run in Supabase SQL Editor → Run All. Safe to re-run (IF NOT EXISTS).
--
-- This is the substrate for:
--   - call/lead/booking/objection intelligence
--   - per-provider failure tracking
--   - future PAS Credits accounting (token/cost rollups)
--   - future PA Mode summaries
--
-- Append-only by design. No UPDATE path. To correct an event, log a new one.
-- Backend writes through the Supabase service-role client (bypasses RLS).
-- No anon policies — keep parity with calls/bookings/error_logs.
-- ─────────────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS pas_events (
    id              BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    event_type      TEXT        NOT NULL,                 -- "call.started", "state.transition", ...
    event_category  TEXT,                                  -- "call" | "lead" | "llm" | "provider" | "booking" | "ops"
    event_source    TEXT,                                  -- "state_machine" | "websocket" | "simulate" | "twilio_webhook" | "portal" | "admin"
    severity        TEXT        NOT NULL DEFAULT 'info',   -- "debug" | "info" | "warning" | "error" | "critical"

    brokerage_id    TEXT        REFERENCES brokerages(id) ON DELETE SET NULL,
    call_id         TEXT        REFERENCES calls(id)      ON DELETE SET NULL,
    lead_id         UUID        REFERENCES leads(id)      ON DELETE SET NULL,
    agent_id        UUID        REFERENCES agents(id)     ON DELETE SET NULL,
    user_id         TEXT,                                  -- portal user (no users table yet)

    provider        TEXT,                                  -- "anthropic" | "openai" | "twilio" | "deepgram" | "elevenlabs" | "calcom"
    state           TEXT,                                  -- conversation state, e.g. "GREETING" | "INTENT" | ...
    payload         JSONB       NOT NULL DEFAULT '{}'::jsonb,

    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ── INDEXES ─────────────────────────────────────────────────────
CREATE INDEX IF NOT EXISTS idx_pas_events_brokerage_time
    ON pas_events (brokerage_id, created_at DESC);

CREATE INDEX IF NOT EXISTS idx_pas_events_call_time
    ON pas_events (call_id, created_at);

CREATE INDEX IF NOT EXISTS idx_pas_events_type_time
    ON pas_events (event_type, created_at DESC);

CREATE INDEX IF NOT EXISTS idx_pas_events_lead_time
    ON pas_events (lead_id, created_at DESC);

-- Partial index for incident triage / ops dashboards
CREATE INDEX IF NOT EXISTS idx_pas_events_severity
    ON pas_events (severity, created_at DESC)
    WHERE severity IN ('warning', 'error', 'critical');

-- Partial index for provider cost/perf rollups (future PAS Credits)
CREATE INDEX IF NOT EXISTS idx_pas_events_provider_time
    ON pas_events (provider, created_at DESC)
    WHERE provider IS NOT NULL;

-- ── RLS ─────────────────────────────────────────────────────────
-- Mirror existing pattern: enable RLS, no anon policies, writes go
-- through the FastAPI backend's service-role Supabase client.
-- When portal JWT auth lands, add a tenant-isolation read policy:
--     USING (brokerage_id = (auth.jwt() ->> 'brokerage_id'))
ALTER TABLE pas_events ENABLE ROW LEVEL SECURITY;

-- ── USEFUL QUERIES (reference — not executed) ───────────────────
-- Per-call event timeline:
-- SELECT created_at, event_type, state, payload
-- FROM pas_events WHERE call_id = ? ORDER BY created_at;
--
-- Today's event volume by type for one brokerage:
-- SELECT event_type, COUNT(*)
-- FROM pas_events
-- WHERE brokerage_id = ? AND created_at >= date_trunc('day', NOW())
-- GROUP BY 1 ORDER BY 2 DESC;
--
-- Provider failure rate last 24h:
-- SELECT provider, COUNT(*) FILTER (WHERE event_type LIKE '%.failed') AS fails,
--                          COUNT(*) AS total
-- FROM pas_events
-- WHERE provider IS NOT NULL AND created_at > NOW() - INTERVAL '24 hours'
-- GROUP BY provider;
