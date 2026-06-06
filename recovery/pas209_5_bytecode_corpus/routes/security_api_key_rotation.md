# routes/security_api_key_rotation

- **pyc:** `app\routes\__pycache__\security_api_key_rotation.cpython-314.pyc`
- **expected source path (absent):** `app\routes/security_api_key_rotation.py`
- **co_filename (from bytecode):** `app/routes/security_api_key_rotation.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** routes

## Module docstring

```
PAS-SECURITY-02 — API-key rotation routes.

Tenant-initiated + operator-approved rotation surfaces for
tenant API keys. Two routers:

* ``tenant_router`` mounted at ``/tenant/api-key`` (X-API-Key
  required). Routes:
    POST /tenant/api-key/rotation-request
    GET  /tenant/api-key/rotation-status
* ``operator_router`` mounted at ``/ops/api-key-rotation``
  (X-Admin-Key required). Routes:
    POST /ops/api-key-rotation/{rotation_id}/approve
    POST /ops/api-key-rotation/{rotation_id}/cancel
    POST /ops/api-key-rotation/{rotation_id}/fail

Doctrine:

* **No raw API key echo.** Tenant route bodies never carry
  the raw key; only an optional sha256 fingerprint of the
  current key is computed server-side from a body field.
* **Rate-limited.** Both rotation surfaces use the
  ``api_key_rotation`` policy (3 / hour / brokerage).
* **Auth enforced server-side.** Tenant routes use
  ``require_brokerage``; operator routes use
  ``require_admin``.
* **Forbidden-token scanner** on every response.
* **NEVER raises.**
```

## Imports

`ALLOWED_ACTOR_TYPES`, `APIRouter`, `Any`, `Body`, `Depends`, `Dict`, `HTTPException`, `Header`, `Optional`, `__future__`, `annotations`, `api_key_rotation_status`, `app.config`, `app.db.brokerage_store`, `app.services.learning.recommendation_review`, `app.services.security.api_key_reveal`, `app.services.security.api_key_rotation`, `app.services.security.rate_limit`, `approve_api_key_rotation`, `cancel_api_key_rotation`, `check_rate_limit`, `fail_api_key_rotation`, `fastapi`, `get_brokerage_by_api_key`, `get_settings`, `logging`, `rate_limit_public_error`, `request_api_key_rotation`, `reveal_rotated_api_key_once`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_final_envelope`, `_operator_transition`, `_project_operator`, `_project_tenant`, `_rate_limit_or_pass`, `_resolve_brokerage_id`, `_safe_bid_from_path`, `_scan_for_forbidden`, `operator_rotation_approve_route`, `operator_rotation_cancel_route`, `operator_rotation_fail_route`, `require_admin`, `require_brokerage`, `tenant_rotation_request_route`, `tenant_rotation_reveal_route`, `tenant_rotation_status_route`

## Env-key candidates

`ADMIN`, `OPERATOR`, `TENANT`

## String constants (redacted where noted)

- '\nPAS-SECURITY-02 — API-key rotation routes.\n\nTenant-initiated + operator-approved rotation surfaces for\ntenant API keys. Two routers:\n\n* ``tenant_router`` mounted at ``/tenant/api-key`` (X-API-Key\n  required). Routes:\n    POST /tenant/api-key/rotation-request\n    GET  /tenant/api-key/rotation-status\n* ``operator_router`` mounted at ``/ops/api-key-rotation``\n  (X-Admin-Key required). Routes:\n    POST /ops/api-key-rotation/{rotation_id}/approve\n    POST /ops/api-key-rotation/{rotation_id}/cancel\n    POST /ops/api-key-rotation/{rotation_id}/fail\n\nDoctrine:\n\n* **No raw API key echo.** Tenant route bodies never carry\n  the raw key; only an optional sha256 fingerprint of the\n  current key is computed server-side from a body field.\n* **Rate-limited.** Both rotation surfaces use the\n  ``api_key_rotation`` policy (3 / hour / brokerage).\n* **Auth enforced server-side.** Tenant routes use\n  ``require_brokerage``; operator routes use\n  ``require_admin``.\n* **Forbidden-token scanner** on every response.\n* **NEVER raises.**\n'
- 'pas.security.api_key_rotation_routes'
- '/rotation-request'
- '/rotation-status'
- '/rotation/{rotation_id}/reveal'
- '/{rotation_id}/approve'
- '/{rotation_id}/cancel'
- '/{rotation_id}/fail'
- 'x_api_key'
- 'str'
- 'demo'
- 'Invalid API key'
- 'x_admin_key'
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
- 'api_key'
- 'token'
- 'env'
- 'Dict[str, Any]'
- 'surface'
- 'security_api_key_rotation surface='
- ' collapsed — forbidden token leaked'
- 'status'
- 'failed'
- 'error_code'
- 'envelope_forbidden_token'
- 'warnings'
- 'brokerage'
- 'value'
- 'row'
- 'brokerage_id'
- 'actor_type'
- 'Apply the rate-limit check. Returns the public error\nenvelope on block, else None.'
- 'body'
- "Tenant entry. Inserts a REQUESTED rotation row for the\ncaller's brokerage. NEVER stores the raw key."
- 'api_key_rotation'
- 'TENANT'
- 'tenant.api_key.rotation_request'
- 'actor_token'
- 'current_api_key'
- 'payload'
- 'record'
- 'tenant_rotation_request_route error type='
- 'unexpected:'
- "Tenant read of the most-recent rotation row for the\ncaller's brokerage. NEVER returns the raw key."
- 'tenant.api_key.rotation_status'
- 'skipped'
- 'tenant_rotation_status_route error type='
- 'rotation_id'
- 'One-time reveal endpoint. Tenant presents the\nout-of-band-delivered reveal token; service verifies the\nsha256 hash against the v34 column. Raw key payload is\nDEFERRED — see [docs/pas_api_key_delivery_doctrine.md](../../docs/pas_api_key_delivery_doctrine.md)\n§5. PAS-SECURITY-04 returns ``status="deferred"`` with\n``error_code="raw_key_reveal_unsupported"`` after a\nsuccessful token verify. The reveal attempt is audit-\nlogged and the attempt counter is bumped.'
- 'tenant.api_key.rotation_reveal'
- 'reveal_token_missing'
- 'one_time'
- 'expires_at'
- 'tenant_rotation_reveal_route error type='
- 'actor_id'
- 'OPERATOR'
- 'transition'
- 'audit_row'
- '_operator_transition '
- ' error type='
- 'ops.api_key.rotation_approve'
- 'ops.api_key.rotation_cancel'
- 'ops.api_key.rotation_fail'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS-SECURITY-02 — API-key rotation routes.\n\nTenant-initiated + operator-approved rotation surfaces for\ntenant API keys. Two routers:\n\n* ``tenant_router`` mounted at ``/tenant/api-key`` (X-API-Key\n  required). Routes:\n    POST /tenant/api-key/rotation-request\n    GET  /tenant/api-key/rotation-status\n* ``operator_router`` mounted at ``/ops/api-key-rotation``\n  (X-Admin-Key required). Routes:\n    POST /ops/api-key-rotation/{rotation_id}/approve\n    POST /ops/api-key-rotation/{rotation_id}/cancel\n    POST /ops/api-key-rotation/{rotation_id}/fail\n\nDoctrine:\n\n* **No raw API key echo.** Tenant route bodies never carry\n  the raw key; only an optional sha256 fingerprint of the\n  current key is computed server-side from a body field.\n* **Rate-limited.** Both rotation surfaces use the\n  ``api_key_rotation`` policy (3 / hour / brokerage).\n* **Auth enforced server-side.** Tenant routes use\n  ``require_brokerage``; operator routes use\n  ``require_admin``.\n* **Forbidden-token scanner** on every response.\n* **NEVER raises.**\n')
              STORE_NAME               0 (__doc__)

 31           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 33           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 34           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (Optional)
              STORE_NAME               7 (Optional)
              POP_TOP

 36           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('APIRouter', 'Body', 'Depends', 'Header', 'HTTPException'))
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
              POP_TOP

 38           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('get_settings',))
              IMPORT_NAME             14 (app.config)
              IMPORT_FROM             15 (get_settings)
              STORE_NAME              15 (get_settings)
              POP_TOP

 39           LOAD_SMALL_INT           0
              LOAD_CONST               6 (('get_brokerage_by_api_key',))
              IMPORT_NAME             16 (app.db.brokerage_store)
              IMPORT_FROM             17 (get_brokerage_by_api_key)
              STORE_NAME              17 (get_brokerage_by_api_key)
              POP_TOP

 42           LOAD_NAME                9 (APIRouter)
              PUSH_NULL
              CALL                     0
              STORE_NAME              18 (tenant_router)

 43           LOAD_NAME                9 (APIRouter)
              PUSH_NULL
              CALL                     0
              STORE_NAME              19 (operator_router)

 45           LOAD_NAME                3 (logging)
              LOAD_ATTR               40 (getLogger)
              PUSH_NULL
              LOAD_CONST               7 ('pas.security.api_key_rotation_routes')
              CALL                     1
              STORE_NAME              21 (logger)

 52           LOAD_NAME               12 (Header)
              PUSH_NULL
              LOAD_CONST               8 (Ellipsis)
              CALL                     1
              BUILD_TUPLE              1
              LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA2C40, file "app/routes/security_api_key_rotation.py", line 52>)
              MAKE_FUNCTION
              LOAD_CONST              10 (<code object require_brokerage at 0x0000018C17FE1290, file "app/routes/security_api_key_rotation.py", line 52>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              22 (require_brokerage)

 59           LOAD_NAME               12 (Header)
              PUSH_NULL
              LOAD_CONST               8 (Ellipsis)
              CALL                     1
              BUILD_TUPLE              1
              LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA3B40, file "app/routes/security_api_key_rotation.py", line 59>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object require_admin at 0x0000018C179A7290, file "app/routes/security_api_key_rotation.py", line 59>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              23 (require_admin)

 88           LOAD_CONST              48 (('phone', 'email', 'name_token', 'raw_payload', 'raw_email', 'raw_body', 'transcript', 'summary_text', 'secret', 'signature', 'token', 'api_key', 'env_value', 'env_values', 'dedupe_key', 'callback_notes', 'rationale_text', 'stack_trace', 'traceback'))
              STORE_NAME              24 (_FORBIDDEN_RESPONSE_TOKENS)

 99           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA3960, file "app/routes/security_api_key_rotation.py", line 99>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object _scan_for_forbidden at 0x0000018C18025A30, file "app/routes/security_api_key_rotation.py", line 99>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_scan_for_forbidden)

