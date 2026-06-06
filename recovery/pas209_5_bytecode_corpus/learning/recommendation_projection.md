# learning/recommendation_projection

- **pyc:** `app\services\learning\__pycache__\recommendation_projection.cpython-314.pyc`
- **expected source path (absent):** `app\services\learning/recommendation_projection.py`
- **co_filename (from bytecode):** `app/services/learning/recommendation_projection.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** learning

## Module docstring

```
PAS180 — Safe projections for learning recommendation records.

Renders a raw `pas_learning_recommendations` row into two
closed-shape envelopes:

* ``project_operator_view(row)`` — operator dashboard projection.
* ``project_tenant_view(row)``   — tenant-portal projection.

Doctrine:

* **Closed allow-lists.** Both projections are explicit — any
  field outside the allow-list is dropped. Forbidden fields
  (rationale_text / raw_payload / transcript / phone / email /
  signature / env_value / secret) are NEVER reachable because
  the v28 schema doesn't store them in the first place; the
  projection layer is defence-in-depth.
* **Tenant projection excludes:** ``brokerage_id`` (tenant
  resolves their own from auth — projection deliberately
  drops the column), ``source_id``, ``recommended_action``,
  ``rationale_token``, ``metadata``, ``reviewed_by_actor_type``,
  ``reviewed_by_actor_id``, ``warning_count`` (operator-only
  internals).
* **NEVER raises.**
```

## Imports

`Any`, `Dict`, `Iterable`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `logging`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_is_safe_value`, `_key_is_forbidden`, `project_operator_list`, `project_operator_view`, `project_tenant_list`, `project_tenant_view`

## Env-key candidates

`OPERATOR_PROJECTION_KEYS`, `PROJECTION_FORBIDDEN_KEYS`, `TENANT_PROJECTION_KEYS`

## String constants (redacted where noted)

