# routes/tenant_learning_tests

- **pyc:** `app\routes\__pycache__\tenant_learning_tests.cpython-314.pyc`
- **expected source path (absent):** `app\routes/tenant_learning_tests.py`
- **co_filename (from bytecode):** `app/routes/tenant_learning_tests.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** routes

## Module docstring

```
PAS181 — Tenant-safe manual-test visibility routes.

Bounded read-only surfaces for the tenant-side portal.
Mounted at ``/tenant/learning``. Auth: X-API-Key via
``require_brokerage``.

Doctrine:

* **Tenant-auth only.** No admin path here.
* **Brokerage-scoped only.** Every helper unpacks the
  brokerage_id from the resolved brokerage dict.
* **Read-only.** No mutation routes; tenants CANNOT plan /
  run / complete / cancel manual-test runs.
* **Closed tenant projection.** Drops recommendation_id,
  evidence_fingerprint, actor_type, actor_id, metadata,
  warning_count.
* **Defensive forbidden-field scan** on every response.
* **NEVER raises.**

Routes (all GET):

    GET /tenant/learning/tests
    GET /tenant/learning/tests/{test_run_id}
```

## Imports

`APIRouter`, `Any`, `Depends`, `Dict`, `HTTPException`, `Header`, `Optional`, `Query`, `__future__`, `annotations`, `app.db.brokerage_store`, `app.services.learning.manual_test_harness`, `fastapi`, `get_brokerage_by_api_key`, `get_manual_test_run`, `logging`, `manual_test_run_report`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_int`, `_final_envelope`, `_project_tenant_run`, `_project_tenant_run_list`, `_resolve_brokerage_id`, `_safe_test_run_id`, `_scan_for_forbidden`, `require_brokerage`, `tenant_tests_get_route`, `tenant_tests_list_route`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS181 — Tenant-safe manual-test visibility routes.\n\nBounded read-only surfaces for the tenant-side portal.\nMounted at ``/tenant/learning``. Auth: X-API-Key via\n``require_brokerage``.\n\nDoctrine:\n\n* **Tenant-auth only.** No admin path here.\n* **Brokerage-scoped only.** Every helper unpacks the\n  brokerage_id from the resolved brokerage dict.\n* **Read-only.** No mutation routes; tenants CANNOT plan /\n  run / complete / cancel manual-test runs.\n* **Closed tenant projection.** Drops recommendation_id,\n  evidence_fingerprint, actor_type, actor_id, metadata,\n  warning_count.\n* **Defensive forbidden-field scan** on every response.\n* **NEVER raises.**\n\nRoutes (all GET):\n\n    GET /tenant/learning/tests\n    GET /tenant/learning/tests/{test_run_id}\n'
- 'pas.tenant.learning_tests'
- '/tests'
- '/tests/{test_run_id}'
- 'x_api_key'
- 'str'
- 'demo'
- 'Invalid API key'
- 'envelope'
- 'Any'
- 'return'
- 'Optional[str]'
- 'obj'
- 'env'
- 'Dict[str, Any]'
- 'surface'
- 'tenant_learning_tests surface='
- ' collapsed — forbidden token leaked'
- 'status'
- 'failed'
- 'error_code'
- 'tenant_envelope_forbidden_field'
- 'warnings'
- 'row'
- 'rows'
- 'list'
- 'value'
- 'int'
- 'default'
- 'brokerage'
- 'limit'
- "Tenant-safe list of manual-test runs for the caller's\nbrokerage. Closed-shape projection drops every operator\ninternal."
- 'skipped'
- 'tenant.learning.tests.list'
- 'brokerage_id'
- 'payload'
- 'count'
- 'tenant_learning_tests list error type='
- 'unexpected:'
- 'test_run_id'
- 'invalid test_run_id'
- 'tenant.learning.tests.get'
- 'test_run'
- 'tenant_learning_tests get error type='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS181 — Tenant-safe manual-test visibility routes.\n\nBounded read-only surfaces for the tenant-side portal.\nMounted at ``/tenant/learning``. Auth: X-API-Key via\n``require_brokerage``.\n\nDoctrine:\n\n* **Tenant-auth only.** No admin path here.\n* **Brokerage-scoped only.** Every helper unpacks the\n  brokerage_id from the resolved brokerage dict.\n* **Read-only.** No mutation routes; tenants CANNOT plan /\n  run / complete / cancel manual-test runs.\n* **Closed tenant projection.** Drops recommendation_id,\n  evidence_fingerprint, actor_type, actor_id, metadata,\n  warning_count.\n* **Defensive forbidden-field scan** on every response.\n* **NEVER raises.**\n\nRoutes (all GET):\n\n    GET /tenant/learning/tests\n    GET /tenant/learning/tests/{test_run_id}\n')
              STORE_NAME               0 (__doc__)

 27           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 29           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 30           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (Optional)
              STORE_NAME               7 (Optional)
              POP_TOP

 32           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('APIRouter', 'Depends', 'Header', 'HTTPException', 'Query'))
              IMPORT_NAME              8 (fastapi)
              IMPORT_FROM              9 (APIRouter)
              STORE_NAME               9 (APIRouter)
              IMPORT_FROM             10 (Depends)
              STORE_NAME              10 (Depends)
              IMPORT_FROM             11 (Header)
              STORE_NAME              11 (Header)
              IMPORT_FROM             12 (HTTPException)
              STORE_NAME              12 (HTTPException)
              IMPORT_FROM             13 (Query)
              STORE_NAME              13 (Query)
              POP_TOP

 34           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('get_brokerage_by_api_key',))
              IMPORT_NAME             14 (app.db.brokerage_store)
              IMPORT_FROM             15 (get_brokerage_by_api_key)
              STORE_NAME              15 (get_brokerage_by_api_key)
              POP_TOP

 37           LOAD_NAME                9 (APIRouter)
              PUSH_NULL
              CALL                     0
              STORE_NAME              16 (router)

 38           LOAD_NAME                3 (logging)
              LOAD_ATTR               34 (getLogger)
              PUSH_NULL
              LOAD_CONST               6 ('pas.tenant.learning_tests')
              CALL                     1
              STORE_NAME              18 (logger)

 41           LOAD_NAME               11 (Header)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              CALL                     1
              BUILD_TUPLE              1
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA34B0, file "app/routes/tenant_learning_tests.py", line 41>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object require_brokerage at 0x0000018C17FE1530, file "app/routes/tenant_learning_tests.py", line 41>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              19 (require_brokerage)

 50           LOAD_CONST              31 (('phone', 'email', 'name_token', 'raw_payload', 'raw_email', 'raw_body', 'transcript', 'summary_text', 'secret', 'signature', 'dedupe_key', 'callback_notes', 'operator_notes', 'action_id', 'actor_id', 'env_value', 'env_values', 'slack_internal', 'memory_candidate', 'rationale_text', 'rationale_freeform', 'prompt_text', 'live_mutation_payload', 'evidence_fingerprint', 'evidence_raw', 'recommendation_id', 'scenario_fingerprint'))
              STORE_NAME              20 (_FORBIDDEN_TENANT_FIELDS)

 69           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA3B40, file "app/routes/tenant_learning_tests.py", line 69>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _scan_for_forbidden at 0x0000018C18024C30, file "app/routes/tenant_learning_tests.py", line 69>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (_scan_for_forbidden)

 93           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C18025730, file "app/routes/tenant_learning_tests.py", line 93>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _final_envelope at 0x0000018C17FE17D0, file "app/routes/tenant_learning_tests.py", line 93>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (_final_envelope)

