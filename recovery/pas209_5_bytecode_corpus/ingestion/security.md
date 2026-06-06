# ingestion/security

- **pyc:** `app\services\ingestion\__pycache__\security.cpython-314.pyc`
- **expected source path (absent):** `app\services\ingestion/security.py`
- **co_filename (from bytecode):** `app\services\ingestion\security.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** ingestion

## Module docstring

```
PAS161 — Webhook security helpers.

Two primitives:

* ``verify_shared_secret(request, expected_secret)`` — constant-
  time comparison of an ``X-PAS-Webhook-Secret`` header against
  an expected value. For Zapier / generic endpoints where the
  upstream cannot HMAC-sign.

* ``verify_hmac_signature(body, signature, secret)`` — constant-
  time comparison of a hex-encoded HMAC-SHA256 of the raw body
  against the upstream-provided signature. For providers that
  sign their webhooks (Follow Up Boss, GoHighLevel; the
  signature header name varies per provider).

Both helpers are pure / never raise. PAS161 ships them but
**does not yet wire them** into the four webhook routes —
routes use ``Depends(require_brokerage)`` (``X-API-Key`` flow)
for tenant gating in this phase. Per-provider signature
verification is layered on in a follow-on phase once at least
one real brokerage is connected.
```

## Imports

`Any`, `Optional`, `__future__`, `annotations`, `hashlib`, `hmac`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `verify_hmac_signature`, `verify_shared_secret`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS161 — Webhook security helpers.\n\nTwo primitives:\n\n* ``verify_shared_secret(request, expected_secret)`` — constant-\n  time comparison of an ``X-PAS-Webhook-Secret`` header against\n  an expected value. For Zapier / generic endpoints where the\n  upstream cannot HMAC-sign.\n\n* ``verify_hmac_signature(body, signature, secret)`` — constant-\n  time comparison of a hex-encoded HMAC-SHA256 of the raw body\n  against the upstream-provided signature. For providers that\n  sign their webhooks (Follow Up Boss, GoHighLevel; the\n  signature header name varies per provider).\n\nBoth helpers are pure / never raise. PAS161 ships them but\n**does not yet wire them** into the four webhook routes —\nroutes use ``Depends(require_brokerage)`` (``X-API-Key`` flow)\nfor tenant gating in this phase. Per-provider signature\nverification is layered on in a follow-on phase once at least\none real brokerage is connected.\n'
- 'algorithm'
- 'sha256'
- 'request'
- 'Any'
- 'expected_secret'
- 'Optional[str]'
- 'return'
- 'bool'
- 'Constant-time check of the ``X-PAS-Webhook-Secret`` header\nagainst ``expected_secret``.\n\nReturns ``False`` if either side is missing / empty. The\ncomparison is constant-time via ``hmac.compare_digest`` to\navoid timing-side-channel leakage of the expected secret.\n\n``request`` is typed ``Any`` because this helper is\nframework-agnostic — a FastAPI ``Request`` works; a dict-\nlike header object works; a Pydantic model with a\n``headers`` attribute works. We probe for ``.headers`` then\nfall back to direct dict access.\n'
- 'headers'
- 'x-pas-webhook-secret'
- 'X-PAS-Webhook-Secret'
- 'utf-8'
- 'body'
- 'bytes'
- 'signature'
- 'secret'
- 'str'
- 'Constant-time verification of a hex-encoded HMAC signature\nover ``body`` using ``secret``.\n\nDefaults to HMAC-SHA256 (every supported provider). Returns\n``False`` on any missing / malformed input. Never raises.\n\nHex-encoded signatures may be wrapped with a provider-\nspecific prefix (e.g. GitHub uses ``sha256=...``). This\nhelper strips a single ``sha256=`` / ``sha1=`` prefix if\npresent, then compares the remainder.\n'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS161 — Webhook security helpers.\n\nTwo primitives:\n\n* ``verify_shared_secret(request, expected_secret)`` — constant-\n  time comparison of an ``X-PAS-Webhook-Secret`` header against\n  an expected value. For Zapier / generic endpoints where the\n  upstream cannot HMAC-sign.\n\n* ``verify_hmac_signature(body, signature, secret)`` — constant-\n  time comparison of a hex-encoded HMAC-SHA256 of the raw body\n  against the upstream-provided signature. For providers that\n  sign their webhooks (Follow Up Boss, GoHighLevel; the\n  signature header name varies per provider).\n\nBoth helpers are pure / never raise. PAS161 ships them but\n**does not yet wire them** into the four webhook routes —\nroutes use ``Depends(require_brokerage)`` (``X-API-Key`` flow)\nfor tenant gating in this phase. Per-provider signature\nverification is layered on in a follow-on phase once at least\none real brokerage is connected.\n')
              STORE_NAME               0 (__doc__)

 25           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 27           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (hashlib)
              STORE_NAME               3 (hashlib)

 28           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (hmac)
              STORE_NAME               4 (hmac)

 29           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Optional'))
              IMPORT_NAME              5 (typing)
              IMPORT_FROM              6 (Any)
              STORE_NAME               6 (Any)
              IMPORT_FROM              7 (Optional)
              STORE_NAME               7 (Optional)
              POP_TOP

 32           LOAD_CONST               4 (<code object __annotate__ at 0x0000018C18025D30, file "app\services\ingestion\security.py", line 32>)
              MAKE_FUNCTION
              LOAD_CONST               5 (<code object verify_shared_secret at 0x0000018C17F7EF60, file "app\services\ingestion\security.py", line 32>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME               8 (verify_shared_secret)

 75           LOAD_CONST               6 ('algorithm')

 80           LOAD_CONST               7 ('sha256')

 75           BUILD_MAP                1
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C18025730, file "app\services\ingestion\security.py", line 75>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object verify_hmac_signature at 0x0000018C17F843E0, file "app\services\ingestion\security.py", line 75>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME               9 (verify_hmac_signature)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\services\ingestion\security.py", line 32>:
 32           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('request')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('expected_secret')
              LOAD_CONST               4 ('Optional[str]')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('bool')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object verify_shared_secret at 0x0000018C17F7EF60, file "app\services\ingestion\security.py", line 32>:
  32            RESUME                   0

  46            LOAD_FAST_BORROW         1 (expected_secret)
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L1)
                NOT_TAKEN
                LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (expected_secret)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN

  47    L1:     LOAD_CONST               1 (False)
                RETURN_VALUE

  48    L2:     LOAD_FAST_BORROW         1 (expected_secret)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               2 (expected)

  49            LOAD_FAST_BORROW         2 (expected)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN

  50            LOAD_CONST               1 (False)
                RETURN_VALUE

  53    L3:     LOAD_CONST               2 (None)
                STORE_FAST               3 (presented)

  54            LOAD_GLOBAL              7 (getattr + NULL)
                LOAD_FAST_BORROW         0 (request)
                LOAD_CONST               3 ('headers')
                LOAD_CONST               2 (None)
                CALL                     3
                STORE_FAST               4 (headers)

  55            LOAD_FAST_BORROW         4 (headers)
                POP_JUMP_IF_NONE        45 (to L9)
                NOT_TAKEN

  56            NOP

  57    L4:     LOAD_FAST_BORROW         4 (headers)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               4 ('x-pas-webhook-secret')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP

  58            LOAD_FAST_BORROW         4 (headers)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               5 ('X-PAS-Webhook-Secret')
                CALL                     1

  57    L7:     STORE_FAST               3 (presented)
        L8:     JUMP_FORWARD            64 (to L11)

  61    L9:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (request)
                LOAD_GLOBAL             12 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       43 (to L11)
                NOT_TAKEN

  62            LOAD_FAST_BORROW         0 (request)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               5 ('X-PAS-Webhook-Secret')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L10)
                NOT_TAKEN
                POP_TOP

  63            LOAD_FAST_BORROW         0 (request)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               4 ('x-pas-webhook-secret')
                CALL                     1

  62   L10:     STORE_FAST               3 (presented)

  65   L11:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (presented)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN

  66            LOAD_CONST               1 (False)
                RETURN_VALUE

  67   L12:     LOAD_FAST_BORROW         3 (presented)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               3 (presented)

  68            LOAD_FAST_BORROW         3 (presented)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN

  69            LOAD_CONST               1 (False)
                RETURN_VALUE

  71   L13:     LOAD_GLOBAL             14 (hmac)
                LOAD_ATTR               16 (compare_digest)
                PUSH_NULL
                LOAD_FAST_BORROW         3 (presented)
                LOAD_ATTR               19 (encode + NULL|self)
                LOAD_CONST               6 ('utf-8')
                CALL                     1

  72            LOAD_FAST_BORROW         2 (expected)
                LOAD_ATTR               19 (encode + NULL|self)
                LOAD_CONST               6 ('utf-8')
                CALL                     1

  71            CALL                     2
                RETURN_VALUE

  --   L14:     PUSH_EXC_INFO

  59            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L16)
                NOT_TAKEN
                POP_TOP

  60            LOAD_CONST               2 (None)
                STORE_FAST               3 (presented)
       L15:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 118 (to L11)

  59   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L14 [0]
  L6 to L8 -> L14 [0]
  L14 to L15 -> L17 [1] lasti
  L16 to L17 -> L17 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app\services\ingestion\security.py", line 75>:
 75           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')

 76           LOAD_CONST               2 ('bytes')

 75           LOAD_CONST               3 ('signature')

 77           LOAD_CONST               4 ('Optional[str]')

 75           LOAD_CONST               5 ('secret')

 78           LOAD_CONST               4 ('Optional[str]')

 75           LOAD_CONST               6 ('algorithm')

 80           LOAD_CONST               7 ('str')

 75           LOAD_CONST               8 ('return')

 81           LOAD_CONST               9 ('bool')

 75           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object verify_hmac_signature at 0x0000018C17F843E0, file "app\services\ingestion\security.py", line 75>:
  75            RESUME                   0

  93            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (body)
                LOAD_GLOBAL              2 (bytes)
                LOAD_GLOBAL              4 (bytearray)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

  94            LOAD_CONST               1 (False)
                RETURN_VALUE

  95    L1:     LOAD_FAST_BORROW         1 (signature)
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (signature)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN

  96    L2:     LOAD_CONST               1 (False)
                RETURN_VALUE

  97    L3:     LOAD_FAST_BORROW         2 (secret)
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L4)
                NOT_TAKEN
                LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (secret)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN

  98    L4:     LOAD_CONST               1 (False)
                RETURN_VALUE

 100    L5:     LOAD_FAST_BORROW         1 (signature)
                LOAD_ATTR                9 (strip + NULL|self)
                CALL                     0
                STORE_FAST               4 (sig)

 102            LOAD_CONST               4 (('sha256=', 'sha1=', 'hmac-sha256=', 'hmac='))
                GET_ITER
        L6:     FOR_ITER                56 (to L8)
                STORE_FAST               5 (prefix)

 103            LOAD_FAST_BORROW         4 (sig)
                LOAD_ATTR               11 (lower + NULL|self)
                CALL                     0
                LOAD_ATTR               13 (startswith + NULL|self)
                LOAD_FAST_BORROW         5 (prefix)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           42 (to L6)

 104    L7:     LOAD_FAST_BORROW         4 (sig)
                LOAD_GLOBAL             15 (len + NULL)
                LOAD_FAST_BORROW         5 (prefix)
                CALL                     1
                LOAD_CONST               2 (None)
                BINARY_SLICE
                STORE_FAST               4 (sig)

 105            POP_TOP
                JUMP_FORWARD             2 (to L9)

 102    L8:     END_FOR
                POP_ITER

 106    L9:     LOAD_FAST_BORROW         4 (sig)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN

 107            LOAD_CONST               1 (False)
                RETURN_VALUE

 109   L10:     NOP

 110   L11:     LOAD_GLOBAL             16 (hmac)
                LOAD_ATTR               18 (new)
                PUSH_NULL

 111            LOAD_FAST_BORROW         2 (secret)
                LOAD_ATTR               21 (encode + NULL|self)
                LOAD_CONST               3 ('utf-8')
                CALL                     1

 112            LOAD_GLOBAL              3 (bytes + NULL)
                LOAD_FAST_BORROW         0 (body)
                CALL                     1

 113            LOAD_GLOBAL             23 (getattr + NULL)
                LOAD_GLOBAL             24 (hashlib)
                LOAD_FAST_BORROW         3 (algorithm)
                CALL                     2

 110            CALL                     3

 114            LOAD_ATTR               27 (hexdigest + NULL|self)
                CALL                     0

 110            STORE_FAST               6 (mac)

 118   L12:     LOAD_GLOBAL             16 (hmac)
                LOAD_ATTR               30 (compare_digest)
                PUSH_NULL
                LOAD_FAST                6 (mac)
                LOAD_ATTR               21 (encode + NULL|self)
                LOAD_CONST               3 ('utf-8')
                CALL                     1

 119            LOAD_FAST                4 (sig)
                LOAD_ATTR               11 (lower + NULL|self)
                CALL                     0
                LOAD_ATTR               21 (encode + NULL|self)
                LOAD_CONST               3 ('utf-8')
                CALL                     1

 118            CALL                     2
                RETURN_VALUE

  --   L13:     PUSH_EXC_INFO

 115            LOAD_GLOBAL             28 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L15)
                NOT_TAKEN
                POP_TOP

 116   L14:     POP_EXCEPT
                LOAD_CONST               1 (False)
                RETURN_VALUE

 115   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L11 to L12 -> L13 [0]
  L13 to L14 -> L16 [1] lasti
  L15 to L16 -> L16 [1] lasti
```
