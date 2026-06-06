# security/https_enforcement

- **pyc:** `app\services\security\__pycache__\https_enforcement.cpython-314.pyc`
- **expected source path (absent):** `app\services\security/https_enforcement.py`
- **co_filename (from bytecode):** `app/services/security/https_enforcement.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** security

## Module docstring

```
PAS-SECURITY-04 — App-layer HTTPS enforcement helper.

Defensive helper that classifies an inbound request as
``secure`` / ``insecure`` based on the trusted-proxy
``X-Forwarded-Proto`` header, and emits a structural verdict
the middleware layer can use to reject HTTP-over-proxy
requests in production.

Doctrine:

* **Trusted proxy posture.** PAS deployments sit behind a
  reverse-proxy / WAF / CDN that terminates TLS and sets
  ``X-Forwarded-Proto: https`` for HTTPS-terminated requests.
  When the header is ``http``, the request was proxied over
  plaintext — reject.
* **Production-only.** Local development (no proxy, no
  header) MUST work. The helper returns ``allow`` when the
  environment is `development` regardless of header state.
* **Header-absent fallback.** When the header is missing
  (direct connection or proxy doesn't set it), the helper
  ALLOWS the request — refusing would break operators that
  haven't configured the proxy yet. The WAF baseline doc
  ([docs/pas_waf_boundary_security_baseline.md](../../../docs/pas_waf_boundary_security_baseline.md))
  documents the operator's responsibility to configure the
  header.
* **NEVER raises.** All helpers return structural envelopes.
* **No raw headers echoed.** The verdict carries only the
  closed reason token.

Public surface:

  * ``ALLOWED_ENVIRONMENT_TIERS``               — closed enum.
  * ``PRODUCTION_TIER_ENVIRONMENTS``            — closed set.
  * ``https_enforcement_enabled(env)``          — bool.
  * ``should_reject_insecure_request(forwarded_proto, environment)``
                                                 — bool.
  * ``insecure_request_public_error()``         — structural 400 envelope.
```

## Imports

`Any`, `Dict`, `Optional`, `Tuple`, `__future__`, `annotations`, `logging`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_normalise_env`, `_normalise_proto`, `https_enforcement_enabled`, `insecure_request_public_error`, `should_reject_insecure_request`

## Env-key candidates

`ALLOWED_ENVIRONMENT_TIERS`, `PRODUCTION_TIER_ENVIRONMENTS`

## String constants (redacted where noted)

- "\nPAS-SECURITY-04 — App-layer HTTPS enforcement helper.\n\nDefensive helper that classifies an inbound request as\n``secure`` / ``insecure`` based on the trusted-proxy\n``X-Forwarded-Proto`` header, and emits a structural verdict\nthe middleware layer can use to reject HTTP-over-proxy\nrequests in production.\n\nDoctrine:\n\n* **Trusted proxy posture.** PAS deployments sit behind a\n  reverse-proxy / WAF / CDN that terminates TLS and sets\n  ``X-Forwarded-Proto: https`` for HTTPS-terminated requests.\n  When the header is ``http``, the request was proxied over\n  plaintext — reject.\n* **Production-only.** Local development (no proxy, no\n  header) MUST work. The helper returns ``allow`` when the\n  environment is `development` regardless of header state.\n* **Header-absent fallback.** When the header is missing\n  (direct connection or proxy doesn't set it), the helper\n  ALLOWS the request — refusing would break operators that\n  haven't configured the proxy yet. The WAF baseline doc\n  ([docs/pas_waf_boundary_security_baseline.md](../../../docs/pas_waf_boundary_security_baseline.md))\n  documents the operator's responsibility to configure the\n  header.\n* **NEVER raises.** All helpers return structural envelopes.\n* **No raw headers echoed.** The verdict carries only the\n  closed reason token.\n\nPublic surface:\n\n  * ``ALLOWED_ENVIRONMENT_TIERS``               — closed enum.\n  * ``PRODUCTION_TIER_ENVIRONMENTS``            — closed set.\n  * ``https_enforcement_enabled(env)``          — bool.\n  * ``should_reject_insecure_request(forwarded_proto, environment)``\n                                                 — bool.\n  * ``insecure_request_public_error()``         — structural 400 envelope.\n"
- 'pas.security.https_enforcement'
- 'Tuple[str, ...]'
- 'ALLOWED_ENVIRONMENT_TIERS'
- 'PRODUCTION_TIER_ENVIRONMENTS'
- 'development_environment_allowed'
- 'x_forwarded_proto_absent_allowed'
- 'x_forwarded_proto_https'
- 'x_forwarded_proto_http_in_production'
- 'value'
- 'Any'
- 'return'
- 'Optional[str]'
- 'environment'
- 'bool'
- 'Returns True if the environment is production-tier.\nNEVER raises.'
- 'forwarded_proto'
- 'Dict[str, Any]'
- 'Decide whether to reject a request. NEVER raises.\n\nReturns a closed envelope:\n    {\n      "reject": bool,\n      "reason": "<closed token>",\n      "environment": "<tier>" | None,\n    }\n'
- 'development'
- 'reject'
- 'reason'
- 'https'
- 'should_reject_insecure_request error type='
- 'unexpected:'
- 'Return the closed-shape 400-style public envelope for\nan HTTPS-rejected request. NEVER carries the raw headers\n/ origin / user-agent.'
- 'status'
- 'failed'
- 'error_code'
- 'insecure_request_rejected'
- 'warnings'
- 'https_enforcement_active'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ("\nPAS-SECURITY-04 — App-layer HTTPS enforcement helper.\n\nDefensive helper that classifies an inbound request as\n``secure`` / ``insecure`` based on the trusted-proxy\n``X-Forwarded-Proto`` header, and emits a structural verdict\nthe middleware layer can use to reject HTTP-over-proxy\nrequests in production.\n\nDoctrine:\n\n* **Trusted proxy posture.** PAS deployments sit behind a\n  reverse-proxy / WAF / CDN that terminates TLS and sets\n  ``X-Forwarded-Proto: https`` for HTTPS-terminated requests.\n  When the header is ``http``, the request was proxied over\n  plaintext — reject.\n* **Production-only.** Local development (no proxy, no\n  header) MUST work. The helper returns ``allow`` when the\n  environment is `development` regardless of header state.\n* **Header-absent fallback.** When the header is missing\n  (direct connection or proxy doesn't set it), the helper\n  ALLOWS the request — refusing would break operators that\n  haven't configured the proxy yet. The WAF baseline doc\n  ([docs/pas_waf_boundary_security_baseline.md](../../../docs/pas_waf_boundary_security_baseline.md))\n  documents the operator's responsibility to configure the\n  header.\n* **NEVER raises.** All helpers return structural envelopes.\n* **No raw headers echoed.** The verdict carries only the\n  closed reason token.\n\nPublic surface:\n\n  * ``ALLOWED_ENVIRONMENT_TIERS``               — closed enum.\n  * ``PRODUCTION_TIER_ENVIRONMENTS``            — closed set.\n  * ``https_enforcement_enabled(env)``          — bool.\n  * ``should_reject_insecure_request(forwarded_proto, environment)``\n                                                 — bool.\n  * ``insecure_request_public_error()``         — structural 400 envelope.\n")
               STORE_NAME               1 (__doc__)

  41           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  43           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  44           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('Any', 'Dict', 'Optional', 'Tuple'))
               IMPORT_NAME              5 (typing)
               IMPORT_FROM              6 (Any)
               STORE_NAME               6 (Any)
               IMPORT_FROM              7 (Dict)
               STORE_NAME               7 (Dict)
               IMPORT_FROM              8 (Optional)
               STORE_NAME               8 (Optional)
               IMPORT_FROM              9 (Tuple)
               STORE_NAME               9 (Tuple)
               POP_TOP

  47           LOAD_NAME                4 (logging)
               LOAD_ATTR               20 (getLogger)
               PUSH_NULL
               LOAD_CONST               4 ('pas.security.https_enforcement')
               CALL                     1
               STORE_NAME              11 (logger)

  51           LOAD_CONST              22 (('development', 'staging', 'pilot', 'production'))
               STORE_NAME              12 (ALLOWED_ENVIRONMENT_TIERS)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               13 (__annotations__)
               LOAD_CONST               6 ('ALLOWED_ENVIRONMENT_TIERS')
               STORE_SUBSCR

  60           LOAD_CONST              23 (('staging', 'pilot', 'production'))
               STORE_NAME              14 (PRODUCTION_TIER_ENVIRONMENTS)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               13 (__annotations__)
               LOAD_CONST               7 ('PRODUCTION_TIER_ENVIRONMENTS')
               STORE_SUBSCR

  68           LOAD_CONST               8 ('development_environment_allowed')
               STORE_NAME              15 (_REASON_DEV_ALLOWED)

  69           LOAD_CONST               9 ('x_forwarded_proto_absent_allowed')
               STORE_NAME              16 (_REASON_HEADER_ABSENT_ALLOWED)

  70           LOAD_CONST              10 ('x_forwarded_proto_https')
               STORE_NAME              17 (_REASON_HTTPS_OK)

  71           LOAD_CONST              11 ('x_forwarded_proto_http_in_production')
               STORE_NAME              18 (_REASON_HTTP_REJECTED)

  74           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA31E0, file "app/services/security/https_enforcement.py", line 74>)
               MAKE_FUNCTION
               LOAD_CONST              13 (<code object _normalise_env at 0x0000018C17972550, file "app/services/security/https_enforcement.py", line 74>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              19 (_normalise_env)

  83           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA3690, file "app/services/security/https_enforcement.py", line 83>)
               MAKE_FUNCTION
               LOAD_CONST              15 (<code object _normalise_proto at 0x0000018C18048E30, file "app/services/security/https_enforcement.py", line 83>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              20 (_normalise_proto)

  96           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA3E10, file "app/services/security/https_enforcement.py", line 96>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object https_enforcement_enabled at 0x0000018C18025230, file "app/services/security/https_enforcement.py", line 96>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              21 (https_enforcement_enabled)

 103           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C18025D30, file "app/services/security/https_enforcement.py", line 103>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object should_reject_insecure_request at 0x0000018C17CC2E60, file "app/services/security/https_enforcement.py", line 103>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              22 (should_reject_insecure_request)

 170           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA3A50, file "app/services/security/https_enforcement.py", line 170>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object insecure_request_public_error at 0x0000018C17FA1E30, file "app/services/security/https_enforcement.py", line 170>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              23 (insecure_request_public_error)

 181           BUILD_LIST               0
               LOAD_CONST              24 (('ALLOWED_ENVIRONMENT_TIERS', 'PRODUCTION_TIER_ENVIRONMENTS', 'https_enforcement_enabled', 'should_reject_insecure_request', 'insecure_request_public_error'))
               LIST_EXTEND              1
               STORE_NAME              24 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "app/services/security/https_enforcement.py", line 74>:
 74           RESUME                   0
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

Disassembly of <code object _normalise_env at 0x0000018C17972550, file "app/services/security/https_enforcement.py", line 74>:
 74           RESUME                   0

 75           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 76           LOAD_CONST               0 (None)
              RETURN_VALUE

 77   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR                7 (lower + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

 78           LOAD_FAST_BORROW         1 (s)
              LOAD_GLOBAL              8 (ALLOWED_ENVIRONMENT_TIERS)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

 79           LOAD_CONST               0 (None)
              RETURN_VALUE

 80   L2:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app/services/security/https_enforcement.py", line 83>:
 83           RESUME                   0
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

Disassembly of <code object _normalise_proto at 0x0000018C18048E30, file "app/services/security/https_enforcement.py", line 83>:
 83           RESUME                   0

 84           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 85           LOAD_CONST               0 (None)
              RETURN_VALUE

 86   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR                7 (lower + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

 87           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

 88           LOAD_CONST               0 (None)
              RETURN_VALUE

 92   L2:     LOAD_FAST_BORROW         1 (s)
              LOAD_ATTR                9 (split + NULL|self)
              LOAD_CONST               1 (',')
              CALL                     1
              LOAD_SMALL_INT           0
              BINARY_OP               26 ([])
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (first)

 93           LOAD_FAST                2 (first)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               0 (None)
      L3:     RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "app/services/security/https_enforcement.py", line 96>:
 96           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('environment')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object https_enforcement_enabled at 0x0000018C18025230, file "app/services/security/https_enforcement.py", line 96>:
 96           RESUME                   0

 99           LOAD_GLOBAL              1 (_normalise_env + NULL)
              LOAD_FAST_BORROW         0 (environment)
              CALL                     1
              STORE_FAST               1 (env)

100           LOAD_FAST_BORROW         1 (env)
              LOAD_GLOBAL              2 (PRODUCTION_TIER_ENVIRONMENTS)
              CONTAINS_OP              0 (in)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app/services/security/https_enforcement.py", line 103>:
103           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('forwarded_proto')

105           LOAD_CONST               2 ('Any')

103           LOAD_CONST               3 ('environment')

106           LOAD_CONST               2 ('Any')

103           LOAD_CONST               4 ('return')

107           LOAD_CONST               5 ('Dict[str, Any]')

103           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object should_reject_insecure_request at 0x0000018C17CC2E60, file "app/services/security/https_enforcement.py", line 103>:
 103            RESUME                   0

 117            NOP

 118    L1:     LOAD_GLOBAL              1 (_normalise_env + NULL)
                LOAD_FAST_BORROW         1 (environment)
                CALL                     1
                STORE_FAST               2 (env)

 120            LOAD_FAST_BORROW         2 (env)
                LOAD_CONST               1 ('development')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       13 (to L3)
                NOT_TAKEN

 122            LOAD_CONST               2 ('reject')
                LOAD_CONST               3 (False)

 123            LOAD_CONST               4 ('reason')
                LOAD_GLOBAL              2 (_REASON_DEV_ALLOWED)

 124            LOAD_CONST               5 ('environment')
                LOAD_FAST_BORROW         2 (env)

 121            BUILD_MAP                3
        L2:     RETURN_VALUE

 128    L3:     LOAD_FAST_BORROW         2 (env)
                LOAD_GLOBAL              4 (PRODUCTION_TIER_ENVIRONMENTS)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       13 (to L5)
                NOT_TAKEN

 130            LOAD_CONST               2 ('reject')
                LOAD_CONST               3 (False)

 131            LOAD_CONST               4 ('reason')
                LOAD_GLOBAL              2 (_REASON_DEV_ALLOWED)

 132            LOAD_CONST               5 ('environment')
                LOAD_FAST_BORROW         2 (env)

 129            BUILD_MAP                3
        L4:     RETURN_VALUE

 134    L5:     LOAD_GLOBAL              7 (_normalise_proto + NULL)
                LOAD_FAST_BORROW         0 (forwarded_proto)
                CALL                     1
                STORE_FAST               3 (proto)

 137            LOAD_FAST_BORROW         3 (proto)
                POP_JUMP_IF_NOT_NONE    13 (to L7)
                NOT_TAKEN

 139            LOAD_CONST               2 ('reject')
                LOAD_CONST               3 (False)

 140            LOAD_CONST               4 ('reason')
                LOAD_GLOBAL              8 (_REASON_HEADER_ABSENT_ALLOWED)

 141            LOAD_CONST               5 ('environment')
                LOAD_FAST_BORROW         2 (env)

 138            BUILD_MAP                3
        L6:     RETURN_VALUE

 144    L7:     LOAD_FAST_BORROW         3 (proto)
                LOAD_CONST               7 ('https')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       13 (to L9)
                NOT_TAKEN

 146            LOAD_CONST               2 ('reject')
                LOAD_CONST               3 (False)

 147            LOAD_CONST               4 ('reason')
                LOAD_GLOBAL             10 (_REASON_HTTPS_OK)

 148            LOAD_CONST               5 ('environment')
                LOAD_FAST_BORROW         2 (env)

 145            BUILD_MAP                3
        L8:     RETURN_VALUE

 153    L9:     LOAD_CONST               2 ('reject')
                LOAD_CONST               8 (True)

 154            LOAD_CONST               4 ('reason')
                LOAD_GLOBAL             12 (_REASON_HTTP_REJECTED)

 155            LOAD_CONST               5 ('environment')
                LOAD_FAST_BORROW         2 (env)

 152            BUILD_MAP                3
       L10:     RETURN_VALUE

  --   L11:     PUSH_EXC_INFO

 157            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       84 (to L16)
                NOT_TAKEN
                STORE_FAST               4 (e)

 158   L12:     LOAD_GLOBAL             16 (logger)
                LOAD_ATTR               19 (warning + NULL|self)

 159            LOAD_CONST               9 ('should_reject_insecure_request error type=')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 158            CALL                     1
                POP_TOP

 164            LOAD_CONST               2 ('reject')
                LOAD_CONST               3 (False)

 165            LOAD_CONST               4 ('reason')
                LOAD_CONST              10 ('unexpected:')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 166            LOAD_CONST               5 ('environment')
                LOAD_CONST               6 (None)

 163            BUILD_MAP                3
       L13:     SWAP                     2
       L14:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RETURN_VALUE

  --   L15:     LOAD_CONST               6 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 157   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L11 [0]
  L3 to L4 -> L11 [0]
  L5 to L6 -> L11 [0]
  L7 to L8 -> L11 [0]
  L9 to L10 -> L11 [0]
  L11 to L12 -> L17 [1] lasti
  L12 to L13 -> L15 [1] lasti
  L13 to L14 -> L17 [1] lasti
  L15 to L17 -> L17 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app/services/security/https_enforcement.py", line 170>:
170           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object insecure_request_public_error at 0x0000018C17FA1E30, file "app/services/security/https_enforcement.py", line 170>:
170           RESUME                   0

175           LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('failed')

176           LOAD_CONST               3 ('error_code')
              LOAD_CONST               4 ('insecure_request_rejected')

177           LOAD_CONST               5 ('warnings')
              LOAD_CONST               6 ('https_enforcement_active')
              BUILD_LIST               1

174           BUILD_MAP                3
              RETURN_VALUE
```
