# scripts_readiness/pas170_demo_brokerage_smoke_plan

- **pyc:** `scripts\__pycache__\pas170_demo_brokerage_smoke_plan.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas170_demo_brokerage_smoke_plan.py`
- **co_filename (from bytecode):** `scripts\pas170_demo_brokerage_smoke_plan.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS170 — Demo brokerage smoke plan generator.

Operator-runnable helper that prints the structural smoke-test
matrix an operator should walk through against a real internal
demo brokerage BEFORE inviting external pilot traffic. The
script is read-only — it never opens a network connection,
never reads ``.env``, never writes to the DB. Its job is to
produce the curl placeholders + a checklist the operator can
copy into a runbook.

Doctrine:

* **Structural only.** Sample emails / phones / names in the
  output are sanitised placeholders ("Smoke Test" / "(555)
  555-0100" / "smoke@example.com"). The script NEVER reads
  real brokerage data.
* **No production data mutation.** The script does not POST
  anything. It prints command placeholders the operator runs
  by hand.
* **Worker stays OFF.** The smoke plan deliberately does NOT
  start the pending-call worker. The operator may start it
  separately under PAS162 doctrine.
* **No PII** anywhere in the smoke plan output.

Usage:
  python scripts/pas170_demo_brokerage_smoke_plan.py
  python scripts/pas170_demo_brokerage_smoke_plan.py --json
  python scripts/pas170_demo_brokerage_smoke_plan.py --brokerage-id brk-demo
  python scripts/pas170_demo_brokerage_smoke_plan.py --host https://pas.example

Exit codes:
    0  — plan rendered successfully
    2  — bad CLI arguments
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `argparse`, `datetime`, `json`, `os`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_acceptance_criteria`, `_build_chaos_scenarios`, `_build_parser`, `_build_smoke_matrix`, `_now_iso`, `_print_plan`, `main`

## Env-key candidates

`PAS170`

## String constants (redacted where noted)