141           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18024C30, file "app/routes/security_api_key_rotation.py", line 141>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _final_envelope at 0x0000018C17FE17D0, file "app/routes/security_api_key_rotation.py", line 141>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_final_envelope)

157           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA23D0, file "app/routes/security_api_key_rotation.py", line 157>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _resolve_brokerage_id at 0x0000018C1796DBD0, file "app/routes/security_api_key_rotation.py", line 157>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_resolve_brokerage_id)

166           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA2880, file "app/routes/security_api_key_rotation.py", line 166>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _safe_bid_from_path at 0x0000018C17972D90, file "app/routes/security_api_key_rotation.py", line 166>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_safe_bid_from_path)

180           LOAD_CONST              49 (('rotation_id', 'brokerage_id', 'requested_at', 'actor_type', 'status', 'previous_key_fingerprint', 'new_key_fingerprint', 'effective_at', 'warning_count'))
              STORE_NAME              29 (_OPERATOR_PROJECTION_KEYS)

192           LOAD_CONST              50 (('rotation_id', 'requested_at', 'status', 'effective_at'))
              STORE_NAME              30 (_TENANT_PROJECTION_KEYS)

200           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA2100, file "app/routes/security_api_key_rotation.py", line 200>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _project_operator at 0x0000018C17972550, file "app/routes/security_api_key_rotation.py", line 200>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_project_operator)

206           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA2B50, file "app/routes/security_api_key_rotation.py", line 206>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object _project_tenant at 0x0000018C18010B30, file "app/routes/security_api_key_rotation.py", line 206>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_project_tenant)

212           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C18024B30, file "app/routes/security_api_key_rotation.py", line 212>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object _rate_limit_or_pass at 0x0000018C17F96420, file "app/routes/security_api_key_rotation.py", line 212>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_rate_limit_or_pass)

240           LOAD_NAME               18 (tenant_router)
              LOAD_ATTR               69 (post + NULL|self)
              LOAD_CONST              27 ('/rotation-request')
              CALL                     1

242           LOAD_NAME               10 (Body)
              PUSH_NULL
              LOAD_CONST               8 (Ellipsis)
              CALL                     1

243           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               22 (require_brokerage)
              CALL                     1

241           BUILD_TUPLE              2
              LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3C30, file "app/routes/security_api_key_rotation.py", line 241>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object tenant_rotation_request_route at 0x0000018C17F61B70, file "app/routes/security_api_key_rotation.py", line 240>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

240           CALL                     0

241           STORE_NAME              35 (tenant_rotation_request_route)

296           LOAD_NAME               18 (tenant_router)
              LOAD_ATTR               73 (get + NULL|self)
              LOAD_CONST              30 ('/rotation-status')
              CALL                     1

298           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               22 (require_brokerage)
              CALL                     1

