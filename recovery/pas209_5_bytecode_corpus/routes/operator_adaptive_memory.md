# routes/operator_adaptive_memory

- **pyc:** `app\routes\__pycache__\operator_adaptive_memory.cpython-314.pyc`
- **expected source path (absent):** `app\routes/operator_adaptive_memory.py`
- **co_filename (from bytecode):** `app/routes/operator_adaptive_memory.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** routes

## Module docstring

```
PAS182 — Operator adaptive-memory bridge routes.

Admin-only REST surface for the PAS182 manual-test → CANDIDATE
memory bridge. Mounted at ``/ops/learning``. Wraps
``app.services.learning.adaptive_memory_bridge`` into 2 routes.

Doctrine:

* **Admin auth only** (X-Admin-Key) + PAS-SECURITY-04
  operator rate limit.
* **No live behaviour mutation.** The bridge writes a
  CANDIDATE memory only — APPROVED is the Memory Review
  console's job.
* **Forbidden-token scanner** on every response.
* **Audit-safe.** Confirmation + rejection both write a
  PAS174 audit row via the bridge service.
* **NEVER raises.**

Routes:

    POST /ops/learning/manual-tests/{test_run_id}/bridge-memory-candidate
    GET  /ops/learning/adaptive-memory/bridge-report
```

## Imports

`APIRouter`, `Any`, `Body`, `Depends`, `Dict`, `HTTPException`, `Header`, `Optional`, `Query`, `__future__`, `adaptive_memory_bridge_report`, `annotations`, `app.config`, `app.services.learning.adaptive_memory_bridge`, `app.services.learning.adaptive_memory_projection`, `app.services.security.rate_limit`, `bridge_to_memory_candidate`, `check_rate_limit`, `fastapi`, `get_settings`, `logging`, `project_operator_bridge_list`, `project_operator_bridge_view`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_int`, `_final_envelope`, `_safe_brokerage`, `_safe_test_run_id`, `_scan_for_forbidden`, `bridge_memory_candidate_route`, `bridge_report_route`, `require_admin`

## Env-key candidates

`ADMIN`

## String constants (redacted where noted)

