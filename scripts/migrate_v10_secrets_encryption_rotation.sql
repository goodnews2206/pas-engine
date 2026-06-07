-- ─────────────────────────────────────────────────────────────────
-- PAS — Migration v10 (PAS211F)
-- Secrets-at-rest: API-key hashing + rotation readiness + encryption columns.
-- Run in Supabase SQL Editor → Run All. Safe to re-run (IF NOT EXISTS).
--
-- STATUS: PROPOSAL — NOT auto-applied by any code path. Apply by hand.
--
-- This migration is ADDITIVE ONLY:
--   - No column/table/constraint is dropped or altered.
--   - Legacy plaintext columns (brokerages.api_key, .slack_signing_secret,
--     .slack_webhook_url; onboarding_keys.key) are KEPT for the compatibility
--     phase and removed only in a LATER, separate cleanup migration once every
--     credential has been re-issued in hashed/encrypted form.
--
-- ── PHASES ───────────────────────────────────────────────────────
-- Phase 0 (today, code merged, this migration NOT applied):
--   * Admin reads already redact api_key / slack_signing_secret /
--     slack_webhook_url (app-level, no schema change).
--   * Hashing code paths are gated behind SECRETS_HASHING_ENABLED=false.
-- Phase 1 (apply THIS migration):
--   * Adds api_key_hash + api_key_version to brokerages, and the *_enc /
--     *_kid columns for the eventual Slack-secret encryption.
--   * onboarding_keys.key_hash / key_lookup already exist (migrate_v7).
-- Phase 2 (set SECRETS_HASHING_ENABLED=true):
--   * New/rotated brokerage API keys + new invite keys are stored HASHED;
--     the plaintext column is written empty. Lookups hash the presented value;
--     a legacy plaintext fallback keeps pre-existing keys working.
-- Phase 3 (operational): rotate every brokerage key so no plaintext remains,
--   then (Phase 4, future migration) drop the legacy plaintext columns.
--
-- ── ENCRYPTION NOTE (Slack secret / webhook) ─────────────────────
-- slack_signing_secret + slack_webhook_url must be RECOVERED at runtime (to
-- verify Slack signatures / post messages), so they need reversible encryption,
-- not hashing. This migration adds the columns (slack_signing_secret_enc,
-- slack_webhook_url_enc, secret_kid) but does NOT itself encrypt anything —
-- choosing a key-management approach (Supabase Vault / pgcrypto / app-side
-- Fernet via a KMS-held key) is an explicit decision tracked separately. Until
-- that is wired, those secrets remain plaintext at rest in the legacy columns;
-- the residual risk is documented in docs/pas211f_secrets_encryption_rotation.md.
-- DO NOT treat the presence of these columns as "Slack secrets are encrypted".
--
-- ── ROLLBACK / DISABLE ───────────────────────────────────────────
-- This migration only ADDS nullable columns, so it is safe to leave in place.
-- To disable the hashed-write behaviour at runtime, set
-- SECRETS_HASHING_ENABLED=false (the legacy plaintext path resumes). No SQL
-- rollback is required; if you must remove the columns, do so in a dedicated
-- cleanup migration after confirming nothing references them.
-- ─────────────────────────────────────────────────────────────────


-- ── brokerages: hashed API key + version + encryption columns ────
ALTER TABLE brokerages
    ADD COLUMN IF NOT EXISTS api_key_hash             TEXT,
    ADD COLUMN IF NOT EXISTS api_key_version          INT  DEFAULT 1,
    ADD COLUMN IF NOT EXISTS slack_signing_secret_enc TEXT,
    ADD COLUMN IF NOT EXISTS slack_webhook_url_enc    TEXT,
    ADD COLUMN IF NOT EXISTS secret_kid               TEXT;

-- Unique-ish lookup index on the hash. Partial so legacy rows (NULL hash) are
-- ignored and the existing plaintext api_key continues to work meanwhile.
CREATE UNIQUE INDEX IF NOT EXISTS brokerages_api_key_hash_idx
    ON brokerages (api_key_hash)
    WHERE api_key_hash IS NOT NULL;


-- ── onboarding_keys: key_hash / key_lookup already exist (v7) ────
-- Re-assert idempotently so v10 is self-contained even if v7's columns are
-- somehow absent. No-op when they already exist.
ALTER TABLE onboarding_keys
    ADD COLUMN IF NOT EXISTS key_hash   TEXT,
    ADD COLUMN IF NOT EXISTS key_lookup TEXT;

CREATE INDEX IF NOT EXISTS onboarding_keys_key_lookup_idx
    ON onboarding_keys (key_lookup)
    WHERE key_lookup IS NOT NULL;


-- ── Verification (reference — not executed) ─────────────────────
-- New columns present:
--   SELECT column_name FROM information_schema.columns
--   WHERE table_name='brokerages'
--     AND column_name IN ('api_key_hash','api_key_version',
--                         'slack_signing_secret_enc','slack_webhook_url_enc',
--                         'secret_kid');
--
-- After Phase 3 (all keys rotated), this should return 0 rows — i.e. no
-- brokerage still has a non-empty plaintext api_key:
--   SELECT count(*) FROM brokerages WHERE COALESCE(api_key,'') <> '';
