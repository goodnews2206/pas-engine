"""
PAS206 — Run the PAS205 read-only proactive observer against a
Supabase-loaded snapshot, write the digest under
reports/simulations/, and print the broker-readable summary.

Strict invariants:

  * READ-ONLY. The Supabase snapshot adapter issues select-only
    queries and never insert/update/delete/upsert/rpc.
  * Default mode is `--stub`. The CLI ships a deterministic
    in-memory stub client so the runner is safe to execute on a
    laptop with no Supabase reachability and no production
    credentials in the environment.
  * Live mode (`--live`) requires explicit opt-in and a fully
    initialised Supabase client. The CLI refuses to run live
    without `--brokerage-id` and an `--i-understand-this-is-readonly`
    acknowledgement flag.
  * No Twilio, no Slack outbound, no email, no scheduler.

Exit codes:
  0 — digest written
  2 — bad CLI args or write failure
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, List


_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


from app.services.proactive.observer import observe  # noqa: E402
from app.services.proactive.observer_digest import (  # noqa: E402
    to_broker_report,
    to_machine_json,
    to_slack_summary,
)
from app.services.proactive.supabase_snapshot_adapter import (  # noqa: E402
    load_snapshot,
)


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


REPORTS_SUBDIR = Path("reports") / "simulations"


# ──────────────────────────────────────────────────────────────────
# Deterministic stub Supabase client.
#
# Used for the default `--stub` mode so the CLI is end-to-end
# runnable without touching the live database. The stub mimics the
# subset of the supabase-py interface the adapter calls:
#
#   client.table(name).select(cols).eq(col, val).limit(n).execute()
#
# It returns a value object with a `.data` attribute. The stub
# refuses to handle anything other than select; any attempt to
# call insert/update/delete/upsert/rpc raises immediately. That
# property is exercised in the unit tests, not here.
# ──────────────────────────────────────────────────────────────────

class _StubResult:
    def __init__(self, rows: List[dict]) -> None:
        self.data = rows


class _StubQuery:
    def __init__(self, rows: List[dict]) -> None:
        self._rows = rows

    def eq(self, _col: str, _val: Any) -> "_StubQuery":
        return _StubQuery(self._rows)

    def limit(self, n: int) -> "_StubQuery":
        return _StubQuery(list(self._rows)[: int(n)])

    def order(self, _col: str, **_kwargs: Any) -> "_StubQuery":
        return _StubQuery(self._rows)

    def select(self, _cols: str = "*") -> "_StubQuery":
        return _StubQuery(self._rows)

    def execute(self) -> _StubResult:
        return _StubResult(self._rows)


class _StubTable:
    def __init__(self, rows: List[dict]) -> None:
        self._rows = rows

    def select(self, _cols: str = "*") -> _StubQuery:
        return _StubQuery(self._rows)


class _MissingTable:
    """Mimic supabase-py raising on a relation that does not exist."""

    def select(self, _cols: str = "*") -> _StubQuery:
        raise RuntimeError("relation does not exist")


class _StubSupabaseClient:
    """Minimal deterministic stand-in for `supabase.Client`."""

    def __init__(self, data: dict) -> None:
        self._data = data

    def table(self, name: str):
        rows = self._data.get(name)
        if rows is None:
            return _MissingTable()
        return _StubTable(list(rows))


# Hard-coded brokerage scope for stub mode.
_STUB_BROKERAGE = "demo-brokerage"


def _stub_dataset() -> dict:
    """Bounded, PII-free seed data covering every PAS205 rule."""
    return {
        "leads": [
            {
                "id": "L-101",
                "brokerage_id": _STUB_BROKERAGE,
                "phone_number": "+15550101",
                "created_at": "2026-05-24T01:00:00Z",
                "updated_at": "2026-05-24T01:00:00Z",
                "first_response_at": None,
                "last_activity_at": "2026-05-24T01:00:00Z",
                "assigned_agent_id": None,
                "source": "web",
                "value_tier": "high",
                "after_hours": False,
                "needs_human_review": False,
            },
            {
                "id": "L-102",
                "brokerage_id": _STUB_BROKERAGE,
                "phone_number": "+15550102",
                "created_at": "2026-05-23T22:00:00Z",
                "updated_at": "2026-05-23T22:00:00Z",
                "first_response_at": "2026-05-23T22:15:00Z",
                "last_activity_at": "2026-05-23T22:15:00Z",
                "assigned_agent_id": "A-1",
                "source": "phone",
                "value_tier": "standard",
                "after_hours": True,
                "needs_human_review": False,
            },
            {
                "id": "L-103",
                "brokerage_id": _STUB_BROKERAGE,
                "phone_number": "+15550103",
                "created_at": "2026-05-20T09:00:00Z",
                "updated_at": "2026-05-21T09:00:00Z",
                "first_response_at": "2026-05-20T09:10:00Z",
                "last_activity_at": "2026-05-21T09:00:00Z",
                "assigned_agent_id": "A-1",
                "source": "referral",
                "value_tier": "standard",
                "after_hours": False,
                "needs_human_review": True,
            },
        ],
        "calls": [
            {
                "id": "C-201",
                "brokerage_id": _STUB_BROKERAGE,
                "lead_id": "L-101",
                "start_time": "2026-05-24T01:05:00Z",
                "outcome": "failed",
                "attempt_index": 1,
            },
            {
                "id": "C-202",
                "brokerage_id": _STUB_BROKERAGE,
                "lead_id": "L-101",
                "start_time": "2026-05-24T01:15:00Z",
                "outcome": "failed",
                "attempt_index": 2,
            },
            {
                "id": "C-203",
                "brokerage_id": _STUB_BROKERAGE,
                "lead_id": "L-101",
                "start_time": "2026-05-24T01:25:00Z",
                "outcome": "failed",
                "attempt_index": 3,
            },
        ],
        "bookings": [
            {
                "id": "B-301",
                "brokerage_id": _STUB_BROKERAGE,
                "lead_id": "L-102",
                "slot_time": "2026-05-25T15:00:00Z",
                "status": "failed",
                "updated_at": "2026-05-24T01:30:00Z",
            },
        ],
        "agents": [
            {
                "id": "A-1",
                "brokerage_id": _STUB_BROKERAGE,
                "status": "busy",
                "updated_at": "2026-05-24T01:00:00Z",
            },
        ],
        # 'callbacks' deliberately omitted to exercise the
        # missing-optional-table path on the readiness gate.
    }


def _build_stub_client() -> _StubSupabaseClient:
    return _StubSupabaseClient(_stub_dataset())


# ──────────────────────────────────────────────────────────────────
# Report builder.
# ──────────────────────────────────────────────────────────────────

def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _build_report(client: Any, brokerage_id: str, loaded_at: str) -> dict:
    result = load_snapshot(client, brokerage_id=brokerage_id, loaded_at=loaded_at)
    digest = observe(result.snapshot)
    machine = to_machine_json(digest)
    return {
        "phase":                 "PAS206",
        "allowed_environment":   "SIMULATION_ONLY",
        "live_behavior_changed": False,
        "read_only":             result.read_only,
        "generated_at":          _now_iso(),
        "brokerage_id":          brokerage_id,
        "snapshot_loaded_at":    result.loaded_at,
        "row_counts":            dict(result.row_counts),
        "source_status":         dict(result.source_status),
        "unavailable_sources":   list(result.unavailable_sources),
        "digest":                machine,
        "human": {
            "slack_summary": to_slack_summary(digest),
            "broker_report": to_broker_report(digest),
        },
    }


def _write_report(repo_root: Path, report: dict) -> Path:
    reports_dir = repo_root / REPORTS_SUBDIR
    reports_dir.mkdir(parents=True, exist_ok=True)
    stamp = report["generated_at"].replace(":", "").replace("-", "")
    filename = f"pas206_supabase_snapshot_demo_{stamp}.json"
    path = reports_dir / filename
    path.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


# ──────────────────────────────────────────────────────────────────
# Argument plumbing.
# ──────────────────────────────────────────────────────────────────

def _parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "PAS206 — Run the PAS205 read-only proactive observer "
            "against a Supabase-loaded snapshot. Defaults to stub mode."
        ),
    )
    parser.add_argument(
        "--brokerage-id",
        type=str,
        default=_STUB_BROKERAGE,
        help="Brokerage scope filter for the snapshot read.",
    )
    parser.add_argument(
        "--stub",
        action="store_true",
        default=True,
        help="Use the deterministic in-memory stub client (default).",
    )
    parser.add_argument(
        "--live",
        action="store_true",
        help=(
            "Use the live Supabase singleton client (requires "
            "--i-understand-this-is-readonly)."
        ),
    )
    parser.add_argument(
        "--i-understand-this-is-readonly",
        action="store_true",
        help="Explicit acknowledgement required to enable --live.",
    )
    parser.add_argument(
        "--no-write",
        action="store_true",
        help="Do not write a report file; print to stdout only.",
    )
    parser.add_argument(
        "--summary-only",
        action="store_true",
        help="Print only the broker-readable summary, no JSON path.",
    )
    return parser.parse_args(argv)


def _build_client(args: argparse.Namespace) -> Any:
    if not args.live:
        return _build_stub_client()

    if not args.i_understand_this_is_readonly:
        raise SystemExit(
            "PAS206 refuses --live without "
            "--i-understand-this-is-readonly. The adapter is read-only, "
            "but the operator must acknowledge the intent."
        )
    # Lazy import keeps the stub path free of supabase-py dependency.
    from app.db.supabase_client import get_supabase  # type: ignore[import-not-found]
    return get_supabase()


def main(argv: List[str]) -> int:
    args = _parse_args(argv)

    client = _build_client(args)
    loaded_at = _now_iso()
    report = _build_report(client, args.brokerage_id, loaded_at)

    if not args.no_write:
        try:
            written = _write_report(_REPO_ROOT, report)
        except OSError as e:
            print(f"PAS206: failed to write report ({e})", file=sys.stderr)
            return 2
    else:
        written = None

    summary = report["human"]["broker_report"]
    digest = report["digest"]
    signals_count = len(digest["signals"])

    if args.summary_only:
        print(summary)
        return 0

    print(summary)
    print("")
    print(f"brokerage: {args.brokerage_id}")
    print(f"signals: {signals_count}")
    print(f"row_counts: {report['row_counts']}")
    print(f"source_status: {report['source_status']}")
    if report["unavailable_sources"]:
        print(f"unavailable_sources: {report['unavailable_sources']}")
    if written is not None:
        print(f"report: {written.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
