# PAS211J — Twilio Webhook URL Pinning + Replay Guard

Hardens Twilio webhook authenticity and replay resistance before paid-client
voice traffic enters PAS. No voice business logic, prompts, outbound automation,
UI, JWT/RBAC, or RLS work is in scope here — this checkpoint only changes *how a
Twilio webhook is authenticated*.

## Audit finding addressed (PAS211C)

The Twilio signature check rebuilt the signed URL from request headers:

```python
proto = request.headers.get("X-Forwarded-Proto", request.url.scheme)
host  = request.headers.get("X-Forwarded-Host", request.headers.get("host", ...))
url   = f"{proto}://{host}{request.url.path}"
```

`X-Forwarded-Proto` / `X-Forwarded-Host` / `Host` are client-controlled. An
attacker able to set them could steer the URL that the validator reconstructs,
weakening the guarantee that the `X-Twilio-Signature` was computed for *our*
endpoint. There was also **no replay protection**: a captured, validly-signed
request could be replayed.

## URL pinning strategy

`_pinned_webhook_url()` derives the URL used for verification from the configured
`BASE_URL`, plus the real route path and query string — never from forwarded
headers:

```
verify_url = BASE_URL.rstrip("/") + request.url.path  [+ "?" + request.url.query]
```

- A captured signature is only valid for the URL Twilio was configured to call.
  Pinning to `BASE_URL` means forwarded/Host headers an attacker controls cannot
  move the verification target. Tests assert a signature valid for `BASE_URL`
  still passes even with spoofed `X-Forwarded-Host/Proto`, while a signature
  computed for the spoofed host **fails**.
- The route path and query string are preserved so multi-path / query-bearing
  callbacks still verify against the exact URL Twilio signed.
- **Fail closed:** if `BASE_URL` is empty or not an `http(s)://` URL,
  `_pinned_webhook_url()` returns `""` and `_verify_twilio()` returns `False`,
  so the request is rejected (403) rather than verified against a guessed URL.
  This complements the existing PAS211A startup guard
  (`validate_runtime_security`), which already refuses to boot a production-like
  host left on a non-production `ENVIRONMENT`.

Forwarded headers are deliberately **not** consulted for the signed URL even when
`TRUST_PROXY_HEADERS=true` — that flag governs per-IP rate-limit attribution
(`client_ip`), not signature authenticity. Pinning to `BASE_URL` is strictly
stronger than trusting a proxy header.

## Replay guard strategy

Twilio, unlike Slack, sends **no request-timestamp header**, so replays cannot be
bounded by clock skew (Slack uses `X-Slack-Request-Timestamp` with a ±300s
window). Instead we dedupe on the signature itself:

- `X-Twilio-Signature` is an HMAC-SHA1 over the exact (signed-URL, sorted-POST-
  params) tuple. A byte-for-byte replay carries an **identical** signature; any
  genuinely distinct webhook (different `CallSid`/params/route) produces a
  different one. The signature therefore already binds both the route and the
  body — keying the cache on `path|signature` is belt-and-braces.
- `app/utils/twilio_replay.py` keeps a process-local TTL cache of recently-seen
  `path|signature` keys. The replay window defaults to **300s (5 minutes)** —
  conservative, matching the Slack guard. The first delivery is recorded and
  accepted; a duplicate within the window is rejected with `403 Duplicate Twilio
  request (replay)`.
- The replay check runs **after** signature verification, so only authentic
  requests are ever cached — an attacker cannot flood the cache with forged
  signatures.

## Production behaviour

`require_twilio_signature` is `True` in every non-development environment
(PAS211A). For `/twilio/voice` and `/twilio/status`:

1. Per-IP rate limit (PAS211D) — unchanged.
2. BASE_URL-pinned signature verification — forged/invalid → `403`.
3. Replay rejection — duplicate signed request within 5 min → `403`.

Missing/invalid `BASE_URL` fails closed (`403`).

## Local / development behaviour

In explicit `ENVIRONMENT=development`, `require_twilio_signature` is `False`, so
`_reject_unverified_or_replayed()` is a no-op: local calls work without live
Twilio signatures, and no replay bookkeeping occurs. This preserves the existing
developer/sales loop. Rate limits still apply.

## Process-local limitation

The replay cache lives in process memory. In a multi-worker or multi-host
deployment each worker has its own cache, so a replay routed to a *different*
worker than the original is not caught. This is acceptable for PAS211J (it raises
the bar materially with zero new infrastructure) but is **not** a complete replay
defence on its own.

A legitimate Twilio retry of a *failed* delivery reuses the signature and would
be treated as a replay; this is acceptable because Twilio does not retry a
delivery that already returned `2xx`, and the handlers complete their work before
responding.

## Remaining deferred gaps

- **Durable / shared replay protection** (cross-worker, cross-host) — deferred to
  **PAS214P**. Candidates: a short-TTL Redis/DB-backed seen-signature set.
- No change to voice business logic, outbound automation, or media-stream
  authentication; those remain as-is.

## Paid-client readiness impact

Closes the spoofable-URL signature gap and adds first-line replay resistance on
the two Twilio callback surfaces that paid-client voice traffic depends on
(`/voice`, `/status`). Combined with PAS211A (enforcement seam) and PAS211D
(rate limits), Twilio webhook ingress is now fail-closed, URL-pinned, throttled,
and single-process replay-resistant. The remaining multi-process replay gap is
explicitly tracked for PAS214P.
