# operator/circuit_breaker

- **pyc:** `app\services\operator\__pycache__\circuit_breaker.cpython-314.pyc`
- **expected source path (absent):** `app\services\operator/circuit_breaker.py`
- **co_filename (from bytecode):** `app\services\operator\circuit_breaker.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** operator

## Module docstring

```
PAS188 — Per-brokerage circuit-breaker service.

Records and reads operator-driven circuit-breaker state
per brokerage. The breaker is an **advisory flag** — it
advertises that a brokerage should be treated as offline
by upstream surfaces (dashboard, daily checklist, fleet
status) but does NOT directly mutate Twilio / Cal.com /
the FSM / the worker / the dialer.

Doctrine:

* **Operator-driven only.** ``trip_breaker`` and
  ``reset_breaker`` require an actor; PAS surfaces NEVER
  auto-trip or auto-reset. PAS188 contains NO logic that
  observes a metric and trips a breaker.
* **No external side-effects.** Tripping a breaker is a
  row insert + an audit event. It does NOT disable
  Twilio inbound, suspend Cal.com webhooks, or alter
  worker scheduling.
* **Closed status + reason enums.** Mirrors v37 CHECK
  constraints exactly.
* **No PII / no secrets.** Free-text rationale is
  trimmed to 2 KB and stored in ``metadata.rationale_text``.
* **Append-only-ish ledger.** Each call inserts a new row;
  ``current_breaker_state(brokerage_id)`` returns the
  most-recent row. UPDATE is reserved for the canonical
  service_role writer (transitions between OK / TRIPPED /
  RESETTING on the same row).
* **NEVER raises.** DB-unavailable -> ``status="skipped"``
  + warning; in-memory state is still returned.

Public surface:

  * ``trip_breaker(...)``
  * ``reset_breaker(...)``
  * ``current_breaker_state(...)``
  * ``list_breakers(...)``
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.event_logger`, `app.db.supabase_client`, `datetime`, `get_supabase`, `log_event_bg`, `logging`, `timezone`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_emit_event`, `_final`, `_get_db`, `_now_iso`, `_project_row`, `_safe_actor_id`, `_safe_actor_type`, `_safe_brokerage`, `_safe_rationale`, `_safe_reason`, `_safe_str`, `_scan_for_forbidden`, `current_breaker_state`, `list_breakers`, `reset_breaker`, `trip_breaker`

## Env-key candidates

`OPERATOR_REQUESTED`, `RESETTING`, `ROLLBACK_INITIATED`, `S1_INBOUND_FAILING`, `S2_AUDIT_INTEGRITY_RISK`, `S3_PII_OR_SECRET_EXPOSURE`, `S4_OPERATOR_BLOCKING_UI`, `S5_SLOW_OR_NOISY`, `TRIPPED`

## String constants (redacted where noted)

- '\nPAS188 — Per-brokerage circuit-breaker service.\n\nRecords and reads operator-driven circuit-breaker state\nper brokerage. The breaker is an **advisory flag** — it\nadvertises that a brokerage should be treated as offline\nby upstream surfaces (dashboard, daily checklist, fleet\nstatus) but does NOT directly mutate Twilio / Cal.com /\nthe FSM / the worker / the dialer.\n\nDoctrine:\n\n* **Operator-driven only.** ``trip_breaker`` and\n  ``reset_breaker`` require an actor; PAS surfaces NEVER\n  auto-trip or auto-reset. PAS188 contains NO logic that\n  observes a metric and trips a breaker.\n* **No external side-effects.** Tripping a breaker is a\n  row insert + an audit event. It does NOT disable\n  Twilio inbound, suspend Cal.com webhooks, or alter\n  worker scheduling.\n* **Closed status + reason enums.** Mirrors v37 CHECK\n  constraints exactly.\n* **No PII / no secrets.** Free-text rationale is\n  trimmed to 2 KB and stored in ``metadata.rationale_text``.\n* **Append-only-ish ledger.** Each call inserts a new row;\n  ``current_breaker_state(brokerage_id)`` returns the\n  most-recent row. UPDATE is reserved for the canonical\n  service_role writer (transitions between OK / TRIPPED /\n  RESETTING on the same row).\n* **NEVER raises.** DB-unavailable -> ``status="skipped"``\n  + warning; in-memory state is still returned.\n\nPublic surface:\n\n  * ``trip_breaker(...)``\n  * ``reset_breaker(...)``\n  * ``current_breaker_state(...)``\n  * ``list_breakers(...)``\n'
- 'pas.operator.circuit_breaker'
- 'pas_brokerage_circuit_breakers'
- 'TRIPPED'
- 'RESETTING'
- 'S1_INBOUND_FAILING'
- 'S2_AUDIT_INTEGRITY_RISK'
- 'S3_PII_OR_SECRET_EXPOSURE'
- 'S4_OPERATOR_BLOCKING_UI'
- 'S5_SLOW_OR_NOISY'
- 'OPERATOR_REQUESTED'
- 'ROLLBACK_INITIATED'
- 'status'
- 'rationale'
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
- 'circuit_breaker surface='
- ' collapsed — forbidden token leaked'
- 'failed'
- 'error_code'
- 'breaker_envelope_forbidden_token'
- 'warnings'
- 'row'
- 'event_type'
- 'payload'
- 'None'
- 'brokerage_id'
- 'reason_code'
- 'actor_type'
- 'actor_id'
- 'Operator-driven breaker trip. Records a new row with\nstatus=TRIPPED. Does NOT mutate Twilio / Cal.com /\nthe worker.'
- 'ops.circuit_breaker.trip'
- 'invalid_brokerage_id'
- 'invalid_reason_code'
- 'invalid_actor'
- 'breaker_id'
- 'tripped_at'
- 'tripped_by_actor_type'
- 'tripped_by_actor_id'
- 'updated_at'
- 'rationale_text'
- 'db_unavailable'
- 'skipped'
- 'metadata'
- 'circuit_breaker trip insert error type='
- 'db_insert_failed:'
- 'circuit_breaker.tripped'
- 'trip_breaker error type='
- 'unexpected:'
- 'Operator-driven breaker reset. Records a new row\nwith status=OK. Does NOT re-enable Twilio / Cal.com /\nthe worker — those mutations are SEPARATE operator\nactions.'
- 'ops.circuit_breaker.reset'
- 'reset_at'
- 'reset_by_actor_type'
- 'reset_by_actor_id'
- 'circuit_breaker reset insert error type='
- 'circuit_breaker.reset'
- 'action_required'
- 'operator_must_re_enable_inbound_externally'
- 'reset_breaker error type='
- 'Returns the most-recent breaker row for the brokerage.\nDB unavailable -> `status="skipped"` + a row with\n`status=OK` (fail-safe: assume open if we cannot read\nthe ledger).'
- 'ops.circuit_breaker.current'
- 'current_breaker_state query error type='
- 'db_query_failed:'
- 'db_query_failed'
- 'data'
- 'current_breaker_state error type='
- 'Read-only listing of breaker rows. Bounded to closed\nallow-list.'
- 'ops.circuit_breaker.list'
- 'rows'
- 'count'
- 'list_breakers query error type='
- 'list_breakers error type='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS188 — Per-brokerage circuit-breaker service.\n\nRecords and reads operator-driven circuit-breaker state\nper brokerage. The breaker is an **advisory flag** — it\nadvertises that a brokerage should be treated as offline\nby upstream surfaces (dashboard, daily checklist, fleet\nstatus) but does NOT directly mutate Twilio / Cal.com /\nthe FSM / the worker / the dialer.\n\nDoctrine:\n\n* **Operator-driven only.** ``trip_breaker`` and\n  ``reset_breaker`` require an actor; PAS surfaces NEVER\n  auto-trip or auto-reset. PAS188 contains NO logic that\n  observes a metric and trips a breaker.\n* **No external side-effects.** Tripping a breaker is a\n  row insert + an audit event. It does NOT disable\n  Twilio inbound, suspend Cal.com webhooks, or alter\n  worker scheduling.\n* **Closed status + reason enums.** Mirrors v37 CHECK\n  constraints exactly.\n* **No PII / no secrets.** Free-text rationale is\n  trimmed to 2 KB and stored in ``metadata.rationale_text``.\n* **Append-only-ish ledger.** Each call inserts a new row;\n  ``current_breaker_state(brokerage_id)`` returns the\n  most-recent row. UPDATE is reserved for the canonical\n  service_role writer (transitions between OK / TRIPPED /\n  RESETTING on the same row).\n* **NEVER raises.** DB-unavailable -> ``status="skipped"``\n  + warning; in-memory state is still returned.\n\nPublic surface:\n\n  * ``trip_breaker(...)``\n  * ``reset_breaker(...)``\n  * ``current_breaker_state(...)``\n  * ``list_breakers(...)``\n')
              STORE_NAME               0 (__doc__)

 41           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 43           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 44           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (uuid)
              STORE_NAME               4 (uuid)

 45           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timezone'))
              IMPORT_NAME              5 (datetime)
              IMPORT_FROM              5 (datetime)
              STORE_NAME               5 (datetime)
              IMPORT_FROM              6 (timezone)
              STORE_NAME               6 (timezone)
              POP_TOP

 46           LOAD_SMALL_INT           0
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

 49           LOAD_NAME                3 (logging)
              LOAD_ATTR               24 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.operator.circuit_breaker')
              CALL                     1
              STORE_NAME              13 (logger)

 56           LOAD_CONST               6 ('pas_brokerage_circuit_breakers')
              STORE_NAME              14 (_TABLE_NAME)

 58           LOAD_CONST               7 ('OK')
              STORE_NAME              15 (STATUS_OK)

 59           LOAD_CONST               8 ('TRIPPED')
              STORE_NAME              16 (STATUS_TRIPPED)

 60           LOAD_CONST               9 ('RESETTING')
              STORE_NAME              17 (STATUS_RESETTING)

 62           LOAD_NAME               18 (frozenset)
              PUSH_NULL
              LOAD_NAME               15 (STATUS_OK)
              LOAD_NAME               16 (STATUS_TRIPPED)
              LOAD_NAME               17 (STATUS_RESETTING)
              BUILD_SET                3
              CALL                     1
              STORE_NAME              19 (_VALID_STATUSES)

 64           LOAD_CONST              10 ('S1_INBOUND_FAILING')
              STORE_NAME              20 (REASON_S1)

 65           LOAD_CONST              11 ('S2_AUDIT_INTEGRITY_RISK')
              STORE_NAME              21 (REASON_S2)

 66           LOAD_CONST              12 ('S3_PII_OR_SECRET_EXPOSURE')
              STORE_NAME              22 (REASON_S3)

 67           LOAD_CONST              13 ('S4_OPERATOR_BLOCKING_UI')
              STORE_NAME              23 (REASON_S4)

 68           LOAD_CONST              14 ('S5_SLOW_OR_NOISY')
              STORE_NAME              24 (REASON_S5)

 69           LOAD_CONST              15 ('OPERATOR_REQUESTED')
              STORE_NAME              25 (REASON_OPERATOR)

 70           LOAD_CONST              16 ('ROLLBACK_INITIATED')
              STORE_NAME              26 (REASON_ROLLBACK)

 72           LOAD_NAME               18 (frozenset)
              PUSH_NULL

 73           LOAD_NAME               20 (REASON_S1)
              LOAD_NAME               21 (REASON_S2)
              LOAD_NAME               22 (REASON_S3)
              LOAD_NAME               23 (REASON_S4)
              LOAD_NAME               24 (REASON_S5)

 74           LOAD_NAME               25 (REASON_OPERATOR)
              LOAD_NAME               26 (REASON_ROLLBACK)

 72           BUILD_SET                7
              CALL                     1
              STORE_NAME              27 (_VALID_REASONS)

 77           LOAD_SMALL_INT         200
              STORE_NAME              28 (_BROKERAGE_ID_MAX_LEN)

 78           LOAD_SMALL_INT         200
              STORE_NAME              29 (_ACTOR_ID_MAX_LEN)

 79           LOAD_CONST              17 (2048)
              STORE_NAME              30 (_RATIONALE_MAX_LEN)

 81           LOAD_CONST              52 (('breaker_id', 'brokerage_id', 'status', 'reason_code', 'tripped_at', 'tripped_by_actor_type', 'tripped_by_actor_id', 'reset_at', 'reset_by_actor_type', 'reset_by_actor_id', 'updated_at'))
              STORE_NAME              31 (_ROW_ALLOWLIST)

 95           LOAD_CONST              53 (('phone', 'email', 'name_token', 'transcript', 'raw_payload', 'raw_email', 'raw_body', 'secret', 'signature', 'dedupe_key', 'api_key', 'token', 'stack_trace', 'prompt_text', 'env_values'))
              STORE_NAME              32 (_FORBIDDEN_RESPONSE_TOKENS)

