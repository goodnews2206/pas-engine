# learning/outcome_feedback

- **pyc:** `app\services\learning\__pycache__\outcome_feedback.cpython-314.pyc`
- **expected source path (absent):** `app\services\learning/outcome_feedback.py`
- **co_filename (from bytecode):** `app/services/learning/outcome_feedback.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** learning

## Module docstring

```
PAS179 — Bounded outcome feedback contract.

Closed structural feedback records describing the outcome of a
real-world interaction or scenario run. Used by the
recommendation engine to score candidate learning signals
*deterministically* — no LLM, no embedding, no freeform text.

Doctrine:

* **No PII.** Forbidden fields rejected before fingerprinting.
* **Deterministic scoring.** Same canonical envelope → byte-
  identical score envelope.
* **Bounded.** Score in [0, 1].
* **NEVER raises.** All helpers collapse to structural
  envelopes on failure.
* **No external calls.** Pure functions only.

Public surface:

  * ``ALLOWED_OUTCOMES``           — closed enum
  * ``FORBIDDEN_FEEDBACK_FIELDS``  — PII blocklist
  * ``build_outcome_feedback(...)``
  * ``outcome_feedback_fingerprint(...)``
  * ``score_outcome_feedback(feedback)`` — deterministic [0,1]
  * ``feedback_summary(list_of_feedback)``
```

## Imports

`Any`, `Dict`, `Iterable`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `hashlib`, `json`, `logging`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_bound_brokerage_id`, `_canonical_json`, `_project_metadata`, `_safe_envelope`, `_scan_forbidden_keys`, `build_outcome_feedback`, `feedback_summary`, `outcome_feedback_fingerprint`, `score_outcome_feedback`

## Env-key candidates

`ALLOWED_FEEDBACK_METADATA_KEYS`, `ALLOWED_OUTCOMES`, `BOOKED`, `CALLBACK_COMPLETED`, `CALLBACK_REQUESTED`, `CONTACTED`, `DUPLICATE_SUPPRESSED`, `FAILED_PROVIDER`, `FAILED_WORKER`, `FORBIDDEN_FEEDBACK_FIELDS`, `NOT_CONTACTED`, `REJECTED_BY_OPERATOR`

## String constants (redacted where noted)

