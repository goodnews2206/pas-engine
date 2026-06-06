# operator/audit_integrity

- **pyc:** `app\services\operator\__pycache__\audit_integrity.cpython-314.pyc`
- **expected source path (absent):** `app\services\operator/audit_integrity.py`
- **co_filename (from bytecode):** `app\services\operator\audit_integrity.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** operator

## Module docstring

```
PAS175 — Operator audit log integrity service.

Forward-secure hash-chain over the PAS174 ``pas_operator_
actions_log`` table. Deterministic. NEVER hashes PII or
secrets.

Doctrine:

* **Read-only.** This module never writes, updates, or deletes
  audit rows. It computes hashes deterministically and verifies
  the chain.
* **Deterministic.** Same input → same hash, byte-for-byte.
  The canonical-row builder explicitly lists the fields
  contributing to the hash so a schema change cannot silently
  alter the chain.
* **No PII / no secrets in the hash input.** The canonical-row
  shape carries only `action_id / occurred_at / brokerage_id /
  actor_type / actor_id / action / target_type / target_id /
  status / warning_count` plus the metadata's allow-listed
  keys. No raw payload, no env value, no transcript.
* **Genesis sentinel.** The first row's ``prev_hash`` is the
  literal string ``"GENESIS"`` (also accepted as a SHA-256
  shape-exempt value by the v23 CHECK constraint).
* **NEVER raises.** DB unavailable → ``status="skipped"``
  envelope.

