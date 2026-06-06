# ingestion/email_auth

- **pyc:** `app\services\ingestion\__pycache__\email_auth.cpython-314.pyc`
- **expected source path (absent):** `app\services\ingestion/email_auth.py`
- **co_filename (from bytecode):** `app\services\ingestion\email_auth.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** ingestion

## Module docstring

```
PAS165 — Email forwarder signature verification.

Optional HMAC-style signature on the inbound email-ingestion
forwarder so PAS can confirm a forwarded email actually came
from the brokerage's authorised forwarder, not from someone
who scraped a brokerage's API key.

Doctrine carried by every helper here:

* The verifier is a pure function. It NEVER raises on
  malformed input or comparison failure.
* The verifier NEVER echoes the secret, the provided
  signature, the computed signature, or the raw body in any
  warning, error, or return value.
* The signing surface NEVER signs the raw body directly. The
  body is hashed first (capped at 64 KB) and only the digest
  enters the canonical payload. That keeps the signature
  computation memory-bounded and removes any path where the
  body could be re-hashed during verification.
* The verifier uses constant-time comparison
  (``hmac.compare_digest``) to remove a timing oracle.

Header format:
    X-Forwarder-Signature: sha256=<hex>

Soft-rollout policy:

The verifier returns a structural envelope rather than a
binary "valid / invalid". The four states the caller cares
about:

* signature provided AND secret configured AND match
  → ``valid=True, verified=True``
* signature provided AND secret configured AND mismatch
  → ``valid=False, error_code="forwarder_signature_invalid"``
* signature provided AND malformed (no ``sha256=`` prefix /
  not lower-hex / wrong length)
  → ``valid=False, error_code="forwarder_signature_malformed"``
* signature missing OR secret missing
  → ``valid=True, verified=False`` with a structural warning
    (``forwarder_signature_missing`` /
     ``forwarder_signature_unconfigured``).
    Ingestion is still allowed in this phase. A future phase
    may flip the policy to "missing → reject".

