# operator/audit_window_chain

- **pyc:** `app\services\operator\__pycache__\audit_window_chain.cpython-314.pyc`
- **expected source path (absent):** `app\services\operator/audit_window_chain.py`
- **co_filename (from bytecode):** `app/services/operator/audit_window_chain.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** operator

## Module docstring

```
PAS178 — Cross-window Merkle chain service.

Forward-secure chain linking PAS176 Merkle windows over time.
Each chain entry references a Merkle root and computes a
``chain_hash`` over `(previous_chain_hash, merkle_root_hash,
window_start, window_end, brokerage_id)`. Chain entries are
append-only at all layers.

Doctrine carried by every helper:

* **Append-only.** Insert + read helpers only. No update /
  delete; the PAS178 readiness gate structurally enforces
  the absence of mutation symbols.
* **Deterministic hashing.** Same inputs → byte-identical
  ``chain_hash``. Hash material is a closed allow-list of
  structural fields only.
* **No PII.** No phone / email / name / transcript / raw
  payload / signature / secret / env_value / callback_notes
  / raw_audit_metadata. The metadata column is projected
  against a closed allow-list at insert time.
* **Closed enums** mirror v26 CHECK constraints:
    actor_type ∈ {OPERATOR, ADMIN, SYSTEM}
    status     ∈ {GENERATED, VERIFIED, BROKEN, SUPERSEDED}
* **NEVER raises.** DB unavailable → ``status="skipped"``.
* **No auto-repair.** A detected break surfaces structurally;
  the operator decides whether to file a P0.

