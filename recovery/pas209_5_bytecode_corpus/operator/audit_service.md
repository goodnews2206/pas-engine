# operator/audit_service

- **pyc:** `app\services\operator\__pycache__\audit_service.cpython-314.pyc`
- **expected source path (absent):** `app\services\operator/audit_service.py`
- **co_filename (from bytecode):** `app\services\operator\audit_service.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** operator

## Module docstring

```
PAS174 — Operator action audit service (Supabase-backed v1).

Append-only durable audit log for every operator action.
Persists to ``pas_operator_actions_log`` (proposal at
``scripts/migrate_v22_operator_actions_log.sql``).

Doctrine carried by every helper:

* **Append-only.** This module exposes only ``log_operator_action``
  (INSERT) and the read helpers. There is NO update helper, NO
  delete helper, NO mutation surface anywhere. The PAS174
  readiness gate structurally enforces the absence of
  ``update_audit_*`` and ``delete_audit_*`` symbols.
* **Closed actor_type + status enums.** Mirrors the SQL CHECK
  constraints. Anything outside is rejected at the service
  layer.
* **Closed metadata allow-list.** The JSONB payload is
  projected against ``ALLOWED_METADATA_KEYS`` at write time;
  anything outside is dropped before insert.
* **No PII.** No phone / email / name / transcript / raw
  payload / signature / secret / env_value / callback_notes
  anywhere.
* **No exceptions escape.** DB unavailable → structural
  ``status="skipped"`` envelope. NEVER raises.
* **Bounded pagination.** Hard caps in the read helpers so an
  operator typo cannot table-scan.

