# PAS203 — Slack Read-Only Evidence Digest Command

## Purpose

PAS201 produces the simulation evidence digest; PAS202 renders it
as a Slack-safe markdown string. PAS203 closes the loop for
operators by exposing that rendering as a deterministic
**read-only Slack intent** — a brokerage manager can type
`/pas simulation digest` (or any of the recognised phrases) and
receive the latest digest summary inside Slack.

PAS203 is **strictly read-only**. It never:

* sends any outbound Slack API call (the module returns a
  string — the existing dispatcher converts it into a Slack
  response on the path already used by PAS191 / PAS192);
* executes a simulation;
* generates or writes any artefact, including no read-only
  summary file;
* mutates any production system, brokerage row, or queue;
* makes any live-routing or "strategy deployed" claim — a
  defensive guard rejects any rendering that contains a
  forbidden live-routing token.

## What PAS203 proves

* **A deterministic Slack intent maps recognised phrases to the
  simulation digest.** Six spec-required phrases — `simulation
  digest`, `evidence digest`, `show simulation evidence`, `what
  did the simulation prove`, `rehearsal evidence`, `strategy
  evidence` — plus a small set of natural variants resolve to
  the `simulation_digest` intent. Anything else returns False
  and falls through to the existing PAS191 matcher unchanged.
* **PAS191 / PAS192 carry-forward is intact.** PAS203 ships a
  **new** module (`app/services/slack/simulation_digest_intent.py`)
  with its own intent constant, alias table, and matcher. It
  does NOT touch `operator_intents.py` or `operator_responses.py`;
  the PAS191 / PAS192 tests assert `len(INTENT_CODES) == 15` and
  PAS203 holds that invariant by construction. The readiness
  gate verifies it explicitly.
* **The Slack path is read-only.** The loader walks
  `reports/simulations/` for `pas201_simulation_evidence_digest_*.json`
  files, sorts by filename (PAS201 filenames embed sortable UTC
  timestamps), reads the newest, validates its top-level
  contract (`phase=PAS201`, `allowed_environment=SIMULATION_ONLY`,
  `live_behavior_changed=False`), and hands it to PAS202's
  `format_digest_for_slack`. No write call appears anywhere on
  the Slack path; the readiness gate asserts the service file
  contains no `write_text` / `write_bytes` / `mkdir` / `touch`
  / `rename` / `unlink` / `rmdir` calls.
* **The output is bounded.** Rendering delegates to PAS202's
  Slack formatter, which is itself bounded to closed
  vocabularies and hard-capped at 4 000 characters. A defensive
  per-call scan refuses any output that contains
  `live_routing_active`, `live_call_routed`,
  `strategy_deployed_live`, `real_lead_handled`, or
  `production_traffic_served`.
* **The missing-digest case is a clean fallback.** If
  `reports/simulations/` has no PAS201 digest, the matcher still
  returns a recognised response — the bounded
  `MISSING_DIGEST_FALLBACK_MESSAGE` that points the operator at
  the PAS201 CLI. The Slack path never raises into the
  dispatcher and never leaks underlying exception text.
* **No outbound Slack API call.** PAS203 source does not import
  `slack_sdk` and does not import the outbound Slack
  notification client (`app.services.notifications.slack_client`).
  The readiness gate enforces this by AST import scan.
* **No execution dependencies.** PAS203 source does not import
  `twilio`, `openai`, `anthropic`, `dotenv`, `supabase`, the
  live state machine, or `app.engine.*`. The readiness gate
  enforces this by AST import scan.
* **No forbidden status literals.** The strings `APPROVED`,
  `APPLIED`, `AUTO_APPLIED`, `LIVE`, `DEPLOYED` never appear as
  string constants in PAS203 source.
* **No forbidden live-mutation / outbound-messaging identifiers.**
  Fourteen identifier names — `apply_recommendation`,
  `deploy_strategy`, `switch_strategy_live`, `auto_apply`,
  `auto_promote`, `force_promote`, `live_apply`, `auto_deploy`,
  `route_lead_live`, `route_call_live`, `send_real_sms`,
  `send_real_call`, `send_slack_message`, `post_to_slack` —
  are absent from PAS203 source.

## What PAS203 does not prove

