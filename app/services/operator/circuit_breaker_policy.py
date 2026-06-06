"""PAS189 (PAS209.7 minimal runtime repair) — circuit-breaker policy.

Minimal import-repair reconstruction scoped to what the committed runtime
imports today: ``should_block_new_outbound_for_brokerage`` (used by
app/routes/slack_command.py).

This is a thin, **read-only, advisory** policy layer over PAS188's
``circuit_breaker`` ledger. PAS188 is a deferred rebuild (it is NOT present
today), so there is no breaker state to read — and the original doctrine's
fail-open default applies cleanly: with no TRIPPED state, nothing is blocked.

Doctrine preserved from the original spec:

* **Advisory only.** Never trips, resets, or mutates any breaker state.
* **No auto-trip / no auto-reset / no autonomous remediation.**
* **Fail-open.** Any failure (missing ledger, malformed row, exception)
  yields ``should_block=False`` — the doctrine prefers leads through.
* **No PII.** Envelopes carry only ``brokerage_id``, ``status``, and
  structural ``warnings``.
* **NEVER raises.**
"""
from __future__ import annotations

import logging
from typing import Any, Dict, Optional

logger = logging.getLogger("pas.operator.circuit_breaker_policy")

_TRIPPED = "TRIPPED"
_FAIL_OPEN_WARNING = "policy_check_failed_fail_open"


def _read_current_state(brokerage_id: str) -> Optional[Dict[str, Any]]:
    """Advisory read-through over PAS188 ``circuit_breaker`` if it exists.

    PAS188 is a deferred rebuild; when its module is absent (today) this
    returns ``None`` and callers fail open. Imported lazily so this module
    stays import-safe regardless of PAS188's presence.
    """
    try:
        from app.services.operator.circuit_breaker import current_breaker_state  # type: ignore
    except Exception:
        return None
    try:
        state = current_breaker_state(brokerage_id)
        return state if isinstance(state, dict) else None
    except Exception:
        return None


def brokerage_circuit_breaker_status(brokerage_id: str) -> Dict[str, Any]:
    """Closed-projection breaker status envelope. Fail-open on any failure."""
    try:
        state = _read_current_state(brokerage_id)
        if state is None:
            return {
                "brokerage_id": brokerage_id,
                "status": "UNKNOWN",
                "warnings": [_FAIL_OPEN_WARNING],
                "warning_count": 1,
            }
        status = str(state.get("status") or "UNKNOWN").upper()
        return {
            "brokerage_id": brokerage_id,
            "status": status,
            "reason_code": state.get("reason_code"),
            "warnings": [],
            "warning_count": 0,
        }
    except Exception:  # pragma: no cover - defensive fail-open
        return {
            "brokerage_id": brokerage_id,
            "status": "UNKNOWN",
            "warnings": [_FAIL_OPEN_WARNING],
            "warning_count": 1,
        }


def should_block_new_outbound_for_brokerage(brokerage_id: str) -> bool:
    """``True`` only when the most-recent breaker row is TRIPPED.

    Fail-open: any policy failure (including the absence of the PAS188
    ledger) returns ``False`` so new outbound is not blocked.
    """
    try:
        return brokerage_circuit_breaker_status(brokerage_id).get("status") == _TRIPPED
    except Exception:  # pragma: no cover - defensive fail-open
        return False


def circuit_breaker_public_warning(brokerage_id: str) -> str:
    """Short structural warning string for operator UI; "" when not tripped."""
    try:
        if should_block_new_outbound_for_brokerage(brokerage_id):
            return "brokerage_circuit_breaker_tripped"
        return ""
    except Exception:  # pragma: no cover - defensive fail-open
        return ""
