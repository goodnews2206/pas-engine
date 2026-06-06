# operator/incident_log

- **pyc:** `app\services\operator\__pycache__\incident_log.cpython-314.pyc`
- **expected source path (absent):** `app\services\operator/incident_log.py`
- **co_filename (from bytecode):** `app\services\operator\incident_log.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** operator

## Module docstring

```
PAS188 — Structured incident log (operator-opened only,
append-only).

Records operator-opened incidents per the severity matrix
in
``docs/pas186_final_pilot_cutover.md`` § 10 (S1..S6).

Doctrine:

* **Operator-opened only.** No autonomous opener. PAS
  surfaces NEVER auto-open an incident in response to a
  metric.
* **Append-only on the row.** ``opened_at``, ``severity``,
  ``brokerage_id``, ``summary``, ``opened_by_actor_*``
  are immutable; only ``status`` + ``resolved_*`` +
  ``metadata`` may transition. DELETE is forbidden for
  non-service roles (enforced at the SQL layer in v38).
* **Closed severity enum.** S1..S6.
* **Closed status enum.** OPEN | INVESTIGATING |
  RESOLVED | WONT_FIX | DUPLICATE.
* **No PII / no secrets.** Free-text ``summary`` is
  trimmed to 4 KB; ``resolution_text`` to 2 KB. Operator
  is responsible for redaction; the forbidden-token
  scanner is a defence in depth on the returned
  envelope.
* **NEVER raises.** DB-unavailable -> ``status="skipped"``
  + warning.

Public surface:

  * ``open_incident(...)``
  * ``update_incident_status(...)``
  * ``resolve_incident(...)``
  * ``list_incidents(...)``
  * ``get_incident(...)``
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.event_logger`, `app.db.supabase_client`, `datetime`, `get_supabase`, `log_event_bg`, `logging`, `timezone`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_emit_event`, `_final`, `_get_db`, `_now_iso`, `_project_row`, `_safe_actor_id`, `_safe_actor_type`, `_safe_brokerage`, `_safe_resolution`, `_safe_resolution_code`, `_safe_severity`, `_safe_str`, `_safe_summary`, `_scan_for_forbidden`, `get_incident`, `list_incidents`, `open_incident`, `resolve_incident`, `update_incident_status`

## Env-key candidates

`DUPLICATE`, `INVESTIGATING`, `OPEN`, `RESOLVED`, `WONT_FIX`

## String constants (redacted where noted)

- '\nPAS188 — Structured incident log (operator-opened only,\nappend-only).\n\nRecords operator-opened incidents per the severity matrix\nin\n``docs/pas186_final_pilot_cutover.md`` § 10 (S1..S6).\n\nDoctrine:\n\n* **Operator-opened only.** No autonomous opener. PAS\n  surfaces NEVER auto-open an incident in response to a\n  metric.\n* **Append-only on the row.** ``opened_at``, ``severity``,\n  ``brokerage_id``, ``summary``, ``opened_by_actor_*``\n  are immutable; only ``status`` + ``resolved_*`` +\n  ``metadata`` may transition. DELETE is forbidden for\n  non-service roles (enforced at the SQL layer in v38).\n* **Closed severity enum.** S1..S6.\n* **Closed status enum.** OPEN | INVESTIGATING |\n  RESOLVED | WONT_FIX | DUPLICATE.\n* **No PII / no secrets.** Free-text ``summary`` is\n  trimmed to 4 KB; ``resolution_text`` to 2 KB. Operator\n  is responsible for redaction; the forbidden-token\n  scanner is a defence in depth on the returned\n  envelope.\n* **NEVER raises.** DB-unavailable -> ``status="skipped"``\n  + warning.\n\nPublic surface:\n\n  * ``open_incident(...)``\n  * ``update_incident_status(...)``\n  * ``resolve_incident(...)``\n  * ``list_incidents(...)``\n  * ``get_incident(...)``\n'
- 'pas.operator.incident_log'
- 'pas_operator_incidents'
- 'OPEN'
- 'INVESTIGATING'
- 'RESOLVED'
- 'WONT_FIX'
- 'DUPLICATE'
- 'brokerage_id'
- 'severity'
- 'status'
- 'actor_id'
- 'resolution_text'
- 'limit'
- 'return'
- 'str'
- 'seconds'
- 'value'
- 'Any'
- 'max_len'
- 'int'
- 'Optional[str]'
- 'envelope'
- 'obj'
- 'env'
- 'Dict[str, Any]'
- 'surface'
- 'incident_log surface='
- ' collapsed — forbidden token leaked'
- 'failed'
- 'error_code'
- 'incident_envelope_forbidden_token'
- 'warnings'
- 'row'
- 'event_type'
- 'payload'
- 'None'
- 'summary'
- 'actor_type'
- 'Open a new incident. Returns the canonical envelope\nwith the new ``incident_id`` + bounded row.'
- 'ops.incident.open'
- 'invalid_severity'
- 'invalid_summary'
- 'invalid_actor_type'
- 'incident_id'
- 'opened_at'
- 'opened_by_actor_type'
- 'opened_by_actor_id'
- 'db_unavailable'
- 'skipped'
- 'metadata'
- 'incident_log open insert error type='
- 'db_insert_failed:'
- 'incident.opened'
- 'open_incident error type='
- 'unexpected:'
- "Transition an open incident's status. The\nimmutable opening fields are NOT touched."
- 'ops.incident.update_status'
- 'invalid_arguments'
- 'invalid_status'
- 'incident_log update_status error type='
- 'db_update_failed:'
- 'incident.status_changed'
- 'update_incident_status error type='
- 'resolution_code'
- 'Resolve an incident. Sets status=RESOLVED + records\nresolution fields. ``resolution_code`` is operator-\nsupplied (free string, bounded).'
- 'ops.incident.resolve'
- 'resolved_at'
- 'resolved_by_actor_type'
- 'resolved_by_actor_id'
- 'incident_log resolve error type='
- 'incident.resolved'
- 'resolve_incident error type='
- 'Bounded listing of incidents. Closed allow-list.'
- 'ops.incident.list'
- 'rows'
- 'count'
- 'list_incidents query error type='
- 'db_query_failed:'
- 'db_query_failed'
- 'data'
- 'list_incidents error type='
- 'ops.incident.get'
- 'invalid_incident_id'
- 'get_incident query error type='
- 'incident_not_found'
- 'get_incident error type='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS188 — Structured incident log (operator-opened only,\nappend-only).\n\nRecords operator-opened incidents per the severity matrix\nin\n``docs/pas186_final_pilot_cutover.md`` § 10 (S1..S6).\n\nDoctrine:\n\n* **Operator-opened only.** No autonomous opener. PAS\n  surfaces NEVER auto-open an incident in response to a\n  metric.\n* **Append-only on the row.** ``opened_at``, ``severity``,\n  ``brokerage_id``, ``summary``, ``opened_by_actor_*``\n  are immutable; only ``status`` + ``resolved_*`` +\n  ``metadata`` may transition. DELETE is forbidden for\n  non-service roles (enforced at the SQL layer in v38).\n* **Closed severity enum.** S1..S6.\n* **Closed status enum.** OPEN | INVESTIGATING |\n  RESOLVED | WONT_FIX | DUPLICATE.\n* **No PII / no secrets.** Free-text ``summary`` is\n  trimmed to 4 KB; ``resolution_text`` to 2 KB. Operator\n  is responsible for redaction; the forbidden-token\n  scanner is a defence in depth on the returned\n  envelope.\n* **NEVER raises.** DB-unavailable -> ``status="skipped"``\n  + warning.\n\nPublic surface:\n\n  * ``open_incident(...)``\n  * ``update_incident_status(...)``\n  * ``resolve_incident(...)``\n  * ``list_incidents(...)``\n  * ``get_incident(...)``\n')
              STORE_NAME               0 (__doc__)

 39           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 41           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 42           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (uuid)
              STORE_NAME               4 (uuid)

 43           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timezone'))
              IMPORT_NAME              5 (datetime)
              IMPORT_FROM              5 (datetime)
              STORE_NAME               5 (datetime)
              IMPORT_FROM              6 (timezone)
              STORE_NAME               6 (timezone)
              POP_TOP

 44           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              7 (typing)
              IMPORT_FROM              8 (Any)
              STORE_NAME               8 (Any)
              IMPORT_FROM              9 (Dict)
              STORE_NAME               9 (Dict)
              IMPORT_FROM             10 (List)
              STORE_NAME              10 (List)
              IMPORT_FROM             11 (Optional)
              STORE_NAME              11 (Optional)
              POP_TOP

 47           LOAD_NAME                3 (logging)
              LOAD_ATTR               24 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.operator.incident_log')
              CALL                     1
              STORE_NAME              13 (logger)

 54           LOAD_CONST               6 ('pas_operator_incidents')
              STORE_NAME              14 (_TABLE_NAME)

 56           LOAD_CONST               7 ('OPEN')
              STORE_NAME              15 (STATUS_OPEN)

 57           LOAD_CONST               8 ('INVESTIGATING')
              STORE_NAME              16 (STATUS_INVESTIGATING)

 58           LOAD_CONST               9 ('RESOLVED')
              STORE_NAME              17 (STATUS_RESOLVED)

 59           LOAD_CONST              10 ('WONT_FIX')
              STORE_NAME              18 (STATUS_WONT_FIX)

 60           LOAD_CONST              11 ('DUPLICATE')
              STORE_NAME              19 (STATUS_DUPLICATE)

 62           LOAD_NAME               20 (frozenset)
              PUSH_NULL

 63           LOAD_NAME               15 (STATUS_OPEN)
              LOAD_NAME               16 (STATUS_INVESTIGATING)
              LOAD_NAME               17 (STATUS_RESOLVED)

 64           LOAD_NAME               18 (STATUS_WONT_FIX)
              LOAD_NAME               19 (STATUS_DUPLICATE)

 62           BUILD_SET                5
              CALL                     1
              STORE_NAME              21 (_VALID_STATUSES)

 67           LOAD_NAME               20 (frozenset)
              PUSH_NULL

 68           LOAD_NAME               17 (STATUS_RESOLVED)
              LOAD_NAME               18 (STATUS_WONT_FIX)
              LOAD_NAME               19 (STATUS_DUPLICATE)

 67           BUILD_SET                3
              CALL                     1
              STORE_NAME              22 (_TERMINAL_STATUSES)

 71           LOAD_NAME               20 (frozenset)
              PUSH_NULL
              BUILD_SET                0
              LOAD_CONST              57 (frozenset({'S2', 'S5', 'S1', 'S3', 'S6', 'S4'}))
              SET_UPDATE               1
              CALL                     1
              STORE_NAME              23 (_VALID_SEVERITIES)

 73           LOAD_SMALL_INT         200
              STORE_NAME              24 (_BROKERAGE_ID_MAX_LEN)

 74           LOAD_SMALL_INT         200
              STORE_NAME              25 (_ACTOR_ID_MAX_LEN)

 75           LOAD_CONST              12 (4096)
              STORE_NAME              26 (_SUMMARY_MAX_LEN)

 76           LOAD_CONST              13 (2048)
              STORE_NAME              27 (_RESOLUTION_MAX_LEN)

 78           LOAD_CONST              58 (('incident_id', 'brokerage_id', 'opened_at', 'opened_by_actor_type', 'opened_by_actor_id', 'severity', 'summary', 'status', 'resolved_at', 'resolved_by_actor_type', 'resolved_by_actor_id', 'resolution_code'))
              STORE_NAME              28 (_ROW_ALLOWLIST)

 93           LOAD_CONST              59 (('phone', 'email', 'name_token', 'transcript', 'raw_payload', 'raw_email', 'raw_body', 'secret', 'signature', 'dedupe_key', 'api_key', 'token', 'stack_trace', 'prompt_text', 'env_values'))
              STORE_NAME              29 (_FORBIDDEN_RESPONSE_TOKENS)

