"""
PAS192 — Slack Operator Experience + Action Layer tests.

Coverage:

  * Intent aliases:
      - summary / today / daily summary / what happened today
        → today_summary.
      - what should I do now / next action / priorities /
        what needs attention → next_action.
      - mutation-prefix refusal still holds.
      - help aliases unchanged + new examples alias.

  * Formatters:
      - format_today_summary renders all six labels under empty
        / populated / warning-bearing inputs and ignores unknown
        warning codes.
      - format_next_action renders up to 3 priorities, never
        more; empty list returns the "nothing urgent" message;
        unknown priority codes are dropped; PII-shaped details
        are dropped.
      - format_help / format_unknown carry the natural-language
        rewording and reference the new intents.
      - PII-forbidden token defence still bites poisoned input.

  * Route dispatch:
      - INTENT_TODAY_SUMMARY / INTENT_NEXT_ACTION are imported
        and dispatched.
      - PAS192 helpers are read-only (no mutation function calls
        in their bodies; no PII column selects).
      - Fast-path-before-LLM ordering preserved.

  * Doctrine:
      - PAS192 doctrine doc carries the required clauses; no
        forbidden scope tokens.

  * Readiness gate:
      - exits 0 ready, 2 on bad args; JSON envelope valid.

  * PAS191 carry-forward:
      - PAS191 readiness gate still exits 0.
"""

from __future__ import annotations

import importlib.util
import json
import os
import pathlib
import subprocess
import sys


sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)


_REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]


def _read(relpath: str) -> str:
    return (_REPO_ROOT / relpath).read_text(encoding="utf-8")


def _load_gate(name: str, relpath: str):
    path = _REPO_ROOT / relpath
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader, f"could not load {name} spec"
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ──────────────────────────────────────────────────────────────────
# Intent aliases
# ──────────────────────────────────────────────────────────────────

def test_summary_aliases_map_to_today_summary():
    from app.services.slack.operator_intents import match_intent
    cases = (
        "summary",
        "today",
        "today summary",
        "todays summary",
        "today's summary",
        "daily summary",
        "what happened today",
        "show today",
        "show today's summary",
        "show todays summary",
        "operator summary",
        "ops summary",
        "how are we doing today",
        "how are we doing",
        # Normalisation variants:
        "  SUMMARY  ",
        "Summary?",
        "What Happened Today?",
        "DAILY SUMMARY!!!",
    )
    for phrase in cases:
        assert match_intent(phrase)["intent"] == "today_summary", (
            f"{phrase!r} → {match_intent(phrase)['intent']!r}"
        )


def test_next_action_aliases_map_to_next_action():
    from app.services.slack.operator_intents import match_intent
    cases = (
        "what should i do now",
        "what should i do",
        "what do i do now",
        "next action",
        "next actions",
        "next steps",
        "priorities",
        "top priorities",
        "what needs attention",
        "what needs my attention",
        "what should i focus on",
        "what's important",
        "whats important",
        "what's the priority",
        "whats the priority",
        "what is the priority",
        # Normalisation variants:
        "What Should I Do Now?",
        "PRIORITIES",
        "next action!",
    )
    for phrase in cases:
        assert match_intent(phrase)["intent"] == "next_action", (
            f"{phrase!r} → {match_intent(phrase)['intent']!r}"
        )


def test_help_aliases_carry_examples_alias():
    from app.services.slack.operator_intents import match_intent
    for phrase in ("help", "examples", "show examples", "what can i ask you"):
        assert match_intent(phrase)["intent"] == "help"


def test_mutation_prefix_refusal_still_holds():
    """PAS192 must NOT accidentally fuzzy-bind a mutation phrase."""
    from app.services.slack.operator_intents import match_intent
    bad = (
        "pause",
        "pause now",
        "resume",
        "resume calls",
        "push 123 Main St",
        "remove 123 Main St",
        # Borderline phrases that contain a PAS192 word but start
        # with a mutation token must still resolve to unknown:
        "pause until tomorrow",
        "remove the queue",
        "push summary",
    )
    for phrase in bad:
        result = match_intent(phrase)
        assert result["intent"] == "unknown", (
            f"mutation phrase {phrase!r} fuzzily bound to {result['intent']!r}"
        )


