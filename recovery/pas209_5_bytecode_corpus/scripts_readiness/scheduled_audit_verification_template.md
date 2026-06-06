# scripts_readiness/scheduled_audit_verification_template

- **pyc:** `scripts\__pycache__\scheduled_audit_verification_template.cpython-314.pyc`
- **expected source path (absent):** `scripts/scheduled_audit_verification_template.py`
- **co_filename (from bytecode):** `scripts\scheduled_audit_verification_template.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS177 — Scheduled audit verification operator template.

**Template-only script.** Prints the exact operator command
sequence for a daily audit-chain verification cadence. Does
NOT install a cron entry, does NOT auto-run anything, does
NOT read .env, does NOT touch the DB or any external service.

Doctrine:

* **No autonomous installation.** The operator pastes the
  printed command sequence into their existing scheduler
  (Railway scheduled jobs / pg_cron / external cron). PAS
  never installs cron entries from inside the app.
* **No DB writes.** The template prints commands; it doesn't
  execute them.
* **No env reads.** The template does not look up
  ``$PAS_ALERT_SLACK_WEBHOOK_URL`` or any other env value.
  It emits placeholders the operator substitutes by hand.
* **No external calls.**
* **Operator cadence documentation.** The output explicitly
  documents the recommended daily cadence and the operator
  follow-up actions on a degraded result.

Usage:

    python scripts/scheduled_audit_verification_template.py
    python scripts/scheduled_audit_verification_template.py --json

Exit codes:
    0 — always.
    2 — bad CLI arguments.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `argparse`, `json`, `sys`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_print_summary`, `_template_payload`, `main`

## Env-key candidates

`PAS177`

## String constants (redacted where noted)

