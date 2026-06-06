# learning/manual_test_scoring

- **pyc:** `app\services\learning\__pycache__\manual_test_scoring.cpython-314.pyc`
- **expected source path (absent):** `app\services\learning/manual_test_scoring.py`
- **co_filename (from bytecode):** `app/services/learning/manual_test_scoring.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** learning

## Module docstring

```
PAS181 — Deterministic manual-test scoring.

Pure-Python deterministic scoring for manual-test runs. No
LLM, no embedding, no external state.

Doctrine:

* **Deterministic.** Same inputs → byte-identical scores.
* **Bounded.** Every score is clamped to [0, 1].
* **No external calls.** Pure functions only.
* **Fail-closed on malformed input.** Returns
  ``status="failed"`` with ``error_code`` and ``score=0.0``;
  no exception escapes.
* **Risk cannot be hidden.** The overall score is multiplied
  by ``(1 - risk_delta)`` so a high risk_score directly
  attenuates the overall score. A separate
  ``escalation_required`` boolean is set when the risk
  exceeds the high-risk threshold.

Public surface:

  * ``HIGH_RISK_THRESHOLD``               — closed numeric constant.
  * ``score_manual_test_result(...)``     — combined score envelope.
  * ``score_risk_delta(...)``             — structural risk score.
  * ``score_usefulness_delta(...)``       — structural usefulness score.
  * ``score_confidence_delta(...)``       — structural confidence score.
```

## Imports

`Any`, `Dict`, `Optional`, `__future__`, `annotations`, `logging`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp01`, `_nonneg_int`, `_safe_envelope`, `score_confidence_delta`, `score_manual_test_result`, `score_risk_delta`, `score_usefulness_delta`

## Env-key candidates

`HIGH_RISK_THRESHOLD`, `SIMULATION_ONLY`

## String constants (redacted where noted)