Public surface:

  * ``compute_audit_window_chain_hash(...)`` — pure function.
  * ``generate_audit_window_chain_entry(...)`` — append-only insert.
  * ``verify_audit_window_chain(...)`` — read-only walk.
  * ``chain_status_report(...)`` — structural summary.
  * ``brokerage_chain_badge(...)`` — compact operator badge.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `datetime`, `get_supabase`, `hashlib`, `json`, `logging`, `timezone`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_bound_actor_id`, `_bound_brokerage_id`, `_clamp_limit`, `_get_db_safe`, `_is_sha256_hex`, `_iso`, `_now_dt`, `_project_metadata`, `_project_row`, `_read_chain_head_safe`, `_safe_envelope`, `brokerage_chain_badge`, `chain_status_report`, `compute_audit_window_chain_hash`, `generate_audit_window_chain_entry`, `verify_audit_window_chain`

## Env-key candidates

`BROKEN`, `GENERATED`, `GENESIS`, `OPERATOR`, `VERIFIED`

## String constants (redacted where noted)

- '\nPAS178 — Cross-window Merkle chain service.\n\nForward-secure chain linking PAS176 Merkle windows over time.\nEach chain entry references a Merkle root and computes a\n``chain_hash`` over `(previous_chain_hash, merkle_root_hash,\nwindow_start, window_end, brokerage_id)`. Chain entries are\nappend-only at all layers.\n\nDoctrine carried by every helper:\n\n* **Append-only.** Insert + read helpers only. No update /\n  delete; the PAS178 readiness gate structurally enforces\n  the absence of mutation symbols.\n* **Deterministic hashing.** Same inputs → byte-identical\n  ``chain_hash``. Hash material is a closed allow-list of\n  structural fields only.\n* **No PII.** No phone / email / name / transcript / raw\n  payload / signature / secret / env_value / callback_notes\n  / raw_audit_metadata. The metadata column is projected\n  against a closed allow-list at insert time.\n* **Closed enums** mirror v26 CHECK constraints:\n    actor_type ∈ {OPERATOR, ADMIN, SYSTEM}\n    status     ∈ {GENERATED, VERIFIED, BROKEN, SUPERSEDED}\n* **NEVER raises.** DB unavailable → ``status="skipped"``.\n* **No auto-repair.** A detected break surfaces structurally;\n  the operator decides whether to file a P0.\n\nPublic surface:\n\n  * ``compute_audit_window_chain_hash(...)`` — pure function.\n  * ``generate_audit_window_chain_entry(...)`` — append-only insert.\n  * ``verify_audit_window_chain(...)`` — read-only walk.\n  * ``chain_status_report(...)`` — structural summary.\n  * ``brokerage_chain_badge(...)`` — compact operator badge.\n'
- 'pas.operator.audit_window_chain'
- 'pas_audit_window_chain'
- 'pas_audit_merkle_roots'
- 'OPERATOR'
- 'GENESIS'
- 'error_code'
- 🔒 '<REDACTED:high-entropy blob, len=64>'
- 'brokerage_id'
- 'generated_by_actor_type'
- 'generated_by_actor_id'
- 'metadata'
- 'entry'
- 'warnings'
- 'now'
- 'limit'
- 'Any'
- 'return'
- 'datetime'
- 'str'
- 'seconds'
- 'audit_window_chain db client unavailable type='
- 'value'
- 'bool'
- '0123456789abcdef'
- 'Optional[str]'
- 'Dict[str, Any]'
- 'row'
- 'Optional[Dict[str, Any]]'
- 'int'
- 'status'
- 'Optional[List[str]]'
- 'previous_chain_hash'
- 'merkle_root_hash'
- 'window_start'
- 'window_end'
- 'Deterministically compute the chain_hash. NEVER raises.\n\nHash material is the canonical JSON serialisation of a\nclosed allow-list of structural fields — no raw payload,\nno PII, no env values.\n'
- 'utf-8'
- 'compute_audit_window_chain_hash unexpected error type='
- "Most-recent chain entry's ``chain_hash`` for the given\nscope. Returns the GENESIS sentinel when none exists.\nNEVER raises."
- 'chain_hash, window_end'
- 'data'
- 'chain_hash'
- '_read_chain_head_safe error type='
- 'merkle_root_id'
- 'Generate + append a chain entry. NEVER raises.\n\nOutcomes:\n  * ``status="ok"`` — fresh insert; ``entry`` populated.\n  * ``status="skipped"`` — DB unavailable.\n  * ``status="failed"`` — input validation error.\n'
- 'failed'
- 'invalid_actor_type'
- 'invalid_merkle_root_hash_shape'
- 'missing_merkle_root_id'
- 'missing_window_start'
- 'missing_window_end'
- 'invalid_brokerage_id'
- 'invalid_actor_id'
- 'skipped'
- 'audit_window_chain_store_unavailable'
- 'chain_window_id'
- 'generated_at'
- 'GENERATED'
- 'generate_audit_window_chain_entry db error type='
- 'db_write_failed:'
- 'Walk chain entries in ``window_start ASC``; recompute\neach ``chain_hash``; flag any breaks. NEVER raises.\n\nReturns a structural envelope::\n\n    {\n      "status":       "ok" | "skipped",\n      "brokerage_id": Optional[str],\n      "limit":        int,\n      "entries_checked": int,\n      "chain_status": "ok" | "genesis" | "degraded",\n      "breaks_count": int,\n      "breaks":       [<structural break>, ...],\n      "warnings":     [<structural>],\n      "error_code":   None | "<structural>",\n    }\n'
- 'entries_checked'
- 'chain_status'
- 'genesis'
- 'breaks_count'
- 'breaks'
- 'verify_audit_window_chain read error type='
- 'db_read_failed:'
- 'break_type'
- 'missing_previous_chain_hash'
- 'previous_chain_hash_mismatch'
- 'missing_chain_hash'
- 'chain_hash_mismatch'
- 'degraded'
- 'Structural summary of the chain entries: count by\nstatus, latest entry, latest chain_hash fingerprint.\nNEVER raises. NEVER returns PII.'
- 'total'
- 'by_status'
- 'latest_entry'
- 'chain_status_report read error type='
- 'Compact badge for the multi-brokerage operator console.\nReturns only structural status tokens — never PII.'
- 'unknown'
- 'entries_total'
- 'latest_window_end'
- 'missing_brokerage_id'
- 'none'
- 'BROKEN'
- 'broken'
- 'VERIFIED'
- 'verified'
- 'mixed'
- 'generated'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS178 — Cross-window Merkle chain service.\n\nForward-secure chain linking PAS176 Merkle windows over time.\nEach chain entry references a Merkle root and computes a\n``chain_hash`` over `(previous_chain_hash, merkle_root_hash,\nwindow_start, window_end, brokerage_id)`. Chain entries are\nappend-only at all layers.\n\nDoctrine carried by every helper:\n\n* **Append-only.** Insert + read helpers only. No update /\n  delete; the PAS178 readiness gate structurally enforces\n  the absence of mutation symbols.\n* **Deterministic hashing.** Same inputs → byte-identical\n  ``chain_hash``. Hash material is a closed allow-list of\n  structural fields only.\n* **No PII.** No phone / email / name / transcript / raw\n  payload / signature / secret / env_value / callback_notes\n  / raw_audit_metadata. The metadata column is projected\n  against a closed allow-list at insert time.\n* **Closed enums** mirror v26 CHECK constraints:\n    actor_type ∈ {OPERATOR, ADMIN, SYSTEM}\n    status     ∈ {GENERATED, VERIFIED, BROKEN, SUPERSEDED}\n* **NEVER raises.** DB unavailable → ``status="skipped"``.\n* **No auto-repair.** A detected break surfaces structurally;\n  the operator decides whether to file a P0.\n\nPublic surface:\n\n  * ``compute_audit_window_chain_hash(...)`` — pure function.\n  * ``generate_audit_window_chain_entry(...)`` — append-only insert.\n  * ``verify_audit_window_chain(...)`` — read-only walk.\n  * ``chain_status_report(...)`` — structural summary.\n  * ``brokerage_chain_badge(...)`` — compact operator badge.\n')
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
              LOAD_CONST               2 (None)
              IMPORT_NAME              6 (uuid)
              STORE_NAME               6 (uuid)

 44           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timezone'))
              IMPORT_NAME              7 (datetime)
              IMPORT_FROM              7 (datetime)
              STORE_NAME               7 (datetime)
              IMPORT_FROM              8 (timezone)
              STORE_NAME               8 (timezone)
              POP_TOP

 45           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              9 (typing)
              IMPORT_FROM             10 (Any)
              STORE_NAME              10 (Any)
              IMPORT_FROM             11 (Dict)
              STORE_NAME              11 (Dict)
              IMPORT_FROM             12 (List)
              STORE_NAME              12 (List)
              IMPORT_FROM             13 (Optional)
              STORE_NAME              13 (Optional)
              POP_TOP

 48           LOAD_NAME                5 (logging)
              LOAD_ATTR               28 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.operator.audit_window_chain')
              CALL                     1
              STORE_NAME              15 (logger)

 51           LOAD_CONST               6 ('pas_audit_window_chain')
              STORE_NAME              16 (_CHAIN_TABLE)

 52           LOAD_CONST               7 ('pas_audit_merkle_roots')
              STORE_NAME              17 (_MERKLE_TABLE)

 56           LOAD_CONST              52 (('OPERATOR', 'ADMIN', 'SYSTEM'))
              STORE_NAME              18 (ALLOWED_ACTOR_TYPES)

 57           LOAD_CONST              53 (('GENERATED', 'VERIFIED', 'BROKEN', 'SUPERSEDED'))
              STORE_NAME              19 (ALLOWED_CHAIN_STATUSES)

 61           LOAD_CONST               9 ('GENESIS')
              STORE_NAME              20 (GENESIS_CHAIN_SENTINEL)

 64           LOAD_CONST              54 (('rows_in_window', 'warning_count', 'error_code', 'event', 'chain_index'))
              STORE_NAME              21 (ALLOWED_METADATA_KEYS)

 73           LOAD_SMALL_INT         200
              STORE_NAME              22 (_BROKERAGE_ID_MAX_LEN)

 74           LOAD_SMALL_INT         200
              STORE_NAME              23 (_ACTOR_ID_MAX_LEN)

 75           LOAD_CONST              11 (5000)
              STORE_NAME              24 (_LIST_HARD_CAP)

 76           LOAD_SMALL_INT         200
              STORE_NAME              25 (_DEFAULT_LIMIT)

 80           LOAD_CONST              12 ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_')

 79           STORE_NAME              26 (_ALLOWED_TOKEN_CHARS)

 86           LOAD_CONST              55 (('chain_window_id', 'brokerage_id', 'window_start', 'window_end', 'merkle_root_id', 'merkle_root_hash', 'previous_chain_hash', 'chain_hash', 'generated_at', 'generated_by_actor_type', 'generated_by_actor_id', 'status', 'metadata'))
              STORE_NAME              27 (_STRUCTURAL_COLUMNS)

107           LOAD_CONST              56 ((None,))
              LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA32D0, file "app/services/operator/audit_window_chain.py", line 107>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _now_dt at 0x0000018C180D4030, file "app/services/operator/audit_window_chain.py", line 107>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              28 (_now_dt)

115           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA34B0, file "app/services/operator/audit_window_chain.py", line 115>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _iso at 0x0000018C18025530, file "app/services/operator/audit_window_chain.py", line 115>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_iso)

119           LOAD_CONST              21 (<code object _get_db_safe at 0x0000018C17FF13B0, file "app/services/operator/audit_window_chain.py", line 119>)
              MAKE_FUNCTION
              STORE_NAME              30 (_get_db_safe)

131           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA2100, file "app/services/operator/audit_window_chain.py", line 131>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object _is_sha256_hex at 0x0000018C1794ED80, file "app/services/operator/audit_window_chain.py", line 131>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_is_sha256_hex)

140           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA2970, file "app/services/operator/audit_window_chain.py", line 140>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object _bound_brokerage_id at 0x0000018C17F96420, file "app/services/operator/audit_window_chain.py", line 140>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_bound_brokerage_id)

149           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA23D0, file "app/services/operator/audit_window_chain.py", line 149>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object _bound_actor_id at 0x0000018C180D4210, file "app/services/operator/audit_window_chain.py", line 149>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_bound_actor_id)

160           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA2B50, file "app/services/operator/audit_window_chain.py", line 160>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object _project_metadata at 0x0000018C17FEE030, file "app/services/operator/audit_window_chain.py", line 160>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              34 (_project_metadata)

175           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA2D30, file "app/services/operator/audit_window_chain.py", line 175>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object _project_row at 0x0000018C1796DBD0, file "app/services/operator/audit_window_chain.py", line 175>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              35 (_project_row)

186           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA21F0, file "app/services/operator/audit_window_chain.py", line 186>)
              MAKE_FUNCTION
              LOAD_CONST              33 (<code object _clamp_limit at 0x0000018C17972550, file "app/services/operator/audit_window_chain.py", line 186>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              36 (_clamp_limit)

198           LOAD_CONST              34 ('entry')

201           LOAD_CONST               2 (None)

198           LOAD_CONST              35 ('warnings')

202           LOAD_CONST               2 (None)

198           LOAD_CONST              10 ('error_code')

203           LOAD_CONST               2 (None)

198           BUILD_MAP                3
              LOAD_CONST              36 (<code object __annotate__ at 0x0000018C18024E30, file "app/services/operator/audit_window_chain.py", line 198>)
              MAKE_FUNCTION
              LOAD_CONST              37 (<code object _safe_envelope at 0x0000018C180C4140, file "app/services/operator/audit_window_chain.py", line 198>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              37 (_safe_envelope)

217           LOAD_CONST              13 ('brokerage_id')

223           LOAD_CONST               2 (None)

217           BUILD_MAP                1
              LOAD_CONST              38 (<code object __annotate__ at 0x0000018C18024B30, file "app/services/operator/audit_window_chain.py", line 217>)
              MAKE_FUNCTION
              LOAD_CONST              39 (<code object compute_audit_window_chain_hash at 0x0000018C17D81910, file "app/services/operator/audit_window_chain.py", line 217>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              38 (compute_audit_window_chain_hash)

265           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C18025D30, file "app/services/operator/audit_window_chain.py", line 265>)
              MAKE_FUNCTION
              LOAD_CONST              41 (<code object _read_chain_head_safe at 0x0000018C17D8BF50, file "app/services/operator/audit_window_chain.py", line 265>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              39 (_read_chain_head_safe)

305           LOAD_CONST              14 ('generated_by_actor_type')

312           LOAD_CONST               8 ('OPERATOR')

305           LOAD_CONST              15 ('generated_by_actor_id')

313           LOAD_CONST               2 (None)

305           LOAD_CONST              16 ('metadata')

314           LOAD_CONST               2 (None)

305           LOAD_CONST              42 ('now')

315           LOAD_CONST               2 (None)

305           BUILD_MAP                4
              LOAD_CONST              43 (<code object __annotate__ at 0x0000018C180C4250, file "app/services/operator/audit_window_chain.py", line 305>)
              MAKE_FUNCTION
              LOAD_CONST              44 (<code object generate_audit_window_chain_entry at 0x0000018C17E94C50, file "app/services/operator/audit_window_chain.py", line 305>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              40 (generate_audit_window_chain_entry)

400           LOAD_CONST              13 ('brokerage_id')

402           LOAD_CONST               2 (None)

400           LOAD_CONST              45 ('limit')

403           LOAD_NAME               25 (_DEFAULT_LIMIT)

400           BUILD_MAP                2
              LOAD_CONST              46 (<code object __annotate__ at 0x0000018C18025E30, file "app/services/operator/audit_window_chain.py", line 400>)
              MAKE_FUNCTION
              LOAD_CONST              47 (<code object verify_audit_window_chain at 0x0000018C17D51720, file "app/services/operator/audit_window_chain.py", line 400>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              41 (verify_audit_window_chain)

552           LOAD_CONST              13 ('brokerage_id')

554           LOAD_CONST               2 (None)

552           LOAD_CONST              45 ('limit')

555           LOAD_NAME               25 (_DEFAULT_LIMIT)

552           BUILD_MAP                2
              LOAD_CONST              48 (<code object __annotate__ at 0x0000018C18025C30, file "app/services/operator/audit_window_chain.py", line 552>)
              MAKE_FUNCTION
              LOAD_CONST              49 (<code object chain_status_report at 0x0000018C17D51E80, file "app/services/operator/audit_window_chain.py", line 552>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              42 (chain_status_report)

619           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C17FA30F0, file "app/services/operator/audit_window_chain.py", line 619>)
              MAKE_FUNCTION
              LOAD_CONST              51 (<code object brokerage_chain_badge at 0x0000018C17D7C8F0, file "app/services/operator/audit_window_chain.py", line 619>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              43 (brokerage_chain_badge)

668           BUILD_LIST               0
              LOAD_CONST              57 (('GENESIS_CHAIN_SENTINEL', 'ALLOWED_ACTOR_TYPES', 'ALLOWED_CHAIN_STATUSES', 'ALLOWED_METADATA_KEYS', 'compute_audit_window_chain_hash', 'generate_audit_window_chain_entry', 'verify_audit_window_chain', 'chain_status_report', 'brokerage_chain_badge'))
              LIST_EXTEND              1
              STORE_NAME              44 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "app/services/operator/audit_window_chain.py", line 107>:
107           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('now')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('datetime')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _now_dt at 0x0000018C180D4030, file "app/services/operator/audit_window_chain.py", line 107>:
107           RESUME                   0

108           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (now)
              LOAD_GLOBAL              2 (datetime)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       78 (to L2)
              NOT_TAKEN

109           LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR                4 (tzinfo)
              POP_JUMP_IF_NOT_NONE    33 (to L1)
              NOT_TAKEN

110           LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR                7 (replace + NULL|self)
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              LOAD_CONST               1 (('tzinfo',))
              CALL_KW                  1
              RETURN_VALUE

111   L1:     LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR               13 (astimezone + NULL|self)
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              CALL                     1
              RETURN_VALUE

112   L2:     LOAD_GLOBAL              2 (datetime)
              LOAD_ATTR               14 (now)
              PUSH_NULL
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app/services/operator/audit_window_chain.py", line 115>:
115           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('dt')
              LOAD_CONST               2 ('datetime')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _iso at 0x0000018C18025530, file "app/services/operator/audit_window_chain.py", line 115>:
115           RESUME                   0

116           LOAD_FAST_BORROW         0 (dt)
              LOAD_ATTR                1 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object _get_db_safe at 0x0000018C17FF13B0, file "app/services/operator/audit_window_chain.py", line 119>:
 119           RESUME                   0

 120           NOP

 121   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 122           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 123           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 124   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 125           LOAD_CONST               2 ('audit_window_chain db client unavailable type=')

 126           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 125           BUILD_STRING             2

 124           CALL                     1
               POP_TOP

 128   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 123   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app/services/operator/audit_window_chain.py", line 131>:
131           RESUME                   0
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
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _is_sha256_hex at 0x0000018C1794ED80, file "app/services/operator/audit_window_chain.py", line 131>:
131           RESUME                   0

132           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

133           LOAD_CONST               0 (False)
              RETURN_VALUE

134   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR                7 (lower + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

135           LOAD_GLOBAL              9 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_SMALL_INT          64
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

136           LOAD_CONST               0 (False)
              RETURN_VALUE

137   L2:     LOAD_GLOBAL             10 (all)
              COPY                     1
              LOAD_COMMON_CONSTANT     3 (<built-in function all>)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE       28 (to L6)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18024C30, file "app/services/operator/audit_window_chain.py", line 137>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (s)
              GET_ITER
              CALL                     0
      L3:     FOR_ITER                12 (to L5)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L3)
      L4:     POP_ITER
              LOAD_CONST               0 (False)
              RETURN_VALUE
      L5:     END_FOR
              POP_ITER
              LOAD_CONST               2 (True)
              RETURN_VALUE
      L6:     PUSH_NULL
              LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18024C30, file "app/services/operator/audit_window_chain.py", line 137>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (s)
              GET_ITER
              CALL                     0
              CALL                     1
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18024C30, file "app/services/operator/audit_window_chain.py", line 137>:
 137           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app/services/operator/audit_window_chain.py", line 140>:
140           RESUME                   0
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

Disassembly of <code object _bound_brokerage_id at 0x0000018C17F96420, file "app/services/operator/audit_window_chain.py", line 140>:
140           RESUME                   0

141           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

142           LOAD_CONST               0 (None)
              RETURN_VALUE

143   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

144           LOAD_FAST_BORROW         1 (s)
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

145   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

146   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app/services/operator/audit_window_chain.py", line 149>:
149           RESUME                   0
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

Disassembly of <code object _bound_actor_id at 0x0000018C180D4210, file "app/services/operator/audit_window_chain.py", line 149>:
149           RESUME                   0

150           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

151           LOAD_CONST               0 (None)
              RETURN_VALUE

152   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

153           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_ACTOR_ID_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

154   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

155   L3:     LOAD_GLOBAL             10 (any)
              COPY                     1
              LOAD_COMMON_CONSTANT     4 (<built-in function any>)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE       28 (to L7)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 (<code object <genexpr> at 0x0000018C17FBFEE0, file "app/services/operator/audit_window_chain.py", line 155>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (s)
              GET_ITER
              CALL                     0
      L4:     FOR_ITER                12 (to L6)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L4)
      L5:     POP_ITER
              LOAD_CONST               2 (True)
              JUMP_FORWARD            17 (to L8)
      L6:     END_FOR
              POP_ITER
              LOAD_CONST               3 (False)
              JUMP_FORWARD            13 (to L8)
      L7:     PUSH_NULL
              LOAD_CONST               1 (<code object <genexpr> at 0x0000018C17FBFEE0, file "app/services/operator/audit_window_chain.py", line 155>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (s)
              GET_ITER
              CALL                     0
              CALL                     1
      L8:     TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L9)
              NOT_TAKEN

156           LOAD_CONST               0 (None)
              RETURN_VALUE

157   L9:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C17FBFEE0, file "app/services/operator/audit_window_chain.py", line 155>:
 155           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                13 (to L3)
               STORE_FAST_LOAD_FAST    17 (ch, ch)
               LOAD_GLOBAL              0 (_ALLOWED_TOKEN_CHARS)
               CONTAINS_OP              1 (not in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           15 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app/services/operator/audit_window_chain.py", line 160>:
160           RESUME                   0
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

Disassembly of <code object _project_metadata at 0x0000018C17FEE030, file "app/services/operator/audit_window_chain.py", line 160>:
160           RESUME                   0

161           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (metadata)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

162           BUILD_MAP                0
              RETURN_VALUE

163   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

164           LOAD_GLOBAL              4 (ALLOWED_METADATA_KEYS)
              GET_ITER
      L2:     FOR_ITER               108 (to L8)
              STORE_FAST               2 (k)

165           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, metadata)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

166           JUMP_BACKWARD           11 (to L2)

167   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (metadata, k)
              BINARY_OP               26 ([])
              STORE_FAST               3 (v)

168           LOAD_FAST_BORROW         3 (v)
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

169   L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD           62 (to L2)

170   L5:     LOAD_GLOBAL              1 (isinstance + NULL)
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
              LOAD_SMALL_INT         200
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_TRUE         3 (to L7)
              NOT_TAKEN
              JUMP_BACKWARD          104 (to L2)

171   L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD          110 (to L2)

164   L8:     END_FOR
              POP_ITER

172           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app/services/operator/audit_window_chain.py", line 175>:
175           RESUME                   0
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
              LOAD_CONST               4 ('Optional[Dict[str, Any]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _project_row at 0x0000018C1796DBD0, file "app/services/operator/audit_window_chain.py", line 175>:
175           RESUME                   0

176           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

177           LOAD_CONST               0 (None)
              RETURN_VALUE

178   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

179           LOAD_GLOBAL              4 (_STRUCTURAL_COLUMNS)
              GET_ITER
      L2:     FOR_ITER                21 (to L4)
              STORE_FAST               2 (col)

180           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (col, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

181   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, col)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, col)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L2)

179   L4:     END_FOR
              POP_ITER

182           LOAD_GLOBAL              7 (_project_metadata + NULL)
              LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               1 ('metadata')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L5:     CALL                     1
              LOAD_FAST_BORROW         1 (out)
              LOAD_CONST               1 ('metadata')
              STORE_SUBSCR

183           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app/services/operator/audit_window_chain.py", line 186>:
186           RESUME                   0
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

Disassembly of <code object _clamp_limit at 0x0000018C17972550, file "app/services/operator/audit_window_chain.py", line 186>:
 186           RESUME                   0

 187           NOP

 188   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (v)

 191   L2:     LOAD_FAST                1 (v)
               LOAD_SMALL_INT           1
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 192           LOAD_SMALL_INT           1
               RETURN_VALUE

 193   L3:     LOAD_FAST                1 (v)
               LOAD_GLOBAL              8 (_LIST_HARD_CAP)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 194           LOAD_GLOBAL              8 (_LIST_HARD_CAP)
               RETURN_VALUE

 195   L4:     LOAD_FAST                1 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 189           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

 190           LOAD_GLOBAL              6 (_DEFAULT_LIMIT)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 189   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app/services/operator/audit_window_chain.py", line 198>:
198           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

200           LOAD_CONST               2 ('str')

198           LOAD_CONST               3 ('entry')

201           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

198           LOAD_CONST               5 ('warnings')

202           LOAD_CONST               6 ('Optional[List[str]]')

198           LOAD_CONST               7 ('error_code')

203           LOAD_CONST               8 ('Optional[str]')

198           LOAD_CONST               9 ('return')

204           LOAD_CONST              10 ('Dict[str, Any]')

198           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C180C4140, file "app/services/operator/audit_window_chain.py", line 198>:
198           RESUME                   0

206           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

207           LOAD_CONST               1 ('entry')
              LOAD_FAST                1 (entry)

208           LOAD_CONST               2 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                2 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

209           LOAD_CONST               3 ('error_code')
              LOAD_FAST_BORROW         3 (error_code)

205           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app/services/operator/audit_window_chain.py", line 217>:
217           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('previous_chain_hash')

219           LOAD_CONST               2 ('Any')

217           LOAD_CONST               3 ('merkle_root_hash')

220           LOAD_CONST               2 ('Any')

217           LOAD_CONST               4 ('window_start')

221           LOAD_CONST               2 ('Any')

217           LOAD_CONST               5 ('window_end')

222           LOAD_CONST               2 ('Any')

217           LOAD_CONST               6 ('brokerage_id')

223           LOAD_CONST               2 ('Any')

217           LOAD_CONST               7 ('return')

224           LOAD_CONST               8 ('str')

217           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object compute_audit_window_chain_hash at 0x0000018C17D81910, file "app/services/operator/audit_window_chain.py", line 217>:
 217            RESUME                   0

 233            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (previous_chain_hash)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (previous_chain_hash)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L1)
                NOT_TAKEN

 232            LOAD_FAST_BORROW         0 (previous_chain_hash)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             5 (to L2)

 234    L1:     LOAD_GLOBAL              6 (GENESIS_CHAIN_SENTINEL)

 231    L2:     STORE_FAST               5 (prev)

 238            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (merkle_root_hash)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       53 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (merkle_root_hash)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       31 (to L3)
                NOT_TAKEN

 237            LOAD_FAST_BORROW         1 (merkle_root_hash)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L4)

 239    L3:     LOAD_CONST               1 ('')

 236    L4:     STORE_FAST               6 (merkle)

 241            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (window_start)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_FAST                2 (window_start)
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               1 ('')
        L6:     STORE_FAST               7 (ws)

 242            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (window_end)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN
                LOAD_FAST                3 (window_end)
                JUMP_FORWARD             1 (to L8)
        L7:     LOAD_CONST               1 ('')
        L8:     STORE_FAST               8 (we)

 243            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (brokerage_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L9)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L9)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               1 ('')
       L10:     STORE_FAST               9 (bid)

 244            LOAD_GLOBAL             10 (json)
                LOAD_ATTR               12 (dumps)
                PUSH_NULL

 245            LOAD_CONST               2 ('previous_chain_hash')
                LOAD_FAST_BORROW         5 (prev)

 246            LOAD_CONST               3 ('merkle_root_hash')
                LOAD_FAST_BORROW         6 (merkle)

 247            LOAD_CONST               4 ('window_start')
                LOAD_FAST_BORROW         7 (ws)

 248            LOAD_CONST               5 ('window_end')
                LOAD_FAST_BORROW         8 (we)

 249            LOAD_CONST               6 ('brokerage_id')
                LOAD_FAST_BORROW         9 (bid)

 244            BUILD_MAP                5

 250            LOAD_CONST               7 (True)
                LOAD_CONST              13 ((',', ':'))

 244            LOAD_CONST               8 (('sort_keys', 'separators'))
                CALL_KW                  3
                STORE_FAST              10 (canonical)

 251            NOP

 252   L11:     LOAD_GLOBAL             14 (hashlib)
                LOAD_ATTR               16 (sha256)
                PUSH_NULL
                LOAD_FAST_BORROW        10 (canonical)
                LOAD_ATTR               19 (encode + NULL|self)
                LOAD_CONST               9 ('utf-8')
                CALL                     1
                CALL                     1
                LOAD_ATTR               21 (hexdigest + NULL|self)
                CALL                     0
       L12:     RETURN_VALUE

  --   L13:     PUSH_EXC_INFO

 253            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       90 (to L18)
                NOT_TAKEN
                STORE_FAST              11 (e)

 254   L14:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 255            LOAD_CONST              10 ('compute_audit_window_chain_hash unexpected error type=')

 256            LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 255            BUILD_STRING             2

 254            CALL                     1
                POP_TOP

 258            LOAD_GLOBAL             14 (hashlib)
                LOAD_ATTR               16 (sha256)
                PUSH_NULL
                LOAD_CONST              11 (b'')
                CALL                     1
                LOAD_ATTR               21 (hexdigest + NULL|self)
                CALL                     0
       L15:     SWAP                     2
       L16:     POP_EXCEPT
                LOAD_CONST              12 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RETURN_VALUE

  --   L17:     LOAD_CONST              12 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 253   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L11 to L12 -> L13 [0]
  L13 to L14 -> L19 [1] lasti
  L14 to L15 -> L17 [1] lasti
  L15 to L16 -> L19 [1] lasti
  L17 to L19 -> L19 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app/services/operator/audit_window_chain.py", line 265>:
265           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('db')

266           LOAD_CONST               2 ('Any')

265           LOAD_CONST               3 ('brokerage_id')

268           LOAD_CONST               4 ('Optional[str]')

265           LOAD_CONST               5 ('return')

269           LOAD_CONST               6 ('str')

265           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _read_chain_head_safe at 0x0000018C17D8BF50, file "app/services/operator/audit_window_chain.py", line 265>:
 265            RESUME                   0

 273            NOP

 275    L1:     LOAD_FAST_BORROW         0 (db)
                LOAD_ATTR                1 (table + NULL|self)
                LOAD_GLOBAL              2 (_CHAIN_TABLE)
                CALL                     1

 276            LOAD_ATTR                5 (select + NULL|self)
                LOAD_CONST               1 ('chain_hash, window_end')
                CALL                     1

 277            LOAD_ATTR                7 (order + NULL|self)
                LOAD_CONST               2 ('window_end')
                LOAD_CONST               3 (True)
                LOAD_CONST               4 (('desc',))
                CALL_KW                  2

 278            LOAD_ATTR                9 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 274            STORE_FAST               2 (query)

 284            LOAD_FAST_BORROW         1 (brokerage_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L4)
        L2:     NOT_TAKEN

 285    L3:     LOAD_FAST_BORROW         2 (query)
                LOAD_ATTR               11 (eq + NULL|self)
                LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST_BORROW         1 (brokerage_id)
                CALL                     2
                STORE_FAST               2 (query)

 286    L4:     LOAD_FAST_BORROW         2 (query)
                LOAD_ATTR               13 (execute + NULL|self)
                CALL                     0
                STORE_FAST               3 (result)

 287            LOAD_GLOBAL             15 (list + NULL)
                LOAD_GLOBAL             17 (getattr + NULL)
                LOAD_FAST_BORROW         3 (result)
                LOAD_CONST               6 ('data')
                LOAD_CONST               7 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                BUILD_LIST               0
        L7:     CALL                     1
                STORE_FAST               4 (rows)

 288            LOAD_FAST_BORROW         4 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE         7 (to L11)
        L8:     NOT_TAKEN

 289    L9:     LOAD_GLOBAL             18 (GENESIS_CHAIN_SENTINEL)
       L10:     RETURN_VALUE

 290   L11:     LOAD_FAST_BORROW         4 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_ATTR               21 (get + NULL|self)
                LOAD_CONST               8 ('chain_hash')
                CALL                     1
                STORE_FAST               5 (head)

 291            LOAD_GLOBAL             23 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (head)
                LOAD_GLOBAL             24 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L15)
                NOT_TAKEN
                LOAD_FAST_BORROW         5 (head)
                LOAD_ATTR               27 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L15)
       L12:     NOT_TAKEN

 292   L13:     LOAD_FAST_BORROW         5 (head)
                LOAD_ATTR               27 (strip + NULL|self)
                CALL                     0
       L14:     RETURN_VALUE

 293   L15:     LOAD_GLOBAL             18 (GENESIS_CHAIN_SENTINEL)
       L16:     RETURN_VALUE

  --   L17:     PUSH_EXC_INFO

 294            LOAD_GLOBAL             28 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       60 (to L22)
                NOT_TAKEN
                STORE_FAST               6 (e)

 295   L18:     LOAD_GLOBAL             30 (logger)
                LOAD_ATTR               33 (warning + NULL|self)

 296            LOAD_CONST               9 ('_read_chain_head_safe error type=')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 295            CALL                     1
                POP_TOP

 298            LOAD_GLOBAL             18 (GENESIS_CHAIN_SENTINEL)
       L19:     SWAP                     2
       L20:     POP_EXCEPT
                LOAD_CONST               7 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --   L21:     LOAD_CONST               7 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 294   L22:     RERAISE                  0

  --   L23:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L17 [0]
  L3 to L5 -> L17 [0]
  L6 to L8 -> L17 [0]
  L9 to L10 -> L17 [0]
  L11 to L12 -> L17 [0]
  L13 to L14 -> L17 [0]
  L15 to L16 -> L17 [0]
  L17 to L18 -> L23 [1] lasti
  L18 to L19 -> L21 [1] lasti
  L19 to L20 -> L23 [1] lasti
  L21 to L23 -> L23 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C180C4250, file "app/services/operator/audit_window_chain.py", line 305>:
305           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

307           LOAD_CONST               2 ('Optional[str]')

305           LOAD_CONST               3 ('window_start')

308           LOAD_CONST               4 ('str')

305           LOAD_CONST               5 ('window_end')

309           LOAD_CONST               4 ('str')

305           LOAD_CONST               6 ('merkle_root_id')

310           LOAD_CONST               4 ('str')

305           LOAD_CONST               7 ('merkle_root_hash')

311           LOAD_CONST               4 ('str')

305           LOAD_CONST               8 ('generated_by_actor_type')

312           LOAD_CONST               4 ('str')

305           LOAD_CONST               9 ('generated_by_actor_id')

313           LOAD_CONST               2 ('Optional[str]')

305           LOAD_CONST              10 ('metadata')

314           LOAD_CONST              11 ('Optional[Dict[str, Any]]')

305           LOAD_CONST              12 ('now')

315           LOAD_CONST              13 ('Any')

305           LOAD_CONST              14 ('return')

316           LOAD_CONST              15 ('Dict[str, Any]')

305           BUILD_MAP               10
              RETURN_VALUE

Disassembly of <code object generate_audit_window_chain_entry at 0x0000018C17E94C50, file "app/services/operator/audit_window_chain.py", line 305>:
 305            RESUME                   0

 325            LOAD_FAST_BORROW         5 (generated_by_actor_type)
                LOAD_GLOBAL              0 (ALLOWED_ACTOR_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       14 (to L1)
                NOT_TAKEN

 326            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               2 ('invalid_actor_type')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 327    L1:     LOAD_GLOBAL              5 (_is_sha256_hex + NULL)
                LOAD_FAST_BORROW         4 (merkle_root_hash)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L2)
                NOT_TAKEN

 328            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 329            LOAD_CONST               1 ('failed')
                LOAD_CONST               4 ('invalid_merkle_root_hash_shape')

 328            LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 331    L2:     LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (merkle_root_id)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (merkle_root_id)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L4)
                NOT_TAKEN

 332    L3:     LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               5 ('missing_merkle_root_id')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 333    L4:     LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (window_start)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (window_start)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L6)
                NOT_TAKEN

 334    L5:     LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               6 ('missing_window_start')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 335    L6:     LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (window_end)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L7)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (window_end)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L8)
                NOT_TAKEN

 336    L7:     LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               7 ('missing_window_end')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 337    L8:     LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L9)
                NOT_TAKEN
                LOAD_GLOBAL             13 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               8 (None)
       L10:     STORE_FAST               9 (bid)

 338            LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        18 (to L11)
                NOT_TAKEN
                LOAD_FAST_BORROW         9 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L11)
                NOT_TAKEN

 339            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               9 ('invalid_brokerage_id')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 342   L11:     LOAD_FAST_BORROW         6 (generated_by_actor_id)
                POP_JUMP_IF_NONE        12 (to L12)
                NOT_TAKEN

 341            LOAD_GLOBAL             15 (_bound_actor_id + NULL)
                LOAD_FAST_BORROW         6 (generated_by_actor_id)
                CALL                     1
                JUMP_FORWARD             1 (to L13)

 342   L12:     LOAD_CONST               8 (None)

 340   L13:     STORE_FAST              10 (actor_id)

 344            LOAD_FAST_BORROW         6 (generated_by_actor_id)
                POP_JUMP_IF_NONE        18 (to L14)
                NOT_TAKEN
                LOAD_FAST_BORROW        10 (actor_id)
                POP_JUMP_IF_NOT_NONE    14 (to L14)
                NOT_TAKEN

 345            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST              10 ('invalid_actor_id')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 347   L14:     LOAD_GLOBAL             17 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST              11 (db)

 348            LOAD_FAST_BORROW        11 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L15)
                NOT_TAKEN

 349            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 350            LOAD_CONST              11 ('skipped')

 351            LOAD_CONST              12 ('audit_window_chain_store_unavailable')
                BUILD_LIST               1

 352            LOAD_CONST              12 ('audit_window_chain_store_unavailable')

 349            LOAD_CONST              13 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 355   L15:     LOAD_GLOBAL             19 (_read_chain_head_safe + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 185 (db, bid)
                LOAD_CONST              14 (('brokerage_id',))
                CALL_KW                  2
                STORE_FAST              12 (prev_chain_hash)

 356            LOAD_GLOBAL             21 (compute_audit_window_chain_hash + NULL)

 357            LOAD_FAST_BORROW        12 (prev_chain_hash)

 358            LOAD_FAST_BORROW         4 (merkle_root_hash)

 359            LOAD_FAST_BORROW         1 (window_start)

 360            LOAD_FAST_BORROW         2 (window_end)

 361            LOAD_FAST_BORROW         9 (bid)

 356            LOAD_CONST              15 (('previous_chain_hash', 'merkle_root_hash', 'window_start', 'window_end', 'brokerage_id'))
                CALL_KW                  5
                STORE_FAST              13 (new_chain_hash)

 363            LOAD_GLOBAL             23 (_iso + NULL)
                LOAD_GLOBAL             25 (_now_dt + NULL)
                LOAD_FAST_BORROW         8 (now)
                CALL                     1
                CALL                     1
                STORE_FAST              14 (iso_now)

 365            LOAD_CONST              16 ('chain_window_id')
                LOAD_GLOBAL              9 (str + NULL)
                LOAD_GLOBAL             26 (uuid)
                LOAD_ATTR               28 (uuid4)
                PUSH_NULL
                CALL                     0
                CALL                     1

 366            LOAD_CONST              17 ('brokerage_id')
                LOAD_FAST_BORROW         9 (bid)

 367            LOAD_CONST              18 ('window_start')
                LOAD_FAST_BORROW         1 (window_start)

 368            LOAD_CONST              19 ('window_end')
                LOAD_FAST_BORROW         2 (window_end)

 369            LOAD_CONST              20 ('merkle_root_id')
                LOAD_FAST_BORROW         3 (merkle_root_id)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0

 370            LOAD_CONST              21 ('merkle_root_hash')
                LOAD_FAST_BORROW         4 (merkle_root_hash)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               31 (lower + NULL|self)
                CALL                     0

 371            LOAD_CONST              22 ('previous_chain_hash')
                LOAD_FAST_BORROW        12 (prev_chain_hash)

 372            LOAD_CONST              23 ('chain_hash')
                LOAD_FAST_BORROW        13 (new_chain_hash)

 373            LOAD_CONST              24 ('generated_at')
                LOAD_FAST_BORROW        14 (iso_now)

 374            LOAD_CONST              25 ('generated_by_actor_type')
                LOAD_FAST_BORROW         5 (generated_by_actor_type)

 375            LOAD_CONST              26 ('generated_by_actor_id')
                LOAD_FAST_BORROW        10 (actor_id)

 376            LOAD_CONST              27 ('status')
                LOAD_CONST              28 ('GENERATED')

 377            LOAD_CONST              29 ('metadata')
                LOAD_GLOBAL             33 (_project_metadata + NULL)
                LOAD_FAST_BORROW         7 (metadata)
                CALL                     1

 364            BUILD_MAP               13
                STORE_FAST              15 (row)

 379            NOP

 380   L16:     LOAD_FAST_BORROW        11 (db)
                LOAD_ATTR               35 (table + NULL|self)
                LOAD_GLOBAL             36 (_CHAIN_TABLE)
                CALL                     1
                LOAD_ATTR               39 (insert + NULL|self)
                LOAD_FAST_BORROW        15 (row)
                CALL                     1
                LOAD_ATTR               41 (execute + NULL|self)
                CALL                     0
                STORE_FAST              16 (result)

 381            LOAD_GLOBAL             43 (list + NULL)
                LOAD_GLOBAL             45 (getattr + NULL)
                LOAD_FAST_BORROW        16 (result)
                LOAD_CONST              30 ('data')
                LOAD_CONST               8 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L17)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L17:     CALL                     1
                STORE_FAST              17 (rows)

 382            LOAD_FAST_BORROW        17 (rows)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L20)
       L18:     NOT_TAKEN
       L19:     LOAD_GLOBAL             47 (_project_row + NULL)
                LOAD_FAST_BORROW        17 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                JUMP_FORWARD            10 (to L21)
       L20:     LOAD_GLOBAL             47 (_project_row + NULL)
                LOAD_FAST_BORROW        15 (row)
                CALL                     1
       L21:     STORE_FAST              18 (proj)

 383            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST              31 ('ok')
                LOAD_FAST_BORROW        18 (proj)
                LOAD_CONST              32 (('status', 'entry'))
                CALL_KW                  2
       L22:     RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 384            LOAD_GLOBAL             48 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L28)
                NOT_TAKEN
                STORE_FAST              19 (e)

 385   L24:     LOAD_GLOBAL             50 (logger)
                LOAD_ATTR               53 (warning + NULL|self)

 386            LOAD_CONST              33 ('generate_audit_window_chain_entry db error type=')

 387            LOAD_GLOBAL             55 (type + NULL)
                LOAD_FAST               19 (e)
                CALL                     1
                LOAD_ATTR               56 (__name__)
                FORMAT_SIMPLE

 386            BUILD_STRING             2

 385            CALL                     1
                POP_TOP

 389            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 390            LOAD_CONST              11 ('skipped')

 391            LOAD_CONST              34 ('db_write_failed:')
                LOAD_GLOBAL             55 (type + NULL)
                LOAD_FAST               19 (e)
                CALL                     1
                LOAD_ATTR               56 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 392            LOAD_CONST              12 ('audit_window_chain_store_unavailable')

 389            LOAD_CONST              13 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
       L25:     SWAP                     2
       L26:     POP_EXCEPT
                LOAD_CONST               8 (None)
                STORE_FAST              19 (e)
                DELETE_FAST             19 (e)
                RETURN_VALUE

  --   L27:     LOAD_CONST               8 (None)
                STORE_FAST              19 (e)
                DELETE_FAST             19 (e)
                RERAISE                  1

 384   L28:     RERAISE                  0

  --   L29:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L16 to L18 -> L23 [0]
  L19 to L22 -> L23 [0]
  L23 to L24 -> L29 [1] lasti
  L24 to L25 -> L27 [1] lasti
  L25 to L26 -> L29 [1] lasti
  L27 to L29 -> L29 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app/services/operator/audit_window_chain.py", line 400>:
400           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

402           LOAD_CONST               2 ('Optional[str]')

400           LOAD_CONST               3 ('limit')

403           LOAD_CONST               4 ('Any')

400           LOAD_CONST               5 ('return')

404           LOAD_CONST               6 ('Dict[str, Any]')

400           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object verify_audit_window_chain at 0x0000018C17D51720, file "app/services/operator/audit_window_chain.py", line 400>:
 400            RESUME                   0

 422            LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L1)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST               1 (None)
        L2:     STORE_FAST               2 (bid)

 423            LOAD_GLOBAL              3 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         1 (limit)
                CALL                     1
                STORE_FAST               3 (capped)

 424            LOAD_GLOBAL              5 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               4 (db)

 425            LOAD_FAST_BORROW         4 (db)
                POP_JUMP_IF_NOT_NONE    22 (to L3)
                NOT_TAKEN

 427            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('skipped')

 428            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)

 429            LOAD_CONST               5 ('limit')
                LOAD_FAST_BORROW         3 (capped)

 430            LOAD_CONST               6 ('entries_checked')
                LOAD_SMALL_INT           0

 431            LOAD_CONST               7 ('chain_status')
                LOAD_CONST               8 ('genesis')

 432            LOAD_CONST               9 ('breaks_count')
                LOAD_SMALL_INT           0

 433            LOAD_CONST              10 ('breaks')
                BUILD_LIST               0

 434            LOAD_CONST              11 ('warnings')
                LOAD_CONST              12 ('audit_window_chain_store_unavailable')
                BUILD_LIST               1

 435            LOAD_CONST              13 ('error_code')
                LOAD_CONST              12 ('audit_window_chain_store_unavailable')

 426            BUILD_MAP                9
                RETURN_VALUE

 437    L3:     NOP

 439    L4:     LOAD_FAST_BORROW         4 (db)
                LOAD_ATTR                7 (table + NULL|self)
                LOAD_GLOBAL              8 (_CHAIN_TABLE)
                CALL                     1

 440            LOAD_ATTR               11 (select + NULL|self)
                LOAD_CONST              14 (',')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_GLOBAL             14 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 441            LOAD_ATTR               17 (order + NULL|self)
                LOAD_CONST              15 ('window_start')
                LOAD_CONST              16 (False)
                LOAD_CONST              17 (('desc',))
                CALL_KW                  2

 442            LOAD_ATTR               19 (limit + NULL|self)
                LOAD_FAST_BORROW         3 (capped)
                CALL                     1

 438            STORE_FAST               5 (query)

 444            LOAD_FAST_BORROW         2 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L7)
        L5:     NOT_TAKEN

 445    L6:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)
                CALL                     2
                STORE_FAST               5 (query)

 446    L7:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               23 (execute + NULL|self)
                CALL                     0
                STORE_FAST               6 (result)

 447            LOAD_GLOBAL             25 (list + NULL)
                LOAD_GLOBAL             27 (getattr + NULL)
                LOAD_FAST_BORROW         6 (result)
                LOAD_CONST              18 ('data')
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

 464   L11:     LOAD_FAST                7 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        21 (to L12)
                NOT_TAKEN

 466            LOAD_CONST               2 ('status')
                LOAD_CONST              21 ('ok')

 467            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                2 (bid)

 468            LOAD_CONST               5 ('limit')
                LOAD_FAST                3 (capped)

 469            LOAD_CONST               6 ('entries_checked')
                LOAD_SMALL_INT           0

 470            LOAD_CONST               7 ('chain_status')
                LOAD_CONST               8 ('genesis')

 471            LOAD_CONST               9 ('breaks_count')
                LOAD_SMALL_INT           0

 472            LOAD_CONST              10 ('breaks')
                BUILD_LIST               0

 473            LOAD_CONST              11 ('warnings')
                BUILD_LIST               0

 474            LOAD_CONST              13 ('error_code')
                LOAD_CONST               1 (None)

 465            BUILD_MAP                9
                RETURN_VALUE

 477   L12:     BUILD_LIST               0
                STORE_FAST               9 (breaks)

 478            LOAD_GLOBAL             38 (GENESIS_CHAIN_SENTINEL)
                STORE_FAST              10 (expected_prev)

 479            LOAD_FAST                7 (rows)
                GET_ITER
       L13:     EXTENDED_ARG             1
                FOR_ITER               404 (to L23)
                STORE_FAST              11 (r)

 480            LOAD_GLOBAL             41 (isinstance + NULL)
                LOAD_FAST               11 (r)
                LOAD_GLOBAL             42 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN

 481            JUMP_BACKWARD           28 (to L13)

 482   L14:     LOAD_FAST               11 (r)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST              22 ('chain_window_id')
                CALL                     1
                STORE_FAST              12 (cw_id)

 483            LOAD_FAST               11 (r)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST              15 ('window_start')
                CALL                     1
                STORE_FAST              13 (window_start)

 484            LOAD_FAST               11 (r)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST              23 ('previous_chain_hash')
                CALL                     1
                STORE_FAST              14 (stored_prev)

 485            LOAD_FAST               11 (r)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST              24 ('chain_hash')
                CALL                     1
                STORE_FAST              15 (stored_chain)

 486            LOAD_FAST               11 (r)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST              25 ('merkle_root_hash')
                CALL                     1
                STORE_FAST              16 (merkle_hash)

 487            LOAD_FAST               11 (r)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST               4 ('brokerage_id')
                CALL                     1
                STORE_FAST              17 (row_brokerage)

 488            LOAD_GLOBAL             47 (compute_audit_window_chain_hash + NULL)

 489            LOAD_FAST               10 (expected_prev)

 490            LOAD_FAST               16 (merkle_hash)

 491            LOAD_FAST               13 (window_start)

 492            LOAD_FAST               11 (r)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST              26 ('window_end')
                CALL                     1

 493            LOAD_FAST               17 (row_brokerage)

 488            LOAD_CONST              27 (('previous_chain_hash', 'merkle_root_hash', 'window_start', 'window_end', 'brokerage_id'))
                CALL_KW                  5
                STORE_FAST              18 (recomputed)

 496            LOAD_GLOBAL             41 (isinstance + NULL)
                LOAD_FAST               14 (stored_prev)
                LOAD_GLOBAL             48 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L15)
                NOT_TAKEN
                LOAD_FAST               14 (stored_prev)
                LOAD_ATTR               51 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L16)
                NOT_TAKEN

 497   L15:     LOAD_FAST                9 (breaks)
                LOAD_ATTR               53 (append + NULL|self)

 498            LOAD_CONST              22 ('chain_window_id')
                LOAD_FAST               12 (cw_id)

 499            LOAD_CONST              15 ('window_start')
                LOAD_FAST               13 (window_start)

 500            LOAD_CONST              28 ('break_type')
                LOAD_CONST              29 ('missing_previous_chain_hash')

 497            BUILD_MAP                3
                CALL                     1
                POP_TOP
                JUMP_FORWARD            29 (to L17)

 502   L16:     LOAD_FAST_LOAD_FAST    234 (stored_prev, expected_prev)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       24 (to L17)
                NOT_TAKEN

 509            LOAD_FAST                9 (breaks)
                LOAD_ATTR               53 (append + NULL|self)

 510            LOAD_CONST              22 ('chain_window_id')
                LOAD_FAST               12 (cw_id)

 511            LOAD_CONST              15 ('window_start')
                LOAD_FAST               13 (window_start)

 512            LOAD_CONST              28 ('break_type')
                LOAD_CONST              30 ('previous_chain_hash_mismatch')

 509            BUILD_MAP                3
                CALL                     1
                POP_TOP

 515   L17:     LOAD_GLOBAL             41 (isinstance + NULL)
                LOAD_FAST               15 (stored_chain)
                LOAD_GLOBAL             48 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L18)
                NOT_TAKEN
                LOAD_FAST               15 (stored_chain)
                LOAD_ATTR               51 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L19)
                NOT_TAKEN

 516   L18:     LOAD_FAST                9 (breaks)
                LOAD_ATTR               53 (append + NULL|self)

 517            LOAD_CONST              22 ('chain_window_id')
                LOAD_FAST               12 (cw_id)

 518            LOAD_CONST              15 ('window_start')
                LOAD_FAST               13 (window_start)

 519            LOAD_CONST              28 ('break_type')
                LOAD_CONST              31 ('missing_chain_hash')

 516            BUILD_MAP                3
                CALL                     1
                POP_TOP
                JUMP_FORWARD            30 (to L20)

 521   L19:     LOAD_FAST               15 (stored_chain)
                LOAD_FAST               18 (recomputed)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       24 (to L20)
                NOT_TAKEN

 522            LOAD_FAST                9 (breaks)
                LOAD_ATTR               53 (append + NULL|self)

 523            LOAD_CONST              22 ('chain_window_id')
                LOAD_FAST               12 (cw_id)

 524            LOAD_CONST              15 ('window_start')
                LOAD_FAST               13 (window_start)

 525            LOAD_CONST              28 ('break_type')
                LOAD_CONST              32 ('chain_hash_mismatch')

 522            BUILD_MAP                3
                CALL                     1
                POP_TOP

 530   L20:     LOAD_GLOBAL             41 (isinstance + NULL)
                LOAD_FAST               15 (stored_chain)
                LOAD_GLOBAL             48 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L21)
                NOT_TAKEN
                LOAD_FAST               15 (stored_chain)
                LOAD_ATTR               51 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L21)
                NOT_TAKEN
                LOAD_FAST               15 (stored_chain)
                JUMP_FORWARD             1 (to L22)

 531   L21:     LOAD_FAST               18 (recomputed)

 529   L22:     STORE_FAST              10 (expected_prev)
                EXTENDED_ARG             1
                JUMP_BACKWARD          407 (to L13)

 479   L23:     END_FOR
                POP_ITER

 534            LOAD_FAST                9 (breaks)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L24)
                NOT_TAKEN
                LOAD_CONST              21 ('ok')
                JUMP_FORWARD             1 (to L25)
       L24:     LOAD_CONST              33 ('degraded')
       L25:     STORE_FAST              19 (chain_status)

 536            LOAD_CONST               2 ('status')
                LOAD_CONST              21 ('ok')

 537            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                2 (bid)

 538            LOAD_CONST               5 ('limit')
                LOAD_FAST                3 (capped)

 539            LOAD_CONST               6 ('entries_checked')
                LOAD_GLOBAL             55 (len + NULL)
                LOAD_FAST                7 (rows)
                CALL                     1

 540            LOAD_CONST               7 ('chain_status')
                LOAD_FAST               19 (chain_status)

 541            LOAD_CONST               9 ('breaks_count')
                LOAD_GLOBAL             55 (len + NULL)
                LOAD_FAST                9 (breaks)
                CALL                     1

 542            LOAD_CONST              10 ('breaks')
                LOAD_FAST                9 (breaks)

 543            LOAD_CONST              11 ('warnings')
                BUILD_LIST               0

 544            LOAD_CONST              13 ('error_code')
                LOAD_CONST               1 (None)

 535            BUILD_MAP                9
                RETURN_VALUE

  --   L26:     PUSH_EXC_INFO

 448            LOAD_GLOBAL             28 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L31)
                NOT_TAKEN
                STORE_FAST               8 (e)

 449   L27:     LOAD_GLOBAL             30 (logger)
                LOAD_ATTR               33 (warning + NULL|self)

 450            LOAD_CONST              19 ('verify_audit_window_chain read error type=')

 451            LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE

 450            BUILD_STRING             2

 449            CALL                     1
                POP_TOP

 454            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('skipped')

 455            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                2 (bid)

 456            LOAD_CONST               5 ('limit')
                LOAD_FAST                3 (capped)

 457            LOAD_CONST               6 ('entries_checked')
                LOAD_SMALL_INT           0

 458            LOAD_CONST               7 ('chain_status')
                LOAD_CONST               8 ('genesis')

 459            LOAD_CONST               9 ('breaks_count')
                LOAD_SMALL_INT           0

 460            LOAD_CONST              10 ('breaks')
                BUILD_LIST               0

 461            LOAD_CONST              11 ('warnings')
                LOAD_CONST              20 ('db_read_failed:')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 462            LOAD_CONST              13 ('error_code')
                LOAD_CONST              12 ('audit_window_chain_store_unavailable')

 453            BUILD_MAP                9
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

 448   L31:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app/services/operator/audit_window_chain.py", line 552>:
552           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

554           LOAD_CONST               2 ('Optional[str]')

552           LOAD_CONST               3 ('limit')

555           LOAD_CONST               4 ('Any')

552           LOAD_CONST               5 ('return')

556           LOAD_CONST               6 ('Dict[str, Any]')

552           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object chain_status_report at 0x0000018C17D51E80, file "app/services/operator/audit_window_chain.py", line 552>:
 552            RESUME                   0

 560            LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L1)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST               1 (None)
        L2:     STORE_FAST               2 (bid)

 561            LOAD_GLOBAL              3 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         1 (limit)
                CALL                     1
                STORE_FAST               3 (capped)

 562            LOAD_GLOBAL              5 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               4 (db)

 563            LOAD_FAST_BORROW         4 (db)
                POP_JUMP_IF_NOT_NONE    20 (to L3)
                NOT_TAKEN

 565            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('skipped')

 566            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)

 567            LOAD_CONST               5 ('limit')
                LOAD_FAST_BORROW         3 (capped)

 568            LOAD_CONST               6 ('total')
                LOAD_SMALL_INT           0

 569            LOAD_CONST               7 ('by_status')
                BUILD_MAP                0

 570            LOAD_CONST               8 ('latest_entry')
                LOAD_CONST               1 (None)

 571            LOAD_CONST               9 ('warnings')
                LOAD_CONST              10 ('audit_window_chain_store_unavailable')
                BUILD_LIST               1

 572            LOAD_CONST              11 ('error_code')
                LOAD_CONST              10 ('audit_window_chain_store_unavailable')

 564            BUILD_MAP                8
                RETURN_VALUE

 574    L3:     NOP

 576    L4:     LOAD_FAST_BORROW         4 (db)
                LOAD_ATTR                7 (table + NULL|self)
                LOAD_GLOBAL              8 (_CHAIN_TABLE)
                CALL                     1

 577            LOAD_ATTR               11 (select + NULL|self)
                LOAD_CONST              12 (',')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_GLOBAL             14 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 578            LOAD_ATTR               17 (order + NULL|self)
                LOAD_CONST              13 ('window_start')
                LOAD_CONST              14 (True)
                LOAD_CONST              15 (('desc',))
                CALL_KW                  2

 579            LOAD_ATTR               19 (limit + NULL|self)
                LOAD_FAST_BORROW         3 (capped)
                CALL                     1

 575            STORE_FAST               5 (query)

 581            LOAD_FAST_BORROW         2 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L7)
        L5:     NOT_TAKEN

 582    L6:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)
                CALL                     2
                STORE_FAST               5 (query)

 583    L7:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               23 (execute + NULL|self)
                CALL                     0
                STORE_FAST               6 (result)

 584            LOAD_GLOBAL             25 (list + NULL)
                LOAD_GLOBAL             27 (getattr + NULL)
                LOAD_FAST_BORROW         6 (result)
                LOAD_CONST              16 ('data')
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

 599   L11:     BUILD_MAP                0
                STORE_FAST               9 (by_status)

 600            LOAD_FAST                7 (rows)
                GET_ITER
       L12:     FOR_ITER               108 (to L16)
                STORE_FAST              10 (r)

 601            LOAD_GLOBAL             39 (isinstance + NULL)
                LOAD_FAST               10 (r)
                LOAD_GLOBAL             40 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN

 602            JUMP_BACKWARD           27 (to L12)

 603   L13:     LOAD_FAST               10 (r)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                STORE_FAST              11 (s)

 604            LOAD_GLOBAL             39 (isinstance + NULL)
                LOAD_FAST               11 (s)
                LOAD_GLOBAL             44 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           68 (to L12)
       L14:     LOAD_FAST               11 (s)
                LOAD_GLOBAL             46 (ALLOWED_CHAIN_STATUSES)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN
                JUMP_BACKWARD           81 (to L12)

 605   L15:     LOAD_FAST                9 (by_status)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_FAST               11 (s)
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST_LOAD_FAST    155 (by_status, s)
                STORE_SUBSCR
                JUMP_BACKWARD          110 (to L12)

 600   L16:     END_FOR
                POP_ITER

 606            LOAD_FAST                7 (rows)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL             49 (_project_row + NULL)
                LOAD_FAST                7 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                JUMP_FORWARD             1 (to L18)
       L17:     LOAD_CONST               1 (None)
       L18:     STORE_FAST              12 (latest)

 608            LOAD_CONST               2 ('status')
                LOAD_CONST              19 ('ok')

 609            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                2 (bid)

 610            LOAD_CONST               5 ('limit')
                LOAD_FAST                3 (capped)

 611            LOAD_CONST               6 ('total')
                LOAD_GLOBAL             51 (len + NULL)
                LOAD_FAST                7 (rows)
                CALL                     1

 612            LOAD_CONST               7 ('by_status')
                LOAD_FAST                9 (by_status)

 613            LOAD_CONST               8 ('latest_entry')
                LOAD_FAST               12 (latest)

 614            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 615            LOAD_CONST              11 ('error_code')
                LOAD_CONST               1 (None)

 607            BUILD_MAP                8
                RETURN_VALUE

  --   L19:     PUSH_EXC_INFO

 585            LOAD_GLOBAL             28 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       95 (to L24)
                NOT_TAKEN
                STORE_FAST               8 (e)

 586   L20:     LOAD_GLOBAL             30 (logger)
                LOAD_ATTR               33 (warning + NULL|self)

 587            LOAD_CONST              17 ('chain_status_report read error type=')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 586            CALL                     1
                POP_TOP

 590            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('skipped')

 591            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                2 (bid)

 592            LOAD_CONST               5 ('limit')
                LOAD_FAST                3 (capped)

 593            LOAD_CONST               6 ('total')
                LOAD_SMALL_INT           0

 594            LOAD_CONST               7 ('by_status')
                BUILD_MAP                0

 595            LOAD_CONST               8 ('latest_entry')
                LOAD_CONST               1 (None)

 596            LOAD_CONST               9 ('warnings')
                LOAD_CONST              18 ('db_read_failed:')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 597            LOAD_CONST              11 ('error_code')
                LOAD_CONST              10 ('audit_window_chain_store_unavailable')

 589            BUILD_MAP                8
       L21:     SWAP                     2
       L22:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RETURN_VALUE

  --   L23:     LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 585   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L19 [0]
  L6 to L8 -> L19 [0]
  L9 to L11 -> L19 [0]
  L19 to L20 -> L25 [1] lasti
  L20 to L21 -> L23 [1] lasti
  L21 to L22 -> L25 [1] lasti
  L23 to L25 -> L25 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "app/services/operator/audit_window_chain.py", line 619>:
619           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object brokerage_chain_badge at 0x0000018C17D7C8F0, file "app/services/operator/audit_window_chain.py", line 619>:
619            RESUME                   0

622            LOAD_FAST_BORROW         0 (brokerage_id)
               POP_JUMP_IF_NONE        12 (to L1)
               NOT_TAKEN
               LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
               LOAD_FAST_BORROW         0 (brokerage_id)
               CALL                     1
               JUMP_FORWARD             1 (to L2)
       L1:     LOAD_CONST               1 (None)
       L2:     STORE_FAST               1 (bid)

623            LOAD_FAST_BORROW         1 (bid)
               POP_JUMP_IF_NOT_NONE    17 (to L3)
               NOT_TAKEN

625            LOAD_CONST               2 ('status')
               LOAD_CONST               3 ('failed')

626            LOAD_CONST               4 ('brokerage_id')
               LOAD_CONST               1 (None)

627            LOAD_CONST               5 ('chain_status')
               LOAD_CONST               6 ('unknown')

628            LOAD_CONST               7 ('entries_total')
               LOAD_SMALL_INT           0

629            LOAD_CONST               8 ('latest_window_end')
               LOAD_CONST               1 (None)

630            LOAD_CONST               9 ('error_code')
               LOAD_CONST              10 ('missing_brokerage_id')

631            LOAD_CONST              11 ('warnings')
               BUILD_LIST               0

624            BUILD_MAP                7
               RETURN_VALUE

633    L3:     LOAD_GLOBAL              3 (chain_status_report + NULL)
               LOAD_FAST_BORROW         1 (bid)
               LOAD_SMALL_INT         200
               LOAD_CONST              12 (('brokerage_id', 'limit'))
               CALL_KW                  2
               STORE_FAST               2 (report)

634            LOAD_FAST_BORROW         2 (report)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               2 ('status')
               CALL                     1
               LOAD_CONST              13 ('ok')
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE       91 (to L6)
               NOT_TAKEN

636            LOAD_CONST               2 ('status')
               LOAD_FAST_BORROW         2 (report)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               2 ('status')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              14 ('skipped')

637    L4:     LOAD_CONST               4 ('brokerage_id')
               LOAD_FAST                1 (bid)

638            LOAD_CONST               5 ('chain_status')
               LOAD_CONST               6 ('unknown')

639            LOAD_CONST               7 ('entries_total')
               LOAD_SMALL_INT           0

640            LOAD_CONST               8 ('latest_window_end')
               LOAD_CONST               1 (None)

641            LOAD_CONST               9 ('error_code')
               LOAD_FAST_BORROW         2 (report)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               9 ('error_code')
               CALL                     1

642            LOAD_CONST              11 ('warnings')
               LOAD_GLOBAL              7 (list + NULL)
               LOAD_FAST_BORROW         2 (report)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              11 ('warnings')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L5:     CALL                     1

635            BUILD_MAP                7
               RETURN_VALUE

644    L6:     LOAD_FAST_BORROW         2 (report)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              15 ('by_status')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L7)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
       L7:     STORE_FAST               3 (by_status)

645            LOAD_GLOBAL              9 (int + NULL)
               LOAD_FAST_BORROW         2 (report)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              16 ('total')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               POP_TOP
               LOAD_SMALL_INT           0
       L8:     CALL                     1
               STORE_FAST               4 (total)

646            LOAD_FAST_BORROW         4 (total)
               LOAD_SMALL_INT           0
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        4 (to L9)
               NOT_TAKEN

647            LOAD_CONST              17 ('none')
               STORE_FAST               5 (chain_status)
               JUMP_FORWARD           139 (to L13)

648    L9:     LOAD_GLOBAL              9 (int + NULL)
               LOAD_FAST_BORROW         3 (by_status)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              18 ('BROKEN')
               LOAD_SMALL_INT           0
               CALL                     2
               CALL                     1
               LOAD_SMALL_INT           0
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        4 (to L10)
               NOT_TAKEN

649            LOAD_CONST              19 ('broken')
               STORE_FAST               5 (chain_status)
               JUMP_FORWARD           104 (to L13)

650   L10:     LOAD_GLOBAL              9 (int + NULL)
               LOAD_FAST_BORROW         3 (by_status)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              20 ('VERIFIED')
               LOAD_SMALL_INT           0
               CALL                     2
               CALL                     1
               LOAD_SMALL_INT           0
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE       36 (to L11)
               NOT_TAKEN
               LOAD_GLOBAL              9 (int + NULL)
               LOAD_FAST_BORROW         3 (by_status)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              21 ('GENERATED')
               LOAD_SMALL_INT           0
               CALL                     2
               CALL                     1
               LOAD_SMALL_INT           0
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        4 (to L11)
               NOT_TAKEN

651            LOAD_CONST              22 ('verified')
               STORE_FAST               5 (chain_status)
               JUMP_FORWARD            37 (to L13)

652   L11:     LOAD_GLOBAL              9 (int + NULL)
               LOAD_FAST_BORROW         3 (by_status)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              20 ('VERIFIED')
               LOAD_SMALL_INT           0
               CALL                     2
               CALL                     1
               LOAD_SMALL_INT           0
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        4 (to L12)
               NOT_TAKEN

653            LOAD_CONST              23 ('mixed')
               STORE_FAST               5 (chain_status)
               JUMP_FORWARD             2 (to L13)

655   L12:     LOAD_CONST              24 ('generated')
               STORE_FAST               5 (chain_status)

656   L13:     LOAD_FAST_BORROW         2 (report)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              25 ('latest_entry')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L14)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
      L14:     STORE_FAST               6 (latest)

658            LOAD_CONST               2 ('status')
               LOAD_CONST              13 ('ok')

659            LOAD_CONST               4 ('brokerage_id')
               LOAD_FAST_BORROW         1 (bid)

660            LOAD_CONST               5 ('chain_status')
               LOAD_FAST_BORROW         5 (chain_status)

661            LOAD_CONST               7 ('entries_total')
               LOAD_FAST_BORROW         4 (total)

662            LOAD_CONST               8 ('latest_window_end')
               LOAD_FAST_BORROW         6 (latest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              26 ('window_end')
               CALL                     1

663            LOAD_CONST               9 ('error_code')
               LOAD_CONST               1 (None)

664            LOAD_CONST              11 ('warnings')
               BUILD_LIST               0

657            BUILD_MAP                7
               RETURN_VALUE
```