Public surface:

  * ``ALLOWED_ACTOR_TYPES``     — closed enum.
  * ``ALLOWED_AUDIT_STATUSES``  — closed enum.
  * ``ALLOWED_METADATA_KEYS``   — closed allow-list.
  * ``log_operator_action(...)`` — append-only insert.
  * ``operator_action_history(...)``     — paginated read.
  * ``brokerage_action_history(...)``    — brokerage-scoped read.
  * ``recent_failed_operator_actions(...)`` — fast triage read.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `app.services.operator.audit_integrity`, `compute_row_hash`, `datetime`, `get_supabase`, `logging`, `timedelta`, `timezone`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_bound_str`, `_clamp_limit`, `_get_db_safe`, `_iso`, `_list_envelope`, `_now_dt`, `_project_metadata`, `_project_row`, `_read_chain_head_safe`, `_safe_envelope`, `_validate_actor_type`, `_validate_status`, `brokerage_action_history`, `log_operator_action`, `operator_action_history`, `recent_failed_operator_actions`

## Env-key candidates

`FAILED`, `GENESIS`

## String constants (redacted where noted)

- '\nPAS174 — Operator action audit service (Supabase-backed v1).\n\nAppend-only durable audit log for every operator action.\nPersists to ``pas_operator_actions_log`` (proposal at\n``scripts/migrate_v22_operator_actions_log.sql``).\n\nDoctrine carried by every helper:\n\n* **Append-only.** This module exposes only ``log_operator_action``\n  (INSERT) and the read helpers. There is NO update helper, NO\n  delete helper, NO mutation surface anywhere. The PAS174\n  readiness gate structurally enforces the absence of\n  ``update_audit_*`` and ``delete_audit_*`` symbols.\n* **Closed actor_type + status enums.** Mirrors the SQL CHECK\n  constraints. Anything outside is rejected at the service\n  layer.\n* **Closed metadata allow-list.** The JSONB payload is\n  projected against ``ALLOWED_METADATA_KEYS`` at write time;\n  anything outside is dropped before insert.\n* **No PII.** No phone / email / name / transcript / raw\n  payload / signature / secret / env_value / callback_notes\n  anywhere.\n* **No exceptions escape.** DB unavailable → structural\n  ``status="skipped"`` envelope. NEVER raises.\n* **Bounded pagination.** Hard caps in the read helpers so an\n  operator typo cannot table-scan.\n\nPublic surface:\n\n  * ``ALLOWED_ACTOR_TYPES``     — closed enum.\n  * ``ALLOWED_AUDIT_STATUSES``  — closed enum.\n  * ``ALLOWED_METADATA_KEYS``   — closed allow-list.\n  * ``log_operator_action(...)`` — append-only insert.\n  * ``operator_action_history(...)``     — paginated read.\n  * ``brokerage_action_history(...)``    — brokerage-scoped read.\n  * ``recent_failed_operator_actions(...)`` — fast triage read.\n'
- 'pas.operator.audit_service'
- 'pas_operator_actions_log'
- 'warning_count'
- 'error_code'
- 'brokerage_id'
- 'actor_type'
- 'target_type'
- 'target_id'
- 'metadata'
- 'audit_row'
- 'warnings'
- 'rows'
- 'count'
- 'limit'
- 'now'
- 'within_hours'
- 'Any'
- 'return'
- 'datetime'
- 'str'
- 'seconds'
- 'audit_service db client unavailable type='
- 'Read the most-recent ``row_hash`` from the audit log.\nReturns the literal GENESIS sentinel when the chain is\nempty or the column is missing. NEVER raises.'
- 'row_hash'
- 'occurred_at'
- 'data'
- 'GENESIS'
- '_read_chain_head_safe error type='
- 'value'
- 'max_len'
- 'int'
- 'Optional[str]'
- 'Dict[str, Any]'
- 'row'
- 'Optional[Dict[str, Any]]'
- 'status'
- 'Optional[List[str]]'
- 'Optional[List[Dict[str, Any]]]'
- 'invalid_actor_type'
- 'invalid_audit_status'
- 'actor_id'
- 'action'
- 'Append an operator-action audit row. Returns a\nstructural envelope.\n\nOutcomes:\n\n* ``status="ok"`` — fresh insert; ``audit_row`` populated.\n* ``status="skipped"`` — DB unavailable. Caller MUST treat\n  as a non-fatal observability gap; the operator action\n  itself proceeded.\n* ``status="failed"`` — input validation error.\n\nNEVER raises. NEVER returns raw payloads / secrets / PII.\n'
- 'failed'
- 'invalid_action'
- 'event'
- 'operator.action.executed'
- 'skipped'
- 'audit_store_unavailable'
- 'action_id'
- 'prev_hash'
- 'log_operator_action row_hash compute error type='
- 'log_operator_action db error type='
- 'db_write_failed:'
- 'Recent operator-action audit rows across all brokerages.\nRead-only. NEVER raises.'
- 'operator_action_history read error type='
- 'db_read_failed:'
- 'Brokerage-scoped audit history. NEVER raises.'
- 'missing_brokerage_id'
- 'brokerage_action_history read error type='
- 'Triage helper — recent FAILED audit rows in the last\n``within_hours``. NEVER raises.'
- 'FAILED'
- 'recent_failed_operator_actions read error type='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS174 — Operator action audit service (Supabase-backed v1).\n\nAppend-only durable audit log for every operator action.\nPersists to ``pas_operator_actions_log`` (proposal at\n``scripts/migrate_v22_operator_actions_log.sql``).\n\nDoctrine carried by every helper:\n\n* **Append-only.** This module exposes only ``log_operator_action``\n  (INSERT) and the read helpers. There is NO update helper, NO\n  delete helper, NO mutation surface anywhere. The PAS174\n  readiness gate structurally enforces the absence of\n  ``update_audit_*`` and ``delete_audit_*`` symbols.\n* **Closed actor_type + status enums.** Mirrors the SQL CHECK\n  constraints. Anything outside is rejected at the service\n  layer.\n* **Closed metadata allow-list.** The JSONB payload is\n  projected against ``ALLOWED_METADATA_KEYS`` at write time;\n  anything outside is dropped before insert.\n* **No PII.** No phone / email / name / transcript / raw\n  payload / signature / secret / env_value / callback_notes\n  anywhere.\n* **No exceptions escape.** DB unavailable → structural\n  ``status="skipped"`` envelope. NEVER raises.\n* **Bounded pagination.** Hard caps in the read helpers so an\n  operator typo cannot table-scan.\n\nPublic surface:\n\n  * ``ALLOWED_ACTOR_TYPES``     — closed enum.\n  * ``ALLOWED_AUDIT_STATUSES``  — closed enum.\n  * ``ALLOWED_METADATA_KEYS``   — closed allow-list.\n  * ``log_operator_action(...)`` — append-only insert.\n  * ``operator_action_history(...)``     — paginated read.\n  * ``brokerage_action_history(...)``    — brokerage-scoped read.\n  * ``recent_failed_operator_actions(...)`` — fast triage read.\n')
              STORE_NAME               0 (__doc__)

 40           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 42           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 43           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (uuid)
              STORE_NAME               4 (uuid)

 44           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timedelta', 'timezone'))
              IMPORT_NAME              5 (datetime)
              IMPORT_FROM              5 (datetime)
              STORE_NAME               5 (datetime)
              IMPORT_FROM              6 (timedelta)
              STORE_NAME               6 (timedelta)
              IMPORT_FROM              7 (timezone)
              STORE_NAME               7 (timezone)
              POP_TOP

 45           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              8 (typing)
              IMPORT_FROM              9 (Any)
              STORE_NAME               9 (Any)
              IMPORT_FROM             10 (Dict)
              STORE_NAME              10 (Dict)
              IMPORT_FROM             11 (List)
              STORE_NAME              11 (List)
              IMPORT_FROM             12 (Optional)
              STORE_NAME              12 (Optional)
              POP_TOP

 48           LOAD_NAME                3 (logging)
              LOAD_ATTR               26 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.operator.audit_service')
              CALL                     1
              STORE_NAME              14 (logger)

 51           LOAD_CONST               6 ('pas_operator_actions_log')
              STORE_NAME              15 (_TABLE)

 55           LOAD_CONST              53 (('OPERATOR', 'ADMIN', 'SYSTEM'))
              STORE_NAME              16 (ALLOWED_ACTOR_TYPES)

 61           LOAD_CONST              54 (('SUCCESS', 'FAILED', 'SKIPPED'))
              STORE_NAME              17 (ALLOWED_AUDIT_STATUSES)

 71           LOAD_CONST              55 (('event', 'warning_count', 'error_count', 'error_code', 'stage', 'target_status', 'launch_ready', 'probe_type', 'subsystem', 'onboarding_status', 'pilot_stage', 'evidence_audit_row_id', 'request_id', 'rotation_proposal_only'))
              STORE_NAME              18 (ALLOWED_METADATA_KEYS)

 90           LOAD_SMALL_INT         100
              STORE_NAME              19 (_ACTION_MAX_LEN)

 91           LOAD_SMALL_INT          64
              STORE_NAME              20 (_TARGET_TYPE_MAX_LEN)

 92           LOAD_SMALL_INT         200
              STORE_NAME              21 (_TARGET_ID_MAX_LEN)

 93           LOAD_SMALL_INT         200
              STORE_NAME              22 (_BROKERAGE_ID_MAX_LEN)

 94           LOAD_SMALL_INT         200
              STORE_NAME              23 (_ACTOR_ID_MAX_LEN)

 96           LOAD_CONST               9 (500)
              STORE_NAME              24 (_LIST_HARD_CAP)

 97           LOAD_SMALL_INT          50
              STORE_NAME              25 (_DEFAULT_LIMIT)

 99           LOAD_CONST              56 (('action_id', 'occurred_at', 'brokerage_id', 'actor_type', 'actor_id', 'action', 'target_type', 'target_id', 'status', 'warning_count', 'metadata', 'prev_hash', 'row_hash'))
              STORE_NAME              26 (_STRUCTURAL_COLUMNS)

124           LOAD_CONST              57 ((None,))
              LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA33C0, file "app\services\operator\audit_service.py", line 124>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _now_dt at 0x0000018C179C3C30, file "app\services\operator\audit_service.py", line 124>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              27 (_now_dt)

132           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\operator\audit_service.py", line 132>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _iso at 0x0000018C18025530, file "app\services\operator\audit_service.py", line 132>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_iso)

136           LOAD_CONST              19 (<code object _get_db_safe at 0x0000018C17FF13B0, file "app\services\operator\audit_service.py", line 136>)
              MAKE_FUNCTION
              STORE_NAME              29 (_get_db_safe)

148           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA2100, file "app\services\operator\audit_service.py", line 148>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object _read_chain_head_safe at 0x0000018C17EE1CC0, file "app\services\operator\audit_service.py", line 148>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_read_chain_head_safe)

174           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18024E30, file "app\services\operator\audit_service.py", line 174>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object _bound_str at 0x0000018C17972550, file "app\services\operator\audit_service.py", line 174>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_bound_str)

185           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA2970, file "app\services\operator\audit_service.py", line 185>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object _project_metadata at 0x0000018C17FED630, file "app\services\operator\audit_service.py", line 185>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_project_metadata)

201           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA23D0, file "app\services\operator\audit_service.py", line 201>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object _project_row at 0x0000018C1796DBD0, file "app\services\operator\audit_service.py", line 201>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_project_row)

212           LOAD_CONST              28 ('audit_row')

215           LOAD_CONST               2 (None)

212           LOAD_CONST              29 ('warnings')

216           LOAD_CONST               2 (None)

212           LOAD_CONST               8 ('error_code')

217           LOAD_CONST               2 (None)

212           BUILD_MAP                3
              LOAD_CONST              30 (<code object __annotate__ at 0x0000018C18024B30, file "app\services\operator\audit_service.py", line 212>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object _safe_envelope at 0x0000018C17FBFEE0, file "app\services\operator\audit_service.py", line 212>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              34 (_safe_envelope)

227           LOAD_CONST              32 ('rows')

230           LOAD_CONST               2 (None)

227           LOAD_CONST              33 ('count')

231           LOAD_SMALL_INT           0

227           LOAD_CONST              34 ('limit')

232           LOAD_NAME               25 (_DEFAULT_LIMIT)

227           LOAD_CONST              10 ('brokerage_id')

233           LOAD_CONST               2 (None)

227           LOAD_CONST              11 ('actor_type')

234           LOAD_CONST               2 (None)

227           LOAD_CONST              29 ('warnings')

235           LOAD_CONST               2 (None)

227           LOAD_CONST               8 ('error_code')

236           LOAD_CONST               2 (None)

227           BUILD_MAP                7
              LOAD_CONST              35 (<code object __annotate__ at 0x0000018C180C4250, file "app\services\operator\audit_service.py", line 227>)
              MAKE_FUNCTION
              LOAD_CONST              36 (<code object _list_envelope at 0x0000018C17FE1530, file "app\services\operator\audit_service.py", line 227>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              35 (_list_envelope)

250           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C17FA2D30, file "app\services\operator\audit_service.py", line 250>)
              MAKE_FUNCTION
              LOAD_CONST              38 (<code object _clamp_limit at 0x0000018C18010B30, file "app\services\operator\audit_service.py", line 250>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              36 (_clamp_limit)

262           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C17FA35A0, file "app\services\operator\audit_service.py", line 262>)
              MAKE_FUNCTION
              LOAD_CONST              40 (<code object _validate_actor_type at 0x0000018C17FA21F0, file "app\services\operator\audit_service.py", line 262>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              37 (_validate_actor_type)

268           LOAD_CONST              41 (<code object __annotate__ at 0x0000018C17FA30F0, file "app\services\operator\audit_service.py", line 268>)
              MAKE_FUNCTION
              LOAD_CONST              42 (<code object _validate_status at 0x0000018C17FA31E0, file "app\services\operator\audit_service.py", line 268>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              38 (_validate_status)

278           LOAD_CONST              12 ('target_type')

285           LOAD_CONST               2 (None)

278           LOAD_CONST              13 ('target_id')

286           LOAD_CONST               2 (None)

278           LOAD_CONST               7 ('warning_count')

287           LOAD_SMALL_INT           0

278           LOAD_CONST              14 ('metadata')

288           LOAD_CONST               2 (None)

278           LOAD_CONST              43 ('now')

289           LOAD_CONST               2 (None)

278           BUILD_MAP                5
              LOAD_CONST              44 (<code object __annotate__ at 0x0000018C180531B0, file "app\services\operator\audit_service.py", line 278>)
              MAKE_FUNCTION
              LOAD_CONST              45 (<code object log_operator_action at 0x0000018C17D8BF50, file "app\services\operator\audit_service.py", line 278>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              39 (log_operator_action)

383           LOAD_CONST              11 ('actor_type')

385           LOAD_CONST               2 (None)

383           LOAD_CONST              34 ('limit')

386           LOAD_NAME               25 (_DEFAULT_LIMIT)

383           BUILD_MAP                2
              LOAD_CONST              46 (<code object __annotate__ at 0x0000018C18025E30, file "app\services\operator\audit_service.py", line 383>)
              MAKE_FUNCTION
              LOAD_CONST              47 (<code object operator_action_history at 0x0000018C17EFB9B0, file "app\services\operator\audit_service.py", line 383>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              40 (operator_action_history)

430           LOAD_CONST              34 ('limit')

433           LOAD_NAME               25 (_DEFAULT_LIMIT)

430           BUILD_MAP                1
              LOAD_CONST              48 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\operator\audit_service.py", line 430>)
              MAKE_FUNCTION
              LOAD_CONST              49 (<code object brokerage_action_history at 0x0000018C17EDA2F0, file "app\services\operator\audit_service.py", line 430>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              41 (brokerage_action_history)

476           LOAD_CONST              50 ('within_hours')

478           LOAD_SMALL_INT          24

476           LOAD_CONST              34 ('limit')

479           LOAD_NAME               25 (_DEFAULT_LIMIT)

476           BUILD_MAP                2
              LOAD_CONST              51 (<code object __annotate__ at 0x0000018C18024930, file "app\services\operator\audit_service.py", line 476>)
              MAKE_FUNCTION
              LOAD_CONST              52 (<code object recent_failed_operator_actions at 0x0000018C17D513C0, file "app\services\operator\audit_service.py", line 476>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              42 (recent_failed_operator_actions)

528           BUILD_LIST               0
              LOAD_CONST              58 (('ALLOWED_ACTOR_TYPES', 'ALLOWED_AUDIT_STATUSES', 'ALLOWED_METADATA_KEYS', 'log_operator_action', 'operator_action_history', 'brokerage_action_history', 'recent_failed_operator_actions'))
              LIST_EXTEND              1
              STORE_NAME              43 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app\services\operator\audit_service.py", line 124>:
124           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('now')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('datetime')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _now_dt at 0x0000018C179C3C30, file "app\services\operator\audit_service.py", line 124>:
124           RESUME                   0

125           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (now)
              LOAD_GLOBAL              2 (datetime)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       78 (to L2)
              NOT_TAKEN

126           LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR                4 (tzinfo)
              POP_JUMP_IF_NOT_NONE    33 (to L1)
              NOT_TAKEN

127           LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR                7 (replace + NULL|self)
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              LOAD_CONST               1 (('tzinfo',))
              CALL_KW                  1
              RETURN_VALUE

128   L1:     LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR               13 (astimezone + NULL|self)
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              CALL                     1
              RETURN_VALUE

129   L2:     LOAD_GLOBAL              2 (datetime)
              LOAD_ATTR               14 (now)
              PUSH_NULL
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\operator\audit_service.py", line 132>:
132           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('dt')
              LOAD_CONST               2 ('datetime')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _iso at 0x0000018C18025530, file "app\services\operator\audit_service.py", line 132>:
132           RESUME                   0

133           LOAD_FAST_BORROW         0 (dt)
              LOAD_ATTR                1 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object _get_db_safe at 0x0000018C17FF13B0, file "app\services\operator\audit_service.py", line 136>:
 136           RESUME                   0

 137           NOP

 138   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 139           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 140           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 141   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 142           LOAD_CONST               2 ('audit_service db client unavailable type=')

 143           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 142           BUILD_STRING             2

 141           CALL                     1
               POP_TOP

 145   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 140   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app\services\operator\audit_service.py", line 148>:
148           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('db')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _read_chain_head_safe at 0x0000018C17EE1CC0, file "app\services\operator\audit_service.py", line 148>:
 148            RESUME                   0

 152            NOP

 154    L1:     LOAD_FAST_BORROW         0 (db)
                LOAD_ATTR                1 (table + NULL|self)
                LOAD_GLOBAL              2 (_TABLE)
                CALL                     1

 155            LOAD_ATTR                5 (select + NULL|self)
                LOAD_CONST               1 ('row_hash')
                CALL                     1

 156            LOAD_ATTR                7 (order + NULL|self)
                LOAD_CONST               2 ('occurred_at')
                LOAD_CONST               3 (True)
                LOAD_CONST               4 (('desc',))
                CALL_KW                  2

 157            LOAD_ATTR                9 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 158            LOAD_ATTR               11 (execute + NULL|self)
                CALL                     0

 153            STORE_FAST               1 (result)

 160            LOAD_GLOBAL             13 (list + NULL)
                LOAD_GLOBAL             15 (getattr + NULL)
                LOAD_FAST_BORROW         1 (result)
                LOAD_CONST               5 ('data')
                LOAD_CONST               6 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
        L2:     NOT_TAKEN
        L3:     POP_TOP
                BUILD_LIST               0
        L4:     CALL                     1
                STORE_FAST               2 (rows)

 161            LOAD_FAST_BORROW         2 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
        L5:     NOT_TAKEN

 162            LOAD_CONST               7 ('GENESIS')
                RETURN_VALUE

 163    L6:     LOAD_FAST_BORROW         2 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               1 ('row_hash')
                CALL                     1
                STORE_FAST               3 (head)

 164            LOAD_GLOBAL             19 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (head)
                LOAD_GLOBAL             20 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L10)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (head)
                LOAD_ATTR               23 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L10)
        L7:     NOT_TAKEN

 165    L8:     LOAD_FAST_BORROW         3 (head)
                LOAD_ATTR               23 (strip + NULL|self)
                CALL                     0
        L9:     RETURN_VALUE

 166   L10:     LOAD_CONST               7 ('GENESIS')
                RETURN_VALUE

  --   L11:     PUSH_EXC_INFO

 167            LOAD_GLOBAL             24 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L15)
                NOT_TAKEN
                STORE_FAST               4 (e)

 168   L12:     LOAD_GLOBAL             26 (logger)
                LOAD_ATTR               29 (warning + NULL|self)

 169            LOAD_CONST               8 ('_read_chain_head_safe error type=')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 168            CALL                     1
                POP_TOP

 171   L13:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                LOAD_CONST               7 ('GENESIS')
                RETURN_VALUE

  --   L14:     LOAD_CONST               6 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 167   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L11 [0]
  L3 to L5 -> L11 [0]
  L6 to L7 -> L11 [0]
  L8 to L9 -> L11 [0]
  L11 to L12 -> L16 [1] lasti
  L12 to L13 -> L14 [1] lasti
  L14 to L16 -> L16 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app\services\operator\audit_service.py", line 174>:
174           RESUME                   0
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

Disassembly of <code object _bound_str at 0x0000018C17972550, file "app\services\operator\audit_service.py", line 174>:
174           RESUME                   0

175           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

176           LOAD_CONST               0 (None)
              RETURN_VALUE

177   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (s)

178           LOAD_FAST_BORROW         2 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

179           LOAD_CONST               0 (None)
              RETURN_VALUE

180   L2:     LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         2 (s)
              CALL                     1
              LOAD_FAST_BORROW         1 (max_len)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

181           LOAD_CONST               0 (None)
              RETURN_VALUE

182   L3:     LOAD_FAST_BORROW         2 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app\services\operator\audit_service.py", line 185>:
185           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('metadata')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _project_metadata at 0x0000018C17FED630, file "app\services\operator\audit_service.py", line 185>:
185           RESUME                   0

186           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (metadata)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

187           BUILD_MAP                0
              RETURN_VALUE

188   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

189           LOAD_GLOBAL              4 (ALLOWED_METADATA_KEYS)
              GET_ITER
      L2:     FOR_ITER               108 (to L8)
              STORE_FAST               2 (k)

190           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, metadata)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

191           JUMP_BACKWARD           11 (to L2)

192   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (metadata, k)
              BINARY_OP               26 ([])
              STORE_FAST               3 (v)

193           LOAD_FAST_BORROW         3 (v)
              POP_JUMP_IF_NONE        34 (to L4)
              NOT_TAKEN
              LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (v)
              LOAD_GLOBAL              6 (int)
              LOAD_GLOBAL              8 (float)
              LOAD_GLOBAL             10 (bool)
              BUILD_TUPLE              3
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        7 (to L5)
              NOT_TAKEN

194   L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD           62 (to L2)

195   L5:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (v)
              LOAD_GLOBAL             12 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              JUMP_BACKWARD           86 (to L2)

196   L6:     LOAD_GLOBAL             15 (len + NULL)
              LOAD_FAST_BORROW         3 (v)
              CALL                     1
              LOAD_SMALL_INT         200
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_TRUE         3 (to L7)
              NOT_TAKEN
              JUMP_BACKWARD          104 (to L2)

197   L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD          110 (to L2)

189   L8:     END_FOR
              POP_ITER

198           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app\services\operator\audit_service.py", line 201>:
201           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[Dict[str, Any]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _project_row at 0x0000018C1796DBD0, file "app\services\operator\audit_service.py", line 201>:
201           RESUME                   0

202           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

203           LOAD_CONST               0 (None)
              RETURN_VALUE

204   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

205           LOAD_GLOBAL              4 (_STRUCTURAL_COLUMNS)
              GET_ITER
      L2:     FOR_ITER                21 (to L4)
              STORE_FAST               2 (col)

206           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (col, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

207   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, col)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, col)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L2)

205   L4:     END_FOR
              POP_ITER

208           LOAD_GLOBAL              7 (_project_metadata + NULL)
              LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               1 ('metadata')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L5:     CALL                     1
              LOAD_FAST_BORROW         1 (out)
              LOAD_CONST               1 ('metadata')
              STORE_SUBSCR

209           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app\services\operator\audit_service.py", line 212>:
212           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

214           LOAD_CONST               2 ('str')

212           LOAD_CONST               3 ('audit_row')

215           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

212           LOAD_CONST               5 ('warnings')

216           LOAD_CONST               6 ('Optional[List[str]]')

212           LOAD_CONST               7 ('error_code')

217           LOAD_CONST               8 ('Optional[str]')

212           LOAD_CONST               9 ('return')

218           LOAD_CONST              10 ('Dict[str, Any]')

212           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C17FBFEE0, file "app\services\operator\audit_service.py", line 212>:
212           RESUME                   0

220           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

221           LOAD_CONST               1 ('audit_row')
              LOAD_FAST                1 (audit_row)

222           LOAD_CONST               2 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                2 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

223           LOAD_CONST               3 ('error_code')
              LOAD_FAST_BORROW         3 (error_code)

219           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180C4250, file "app\services\operator\audit_service.py", line 227>:
227           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

229           LOAD_CONST               2 ('str')

227           LOAD_CONST               3 ('rows')

230           LOAD_CONST               4 ('Optional[List[Dict[str, Any]]]')

227           LOAD_CONST               5 ('count')

231           LOAD_CONST               6 ('int')

227           LOAD_CONST               7 ('limit')

232           LOAD_CONST               6 ('int')

227           LOAD_CONST               8 ('brokerage_id')

233           LOAD_CONST               9 ('Optional[str]')

227           LOAD_CONST              10 ('actor_type')

234           LOAD_CONST               9 ('Optional[str]')

227           LOAD_CONST              11 ('warnings')

235           LOAD_CONST              12 ('Optional[List[str]]')

227           LOAD_CONST              13 ('error_code')

236           LOAD_CONST               9 ('Optional[str]')

227           LOAD_CONST              14 ('return')

237           LOAD_CONST              15 ('Dict[str, Any]')

227           BUILD_MAP                9
              RETURN_VALUE

Disassembly of <code object _list_envelope at 0x0000018C17FE1530, file "app\services\operator\audit_service.py", line 227>:
227           RESUME                   0

239           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

240           LOAD_CONST               1 ('rows')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                1 (rows)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

241           LOAD_CONST               2 ('count')
              LOAD_FAST                2 (count)

242           LOAD_CONST               3 ('limit')
              LOAD_FAST                3 (limit)

243           LOAD_CONST               4 ('brokerage_id')
              LOAD_FAST                4 (brokerage_id)

244           LOAD_CONST               5 ('actor_type')
              LOAD_FAST                5 (actor_type)

245           LOAD_CONST               6 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                6 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L2:     CALL                     1

246           LOAD_CONST               7 ('error_code')
              LOAD_FAST_BORROW         7 (error_code)

238           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app\services\operator\audit_service.py", line 250>:
250           RESUME                   0
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

Disassembly of <code object _clamp_limit at 0x0000018C18010B30, file "app\services\operator\audit_service.py", line 250>:
 250           RESUME                   0

 251           NOP

 252   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (v)

 255   L2:     LOAD_FAST                1 (v)
               LOAD_SMALL_INT           1
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 256           LOAD_SMALL_INT           1
               RETURN_VALUE

 257   L3:     LOAD_FAST                1 (v)
               LOAD_GLOBAL              8 (_LIST_HARD_CAP)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 258           LOAD_GLOBAL              8 (_LIST_HARD_CAP)
               RETURN_VALUE

 259   L4:     LOAD_FAST                1 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 253           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

 254           LOAD_GLOBAL              6 (_DEFAULT_LIMIT)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 253   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app\services\operator\audit_service.py", line 262>:
262           RESUME                   0
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

Disassembly of <code object _validate_actor_type at 0x0000018C17FA21F0, file "app\services\operator\audit_service.py", line 262>:
262           RESUME                   0

263           LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              0 (ALLOWED_ACTOR_TYPES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

264           LOAD_CONST               0 ('invalid_actor_type')
              RETURN_VALUE

265   L1:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "app\services\operator\audit_service.py", line 268>:
268           RESUME                   0
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

Disassembly of <code object _validate_status at 0x0000018C17FA31E0, file "app\services\operator\audit_service.py", line 268>:
268           RESUME                   0

269           LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              0 (ALLOWED_AUDIT_STATUSES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

270           LOAD_CONST               0 ('invalid_audit_status')
              RETURN_VALUE

271   L1:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180531B0, file "app\services\operator\audit_service.py", line 278>:
278           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

280           LOAD_CONST               2 ('Optional[str]')

278           LOAD_CONST               3 ('actor_type')

281           LOAD_CONST               4 ('str')

278           LOAD_CONST               5 ('actor_id')

282           LOAD_CONST               2 ('Optional[str]')

278           LOAD_CONST               6 ('action')

283           LOAD_CONST               4 ('str')

278           LOAD_CONST               7 ('status')

284           LOAD_CONST               4 ('str')

278           LOAD_CONST               8 ('target_type')

285           LOAD_CONST               2 ('Optional[str]')

278           LOAD_CONST               9 ('target_id')

286           LOAD_CONST               2 ('Optional[str]')

278           LOAD_CONST              10 ('warning_count')

287           LOAD_CONST              11 ('int')

278           LOAD_CONST              12 ('metadata')

288           LOAD_CONST              13 ('Optional[Dict[str, Any]]')

278           LOAD_CONST              14 ('now')

289           LOAD_CONST              15 ('Any')

278           LOAD_CONST              16 ('return')

290           LOAD_CONST              17 ('Dict[str, Any]')

278           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object log_operator_action at 0x0000018C17D8BF50, file "app\services\operator\audit_service.py", line 278>:
 278            RESUME                   0

 304            LOAD_GLOBAL              1 (_validate_actor_type + NULL)
                LOAD_FAST_BORROW         1 (actor_type)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_GLOBAL              3 (_validate_status + NULL)
                LOAD_FAST_BORROW         4 (status)
                CALL                     1
        L1:     STORE_FAST              10 (err)

 305            LOAD_FAST_BORROW        10 (err)
                POP_JUMP_IF_NONE        14 (to L2)
                NOT_TAKEN

 306            LOAD_GLOBAL              5 (_safe_envelope + NULL)
                LOAD_CONST               2 ('failed')
                LOAD_FAST_BORROW        10 (err)
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 307    L2:     LOAD_GLOBAL              7 (_bound_str + NULL)
                LOAD_FAST_BORROW         3 (action)
                LOAD_GLOBAL              8 (_ACTION_MAX_LEN)
                CALL                     2
                STORE_FAST              11 (action_bounded)

 308            LOAD_FAST_BORROW        11 (action_bounded)
                POP_JUMP_IF_NOT_NONE    14 (to L3)
                NOT_TAKEN

 309            LOAD_GLOBAL              5 (_safe_envelope + NULL)
                LOAD_CONST               2 ('failed')
                LOAD_CONST               4 ('invalid_action')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 311    L3:     LOAD_GLOBAL              7 (_bound_str + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_GLOBAL             10 (_BROKERAGE_ID_MAX_LEN)
                CALL                     2
                STORE_FAST              12 (bid)

 312            LOAD_GLOBAL              7 (_bound_str + NULL)
                LOAD_FAST_BORROW         2 (actor_id)
                LOAD_GLOBAL             12 (_ACTOR_ID_MAX_LEN)
                CALL                     2
                STORE_FAST              13 (actor)

 313            LOAD_GLOBAL              7 (_bound_str + NULL)
                LOAD_FAST_BORROW         5 (target_type)
                LOAD_GLOBAL             14 (_TARGET_TYPE_MAX_LEN)
                CALL                     2
                STORE_FAST              14 (t_type)

 314            LOAD_GLOBAL              7 (_bound_str + NULL)
                LOAD_FAST_BORROW         6 (target_id)
                LOAD_GLOBAL             16 (_TARGET_ID_MAX_LEN)
                CALL                     2
                STORE_FAST              15 (t_id)

 315            NOP

 316    L4:     LOAD_GLOBAL             19 (int + NULL)
                LOAD_FAST_BORROW         7 (warning_count)
                CALL                     1
                STORE_FAST              16 (wc)

 317            LOAD_FAST_BORROW        16 (wc)
                LOAD_SMALL_INT           0
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

 318            LOAD_SMALL_INT           0
                STORE_FAST              16 (wc)

 321    L5:     LOAD_GLOBAL             25 (_project_metadata + NULL)
                LOAD_FAST                8 (metadata)
                CALL                     1
                STORE_FAST              17 (md)

 323            LOAD_FAST               17 (md)
                LOAD_ATTR               27 (setdefault + NULL|self)
                LOAD_CONST               5 ('event')
                LOAD_CONST               6 ('operator.action.executed')
                CALL                     2
                POP_TOP

 325            LOAD_GLOBAL             29 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST              18 (db)

 326            LOAD_FAST               18 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L6)
                NOT_TAKEN

 327            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 328            LOAD_CONST               7 ('skipped')

 329            LOAD_CONST               8 ('audit_store_unavailable')
                BUILD_LIST               1

 330            LOAD_CONST               8 ('audit_store_unavailable')

 327            LOAD_CONST               9 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 334    L6:     LOAD_CONST              10 ('action_id')
                LOAD_GLOBAL             31 (str + NULL)
                LOAD_GLOBAL             32 (uuid)
                LOAD_ATTR               34 (uuid4)
                PUSH_NULL
                CALL                     0
                CALL                     1

 335            LOAD_CONST              11 ('occurred_at')
                LOAD_GLOBAL             37 (_iso + NULL)
                LOAD_GLOBAL             39 (_now_dt + NULL)
                LOAD_FAST                9 (now)
                CALL                     1
                CALL                     1

 336            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST               12 (bid)

 337            LOAD_CONST              13 ('actor_type')
                LOAD_FAST                1 (actor_type)

 338            LOAD_CONST              14 ('actor_id')
                LOAD_FAST               13 (actor)

 339            LOAD_CONST              15 ('action')
                LOAD_FAST               11 (action_bounded)

 340            LOAD_CONST              16 ('target_type')
                LOAD_FAST               14 (t_type)

 341            LOAD_CONST              17 ('target_id')
                LOAD_FAST               15 (t_id)

 342            LOAD_CONST              18 ('status')
                LOAD_FAST                4 (status)

 343            LOAD_CONST              19 ('warning_count')
                LOAD_FAST               16 (wc)

 344            LOAD_CONST              20 ('metadata')
                LOAD_FAST               17 (md)

 333            BUILD_MAP               11
                STORE_FAST              19 (row)

 352            LOAD_GLOBAL             41 (_read_chain_head_safe + NULL)
                LOAD_FAST               18 (db)
                CALL                     1
                STORE_FAST              20 (_chain_prev)

 353            LOAD_FAST               20 (_chain_prev)
                LOAD_FAST               19 (row)
                LOAD_CONST              21 ('prev_hash')
                STORE_SUBSCR

 354            NOP

 355    L7:     LOAD_SMALL_INT           0
                LOAD_CONST              22 (('compute_row_hash',))
                IMPORT_NAME             21 (app.services.operator.audit_integrity)
                IMPORT_FROM             22 (compute_row_hash)
                STORE_FAST              21 (compute_row_hash)
                POP_TOP

 356            LOAD_FAST               21 (compute_row_hash)
                PUSH_NULL
                LOAD_FAST               20 (_chain_prev)
                LOAD_FAST               19 (row)
                CALL                     2
                LOAD_FAST               19 (row)
                LOAD_CONST              23 ('row_hash')
                STORE_SUBSCR

 363    L8:     NOP

 364    L9:     LOAD_FAST               18 (db)
                LOAD_ATTR               57 (table + NULL|self)
                LOAD_GLOBAL             58 (_TABLE)
                CALL                     1
                LOAD_ATTR               61 (insert + NULL|self)
                LOAD_FAST               19 (row)
                CALL                     1
                LOAD_ATTR               63 (execute + NULL|self)
                CALL                     0
                STORE_FAST              23 (result)

 365            LOAD_GLOBAL             65 (list + NULL)
                LOAD_GLOBAL             67 (getattr + NULL)
                LOAD_FAST               23 (result)
                LOAD_CONST              25 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
       L10:     NOT_TAKEN
       L11:     POP_TOP
                BUILD_LIST               0
       L12:     CALL                     1
                STORE_FAST              24 (rows)

 366            LOAD_FAST               24 (rows)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L15)
       L13:     NOT_TAKEN
       L14:     LOAD_GLOBAL             69 (_project_row + NULL)
                LOAD_FAST               24 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                JUMP_FORWARD            10 (to L16)
       L15:     LOAD_GLOBAL             69 (_project_row + NULL)
                LOAD_FAST               19 (row)
                CALL                     1
       L16:     STORE_FAST              25 (proj)

 367            LOAD_GLOBAL              5 (_safe_envelope + NULL)
                LOAD_CONST              26 ('ok')
                LOAD_FAST               25 (proj)
                LOAD_CONST              27 (('status', 'audit_row'))
                CALL_KW                  2
       L17:     RETURN_VALUE

  --   L18:     PUSH_EXC_INFO

 319            LOAD_GLOBAL             20 (TypeError)
                LOAD_GLOBAL             22 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        7 (to L20)
                NOT_TAKEN
                POP_TOP

 320            LOAD_SMALL_INT           0
                STORE_FAST              16 (wc)
       L19:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 318 (to L5)

 319   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L22:     PUSH_EXC_INFO

 357            LOAD_GLOBAL             46 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       59 (to L26)
                NOT_TAKEN
                STORE_FAST              22 (e)

 358   L23:     LOAD_GLOBAL             48 (logger)
                LOAD_ATTR               51 (warning + NULL|self)

 359            LOAD_CONST              24 ('log_operator_action row_hash compute error type=')

 360            LOAD_GLOBAL             53 (type + NULL)
                LOAD_FAST               22 (e)
                CALL                     1
                LOAD_ATTR               54 (__name__)
                FORMAT_SIMPLE

 359            BUILD_STRING             2

 358            CALL                     1
                POP_TOP

 362            LOAD_CONST               1 (None)
                LOAD_FAST               19 (row)
                LOAD_CONST              23 ('row_hash')
                STORE_SUBSCR
       L24:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              22 (e)
                DELETE_FAST             22 (e)
                JUMP_BACKWARD_NO_INTERRUPT 223 (to L8)

  --   L25:     LOAD_CONST               1 (None)
                STORE_FAST              22 (e)
                DELETE_FAST             22 (e)
                RERAISE                  1

 357   L26:     RERAISE                  0

  --   L27:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L28:     PUSH_EXC_INFO

 368            LOAD_GLOBAL             46 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L33)
                NOT_TAKEN
                STORE_FAST              22 (e)

 369   L29:     LOAD_GLOBAL             48 (logger)
                LOAD_ATTR               51 (warning + NULL|self)

 370            LOAD_CONST              28 ('log_operator_action db error type=')
                LOAD_GLOBAL             53 (type + NULL)
                LOAD_FAST               22 (e)
                CALL                     1
                LOAD_ATTR               54 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 369            CALL                     1
                POP_TOP

 372            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 373            LOAD_CONST               7 ('skipped')

 374            LOAD_CONST              29 ('db_write_failed:')
                LOAD_GLOBAL             53 (type + NULL)
                LOAD_FAST               22 (e)
                CALL                     1
                LOAD_ATTR               54 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 375            LOAD_CONST               8 ('audit_store_unavailable')

 372            LOAD_CONST               9 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
       L30:     SWAP                     2
       L31:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              22 (e)
                DELETE_FAST             22 (e)
                RETURN_VALUE

  --   L32:     LOAD_CONST               1 (None)
                STORE_FAST              22 (e)
                DELETE_FAST             22 (e)
                RERAISE                  1

 368   L33:     RERAISE                  0

  --   L34:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L18 [0]
  L7 to L8 -> L22 [0]
  L9 to L10 -> L28 [0]
  L11 to L13 -> L28 [0]
  L14 to L17 -> L28 [0]
  L18 to L19 -> L21 [1] lasti
  L20 to L21 -> L21 [1] lasti
  L22 to L23 -> L27 [1] lasti
  L23 to L24 -> L25 [1] lasti
  L25 to L27 -> L27 [1] lasti
  L28 to L29 -> L34 [1] lasti
  L29 to L30 -> L32 [1] lasti
  L30 to L31 -> L34 [1] lasti
  L32 to L34 -> L34 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app\services\operator\audit_service.py", line 383>:
383           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('actor_type')

385           LOAD_CONST               2 ('Optional[str]')

383           LOAD_CONST               3 ('limit')

386           LOAD_CONST               4 ('Any')

383           LOAD_CONST               5 ('return')

387           LOAD_CONST               6 ('Dict[str, Any]')

383           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object operator_action_history at 0x0000018C17EFB9B0, file "app\services\operator\audit_service.py", line 383>:
 383            RESUME                   0

 390            LOAD_FAST_BORROW         0 (actor_type)
                POP_JUMP_IF_NONE        26 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (actor_type)
                LOAD_GLOBAL              0 (ALLOWED_ACTOR_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       15 (to L1)
                NOT_TAKEN

 391            LOAD_GLOBAL              3 (_list_envelope + NULL)

 392            LOAD_CONST               2 ('failed')
                LOAD_FAST_BORROW         0 (actor_type)

 393            LOAD_CONST               3 ('invalid_actor_type')

 391            LOAD_CONST               4 (('status', 'actor_type', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 395    L1:     LOAD_GLOBAL              5 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         1 (limit)
                CALL                     1
                STORE_FAST               2 (capped)

 396            LOAD_GLOBAL              7 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               3 (db)

 397            LOAD_FAST_BORROW         3 (db)
                POP_JUMP_IF_NOT_NONE    17 (to L2)
                NOT_TAKEN

 398            LOAD_GLOBAL              3 (_list_envelope + NULL)

 399            LOAD_CONST               5 ('skipped')
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (actor_type, capped)

 400            LOAD_CONST               6 ('audit_store_unavailable')
                BUILD_LIST               1

 401            LOAD_CONST               6 ('audit_store_unavailable')

 398            LOAD_CONST               7 (('status', 'actor_type', 'limit', 'warnings', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

 403    L2:     NOP

 405    L3:     LOAD_FAST_BORROW         3 (db)
                LOAD_ATTR                9 (table + NULL|self)
                LOAD_GLOBAL             10 (_TABLE)
                CALL                     1

 406            LOAD_ATTR               13 (select + NULL|self)
                LOAD_CONST               8 (',')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_GLOBAL             16 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 407            LOAD_ATTR               19 (order + NULL|self)
                LOAD_CONST               9 ('occurred_at')
                LOAD_CONST              10 (True)
                LOAD_CONST              11 (('desc',))
                CALL_KW                  2

 408            LOAD_ATTR               21 (limit + NULL|self)
                LOAD_FAST_BORROW         2 (capped)
                CALL                     1

 404            STORE_FAST               4 (query)

 410            LOAD_FAST_BORROW         0 (actor_type)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L6)
        L4:     NOT_TAKEN

 411    L5:     LOAD_FAST_BORROW         4 (query)
                LOAD_ATTR               23 (eq + NULL|self)
                LOAD_CONST              12 ('actor_type')
                LOAD_FAST_BORROW         0 (actor_type)
                CALL                     2
                STORE_FAST               4 (query)

 412    L6:     LOAD_FAST_BORROW         4 (query)
                LOAD_ATTR               25 (execute + NULL|self)
                CALL                     0
                STORE_FAST               5 (result)

 413            LOAD_GLOBAL             27 (list + NULL)
                LOAD_GLOBAL             29 (getattr + NULL)
                LOAD_FAST_BORROW         5 (result)
                LOAD_CONST              13 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
        L7:     NOT_TAKEN
        L8:     POP_TOP
                BUILD_LIST               0
        L9:     CALL                     1
                STORE_FAST               6 (rows)

 414            LOAD_CONST              14 (<code object <genexpr> at 0x0000018C180C4580, file "app\services\operator\audit_service.py", line 414>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         6 (rows)
                GET_ITER
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      7 (p)
                SWAP                     2
       L10:     BUILD_LIST               0
                SWAP                     2
       L11:     FOR_ITER                10 (to L14)
                STORE_FAST_LOAD_FAST   119 (p, p)
       L12:     POP_JUMP_IF_NOT_NONE     3 (to L13)
                NOT_TAKEN
                JUMP_BACKWARD            8 (to L11)
       L13:     LOAD_FAST_BORROW         7 (p)
                LIST_APPEND              2
                JUMP_BACKWARD           12 (to L11)
       L14:     END_FOR
                POP_ITER
       L15:     STORE_FAST               8 (projected)
                STORE_FAST               7 (p)

 415            LOAD_GLOBAL              3 (_list_envelope + NULL)

 416            LOAD_CONST              15 ('ok')
                LOAD_FAST_BORROW         8 (projected)
                LOAD_GLOBAL             31 (len + NULL)
                LOAD_FAST_BORROW         8 (projected)
                CALL                     1

 417            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (actor_type, capped)

 415            LOAD_CONST              16 (('status', 'rows', 'count', 'actor_type', 'limit'))
                CALL_KW                  5
       L16:     RETURN_VALUE

  --   L17:     SWAP                     2
                POP_TOP

 414            SWAP                     2
                STORE_FAST               7 (p)
                RERAISE                  0

  --   L18:     PUSH_EXC_INFO

 419            LOAD_GLOBAL             32 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       92 (to L23)
                NOT_TAKEN
                STORE_FAST               9 (e)

 420   L19:     LOAD_GLOBAL             34 (logger)
                LOAD_ATTR               37 (warning + NULL|self)

 421            LOAD_CONST              17 ('operator_action_history read error type=')
                LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 420            CALL                     1
                POP_TOP

 423            LOAD_GLOBAL              3 (_list_envelope + NULL)

 424            LOAD_CONST               5 ('skipped')
                LOAD_FAST_LOAD_FAST      2 (actor_type, capped)

 425            LOAD_CONST              18 ('db_read_failed:')
                LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 426            LOAD_CONST               6 ('audit_store_unavailable')

 423            LOAD_CONST               7 (('status', 'actor_type', 'limit', 'warnings', 'error_code'))
                CALL_KW                  5
       L20:     SWAP                     2
       L21:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RETURN_VALUE

  --   L22:     LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 419   L23:     RERAISE                  0

  --   L24:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L18 [0]
  L5 to L7 -> L18 [0]
  L8 to L10 -> L18 [0]
  L10 to L12 -> L17 [2]
  L13 to L15 -> L17 [2]
  L15 to L16 -> L18 [0]
  L17 to L18 -> L18 [0]
  L18 to L19 -> L24 [1] lasti
  L19 to L20 -> L22 [1] lasti
  L20 to L21 -> L24 [1] lasti
  L22 to L24 -> L24 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C180C4580, file "app\services\operator\audit_service.py", line 414>:
 414           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (_project_row + NULL)
               LOAD_FAST_BORROW         1 (r)
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           18 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\operator\audit_service.py", line 430>:
430           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

431           LOAD_CONST               2 ('str')

430           LOAD_CONST               3 ('limit')

433           LOAD_CONST               4 ('Any')

430           LOAD_CONST               5 ('return')

434           LOAD_CONST               6 ('Dict[str, Any]')

430           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object brokerage_action_history at 0x0000018C17EDA2F0, file "app\services\operator\audit_service.py", line 430>:
 430            RESUME                   0

 436            LOAD_GLOBAL              1 (_bound_str + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_GLOBAL              2 (_BROKERAGE_ID_MAX_LEN)
                CALL                     2
                STORE_FAST               2 (bid)

 437            LOAD_FAST_BORROW         2 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L1)
                NOT_TAKEN

 438            LOAD_GLOBAL              5 (_list_envelope + NULL)

 439            LOAD_CONST               2 ('failed')

 440            LOAD_CONST               3 ('missing_brokerage_id')

 438            LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 442    L1:     LOAD_GLOBAL              7 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         1 (limit)
                CALL                     1
                STORE_FAST               3 (capped)

 443            LOAD_GLOBAL              9 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               4 (db)

 444            LOAD_FAST_BORROW         4 (db)
                POP_JUMP_IF_NOT_NONE    17 (to L2)
                NOT_TAKEN

 445            LOAD_GLOBAL              5 (_list_envelope + NULL)

 446            LOAD_CONST               5 ('skipped')
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (bid, capped)

 447            LOAD_CONST               6 ('audit_store_unavailable')
                BUILD_LIST               1

 448            LOAD_CONST               6 ('audit_store_unavailable')

 445            LOAD_CONST               7 (('status', 'brokerage_id', 'limit', 'warnings', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

 450    L2:     NOP

 452    L3:     LOAD_FAST_BORROW         4 (db)
                LOAD_ATTR               11 (table + NULL|self)
                LOAD_GLOBAL             12 (_TABLE)
                CALL                     1

 453            LOAD_ATTR               15 (select + NULL|self)
                LOAD_CONST               8 (',')
                LOAD_ATTR               17 (join + NULL|self)
                LOAD_GLOBAL             18 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 454            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST               9 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)
                CALL                     2

 455            LOAD_ATTR               23 (order + NULL|self)
                LOAD_CONST              10 ('occurred_at')
                LOAD_CONST              11 (True)
                LOAD_CONST              12 (('desc',))
                CALL_KW                  2

 456            LOAD_ATTR               25 (limit + NULL|self)
                LOAD_FAST_BORROW         3 (capped)
                CALL                     1

 457            LOAD_ATTR               27 (execute + NULL|self)
                CALL                     0

 451            STORE_FAST               5 (result)

 459            LOAD_GLOBAL             29 (list + NULL)
                LOAD_GLOBAL             31 (getattr + NULL)
                LOAD_FAST_BORROW         5 (result)
                LOAD_CONST              13 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
        L4:     NOT_TAKEN
        L5:     POP_TOP
                BUILD_LIST               0
        L6:     CALL                     1
                STORE_FAST               6 (rows)

 460            LOAD_CONST              14 (<code object <genexpr> at 0x0000018C180C4360, file "app\services\operator\audit_service.py", line 460>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         6 (rows)
                GET_ITER
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      7 (p)
                SWAP                     2
        L7:     BUILD_LIST               0
                SWAP                     2
        L8:     FOR_ITER                10 (to L11)
                STORE_FAST_LOAD_FAST   119 (p, p)
        L9:     POP_JUMP_IF_NOT_NONE     3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD            8 (to L8)
       L10:     LOAD_FAST_BORROW         7 (p)
                LIST_APPEND              2
                JUMP_BACKWARD           12 (to L8)
       L11:     END_FOR
                POP_ITER
       L12:     STORE_FAST               8 (projected)
                STORE_FAST               7 (p)

 461            LOAD_GLOBAL              5 (_list_envelope + NULL)

 462            LOAD_CONST              15 ('ok')
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (bid, capped)

 463            LOAD_FAST_BORROW         8 (projected)
                LOAD_GLOBAL             33 (len + NULL)
                LOAD_FAST_BORROW         8 (projected)
                CALL                     1

 461            LOAD_CONST              16 (('status', 'brokerage_id', 'limit', 'rows', 'count'))
                CALL_KW                  5
       L13:     RETURN_VALUE

  --   L14:     SWAP                     2
                POP_TOP

 460            SWAP                     2
                STORE_FAST               7 (p)
                RERAISE                  0

  --   L15:     PUSH_EXC_INFO

 465            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       92 (to L20)
                NOT_TAKEN
                STORE_FAST               9 (e)

 466   L16:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 467            LOAD_CONST              17 ('brokerage_action_history read error type=')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 466            CALL                     1
                POP_TOP

 469            LOAD_GLOBAL              5 (_list_envelope + NULL)

 470            LOAD_CONST               5 ('skipped')
                LOAD_FAST_LOAD_FAST     35 (bid, capped)

 471            LOAD_CONST              18 ('db_read_failed:')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 472            LOAD_CONST               6 ('audit_store_unavailable')

 469            LOAD_CONST               7 (('status', 'brokerage_id', 'limit', 'warnings', 'error_code'))
                CALL_KW                  5
       L17:     SWAP                     2
       L18:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RETURN_VALUE

  --   L19:     LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 465   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L15 [0]
  L5 to L7 -> L15 [0]
  L7 to L9 -> L14 [2]
  L10 to L12 -> L14 [2]
  L12 to L13 -> L15 [0]
  L14 to L15 -> L15 [0]
  L15 to L16 -> L21 [1] lasti
  L16 to L17 -> L19 [1] lasti
  L17 to L18 -> L21 [1] lasti
  L19 to L21 -> L21 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C180C4360, file "app\services\operator\audit_service.py", line 460>:
 460           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (_project_row + NULL)
               LOAD_FAST_BORROW         1 (r)
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           18 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app\services\operator\audit_service.py", line 476>:
476           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('within_hours')

478           LOAD_CONST               2 ('int')

476           LOAD_CONST               3 ('limit')

479           LOAD_CONST               4 ('Any')

476           LOAD_CONST               5 ('return')

480           LOAD_CONST               6 ('Dict[str, Any]')

476           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object recent_failed_operator_actions at 0x0000018C17D513C0, file "app\services\operator\audit_service.py", line 476>:
 476            RESUME                   0

 483            NOP

 484    L1:     LOAD_GLOBAL              1 (int + NULL)
                LOAD_FAST_BORROW         0 (within_hours)
                CALL                     1
                STORE_FAST               2 (win)

 487    L2:     LOAD_FAST_BORROW         2 (win)
                LOAD_SMALL_INT           1
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN

 488            LOAD_SMALL_INT           1
                STORE_FAST               2 (win)

 489    L3:     LOAD_FAST_BORROW         2 (win)
                LOAD_CONST              18 (720)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN

 490            LOAD_CONST              18 (720)
                STORE_FAST               2 (win)

 491    L4:     LOAD_GLOBAL              7 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         1 (limit)
                CALL                     1
                STORE_FAST               3 (capped)

 492            LOAD_GLOBAL              9 (_iso + NULL)
                LOAD_GLOBAL             11 (_now_dt + NULL)
                CALL                     0
                LOAD_GLOBAL             13 (timedelta + NULL)
                LOAD_FAST_BORROW         2 (win)
                LOAD_CONST               1 (('hours',))
                CALL_KW                  1
                BINARY_OP               10 (-)
                CALL                     1
                STORE_FAST               4 (cutoff_iso)

 493            LOAD_GLOBAL             15 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               5 (db)

 494            LOAD_FAST_BORROW         5 (db)
                POP_JUMP_IF_NOT_NONE    17 (to L5)
                NOT_TAKEN

 495            LOAD_GLOBAL             17 (_list_envelope + NULL)

 496            LOAD_CONST               3 ('skipped')
                LOAD_FAST_BORROW         3 (capped)

 497            LOAD_CONST               4 ('audit_store_unavailable')
                BUILD_LIST               1

 498            LOAD_CONST               4 ('audit_store_unavailable')

 495            LOAD_CONST               5 (('status', 'limit', 'warnings', 'error_code'))
                CALL_KW                  4
                RETURN_VALUE

 500    L5:     NOP

 502    L6:     LOAD_FAST_BORROW         5 (db)
                LOAD_ATTR               19 (table + NULL|self)
                LOAD_GLOBAL             20 (_TABLE)
                CALL                     1

 503            LOAD_ATTR               23 (select + NULL|self)
                LOAD_CONST               6 (',')
                LOAD_ATTR               25 (join + NULL|self)
                LOAD_GLOBAL             26 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 504            LOAD_ATTR               29 (eq + NULL|self)
                LOAD_CONST               7 ('status')
                LOAD_CONST               8 ('FAILED')
                CALL                     2

 505            LOAD_ATTR               31 (gt + NULL|self)
                LOAD_CONST               9 ('occurred_at')
                LOAD_FAST_BORROW         4 (cutoff_iso)
                CALL                     2

 506            LOAD_ATTR               33 (order + NULL|self)
                LOAD_CONST               9 ('occurred_at')
                LOAD_CONST              10 (True)
                LOAD_CONST              11 (('desc',))
                CALL_KW                  2

 507            LOAD_ATTR               35 (limit + NULL|self)
                LOAD_FAST_BORROW         3 (capped)
                CALL                     1

 508            LOAD_ATTR               37 (execute + NULL|self)
                CALL                     0

 501            STORE_FAST               6 (result)

 510            LOAD_GLOBAL             39 (list + NULL)
                LOAD_GLOBAL             41 (getattr + NULL)
                LOAD_FAST_BORROW         6 (result)
                LOAD_CONST              12 ('data')
                LOAD_CONST               2 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
        L7:     NOT_TAKEN
        L8:     POP_TOP
                BUILD_LIST               0
        L9:     CALL                     1
                STORE_FAST               7 (rows)

 511            LOAD_CONST              13 (<code object <genexpr> at 0x0000018C180C4030, file "app\services\operator\audit_service.py", line 511>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         7 (rows)
                GET_ITER
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      8 (p)
                SWAP                     2
       L10:     BUILD_LIST               0
                SWAP                     2
       L11:     FOR_ITER                10 (to L14)
                STORE_FAST_LOAD_FAST   136 (p, p)
       L12:     POP_JUMP_IF_NOT_NONE     3 (to L13)
                NOT_TAKEN
                JUMP_BACKWARD            8 (to L11)
       L13:     LOAD_FAST_BORROW         8 (p)
                LIST_APPEND              2
                JUMP_BACKWARD           12 (to L11)
       L14:     END_FOR
                POP_ITER
       L15:     STORE_FAST               9 (projected)
                STORE_FAST               8 (p)

 512            LOAD_GLOBAL             17 (_list_envelope + NULL)

 513            LOAD_CONST              14 ('ok')
                LOAD_FAST_BORROW         9 (projected)
                LOAD_GLOBAL             43 (len + NULL)
                LOAD_FAST_BORROW         9 (projected)
                CALL                     1

 514            LOAD_FAST_BORROW         3 (capped)

 512            LOAD_CONST              15 (('status', 'rows', 'count', 'limit'))
                CALL_KW                  4
       L16:     RETURN_VALUE

  --   L17:     PUSH_EXC_INFO

 485            LOAD_GLOBAL              2 (TypeError)
                LOAD_GLOBAL              4 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        7 (to L19)
                NOT_TAKEN
                POP_TOP

 486            LOAD_SMALL_INT          24
                STORE_FAST               2 (win)
       L18:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 336 (to L2)

 485   L19:     RERAISE                  0

  --   L20:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L21:     SWAP                     2
                POP_TOP

 511            SWAP                     2
                STORE_FAST               8 (p)
                RERAISE                  0

  --   L22:     PUSH_EXC_INFO

 516            LOAD_GLOBAL             44 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       92 (to L27)
                NOT_TAKEN
                STORE_FAST              10 (e)

 517   L23:     LOAD_GLOBAL             46 (logger)
                LOAD_ATTR               49 (warning + NULL|self)

 518            LOAD_CONST              16 ('recent_failed_operator_actions read error type=')

 519            LOAD_GLOBAL             51 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               52 (__name__)
                FORMAT_SIMPLE

 518            BUILD_STRING             2

 517            CALL                     1
                POP_TOP

 521            LOAD_GLOBAL             17 (_list_envelope + NULL)

 522            LOAD_CONST               3 ('skipped')
                LOAD_FAST                3 (capped)

 523            LOAD_CONST              17 ('db_read_failed:')
                LOAD_GLOBAL             51 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               52 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 524            LOAD_CONST               4 ('audit_store_unavailable')

 521            LOAD_CONST               5 (('status', 'limit', 'warnings', 'error_code'))
                CALL_KW                  4
       L24:     SWAP                     2
       L25:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RETURN_VALUE

  --   L26:     LOAD_CONST               2 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 516   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L17 [0]
  L6 to L7 -> L22 [0]
  L8 to L10 -> L22 [0]
  L10 to L12 -> L21 [2]
  L13 to L15 -> L21 [2]
  L15 to L16 -> L22 [0]
  L17 to L18 -> L20 [1] lasti
  L19 to L20 -> L20 [1] lasti
  L21 to L22 -> L22 [0]
  L22 to L23 -> L28 [1] lasti
  L23 to L24 -> L26 [1] lasti
  L24 to L25 -> L28 [1] lasti
  L26 to L28 -> L28 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C180C4030, file "app\services\operator\audit_service.py", line 511>:
 511           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (_project_row + NULL)
               LOAD_FAST_BORROW         1 (r)
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           18 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti
```