- '\nPAS179 — Bounded outcome feedback contract.\n\nClosed structural feedback records describing the outcome of a\nreal-world interaction or scenario run. Used by the\nrecommendation engine to score candidate learning signals\n*deterministically* — no LLM, no embedding, no freeform text.\n\nDoctrine:\n\n* **No PII.** Forbidden fields rejected before fingerprinting.\n* **Deterministic scoring.** Same canonical envelope → byte-\n  identical score envelope.\n* **Bounded.** Score in [0, 1].\n* **NEVER raises.** All helpers collapse to structural\n  envelopes on failure.\n* **No external calls.** Pure functions only.\n\nPublic surface:\n\n  * ``ALLOWED_OUTCOMES``           — closed enum\n  * ``FORBIDDEN_FEEDBACK_FIELDS``  — PII blocklist\n  * ``build_outcome_feedback(...)``\n  * ``outcome_feedback_fingerprint(...)``\n  * ``score_outcome_feedback(feedback)`` — deterministic [0,1]\n  * ``feedback_summary(list_of_feedback)``\n'
- 'pas.learning.outcome_feedback'
- 'CONTACTED'
- 'NOT_CONTACTED'
- 'BOOKED'
- 'CALLBACK_REQUESTED'
- 'CALLBACK_COMPLETED'
- 'DUPLICATE_SUPPRESSED'
- 'FAILED_PROVIDER'
- 'FAILED_WORKER'
- 'REJECTED_BY_OPERATOR'
- 'Tuple[str, ...]'
- 'ALLOWED_OUTCOMES'
- 'Dict[str, float]'
- '_OUTCOME_SCORE_TABLE'
- 'FORBIDDEN_FEEDBACK_FIELDS'
- 'ALLOWED_FEEDBACK_METADATA_KEYS'
- 'feedback'
- 'fingerprint'
- 'warnings'
- 'error_code'
- 'metadata'
- 'value'
- 'Any'
- 'return'
- 'Optional[str]'
- 'payload'
- 'List[str]'
- 'Dict[str, Any]'
- 'status'
- 'str'
- 'brokerage_id'
- 'outcome'
- 'Optional[Dict[str, Any]]'
- 'Optional[List[str]]'
- 'envelope'
- 'Deterministic sha256 over the canonical feedback envelope.\nNEVER raises.'
- 'utf-8'
- 'outcome_feedback_fingerprint error type='
- 'Build a structural outcome feedback record. NEVER raises.'
- 'failed'
- 'missing_brokerage_id'
- 'invalid_outcome'
- 'forbidden_field:'
- 'forbidden_feedback_field'
- 'Deterministic [0, 1] score for the feedback record.\nNEVER raises.'
- 'score'
- 'invalid_feedback'
- 'score_outcome_feedback error type='
- 'unexpected:'
- 'feedback_list'
- 'Iterable[Any]'
- 'Bounded summary across a list of feedback records.\nNEVER raises. NEVER returns PII.'
- 'total'
- 'by_outcome'
- 'average_score'
- 'feedback_summary error type='

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS179 — Bounded outcome feedback contract.\n\nClosed structural feedback records describing the outcome of a\nreal-world interaction or scenario run. Used by the\nrecommendation engine to score candidate learning signals\n*deterministically* — no LLM, no embedding, no freeform text.\n\nDoctrine:\n\n* **No PII.** Forbidden fields rejected before fingerprinting.\n* **Deterministic scoring.** Same canonical envelope → byte-\n  identical score envelope.\n* **Bounded.** Score in [0, 1].\n* **NEVER raises.** All helpers collapse to structural\n  envelopes on failure.\n* **No external calls.** Pure functions only.\n\nPublic surface:\n\n  * ``ALLOWED_OUTCOMES``           — closed enum\n  * ``FORBIDDEN_FEEDBACK_FIELDS``  — PII blocklist\n  * ``build_outcome_feedback(...)``\n  * ``outcome_feedback_fingerprint(...)``\n  * ``score_outcome_feedback(feedback)`` — deterministic [0,1]\n  * ``feedback_summary(list_of_feedback)``\n')
               STORE_NAME               1 (__doc__)

  29           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  31           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (hashlib)
               STORE_NAME               4 (hashlib)

  32           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (json)
               STORE_NAME               5 (json)

  33           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (logging)
               STORE_NAME               6 (logging)

  34           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('Any', 'Dict', 'Iterable', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME              7 (typing)
               IMPORT_FROM              8 (Any)
               STORE_NAME               8 (Any)
               IMPORT_FROM              9 (Dict)
               STORE_NAME               9 (Dict)
               IMPORT_FROM             10 (Iterable)
               STORE_NAME              10 (Iterable)
               IMPORT_FROM             11 (List)
               STORE_NAME              11 (List)
               IMPORT_FROM             12 (Optional)
               STORE_NAME              12 (Optional)
               IMPORT_FROM             13 (Tuple)
               STORE_NAME              13 (Tuple)
               POP_TOP

  37           LOAD_NAME                6 (logging)
               LOAD_ATTR               28 (getLogger)
               PUSH_NULL
               LOAD_CONST               4 ('pas.learning.outcome_feedback')
               CALL                     1
               STORE_NAME              15 (logger)

  41           LOAD_CONST              52 (('CONTACTED', 'NOT_CONTACTED', 'BOOKED', 'CALLBACK_REQUESTED', 'CALLBACK_COMPLETED', 'DUPLICATE_SUPPRESSED', 'FAILED_PROVIDER', 'FAILED_WORKER', 'REJECTED_BY_OPERATOR'))
               STORE_NAME              16 (ALLOWED_OUTCOMES)
               LOAD_CONST              14 ('Tuple[str, ...]')
               LOAD_NAME               17 (__annotations__)
               LOAD_CONST              15 ('ALLOWED_OUTCOMES')
               STORE_SUBSCR

  58           LOAD_CONST               7 ('BOOKED')
               LOAD_CONST              16 (1.0)

  59           LOAD_CONST               9 ('CALLBACK_COMPLETED')
               LOAD_CONST              17 (0.8)

  60           LOAD_CONST               5 ('CONTACTED')
               LOAD_CONST              18 (0.6)

  61           LOAD_CONST               8 ('CALLBACK_REQUESTED')
               LOAD_CONST              19 (0.55)

  62           LOAD_CONST              10 ('DUPLICATE_SUPPRESSED')
               LOAD_CONST              20 (0.5)

  63           LOAD_CONST               6 ('NOT_CONTACTED')
               LOAD_CONST              21 (0.2)

  64           LOAD_CONST              13 ('REJECTED_BY_OPERATOR')
               LOAD_CONST              22 (0.1)

  65           LOAD_CONST              11 ('FAILED_PROVIDER')
               LOAD_CONST              23 (0.05)

  66           LOAD_CONST              12 ('FAILED_WORKER')
               LOAD_CONST              24 (0.0)

  57           BUILD_MAP                9
               STORE_NAME              18 (_OUTCOME_SCORE_TABLE)
               LOAD_CONST              25 ('Dict[str, float]')
               LOAD_NAME               17 (__annotations__)
               LOAD_CONST              26 ('_OUTCOME_SCORE_TABLE')
               STORE_SUBSCR

  71           LOAD_CONST              53 (('phone', 'email', 'name', 'raw_payload', 'raw_email', 'raw_body', 'transcript', 'summary', 'summary_text', 'secret', 'signature', 'env_value', 'env_values', 'dedupe_key', 'callback_notes', 'first_name', 'last_name', 'full_name', 'address', 'street'))
               STORE_NAME              19 (FORBIDDEN_FEEDBACK_FIELDS)
               LOAD_CONST              14 ('Tuple[str, ...]')
               LOAD_NAME               17 (__annotations__)
               LOAD_CONST              27 ('FORBIDDEN_FEEDBACK_FIELDS')
               STORE_SUBSCR

  83           LOAD_CONST              54 (('scenario_type', 'scenario_fingerprint', 'simulation_run_id', 'warning_count', 'duration_band'))
               STORE_NAME              20 (ALLOWED_FEEDBACK_METADATA_KEYS)
               LOAD_CONST              14 ('Tuple[str, ...]')
               LOAD_NAME               17 (__annotations__)
               LOAD_CONST              28 ('ALLOWED_FEEDBACK_METADATA_KEYS')
               STORE_SUBSCR

  92           LOAD_SMALL_INT         200
               STORE_NAME              21 (_BROKERAGE_ID_MAX_LEN)

  93           LOAD_SMALL_INT         200
               STORE_NAME              22 (_VALUE_MAX_LEN)

  96           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA3C30, file "app/services/learning/outcome_feedback.py", line 96>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object _bound_brokerage_id at 0x0000018C17F95E60, file "app/services/learning/outcome_feedback.py", line 96>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              23 (_bound_brokerage_id)

 105           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA2B50, file "app/services/learning/outcome_feedback.py", line 105>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object _scan_forbidden_keys at 0x0000018C179C3A50, file "app/services/learning/outcome_feedback.py", line 105>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              24 (_scan_forbidden_keys)

 120           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C17FA2D30, file "app/services/learning/outcome_feedback.py", line 120>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object _project_metadata at 0x0000018C17FED630, file "app/services/learning/outcome_feedback.py", line 120>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              25 (_project_metadata)

 135           LOAD_CONST              35 ('feedback')

 140           LOAD_CONST               2 (None)

 135           LOAD_CONST              36 ('fingerprint')

 141           LOAD_CONST               2 (None)

 135           LOAD_CONST              37 ('warnings')

 142           LOAD_CONST               2 (None)

 135           LOAD_CONST              38 ('error_code')

 143           LOAD_CONST               2 (None)

 135           BUILD_MAP                4
               LOAD_CONST              39 (<code object __annotate__ at 0x0000018C17FBFEE0, file "app/services/learning/outcome_feedback.py", line 135>)
               MAKE_FUNCTION
               LOAD_CONST              40 (<code object _safe_envelope at 0x0000018C18053870, file "app/services/learning/outcome_feedback.py", line 135>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              26 (_safe_envelope)

 156           LOAD_CONST              41 (<code object __annotate__ at 0x0000018C17FA33C0, file "app/services/learning/outcome_feedback.py", line 156>)
               MAKE_FUNCTION
               LOAD_CONST              42 (<code object _canonical_json at 0x0000018C18090360, file "app/services/learning/outcome_feedback.py", line 156>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              27 (_canonical_json)

 160           LOAD_CONST              43 (<code object __annotate__ at 0x0000018C17FA2100, file "app/services/learning/outcome_feedback.py", line 160>)
               MAKE_FUNCTION
               LOAD_CONST              44 (<code object outcome_feedback_fingerprint at 0x0000018C17EDAAB0, file "app/services/learning/outcome_feedback.py", line 160>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (outcome_feedback_fingerprint)

 179           LOAD_CONST              45 ('metadata')

 183           LOAD_CONST               2 (None)

 179           BUILD_MAP                1
               LOAD_CONST              46 (<code object __annotate__ at 0x0000018C18024D30, file "app/services/learning/outcome_feedback.py", line 179>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object build_outcome_feedback at 0x0000018C17ED6350, file "app/services/learning/outcome_feedback.py", line 179>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              29 (build_outcome_feedback)

 226           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA2C40, file "app/services/learning/outcome_feedback.py", line 226>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object score_outcome_feedback at 0x0000018C17F84CD0, file "app/services/learning/outcome_feedback.py", line 226>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              30 (score_outcome_feedback)

 269           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C17FA2E20, file "app/services/learning/outcome_feedback.py", line 269>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object feedback_summary at 0x0000018C17F749F0, file "app/services/learning/outcome_feedback.py", line 269>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (feedback_summary)

 308           BUILD_LIST               0
               LOAD_CONST              55 (('ALLOWED_OUTCOMES', 'FORBIDDEN_FEEDBACK_FIELDS', 'ALLOWED_FEEDBACK_METADATA_KEYS', 'build_outcome_feedback', 'outcome_feedback_fingerprint', 'score_outcome_feedback', 'feedback_summary'))
               LIST_EXTEND              1
               STORE_NAME              32 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app/services/learning/outcome_feedback.py", line 96>:
 96           RESUME                   0
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

Disassembly of <code object _bound_brokerage_id at 0x0000018C17F95E60, file "app/services/learning/outcome_feedback.py", line 96>:
 96           RESUME                   0

 97           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 98           LOAD_CONST               0 (None)
              RETURN_VALUE

 99   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

100           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_BROKERAGE_ID_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

101   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

102   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app/services/learning/outcome_feedback.py", line 105>:
105           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('payload')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _scan_forbidden_keys at 0x0000018C179C3A50, file "app/services/learning/outcome_feedback.py", line 105>:
105           RESUME                   0

106           BUILD_LIST               0
              STORE_FAST               1 (bad)

107           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (payload)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

108           LOAD_FAST_BORROW         1 (bad)
              RETURN_VALUE

109   L1:     LOAD_FAST_BORROW         0 (payload)
              LOAD_ATTR                5 (keys + NULL|self)
              CALL                     0
              GET_ITER
      L2:     FOR_ITER                82 (to L7)
              STORE_FAST               2 (k)

110           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (k)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

111           JUMP_BACKWARD           27 (to L2)

112   L3:     LOAD_FAST_BORROW         2 (k)
              LOAD_ATTR                9 (lower + NULL|self)
              CALL                     0
              STORE_FAST               3 (kl)

113           LOAD_GLOBAL             10 (FORBIDDEN_FEEDBACK_FIELDS)
              GET_ITER
      L4:     FOR_ITER                29 (to L6)
              STORE_FAST               4 (forb)

114           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (forb, kl)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L4)

115   L5:     LOAD_FAST_BORROW         1 (bad)
              LOAD_ATTR               13 (append + NULL|self)
              LOAD_FAST_BORROW         2 (k)
              CALL                     1
              POP_TOP

116           POP_TOP
              JUMP_BACKWARD           80 (to L2)

113   L6:     END_FOR
              POP_ITER
              JUMP_BACKWARD           84 (to L2)

109   L7:     END_FOR
              POP_ITER

117           LOAD_FAST_BORROW         1 (bad)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app/services/learning/outcome_feedback.py", line 120>:
120           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('metadata')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _project_metadata at 0x0000018C17FED630, file "app/services/learning/outcome_feedback.py", line 120>:
120           RESUME                   0

121           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (metadata)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

122           BUILD_MAP                0
              RETURN_VALUE

123   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

124           LOAD_GLOBAL              4 (ALLOWED_FEEDBACK_METADATA_KEYS)
              GET_ITER
      L2:     FOR_ITER               112 (to L8)
              STORE_FAST               2 (k)

125           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, metadata)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

126           JUMP_BACKWARD           11 (to L2)

127   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (metadata, k)
              BINARY_OP               26 ([])
              STORE_FAST               3 (v)

128           LOAD_FAST_BORROW         3 (v)
              POP_JUMP_IF_NONE        34 (to L4)
              NOT_TAKEN
              LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (v)
              LOAD_GLOBAL              6 (bool)
              LOAD_GLOBAL              8 (int)
              LOAD_GLOBAL             10 (float)
              BUILD_TUPLE              3
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        7 (to L5)
              NOT_TAKEN

129   L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD           62 (to L2)

130   L5:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (v)
              LOAD_GLOBAL             12 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              JUMP_BACKWARD           86 (to L2)
      L6:     LOAD_GLOBAL             15 (len + NULL)
              LOAD_FAST_BORROW         3 (v)
              CALL                     1
              LOAD_GLOBAL             16 (_VALUE_MAX_LEN)
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_TRUE         3 (to L7)
              NOT_TAKEN
              JUMP_BACKWARD          108 (to L2)

131   L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD          114 (to L2)

124   L8:     END_FOR
              POP_ITER

132           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FBFEE0, file "app/services/learning/outcome_feedback.py", line 135>:
135           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

137           LOAD_CONST               2 ('str')

135           LOAD_CONST               3 ('brokerage_id')

138           LOAD_CONST               4 ('Optional[str]')

135           LOAD_CONST               5 ('outcome')

139           LOAD_CONST               4 ('Optional[str]')

135           LOAD_CONST               6 ('feedback')

140           LOAD_CONST               7 ('Optional[Dict[str, Any]]')

135           LOAD_CONST               8 ('fingerprint')

141           LOAD_CONST               4 ('Optional[str]')

135           LOAD_CONST               9 ('warnings')

142           LOAD_CONST              10 ('Optional[List[str]]')

135           LOAD_CONST              11 ('error_code')

143           LOAD_CONST               4 ('Optional[str]')

135           LOAD_CONST              12 ('return')

144           LOAD_CONST              13 ('Dict[str, Any]')

135           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C18053870, file "app/services/learning/outcome_feedback.py", line 135>:
135           RESUME                   0

146           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

147           LOAD_CONST               1 ('brokerage_id')
              LOAD_FAST                1 (brokerage_id)

148           LOAD_CONST               2 ('outcome')
              LOAD_FAST                2 (outcome)

149           LOAD_CONST               3 ('feedback')
              LOAD_FAST                3 (feedback)

150           LOAD_CONST               4 ('fingerprint')
              LOAD_FAST                4 (fingerprint)

151           LOAD_CONST               5 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                5 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

152           LOAD_CONST               6 ('error_code')
              LOAD_FAST_BORROW         6 (error_code)

145           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app/services/learning/outcome_feedback.py", line 156>:
156           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('envelope')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _canonical_json at 0x0000018C18090360, file "app/services/learning/outcome_feedback.py", line 156>:
156           RESUME                   0

157           LOAD_GLOBAL              0 (json)
              LOAD_ATTR                2 (dumps)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (envelope)
              LOAD_CONST               0 (True)
              LOAD_CONST               2 ((',', ':'))
              LOAD_CONST               1 (('sort_keys', 'separators'))
              CALL_KW                  3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app/services/learning/outcome_feedback.py", line 160>:
160           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('feedback')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object outcome_feedback_fingerprint at 0x0000018C17EDAAB0, file "app/services/learning/outcome_feedback.py", line 160>:
 160            RESUME                   0

 163            NOP

 164    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (feedback)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        37 (to L3)
                NOT_TAKEN

 165            LOAD_GLOBAL              4 (hashlib)
                LOAD_ATTR                6 (sha256)
                PUSH_NULL
                LOAD_CONST               1 (b'')
                CALL                     1
                LOAD_ATTR                9 (hexdigest + NULL|self)
                CALL                     0
        L2:     RETURN_VALUE

 166    L3:     LOAD_GLOBAL             11 (_canonical_json + NULL)

 167            LOAD_CONST               2 ('brokerage_id')
                LOAD_FAST_BORROW         0 (feedback)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               2 ('brokerage_id')
                CALL                     1

 168            LOAD_CONST               3 ('outcome')
                LOAD_FAST_BORROW         0 (feedback)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               3 ('outcome')
                CALL                     1

 169            LOAD_CONST               4 ('metadata')
                LOAD_GLOBAL             15 (_project_metadata + NULL)
                LOAD_FAST_BORROW         0 (feedback)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               4 ('metadata')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
        L4:     NOT_TAKEN
        L5:     POP_TOP
                BUILD_MAP                0
        L6:     CALL                     1

 166            BUILD_MAP                3
                CALL                     1
                STORE_FAST               1 (canonical)

 171            LOAD_GLOBAL              4 (hashlib)
                LOAD_ATTR                6 (sha256)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (canonical)
                LOAD_ATTR               17 (encode + NULL|self)
                LOAD_CONST               5 ('utf-8')
                CALL                     1
                CALL                     1
                LOAD_ATTR                9 (hexdigest + NULL|self)
                CALL                     0
        L7:     RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

 172            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       90 (to L13)
                NOT_TAKEN
                STORE_FAST               2 (e)

 173    L9:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 174            LOAD_CONST               6 ('outcome_feedback_fingerprint error type=')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                2 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 173            CALL                     1
                POP_TOP

 176            LOAD_GLOBAL              4 (hashlib)
                LOAD_ATTR                6 (sha256)
                PUSH_NULL
                LOAD_CONST               1 (b'')
                CALL                     1
                LOAD_ATTR                9 (hexdigest + NULL|self)
                CALL                     0
       L10:     SWAP                     2
       L11:     POP_EXCEPT
                LOAD_CONST               7 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                RETURN_VALUE

  --   L12:     LOAD_CONST               7 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                RERAISE                  1

 172   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L8 [0]
  L3 to L4 -> L8 [0]
  L5 to L7 -> L8 [0]
  L8 to L9 -> L14 [1] lasti
  L9 to L10 -> L12 [1] lasti
  L10 to L11 -> L14 [1] lasti
  L12 to L14 -> L14 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024D30, file "app/services/learning/outcome_feedback.py", line 179>:
179           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

181           LOAD_CONST               2 ('Any')

179           LOAD_CONST               3 ('outcome')

182           LOAD_CONST               2 ('Any')

179           LOAD_CONST               4 ('metadata')

183           LOAD_CONST               2 ('Any')

179           LOAD_CONST               5 ('return')

184           LOAD_CONST               6 ('Dict[str, Any]')

179           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object build_outcome_feedback at 0x0000018C17ED6350, file "app/services/learning/outcome_feedback.py", line 179>:
 179           RESUME                   0

 186           LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
               LOAD_FAST_BORROW         0 (brokerage_id)
               CALL                     1
               STORE_FAST               3 (bid)

 187           LOAD_FAST_BORROW         3 (bid)
               POP_JUMP_IF_NOT_NONE    16 (to L1)
               NOT_TAKEN

 188           LOAD_GLOBAL              3 (_safe_envelope + NULL)

 189           LOAD_CONST               2 ('failed')

 190           LOAD_CONST               1 (None)

 191           LOAD_CONST               1 (None)

 192           LOAD_CONST               3 ('missing_brokerage_id')

 188           LOAD_CONST               4 (('status', 'brokerage_id', 'outcome', 'error_code'))
               CALL_KW                  4
               RETURN_VALUE

 194   L1:     LOAD_FAST_BORROW         1 (outcome)
               LOAD_GLOBAL              4 (ALLOWED_OUTCOMES)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       16 (to L2)
               NOT_TAKEN

 195           LOAD_GLOBAL              3 (_safe_envelope + NULL)

 196           LOAD_CONST               2 ('failed')

 197           LOAD_FAST_BORROW         3 (bid)

 198           LOAD_CONST               1 (None)

 199           LOAD_CONST               5 ('invalid_outcome')

 195           LOAD_CONST               4 (('status', 'brokerage_id', 'outcome', 'error_code'))
               CALL_KW                  4
               RETURN_VALUE

 201   L2:     LOAD_GLOBAL              7 (_scan_forbidden_keys + NULL)
               LOAD_FAST_BORROW         2 (metadata)
               CALL                     1
               STORE_FAST               4 (forbidden)

 202           LOAD_FAST_BORROW         4 (forbidden)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L7)
               NOT_TAKEN

 203           LOAD_GLOBAL              3 (_safe_envelope + NULL)

 204           LOAD_CONST               2 ('failed')

 205           LOAD_FAST                3 (bid)

 206           LOAD_FAST                1 (outcome)

 207           LOAD_FAST_BORROW         4 (forbidden)
               LOAD_CONST               6 (slice(None, 5, None))
               BINARY_OP               26 ([])
               GET_ITER
               LOAD_FAST_AND_CLEAR      5 (k)
               SWAP                     2
       L3:     BUILD_LIST               0
               SWAP                     2
       L4:     FOR_ITER                 8 (to L5)
               STORE_FAST               5 (k)
               LOAD_CONST               7 ('forbidden_field:')
               LOAD_FAST_BORROW         5 (k)
               FORMAT_SIMPLE
               BUILD_STRING             2
               LIST_APPEND              2
               JUMP_BACKWARD           10 (to L4)
       L5:     END_FOR
               POP_ITER
       L6:     SWAP                     2
               STORE_FAST               5 (k)

 208           LOAD_CONST               8 ('forbidden_feedback_field')

 203           LOAD_CONST               9 (('status', 'brokerage_id', 'outcome', 'warnings', 'error_code'))
               CALL_KW                  5
               RETURN_VALUE

 210   L7:     LOAD_GLOBAL              9 (_project_metadata + NULL)
               LOAD_FAST_BORROW         2 (metadata)
               CALL                     1
               STORE_FAST               6 (meta)

 212           LOAD_CONST              10 ('brokerage_id')
               LOAD_FAST_BORROW         3 (bid)

 213           LOAD_CONST              11 ('outcome')
               LOAD_FAST_BORROW         1 (outcome)

 214           LOAD_CONST              12 ('metadata')
               LOAD_FAST_BORROW         6 (meta)

 211           BUILD_MAP                3
               STORE_FAST               7 (feedback)

 216           LOAD_GLOBAL             11 (outcome_feedback_fingerprint + NULL)
               LOAD_FAST_BORROW         7 (feedback)
               CALL                     1
               STORE_FAST               8 (fp)

 217           LOAD_GLOBAL              3 (_safe_envelope + NULL)

 218           LOAD_CONST              13 ('ok')

 219           LOAD_FAST_BORROW         3 (bid)

 220           LOAD_FAST_BORROW         1 (outcome)

 221           LOAD_FAST_BORROW         7 (feedback)

 222           LOAD_FAST_BORROW         8 (fp)

 217           LOAD_CONST              14 (('status', 'brokerage_id', 'outcome', 'feedback', 'fingerprint'))
               CALL_KW                  5
               RETURN_VALUE

  --   L8:     SWAP                     2
               POP_TOP

 207           SWAP                     2
               STORE_FAST               5 (k)
               RERAISE                  0
ExceptionTable:
  L3 to L6 -> L8 [7]

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app/services/learning/outcome_feedback.py", line 226>:
226           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('feedback')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object score_outcome_feedback at 0x0000018C17F84CD0, file "app/services/learning/outcome_feedback.py", line 226>:
 226            RESUME                   0

 229            NOP

 230    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (feedback)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L3)
                NOT_TAKEN

 232            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 233            LOAD_CONST               3 ('score')
                LOAD_CONST               4 (0.0)

 234            LOAD_CONST               5 ('outcome')
                LOAD_CONST               6 (None)

 235            LOAD_CONST               7 ('error_code')
                LOAD_CONST               8 ('invalid_feedback')

 231            BUILD_MAP                4
        L2:     RETURN_VALUE

 237    L3:     LOAD_FAST_BORROW         0 (feedback)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               5 ('outcome')
                CALL                     1
                STORE_FAST               1 (outcome)

 238            LOAD_FAST_BORROW         1 (outcome)
                LOAD_GLOBAL              6 (ALLOWED_OUTCOMES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       11 (to L5)
                NOT_TAKEN

 240            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 241            LOAD_CONST               3 ('score')
                LOAD_CONST               4 (0.0)

 242            LOAD_CONST               5 ('outcome')
                LOAD_CONST               6 (None)

 243            LOAD_CONST               7 ('error_code')
                LOAD_CONST               9 ('invalid_outcome')

 239            BUILD_MAP                4
        L4:     RETURN_VALUE

 245    L5:     LOAD_GLOBAL              9 (float + NULL)
                LOAD_GLOBAL             10 (_OUTCOME_SCORE_TABLE)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_FAST_BORROW         1 (outcome)
                LOAD_CONST               4 (0.0)
                CALL                     2
                CALL                     1
                STORE_FAST               2 (score)

 247            LOAD_FAST_BORROW         2 (score)
                LOAD_CONST               4 (0.0)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN

 248            LOAD_CONST               4 (0.0)
                STORE_FAST               2 (score)

 249    L6:     LOAD_FAST_BORROW         2 (score)
                LOAD_CONST              10 (1.0)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN

 250            LOAD_CONST              10 (1.0)
                STORE_FAST               2 (score)

 252    L7:     LOAD_CONST               1 ('status')
                LOAD_CONST              11 ('ok')

 253            LOAD_CONST               3 ('score')
                LOAD_FAST_BORROW         2 (score)

 254            LOAD_CONST               5 ('outcome')
                LOAD_FAST_BORROW         1 (outcome)

 255            LOAD_CONST               7 ('error_code')
                LOAD_CONST               6 (None)

 251            BUILD_MAP                4
        L8:     RETURN_VALUE

  --    L9:     PUSH_EXC_INFO

 257            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L14)
                NOT_TAKEN
                STORE_FAST               3 (e)

 258   L10:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 259            LOAD_CONST              12 ('score_outcome_feedback error type=')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 258            CALL                     1
                POP_TOP

 262            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 263            LOAD_CONST               3 ('score')
                LOAD_CONST               4 (0.0)

 264            LOAD_CONST               5 ('outcome')
                LOAD_CONST               6 (None)

 265            LOAD_CONST               7 ('error_code')
                LOAD_CONST              13 ('unexpected:')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 261            BUILD_MAP                4
       L11:     SWAP                     2
       L12:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L13:     LOAD_CONST               6 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 257   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L9 [0]
  L3 to L4 -> L9 [0]
  L5 to L8 -> L9 [0]
  L9 to L10 -> L15 [1] lasti
  L10 to L11 -> L13 [1] lasti
  L11 to L12 -> L15 [1] lasti
  L13 to L15 -> L15 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app/services/learning/outcome_feedback.py", line 269>:
269           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('feedback_list')
              LOAD_CONST               2 ('Iterable[Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object feedback_summary at 0x0000018C17F749F0, file "app/services/learning/outcome_feedback.py", line 269>:
 269            RESUME                   0

 272            NOP

 273    L1:     LOAD_GLOBAL              0 (ALLOWED_OUTCOMES)
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (o)
                SWAP                     2
        L2:     BUILD_MAP                0
                SWAP                     2
        L3:     FOR_ITER                 5 (to L4)
                STORE_FAST_LOAD_FAST    17 (o, o)
                LOAD_SMALL_INT           0
                MAP_ADD                  2
                JUMP_BACKWARD            7 (to L3)
        L4:     END_FOR
                POP_ITER
        L5:     STORE_FAST               2 (counts)
                STORE_FAST               1 (o)

 274            LOAD_SMALL_INT           0
                STORE_FAST               3 (total)

 275            LOAD_CONST               1 (0.0)
                STORE_FAST               4 (score_sum)

 276            LOAD_FAST                0 (feedback_list)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                LOAD_CONST              14 (())
        L8:     GET_ITER
        L9:     FOR_ITER               131 (to L12)
                STORE_FAST               5 (fb)

 277            LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (fb)
                LOAD_GLOBAL              4 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN

 278            JUMP_BACKWARD           27 (to L9)

 279   L10:     LOAD_FAST_BORROW         5 (fb)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               2 ('outcome')
                CALL                     1
                STORE_FAST               6 (outcome)

 280            LOAD_FAST_BORROW         6 (outcome)
                LOAD_GLOBAL              0 (ALLOWED_OUTCOMES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN

 281            JUMP_BACKWARD           57 (to L9)

 282   L11:     LOAD_FAST_BORROW         2 (counts)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_FAST_BORROW         6 (outcome)
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 38 (counts, outcome)
                STORE_SUBSCR

 283            LOAD_FAST_BORROW         3 (total)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               3 (total)

 284            LOAD_FAST_BORROW         4 (score_sum)
                LOAD_GLOBAL              9 (float + NULL)
                LOAD_GLOBAL             10 (_OUTCOME_SCORE_TABLE)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_FAST_BORROW         6 (outcome)
                LOAD_CONST               1 (0.0)
                CALL                     2
                CALL                     1
                BINARY_OP               13 (+=)
                STORE_FAST               4 (score_sum)
                JUMP_BACKWARD          133 (to L9)

 276   L12:     END_FOR
                POP_ITER

 285            LOAD_FAST_BORROW         3 (total)
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        9 (to L13)
                NOT_TAKEN
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (score_sum, total)
                BINARY_OP               11 (/)
                JUMP_FORWARD             1 (to L14)
       L13:     LOAD_CONST               1 (0.0)
       L14:     STORE_FAST               7 (avg)

 287            LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('ok')

 288            LOAD_CONST               5 ('total')
                LOAD_FAST_BORROW         3 (total)

 289            LOAD_CONST               6 ('by_outcome')
                LOAD_FAST_BORROW         2 (counts)

 290            LOAD_CONST               7 ('average_score')
                LOAD_GLOBAL             13 (round + NULL)
                LOAD_FAST_BORROW         7 (avg)
                LOAD_SMALL_INT           4
                CALL                     2

 291            LOAD_CONST               8 ('warnings')
                BUILD_LIST               0

 292            LOAD_CONST               9 ('error_code')
                LOAD_CONST              10 (None)

 286            BUILD_MAP                6
       L15:     RETURN_VALUE

  --   L16:     SWAP                     2
                POP_TOP

 273            SWAP                     2
                STORE_FAST               1 (o)
                RERAISE                  0

  --   L17:     PUSH_EXC_INFO

 294            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      113 (to L22)
                NOT_TAKEN
                STORE_FAST               8 (e)

 295   L18:     LOAD_GLOBAL             16 (logger)
                LOAD_ATTR               19 (warning + NULL|self)

 296            LOAD_CONST              11 ('feedback_summary error type=')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 295            CALL                     1
                POP_TOP

 299            LOAD_CONST               3 ('status')
                LOAD_CONST              12 ('failed')

 300            LOAD_CONST               5 ('total')
                LOAD_SMALL_INT           0

 301            LOAD_CONST               6 ('by_outcome')
                BUILD_MAP                0

 302            LOAD_CONST               7 ('average_score')
                LOAD_CONST               1 (0.0)

 303            LOAD_CONST               8 ('warnings')
                LOAD_CONST              13 ('unexpected:')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 304            LOAD_CONST               9 ('error_code')
                LOAD_CONST              13 ('unexpected:')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 298            BUILD_MAP                6
       L19:     SWAP                     2
       L20:     POP_EXCEPT
                LOAD_CONST              10 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RETURN_VALUE

  --   L21:     LOAD_CONST              10 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 294   L22:     RERAISE                  0

  --   L23:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L17 [0]
  L2 to L5 -> L16 [2]
  L5 to L6 -> L17 [0]
  L7 to L15 -> L17 [0]
  L16 to L17 -> L17 [0]
  L17 to L18 -> L23 [1] lasti
  L18 to L19 -> L21 [1] lasti
  L19 to L20 -> L23 [1] lasti
  L21 to L23 -> L23 [1] lasti
```
