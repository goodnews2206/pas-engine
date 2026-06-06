# routes/operator_learning_tests

- **pyc:** `app\routes\__pycache__\operator_learning_tests.cpython-314.pyc`
- **expected source path (absent):** `app\routes/operator_learning_tests.py`
- **co_filename (from bytecode):** `app/routes/operator_learning_tests.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** routes

## Module docstring

```
PAS181 — Operator manual-test routes.

Admin-only REST surface for PAS181 manual-test execution.
Mounted at ``/ops/learning``. Wraps
``app.services.learning.manual_test_harness`` into 5 routes.

Doctrine:

* **Admin auth only** (X-Admin-Key).
* **No live behaviour mutation.** Every helper this module
  calls is simulation-only.
* **No outbound calls / no booking writes / no worker enqueue
  / no Memory Review writes.** PAS181 readiness verifies the
  import bans structurally.
* **Forbidden-token scanner** on every response.
* **Audit-safe.** Every mutation writes a PAS174 audit row
  via the harness.
* **NEVER raises.**

Routes:

    GET  /ops/learning/tests
    GET  /ops/learning/tests/{test_run_id}
    POST /ops/learning/recommendations/{recommendation_id}/manual-tests
    POST /ops/learning/tests/{test_run_id}/cancel
    POST /ops/learning/tests/{test_run_id}/complete
```

## Imports

`APIRouter`, `Any`, `Body`, `Depends`, `Dict`, `HTTPException`, `Header`, `Optional`, `Query`, `__future__`, `annotations`, `app.config`, `app.services.learning.manual_test_harness`, `app.services.security.rate_limit`, `cancel_manual_test_run`, `check_rate_limit`, `complete_manual_test_run`, `create_manual_test_plan`, `fastapi`, `get_manual_test_run`, `get_settings`, `logging`, `manual_test_run_report`, `run_manual_test_simulation`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_int`, `_final_envelope`, `_project_operator_run`, `_project_operator_run_list`, `_safe_brokerage`, `_safe_recommendation_id`, `_safe_test_run_id`, `_scan_for_forbidden`, `cancel_test_route`, `complete_test_route`, `create_and_run_test_route`, `get_test_route`, `list_tests_route`, `require_admin`

## Env-key candidates

`ADMIN`, `OPERATOR`, `SIMULATION_ONLY`

## String constants (redacted where noted)

- '\nPAS181 — Operator manual-test routes.\n\nAdmin-only REST surface for PAS181 manual-test execution.\nMounted at ``/ops/learning``. Wraps\n``app.services.learning.manual_test_harness`` into 5 routes.\n\nDoctrine:\n\n* **Admin auth only** (X-Admin-Key).\n* **No live behaviour mutation.** Every helper this module\n  calls is simulation-only.\n* **No outbound calls / no booking writes / no worker enqueue\n  / no Memory Review writes.** PAS181 readiness verifies the\n  import bans structurally.\n* **Forbidden-token scanner** on every response.\n* **Audit-safe.** Every mutation writes a PAS174 audit row\n  via the harness.\n* **NEVER raises.**\n\nRoutes:\n\n    GET  /ops/learning/tests\n    GET  /ops/learning/tests/{test_run_id}\n    POST /ops/learning/recommendations/{recommendation_id}/manual-tests\n    POST /ops/learning/tests/{test_run_id}/cancel\n    POST /ops/learning/tests/{test_run_id}/complete\n'
- 'pas.ops.learning_tests'
- '/tests'
- '/tests/{test_run_id}'
- '/recommendations/{recommendation_id}/manual-tests'
- '/tests/{test_run_id}/cancel'
- '/tests/{test_run_id}/complete'
- 'x_admin_key'
- 'str'
- 'return'
- 'bool'
- 'Invalid admin key'
- 'admin'
- 'ADMIN'
- 'allowed'
- 'Operator rate limit exceeded. Retry after the current window.'
- 'envelope'
- 'Any'
- 'Optional[str]'
- 'obj'
- 'env'
- 'Dict[str, Any]'
- 'surface'
- 'operator_learning_tests surface='
- ' collapsed — forbidden token leaked'
- 'status'
- 'failed'
- 'error_code'
- 'ops_envelope_forbidden_token'
- 'warnings'
- 'value'
- 'int'
- 'default'
- 'row'
- 'rows'
- 'list'
- 'brokerage_id'
- 'limit'
- 'skipped'
- 'ops.learning.tests.list'
- 'count'
- 'operator_learning_tests list error type='
- 'unexpected:'
- 'test_run_id'
- 'invalid test_run_id'
- 'ops.learning.tests.get'
- 'record'
- 'test_run'
- 'operator_learning_tests get error type='
- 'recommendation_id'
- 'body'
- 'Atomic plan + run. Creates PLANNED, executes the\ndeterministic simulation, transitions to RUNNING. The\noperator must call ``complete`` afterwards to finalize.'
- 'invalid recommendation_id'
- 'actor_type'
- 'actor_id'
- 'scenario_type'
- 'mode'
- 'SIMULATION_ONLY'
- 'ops.learning.tests.create'
- 'plan'
- 'run'
- 'OPERATOR'
- 'audit_row'
- 'evidence'
- 'transition'
- 'operator_learning_tests create error type='
- 'ops.learning.tests.cancel'
- 'operator_learning_tests cancel error type='
- 'acknowledge_high_risk'
- 'ops.learning.tests.complete'
- 'operator_learning_tests complete error type='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS181 — Operator manual-test routes.\n\nAdmin-only REST surface for PAS181 manual-test execution.\nMounted at ``/ops/learning``. Wraps\n``app.services.learning.manual_test_harness`` into 5 routes.\n\nDoctrine:\n\n* **Admin auth only** (X-Admin-Key).\n* **No live behaviour mutation.** Every helper this module\n  calls is simulation-only.\n* **No outbound calls / no booking writes / no worker enqueue\n  / no Memory Review writes.** PAS181 readiness verifies the\n  import bans structurally.\n* **Forbidden-token scanner** on every response.\n* **Audit-safe.** Every mutation writes a PAS174 audit row\n  via the harness.\n* **NEVER raises.**\n\nRoutes:\n\n    GET  /ops/learning/tests\n    GET  /ops/learning/tests/{test_run_id}\n    POST /ops/learning/recommendations/{recommendation_id}/manual-tests\n    POST /ops/learning/tests/{test_run_id}/cancel\n    POST /ops/learning/tests/{test_run_id}/complete\n')
              STORE_NAME               0 (__doc__)

 30           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 32           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 33           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (Optional)
              STORE_NAME               7 (Optional)
              POP_TOP

 35           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('APIRouter', 'Body', 'Depends', 'Header', 'HTTPException', 'Query'))
              IMPORT_NAME              8 (fastapi)
              IMPORT_FROM              9 (APIRouter)
              STORE_NAME               9 (APIRouter)
              IMPORT_FROM             10 (Body)
              STORE_NAME              10 (Body)
              IMPORT_FROM             11 (Depends)
              STORE_NAME              11 (Depends)
              IMPORT_FROM             12 (Header)
              STORE_NAME              12 (Header)
              IMPORT_FROM             13 (HTTPException)
              STORE_NAME              13 (HTTPException)
              IMPORT_FROM             14 (Query)
              STORE_NAME              14 (Query)
              POP_TOP

 37           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('get_settings',))
              IMPORT_NAME             15 (app.config)
              IMPORT_FROM             16 (get_settings)
              STORE_NAME              16 (get_settings)
              POP_TOP

 40           LOAD_NAME                9 (APIRouter)
              PUSH_NULL
              CALL                     0
              STORE_NAME              17 (router)

 41           LOAD_NAME                3 (logging)
              LOAD_ATTR               36 (getLogger)
              PUSH_NULL
              LOAD_CONST               6 ('pas.ops.learning_tests')
              CALL                     1
              STORE_NAME              19 (logger)

 44           LOAD_NAME               12 (Header)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              CALL                     1
              BUILD_TUPLE              1
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA2C40, file "app/routes/operator_learning_tests.py", line 44>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object require_admin at 0x0000018C179A7290, file "app/routes/operator_learning_tests.py", line 44>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              20 (require_admin)

 73           LOAD_SMALL_INT         200
              STORE_NAME              21 (_BROKERAGE_ID_MAX_LEN)

 74           LOAD_SMALL_INT         200
              STORE_NAME              22 (_REC_ID_MAX_LEN)

 75           LOAD_SMALL_INT         200
              STORE_NAME              23 (_TEST_RUN_ID_MAX_LEN)

 76           LOAD_SMALL_INT          50
              STORE_NAME              24 (_LIST_LIMIT_DEFAULT)

 77           LOAD_CONST              10 (500)
              STORE_NAME              25 (_LIST_LIMIT_MAX)

 80           LOAD_CONST              43 (('phone', 'email', 'name_token', 'transcript', 'summary_text', 'raw_payload', 'raw_email', 'raw_body', 'secret', 'signature', 'dedupe_key', 'callback_notes', 'rationale_text', 'rationale_freeform', 'prompt_text', 'live_mutation_payload', 'evidence_raw'))
              STORE_NAME              26 (_FORBIDDEN_RESPONSE_TOKENS)

 90           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA34B0, file "app/routes/operator_learning_tests.py", line 90>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object _scan_for_forbidden at 0x0000018C18025C30, file "app/routes/operator_learning_tests.py", line 90>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_scan_for_forbidden)

