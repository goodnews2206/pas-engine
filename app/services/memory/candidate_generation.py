"""PAS212 — deterministic memory candidate generation.

Pure functions that turn already-committed operational data (lead rows, event
rows) into CANDIDATE-status :class:`MemoryCandidate` records. No I/O, no LLM, no
embeddings, no DB reads — callers pass the data in. Generation is:

  * **Deterministic.** Same inputs (+ same ``now``) → identical candidates,
    including identical ids (the id is derived from stable fields only).
  * **Conservative.** Thresholds are intentionally high; weak signals produce
    nothing. Missing evidence never produces a candidate.
  * **Tenant-pinned from the argument only.** ``brokerage_id`` is taken from the
    explicit argument; any ``brokerage_id`` on an input row is ignored.
  * **Transcript-free.** Only summaries / counts / categories are emitted.
"""
from __future__ import annotations

from typing import Any, Dict, List, Mapping, Optional, Sequence

from app.services.memory.candidate_contracts import (
    SUBJECT_AGENT,
    SUBJECT_LEAD,
    SUBJECT_SOURCE,
    TYPE_AGENT_FOLLOWUP,
    TYPE_CALLBACK_PREFERENCE,
    TYPE_LEAD_FACT,
    TYPE_REPEATED_OBJECTION,
    TYPE_SOURCE_LEAD_QUALITY,
    MemoryCandidate,
    make_candidate,
)
from app.services.security.prompt_safety import sanitize_for_memory_candidate

# Conservative thresholds.
_MIN_OBJECTIONS_FOR_PATTERN = 2
_MIN_LEADS_FOR_SOURCE_SIGNAL = 3
_MIN_LEADS_FOR_AGENT_PATTERN = 3


def _row_id(row: Mapping[str, Any], *keys: str) -> Optional[str]:
    for k in keys:
        v = row.get(k)
        if v not in (None, ""):
            return str(v)
    return None


def _booked(lead: Mapping[str, Any]) -> bool:
    if lead.get("last_booked_at"):
        return True
    return str(lead.get("outcome") or "").lower() == "booked"


# ── individual generators ───────────────────────────────────────────

def generate_lead_fact_candidates(
    brokerage_id: str, leads: Sequence[Mapping[str, Any]], now: Optional[str] = None
) -> List[MemoryCandidate]:
    out: List[MemoryCandidate] = []
    for lead in leads:
        lead_id = _row_id(lead, "id", "lead_id")
        if not lead_id:  # no id → no evidence → no candidate
            continue
        # PAS211H: lead-controlled fields are sanitized before they can become
        # proposed memory (instruction phrases redacted, length-capped). Benign
        # qualification values pass through unchanged.
        facts = []
        if lead.get("intent"):
            facts.append(f"intent={sanitize_for_memory_candidate(lead['intent'])}")
        if lead.get("budget"):
            facts.append(f"budget={sanitize_for_memory_candidate(lead['budget'])}")
        if lead.get("timeline"):
            facts.append(f"timeline={sanitize_for_memory_candidate(lead['timeline'])}")
        if not facts:
            continue
        proposed = "Lead qualification facts: " + "; ".join(facts) + "."
        out.append(
            make_candidate(
                brokerage_id=brokerage_id,
                subject_type=SUBJECT_LEAD,
                subject_id=lead_id,
                candidate_type=TYPE_LEAD_FACT,
                proposed_memory=proposed,
                evidence_refs=(f"lead:{lead_id}",),
                provenance="derived from committed lead row (intent/budget/timeline)",
                confidence=min(0.5 + 0.15 * len(facts), 0.95),
                now=now,
            )
        )
    return [c for c in out if c is not None]


def generate_callback_preference_candidates(
    brokerage_id: str, events: Sequence[Mapping[str, Any]], now: Optional[str] = None
) -> List[MemoryCandidate]:
    by_lead: Dict[str, List[str]] = {}
    for ev in events:
        etype = str(ev.get("event_type") or "").lower()
        if "callback" not in etype:
            continue
        lead_id = _row_id(ev, "lead_id")
        ev_id = _row_id(ev, "id", "event_id")
        if not lead_id or not ev_id:
            continue
        by_lead.setdefault(lead_id, []).append(f"event:{ev_id}")
    out: List[MemoryCandidate] = []
    for lead_id, refs in by_lead.items():
        out.append(
            make_candidate(
                brokerage_id=brokerage_id,
                subject_type=SUBJECT_LEAD,
                subject_id=lead_id,
                candidate_type=TYPE_CALLBACK_PREFERENCE,
                proposed_memory="Lead has requested a scheduled callback rather than booking on the call.",
                evidence_refs=tuple(sorted(refs)),
                provenance="derived from committed callback events",
                confidence=0.7,
                now=now,
            )
        )
    return [c for c in out if c is not None]