297           BUILD_TUPLE              1
              LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA3E10, file "app/routes/security_api_key_rotation.py", line 297>)
              MAKE_FUNCTION
              LOAD_CONST              32 (<code object tenant_rotation_status_route at 0x0000018C17D8BF50, file "app/routes/security_api_key_rotation.py", line 296>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

296           CALL                     0

297           STORE_NAME              37 (tenant_rotation_status_route)

345           LOAD_NAME               18 (tenant_router)
              LOAD_ATTR               73 (get + NULL|self)
              LOAD_CONST              33 ('/rotation/{rotation_id}/reveal')
              CALL                     1

348           LOAD_CONST              34 ('')

349           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               22 (require_brokerage)
              CALL                     1

346           BUILD_TUPLE              2
              LOAD_CONST              35 (<code object __annotate__ at 0x0000018C18026430, file "app/routes/security_api_key_rotation.py", line 346>)
              MAKE_FUNCTION
              LOAD_CONST              36 (<code object tenant_rotation_reveal_route at 0x0000018C17ED88D0, file "app/routes/security_api_key_rotation.py", line 345>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

345           CALL                     0

346           STORE_NAME              38 (tenant_rotation_reveal_route)

420           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C18025130, file "app/routes/security_api_key_rotation.py", line 420>)
              MAKE_FUNCTION
              LOAD_CONST              38 (<code object _operator_transition at 0x0000018C17E7EBE0, file "app/routes/security_api_key_rotation.py", line 420>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              39 (_operator_transition)

468           LOAD_NAME               19 (operator_router)
              LOAD_ATTR               69 (post + NULL|self)
              LOAD_CONST              39 ('/{rotation_id}/approve')
              CALL                     1

471           LOAD_NAME               10 (Body)
              PUSH_NULL
              LOAD_CONST               8 (Ellipsis)
              CALL                     1

472           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               23 (require_admin)
              CALL                     1

469           BUILD_TUPLE              2
              LOAD_CONST              40 (<code object __annotate__ at 0x0000018C18024930, file "app/routes/security_api_key_rotation.py", line 469>)
              MAKE_FUNCTION
              LOAD_CONST              41 (<code object operator_rotation_approve_route at 0x0000018C180E8030, file "app/routes/security_api_key_rotation.py", line 468>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

468           CALL                     0

469           STORE_NAME              40 (operator_rotation_approve_route)

485           LOAD_NAME               19 (operator_router)
              LOAD_ATTR               69 (post + NULL|self)
              LOAD_CONST              42 ('/{rotation_id}/cancel')
              CALL                     1

488           LOAD_NAME               10 (Body)
              PUSH_NULL
              LOAD_CONST               8 (Ellipsis)
              CALL                     1

489           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               23 (require_admin)
              CALL                     1

486           BUILD_TUPLE              2
              LOAD_CONST              43 (<code object __annotate__ at 0x0000018C18026530, file "app/routes/security_api_key_rotation.py", line 486>)
              MAKE_FUNCTION
              LOAD_CONST              44 (<code object operator_rotation_cancel_route at 0x0000018C180E8140, file "app/routes/security_api_key_rotation.py", line 485>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

485           CALL                     0

486           STORE_NAME              41 (operator_rotation_cancel_route)

502           LOAD_NAME               19 (operator_router)
              LOAD_ATTR               69 (post + NULL|self)
              LOAD_CONST              45 ('/{rotation_id}/fail')
              CALL                     1

505           LOAD_NAME               10 (Body)
              PUSH_NULL
              LOAD_CONST               8 (Ellipsis)
              CALL                     1

506           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               23 (require_admin)
              CALL                     1

503           BUILD_TUPLE              2
              LOAD_CONST              46 (<code object __annotate__ at 0x0000018C18026230, file "app/routes/security_api_key_rotation.py", line 503>)
              MAKE_FUNCTION
              LOAD_CONST              47 (<code object operator_rotation_fail_route at 0x0000018C180E8250, file "app/routes/security_api_key_rotation.py", line 502>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

502           CALL                     0

503           STORE_NAME              42 (operator_rotation_fail_route)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app/routes/security_api_key_rotation.py", line 52>:
 52           RESUME                   0
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

Disassembly of <code object require_brokerage at 0x0000018C17FE1290, file "app/routes/security_api_key_rotation.py", line 52>:
 52           RESUME                   0

 53           LOAD_GLOBAL              1 (get_brokerage_by_api_key + NULL)
              LOAD_FAST_BORROW         0 (x_api_key)
              CALL                     1
              STORE_FAST               1 (brokerage)

 54           LOAD_FAST_BORROW         1 (brokerage)
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

 55   L1:     LOAD_GLOBAL              5 (HTTPException + NULL)
              LOAD_CONST               2 (401)
              LOAD_CONST               3 ('Invalid API key')
              LOAD_CONST               4 (('status_code', 'detail'))
              CALL_KW                  2
              RAISE_VARARGS            1

 56   L2:     LOAD_FAST_BORROW         1 (brokerage)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app/routes/security_api_key_rotation.py", line 59>:
 59           RESUME                   0
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

Disassembly of <code object require_admin at 0x0000018C179A7290, file "app/routes/security_api_key_rotation.py", line 59>:
  59            RESUME                   0

  60            LOAD_GLOBAL              1 (get_settings + NULL)
                CALL                     0
                STORE_FAST               1 (settings)

  61            LOAD_FAST_BORROW         1 (settings)
                LOAD_ATTR                2 (ADMIN_API_KEY)
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (x_admin_key, settings)
                LOAD_ATTR                2 (ADMIN_API_KEY)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       14 (to L2)
                NOT_TAKEN

  62    L1:     LOAD_GLOBAL              5 (HTTPException + NULL)
                LOAD_CONST               0 (401)
                LOAD_CONST               1 ('Invalid admin key')
                LOAD_CONST               2 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

  65    L2:     NOP

  66    L3:     LOAD_SMALL_INT           0
                LOAD_CONST               3 (('check_rate_limit',))
                IMPORT_NAME              3 (app.services.security.rate_limit)
                IMPORT_FROM              4 (check_rate_limit)
                STORE_FAST               2 (check_rate_limit)
                POP_TOP

  67            LOAD_FAST_BORROW         2 (check_rate_limit)
                PUSH_NULL

  68            LOAD_CONST               4 ('admin')

  69            LOAD_CONST               5 ('ADMIN')

  70            LOAD_FAST_BORROW         0 (x_admin_key)

  67            LOAD_CONST               6 (('surface', 'actor_type', 'actor_token'))
                CALL_KW                  3
                STORE_FAST               3 (_rl_verdict)

  72            LOAD_FAST_BORROW         3 (_rl_verdict)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               7 ('allowed')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L6)
        L4:     NOT_TAKEN

  73    L5:     LOAD_GLOBAL              5 (HTTPException + NULL)

  74            LOAD_CONST               8 (429)

  75            LOAD_CONST               9 ('Operator rate limit exceeded. Retry after the current window.')

  73            LOAD_CONST               2 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

  72    L6:     NOP

  81            LOAD_CONST              10 (True)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  77            LOAD_GLOBAL              4 (HTTPException)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                POP_TOP

  78            RAISE_VARARGS            0

  79    L8:     LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L12)
        L9:     NOT_TAKEN
       L10:     POP_TOP

  80   L11:     POP_EXCEPT

  81            LOAD_CONST              10 (True)
                RETURN_VALUE

  79   L12:     RERAISE                  0

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L7 [0]
  L5 to L6 -> L7 [0]
  L7 to L9 -> L13 [1] lasti
  L10 to L11 -> L13 [1] lasti
  L12 to L13 -> L13 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app/routes/security_api_key_rotation.py", line 99>:
 99           RESUME                   0
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

Disassembly of <code object _scan_for_forbidden at 0x0000018C18025A30, file "app/routes/security_api_key_rotation.py", line 99>:
  --           MAKE_CELL                1 (walk)

  99           RESUME                   0

 100           LOAD_CONST               0 (<code object __annotate__ at 0x0000018C17FA2970, file "app/routes/security_api_key_rotation.py", line 100>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object walk at 0x0000018C17D6DFC0, file "app/routes/security_api_key_rotation.py", line 100>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

 138           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app/routes/security_api_key_rotation.py", line 100>:
100           RESUME                   0
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

Disassembly of <code object walk at 0x0000018C17D6DFC0, file "app/routes/security_api_key_rotation.py", line 100>:
  --            COPY_FREE_VARS           1

 100            RESUME                   0

 101            NOP

 102    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      171 (to L18)
        L2:     NOT_TAKEN

 103    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER               148 (to L16)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

 104            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      102 (to L12)
                NOT_TAKEN

 105            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

 106            LOAD_GLOBAL             10 (_FORBIDDEN_RESPONSE_TOKENS)
                GET_ITER
        L5:     FOR_ITER                75 (to L11)
                STORE_FAST               4 (tok)

 107            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)

 115    L7:     LOAD_FAST_BORROW         4 (tok)
                LOAD_CONST               0 ('api_key')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       24 (to L8)
                NOT_TAKEN

 116            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                LOAD_CONST               3 (('previous_key_fingerprint', 'new_key_fingerprint'))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN

 121            JUMP_BACKWARD           41 (to L5)

 122    L8:     LOAD_FAST_BORROW         4 (tok)
                LOAD_CONST               1 ('token')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       24 (to L9)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                LOAD_CONST               4 (('rotation_token',))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN

 125            JUMP_BACKWARD           71 (to L5)

 126    L9:     LOAD_FAST_BORROW         4 (tok)
                SWAP                     2
                POP_TOP
                SWAP                     2
                POP_TOP
       L10:     RETURN_VALUE

 106   L11:     END_FOR
                POP_ITER

 127   L12:     LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 128            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD          146 (to L4)

 129   L14:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L15:     RETURN_VALUE

 103   L16:     END_FOR
                POP_ITER

 137   L17:     LOAD_CONST               2 (None)
                RETURN_VALUE

 130   L18:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             12 (list)
                LOAD_GLOBAL             14 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L24)
                NOT_TAKEN

 131            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L19:     FOR_ITER                23 (to L23)
                STORE_FAST               2 (v)

 132            LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 133            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L20:     POP_JUMP_IF_TRUE         3 (to L21)
                NOT_TAKEN
                JUMP_BACKWARD           21 (to L19)

 134   L21:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L22:     RETURN_VALUE

 131   L23:     END_FOR
                POP_ITER

 137   L24:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L25:     PUSH_EXC_INFO

 135            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L27)
                NOT_TAKEN
                POP_TOP

 136   L26:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 135   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L25 [0]
  L3 to L6 -> L25 [0]
  L7 to L10 -> L25 [0]
  L11 to L13 -> L25 [0]
  L14 to L15 -> L25 [0]
  L16 to L17 -> L25 [0]
  L18 to L20 -> L25 [0]
  L21 to L22 -> L25 [0]
  L23 to L24 -> L25 [0]
  L25 to L26 -> L28 [1] lasti
  L27 to L28 -> L28 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app/routes/security_api_key_rotation.py", line 141>:
141           RESUME                   0
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

Disassembly of <code object _final_envelope at 0x0000018C17FE17D0, file "app/routes/security_api_key_rotation.py", line 141>:
141           RESUME                   0

142           LOAD_GLOBAL              1 (_scan_for_forbidden + NULL)
              LOAD_FAST_BORROW         0 (env)
              CALL                     1
              STORE_FAST               2 (leak)

143           LOAD_FAST_BORROW         2 (leak)
              TO_BOOL
              POP_JUMP_IF_FALSE       37 (to L1)
              NOT_TAKEN

144           LOAD_GLOBAL              2 (logger)
              LOAD_ATTR                5 (warning + NULL|self)

145           LOAD_CONST               0 ('security_api_key_rotation surface=')
              LOAD_FAST_BORROW         1 (surface)
              FORMAT_SIMPLE
              LOAD_CONST               1 (' collapsed — forbidden token leaked')
              BUILD_STRING             3

144           CALL                     1
              POP_TOP

149           LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('failed')

150           LOAD_CONST               4 ('surface')
              LOAD_FAST_BORROW         1 (surface)

151           LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('envelope_forbidden_token')

152           LOAD_CONST               7 ('warnings')
              LOAD_CONST               6 ('envelope_forbidden_token')
              BUILD_LIST               1

148           BUILD_MAP                4
              RETURN_VALUE

154   L1:     LOAD_FAST_BORROW         0 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app/routes/security_api_key_rotation.py", line 157>:
157           RESUME                   0
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

Disassembly of <code object _resolve_brokerage_id at 0x0000018C1796DBD0, file "app/routes/security_api_key_rotation.py", line 157>:
157           RESUME                   0

158           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

159           LOAD_CONST               0 (None)
              RETURN_VALUE

160   L1:     LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('id')
              CALL                     1
              STORE_FAST               1 (bid)

161           LOAD_GLOBAL              1 (isinstance + NULL)
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

162   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

163   L3:     LOAD_FAST_BORROW         1 (bid)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app/routes/security_api_key_rotation.py", line 166>:
166           RESUME                   0
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

Disassembly of <code object _safe_bid_from_path at 0x0000018C17972D90, file "app/routes/security_api_key_rotation.py", line 166>:
166           RESUME                   0

167           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

168           LOAD_CONST               0 (None)
              RETURN_VALUE

169   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

170           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_SMALL_INT         200
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

171   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

172   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app/routes/security_api_key_rotation.py", line 200>:
200           RESUME                   0
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

Disassembly of <code object _project_operator at 0x0000018C17972550, file "app/routes/security_api_key_rotation.py", line 200>:
 200           RESUME                   0

 201           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (row)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

 202           BUILD_MAP                0
               RETURN_VALUE

 203   L1:     LOAD_GLOBAL              4 (_OPERATOR_PROJECTION_KEYS)
               GET_ITER
               LOAD_FAST_AND_CLEAR      1 (k)
               SWAP                     2
       L2:     BUILD_MAP                0
               SWAP                     2
       L3:     FOR_ITER                20 (to L6)
               STORE_FAST_LOAD_FAST    17 (k, k)
               LOAD_FAST_BORROW         0 (row)
               CONTAINS_OP              0 (in)
       L4:     POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)
       L5:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (k, row)
               LOAD_FAST_BORROW         1 (k)
               BINARY_OP               26 ([])
               MAP_ADD                  2
               JUMP_BACKWARD           22 (to L3)
       L6:     END_FOR
               POP_ITER
       L7:     SWAP                     2
               STORE_FAST               1 (k)
               RETURN_VALUE

  --   L8:     SWAP                     2
               POP_TOP

 203           SWAP                     2
               STORE_FAST               1 (k)
               RERAISE                  0
