-- ─────────────────────────────────────────────────────────────────────────
-- PAS Schema Migration V3 — Portal & Intelligence Layer
-- Run in Supabase SQL Editor → Run All
-- Safe: all ADD COLUMN IF NOT EXISTS, all CREATE TABLE IF NOT EXISTS
-- ─────────────────────────────────────────────────────────────────────────

-- ── 1. ONBOARDING KEYS ───────────────────────────────────────────────────
-- One-time invite keys: admin generates → brokerage claims → key expires.
-- Claiming a key returns the brokerage's api_key for future portal access.
CREATE TABLE IF NOT EXISTS onboarding_keys (
    id           UUID        DEFAULT gen_random_uuid() PRIMARY KEY,
    key          TEXT        NOT NULL UNIQUE,           -- "orvn_" + token
    brokerage_id TEXT        NOT NULL REFERENCES brokerages(id) ON DELETE CASCADE,
    created_by   TEXT        NOT NULL DEFAULT 'admin',
    expires_at   TIMESTAMPTZ NOT NULL,
    used         BOOLEAN     NOT NULL DEFAULT false,
    used_at      TIMESTAMPTZ,
    used_by_email TEXT,
    revoked      BOOLEAN     NOT NULL DEFAULT false,
    created_at   TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_keys_brokerage ON onboarding_keys(brokerage_id);
CREATE INDEX IF NOT EXISTS idx_keys_key       ON onboarding_keys(key);

-- ── 2. BOOKINGS ──────────────────────────────────────────────────────────
-- Tracks every Cal.com booking PAS creates. Source of truth for scheduled
-- appointments, no-shows, completions — the evidence of business value.
CREATE TABLE IF NOT EXISTS bookings (
    id           TEXT        PRIMARY KEY,               -- Cal.com booking ID or DEMO-xxx
    brokerage_id TEXT        REFERENCES brokerages(id),
    call_sid     TEXT        REFERENCES calls(id),
    lead_id      UUID        REFERENCES leads(id),
    agent_id     UUID        REFERENCES agents(id),
    status       TEXT        NOT NULL DEFAULT 'scheduled',
    -- scheduled | cancelled | rescheduled | completed | no_show | failed
    slot_time    TIMESTAMPTZ,
    lead_name    TEXT,
    lead_phone   TEXT,
    lead_email   TEXT,
    notes        TEXT,
    calcom_url   TEXT,
    admin_note   TEXT,
    created_at   TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at   TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_bookings_brokerage  ON bookings(brokerage_id);
CREATE INDEX IF NOT EXISTS idx_bookings_status     ON bookings(status);
CREATE INDEX IF NOT EXISTS idx_bookings_slot_time  ON bookings(slot_time DESC);
CREATE INDEX IF NOT EXISTS idx_bookings_call       ON bookings(call_sid);

-- ── 3. ERROR LOGS ─────────────────────────────────────────────────────────
-- Captures all system errors: broken API calls, failed bookings, Twilio
-- drops, LLM timeouts. Makes failures visible and actionable from the dashboard.
CREATE TABLE IF NOT EXISTS error_logs (
    id           UUID        DEFAULT gen_random_uuid() PRIMARY KEY,
    service      TEXT        NOT NULL,
    -- twilio | deepgram | elevenlabs | anthropic | calcom | supabase | system | simulate
    brokerage_id TEXT,
    call_sid     TEXT,
    severity     TEXT        NOT NULL DEFAULT 'error',
    -- debug | info | warning | error | critical
    message      TEXT        NOT NULL,
    detail       TEXT,                                  -- stack trace or extra context
    resolved     BOOLEAN     NOT NULL DEFAULT false,
    resolved_at  TIMESTAMPTZ,
    admin_note   TEXT,
    created_at   TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_errors_service    ON error_logs(service);
CREATE INDEX IF NOT EXISTS idx_errors_brokerage  ON error_logs(brokerage_id);
CREATE INDEX IF NOT EXISTS idx_errors_resolved   ON error_logs(resolved);
CREATE INDEX IF NOT EXISTS idx_errors_created    ON error_logs(created_at DESC);

-- ── 4. ADMIN NOTES ───────────────────────────────────────────────────────
-- Internal notes that ORVN staff attach to any entity.
CREATE TABLE IF NOT EXISTS admin_notes (
    id          UUID        DEFAULT gen_random_uuid() PRIMARY KEY,
    entity_type TEXT        NOT NULL,   -- brokerage | call | lead | agent | booking
    entity_id   TEXT        NOT NULL,
    note        TEXT        NOT NULL,
    created_by  TEXT        NOT NULL DEFAULT 'admin',
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_notes_entity ON admin_notes(entity_type, entity_id);

-- ── 5. BROKERAGES — new columns ──────────────────────────────────────────

-- Owner contact
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS owner_name     TEXT DEFAULT '';
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS owner_email    TEXT DEFAULT '';
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS owner_phone    TEXT DEFAULT '';
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS company_website TEXT DEFAULT '';
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS crm_used       TEXT DEFAULT '';

-- Plan / billing
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS plan           TEXT DEFAULT 'trial';
-- trial | starter | professional | enterprise
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS billing_status TEXT DEFAULT 'trial';
-- trial | active | past_due | paused | cancelled
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS trial_ends_at  TIMESTAMPTZ;
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS setup_fee_paid BOOLEAN DEFAULT false;

-- Internal ORVN-only notes (not shown to client)
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS internal_notes TEXT DEFAULT '';

-- Per-brokerage feature flags (which portal features are active)
-- See feature_defaults in brokerage_store.py for the shape
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS features JSONB DEFAULT '{}';

-- Per-brokerage notification preferences
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS notification_config JSONB DEFAULT '{}';

-- ── 6. LEADS — new columns ───────────────────────────────────────────────
ALTER TABLE leads ADD COLUMN IF NOT EXISTS status           TEXT DEFAULT 'new';
-- new | qualified | booked | transferred | nurture | not_ready | not_interested | do_not_call | closed
ALTER TABLE leads ADD COLUMN IF NOT EXISTS lead_source      TEXT DEFAULT '';
ALTER TABLE leads ADD COLUMN IF NOT EXISTS assigned_agent_id UUID REFERENCES agents(id);

CREATE INDEX IF NOT EXISTS idx_leads_status ON leads(status);

-- ── 7. CALLS — agent_name denormalization for quick display ──────────────
ALTER TABLE calls ADD COLUMN IF NOT EXISTS lead_name TEXT DEFAULT '';

-- ── RLS on new tables ────────────────────────────────────────────────────
ALTER TABLE onboarding_keys ENABLE ROW LEVEL SECURITY;
ALTER TABLE bookings        ENABLE ROW LEVEL SECURITY;
ALTER TABLE error_logs      ENABLE ROW LEVEL SECURITY;
ALTER TABLE admin_notes     ENABLE ROW LEVEL SECURITY;

-- ─────────────────────────────────────────────────────────────────────────
-- FEATURE FLAGS REFERENCE (stored in brokerages.features JSONB)
-- ─────────────────────────────────────────────────────────────────────────
-- {
--   "simulation_enabled":    true,   -- /portal shows simulation test tab
--   "analytics_enabled":     true,   -- /portal/overview metrics visible
--   "insights_enabled":      true,   -- /portal/insights intelligence cards
--   "reports_enabled":       false,  -- weekly/monthly report generation
--   "self_training_enabled": true,   -- auto script improvement
--   "booking_enabled":       true,   -- Cal.com appointment creation
--   "transfer_enabled":      true,   -- human transfer on request
--   "sms_enabled":           true,   -- SMS confirmations to leads
--   "email_notifications":   true,   -- email summaries
--   "slack_notifications":   false,  -- Slack webhook active
--   "call_recording":        false,  -- call audio retention
--   "crm_sync":              false   -- CRM push (future)
-- }
-- ─────────────────────────────────────────────────────────────────────────
