"""
PAS204-C — Demo / rehearsal data detector.

Deterministic, read-only detector that decides whether the data
about to be rendered into `/pas stats` (and any other seeded
metric response) is real production data or seeded/demo data.

The detector is bounded by closed signal vocabulary. It NEVER
labels real production data as demo without evidence; conversely,
it never silently passes seeded data off as real.

Verdicts (closed vocab):

  * "demo_detected"     — at least one demo signal fires.
  * "no_demo_signal"    — inputs were inspected and carry no
                          demo marker.
  * "unknown"           — caller couldn't supply enough inputs
                          to decide (e.g., DB query failed, no
                          brokerage record). Renderer should
                          fall back to a conservative note
                          rather than silently asserting either
                          shape.

Closed signal vocabulary (all hand-curated, no fuzzy expansion):

  * brokerage_marked_demo
  * brokerage_environment_label
  * row_source_simulated
  * row_call_type_simulated
  * row_metadata_seed_batch
  * row_phone_seed_convention

Inputs are intentionally OPTIONAL — callers pass whatever they
have. With no inputs the verdict is "unknown".
"""

from __future__ import annotations

from typing import Dict, List, Optional, Sequence, Tuple


# ──────────────────────────────────────────────────────────────────
# Closed vocabularies
# ──────────────────────────────────────────────────────────────────

VERDICT_DEMO_DETECTED:  str = "demo_detected"
VERDICT_NO_DEMO_SIGNAL: str = "no_demo_signal"
VERDICT_UNKNOWN:        str = "unknown"

VERDICT_VALUES: Tuple[str, ...] = (
    VERDICT_DEMO_DETECTED,
    VERDICT_NO_DEMO_SIGNAL,
    VERDICT_UNKNOWN,
)


SIGNAL_BROKERAGE_MARKED_DEMO:        str = "brokerage_marked_demo"
SIGNAL_BROKERAGE_ENVIRONMENT_LABEL:  str = "brokerage_environment_label"
SIGNAL_ROW_SOURCE_SIMULATED:         str = "row_source_simulated"
SIGNAL_ROW_CALL_TYPE_SIMULATED:      str = "row_call_type_simulated"
SIGNAL_ROW_METADATA_SEED_BATCH:      str = "row_metadata_seed_batch"
SIGNAL_ROW_PHONE_SEED_CONVENTION:    str = "row_phone_seed_convention"

SIGNALS: Tuple[str, ...] = (
    SIGNAL_BROKERAGE_MARKED_DEMO,
    SIGNAL_BROKERAGE_ENVIRONMENT_LABEL,
    SIGNAL_ROW_SOURCE_SIMULATED,
    SIGNAL_ROW_CALL_TYPE_SIMULATED,
    SIGNAL_ROW_METADATA_SEED_BATCH,
    SIGNAL_ROW_PHONE_SEED_CONVENTION,
)


# Phone-number seed convention used widely for fake numbers.
# Only mark as a demo signal when this prefix is in use AS A
# SEED CONVENTION (caller responsibility — we just detect the
# prefix shape).
_PHONE_SEED_PREFIX: str = "+1555555"


# Closed list of brokerage-record fields/values that mean
# "this brokerage is a demo environment".
_BROKERAGE_DEMO_FLAGS: Tuple[str, ...] = (
    "is_demo",
    "demo_environment",
    "is_seeded",
    "seeded",
)
_BROKERAGE_DEMO_ENV_VALUES: Tuple[str, ...] = (
    "demo",
    "rehearsal",
    "sandbox",
    "seeded",
    "simulation",
)


_ROW_SIMULATED_SOURCE_VALUES: Tuple[str, ...] = (
    "simulated",
    "simulation",
    "demo",
    "seed",
    "seeded",
    "rehearsal",
)


# ──────────────────────────────────────────────────────────────────
# Detector
# ──────────────────────────────────────────────────────────────────