Reason for the soft rollout: brokerages onboarding their
forwarder will not have a signed forwarder on day one. We
want to capture the lead, surface a structural warning, and
let the operator turn signing on once the brokerage has the
infrastructure.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `hashlib`, `hmac`, `logging`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_capped_body_bytes`, `_envelope`, `_hash_body`, `_looks_like_well_formed_sig`, `_trim`, `canonical_forward_payload`, `sign_forward_payload`, `verify_forwarder_signature`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS165 — Email forwarder signature verification.\n\nOptional HMAC-style signature on the inbound email-ingestion\nforwarder so PAS can confirm a forwarded email actually came\nfrom the brokerage\'s authorised forwarder, not from someone\nwho scraped a brokerage\'s API key.\n\nDoctrine carried by every helper here:\n\n* The verifier is a pure function. It NEVER raises on\n  malformed input or comparison failure.\n* The verifier NEVER echoes the secret, the provided\n  signature, the computed signature, or the raw body in any\n  warning, error, or return value.\n* The signing surface NEVER signs the raw body directly. The\n  body is hashed first (capped at 64 KB) and only the digest\n  enters the canonical payload. That keeps the signature\n  computation memory-bounded and removes any path where the\n  body could be re-hashed during verification.\n* The verifier uses constant-time comparison\n  (``hmac.compare_digest``) to remove a timing oracle.\n\nHeader format:\n    X-Forwarder-Signature: sha256=<hex>\n\nSoft-rollout policy:\n\nThe verifier returns a structural envelope rather than a\nbinary "valid / invalid". The four states the caller cares\nabout:\n\n* signature provided AND secret configured AND match\n  → ``valid=True, verified=True``\n* signature provided AND secret configured AND mismatch\n  → ``valid=False, error_code="forwarder_signature_invalid"``\n* signature provided AND malformed (no ``sha256=`` prefix /\n  not lower-hex / wrong length)\n  → ``valid=False, error_code="forwarder_signature_malformed"``\n* signature missing OR secret missing\n  → ``valid=True, verified=False`` with a structural warning\n    (``forwarder_signature_missing`` /\n     ``forwarder_signature_unconfigured``).\n    Ingestion is still allowed in this phase. A future phase\n    may flip the policy to "missing → reject".\n\nReason for the soft rollout: brokerages onboarding their\nforwarder will not have a signed forwarder on day one. We\nwant to capture the lead, surface a structural warning, and\nlet the operator turn signing on once the brokerage has the\ninfrastructure.\n'
- 'pas.ingestion.email_auth'
- 'sha256='
- '0123456789abcdef'
- 'warnings'
- 'error_code'
- 'value'
- 'Any'
- 'return'
- 'str'
- 'Defensive trim that collapses ``None`` / non-strings to\nempty string. NEVER raises.'
- 'utf-8'
- 'replace'
- 'body'
- 'bytes'
- 'Return the body sliced to ``_BODY_HASH_CAP_BYTES``. Encodes\nUTF-8 with replacement before slicing so the cap is a true\nbyte cap, not a character cap. NEVER raises.'
- 'SHA-256 of the capped body as lowercase hex. NEVER raises.'
- '_hash_body unexpected error type='
- 'sender'
- 'Optional[str]'
- 'subject'
- 'Build the canonical payload that gets signed.\n\nFormat::\n\n    lower(sender.trim()) + "\\n"\n    + lower(subject.trim()) + "\\n"\n    + sha256(body[:65536])\n\nThe body is HASHED, not embedded — this caps the canonical\npayload size and removes any path where the raw body could\nleak via the signing surface.\n\nNEVER raises. NEVER echoes the body.\n'
- 'secret'
- 'Compute the signature for a forward payload.\n\nReturns the header-shaped string ``"sha256=<hex>"``. If the\nsecret is missing or empty, returns ``"sha256="`` (an empty\ndigest tail) — callers should treat that as "no signature\navailable" rather than a valid signature.\n\nNEVER raises. NEVER echoes the secret.\n'
- 'sign_forward_payload unexpected error type='
- 'valid'
- 'bool'
- 'verified'
- 'Optional[List[str]]'
- 'Dict[str, Any]'
- 'provided'
- 'Strict shape check: ``sha256=<64 lower-hex>``. NEVER\nraises. NEVER echoes the provided value.'
- 'provided_signature'
- 'Verify a forwarder signature.\n\nReturns the closed-shape envelope::\n\n    {\n      "valid":      bool,\n      "verified":   bool,\n      "warnings":   [<structural tokens>],\n      "error_code": None | "<structural token>",\n    }\n\nSoft-rollout decision matrix:\n\n* secret missing → ``valid=True, verified=False``,\n  ``forwarder_signature_unconfigured`` warning.\n* signature missing → ``valid=True, verified=False``,\n  ``forwarder_signature_missing`` warning.\n* signature malformed → ``valid=False`` with\n  ``error_code="forwarder_signature_malformed"``.\n* signature mismatch → ``valid=False`` with\n  ``error_code="forwarder_signature_invalid"``.\n* signature match → ``valid=True, verified=True``.\n\nNEVER raises. NEVER echoes the secret, the provided\nsignature, the computed signature, or any of\nsender/subject/body.\n'
- 'forwarder_signature_unconfigured'
- 'forwarder_signature_missing'
- 'forwarder_signature_malformed'
- 'verify_forwarder_signature compute error type='
- 'forwarder_signature_compute_failed'
- 'verify_forwarder_signature compare error type='
- 'forwarder_signature_invalid'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS165 — Email forwarder signature verification.\n\nOptional HMAC-style signature on the inbound email-ingestion\nforwarder so PAS can confirm a forwarded email actually came\nfrom the brokerage\'s authorised forwarder, not from someone\nwho scraped a brokerage\'s API key.\n\nDoctrine carried by every helper here:\n\n* The verifier is a pure function. It NEVER raises on\n  malformed input or comparison failure.\n* The verifier NEVER echoes the secret, the provided\n  signature, the computed signature, or the raw body in any\n  warning, error, or return value.\n* The signing surface NEVER signs the raw body directly. The\n  body is hashed first (capped at 64 KB) and only the digest\n  enters the canonical payload. That keeps the signature\n  computation memory-bounded and removes any path where the\n  body could be re-hashed during verification.\n* The verifier uses constant-time comparison\n  (``hmac.compare_digest``) to remove a timing oracle.\n\nHeader format:\n    X-Forwarder-Signature: sha256=<hex>\n\nSoft-rollout policy:\n\nThe verifier returns a structural envelope rather than a\nbinary "valid / invalid". The four states the caller cares\nabout:\n\n* signature provided AND secret configured AND match\n  → ``valid=True, verified=True``\n* signature provided AND secret configured AND mismatch\n  → ``valid=False, error_code="forwarder_signature_invalid"``\n* signature provided AND malformed (no ``sha256=`` prefix /\n  not lower-hex / wrong length)\n  → ``valid=False, error_code="forwarder_signature_malformed"``\n* signature missing OR secret missing\n  → ``valid=True, verified=False`` with a structural warning\n    (``forwarder_signature_missing`` /\n     ``forwarder_signature_unconfigured``).\n    Ingestion is still allowed in this phase. A future phase\n    may flip the policy to "missing → reject".\n\nReason for the soft rollout: brokerages onboarding their\nforwarder will not have a signed forwarder on day one. We\nwant to capture the lead, surface a structural warning, and\nlet the operator turn signing on once the brokerage has the\ninfrastructure.\n')
              STORE_NAME               0 (__doc__)

 54           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 56           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (hashlib)
              STORE_NAME               3 (hashlib)

 57           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (hmac)
              STORE_NAME               4 (hmac)

 58           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              5 (logging)
              STORE_NAME               5 (logging)

 59           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              6 (typing)
              IMPORT_FROM              7 (Any)
              STORE_NAME               7 (Any)
              IMPORT_FROM              8 (Dict)
              STORE_NAME               8 (Dict)
              IMPORT_FROM              9 (List)
              STORE_NAME               9 (List)
              IMPORT_FROM             10 (Optional)
              STORE_NAME              10 (Optional)
              POP_TOP

 62           LOAD_NAME                5 (logging)
              LOAD_ATTR               22 (getLogger)
              PUSH_NULL
              LOAD_CONST               4 ('pas.ingestion.email_auth')
              CALL                     1
              STORE_NAME              12 (logger)

 69           LOAD_CONST              25 (65536)
              STORE_NAME              13 (_BODY_HASH_CAP_BYTES)

 76           LOAD_CONST               5 ('sha256=')
              STORE_NAME              14 (_SIG_PREFIX)

 79           LOAD_SMALL_INT          64
              STORE_NAME              15 (_SHA256_HEX_LEN)

 80           LOAD_NAME               16 (set)
              PUSH_NULL
              LOAD_CONST               6 ('0123456789abcdef')
              CALL                     1
              STORE_NAME              17 (_HEX_CHARSET)

 87           LOAD_CONST               7 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\ingestion\email_auth.py", line 87>)
              MAKE_FUNCTION
              LOAD_CONST               8 (<code object _trim at 0x0000018C17EC4280, file "app\services\ingestion\email_auth.py", line 87>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              18 (_trim)

105           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA3780, file "app\services\ingestion\email_auth.py", line 105>)
              MAKE_FUNCTION
              LOAD_CONST              10 (<code object _capped_body_bytes at 0x0000018C17FED630, file "app\services\ingestion\email_auth.py", line 105>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              19 (_capped_body_bytes)

126           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA3870, file "app\services\ingestion\email_auth.py", line 126>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object _hash_body at 0x0000018C17FEDA30, file "app\services\ingestion\email_auth.py", line 126>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              20 (_hash_body)

137           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18025B30, file "app\services\ingestion\email_auth.py", line 137>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object canonical_forward_payload at 0x0000018C18010DF0, file "app\services\ingestion\email_auth.py", line 137>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (canonical_forward_payload)

162           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\ingestion\email_auth.py", line 162>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object sign_forward_payload at 0x0000018C17EDA290, file "app\services\ingestion\email_auth.py", line 162>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (sign_forward_payload)

198           LOAD_CONST              17 ('warnings')

202           LOAD_CONST               2 (None)

198           LOAD_CONST              18 ('error_code')

203           LOAD_CONST               2 (None)

198           BUILD_MAP                2
              LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18025D30, file "app\services\ingestion\email_auth.py", line 198>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _envelope at 0x0000018C1802C620, file "app\services\ingestion\email_auth.py", line 198>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              23 (_envelope)

213           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA3A50, file "app\services\ingestion\email_auth.py", line 213>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _looks_like_well_formed_sig at 0x0000018C180483B0, file "app\services\ingestion\email_auth.py", line 213>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_looks_like_well_formed_sig)

229           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C18025E30, file "app\services\ingestion\email_auth.py", line 229>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object verify_forwarder_signature at 0x0000018C17F84930, file "app\services\ingestion\email_auth.py", line 229>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (verify_forwarder_signature)

342           BUILD_LIST               0
              LOAD_CONST              26 (('canonical_forward_payload', 'sign_forward_payload', 'verify_forwarder_signature'))
              LIST_EXTEND              1
              STORE_NAME              26 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\ingestion\email_auth.py", line 87>:
 87           RESUME                   0
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
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _trim at 0x0000018C17EC4280, file "app\services\ingestion\email_auth.py", line 87>:
  87            RESUME                   0

  90            LOAD_FAST_BORROW         0 (value)
                POP_JUMP_IF_NOT_NONE     3 (to L1)
                NOT_TAKEN

  91            LOAD_CONST               1 ('')
                RETURN_VALUE

  92    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL              2 (bytes)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L4)
                NOT_TAKEN

  93            NOP

  94    L2:     LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR                5 (decode + NULL|self)
                LOAD_CONST               2 ('utf-8')
                LOAD_CONST               3 ('replace')
                LOAD_CONST               4 (('errors',))
                CALL_KW                  2
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
        L3:     RETURN_VALUE

  97    L4:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL             10 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        27 (to L7)
                NOT_TAKEN

  98            NOP

  99    L5:     LOAD_GLOBAL             11 (str + NULL)
                LOAD_FAST_BORROW         0 (value)
                CALL                     1
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
        L6:     RETURN_VALUE

 102    L7:     LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

  95            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L10)
                NOT_TAKEN
                POP_TOP

  96    L9:     POP_EXCEPT
                LOAD_CONST               1 ('')
                RETURN_VALUE

  95   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L12:     PUSH_EXC_INFO

 100            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L14)
                NOT_TAKEN
                POP_TOP

 101   L13:     POP_EXCEPT
                LOAD_CONST               1 ('')
                RETURN_VALUE

 100   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L8 [0]
  L5 to L6 -> L12 [0]
  L8 to L9 -> L11 [1] lasti
  L10 to L11 -> L11 [1] lasti
  L12 to L13 -> L15 [1] lasti
  L14 to L15 -> L15 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app\services\ingestion\email_auth.py", line 105>:
105           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bytes')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _capped_body_bytes at 0x0000018C17FED630, file "app\services\ingestion\email_auth.py", line 105>:
 105            RESUME                   0

 109            LOAD_FAST_BORROW         0 (body)
                POP_JUMP_IF_NOT_NONE     3 (to L1)
                NOT_TAKEN

 110            LOAD_CONST               2 (b'')
                RETURN_VALUE

 111    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (body)
                LOAD_GLOBAL              2 (bytes)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        4 (to L2)
                NOT_TAKEN

 112            LOAD_FAST                0 (body)
                STORE_FAST               1 (encoded)
                JUMP_FORWARD            72 (to L7)

 113    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (body)
                LOAD_GLOBAL              4 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       22 (to L5)
                NOT_TAKEN

 114            NOP

 115    L3:     LOAD_FAST_BORROW         0 (body)
                LOAD_ATTR                7 (encode + NULL|self)
                LOAD_CONST               3 ('utf-8')
                LOAD_CONST               4 ('replace')
                LOAD_CONST               5 (('errors',))
                CALL_KW                  2
                STORE_FAST               1 (encoded)
        L4:     JUMP_FORWARD            29 (to L7)

 119    L5:     NOP

 120    L6:     LOAD_GLOBAL              5 (str + NULL)
                LOAD_FAST_BORROW         0 (body)
                CALL                     1
                LOAD_ATTR                7 (encode + NULL|self)
                LOAD_CONST               3 ('utf-8')
                LOAD_CONST               4 ('replace')
                LOAD_CONST               5 (('errors',))
                CALL_KW                  2
                STORE_FAST               1 (encoded)

 123    L7:     LOAD_FAST_BORROW         1 (encoded)
                LOAD_CONST               1 (None)
                LOAD_GLOBAL             10 (_BODY_HASH_CAP_BYTES)
                BINARY_SLICE
                RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

 116            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L10)
                NOT_TAKEN
                POP_TOP

 117    L9:     POP_EXCEPT
                LOAD_CONST               2 (b'')
                RETURN_VALUE

 116   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L12:     PUSH_EXC_INFO

 121            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L14)
                NOT_TAKEN
                POP_TOP

 122   L13:     POP_EXCEPT
                LOAD_CONST               2 (b'')
                RETURN_VALUE

 121   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L8 [0]
  L6 to L7 -> L12 [0]
  L8 to L9 -> L11 [1] lasti
  L10 to L11 -> L11 [1] lasti
  L12 to L13 -> L15 [1] lasti
  L14 to L15 -> L15 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\services\ingestion\email_auth.py", line 126>:
126           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _hash_body at 0x0000018C17FEDA30, file "app\services\ingestion\email_auth.py", line 126>:
 126           RESUME                   0

 128           NOP

 129   L1:     LOAD_GLOBAL              0 (hashlib)
               LOAD_ATTR                2 (sha256)
               PUSH_NULL
               LOAD_GLOBAL              5 (_capped_body_bytes + NULL)
               LOAD_FAST_BORROW         0 (body)
               CALL                     1
               CALL                     1
               LOAD_ATTR                7 (hexdigest + NULL|self)
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 130           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       90 (to L8)
               NOT_TAKEN
               STORE_FAST               1 (e)

 131   L4:     LOAD_GLOBAL             10 (logger)
               LOAD_ATTR               13 (warning + NULL|self)

 132           LOAD_CONST               1 ('_hash_body unexpected error type=')
               LOAD_GLOBAL             15 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               16 (__name__)
               FORMAT_SIMPLE
               BUILD_STRING             2

 131           CALL                     1
               POP_TOP

 134           LOAD_GLOBAL              0 (hashlib)
               LOAD_ATTR                2 (sha256)
               PUSH_NULL
               LOAD_CONST               2 (b'')
               CALL                     1
               LOAD_ATTR                7 (hexdigest + NULL|self)
               CALL                     0
       L5:     SWAP                     2
       L6:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RETURN_VALUE

  --   L7:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 130   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L9 [1] lasti
  L4 to L5 -> L7 [1] lasti
  L5 to L6 -> L9 [1] lasti
  L7 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025B30, file "app\services\ingestion\email_auth.py", line 137>:
137           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('sender')

138           LOAD_CONST               2 ('Optional[str]')

137           LOAD_CONST               3 ('subject')

139           LOAD_CONST               2 ('Optional[str]')

137           LOAD_CONST               4 ('body')

140           LOAD_CONST               2 ('Optional[str]')

137           LOAD_CONST               5 ('return')

141           LOAD_CONST               6 ('str')

137           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object canonical_forward_payload at 0x0000018C18010DF0, file "app\services\ingestion\email_auth.py", line 137>:
137           RESUME                   0

156           LOAD_GLOBAL              1 (_trim + NULL)
              LOAD_FAST_BORROW         0 (sender)
              CALL                     1
              LOAD_ATTR                3 (lower + NULL|self)
              CALL                     0
              STORE_FAST               3 (s)

157           LOAD_GLOBAL              1 (_trim + NULL)
              LOAD_FAST_BORROW         1 (subject)
              CALL                     1
              LOAD_ATTR                3 (lower + NULL|self)
              CALL                     0
              STORE_FAST               4 (j)

158           LOAD_GLOBAL              5 (_hash_body + NULL)
              LOAD_FAST_BORROW         2 (body)
              CALL                     1
              STORE_FAST               5 (body_digest)

159           LOAD_FAST_BORROW         3 (s)
              FORMAT_SIMPLE
              LOAD_CONST               1 ('\n')
              LOAD_FAST_BORROW         4 (j)
              FORMAT_SIMPLE
              LOAD_CONST               1 ('\n')
              LOAD_FAST_BORROW         5 (body_digest)
              FORMAT_SIMPLE
              BUILD_STRING             5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\ingestion\email_auth.py", line 162>:
162           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('secret')

163           LOAD_CONST               2 ('Any')

162           LOAD_CONST               3 ('sender')

164           LOAD_CONST               4 ('Optional[str]')

162           LOAD_CONST               5 ('subject')

165           LOAD_CONST               4 ('Optional[str]')

162           LOAD_CONST               6 ('body')

166           LOAD_CONST               4 ('Optional[str]')

162           LOAD_CONST               7 ('return')

167           LOAD_CONST               8 ('str')

162           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object sign_forward_payload at 0x0000018C17EDA290, file "app\services\ingestion\email_auth.py", line 162>:
 162            RESUME                   0

 177            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (secret)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (secret)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         7 (to L2)
                NOT_TAKEN

 178    L1:     LOAD_GLOBAL              6 (_SIG_PREFIX)
                RETURN_VALUE

 179    L2:     LOAD_GLOBAL              9 (canonical_forward_payload + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (sender, subject)
                LOAD_FAST_BORROW         3 (body)
                CALL                     3
                STORE_FAST               4 (canonical)

 180            NOP

 181    L3:     LOAD_GLOBAL             10 (hmac)
                LOAD_ATTR               12 (new)
                PUSH_NULL

 182            LOAD_FAST_BORROW         0 (secret)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               15 (encode + NULL|self)
                LOAD_CONST               1 ('utf-8')
                LOAD_CONST               2 ('replace')
                LOAD_CONST               3 (('errors',))
                CALL_KW                  2

 183            LOAD_FAST_BORROW         4 (canonical)
                LOAD_ATTR               15 (encode + NULL|self)
                LOAD_CONST               1 ('utf-8')
                LOAD_CONST               2 ('replace')
                LOAD_CONST               3 (('errors',))
                CALL_KW                  2

 184            LOAD_GLOBAL             16 (hashlib)
                LOAD_ATTR               18 (sha256)

 181            CALL                     3

 185            LOAD_ATTR               21 (hexdigest + NULL|self)
                CALL                     0

 181            STORE_FAST               5 (digest)

 191    L4:     LOAD_GLOBAL              6 (_SIG_PREFIX)
                LOAD_FAST_BORROW         5 (digest)
                BINARY_OP                0 (+)
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 186            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       60 (to L10)
                NOT_TAKEN
                STORE_FAST               6 (e)

 187    L6:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 188            LOAD_CONST               4 ('sign_forward_payload unexpected error type=')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 187            CALL                     1
                POP_TOP

 190            LOAD_GLOBAL              6 (_SIG_PREFIX)
        L7:     SWAP                     2
        L8:     POP_EXCEPT
                LOAD_CONST               5 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --    L9:     LOAD_CONST               5 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 186   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L5 [0]
  L5 to L6 -> L11 [1] lasti
  L6 to L7 -> L9 [1] lasti
  L7 to L8 -> L11 [1] lasti
  L9 to L11 -> L11 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\services\ingestion\email_auth.py", line 198>:
198           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('valid')

200           LOAD_CONST               2 ('bool')

198           LOAD_CONST               3 ('verified')

201           LOAD_CONST               2 ('bool')

198           LOAD_CONST               4 ('warnings')

202           LOAD_CONST               5 ('Optional[List[str]]')

198           LOAD_CONST               6 ('error_code')

203           LOAD_CONST               7 ('Optional[str]')

198           LOAD_CONST               8 ('return')

204           LOAD_CONST               9 ('Dict[str, Any]')

198           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _envelope at 0x0000018C1802C620, file "app\services\ingestion\email_auth.py", line 198>:
198           RESUME                   0

206           LOAD_CONST               0 ('valid')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         0 (valid)
              CALL                     1

207           LOAD_CONST               1 ('verified')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         1 (verified)
              CALL                     1

208           LOAD_CONST               2 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                2 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

209           LOAD_CONST               3 ('error_code')
              LOAD_FAST_BORROW         3 (error_code)

205           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app\services\ingestion\email_auth.py", line 213>:
213           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('provided')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _looks_like_well_formed_sig at 0x0000018C180483B0, file "app\services\ingestion\email_auth.py", line 213>:
213           RESUME                   0

216           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (provided)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

217           LOAD_CONST               1 (False)
              RETURN_VALUE

218   L1:     LOAD_FAST_BORROW         0 (provided)
              LOAD_ATTR                5 (startswith + NULL|self)
              LOAD_GLOBAL              6 (_SIG_PREFIX)
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

219           LOAD_CONST               1 (False)
              RETURN_VALUE

220   L2:     LOAD_FAST_BORROW         0 (provided)
              LOAD_GLOBAL              9 (len + NULL)
              LOAD_GLOBAL              6 (_SIG_PREFIX)
              CALL                     1
              LOAD_CONST               2 (None)
              BINARY_SLICE
              STORE_FAST               1 (tail)

221           LOAD_GLOBAL              9 (len + NULL)
              LOAD_FAST_BORROW         1 (tail)
              CALL                     1
              LOAD_GLOBAL             10 (_SHA256_HEX_LEN)
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

222           LOAD_CONST               1 (False)
              RETURN_VALUE

223   L3:     LOAD_FAST_BORROW         1 (tail)
              GET_ITER
      L4:     FOR_ITER                17 (to L6)
              STORE_FAST               2 (ch)

224           LOAD_FAST_BORROW         2 (ch)
              LOAD_GLOBAL             12 (_HEX_CHARSET)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           16 (to L4)

225   L5:     POP_TOP
              LOAD_CONST               1 (False)
              RETURN_VALUE

223   L6:     END_FOR
              POP_ITER

226           LOAD_CONST               3 (True)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app\services\ingestion\email_auth.py", line 229>:
229           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('sender')

231           LOAD_CONST               2 ('Optional[str]')

229           LOAD_CONST               3 ('subject')

232           LOAD_CONST               2 ('Optional[str]')

229           LOAD_CONST               4 ('body')

233           LOAD_CONST               2 ('Optional[str]')

229           LOAD_CONST               5 ('provided_signature')

234           LOAD_CONST               2 ('Optional[str]')

229           LOAD_CONST               6 ('secret')

235           LOAD_CONST               2 ('Optional[str]')

229           LOAD_CONST               7 ('return')

236           LOAD_CONST               8 ('Dict[str, Any]')

229           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object verify_forwarder_signature at 0x0000018C17F84930, file "app\services\ingestion\email_auth.py", line 229>:
 229            RESUME                   0

 265            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (secret)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L1)
                NOT_TAKEN
                LOAD_GLOBAL              5 (_trim + NULL)
                LOAD_FAST_BORROW         4 (secret)
                CALL                     1
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST               1 ('')
        L2:     STORE_FAST               5 (secret_clean)

 266            LOAD_FAST_BORROW         5 (secret_clean)
                TO_BOOL
                POP_JUMP_IF_TRUE        16 (to L3)
                NOT_TAKEN

 267            LOAD_GLOBAL              7 (_envelope + NULL)

 268            LOAD_CONST               2 (True)

 269            LOAD_CONST               3 (False)

 270            LOAD_CONST               4 ('forwarder_signature_unconfigured')
                BUILD_LIST               1

 267            LOAD_CONST               5 (('valid', 'verified', 'warnings'))
                CALL_KW                  3
                RETURN_VALUE

 274    L3:     LOAD_GLOBAL              5 (_trim + NULL)
                LOAD_FAST_BORROW         3 (provided_signature)
                CALL                     1
                STORE_FAST               6 (provided_clean)

 275            LOAD_FAST_BORROW         6 (provided_clean)
                TO_BOOL
                POP_JUMP_IF_TRUE        16 (to L4)
                NOT_TAKEN

 276            LOAD_GLOBAL              7 (_envelope + NULL)

 277            LOAD_CONST               2 (True)

 278            LOAD_CONST               3 (False)

 279            LOAD_CONST               6 ('forwarder_signature_missing')
                BUILD_LIST               1

 276            LOAD_CONST               5 (('valid', 'verified', 'warnings'))
                CALL_KW                  3
                RETURN_VALUE

 283    L4:     LOAD_GLOBAL              9 (_looks_like_well_formed_sig + NULL)
                LOAD_FAST_BORROW         6 (provided_clean)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L5)
                NOT_TAKEN

 284            LOAD_GLOBAL              7 (_envelope + NULL)

 285            LOAD_CONST               3 (False)

 286            LOAD_CONST               3 (False)

 287            LOAD_CONST               7 ('forwarder_signature_malformed')

 284            LOAD_CONST               8 (('valid', 'verified', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 292    L5:     NOP

 293    L6:     LOAD_GLOBAL             11 (sign_forward_payload + NULL)

 294            LOAD_FAST_BORROW_LOAD_FAST_BORROW 80 (secret_clean, sender)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (subject, body)

 293            CALL                     4
                STORE_FAST               7 (expected)

 307    L7:     LOAD_GLOBAL              9 (_looks_like_well_formed_sig + NULL)
                LOAD_FAST                7 (expected)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L8)
                NOT_TAKEN

 311            LOAD_GLOBAL              7 (_envelope + NULL)

 312            LOAD_CONST               3 (False)

 313            LOAD_CONST               3 (False)

 314            LOAD_CONST              10 ('forwarder_signature_compute_failed')

 311            LOAD_CONST               8 (('valid', 'verified', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 317    L8:     NOP

 318    L9:     LOAD_GLOBAL             22 (hmac)
                LOAD_ATTR               24 (compare_digest)
                PUSH_NULL

 319            LOAD_FAST                7 (expected)
                LOAD_ATTR               27 (encode + NULL|self)
                LOAD_CONST              12 ('utf-8')
                LOAD_CONST              13 ('replace')
                LOAD_CONST              14 (('errors',))
                CALL_KW                  2

 320            LOAD_FAST                6 (provided_clean)
                LOAD_ATTR               27 (encode + NULL|self)
                LOAD_CONST              12 ('utf-8')
                LOAD_CONST              13 ('replace')
                LOAD_CONST              14 (('errors',))
                CALL_KW                  2

 318            CALL                     2
                STORE_FAST               9 (match)

 333   L10:     LOAD_FAST                9 (match)
                TO_BOOL
                POP_JUMP_IF_FALSE       14 (to L11)
                NOT_TAKEN

 334            LOAD_GLOBAL              7 (_envelope + NULL)
                LOAD_CONST               2 (True)
                LOAD_CONST               2 (True)
                LOAD_CONST              16 (('valid', 'verified'))
                CALL_KW                  2
                RETURN_VALUE

 335   L11:     LOAD_GLOBAL              7 (_envelope + NULL)

 336            LOAD_CONST               3 (False)

 337            LOAD_CONST               3 (False)

 338            LOAD_CONST              17 ('forwarder_signature_invalid')

 335            LOAD_CONST               8 (('valid', 'verified', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 296            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       68 (to L17)
                NOT_TAKEN
                STORE_FAST               8 (e)

 297   L13:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 298            LOAD_CONST               9 ('verify_forwarder_signature compute error type=')

 299            LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE

 298            BUILD_STRING             2

 297            CALL                     1
                POP_TOP

 301            LOAD_GLOBAL              7 (_envelope + NULL)

 302            LOAD_CONST               3 (False)

 303            LOAD_CONST               3 (False)

 304            LOAD_CONST              10 ('forwarder_signature_compute_failed')

 301            LOAD_CONST               8 (('valid', 'verified', 'error_code'))
                CALL_KW                  3
       L14:     SWAP                     2
       L15:     POP_EXCEPT
                LOAD_CONST              11 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RETURN_VALUE

  --   L16:     LOAD_CONST              11 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 296   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L19:     PUSH_EXC_INFO

 322            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       68 (to L24)
                NOT_TAKEN
                STORE_FAST               8 (e)

 323   L20:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 324            LOAD_CONST              15 ('verify_forwarder_signature compare error type=')

 325            LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE

 324            BUILD_STRING             2

 323            CALL                     1
                POP_TOP

 327            LOAD_GLOBAL              7 (_envelope + NULL)

 328            LOAD_CONST               3 (False)

 329            LOAD_CONST               3 (False)

 330            LOAD_CONST              10 ('forwarder_signature_compute_failed')

 327            LOAD_CONST               8 (('valid', 'verified', 'error_code'))
                CALL_KW                  3
       L21:     SWAP                     2
       L22:     POP_EXCEPT
                LOAD_CONST              11 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RETURN_VALUE

  --   L23:     LOAD_CONST              11 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 322   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L6 to L7 -> L12 [0]
  L9 to L10 -> L19 [0]
  L12 to L13 -> L18 [1] lasti
  L13 to L14 -> L16 [1] lasti
  L14 to L15 -> L18 [1] lasti
  L16 to L18 -> L18 [1] lasti
  L19 to L20 -> L25 [1] lasti
  L20 to L21 -> L23 [1] lasti
  L21 to L22 -> L25 [1] lasti
  L23 to L25 -> L25 [1] lasti
```
