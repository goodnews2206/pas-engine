# routes/operator_learning

- **pyc:** `app\routes\__pycache__\operator_learning.cpython-314.pyc`
- **expected source path (absent):** `app\routes/operator_learning.py`
- **co_filename (from bytecode):** `app/routes/operator_learning.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** routes

## Module docstring

```
PAS180 — Operator learning recommendation review routes.

Admin-only surfaces mounted at ``/ops/learning``. Wraps the
PAS180 ``recommendation_review`` + ``recommendation_projection``
services into the operator REST surface.

Doctrine:

* **Admin auth only** (X-Admin-Key).
* **No tenant exposure.** Tenants use ``/tenant/learning``.
* **Bounded pagination caps.**
* **Forbidden-token scanner** on every response.
* **No live behaviour mutation.** PAS180 reviews are
  recommendation-row status transitions only; nothing in the
  outbound FSM / Memory Review / booking / worker is touched.
* **Audit-safe.** Every mutation writes a PAS174 audit row via
  the recommendation_review service.
* **NEVER raises.**

Routes:

    GET  /ops/learning/recommendations
    GET  /ops/learning/recommendations/{recommendation_id}
    POST /ops/learning/recommendations/{recommendation_id}/approve-manual-test
    POST /ops/learning/recommendations/{recommendation_id}/reject
    POST /ops/learning/recommendations/{recommendation_id}/expire
```

## Imports

`APIRouter`, `Any`, `Body`, `Depends`, `Dict`, `HTTPException`, `Header`, `Optional`, `Query`, `__future__`, `annotations`, `app.config`, `app.services.learning.recommendation_projection`, `app.services.learning.recommendation_review`, `app.services.security.rate_limit`, `approve_recommendation_for_manual_test`, `check_rate_limit`, `expire_learning_recommendation`, `fastapi`, `get_learning_recommendation`, `get_settings`, `list_learning_recommendations`, `logging`, `project_operator_list`, `project_operator_view`, `recommendation_review_history`, `reject_learning_recommendation`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_int`, `_final_envelope`, `_safe_brokerage`, `_safe_recommendation_id`, `_scan_for_forbidden`, `_surface_review`, `approve_manual_test_route`, `expire_recommendation_route`, `get_recommendation_route`, `list_recommendations_route`, `reject_recommendation_route`, `require_admin`

## Env-key candidates

`ADMIN`

## String constants (redacted where noted)