ExceptionTable:
  L2 to L4 -> L8 [2]
  L5 to L7 -> L8 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app/routes/security_api_key_rotation.py", line 206>:
206           RESUME                   0
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

Disassembly of <code object _project_tenant at 0x0000018C18010B30, file "app/routes/security_api_key_rotation.py", line 206>:
 206           RESUME                   0

 207           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (row)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

 208           BUILD_MAP                0
               RETURN_VALUE

 209   L1:     LOAD_GLOBAL              4 (_TENANT_PROJECTION_KEYS)
               GET_ITER
               LOAD_FAST_AND_CLEAR      1 (k)
               SWAP                     2
       L2:     BUILD_MAP                0
               SWAP                     2
       L3:     FOR_ITER                20 (to L6)
               STORE_FAST_LOAD_FAST    17 (k, k)
               LOAD_FAST_BORROW         0 (row)
               CONTAINS_OP              0 (in)
       L4:     POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)
       L5:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (k, row)
               LOAD_FAST_BORROW         1 (k)
               BINARY_OP               26 ([])
               MAP_ADD                  2
               JUMP_BACKWARD           22 (to L3)
       L6:     END_FOR
               POP_ITER
       L7:     SWAP                     2
               STORE_FAST               1 (k)
               RETURN_VALUE

  --   L8:     SWAP                     2
               POP_TOP

 209           SWAP                     2
               STORE_FAST               1 (k)
               RERAISE                  0