def generate_repeated_objection_candidates(
    brokerage_id: str, events: Sequence[Mapping[str, Any]], now: Optional[str] = None
) -> List[MemoryCandidate]:
    by_lead: Dict[str, List[str]] = {}
    for ev in events:
        etype = str(ev.get("event_type") or "").lower()
        if "objection" not in etype:
            continue
        lead_id = _row_id(ev, "lead_id")
        ev_id = _row_id(ev, "id", "event_id")
        if not lead_id or not ev_id:
            continue
        by_lead.setdefault(lead_id, []).append(f"event:{ev_id}")
    out: List[MemoryCandidate] = []
    for lead_id, refs in by_lead.items():
        if len(refs) < _MIN_OBJECTIONS_FOR_PATTERN:
            continue
        out.append(
            make_candidate(
                brokerage_id=brokerage_id,
                subject_type=SUBJECT_LEAD,
                subject_id=lead_id,
                candidate_type=TYPE_REPEATED_OBJECTION,
                proposed_memory=f"Lead has raised objections repeatedly ({len(refs)} times); approach with extra reassurance.",
                evidence_refs=tuple(sorted(refs)),
                provenance="derived from repeated committed objection events",
                confidence=min(0.5 + 0.1 * len(refs), 0.9),
                now=now,
            )
        )
    return [c for c in out if c is not None]


def generate_source_quality_candidates(
    brokerage_id: str, leads: Sequence[Mapping[str, Any]], now: Optional[str] = None
) -> List[MemoryCandidate]:
    by_source: Dict[str, List[Mapping[str, Any]]] = {}
    for lead in leads:
        source = lead.get("source")
        lead_id = _row_id(lead, "id", "lead_id")
        if not source or not lead_id:
            continue
        by_source.setdefault(str(source), []).append(lead)
    out: List[MemoryCandidate] = []
    for source, rows in by_source.items():
        if len(rows) < _MIN_LEADS_FOR_SOURCE_SIGNAL:
            continue
        booked = sum(1 for r in rows if _booked(r))
        rate = booked / len(rows)
        if 0.0 < rate < 1.0 and not (rate >= 0.5 or rate == 0.0):
            continue  # only emit for clearly strong / clearly weak sources
        quality = "high-converting" if rate >= 0.5 else "low-converting"
        refs = tuple(sorted(f"lead:{_row_id(r, 'id', 'lead_id')}" for r in rows))
        out.append(
            make_candidate(
                brokerage_id=brokerage_id,
                subject_type=SUBJECT_SOURCE,
                subject_id=str(source),
                candidate_type=TYPE_SOURCE_LEAD_QUALITY,
                proposed_memory=f"Source '{source}' appears {quality} ({booked}/{len(rows)} booked).",
                evidence_refs=refs,
                provenance="aggregated over committed lead rows by source",
                confidence=0.6,
                now=now,
            )
        )
    return [c for c in out if c is not None]


def generate_agent_followup_candidates(
    brokerage_id: str, leads: Sequence[Mapping[str, Any]], now: Optional[str] = None
) -> List[MemoryCandidate]:
    by_agent: Dict[str, List[Mapping[str, Any]]] = {}
    for lead in leads:
        agent_id = _row_id(lead, "assigned_agent_id", "agent_id")
        lead_id = _row_id(lead, "id", "lead_id")
        if not agent_id or not lead_id:
            continue
        by_agent.setdefault(agent_id, []).append(lead)
    out: List[MemoryCandidate] = []
    for agent_id, rows in by_agent.items():
        if len(rows) < _MIN_LEADS_FOR_AGENT_PATTERN:
            continue
        booked = sum(1 for r in rows if _booked(r))
        if booked < _MIN_LEADS_FOR_AGENT_PATTERN:  # only a strong, positive pattern
            continue
        refs = tuple(sorted(f"lead:{_row_id(r, 'id', 'lead_id')}" for r in rows))
        out.append(
            make_candidate(
                brokerage_id=brokerage_id,
                subject_type=SUBJECT_AGENT,
                subject_id=agent_id,
                candidate_type=TYPE_AGENT_FOLLOWUP,
                proposed_memory=f"Agent {agent_id} consistently converts assigned leads ({booked}/{len(rows)} booked).",
                evidence_refs=refs,
                provenance="aggregated over committed lead rows by assigned agent",
                confidence=0.6,
                now=now,
            )
        )
    return [c for c in out if c is not None]


# ── orchestrator ────────────────────────────────────────────────────

def generate_candidates(
    brokerage_id: str,
    *,
    leads: Sequence[Mapping[str, Any]] = (),
    events: Sequence[Mapping[str, Any]] = (),
    now: Optional[str] = None,
) -> List[MemoryCandidate]:
    """Run every generator and return a de-duplicated, deterministically-ordered
    list of CANDIDATE records. ``brokerage_id`` is the only tenant source."""
    if not (brokerage_id or "").strip():
        return []
    candidates: List[MemoryCandidate] = []
    candidates += generate_lead_fact_candidates(brokerage_id, leads, now)
    candidates += generate_callback_preference_candidates(brokerage_id, events, now)
    candidates += generate_repeated_objection_candidates(brokerage_id, events, now)
    candidates += generate_source_quality_candidates(brokerage_id, leads, now)
    candidates += generate_agent_followup_candidates(brokerage_id, leads, now)

    # de-dupe by id (idempotent regeneration), stable order by id
    seen: Dict[str, MemoryCandidate] = {}
    for c in candidates:
        seen.setdefault(c.id, c)
    return [seen[k] for k in sorted(seen)]
