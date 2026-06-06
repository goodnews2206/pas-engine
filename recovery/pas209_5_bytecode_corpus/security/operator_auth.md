# security/operator_auth

- **pyc:** `app\services\security\__pycache__\operator_auth.cpython-314.pyc`
- **expected source path (absent):** `app\services\security/operator_auth.py`
- **co_filename (from bytecode):** `app/services/security/operator_auth.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** security

## Module docstring

```
PAS-SECURITY-04 — Consolidated operator/admin auth + rate-limit
helper.

Single reusable dependency for `/ops/*` routes (and any other
admin-key-gated surface). Replaces the per-file ad-hoc
``require_admin`` definitions with a closed helper that:

  1. Verifies the ``X-Admin-Key`` against
     ``settings.ADMIN_API_KEY``.
  2. Calls PAS-SECURITY-02's ``check_rate_limit(surface="admin", actor_type="ADMIN",
     actor_token=x_admin_key)`` and raises 429 on block.
  3. Returns a closed ``operator_actor_context`` dict for the
     caller — bounded actor tokens only; NEVER carries the raw
     admin key.

Doctrine:

* **Closed actor context.** ``operator_actor_context`` carries
  only ``actor_type``, ``actor_fingerprint`` (sha256 hex of
  the admin key), bounded ``actor_id`` if supplied by the
  caller. NEVER the raw key.
* **Failure isolation.** A limiter outage MUST NOT lock the
  operator out. Any exception other than the deliberate 401 /
  429 is swallowed.
* **NEVER raises** — except the deliberate 401 (invalid key)
  and 429 (rate limit). All other paths return structural
  envelopes.
* **No body brokerage_id trust.** The helper does NOT read
  brokerage_id from the request body / URL.

Public surface:

  * ``ALLOWED_ACTOR_TYPES``                  — closed enum.
  * ``OPERATOR_AUTH_SURFACE``                — closed surface token.
  * ``require_operator_or_admin(x_admin_key)`` — FastAPI Depends helper.
  * ``operator_actor_context(x_admin_key, actor_id_override=None)``
                                              — pure helper.
  * ``operator_rate_limit_context(actor_token)``
                                              — diagnostic envelope.
```

## Imports

`Any`, `Dict`, `HTTPException`, `Header`, `Optional`, `Tuple`, `__future__`, `annotations`, `app.config`, `app.services.security.rate_limit`, `check_rate_limit`, `fastapi`, `get_settings`, `hashlib`, `logging`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_safe_fingerprint`, `operator_actor_context`, `operator_rate_limit_context`, `require_operator_or_admin`

## Env-key candidates

`ADMIN`, `ALLOWED_ACTOR_TYPES`, `OPERATOR_AUTH_SURFACE`

## String constants (redacted where noted)