- "\nPAS177 — Scheduled audit verification operator template.\n\n**Template-only script.** Prints the exact operator command\nsequence for a daily audit-chain verification cadence. Does\nNOT install a cron entry, does NOT auto-run anything, does\nNOT read .env, does NOT touch the DB or any external service.\n\nDoctrine:\n\n* **No autonomous installation.** The operator pastes the\n  printed command sequence into their existing scheduler\n  (Railway scheduled jobs / pg_cron / external cron). PAS\n  never installs cron entries from inside the app.\n* **No DB writes.** The template prints commands; it doesn't\n  execute them.\n* **No env reads.** The template does not look up\n  ``$PAS_ALERT_SLACK_WEBHOOK_URL`` or any other env value.\n  It emits placeholders the operator substitutes by hand.\n* **No external calls.**\n* **Operator cadence documentation.** The output explicitly\n  documents the recommended daily cadence and the operator\n  follow-up actions on a degraded result.\n\nUsage:\n\n    python scripts/scheduled_audit_verification_template.py\n    python scripts/scheduled_audit_verification_template.py --json\n\nExit codes:\n    0 — always.\n    2 — bad CLI arguments.\n"
- 'return'
- 'Dict[str, Any]'
- 'Build the deterministic template payload.'
- 'phase'
- 'PAS177'
- 'template'
- 'scheduled_audit_verification'
- 'cadence'
- 'recommended_interval'
- 'daily'
- 'recommended_hour_utc'
- '03:00'
- 'recommended_window_hours'
- 'operator_command_sequence'
- 'step'
- 'name'
- 'Verify chain over the last 24h window'
- 'purpose'
- 'Detect any chain-break in the most recent window.'
- 'command'
- "python scripts/verify_operator_audit_chain.py --window-hours 24 --execute --generated-by '<OPERATOR_HANDLE>'"
- 'expected_exit_code'
- 'expected_status'
- 'Inspect the Slack alert channel (if chain degraded)'
- 'On chain_status=degraded, the verify script emits a structural Slack alert via the PAS171 pilot transport (requires PAS_ALERT_SLACK_WEBHOOK_URL configured). Operator inspects the alert and files a P0 ticket if needed.'
- '# Operator-side action; no PAS command.'
- 'Optional — generate proof for any flagged audit entry'
- 'On any flagged break, generate an inclusion proof so the operator can prove which row deviated from the chain.'
- "python scripts/generate_audit_inclusion_proof.py --brokerage-id '<BROKERAGE_ID>' --audit-entry-id '<ACTION_ID>' --json"
- 'Weekly — run the operator audit reaper (90-day retention)'
- 'Once per week, reap aged audit rows. v23 SQL policy enforces 30-day floor; the reaper script clamps to 60 days minimum. Default retention is 90 days.'
- 'python scripts/reap_operator_audit_log.py --older-than-days 90 --execute --json'
- 'operator_followups_on_degraded_chain'
- 'operator_followups_on_skipped_chain'
- 'constraints'
- 'notes'
- 'This template is the canonical operator runbook for the PAS audit chain verification cadence. Paste the command sequence into your scheduler of choice. PAS remains operator-controlled across every step.'
- 'argparse.ArgumentParser'
- 'scheduled_audit_verification_template'
- 'PAS177 — Print the operator command sequence for scheduled audit chain verification. Template only; does NOT install a scheduler. Read-only; no DB writes; no env reads; no external calls.'
- '--json'
- 'store_true'
- 'Emit the template as JSON on stdout instead of the human summary.'
- 'payload'
- 'None'
- '[PAS177/scheduled_audit_verification_template]'
- '  recommended cadence: '
- ' at '
- ' UTC, window='
- '  Command sequence:'
- '    '
- '       $ '
- '       (why: '
- '  Constraints (all preserved):'
- '    - '
- 'argv'
- 'Optional[List[str]]'
- 'int'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ("\nPAS177 — Scheduled audit verification operator template.\n\n**Template-only script.** Prints the exact operator command\nsequence for a daily audit-chain verification cadence. Does\nNOT install a cron entry, does NOT auto-run anything, does\nNOT read .env, does NOT touch the DB or any external service.\n\nDoctrine:\n\n* **No autonomous installation.** The operator pastes the\n  printed command sequence into their existing scheduler\n  (Railway scheduled jobs / pg_cron / external cron). PAS\n  never installs cron entries from inside the app.\n* **No DB writes.** The template prints commands; it doesn't\n  execute them.\n* **No env reads.** The template does not look up\n  ``$PAS_ALERT_SLACK_WEBHOOK_URL`` or any other env value.\n  It emits placeholders the operator substitutes by hand.\n* **No external calls.**\n* **Operator cadence documentation.** The output explicitly\n  documents the recommended daily cadence and the operator\n  follow-up actions on a degraded result.\n\nUsage:\n\n    python scripts/scheduled_audit_verification_template.py\n    python scripts/scheduled_audit_verification_template.py --json\n\nExit codes:\n    0 — always.\n    2 — bad CLI arguments.\n")
              STORE_NAME               0 (__doc__)

 35           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 37           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (argparse)
              STORE_NAME               3 (argparse)

 38           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (json)
              STORE_NAME               4 (json)

 39           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              5 (sys)
              STORE_NAME               5 (sys)

 40           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              6 (typing)
              IMPORT_FROM              7 (Any)
              STORE_NAME               7 (Any)
              IMPORT_FROM              8 (Dict)
              STORE_NAME               8 (Dict)
              IMPORT_FROM              9 (List)
              STORE_NAME               9 (List)
              IMPORT_FROM             10 (Optional)
              STORE_NAME              10 (Optional)
              POP_TOP

 43           LOAD_CONST               4 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts\scheduled_audit_verification_template.py", line 43>)
              MAKE_FUNCTION
              LOAD_CONST               5 (<code object _template_payload at 0x0000018C17FF10B0, file "scripts\scheduled_audit_verification_template.py", line 43>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              11 (_template_payload)

141           LOAD_CONST               6 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts\scheduled_audit_verification_template.py", line 141>)
              MAKE_FUNCTION
              LOAD_CONST               7 (<code object _build_parser at 0x0000018C17C49B80, file "scripts\scheduled_audit_verification_template.py", line 141>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              12 (_build_parser)

158           LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts\scheduled_audit_verification_template.py", line 158>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object _print_summary at 0x0000018C17F7AC00, file "scripts\scheduled_audit_verification_template.py", line 158>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              13 (_print_summary)

178           LOAD_CONST              13 ((None,))
              LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts\scheduled_audit_verification_template.py", line 178>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object main at 0x0000018C17D77E00, file "scripts\scheduled_audit_verification_template.py", line 178>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              14 (main)

195           LOAD_NAME               15 (__name__)
              LOAD_CONST              12 ('__main__')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       26 (to L1)
              NOT_TAKEN

196           LOAD_NAME                5 (sys)
              LOAD_ATTR               32 (exit)
              PUSH_NULL
              LOAD_NAME               14 (main)
              PUSH_NULL
              CALL                     0
              CALL                     1
              POP_TOP
              LOAD_CONST               2 (None)
              RETURN_VALUE

195   L1:     LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts\scheduled_audit_verification_template.py", line 43>:
 43           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _template_payload at 0x0000018C17FF10B0, file "scripts\scheduled_audit_verification_template.py", line 43>:
 43           RESUME                   0

 46           LOAD_CONST               1 ('phase')
              LOAD_CONST               2 ('PAS177')

 47           LOAD_CONST               3 ('template')
              LOAD_CONST               4 ('scheduled_audit_verification')

 48           LOAD_CONST               5 ('cadence')

 49           LOAD_CONST               6 ('recommended_interval')
              LOAD_CONST               7 ('daily')

 50           LOAD_CONST               8 ('recommended_hour_utc')
              LOAD_CONST               9 ('03:00')

 51           LOAD_CONST              10 ('recommended_window_hours')
              LOAD_SMALL_INT          24

 48           BUILD_MAP                3

 53           LOAD_CONST              11 ('operator_command_sequence')

 55           LOAD_CONST              12 ('step')
              LOAD_SMALL_INT           1

 56           LOAD_CONST              13 ('name')
              LOAD_CONST              14 ('Verify chain over the last 24h window')

 57           LOAD_CONST              15 ('purpose')
              LOAD_CONST              16 ('Detect any chain-break in the most recent window.')

 58           LOAD_CONST              17 ('command')

 59           LOAD_CONST              18 ("python scripts/verify_operator_audit_chain.py --window-hours 24 --execute --generated-by '<OPERATOR_HANDLE>'")

 63           LOAD_CONST              19 ('expected_exit_code')
              LOAD_SMALL_INT           0

 64           LOAD_CONST              20 ('expected_status')
              LOAD_CONST              21 ('ok')

 54           BUILD_MAP                6

 67           LOAD_CONST              12 ('step')
              LOAD_SMALL_INT           2

 68           LOAD_CONST              13 ('name')
              LOAD_CONST              22 ('Inspect the Slack alert channel (if chain degraded)')

 69           LOAD_CONST              15 ('purpose')

 70           LOAD_CONST              23 ('On chain_status=degraded, the verify script emits a structural Slack alert via the PAS171 pilot transport (requires PAS_ALERT_SLACK_WEBHOOK_URL configured). Operator inspects the alert and files a P0 ticket if needed.')

 76           LOAD_CONST              17 ('command')
              LOAD_CONST              24 ('# Operator-side action; no PAS command.')

 77           LOAD_CONST              19 ('expected_exit_code')
              LOAD_CONST              25 (None)

 78           LOAD_CONST              20 ('expected_status')
              LOAD_CONST              25 (None)

 66           BUILD_MAP                6

 81           LOAD_CONST              12 ('step')
              LOAD_SMALL_INT           3

 82           LOAD_CONST              13 ('name')
              LOAD_CONST              26 ('Optional — generate proof for any flagged audit entry')

 83           LOAD_CONST              15 ('purpose')

 84           LOAD_CONST              27 ('On any flagged break, generate an inclusion proof so the operator can prove which row deviated from the chain.')

 88           LOAD_CONST              17 ('command')

 89           LOAD_CONST              28 ("python scripts/generate_audit_inclusion_proof.py --brokerage-id '<BROKERAGE_ID>' --audit-entry-id '<ACTION_ID>' --json")

 93           LOAD_CONST              19 ('expected_exit_code')
              LOAD_SMALL_INT           0

 94           LOAD_CONST              20 ('expected_status')
              LOAD_CONST              21 ('ok')

 80           BUILD_MAP                6

 97           LOAD_CONST              12 ('step')
              LOAD_SMALL_INT           4

 98           LOAD_CONST              13 ('name')
              LOAD_CONST              29 ('Weekly — run the operator audit reaper (90-day retention)')

 99           LOAD_CONST              15 ('purpose')

100           LOAD_CONST              30 ('Once per week, reap aged audit rows. v23 SQL policy enforces 30-day floor; the reaper script clamps to 60 days minimum. Default retention is 90 days.')

105           LOAD_CONST              17 ('command')

106           LOAD_CONST              31 ('python scripts/reap_operator_audit_log.py --older-than-days 90 --execute --json')

109           LOAD_CONST              19 ('expected_exit_code')
              LOAD_SMALL_INT           0

110           LOAD_CONST              20 ('expected_status')
              LOAD_CONST              21 ('ok')

 96           BUILD_MAP                6

 53           BUILD_LIST               4

113           LOAD_CONST              32 ('operator_followups_on_degraded_chain')
              BUILD_LIST               0
              LOAD_CONST              37 (('Inspect the per-break list returned by verify_window.', 'Identify the offending action_id(s) and occurred_at timestamps.', 'Generate an inclusion proof via generate_audit_inclusion_proof.py.', 'Cross-reference against any recent operator actions in the audit history.', 'File a P0 ticket; PAS does NOT auto-remediate.'))
              LIST_EXTEND              1

120           LOAD_CONST              33 ('operator_followups_on_skipped_chain')
              BUILD_LIST               0
              LOAD_CONST              38 (('Check Supabase connectivity from the deployment host.', 'Confirm PAS_PENDING_CALL_DEDUPE_DURABLE_ENABLED / PAS_CALLBACK_SCHEDULE_DURABLE_ENABLED are not falsely toggled off.', 'Re-run the verification once the durable store is reachable.'))
              LIST_EXTEND              1

125           LOAD_CONST              34 ('constraints')
              BUILD_LIST               0
              LOAD_CONST              39 (('PAS does NOT install cron entries from inside the app.', 'PAS does NOT auto-run verification.', 'PAS does NOT auto-page on a degraded chain — operator inspects Slack.', 'PAS does NOT auto-remediate on detected break.', 'All commands are operator-driven and audited via the PAS174 audit log.'))
              LIST_EXTEND              1

132           LOAD_CONST              35 ('notes')

133           LOAD_CONST              36 ('This template is the canonical operator runbook for the PAS audit chain verification cadence. Paste the command sequence into your scheduler of choice. PAS remains operator-controlled across every step.')

 45           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts\scheduled_audit_verification_template.py", line 141>:
141           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C17C49B80, file "scripts\scheduled_audit_verification_template.py", line 141>:
141           RESUME                   0

142           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

143           LOAD_CONST               0 ('scheduled_audit_verification_template')

145           LOAD_CONST               1 ('PAS177 — Print the operator command sequence for scheduled audit chain verification. Template only; does NOT install a scheduler. Read-only; no DB writes; no env reads; no external calls.')

142           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

151           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

152           LOAD_CONST               3 ('--json')
              LOAD_CONST               4 ('store_true')

153           LOAD_CONST               5 ('Emit the template as JSON on stdout instead of the human summary.')

151           LOAD_CONST               6 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

155           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts\scheduled_audit_verification_template.py", line 158>:
158           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('payload')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _print_summary at 0x0000018C17F7AC00, file "scripts\scheduled_audit_verification_template.py", line 158>:
158           RESUME                   0

159           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST               0 ('[PAS177/scheduled_audit_verification_template]')
              CALL                     1
              POP_TOP

160           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST               1 ('  recommended cadence: ')
              LOAD_FAST_BORROW         0 (payload)
              LOAD_CONST               2 ('cadence')
              BINARY_OP               26 ([])
              LOAD_CONST               3 ('recommended_interval')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' at ')

161           LOAD_FAST_BORROW         0 (payload)
              LOAD_CONST               2 ('cadence')
              BINARY_OP               26 ([])
              LOAD_CONST               5 ('recommended_hour_utc')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' UTC, window=')