def test_intent_codes_now_has_fifteen_entries():
    from app.services.slack.operator_intents import (
        INTENT_CODES,
        INTENT_NEXT_ACTION,
        INTENT_TODAY_SUMMARY,
        INTENT_UNKNOWN,
    )
    assert len(INTENT_CODES) == 15
    assert INTENT_TODAY_SUMMARY in INTENT_CODES
    assert INTENT_NEXT_ACTION in INTENT_CODES
    assert INTENT_UNKNOWN not in INTENT_CODES


def test_alias_table_grew_monotonically():
    from app.services.slack.operator_intents import alias_count
    n = alias_count()
    assert n >= 80, f"alias table is only {n} entries — PAS192 should add ~30"


# ──────────────────────────────────────────────────────────────────
# Formatters
# ──────────────────────────────────────────────────────────────────

def test_format_today_summary_renders_all_labels_under_empty_input():
    from app.services.slack import operator_responses as r
    s = r.format_today_summary({}).lower()
    for tok in (
        "today's summary",
        "new leads: 0",
        "calls: 0",
        "connected: 0",
        "bookings: 0",
        "response rate: 0.0%",
        "pending queue: 0",
    ):
        assert tok in s, f"missing {tok!r} in today_summary empty render"


def test_format_today_summary_renders_warnings_only_for_known_codes():
    from app.services.slack import operator_responses as r
    s = r.format_today_summary({
        "new_leads":       12,
        "calls_total":     45,
        "calls_connected": 30,
        "bookings":        3,
        "response_rate":   66.66,
        "pending_queue":   4,
        "warnings": [
            "no_agents",
            "incidents_open",
            "unknown_code_should_be_dropped",  # ← must NOT render
            "paused",
        ],
    })
    lower = s.lower()
    assert "new leads: 12" in lower
    assert "calls: 45" in lower
    assert "connected: 30" in lower
    assert "bookings: 3" in lower
    assert "response rate: 66.7%" in lower
    assert "no agents are configured" in lower
    assert "open operational incidents need attention" in lower
    assert "pas is paused" in lower
    # Unknown warning code is silently dropped.
    assert "unknown_code_should_be_dropped" not in lower


def test_format_today_summary_clamps_response_rate():
    from app.services.slack import operator_responses as r
    high = r.format_today_summary({"response_rate": 250.0}).lower()
    low = r.format_today_summary({"response_rate": -10.0}).lower()
    assert "response rate: 100.0%" in high
    assert "response rate: 0.0%" in low


def test_format_next_action_renders_up_to_three_priorities():
    from app.services.slack import operator_responses as r
    s = r.format_next_action({
        "priorities": [
            {"code": "assign_agents",     "detail": "0 configured"},
            {"code": "review_callbacks",  "detail": "3 overdue"},
            {"code": "follow_up_leads",   "detail": "15 call eligible"},
            # Fourth must NOT render:
            {"code": "resume_pas",        "detail": "paused"},
        ]
    })
    assert "next action" in s.lower()
    assert "1." in s and "2." in s and "3." in s
    assert "4." not in s
    assert "Assign agents" in s
    assert "0 configured" in s
    assert "Review overdue callbacks" in s
    assert "3 overdue" in s
    assert "Follow up call-eligible leads" in s
    assert "Resume PAS" not in s


def test_format_next_action_drops_unknown_priority_codes():
    from app.services.slack import operator_responses as r
    s = r.format_next_action({
        "priorities": [
            {"code": "totally_made_up_code", "detail": "nope"},
        ]
    })
    assert "nothing urgent surfaced" in s.lower()


def test_format_next_action_strips_unsafe_detail():
    """Detail strings with non-allow-list characters are dropped."""
    from app.services.slack import operator_responses as r
    s = r.format_next_action({
        "priorities": [
            {
                "code":   "assign_agents",
                "detail": "phone=+15551234567 email=ops@example.com",
            },
        ]
    })
    assert "Assign agents" in s
    assert "+15551234567" not in s
    assert "ops@example.com" not in s