- "\nPAS182 — Operator adaptive-memory bridge routes.\n\nAdmin-only REST surface for the PAS182 manual-test → CANDIDATE\nmemory bridge. Mounted at ``/ops/learning``. Wraps\n``app.services.learning.adaptive_memory_bridge`` into 2 routes.\n\nDoctrine:\n\n* **Admin auth only** (X-Admin-Key) + PAS-SECURITY-04\n  operator rate limit.\n* **No live behaviour mutation.** The bridge writes a\n  CANDIDATE memory only — APPROVED is the Memory Review\n  console's job.\n* **Forbidden-token scanner** on every response.\n* **Audit-safe.** Confirmation + rejection both write a\n  PAS174 audit row via the bridge service.\n* **NEVER raises.**\n\nRoutes:\n\n    POST /ops/learning/manual-tests/{test_run_id}/bridge-memory-candidate\n    GET  /ops/learning/adaptive-memory/bridge-report\n"
- 'pas.ops.adaptive_memory'
- '/manual-tests/{test_run_id}/bridge-memory-candidate'
- '/adaptive-memory/bridge-report'
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
- 'operator_adaptive_memory surface='
- ' collapsed — forbidden token leaked'
- 'status'
- 'failed'
- 'error_code'
- 'ops_envelope_forbidden_token'
- 'warnings'
- 'value'
- 'int'
- 'default'
- 'test_run_id'
- 'body'
- 'Operator-initiated confirmation that a COMPLETED manual-\ntest run should bridge into a CANDIDATE memory record.\nRequires ``confirm=True`` in the body — anything else is\nrejected as ``bridge_rejected_by_operator``.'
- 'invalid test_run_id'
- 'actor_type'
- 'actor_id'
- 'confirm'
- 'ops.learning.adaptive_memory.bridge'
- 'record'
- 'operator_adaptive_memory bridge error type='
- 'unexpected:'
- 'brokerage_id'
- 'limit'
- 'Bounded paginated read of bridge activity. Operator\nprojection only — tenant callers MUST use the tenant route.'
- 'rows'
- 'skipped'
- 'ops.learning.adaptive_memory.bridge_report'
- 'count'
- 'operator_adaptive_memory report error type='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ("\nPAS182 — Operator adaptive-memory bridge routes.\n\nAdmin-only REST surface for the PAS182 manual-test → CANDIDATE\nmemory bridge. Mounted at ``/ops/learning``. Wraps\n``app.services.learning.adaptive_memory_bridge`` into 2 routes.\n\nDoctrine:\n\n* **Admin auth only** (X-Admin-Key) + PAS-SECURITY-04\n  operator rate limit.\n* **No live behaviour mutation.** The bridge writes a\n  CANDIDATE memory only — APPROVED is the Memory Review\n  console's job.\n* **Forbidden-token scanner** on every response.\n* **Audit-safe.** Confirmation + rejection both write a\n  PAS174 audit row via the bridge service.\n* **NEVER raises.**\n\nRoutes:\n\n    POST /ops/learning/manual-tests/{test_run_id}/bridge-memory-candidate\n    GET  /ops/learning/adaptive-memory/bridge-report\n")
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
              LOAD_CONST               3 (('Any', 'Dict', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (Optional)
              STORE_NAME               7 (Optional)
              POP_TOP

 31           LOAD_SMALL_INT           0
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

 33           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('get_settings',))
              IMPORT_NAME             15 (app.config)
              IMPORT_FROM             16 (get_settings)
              STORE_NAME              16 (get_settings)
              POP_TOP

 36           LOAD_NAME                9 (APIRouter)
              PUSH_NULL
              CALL                     0
              STORE_NAME              17 (router)

 37           LOAD_NAME                3 (logging)
              LOAD_ATTR               36 (getLogger)
              PUSH_NULL
              LOAD_CONST               6 ('pas.ops.adaptive_memory')
              CALL                     1
              STORE_NAME              19 (logger)

 40           LOAD_NAME               12 (Header)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              CALL                     1
              BUILD_TUPLE              1
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA2C40, file "app/routes/operator_adaptive_memory.py", line 40>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object require_admin at 0x0000018C179A7290, file "app/routes/operator_adaptive_memory.py", line 40>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              20 (require_admin)

 69           LOAD_SMALL_INT         200
              STORE_NAME              21 (_BROKERAGE_ID_MAX_LEN)

 70           LOAD_SMALL_INT         200
              STORE_NAME              22 (_TEST_RUN_ID_MAX_LEN)

 71           LOAD_SMALL_INT         200
              STORE_NAME              23 (_ACTOR_ID_MAX_LEN)

 72           LOAD_SMALL_INT          50
              STORE_NAME              24 (_LIST_LIMIT_DEFAULT)

 73           LOAD_CONST              10 (500)
              STORE_NAME              25 (_LIST_LIMIT_MAX)

 76           LOAD_CONST              28 (('phone', 'email', 'name_token', 'transcript', 'summary_text', 'raw_payload', 'raw_email', 'raw_body', 'secret', 'signature', 'dedupe_key', 'callback_notes', 'rationale_text', 'rationale_freeform', 'prompt_text', 'live_mutation_payload', 'evidence_raw'))
              STORE_NAME              26 (_FORBIDDEN_RESPONSE_TOKENS)

 86           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA34B0, file "app/routes/operator_adaptive_memory.py", line 86>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object _scan_for_forbidden at 0x0000018C18025C30, file "app/routes/operator_adaptive_memory.py", line 86>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_scan_for_forbidden)

110           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18025030, file "app/routes/operator_adaptive_memory.py", line 110>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object _final_envelope at 0x0000018C17FE1920, file "app/routes/operator_adaptive_memory.py", line 110>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_final_envelope)