ExceptionTable:
  L2 to L4 -> L8 [2]
  L5 to L7 -> L8 [2]

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app/routes/security_api_key_rotation.py", line 212>:
212           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('surface')

214           LOAD_CONST               2 ('str')

212           LOAD_CONST               3 ('brokerage_id')

215           LOAD_CONST               4 ('Optional[str]')

212           LOAD_CONST               5 ('actor_type')

216           LOAD_CONST               2 ('str')

212           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _rate_limit_or_pass at 0x0000018C17F96420, file "app/routes/security_api_key_rotation.py", line 212>:
 212           RESUME                   0

 220           NOP

 221   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('check_rate_limit', 'rate_limit_public_error'))
               IMPORT_NAME              0 (app.services.security.rate_limit)
               IMPORT_FROM              1 (check_rate_limit)
               STORE_FAST               3 (check_rate_limit)
               IMPORT_FROM              2 (rate_limit_public_error)
               STORE_FAST               4 (rate_limit_public_error)
               POP_TOP

 224           LOAD_FAST_BORROW         3 (check_rate_limit)
               PUSH_NULL

 225           LOAD_FAST_BORROW         0 (surface)

 226           LOAD_FAST_BORROW         1 (brokerage_id)

 227           LOAD_FAST_BORROW         2 (actor_type)

 224           LOAD_CONST               2 (('surface', 'brokerage_id', 'actor_type'))
               CALL_KW                  3
               STORE_FAST               5 (verdict)

 229           LOAD_FAST_BORROW         5 (verdict)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               3 ('allowed')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         9 (to L5)
       L2:     NOT_TAKEN

 230   L3:     LOAD_FAST_BORROW         4 (rate_limit_public_error)
               PUSH_NULL
               LOAD_FAST_BORROW         5 (verdict)
               CALL                     1
       L4:     RETURN_VALUE

 229   L5:     NOP

 233           LOAD_CONST               4 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

 231           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

 232   L7:     POP_EXCEPT

 233           LOAD_CONST               4 (None)
               RETURN_VALUE

 231   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L6 [0]
  L3 to L4 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app/routes/security_api_key_rotation.py", line 241>:
241           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')

242           LOAD_CONST               2 ('Dict[str, Any]')

241           LOAD_CONST               3 ('return')

244           LOAD_CONST               2 ('Dict[str, Any]')

241           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object tenant_rotation_request_route at 0x0000018C17F61B70, file "app/routes/security_api_key_rotation.py", line 240>:
 240            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 247            LOAD_GLOBAL              1 (_resolve_brokerage_id + NULL)
                LOAD_FAST_BORROW         1 (brokerage)
                CALL                     1
                STORE_FAST               2 (bid)

 248            LOAD_FAST_BORROW         2 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 249            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               2 (401)
                LOAD_CONST               3 ('Invalid API key')
                LOAD_CONST               4 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 250    L2:     LOAD_GLOBAL              5 (_rate_limit_or_pass + NULL)

 251            LOAD_CONST               5 ('api_key_rotation')

 252            LOAD_FAST_BORROW         2 (bid)

 253            LOAD_CONST               6 ('TENANT')

 250            LOAD_CONST               7 (('surface', 'brokerage_id', 'actor_type'))
                CALL_KW                  3
                STORE_FAST               3 (blocked)

 255            LOAD_FAST_BORROW         3 (blocked)
                POP_JUMP_IF_NONE        20 (to L3)
                NOT_TAKEN

 256            LOAD_GLOBAL              7 (_final_envelope + NULL)

 257            BUILD_MAP                0
                LOAD_FAST_BORROW         3 (blocked)
                DICT_UPDATE              1
                LOAD_CONST               8 ('surface')
                LOAD_CONST               9 ('tenant.api_key.rotation_request')
                BUILD_MAP                1
                DICT_UPDATE              1

 258            LOAD_CONST               9 ('tenant.api_key.rotation_request')

 256            LOAD_CONST              10 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

 260    L3:     LOAD_GLOBAL              9 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (body)
                LOAD_GLOBAL             10 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (body)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              11 ('actor_token')
                CALL                     1
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               1 (None)
        L5:     STORE_FAST               4 (actor_id)

 261            LOAD_GLOBAL              9 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (body)
                LOAD_GLOBAL             10 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L6)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (body)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              12 ('current_api_key')
                CALL                     1
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               1 (None)
        L7:     STORE_FAST               5 (previous_api_key)

 262            LOAD_SMALL_INT           0
                LOAD_CONST              13 (('ALLOWED_ACTOR_TYPES',))
                IMPORT_NAME              7 (app.services.learning.recommendation_review)
                IMPORT_FROM              8 (ALLOWED_ACTOR_TYPES)
                STORE_FAST               6 (_OPERATOR_ACTOR_TYPES)
                POP_TOP

 265            LOAD_SMALL_INT           0
                LOAD_CONST              14 (('request_api_key_rotation',))
                IMPORT_NAME              9 (app.services.security.api_key_rotation)
                IMPORT_FROM             10 (request_api_key_rotation)
                STORE_FAST               7 (request_api_key_rotation)
                POP_TOP

 268    L8:     NOP

 269    L9:     LOAD_FAST_BORROW         7 (request_api_key_rotation)
                PUSH_NULL

 270            LOAD_FAST_BORROW         2 (bid)

 271            LOAD_CONST               6 ('TENANT')

 272            LOAD_FAST_BORROW         4 (actor_id)

 273            LOAD_FAST_BORROW         5 (previous_api_key)

 269            LOAD_CONST              15 (('brokerage_id', 'actor_type', 'actor_id', 'previous_api_key'))
                CALL_KW                  4
                STORE_FAST               8 (result)

 276            LOAD_CONST              16 ('status')
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              16 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
       L10:     NOT_TAKEN
       L11:     POP_TOP
                LOAD_CONST              17 ('failed')

 277   L12:     LOAD_CONST               8 ('surface')
                LOAD_CONST               9 ('tenant.api_key.rotation_request')

 278            LOAD_CONST              18 ('brokerage_id')
                LOAD_FAST                2 (bid)

 279            LOAD_CONST              19 ('payload')
                LOAD_GLOBAL             23 (_project_tenant + NULL)
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              20 ('record')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
       L13:     NOT_TAKEN
       L14:     POP_TOP
                BUILD_MAP                0
       L15:     CALL                     1

 280            LOAD_CONST              21 ('warnings')
                LOAD_GLOBAL             25 (list + NULL)
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              21 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
       L16:     NOT_TAKEN
       L17:     POP_TOP
                BUILD_LIST               0
       L18:     CALL                     1

 281            LOAD_CONST              22 ('error_code')
                LOAD_FAST_BORROW         8 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              22 ('error_code')
                CALL                     1

 275            BUILD_MAP                6
                STORE_FAST               9 (env)

 293   L19:     LOAD_GLOBAL              7 (_final_envelope + NULL)
                LOAD_FAST_BORROW         9 (env)
                LOAD_CONST               9 ('tenant.api_key.rotation_request')
                LOAD_CONST              10 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L20:     PUSH_EXC_INFO

 283            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L24)
                NOT_TAKEN
                STORE_FAST              10 (e)

 284   L21:     LOAD_GLOBAL             28 (logger)
                LOAD_ATTR               31 (warning + NULL|self)

 285            LOAD_CONST              23 ('tenant_rotation_request_route error type=')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 284            CALL                     1
                POP_TOP

 288            LOAD_CONST              16 ('status')
                LOAD_CONST              17 ('failed')

 289            LOAD_CONST               8 ('surface')
                LOAD_CONST               9 ('tenant.api_key.rotation_request')

 290            LOAD_CONST              22 ('error_code')
                LOAD_CONST              24 ('unexpected:')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 291            LOAD_CONST              21 ('warnings')
                BUILD_LIST               0

 287            BUILD_MAP                4
                STORE_FAST               9 (env)
       L22:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L19)

  --   L23:     LOAD_CONST               1 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 283   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L26:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L8 -> L26 [0] lasti
  L9 to L10 -> L20 [0]
  L11 to L13 -> L20 [0]
  L14 to L16 -> L20 [0]
  L17 to L19 -> L20 [0]
  L19 to L20 -> L26 [0] lasti
  L20 to L21 -> L25 [1] lasti
  L21 to L22 -> L23 [1] lasti
  L22 to L23 -> L26 [0] lasti
  L23 to L25 -> L25 [1] lasti
  L25 to L26 -> L26 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "app/routes/security_api_key_rotation.py", line 297>:
297           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')

299           LOAD_CONST               2 ('Dict[str, Any]')

297           BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object tenant_rotation_status_route at 0x0000018C17D8BF50, file "app/routes/security_api_key_rotation.py", line 296>:
 296            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 302            LOAD_GLOBAL              1 (_resolve_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               1 (bid)

 303            LOAD_FAST_BORROW         1 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 304            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               2 (401)
                LOAD_CONST               3 ('Invalid API key')
                LOAD_CONST               4 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 305    L2:     LOAD_GLOBAL              5 (_rate_limit_or_pass + NULL)

 306            LOAD_CONST               5 ('api_key_rotation')

 307            LOAD_FAST_BORROW         1 (bid)

 308            LOAD_CONST               6 ('TENANT')

 305            LOAD_CONST               7 (('surface', 'brokerage_id', 'actor_type'))
                CALL_KW                  3
                STORE_FAST               2 (blocked)

 310            LOAD_FAST_BORROW         2 (blocked)
                POP_JUMP_IF_NONE        20 (to L3)
                NOT_TAKEN

 311            LOAD_GLOBAL              7 (_final_envelope + NULL)

 312            BUILD_MAP                0
                LOAD_FAST_BORROW         2 (blocked)
                DICT_UPDATE              1
                LOAD_CONST               8 ('surface')
                LOAD_CONST               9 ('tenant.api_key.rotation_status')
                BUILD_MAP                1
                DICT_UPDATE              1

 313            LOAD_CONST               9 ('tenant.api_key.rotation_status')

 311            LOAD_CONST              10 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

 315    L3:     LOAD_SMALL_INT           0
                LOAD_CONST              11 (('api_key_rotation_status',))
                IMPORT_NAME              4 (app.services.security.api_key_rotation)
                IMPORT_FROM              5 (api_key_rotation_status)
                STORE_FAST               3 (api_key_rotation_status)
                POP_TOP

 318    L4:     NOP

 319    L5:     LOAD_FAST_BORROW         3 (api_key_rotation_status)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (bid)
                LOAD_CONST              12 (('brokerage_id',))
                CALL_KW                  1
                STORE_FAST               4 (result)

 321            LOAD_CONST              13 ('status')
                LOAD_FAST_BORROW         4 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              13 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                LOAD_CONST              14 ('skipped')

 322    L8:     LOAD_CONST               8 ('surface')
                LOAD_CONST               9 ('tenant.api_key.rotation_status')

 323            LOAD_CONST              15 ('brokerage_id')
                LOAD_FAST                1 (bid)

 324            LOAD_CONST              16 ('payload')
                LOAD_GLOBAL             15 (_project_tenant + NULL)
                LOAD_FAST_BORROW         4 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              17 ('record')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                BUILD_MAP                0
       L11:     CALL                     1

 325            LOAD_CONST              18 ('warnings')
                LOAD_GLOBAL             17 (list + NULL)
                LOAD_FAST_BORROW         4 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              18 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
       L12:     NOT_TAKEN
       L13:     POP_TOP
                BUILD_LIST               0
       L14:     CALL                     1

 326            LOAD_CONST              19 ('error_code')
                LOAD_FAST_BORROW         4 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              19 ('error_code')
                CALL                     1

 320            BUILD_MAP                6
                STORE_FAST               5 (env)

 338   L15:     LOAD_GLOBAL              7 (_final_envelope + NULL)
                LOAD_FAST_BORROW         5 (env)
                LOAD_CONST               9 ('tenant.api_key.rotation_status')
                LOAD_CONST              10 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L16:     PUSH_EXC_INFO

 328            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L20)
                NOT_TAKEN
                STORE_FAST               6 (e)

 329   L17:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 330            LOAD_CONST              20 ('tenant_rotation_status_route error type=')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 329            CALL                     1
                POP_TOP

 333            LOAD_CONST              13 ('status')
                LOAD_CONST              21 ('failed')

 334            LOAD_CONST               8 ('surface')
                LOAD_CONST               9 ('tenant.api_key.rotation_status')

 335            LOAD_CONST              19 ('error_code')
                LOAD_CONST              22 ('unexpected:')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 336            LOAD_CONST              18 ('warnings')
                BUILD_LIST               0

 332            BUILD_MAP                4
                STORE_FAST               5 (env)
       L18:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L15)

  --   L19:     LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 328   L20:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "app/routes/security_api_key_rotation.py", line 346>:
346           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rotation_id')

347           LOAD_CONST               2 ('str')

346           LOAD_CONST               3 ('token')

348           LOAD_CONST               2 ('str')

346           LOAD_CONST               4 ('return')

350           LOAD_CONST               5 ('Dict[str, Any]')

