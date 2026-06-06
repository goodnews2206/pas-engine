"""PAS210 — Live Operational Snapshot Bridge (read-only, feature-flagged).

Bridges the already-built PAS205 observer / PAS207 needs-attention surface from
the deterministic DEMO snapshot to **real per-tenant Supabase data** via the
PAS206 read-only adapter — without changing any observer, renderer, or Slack
matcher logic.

Hard doctrine (sacrosanct for PAS210):

* **Read-only.** This module never writes, schedules, sends, or mutates. It
  only selects a per-tenant snapshot and hands it to the existing observer.
* **Feature-flagged.** Behaviour is governed by a single env flag,
  ``PAS_LIVE_OPERATIONAL_SNAPSHOT_ENABLED``. Missing or anything other than the
  literal ``"true"`` → current demo behaviour is unchanged.
* **Tenant-scoped, fail-closed.** Live mode REQUIRES a non-empty
  ``brokerage_id``. Missing tenant → explicit *unavailable* state. The tenant is
  never inferred, never queried across tenants, never defaulted.
* **No silent fallback / no silent mixing.** A live-adapter failure yields an
  explicit, clearly-labelled *unavailable* state — never a silent fall-back to
  demo data and never a blend of demo + live rows.
* **Source-transparent.** Every result carries a ``source_mode`` of ``demo``,
  ``live``, or ``unavailable`` so callers (and users) always know what produced
  the answer.
"""
from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import Any, Callable, Optional

from app.services.proactive.observer_models import ObservedSnapshot
from app.services.proactive.supabase_snapshot_adapter import load_snapshot
from app.services.slack.proactive_digest_intent import (
    build_demo_snapshot,
    format_needs_attention_response,
    match_needs_attention_intent,
    try_route_needs_attention,
)

logger = logging.getLogger("pas.proactive.live_snapshot_bridge")

# The single PAS210 feature flag. Literal "true" enables live mode; anything
# else (including unset) preserves current demo behaviour.
LIVE_SNAPSHOT_FLAG = "PAS_LIVE_OPERATIONAL_SNAPSHOT_ENABLED"

SOURCE_MODE_DEMO = "demo"
SOURCE_MODE_LIVE = "live"
SOURCE_MODE_UNAVAILABLE = "unavailable"

_LIVE_HEADER = (
    "🔎 Source: *live operational data* (brokerage `{bid}`). "
    "Read-only — I only watch.\n\n"
)
_UNAVAILABLE_NO_TENANT = (
    "⚠️ Live operational view is enabled, but no brokerage context was provided. "
    "I won't guess across tenants, so I can't show live data here. "
    "_(source: unavailable)_"
)
_UNAVAILABLE_ADAPTER = (
    "⚠️ Live operational data is temporarily unavailable for this brokerage. "
    "I won't silently fall back to rehearsal data. Please retry shortly. "
    "_(source: unavailable)_"
)

SnapshotProvider = Callable[[], ObservedSnapshot]
ClientFactory = Callable[[], Any]


def live_snapshot_enabled() -> bool:
    """True only when the flag is the literal string ``"true"``."""
    return os.environ.get(LIVE_SNAPSHOT_FLAG) == "true"


def _default_client_factory() -> Any:
    """Lazy import of the production Supabase singleton (kept out of module
    import so this module loads with no DB and tests can inject a stub)."""
    from app.db.supabase_client import get_supabase

    return get_supabase()


@dataclass(frozen=True)
class SnapshotResolution:
    """Outcome of resolving which snapshot to use for a request."""

    snapshot: Optional[ObservedSnapshot]
    source_mode: str
    available: bool
    brokerage_id: Optional[str]
    detail: str


