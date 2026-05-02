-- ─────────────────────────────────────────────────────────────────
-- PAS — Seed: demo brokerage
-- Run in Supabase SQL Editor. Safe to re-run (ON CONFLICT DO NOTHING).
--
-- Why:
--   The codebase falls back to an in-memory _DEFAULT_BROKERAGE dict when
--   `get_brokerage_by_id("demo")` finds no row — so the engine RUNS for
--   /simulate-call, but the database can't persist anything that
--   references brokerage_id="demo" (calls.brokerage_id REFERENCES
--   brokerages(id) → FK violation → silent insert failure).
--
--   Seeding the row makes /simulate-call durable end-to-end: calls are
--   persisted, lead memory works, training/summary/dashboard see sim runs.
--
-- Columns chosen (minimum valid insert against scripts/schema.sql):
--   id          — TEXT PRIMARY KEY (no default; required)
--   name        — TEXT NOT NULL    (no default; required)
--   agent_name  — TEXT NOT NULL DEFAULT 'Alex'   (set explicitly)
--   active      — BOOLEAN NOT NULL DEFAULT true  (set explicitly)
-- All other columns have defaults from schema.sql + migrate_v2..v4.sql.
-- ─────────────────────────────────────────────────────────────────

INSERT INTO brokerages (id, name, agent_name, active)
VALUES ('demo', 'ORVN Realty', 'Alex', true)
ON CONFLICT (id) DO NOTHING;

-- ── Verification (reference — not executed) ─────────────────────
-- SELECT id, name, agent_name, active FROM brokerages WHERE id = 'demo';