126           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA3960, file "app/routes/operator_adaptive_memory.py", line 126>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _safe_brokerage at 0x0000018C17F95E60, file "app/routes/operator_adaptive_memory.py", line 126>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_safe_brokerage)

135           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA2970, file "app/routes/operator_adaptive_memory.py", line 135>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _safe_test_run_id at 0x0000018C17F95FD0, file "app/routes/operator_adaptive_memory.py", line 135>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_safe_test_run_id)

144           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18025A30, file "app/routes/operator_adaptive_memory.py", line 144>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _clamp_int at 0x0000018C18038670, file "app/routes/operator_adaptive_memory.py", line 144>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_clamp_int)

160           LOAD_NAME               17 (router)
              LOAD_ATTR               65 (post + NULL|self)
              LOAD_CONST              21 ('/manual-tests/{test_run_id}/bridge-memory-candidate')
              CALL                     1

163           LOAD_NAME               10 (Body)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              CALL                     1

164           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               20 (require_admin)
              CALL                     1

161           BUILD_TUPLE              2
              LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18024C30, file "app/routes/operator_adaptive_memory.py", line 161>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object bridge_memory_candidate_route at 0x0000018C17F4FB10, file "app/routes/operator_adaptive_memory.py", line 160>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

160           CALL                     0

161           STORE_NAME              33 (bridge_memory_candidate_route)

210           LOAD_NAME               17 (router)
              LOAD_ATTR               69 (get + NULL|self)
              LOAD_CONST              24 ('/adaptive-memory/bridge-report')
              CALL                     1

212           LOAD_NAME               14 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT         200
              LOAD_CONST              25 (('max_length',))
              CALL_KW                  2

213           LOAD_NAME               14 (Query)
              PUSH_NULL
              LOAD_NAME               24 (_LIST_LIMIT_DEFAULT)
              CALL                     1

214           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               20 (require_admin)
              CALL                     1

211           BUILD_TUPLE              3
              LOAD_CONST              26 (<code object __annotate__ at 0x0000018C18026330, file "app/routes/operator_adaptive_memory.py", line 211>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object bridge_report_route at 0x0000018C17D6DFC0, file "app/routes/operator_adaptive_memory.py", line 210>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

210           CALL                     0

211           STORE_NAME              35 (bridge_report_route)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app/routes/operator_adaptive_memory.py", line 40>:
 40           RESUME                   0
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

Disassembly of <code object require_admin at 0x0000018C179A7290, file "app/routes/operator_adaptive_memory.py", line 40>:
  40            RESUME                   0

  41            LOAD_GLOBAL              1 (get_settings + NULL)
                CALL                     0
                STORE_FAST               1 (settings)

  42            LOAD_FAST_BORROW         1 (settings)
                LOAD_ATTR                2 (ADMIN_API_KEY)
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (x_admin_key, settings)
                LOAD_ATTR                2 (ADMIN_API_KEY)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       14 (to L2)
                NOT_TAKEN

  43    L1:     LOAD_GLOBAL              5 (HTTPException + NULL)
                LOAD_CONST               0 (401)
                LOAD_CONST               1 ('Invalid admin key')
                LOAD_CONST               2 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

  46    L2:     NOP

  47    L3:     LOAD_SMALL_INT           0
                LOAD_CONST               3 (('check_rate_limit',))
                IMPORT_NAME              3 (app.services.security.rate_limit)
                IMPORT_FROM              4 (check_rate_limit)
                STORE_FAST               2 (check_rate_limit)
                POP_TOP

  48            LOAD_FAST_BORROW         2 (check_rate_limit)
                PUSH_NULL

  49            LOAD_CONST               4 ('admin')

  50            LOAD_CONST               5 ('ADMIN')

  51            LOAD_FAST_BORROW         0 (x_admin_key)

  48            LOAD_CONST               6 (('surface', 'actor_type', 'actor_token'))
                CALL_KW                  3
                STORE_FAST               3 (_rl_verdict)

  53            LOAD_FAST_BORROW         3 (_rl_verdict)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               7 ('allowed')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L6)
        L4:     NOT_TAKEN

  54    L5:     LOAD_GLOBAL              5 (HTTPException + NULL)

  55            LOAD_CONST               8 (429)

  56            LOAD_CONST               9 ('Operator rate limit exceeded. Retry after the current window.')

  54            LOAD_CONST               2 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

  53    L6:     NOP

  62            LOAD_CONST              10 (True)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  58            LOAD_GLOBAL              4 (HTTPException)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                POP_TOP

  59            RAISE_VARARGS            0

  60    L8:     LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L12)
        L9:     NOT_TAKEN
       L10:     POP_TOP

  61   L11:     POP_EXCEPT

  62            LOAD_CONST              10 (True)
                RETURN_VALUE

  60   L12:     RERAISE                  0

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L7 [0]
  L5 to L6 -> L7 [0]
  L7 to L9 -> L13 [1] lasti
  L10 to L11 -> L13 [1] lasti
  L12 to L13 -> L13 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app/routes/operator_adaptive_memory.py", line 86>:
 86           RESUME                   0
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