107           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA2C40, file "app\services\operator\circuit_breaker.py", line 107>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _now_iso at 0x0000018C18038F30, file "app\services\operator\circuit_breaker.py", line 107>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_now_iso)

111           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\operator\circuit_breaker.py", line 111>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _safe_str at 0x0000018C17972550, file "app\services\operator\circuit_breaker.py", line 111>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              34 (_safe_str)

120           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA32D0, file "app\services\operator\circuit_breaker.py", line 120>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object _safe_brokerage at 0x0000018C18024E30, file "app\services\operator\circuit_breaker.py", line 120>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              35 (_safe_brokerage)

124           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\operator\circuit_breaker.py", line 124>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object _safe_actor_id at 0x0000018C18024B30, file "app\services\operator\circuit_breaker.py", line 124>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              36 (_safe_actor_id)

128           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA2100, file "app\services\operator\circuit_breaker.py", line 128>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object _safe_actor_type at 0x0000018C18038CB0, file "app\services\operator\circuit_breaker.py", line 128>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              37 (_safe_actor_type)

138           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA2970, file "app\services\operator\circuit_breaker.py", line 138>)
              MAKE_FUNCTION
              LOAD_CONST              30 (<code object _safe_reason at 0x0000018C18038B70, file "app\services\operator\circuit_breaker.py", line 138>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              38 (_safe_reason)

148           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA23D0, file "app\services\operator\circuit_breaker.py", line 148>)
              MAKE_FUNCTION
              LOAD_CONST              32 (<code object _safe_rationale at 0x0000018C17FF13B0, file "app\services\operator\circuit_breaker.py", line 148>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              39 (_safe_rationale)

161           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\operator\circuit_breaker.py", line 161>)
              MAKE_FUNCTION
              LOAD_CONST              34 (<code object _scan_for_forbidden at 0x0000018C18025D30, file "app\services\operator\circuit_breaker.py", line 161>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              40 (_scan_for_forbidden)

185           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C18025E30, file "app\services\operator\circuit_breaker.py", line 185>)
              MAKE_FUNCTION
              LOAD_CONST              36 (<code object _final at 0x0000018C17FE17D0, file "app\services\operator\circuit_breaker.py", line 185>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              41 (_final)

201           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C17FA2E20, file "app\services\operator\circuit_breaker.py", line 201>)
              MAKE_FUNCTION
              LOAD_CONST              38 (<code object _project_row at 0x0000018C18053CF0, file "app\services\operator\circuit_breaker.py", line 201>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              42 (_project_row)

209           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\operator\circuit_breaker.py", line 209>)
              MAKE_FUNCTION
              LOAD_CONST              40 (<code object _emit_event at 0x0000018C18038670, file "app\services\operator\circuit_breaker.py", line 209>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              43 (_emit_event)

220           LOAD_CONST              41 (<code object _get_db at 0x0000018C180533F0, file "app\services\operator\circuit_breaker.py", line 220>)
              MAKE_FUNCTION
              STORE_NAME              44 (_get_db)

232           LOAD_CONST              42 ('rationale')

238           LOAD_CONST               2 (None)

232           BUILD_MAP                1
              LOAD_CONST              43 (<code object __annotate__ at 0x0000018C18024930, file "app\services\operator\circuit_breaker.py", line 232>)
              MAKE_FUNCTION
              LOAD_CONST              44 (<code object trip_breaker at 0x0000018C17D8BF50, file "app\services\operator\circuit_breaker.py", line 232>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              45 (trip_breaker)

326           LOAD_CONST              42 ('rationale')

331           LOAD_CONST               2 (None)

326           BUILD_MAP                1
              LOAD_CONST              45 (<code object __annotate__ at 0x0000018C18025730, file "app\services\operator\circuit_breaker.py", line 326>)
              MAKE_FUNCTION
              LOAD_CONST              46 (<code object reset_breaker at 0x0000018C177ACF10, file "app\services\operator\circuit_breaker.py", line 326>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              46 (reset_breaker)

412           LOAD_CONST              47 (<code object __annotate__ at 0x0000018C17FA3B40, file "app\services\operator\circuit_breaker.py", line 412>)
              MAKE_FUNCTION
              LOAD_CONST              48 (<code object current_breaker_state at 0x0000018C17E94C50, file "app\services\operator\circuit_breaker.py", line 412>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              47 (current_breaker_state)

498           LOAD_CONST              18 ('status')
              LOAD_CONST               2 (None)
              LOAD_CONST              49 ('limit')
              LOAD_SMALL_INT         100
              BUILD_MAP                2
              LOAD_CONST              50 (<code object __annotate__ at 0x0000018C18025F30, file "app\services\operator\circuit_breaker.py", line 498>)
              MAKE_FUNCTION
              LOAD_CONST              51 (<code object list_breakers at 0x0000018C17D512D0, file "app\services\operator\circuit_breaker.py", line 498>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              48 (list_breakers)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app\services\operator\circuit_breaker.py", line 107>:
107           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038F30, file "app\services\operator\circuit_breaker.py", line 107>:
107           RESUME                   0

108           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\operator\circuit_breaker.py", line 111>:
111           RESUME                   0
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

Disassembly of <code object _safe_str at 0x0000018C17972550, file "app\services\operator\circuit_breaker.py", line 111>:
111           RESUME                   0

112           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

113           LOAD_CONST               0 (None)
              RETURN_VALUE

114   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (s)

115           LOAD_FAST_BORROW         2 (s)
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

116   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

117   L3:     LOAD_FAST_BORROW         2 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "app\services\operator\circuit_breaker.py", line 120>:
120           RESUME                   0
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

Disassembly of <code object _safe_brokerage at 0x0000018C18024E30, file "app\services\operator\circuit_breaker.py", line 120>:
120           RESUME                   0

121           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (_BROKERAGE_ID_MAX_LEN)
              CALL                     2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\operator\circuit_breaker.py", line 124>:
124           RESUME                   0
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

Disassembly of <code object _safe_actor_id at 0x0000018C18024B30, file "app\services\operator\circuit_breaker.py", line 124>:
124           RESUME                   0

125           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (_ACTOR_ID_MAX_LEN)
              CALL                     2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app\services\operator\circuit_breaker.py", line 128>:
128           RESUME                   0
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

Disassembly of <code object _safe_actor_type at 0x0000018C18038CB0, file "app\services\operator\circuit_breaker.py", line 128>:
128           RESUME                   0

129           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_SMALL_INT          32
              CALL                     2
              STORE_FAST               1 (s)

130           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

131           LOAD_CONST               1 (None)
              RETURN_VALUE

132   L1:     LOAD_FAST_BORROW         1 (s)
              LOAD_ATTR                3 (upper + NULL|self)
              CALL                     0
              STORE_FAST               2 (up)

133           LOAD_FAST_BORROW         2 (up)
              LOAD_CONST               2 (('ADMIN', 'OPERATOR'))
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

134           LOAD_CONST               1 (None)
              RETURN_VALUE

135   L2:     LOAD_FAST_BORROW         2 (up)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app\services\operator\circuit_breaker.py", line 138>:
138           RESUME                   0
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

Disassembly of <code object _safe_reason at 0x0000018C18038B70, file "app\services\operator\circuit_breaker.py", line 138>:
138           RESUME                   0

139           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_SMALL_INT          64
              CALL                     2
              STORE_FAST               1 (s)

140           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

141           LOAD_CONST               1 (None)
              RETURN_VALUE

142   L1:     LOAD_FAST_BORROW         1 (s)
              LOAD_ATTR                3 (upper + NULL|self)
              CALL                     0
              STORE_FAST               2 (up)

143           LOAD_FAST_BORROW         2 (up)
              LOAD_GLOBAL              4 (_VALID_REASONS)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

144           LOAD_CONST               1 (None)
              RETURN_VALUE

145   L2:     LOAD_FAST_BORROW         2 (up)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app\services\operator\circuit_breaker.py", line 148>:
148           RESUME                   0
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

Disassembly of <code object _safe_rationale at 0x0000018C17FF13B0, file "app\services\operator\circuit_breaker.py", line 148>:
148           RESUME                   0

149           LOAD_FAST_BORROW         0 (value)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

150           LOAD_CONST               0 (None)
              RETURN_VALUE

151   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

152           LOAD_CONST               0 (None)
              RETURN_VALUE

153   L2:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

154           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

155           LOAD_CONST               0 (None)
              RETURN_VALUE

156   L3:     LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_RATIONALE_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       10 (to L4)
              NOT_TAKEN

157           LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               0 (None)
              LOAD_GLOBAL              8 (_RATIONALE_MAX_LEN)
              BINARY_SLICE
              STORE_FAST               1 (s)

158   L4:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\operator\circuit_breaker.py", line 161>:
161           RESUME                   0
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

Disassembly of <code object _scan_for_forbidden at 0x0000018C18025D30, file "app\services\operator\circuit_breaker.py", line 161>:
  --           MAKE_CELL                1 (walk)

 161           RESUME                   0

 162           LOAD_CONST               0 (<code object __annotate__ at 0x0000018C17FA2D30, file "app\services\operator\circuit_breaker.py", line 162>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object walk at 0x0000018C17CC2460, file "app\services\operator\circuit_breaker.py", line 162>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

 182           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app\services\operator\circuit_breaker.py", line 162>:
162           RESUME                   0
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

Disassembly of <code object walk at 0x0000018C17CC2460, file "app\services\operator\circuit_breaker.py", line 162>:
  --            COPY_FREE_VARS           1

 162            RESUME                   0

 163            NOP

 164    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      111 (to L16)
        L2:     NOT_TAKEN

 165    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                88 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

 166            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L10)
                NOT_TAKEN

 167            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

 168            LOAD_GLOBAL             10 (_FORBIDDEN_RESPONSE_TOKENS)
                GET_ITER
        L5:     FOR_ITER                15 (to L9)
                STORE_FAST               4 (tok)

 169            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)

 170    L7:     LOAD_FAST_BORROW         4 (tok)
                SWAP                     2
                POP_TOP
                SWAP                     2
                POP_TOP
        L8:     RETURN_VALUE

 168    L9:     END_FOR
                POP_ITER

 171   L10:     LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 172            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           86 (to L4)

 173   L12:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L13:     RETURN_VALUE

 165   L14:     END_FOR
                POP_ITER

 181   L15:     LOAD_CONST               0 (None)
                RETURN_VALUE

 174   L16:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             12 (list)
                LOAD_GLOBAL             14 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L22)
                NOT_TAKEN

 175            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L17:     FOR_ITER                23 (to L21)
                STORE_FAST               2 (v)

 176            LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 177            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           21 (to L17)

 178   L19:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L20:     RETURN_VALUE

 175   L21:     END_FOR
                POP_ITER

 181   L22:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 179            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L25)
                NOT_TAKEN
                POP_TOP

 180   L24:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 179   L25:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app\services\operator\circuit_breaker.py", line 185>:
185           RESUME                   0
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

Disassembly of <code object _final at 0x0000018C17FE17D0, file "app\services\operator\circuit_breaker.py", line 185>:
185           RESUME                   0

186           LOAD_GLOBAL              1 (_scan_for_forbidden + NULL)
              LOAD_FAST_BORROW         0 (env)
              CALL                     1
              STORE_FAST               2 (leak)

187           LOAD_FAST_BORROW         2 (leak)
              TO_BOOL
              POP_JUMP_IF_FALSE       37 (to L1)
              NOT_TAKEN

188           LOAD_GLOBAL              2 (logger)
              LOAD_ATTR                5 (warning + NULL|self)

189           LOAD_CONST               0 ('circuit_breaker surface=')
              LOAD_FAST_BORROW         1 (surface)
              FORMAT_SIMPLE
              LOAD_CONST               1 (' collapsed — forbidden token leaked')
              BUILD_STRING             3

188           CALL                     1
              POP_TOP

193           LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('failed')

194           LOAD_CONST               4 ('surface')
              LOAD_FAST_BORROW         1 (surface)

195           LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('breaker_envelope_forbidden_token')

196           LOAD_CONST               7 ('warnings')
              LOAD_CONST               6 ('breaker_envelope_forbidden_token')
              BUILD_LIST               1

192           BUILD_MAP                4
              RETURN_VALUE

198   L1:     LOAD_FAST_BORROW         0 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app\services\operator\circuit_breaker.py", line 201>:
201           RESUME                   0
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

Disassembly of <code object _project_row at 0x0000018C18053CF0, file "app\services\operator\circuit_breaker.py", line 201>:
201           RESUME                   0

202           BUILD_MAP                0
              STORE_FAST               1 (out)

203           LOAD_GLOBAL              0 (_ROW_ALLOWLIST)
              GET_ITER
      L1:     FOR_ITER                21 (to L3)
              STORE_FAST               2 (k)

204           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L1)

205   L2:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, k)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, k)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L1)

