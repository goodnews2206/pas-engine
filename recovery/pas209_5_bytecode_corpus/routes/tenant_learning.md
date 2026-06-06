# routes/tenant_learning

- **pyc:** `app\routes\__pycache__\tenant_learning.cpython-314.pyc`
- **expected source path (absent):** `app\routes/tenant_learning.py`
- **co_filename (from bytecode):** `app/routes/tenant_learning.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** routes

## Module docstring

```
PAS180 — Tenant-safe learning recommendation visibility routes.

Bounded read-only surfaces for the tenant-side portal. Mounted
at ``/tenant/learning``. Auth: X-API-Key via
``require_brokerage`` — same model as
``app/routes/tenant_portal.py``.

Doctrine:

* **Tenant-auth only.** No admin path here.
* **Brokerage-scoped only.** Every helper unpacks the
  brokerage_id from the resolved brokerage dict; the route
  takes the brokerage from auth, never from URL.
* **Read-only.** No mutation routes; tenants CANNOT transition
  recommendation status.
* **Closed tenant allow-list projection.** Drops source_id,
  recommended_action, rationale_token, metadata, reviewed_by_*,
  warning_count.
* **Defensive forbidden-field scan** on every response.
* **NEVER raises.**

Routes (all GET):

    GET /tenant/learning/recommendations
    GET /tenant/learning/recommendations/{recommendation_id}
