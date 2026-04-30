-- ─────────────────────────────────────────────────────────────────────────
-- PAS Schema Migration V2
-- Run in Supabase SQL Editor → Run All
-- Safe: all statements are additive (IF NOT EXISTS / no data dropped)
-- ─────────────────────────────────────────────────────────────────────────

-- ── brokerages: operational config JSONB field ───────────────────────────
-- Stores per-brokerage behaviour overrides. Using JSONB avoids frequent
-- column migrations as config options grow. _row() in brokerage_store.py
-- unpacks this into typed fields with safe defaults.
ALTER TABLE brokerages ADD COLUMN IF NOT EXISTS config JSONB DEFAULT '{}';

-- ── calls: call_type for filtering simulation vs live calls ──────────────
-- 'inbound' | 'outbound' | 'simulated'
-- (The existing `source` column holds the same values; call_type makes
-- filtering explicit and forwards-compatible with future sources.)
ALTER TABLE calls ADD COLUMN IF NOT EXISTS call_type TEXT DEFAULT 'inbound';

-- Index to quickly filter simulated calls in admin dashboard
CREATE INDEX IF NOT EXISTS idx_calls_type ON calls(call_type);

-- ── Backfill call_type from source for existing rows ────────────────────
UPDATE calls SET call_type = source WHERE call_type IS NULL OR call_type = 'inbound';

-- ─────────────────────────────────────────────────────────────────────────
-- What the `config` JSONB column stores (reference — not enforced by DB):
--
-- {
--   "transfer_enabled":      true,
--   "booking_enabled":       true,
--   "ai_disclosure_enabled": true,
--   "max_objection_attempts": 2,
--   "tone":                  "professional",   -- professional | friendly | formal
--   "script_style":          "default",        -- default | consultative | aggressive
--   "market_location":       "Miami Beach, FL",
--   "business_hours":        {},               -- {mon: {start: "09:00", end: "18:00"}, ...}
--   "after_hours_behavior":  "callback",       -- callback | voicemail | none
--   "calcom_event_type_id":  0                 -- per-brokerage override for Cal.com
-- }
-- ─────────────────────────────────────────────────────────────────────────