* **PAS203 does not send a Slack message.** It returns a
  string; the existing dispatcher converts strings into Slack
  responses through the path PAS191 / PAS192 already use.
* **PAS203 does not modify the PAS191 / PAS192 intent layer.**
  The PAS191 `INTENT_CODES` tuple, the alias table, and
  `format_help()` are all unchanged. PAS203 ships
  `SIMULATION_DIGEST_HELP_LINES` as a closed tuple of
  help-line additions; integrating them into the help message
  is a deliberate dispatcher-side change documented below.
* **PAS203 does not generate a digest.** If no PAS201 digest
  is on disk, the response is a fallback — Slack never
  triggers digest generation.
* **PAS203 does not promote a strategy or route a live call.**
* **PAS203 does not validate digest evidence against live
  outcomes.** Calibration belongs to PAS204+.

## How an operator uses it (once integrated)

```
/pas simulation digest
/pas what did the simulation prove?
/pas show simulation evidence
/pas rehearsal evidence
/pas strategy evidence
/pas evidence digest
```

Any of those resolve to the `simulation_digest` intent. The
Slack response is the PAS202 Slack-safe rendering of the latest
PAS201 digest, or — if no digest is on disk — the bounded
"no digest found yet, run PAS201 first" fallback message.

If you want to test PAS203 directly (no Slack required):

```python
from pathlib import Path
from app.services.slack.simulation_digest_intent import (
    try_route_simulation_digest,
)
out = try_route_simulation_digest(
    "simulation digest",
    Path("reports/simulations"),
)
print(out)
```

## Dispatcher integration (follow-up wiring step)

PAS203 ships the bounded building blocks. Wiring them into the
existing `/pas` slash-command dispatcher (`app/routes/slack_command.py`)
is a small, deliberate, additive edit that this PAS leaves to
the operator. The shape of the change:

```python
# In app/routes/slack_command.py, after parsing operator text
# and BEFORE invoking PAS191's match_intent():
from pathlib import Path
from app.services.slack.simulation_digest_intent import (
    try_route_simulation_digest,
)

REPORTS_DIR = Path(__file__).resolve().parents[2] / "reports" / "simulations"

simulation_digest_response = try_route_simulation_digest(text, REPORTS_DIR)
if simulation_digest_response is not None:
    return JSONResponse({"text": simulation_digest_response})
```

And to surface the help additions:

```python
# Where format_help() is called, append PAS203's lines:
from app.services.slack.simulation_digest_intent import (
    SIMULATION_DIGEST_HELP_LINES,
)
help_text = pas191_responses.format_help() + "\n" + "\n".join(
    SIMULATION_DIGEST_HELP_LINES,
)
```

The PAS203 readiness gate runs without the dispatcher edit
because PAS203 is self-contained — wiring is a deliberate,
operator-controlled step.

## Claimable today (with PAS203 merged)

* PAS203 ships a deterministic, read-only Slack intent module
  for the PAS201 evidence digest with six spec-required
  phrases and a small set of natural-variant aliases.
* The Slack path is strictly read-only: no `write_text`, no
  `mkdir`, no outbound Slack API call, no simulation
  execution, no digest generation.
* PAS191 / PAS192 carry-forward is intact: `INTENT_CODES`
  still has exactly 15 entries, alias counts are unchanged,
  and `format_help()` is byte-for-byte unmodified.
* The Slack response is bounded: it delegates to PAS202's
  Slack formatter (which is itself bounded to closed
  vocabularies and a 4 000-character cap) and adds a
  defensive forbidden-token guard on top.
* Missing-digest case is a clean operator-readable fallback.
* No PII, no production brokerage IDs, no live-routing
  wording in any rendering.

## Still not claimable (PAS204+)

* PAS203 is not yet wired into the production dispatcher. The
  two-snippet integration step lives in this doc and is a
  deliberate operator-side choice; until that edit lands, the
  Slack command will not actually fire from `/pas`.
* PAS203 does not validate digest strength against live-call
  performance.
* PAS203 does not let operators trigger digest generation from
  Slack (running PAS201 from Slack would be a mutating
  surface; the current path is strictly read-only).
