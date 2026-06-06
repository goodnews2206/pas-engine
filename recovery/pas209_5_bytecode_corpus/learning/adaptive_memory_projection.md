# learning/adaptive_memory_projection

- **pyc:** `app\services\learning\__pycache__\adaptive_memory_projection.cpython-314.pyc`
- **expected source path (absent):** `app\services\learning/adaptive_memory_projection.py`
- **co_filename (from bytecode):** `app/services/learning/adaptive_memory_projection.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** learning

## Module docstring

```
PAS182 — Safe projections for adaptive-memory bridge envelopes.

Renders bridge-state and bridge-eligibility envelopes into two
closed-shape projections:

* ``project_operator_bridge_view(envelope)`` — operator dashboard.
* ``project_tenant_bridge_view(envelope)``   — tenant portal.

Doctrine:

* **Closed allow-lists.** Both projections are explicit — every
  field outside the allow-list is dropped.
* **Tenant projection deliberately narrower.** Drops
  ``recommendation_id``, ``test_run_id``, ``memory_candidate_id``,
  ``evidence_fingerprint``, ``actor_type``, ``actor_id``, and
  any operator-internal counter.
* **Forbidden-field scan.** Mirrors the PAS180 / PAS181
  blocklists plus the PAS182-specific raw-content tokens.
* **NEVER raises.**
```

## Imports

`Any`, `Dict`, `Iterable`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `logging`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_is_safe_value`, `_key_is_forbidden`, `project_operator_bridge_list`, `project_operator_bridge_view`, `project_tenant_bridge_list`, `project_tenant_bridge_view`

## Env-key candidates

`OPERATOR_BRIDGE_KEYS`, `PROJECTION_FORBIDDEN_KEYS`, `TENANT_BRIDGE_KEYS`

## String constants (redacted where noted)