346           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object tenant_rotation_reveal_route at 0x0000018C17ED88D0, file "app/routes/security_api_key_rotation.py", line 345>:
 345            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 359            LOAD_GLOBAL              1 (_resolve_brokerage_id + NULL)
                LOAD_FAST_BORROW         2 (brokerage)
                CALL                     1
                STORE_FAST               3 (bid)

 360            LOAD_FAST_BORROW         3 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 361            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               2 (401)
                LOAD_CONST               3 ('Invalid API key')
                LOAD_CONST               4 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 362    L2:     LOAD_GLOBAL              5 (_rate_limit_or_pass + NULL)

 363            LOAD_CONST               5 ('api_key_rotation')

 364            LOAD_FAST_BORROW         3 (bid)

 365            LOAD_CONST               6 ('TENANT')

 362            LOAD_CONST               7 (('surface', 'brokerage_id', 'actor_type'))
                CALL_KW                  3
                STORE_FAST               4 (blocked)

 367            LOAD_FAST_BORROW         4 (blocked)
                POP_JUMP_IF_NONE        20 (to L3)
                NOT_TAKEN

 368            LOAD_GLOBAL              7 (_final_envelope + NULL)

 369            BUILD_MAP                0
                LOAD_FAST_BORROW         4 (blocked)
                DICT_UPDATE              1
                LOAD_CONST               8 ('surface')
                LOAD_CONST               9 ('tenant.api_key.rotation_reveal')
                BUILD_MAP                1
                DICT_UPDATE              1

 370            LOAD_CONST               9 ('tenant.api_key.rotation_reveal')

 368            LOAD_CONST              10 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

 372    L3:     LOAD_GLOBAL              9 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (token)
                LOAD_GLOBAL             10 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (token)
                LOAD_ATTR               13 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        26 (to L6)
        L4:     NOT_TAKEN

 374    L5:     LOAD_CONST              11 ('status')
                LOAD_CONST              12 ('failed')

 375            LOAD_CONST               8 ('surface')
                LOAD_CONST               9 ('tenant.api_key.rotation_reveal')

 376            LOAD_CONST              13 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)

 377            LOAD_CONST              14 ('error_code')
                LOAD_CONST              15 ('reveal_token_missing')

 378            LOAD_CONST              16 ('warnings')
                BUILD_LIST               0

 373            BUILD_MAP                5
                STORE_FAST               5 (env)

 380            LOAD_GLOBAL              7 (_final_envelope + NULL)
                LOAD_FAST_BORROW         5 (env)
                LOAD_CONST               9 ('tenant.api_key.rotation_reveal')
                LOAD_CONST              10 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

 381    L6:     LOAD_SMALL_INT           0
                LOAD_CONST              17 (('reveal_rotated_api_key_once',))
                IMPORT_NAME              7 (app.services.security.api_key_reveal)
                IMPORT_FROM              8 (reveal_rotated_api_key_once)
                STORE_FAST               6 (reveal_rotated_api_key_once)
                POP_TOP

 384    L7:     NOP

 385    L8:     LOAD_FAST_BORROW         6 (reveal_rotated_api_key_once)
                PUSH_NULL

 386            LOAD_FAST_BORROW         0 (rotation_id)

 387            LOAD_FAST_BORROW         1 (token)

 388            LOAD_FAST_BORROW         3 (bid)

 385            LOAD_CONST              18 (('rotation_id', 'raw_token', 'brokerage_id'))
                CALL_KW                  3
                STORE_FAST               7 (result)

 391            LOAD_CONST              11 ('status')
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              11 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                LOAD_CONST              12 ('failed')

 392   L11:     LOAD_CONST               8 ('surface')
                LOAD_CONST               9 ('tenant.api_key.rotation_reveal')

 393            LOAD_CONST              13 ('brokerage_id')
                LOAD_FAST                3 (bid)

 396            LOAD_CONST              19 ('payload')

 397            LOAD_CONST              20 ('one_time')
                LOAD_GLOBAL             21 (bool + NULL)
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              20 ('one_time')
                CALL                     1
                CALL                     1

 398            LOAD_CONST              21 ('expires_at')
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              21 ('expires_at')
                CALL                     1

 396            BUILD_MAP                2

 400            LOAD_CONST              16 ('warnings')
                LOAD_GLOBAL             23 (list + NULL)
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              16 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
       L12:     NOT_TAKEN
       L13:     POP_TOP
                BUILD_LIST               0
       L14:     CALL                     1

 401            LOAD_CONST              14 ('error_code')
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              14 ('error_code')
                CALL                     1

 390            BUILD_MAP                6
                STORE_FAST               5 (env)

 413   L15:     LOAD_GLOBAL              7 (_final_envelope + NULL)
                LOAD_FAST_BORROW         5 (env)
                LOAD_CONST               9 ('tenant.api_key.rotation_reveal')
                LOAD_CONST              10 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L16:     PUSH_EXC_INFO

 403            LOAD_GLOBAL             24 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L20)
                NOT_TAKEN
                STORE_FAST               8 (e)

 404   L17:     LOAD_GLOBAL             26 (logger)
                LOAD_ATTR               29 (warning + NULL|self)

 405            LOAD_CONST              22 ('tenant_rotation_reveal_route error type=')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 404            CALL                     1
                POP_TOP

 408            LOAD_CONST              11 ('status')
                LOAD_CONST              12 ('failed')

 409            LOAD_CONST               8 ('surface')
                LOAD_CONST               9 ('tenant.api_key.rotation_reveal')

 410            LOAD_CONST              14 ('error_code')
                LOAD_CONST              23 ('unexpected:')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 411            LOAD_CONST              16 ('warnings')
                BUILD_LIST               0

 407            BUILD_MAP                4
                STORE_FAST               5 (env)
       L18:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L15)

  --   L19:     LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 403   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L22:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L4 -> L22 [0] lasti
  L5 to L7 -> L22 [0] lasti
  L8 to L9 -> L16 [0]
  L10 to L12 -> L16 [0]
  L13 to L15 -> L16 [0]
  L15 to L16 -> L22 [0] lasti
  L16 to L17 -> L21 [1] lasti
  L17 to L18 -> L19 [1] lasti
  L18 to L19 -> L22 [0] lasti
  L19 to L21 -> L21 [1] lasti
  L21 to L22 -> L22 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "app/routes/security_api_key_rotation.py", line 420>:
420           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rotation_id')

422           LOAD_CONST               2 ('str')

420           LOAD_CONST               3 ('body')

423           LOAD_CONST               4 ('Dict[str, Any]')

420           LOAD_CONST               5 ('surface')

425           LOAD_CONST               2 ('str')

420           LOAD_CONST               6 ('return')

426           LOAD_CONST               4 ('Dict[str, Any]')