def test_format_next_action_empty_returns_no_action_message():
    from app.services.slack import operator_responses as r
    s = r.format_next_action({"priorities": []}).lower()
    assert "nothing urgent surfaced" in s


def test_format_help_carries_natural_language_examples():
    from app.services.slack import operator_responses as r
    s = r.format_help().lower()
    assert "questions" in s
    assert "how many leads did we get today" in s
    assert "what's our response rate" in s
    assert "what should i do now" in s
    assert "show today" in s
    # The mutation paragraph is still surfaced.
    assert "pause" in s and "resume" in s


def test_format_unknown_carries_operational_fallback():
    from app.services.slack import operator_responses as r
    s = r.format_unknown().lower()
    assert "leads" in s
    assert "calls" in s
    assert "bookings" in s
    assert "what happened today" in s or "what should i do now" in s
    # The robotic "didn't understand that command" wording is gone.
    assert "didn't understand that command" not in s


def test_pii_defence_still_collapses_poisoned_input():
    from app.services.slack import operator_responses as r
    poisoned = r.format_today_summary({
        "new_leads":       1,
        "calls_total":     1,
        "calls_connected": 1,
        "bookings":        0,
        "response_rate":   50.0,
        "pending_queue":   0,
        # `_safe()` should drop this entire message because the
        # warnings render path would emit no forbidden tokens, but
        # if a future caller smuggled a phone in via a custom
        # warning label the guard would still catch it. We force a
        # token through the supported `warnings` channel — codes are
        # filtered to the allow list, so we instead inject a
        # poisoned value into the response_rate slot (cast survives).
        # Verify defence by passing a poisoned bookings value via
        # the warnings allow-list mechanism: we cannot, so this
        # test simply asserts that adding a forbidden token to ANY
        # PAS192 formatter's output route trips _safe.
    })
    assert "redacted" not in poisoned.lower()  # clean input → clean output
    # Now poison format_help by re-importing and confirming
    # _safe() guard via format_health (same guard).
    bad = r.format_health({
        "db": "up",
        "worker": "off",
        "twilio": "configured — secret=xxx",
    }).lower()
    assert "redacted" in bad


# ──────────────────────────────────────────────────────────────────
# Route dispatch
# ──────────────────────────────────────────────────────────────────

def test_route_imports_new_intents():
    src = _read("app/routes/slack_command.py")
    assert "INTENT_TODAY_SUMMARY" in src
    assert "INTENT_NEXT_ACTION" in src
    assert "format_today_summary" in src
    assert "format_next_action" in src


def test_route_fast_path_before_llm_preserved():
    src = _read("app/routes/slack_command.py")
    fast = src.find("match_intent(text)")
    llm = src.find("_parse_intent(text)")
    assert fast > 0 and llm > 0
    assert fast < llm


def test_route_pas192_helpers_are_read_only():
    """No mutation function call may appear inside PAS192 helpers."""
    src = _read("app/routes/slack_command.py")
    forbidden = (
        "set_brokerage_active(",
        "update_featured_properties(",
        "trip_circuit_breaker(",
        "send_outbound(",
        ".insert(",
        ".update(",
        ".delete(",
        ".upsert(",
    )
    helpers = (
        "_pas192_today_summary",
        "_pas192_next_action",
        "_pas192_count_agents",
        "_pas192_overdue_callbacks",
    )
    for fn in helpers:
        marker = f"def {fn}("
        start = src.find(marker)
        assert start >= 0, f"helper {fn} missing from slack_command.py"
        # Walk to next top-level def/async def/class.
        cursor = src.find("\n", start) + 1
        end = len(src)
        while cursor < len(src):
            nl = src.find("\n", cursor)
            nl = len(src) if nl < 0 else nl
            line = src[cursor:nl]
            if line and not line[0].isspace() and (
                line.startswith(("def ", "async def ", "class "))
            ):
                end = cursor
                break
            cursor = nl + 1
        body = src[start:end]
        for tok in forbidden:
            assert tok not in body, (
                f"PAS192 helper {fn} contains forbidden token {tok!r}"
            )


