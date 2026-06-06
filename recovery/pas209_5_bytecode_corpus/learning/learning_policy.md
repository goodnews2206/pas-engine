# learning/learning_policy

- **pyc:** `app\services\learning\__pycache__\learning_policy.cpython-314.pyc`
- **expected source path (absent):** `app\services\learning/learning_policy.py`
- **co_filename (from bytecode):** `app/services/learning/learning_policy.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** learning

## Module docstring

```
PAS179 — Manual / automatic learning-mode policy.

Resolves the *effective* learning mode for a brokerage. The
**default is MANUAL**; the AUTOMATIC_LOCKED mode is structurally
representable but PAS179 deliberately refuses to enable it.

Doctrine:

* **Manual default.** ``resolve_learning_mode`` returns
  ``MANUAL`` unless every gate below is satisfied.
* **Automatic locked by default.** Even with all gates open,
  PAS179 does NOT auto-approve memory and does NOT mutate live
  behavior; ``automatic_mode_allowed`` returns False unless an
  explicit operator unlock is wired into PAS180+.
* **Three independent gates required to *represent* automatic
  mode (not to enable it):**
    1. ``brokerage["learning_mode"]`` literally equals
       ``"AUTOMATIC_LOCKED"``.
    2. ``brokerage["features"]["adaptive_learning_enabled"]``
       is literally ``True``.
    3. The global env flag
       ``PAS_ADAPTIVE_LEARNING_AUTOMATIC_ENABLED`` reads
       literally ``"true"``.
* **NEVER raises.** All helpers return structural envelopes.
* **No PII / no secrets.** Envelopes carry only the mode + the
  bounded reason tokens for each gate decision.

