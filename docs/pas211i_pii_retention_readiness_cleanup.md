# PAS211I — PII / Retention / Readiness-Gate Cleanup

Reduces PII leakage into logs/events/errors, defines a retention/deletion/export
**posture** (not a full implementation), and retires the stale readiness-gate
self-checks. Not full GDPR/CCPA, no data-subject portal, no UI, no new vendor.

## What PAS stores today

| Store | Contents | PII? |
|---|---|---|
| `leads` | name, phone, email, intent/budget/timeline, notes, counts | **Yes** (contact + qualification) |
| `calls` | transcript, summary, phone, outcome, metadata | **Yes** (transcript + phone) |
| `bookings` | lead name/phone/email, slot, status | **Yes** |
| `pas_events` | operational event stream (categories, statuses, ids, booleans) | **Minimized** (see below) |
| `error_logs` | service errors (message/detail) | **Redacted** (PAS211I) |
| `onboarding_keys` | invite keys | secret-bearing (hashed path in PAS211F) |
| memory candidates | aggregated/sanitized summaries | no raw PII (sanitized PAS211H) |

## PII categories & where they appear

- **Contact:** phone, email, name → `leads`, `calls`, `bookings`, Slack handoff
  notifications. **Logs now mask** phone (websocket, lead_memory) and never log
  full transcripts at INFO.
- **Content:** transcript, objection/callback text → `calls.transcript` (stored,
  needed for summary/training); **no longer copied raw into `pas_events`**.
- **Secret-shaped:** API keys/tokens → redacted from error records (PAS211I) and
  admin reads (PAS211F).

## What was minimized in this checkpoint

- **`pas_events`:** `lead.extracted` drops `raw_text` (→ `raw_text_len`);
  `objection.detected` drops the raw `text` (→ `text_len` + kept `category`);
  `callback.requested` drops `trigger_excerpt` (→ `trigger_len`);
  `call.ended_with_callback` keeps the reason but **PII-redacted**. Ingestion
  events remain PII-free (has_email/has_message booleans + opaque dedupe hash).
- **Logs:** full transcript no longer logged at INFO (length only; redacted at
  DEBUG); caller/agent phone masked (`websocket_handler`); lead phone masked in
  `lead_memory` logs.
- **error_store:** `message`/`detail` are run through `sanitize_error_message`
  (redacts phone/email/secret tokens) before they reach `pas_events`,
  `error_logs`, and the admin dashboard.
- **Slack:** `sanitize_slack_payload` is wired at both Slack send boundaries
  (`slack_client._post_to_slack`, `slack_sender.send_slack_notification`) so no
  secret-shaped token leaves PAS in a Slack payload; webhook URLs are scrubbed
  from error logs (see Slack posture).
- **Utilities:** `app/services/security/pii_safety.py` — `mask_phone`,
  `mask_email`, `mask_name_if_needed`, `redact_pii`, `sanitize_error_message`,
  `sanitize_event_payload`, `sanitize_log_payload`, `sanitize_slack_payload`
  (deterministic, stdlib-only, never logs raw text).

> **Event payload safety is targeted, not centralized.** PAS211I minimizes PII
> at the specific `pas_events` call sites that carried raw spoken text (above),
> rather than wrapping `event_logger.log_event` in `sanitize_event_payload`. A
> centralized event backstop is **deferred**: a blanket sanitizer at the logger
> boundary would rewrite every event payload (masking/redacting structured
> values) and risk broad regressions to existing event-contract assertions. The
> `sanitize_event_payload` / `sanitize_log_payload` helpers exist for callers and
> for a future, separately-validated centralization pass.

## What remains intentionally stored

- `calls.transcript` + `calls.summary` — required for the summary, self-training,
  and operator review features. This is the primary at-rest PII and the main
  target of the retention/deletion roadmap below.
- `leads`/`bookings` contact details — the product's operational core.
- Slack notifications intentionally include lead name/phone/email for **agent
  handoff** (see Slack posture).

## Slack / notification PII posture

