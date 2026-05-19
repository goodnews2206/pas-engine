"""
PAS191 — Bounded Slack natural-language operator commands tests.

Coverage:

  * Mapper:
      - 12 canonical phrases map to the right intent code.
      - aliases for the same intent all map identically.
      - normalisation strips whitespace, case, trailing
        punctuation.
      - empty / whitespace input → unknown.
      - phrases starting with pause/resume/push/remove →
        always unknown, regardless of trailing text.
      - unknown phrases return unknown + empty matched_alias.
      - alias table is non-trivially sized (>=  50).
      - INTENT_CODES has exactly 12 entries.

  * Formatter:
      - format_help / format_unknown / format_paused_status
        return strings.
      - Each format_* helper handles missing / zero values.
      - PII forbidden-token defence: a poisoned input
        collapses to the generic redacted line.
      - format_error never echoes the underlying message.

  * Route wire-through:
      - PAS191 fast-path appears in slack_command.py BEFORE
        the LLM intent parser.
      - operator_intents and operator_responses are imported.

  * Doctrine:
      - operator_intents.py has no LLM / regex / threading
        / subprocess imports.
      - operator_responses.py has no network imports.
      - operator_intents.py has no eval/exec.
      - Doctrine doc carries required clauses; no forbidden
        scope tokens.

  * Event contract:
      - slack.intent.matched / slack.intent.unknown literals
        present.

  * Readiness gate:
      - exits 0 ready, 2 bad args; JSON mode emits a valid
        envelope.

  * PAS186 + PAS187 + PAS188 + PAS189 + PAS190 carry-forward
    READY (the prior gates still pass).
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


def _load_pas191_gate():
    return _load_gate(
        "pas191_gate",
        "scripts/pas191_slack_nl_command_readiness_check.py",
    )


# ──────────────────────────────────────────────────────────────────
# Mapper: canonical-phrase coverage
# ──────────────────────────────────────────────────────────────────

CANONICAL_PHRASES = (
    ("stats",                             "stats"),
    ("calls today",                       "calls_today"),
    ("calls this week",                   "calls_week"),
    ("response rate",                     "response_rate"),
    ("bookings today",                    "bookings_today"),
    ("callbacks",                         "callbacks_due"),
    ("queue",                             "queue"),
    ("incidents",                         "incidents"),
    ("policy",                            "policy"),
    ("health",                            "health"),
    ("are we paused",                     "paused_status"),
    ("help",                              "help"),
    ("leads today",                       "leads_today"),
)


def test_canonical_phrases_map_correctly():
    from app.services.slack.operator_intents import match_intent
    for phrase, expected in CANONICAL_PHRASES:
        result = match_intent(phrase)
        assert result["intent"] == expected, (
            f"{phrase!r} → {result['intent']!r}, expected {expected!r}"
        )


def test_alias_variants_match_same_intent():
    from app.services.slack.operator_intents import match_intent
    cases = (
        # response_rate aliases
        ("response rate",                "response_rate"),
        ("what's our response rate?",    "response_rate"),
        ("pickup rate",                  "response_rate"),
        ("connection rate",              "response_rate"),
        # bookings_today aliases (the user's literal example)
        ("did we book any clients for showing",      "bookings_today"),
        ("did we book any clients for showing?",     "bookings_today"),
        ("bookings today",                           "bookings_today"),
        ("any bookings today",                       "bookings_today"),
        # paused_status aliases
        ("are we paused",                "paused_status"),
        ("is pas paused",                "paused_status"),
        ("are we live",                  "paused_status"),
        # calls_today "have we had" variant (PAS191-A)
        ("how many calls have we had today",         "calls_today"),
        ("how many calls have we had today?",        "calls_today"),
    )
    for phrase, expected in cases:
        result = match_intent(phrase)
        assert result["intent"] == expected, (
            f"{phrase!r} → {result['intent']!r}, expected {expected!r}"
        )


def test_normalisation_strips_case_whitespace_and_punctuation():
    from app.services.slack.operator_intents import match_intent
    assert match_intent("  STATS  ")["intent"] == "stats"
    assert match_intent("Stats?")["intent"] == "stats"
    assert match_intent("\thelp.\n")["intent"] == "help"
    assert match_intent("HELP!!!")["intent"] == "help"
    # Internal whitespace collapse:
    assert match_intent("calls    today")["intent"] == "calls_today"


def test_empty_input_returns_unknown():
    from app.services.slack.operator_intents import match_intent
    for text in ("", "   ", "\n\t", None):  # type: ignore[arg-type]
        result = match_intent(text)  # type: ignore[arg-type]
        assert result["intent"] == "unknown"
        assert result["matched_alias"] == ""


def test_mutation_command_prefixes_always_return_unknown():
    """Pause / resume / push / remove must NEVER bind via the fuzzy matcher."""
    from app.services.slack.operator_intents import match_intent
    bad_phrases = (
        "pause",
        "pause please",
        "resume",
        "resume now",
        "push 123 Main St",
        "remove 123 Main St",
        "pause everything for a moment",
    )
    for p in bad_phrases:
        result = match_intent(p)
        assert result["intent"] == "unknown", (
            f"mutation phrase {p!r} fuzzily bound to {result['intent']!r}"
        )
        assert result["matched_alias"] == ""


def test_unknown_phrases_return_unknown_with_empty_alias():
    from app.services.slack.operator_intents import match_intent
    cases = (
        "what is the meaning of life",
        "send a marketing email",
        "trip the breaker",
        "delete the database",
        "run a migration",
    )
    for phrase in cases:
        result = match_intent(phrase)
        assert result["intent"] == "unknown"
        assert result["matched_alias"] == ""


def test_alias_table_is_meaningfully_populated():
    from app.services.slack.operator_intents import alias_count
    n = alias_count()
    assert n >= 50, f"alias table only has {n} entries — expected >=50"


def test_intent_codes_has_exactly_thirteen_entries():
    """
    PAS191 closed-intent count guard. PAS191-B bumped this from 12
    to 13; PAS192 added `today_summary` and `next_action` to bring
    the total to 15. Every bump must be a deliberate code change
    with a new alias-table entry, formatter, and dispatcher branch.
    """
    from app.services.slack.operator_intents import (
        INTENT_CODES,
        INTENT_UNKNOWN,
    )
    assert len(INTENT_CODES) == 15
    assert INTENT_UNKNOWN not in INTENT_CODES


def test_leads_today_phrases_map_to_intent():
    """PAS191-B — natural questions about today's lead intake."""
    from app.services.slack.operator_intents import match_intent
    cases = (
        "how many leads did we get today",
        "leads today",
        "new leads today",
        "how many new leads came in today",
        "did we get any leads today",
        # punctuation / case / whitespace variants are normalised:
        "How Many Leads Did We Get Today?",
        "  leads   today  ",
        "did we get any leads today?!",
    )
    for phrase in cases:
        result = match_intent(phrase)
        assert result["intent"] == "leads_today", (
            f"{phrase!r} → {result['intent']!r}, expected 'leads_today'"
        )