162           LOAD_FAST_BORROW         0 (payload)
              LOAD_CONST               2 ('cadence')
              BINARY_OP               26 ([])
              LOAD_CONST               7 ('recommended_window_hours')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 ('h')

160           BUILD_STRING             7
              CALL                     1
              POP_TOP

163           LOAD_GLOBAL              1 (print + NULL)
              CALL                     0
              POP_TOP

164           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST               9 ('  Command sequence:')
              CALL                     1
              POP_TOP

165           LOAD_FAST_BORROW         0 (payload)
              LOAD_CONST              10 ('operator_command_sequence')
              BINARY_OP               26 ([])
              GET_ITER
      L1:     FOR_ITER               141 (to L6)
              STORE_FAST               1 (step)

166           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              11 ('    ')
              LOAD_FAST_BORROW         1 (step)
              LOAD_CONST              12 ('step')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              13 ('. ')
              LOAD_FAST_BORROW         1 (step)
              LOAD_CONST              14 ('name')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             4
              CALL                     1
              POP_TOP

167           LOAD_FAST_BORROW         1 (step)
              LOAD_CONST              15 ('command')
              BINARY_OP               26 ([])
              TO_BOOL
              POP_JUMP_IF_FALSE       46 (to L4)
              NOT_TAKEN