114           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18025A30, file "app/routes/operator_learning_tests.py", line 114>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object _final_envelope at 0x0000018C17FE1290, file "app/routes/operator_learning_tests.py", line 114>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_final_envelope)

130           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA3960, file "app/routes/operator_learning_tests.py", line 130>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _safe_brokerage at 0x0000018C17F962B0, file "app/routes/operator_learning_tests.py", line 130>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_safe_brokerage)

139           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA2970, file "app/routes/operator_learning_tests.py", line 139>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _safe_recommendation_id at 0x0000018C17F96590, file "app/routes/operator_learning_tests.py", line 139>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_safe_recommendation_id)

148           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA23D0, file "app/routes/operator_learning_tests.py", line 148>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _safe_test_run_id at 0x0000018C17F95FD0, file "app/routes/operator_learning_tests.py", line 148>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_safe_test_run_id)

157           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C18024C30, file "app/routes/operator_learning_tests.py", line 157>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _clamp_int at 0x0000018C18038DF0, file "app/routes/operator_learning_tests.py", line 157>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_clamp_int)

173           LOAD_CONST              44 (('test_run_id', 'recommendation_id', 'brokerage_id', 'scenario_type', 'status', 'mode', 'started_at', 'completed_at', 'score', 'confidence_score', 'risk_score', 'evidence_fingerprint', 'warning_count', 'error_code', 'actor_type', 'metadata'))
              STORE_NAME              33 (_OPERATOR_TEST_RUN_KEYS)

193           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA2880, file "app/routes/operator_learning_tests.py", line 193>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object _project_operator_run at 0x0000018C17FE1680, file "app/routes/operator_learning_tests.py", line 193>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              34 (_project_operator_run)

203           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA2100, file "app/routes/operator_learning_tests.py", line 203>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object _project_operator_run_list at 0x0000018C17FF13B0, file "app/routes/operator_learning_tests.py", line 203>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              35 (_project_operator_run_list)

213           LOAD_NAME               17 (router)
              LOAD_ATTR               73 (get + NULL|self)
              LOAD_CONST              27 ('/tests')
              CALL                     1

215           LOAD_NAME               14 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT         200
              LOAD_CONST              28 (('max_length',))
              CALL_KW                  2

216           LOAD_NAME               14 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT          64
              LOAD_CONST              28 (('max_length',))
              CALL_KW                  2

217           LOAD_NAME               14 (Query)
              PUSH_NULL
              LOAD_NAME               24 (_LIST_LIMIT_DEFAULT)
              CALL                     1

218           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               20 (require_admin)
              CALL                     1

