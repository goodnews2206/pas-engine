# routes/operator_learning_dashboard

- **pyc:** `app\routes\__pycache__\operator_learning_dashboard.cpython-314.pyc`
- **expected source path (absent):** `app\routes/operator_learning_dashboard.py`
- **co_filename (from bytecode):** `app\routes\operator_learning_dashboard.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** routes

## Module docstring

```
PAS184 — Operator learning unified dashboard (read-only).

Aggregates PAS179/PAS180 recommendations + PAS181 manual-test runs
+ PAS182 adaptive-memory bridge activity into a single read-only
operator envelope. Mounted at ``/ops/learning``.

Doctrine:

* **Read-only.** ``GET`` only. No mutation surface — the three
  underlying surfaces (PAS180 / PAS181 / PAS182) remain
  authoritative for any state transition.
* **Admin auth only** (X-Admin-Key) + PAS-SECURITY-04 operator
  rate limit.
* **Existing closed projections.** This module imports the
  service-layer helpers (``manual_test_run_report``,
  ``adaptive_memory_bridge_report``) plus the existing
  projection functions and assembles the response — it does
  NOT define new projection allow-lists or any new payload
  shape.
* **No new payload keys beyond the underlying surfaces' allow-lists.**
* **Forbidden-token scanner** on the final envelope.
* **NEVER raises.**

Route:

    GET /ops/learning/dashboard
```

## Imports

`APIRouter`, `Any`, `Depends`, `Dict`, `HTTPException`, `Header`, `Optional`, `Query`, `__future__`, `adaptive_memory_bridge_report`, `annotations`, `app.config`, `app.services.learning.adaptive_memory_bridge`, `app.services.learning.adaptive_memory_projection`, `app.services.learning.manual_test_harness`, `app.services.learning.recommendation_projection`, `app.services.learning.recommendation_review`, `app.services.security.rate_limit`, `check_rate_limit`, `fastapi`, `get_settings`, `list_learning_recommendations`, `logging`, `manual_test_run_report`, `project_operator_bridge_list`, `project_operator_list`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_int`, `_final_envelope`, `_safe_brokerage`, `_safe_section`, `_scan_for_forbidden`, `operator_learning_dashboard`, `require_admin`

## Env-key candidates

`ADMIN`

## String constants (redacted where noted)