105           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA3B40, file "app\services\operator\incident_log.py", line 105>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _now_iso at 0x0000018C18038670, file "app\services\operator\incident_log.py", line 105>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_now_iso)

109           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18025A30, file "app\services\operator\incident_log.py", line 109>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _safe_str at 0x0000018C18010DF0, file "app\services\operator\incident_log.py", line 109>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_safe_str)

118           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA1D40, file "app\services\operator\incident_log.py", line 118>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _safe_brokerage at 0x0000018C18025130, file "app\services\operator\incident_log.py", line 118>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_safe_brokerage)

122           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA3870, file "app\services\operator\incident_log.py", line 122>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object _safe_actor_id at 0x0000018C18024B30, file "app\services\operator\incident_log.py", line 122>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_safe_actor_id)

126           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA2A60, file "app\services\operator\incident_log.py", line 126>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object _safe_actor_type at 0x0000018C18038F30, file "app\services\operator\incident_log.py", line 126>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              34 (_safe_actor_type)

136           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\operator\incident_log.py", line 136>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object _safe_severity at 0x0000018C18038170, file "app\services\operator\incident_log.py", line 136>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              35 (_safe_severity)

146           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA3780, file "app\services\operator\incident_log.py", line 146>)
              MAKE_FUNCTION
              LOAD_CONST              30 (<code object _safe_summary at 0x0000018C17FF1230, file "app\services\operator\incident_log.py", line 146>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              36 (_safe_summary)

157           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA3C30, file "app\services\operator\incident_log.py", line 157>)
              MAKE_FUNCTION
              LOAD_CONST              32 (<code object _safe_resolution at 0x0000018C17FF10B0, file "app\services\operator\incident_log.py", line 157>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              37 (_safe_resolution)

170           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C17FA3A50, file "app\services\operator\incident_log.py", line 170>)
              MAKE_FUNCTION
              LOAD_CONST              34 (<code object _safe_resolution_code at 0x0000018C180532D0, file "app\services\operator\incident_log.py", line 170>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              38 (_safe_resolution_code)

177           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C17FA2F10, file "app\services\operator\incident_log.py", line 177>)
              MAKE_FUNCTION
              LOAD_CONST              36 (<code object _scan_for_forbidden at 0x0000018C18024E30, file "app\services\operator\incident_log.py", line 177>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              39 (_scan_for_forbidden)

201           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C18025D30, file "app\services\operator\incident_log.py", line 201>)
              MAKE_FUNCTION
              LOAD_CONST              38 (<code object _final at 0x0000018C17FE1290, file "app\services\operator\incident_log.py", line 201>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              40 (_final)

217           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C17FA3000, file "app\services\operator\incident_log.py", line 217>)
              MAKE_FUNCTION
              LOAD_CONST              40 (<code object _project_row at 0x0000018C180531B0, file "app\services\operator\incident_log.py", line 217>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              41 (_project_row)

225           LOAD_CONST              41 (<code object __annotate__ at 0x0000018C18025E30, file "app\services\operator\incident_log.py", line 225>)
              MAKE_FUNCTION
              LOAD_CONST              42 (<code object _emit_event at 0x0000018C18038B70, file "app\services\operator\incident_log.py", line 225>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              42 (_emit_event)

236           LOAD_CONST              43 (<code object _get_db at 0x0000018C18053CF0, file "app\services\operator\incident_log.py", line 236>)
              MAKE_FUNCTION
              STORE_NAME              43 (_get_db)

248           LOAD_CONST              14 ('brokerage_id')

250           LOAD_CONST               2 (None)

248           LOAD_CONST              44 ('actor_id')

254           LOAD_CONST               2 (None)

248           BUILD_MAP                2
              LOAD_CONST              45 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\operator\incident_log.py", line 248>)
              MAKE_FUNCTION
              LOAD_CONST              46 (<code object open_incident at 0x0000018C18325010, file "app\services\operator\incident_log.py", line 248>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              44 (open_incident)

340           LOAD_CONST              47 (<code object __annotate__ at 0x0000018C18024930, file "app\services\operator\incident_log.py", line 340>)
              MAKE_FUNCTION
              LOAD_CONST              48 (<code object update_incident_status at 0x0000018C17ED9FB0, file "app\services\operator\incident_log.py", line 340>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              45 (update_incident_status)

413           LOAD_CONST              49 ('resolution_text')

419           LOAD_CONST               2 (None)

413           BUILD_MAP                1
              LOAD_CONST              50 (<code object __annotate__ at 0x0000018C18025730, file "app\services\operator\incident_log.py", line 413>)
              MAKE_FUNCTION
              LOAD_CONST              51 (<code object resolve_incident at 0x0000018C17E7F430, file "app\services\operator\incident_log.py", line 413>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              46 (resolve_incident)

496           LOAD_CONST              14 ('brokerage_id')

498           LOAD_CONST               2 (None)

496           LOAD_CONST              15 ('severity')

499           LOAD_CONST               2 (None)

496           LOAD_CONST              16 ('status')

500           LOAD_CONST               2 (None)

496           LOAD_CONST              52 ('limit')

501           LOAD_SMALL_INT          50

496           BUILD_MAP                4
              LOAD_CONST              53 (<code object __annotate__ at 0x0000018C18026530, file "app\services\operator\incident_log.py", line 496>)
              MAKE_FUNCTION
              LOAD_CONST              54 (<code object list_incidents at 0x0000018C17D7CFC0, file "app\services\operator\incident_log.py", line 496>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              47 (list_incidents)

581           LOAD_CONST              55 (<code object __annotate__ at 0x0000018C17FA2880, file "app\services\operator\incident_log.py", line 581>)
              MAKE_FUNCTION
              LOAD_CONST              56 (<code object get_incident at 0x0000018C17F69200, file "app\services\operator\incident_log.py", line 581>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              48 (get_incident)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app\services\operator\incident_log.py", line 105>:
105           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038670, file "app\services\operator\incident_log.py", line 105>:
105           RESUME                   0

106           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app\services\operator\incident_log.py", line 109>:
109           RESUME                   0
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

Disassembly of <code object _safe_str at 0x0000018C18010DF0, file "app\services\operator\incident_log.py", line 109>:
109           RESUME                   0

110           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

111           LOAD_CONST               0 (None)
              RETURN_VALUE

112   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (s)

113           LOAD_FAST_BORROW         2 (s)
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

114   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

115   L3:     LOAD_FAST_BORROW         2 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "app\services\operator\incident_log.py", line 118>:
118           RESUME                   0
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

Disassembly of <code object _safe_brokerage at 0x0000018C18025130, file "app\services\operator\incident_log.py", line 118>:
118           RESUME                   0

119           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (_BROKERAGE_ID_MAX_LEN)
              CALL                     2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\services\operator\incident_log.py", line 122>:
122           RESUME                   0
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

Disassembly of <code object _safe_actor_id at 0x0000018C18024B30, file "app\services\operator\incident_log.py", line 122>:
122           RESUME                   0

123           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (_ACTOR_ID_MAX_LEN)
              CALL                     2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app\services\operator\incident_log.py", line 126>:
126           RESUME                   0
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

Disassembly of <code object _safe_actor_type at 0x0000018C18038F30, file "app\services\operator\incident_log.py", line 126>:
126           RESUME                   0

127           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_SMALL_INT          32
              CALL                     2
              STORE_FAST               1 (s)

128           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

129           LOAD_CONST               1 (None)
              RETURN_VALUE

130   L1:     LOAD_FAST_BORROW         1 (s)
              LOAD_ATTR                3 (upper + NULL|self)
              CALL                     0
              STORE_FAST               2 (up)

131           LOAD_FAST_BORROW         2 (up)
              LOAD_CONST               2 (('ADMIN', 'OPERATOR'))
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

132           LOAD_CONST               1 (None)
              RETURN_VALUE

133   L2:     LOAD_FAST_BORROW         2 (up)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\operator\incident_log.py", line 136>:
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

Disassembly of <code object _safe_severity at 0x0000018C18038170, file "app\services\operator\incident_log.py", line 136>:
136           RESUME                   0

137           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_SMALL_INT           8
              CALL                     2
              STORE_FAST               1 (s)

138           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

139           LOAD_CONST               1 (None)
              RETURN_VALUE

140   L1:     LOAD_FAST_BORROW         1 (s)
              LOAD_ATTR                3 (upper + NULL|self)
              CALL                     0
              STORE_FAST               2 (up)

141           LOAD_FAST_BORROW         2 (up)
              LOAD_GLOBAL              4 (_VALID_SEVERITIES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

142           LOAD_CONST               1 (None)
              RETURN_VALUE

143   L2:     LOAD_FAST_BORROW         2 (up)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app\services\operator\incident_log.py", line 146>:
146           RESUME                   0
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

Disassembly of <code object _safe_summary at 0x0000018C17FF1230, file "app\services\operator\incident_log.py", line 146>:
146           RESUME                   0

147           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

148           LOAD_CONST               0 (None)
              RETURN_VALUE

149   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

150           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

151           LOAD_CONST               0 (None)
              RETURN_VALUE

152   L2:     LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_SUMMARY_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       10 (to L3)
              NOT_TAKEN

153           LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               0 (None)
              LOAD_GLOBAL              8 (_SUMMARY_MAX_LEN)
              BINARY_SLICE
              STORE_FAST               1 (s)

154   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app\services\operator\incident_log.py", line 157>:
157           RESUME                   0
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

Disassembly of <code object _safe_resolution at 0x0000018C17FF10B0, file "app\services\operator\incident_log.py", line 157>:
157           RESUME                   0

158           LOAD_FAST_BORROW         0 (value)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

159           LOAD_CONST               0 (None)
              RETURN_VALUE

160   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

161           LOAD_CONST               0 (None)
              RETURN_VALUE

162   L2:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

163           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

164           LOAD_CONST               0 (None)
              RETURN_VALUE

165   L3:     LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_RESOLUTION_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       10 (to L4)
              NOT_TAKEN

166           LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               0 (None)
              LOAD_GLOBAL              8 (_RESOLUTION_MAX_LEN)
              BINARY_SLICE
              STORE_FAST               1 (s)

167   L4:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app\services\operator\incident_log.py", line 170>:
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

Disassembly of <code object _safe_resolution_code at 0x0000018C180532D0, file "app\services\operator\incident_log.py", line 170>:
170           RESUME                   0

171           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_SMALL_INT          64
              CALL                     2
              STORE_FAST               1 (s)

172           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

173           LOAD_CONST               1 (None)
              RETURN_VALUE

174   L1:     LOAD_FAST_BORROW         1 (s)
              LOAD_ATTR                3 (upper + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "app\services\operator\incident_log.py", line 177>:
177           RESUME                   0
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

Disassembly of <code object _scan_for_forbidden at 0x0000018C18024E30, file "app\services\operator\incident_log.py", line 177>:
  --           MAKE_CELL                1 (walk)

 177           RESUME                   0

 178           LOAD_CONST               0 (<code object __annotate__ at 0x0000018C17FA1E30, file "app\services\operator\incident_log.py", line 178>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object walk at 0x0000018C17CC1CE0, file "app\services\operator\incident_log.py", line 178>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

 198           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "app\services\operator\incident_log.py", line 178>:
178           RESUME                   0
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

Disassembly of <code object walk at 0x0000018C17CC1CE0, file "app\services\operator\incident_log.py", line 178>:
  --            COPY_FREE_VARS           1

 178            RESUME                   0

 179            NOP

 180    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      111 (to L16)
        L2:     NOT_TAKEN

 181    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                88 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

 182            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L10)
                NOT_TAKEN

 183            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

 184            LOAD_GLOBAL             10 (_FORBIDDEN_RESPONSE_TOKENS)
                GET_ITER
        L5:     FOR_ITER                15 (to L9)
                STORE_FAST               4 (tok)

 185            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)

 186    L7:     LOAD_FAST_BORROW         4 (tok)
                SWAP                     2
                POP_TOP
                SWAP                     2
                POP_TOP
        L8:     RETURN_VALUE

 184    L9:     END_FOR
                POP_ITER

 187   L10:     LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 188            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           86 (to L4)

 189   L12:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L13:     RETURN_VALUE

 181   L14:     END_FOR
                POP_ITER

 197   L15:     LOAD_CONST               0 (None)
                RETURN_VALUE

 190   L16:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             12 (list)
                LOAD_GLOBAL             14 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L22)
                NOT_TAKEN

 191            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L17:     FOR_ITER                23 (to L21)
                STORE_FAST               2 (v)

 192            LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 193            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           21 (to L17)

 194   L19:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L20:     RETURN_VALUE

 191   L21:     END_FOR
                POP_ITER

 197   L22:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 195            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L25)
                NOT_TAKEN
                POP_TOP

 196   L24:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 195   L25:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\services\operator\incident_log.py", line 201>:
201           RESUME                   0
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

Disassembly of <code object _final at 0x0000018C17FE1290, file "app\services\operator\incident_log.py", line 201>:
201           RESUME                   0

202           LOAD_GLOBAL              1 (_scan_for_forbidden + NULL)
              LOAD_FAST_BORROW         0 (env)
              CALL                     1
              STORE_FAST               2 (leak)

203           LOAD_FAST_BORROW         2 (leak)
              TO_BOOL
              POP_JUMP_IF_FALSE       37 (to L1)
              NOT_TAKEN

204           LOAD_GLOBAL              2 (logger)
              LOAD_ATTR                5 (warning + NULL|self)

205           LOAD_CONST               0 ('incident_log surface=')
              LOAD_FAST_BORROW         1 (surface)
              FORMAT_SIMPLE
              LOAD_CONST               1 (' collapsed — forbidden token leaked')
              BUILD_STRING             3

204           CALL                     1
              POP_TOP

209           LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('failed')

210           LOAD_CONST               4 ('surface')
              LOAD_FAST_BORROW         1 (surface)

211           LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('incident_envelope_forbidden_token')

212           LOAD_CONST               7 ('warnings')
              LOAD_CONST               6 ('incident_envelope_forbidden_token')
              BUILD_LIST               1

208           BUILD_MAP                4
              RETURN_VALUE

214   L1:     LOAD_FAST_BORROW         0 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "app\services\operator\incident_log.py", line 217>:
217           RESUME                   0
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

Disassembly of <code object _project_row at 0x0000018C180531B0, file "app\services\operator\incident_log.py", line 217>:
217           RESUME                   0

218           BUILD_MAP                0
              STORE_FAST               1 (out)

219           LOAD_GLOBAL              0 (_ROW_ALLOWLIST)
              GET_ITER
      L1:     FOR_ITER                21 (to L3)
              STORE_FAST               2 (k)

220           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L1)

221   L2:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, k)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, k)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L1)

219   L3:     END_FOR
              POP_ITER

222           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app\services\operator\incident_log.py", line 225>:
225           RESUME                   0
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

Disassembly of <code object _emit_event at 0x0000018C18038B70, file "app\services\operator\incident_log.py", line 225>:
 225            RESUME                   0

 226            NOP

 227    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('log_event_bg',))
                IMPORT_NAME              0 (app.db.event_logger)
                IMPORT_FROM              1 (log_event_bg)
                STORE_FAST               2 (log_event_bg)
                POP_TOP

 230    L2:     NOP

 231    L3:     LOAD_FAST                2 (log_event_bg)
                PUSH_NULL
                LOAD_FAST_LOAD_FAST      1 (event_type, payload)
                CALL                     2
                POP_TOP
        L4:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 228            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L7)
                NOT_TAKEN
                POP_TOP

 229    L6:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 228    L7:     RERAISE                  0

  --    L8:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
        L9:     PUSH_EXC_INFO

 232            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L11)
                NOT_TAKEN
                POP_TOP

 233   L10:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 232   L11:     RERAISE                  0

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

