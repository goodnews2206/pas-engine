-- ─────────────────────────────────────────────────────────────────
-- PAS — Migration v6
-- Convert pas_events foreign keys into soft references.
-- Run in Supabase SQL Editor → Run All. Safe to re-run (IF EXISTS).
--
-- Why:
--   pas_events is an observability stream — events MUST land even when
--   the parent row (brokerage / call / lead / agent) is missing or its
--   insert failed. The original v5 hard FK constraints silently rejected
--   events whose parent did not exist (e.g. simulated calls against a
--   brokerage that has no row in `brokerages`), defeating the purpose
--   of a universal event log.
--
--   The columns themselves are kept (typed TEXT/UUID) so dashboard joins
--   continue to work — they're just no longer FK-enforced. Indexes are
--   not affected by dropping the FKs.
--
-- Out of scope for this migration:
--   - No column drops.
--   - No index changes.
--   - No payload changes.
--   - No RLS changes (RLS stays enabled).
--   - No anon/public policies.
-- ─────────────────────────────────────────────────────────────────

ALTER TABLE pas_events DROP CONSTRAINT IF EXISTS pas_events_brokerage_id_fkey;
ALTER TABLE pas_events DROP CONSTRAINT IF EXISTS pas_events_call_id_fkey;
ALTER TABLE pas_events DROP CONSTRAINT IF EXISTS pas_events_lead_id_fkey;
ALTER TABLE pas_events DROP CONSTRAINT IF EXISTS pas_events_agent_id_fkey;

-- ── Verification (reference — not executed) ─────────────────────
-- After running, this should return 0 rows:
--   SELECT conname FROM pg_constraint
--   WHERE conrelid = 'pas_events'::regclass AND contype = 'f';