Public surface:

  * ``GENESIS_HASH``
  * ``compute_row_hash(prev_hash, row)`` — deterministic hash.
  * ``compute_chain_head(brokerage_id=None)`` — latest row's
    ``row_hash`` (operator-callable read).
  * ``verify_audit_chain(brokerage_id=None, limit=...)`` —
    walk the chain, report break(s).
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `datetime`, `get_supabase`, `hashlib`, `json`, `logging`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_bound_brokerage_id`, `_canonicalise_row`, `_clamp_limit`, `_get_db_safe`, `_project_metadata`, `_safe_envelope`, `compute_chain_head`, `compute_row_hash`, `verify_audit_chain`

## Env-key candidates

`GENESIS`

## String constants (redacted where noted)

- '\nPAS175 — Operator audit log integrity service.\n\nForward-secure hash-chain over the PAS174 ``pas_operator_\nactions_log`` table. Deterministic. NEVER hashes PII or\nsecrets.\n\nDoctrine:\n\n* **Read-only.** This module never writes, updates, or deletes\n  audit rows. It computes hashes deterministically and verifies\n  the chain.\n* **Deterministic.** Same input → same hash, byte-for-byte.\n  The canonical-row builder explicitly lists the fields\n  contributing to the hash so a schema change cannot silently\n  alter the chain.\n* **No PII / no secrets in the hash input.** The canonical-row\n  shape carries only `action_id / occurred_at / brokerage_id /\n  actor_type / actor_id / action / target_type / target_id /\n  status / warning_count` plus the metadata\'s allow-listed\n  keys. No raw payload, no env value, no transcript.\n* **Genesis sentinel.** The first row\'s ``prev_hash`` is the\n  literal string ``"GENESIS"`` (also accepted as a SHA-256\n  shape-exempt value by the v23 CHECK constraint).\n* **NEVER raises.** DB unavailable → ``status="skipped"``\n  envelope.\n\nPublic surface:\n\n  * ``GENESIS_HASH``\n  * ``compute_row_hash(prev_hash, row)`` — deterministic hash.\n  * ``compute_chain_head(brokerage_id=None)`` — latest row\'s\n    ``row_hash`` (operator-callable read).\n  * ``verify_audit_chain(brokerage_id=None, limit=...)`` —\n    walk the chain, report break(s).\n'
- 'pas.operator.audit_integrity'
- 'pas_operator_actions_log'
- 'GENESIS'
- 'brokerage_id'
- 'error_code'
- 'chain_status'
- 'limit'
- 'rows_checked'
- 'breaks'
- 'head'
- 'warnings'
- 'metadata'
- 'Any'
- 'return'
- 'Dict[str, Any]'
- 'row'
- 'Project a row dict into the canonical hash input shape.\nNEVER includes fields outside ``_HASH_FIELDS``. NEVER\nincludes metadata keys outside the allow-list.'
- 'prev_hash'
- 'str'
- "Deterministically compute the row_hash from the previous\nrow's hash + the canonical row payload. NEVER raises."
- 'utf-8'
- 'compute_row_hash unexpected error type='
- 'audit_integrity db client unavailable type='
- 'value'
- 'int'
- 'Optional[str]'
- 'status'
- 'Optional[List[Dict[str, Any]]]'
- 'Optional[List[str]]'
- 'Return the most-recent ``row_hash`` for the chain\n(optionally scoped to a brokerage). Returns the literal\n``GENESIS_HASH`` when the chain is empty. NEVER raises.'
- 'skipped'
- 'audit_store_unavailable'
- 'row_hash, occurred_at'
- 'occurred_at'
- 'data'
- 'genesis'
- 'row_hash'
- 'degraded'
- 'chain_head_missing_hash'
- 'compute_chain_head read error type='
- 'db_read_failed:'
- 'Walk the audit log in ``occurred_at ASC`` order,\nrecompute the chain, and return a structural envelope\ndescribing any break(s). NEVER raises.\n\nStatus semantics:\n\n* ``status="ok", chain_status="ok"`` — chain intact end-to-end.\n* ``status="ok", chain_status="genesis"`` — chain empty.\n* ``status="ok", chain_status="degraded"`` — chain has at\n  least one break (rows with missing or mismatched hashes).\n* ``status="skipped"`` — DB unavailable / table missing.\n\nNEVER returns raw payload contents — break entries carry\nonly structural identifiers (``action_id``, ``occurred_at``)\nand the type of break.\n'
- 'action_id, occurred_at, brokerage_id, actor_type, actor_id, action, target_type, target_id, status, warning_count, metadata, prev_hash, row_hash'
- 'verify_audit_chain db error type='
- 'action_id'
- 'break_type'
- 'missing_prev_hash'
- 'expected_prev_hash_present'
- 'prev_hash_mismatch'
- 'missing_row_hash'
- 'expected_row_hash_present'
- 'row_hash_mismatch'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS175 — Operator audit log integrity service.\n\nForward-secure hash-chain over the PAS174 ``pas_operator_\nactions_log`` table. Deterministic. NEVER hashes PII or\nsecrets.\n\nDoctrine:\n\n* **Read-only.** This module never writes, updates, or deletes\n  audit rows. It computes hashes deterministically and verifies\n  the chain.\n* **Deterministic.** Same input → same hash, byte-for-byte.\n  The canonical-row builder explicitly lists the fields\n  contributing to the hash so a schema change cannot silently\n  alter the chain.\n* **No PII / no secrets in the hash input.** The canonical-row\n  shape carries only `action_id / occurred_at / brokerage_id /\n  actor_type / actor_id / action / target_type / target_id /\n  status / warning_count` plus the metadata\'s allow-listed\n  keys. No raw payload, no env value, no transcript.\n* **Genesis sentinel.** The first row\'s ``prev_hash`` is the\n  literal string ``"GENESIS"`` (also accepted as a SHA-256\n  shape-exempt value by the v23 CHECK constraint).\n* **NEVER raises.** DB unavailable → ``status="skipped"``\n  envelope.\n\nPublic surface:\n\n  * ``GENESIS_HASH``\n  * ``compute_row_hash(prev_hash, row)`` — deterministic hash.\n  * ``compute_chain_head(brokerage_id=None)`` — latest row\'s\n    ``row_hash`` (operator-callable read).\n  * ``verify_audit_chain(brokerage_id=None, limit=...)`` —\n    walk the chain, report break(s).\n')
              STORE_NAME               0 (__doc__)

 38           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 40           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (hashlib)
              STORE_NAME               3 (hashlib)

 41           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (json)
              STORE_NAME               4 (json)

 42           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              5 (logging)
              STORE_NAME               5 (logging)

 43           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timezone'))
              IMPORT_NAME              6 (datetime)
              IMPORT_FROM              6 (datetime)
              STORE_NAME               6 (datetime)
              IMPORT_FROM              7 (timezone)
              STORE_NAME               7 (timezone)
              POP_TOP

 44           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              8 (typing)
              IMPORT_FROM              9 (Any)
              STORE_NAME               9 (Any)
              IMPORT_FROM             10 (Dict)
              STORE_NAME              10 (Dict)
              IMPORT_FROM             11 (List)
              STORE_NAME              11 (List)
              IMPORT_FROM             12 (Optional)
              STORE_NAME              12 (Optional)
              POP_TOP

 47           LOAD_NAME                5 (logging)
              LOAD_ATTR               26 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.operator.audit_integrity')
              CALL                     1
              STORE_NAME              14 (logger)

 50           LOAD_CONST               6 ('pas_operator_actions_log')
              STORE_NAME              15 (_TABLE)

 52           LOAD_CONST               7 ('GENESIS')
              STORE_NAME              16 (GENESIS_HASH)

 55           LOAD_CONST               8 (5000)
              STORE_NAME              17 (_LIST_HARD_CAP)

 56           LOAD_CONST               9 (500)
              STORE_NAME              18 (_DEFAULT_LIMIT)

 64           LOAD_CONST              35 (('action_id', 'occurred_at', 'brokerage_id', 'actor_type', 'actor_id', 'action', 'target_type', 'target_id', 'status', 'warning_count', 'metadata'))
              STORE_NAME              19 (_HASH_FIELDS)

 80           LOAD_CONST              36 (('event', 'warning_count', 'error_count', 'error_code', 'stage', 'target_status', 'launch_ready', 'probe_type', 'subsystem', 'onboarding_status', 'pilot_stage', 'evidence_audit_row_id', 'request_id', 'rotation_proposal_only'))
              STORE_NAME              20 (_METADATA_ALLOW_LIST)

103           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\operator\audit_integrity.py", line 103>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _project_metadata at 0x0000018C17FEDC30, file "app\services\operator\audit_integrity.py", line 103>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (_project_metadata)

119           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA2C40, file "app\services\operator\audit_integrity.py", line 119>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _canonicalise_row at 0x0000018C17D77E00, file "app\services\operator\audit_integrity.py", line 119>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (_canonicalise_row)

140           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18025130, file "app\services\operator\audit_integrity.py", line 140>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object compute_row_hash at 0x0000018C17ED2E80, file "app\services\operator\audit_integrity.py", line 140>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              23 (compute_row_hash)

166           LOAD_CONST              18 (<code object _get_db_safe at 0x0000018C17FF1230, file "app\services\operator\audit_integrity.py", line 166>)
              MAKE_FUNCTION
              STORE_NAME              24 (_get_db_safe)

178           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA3960, file "app\services\operator\audit_integrity.py", line 178>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _clamp_limit at 0x0000018C18011210, file "app\services\operator\audit_integrity.py", line 178>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_clamp_limit)

190           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA3870, file "app\services\operator\audit_integrity.py", line 190>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _bound_brokerage_id at 0x0000018C18011370, file "app\services\operator\audit_integrity.py", line 190>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_bound_brokerage_id)

199           LOAD_CONST              23 ('chain_status')

202           LOAD_CONST               2 (None)

199           LOAD_CONST              10 ('brokerage_id')

203           LOAD_CONST               2 (None)

199           LOAD_CONST              24 ('limit')

204           LOAD_NAME               18 (_DEFAULT_LIMIT)

199           LOAD_CONST              25 ('rows_checked')

205           LOAD_SMALL_INT           0

199           LOAD_CONST              26 ('breaks')

206           LOAD_CONST               2 (None)

199           LOAD_CONST              27 ('head')

207           LOAD_CONST               2 (None)

199           LOAD_CONST              28 ('warnings')

208           LOAD_CONST               2 (None)

199           LOAD_CONST              11 ('error_code')

209           LOAD_CONST               2 (None)

199           BUILD_MAP                8
              LOAD_CONST              29 (<code object __annotate__ at 0x0000018C180C4470, file "app\services\operator\audit_integrity.py", line 199>)
              MAKE_FUNCTION
              LOAD_CONST              30 (<code object _safe_envelope at 0x0000018C17FE1290, file "app\services\operator\audit_integrity.py", line 199>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              27 (_safe_envelope)

228           LOAD_CONST              10 ('brokerage_id')

230           LOAD_CONST               2 (None)

228           BUILD_MAP                1
              LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\operator\audit_integrity.py", line 228>)
              MAKE_FUNCTION
              LOAD_CONST              32 (<code object compute_chain_head at 0x0000018C181FC460, file "app\services\operator\audit_integrity.py", line 228>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              28 (compute_chain_head)

293           LOAD_CONST              10 ('brokerage_id')

295           LOAD_CONST               2 (None)

293           LOAD_CONST              24 ('limit')

296           LOAD_NAME               18 (_DEFAULT_LIMIT)

293           BUILD_MAP                2
              LOAD_CONST              33 (<code object __annotate__ at 0x0000018C18025A30, file "app\services\operator\audit_integrity.py", line 293>)
              MAKE_FUNCTION
              LOAD_CONST              34 (<code object verify_audit_chain at 0x0000018C181A2DB0, file "app\services\operator\audit_integrity.py", line 293>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              29 (verify_audit_chain)

424           BUILD_LIST               0
              LOAD_CONST              37 (('GENESIS_HASH', 'compute_row_hash', 'compute_chain_head', 'verify_audit_chain'))
              LIST_EXTEND              1
              STORE_NAME              30 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\operator\audit_integrity.py", line 103>:
103           RESUME                   0
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

Disassembly of <code object _project_metadata at 0x0000018C17FEDC30, file "app\services\operator\audit_integrity.py", line 103>:
103           RESUME                   0

104           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (metadata)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

105           BUILD_MAP                0
              RETURN_VALUE

106   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

107           LOAD_GLOBAL              4 (_METADATA_ALLOW_LIST)
              GET_ITER
      L2:     FOR_ITER               108 (to L8)
              STORE_FAST               2 (k)

108           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, metadata)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

109           JUMP_BACKWARD           11 (to L2)

110   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (metadata, k)
              BINARY_OP               26 ([])
              STORE_FAST               3 (v)

111           LOAD_FAST_BORROW         3 (v)
              POP_JUMP_IF_NONE        34 (to L4)
              NOT_TAKEN
              LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (v)
              LOAD_GLOBAL              6 (int)
              LOAD_GLOBAL              8 (float)
              LOAD_GLOBAL             10 (bool)
              BUILD_TUPLE              3
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        7 (to L5)
              NOT_TAKEN

112   L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD           62 (to L2)

113   L5:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (v)
              LOAD_GLOBAL             12 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              JUMP_BACKWARD           86 (to L2)

114   L6:     LOAD_GLOBAL             15 (len + NULL)
              LOAD_FAST_BORROW         3 (v)
              CALL                     1
              LOAD_SMALL_INT         200
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_TRUE         3 (to L7)
              NOT_TAKEN
              JUMP_BACKWARD          104 (to L2)

115   L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD          110 (to L2)

107   L8:     END_FOR
              POP_ITER

116           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app\services\operator\audit_integrity.py", line 119>:
119           RESUME                   0
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

Disassembly of <code object _canonicalise_row at 0x0000018C17D77E00, file "app\services\operator\audit_integrity.py", line 119>:
119           RESUME                   0

123           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

124           BUILD_MAP                0
              RETURN_VALUE

125   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

126           LOAD_GLOBAL              4 (_HASH_FIELDS)
              GET_ITER
      L2:     FOR_ITER               134 (to L7)
              STORE_FAST               2 (k)

127           LOAD_FAST_BORROW         2 (k)
              LOAD_CONST               1 ('metadata')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       41 (to L4)
              NOT_TAKEN

128           LOAD_GLOBAL              7 (_project_metadata + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               1 ('metadata')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L3:     CALL                     1
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, k)
              STORE_SUBSCR
              JUMP_BACKWARD           50 (to L2)

130   L4:     LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_FAST_BORROW         2 (k)
              CALL                     1
              STORE_FAST               3 (v)

131           LOAD_FAST_BORROW         3 (v)
              POP_JUMP_IF_NOT_NONE     7 (to L5)
              NOT_TAKEN

132           LOAD_CONST               2 (None)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, k)
              STORE_SUBSCR
              JUMP_BACKWARD           77 (to L2)

133   L5:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (v)
              LOAD_GLOBAL             10 (int)
              LOAD_GLOBAL             12 (float)
              LOAD_GLOBAL             14 (bool)
              LOAD_GLOBAL             16 (str)
              BUILD_TUPLE              4
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        7 (to L6)
              NOT_TAKEN

134           LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD          121 (to L2)

136   L6:     LOAD_GLOBAL             17 (str + NULL)
              LOAD_FAST_BORROW         3 (v)
              CALL                     1
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, k)
              STORE_SUBSCR
              JUMP_BACKWARD          136 (to L2)

126   L7:     END_FOR
              POP_ITER

137           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "app\services\operator\audit_integrity.py", line 140>:
140           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('prev_hash')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('row')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('str')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object compute_row_hash at 0x0000018C17ED2E80, file "app\services\operator\audit_integrity.py", line 140>:
 140            RESUME                   0

 145            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (prev_hash)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (prev_hash)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L1)
                NOT_TAKEN

 144            LOAD_FAST_BORROW         0 (prev_hash)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             5 (to L2)

 146    L1:     LOAD_GLOBAL              6 (GENESIS_HASH)

 143    L2:     STORE_FAST               2 (ph)

 148            LOAD_GLOBAL              9 (_canonicalise_row + NULL)
                LOAD_FAST_BORROW         1 (row)
                CALL                     1
                STORE_FAST               3 (canonical)

 149            LOAD_GLOBAL             10 (json)
                LOAD_ATTR               12 (dumps)
                PUSH_NULL

 150            LOAD_CONST               1 ('prev_hash')
                LOAD_FAST_BORROW         2 (ph)
                LOAD_CONST               2 ('row')
                LOAD_FAST_BORROW         3 (canonical)
                BUILD_MAP                2

 151            LOAD_CONST               3 (True)
                LOAD_CONST               9 ((',', ':'))
                LOAD_GLOBAL              2 (str)

 149            LOAD_CONST               4 (('sort_keys', 'separators', 'default'))
                CALL_KW                  4
                STORE_FAST               4 (payload)

 153            NOP

 154    L3:     LOAD_GLOBAL             14 (hashlib)
                LOAD_ATTR               16 (sha256)
                PUSH_NULL
                LOAD_FAST_BORROW         4 (payload)
                LOAD_ATTR               19 (encode + NULL|self)
                LOAD_CONST               5 ('utf-8')
                CALL                     1
                CALL                     1
                LOAD_ATTR               21 (hexdigest + NULL|self)
                CALL                     0
        L4:     RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 155            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       90 (to L10)
                NOT_TAKEN
                STORE_FAST               5 (e)

 156    L6:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 157            LOAD_CONST               6 ('compute_row_hash unexpected error type=')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 156            CALL                     1
                POP_TOP

 159            LOAD_GLOBAL             14 (hashlib)
                LOAD_ATTR               16 (sha256)
                PUSH_NULL
                LOAD_CONST               7 (b'')
                CALL                     1
                LOAD_ATTR               21 (hexdigest + NULL|self)
                CALL                     0
        L7:     SWAP                     2
        L8:     POP_EXCEPT
                LOAD_CONST               8 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RETURN_VALUE

  --    L9:     LOAD_CONST               8 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 155   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L5 [0]
  L5 to L6 -> L11 [1] lasti
  L6 to L7 -> L9 [1] lasti
  L7 to L8 -> L11 [1] lasti
  L9 to L11 -> L11 [1] lasti

Disassembly of <code object _get_db_safe at 0x0000018C17FF1230, file "app\services\operator\audit_integrity.py", line 166>:
 166           RESUME                   0

 167           NOP

 168   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 169           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 170           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 171   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 172           LOAD_CONST               2 ('audit_integrity db client unavailable type=')

 173           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 172           BUILD_STRING             2

 171           CALL                     1
               POP_TOP

 175   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 170   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app\services\operator\audit_integrity.py", line 178>:
178           RESUME                   0
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
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _clamp_limit at 0x0000018C18011210, file "app\services\operator\audit_integrity.py", line 178>:
 178           RESUME                   0

 179           NOP

 180   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (v)

 183   L2:     LOAD_FAST                1 (v)
               LOAD_SMALL_INT           1
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 184           LOAD_SMALL_INT           1
               RETURN_VALUE

 185   L3:     LOAD_FAST                1 (v)
               LOAD_GLOBAL              8 (_LIST_HARD_CAP)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 186           LOAD_GLOBAL              8 (_LIST_HARD_CAP)
               RETURN_VALUE

 187   L4:     LOAD_FAST                1 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 181           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

 182           LOAD_GLOBAL              6 (_DEFAULT_LIMIT)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 181   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\services\operator\audit_integrity.py", line 190>:
190           RESUME                   0
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

Disassembly of <code object _bound_brokerage_id at 0x0000018C18011370, file "app\services\operator\audit_integrity.py", line 190>:
190           RESUME                   0

191           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

192           LOAD_CONST               0 (None)
              RETURN_VALUE

193   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

194           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_SMALL_INT         200
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

195   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

196   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180C4470, file "app\services\operator\audit_integrity.py", line 199>:
199           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

201           LOAD_CONST               2 ('str')

199           LOAD_CONST               3 ('chain_status')

202           LOAD_CONST               4 ('Optional[str]')

199           LOAD_CONST               5 ('brokerage_id')

203           LOAD_CONST               4 ('Optional[str]')

199           LOAD_CONST               6 ('limit')

204           LOAD_CONST               7 ('int')

199           LOAD_CONST               8 ('rows_checked')

205           LOAD_CONST               7 ('int')

199           LOAD_CONST               9 ('breaks')

206           LOAD_CONST              10 ('Optional[List[Dict[str, Any]]]')

199           LOAD_CONST              11 ('head')

207           LOAD_CONST               4 ('Optional[str]')

199           LOAD_CONST              12 ('warnings')

208           LOAD_CONST              13 ('Optional[List[str]]')

199           LOAD_CONST              14 ('error_code')

209           LOAD_CONST               4 ('Optional[str]')

199           LOAD_CONST              15 ('return')

210           LOAD_CONST              16 ('Dict[str, Any]')

199           BUILD_MAP               10
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C17FE1290, file "app\services\operator\audit_integrity.py", line 199>:
199           RESUME                   0

212           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

213           LOAD_CONST               1 ('chain_status')
              LOAD_FAST                1 (chain_status)

214           LOAD_CONST               2 ('brokerage_id')
              LOAD_FAST                2 (brokerage_id)

215           LOAD_CONST               3 ('limit')
              LOAD_FAST                3 (limit)

216           LOAD_CONST               4 ('rows_checked')
              LOAD_FAST                4 (rows_checked)

217           LOAD_CONST               5 ('breaks')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                5 (breaks)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

218           LOAD_CONST               6 ('head')
              LOAD_FAST                6 (head)

219           LOAD_CONST               7 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                7 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L2:     CALL                     1

220           LOAD_CONST               8 ('error_code')
              LOAD_FAST_BORROW         8 (error_code)

211           BUILD_MAP                9
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\operator\audit_integrity.py", line 228>:
228           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

230           LOAD_CONST               2 ('Optional[str]')

228           LOAD_CONST               3 ('return')

231           LOAD_CONST               4 ('Dict[str, Any]')

228           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object compute_chain_head at 0x0000018C181FC460, file "app\services\operator\audit_integrity.py", line 228>:
 228            RESUME                   0

 235            LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L1)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST               1 (None)
        L2:     STORE_FAST               1 (bid)

 236            LOAD_GLOBAL              3 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               2 (db)

 237            LOAD_FAST_BORROW         2 (db)
                POP_JUMP_IF_NOT_NONE    17 (to L3)
                NOT_TAKEN

 238            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 239            LOAD_CONST               2 ('skipped')

 240            LOAD_FAST_BORROW         1 (bid)

 241            LOAD_CONST               3 ('audit_store_unavailable')
                BUILD_LIST               1

 242            LOAD_CONST               3 ('audit_store_unavailable')

 238            LOAD_CONST               4 (('status', 'brokerage_id', 'warnings', 'error_code'))
                CALL_KW                  4
                RETURN_VALUE

 244    L3:     NOP

 246    L4:     LOAD_FAST_BORROW         2 (db)
                LOAD_ATTR                7 (table + NULL|self)
                LOAD_GLOBAL              8 (_TABLE)
                CALL                     1

 247            LOAD_ATTR               11 (select + NULL|self)
                LOAD_CONST               5 ('row_hash, occurred_at')
                CALL                     1

 248            LOAD_ATTR               13 (order + NULL|self)
                LOAD_CONST               6 ('occurred_at')
                LOAD_CONST               7 (True)
                LOAD_CONST               8 (('desc',))
                CALL_KW                  2

 249            LOAD_ATTR               15 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 245            STORE_FAST               3 (query)

 251            LOAD_FAST_BORROW         1 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L7)
        L5:     NOT_TAKEN

 252    L6:     LOAD_FAST_BORROW         3 (query)
                LOAD_ATTR               17 (eq + NULL|self)
                LOAD_CONST               9 ('brokerage_id')
                LOAD_FAST_BORROW         1 (bid)
                CALL                     2
                STORE_FAST               3 (query)

 253    L7:     LOAD_FAST_BORROW         3 (query)
                LOAD_ATTR               19 (execute + NULL|self)
                CALL                     0
                STORE_FAST               4 (result)

 254            LOAD_GLOBAL             21 (list + NULL)
                LOAD_GLOBAL             23 (getattr + NULL)
                LOAD_FAST_BORROW         4 (result)
                LOAD_CONST              10 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                BUILD_LIST               0
       L10:     CALL                     1
                STORE_FAST               5 (rows)

 255            LOAD_FAST_BORROW         5 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        20 (to L14)
       L11:     NOT_TAKEN

 256   L12:     LOAD_GLOBAL              5 (_safe_envelope + NULL)

 257            LOAD_CONST              11 ('ok')

 258            LOAD_CONST              12 ('genesis')

 259            LOAD_FAST_BORROW         1 (bid)

 260            LOAD_GLOBAL             24 (GENESIS_HASH)

 256            LOAD_CONST              13 (('status', 'chain_status', 'brokerage_id', 'head'))
                CALL_KW                  4
       L13:     RETURN_VALUE

 262   L14:     LOAD_FAST_BORROW         5 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              14 ('row_hash')
                CALL                     1
                STORE_FAST               6 (head)

 263            LOAD_GLOBAL             29 (isinstance + NULL)
                LOAD_FAST_BORROW         6 (head)
                LOAD_GLOBAL             30 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L16)
                NOT_TAKEN
                LOAD_FAST_BORROW         6 (head)
                LOAD_ATTR               33 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L18)
       L15:     NOT_TAKEN

 264   L16:     LOAD_GLOBAL              5 (_safe_envelope + NULL)

 265            LOAD_CONST              11 ('ok')

 266            LOAD_CONST              15 ('degraded')

 267            LOAD_FAST_BORROW         1 (bid)

 268            LOAD_CONST               1 (None)

 269            LOAD_CONST              16 ('chain_head_missing_hash')
                BUILD_LIST               1

 264            LOAD_CONST              17 (('status', 'chain_status', 'brokerage_id', 'head', 'warnings'))
                CALL_KW                  5
       L17:     RETURN_VALUE

 271   L18:     LOAD_GLOBAL              5 (_safe_envelope + NULL)

 272            LOAD_CONST              11 ('ok')

 273            LOAD_CONST              11 ('ok')

 274            LOAD_FAST_BORROW         1 (bid)

 275            LOAD_FAST_BORROW         6 (head)

 271            LOAD_CONST              13 (('status', 'chain_status', 'brokerage_id', 'head'))
                CALL_KW                  4
       L19:     RETURN_VALUE

  --   L20:     PUSH_EXC_INFO

 277            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       92 (to L25)
                NOT_TAKEN
                STORE_FAST               7 (e)

 278   L21:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 279            LOAD_CONST              18 ('compute_chain_head read error type=')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 278            CALL                     1
                POP_TOP

 281            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 282            LOAD_CONST               2 ('skipped')

 283            LOAD_FAST                1 (bid)

 284            LOAD_CONST              19 ('db_read_failed:')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 285            LOAD_CONST               3 ('audit_store_unavailable')

 281            LOAD_CONST               4 (('status', 'brokerage_id', 'warnings', 'error_code'))
                CALL_KW                  4
       L22:     SWAP                     2
       L23:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L24:     LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 277   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L20 [0]
  L6 to L8 -> L20 [0]
  L9 to L11 -> L20 [0]
  L12 to L13 -> L20 [0]
  L14 to L15 -> L20 [0]
  L16 to L17 -> L20 [0]
  L18 to L19 -> L20 [0]
  L20 to L21 -> L26 [1] lasti
  L21 to L22 -> L24 [1] lasti
  L22 to L23 -> L26 [1] lasti
  L24 to L26 -> L26 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app\services\operator\audit_integrity.py", line 293>:
293           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

295           LOAD_CONST               2 ('Optional[str]')

293           LOAD_CONST               3 ('limit')

296           LOAD_CONST               4 ('Any')

293           LOAD_CONST               5 ('return')

297           LOAD_CONST               6 ('Dict[str, Any]')

293           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object verify_audit_chain at 0x0000018C181A2DB0, file "app\services\operator\audit_integrity.py", line 293>:
 293            RESUME                   0

 314            LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L1)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST               1 (None)
        L2:     STORE_FAST               2 (bid)

 315            LOAD_GLOBAL              3 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         1 (limit)
                CALL                     1
                STORE_FAST               3 (capped)

 316            LOAD_GLOBAL              5 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               4 (db)

 317            LOAD_FAST_BORROW         4 (db)
                POP_JUMP_IF_NOT_NONE    18 (to L3)
                NOT_TAKEN

 318            LOAD_GLOBAL              7 (_safe_envelope + NULL)

 319            LOAD_CONST               2 ('skipped')

 320            LOAD_FAST_BORROW         2 (bid)

 321            LOAD_FAST_BORROW         3 (capped)

 322            LOAD_CONST               3 ('audit_store_unavailable')
                BUILD_LIST               1

 323            LOAD_CONST               3 ('audit_store_unavailable')

 318            LOAD_CONST               4 (('status', 'brokerage_id', 'limit', 'warnings', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

 325    L3:     NOP

 327    L4:     LOAD_FAST_BORROW         4 (db)
                LOAD_ATTR                9 (table + NULL|self)
                LOAD_GLOBAL             10 (_TABLE)
                CALL                     1

 328            LOAD_ATTR               13 (select + NULL|self)

 329            LOAD_CONST               5 ('action_id, occurred_at, brokerage_id, actor_type, actor_id, action, target_type, target_id, status, warning_count, metadata, prev_hash, row_hash')

 328            CALL                     1

 333            LOAD_ATTR               15 (order + NULL|self)
                LOAD_CONST               6 ('occurred_at')
                LOAD_CONST               7 (False)
                LOAD_CONST               8 (('desc',))
                CALL_KW                  2

 334            LOAD_ATTR               17 (limit + NULL|self)
                LOAD_FAST_BORROW         3 (capped)
                CALL                     1

 326            STORE_FAST               5 (query)

 336            LOAD_FAST_BORROW         2 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L7)
        L5:     NOT_TAKEN

 337    L6:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               19 (eq + NULL|self)
                LOAD_CONST               9 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)
                CALL                     2
                STORE_FAST               5 (query)

 338    L7:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               21 (execute + NULL|self)
                CALL                     0
                STORE_FAST               6 (result)

 339            LOAD_GLOBAL             23 (list + NULL)
                LOAD_GLOBAL             25 (getattr + NULL)
                LOAD_FAST_BORROW         6 (result)
                LOAD_CONST              10 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                BUILD_LIST               0
       L10:     CALL                     1
                STORE_FAST               7 (rows)

 351   L11:     LOAD_FAST                7 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        22 (to L12)
                NOT_TAKEN

 352            LOAD_GLOBAL              7 (_safe_envelope + NULL)

 353            LOAD_CONST              13 ('ok')

 354            LOAD_CONST              14 ('genesis')

 355            LOAD_FAST                2 (bid)

 356            LOAD_FAST                3 (capped)

 357            LOAD_SMALL_INT           0

 358            LOAD_GLOBAL             36 (GENESIS_HASH)

 352            LOAD_CONST              15 (('status', 'chain_status', 'brokerage_id', 'limit', 'rows_checked', 'head'))
                CALL_KW                  6
                RETURN_VALUE

 361   L12:     BUILD_LIST               0
                STORE_FAST               9 (breaks)

 362            LOAD_GLOBAL             36 (GENESIS_HASH)
                STORE_FAST              10 (expected_prev)

 363            LOAD_CONST               1 (None)
                STORE_FAST              11 (last_row_hash)

 364            LOAD_FAST                7 (rows)
                GET_ITER
       L13:     EXTENDED_ARG             1
                FOR_ITER               360 (to L23)
                STORE_FAST              12 (r)

 365            LOAD_GLOBAL             39 (isinstance + NULL)
                LOAD_FAST               12 (r)
                LOAD_GLOBAL             40 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN

 366            JUMP_BACKWARD           28 (to L13)

 367   L14:     LOAD_FAST               12 (r)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST              16 ('action_id')
                CALL                     1
                STORE_FAST              13 (action_id)

 368            LOAD_FAST               12 (r)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST               6 ('occurred_at')
                CALL                     1
                STORE_FAST              14 (occurred_at)

 369            LOAD_FAST               12 (r)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST              17 ('prev_hash')
                CALL                     1
                STORE_FAST              15 (stored_prev)

 370            LOAD_FAST               12 (r)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST              18 ('row_hash')
                CALL                     1
                STORE_FAST              16 (stored_row)

 371            LOAD_GLOBAL             45 (compute_row_hash + NULL)
                LOAD_FAST_LOAD_FAST    172 (expected_prev, r)
                CALL                     2
                STORE_FAST              17 (recomputed_hash)

 373            LOAD_GLOBAL             39 (isinstance + NULL)
                LOAD_FAST               15 (stored_prev)
                LOAD_GLOBAL             46 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L15)
                NOT_TAKEN
                LOAD_FAST               15 (stored_prev)
                LOAD_ATTR               49 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        27 (to L16)
                NOT_TAKEN

 374   L15:     LOAD_FAST                9 (breaks)
                LOAD_ATTR               51 (append + NULL|self)

 375            LOAD_CONST              16 ('action_id')
                LOAD_FAST               13 (action_id)

 376            LOAD_CONST               6 ('occurred_at')
                LOAD_FAST               14 (occurred_at)

 377            LOAD_CONST              19 ('break_type')
                LOAD_CONST              20 ('missing_prev_hash')

 378            LOAD_CONST              21 ('expected_prev_hash_present')
                LOAD_CONST              22 (True)

 374            BUILD_MAP                4
                CALL                     1
                POP_TOP
                JUMP_FORWARD            31 (to L17)

 382   L16:     LOAD_FAST_LOAD_FAST    250 (stored_prev, expected_prev)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       26 (to L17)
                NOT_TAKEN

 383            LOAD_FAST                9 (breaks)
                LOAD_ATTR               51 (append + NULL|self)

 384            LOAD_CONST              16 ('action_id')
                LOAD_FAST               13 (action_id)

 385            LOAD_CONST               6 ('occurred_at')
                LOAD_FAST               14 (occurred_at)

 386            LOAD_CONST              19 ('break_type')
                LOAD_CONST              23 ('prev_hash_mismatch')

 387            LOAD_CONST              21 ('expected_prev_hash_present')
                LOAD_CONST              22 (True)

 383            BUILD_MAP                4
                CALL                     1
                POP_TOP

 389   L17:     LOAD_GLOBAL             39 (isinstance + NULL)
                LOAD_FAST               16 (stored_row)
                LOAD_GLOBAL             46 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L18)
                NOT_TAKEN
                LOAD_FAST               16 (stored_row)
                LOAD_ATTR               49 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        27 (to L19)
                NOT_TAKEN

 390   L18:     LOAD_FAST                9 (breaks)
                LOAD_ATTR               51 (append + NULL|self)

 391            LOAD_CONST              16 ('action_id')
                LOAD_FAST               13 (action_id)

 392            LOAD_CONST               6 ('occurred_at')
                LOAD_FAST               14 (occurred_at)

 393            LOAD_CONST              19 ('break_type')
                LOAD_CONST              24 ('missing_row_hash')

 394            LOAD_CONST              25 ('expected_row_hash_present')
                LOAD_CONST              22 (True)

 390            BUILD_MAP                4
                CALL                     1
                POP_TOP
                JUMP_FORWARD            32 (to L20)

 396   L19:     LOAD_FAST               16 (stored_row)
                LOAD_FAST               17 (recomputed_hash)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       26 (to L20)
                NOT_TAKEN

 397            LOAD_FAST                9 (breaks)
                LOAD_ATTR               51 (append + NULL|self)

 398            LOAD_CONST              16 ('action_id')
                LOAD_FAST               13 (action_id)

 399            LOAD_CONST               6 ('occurred_at')
                LOAD_FAST               14 (occurred_at)

 400            LOAD_CONST              19 ('break_type')
                LOAD_CONST              26 ('row_hash_mismatch')

 401            LOAD_CONST              25 ('expected_row_hash_present')
                LOAD_CONST              22 (True)

 397            BUILD_MAP                4
                CALL                     1
                POP_TOP

 407   L20:     LOAD_GLOBAL             39 (isinstance + NULL)
                LOAD_FAST               16 (stored_row)
                LOAD_GLOBAL             46 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L21)
                NOT_TAKEN
                LOAD_FAST               16 (stored_row)
                LOAD_ATTR               49 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L21)
                NOT_TAKEN
                LOAD_FAST               16 (stored_row)
                JUMP_FORWARD             1 (to L22)

 408   L21:     LOAD_FAST               17 (recomputed_hash)

 406   L22:     STORE_FAST              10 (expected_prev)

 410            LOAD_FAST               10 (expected_prev)
                STORE_FAST              11 (last_row_hash)
                EXTENDED_ARG             1
                JUMP_BACKWARD          363 (to L13)

 364   L23:     END_FOR
                POP_ITER

 412            LOAD_FAST                9 (breaks)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L24)
                NOT_TAKEN
                LOAD_CONST              13 ('ok')
                JUMP_FORWARD             1 (to L25)
       L24:     LOAD_CONST              27 ('degraded')
       L25:     STORE_FAST              18 (chain_status)

 413            LOAD_GLOBAL              7 (_safe_envelope + NULL)

 414            LOAD_CONST              13 ('ok')

 415            LOAD_FAST               18 (chain_status)

 416            LOAD_FAST                2 (bid)

 417            LOAD_FAST                3 (capped)

 418            LOAD_GLOBAL             53 (len + NULL)
                LOAD_FAST                7 (rows)
                CALL                     1

 419            LOAD_FAST                9 (breaks)

 420            LOAD_FAST               11 (last_row_hash)

 413            LOAD_CONST              28 (('status', 'chain_status', 'brokerage_id', 'limit', 'rows_checked', 'breaks', 'head'))
                CALL_KW                  7
                RETURN_VALUE

  --   L26:     PUSH_EXC_INFO

 340            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       93 (to L31)
                NOT_TAKEN
                STORE_FAST               8 (e)

 341   L27:     LOAD_GLOBAL             28 (logger)
                LOAD_ATTR               31 (warning + NULL|self)

 342            LOAD_CONST              11 ('verify_audit_chain db error type=')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 341            CALL                     1
                POP_TOP

 344            LOAD_GLOBAL              7 (_safe_envelope + NULL)

 345            LOAD_CONST               2 ('skipped')

 346            LOAD_FAST                2 (bid)

 347            LOAD_FAST                3 (capped)

 348            LOAD_CONST              12 ('db_read_failed:')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 349            LOAD_CONST               3 ('audit_store_unavailable')

 344            LOAD_CONST               4 (('status', 'brokerage_id', 'limit', 'warnings', 'error_code'))
                CALL_KW                  5
       L28:     SWAP                     2
       L29:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RETURN_VALUE

  --   L30:     LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 340   L31:     RERAISE                  0

  --   L32:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L26 [0]
  L6 to L8 -> L26 [0]
  L9 to L11 -> L26 [0]
  L26 to L27 -> L32 [1] lasti
  L27 to L28 -> L30 [1] lasti
  L28 to L29 -> L32 [1] lasti
  L30 to L32 -> L32 [1] lasti
```