def resolve_snapshot(
    brokerage_id: Optional[str],
    *,
    client_factory: Optional[ClientFactory] = None,
    demo_provider: Optional[SnapshotProvider] = None,
) -> SnapshotResolution:
    """Decide demo vs. live vs. unavailable. Never raises."""
    demo_provider = demo_provider or build_demo_snapshot

    # Flag off / missing → unchanged demo behaviour.
    if not live_snapshot_enabled():
        return SnapshotResolution(
            snapshot=demo_provider(),
            source_mode=SOURCE_MODE_DEMO,
            available=True,
            brokerage_id=brokerage_id,
            detail="flag_off_demo",
        )

    # Flag on. Tenant is mandatory — fail closed, never infer.
    if not isinstance(brokerage_id, str) or not brokerage_id.strip():
        return SnapshotResolution(
            snapshot=None,
            source_mode=SOURCE_MODE_UNAVAILABLE,
            available=False,
            brokerage_id=None,
            detail="brokerage_id_required",
        )

    # Flag on + tenant present → tenant-scoped live read via PAS206.
    try:
        factory = client_factory or _default_client_factory
        client = factory()
        result = load_snapshot(client, brokerage_id)
        return SnapshotResolution(
            snapshot=result.snapshot,
            source_mode=SOURCE_MODE_LIVE,
            available=True,
            brokerage_id=brokerage_id,
            detail="live_ok",
        )
    except Exception:
        # No silent demo fallback — surface an explicit unavailable state.
        logger.warning(
            "live snapshot load failed for a brokerage; reporting unavailable "
            "(no silent demo fallback)",
            exc_info=False,
        )
        return SnapshotResolution(
            snapshot=None,
            source_mode=SOURCE_MODE_UNAVAILABLE,
            available=False,
            brokerage_id=brokerage_id,
            detail="adapter_unavailable",
        )


@dataclass(frozen=True)
class BridgeResult:
    """A needs-attention response plus its source provenance."""

    text: str
    source_mode: str
    available: bool
    brokerage_id: Optional[str]


def build_needs_attention_bridge(
    text: str,
    brokerage_id: Optional[str] = None,
    *,
    client_factory: Optional[ClientFactory] = None,
    demo_provider: Optional[SnapshotProvider] = None,
) -> Optional[BridgeResult]:
    """PAS210 needs-attention entry point.

    Returns ``None`` for non-matching text (dispatcher falls through, exactly
    as today). Otherwise returns a :class:`BridgeResult` whose ``source_mode``
    is always one of demo / live / unavailable.

    * Flag off  → byte-identical demo output (no label), ``source_mode=demo``.
    * Flag on, no brokerage → fail-closed unavailable (no tenant inference).
    * Flag on, brokerage, live ok → labelled live output, ``source_mode=live``.
    * Flag on, brokerage, adapter fails → explicit unavailable (no demo blend).
    """
    if not match_needs_attention_intent(text):
        return None

    # Flag off / missing → preserve existing behaviour exactly.
    if not live_snapshot_enabled():
        demo_text = try_route_needs_attention(text, snapshot_provider=demo_provider)
        return BridgeResult(
            text=demo_text or "",
            source_mode=SOURCE_MODE_DEMO,
            available=True,
            brokerage_id=brokerage_id,
        )

    resolution = resolve_snapshot(
        brokerage_id,
        client_factory=client_factory,
        demo_provider=demo_provider,
    )

    if not resolution.available or resolution.snapshot is None:
        message = (
            _UNAVAILABLE_NO_TENANT
            if resolution.detail == "brokerage_id_required"
            else _UNAVAILABLE_ADAPTER
        )
        return BridgeResult(
            text=message,
            source_mode=SOURCE_MODE_UNAVAILABLE,
            available=False,
            brokerage_id=resolution.brokerage_id,
        )

    body = format_needs_attention_response(resolution.snapshot)
    header = _LIVE_HEADER.format(bid=resolution.brokerage_id)
    return BridgeResult(
        text=header + body,
        source_mode=SOURCE_MODE_LIVE,
        available=True,
        brokerage_id=resolution.brokerage_id,
    )


__all__ = (
    "LIVE_SNAPSHOT_FLAG",
    "SOURCE_MODE_DEMO",
    "SOURCE_MODE_LIVE",
    "SOURCE_MODE_UNAVAILABLE",
    "live_snapshot_enabled",
    "SnapshotResolution",
    "resolve_snapshot",
    "BridgeResult",
    "build_needs_attention_bridge",
)
