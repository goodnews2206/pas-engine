# learning/guardrails

- **pyc:** `app\services\learning\__pycache__\guardrails.cpython-314.pyc`
- **expected source path (absent):** `app\services\learning/guardrails.py`
- **co_filename (from bytecode):** `app/services/learning/guardrails.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** learning

## Module docstring

```
PAS179 — Controlled learning guardrails.

Closed validators used by the recommendation engine and the
simulation harness to make sure no PII / secret / freeform
content / live-mutation request slips through.

Doctrine:

* **NEVER raises.** All validators return structural verdicts.
* **No external calls.** Pure functions only.
* **Closed forbidden-field allow-list.** ``FORBIDDEN_FIELDS``
  mirrors the PAS174 tenant forbidden-key blocklist plus the
  PAS179-specific raw-content tokens.
* **Locked-by-default automatic mode.** ``validate_adaptive_
  memory_guardrails`` always reports the structural reason
  the recommendation cannot bypass operator review.

Public surface:

  * ``FORBIDDEN_FIELDS``                                — PII / secret tokens
  * ``learning_forbidden_field_scan(envelope)``         — deep scan
  * ``validate_learning_recommendation(record)``       — structural check
  * ``validate_simulation_safety(scenario)``           — read-only-only
  * ``validate_adaptive_memory_guardrails(record, brokerage)``
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `app.services.learning.learning_policy`, `automatic_mode_allowed`, `logging`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_safe_verdict`, `_walk_dict_keys`, `learning_forbidden_field_scan`, `validate_adaptive_memory_guardrails`, `validate_learning_recommendation`, `validate_simulation_safety`

## Env-key candidates

`FORBIDDEN_FIELDS`, `MEMORY_UPDATE`

## String constants (redacted where noted)

- '\nPAS179 — Controlled learning guardrails.\n\nClosed validators used by the recommendation engine and the\nsimulation harness to make sure no PII / secret / freeform\ncontent / live-mutation request slips through.\n\nDoctrine:\n\n* **NEVER raises.** All validators return structural verdicts.\n* **No external calls.** Pure functions only.\n* **Closed forbidden-field allow-list.** ``FORBIDDEN_FIELDS``\n  mirrors the PAS174 tenant forbidden-key blocklist plus the\n  PAS179-specific raw-content tokens.\n* **Locked-by-default automatic mode.** ``validate_adaptive_\n  memory_guardrails`` always reports the structural reason\n  the recommendation cannot bypass operator review.\n\nPublic surface:\n\n  * ``FORBIDDEN_FIELDS``                                — PII / secret tokens\n  * ``learning_forbidden_field_scan(envelope)``         — deep scan\n  * ``validate_learning_recommendation(record)``       — structural check\n  * ``validate_simulation_safety(scenario)``           — read-only-only\n  * ``validate_adaptive_memory_guardrails(record, brokerage)``\n'
- 'pas.learning.guardrails'
- 'Tuple[str, ...]'
- 'FORBIDDEN_FIELDS'
- 'error_code'
- 'warnings'
- 'found'
- 'path'
- 'out'
- 'valid'
- 'bool'
- 'Optional[str]'
- 'Optional[List[str]]'
- 'return'
- 'Dict[str, Any]'
- 'envelope'
- 'Any'
- 'str'
- 'Optional[List[Tuple[str, str]]]'
- 'List[Tuple[str, str]]'
- 'Walk every dict key in the envelope. Returns [(path, key)]\nlist. NEVER raises.'
- 'Scan an envelope for forbidden field names (case-\ninsensitive substring on keys). NEVER raises.'
- 'forbidden_field_present'
- 'learning_forbidden_field_scan error type='
- 'unexpected:'
- 'record'
- 'Structural validation of a CANDIDATE recommendation.\nNEVER raises.'
- 'invalid_record'
- 'status'
- 'recommendation_must_be_candidate'
- 'recommendation_type'
- 'invalid_recommendation_type'
- 'invalid_'
- 'out_of_range_'
- 'rationale_text'
- 'rationale_freeform'
- 'raw_rationale_present'
- 'scenario'
- 'Read-only simulation safety check. NEVER raises.\n\nConfirms:\n  * Envelope is a dict with a closed shape.\n  * No forbidden fields anywhere in the envelope.\n  * No request to mutate live behavior (i.e. metadata does\n    not carry an ``apply_live`` / ``mutate_*`` token).\n'
- 'invalid_scenario'
- 'live_mutation_request_blocked'
- 'brokerage'
- 'Cross-validate a MEMORY_UPDATE recommendation against\nthe controlled-learning policy. NEVER raises.\n\nPAS179 invariant: even for ``MEMORY_UPDATE`` recommendations,\nthe operator MUST review. The verdict ALWAYS includes\n``requires_operator_review=True``; PAS179 has no surface\nto auto-apply.\n'
- 'requires_operator_review'
- 'MEMORY_UPDATE'
- 'rationale_token'
- 'memory_update_requires_rationale_token'
- 'validate_adaptive_memory_guardrails policy lookup error type='
- 'automatic_mode_allowed'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS179 — Controlled learning guardrails.\n\nClosed validators used by the recommendation engine and the\nsimulation harness to make sure no PII / secret / freeform\ncontent / live-mutation request slips through.\n\nDoctrine:\n\n* **NEVER raises.** All validators return structural verdicts.\n* **No external calls.** Pure functions only.\n* **Closed forbidden-field allow-list.** ``FORBIDDEN_FIELDS``\n  mirrors the PAS174 tenant forbidden-key blocklist plus the\n  PAS179-specific raw-content tokens.\n* **Locked-by-default automatic mode.** ``validate_adaptive_\n  memory_guardrails`` always reports the structural reason\n  the recommendation cannot bypass operator review.\n\nPublic surface:\n\n  * ``FORBIDDEN_FIELDS``                                — PII / secret tokens\n  * ``learning_forbidden_field_scan(envelope)``         — deep scan\n  * ``validate_learning_recommendation(record)``       — structural check\n  * ``validate_simulation_safety(scenario)``           — read-only-only\n  * ``validate_adaptive_memory_guardrails(record, brokerage)``\n')
               STORE_NAME               1 (__doc__)

  28           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  30           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  31           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME              5 (typing)
               IMPORT_FROM              6 (Any)
               STORE_NAME               6 (Any)
               IMPORT_FROM              7 (Dict)
               STORE_NAME               7 (Dict)
               IMPORT_FROM              8 (List)
               STORE_NAME               8 (List)
               IMPORT_FROM              9 (Optional)
               STORE_NAME               9 (Optional)
               IMPORT_FROM             10 (Tuple)
               STORE_NAME              10 (Tuple)
               POP_TOP

  34           LOAD_NAME                4 (logging)
               LOAD_ATTR               22 (getLogger)
               PUSH_NULL
               LOAD_CONST               4 ('pas.learning.guardrails')
               CALL                     1
               STORE_NAME              12 (logger)

  40           LOAD_CONST              25 (('phone', 'email', 'name', 'raw_payload', 'raw_email', 'raw_body', 'transcript', 'summary', 'summary_text', 'secret', 'signature', 'env_value', 'env_values', 'dedupe_key', 'callback_notes', 'rationale_text', 'rationale_freeform', 'address', 'street', 'first_name', 'last_name', 'full_name'))
               STORE_NAME              13 (FORBIDDEN_FIELDS)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               14 (__annotations__)
               LOAD_CONST               6 ('FORBIDDEN_FIELDS')
               STORE_SUBSCR

  67           LOAD_CONST              26 (('MEMORY_UPDATE', 'SCRIPT_BRANCH_REVIEW', 'CALLBACK_TIMING_REVIEW', 'LEAD_PRIORITY_REVIEW', 'ROUTING_RULE_REVIEW', 'OBJECTION_PATTERN_REVIEW'))
               STORE_NAME              15 (_ALLOWED_RECOMMENDATION_TYPES)

  76           LOAD_CONST              27 (('CANDIDATE',))
               STORE_NAME              16 (_ALLOWED_INITIAL_STATUSES)

  79           LOAD_CONST               7 ('error_code')

  82           LOAD_CONST               2 (None)

  79           LOAD_CONST               8 ('warnings')

  83           LOAD_CONST               2 (None)

  79           LOAD_CONST               9 ('found')

  84           LOAD_CONST               2 (None)

  79           BUILD_MAP                3
               LOAD_CONST              10 (<code object __annotate__ at 0x0000018C18024D30, file "app/services/learning/guardrails.py", line 79>)
               MAKE_FUNCTION
               LOAD_CONST              11 (<code object _safe_verdict at 0x0000018C17FE17D0, file "app/services/learning/guardrails.py", line 79>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              17 (_safe_verdict)

  94           LOAD_CONST              12 ('path')

  97           LOAD_CONST              13 ('')

  94           LOAD_CONST              14 ('out')

  98           LOAD_CONST               2 (None)

  94           BUILD_MAP                2
               LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18025930, file "app/services/learning/guardrails.py", line 94>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _walk_dict_keys at 0x0000018C17F78410, file "app/services/learning/guardrails.py", line 94>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              18 (_walk_dict_keys)

 118           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA2B50, file "app/services/learning/guardrails.py", line 118>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object learning_forbidden_field_scan at 0x0000018C17EDABA0, file "app/services/learning/guardrails.py", line 118>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              19 (learning_forbidden_field_scan)

 145           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA3960, file "app/services/learning/guardrails.py", line 145>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object validate_learning_recommendation at 0x0000018C17D6DFC0, file "app/services/learning/guardrails.py", line 145>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              20 (validate_learning_recommendation)

 187           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA3B40, file "app/services/learning/guardrails.py", line 187>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object validate_simulation_safety at 0x0000018C17F0C960, file "app/services/learning/guardrails.py", line 187>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              21 (validate_simulation_safety)

 220           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C18025C30, file "app/services/learning/guardrails.py", line 220>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object validate_adaptive_memory_guardrails at 0x0000018C17CD4970, file "app/services/learning/guardrails.py", line 220>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              22 (validate_adaptive_memory_guardrails)

 268           BUILD_LIST               0
               LOAD_CONST              28 (('FORBIDDEN_FIELDS', 'learning_forbidden_field_scan', 'validate_learning_recommendation', 'validate_simulation_safety', 'validate_adaptive_memory_guardrails'))
               LIST_EXTEND              1
               STORE_NAME              23 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024D30, file "app/services/learning/guardrails.py", line 79>:
 79           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('valid')

 81           LOAD_CONST               2 ('bool')

 79           LOAD_CONST               3 ('error_code')

 82           LOAD_CONST               4 ('Optional[str]')

 79           LOAD_CONST               5 ('warnings')

 83           LOAD_CONST               6 ('Optional[List[str]]')

 79           LOAD_CONST               7 ('found')

 84           LOAD_CONST               6 ('Optional[List[str]]')

 79           LOAD_CONST               8 ('return')

 85           LOAD_CONST               9 ('Dict[str, Any]')

 79           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _safe_verdict at 0x0000018C17FE17D0, file "app/services/learning/guardrails.py", line 79>:
 79           RESUME                   0

 87           LOAD_CONST               0 ('valid')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         0 (valid)
              CALL                     1

 88           LOAD_CONST               1 ('error_code')
              LOAD_FAST                1 (error_code)

 89           LOAD_CONST               2 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                2 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

 90           LOAD_CONST               3 ('found')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                3 (found)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L2:     CALL                     1

 86           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app/services/learning/guardrails.py", line 94>:
 94           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('envelope')

 95           LOAD_CONST               2 ('Any')

 94           LOAD_CONST               3 ('path')

 97           LOAD_CONST               4 ('str')

 94           LOAD_CONST               5 ('out')

 98           LOAD_CONST               6 ('Optional[List[Tuple[str, str]]]')

 94           LOAD_CONST               7 ('return')

 99           LOAD_CONST               8 ('List[Tuple[str, str]]')

 94           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _walk_dict_keys at 0x0000018C17F78410, file "app/services/learning/guardrails.py", line 94>:
  94            RESUME                   0

 102            LOAD_FAST_BORROW         2 (out)
                POP_JUMP_IF_NOT_NONE     3 (to L1)
                NOT_TAKEN

 103            BUILD_LIST               0
                STORE_FAST               2 (out)

 104    L1:     NOP

 105    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (envelope)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       86 (to L7)
                NOT_TAKEN

 106            LOAD_FAST_BORROW         0 (envelope)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L3:     FOR_ITER                63 (to L5)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   52 (k, v)

 107            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L4)
                NOT_TAKEN

 108            LOAD_FAST_BORROW         2 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 19 (path, k)
                BUILD_TUPLE              2
                CALL                     1
                POP_TOP

 109    L4:     LOAD_GLOBAL             11 (_walk_dict_keys + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 65 (v, path)
                FORMAT_SIMPLE
                LOAD_CONST               1 ('.')
                LOAD_FAST_BORROW         3 (k)
                FORMAT_SIMPLE
                BUILD_STRING             3
                LOAD_FAST_BORROW         2 (out)
                LOAD_CONST               2 (('path', 'out'))
                CALL_KW                  3
                POP_TOP
                JUMP_BACKWARD           65 (to L3)

 106    L5:     END_FOR
                POP_ITER

 115    L6:     LOAD_FAST_BORROW         2 (out)
                RETURN_VALUE

 110    L7:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (envelope)
                LOAD_GLOBAL             12 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       40 (to L10)
                NOT_TAKEN

 111            LOAD_GLOBAL             15 (enumerate + NULL)
                LOAD_FAST_BORROW         0 (envelope)
                CALL                     1
                GET_ITER
        L8:     FOR_ITER                24 (to L9)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   84 (i, v)

 112            LOAD_GLOBAL             11 (_walk_dict_keys + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 65 (v, path)
                FORMAT_SIMPLE
                LOAD_CONST               3 ('[')
                LOAD_FAST_BORROW         5 (i)
                FORMAT_SIMPLE
                LOAD_CONST               4 (']')
                BUILD_STRING             4
                LOAD_FAST_BORROW         2 (out)
                LOAD_CONST               2 (('path', 'out'))
                CALL_KW                  3
                POP_TOP
                JUMP_BACKWARD           26 (to L8)

 111    L9:     END_FOR
                POP_ITER

 115   L10:     LOAD_FAST_BORROW         2 (out)
                RETURN_VALUE

  --   L11:     PUSH_EXC_INFO

 113            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L13)
                NOT_TAKEN
                POP_TOP

 114   L12:     POP_EXCEPT

 115            LOAD_FAST                2 (out)
                RETURN_VALUE

 113   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L6 -> L11 [0]
  L7 to L10 -> L11 [0]
  L11 to L12 -> L14 [1] lasti
  L13 to L14 -> L14 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app/services/learning/guardrails.py", line 118>:
118           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object learning_forbidden_field_scan at 0x0000018C17EDABA0, file "app/services/learning/guardrails.py", line 118>:
 118            RESUME                   0

 121            NOP

 122    L1:     LOAD_GLOBAL              1 (_walk_dict_keys + NULL)
                LOAD_FAST_BORROW         0 (envelope)
                CALL                     1
                STORE_FAST               1 (keys)

 123            BUILD_LIST               0
                STORE_FAST               2 (bad)

 124            LOAD_FAST_BORROW         1 (keys)
                GET_ITER
        L2:     FOR_ITER                75 (to L11)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   52 (path, k)

 125            LOAD_FAST_BORROW         4 (k)
                LOAD_ATTR                3 (lower + NULL|self)
                CALL                     0
                STORE_FAST               5 (kl)

 126            LOAD_GLOBAL              4 (FORBIDDEN_FIELDS)
                GET_ITER
        L3:     FOR_ITER                44 (to L10)
                STORE_FAST               6 (forb)

 127            LOAD_FAST_BORROW_LOAD_FAST_BORROW 101 (forb, kl)
                CONTAINS_OP              0 (in)
        L4:     POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L3)

 128    L5:     LOAD_FAST                2 (bad)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_FAST_BORROW         3 (path)
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L8)
        L6:     NOT_TAKEN
        L7:     LOAD_FAST_BORROW         3 (path)
                FORMAT_SIMPLE
                LOAD_CONST               1 ('.')
                LOAD_FAST_BORROW         4 (k)
                FORMAT_SIMPLE
                BUILD_STRING             3
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_FAST                4 (k)
        L9:     CALL                     1
                POP_TOP

 129            POP_TOP
                JUMP_BACKWARD           73 (to L2)

 126   L10:     END_FOR
                POP_ITER
                JUMP_BACKWARD           77 (to L2)

 124   L11:     END_FOR
                POP_ITER

 130            LOAD_GLOBAL              9 (_safe_verdict + NULL)

 131            LOAD_FAST_BORROW         2 (bad)
                TO_BOOL
                UNARY_NOT

 132            LOAD_FAST_BORROW         2 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN
                LOAD_CONST               2 ('forbidden_field_present')
                JUMP_FORWARD             1 (to L13)
       L12:     LOAD_CONST               3 (None)

 133   L13:     LOAD_FAST_BORROW         2 (bad)
                LOAD_CONST               4 (slice(None, 25, None))
                BINARY_OP               26 ([])

 130            LOAD_CONST               5 (('valid', 'error_code', 'found'))
                CALL_KW                  3
       L14:     RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 135            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       89 (to L20)
                NOT_TAKEN
                STORE_FAST               7 (e)

 136   L16:     LOAD_GLOBAL             12 (logger)
                LOAD_ATTR               15 (warning + NULL|self)

 137            LOAD_CONST               6 ('learning_forbidden_field_scan error type=')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 136            CALL                     1
                POP_TOP

 139            LOAD_GLOBAL              9 (_safe_verdict + NULL)

 140            LOAD_CONST               7 (False)

 141            LOAD_CONST               8 ('unexpected:')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 139            LOAD_CONST               9 (('valid', 'error_code'))
                CALL_KW                  2
       L17:     SWAP                     2
       L18:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L19:     LOAD_CONST               3 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 135   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L4 -> L15 [0]
  L5 to L6 -> L15 [0]
  L7 to L14 -> L15 [0]
  L15 to L16 -> L21 [1] lasti
  L16 to L17 -> L19 [1] lasti
  L17 to L18 -> L21 [1] lasti
  L19 to L21 -> L21 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app/services/learning/guardrails.py", line 145>:
145           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object validate_learning_recommendation at 0x0000018C17D6DFC0, file "app/services/learning/guardrails.py", line 145>:
 145            RESUME                   0

 148            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (record)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L1)
                NOT_TAKEN

 149            LOAD_GLOBAL              5 (_safe_verdict + NULL)
                LOAD_CONST               1 (False)
                LOAD_CONST               2 ('invalid_record')
                LOAD_CONST               3 (('valid', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 151    L1:     LOAD_FAST_BORROW         0 (record)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               4 ('status')
                CALL                     1
                LOAD_GLOBAL              8 (_ALLOWED_INITIAL_STATUSES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       14 (to L2)
                NOT_TAKEN

 152            LOAD_GLOBAL              5 (_safe_verdict + NULL)

 153            LOAD_CONST               1 (False)
                LOAD_CONST               5 ('recommendation_must_be_candidate')

 152            LOAD_CONST               3 (('valid', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 156    L2:     LOAD_FAST_BORROW         0 (record)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               6 ('recommendation_type')
                CALL                     1
                LOAD_GLOBAL             10 (_ALLOWED_RECOMMENDATION_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       14 (to L3)
                NOT_TAKEN

 157            LOAD_GLOBAL              5 (_safe_verdict + NULL)

 158            LOAD_CONST               1 (False)
                LOAD_CONST               7 ('invalid_recommendation_type')

 157            LOAD_CONST               3 (('valid', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 161    L3:     LOAD_CONST              21 (('confidence_score', 'risk_score', 'usefulness_score'))
                GET_ITER
        L4:     FOR_ITER                70 (to L9)
                STORE_FAST               1 (k)

 162            LOAD_FAST_BORROW         0 (record)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_FAST_BORROW         1 (k)
                CALL                     1
                STORE_FAST               2 (v)

 163            LOAD_FAST_BORROW         2 (v)
                POP_JUMP_IF_NOT_NONE     3 (to L5)
                NOT_TAKEN

 164            JUMP_BACKWARD           26 (to L4)

 165    L5:     NOP

 166    L6:     LOAD_GLOBAL             13 (float + NULL)
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               3 (f)

 169    L7:     LOAD_FAST                3 (f)
                LOAD_CONST               9 (0.0)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_TRUE        10 (to L8)
                NOT_TAKEN
                LOAD_FAST                3 (f)
                LOAD_CONST              10 (1.0)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           54 (to L4)

 170    L8:     LOAD_GLOBAL              5 (_safe_verdict + NULL)
                LOAD_CONST               1 (False)
                LOAD_CONST              11 ('out_of_range_')
                LOAD_FAST                1 (k)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_CONST               3 (('valid', 'error_code'))
                CALL_KW                  2
                SWAP                     2
                POP_TOP
                RETURN_VALUE

 161    L9:     END_FOR
                POP_ITER

 172            LOAD_FAST_BORROW         0 (record)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST              12 ('rationale_text')
                CALL                     1
                POP_JUMP_IF_NOT_NONE    20 (to L10)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (record)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST              13 ('rationale_freeform')
                CALL                     1
                POP_JUMP_IF_NONE        14 (to L11)
                NOT_TAKEN

 173   L10:     LOAD_GLOBAL              5 (_safe_verdict + NULL)

 174            LOAD_CONST               1 (False)
                LOAD_CONST              14 ('raw_rationale_present')

 173            LOAD_CONST               3 (('valid', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 177   L11:     LOAD_GLOBAL             19 (learning_forbidden_field_scan + NULL)
                LOAD_FAST_BORROW         0 (record)
                CALL                     1
                STORE_FAST               4 (scan)

 178            LOAD_FAST_BORROW         4 (scan)
                LOAD_CONST              15 ('valid')
                BINARY_OP               26 ([])
                TO_BOOL
                POP_JUMP_IF_TRUE        29 (to L12)
                NOT_TAKEN

 179            LOAD_GLOBAL              5 (_safe_verdict + NULL)

 180            LOAD_CONST               1 (False)

 181            LOAD_FAST_BORROW         4 (scan)
                LOAD_CONST              16 ('error_code')
                BINARY_OP               26 ([])

 182            LOAD_FAST_BORROW         4 (scan)
                LOAD_CONST              17 ('found')
                BINARY_OP               26 ([])

 179            LOAD_CONST              18 (('valid', 'error_code', 'found'))
                CALL_KW                  3
                RETURN_VALUE

 184   L12:     LOAD_GLOBAL              5 (_safe_verdict + NULL)
                LOAD_CONST              19 (True)
                LOAD_CONST              20 (('valid',))
                CALL_KW                  1
                RETURN_VALUE

  --   L13:     PUSH_EXC_INFO

 167            LOAD_GLOBAL             14 (TypeError)
                LOAD_GLOBAL             16 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       22 (to L15)
                NOT_TAKEN
                POP_TOP

 168            LOAD_GLOBAL              5 (_safe_verdict + NULL)
                LOAD_CONST               1 (False)
                LOAD_CONST               8 ('invalid_')
                LOAD_FAST                1 (k)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_CONST               3 (('valid', 'error_code'))
                CALL_KW                  2
                SWAP                     2
       L14:     POP_EXCEPT
                SWAP                     2
                POP_TOP
                RETURN_VALUE

 167   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L6 to L7 -> L13 [1]
  L13 to L14 -> L16 [2] lasti
  L15 to L16 -> L16 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app/services/learning/guardrails.py", line 187>:
187           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('scenario')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object validate_simulation_safety at 0x0000018C17F0C960, file "app/services/learning/guardrails.py", line 187>:
187           RESUME                   0

196           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (scenario)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        14 (to L1)
              NOT_TAKEN

197           LOAD_GLOBAL              5 (_safe_verdict + NULL)
              LOAD_CONST               1 (False)
              LOAD_CONST               2 ('invalid_scenario')
              LOAD_CONST               3 (('valid', 'error_code'))
              CALL_KW                  2
              RETURN_VALUE

198   L1:     LOAD_GLOBAL              7 (learning_forbidden_field_scan + NULL)
              LOAD_FAST_BORROW         0 (scenario)
              CALL                     1
              STORE_FAST               1 (scan)

199           LOAD_FAST_BORROW         1 (scan)
              LOAD_CONST               4 ('valid')
              BINARY_OP               26 ([])
              TO_BOOL
              POP_JUMP_IF_TRUE        29 (to L2)
              NOT_TAKEN

200           LOAD_GLOBAL              5 (_safe_verdict + NULL)

201           LOAD_CONST               1 (False)

202           LOAD_FAST_BORROW         1 (scan)
              LOAD_CONST               5 ('error_code')
              BINARY_OP               26 ([])

203           LOAD_FAST_BORROW         1 (scan)
              LOAD_CONST               6 ('found')
              BINARY_OP               26 ([])

200           LOAD_CONST               7 (('valid', 'error_code', 'found'))
              CALL_KW                  3
              RETURN_VALUE

206   L2:     LOAD_CONST              12 (('apply_live', 'mutate_live', 'auto_apply', 'auto_approve'))
              STORE_FAST               2 (bad_tokens)

207           LOAD_GLOBAL              9 (_walk_dict_keys + NULL)
              LOAD_FAST_BORROW         0 (scenario)
              CALL                     1
              STORE_FAST               3 (keys)

208           LOAD_FAST_BORROW         3 (keys)
              GET_ITER
      L3:     FOR_ITER                70 (to L9)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   69 (path, k)

209           LOAD_FAST_BORROW         5 (k)
              LOAD_ATTR               11 (lower + NULL|self)
              CALL                     0
              STORE_FAST               6 (kl)

210           LOAD_FAST_BORROW         2 (bad_tokens)
              GET_ITER
      L4:     FOR_ITER                43 (to L8)
              STORE_FAST               7 (tok)

211           LOAD_FAST_BORROW_LOAD_FAST_BORROW 118 (tok, kl)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L4)

212   L5:     LOAD_GLOBAL              5 (_safe_verdict + NULL)

213           LOAD_CONST               1 (False)

214           LOAD_CONST               8 ('live_mutation_request_blocked')

215           LOAD_FAST_BORROW         4 (path)
              TO_BOOL
              POP_JUMP_IF_FALSE        8 (to L6)
              NOT_TAKEN
              LOAD_FAST_BORROW         4 (path)
              FORMAT_SIMPLE
              LOAD_CONST               9 ('.')
              LOAD_FAST_BORROW         5 (k)
              FORMAT_SIMPLE
              BUILD_STRING             3
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_FAST                5 (k)
      L7:     BUILD_LIST               1

212           LOAD_CONST               7 (('valid', 'error_code', 'found'))
              CALL_KW                  3
              SWAP                     2
              POP_TOP
              SWAP                     2
              POP_TOP
              RETURN_VALUE

210   L8:     END_FOR
              POP_ITER
              JUMP_BACKWARD           72 (to L3)

208   L9:     END_FOR
              POP_ITER

217           LOAD_GLOBAL              5 (_safe_verdict + NULL)
              LOAD_CONST              10 (True)
              LOAD_CONST              11 (('valid',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app/services/learning/guardrails.py", line 220>:
220           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record')

221           LOAD_CONST               2 ('Any')

220           LOAD_CONST               3 ('brokerage')

222           LOAD_CONST               2 ('Any')

220           LOAD_CONST               4 ('return')

223           LOAD_CONST               5 ('Dict[str, Any]')

220           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object validate_adaptive_memory_guardrails at 0x0000018C17CD4970, file "app/services/learning/guardrails.py", line 220>:
 220            RESUME                   0

 232            LOAD_GLOBAL              1 (validate_learning_recommendation + NULL)
                LOAD_FAST_BORROW         0 (record)
                CALL                     1
                STORE_FAST               2 (base)

 233            LOAD_FAST_BORROW         2 (base)
                LOAD_CONST               1 ('valid')
                BINARY_OP               26 ([])
                TO_BOOL
                POP_JUMP_IF_TRUE         9 (to L1)
                NOT_TAKEN

 234            BUILD_MAP                0

 235            LOAD_FAST_BORROW         2 (base)

 234            DICT_UPDATE              1

 236            LOAD_CONST               2 ('requires_operator_review')
                LOAD_CONST               3 (True)

 234            BUILD_MAP                1
                DICT_UPDATE              1
                RETURN_VALUE

 240    L1:     LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (record)
                LOAD_GLOBAL              4 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      111 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (record)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               4 ('recommendation_type')
                CALL                     1
                LOAD_CONST               5 ('MEMORY_UPDATE')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       89 (to L3)
                NOT_TAKEN

 241            LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (record)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               6 ('rationale_token')
                CALL                     1
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (record)
                LOAD_CONST               6 ('rationale_token')
                BINARY_OP               26 ([])
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L3)
                NOT_TAKEN

 242    L2:     LOAD_GLOBAL             13 (_safe_verdict + NULL)

 243            LOAD_CONST               7 (False)

 244            LOAD_CONST               8 ('memory_update_requires_rationale_token')

 242            LOAD_CONST               9 (('valid', 'error_code'))
                CALL_KW                  2

 245            LOAD_CONST               2 ('requires_operator_review')
                LOAD_CONST               3 (True)
                BUILD_MAP                1

 242            BINARY_OP                7 (|)
                RETURN_VALUE

 247    L3:     NOP

 248    L4:     LOAD_SMALL_INT           0
                LOAD_CONST              10 (('automatic_mode_allowed',))
                IMPORT_NAME              7 (app.services.learning.learning_policy)
                IMPORT_FROM              8 (automatic_mode_allowed)
                STORE_FAST               3 (automatic_mode_allowed)
                POP_TOP

 251            LOAD_FAST_BORROW         3 (automatic_mode_allowed)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (brokerage)
                CALL                     1
                STORE_FAST               4 (allowed)

 259    L5:     LOAD_CONST               1 ('valid')
                LOAD_CONST               3 (True)

 260            LOAD_CONST              13 ('error_code')
                LOAD_CONST              12 (None)

 261            LOAD_CONST              14 ('warnings')
                BUILD_LIST               0

 262            LOAD_CONST              15 ('found')
                BUILD_LIST               0

 263            LOAD_CONST               2 ('requires_operator_review')
                LOAD_CONST               3 (True)

 264            LOAD_CONST              16 ('automatic_mode_allowed')
                LOAD_GLOBAL             29 (bool + NULL)
                LOAD_FAST_BORROW         4 (allowed)
                CALL                     1

 258            BUILD_MAP                6
                RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 252            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       56 (to L10)
                NOT_TAKEN
                STORE_FAST               5 (e)

 253    L7:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 254            LOAD_CONST              11 ('validate_adaptive_memory_guardrails policy lookup error type=')

 255            LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE

 254            BUILD_STRING             2

 253            CALL                     1
                POP_TOP

 257            LOAD_CONST               7 (False)
                STORE_FAST               4 (allowed)
        L8:     POP_EXCEPT
                LOAD_CONST              12 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                JUMP_BACKWARD_NO_INTERRUPT 84 (to L5)

  --    L9:     LOAD_CONST              12 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 252   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L6 [0]
  L6 to L7 -> L11 [1] lasti
  L7 to L8 -> L9 [1] lasti
  L9 to L11 -> L11 [1] lasti
```