- '\nPAS170 — Demo brokerage smoke plan generator.\n\nOperator-runnable helper that prints the structural smoke-test\nmatrix an operator should walk through against a real internal\ndemo brokerage BEFORE inviting external pilot traffic. The\nscript is read-only — it never opens a network connection,\nnever reads ``.env``, never writes to the DB. Its job is to\nproduce the curl placeholders + a checklist the operator can\ncopy into a runbook.\n\nDoctrine:\n\n* **Structural only.** Sample emails / phones / names in the\n  output are sanitised placeholders ("Smoke Test" / "(555)\n  555-0100" / "smoke@example.com"). The script NEVER reads\n  real brokerage data.\n* **No production data mutation.** The script does not POST\n  anything. It prints command placeholders the operator runs\n  by hand.\n* **Worker stays OFF.** The smoke plan deliberately does NOT\n  start the pending-call worker. The operator may start it\n  separately under PAS162 doctrine.\n* **No PII** anywhere in the smoke plan output.\n\nUsage:\n  python scripts/pas170_demo_brokerage_smoke_plan.py\n  python scripts/pas170_demo_brokerage_smoke_plan.py --json\n  python scripts/pas170_demo_brokerage_smoke_plan.py --brokerage-id brk-demo\n  python scripts/pas170_demo_brokerage_smoke_plan.py --host https://pas.example\n\nExit codes:\n    0  — plan rendered successfully\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'https://<HOST>'
- '<ADMIN_KEY>'
- '<BROKERAGE_KEY>'
- 'brk-demo'
- '(555) 555-0100'
- 'Smoke Test'
- 'smoke@example.com'
- 'return'
- 'str'
- 'seconds'
- 'host'
- 'brokerage_id'
- 'List[Dict[str, Any]]'
- 'Return the structural smoke-test entries. Each entry\nis a closed dict containing the test id, what it covers,\nthe curl placeholder, and the structural expectation.\nNEVER includes real PII.'
- 'You have a new lead from Zillow Premier Agent.\\n\\nName: '
- '\\nPhone: '
- '\\nEmail: '
- '\\nProperty: 1 Test Way, Springfield, IL\\n'
- 'A visitor submitted the contact form on your website.\\n\\nName:    '
- '\\nEmail:   '
- '\\nMessage: Smoke test — no phone supplied.'
- 'smoke_a_parse_admin'
- 'covers'
- 'PAS164 /parse admin-only diagnostic'
- 'curl'
- 'curl -sX POST "'
- '/email-ingestion/parse" -H "X-Admin-Key: '
- '" -H "Content-Type: application/json" -d \'{"subject":"New Lead from Zillow","sender":"no-reply@premieragent.zillow.com","body":"'
- '"}\''
- 'expect'
- 'http'
- 'status'
- 'fields_present'
- 'call_eligible'
- 'fields_absent'
- 'smoke_b_ingest_first'
- 'PAS164 /ingest brokerage auth (first submission)'
- '/email-ingestion/ingest" -H "X-API-Key: '
- 'accepted'
- 'duplicate'
- 'smoke_c_ingest_duplicate'
- 'PAS165/PAS166 email dedupe + PAS170 pending-call dedupe (re-submit identical body)'
- '# Re-run smoke_b_ingest_first VERBATIM with the same body.'
- 'pending_call_id'
- 'call_queued'
- 'smoke_d_email_only_contact'
- 'PAS164 call_eligible=False path (email-only contact)'
- '" -H "Content-Type: application/json" -d \'{"subject":"New website inquiry","sender":"contact-form@brokerage.example","body":"'
- 'warnings_include'
- 'email_lead_missing_phone'
- 'smoke_e_queue_status'
- 'PAS170 queue status report (read-only)'
- 'command'
- 'python -c \'from app.services.ingestion.pending_call_recovery import queue_status_report; import json; print(json.dumps(queue_status_report(brokerage_id="'
- '"), indent=2))\''
- 'smoke_f_stale_detect_dry'
- 'PAS170 stale-DIALING detection (dry-run only)'
- 'python -c \'from app.services.ingestion.pending_call_recovery import detect_stale_dialing_rows; import json; print(json.dumps(detect_stale_dialing_rows(brokerage_id="'
- 'smoke_g_callback_schedule'
- 'PAS170 callback schedule round-trip (in-process)'
- 'python -c \'from app.services.callbacks.callback_schedule import schedule_callback, list_pending_callbacks, reset_callback_registry_for_tests, reminder_report; import json; reset_callback_registry_for_tests(); r = schedule_callback(brokerage_id="'
- '", source_call_id="call-smoke", scheduled_for="2026-01-01T15:00:00+00:00"); print(json.dumps(r, indent=2)); print(json.dumps(list_pending_callbacks("'
- '"), indent=2)); print(json.dumps(reminder_report("'
- 'smoke_h_slack_alert_optional'
- 'PAS170 Slack alert transport (skip when unconfigured)'
- 'python -c \'from app.services.monitoring.slack_alert_transport import send_alert_to_slack; import json; print(json.dumps(send_alert_to_slack({"id":"smoke", "category":"info", "severity":"info", "title":"smoke", "description":"smoke"}), indent=2))\''
- 'status_when_not_configured'
- 'skipped'
- 'slack_webhook_not_configured'
- 'smoke_i_worker_off'
- 'PAS162 worker is OFF (no Twilio dial)'
- "python -c 'from app.services.ingestion.worker import pending_calls_worker_enabled; print(pending_calls_worker_enabled())'"
- 'stdout_contains'
- 'False'
- 'operator_note'
- 'Worker remains OFF by default. Operator may explicitly start it with PENDING_CALLS_WORKER_ENABLED=true python scripts/run_pending_calls_worker.py after smoke tests pass.'
- 'chaos_a_worker_kill_mid_dial'
- 'PAS170 stale DIALING detection + recovery'
- 'steps'
- 'expect_event_types'
- 'pending_call.stale_detected'
- 'pending_call.recovered'
- 'chaos_b_duplicate_webhook'
- 'PAS170 per-brokerage pending-call dedupe'
- 'pending_call.duplicate_suppressed'
- 'chaos_c_decrypt_storm'
- 'PAS167/PAS168 decrypt failure + Slack alert transport'
- 'email.forwarder.secret.decrypt_failed'
- 'alert.slack.sent'
- 'chaos_d_calcom_timezone_pin'
- 'PAS170 Cal.com timezone hotfix'
- "Set the demo brokerage row's timezone field to a non-Eastern zone (e.g. America/Los_Angeles)."
- "Trigger a booking via /simulate-call and verify the Cal.com payload's timeZone matches the brokerage row, not the America/New_York fallback."
- 'List[str]'
- 'All smoke entries report status=ok / status=accepted / status=duplicate / status=skipped per their expectation.'
- 'argparse.ArgumentParser'
- 'pas170_demo_brokerage_smoke_plan'
- 'PAS170 — Render the structural smoke-test plan an operator should run against an internal demo brokerage before opening pilot traffic. NEVER writes anywhere; NEVER reads .env; NEVER touches production data. Sample lead values in the output are sanitised placeholders.'
- '--host'
- 'Base URL to embed in curl placeholders.'
- '--brokerage-id'
- 'Demo brokerage identifier (placeholder only).'
- '--json'
- 'store_true'
- 'Emit the plan as a single JSON document.'
- 'plan'
- 'Dict[str, Any]'
- 'None'
- '[PAS170-smoke-plan] generated_at='
- 'generated_at'
- '[PAS170-smoke-plan] host='
- '[PAS170-smoke-plan] brokerage_id='
- '=== SMOKE MATRIX ==='
- 'smoke_matrix'
- '  $ '
- '  expect: '
- '=== CHAOS SCENARIOS ==='
- 'chaos_scenarios'
- '  expect_event_types: '
- '=== ACCEPTANCE CRITERIA ==='
- 'acceptance_criteria'
- 'argv'
- 'Optional[List[str]]'
- 'int'
- 'phase'
- 'PAS170'

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ('\nPAS170 — Demo brokerage smoke plan generator.\n\nOperator-runnable helper that prints the structural smoke-test\nmatrix an operator should walk through against a real internal\ndemo brokerage BEFORE inviting external pilot traffic. The\nscript is read-only — it never opens a network connection,\nnever reads ``.env``, never writes to the DB. Its job is to\nproduce the curl placeholders + a checklist the operator can\ncopy into a runbook.\n\nDoctrine:\n\n* **Structural only.** Sample emails / phones / names in the\n  output are sanitised placeholders ("Smoke Test" / "(555)\n  555-0100" / "smoke@example.com"). The script NEVER reads\n  real brokerage data.\n* **No production data mutation.** The script does not POST\n  anything. It prints command placeholders the operator runs\n  by hand.\n* **Worker stays OFF.** The smoke plan deliberately does NOT\n  start the pending-call worker. The operator may start it\n  separately under PAS162 doctrine.\n* **No PII** anywhere in the smoke plan output.\n\nUsage:\n  python scripts/pas170_demo_brokerage_smoke_plan.py\n  python scripts/pas170_demo_brokerage_smoke_plan.py --json\n  python scripts/pas170_demo_brokerage_smoke_plan.py --brokerage-id brk-demo\n  python scripts/pas170_demo_brokerage_smoke_plan.py --host https://pas.example\n\nExit codes:\n    0  — plan rendered successfully\n    2  — bad CLI arguments\n')
               STORE_NAME               0 (__doc__)

  37           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  39           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  40           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  41           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  42           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  43           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  44           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
               IMPORT_NAME              9 (typing)
               IMPORT_FROM             10 (Any)
               STORE_NAME              10 (Any)
               IMPORT_FROM             11 (Dict)
               STORE_NAME              11 (Dict)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  47           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  48           NOP

  49   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               5 ('utf-8')
               LOAD_CONST               6 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  47   L4:     END_FOR
               POP_ITER

  56           LOAD_CONST               7 ('https://<HOST>')
               STORE_NAME              19 (_PLACEHOLDER_HOST)

  57           LOAD_CONST               8 ('<ADMIN_KEY>')
               STORE_NAME              20 (_PLACEHOLDER_ADMIN_KEY)

  58           LOAD_CONST               9 ('<BROKERAGE_KEY>')
               STORE_NAME              21 (_PLACEHOLDER_BROKERAGE_KEY)

  59           LOAD_CONST              10 ('brk-demo')
               STORE_NAME              22 (_PLACEHOLDER_BROKERAGE_ID)

  61           LOAD_CONST              11 ('(555) 555-0100')
               STORE_NAME              23 (_SANITISED_PHONE)

  62           LOAD_CONST              12 ('Smoke Test')
               STORE_NAME              24 (_SANITISED_NAME)

  63           LOAD_CONST              13 ('smoke@example.com')
               STORE_NAME              25 (_SANITISED_EMAIL)

  66           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA34B0, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 66>)
               MAKE_FUNCTION
               LOAD_CONST              15 (<code object _now_iso at 0x0000018C18038170, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 66>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              26 (_now_iso)

  74           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18025D30, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 74>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _build_smoke_matrix at 0x0000018C17D4CB40, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 74>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              27 (_build_smoke_matrix)

 293           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 293>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _build_chaos_scenarios at 0x0000018C18038670, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 293>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (_build_chaos_scenarios)

 376           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 376>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _build_acceptance_criteria at 0x0000018C18069370, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 376>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              29 (_build_acceptance_criteria)

 392           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 392>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _build_parser at 0x0000018C1800B230, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 392>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              30 (_build_parser)

 419           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 419>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object _print_plan at 0x0000018C17ED9FB0, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 419>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_print_plan)

 449           LOAD_CONST              29 ((None,))
               LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 449>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object main at 0x0000018C17D4B040, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 449>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              32 (main)

 476           LOAD_NAME               33 (__name__)
               LOAD_CONST              28 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 477           LOAD_NAME                6 (sys)
               LOAD_ATTR               68 (exit)
               PUSH_NULL
               LOAD_NAME               32 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 476   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  50           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

  51   L7:     POP_EXCEPT
               JUMP_BACKWARD          128 (to L1)

  50   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 66>:
 66           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _now_iso at 0x0000018C18038170, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 66>:
 66           RESUME                   0

 67           LOAD_GLOBAL              0 (datetime)
              LOAD_ATTR                2 (now)
              PUSH_NULL
              LOAD_GLOBAL              4 (timezone)
              LOAD_ATTR                6 (utc)
              CALL                     1
              LOAD_ATTR                9 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 74>:
 74           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('host')

 76           LOAD_CONST               2 ('str')

 74           LOAD_CONST               3 ('brokerage_id')

 77           LOAD_CONST               2 ('str')

 74           LOAD_CONST               4 ('return')

 78           LOAD_CONST               5 ('List[Dict[str, Any]]')

 74           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _build_smoke_matrix at 0x0000018C17D4CB40, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 74>:
 74           RESUME                   0

 84           LOAD_CONST               1 ('You have a new lead from Zillow Premier Agent.\\n\\nName: ')

 85           LOAD_GLOBAL              0 (_SANITISED_NAME)
              FORMAT_SIMPLE
              LOAD_CONST               2 ('\\nPhone: ')

 86           LOAD_GLOBAL              2 (_SANITISED_PHONE)
              FORMAT_SIMPLE
              LOAD_CONST               3 ('\\nEmail: ')

 87           LOAD_GLOBAL              4 (_SANITISED_EMAIL)
              FORMAT_SIMPLE
              LOAD_CONST               4 ('\\nProperty: 1 Test Way, Springfield, IL\\n')

 84           BUILD_STRING             7

 83           STORE_FAST               2 (base_zillow_body)

 91           LOAD_CONST               5 ('A visitor submitted the contact form on your website.\\n\\nName:    ')

 92           LOAD_GLOBAL              0 (_SANITISED_NAME)
              FORMAT_SIMPLE
              LOAD_CONST               6 ('\\nEmail:   ')

 93           LOAD_GLOBAL              4 (_SANITISED_EMAIL)
              FORMAT_SIMPLE
              LOAD_CONST               7 ('\\nMessage: Smoke test — no phone supplied.')

 91           BUILD_STRING             5

 90           STORE_FAST               3 (base_website_body)

 98           LOAD_CONST               8 ('id')
              LOAD_CONST               9 ('smoke_a_parse_admin')

 99           LOAD_CONST              10 ('covers')
              LOAD_CONST              11 ('PAS164 /parse admin-only diagnostic')