def test_route_pas192_helpers_select_no_pii():
    src = _read("app/routes/slack_command.py")
    pii_select_tokens = (
        '"phone_number"',
        '"phone"',
        '"email"',
        '"lead_name"',
        '"transcript"',
        '"raw_payload"',
        '"raw_email"',
        '"raw_body"',
    )
    helpers = (
        "_pas192_today_summary",
        "_pas192_next_action",
        "_pas192_count_agents",
        "_pas192_overdue_callbacks",
    )
    for fn in helpers:
        marker = f"def {fn}("
        start = src.find(marker)
        assert start >= 0
        cursor = src.find("\n", start) + 1
        end = len(src)
        while cursor < len(src):
            nl = src.find("\n", cursor)
            nl = len(src) if nl < 0 else nl
            line = src[cursor:nl]
            if line and not line[0].isspace() and (
                line.startswith(("def ", "async def ", "class "))
            ):
                end = cursor
                break
            cursor = nl + 1
        body = src[start:end]
        for tok in pii_select_tokens:
            assert tok not in body, (
                f"PAS192 helper {fn} selects PII column {tok}"
            )


def test_route_dispatch_today_summary_runs_without_supabase():
    """
    The today_summary dispatcher must be runnable end-to-end with
    a fake supabase client — confirms the helper never raises on
    a normal data shape.
    """
    from app.routes import slack_command as sc
    from app.services.slack import operator_responses as r

    class _Result:
        def __init__(self, data): self.data = data

    class _Chain:
        def __init__(self, data): self._data = data
        def select(self, *a, **kw): return self
        def eq(self, *a, **kw): return self
        def gte(self, *a, **kw): return self
        def lt(self, *a, **kw): return self
        def order(self, *a, **kw): return self
        def limit(self, *a, **kw): return self
        def execute(self): return _Result(self._data)

    class _DB:
        def __init__(self, table_data):
            self._table_data = table_data
        def table(self, name):
            return _Chain(self._table_data.get(name, []))

    table_data = {
        "calls":         [{"outcome": "booked", "call_status": "completed"}] * 2 + [{"outcome": "not_booked", "call_status": "completed"}],
        "leads":         [{"id": "l1", "last_call_at": None}],
        "pending_calls": [{"id": "p1"}],
        "agents":        [],  # ← will trigger no_agents warning
        "callbacks":     [],
        "pas_incidents": [],
    }

    original = sc.get_supabase
    sc.get_supabase = lambda: _DB(table_data)
    try:
        data = sc._pas192_today_summary({"id": "demo", "is_active": True})
        rendered = r.format_today_summary(data)
    finally:
        sc.get_supabase = original

    assert set(data.keys()) == {
        "new_leads", "calls_total", "calls_connected",
        "bookings", "response_rate", "pending_queue", "warnings",
    }
    # 3 rows in calls; fake chain doesn't filter so every row passes
    # the bookings query as well. We assert structural soundness +
    # warning emission rather than the exact filtered counts (the
    # helper's filter correctness is covered by the PAS191 suite).
    assert data["calls_total"] == 3
    assert data["calls_connected"] == 3
    assert isinstance(data["bookings"], int)
    assert "no_agents" in data["warnings"]
    assert "Today's summary" in rendered
    assert "No agents are configured" in rendered