214           BUILD_TUPLE              4
              LOAD_CONST              29 (<code object __annotate__ at 0x0000018C18026330, file "app/routes/operator_learning_tests.py", line 214>)
              MAKE_FUNCTION
              LOAD_CONST              30 (<code object list_tests_route at 0x0000018C17E93090, file "app/routes/operator_learning_tests.py", line 213>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

213           CALL                     0

214           STORE_NAME              37 (list_tests_route)

251           LOAD_NAME               17 (router)
              LOAD_ATTR               73 (get + NULL|self)
              LOAD_CONST              31 ('/tests/{test_run_id}')
              CALL                     1

254           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               20 (require_admin)
              CALL                     1

252           BUILD_TUPLE              1
              LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA2B50, file "app/routes/operator_learning_tests.py", line 252>)
              MAKE_FUNCTION
              LOAD_CONST              33 (<code object get_test_route at 0x0000018C17EE1CC0, file "app/routes/operator_learning_tests.py", line 251>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

251           CALL                     0

252           STORE_NAME              38 (get_test_route)

286           LOAD_NAME               17 (router)
              LOAD_ATTR               79 (post + NULL|self)
              LOAD_CONST              34 ('/recommendations/{recommendation_id}/manual-tests')
              CALL                     1

289           LOAD_NAME               10 (Body)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              CALL                     1

290           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               20 (require_admin)
              CALL                     1

287           BUILD_TUPLE              2
              LOAD_CONST              35 (<code object __annotate__ at 0x0000018C18024B30, file "app/routes/operator_learning_tests.py", line 287>)
              MAKE_FUNCTION
              LOAD_CONST              36 (<code object create_and_run_test_route at 0x0000018C17ED9FB0, file "app/routes/operator_learning_tests.py", line 286>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

286           CALL                     0

287           STORE_NAME              40 (create_and_run_test_route)

358           LOAD_NAME               17 (router)
              LOAD_ATTR               79 (post + NULL|self)
              LOAD_CONST              37 ('/tests/{test_run_id}/cancel')
              CALL                     1

361           LOAD_NAME               10 (Body)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              CALL                     1

362           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               20 (require_admin)
              CALL                     1

359           BUILD_TUPLE              2
              LOAD_CONST              38 (<code object __annotate__ at 0x0000018C18026630, file "app/routes/operator_learning_tests.py", line 359>)
              MAKE_FUNCTION
              LOAD_CONST              39 (<code object cancel_test_route at 0x0000018C17F60B30, file "app/routes/operator_learning_tests.py", line 358>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

358           CALL                     0

359           STORE_NAME              41 (cancel_test_route)

398           LOAD_NAME               17 (router)
              LOAD_ATTR               79 (post + NULL|self)
              LOAD_CONST              40 ('/tests/{test_run_id}/complete')
              CALL                     1

401           LOAD_NAME               10 (Body)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              CALL                     1

402           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               20 (require_admin)
              CALL                     1

399           BUILD_TUPLE              2
              LOAD_CONST              41 (<code object __annotate__ at 0x0000018C18026430, file "app/routes/operator_learning_tests.py", line 399>)
              MAKE_FUNCTION
              LOAD_CONST              42 (<code object complete_test_route at 0x0000018C17E7D9A0, file "app/routes/operator_learning_tests.py", line 398>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

398           CALL                     0

399           STORE_NAME              42 (complete_test_route)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app/routes/operator_learning_tests.py", line 44>:
 44           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('x_admin_key')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object require_admin at 0x0000018C179A7290, file "app/routes/operator_learning_tests.py", line 44>:
  44            RESUME                   0

  45            LOAD_GLOBAL              1 (get_settings + NULL)
                CALL                     0
                STORE_FAST               1 (settings)

  46            LOAD_FAST_BORROW         1 (settings)
                LOAD_ATTR                2 (ADMIN_API_KEY)
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (x_admin_key, settings)
                LOAD_ATTR                2 (ADMIN_API_KEY)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       14 (to L2)
                NOT_TAKEN

  47    L1:     LOAD_GLOBAL              5 (HTTPException + NULL)
                LOAD_CONST               0 (401)
                LOAD_CONST               1 ('Invalid admin key')
                LOAD_CONST               2 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

  50    L2:     NOP

  51    L3:     LOAD_SMALL_INT           0
                LOAD_CONST               3 (('check_rate_limit',))
                IMPORT_NAME              3 (app.services.security.rate_limit)
                IMPORT_FROM              4 (check_rate_limit)
                STORE_FAST               2 (check_rate_limit)
                POP_TOP

  52            LOAD_FAST_BORROW         2 (check_rate_limit)
                PUSH_NULL

  53            LOAD_CONST               4 ('admin')

  54            LOAD_CONST               5 ('ADMIN')

  55            LOAD_FAST_BORROW         0 (x_admin_key)

  52            LOAD_CONST               6 (('surface', 'actor_type', 'actor_token'))
                CALL_KW                  3
                STORE_FAST               3 (_rl_verdict)

  57            LOAD_FAST_BORROW         3 (_rl_verdict)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               7 ('allowed')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L6)
        L4:     NOT_TAKEN

  58    L5:     LOAD_GLOBAL              5 (HTTPException + NULL)

  59            LOAD_CONST               8 (429)

  60            LOAD_CONST               9 ('Operator rate limit exceeded. Retry after the current window.')

  58            LOAD_CONST               2 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

  57    L6:     NOP

  66            LOAD_CONST              10 (True)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  62            LOAD_GLOBAL              4 (HTTPException)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                POP_TOP

  63            RAISE_VARARGS            0

  64    L8:     LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L12)
        L9:     NOT_TAKEN
       L10:     POP_TOP

  65   L11:     POP_EXCEPT

  66            LOAD_CONST              10 (True)
                RETURN_VALUE

  64   L12:     RERAISE                  0

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L7 [0]
  L5 to L6 -> L7 [0]
  L7 to L9 -> L13 [1] lasti
  L10 to L11 -> L13 [1] lasti
  L12 to L13 -> L13 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app/routes/operator_learning_tests.py", line 90>:
 90           RESUME                   0
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

Disassembly of <code object _scan_for_forbidden at 0x0000018C18025C30, file "app/routes/operator_learning_tests.py", line 90>:
  --           MAKE_CELL                1 (walk)

  90           RESUME                   0

  91           LOAD_CONST               0 (<code object __annotate__ at 0x0000018C17FA3B40, file "app/routes/operator_learning_tests.py", line 91>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object walk at 0x0000018C17CC1CE0, file "app/routes/operator_learning_tests.py", line 91>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

 111           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app/routes/operator_learning_tests.py", line 91>:
 91           RESUME                   0
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

Disassembly of <code object walk at 0x0000018C17CC1CE0, file "app/routes/operator_learning_tests.py", line 91>:
  --            COPY_FREE_VARS           1

  91            RESUME                   0

  92            NOP

  93    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      111 (to L16)
        L2:     NOT_TAKEN

  94    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                88 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

  95            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L10)
                NOT_TAKEN

  96            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

  97            LOAD_GLOBAL             10 (_FORBIDDEN_RESPONSE_TOKENS)
                GET_ITER
        L5:     FOR_ITER                15 (to L9)
                STORE_FAST               4 (tok)

  98            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)

  99    L7:     LOAD_FAST_BORROW         4 (tok)
                SWAP                     2
                POP_TOP
                SWAP                     2
                POP_TOP
        L8:     RETURN_VALUE

  97    L9:     END_FOR
                POP_ITER

 100   L10:     LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 101            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           86 (to L4)

 102   L12:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L13:     RETURN_VALUE

  94   L14:     END_FOR
                POP_ITER

 110   L15:     LOAD_CONST               0 (None)
                RETURN_VALUE

 103   L16:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             12 (list)
                LOAD_GLOBAL             14 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L22)
                NOT_TAKEN

 104            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L17:     FOR_ITER                23 (to L21)
                STORE_FAST               2 (v)

 105            LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 106            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           21 (to L17)

 107   L19:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L20:     RETURN_VALUE

 104   L21:     END_FOR
                POP_ITER

 110   L22:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 108            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L25)
                NOT_TAKEN
                POP_TOP

 109   L24:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 108   L25:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app/routes/operator_learning_tests.py", line 114>:
114           RESUME                   0
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

