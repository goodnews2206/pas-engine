"""PAS212C — approved memory retrieval (read-only context).

Reads ONLY approved memory candidates and renders them as read-only context
blocks. This is not injection: nothing here writes to the engine, alters a
prompt, or changes call behaviour. Governed injection into live calls is a
later, explicitly-gated step (PAS212D).

Hard contract:
  * **Approved only.** Retrieval always filters to ``status == approved``;
    candidate / rejected / archived records are never returned as trusted
    context, regardless of caller input.
  * **Tenant-scoped.** Every read goes through the store keyed by
    ``brokerage_id``; another tenant's memory is never reachable.
  * **No behaviour change.** The formatter emits neutral, read-only context
    blocks — it never adds directive/instruction language and marks every block
    ``read_only``.
  * **No transcript leakage.** Only the already-transcript-free candidate fields
    are surfaced (summary, evidence refs, provenance, confidence).
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from app.services.memory.candidate_contracts import STATUS_APPROVED, MemoryCandidate
from app.services.memory.candidate_store import MemoryCandidateStore, default_store

# Marker labelling these blocks as the source/kind of context.
CONTEXT_SOURCE = "approved_memory"


def retrieve_approved(
    brokerage_id: str,
    *,
    store: Optional[MemoryCandidateStore] = None,
    subject_type: Optional[str] = None,
    subject_id: Optional[str] = None,
    candidate_type: Optional[str] = None,
) -> List[MemoryCandidate]:
    """Return approved memories for a brokerage, optionally filtered. Returns an
    empty list if none. Never returns unapproved records."""
    if not (brokerage_id or "").strip():
        return []
    st = store or default_store()
    # Hard-coded APPROVED — the caller cannot widen this.
    rows = st.list_candidates(brokerage_id, status=STATUS_APPROVED)
    if subject_type is not None:
        rows = [m for m in rows if m.subject_type == subject_type]
    if subject_id is not None:
        rows = [m for m in rows if m.subject_id == subject_id]
    if candidate_type is not None:
        rows = [m for m in rows if m.candidate_type == candidate_type]
    # Defensive: never surface anything not actually approved.
    return [m for m in rows if m.status == STATUS_APPROVED]


def format_approved_context(memories: List[MemoryCandidate]) -> List[Dict[str, Any]]:
    """Turn approved memories into neutral, read-only context blocks.

    Each block carries the approved memory as *context*, with evidence,
    provenance, and confidence. It adds NO directive/instruction language and is
    flagged ``read_only`` so downstream consumers treat it as observation, not
    behaviour."""
    blocks: List[Dict[str, Any]] = []
    for m in memories:
        if m.status != STATUS_APPROVED:  # belt-and-suspenders
            continue
        blocks.append(
            {
                "source": CONTEXT_SOURCE,
                "read_only": True,
                "subject_type": m.subject_type,
                "subject_id": m.subject_id,
                "candidate_type": m.candidate_type,
                "approved_memory": m.proposed_memory,
                "evidence_refs": list(m.evidence_refs),
                "provenance": m.provenance,
                "confidence": m.confidence,
            }
        )
    return blocks


__all__ = ("CONTEXT_SOURCE", "retrieve_approved", "format_approved_context")