```

## Imports

`APIRouter`, `Any`, `Depends`, `Dict`, `HTTPException`, `Header`, `Optional`, `Query`, `__future__`, `annotations`, `app.db.brokerage_store`, `app.services.learning.recommendation_projection`, `app.services.learning.recommendation_review`, `fastapi`, `get_brokerage_by_api_key`, `get_learning_recommendation`, `list_learning_recommendations`, `logging`, `project_tenant_list`, `project_tenant_view`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_int`, `_final_envelope`, `_resolve_brokerage_id`, `_scan_for_forbidden`, `require_brokerage`, `tenant_recommendation_get_route`, `tenant_recommendations_route`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS180 — Tenant-safe learning recommendation visibility routes.\n\nBounded read-only surfaces for the tenant-side portal. Mounted\nat ``/tenant/learning``. Auth: X-API-Key via\n``require_brokerage`` — same model as\n``app/routes/tenant_portal.py``.\n\nDoctrine:\n\n* **Tenant-auth only.** No admin path here.\n* **Brokerage-scoped only.** Every helper unpacks the\n  brokerage_id from the resolved brokerage dict; the route\n  takes the brokerage from auth, never from URL.\n* **Read-only.** No mutation routes; tenants CANNOT transition\n  recommendation status.\n* **Closed tenant allow-list projection.** Drops source_id,\n  recommended_action, rationale_token, metadata, reviewed_by_*,\n  warning_count.\n* **Defensive forbidden-field scan** on every response.\n* **NEVER raises.**\n\nRoutes (all GET):\n\n    GET /tenant/learning/recommendations\n    GET /tenant/learning/recommendations/{recommendation_id}\n'
- 'pas.tenant.learning'
- '/recommendations'
- '/recommendations/{recommendation_id}'
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
- 'tenant_learning surface='
- ' collapsed — forbidden token leaked'
- 'status'
- 'failed'
- 'error_code'
- 'tenant_envelope_forbidden_field'
- 'warnings'
- 'value'
- 'int'
- 'default'
- 'brokerage'
- 'limit'
- "Tenant-safe list of learning recommendations for the\ncaller's brokerage. Closed-shape projection drops every\noperator internal."
- 'rows'
- 'skipped'
- 'tenant.learning.recommendations.list'
- 'brokerage_id'
- 'payload'
- 'count'
- 'tenant_learning list error type='
- 'unexpected:'
- 'recommendation_id'
- 'Tenant-safe single recommendation. Cross-brokerage\nattempts are blocked at the service layer (the get helper\nscopes by brokerage_id from auth, not from URL).'
- 'tenant.learning.recommendations.get'
- 'record'
- 'tenant_learning get error type='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS180 — Tenant-safe learning recommendation visibility routes.\n\nBounded read-only surfaces for the tenant-side portal. Mounted\nat ``/tenant/learning``. Auth: X-API-Key via\n``require_brokerage`` — same model as\n``app/routes/tenant_portal.py``.\n\nDoctrine:\n\n* **Tenant-auth only.** No admin path here.\n* **Brokerage-scoped only.** Every helper unpacks the\n  brokerage_id from the resolved brokerage dict; the route\n  takes the brokerage from auth, never from URL.\n* **Read-only.** No mutation routes; tenants CANNOT transition\n  recommendation status.\n* **Closed tenant allow-list projection.** Drops source_id,\n  recommended_action, rationale_token, metadata, reviewed_by_*,\n  warning_count.\n* **Defensive forbidden-field scan** on every response.\n* **NEVER raises.**\n\nRoutes (all GET):\n\n    GET /tenant/learning/recommendations\n    GET /tenant/learning/recommendations/{recommendation_id}\n')
              STORE_NAME               0 (__doc__)

 29           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 31           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 32           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (Optional)
              STORE_NAME               7 (Optional)
              POP_TOP

 34           LOAD_SMALL_INT           0
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

 36           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('get_brokerage_by_api_key',))
              IMPORT_NAME             14 (app.db.brokerage_store)
              IMPORT_FROM             15 (get_brokerage_by_api_key)
              STORE_NAME              15 (get_brokerage_by_api_key)
              POP_TOP

 39           LOAD_NAME                9 (APIRouter)
              PUSH_NULL
              CALL                     0
              STORE_NAME              16 (router)

 40           LOAD_NAME                3 (logging)
              LOAD_ATTR               34 (getLogger)
              PUSH_NULL
              LOAD_CONST               6 ('pas.tenant.learning')
              CALL                     1
              STORE_NAME              18 (logger)

 43           LOAD_NAME               11 (Header)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              CALL                     1
              BUILD_TUPLE              1
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA2D30, file "app/routes/tenant_learning.py", line 43>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object require_brokerage at 0x0000018C17FE13E0, file "app/routes/tenant_learning.py", line 43>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              19 (require_brokerage)

 52           LOAD_CONST              25 (('phone', 'email', 'name_token', 'raw_payload', 'raw_email', 'raw_body', 'transcript', 'summary_text', 'secret', 'signature', 'dedupe_key', 'callback_notes', 'operator_notes', 'action_id', 'actor_id', 'env_value', 'env_values', 'slack_internal', 'memory_candidate', 'rationale_text', 'rationale_freeform', 'prompt_text', 'live_mutation_payload', 'recommended_action', 'source_id'))
              STORE_NAME              20 (_FORBIDDEN_TENANT_FIELDS)

 69           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA3A50, file "app/routes/tenant_learning.py", line 69>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _scan_for_forbidden at 0x0000018C18025030, file "app/routes/tenant_learning.py", line 69>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (_scan_for_forbidden)

 93           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C18025E30, file "app/routes/tenant_learning.py", line 93>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _final_envelope at 0x0000018C17FE1A70, file "app/routes/tenant_learning.py", line 93>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (_final_envelope)

109           LOAD_SMALL_INT          50
              STORE_NAME              23 (_LIST_LIMIT_DEFAULT)

110           LOAD_SMALL_INT         200
              STORE_NAME              24 (_LIST_LIMIT_MAX)

113           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C18025A30, file "app/routes/tenant_learning.py", line 113>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _clamp_int at 0x0000018C18038DF0, file "app/routes/tenant_learning.py", line 113>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_clamp_int)

125           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA3000, file "app/routes/tenant_learning.py", line 125>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _resolve_brokerage_id at 0x0000018C1804CD30, file "app/routes/tenant_learning.py", line 125>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_resolve_brokerage_id)

138           LOAD_NAME               16 (router)
              LOAD_ATTR               55 (get + NULL|self)
              LOAD_CONST              18 ('/recommendations')
              CALL                     1

140           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT          64
              LOAD_CONST              19 (('max_length',))
              CALL_KW                  2

141           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_NAME               23 (_LIST_LIMIT_DEFAULT)
              CALL                     1

142           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               19 (require_brokerage)
              CALL                     1