168           LOAD_FAST_BORROW         1 (step)
              LOAD_CONST              15 ('command')
              BINARY_OP               26 ([])
              LOAD_ATTR                3 (split + NULL|self)
              LOAD_CONST              16 ('\n')
              CALL                     1
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (line)

169           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              17 ('       $ ')
              LOAD_FAST_BORROW         2 (line)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

168   L3:     END_FOR
              POP_ITER

170   L4:     LOAD_FAST_BORROW         1 (step)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST              18 ('purpose')
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD          119 (to L1)

171   L5:     LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              19 ('       (why: ')
              LOAD_FAST_BORROW         1 (step)
              LOAD_CONST              18 ('purpose')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              20 (')')
              BUILD_STRING             3
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          143 (to L1)

165   L6:     END_FOR
              POP_ITER

172           LOAD_GLOBAL              1 (print + NULL)
              CALL                     0
              POP_TOP

173           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              21 ('  Constraints (all preserved):')
              CALL                     1
              POP_TOP

174           LOAD_FAST_BORROW         0 (payload)
              LOAD_CONST              22 ('constraints')
              BINARY_OP               26 ([])
              GET_ITER
      L7:     FOR_ITER                17 (to L8)
              STORE_FAST               3 (c)

175           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              23 ('    - ')
              LOAD_FAST_BORROW         3 (c)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L7)

