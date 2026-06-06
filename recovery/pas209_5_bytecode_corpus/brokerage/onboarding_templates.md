# brokerage/onboarding_templates

- **pyc:** `app\services\brokerage\__pycache__\onboarding_templates.cpython-314.pyc`
- **expected source path (absent):** `app\services\brokerage/onboarding_templates.py`
- **co_filename (from bytecode):** `app\services\brokerage\onboarding_templates.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** brokerage

## Module docstring

```
PAS173 — Brokerage onboarding templates (deterministic).

Pure data. No AI generation, no LLM call, no DB read, no env
read. Every template here is a closed-shape, structurally-bounded
dict the operator route hands back to the dashboard.

Doctrine:

* **Deterministic.** Same input → same output, byte-for-byte.
* **No secrets.** Placeholders for sensitive values
  (``<TWILIO_AUTH_TOKEN>``, ``<CALCOM_API_KEY>``, etc.) are
  the only references — never the real values.
* **No PII.** Sample contact values in any template are the
  sanitised placeholders defined in the PAS170 smoke plan
  (``Smoke Test`` / ``(555) 555-0100`` / ``smoke@example.com``).
* **Bounded structure.** Every template is a list of steps,
  each step a closed dict with the same shape.
* **No dynamic AI generation.** Operators get the same
  checklist every time so the audit trail is reproducible.

Public surface:

  * ``brokerage_onboarding_checklist(...)``
  * ``launch_checklist(...)``
  * ``rollback_checklist(...)``
  * ``smoke_test_template(...)``
  * ``pilot_expansion_checklist(...)``