109           LOAD_SMALL_INT          50
              STORE_NAME              23 (_LIST_LIMIT_DEFAULT)

110           LOAD_SMALL_INT         200
              STORE_NAME              24 (_LIST_LIMIT_MAX)

111           LOAD_SMALL_INT         200
              STORE_NAME              25 (_TEST_RUN_ID_MAX_LEN)

115           LOAD_CONST              32 (('test_run_id', 'scenario_type', 'status', 'mode', 'started_at', 'completed_at', 'score', 'confidence_score', 'risk_score'))
              STORE_NAME              26 (_TENANT_TEST_RUN_KEYS)

128           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA2970, file "app/routes/tenant_learning_tests.py", line 128>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _project_tenant_run at 0x0000018C17FE1680, file "app/routes/tenant_learning_tests.py", line 128>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_project_tenant_run)

138           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA23D0, file "app/routes/tenant_learning_tests.py", line 138>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _project_tenant_run_list at 0x0000018C17FF13B0, file "app/routes/tenant_learning_tests.py", line 138>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_project_tenant_run_list)

144           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C18026130, file "app/routes/tenant_learning_tests.py", line 144>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object _clamp_int at 0x0000018C18038170, file "app/routes/tenant_learning_tests.py", line 144>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_clamp_int)

156           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA2880, file "app/routes/tenant_learning_tests.py", line 156>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object _resolve_brokerage_id at 0x0000018C1804CED0, file "app/routes/tenant_learning_tests.py", line 156>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_resolve_brokerage_id)