* PAS203 does not modify PAS191's natural-language matcher; an
  operator can still type any of the 15 PAS191 / PAS192
  intents and they continue to behave as before.

## Future PAS204 path

PAS204 is the next bounded step: an operator-confirmed
**digest-generation-on-demand** Slack action that, with explicit
confirmation, runs the PAS201 build flow in the background and
posts the resulting digest summary back. Expected shape:

1. A new "mutating" command branch (gated behind explicit
   confirmation, parallel to the existing pause/resume/push
   exact-command branch).
2. A bounded background runner that calls PAS201's CLI in
   `SIMULATION_ONLY` mode and writes the new digest under
   `reports/simulations/`.
3. A readiness gate asserting the runner cannot bypass the
   PAS201 contract (no live-routing identifiers, no
   PAS191/PAS192 mutations).
4. Tests asserting the runner remains structurally
   `SIMULATION_ONLY` and cannot trigger any production
   behaviour.

PAS204 is **not** PAS203's responsibility. PAS203 ships the
read-only Slack surface; PAS204 ships the operator-confirmed
mutating surface.

## Safety constraints (inherited + extended)

PAS203 inherits the full PAS191 / PAS192 / PAS201 / PAS202
safety doctrine:

* No real leads, no real phone calls, no Twilio live calls.
* No outbound Slack messages — PAS203 returns strings; the
  existing dispatcher converts strings into Slack responses on
  the path PAS191 / PAS192 already use.
* No worker auto-start, no production brokerage mutation.
* No new SQL migration, no edits to
  `combined_supabase_migration.sql`.
* No secret-shaped tokens in source or in renderings.
* No PII in renderings — no free-form text fields, no real
  user ids, no email addresses, no phone numbers, no
  production brokerage UUIDs.
* No autonomous-apply / outbound-messaging identifiers in
  PAS203 source — readiness gate enforces by AST scan.
* No forbidden status literals (`APPROVED`, `APPLIED`,
  `AUTO_APPLIED`, `LIVE`, `DEPLOYED`) in PAS203 source —
  readiness gate enforces by AST string-constant scan.
* No live-routing assertions in any rendering — a defensive
  check rejects any output that contains a forbidden token.
* No filesystem writes anywhere on the Slack path — readiness
  gate scans the service file for `write_text` / `write_bytes`
  / `mkdir` / `touch` / `rename` / `unlink` / `rmdir`.
* Input digest must carry `phase=PAS201`,
  `allowed_environment=SIMULATION_ONLY`,
  `live_behavior_changed=False`. PAS203's loader refuses
  anything else.

## How to run

```
# Compile-check.
python -m compileall -q app scripts tests

# Unit + integration tests (PAS203 only, plus carry-forward
# spot-checks PAS191 / PAS192 / PAS202 still pass).
python -m pytest \
    tests/mvp/test_pas191_slack_natural_language_commands.py \
    tests/mvp/test_pas192_slack_operator_experience.py \
    tests/mvp/test_pas202_evidence_digest_surface.py \
    tests/mvp/test_pas203_slack_evidence_digest_command.py -q

# Read-only readiness gate.
python scripts/pas203_slack_evidence_digest_readiness_check.py --summary-only
```

There is no PAS203 CLI binary — the surface is a Slack intent
module designed to be invoked by the dispatcher. The PAS203
readiness gate is the only script.

## Relationship to PAS191 / PAS192 / PAS202

PAS203 is purely additive over all three:

* **PAS191** — new file, new intent constant, new alias table.
  No edits to `operator_intents.py`. `INTENT_CODES` count is
  unchanged at 15 (asserted by both PAS191 and PAS192 tests).
* **PAS192** — no edits to `operator_responses.py`.
  `format_help()` byte-for-byte unchanged. The
  `SIMULATION_DIGEST_HELP_LINES` tuple ships separately and is
  intended for the dispatcher to concatenate post-help if the
  operator chooses to surface the new intent.
* **PAS202** — PAS203 *uses* `format_digest_for_slack`
  unchanged. No duplication of formatting logic. PAS203 adds
  loader + intent + fallback + defensive guard on top.

A PAS203 response is always either the PAS202 Slack rendering
of a validated PAS201 digest, or the bounded fallback string —
never anything else.
