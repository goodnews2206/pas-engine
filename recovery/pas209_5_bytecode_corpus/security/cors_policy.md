# security/cors_policy

- **pyc:** `app\services\security\__pycache__\cors_policy.cpython-314.pyc`
- **expected source path (absent):** `app\services\security/cors_policy.py`
- **co_filename (from bytecode):** `app/services/security/cors_policy.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** security

## Module docstring

```
PAS-SECURITY-01 — CORS policy validators (additive).

Read-only validators that classify a CORS posture against the
PAS defensive doctrine:

* **Wildcard `"*"` is allowed only in `development`.** In any
  other environment (staging / pilot / production) wildcard
  origins MUST be rejected.
* **Origins must be env/config-bound** — not hard-coded source
  literals.
* **Local origins (localhost / 127.0.0.1 / file://) must NOT
  be present in production-tier allow-lists.**
* **NEVER raises.** All helpers return structural verdicts.

The helpers here do NOT mutate the FastAPI middleware. They
classify a candidate config so that:

  1. ``app/main.py`` can decide whether to fail-fast in
     non-dev environments (a future hardening step).
  2. The PAS-SECURITY-01 readiness gate can verify that the
     repo's CORS configuration matches doctrine.

Public surface:

  * ``ALLOWED_ENVIRONMENT_TIERS``                  — closed enum.
  * ``LOCAL_ORIGIN_FORBIDDEN_TOKENS``              — closed allow-list.
  * ``classify_cors_posture(origins, environment)`` — verdict envelope.
  * ``is_wildcard_origin(origin)``                 — bool.
  * ``is_local_origin(origin)``                    — bool.
  * ``audit_cors_config(origins, environment)``    — diagnostic envelope.
```

## Imports

`Any`, `Dict`, `Iterable`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `logging`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_normalise_origins`, `_safe_envelope`, `audit_cors_config`, `classify_cors_posture`, `is_local_origin`, `is_wildcard_origin`

## Env-key candidates

`ALLOWED_ENVIRONMENT_TIERS`, `LOCAL_ORIGIN_FORBIDDEN_TOKENS`

## String constants (redacted where noted)

- '\nPAS-SECURITY-01 — CORS policy validators (additive).\n\nRead-only validators that classify a CORS posture against the\nPAS defensive doctrine:\n\n* **Wildcard `"*"` is allowed only in `development`.** In any\n  other environment (staging / pilot / production) wildcard\n  origins MUST be rejected.\n* **Origins must be env/config-bound** — not hard-coded source\n  literals.\n* **Local origins (localhost / 127.0.0.1 / file://) must NOT\n  be present in production-tier allow-lists.**\n* **NEVER raises.** All helpers return structural verdicts.\n\nThe helpers here do NOT mutate the FastAPI middleware. They\nclassify a candidate config so that:\n\n  1. ``app/main.py`` can decide whether to fail-fast in\n     non-dev environments (a future hardening step).\n  2. The PAS-SECURITY-01 readiness gate can verify that the\n     repo\'s CORS configuration matches doctrine.\n\nPublic surface:\n\n  * ``ALLOWED_ENVIRONMENT_TIERS``                  — closed enum.\n  * ``LOCAL_ORIGIN_FORBIDDEN_TOKENS``              — closed allow-list.\n  * ``classify_cors_posture(origins, environment)`` — verdict envelope.\n  * ``is_wildcard_origin(origin)``                 — bool.\n  * ``is_local_origin(origin)``                    — bool.\n  * ``audit_cors_config(origins, environment)``    — diagnostic envelope.\n'
- 'pas.security.cors_policy'
- 'Tuple[str, ...]'
- 'ALLOWED_ENVIRONMENT_TIERS'
- 'LOCAL_ORIGIN_FORBIDDEN_TOKENS'
- 'warn'
- 'fail'
- 'warnings'
- 'error_code'
- 'wildcard_present'
- 'local_origins_in_prod'
- 'origin'
- 'Any'
- 'return'
- 'bool'
- 'Returns True for wildcard / blank origin entries. NEVER\nraises.'
- 'Returns True for local/dev-only origins. NEVER raises.'
- 'origins'
- 'List[str]'
- 'verdict'
- 'str'
- 'environment'
- 'Optional[str]'
- 'Optional[List[str]]'
- 'Dict[str, Any]'
- 'Classify a CORS posture. NEVER raises.\n\nReturns:\n  * ``verdict="fail"`` — wildcard `"*"` in a non-dev\n    environment, or local origin in a non-dev environment.\n  * ``verdict="warn"`` — local origin in any environment\n    without enough context to reject; empty origin list in\n    production-tier (which would block all browsers).\n  * ``verdict="ok"`` — otherwise.\n'
- 'wildcard_origin_in_production'
- 'local_origin_in_production'
- 'empty_origin_list_in_production'
- 'development'
- 'unknown_environment'
- 'classify_cors_posture error type='
- 'unexpected:'
- 'Operator-facing diagnostic envelope. Same verdict as\n``classify_cors_posture`` plus a structural summary.'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS-SECURITY-01 — CORS policy validators (additive).\n\nRead-only validators that classify a CORS posture against the\nPAS defensive doctrine:\n\n* **Wildcard `"*"` is allowed only in `development`.** In any\n  other environment (staging / pilot / production) wildcard\n  origins MUST be rejected.\n* **Origins must be env/config-bound** — not hard-coded source\n  literals.\n* **Local origins (localhost / 127.0.0.1 / file://) must NOT\n  be present in production-tier allow-lists.**\n* **NEVER raises.** All helpers return structural verdicts.\n\nThe helpers here do NOT mutate the FastAPI middleware. They\nclassify a candidate config so that:\n\n  1. ``app/main.py`` can decide whether to fail-fast in\n     non-dev environments (a future hardening step).\n  2. The PAS-SECURITY-01 readiness gate can verify that the\n     repo\'s CORS configuration matches doctrine.\n\nPublic surface:\n\n  * ``ALLOWED_ENVIRONMENT_TIERS``                  — closed enum.\n  * ``LOCAL_ORIGIN_FORBIDDEN_TOKENS``              — closed allow-list.\n  * ``classify_cors_posture(origins, environment)`` — verdict envelope.\n  * ``is_wildcard_origin(origin)``                 — bool.\n  * ``is_local_origin(origin)``                    — bool.\n  * ``audit_cors_config(origins, environment)``    — diagnostic envelope.\n')
               STORE_NAME               1 (__doc__)

  34           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  36           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  37           LOAD_SMALL_INT           0
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

  40           LOAD_NAME                4 (logging)
               LOAD_ATTR               24 (getLogger)
               PUSH_NULL
               LOAD_CONST               4 ('pas.security.cors_policy')
               CALL                     1
               STORE_NAME              13 (logger)

  46           LOAD_CONST              28 (('development', 'staging', 'pilot', 'production'))
               STORE_NAME              14 (ALLOWED_ENVIRONMENT_TIERS)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               15 (__annotations__)
               LOAD_CONST               6 ('ALLOWED_ENVIRONMENT_TIERS')
               STORE_SUBSCR

  56           LOAD_CONST              29 (('localhost', '127.0.0.1', '0.0.0.0', '::1', 'file://', '.local'))
               STORE_NAME              16 (LOCAL_ORIGIN_FORBIDDEN_TOKENS)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               15 (__annotations__)
               LOAD_CONST               7 ('LOCAL_ORIGIN_FORBIDDEN_TOKENS')
               STORE_SUBSCR

  67           LOAD_CONST               8 ('ok')
               STORE_NAME              17 (VERDICT_OK)

  68           LOAD_CONST               9 ('warn')
               STORE_NAME              18 (VERDICT_WARN)

  69           LOAD_CONST              10 ('fail')
               STORE_NAME              19 (VERDICT_FAIL)

  72           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA1E30, file "app/services/security/cors_policy.py", line 72>)
               MAKE_FUNCTION
               LOAD_CONST              12 (<code object is_wildcard_origin at 0x0000018C1802CC10, file "app/services/security/cors_policy.py", line 72>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              20 (is_wildcard_origin)

  81           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA21F0, file "app/services/security/cors_policy.py", line 81>)
               MAKE_FUNCTION
               LOAD_CONST              14 (<code object is_local_origin at 0x0000018C17F96420, file "app/services/security/cors_policy.py", line 81>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              21 (is_local_origin)

  92           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA30F0, file "app/services/security/cors_policy.py", line 92>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _normalise_origins at 0x0000018C17F786F0, file "app/services/security/cors_policy.py", line 92>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              22 (_normalise_origins)

 106           LOAD_CONST              17 ('warnings')

 111           LOAD_CONST               2 (None)

 106           LOAD_CONST              18 ('error_code')

 112           LOAD_CONST               2 (None)

 106           LOAD_CONST              19 ('wildcard_present')

 113           LOAD_CONST              20 (False)

 106           LOAD_CONST              21 ('local_origins_in_prod')

 114           LOAD_CONST              20 (False)

 106           BUILD_MAP                4
               LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FBFEE0, file "app/services/security/cors_policy.py", line 106>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _safe_envelope at 0x0000018C17FE1530, file "app/services/security/cors_policy.py", line 106>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              23 (_safe_envelope)

 127           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C18025C30, file "app/services/security/cors_policy.py", line 127>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object classify_cors_posture at 0x0000018C17EA6230, file "app/services/security/cors_policy.py", line 127>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              24 (classify_cors_posture)

 217           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C18026430, file "app/services/security/cors_policy.py", line 217>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object audit_cors_config at 0x0000018C17FA2E20, file "app/services/security/cors_policy.py", line 217>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              25 (audit_cors_config)

 227           BUILD_LIST               0
               LOAD_CONST              30 (('ALLOWED_ENVIRONMENT_TIERS', 'LOCAL_ORIGIN_FORBIDDEN_TOKENS', 'VERDICT_OK', 'VERDICT_WARN', 'VERDICT_FAIL', 'is_wildcard_origin', 'is_local_origin', 'classify_cors_posture', 'audit_cors_config'))
               LIST_EXTEND              1
               STORE_NAME              26 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "app/services/security/cors_policy.py", line 72>:
 72           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('origin')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object is_wildcard_origin at 0x0000018C1802CC10, file "app/services/security/cors_policy.py", line 72>:
 72           RESUME                   0

 75           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (origin)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 76           LOAD_CONST               1 (False)
              RETURN_VALUE

 77   L1:     LOAD_FAST_BORROW         0 (origin)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

 78           LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               2 ('*')
              COMPARE_OP              72 (==)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app/services/security/cors_policy.py", line 81>:
 81           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('origin')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object is_local_origin at 0x0000018C17F96420, file "app/services/security/cors_policy.py", line 81>:
 81           RESUME                   0

 83           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (origin)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 84           LOAD_CONST               1 (False)
              RETURN_VALUE

 85   L1:     LOAD_FAST_BORROW         0 (origin)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR                7 (lower + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

 86           LOAD_GLOBAL              8 (LOCAL_ORIGIN_FORBIDDEN_TOKENS)
              GET_ITER
      L2:     FOR_ITER                12 (to L4)
              STORE_FAST               2 (tok)

 87           LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (tok, s)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

 88   L3:     POP_TOP
              LOAD_CONST               2 (True)
              RETURN_VALUE

 86   L4:     END_FOR
              POP_ITER

 89           LOAD_CONST               1 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "app/services/security/cors_policy.py", line 92>:
 92           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('origins')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _normalise_origins at 0x0000018C17F786F0, file "app/services/security/cors_policy.py", line 92>:
  92            RESUME                   0

  93            LOAD_FAST_BORROW         0 (origins)
                POP_JUMP_IF_NOT_NONE     3 (to L1)
                NOT_TAKEN

  94            BUILD_LIST               0
                RETURN_VALUE

  95    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (origins)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       71 (to L8)
                NOT_TAKEN

  96            LOAD_FAST_BORROW         0 (origins)
                LOAD_ATTR                5 (split + NULL|self)
                LOAD_CONST               1 (',')
                CALL                     1
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (o)
                SWAP                     2
        L2:     BUILD_LIST               0
                SWAP                     2
        L3:     FOR_ITER                42 (to L6)
                STORE_FAST_LOAD_FAST    17 (o, o)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                TO_BOOL
        L4:     POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           26 (to L3)
        L5:     LOAD_FAST_BORROW         1 (o)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                LIST_APPEND              2
                JUMP_BACKWARD           44 (to L3)
        L6:     END_FOR
                POP_ITER
        L7:     SWAP                     2
                STORE_FAST               1 (o)
                RETURN_VALUE

  97    L8:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (origins)
                LOAD_GLOBAL              8 (list)
                LOAD_GLOBAL             10 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       93 (to L13)
                NOT_TAKEN

  98            BUILD_LIST               0
                STORE_FAST               2 (out)

  99            LOAD_FAST_BORROW         0 (origins)
                GET_ITER
        L9:     FOR_ITER                82 (to L12)
                STORE_FAST               1 (o)

 100            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (o)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L9)
       L10:     LOAD_FAST_BORROW         1 (o)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                JUMP_BACKWARD           51 (to L9)

 101   L11:     LOAD_FAST_BORROW         2 (out)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_FAST_BORROW         1 (o)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           84 (to L9)

  99   L12:     END_FOR
                POP_ITER

 102            LOAD_FAST_BORROW         2 (out)
                RETURN_VALUE

 103   L13:     BUILD_LIST               0
                RETURN_VALUE

  --   L14:     SWAP                     2
                POP_TOP

  96            SWAP                     2
                STORE_FAST               1 (o)
                RERAISE                  0
ExceptionTable:
  L2 to L4 -> L14 [2]
  L5 to L7 -> L14 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FBFEE0, file "app/services/security/cors_policy.py", line 106>:
106           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('verdict')

108           LOAD_CONST               2 ('str')

106           LOAD_CONST               3 ('environment')

109           LOAD_CONST               4 ('Optional[str]')

106           LOAD_CONST               5 ('origins')

110           LOAD_CONST               6 ('List[str]')

106           LOAD_CONST               7 ('warnings')

111           LOAD_CONST               8 ('Optional[List[str]]')

106           LOAD_CONST               9 ('error_code')

112           LOAD_CONST               4 ('Optional[str]')

106           LOAD_CONST              10 ('wildcard_present')

113           LOAD_CONST              11 ('bool')

106           LOAD_CONST              12 ('local_origins_in_prod')

114           LOAD_CONST              11 ('bool')

106           LOAD_CONST              13 ('return')

115           LOAD_CONST              14 ('Dict[str, Any]')

106           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C17FE1530, file "app/services/security/cors_policy.py", line 106>:
106           RESUME                   0

117           LOAD_CONST               0 ('verdict')
              LOAD_FAST                0 (verdict)

118           LOAD_CONST               1 ('environment')
              LOAD_FAST                1 (environment)

119           LOAD_CONST               2 ('origins')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST_BORROW         2 (origins)
              CALL                     1

120           LOAD_CONST               3 ('wildcard_present')
              LOAD_GLOBAL              3 (bool + NULL)
              LOAD_FAST_BORROW         5 (wildcard_present)
              CALL                     1

121           LOAD_CONST               4 ('local_origins_in_prod')
              LOAD_GLOBAL              3 (bool + NULL)
              LOAD_FAST_BORROW         6 (local_origins_in_prod)
              CALL                     1

122           LOAD_CONST               5 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                3 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

123           LOAD_CONST               6 ('error_code')
              LOAD_FAST_BORROW         4 (error_code)

116           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app/services/security/cors_policy.py", line 127>:
127           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('origins')

129           LOAD_CONST               2 ('Any')

127           LOAD_CONST               3 ('environment')

130           LOAD_CONST               2 ('Any')

127           LOAD_CONST               4 ('return')

131           LOAD_CONST               5 ('Dict[str, Any]')

127           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object classify_cors_posture at 0x0000018C17EA6230, file "app/services/security/cors_policy.py", line 127>:
 127            RESUME                   0

 142            NOP

 143    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (environment)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       31 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (environment)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR                7 (lower + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               1 (None)
        L3:     STORE_FAST               2 (env)

 144            LOAD_FAST_BORROW         2 (env)
                LOAD_GLOBAL              8 (ALLOWED_ENVIRONMENT_TIERS)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN

 145            LOAD_CONST               1 (None)
                STORE_FAST               2 (env)

 146    L4:     LOAD_GLOBAL             11 (_normalise_origins + NULL)
                LOAD_FAST_BORROW         0 (origins)
                CALL                     1
                STORE_FAST               3 (items)

 147            LOAD_GLOBAL             12 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       28 (to L9)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 (<code object <genexpr> at 0x0000018C1812C8B0, file "app/services/security/cors_policy.py", line 147>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         3 (items)
                GET_ITER
                CALL                     0
        L5:     FOR_ITER                12 (to L8)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L6:     NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)
        L7:     POP_ITER
                LOAD_CONST               3 (True)
                JUMP_FORWARD            17 (to L10)
        L8:     END_FOR
                POP_ITER
                LOAD_CONST               4 (False)
                JUMP_FORWARD            13 (to L10)
        L9:     PUSH_NULL
                LOAD_CONST               2 (<code object <genexpr> at 0x0000018C1812C8B0, file "app/services/security/cors_policy.py", line 147>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         3 (items)
                GET_ITER
                CALL                     0
                CALL                     1
       L10:     STORE_FAST               4 (wildcard)

 148            LOAD_GLOBAL             12 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       28 (to L17)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                LOAD_CONST               5 (<code object <genexpr> at 0x0000018C1812C9C0, file "app/services/security/cors_policy.py", line 148>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         3 (items)
                GET_ITER
                CALL                     0
       L13:     FOR_ITER                12 (to L16)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
       L14:     NOT_TAKEN
                JUMP_BACKWARD           11 (to L13)
       L15:     POP_ITER
                LOAD_CONST               3 (True)
                JUMP_FORWARD            17 (to L18)
       L16:     END_FOR
                POP_ITER
                LOAD_CONST               4 (False)
                JUMP_FORWARD            13 (to L18)
       L17:     PUSH_NULL
                LOAD_CONST               5 (<code object <genexpr> at 0x0000018C1812C9C0, file "app/services/security/cors_policy.py", line 148>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         3 (items)
                GET_ITER
                CALL                     0
                CALL                     1
       L18:     STORE_FAST               5 (locals_present)

 149            BUILD_LIST               0
                STORE_FAST               6 (warnings)

 151            LOAD_FAST_BORROW         2 (env)
                LOAD_CONST              17 (('staging', 'pilot', 'production'))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE      170 (to L37)
                NOT_TAKEN

 152            BUILD_LIST               0
                STORE_FAST               7 (bad)

 153            LOAD_FAST_BORROW         4 (wildcard)
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L21)
       L19:     NOT_TAKEN

 154   L20:     LOAD_FAST_BORROW         7 (bad)
                LOAD_ATTR               15 (append + NULL|self)
                LOAD_CONST               6 ('wildcard_origin_in_production')
                CALL                     1
                POP_TOP

 155   L21:     LOAD_FAST_BORROW         5 (locals_present)
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L24)
       L22:     NOT_TAKEN

 156   L23:     LOAD_FAST_BORROW         7 (bad)
                LOAD_ATTR               15 (append + NULL|self)
                LOAD_CONST               7 ('local_origin_in_production')
                CALL                     1
                POP_TOP

 157   L24:     LOAD_FAST_BORROW         3 (items)
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L27)
       L25:     NOT_TAKEN

 158   L26:     LOAD_FAST_BORROW         6 (warnings)
                LOAD_ATTR               15 (append + NULL|self)
                LOAD_CONST               8 ('empty_origin_list_in_production')
                CALL                     1
                POP_TOP

 159   L27:     LOAD_FAST_BORROW         7 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       36 (to L31)
       L28:     NOT_TAKEN

 160   L29:     LOAD_GLOBAL             17 (_safe_envelope + NULL)

 161            LOAD_GLOBAL             18 (VERDICT_FAIL)

 162            LOAD_FAST_BORROW         2 (env)

 163            LOAD_FAST_BORROW         3 (items)

 164            LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (warnings, bad)
                BINARY_OP                0 (+)

 165            LOAD_FAST_BORROW         7 (bad)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])

 166            LOAD_FAST_BORROW         4 (wildcard)

 167            LOAD_FAST_BORROW         5 (locals_present)

 160            LOAD_CONST               9 (('verdict', 'environment', 'origins', 'warnings', 'error_code', 'wildcard_present', 'local_origins_in_prod'))
                CALL_KW                  7
       L30:     RETURN_VALUE

 169   L31:     LOAD_FAST_BORROW         6 (warnings)
                TO_BOOL
                POP_JUMP_IF_FALSE       22 (to L35)
       L32:     NOT_TAKEN

 170   L33:     LOAD_GLOBAL             17 (_safe_envelope + NULL)

 171            LOAD_GLOBAL             20 (VERDICT_WARN)

 172            LOAD_FAST_BORROW         2 (env)

 173            LOAD_FAST_BORROW         3 (items)

 174            LOAD_FAST_BORROW         6 (warnings)

 175            LOAD_FAST_BORROW         4 (wildcard)

 176            LOAD_FAST_BORROW         5 (locals_present)

 170            LOAD_CONST              10 (('verdict', 'environment', 'origins', 'warnings', 'wildcard_present', 'local_origins_in_prod'))
                CALL_KW                  6
       L34:     RETURN_VALUE

 178   L35:     LOAD_GLOBAL             17 (_safe_envelope + NULL)

 179            LOAD_GLOBAL             22 (VERDICT_OK)

 180            LOAD_FAST_BORROW         2 (env)

 181            LOAD_FAST_BORROW         3 (items)

 182            LOAD_CONST               4 (False)

 183            LOAD_CONST               4 (False)

 178            LOAD_CONST              11 (('verdict', 'environment', 'origins', 'wildcard_present', 'local_origins_in_prod'))
                CALL_KW                  5
       L36:     RETURN_VALUE

 186   L37:     LOAD_FAST_BORROW         2 (env)
                LOAD_CONST              12 ('development')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       21 (to L39)
                NOT_TAKEN

 187            LOAD_GLOBAL             17 (_safe_envelope + NULL)

 188            LOAD_GLOBAL             22 (VERDICT_OK)

 189            LOAD_FAST_BORROW         2 (env)

 190            LOAD_FAST_BORROW         3 (items)

 191            LOAD_FAST_BORROW         4 (wildcard)

 192            LOAD_CONST               4 (False)

 187            LOAD_CONST              11 (('verdict', 'environment', 'origins', 'wildcard_present', 'local_origins_in_prod'))
                CALL_KW                  5
       L38:     RETURN_VALUE

 195   L39:     LOAD_GLOBAL             17 (_safe_envelope + NULL)

 196            LOAD_GLOBAL             20 (VERDICT_WARN)

 197            LOAD_FAST_BORROW         2 (env)

 198            LOAD_FAST_BORROW         3 (items)

 199            LOAD_CONST              13 ('unknown_environment')
                BUILD_LIST               1

 200            LOAD_CONST              13 ('unknown_environment')

 201            LOAD_FAST_BORROW         4 (wildcard)

 202            LOAD_FAST_BORROW         5 (locals_present)

 195            LOAD_CONST               9 (('verdict', 'environment', 'origins', 'warnings', 'error_code', 'wildcard_present', 'local_origins_in_prod'))
                CALL_KW                  7
       L40:     RETURN_VALUE

  --   L41:     PUSH_EXC_INFO

 204            LOAD_GLOBAL             24 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      119 (to L46)
                NOT_TAKEN
                STORE_FAST               8 (e)

 205   L42:     LOAD_GLOBAL             26 (logger)
                LOAD_ATTR               29 (warning + NULL|self)

 206            LOAD_CONST              14 ('classify_cors_posture error type=')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 205            CALL                     1
                POP_TOP

 208            LOAD_GLOBAL             17 (_safe_envelope + NULL)

 209            LOAD_GLOBAL             18 (VERDICT_FAIL)

 210            LOAD_CONST               1 (None)

 211            BUILD_LIST               0

 212            LOAD_CONST              15 ('unexpected:')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 213            LOAD_CONST              15 ('unexpected:')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 208            LOAD_CONST              16 (('verdict', 'environment', 'origins', 'warnings', 'error_code'))
                CALL_KW                  5
       L43:     SWAP                     2
       L44:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RETURN_VALUE

  --   L45:     LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 204   L46:     RERAISE                  0

  --   L47:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L6 -> L41 [0]
  L7 to L11 -> L41 [0]
  L12 to L14 -> L41 [0]
  L15 to L19 -> L41 [0]
  L20 to L22 -> L41 [0]
  L23 to L25 -> L41 [0]
  L26 to L28 -> L41 [0]
  L29 to L30 -> L41 [0]
  L31 to L32 -> L41 [0]
  L33 to L34 -> L41 [0]
  L35 to L36 -> L41 [0]
  L37 to L38 -> L41 [0]
  L39 to L40 -> L41 [0]
  L41 to L42 -> L47 [1] lasti
  L42 to L43 -> L45 [1] lasti
  L43 to L44 -> L47 [1] lasti
  L45 to L47 -> L47 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C1812C8B0, file "app/services/security/cors_policy.py", line 147>:
 147           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (o)
               LOAD_GLOBAL              1 (is_wildcard_origin + NULL)
               LOAD_FAST_BORROW         1 (o)
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           18 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C1812C9C0, file "app/services/security/cors_policy.py", line 148>:
 148           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (o)
               LOAD_GLOBAL              1 (is_local_origin + NULL)
               LOAD_FAST_BORROW         1 (o)
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           18 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "app/services/security/cors_policy.py", line 217>:
217           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('origins')

219           LOAD_CONST               2 ('Any')

217           LOAD_CONST               3 ('environment')

220           LOAD_CONST               2 ('Any')

217           LOAD_CONST               4 ('return')

221           LOAD_CONST               5 ('Dict[str, Any]')

217           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object audit_cors_config at 0x0000018C17FA2E20, file "app/services/security/cors_policy.py", line 217>:
217           RESUME                   0

224           LOAD_GLOBAL              1 (classify_cors_posture + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (origins, environment)
              LOAD_CONST               1 (('origins', 'environment'))
              CALL_KW                  2
              RETURN_VALUE
```