def test_leads_today_formatter_renders_safe_message():
    """The leads_today formatter renders the three required counts and is PII-safe."""
    from app.services.slack import operator_responses as r
    # Full payload renders all three labels with the given counts.
    s = r.format_leads_today({"new_leads": 5, "call_eligible": 3, "pending_queue": 2})
    assert "leads today" in s.lower()
    assert "new leads: 5" in s.lower()
    assert "call eligible: 3" in s.lower()
    assert "pending queue: 2" in s.lower()
    # Empty payload → all zeros, never raises.
    s0 = r.format_leads_today({})
    assert "new leads: 0" in s0.lower()
    assert "call eligible: 0" in s0.lower()
    assert "pending queue: 0" in s0.lower()
    # The formatter must NEVER include PII labels regardless of input,
    # because it only accepts the three numeric counts and never
    # touches lead names / phone numbers / emails.
    for tok in ("phone", "email", "name=", "transcript"):
        assert tok not in s.lower()
        assert tok not in s0.lower()


# ──────────────────────────────────────────────────────────────────
# Formatter
# ──────────────────────────────────────────────────────────────────

def test_formatters_handle_empty_inputs():
    from app.services.slack import operator_responses as r
    assert "stats" in r.format_stats({}).lower()
    assert "calls today" in r.format_calls_today({}).lower()
    assert "calls this week" in r.format_calls_week({}).lower()
    assert "response rate" in r.format_response_rate({}).lower()
    assert "bookings today" in r.format_bookings_today({}).lower()
    assert "callbacks" in r.format_callbacks_due({}).lower()
    assert "queue" in r.format_queue({}).lower()
    assert "incidents" in r.format_incidents({}).lower()
    assert "policy" in r.format_policy({}).lower()
    assert "health" in r.format_health({}).lower()
    assert "leads today" in r.format_leads_today({}).lower()
    s = r.format_paused_status({"active": False})
    assert "paused" in s.lower()
    assert "active" in r.format_paused_status({"active": True}).lower()
    assert "not available" in r.format_paused_status({"active": None}).lower()
    assert "help" not in r.format_help() or "questions" in r.format_help().lower()
    assert "didn" in r.format_unknown().lower() or "recogn" in r.format_unknown().lower()


