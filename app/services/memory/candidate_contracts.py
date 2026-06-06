"""PAS212 — memory candidate contracts.

Pure dataclasses, enums, and validation. No I/O, no DB, no LLM, no embeddings,
no learning loop. Defines the shape of a memory *candidate* — a proposed,
human-reviewable fact derived from committed operational data.

Doctrine (from the PAS209.5 corpus spec, minimally applied):
  * Tenant isolation is mandatory — a candidate without brokerage_id is invalid.
  * Evidence is mandatory — a candidate without evidence_refs is invalid.
  * No raw transcripts — proposed_memory is a short summary, never call text.
  * CANDIDATE by default — promotion is the operator's explicit decision.
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from typing import List, Optional, Tuple

# ── closed vocabularies ─────────────────────────────────────────────

# Candidate lifecycle status.
STATUS_CANDIDATE = "candidate"
STATUS_APPROVED = "approved"
STATUS_REJECTED = "rejected"
STATUS_ARCHIVED = "archived"
ALL_STATUSES = (STATUS_CANDIDATE, STATUS_APPROVED, STATUS_REJECTED, STATUS_ARCHIVED)

# What the candidate is about.
SUBJECT_LEAD = "lead"
SUBJECT_BROKERAGE = "brokerage"
SUBJECT_AGENT = "agent"
SUBJECT_SOURCE = "source"
ALL_SUBJECT_TYPES = (SUBJECT_LEAD, SUBJECT_BROKERAGE, SUBJECT_AGENT, SUBJECT_SOURCE)

# Conservative, closed set of candidate kinds (PAS212 examples only).
TYPE_LEAD_FACT = "lead_fact"
TYPE_CALLBACK_PREFERENCE = "callback_preference"
TYPE_REPEATED_OBJECTION = "repeated_objection_pattern"
TYPE_SOURCE_LEAD_QUALITY = "source_lead_quality_signal"
TYPE_AGENT_FOLLOWUP = "agent_followup_pattern"
ALL_CANDIDATE_TYPES = (
    TYPE_LEAD_FACT,
    TYPE_CALLBACK_PREFERENCE,
    TYPE_REPEATED_OBJECTION,
    TYPE_SOURCE_LEAD_QUALITY,
    TYPE_AGENT_FOLLOWUP,
)

DEFAULT_CREATED_BY_SYSTEM = "pas212.candidate_generation"

# Keys that would indicate a raw-transcript leak — never allowed in evidence/memory.
_FORBIDDEN_TRANSCRIPT_TOKENS = ("transcript", "turns", "raw_text", "utterance")


def _now_iso(now: Optional[str] = None) -> str:
    return now or datetime.now(timezone.utc).isoformat()


def derive_candidate_id(
    brokerage_id: str,
    subject_type: str,
    subject_id: str,
    candidate_type: str,
    evidence_refs: Tuple[str, ...],
) -> str:
    """Deterministic id: identical (tenant, subject, type, evidence) → identical
    id, so regeneration is idempotent (the store can de-dupe). Excludes any
    timestamp so generation is deterministic."""
    basis = "|".join(
        [
            brokerage_id,
            subject_type,
            subject_id,
            candidate_type,
            ",".join(sorted(evidence_refs)),
        ]
    )
    return "mc_" + hashlib.sha256(basis.encode("utf-8")).hexdigest()[:16]


@dataclass(frozen=True)
class MemoryCandidate:
    id: str
    brokerage_id: str
    subject_type: str
    subject_id: str
    candidate_type: str
    proposed_memory: str
    evidence_refs: Tuple[str, ...]
    provenance: str
    confidence: float
    status: str = STATUS_CANDIDATE
    created_at: str = ""
    created_by_system: str = DEFAULT_CREATED_BY_SYSTEM
    reviewed_by: Optional[str] = None
    reviewed_at: Optional[str] = None

    def with_review(self, *, status: str, reviewer: str, now: Optional[str] = None) -> "MemoryCandidate":
        """Return a new candidate carrying an explicit review decision."""
        return replace(
            self,
            status=status,
            reviewed_by=reviewer,
            reviewed_at=_now_iso(now),
        )


def validate_candidate(candidate: MemoryCandidate) -> List[str]:
    """Return a list of structural problems; empty list == valid."""
    problems: List[str] = []
    if not (candidate.brokerage_id or "").strip():
        problems.append("missing brokerage_id")
    if candidate.subject_type not in ALL_SUBJECT_TYPES:
        problems.append("invalid subject_type")
    if not (candidate.subject_id or "").strip():
        problems.append("missing subject_id")
    if candidate.candidate_type not in ALL_CANDIDATE_TYPES:
        problems.append("invalid candidate_type")
    if not (candidate.proposed_memory or "").strip():
        problems.append("empty proposed_memory")
    if not candidate.evidence_refs:
        problems.append("missing evidence_refs")
    if candidate.status not in ALL_STATUSES:
        problems.append("invalid status")
    if not (0.0 <= float(candidate.confidence) <= 1.0):
        problems.append("confidence out of range")
    blob = (candidate.proposed_memory + " " + " ".join(candidate.evidence_refs)).lower()
    if any(tok in blob for tok in _FORBIDDEN_TRANSCRIPT_TOKENS):
        problems.append("raw transcript leak")
    return problems


def is_valid(candidate: MemoryCandidate) -> bool:
    return not validate_candidate(candidate)


def make_candidate(
    *,
    brokerage_id: str,
    subject_type: str,
    subject_id: str,
    candidate_type: str,
    proposed_memory: str,
    evidence_refs: Tuple[str, ...],
    provenance: str,
    confidence: float,
    now: Optional[str] = None,
) -> Optional[MemoryCandidate]:
    """Build a CANDIDATE-status record. Returns None if it would be invalid
    (e.g. missing evidence) — generators never emit malformed candidates."""
    evidence = tuple(e for e in evidence_refs if e)
    cid = derive_candidate_id(brokerage_id, subject_type, subject_id, candidate_type, evidence)
    candidate = MemoryCandidate(
        id=cid,
        brokerage_id=brokerage_id,
        subject_type=subject_type,
        subject_id=subject_id,
        candidate_type=candidate_type,
        proposed_memory=proposed_memory,
        evidence_refs=evidence,
        provenance=provenance,
        confidence=round(float(confidence), 4),
        status=STATUS_CANDIDATE,
        created_at=_now_iso(now),
        created_by_system=DEFAULT_CREATED_BY_SYSTEM,
        reviewed_by=None,
        reviewed_at=None,
    )
    return candidate if is_valid(candidate) else None
