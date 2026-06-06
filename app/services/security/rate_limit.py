"""PAS-SECURITY-02 (PAS209.7 minimal runtime repair) — per-surface rate limit.

This is the **minimal import-repair** reconstruction of the original
PAS-SECURITY-02 service, scoped to what the committed runtime actually
imports today: ``check_rate_limit`` (used by app/routes/slack_command.py).

Differences from the original (intentional, see PAS209.6 triage):

* The original wrapped a durable, brokerage-scoped counter store
  (``app.services.security.rate_limit_store`` + Supabase) so counters
  survived process restarts. That store is a deferred rebuild (PAS211),
  so this repair uses a **process-local fixed-window counter** instead.
  No DB, no network, no new dependencies.

Doctrine preserved from the original spec:

* **Conservative defaults.** A safe baseline is hard-coded per surface.
* **Brokerage-scoped where possible.** When ``brokerage_id`` is present
  the bucket is keyed on it; otherwise a hashed anonymous fingerprint.
* **No raw IP / secret stored.** Bucket keys are sha256 fingerprints.
* **NEVER raises.** Every helper returns a structural envelope.
* **Failure isolation / fail-open.** Any internal error falls back to
  ``allowed=True`` so a limiter fault never deadlocks production traffic.
"""
from __future__ import annotations

import hashlib
import logging
import threading
import time
from typing import Any, Dict, Optional

logger = logging.getLogger("pas.security.rate_limit")

# Closed enums (kept for callers/tests; not broadened beyond the spec surface).
ALLOWED_SURFACES = ("slack_command", "email_ingestion", "admin", "tenant_api")
ALLOWED_ACTOR_TYPES = ("TENANT", "OPERATOR", "ANON")

# surface -> {limit, window_seconds}. Conservative baseline (per-window cap).
DEFAULT_POLICIES: Dict[str, Dict[str, int]] = {
    "slack_command":   {"limit": 30,  "window_seconds": 60},
    "email_ingestion": {"limit": 60,  "window_seconds": 60},
    "admin":           {"limit": 60,  "window_seconds": 60},
    "tenant_api":      {"limit": 120, "window_seconds": 60},
}
# Used for any unknown surface — tight by default.
_FALLBACK_POLICY: Dict[str, int] = {"limit": 30, "window_seconds": 60}

# Process-local counter state: (surface, bucket, window_index) -> count.
_lock = threading.Lock()
_counters: Dict[tuple, int] = {}


def resolve_rate_limit_policy(surface: str) -> Dict[str, int]:
    """Closed lookup — returns a copy so callers cannot mutate the table."""
    return dict(DEFAULT_POLICIES.get(surface, _FALLBACK_POLICY))


def _sha256_hex(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8", "replace")).hexdigest()


def build_rate_limit_bucket_key(
    surface: str,
    brokerage_id: Optional[str],
    actor_type: str,
    actor_fingerprint: Optional[str] = None,
) -> str:
    """Deterministic bucket key. Raw IP is never stored — only its sha256."""
    if brokerage_id:
        actor = f"brokerage:{brokerage_id}"
    elif actor_fingerprint:
        actor = f"anon:{_sha256_hex(actor_fingerprint)}"
    else:
        actor = "anon:unknown"
    return _sha256_hex(f"{surface}|{actor_type}|{actor}")


def _prune_other_windows(surface: str, bucket: str, current_window: int) -> None:
    """Drop stale windows for this bucket so the dict cannot grow unbounded."""
    stale = [
        k for k in _counters
        if k[0] == surface and k[1] == bucket and k[2] != current_window
    ]
    for k in stale:
        _counters.pop(k, None)


def check_rate_limit(
    surface: str,
    brokerage_id: Optional[str] = None,
    actor_type: str = "ANON",
    actor_fingerprint: Optional[str] = None,
    now: Optional[float] = None,
) -> Dict[str, Any]:
    """Increment the per-window counter and return a verdict envelope.

    Returns ``{"allowed": bool, ...}``. Fail-open: on any internal error
    returns ``{"allowed": True, "fail_open": True}`` so production traffic
    is never blocked by a limiter fault.
    """
    try:
        policy = resolve_rate_limit_policy(surface)
        limit = int(policy["limit"])
        window = int(policy["window_seconds"])
        t = time.time() if now is None else float(now)
        window_index = int(t // window)
        bucket = build_rate_limit_bucket_key(
            surface, brokerage_id, actor_type, actor_fingerprint
        )
        key = (surface, bucket, window_index)
        with _lock:
            _prune_other_windows(surface, bucket, window_index)
            count = _counters.get(key, 0) + 1
            _counters[key] = count
        allowed = count <= limit
        return {
            "allowed": allowed,
            "surface": surface,
            "limit": limit,
            "window_seconds": window,
            "count": count,
            "bucket": bucket,
        }
    except Exception:  # pragma: no cover - defensive fail-open
        logger.warning("rate_limit check failed; failing open", exc_info=False)
        return {"allowed": True, "surface": surface, "fail_open": True}


def rate_limit_public_error(verdict: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Closed 429-style public envelope — never leaks the policy or bucket key."""
    return {
        "error": "rate_limited",
        "status": 429,
        "message": "Rate limit reached. Please wait a moment and retry.",
    }