100           LOAD_CONST              12 ('curl')

101           LOAD_CONST              13 ('curl -sX POST "')
              LOAD_FAST_BORROW         0 (host)
              FORMAT_SIMPLE
              LOAD_CONST              14 ('/email-ingestion/parse" -H "X-Admin-Key: ')

102           LOAD_GLOBAL              6 (_PLACEHOLDER_ADMIN_KEY)
              FORMAT_SIMPLE
              LOAD_CONST              15 ('" -H "Content-Type: application/json" -d \'{"subject":"New Lead from Zillow","sender":"no-reply@premieragent.zillow.com","body":"')

106           LOAD_FAST_BORROW         2 (base_zillow_body)
              FORMAT_SIMPLE
              LOAD_CONST              16 ('"}\'')

101           BUILD_STRING             7

108           LOAD_CONST              17 ('expect')

109           LOAD_CONST              18 ('http')
              LOAD_SMALL_INT         200

110           LOAD_CONST              19 ('status')
              LOAD_CONST              20 ('ok')

111           LOAD_CONST              21 ('fields_present')
              BUILD_LIST               0
              LOAD_CONST              68 (('status', 'source', 'call_eligible', 'has_phone', 'has_email', 'warnings', 'errors'))
              LIST_EXTEND              1

115           LOAD_CONST              23 ('fields_absent')
              BUILD_LIST               0
              LOAD_CONST              69 (('phone', 'email', 'name', 'property_address', 'subject', 'sender', 'body', 'notes', 'transcript', 'raw_email', 'raw_body', 'signature', 'dedupe_key', 'secret'))
              LIST_EXTEND              1

