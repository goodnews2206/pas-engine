# PAS211D — Critical Security Fix Pack 1

Closes the most immediately exploitable issues from the **PAS211C** audit. This
is a focused, minimal, paid-client-facing fix pack — **not** full RLS hardening,
secrets encryption, JWT/RBAC, prompt-injection safety, or performance work
(those remain PAS211E/F/G/H/I/J and PAS214P).

## Scope

| Audit finding | Severity | Status |
|---|---|---|
| `/simulate-call` unauthenticated, body-driven `brokerage_id`, writes real tenant data + fires notifications | Critical | **Fixed** |
| `/demo/token` unauthenticated, wildcard CORS, mints live Twilio tokens | Critical (toll-fraud) | **Fixed** |
| Admin key compared with non-constant-time `!=` | High | **Fixed** |
| Rate limiter trusts raw `X-Forwarded-For` | High | **Fixed** |
| Sensitive routes missing rate limits (`/demo/token`, `/twilio/status`, `/onboarding/claim`) | High/Medium | **Fixed** |

## New configuration

Two settings in `app/config.py` (both default to the **safe** value):

- `ENABLE_DEMO_ENDPOINTS` (default `False`) — in **production**, `/simulate-call`
  and `/demo/token` return `404` unless this is explicitly set `true`. Outside
  production they remain available. Exposed as `Settings.demo_endpoints_allowed`.
- `TRUST_PROXY_HEADERS` (default `False`) — only when `true` does the rate
  limiter honour `X-Forwarded-For`; otherwise it keys on the real peer
  (`request.client.host`). Set this `true` **only** when PAS runs behind a
  trusted reverse proxy that sets a reliable `X-Forwarded-For`.

## Routes hardened

### `/simulate-call` ([app/routes/simulate.py](../app/routes/simulate.py))
- **Production gate:** `404` unless `demo_endpoints_allowed`.
- **Tenant authorization (`_authorize_simulation`):** anonymous callers may only
  simulate the `demo` tenant. Simulating a real `brokerage_id` now **requires
  that brokerage's own `X-API-Key`**, and the key's tenant must match the
  requested id (`401` if no key, `403` on mismatch/unknown). An anonymous caller
  can no longer drive the engine against a real tenant, so the finalize path can
  no longer upsert real lead memory or fire real-tenant Slack/email alerts for an
  attacker-chosen brokerage.

### `/demo/token` ([app/routes/demo.py](../app/routes/demo.py))
- **Production gate:** `404` unless `demo_endpoints_allowed` (no live Twilio voice
  grant minted anonymously in production).
- **CORS:** `Access-Control-Allow-Origin` is `*` **only in development**; in any
  other environment it is restricted to the configured `BASE_URL` origin
  (token + preflight + 503 paths).
- **Rate limit:** per-IP `10/min`.

### `/twilio/status` ([app/routes/twilio_webhook.py](../app/routes/twilio_webhook.py))
- Added per-IP rate limit `120/min` (previously unlimited). Runs before the
  existing Twilio signature check, which is unchanged.

### `/onboarding/claim` ([app/routes/onboarding.py](../app/routes/onboarding.py))
- Added per-IP rate limit `10/min` to blunt brute-force enumeration of the
  invite-key space (the endpoint returns a brokerage `api_key` on success).

### Admin auth ([app/routes/admin.py](../app/routes/admin.py))
- `require_admin` now uses `hmac.compare_digest` (constant-time) instead of `!=`.
  An empty configured `ADMIN_API_KEY` still rejects; the weak/empty-key
  production startup refusal in `app/main.py` is unchanged.

### Rate-limit client IP ([app/utils/rate_limiter.py](../app/utils/rate_limiter.py))
- `client_ip` no longer trusts `X-Forwarded-For` by default; it uses the real
  peer unless `TRUST_PROXY_HEADERS=true`. This prevents header-rotation bypass of
  every per-IP limit (`/simulate-call`, `/outbound/call`, `/ingest/lead`,
  `/twilio/voice`, and the new limits above).

## Production behaviour — before → after

| Surface | Before | After |
|---|---|---|
| `POST /simulate-call` (prod) | Open; writes any `brokerage_id` from body; fires notifications | **404** (unless `ENABLE_DEMO_ENDPOINTS=true`) |
| `GET /demo/token` (prod) | Open; CORS `*`; mints live Twilio token | **404** (unless `ENABLE_DEMO_ENDPOINTS=true`); CORS = site origin; rate limited |
| Rate-limit key | First `X-Forwarded-For` hop (spoofable) | Real peer IP (unless `TRUST_PROXY_HEADERS=true`) |
| Admin key compare | `!=` (timing-leak) | `hmac.compare_digest` |
| `/twilio/status`, `/onboarding/claim` | No rate limit | Per-IP limited |

## Local / demo behaviour — before → after

- **Unchanged for local development.** With `ENVIRONMENT=development`,
  `/simulate-call` and `/demo/token` remain available, and `/demo/token` keeps
  CORS `*` for the website widget.
- The **only** new local constraint: simulating a *non-demo* `brokerage_id`
  requires that brokerage's `X-API-Key` (demo simulation is unchanged and needs
  no key). This is the intended anti-poisoning guard.
- Behind a real proxy, set `TRUST_PROXY_HEADERS=true` so per-IP limits see real
  client IPs; otherwise all traffic shares the proxy's IP bucket (safe, but
  coarser).

## Remaining gaps (deferred — NOT in PAS211D)

- **PAS211E — Tenant isolation / RLS:** no DB-level RLS policies; several store
  functions mutate by global PK without a `brokerage_id` predicate.
- **PAS211F — Secrets encryption + rotation:** plaintext `brokerages.api_key` /
  `slack_signing_secret` / onboarding keys; rotate the live `.env` credentials.
- **PAS211G — Admin/operator auth hardening:** single static admin key, no
  rotation, no per-operator identity; JWT/RBAC scaffolding (`app/auth/*`) unwired.
- **PAS211H — Prompt & memory injection safety:** self-training transcript →
  persisted system prompt; undelimited lead text in objection/summary prompts.
- **PAS211I — Readiness gate cleanup + PII/retention:** retire/redirect the 8
  stale readiness-gate tests; add deletion/export + retention; minimize PII in
  logs/`pas_events`.
- **PAS211J — Webhook hardening:** pin Twilio signed URL to `BASE_URL`; add
  replay/nonce protection.
- **PAS211K / PAS214P — Durable/shared rate limiting** (the current limiter is
  process-local) and full trusted-proxy CIDR validation; region/timezone.

## Paid-client readiness impact

PAS211D removes the **anonymous, internet-reachable** attack paths that let any
caller poison a tenant's data, trigger that tenant's notifications, or mint
billable Twilio calls — and closes the admin-key timing leak and the
rate-limit-bypass header trick. This moves the most acute "anyone on the
internet" exposure off the table.

It does **not** by itself make PAS *Ready* for paying-client real lead data: the
PAS211C verdict stays **Conditionally Ready at best** until at least PAS211E
(tenant isolation/RLS) and the PAS211F secrets items are also done. PAS211D is a
necessary first gate, not the finish line.