- "\nPAS180 — Safe projections for learning recommendation records.\n\nRenders a raw `pas_learning_recommendations` row into two\nclosed-shape envelopes:\n\n* ``project_operator_view(row)`` — operator dashboard projection.\n* ``project_tenant_view(row)``   — tenant-portal projection.\n\nDoctrine:\n\n* **Closed allow-lists.** Both projections are explicit — any\n  field outside the allow-list is dropped. Forbidden fields\n  (rationale_text / raw_payload / transcript / phone / email /\n  signature / env_value / secret) are NEVER reachable because\n  the v28 schema doesn't store them in the first place; the\n  projection layer is defence-in-depth.\n* **Tenant projection excludes:** ``brokerage_id`` (tenant\n  resolves their own from auth — projection deliberately\n  drops the column), ``source_id``, ``recommended_action``,\n  ``rationale_token``, ``metadata``, ``reviewed_by_actor_type``,\n  ``reviewed_by_actor_id``, ``warning_count`` (operator-only\n  internals).\n* **NEVER raises.**\n"
- 'pas.learning.recommendation_projection'
- 'Tuple[str, ...]'
- 'OPERATOR_PROJECTION_KEYS'
- 'TENANT_PROJECTION_KEYS'
- 'PROJECTION_FORBIDDEN_KEYS'
- 'Any'
- 'return'
- 'bool'
- 'Closed-shape primitive: bool / int / float / None /\nbounded string. Lists / dicts are not allowed in projections.'
- 'row'
- 'Dict[str, Any]'
- 'Render a row for the operator dashboard. NEVER raises.'
- 'project_operator_view error type='
- 'Render a row for the tenant portal. NEVER raises.\nNEVER carries operator actor ids / source_id /\nrationale_token / metadata.'
- 'project_tenant_view error type='
- 'rows'
- 'Iterable[Any]'
- 'List[Dict[str, Any]]'
- 'Map ``project_operator_view`` over a row list. NEVER raises.'
- 'project_operator_list error type='
- 'Map ``project_tenant_view`` over a row list. NEVER raises.'
- 'project_tenant_list error type='

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ("\nPAS180 — Safe projections for learning recommendation records.\n\nRenders a raw `pas_learning_recommendations` row into two\nclosed-shape envelopes:\n\n* ``project_operator_view(row)`` — operator dashboard projection.\n* ``project_tenant_view(row)``   — tenant-portal projection.\n\nDoctrine:\n\n* **Closed allow-lists.** Both projections are explicit — any\n  field outside the allow-list is dropped. Forbidden fields\n  (rationale_text / raw_payload / transcript / phone / email /\n  signature / env_value / secret) are NEVER reachable because\n  the v28 schema doesn't store them in the first place; the\n  projection layer is defence-in-depth.\n* **Tenant projection excludes:** ``brokerage_id`` (tenant\n  resolves their own from auth — projection deliberately\n  drops the column), ``source_id``, ``recommended_action``,\n  ``rationale_token``, ``metadata``, ``reviewed_by_actor_type``,\n  ``reviewed_by_actor_id``, ``warning_count`` (operator-only\n  internals).\n* **NEVER raises.**\n")
               STORE_NAME               1 (__doc__)

  27           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  29           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  30           LOAD_SMALL_INT           0
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

  33           LOAD_NAME                4 (logging)
               LOAD_ATTR               24 (getLogger)
               PUSH_NULL
               LOAD_CONST               4 ('pas.learning.recommendation_projection')
               CALL                     1
               STORE_NAME              13 (logger)

  37           LOAD_CONST              21 (('recommendation_id', 'brokerage_id', 'recommendation_type', 'source_type', 'source_id', 'status', 'confidence_score', 'risk_score', 'usefulness_score', 'recommended_action', 'rationale_token', 'created_at', 'reviewed_at', 'warning_count'))
               STORE_NAME              14 (OPERATOR_PROJECTION_KEYS)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               15 (__annotations__)
               LOAD_CONST               6 ('OPERATOR_PROJECTION_KEYS')
               STORE_SUBSCR

  58           LOAD_CONST              22 (('recommendation_id', 'recommendation_type', 'status', 'confidence_score', 'risk_score', 'usefulness_score', 'created_at', 'reviewed_at'))
               STORE_NAME              16 (TENANT_PROJECTION_KEYS)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               15 (__annotations__)
               LOAD_CONST               7 ('TENANT_PROJECTION_KEYS')
               STORE_SUBSCR

  72           LOAD_CONST              23 (('phone', 'email', 'name', 'raw_payload', 'raw_email', 'raw_body', 'transcript', 'summary', 'summary_text', 'secret', 'signature', 'env_value', 'env_values', 'dedupe_key', 'callback_notes', 'rationale_text', 'rationale_freeform', 'prompt', 'prompt_text', 'live_mutation_payload'))
               STORE_NAME              17 (PROJECTION_FORBIDDEN_KEYS)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               15 (__annotations__)
               LOAD_CONST               8 ('PROJECTION_FORBIDDEN_KEYS')
               STORE_SUBSCR

  84           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA33C0, file "app/services/learning/recommendation_projection.py", line 84>)
               MAKE_FUNCTION
               LOAD_CONST              10 (<code object _is_safe_value at 0x0000018C17FF13B0, file "app/services/learning/recommendation_projection.py", line 84>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              18 (_is_safe_value)

  94           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA2100, file "app/services/learning/recommendation_projection.py", line 94>)
               MAKE_FUNCTION
               LOAD_CONST              12 (<code object _key_is_forbidden at 0x0000018C17972550, file "app/services/learning/recommendation_projection.py", line 94>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              19 (_key_is_forbidden)

 104           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA2C40, file "app/services/learning/recommendation_projection.py", line 104>)
               MAKE_FUNCTION
               LOAD_CONST              14 (<code object project_operator_view at 0x0000018C17ED4B40, file "app/services/learning/recommendation_projection.py", line 104>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              20 (project_operator_view)

 123           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA2E20, file "app/services/learning/recommendation_projection.py", line 123>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object project_tenant_view at 0x0000018C17ED4D70, file "app/services/learning/recommendation_projection.py", line 123>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              21 (project_tenant_view)

 144           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA3690, file "app/services/learning/recommendation_projection.py", line 144>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object project_operator_list at 0x0000018C18048730, file "app/services/learning/recommendation_projection.py", line 144>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              22 (project_operator_list)

 155           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA34B0, file "app/services/learning/recommendation_projection.py", line 155>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object project_tenant_list at 0x0000018C180488F0, file "app/services/learning/recommendation_projection.py", line 155>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              23 (project_tenant_list)

 166           BUILD_LIST               0
               LOAD_CONST              24 (('OPERATOR_PROJECTION_KEYS', 'TENANT_PROJECTION_KEYS', 'PROJECTION_FORBIDDEN_KEYS', 'project_operator_view', 'project_tenant_view', 'project_operator_list', 'project_tenant_list'))
               LIST_EXTEND              1
               STORE_NAME              24 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app/services/learning/recommendation_projection.py", line 84>:
 84           RESUME                   0
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

Disassembly of <code object _is_safe_value at 0x0000018C17FF13B0, file "app/services/learning/recommendation_projection.py", line 84>:
 84           RESUME                   0

 87           LOAD_FAST_BORROW         0 (v)
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

 88   L1:     LOAD_CONST               1 (True)
              RETURN_VALUE

 89   L2:     LOAD_GLOBAL              1 (isinstance + NULL)
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

 90           LOAD_CONST               1 (True)
              RETURN_VALUE

 91   L3:     LOAD_CONST               3 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app/services/learning/recommendation_projection.py", line 94>:
 94           RESUME                   0
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

Disassembly of <code object _key_is_forbidden at 0x0000018C17972550, file "app/services/learning/recommendation_projection.py", line 94>:
 94           RESUME                   0

 95           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (k)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 96           LOAD_CONST               0 (False)
              RETURN_VALUE

 97   L1:     LOAD_FAST_BORROW         0 (k)
              LOAD_ATTR                5 (lower + NULL|self)
              CALL                     0
              STORE_FAST               1 (kl)

 98           LOAD_GLOBAL              6 (PROJECTION_FORBIDDEN_KEYS)
              GET_ITER
      L2:     FOR_ITER                12 (to L4)
              STORE_FAST               2 (forb)

 99           LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (forb, kl)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

100   L3:     POP_TOP
              LOAD_CONST               1 (True)
              RETURN_VALUE

 98   L4:     END_FOR
              POP_ITER

101           LOAD_CONST               0 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app/services/learning/recommendation_projection.py", line 104>:
104           RESUME                   0
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

Disassembly of <code object project_operator_view at 0x0000018C17ED4B40, file "app/services/learning/recommendation_projection.py", line 104>:
 104            RESUME                   0

 106            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (row)
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

 110    L2:     LOAD_GLOBAL              4 (OPERATOR_PROJECTION_KEYS)
                GET_ITER
        L3:     FOR_ITER                61 (to L10)
                STORE_FAST               2 (k)

 111            LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, row)
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

 112    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, k)
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

 118            LOAD_CONST               1 ('project_operator_view error type=')
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app/services/learning/recommendation_projection.py", line 123>:
123           RESUME                   0
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

