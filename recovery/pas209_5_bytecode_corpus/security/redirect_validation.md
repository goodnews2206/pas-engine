# security/redirect_validation

- **pyc:** `app\services\security\__pycache__\redirect_validation.cpython-314.pyc`
- **expected source path (absent):** `app\services\security/redirect_validation.py`
- **co_filename (from bytecode):** `app/services/security/redirect_validation.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** security

## Module docstring

```
PAS-SECURITY-01 — Redirect-target allow-list guard (additive).

Defensive helper for any future route that needs to accept a
caller-supplied ``redirect_url`` / ``next`` / ``return_to`` /
``callback_url`` / ``destination`` parameter.

Doctrine:

* **Allow-list only.** Targets are validated against a closed
  list of permitted hosts. Anything else is refused.
* **No arbitrary external redirect.** A bare or unknown host
  fails closed with ``error_code="redirect_target_not_allowed"``.
* **No protocol-relative or scheme-shifted redirects.** Only
  `http` / `https` accepted; relative-only same-origin
  targets are also permitted when ``allow_relative=True``.
* **No userinfo / no port-shift attacks.** ``user@host`` and
  ``host:port`` are normalised; only the bare host (lowercased)
  is matched against the allow-list.
* **NEVER raises.**
* **No live PAS state touched.** This module classifies; it
  does NOT call any route.

PAS posture at the time of audit: PAS160-PAS181 routes do not
accept user-supplied redirect parameters. This module is
*defence-in-depth*: any future feature that adds a redirect
target MUST call ``validate_redirect_target(...)`` before
issuing a 302.

Public surface:

  * ``ALLOWED_REDIRECT_SCHEMES``                — closed enum.
  * ``FORBIDDEN_REDIRECT_TOKENS``               — substring blocklist.
  * ``normalise_redirect_host(url)``            — bare host or None.
  * ``validate_redirect_target(url, allowed_hosts, allow_relative)``
                                               — verdict envelope.