- "\nPAS184 — Operator learning unified dashboard (read-only).\n\nAggregates PAS179/PAS180 recommendations + PAS181 manual-test runs\n+ PAS182 adaptive-memory bridge activity into a single read-only\noperator envelope. Mounted at ``/ops/learning``.\n\nDoctrine:\n\n* **Read-only.** ``GET`` only. No mutation surface — the three\n  underlying surfaces (PAS180 / PAS181 / PAS182) remain\n  authoritative for any state transition.\n* **Admin auth only** (X-Admin-Key) + PAS-SECURITY-04 operator\n  rate limit.\n* **Existing closed projections.** This module imports the\n  service-layer helpers (``manual_test_run_report``,\n  ``adaptive_memory_bridge_report``) plus the existing\n  projection functions and assembles the response — it does\n  NOT define new projection allow-lists or any new payload\n  shape.\n* **No new payload keys beyond the underlying surfaces' allow-lists.**\n* **Forbidden-token scanner** on the final envelope.\n* **NEVER raises.**\n\nRoute:\n\n    GET /ops/learning/dashboard\n"
- 'pas.ops.learning_dashboard'
- '/dashboard'
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
- 'operator_learning_dashboard surface='
- ' collapsed — forbidden token leaked'
- 'status'
- 'failed'
- 'error_code'
- 'ops_envelope_forbidden_token'
- 'warnings'
- 'value'
- 'int'
- 'default'
- 'label'
- 'Call the underlying service helper and fold its envelope\ninto a uniform `{label, status, count, rows, error_code,\nwarnings}` shape. NEVER raises.'
- 'operator_learning_dashboard section='
- ' error type='
- 'count'
- 'rows'
- 'unexpected:'
- 'invalid_section_envelope'
- 'skipped'
- 'brokerage_id'
- 'limit'
- 'Unified read-only operator view across PAS180 recommendations\n+ PAS181 manual-test runs + PAS182 adaptive-memory bridge.\n\nThe route does NOT define new payload keys — it composes the\nclosed envelopes returned by the underlying service helpers\nand re-runs the forbidden-token scanner over the final\ncomposition.'
- 'operator_learning_dashboard imports failed type='
- 'operator_learning_dashboard manual_test_harness import failed type='
- 'operator_learning_dashboard adaptive_memory imports failed type='
- 'learning.recommendations'
- 'recommendation_review_unavailable'
- 'operator_learning_dashboard recommendations projection error type='
- 'projection_failed:'
- 'learning.manual_tests'
- 'manual_test_harness_unavailable'
- 'learning.adaptive_memory_bridge'
- 'adaptive_memory_bridge_unavailable'
- 'operator_learning_dashboard bridge projection error type='
- 'ops.learning.dashboard'
- 'sections'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ("\nPAS184 — Operator learning unified dashboard (read-only).\n\nAggregates PAS179/PAS180 recommendations + PAS181 manual-test runs\n+ PAS182 adaptive-memory bridge activity into a single read-only\noperator envelope. Mounted at ``/ops/learning``.\n\nDoctrine:\n\n* **Read-only.** ``GET`` only. No mutation surface — the three\n  underlying surfaces (PAS180 / PAS181 / PAS182) remain\n  authoritative for any state transition.\n* **Admin auth only** (X-Admin-Key) + PAS-SECURITY-04 operator\n  rate limit.\n* **Existing closed projections.** This module imports the\n  service-layer helpers (``manual_test_run_report``,\n  ``adaptive_memory_bridge_report``) plus the existing\n  projection functions and assembles the response — it does\n  NOT define new projection allow-lists or any new payload\n  shape.\n* **No new payload keys beyond the underlying surfaces' allow-lists.**\n* **Forbidden-token scanner** on the final envelope.\n* **NEVER raises.**\n\nRoute:\n\n    GET /ops/learning/dashboard\n")
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

 37           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('get_settings',))
              IMPORT_NAME             14 (app.config)
              IMPORT_FROM             15 (get_settings)
              STORE_NAME              15 (get_settings)
              POP_TOP

 40           LOAD_NAME                9 (APIRouter)
              PUSH_NULL
              CALL                     0
              STORE_NAME              16 (router)

 41           LOAD_NAME                3 (logging)
              LOAD_ATTR               34 (getLogger)
              PUSH_NULL
              LOAD_CONST               6 ('pas.ops.learning_dashboard')
              CALL                     1
              STORE_NAME              18 (logger)

 44           LOAD_NAME               11 (Header)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              CALL                     1
              BUILD_TUPLE              1
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA3A50, file "app\routes\operator_learning_dashboard.py", line 44>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object require_admin at 0x0000018C1801C410, file "app\routes\operator_learning_dashboard.py", line 44>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              19 (require_admin)

 69           LOAD_SMALL_INT         200
              STORE_NAME              20 (_BROKERAGE_ID_MAX_LEN)

 70           LOAD_SMALL_INT          25
              STORE_NAME              21 (_LIST_LIMIT_DEFAULT)

 71           LOAD_SMALL_INT         100
              STORE_NAME              22 (_LIST_LIMIT_MAX)

 74           LOAD_CONST              24 (('phone', 'email', 'name_token', 'transcript', 'summary_text', 'raw_payload', 'raw_email', 'raw_body', 'secret', 'signature', 'dedupe_key', 'callback_notes', 'rationale_text', 'rationale_freeform', 'prompt_text', 'live_mutation_payload', 'evidence_raw'))
              STORE_NAME              23 (_FORBIDDEN_RESPONSE_TOKENS)

 84           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA2A60, file "app\routes\operator_learning_dashboard.py", line 84>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _scan_for_forbidden at 0x0000018C18026130, file "app\routes\operator_learning_dashboard.py", line 84>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_scan_for_forbidden)

108           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C18025730, file "app\routes\operator_learning_dashboard.py", line 108>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _final_envelope at 0x0000018C17FE1530, file "app\routes\operator_learning_dashboard.py", line 108>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_final_envelope)

124           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA33C0, file "app\routes\operator_learning_dashboard.py", line 124>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _safe_brokerage at 0x0000018C17F96420, file "app\routes\operator_learning_dashboard.py", line 124>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_safe_brokerage)

133           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18025E30, file "app\routes\operator_learning_dashboard.py", line 133>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _clamp_int at 0x0000018C18038B70, file "app\routes\operator_learning_dashboard.py", line 133>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_clamp_int)

145           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA35A0, file "app\routes\operator_learning_dashboard.py", line 145>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object _safe_section at 0x0000018C183252E0, file "app\routes\operator_learning_dashboard.py", line 145>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_safe_section)

184           LOAD_NAME               16 (router)
              LOAD_ATTR               59 (get + NULL|self)
              LOAD_CONST              20 ('/dashboard')
              CALL                     1

186           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT         200
              LOAD_CONST              21 (('max_length',))
              CALL_KW                  2

187           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_NAME               21 (_LIST_LIMIT_DEFAULT)
              CALL                     1

188           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               19 (require_admin)
              CALL                     1

185           BUILD_TUPLE              3
              LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18025D30, file "app\routes\operator_learning_dashboard.py", line 185>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object operator_learning_dashboard at 0x0000018C17F69310, file "app\routes\operator_learning_dashboard.py", line 184>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

184           CALL                     0

185           STORE_NAME              30 (operator_learning_dashboard)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app\routes\operator_learning_dashboard.py", line 44>:
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

Disassembly of <code object require_admin at 0x0000018C1801C410, file "app\routes\operator_learning_dashboard.py", line 44>:
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app\routes\operator_learning_dashboard.py", line 84>:
 84           RESUME                   0
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