108           BUILD_MAP                4

 97           BUILD_MAP                4

124           LOAD_CONST               8 ('id')
              LOAD_CONST              24 ('smoke_b_ingest_first')

125           LOAD_CONST              10 ('covers')
              LOAD_CONST              25 ('PAS164 /ingest brokerage auth (first submission)')

126           LOAD_CONST              12 ('curl')

127           LOAD_CONST              13 ('curl -sX POST "')
              LOAD_FAST_BORROW         0 (host)
              FORMAT_SIMPLE
              LOAD_CONST              26 ('/email-ingestion/ingest" -H "X-API-Key: ')

128           LOAD_GLOBAL              8 (_PLACEHOLDER_BROKERAGE_KEY)
              FORMAT_SIMPLE
              LOAD_CONST              15 ('" -H "Content-Type: application/json" -d \'{"subject":"New Lead from Zillow","sender":"no-reply@premieragent.zillow.com","body":"')

132           LOAD_FAST_BORROW         2 (base_zillow_body)
              FORMAT_SIMPLE
              LOAD_CONST              16 ('"}\'')

127           BUILD_STRING             7

134           LOAD_CONST              17 ('expect')

135           LOAD_CONST              18 ('http')
              LOAD_SMALL_INT         200

136           LOAD_CONST              19 ('status')
              LOAD_CONST              27 ('accepted')

137           LOAD_CONST              28 ('duplicate')
              LOAD_CONST              29 (False)

138           LOAD_CONST              22 ('call_eligible')
              LOAD_CONST              30 (True)

139           LOAD_CONST              23 ('fields_absent')
              BUILD_LIST               0
              LOAD_CONST              70 (('phone', 'email', 'name', 'subject', 'sender', 'body', 'notes', 'raw_email', 'raw_body', 'signature', 'dedupe_key', 'secret'))
              LIST_EXTEND              1

134           BUILD_MAP                5

123           BUILD_MAP                4

147           LOAD_CONST               8 ('id')
              LOAD_CONST              31 ('smoke_c_ingest_duplicate')

148           LOAD_CONST              10 ('covers')

149           LOAD_CONST              32 ('PAS165/PAS166 email dedupe + PAS170 pending-call dedupe (re-submit identical body)')

152           LOAD_CONST              12 ('curl')

153           LOAD_CONST              33 ('# Re-run smoke_b_ingest_first VERBATIM with the same body.')

155           LOAD_CONST              17 ('expect')

156           LOAD_CONST              18 ('http')
              LOAD_SMALL_INT         200

157           LOAD_CONST              19 ('status')
              LOAD_CONST              28 ('duplicate')

158           LOAD_CONST              28 ('duplicate')
              LOAD_CONST              30 (True)

159           LOAD_CONST              34 ('pending_call_id')
              LOAD_CONST              35 (None)

160           LOAD_CONST              36 ('call_queued')
              LOAD_CONST              29 (False)

155           BUILD_MAP                5

146           BUILD_MAP                4

164           LOAD_CONST               8 ('id')
              LOAD_CONST              37 ('smoke_d_email_only_contact')

165           LOAD_CONST              10 ('covers')
              LOAD_CONST              38 ('PAS164 call_eligible=False path (email-only contact)')

166           LOAD_CONST              12 ('curl')

167           LOAD_CONST              13 ('curl -sX POST "')
              LOAD_FAST_BORROW         0 (host)
              FORMAT_SIMPLE
              LOAD_CONST              26 ('/email-ingestion/ingest" -H "X-API-Key: ')

168           LOAD_GLOBAL              8 (_PLACEHOLDER_BROKERAGE_KEY)
              FORMAT_SIMPLE
              LOAD_CONST              39 ('" -H "Content-Type: application/json" -d \'{"subject":"New website inquiry","sender":"contact-form@brokerage.example","body":"')

