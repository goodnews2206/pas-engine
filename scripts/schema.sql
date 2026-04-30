-- ─────────────────────────────────────────────────
-- PAS — Supabase Schema  (run in SQL Editor → Run All)
-- ─────────────────────────────────────────────────

-- ─── BROKERAGES ───────────────────────────────────
CREATE TABLE IF NOT EXISTS brokerages (
    id                   TEXT PRIMARY KEY,           -- "remax-miami"
    name                 TEXT NOT NULL,              -- "RE/MAX Miami"
    agent_name           TEXT NOT NULL DEFAULT 'Alex',
    twilio_phone         TEXT UNIQUE,                -- dedicated inbound/outbound number
    agent_phone          TEXT,                       -- real agent — gets SMS after booking
    slack_webhook_url    TEXT,
    slack_team_id        TEXT,
    slack_signing_secret TEXT,
    api_key              TEXT UNIQUE,                -- brokerage uses this for /outbound/call
    featured_properties  JSONB    DEFAULT '[]',
    active               BOOLEAN  NOT NULL DEFAULT true,

    -- Operational config (see migrate_v2.sql for shape)
    config               JSONB    DEFAULT '{}',

    -- Self-training
    call_count           INTEGER  NOT NULL DEFAULT 0,
    training_version     INTEGER  NOT NULL DEFAULT 0,
    training_config      JSONB    DEFAULT '{}',
    -- training_config shape:
    -- {
    --   "booking_prompt": "...",
    --   "objection_system_prompt": "...",
    --   "insights": {
    --     "booking_rate": 0.34,
    --     "top_dropout_state": "BUDGET",
    --     "common_objections": ["...", "..."],
    --     "what_works": "...",
    --     "calls_analyzed": 50
    --   },
    --   "trained_at": "2026-04-27T..."
    -- }

    created_at           TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at           TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ─── AGENTS ───────────────────────────────────────────
-- One row per human agent at a brokerage.
-- PAS uses this to route appointments, track availability, and measure performance.
CREATE TABLE IF NOT EXISTS agents (
    id               UUID        DEFAULT gen_random_uuid() PRIMARY KEY,
    brokerage_id     TEXT        NOT NULL REFERENCES brokerages(id) ON DELETE CASCADE,
    name             TEXT        NOT NULL,
    phone            TEXT,                          -- for SMS reminders + warm transfer
    email            TEXT,
    slack_member_id  TEXT,                          -- e.g. "U012AB3CD" for Slack @mention
    status           TEXT        NOT NULL DEFAULT 'available',
    -- available | busy | offline
    specialties      TEXT[]      DEFAULT '{}',      -- ["buying","selling","luxury","commercial"]
    areas            TEXT[]      DEFAULT '{}',      -- ["Miami Beach","Downtown","Coral Gables"]
    languages        TEXT[]      DEFAULT '{"en"}',  -- ISO 639-1 codes
    -- Performance (updated after each appointment outcome)
    total_assigned   INTEGER     NOT NULL DEFAULT 0,
    total_closed     INTEGER     NOT NULL DEFAULT 0,
    close_rate       NUMERIC(5,2) GENERATED ALWAYS AS (
        CASE WHEN total_assigned = 0 THEN 0
             ELSE ROUND(total_closed * 100.0 / total_assigned, 2)
        END
    ) STORED,
    created_at       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at       TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ─── LEADS (MEMORY — per brokerage, fully isolated) ──
-- UNIQUE(brokerage_id, phone_number) ensures one record per prospect per tenant.
-- A lead calling RE/MAX and Coldwell Banker gets two completely separate records.
CREATE TABLE IF NOT EXISTS leads (
    id              UUID        DEFAULT gen_random_uuid() PRIMARY KEY,
    brokerage_id    TEXT        NOT NULL REFERENCES brokerages(id) ON DELETE CASCADE,
    phone_number    TEXT        NOT NULL,
    name            TEXT,
    email           TEXT,
    intent          TEXT,        -- buying | selling | renting
    budget          TEXT,
    timeline        TEXT,
    notes           TEXT,        -- cumulative notes from all calls (append-only)
    total_calls     INTEGER      NOT NULL DEFAULT 0,
    last_call_at    TIMESTAMPTZ,
    last_booked_at  TIMESTAMPTZ,
    created_at      TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    UNIQUE(brokerage_id, phone_number)
);

-- ─── CALLS ────────────────────────────────────────
CREATE TABLE IF NOT EXISTS calls (
    id               TEXT        PRIMARY KEY,         -- Twilio CallSid or SIM-xxx
    brokerage_id     TEXT        REFERENCES brokerages(id),
    phone_number     TEXT        NOT NULL,
    email            TEXT,
    source           TEXT        NOT NULL DEFAULT 'inbound',   -- inbound | outbound | simulated
    call_type        TEXT        NOT NULL DEFAULT 'inbound',   -- inbound | outbound | simulated
    start_time       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    end_time         TIMESTAMPTZ,
    duration_seconds INTEGER,
    call_status      TEXT        NOT NULL DEFAULT 'active',    -- active | completed | failed | dropped
    outcome          TEXT        NOT NULL DEFAULT 'pending',   -- pending | booked | not_booked | transferred
    agent_id         UUID        REFERENCES agents(id),        -- assigned agent (booking or transfer)
    summary          TEXT,
    transcript       TEXT,
    metadata         JSONB,      -- {lead, final_state, is_outbound, states_visited, objections_detected, ...}
    created_at       TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ─── TRAINING LOGS ────────────────────────────────
-- Audit trail of every self-training run per brokerage.
CREATE TABLE IF NOT EXISTS training_logs (
    id             UUID        DEFAULT gen_random_uuid() PRIMARY KEY,
    brokerage_id   TEXT        NOT NULL REFERENCES brokerages(id) ON DELETE CASCADE,
    version        INTEGER     NOT NULL,
    calls_analyzed INTEGER     NOT NULL,
    booking_rate   NUMERIC(5,2),
    insights       JSONB,
    created_at     TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ─── INDEXES ──────────────────────────────────────
CREATE INDEX IF NOT EXISTS idx_agents_brokerage     ON agents(brokerage_id);
CREATE INDEX IF NOT EXISTS idx_agents_status        ON agents(brokerage_id, status);
CREATE INDEX IF NOT EXISTS idx_brokerages_api_key   ON brokerages(api_key);
CREATE INDEX IF NOT EXISTS idx_calls_brokerage      ON calls(brokerage_id);
CREATE INDEX IF NOT EXISTS idx_calls_outcome        ON calls(outcome);
CREATE INDEX IF NOT EXISTS idx_calls_start_time     ON calls(start_time DESC);
CREATE INDEX IF NOT EXISTS idx_calls_phone          ON calls(phone_number);
CREATE INDEX IF NOT EXISTS idx_calls_type           ON calls(call_type);
CREATE INDEX IF NOT EXISTS idx_leads_brokerage      ON leads(brokerage_id);
CREATE INDEX IF NOT EXISTS idx_leads_phone          ON leads(phone_number);
CREATE INDEX IF NOT EXISTS idx_training_logs_broker ON training_logs(brokerage_id, created_at DESC);

-- ─── RLS ──────────────────────────────────────────
ALTER TABLE brokerages    ENABLE ROW LEVEL SECURITY;
ALTER TABLE agents        ENABLE ROW LEVEL SECURITY;
ALTER TABLE calls         ENABLE ROW LEVEL SECURITY;
ALTER TABLE leads         ENABLE ROW LEVEL SECURITY;
ALTER TABLE training_logs ENABLE ROW LEVEL SECURITY;

-- ─────────────────────────────────────────────────
-- USEFUL QUERIES
-- ─────────────────────────────────────────────────

-- Per-brokerage conversion rate
-- SELECT b.name, b.call_count, b.training_version,
--   COUNT(c.*) FILTER (WHERE c.outcome = 'booked') AS booked,
--   ROUND(COUNT(c.*) FILTER (WHERE c.outcome='booked') * 100.0
--         / NULLIF(b.call_count, 0), 2) AS conversion_pct
-- FROM brokerages b LEFT JOIN calls c ON c.brokerage_id = b.id
-- GROUP BY b.id;

-- Training improvement over time
-- SELECT version, booking_rate, calls_analyzed, insights->>'top_dropout_state', created_at
-- FROM training_logs WHERE brokerage_id = 'your-id' ORDER BY version;

-- Hot leads (booked in last 7 days)
-- SELECT l.name, l.phone_number, l.intent, l.budget, l.last_booked_at
-- FROM leads l WHERE l.brokerage_id = 'your-id'
-- AND l.last_booked_at >= NOW() - INTERVAL '7 days'
-- ORDER BY l.last_booked_at DESC;
