# slack/employee_mode

- **pyc:** `app\services\slack\__pycache__\employee_mode.cpython-314.pyc`
- **expected source path (absent):** `app\services\slack/employee_mode.py`
- **co_filename (from bytecode):** `app/services/slack\employee_mode.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** slack

## Module docstring

```
PAS172 — Slack Employee Mode v1 (OPS-ONLY block builders).

STRICTLY OPS-ONLY. The doctrine here is the same as the PAS171
pilot Slack transport but for the human-readable Slack
*content* (blocks) rather than the wire-level transport:

ALLOWED:
  * Queue depth summaries.
  * Stale worker alerts.
  * Callback due / overdue summaries.
  * Pending-call recovery summaries.
  * Operator diagnostics.
  * Brokerage-scoped visibility.

NOT ALLOWED:
  * AI chat assistant.
  * Interactive booking.
  * Interactive memory approval / editing.
  * Lead transcript / raw call transcript display.
  * Raw payload display.
  * Autonomous actions.
  * Gmail / email access.
  * Slash-command interactivity (Block Kit buttons / modals /
    `type: button` / `type: actions`).

Doctrine carried by every builder here:

* **Outbound-display only.** Block builders return JSON-safe
  dicts the caller hands to the PAS171 ``send_pilot_alert_to_
  slack`` (or directly POSTs to a webhook URL). No
  interactive elements.
* **Closed allow-listed fields.** Every builder projects
  inputs against a tight allow-list. PII tokens (phone,
  email, name, transcript, raw payload, secret, signature,
  dedupe key) are NEVER serialised into the output.
* **Defensive scan.** Every public builder runs the final
  block list through ``_scan_blocks_for_forbidden_tokens``;
  any leak collapses the output to a single warning block.
* **No raises.** Bad input collapses to a single warning
  block; the caller continues.