165           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA2100, file "app/routes/tenant_learning_tests.py", line 165>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object _safe_test_run_id at 0x0000018C17F96140, file "app/routes/tenant_learning_tests.py", line 165>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_safe_test_run_id)

178           LOAD_NAME               16 (router)
              LOAD_ATTR               65 (get + NULL|self)
              LOAD_CONST              24 ('/tests')
              CALL                     1

180           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT          64
              LOAD_CONST              25 (('max_length',))
              CALL_KW                  2

181           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_NAME               23 (_LIST_LIMIT_DEFAULT)
              CALL                     1

182           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               19 (require_brokerage)
              CALL                     1

179           BUILD_TUPLE              3
              LOAD_CONST              26 (<code object __annotate__ at 0x0000018C18026530, file "app/routes/tenant_learning_tests.py", line 179>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object tenant_tests_list_route at 0x0000018C17F686E0, file "app/routes/tenant_learning_tests.py", line 178>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

178           CALL                     0

179           STORE_NAME              33 (tenant_tests_list_route)

223           LOAD_NAME               16 (router)
              LOAD_ATTR               65 (get + NULL|self)
              LOAD_CONST              28 ('/tests/{test_run_id}')
              CALL                     1

226           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               19 (require_brokerage)
              CALL                     1

224           BUILD_TUPLE              1
              LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA2B50, file "app/routes/tenant_learning_tests.py", line 224>)
              MAKE_FUNCTION
              LOAD_CONST              30 (<code object tenant_tests_get_route at 0x0000018C17D8BF50, file "app/routes/tenant_learning_tests.py", line 223>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

223           CALL                     0

224           STORE_NAME              34 (tenant_tests_get_route)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app/routes/tenant_learning_tests.py", line 41>:
 41           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('x_api_key')
              LOAD_CONST               2 ('str')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object require_brokerage at 0x0000018C17FE1530, file "app/routes/tenant_learning_tests.py", line 41>:
 41           RESUME                   0

 42           LOAD_GLOBAL              1 (get_brokerage_by_api_key + NULL)
              LOAD_FAST_BORROW         0 (x_api_key)
              CALL                     1
              STORE_FAST               1 (brokerage)

 43           LOAD_FAST_BORROW         1 (brokerage)
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (brokerage)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               0 ('id')
              CALL                     1
              LOAD_CONST               1 ('demo')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       14 (to L2)
              NOT_TAKEN

 44   L1:     LOAD_GLOBAL              5 (HTTPException + NULL)
              LOAD_CONST               2 (401)
              LOAD_CONST               3 ('Invalid API key')
              LOAD_CONST               4 (('status_code', 'detail'))
              CALL_KW                  2
              RAISE_VARARGS            1

 45   L2:     LOAD_FAST_BORROW         1 (brokerage)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app/routes/tenant_learning_tests.py", line 69>:
 69           RESUME                   0
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

Disassembly of <code object _scan_for_forbidden at 0x0000018C18024C30, file "app/routes/tenant_learning_tests.py", line 69>:
  --           MAKE_CELL                1 (walk)

  69           RESUME                   0

  70           LOAD_CONST               0 (<code object __annotate__ at 0x0000018C17FA3960, file "app/routes/tenant_learning_tests.py", line 70>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object walk at 0x0000018C17CC2E60, file "app/routes/tenant_learning_tests.py", line 70>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

  90           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app/routes/tenant_learning_tests.py", line 70>:
 70           RESUME                   0
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

Disassembly of <code object walk at 0x0000018C17CC2E60, file "app/routes/tenant_learning_tests.py", line 70>:
  --            COPY_FREE_VARS           1

  70            RESUME                   0

  71            NOP

  72    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      111 (to L16)
        L2:     NOT_TAKEN

  73    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                88 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

  74            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L10)
                NOT_TAKEN

  75            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

  76            LOAD_GLOBAL             10 (_FORBIDDEN_TENANT_FIELDS)
                GET_ITER
        L5:     FOR_ITER                15 (to L9)
                STORE_FAST               4 (tok)

  77            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)

  78    L7:     LOAD_FAST_BORROW         4 (tok)
                SWAP                     2
                POP_TOP
                SWAP                     2
                POP_TOP
        L8:     RETURN_VALUE

  76    L9:     END_FOR
                POP_ITER

  79   L10:     LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

  80            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           86 (to L4)

  81   L12:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L13:     RETURN_VALUE

  73   L14:     END_FOR
                POP_ITER

  89   L15:     LOAD_CONST               0 (None)
                RETURN_VALUE

  82   L16:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             12 (list)
                LOAD_GLOBAL             14 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L22)
                NOT_TAKEN

  83            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L17:     FOR_ITER                23 (to L21)
                STORE_FAST               2 (v)

  84            LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

  85            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           21 (to L17)

  86   L19:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L20:     RETURN_VALUE

  83   L21:     END_FOR
                POP_ITER

  89   L22:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

  87            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L25)
                NOT_TAKEN
                POP_TOP

  88   L24:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

  87   L25:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app/routes/tenant_learning_tests.py", line 93>:
 93           RESUME                   0
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