Disassembly of <code object _scan_for_forbidden at 0x0000018C18025C30, file "app/routes/operator_adaptive_memory.py", line 86>:
  --           MAKE_CELL                1 (walk)

  86           RESUME                   0

  87           LOAD_CONST               0 (<code object __annotate__ at 0x0000018C17FA3B40, file "app/routes/operator_adaptive_memory.py", line 87>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object walk at 0x0000018C17CC1CE0, file "app/routes/operator_adaptive_memory.py", line 87>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

 107           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app/routes/operator_adaptive_memory.py", line 87>:
 87           RESUME                   0
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

Disassembly of <code object walk at 0x0000018C17CC1CE0, file "app/routes/operator_adaptive_memory.py", line 87>:
  --            COPY_FREE_VARS           1

  87            RESUME                   0

  88            NOP

  89    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      111 (to L16)
        L2:     NOT_TAKEN

  90    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                88 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

  91            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L10)
                NOT_TAKEN

  92            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

  93            LOAD_GLOBAL             10 (_FORBIDDEN_RESPONSE_TOKENS)
                GET_ITER
        L5:     FOR_ITER                15 (to L9)
                STORE_FAST               4 (tok)

  94            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)

  95    L7:     LOAD_FAST_BORROW         4 (tok)
                SWAP                     2
                POP_TOP
                SWAP                     2
                POP_TOP
        L8:     RETURN_VALUE

  93    L9:     END_FOR
                POP_ITER

  96   L10:     LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

  97            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           86 (to L4)

  98   L12:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L13:     RETURN_VALUE

  90   L14:     END_FOR
                POP_ITER

 106   L15:     LOAD_CONST               0 (None)
                RETURN_VALUE

  99   L16:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             12 (list)
                LOAD_GLOBAL             14 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L22)
                NOT_TAKEN

 100            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L17:     FOR_ITER                23 (to L21)
                STORE_FAST               2 (v)

 101            LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 102            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           21 (to L17)

 103   L19:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L20:     RETURN_VALUE

 100   L21:     END_FOR
                POP_ITER

 106   L22:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 104            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L25)
                NOT_TAKEN
                POP_TOP

 105   L24:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 104   L25:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "app/routes/operator_adaptive_memory.py", line 110>:
110           RESUME                   0
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

Disassembly of <code object _final_envelope at 0x0000018C17FE1920, file "app/routes/operator_adaptive_memory.py", line 110>:
110           RESUME                   0

111           LOAD_GLOBAL              1 (_scan_for_forbidden + NULL)
              LOAD_FAST_BORROW         0 (env)
              CALL                     1
              STORE_FAST               2 (leak)