Public surface:

  * ``build_worker_status_block(report)``
  * ``build_queue_summary_block(queue_report, *, brokerage_id=None)``
  * ``build_callback_summary_block(reminder_report,
        *, brokerage_id=None)``
  * ``build_recovery_summary_block(recovery_report,
        *, brokerage_id=None)``
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `logging`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_finalise`, `_safe_int`, `_safe_str`, `_scan_block_types`, `_scan_blocks_for_forbidden_tokens`, `_scope_label`, `_warning_block`, `build_callback_summary_block`, `build_queue_summary_block`, `build_recovery_summary_block`, `build_worker_status_block`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS172 — Slack Employee Mode v1 (OPS-ONLY block builders).\n\nSTRICTLY OPS-ONLY. The doctrine here is the same as the PAS171\npilot Slack transport but for the human-readable Slack\n*content* (blocks) rather than the wire-level transport:\n\nALLOWED:\n  * Queue depth summaries.\n  * Stale worker alerts.\n  * Callback due / overdue summaries.\n  * Pending-call recovery summaries.\n  * Operator diagnostics.\n  * Brokerage-scoped visibility.\n\nNOT ALLOWED:\n  * AI chat assistant.\n  * Interactive booking.\n  * Interactive memory approval / editing.\n  * Lead transcript / raw call transcript display.\n  * Raw payload display.\n  * Autonomous actions.\n  * Gmail / email access.\n  * Slash-command interactivity (Block Kit buttons / modals /\n    `type: button` / `type: actions`).\n\nDoctrine carried by every builder here:\n\n* **Outbound-display only.** Block builders return JSON-safe\n  dicts the caller hands to the PAS171 ``send_pilot_alert_to_\n  slack`` (or directly POSTs to a webhook URL). No\n  interactive elements.\n* **Closed allow-listed fields.** Every builder projects\n  inputs against a tight allow-list. PII tokens (phone,\n  email, name, transcript, raw payload, secret, signature,\n  dedupe key) are NEVER serialised into the output.\n* **Defensive scan.** Every public builder runs the final\n  block list through ``_scan_blocks_for_forbidden_tokens``;\n  any leak collapses the output to a single warning block.\n* **No raises.** Bad input collapses to a single warning\n  block; the caller continues.\n\nPublic surface:\n\n  * ``build_worker_status_block(report)``\n  * ``build_queue_summary_block(queue_report, *, brokerage_id=None)``\n  * ``build_callback_summary_block(reminder_report,\n        *, brokerage_id=None)``\n  * ``build_recovery_summary_block(recovery_report,\n        *, brokerage_id=None)``\n'
- 'pas.slack.employee_mode'
- 'default'
- 'brokerage_id'
- 'value'
- 'Any'
- 'int'
- 'return'
- 'str'
- 'Optional[str]'
- '_brokerage_: `'
- '_scope_: all brokerages'
- 'message'
- 'List[Dict[str, Any]]'
- 'Single-block fallback used when a builder is handed bad\ninput or when the defensive scan tripped. NEVER carries the\noffending value.'
- 'type'
- 'section'
- 'text'
- 'mrkdwn'
- ':warning: *PAS ops block builder*\n'
- 'blocks'
- 'List[str]'
- 'Walk the block list recursively; return any forbidden\ntokens (substring match on keys + string values, case\ninsensitive). NEVER raises.'
- 'obj'
- 'None'
- 'Return a list of block types outside the allow-list.\nNEVER raises.'
- 'non_list_blocks'
- 'non_dict_block'
- 'Defensive final pass — if either the forbidden-token\nscan or the block-type scan trips, collapse to a single\nwarning block. NEVER raises.'
- 'output collapsed — forbidden token(s) detected: `'
- 'output collapsed — disallowed block type(s) detected: `'
- 'report'
- 'Convert a ``heartbeat_monitor_report`` envelope into a\nSlack Block Kit list. NEVER raises.\n\n``report`` is expected shape::\n\n    {\n      "status":       "ok" | "skipped" | "failed",\n      "total":        int,\n      "by_status":    {"RUNNING": n, ...},\n      "by_worker_type": {"pending_call_worker": n, ...},\n      "oldest_age_seconds": int | None,\n      ...\n    }\n'
- 'worker report payload is not a dict'
- 'status'
- 'total'
- 'by_status'
- 'by_worker_type'
- 'oldest_age_seconds'
- ':robot_face:'
- ':construction:'
- 'header'
- 'plain_text'
- ' PAS worker status'
- '*Snapshot status*: `'
- 'unknown'
- '`\n*Workers tracked*: `'
- '`\n*Oldest heartbeat age*: `'
- '*By status*: '
- '*By worker type*: '
- '`: '
- 'queue_report'
- 'Convert a ``queue_status_report`` envelope into a Slack\nBlock Kit list. NEVER raises.\n\n``queue_report`` is expected shape::\n\n    {\n      "status":       "ok" | "skipped",\n      "total":        int,\n      "by_status":    {"PENDING": n, "DIALING": n, ...},\n      "by_age":       {"lt_60s": n, ...},\n      "oldest_age_seconds": int | None,\n      ...\n    }\n'
- 'queue report payload is not a dict'
- 'by_age'
- ':inbox_tray: PAS pending-call queue'
- 'context'
- 'elements'
- '*Rows*: `'
- '`\n*Oldest age*: `'
- '*Age buckets*: '
- 'reminder_report'
- 'Convert a ``reminder_report`` envelope into a Slack\nBlock Kit list. NEVER raises.\n\n``reminder_report`` is expected shape::\n\n    {\n      "status":            "ok" | "skipped" | "failed",\n      "lookahead_minutes": int,\n      "due_count":         int,\n      "overdue_count":     int,\n      ...\n    }\n'
- 'reminder report payload is not a dict'
- 'lookahead_minutes'
- 'due_count'
- 'overdue_count'
- ':bell:'
- ':rotating_light:'
- ' PAS callback summary'
- '*Lookahead*: `'
- ' min`\n*Due in window*: `'
- '`\n*Overdue*: `'
- 'recovery_report'
- 'Convert a stale-DIALING ``recover_stale_dialing_rows``\nenvelope into a Slack Block Kit list. NEVER raises.\n\n``recovery_report`` is expected shape::\n\n    {\n      "status":              "ok" | "skipped" | "failed",\n      "mode":                "dry-run" | "execute",\n      "stale_after_seconds": int,\n      "candidate_count":     int,\n      "recovered_count":     int,\n      "skipped_count":       int,\n      "failed_count":        int,\n      ...\n    }\n'
- 'recovery report payload is not a dict'
- 'mode'
- 'stale_after_seconds'
- 'candidate_count'
- 'recovered_count'
- 'skipped_count'
- 'failed_count'
- 'execute'
- ':wrench:'
- ':mag:'
- ' PAS stale-DIALING recovery'
- '*Mode*: `'
- '`\n*Stale threshold*: `'
- ' s`\n*Candidates*: `'
- '*Recovered*: `'
- '`  *Skipped*: `'
- '`  *Failed*: `'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS172 — Slack Employee Mode v1 (OPS-ONLY block builders).\n\nSTRICTLY OPS-ONLY. The doctrine here is the same as the PAS171\npilot Slack transport but for the human-readable Slack\n*content* (blocks) rather than the wire-level transport:\n\nALLOWED:\n  * Queue depth summaries.\n  * Stale worker alerts.\n  * Callback due / overdue summaries.\n  * Pending-call recovery summaries.\n  * Operator diagnostics.\n  * Brokerage-scoped visibility.\n\nNOT ALLOWED:\n  * AI chat assistant.\n  * Interactive booking.\n  * Interactive memory approval / editing.\n  * Lead transcript / raw call transcript display.\n  * Raw payload display.\n  * Autonomous actions.\n  * Gmail / email access.\n  * Slash-command interactivity (Block Kit buttons / modals /\n    `type: button` / `type: actions`).\n\nDoctrine carried by every builder here:\n\n* **Outbound-display only.** Block builders return JSON-safe\n  dicts the caller hands to the PAS171 ``send_pilot_alert_to_\n  slack`` (or directly POSTs to a webhook URL). No\n  interactive elements.\n* **Closed allow-listed fields.** Every builder projects\n  inputs against a tight allow-list. PII tokens (phone,\n  email, name, transcript, raw payload, secret, signature,\n  dedupe key) are NEVER serialised into the output.\n* **Defensive scan.** Every public builder runs the final\n  block list through ``_scan_blocks_for_forbidden_tokens``;\n  any leak collapses the output to a single warning block.\n* **No raises.** Bad input collapses to a single warning\n  block; the caller continues.\n\nPublic surface:\n\n  * ``build_worker_status_block(report)``\n  * ``build_queue_summary_block(queue_report, *, brokerage_id=None)``\n  * ``build_callback_summary_block(reminder_report,\n        *, brokerage_id=None)``\n  * ``build_recovery_summary_block(recovery_report,\n        *, brokerage_id=None)``\n')
              STORE_NAME               0 (__doc__)

 53           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 55           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 56           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (List)
              STORE_NAME               7 (List)
              IMPORT_FROM              8 (Optional)
              STORE_NAME               8 (Optional)
              POP_TOP

 59           LOAD_NAME                3 (logging)
              LOAD_ATTR               18 (getLogger)
              PUSH_NULL
              LOAD_CONST               4 ('pas.slack.employee_mode')
              CALL                     1
              STORE_NAME              10 (logger)

 68           LOAD_CONST              29 (('phone', 'email', 'name', 'transcript', 'summary_text', 'raw_payload', 'raw_email', 'raw_body', 'secret', 'signature', 'dedupe_key', 'callback_notes', 'x_api_key', 'x-api-key', 'service_role'))
              STORE_NAME              11 (FORBIDDEN_BLOCK_TOKENS)

 88           LOAD_CONST              30 (('header', 'section', 'context', 'divider'))
              STORE_NAME              12 (ALLOWED_BLOCK_TYPES)

