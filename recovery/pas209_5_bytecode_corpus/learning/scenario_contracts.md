# learning/scenario_contracts

- **pyc:** `app\services\learning\__pycache__\scenario_contracts.cpython-314.pyc`
- **expected source path (absent):** `app\services\learning/scenario_contracts.py`
- **co_filename (from bytecode):** `app/services/learning/scenario_contracts.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** learning

## Module docstring

```
PAS179 — Deterministic scenario contracts.

Closed structural shapes for the 8 PAS179 scenario types. Each
contract:

* Accepts only sanitised structural fields. Forbidden fields
  (phone, email, name, raw_body, transcript, raw_payload, ...)
  fail closed at validation.
* Carries a tenant-scoped ``brokerage_id``.
* Has a deterministic ``scenario_fingerprint`` — sha256 hex
  over the canonical JSON of the closed allow-list of fields.
* Has a closed-token ``scenario_type``.
* NEVER raises.

Doctrine:

* **No PII.** Forbidden fields rejected before fingerprinting.
* **Deterministic.** Same canonical envelope → byte-identical
  fingerprint.
* **No external calls.** Pure functions only — no LLM, no DB,
  no I/O.
* **Closed enums.** ``ALLOWED_SCENARIO_TYPES`` mirrors v29
  CHECK constraints.
* **Tenant-scoped.** Brokerage_id required and bounded.

Public surface:

  * ``ALLOWED_SCENARIO_TYPES``                          — closed enum
  * ``FORBIDDEN_SCENARIO_FIELDS``                       — PII blocklist
  * ``ALLOWED_SCENARIO_FIELDS[scenario_type]``          — per-type allow-list
  * ``build_scenario(scenario_type, payload, brokerage_id)`` — projector
  * ``scenario_fingerprint(scenario_envelope)``         — sha256 hex
  * ``LeadResponseScenario`` and the other 7 typed constructors
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `hashlib`, `json`, `logging`, `typing`

## Classes

`BookingFlowScenario`, `CallbackFlowScenario`, `DuplicateSuppressionScenario`, `LeadResponseScenario`, `MemoryInjectionEffectScenario`, `ObjectionHandlingScenario`, `ProviderFailureScenario`, `WorkerFailureScenario`

## Functions / methods

`__annotate__`, `_bound_brokerage_id`, `_canonical_json`, `_is_safe_value`, `_project`, `_safe_envelope`, `_scan_forbidden_keys`, `build_scenario`, `scenario_fingerprint`

## Env-key candidates

`ALLOWED_SCENARIO_FIELDS`, `ALLOWED_SCENARIO_TYPES`, `BOOKING_FLOW`, `CALLBACK_FLOW`, `DUPLICATE_SUPPRESSION`, `FORBIDDEN_SCENARIO_FIELDS`, `LEAD_RESPONSE`, `MEMORY_INJECTION_EFFECT`, `OBJECTION_HANDLING`, `PROVIDER_FAILURE`, `WORKER_FAILURE`

## String constants (redacted where noted)