def _check_brokerage(brokerage: Dict) -> List[str]:
    signals: List[str] = []
    if not isinstance(brokerage, dict):
        return signals
    for flag in _BROKERAGE_DEMO_FLAGS:
        if bool(brokerage.get(flag)):
            signals.append(SIGNAL_BROKERAGE_MARKED_DEMO)
            break
    env = brokerage.get("environment")
    if isinstance(env, str) and env.strip().lower() in _BROKERAGE_DEMO_ENV_VALUES:
        signals.append(SIGNAL_BROKERAGE_ENVIRONMENT_LABEL)
    return signals


def _check_rows(rows: Sequence[Dict]) -> List[str]:
    signals: List[str] = []
    has_simulated_source = False
    has_simulated_call_type = False
    has_seed_batch = False
    has_phone_seed = False
    for r in rows:
        if not isinstance(r, dict):
            continue
        if not has_simulated_source:
            src = r.get("source")
            if isinstance(src, str) and src.strip().lower() in _ROW_SIMULATED_SOURCE_VALUES:
                has_simulated_source = True
        if not has_simulated_call_type:
            ct = r.get("call_type")
            if isinstance(ct, str) and ct.strip().lower() in _ROW_SIMULATED_SOURCE_VALUES:
                has_simulated_call_type = True
        if not has_seed_batch:
            meta = r.get("metadata")
            if isinstance(meta, dict) and (
                meta.get("seed_batch") or meta.get("demo_seed")
                or meta.get("seeded")
            ):
                has_seed_batch = True
        if not has_phone_seed:
            phone = r.get("phone_number") or r.get("phone") or ""
            if isinstance(phone, str) and phone.replace(" ", "").replace("-", "").startswith(_PHONE_SEED_PREFIX):
                has_phone_seed = True
        # Early termination — every signal we care about has fired.
        if has_simulated_source and has_simulated_call_type and has_seed_batch and has_phone_seed:
            break
    if has_simulated_source:
        signals.append(SIGNAL_ROW_SOURCE_SIMULATED)
    if has_simulated_call_type:
        signals.append(SIGNAL_ROW_CALL_TYPE_SIMULATED)
    if has_seed_batch:
        signals.append(SIGNAL_ROW_METADATA_SEED_BATCH)
    if has_phone_seed:
        signals.append(SIGNAL_ROW_PHONE_SEED_CONVENTION)
    return signals


def detect_demo_signals(
    brokerage: Optional[Dict] = None,
    rows: Optional[Sequence[Dict]] = None,
) -> Dict[str, object]:
    """
    Inspect optional brokerage record and/or row sample and
    return a closed verdict envelope:

        {
            "verdict": "demo_detected" | "no_demo_signal" | "unknown",
            "signals": tuple of fired SIGNALS,
        }

    Rules:
      * Any positive signal -> demo_detected.
      * Both inputs supplied AND zero signals -> no_demo_signal.
      * No inputs supplied at all -> unknown.
      * brokerage supplied alone with no demo flag -> no_demo_signal
        (we trust the brokerage record).
      * rows supplied alone (no brokerage) and no row-level signals
        -> no_demo_signal (we trust the sample).
    """
    fired: List[str] = []
    inspected_anything = False
    if brokerage is not None:
        inspected_anything = True
        fired.extend(_check_brokerage(brokerage))
    if rows is not None:
        inspected_anything = True
        fired.extend(_check_rows(rows))

    fired_unique = []
    seen = set()
    for s in fired:
        if s not in seen:
            seen.add(s)
            fired_unique.append(s)

    if fired_unique:
        verdict = VERDICT_DEMO_DETECTED
    elif inspected_anything:
        verdict = VERDICT_NO_DEMO_SIGNAL
    else:
        verdict = VERDICT_UNKNOWN
    return {"verdict": verdict, "signals": tuple(fired_unique)}


def signal_count() -> int:
    """Number of closed signal codes registered."""
    return len(SIGNALS)


def list_verdicts() -> Tuple[str, ...]:
    return VERDICT_VALUES


def list_signals() -> Tuple[str, ...]:
    return SIGNALS