- '\nPAS181 — Deterministic manual-test scoring.\n\nPure-Python deterministic scoring for manual-test runs. No\nLLM, no embedding, no external state.\n\nDoctrine:\n\n* **Deterministic.** Same inputs → byte-identical scores.\n* **Bounded.** Every score is clamped to [0, 1].\n* **No external calls.** Pure functions only.\n* **Fail-closed on malformed input.** Returns\n  ``status="failed"`` with ``error_code`` and ``score=0.0``;\n  no exception escapes.\n* **Risk cannot be hidden.** The overall score is multiplied\n  by ``(1 - risk_delta)`` so a high risk_score directly\n  attenuates the overall score. A separate\n  ``escalation_required`` boolean is set when the risk\n  exceeds the high-risk threshold.\n\nPublic surface:\n\n  * ``HIGH_RISK_THRESHOLD``               — closed numeric constant.\n  * ``score_manual_test_result(...)``     — combined score envelope.\n  * ``score_risk_delta(...)``             — structural risk score.\n  * ``score_usefulness_delta(...)``       — structural usefulness score.\n  * ``score_confidence_delta(...)``       — structural confidence score.\n'
- 'pas.learning.manual_test_scoring'
- 'float'
- 'HIGH_RISK_THRESHOLD'
- '_SIMULATION_CONFIDENCE_DISCOUNT'
- '_WARNING_RISK_INCREMENT'
- 'score'
- 'components'
- 'escalation_required'
- 'error_code'
- 'warning_count'
- 'mode'
- 'SIMULATION_ONLY'
- 'value'
- 'Any'
- 'default'
- 'return'
- 'Clamp a value to [0, 1]. NEVER raises. Returns\n``default`` on malformed input.'
- 'int'
- 'status'
- 'str'
- 'Optional[Dict[str, float]]'
- 'bool'
- 'Optional[str]'
- 'Dict[str, Any]'
- 'recommendation'
- "Deterministic risk_delta in [0, 1]. NEVER raises.\n\nReturns the recommendation's risk_score plus a small\nwarning-count penalty. Caps at 1.0 so the score-mix\nnever produces nonsensical negative or > 1 results."
- 'failed'
- 'invalid_recommendation'
- 'risk_score'
- "Deterministic usefulness_delta. NEVER raises.\n\nFor PAS181 the usefulness signal is the recommendation's\nown usefulness_score, *not* a fresh measurement. Future\nPAS phases may compute a true delta against historical\noutcomes; PAS181 deliberately doesn't."
- 'usefulness_score'
- "Deterministic confidence_delta. NEVER raises.\n\nThe recommendation's confidence_score, optionally\ndiscounted because we're in simulation mode (not live)."
- 'confidence_score'
- 'Combined deterministic score. NEVER raises. NEVER\ncalls an LLM. Returns:\n\n    {\n      "status":              "ok"|"failed",\n      "score":               <float [0, 1]>,\n      "components":          {\n          "risk":       <float>,\n          "usefulness": <float>,\n          "confidence": <float>,\n      },\n      "escalation_required": <bool>,\n      "error_code":          None|str,\n    }\n'
- 'invalid_mode'
- 'component_score_failed'
- 'risk'
- 'usefulness'
- 'confidence'
- 'score_manual_test_result unexpected error type='
- 'unexpected:'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS181 — Deterministic manual-test scoring.\n\nPure-Python deterministic scoring for manual-test runs. No\nLLM, no embedding, no external state.\n\nDoctrine:\n\n* **Deterministic.** Same inputs → byte-identical scores.\n* **Bounded.** Every score is clamped to [0, 1].\n* **No external calls.** Pure functions only.\n* **Fail-closed on malformed input.** Returns\n  ``status="failed"`` with ``error_code`` and ``score=0.0``;\n  no exception escapes.\n* **Risk cannot be hidden.** The overall score is multiplied\n  by ``(1 - risk_delta)`` so a high risk_score directly\n  attenuates the overall score. A separate\n  ``escalation_required`` boolean is set when the risk\n  exceeds the high-risk threshold.\n\nPublic surface:\n\n  * ``HIGH_RISK_THRESHOLD``               — closed numeric constant.\n  * ``score_manual_test_result(...)``     — combined score envelope.\n  * ``score_risk_delta(...)``             — structural risk score.\n  * ``score_usefulness_delta(...)``       — structural usefulness score.\n  * ``score_confidence_delta(...)``       — structural confidence score.\n')
               STORE_NAME               1 (__doc__)

  30           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  32           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  33           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('Any', 'Dict', 'Optional'))
               IMPORT_NAME              5 (typing)
               IMPORT_FROM              6 (Any)
               STORE_NAME               6 (Any)
               IMPORT_FROM              7 (Dict)
               STORE_NAME               7 (Dict)
               IMPORT_FROM              8 (Optional)
               STORE_NAME               8 (Optional)
               POP_TOP

  36           LOAD_NAME                4 (logging)
               LOAD_ATTR               18 (getLogger)
               PUSH_NULL
               LOAD_CONST               4 ('pas.learning.manual_test_scoring')
               CALL                     1
               STORE_NAME              10 (logger)

  42           LOAD_CONST               5 (0.7)
               STORE_NAME              11 (HIGH_RISK_THRESHOLD)
               LOAD_CONST               6 ('float')
               LOAD_NAME               12 (__annotations__)
               LOAD_CONST               7 ('HIGH_RISK_THRESHOLD')
               STORE_SUBSCR

  49           LOAD_CONST               8 (0.9)
               STORE_NAME              13 (_SIMULATION_CONFIDENCE_DISCOUNT)
               LOAD_CONST               6 ('float')
               LOAD_NAME               12 (__annotations__)
               LOAD_CONST               9 ('_SIMULATION_CONFIDENCE_DISCOUNT')
               STORE_SUBSCR

  54           LOAD_CONST              10 (0.05)
               STORE_NAME              14 (_WARNING_RISK_INCREMENT)
               LOAD_CONST               6 ('float')
               LOAD_NAME               12 (__annotations__)
               LOAD_CONST              11 ('_WARNING_RISK_INCREMENT')
               STORE_SUBSCR

  57           LOAD_CONST              35 ((0.0,))
               LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18024930, file "app/services/learning/manual_test_scoring.py", line 57>)
               MAKE_FUNCTION
               LOAD_CONST              14 (<code object _clamp01 at 0x0000018C1796DBD0, file "app/services/learning/manual_test_scoring.py", line 57>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              15 (_clamp01)

  75           LOAD_CONST              36 ((0,))
               LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18024F30, file "app/services/learning/manual_test_scoring.py", line 75>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _nonneg_int at 0x0000018C18039070, file "app/services/learning/manual_test_scoring.py", line 75>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              16 (_nonneg_int)

  83           LOAD_CONST              17 ('score')

  86           LOAD_CONST              12 (0.0)

  83           LOAD_CONST              18 ('components')

  87           LOAD_CONST               2 (None)

  83           LOAD_CONST              19 ('escalation_required')

  88           LOAD_CONST              20 (False)

  83           LOAD_CONST              21 ('error_code')

  89           LOAD_CONST               2 (None)

  83           BUILD_MAP                4
               LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18025C30, file "app/services/learning/manual_test_scoring.py", line 83>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _safe_envelope at 0x0000018C18038F30, file "app/services/learning/manual_test_scoring.py", line 83>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              17 (_safe_envelope)

 100           LOAD_CONST              24 ('warning_count')

 103           LOAD_SMALL_INT           0

 100           BUILD_MAP                1
               LOAD_CONST              25 (<code object __annotate__ at 0x0000018C18025530, file "app/services/learning/manual_test_scoring.py", line 100>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object score_risk_delta at 0x0000018C1794E810, file "app/services/learning/manual_test_scoring.py", line 100>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              18 (score_risk_delta)

 123           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA3B40, file "app/services/learning/manual_test_scoring.py", line 123>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object score_usefulness_delta at 0x0000018C17F95CF0, file "app/services/learning/manual_test_scoring.py", line 123>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              19 (score_usefulness_delta)

 142           LOAD_CONST              29 ('mode')

 145           LOAD_CONST              30 ('SIMULATION_ONLY')

 142           BUILD_MAP                1
               LOAD_CONST              31 (<code object __annotate__ at 0x0000018C18025130, file "app/services/learning/manual_test_scoring.py", line 142>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object score_confidence_delta at 0x0000018C18060390, file "app/services/learning/manual_test_scoring.py", line 142>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              20 (score_confidence_delta)

 163           LOAD_CONST              29 ('mode')

 166           LOAD_CONST              30 ('SIMULATION_ONLY')

 163           LOAD_CONST              24 ('warning_count')

 167           LOAD_SMALL_INT           0

 163           BUILD_MAP                2
               LOAD_CONST              33 (<code object __annotate__ at 0x0000018C18025330, file "app/services/learning/manual_test_scoring.py", line 163>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object score_manual_test_result at 0x0000018C17E861D0, file "app/services/learning/manual_test_scoring.py", line 163>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              21 (score_manual_test_result)

 241           BUILD_LIST               0
               LOAD_CONST              37 (('HIGH_RISK_THRESHOLD', 'score_manual_test_result', 'score_risk_delta', 'score_usefulness_delta', 'score_confidence_delta'))
               LIST_EXTEND              1
               STORE_NAME              22 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app/services/learning/manual_test_scoring.py", line 57>:
 57           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('default')
              LOAD_CONST               4 ('float')
              LOAD_CONST               5 ('return')
              LOAD_CONST               4 ('float')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _clamp01 at 0x0000018C1796DBD0, file "app/services/learning/manual_test_scoring.py", line 57>:
  57            RESUME                   0

  60            LOAD_FAST_BORROW         0 (value)
                POP_JUMP_IF_NOT_NONE    12 (to L1)
                NOT_TAKEN

  61            LOAD_GLOBAL              1 (float + NULL)
                LOAD_FAST_BORROW         1 (default)
                CALL                     1
                RETURN_VALUE

  62    L1:     NOP

  63    L2:     LOAD_GLOBAL              1 (float + NULL)
                LOAD_FAST_BORROW         0 (value)
                CALL                     1
                STORE_FAST               2 (v)

  66    L3:     LOAD_FAST_LOAD_FAST     34 (v, v)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       12 (to L4)
                NOT_TAKEN

  67            LOAD_GLOBAL              1 (float + NULL)
                LOAD_FAST                1 (default)
                CALL                     1
                RETURN_VALUE

  68    L4:     LOAD_FAST                2 (v)
                LOAD_CONST               1 (0.0)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

  69            LOAD_CONST               1 (0.0)
                RETURN_VALUE

  70    L5:     LOAD_FAST                2 (v)
                LOAD_CONST               2 (1.0)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN

  71            LOAD_CONST               2 (1.0)
                RETURN_VALUE

  72    L6:     LOAD_FAST                2 (v)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  64            LOAD_GLOBAL              2 (TypeError)
                LOAD_GLOBAL              4 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       15 (to L9)
                NOT_TAKEN
                POP_TOP

  65            LOAD_GLOBAL              1 (float + NULL)
                LOAD_FAST                1 (default)
                CALL                     1
                SWAP                     2
        L8:     POP_EXCEPT
                RETURN_VALUE

  64    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024F30, file "app/services/learning/manual_test_scoring.py", line 75>:
 75           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('default')
              LOAD_CONST               4 ('int')
              LOAD_CONST               5 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _nonneg_int at 0x0000018C18039070, file "app/services/learning/manual_test_scoring.py", line 75>:
  75           RESUME                   0

  76           NOP

  77   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               2 (v)

  80   L2:     LOAD_FAST                2 (v)
               LOAD_SMALL_INT           0
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_FAST                2 (v)
               RETURN_VALUE
       L3:     LOAD_SMALL_INT           0
               RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

  78           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L6)
               NOT_TAKEN
               POP_TOP

  79           LOAD_FAST                1 (default)
               SWAP                     2
       L5:     POP_EXCEPT
               RETURN_VALUE

  78   L6:     RERAISE                  0

  --   L7:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L4 [0]
  L4 to L5 -> L7 [1] lasti
  L6 to L7 -> L7 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app/services/learning/manual_test_scoring.py", line 83>:
 83           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

 85           LOAD_CONST               2 ('str')

 83           LOAD_CONST               3 ('score')

 86           LOAD_CONST               4 ('float')

 83           LOAD_CONST               5 ('components')

 87           LOAD_CONST               6 ('Optional[Dict[str, float]]')

 83           LOAD_CONST               7 ('escalation_required')

 88           LOAD_CONST               8 ('bool')

 83           LOAD_CONST               9 ('error_code')

 89           LOAD_CONST              10 ('Optional[str]')

 83           LOAD_CONST              11 ('return')

 90           LOAD_CONST              12 ('Dict[str, Any]')

 83           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C18038F30, file "app/services/learning/manual_test_scoring.py", line 83>:
 83           RESUME                   0

 92           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

 93           LOAD_CONST               1 ('score')
              LOAD_GLOBAL              1 (round + NULL)
              LOAD_GLOBAL              3 (_clamp01 + NULL)
              LOAD_FAST_BORROW         1 (score)
              CALL                     1
              LOAD_SMALL_INT           4
              CALL                     2

 94           LOAD_CONST               2 ('components')
              LOAD_FAST                2 (components)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0

 95   L1:     LOAD_CONST               3 ('escalation_required')
              LOAD_GLOBAL              5 (bool + NULL)
              LOAD_FAST_BORROW         3 (escalation_required)
              CALL                     1

 96           LOAD_CONST               4 ('error_code')
              LOAD_FAST_BORROW         4 (error_code)

 91           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "app/services/learning/manual_test_scoring.py", line 100>:
100           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendation')

102           LOAD_CONST               2 ('Any')

100           LOAD_CONST               3 ('warning_count')

103           LOAD_CONST               2 ('Any')

100           LOAD_CONST               4 ('return')

104           LOAD_CONST               5 ('Dict[str, Any]')

100           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object score_risk_delta at 0x0000018C1794E810, file "app/services/learning/manual_test_scoring.py", line 100>:
100           RESUME                   0

110           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (recommendation)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         9 (to L1)
              NOT_TAKEN

111           LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('failed')
              LOAD_CONST               3 ('value')
              LOAD_CONST               4 (0.0)
              LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('invalid_recommendation')
              BUILD_MAP                3
              RETURN_VALUE

112   L1:     LOAD_GLOBAL              5 (_clamp01 + NULL)
              LOAD_FAST_BORROW         0 (recommendation)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               7 ('risk_score')
              CALL                     1
              LOAD_CONST               4 (0.0)
              CALL                     2
              STORE_FAST               2 (base)

113           LOAD_GLOBAL              9 (_nonneg_int + NULL)
              LOAD_FAST_BORROW         1 (warning_count)
              CALL                     1
              STORE_FAST               3 (wc)

114           LOAD_GLOBAL             11 (min + NULL)
              LOAD_CONST               8 (1.0)
              LOAD_FAST_BORROW         3 (wc)
              LOAD_GLOBAL             12 (_WARNING_RISK_INCREMENT)
              BINARY_OP                5 (*)
              CALL                     2
              STORE_FAST               4 (penalty)

115           LOAD_GLOBAL             11 (min + NULL)
              LOAD_CONST               8 (1.0)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 36 (base, penalty)
              BINARY_OP                0 (+)
              CALL                     2
              STORE_FAST               5 (risk)

117           LOAD_CONST               1 ('status')
              LOAD_CONST               9 ('ok')

118           LOAD_CONST               3 ('value')
              LOAD_GLOBAL             15 (round + NULL)
              LOAD_FAST_BORROW         5 (risk)
              LOAD_SMALL_INT           4
              CALL                     2

119           LOAD_CONST               5 ('error_code')
              LOAD_CONST              10 (None)

116           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app/services/learning/manual_test_scoring.py", line 123>:
123           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendation')

125           LOAD_CONST               2 ('Any')

123           LOAD_CONST               3 ('return')

126           LOAD_CONST               4 ('Dict[str, Any]')

123           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object score_usefulness_delta at 0x0000018C17F95CF0, file "app/services/learning/manual_test_scoring.py", line 123>:
123           RESUME                   0

133           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (recommendation)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         9 (to L1)
              NOT_TAKEN

134           LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('failed')
              LOAD_CONST               3 ('value')
              LOAD_CONST               4 (0.0)
              LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('invalid_recommendation')
              BUILD_MAP                3
              RETURN_VALUE

136   L1:     LOAD_CONST               1 ('status')
              LOAD_CONST               7 ('ok')

137           LOAD_CONST               3 ('value')
              LOAD_GLOBAL              5 (round + NULL)
              LOAD_GLOBAL              7 (_clamp01 + NULL)
              LOAD_FAST_BORROW         0 (recommendation)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               8 ('usefulness_score')
              CALL                     1
              LOAD_CONST               4 (0.0)
              CALL                     2
              LOAD_SMALL_INT           4
              CALL                     2

138           LOAD_CONST               5 ('error_code')
              LOAD_CONST               9 (None)

135           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "app/services/learning/manual_test_scoring.py", line 142>:
142           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendation')

144           LOAD_CONST               2 ('Any')

142           LOAD_CONST               3 ('mode')

145           LOAD_CONST               4 ('str')

142           LOAD_CONST               5 ('return')

146           LOAD_CONST               6 ('Dict[str, Any]')

142           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object score_confidence_delta at 0x0000018C18060390, file "app/services/learning/manual_test_scoring.py", line 142>:
142           RESUME                   0

151           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (recommendation)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         9 (to L1)
              NOT_TAKEN

152           LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('failed')
              LOAD_CONST               3 ('value')
              LOAD_CONST               4 (0.0)
              LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('invalid_recommendation')
              BUILD_MAP                3
              RETURN_VALUE

153   L1:     LOAD_GLOBAL              5 (_clamp01 + NULL)
              LOAD_FAST_BORROW         0 (recommendation)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               7 ('confidence_score')
              CALL                     1
              LOAD_CONST               4 (0.0)
              CALL                     2
              STORE_FAST               2 (base)

154           LOAD_FAST_BORROW         1 (mode)
              LOAD_CONST               8 ('SIMULATION_ONLY')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       14 (to L2)
              NOT_TAKEN

155           LOAD_FAST_BORROW         2 (base)
              LOAD_GLOBAL              8 (_SIMULATION_CONFIDENCE_DISCOUNT)
              BINARY_OP                5 (*)
              STORE_FAST               2 (base)

157   L2:     LOAD_CONST               1 ('status')
              LOAD_CONST               9 ('ok')

158           LOAD_CONST               3 ('value')
              LOAD_GLOBAL             11 (round + NULL)
              LOAD_GLOBAL              5 (_clamp01 + NULL)
              LOAD_FAST_BORROW         2 (base)
              CALL                     1
              LOAD_SMALL_INT           4
              CALL                     2

159           LOAD_CONST               5 ('error_code')
              LOAD_CONST              10 (None)

156           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025330, file "app/services/learning/manual_test_scoring.py", line 163>:
163           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendation')

165           LOAD_CONST               2 ('Any')

163           LOAD_CONST               3 ('mode')

166           LOAD_CONST               4 ('str')

163           LOAD_CONST               5 ('warning_count')

167           LOAD_CONST               2 ('Any')

163           LOAD_CONST               6 ('return')

168           LOAD_CONST               7 ('Dict[str, Any]')

163           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object score_manual_test_result at 0x0000018C17E861D0, file "app/services/learning/manual_test_scoring.py", line 163>:
 163            RESUME                   0

 184            NOP

 185    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (recommendation)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L3)
                NOT_TAKEN

 186            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 187            LOAD_CONST               1 ('failed')

 188            LOAD_CONST               2 ('invalid_recommendation')

 186            LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
        L2:     RETURN_VALUE

 190    L3:     LOAD_FAST_BORROW         1 (mode)
                LOAD_CONST              21 (('SIMULATION_ONLY', 'OBSERVATIONAL_ONLY'))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       14 (to L5)
                NOT_TAKEN

 191            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 192            LOAD_CONST               1 ('failed')

 193            LOAD_CONST               4 ('invalid_mode')

 191            LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
        L4:     RETURN_VALUE

 195    L5:     LOAD_GLOBAL              7 (score_risk_delta + NULL)

 196            LOAD_FAST_BORROW         0 (recommendation)

 197            LOAD_FAST_BORROW         2 (warning_count)

 195            LOAD_CONST               5 (('recommendation', 'warning_count'))
                CALL_KW                  2
                STORE_FAST               3 (risk_env)

 199            LOAD_GLOBAL              9 (score_usefulness_delta + NULL)
                LOAD_FAST_BORROW         0 (recommendation)
                LOAD_CONST               6 (('recommendation',))
                CALL_KW                  1
                STORE_FAST               4 (useful_env)

 200            LOAD_GLOBAL             11 (score_confidence_delta + NULL)

 201            LOAD_FAST_BORROW         0 (recommendation)

 202            LOAD_FAST_BORROW         1 (mode)

 200            LOAD_CONST               7 (('recommendation', 'mode'))
                CALL_KW                  2
                STORE_FAST               5 (conf_env)

 204            LOAD_FAST_BORROW         3 (risk_env)
                LOAD_CONST               8 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               9 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_TRUE        29 (to L6)
                NOT_TAKEN

 205            LOAD_FAST_BORROW         4 (useful_env)
                LOAD_CONST               8 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               9 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_TRUE        15 (to L6)
                NOT_TAKEN

 206            LOAD_FAST_BORROW         5 (conf_env)
                LOAD_CONST               8 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               9 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       14 (to L8)
                NOT_TAKEN

 207    L6:     LOAD_GLOBAL              5 (_safe_envelope + NULL)

 208            LOAD_CONST               1 ('failed')

 209            LOAD_CONST              10 ('component_score_failed')

 207            LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
        L7:     RETURN_VALUE

 211    L8:     LOAD_GLOBAL             13 (float + NULL)
                LOAD_FAST_BORROW         3 (risk_env)
                LOAD_CONST              11 ('value')
                BINARY_OP               26 ([])
                CALL                     1
                STORE_FAST               6 (risk)

 212            LOAD_GLOBAL             13 (float + NULL)
                LOAD_FAST_BORROW         4 (useful_env)
                LOAD_CONST              11 ('value')
                BINARY_OP               26 ([])
                CALL                     1
                STORE_FAST               7 (useful)

 213            LOAD_GLOBAL             13 (float + NULL)
                LOAD_FAST_BORROW         5 (conf_env)
                LOAD_CONST              11 ('value')
                BINARY_OP               26 ([])
                CALL                     1
                STORE_FAST               8 (conf)

 215            LOAD_FAST_BORROW         7 (useful)
                LOAD_CONST              12 (1.0)
                LOAD_FAST_BORROW         6 (risk)
                BINARY_OP               10 (-)
                BINARY_OP                5 (*)
                LOAD_FAST_BORROW         8 (conf)
                BINARY_OP                5 (*)
                STORE_FAST               9 (score)

 216            LOAD_FAST_BORROW         9 (score)
                LOAD_CONST              13 (0.0)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN

 217            LOAD_CONST              13 (0.0)
                STORE_FAST               9 (score)

 218    L9:     LOAD_FAST_BORROW         9 (score)
                LOAD_CONST              12 (1.0)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN

 219            LOAD_CONST              12 (1.0)
                STORE_FAST               9 (score)

 220   L10:     LOAD_GLOBAL              5 (_safe_envelope + NULL)

 221            LOAD_CONST               9 ('ok')

 222            LOAD_FAST_BORROW         9 (score)

 224            LOAD_CONST              14 ('risk')
                LOAD_GLOBAL             15 (round + NULL)
                LOAD_FAST_BORROW         6 (risk)
                LOAD_SMALL_INT           4
                CALL                     2

 225            LOAD_CONST              15 ('usefulness')
                LOAD_GLOBAL             15 (round + NULL)
                LOAD_FAST_BORROW         7 (useful)
                LOAD_SMALL_INT           4
                CALL                     2

 226            LOAD_CONST              16 ('confidence')
                LOAD_GLOBAL             15 (round + NULL)
                LOAD_FAST_BORROW         8 (conf)
                LOAD_SMALL_INT           4
                CALL                     2

 223            BUILD_MAP                3

 228            LOAD_FAST_BORROW         6 (risk)
                LOAD_GLOBAL             16 (HIGH_RISK_THRESHOLD)
                COMPARE_OP             172 (>=)

 220            LOAD_CONST              17 (('status', 'score', 'components', 'escalation_required'))
                CALL_KW                  4
       L11:     RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 230            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       89 (to L17)
                NOT_TAKEN
                STORE_FAST              10 (e)

 231   L13:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 232            LOAD_CONST              18 ('score_manual_test_result unexpected error type=')

 233            LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE

 232            BUILD_STRING             2

 231            CALL                     1
                POP_TOP

 235            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 236            LOAD_CONST               1 ('failed')

 237            LOAD_CONST              19 ('unexpected:')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 235            LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
       L14:     SWAP                     2
       L15:     POP_EXCEPT
                LOAD_CONST              20 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RETURN_VALUE

  --   L16:     LOAD_CONST              20 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 230   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L12 [0]
  L3 to L4 -> L12 [0]
  L5 to L7 -> L12 [0]
  L8 to L11 -> L12 [0]
  L12 to L13 -> L18 [1] lasti
  L13 to L14 -> L16 [1] lasti
  L14 to L15 -> L18 [1] lasti
  L16 to L18 -> L18 [1] lasti
```
