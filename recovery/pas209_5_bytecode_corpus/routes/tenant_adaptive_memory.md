# routes/tenant_adaptive_memory

- **pyc:** `app\routes\__pycache__\tenant_adaptive_memory.cpython-314.pyc`
- **expected source path (absent):** `app\routes/tenant_adaptive_memory.py`
- **co_filename (from bytecode):** `app/routes/tenant_adaptive_memory.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** routes

## Module docstring

```
PAS182 — Tenant adaptive-memory bridge-status route.

Bounded read-only surface for the tenant-side portal. Mounted
at ``/tenant/learning``. Auth: X-API-Key via
``require_brokerage``.

Doctrine:

* **Tenant-auth only.** No admin path here.
* **Brokerage-scoped only.** Every helper unpacks
  ``brokerage_id`` from the resolved brokerage dict.
* **Read-only.** No mutation routes; tenants CANNOT bridge,
  approve, or reject.
* **Closed tenant projection.** Drops recommendation_id,
  test_run_id, memory_candidate_id, evidence_fingerprint,
  actor_type, actor_id, warning_count, error_code.
* **Defensive forbidden-field scan** on every response.
* **NEVER raises.**

Routes:

    GET /tenant/learning/adaptive-memory/bridge-status
```

## Imports

`APIRouter`, `Any`, `Depends`, `Dict`, `HTTPException`, `Header`, `Optional`, `Query`, `__future__`, `adaptive_memory_bridge_report`, `annotations`, `app.db.brokerage_store`, `app.db.event_logger`, `app.services.learning.adaptive_memory_bridge`, `app.services.learning.adaptive_memory_projection`, `fastapi`, `get_brokerage_by_api_key`, `log_event`, `logging`, `project_tenant_bridge_list`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_int`, `_final_envelope`, `_resolve_brokerage_id`, `_scan_for_forbidden`, `bridge_status_route`, `require_brokerage`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS182 — Tenant adaptive-memory bridge-status route.\n\nBounded read-only surface for the tenant-side portal. Mounted\nat ``/tenant/learning``. Auth: X-API-Key via\n``require_brokerage``.\n\nDoctrine:\n\n* **Tenant-auth only.** No admin path here.\n* **Brokerage-scoped only.** Every helper unpacks\n  ``brokerage_id`` from the resolved brokerage dict.\n* **Read-only.** No mutation routes; tenants CANNOT bridge,\n  approve, or reject.\n* **Closed tenant projection.** Drops recommendation_id,\n  test_run_id, memory_candidate_id, evidence_fingerprint,\n  actor_type, actor_id, warning_count, error_code.\n* **Defensive forbidden-field scan** on every response.\n* **NEVER raises.**\n\nRoutes:\n\n    GET /tenant/learning/adaptive-memory/bridge-status\n'
- 'pas.tenant.adaptive_memory'
- '/adaptive-memory/bridge-status'
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
- 'tenant_adaptive_memory surface='
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
- "Tenant-safe view of adaptive-memory bridge activity for\nthe caller's brokerage. Closed-shape projection drops every\noperator internal."
- 'tenant.learning.adaptive_memory.viewed'
- 'broker'
- 'tenant_adaptive_memory'
- 'tenant.learning.adaptive_memory.bridge_status'
- 'rows'
- 'skipped'
- 'brokerage_id'
- 'payload'
- 'count'
- 'tenant_adaptive_memory status error type='
- 'unexpected:'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS182 — Tenant adaptive-memory bridge-status route.\n\nBounded read-only surface for the tenant-side portal. Mounted\nat ``/tenant/learning``. Auth: X-API-Key via\n``require_brokerage``.\n\nDoctrine:\n\n* **Tenant-auth only.** No admin path here.\n* **Brokerage-scoped only.** Every helper unpacks\n  ``brokerage_id`` from the resolved brokerage dict.\n* **Read-only.** No mutation routes; tenants CANNOT bridge,\n  approve, or reject.\n* **Closed tenant projection.** Drops recommendation_id,\n  test_run_id, memory_candidate_id, evidence_fingerprint,\n  actor_type, actor_id, warning_count, error_code.\n* **Defensive forbidden-field scan** on every response.\n* **NEVER raises.**\n\nRoutes:\n\n    GET /tenant/learning/adaptive-memory/bridge-status\n')
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

 33           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('get_brokerage_by_api_key',))
              IMPORT_NAME             14 (app.db.brokerage_store)
              IMPORT_FROM             15 (get_brokerage_by_api_key)
              STORE_NAME              15 (get_brokerage_by_api_key)
              POP_TOP

 36           LOAD_NAME                9 (APIRouter)
              PUSH_NULL
              CALL                     0
              STORE_NAME              16 (router)

 37           LOAD_NAME                3 (logging)
              LOAD_ATTR               34 (getLogger)
              PUSH_NULL
              LOAD_CONST               6 ('pas.tenant.adaptive_memory')
              CALL                     1
              STORE_NAME              18 (logger)

 40           LOAD_NAME               11 (Header)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              CALL                     1
              BUILD_TUPLE              1
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA34B0, file "app/routes/tenant_adaptive_memory.py", line 40>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object require_brokerage at 0x0000018C17FE13E0, file "app/routes/tenant_adaptive_memory.py", line 40>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              19 (require_brokerage)

 49           LOAD_CONST              21 (('phone', 'email', 'name_token', 'raw_payload', 'raw_email', 'raw_body', 'transcript', 'summary_text', 'secret', 'signature', 'dedupe_key', 'callback_notes', 'operator_notes', 'action_id', 'actor_id', 'env_value', 'env_values', 'slack_internal', 'memory_candidate', 'rationale_text', 'rationale_freeform', 'prompt_text', 'live_mutation_payload', 'evidence_fingerprint', 'evidence_raw', 'recommendation_id', 'scenario_fingerprint', 'test_run_id', 'memory_candidate_id'))
              STORE_NAME              20 (_FORBIDDEN_TENANT_FIELDS)

 70           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA2D30, file "app/routes/tenant_adaptive_memory.py", line 70>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _scan_for_forbidden at 0x0000018C18025C30, file "app/routes/tenant_adaptive_memory.py", line 70>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (_scan_for_forbidden)

 94           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C18025030, file "app/routes/tenant_adaptive_memory.py", line 94>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _final_envelope at 0x0000018C17FE1A70, file "app/routes/tenant_adaptive_memory.py", line 94>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (_final_envelope)

