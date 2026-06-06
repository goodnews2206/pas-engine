# learning/manual_test_evidence

- **pyc:** `app\services\learning\__pycache__\manual_test_evidence.cpython-314.pyc`
- **expected source path (absent):** `app\services\learning/manual_test_evidence.py`
- **co_filename (from bytecode):** `app/services/learning/manual_test_evidence.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** learning

## Module docstring

```
PAS181 — Bounded evidence packets for manual-test runs.

Builds a closed-shape structural "evidence" record describing
what the simulation observed. NEVER carries raw transcript /
raw payload / PII / rationale_text. The packet is a
deterministic projection of the scenario + recommendation
fingerprints plus a small set of structural counts.

Doctrine:

* **Bounded.** Every field is a sha256 hex digest, a closed
  enum token, or a bounded integer. NEVER freeform prose.
* **Deterministic.** Same canonical inputs → byte-identical
  fingerprint.
* **No external calls.** Pure functions only.
* **NEVER raises.**
* **Tenant projection strictly narrower than operator
  projection** — drops the scenario fingerprint, the
  recommendation_id, the rationale_token, and all internal
  counters.

Public surface:

  * ``FORBIDDEN_EVIDENCE_FIELDS``                   — PII blocklist
  * ``ALLOWED_EVIDENCE_KEYS``                       — closed allow-list
  * ``OPERATOR_EVIDENCE_KEYS``                      — operator projection
  * ``TENANT_EVIDENCE_KEYS``                        — tenant projection
  * ``build_manual_test_evidence_packet(...)``     — pure builder
  * ``evidence_fingerprint(packet)``               — sha256 hex
  * ``evidence_public_projection(packet)``         — tenant-safe
  * ``evidence_operator_projection(packet)``       — operator-safe
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `hashlib`, `json`, `logging`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_canonical_json`, `_is_safe_value`, `_key_is_forbidden`, `_scan_forbidden_keys`, `build_manual_test_evidence_packet`, `evidence_fingerprint`, `evidence_operator_projection`, `evidence_public_projection`

## Env-key candidates

`ALLOWED_EVIDENCE_KEYS`, `FORBIDDEN_EVIDENCE_FIELDS`, `OPERATOR_EVIDENCE_KEYS`, `SIMULATION_ONLY`, `TENANT_EVIDENCE_KEYS`

## String constants (redacted where noted)

- '\nPAS181 — Bounded evidence packets for manual-test runs.\n\nBuilds a closed-shape structural "evidence" record describing\nwhat the simulation observed. NEVER carries raw transcript /\nraw payload / PII / rationale_text. The packet is a\ndeterministic projection of the scenario + recommendation\nfingerprints plus a small set of structural counts.\n\nDoctrine:\n\n* **Bounded.** Every field is a sha256 hex digest, a closed\n  enum token, or a bounded integer. NEVER freeform prose.\n* **Deterministic.** Same canonical inputs → byte-identical\n  fingerprint.\n* **No external calls.** Pure functions only.\n* **NEVER raises.**\n* **Tenant projection strictly narrower than operator\n  projection** — drops the scenario fingerprint, the\n  recommendation_id, the rationale_token, and all internal\n  counters.\n\nPublic surface:\n\n  * ``FORBIDDEN_EVIDENCE_FIELDS``                   — PII blocklist\n  * ``ALLOWED_EVIDENCE_KEYS``                       — closed allow-list\n  * ``OPERATOR_EVIDENCE_KEYS``                      — operator projection\n  * ``TENANT_EVIDENCE_KEYS``                        — tenant projection\n  * ``build_manual_test_evidence_packet(...)``     — pure builder\n  * ``evidence_fingerprint(packet)``               — sha256 hex\n  * ``evidence_public_projection(packet)``         — tenant-safe\n  * ``evidence_operator_projection(packet)``       — operator-safe\n'
- 'pas.learning.manual_test_evidence'
- 'Tuple[str, ...]'
- 'FORBIDDEN_EVIDENCE_FIELDS'
- 'scenario_fingerprint'
- 'mode'
- 'observation_count'
- 'warning_count'
- 'ALLOWED_EVIDENCE_KEYS'
- 'OPERATOR_EVIDENCE_KEYS'
- 'TENANT_EVIDENCE_KEYS'
- 'pas181.v1'
- 'SIMULATION_ONLY'
- 'extra'
- 'Any'
- 'return'
- 'bool'
- 'payload'
- 'List[str]'
- 'envelope'
- 'Dict[str, Any]'
- 'str'
- 'packet'
- 'Deterministic sha256 over the canonical packet envelope.\nNEVER raises.'
- 'utf-8'
- 'evidence_fingerprint error type='
- 'recommendation'
- 'scenario_type'
- 'Optional[str]'
- 'Optional[Dict[str, Any]]'
- 'Build a bounded evidence packet. NEVER raises.\n\nOutcomes:\n  * ``status="ok"`` — packet + fingerprint populated.\n  * ``status="failed"`` — input validation failed (e.g.\n    forbidden field in ``extra``).\n'
- 'status'
- 'failed'
- 'fingerprint'
- 'warnings'
- 'error_code'
- 'invalid_recommendation'
- 'invalid_scenario_type'
- 'invalid_mode'
- 'forbidden_field:'
- 'forbidden_evidence_field'
- 'recommendation_id'
- 'recommendation_type'
- 'rationale_token'
- 'evidence_packet_version'
- '0123456789abcdef'
- 'Operator-side projection. NEVER raises.'
- 'evidence_operator_projection error type='
- 'Tenant-side projection. Strictly narrower than\noperator. NEVER raises. NEVER carries scenario_fingerprint\nor rationale_token.'
- 'evidence_public_projection error type='

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS181 — Bounded evidence packets for manual-test runs.\n\nBuilds a closed-shape structural "evidence" record describing\nwhat the simulation observed. NEVER carries raw transcript /\nraw payload / PII / rationale_text. The packet is a\ndeterministic projection of the scenario + recommendation\nfingerprints plus a small set of structural counts.\n\nDoctrine:\n\n* **Bounded.** Every field is a sha256 hex digest, a closed\n  enum token, or a bounded integer. NEVER freeform prose.\n* **Deterministic.** Same canonical inputs → byte-identical\n  fingerprint.\n* **No external calls.** Pure functions only.\n* **NEVER raises.**\n* **Tenant projection strictly narrower than operator\n  projection** — drops the scenario fingerprint, the\n  recommendation_id, the rationale_token, and all internal\n  counters.\n\nPublic surface:\n\n  * ``FORBIDDEN_EVIDENCE_FIELDS``                   — PII blocklist\n  * ``ALLOWED_EVIDENCE_KEYS``                       — closed allow-list\n  * ``OPERATOR_EVIDENCE_KEYS``                      — operator projection\n  * ``TENANT_EVIDENCE_KEYS``                        — tenant projection\n  * ``build_manual_test_evidence_packet(...)``     — pure builder\n  * ``evidence_fingerprint(packet)``               — sha256 hex\n  * ``evidence_public_projection(packet)``         — tenant-safe\n  * ``evidence_operator_projection(packet)``       — operator-safe\n')
               STORE_NAME               1 (__doc__)

  35           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  37           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (hashlib)
               STORE_NAME               4 (hashlib)

  38           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (json)
               STORE_NAME               5 (json)

  39           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (logging)
               STORE_NAME               6 (logging)

  40           LOAD_SMALL_INT           0
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

  43           LOAD_NAME                6 (logging)
               LOAD_ATTR               26 (getLogger)
               PUSH_NULL
               LOAD_CONST               4 ('pas.learning.manual_test_evidence')
               CALL                     1
               STORE_NAME              14 (logger)

  49           LOAD_CONST              33 (('phone', 'email', 'name', 'raw_payload', 'raw_email', 'raw_body', 'transcript', 'summary', 'summary_text', 'secret', 'signature', 'env_value', 'env_values', 'dedupe_key', 'callback_notes', 'rationale_text', 'rationale_freeform', 'prompt_text', 'evidence_raw', 'live_mutation_payload', 'first_name', 'last_name', 'full_name', 'address', 'street'))
               STORE_NAME              15 (FORBIDDEN_EVIDENCE_FIELDS)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               16 (__annotations__)
               LOAD_CONST               6 ('FORBIDDEN_EVIDENCE_FIELDS')
               STORE_SUBSCR

  66           LOAD_CONST              34 (('recommendation_id', 'recommendation_type', 'scenario_type', 'scenario_fingerprint', 'mode', 'rationale_token', 'observation_count', 'warning_count', 'evidence_packet_version'))
               STORE_NAME              17 (ALLOWED_EVIDENCE_KEYS)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               16 (__annotations__)
               LOAD_CONST              11 ('ALLOWED_EVIDENCE_KEYS')
               STORE_SUBSCR

  81           LOAD_CONST              34 (('recommendation_id', 'recommendation_type', 'scenario_type', 'scenario_fingerprint', 'mode', 'rationale_token', 'observation_count', 'warning_count', 'evidence_packet_version'))
               STORE_NAME              18 (OPERATOR_EVIDENCE_KEYS)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               16 (__annotations__)
               LOAD_CONST              12 ('OPERATOR_EVIDENCE_KEYS')
               STORE_SUBSCR

  98           LOAD_CONST              35 (('recommendation_type', 'scenario_type', 'mode', 'observation_count', 'evidence_packet_version'))
               STORE_NAME              19 (TENANT_EVIDENCE_KEYS)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               16 (__annotations__)
               LOAD_CONST              13 ('TENANT_EVIDENCE_KEYS')
               STORE_SUBSCR

 107           LOAD_CONST              14 ('pas181.v1')
               STORE_NAME              20 (_EVIDENCE_PACKET_VERSION)

 109           LOAD_SMALL_INT         200
               STORE_NAME              21 (_VALUE_MAX_LEN)

 112           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA3780, file "app/services/learning/manual_test_evidence.py", line 112>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _is_safe_value at 0x0000018C17FF13B0, file "app/services/learning/manual_test_evidence.py", line 112>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              22 (_is_safe_value)

 120           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA3C30, file "app/services/learning/manual_test_evidence.py", line 120>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object _key_is_forbidden at 0x0000018C18010B30, file "app/services/learning/manual_test_evidence.py", line 120>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              23 (_key_is_forbidden)

 130           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA2B50, file "app/services/learning/manual_test_evidence.py", line 130>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object _scan_forbidden_keys at 0x0000018C18060A50, file "app/services/learning/manual_test_evidence.py", line 130>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              24 (_scan_forbidden_keys)

 141           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA3960, file "app/services/learning/manual_test_evidence.py", line 141>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object _canonical_json at 0x0000018C18090690, file "app/services/learning/manual_test_evidence.py", line 141>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              25 (_canonical_json)

 145           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA3B40, file "app/services/learning/manual_test_evidence.py", line 145>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object evidence_fingerprint at 0x0000018C17ED85A0, file "app/services/learning/manual_test_evidence.py", line 145>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              26 (evidence_fingerprint)

 164           LOAD_CONST               7 ('scenario_fingerprint')

 168           LOAD_CONST               2 (None)

 164           LOAD_CONST               8 ('mode')

 169           LOAD_CONST              25 ('SIMULATION_ONLY')

 164           LOAD_CONST               9 ('observation_count')

 170           LOAD_SMALL_INT           0

 164           LOAD_CONST              10 ('warning_count')

 171           LOAD_SMALL_INT           0

 164           LOAD_CONST              26 ('extra')

 172           LOAD_CONST               2 (None)

 164           BUILD_MAP                5
               LOAD_CONST              27 (<code object __annotate__ at 0x0000018C180907A0, file "app/services/learning/manual_test_evidence.py", line 164>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object build_manual_test_evidence_packet at 0x0000018C181A3080, file "app/services/learning/manual_test_evidence.py", line 164>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              27 (build_manual_test_evidence_packet)

 259           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA21F0, file "app/services/learning/manual_test_evidence.py", line 259>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object evidence_operator_projection at 0x0000018C17ED4B40, file "app/services/learning/manual_test_evidence.py", line 259>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (evidence_operator_projection)

 277           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA2A60, file "app/services/learning/manual_test_evidence.py", line 277>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object evidence_public_projection at 0x0000018C17ED4910, file "app/services/learning/manual_test_evidence.py", line 277>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              29 (evidence_public_projection)

 297           BUILD_LIST               0
               LOAD_CONST              36 (('FORBIDDEN_EVIDENCE_FIELDS', 'ALLOWED_EVIDENCE_KEYS', 'OPERATOR_EVIDENCE_KEYS', 'TENANT_EVIDENCE_KEYS', 'build_manual_test_evidence_packet', 'evidence_fingerprint', 'evidence_operator_projection', 'evidence_public_projection'))
               LIST_EXTEND              1
               STORE_NAME              30 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app/services/learning/manual_test_evidence.py", line 112>:
112           RESUME                   0
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

Disassembly of <code object _is_safe_value at 0x0000018C17FF13B0, file "app/services/learning/manual_test_evidence.py", line 112>:
112           RESUME                   0

113           LOAD_FAST_BORROW         0 (v)
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

114   L1:     LOAD_CONST               1 (True)
              RETURN_VALUE

115   L2:     LOAD_GLOBAL              1 (isinstance + NULL)
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

116           LOAD_CONST               1 (True)
              RETURN_VALUE

117   L3:     LOAD_CONST               2 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app/services/learning/manual_test_evidence.py", line 120>:
120           RESUME                   0
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

Disassembly of <code object _key_is_forbidden at 0x0000018C18010B30, file "app/services/learning/manual_test_evidence.py", line 120>:
120           RESUME                   0

121           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (k)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

122           LOAD_CONST               0 (False)
              RETURN_VALUE

123   L1:     LOAD_FAST_BORROW         0 (k)
              LOAD_ATTR                5 (lower + NULL|self)
              CALL                     0
              STORE_FAST               1 (kl)

124           LOAD_GLOBAL              6 (FORBIDDEN_EVIDENCE_FIELDS)
              GET_ITER
      L2:     FOR_ITER                12 (to L4)
              STORE_FAST               2 (forb)

125           LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (forb, kl)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

126   L3:     POP_TOP
              LOAD_CONST               1 (True)
              RETURN_VALUE

124   L4:     END_FOR
              POP_ITER

127           LOAD_CONST               0 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app/services/learning/manual_test_evidence.py", line 130>:
130           RESUME                   0
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

Disassembly of <code object _scan_forbidden_keys at 0x0000018C18060A50, file "app/services/learning/manual_test_evidence.py", line 130>:
130           RESUME                   0

131           BUILD_LIST               0
              STORE_FAST               1 (bad)

132           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (payload)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

133           LOAD_FAST_BORROW         1 (bad)
              RETURN_VALUE

134   L1:     LOAD_FAST_BORROW         0 (payload)
              LOAD_ATTR                5 (keys + NULL|self)
              CALL                     0
              GET_ITER
      L2:     FOR_ITER                63 (to L5)
              STORE_FAST               2 (k)

135           LOAD_GLOBAL              7 (_key_is_forbidden + NULL)
              LOAD_FAST_BORROW         2 (k)
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           22 (to L2)

136   L3:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (k)
              LOAD_GLOBAL              8 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD           46 (to L2)

137   L4:     LOAD_FAST_BORROW         1 (bad)
              LOAD_ATTR               11 (append + NULL|self)
              LOAD_FAST_BORROW         2 (k)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           65 (to L2)

134   L5:     END_FOR
              POP_ITER

138           LOAD_FAST_BORROW         1 (bad)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app/services/learning/manual_test_evidence.py", line 141>:
141           RESUME                   0
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

Disassembly of <code object _canonical_json at 0x0000018C18090690, file "app/services/learning/manual_test_evidence.py", line 141>:
141           RESUME                   0

142           LOAD_GLOBAL              0 (json)
              LOAD_ATTR                2 (dumps)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (envelope)
              LOAD_CONST               0 (True)
              LOAD_CONST               2 ((',', ':'))
              LOAD_CONST               1 (('sort_keys', 'separators'))
              CALL_KW                  3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app/services/learning/manual_test_evidence.py", line 145>:
145           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('packet')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object evidence_fingerprint at 0x0000018C17ED85A0, file "app/services/learning/manual_test_evidence.py", line 145>:
 145            RESUME                   0

 148            NOP

 149    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (packet)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        37 (to L3)
                NOT_TAKEN

 150            LOAD_GLOBAL              4 (hashlib)
                LOAD_ATTR                6 (sha256)
                PUSH_NULL
                LOAD_CONST               1 (b'')
                CALL                     1
                LOAD_ATTR                9 (hexdigest + NULL|self)
                CALL                     0
        L2:     RETURN_VALUE

 151    L3:     BUILD_MAP                0
                STORE_FAST               1 (projected)

 152            LOAD_GLOBAL             10 (ALLOWED_EVIDENCE_KEYS)
                GET_ITER
        L4:     FOR_ITER                21 (to L7)
                STORE_FAST               2 (k)

 153            LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, packet)
                CONTAINS_OP              0 (in)
        L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L4)

 154    L6:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (packet, k)
                BINARY_OP               26 ([])
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (projected, k)
                STORE_SUBSCR
                JUMP_BACKWARD           23 (to L4)

 152    L7:     END_FOR
                POP_ITER

 155            LOAD_GLOBAL             13 (_canonical_json + NULL)
                LOAD_FAST_BORROW         1 (projected)
                CALL                     1
                STORE_FAST               3 (canonical)

 156            LOAD_GLOBAL              4 (hashlib)
                LOAD_ATTR                6 (sha256)
                PUSH_NULL
                LOAD_FAST_BORROW         3 (canonical)
                LOAD_ATTR               15 (encode + NULL|self)
                LOAD_CONST               2 ('utf-8')
                CALL                     1
                CALL                     1
                LOAD_ATTR                9 (hexdigest + NULL|self)
                CALL                     0
        L8:     RETURN_VALUE

  --    L9:     PUSH_EXC_INFO

 157            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       90 (to L14)
                NOT_TAKEN
                STORE_FAST               4 (e)

 158   L10:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 159            LOAD_CONST               3 ('evidence_fingerprint error type=')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 158            CALL                     1
                POP_TOP

 161            LOAD_GLOBAL              4 (hashlib)
                LOAD_ATTR                6 (sha256)
                PUSH_NULL
                LOAD_CONST               1 (b'')
                CALL                     1
                LOAD_ATTR                9 (hexdigest + NULL|self)
                CALL                     0
       L11:     SWAP                     2
       L12:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RETURN_VALUE

  --   L13:     LOAD_CONST               4 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 157   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L9 [0]
  L3 to L5 -> L9 [0]
  L6 to L8 -> L9 [0]
  L9 to L10 -> L15 [1] lasti
  L10 to L11 -> L13 [1] lasti
  L11 to L12 -> L15 [1] lasti
  L13 to L15 -> L15 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C180907A0, file "app/services/learning/manual_test_evidence.py", line 164>:
164           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendation')

166           LOAD_CONST               2 ('Any')

164           LOAD_CONST               3 ('scenario_type')

167           LOAD_CONST               4 ('str')

164           LOAD_CONST               5 ('scenario_fingerprint')

168           LOAD_CONST               6 ('Optional[str]')

164           LOAD_CONST               7 ('mode')

169           LOAD_CONST               4 ('str')

164           LOAD_CONST               8 ('observation_count')

170           LOAD_CONST               2 ('Any')

164           LOAD_CONST               9 ('warning_count')

171           LOAD_CONST               2 ('Any')

164           LOAD_CONST              10 ('extra')

172           LOAD_CONST              11 ('Optional[Dict[str, Any]]')

164           LOAD_CONST              12 ('return')

173           LOAD_CONST              13 ('Dict[str, Any]')

164           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object build_manual_test_evidence_packet at 0x0000018C181A3080, file "app/services/learning/manual_test_evidence.py", line 164>:
 164            RESUME                   0

 181            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (recommendation)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        13 (to L1)
                NOT_TAKEN

 183            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 184            LOAD_CONST               3 ('packet')
                LOAD_CONST               4 (None)

 185            LOAD_CONST               5 ('fingerprint')
                LOAD_CONST               4 (None)

 186            LOAD_CONST               6 ('warnings')
                BUILD_LIST               0

 187            LOAD_CONST               7 ('error_code')
                LOAD_CONST               8 ('invalid_recommendation')

 182            BUILD_MAP                5
                RETURN_VALUE

 189    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (scenario_type)
                LOAD_GLOBAL              4 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (scenario_type)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        13 (to L3)
                NOT_TAKEN

 191    L2:     LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 192            LOAD_CONST               3 ('packet')
                LOAD_CONST               4 (None)

 193            LOAD_CONST               5 ('fingerprint')
                LOAD_CONST               4 (None)

 194            LOAD_CONST               6 ('warnings')
                BUILD_LIST               0

 195            LOAD_CONST               7 ('error_code')
                LOAD_CONST               9 ('invalid_scenario_type')

 190            BUILD_MAP                5
                RETURN_VALUE

 197    L3:     LOAD_FAST_BORROW         3 (mode)
                LOAD_CONST              27 (('SIMULATION_ONLY', 'OBSERVATIONAL_ONLY'))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       13 (to L4)
                NOT_TAKEN

 199            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 200            LOAD_CONST               3 ('packet')
                LOAD_CONST               4 (None)

 201            LOAD_CONST               5 ('fingerprint')
                LOAD_CONST               4 (None)

 202            LOAD_CONST               6 ('warnings')
                BUILD_LIST               0

 203            LOAD_CONST               7 ('error_code')
                LOAD_CONST              10 ('invalid_mode')

 198            BUILD_MAP                5
                RETURN_VALUE

 205    L4:     LOAD_GLOBAL              9 (_scan_forbidden_keys + NULL)
                LOAD_FAST_BORROW         6 (extra)
                CALL                     1
                STORE_FAST               7 (bad)

 206            LOAD_FAST_BORROW         7 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L9)
                NOT_TAKEN

 208            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 209            LOAD_CONST               3 ('packet')
                LOAD_CONST               4 (None)

 210            LOAD_CONST               5 ('fingerprint')
                LOAD_CONST               4 (None)

 211            LOAD_CONST               6 ('warnings')
                LOAD_FAST_BORROW         7 (bad)
                LOAD_CONST              11 (slice(None, 5, None))
                BINARY_OP               26 ([])
                GET_ITER
                LOAD_FAST_AND_CLEAR      8 (k)
                SWAP                     2
        L5:     BUILD_LIST               0
                SWAP                     2
        L6:     FOR_ITER                 8 (to L7)
                STORE_FAST               8 (k)
                LOAD_CONST              12 ('forbidden_field:')
                LOAD_FAST_BORROW         8 (k)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LIST_APPEND              2
                JUMP_BACKWARD           10 (to L6)
        L7:     END_FOR
                POP_ITER
        L8:     SWAP                     2
                STORE_FAST               8 (k)

 212            LOAD_CONST               7 ('error_code')
                LOAD_CONST              13 ('forbidden_evidence_field')

 207            BUILD_MAP                5
                RETURN_VALUE

 214    L9:     NOP

 215   L10:     LOAD_GLOBAL             11 (int + NULL)
                LOAD_FAST_BORROW         4 (observation_count)
                CALL                     1
                STORE_FAST               9 (obs)

 216            LOAD_FAST_BORROW         9 (obs)
                LOAD_SMALL_INT           0
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN

 217            LOAD_SMALL_INT           0
                STORE_FAST               9 (obs)

 220   L11:     NOP

 221   L12:     LOAD_GLOBAL             11 (int + NULL)
                LOAD_FAST                5 (warning_count)
                CALL                     1
                STORE_FAST              10 (wc)

 222            LOAD_FAST               10 (wc)
                LOAD_SMALL_INT           0
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN

 223            LOAD_SMALL_INT           0
                STORE_FAST              10 (wc)

 228   L13:     LOAD_CONST              14 ('recommendation_id')
                LOAD_FAST                0 (recommendation)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              14 ('recommendation_id')
                CALL                     1

 229            LOAD_CONST              15 ('recommendation_type')
                LOAD_FAST                0 (recommendation)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              15 ('recommendation_type')
                CALL                     1

 230            LOAD_CONST              16 ('scenario_type')
                LOAD_FAST                1 (scenario_type)

 231            LOAD_CONST              17 ('scenario_fingerprint')

 232            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST                2 (scenario_fingerprint)
                LOAD_GLOBAL              4 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       77 (to L19)
                NOT_TAKEN

 233            LOAD_GLOBAL             19 (len + NULL)
                LOAD_FAST                2 (scenario_fingerprint)
                CALL                     1
                LOAD_SMALL_INT          64
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       61 (to L19)
                NOT_TAKEN

 234            LOAD_GLOBAL             20 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       28 (to L17)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              18 (<code object <genexpr> at 0x0000018C18024930, file "app/services/learning/manual_test_evidence.py", line 234>)
                MAKE_FUNCTION
                LOAD_FAST                2 (scenario_fingerprint)
                GET_ITER
                CALL                     0
       L14:     FOR_ITER                12 (to L16)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L14)
       L15:     POP_ITER
                LOAD_CONST              19 (False)
                JUMP_FORWARD            17 (to L18)
       L16:     END_FOR
                POP_ITER
                LOAD_CONST              20 (True)
                JUMP_FORWARD            13 (to L18)
       L17:     PUSH_NULL
                LOAD_CONST              18 (<code object <genexpr> at 0x0000018C18024930, file "app/services/learning/manual_test_evidence.py", line 234>)
                MAKE_FUNCTION
                LOAD_FAST                2 (scenario_fingerprint)
                GET_ITER
                CALL                     0
                CALL                     1
       L18:     TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L19)
                NOT_TAKEN

 232            LOAD_FAST                2 (scenario_fingerprint)
                JUMP_FORWARD             1 (to L20)

 235   L19:     LOAD_CONST               4 (None)

 237   L20:     LOAD_CONST              21 ('mode')
                LOAD_FAST                3 (mode)

 238            LOAD_CONST              22 ('rationale_token')
                LOAD_FAST                0 (recommendation)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              22 ('rationale_token')
                CALL                     1

 239            LOAD_CONST              23 ('observation_count')
                LOAD_FAST                9 (obs)

 240            LOAD_CONST              24 ('warning_count')
                LOAD_FAST               10 (wc)

 241            LOAD_CONST              25 ('evidence_packet_version')
                LOAD_GLOBAL             22 (_EVIDENCE_PACKET_VERSION)

 227            BUILD_MAP                9
                STORE_FAST              11 (packet)

 244            BUILD_MAP                0
                STORE_FAST              12 (bounded)

 245            LOAD_GLOBAL             24 (ALLOWED_EVIDENCE_KEYS)
                GET_ITER
       L21:     FOR_ITER                46 (to L24)
                STORE_FAST               8 (k)

 246            LOAD_FAST_LOAD_FAST    139 (k, packet)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         3 (to L22)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L21)
       L22:     LOAD_GLOBAL             27 (_is_safe_value + NULL)
                LOAD_FAST_LOAD_FAST    184 (packet, k)
                BINARY_OP               26 ([])
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L23)
                NOT_TAKEN
                JUMP_BACKWARD           36 (to L21)

 247   L23:     LOAD_FAST_LOAD_FAST    184 (packet, k)
                BINARY_OP               26 ([])
                LOAD_FAST_LOAD_FAST    200 (bounded, k)
                STORE_SUBSCR
                JUMP_BACKWARD           48 (to L21)

 245   L24:     END_FOR
                POP_ITER

 249            LOAD_GLOBAL             29 (evidence_fingerprint + NULL)
                LOAD_FAST               12 (bounded)
                CALL                     1
                STORE_FAST              13 (fp)

 251            LOAD_CONST               1 ('status')
                LOAD_CONST              26 ('ok')

 252            LOAD_CONST               3 ('packet')
                LOAD_FAST               12 (bounded)

 253            LOAD_CONST               5 ('fingerprint')
                LOAD_FAST               13 (fp)

 254            LOAD_CONST               6 ('warnings')
                BUILD_LIST               0

 255            LOAD_CONST               7 ('error_code')
                LOAD_CONST               4 (None)

 250            BUILD_MAP                5
                RETURN_VALUE

  --   L25:     SWAP                     2
                POP_TOP

 211            SWAP                     2
                STORE_FAST               8 (k)
                RERAISE                  0

  --   L26:     PUSH_EXC_INFO

 218            LOAD_GLOBAL             12 (TypeError)
                LOAD_GLOBAL             14 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        7 (to L28)
                NOT_TAKEN
                POP_TOP

 219            LOAD_SMALL_INT           0
                STORE_FAST               9 (obs)
       L27:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 296 (to L11)

 218   L28:     RERAISE                  0

  --   L29:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L30:     PUSH_EXC_INFO

 224            LOAD_GLOBAL             12 (TypeError)
                LOAD_GLOBAL             14 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        7 (to L32)
                NOT_TAKEN
                POP_TOP

 225            LOAD_SMALL_INT           0
                STORE_FAST              10 (wc)
       L31:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 301 (to L13)

 224   L32:     RERAISE                  0

  --   L33:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L8 -> L25 [9]
  L10 to L11 -> L26 [0]
  L12 to L13 -> L30 [0]
  L26 to L27 -> L29 [1] lasti
  L28 to L29 -> L29 [1] lasti
  L30 to L31 -> L33 [1] lasti
  L32 to L33 -> L33 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C18024930, file "app/services/learning/manual_test_evidence.py", line 234>:
 234           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (c, c)
               LOAD_CONST               0 ('0123456789abcdef')
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           11 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app/services/learning/manual_test_evidence.py", line 259>:
259           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('packet')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object evidence_operator_projection at 0x0000018C17ED4B40, file "app/services/learning/manual_test_evidence.py", line 259>:
 259            RESUME                   0

 261            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (packet)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 262            BUILD_MAP                0
                RETURN_VALUE

 263    L1:     BUILD_MAP                0
                STORE_FAST               1 (out)

 264            NOP

 265    L2:     LOAD_GLOBAL              4 (OPERATOR_EVIDENCE_KEYS)
                GET_ITER
        L3:     FOR_ITER                61 (to L10)
                STORE_FAST               2 (k)

 266            LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, packet)
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

 267    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (packet, k)
                BINARY_OP               26 ([])
                STORE_FAST               3 (v)

 268            LOAD_GLOBAL              9 (_is_safe_value + NULL)
                LOAD_FAST_BORROW         3 (v)
                CALL                     1
                TO_BOOL
        L8:     POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           57 (to L3)

 269    L9:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
                LOAD_FAST_BORROW         2 (k)
                STORE_SUBSCR
                JUMP_BACKWARD           63 (to L3)

 265   L10:     END_FOR
                POP_ITER

 274   L11:     LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 270            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L16)
                NOT_TAKEN
                STORE_FAST               4 (e)

 271   L13:     LOAD_GLOBAL             12 (logger)
                LOAD_ATTR               15 (warning + NULL|self)

 272            LOAD_CONST               1 ('evidence_operator_projection error type=')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 271            CALL                     1
                POP_TOP
       L14:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)

 274            LOAD_FAST                1 (out)
                RETURN_VALUE

  --   L15:     LOAD_CONST               2 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 270   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L4 -> L12 [0]
  L5 to L6 -> L12 [0]
  L7 to L8 -> L12 [0]
  L9 to L11 -> L12 [0]
  L12 to L13 -> L17 [1] lasti
  L13 to L14 -> L15 [1] lasti
  L15 to L17 -> L17 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app/services/learning/manual_test_evidence.py", line 277>:
277           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('packet')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object evidence_public_projection at 0x0000018C17ED4910, file "app/services/learning/manual_test_evidence.py", line 277>:
 277            RESUME                   0

 281            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (packet)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 282            BUILD_MAP                0
                RETURN_VALUE

 283    L1:     BUILD_MAP                0
                STORE_FAST               1 (out)

 284            NOP

 285    L2:     LOAD_GLOBAL              4 (TENANT_EVIDENCE_KEYS)
                GET_ITER
        L3:     FOR_ITER                61 (to L10)
                STORE_FAST               2 (k)

 286            LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, packet)
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

 287    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (packet, k)
                BINARY_OP               26 ([])
                STORE_FAST               3 (v)

 288            LOAD_GLOBAL              9 (_is_safe_value + NULL)
                LOAD_FAST_BORROW         3 (v)
                CALL                     1
                TO_BOOL
        L8:     POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           57 (to L3)

 289    L9:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
                LOAD_FAST_BORROW         2 (k)
                STORE_SUBSCR
                JUMP_BACKWARD           63 (to L3)

 285   L10:     END_FOR
                POP_ITER

 294   L11:     LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 290            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L16)
                NOT_TAKEN
                STORE_FAST               4 (e)

 291   L13:     LOAD_GLOBAL             12 (logger)
                LOAD_ATTR               15 (warning + NULL|self)

 292            LOAD_CONST               1 ('evidence_public_projection error type=')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 291            CALL                     1
                POP_TOP
       L14:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)

 294            LOAD_FAST                1 (out)
                RETURN_VALUE

  --   L15:     LOAD_CONST               2 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 290   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L4 -> L12 [0]
  L5 to L6 -> L12 [0]
  L7 to L8 -> L12 [0]
  L9 to L11 -> L12 [0]
  L12 to L13 -> L17 [1] lasti
  L13 to L14 -> L15 [1] lasti
  L15 to L17 -> L17 [1] lasti
```