- '\nPAS180 — Operator learning recommendation review routes.\n\nAdmin-only surfaces mounted at ``/ops/learning``. Wraps the\nPAS180 ``recommendation_review`` + ``recommendation_projection``\nservices into the operator REST surface.\n\nDoctrine:\n\n* **Admin auth only** (X-Admin-Key).\n* **No tenant exposure.** Tenants use ``/tenant/learning``.\n* **Bounded pagination caps.**\n* **Forbidden-token scanner** on every response.\n* **No live behaviour mutation.** PAS180 reviews are\n  recommendation-row status transitions only; nothing in the\n  outbound FSM / Memory Review / booking / worker is touched.\n* **Audit-safe.** Every mutation writes a PAS174 audit row via\n  the recommendation_review service.\n* **NEVER raises.**\n\nRoutes:\n\n    GET  /ops/learning/recommendations\n    GET  /ops/learning/recommendations/{recommendation_id}\n    POST /ops/learning/recommendations/{recommendation_id}/approve-manual-test\n    POST /ops/learning/recommendations/{recommendation_id}/reject\n    POST /ops/learning/recommendations/{recommendation_id}/expire\n'
- 'pas.ops.learning'
- '/recommendations'
- '/recommendations/{recommendation_id}'
- '/recommendations/{recommendation_id}/approve-manual-test'
- '/recommendations/{recommendation_id}/reject'
- '/recommendations/{recommendation_id}/expire'
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
- 'operator_learning surface='
- ' collapsed — forbidden token leaked'
- 'status'
- 'failed'
- 'error_code'
- 'ops_envelope_forbidden_token'
- 'warnings'
- 'value'
- 'int'
- 'default'
- 'brokerage_id'
- 'limit'
- 'skipped'
- 'ops.learning.recommendations.list'
- 'rows'
- 'count'
- 'operator_learning list error type='
- 'unexpected:'
- 'recommendation_id'
- 'invalid recommendation_id'
- 'ops.learning.recommendations.get'
- 'record'
- 'history'
- 'operator_learning get error type='
- 'surface_name'
- 'body'
- 'actor_type'
- 'actor_id'
- 'reason_token'
- 'transition'
- 'audit_row'
- 'operator_learning '
- ' error type='
- 'ops.learning.recommendations.approve_manual_test'
- 'ops.learning.recommendations.reject'
- 'ops.learning.recommendations.expire'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS180 — Operator learning recommendation review routes.\n\nAdmin-only surfaces mounted at ``/ops/learning``. Wraps the\nPAS180 ``recommendation_review`` + ``recommendation_projection``\nservices into the operator REST surface.\n\nDoctrine:\n\n* **Admin auth only** (X-Admin-Key).\n* **No tenant exposure.** Tenants use ``/tenant/learning``.\n* **Bounded pagination caps.**\n* **Forbidden-token scanner** on every response.\n* **No live behaviour mutation.** PAS180 reviews are\n  recommendation-row status transitions only; nothing in the\n  outbound FSM / Memory Review / booking / worker is touched.\n* **Audit-safe.** Every mutation writes a PAS174 audit row via\n  the recommendation_review service.\n* **NEVER raises.**\n\nRoutes:\n\n    GET  /ops/learning/recommendations\n    GET  /ops/learning/recommendations/{recommendation_id}\n    POST /ops/learning/recommendations/{recommendation_id}/approve-manual-test\n    POST /ops/learning/recommendations/{recommendation_id}/reject\n    POST /ops/learning/recommendations/{recommendation_id}/expire\n')
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
              LOAD_CONST               6 ('pas.ops.learning')
              CALL                     1
              STORE_NAME              19 (logger)

 44           LOAD_NAME               12 (Header)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              CALL                     1
              BUILD_TUPLE              1
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA2C40, file "app/routes/operator_learning.py", line 44>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object require_admin at 0x0000018C179A7290, file "app/routes/operator_learning.py", line 44>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              20 (require_admin)

 73           LOAD_SMALL_INT         200
              STORE_NAME              21 (_BROKERAGE_ID_MAX_LEN)

 74           LOAD_SMALL_INT         200
              STORE_NAME              22 (_REC_ID_MAX_LEN)

 75           LOAD_SMALL_INT          50
              STORE_NAME              23 (_LIST_LIMIT_DEFAULT)

 76           LOAD_CONST              10 (500)
              STORE_NAME              24 (_LIST_LIMIT_MAX)

 79           LOAD_CONST              39 (('phone', 'email', 'name_token', 'transcript', 'summary_text', 'raw_payload', 'raw_email', 'raw_body', 'secret', 'signature', 'dedupe_key', 'callback_notes', 'rationale_text', 'rationale_freeform', 'prompt_text', 'live_mutation_payload'))
              STORE_NAME              25 (_FORBIDDEN_RESPONSE_TOKENS)

 88           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA34B0, file "app/routes/operator_learning.py", line 88>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object _scan_for_forbidden at 0x0000018C18025C30, file "app/routes/operator_learning.py", line 88>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_scan_for_forbidden)

112           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18025A30, file "app/routes/operator_learning.py", line 112>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object _final_envelope at 0x0000018C17FE1920, file "app/routes/operator_learning.py", line 112>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_final_envelope)

128           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA3960, file "app/routes/operator_learning.py", line 128>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _safe_brokerage at 0x0000018C17F95FD0, file "app/routes/operator_learning.py", line 128>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_safe_brokerage)

137           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA2970, file "app/routes/operator_learning.py", line 137>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _safe_recommendation_id at 0x0000018C17F95CF0, file "app/routes/operator_learning.py", line 137>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_safe_recommendation_id)

146           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18024C30, file "app/routes/operator_learning.py", line 146>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _clamp_int at 0x0000018C18038DF0, file "app/routes/operator_learning.py", line 146>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_clamp_int)

162           LOAD_NAME               17 (router)
              LOAD_ATTR               63 (get + NULL|self)
              LOAD_CONST              21 ('/recommendations')
              CALL                     1

164           LOAD_NAME               14 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT         200
              LOAD_CONST              22 (('max_length',))
              CALL_KW                  2

165           LOAD_NAME               14 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT          64
              LOAD_CONST              22 (('max_length',))
              CALL_KW                  2

166           LOAD_NAME               14 (Query)
              PUSH_NULL
              LOAD_NAME               23 (_LIST_LIMIT_DEFAULT)
              CALL                     1

167           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               20 (require_admin)
              CALL                     1