Disassembly of <code object project_tenant_view at 0x0000018C17ED4D70, file "app/services/learning/recommendation_projection.py", line 123>:
 123            RESUME                   0

 127            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (row)
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

 131    L2:     LOAD_GLOBAL              4 (TENANT_PROJECTION_KEYS)
                GET_ITER
        L3:     FOR_ITER                61 (to L10)
                STORE_FAST               2 (k)

 132            LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, row)
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

 133    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, k)
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

 139            LOAD_CONST               1 ('project_tenant_view error type=')
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app/services/learning/recommendation_projection.py", line 144>:
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

Disassembly of <code object project_operator_list at 0x0000018C18048730, file "app/services/learning/recommendation_projection.py", line 144>:
 144            RESUME                   0

 146            NOP

 147    L1:     LOAD_CONST               1 (<code object <genexpr> at 0x0000018C180908B0, file "app/services/learning/recommendation_projection.py", line 147>)
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

 147            SWAP                     2
                STORE_FAST               1 (p)
                RERAISE                  0

  --   L13:     PUSH_EXC_INFO

 148            LOAD_GLOBAL              0 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       56 (to L18)
                NOT_TAKEN
                STORE_FAST               2 (e)

 149   L14:     LOAD_GLOBAL              2 (logger)
                LOAD_ATTR                5 (warning + NULL|self)

 150            LOAD_CONST               2 ('project_operator_list error type=')
                LOAD_GLOBAL              7 (type + NULL)
                LOAD_FAST                2 (e)
                CALL                     1
                LOAD_ATTR                8 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 149            CALL                     1
                POP_TOP

 152            BUILD_LIST               0
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

 148   L18:     RERAISE                  0

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

Disassembly of <code object <genexpr> at 0x0000018C180908B0, file "app/services/learning/recommendation_projection.py", line 147>:
 147           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (project_operator_view + NULL)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app/services/learning/recommendation_projection.py", line 155>:
155           RESUME                   0
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

Disassembly of <code object project_tenant_list at 0x0000018C180488F0, file "app/services/learning/recommendation_projection.py", line 155>:
 155            RESUME                   0

 157            NOP

 158    L1:     LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18090360, file "app/services/learning/recommendation_projection.py", line 158>)
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

 158            SWAP                     2
                STORE_FAST               1 (p)
                RERAISE                  0

  --   L13:     PUSH_EXC_INFO

 159            LOAD_GLOBAL              0 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       56 (to L18)
                NOT_TAKEN
                STORE_FAST               2 (e)

 160   L14:     LOAD_GLOBAL              2 (logger)
                LOAD_ATTR                5 (warning + NULL|self)

 161            LOAD_CONST               2 ('project_tenant_list error type=')
                LOAD_GLOBAL              7 (type + NULL)
                LOAD_FAST                2 (e)
                CALL                     1
                LOAD_ATTR                8 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 160            CALL                     1
                POP_TOP

 163            BUILD_LIST               0
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

 159   L18:     RERAISE                  0

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

Disassembly of <code object <genexpr> at 0x0000018C18090360, file "app/services/learning/recommendation_projection.py", line 158>:
 158           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (project_tenant_view + NULL)
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