def test_formatters_never_echo_raw_zero_as_text():
    from app.services.slack import operator_responses as r
    s = r.format_bookings_today({"booked_count": 0})
    assert "no showings" in s.lower()
    s = r.format_callbacks_due({"pending_count": 0, "overdue_count": 0})
    assert "no pending callbacks" in s.lower()
    s = r.format_incidents({"open_count": 0, "severity_counts": {}})
    assert "no open incidents" in s.lower()


def test_pii_defence_collapses_poisoned_input():
    """A formatter receiving a poisoned label must collapse to the redacted line."""
    from app.services.slack import operator_responses as r
    poisoned = r.format_health({
        "db": "up",
        "worker": "off",
        "twilio": "configured — token=secret123",
    })
    assert "redacted" in poisoned.lower()


def test_format_error_never_echoes_message():
    from app.services.slack import operator_responses as r
    out = r.format_error("stats", "DatabaseError('private secret here')")
    assert "private secret" not in out
    assert "couldn't fetch" in out.lower()
    out2 = r.format_error("not_an_intent", "RuntimeError")
    assert "request" in out2.lower()


# ──────────────────────────────────────────────────────────────────
# Route wire-through
# ──────────────────────────────────────────────────────────────────

def test_route_imports_pas191_modules():
    src = _read("app/routes/slack_command.py")
    assert "from app.services.slack.operator_intents import" in src
    assert "from app.services.slack import operator_responses as pas191_responses" in src


def test_route_fast_path_before_llm():
    src = _read("app/routes/slack_command.py")
    fast = src.find("match_intent(text)")
    llm = src.find("_parse_intent(text)")
    assert fast > 0 and llm > 0, "missing key call sites"
    assert fast < llm, "PAS191 fast-path must fire BEFORE LLM intent parser"


def test_route_dispatch_function_exists():
    src = _read("app/routes/slack_command.py")
    assert "_pas191_dispatch" in src
    assert "slack.intent.matched" in src


# ──────────────────────────────────────────────────────────────────
# Doctrine — no forbidden patterns
# ──────────────────────────────────────────────────────────────────

def test_intents_module_no_unsafe_constructs():
    src = _read("app/services/slack/operator_intents.py")
    # eval/exec are catastrophic — must be absent even in docstrings.
    assert "eval(" not in src
    assert "exec(" not in src
    # No regex / threading / autonomy.
    assert "re.compile(" not in src
    assert "threading.Thread(" not in src
    assert "asyncio.create_task(" not in src


def test_intents_module_has_no_llm_import():
    src = _read("app/services/slack/operator_intents.py")
    # No LLM provider import at all in the pure mapper.
    assert "app.services.llm" not in src
    assert "from anthropic" not in src
    assert "import anthropic" not in src


def test_responses_module_no_network_imports():
    src = _read("app/services/slack/operator_responses.py")
    for tok in (
        "requests.get(",
        "requests.post(",
        "httpx.get(",
        "httpx.post(",
        "urllib.request.urlopen(",
        "subprocess.",
    ):
        assert tok not in src, f"forbidden token {tok!r} in operator_responses.py"


def test_responses_module_has_no_llm_import():
    src = _read("app/services/slack/operator_responses.py")
    assert "app.services.llm" not in src
    assert "from anthropic" not in src
    assert "import anthropic" not in src


def test_doctrine_doc_carries_required_clauses():
    src = _read("docs/pas191_slack_natural_language_commands.md").lower()
    required = (
        "purpose",
        "relationship to pas190",
        "deterministic mapping doctrine",
        "closed intent set doctrine",
        "no llm doctrine",
        "no mutation via natural language",
        "pii redaction doctrine",
        "fail-closed on unknown intent",
        "operator help doctrine",
        "alias table curation doctrine",
        "intentionally does not build",
        "no autonomous remediation",
        "remaining limitations",
        "no gmail",
        "composio",
    )
    for clause in required:
        assert clause in src, f"doctrine doc missing clause: {clause!r}"