100           LOAD_CONST               5 ('default')
              LOAD_SMALL_INT           0
              BUILD_MAP                1
              LOAD_CONST               6 (<code object __annotate__ at 0x0000018C18024C30, file "app/services/slack\employee_mode.py", line 100>)
              MAKE_FUNCTION
              LOAD_CONST               7 (<code object _safe_int at 0x0000018C180392F0, file "app/services/slack\employee_mode.py", line 100>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              13 (_safe_int)

110           LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA21F0, file "app/services/slack\employee_mode.py", line 110>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object _safe_str at 0x0000018C1802CD40, file "app/services/slack\employee_mode.py", line 110>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              14 (_safe_str)

118           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA2F10, file "app/services/slack\employee_mode.py", line 118>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _scope_label at 0x0000018C17FBFEE0, file "app/services/slack\employee_mode.py", line 118>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              15 (_scope_label)

123           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA31E0, file "app/services/slack\employee_mode.py", line 123>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _warning_block at 0x0000018C17FA3690, file "app/services/slack\employee_mode.py", line 123>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              16 (_warning_block)

138           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA3960, file "app/services/slack\employee_mode.py", line 138>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _scan_blocks_for_forbidden_tokens at 0x0000018C18128360, file "app/services/slack\employee_mode.py", line 138>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              17 (_scan_blocks_for_forbidden_tokens)

167           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA3F00, file "app/services/slack\employee_mode.py", line 167>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _scan_block_types at 0x0000018C17EC4280, file "app/services/slack\employee_mode.py", line 167>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              18 (_scan_block_types)

183           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA1E30, file "app/services/slack\employee_mode.py", line 183>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object _finalise at 0x0000018C179A7290, file "app/services/slack\employee_mode.py", line 183>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              19 (_finalise)

206           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA32D0, file "app/services/slack\employee_mode.py", line 206>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object build_worker_status_block at 0x0000018C17ED5230, file "app/services/slack\employee_mode.py", line 206>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              20 (build_worker_status_block)

283           LOAD_CONST              22 ('brokerage_id')

286           LOAD_CONST               2 (None)

283           BUILD_MAP                1
              LOAD_CONST              23 (<code object __annotate__ at 0x0000018C18025E30, file "app/services/slack\employee_mode.py", line 283>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object build_queue_summary_block at 0x0000018C181B3A30, file "app/services/slack\employee_mode.py", line 283>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              21 (build_queue_summary_block)

363           LOAD_CONST              22 ('brokerage_id')

366           LOAD_CONST               2 (None)

363           BUILD_MAP                1
              LOAD_CONST              25 (<code object __annotate__ at 0x0000018C18026530, file "app/services/slack\employee_mode.py", line 363>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object build_callback_summary_block at 0x0000018C17D85D70, file "app/services/slack\employee_mode.py", line 363>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              22 (build_callback_summary_block)

425           LOAD_CONST              22 ('brokerage_id')

428           LOAD_CONST               2 (None)

425           BUILD_MAP                1
              LOAD_CONST              27 (<code object __annotate__ at 0x0000018C18024E30, file "app/services/slack\employee_mode.py", line 425>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object build_recovery_summary_block at 0x0000018C17D6DFC0, file "app/services/slack\employee_mode.py", line 425>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              23 (build_recovery_summary_block)

496           BUILD_LIST               0
              LOAD_CONST              31 (('FORBIDDEN_BLOCK_TOKENS', 'ALLOWED_BLOCK_TYPES', 'build_worker_status_block', 'build_queue_summary_block', 'build_callback_summary_block', 'build_recovery_summary_block'))
              LIST_EXTEND              1
              STORE_NAME              24 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app/services/slack\employee_mode.py", line 100>:
100           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('default')
              LOAD_CONST               4 ('int')
              LOAD_CONST               5 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _safe_int at 0x0000018C180392F0, file "app/services/slack\employee_mode.py", line 100>:
 100           RESUME                   0

 101           NOP

 102   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               2 (v)

 103           LOAD_FAST_BORROW         2 (v)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 104           LOAD_FAST_BORROW         1 (default)
       L2:     RETURN_VALUE

 105   L3:     LOAD_FAST_BORROW         2 (v)
       L4:     RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 106           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

 107           LOAD_FAST                1 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 106   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L3 to L4 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app/services/slack\employee_mode.py", line 110>:
110           RESUME                   0
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

Disassembly of <code object _safe_str at 0x0000018C1802CD40, file "app/services/slack\employee_mode.py", line 110>:
110           RESUME                   0

111           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L1)
              NOT_TAKEN

112           LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

113   L1:     LOAD_FAST_BORROW         0 (value)
              POP_JUMP_IF_NOT_NONE     3 (to L2)
              NOT_TAKEN

114           LOAD_CONST               1 ('')
              RETURN_VALUE

115   L2:     LOAD_CONST               1 ('')
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "app/services/slack\employee_mode.py", line 118>:
118           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('Optional[str]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _scope_label at 0x0000018C17FBFEE0, file "app/services/slack\employee_mode.py", line 118>:
118           RESUME                   0

119           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (brokerage_id)
              CALL                     1
              STORE_FAST               1 (bid)

120           LOAD_FAST_BORROW         1 (bid)
              TO_BOOL
              POP_JUMP_IF_FALSE        7 (to L1)
              NOT_TAKEN
              LOAD_CONST               0 ('_brokerage_: `')
              LOAD_FAST_BORROW         1 (bid)
              FORMAT_SIMPLE
              LOAD_CONST               1 ('`')
              BUILD_STRING             3
              RETURN_VALUE
      L1:     LOAD_CONST               2 ('_scope_: all brokerages')
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "app/services/slack\employee_mode.py", line 123>:
123           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('message')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Dict[str, Any]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _warning_block at 0x0000018C17FA3690, file "app/services/slack\employee_mode.py", line 123>:
123           RESUME                   0

129           LOAD_CONST               1 ('type')
              LOAD_CONST               2 ('section')

130           LOAD_CONST               3 ('text')

131           LOAD_CONST               1 ('type')
              LOAD_CONST               4 ('mrkdwn')

132           LOAD_CONST               3 ('text')
              LOAD_CONST               5 (':warning: *PAS ops block builder*\n')
              LOAD_FAST_BORROW         0 (message)
              FORMAT_SIMPLE
              BUILD_STRING             2

130           BUILD_MAP                2

128           BUILD_MAP                2

127           BUILD_LIST               1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app/services/slack\employee_mode.py", line 138>:
138           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('blocks')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _scan_blocks_for_forbidden_tokens at 0x0000018C18128360, file "app/services/slack\employee_mode.py", line 138>:
  --           MAKE_CELL                1 (found)
               MAKE_CELL                2 (walk)

 138           RESUME                   0

 142           BUILD_LIST               0
               STORE_DEREF              1 (found)

 143           LOAD_CONST               1 (<code object __annotate__ at 0x0000018C17FA2E20, file "app/services/slack\employee_mode.py", line 143>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (found)
               LOAD_FAST_BORROW         2 (walk)
               BUILD_TUPLE              2
               LOAD_CONST               2 (<code object walk at 0x0000018C18646C00, file "app/services/slack\employee_mode.py", line 143>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              2 (walk)

 163           LOAD_DEREF               2 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (blocks)
               CALL                     1
               POP_TOP

 164           LOAD_DEREF               1 (found)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app/services/slack\employee_mode.py", line 143>:
143           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('obj')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object walk at 0x0000018C18646C00, file "app/services/slack\employee_mode.py", line 143>:
  --            COPY_FREE_VARS           2

 143            RESUME                   0

 144            NOP

 145    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      121 (to L14)
        L2:     NOT_TAKEN

 146    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                98 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

 147            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       64 (to L11)
                NOT_TAKEN

 148            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

 149            LOAD_GLOBAL             10 (FORBIDDEN_BLOCK_TOKENS)
                GET_ITER
        L5:     FOR_ITER                37 (to L10)
                STORE_FAST               4 (tok)

 150            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)
        L7:     LOAD_FAST_BORROW         4 (tok)
                LOAD_DEREF               6 (found)
                CONTAINS_OP              1 (not in)
        L8:     POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           20 (to L5)

 151    L9:     LOAD_DEREF               6 (found)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_FAST_BORROW         4 (tok)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           39 (to L5)

 149   L10:     END_FOR
                POP_ITER

 152   L11:     LOAD_DEREF               7 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          100 (to L4)

 146   L12:     END_FOR
                POP_ITER
       L13:     LOAD_CONST               0 (None)
                RETURN_VALUE

 153   L14:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             14 (list)
                LOAD_GLOBAL             16 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       20 (to L18)
                NOT_TAKEN

 154            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L15:     FOR_ITER                11 (to L16)
                STORE_FAST               2 (v)

 155            LOAD_DEREF               7 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           13 (to L15)

 154   L16:     END_FOR
                POP_ITER
       L17:     LOAD_CONST               0 (None)
                RETURN_VALUE

 156   L18:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       66 (to L26)
                NOT_TAKEN

 157            LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               5 (ol)

 158            LOAD_GLOBAL             10 (FORBIDDEN_BLOCK_TOKENS)
                GET_ITER
       L19:     FOR_ITER                37 (to L24)
                STORE_FAST               4 (tok)

 159            LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (tok, ol)
                CONTAINS_OP              0 (in)
       L20:     POP_JUMP_IF_TRUE         3 (to L21)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L19)
       L21:     LOAD_FAST_BORROW         4 (tok)
                LOAD_DEREF               6 (found)
                CONTAINS_OP              1 (not in)
       L22:     POP_JUMP_IF_TRUE         3 (to L23)
                NOT_TAKEN
                JUMP_BACKWARD           20 (to L19)

 160   L23:     LOAD_DEREF               6 (found)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_FAST_BORROW         4 (tok)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           39 (to L19)

 158   L24:     END_FOR
                POP_ITER
       L25:     LOAD_CONST               0 (None)
                RETURN_VALUE

 156   L26:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L27:     PUSH_EXC_INFO

 161            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L29)
                NOT_TAKEN
                POP_TOP

 162   L28:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 161   L29:     RERAISE                  0

  --   L30:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L27 [0]
  L3 to L6 -> L27 [0]
  L7 to L8 -> L27 [0]
  L9 to L13 -> L27 [0]
  L14 to L17 -> L27 [0]
  L18 to L20 -> L27 [0]
  L21 to L22 -> L27 [0]
  L23 to L25 -> L27 [0]
  L27 to L28 -> L30 [1] lasti
  L29 to L30 -> L30 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "app/services/slack\employee_mode.py", line 167>:
167           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('blocks')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _scan_block_types at 0x0000018C17EC4280, file "app/services/slack\employee_mode.py", line 167>:
167           RESUME                   0

170           BUILD_LIST               0
              STORE_FAST               1 (out)

171           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (blocks)
              LOAD_GLOBAL              2 (list)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         4 (to L1)
              NOT_TAKEN

172           LOAD_CONST               1 ('non_list_blocks')
              BUILD_LIST               1
              RETURN_VALUE

173   L1:     LOAD_FAST_BORROW         0 (blocks)
              GET_ITER
      L2:     FOR_ITER               122 (to L5)
              STORE_FAST               2 (block)

174           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (block)
              LOAD_GLOBAL              4 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        20 (to L3)
              NOT_TAKEN

175           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               2 ('non_dict_block')
              CALL                     1
              POP_TOP

176           JUMP_BACKWARD           44 (to L2)

177   L3:     LOAD_FAST_BORROW         2 (block)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               3 ('type')
              CALL                     1
              STORE_FAST               3 (t)

178           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (t)
              LOAD_GLOBAL             10 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       14 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         3 (t)
              LOAD_GLOBAL             12 (ALLOWED_BLOCK_TYPES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD           96 (to L2)

179   L4:     LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL             11 (str + NULL)
              LOAD_FAST_BORROW         3 (t)
              CALL                     1
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          124 (to L2)

173   L5:     END_FOR
              POP_ITER

180           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "app/services/slack\employee_mode.py", line 183>:
183           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('blocks')
              LOAD_CONST               2 ('List[Dict[str, Any]]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('List[Dict[str, Any]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _finalise at 0x0000018C179A7290, file "app/services/slack\employee_mode.py", line 183>:
183           RESUME                   0

187           LOAD_GLOBAL              1 (_scan_blocks_for_forbidden_tokens + NULL)
              LOAD_FAST_BORROW         0 (blocks)
              CALL                     1
              STORE_FAST               1 (leaked)

188           LOAD_FAST_BORROW         1 (leaked)
              TO_BOOL
              POP_JUMP_IF_FALSE       47 (to L1)
              NOT_TAKEN

189           LOAD_GLOBAL              3 (_warning_block + NULL)

190           LOAD_CONST               1 ('output collapsed — forbidden token(s) detected: `')

191           LOAD_CONST               2 (', ')
              LOAD_ATTR                5 (join + NULL|self)
              LOAD_GLOBAL              7 (sorted + NULL)
              LOAD_FAST_BORROW         1 (leaked)
              CALL                     1
              CALL                     1
              LOAD_CONST               3 (slice(None, 200, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 ('`')

190           BUILD_STRING             3

189           CALL                     1
              RETURN_VALUE

193   L1:     LOAD_GLOBAL              9 (_scan_block_types + NULL)
              LOAD_FAST_BORROW         0 (blocks)
              CALL                     1
              STORE_FAST               2 (bad_types)

194           LOAD_FAST_BORROW         2 (bad_types)
              TO_BOOL
              POP_JUMP_IF_FALSE       56 (to L2)
              NOT_TAKEN

195           LOAD_GLOBAL              3 (_warning_block + NULL)

196           LOAD_CONST               5 ('output collapsed — disallowed block type(s) detected: `')

197           LOAD_CONST               2 (', ')
              LOAD_ATTR                5 (join + NULL|self)
              LOAD_GLOBAL              7 (sorted + NULL)
              LOAD_GLOBAL             11 (set + NULL)
              LOAD_FAST_BORROW         2 (bad_types)
              CALL                     1
              CALL                     1
              CALL                     1
              LOAD_CONST               3 (slice(None, 200, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 ('`')

196           BUILD_STRING             3

195           CALL                     1
              RETURN_VALUE

199   L2:     LOAD_FAST_BORROW         0 (blocks)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "app/services/slack\employee_mode.py", line 206>:
206           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')

207           LOAD_CONST               2 ('Any')

206           LOAD_CONST               3 ('return')

208           LOAD_CONST               4 ('List[Dict[str, Any]]')

206           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object build_worker_status_block at 0x0000018C17ED5230, file "app/services/slack\employee_mode.py", line 206>:
206            RESUME                   0

223            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (report)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L1)
               NOT_TAKEN

224            LOAD_GLOBAL              5 (_warning_block + NULL)
               LOAD_CONST               1 ('worker report payload is not a dict')
               CALL                     1
               RETURN_VALUE

225    L1:     LOAD_GLOBAL              7 (_safe_str + NULL)
               LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               2 ('status')
               CALL                     1
               CALL                     1
               STORE_FAST               1 (status)

226            LOAD_GLOBAL             11 (_safe_int + NULL)
               LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               3 ('total')
               CALL                     1
               CALL                     1
               STORE_FAST               2 (total)

227            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               4 ('by_status')
               CALL                     1
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L2)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               4 ('by_status')
               CALL                     1
               JUMP_FORWARD             1 (to L3)
       L2:     BUILD_MAP                0
       L3:     STORE_FAST               3 (by_status)

228            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               5 ('by_worker_type')
               CALL                     1
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               5 ('by_worker_type')
               CALL                     1
               JUMP_FORWARD             1 (to L5)
       L4:     BUILD_MAP                0
       L5:     STORE_FAST               4 (by_wt)

229            LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               6 ('oldest_age_seconds')
               CALL                     1
               STORE_FAST               5 (oldest)

231            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         5 (oldest)
               LOAD_GLOBAL             12 (int)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       15 (to L6)
               NOT_TAKEN
               LOAD_GLOBAL             13 (int + NULL)
               LOAD_FAST_BORROW         5 (oldest)
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST               7 (' s')
               BUILD_STRING             2
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               8 ('—')

230    L7:     STORE_FAST               6 (oldest_str)

234            LOAD_CONST               9 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_CONST              10 (<code object <genexpr> at 0x0000018C17FE1920, file "app/services/slack\employee_mode.py", line 234>)
               MAKE_FUNCTION

236            LOAD_GLOBAL             17 (sorted + NULL)
               LOAD_FAST_BORROW         3 (by_status)
               LOAD_ATTR               19 (items + NULL|self)
               CALL                     0
               CALL                     1
               GET_ITER

234            CALL                     0
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               POP_TOP

238            LOAD_CONST               8 ('—')

234    L8:     STORE_FAST               7 (by_status_line)

239            LOAD_CONST               9 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_CONST              11 (<code object <genexpr> at 0x0000018C17FE13E0, file "app/services/slack\employee_mode.py", line 239>)
               MAKE_FUNCTION

241            LOAD_GLOBAL             17 (sorted + NULL)
               LOAD_FAST_BORROW         4 (by_wt)
               LOAD_ATTR               19 (items + NULL|self)
               CALL                     0
               CALL                     1
               GET_ITER

239            CALL                     0
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               POP_TOP

243            LOAD_CONST               8 ('—')

239    L9:     STORE_FAST               8 (by_wt_line)

245            LOAD_FAST_BORROW         1 (status)
               LOAD_CONST              12 ('ok')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST              13 (':robot_face:')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              14 (':construction:')
      L11:     STORE_FAST               9 (emoji)

248            LOAD_CONST              15 ('type')
               LOAD_CONST              16 ('header')

249            LOAD_CONST              17 ('text')

250            LOAD_CONST              15 ('type')
               LOAD_CONST              18 ('plain_text')

251            LOAD_CONST              17 ('text')
               LOAD_FAST_BORROW         9 (emoji)
               FORMAT_SIMPLE
               LOAD_CONST              19 (' PAS worker status')
               BUILD_STRING             2

249            BUILD_MAP                2

247            BUILD_MAP                2

255            LOAD_CONST              15 ('type')
               LOAD_CONST              20 ('section')

256            LOAD_CONST              17 ('text')

257            LOAD_CONST              15 ('type')
               LOAD_CONST              21 ('mrkdwn')

258            LOAD_CONST              17 ('text')

259            LOAD_CONST              22 ('*Snapshot status*: `')
               LOAD_FAST                1 (status)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L12)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              23 ('unknown')
      L12:     FORMAT_SIMPLE
               LOAD_CONST              24 ('`\n*Workers tracked*: `')

260            LOAD_FAST_BORROW         2 (total)
               FORMAT_SIMPLE
               LOAD_CONST              25 ('`\n*Oldest heartbeat age*: `')

261            LOAD_FAST_BORROW         6 (oldest_str)
               FORMAT_SIMPLE
               LOAD_CONST              26 ('`')

259            BUILD_STRING             7

256            BUILD_MAP                2

254            BUILD_MAP                2

266            LOAD_CONST              15 ('type')
               LOAD_CONST              20 ('section')

267            LOAD_CONST              17 ('text')

268            LOAD_CONST              15 ('type')
               LOAD_CONST              21 ('mrkdwn')

269            LOAD_CONST              17 ('text')
               LOAD_CONST              27 ('*By status*: ')
               LOAD_FAST_BORROW         7 (by_status_line)
               FORMAT_SIMPLE
               BUILD_STRING             2

267            BUILD_MAP                2

265            BUILD_MAP                2

273            LOAD_CONST              15 ('type')
               LOAD_CONST              20 ('section')

274            LOAD_CONST              17 ('text')

275            LOAD_CONST              15 ('type')
               LOAD_CONST              21 ('mrkdwn')

276            LOAD_CONST              17 ('text')
               LOAD_CONST              28 ('*By worker type*: ')
               LOAD_FAST_BORROW         8 (by_wt_line)
               FORMAT_SIMPLE
               BUILD_STRING             2

274            BUILD_MAP                2

272            BUILD_MAP                2

246            BUILD_LIST               4
               STORE_FAST              10 (blocks)

280            LOAD_GLOBAL             21 (_finalise + NULL)
               LOAD_FAST_BORROW        10 (blocks)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C17FE1920, file "app/services/slack\employee_mode.py", line 234>:
 234           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 236   L2:     FOR_ITER                48 (to L5)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   18 (k, v)

 237           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (k)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL

 235   L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           29 (to L2)
       L4:     LOAD_CONST               0 ('`')
               LOAD_FAST_BORROW         1 (k)
               FORMAT_SIMPLE
               LOAD_CONST               1 ('`: ')
               LOAD_GLOBAL              5 (_safe_int + NULL)
               LOAD_FAST_BORROW         2 (v)
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             4
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           50 (to L2)

 236   L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C17FE13E0, file "app/services/slack\employee_mode.py", line 239>:
 239           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 241   L2:     FOR_ITER                48 (to L5)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   18 (k, v)

 242           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (k)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL

 240   L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           29 (to L2)
       L4:     LOAD_CONST               0 ('`')
               LOAD_FAST_BORROW         1 (k)
               FORMAT_SIMPLE
               LOAD_CONST               1 ('`: ')
               LOAD_GLOBAL              5 (_safe_int + NULL)
               LOAD_FAST_BORROW         2 (v)
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             4
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           50 (to L2)

 241   L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app/services/slack\employee_mode.py", line 283>:
283           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('queue_report')

284           LOAD_CONST               2 ('Any')

283           LOAD_CONST               3 ('brokerage_id')

286           LOAD_CONST               4 ('Optional[str]')

283           LOAD_CONST               5 ('return')

287           LOAD_CONST               6 ('List[Dict[str, Any]]')

283           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object build_queue_summary_block at 0x0000018C181B3A30, file "app/services/slack\employee_mode.py", line 283>:
283           RESUME                   0

302           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (queue_report)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        12 (to L1)
              NOT_TAKEN

303           LOAD_GLOBAL              5 (_warning_block + NULL)
              LOAD_CONST               1 ('queue report payload is not a dict')
              CALL                     1
              RETURN_VALUE

304   L1:     LOAD_GLOBAL              7 (_safe_int + NULL)
              LOAD_FAST_BORROW         0 (queue_report)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               2 ('total')
              CALL                     1
              CALL                     1
              STORE_FAST               2 (total)

305           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (queue_report)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               3 ('by_status')
              CALL                     1
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (queue_report)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               3 ('by_status')
              CALL                     1
              JUMP_FORWARD             1 (to L3)
      L2:     BUILD_MAP                0
      L3:     STORE_FAST               3 (by_status)

306           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (queue_report)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               4 ('by_age')
              CALL                     1
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (queue_report)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               4 ('by_age')
              CALL                     1
              JUMP_FORWARD             1 (to L5)
      L4:     BUILD_MAP                0
      L5:     STORE_FAST               4 (by_age)

307           LOAD_FAST_BORROW         0 (queue_report)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               5 ('oldest_age_seconds')
              CALL                     1
              STORE_FAST               5 (oldest)

308           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         5 (oldest)
              LOAD_GLOBAL             10 (int)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       15 (to L6)
              NOT_TAKEN
              LOAD_GLOBAL             11 (int + NULL)
              LOAD_FAST_BORROW         5 (oldest)
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST               6 (' s')
              BUILD_STRING             2
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST               7 ('—')
      L7:     STORE_FAST               6 (oldest_str)

310           LOAD_CONST               8 (', ')
              LOAD_ATTR               13 (join + NULL|self)
              LOAD_CONST               9 (<code object <genexpr> at 0x0000018C17FE17D0, file "app/services/slack\employee_mode.py", line 310>)
              MAKE_FUNCTION

312           LOAD_GLOBAL             15 (sorted + NULL)
              LOAD_FAST_BORROW         3 (by_status)
              LOAD_ATTR               17 (items + NULL|self)
              CALL                     0
              CALL                     1
              GET_ITER

310           CALL                     0
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L8)
              NOT_TAKEN
              POP_TOP

314           LOAD_CONST               7 ('—')

310   L8:     STORE_FAST               7 (by_status_line)

315           LOAD_CONST               8 (', ')
              LOAD_ATTR               13 (join + NULL|self)
              LOAD_CONST              10 (<code object <genexpr> at 0x0000018C17FE1BC0, file "app/services/slack\employee_mode.py", line 315>)
              MAKE_FUNCTION

317           LOAD_GLOBAL             15 (sorted + NULL)
              LOAD_FAST_BORROW         4 (by_age)
              LOAD_ATTR               17 (items + NULL|self)
              CALL                     0
              CALL                     1
              GET_ITER

315           CALL                     0
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L9)
              NOT_TAKEN
              POP_TOP

319           LOAD_CONST               7 ('—')

315   L9:     STORE_FAST               8 (by_age_line)

323           LOAD_CONST              11 ('type')
              LOAD_CONST              12 ('header')

324           LOAD_CONST              13 ('text')

325           LOAD_CONST              11 ('type')
              LOAD_CONST              14 ('plain_text')

326           LOAD_CONST              13 ('text')
              LOAD_CONST              15 (':inbox_tray: PAS pending-call queue')

324           BUILD_MAP                2

322           BUILD_MAP                2

330           LOAD_CONST              11 ('type')
              LOAD_CONST              16 ('context')

331           LOAD_CONST              17 ('elements')

332           LOAD_CONST              11 ('type')
              LOAD_CONST              18 ('mrkdwn')
              LOAD_CONST              13 ('text')
              LOAD_GLOBAL             19 (_scope_label + NULL)
              LOAD_FAST_BORROW         1 (brokerage_id)
              CALL                     1
              BUILD_MAP                2

331           BUILD_LIST               1

329           BUILD_MAP                2

336           LOAD_CONST              11 ('type')
              LOAD_CONST              19 ('section')

337           LOAD_CONST              13 ('text')

338           LOAD_CONST              11 ('type')
              LOAD_CONST              18 ('mrkdwn')

339           LOAD_CONST              13 ('text')

340           LOAD_CONST              20 ('*Rows*: `')
              LOAD_FAST_BORROW         2 (total)
              FORMAT_SIMPLE
              LOAD_CONST              21 ('`\n*Oldest age*: `')

341           LOAD_FAST_BORROW         6 (oldest_str)
              FORMAT_SIMPLE
              LOAD_CONST              22 ('`')

340           BUILD_STRING             5

337           BUILD_MAP                2

335           BUILD_MAP                2

346           LOAD_CONST              11 ('type')
              LOAD_CONST              19 ('section')

347           LOAD_CONST              13 ('text')

348           LOAD_CONST              11 ('type')
              LOAD_CONST              18 ('mrkdwn')

349           LOAD_CONST              13 ('text')
              LOAD_CONST              23 ('*By status*: ')
              LOAD_FAST_BORROW         7 (by_status_line)
              FORMAT_SIMPLE
              BUILD_STRING             2

347           BUILD_MAP                2

345           BUILD_MAP                2

353           LOAD_CONST              11 ('type')
              LOAD_CONST              19 ('section')

354           LOAD_CONST              13 ('text')

355           LOAD_CONST              11 ('type')
              LOAD_CONST              18 ('mrkdwn')

356           LOAD_CONST              13 ('text')
              LOAD_CONST              24 ('*Age buckets*: ')
              LOAD_FAST_BORROW         8 (by_age_line)
              FORMAT_SIMPLE
              BUILD_STRING             2

354           BUILD_MAP                2

352           BUILD_MAP                2

321           BUILD_LIST               5
              STORE_FAST               9 (blocks)

360           LOAD_GLOBAL             21 (_finalise + NULL)
              LOAD_FAST_BORROW         9 (blocks)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C17FE17D0, file "app/services/slack\employee_mode.py", line 310>:
 310           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 312   L2:     FOR_ITER                48 (to L5)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   18 (k, v)

 313           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (k)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL

 311   L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           29 (to L2)
       L4:     LOAD_CONST               0 ('`')
               LOAD_FAST_BORROW         1 (k)
               FORMAT_SIMPLE
               LOAD_CONST               1 ('`: ')
               LOAD_GLOBAL              5 (_safe_int + NULL)
               LOAD_FAST_BORROW         2 (v)
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             4
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           50 (to L2)

 312   L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C17FE1BC0, file "app/services/slack\employee_mode.py", line 315>:
 315           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 317   L2:     FOR_ITER                48 (to L5)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   18 (k, v)

 318           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (k)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL

 316   L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           29 (to L2)
       L4:     LOAD_CONST               0 ('`')
               LOAD_FAST_BORROW         1 (k)
               FORMAT_SIMPLE
               LOAD_CONST               1 ('`: ')
               LOAD_GLOBAL              5 (_safe_int + NULL)
               LOAD_FAST_BORROW         2 (v)
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             4
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           50 (to L2)

 317   L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026530, file "app/services/slack\employee_mode.py", line 363>:
363           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('reminder_report')

364           LOAD_CONST               2 ('Any')

363           LOAD_CONST               3 ('brokerage_id')

366           LOAD_CONST               4 ('Optional[str]')

363           LOAD_CONST               5 ('return')

367           LOAD_CONST               6 ('List[Dict[str, Any]]')

363           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object build_callback_summary_block at 0x0000018C17D85D70, file "app/services/slack\employee_mode.py", line 363>:
363           RESUME                   0

381           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (reminder_report)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        12 (to L1)
              NOT_TAKEN

382           LOAD_GLOBAL              5 (_warning_block + NULL)
              LOAD_CONST               1 ('reminder report payload is not a dict')
              CALL                     1
              RETURN_VALUE

383   L1:     LOAD_GLOBAL              7 (_safe_int + NULL)
              LOAD_FAST_BORROW         0 (reminder_report)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               2 ('lookahead_minutes')
              CALL                     1
              CALL                     1
              STORE_FAST               2 (lookahead)

384           LOAD_GLOBAL              7 (_safe_int + NULL)
              LOAD_FAST_BORROW         0 (reminder_report)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               3 ('due_count')
              CALL                     1
              CALL                     1
              STORE_FAST               3 (due)

385           LOAD_GLOBAL              7 (_safe_int + NULL)
              LOAD_FAST_BORROW         0 (reminder_report)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               4 ('overdue_count')
              CALL                     1
              CALL                     1
              STORE_FAST               4 (overdue)

395           LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (due, overdue)
              BINARY_OP                0 (+)
              LOAD_SMALL_INT           0
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               5 (':bell:')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               6 (':rotating_light:')
      L3:     STORE_FAST               5 (emoji)

398           LOAD_CONST               7 ('type')
              LOAD_CONST               8 ('header')

399           LOAD_CONST               9 ('text')

400           LOAD_CONST               7 ('type')
              LOAD_CONST              10 ('plain_text')

401           LOAD_CONST               9 ('text')
              LOAD_FAST_BORROW         5 (emoji)
              FORMAT_SIMPLE
              LOAD_CONST              11 (' PAS callback summary')
              BUILD_STRING             2

399           BUILD_MAP                2

397           BUILD_MAP                2

405           LOAD_CONST               7 ('type')
              LOAD_CONST              12 ('context')

406           LOAD_CONST              13 ('elements')

407           LOAD_CONST               7 ('type')
              LOAD_CONST              14 ('mrkdwn')
              LOAD_CONST               9 ('text')
              LOAD_GLOBAL             11 (_scope_label + NULL)
              LOAD_FAST_BORROW         1 (brokerage_id)
              CALL                     1
              BUILD_MAP                2

406           BUILD_LIST               1

404           BUILD_MAP                2

411           LOAD_CONST               7 ('type')
              LOAD_CONST              15 ('section')

412           LOAD_CONST               9 ('text')

413           LOAD_CONST               7 ('type')
              LOAD_CONST              14 ('mrkdwn')

414           LOAD_CONST               9 ('text')

415           LOAD_CONST              16 ('*Lookahead*: `')
              LOAD_FAST_BORROW         2 (lookahead)
              FORMAT_SIMPLE
              LOAD_CONST              17 (' min`\n*Due in window*: `')

416           LOAD_FAST_BORROW         3 (due)
              FORMAT_SIMPLE
              LOAD_CONST              18 ('`\n*Overdue*: `')

417           LOAD_FAST_BORROW         4 (overdue)
              FORMAT_SIMPLE
              LOAD_CONST              19 ('`')

415           BUILD_STRING             7

412           BUILD_MAP                2

410           BUILD_MAP                2

396           BUILD_LIST               3
              STORE_FAST               6 (blocks)

422           LOAD_GLOBAL             13 (_finalise + NULL)
              LOAD_FAST_BORROW         6 (blocks)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app/services/slack\employee_mode.py", line 425>:
425           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recovery_report')

426           LOAD_CONST               2 ('Any')

425           LOAD_CONST               3 ('brokerage_id')

428           LOAD_CONST               4 ('Optional[str]')

425           LOAD_CONST               5 ('return')

429           LOAD_CONST               6 ('List[Dict[str, Any]]')

425           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object build_recovery_summary_block at 0x0000018C17D6DFC0, file "app/services/slack\employee_mode.py", line 425>:
425           RESUME                   0

446           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (recovery_report)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        12 (to L1)
              NOT_TAKEN

447           LOAD_GLOBAL              5 (_warning_block + NULL)
              LOAD_CONST               1 ('recovery report payload is not a dict')
              CALL                     1
              RETURN_VALUE

448   L1:     LOAD_GLOBAL              7 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (recovery_report)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               2 ('mode')
              CALL                     1
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               3 ('—')
      L2:     STORE_FAST               2 (mode)

449           LOAD_GLOBAL             11 (_safe_int + NULL)
              LOAD_FAST_BORROW         0 (recovery_report)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               4 ('stale_after_seconds')
              CALL                     1
              CALL                     1
              STORE_FAST               3 (threshold)

450           LOAD_GLOBAL             11 (_safe_int + NULL)
              LOAD_FAST_BORROW         0 (recovery_report)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               5 ('candidate_count')
              CALL                     1
              CALL                     1
              STORE_FAST               4 (candidate)

451           LOAD_GLOBAL             11 (_safe_int + NULL)
              LOAD_FAST_BORROW         0 (recovery_report)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               6 ('recovered_count')
              CALL                     1
              CALL                     1
              STORE_FAST               5 (recovered)

452           LOAD_GLOBAL             11 (_safe_int + NULL)
              LOAD_FAST_BORROW         0 (recovery_report)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               7 ('skipped_count')
              CALL                     1
              CALL                     1
              STORE_FAST               6 (skipped)

453           LOAD_GLOBAL             11 (_safe_int + NULL)
              LOAD_FAST_BORROW         0 (recovery_report)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               8 ('failed_count')
              CALL                     1
              CALL                     1
              STORE_FAST               7 (failed)

455           LOAD_FAST_BORROW         2 (mode)
              LOAD_CONST               9 ('execute')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST              10 (':wrench:')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST              11 (':mag:')
      L4:     STORE_FAST               8 (emoji)

458           LOAD_CONST              12 ('type')
              LOAD_CONST              13 ('header')

459           LOAD_CONST              14 ('text')

460           LOAD_CONST              12 ('type')
              LOAD_CONST              15 ('plain_text')

461           LOAD_CONST              14 ('text')
              LOAD_FAST_BORROW         8 (emoji)
              FORMAT_SIMPLE
              LOAD_CONST              16 (' PAS stale-DIALING recovery')
              BUILD_STRING             2

459           BUILD_MAP                2

457           BUILD_MAP                2

465           LOAD_CONST              12 ('type')
              LOAD_CONST              17 ('context')

466           LOAD_CONST              18 ('elements')

467           LOAD_CONST              12 ('type')
              LOAD_CONST              19 ('mrkdwn')
              LOAD_CONST              14 ('text')
              LOAD_GLOBAL             13 (_scope_label + NULL)
              LOAD_FAST_BORROW         1 (brokerage_id)
              CALL                     1
              BUILD_MAP                2

466           BUILD_LIST               1

464           BUILD_MAP                2

471           LOAD_CONST              12 ('type')
              LOAD_CONST              20 ('section')

472           LOAD_CONST              14 ('text')

473           LOAD_CONST              12 ('type')
              LOAD_CONST              19 ('mrkdwn')

474           LOAD_CONST              14 ('text')

475           LOAD_CONST              21 ('*Mode*: `')
              LOAD_FAST_BORROW         2 (mode)
              FORMAT_SIMPLE
              LOAD_CONST              22 ('`\n*Stale threshold*: `')

476           LOAD_FAST_BORROW         3 (threshold)
              FORMAT_SIMPLE
              LOAD_CONST              23 (' s`\n*Candidates*: `')

477           LOAD_FAST_BORROW         4 (candidate)
              FORMAT_SIMPLE
              LOAD_CONST              24 ('`')

475           BUILD_STRING             7

472           BUILD_MAP                2

470           BUILD_MAP                2

482           LOAD_CONST              12 ('type')
              LOAD_CONST              20 ('section')

483           LOAD_CONST              14 ('text')

484           LOAD_CONST              12 ('type')
              LOAD_CONST              19 ('mrkdwn')

485           LOAD_CONST              14 ('text')

486           LOAD_CONST              25 ('*Recovered*: `')
              LOAD_FAST_BORROW         5 (recovered)
              FORMAT_SIMPLE
              LOAD_CONST              26 ('`  *Skipped*: `')

487           LOAD_FAST_BORROW         6 (skipped)
              FORMAT_SIMPLE
              LOAD_CONST              27 ('`  *Failed*: `')

488           LOAD_FAST_BORROW         7 (failed)
              FORMAT_SIMPLE
              LOAD_CONST              24 ('`')

486           BUILD_STRING             7

483           BUILD_MAP                2

481           BUILD_MAP                2

456           BUILD_LIST               4
              STORE_FAST               9 (blocks)

493           LOAD_GLOBAL             15 (_finalise + NULL)
              LOAD_FAST_BORROW         9 (blocks)
              CALL                     1
              RETURN_VALUE
```