174   L8:     END_FOR
              POP_ITER
              LOAD_CONST              24 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts\scheduled_audit_verification_template.py", line 178>:
178           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D77E00, file "scripts\scheduled_audit_verification_template.py", line 178>:
 178            RESUME                   0

 179            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 180            NOP

 181    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 185    L2:     LOAD_GLOBAL             11 (_template_payload + NULL)
                CALL                     0
                STORE_FAST               4 (payload)

 187            LOAD_FAST                2 (args)
                LOAD_ATTR               12 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       37 (to L3)
                NOT_TAKEN

 188            LOAD_GLOBAL             15 (print + NULL)
                LOAD_GLOBAL             12 (json)
                LOAD_ATTR               16 (dumps)
                PUSH_NULL
                LOAD_FAST                4 (payload)
                LOAD_SMALL_INT           2
                LOAD_CONST               2 (True)
                LOAD_CONST               3 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 192            LOAD_SMALL_INT           0
                RETURN_VALUE

 190    L3:     LOAD_GLOBAL             19 (_print_summary + NULL)
                LOAD_FAST                4 (payload)
                CALL                     1
                POP_TOP

 192            LOAD_SMALL_INT           0
                RETURN_VALUE

  --    L4:     PUSH_EXC_INFO

 182            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L13)
                NOT_TAKEN
                STORE_FAST               3 (e)

 183    L5:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST               4 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L10)
        L6:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
        L7:     NOT_TAKEN
        L8:     POP_TOP
                LOAD_SMALL_INT           0
        L9:     CALL                     1
       L10:     SWAP                     2
       L11:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L12:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 182   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L4 [0]
  L4 to L5 -> L14 [1] lasti
  L5 to L7 -> L12 [1] lasti
  L8 to L10 -> L12 [1] lasti
  L10 to L11 -> L14 [1] lasti
  L12 to L14 -> L14 [1] lasti
```
