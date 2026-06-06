# operator/daily_ops_checklist

- **pyc:** `app\services\operator\__pycache__\daily_ops_checklist.cpython-314.pyc`
- **expected source path (absent):** `app\services\operator/daily_ops_checklist.py`
- **co_filename (from bytecode):** `app\services\operator\daily_ops_checklist.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** operator

## Module docstring

```
PAS187 — Daily operator checklist runner (durable record).

Records each daily operator-driven checklist run per
brokerage (or fleet-wide). The runner is **operator-
triggered**; PAS187 ships NO scheduler / cron / autonomous
remediation.

Doctrine:

* **Operator-run only.** Every record is attributed to an
  actor (X-Admin-Key holder) who ran the checklist.
* **No autonomous remediation.** The checklist records WHAT
  was reviewed, not WHO acted on findings. Findings still
  flow through the existing operator-action dispatcher
  (PAS173) which is auth-gated and audit-logged.
* **Structural only.** ``build_daily_ops_checklist`` returns
  the planned checklist items as a closed envelope;
  ``complete_daily_ops_checklist`` records the operator's
  attestation. Neither call touches transcripts, leads, or
  any PII.
* **NEVER raises.** Any unexpected exception collapses to
  ``status="skipped"`` + ``error_code="unexpected:<TypeName>"``.
* **DB unavailable** -> ``status="skipped"`` + a warning;
  the in-memory plan is still returned so the operator can
  print it.