163           BUILD_TUPLE              4
              LOAD_CONST              23 (<code object __annotate__ at 0x0000018C18026330, file "app/routes/operator_learning.py", line 163>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object list_recommendations_route at 0x0000018C17D6DFC0, file "app/routes/operator_learning.py", line 162>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

162           CALL                     0

163           STORE_NAME              32 (list_recommendations_route)

204           LOAD_NAME               17 (router)
              LOAD_ATTR               63 (get + NULL|self)
              LOAD_CONST              25 ('/recommendations/{recommendation_id}')
              CALL                     1

207           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               20 (require_admin)
              CALL                     1

205           BUILD_TUPLE              1
              LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA23D0, file "app/routes/operator_learning.py", line 205>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object get_recommendation_route at 0x0000018C17D8BF50, file "app/routes/operator_learning.py", line 204>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

204           CALL                     0

205           STORE_NAME              33 (get_recommendation_route)

250           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C18024B30, file "app/routes/operator_learning.py", line 250>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object _surface_review at 0x0000018C17F62FC0, file "app/routes/operator_learning.py", line 250>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              34 (_surface_review)

292           LOAD_NAME               17 (router)
              LOAD_ATTR               71 (post + NULL|self)
              LOAD_CONST              30 ('/recommendations/{recommendation_id}/approve-manual-test')
              CALL                     1

295           LOAD_NAME               10 (Body)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              CALL                     1

296           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               20 (require_admin)
              CALL                     1

293           BUILD_TUPLE              2
              LOAD_CONST              31 (<code object __annotate__ at 0x0000018C18026630, file "app/routes/operator_learning.py", line 293>)
              MAKE_FUNCTION
              LOAD_CONST              32 (<code object approve_manual_test_route at 0x0000018C18038670, file "app/routes/operator_learning.py", line 292>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

292           CALL                     0

293           STORE_NAME              36 (approve_manual_test_route)

312           LOAD_NAME               17 (router)
              LOAD_ATTR               71 (post + NULL|self)
              LOAD_CONST              33 ('/recommendations/{recommendation_id}/reject')
              CALL                     1

315           LOAD_NAME               10 (Body)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              CALL                     1

316           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               20 (require_admin)
              CALL                     1

313           BUILD_TUPLE              2
              LOAD_CONST              34 (<code object __annotate__ at 0x0000018C18026430, file "app/routes/operator_learning.py", line 313>)
              MAKE_FUNCTION
              LOAD_CONST              35 (<code object reject_recommendation_route at 0x0000018C18038170, file "app/routes/operator_learning.py", line 312>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

312           CALL                     0

313           STORE_NAME              37 (reject_recommendation_route)

332           LOAD_NAME               17 (router)
              LOAD_ATTR               71 (post + NULL|self)
              LOAD_CONST              36 ('/recommendations/{recommendation_id}/expire')
              CALL                     1

335           LOAD_NAME               10 (Body)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              CALL                     1

336           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               20 (require_admin)
              CALL                     1

333           BUILD_TUPLE              2
              LOAD_CONST              37 (<code object __annotate__ at 0x0000018C18025830, file "app/routes/operator_learning.py", line 333>)
              MAKE_FUNCTION
              LOAD_CONST              38 (<code object expire_recommendation_route at 0x0000018C180388F0, file "app/routes/operator_learning.py", line 332>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

332           CALL                     0

333           STORE_NAME              38 (expire_recommendation_route)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app/routes/operator_learning.py", line 44>:
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

Disassembly of <code object require_admin at 0x0000018C179A7290, file "app/routes/operator_learning.py", line 44>:
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

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app/routes/operator_learning.py", line 88>:
 88           RESUME                   0
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

Disassembly of <code object _scan_for_forbidden at 0x0000018C18025C30, file "app/routes/operator_learning.py", line 88>:
  --           MAKE_CELL                1 (walk)

  88           RESUME                   0

  89           LOAD_CONST               0 (<code object __annotate__ at 0x0000018C17FA3B40, file "app/routes/operator_learning.py", line 89>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object walk at 0x0000018C17CC2460, file "app/routes/operator_learning.py", line 89>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

 109           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app/routes/operator_learning.py", line 89>:
 89           RESUME                   0
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

Disassembly of <code object walk at 0x0000018C17CC2460, file "app/routes/operator_learning.py", line 89>:
  --            COPY_FREE_VARS           1

  89            RESUME                   0

  90            NOP

  91    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      111 (to L16)
        L2:     NOT_TAKEN

  92    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                88 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

  93            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L10)
                NOT_TAKEN

  94            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

  95            LOAD_GLOBAL             10 (_FORBIDDEN_RESPONSE_TOKENS)
                GET_ITER
        L5:     FOR_ITER                15 (to L9)
                STORE_FAST               4 (tok)

  96            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)

  97    L7:     LOAD_FAST_BORROW         4 (tok)
                SWAP                     2
                POP_TOP
                SWAP                     2
                POP_TOP
        L8:     RETURN_VALUE

  95    L9:     END_FOR
                POP_ITER

  98   L10:     LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

  99            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           86 (to L4)

 100   L12:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L13:     RETURN_VALUE

  92   L14:     END_FOR
                POP_ITER

 108   L15:     LOAD_CONST               0 (None)
                RETURN_VALUE

 101   L16:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             12 (list)
                LOAD_GLOBAL             14 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L22)
                NOT_TAKEN

 102            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L17:     FOR_ITER                23 (to L21)
                STORE_FAST               2 (v)

 103            LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 104            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           21 (to L17)

 105   L19:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L20:     RETURN_VALUE

 102   L21:     END_FOR
                POP_ITER

 108   L22:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 106            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L25)
                NOT_TAKEN
                POP_TOP

 107   L24:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 106   L25:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app/routes/operator_learning.py", line 112>:
112           RESUME                   0
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

Disassembly of <code object _final_envelope at 0x0000018C17FE1920, file "app/routes/operator_learning.py", line 112>:
112           RESUME                   0

113           LOAD_GLOBAL              1 (_scan_for_forbidden + NULL)
              LOAD_FAST_BORROW         0 (env)
              CALL                     1
              STORE_FAST               2 (leak)

114           LOAD_FAST_BORROW         2 (leak)
              TO_BOOL
              POP_JUMP_IF_FALSE       37 (to L1)
              NOT_TAKEN

115           LOAD_GLOBAL              2 (logger)
              LOAD_ATTR                5 (warning + NULL|self)

116           LOAD_CONST               0 ('operator_learning surface=')
              LOAD_FAST_BORROW         1 (surface)
              FORMAT_SIMPLE
              LOAD_CONST               1 (' collapsed — forbidden token leaked')
              BUILD_STRING             3

115           CALL                     1
              POP_TOP

120           LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('failed')

121           LOAD_CONST               4 ('surface')
              LOAD_FAST_BORROW         1 (surface)

122           LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('ops_envelope_forbidden_token')

123           LOAD_CONST               7 ('warnings')
              LOAD_CONST               6 ('ops_envelope_forbidden_token')
              BUILD_LIST               1

119           BUILD_MAP                4
              RETURN_VALUE

125   L1:     LOAD_FAST_BORROW         0 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app/routes/operator_learning.py", line 128>:
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

Disassembly of <code object _safe_brokerage at 0x0000018C17F95FD0, file "app/routes/operator_learning.py", line 128>:
128           RESUME                   0

129           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

130           LOAD_CONST               0 (None)
              RETURN_VALUE

131   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

132           LOAD_FAST_BORROW         1 (s)
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

133   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

134   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app/routes/operator_learning.py", line 137>:
137           RESUME                   0
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

Disassembly of <code object _safe_recommendation_id at 0x0000018C17F95CF0, file "app/routes/operator_learning.py", line 137>:
137           RESUME                   0

138           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

139           LOAD_CONST               0 (None)
              RETURN_VALUE

140   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

141           LOAD_FAST_BORROW         1 (s)
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

142   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

143   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app/routes/operator_learning.py", line 146>:
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

Disassembly of <code object _clamp_int at 0x0000018C18038DF0, file "app/routes/operator_learning.py", line 146>:
 146           RESUME                   0

 147           NOP

 148   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

 151   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 152           LOAD_FAST                1 (lo)
               RETURN_VALUE

 153   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 154           LOAD_FAST                2 (hi)
               RETURN_VALUE

 155   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 149           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

 150           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 149   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026330, file "app/routes/operator_learning.py", line 163>:
163           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

164           LOAD_CONST               2 ('Optional[str]')

163           LOAD_CONST               3 ('status')

165           LOAD_CONST               2 ('Optional[str]')

163           LOAD_CONST               4 ('limit')

166           LOAD_CONST               5 ('int')

163           LOAD_CONST               6 ('return')

168           LOAD_CONST               7 ('Dict[str, Any]')

163           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object list_recommendations_route at 0x0000018C17D6DFC0, file "app/routes/operator_learning.py", line 162>:
 162            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 169            LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               0 (None)
        L3:     STORE_FAST               4 (bid)

 170            LOAD_GLOBAL              3 (_clamp_int + NULL)
                LOAD_FAST_BORROW         2 (limit)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              4 (_LIST_LIMIT_MAX)
                LOAD_GLOBAL              6 (_LIST_LIMIT_DEFAULT)
                CALL                     4
                STORE_FAST               5 (capped_limit)

 171            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('list_learning_recommendations',))
                IMPORT_NAME              4 (app.services.learning.recommendation_review)
                IMPORT_FROM              5 (list_learning_recommendations)
                STORE_FAST               6 (list_learning_recommendations)
                POP_TOP

 174            LOAD_SMALL_INT           0
                LOAD_CONST               2 (('project_operator_list',))
                IMPORT_NAME              6 (app.services.learning.recommendation_projection)
                IMPORT_FROM              7 (project_operator_list)
                STORE_FAST               7 (project_operator_list)
                POP_TOP

 177    L4:     NOP

 178    L5:     LOAD_FAST_BORROW         6 (list_learning_recommendations)
                PUSH_NULL

 179            LOAD_FAST_BORROW         4 (bid)

 180            LOAD_FAST_BORROW         1 (status)

 181            LOAD_FAST_BORROW         5 (capped_limit)

 178            LOAD_CONST               3 (('brokerage_id', 'status', 'limit'))
                CALL_KW                  3
                STORE_FAST               8 (result)

 184            LOAD_CONST               4 ('status')
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               4 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                LOAD_CONST               5 ('skipped')

 185    L8:     LOAD_CONST               6 ('surface')
                LOAD_CONST               7 ('ops.learning.recommendations.list')

 186            LOAD_CONST               8 ('rows')
                LOAD_FAST                7 (project_operator_list)
                PUSH_NULL
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               8 ('rows')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                BUILD_LIST               0
       L11:     CALL                     1

 187            LOAD_CONST               9 ('count')
                LOAD_GLOBAL             19 (len + NULL)
                LOAD_FAST                7 (project_operator_list)
                PUSH_NULL
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               8 ('rows')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
       L12:     NOT_TAKEN
       L13:     POP_TOP
                BUILD_LIST               0
       L14:     CALL                     1
                CALL                     1

 188            LOAD_CONST              10 ('warnings')
                LOAD_GLOBAL             21 (list + NULL)
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              10 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L17)
       L15:     NOT_TAKEN
       L16:     POP_TOP
                BUILD_LIST               0
       L17:     CALL                     1

 189            LOAD_CONST              11 ('error_code')
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              11 ('error_code')
                CALL                     1

 183            BUILD_MAP                6
                STORE_FAST               9 (env)

 201   L18:     LOAD_GLOBAL             33 (_final_envelope + NULL)
                LOAD_FAST_BORROW         9 (env)
                LOAD_CONST               7 ('ops.learning.recommendations.list')
                LOAD_CONST              15 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L19:     PUSH_EXC_INFO

 191            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L23)
                NOT_TAKEN
                STORE_FAST              10 (e)

 192   L20:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 193            LOAD_CONST              12 ('operator_learning list error type=')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 192            CALL                     1
                POP_TOP

 196            LOAD_CONST               4 ('status')
                LOAD_CONST              13 ('failed')

 197            LOAD_CONST               6 ('surface')
                LOAD_CONST               7 ('ops.learning.recommendations.list')

 198            LOAD_CONST              11 ('error_code')
                LOAD_CONST              14 ('unexpected:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 199            LOAD_CONST              10 ('warnings')
                BUILD_LIST               0

 195            BUILD_MAP                4
                STORE_FAST               9 (env)
       L21:     POP_EXCEPT
                LOAD_CONST               0 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L18)

  --   L22:     LOAD_CONST               0 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 191   L23:     RERAISE                  0

  --   L24:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L25:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L4 -> L25 [0] lasti
  L5 to L6 -> L19 [0]
  L7 to L9 -> L19 [0]
  L10 to L12 -> L19 [0]
  L13 to L15 -> L19 [0]
  L16 to L18 -> L19 [0]
  L18 to L19 -> L25 [0] lasti
  L19 to L20 -> L24 [1] lasti
  L20 to L21 -> L22 [1] lasti
  L21 to L22 -> L25 [0] lasti
  L22 to L24 -> L24 [1] lasti
  L24 to L25 -> L25 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app/routes/operator_learning.py", line 205>:
205           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendation_id')

206           LOAD_CONST               2 ('str')

205           LOAD_CONST               3 ('return')

208           LOAD_CONST               4 ('Dict[str, Any]')

205           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object get_recommendation_route at 0x0000018C17D8BF50, file "app/routes/operator_learning.py", line 204>:
 204            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 209            LOAD_GLOBAL              1 (_safe_recommendation_id + NULL)
                LOAD_FAST_BORROW         0 (recommendation_id)
                CALL                     1
                STORE_FAST               2 (rid)

 210            LOAD_FAST_BORROW         2 (rid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 211            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               1 (400)
                LOAD_CONST               2 ('invalid recommendation_id')
                LOAD_CONST               3 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 212    L2:     LOAD_SMALL_INT           0
                LOAD_CONST               4 (('get_learning_recommendation', 'recommendation_review_history'))
                IMPORT_NAME              2 (app.services.learning.recommendation_review)
                IMPORT_FROM              3 (get_learning_recommendation)
                STORE_FAST               3 (get_learning_recommendation)
                IMPORT_FROM              4 (recommendation_review_history)
                STORE_FAST               4 (recommendation_review_history)
                POP_TOP

 215            LOAD_SMALL_INT           0
                LOAD_CONST               5 (('project_operator_view',))
                IMPORT_NAME              5 (app.services.learning.recommendation_projection)
                IMPORT_FROM              6 (project_operator_view)
                STORE_FAST               5 (project_operator_view)
                POP_TOP

 218    L3:     NOP

 219    L4:     LOAD_FAST_BORROW         3 (get_learning_recommendation)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (rid)
                LOAD_CONST               6 (('recommendation_id',))
                CALL_KW                  1
                STORE_FAST               6 (result)

 220            LOAD_FAST_BORROW         4 (recommendation_review_history)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (rid)
                LOAD_CONST               6 (('recommendation_id',))
                CALL_KW                  1
                STORE_FAST               7 (history)

 222            LOAD_CONST               7 ('status')
                LOAD_FAST_BORROW         6 (result)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                LOAD_CONST               8 ('skipped')

 223    L7:     LOAD_CONST               9 ('surface')
                LOAD_CONST              10 ('ops.learning.recommendations.get')

 224            LOAD_CONST              11 ('record')
                LOAD_FAST                5 (project_operator_view)
                PUSH_NULL
                LOAD_FAST_BORROW         6 (result)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              11 ('record')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                BUILD_MAP                0
       L10:     CALL                     1

 225            LOAD_CONST              12 ('history')

 226            LOAD_CONST              13 ('count')
                LOAD_GLOBAL             17 (int + NULL)
                LOAD_FAST_BORROW         7 (history)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              13 ('count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                LOAD_SMALL_INT           0
       L13:     CALL                     1

 227            LOAD_CONST              14 ('rows')
                LOAD_GLOBAL             19 (list + NULL)
                LOAD_FAST_BORROW         7 (history)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              14 ('rows')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
       L14:     NOT_TAKEN
       L15:     POP_TOP
                BUILD_LIST               0
       L16:     CALL                     1

 228            LOAD_CONST               7 ('status')
                LOAD_FAST_BORROW         7 (history)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1

 225            BUILD_MAP                3

 230            LOAD_CONST              15 ('warnings')
                LOAD_GLOBAL             19 (list + NULL)
                LOAD_FAST_BORROW         6 (result)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              15 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L19)
       L17:     NOT_TAKEN
       L18:     POP_TOP
                BUILD_LIST               0
       L19:     CALL                     1

 231            LOAD_CONST              16 ('error_code')
                LOAD_FAST_BORROW         6 (result)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              16 ('error_code')
                CALL                     1

 221            BUILD_MAP                6
                STORE_FAST               8 (env)

 243   L20:     LOAD_GLOBAL             31 (_final_envelope + NULL)
                LOAD_FAST_BORROW         8 (env)
                LOAD_CONST              10 ('ops.learning.recommendations.get')
                LOAD_CONST              20 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L21:     PUSH_EXC_INFO

 233            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L25)
                NOT_TAKEN
                STORE_FAST               9 (e)

 234   L22:     LOAD_GLOBAL             22 (logger)
                LOAD_ATTR               25 (warning + NULL|self)

 235            LOAD_CONST              17 ('operator_learning get error type=')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 234            CALL                     1
                POP_TOP

 238            LOAD_CONST               7 ('status')
                LOAD_CONST              18 ('failed')

 239            LOAD_CONST               9 ('surface')
                LOAD_CONST              10 ('ops.learning.recommendations.get')

 240            LOAD_CONST              16 ('error_code')
                LOAD_CONST              19 ('unexpected:')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 241            LOAD_CONST              15 ('warnings')
                BUILD_LIST               0

 237            BUILD_MAP                4
                STORE_FAST               8 (env)
       L23:     POP_EXCEPT
                LOAD_CONST               0 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L20)

  --   L24:     LOAD_CONST               0 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 233   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L27:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L27 [0] lasti
  L4 to L5 -> L21 [0]
  L6 to L8 -> L21 [0]
  L9 to L11 -> L21 [0]
  L12 to L14 -> L21 [0]
  L15 to L17 -> L21 [0]
  L18 to L20 -> L21 [0]
  L20 to L21 -> L27 [0] lasti
  L21 to L22 -> L26 [1] lasti
  L22 to L23 -> L24 [1] lasti
  L23 to L24 -> L27 [0] lasti
  L24 to L26 -> L26 [1] lasti
  L26 to L27 -> L27 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app/routes/operator_learning.py", line 250>:
250           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('surface_name')

252           LOAD_CONST               2 ('str')

250           LOAD_CONST               3 ('body')

253           LOAD_CONST               4 ('Dict[str, Any]')

250           LOAD_CONST               5 ('recommendation_id')

255           LOAD_CONST               2 ('str')

250           LOAD_CONST               6 ('return')

256           LOAD_CONST               4 ('Dict[str, Any]')

250           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _surface_review at 0x0000018C17F62FC0, file "app/routes/operator_learning.py", line 250>:
 250            RESUME                   0

 257            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('project_operator_view',))
                IMPORT_NAME              0 (app.services.learning.recommendation_projection)
                IMPORT_FROM              1 (project_operator_view)
                STORE_FAST               4 (project_operator_view)
                POP_TOP

 260            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (body)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               2 ('actor_type')
                CALL                     1
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST               3 (None)
        L2:     STORE_FAST               5 (actor_type)

 261            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (body)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               4 ('actor_id')
                CALL                     1
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               3 (None)
        L4:     STORE_FAST               6 (actor_id)

 262            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (body)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               5 ('reason_token')
                CALL                     1
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               3 (None)
        L6:     STORE_FAST               7 (reason)

 263            NOP

 264    L7:     LOAD_FAST_BORROW         2 (handler)
                PUSH_NULL

 265            LOAD_FAST_BORROW         3 (recommendation_id)

 266            LOAD_FAST_BORROW         5 (actor_type)

 267            LOAD_FAST_BORROW         6 (actor_id)

 268            LOAD_FAST_BORROW         7 (reason)

 264            LOAD_CONST               6 (('recommendation_id', 'actor_type', 'actor_id', 'reason_token'))
                CALL_KW                  4
                STORE_FAST               8 (result)

 271            LOAD_CONST               7 ('status')
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                LOAD_CONST               8 ('failed')

 272   L10:     LOAD_CONST               9 ('surface')
                LOAD_FAST                0 (surface_name)

 273            LOAD_CONST              10 ('record')
                LOAD_FAST                4 (project_operator_view)
                PUSH_NULL
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              10 ('record')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                BUILD_MAP                0
       L13:     CALL                     1

 274            LOAD_CONST              11 ('transition')
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              11 ('transition')
                CALL                     1

 275            LOAD_CONST              12 ('audit_row')
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              12 ('audit_row')
                CALL                     1

 276            LOAD_CONST              13 ('warnings')
                LOAD_GLOBAL             11 (list + NULL)
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              13 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
       L14:     NOT_TAKEN
       L15:     POP_TOP
                BUILD_LIST               0
       L16:     CALL                     1

 277            LOAD_CONST              14 ('error_code')
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              14 ('error_code')
                CALL                     1

 270            BUILD_MAP                7
                STORE_FAST               9 (env)

 289   L17:     LOAD_GLOBAL             23 (_final_envelope + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 144 (env, surface_name)
                LOAD_CONST              18 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L18:     PUSH_EXC_INFO

 279            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       89 (to L22)
                NOT_TAKEN
                STORE_FAST              10 (e)

 280   L19:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 281            LOAD_CONST              15 ('operator_learning ')
                LOAD_FAST                0 (surface_name)
                FORMAT_SIMPLE
                LOAD_CONST              16 (' error type=')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             4

 280            CALL                     1
                POP_TOP

 284            LOAD_CONST               7 ('status')
                LOAD_CONST               8 ('failed')

 285            LOAD_CONST               9 ('surface')
                LOAD_FAST                0 (surface_name)

 286            LOAD_CONST              14 ('error_code')
                LOAD_CONST              17 ('unexpected:')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 287            LOAD_CONST              13 ('warnings')
                BUILD_LIST               0

 283            BUILD_MAP                4
                STORE_FAST               9 (env)
       L20:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                JUMP_BACKWARD_NO_INTERRUPT 106 (to L17)

  --   L21:     LOAD_CONST               3 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 279   L22:     RERAISE                  0

  --   L23:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L7 to L8 -> L18 [0]
  L9 to L11 -> L18 [0]
  L12 to L14 -> L18 [0]
  L15 to L17 -> L18 [0]
  L18 to L19 -> L23 [1] lasti
  L19 to L20 -> L21 [1] lasti
  L21 to L23 -> L23 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026630, file "app/routes/operator_learning.py", line 293>:
293           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendation_id')

294           LOAD_CONST               2 ('str')

293           LOAD_CONST               3 ('body')

295           LOAD_CONST               4 ('Dict[str, Any]')

293           LOAD_CONST               5 ('return')

297           LOAD_CONST               4 ('Dict[str, Any]')

293           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object approve_manual_test_route at 0x0000018C18038670, file "app/routes/operator_learning.py", line 292>:
 292           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 298           LOAD_GLOBAL              1 (_safe_recommendation_id + NULL)
               LOAD_FAST_BORROW         0 (recommendation_id)
               CALL                     1
               STORE_FAST               3 (rid)

 299           LOAD_FAST_BORROW         3 (rid)
               POP_JUMP_IF_NOT_NONE    14 (to L2)
               NOT_TAKEN

 300           LOAD_GLOBAL              3 (HTTPException + NULL)
               LOAD_CONST               1 (400)
               LOAD_CONST               2 ('invalid recommendation_id')
               LOAD_CONST               3 (('status_code', 'detail'))
               CALL_KW                  2
               RAISE_VARARGS            1

 301   L2:     LOAD_SMALL_INT           0
               LOAD_CONST               4 (('approve_recommendation_for_manual_test',))
               IMPORT_NAME              2 (app.services.learning.recommendation_review)
               IMPORT_FROM              3 (approve_recommendation_for_manual_test)
               STORE_FAST               4 (approve_recommendation_for_manual_test)
               POP_TOP

 304           LOAD_GLOBAL              9 (_surface_review + NULL)

 305           LOAD_CONST               5 ('ops.learning.recommendations.approve_manual_test')

 306           LOAD_FAST_BORROW         1 (body)

 307           LOAD_FAST_BORROW         4 (approve_recommendation_for_manual_test)

 308           LOAD_FAST_BORROW         3 (rid)

 304           LOAD_CONST               6 (('surface_name', 'body', 'handler', 'recommendation_id'))
               CALL_KW                  4
               RETURN_VALUE

  --   L3:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L3 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "app/routes/operator_learning.py", line 313>:
313           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendation_id')

314           LOAD_CONST               2 ('str')

313           LOAD_CONST               3 ('body')

315           LOAD_CONST               4 ('Dict[str, Any]')

313           LOAD_CONST               5 ('return')

317           LOAD_CONST               4 ('Dict[str, Any]')

313           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object reject_recommendation_route at 0x0000018C18038170, file "app/routes/operator_learning.py", line 312>:
 312           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 318           LOAD_GLOBAL              1 (_safe_recommendation_id + NULL)
               LOAD_FAST_BORROW         0 (recommendation_id)
               CALL                     1
               STORE_FAST               3 (rid)

 319           LOAD_FAST_BORROW         3 (rid)
               POP_JUMP_IF_NOT_NONE    14 (to L2)
               NOT_TAKEN

 320           LOAD_GLOBAL              3 (HTTPException + NULL)
               LOAD_CONST               1 (400)
               LOAD_CONST               2 ('invalid recommendation_id')
               LOAD_CONST               3 (('status_code', 'detail'))
               CALL_KW                  2
               RAISE_VARARGS            1

 321   L2:     LOAD_SMALL_INT           0
               LOAD_CONST               4 (('reject_learning_recommendation',))
               IMPORT_NAME              2 (app.services.learning.recommendation_review)
               IMPORT_FROM              3 (reject_learning_recommendation)
               STORE_FAST               4 (reject_learning_recommendation)
               POP_TOP

 324           LOAD_GLOBAL              9 (_surface_review + NULL)

 325           LOAD_CONST               5 ('ops.learning.recommendations.reject')

 326           LOAD_FAST_BORROW         1 (body)

 327           LOAD_FAST_BORROW         4 (reject_learning_recommendation)

 328           LOAD_FAST_BORROW         3 (rid)

 324           LOAD_CONST               6 (('surface_name', 'body', 'handler', 'recommendation_id'))
               CALL_KW                  4
               RETURN_VALUE

  --   L3:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L3 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025830, file "app/routes/operator_learning.py", line 333>:
333           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendation_id')

334           LOAD_CONST               2 ('str')

333           LOAD_CONST               3 ('body')

335           LOAD_CONST               4 ('Dict[str, Any]')

333           LOAD_CONST               5 ('return')

337           LOAD_CONST               4 ('Dict[str, Any]')

333           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object expire_recommendation_route at 0x0000018C180388F0, file "app/routes/operator_learning.py", line 332>:
 332           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 338           LOAD_GLOBAL              1 (_safe_recommendation_id + NULL)
               LOAD_FAST_BORROW         0 (recommendation_id)
               CALL                     1
               STORE_FAST               3 (rid)

 339           LOAD_FAST_BORROW         3 (rid)
               POP_JUMP_IF_NOT_NONE    14 (to L2)
               NOT_TAKEN

 340           LOAD_GLOBAL              3 (HTTPException + NULL)
               LOAD_CONST               1 (400)
               LOAD_CONST               2 ('invalid recommendation_id')
               LOAD_CONST               3 (('status_code', 'detail'))
               CALL_KW                  2
               RAISE_VARARGS            1

 341   L2:     LOAD_SMALL_INT           0
               LOAD_CONST               4 (('expire_learning_recommendation',))
               IMPORT_NAME              2 (app.services.learning.recommendation_review)
               IMPORT_FROM              3 (expire_learning_recommendation)
               STORE_FAST               4 (expire_learning_recommendation)
               POP_TOP

 344           LOAD_GLOBAL              9 (_surface_review + NULL)

 345           LOAD_CONST               5 ('ops.learning.recommendations.expire')

 346           LOAD_FAST_BORROW         1 (body)

 347           LOAD_FAST_BORROW         4 (expire_learning_recommendation)

 348           LOAD_FAST_BORROW         3 (rid)

 344           LOAD_CONST               6 (('surface_name', 'body', 'handler', 'recommendation_id'))
               CALL_KW                  4
               RETURN_VALUE

  --   L3:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L3 [0] lasti
```