- '\nPAS179 — Deterministic scenario contracts.\n\nClosed structural shapes for the 8 PAS179 scenario types. Each\ncontract:\n\n* Accepts only sanitised structural fields. Forbidden fields\n  (phone, email, name, raw_body, transcript, raw_payload, ...)\n  fail closed at validation.\n* Carries a tenant-scoped ``brokerage_id``.\n* Has a deterministic ``scenario_fingerprint`` — sha256 hex\n  over the canonical JSON of the closed allow-list of fields.\n* Has a closed-token ``scenario_type``.\n* NEVER raises.\n\nDoctrine:\n\n* **No PII.** Forbidden fields rejected before fingerprinting.\n* **Deterministic.** Same canonical envelope → byte-identical\n  fingerprint.\n* **No external calls.** Pure functions only — no LLM, no DB,\n  no I/O.\n* **Closed enums.** ``ALLOWED_SCENARIO_TYPES`` mirrors v29\n  CHECK constraints.\n* **Tenant-scoped.** Brokerage_id required and bounded.\n\nPublic surface:\n\n  * ``ALLOWED_SCENARIO_TYPES``                          — closed enum\n  * ``FORBIDDEN_SCENARIO_FIELDS``                       — PII blocklist\n  * ``ALLOWED_SCENARIO_FIELDS[scenario_type]``          — per-type allow-list\n  * ``build_scenario(scenario_type, payload, brokerage_id)`` — projector\n  * ``scenario_fingerprint(scenario_envelope)``         — sha256 hex\n  * ``LeadResponseScenario`` and the other 7 typed constructors\n'
- 'pas.learning.scenario_contracts'
- 'LEAD_RESPONSE'
- 'OBJECTION_HANDLING'
- 'CALLBACK_FLOW'
- 'BOOKING_FLOW'
- 'DUPLICATE_SUPPRESSION'
- 'WORKER_FAILURE'
- 'PROVIDER_FAILURE'
- 'MEMORY_INJECTION_EFFECT'
- 'Tuple[str, ...]'
- 'ALLOWED_SCENARIO_TYPES'
- 'FORBIDDEN_SCENARIO_FIELDS'
- 'Dict[str, Tuple[str, ...]]'
- 'ALLOWED_SCENARIO_FIELDS'
- 'payload'
- 'fingerprint'
- 'warnings'
- 'error_code'
- 'value'
- 'Any'
- 'return'
- 'Optional[str]'
- 'bool'
- 'Closed-shape primitive: bool / int / float / None /\nbounded string.'
- 'List[str]'
- 'Return the list of forbidden keys present anywhere in\nthe payload (case-insensitive).'
- 'status'
- 'str'
- 'scenario_type'
- 'brokerage_id'
- 'Optional[Dict[str, Any]]'
- 'Optional[List[str]]'
- 'Dict[str, Any]'
- 'Tuple[Dict[str, Any], List[str]]'
- 'Return (projected_payload, dropped_keys). Allow-list is\nclosed per scenario.'
- 'envelope'
- 'scenario_envelope'
- 'Deterministic sha256 over the canonical scenario\nenvelope. NEVER raises. Returns the zero-digest for\nmalformed input.'
- 'utf-8'
- 'scenario_fingerprint error type='
- 'Project the payload against the per-scenario allow-list,\nreject forbidden keys, and emit a structural scenario\nenvelope + deterministic fingerprint. NEVER raises.'
- 'failed'
- 'invalid_scenario_type'
- 'missing_brokerage_id'
- 'forbidden_field:'
- 'forbidden_scenario_field'
- 'dropped_unknown:'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS179 — Deterministic scenario contracts.\n\nClosed structural shapes for the 8 PAS179 scenario types. Each\ncontract:\n\n* Accepts only sanitised structural fields. Forbidden fields\n  (phone, email, name, raw_body, transcript, raw_payload, ...)\n  fail closed at validation.\n* Carries a tenant-scoped ``brokerage_id``.\n* Has a deterministic ``scenario_fingerprint`` — sha256 hex\n  over the canonical JSON of the closed allow-list of fields.\n* Has a closed-token ``scenario_type``.\n* NEVER raises.\n\nDoctrine:\n\n* **No PII.** Forbidden fields rejected before fingerprinting.\n* **Deterministic.** Same canonical envelope → byte-identical\n  fingerprint.\n* **No external calls.** Pure functions only — no LLM, no DB,\n  no I/O.\n* **Closed enums.** ``ALLOWED_SCENARIO_TYPES`` mirrors v29\n  CHECK constraints.\n* **Tenant-scoped.** Brokerage_id required and bounded.\n\nPublic surface:\n\n  * ``ALLOWED_SCENARIO_TYPES``                          — closed enum\n  * ``FORBIDDEN_SCENARIO_FIELDS``                       — PII blocklist\n  * ``ALLOWED_SCENARIO_FIELDS[scenario_type]``          — per-type allow-list\n  * ``build_scenario(scenario_type, payload, brokerage_id)`` — projector\n  * ``scenario_fingerprint(scenario_envelope)``         — sha256 hex\n  * ``LeadResponseScenario`` and the other 7 typed constructors\n')
               STORE_NAME               1 (__doc__)

  37           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  39           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (hashlib)
               STORE_NAME               4 (hashlib)

  40           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (json)
               STORE_NAME               5 (json)

  41           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (logging)
               STORE_NAME               6 (logging)

  42           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME              7 (typing)
               IMPORT_FROM              8 (Any)
               STORE_NAME               8 (Any)
               IMPORT_FROM              9 (Dict)
               STORE_NAME               9 (Dict)
               IMPORT_FROM             10 (List)
               STORE_NAME              10 (List)
               IMPORT_FROM             11 (Optional)
               STORE_NAME              11 (Optional)
               IMPORT_FROM             12 (Tuple)
               STORE_NAME              12 (Tuple)
               POP_TOP

  45           LOAD_NAME                6 (logging)
               LOAD_ATTR               26 (getLogger)
               PUSH_NULL
               LOAD_CONST               4 ('pas.learning.scenario_contracts')
               CALL                     1
               STORE_NAME              14 (logger)

  49           LOAD_CONST              54 (('LEAD_RESPONSE', 'OBJECTION_HANDLING', 'CALLBACK_FLOW', 'BOOKING_FLOW', 'DUPLICATE_SUPPRESSION', 'WORKER_FAILURE', 'PROVIDER_FAILURE', 'MEMORY_INJECTION_EFFECT'))
               STORE_NAME              15 (ALLOWED_SCENARIO_TYPES)
               LOAD_CONST              13 ('Tuple[str, ...]')
               LOAD_NAME               16 (__annotations__)
               LOAD_CONST              14 ('ALLOWED_SCENARIO_TYPES')
               STORE_SUBSCR

  63           LOAD_CONST              55 (('phone', 'email', 'name', 'raw_payload', 'raw_email', 'raw_body', 'transcript', 'summary', 'summary_text', 'secret', 'signature', 'env_value', 'env_values', 'dedupe_key', 'callback_notes', 'rationale_text', 'rationale_freeform', 'first_name', 'last_name', 'full_name', 'address', 'street'))
               STORE_NAME              17 (FORBIDDEN_SCENARIO_FIELDS)
               LOAD_CONST              13 ('Tuple[str, ...]')
               LOAD_NAME               16 (__annotations__)
               LOAD_CONST              15 ('FORBIDDEN_SCENARIO_FIELDS')
               STORE_SUBSCR

  80           LOAD_CONST               5 ('LEAD_RESPONSE')
               LOAD_CONST              56 (('lead_source', 'intent_token', 'budget_band', 'timeline_band', 'has_callback_token', 'expected_response_token'))

  85           LOAD_CONST               6 ('OBJECTION_HANDLING')
               LOAD_CONST              57 (('objection_token', 'stage_token', 'expected_resolution_token', 'memory_inject_token'))

  89           LOAD_CONST               7 ('CALLBACK_FLOW')
               LOAD_CONST              58 (('callback_window_token', 'lead_priority_band', 'expected_outcome_token'))

  93           LOAD_CONST               8 ('BOOKING_FLOW')
               LOAD_CONST              59 (('intent_token', 'timeline_band', 'calendar_token', 'expected_booking_outcome_token'))

  97           LOAD_CONST               9 ('DUPLICATE_SUPPRESSION')
               LOAD_CONST              60 (('source_token', 'dedupe_window_band', 'expected_suppression_token'))

 101           LOAD_CONST              10 ('WORKER_FAILURE')
               LOAD_CONST              61 (('failure_token', 'retry_band', 'expected_recovery_token'))

 105           LOAD_CONST              11 ('PROVIDER_FAILURE')
               LOAD_CONST              62 (('provider_token', 'failure_token', 'expected_fallback_token'))

 109           LOAD_CONST              12 ('MEMORY_INJECTION_EFFECT')
               LOAD_CONST              63 (('memory_inject_token', 'stage_token', 'expected_effect_token'))

  79           BUILD_MAP                8
               STORE_NAME              18 (ALLOWED_SCENARIO_FIELDS)
               LOAD_CONST              16 ('Dict[str, Tuple[str, ...]]')
               LOAD_NAME               16 (__annotations__)
               LOAD_CONST              17 ('ALLOWED_SCENARIO_FIELDS')
               STORE_SUBSCR

 116           LOAD_SMALL_INT         200
               STORE_NAME              19 (_BROKERAGE_ID_MAX_LEN)

 117           LOAD_SMALL_INT         200
               STORE_NAME              20 (_VALUE_MAX_LEN)

 120           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3690, file "app/services/learning/scenario_contracts.py", line 120>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _bound_brokerage_id at 0x0000018C17F95CF0, file "app/services/learning/scenario_contracts.py", line 120>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              21 (_bound_brokerage_id)

 129           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA34B0, file "app/services/learning/scenario_contracts.py", line 129>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _is_safe_value at 0x0000018C17FF13B0, file "app/services/learning/scenario_contracts.py", line 129>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              22 (_is_safe_value)

 139           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3870, file "app/services/learning/scenario_contracts.py", line 139>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _scan_forbidden_keys at 0x0000018C179C3A50, file "app/services/learning/scenario_contracts.py", line 139>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              23 (_scan_forbidden_keys)

 156           LOAD_CONST              24 ('payload')

 161           LOAD_CONST               2 (None)

 156           LOAD_CONST              25 ('fingerprint')

 162           LOAD_CONST               2 (None)

 156           LOAD_CONST              26 ('warnings')

 163           LOAD_CONST               2 (None)

 156           LOAD_CONST              27 ('error_code')

 164           LOAD_CONST               2 (None)

 156           BUILD_MAP                4
               LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FBFEE0, file "app/services/learning/scenario_contracts.py", line 156>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object _safe_envelope at 0x0000018C18053090, file "app/services/learning/scenario_contracts.py", line 156>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              24 (_safe_envelope)

 177           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C18025C30, file "app/services/learning/scenario_contracts.py", line 177>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object _project at 0x0000018C17FEDA30, file "app/services/learning/scenario_contracts.py", line 177>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              25 (_project)

 198           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA3B40, file "app/services/learning/scenario_contracts.py", line 198>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object _canonical_json at 0x0000018C180908B0, file "app/services/learning/scenario_contracts.py", line 198>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              26 (_canonical_json)

 202           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA21F0, file "app/services/learning/scenario_contracts.py", line 202>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object scenario_fingerprint at 0x0000018C17ED9FB0, file "app/services/learning/scenario_contracts.py", line 202>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              27 (scenario_fingerprint)

 222           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C18024D30, file "app/services/learning/scenario_contracts.py", line 222>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object build_scenario at 0x0000018C17D8CD10, file "app/services/learning/scenario_contracts.py", line 222>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (build_scenario)

 277           LOAD_CONST              64 ((None,))
               LOAD_CONST              38 (<code object __annotate__ at 0x0000018C18025230, file "app/services/learning/scenario_contracts.py", line 277>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object LeadResponseScenario at 0x0000018C18090030, file "app/services/learning/scenario_contracts.py", line 277>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              29 (LeadResponseScenario)

 285           LOAD_CONST              64 ((None,))
               LOAD_CONST              40 (<code object __annotate__ at 0x0000018C18025D30, file "app/services/learning/scenario_contracts.py", line 285>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object ObjectionHandlingScenario at 0x0000018C18090250, file "app/services/learning/scenario_contracts.py", line 285>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              30 (ObjectionHandlingScenario)

 293           LOAD_CONST              64 ((None,))
               LOAD_CONST              42 (<code object __annotate__ at 0x0000018C18025730, file "app/services/learning/scenario_contracts.py", line 293>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object CallbackFlowScenario at 0x0000018C18090690, file "app/services/learning/scenario_contracts.py", line 293>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              31 (CallbackFlowScenario)

 301           LOAD_CONST              64 ((None,))
               LOAD_CONST              44 (<code object __annotate__ at 0x0000018C18025030, file "app/services/learning/scenario_contracts.py", line 301>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object BookingFlowScenario at 0x0000018C180907A0, file "app/services/learning/scenario_contracts.py", line 301>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              32 (BookingFlowScenario)

 309           LOAD_CONST              64 ((None,))
               LOAD_CONST              46 (<code object __annotate__ at 0x0000018C18024E30, file "app/services/learning/scenario_contracts.py", line 309>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object DuplicateSuppressionScenario at 0x0000018C18090470, file "app/services/learning/scenario_contracts.py", line 309>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              33 (DuplicateSuppressionScenario)

 317           LOAD_CONST              64 ((None,))
               LOAD_CONST              48 (<code object __annotate__ at 0x0000018C18025E30, file "app/services/learning/scenario_contracts.py", line 317>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object WorkerFailureScenario at 0x0000018C18090AD0, file "app/services/learning/scenario_contracts.py", line 317>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              34 (WorkerFailureScenario)

 325           LOAD_CONST              64 ((None,))
               LOAD_CONST              50 (<code object __annotate__ at 0x0000018C18024B30, file "app/services/learning/scenario_contracts.py", line 325>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object ProviderFailureScenario at 0x0000018C18090BE0, file "app/services/learning/scenario_contracts.py", line 325>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              35 (ProviderFailureScenario)

 333           LOAD_CONST              64 ((None,))
               LOAD_CONST              52 (<code object __annotate__ at 0x0000018C18025F30, file "app/services/learning/scenario_contracts.py", line 333>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object MemoryInjectionEffectScenario at 0x0000018C18090CF0, file "app/services/learning/scenario_contracts.py", line 333>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              36 (MemoryInjectionEffectScenario)

 341           BUILD_LIST               0
               LOAD_CONST              65 (('ALLOWED_SCENARIO_TYPES', 'FORBIDDEN_SCENARIO_FIELDS', 'ALLOWED_SCENARIO_FIELDS', 'build_scenario', 'scenario_fingerprint', 'LeadResponseScenario', 'ObjectionHandlingScenario', 'CallbackFlowScenario', 'BookingFlowScenario', 'DuplicateSuppressionScenario', 'WorkerFailureScenario', 'ProviderFailureScenario', 'MemoryInjectionEffectScenario'))
               LIST_EXTEND              1
               STORE_NAME              37 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app/services/learning/scenario_contracts.py", line 120>:
120           RESUME                   0
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

Disassembly of <code object _bound_brokerage_id at 0x0000018C17F95CF0, file "app/services/learning/scenario_contracts.py", line 120>:
120           RESUME                   0

121           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

122           LOAD_CONST               0 (None)
              RETURN_VALUE

123   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

124           LOAD_FAST_BORROW         1 (s)
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

125   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

126   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app/services/learning/scenario_contracts.py", line 129>:
129           RESUME                   0
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

Disassembly of <code object _is_safe_value at 0x0000018C17FF13B0, file "app/services/learning/scenario_contracts.py", line 129>:
129           RESUME                   0

132           LOAD_FAST_BORROW         0 (v)
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

133   L1:     LOAD_CONST               1 (True)
              RETURN_VALUE

134   L2:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (v)
              LOAD_GLOBAL              8 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L3)
              NOT_TAKEN
              LOAD_GLOBAL             11 (len + NULL)
              LOAD_FAST_BORROW         0 (v)
              CALL                     1
              LOAD_GLOBAL             12 (_VALUE_MAX_LEN)
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

135           LOAD_CONST               1 (True)
              RETURN_VALUE

136   L3:     LOAD_CONST               2 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app/services/learning/scenario_contracts.py", line 139>:
139           RESUME                   0
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

Disassembly of <code object _scan_forbidden_keys at 0x0000018C179C3A50, file "app/services/learning/scenario_contracts.py", line 139>:
139           RESUME                   0

142           BUILD_LIST               0
              STORE_FAST               1 (bad)

143           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (payload)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

144           LOAD_FAST_BORROW         1 (bad)
              RETURN_VALUE

145   L1:     LOAD_FAST_BORROW         0 (payload)
              LOAD_ATTR                5 (keys + NULL|self)
              CALL                     0
              GET_ITER
      L2:     FOR_ITER                82 (to L7)
              STORE_FAST               2 (k)

146           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (k)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

147           JUMP_BACKWARD           27 (to L2)

148   L3:     LOAD_FAST_BORROW         2 (k)
              LOAD_ATTR                9 (lower + NULL|self)
              CALL                     0
              STORE_FAST               3 (kl)

149           LOAD_GLOBAL             10 (FORBIDDEN_SCENARIO_FIELDS)
              GET_ITER
      L4:     FOR_ITER                29 (to L6)
              STORE_FAST               4 (forb)

150           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (forb, kl)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L4)

151   L5:     LOAD_FAST_BORROW         1 (bad)
              LOAD_ATTR               13 (append + NULL|self)
              LOAD_FAST_BORROW         2 (k)
              CALL                     1
              POP_TOP

152           POP_TOP
              JUMP_BACKWARD           80 (to L2)

149   L6:     END_FOR
              POP_ITER
              JUMP_BACKWARD           84 (to L2)

145   L7:     END_FOR
              POP_ITER

153           LOAD_FAST_BORROW         1 (bad)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FBFEE0, file "app/services/learning/scenario_contracts.py", line 156>:
156           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

158           LOAD_CONST               2 ('str')

156           LOAD_CONST               3 ('scenario_type')

159           LOAD_CONST               4 ('Optional[str]')

156           LOAD_CONST               5 ('brokerage_id')

160           LOAD_CONST               4 ('Optional[str]')

156           LOAD_CONST               6 ('payload')

161           LOAD_CONST               7 ('Optional[Dict[str, Any]]')

156           LOAD_CONST               8 ('fingerprint')

162           LOAD_CONST               4 ('Optional[str]')

156           LOAD_CONST               9 ('warnings')

163           LOAD_CONST              10 ('Optional[List[str]]')

156           LOAD_CONST              11 ('error_code')

164           LOAD_CONST               4 ('Optional[str]')

156           LOAD_CONST              12 ('return')

165           LOAD_CONST              13 ('Dict[str, Any]')

156           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C18053090, file "app/services/learning/scenario_contracts.py", line 156>:
156           RESUME                   0

167           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

168           LOAD_CONST               1 ('scenario_type')
              LOAD_FAST                1 (scenario_type)

169           LOAD_CONST               2 ('brokerage_id')
              LOAD_FAST                2 (brokerage_id)

170           LOAD_CONST               3 ('payload')
              LOAD_FAST                3 (payload)

171           LOAD_CONST               4 ('fingerprint')
              LOAD_FAST                4 (fingerprint)

172           LOAD_CONST               5 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                5 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

173           LOAD_CONST               6 ('error_code')
              LOAD_FAST_BORROW         6 (error_code)

166           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app/services/learning/scenario_contracts.py", line 177>:
177           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('scenario_type')

178           LOAD_CONST               2 ('str')

177           LOAD_CONST               3 ('payload')

179           LOAD_CONST               4 ('Any')

177           LOAD_CONST               5 ('return')

180           LOAD_CONST               6 ('Tuple[Dict[str, Any], List[str]]')

177           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _project at 0x0000018C17FEDA30, file "app/services/learning/scenario_contracts.py", line 177>:
177           RESUME                   0

183           LOAD_GLOBAL              0 (ALLOWED_SCENARIO_FIELDS)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_FAST_BORROW         0 (scenario_type)
              LOAD_CONST               1 (())
              CALL                     2
              STORE_FAST               2 (allowed)

184           BUILD_MAP                0
              STORE_FAST               3 (out)

185           BUILD_LIST               0
              STORE_FAST               4 (dropped)

186           LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (payload)
              LOAD_GLOBAL              6 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         4 (to L1)
              NOT_TAKEN

187           LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (out, dropped)
              BUILD_TUPLE              2
              RETURN_VALUE

188   L1:     LOAD_FAST_BORROW         1 (payload)
              LOAD_ATTR                9 (items + NULL|self)
              CALL                     0
              GET_ITER
      L2:     FOR_ITER                75 (to L5)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   86 (k, v)

189           LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         5 (k)
              LOAD_GLOBAL             10 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

190           JUMP_BACKWARD           29 (to L2)

191   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 82 (k, allowed)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       24 (to L4)
              NOT_TAKEN
              LOAD_GLOBAL             13 (_is_safe_value + NULL)
              LOAD_FAST_BORROW         6 (v)
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        7 (to L4)
              NOT_TAKEN

192           LOAD_FAST_BORROW_LOAD_FAST_BORROW 99 (v, out)
              LOAD_FAST_BORROW         5 (k)
              STORE_SUBSCR
              JUMP_BACKWARD           58 (to L2)

194   L4:     LOAD_FAST_BORROW         4 (dropped)
              LOAD_ATTR               15 (append + NULL|self)
              LOAD_FAST_BORROW         5 (k)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           77 (to L2)

188   L5:     END_FOR
              POP_ITER

195           LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (out, dropped)
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app/services/learning/scenario_contracts.py", line 198>:
198           RESUME                   0
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

Disassembly of <code object _canonical_json at 0x0000018C180908B0, file "app/services/learning/scenario_contracts.py", line 198>:
198           RESUME                   0

199           LOAD_GLOBAL              0 (json)
              LOAD_ATTR                2 (dumps)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (envelope)
              LOAD_CONST               0 (True)
              LOAD_CONST               2 ((',', ':'))
              LOAD_CONST               1 (('sort_keys', 'separators'))
              CALL_KW                  3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app/services/learning/scenario_contracts.py", line 202>:
202           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('scenario_envelope')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object scenario_fingerprint at 0x0000018C17ED9FB0, file "app/services/learning/scenario_contracts.py", line 202>:
 202            RESUME                   0

 206            NOP

 207    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (scenario_envelope)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        37 (to L3)
                NOT_TAKEN

 208            LOAD_GLOBAL              4 (hashlib)
                LOAD_ATTR                6 (sha256)
                PUSH_NULL
                LOAD_CONST               1 (b'')
                CALL                     1
                LOAD_ATTR                9 (hexdigest + NULL|self)
                CALL                     0
        L2:     RETURN_VALUE

 209    L3:     LOAD_GLOBAL             11 (_canonical_json + NULL)

 210            LOAD_CONST               2 ('scenario_type')
                LOAD_FAST_BORROW         0 (scenario_envelope)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               2 ('scenario_type')
                CALL                     1

 211            LOAD_CONST               3 ('brokerage_id')
                LOAD_FAST_BORROW         0 (scenario_envelope)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               3 ('brokerage_id')
                CALL                     1

 212            LOAD_CONST               4 ('payload')
                LOAD_FAST_BORROW         0 (scenario_envelope)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               4 ('payload')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
        L4:     NOT_TAKEN
        L5:     POP_TOP
                BUILD_MAP                0

 209    L6:     BUILD_MAP                3
                CALL                     1
                STORE_FAST               1 (canonical)

 214            LOAD_GLOBAL              4 (hashlib)
                LOAD_ATTR                6 (sha256)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (canonical)
                LOAD_ATTR               15 (encode + NULL|self)
                LOAD_CONST               5 ('utf-8')
                CALL                     1
                CALL                     1
                LOAD_ATTR                9 (hexdigest + NULL|self)
                CALL                     0
        L7:     RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

 215            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       90 (to L13)
                NOT_TAKEN
                STORE_FAST               2 (e)

 216    L9:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 217            LOAD_CONST               6 ('scenario_fingerprint error type=')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                2 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 216            CALL                     1
                POP_TOP

 219            LOAD_GLOBAL              4 (hashlib)
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

 215   L13:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18024D30, file "app/services/learning/scenario_contracts.py", line 222>:
222           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('scenario_type')

224           LOAD_CONST               2 ('str')

222           LOAD_CONST               3 ('payload')

225           LOAD_CONST               4 ('Any')

222           LOAD_CONST               5 ('brokerage_id')

226           LOAD_CONST               4 ('Any')

222           LOAD_CONST               6 ('return')

227           LOAD_CONST               7 ('Dict[str, Any]')

222           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object build_scenario at 0x0000018C17D8CD10, file "app/services/learning/scenario_contracts.py", line 222>:
 222            RESUME                   0

 231            LOAD_FAST_BORROW         0 (scenario_type)
                LOAD_GLOBAL              0 (ALLOWED_SCENARIO_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       16 (to L1)
                NOT_TAKEN

 232            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 233            LOAD_CONST               1 ('failed')

 234            LOAD_CONST               2 (None)

 235            LOAD_CONST               2 (None)

 236            LOAD_CONST               3 ('invalid_scenario_type')

 232            LOAD_CONST               4 (('status', 'scenario_type', 'brokerage_id', 'error_code'))
                CALL_KW                  4
                RETURN_VALUE

 238    L1:     LOAD_GLOBAL              5 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         2 (brokerage_id)
                CALL                     1
                STORE_FAST               3 (bid)

 239            LOAD_FAST_BORROW         3 (bid)
                POP_JUMP_IF_NOT_NONE    16 (to L2)
                NOT_TAKEN

 240            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 241            LOAD_CONST               1 ('failed')

 242            LOAD_FAST_BORROW         0 (scenario_type)

 243            LOAD_CONST               2 (None)

 244            LOAD_CONST               5 ('missing_brokerage_id')

 240            LOAD_CONST               4 (('status', 'scenario_type', 'brokerage_id', 'error_code'))
                CALL_KW                  4
                RETURN_VALUE

 246    L2:     LOAD_GLOBAL              7 (_scan_forbidden_keys + NULL)
                LOAD_FAST_BORROW         1 (payload)
                CALL                     1
                STORE_FAST               4 (forbidden)

 247            LOAD_FAST_BORROW         4 (forbidden)
                TO_BOOL
                POP_JUMP_IF_FALSE       43 (to L7)
                NOT_TAKEN

 248            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 249            LOAD_CONST               1 ('failed')

 250            LOAD_FAST                0 (scenario_type)

 251            LOAD_FAST                3 (bid)

 252            LOAD_FAST_BORROW         4 (forbidden)
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

 253            LOAD_CONST               8 ('forbidden_scenario_field')

 248            LOAD_CONST               9 (('status', 'scenario_type', 'brokerage_id', 'warnings', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

 255    L7:     LOAD_GLOBAL              9 (_project + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (scenario_type, payload)
                CALL                     2
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  103 (projected, dropped)

 257            LOAD_CONST              10 ('scenario_type')
                LOAD_FAST_BORROW         0 (scenario_type)

 258            LOAD_CONST              11 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)

 259            LOAD_CONST              12 ('payload')
                LOAD_FAST_BORROW         6 (projected)

 256            BUILD_MAP                3
                STORE_FAST               8 (envelope)

 261            LOAD_GLOBAL             11 (scenario_fingerprint + NULL)
                LOAD_FAST_BORROW         8 (envelope)
                CALL                     1
                STORE_FAST               9 (fp)

 262            LOAD_FAST_BORROW         7 (dropped)
                LOAD_CONST               6 (slice(None, 5, None))
                BINARY_OP               26 ([])
                GET_ITER
                LOAD_FAST_AND_CLEAR      5 (k)
                SWAP                     2
        L8:     BUILD_LIST               0
                SWAP                     2
        L9:     FOR_ITER                 8 (to L10)
                STORE_FAST               5 (k)
                LOAD_CONST              13 ('dropped_unknown:')
                LOAD_FAST_BORROW         5 (k)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LIST_APPEND              2
                JUMP_BACKWARD           10 (to L9)
       L10:     END_FOR
                POP_ITER
       L11:     STORE_FAST              10 (warnings)
                STORE_FAST               5 (k)

 263            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 264            LOAD_CONST              14 ('ok')

 265            LOAD_FAST_BORROW         0 (scenario_type)

 266            LOAD_FAST_BORROW         3 (bid)

 267            LOAD_FAST_BORROW         6 (projected)

 268            LOAD_FAST_BORROW         9 (fp)

 269            LOAD_FAST_BORROW        10 (warnings)

 263            LOAD_CONST              15 (('status', 'scenario_type', 'brokerage_id', 'payload', 'fingerprint', 'warnings'))
                CALL_KW                  6
                RETURN_VALUE

  --   L12:     SWAP                     2
                POP_TOP

 252            SWAP                     2
                STORE_FAST               5 (k)
                RERAISE                  0

  --   L13:     SWAP                     2
                POP_TOP

 262            SWAP                     2
                STORE_FAST               5 (k)
                RERAISE                  0
ExceptionTable:
  L3 to L6 -> L12 [7]
  L8 to L11 -> L13 [2]

Disassembly of <code object __annotate__ at 0x0000018C18025230, file "app/services/learning/scenario_contracts.py", line 277>:
277           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('payload')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('Dict[str, Any]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object LeadResponseScenario at 0x0000018C18090030, file "app/services/learning/scenario_contracts.py", line 277>:
277           RESUME                   0

278           LOAD_GLOBAL              1 (build_scenario + NULL)

279           LOAD_CONST               0 ('LEAD_RESPONSE')

280           LOAD_FAST                1 (payload)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0

281   L1:     LOAD_FAST_BORROW         0 (brokerage_id)

278           LOAD_CONST               1 (('scenario_type', 'payload', 'brokerage_id'))
              CALL_KW                  3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app/services/learning/scenario_contracts.py", line 285>:
285           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('payload')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('Dict[str, Any]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object ObjectionHandlingScenario at 0x0000018C18090250, file "app/services/learning/scenario_contracts.py", line 285>:
285           RESUME                   0

286           LOAD_GLOBAL              1 (build_scenario + NULL)

287           LOAD_CONST               0 ('OBJECTION_HANDLING')

288           LOAD_FAST                1 (payload)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0

289   L1:     LOAD_FAST_BORROW         0 (brokerage_id)

286           LOAD_CONST               1 (('scenario_type', 'payload', 'brokerage_id'))
              CALL_KW                  3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app/services/learning/scenario_contracts.py", line 293>:
293           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('payload')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('Dict[str, Any]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object CallbackFlowScenario at 0x0000018C18090690, file "app/services/learning/scenario_contracts.py", line 293>:
293           RESUME                   0

294           LOAD_GLOBAL              1 (build_scenario + NULL)

295           LOAD_CONST               0 ('CALLBACK_FLOW')

296           LOAD_FAST                1 (payload)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0

297   L1:     LOAD_FAST_BORROW         0 (brokerage_id)

294           LOAD_CONST               1 (('scenario_type', 'payload', 'brokerage_id'))
              CALL_KW                  3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "app/services/learning/scenario_contracts.py", line 301>:
301           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('payload')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('Dict[str, Any]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object BookingFlowScenario at 0x0000018C180907A0, file "app/services/learning/scenario_contracts.py", line 301>:
301           RESUME                   0

302           LOAD_GLOBAL              1 (build_scenario + NULL)

303           LOAD_CONST               0 ('BOOKING_FLOW')

304           LOAD_FAST                1 (payload)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0

305   L1:     LOAD_FAST_BORROW         0 (brokerage_id)

302           LOAD_CONST               1 (('scenario_type', 'payload', 'brokerage_id'))
              CALL_KW                  3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app/services/learning/scenario_contracts.py", line 309>:
309           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('payload')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('Dict[str, Any]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object DuplicateSuppressionScenario at 0x0000018C18090470, file "app/services/learning/scenario_contracts.py", line 309>:
309           RESUME                   0

310           LOAD_GLOBAL              1 (build_scenario + NULL)

311           LOAD_CONST               0 ('DUPLICATE_SUPPRESSION')

312           LOAD_FAST                1 (payload)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0

313   L1:     LOAD_FAST_BORROW         0 (brokerage_id)

310           LOAD_CONST               1 (('scenario_type', 'payload', 'brokerage_id'))
              CALL_KW                  3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app/services/learning/scenario_contracts.py", line 317>:
317           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('payload')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('Dict[str, Any]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object WorkerFailureScenario at 0x0000018C18090AD0, file "app/services/learning/scenario_contracts.py", line 317>:
317           RESUME                   0

318           LOAD_GLOBAL              1 (build_scenario + NULL)

319           LOAD_CONST               0 ('WORKER_FAILURE')

320           LOAD_FAST                1 (payload)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0

321   L1:     LOAD_FAST_BORROW         0 (brokerage_id)

318           LOAD_CONST               1 (('scenario_type', 'payload', 'brokerage_id'))
              CALL_KW                  3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app/services/learning/scenario_contracts.py", line 325>:
325           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('payload')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('Dict[str, Any]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object ProviderFailureScenario at 0x0000018C18090BE0, file "app/services/learning/scenario_contracts.py", line 325>:
325           RESUME                   0

326           LOAD_GLOBAL              1 (build_scenario + NULL)

327           LOAD_CONST               0 ('PROVIDER_FAILURE')

328           LOAD_FAST                1 (payload)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0

329   L1:     LOAD_FAST_BORROW         0 (brokerage_id)

326           LOAD_CONST               1 (('scenario_type', 'payload', 'brokerage_id'))
              CALL_KW                  3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "app/services/learning/scenario_contracts.py", line 333>:
333           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('payload')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('Dict[str, Any]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object MemoryInjectionEffectScenario at 0x0000018C18090CF0, file "app/services/learning/scenario_contracts.py", line 333>:
333           RESUME                   0

334           LOAD_GLOBAL              1 (build_scenario + NULL)

335           LOAD_CONST               0 ('MEMORY_INJECTION_EFFECT')

336           LOAD_FAST                1 (payload)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0

337   L1:     LOAD_FAST_BORROW         0 (brokerage_id)

334           LOAD_CONST               1 (('scenario_type', 'payload', 'brokerage_id'))
              CALL_KW                  3
              RETURN_VALUE
```