172           LOAD_FAST_BORROW         3 (base_website_body)
              FORMAT_SIMPLE
              LOAD_CONST              16 ('"}\'')

167           BUILD_STRING             7

174           LOAD_CONST              17 ('expect')

175           LOAD_CONST              18 ('http')
              LOAD_SMALL_INT         200

176           LOAD_CONST              19 ('status')
              LOAD_CONST              27 ('accepted')

177           LOAD_CONST              22 ('call_eligible')
              LOAD_CONST              29 (False)

178           LOAD_CONST              36 ('call_queued')
              LOAD_CONST              29 (False)

179           LOAD_CONST              34 ('pending_call_id')
              LOAD_CONST              35 (None)

180           LOAD_CONST              40 ('warnings_include')

181           LOAD_CONST              41 ('email_lead_missing_phone')

180           BUILD_LIST               1

174           BUILD_MAP                6

163           BUILD_MAP                4

186           LOAD_CONST               8 ('id')
              LOAD_CONST              42 ('smoke_e_queue_status')

187           LOAD_CONST              10 ('covers')
              LOAD_CONST              43 ('PAS170 queue status report (read-only)')

188           LOAD_CONST              44 ('command')

189           LOAD_CONST              45 ('python -c \'from app.services.ingestion.pending_call_recovery import queue_status_report; import json; print(json.dumps(queue_status_report(brokerage_id="')

192           LOAD_FAST_BORROW         1 (brokerage_id)
              FORMAT_SIMPLE
              LOAD_CONST              46 ('"), indent=2))\'')

189           BUILD_STRING             3

194           LOAD_CONST              17 ('expect')

195           LOAD_CONST              19 ('status')
              LOAD_CONST              20 ('ok')

196           LOAD_CONST              21 ('fields_present')
              BUILD_LIST               0
              LOAD_CONST              71 (('total', 'by_status', 'by_age', 'oldest_age_seconds'))
              LIST_EXTEND              1

200           LOAD_CONST              23 ('fields_absent')
              BUILD_LIST               0
              LOAD_CONST              72 (('phone', 'email', 'name', 'transcript'))
              LIST_EXTEND              1

194           BUILD_MAP                3

185           BUILD_MAP                4

206           LOAD_CONST               8 ('id')
              LOAD_CONST              47 ('smoke_f_stale_detect_dry')

207           LOAD_CONST              10 ('covers')
              LOAD_CONST              48 ('PAS170 stale-DIALING detection (dry-run only)')

208           LOAD_CONST              44 ('command')

209           LOAD_CONST              49 ('python -c \'from app.services.ingestion.pending_call_recovery import detect_stale_dialing_rows; import json; print(json.dumps(detect_stale_dialing_rows(brokerage_id="')

212           LOAD_FAST_BORROW         1 (brokerage_id)
              FORMAT_SIMPLE
              LOAD_CONST              46 ('"), indent=2))\'')

209           BUILD_STRING             3

214           LOAD_CONST              17 ('expect')

215           LOAD_CONST              19 ('status')
              LOAD_CONST              20 ('ok')

216           LOAD_CONST              21 ('fields_present')
              BUILD_LIST               0
              LOAD_CONST              73 (('stale_after_seconds', 'count', 'rows'))
              LIST_EXTEND              1

219           LOAD_CONST              23 ('fields_absent')
              BUILD_LIST               0
              LOAD_CONST              72 (('phone', 'email', 'name', 'transcript'))
              LIST_EXTEND              1

214           BUILD_MAP                3

205           BUILD_MAP                4

225           LOAD_CONST               8 ('id')
              LOAD_CONST              50 ('smoke_g_callback_schedule')

226           LOAD_CONST              10 ('covers')
              LOAD_CONST              51 ('PAS170 callback schedule round-trip (in-process)')

227           LOAD_CONST              44 ('command')

228           LOAD_CONST              52 ('python -c \'from app.services.callbacks.callback_schedule import schedule_callback, list_pending_callbacks, reset_callback_registry_for_tests, reminder_report; import json; reset_callback_registry_for_tests(); r = schedule_callback(brokerage_id="')

232           LOAD_FAST_BORROW         1 (brokerage_id)
              FORMAT_SIMPLE
              LOAD_CONST              53 ('", source_call_id="call-smoke", scheduled_for="2026-01-01T15:00:00+00:00"); print(json.dumps(r, indent=2)); print(json.dumps(list_pending_callbacks("')

235           LOAD_FAST_BORROW         1 (brokerage_id)
              FORMAT_SIMPLE
              LOAD_CONST              54 ('"), indent=2)); print(json.dumps(reminder_report("')

236           LOAD_FAST_BORROW         1 (brokerage_id)
              FORMAT_SIMPLE
              LOAD_CONST              46 ('"), indent=2))\'')

228           BUILD_STRING             7

238           LOAD_CONST              17 ('expect')

239           LOAD_CONST              19 ('status')
              LOAD_CONST              20 ('ok')

240           LOAD_CONST              21 ('fields_present')
              BUILD_LIST               0
              LOAD_CONST              74 (('callback', 'callbacks', 'due', 'overdue'))
              LIST_EXTEND              1

243           LOAD_CONST              23 ('fields_absent')
              BUILD_LIST               0
              LOAD_CONST              75 (('phone', 'email', 'name', 'notes', 'transcript', 'summary'))
              LIST_EXTEND              1

238           BUILD_MAP                3

224           BUILD_MAP                4