Disassembly of <code object _scan_for_forbidden at 0x0000018C18026130, file "app\routes\operator_learning_dashboard.py", line 84>:
  --           MAKE_CELL                1 (walk)

  84           RESUME                   0

  85           LOAD_CONST               0 (<code object __annotate__ at 0x0000018C17FA3000, file "app\routes\operator_learning_dashboard.py", line 85>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object walk at 0x0000018C17CC2960, file "app\routes\operator_learning_dashboard.py", line 85>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

 105           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "app\routes\operator_learning_dashboard.py", line 85>:
 85           RESUME                   0
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

Disassembly of <code object walk at 0x0000018C17CC2960, file "app\routes\operator_learning_dashboard.py", line 85>:
  --            COPY_FREE_VARS           1

  85            RESUME                   0

  86            NOP

  87    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      111 (to L16)
        L2:     NOT_TAKEN

  88    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                88 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

  89            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L10)
                NOT_TAKEN

  90            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

  91            LOAD_GLOBAL             10 (_FORBIDDEN_RESPONSE_TOKENS)
                GET_ITER
        L5:     FOR_ITER                15 (to L9)
                STORE_FAST               4 (tok)

  92            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)

  93    L7:     LOAD_FAST_BORROW         4 (tok)
                SWAP                     2
                POP_TOP
                SWAP                     2
                POP_TOP
        L8:     RETURN_VALUE

  91    L9:     END_FOR
                POP_ITER

  94   L10:     LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

  95            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           86 (to L4)

  96   L12:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L13:     RETURN_VALUE

  88   L14:     END_FOR
                POP_ITER

 104   L15:     LOAD_CONST               0 (None)
                RETURN_VALUE

  97   L16:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             12 (list)
                LOAD_GLOBAL             14 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L22)
                NOT_TAKEN

  98            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L17:     FOR_ITER                23 (to L21)
                STORE_FAST               2 (v)

  99            LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 100            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           21 (to L17)

 101   L19:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L20:     RETURN_VALUE

  98   L21:     END_FOR
                POP_ITER

 104   L22:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 102            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L25)
                NOT_TAKEN
                POP_TOP

 103   L24:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 102   L25:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app\routes\operator_learning_dashboard.py", line 108>:
108           RESUME                   0
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

Disassembly of <code object _final_envelope at 0x0000018C17FE1530, file "app\routes\operator_learning_dashboard.py", line 108>:
108           RESUME                   0

109           LOAD_GLOBAL              1 (_scan_for_forbidden + NULL)
              LOAD_FAST_BORROW         0 (env)
              CALL                     1
              STORE_FAST               2 (leak)

110           LOAD_FAST_BORROW         2 (leak)
              TO_BOOL
              POP_JUMP_IF_FALSE       37 (to L1)
              NOT_TAKEN

111           LOAD_GLOBAL              2 (logger)
              LOAD_ATTR                5 (warning + NULL|self)

112           LOAD_CONST               0 ('operator_learning_dashboard surface=')
              LOAD_FAST_BORROW         1 (surface)
              FORMAT_SIMPLE
              LOAD_CONST               1 (' collapsed — forbidden token leaked')
              BUILD_STRING             3

111           CALL                     1
              POP_TOP

116           LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('failed')

117           LOAD_CONST               4 ('surface')
              LOAD_FAST_BORROW         1 (surface)

118           LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('ops_envelope_forbidden_token')

119           LOAD_CONST               7 ('warnings')
              LOAD_CONST               6 ('ops_envelope_forbidden_token')
              BUILD_LIST               1

115           BUILD_MAP                4
              RETURN_VALUE

121   L1:     LOAD_FAST_BORROW         0 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app\routes\operator_learning_dashboard.py", line 124>:
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

Disassembly of <code object _safe_brokerage at 0x0000018C17F96420, file "app\routes\operator_learning_dashboard.py", line 124>:
124           RESUME                   0

125           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

126           LOAD_CONST               0 (None)
              RETURN_VALUE

127   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

128           LOAD_FAST_BORROW         1 (s)
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

129   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

130   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app\routes\operator_learning_dashboard.py", line 133>:
133           RESUME                   0
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

Disassembly of <code object _clamp_int at 0x0000018C18038B70, file "app\routes\operator_learning_dashboard.py", line 133>:
 133           RESUME                   0

 134           NOP

 135   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

 138   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 139           LOAD_FAST                1 (lo)
               RETURN_VALUE

 140   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 141           LOAD_FAST                2 (hi)
               RETURN_VALUE

 142   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 136           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

 137           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 136   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app\routes\operator_learning_dashboard.py", line 145>:
145           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('label')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_section at 0x0000018C183252E0, file "app\routes\operator_learning_dashboard.py", line 145>:
 145            RESUME                   0

 149            NOP

 150    L1:     LOAD_FAST_BORROW         0 (callable_)
                PUSH_NULL
                LOAD_CONST              14 (())
                BUILD_MAP                0
                LOAD_FAST_BORROW         2 (kwargs)
                DICT_MERGE               1
                CALL_FUNCTION_EX
                STORE_FAST               3 (out)

 164    L2:     LOAD_GLOBAL             11 (isinstance + NULL)
                LOAD_FAST                3 (out)
                LOAD_GLOBAL             12 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L3)
                NOT_TAKEN

 166            LOAD_CONST               3 ('label')
                LOAD_FAST                1 (label)

 167            LOAD_CONST               4 ('status')
                LOAD_CONST               5 ('failed')

 168            LOAD_CONST               6 ('count')
                LOAD_SMALL_INT           0

 169            LOAD_CONST               7 ('rows')
                BUILD_LIST               0

 170            LOAD_CONST               8 ('error_code')
                LOAD_CONST              12 ('invalid_section_envelope')

 171            LOAD_CONST              10 ('warnings')
                BUILD_LIST               0

 165            BUILD_MAP                6
                RETURN_VALUE

 173    L3:     LOAD_GLOBAL             11 (isinstance + NULL)
                LOAD_FAST                3 (out)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               7 ('rows')
                CALL                     1
                LOAD_GLOBAL             16 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L4)
                NOT_TAKEN
                LOAD_FAST                3 (out)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               7 ('rows')
                CALL                     1
                JUMP_FORWARD             1 (to L5)
        L4:     BUILD_LIST               0
        L5:     STORE_FAST               5 (rows)

 175            LOAD_CONST               3 ('label')
                LOAD_FAST                1 (label)

 176            LOAD_CONST               4 ('status')
                LOAD_FAST                3 (out)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               4 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              13 ('skipped')

 177    L6:     LOAD_CONST               6 ('count')
                LOAD_GLOBAL             19 (int + NULL)
                LOAD_FAST                3 (out)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               6 ('count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L7)
                NOT_TAKEN
                POP_TOP
                LOAD_GLOBAL             21 (len + NULL)
                LOAD_FAST                5 (rows)
                CALL                     1
        L7:     CALL                     1

 178            LOAD_CONST               7 ('rows')
                LOAD_FAST                5 (rows)

 179            LOAD_CONST               8 ('error_code')
                LOAD_FAST                3 (out)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               8 ('error_code')
                CALL                     1

 180            LOAD_CONST              10 ('warnings')
                LOAD_GLOBAL             17 (list + NULL)
                LOAD_FAST                3 (out)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              10 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L8:     CALL                     1

 174            BUILD_MAP                6
                RETURN_VALUE

  --    L9:     PUSH_EXC_INFO

 151            LOAD_GLOBAL              0 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       93 (to L14)
                NOT_TAKEN
                STORE_FAST               4 (e)

 152   L10:     LOAD_GLOBAL              2 (logger)
                LOAD_ATTR                5 (warning + NULL|self)

 153            LOAD_CONST               1 ('operator_learning_dashboard section=')
                LOAD_FAST                1 (label)
                FORMAT_SIMPLE
                LOAD_CONST               2 (' error type=')

 154            LOAD_GLOBAL              7 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR                8 (__name__)
                FORMAT_SIMPLE

 153            BUILD_STRING             4

 152            CALL                     1
                POP_TOP

 157            LOAD_CONST               3 ('label')
                LOAD_FAST                1 (label)

 158            LOAD_CONST               4 ('status')
                LOAD_CONST               5 ('failed')

 159            LOAD_CONST               6 ('count')
                LOAD_SMALL_INT           0

 160            LOAD_CONST               7 ('rows')
                BUILD_LIST               0

 161            LOAD_CONST               8 ('error_code')
                LOAD_CONST               9 ('unexpected:')
                LOAD_GLOBAL              7 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR                8 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 162            LOAD_CONST              10 ('warnings')
                BUILD_LIST               0

 156            BUILD_MAP                6
       L11:     SWAP                     2
       L12:     POP_EXCEPT
                LOAD_CONST              11 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RETURN_VALUE

  --   L13:     LOAD_CONST              11 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 151   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L9 [0]
  L9 to L10 -> L15 [1] lasti
  L10 to L11 -> L13 [1] lasti
  L11 to L12 -> L15 [1] lasti
  L13 to L15 -> L15 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\routes\operator_learning_dashboard.py", line 185>:
185           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

186           LOAD_CONST               2 ('Optional[str]')

185           LOAD_CONST               3 ('limit')

187           LOAD_CONST               4 ('int')

185           LOAD_CONST               5 ('return')

189           LOAD_CONST               6 ('Dict[str, Any]')

185           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object operator_learning_dashboard at 0x0000018C17F69310, file "app\routes\operator_learning_dashboard.py", line 184>:
 184            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 197            LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               1 (None)
        L3:     STORE_FAST               3 (bid)

 198            LOAD_GLOBAL              3 (_clamp_int + NULL)
                LOAD_FAST_BORROW         1 (limit)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              4 (_LIST_LIMIT_MAX)
                LOAD_GLOBAL              6 (_LIST_LIMIT_DEFAULT)
                CALL                     4
                STORE_FAST               4 (capped)

 202    L4:     NOP

 203    L5:     LOAD_SMALL_INT           0
                LOAD_CONST               2 (('list_learning_recommendations',))
                IMPORT_NAME              4 (app.services.learning.recommendation_review)
                IMPORT_FROM              5 (list_learning_recommendations)
                STORE_FAST               5 (list_learning_recommendations)
                POP_TOP

 206            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('project_operator_list',))
                IMPORT_NAME              6 (app.services.learning.recommendation_projection)
                IMPORT_FROM              7 (project_operator_list)
                STORE_FAST               6 (project_operator_list)
                POP_TOP

 216    L6:     NOP

 217    L7:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('manual_test_run_report',))
                IMPORT_NAME             13 (app.services.learning.manual_test_harness)
                IMPORT_FROM             14 (manual_test_run_report)
                STORE_FAST               8 (manual_test_run_report)
                POP_TOP

 226    L8:     NOP

 227    L9:     LOAD_SMALL_INT           0
                LOAD_CONST               7 (('adaptive_memory_bridge_report',))
                IMPORT_NAME             15 (app.services.learning.adaptive_memory_bridge)
                IMPORT_FROM             16 (adaptive_memory_bridge_report)
                STORE_FAST               9 (adaptive_memory_bridge_report)
                POP_TOP

 230            LOAD_SMALL_INT           0
                LOAD_CONST               8 (('project_operator_bridge_list',))
                IMPORT_NAME             17 (app.services.learning.adaptive_memory_projection)
                IMPORT_FROM             18 (project_operator_bridge_list)
                STORE_FAST              10 (project_operator_bridge_list)
                POP_TOP

 242   L10:     LOAD_FAST_BORROW         5 (list_learning_recommendations)
                POP_JUMP_IF_NOT_NONE    17 (to L11)
                NOT_TAKEN

 244            LOAD_CONST              10 ('label')
                LOAD_CONST              11 ('learning.recommendations')

 245            LOAD_CONST              12 ('status')
                LOAD_CONST              13 ('skipped')

 246            LOAD_CONST              14 ('count')
                LOAD_SMALL_INT           0

 247            LOAD_CONST              15 ('rows')
                BUILD_LIST               0

 248            LOAD_CONST              16 ('error_code')
                LOAD_CONST              17 ('recommendation_review_unavailable')

 249            LOAD_CONST              18 ('warnings')
                LOAD_CONST              17 ('recommendation_review_unavailable')
                BUILD_LIST               1

 243            BUILD_MAP                6
                STORE_FAST              11 (recommendations_section)
                JUMP_FORWARD            74 (to L14)

 252   L11:     LOAD_GLOBAL             39 (_safe_section + NULL)

 253            LOAD_FAST_BORROW         5 (list_learning_recommendations)

 254            LOAD_CONST              11 ('learning.recommendations')

 255            LOAD_FAST_BORROW         3 (bid)

 256            LOAD_FAST_BORROW         4 (capped)

 252            LOAD_CONST              19 (('label', 'brokerage_id', 'limit'))
                CALL_KW                  4
                STORE_FAST              11 (recommendations_section)

 258            LOAD_FAST_BORROW         6 (project_operator_list)
                POP_JUMP_IF_NONE        56 (to L14)
                NOT_TAKEN
                LOAD_FAST_BORROW        11 (recommendations_section)
                LOAD_CONST              15 ('rows')
                BINARY_OP               26 ([])
                TO_BOOL
                POP_JUMP_IF_FALSE       41 (to L14)
       L12:     NOT_TAKEN

 259            NOP

 260   L13:     LOAD_FAST_BORROW         6 (project_operator_list)
                PUSH_NULL

 261            LOAD_FAST_BORROW        11 (recommendations_section)
                LOAD_CONST              15 ('rows')
                BINARY_OP               26 ([])

 260            CALL                     1
                LOAD_FAST_BORROW        11 (recommendations_section)
                LOAD_CONST              15 ('rows')
                STORE_SUBSCR

 263            LOAD_GLOBAL             41 (len + NULL)
                LOAD_FAST_BORROW        11 (recommendations_section)
                LOAD_CONST              15 ('rows')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_FAST_BORROW        11 (recommendations_section)
                LOAD_CONST              14 ('count')
                STORE_SUBSCR

 276   L14:     LOAD_FAST_BORROW         8 (manual_test_run_report)
                POP_JUMP_IF_NOT_NONE    17 (to L15)
                NOT_TAKEN

 278            LOAD_CONST              10 ('label')
                LOAD_CONST              22 ('learning.manual_tests')

 279            LOAD_CONST              12 ('status')
                LOAD_CONST              13 ('skipped')

 280            LOAD_CONST              14 ('count')
                LOAD_SMALL_INT           0

 281            LOAD_CONST              15 ('rows')
                BUILD_LIST               0

 282            LOAD_CONST              16 ('error_code')
                LOAD_CONST              23 ('manual_test_harness_unavailable')

 283            LOAD_CONST              18 ('warnings')
                LOAD_CONST              23 ('manual_test_harness_unavailable')
                BUILD_LIST               1

 277            BUILD_MAP                6
                STORE_FAST              12 (manual_tests_section)
                JUMP_FORWARD            15 (to L16)

 286   L15:     LOAD_GLOBAL             39 (_safe_section + NULL)

 287            LOAD_FAST_BORROW         8 (manual_test_run_report)

 288            LOAD_CONST              22 ('learning.manual_tests')

 289            LOAD_FAST_BORROW         3 (bid)

 290            LOAD_FAST_BORROW         4 (capped)

 286            LOAD_CONST              19 (('label', 'brokerage_id', 'limit'))
                CALL_KW                  4
                STORE_FAST              12 (manual_tests_section)

 294   L16:     LOAD_FAST_BORROW         9 (adaptive_memory_bridge_report)
                POP_JUMP_IF_NOT_NONE    17 (to L17)
                NOT_TAKEN

 296            LOAD_CONST              10 ('label')
                LOAD_CONST              24 ('learning.adaptive_memory_bridge')

 297            LOAD_CONST              12 ('status')
                LOAD_CONST              13 ('skipped')

 298            LOAD_CONST              14 ('count')
                LOAD_SMALL_INT           0

 299            LOAD_CONST              15 ('rows')
                BUILD_LIST               0

 300            LOAD_CONST              16 ('error_code')
                LOAD_CONST              25 ('adaptive_memory_bridge_unavailable')

 301            LOAD_CONST              18 ('warnings')
                LOAD_CONST              25 ('adaptive_memory_bridge_unavailable')
                BUILD_LIST               1

 295            BUILD_MAP                6
                STORE_FAST              13 (bridge_section)
                JUMP_FORWARD            74 (to L20)

 304   L17:     LOAD_GLOBAL             39 (_safe_section + NULL)

 305            LOAD_FAST_BORROW         9 (adaptive_memory_bridge_report)

 306            LOAD_CONST              24 ('learning.adaptive_memory_bridge')

 307            LOAD_FAST_BORROW         3 (bid)

 308            LOAD_FAST_BORROW         4 (capped)

 304            LOAD_CONST              19 (('label', 'brokerage_id', 'limit'))
                CALL_KW                  4
                STORE_FAST              13 (bridge_section)

 310            LOAD_FAST_BORROW        10 (project_operator_bridge_list)
                POP_JUMP_IF_NONE        56 (to L20)
                NOT_TAKEN
                LOAD_FAST_BORROW        13 (bridge_section)
                LOAD_CONST              15 ('rows')
                BINARY_OP               26 ([])
                TO_BOOL
                POP_JUMP_IF_FALSE       41 (to L20)
       L18:     NOT_TAKEN

 311            NOP

 312   L19:     LOAD_FAST_BORROW        10 (project_operator_bridge_list)
                PUSH_NULL

 313            LOAD_FAST_BORROW        13 (bridge_section)
                LOAD_CONST              15 ('rows')
                BINARY_OP               26 ([])

 312            CALL                     1
                LOAD_FAST_BORROW        13 (bridge_section)
                LOAD_CONST              15 ('rows')
                STORE_SUBSCR

 315            LOAD_GLOBAL             41 (len + NULL)
                LOAD_FAST_BORROW        13 (bridge_section)
                LOAD_CONST              15 ('rows')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_FAST_BORROW        13 (bridge_section)
                LOAD_CONST              14 ('count')
                STORE_SUBSCR

 327   L20:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (recommendations_section, manual_tests_section)
                LOAD_FAST_BORROW        13 (bridge_section)
                BUILD_LIST               3
                STORE_FAST              14 (sections)

 328            LOAD_CONST              27 ('ok')
                STORE_FAST              15 (overall_status)

 329            LOAD_GLOBAL             44 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       28 (to L25)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              28 (<code object <genexpr> at 0x0000018C18053E10, file "app\routes\operator_learning_dashboard.py", line 329>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW        14 (sections)
                GET_ITER
                CALL                     0
       L21:     FOR_ITER                12 (to L24)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L23)
       L22:     NOT_TAKEN
                JUMP_BACKWARD           11 (to L21)
       L23:     POP_ITER
                LOAD_CONST              29 (True)
                JUMP_FORWARD            17 (to L26)
       L24:     END_FOR
                POP_ITER
                LOAD_CONST              30 (False)
                JUMP_FORWARD            13 (to L26)
       L25:     PUSH_NULL
                LOAD_CONST              28 (<code object <genexpr> at 0x0000018C18053E10, file "app\routes\operator_learning_dashboard.py", line 329>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW        14 (sections)
                GET_ITER
                CALL                     0
                CALL                     1
       L26:     TO_BOOL
                POP_JUMP_IF_FALSE        4 (to L29)
       L27:     NOT_TAKEN

 330   L28:     LOAD_CONST              31 ('failed')
                STORE_FAST              15 (overall_status)
                JUMP_FORWARD           121 (to L51)

 331   L29:     LOAD_GLOBAL             46 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       28 (to L36)
       L30:     NOT_TAKEN
       L31:     POP_TOP
                LOAD_CONST              32 (<code object <genexpr> at 0x0000018C18053AB0, file "app\routes\operator_learning_dashboard.py", line 331>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW        14 (sections)
                GET_ITER
                CALL                     0
       L32:     FOR_ITER                12 (to L35)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L34)
       L33:     NOT_TAKEN
                JUMP_BACKWARD           11 (to L32)
       L34:     POP_ITER
                LOAD_CONST              30 (False)
                JUMP_FORWARD            17 (to L37)
       L35:     END_FOR
                POP_ITER
                LOAD_CONST              29 (True)
                JUMP_FORWARD            13 (to L37)
       L36:     PUSH_NULL
                LOAD_CONST              32 (<code object <genexpr> at 0x0000018C18053AB0, file "app\routes\operator_learning_dashboard.py", line 331>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW        14 (sections)
                GET_ITER
                CALL                     0
                CALL                     1
       L37:     TO_BOOL
                POP_JUMP_IF_FALSE        4 (to L40)
       L38:     NOT_TAKEN

 332   L39:     LOAD_CONST              13 ('skipped')
                STORE_FAST              15 (overall_status)
                JUMP_FORWARD            60 (to L51)

 333   L40:     LOAD_GLOBAL             44 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       28 (to L47)
       L41:     NOT_TAKEN
       L42:     POP_TOP
                LOAD_CONST              33 (<code object <genexpr> at 0x0000018C18053CF0, file "app\routes\operator_learning_dashboard.py", line 333>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW        14 (sections)
                GET_ITER
                CALL                     0
       L43:     FOR_ITER                12 (to L46)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L45)
       L44:     NOT_TAKEN
                JUMP_BACKWARD           11 (to L43)
       L45:     POP_ITER
                LOAD_CONST              29 (True)
                JUMP_FORWARD            17 (to L48)
       L46:     END_FOR
                POP_ITER
                LOAD_CONST              30 (False)
                JUMP_FORWARD            13 (to L48)
       L47:     PUSH_NULL
                LOAD_CONST              33 (<code object <genexpr> at 0x0000018C18053CF0, file "app\routes\operator_learning_dashboard.py", line 333>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW        14 (sections)
                GET_ITER
                CALL                     0
                CALL                     1
       L48:     TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L51)
       L49:     NOT_TAKEN

 334   L50:     LOAD_CONST              27 ('ok')
                STORE_FAST              15 (overall_status)

 337   L51:     LOAD_CONST              12 ('status')
                LOAD_FAST_BORROW        15 (overall_status)

 338            LOAD_CONST              34 ('surface')
                LOAD_CONST              35 ('ops.learning.dashboard')

 339            LOAD_CONST              36 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)

 340            LOAD_CONST              37 ('limit')
                LOAD_FAST_BORROW         4 (capped)

 341            LOAD_CONST              38 ('sections')
                LOAD_FAST_BORROW        14 (sections)

 342            LOAD_CONST              18 ('warnings')
                BUILD_LIST               0

 343            LOAD_CONST              16 ('error_code')
                LOAD_CONST               1 (None)

 336            BUILD_MAP                7
                STORE_FAST              16 (env)

 345            LOAD_GLOBAL             49 (_final_envelope + NULL)
                LOAD_FAST_BORROW        16 (env)
                LOAD_CONST              35 ('ops.learning.dashboard')
                LOAD_CONST              39 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L52:     PUSH_EXC_INFO

 209            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       59 (to L56)
                NOT_TAKEN
                STORE_FAST               7 (e)

 210   L53:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 211            LOAD_CONST               4 ('operator_learning_dashboard imports failed type=')

 212            LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE

 211            BUILD_STRING             2

 210            CALL                     1
                POP_TOP

 214            LOAD_CONST               1 (None)
                STORE_FAST               5 (list_learning_recommendations)

 215            LOAD_CONST               1 (None)
                STORE_FAST               6 (project_operator_list)
       L54:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 524 (to L6)

  --   L55:     LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 209   L56:     RERAISE                  0

  --   L57:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L58:     PUSH_EXC_INFO

 220            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       57 (to L62)
                NOT_TAKEN
                STORE_FAST               7 (e)

 221   L59:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 222            LOAD_CONST               6 ('operator_learning_dashboard manual_test_harness import failed type=')

 223            LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE

 222            BUILD_STRING             2

 221            CALL                     1
                POP_TOP

 225            LOAD_CONST               1 (None)
                STORE_FAST               8 (manual_test_run_report)
       L60:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 587 (to L8)

  --   L61:     LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 220   L62:     RERAISE                  0

  --   L63:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L64:     PUSH_EXC_INFO

 233            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       59 (to L68)
                NOT_TAKEN
                STORE_FAST               7 (e)

 234   L65:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 235            LOAD_CONST               9 ('operator_learning_dashboard adaptive_memory imports failed type=')

 236            LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE

 235            BUILD_STRING             2

 234            CALL                     1
                POP_TOP

 238            LOAD_CONST               1 (None)
                STORE_FAST               9 (adaptive_memory_bridge_report)

 239            LOAD_CONST               1 (None)
                STORE_FAST              10 (project_operator_bridge_list)
       L66:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 646 (to L10)

  --   L67:     LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 233   L68:     RERAISE                  0

  --   L69:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L70:     PUSH_EXC_INFO

 264            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      111 (to L74)
                NOT_TAKEN
                STORE_FAST               7 (e)

 265   L71:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 266            LOAD_CONST              20 ('operator_learning_dashboard recommendations projection error type=')

 267            LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE

 266            BUILD_STRING             2

 265            CALL                     1
                POP_TOP

 269            BUILD_LIST               0
                LOAD_FAST               11 (recommendations_section)
                LOAD_CONST              15 ('rows')
                STORE_SUBSCR

 270            LOAD_SMALL_INT           0
                LOAD_FAST               11 (recommendations_section)
                LOAD_CONST              14 ('count')
                STORE_SUBSCR

 271            LOAD_FAST               11 (recommendations_section)
                LOAD_CONST              18 ('warnings')
                BINARY_OP               26 ([])
                LOAD_ATTR               43 (append + NULL|self)

 272            LOAD_CONST              21 ('projection_failed:')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 271            CALL                     1
                POP_TOP
       L72:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 676 (to L14)

  --   L73:     LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 264   L74:     RERAISE                  0

  --   L75:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L76:     PUSH_EXC_INFO

 316            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      111 (to L80)
                NOT_TAKEN
                STORE_FAST               7 (e)

 317   L77:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 318            LOAD_CONST              26 ('operator_learning_dashboard bridge projection error type=')

 319            LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE

 318            BUILD_STRING             2

 317            CALL                     1
                POP_TOP

 321            BUILD_LIST               0
                LOAD_FAST               13 (bridge_section)
                LOAD_CONST              15 ('rows')
                STORE_SUBSCR

 322            LOAD_SMALL_INT           0
                LOAD_FAST               13 (bridge_section)
                LOAD_CONST              14 ('count')
                STORE_SUBSCR

 323            LOAD_FAST               13 (bridge_section)
                LOAD_CONST              18 ('warnings')
                BINARY_OP               26 ([])
                LOAD_ATTR               43 (append + NULL|self)

 324            LOAD_CONST              21 ('projection_failed:')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 323            CALL                     1
                POP_TOP
       L78:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 671 (to L20)

  --   L79:     LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 316   L80:     RERAISE                  0

  --   L81:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L82:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L4 -> L82 [0] lasti
  L5 to L6 -> L52 [0]
  L7 to L8 -> L58 [0]
  L9 to L10 -> L64 [0]
  L10 to L12 -> L82 [0] lasti
  L13 to L14 -> L70 [0]
  L14 to L18 -> L82 [0] lasti
  L19 to L20 -> L76 [0]
  L20 to L22 -> L82 [0] lasti
  L23 to L27 -> L82 [0] lasti
  L28 to L30 -> L82 [0] lasti
  L31 to L33 -> L82 [0] lasti
  L34 to L38 -> L82 [0] lasti
  L39 to L41 -> L82 [0] lasti
  L42 to L44 -> L82 [0] lasti
  L45 to L49 -> L82 [0] lasti
  L50 to L52 -> L82 [0] lasti
  L52 to L53 -> L57 [1] lasti
  L53 to L54 -> L55 [1] lasti
  L54 to L55 -> L82 [0] lasti
  L55 to L57 -> L57 [1] lasti
  L57 to L58 -> L82 [0] lasti
  L58 to L59 -> L63 [1] lasti
  L59 to L60 -> L61 [1] lasti
  L60 to L61 -> L82 [0] lasti
  L61 to L63 -> L63 [1] lasti
  L63 to L64 -> L82 [0] lasti
  L64 to L65 -> L69 [1] lasti
  L65 to L66 -> L67 [1] lasti
  L66 to L67 -> L82 [0] lasti
  L67 to L69 -> L69 [1] lasti
  L69 to L70 -> L82 [0] lasti
  L70 to L71 -> L75 [1] lasti
  L71 to L72 -> L73 [1] lasti
  L72 to L73 -> L82 [0] lasti
  L73 to L75 -> L75 [1] lasti
  L75 to L76 -> L82 [0] lasti
  L76 to L77 -> L81 [1] lasti
  L77 to L78 -> L79 [1] lasti
  L78 to L79 -> L82 [0] lasti
  L79 to L81 -> L81 [1] lasti
  L81 to L82 -> L82 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18053E10, file "app\routes\operator_learning_dashboard.py", line 329>:
 329           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                24 (to L3)
               STORE_FAST_LOAD_FAST    17 (s, s)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('status')
               CALL                     1
               LOAD_CONST               1 ('failed')
               COMPARE_OP              72 (==)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           26 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18053AB0, file "app\routes\operator_learning_dashboard.py", line 331>:
 331           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                24 (to L3)
               STORE_FAST_LOAD_FAST    17 (s, s)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('status')
               CALL                     1
               LOAD_CONST               1 ('skipped')
               COMPARE_OP              72 (==)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           26 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18053CF0, file "app\routes\operator_learning_dashboard.py", line 333>:
 333           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                24 (to L3)
               STORE_FAST_LOAD_FAST    17 (s, s)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('status')
               CALL                     1
               LOAD_CONST               1 ('skipped')
               COMPARE_OP              72 (==)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           26 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti
```