- '\nPAS182 — Safe projections for adaptive-memory bridge envelopes.\n\nRenders bridge-state and bridge-eligibility envelopes into two\nclosed-shape projections:\n\n* ``project_operator_bridge_view(envelope)`` — operator dashboard.\n* ``project_tenant_bridge_view(envelope)``   — tenant portal.\n\nDoctrine:\n\n* **Closed allow-lists.** Both projections are explicit — every\n  field outside the allow-list is dropped.\n* **Tenant projection deliberately narrower.** Drops\n  ``recommendation_id``, ``test_run_id``, ``memory_candidate_id``,\n  ``evidence_fingerprint``, ``actor_type``, ``actor_id``, and\n  any operator-internal counter.\n* **Forbidden-field scan.** Mirrors the PAS180 / PAS181\n  blocklists plus the PAS182-specific raw-content tokens.\n* **NEVER raises.**\n'
- 'pas.learning.adaptive_memory_projection'
- 'Tuple[str, ...]'
- 'OPERATOR_BRIDGE_KEYS'
- 'TENANT_BRIDGE_KEYS'
- 'PROJECTION_FORBIDDEN_KEYS'
- 'Any'
- 'return'
- 'bool'
- 'Closed-shape primitive: bool / int / float / None / bounded\nstring. Lists / dicts are not allowed in projections.'
- 'envelope'
- 'Dict[str, Any]'
- 'Render a single bridge envelope for the operator dashboard.\nNEVER raises.'
- 'project_operator_bridge_view error type='
- 'Render a single bridge envelope for the tenant portal.\nNEVER raises. NEVER carries operator actor ids / recommendation\nids / fingerprints.'
- 'project_tenant_bridge_view error type='
- 'rows'
- 'Iterable[Any]'
- 'List[Dict[str, Any]]'
- 'Map ``project_operator_bridge_view`` over a row list.\nNEVER raises.'
- 'project_operator_bridge_list error type='
- 'Map ``project_tenant_bridge_view`` over a row list.\nNEVER raises.'
- 'project_tenant_bridge_list error type='

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS182 — Safe projections for adaptive-memory bridge envelopes.\n\nRenders bridge-state and bridge-eligibility envelopes into two\nclosed-shape projections:\n\n* ``project_operator_bridge_view(envelope)`` — operator dashboard.\n* ``project_tenant_bridge_view(envelope)``   — tenant portal.\n\nDoctrine:\n\n* **Closed allow-lists.** Both projections are explicit — every\n  field outside the allow-list is dropped.\n* **Tenant projection deliberately narrower.** Drops\n  ``recommendation_id``, ``test_run_id``, ``memory_candidate_id``,\n  ``evidence_fingerprint``, ``actor_type``, ``actor_id``, and\n  any operator-internal counter.\n* **Forbidden-field scan.** Mirrors the PAS180 / PAS181\n  blocklists plus the PAS182-specific raw-content tokens.\n* **NEVER raises.**\n')
               STORE_NAME               1 (__doc__)

  23           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  25           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  26           LOAD_SMALL_INT           0
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

  29           LOAD_NAME                4 (logging)
               LOAD_ATTR               24 (getLogger)
               PUSH_NULL
               LOAD_CONST               4 ('pas.learning.adaptive_memory_projection')
               CALL                     1
               STORE_NAME              13 (logger)

  34           LOAD_CONST              21 (('brokerage_id', 'recommendation_id', 'test_run_id', 'memory_candidate_id', 'status', 'eligible', 'reason_code', 'risk_score', 'confidence_score', 'warning_count', 'error_code', 'actor_type', 'actor_id', 'created_at', 'evidence_fingerprint'))
               STORE_NAME              14 (OPERATOR_BRIDGE_KEYS)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               15 (__annotations__)
               LOAD_CONST               6 ('OPERATOR_BRIDGE_KEYS')
               STORE_SUBSCR

  56           LOAD_CONST              22 (('status', 'eligible', 'reason_code', 'risk_score', 'confidence_score', 'created_at'))
               STORE_NAME              16 (TENANT_BRIDGE_KEYS)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               15 (__annotations__)
               LOAD_CONST               7 ('TENANT_BRIDGE_KEYS')
               STORE_SUBSCR

  68           LOAD_CONST              23 (('phone', 'email', 'name', 'raw_payload', 'raw_email', 'raw_body', 'transcript', 'summary', 'summary_text', 'secret', 'signature', 'env_value', 'env_values', 'dedupe_key', 'callback_notes', 'rationale_text', 'rationale_freeform', 'prompt', 'prompt_text', 'evidence_raw', 'live_mutation_payload', 'first_name', 'last_name', 'full_name', 'address', 'street'))
               STORE_NAME              17 (PROJECTION_FORBIDDEN_KEYS)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               15 (__annotations__)
               LOAD_CONST               8 ('PROJECTION_FORBIDDEN_KEYS')
               STORE_SUBSCR

  83           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA3780, file "app/services/learning/adaptive_memory_projection.py", line 83>)
               MAKE_FUNCTION
               LOAD_CONST              10 (<code object _is_safe_value at 0x0000018C17FF13B0, file "app/services/learning/adaptive_memory_projection.py", line 83>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              18 (_is_safe_value)

  93           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA3870, file "app/services/learning/adaptive_memory_projection.py", line 93>)
               MAKE_FUNCTION
               LOAD_CONST              12 (<code object _key_is_forbidden at 0x0000018C18010DF0, file "app/services/learning/adaptive_memory_projection.py", line 93>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              19 (_key_is_forbidden)

 103           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA33C0, file "app/services/learning/adaptive_memory_projection.py", line 103>)
               MAKE_FUNCTION
               LOAD_CONST              14 (<code object project_operator_bridge_view at 0x0000018C17ED5630, file "app/services/learning/adaptive_memory_projection.py", line 103>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              20 (project_operator_bridge_view)

 123           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA2100, file "app/services/learning/adaptive_memory_projection.py", line 123>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object project_tenant_bridge_view at 0x0000018C17ED5860, file "app/services/learning/adaptive_memory_projection.py", line 123>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              21 (project_tenant_bridge_view)

 144           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA2C40, file "app/services/learning/adaptive_memory_projection.py", line 144>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object project_operator_bridge_list at 0x0000018C180488F0, file "app/services/learning/adaptive_memory_projection.py", line 144>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              22 (project_operator_bridge_list)

 156           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA2E20, file "app/services/learning/adaptive_memory_projection.py", line 156>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object project_tenant_bridge_list at 0x0000018C180483B0, file "app/services/learning/adaptive_memory_projection.py", line 156>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              23 (project_tenant_bridge_list)

 168           BUILD_LIST               0
               LOAD_CONST              24 (('OPERATOR_BRIDGE_KEYS', 'TENANT_BRIDGE_KEYS', 'PROJECTION_FORBIDDEN_KEYS', 'project_operator_bridge_view', 'project_tenant_bridge_view', 'project_operator_bridge_list', 'project_tenant_bridge_list'))
               LIST_EXTEND              1
               STORE_NAME              24 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app/services/learning/adaptive_memory_projection.py", line 83>:
 83           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('v')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _is_safe_value at 0x0000018C17FF13B0, file "app/services/learning/adaptive_memory_projection.py", line 83>:
 83           RESUME                   0

 86           LOAD_FAST_BORROW         0 (v)
              POP_JUMP_IF_NONE        34 (to L1)
              NOT_TAKEN
              LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (v)
              LOAD_GLOBAL              2 (bool)
              LOAD_GLOBAL              4 (int)
              LOAD_GLOBAL              6 (float)
              BUILD_TUPLE              3
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

 87   L1:     LOAD_CONST               1 (True)
              RETURN_VALUE

 88   L2:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (v)
              LOAD_GLOBAL              8 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       19 (to L3)
              NOT_TAKEN
              LOAD_GLOBAL             11 (len + NULL)
              LOAD_FAST_BORROW         0 (v)
              CALL                     1
              LOAD_CONST               2 (1024)
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

 89           LOAD_CONST               1 (True)
              RETURN_VALUE

 90   L3:     LOAD_CONST               3 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app/services/learning/adaptive_memory_projection.py", line 93>:
 93           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('k')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _key_is_forbidden at 0x0000018C18010DF0, file "app/services/learning/adaptive_memory_projection.py", line 93>:
 93           RESUME                   0

 94           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (k)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 95           LOAD_CONST               0 (False)
              RETURN_VALUE

 96   L1:     LOAD_FAST_BORROW         0 (k)
              LOAD_ATTR                5 (lower + NULL|self)
              CALL                     0
              STORE_FAST               1 (kl)

 97           LOAD_GLOBAL              6 (PROJECTION_FORBIDDEN_KEYS)
              GET_ITER
      L2:     FOR_ITER                12 (to L4)
              STORE_FAST               2 (forb)

 98           LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (forb, kl)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

 99   L3:     POP_TOP
              LOAD_CONST               1 (True)
              RETURN_VALUE

 97   L4:     END_FOR
              POP_ITER

100           LOAD_CONST               0 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app/services/learning/adaptive_memory_projection.py", line 103>:
103           RESUME                   0
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

Disassembly of <code object project_operator_bridge_view at 0x0000018C17ED5630, file "app/services/learning/adaptive_memory_projection.py", line 103>:
 103            RESUME                   0

 106            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (envelope)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 107            BUILD_MAP                0
                RETURN_VALUE

 108    L1:     BUILD_MAP                0
                STORE_FAST               1 (out)

 109            NOP

 110    L2:     LOAD_GLOBAL              4 (OPERATOR_BRIDGE_KEYS)
                GET_ITER
        L3:     FOR_ITER                61 (to L10)
                STORE_FAST               2 (k)

 111            LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, envelope)
                CONTAINS_OP              0 (in)
        L4:     POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L3)
        L5:     LOAD_GLOBAL              7 (_key_is_forbidden + NULL)
                LOAD_FAST_BORROW         2 (k)
                CALL                     1
                TO_BOOL
        L6:     POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           30 (to L3)

 112    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (envelope, k)
                BINARY_OP               26 ([])
                STORE_FAST               3 (v)

 113            LOAD_GLOBAL              9 (_is_safe_value + NULL)
                LOAD_FAST_BORROW         3 (v)
                CALL                     1
                TO_BOOL
        L8:     POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           57 (to L3)

 114    L9:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
                LOAD_FAST_BORROW         2 (k)
                STORE_SUBSCR
                JUMP_BACKWARD           63 (to L3)

 110   L10:     END_FOR
                POP_ITER

 115            LOAD_FAST_BORROW         1 (out)
       L11:     RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 116            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       56 (to L17)
                NOT_TAKEN
                STORE_FAST               4 (e)

 117   L13:     LOAD_GLOBAL             12 (logger)
                LOAD_ATTR               15 (warning + NULL|self)

 118            LOAD_CONST               1 ('project_operator_bridge_view error type=')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 117            CALL                     1
                POP_TOP

 120            BUILD_MAP                0
       L14:     SWAP                     2
       L15:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RETURN_VALUE

  --   L16:     LOAD_CONST               2 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 116   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L4 -> L12 [0]
  L5 to L6 -> L12 [0]
  L7 to L8 -> L12 [0]
  L9 to L11 -> L12 [0]
  L12 to L13 -> L18 [1] lasti
  L13 to L14 -> L16 [1] lasti
  L14 to L15 -> L18 [1] lasti
  L16 to L18 -> L18 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app/services/learning/adaptive_memory_projection.py", line 123>:
123           RESUME                   0
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

Disassembly of <code object project_tenant_bridge_view at 0x0000018C17ED5860, file "app/services/learning/adaptive_memory_projection.py", line 123>:
 123            RESUME                   0

 127            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (envelope)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 128            BUILD_MAP                0
                RETURN_VALUE

 129    L1:     BUILD_MAP                0
                STORE_FAST               1 (out)

 130            NOP

 131    L2:     LOAD_GLOBAL              4 (TENANT_BRIDGE_KEYS)
                GET_ITER
        L3:     FOR_ITER                61 (to L10)
                STORE_FAST               2 (k)

 132            LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, envelope)
                CONTAINS_OP              0 (in)
        L4:     POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L3)
        L5:     LOAD_GLOBAL              7 (_key_is_forbidden + NULL)
                LOAD_FAST_BORROW         2 (k)
                CALL                     1
                TO_BOOL
        L6:     POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           30 (to L3)

 133    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (envelope, k)
                BINARY_OP               26 ([])
                STORE_FAST               3 (v)

 134            LOAD_GLOBAL              9 (_is_safe_value + NULL)
                LOAD_FAST_BORROW         3 (v)
                CALL                     1
                TO_BOOL
        L8:     POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           57 (to L3)

 135    L9:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
                LOAD_FAST_BORROW         2 (k)
                STORE_SUBSCR
                JUMP_BACKWARD           63 (to L3)

 131   L10:     END_FOR
                POP_ITER

 136            LOAD_FAST_BORROW         1 (out)
       L11:     RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 137            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       56 (to L17)
                NOT_TAKEN
                STORE_FAST               4 (e)

 138   L13:     LOAD_GLOBAL             12 (logger)
                LOAD_ATTR               15 (warning + NULL|self)

 139            LOAD_CONST               1 ('project_tenant_bridge_view error type=')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 138            CALL                     1
                POP_TOP

 141            BUILD_MAP                0
       L14:     SWAP                     2
       L15:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RETURN_VALUE

  --   L16:     LOAD_CONST               2 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 137   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L4 -> L12 [0]
  L5 to L6 -> L12 [0]
  L7 to L8 -> L12 [0]
  L9 to L11 -> L12 [0]
  L12 to L13 -> L18 [1] lasti
  L13 to L14 -> L16 [1] lasti
  L14 to L15 -> L18 [1] lasti
  L16 to L18 -> L18 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app/services/learning/adaptive_memory_projection.py", line 144>:
144           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rows')
              LOAD_CONST               2 ('Iterable[Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Dict[str, Any]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object project_operator_bridge_list at 0x0000018C180488F0, file "app/services/learning/adaptive_memory_projection.py", line 144>:
 144            RESUME                   0

 147            NOP

 148    L1:     LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18090030, file "app/services/learning/adaptive_memory_projection.py", line 148>)
                MAKE_FUNCTION
                LOAD_FAST                0 (rows)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
        L2:     NOT_TAKEN
        L3:     POP_TOP
                LOAD_CONST               4 (())
        L4:     GET_ITER
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (p)
                SWAP                     2
        L5:     BUILD_LIST               0
                SWAP                     2
        L6:     FOR_ITER                14 (to L9)
                STORE_FAST_LOAD_FAST    17 (p, p)
                TO_BOOL
        L7:     POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           12 (to L6)
        L8:     LOAD_FAST_BORROW         1 (p)
                LIST_APPEND              2
                JUMP_BACKWARD           16 (to L6)
        L9:     END_FOR
                POP_ITER
       L10:     SWAP                     2
                STORE_FAST               1 (p)
       L11:     RETURN_VALUE

  --   L12:     SWAP                     2
                POP_TOP

 148            SWAP                     2
                STORE_FAST               1 (p)
                RERAISE                  0

  --   L13:     PUSH_EXC_INFO

 149            LOAD_GLOBAL              0 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       56 (to L18)
                NOT_TAKEN
                STORE_FAST               2 (e)

 150   L14:     LOAD_GLOBAL              2 (logger)
                LOAD_ATTR                5 (warning + NULL|self)

 151            LOAD_CONST               2 ('project_operator_bridge_list error type=')
                LOAD_GLOBAL              7 (type + NULL)
                LOAD_FAST                2 (e)
                CALL                     1
                LOAD_ATTR                8 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 150            CALL                     1
                POP_TOP

 153            BUILD_LIST               0
       L15:     SWAP                     2
       L16:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                RETURN_VALUE

  --   L17:     LOAD_CONST               3 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                RERAISE                  1

 149   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L13 [0]
  L3 to L5 -> L13 [0]
  L5 to L7 -> L12 [2]
  L8 to L10 -> L12 [2]
  L10 to L11 -> L13 [0]
  L12 to L13 -> L13 [0]
  L13 to L14 -> L19 [1] lasti
  L14 to L15 -> L17 [1] lasti
  L15 to L16 -> L19 [1] lasti
  L17 to L19 -> L19 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C18090030, file "app/services/learning/adaptive_memory_projection.py", line 148>:
 148           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (project_operator_bridge_view + NULL)
               LOAD_FAST_BORROW         1 (r)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app/services/learning/adaptive_memory_projection.py", line 156>:
156           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rows')
              LOAD_CONST               2 ('Iterable[Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Dict[str, Any]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object project_tenant_bridge_list at 0x0000018C180483B0, file "app/services/learning/adaptive_memory_projection.py", line 156>:
 156            RESUME                   0

 159            NOP

 160    L1:     LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18090140, file "app/services/learning/adaptive_memory_projection.py", line 160>)
                MAKE_FUNCTION
                LOAD_FAST                0 (rows)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
        L2:     NOT_TAKEN
        L3:     POP_TOP
                LOAD_CONST               4 (())
        L4:     GET_ITER
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (p)
                SWAP                     2
        L5:     BUILD_LIST               0
                SWAP                     2
        L6:     FOR_ITER                14 (to L9)
                STORE_FAST_LOAD_FAST    17 (p, p)
                TO_BOOL
        L7:     POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           12 (to L6)
        L8:     LOAD_FAST_BORROW         1 (p)
                LIST_APPEND              2
                JUMP_BACKWARD           16 (to L6)
        L9:     END_FOR
                POP_ITER
       L10:     SWAP                     2
                STORE_FAST               1 (p)
       L11:     RETURN_VALUE

  --   L12:     SWAP                     2
                POP_TOP

 160            SWAP                     2
                STORE_FAST               1 (p)
                RERAISE                  0

  --   L13:     PUSH_EXC_INFO

 161            LOAD_GLOBAL              0 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       56 (to L18)
                NOT_TAKEN
                STORE_FAST               2 (e)

 162   L14:     LOAD_GLOBAL              2 (logger)
                LOAD_ATTR                5 (warning + NULL|self)

 163            LOAD_CONST               2 ('project_tenant_bridge_list error type=')
                LOAD_GLOBAL              7 (type + NULL)
                LOAD_FAST                2 (e)
                CALL                     1
                LOAD_ATTR                8 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 162            CALL                     1
                POP_TOP

 165            BUILD_LIST               0
       L15:     SWAP                     2
       L16:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                RETURN_VALUE

  --   L17:     LOAD_CONST               3 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                RERAISE                  1

 161   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L13 [0]
  L3 to L5 -> L13 [0]
  L5 to L7 -> L12 [2]
  L8 to L10 -> L12 [2]
  L10 to L11 -> L13 [0]
  L12 to L13 -> L13 [0]
  L13 to L14 -> L19 [1] lasti
  L14 to L15 -> L17 [1] lasti
  L15 to L16 -> L19 [1] lasti
  L17 to L19 -> L19 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C18090140, file "app/services/learning/adaptive_memory_projection.py", line 160>:
 160           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (project_tenant_bridge_view + NULL)
               LOAD_FAST_BORROW         1 (r)
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
```
