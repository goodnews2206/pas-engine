"""PAS212 — in-memory, tenant-scoped memory candidate store.

The minimal storage + review boundary for the candidate pipeline. PAS212 ships
**no database table** (the corpus `pas_memory_records` migration is absent and a
migration is not justified yet) — this is a process-local, file-free abstraction
with the full approval semantics. Durable persistence is PAS212B.

Hard contract:
  * **No automatic approval.** Candidates are stored as CANDIDATE only; approval
    requires an explicit reviewer call.
  * **No live behaviour change.** This module imports nothing from the engine,
    brokerage config, or any outbound surface. Approving a candidate records a
    decision; it does NOT alter prompts, flags, or call behaviour. Wiring
    approved memory into the runtime is explicitly out of PAS212 scope.
  * **Tenant isolation.** Every read/transition is scoped by brokerage_id; a
    candidate stored under one brokerage is unreachable via another.
  * **Rejected candidates remain auditable.** Reject/archive keep the record.
  * Never raises into the caller for normal control flow; returns structured
    results.
"""
from __future__ import annotations

import threading
from typing import Dict, List, Optional, Tuple

from app.services.memory.candidate_contracts import (
    STATUS_APPROVED,
    STATUS_ARCHIVED,
    STATUS_CANDIDATE,
    STATUS_REJECTED,
    MemoryCandidate,
    is_valid,
)


class MemoryCandidateStore:
    """Process-local store. Keyed by (brokerage_id, candidate_id)."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._by_tenant: Dict[str, Dict[str, MemoryCandidate]] = {}

    # ── writes ──────────────────────────────────────────────────────

    def add_candidates(
        self, brokerage_id: str, candidates: List[MemoryCandidate]
    ) -> List[MemoryCandidate]:
        """Store valid CANDIDATE records under their tenant. Idempotent by id;
        an existing candidate is NOT overwritten (so a prior review survives a
        regeneration). Cross-tenant candidates are skipped."""
        if not (brokerage_id or "").strip():
            return []
        stored: List[MemoryCandidate] = []
        with self._lock:
            bucket = self._by_tenant.setdefault(brokerage_id, {})
            for c in candidates:
                if c.brokerage_id != brokerage_id:  # tenant pin guard
                    continue
                if not is_valid(c):
                    continue
                if c.id in bucket:
                    stored.append(bucket[c.id])
                    continue
                bucket[c.id] = c
                stored.append(c)
        return stored

    # ── reads (tenant-scoped) ───────────────────────────────────────

    def get_candidate(self, brokerage_id: str, candidate_id: str) -> Optional[MemoryCandidate]:
        with self._lock:
            return self._by_tenant.get(brokerage_id, {}).get(candidate_id)

    def list_candidates(
        self, brokerage_id: str, status: Optional[str] = None
    ) -> List[MemoryCandidate]:
        with self._lock:
            rows = list(self._by_tenant.get(brokerage_id, {}).values())
        if status is not None:
            rows = [c for c in rows if c.status == status]
        return sorted(rows, key=lambda c: c.id)

    # ── explicit review transitions ─────────────────────────────────

    def _transition(
        self,
        brokerage_id: str,
        candidate_id: str,
        *,
        to_status: str,
        reviewer: str,
        from_statuses: Tuple[str, ...],
        now: Optional[str] = None,
    ) -> dict:
        if not (reviewer or "").strip():
            return {"status": "failed", "error": "reviewer is required"}
        with self._lock:
            bucket = self._by_tenant.get(brokerage_id, {})
            current = bucket.get(candidate_id)  # tenant-scoped lookup only
            if current is None:
                return {"status": "failed", "error": "candidate not found for tenant"}
            if current.status not in from_statuses:
                return {
                    "status": "failed",
                    "error": f"invalid transition from {current.status} to {to_status}",
                }
            updated = current.with_review(status=to_status, reviewer=reviewer, now=now)
            bucket[candidate_id] = updated
        return {"status": "ok", "candidate": updated}

    def approve(self, brokerage_id: str, candidate_id: str, reviewer: str, now: Optional[str] = None) -> dict:
        """Explicit approval. Only a CANDIDATE may be approved. Records who/when.
        Does NOT change any live behaviour."""
        return self._transition(
            brokerage_id, candidate_id,
            to_status=STATUS_APPROVED, reviewer=reviewer,
            from_statuses=(STATUS_CANDIDATE,), now=now,
        )

    def reject(self, brokerage_id: str, candidate_id: str, reviewer: str, now: Optional[str] = None) -> dict:
        """Explicit rejection. A rejected candidate stays stored (auditable) and
        can never be approved afterwards."""
        return self._transition(
            brokerage_id, candidate_id,
            to_status=STATUS_REJECTED, reviewer=reviewer,
            from_statuses=(STATUS_CANDIDATE,), now=now,
        )

    def archive(self, brokerage_id: str, candidate_id: str, reviewer: str, now: Optional[str] = None) -> dict:
        return self._transition(
            brokerage_id, candidate_id,
            to_status=STATUS_ARCHIVED, reviewer=reviewer,
            from_statuses=(STATUS_CANDIDATE, STATUS_APPROVED, STATUS_REJECTED), now=now,
        )


# A module-level default store for convenience (process-local).
_default_store = MemoryCandidateStore()


def default_store() -> MemoryCandidateStore:
    return _default_store


__all__ = ("MemoryCandidateStore", "default_store")