Disassembly of <code object _final_envelope at 0x0000018C17FE17D0, file "app/routes/tenant_learning_tests.py", line 93>:
 93           RESUME                   0

 94           LOAD_GLOBAL              1 (_scan_for_forbidden + NULL)
              LOAD_FAST_BORROW         0 (env)
              CALL                     1
              STORE_FAST               2 (leak)

 95           LOAD_FAST_BORROW         2 (leak)
              TO_BOOL
              POP_JUMP_IF_FALSE       37 (to L1)
              NOT_TAKEN

 96           LOAD_GLOBAL              2 (logger)
              LOAD_ATTR                5 (warning + NULL|self)

 97           LOAD_CONST               0 ('tenant_learning_tests surface=')
              LOAD_FAST_BORROW         1 (surface)
              FORMAT_SIMPLE
              LOAD_CONST               1 (' collapsed — forbidden token leaked')
              BUILD_STRING             3

 96           CALL                     1
              POP_TOP

101           LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('failed')

102           LOAD_CONST               4 ('surface')
              LOAD_FAST_BORROW         1 (surface)

103           LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('tenant_envelope_forbidden_field')

104           LOAD_CONST               7 ('warnings')
              LOAD_CONST               6 ('tenant_envelope_forbidden_field')
              BUILD_LIST               1