203   L3:     END_FOR
              POP_ITER

206           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\operator\circuit_breaker.py", line 209>:
209           RESUME                   0
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

Disassembly of <code object _emit_event at 0x0000018C18038670, file "app\services\operator\circuit_breaker.py", line 209>:
 209            RESUME                   0

 210            NOP

 211    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('log_event_bg',))
                IMPORT_NAME              0 (app.db.event_logger)
                IMPORT_FROM              1 (log_event_bg)
                STORE_FAST               2 (log_event_bg)
                POP_TOP

 214    L2:     NOP

 215    L3:     LOAD_FAST                2 (log_event_bg)
                PUSH_NULL
                LOAD_FAST_LOAD_FAST      1 (event_type, payload)
                CALL                     2
                POP_TOP
        L4:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 212            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L7)
                NOT_TAKEN
                POP_TOP

 213    L6:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 212    L7:     RERAISE                  0

  --    L8:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
        L9:     PUSH_EXC_INFO

 216            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L11)
                NOT_TAKEN
                POP_TOP

 217   L10:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 216   L11:     RERAISE                  0

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

Disassembly of <code object _get_db at 0x0000018C180533F0, file "app\services\operator\circuit_breaker.py", line 220>:
 220           RESUME                   0

 221           NOP

 222   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 223           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 224           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 225   L4:     POP_EXCEPT
               LOAD_CONST               2 (None)
               RETURN_VALUE

 224   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app\services\operator\circuit_breaker.py", line 232>:
232           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

234           LOAD_CONST               2 ('Any')

232           LOAD_CONST               3 ('reason_code')

235           LOAD_CONST               2 ('Any')

232           LOAD_CONST               4 ('actor_type')

236           LOAD_CONST               2 ('Any')

232           LOAD_CONST               5 ('actor_id')

237           LOAD_CONST               2 ('Any')

232           LOAD_CONST               6 ('rationale')

238           LOAD_CONST               2 ('Any')

232           LOAD_CONST               7 ('return')

239           LOAD_CONST               8 ('Dict[str, Any]')

232           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object trip_breaker at 0x0000018C17D8BF50, file "app\services\operator\circuit_breaker.py", line 232>:
 232            RESUME                   0

 243            LOAD_CONST               1 ('ops.circuit_breaker.trip')
                STORE_FAST               5 (surface)

 244            NOP

 245    L1:     LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               6 (bid)

 246            LOAD_GLOBAL              3 (_safe_reason + NULL)
                LOAD_FAST_BORROW         1 (reason_code)
                CALL                     1
                STORE_FAST               7 (reason)

 247            LOAD_GLOBAL              5 (_safe_actor_type + NULL)
                LOAD_FAST_BORROW         2 (actor_type)
                CALL                     1
                STORE_FAST               8 (atype)

 248            LOAD_GLOBAL              7 (_safe_actor_id + NULL)
                LOAD_FAST_BORROW         3 (actor_id)
                CALL                     1
                STORE_FAST               9 (aid)

 249            LOAD_GLOBAL              9 (_safe_rationale + NULL)
                LOAD_FAST_BORROW         4 (rationale)
                CALL                     1
                STORE_FAST              10 (rat)

 250            LOAD_FAST_BORROW         6 (bid)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L3)
                NOT_TAKEN

 251            LOAD_GLOBAL             11 (_final + NULL)

 252            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 253            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         5 (surface)

 254            LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('invalid_brokerage_id')

 255            LOAD_CONST               7 ('warnings')
                LOAD_CONST               6 ('invalid_brokerage_id')
                BUILD_LIST               1

 251            BUILD_MAP                4

 256            LOAD_FAST_BORROW         5 (surface)

 251            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L2:     RETURN_VALUE

 257    L3:     LOAD_FAST_BORROW         7 (reason)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L7)
        L4:     NOT_TAKEN

 258    L5:     LOAD_GLOBAL             11 (_final + NULL)

 259            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 260            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         5 (surface)

 261            LOAD_CONST               5 ('error_code')
                LOAD_CONST               9 ('invalid_reason_code')

 262            LOAD_CONST               7 ('warnings')
                LOAD_CONST               9 ('invalid_reason_code')
                BUILD_LIST               1

 258            BUILD_MAP                4

 263            LOAD_FAST_BORROW         5 (surface)

 258            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L6:     RETURN_VALUE

 264    L7:     LOAD_FAST_BORROW         8 (atype)
                TO_BOOL
                POP_JUMP_IF_FALSE        9 (to L11)
        L8:     NOT_TAKEN
        L9:     LOAD_FAST_BORROW         9 (aid)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L13)
       L10:     NOT_TAKEN

 265   L11:     LOAD_GLOBAL             11 (_final + NULL)

 266            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 267            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         5 (surface)

 268            LOAD_CONST               5 ('error_code')
                LOAD_CONST              10 ('invalid_actor')

 269            LOAD_CONST               7 ('warnings')
                LOAD_CONST              10 ('invalid_actor')
                BUILD_LIST               1

 265            BUILD_MAP                4

 270            LOAD_FAST_BORROW         5 (surface)

 265            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L12:     RETURN_VALUE

 271   L13:     LOAD_GLOBAL             13 (_now_iso + NULL)
                CALL                     0
                STORE_FAST              11 (now)

 273            LOAD_CONST              11 ('breaker_id')
                LOAD_GLOBAL             15 (str + NULL)
                LOAD_GLOBAL             16 (uuid)
                LOAD_ATTR               18 (uuid4)
                PUSH_NULL
                CALL                     0
                CALL                     1

 274            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST_BORROW         6 (bid)

 275            LOAD_CONST               2 ('status')
                LOAD_GLOBAL             20 (STATUS_TRIPPED)

 276            LOAD_CONST              13 ('reason_code')
                LOAD_FAST_BORROW         7 (reason)

 277            LOAD_CONST              14 ('tripped_at')
                LOAD_FAST_BORROW        11 (now)

 278            LOAD_CONST              15 ('tripped_by_actor_type')
                LOAD_FAST_BORROW         8 (atype)

 279            LOAD_CONST              16 ('tripped_by_actor_id')
                LOAD_FAST_BORROW         9 (aid)

 280            LOAD_CONST              17 ('updated_at')
                LOAD_FAST_BORROW        11 (now)

 272            BUILD_MAP                8
                STORE_FAST              12 (row)

 282            LOAD_FAST_BORROW        10 (rat)
                TO_BOOL
                POP_JUMP_IF_FALSE        5 (to L14)
                NOT_TAKEN
                LOAD_CONST              18 ('rationale_text')
                LOAD_FAST_BORROW        10 (rat)
                BUILD_MAP                1
                JUMP_FORWARD             1 (to L15)
       L14:     BUILD_MAP                0
       L15:     STORE_FAST              13 (meta)

 283            LOAD_GLOBAL             23 (_get_db + NULL)
                CALL                     0
                STORE_FAST              14 (db)

 284            BUILD_LIST               0
                STORE_FAST              15 (warnings)

 285            LOAD_FAST_BORROW        14 (db)
                POP_JUMP_IF_NOT_NONE    21 (to L16)
                NOT_TAKEN

 286            LOAD_FAST_BORROW        15 (warnings)
                LOAD_ATTR               25 (append + NULL|self)
                LOAD_CONST              20 ('db_unavailable')
                CALL                     1
                POP_TOP

 287            LOAD_CONST              21 ('skipped')
                STORE_FAST              16 (db_status)
                JUMP_FORWARD            59 (to L18)

 289   L16:     NOP

 290   L17:     LOAD_FAST_BORROW        14 (db)
                LOAD_ATTR               27 (table + NULL|self)
                LOAD_GLOBAL             28 (_TABLE_NAME)
                CALL                     1
                LOAD_ATTR               31 (insert + NULL|self)
                BUILD_MAP                0
                LOAD_FAST_BORROW        12 (row)
                DICT_UPDATE              1
                LOAD_CONST              22 ('metadata')
                LOAD_FAST_BORROW        13 (meta)
                BUILD_MAP                1
                DICT_UPDATE              1
                CALL                     1
                LOAD_ATTR               33 (execute + NULL|self)
                CALL                     0
                POP_TOP

 291            LOAD_CONST              23 ('ok')
                STORE_FAST              16 (db_status)

 299   L18:     LOAD_GLOBAL             45 (_emit_event + NULL)
                LOAD_CONST              26 ('circuit_breaker.tripped')

 300            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST_BORROW         6 (bid)

 301            LOAD_CONST              11 ('breaker_id')
                LOAD_FAST_BORROW        12 (row)
                LOAD_CONST              11 ('breaker_id')
                BINARY_OP               26 ([])

 302            LOAD_CONST              13 ('reason_code')
                LOAD_FAST_BORROW         7 (reason)

 303            LOAD_CONST              27 ('actor_type')
                LOAD_FAST_BORROW         8 (atype)

 304            LOAD_CONST              28 ('actor_id')
                LOAD_FAST_BORROW         9 (aid)

 305            LOAD_CONST               2 ('status')
                LOAD_GLOBAL             20 (STATUS_TRIPPED)

 299            BUILD_MAP                6
                CALL                     2
                POP_TOP

 307            LOAD_GLOBAL             11 (_final + NULL)

 308            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW        16 (db_status)
                LOAD_CONST              23 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L19)
                NOT_TAKEN
                LOAD_CONST              23 ('ok')
                JUMP_FORWARD             1 (to L20)
       L19:     LOAD_CONST              21 ('skipped')

 309   L20:     LOAD_CONST               4 ('surface')
                LOAD_FAST                5 (surface)

 310            LOAD_CONST              29 ('row')
                LOAD_GLOBAL             47 (_project_row + NULL)
                LOAD_FAST_BORROW        12 (row)
                CALL                     1

 311            LOAD_CONST               7 ('warnings')
                LOAD_FAST               15 (warnings)

 312            LOAD_CONST               5 ('error_code')
                LOAD_FAST_BORROW        16 (db_status)
                LOAD_CONST              23 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L21)
                NOT_TAKEN
                LOAD_CONST              19 (None)
                JUMP_FORWARD             1 (to L22)
       L21:     LOAD_CONST              20 ('db_unavailable')

 307   L22:     BUILD_MAP                5

 313            LOAD_FAST_BORROW         5 (surface)

 307            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L23:     RETURN_VALUE

  --   L24:     PUSH_EXC_INFO

 292            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       95 (to L28)
                NOT_TAKEN
                STORE_FAST              17 (e)

 293   L25:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 294            LOAD_CONST              24 ('circuit_breaker trip insert error type=')

 295            LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               17 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE

 294            BUILD_STRING             2

 293            CALL                     1
                POP_TOP

 297            LOAD_FAST               15 (warnings)
                LOAD_ATTR               25 (append + NULL|self)
                LOAD_CONST              25 ('db_insert_failed:')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               17 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 298            LOAD_CONST              21 ('skipped')
                STORE_FAST              16 (db_status)
       L26:     POP_EXCEPT
                LOAD_CONST              19 (None)
                STORE_FAST              17 (e)
                DELETE_FAST             17 (e)
                JUMP_BACKWARD_NO_INTERRUPT 185 (to L18)

  --   L27:     LOAD_CONST              19 (None)
                STORE_FAST              17 (e)
                DELETE_FAST             17 (e)
                RERAISE                  1

 292   L28:     RERAISE                  0

  --   L29:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L30:     PUSH_EXC_INFO

 314            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L35)
                NOT_TAKEN
                STORE_FAST              17 (e)

 315   L31:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 316            LOAD_CONST              30 ('trip_breaker error type=')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               17 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 315            CALL                     1
                POP_TOP

 318            LOAD_GLOBAL             11 (_final + NULL)

 319            LOAD_CONST               2 ('status')
                LOAD_CONST              21 ('skipped')

 320            LOAD_CONST               4 ('surface')
                LOAD_FAST                5 (surface)

 321            LOAD_CONST               5 ('error_code')
                LOAD_CONST              31 ('unexpected:')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               17 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 322            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 318            BUILD_MAP                4

 323            LOAD_FAST                5 (surface)

 318            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L32:     SWAP                     2
       L33:     POP_EXCEPT
                LOAD_CONST              19 (None)
                STORE_FAST              17 (e)
                DELETE_FAST             17 (e)
                RETURN_VALUE

  --   L34:     LOAD_CONST              19 (None)
                STORE_FAST              17 (e)
                DELETE_FAST             17 (e)
                RERAISE                  1

 314   L35:     RERAISE                  0

  --   L36:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L30 [0]
  L3 to L4 -> L30 [0]
  L5 to L6 -> L30 [0]
  L7 to L8 -> L30 [0]
  L9 to L10 -> L30 [0]
  L11 to L12 -> L30 [0]
  L13 to L16 -> L30 [0]
  L17 to L18 -> L24 [0]
  L18 to L23 -> L30 [0]
  L24 to L25 -> L29 [1] lasti
  L25 to L26 -> L27 [1] lasti
  L26 to L27 -> L30 [0]
  L27 to L29 -> L29 [1] lasti
  L29 to L30 -> L30 [0]
  L30 to L31 -> L36 [1] lasti
  L31 to L32 -> L34 [1] lasti
  L32 to L33 -> L36 [1] lasti
  L34 to L36 -> L36 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app\services\operator\circuit_breaker.py", line 326>:
326           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

328           LOAD_CONST               2 ('Any')

326           LOAD_CONST               3 ('actor_type')

329           LOAD_CONST               2 ('Any')

326           LOAD_CONST               4 ('actor_id')

330           LOAD_CONST               2 ('Any')

326           LOAD_CONST               5 ('rationale')

331           LOAD_CONST               2 ('Any')

326           LOAD_CONST               6 ('return')

332           LOAD_CONST               7 ('Dict[str, Any]')

326           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object reset_breaker at 0x0000018C177ACF10, file "app\services\operator\circuit_breaker.py", line 326>:
 326            RESUME                   0

 337            LOAD_CONST               1 ('ops.circuit_breaker.reset')
                STORE_FAST               4 (surface)

 338            NOP

 339    L1:     LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               5 (bid)

 340            LOAD_GLOBAL              3 (_safe_actor_type + NULL)
                LOAD_FAST_BORROW         1 (actor_type)
                CALL                     1
                STORE_FAST               6 (atype)

 341            LOAD_GLOBAL              5 (_safe_actor_id + NULL)
                LOAD_FAST_BORROW         2 (actor_id)
                CALL                     1
                STORE_FAST               7 (aid)

 342            LOAD_GLOBAL              7 (_safe_rationale + NULL)
                LOAD_FAST_BORROW         3 (rationale)
                CALL                     1
                STORE_FAST               8 (rat)

 343            LOAD_FAST_BORROW         5 (bid)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L3)
                NOT_TAKEN

 344            LOAD_GLOBAL              9 (_final + NULL)

 345            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 346            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         4 (surface)

 347            LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('invalid_brokerage_id')

 348            LOAD_CONST               7 ('warnings')
                LOAD_CONST               6 ('invalid_brokerage_id')
                BUILD_LIST               1

 344            BUILD_MAP                4

 349            LOAD_FAST_BORROW         4 (surface)

 344            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L2:     RETURN_VALUE

 350    L3:     LOAD_FAST_BORROW         6 (atype)
                TO_BOOL
                POP_JUMP_IF_FALSE        9 (to L7)
        L4:     NOT_TAKEN
        L5:     LOAD_FAST_BORROW         7 (aid)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L9)
        L6:     NOT_TAKEN

 351    L7:     LOAD_GLOBAL              9 (_final + NULL)

 352            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 353            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         4 (surface)

 354            LOAD_CONST               5 ('error_code')
                LOAD_CONST               9 ('invalid_actor')

 355            LOAD_CONST               7 ('warnings')
                LOAD_CONST               9 ('invalid_actor')
                BUILD_LIST               1

 351            BUILD_MAP                4

 356            LOAD_FAST_BORROW         4 (surface)

 351            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L8:     RETURN_VALUE

 357    L9:     LOAD_GLOBAL             11 (_now_iso + NULL)
                CALL                     0
                STORE_FAST               9 (now)

 359            LOAD_CONST              10 ('breaker_id')
                LOAD_GLOBAL             13 (str + NULL)
                LOAD_GLOBAL             14 (uuid)
                LOAD_ATTR               16 (uuid4)
                PUSH_NULL
                CALL                     0
                CALL                     1

 360            LOAD_CONST              11 ('brokerage_id')
                LOAD_FAST_BORROW         5 (bid)

 361            LOAD_CONST               2 ('status')
                LOAD_GLOBAL             18 (STATUS_OK)

 362            LOAD_CONST              12 ('reason_code')
                LOAD_CONST              13 (None)

 363            LOAD_CONST              14 ('reset_at')
                LOAD_FAST_BORROW         9 (now)

 364            LOAD_CONST              15 ('reset_by_actor_type')
                LOAD_FAST_BORROW         6 (atype)

 365            LOAD_CONST              16 ('reset_by_actor_id')
                LOAD_FAST_BORROW         7 (aid)

 366            LOAD_CONST              17 ('updated_at')
                LOAD_FAST_BORROW         9 (now)

 358            BUILD_MAP                8
                STORE_FAST              10 (row)

 368            LOAD_FAST_BORROW         8 (rat)
                TO_BOOL
                POP_JUMP_IF_FALSE        5 (to L10)
                NOT_TAKEN
                LOAD_CONST              18 ('rationale_text')
                LOAD_FAST_BORROW         8 (rat)
                BUILD_MAP                1
                JUMP_FORWARD             1 (to L11)
       L10:     BUILD_MAP                0
       L11:     STORE_FAST              11 (meta)

 369            LOAD_GLOBAL             21 (_get_db + NULL)
                CALL                     0
                STORE_FAST              12 (db)

 370            BUILD_LIST               0
                STORE_FAST              13 (warnings)

 371            LOAD_FAST_BORROW        12 (db)
                POP_JUMP_IF_NOT_NONE    21 (to L12)
                NOT_TAKEN

 372            LOAD_FAST_BORROW        13 (warnings)
                LOAD_ATTR               23 (append + NULL|self)
                LOAD_CONST              19 ('db_unavailable')
                CALL                     1
                POP_TOP

 373            LOAD_CONST              20 ('skipped')
                STORE_FAST              14 (db_status)
                JUMP_FORWARD            59 (to L14)

 375   L12:     NOP

 376   L13:     LOAD_FAST_BORROW        12 (db)
                LOAD_ATTR               25 (table + NULL|self)
                LOAD_GLOBAL             26 (_TABLE_NAME)
                CALL                     1
                LOAD_ATTR               29 (insert + NULL|self)
                BUILD_MAP                0
                LOAD_FAST_BORROW        10 (row)
                DICT_UPDATE              1
                LOAD_CONST              21 ('metadata')
                LOAD_FAST_BORROW        11 (meta)
                BUILD_MAP                1
                DICT_UPDATE              1
                CALL                     1
                LOAD_ATTR               31 (execute + NULL|self)
                CALL                     0
                POP_TOP

 377            LOAD_CONST              22 ('ok')
                STORE_FAST              14 (db_status)

 385   L14:     LOAD_GLOBAL             43 (_emit_event + NULL)
                LOAD_CONST              25 ('circuit_breaker.reset')

 386            LOAD_CONST              11 ('brokerage_id')
                LOAD_FAST_BORROW         5 (bid)

 387            LOAD_CONST              10 ('breaker_id')
                LOAD_FAST_BORROW        10 (row)
                LOAD_CONST              10 ('breaker_id')
                BINARY_OP               26 ([])

 388            LOAD_CONST              26 ('actor_type')
                LOAD_FAST_BORROW         6 (atype)

 389            LOAD_CONST              27 ('actor_id')
                LOAD_FAST_BORROW         7 (aid)

 390            LOAD_CONST               2 ('status')
                LOAD_GLOBAL             18 (STATUS_OK)

 385            BUILD_MAP                5
                CALL                     2
                POP_TOP

 392            LOAD_GLOBAL              9 (_final + NULL)

 393            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW        14 (db_status)
                LOAD_CONST              22 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN
                LOAD_CONST              22 ('ok')
                JUMP_FORWARD             1 (to L16)
       L15:     LOAD_CONST              20 ('skipped')

 394   L16:     LOAD_CONST               4 ('surface')
                LOAD_FAST                4 (surface)

 395            LOAD_CONST              28 ('row')
                LOAD_GLOBAL             45 (_project_row + NULL)
                LOAD_FAST_BORROW        10 (row)
                CALL                     1

 396            LOAD_CONST               7 ('warnings')
                LOAD_FAST               13 (warnings)

 397            LOAD_CONST               5 ('error_code')
                LOAD_FAST_BORROW        14 (db_status)
                LOAD_CONST              22 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L17)
                NOT_TAKEN
                LOAD_CONST              13 (None)
                JUMP_FORWARD             1 (to L18)
       L17:     LOAD_CONST              19 ('db_unavailable')

 398   L18:     LOAD_CONST              29 ('action_required')
                LOAD_CONST              30 ('operator_must_re_enable_inbound_externally')

 392            BUILD_MAP                6

 399            LOAD_FAST_BORROW         4 (surface)

 392            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L19:     RETURN_VALUE

  --   L20:     PUSH_EXC_INFO

 378            LOAD_GLOBAL             32 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       95 (to L24)
                NOT_TAKEN
                STORE_FAST              15 (e)

 379   L21:     LOAD_GLOBAL             34 (logger)
                LOAD_ATTR               37 (warning + NULL|self)

 380            LOAD_CONST              23 ('circuit_breaker reset insert error type=')

 381            LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)
                FORMAT_SIMPLE

 380            BUILD_STRING             2

 379            CALL                     1
                POP_TOP

 383            LOAD_FAST               13 (warnings)
                LOAD_ATTR               23 (append + NULL|self)
                LOAD_CONST              24 ('db_insert_failed:')
                LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 384            LOAD_CONST              20 ('skipped')
                STORE_FAST              14 (db_status)
       L22:     POP_EXCEPT
                LOAD_CONST              13 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                JUMP_BACKWARD_NO_INTERRUPT 185 (to L14)

  --   L23:     LOAD_CONST              13 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RERAISE                  1

 378   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L26:     PUSH_EXC_INFO

 400            LOAD_GLOBAL             32 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L31)
                NOT_TAKEN
                STORE_FAST              15 (e)

 401   L27:     LOAD_GLOBAL             34 (logger)
                LOAD_ATTR               37 (warning + NULL|self)

 402            LOAD_CONST              31 ('reset_breaker error type=')
                LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 401            CALL                     1
                POP_TOP

 404            LOAD_GLOBAL              9 (_final + NULL)

 405            LOAD_CONST               2 ('status')
                LOAD_CONST              20 ('skipped')

 406            LOAD_CONST               4 ('surface')
                LOAD_FAST                4 (surface)

 407            LOAD_CONST               5 ('error_code')
                LOAD_CONST              32 ('unexpected:')
                LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 408            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 404            BUILD_MAP                4

 409            LOAD_FAST                4 (surface)

 404            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L28:     SWAP                     2
       L29:     POP_EXCEPT
                LOAD_CONST              13 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RETURN_VALUE

  --   L30:     LOAD_CONST              13 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RERAISE                  1

 400   L31:     RERAISE                  0

  --   L32:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L26 [0]
  L3 to L4 -> L26 [0]
  L5 to L6 -> L26 [0]
  L7 to L8 -> L26 [0]
  L9 to L12 -> L26 [0]
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app\services\operator\circuit_breaker.py", line 412>:
412           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object current_breaker_state at 0x0000018C17E94C50, file "app\services\operator\circuit_breaker.py", line 412>:
 412            RESUME                   0

 417            LOAD_CONST               1 ('ops.circuit_breaker.current')
                STORE_FAST               1 (surface)

 418            NOP

 419    L1:     LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               2 (bid)

 420            LOAD_FAST_BORROW         2 (bid)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L3)
                NOT_TAKEN

 421            LOAD_GLOBAL              3 (_final + NULL)

 422            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 423            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         1 (surface)

 424            LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('invalid_brokerage_id')

 425            LOAD_CONST               7 ('warnings')
                LOAD_CONST               6 ('invalid_brokerage_id')
                BUILD_LIST               1

 421            BUILD_MAP                4

 426            LOAD_FAST_BORROW         1 (surface)

 421            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L2:     RETURN_VALUE

 427    L3:     LOAD_GLOBAL              5 (_get_db + NULL)
                CALL                     0
                STORE_FAST               3 (db)

 428            LOAD_FAST_BORROW         3 (db)
                POP_JUMP_IF_NOT_NONE    35 (to L5)
                NOT_TAKEN

 429            LOAD_GLOBAL              3 (_final + NULL)

 430            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('skipped')

 431            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         1 (surface)

 432            LOAD_CONST              11 ('row')

 433            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)

 434            LOAD_CONST               2 ('status')
                LOAD_GLOBAL              6 (STATUS_OK)

 435            LOAD_CONST              13 ('reason_code')
                LOAD_CONST               9 (None)

 432            BUILD_MAP                3

 437            LOAD_CONST               7 ('warnings')
                LOAD_CONST              14 ('db_unavailable')
                BUILD_LIST               1

 438            LOAD_CONST               5 ('error_code')
                LOAD_CONST              14 ('db_unavailable')

 429            BUILD_MAP                5

 439            LOAD_FAST_BORROW         1 (surface)

 429            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L4:     RETURN_VALUE

 440    L5:     NOP

 442    L6:     LOAD_FAST_BORROW         3 (db)
                LOAD_ATTR                9 (table + NULL|self)
                LOAD_GLOBAL             10 (_TABLE_NAME)
                CALL                     1

 443            LOAD_ATTR               13 (select + NULL|self)
                LOAD_CONST              15 ('*')
                CALL                     1

 444            LOAD_ATTR               15 (eq + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)
                CALL                     2

 445            LOAD_ATTR               17 (order + NULL|self)
                LOAD_CONST              16 ('updated_at')
                LOAD_CONST              17 (True)
                LOAD_CONST              18 (('desc',))
                CALL_KW                  2

 446            LOAD_ATTR               19 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 447            LOAD_ATTR               21 (execute + NULL|self)
                CALL                     0

 441            STORE_FAST               4 (resp)

 465    L7:     LOAD_GLOBAL             33 (getattr + NULL)
                LOAD_FAST                4 (resp)
                LOAD_CONST              22 ('data')
                LOAD_CONST               9 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                BUILD_LIST               0
       L10:     STORE_FAST               6 (data)

 466            LOAD_FAST                6 (data)
                TO_BOOL
                POP_JUMP_IF_FALSE       69 (to L14)
       L11:     NOT_TAKEN
       L12:     LOAD_GLOBAL             35 (isinstance + NULL)
                LOAD_FAST                6 (data)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_GLOBAL             36 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       40 (to L14)
                NOT_TAKEN

 467            LOAD_GLOBAL              3 (_final + NULL)

 468            LOAD_CONST               2 ('status')
                LOAD_CONST              23 ('ok')

 469            LOAD_CONST               4 ('surface')
                LOAD_FAST                1 (surface)

 470            LOAD_CONST              11 ('row')
                LOAD_GLOBAL             39 (_project_row + NULL)
                LOAD_FAST                6 (data)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1

 471            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 472            LOAD_CONST               5 ('error_code')
                LOAD_CONST               9 (None)

 467            BUILD_MAP                5

 473            LOAD_FAST                1 (surface)

 467            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L13:     RETURN_VALUE

 475   L14:     LOAD_GLOBAL              3 (_final + NULL)

 476            LOAD_CONST               2 ('status')
                LOAD_CONST              23 ('ok')

 477            LOAD_CONST               4 ('surface')
                LOAD_FAST                1 (surface)

 478            LOAD_CONST              11 ('row')

 479            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST                2 (bid)

 480            LOAD_CONST               2 ('status')
                LOAD_GLOBAL              6 (STATUS_OK)

 481            LOAD_CONST              13 ('reason_code')
                LOAD_CONST               9 (None)

 478            BUILD_MAP                3

 483            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 484            LOAD_CONST               5 ('error_code')
                LOAD_CONST               9 (None)

 475            BUILD_MAP                5

 485            LOAD_FAST                1 (surface)

 475            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L15:     RETURN_VALUE

  --   L16:     PUSH_EXC_INFO

 449            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      110 (to L22)
                NOT_TAKEN
                STORE_FAST               5 (e)

 450   L17:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 451            LOAD_CONST              19 ('current_breaker_state query error type=')

 452            LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 451            BUILD_STRING             2

 450            CALL                     1
                POP_TOP

 454            LOAD_GLOBAL              3 (_final + NULL)

 455            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('skipped')

 456            LOAD_CONST               4 ('surface')
                LOAD_FAST                1 (surface)

 457            LOAD_CONST              11 ('row')

 458            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST                2 (bid)

 459            LOAD_CONST               2 ('status')
                LOAD_GLOBAL              6 (STATUS_OK)

 460            LOAD_CONST              13 ('reason_code')
                LOAD_CONST               9 (None)

 457            BUILD_MAP                3

 462            LOAD_CONST               7 ('warnings')
                LOAD_CONST              20 ('db_query_failed:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 463            LOAD_CONST               5 ('error_code')
                LOAD_CONST              21 ('db_query_failed')

 454            BUILD_MAP                5

 464            LOAD_FAST                1 (surface)

 454            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L18:     SWAP                     2
       L19:     POP_EXCEPT
                LOAD_CONST               9 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
       L20:     RETURN_VALUE

  --   L21:     LOAD_CONST               9 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 449   L22:     RERAISE                  0

  --   L23:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L24:     PUSH_EXC_INFO

 486            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L29)
                NOT_TAKEN
                STORE_FAST               5 (e)

 487   L25:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 488            LOAD_CONST              24 ('current_breaker_state error type=')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 487            CALL                     1
                POP_TOP

 490            LOAD_GLOBAL              3 (_final + NULL)

 491            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('skipped')

 492            LOAD_CONST               4 ('surface')
                LOAD_FAST                1 (surface)

 493            LOAD_CONST               5 ('error_code')
                LOAD_CONST              25 ('unexpected:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 494            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 490            BUILD_MAP                4

 495            LOAD_FAST                1 (surface)

 490            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L26:     SWAP                     2
       L27:     POP_EXCEPT
                LOAD_CONST               9 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RETURN_VALUE

  --   L28:     LOAD_CONST               9 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 486   L29:     RERAISE                  0

  --   L30:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L24 [0]
  L3 to L4 -> L24 [0]
  L6 to L7 -> L16 [0]
  L7 to L8 -> L24 [0]
  L9 to L11 -> L24 [0]
  L12 to L13 -> L24 [0]
  L14 to L15 -> L24 [0]
  L16 to L17 -> L23 [1] lasti
  L17 to L18 -> L21 [1] lasti
  L18 to L19 -> L23 [1] lasti
  L19 to L20 -> L24 [0]
  L21 to L23 -> L23 [1] lasti
  L23 to L24 -> L24 [0]
  L24 to L25 -> L30 [1] lasti
  L25 to L26 -> L28 [1] lasti
  L26 to L27 -> L30 [1] lasti
  L28 to L30 -> L30 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "app\services\operator\circuit_breaker.py", line 498>:
498           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('limit')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('Dict[str, Any]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object list_breakers at 0x0000018C17D512D0, file "app\services\operator\circuit_breaker.py", line 498>:
 498            RESUME                   0

 501            LOAD_CONST               1 ('ops.circuit_breaker.list')
                STORE_FAST               2 (surface)

 502            NOP

 503    L1:     LOAD_SMALL_INT         100
                STORE_FAST               3 (cap)

 504    L2:     NOP

 505    L3:     LOAD_GLOBAL              1 (int + NULL)
                LOAD_FAST_BORROW         1 (limit)
                CALL                     1
                STORE_FAST               3 (cap)

 508    L4:     LOAD_FAST_BORROW         3 (cap)
                LOAD_SMALL_INT           1
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

 509            LOAD_SMALL_INT           1
                STORE_FAST               3 (cap)

 510    L5:     LOAD_FAST_BORROW         3 (cap)
                LOAD_CONST               2 (500)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN

 511            LOAD_CONST               2 (500)
                STORE_FAST               3 (cap)

 512    L6:     LOAD_CONST               3 (None)
                STORE_FAST               4 (stat)

 513            LOAD_FAST_BORROW         0 (status)
                POP_JUMP_IF_NONE        62 (to L7)
                NOT_TAKEN

 514            LOAD_GLOBAL              7 (_safe_str + NULL)
                LOAD_FAST_BORROW         0 (status)
                LOAD_SMALL_INT          32
                CALL                     2
                STORE_FAST               5 (s)

 515            LOAD_FAST_BORROW         5 (s)
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L7)
                NOT_TAKEN
                LOAD_FAST_BORROW         5 (s)
                LOAD_ATTR                9 (upper + NULL|self)
                CALL                     0
                LOAD_GLOBAL             10 (_VALID_STATUSES)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       17 (to L7)
                NOT_TAKEN

 516            LOAD_FAST_BORROW         5 (s)
                LOAD_ATTR                9 (upper + NULL|self)
                CALL                     0
                STORE_FAST               4 (stat)

 517    L7:     LOAD_GLOBAL             13 (_get_db + NULL)
                CALL                     0
                STORE_FAST               6 (db)

 518            LOAD_FAST_BORROW         6 (db)
                POP_JUMP_IF_NOT_NONE    27 (to L9)
                NOT_TAKEN

 519            LOAD_GLOBAL             15 (_final + NULL)

 520            LOAD_CONST               4 ('status')
                LOAD_CONST               5 ('skipped')

 521            LOAD_CONST               6 ('surface')
                LOAD_FAST_BORROW         2 (surface)

 522            LOAD_CONST               7 ('rows')
                BUILD_LIST               0

 523            LOAD_CONST               8 ('count')
                LOAD_SMALL_INT           0

 524            LOAD_CONST               9 ('warnings')
                LOAD_CONST              10 ('db_unavailable')
                BUILD_LIST               1

 525            LOAD_CONST              11 ('error_code')
                LOAD_CONST              10 ('db_unavailable')

 519            BUILD_MAP                6

 526            LOAD_FAST_BORROW         2 (surface)

 519            LOAD_CONST              12 (('surface',))
                CALL_KW                  2
        L8:     RETURN_VALUE

 527    L9:     NOP

 528   L10:     LOAD_FAST_BORROW         6 (db)
                LOAD_ATTR               17 (table + NULL|self)
                LOAD_GLOBAL             18 (_TABLE_NAME)
                CALL                     1
                LOAD_ATTR               21 (select + NULL|self)
                LOAD_CONST              13 ('*')
                CALL                     1
                STORE_FAST               7 (q)

 529            LOAD_FAST_BORROW         4 (stat)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L13)
       L11:     NOT_TAKEN

 530   L12:     LOAD_FAST_BORROW         7 (q)
                LOAD_ATTR               23 (eq + NULL|self)
                LOAD_CONST               4 ('status')
                LOAD_FAST_BORROW         4 (stat)
                CALL                     2
                STORE_FAST               7 (q)

 531   L13:     LOAD_FAST_BORROW         7 (q)
                LOAD_ATTR               25 (order + NULL|self)
                LOAD_CONST              14 ('updated_at')
                LOAD_CONST              15 (True)
                LOAD_CONST              16 (('desc',))
                CALL_KW                  2
                LOAD_ATTR               27 (limit + NULL|self)
                LOAD_FAST_BORROW         3 (cap)
                CALL                     1
                STORE_FAST               7 (q)

 532            LOAD_FAST_BORROW         7 (q)
                LOAD_ATTR               29 (execute + NULL|self)
                CALL                     0
                STORE_FAST               8 (resp)

 545   L14:     LOAD_GLOBAL             41 (getattr + NULL)
                LOAD_FAST                8 (resp)
                LOAD_CONST              20 ('data')
                LOAD_CONST               3 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L17)
       L15:     NOT_TAKEN
       L16:     POP_TOP
                BUILD_LIST               0
       L17:     STORE_FAST              10 (data)

 546            BUILD_LIST               0
                STORE_FAST              11 (rows)

 547            LOAD_FAST               10 (data)
                LOAD_CONST               3 (None)
                LOAD_FAST                3 (cap)
                BINARY_SLICE
                GET_ITER
       L18:     FOR_ITER                53 (to L21)
                STORE_FAST              12 (r)

 548            LOAD_GLOBAL             43 (isinstance + NULL)
                LOAD_FAST               12 (r)
                LOAD_GLOBAL             44 (dict)
                CALL                     2
                TO_BOOL
       L19:     POP_JUMP_IF_TRUE         3 (to L20)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L18)

 549   L20:     LOAD_FAST               11 (rows)
                LOAD_ATTR               47 (append + NULL|self)
                LOAD_GLOBAL             49 (_project_row + NULL)
                LOAD_FAST               12 (r)
                CALL                     1
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           55 (to L18)

 547   L21:     END_FOR
                POP_ITER

 550            LOAD_GLOBAL             15 (_final + NULL)

 551            LOAD_CONST               4 ('status')
                LOAD_CONST              21 ('ok')

 552            LOAD_CONST               6 ('surface')
                LOAD_FAST                2 (surface)

 553            LOAD_CONST               7 ('rows')
                LOAD_FAST               11 (rows)

 554            LOAD_CONST               8 ('count')
                LOAD_GLOBAL             51 (len + NULL)
                LOAD_FAST               11 (rows)
                CALL                     1

 555            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 556            LOAD_CONST              11 ('error_code')
                LOAD_CONST               3 (None)

 550            BUILD_MAP                6

 557            LOAD_FAST                2 (surface)

 550            LOAD_CONST              12 (('surface',))
                CALL_KW                  2
       L22:     RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 506            LOAD_GLOBAL              2 (TypeError)
                LOAD_GLOBAL              4 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        7 (to L25)
                NOT_TAKEN
                POP_TOP

 507            LOAD_SMALL_INT         100
                STORE_FAST               3 (cap)
       L24:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 381 (to L4)

 506   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L27:     PUSH_EXC_INFO

 533            LOAD_GLOBAL             30 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      102 (to L33)
                NOT_TAKEN
                STORE_FAST               9 (e)

 534   L28:     LOAD_GLOBAL             32 (logger)
                LOAD_ATTR               35 (warning + NULL|self)

 535            LOAD_CONST              17 ('list_breakers query error type=')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 534            CALL                     1
                POP_TOP

 537            LOAD_GLOBAL             15 (_final + NULL)

 538            LOAD_CONST               4 ('status')
                LOAD_CONST               5 ('skipped')

 539            LOAD_CONST               6 ('surface')
                LOAD_FAST                2 (surface)

 540            LOAD_CONST               7 ('rows')
                BUILD_LIST               0

 541            LOAD_CONST               8 ('count')
                LOAD_SMALL_INT           0

 542            LOAD_CONST               9 ('warnings')
                LOAD_CONST              18 ('db_query_failed:')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 543            LOAD_CONST              11 ('error_code')
                LOAD_CONST              19 ('db_query_failed')

 537            BUILD_MAP                6

 544            LOAD_FAST                2 (surface)

 537            LOAD_CONST              12 (('surface',))
                CALL_KW                  2
       L29:     SWAP                     2
       L30:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
       L31:     RETURN_VALUE

  --   L32:     LOAD_CONST               3 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 533   L33:     RERAISE                  0

  --   L34:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L35:     PUSH_EXC_INFO

 558            LOAD_GLOBAL             30 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      101 (to L40)
                NOT_TAKEN
                STORE_FAST               9 (e)

 559   L36:     LOAD_GLOBAL             32 (logger)
                LOAD_ATTR               35 (warning + NULL|self)

 560            LOAD_CONST              22 ('list_breakers error type=')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 559            CALL                     1
                POP_TOP

 562            LOAD_GLOBAL             15 (_final + NULL)

 563            LOAD_CONST               4 ('status')
                LOAD_CONST               5 ('skipped')

 564            LOAD_CONST               6 ('surface')
                LOAD_FAST                2 (surface)

 565            LOAD_CONST               7 ('rows')
                BUILD_LIST               0

 566            LOAD_CONST               8 ('count')
                LOAD_SMALL_INT           0

 567            LOAD_CONST              11 ('error_code')
                LOAD_CONST              23 ('unexpected:')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 568            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 562            BUILD_MAP                6

 569            LOAD_FAST                2 (surface)

 562            LOAD_CONST              12 (('surface',))
                CALL_KW                  2
       L37:     SWAP                     2
       L38:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RETURN_VALUE

  --   L39:     LOAD_CONST               3 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 558   L40:     RERAISE                  0

  --   L41:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L35 [0]
  L3 to L4 -> L23 [0]
  L4 to L8 -> L35 [0]
  L10 to L11 -> L27 [0]
  L12 to L14 -> L27 [0]
  L14 to L15 -> L35 [0]
  L16 to L19 -> L35 [0]
  L20 to L22 -> L35 [0]
  L23 to L24 -> L26 [1] lasti
  L24 to L25 -> L35 [0]
  L25 to L26 -> L26 [1] lasti
  L26 to L27 -> L35 [0]
  L27 to L28 -> L34 [1] lasti
  L28 to L29 -> L32 [1] lasti
  L29 to L30 -> L34 [1] lasti
  L30 to L31 -> L35 [0]
  L32 to L34 -> L34 [1] lasti
  L34 to L35 -> L35 [0]
  L35 to L36 -> L41 [1] lasti
  L36 to L37 -> L39 [1] lasti
  L37 to L38 -> L41 [1] lasti
  L39 to L41 -> L41 [1] lasti
```