Disassembly of <code object _final_envelope at 0x0000018C17FE1290, file "app/routes/operator_learning_tests.py", line 114>:
114           RESUME                   0

115           LOAD_GLOBAL              1 (_scan_for_forbidden + NULL)
              LOAD_FAST_BORROW         0 (env)
              CALL                     1
              STORE_FAST               2 (leak)

116           LOAD_FAST_BORROW         2 (leak)
              TO_BOOL
              POP_JUMP_IF_FALSE       37 (to L1)
              NOT_TAKEN

117           LOAD_GLOBAL              2 (logger)
              LOAD_ATTR                5 (warning + NULL|self)

118           LOAD_CONST               0 ('operator_learning_tests surface=')
              LOAD_FAST_BORROW         1 (surface)
              FORMAT_SIMPLE
              LOAD_CONST               1 (' collapsed — forbidden token leaked')
              BUILD_STRING             3

117           CALL                     1
              POP_TOP

122           LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('failed')

123           LOAD_CONST               4 ('surface')
              LOAD_FAST_BORROW         1 (surface)

124           LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('ops_envelope_forbidden_token')

125           LOAD_CONST               7 ('warnings')
              LOAD_CONST               6 ('ops_envelope_forbidden_token')
              BUILD_LIST               1

121           BUILD_MAP                4
              RETURN_VALUE

127   L1:     LOAD_FAST_BORROW         0 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app/routes/operator_learning_tests.py", line 130>:
130           RESUME                   0
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

Disassembly of <code object _safe_brokerage at 0x0000018C17F962B0, file "app/routes/operator_learning_tests.py", line 130>:
130           RESUME                   0

131           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

132           LOAD_CONST               0 (None)
              RETURN_VALUE

133   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

134           LOAD_FAST_BORROW         1 (s)
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

135   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

136   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app/routes/operator_learning_tests.py", line 139>:
139           RESUME                   0
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

Disassembly of <code object _safe_recommendation_id at 0x0000018C17F96590, file "app/routes/operator_learning_tests.py", line 139>:
139           RESUME                   0

140           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

141           LOAD_CONST               0 (None)
              RETURN_VALUE

142   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

143           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_REC_ID_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

144   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

145   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app/routes/operator_learning_tests.py", line 148>:
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

Disassembly of <code object _safe_test_run_id at 0x0000018C17F95FD0, file "app/routes/operator_learning_tests.py", line 148>:
148           RESUME                   0

149           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

150           LOAD_CONST               0 (None)
              RETURN_VALUE

151   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

152           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_TEST_RUN_ID_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

153   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

154   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app/routes/operator_learning_tests.py", line 157>:
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
              LOAD_CONST               3 ('lo')
              LOAD_CONST               4 ('int')
              LOAD_CONST               5 ('hi')
              LOAD_CONST               4 ('int')
              LOAD_CONST               6 ('default')
              LOAD_CONST               4 ('int')
              LOAD_CONST               7 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _clamp_int at 0x0000018C18038DF0, file "app/routes/operator_learning_tests.py", line 157>:
 157           RESUME                   0

 158           NOP

 159   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

 162   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 163           LOAD_FAST                1 (lo)
               RETURN_VALUE

 164   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 165           LOAD_FAST                2 (hi)
               RETURN_VALUE

 166   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 160           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

 161           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 160   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app/routes/operator_learning_tests.py", line 193>:
193           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _project_operator_run at 0x0000018C17FE1680, file "app/routes/operator_learning_tests.py", line 193>:
193           RESUME                   0

194           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

195           BUILD_MAP                0
              RETURN_VALUE

196   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

197           LOAD_GLOBAL              4 (_OPERATOR_TEST_RUN_KEYS)
              GET_ITER
      L2:     FOR_ITER                21 (to L4)
              STORE_FAST               2 (k)

198           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

199   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, k)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, k)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L2)

197   L4:     END_FOR
              POP_ITER

200           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app/routes/operator_learning_tests.py", line 203>:
203           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rows')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('list')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _project_operator_run_list at 0x0000018C17FF13B0, file "app/routes/operator_learning_tests.py", line 203>:
 203           RESUME                   0

 204           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (rows)
               LOAD_GLOBAL              2 (list)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

 205           BUILD_LIST               0
               RETURN_VALUE

 206   L1:     LOAD_FAST_BORROW         0 (rows)
               GET_ITER
               LOAD_FAST_AND_CLEAR      1 (r)
               SWAP                     2
       L2:     BUILD_LIST               0
               SWAP                     2
       L3:     FOR_ITER                38 (to L6)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (r)
               LOAD_GLOBAL              4 (dict)
               CALL                     2
               TO_BOOL
       L4:     POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           27 (to L3)
       L5:     LOAD_GLOBAL              7 (_project_operator_run + NULL)
               LOAD_FAST_BORROW         1 (r)
               CALL                     1
               LIST_APPEND              2
               JUMP_BACKWARD           40 (to L3)
       L6:     END_FOR
               POP_ITER
       L7:     SWAP                     2
               STORE_FAST               1 (r)
               RETURN_VALUE

  --   L8:     SWAP                     2
               POP_TOP

 206           SWAP                     2
               STORE_FAST               1 (r)
               RERAISE                  0
ExceptionTable:
  L2 to L4 -> L8 [2]
  L5 to L7 -> L8 [2]

Disassembly of <code object __annotate__ at 0x0000018C18026330, file "app/routes/operator_learning_tests.py", line 214>:
214           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

215           LOAD_CONST               2 ('Optional[str]')

214           LOAD_CONST               3 ('status')

216           LOAD_CONST               2 ('Optional[str]')

214           LOAD_CONST               4 ('limit')

217           LOAD_CONST               5 ('int')

214           LOAD_CONST               6 ('return')

219           LOAD_CONST               7 ('Dict[str, Any]')