250           LOAD_CONST               8 ('id')
              LOAD_CONST              55 ('smoke_h_slack_alert_optional')

251           LOAD_CONST              10 ('covers')
              LOAD_CONST              56 ('PAS170 Slack alert transport (skip when unconfigured)')

252           LOAD_CONST              44 ('command')

253           LOAD_CONST              57 ('python -c \'from app.services.monitoring.slack_alert_transport import send_alert_to_slack; import json; print(json.dumps(send_alert_to_slack({"id":"smoke", "category":"info", "severity":"info", "title":"smoke", "description":"smoke"}), indent=2))\'')

259           LOAD_CONST              17 ('expect')

260           LOAD_CONST              58 ('status_when_not_configured')
              LOAD_CONST              59 ('skipped')

261           LOAD_CONST              40 ('warnings_include')

262           LOAD_CONST              60 ('slack_webhook_not_configured')

261           BUILD_LIST               1

259           BUILD_MAP                2

249           BUILD_MAP                4

267           LOAD_CONST               8 ('id')
              LOAD_CONST              61 ('smoke_i_worker_off')

268           LOAD_CONST              10 ('covers')
              LOAD_CONST              62 ('PAS162 worker is OFF (no Twilio dial)')

269           LOAD_CONST              44 ('command')

270           LOAD_CONST              63 ("python -c 'from app.services.ingestion.worker import pending_calls_worker_enabled; print(pending_calls_worker_enabled())'")

274           LOAD_CONST              17 ('expect')

275           LOAD_CONST              64 ('stdout_contains')
              LOAD_CONST              65 ('False')

276           LOAD_CONST              66 ('operator_note')

277           LOAD_CONST              67 ('Worker remains OFF by default. Operator may explicitly start it with PENDING_CALLS_WORKER_ENABLED=true python scripts/run_pending_calls_worker.py after smoke tests pass.')

274           BUILD_MAP                2

266           BUILD_MAP                4

 96           BUILD_LIST               9
              STORE_FAST               4 (entries)