420           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _operator_transition at 0x0000018C17E7EBE0, file "app/routes/security_api_key_rotation.py", line 420>:
 420            RESUME                   0

 427            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (body)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               0 ('actor_type')
                CALL                     1
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST               1 (None)
        L2:     STORE_FAST               4 (actor_type)

 428            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (body)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               2 ('actor_id')
                CALL                     1
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               1 (None)
        L4:     STORE_FAST               5 (actor_id)

 429            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (actor_type)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (actor_type)
                LOAD_ATTR                9 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN

 430    L5:     LOAD_CONST               3 ('OPERATOR')
                STORE_FAST               4 (actor_type)

 431    L6:     LOAD_GLOBAL             11 (_rate_limit_or_pass + NULL)

 432            LOAD_CONST               4 ('api_key_rotation')

 433            LOAD_CONST               1 (None)

 434            LOAD_CONST               3 ('OPERATOR')

 431            LOAD_CONST               5 (('surface', 'brokerage_id', 'actor_type'))
                CALL_KW                  3
                STORE_FAST               6 (blocked)

 436            LOAD_FAST_BORROW         6 (blocked)
                POP_JUMP_IF_NONE        20 (to L7)
                NOT_TAKEN

 437            LOAD_GLOBAL             13 (_final_envelope + NULL)

 438            BUILD_MAP                0
                LOAD_FAST_BORROW         6 (blocked)
                DICT_UPDATE              1
                LOAD_CONST               6 ('surface')
                LOAD_FAST_BORROW         3 (surface)
                BUILD_MAP                1
                DICT_UPDATE              1
                LOAD_FAST_BORROW         3 (surface)

 437            LOAD_CONST               7 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

 440    L7:     NOP

 441    L8:     LOAD_FAST_BORROW         2 (handler)
                PUSH_NULL

 442            LOAD_FAST_BORROW         0 (rotation_id)

 443            LOAD_FAST_BORROW         4 (actor_type)

 444            LOAD_FAST_BORROW         5 (actor_id)

 441            LOAD_CONST               8 (('rotation_id', 'actor_type', 'actor_id'))
                CALL_KW                  3
                STORE_FAST               7 (result)

 447            LOAD_CONST               9 ('status')
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               9 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                LOAD_CONST              10 ('failed')

 448   L11:     LOAD_CONST               6 ('surface')
                LOAD_FAST                3 (surface)

 449            LOAD_CONST              11 ('record')
                LOAD_GLOBAL             15 (_project_operator + NULL)
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              11 ('record')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
       L12:     NOT_TAKEN
       L13:     POP_TOP
                BUILD_MAP                0
       L14:     CALL                     1

 450            LOAD_CONST              12 ('transition')
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              12 ('transition')
                CALL                     1

 451            LOAD_CONST              13 ('audit_row')
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              13 ('audit_row')
                CALL                     1

 452            LOAD_CONST              14 ('warnings')
                LOAD_GLOBAL             17 (list + NULL)
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              14 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L17)
       L15:     NOT_TAKEN
       L16:     POP_TOP
                BUILD_LIST               0
       L17:     CALL                     1

 453            LOAD_CONST              15 ('error_code')
                LOAD_FAST_BORROW         7 (result)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              15 ('error_code')
                CALL                     1

 446            BUILD_MAP                7
                STORE_FAST               8 (env)

 465   L18:     LOAD_GLOBAL             13 (_final_envelope + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 131 (env, surface)
                LOAD_CONST               7 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L19:     PUSH_EXC_INFO

 455            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       89 (to L23)
                NOT_TAKEN
                STORE_FAST               9 (e)

 456   L20:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 457            LOAD_CONST              16 ('_operator_transition ')
                LOAD_FAST                3 (surface)
                FORMAT_SIMPLE
                LOAD_CONST              17 (' error type=')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             4

 456            CALL                     1
                POP_TOP

 460            LOAD_CONST               9 ('status')
                LOAD_CONST              10 ('failed')

 461            LOAD_CONST               6 ('surface')
                LOAD_FAST                3 (surface)

 462            LOAD_CONST              15 ('error_code')
                LOAD_CONST              18 ('unexpected:')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 463            LOAD_CONST              14 ('warnings')
                BUILD_LIST               0

 459            BUILD_MAP                4
                STORE_FAST               8 (env)
       L21:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                JUMP_BACKWARD_NO_INTERRUPT 106 (to L18)

  --   L22:     LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 455   L23:     RERAISE                  0

  --   L24:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L8 to L9 -> L19 [0]
  L10 to L12 -> L19 [0]
  L13 to L15 -> L19 [0]
  L16 to L18 -> L19 [0]
  L19 to L20 -> L24 [1] lasti
  L20 to L21 -> L22 [1] lasti
  L22 to L24 -> L24 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app/routes/security_api_key_rotation.py", line 469>:
469           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rotation_id')

470           LOAD_CONST               2 ('str')

469           LOAD_CONST               3 ('body')

471           LOAD_CONST               4 ('Dict[str, Any]')

469           LOAD_CONST               5 ('return')

473           LOAD_CONST               4 ('Dict[str, Any]')

469           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object operator_rotation_approve_route at 0x0000018C180E8030, file "app/routes/security_api_key_rotation.py", line 468>:
 468           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 474           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('approve_api_key_rotation',))
               IMPORT_NAME              0 (app.services.security.api_key_rotation)
               IMPORT_FROM              1 (approve_api_key_rotation)
               STORE_FAST               3 (approve_api_key_rotation)
               POP_TOP

 477           LOAD_GLOBAL              5 (_operator_transition + NULL)

 478           LOAD_FAST_BORROW         0 (rotation_id)

 479           LOAD_FAST_BORROW         1 (body)

 480           LOAD_FAST_BORROW         3 (approve_api_key_rotation)

 481           LOAD_CONST               2 ('ops.api_key.rotation_approve')

 477           LOAD_CONST               3 (('rotation_id', 'body', 'handler', 'surface'))
               CALL_KW                  4
               RETURN_VALUE

  --   L2:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L2 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026530, file "app/routes/security_api_key_rotation.py", line 486>:
486           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rotation_id')

487           LOAD_CONST               2 ('str')

486           LOAD_CONST               3 ('body')

488           LOAD_CONST               4 ('Dict[str, Any]')

486           LOAD_CONST               5 ('return')

490           LOAD_CONST               4 ('Dict[str, Any]')

486           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object operator_rotation_cancel_route at 0x0000018C180E8140, file "app/routes/security_api_key_rotation.py", line 485>:
 485           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 491           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('cancel_api_key_rotation',))
               IMPORT_NAME              0 (app.services.security.api_key_rotation)
               IMPORT_FROM              1 (cancel_api_key_rotation)
               STORE_FAST               3 (cancel_api_key_rotation)
               POP_TOP

 494           LOAD_GLOBAL              5 (_operator_transition + NULL)

 495           LOAD_FAST_BORROW         0 (rotation_id)

 496           LOAD_FAST_BORROW         1 (body)

 497           LOAD_FAST_BORROW         3 (cancel_api_key_rotation)

 498           LOAD_CONST               2 ('ops.api_key.rotation_cancel')

 494           LOAD_CONST               3 (('rotation_id', 'body', 'handler', 'surface'))
               CALL_KW                  4
               RETURN_VALUE

  --   L2:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L2 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026230, file "app/routes/security_api_key_rotation.py", line 503>:
503           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rotation_id')

504           LOAD_CONST               2 ('str')

503           LOAD_CONST               3 ('body')

505           LOAD_CONST               4 ('Dict[str, Any]')

503           LOAD_CONST               5 ('return')

507           LOAD_CONST               4 ('Dict[str, Any]')

503           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object operator_rotation_fail_route at 0x0000018C180E8250, file "app/routes/security_api_key_rotation.py", line 502>:
 502           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 508           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('fail_api_key_rotation',))
               IMPORT_NAME              0 (app.services.security.api_key_rotation)
               IMPORT_FROM              1 (fail_api_key_rotation)
               STORE_FAST               3 (fail_api_key_rotation)
               POP_TOP

 511           LOAD_GLOBAL              5 (_operator_transition + NULL)

 512           LOAD_FAST_BORROW         0 (rotation_id)

 513           LOAD_FAST_BORROW         1 (body)

 514           LOAD_FAST_BORROW         3 (fail_api_key_rotation)

 515           LOAD_CONST               2 ('ops.api_key.rotation_fail')

 511           LOAD_CONST               3 (('rotation_id', 'body', 'handler', 'surface'))
               CALL_KW                  4
               RETURN_VALUE

  --   L2:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L2 [0] lasti
```
