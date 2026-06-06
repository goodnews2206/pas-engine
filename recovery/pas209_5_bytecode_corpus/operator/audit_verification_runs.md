# operator/audit_verification_runs

- **pyc:** `app\services\operator\__pycache__\audit_verification_runs.cpython-314.pyc`
- **expected source path (absent):** `app\services\operator/audit_verification_runs.py`
- **co_filename (from bytecode):** `app/services/operator/audit_verification_runs.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** operator

## Module docstring

```
PAS178 — Durable audit verification run persistence.

Append-only durable record of operator-driven audit
verification runs. Mirrors PAS176/PAS177's append-only
doctrine: SELECT + INSERT only, no UPDATE/DELETE.

Doctrine carried by every helper:

* **Append-only.** Insert + read only. No update / delete.
* **Closed enums.** Mirror v27 CHECK constraints.
* **No PII.** Metadata projected against closed allow-list;
  bounded actor_id + error_code.
* **NEVER raises.** DB unavailable → ``status="skipped"``.
* **Bounded pagination.** Hard caps in the read helpers.

Public surface:

  * ``build_verification_run_record(...)`` — pure helper.
  * ``persist_verification_run(...)`` — append-only insert.
  * ``list_verification_runs(...)`` — bounded read.
  * ``verification_run_summary(...)`` — count by status / type.
  * ``latest_verification_status_for_brokerage(...)`` — fast badge.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `datetime`, `get_supabase`, `logging`, `timezone`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_bound_actor_id`, `_bound_brokerage_id`, `_bound_error_code`, `_clamp_limit`, `_get_db_safe`, `_iso`, `_nonneg_int`, `_now_dt`, `_project_metadata`, `_project_row`, `build_verification_run_record`, `latest_verification_status_for_brokerage`, `list_verification_runs`, `persist_verification_run`, `verification_run_summary`

## Env-key candidates

`NONE`, `OPERATOR`

## String constants (redacted where noted)

- '\nPAS178 — Durable audit verification run persistence.\n\nAppend-only durable record of operator-driven audit\nverification runs. Mirrors PAS176/PAS177\'s append-only\ndoctrine: SELECT + INSERT only, no UPDATE/DELETE.\n\nDoctrine carried by every helper:\n\n* **Append-only.** Insert + read only. No update / delete.\n* **Closed enums.** Mirror v27 CHECK constraints.\n* **No PII.** Metadata projected against closed allow-list;\n  bounded actor_id + error_code.\n* **NEVER raises.** DB unavailable → ``status="skipped"``.\n* **Bounded pagination.** Hard caps in the read helpers.\n\nPublic surface:\n\n  * ``build_verification_run_record(...)`` — pure helper.\n  * ``persist_verification_run(...)`` — append-only insert.\n  * ``list_verification_runs(...)`` — bounded read.\n  * ``verification_run_summary(...)`` — count by status / type.\n  * ``latest_verification_status_for_brokerage(...)`` — fast badge.\n'
- 'pas.operator.audit_verification_runs'
- 'pas_audit_verification_runs'
- 'OPERATOR'
- 🔒 '<REDACTED:high-entropy blob, len=64>'
- 'brokerage_id'
- 'completed_at'
- 'verification_type'
- 'checked_window_count'
- 'checked_audit_row_count'
- 'broken_chain_count'
- 'warning_count'
- 'error_code'
- 'generated_by_actor_type'
- 'generated_by_actor_id'
- 'metadata'
- 'limit'
- 'now'
- 'Any'
- 'return'
- 'datetime'
- 'str'
- 'seconds'
- 'audit_verification_runs db client unavailable type='
- 'value'
- 'Optional[str]'
- 'int'
- 'Dict[str, Any]'
- 'row'
- 'Optional[Dict[str, Any]]'
- 'status'
- 'started_at'
- 'Build a structural verification-run record without\npersisting. Returns a closed-shape envelope. NEVER raises.'
- 'failed'
- 'record'
- 'invalid_verification_type'
- 'warnings'
- 'invalid_run_status'
- 'invalid_actor_type'
- 'invalid_brokerage_id'
- 'invalid_actor_id'
- 'invalid_error_code'
- 'verification_run_id'
- 'Insert a verification-run record into the v27 table.\nNEVER raises. NEVER returns PII.'
- 'run_row'
- 'invalid_record'
- 'skipped'
- 'audit_verification_runs_unavailable'
- 'data'
- 'persist_verification_run db error type='
- 'db_write_failed:'
- 'Bounded read of verification runs. NEVER raises.'
- 'rows'
- 'count'
- 'list_verification_runs read error type='
- 'db_read_failed:'
- 'Summary: counts by status and verification_type, plus\nlatest run snapshot. NEVER raises. NEVER returns PII.'
- 'total'
- 'by_status'
- 'by_type'
- 'latest_run'
- 'verification_run_summary read error type='
- "Compact badge for the operator console. Returns the\nmost-recent run's status + started_at. NEVER raises."
- 'latest_status'
- 'NONE'
- 'missing_brokerage_id'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS178 — Durable audit verification run persistence.\n\nAppend-only durable record of operator-driven audit\nverification runs. Mirrors PAS176/PAS177\'s append-only\ndoctrine: SELECT + INSERT only, no UPDATE/DELETE.\n\nDoctrine carried by every helper:\n\n* **Append-only.** Insert + read only. No update / delete.\n* **Closed enums.** Mirror v27 CHECK constraints.\n* **No PII.** Metadata projected against closed allow-list;\n  bounded actor_id + error_code.\n* **NEVER raises.** DB unavailable → ``status="skipped"``.\n* **Bounded pagination.** Hard caps in the read helpers.\n\nPublic surface:\n\n  * ``build_verification_run_record(...)`` — pure helper.\n  * ``persist_verification_run(...)`` — append-only insert.\n  * ``list_verification_runs(...)`` — bounded read.\n  * ``verification_run_summary(...)`` — count by status / type.\n  * ``latest_verification_status_for_brokerage(...)`` — fast badge.\n')
              STORE_NAME               0 (__doc__)

 26           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 28           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 29           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (uuid)
              STORE_NAME               4 (uuid)

 30           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timezone'))
              IMPORT_NAME              5 (datetime)
              IMPORT_FROM              5 (datetime)
              STORE_NAME               5 (datetime)
              IMPORT_FROM              6 (timezone)
              STORE_NAME               6 (timezone)
              POP_TOP

 31           LOAD_SMALL_INT           0
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

 34           LOAD_NAME                3 (logging)
              LOAD_ATTR               24 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.operator.audit_verification_runs')
              CALL                     1
              STORE_NAME              13 (logger)

 37           LOAD_CONST               6 ('pas_audit_verification_runs')
              STORE_NAME              14 (_TABLE)

 40           LOAD_CONST              51 (('AUDIT_ROW_HASH_CHAIN', 'MERKLE_WINDOW', 'CROSS_WINDOW_CHAIN', 'FULL_AUDIT_INTEGRITY'))
              STORE_NAME              15 (ALLOWED_VERIFICATION_TYPES)

 47           LOAD_CONST              52 (('PASSED', 'FAILED', 'SKIPPED', 'PARTIAL'))
              STORE_NAME              16 (ALLOWED_RUN_STATUSES)

 51           LOAD_CONST              53 (('OPERATOR', 'ADMIN', 'SYSTEM'))
              STORE_NAME              17 (ALLOWED_ACTOR_TYPES)

 54           LOAD_CONST              54 (('event', 'chain_status', 'merkle_root_count', 'window_count', 'operator_command'))
              STORE_NAME              18 (ALLOWED_METADATA_KEYS)

 62           LOAD_SMALL_INT         200
              STORE_NAME              19 (_BROKERAGE_ID_MAX_LEN)

 63           LOAD_SMALL_INT         200
              STORE_NAME              20 (_ACTOR_ID_MAX_LEN)

 64           LOAD_SMALL_INT         200
              STORE_NAME              21 (_ERROR_CODE_MAX_LEN)

 65           LOAD_CONST               8 (5000)
              STORE_NAME              22 (_LIST_HARD_CAP)

 66           LOAD_SMALL_INT          50
              STORE_NAME              23 (_DEFAULT_LIMIT)

 69           LOAD_CONST               9 ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_')

 68           STORE_NAME              24 (_ALLOWED_TOKEN_CHARS)

 74           LOAD_CONST              55 (('verification_run_id', 'brokerage_id', 'started_at', 'completed_at', 'verification_type', 'status', 'checked_window_count', 'checked_audit_row_count', 'broken_chain_count', 'warning_count', 'error_code', 'generated_by_actor_type', 'generated_by_actor_id', 'metadata'))
              STORE_NAME              25 (_STRUCTURAL_COLUMNS)

 96           LOAD_CONST              56 ((None,))
              LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA2E20, file "app/services/operator/audit_verification_runs.py", line 96>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _now_dt at 0x0000018C179C3A50, file "app/services/operator/audit_verification_runs.py", line 96>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              26 (_now_dt)

104           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA3960, file "app/services/operator/audit_verification_runs.py", line 104>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object _iso at 0x0000018C18025130, file "app/services/operator/audit_verification_runs.py", line 104>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_iso)

108           LOAD_CONST              25 (<code object _get_db_safe at 0x0000018C17FF1230, file "app/services/operator/audit_verification_runs.py", line 108>)
              MAKE_FUNCTION
              STORE_NAME              28 (_get_db_safe)

120           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA1D40, file "app/services/operator/audit_verification_runs.py", line 120>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object _bound_brokerage_id at 0x0000018C17F95E60, file "app/services/operator/audit_verification_runs.py", line 120>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_bound_brokerage_id)

129           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3870, file "app/services/operator/audit_verification_runs.py", line 129>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object _bound_actor_id at 0x0000018C179C3E10, file "app/services/operator/audit_verification_runs.py", line 129>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_bound_actor_id)

140           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA3690, file "app/services/operator/audit_verification_runs.py", line 140>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object _bound_error_code at 0x0000018C17F95CF0, file "app/services/operator/audit_verification_runs.py", line 140>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_bound_error_code)

151           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA2A60, file "app/services/operator/audit_verification_runs.py", line 151>)
              MAKE_FUNCTION
              LOAD_CONST              33 (<code object _nonneg_int at 0x0000018C1802C880, file "app/services/operator/audit_verification_runs.py", line 151>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_nonneg_int)

159           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA3780, file "app/services/operator/audit_verification_runs.py", line 159>)
              MAKE_FUNCTION
              LOAD_CONST              35 (<code object _project_metadata at 0x0000018C17FEE230, file "app/services/operator/audit_verification_runs.py", line 159>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_project_metadata)

174           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA3B40, file "app/services/operator/audit_verification_runs.py", line 174>)
              MAKE_FUNCTION
              LOAD_CONST              37 (<code object _project_row at 0x0000018C1804C9F0, file "app/services/operator/audit_verification_runs.py", line 174>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              34 (_project_row)

185           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA3C30, file "app/services/operator/audit_verification_runs.py", line 185>)
              MAKE_FUNCTION
              LOAD_CONST              39 (<code object _clamp_limit at 0x0000018C17972D90, file "app/services/operator/audit_verification_runs.py", line 185>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              35 (_clamp_limit)

201           LOAD_CONST              11 ('completed_at')

207           LOAD_CONST               2 (None)

201           LOAD_CONST              13 ('checked_window_count')

208           LOAD_SMALL_INT           0

201           LOAD_CONST              14 ('checked_audit_row_count')

209           LOAD_SMALL_INT           0

201           LOAD_CONST              15 ('broken_chain_count')

210           LOAD_SMALL_INT           0

201           LOAD_CONST              16 ('warning_count')

211           LOAD_SMALL_INT           0

201           LOAD_CONST              17 ('error_code')

212           LOAD_CONST               2 (None)

201           LOAD_CONST              18 ('generated_by_actor_type')

213           LOAD_CONST               7 ('OPERATOR')

201           LOAD_CONST              19 ('generated_by_actor_id')

214           LOAD_CONST               2 (None)

201           LOAD_CONST              20 ('metadata')

215           LOAD_CONST               2 (None)

201           BUILD_MAP                9
              LOAD_CONST              40 (<code object __annotate__ at 0x0000018C18053630, file "app/services/operator/audit_verification_runs.py", line 201>)
              MAKE_FUNCTION
              LOAD_CONST              41 (<code object build_verification_run_record at 0x0000018C181A17D0, file "app/services/operator/audit_verification_runs.py", line 201>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              36 (build_verification_run_record)

300           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA3A50, file "app/services/operator/audit_verification_runs.py", line 300>)
              MAKE_FUNCTION
              LOAD_CONST              43 (<code object persist_verification_run at 0x0000018C17D7D580, file "app/services/operator/audit_verification_runs.py", line 300>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              37 (persist_verification_run)

350           LOAD_CONST              10 ('brokerage_id')

352           LOAD_CONST               2 (None)

350           LOAD_CONST              12 ('verification_type')

353           LOAD_CONST               2 (None)

350           LOAD_CONST              44 ('limit')

354           LOAD_NAME               23 (_DEFAULT_LIMIT)

350           BUILD_MAP                3
              LOAD_CONST              45 (<code object __annotate__ at 0x0000018C18025230, file "app/services/operator/audit_verification_runs.py", line 350>)
              MAKE_FUNCTION
              LOAD_CONST              46 (<code object list_verification_runs at 0x0000018C181A22B0, file "app/services/operator/audit_verification_runs.py", line 350>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              38 (list_verification_runs)

422           LOAD_CONST              10 ('brokerage_id')

424           LOAD_CONST               2 (None)

422           BUILD_MAP                1
              LOAD_CONST              47 (<code object __annotate__ at 0x0000018C17FA1E30, file "app/services/operator/audit_verification_runs.py", line 422>)
              MAKE_FUNCTION
              LOAD_CONST              48 (<code object verification_run_summary at 0x0000018C17E8AB60, file "app/services/operator/audit_verification_runs.py", line 422>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              39 (verification_run_summary)

490           LOAD_CONST              49 (<code object __annotate__ at 0x0000018C17FA3000, file "app/services/operator/audit_verification_runs.py", line 490>)
              MAKE_FUNCTION
              LOAD_CONST              50 (<code object latest_verification_status_for_brokerage at 0x0000018C17D6DFC0, file "app/services/operator/audit_verification_runs.py", line 490>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              40 (latest_verification_status_for_brokerage)

527           BUILD_LIST               0
              LOAD_CONST              57 (('ALLOWED_VERIFICATION_TYPES', 'ALLOWED_RUN_STATUSES', 'ALLOWED_ACTOR_TYPES', 'ALLOWED_METADATA_KEYS', 'build_verification_run_record', 'persist_verification_run', 'list_verification_runs', 'verification_run_summary', 'latest_verification_status_for_brokerage'))
              LIST_EXTEND              1
              STORE_NAME              41 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app/services/operator/audit_verification_runs.py", line 96>:
 96           RESUME                   0
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

Disassembly of <code object _now_dt at 0x0000018C179C3A50, file "app/services/operator/audit_verification_runs.py", line 96>:
 96           RESUME                   0

 97           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (now)
              LOAD_GLOBAL              2 (datetime)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       78 (to L2)
              NOT_TAKEN

 98           LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR                4 (tzinfo)
              POP_JUMP_IF_NOT_NONE    33 (to L1)
              NOT_TAKEN

 99           LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR                7 (replace + NULL|self)
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              LOAD_CONST               1 (('tzinfo',))
              CALL_KW                  1
              RETURN_VALUE

100   L1:     LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR               13 (astimezone + NULL|self)
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              CALL                     1
              RETURN_VALUE

101   L2:     LOAD_GLOBAL              2 (datetime)
              LOAD_ATTR               14 (now)
              PUSH_NULL
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app/services/operator/audit_verification_runs.py", line 104>:
104           RESUME                   0
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

Disassembly of <code object _iso at 0x0000018C18025130, file "app/services/operator/audit_verification_runs.py", line 104>:
104           RESUME                   0

105           LOAD_FAST_BORROW         0 (dt)
              LOAD_ATTR                1 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object _get_db_safe at 0x0000018C17FF1230, file "app/services/operator/audit_verification_runs.py", line 108>:
 108           RESUME                   0

 109           NOP

 110   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 111           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 112           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 113   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 114           LOAD_CONST               2 ('audit_verification_runs db client unavailable type=')

 115           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 114           BUILD_STRING             2

 113           CALL                     1
               POP_TOP

 117   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 112   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "app/services/operator/audit_verification_runs.py", line 120>:
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

Disassembly of <code object _bound_brokerage_id at 0x0000018C17F95E60, file "app/services/operator/audit_verification_runs.py", line 120>:
120           RESUME                   0

121           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

122           LOAD_CONST               0 (None)
              RETURN_VALUE

123   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

124           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_BROKERAGE_ID_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

125   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

126   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app/services/operator/audit_verification_runs.py", line 129>:
129           RESUME                   0
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

Disassembly of <code object _bound_actor_id at 0x0000018C179C3E10, file "app/services/operator/audit_verification_runs.py", line 129>:
129           RESUME                   0

130           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

131           LOAD_CONST               0 (None)
              RETURN_VALUE

132   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

133           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_ACTOR_ID_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

134   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

135   L3:     LOAD_GLOBAL             10 (any)
              COPY                     1
              LOAD_COMMON_CONSTANT     4 (<built-in function any>)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE       28 (to L7)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 (<code object <genexpr> at 0x0000018C180C4470, file "app/services/operator/audit_verification_runs.py", line 135>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (s)
              GET_ITER
              CALL                     0
      L4:     FOR_ITER                12 (to L6)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L4)
      L5:     POP_ITER
              LOAD_CONST               2 (True)
              JUMP_FORWARD            17 (to L8)
      L6:     END_FOR
              POP_ITER
              LOAD_CONST               3 (False)
              JUMP_FORWARD            13 (to L8)
      L7:     PUSH_NULL
              LOAD_CONST               1 (<code object <genexpr> at 0x0000018C180C4470, file "app/services/operator/audit_verification_runs.py", line 135>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (s)
              GET_ITER
              CALL                     0
              CALL                     1
      L8:     TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L9)
              NOT_TAKEN

136           LOAD_CONST               0 (None)
              RETURN_VALUE

137   L9:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180C4470, file "app/services/operator/audit_verification_runs.py", line 135>:
 135           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                13 (to L3)
               STORE_FAST_LOAD_FAST    17 (ch, ch)
               LOAD_GLOBAL              0 (_ALLOWED_TOKEN_CHARS)
               CONTAINS_OP              1 (not in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           15 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app/services/operator/audit_verification_runs.py", line 140>:
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

Disassembly of <code object _bound_error_code at 0x0000018C17F95CF0, file "app/services/operator/audit_verification_runs.py", line 140>:
140           RESUME                   0

141           LOAD_FAST_BORROW         0 (value)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

142           LOAD_CONST               0 (None)
              RETURN_VALUE

143   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

144           LOAD_CONST               0 (None)
              RETURN_VALUE

145   L2:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

146           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L3)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_ERROR_CODE_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN

147   L3:     LOAD_CONST               0 (None)
              RETURN_VALUE

148   L4:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app/services/operator/audit_verification_runs.py", line 151>:
151           RESUME                   0
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

Disassembly of <code object _nonneg_int at 0x0000018C1802C880, file "app/services/operator/audit_verification_runs.py", line 151>:
 151           RESUME                   0

 152           NOP

 153   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (v)

 154           LOAD_FAST_BORROW         1 (v)
               LOAD_SMALL_INT           0
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_FAST_BORROW         1 (v)
       L2:     RETURN_VALUE
       L3:     LOAD_SMALL_INT           0
       L4:     RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 155           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L7)
               NOT_TAKEN
               POP_TOP

 156   L6:     POP_EXCEPT
               LOAD_SMALL_INT           0
               RETURN_VALUE

 155   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L3 to L4 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app/services/operator/audit_verification_runs.py", line 159>:
159           RESUME                   0
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

Disassembly of <code object _project_metadata at 0x0000018C17FEE230, file "app/services/operator/audit_verification_runs.py", line 159>:
159           RESUME                   0

160           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (metadata)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

161           BUILD_MAP                0
              RETURN_VALUE

162   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

163           LOAD_GLOBAL              4 (ALLOWED_METADATA_KEYS)
              GET_ITER
      L2:     FOR_ITER               108 (to L8)
              STORE_FAST               2 (k)

164           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, metadata)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

165           JUMP_BACKWARD           11 (to L2)

166   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (metadata, k)
              BINARY_OP               26 ([])
              STORE_FAST               3 (v)

167           LOAD_FAST_BORROW         3 (v)
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

168   L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD           62 (to L2)

169   L5:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (v)
              LOAD_GLOBAL             12 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              JUMP_BACKWARD           86 (to L2)
      L6:     LOAD_GLOBAL             15 (len + NULL)
              LOAD_FAST_BORROW         3 (v)
              CALL                     1
              LOAD_SMALL_INT         200
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_TRUE         3 (to L7)
              NOT_TAKEN
              JUMP_BACKWARD          104 (to L2)

170   L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD          110 (to L2)

163   L8:     END_FOR
              POP_ITER

171           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app/services/operator/audit_verification_runs.py", line 174>:
174           RESUME                   0
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

Disassembly of <code object _project_row at 0x0000018C1804C9F0, file "app/services/operator/audit_verification_runs.py", line 174>:
174           RESUME                   0

175           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

176           LOAD_CONST               0 (None)
              RETURN_VALUE

177   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

178           LOAD_GLOBAL              4 (_STRUCTURAL_COLUMNS)
              GET_ITER
      L2:     FOR_ITER                21 (to L4)
              STORE_FAST               2 (col)

179           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (col, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

180   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, col)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, col)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L2)

178   L4:     END_FOR
              POP_ITER

181           LOAD_GLOBAL              7 (_project_metadata + NULL)
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

182           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app/services/operator/audit_verification_runs.py", line 185>:
185           RESUME                   0
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

Disassembly of <code object _clamp_limit at 0x0000018C17972D90, file "app/services/operator/audit_verification_runs.py", line 185>:
 185           RESUME                   0

 186           NOP

 187   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (v)

 190   L2:     LOAD_FAST                1 (v)
               LOAD_SMALL_INT           1
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 191           LOAD_SMALL_INT           1
               RETURN_VALUE

 192   L3:     LOAD_FAST                1 (v)
               LOAD_GLOBAL              8 (_LIST_HARD_CAP)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 193           LOAD_GLOBAL              8 (_LIST_HARD_CAP)
               RETURN_VALUE

 194   L4:     LOAD_FAST                1 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 188           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

 189           LOAD_GLOBAL              6 (_DEFAULT_LIMIT)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 188   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18053630, file "app/services/operator/audit_verification_runs.py", line 201>:
201           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

203           LOAD_CONST               2 ('Optional[str]')

201           LOAD_CONST               3 ('verification_type')

204           LOAD_CONST               4 ('str')

201           LOAD_CONST               5 ('status')

205           LOAD_CONST               4 ('str')

201           LOAD_CONST               6 ('started_at')

206           LOAD_CONST               7 ('Any')

201           LOAD_CONST               8 ('completed_at')

207           LOAD_CONST               7 ('Any')

201           LOAD_CONST               9 ('checked_window_count')

208           LOAD_CONST               7 ('Any')

201           LOAD_CONST              10 ('checked_audit_row_count')

209           LOAD_CONST               7 ('Any')

201           LOAD_CONST              11 ('broken_chain_count')

210           LOAD_CONST               7 ('Any')

201           LOAD_CONST              12 ('warning_count')

211           LOAD_CONST               7 ('Any')

201           LOAD_CONST              13 ('error_code')

212           LOAD_CONST               2 ('Optional[str]')

201           LOAD_CONST              14 ('generated_by_actor_type')

213           LOAD_CONST               4 ('str')

201           LOAD_CONST              15 ('generated_by_actor_id')

214           LOAD_CONST               2 ('Optional[str]')

201           LOAD_CONST              16 ('metadata')

215           LOAD_CONST              17 ('Optional[Dict[str, Any]]')

201           LOAD_CONST              18 ('return')

216           LOAD_CONST              19 ('Dict[str, Any]')

201           BUILD_MAP               14
              RETURN_VALUE

Disassembly of <code object build_verification_run_record at 0x0000018C181A17D0, file "app/services/operator/audit_verification_runs.py", line 201>:
201            RESUME                   0

219            LOAD_FAST_BORROW         1 (verification_type)
               LOAD_GLOBAL              0 (ALLOWED_VERIFICATION_TYPES)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       11 (to L1)
               NOT_TAKEN

221            LOAD_CONST               1 ('status')
               LOAD_CONST               2 ('failed')

222            LOAD_CONST               3 ('record')
               LOAD_CONST               4 (None)

223            LOAD_CONST               5 ('error_code')
               LOAD_CONST               6 ('invalid_verification_type')

224            LOAD_CONST               7 ('warnings')
               BUILD_LIST               0

220            BUILD_MAP                4
               RETURN_VALUE

226    L1:     LOAD_FAST_BORROW         2 (status)
               LOAD_GLOBAL              2 (ALLOWED_RUN_STATUSES)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       11 (to L2)
               NOT_TAKEN

228            LOAD_CONST               1 ('status')
               LOAD_CONST               2 ('failed')

229            LOAD_CONST               3 ('record')
               LOAD_CONST               4 (None)

230            LOAD_CONST               5 ('error_code')
               LOAD_CONST               8 ('invalid_run_status')

231            LOAD_CONST               7 ('warnings')
               BUILD_LIST               0

227            BUILD_MAP                4
               RETURN_VALUE

233    L2:     LOAD_FAST_BORROW        10 (generated_by_actor_type)
               LOAD_GLOBAL              4 (ALLOWED_ACTOR_TYPES)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       11 (to L3)
               NOT_TAKEN

235            LOAD_CONST               1 ('status')
               LOAD_CONST               2 ('failed')

236            LOAD_CONST               3 ('record')
               LOAD_CONST               4 (None)

237            LOAD_CONST               5 ('error_code')
               LOAD_CONST               9 ('invalid_actor_type')

238            LOAD_CONST               7 ('warnings')
               BUILD_LIST               0

234            BUILD_MAP                4
               RETURN_VALUE

240    L3:     LOAD_FAST_BORROW         0 (brokerage_id)
               POP_JUMP_IF_NONE        12 (to L4)
               NOT_TAKEN
               LOAD_GLOBAL              7 (_bound_brokerage_id + NULL)
               LOAD_FAST_BORROW         0 (brokerage_id)
               CALL                     1
               JUMP_FORWARD             1 (to L5)
       L4:     LOAD_CONST               4 (None)
       L5:     STORE_FAST              13 (bid)

241            LOAD_FAST_BORROW         0 (brokerage_id)
               POP_JUMP_IF_NONE        15 (to L6)
               NOT_TAKEN
               LOAD_FAST_BORROW        13 (bid)
               POP_JUMP_IF_NOT_NONE    11 (to L6)
               NOT_TAKEN

243            LOAD_CONST               1 ('status')
               LOAD_CONST               2 ('failed')

244            LOAD_CONST               3 ('record')
               LOAD_CONST               4 (None)

245            LOAD_CONST               5 ('error_code')
               LOAD_CONST              10 ('invalid_brokerage_id')

246            LOAD_CONST               7 ('warnings')
               BUILD_LIST               0

242            BUILD_MAP                4
               RETURN_VALUE

248    L6:     LOAD_FAST_BORROW        11 (generated_by_actor_id)
               POP_JUMP_IF_NONE        12 (to L7)
               NOT_TAKEN
               LOAD_GLOBAL              9 (_bound_actor_id + NULL)
               LOAD_FAST_BORROW        11 (generated_by_actor_id)
               CALL                     1
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 (None)
       L8:     STORE_FAST              14 (actor)

249            LOAD_FAST_BORROW        11 (generated_by_actor_id)
               POP_JUMP_IF_NONE        15 (to L9)
               NOT_TAKEN
               LOAD_FAST_BORROW        14 (actor)
               POP_JUMP_IF_NOT_NONE    11 (to L9)
               NOT_TAKEN

251            LOAD_CONST               1 ('status')
               LOAD_CONST               2 ('failed')

252            LOAD_CONST               3 ('record')
               LOAD_CONST               4 (None)

253            LOAD_CONST               5 ('error_code')
               LOAD_CONST              11 ('invalid_actor_id')

254            LOAD_CONST               7 ('warnings')
               BUILD_LIST               0

250            BUILD_MAP                4
               RETURN_VALUE

256    L9:     LOAD_GLOBAL             11 (_bound_error_code + NULL)
               LOAD_FAST_BORROW         9 (error_code)
               CALL                     1
               STORE_FAST              15 (err)

257            LOAD_FAST_BORROW         9 (error_code)
               POP_JUMP_IF_NONE        15 (to L10)
               NOT_TAKEN
               LOAD_FAST_BORROW        15 (err)
               POP_JUMP_IF_NOT_NONE    11 (to L10)
               NOT_TAKEN

259            LOAD_CONST               1 ('status')
               LOAD_CONST               2 ('failed')

260            LOAD_CONST               3 ('record')
               LOAD_CONST               4 (None)

261            LOAD_CONST               5 ('error_code')
               LOAD_CONST              12 ('invalid_error_code')

262            LOAD_CONST               7 ('warnings')
               BUILD_LIST               0

258            BUILD_MAP                4
               RETURN_VALUE

265   L10:     LOAD_GLOBAL             13 (isinstance + NULL)
               LOAD_FAST_BORROW         3 (started_at)
               LOAD_GLOBAL             14 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_FAST                3 (started_at)
               JUMP_FORWARD            19 (to L12)

266   L11:     LOAD_GLOBAL             17 (_iso + NULL)
               LOAD_GLOBAL             19 (_now_dt + NULL)
               LOAD_FAST_BORROW         3 (started_at)
               CALL                     1
               CALL                     1

264   L12:     STORE_FAST              16 (started_iso)

269            LOAD_GLOBAL             13 (isinstance + NULL)
               LOAD_FAST_BORROW         4 (completed_at)
               LOAD_GLOBAL             14 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_FAST                4 (completed_at)
               JUMP_FORWARD            25 (to L15)

270   L13:     LOAD_FAST_BORROW         4 (completed_at)
               POP_JUMP_IF_NONE        21 (to L14)
               NOT_TAKEN
               LOAD_GLOBAL             17 (_iso + NULL)
               LOAD_GLOBAL             19 (_now_dt + NULL)
               LOAD_FAST_BORROW         4 (completed_at)
               CALL                     1
               CALL                     1
               JUMP_FORWARD             1 (to L15)
      L14:     LOAD_CONST               4 (None)

268   L15:     STORE_FAST              17 (completed_iso)

273            LOAD_CONST              13 ('verification_run_id')
               LOAD_GLOBAL             15 (str + NULL)
               LOAD_GLOBAL             20 (uuid)
               LOAD_ATTR               22 (uuid4)
               PUSH_NULL
               CALL                     0
               CALL                     1

274            LOAD_CONST              14 ('brokerage_id')
               LOAD_FAST_BORROW        13 (bid)

275            LOAD_CONST              15 ('started_at')
               LOAD_FAST_BORROW        16 (started_iso)

276            LOAD_CONST              16 ('completed_at')
               LOAD_FAST_BORROW        17 (completed_iso)

277            LOAD_CONST              17 ('verification_type')
               LOAD_FAST_BORROW         1 (verification_type)

278            LOAD_CONST               1 ('status')
               LOAD_FAST_BORROW         2 (status)

279            LOAD_CONST              18 ('checked_window_count')
               LOAD_GLOBAL             25 (_nonneg_int + NULL)
               LOAD_FAST_BORROW         5 (checked_window_count)
               CALL                     1

280            LOAD_CONST              19 ('checked_audit_row_count')
               LOAD_GLOBAL             25 (_nonneg_int + NULL)
               LOAD_FAST_BORROW         6 (checked_audit_row_count)
               CALL                     1

281            LOAD_CONST              20 ('broken_chain_count')
               LOAD_GLOBAL             25 (_nonneg_int + NULL)
               LOAD_FAST_BORROW         7 (broken_chain_count)
               CALL                     1

282            LOAD_CONST              21 ('warning_count')
               LOAD_GLOBAL             25 (_nonneg_int + NULL)
               LOAD_FAST_BORROW         8 (warning_count)
               CALL                     1

283            LOAD_CONST               5 ('error_code')
               LOAD_FAST_BORROW        15 (err)

284            LOAD_CONST              22 ('generated_by_actor_type')
               LOAD_FAST_BORROW        10 (generated_by_actor_type)

285            LOAD_CONST              23 ('generated_by_actor_id')
               LOAD_FAST_BORROW        14 (actor)

286            LOAD_CONST              24 ('metadata')
               LOAD_GLOBAL             27 (_project_metadata + NULL)
               LOAD_FAST_BORROW        12 (metadata)
               CALL                     1

272            BUILD_MAP               14
               STORE_FAST              18 (record)

289            LOAD_CONST               1 ('status')
               LOAD_CONST              25 ('ok')

290            LOAD_CONST               3 ('record')
               LOAD_FAST_BORROW        18 (record)

291            LOAD_CONST               7 ('warnings')
               BUILD_LIST               0

292            LOAD_CONST               5 ('error_code')
               LOAD_CONST               4 (None)

288            BUILD_MAP                4
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app/services/operator/audit_verification_runs.py", line 300>:
300           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record')

301           LOAD_CONST               2 ('Any')

300           LOAD_CONST               3 ('return')

302           LOAD_CONST               4 ('Dict[str, Any]')

300           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object persist_verification_run at 0x0000018C17D7D580, file "app/services/operator/audit_verification_runs.py", line 300>:
 300            RESUME                   0

 305            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (record)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L1)
                NOT_TAKEN

 307            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 308            LOAD_CONST               3 ('run_row')
                LOAD_CONST               4 (None)

 309            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 310            LOAD_CONST               6 ('error_code')
                LOAD_CONST               7 ('invalid_record')

 306            BUILD_MAP                4
                RETURN_VALUE

 314    L1:     LOAD_GLOBAL              3 (dict + NULL)
                LOAD_FAST_BORROW         0 (record)
                CALL                     1
                STORE_FAST               1 (row)

 315            LOAD_GLOBAL              5 (_project_metadata + NULL)
                LOAD_FAST_BORROW         1 (row)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               8 ('metadata')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L2:     CALL                     1
                LOAD_FAST_BORROW         1 (row)
                LOAD_CONST               8 ('metadata')
                STORE_SUBSCR

 316            LOAD_GLOBAL              9 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               2 (db)

 317            LOAD_FAST_BORROW         2 (db)
                POP_JUMP_IF_NOT_NONE    12 (to L3)
                NOT_TAKEN

 319            LOAD_CONST               1 ('status')
                LOAD_CONST               9 ('skipped')

 320            LOAD_CONST               3 ('run_row')
                LOAD_CONST               4 (None)

 321            LOAD_CONST               5 ('warnings')
                LOAD_CONST              10 ('audit_verification_runs_unavailable')
                BUILD_LIST               1

 322            LOAD_CONST               6 ('error_code')
                LOAD_CONST              10 ('audit_verification_runs_unavailable')

 318            BUILD_MAP                4
                RETURN_VALUE

 324    L3:     NOP

 325    L4:     LOAD_FAST_BORROW         2 (db)
                LOAD_ATTR               11 (table + NULL|self)
                LOAD_GLOBAL             12 (_TABLE)
                CALL                     1
                LOAD_ATTR               15 (insert + NULL|self)
                LOAD_FAST_BORROW         1 (row)
                CALL                     1
                LOAD_ATTR               17 (execute + NULL|self)
                CALL                     0
                STORE_FAST               3 (result)

 326            LOAD_GLOBAL             19 (list + NULL)
                LOAD_GLOBAL             21 (getattr + NULL)
                LOAD_FAST_BORROW         3 (result)
                LOAD_CONST              11 ('data')
                LOAD_CONST               4 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                BUILD_LIST               0
        L7:     CALL                     1
                STORE_FAST               4 (rows)

 327            LOAD_FAST_BORROW         4 (rows)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L10)
        L8:     NOT_TAKEN
        L9:     LOAD_GLOBAL             23 (_project_row + NULL)
                LOAD_FAST_BORROW         4 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                JUMP_FORWARD            10 (to L11)
       L10:     LOAD_GLOBAL             23 (_project_row + NULL)
                LOAD_FAST_BORROW         1 (row)
                CALL                     1
       L11:     STORE_FAST               5 (proj)

 329            LOAD_CONST               1 ('status')
                LOAD_CONST              12 ('ok')

 330            LOAD_CONST               3 ('run_row')
                LOAD_FAST_BORROW         5 (proj)

 331            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 332            LOAD_CONST               6 ('error_code')
                LOAD_CONST               4 (None)

 328            BUILD_MAP                4
       L12:     RETURN_VALUE

  --   L13:     PUSH_EXC_INFO

 334            LOAD_GLOBAL             24 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       87 (to L18)
                NOT_TAKEN
                STORE_FAST               6 (e)

 335   L14:     LOAD_GLOBAL             26 (logger)
                LOAD_ATTR               29 (warning + NULL|self)

 336            LOAD_CONST              13 ('persist_verification_run db error type=')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 335            CALL                     1
                POP_TOP

 339            LOAD_CONST               1 ('status')
                LOAD_CONST               9 ('skipped')

 340            LOAD_CONST               3 ('run_row')
                LOAD_CONST               4 (None)

 341            LOAD_CONST               5 ('warnings')
                LOAD_CONST              14 ('db_write_failed:')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 342            LOAD_CONST               6 ('error_code')
                LOAD_CONST              10 ('audit_verification_runs_unavailable')

 338            BUILD_MAP                4
       L15:     SWAP                     2
       L16:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --   L17:     LOAD_CONST               4 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 334   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L13 [0]
  L6 to L8 -> L13 [0]
  L9 to L12 -> L13 [0]
  L13 to L14 -> L19 [1] lasti
  L14 to L15 -> L17 [1] lasti
  L15 to L16 -> L19 [1] lasti
  L17 to L19 -> L19 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025230, file "app/services/operator/audit_verification_runs.py", line 350>:
350           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

352           LOAD_CONST               2 ('Optional[str]')

350           LOAD_CONST               3 ('verification_type')

353           LOAD_CONST               2 ('Optional[str]')

350           LOAD_CONST               4 ('limit')

354           LOAD_CONST               5 ('Any')

350           LOAD_CONST               6 ('return')

355           LOAD_CONST               7 ('Dict[str, Any]')

350           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object list_verification_runs at 0x0000018C181A22B0, file "app/services/operator/audit_verification_runs.py", line 350>:
 350            RESUME                   0

 357            LOAD_FAST_BORROW         1 (verification_type)
                POP_JUMP_IF_NONE        39 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (verification_type)
                LOAD_GLOBAL              0 (ALLOWED_VERIFICATION_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       28 (to L1)
                NOT_TAKEN

 359            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 360            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         0 (brokerage_id)

 361            LOAD_CONST               5 ('verification_type')
                LOAD_FAST_BORROW         1 (verification_type)

 362            LOAD_CONST               6 ('limit')
                LOAD_GLOBAL              3 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1

 363            LOAD_CONST               7 ('rows')
                BUILD_LIST               0

 364            LOAD_CONST               8 ('count')
                LOAD_SMALL_INT           0

 365            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 366            LOAD_CONST              10 ('error_code')
                LOAD_CONST              11 ('invalid_verification_type')

 358            BUILD_MAP                8
                RETURN_VALUE

 368    L1:     LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              5 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               1 (None)
        L3:     STORE_FAST               3 (bid)

 369            LOAD_GLOBAL              3 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1
                STORE_FAST               4 (capped)

 370            LOAD_GLOBAL              7 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               5 (db)

 371            LOAD_FAST_BORROW         5 (db)
                POP_JUMP_IF_NOT_NONE    20 (to L4)
                NOT_TAKEN

 373            LOAD_CONST               2 ('status')
                LOAD_CONST              12 ('skipped')

 374            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)

 375            LOAD_CONST               5 ('verification_type')
                LOAD_FAST_BORROW         1 (verification_type)

 376            LOAD_CONST               6 ('limit')
                LOAD_FAST_BORROW         4 (capped)

 377            LOAD_CONST               7 ('rows')
                BUILD_LIST               0

 378            LOAD_CONST               8 ('count')
                LOAD_SMALL_INT           0

 379            LOAD_CONST               9 ('warnings')
                LOAD_CONST              13 ('audit_verification_runs_unavailable')
                BUILD_LIST               1

 380            LOAD_CONST              10 ('error_code')
                LOAD_CONST              13 ('audit_verification_runs_unavailable')

 372            BUILD_MAP                8
                RETURN_VALUE

 382    L4:     NOP

 384    L5:     LOAD_FAST_BORROW         5 (db)
                LOAD_ATTR                9 (table + NULL|self)
                LOAD_GLOBAL             10 (_TABLE)
                CALL                     1

 385            LOAD_ATTR               13 (select + NULL|self)
                LOAD_CONST              14 (',')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_GLOBAL             16 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 386            LOAD_ATTR               19 (order + NULL|self)
                LOAD_CONST              15 ('started_at')
                LOAD_CONST              16 (True)
                LOAD_CONST              17 (('desc',))
                CALL_KW                  2

 387            LOAD_ATTR               21 (limit + NULL|self)
                LOAD_FAST_BORROW         4 (capped)
                CALL                     1

 383            STORE_FAST               6 (query)

 389            LOAD_FAST_BORROW         3 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L8)
        L6:     NOT_TAKEN

 390    L7:     LOAD_FAST_BORROW         6 (query)
                LOAD_ATTR               23 (eq + NULL|self)
                LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)
                CALL                     2
                STORE_FAST               6 (query)

 391    L8:     LOAD_FAST_BORROW         1 (verification_type)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L11)
        L9:     NOT_TAKEN

 392   L10:     LOAD_FAST_BORROW         6 (query)
                LOAD_ATTR               23 (eq + NULL|self)
                LOAD_CONST               5 ('verification_type')
                LOAD_FAST_BORROW         1 (verification_type)
                CALL                     2
                STORE_FAST               6 (query)

 393   L11:     LOAD_FAST_BORROW         6 (query)
                LOAD_ATTR               25 (execute + NULL|self)
                CALL                     0
                STORE_FAST               7 (result)

 394            LOAD_GLOBAL             27 (list + NULL)
                LOAD_GLOBAL             29 (getattr + NULL)
                LOAD_FAST_BORROW         7 (result)
                LOAD_CONST              18 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
       L12:     NOT_TAKEN
       L13:     POP_TOP
                BUILD_LIST               0
       L14:     CALL                     1
                STORE_FAST               8 (rows)

 395            LOAD_CONST              19 (<code object <genexpr> at 0x0000018C180C47A0, file "app/services/operator/audit_verification_runs.py", line 395>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         8 (rows)
                GET_ITER
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      9 (p)
                SWAP                     2
       L15:     BUILD_LIST               0
                SWAP                     2
       L16:     FOR_ITER                10 (to L19)
                STORE_FAST_LOAD_FAST   153 (p, p)
       L17:     POP_JUMP_IF_NOT_NONE     3 (to L18)
                NOT_TAKEN
                JUMP_BACKWARD            8 (to L16)
       L18:     LOAD_FAST_BORROW         9 (p)
                LIST_APPEND              2
                JUMP_BACKWARD           12 (to L16)
       L19:     END_FOR
                POP_ITER
       L20:     STORE_FAST              10 (projected)
                STORE_FAST               9 (p)

 397            LOAD_CONST               2 ('status')
                LOAD_CONST              20 ('ok')

 398            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)

 399            LOAD_CONST               5 ('verification_type')
                LOAD_FAST_BORROW         1 (verification_type)

 400            LOAD_CONST               6 ('limit')
                LOAD_FAST_BORROW         4 (capped)

 401            LOAD_CONST               7 ('rows')
                LOAD_FAST_BORROW        10 (projected)

 402            LOAD_CONST               8 ('count')
                LOAD_GLOBAL             31 (len + NULL)
                LOAD_FAST_BORROW        10 (projected)
                CALL                     1

 403            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 404            LOAD_CONST              10 ('error_code')
                LOAD_CONST               1 (None)

 396            BUILD_MAP                8
       L21:     RETURN_VALUE

  --   L22:     SWAP                     2
                POP_TOP

 395            SWAP                     2
                STORE_FAST               9 (p)
                RERAISE                  0

  --   L23:     PUSH_EXC_INFO

 406            LOAD_GLOBAL             32 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       95 (to L28)
                NOT_TAKEN
                STORE_FAST              11 (e)

 407   L24:     LOAD_GLOBAL             34 (logger)
                LOAD_ATTR               37 (warning + NULL|self)

 408            LOAD_CONST              21 ('list_verification_runs read error type=')
                LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 407            CALL                     1
                POP_TOP

 411            LOAD_CONST               2 ('status')
                LOAD_CONST              12 ('skipped')

 412            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                3 (bid)

 413            LOAD_CONST               5 ('verification_type')
                LOAD_FAST                1 (verification_type)

 414            LOAD_CONST               6 ('limit')
                LOAD_FAST                4 (capped)

 415            LOAD_CONST               7 ('rows')
                BUILD_LIST               0

 416            LOAD_CONST               8 ('count')
                LOAD_SMALL_INT           0

 417            LOAD_CONST               9 ('warnings')
                LOAD_CONST              22 ('db_read_failed:')
                LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 418            LOAD_CONST              10 ('error_code')
                LOAD_CONST              13 ('audit_verification_runs_unavailable')

 410            BUILD_MAP                8
       L25:     SWAP                     2
       L26:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RETURN_VALUE

  --   L27:     LOAD_CONST               1 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 406   L28:     RERAISE                  0

  --   L29:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L23 [0]
  L7 to L9 -> L23 [0]
  L10 to L12 -> L23 [0]
  L13 to L15 -> L23 [0]
  L15 to L17 -> L22 [2]
  L18 to L20 -> L22 [2]
  L20 to L21 -> L23 [0]
  L22 to L23 -> L23 [0]
  L23 to L24 -> L29 [1] lasti
  L24 to L25 -> L27 [1] lasti
  L25 to L26 -> L29 [1] lasti
  L27 to L29 -> L29 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C180C47A0, file "app/services/operator/audit_verification_runs.py", line 395>:
 395           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "app/services/operator/audit_verification_runs.py", line 422>:
422           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

424           LOAD_CONST               2 ('Optional[str]')

422           LOAD_CONST               3 ('return')

425           LOAD_CONST               4 ('Dict[str, Any]')

422           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object verification_run_summary at 0x0000018C17E8AB60, file "app/services/operator/audit_verification_runs.py", line 422>:
 422            RESUME                   0

 428            LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L1)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST               1 (None)
        L2:     STORE_FAST               1 (bid)

 429            LOAD_GLOBAL              3 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               2 (db)

 430            LOAD_FAST_BORROW         2 (db)
                POP_JUMP_IF_NOT_NONE    20 (to L3)
                NOT_TAKEN

 432            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('skipped')

 433            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         1 (bid)

 434            LOAD_CONST               5 ('total')
                LOAD_SMALL_INT           0

 435            LOAD_CONST               6 ('by_status')
                BUILD_MAP                0

 436            LOAD_CONST               7 ('by_type')
                BUILD_MAP                0

 437            LOAD_CONST               8 ('latest_run')
                LOAD_CONST               1 (None)

 438            LOAD_CONST               9 ('warnings')
                LOAD_CONST              10 ('audit_verification_runs_unavailable')
                BUILD_LIST               1

 439            LOAD_CONST              11 ('error_code')
                LOAD_CONST              10 ('audit_verification_runs_unavailable')

 431            BUILD_MAP                8
                RETURN_VALUE

 441    L3:     NOP

 443    L4:     LOAD_FAST_BORROW         2 (db)
                LOAD_ATTR                5 (table + NULL|self)
                LOAD_GLOBAL              6 (_TABLE)
                CALL                     1

 444            LOAD_ATTR                9 (select + NULL|self)
                LOAD_CONST              12 (',')
                LOAD_ATTR               11 (join + NULL|self)
                LOAD_GLOBAL             12 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 445            LOAD_ATTR               15 (order + NULL|self)
                LOAD_CONST              13 ('started_at')
                LOAD_CONST              14 (True)
                LOAD_CONST              15 (('desc',))
                CALL_KW                  2

 446            LOAD_ATTR               17 (limit + NULL|self)
                LOAD_GLOBAL             18 (_LIST_HARD_CAP)
                CALL                     1

 447            LOAD_ATTR               21 (execute + NULL|self)
                CALL                     0

 442            STORE_FAST               3 (result)

 449            LOAD_GLOBAL             23 (list + NULL)
                LOAD_GLOBAL             25 (getattr + NULL)
                LOAD_FAST_BORROW         3 (result)
                LOAD_CONST              16 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                BUILD_LIST               0
        L7:     CALL                     1
                STORE_FAST               4 (rows)

 450            LOAD_FAST_BORROW         1 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       66 (to L18)
        L8:     NOT_TAKEN

 451    L9:     LOAD_FAST_BORROW         4 (rows)
                GET_ITER
                LOAD_FAST_AND_CLEAR      5 (r)
                SWAP                     2
       L10:     BUILD_LIST               0
                SWAP                     2
       L11:     FOR_ITER                53 (to L16)
                STORE_FAST               5 (r)
                LOAD_GLOBAL             27 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (r)
                LOAD_GLOBAL             28 (dict)
                CALL                     2
                TO_BOOL
       L12:     POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L11)
       L13:     LOAD_FAST_BORROW         5 (r)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               4 ('brokerage_id')
                CALL                     1
                LOAD_FAST_BORROW         1 (bid)
                COMPARE_OP              88 (bool(==))
       L14:     POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN
                JUMP_BACKWARD           51 (to L11)
       L15:     LOAD_FAST_BORROW         5 (r)
                LIST_APPEND              2
                JUMP_BACKWARD           55 (to L11)
       L16:     END_FOR
                POP_ITER
       L17:     STORE_FAST               4 (rows)
                STORE_FAST               5 (r)

 466   L18:     BUILD_MAP                0
                STORE_FAST               7 (by_status)

 467            BUILD_MAP                0
                STORE_FAST               8 (by_type)

 468            LOAD_FAST                4 (rows)
                GET_ITER
       L19:     FOR_ITER               185 (to L24)
                STORE_FAST               5 (r)

 469            LOAD_GLOBAL             27 (isinstance + NULL)
                LOAD_FAST                5 (r)
                LOAD_GLOBAL             28 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L20)
                NOT_TAKEN

 470            JUMP_BACKWARD           27 (to L19)

 471   L20:     LOAD_FAST                5 (r)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                STORE_FAST               9 (s)

 472            LOAD_GLOBAL             27 (isinstance + NULL)
                LOAD_FAST                9 (s)
                LOAD_GLOBAL             42 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L21)
                NOT_TAKEN
                LOAD_FAST                9 (s)
                LOAD_GLOBAL             44 (ALLOWED_RUN_STATUSES)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       28 (to L21)
                NOT_TAKEN

 473            LOAD_FAST                7 (by_status)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_FAST                9 (s)
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST_LOAD_FAST    121 (by_status, s)
                STORE_SUBSCR

 474   L21:     LOAD_FAST                5 (r)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              19 ('verification_type')
                CALL                     1
                STORE_FAST              10 (t)

 475            LOAD_GLOBAL             27 (isinstance + NULL)
                LOAD_FAST               10 (t)
                LOAD_GLOBAL             42 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L22)
                NOT_TAKEN
                JUMP_BACKWARD          145 (to L19)
       L22:     LOAD_FAST               10 (t)
                LOAD_GLOBAL             46 (ALLOWED_VERIFICATION_TYPES)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         3 (to L23)
                NOT_TAKEN
                JUMP_BACKWARD          158 (to L19)

 476   L23:     LOAD_FAST                8 (by_type)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_FAST               10 (t)
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST_LOAD_FAST    138 (by_type, t)
                STORE_SUBSCR
                JUMP_BACKWARD          187 (to L19)

 468   L24:     END_FOR
                POP_ITER

 477            LOAD_FAST                4 (rows)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L25)
                NOT_TAKEN
                LOAD_GLOBAL             49 (_project_row + NULL)
                LOAD_FAST                4 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                JUMP_FORWARD             1 (to L26)
       L25:     LOAD_CONST               1 (None)
       L26:     STORE_FAST              11 (latest)

 479            LOAD_CONST               2 ('status')
                LOAD_CONST              20 ('ok')

 480            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                1 (bid)

 481            LOAD_CONST               5 ('total')
                LOAD_GLOBAL             51 (len + NULL)
                LOAD_FAST                4 (rows)
                CALL                     1

 482            LOAD_CONST               6 ('by_status')
                LOAD_FAST                7 (by_status)

 483            LOAD_CONST               7 ('by_type')
                LOAD_FAST                8 (by_type)

 484            LOAD_CONST               8 ('latest_run')
                LOAD_FAST               11 (latest)

 485            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 486            LOAD_CONST              11 ('error_code')
                LOAD_CONST               1 (None)

 478            BUILD_MAP                8
                RETURN_VALUE

  --   L27:     SWAP                     2
                POP_TOP

 451            SWAP                     2
                STORE_FAST               5 (r)
                RERAISE                  0

  --   L28:     PUSH_EXC_INFO

 452            LOAD_GLOBAL             32 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       95 (to L33)
                NOT_TAKEN
                STORE_FAST               6 (e)

 453   L29:     LOAD_GLOBAL             34 (logger)
                LOAD_ATTR               37 (warning + NULL|self)

 454            LOAD_CONST              17 ('verification_run_summary read error type=')
                LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 453            CALL                     1
                POP_TOP

 457            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('skipped')

 458            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                1 (bid)

 459            LOAD_CONST               5 ('total')
                LOAD_SMALL_INT           0

 460            LOAD_CONST               6 ('by_status')
                BUILD_MAP                0

 461            LOAD_CONST               7 ('by_type')
                BUILD_MAP                0

 462            LOAD_CONST               8 ('latest_run')
                LOAD_CONST               1 (None)

 463            LOAD_CONST               9 ('warnings')
                LOAD_CONST              18 ('db_read_failed:')
                LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 464            LOAD_CONST              11 ('error_code')
                LOAD_CONST              10 ('audit_verification_runs_unavailable')

 456            BUILD_MAP                8
       L30:     SWAP                     2
       L31:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --   L32:     LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 452   L33:     RERAISE                  0

  --   L34:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L28 [0]
  L6 to L8 -> L28 [0]
  L9 to L10 -> L28 [0]
  L10 to L12 -> L27 [2]
  L13 to L14 -> L27 [2]
  L15 to L17 -> L27 [2]
  L17 to L18 -> L28 [0]
  L27 to L28 -> L28 [0]
  L28 to L29 -> L34 [1] lasti
  L29 to L30 -> L32 [1] lasti
  L30 to L31 -> L34 [1] lasti
  L32 to L34 -> L34 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "app/services/operator/audit_verification_runs.py", line 490>:
490           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

491           LOAD_CONST               2 ('Any')

490           LOAD_CONST               3 ('return')

492           LOAD_CONST               4 ('Dict[str, Any]')

490           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object latest_verification_status_for_brokerage at 0x0000018C17D6DFC0, file "app/services/operator/audit_verification_runs.py", line 490>:
490            RESUME                   0

495            LOAD_FAST_BORROW         0 (brokerage_id)
               POP_JUMP_IF_NONE        12 (to L1)
               NOT_TAKEN
               LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
               LOAD_FAST_BORROW         0 (brokerage_id)
               CALL                     1
               JUMP_FORWARD             1 (to L2)
       L1:     LOAD_CONST               1 (None)
       L2:     STORE_FAST               1 (bid)

496            LOAD_FAST_BORROW         1 (bid)
               POP_JUMP_IF_NOT_NONE    15 (to L3)
               NOT_TAKEN

498            LOAD_CONST               2 ('status')
               LOAD_CONST               3 ('failed')

499            LOAD_CONST               4 ('brokerage_id')
               LOAD_CONST               1 (None)

500            LOAD_CONST               5 ('latest_status')
               LOAD_CONST               6 ('NONE')

501            LOAD_CONST               7 ('started_at')
               LOAD_CONST               1 (None)

502            LOAD_CONST               8 ('error_code')
               LOAD_CONST               9 ('missing_brokerage_id')

503            LOAD_CONST              10 ('warnings')
               BUILD_LIST               0

497            BUILD_MAP                6
               RETURN_VALUE

505    L3:     LOAD_GLOBAL              3 (verification_run_summary + NULL)
               LOAD_FAST_BORROW         1 (bid)
               LOAD_CONST              11 (('brokerage_id',))
               CALL_KW                  1
               STORE_FAST               2 (summary)

506            LOAD_FAST_BORROW         2 (summary)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               2 ('status')
               CALL                     1
               LOAD_CONST              12 ('ok')
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE       89 (to L6)
               NOT_TAKEN

508            LOAD_CONST               2 ('status')
               LOAD_FAST_BORROW         2 (summary)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               2 ('status')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              13 ('skipped')

509    L4:     LOAD_CONST               4 ('brokerage_id')
               LOAD_FAST                1 (bid)

510            LOAD_CONST               5 ('latest_status')
               LOAD_CONST               6 ('NONE')

511            LOAD_CONST               7 ('started_at')
               LOAD_CONST               1 (None)

512            LOAD_CONST               8 ('error_code')
               LOAD_FAST_BORROW         2 (summary)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               8 ('error_code')
               CALL                     1

513            LOAD_CONST              10 ('warnings')
               LOAD_GLOBAL              7 (list + NULL)
               LOAD_FAST_BORROW         2 (summary)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              10 ('warnings')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L5:     CALL                     1

507            BUILD_MAP                6
               RETURN_VALUE

515    L6:     LOAD_FAST_BORROW         2 (summary)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              14 ('latest_run')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L7)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
       L7:     STORE_FAST               3 (latest)

517            LOAD_CONST               2 ('status')
               LOAD_CONST              12 ('ok')

518            LOAD_CONST               4 ('brokerage_id')
               LOAD_FAST                1 (bid)

519            LOAD_CONST               5 ('latest_status')
               LOAD_GLOBAL              9 (isinstance + NULL)
               LOAD_FAST_BORROW         3 (latest)
               LOAD_GLOBAL             10 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L8)
               NOT_TAKEN
               LOAD_FAST_BORROW         3 (latest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               2 ('status')
               CALL                     1
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               6 ('NONE')

520    L9:     LOAD_CONST               7 ('started_at')
               LOAD_GLOBAL              9 (isinstance + NULL)
               LOAD_FAST_BORROW         3 (latest)
               LOAD_GLOBAL             10 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L10)
               NOT_TAKEN
               LOAD_FAST_BORROW         3 (latest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               7 ('started_at')
               CALL                     1
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST               1 (None)

521   L11:     LOAD_CONST              15 ('completed_at')
               LOAD_GLOBAL              9 (isinstance + NULL)
               LOAD_FAST_BORROW         3 (latest)
               LOAD_GLOBAL             10 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L12)
               NOT_TAKEN
               LOAD_FAST_BORROW         3 (latest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              15 ('completed_at')
               CALL                     1
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST               1 (None)

522   L13:     LOAD_CONST               8 ('error_code')
               LOAD_CONST               1 (None)

523            LOAD_CONST              10 ('warnings')
               BUILD_LIST               0

516            BUILD_MAP                7
               RETURN_VALUE
```
