"""PAS211J — process-local replay guard for signed Twilio webhooks.

Twilio (unlike Slack) sends no request-timestamp header, so replays cannot be
bounded by clock skew the way ``_verify_slack_signature`` does. Instead we dedupe
on the ``X-Twilio-Signature`` itself: that header is an HMAC-SHA1 over the exact
(signed-URL, sorted-POST-params) tuple, so a byte-for-byte replay of a captured
signed request carries an identical signature, while any genuinely distinct
webhook (different CallSid / params / route) produces a different one. We
remember recently-seen signatures for a short TTL and reject duplicates inside
that window.

The cache key folds in the request path as well, so the same signature can never
be cross-replayed onto a different route (the signature already binds the path —
this is belt-and-braces).

Limitations (see docs/pas211j_twilio_webhook_hardening.md):
  * Process-local only — a multi-worker / multi-host deployment keeps one cache
    per process, so a replay routed to a *different* worker is not caught.
    Durable, shared replay protection is deferred to PAS214P.
  * A legitimate Twilio retry of a *failed* delivery reuses the signature and is
    treated as a replay. This is acceptable: Twilio does not retry a delivery
    that already returned 2xx, and our handlers do their work before responding.
"""

import time

# 5 minutes — conservative replay window, matching the Slack signing guard.
DEFAULT_TTL_SECONDS = 300

# key -> first-seen monotonic timestamp
_seen: dict[str, float] = {}


def _prune(now: float, ttl: float) -> None:
    """Drop entries older than the TTL so the cache stays bounded by traffic in
    the last ``ttl`` seconds rather than growing without limit."""
    for k in [k for k, t in _seen.items() if now - t >= ttl]:
        _seen.pop(k, None)


def is_replay(path: str, signature: str, ttl_seconds: float = DEFAULT_TTL_SECONDS) -> bool:
    """Return True if this (path, signature) pair was already seen within the TTL
    window — i.e. a replay — otherwise record it now and return False.

    An empty signature is never treated as a replay: callers verify the signature
    BEFORE calling this, so an empty value only reaches here in non-enforcing
    (development) mode, where replay protection is intentionally off.
    """
    if not signature:
        return False
    now = time.monotonic()
    _prune(now, ttl_seconds)
    key = f"{path}|{signature}"
    if key in _seen:
        return True
    _seen[key] = now
    return False


def reset() -> None:
    """Clear the cache. Test helper / operational reset; not used in the request
    path."""
    _seen.clear()
