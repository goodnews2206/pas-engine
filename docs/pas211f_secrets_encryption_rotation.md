# PAS211F — Secrets Encryption + Rotation (Runbook)

Reduces credential-exposure risk before paid-client real lead data enters PAS.
Focused on **secrets at rest, rotation readiness, and safe migration planning** —
not a full enterprise secrets manager, no new vendor, no new dependency.

## Current risk (from PAS211C)

- `brokerages.api_key`, `slack_signing_secret`, `slack_webhook_url` stored
  **plaintext** and (api_key + slack secrets) were returned by admin reads.
- Onboarding invite keys stored plaintext despite `key_hash`/`key_lookup`
  columns existing (migrate_v7).
- A local `.env` holds live-looking third-party credentials that should be
  treated as exposed to tooling and rotated.

## What changed in PAS211F

**Always on (no flag, no schema change):**
- **Admin reads redact secrets.** `GET /admin/brokerages` and
  `GET /admin/brokerages/{id}` no longer return `api_key`,
  `slack_signing_secret`, or `slack_webhook_url` (masked with `***redacted***`).
  Create/rotate still show the **raw api_key exactly once**; the create response
  also redacts the Slack secret.
- **Redaction helper** `app/services/security/secret_redaction.py`
  (`redact_brokerage`, `redact_secret_fields`).

**Behind `SECRETS_HASHING_ENABLED` (default OFF — compatibility phase):**
- **Hashing layer** `app/services/security/secret_hash.py` — deterministic
  peppered SHA-256 (stdlib only). High-entropy tokens are hashed for indexed
  lookup; an optional `SECRET_HASH_PEPPER` resists offline brute-force of a
  stolen DB.
- **Brokerage API keys**: when enabled, `create_brokerage` / `rotate_api_key`
  store `api_key_hash` and leave the plaintext column empty; the raw key is
  returned once. `get_brokerage_by_api_key` hashes the presented key and looks
  up by `api_key_hash`, with a **legacy plaintext fallback** so keys issued
  before activation keep working.
- **Invite keys**: same pattern using the existing `key_hash`/`key_lookup`
  columns; `claim_invite_key` does a hashed lookup with plaintext fallback.

**Slack signing secret / webhook URL:** these must be *recovered* at runtime
(to verify Slack signatures / post messages), so they need reversible
**encryption**, not hashing. PAS211F **does not encrypt them** — it (a) stops
returning them from admin reads, and (b) adds `*_enc` / `secret_kid` columns in
the migration proposal as the seam. Choosing key management (Supabase Vault /
pgcrypto / app-side cipher with a KMS-held key) is a deliberate follow-on; until
then they remain plaintext at rest. **Do not treat the columns' existence as
"encrypted".** (Documented residual risk.)

## Migration proposal

`scripts/migrate_v10_secrets_encryption_rotation.sql` — **proposal, NOT applied.**
Additive + idempotent (`ADD COLUMN IF NOT EXISTS`, partial unique index on
`api_key_hash`), **no destructive SQL**, legacy plaintext columns preserved for
the compatibility phase. Adds `brokerages.api_key_hash`, `api_key_version`,
`slack_signing_secret_enc`, `slack_webhook_url_enc`, `secret_kid`; re-asserts the
onboarding `key_hash`/`key_lookup` columns + lookup index.

### Phases
0. **Today** (code merged, migration NOT applied): admin reads redacted; hashing
   gated off → runtime behaviour unchanged.
1. **Apply `migrate_v10`** (operator, by hand in the Supabase SQL editor).
2. **Set `SECRETS_HASHING_ENABLED=true`** → new/rotated keys stored hashed; old
   keys still resolve via the plaintext fallback.
3. **Rotate every brokerage key** so no plaintext remains (verification query in
   the migration footer).
4. **Future cleanup migration** drops the legacy plaintext columns.

### Rollback / disable
Columns are additive + nullable → safe to leave. To revert behaviour, set
`SECRETS_HASHING_ENABLED=false` (legacy plaintext path resumes). No SQL rollback
needed.

## How to rotate the local `.env` secrets safely

> Do **not** print or paste secret values. Rotate at the provider, then update
> `.env` in your editor / secret store; never echo the value to a shell or log.

For each credential: generate a new value in the provider console, paste it into
`.env` (or your hosting secret store), restart the app, then revoke the old
value at the provider. Verify the app still boots (lifespan logs "configured")
and that the old value is rejected.

### Secrets that MUST be rotated before paid-client traffic
- **Supabase service-role key** (`SUPABASE_SERVICE_KEY`) — master DB access.
- **Twilio** auth token + API keys (`TWILIO_AUTH_TOKEN`, `TWILIO_API_KEY_SID`,
  `TWILIO_API_SECRET`).
- **Slack** signing secrets / webhook URLs — only if a real workspace was used.
- **Cal.com** key (`CALCOM_API_KEY`).
- **Deepgram** key (`DEEPGRAM_API_KEY`).
- **ElevenLabs** key (`ELEVENLABS_API_KEY`).
- **LLM provider** keys (`ANTHROPIC_API_KEY` / `OPENAI_API_KEY`).
- **Admin** key (`ADMIN_API_KEY`) — rotate and store strongly.

## How to verify secrets are not printed or returned

- Admin reads: `GET /admin/brokerages` and `/admin/brokerages/{id}` must show
  `***redacted***` for api_key / slack secrets (covered by PAS211F tests).
- Logs: `main.py` suppresses httpx URL logging; no code logs secret **values**
  (audit_log + this layer redact). Grep new code for accidental secret logging.
- `.env` is gitignored, untracked, never committed (verified) — keep it so.

## Paid-client readiness impact

PAS211F **stops exposing** tenant credentials through admin reads (immediate, no
flag) and ships a **safe, reversible activation path** to hash API/invite keys at
rest, plus a reviewable migration. It is a material reduction in credential blast
radius.

It does **not** fully close the secrets gap on its own: Slack secret encryption
is deferred to a key-management decision, and the hashing path is inert until an
operator applies `migrate_v10` + flips the flag + rotates existing keys. Combined
with rotating the live `.env` credentials, this clears the secrets blocker for a
**Conditionally Ready** paid-client pilot; the broader **Ready** verdict still
also depends on PAS211G (JWT/RBAC + RLS enforcement).