112           LOAD_FAST_BORROW         2 (leak)
              TO_BOOL
              POP_JUMP_IF_FALSE       37 (to L1)
              NOT_TAKEN

113           LOAD_GLOBAL              2 (logger)
              LOAD_ATTR                5 (warning + NULL|self)

114           LOAD_CONST               0 ('operator_adaptive_memory surface=')
              LOAD_FAST_BORROW         1 (surface)
              FORMAT_SIMPLE
              LOAD_CONST               1 (' collapsed — forbidden token leaked')
              BUILD_STRING             3

113           CALL                     1
              POP_TOP

118           LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('failed')

119           LOAD_CONST               4 ('surface')
              LOAD_FAST_BORROW         1 (surface)

120           LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('ops_envelope_forbidden_token')

121           LOAD_CONST               7 ('warnings')
              LOAD_CONST               6 ('ops_envelope_forbidden_token')
              BUILD_LIST               1

117           BUILD_MAP                4
              RETURN_VALUE

123   L1:     LOAD_FAST_BORROW         0 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app/routes/operator_adaptive_memory.py", line 126>:
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

Disassembly of <code object _safe_brokerage at 0x0000018C17F95E60, file "app/routes/operator_adaptive_memory.py", line 126>:
126           RESUME                   0

127           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

128           LOAD_CONST               0 (None)
              RETURN_VALUE

129   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

130           LOAD_FAST_BORROW         1 (s)
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

131   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

132   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app/routes/operator_adaptive_memory.py", line 135>:
135           RESUME                   0
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

Disassembly of <code object _safe_test_run_id at 0x0000018C17F95FD0, file "app/routes/operator_adaptive_memory.py", line 135>:
135           RESUME                   0

136           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

137           LOAD_CONST               0 (None)
              RETURN_VALUE

138   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

139           LOAD_FAST_BORROW         1 (s)
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

140   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

141   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app/routes/operator_adaptive_memory.py", line 144>:
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

Disassembly of <code object _clamp_int at 0x0000018C18038670, file "app/routes/operator_adaptive_memory.py", line 144>:
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

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app/routes/operator_adaptive_memory.py", line 161>:
161           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('test_run_id')

162           LOAD_CONST               2 ('str')

161           LOAD_CONST               3 ('body')

163           LOAD_CONST               4 ('Dict[str, Any]')

161           LOAD_CONST               5 ('return')

165           LOAD_CONST               4 ('Dict[str, Any]')