285           LOAD_FAST_BORROW         4 (entries)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 293>:
293           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('List[Dict[str, Any]]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _build_chaos_scenarios at 0x0000018C18038670, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 293>:
293           RESUME                   0

296           LOAD_CONST               0 ('id')
              LOAD_CONST               1 ('chaos_a_worker_kill_mid_dial')

297           LOAD_CONST               2 ('covers')
              LOAD_CONST               3 ('PAS170 stale DIALING detection + recovery')

298           LOAD_CONST               4 ('steps')
              BUILD_LIST               0
              LOAD_CONST              19 (('Kill the worker process while one row is DIALING.', 'Wait stale_after_seconds (default 900 s).', 'Run detect_stale_dialing_rows(...) — expect count >= 1.', 'Run recover_stale_dialing_rows(..., dry_run=False) — expect recovered_count >= 1 and the row back to PENDING.'))
              LIST_EXTEND              1

307           LOAD_CONST               5 ('expect_event_types')

308           LOAD_CONST               6 ('pending_call.stale_detected')

309           LOAD_CONST               7 ('pending_call.recovered')

307           BUILD_LIST               2

295           BUILD_MAP                4

313           LOAD_CONST               0 ('id')
              LOAD_CONST               8 ('chaos_b_duplicate_webhook')

314           LOAD_CONST               2 ('covers')
              LOAD_CONST               9 ('PAS170 per-brokerage pending-call dedupe')

315           LOAD_CONST               4 ('steps')
              BUILD_LIST               0
              LOAD_CONST              20 (('Submit the SAME webhook lead twice within 24 h to /webhooks/generic with the same phone.', 'First submission: expect status=accepted.', 'Second submission: expect status=duplicate, pending_call_id=null.'))
              LIST_EXTEND              1

326           LOAD_CONST               5 ('expect_event_types')

327           LOAD_CONST              10 ('pending_call.duplicate_suppressed')

326           BUILD_LIST               1

312           BUILD_MAP                4

331           LOAD_CONST               0 ('id')
              LOAD_CONST              11 ('chaos_c_decrypt_storm')

332           LOAD_CONST               2 ('covers')
              LOAD_CONST              12 ('PAS167/PAS168 decrypt failure + Slack alert transport')

333           LOAD_CONST               4 ('steps')
              BUILD_LIST               0
              LOAD_CONST              21 (('Rotate PAS_EMAIL_FORWARDER_SECRET_ACTIVE_KID without rotating the per-kid env key — any encrypted column will refuse to decrypt.', 'Submit an /email-ingestion/ingest request — expect status=failed, error_code in (crypto_key_missing, forwarder_secret_decrypt_failed).', 'Verify the Slack webhook (if configured) received a structural alert.'))
              LIST_EXTEND              1

349           LOAD_CONST               5 ('expect_event_types')

350           LOAD_CONST              13 ('email.forwarder.secret.decrypt_failed')

351           LOAD_CONST              14 ('alert.slack.sent')

349           BUILD_LIST               2

330           BUILD_MAP                4

355           LOAD_CONST               0 ('id')
              LOAD_CONST              15 ('chaos_d_calcom_timezone_pin')

356           LOAD_CONST               2 ('covers')
              LOAD_CONST              16 ('PAS170 Cal.com timezone hotfix')

357           LOAD_CONST               4 ('steps')

359           LOAD_CONST              17 ("Set the demo brokerage row's timezone field to a non-Eastern zone (e.g. America/Los_Angeles).")

363           LOAD_CONST              18 ("Trigger a booking via /simulate-call and verify the Cal.com payload's timeZone matches the brokerage row, not the America/New_York fallback.")

357           BUILD_LIST               2

354           BUILD_MAP                3

294           BUILD_LIST               4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 376>:
376           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('List[str]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _build_acceptance_criteria at 0x0000018C18069370, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 376>:
376           RESUME                   0

377           BUILD_LIST               0
              LOAD_CONST               1 (('All smoke entries report status=ok / status=accepted / status=duplicate / status=skipped per their expectation.', 'No smoke entry surfaces phone / email / name / raw_payload / raw_email / raw_body / transcript / signature / dedupe_key / secret in the response.', 'All four chaos scenarios produce the expected event types.', 'Worker remains OFF by default; no Twilio dial fires during the smoke matrix.', 'PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_<KID> and PAS_EMAIL_FORWARDER_SECRET_ACTIVE_KID are exported only if encryption is to be tested.', 'No migration is auto-executed; v15/v16/v17 remain proposal-only.', 'PAS-LAUNCH-01 + every PAS160-PAS170 readiness gate still reports READY.'))
              LIST_EXTEND              1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 392>:
392           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('argparse.ArgumentParser')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _build_parser at 0x0000018C1800B230, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 392>:
392           RESUME                   0

393           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

394           LOAD_CONST               0 ('pas170_demo_brokerage_smoke_plan')

396           LOAD_CONST               1 ('PAS170 — Render the structural smoke-test plan an operator should run against an internal demo brokerage before opening pilot traffic. NEVER writes anywhere; NEVER reads .env; NEVER touches production data. Sample lead values in the output are sanitised placeholders.')

393           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

404           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

405           LOAD_CONST               3 ('--host')
              LOAD_GLOBAL              6 (_PLACEHOLDER_HOST)

406           LOAD_CONST               4 ('Base URL to embed in curl placeholders.')

404           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

408           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

409           LOAD_CONST               6 ('--brokerage-id')
              LOAD_GLOBAL              8 (_PLACEHOLDER_BROKERAGE_ID)

410           LOAD_CONST               7 ('Demo brokerage identifier (placeholder only).')

408           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

412           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

413           LOAD_CONST               8 ('--json')
              LOAD_CONST               9 ('store_true')

414           LOAD_CONST              10 ('Emit the plan as a single JSON document.')

412           LOAD_CONST              11 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

416           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 419>:
419           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('plan')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _print_plan at 0x0000018C17ED9FB0, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 419>:
419            RESUME                   0

420            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST               0 ('[PAS170-smoke-plan] generated_at=')
               LOAD_FAST_BORROW         0 (plan)
               LOAD_CONST               1 ('generated_at')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

421            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST               2 ('[PAS170-smoke-plan] host=')
               LOAD_FAST_BORROW         0 (plan)
               LOAD_CONST               3 ('host')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

422            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST               4 ('[PAS170-smoke-plan] brokerage_id=')
               LOAD_FAST_BORROW         0 (plan)
               LOAD_CONST               5 ('brokerage_id')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

423            LOAD_GLOBAL              1 (print + NULL)
               CALL                     0
               POP_TOP

424            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST               6 ('=== SMOKE MATRIX ===')
               CALL                     1
               POP_TOP

425            LOAD_FAST_BORROW         0 (plan)
               LOAD_CONST               7 ('smoke_matrix')
               BINARY_OP               26 ([])
               GET_ITER
       L1:     FOR_ITER               131 (to L4)
               STORE_FAST               1 (entry)

426            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST               8 ('\n[')
               LOAD_FAST_BORROW         1 (entry)
               LOAD_CONST               9 ('id')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST              10 ('] ')
               LOAD_FAST_BORROW         1 (entry)
               LOAD_CONST              11 ('covers')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             4
               CALL                     1
               POP_TOP

427            LOAD_CONST              12 ('curl')
               LOAD_FAST_BORROW         1 (entry)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       22 (to L2)
               NOT_TAKEN

428            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              13 ('  $ ')
               LOAD_FAST_BORROW         1 (entry)
               LOAD_CONST              12 ('curl')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

429    L2:     LOAD_CONST              14 ('command')
               LOAD_FAST_BORROW         1 (entry)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       22 (to L3)
               NOT_TAKEN

430            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              13 ('  $ ')
               LOAD_FAST_BORROW         1 (entry)
               LOAD_CONST              14 ('command')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

431    L3:     LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              15 ('  expect: ')
               LOAD_GLOBAL              2 (json)
               LOAD_ATTR                4 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (entry)
               LOAD_CONST              16 ('expect')
               BINARY_OP               26 ([])
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          133 (to L1)

425    L4:     END_FOR
               POP_ITER

432            LOAD_GLOBAL              1 (print + NULL)
               CALL                     0
               POP_TOP

433            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              17 ('=== CHAOS SCENARIOS ===')
               CALL                     1
               POP_TOP

434            LOAD_FAST_BORROW         0 (plan)
               LOAD_CONST              18 ('chaos_scenarios')
               BINARY_OP               26 ([])
               GET_ITER
       L5:     FOR_ITER               145 (to L9)
               STORE_FAST               1 (entry)

435            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST               8 ('\n[')
               LOAD_FAST_BORROW         1 (entry)
               LOAD_CONST               9 ('id')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST              10 ('] ')
               LOAD_FAST_BORROW         1 (entry)
               LOAD_CONST              11 ('covers')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             4
               CALL                     1
               POP_TOP

436            LOAD_GLOBAL              7 (enumerate + NULL)
               LOAD_FAST_BORROW         1 (entry)
               LOAD_CONST              19 ('steps')
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               CALL                     2
               GET_ITER
       L6:     FOR_ITER                22 (to L7)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   35 (i, step)

437            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              20 ('  ')
               LOAD_FAST_BORROW         2 (i)
               FORMAT_SIMPLE
               LOAD_CONST              21 ('. ')
               LOAD_FAST_BORROW         3 (step)
               FORMAT_SIMPLE
               BUILD_STRING             4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           24 (to L6)

436    L7:     END_FOR
               POP_ITER

438            LOAD_FAST_BORROW         1 (entry)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST              22 ('expect_event_types')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          104 (to L5)

439    L8:     LOAD_GLOBAL              1 (print + NULL)

440            LOAD_CONST              23 ('  expect_event_types: ')

441            LOAD_GLOBAL              2 (json)
               LOAD_ATTR                4 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (entry)
               LOAD_CONST              22 ('expect_event_types')
               BINARY_OP               26 ([])
               CALL                     1
               FORMAT_SIMPLE

440            BUILD_STRING             2

439            CALL                     1
               POP_TOP
               JUMP_BACKWARD          147 (to L5)

434    L9:     END_FOR
               POP_ITER

443            LOAD_GLOBAL              1 (print + NULL)
               CALL                     0
               POP_TOP

444            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              24 ('=== ACCEPTANCE CRITERIA ===')
               CALL                     1
               POP_TOP

445            LOAD_GLOBAL              7 (enumerate + NULL)
               LOAD_FAST_BORROW         0 (plan)
               LOAD_CONST              25 ('acceptance_criteria')
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               CALL                     2
               GET_ITER
      L10:     FOR_ITER                22 (to L11)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   36 (i, crit)

446            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              20 ('  ')
               LOAD_FAST_BORROW         2 (i)
               FORMAT_SIMPLE
               LOAD_CONST              21 ('. ')
               LOAD_FAST_BORROW         4 (crit)
               FORMAT_SIMPLE
               BUILD_STRING             4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           24 (to L10)

445   L11:     END_FOR
               POP_ITER
               LOAD_CONST              26 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 449>:
449           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('argv')
              LOAD_CONST               2 ('Optional[List[str]]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object main at 0x0000018C17D4B040, file "scripts\pas170_demo_brokerage_smoke_plan.py", line 449>:
 449            RESUME                   0

 450            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 451            NOP

 452    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 456    L2:     LOAD_FAST                2 (args)
                LOAD_ATTR               10 (host)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         7 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_GLOBAL             12 (_PLACEHOLDER_HOST)
        L3:     STORE_FAST               4 (host)

 457            LOAD_FAST                2 (args)
                LOAD_ATTR               14 (brokerage_id)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         7 (to L4)
                NOT_TAKEN
                POP_TOP
                LOAD_GLOBAL             16 (_PLACEHOLDER_BROKERAGE_ID)
        L4:     STORE_FAST               5 (bid)

 460            LOAD_CONST               2 ('phase')
                LOAD_CONST               3 ('PAS170')

 461            LOAD_CONST               4 ('generated_at')
                LOAD_GLOBAL             19 (_now_iso + NULL)
                CALL                     0

 462            LOAD_CONST               5 ('host')
                LOAD_FAST                4 (host)

 463            LOAD_CONST               6 ('brokerage_id')
                LOAD_FAST                5 (bid)

 464            LOAD_CONST               7 ('smoke_matrix')
                LOAD_GLOBAL             21 (_build_smoke_matrix + NULL)
                LOAD_FAST_LOAD_FAST     69 (host, bid)
                LOAD_CONST               8 (('host', 'brokerage_id'))
                CALL_KW                  2

 465            LOAD_CONST               9 ('chaos_scenarios')
                LOAD_GLOBAL             23 (_build_chaos_scenarios + NULL)
                CALL                     0

 466            LOAD_CONST              10 ('acceptance_criteria')
                LOAD_GLOBAL             25 (_build_acceptance_criteria + NULL)
                CALL                     0

 459            BUILD_MAP                7
                STORE_FAST               6 (plan)

 469            LOAD_FAST                2 (args)
                LOAD_ATTR               26 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       37 (to L5)
                NOT_TAKEN

 470            LOAD_GLOBAL             29 (print + NULL)
                LOAD_GLOBAL             26 (json)
                LOAD_ATTR               30 (dumps)
                PUSH_NULL
                LOAD_FAST                6 (plan)
                LOAD_SMALL_INT           2
                LOAD_CONST              11 (True)
                LOAD_CONST              12 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 473            LOAD_SMALL_INT           0
                RETURN_VALUE

 472    L5:     LOAD_GLOBAL             33 (_print_plan + NULL)
                LOAD_FAST                6 (plan)
                CALL                     1
                POP_TOP

 473            LOAD_SMALL_INT           0
                RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 453            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L15)
                NOT_TAKEN
                STORE_FAST               3 (e)

 454    L7:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST              13 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L12)
        L8:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                LOAD_SMALL_INT           0
       L11:     CALL                     1
       L12:     SWAP                     2
       L13:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L14:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 453   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L6 [0]
  L6 to L7 -> L16 [1] lasti
  L7 to L9 -> L14 [1] lasti
  L10 to L12 -> L14 [1] lasti
  L12 to L13 -> L16 [1] lasti
  L14 to L16 -> L16 [1] lasti
```