100           BUILD_MAP                4
              RETURN_VALUE

106   L1:     LOAD_FAST_BORROW         0 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app/routes/tenant_learning_tests.py", line 128>:
128           RESUME                   0
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

Disassembly of <code object _project_tenant_run at 0x0000018C17FE1680, file "app/routes/tenant_learning_tests.py", line 128>:
128           RESUME                   0

129           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

130           BUILD_MAP                0
              RETURN_VALUE

131   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

132           LOAD_GLOBAL              4 (_TENANT_TEST_RUN_KEYS)
              GET_ITER
      L2:     FOR_ITER                21 (to L4)
              STORE_FAST               2 (k)

133           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

134   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, k)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, k)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L2)

132   L4:     END_FOR
              POP_ITER

135           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app/routes/tenant_learning_tests.py", line 138>:
138           RESUME                   0
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

Disassembly of <code object _project_tenant_run_list at 0x0000018C17FF13B0, file "app/routes/tenant_learning_tests.py", line 138>:
 138           RESUME                   0

 139           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (rows)
               LOAD_GLOBAL              2 (list)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

 140           BUILD_LIST               0
               RETURN_VALUE

 141   L1:     LOAD_FAST_BORROW         0 (rows)
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
       L5:     LOAD_GLOBAL              7 (_project_tenant_run + NULL)
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

 141           SWAP                     2
               STORE_FAST               1 (r)
               RERAISE                  0
ExceptionTable:
  L2 to L4 -> L8 [2]
  L5 to L7 -> L8 [2]

Disassembly of <code object __annotate__ at 0x0000018C18026130, file "app/routes/tenant_learning_tests.py", line 144>:
144           RESUME                   0
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

Disassembly of <code object _clamp_int at 0x0000018C18038170, file "app/routes/tenant_learning_tests.py", line 144>:
 144           RESUME                   0

 145           NOP

 146   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

 149   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 150           LOAD_FAST                1 (lo)
               RETURN_VALUE

 151   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 152           LOAD_FAST                2 (hi)
               RETURN_VALUE

 153   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 147           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

 148           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 147   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app/routes/tenant_learning_tests.py", line 156>:
156           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _resolve_brokerage_id at 0x0000018C1804CED0, file "app/routes/tenant_learning_tests.py", line 156>:
156           RESUME                   0

157           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

158           LOAD_CONST               0 (None)
              RETURN_VALUE

159   L1:     LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('id')
              CALL                     1
              STORE_FAST               1 (bid)

160           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (bid)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (bid)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

161   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

162   L3:     LOAD_FAST_BORROW         1 (bid)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app/routes/tenant_learning_tests.py", line 165>:
165           RESUME                   0
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

Disassembly of <code object _safe_test_run_id at 0x0000018C17F96140, file "app/routes/tenant_learning_tests.py", line 165>:
165           RESUME                   0

166           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

167           LOAD_CONST               0 (None)
              RETURN_VALUE

168   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

169           LOAD_FAST_BORROW         1 (s)
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

170   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

171   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026530, file "app/routes/tenant_learning_tests.py", line 179>:
179           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

180           LOAD_CONST               2 ('Optional[str]')

179           LOAD_CONST               3 ('limit')

181           LOAD_CONST               4 ('int')

179           LOAD_CONST               5 ('return')

183           LOAD_CONST               6 ('Dict[str, Any]')