def test_doctrine_doc_no_forbidden_scope_tokens():
    src = _read("docs/pas191_slack_natural_language_commands.md").lower()
    bad = (
        "gmail oauth integration",
        "composio integration",
        "auto-approve memory",
        "embedding model",
        "vector store",
        "ai chat assistant enabled",
        "imap inbox scanner",
        "pop3 inbox scanner",
        "auto-trip enabled",
        "autonomous trip",
        "free-form llm reply",
    )
    for tok in bad:
        assert tok not in src, f"forbidden token in doctrine doc: {tok!r}"


# ──────────────────────────────────────────────────────────────────
# PAS191-C — Today-filter helpers use Python-computed ISO cutoffs
# ──────────────────────────────────────────────────────────────────

# PostgREST does NOT evaluate SQL expressions like "now() - interval"
# in filter values — they get compared as literal strings and return
# zero rows. Every PAS191 helper that filters on a date column must
# compute its cutoff Python-side and pass an ISO-formatted timestamp.

_PAS191_HELPER_FUNCTIONS = (
    "_pas191_calls",
    "_pas191_bookings_today",
    "_pas191_callbacks_due",
    "_pas191_leads_today",
)


def _extract_function_body(src: str, fn_name: str) -> str:
    """
    Return the source-text body of a top-level `def fn_name(...)` block.
    Stops at the next top-level def/class line.
    """
    marker = f"def {fn_name}("
    start = src.find(marker)
    assert start >= 0, f"function {fn_name} missing from slack_command.py"
    line_start = src.rfind("\n", 0, start) + 1
    end = len(src)
    # Walk lines after the def looking for the next top-level def/class.
    cursor = src.find("\n", start) + 1
    while cursor < len(src):
        nl = src.find("\n", cursor)
        nl = len(src) if nl < 0 else nl
        line = src[cursor:nl]
        # A top-level def/class is column-0 — body lines are indented.
        if line and not line[0].isspace() and (
            line.startswith(("def ", "async def ", "class "))
        ):
            end = cursor
            break
        cursor = nl + 1
    return src[line_start:end]


def test_pas191_helpers_have_no_sql_expression_filter_literals():
    """No PAS191 helper may pass a SQL-expression string to gte/lt."""
    src = _read("app/routes/slack_command.py")
    for fn in _PAS191_HELPER_FUNCTIONS:
        body = _extract_function_body(src, fn)
        assert "now() - interval" not in body, (
            f"{fn} still passes 'now() - interval ...' as a filter literal — "
            "PostgREST will not evaluate it"
        )
        # Bare "now()" string literals are similarly inert; the helper
        # must use _pas191_now_iso() if it needs the current timestamp.
        assert '"now()"' not in body and "'now()'" not in body, (
            f"{fn} still passes bare 'now()' as a filter literal"
        )


def test_pas191_cutoff_helpers_defined_and_used():
    """The Python-side cutoff helpers must exist and be referenced."""
    src = _read("app/routes/slack_command.py")
    assert "def _pas191_cutoff_iso(" in src
    assert "def _pas191_now_iso(" in src
    # The cutoff helpers must use timezone-aware UTC time so the ISO
    # string round-trips through PostgREST cleanly.
    assert "datetime.now(timezone.utc)" in src
    assert ".isoformat()" in src
    # And every date-filtered helper must actually call one of them.
    for fn in _PAS191_HELPER_FUNCTIONS:
        body = _extract_function_body(src, fn)
        if fn == "_pas191_callbacks_due":
            # The callbacks helper compares against "now" for the
            # overdue branch, not against "today".
            assert "_pas191_now_iso(" in body, (
                f"{fn} must call _pas191_now_iso()"
            )
        else:
            assert "_pas191_cutoff_iso(" in body, (
                f"{fn} must call _pas191_cutoff_iso()"
            )


def test_pas191_cutoff_helpers_return_iso_timestamps():
    """Helpers must return parseable ISO 8601 timestamps in UTC."""
    from datetime import datetime as _dt, timezone as _tz
    from app.routes.slack_command import (
        _pas191_cutoff_iso,
        _pas191_now_iso,
    )
    for value in (_pas191_cutoff_iso(1), _pas191_cutoff_iso(7), _pas191_now_iso()):
        # fromisoformat accepts the format datetime.isoformat() emits,
        # including the +00:00 offset for timezone-aware datetimes.
        parsed = _dt.fromisoformat(value)
        assert parsed.tzinfo is not None, f"{value!r} is not timezone-aware"
        # UTC offset is zero for tzinfo=timezone.utc
        assert parsed.utcoffset().total_seconds() == 0, (
            f"{value!r} must be in UTC"
        )