214           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object list_tests_route at 0x0000018C17E93090, file "app/routes/operator_learning_tests.py", line 213>:
 213            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 220            LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               0 (None)
        L3:     STORE_FAST               4 (bid)

 221            LOAD_GLOBAL              3 (_clamp_int + NULL)
                LOAD_FAST_BORROW         2 (limit)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              4 (_LIST_LIMIT_MAX)
                LOAD_GLOBAL              6 (_LIST_LIMIT_DEFAULT)
                CALL                     4
                STORE_FAST               5 (capped_limit)

 222            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('manual_test_run_report',))
                IMPORT_NAME              4 (app.services.learning.manual_test_harness)
                IMPORT_FROM              5 (manual_test_run_report)
                STORE_FAST               6 (manual_test_run_report)
                POP_TOP

 223    L4:     NOP

 224    L5:     LOAD_FAST_BORROW         6 (manual_test_run_report)
                PUSH_NULL

 225            LOAD_FAST_BORROW         4 (bid)

 226            LOAD_FAST_BORROW         1 (status)

 227            LOAD_FAST_BORROW         5 (capped_limit)

 224            LOAD_CONST               2 (('brokerage_id', 'status', 'limit'))
                CALL_KW                  3
                STORE_FAST               7 (result)

 229            LOAD_GLOBAL             13 (_project_operator_run_list + NULL)
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               3 ('rows')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                BUILD_LIST               0
        L8:     CALL                     1
                STORE_FAST               8 (rows)

 231            LOAD_CONST               4 ('status')
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               4 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                LOAD_CONST               5 ('skipped')

 232   L11:     LOAD_CONST               6 ('surface')
                LOAD_CONST               7 ('ops.learning.tests.list')

 233            LOAD_CONST               3 ('rows')
                LOAD_FAST                8 (rows)

 234            LOAD_CONST               8 ('count')
                LOAD_GLOBAL             17 (len + NULL)
                LOAD_FAST_BORROW         8 (rows)
                CALL                     1

 235            LOAD_CONST               9 ('warnings')
                LOAD_GLOBAL             19 (list + NULL)
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               9 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
       L12:     NOT_TAKEN
       L13:     POP_TOP
                BUILD_LIST               0
       L14:     CALL                     1

 236            LOAD_CONST              10 ('error_code')
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              10 ('error_code')
                CALL                     1

 230            BUILD_MAP                6
                STORE_FAST               9 (env)

 248   L15:     LOAD_GLOBAL             31 (_final_envelope + NULL)
                LOAD_FAST_BORROW         9 (env)
                LOAD_CONST               7 ('ops.learning.tests.list')
                LOAD_CONST              14 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L16:     PUSH_EXC_INFO

 238            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L20)
                NOT_TAKEN
                STORE_FAST              10 (e)

 239   L17:     LOAD_GLOBAL             22 (logger)
                LOAD_ATTR               25 (warning + NULL|self)

 240            LOAD_CONST              11 ('operator_learning_tests list error type=')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 239            CALL                     1
                POP_TOP

 243            LOAD_CONST               4 ('status')
                LOAD_CONST              12 ('failed')

 244            LOAD_CONST               6 ('surface')
                LOAD_CONST               7 ('ops.learning.tests.list')

 245            LOAD_CONST              10 ('error_code')
                LOAD_CONST              13 ('unexpected:')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 246            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 242            BUILD_MAP                4
                STORE_FAST               9 (env)
       L18:     POP_EXCEPT
                LOAD_CONST               0 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L15)

  --   L19:     LOAD_CONST               0 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 238   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L22:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L4 -> L22 [0] lasti
  L5 to L6 -> L16 [0]
  L7 to L9 -> L16 [0]
  L10 to L12 -> L16 [0]
  L13 to L15 -> L16 [0]
  L15 to L16 -> L22 [0] lasti
  L16 to L17 -> L21 [1] lasti
  L17 to L18 -> L19 [1] lasti
  L18 to L19 -> L22 [0] lasti
  L19 to L21 -> L21 [1] lasti
  L21 to L22 -> L22 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app/routes/operator_learning_tests.py", line 252>:
252           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('test_run_id')

253           LOAD_CONST               2 ('str')

252           LOAD_CONST               3 ('return')

255           LOAD_CONST               4 ('Dict[str, Any]')

252           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object get_test_route at 0x0000018C17EE1CC0, file "app/routes/operator_learning_tests.py", line 251>:
 251            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 256            LOAD_GLOBAL              1 (_safe_test_run_id + NULL)
                LOAD_FAST_BORROW         0 (test_run_id)
                CALL                     1
                STORE_FAST               2 (trid)

 257            LOAD_FAST_BORROW         2 (trid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 258            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               1 (400)
                LOAD_CONST               2 ('invalid test_run_id')
                LOAD_CONST               3 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 259    L2:     LOAD_SMALL_INT           0
                LOAD_CONST               4 (('get_manual_test_run',))
                IMPORT_NAME              2 (app.services.learning.manual_test_harness)
                IMPORT_FROM              3 (get_manual_test_run)
                STORE_FAST               3 (get_manual_test_run)
                POP_TOP

 260    L3:     NOP

 261    L4:     LOAD_FAST_BORROW         3 (get_manual_test_run)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (trid)
                LOAD_CONST               5 (('test_run_id',))
                CALL_KW                  1
                STORE_FAST               4 (result)

 263            LOAD_CONST               6 ('status')
                LOAD_FAST_BORROW         4 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               6 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                LOAD_CONST               7 ('skipped')

 264    L7:     LOAD_CONST               8 ('surface')
                LOAD_CONST               9 ('ops.learning.tests.get')

 265            LOAD_CONST              10 ('record')
                LOAD_GLOBAL             11 (_project_operator_run + NULL)
                LOAD_FAST_BORROW         4 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              11 ('test_run')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                BUILD_MAP                0
       L10:     CALL                     1

 266            LOAD_CONST              12 ('warnings')
                LOAD_GLOBAL             13 (list + NULL)
                LOAD_FAST_BORROW         4 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              12 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                BUILD_LIST               0
       L13:     CALL                     1

 267            LOAD_CONST              13 ('error_code')
                LOAD_FAST_BORROW         4 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              13 ('error_code')
                CALL                     1

 262            BUILD_MAP                5
                STORE_FAST               5 (env)

 279   L14:     LOAD_GLOBAL             25 (_final_envelope + NULL)
                LOAD_FAST_BORROW         5 (env)
                LOAD_CONST               9 ('ops.learning.tests.get')
                LOAD_CONST              17 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 269            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L19)
                NOT_TAKEN
                STORE_FAST               6 (e)

 270   L16:     LOAD_GLOBAL             16 (logger)
                LOAD_ATTR               19 (warning + NULL|self)

 271            LOAD_CONST              14 ('operator_learning_tests get error type=')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 270            CALL                     1
                POP_TOP

 274            LOAD_CONST               6 ('status')
                LOAD_CONST              15 ('failed')

 275            LOAD_CONST               8 ('surface')
                LOAD_CONST               9 ('ops.learning.tests.get')

 276            LOAD_CONST              13 ('error_code')
                LOAD_CONST              16 ('unexpected:')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 277            LOAD_CONST              12 ('warnings')
                BUILD_LIST               0

 273            BUILD_MAP                4
                STORE_FAST               5 (env)
       L17:     POP_EXCEPT
                LOAD_CONST               0 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L14)

  --   L18:     LOAD_CONST               0 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 269   L19:     RERAISE                  0

  --   L20:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L21:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L21 [0] lasti
  L4 to L5 -> L15 [0]
  L6 to L8 -> L15 [0]
  L9 to L11 -> L15 [0]
  L12 to L14 -> L15 [0]
  L14 to L15 -> L21 [0] lasti
  L15 to L16 -> L20 [1] lasti
  L16 to L17 -> L18 [1] lasti
  L17 to L18 -> L21 [0] lasti
  L18 to L20 -> L20 [1] lasti
  L20 to L21 -> L21 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app/routes/operator_learning_tests.py", line 287>:
287           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendation_id')

288           LOAD_CONST               2 ('str')

287           LOAD_CONST               3 ('body')

289           LOAD_CONST               4 ('Dict[str, Any]')

287           LOAD_CONST               5 ('return')

291           LOAD_CONST               4 ('Dict[str, Any]')

287           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object create_and_run_test_route at 0x0000018C17ED9FB0, file "app/routes/operator_learning_tests.py", line 286>:
 286            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 295            LOAD_GLOBAL              1 (_safe_recommendation_id + NULL)
                LOAD_FAST_BORROW         0 (recommendation_id)
                CALL                     1
                STORE_FAST               3 (rid)

 296            LOAD_FAST_BORROW         3 (rid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 297            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               2 (400)
                LOAD_CONST               3 ('invalid recommendation_id')
                LOAD_CONST               4 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 298    L2:     LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (body)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               5 ('actor_type')
                CALL                     1
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               1 (None)
        L4:     STORE_FAST               4 (actor_type)

 299            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (body)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               6 ('actor_id')
                CALL                     1
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               1 (None)
        L6:     STORE_FAST               5 (actor_id)

 300            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (body)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L7)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               7 ('scenario_type')
                CALL                     1
                JUMP_FORWARD             1 (to L8)
        L7:     LOAD_CONST               1 (None)
        L8:     STORE_FAST               6 (scenario_type)

 301            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (body)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L9)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               8 ('mode')
                CALL                     1
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               9 ('SIMULATION_ONLY')
       L10:     STORE_FAST               7 (mode)

 302            LOAD_SMALL_INT           0
                LOAD_CONST              10 (('create_manual_test_plan', 'run_manual_test_simulation'))
                IMPORT_NAME              5 (app.services.learning.manual_test_harness)
                IMPORT_FROM              6 (create_manual_test_plan)
                STORE_FAST               8 (create_manual_test_plan)
                IMPORT_FROM              7 (run_manual_test_simulation)
                STORE_FAST               9 (run_manual_test_simulation)
                POP_TOP

 305   L11:     NOP

 306   L12:     LOAD_FAST                8 (create_manual_test_plan)
                PUSH_NULL

 307            LOAD_FAST                3 (rid)

 308            LOAD_FAST                6 (scenario_type)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
       L13:     NOT_TAKEN
       L14:     POP_TOP
                LOAD_CONST              11 ('')

 309   L15:     LOAD_FAST                4 (actor_type)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
       L16:     NOT_TAKEN
       L17:     POP_TOP
                LOAD_CONST              11 ('')

 310   L18:     LOAD_FAST                5 (actor_id)

 311            LOAD_FAST                7 (mode)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L21)
       L19:     NOT_TAKEN
       L20:     POP_TOP
                LOAD_CONST               9 ('SIMULATION_ONLY')

 306   L21:     LOAD_CONST              12 (('recommendation_id', 'scenario_type', 'actor_type', 'actor_id', 'mode'))
                CALL_KW                  5
                STORE_FAST              10 (plan)

 313            LOAD_FAST_BORROW        10 (plan)
                LOAD_CONST              13 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST              14 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE      102 (to L29)
                NOT_TAKEN

 315            LOAD_CONST              13 ('status')
                LOAD_FAST_BORROW        10 (plan)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              13 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L24)
       L22:     NOT_TAKEN
       L23:     POP_TOP
                LOAD_CONST              15 ('failed')

 316   L24:     LOAD_CONST              16 ('surface')
                LOAD_CONST              17 ('ops.learning.tests.create')

 317            LOAD_CONST              18 ('plan')
                LOAD_FAST               10 (plan)

 318            LOAD_CONST              19 ('run')
                LOAD_CONST               1 (None)

 319            LOAD_CONST              20 ('warnings')
                LOAD_GLOBAL             17 (list + NULL)
                LOAD_FAST_BORROW        10 (plan)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              20 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L27)
       L25:     NOT_TAKEN
       L26:     POP_TOP
                BUILD_LIST               0
       L27:     CALL                     1

 320            LOAD_CONST              21 ('error_code')
                LOAD_FAST_BORROW        10 (plan)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              21 ('error_code')
                CALL                     1

 314            BUILD_MAP                6
                STORE_FAST              11 (env)

 322            LOAD_GLOBAL             19 (_final_envelope + NULL)
                LOAD_FAST_BORROW        11 (env)
                LOAD_CONST              17 ('ops.learning.tests.create')
                LOAD_CONST              22 (('surface',))
                CALL_KW                  2
       L28:     RETURN_VALUE

 323   L29:     LOAD_FAST_BORROW        10 (plan)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              23 ('test_run')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L32)
       L30:     NOT_TAKEN
       L31:     POP_TOP
                BUILD_MAP                0
       L32:     LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              24 ('test_run_id')
                CALL                     1
                STORE_FAST              12 (trid)

 324            LOAD_FAST                9 (run_manual_test_simulation)
                PUSH_NULL

 325            LOAD_FAST               12 (trid)

 326            LOAD_FAST                4 (actor_type)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L35)
       L33:     NOT_TAKEN
       L34:     POP_TOP
                LOAD_CONST              25 ('OPERATOR')

 327   L35:     LOAD_FAST_BORROW         5 (actor_id)

 324            LOAD_CONST              26 (('test_run_id', 'actor_type', 'actor_id'))
                CALL_KW                  3
                STORE_FAST              13 (run)

 330            LOAD_CONST              13 ('status')
                LOAD_FAST_BORROW        13 (run)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              13 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L38)
       L36:     NOT_TAKEN
       L37:     POP_TOP
                LOAD_CONST              15 ('failed')

 331   L38:     LOAD_CONST              16 ('surface')
                LOAD_CONST              17 ('ops.learning.tests.create')

 332            LOAD_CONST              18 ('plan')

 333            LOAD_CONST              23 ('test_run')
                LOAD_GLOBAL             21 (_project_operator_run + NULL)
                LOAD_FAST_BORROW        10 (plan)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              23 ('test_run')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L41)
       L39:     NOT_TAKEN
       L40:     POP_TOP
                BUILD_MAP                0
       L41:     CALL                     1

 334            LOAD_CONST              27 ('audit_row')
                LOAD_FAST_BORROW        10 (plan)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              27 ('audit_row')
                CALL                     1

 332            BUILD_MAP                2

 336            LOAD_CONST              19 ('run')

 337            LOAD_CONST              23 ('test_run')
                LOAD_GLOBAL             21 (_project_operator_run + NULL)
                LOAD_FAST_BORROW        13 (run)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              23 ('test_run')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L44)
       L42:     NOT_TAKEN
       L43:     POP_TOP
                BUILD_MAP                0
       L44:     CALL                     1

 338            LOAD_CONST              28 ('evidence')
                LOAD_FAST_BORROW        13 (run)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              28 ('evidence')
                CALL                     1

 339            LOAD_CONST              29 ('transition')
                LOAD_FAST_BORROW        13 (run)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              29 ('transition')
                CALL                     1

 340            LOAD_CONST              27 ('audit_row')
                LOAD_FAST_BORROW        13 (run)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              27 ('audit_row')
                CALL                     1

 336            BUILD_MAP                4

 342            LOAD_CONST              20 ('warnings')
                LOAD_GLOBAL             17 (list + NULL)
                LOAD_FAST_BORROW        13 (run)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              20 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L47)
       L45:     NOT_TAKEN
       L46:     POP_TOP
                BUILD_LIST               0
       L47:     CALL                     1

 343            LOAD_CONST              21 ('error_code')
                LOAD_FAST_BORROW        13 (run)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              21 ('error_code')
                CALL                     1

 329            BUILD_MAP                6
                STORE_FAST              11 (env)

 355   L48:     LOAD_GLOBAL             19 (_final_envelope + NULL)
                LOAD_FAST_BORROW        11 (env)
                LOAD_CONST              17 ('ops.learning.tests.create')
                LOAD_CONST              22 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L49:     PUSH_EXC_INFO

 345            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L53)
                NOT_TAKEN
                STORE_FAST              14 (e)

 346   L50:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 347            LOAD_CONST              30 ('operator_learning_tests create error type=')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 346            CALL                     1
                POP_TOP

 350            LOAD_CONST              13 ('status')
                LOAD_CONST              15 ('failed')

 351            LOAD_CONST              16 ('surface')
                LOAD_CONST              17 ('ops.learning.tests.create')

 352            LOAD_CONST              21 ('error_code')
                LOAD_CONST              31 ('unexpected:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 353            LOAD_CONST              20 ('warnings')
                BUILD_LIST               0

 349            BUILD_MAP                4
                STORE_FAST              11 (env)
       L51:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L48)

  --   L52:     LOAD_CONST               1 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RERAISE                  1

 345   L53:     RERAISE                  0

  --   L54:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L55:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L11 -> L55 [0] lasti
  L12 to L13 -> L49 [0]
  L14 to L16 -> L49 [0]
  L17 to L19 -> L49 [0]
  L20 to L22 -> L49 [0]
  L23 to L25 -> L49 [0]
  L26 to L28 -> L49 [0]
  L28 to L29 -> L55 [0] lasti
  L29 to L30 -> L49 [0]
  L31 to L33 -> L49 [0]
  L34 to L36 -> L49 [0]
  L37 to L39 -> L49 [0]
  L40 to L42 -> L49 [0]
  L43 to L45 -> L49 [0]
  L46 to L48 -> L49 [0]
  L48 to L49 -> L55 [0] lasti
  L49 to L50 -> L54 [1] lasti
  L50 to L51 -> L52 [1] lasti
  L51 to L52 -> L55 [0] lasti
  L52 to L54 -> L54 [1] lasti
  L54 to L55 -> L55 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026630, file "app/routes/operator_learning_tests.py", line 359>:
359           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('test_run_id')

360           LOAD_CONST               2 ('str')

359           LOAD_CONST               3 ('body')

361           LOAD_CONST               4 ('Dict[str, Any]')

359           LOAD_CONST               5 ('return')

363           LOAD_CONST               4 ('Dict[str, Any]')

359           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object cancel_test_route at 0x0000018C17F60B30, file "app/routes/operator_learning_tests.py", line 358>:
 358            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 364            LOAD_GLOBAL              1 (_safe_test_run_id + NULL)
                LOAD_FAST_BORROW         0 (test_run_id)
                CALL                     1
                STORE_FAST               3 (trid)

 365            LOAD_FAST_BORROW         3 (trid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 366            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               1 (400)
                LOAD_CONST               2 ('invalid test_run_id')
                LOAD_CONST               3 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 367    L2:     LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (body)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               4 ('actor_type')
                CALL                     1
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               0 (None)
        L4:     STORE_FAST               4 (actor_type)

 368            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (body)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               5 ('actor_id')
                CALL                     1
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               0 (None)
        L6:     STORE_FAST               5 (actor_id)

 369            LOAD_SMALL_INT           0
                LOAD_CONST               6 (('cancel_manual_test_run',))
                IMPORT_NAME              5 (app.services.learning.manual_test_harness)
                IMPORT_FROM              6 (cancel_manual_test_run)
                STORE_FAST               6 (cancel_manual_test_run)
                POP_TOP

 370    L7:     NOP

 371    L8:     LOAD_FAST                6 (cancel_manual_test_run)
                PUSH_NULL

 372            LOAD_FAST                3 (trid)

 373            LOAD_FAST                4 (actor_type)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                LOAD_CONST               7 ('')

 374   L11:     LOAD_FAST_BORROW         5 (actor_id)

 371            LOAD_CONST               8 (('test_run_id', 'actor_type', 'actor_id'))
                CALL_KW                  3
                STORE_FAST               7 (result)

 377            LOAD_CONST               9 ('status')
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               9 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
       L12:     NOT_TAKEN
       L13:     POP_TOP
                LOAD_CONST              10 ('failed')

 378   L14:     LOAD_CONST              11 ('surface')
                LOAD_CONST              12 ('ops.learning.tests.cancel')

 379            LOAD_CONST              13 ('record')
                LOAD_GLOBAL             15 (_project_operator_run + NULL)
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              14 ('test_run')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L17)
       L15:     NOT_TAKEN
       L16:     POP_TOP
                BUILD_MAP                0
       L17:     CALL                     1

 380            LOAD_CONST              15 ('transition')
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              15 ('transition')
                CALL                     1

 381            LOAD_CONST              16 ('audit_row')
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              16 ('audit_row')
                CALL                     1

 382            LOAD_CONST              17 ('warnings')
                LOAD_GLOBAL             17 (list + NULL)
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              17 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L20)
       L18:     NOT_TAKEN
       L19:     POP_TOP
                BUILD_LIST               0
       L20:     CALL                     1

 383            LOAD_CONST              18 ('error_code')
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              18 ('error_code')
                CALL                     1

 376            BUILD_MAP                7
                STORE_FAST               8 (env)

 395   L21:     LOAD_GLOBAL             29 (_final_envelope + NULL)
                LOAD_FAST_BORROW         8 (env)
                LOAD_CONST              12 ('ops.learning.tests.cancel')
                LOAD_CONST              21 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L22:     PUSH_EXC_INFO

 385            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L26)
                NOT_TAKEN
                STORE_FAST               9 (e)

 386   L23:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 387            LOAD_CONST              19 ('operator_learning_tests cancel error type=')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 386            CALL                     1
                POP_TOP

 390            LOAD_CONST               9 ('status')
                LOAD_CONST              10 ('failed')

 391            LOAD_CONST              11 ('surface')
                LOAD_CONST              12 ('ops.learning.tests.cancel')

 392            LOAD_CONST              18 ('error_code')
                LOAD_CONST              20 ('unexpected:')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 393            LOAD_CONST              17 ('warnings')
                BUILD_LIST               0

 389            BUILD_MAP                4
                STORE_FAST               8 (env)
       L24:     POP_EXCEPT
                LOAD_CONST               0 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L21)

  --   L25:     LOAD_CONST               0 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 385   L26:     RERAISE                  0

  --   L27:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L28:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L7 -> L28 [0] lasti
  L8 to L9 -> L22 [0]
  L10 to L12 -> L22 [0]
  L13 to L15 -> L22 [0]
  L16 to L18 -> L22 [0]
  L19 to L21 -> L22 [0]
  L21 to L22 -> L28 [0] lasti
  L22 to L23 -> L27 [1] lasti
  L23 to L24 -> L25 [1] lasti
  L24 to L25 -> L28 [0] lasti
  L25 to L27 -> L27 [1] lasti
  L27 to L28 -> L28 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "app/routes/operator_learning_tests.py", line 399>:
399           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('test_run_id')

400           LOAD_CONST               2 ('str')

399           LOAD_CONST               3 ('body')

401           LOAD_CONST               4 ('Dict[str, Any]')

399           LOAD_CONST               5 ('return')

403           LOAD_CONST               4 ('Dict[str, Any]')

399           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object complete_test_route at 0x0000018C17E7D9A0, file "app/routes/operator_learning_tests.py", line 398>:
 398            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 404            LOAD_GLOBAL              1 (_safe_test_run_id + NULL)
                LOAD_FAST_BORROW         0 (test_run_id)
                CALL                     1
                STORE_FAST               3 (trid)

 405            LOAD_FAST_BORROW         3 (trid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 406            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               1 (400)
                LOAD_CONST               2 ('invalid test_run_id')
                LOAD_CONST               3 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 407    L2:     LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (body)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               4 ('actor_type')
                CALL                     1
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               0 (None)
        L4:     STORE_FAST               4 (actor_type)

 408            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (body)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               5 ('actor_id')
                CALL                     1
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               0 (None)
        L6:     STORE_FAST               5 (actor_id)

 409            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (body)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L7)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               6 ('acknowledge_high_risk')
                CALL                     1
                JUMP_FORWARD             1 (to L8)
        L7:     LOAD_CONST               7 (False)
        L8:     STORE_FAST               6 (acknowledge_high_risk)

 410            LOAD_SMALL_INT           0
                LOAD_CONST               8 (('complete_manual_test_run',))
                IMPORT_NAME              5 (app.services.learning.manual_test_harness)
                IMPORT_FROM              6 (complete_manual_test_run)
                STORE_FAST               7 (complete_manual_test_run)
                POP_TOP

 411    L9:     NOP

 412   L10:     LOAD_FAST                7 (complete_manual_test_run)
                PUSH_NULL

 413            LOAD_FAST                3 (trid)

 414            LOAD_FAST                4 (actor_type)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                LOAD_CONST               9 ('')

 415   L13:     LOAD_FAST_BORROW         5 (actor_id)

 416            LOAD_GLOBAL             15 (bool + NULL)
                LOAD_FAST_BORROW         6 (acknowledge_high_risk)
                CALL                     1

 412            LOAD_CONST              10 (('test_run_id', 'actor_type', 'actor_id', 'acknowledge_high_risk'))
                CALL_KW                  4
                STORE_FAST               8 (result)

 419            LOAD_CONST              11 ('status')
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              11 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
       L14:     NOT_TAKEN
       L15:     POP_TOP
                LOAD_CONST              12 ('failed')

 420   L16:     LOAD_CONST              13 ('surface')
                LOAD_CONST              14 ('ops.learning.tests.complete')

 421            LOAD_CONST              15 ('record')
                LOAD_GLOBAL             17 (_project_operator_run + NULL)
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              16 ('test_run')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L19)
       L17:     NOT_TAKEN
       L18:     POP_TOP
                BUILD_MAP                0
       L19:     CALL                     1

 422            LOAD_CONST              17 ('transition')
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              17 ('transition')
                CALL                     1

 423            LOAD_CONST              18 ('audit_row')
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              18 ('audit_row')
                CALL                     1

 424            LOAD_CONST              19 ('warnings')
                LOAD_GLOBAL             19 (list + NULL)
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              19 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L22)
       L20:     NOT_TAKEN
       L21:     POP_TOP
                BUILD_LIST               0
       L22:     CALL                     1

 425            LOAD_CONST              20 ('error_code')
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              20 ('error_code')
                CALL                     1

 418            BUILD_MAP                7
                STORE_FAST               9 (env)

 437   L23:     LOAD_GLOBAL             31 (_final_envelope + NULL)
                LOAD_FAST_BORROW         9 (env)
                LOAD_CONST              14 ('ops.learning.tests.complete')
                LOAD_CONST              23 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L24:     PUSH_EXC_INFO

 427            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L28)
                NOT_TAKEN
                STORE_FAST              10 (e)

 428   L25:     LOAD_GLOBAL             22 (logger)
                LOAD_ATTR               25 (warning + NULL|self)

 429            LOAD_CONST              21 ('operator_learning_tests complete error type=')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 428            CALL                     1
                POP_TOP

 432            LOAD_CONST              11 ('status')
                LOAD_CONST              12 ('failed')

 433            LOAD_CONST              13 ('surface')
                LOAD_CONST              14 ('ops.learning.tests.complete')

 434            LOAD_CONST              20 ('error_code')
                LOAD_CONST              22 ('unexpected:')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 435            LOAD_CONST              19 ('warnings')
                BUILD_LIST               0

 431            BUILD_MAP                4
                STORE_FAST               9 (env)
       L26:     POP_EXCEPT
                LOAD_CONST               0 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L23)

  --   L27:     LOAD_CONST               0 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 427   L28:     RERAISE                  0

  --   L29:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L30:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L9 -> L30 [0] lasti
  L10 to L11 -> L24 [0]
  L12 to L14 -> L24 [0]
  L15 to L17 -> L24 [0]
  L18 to L20 -> L24 [0]
  L21 to L23 -> L24 [0]
  L23 to L24 -> L30 [0] lasti
  L24 to L25 -> L29 [1] lasti
  L25 to L26 -> L27 [1] lasti
  L26 to L27 -> L30 [0] lasti
  L27 to L29 -> L29 [1] lasti
  L29 to L30 -> L30 [0] lasti
```