- 🔒 '<REDACTED:secret-bearing literal>'
- 'pas.security.operator_auth'
- 'Tuple[str, ...]'
- 'ALLOWED_ACTOR_TYPES'
- 'admin'
- 'str'
- 'OPERATOR_AUTH_SURFACE'
- 'actor_id_override'
- 'value'
- 'Any'
- 'return'
- 'Optional[str]'
- 'sha256 hex of a bounded string. NEVER returns the\noriginal value. NEVER raises.'
- 'utf-8'
- 'x_admin_key'
- 'Dict[str, Any]'
- 'Return a closed actor context. NEVER raises. NEVER\ncarries the raw admin key.\n\n``actor_id_override`` lets the caller pin a bounded\noperator handle (e.g. from a per-operator deployment env\nvar). Defaults to "operator" — a closed token, never the\nraw key.\n'
- 'actor_type'
- 'ADMIN'
- 'actor_fingerprint'
- 'actor_id'
- 'operator'
- 'surface'
- 'actor_token'
- 'Diagnostic envelope describing what the rate limiter\nwould key on. NEVER raises. NEVER returns the raw token.'
- 'Consolidated operator/admin dependency. Verifies the\nX-Admin-Key, applies the rate-limit, and returns a closed\nactor context.\n\nRaises:\n    HTTPException(401) — invalid admin key.\n    HTTPException(429) — rate limit exceeded.\n\nReturns:\n    The closed actor context (see ``operator_actor_context``).\n'
- 'require_operator_or_admin settings unavailable type='
- 'Invalid admin key'
- 'allowed'
- 'Operator rate limit exceeded. Retry after the current window.'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS-SECURITY-04 — Consolidated operator/admin auth + rate-limit\nhelper.\n\nSingle reusable dependency for `/ops/*` routes (and any other\nadmin-key-gated surface). Replaces the per-file ad-hoc\n``require_admin`` definitions with a closed helper that:\n\n  1. Verifies the ``X-Admin-Key`` against\n     ``settings.ADMIN_API_KEY``.\n  2. Calls PAS-SECURITY-02\'s ``check_rate_limit(surface="admin", actor_type="ADMIN",\n     actor_token=x_admin_key)`` and raises 429 on block.\n  3. Returns a closed ``operator_actor_context`` dict for the\n     caller — bounded actor tokens only; NEVER carries the raw\n     admin key.\n\nDoctrine:\n\n* **Closed actor context.** ``operator_actor_context`` carries\n  only ``actor_type``, ``actor_fingerprint`` (sha256 hex of\n  the admin key), bounded ``actor_id`` if supplied by the\n  caller. NEVER the raw key.\n* **Failure isolation.** A limiter outage MUST NOT lock the\n  operator out. Any exception other than the deliberate 401 /\n  429 is swallowed.\n* **NEVER raises** — except the deliberate 401 (invalid key)\n  and 429 (rate limit). All other paths return structural\n  envelopes.\n* **No body brokerage_id trust.** The helper does NOT read\n  brokerage_id from the request body / URL.\n\nPublic surface:\n\n  * ``ALLOWED_ACTOR_TYPES``                  — closed enum.\n  * ``OPERATOR_AUTH_SURFACE``                — closed surface token.\n  * ``require_operator_or_admin(x_admin_key)`` — FastAPI Depends helper.\n  * ``operator_actor_context(x_admin_key, actor_id_override=None)``\n                                              — pure helper.\n  * ``operator_rate_limit_context(actor_token)``\n                                              — diagnostic envelope.\n')
               STORE_NAME               1 (__doc__)

  43           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  45           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (hashlib)
               STORE_NAME               4 (hashlib)

  46           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (logging)
               STORE_NAME               5 (logging)

  47           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('Any', 'Dict', 'Optional', 'Tuple'))
               IMPORT_NAME              6 (typing)
               IMPORT_FROM              7 (Any)
               STORE_NAME               7 (Any)
               IMPORT_FROM              8 (Dict)
               STORE_NAME               8 (Dict)
               IMPORT_FROM              9 (Optional)
               STORE_NAME               9 (Optional)
               IMPORT_FROM             10 (Tuple)
               STORE_NAME              10 (Tuple)
               POP_TOP

  49           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Header', 'HTTPException'))
               IMPORT_NAME             11 (fastapi)
               IMPORT_FROM             12 (Header)
               STORE_NAME              12 (Header)
               IMPORT_FROM             13 (HTTPException)
               STORE_NAME              13 (HTTPException)
               POP_TOP

  52           LOAD_NAME                5 (logging)
               LOAD_ATTR               28 (getLogger)
               PUSH_NULL
               LOAD_CONST               5 ('pas.security.operator_auth')
               CALL                     1
               STORE_NAME              15 (logger)

  56           LOAD_CONST              21 (('OPERATOR', 'ADMIN'))
               STORE_NAME              16 (ALLOWED_ACTOR_TYPES)
               LOAD_CONST               6 ('Tuple[str, ...]')
               LOAD_NAME               17 (__annotations__)
               LOAD_CONST               7 ('ALLOWED_ACTOR_TYPES')
               STORE_SUBSCR

  60           LOAD_CONST               8 ('admin')
               STORE_NAME              18 (OPERATOR_AUTH_SURFACE)
               LOAD_CONST               9 ('str')
               LOAD_NAME               17 (__annotations__)
               LOAD_CONST              10 ('OPERATOR_AUTH_SURFACE')
               STORE_SUBSCR

  63           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA33C0, file "app/services/security/operator_auth.py", line 63>)
               MAKE_FUNCTION
               LOAD_CONST              12 (<code object _safe_fingerprint at 0x0000018C179A7290, file "app/services/security/operator_auth.py", line 63>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              19 (_safe_fingerprint)

  77           LOAD_CONST              13 ('actor_id_override')

  80           LOAD_CONST               2 (None)

  77           BUILD_MAP                1
               LOAD_CONST              14 (<code object __annotate__ at 0x0000018C18024E30, file "app/services/security/operator_auth.py", line 77>)
               MAKE_FUNCTION
               LOAD_CONST              15 (<code object operator_actor_context at 0x0000018C17F95E60, file "app/services/security/operator_auth.py", line 77>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              20 (operator_actor_context)

 103           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA2E20, file "app/services/security/operator_auth.py", line 103>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object operator_rate_limit_context at 0x0000018C18025A30, file "app/services/security/operator_auth.py", line 103>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              21 (operator_rate_limit_context)

 116           LOAD_NAME               12 (Header)
               PUSH_NULL
               LOAD_CONST              18 (Ellipsis)
               CALL                     1
               BUILD_TUPLE              1
               LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA3F00, file "app/services/security/operator_auth.py", line 116>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object require_operator_or_admin at 0x0000018C17E7EC70, file "app/services/security/operator_auth.py", line 116>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              22 (require_operator_or_admin)

 164           BUILD_LIST               0
               LOAD_CONST              22 (('ALLOWED_ACTOR_TYPES', 'OPERATOR_AUTH_SURFACE', 'require_operator_or_admin', 'operator_actor_context', 'operator_rate_limit_context'))
               LIST_EXTEND              1
               STORE_NAME              23 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app/services/security/operator_auth.py", line 63>:
 63           RESUME                   0
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

Disassembly of <code object _safe_fingerprint at 0x0000018C179A7290, file "app/services/security/operator_auth.py", line 63>:
  63           RESUME                   0

  66           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (value)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

  67           LOAD_CONST               1 (None)
               RETURN_VALUE

  68   L1:     LOAD_FAST_BORROW         0 (value)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               STORE_FAST               1 (s)

  69           LOAD_FAST_BORROW         1 (s)
               TO_BOOL
               POP_JUMP_IF_FALSE       17 (to L2)
               NOT_TAKEN
               LOAD_GLOBAL              7 (len + NULL)
               LOAD_FAST_BORROW         1 (s)
               CALL                     1
               LOAD_CONST               2 (1024)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

  70   L2:     LOAD_CONST               1 (None)
               RETURN_VALUE

  71   L3:     NOP

  72   L4:     LOAD_GLOBAL              8 (hashlib)
               LOAD_ATTR               10 (sha256)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR               13 (encode + NULL|self)
               LOAD_CONST               3 ('utf-8')
               CALL                     1
               CALL                     1
               LOAD_ATTR               15 (hexdigest + NULL|self)
               CALL                     0
       L5:     RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  73           LOAD_GLOBAL             16 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

  74   L7:     POP_EXCEPT
               LOAD_CONST               1 (None)
               RETURN_VALUE

  73   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L4 to L5 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app/services/security/operator_auth.py", line 77>:
 77           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('x_admin_key')

 78           LOAD_CONST               2 ('Any')

 77           LOAD_CONST               3 ('actor_id_override')

 80           LOAD_CONST               4 ('Optional[str]')

 77           LOAD_CONST               5 ('return')

 81           LOAD_CONST               6 ('Dict[str, Any]')

 77           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object operator_actor_context at 0x0000018C17F95E60, file "app/services/security/operator_auth.py", line 77>:
 77           RESUME                   0

 90           LOAD_GLOBAL              1 (_safe_fingerprint + NULL)
              LOAD_FAST_BORROW         0 (x_admin_key)
              CALL                     1
              STORE_FAST               2 (fp)

 92           LOAD_CONST               1 ('actor_type')
              LOAD_CONST               2 ('ADMIN')

 93           LOAD_CONST               3 ('actor_fingerprint')
              LOAD_FAST                2 (fp)

 94           LOAD_CONST               4 ('actor_id')

 96           LOAD_GLOBAL              3 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (actor_id_override)
              LOAD_GLOBAL              4 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       32 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (actor_id_override)
              LOAD_ATTR                7 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       10 (to L1)
              NOT_TAKEN

 95           LOAD_FAST_BORROW         1 (actor_id_override)

 99           LOAD_CONST               6 ('surface')
              LOAD_GLOBAL              8 (OPERATOR_AUTH_SURFACE)

 91           BUILD_MAP                4
              RETURN_VALUE

 97   L1:     LOAD_CONST               5 ('operator')

 99           LOAD_CONST               6 ('surface')
              LOAD_GLOBAL              8 (OPERATOR_AUTH_SURFACE)

 91           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app/services/security/operator_auth.py", line 103>:
103           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('actor_token')

104           LOAD_CONST               2 ('Any')

103           LOAD_CONST               3 ('return')

105           LOAD_CONST               4 ('Dict[str, Any]')

103           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object operator_rate_limit_context at 0x0000018C18025A30, file "app/services/security/operator_auth.py", line 103>:
103           RESUME                   0

108           LOAD_GLOBAL              1 (_safe_fingerprint + NULL)
              LOAD_FAST_BORROW         0 (actor_token)
              CALL                     1
              STORE_FAST               1 (fp)

110           LOAD_CONST               1 ('surface')
              LOAD_GLOBAL              2 (OPERATOR_AUTH_SURFACE)

111           LOAD_CONST               2 ('actor_type')
              LOAD_CONST               3 ('ADMIN')

112           LOAD_CONST               4 ('actor_fingerprint')
              LOAD_FAST_BORROW         1 (fp)

109           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "app/services/security/operator_auth.py", line 116>:
116           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object require_operator_or_admin at 0x0000018C17E7EC70, file "app/services/security/operator_auth.py", line 116>:
 116            RESUME                   0

 129            NOP

 130    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('get_settings',))
                IMPORT_NAME              0 (app.config)
                IMPORT_FROM              1 (get_settings)
                STORE_FAST               1 (get_settings)
                POP_TOP

 131            LOAD_FAST_BORROW         1 (get_settings)
                PUSH_NULL
                CALL                     0
                STORE_FAST               2 (settings)

 138    L2:     LOAD_FAST                2 (settings)
                LOAD_ATTR               16 (ADMIN_API_KEY)
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L3)
                NOT_TAKEN
                LOAD_FAST_LOAD_FAST      2 (x_admin_key, settings)
                LOAD_ATTR               16 (ADMIN_API_KEY)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       14 (to L4)
                NOT_TAKEN

 139    L3:     LOAD_GLOBAL             15 (HTTPException + NULL)
                LOAD_CONST               3 (401)
                LOAD_CONST               4 ('Invalid admin key')
                LOAD_CONST               5 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 142    L4:     NOP

 143    L5:     LOAD_SMALL_INT           0
                LOAD_CONST               7 (('check_rate_limit',))
                IMPORT_NAME              9 (app.services.security.rate_limit)
                IMPORT_FROM             10 (check_rate_limit)
                STORE_FAST               4 (check_rate_limit)
                POP_TOP

 144            LOAD_FAST                4 (check_rate_limit)
                PUSH_NULL

 145            LOAD_GLOBAL             22 (OPERATOR_AUTH_SURFACE)

 146            LOAD_CONST               8 ('ADMIN')

 147            LOAD_FAST                0 (x_admin_key)

 144            LOAD_CONST               9 (('surface', 'actor_type', 'actor_token'))
                CALL_KW                  3
                STORE_FAST               5 (verdict)

 149            LOAD_FAST                5 (verdict)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              10 ('allowed')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L8)
        L6:     NOT_TAKEN

 150    L7:     LOAD_GLOBAL             15 (HTTPException + NULL)

 151            LOAD_CONST              11 (429)

 152            LOAD_CONST              12 ('Operator rate limit exceeded. Retry after the current window.')

 150            LOAD_CONST               5 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 149    L8:     NOP

 161    L9:     LOAD_GLOBAL             27 (operator_actor_context + NULL)
                LOAD_FAST                0 (x_admin_key)
                CALL                     1
                RETURN_VALUE

  --   L10:     PUSH_EXC_INFO

 132            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       62 (to L13)
                NOT_TAKEN
                STORE_FAST               3 (e)

 133   L11:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 134            LOAD_CONST               2 ('require_operator_or_admin settings unavailable type=')

 135            LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE

 134            BUILD_STRING             2

 133            CALL                     1
                POP_TOP

 137            LOAD_GLOBAL             15 (HTTPException + NULL)
                LOAD_CONST               3 (401)
                LOAD_CONST               4 ('Invalid admin key')
                LOAD_CONST               5 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

  --   L12:     LOAD_CONST               6 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 132   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L15:     PUSH_EXC_INFO

 154            LOAD_GLOBAL             14 (HTTPException)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        3 (to L16)
                NOT_TAKEN
                POP_TOP

 155            RAISE_VARARGS            0

 156   L16:     LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        4 (to L20)
       L17:     NOT_TAKEN
       L18:     POP_TOP

 158   L19:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 110 (to L9)

 156   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L10 [0]
  L5 to L6 -> L15 [0]
  L7 to L8 -> L15 [0]
  L10 to L11 -> L14 [1] lasti
  L11 to L12 -> L12 [1] lasti
  L12 to L14 -> L14 [1] lasti
  L15 to L17 -> L21 [1] lasti
  L18 to L19 -> L21 [1] lasti
  L20 to L21 -> L21 [1] lasti
```
