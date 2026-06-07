-- ─────────────────────────────────────────────────────────────────
-- PAS — Migration v8 (PAS213B)
-- Durable digital-lead ingestion dedupe.
-- Run in Supabase SQL Editor → Run All. Safe to re-run (IF NOT EXISTS).
--
-- STATUS: PROPOSAL — NOT auto-applied by any code path. An operator applies
-- this by hand, exactly like every prior migrate_v*.sql. Until it is applied,
-- the durable dedupe store (app.services.ingestion.lead_dedupe.
-- SupabaseLeadDedupeStore) fails OPEN — every lead is still persisted to the
-- `leads` table and every ingestion event is still written to `pas_events`;
-- only cross-restart duplicate suppression is inactive. No lead is lost.
--
-- This migration is ADDITIVE ONLY:
--   - No existing table, column, constraint, or index is dropped or altered.
--   - One new table + its indexes are created.
--
-- Why a dedicated table (not a column on `leads`):
--   `leads` is phone-keyed (UNIQUE(brokerage_id, phone_number)) and merges by
--   phone. Digital dedupe must also catch (a) duplicate external_lead_id across
--   *different* phones, and (b) duplicate messages with no external id — neither
--   of which the phone-keyed leads row can express. A separate seen-key ledger
--   keeps that concern out of the prospect record.
--
-- Tenant safety:
--   `brokerage_id` is part of the UNIQUE key, so a dedupe key seen under one
--   tenant can never suppress another tenant's lead. Soft reference only (no FK)
--   — mirrors the pas_events / audit_log precedent so a dedupe row can never
--   fail to land because a parent row is missing.
--
-- PII:
--   This table stores NO raw contact PII. `dedupe_key` is an opaque
--   sha256-derived token (dl_<hex16>); `external_lead_id` is a vendor lead id,
--   not personal data. Name / phone / email / message are NEVER written here.
-- ─────────────────────────────────────────────────────────────────


-- ── lead_ingestion_dedupe ───────────────────────────────────────
CREATE TABLE IF NOT EXISTS lead_ingestion_dedupe (
    id               BIGINT      GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    brokerage_id     TEXT        NOT NULL,            -- tenant scope (soft ref)
    dedupe_key       TEXT        NOT NULL,            -- deterministic dl_<sha> token
    source           TEXT,                            -- closed-vocab source label
    external_lead_id TEXT,                            -- vendor lead id (not PII), when present
    lead_id          UUID,                            -- soft ref to leads.id (nullable, no FK)
    hit_count        INTEGER     NOT NULL DEFAULT 1,  -- times this key was seen (1 = first)
    first_seen_at    TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    last_seen_at     TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    -- Tenant-scoped uniqueness IS the race backstop: a concurrent/duplicate
    -- registration of the same (tenant, key) is rejected by this constraint,
    -- which the application swallows. Also creates the lookup index used by
    -- is_duplicate(brokerage_id, dedupe_key).
    UNIQUE (brokerage_id, dedupe_key)
);

-- Secondary lookup for external-id audits / future source-adapter reconciles.
CREATE INDEX IF NOT EXISTS lead_ingestion_dedupe_ext_idx
    ON lead_ingestion_dedupe (brokerage_id, external_lead_id)
    WHERE external_lead_id IS NOT NULL;

-- RLS parity with leads / calls / pas_events / audit_log: enable, no anon
-- policies, writes via the service-role backend client.
ALTER TABLE lead_ingestion_dedupe ENABLE ROW LEVEL SECURITY;


-- ── Verification (reference — not executed) ─────────────────────
-- After running, this should return a row:
--   SELECT to_regclass('public.lead_ingestion_dedupe');
--
-- And the tenant-scoped unique should be present:
--   SELECT conname FROM pg_constraint
--   WHERE conrelid = 'lead_ingestion_dedupe'::regclass AND contype = 'u';