Disassembly of <code object _get_db at 0x0000018C18053CF0, file "app\services\operator\incident_log.py", line 236>:
 236           RESUME                   0

 237           NOP

 238   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 239           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 240           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 241   L4:     POP_EXCEPT
               LOAD_CONST               2 (None)
               RETURN_VALUE

 240   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\operator\incident_log.py", line 248>:
248           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

250           LOAD_CONST               2 ('Any')

248           LOAD_CONST               3 ('severity')

251           LOAD_CONST               2 ('Any')

248           LOAD_CONST               4 ('summary')

252           LOAD_CONST               2 ('Any')

248           LOAD_CONST               5 ('actor_type')

253           LOAD_CONST               2 ('Any')

248           LOAD_CONST               6 ('actor_id')

254           LOAD_CONST               2 ('Any')

248           LOAD_CONST               7 ('return')

255           LOAD_CONST               8 ('Dict[str, Any]')

248           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object open_incident at 0x0000018C18325010, file "app\services\operator\incident_log.py", line 248>:
 248            RESUME                   0

 258            LOAD_CONST               1 ('ops.incident.open')
                STORE_FAST               5 (surface)

 259            NOP

 260    L1:     LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               2 (None)
        L3:     STORE_FAST               6 (bid)

 261            LOAD_GLOBAL              3 (_safe_severity + NULL)
                LOAD_FAST_BORROW         1 (severity)
                CALL                     1
                STORE_FAST               7 (sev)

 262            LOAD_GLOBAL              5 (_safe_summary + NULL)
                LOAD_FAST_BORROW         2 (summary)
                CALL                     1
                STORE_FAST               8 (summ)

 263            LOAD_GLOBAL              7 (_safe_actor_type + NULL)
                LOAD_FAST_BORROW         3 (actor_type)
                CALL                     1
                STORE_FAST               9 (atype)

 264            LOAD_FAST_BORROW         4 (actor_id)
                POP_JUMP_IF_NONE        12 (to L4)
                NOT_TAKEN
                LOAD_GLOBAL              9 (_safe_actor_id + NULL)
                LOAD_FAST_BORROW         4 (actor_id)
                CALL                     1
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               2 (None)
        L5:     STORE_FAST              10 (aid)

 265            LOAD_FAST_BORROW         7 (sev)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L9)
        L6:     NOT_TAKEN

 266    L7:     LOAD_GLOBAL             11 (_final + NULL)

 267            LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('failed')

 268            LOAD_CONST               5 ('surface')
                LOAD_FAST_BORROW         5 (surface)

 269            LOAD_CONST               6 ('error_code')
                LOAD_CONST               7 ('invalid_severity')

 270            LOAD_CONST               8 ('warnings')
                LOAD_CONST               7 ('invalid_severity')
                BUILD_LIST               1

 266            BUILD_MAP                4

 271            LOAD_FAST_BORROW         5 (surface)

 266            LOAD_CONST               9 (('surface',))
                CALL_KW                  2
        L8:     RETURN_VALUE

 272    L9:     LOAD_FAST_BORROW         8 (summ)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L13)
       L10:     NOT_TAKEN

 273   L11:     LOAD_GLOBAL             11 (_final + NULL)

 274            LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('failed')

 275            LOAD_CONST               5 ('surface')
                LOAD_FAST_BORROW         5 (surface)

 276            LOAD_CONST               6 ('error_code')
                LOAD_CONST              10 ('invalid_summary')

 277            LOAD_CONST               8 ('warnings')
                LOAD_CONST              10 ('invalid_summary')
                BUILD_LIST               1

 273            BUILD_MAP                4

 278            LOAD_FAST_BORROW         5 (surface)

 273            LOAD_CONST               9 (('surface',))
                CALL_KW                  2
       L12:     RETURN_VALUE

 279   L13:     LOAD_FAST_BORROW         9 (atype)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L17)
       L14:     NOT_TAKEN

 280   L15:     LOAD_GLOBAL             11 (_final + NULL)

 281            LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('failed')

 282            LOAD_CONST               5 ('surface')
                LOAD_FAST_BORROW         5 (surface)

 283            LOAD_CONST               6 ('error_code')
                LOAD_CONST              11 ('invalid_actor_type')

 284            LOAD_CONST               8 ('warnings')
                LOAD_CONST              11 ('invalid_actor_type')
                BUILD_LIST               1

 280            BUILD_MAP                4

 285            LOAD_FAST_BORROW         5 (surface)

 280            LOAD_CONST               9 (('surface',))
                CALL_KW                  2
       L16:     RETURN_VALUE

 286   L17:     LOAD_GLOBAL             13 (_now_iso + NULL)
                CALL                     0
                STORE_FAST              11 (now)

 288            LOAD_CONST              12 ('incident_id')
                LOAD_GLOBAL             15 (str + NULL)
                LOAD_GLOBAL             16 (uuid)
                LOAD_ATTR               18 (uuid4)
                PUSH_NULL
                CALL                     0
                CALL                     1

 289            LOAD_CONST              13 ('brokerage_id')
                LOAD_FAST_BORROW         6 (bid)

 290            LOAD_CONST              14 ('opened_at')
                LOAD_FAST_BORROW        11 (now)

 291            LOAD_CONST              15 ('opened_by_actor_type')
                LOAD_FAST_BORROW         9 (atype)

 292            LOAD_CONST              16 ('opened_by_actor_id')
                LOAD_FAST_BORROW        10 (aid)

 293            LOAD_CONST              17 ('severity')
                LOAD_FAST_BORROW         7 (sev)

 294            LOAD_CONST              18 ('summary')
                LOAD_FAST_BORROW         8 (summ)

 295            LOAD_CONST               3 ('status')
                LOAD_GLOBAL             20 (STATUS_OPEN)

 287            BUILD_MAP                8
                STORE_FAST              12 (row)

 297            LOAD_GLOBAL             23 (_get_db + NULL)
                CALL                     0
                STORE_FAST              13 (db)

 298            BUILD_LIST               0
                STORE_FAST              14 (warnings)

 299            LOAD_FAST_BORROW        13 (db)
                POP_JUMP_IF_NOT_NONE    21 (to L18)
                NOT_TAKEN

 300            LOAD_FAST_BORROW        14 (warnings)
                LOAD_ATTR               25 (append + NULL|self)
                LOAD_CONST              19 ('db_unavailable')
                CALL                     1
                POP_TOP

 301            LOAD_CONST              20 ('skipped')
                STORE_FAST              15 (db_status)
                JUMP_FORWARD            59 (to L20)

 303   L18:     NOP

 304   L19:     LOAD_FAST_BORROW        13 (db)
                LOAD_ATTR               27 (table + NULL|self)
                LOAD_GLOBAL             28 (_TABLE_NAME)
                CALL                     1
                LOAD_ATTR               31 (insert + NULL|self)
                BUILD_MAP                0
                LOAD_FAST_BORROW        12 (row)
                DICT_UPDATE              1
                LOAD_CONST              21 ('metadata')
                BUILD_MAP                0
                BUILD_MAP                1
                DICT_UPDATE              1
                CALL                     1
                LOAD_ATTR               33 (execute + NULL|self)
                CALL                     0
                POP_TOP

 305            LOAD_CONST              22 ('ok')
                STORE_FAST              15 (db_status)

 313   L20:     LOAD_GLOBAL             45 (_emit_event + NULL)
                LOAD_CONST              25 ('incident.opened')

 314            LOAD_CONST              13 ('brokerage_id')
                LOAD_FAST_BORROW         6 (bid)

 315            LOAD_CONST              12 ('incident_id')
                LOAD_FAST_BORROW        12 (row)
                LOAD_CONST              12 ('incident_id')
                BINARY_OP               26 ([])

 316            LOAD_CONST              17 ('severity')
                LOAD_FAST_BORROW         7 (sev)

 317            LOAD_CONST              26 ('actor_type')
                LOAD_FAST_BORROW         9 (atype)

 318            LOAD_CONST              27 ('actor_id')
                LOAD_FAST_BORROW        10 (aid)

 319            LOAD_CONST               3 ('status')
                LOAD_GLOBAL             20 (STATUS_OPEN)

 313            BUILD_MAP                6
                CALL                     2
                POP_TOP

 321            LOAD_GLOBAL             11 (_final + NULL)

 322            LOAD_CONST               3 ('status')
                LOAD_FAST_BORROW        15 (db_status)
                LOAD_CONST              22 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L21)
                NOT_TAKEN
                LOAD_CONST              22 ('ok')
                JUMP_FORWARD             1 (to L22)
       L21:     LOAD_CONST              20 ('skipped')

 323   L22:     LOAD_CONST               5 ('surface')
                LOAD_FAST                5 (surface)

 324            LOAD_CONST              28 ('row')
                LOAD_GLOBAL             47 (_project_row + NULL)
                LOAD_FAST_BORROW        12 (row)
                CALL                     1

 325            LOAD_CONST               8 ('warnings')
                LOAD_FAST               14 (warnings)

 326            LOAD_CONST               6 ('error_code')
                LOAD_FAST_BORROW        15 (db_status)
                LOAD_CONST              22 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L23)
                NOT_TAKEN
                LOAD_CONST               2 (None)
                JUMP_FORWARD             1 (to L24)
       L23:     LOAD_CONST              19 ('db_unavailable')

 321   L24:     BUILD_MAP                5

 327            LOAD_FAST_BORROW         5 (surface)

 321            LOAD_CONST               9 (('surface',))
                CALL_KW                  2
       L25:     RETURN_VALUE

  --   L26:     PUSH_EXC_INFO

 306            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       95 (to L30)
                NOT_TAKEN
                STORE_FAST              16 (e)

 307   L27:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 308            LOAD_CONST              23 ('incident_log open insert error type=')

 309            LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               16 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE

 308            BUILD_STRING             2

 307            CALL                     1
                POP_TOP

 311            LOAD_FAST               14 (warnings)
                LOAD_ATTR               25 (append + NULL|self)
                LOAD_CONST              24 ('db_insert_failed:')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               16 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 312            LOAD_CONST              20 ('skipped')
                STORE_FAST              15 (db_status)
       L28:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              16 (e)
                DELETE_FAST             16 (e)
                JUMP_BACKWARD_NO_INTERRUPT 185 (to L20)

  --   L29:     LOAD_CONST               2 (None)
                STORE_FAST              16 (e)
                DELETE_FAST             16 (e)
                RERAISE                  1

 306   L30:     RERAISE                  0

  --   L31:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L32:     PUSH_EXC_INFO

 328            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L37)
                NOT_TAKEN
                STORE_FAST              16 (e)

 329   L33:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 330            LOAD_CONST              29 ('open_incident error type=')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               16 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 329            CALL                     1
                POP_TOP

 332            LOAD_GLOBAL             11 (_final + NULL)

 333            LOAD_CONST               3 ('status')
                LOAD_CONST              20 ('skipped')

 334            LOAD_CONST               5 ('surface')
                LOAD_FAST                5 (surface)

 335            LOAD_CONST               6 ('error_code')
                LOAD_CONST              30 ('unexpected:')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               16 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 336            LOAD_CONST               8 ('warnings')
                BUILD_LIST               0

 332            BUILD_MAP                4

 337            LOAD_FAST                5 (surface)

 332            LOAD_CONST               9 (('surface',))
                CALL_KW                  2
       L34:     SWAP                     2
       L35:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              16 (e)
                DELETE_FAST             16 (e)
                RETURN_VALUE

  --   L36:     LOAD_CONST               2 (None)
                STORE_FAST              16 (e)
                DELETE_FAST             16 (e)
                RERAISE                  1

 328   L37:     RERAISE                  0

  --   L38:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L6 -> L32 [0]
  L7 to L8 -> L32 [0]
  L9 to L10 -> L32 [0]
  L11 to L12 -> L32 [0]
  L13 to L14 -> L32 [0]
  L15 to L16 -> L32 [0]
  L17 to L18 -> L32 [0]
  L19 to L20 -> L26 [0]
  L20 to L25 -> L32 [0]
  L26 to L27 -> L31 [1] lasti
  L27 to L28 -> L29 [1] lasti
  L28 to L29 -> L32 [0]
  L29 to L31 -> L31 [1] lasti
  L31 to L32 -> L32 [0]
  L32 to L33 -> L38 [1] lasti
  L33 to L34 -> L36 [1] lasti
  L34 to L35 -> L38 [1] lasti
  L36 to L38 -> L38 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app\services\operator\incident_log.py", line 340>:
340           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('incident_id')

342           LOAD_CONST               2 ('Any')

340           LOAD_CONST               3 ('status')

343           LOAD_CONST               2 ('Any')

340           LOAD_CONST               4 ('actor_type')

344           LOAD_CONST               2 ('Any')

340           LOAD_CONST               5 ('actor_id')

345           LOAD_CONST               2 ('Any')

340           LOAD_CONST               6 ('return')

346           LOAD_CONST               7 ('Dict[str, Any]')

340           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object update_incident_status at 0x0000018C17ED9FB0, file "app\services\operator\incident_log.py", line 340>:
 340            RESUME                   0

 349            LOAD_CONST               1 ('ops.incident.update_status')
                STORE_FAST               4 (surface)

 350            NOP

 351    L1:     LOAD_GLOBAL              1 (_safe_str + NULL)
                LOAD_FAST_BORROW         0 (incident_id)
                LOAD_SMALL_INT          64
                CALL                     2
                STORE_FAST               5 (iid)

 352            LOAD_GLOBAL              1 (_safe_str + NULL)
                LOAD_FAST_BORROW         1 (status)
                LOAD_SMALL_INT          32
                CALL                     2
                STORE_FAST               6 (new)

 353            LOAD_GLOBAL              3 (_safe_actor_type + NULL)
                LOAD_FAST_BORROW         2 (actor_type)
                CALL                     1
                STORE_FAST               7 (atype)

 354            LOAD_GLOBAL              5 (_safe_actor_id + NULL)
                LOAD_FAST_BORROW         3 (actor_id)
                CALL                     1
                STORE_FAST               8 (aid)

 355            LOAD_FAST_BORROW         5 (iid)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L7)
                NOT_TAKEN
                LOAD_FAST_BORROW         6 (new)
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L7)
        L2:     NOT_TAKEN
        L3:     LOAD_FAST_BORROW         7 (atype)
                TO_BOOL
                POP_JUMP_IF_FALSE        9 (to L7)
        L4:     NOT_TAKEN
        L5:     LOAD_FAST_BORROW         8 (aid)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L9)
        L6:     NOT_TAKEN

 356    L7:     LOAD_GLOBAL              7 (_final + NULL)

 357            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 358            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         4 (surface)

 359            LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('invalid_arguments')

 360            LOAD_CONST               7 ('warnings')
                LOAD_CONST               6 ('invalid_arguments')
                BUILD_LIST               1

 356            BUILD_MAP                4

 361            LOAD_FAST_BORROW         4 (surface)

 356            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L8:     RETURN_VALUE

 362    L9:     LOAD_FAST_BORROW         6 (new)
                LOAD_ATTR                9 (upper + NULL|self)
                CALL                     0
                STORE_FAST               9 (new_up)

 363            LOAD_FAST_BORROW         9 (new_up)
                LOAD_GLOBAL             10 (_VALID_STATUSES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       23 (to L11)
                NOT_TAKEN

 364            LOAD_GLOBAL              7 (_final + NULL)

 365            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 366            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         4 (surface)

 367            LOAD_CONST               5 ('error_code')
                LOAD_CONST               9 ('invalid_status')

 368            LOAD_CONST               7 ('warnings')
                LOAD_CONST               9 ('invalid_status')
                BUILD_LIST               1

 364            BUILD_MAP                4

 369            LOAD_FAST_BORROW         4 (surface)

 364            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L10:     RETURN_VALUE

 370   L11:     LOAD_GLOBAL             13 (_get_db + NULL)
                CALL                     0
                STORE_FAST              10 (db)

 371            BUILD_LIST               0
                STORE_FAST              11 (warnings)

 372            LOAD_FAST_BORROW        10 (db)
                POP_JUMP_IF_NOT_NONE    21 (to L12)
                NOT_TAKEN

 373            LOAD_FAST_BORROW        11 (warnings)
                LOAD_ATTR               15 (append + NULL|self)
                LOAD_CONST              11 ('db_unavailable')
                CALL                     1
                POP_TOP

 374            LOAD_CONST              12 ('skipped')
                STORE_FAST              12 (db_status)
                JUMP_FORWARD            71 (to L14)

 376   L12:     NOP

 377   L13:     LOAD_FAST_BORROW        10 (db)
                LOAD_ATTR               17 (table + NULL|self)
                LOAD_GLOBAL             18 (_TABLE_NAME)
                CALL                     1
                LOAD_ATTR               21 (update + NULL|self)

 378            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW         9 (new_up)
                BUILD_MAP                1

 377            CALL                     1

 379            LOAD_ATTR               23 (eq + NULL|self)
                LOAD_CONST              13 ('incident_id')
                LOAD_FAST_BORROW         5 (iid)
                CALL                     2
                LOAD_ATTR               25 (execute + NULL|self)
                CALL                     0
                POP_TOP

 380            LOAD_CONST              14 ('ok')
                STORE_FAST              12 (db_status)

 388   L14:     LOAD_GLOBAL             37 (_emit_event + NULL)
                LOAD_CONST              17 ('incident.status_changed')

 389            LOAD_CONST              13 ('incident_id')
                LOAD_FAST_BORROW         5 (iid)

 390            LOAD_CONST              18 ('actor_type')
                LOAD_FAST_BORROW         7 (atype)

 391            LOAD_CONST              19 ('actor_id')
                LOAD_FAST_BORROW         8 (aid)

 392            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW         9 (new_up)

 388            BUILD_MAP                4
                CALL                     2
                POP_TOP

 394            LOAD_GLOBAL              7 (_final + NULL)

 395            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW        12 (db_status)
                LOAD_CONST              14 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN
                LOAD_CONST              14 ('ok')
                JUMP_FORWARD             1 (to L16)
       L15:     LOAD_CONST              12 ('skipped')

 396   L16:     LOAD_CONST               4 ('surface')
                LOAD_FAST                4 (surface)

 397            LOAD_CONST              20 ('row')
                LOAD_CONST              13 ('incident_id')
                LOAD_FAST_BORROW         5 (iid)
                LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW         9 (new_up)
                BUILD_MAP                2

 398            LOAD_CONST               7 ('warnings')
                LOAD_FAST               11 (warnings)

 399            LOAD_CONST               5 ('error_code')
                LOAD_FAST_BORROW        12 (db_status)
                LOAD_CONST              14 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L17)
                NOT_TAKEN
                LOAD_CONST              10 (None)
                JUMP_FORWARD             1 (to L18)
       L17:     LOAD_CONST              11 ('db_unavailable')

 394   L18:     BUILD_MAP                5

 400            LOAD_FAST_BORROW         4 (surface)

 394            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L19:     RETURN_VALUE

  --   L20:     PUSH_EXC_INFO

 381            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       95 (to L24)
                NOT_TAKEN
                STORE_FAST              13 (e)

 382   L21:     LOAD_GLOBAL             28 (logger)
                LOAD_ATTR               31 (warning + NULL|self)

 383            LOAD_CONST              15 ('incident_log update_status error type=')

 384            LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE

 383            BUILD_STRING             2

 382            CALL                     1
                POP_TOP

 386            LOAD_FAST               11 (warnings)
                LOAD_ATTR               15 (append + NULL|self)
                LOAD_CONST              16 ('db_update_failed:')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 387            LOAD_CONST              12 ('skipped')
                STORE_FAST              12 (db_status)
       L22:     POP_EXCEPT
                LOAD_CONST              10 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                JUMP_BACKWARD_NO_INTERRUPT 165 (to L14)

  --   L23:     LOAD_CONST              10 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RERAISE                  1

 381   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L26:     PUSH_EXC_INFO

 401            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L31)
                NOT_TAKEN
                STORE_FAST              13 (e)

 402   L27:     LOAD_GLOBAL             28 (logger)
                LOAD_ATTR               31 (warning + NULL|self)

 403            LOAD_CONST              21 ('update_incident_status error type=')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 402            CALL                     1
                POP_TOP

 405            LOAD_GLOBAL              7 (_final + NULL)

 406            LOAD_CONST               2 ('status')
                LOAD_CONST              12 ('skipped')

 407            LOAD_CONST               4 ('surface')
                LOAD_FAST                4 (surface)

 408            LOAD_CONST               5 ('error_code')
                LOAD_CONST              22 ('unexpected:')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 409            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 405            BUILD_MAP                4

 410            LOAD_FAST                4 (surface)

 405            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L28:     SWAP                     2
       L29:     POP_EXCEPT
                LOAD_CONST              10 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RETURN_VALUE

  --   L30:     LOAD_CONST              10 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RERAISE                  1

 401   L31:     RERAISE                  0

  --   L32:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L26 [0]
  L3 to L4 -> L26 [0]
  L5 to L6 -> L26 [0]
  L7 to L8 -> L26 [0]
  L9 to L10 -> L26 [0]
  L11 to L12 -> L26 [0]
  L13 to L14 -> L20 [0]
  L14 to L19 -> L26 [0]
  L20 to L21 -> L25 [1] lasti
  L21 to L22 -> L23 [1] lasti
  L22 to L23 -> L26 [0]
  L23 to L25 -> L25 [1] lasti
  L25 to L26 -> L26 [0]
  L26 to L27 -> L32 [1] lasti
  L27 to L28 -> L30 [1] lasti
  L28 to L29 -> L32 [1] lasti
  L30 to L32 -> L32 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app\services\operator\incident_log.py", line 413>:
413           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('incident_id')

415           LOAD_CONST               2 ('Any')

413           LOAD_CONST               3 ('resolution_code')

416           LOAD_CONST               2 ('Any')

413           LOAD_CONST               4 ('actor_type')

417           LOAD_CONST               2 ('Any')

413           LOAD_CONST               5 ('actor_id')

418           LOAD_CONST               2 ('Any')

413           LOAD_CONST               6 ('resolution_text')

419           LOAD_CONST               2 ('Any')

413           LOAD_CONST               7 ('return')

420           LOAD_CONST               8 ('Dict[str, Any]')

413           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object resolve_incident at 0x0000018C17E7F430, file "app\services\operator\incident_log.py", line 413>:
 413            RESUME                   0

 424            LOAD_CONST               1 ('ops.incident.resolve')
                STORE_FAST               5 (surface)

 425            NOP

 426    L1:     LOAD_GLOBAL              1 (_safe_str + NULL)
                LOAD_FAST_BORROW         0 (incident_id)
                LOAD_SMALL_INT          64
                CALL                     2
                STORE_FAST               6 (iid)

 427            LOAD_GLOBAL              3 (_safe_resolution_code + NULL)
                LOAD_FAST_BORROW         1 (resolution_code)
                CALL                     1
                STORE_FAST               7 (rcode)

 428            LOAD_GLOBAL              5 (_safe_actor_type + NULL)
                LOAD_FAST_BORROW         2 (actor_type)
                CALL                     1
                STORE_FAST               8 (atype)

 429            LOAD_GLOBAL              7 (_safe_actor_id + NULL)
                LOAD_FAST_BORROW         3 (actor_id)
                CALL                     1
                STORE_FAST               9 (aid)

 430            LOAD_GLOBAL              9 (_safe_resolution + NULL)
                LOAD_FAST_BORROW         4 (resolution_text)
                CALL                     1
                STORE_FAST              10 (rtext)

 431            LOAD_FAST_BORROW         6 (iid)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L7)
                NOT_TAKEN
                LOAD_FAST_BORROW         7 (rcode)
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L7)
        L2:     NOT_TAKEN
        L3:     LOAD_FAST_BORROW         8 (atype)
                TO_BOOL
                POP_JUMP_IF_FALSE        9 (to L7)
        L4:     NOT_TAKEN
        L5:     LOAD_FAST_BORROW         9 (aid)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L9)
        L6:     NOT_TAKEN

 432    L7:     LOAD_GLOBAL             11 (_final + NULL)

 433            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 434            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         5 (surface)

 435            LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('invalid_arguments')

 436            LOAD_CONST               7 ('warnings')
                LOAD_CONST               6 ('invalid_arguments')
                BUILD_LIST               1

 432            BUILD_MAP                4

 437            LOAD_FAST_BORROW         5 (surface)

 432            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L8:     RETURN_VALUE

 438    L9:     LOAD_GLOBAL             13 (_now_iso + NULL)
                CALL                     0
                STORE_FAST              11 (now)

 440            LOAD_CONST               2 ('status')
                LOAD_GLOBAL             14 (STATUS_RESOLVED)

 441            LOAD_CONST               9 ('resolved_at')
                LOAD_FAST_BORROW        11 (now)

 442            LOAD_CONST              10 ('resolved_by_actor_type')
                LOAD_FAST_BORROW         8 (atype)

 443            LOAD_CONST              11 ('resolved_by_actor_id')
                LOAD_FAST_BORROW         9 (aid)

 444            LOAD_CONST              12 ('resolution_code')
                LOAD_FAST_BORROW         7 (rcode)

 439            BUILD_MAP                5
                STORE_FAST              12 (updates)

 446            LOAD_FAST_BORROW        10 (rtext)
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L10)
                NOT_TAKEN

 447            LOAD_CONST              13 ('resolution_text')
                LOAD_FAST_BORROW        10 (rtext)
                BUILD_MAP                1
                LOAD_FAST_BORROW        12 (updates)
                LOAD_CONST              14 ('metadata')
                STORE_SUBSCR

 448   L10:     LOAD_GLOBAL             17 (_get_db + NULL)
                CALL                     0
                STORE_FAST              13 (db)

 449            BUILD_LIST               0
                STORE_FAST              14 (warnings)

 450            LOAD_FAST_BORROW        13 (db)
                POP_JUMP_IF_NOT_NONE    21 (to L11)
                NOT_TAKEN

 451            LOAD_FAST_BORROW        14 (warnings)
                LOAD_ATTR               19 (append + NULL|self)
                LOAD_CONST              16 ('db_unavailable')
                CALL                     1
                POP_TOP

 452            LOAD_CONST              17 ('skipped')
                STORE_FAST              15 (db_status)
                JUMP_FORWARD            69 (to L13)

 454   L11:     NOP

 455   L12:     LOAD_FAST_BORROW        13 (db)
                LOAD_ATTR               21 (table + NULL|self)
                LOAD_GLOBAL             22 (_TABLE_NAME)
                CALL                     1
                LOAD_ATTR               25 (update + NULL|self)
                LOAD_FAST_BORROW        12 (updates)
                CALL                     1
                LOAD_ATTR               27 (eq + NULL|self)
                LOAD_CONST              18 ('incident_id')
                LOAD_FAST_BORROW         6 (iid)
                CALL                     2
                LOAD_ATTR               29 (execute + NULL|self)
                CALL                     0
                POP_TOP

 456            LOAD_CONST              19 ('ok')
                STORE_FAST              15 (db_status)

 463   L13:     LOAD_GLOBAL             41 (_emit_event + NULL)
                LOAD_CONST              22 ('incident.resolved')

 464            LOAD_CONST              18 ('incident_id')
                LOAD_FAST_BORROW         6 (iid)

 465            LOAD_CONST              23 ('actor_type')
                LOAD_FAST_BORROW         8 (atype)

 466            LOAD_CONST              24 ('actor_id')
                LOAD_FAST_BORROW         9 (aid)

 467            LOAD_CONST               2 ('status')
                LOAD_GLOBAL             14 (STATUS_RESOLVED)

 468            LOAD_CONST              12 ('resolution_code')
                LOAD_FAST_BORROW         7 (rcode)

 463            BUILD_MAP                5
                CALL                     2
                POP_TOP

 470            LOAD_GLOBAL             11 (_final + NULL)

 471            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW        15 (db_status)
                LOAD_CONST              19 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN
                LOAD_CONST              19 ('ok')
                JUMP_FORWARD             1 (to L15)
       L14:     LOAD_CONST              17 ('skipped')

 472   L15:     LOAD_CONST               4 ('surface')
                LOAD_FAST                5 (surface)

 473            LOAD_CONST              25 ('row')

 474            LOAD_CONST              18 ('incident_id')
                LOAD_FAST_BORROW         6 (iid)

 475            LOAD_CONST               2 ('status')
                LOAD_GLOBAL             14 (STATUS_RESOLVED)

 476            LOAD_CONST               9 ('resolved_at')
                LOAD_FAST_BORROW        11 (now)

 477            LOAD_CONST              10 ('resolved_by_actor_type')
                LOAD_FAST_BORROW         8 (atype)

 478            LOAD_CONST              11 ('resolved_by_actor_id')
                LOAD_FAST_BORROW         9 (aid)

 479            LOAD_CONST              12 ('resolution_code')
                LOAD_FAST_BORROW         7 (rcode)

 473            BUILD_MAP                6

 481            LOAD_CONST               7 ('warnings')
                LOAD_FAST               14 (warnings)

 482            LOAD_CONST               5 ('error_code')
                LOAD_FAST_BORROW        15 (db_status)
                LOAD_CONST              19 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L16)
                NOT_TAKEN
                LOAD_CONST              15 (None)
                JUMP_FORWARD             1 (to L17)
       L16:     LOAD_CONST              16 ('db_unavailable')

 470   L17:     BUILD_MAP                5

 483            LOAD_FAST_BORROW         5 (surface)

 470            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L18:     RETURN_VALUE

  --   L19:     PUSH_EXC_INFO

 457            LOAD_GLOBAL             30 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       95 (to L23)
                NOT_TAKEN
                STORE_FAST              16 (e)

 458   L20:     LOAD_GLOBAL             32 (logger)
                LOAD_ATTR               35 (warning + NULL|self)

 459            LOAD_CONST              20 ('incident_log resolve error type=')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST               16 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 458            CALL                     1
                POP_TOP

 461            LOAD_FAST               14 (warnings)
                LOAD_ATTR               19 (append + NULL|self)
                LOAD_CONST              21 ('db_update_failed:')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST               16 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 462            LOAD_CONST              17 ('skipped')
                STORE_FAST              15 (db_status)
       L21:     POP_EXCEPT
                LOAD_CONST              15 (None)
                STORE_FAST              16 (e)
                DELETE_FAST             16 (e)
                JUMP_BACKWARD_NO_INTERRUPT 183 (to L13)

  --   L22:     LOAD_CONST              15 (None)
                STORE_FAST              16 (e)
                DELETE_FAST             16 (e)
                RERAISE                  1

 457   L23:     RERAISE                  0

  --   L24:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L25:     PUSH_EXC_INFO

 484            LOAD_GLOBAL             30 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L30)
                NOT_TAKEN
                STORE_FAST              16 (e)

 485   L26:     LOAD_GLOBAL             32 (logger)
                LOAD_ATTR               35 (warning + NULL|self)

 486            LOAD_CONST              26 ('resolve_incident error type=')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST               16 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 485            CALL                     1
                POP_TOP

 488            LOAD_GLOBAL             11 (_final + NULL)

 489            LOAD_CONST               2 ('status')
                LOAD_CONST              17 ('skipped')

 490            LOAD_CONST               4 ('surface')
                LOAD_FAST                5 (surface)

 491            LOAD_CONST               5 ('error_code')
                LOAD_CONST              27 ('unexpected:')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST               16 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 492            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 488            BUILD_MAP                4

 493            LOAD_FAST                5 (surface)

 488            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L27:     SWAP                     2
       L28:     POP_EXCEPT
                LOAD_CONST              15 (None)
                STORE_FAST              16 (e)
                DELETE_FAST             16 (e)
                RETURN_VALUE

  --   L29:     LOAD_CONST              15 (None)
                STORE_FAST              16 (e)
                DELETE_FAST             16 (e)
                RERAISE                  1

 484   L30:     RERAISE                  0

  --   L31:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L25 [0]
  L3 to L4 -> L25 [0]
  L5 to L6 -> L25 [0]
  L7 to L8 -> L25 [0]
  L9 to L11 -> L25 [0]
  L12 to L13 -> L19 [0]
  L13 to L18 -> L25 [0]
  L19 to L20 -> L24 [1] lasti
  L20 to L21 -> L22 [1] lasti
  L21 to L22 -> L25 [0]
  L22 to L24 -> L24 [1] lasti
  L24 to L25 -> L25 [0]
  L25 to L26 -> L31 [1] lasti
  L26 to L27 -> L29 [1] lasti
  L27 to L28 -> L31 [1] lasti
  L29 to L31 -> L31 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026530, file "app\services\operator\incident_log.py", line 496>:
496           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

498           LOAD_CONST               2 ('Any')

496           LOAD_CONST               3 ('severity')

499           LOAD_CONST               2 ('Any')

496           LOAD_CONST               4 ('status')

500           LOAD_CONST               2 ('Any')

496           LOAD_CONST               5 ('limit')

501           LOAD_CONST               2 ('Any')

496           LOAD_CONST               6 ('return')

502           LOAD_CONST               7 ('Dict[str, Any]')

496           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object list_incidents at 0x0000018C17D7CFC0, file "app\services\operator\incident_log.py", line 496>:
 496            RESUME                   0

 504            LOAD_CONST               1 ('ops.incident.list')
                STORE_FAST               4 (surface)

 505            NOP

 506    L1:     LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               2 (None)
        L3:     STORE_FAST               5 (bid)

 507            LOAD_FAST_BORROW         1 (severity)
                POP_JUMP_IF_NONE        12 (to L4)
                NOT_TAKEN
                LOAD_GLOBAL              3 (_safe_severity + NULL)
                LOAD_FAST_BORROW         1 (severity)
                CALL                     1
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               2 (None)
        L5:     STORE_FAST               6 (sev)

 508            LOAD_CONST               2 (None)
                STORE_FAST               7 (stat)

 509            LOAD_FAST_BORROW         2 (status)
                POP_JUMP_IF_NONE        62 (to L6)
                NOT_TAKEN

 510            LOAD_GLOBAL              5 (_safe_str + NULL)
                LOAD_FAST_BORROW         2 (status)
                LOAD_SMALL_INT          32
                CALL                     2
                STORE_FAST               8 (s)

 511            LOAD_FAST_BORROW         8 (s)
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L6)
                NOT_TAKEN
                LOAD_FAST_BORROW         8 (s)
                LOAD_ATTR                7 (upper + NULL|self)
                CALL                     0
                LOAD_GLOBAL              8 (_VALID_STATUSES)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       17 (to L6)
                NOT_TAKEN

 512            LOAD_FAST_BORROW         8 (s)
                LOAD_ATTR                7 (upper + NULL|self)
                CALL                     0
                STORE_FAST               7 (stat)

 513    L6:     LOAD_SMALL_INT          50
                STORE_FAST               9 (cap)

 514    L7:     NOP

 515    L8:     LOAD_GLOBAL             11 (int + NULL)
                LOAD_FAST_BORROW         3 (limit)
                CALL                     1
                STORE_FAST               9 (cap)

 518    L9:     LOAD_FAST_BORROW         9 (cap)
                LOAD_SMALL_INT           1
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN

 519            LOAD_SMALL_INT           1
                STORE_FAST               9 (cap)

 520   L10:     LOAD_FAST_BORROW         9 (cap)
                LOAD_CONST               3 (500)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN

 521            LOAD_CONST               3 (500)
                STORE_FAST               9 (cap)

 522   L11:     LOAD_GLOBAL             17 (_get_db + NULL)
                CALL                     0
                STORE_FAST              10 (db)

 523            LOAD_FAST_BORROW        10 (db)
                POP_JUMP_IF_NOT_NONE    27 (to L13)
                NOT_TAKEN

 524            LOAD_GLOBAL             19 (_final + NULL)

 525            LOAD_CONST               4 ('status')
                LOAD_CONST               5 ('skipped')

 526            LOAD_CONST               6 ('surface')
                LOAD_FAST_BORROW         4 (surface)

 527            LOAD_CONST               7 ('rows')
                BUILD_LIST               0

 528            LOAD_CONST               8 ('count')
                LOAD_SMALL_INT           0

 529            LOAD_CONST               9 ('warnings')
                LOAD_CONST              10 ('db_unavailable')
                BUILD_LIST               1

 530            LOAD_CONST              11 ('error_code')
                LOAD_CONST              10 ('db_unavailable')

 524            BUILD_MAP                6

 531            LOAD_FAST_BORROW         4 (surface)

 524            LOAD_CONST              12 (('surface',))
                CALL_KW                  2
       L12:     RETURN_VALUE

 532   L13:     NOP

 533   L14:     LOAD_FAST_BORROW        10 (db)
                LOAD_ATTR               21 (table + NULL|self)
                LOAD_GLOBAL             22 (_TABLE_NAME)
                CALL                     1
                LOAD_ATTR               25 (select + NULL|self)
                LOAD_CONST              13 ('*')
                CALL                     1
                STORE_FAST              11 (q)

 534            LOAD_FAST_BORROW         5 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L17)
       L15:     NOT_TAKEN

 535   L16:     LOAD_FAST_BORROW        11 (q)
                LOAD_ATTR               27 (eq + NULL|self)
                LOAD_CONST              14 ('brokerage_id')
                LOAD_FAST_BORROW         5 (bid)
                CALL                     2
                STORE_FAST              11 (q)

 536   L17:     LOAD_FAST_BORROW         6 (sev)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L20)
       L18:     NOT_TAKEN

 537   L19:     LOAD_FAST_BORROW        11 (q)
                LOAD_ATTR               27 (eq + NULL|self)
                LOAD_CONST              15 ('severity')
                LOAD_FAST_BORROW         6 (sev)
                CALL                     2
                STORE_FAST              11 (q)

 538   L20:     LOAD_FAST_BORROW         7 (stat)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L23)
       L21:     NOT_TAKEN

 539   L22:     LOAD_FAST_BORROW        11 (q)
                LOAD_ATTR               27 (eq + NULL|self)
                LOAD_CONST               4 ('status')
                LOAD_FAST_BORROW         7 (stat)
                CALL                     2
                STORE_FAST              11 (q)

 540   L23:     LOAD_FAST_BORROW        11 (q)
                LOAD_ATTR               29 (order + NULL|self)
                LOAD_CONST              16 ('opened_at')
                LOAD_CONST              17 (True)
                LOAD_CONST              18 (('desc',))
                CALL_KW                  2
                LOAD_ATTR               31 (limit + NULL|self)
                LOAD_FAST_BORROW         9 (cap)
                CALL                     1
                STORE_FAST              11 (q)

 541            LOAD_FAST_BORROW        11 (q)
                LOAD_ATTR               33 (execute + NULL|self)
                CALL                     0
                STORE_FAST              12 (resp)

 554   L24:     LOAD_GLOBAL             45 (getattr + NULL)
                LOAD_FAST               12 (resp)
                LOAD_CONST              22 ('data')
                LOAD_CONST               2 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L27)
       L25:     NOT_TAKEN
       L26:     POP_TOP
                BUILD_LIST               0
       L27:     STORE_FAST              14 (data)

 555            BUILD_LIST               0
                STORE_FAST              15 (rows)

 556            LOAD_FAST               14 (data)
                LOAD_CONST               2 (None)
                LOAD_FAST                9 (cap)
                BINARY_SLICE
                GET_ITER
       L28:     FOR_ITER                53 (to L31)
                STORE_FAST              16 (r)

 557            LOAD_GLOBAL             47 (isinstance + NULL)
                LOAD_FAST               16 (r)
                LOAD_GLOBAL             48 (dict)
                CALL                     2
                TO_BOOL
       L29:     POP_JUMP_IF_TRUE         3 (to L30)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L28)

 558   L30:     LOAD_FAST               15 (rows)
                LOAD_ATTR               51 (append + NULL|self)
                LOAD_GLOBAL             53 (_project_row + NULL)
                LOAD_FAST               16 (r)
                CALL                     1
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           55 (to L28)

 556   L31:     END_FOR
                POP_ITER

 559            LOAD_GLOBAL             19 (_final + NULL)

 560            LOAD_CONST               4 ('status')
                LOAD_CONST              23 ('ok')

 561            LOAD_CONST               6 ('surface')
                LOAD_FAST                4 (surface)

 562            LOAD_CONST               7 ('rows')
                LOAD_FAST               15 (rows)

 563            LOAD_CONST               8 ('count')
                LOAD_GLOBAL             55 (len + NULL)
                LOAD_FAST               15 (rows)
                CALL                     1

 564            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 565            LOAD_CONST              11 ('error_code')
                LOAD_CONST               2 (None)

 559            BUILD_MAP                6

 566            LOAD_FAST                4 (surface)

 559            LOAD_CONST              12 (('surface',))
                CALL_KW                  2
       L32:     RETURN_VALUE

  --   L33:     PUSH_EXC_INFO

 516            LOAD_GLOBAL             12 (TypeError)
                LOAD_GLOBAL             14 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        7 (to L35)
                NOT_TAKEN
                POP_TOP

 517            LOAD_SMALL_INT          50
                STORE_FAST               9 (cap)
       L34:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 366 (to L9)

 516   L35:     RERAISE                  0

  --   L36:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L37:     PUSH_EXC_INFO

 542            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      102 (to L43)
                NOT_TAKEN
                STORE_FAST              13 (e)

 543   L38:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 544            LOAD_CONST              19 ('list_incidents query error type=')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 543            CALL                     1
                POP_TOP

 546            LOAD_GLOBAL             19 (_final + NULL)

 547            LOAD_CONST               4 ('status')
                LOAD_CONST               5 ('skipped')

 548            LOAD_CONST               6 ('surface')
                LOAD_FAST                4 (surface)

 549            LOAD_CONST               7 ('rows')
                BUILD_LIST               0

 550            LOAD_CONST               8 ('count')
                LOAD_SMALL_INT           0

 551            LOAD_CONST               9 ('warnings')
                LOAD_CONST              20 ('db_query_failed:')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 552            LOAD_CONST              11 ('error_code')
                LOAD_CONST              21 ('db_query_failed')

 546            BUILD_MAP                6

 553            LOAD_FAST                4 (surface)

 546            LOAD_CONST              12 (('surface',))
                CALL_KW                  2
       L39:     SWAP                     2
       L40:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
       L41:     RETURN_VALUE

  --   L42:     LOAD_CONST               2 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RERAISE                  1

 542   L43:     RERAISE                  0

  --   L44:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L45:     PUSH_EXC_INFO

 567            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      101 (to L50)
                NOT_TAKEN
                STORE_FAST              13 (e)

 568   L46:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 569            LOAD_CONST              24 ('list_incidents error type=')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 568            CALL                     1
                POP_TOP

 571            LOAD_GLOBAL             19 (_final + NULL)

 572            LOAD_CONST               4 ('status')
                LOAD_CONST               5 ('skipped')

 573            LOAD_CONST               6 ('surface')
                LOAD_FAST                4 (surface)

 574            LOAD_CONST               7 ('rows')
                BUILD_LIST               0

 575            LOAD_CONST               8 ('count')
                LOAD_SMALL_INT           0

 576            LOAD_CONST              11 ('error_code')
                LOAD_CONST              25 ('unexpected:')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 577            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 571            BUILD_MAP                6

 578            LOAD_FAST                4 (surface)

 571            LOAD_CONST              12 (('surface',))
                CALL_KW                  2
       L47:     SWAP                     2
       L48:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RETURN_VALUE

  --   L49:     LOAD_CONST               2 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RERAISE                  1

 567   L50:     RERAISE                  0

  --   L51:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L7 -> L45 [0]
  L8 to L9 -> L33 [0]
  L9 to L12 -> L45 [0]
  L14 to L15 -> L37 [0]
  L16 to L18 -> L37 [0]
  L19 to L21 -> L37 [0]
  L22 to L24 -> L37 [0]
  L24 to L25 -> L45 [0]
  L26 to L29 -> L45 [0]
  L30 to L32 -> L45 [0]
  L33 to L34 -> L36 [1] lasti
  L34 to L35 -> L45 [0]
  L35 to L36 -> L36 [1] lasti
  L36 to L37 -> L45 [0]
  L37 to L38 -> L44 [1] lasti
  L38 to L39 -> L42 [1] lasti
  L39 to L40 -> L44 [1] lasti
  L40 to L41 -> L45 [0]
  L42 to L44 -> L44 [1] lasti
  L44 to L45 -> L45 [0]
  L45 to L46 -> L51 [1] lasti
  L46 to L47 -> L49 [1] lasti
  L47 to L48 -> L51 [1] lasti
  L49 to L51 -> L51 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app\services\operator\incident_log.py", line 581>:
581           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('incident_id')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object get_incident at 0x0000018C17F69200, file "app\services\operator\incident_log.py", line 581>:
 581            RESUME                   0

 582            LOAD_CONST               0 ('ops.incident.get')
                STORE_FAST               1 (surface)

 583            NOP

 584    L1:     LOAD_GLOBAL              1 (_safe_str + NULL)
                LOAD_FAST_BORROW         0 (incident_id)
                LOAD_SMALL_INT          64
                CALL                     2
                STORE_FAST               2 (iid)

 585            LOAD_FAST_BORROW         2 (iid)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L3)
                NOT_TAKEN

 586            LOAD_GLOBAL              3 (_final + NULL)

 587            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 588            LOAD_CONST               3 ('surface')
                LOAD_FAST_BORROW         1 (surface)

 589            LOAD_CONST               4 ('error_code')
                LOAD_CONST               5 ('invalid_incident_id')

 590            LOAD_CONST               6 ('warnings')
                LOAD_CONST               5 ('invalid_incident_id')
                BUILD_LIST               1

 586            BUILD_MAP                4

 591            LOAD_FAST_BORROW         1 (surface)

 586            LOAD_CONST               7 (('surface',))
                CALL_KW                  2
        L2:     RETURN_VALUE

 592    L3:     LOAD_GLOBAL              5 (_get_db + NULL)
                CALL                     0
                STORE_FAST               3 (db)

 593            LOAD_FAST_BORROW         3 (db)
                POP_JUMP_IF_NOT_NONE    23 (to L5)
                NOT_TAKEN

 594            LOAD_GLOBAL              3 (_final + NULL)

 595            LOAD_CONST               1 ('status')
                LOAD_CONST               9 ('skipped')

 596            LOAD_CONST               3 ('surface')
                LOAD_FAST_BORROW         1 (surface)

 597            LOAD_CONST               6 ('warnings')
                LOAD_CONST              10 ('db_unavailable')
                BUILD_LIST               1

 598            LOAD_CONST               4 ('error_code')
                LOAD_CONST              10 ('db_unavailable')

 594            BUILD_MAP                4

 599            LOAD_FAST_BORROW         1 (surface)

 594            LOAD_CONST               7 (('surface',))
                CALL_KW                  2
        L4:     RETURN_VALUE

 600    L5:     NOP

 602    L6:     LOAD_FAST_BORROW         3 (db)
                LOAD_ATTR                7 (table + NULL|self)
                LOAD_GLOBAL              8 (_TABLE_NAME)
                CALL                     1

 603            LOAD_ATTR               11 (select + NULL|self)
                LOAD_CONST              11 ('*')
                CALL                     1

 604            LOAD_ATTR               13 (eq + NULL|self)
                LOAD_CONST              12 ('incident_id')
                LOAD_FAST_BORROW         2 (iid)
                CALL                     2

 605            LOAD_ATTR               15 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 606            LOAD_ATTR               17 (execute + NULL|self)
                CALL                     0

 601            STORE_FAST               4 (resp)

 618    L7:     LOAD_GLOBAL             29 (getattr + NULL)
                LOAD_FAST                4 (resp)
                LOAD_CONST              16 ('data')
                LOAD_CONST               8 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                BUILD_LIST               0
       L10:     STORE_FAST               6 (data)

 619            LOAD_FAST                6 (data)
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L13)
       L11:     NOT_TAKEN
       L12:     LOAD_GLOBAL             31 (isinstance + NULL)
                LOAD_FAST                6 (data)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_GLOBAL             32 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L15)
                NOT_TAKEN

 620   L13:     LOAD_GLOBAL              3 (_final + NULL)

 621            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 622            LOAD_CONST               3 ('surface')
                LOAD_FAST                1 (surface)

 623            LOAD_CONST               4 ('error_code')
                LOAD_CONST              17 ('incident_not_found')

 624            LOAD_CONST               6 ('warnings')
                LOAD_CONST              17 ('incident_not_found')
                BUILD_LIST               1

 620            BUILD_MAP                4

 625            LOAD_FAST                1 (surface)

 620            LOAD_CONST               7 (('surface',))
                CALL_KW                  2
       L14:     RETURN_VALUE

 626   L15:     LOAD_GLOBAL              3 (_final + NULL)

 627            LOAD_CONST               1 ('status')
                LOAD_CONST              18 ('ok')

 628            LOAD_CONST               3 ('surface')
                LOAD_FAST                1 (surface)

 629            LOAD_CONST              19 ('row')
                LOAD_GLOBAL             35 (_project_row + NULL)
                LOAD_FAST                6 (data)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1

 630            LOAD_CONST               6 ('warnings')
                BUILD_LIST               0

 631            LOAD_CONST               4 ('error_code')
                LOAD_CONST               8 (None)

 626            BUILD_MAP                5

 632            LOAD_FAST                1 (surface)

 626            LOAD_CONST               7 (('surface',))
                CALL_KW                  2
       L16:     RETURN_VALUE

  --   L17:     PUSH_EXC_INFO

 608            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       98 (to L23)
                NOT_TAKEN
                STORE_FAST               5 (e)

 609   L18:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 610            LOAD_CONST              13 ('get_incident query error type=')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 609            CALL                     1
                POP_TOP

 612            LOAD_GLOBAL              3 (_final + NULL)

 613            LOAD_CONST               1 ('status')
                LOAD_CONST               9 ('skipped')

 614            LOAD_CONST               3 ('surface')
                LOAD_FAST                1 (surface)

 615            LOAD_CONST               6 ('warnings')
                LOAD_CONST              14 ('db_query_failed:')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 616            LOAD_CONST               4 ('error_code')
                LOAD_CONST              15 ('db_query_failed')

 612            BUILD_MAP                4

 617            LOAD_FAST                1 (surface)

 612            LOAD_CONST               7 (('surface',))
                CALL_KW                  2
       L19:     SWAP                     2
       L20:     POP_EXCEPT
                LOAD_CONST               8 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
       L21:     RETURN_VALUE

  --   L22:     LOAD_CONST               8 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 608   L23:     RERAISE                  0

  --   L24:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L25:     PUSH_EXC_INFO

 633            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L30)
                NOT_TAKEN
                STORE_FAST               5 (e)

 634   L26:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 635            LOAD_CONST              20 ('get_incident error type=')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 634            CALL                     1
                POP_TOP

 637            LOAD_GLOBAL              3 (_final + NULL)

 638            LOAD_CONST               1 ('status')
                LOAD_CONST               9 ('skipped')

 639            LOAD_CONST               3 ('surface')
                LOAD_FAST                1 (surface)

 640            LOAD_CONST               4 ('error_code')
                LOAD_CONST              21 ('unexpected:')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 641            LOAD_CONST               6 ('warnings')
                BUILD_LIST               0

 637            BUILD_MAP                4

 642            LOAD_FAST                1 (surface)

 637            LOAD_CONST               7 (('surface',))
                CALL_KW                  2
       L27:     SWAP                     2
       L28:     POP_EXCEPT
                LOAD_CONST               8 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RETURN_VALUE

  --   L29:     LOAD_CONST               8 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 633   L30:     RERAISE                  0

  --   L31:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L25 [0]
  L3 to L4 -> L25 [0]
  L6 to L7 -> L17 [0]
  L7 to L8 -> L25 [0]
  L9 to L11 -> L25 [0]
  L12 to L14 -> L25 [0]
  L15 to L16 -> L25 [0]
  L17 to L18 -> L24 [1] lasti
  L18 to L19 -> L22 [1] lasti
  L19 to L20 -> L24 [1] lasti
  L20 to L21 -> L25 [0]
  L22 to L24 -> L24 [1] lasti
  L24 to L25 -> L25 [0]
  L25 to L26 -> L31 [1] lasti
  L26 to L27 -> L29 [1] lasti
  L27 to L28 -> L31 [1] lasti
  L29 to L31 -> L31 [1] lasti
```