161           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object bridge_memory_candidate_route at 0x0000018C17F4FB10, file "app/routes/operator_adaptive_memory.py", line 160>:
 160            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 170            LOAD_GLOBAL              1 (_safe_test_run_id + NULL)
                LOAD_FAST_BORROW         0 (test_run_id)
                CALL                     1
                STORE_FAST               3 (trid)

 171            LOAD_FAST_BORROW         3 (trid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 172            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               2 (400)
                LOAD_CONST               3 ('invalid test_run_id')
                LOAD_CONST               4 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 173    L2:     LOAD_GLOBAL              5 (isinstance + NULL)
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

 174            LOAD_GLOBAL              5 (isinstance + NULL)
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

 175            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (body)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       27 (to L7)
                NOT_TAKEN
                LOAD_GLOBAL             11 (bool + NULL)
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               7 ('confirm')
                CALL                     1
                CALL                     1
                JUMP_FORWARD             1 (to L8)
        L7:     LOAD_CONST               8 (False)
        L8:     STORE_FAST               6 (confirm)

 176            LOAD_SMALL_INT           0
                LOAD_CONST               9 (('bridge_to_memory_candidate',))
                IMPORT_NAME              6 (app.services.learning.adaptive_memory_bridge)
                IMPORT_FROM              7 (bridge_to_memory_candidate)
                STORE_FAST               7 (bridge_to_memory_candidate)
                POP_TOP

 179            LOAD_SMALL_INT           0
                LOAD_CONST              10 (('project_operator_bridge_view',))
                IMPORT_NAME              8 (app.services.learning.adaptive_memory_projection)
                IMPORT_FROM              9 (project_operator_bridge_view)
                STORE_FAST               8 (project_operator_bridge_view)
                POP_TOP

 182    L9:     NOP

 183   L10:     LOAD_FAST                7 (bridge_to_memory_candidate)
                PUSH_NULL

 184            LOAD_FAST                3 (trid)

 185            LOAD_CONST               1 (None)

 186            LOAD_FAST                4 (actor_type)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                LOAD_CONST              11 ('')

 187   L13:     LOAD_FAST_BORROW         5 (actor_id)

 188            LOAD_FAST_BORROW         6 (confirm)

 183            LOAD_CONST              12 (('test_run_id', 'brokerage_id', 'actor_type', 'actor_id', 'confirm'))
                CALL_KW                  5
                STORE_FAST               9 (result)

 191            LOAD_CONST              13 ('status')
                LOAD_FAST_BORROW         9 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              13 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
       L14:     NOT_TAKEN
       L15:     POP_TOP
                LOAD_CONST              14 ('failed')

 192   L16:     LOAD_CONST              15 ('surface')
                LOAD_CONST              16 ('ops.learning.adaptive_memory.bridge')

 193            LOAD_CONST              17 ('record')
                LOAD_FAST_BORROW         8 (project_operator_bridge_view)
                PUSH_NULL
                LOAD_FAST_BORROW         9 (result)
                CALL                     1

 194            LOAD_CONST              18 ('warnings')
                LOAD_GLOBAL             21 (list + NULL)
                LOAD_FAST_BORROW         9 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              18 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L19)
       L17:     NOT_TAKEN
       L18:     POP_TOP
                BUILD_LIST               0
       L19:     CALL                     1

 195            LOAD_CONST              19 ('error_code')
                LOAD_FAST_BORROW         9 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              19 ('error_code')
                CALL                     1

 190            BUILD_MAP                5
                STORE_FAST              10 (env)

 207   L20:     LOAD_GLOBAL             33 (_final_envelope + NULL)
                LOAD_FAST_BORROW        10 (env)
                LOAD_CONST              16 ('ops.learning.adaptive_memory.bridge')
                LOAD_CONST              22 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L21:     PUSH_EXC_INFO

 197            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L25)
                NOT_TAKEN
                STORE_FAST              11 (e)

 198   L22:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 199            LOAD_CONST              20 ('operator_adaptive_memory bridge error type=')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 198            CALL                     1
                POP_TOP

 202            LOAD_CONST              13 ('status')
                LOAD_CONST              14 ('failed')

 203            LOAD_CONST              15 ('surface')
                LOAD_CONST              16 ('ops.learning.adaptive_memory.bridge')

 204            LOAD_CONST              19 ('error_code')
                LOAD_CONST              21 ('unexpected:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 205            LOAD_CONST              18 ('warnings')
                BUILD_LIST               0

 201            BUILD_MAP                4
                STORE_FAST              10 (env)
       L23:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L20)

  --   L24:     LOAD_CONST               1 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 197   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L27:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L9 -> L27 [0] lasti
  L10 to L11 -> L21 [0]
  L12 to L14 -> L21 [0]
  L15 to L17 -> L21 [0]
  L18 to L20 -> L21 [0]
  L20 to L21 -> L27 [0] lasti
  L21 to L22 -> L26 [1] lasti
  L22 to L23 -> L24 [1] lasti
  L23 to L24 -> L27 [0] lasti
  L24 to L26 -> L26 [1] lasti
  L26 to L27 -> L27 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026330, file "app/routes/operator_adaptive_memory.py", line 211>:
211           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

212           LOAD_CONST               2 ('Optional[str]')

211           LOAD_CONST               3 ('limit')

213           LOAD_CONST               4 ('int')

211           LOAD_CONST               5 ('return')

215           LOAD_CONST               6 ('Dict[str, Any]')