Public surface:

  * ``build_daily_ops_checklist(...)``
  * ``complete_daily_ops_checklist(...)``
  * ``daily_ops_checklist_report(...)``
  * ``fleet_daily_ops_summary(...)``
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `app.db.event_logger`, `app.db.supabase_client`, `date`, `datetime`, `get_supabase`, `log_event_bg`, `logging`, `timezone`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_derive_status`, `_emit_event`, `_final`, `_get_db`, `_now_iso`, `_project_row`, `_safe_actor_id`, `_safe_actor_type`, `_safe_bool`, `_safe_brokerage`, `_safe_count`, `_safe_notes`, `_safe_str`, `_scan_for_forbidden`, `_today_iso`, `build_daily_ops_checklist`, `complete_daily_ops_checklist`, `daily_ops_checklist_report`, `fleet_daily_ops_summary`

## Env-key candidates

`COMPLETED`, `FAILED`, `PARTIAL`, `PLANNED`, `SKIPPED`, `UNKNOWN`

## String constants (redacted where noted)

- '\nPAS187 — Daily operator checklist runner (durable record).\n\nRecords each daily operator-driven checklist run per\nbrokerage (or fleet-wide). The runner is **operator-\ntriggered**; PAS187 ships NO scheduler / cron / autonomous\nremediation.\n\nDoctrine:\n\n* **Operator-run only.** Every record is attributed to an\n  actor (X-Admin-Key holder) who ran the checklist.\n* **No autonomous remediation.** The checklist records WHAT\n  was reviewed, not WHO acted on findings. Findings still\n  flow through the existing operator-action dispatcher\n  (PAS173) which is auth-gated and audit-logged.\n* **Structural only.** ``build_daily_ops_checklist`` returns\n  the planned checklist items as a closed envelope;\n  ``complete_daily_ops_checklist`` records the operator\'s\n  attestation. Neither call touches transcripts, leads, or\n  any PII.\n* **NEVER raises.** Any unexpected exception collapses to\n  ``status="skipped"`` + ``error_code="unexpected:<TypeName>"``.\n* **DB unavailable** -> ``status="skipped"`` + a warning;\n  the in-memory plan is still returned so the operator can\n  print it.\n\nPublic surface:\n\n  * ``build_daily_ops_checklist(...)``\n  * ``complete_daily_ops_checklist(...)``\n  * ``daily_ops_checklist_report(...)``\n  * ``fleet_daily_ops_summary(...)``\n'
- 'pas.operator.daily_ops_checklist'
- 'pas_daily_ops_checklist_runs'
- 'PLANNED'
- 'COMPLETED'
- 'PARTIAL'
- 'FAILED'
- 'SKIPPED'
- 'Tuple[Tuple[str, str], ...]'
- '_CHECKLIST_ITEMS'
- 'brokerage_id'
- 'run_date'
- 'queue_checked'
- 'callbacks_checked'
- 'bookings_checked'
- 'audit_checked'
- 'learning_checked'
- 'security_checked'
- 'incident_count'
- 'warning_count'
- 'notes'
- 'limit'
- 'return'
- 'str'
- 'seconds'
- 'value'
- 'Any'
- 'max_len'
- 'int'
- 'Optional[str]'
- 'bool'
- 'true'
- 'envelope'
- 'obj'
- 'env'
- 'Dict[str, Any]'
- 'surface'
- 'daily_ops_checklist surface='
- ' collapsed — forbidden token leaked'
- 'status'
- 'failed'
- 'error_code'
- 'daily_ops_envelope_forbidden_token'
- 'warnings'
- 'row'
- 'event_type'
- 'payload'
- 'None'
- 'all_present'
- 'any_present'
- 'Deterministic in-memory checklist plan. Does NOT\ntouch the DB. Returns the same structural shape every\ntime for the same (brokerage, date) tuple.'
- 'ops.daily_checklist.build'
- 'key'
- 'label'
- 'section_ref'
- 'docs/orvn_daily_pilot_operations_checklist.md#'
- 'items'
- 'build_daily_ops_checklist error type='
- 'skipped'
- 'unexpected:'
- 'actor_type'
- 'actor_id'
- "Persist the operator's attestation for today's\nchecklist. Status is derived from the boolean checks:\nall-true -> COMPLETED, some-true -> PARTIAL, all-false\n-> FAILED. The operator may explicitly pass status to\noverride (not currently exposed via the route; reserved\nfor the autonomous runner that does NOT exist in\nPAS187)."
- 'ops.daily_checklist.complete'
- 'invalid_actor'
- 'checklist_run_id'
- 'completed_at'
- 'completed_by_actor_type'
- 'completed_by_actor_id'
- 'notes_text'
- 'db_unavailable'
- 'metadata'
- 'complete_daily_ops_checklist insert error type='
- 'db_insert_failed:'
- 'daily_ops.checklist.completed'
- 'daily_ops.checklist.failed'
- 'complete_daily_ops_checklist error type='
- 'Read-only report of recent checklist runs. Bounded\nto the closed allow-list.'
- 'ops.daily_checklist.report'
- 'rows'
- 'count'
- 'daily_ops_checklist_report query error type='
- 'db_query_failed:'
- 'db_query_failed'
- 'data'
- 'daily_ops_checklist_report error type='
- "Aggregate today's most-recent checklist row per\nbrokerage. Used by the fleet operations dashboard\nsurface."
- 'ops.daily_checklist.fleet_summary'
- '<fleet>'
- 'UNKNOWN'
- 'by_status'
- 'fleet_daily_ops_summary error type='

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS187 — Daily operator checklist runner (durable record).\n\nRecords each daily operator-driven checklist run per\nbrokerage (or fleet-wide). The runner is **operator-\ntriggered**; PAS187 ships NO scheduler / cron / autonomous\nremediation.\n\nDoctrine:\n\n* **Operator-run only.** Every record is attributed to an\n  actor (X-Admin-Key holder) who ran the checklist.\n* **No autonomous remediation.** The checklist records WHAT\n  was reviewed, not WHO acted on findings. Findings still\n  flow through the existing operator-action dispatcher\n  (PAS173) which is auth-gated and audit-logged.\n* **Structural only.** ``build_daily_ops_checklist`` returns\n  the planned checklist items as a closed envelope;\n  ``complete_daily_ops_checklist`` records the operator\'s\n  attestation. Neither call touches transcripts, leads, or\n  any PII.\n* **NEVER raises.** Any unexpected exception collapses to\n  ``status="skipped"`` + ``error_code="unexpected:<TypeName>"``.\n* **DB unavailable** -> ``status="skipped"`` + a warning;\n  the in-memory plan is still returned so the operator can\n  print it.\n\nPublic surface:\n\n  * ``build_daily_ops_checklist(...)``\n  * ``complete_daily_ops_checklist(...)``\n  * ``daily_ops_checklist_report(...)``\n  * ``fleet_daily_ops_summary(...)``\n')
               STORE_NAME               1 (__doc__)

  36           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  38           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  39           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (uuid)
               STORE_NAME               5 (uuid)

  40           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('date', 'datetime', 'timezone'))
               IMPORT_NAME              6 (datetime)
               IMPORT_FROM              7 (date)
               STORE_NAME               7 (date)
               IMPORT_FROM              6 (datetime)
               STORE_NAME               6 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  41           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME              9 (typing)
               IMPORT_FROM             10 (Any)
               STORE_NAME              10 (Any)
               IMPORT_FROM             11 (Dict)
               STORE_NAME              11 (Dict)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               IMPORT_FROM             14 (Tuple)
               STORE_NAME              14 (Tuple)
               POP_TOP

  44           LOAD_NAME                4 (logging)
               LOAD_ATTR               30 (getLogger)
               PUSH_NULL
               LOAD_CONST               5 ('pas.operator.daily_ops_checklist')
               CALL                     1
               STORE_NAME              16 (logger)

  51           LOAD_CONST               6 ('pas_daily_ops_checklist_runs')
               STORE_NAME              17 (_TABLE_NAME)

  53           LOAD_CONST               7 ('PLANNED')
               STORE_NAME              18 (STATUS_PLANNED)

  54           LOAD_CONST               8 ('COMPLETED')
               STORE_NAME              19 (STATUS_COMPLETED)

  55           LOAD_CONST               9 ('PARTIAL')
               STORE_NAME              20 (STATUS_PARTIAL)

  56           LOAD_CONST              10 ('FAILED')
               STORE_NAME              21 (STATUS_FAILED)

  57           LOAD_CONST              11 ('SKIPPED')
               STORE_NAME              22 (STATUS_SKIPPED)

  59           LOAD_NAME               23 (frozenset)
               PUSH_NULL

  60           LOAD_NAME               18 (STATUS_PLANNED)

  61           LOAD_NAME               19 (STATUS_COMPLETED)

  62           LOAD_NAME               20 (STATUS_PARTIAL)

  63           LOAD_NAME               21 (STATUS_FAILED)

  64           LOAD_NAME               22 (STATUS_SKIPPED)

  59           BUILD_SET                5
               CALL                     1
               STORE_NAME              24 (_VALID_STATUSES)

  72           LOAD_CONST              65 ((('queue', 'Queue-depth review'), ('callbacks', 'Callback review'), ('bookings', 'Booking review'), ('audit', 'Audit verification review'), ('learning', 'Learning recommendation review'), ('security', 'Rate-limit + verification-run review')))
               STORE_NAME              25 (_CHECKLIST_ITEMS)
               LOAD_CONST              12 ('Tuple[Tuple[str, str], ...]')
               LOAD_NAME               26 (__annotations__)
               LOAD_CONST              13 ('_CHECKLIST_ITEMS')
               STORE_SUBSCR

  81           LOAD_CONST              66 (('checklist_run_id', 'brokerage_id', 'run_date', 'completed_at', 'completed_by_actor_type', 'completed_by_actor_id', 'status', 'queue_checked', 'callbacks_checked', 'bookings_checked', 'audit_checked', 'learning_checked', 'security_checked', 'incident_count', 'warning_count'))
               STORE_NAME              27 (_ROW_ALLOWLIST)

  99           LOAD_CONST              67 (('phone', 'email', 'name_token', 'transcript', 'raw_payload', 'raw_email', 'raw_body', 'secret', 'signature', 'dedupe_key', 'api_key', 'token', 'stack_trace', 'prompt_text', 'env_values'))
               STORE_NAME              28 (_FORBIDDEN_RESPONSE_TOKENS)

 106           LOAD_SMALL_INT         200
               STORE_NAME              29 (_BROKERAGE_ID_MAX_LEN)

 107           LOAD_SMALL_INT         200
               STORE_NAME              30 (_ACTOR_ID_MAX_LEN)

 108           LOAD_CONST              24 (2048)
               STORE_NAME              31 (_NOTES_MAX_LEN)

 115           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA3960, file "app\services\operator\daily_ops_checklist.py", line 115>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object _now_iso at 0x0000018C18038CB0, file "app\services\operator\daily_ops_checklist.py", line 115>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_now_iso)

 119           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA2C40, file "app\services\operator\daily_ops_checklist.py", line 119>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object _today_iso at 0x0000018C180532D0, file "app\services\operator\daily_ops_checklist.py", line 119>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              33 (_today_iso)

 123           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\operator\daily_ops_checklist.py", line 123>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object _safe_str at 0x0000018C17972550, file "app\services\operator\daily_ops_checklist.py", line 123>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_safe_str)

 132           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA32D0, file "app\services\operator\daily_ops_checklist.py", line 132>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object _safe_brokerage at 0x0000018C18024F30, file "app\services\operator\daily_ops_checklist.py", line 132>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (_safe_brokerage)

 136           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\operator\daily_ops_checklist.py", line 136>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object _safe_actor_id at 0x0000018C18025030, file "app\services\operator\daily_ops_checklist.py", line 136>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              36 (_safe_actor_id)

 140           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C17FA2100, file "app\services\operator\daily_ops_checklist.py", line 140>)
               MAKE_FUNCTION
               LOAD_CONST              36 (<code object _safe_actor_type at 0x0000018C18038670, file "app\services\operator\daily_ops_checklist.py", line 140>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              37 (_safe_actor_type)

 150           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C17FA2970, file "app\services\operator\daily_ops_checklist.py", line 150>)
               MAKE_FUNCTION
               LOAD_CONST              38 (<code object _safe_count at 0x0000018C17FE1530, file "app\services\operator\daily_ops_checklist.py", line 150>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (_safe_count)

 162           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C17FA23D0, file "app\services\operator\daily_ops_checklist.py", line 162>)
               MAKE_FUNCTION
               LOAD_CONST              40 (<code object _safe_bool at 0x0000018C17FF13B0, file "app\services\operator\daily_ops_checklist.py", line 162>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              39 (_safe_bool)

 170           LOAD_CONST              41 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\operator\daily_ops_checklist.py", line 170>)
               MAKE_FUNCTION
               LOAD_CONST              42 (<code object _safe_notes at 0x0000018C17FF0DB0, file "app\services\operator\daily_ops_checklist.py", line 170>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              40 (_safe_notes)

 183           LOAD_CONST              43 (<code object __annotate__ at 0x0000018C17FA2D30, file "app\services\operator\daily_ops_checklist.py", line 183>)
               MAKE_FUNCTION
               LOAD_CONST              44 (<code object _scan_for_forbidden at 0x0000018C18026130, file "app\services\operator\daily_ops_checklist.py", line 183>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (_scan_for_forbidden)

 207           LOAD_CONST              45 (<code object __annotate__ at 0x0000018C18026230, file "app\services\operator\daily_ops_checklist.py", line 207>)
               MAKE_FUNCTION
               LOAD_CONST              46 (<code object _final at 0x0000018C17FE17D0, file "app\services\operator\daily_ops_checklist.py", line 207>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (_final)

 223           LOAD_CONST              47 (<code object __annotate__ at 0x0000018C17FA21F0, file "app\services\operator\daily_ops_checklist.py", line 223>)
               MAKE_FUNCTION
               LOAD_CONST              48 (<code object _project_row at 0x0000018C18053090, file "app\services\operator\daily_ops_checklist.py", line 223>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_project_row)

 231           LOAD_CONST              49 (<code object __annotate__ at 0x0000018C18026330, file "app\services\operator\daily_ops_checklist.py", line 231>)
               MAKE_FUNCTION
               LOAD_CONST              50 (<code object _emit_event at 0x0000018C18038170, file "app\services\operator\daily_ops_checklist.py", line 231>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_emit_event)

 242           LOAD_CONST              51 (<code object _get_db at 0x0000018C18053CF0, file "app\services\operator\daily_ops_checklist.py", line 242>)
               MAKE_FUNCTION
               STORE_NAME              45 (_get_db)

 250           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C18026430, file "app\services\operator\daily_ops_checklist.py", line 250>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object _derive_status at 0x0000018C180531B0, file "app\services\operator\daily_ops_checklist.py", line 250>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (_derive_status)

 262           LOAD_CONST              14 ('brokerage_id')

 264           LOAD_CONST               2 (None)

 262           LOAD_CONST              15 ('run_date')

 265           LOAD_CONST               2 (None)

 262           BUILD_MAP                2
               LOAD_CONST              54 (<code object __annotate__ at 0x0000018C18026530, file "app\services\operator\daily_ops_checklist.py", line 262>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object build_daily_ops_checklist at 0x0000018C17CD4970, file "app\services\operator\daily_ops_checklist.py", line 262>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              47 (build_daily_ops_checklist)

 304           LOAD_CONST              14 ('brokerage_id')

 306           LOAD_CONST               2 (None)

 304           LOAD_CONST              15 ('run_date')

 307           LOAD_CONST               2 (None)

 304           LOAD_CONST              16 ('queue_checked')

 310           LOAD_CONST              56 (False)

 304           LOAD_CONST              17 ('callbacks_checked')

 311           LOAD_CONST              56 (False)

 304           LOAD_CONST              18 ('bookings_checked')

 312           LOAD_CONST              56 (False)

 304           LOAD_CONST              19 ('audit_checked')

 313           LOAD_CONST              56 (False)

 304           LOAD_CONST              20 ('learning_checked')

 314           LOAD_CONST              56 (False)

 304           LOAD_CONST              21 ('security_checked')

 315           LOAD_CONST              56 (False)

 304           LOAD_CONST              22 ('incident_count')

 316           LOAD_SMALL_INT           0

 304           LOAD_CONST              23 ('warning_count')

 317           LOAD_SMALL_INT           0

 304           LOAD_CONST              57 ('notes')

 318           LOAD_CONST               2 (None)

 304           BUILD_MAP               11
               LOAD_CONST              58 (<code object __annotate__ at 0x0000018C180533F0, file "app\services\operator\daily_ops_checklist.py", line 304>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object complete_daily_ops_checklist at 0x0000018C181A10A0, file "app\services\operator\daily_ops_checklist.py", line 304>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              48 (complete_daily_ops_checklist)

 415           LOAD_CONST              14 ('brokerage_id')

 417           LOAD_CONST               2 (None)

 415           LOAD_CONST              60 ('limit')

 418           LOAD_SMALL_INT          30

 415           BUILD_MAP                2
               LOAD_CONST              61 (<code object __annotate__ at 0x0000018C18026630, file "app\services\operator\daily_ops_checklist.py", line 415>)
               MAKE_FUNCTION
               LOAD_CONST              62 (<code object daily_ops_checklist_report at 0x0000018C17D7C9E0, file "app\services\operator\daily_ops_checklist.py", line 415>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              49 (daily_ops_checklist_report)

 484           LOAD_CONST              60 ('limit')

 486           LOAD_SMALL_INT         100

 484           BUILD_MAP                1
               LOAD_CONST              63 (<code object __annotate__ at 0x0000018C17FA31E0, file "app\services\operator\daily_ops_checklist.py", line 484>)
               MAKE_FUNCTION
               LOAD_CONST              64 (<code object fleet_daily_ops_summary at 0x0000018C17EA5290, file "app\services\operator\daily_ops_checklist.py", line 484>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              50 (fleet_daily_ops_summary)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app\services\operator\daily_ops_checklist.py", line 115>:
115           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038CB0, file "app\services\operator\daily_ops_checklist.py", line 115>:
115           RESUME                   0

116           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app\services\operator\daily_ops_checklist.py", line 119>:
119           RESUME                   0
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

Disassembly of <code object _today_iso at 0x0000018C180532D0, file "app\services\operator\daily_ops_checklist.py", line 119>:
119           RESUME                   0

120           LOAD_GLOBAL              0 (date)
              LOAD_ATTR                2 (today)
              PUSH_NULL
              CALL                     0
              LOAD_ATTR                5 (isoformat + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\operator\daily_ops_checklist.py", line 123>:
123           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('max_len')
              LOAD_CONST               4 ('int')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Optional[str]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _safe_str at 0x0000018C17972550, file "app\services\operator\daily_ops_checklist.py", line 123>:
123           RESUME                   0

124           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

125           LOAD_CONST               0 (None)
              RETURN_VALUE

126   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (s)

127           LOAD_FAST_BORROW         2 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         2 (s)
              CALL                     1
              LOAD_FAST_BORROW         1 (max_len)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

128   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

129   L3:     LOAD_FAST_BORROW         2 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "app\services\operator\daily_ops_checklist.py", line 132>:
132           RESUME                   0
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
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_brokerage at 0x0000018C18024F30, file "app\services\operator\daily_ops_checklist.py", line 132>:
132           RESUME                   0

133           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (_BROKERAGE_ID_MAX_LEN)
              CALL                     2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\operator\daily_ops_checklist.py", line 136>:
136           RESUME                   0
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
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_actor_id at 0x0000018C18025030, file "app\services\operator\daily_ops_checklist.py", line 136>:
136           RESUME                   0

137           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (_ACTOR_ID_MAX_LEN)
              CALL                     2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app\services\operator\daily_ops_checklist.py", line 140>:
140           RESUME                   0
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
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_actor_type at 0x0000018C18038670, file "app\services\operator\daily_ops_checklist.py", line 140>:
140           RESUME                   0

141           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_SMALL_INT          32
              CALL                     2
              STORE_FAST               1 (s)

142           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

143           LOAD_CONST               1 (None)
              RETURN_VALUE

144   L1:     LOAD_FAST_BORROW         1 (s)
              LOAD_ATTR                3 (upper + NULL|self)
              CALL                     0
              STORE_FAST               2 (up)

145           LOAD_FAST_BORROW         2 (up)
              LOAD_CONST               2 (('ADMIN', 'OPERATOR'))
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

146           LOAD_CONST               1 (None)
              RETURN_VALUE

147   L2:     LOAD_FAST_BORROW         2 (up)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app\services\operator\daily_ops_checklist.py", line 150>:
150           RESUME                   0
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
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_count at 0x0000018C17FE1530, file "app\services\operator\daily_ops_checklist.py", line 150>:
 150           RESUME                   0

 151           NOP

 152   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (v)

 155   L2:     LOAD_FAST                1 (v)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 156           LOAD_SMALL_INT           0
               RETURN_VALUE

 157   L3:     LOAD_FAST                1 (v)
               LOAD_CONST               1 (1000000)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 158           LOAD_CONST               1 (1000000)
               RETURN_VALUE

 159   L4:     LOAD_FAST                1 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 153           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L7)
               NOT_TAKEN
               POP_TOP

 154   L6:     POP_EXCEPT
               LOAD_SMALL_INT           0
               RETURN_VALUE

 153   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app\services\operator\daily_ops_checklist.py", line 162>:
162           RESUME                   0
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
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_bool at 0x0000018C17FF13B0, file "app\services\operator\daily_ops_checklist.py", line 162>:
162           RESUME                   0

163           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (bool)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

164           LOAD_FAST_BORROW         0 (value)
              RETURN_VALUE

165   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              4 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       34 (to L2)
              NOT_TAKEN

166           LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                7 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR                9 (lower + NULL|self)
              CALL                     0
              LOAD_CONST               2 (('true', '1', 'yes', 'y'))
              CONTAINS_OP              0 (in)
              RETURN_VALUE

167   L2:     LOAD_CONST               1 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\operator\daily_ops_checklist.py", line 170>:
170           RESUME                   0
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
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_notes at 0x0000018C17FF0DB0, file "app\services\operator\daily_ops_checklist.py", line 170>:
170           RESUME                   0

171           LOAD_FAST_BORROW         0 (value)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

172           LOAD_CONST               0 (None)
              RETURN_VALUE

173   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

174           LOAD_CONST               0 (None)
              RETURN_VALUE

175   L2:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

176           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

177           LOAD_CONST               0 (None)
              RETURN_VALUE

178   L3:     LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_NOTES_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       10 (to L4)
              NOT_TAKEN

179           LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               0 (None)
              LOAD_GLOBAL              8 (_NOTES_MAX_LEN)
              BINARY_SLICE
              STORE_FAST               1 (s)

180   L4:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app\services\operator\daily_ops_checklist.py", line 183>:
183           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('envelope')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _scan_for_forbidden at 0x0000018C18026130, file "app\services\operator\daily_ops_checklist.py", line 183>:
  --           MAKE_CELL                1 (walk)

 183           RESUME                   0

 184           LOAD_CONST               0 (<code object __annotate__ at 0x0000018C17FA2E20, file "app\services\operator\daily_ops_checklist.py", line 184>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object walk at 0x0000018C17CC1CE0, file "app\services\operator\daily_ops_checklist.py", line 184>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

 204           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app\services\operator\daily_ops_checklist.py", line 184>:
184           RESUME                   0
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
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object walk at 0x0000018C17CC1CE0, file "app\services\operator\daily_ops_checklist.py", line 184>:
  --            COPY_FREE_VARS           1

 184            RESUME                   0

 185            NOP

 186    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      111 (to L16)
        L2:     NOT_TAKEN

 187    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                88 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

 188            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L10)
                NOT_TAKEN

 189            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

 190            LOAD_GLOBAL             10 (_FORBIDDEN_RESPONSE_TOKENS)
                GET_ITER
        L5:     FOR_ITER                15 (to L9)
                STORE_FAST               4 (tok)

 191            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)

 192    L7:     LOAD_FAST_BORROW         4 (tok)
                SWAP                     2
                POP_TOP
                SWAP                     2
                POP_TOP
        L8:     RETURN_VALUE

 190    L9:     END_FOR
                POP_ITER

 193   L10:     LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 194            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           86 (to L4)

 195   L12:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L13:     RETURN_VALUE

 187   L14:     END_FOR
                POP_ITER

 203   L15:     LOAD_CONST               0 (None)
                RETURN_VALUE

 196   L16:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             12 (list)
                LOAD_GLOBAL             14 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L22)
                NOT_TAKEN

 197            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L17:     FOR_ITER                23 (to L21)
                STORE_FAST               2 (v)

 198            LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 199            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           21 (to L17)

 200   L19:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L20:     RETURN_VALUE

 197   L21:     END_FOR
                POP_ITER

 203   L22:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 201            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L25)
                NOT_TAKEN
                POP_TOP

 202   L24:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 201   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L23 [0]
  L3 to L6 -> L23 [0]
  L7 to L8 -> L23 [0]
  L9 to L11 -> L23 [0]
  L12 to L13 -> L23 [0]
  L14 to L15 -> L23 [0]
  L16 to L18 -> L23 [0]
  L19 to L20 -> L23 [0]
  L21 to L22 -> L23 [0]
  L23 to L24 -> L26 [1] lasti
  L25 to L26 -> L26 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026230, file "app\services\operator\daily_ops_checklist.py", line 207>:
207           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('env')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('surface')
              LOAD_CONST               4 ('str')
              LOAD_CONST               5 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _final at 0x0000018C17FE17D0, file "app\services\operator\daily_ops_checklist.py", line 207>:
207           RESUME                   0

208           LOAD_GLOBAL              1 (_scan_for_forbidden + NULL)
              LOAD_FAST_BORROW         0 (env)
              CALL                     1
              STORE_FAST               2 (leak)

209           LOAD_FAST_BORROW         2 (leak)
              TO_BOOL
              POP_JUMP_IF_FALSE       37 (to L1)
              NOT_TAKEN

210           LOAD_GLOBAL              2 (logger)
              LOAD_ATTR                5 (warning + NULL|self)

211           LOAD_CONST               0 ('daily_ops_checklist surface=')
              LOAD_FAST_BORROW         1 (surface)
              FORMAT_SIMPLE
              LOAD_CONST               1 (' collapsed — forbidden token leaked')
              BUILD_STRING             3

210           CALL                     1
              POP_TOP

215           LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('failed')

216           LOAD_CONST               4 ('surface')
              LOAD_FAST_BORROW         1 (surface)

217           LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('daily_ops_envelope_forbidden_token')

218           LOAD_CONST               7 ('warnings')
              LOAD_CONST               6 ('daily_ops_envelope_forbidden_token')
              BUILD_LIST               1

214           BUILD_MAP                4
              RETURN_VALUE

220   L1:     LOAD_FAST_BORROW         0 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app\services\operator\daily_ops_checklist.py", line 223>:
223           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _project_row at 0x0000018C18053090, file "app\services\operator\daily_ops_checklist.py", line 223>:
223           RESUME                   0

224           BUILD_MAP                0
              STORE_FAST               1 (out)

225           LOAD_GLOBAL              0 (_ROW_ALLOWLIST)
              GET_ITER
      L1:     FOR_ITER                21 (to L3)
              STORE_FAST               2 (k)

226           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L1)

227   L2:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, k)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, k)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L1)

225   L3:     END_FOR
              POP_ITER

228           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026330, file "app\services\operator\daily_ops_checklist.py", line 231>:
231           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('event_type')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('payload')
              LOAD_CONST               4 ('Dict[str, Any]')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('None')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _emit_event at 0x0000018C18038170, file "app\services\operator\daily_ops_checklist.py", line 231>:
 231            RESUME                   0

 232            NOP

 233    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('log_event_bg',))
                IMPORT_NAME              0 (app.db.event_logger)
                IMPORT_FROM              1 (log_event_bg)
                STORE_FAST               2 (log_event_bg)
                POP_TOP

 236    L2:     NOP

 237    L3:     LOAD_FAST                2 (log_event_bg)
                PUSH_NULL
                LOAD_FAST_LOAD_FAST      1 (event_type, payload)
                CALL                     2
                POP_TOP
        L4:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 234            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L7)
                NOT_TAKEN
                POP_TOP

 235    L6:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 234    L7:     RERAISE                  0

  --    L8:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
        L9:     PUSH_EXC_INFO

 238            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L11)
                NOT_TAKEN
                POP_TOP

 239   L10:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 238   L11:     RERAISE                  0

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L3 to L4 -> L9 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti
  L9 to L10 -> L12 [1] lasti
  L11 to L12 -> L12 [1] lasti

Disassembly of <code object _get_db at 0x0000018C18053CF0, file "app\services\operator\daily_ops_checklist.py", line 242>:
 242           RESUME                   0

 243           NOP

 244   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 245           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 246           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 247   L4:     POP_EXCEPT
               LOAD_CONST               2 (None)
               RETURN_VALUE

 246   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "app\services\operator\daily_ops_checklist.py", line 250>:
250           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('all_present')
              LOAD_CONST               2 ('bool')
              LOAD_CONST               3 ('any_present')
              LOAD_CONST               2 ('bool')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('str')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _derive_status at 0x0000018C180531B0, file "app\services\operator\daily_ops_checklist.py", line 250>:
250           RESUME                   0

251           LOAD_FAST_BORROW         0 (all_present)
              TO_BOOL
              POP_JUMP_IF_FALSE        7 (to L1)
              NOT_TAKEN

252           LOAD_GLOBAL              0 (STATUS_COMPLETED)
              RETURN_VALUE

253   L1:     LOAD_FAST_BORROW         1 (any_present)
              TO_BOOL
              POP_JUMP_IF_FALSE        7 (to L2)
              NOT_TAKEN

254           LOAD_GLOBAL              2 (STATUS_PARTIAL)
              RETURN_VALUE

255   L2:     LOAD_GLOBAL              4 (STATUS_FAILED)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026530, file "app\services\operator\daily_ops_checklist.py", line 262>:
262           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

264           LOAD_CONST               2 ('Any')

262           LOAD_CONST               3 ('run_date')

265           LOAD_CONST               2 ('Any')

262           LOAD_CONST               4 ('return')

266           LOAD_CONST               5 ('Dict[str, Any]')

262           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object build_daily_ops_checklist at 0x0000018C17CD4970, file "app\services\operator\daily_ops_checklist.py", line 262>:
 262            RESUME                   0

 270            LOAD_CONST               1 ('ops.daily_checklist.build')
                STORE_FAST               2 (surface)

 271            NOP

 272    L1:     LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               2 (None)
        L3:     STORE_FAST               3 (bid)

 273            LOAD_FAST_BORROW         1 (run_date)
                POP_JUMP_IF_NONE        13 (to L4)
                NOT_TAKEN
                LOAD_GLOBAL              3 (_safe_str + NULL)
                LOAD_FAST_BORROW         1 (run_date)
                LOAD_SMALL_INT          32
                CALL                     2
                JUMP_FORWARD             9 (to L5)
        L4:     LOAD_GLOBAL              5 (_today_iso + NULL)
                CALL                     0
        L5:     STORE_FAST               4 (rdate)

 280            LOAD_GLOBAL              7 (enumerate + NULL)
                LOAD_GLOBAL              8 (_CHECKLIST_ITEMS)
                CALL                     1
                GET_ITER

 274            LOAD_FAST_AND_CLEAR      5 (i)
                LOAD_FAST_AND_CLEAR      6 (key)
                LOAD_FAST_AND_CLEAR      7 (label)
                SWAP                     4
        L6:     BUILD_LIST               0
                SWAP                     2

 280    L7:     FOR_ITER                26 (to L8)
                UNPACK_SEQUENCE          2
                STORE_FAST               5 (i)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  103 (key, label)

 276            LOAD_CONST               3 ('key')
                LOAD_FAST_BORROW         6 (key)

 277            LOAD_CONST               4 ('label')
                LOAD_FAST_BORROW         7 (label)

 278            LOAD_CONST               5 ('section_ref')
                LOAD_CONST               6 ('docs/orvn_daily_pilot_operations_checklist.md#')
                LOAD_FAST_BORROW         5 (i)
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                FORMAT_SIMPLE
                BUILD_STRING             2

 275            BUILD_MAP                3
                LIST_APPEND              2
                JUMP_BACKWARD           28 (to L7)

 280    L8:     END_FOR
                POP_ITER

 274    L9:     STORE_FAST               8 (items)
                STORE_FAST               6 (key)
                STORE_FAST               5 (i)
                STORE_FAST               7 (label)

 282            LOAD_GLOBAL             11 (_final + NULL)

 283            LOAD_CONST               7 ('status')
                LOAD_CONST               8 ('ok')

 284            LOAD_CONST               9 ('surface')
                LOAD_FAST_BORROW         2 (surface)

 285            LOAD_CONST              10 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)

 286            LOAD_CONST              11 ('run_date')
                LOAD_FAST_BORROW         4 (rdate)

 287            LOAD_CONST              12 ('items')
                LOAD_FAST_BORROW         8 (items)

 288            LOAD_CONST              13 ('warnings')
                BUILD_LIST               0

 289            LOAD_CONST              14 ('error_code')
                LOAD_CONST               2 (None)

 282            BUILD_MAP                7

 290            LOAD_FAST_BORROW         2 (surface)

 282            LOAD_CONST              15 (('surface',))
                CALL_KW                  2
       L10:     RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 274            SWAP                     4
                STORE_FAST               7 (label)
                STORE_FAST               6 (key)
                STORE_FAST               5 (i)
                RERAISE                  0

  --   L12:     PUSH_EXC_INFO

 291            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       99 (to L17)
                NOT_TAKEN
                STORE_FAST               9 (e)

 292   L13:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 293            LOAD_CONST              16 ('build_daily_ops_checklist error type=')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 292            CALL                     1
                POP_TOP

 295            LOAD_GLOBAL             11 (_final + NULL)

 296            LOAD_CONST               7 ('status')
                LOAD_CONST              17 ('skipped')

 297            LOAD_CONST               9 ('surface')
                LOAD_FAST                2 (surface)

 298            LOAD_CONST              12 ('items')
                BUILD_LIST               0

 299            LOAD_CONST              13 ('warnings')
                BUILD_LIST               0

 300            LOAD_CONST              14 ('error_code')
                LOAD_CONST              18 ('unexpected:')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 295            BUILD_MAP                5

 301            LOAD_FAST                2 (surface)

 295            LOAD_CONST              15 (('surface',))
                CALL_KW                  2
       L14:     SWAP                     2
       L15:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RETURN_VALUE

  --   L16:     LOAD_CONST               2 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 291   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L6 -> L12 [0]
  L6 to L9 -> L11 [4]
  L9 to L10 -> L12 [0]
  L11 to L12 -> L12 [0]
  L12 to L13 -> L18 [1] lasti
  L13 to L14 -> L16 [1] lasti
  L14 to L15 -> L18 [1] lasti
  L16 to L18 -> L18 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C180533F0, file "app\services\operator\daily_ops_checklist.py", line 304>:
304           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

306           LOAD_CONST               2 ('Any')

304           LOAD_CONST               3 ('run_date')

307           LOAD_CONST               2 ('Any')

304           LOAD_CONST               4 ('actor_type')

308           LOAD_CONST               2 ('Any')

304           LOAD_CONST               5 ('actor_id')

309           LOAD_CONST               2 ('Any')

304           LOAD_CONST               6 ('queue_checked')

310           LOAD_CONST               2 ('Any')

304           LOAD_CONST               7 ('callbacks_checked')

311           LOAD_CONST               2 ('Any')

304           LOAD_CONST               8 ('bookings_checked')

312           LOAD_CONST               2 ('Any')

304           LOAD_CONST               9 ('audit_checked')

313           LOAD_CONST               2 ('Any')

304           LOAD_CONST              10 ('learning_checked')

314           LOAD_CONST               2 ('Any')

304           LOAD_CONST              11 ('security_checked')

315           LOAD_CONST               2 ('Any')

304           LOAD_CONST              12 ('incident_count')

316           LOAD_CONST               2 ('Any')

304           LOAD_CONST              13 ('warning_count')

317           LOAD_CONST               2 ('Any')

304           LOAD_CONST              14 ('notes')

318           LOAD_CONST               2 ('Any')

304           LOAD_CONST              15 ('return')

319           LOAD_CONST              16 ('Dict[str, Any]')

304           BUILD_MAP               14
              RETURN_VALUE

Disassembly of <code object complete_daily_ops_checklist at 0x0000018C181A10A0, file "app\services\operator\daily_ops_checklist.py", line 304>:
 304            RESUME                   0

 327            LOAD_CONST               1 ('ops.daily_checklist.complete')
                STORE_FAST              13 (surface)

 328            NOP

 329    L1:     LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               2 (None)
        L3:     STORE_FAST              14 (bid)

 330            LOAD_FAST_BORROW         1 (run_date)
                POP_JUMP_IF_NONE        13 (to L4)
                NOT_TAKEN
                LOAD_GLOBAL              3 (_safe_str + NULL)
                LOAD_FAST_BORROW         1 (run_date)
                LOAD_SMALL_INT          32
                CALL                     2
                JUMP_FORWARD             9 (to L5)
        L4:     LOAD_GLOBAL              5 (_today_iso + NULL)
                CALL                     0
        L5:     STORE_FAST              15 (rdate)

 331            LOAD_GLOBAL              7 (_safe_actor_type + NULL)
                LOAD_FAST_BORROW         2 (actor_type)
                CALL                     1
                STORE_FAST              16 (atype)

 332            LOAD_GLOBAL              9 (_safe_actor_id + NULL)
                LOAD_FAST_BORROW         3 (actor_id)
                CALL                     1
                STORE_FAST              17 (aid)

 333            LOAD_FAST_BORROW        16 (atype)
                TO_BOOL
                POP_JUMP_IF_FALSE        9 (to L7)
                NOT_TAKEN
                LOAD_FAST_BORROW        17 (aid)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L9)
        L6:     NOT_TAKEN

 334    L7:     LOAD_GLOBAL             11 (_final + NULL)

 335            LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('failed')

 336            LOAD_CONST               5 ('surface')
                LOAD_FAST_BORROW        13 (surface)

 337            LOAD_CONST               6 ('error_code')
                LOAD_CONST               7 ('invalid_actor')

 338            LOAD_CONST               8 ('warnings')
                LOAD_CONST               7 ('invalid_actor')
                BUILD_LIST               1

 334            BUILD_MAP                4

 339            LOAD_FAST_BORROW        13 (surface)

 334            LOAD_CONST               9 (('surface',))
                CALL_KW                  2
        L8:     RETURN_VALUE

 341    L9:     LOAD_CONST              10 ('queue_checked')
                LOAD_GLOBAL             13 (_safe_bool + NULL)
                LOAD_FAST_BORROW         4 (queue_checked)
                CALL                     1

 342            LOAD_CONST              11 ('callbacks_checked')
                LOAD_GLOBAL             13 (_safe_bool + NULL)
                LOAD_FAST_BORROW         5 (callbacks_checked)
                CALL                     1

 343            LOAD_CONST              12 ('bookings_checked')
                LOAD_GLOBAL             13 (_safe_bool + NULL)
                LOAD_FAST_BORROW         6 (bookings_checked)
                CALL                     1

 344            LOAD_CONST              13 ('audit_checked')
                LOAD_GLOBAL             13 (_safe_bool + NULL)
                LOAD_FAST_BORROW         7 (audit_checked)
                CALL                     1

 345            LOAD_CONST              14 ('learning_checked')
                LOAD_GLOBAL             13 (_safe_bool + NULL)
                LOAD_FAST_BORROW         8 (learning_checked)
                CALL                     1

 346            LOAD_CONST              15 ('security_checked')
                LOAD_GLOBAL             13 (_safe_bool + NULL)
                LOAD_FAST_BORROW         9 (security_checked)
                CALL                     1

 340            BUILD_MAP                6
                STORE_FAST              18 (flags)

 348            LOAD_GLOBAL             15 (all + NULL)
                LOAD_FAST_BORROW        18 (flags)
                LOAD_ATTR               17 (values + NULL|self)
                CALL                     0
                CALL                     1
                STORE_FAST              19 (all_present)

 349            LOAD_GLOBAL             19 (any + NULL)
                LOAD_FAST_BORROW        18 (flags)
                LOAD_ATTR               17 (values + NULL|self)
                CALL                     0
                CALL                     1
                STORE_FAST              20 (any_present)

 350            LOAD_GLOBAL             21 (_derive_status + NULL)
                LOAD_FAST_BORROW        19 (all_present)
                LOAD_FAST_BORROW        20 (any_present)
                LOAD_CONST              16 (('all_present', 'any_present'))
                CALL_KW                  2
                STORE_FAST              21 (derived)

 351            LOAD_GLOBAL             23 (_safe_count + NULL)
                LOAD_FAST_BORROW        10 (incident_count)
                CALL                     1
                STORE_FAST              22 (incidents)

 352            LOAD_GLOBAL             23 (_safe_count + NULL)
                LOAD_FAST_BORROW        11 (warning_count)
                CALL                     1
                STORE_FAST              23 (warns)

 353            LOAD_GLOBAL             25 (_safe_notes + NULL)
                LOAD_FAST_BORROW        12 (notes)
                CALL                     1
                STORE_FAST              24 (notes_text)

 355            LOAD_CONST              17 ('checklist_run_id')
                LOAD_GLOBAL             27 (str + NULL)
                LOAD_GLOBAL             28 (uuid)
                LOAD_ATTR               30 (uuid4)
                PUSH_NULL
                CALL                     0
                CALL                     1

 356            LOAD_CONST              18 ('brokerage_id')
                LOAD_FAST_BORROW        14 (bid)

 357            LOAD_CONST              19 ('run_date')
                LOAD_FAST_BORROW        15 (rdate)

 358            LOAD_CONST              20 ('completed_at')
                LOAD_GLOBAL             33 (_now_iso + NULL)
                CALL                     0

 359            LOAD_CONST              21 ('completed_by_actor_type')
                LOAD_FAST_BORROW        16 (atype)

 360            LOAD_CONST              22 ('completed_by_actor_id')
                LOAD_FAST_BORROW        17 (aid)

 361            LOAD_CONST               3 ('status')
                LOAD_FAST_BORROW        21 (derived)

 354            BUILD_MAP                7

 362            LOAD_FAST_BORROW        18 (flags)

 354            DICT_UPDATE              1

 363            LOAD_CONST              23 ('incident_count')
                LOAD_FAST_BORROW        22 (incidents)

 364            LOAD_CONST              24 ('warning_count')
                LOAD_FAST_BORROW        23 (warns)

 354            BUILD_MAP                2
                DICT_UPDATE              1
                STORE_FAST              25 (row)

 366            LOAD_FAST_BORROW        24 (notes_text)
                TO_BOOL
                POP_JUMP_IF_FALSE        5 (to L10)
                NOT_TAKEN
                LOAD_CONST              25 ('notes_text')
                LOAD_FAST_BORROW        24 (notes_text)
                BUILD_MAP                1
                JUMP_FORWARD             1 (to L11)
       L10:     BUILD_MAP                0
       L11:     STORE_FAST              26 (meta)

 367            LOAD_GLOBAL             35 (_get_db + NULL)
                CALL                     0
                STORE_FAST              27 (db)

 368            BUILD_LIST               0
                STORE_FAST              28 (warnings)

 369            LOAD_FAST_BORROW        27 (db)
                POP_JUMP_IF_NOT_NONE    21 (to L12)
                NOT_TAKEN

 370            LOAD_FAST_BORROW        28 (warnings)
                LOAD_ATTR               37 (append + NULL|self)
                LOAD_CONST              26 ('db_unavailable')
                CALL                     1
                POP_TOP

 371            LOAD_CONST              27 ('skipped')
                STORE_FAST              29 (db_status)
                JUMP_FORWARD            59 (to L14)

 373   L12:     NOP

 374   L13:     LOAD_FAST_BORROW        27 (db)
                LOAD_ATTR               39 (table + NULL|self)
                LOAD_GLOBAL             40 (_TABLE_NAME)
                CALL                     1
                LOAD_ATTR               43 (insert + NULL|self)
                BUILD_MAP                0
                LOAD_FAST_BORROW        25 (row)
                DICT_UPDATE              1
                LOAD_CONST              28 ('metadata')
                LOAD_FAST_BORROW        26 (meta)
                BUILD_MAP                1
                DICT_UPDATE              1
                CALL                     1
                LOAD_ATTR               45 (execute + NULL|self)
                CALL                     0
                POP_TOP

 375            LOAD_CONST              29 ('ok')
                STORE_FAST              29 (db_status)

 383   L14:     LOAD_GLOBAL             57 (_emit_event + NULL)

 384            LOAD_FAST_BORROW        21 (derived)
                LOAD_GLOBAL             58 (STATUS_COMPLETED)
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN
                LOAD_CONST              32 ('daily_ops.checklist.completed')
                JUMP_FORWARD             1 (to L16)

 385   L15:     LOAD_CONST              33 ('daily_ops.checklist.failed')

 387   L16:     LOAD_CONST              18 ('brokerage_id')
                LOAD_FAST_BORROW        14 (bid)

 388            LOAD_CONST              17 ('checklist_run_id')
                LOAD_FAST_BORROW        25 (row)
                LOAD_CONST              17 ('checklist_run_id')
                BINARY_OP               26 ([])

 389            LOAD_CONST              34 ('actor_type')
                LOAD_FAST_BORROW        16 (atype)

 390            LOAD_CONST              35 ('actor_id')
                LOAD_FAST_BORROW        17 (aid)

 391            LOAD_CONST               3 ('status')
                LOAD_FAST_BORROW        21 (derived)

 392            LOAD_CONST              23 ('incident_count')
                LOAD_FAST_BORROW        22 (incidents)

 393            LOAD_CONST              24 ('warning_count')
                LOAD_FAST_BORROW        23 (warns)

 386            BUILD_MAP                7

 383            CALL                     2
                POP_TOP

 396            LOAD_GLOBAL             11 (_final + NULL)

 397            LOAD_CONST               3 ('status')
                LOAD_FAST_BORROW        29 (db_status)
                LOAD_CONST              29 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L17)
                NOT_TAKEN
                LOAD_CONST              29 ('ok')
                JUMP_FORWARD             1 (to L18)
       L17:     LOAD_CONST              27 ('skipped')

 398   L18:     LOAD_CONST               5 ('surface')
                LOAD_FAST               13 (surface)

 399            LOAD_CONST              36 ('row')
                LOAD_GLOBAL             61 (_project_row + NULL)
                LOAD_FAST_BORROW        25 (row)
                CALL                     1

 400            LOAD_CONST               8 ('warnings')
                LOAD_FAST               28 (warnings)

 401            LOAD_CONST               6 ('error_code')
                LOAD_FAST_BORROW        29 (db_status)
                LOAD_CONST              29 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L19)
                NOT_TAKEN
                LOAD_CONST               2 (None)
                JUMP_FORWARD             1 (to L20)
       L19:     LOAD_CONST              26 ('db_unavailable')

 396   L20:     BUILD_MAP                5

 402            LOAD_FAST_BORROW        13 (surface)

 396            LOAD_CONST               9 (('surface',))
                CALL_KW                  2
       L21:     RETURN_VALUE

  --   L22:     PUSH_EXC_INFO

 376            LOAD_GLOBAL             46 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       95 (to L26)
                NOT_TAKEN
                STORE_FAST              30 (e)

 377   L23:     LOAD_GLOBAL             48 (logger)
                LOAD_ATTR               51 (warning + NULL|self)

 378            LOAD_CONST              30 ('complete_daily_ops_checklist insert error type=')

 379            LOAD_GLOBAL             53 (type + NULL)
                LOAD_FAST               30 (e)
                CALL                     1
                LOAD_ATTR               54 (__name__)
                FORMAT_SIMPLE

 378            BUILD_STRING             2

 377            CALL                     1
                POP_TOP

 381            LOAD_FAST               28 (warnings)
                LOAD_ATTR               37 (append + NULL|self)
                LOAD_CONST              31 ('db_insert_failed:')
                LOAD_GLOBAL             53 (type + NULL)
                LOAD_FAST               30 (e)
                CALL                     1
                LOAD_ATTR               54 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 382            LOAD_CONST              27 ('skipped')
                STORE_FAST              29 (db_status)
       L24:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              30 (e)
                DELETE_FAST             30 (e)
                JUMP_BACKWARD_NO_INTERRUPT 196 (to L14)

  --   L25:     LOAD_CONST               2 (None)
                STORE_FAST              30 (e)
                DELETE_FAST             30 (e)
                RERAISE                  1

 376   L26:     RERAISE                  0

  --   L27:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L28:     PUSH_EXC_INFO

 403            LOAD_GLOBAL             46 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L33)
                NOT_TAKEN
                STORE_FAST              30 (e)

 404   L29:     LOAD_GLOBAL             48 (logger)
                LOAD_ATTR               51 (warning + NULL|self)

 405            LOAD_CONST              37 ('complete_daily_ops_checklist error type=')
                LOAD_GLOBAL             53 (type + NULL)
                LOAD_FAST               30 (e)
                CALL                     1
                LOAD_ATTR               54 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 404            CALL                     1
                POP_TOP

 407            LOAD_GLOBAL             11 (_final + NULL)

 408            LOAD_CONST               3 ('status')
                LOAD_CONST              27 ('skipped')

 409            LOAD_CONST               5 ('surface')
                LOAD_FAST               13 (surface)

 410            LOAD_CONST               6 ('error_code')
                LOAD_CONST              38 ('unexpected:')
                LOAD_GLOBAL             53 (type + NULL)
                LOAD_FAST               30 (e)
                CALL                     1
                LOAD_ATTR               54 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 411            LOAD_CONST               8 ('warnings')
                BUILD_LIST               0

 407            BUILD_MAP                4

 412            LOAD_FAST               13 (surface)

 407            LOAD_CONST               9 (('surface',))
                CALL_KW                  2
       L30:     SWAP                     2
       L31:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              30 (e)
                DELETE_FAST             30 (e)
                RETURN_VALUE

  --   L32:     LOAD_CONST               2 (None)
                STORE_FAST              30 (e)
                DELETE_FAST             30 (e)
                RERAISE                  1

 403   L33:     RERAISE                  0

  --   L34:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L6 -> L28 [0]
  L7 to L8 -> L28 [0]
  L9 to L12 -> L28 [0]
  L13 to L14 -> L22 [0]
  L14 to L21 -> L28 [0]
  L22 to L23 -> L27 [1] lasti
  L23 to L24 -> L25 [1] lasti
  L24 to L25 -> L28 [0]
  L25 to L27 -> L27 [1] lasti
  L27 to L28 -> L28 [0]
  L28 to L29 -> L34 [1] lasti
  L29 to L30 -> L32 [1] lasti
  L30 to L31 -> L34 [1] lasti
  L32 to L34 -> L34 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026630, file "app\services\operator\daily_ops_checklist.py", line 415>:
415           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

417           LOAD_CONST               2 ('Any')

415           LOAD_CONST               3 ('limit')

418           LOAD_CONST               2 ('Any')

415           LOAD_CONST               4 ('return')

419           LOAD_CONST               5 ('Dict[str, Any]')

415           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object daily_ops_checklist_report at 0x0000018C17D7C9E0, file "app\services\operator\daily_ops_checklist.py", line 415>:
 415            RESUME                   0

 422            LOAD_CONST               1 ('ops.daily_checklist.report')
                STORE_FAST               2 (surface)

 423            NOP

 424    L1:     LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               2 (None)
        L3:     STORE_FAST               3 (bid)

 425            LOAD_GLOBAL              3 (_safe_count + NULL)
                LOAD_FAST_BORROW         1 (limit)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
        L4:     NOT_TAKEN
        L5:     POP_TOP
                LOAD_SMALL_INT          30
        L6:     STORE_FAST               4 (cap)

 426            LOAD_FAST_BORROW         4 (cap)
                LOAD_SMALL_INT         200
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN

 427            LOAD_SMALL_INT         200
                STORE_FAST               4 (cap)

 428    L7:     LOAD_GLOBAL              5 (_get_db + NULL)
                CALL                     0
                STORE_FAST               5 (db)

 429            LOAD_FAST_BORROW         5 (db)
                POP_JUMP_IF_NOT_NONE    27 (to L9)
                NOT_TAKEN

 430            LOAD_GLOBAL              7 (_final + NULL)

 431            LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('skipped')

 432            LOAD_CONST               5 ('surface')
                LOAD_FAST_BORROW         2 (surface)

 433            LOAD_CONST               6 ('rows')
                BUILD_LIST               0

 434            LOAD_CONST               7 ('count')
                LOAD_SMALL_INT           0

 435            LOAD_CONST               8 ('warnings')
                LOAD_CONST               9 ('db_unavailable')
                BUILD_LIST               1

 436            LOAD_CONST              10 ('error_code')
                LOAD_CONST               9 ('db_unavailable')

 430            BUILD_MAP                6

 437            LOAD_FAST_BORROW         2 (surface)

 430            LOAD_CONST              11 (('surface',))
                CALL_KW                  2
        L8:     RETURN_VALUE

 438    L9:     NOP

 439   L10:     LOAD_FAST_BORROW         5 (db)
                LOAD_ATTR                9 (table + NULL|self)
                LOAD_GLOBAL             10 (_TABLE_NAME)
                CALL                     1
                LOAD_ATTR               13 (select + NULL|self)
                LOAD_CONST              12 ('*')
                CALL                     1
                STORE_FAST               6 (query)

 440            LOAD_FAST_BORROW         3 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L13)
       L11:     NOT_TAKEN

 441   L12:     LOAD_FAST_BORROW         6 (query)
                LOAD_ATTR               15 (eq + NULL|self)
                LOAD_CONST              13 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)
                CALL                     2
                STORE_FAST               6 (query)

 442   L13:     LOAD_FAST_BORROW         6 (query)
                LOAD_ATTR               17 (order + NULL|self)
                LOAD_CONST              14 ('run_date')
                LOAD_CONST              15 (True)
                LOAD_CONST              16 (('desc',))
                CALL_KW                  2
                LOAD_ATTR               19 (limit + NULL|self)
                LOAD_FAST_BORROW         4 (cap)
                CALL                     1
                STORE_FAST               6 (query)

 443            LOAD_FAST_BORROW         6 (query)
                LOAD_ATTR               21 (execute + NULL|self)
                CALL                     0
                STORE_FAST               7 (resp)

 457   L14:     LOAD_GLOBAL             33 (getattr + NULL)
                LOAD_FAST                7 (resp)
                LOAD_CONST              20 ('data')
                LOAD_CONST               2 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L17)
       L15:     NOT_TAKEN
       L16:     POP_TOP
                BUILD_LIST               0
       L17:     STORE_FAST               9 (data)

 458            BUILD_LIST               0
                STORE_FAST              10 (rows)

 459            LOAD_FAST                9 (data)
                LOAD_CONST               2 (None)
                LOAD_FAST                4 (cap)
                BINARY_SLICE
                GET_ITER
       L18:     FOR_ITER                53 (to L21)
                STORE_FAST              11 (r)

 460            LOAD_GLOBAL             35 (isinstance + NULL)
                LOAD_FAST               11 (r)
                LOAD_GLOBAL             36 (dict)
                CALL                     2
                TO_BOOL
       L19:     POP_JUMP_IF_TRUE         3 (to L20)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L18)

 461   L20:     LOAD_FAST               10 (rows)
                LOAD_ATTR               39 (append + NULL|self)
                LOAD_GLOBAL             41 (_project_row + NULL)
                LOAD_FAST               11 (r)
                CALL                     1
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           55 (to L18)

 459   L21:     END_FOR
                POP_ITER

 462            LOAD_GLOBAL              7 (_final + NULL)

 463            LOAD_CONST               3 ('status')
                LOAD_CONST              21 ('ok')

 464            LOAD_CONST               5 ('surface')
                LOAD_FAST                2 (surface)

 465            LOAD_CONST               6 ('rows')
                LOAD_FAST               10 (rows)

 466            LOAD_CONST               7 ('count')
                LOAD_GLOBAL             43 (len + NULL)
                LOAD_FAST               10 (rows)
                CALL                     1

 467            LOAD_CONST               8 ('warnings')
                BUILD_LIST               0

 468            LOAD_CONST              10 ('error_code')
                LOAD_CONST               2 (None)

 462            BUILD_MAP                6

 469            LOAD_FAST                2 (surface)

 462            LOAD_CONST              11 (('surface',))
                CALL_KW                  2
       L22:     RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 444            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      102 (to L29)
                NOT_TAKEN
                STORE_FAST               8 (e)

 445   L24:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 446            LOAD_CONST              17 ('daily_ops_checklist_report query error type=')

 447            LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 446            BUILD_STRING             2

 445            CALL                     1
                POP_TOP

 449            LOAD_GLOBAL              7 (_final + NULL)

 450            LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('skipped')

 451            LOAD_CONST               5 ('surface')
                LOAD_FAST                2 (surface)

 452            LOAD_CONST               6 ('rows')
                BUILD_LIST               0

 453            LOAD_CONST               7 ('count')
                LOAD_SMALL_INT           0

 454            LOAD_CONST               8 ('warnings')
                LOAD_CONST              18 ('db_query_failed:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 455            LOAD_CONST              10 ('error_code')
                LOAD_CONST              19 ('db_query_failed')

 449            BUILD_MAP                6

 456            LOAD_FAST                2 (surface)

 449            LOAD_CONST              11 (('surface',))
                CALL_KW                  2
       L25:     SWAP                     2
       L26:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
       L27:     RETURN_VALUE

  --   L28:     LOAD_CONST               2 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 444   L29:     RERAISE                  0

  --   L30:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L31:     PUSH_EXC_INFO

 470            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      101 (to L36)
                NOT_TAKEN
                STORE_FAST               8 (e)

 471   L32:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 472            LOAD_CONST              22 ('daily_ops_checklist_report error type=')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 471            CALL                     1
                POP_TOP

 474            LOAD_GLOBAL              7 (_final + NULL)

 475            LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('skipped')

 476            LOAD_CONST               5 ('surface')
                LOAD_FAST                2 (surface)

 477            LOAD_CONST               6 ('rows')
                BUILD_LIST               0

 478            LOAD_CONST               7 ('count')
                LOAD_SMALL_INT           0

 479            LOAD_CONST              10 ('error_code')
                LOAD_CONST              23 ('unexpected:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 480            LOAD_CONST               8 ('warnings')
                BUILD_LIST               0

 474            BUILD_MAP                6

 481            LOAD_FAST                2 (surface)

 474            LOAD_CONST              11 (('surface',))
                CALL_KW                  2
       L33:     SWAP                     2
       L34:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RETURN_VALUE

  --   L35:     LOAD_CONST               2 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 470   L36:     RERAISE                  0

  --   L37:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L4 -> L31 [0]
  L5 to L8 -> L31 [0]
  L10 to L11 -> L23 [0]
  L12 to L14 -> L23 [0]
  L14 to L15 -> L31 [0]
  L16 to L19 -> L31 [0]
  L20 to L22 -> L31 [0]
  L23 to L24 -> L30 [1] lasti
  L24 to L25 -> L28 [1] lasti
  L25 to L26 -> L30 [1] lasti
  L26 to L27 -> L31 [0]
  L28 to L30 -> L30 [1] lasti
  L30 to L31 -> L31 [0]
  L31 to L32 -> L37 [1] lasti
  L32 to L33 -> L35 [1] lasti
  L33 to L34 -> L37 [1] lasti
  L35 to L37 -> L37 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "app\services\operator\daily_ops_checklist.py", line 484>:
484           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('limit')

486           LOAD_CONST               2 ('Any')

484           LOAD_CONST               3 ('return')

487           LOAD_CONST               4 ('Dict[str, Any]')

484           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object fleet_daily_ops_summary at 0x0000018C17EA5290, file "app\services\operator\daily_ops_checklist.py", line 484>:
 484            RESUME                   0

 491            LOAD_CONST               1 ('ops.daily_checklist.fleet_summary')
                STORE_FAST               1 (surface)

 492            NOP

 493    L1:     LOAD_GLOBAL              1 (_safe_count + NULL)
                LOAD_FAST_BORROW         0 (limit)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
        L2:     NOT_TAKEN
        L3:     POP_TOP
                LOAD_SMALL_INT         100
        L4:     STORE_FAST               2 (cap)

 494            LOAD_FAST_BORROW         2 (cap)
                LOAD_SMALL_INT         200
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

 495            LOAD_SMALL_INT         200
                STORE_FAST               2 (cap)

 496    L5:     LOAD_GLOBAL              3 (daily_ops_checklist_report + NULL)
                LOAD_FAST_BORROW         2 (cap)
                LOAD_CONST               2 (('limit',))
                CALL_KW                  1
                STORE_FAST               3 (report)

 497            LOAD_FAST_BORROW         3 (report)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               3 ('rows')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                BUILD_LIST               0
        L8:     STORE_FAST               4 (rows)

 498            LOAD_GLOBAL              7 (set + NULL)
                CALL                     0
                STORE_FAST               5 (seen)

 499            BUILD_LIST               0
                STORE_FAST               6 (unique_rows)

 503            LOAD_FAST_BORROW         4 (rows)
                GET_ITER
        L9:     FOR_ITER                89 (to L14)
                STORE_FAST               7 (r)

 504            LOAD_FAST_BORROW         7 (r)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               4 ('brokerage_id')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
       L10:     NOT_TAKEN
       L11:     POP_TOP
                LOAD_CONST               5 ('<fleet>')
       L12:     LOAD_FAST_BORROW         7 (r)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               6 ('run_date')
                CALL                     1
                BUILD_TUPLE              2
                STORE_FAST               8 (key)

 505            LOAD_FAST_BORROW_LOAD_FAST_BORROW 133 (key, seen)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN

 506            JUMP_BACKWARD           55 (to L9)

 507   L13:     LOAD_FAST_BORROW         5 (seen)
                LOAD_ATTR                9 (add + NULL|self)
                LOAD_FAST_BORROW         8 (key)
                CALL                     1
                POP_TOP

 508            LOAD_FAST_BORROW         6 (unique_rows)
                LOAD_ATTR               11 (append + NULL|self)
                LOAD_FAST_BORROW         7 (r)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           91 (to L9)

 503   L14:     END_FOR
                POP_ITER

 509            BUILD_MAP                0
                STORE_FAST               9 (by_status)

 510            LOAD_FAST_BORROW         6 (unique_rows)
                GET_ITER
       L15:     FOR_ITER                57 (to L19)
                STORE_FAST               7 (r)

 511            LOAD_FAST_BORROW         7 (r)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
       L16:     NOT_TAKEN
       L17:     POP_TOP
                LOAD_CONST               8 ('UNKNOWN')
       L18:     STORE_FAST              10 (s)

 512            LOAD_FAST_BORROW         9 (by_status)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_FAST_BORROW        10 (s)
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (by_status, s)
                STORE_SUBSCR
                JUMP_BACKWARD           59 (to L15)

 510   L19:     END_FOR
                POP_ITER

 513            LOAD_GLOBAL             13 (_final + NULL)

 514            LOAD_CONST               7 ('status')
                LOAD_FAST_BORROW         3 (report)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               7 ('status')
                LOAD_CONST               9 ('ok')
                CALL                     2

 515            LOAD_CONST              10 ('surface')
                LOAD_FAST_BORROW         1 (surface)

 516            LOAD_CONST              11 ('by_status')
                LOAD_FAST_BORROW         9 (by_status)

 517            LOAD_CONST              12 ('count')
                LOAD_GLOBAL             15 (len + NULL)
                LOAD_FAST_BORROW         6 (unique_rows)
                CALL                     1

 518            LOAD_CONST               3 ('rows')
                LOAD_FAST_BORROW         6 (unique_rows)

 519            LOAD_CONST              13 ('warnings')
                LOAD_FAST_BORROW         3 (report)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              13 ('warnings')
                BUILD_LIST               0
                CALL                     2

 520            LOAD_CONST              14 ('error_code')
                LOAD_FAST_BORROW         3 (report)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              14 ('error_code')
                CALL                     1

 513            BUILD_MAP                7

 521            LOAD_FAST_BORROW         1 (surface)

 513            LOAD_CONST              15 (('surface',))
                CALL_KW                  2
       L20:     RETURN_VALUE

  --   L21:     PUSH_EXC_INFO

 522            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      101 (to L26)
                NOT_TAKEN
                STORE_FAST              11 (e)

 523   L22:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 524            LOAD_CONST              16 ('fleet_daily_ops_summary error type=')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 523            CALL                     1
                POP_TOP

 526            LOAD_GLOBAL             13 (_final + NULL)

 527            LOAD_CONST               7 ('status')
                LOAD_CONST              17 ('skipped')

 528            LOAD_CONST              10 ('surface')
                LOAD_FAST                1 (surface)

 529            LOAD_CONST               3 ('rows')
                BUILD_LIST               0

 530            LOAD_CONST              12 ('count')
                LOAD_SMALL_INT           0

 531            LOAD_CONST              14 ('error_code')
                LOAD_CONST              18 ('unexpected:')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 532            LOAD_CONST              13 ('warnings')
                BUILD_LIST               0

 526            BUILD_MAP                6

 533            LOAD_FAST                1 (surface)

 526            LOAD_CONST              15 (('surface',))
                CALL_KW                  2
       L23:     SWAP                     2
       L24:     POP_EXCEPT
                LOAD_CONST              19 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RETURN_VALUE

  --   L25:     LOAD_CONST              19 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 522   L26:     RERAISE                  0

  --   L27:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L21 [0]
  L3 to L6 -> L21 [0]
  L7 to L10 -> L21 [0]
  L11 to L16 -> L21 [0]
  L17 to L20 -> L21 [0]
  L21 to L22 -> L27 [1] lasti
  L22 to L23 -> L25 [1] lasti
  L23 to L24 -> L27 [1] lasti
  L25 to L27 -> L27 [1] lasti
```
