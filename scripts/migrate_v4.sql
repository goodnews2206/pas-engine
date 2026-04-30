-- ─────────────────────────────────────────────────────────────────
-- PAS — Migration v4
-- Adds fields required by the Admin + Client portal expansions.
-- Run in Supabase SQL Editor. All statements use IF NOT EXISTS / IF EXISTS
-- so this is safe to re-run.
-- ─────────────────────────────────────────────────────────────────

-- ── BROKERAGES ──────────────────────────────────────────────────
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS owner_name        TEXT;
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS owner_email       TEXT;
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS owner_phone       TEXT;
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS company_website   TEXT;
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS crm_used          TEXT;
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS plan              TEXT    DEFAULT 'trial';
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS billing_status    TEXT    DEFAULT 'trial';
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS trial_ends_at     TIMESTAMPTZ;
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS setup_fee_paid    BOOLEAN DEFAULT false;
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS internal_notes    TEXT;
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS features          JSONB   DEFAULT '{}';
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS notification_config JSONB DEFAULT '{}';

-- ── AGENTS ──────────────────────────────────────────────────────
ALTER TABLE agents ADD COLUMN IF NOT EXISTS role               TEXT    DEFAULT 'agent';
ALTER TABLE agents ADD COLUMN IF NOT EXISTS fallback           BOOLEAN DEFAULT false;
ALTER TABLE agents ADD COLUMN IF NOT EXISTS routing_priority   INTEGER DEFAULT 0;
ALTER TABLE agents ADD COLUMN IF NOT EXISTS calcom_link        TEXT;
ALTER TABLE agents ADD COLUMN IF NOT EXISTS calcom_event_type_id INTEGER;

-- ── LEADS ───────────────────────────────────────────────────────
ALTER TABLE leads ADD COLUMN IF NOT EXISTS status             TEXT    DEFAULT 'new';
ALTER TABLE leads ADD COLUMN IF NOT EXISTS assigned_agent_id  UUID    REFERENCES agents(id) ON DELETE SET NULL;

-- ── CALLS ───────────────────────────────────────────────────────
ALTER TABLE calls ADD COLUMN IF NOT EXISTS admin_note TEXT;

-- ── ONBOARDING KEYS (idempotent create) ─────────────────────────
CREATE TABLE IF NOT EXISTS onboarding_keys (
    id              UUID        DEFAULT gen_random_uuid() PRIMARY KEY,
    key             TEXT        UNIQUE NOT NULL,
    brokerage_id    TEXT        NOT NULL REFERENCES brokerages(id) ON DELETE CASCADE,
    created_by      TEXT        DEFAULT 'admin',
    expires_at      TIMESTAMPTZ NOT NULL,
    used            BOOLEAN     NOT NULL DEFAULT false,
    used_by         TEXT,
    used_at         TIMESTAMPTZ,
    revoked         BOOLEAN     NOT NULL DEFAULT false,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_onboarding_keys_brokerage ON onboarding_keys(brokerage_id);
CREATE INDEX IF NOT EXISTS idx_onboarding_keys_key       ON onboarding_keys(key);

-- ── BOOKINGS (idempotent create) ────────────────────────────────
CREATE TABLE IF NOT EXISTS bookings (
    booking_id      TEXT        PRIMARY KEY,
    brokerage_id    TEXT        NOT NULL REFERENCES brokerages(id) ON DELETE CASCADE,
    call_sid        TEXT        REFERENCES calls(id) ON DELETE SET NULL,
    agent_id        UUID        REFERENCES agents(id) ON DELETE SET NULL,
    lead_id         UUID        REFERENCES leads(id) ON DELETE SET NULL,
    lead_name       TEXT,
    lead_phone      TEXT,
    lead_email      TEXT,
    slot_time       TIMESTAMPTZ,
    status          TEXT        NOT NULL DEFAULT 'scheduled',
    notes           TEXT,
    calcom_url      TEXT,
    admin_note      TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_bookings_brokerage  ON bookings(brokerage_id);
CREATE INDEX IF NOT EXISTS idx_bookings_slot_time  ON bookings(slot_time DESC);
CREATE INDEX IF NOT EXISTS idx_bookings_status     ON bookings(status);

-- ── ERROR LOGS (idempotent create) ──────────────────────────────
CREATE TABLE IF NOT EXISTS error_logs (
    id              UUID        DEFAULT gen_random_uuid() PRIMARY KEY,
    service         TEXT        NOT NULL,
    brokerage_id    TEXT        REFERENCES brokerages(id) ON DELETE SET NULL,
    call_sid        TEXT,
    severity        TEXT        NOT NULL DEFAULT 'error',
    message         TEXT        NOT NULL,
    detail          TEXT,
    resolved        BOOLEAN     NOT NULL DEFAULT false,
    admin_note      TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_error_logs_service    ON error_logs(service);
CREATE INDEX IF NOT EXISTS idx_error_logs_brokerage  ON error_logs(brokerage_id);
CREATE INDEX IF NOT EXISTS idx_error_logs_resolved   ON error_logs(resolved);
CREATE INDEX IF NOT EXISTS idx_error_logs_created_at ON error_logs(created_at DESC);

-- ── USEFUL QUERIES ───────────────────────────────────────────────

-- Brokerages by plan
-- SELECT plan, billing_status, COUNT(*) FROM brokerages GROUP BY plan, billing_status;

-- Leads by status
-- SELECT status, COUNT(*) FROM leads GROUP BY status ORDER BY count DESC;

-- Error counts by service (unresolved)
-- SELECT service, COUNT(*) FROM error_logs WHERE resolved = false GROUP BY service ORDER BY count DESC;
