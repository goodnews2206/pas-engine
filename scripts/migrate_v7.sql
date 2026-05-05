-- ─────────────────────────────────────────────────────────────────
-- PAS — Migration v7 (PAS133A)
-- Auth + white-glove onboarding scaffolding.
-- Run in Supabase SQL Editor → Run All. Safe to re-run (IF NOT EXISTS).
--
-- This migration is ADDITIVE ONLY:
--   - No existing column is dropped or renamed.
--   - No existing constraint is altered.
--   - `brokerages.api_key` continues to work for legacy auth.
--   - `onboarding_keys.key` (plaintext) continues to work for any
--     in-flight invites issued before v7.
--
-- Adds:
--   1. admin_users         — ORVN operator → auth.users mapping
--   2. brokerage_users     — brokerage member → auth.users mapping (with role)
--   3. onboarding_keys     — additive columns for hashed setup tokens
--   4. audit_log           — append-only audit trail
--
-- Prerequisite (one-time, in Supabase Studio):
--   Authentication → Providers → Email enabled. This creates the
--   built-in `auth.users` table referenced by the FK constraints below.
--   If `auth.users` does not exist, this migration will fail at the
--   admin_users CREATE TABLE step — that is intentional. Enable Auth
--   first, then re-run.
--
-- Out of scope for this migration:
--   - No code calls these tables yet (PAS133B).
--   - No RLS policies for the new tables (added once route layer wires up).
--   - No data backfill — existing brokerages keep their api_key + invite
--     records untouched.
-- ─────────────────────────────────────────────────────────────────


-- ── 1. admin_users ──────────────────────────────────────────────
-- One row per ORVN operator. user_id is the auth.users.id from
-- Supabase Auth. Role is intentionally narrow for v1.
CREATE TABLE IF NOT EXISTS admin_users (
    user_id     UUID        PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    role        TEXT        NOT NULL DEFAULT 'admin'
                            CHECK (role IN ('admin', 'admin_readonly')),
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by  UUID        REFERENCES auth.users(id) ON DELETE SET NULL,
    removed_at  TIMESTAMPTZ
);


-- ── 2. brokerage_users ──────────────────────────────────────────
-- Membership of a Supabase user in a brokerage, with role. A user
-- belongs to at most one brokerage (UNIQUE(brokerage_id, user_id)
-- prevents duplicates within a brokerage; cross-brokerage membership
-- is allowed at the schema level but route layer will enforce single-
-- tenant scope per principal).
CREATE TABLE IF NOT EXISTS brokerage_users (
    id            UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
    brokerage_id  TEXT        NOT NULL REFERENCES brokerages(id) ON DELETE CASCADE,
    user_id       UUID        NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    role          TEXT        NOT NULL
                              CHECK (role IN ('owner', 'agent', 'viewer', 'demo_viewer')),
    invited_by    UUID        REFERENCES auth.users(id) ON DELETE SET NULL,
    created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    removed_at    TIMESTAMPTZ,
    UNIQUE (brokerage_id, user_id)
);

CREATE INDEX IF NOT EXISTS brokerage_users_user_idx
    ON brokerage_users (user_id);

CREATE INDEX IF NOT EXISTS brokerage_users_brokerage_idx
    ON brokerage_users (brokerage_id);


-- ── 3. onboarding_keys — additive columns ───────────────────────
-- Existing v1 columns (key, brokerage_id, created_by, expires_at,
-- used, used_at, used_by_email, revoked, created_at) are unchanged.
-- New columns enable hashed-at-rest tokens and richer invite intents.
ALTER TABLE onboarding_keys
    ADD COLUMN IF NOT EXISTS key_hash      TEXT,
    ADD COLUMN IF NOT EXISTS key_lookup    TEXT,
    ADD COLUMN IF NOT EXISTS intent        TEXT DEFAULT 'brokerage_setup',
    ADD COLUMN IF NOT EXISTS invited_email TEXT,
    ADD COLUMN IF NOT EXISTS invited_role  TEXT,
    ADD COLUMN IF NOT EXISTS max_uses      INT  DEFAULT 1,
    ADD COLUMN IF NOT EXISTS used_count    INT  DEFAULT 0;

-- CHECK constraints are guarded so re-runs are idempotent.
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint WHERE conname = 'onboarding_keys_intent_chk'
    ) THEN
        ALTER TABLE onboarding_keys
            ADD CONSTRAINT onboarding_keys_intent_chk
            CHECK (intent IS NULL OR intent IN ('brokerage_setup', 'user_invite'));
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint WHERE conname = 'onboarding_keys_invited_role_chk'
    ) THEN
        ALTER TABLE onboarding_keys
            ADD CONSTRAINT onboarding_keys_invited_role_chk
            CHECK (invited_role IS NULL OR invited_role IN ('owner', 'agent', 'viewer'));
    END IF;
END $$;

-- Hash lookup index. Unique because two invites must never share a hash.
-- Existing rows (legacy plaintext-only) have NULL key_hash — the partial
-- unique index ignores them so it's safe to add on a populated table.
CREATE UNIQUE INDEX IF NOT EXISTS onboarding_keys_hash_idx
    ON onboarding_keys (key_hash)
    WHERE key_hash IS NOT NULL;


-- ── 4. audit_log ────────────────────────────────────────────────
-- Append-only audit trail. Soft references on actor_user_id /
-- brokerage_id (no FK) — mirrors the v6 pas_events precedent so an
-- audit row can never fail to land because a referenced row is gone.
-- Payload must never carry secrets; the application-side helper
-- redacts obvious secret fields before insert.
CREATE TABLE IF NOT EXISTS audit_log (
    id              BIGSERIAL    PRIMARY KEY,
    occurred_at     TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    actor_user_id   UUID,
    actor_email     TEXT,
    actor_type      TEXT         NOT NULL
                                 CHECK (actor_type IN ('admin', 'brokerage_user', 'legacy_key', 'system')),
    brokerage_id    TEXT,
    event_type      TEXT         NOT NULL,
    target          TEXT,
    payload         JSONB        NOT NULL DEFAULT '{}'::jsonb,
    request_id      TEXT,
    ip              TEXT
);

CREATE INDEX IF NOT EXISTS audit_log_brokerage_idx
    ON audit_log (brokerage_id, occurred_at DESC);

CREATE INDEX IF NOT EXISTS audit_log_event_idx
    ON audit_log (event_type, occurred_at DESC);

CREATE INDEX IF NOT EXISTS audit_log_actor_idx
    ON audit_log (actor_user_id, occurred_at DESC);

-- RLS parity with calls / bookings / pas_events: enable, no anon
-- policies, writes via service-role backend client.
ALTER TABLE audit_log ENABLE ROW LEVEL SECURITY;


-- ── Verification (reference — not executed) ─────────────────────
-- After running, these should each return a row:
--   SELECT to_regclass('public.admin_users');
--   SELECT to_regclass('public.brokerage_users');
--   SELECT to_regclass('public.audit_log');
--
-- And new columns should be present:
--   SELECT column_name FROM information_schema.columns
--   WHERE table_name = 'onboarding_keys'
--     AND column_name IN ('key_hash','key_lookup','intent',
--                         'invited_email','invited_role',
--                         'max_uses','used_count');