110           LOAD_SMALL_INT          50
              STORE_NAME              23 (_LIST_LIMIT_DEFAULT)

111           LOAD_SMALL_INT         200
              STORE_NAME              24 (_LIST_LIMIT_MAX)

114           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C18025E30, file "app/routes/tenant_adaptive_memory.py", line 114>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _clamp_int at 0x0000018C18038B70, file "app/routes/tenant_adaptive_memory.py", line 114>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_clamp_int)

126           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA2A60, file "app/routes/tenant_adaptive_memory.py", line 126>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _resolve_brokerage_id at 0x0000018C1804D070, file "app/routes/tenant_adaptive_memory.py", line 126>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_resolve_brokerage_id)

139           LOAD_NAME               16 (router)
              LOAD_ATTR               55 (get + NULL|self)
              LOAD_CONST              18 ('/adaptive-memory/bridge-status')
              CALL                     1

141           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_NAME               23 (_LIST_LIMIT_DEFAULT)
              CALL                     1

142           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               19 (require_brokerage)
              CALL                     1

140           BUILD_TUPLE              2
              LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA3000, file "app/routes/tenant_adaptive_memory.py", line 140>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object bridge_status_route at 0x0000018C17F842E0, file "app/routes/tenant_adaptive_memory.py", line 139>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

139           CALL                     0

140           STORE_NAME              28 (bridge_status_route)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app/routes/tenant_adaptive_memory.py", line 40>:
 40           RESUME                   0
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