Slack lead notifications deliberately carry lead contact details so a human agent
can follow up — this is a feature, not a leak. PAS211I guarantees **no secret**
appears in a Slack payload: `sanitize_slack_payload` is **wired into both Slack
send transports** — `slack_client._post_to_slack` (Block Kit call summaries /
agent reminders) and `slack_sender.send_slack_notification` (text lead alerts) —
so every outgoing payload is stripped of secret-shaped tokens at the send
boundary while contact handoff is preserved. The webhook URL (itself a
bearer-secret) is never logged: both transports scrub it (and any token) out of
exception strings before logging, and never log the raw unsanitized payload.
**The Slack workspace is a customer-controlled destination**: lead contact PII in
Slack is an **intentional operational handoff** and must be covered in the
deployment / Data Processing Agreement (the brokerage owns and governs who can
read that channel).

## Recommended retention policy

- **Transcripts (`calls.transcript`):** retain 30–90 days for operations, then
  purge or anonymize. Configurable per brokerage.
- **`pas_events`:** retain 90–180 days (already PII-minimized).
- **`error_logs`:** retain 90 days (already redacted).
- **`leads`/`bookings`:** retain for the customer relationship lifetime; honor
  per-lead deletion on request.

## Deletion / anonymization roadmap (not implemented here)

1. `delete_lead(brokerage_id, lead_id)` — hard-delete the lead + its calls/
   bookings, or anonymize (null contact fields, keep aggregates).
2. Transcript purge job — scheduled anonymizer over `calls.transcript` past the
   retention window.
3. Brokerage off-boarding — cascade delete/anonymize a tenant's data (today
   brokerage delete is a **soft** deactivate that preserves data).

## Export roadmap (not implemented here)

- `export_brokerage_data(brokerage_id)` — tenant-scoped dump of leads/calls/
  bookings/events for a data-subject access/portability request (GDPR Art.
  15/20). Read-only, tenant-scoped (reuses PAS211E scoping).

## Paid-client disclosure / DPA notes

- Disclose: transcripts and lead contact details are stored; Slack notifications
  send contact details to the brokerage's own workspace; data is processed in the
  Supabase region configured for the deployment (see PAS214P).
- Provide a DPA covering sub-processors (Twilio, Deepgram, ElevenLabs, the LLM
  provider, Cal.com, Supabase) and the retention windows above.
- Until the deletion/export endpoints land, data-subject requests are handled
  **operationally** (manual SQL by an operator) — document this interim process.

## Readiness-gate cleanup

The PAS191 gate previously reported `NOT_READY` because
`check_prior_phases_intact`, `check_memory_review_intact`, and
`check_worker_off_by_default` asserted the presence of artifacts that were
**intentionally retired during the PAS209.5 recovery/reconciliation**
(`scripts/pas160–pas190*`, `pas_launch_integrity`, `pas_security_*`, the
PAS147–155 Memory Review module, and `app/services/ingestion/worker.py`).

PAS211I:
- Rewrote those three checks so a **still-present** artifact is asserted intact
  (PASS) while **retired** ones are reported as a single **non-blocking note** —
  no per-file BLOCK. The strict worker off-by-default guard is preserved for if
  the worker module ever returns.
- **Retired** the 5 stale `test_pas18x_carry_forward_ready` tests (they shelled
  now-absent scripts) and replaced them with a guard asserting those historical
  scripts stay absent (so nobody recreates dead scripts to satisfy a stale test).
- Did **not** recreate any deleted script. The PAS191 gate now reports
  `verdict=READY, blockers=0`, and the 8 previously-failing readiness-gate tests
  pass — the suite no longer carries that stale-failure noise. Meaningful checks
  (PAS191 files, event-contract types, doc clauses, security posture) are intact.

## What remains for full compliance later

Deletion + export endpoints, a scheduled retention/anonymization job, a
data-subject-request workflow, and per-tenant retention configuration —
sequenced after the auth/RLS enforcement work (PAS211G.2+) so deletes/exports run
under enforced tenant isolation.