def test_pas191_leads_today_passes_iso_to_gte():
    """
    Runtime: the leads_today helper must pass an ISO-formatted UTC
    timestamp to PostgREST's `gte`, not a SQL-expression string.
    """
    from datetime import datetime as _dt
    from app.routes import slack_command as sc

    captured: list = []

    class _FakeChain:
        def select(self, *a, **kw): return self
        def eq(self, *a, **kw): return self
        def gte(self, col, val):
            captured.append(("gte", col, val))
            return self
        def lt(self, col, val):
            captured.append(("lt", col, val))
            return self
        def execute(self):
            class _R: data = []
            return _R()

    class _FakeDB:
        def table(self, name):
            captured.append(("table", name))
            return _FakeChain()

    original = sc.get_supabase
    sc.get_supabase = lambda: _FakeDB()  # type: ignore[assignment]
    try:
        result = sc._pas191_leads_today("orvn-demo-01")
    finally:
        sc.get_supabase = original  # type: ignore[assignment]

    # Helper still returns the contract-shaped dict.
    assert set(result.keys()) == {"new_leads", "call_eligible", "pending_queue"}
    # Every `gte` value must parse as an ISO timestamp.
    gte_calls = [c for c in captured if c[0] == "gte"]
    assert gte_calls, "no gte filter was recorded"
    for _, col, val in gte_calls:
        assert "now()" not in val, (
            f"{col}={val!r} still passes a SQL expression to PostgREST"
        )
        parsed = _dt.fromisoformat(val)
        assert parsed.tzinfo is not None, f"{val!r} is not timezone-aware"


# ──────────────────────────────────────────────────────────────────
# Event contract
# ──────────────────────────────────────────────────────────────────

def test_event_contract_carries_pas191_event_types():
    src = _read("app/services/events/contract.py")
    assert '"slack.intent.matched"' in src
    assert '"slack.intent.unknown"' in src


# ──────────────────────────────────────────────────────────────────
# Readiness gate
# ──────────────────────────────────────────────────────────────────

def _run_gate(*args: str) -> "subprocess.CompletedProcess[str]":
    cmd = [
        sys.executable,
        str(_REPO_ROOT / "scripts" / "pas191_slack_nl_command_readiness_check.py"),
        *args,
    ]
    return subprocess.run(
        cmd,
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=120,
    )


def test_readiness_gate_exits_ready():
    proc = _run_gate("--summary-only")
    assert proc.returncode == 0, (
        f"PAS191 gate FAILED (rc={proc.returncode})\n"
        f"STDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"
    )
    assert "verdict=READY" in proc.stdout


def test_readiness_gate_bad_args_exits_two():
    proc = _run_gate("--no-such-flag")
    assert proc.returncode == 2


def test_readiness_gate_json_mode_emits_valid_envelope():
    proc = _run_gate("--summary-only", "--json")
    assert proc.returncode == 0
    # Locate the JSON line (gate prints summary first, then JSON).
    payload_str = proc.stdout[proc.stdout.find("{"):]
    payload = json.loads(payload_str)
    assert payload["phase"] == "PAS191"
    assert payload["verdict"] == "READY"
    assert payload["ready"] is True
    assert payload["fail_count"] == 0
    assert payload["blocker_count"] == 0
    assert payload["check_count"] > 0


# ──────────────────────────────────────────────────────────────────
# Carry-forward — prior gates still pass
# ──────────────────────────────────────────────────────────────────

def _run_prior(relpath: str) -> "subprocess.CompletedProcess[str]":
    return subprocess.run(
        [sys.executable, str(_REPO_ROOT / relpath), "--summary-only"],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=120,
    )


def test_pas186_carry_forward_ready():
    proc = _run_prior("scripts/pas186_final_cutover_readiness_check.py")
    assert proc.returncode == 0, proc.stdout + proc.stderr


def test_pas187_carry_forward_ready():
    proc = _run_prior("scripts/pas187_fleet_cutover_readiness_check.py")
    assert proc.returncode == 0, proc.stdout + proc.stderr


def test_pas188_carry_forward_ready():
    proc = _run_prior("scripts/pas188_operational_scaling_readiness_check.py")
    assert proc.returncode == 0, proc.stdout + proc.stderr


def test_pas189_carry_forward_ready():
    proc = _run_prior("scripts/pas189_operational_wirethrough_readiness_check.py")
    assert proc.returncode == 0, proc.stdout + proc.stderr


def test_pas190_carry_forward_ready():
    proc = _run_prior("scripts/pas190_final_wirethrough_readiness_check.py")
    assert proc.returncode == 0, proc.stdout + proc.stderr