Disassembly of <code object require_brokerage at 0x0000018C17FE13E0, file "app/routes/tenant_adaptive_memory.py", line 40>:
 40           RESUME                   0

 41           LOAD_GLOBAL              1 (get_brokerage_by_api_key + NULL)
              LOAD_FAST_BORROW         0 (x_api_key)
              CALL                     1
              STORE_FAST               1 (brokerage)

 42           LOAD_FAST_BORROW         1 (brokerage)
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

 43   L1:     LOAD_GLOBAL              5 (HTTPException + NULL)
              LOAD_CONST               2 (401)
              LOAD_CONST               3 ('Invalid API key')
              LOAD_CONST               4 (('status_code', 'detail'))
              CALL_KW                  2
              RAISE_VARARGS            1

 44   L2:     LOAD_FAST_BORROW         1 (brokerage)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app/routes/tenant_adaptive_memory.py", line 70>:
 70           RESUME                   0
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

Disassembly of <code object _scan_for_forbidden at 0x0000018C18025C30, file "app/routes/tenant_adaptive_memory.py", line 70>:
  --           MAKE_CELL                1 (walk)

  70           RESUME                   0

  71           LOAD_CONST               0 (<code object __annotate__ at 0x0000018C17FA3A50, file "app/routes/tenant_adaptive_memory.py", line 71>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object walk at 0x0000018C17CC2460, file "app/routes/tenant_adaptive_memory.py", line 71>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

  91           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app/routes/tenant_adaptive_memory.py", line 71>:
 71           RESUME                   0
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

Disassembly of <code object walk at 0x0000018C17CC2460, file "app/routes/tenant_adaptive_memory.py", line 71>:
  --            COPY_FREE_VARS           1

  71            RESUME                   0

  72            NOP

  73    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      111 (to L16)
        L2:     NOT_TAKEN

  74    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                88 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

  75            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L10)
                NOT_TAKEN

  76            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

  77            LOAD_GLOBAL             10 (_FORBIDDEN_TENANT_FIELDS)
                GET_ITER
        L5:     FOR_ITER                15 (to L9)
                STORE_FAST               4 (tok)

  78            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)

  79    L7:     LOAD_FAST_BORROW         4 (tok)
                SWAP                     2
                POP_TOP
                SWAP                     2
                POP_TOP
        L8:     RETURN_VALUE

  77    L9:     END_FOR
                POP_ITER

  80   L10:     LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

  81            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           86 (to L4)

  82   L12:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L13:     RETURN_VALUE

  74   L14:     END_FOR
                POP_ITER

  90   L15:     LOAD_CONST               0 (None)
                RETURN_VALUE

  83   L16:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             12 (list)
                LOAD_GLOBAL             14 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L22)
                NOT_TAKEN

  84            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L17:     FOR_ITER                23 (to L21)
                STORE_FAST               2 (v)

  85            LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

  86            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           21 (to L17)

  87   L19:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L20:     RETURN_VALUE

  84   L21:     END_FOR
                POP_ITER

  90   L22:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

  88            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L25)
                NOT_TAKEN
                POP_TOP

  89   L24:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

  88   L25:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "app/routes/tenant_adaptive_memory.py", line 94>:
 94           RESUME                   0
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

Disassembly of <code object _final_envelope at 0x0000018C17FE1A70, file "app/routes/tenant_adaptive_memory.py", line 94>:
 94           RESUME                   0

 95           LOAD_GLOBAL              1 (_scan_for_forbidden + NULL)
              LOAD_FAST_BORROW         0 (env)
              CALL                     1
              STORE_FAST               2 (leak)

 96           LOAD_FAST_BORROW         2 (leak)
              TO_BOOL
              POP_JUMP_IF_FALSE       37 (to L1)
              NOT_TAKEN

 97           LOAD_GLOBAL              2 (logger)
              LOAD_ATTR                5 (warning + NULL|self)

 98           LOAD_CONST               0 ('tenant_adaptive_memory surface=')
              LOAD_FAST_BORROW         1 (surface)
              FORMAT_SIMPLE
              LOAD_CONST               1 (' collapsed — forbidden token leaked')
              BUILD_STRING             3

 97           CALL                     1
              POP_TOP

102           LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('failed')

103           LOAD_CONST               4 ('surface')
              LOAD_FAST_BORROW         1 (surface)

104           LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('tenant_envelope_forbidden_field')

105           LOAD_CONST               7 ('warnings')
              LOAD_CONST               6 ('tenant_envelope_forbidden_field')
              BUILD_LIST               1

