"""PAS209.7 — narrow guards for the Slack security import repair.

Scope: prove the two committed lazy-import sites in slack_command.py no longer
throw ImportError, that the expected symbols exist, and that the conservative
fail-open default behavior holds. Not a full security-suite test (PAS211).
"""
import importlib


def test_rate_limit_module_imports_and_exposes_check_rate_limit():
    mod = importlib.import_module("app.services.security.rate_limit")
    assert hasattr(mod, "check_rate_limit")
    assert callable(mod.check_rate_limit)


def test_circuit_breaker_policy_imports_and_exposes_symbol():
    mod = importlib.import_module("app.services.operator.circuit_breaker_policy")
    assert hasattr(mod, "should_block_new_outbound_for_brokerage")
    assert callable(mod.should_block_new_outbound_for_brokerage)


def test_slack_command_lazy_import_symbols_resolve():
    # Mirror the exact imports slack_command.py performs lazily.
    from app.services.security.rate_limit import check_rate_limit  # noqa: F401
    from app.services.operator.circuit_breaker_policy import (  # noqa: F401
        should_block_new_outbound_for_brokerage,
    )


def test_check_rate_limit_allows_under_limit_brokerage_scoped():
    from app.services.security.rate_limit import check_rate_limit

    verdict = check_rate_limit(
        surface="slack_command", brokerage_id="brk-test-1", actor_type="TENANT", now=1000.0
    )
    assert verdict["allowed"] is True
    assert "bucket" in verdict and verdict["surface"] == "slack_command"


def test_check_rate_limit_blocks_over_limit_in_same_window():
    from app.services.security.rate_limit import check_rate_limit, resolve_rate_limit_policy

    limit = resolve_rate_limit_policy("slack_command")["limit"]
    last = None
    # Same fixed `now` => same window => deterministic counting.
    for _ in range(limit + 5):
        last = check_rate_limit(
            surface="slack_command", brokerage_id="brk-burst", actor_type="TENANT", now=2000.0
        )
    assert last is not None and last["allowed"] is False
    assert last["count"] > limit


def test_check_rate_limit_unknown_surface_uses_fallback_and_allows_first():
    from app.services.security.rate_limit import check_rate_limit

    verdict = check_rate_limit(surface="totally_unknown_surface", now=3000.0)
    assert verdict["allowed"] is True


def test_check_rate_limit_never_stores_raw_brokerage_id_in_bucket():
    from app.services.security.rate_limit import check_rate_limit

    verdict = check_rate_limit(
        surface="slack_command", brokerage_id="secret-brk", actor_type="TENANT", now=4000.0
    )
    # bucket is a sha256 hex digest; the raw id must not appear.
    assert "secret-brk" not in verdict["bucket"]
    assert len(verdict["bucket"]) == 64


def test_should_block_defaults_false_fail_open_when_no_breaker_ledger():
    from app.services.operator.circuit_breaker_policy import (
        should_block_new_outbound_for_brokerage,
    )

    # PAS188 ledger is absent today => advisory policy fails open (no block).
    assert should_block_new_outbound_for_brokerage("brk-any") is False


def test_circuit_breaker_status_is_structural_and_pii_free():
    from app.services.operator.circuit_breaker_policy import (
        brokerage_circuit_breaker_status,
    )

    env = brokerage_circuit_breaker_status("brk-any")
    assert env["brokerage_id"] == "brk-any"
    assert env["status"] in ("UNKNOWN", "TRIPPED", "OK", "RESET", "ACTIVE")
    assert isinstance(env["warnings"], list)