```

## Imports

`Any`, `Dict`, `Iterable`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `logging`, `typing`, `urllib.parse`, `urlparse`

## Classes

_none_

## Functions / methods

`__annotate__`, `_safe_verdict`, `normalise_redirect_host`, `validate_redirect_target`

## Env-key candidates

`ALLOWED_REDIRECT_SCHEMES`, `FORBIDDEN_REDIRECT_TOKENS`

## String constants (redacted where noted)

- '\nPAS-SECURITY-01 — Redirect-target allow-list guard (additive).\n\nDefensive helper for any future route that needs to accept a\ncaller-supplied ``redirect_url`` / ``next`` / ``return_to`` /\n``callback_url`` / ``destination`` parameter.\n\nDoctrine:\n\n* **Allow-list only.** Targets are validated against a closed\n  list of permitted hosts. Anything else is refused.\n* **No arbitrary external redirect.** A bare or unknown host\n  fails closed with ``error_code="redirect_target_not_allowed"``.\n* **No protocol-relative or scheme-shifted redirects.** Only\n  `http` / `https` accepted; relative-only same-origin\n  targets are also permitted when ``allow_relative=True``.\n* **No userinfo / no port-shift attacks.** ``user@host`` and\n  ``host:port`` are normalised; only the bare host (lowercased)\n  is matched against the allow-list.\n* **NEVER raises.**\n* **No live PAS state touched.** This module classifies; it\n  does NOT call any route.\n\nPAS posture at the time of audit: PAS160-PAS181 routes do not\naccept user-supplied redirect parameters. This module is\n*defence-in-depth*: any future feature that adds a redirect\ntarget MUST call ``validate_redirect_target(...)`` before\nissuing a 302.\n\nPublic surface:\n\n  * ``ALLOWED_REDIRECT_SCHEMES``                — closed enum.\n  * ``FORBIDDEN_REDIRECT_TOKENS``               — substring blocklist.\n  * ``normalise_redirect_host(url)``            — bare host or None.\n  * ``validate_redirect_target(url, allowed_hosts, allow_relative)``\n                                               — verdict envelope.\n'
- 'pas.security.redirect_validation'
- 'Tuple[str, ...]'
- 'ALLOWED_REDIRECT_SCHEMES'
- 'FORBIDDEN_REDIRECT_TOKENS'
- 'target'
- 'error_code'
- 'warnings'
- 'allow_relative'
- 'valid'
- 'bool'
- 'Optional[str]'
- 'Optional[List[str]]'
- 'return'
- 'Dict[str, Any]'
- 'url'
- 'Any'
- 'Return the bare lowercased host from ``url``. NEVER raises.\nReturns None for malformed / unsafe input.'
- 'allowed_hosts'
- 'Iterable[str]'
- 'Validate ``url`` against the closed ``allowed_hosts``\nlist. NEVER raises.\n\nOutcomes:\n  * ``valid=True`` — target is a same-origin relative path\n    (only when ``allow_relative=True``) OR an absolute URL\n    with scheme ∈ ALLOWED_REDIRECT_SCHEMES and host on the\n    allow-list.\n  * ``valid=False`` — anything else, with a structural\n    ``error_code``.\n'
- 'missing_redirect_target'
- 'redirect_target_too_long'
- 'forbidden_redirect_token'
- 'forbidden_token:'
- 'invalid_redirect_url'
- 'invalid_redirect_scheme'
- 'scheme:'
- 'missing_redirect_host'
- 'redirect_target_not_allowed'
- '://'
- 'validate_redirect_target error type='
- 'unexpected:'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS-SECURITY-01 — Redirect-target allow-list guard (additive).\n\nDefensive helper for any future route that needs to accept a\ncaller-supplied ``redirect_url`` / ``next`` / ``return_to`` /\n``callback_url`` / ``destination`` parameter.\n\nDoctrine:\n\n* **Allow-list only.** Targets are validated against a closed\n  list of permitted hosts. Anything else is refused.\n* **No arbitrary external redirect.** A bare or unknown host\n  fails closed with ``error_code="redirect_target_not_allowed"``.\n* **No protocol-relative or scheme-shifted redirects.** Only\n  `http` / `https` accepted; relative-only same-origin\n  targets are also permitted when ``allow_relative=True``.\n* **No userinfo / no port-shift attacks.** ``user@host`` and\n  ``host:port`` are normalised; only the bare host (lowercased)\n  is matched against the allow-list.\n* **NEVER raises.**\n* **No live PAS state touched.** This module classifies; it\n  does NOT call any route.\n\nPAS posture at the time of audit: PAS160-PAS181 routes do not\naccept user-supplied redirect parameters. This module is\n*defence-in-depth*: any future feature that adds a redirect\ntarget MUST call ``validate_redirect_target(...)`` before\nissuing a 302.\n\nPublic surface:\n\n  * ``ALLOWED_REDIRECT_SCHEMES``                — closed enum.\n  * ``FORBIDDEN_REDIRECT_TOKENS``               — substring blocklist.\n  * ``normalise_redirect_host(url)``            — bare host or None.\n  * ``validate_redirect_target(url, allowed_hosts, allow_relative)``\n                                               — verdict envelope.\n')
               STORE_NAME               1 (__doc__)

  39           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  41           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  42           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('Any', 'Dict', 'Iterable', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME              5 (typing)
               IMPORT_FROM              6 (Any)
               STORE_NAME               6 (Any)
               IMPORT_FROM              7 (Dict)
               STORE_NAME               7 (Dict)
               IMPORT_FROM              8 (Iterable)
               STORE_NAME               8 (Iterable)
               IMPORT_FROM              9 (List)
               STORE_NAME               9 (List)
               IMPORT_FROM             10 (Optional)
               STORE_NAME              10 (Optional)
               IMPORT_FROM             11 (Tuple)
               STORE_NAME              11 (Tuple)
               POP_TOP

  43           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('urlparse',))
               IMPORT_NAME             12 (urllib.parse)
               IMPORT_FROM             13 (urlparse)
               STORE_NAME              13 (urlparse)
               POP_TOP

  46           LOAD_NAME                4 (logging)
               LOAD_ATTR               28 (getLogger)
               PUSH_NULL
               LOAD_CONST               5 ('pas.security.redirect_validation')
               CALL                     1
               STORE_NAME              15 (logger)

  51           LOAD_CONST              21 (('http', 'https'))
               STORE_NAME              16 (ALLOWED_REDIRECT_SCHEMES)
               LOAD_CONST               6 ('Tuple[str, ...]')
               LOAD_NAME               17 (__annotations__)
               LOAD_CONST               7 ('ALLOWED_REDIRECT_SCHEMES')
               STORE_SUBSCR

  57           LOAD_CONST              22 (('javascript:', 'data:', 'vbscript:', 'file:', 'gopher:', 'ftp:', '\\\\', '@', '\r', '\n', '\x00'))
               STORE_NAME              18 (FORBIDDEN_REDIRECT_TOKENS)
               LOAD_CONST               6 ('Tuple[str, ...]')
               LOAD_NAME               17 (__annotations__)
               LOAD_CONST               8 ('FORBIDDEN_REDIRECT_TOKENS')
               STORE_SUBSCR

  72           LOAD_CONST               9 (2048)
               STORE_NAME              19 (_URL_MAX_LEN)

  75           LOAD_CONST              10 ('target')

  78           LOAD_CONST               2 (None)

  75           LOAD_CONST              11 ('error_code')

  79           LOAD_CONST               2 (None)

  75           LOAD_CONST              12 ('warnings')

  80           LOAD_CONST               2 (None)

  75           BUILD_MAP                3
               LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18025F30, file "app/services/security/redirect_validation.py", line 75>)
               MAKE_FUNCTION
               LOAD_CONST              14 (<code object _safe_verdict at 0x0000018C18053870, file "app/services/security/redirect_validation.py", line 75>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              20 (_safe_verdict)

  90           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA33C0, file "app/services/security/redirect_validation.py", line 90>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object normalise_redirect_host at 0x0000018C17D8E300, file "app/services/security/redirect_validation.py", line 90>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              21 (normalise_redirect_host)

 112           LOAD_CONST              17 ('allow_relative')

 116           LOAD_CONST              18 (False)

 112           BUILD_MAP                1
               LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18025730, file "app/services/security/redirect_validation.py", line 112>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object validate_redirect_target at 0x0000018C17ED4910, file "app/services/security/redirect_validation.py", line 112>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              22 (validate_redirect_target)

 200           BUILD_LIST               0
               LOAD_CONST              23 (('ALLOWED_REDIRECT_SCHEMES', 'FORBIDDEN_REDIRECT_TOKENS', 'normalise_redirect_host', 'validate_redirect_target'))
               LIST_EXTEND              1
               STORE_NAME              23 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "app/services/security/redirect_validation.py", line 75>:
 75           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('valid')

 77           LOAD_CONST               2 ('bool')

 75           LOAD_CONST               3 ('target')

 78           LOAD_CONST               4 ('Optional[str]')

 75           LOAD_CONST               5 ('error_code')

 79           LOAD_CONST               4 ('Optional[str]')

 75           LOAD_CONST               6 ('warnings')

 80           LOAD_CONST               7 ('Optional[List[str]]')

 75           LOAD_CONST               8 ('return')

 81           LOAD_CONST               9 ('Dict[str, Any]')

 75           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _safe_verdict at 0x0000018C18053870, file "app/services/security/redirect_validation.py", line 75>:
 75           RESUME                   0

 83           LOAD_CONST               0 ('valid')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         0 (valid)
              CALL                     1

 84           LOAD_CONST               1 ('target')
              LOAD_FAST                1 (target)

 85           LOAD_CONST               2 ('error_code')
              LOAD_FAST                2 (error_code)

 86           LOAD_CONST               3 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                3 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

 82           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app/services/security/redirect_validation.py", line 90>:
 90           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('url')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object normalise_redirect_host at 0x0000018C17D8E300, file "app/services/security/redirect_validation.py", line 90>:
  90            RESUME                   0

  93            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (url)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

  94            LOAD_CONST               1 (None)
                RETURN_VALUE

  95    L1:     LOAD_FAST_BORROW         0 (url)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               1 (s)

  96            LOAD_FAST_BORROW         1 (s)
                TO_BOOL
                POP_JUMP_IF_FALSE       21 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              7 (len + NULL)
                LOAD_FAST_BORROW         1 (s)
                CALL                     1
                LOAD_GLOBAL              8 (_URL_MAX_LEN)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN

  97    L2:     LOAD_CONST               1 (None)
                RETURN_VALUE

  98    L3:     LOAD_FAST_BORROW         1 (s)
                LOAD_ATTR               11 (lower + NULL|self)
                CALL                     0
                STORE_FAST               2 (lower)

  99            LOAD_GLOBAL             12 (FORBIDDEN_REDIRECT_TOKENS)
                GET_ITER
        L4:     FOR_ITER                12 (to L6)
                STORE_FAST               3 (forb)

 100            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (forb, lower)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L4)

 101    L5:     POP_TOP
                LOAD_CONST               1 (None)
                RETURN_VALUE

  99    L6:     END_FOR
                POP_ITER

 102            NOP

 103    L7:     LOAD_GLOBAL             15 (urlparse + NULL)
                LOAD_FAST_BORROW         1 (s)
                CALL                     1
                STORE_FAST               4 (parsed)

 106    L8:     LOAD_FAST                4 (parsed)
                LOAD_ATTR               18 (hostname)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L9:     LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               11 (lower + NULL|self)
                CALL                     0
                STORE_FAST               5 (host)

 107            LOAD_FAST                5 (host)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN

 108            LOAD_CONST               1 (None)
                RETURN_VALUE

 109   L10:     LOAD_FAST                5 (host)
                RETURN_VALUE

  --   L11:     PUSH_EXC_INFO

 104            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L13)
                NOT_TAKEN
                POP_TOP

 105   L12:     POP_EXCEPT
                LOAD_CONST               1 (None)
                RETURN_VALUE

 104   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L7 to L8 -> L11 [0]
  L11 to L12 -> L14 [1] lasti
  L13 to L14 -> L14 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app/services/security/redirect_validation.py", line 112>:
112           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('url')

113           LOAD_CONST               2 ('Any')

112           LOAD_CONST               3 ('allowed_hosts')

115           LOAD_CONST               4 ('Iterable[str]')

112           LOAD_CONST               5 ('allow_relative')

116           LOAD_CONST               6 ('bool')

112           LOAD_CONST               7 ('return')

117           LOAD_CONST               8 ('Dict[str, Any]')

112           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object validate_redirect_target at 0x0000018C17ED4910, file "app/services/security/redirect_validation.py", line 112>:
 112            RESUME                   0

 129            NOP

 130    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (url)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (url)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L5)
        L2:     NOT_TAKEN

 131    L3:     LOAD_GLOBAL              7 (_safe_verdict + NULL)
                LOAD_CONST               1 (False)
                LOAD_CONST               2 ('missing_redirect_target')
                LOAD_CONST               3 (('valid', 'error_code'))
                CALL_KW                  2
        L4:     RETURN_VALUE

 132    L5:     LOAD_FAST_BORROW         0 (url)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               3 (s)

 133            LOAD_GLOBAL              9 (len + NULL)
                LOAD_FAST_BORROW         3 (s)
                CALL                     1
                LOAD_GLOBAL             10 (_URL_MAX_LEN)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE       14 (to L7)
                NOT_TAKEN

 134            LOAD_GLOBAL              7 (_safe_verdict + NULL)
                LOAD_CONST               1 (False)
                LOAD_CONST               4 ('redirect_target_too_long')
                LOAD_CONST               3 (('valid', 'error_code'))
                CALL_KW                  2
        L6:     RETURN_VALUE

 135    L7:     LOAD_FAST_BORROW         3 (s)
                LOAD_ATTR               13 (lower + NULL|self)
                CALL                     0
                STORE_FAST               4 (lower)

 136            LOAD_GLOBAL             14 (FORBIDDEN_REDIRECT_TOKENS)
                GET_ITER
        L8:     FOR_ITER                29 (to L12)
                STORE_FAST               5 (forb)

 137            LOAD_FAST_BORROW_LOAD_FAST_BORROW 84 (forb, lower)
                CONTAINS_OP              0 (in)
        L9:     POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L8)

 138   L10:     LOAD_GLOBAL              7 (_safe_verdict + NULL)

 139            LOAD_CONST               1 (False)

 140            LOAD_CONST               5 ('forbidden_redirect_token')

 141            LOAD_CONST               6 ('forbidden_token:')
                LOAD_FAST_BORROW         5 (forb)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 138            LOAD_CONST               7 (('valid', 'error_code', 'warnings'))
                CALL_KW                  3
                SWAP                     2
                POP_TOP
       L11:     RETURN_VALUE

 136   L12:     END_FOR
                POP_ITER

 144            BUILD_LIST               0
                STORE_FAST               6 (hosts_lower)

 145   L13:     NOP

 146   L14:     LOAD_FAST                1 (allowed_hosts)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L17)
       L15:     NOT_TAKEN
       L16:     POP_TOP
                LOAD_CONST              24 (())
       L17:     GET_ITER
       L18:     FOR_ITER                96 (to L23)
                STORE_FAST               7 (h)

 147            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         7 (h)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
       L19:     POP_JUMP_IF_TRUE         3 (to L20)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L18)
       L20:     LOAD_FAST_BORROW         7 (h)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
       L21:     POP_JUMP_IF_TRUE         3 (to L22)
                NOT_TAKEN
                JUMP_BACKWARD           51 (to L18)

 148   L22:     LOAD_FAST_BORROW         6 (hosts_lower)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_FAST_BORROW         7 (h)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               13 (lower + NULL|self)
                CALL                     0
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           98 (to L18)

 146   L23:     END_FOR
                POP_ITER

 155   L24:     LOAD_FAST_BORROW         2 (allow_relative)
                TO_BOOL
                POP_JUMP_IF_FALSE       60 (to L32)
       L25:     NOT_TAKEN
       L26:     LOAD_FAST_BORROW         3 (s)
                LOAD_ATTR               21 (startswith + NULL|self)
                LOAD_CONST               8 ('/')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       37 (to L32)
       L27:     NOT_TAKEN
       L28:     LOAD_FAST_BORROW         3 (s)
                LOAD_ATTR               21 (startswith + NULL|self)
                LOAD_CONST               9 ('//')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L32)
       L29:     NOT_TAKEN

 156   L30:     LOAD_GLOBAL              7 (_safe_verdict + NULL)
                LOAD_CONST              10 (True)
                LOAD_FAST_BORROW         3 (s)
                LOAD_CONST              11 (('valid', 'target'))
                CALL_KW                  2
       L31:     RETURN_VALUE

 158   L32:     NOP

 159   L33:     LOAD_GLOBAL             23 (urlparse + NULL)
                LOAD_FAST_BORROW         3 (s)
                CALL                     1
                STORE_FAST               8 (parsed)

 162   L34:     LOAD_FAST                8 (parsed)
                LOAD_ATTR               24 (scheme)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L37)
       L35:     NOT_TAKEN
       L36:     POP_TOP
                LOAD_CONST              13 ('')
       L37:     LOAD_ATTR               13 (lower + NULL|self)
                CALL                     0
                STORE_FAST               9 (scheme)

 163            LOAD_FAST                9 (scheme)
                LOAD_GLOBAL             26 (ALLOWED_REDIRECT_SCHEMES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       19 (to L39)
                NOT_TAKEN

 164            LOAD_GLOBAL              7 (_safe_verdict + NULL)

 165            LOAD_CONST               1 (False)

 166            LOAD_CONST              14 ('invalid_redirect_scheme')

 167            LOAD_CONST              15 ('scheme:')
                LOAD_FAST                9 (scheme)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 164            LOAD_CONST               7 (('valid', 'error_code', 'warnings'))
                CALL_KW                  3
       L38:     RETURN_VALUE

 169   L39:     LOAD_FAST                8 (parsed)
                LOAD_ATTR               28 (hostname)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L42)
       L40:     NOT_TAKEN
       L41:     POP_TOP
                LOAD_CONST              13 ('')
       L42:     LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               13 (lower + NULL|self)
                CALL                     0
                STORE_FAST              10 (host)

 170            LOAD_FAST               10 (host)
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L46)
       L43:     NOT_TAKEN

 171   L44:     LOAD_GLOBAL              7 (_safe_verdict + NULL)

 172            LOAD_CONST               1 (False)

 173            LOAD_CONST              16 ('missing_redirect_host')

 171            LOAD_CONST               3 (('valid', 'error_code'))
                CALL_KW                  2
       L45:     RETURN_VALUE

 175   L46:     LOAD_FAST_LOAD_FAST    166 (host, hosts_lower)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       14 (to L48)
                NOT_TAKEN

 176            LOAD_GLOBAL              7 (_safe_verdict + NULL)

 177            LOAD_CONST               1 (False)

 178            LOAD_CONST              17 ('redirect_target_not_allowed')

 176            LOAD_CONST               3 (('valid', 'error_code'))
                CALL_KW                  2
       L47:     RETURN_VALUE

 182   L48:     LOAD_FAST                9 (scheme)
                FORMAT_SIMPLE
                LOAD_CONST              18 ('://')
                LOAD_FAST               10 (host)
                FORMAT_SIMPLE
                BUILD_STRING             3
                STORE_FAST              11 (canonical)

 183            LOAD_FAST                8 (parsed)
                LOAD_ATTR               30 (port)
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L51)
       L49:     NOT_TAKEN

 184   L50:     LOAD_FAST               11 (canonical)
                LOAD_CONST              19 (':')
                LOAD_FAST                8 (parsed)
                LOAD_ATTR               30 (port)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BINARY_OP               13 (+=)
                STORE_FAST              11 (canonical)

 185   L51:     LOAD_FAST                8 (parsed)
                LOAD_ATTR               32 (path)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L54)
       L52:     NOT_TAKEN
       L53:     POP_TOP
                LOAD_CONST               8 ('/')
       L54:     STORE_FAST              12 (path)

 186            LOAD_FAST_LOAD_FAST    188 (canonical, path)
                BINARY_OP               13 (+=)
                STORE_FAST              11 (canonical)

 187            LOAD_FAST                8 (parsed)
                LOAD_ATTR               34 (query)
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L55)
                NOT_TAKEN

 188            LOAD_FAST               11 (canonical)
                LOAD_CONST              20 ('?')
                LOAD_FAST                8 (parsed)
                LOAD_ATTR               34 (query)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BINARY_OP               13 (+=)
                STORE_FAST              11 (canonical)

 189   L55:     LOAD_GLOBAL              7 (_safe_verdict + NULL)
                LOAD_CONST              10 (True)
                LOAD_FAST               11 (canonical)
                LOAD_CONST              11 (('valid', 'target'))
                CALL_KW                  2
       L56:     RETURN_VALUE

  --   L57:     PUSH_EXC_INFO

 149            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        7 (to L59)
                NOT_TAKEN
                POP_TOP

 150            BUILD_LIST               0
                STORE_FAST               6 (hosts_lower)
       L58:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 380 (to L24)

 149   L59:     RERAISE                  0

  --   L60:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L61:     PUSH_EXC_INFO

 160            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       17 (to L64)
                NOT_TAKEN
                POP_TOP

 161            LOAD_GLOBAL              7 (_safe_verdict + NULL)
                LOAD_CONST               1 (False)
                LOAD_CONST              12 ('invalid_redirect_url')
                LOAD_CONST               3 (('valid', 'error_code'))
                CALL_KW                  2
                SWAP                     2
       L62:     POP_EXCEPT
       L63:     RETURN_VALUE

 160   L64:     RERAISE                  0

  --   L65:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L66:     PUSH_EXC_INFO

 190            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       89 (to L71)
                NOT_TAKEN
                STORE_FAST              13 (e)

 191   L67:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 192            LOAD_CONST              21 ('validate_redirect_target error type=')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 191            CALL                     1
                POP_TOP

 194            LOAD_GLOBAL              7 (_safe_verdict + NULL)

 195            LOAD_CONST               1 (False)

 196            LOAD_CONST              22 ('unexpected:')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 194            LOAD_CONST               3 (('valid', 'error_code'))
                CALL_KW                  2
       L68:     SWAP                     2
       L69:     POP_EXCEPT
                LOAD_CONST              23 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RETURN_VALUE

  --   L70:     LOAD_CONST              23 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RERAISE                  1

 190   L71:     RERAISE                  0

  --   L72:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L66 [0]
  L3 to L4 -> L66 [0]
  L5 to L6 -> L66 [0]
  L7 to L9 -> L66 [0]
  L10 to L11 -> L66 [0]
  L12 to L13 -> L66 [0]
  L14 to L15 -> L57 [0]
  L16 to L19 -> L57 [0]
  L20 to L21 -> L57 [0]
  L22 to L24 -> L57 [0]
  L24 to L25 -> L66 [0]
  L26 to L27 -> L66 [0]
  L28 to L29 -> L66 [0]
  L30 to L31 -> L66 [0]
  L33 to L34 -> L61 [0]
  L34 to L35 -> L66 [0]
  L36 to L38 -> L66 [0]
  L39 to L40 -> L66 [0]
  L41 to L43 -> L66 [0]
  L44 to L45 -> L66 [0]
  L46 to L47 -> L66 [0]
  L48 to L49 -> L66 [0]
  L50 to L52 -> L66 [0]
  L53 to L56 -> L66 [0]
  L57 to L58 -> L60 [1] lasti
  L58 to L59 -> L66 [0]
  L59 to L60 -> L60 [1] lasti
  L60 to L61 -> L66 [0]
  L61 to L62 -> L65 [1] lasti
  L62 to L63 -> L66 [0]
  L64 to L65 -> L65 [1] lasti
  L65 to L66 -> L66 [0]
  L66 to L67 -> L72 [1] lasti
  L67 to L68 -> L70 [1] lasti
  L68 to L69 -> L72 [1] lasti
  L70 to L72 -> L72 [1] lasti
```