101           BUILD_MAP                4
              RETURN_VALUE

107   L1:     LOAD_FAST_BORROW         0 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app/routes/tenant_adaptive_memory.py", line 114>:
114           RESUME                   0
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

Disassembly of <code object _clamp_int at 0x0000018C18038B70, file "app/routes/tenant_adaptive_memory.py", line 114>:
 114           RESUME                   0

 115           NOP

 116   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

 119   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 120           LOAD_FAST                1 (lo)
               RETURN_VALUE

 121   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 122           LOAD_FAST                2 (hi)
               RETURN_VALUE

 123   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 117           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

 118           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 117   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app/routes/tenant_adaptive_memory.py", line 126>:
126           RESUME                   0
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

Disassembly of <code object _resolve_brokerage_id at 0x0000018C1804D070, file "app/routes/tenant_adaptive_memory.py", line 126>:
126           RESUME                   0

127           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

128           LOAD_CONST               0 (None)
              RETURN_VALUE

129   L1:     LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('id')
              CALL                     1
              STORE_FAST               1 (bid)

130           LOAD_GLOBAL              1 (isinstance + NULL)
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

131   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

132   L3:     LOAD_FAST_BORROW         1 (bid)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "app/routes/tenant_adaptive_memory.py", line 140>:
140           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('limit')

141           LOAD_CONST               2 ('int')

140           LOAD_CONST               3 ('return')

143           LOAD_CONST               4 ('Dict[str, Any]')