139           BUILD_TUPLE              3
              LOAD_CONST              20 (<code object __annotate__ at 0x0000018C18026430, file "app/routes/tenant_learning.py", line 139>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object tenant_recommendations_route at 0x0000018C17D78D60, file "app/routes/tenant_learning.py", line 138>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

138           CALL                     0

139           STORE_NAME              28 (tenant_recommendations_route)

188           LOAD_NAME               16 (router)
              LOAD_ATTR               55 (get + NULL|self)
              LOAD_CONST              22 ('/recommendations/{recommendation_id}')
              CALL                     1

191           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               19 (require_brokerage)
              CALL                     1

189           BUILD_TUPLE              1
              LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA2C40, file "app/routes/tenant_learning.py", line 189>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object tenant_recommendation_get_route at 0x0000018C17F84C80, file "app/routes/tenant_learning.py", line 188>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

188           CALL                     0

189           STORE_NAME              29 (tenant_recommendation_get_route)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app/routes/tenant_learning.py", line 43>:
 43           RESUME                   0
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

Disassembly of <code object require_brokerage at 0x0000018C17FE13E0, file "app/routes/tenant_learning.py", line 43>:
 43           RESUME                   0

 44           LOAD_GLOBAL              1 (get_brokerage_by_api_key + NULL)
              LOAD_FAST_BORROW         0 (x_api_key)
              CALL                     1
              STORE_FAST               1 (brokerage)

 45           LOAD_FAST_BORROW         1 (brokerage)
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

 46   L1:     LOAD_GLOBAL              5 (HTTPException + NULL)
              LOAD_CONST               2 (401)
              LOAD_CONST               3 ('Invalid API key')
              LOAD_CONST               4 (('status_code', 'detail'))
              CALL_KW                  2
              RAISE_VARARGS            1

 47   L2:     LOAD_FAST_BORROW         1 (brokerage)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app/routes/tenant_learning.py", line 69>:
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

Disassembly of <code object _scan_for_forbidden at 0x0000018C18025030, file "app/routes/tenant_learning.py", line 69>:
  --           MAKE_CELL                1 (walk)

  69           RESUME                   0

  70           LOAD_CONST               0 (<code object __annotate__ at 0x0000018C17FA2A60, file "app/routes/tenant_learning.py", line 70>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object walk at 0x0000018C17CC1F60, file "app/routes/tenant_learning.py", line 70>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

  90           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app/routes/tenant_learning.py", line 70>:
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

Disassembly of <code object walk at 0x0000018C17CC1F60, file "app/routes/tenant_learning.py", line 70>:
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

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app/routes/tenant_learning.py", line 93>:
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

Disassembly of <code object _final_envelope at 0x0000018C17FE1A70, file "app/routes/tenant_learning.py", line 93>:
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

 97           LOAD_CONST               0 ('tenant_learning surface=')
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

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app/routes/tenant_learning.py", line 113>:
113           RESUME                   0
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

Disassembly of <code object _clamp_int at 0x0000018C18038DF0, file "app/routes/tenant_learning.py", line 113>:
 113           RESUME                   0

 114           NOP

 115   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

 118   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 119           LOAD_FAST                1 (lo)
               RETURN_VALUE

 120   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 121           LOAD_FAST                2 (hi)
               RETURN_VALUE

 122   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 116           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

 117           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 116   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "app/routes/tenant_learning.py", line 125>:
125           RESUME                   0
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

Disassembly of <code object _resolve_brokerage_id at 0x0000018C1804CD30, file "app/routes/tenant_learning.py", line 125>:
125           RESUME                   0

126           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

127           LOAD_CONST               0 (None)
              RETURN_VALUE

128   L1:     LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('id')
              CALL                     1
              STORE_FAST               1 (bid)

129           LOAD_GLOBAL              1 (isinstance + NULL)
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

130   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

131   L3:     LOAD_FAST_BORROW         1 (bid)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "app/routes/tenant_learning.py", line 139>:
139           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

140           LOAD_CONST               2 ('Optional[str]')

139           LOAD_CONST               3 ('limit')

141           LOAD_CONST               4 ('int')

139           LOAD_CONST               5 ('return')

143           LOAD_CONST               6 ('Dict[str, Any]')

139           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object tenant_recommendations_route at 0x0000018C17D78D60, file "app/routes/tenant_learning.py", line 138>:
 138            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 147            LOAD_GLOBAL              1 (_resolve_brokerage_id + NULL)
                LOAD_FAST_BORROW         2 (brokerage)
                CALL                     1
                STORE_FAST               3 (bid)

 148            LOAD_FAST_BORROW         3 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 149            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               2 (401)
                LOAD_CONST               3 ('Invalid API key')
                LOAD_CONST               4 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 150    L2:     LOAD_GLOBAL              5 (_clamp_int + NULL)
                LOAD_FAST_BORROW         1 (limit)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              6 (_LIST_LIMIT_MAX)
                LOAD_GLOBAL              8 (_LIST_LIMIT_DEFAULT)
                CALL                     4
                STORE_FAST               4 (capped)

 151            LOAD_SMALL_INT           0
                LOAD_CONST               5 (('list_learning_recommendations',))
                IMPORT_NAME              5 (app.services.learning.recommendation_review)
                IMPORT_FROM              6 (list_learning_recommendations)
                STORE_FAST               5 (list_learning_recommendations)
                POP_TOP

 154            LOAD_SMALL_INT           0
                LOAD_CONST               6 (('project_tenant_list',))
                IMPORT_NAME              7 (app.services.learning.recommendation_projection)
                IMPORT_FROM              8 (project_tenant_list)
                STORE_FAST               6 (project_tenant_list)
                POP_TOP

 157    L3:     NOP

 158    L4:     LOAD_FAST_BORROW         5 (list_learning_recommendations)
                PUSH_NULL

 159            LOAD_FAST_BORROW         3 (bid)

 160            LOAD_FAST_BORROW         0 (status)

 161            LOAD_FAST_BORROW         4 (capped)

 158            LOAD_CONST               7 (('brokerage_id', 'status', 'limit'))
                CALL_KW                  3
                STORE_FAST               7 (result)

 163            LOAD_FAST                6 (project_tenant_list)
                PUSH_NULL
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               8 ('rows')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                BUILD_LIST               0
        L7:     CALL                     1
                STORE_FAST               8 (projected)

 165            LOAD_CONST               9 ('status')
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               9 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                LOAD_CONST              10 ('skipped')

 166   L10:     LOAD_CONST              11 ('surface')
                LOAD_CONST              12 ('tenant.learning.recommendations.list')

 167            LOAD_CONST              13 ('brokerage_id')
                LOAD_FAST                3 (bid)

 168            LOAD_CONST              14 ('payload')

 169            LOAD_CONST               8 ('rows')
                LOAD_FAST_BORROW         8 (projected)

 170            LOAD_CONST              15 ('count')
                LOAD_GLOBAL             21 (len + NULL)
                LOAD_FAST_BORROW         8 (projected)
                CALL                     1

 168            BUILD_MAP                2

 172            LOAD_CONST              16 ('warnings')
                LOAD_GLOBAL             23 (list + NULL)
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              16 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                BUILD_LIST               0
       L13:     CALL                     1

 173            LOAD_CONST              17 ('error_code')
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              17 ('error_code')
                CALL                     1

 164            BUILD_MAP                6
                STORE_FAST               9 (env)

 185   L14:     LOAD_GLOBAL             35 (_final_envelope + NULL)
                LOAD_FAST_BORROW         9 (env)
                LOAD_CONST              12 ('tenant.learning.recommendations.list')
                LOAD_CONST              21 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 175            LOAD_GLOBAL             24 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L19)
                NOT_TAKEN
                STORE_FAST              10 (e)

 176   L16:     LOAD_GLOBAL             26 (logger)
                LOAD_ATTR               29 (warning + NULL|self)

 177            LOAD_CONST              18 ('tenant_learning list error type=')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 176            CALL                     1
                POP_TOP

 180            LOAD_CONST               9 ('status')
                LOAD_CONST              19 ('failed')

 181            LOAD_CONST              11 ('surface')
                LOAD_CONST              12 ('tenant.learning.recommendations.list')

 182            LOAD_CONST              17 ('error_code')
                LOAD_CONST              20 ('unexpected:')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 183            LOAD_CONST              16 ('warnings')
                BUILD_LIST               0

 179            BUILD_MAP                4
                STORE_FAST               9 (env)
       L17:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L14)

  --   L18:     LOAD_CONST               1 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 175   L19:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app/routes/tenant_learning.py", line 189>:
189           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendation_id')

190           LOAD_CONST               2 ('str')

189           LOAD_CONST               3 ('return')

192           LOAD_CONST               4 ('Dict[str, Any]')

189           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object tenant_recommendation_get_route at 0x0000018C17F84C80, file "app/routes/tenant_learning.py", line 188>:
 188            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 196            LOAD_GLOBAL              1 (_resolve_brokerage_id + NULL)
                LOAD_FAST_BORROW         1 (brokerage)
                CALL                     1
                STORE_FAST               2 (bid)

 197            LOAD_FAST_BORROW         2 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 198            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               2 (401)
                LOAD_CONST               3 ('Invalid API key')
                LOAD_CONST               4 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 199    L2:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('get_learning_recommendation',))
                IMPORT_NAME              2 (app.services.learning.recommendation_review)
                IMPORT_FROM              3 (get_learning_recommendation)
                STORE_FAST               3 (get_learning_recommendation)
                POP_TOP

 202            LOAD_SMALL_INT           0
                LOAD_CONST               6 (('project_tenant_view',))
                IMPORT_NAME              4 (app.services.learning.recommendation_projection)
                IMPORT_FROM              5 (project_tenant_view)
                STORE_FAST               4 (project_tenant_view)
                POP_TOP

 205    L3:     NOP

 206    L4:     LOAD_FAST_BORROW         3 (get_learning_recommendation)
                PUSH_NULL

 207            LOAD_FAST_BORROW         0 (recommendation_id)

 208            LOAD_FAST_BORROW         2 (bid)

 206            LOAD_CONST               7 (('recommendation_id', 'brokerage_id'))
                CALL_KW                  2
                STORE_FAST               5 (result)

 211            LOAD_CONST               8 ('status')
                LOAD_FAST_BORROW         5 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               8 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                LOAD_CONST               9 ('skipped')

 212    L7:     LOAD_CONST              10 ('surface')
                LOAD_CONST              11 ('tenant.learning.recommendations.get')

 213            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST                2 (bid)

 214            LOAD_CONST              13 ('payload')
                LOAD_FAST                4 (project_tenant_view)
                PUSH_NULL
                LOAD_FAST_BORROW         5 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              14 ('record')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                BUILD_MAP                0
       L10:     CALL                     1

 215            LOAD_CONST              15 ('warnings')
                LOAD_GLOBAL             15 (list + NULL)
                LOAD_FAST_BORROW         5 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              15 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                BUILD_LIST               0
       L13:     CALL                     1

 216            LOAD_CONST              16 ('error_code')
                LOAD_FAST_BORROW         5 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              16 ('error_code')
                CALL                     1

 210            BUILD_MAP                6
                STORE_FAST               6 (env)

 228   L14:     LOAD_GLOBAL             27 (_final_envelope + NULL)
                LOAD_FAST_BORROW         6 (env)
                LOAD_CONST              11 ('tenant.learning.recommendations.get')
                LOAD_CONST              20 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 218            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L19)
                NOT_TAKEN
                STORE_FAST               7 (e)

 219   L16:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 220            LOAD_CONST              17 ('tenant_learning get error type=')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 219            CALL                     1
                POP_TOP

 223            LOAD_CONST               8 ('status')
                LOAD_CONST              18 ('failed')

 224            LOAD_CONST              10 ('surface')
                LOAD_CONST              11 ('tenant.learning.recommendations.get')

 225            LOAD_CONST              16 ('error_code')
                LOAD_CONST              19 ('unexpected:')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 226            LOAD_CONST              15 ('warnings')
                BUILD_LIST               0

 222            BUILD_MAP                4
                STORE_FAST               6 (env)
       L17:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L14)

  --   L18:     LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 218   L19:     RERAISE                  0

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
```