179           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object tenant_tests_list_route at 0x0000018C17F686E0, file "app/routes/tenant_learning_tests.py", line 178>:
 178            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 187            LOAD_GLOBAL              1 (_resolve_brokerage_id + NULL)
                LOAD_FAST_BORROW         2 (brokerage)
                CALL                     1
                STORE_FAST               3 (bid)

 188            LOAD_FAST_BORROW         3 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 189            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               2 (401)
                LOAD_CONST               3 ('Invalid API key')
                LOAD_CONST               4 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 190    L2:     LOAD_GLOBAL              5 (_clamp_int + NULL)
                LOAD_FAST_BORROW         1 (limit)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              6 (_LIST_LIMIT_MAX)
                LOAD_GLOBAL              8 (_LIST_LIMIT_DEFAULT)
                CALL                     4
                STORE_FAST               4 (capped)

 191            LOAD_SMALL_INT           0
                LOAD_CONST               5 (('manual_test_run_report',))
                IMPORT_NAME              5 (app.services.learning.manual_test_harness)
                IMPORT_FROM              6 (manual_test_run_report)
                STORE_FAST               5 (manual_test_run_report)
                POP_TOP

 192    L3:     NOP

 193    L4:     LOAD_FAST_BORROW         5 (manual_test_run_report)
                PUSH_NULL

 194            LOAD_FAST_BORROW         3 (bid)

 195            LOAD_FAST_BORROW         0 (status)

 196            LOAD_FAST_BORROW         4 (capped)

 193            LOAD_CONST               6 (('brokerage_id', 'status', 'limit'))
                CALL_KW                  3
                STORE_FAST               6 (result)

 198            LOAD_GLOBAL             15 (_project_tenant_run_list + NULL)
                LOAD_FAST_BORROW         6 (result)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               7 ('rows')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                BUILD_LIST               0
        L7:     CALL                     1
                STORE_FAST               7 (projected)

 200            LOAD_CONST               8 ('status')
                LOAD_FAST_BORROW         6 (result)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               8 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                LOAD_CONST               9 ('skipped')

 201   L10:     LOAD_CONST              10 ('surface')
                LOAD_CONST              11 ('tenant.learning.tests.list')

 202            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST                3 (bid)

 203            LOAD_CONST              13 ('payload')

 204            LOAD_CONST               7 ('rows')
                LOAD_FAST_BORROW         7 (projected)

 205            LOAD_CONST              14 ('count')
                LOAD_GLOBAL             19 (len + NULL)
                LOAD_FAST_BORROW         7 (projected)
                CALL                     1

 203            BUILD_MAP                2

 207            LOAD_CONST              15 ('warnings')
                LOAD_GLOBAL             21 (list + NULL)
                LOAD_FAST_BORROW         6 (result)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              15 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                BUILD_LIST               0
       L13:     CALL                     1

 208            LOAD_CONST              16 ('error_code')
                LOAD_FAST_BORROW         6 (result)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              16 ('error_code')
                CALL                     1

 199            BUILD_MAP                6
                STORE_FAST               8 (env)

 220   L14:     LOAD_GLOBAL             33 (_final_envelope + NULL)
                LOAD_FAST_BORROW         8 (env)
                LOAD_CONST              11 ('tenant.learning.tests.list')
                LOAD_CONST              20 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 210            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L19)
                NOT_TAKEN
                STORE_FAST               9 (e)

 211   L16:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 212            LOAD_CONST              17 ('tenant_learning_tests list error type=')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 211            CALL                     1
                POP_TOP

 215            LOAD_CONST               8 ('status')
                LOAD_CONST              18 ('failed')

 216            LOAD_CONST              10 ('surface')
                LOAD_CONST              11 ('tenant.learning.tests.list')

 217            LOAD_CONST              16 ('error_code')
                LOAD_CONST              19 ('unexpected:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 218            LOAD_CONST              15 ('warnings')
                BUILD_LIST               0

 214            BUILD_MAP                4
                STORE_FAST               8 (env)
       L17:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L14)

  --   L18:     LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 210   L19:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app/routes/tenant_learning_tests.py", line 224>:
224           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('test_run_id')

225           LOAD_CONST               2 ('str')

224           LOAD_CONST               3 ('return')

227           LOAD_CONST               4 ('Dict[str, Any]')