140           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object bridge_status_route at 0x0000018C17F842E0, file "app/routes/tenant_adaptive_memory.py", line 139>:
 139            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 147            LOAD_GLOBAL              1 (_resolve_brokerage_id + NULL)
                LOAD_FAST_BORROW         1 (brokerage)
                CALL                     1
                STORE_FAST               2 (bid)

 148            LOAD_FAST_BORROW         2 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 149            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               2 (401)
                LOAD_CONST               3 ('Invalid API key')
                LOAD_CONST               4 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 150    L2:     LOAD_GLOBAL              5 (_clamp_int + NULL)
                LOAD_FAST_BORROW         0 (limit)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              6 (_LIST_LIMIT_MAX)
                LOAD_GLOBAL              8 (_LIST_LIMIT_DEFAULT)
                CALL                     4
                STORE_FAST               3 (capped)

 152            LOAD_SMALL_INT           0
                LOAD_CONST               5 (('adaptive_memory_bridge_report',))
                IMPORT_NAME              5 (app.services.learning.adaptive_memory_bridge)
                IMPORT_FROM              6 (adaptive_memory_bridge_report)
                STORE_FAST               4 (adaptive_memory_bridge_report)
                POP_TOP

 155            LOAD_SMALL_INT           0
                LOAD_CONST               6 (('project_tenant_bridge_list',))
                IMPORT_NAME              7 (app.services.learning.adaptive_memory_projection)
                IMPORT_FROM              8 (project_tenant_bridge_list)
                STORE_FAST               5 (project_tenant_bridge_list)
                POP_TOP

 159    L3:     NOP

 160    L4:     LOAD_SMALL_INT           0
                LOAD_CONST               7 (('log_event',))
                IMPORT_NAME              9 (app.db.event_logger)
                IMPORT_FROM             10 (log_event)
                STORE_FAST               6 (_log_event)
                POP_TOP

 161            LOAD_FAST_BORROW         6 (_log_event)
                PUSH_NULL

 162            LOAD_CONST               8 ('tenant.learning.adaptive_memory.viewed')

 163            LOAD_FAST_BORROW         2 (bid)

 164            LOAD_CONST               9 ('broker')

 165            LOAD_CONST              10 ('tenant_adaptive_memory')

 166            LOAD_CONST              11 ('surface')
                LOAD_CONST              12 ('tenant.learning.adaptive_memory.bridge_status')
                BUILD_MAP                1

 161            LOAD_CONST              13 (('brokerage_id', 'actor', 'event_source', 'payload'))
                CALL_KW                  5
                POP_TOP

 171    L5:     NOP

 172    L6:     LOAD_FAST_BORROW         4 (adaptive_memory_bridge_report)
                PUSH_NULL

 173            LOAD_FAST_BORROW         2 (bid)

 174            LOAD_FAST_BORROW         3 (capped)

 172            LOAD_CONST              14 (('brokerage_id', 'limit'))
                CALL_KW                  2
                STORE_FAST               7 (result)

 176            LOAD_FAST                5 (project_tenant_bridge_list)
                PUSH_NULL
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              15 ('rows')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
        L7:     NOT_TAKEN
        L8:     POP_TOP
                BUILD_LIST               0
        L9:     CALL                     1
                STORE_FAST               8 (projected)

 178            LOAD_CONST              16 ('status')
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              16 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
       L10:     NOT_TAKEN
       L11:     POP_TOP
                LOAD_CONST              17 ('skipped')

 179   L12:     LOAD_CONST              11 ('surface')
                LOAD_CONST              12 ('tenant.learning.adaptive_memory.bridge_status')

 180            LOAD_CONST              18 ('brokerage_id')
                LOAD_FAST                2 (bid)

 181            LOAD_CONST              19 ('payload')

 182            LOAD_CONST              15 ('rows')
                LOAD_FAST_BORROW         8 (projected)

 183            LOAD_CONST              20 ('count')
                LOAD_GLOBAL             27 (len + NULL)
                LOAD_FAST_BORROW         8 (projected)
                CALL                     1

 181            BUILD_MAP                2

 185            LOAD_CONST              21 ('warnings')
                LOAD_GLOBAL             29 (list + NULL)
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              21 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
       L13:     NOT_TAKEN
       L14:     POP_TOP
                BUILD_LIST               0
       L15:     CALL                     1

 186            LOAD_CONST              22 ('error_code')
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              22 ('error_code')
                CALL                     1

 177            BUILD_MAP                6
                STORE_FAST               9 (env)

 198   L16:     LOAD_GLOBAL             39 (_final_envelope + NULL)
                LOAD_FAST_BORROW         9 (env)
                LOAD_CONST              12 ('tenant.learning.adaptive_memory.bridge_status')
                LOAD_CONST              26 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L17:     PUSH_EXC_INFO

 168            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        4 (to L19)
                NOT_TAKEN
                POP_TOP

 169   L18:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 171 (to L5)

 168   L19:     RERAISE                  0

  --   L20:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L21:     PUSH_EXC_INFO

 188            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L25)
                NOT_TAKEN
                STORE_FAST              10 (e)

 189   L22:     LOAD_GLOBAL             30 (logger)
                LOAD_ATTR               33 (warning + NULL|self)

 190            LOAD_CONST              23 ('tenant_adaptive_memory status error type=')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 189            CALL                     1
                POP_TOP

 193            LOAD_CONST              16 ('status')
                LOAD_CONST              24 ('failed')

 194            LOAD_CONST              11 ('surface')
                LOAD_CONST              12 ('tenant.learning.adaptive_memory.bridge_status')

 195            LOAD_CONST              22 ('error_code')
                LOAD_CONST              25 ('unexpected:')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 196            LOAD_CONST              21 ('warnings')
                BUILD_LIST               0

 192            BUILD_MAP                4
                STORE_FAST               9 (env)
       L23:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                JUMP_BACKWARD_NO_INTERRUPT 121 (to L16)

  --   L24:     LOAD_CONST               1 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 188   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L27:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L27 [0] lasti
  L4 to L5 -> L17 [0]
  L6 to L7 -> L21 [0]
  L8 to L10 -> L21 [0]
  L11 to L13 -> L21 [0]
  L14 to L16 -> L21 [0]
  L16 to L17 -> L27 [0] lasti
  L17 to L18 -> L20 [1] lasti
  L18 to L19 -> L27 [0] lasti
  L19 to L20 -> L20 [1] lasti
  L20 to L21 -> L27 [0] lasti
  L21 to L22 -> L26 [1] lasti
  L22 to L23 -> L24 [1] lasti
  L23 to L24 -> L27 [0] lasti
  L24 to L26 -> L26 [1] lasti
  L26 to L27 -> L27 [0] lasti
```