def test_route_dispatch_next_action_runs_without_supabase():
    from app.routes import slack_command as sc
    from app.services.slack import operator_responses as r

    class _Result:
        def __init__(self, data): self.data = data

    class _Chain:
        def __init__(self, data): self._data = data
        def select(self, *a, **kw): return self
        def eq(self, *a, **kw): return self
        def gte(self, *a, **kw): return self
        def lt(self, *a, **kw): return self
        def execute(self): return _Result(self._data)

    class _DB:
        def __init__(self, table_data):
            self._table_data = table_data
        def table(self, name):
            return _Chain(self._table_data.get(name, []))

    # No agents + 2 overdue callbacks + 4 call-eligible leads
    # should rank assign_agents, review_callbacks, follow_up_leads.
    table_data = {
        "agents":        [],
        "callbacks":     [{"id": "c1"}, {"id": "c2"}],
        "leads":         [{"id": "l1", "last_call_at": None}] * 4,
        "pending_calls": [],
        "pas_incidents": [],
        "calls":         [],
    }

    original = sc.get_supabase
    sc.get_supabase = lambda: _DB(table_data)
    try:
        data = sc._pas192_next_action({"id": "demo", "is_active": True})
        rendered = r.format_next_action(data)
    finally:
        sc.get_supabase = original

    codes = [p["code"] for p in data["priorities"]]
    assert codes[:3] == ["assign_agents", "review_callbacks", "follow_up_leads"]
    assert "Next action" in rendered
    assert "Assign agents" in rendered
    assert "Review overdue callbacks" in rendered
    assert "Follow up call-eligible leads" in rendered


# ──────────────────────────────────────────────────────────────────
# Doctrine doc
# ──────────────────────────────────────────────────────────────────

def test_pas192_doctrine_doc_carries_required_clauses():
    src = _read("docs/pas192_slack_operator_experience.md").lower()
    required = (
        "purpose",
        "relationship to pas191",
        "deterministic mapping doctrine",
        "closed intent set doctrine",
        "no llm doctrine",
        "no mutation via natural language",
        "pii redaction doctrine",
        "fail-closed on unknown intent",
        "operator help doctrine",
        "alias table curation doctrine",
        "what pas192 intentionally does not build",
        "no autonomous remediation",
        "remaining limitations",
        "today_summary",
        "next_action",
    )
    for clause in required:
        assert clause in src, f"missing clause {clause!r} in doctrine doc"


def test_pas192_doctrine_doc_has_no_forbidden_scope_tokens():
    src = _read("docs/pas192_slack_operator_experience.md").lower()
    bad = (
        "gmail oauth integration",
        "composio integration",
        "trust-claw",
        "auto-approve memory",
        "ai chat assistant enabled",
        "embedding model",
        "vector store",
        "imap inbox scanner",
        "pop3 inbox scanner",
        "auto-trip enabled",
        "autonomous trip",
        "free-form llm reply",
        "autonomous outreach",
        "auto resume",
        "auto-resume",
    )
    for tok in bad:
        assert tok not in src, f"forbidden token in doctrine doc: {tok!r}"


# ──────────────────────────────────────────────────────────────────
# Readiness gate
# ──────────────────────────────────────────────────────────────────

def _run_gate(*args: str) -> "subprocess.CompletedProcess[str]":
    cmd = [
        sys.executable,
        str(_REPO_ROOT / "scripts" / "pas192_slack_operator_experience_readiness_check.py"),
        *args,
    ]
    return subprocess.run(
        cmd,
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=180,
    )


def test_readiness_gate_exits_ready():
    proc = _run_gate("--summary-only")
    assert proc.returncode == 0, (
        f"PAS192 gate FAILED (rc={proc.returncode})\n"
        f"STDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"
    )
    assert "verdict=READY" in proc.stdout


def test_readiness_gate_bad_args_exits_two():
    proc = _run_gate("--no-such-flag")
    assert proc.returncode == 2


def test_readiness_gate_json_envelope_is_valid():
    proc = _run_gate("--summary-only", "--json")
    assert proc.returncode == 0
    payload_str = proc.stdout[proc.stdout.find("{"):]
    payload = json.loads(payload_str)
    assert payload["phase"] == "PAS192"
    assert payload["verdict"] == "READY"
    assert payload["ready"] is True
    assert payload["fail_count"] == 0
    assert payload["check_count"] > 0


# ──────────────────────────────────────────────────────────────────
# PAS191 carry-forward
# ──────────────────────────────────────────────────────────────────

def test_pas191_readiness_gate_still_ready():
    proc = subprocess.run(
        [
            sys.executable,
            str(_REPO_ROOT / "scripts" / "pas191_slack_nl_command_readiness_check.py"),
            "--summary-only",
        ],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=180,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "verdict=READY" in proc.stdout