Public surface:

  * ``resolve_learning_mode(brokerage)``       — manual/auto-locked token.
  * ``learning_mode_policy(brokerage)``        — structural verdict.
  * ``automatic_mode_allowed(brokerage)``      — False until PAS180+.
  * ``manual_mode_required(brokerage)``        — True except in
    fully-unlocked future configurations.
  * ``learning_policy_report(brokerage)``      — combined diagnostic.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `logging`, `os`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_brokerage_features`, `_global_env_flag_enabled`, `_resolve_brokerage_id`, `_safe_envelope`, `automatic_mode_allowed`, `learning_mode_policy`, `learning_policy_report`, `manual_mode_required`, `resolve_learning_mode`

## Env-key candidates

`AUTOMATIC_LOCKED`, `MANUAL`, `PAS_ADAPTIVE_LEARNING_AUTOMATIC_ENABLED`

## String constants (redacted where noted)

- '\nPAS179 — Manual / automatic learning-mode policy.\n\nResolves the *effective* learning mode for a brokerage. The\n**default is MANUAL**; the AUTOMATIC_LOCKED mode is structurally\nrepresentable but PAS179 deliberately refuses to enable it.\n\nDoctrine:\n\n* **Manual default.** ``resolve_learning_mode`` returns\n  ``MANUAL`` unless every gate below is satisfied.\n* **Automatic locked by default.** Even with all gates open,\n  PAS179 does NOT auto-approve memory and does NOT mutate live\n  behavior; ``automatic_mode_allowed`` returns False unless an\n  explicit operator unlock is wired into PAS180+.\n* **Three independent gates required to *represent* automatic\n  mode (not to enable it):**\n    1. ``brokerage["learning_mode"]`` literally equals\n       ``"AUTOMATIC_LOCKED"``.\n    2. ``brokerage["features"]["adaptive_learning_enabled"]``\n       is literally ``True``.\n    3. The global env flag\n       ``PAS_ADAPTIVE_LEARNING_AUTOMATIC_ENABLED`` reads\n       literally ``"true"``.\n* **NEVER raises.** All helpers return structural envelopes.\n* **No PII / no secrets.** Envelopes carry only the mode + the\n  bounded reason tokens for each gate decision.\n\nPublic surface:\n\n  * ``resolve_learning_mode(brokerage)``       — manual/auto-locked token.\n  * ``learning_mode_policy(brokerage)``        — structural verdict.\n  * ``automatic_mode_allowed(brokerage)``      — False until PAS180+.\n  * ``manual_mode_required(brokerage)``        — True except in\n    fully-unlocked future configurations.\n  * ``learning_policy_report(brokerage)``      — combined diagnostic.\n'
- 'pas.learning.policy'
- 'adaptive_learning_enabled'
- 'PAS_ADAPTIVE_LEARNING_AUTOMATIC_ENABLED'
- 'true'
- 'manual_default'
- 'brokerage_learning_mode_manual'
- 'brokerage_not_marked_automatic_locked'
- 'brokerage_adaptive_learning_feature_off'
- 'global_automatic_enable_env_flag_off'
- 'automatic_mode_represented_but_blocked'
- 'automatic_mode_fully_unlocked'
- 'invalid_brokerage'
- 'reasons'
- 'warnings'
- 'error_code'
- 'status'
- 'str'
- 'brokerage_id'
- 'Optional[str]'
- 'mode'
- 'automatic_allowed'
- 'bool'
- 'Optional[List[str]]'
- 'return'
- 'Dict[str, Any]'
- 'brokerage'
- 'Any'
- 'features'
- 'Strict-literal env flag check. NEVER raises.'
- 'Structural verdict on the brokerage\'s learning mode.\n\nOutcomes:\n  * ``mode="MANUAL"`` — the only mode PAS179 will use.\n  * ``mode="AUTOMATIC_LOCKED"`` — structurally representable\n    because every gate is open, but ``automatic_allowed``\n    STILL returns False; PAS179 never auto-acts.\n'
- 'failed'
- 'MANUAL'
- 'learning_mode'
- 'AUTOMATIC_LOCKED'
- 'Returns the bounded mode token. NEVER raises.'
- 'resolve_learning_mode error type='
- 'Returns whether automatic adaptation is allowed to *act*.\n\nPAS179 invariant: this ALWAYS returns False. A future\nPAS180+ surface may flip this to True under a separate\noperator unlock — PAS179 itself never does.\n'
- 'automatic_mode_allowed error type='
- 'Inverse of ``automatic_mode_allowed``. NEVER raises.'
- 'Diagnostic envelope. NEVER raises. NEVER returns PII.'
- 'learning_policy_report error type='
- 'unexpected:'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS179 — Manual / automatic learning-mode policy.\n\nResolves the *effective* learning mode for a brokerage. The\n**default is MANUAL**; the AUTOMATIC_LOCKED mode is structurally\nrepresentable but PAS179 deliberately refuses to enable it.\n\nDoctrine:\n\n* **Manual default.** ``resolve_learning_mode`` returns\n  ``MANUAL`` unless every gate below is satisfied.\n* **Automatic locked by default.** Even with all gates open,\n  PAS179 does NOT auto-approve memory and does NOT mutate live\n  behavior; ``automatic_mode_allowed`` returns False unless an\n  explicit operator unlock is wired into PAS180+.\n* **Three independent gates required to *represent* automatic\n  mode (not to enable it):**\n    1. ``brokerage["learning_mode"]`` literally equals\n       ``"AUTOMATIC_LOCKED"``.\n    2. ``brokerage["features"]["adaptive_learning_enabled"]``\n       is literally ``True``.\n    3. The global env flag\n       ``PAS_ADAPTIVE_LEARNING_AUTOMATIC_ENABLED`` reads\n       literally ``"true"``.\n* **NEVER raises.** All helpers return structural envelopes.\n* **No PII / no secrets.** Envelopes carry only the mode + the\n  bounded reason tokens for each gate decision.\n\nPublic surface:\n\n  * ``resolve_learning_mode(brokerage)``       — manual/auto-locked token.\n  * ``learning_mode_policy(brokerage)``        — structural verdict.\n  * ``automatic_mode_allowed(brokerage)``      — False until PAS180+.\n  * ``manual_mode_required(brokerage)``        — True except in\n    fully-unlocked future configurations.\n  * ``learning_policy_report(brokerage)``      — combined diagnostic.\n')
              STORE_NAME               0 (__doc__)

 39           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 41           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 42           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (os)
              STORE_NAME               4 (os)

 43           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              5 (typing)
              IMPORT_FROM              6 (Any)
              STORE_NAME               6 (Any)
              IMPORT_FROM              7 (Dict)
              STORE_NAME               7 (Dict)
              IMPORT_FROM              8 (List)
              STORE_NAME               8 (List)
              IMPORT_FROM              9 (Optional)
              STORE_NAME               9 (Optional)
              POP_TOP

 46           LOAD_NAME                3 (logging)
              LOAD_ATTR               20 (getLogger)
              PUSH_NULL
              LOAD_CONST               4 ('pas.learning.policy')
              CALL                     1
              STORE_NAME              11 (logger)

 53           LOAD_CONST              37 (('MANUAL', 'AUTOMATIC_LOCKED'))
              STORE_NAME              12 (ALLOWED_LEARNING_MODES)

 57           LOAD_CONST               5 ('adaptive_learning_enabled')
              STORE_NAME              13 (_BROKERAGE_ADAPTIVE_FLAG)

 62           LOAD_CONST               6 ('PAS_ADAPTIVE_LEARNING_AUTOMATIC_ENABLED')
              STORE_NAME              14 (_GLOBAL_ENV_FLAG)

 63           LOAD_CONST               7 ('true')
              STORE_NAME              15 (_GLOBAL_ENV_FLAG_ENABLED_LITERAL)

 66           LOAD_CONST               8 ('manual_default')
              STORE_NAME              16 (_REASON_DEFAULT_MANUAL)

 67           LOAD_CONST               9 ('brokerage_learning_mode_manual')
              STORE_NAME              17 (_REASON_BROKERAGE_LEARNING_MODE_MANUAL)

 68           LOAD_CONST              10 ('brokerage_not_marked_automatic_locked')
              STORE_NAME              18 (_REASON_BROKERAGE_NOT_AUTOMATIC_LOCKED)

 69           LOAD_CONST              11 ('brokerage_adaptive_learning_feature_off')
              STORE_NAME              19 (_REASON_BROKERAGE_FEATURE_FLAG_OFF)

 70           LOAD_CONST              12 ('global_automatic_enable_env_flag_off')
              STORE_NAME              20 (_REASON_GLOBAL_ENV_FLAG_OFF)

 71           LOAD_CONST              13 ('automatic_mode_represented_but_blocked')
              STORE_NAME              21 (_REASON_AUTOMATIC_REPRESENTED_BUT_BLOCKED)

 72           LOAD_CONST              14 ('automatic_mode_fully_unlocked')
              STORE_NAME              22 (_REASON_AUTOMATIC_FULLY_UNLOCKED)

 73           LOAD_CONST              15 ('invalid_brokerage')
              STORE_NAME              23 (_REASON_INVALID_BROKERAGE)

 76           LOAD_CONST              16 ('reasons')

 82           LOAD_CONST               2 (None)

 76           LOAD_CONST              17 ('warnings')

 83           LOAD_CONST               2 (None)

 76           LOAD_CONST              18 ('error_code')

 84           LOAD_CONST               2 (None)

 76           BUILD_MAP                3
              LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18090030, file "app/services/learning/learning_policy.py", line 76>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _safe_envelope at 0x0000018C17FE1920, file "app/services/learning/learning_policy.py", line 76>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              24 (_safe_envelope)

 97           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA3870, file "app/services/learning/learning_policy.py", line 97>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _resolve_brokerage_id at 0x0000018C1804CED0, file "app/services/learning/learning_policy.py", line 97>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_resolve_brokerage_id)

106           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA33C0, file "app/services/learning/learning_policy.py", line 106>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object _brokerage_features at 0x0000018C17972D90, file "app/services/learning/learning_policy.py", line 106>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_brokerage_features)

115           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA2100, file "app/services/learning/learning_policy.py", line 115>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object _global_env_flag_enabled at 0x0000018C1800AD80, file "app/services/learning/learning_policy.py", line 115>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_global_env_flag_enabled)

124           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA2C40, file "app/services/learning/learning_policy.py", line 124>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object learning_mode_policy at 0x0000018C17ED68D0, file "app/services/learning/learning_policy.py", line 124>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (learning_mode_policy)

189           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA2E20, file "app/services/learning/learning_policy.py", line 189>)
              MAKE_FUNCTION
              LOAD_CONST              30 (<code object resolve_learning_mode at 0x0000018C18048AB0, file "app/services/learning/learning_policy.py", line 189>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (resolve_learning_mode)

204           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA3A50, file "app/services/learning/learning_policy.py", line 204>)
              MAKE_FUNCTION
              LOAD_CONST              32 (<code object automatic_mode_allowed at 0x0000018C180606F0, file "app/services/learning/learning_policy.py", line 204>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (automatic_mode_allowed)

221           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C17FA2D30, file "app/services/learning/learning_policy.py", line 221>)
              MAKE_FUNCTION
              LOAD_CONST              34 (<code object manual_mode_required at 0x0000018C18025B30, file "app/services/learning/learning_policy.py", line 221>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (manual_mode_required)

226           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C17FA2880, file "app/services/learning/learning_policy.py", line 226>)
              MAKE_FUNCTION
              LOAD_CONST              36 (<code object learning_policy_report at 0x0000018C1801CBD0, file "app/services/learning/learning_policy.py", line 226>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (learning_policy_report)

245           BUILD_LIST               0
              LOAD_CONST              38 (('ALLOWED_LEARNING_MODES', 'learning_mode_policy', 'resolve_learning_mode', 'automatic_mode_allowed', 'manual_mode_required', 'learning_policy_report'))
              LIST_EXTEND              1
              STORE_NAME              33 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18090030, file "app/services/learning/learning_policy.py", line 76>:
 76           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

 78           LOAD_CONST               2 ('str')

 76           LOAD_CONST               3 ('brokerage_id')

 79           LOAD_CONST               4 ('Optional[str]')

 76           LOAD_CONST               5 ('mode')

 80           LOAD_CONST               2 ('str')

 76           LOAD_CONST               6 ('automatic_allowed')

 81           LOAD_CONST               7 ('bool')

 76           LOAD_CONST               8 ('reasons')

 82           LOAD_CONST               9 ('Optional[List[str]]')

 76           LOAD_CONST              10 ('warnings')

 83           LOAD_CONST               9 ('Optional[List[str]]')

 76           LOAD_CONST              11 ('error_code')

 84           LOAD_CONST               4 ('Optional[str]')

 76           LOAD_CONST              12 ('return')

 85           LOAD_CONST              13 ('Dict[str, Any]')

 76           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C17FE1920, file "app/services/learning/learning_policy.py", line 76>:
 76           RESUME                   0

 87           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

 88           LOAD_CONST               1 ('brokerage_id')
              LOAD_FAST                1 (brokerage_id)

 89           LOAD_CONST               2 ('mode')
              LOAD_FAST                2 (mode)

 90           LOAD_CONST               3 ('automatic_allowed')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         3 (automatic_allowed)
              CALL                     1

 91           LOAD_CONST               4 ('reasons')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                4 (reasons)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

 92           LOAD_CONST               5 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                5 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L2:     CALL                     1

 93           LOAD_CONST               6 ('error_code')
              LOAD_FAST_BORROW         6 (error_code)

 86           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app/services/learning/learning_policy.py", line 97>:
 97           RESUME                   0
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

Disassembly of <code object _resolve_brokerage_id at 0x0000018C1804CED0, file "app/services/learning/learning_policy.py", line 97>:
 97           RESUME                   0

 98           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 99           LOAD_CONST               0 (None)
              RETURN_VALUE

100   L1:     LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('id')
              CALL                     1
              STORE_FAST               1 (bid)

101           LOAD_GLOBAL              1 (isinstance + NULL)
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

102   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

103   L3:     LOAD_FAST_BORROW         1 (bid)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app/services/learning/learning_policy.py", line 106>:
106           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _brokerage_features at 0x0000018C17972D90, file "app/services/learning/learning_policy.py", line 106>:
106           RESUME                   0

107           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

108           BUILD_MAP                0
              RETURN_VALUE

109   L1:     LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               0 ('features')
              CALL                     1
              STORE_FAST               1 (feats)

110           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (feats)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

111           LOAD_FAST_BORROW         1 (feats)
              RETURN_VALUE

112   L2:     BUILD_MAP                0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app/services/learning/learning_policy.py", line 115>:
115           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('bool')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _global_env_flag_enabled at 0x0000018C1800AD80, file "app/services/learning/learning_policy.py", line 115>:
 115           RESUME                   0

 117           NOP

 118   L1:     LOAD_GLOBAL              0 (os)
               LOAD_ATTR                2 (environ)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_GLOBAL              6 (_GLOBAL_ENV_FLAG)
               LOAD_CONST               1 ('')
               CALL                     2
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
       L2:     NOT_TAKEN
       L3:     POP_TOP
               LOAD_CONST               1 ('')
       L4:     STORE_FAST               0 (v)

 121   L5:     LOAD_FAST                0 (v)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               LOAD_GLOBAL             12 (_GLOBAL_ENV_FLAG_ENABLED_LITERAL)
               COMPARE_OP              72 (==)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

 119           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

 120   L7:     POP_EXCEPT
               LOAD_CONST               2 (False)
               RETURN_VALUE

 119   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L6 [0]
  L3 to L5 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app/services/learning/learning_policy.py", line 124>:
124           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object learning_mode_policy at 0x0000018C17ED68D0, file "app/services/learning/learning_policy.py", line 124>:
124            RESUME                   0

133            LOAD_GLOBAL              1 (_resolve_brokerage_id + NULL)
               LOAD_FAST_BORROW         0 (brokerage)
               CALL                     1
               STORE_FAST               1 (bid)

134            LOAD_FAST_BORROW         1 (bid)
               POP_JUMP_IF_NOT_NONE    27 (to L1)
               NOT_TAKEN

135            LOAD_GLOBAL              3 (_safe_envelope + NULL)

136            LOAD_CONST               2 ('failed')

137            LOAD_CONST               1 (None)

138            LOAD_CONST               3 ('MANUAL')

139            LOAD_CONST               4 (False)

140            LOAD_GLOBAL              4 (_REASON_INVALID_BROKERAGE)
               BUILD_LIST               1

141            LOAD_GLOBAL              4 (_REASON_INVALID_BROKERAGE)

135            LOAD_CONST               5 (('status', 'brokerage_id', 'mode', 'automatic_allowed', 'reasons', 'error_code'))
               CALL_KW                  6
               RETURN_VALUE

144    L1:     BUILD_LIST               0
               STORE_FAST               2 (reasons)

147            LOAD_GLOBAL              7 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (brokerage)
               LOAD_GLOBAL              8 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L2)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (brokerage)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_CONST               6 ('learning_mode')
               CALL                     1
               JUMP_FORWARD             1 (to L3)
       L2:     LOAD_CONST               1 (None)
       L3:     STORE_FAST               3 (declared)

149            LOAD_GLOBAL              7 (isinstance + NULL)
               LOAD_FAST_BORROW         3 (declared)
               LOAD_GLOBAL             12 (str)
               CALL                     2
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       20 (to L4)
               NOT_TAKEN
               POP_TOP

150            LOAD_FAST_BORROW         3 (declared)
               LOAD_ATTR               15 (strip + NULL|self)
               CALL                     0
               LOAD_CONST               7 ('AUTOMATIC_LOCKED')
               COMPARE_OP              72 (==)

148    L4:     STORE_FAST               4 (gate_1_open)

152            LOAD_FAST_BORROW         4 (gate_1_open)
               TO_BOOL
               POP_JUMP_IF_TRUE        22 (to L5)
               NOT_TAKEN

153            LOAD_FAST_BORROW         2 (reasons)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             18 (_REASON_BROKERAGE_NOT_AUTOMATIC_LOCKED)
               CALL                     1
               POP_TOP

156    L5:     LOAD_GLOBAL             21 (_brokerage_features + NULL)
               LOAD_FAST_BORROW         0 (brokerage)
               CALL                     1
               STORE_FAST               5 (feats)

157            LOAD_FAST_BORROW         5 (feats)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_GLOBAL             22 (_BROKERAGE_ADAPTIVE_FLAG)
               CALL                     1
               LOAD_CONST               8 (True)
               IS_OP                    0 (is)
               STORE_FAST               6 (gate_2_open)

158            LOAD_FAST_BORROW         6 (gate_2_open)
               TO_BOOL
               POP_JUMP_IF_TRUE        22 (to L6)
               NOT_TAKEN

159            LOAD_FAST_BORROW         2 (reasons)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             24 (_REASON_BROKERAGE_FEATURE_FLAG_OFF)
               CALL                     1
               POP_TOP

162    L6:     LOAD_GLOBAL             27 (_global_env_flag_enabled + NULL)
               CALL                     0
               STORE_FAST               7 (gate_3_open)

163            LOAD_FAST_BORROW         7 (gate_3_open)
               TO_BOOL
               POP_JUMP_IF_TRUE        22 (to L7)
               NOT_TAKEN

164            LOAD_FAST_BORROW         2 (reasons)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             28 (_REASON_GLOBAL_ENV_FLAG_OFF)
               CALL                     1
               POP_TOP

166    L7:     LOAD_FAST                4 (gate_1_open)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       13 (to L8)
               NOT_TAKEN
               POP_TOP
               LOAD_FAST                6 (gate_2_open)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               POP_TOP
               LOAD_FAST                7 (gate_3_open)
       L8:     STORE_FAST               8 (all_gates_open)

167            LOAD_FAST_BORROW         8 (all_gates_open)
               TO_BOOL
               POP_JUMP_IF_TRUE        32 (to L10)
               NOT_TAKEN

168            LOAD_GLOBAL              3 (_safe_envelope + NULL)

169            LOAD_CONST               9 ('ok')

170            LOAD_FAST                1 (bid)

171            LOAD_CONST               3 ('MANUAL')

172            LOAD_CONST               4 (False)

173            LOAD_FAST                2 (reasons)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         8 (to L9)
               NOT_TAKEN
               POP_TOP
               LOAD_GLOBAL             30 (_REASON_DEFAULT_MANUAL)
               BUILD_LIST               1

168    L9:     LOAD_CONST              10 (('status', 'brokerage_id', 'mode', 'automatic_allowed', 'reasons'))
               CALL_KW                  5
               RETURN_VALUE

180   L10:     LOAD_GLOBAL              3 (_safe_envelope + NULL)

181            LOAD_CONST               9 ('ok')

182            LOAD_FAST_BORROW         1 (bid)

183            LOAD_CONST               7 ('AUTOMATIC_LOCKED')

184            LOAD_CONST               4 (False)

185            LOAD_GLOBAL             32 (_REASON_AUTOMATIC_REPRESENTED_BUT_BLOCKED)
               BUILD_LIST               1

180            LOAD_CONST              10 (('status', 'brokerage_id', 'mode', 'automatic_allowed', 'reasons'))
               CALL_KW                  5
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app/services/learning/learning_policy.py", line 189>:
189           RESUME                   0
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
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object resolve_learning_mode at 0x0000018C18048AB0, file "app/services/learning/learning_policy.py", line 189>:
 189           RESUME                   0

 191           NOP

 192   L1:     LOAD_GLOBAL              1 (learning_mode_policy + NULL)
               LOAD_FAST_BORROW         0 (brokerage)
               CALL                     1
               STORE_FAST               1 (verdict)

 198   L2:     LOAD_FAST                1 (verdict)
               LOAD_ATTR               13 (get + NULL|self)
               LOAD_CONST               4 ('mode')
               CALL                     1
               STORE_FAST               3 (mode)

 199           LOAD_FAST                3 (mode)
               LOAD_GLOBAL             14 (ALLOWED_LEARNING_MODES)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 200           LOAD_FAST                3 (mode)
               RETURN_VALUE

 201   L3:     LOAD_CONST               3 ('MANUAL')
               RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

 193           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L8)
               NOT_TAKEN
               STORE_FAST               2 (e)

 194   L5:     LOAD_GLOBAL              4 (logger)
               LOAD_ATTR                7 (warning + NULL|self)

 195           LOAD_CONST               1 ('resolve_learning_mode error type=')
               LOAD_GLOBAL              9 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               10 (__name__)
               FORMAT_SIMPLE
               BUILD_STRING             2

 194           CALL                     1
               POP_TOP

 197   L6:     POP_EXCEPT
               LOAD_CONST               2 (None)
               STORE_FAST               2 (e)
               DELETE_FAST              2 (e)
               LOAD_CONST               3 ('MANUAL')
               RETURN_VALUE

  --   L7:     LOAD_CONST               2 (None)
               STORE_FAST               2 (e)
               DELETE_FAST              2 (e)
               RERAISE                  1

 193   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L4 [0]
  L4 to L5 -> L9 [1] lasti
  L5 to L6 -> L7 [1] lasti
  L7 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app/services/learning/learning_policy.py", line 204>:
204           RESUME                   0
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
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object automatic_mode_allowed at 0x0000018C180606F0, file "app/services/learning/learning_policy.py", line 204>:
 204           RESUME                   0

 211           NOP

 212   L1:     LOAD_GLOBAL              1 (learning_mode_policy + NULL)
               LOAD_FAST_BORROW         0 (brokerage)
               CALL                     1
               STORE_FAST               1 (verdict)

 218   L2:     LOAD_GLOBAL             13 (bool + NULL)
               LOAD_FAST                1 (verdict)
               LOAD_ATTR               15 (get + NULL|self)
               LOAD_CONST               4 ('automatic_allowed')
               LOAD_CONST               3 (False)
               CALL                     2
               CALL                     1
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 213           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 214   L4:     LOAD_GLOBAL              4 (logger)
               LOAD_ATTR                7 (warning + NULL|self)

 215           LOAD_CONST               1 ('automatic_mode_allowed error type=')
               LOAD_GLOBAL              9 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               10 (__name__)
               FORMAT_SIMPLE
               BUILD_STRING             2

 214           CALL                     1
               POP_TOP

 217   L5:     POP_EXCEPT
               LOAD_CONST               2 (None)
               STORE_FAST               2 (e)
               DELETE_FAST              2 (e)
               LOAD_CONST               3 (False)
               RETURN_VALUE

  --   L6:     LOAD_CONST               2 (None)
               STORE_FAST               2 (e)
               DELETE_FAST              2 (e)
               RERAISE                  1

 213   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app/services/learning/learning_policy.py", line 221>:
221           RESUME                   0
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
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object manual_mode_required at 0x0000018C18025B30, file "app/services/learning/learning_policy.py", line 221>:
221           RESUME                   0

223           LOAD_GLOBAL              1 (automatic_mode_allowed + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              CALL                     1
              TO_BOOL
              UNARY_NOT
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app/services/learning/learning_policy.py", line 226>:
226           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object learning_policy_report at 0x0000018C1801CBD0, file "app/services/learning/learning_policy.py", line 226>:
 226           RESUME                   0

 228           NOP

 229   L1:     LOAD_GLOBAL              1 (learning_mode_policy + NULL)
               LOAD_FAST_BORROW         0 (brokerage)
               CALL                     1
               STORE_FAST               1 (verdict)

 242   L2:     LOAD_FAST_BORROW         1 (verdict)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 230           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE      116 (to L8)
               NOT_TAKEN
               STORE_FAST               2 (e)

 231   L4:     LOAD_GLOBAL              4 (logger)
               LOAD_ATTR                7 (warning + NULL|self)

 232           LOAD_CONST               1 ('learning_policy_report error type=')
               LOAD_GLOBAL              9 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               10 (__name__)
               FORMAT_SIMPLE
               BUILD_STRING             2

 231           CALL                     1
               POP_TOP

 234           LOAD_GLOBAL             13 (_safe_envelope + NULL)

 235           LOAD_CONST               2 ('failed')

 236           LOAD_CONST               3 (None)

 237           LOAD_CONST               4 ('MANUAL')

 238           LOAD_CONST               5 (False)

 239           LOAD_CONST               6 ('unexpected:')
               LOAD_GLOBAL              9 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               10 (__name__)
               FORMAT_SIMPLE
               BUILD_STRING             2
               BUILD_LIST               1

 240           LOAD_CONST               6 ('unexpected:')
               LOAD_GLOBAL              9 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               10 (__name__)
               FORMAT_SIMPLE
               BUILD_STRING             2

 234           LOAD_CONST               7 (('status', 'brokerage_id', 'mode', 'automatic_allowed', 'warnings', 'error_code'))
               CALL_KW                  6
       L5:     SWAP                     2
       L6:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               2 (e)
               DELETE_FAST              2 (e)
               RETURN_VALUE

  --   L7:     LOAD_CONST               3 (None)
               STORE_FAST               2 (e)
               DELETE_FAST              2 (e)
               RERAISE                  1

 230   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L9 [1] lasti
  L4 to L5 -> L7 [1] lasti
  L5 to L6 -> L9 [1] lasti
  L7 to L9 -> L9 [1] lasti
```