211           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object bridge_report_route at 0x0000018C17D6DFC0, file "app/routes/operator_adaptive_memory.py", line 210>:
 210            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 218            LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               1 (None)
        L3:     STORE_FAST               3 (bid)

 219            LOAD_GLOBAL              3 (_clamp_int + NULL)
                LOAD_FAST_BORROW         1 (limit)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              4 (_LIST_LIMIT_MAX)
                LOAD_GLOBAL              6 (_LIST_LIMIT_DEFAULT)
                CALL                     4
                STORE_FAST               4 (capped)

 220            LOAD_SMALL_INT           0
                LOAD_CONST               2 (('adaptive_memory_bridge_report',))
                IMPORT_NAME              4 (app.services.learning.adaptive_memory_bridge)
                IMPORT_FROM              5 (adaptive_memory_bridge_report)
                STORE_FAST               5 (adaptive_memory_bridge_report)
                POP_TOP

 223            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('project_operator_bridge_list',))
                IMPORT_NAME              6 (app.services.learning.adaptive_memory_projection)
                IMPORT_FROM              7 (project_operator_bridge_list)
                STORE_FAST               6 (project_operator_bridge_list)
                POP_TOP

 226    L4:     NOP

 227    L5:     LOAD_FAST_BORROW         5 (adaptive_memory_bridge_report)
                PUSH_NULL

 228            LOAD_FAST_BORROW         3 (bid)

 229            LOAD_FAST_BORROW         4 (capped)

 227            LOAD_CONST               4 (('brokerage_id', 'limit'))
                CALL_KW                  2
                STORE_FAST               7 (result)

 231            LOAD_FAST                6 (project_operator_bridge_list)
                PUSH_NULL
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               5 ('rows')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                BUILD_LIST               0
        L8:     CALL                     1
                STORE_FAST               8 (rows)

 233            LOAD_CONST               6 ('status')
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               6 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                LOAD_CONST               7 ('skipped')

 234   L11:     LOAD_CONST               8 ('surface')
                LOAD_CONST               9 ('ops.learning.adaptive_memory.bridge_report')

 235            LOAD_CONST               5 ('rows')
                LOAD_FAST                8 (rows)

 236            LOAD_CONST              10 ('count')
                LOAD_GLOBAL             19 (len + NULL)
                LOAD_FAST_BORROW         8 (rows)
                CALL                     1

 237            LOAD_CONST              11 ('warnings')
                LOAD_GLOBAL             21 (list + NULL)
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              11 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
       L12:     NOT_TAKEN
       L13:     POP_TOP
                BUILD_LIST               0
       L14:     CALL                     1

 238            LOAD_CONST              12 ('error_code')
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('error_code')
                CALL                     1

 232            BUILD_MAP                6
                STORE_FAST               9 (env)

 250   L15:     LOAD_GLOBAL             33 (_final_envelope + NULL)
                LOAD_FAST_BORROW         9 (env)
                LOAD_CONST               9 ('ops.learning.adaptive_memory.bridge_report')
                LOAD_CONST              16 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L16:     PUSH_EXC_INFO

 240            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L20)
                NOT_TAKEN
                STORE_FAST              10 (e)

 241   L17:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 242            LOAD_CONST              13 ('operator_adaptive_memory report error type=')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 241            CALL                     1
                POP_TOP

 245            LOAD_CONST               6 ('status')
                LOAD_CONST              14 ('failed')

 246            LOAD_CONST               8 ('surface')
                LOAD_CONST               9 ('ops.learning.adaptive_memory.bridge_report')

 247            LOAD_CONST              12 ('error_code')
                LOAD_CONST              15 ('unexpected:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 248            LOAD_CONST              11 ('warnings')
                BUILD_LIST               0

 244            BUILD_MAP                4
                STORE_FAST               9 (env)
       L18:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L15)

  --   L19:     LOAD_CONST               1 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 240   L20:     RERAISE                  0

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