224           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object tenant_tests_get_route at 0x0000018C17D8BF50, file "app/routes/tenant_learning_tests.py", line 223>:
 223            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 228            LOAD_GLOBAL              1 (_resolve_brokerage_id + NULL)
                LOAD_FAST_BORROW         1 (brokerage)
                CALL                     1
                STORE_FAST               2 (bid)

 229            LOAD_FAST_BORROW         2 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 230            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               1 (401)
                LOAD_CONST               2 ('Invalid API key')
                LOAD_CONST               3 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 231    L2:     LOAD_GLOBAL              5 (_safe_test_run_id + NULL)
                LOAD_FAST_BORROW         0 (test_run_id)
                CALL                     1
                STORE_FAST               3 (trid)

 232            LOAD_FAST_BORROW         3 (trid)
                POP_JUMP_IF_NOT_NONE    14 (to L3)
                NOT_TAKEN

 233            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               4 (400)
                LOAD_CONST               5 ('invalid test_run_id')
                LOAD_CONST               3 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 234    L3:     LOAD_SMALL_INT           0
                LOAD_CONST               6 (('get_manual_test_run',))
                IMPORT_NAME              3 (app.services.learning.manual_test_harness)
                IMPORT_FROM              4 (get_manual_test_run)
                STORE_FAST               4 (get_manual_test_run)
                POP_TOP

 235    L4:     NOP

 236    L5:     LOAD_FAST_BORROW         4 (get_manual_test_run)
                PUSH_NULL
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (trid, bid)
                LOAD_CONST               7 (('test_run_id', 'brokerage_id'))
                CALL_KW                  2
                STORE_FAST               5 (result)

 238            LOAD_CONST               8 ('status')
                LOAD_FAST_BORROW         5 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               8 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                LOAD_CONST               9 ('skipped')

 239    L8:     LOAD_CONST              10 ('surface')
                LOAD_CONST              11 ('tenant.learning.tests.get')

 240            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST                2 (bid)

 241            LOAD_CONST              13 ('payload')
                LOAD_GLOBAL             13 (_project_tenant_run + NULL)
                LOAD_FAST_BORROW         5 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              14 ('test_run')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                BUILD_MAP                0
       L11:     CALL                     1

 242            LOAD_CONST              15 ('warnings')
                LOAD_GLOBAL             15 (list + NULL)
                LOAD_FAST_BORROW         5 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              15 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
       L12:     NOT_TAKEN
       L13:     POP_TOP
                BUILD_LIST               0
       L14:     CALL                     1

 243            LOAD_CONST              16 ('error_code')
                LOAD_FAST_BORROW         5 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              16 ('error_code')
                CALL                     1

 237            BUILD_MAP                6
                STORE_FAST               6 (env)

 255   L15:     LOAD_GLOBAL             27 (_final_envelope + NULL)
                LOAD_FAST_BORROW         6 (env)
                LOAD_CONST              11 ('tenant.learning.tests.get')
                LOAD_CONST              20 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L16:     PUSH_EXC_INFO

 245            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L20)
                NOT_TAKEN
                STORE_FAST               7 (e)

 246   L17:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 247            LOAD_CONST              17 ('tenant_learning_tests get error type=')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 246            CALL                     1
                POP_TOP

 250            LOAD_CONST               8 ('status')
                LOAD_CONST              18 ('failed')

 251            LOAD_CONST              10 ('surface')
                LOAD_CONST              11 ('tenant.learning.tests.get')

 252            LOAD_CONST              16 ('error_code')
                LOAD_CONST              19 ('unexpected:')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 253            LOAD_CONST              15 ('warnings')
                BUILD_LIST               0

 249            BUILD_MAP                4
                STORE_FAST               6 (env)
       L18:     POP_EXCEPT
                LOAD_CONST               0 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L15)

  --   L19:     LOAD_CONST               0 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 245   L20:     RERAISE                  0

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
```