Each helper returns a closed-shape envelope::

    {
      "template":     "<name>",
      "brokerage_id": "<placeholder | provided id>",
      "generated_at": None,                # deterministic — no timestamp
      "steps":        [<step dict>, ...],
      "warnings":     [],
      "error_code":   None,
    }
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_bound_brokerage_id`, `_envelope`, `_step`, `brokerage_onboarding_checklist`, `launch_checklist`, `pilot_expansion_checklist`, `rollback_checklist`, `smoke_test_template`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS173 — Brokerage onboarding templates (deterministic).\n\nPure data. No AI generation, no LLM call, no DB read, no env\nread. Every template here is a closed-shape, structurally-bounded\ndict the operator route hands back to the dashboard.\n\nDoctrine:\n\n* **Deterministic.** Same input → same output, byte-for-byte.\n* **No secrets.** Placeholders for sensitive values\n  (``<TWILIO_AUTH_TOKEN>``, ``<CALCOM_API_KEY>``, etc.) are\n  the only references — never the real values.\n* **No PII.** Sample contact values in any template are the\n  sanitised placeholders defined in the PAS170 smoke plan\n  (``Smoke Test`` / ``(555) 555-0100`` / ``smoke@example.com``).\n* **Bounded structure.** Every template is a list of steps,\n  each step a closed dict with the same shape.\n* **No dynamic AI generation.** Operators get the same\n  checklist every time so the audit trail is reproducible.\n\nPublic surface:\n\n  * ``brokerage_onboarding_checklist(...)``\n  * ``launch_checklist(...)``\n  * ``rollback_checklist(...)``\n  * ``smoke_test_template(...)``\n  * ``pilot_expansion_checklist(...)``\n\nEach helper returns a closed-shape envelope::\n\n    {\n      "template":     "<name>",\n      "brokerage_id": "<placeholder | provided id>",\n      "generated_at": None,                # deterministic — no timestamp\n      "steps":        [<step dict>, ...],\n      "warnings":     [],\n      "error_code":   None,\n    }\n'
- '<BROKERAGE_ID>'
- '<HOST>'
- '<ADMIN_KEY>'
- '<BROKERAGE_API_KEY>'
- '(555) 555-0100'
- 'Smoke Test'
- 'smoke@example.com'
- 'blocking'
- 'artefact'
- 'operator_action'
- 'value'
- 'Any'
- 'return'
- 'str'
- 'step_id'
- 'title'
- 'description'
- 'bool'
- 'Optional[str]'
- 'Dict[str, Any]'
- 'template'
- 'brokerage_id'
- 'steps'
- 'List[Dict[str, Any]]'
- 'generated_at'
- 'warnings'
- 'error_code'
- 'The full onboarding checklist an operator walks for a\nnew brokerage. Deterministic; no AI generation.'
- 'onboard.1.profile_created'
- 'Create the operational profile'
- 'Run ensure_profile(brokerage_id=...) so the operator surface has a side-car row for this brokerage. Idempotent.'
- 'app/services/brokerage/profile_service.py::ensure_profile'
- 'POST /ops/brokerages (PAS173 route) or call ensure_profile() from a script.'
- 'onboard.2.brokerage_row_credentials'
- 'Populate the brokerage row with credentials'
- 'Set twilio_phone, slack_webhook_url, and any alert_slack_webhook_url on the existing brokerages table via PAS admin routes. NEVER paste secrets into Slack / chat / git.'
- 'app/routes/admin.py::update_account'
- 'PATCH /admin/brokerages/{id} with the credential fields.'
- 'onboard.3.timezone_configured'
- "Set the brokerage's timezone on the profile"
- 'PAS170 Cal.com timezone resolver reads timezone from the brokerage row first; PAS173 profile mirrors it. Without a timezone, the lead sees the ET fallback.'
- 'app/services/booking/calcom_client.py::_resolve_brokerage_timezone'
- 'PATCH operator_brokerages with timezone set.'
- 'onboard.4.cal_com_probe'
- 'Verify Cal.com /slots returns 200, not 404'
- "Per operator checklist §3, curl /v2/slots with the brokerage's eventTypeId. STOP if HTTP 404."
- 'docs/orvn_external_pilot_operator_checklist.md#3'
- 'curl Cal.com /slots; coordinate with brokerage admin if 404.'
- 'onboard.5.run_smoke_matrix'
- 'Run the PAS170 smoke matrix against the demo brokerage'
- "Walk the PAS170 smoke_plan output to verify the engine + survival kit behave correctly with this brokerage's config."
- 'scripts/pas170_demo_brokerage_smoke_plan.py'
- 'python scripts/pas170_demo_brokerage_smoke_plan.py --brokerage-id <id>'
- 'onboard.6.mark_configured'
- 'Mark the profile CONFIGURED'
- 'Transition onboarding_status from IN_PROGRESS to CONFIGURED via the operator action.'
- 'app/services/operator/operator_actions.py::execute_action'
- "POST /ops/brokerages/{id}/actions {action:'mark_onboarding_stage', stage:'CONFIGURED'}"
- 'onboard.7.run_readiness_gates'
- 'Run the five readiness gates'
- 'PAS169-launch, PAS-LAUNCH-01, PAS170, PAS171, PAS172 must all report verdict=READY before VERIFIED.'
- 'scripts/pas171_external_pilot_readiness_check.py'
- 'python scripts/pas17X_*_readiness_check.py --summary-only'
- 'onboard.8.mark_verified'
- 'Mark the profile VERIFIED'
- 'Only the operator with audit-trail context (X-Admin-Key + actor_id) can transition the profile to VERIFIED.'
- "POST /ops/brokerages/{id}/actions {action:'mark_onboarding_stage', stage:'VERIFIED'}"
- 'onboard.9.go_live'
- 'Transition to LIVE only after the launch checklist passes'
- 'Run launch_checklist() and walk all blocking steps before transitioning onboarding_status to LIVE.'
- 'app/services/brokerage/onboarding_templates.py::launch_checklist'
- "POST /ops/brokerages/{id}/actions {action:'mark_onboarding_stage', stage:'LIVE'}"
- 'brokerage_onboarding_checklist'
- 'Launch checklist — the gating steps between VERIFIED\nand LIVE.'
- 'launch.1.readiness_gates_green'
- 'All readiness gates GREEN'
- 'Re-run the five readiness gates. Any NOT_READY blocks launch.'
- 'scripts/pas172_pilot_operations_readiness_check.py'
- 'python scripts/pas172_pilot_operations_readiness_check.py --summary-only'
- 'launch.2.heartbeat_wired'
- 'Worker heartbeat wired (if worker enabled)'
- 'If the operator plans to enable the PAS162 worker, the heartbeat helpers must be wired into the run script per orvn_pilot_ops_runbook.md §3.'
- 'docs/orvn_pilot_ops_runbook.md#3'
- 'Edit run_pending_calls_worker.py wrapper.'
- 'launch.3.alert_channel_configured'
- 'PAS_ALERT_SLACK_WEBHOOK_URL set'
- 'Required for outbound pilot alerts. Operator MUST set this on the deployment host.'
- 'docs/orvn_external_pilot_operator_checklist.md#4'
- 'Export PAS_ALERT_SLACK_WEBHOOK_URL; restart the FastAPI deployment.'
- 'launch.4.durable_stores_promoted'
- 'v15 / v16 / v18 / v19 / v20 migrations promoted'
- 'Durable backing for email dedupe / encryption / pending-call dedupe / callback schedule / worker heartbeats must be live OR the operator must accept the documented fallback posture.'
- 'docs/orvn_external_pilot_operator_checklist.md#2'
- 'Promote SQL via the Supabase SQL editor.'
- 'launch.5.first_30min_worker_off'
- 'Open external traffic with worker OFF for 30 min'
- 'Lets the dedupe + callback stores observe inbound shape before any Twilio dial fires.'
- 'docs/orvn_external_pilot_operator_checklist.md#5'
- 'Leave PENDING_CALLS_WORKER_ENABLED unset; observe ops route for 30 min.'
- 'launch.6.enable_worker'
- 'Enable the worker explicitly'
- "Only the literal env value 'true' enables the PAS162 worker. Then run scripts/run_pending_calls_worker.py."
- 'docs/orvn_pilot_ops_runbook.md#5'
- 'PENDING_CALLS_WORKER_ENABLED=true python scripts/run_pending_calls_worker.py'
- 'launch_checklist'
- 'Rollback path — how to revert to a known-good posture\nif a pilot opens and something goes wrong.'
- 'rollback.1.stop_worker'
- 'Stop the PAS162 worker'
- 'Send SIGTERM to scripts/run_pending_calls_worker.py and unset PENDING_CALLS_WORKER_ENABLED. No outbound dial fires while the worker is OFF.'
- 'SIGTERM the worker; unset env var.'
- 'rollback.2.pause_brokerage'
- 'Pause the brokerage profile'
- 'Transition onboarding_status to PAUSED so the operator dashboard reflects the rollback.'
- "POST /ops/brokerages/{id}/actions {action:'pause_brokerage'}"
- 'rollback.3.disable_durable_stores'
- 'Drop to PAS170 process-local fallback (optional)'
- 'If the durable Supabase tables are part of the incident, export PAS_PENDING_CALL_DEDUPE_DURABLE_ENABLED=false and PAS_CALLBACK_SCHEDULE_DURABLE_ENABLED=false and restart.'
- 'docs/orvn_external_pilot_operator_checklist.md#8.5'
- 'Export the env flags; restart the FastAPI deployment.'
- 'rollback.4.disable_pilot_slack'
- 'Disable pilot Slack alerts (optional)'
- 'unset PAS_ALERT_SLACK_WEBHOOK_URL if the alert channel is part of the incident. PAS171 transport collapses to skipped envelope.'
- 'docs/orvn_external_pilot_operator_checklist.md#8.4'
- 'unset PAS_ALERT_SLACK_WEBHOOK_URL; restart the FastAPI deployment.'
- 'rollback.5.capture_post_mortem'
- 'Capture queue + heartbeat snapshots'
- 'Pull /ops/pending-calls/queue and /ops/workers/status snapshots for the post-mortem file.'
- 'docs/orvn_pilot_ops_runbook.md#9'
- 'curl /ops/* with X-Admin-Key; save JSON.'
- 'rollback_checklist'
- 'The smoke-test template the operator runs against the\nbrokerage *before* opening external traffic. Mirrors the\nPAS170 smoke matrix shape with PAS173 sanitised\nplaceholders.'
- 'smoke.1.parse_admin'
- 'Email parse — admin-only'
- 'POST /email-ingestion/parse with X-Admin-Key. Expect call_eligible boolean + structural envelope; NO phone/email/name in the response.'
- 'app/routes/email_ingestion.py'
- 'curl -X POST '
- "/email-ingestion/parse -H 'X-Admin-Key: "
- '\' -d \'{"subject":"smoke","sender":"'
- '","body":"Name: '
- '; Phone: '
- '"}\''
- 'smoke.2.ingest_first_submission'
- 'First email ingest'
- 'POST /email-ingestion/ingest with the brokerage X-API-Key. Expect status=accepted, duplicate=False.'
- "/email-ingestion/ingest -H 'X-API-Key: "
- "' -d '{...same body...}'"
- 'smoke.3.ingest_duplicate'
- 'Duplicate email ingest'
- 'Re-run smoke.2 with the same body. Expect status=duplicate.'
- 'app/services/ingestion/pending_call_dedupe.py'
- 'Re-run smoke.2 verbatim.'
- 'smoke.4.queue_status'
- 'Queue status via ops route'
- 'GET /ops/pending-calls/queue?brokerage_id=<id>. Expect status=ok + structural counts.'
- 'app/routes/operator_ops.py'
- "curl -H 'X-Admin-Key: "
- '/ops/pending-calls/queue?brokerage_id=<id>'
- 'smoke.5.worker_status'
- 'Worker status via ops route'
- 'GET /ops/workers/status. Expect status=ok + stale.stale_count=0 (if the worker is wired in).'
- '/ops/workers/status'
- 'smoke.6.callback_round_trip'
- 'Callback schedule round trip'
- 'Schedule + list + reminder report via the PAS170 surface or the ops route. Expect zero PII in the envelope.'
- 'app/services/callbacks/callback_schedule.py'
- "POST /ops/brokerages/{id}/actions {action:'run_readiness_snapshot'}"
- 'smoke_test_template'
- 'Pilot expansion — TRUSTED_PILOT → EXPANDED_PILOT.\nRequired gates per PAS172/173 doctrine.'
- 'expand.1.single_pilot_clean_14_days'
- 'First pilot stable for ≥14 days'
- 'TRUSTED_PILOT must show zero unresolved P0/P1 incidents and zero unresolved fallback-notice events for 14 consecutive days.'
- 'docs/pas172_pilot_operations_control_layer.md'
- 'Manual review of /ops/* + alert channel history.'
- 'expand.2.durable_heartbeat_promoted'
- 'v20 worker_heartbeats promoted'
- 'Cannot run more than one external brokerage without a durable heartbeat source-of-truth.'
- 'scripts/migrate_v20_worker_heartbeats.sql'
- 'Promote v20 SQL via the Supabase SQL editor.'
- 'expand.3.reapers_scheduled_manually'
- 'Reaper cadence documented'
- 'Operator commits to running reap_pending_call_dedupe.py daily + reap_callback_schedule.py weekly per orvn_pilot_ops_runbook.md §4.'
- 'docs/orvn_pilot_ops_runbook.md#4'
- 'Document the cadence in the team runbook.'
- 'expand.4.profile_pilot_stage'
- 'Profile pilot_stage transitions to EXPANDED_PILOT'
- 'Operator action mark_pilot_stage records the transition with actor_id for audit trail.'
- 'app/services/operator/operator_actions.py'
- "POST /ops/brokerages/{id}/actions {action:'mark_pilot_stage', stage:'EXPANDED_PILOT'}"
- 'expand.5.second_brokerage_onboarding'
- 'Second brokerage onboarded via the same checklist'
- 'Walk brokerage_onboarding_checklist() for the second brokerage. The checklist must be identical step-by-step — same audit trail shape.'
- 'app/services/brokerage/onboarding_templates.py::brokerage_onboarding_checklist'
- 'Run brokerage_onboarding_checklist() and follow.'
- 'pilot_expansion_checklist'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS173 — Brokerage onboarding templates (deterministic).\n\nPure data. No AI generation, no LLM call, no DB read, no env\nread. Every template here is a closed-shape, structurally-bounded\ndict the operator route hands back to the dashboard.\n\nDoctrine:\n\n* **Deterministic.** Same input → same output, byte-for-byte.\n* **No secrets.** Placeholders for sensitive values\n  (``<TWILIO_AUTH_TOKEN>``, ``<CALCOM_API_KEY>``, etc.) are\n  the only references — never the real values.\n* **No PII.** Sample contact values in any template are the\n  sanitised placeholders defined in the PAS170 smoke plan\n  (``Smoke Test`` / ``(555) 555-0100`` / ``smoke@example.com``).\n* **Bounded structure.** Every template is a list of steps,\n  each step a closed dict with the same shape.\n* **No dynamic AI generation.** Operators get the same\n  checklist every time so the audit trail is reproducible.\n\nPublic surface:\n\n  * ``brokerage_onboarding_checklist(...)``\n  * ``launch_checklist(...)``\n  * ``rollback_checklist(...)``\n  * ``smoke_test_template(...)``\n  * ``pilot_expansion_checklist(...)``\n\nEach helper returns a closed-shape envelope::\n\n    {\n      "template":     "<name>",\n      "brokerage_id": "<placeholder | provided id>",\n      "generated_at": None,                # deterministic — no timestamp\n      "steps":        [<step dict>, ...],\n      "warnings":     [],\n      "error_code":   None,\n    }\n')
              STORE_NAME               0 (__doc__)

 42           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 44           LOAD_SMALL_INT           0
              LOAD_CONST               2 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              3 (typing)
              IMPORT_FROM              4 (Any)
              STORE_NAME               4 (Any)
              IMPORT_FROM              5 (Dict)
              STORE_NAME               5 (Dict)
              IMPORT_FROM              6 (List)
              STORE_NAME               6 (List)
              IMPORT_FROM              7 (Optional)
              STORE_NAME               7 (Optional)
              POP_TOP

 51           LOAD_CONST               3 ('<BROKERAGE_ID>')
              STORE_NAME               8 (_PLACEHOLDER_BROKERAGE_ID)

 52           LOAD_CONST               4 ('<HOST>')
              STORE_NAME               9 (_PLACEHOLDER_HOST)

 53           LOAD_CONST               5 ('<ADMIN_KEY>')
              STORE_NAME              10 (_PLACEHOLDER_ADMIN_KEY)

 54           LOAD_CONST               6 ('<BROKERAGE_API_KEY>')
              STORE_NAME              11 (_PLACEHOLDER_API_KEY)

 56           LOAD_CONST               7 ('(555) 555-0100')
              STORE_NAME              12 (_SANITISED_PHONE)

 57           LOAD_CONST               8 ('Smoke Test')
              STORE_NAME              13 (_SANITISED_NAME)

 58           LOAD_CONST               9 ('smoke@example.com')
              STORE_NAME              14 (_SANITISED_EMAIL)

 65           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA23D0, file "app\services\brokerage\onboarding_templates.py", line 65>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _bound_brokerage_id at 0x0000018C17FF0C30, file "app\services\brokerage\onboarding_templates.py", line 65>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              15 (_bound_brokerage_id)

 71           LOAD_CONST              12 ('blocking')

 76           LOAD_CONST              13 (False)

 71           LOAD_CONST              14 ('artefact')

 77           LOAD_CONST              15 (None)

 71           LOAD_CONST              16 ('operator_action')

 78           LOAD_CONST              15 (None)

 71           BUILD_MAP                3
              LOAD_CONST              17 (<code object __annotate__ at 0x0000018C18090470, file "app\services\brokerage\onboarding_templates.py", line 71>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _step at 0x0000018C18025230, file "app\services\brokerage\onboarding_templates.py", line 71>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              16 (_step)

 90           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18025330, file "app\services\brokerage\onboarding_templates.py", line 90>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _envelope at 0x0000018C180531B0, file "app\services\brokerage\onboarding_templates.py", line 90>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              17 (_envelope)

110           LOAD_NAME                8 (_PLACEHOLDER_BROKERAGE_ID)

109           BUILD_TUPLE              1
              LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA22E0, file "app\services\brokerage\onboarding_templates.py", line 109>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object brokerage_onboarding_checklist at 0x0000018C17EC4D20, file "app\services\brokerage\onboarding_templates.py", line 109>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              18 (brokerage_onboarding_checklist)

192           LOAD_NAME                8 (_PLACEHOLDER_BROKERAGE_ID)

191           BUILD_TUPLE              1
              LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA24C0, file "app\services\brokerage\onboarding_templates.py", line 191>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object launch_checklist at 0x0000018C180606F0, file "app\services\brokerage\onboarding_templates.py", line 191>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              19 (launch_checklist)

250           LOAD_NAME                8 (_PLACEHOLDER_BROKERAGE_ID)

249           BUILD_TUPLE              1
              LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA26A0, file "app\services\brokerage\onboarding_templates.py", line 249>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object rollback_checklist at 0x0000018C1800ABF0, file "app\services\brokerage\onboarding_templates.py", line 249>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              20 (rollback_checklist)

300           LOAD_NAME                8 (_PLACEHOLDER_BROKERAGE_ID)

299           BUILD_TUPLE              1
              LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA2790, file "app\services\brokerage\onboarding_templates.py", line 299>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object smoke_test_template at 0x0000018C17F0C960, file "app\services\brokerage\onboarding_templates.py", line 299>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              21 (smoke_test_template)

375           LOAD_NAME                8 (_PLACEHOLDER_BROKERAGE_ID)

374           BUILD_TUPLE              1
              LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA2880, file "app\services\brokerage\onboarding_templates.py", line 374>)
              MAKE_FUNCTION
              LOAD_CONST              30 (<code object pilot_expansion_checklist at 0x0000018C1800AD80, file "app\services\brokerage\onboarding_templates.py", line 374>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              22 (pilot_expansion_checklist)

424           BUILD_LIST               0
              LOAD_CONST              31 (('brokerage_onboarding_checklist', 'launch_checklist', 'rollback_checklist', 'smoke_test_template', 'pilot_expansion_checklist'))
              LIST_EXTEND              1
              STORE_NAME              23 (__all__)
              LOAD_CONST              15 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app\services\brokerage\onboarding_templates.py", line 65>:
 65           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _bound_brokerage_id at 0x0000018C17FF0C30, file "app\services\brokerage\onboarding_templates.py", line 65>:
 65           RESUME                   0

 66           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       55 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       33 (to L1)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         0 (value)
              CALL                     1
              LOAD_SMALL_INT         200
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_FALSE       17 (to L1)
              NOT_TAKEN

 67           LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

 68   L1:     LOAD_GLOBAL              8 (_PLACEHOLDER_BROKERAGE_ID)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18090470, file "app\services\brokerage\onboarding_templates.py", line 71>:
 71           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('step_id')

 72           LOAD_CONST               2 ('str')

 71           LOAD_CONST               3 ('title')

 73           LOAD_CONST               2 ('str')

 71           LOAD_CONST               4 ('description')

 74           LOAD_CONST               2 ('str')

 71           LOAD_CONST               5 ('blocking')

 76           LOAD_CONST               6 ('bool')

 71           LOAD_CONST               7 ('artefact')

 77           LOAD_CONST               8 ('Optional[str]')

 71           LOAD_CONST               9 ('operator_action')

 78           LOAD_CONST               8 ('Optional[str]')

 71           LOAD_CONST              10 ('return')

 79           LOAD_CONST              11 ('Dict[str, Any]')

 71           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object _step at 0x0000018C18025230, file "app\services\brokerage\onboarding_templates.py", line 71>:
 71           RESUME                   0

 81           LOAD_CONST               0 ('step_id')
              LOAD_FAST_BORROW         0 (step_id)

 82           LOAD_CONST               1 ('title')
              LOAD_FAST_BORROW         1 (title)

 83           LOAD_CONST               2 ('description')
              LOAD_FAST_BORROW         2 (description)

 84           LOAD_CONST               3 ('blocking')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         3 (blocking)
              CALL                     1

 85           LOAD_CONST               4 ('artefact')
              LOAD_FAST_BORROW         4 (artefact)

 86           LOAD_CONST               5 ('operator_action')
              LOAD_FAST_BORROW         5 (operator_action)

 80           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025330, file "app\services\brokerage\onboarding_templates.py", line 90>:
 90           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('template')

 91           LOAD_CONST               2 ('str')

 90           LOAD_CONST               3 ('brokerage_id')

 92           LOAD_CONST               4 ('Any')

 90           LOAD_CONST               5 ('steps')

 93           LOAD_CONST               6 ('List[Dict[str, Any]]')

 90           LOAD_CONST               7 ('return')

 94           LOAD_CONST               8 ('Dict[str, Any]')

 90           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _envelope at 0x0000018C180531B0, file "app\services\brokerage\onboarding_templates.py", line 90>:
 90           RESUME                   0

 96           LOAD_CONST               0 ('template')
              LOAD_FAST_BORROW         0 (template)

 97           LOAD_CONST               1 ('brokerage_id')
              LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
              LOAD_FAST_BORROW         1 (brokerage_id)
              CALL                     1

 98           LOAD_CONST               2 ('generated_at')
              LOAD_CONST               3 (None)

 99           LOAD_CONST               4 ('steps')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST_BORROW         2 (steps)
              CALL                     1

100           LOAD_CONST               5 ('warnings')
              BUILD_LIST               0

101           LOAD_CONST               6 ('error_code')
              LOAD_CONST               3 (None)

 95           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "app\services\brokerage\onboarding_templates.py", line 109>:
109           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

110           LOAD_CONST               2 ('Any')

109           LOAD_CONST               3 ('return')

111           LOAD_CONST               4 ('Dict[str, Any]')

109           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object brokerage_onboarding_checklist at 0x0000018C17EC4D20, file "app\services\brokerage\onboarding_templates.py", line 109>:
109           RESUME                   0

115           LOAD_GLOBAL              1 (_step + NULL)

116           LOAD_CONST               1 ('onboard.1.profile_created')

117           LOAD_CONST               2 ('Create the operational profile')

118           LOAD_CONST               3 ('Run ensure_profile(brokerage_id=...) so the operator surface has a side-car row for this brokerage. Idempotent.')

119           LOAD_CONST               4 (True)

120           LOAD_CONST               5 ('app/services/brokerage/profile_service.py::ensure_profile')

121           LOAD_CONST               6 ('POST /ops/brokerages (PAS173 route) or call ensure_profile() from a script.')

115           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

123           LOAD_GLOBAL              1 (_step + NULL)

124           LOAD_CONST               8 ('onboard.2.brokerage_row_credentials')

125           LOAD_CONST               9 ('Populate the brokerage row with credentials')

126           LOAD_CONST              10 ('Set twilio_phone, slack_webhook_url, and any alert_slack_webhook_url on the existing brokerages table via PAS admin routes. NEVER paste secrets into Slack / chat / git.')

127           LOAD_CONST               4 (True)

128           LOAD_CONST              11 ('app/routes/admin.py::update_account')

129           LOAD_CONST              12 ('PATCH /admin/brokerages/{id} with the credential fields.')

123           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

131           LOAD_GLOBAL              1 (_step + NULL)

132           LOAD_CONST              13 ('onboard.3.timezone_configured')

133           LOAD_CONST              14 ("Set the brokerage's timezone on the profile")

134           LOAD_CONST              15 ('PAS170 Cal.com timezone resolver reads timezone from the brokerage row first; PAS173 profile mirrors it. Without a timezone, the lead sees the ET fallback.')

135           LOAD_CONST               4 (True)

136           LOAD_CONST              16 ('app/services/booking/calcom_client.py::_resolve_brokerage_timezone')

137           LOAD_CONST              17 ('PATCH operator_brokerages with timezone set.')

131           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

139           LOAD_GLOBAL              1 (_step + NULL)

140           LOAD_CONST              18 ('onboard.4.cal_com_probe')

141           LOAD_CONST              19 ('Verify Cal.com /slots returns 200, not 404')

142           LOAD_CONST              20 ("Per operator checklist §3, curl /v2/slots with the brokerage's eventTypeId. STOP if HTTP 404.")

143           LOAD_CONST               4 (True)

144           LOAD_CONST              21 ('docs/orvn_external_pilot_operator_checklist.md#3')

145           LOAD_CONST              22 ('curl Cal.com /slots; coordinate with brokerage admin if 404.')

139           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

147           LOAD_GLOBAL              1 (_step + NULL)

148           LOAD_CONST              23 ('onboard.5.run_smoke_matrix')

149           LOAD_CONST              24 ('Run the PAS170 smoke matrix against the demo brokerage')

150           LOAD_CONST              25 ("Walk the PAS170 smoke_plan output to verify the engine + survival kit behave correctly with this brokerage's config.")

151           LOAD_CONST               4 (True)

152           LOAD_CONST              26 ('scripts/pas170_demo_brokerage_smoke_plan.py')

153           LOAD_CONST              27 ('python scripts/pas170_demo_brokerage_smoke_plan.py --brokerage-id <id>')

147           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

155           LOAD_GLOBAL              1 (_step + NULL)

156           LOAD_CONST              28 ('onboard.6.mark_configured')

157           LOAD_CONST              29 ('Mark the profile CONFIGURED')

158           LOAD_CONST              30 ('Transition onboarding_status from IN_PROGRESS to CONFIGURED via the operator action.')

159           LOAD_CONST               4 (True)

160           LOAD_CONST              31 ('app/services/operator/operator_actions.py::execute_action')

161           LOAD_CONST              32 ("POST /ops/brokerages/{id}/actions {action:'mark_onboarding_stage', stage:'CONFIGURED'}")

155           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

163           LOAD_GLOBAL              1 (_step + NULL)

164           LOAD_CONST              33 ('onboard.7.run_readiness_gates')

165           LOAD_CONST              34 ('Run the five readiness gates')

166           LOAD_CONST              35 ('PAS169-launch, PAS-LAUNCH-01, PAS170, PAS171, PAS172 must all report verdict=READY before VERIFIED.')

167           LOAD_CONST               4 (True)

168           LOAD_CONST              36 ('scripts/pas171_external_pilot_readiness_check.py')

169           LOAD_CONST              37 ('python scripts/pas17X_*_readiness_check.py --summary-only')

163           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

171           LOAD_GLOBAL              1 (_step + NULL)

172           LOAD_CONST              38 ('onboard.8.mark_verified')

173           LOAD_CONST              39 ('Mark the profile VERIFIED')

174           LOAD_CONST              40 ('Only the operator with audit-trail context (X-Admin-Key + actor_id) can transition the profile to VERIFIED.')

175           LOAD_CONST               4 (True)

176           LOAD_CONST              31 ('app/services/operator/operator_actions.py::execute_action')

177           LOAD_CONST              41 ("POST /ops/brokerages/{id}/actions {action:'mark_onboarding_stage', stage:'VERIFIED'}")

171           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

179           LOAD_GLOBAL              1 (_step + NULL)

180           LOAD_CONST              42 ('onboard.9.go_live')

181           LOAD_CONST              43 ('Transition to LIVE only after the launch checklist passes')

182           LOAD_CONST              44 ('Run launch_checklist() and walk all blocking steps before transitioning onboarding_status to LIVE.')

183           LOAD_CONST               4 (True)

184           LOAD_CONST              45 ('app/services/brokerage/onboarding_templates.py::launch_checklist')

185           LOAD_CONST              46 ("POST /ops/brokerages/{id}/actions {action:'mark_onboarding_stage', stage:'LIVE'}")

179           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

114           BUILD_LIST               9
              STORE_FAST               1 (steps)

188           LOAD_GLOBAL              3 (_envelope + NULL)
              LOAD_CONST              47 ('brokerage_onboarding_checklist')
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage_id, steps)
              CALL                     3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "app\services\brokerage\onboarding_templates.py", line 191>:
191           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

192           LOAD_CONST               2 ('Any')

191           LOAD_CONST               3 ('return')

193           LOAD_CONST               4 ('Dict[str, Any]')

191           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object launch_checklist at 0x0000018C180606F0, file "app\services\brokerage\onboarding_templates.py", line 191>:
191           RESUME                   0

197           LOAD_GLOBAL              1 (_step + NULL)

198           LOAD_CONST               1 ('launch.1.readiness_gates_green')

199           LOAD_CONST               2 ('All readiness gates GREEN')

200           LOAD_CONST               3 ('Re-run the five readiness gates. Any NOT_READY blocks launch.')

201           LOAD_CONST               4 (True)

202           LOAD_CONST               5 ('scripts/pas172_pilot_operations_readiness_check.py')

203           LOAD_CONST               6 ('python scripts/pas172_pilot_operations_readiness_check.py --summary-only')

197           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

205           LOAD_GLOBAL              1 (_step + NULL)

206           LOAD_CONST               8 ('launch.2.heartbeat_wired')

207           LOAD_CONST               9 ('Worker heartbeat wired (if worker enabled)')

208           LOAD_CONST              10 ('If the operator plans to enable the PAS162 worker, the heartbeat helpers must be wired into the run script per orvn_pilot_ops_runbook.md §3.')

209           LOAD_CONST              11 (False)

210           LOAD_CONST              12 ('docs/orvn_pilot_ops_runbook.md#3')

211           LOAD_CONST              13 ('Edit run_pending_calls_worker.py wrapper.')

205           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

213           LOAD_GLOBAL              1 (_step + NULL)

214           LOAD_CONST              14 ('launch.3.alert_channel_configured')

215           LOAD_CONST              15 ('PAS_ALERT_SLACK_WEBHOOK_URL set')

216           LOAD_CONST              16 ('Required for outbound pilot alerts. Operator MUST set this on the deployment host.')

217           LOAD_CONST               4 (True)

218           LOAD_CONST              17 ('docs/orvn_external_pilot_operator_checklist.md#4')

219           LOAD_CONST              18 ('Export PAS_ALERT_SLACK_WEBHOOK_URL; restart the FastAPI deployment.')

213           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

221           LOAD_GLOBAL              1 (_step + NULL)

222           LOAD_CONST              19 ('launch.4.durable_stores_promoted')

223           LOAD_CONST              20 ('v15 / v16 / v18 / v19 / v20 migrations promoted')

224           LOAD_CONST              21 ('Durable backing for email dedupe / encryption / pending-call dedupe / callback schedule / worker heartbeats must be live OR the operator must accept the documented fallback posture.')

225           LOAD_CONST              11 (False)

226           LOAD_CONST              22 ('docs/orvn_external_pilot_operator_checklist.md#2')

227           LOAD_CONST              23 ('Promote SQL via the Supabase SQL editor.')

221           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

229           LOAD_GLOBAL              1 (_step + NULL)

230           LOAD_CONST              24 ('launch.5.first_30min_worker_off')

231           LOAD_CONST              25 ('Open external traffic with worker OFF for 30 min')

232           LOAD_CONST              26 ('Lets the dedupe + callback stores observe inbound shape before any Twilio dial fires.')

233           LOAD_CONST               4 (True)

234           LOAD_CONST              27 ('docs/orvn_external_pilot_operator_checklist.md#5')

235           LOAD_CONST              28 ('Leave PENDING_CALLS_WORKER_ENABLED unset; observe ops route for 30 min.')

229           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

237           LOAD_GLOBAL              1 (_step + NULL)

238           LOAD_CONST              29 ('launch.6.enable_worker')

239           LOAD_CONST              30 ('Enable the worker explicitly')

240           LOAD_CONST              31 ("Only the literal env value 'true' enables the PAS162 worker. Then run scripts/run_pending_calls_worker.py.")

241           LOAD_CONST              11 (False)

242           LOAD_CONST              32 ('docs/orvn_pilot_ops_runbook.md#5')

243           LOAD_CONST              33 ('PENDING_CALLS_WORKER_ENABLED=true python scripts/run_pending_calls_worker.py')

237           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

196           BUILD_LIST               6
              STORE_FAST               1 (steps)

246           LOAD_GLOBAL              3 (_envelope + NULL)
              LOAD_CONST              34 ('launch_checklist')
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage_id, steps)
              CALL                     3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "app\services\brokerage\onboarding_templates.py", line 249>:
249           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

250           LOAD_CONST               2 ('Any')

249           LOAD_CONST               3 ('return')

251           LOAD_CONST               4 ('Dict[str, Any]')

249           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object rollback_checklist at 0x0000018C1800ABF0, file "app\services\brokerage\onboarding_templates.py", line 249>:
249           RESUME                   0

255           LOAD_GLOBAL              1 (_step + NULL)

256           LOAD_CONST               1 ('rollback.1.stop_worker')

257           LOAD_CONST               2 ('Stop the PAS162 worker')

258           LOAD_CONST               3 ('Send SIGTERM to scripts/run_pending_calls_worker.py and unset PENDING_CALLS_WORKER_ENABLED. No outbound dial fires while the worker is OFF.')

259           LOAD_CONST               4 (True)

260           LOAD_CONST               5 ('docs/orvn_pilot_ops_runbook.md#5')

261           LOAD_CONST               6 ('SIGTERM the worker; unset env var.')

255           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

263           LOAD_GLOBAL              1 (_step + NULL)

264           LOAD_CONST               8 ('rollback.2.pause_brokerage')

265           LOAD_CONST               9 ('Pause the brokerage profile')

266           LOAD_CONST              10 ('Transition onboarding_status to PAUSED so the operator dashboard reflects the rollback.')

267           LOAD_CONST               4 (True)

268           LOAD_CONST              11 ('app/services/operator/operator_actions.py::execute_action')

269           LOAD_CONST              12 ("POST /ops/brokerages/{id}/actions {action:'pause_brokerage'}")

263           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

271           LOAD_GLOBAL              1 (_step + NULL)

272           LOAD_CONST              13 ('rollback.3.disable_durable_stores')

273           LOAD_CONST              14 ('Drop to PAS170 process-local fallback (optional)')

274           LOAD_CONST              15 ('If the durable Supabase tables are part of the incident, export PAS_PENDING_CALL_DEDUPE_DURABLE_ENABLED=false and PAS_CALLBACK_SCHEDULE_DURABLE_ENABLED=false and restart.')

275           LOAD_CONST              16 (False)

276           LOAD_CONST              17 ('docs/orvn_external_pilot_operator_checklist.md#8.5')

277           LOAD_CONST              18 ('Export the env flags; restart the FastAPI deployment.')

271           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

279           LOAD_GLOBAL              1 (_step + NULL)

280           LOAD_CONST              19 ('rollback.4.disable_pilot_slack')

281           LOAD_CONST              20 ('Disable pilot Slack alerts (optional)')

282           LOAD_CONST              21 ('unset PAS_ALERT_SLACK_WEBHOOK_URL if the alert channel is part of the incident. PAS171 transport collapses to skipped envelope.')

283           LOAD_CONST              16 (False)

284           LOAD_CONST              22 ('docs/orvn_external_pilot_operator_checklist.md#8.4')

285           LOAD_CONST              23 ('unset PAS_ALERT_SLACK_WEBHOOK_URL; restart the FastAPI deployment.')

279           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

287           LOAD_GLOBAL              1 (_step + NULL)

288           LOAD_CONST              24 ('rollback.5.capture_post_mortem')

289           LOAD_CONST              25 ('Capture queue + heartbeat snapshots')

290           LOAD_CONST              26 ('Pull /ops/pending-calls/queue and /ops/workers/status snapshots for the post-mortem file.')

291           LOAD_CONST               4 (True)

292           LOAD_CONST              27 ('docs/orvn_pilot_ops_runbook.md#9')

293           LOAD_CONST              28 ('curl /ops/* with X-Admin-Key; save JSON.')

287           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

254           BUILD_LIST               5
              STORE_FAST               1 (steps)

296           LOAD_GLOBAL              3 (_envelope + NULL)
              LOAD_CONST              29 ('rollback_checklist')
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage_id, steps)
              CALL                     3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2790, file "app\services\brokerage\onboarding_templates.py", line 299>:
299           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

300           LOAD_CONST               2 ('Any')

299           LOAD_CONST               3 ('return')

301           LOAD_CONST               4 ('Dict[str, Any]')

299           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object smoke_test_template at 0x0000018C17F0C960, file "app\services\brokerage\onboarding_templates.py", line 299>:
299           RESUME                   0

307           LOAD_GLOBAL              1 (_step + NULL)

308           LOAD_CONST               1 ('smoke.1.parse_admin')

309           LOAD_CONST               2 ('Email parse — admin-only')

310           LOAD_CONST               3 ('POST /email-ingestion/parse with X-Admin-Key. Expect call_eligible boolean + structural envelope; NO phone/email/name in the response.')

311           LOAD_CONST               4 (True)

312           LOAD_CONST               5 ('app/routes/email_ingestion.py')

314           LOAD_CONST               6 ('curl -X POST ')
              LOAD_GLOBAL              2 (_PLACEHOLDER_HOST)
              FORMAT_SIMPLE
              LOAD_CONST               7 ("/email-ingestion/parse -H 'X-Admin-Key: ")

315           LOAD_GLOBAL              4 (_PLACEHOLDER_ADMIN_KEY)
              FORMAT_SIMPLE
              LOAD_CONST               8 ('\' -d \'{"subject":"smoke","sender":"')

316           LOAD_GLOBAL              6 (_SANITISED_EMAIL)
              FORMAT_SIMPLE
              LOAD_CONST               9 ('","body":"Name: ')

317           LOAD_GLOBAL              8 (_SANITISED_NAME)
              FORMAT_SIMPLE
              LOAD_CONST              10 ('; Phone: ')
              LOAD_GLOBAL             10 (_SANITISED_PHONE)
              FORMAT_SIMPLE
              LOAD_CONST              11 ('"}\'')

314           BUILD_STRING            11

307           LOAD_CONST              12 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

320           LOAD_GLOBAL              1 (_step + NULL)

321           LOAD_CONST              13 ('smoke.2.ingest_first_submission')

322           LOAD_CONST              14 ('First email ingest')

323           LOAD_CONST              15 ('POST /email-ingestion/ingest with the brokerage X-API-Key. Expect status=accepted, duplicate=False.')

324           LOAD_CONST               4 (True)

325           LOAD_CONST               5 ('app/routes/email_ingestion.py')

327           LOAD_CONST               6 ('curl -X POST ')
              LOAD_GLOBAL              2 (_PLACEHOLDER_HOST)
              FORMAT_SIMPLE
              LOAD_CONST              16 ("/email-ingestion/ingest -H 'X-API-Key: ")

328           LOAD_GLOBAL             12 (_PLACEHOLDER_API_KEY)
              FORMAT_SIMPLE
              LOAD_CONST              17 ("' -d '{...same body...}'")

327           BUILD_STRING             5

320           LOAD_CONST              12 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

332           LOAD_GLOBAL              1 (_step + NULL)

333           LOAD_CONST              18 ('smoke.3.ingest_duplicate')

334           LOAD_CONST              19 ('Duplicate email ingest')

335           LOAD_CONST              20 ('Re-run smoke.2 with the same body. Expect status=duplicate.')

336           LOAD_CONST               4 (True)

337           LOAD_CONST              21 ('app/services/ingestion/pending_call_dedupe.py')

338           LOAD_CONST              22 ('Re-run smoke.2 verbatim.')

332           LOAD_CONST              12 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

340           LOAD_GLOBAL              1 (_step + NULL)

341           LOAD_CONST              23 ('smoke.4.queue_status')

342           LOAD_CONST              24 ('Queue status via ops route')

343           LOAD_CONST              25 ('GET /ops/pending-calls/queue?brokerage_id=<id>. Expect status=ok + structural counts.')

344           LOAD_CONST               4 (True)

345           LOAD_CONST              26 ('app/routes/operator_ops.py')

347           LOAD_CONST              27 ("curl -H 'X-Admin-Key: ")
              LOAD_GLOBAL              4 (_PLACEHOLDER_ADMIN_KEY)
              FORMAT_SIMPLE
              LOAD_CONST              28 ("' ")

348           LOAD_GLOBAL              2 (_PLACEHOLDER_HOST)
              FORMAT_SIMPLE
              LOAD_CONST              29 ('/ops/pending-calls/queue?brokerage_id=<id>')

347           BUILD_STRING             5

340           LOAD_CONST              12 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

351           LOAD_GLOBAL              1 (_step + NULL)

352           LOAD_CONST              30 ('smoke.5.worker_status')

353           LOAD_CONST              31 ('Worker status via ops route')

354           LOAD_CONST              32 ('GET /ops/workers/status. Expect status=ok + stale.stale_count=0 (if the worker is wired in).')

355           LOAD_CONST              33 (False)

356           LOAD_CONST              26 ('app/routes/operator_ops.py')

358           LOAD_CONST              27 ("curl -H 'X-Admin-Key: ")
              LOAD_GLOBAL              4 (_PLACEHOLDER_ADMIN_KEY)
              FORMAT_SIMPLE
              LOAD_CONST              28 ("' ")

359           LOAD_GLOBAL              2 (_PLACEHOLDER_HOST)
              FORMAT_SIMPLE
              LOAD_CONST              34 ('/ops/workers/status')

358           BUILD_STRING             5

351           LOAD_CONST              12 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

362           LOAD_GLOBAL              1 (_step + NULL)

363           LOAD_CONST              35 ('smoke.6.callback_round_trip')

364           LOAD_CONST              36 ('Callback schedule round trip')

365           LOAD_CONST              37 ('Schedule + list + reminder report via the PAS170 surface or the ops route. Expect zero PII in the envelope.')

366           LOAD_CONST               4 (True)

367           LOAD_CONST              38 ('app/services/callbacks/callback_schedule.py')

368           LOAD_CONST              39 ("POST /ops/brokerages/{id}/actions {action:'run_readiness_snapshot'}")

362           LOAD_CONST              12 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

306           BUILD_LIST               6
              STORE_FAST               1 (steps)

371           LOAD_GLOBAL             15 (_envelope + NULL)
              LOAD_CONST              40 ('smoke_test_template')
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage_id, steps)
              CALL                     3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app\services\brokerage\onboarding_templates.py", line 374>:
374           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

375           LOAD_CONST               2 ('Any')

374           LOAD_CONST               3 ('return')

376           LOAD_CONST               4 ('Dict[str, Any]')

374           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object pilot_expansion_checklist at 0x0000018C1800AD80, file "app\services\brokerage\onboarding_templates.py", line 374>:
374           RESUME                   0

380           LOAD_GLOBAL              1 (_step + NULL)

381           LOAD_CONST               1 ('expand.1.single_pilot_clean_14_days')

382           LOAD_CONST               2 ('First pilot stable for ≥14 days')

383           LOAD_CONST               3 ('TRUSTED_PILOT must show zero unresolved P0/P1 incidents and zero unresolved fallback-notice events for 14 consecutive days.')

384           LOAD_CONST               4 (True)

385           LOAD_CONST               5 ('docs/pas172_pilot_operations_control_layer.md')

386           LOAD_CONST               6 ('Manual review of /ops/* + alert channel history.')

380           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

388           LOAD_GLOBAL              1 (_step + NULL)

389           LOAD_CONST               8 ('expand.2.durable_heartbeat_promoted')

390           LOAD_CONST               9 ('v20 worker_heartbeats promoted')

391           LOAD_CONST              10 ('Cannot run more than one external brokerage without a durable heartbeat source-of-truth.')

392           LOAD_CONST               4 (True)

393           LOAD_CONST              11 ('scripts/migrate_v20_worker_heartbeats.sql')

394           LOAD_CONST              12 ('Promote v20 SQL via the Supabase SQL editor.')

388           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

396           LOAD_GLOBAL              1 (_step + NULL)

397           LOAD_CONST              13 ('expand.3.reapers_scheduled_manually')

398           LOAD_CONST              14 ('Reaper cadence documented')

399           LOAD_CONST              15 ('Operator commits to running reap_pending_call_dedupe.py daily + reap_callback_schedule.py weekly per orvn_pilot_ops_runbook.md §4.')

400           LOAD_CONST               4 (True)

401           LOAD_CONST              16 ('docs/orvn_pilot_ops_runbook.md#4')

402           LOAD_CONST              17 ('Document the cadence in the team runbook.')

396           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

404           LOAD_GLOBAL              1 (_step + NULL)

405           LOAD_CONST              18 ('expand.4.profile_pilot_stage')

406           LOAD_CONST              19 ('Profile pilot_stage transitions to EXPANDED_PILOT')

407           LOAD_CONST              20 ('Operator action mark_pilot_stage records the transition with actor_id for audit trail.')

408           LOAD_CONST               4 (True)

409           LOAD_CONST              21 ('app/services/operator/operator_actions.py')

410           LOAD_CONST              22 ("POST /ops/brokerages/{id}/actions {action:'mark_pilot_stage', stage:'EXPANDED_PILOT'}")

404           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

412           LOAD_GLOBAL              1 (_step + NULL)

413           LOAD_CONST              23 ('expand.5.second_brokerage_onboarding')

414           LOAD_CONST              24 ('Second brokerage onboarded via the same checklist')

415           LOAD_CONST              25 ('Walk brokerage_onboarding_checklist() for the second brokerage. The checklist must be identical step-by-step — same audit trail shape.')

416           LOAD_CONST               4 (True)

417           LOAD_CONST              26 ('app/services/brokerage/onboarding_templates.py::brokerage_onboarding_checklist')

418           LOAD_CONST              27 ('Run brokerage_onboarding_checklist() and follow.')

412           LOAD_CONST               7 (('blocking', 'artefact', 'operator_action'))
              CALL_KW                  6

379           BUILD_LIST               5
              STORE_FAST               1 (steps)

421           LOAD_GLOBAL              3 (_envelope + NULL)
              LOAD_CONST              28 ('pilot_expansion_checklist')
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage_id, steps)
              CALL                     3
              RETURN_VALUE
```
