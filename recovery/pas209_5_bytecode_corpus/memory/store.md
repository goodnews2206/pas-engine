# memory/store

- **pyc:** `app\services\memory\__pycache__\store.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/store.py`
- **co_filename (from bytecode):** `app\services\memory\store.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144B — Tenant-isolated memory store.

The first storage layer for PAS Brain operational memory. Persists
governed `MemoryRecord` instances into the `pas_memory_records` table
created by ``scripts/migrate_v10_memory_store.sql``.

Hard contract — every public function in this module:
  1. Calls ``apply_memory_governance(record)`` BEFORE persistence.
  2. Calls ``should_persist_memory(governed)`` and returns ``None`` when
     the gate refuses (low confidence, dangerous, missing lineage,
     transcript leak, etc.).
  3. Rejects records without a ``brokerage_id`` (tenant isolation is
     mandatory at the application layer; the migration mirrors this
     with ``brokerage_id NOT NULL`` plus RLS).
  4. Refuses any record whose evidence/metadata carries a forbidden
     raw-transcript key (PAS Brain never persists raw text).
  5. Never logs raw evidence/metadata values — only structural facts
     (memory_id, brokerage_id, kind, status).
  6. Fails safely when Supabase is unavailable: returns ``None`` and
     logs a warning. Never raises into the caller.

Public surface (deliberately tiny — retrieval is *not* in this phase):
  - prepare_memory_for_insert(record)            -> dict
  - insert_memory(record)                        -> dict | None
  - upsert_memory(record)                        -> dict | None
  - quarantine_memory(record_or_id, reason)      -> dict | None
  - expire_memory(record_or_id, reason)          -> dict | None

PAS144B explicitly does NOT build:
  - retrieval / similarity search
  - vector / embedding columns
  - autonomous learning
  - dashboard or PAS Brain UI changes
  - external vendors
```

## Imports

`Any`, `Dict`, `MemoryKind`, `MemoryRecord`, `MemoryStatus`, `Optional`, `Union`, `__future__`, `annotations`, `app.db.supabase_client`, `apply_memory_governance`, `contracts`, `dataclasses`, `datetime`, `get_supabase`, `governance`, `has_forbidden_transcript_field`, `logging`, `should_persist_memory`, `should_quarantine_memory`, `timezone`, `typing`, `validate_memory_record`

## Classes

_none_

## Functions / methods

`__annotate__`, `_execute_insert`, `_execute_status_update`, `_execute_upsert`, `_get_db`, `_govern_or_drop`, `_safe_log_decision`, `expire_memory`, `insert_memory`, `prepare_memory_for_insert`, `quarantine_memory`, `upsert_memory`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS144B — Tenant-isolated memory store.\n\nThe first storage layer for PAS Brain operational memory. Persists\ngoverned `MemoryRecord` instances into the `pas_memory_records` table\ncreated by ``scripts/migrate_v10_memory_store.sql``.\n\nHard contract — every public function in this module:\n  1. Calls ``apply_memory_governance(record)`` BEFORE persistence.\n  2. Calls ``should_persist_memory(governed)`` and returns ``None`` when\n     the gate refuses (low confidence, dangerous, missing lineage,\n     transcript leak, etc.).\n  3. Rejects records without a ``brokerage_id`` (tenant isolation is\n     mandatory at the application layer; the migration mirrors this\n     with ``brokerage_id NOT NULL`` plus RLS).\n  4. Refuses any record whose evidence/metadata carries a forbidden\n     raw-transcript key (PAS Brain never persists raw text).\n  5. Never logs raw evidence/metadata values — only structural facts\n     (memory_id, brokerage_id, kind, status).\n  6. Fails safely when Supabase is unavailable: returns ``None`` and\n     logs a warning. Never raises into the caller.\n\nPublic surface (deliberately tiny — retrieval is *not* in this phase):\n  - prepare_memory_for_insert(record)            -> dict\n  - insert_memory(record)                        -> dict | None\n  - upsert_memory(record)                        -> dict | None\n  - quarantine_memory(record_or_id, reason)      -> dict | None\n  - expire_memory(record_or_id, reason)          -> dict | None\n\nPAS144B explicitly does NOT build:\n  - retrieval / similarity search\n  - vector / embedding columns\n  - autonomous learning\n  - dashboard or PAS Brain UI changes\n  - external vendors\n'
- 'pas.memory.store'
- 'pas_memory_records'
- 'extra'
- 'brokerage_id'
- 'record'
- 'MemoryRecord'
- 'return'
- 'dict'
- 'Convert a `MemoryRecord` into a row dict for ``pas_memory_records``.\n\nPure function: no I/O, no governance side-effects. The caller is\nresponsible for governance gating — this helper exists so that\n`insert_memory`/`upsert_memory`/quarantine/expire can share one\nserialization path that mirrors the migration column order.\n\nRaises:\n    TypeError  — when *record* is not a `MemoryRecord`.\n    ValueError — when *record* carries a forbidden raw-transcript\n                 key in evidence or metadata, or has no\n                 brokerage_id. The store never serializes such a\n                 record.\n'
- 'prepare_memory_for_insert requires a MemoryRecord'
- 'brokerage_id is required (tenant isolation)'
- 'evidence/metadata contains a forbidden raw-transcript field; memory will not be serialized'
- 'memory_id'
- 'kind'
- 'source'
- 'status'
- 'title'
- 'summary'
- 'evidence'
- 'confidence'
- 'outcome_weight'
- 'ttl_days'
- 'created_at'
- 'expires_at'
- 'lineage'
- 'metadata'
- 'Resolve the Supabase client lazily so unit tests can patch\n`app.db.supabase_client.get_supabase` without forcing a module-load\nside effect.'
- 'str'
- 'decision'
- 'Optional[Dict[str, Any]]'
- 'None'
- 'Structured, non-sensitive log line. Never echoes evidence /\nmetadata / title / summary.'
- ' | '
- 'Optional[MemoryRecord]'
- 'Run governance and return the corrected record only if the gate\npermits persistence. Returns None on any reject path (and logs\n*why*, structurally, never the values).'
- ' dropped | reason=not_a_memory_record'
- ' dropped | reason=missing_brokerage_id'
- 'dropped'
- 'reason'
- 'forbidden_transcript_field'
- 'governance_validation_failed'
- 'error_count'
- 'should_persist_false'
- 'row'
- 'Optional[dict]'
- 'Insert a single row. Fail-safe: returns None on any Supabase\nerror. Never raises into the caller.'
- ' failed (non-critical) | memory_id='
- ' | error_type='
- 'Upsert a single row by ``memory_id`` (the primary key). Fail-safe.'
- 'new_status'
- 'MemoryStatus'
- "Patch a single row's status (and a metadata.audit entry) by\n``memory_id``. Tenant-scoped via ``brokerage_id`` to make\ncross-tenant patches impossible at the query layer too. Fail-safe."
- 'audit'
- 'data'
- 'Persist a new memory record. Governance-gated.\n\nReturns the row dict on success, ``None`` when the record is not\npersistable (validation failure, low confidence, dangerous, missing\nlineage, transcript leak, missing brokerage_id) or when Supabase\nis unavailable.\n\nDANGEROUS records cannot reach the database through this path —\nthey are routed by ``apply_memory_governance`` to QUARANTINED, and\n``should_persist_memory`` then refuses them. The only legal entry\npoint for a DANGEROUS record is ``quarantine_memory``.\n'
- 'insert_memory'
- 'prepare_failed'
- 'error_type'
- 'Insert-or-update a memory record by ``memory_id``. Governance-\ngated identically to ``insert_memory``.\n\nSame DANGEROUS-record rule as ``insert_memory`` — promotion into\nQUARANTINED only flows through ``quarantine_memory``.\n'
- 'upsert_memory'
- 'record_or_id'
- 'Union[MemoryRecord, str]'
- 'Optional[str]'
- 'Move a record into the QUARANTINED state.\n\nTwo call shapes:\n  * ``quarantine_memory(record, reason)`` — for a *fresh* record\n    that should be inserted directly as QUARANTINED. This is the\n    only legal entry point for DANGEROUS-kind records, which the\n    normal insert path refuses. The record is forced through\n    governance (which already pins DANGEROUS → QUARANTINED) and\n    inserted with status QUARANTINED.\n  * ``quarantine_memory(memory_id, reason, brokerage_id=...)`` — for\n    a record that already exists in the table. Performs a tenant-\n    scoped UPDATE setting status to QUARANTINED and writing a small\n    audit entry into metadata.\n\nReturns the row dict on success, ``None`` on any drop / failure.\n'
- 'quarantine_memory dropped | reason=missing_brokerage_id'
- 'quarantine_memory'
- 'quarantine_memory dropped | reason=invalid_memory_id'
- 'quarantine_memory dropped | memory_id='
- ' | reason=missing_brokerage_id'
- 'Move a record into the EXPIRED state.\n\nTwo call shapes — same as ``quarantine_memory``. Tenant-scoped.\nNever deletes the row; EXPIRED is a soft-removal marker so audit\nhistory is preserved.\n'
- 'expire_memory dropped | reason=missing_brokerage_id'
- 'expire_memory'
- 'expire_memory dropped | reason=invalid_memory_id'
- 'expire_memory dropped | memory_id='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS144B — Tenant-isolated memory store.\n\nThe first storage layer for PAS Brain operational memory. Persists\ngoverned `MemoryRecord` instances into the `pas_memory_records` table\ncreated by ``scripts/migrate_v10_memory_store.sql``.\n\nHard contract — every public function in this module:\n  1. Calls ``apply_memory_governance(record)`` BEFORE persistence.\n  2. Calls ``should_persist_memory(governed)`` and returns ``None`` when\n     the gate refuses (low confidence, dangerous, missing lineage,\n     transcript leak, etc.).\n  3. Rejects records without a ``brokerage_id`` (tenant isolation is\n     mandatory at the application layer; the migration mirrors this\n     with ``brokerage_id NOT NULL`` plus RLS).\n  4. Refuses any record whose evidence/metadata carries a forbidden\n     raw-transcript key (PAS Brain never persists raw text).\n  5. Never logs raw evidence/metadata values — only structural facts\n     (memory_id, brokerage_id, kind, status).\n  6. Fails safely when Supabase is unavailable: returns ``None`` and\n     logs a warning. Never raises into the caller.\n\nPublic surface (deliberately tiny — retrieval is *not* in this phase):\n  - prepare_memory_for_insert(record)            -> dict\n  - insert_memory(record)                        -> dict | None\n  - upsert_memory(record)                        -> dict | None\n  - quarantine_memory(record_or_id, reason)      -> dict | None\n  - expire_memory(record_or_id, reason)          -> dict | None\n\nPAS144B explicitly does NOT build:\n  - retrieval / similarity search\n  - vector / embedding columns\n  - autonomous learning\n  - dashboard or PAS Brain UI changes\n  - external vendors\n')
              STORE_NAME               0 (__doc__)

 38           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 40           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (dataclasses)
              STORE_NAME               3 (dataclasses)

 41           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (logging)
              STORE_NAME               4 (logging)

 42           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timezone'))
              IMPORT_NAME              5 (datetime)
              IMPORT_FROM              5 (datetime)
              STORE_NAME               5 (datetime)
              IMPORT_FROM              6 (timezone)
              STORE_NAME               6 (timezone)
              POP_TOP

 43           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'Optional', 'Union'))
              IMPORT_NAME              7 (typing)
              IMPORT_FROM              8 (Any)
              STORE_NAME               8 (Any)
              IMPORT_FROM              9 (Dict)
              STORE_NAME               9 (Dict)
              IMPORT_FROM             10 (Optional)
              STORE_NAME              10 (Optional)
              IMPORT_FROM             11 (Union)
              STORE_NAME              11 (Union)
              POP_TOP

 45           LOAD_SMALL_INT           1
              LOAD_CONST               5 (('MemoryKind', 'MemoryRecord', 'MemoryStatus', 'has_forbidden_transcript_field'))
              IMPORT_NAME             12 (contracts)
              IMPORT_FROM             13 (MemoryKind)
              STORE_NAME              13 (MemoryKind)
              IMPORT_FROM             14 (MemoryRecord)
              STORE_NAME              14 (MemoryRecord)
              IMPORT_FROM             15 (MemoryStatus)
              STORE_NAME              15 (MemoryStatus)
              IMPORT_FROM             16 (has_forbidden_transcript_field)
              STORE_NAME              16 (has_forbidden_transcript_field)
              POP_TOP

 51           LOAD_SMALL_INT           1
              LOAD_CONST               6 (('apply_memory_governance', 'should_persist_memory', 'should_quarantine_memory', 'validate_memory_record'))
              IMPORT_NAME             17 (governance)
              IMPORT_FROM             18 (apply_memory_governance)
              STORE_NAME              18 (apply_memory_governance)
              IMPORT_FROM             19 (should_persist_memory)
              STORE_NAME              19 (should_persist_memory)
              IMPORT_FROM             20 (should_quarantine_memory)
              STORE_NAME              20 (should_quarantine_memory)
              IMPORT_FROM             21 (validate_memory_record)
              STORE_NAME              21 (validate_memory_record)
              POP_TOP

 58           LOAD_NAME                4 (logging)
              LOAD_ATTR               44 (getLogger)
              PUSH_NULL
              LOAD_CONST               7 ('pas.memory.store')
              CALL                     1
              STORE_NAME              23 (logger)

 61           LOAD_CONST               8 ('pas_memory_records')
              STORE_NAME              24 (_TABLE)

 66           LOAD_CONST               9 (256)
              STORE_NAME              25 (_MAX_TITLE_LEN)

 67           LOAD_CONST              10 (2048)
              STORE_NAME              26 (_MAX_SUMMARY_LEN)

 74           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA2E20, file "app\services\memory\store.py", line 74>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object prepare_memory_for_insert at 0x0000018C17F843D0, file "app\services\memory\store.py", line 74>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (prepare_memory_for_insert)

127           LOAD_CONST              13 (<code object _get_db at 0x0000018C17FA3960, file "app\services\memory\store.py", line 127>)
              MAKE_FUNCTION
              STORE_NAME              28 (_get_db)

138           LOAD_CONST              14 ('extra')

143           LOAD_CONST               2 (None)

138           BUILD_MAP                1
              LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\memory\store.py", line 138>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _safe_log_decision at 0x0000018C17F84850, file "app\services\memory\store.py", line 138>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              29 (_safe_log_decision)

164           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C18025E30, file "app\services\memory\store.py", line 164>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _govern_or_drop at 0x0000018C17CD4970, file "app\services\memory\store.py", line 164>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_govern_or_drop)

205           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\memory\store.py", line 205>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _execute_insert at 0x0000018C179A7290, file "app\services\memory\store.py", line 205>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_execute_insert)

220           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C18024930, file "app\services\memory\store.py", line 220>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _execute_upsert at 0x0000018C1801C9E0, file "app\services\memory\store.py", line 220>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_execute_upsert)

234           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C18025530, file "app\services\memory\store.py", line 234>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object _execute_status_update at 0x0000018C17EDEBC0, file "app\services\memory\store.py", line 234>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_execute_status_update)

277           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\store.py", line 277>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object insert_memory at 0x0000018C1794EBB0, file "app\services\memory\store.py", line 277>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              34 (insert_memory)

307           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\store.py", line 307>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object upsert_memory at 0x0000018C1794E810, file "app\services\memory\store.py", line 307>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              35 (upsert_memory)

335           LOAD_CONST              29 ('brokerage_id')

339           LOAD_CONST               2 (None)

335           BUILD_MAP                1
              LOAD_CONST              30 (<code object __annotate__ at 0x0000018C18025130, file "app\services\memory\store.py", line 335>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object quarantine_memory at 0x0000018C177C69F0, file "app\services\memory\store.py", line 335>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              36 (quarantine_memory)

445           LOAD_CONST              29 ('brokerage_id')

449           LOAD_CONST               2 (None)

445           BUILD_MAP                1
              LOAD_CONST              32 (<code object __annotate__ at 0x0000018C18025A30, file "app\services\memory\store.py", line 445>)
              MAKE_FUNCTION
              LOAD_CONST              33 (<code object expire_memory at 0x0000018C17F84B70, file "app\services\memory\store.py", line 445>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              37 (expire_memory)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app\services\memory\store.py", line 74>:
 74           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record')
              LOAD_CONST               2 ('MemoryRecord')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('dict')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object prepare_memory_for_insert at 0x0000018C17F843D0, file "app\services\memory\store.py", line 74>:
 74           RESUME                   0

 89           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (record)
              LOAD_GLOBAL              2 (MemoryRecord)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        12 (to L1)
              NOT_TAKEN

 90           LOAD_GLOBAL              5 (TypeError + NULL)
              LOAD_CONST               1 ('prepare_memory_for_insert requires a MemoryRecord')
              CALL                     1
              RAISE_VARARGS            1

 92   L1:     LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR                6 (brokerage_id)
              TO_BOOL
              POP_JUMP_IF_FALSE       33 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR                6 (brokerage_id)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE        12 (to L3)
              NOT_TAKEN

 93   L2:     LOAD_GLOBAL             11 (ValueError + NULL)
              LOAD_CONST               2 ('brokerage_id is required (tenant isolation)')
              CALL                     1
              RAISE_VARARGS            1

 95   L3:     LOAD_GLOBAL             13 (has_forbidden_transcript_field + NULL)
              LOAD_FAST_BORROW         0 (record)
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       12 (to L4)
              NOT_TAKEN

 96           LOAD_GLOBAL             11 (ValueError + NULL)

 97           LOAD_CONST               3 ('evidence/metadata contains a forbidden raw-transcript field; memory will not be serialized')

 96           CALL                     1
              RAISE_VARARGS            1

101   L4:     LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               14 (title)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L5:     LOAD_CONST               5 (None)
              LOAD_GLOBAL             16 (_MAX_TITLE_LEN)
              BINARY_SLICE
              STORE_FAST               1 (title)

102           LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               18 (summary)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L6:     LOAD_CONST               5 (None)
              LOAD_GLOBAL             20 (_MAX_SUMMARY_LEN)
              BINARY_SLICE
              STORE_FAST               2 (summary)

105           LOAD_CONST               6 ('memory_id')
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               22 (memory_id)

106           LOAD_CONST               7 ('brokerage_id')
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR                6 (brokerage_id)

107           LOAD_CONST               8 ('kind')
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               24 (kind)
              LOAD_ATTR               26 (value)

108           LOAD_CONST               9 ('source')
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               28 (source)
              LOAD_ATTR               26 (value)

109           LOAD_CONST              10 ('status')
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               30 (status)
              LOAD_ATTR               26 (value)

110           LOAD_CONST              11 ('title')
              LOAD_FAST                1 (title)

111           LOAD_CONST              12 ('summary')
              LOAD_FAST                2 (summary)

112           LOAD_CONST              13 ('evidence')
              LOAD_GLOBAL             33 (dict + NULL)
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               34 (evidence)
              CALL                     1

113           LOAD_CONST              14 ('confidence')
              LOAD_GLOBAL             37 (float + NULL)
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               38 (confidence)
              CALL                     1

114           LOAD_CONST              15 ('outcome_weight')
              LOAD_GLOBAL             37 (float + NULL)
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               40 (outcome_weight)
              CALL                     1

115           LOAD_CONST              16 ('ttl_days')
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               42 (ttl_days)

116           LOAD_CONST              17 ('created_at')
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               44 (created_at)
              LOAD_ATTR               47 (isoformat + NULL|self)
              CALL                     0

117           LOAD_CONST              18 ('expires_at')
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               48 (expires_at)
              TO_BOOL
              POP_JUMP_IF_FALSE       27 (to L7)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               48 (expires_at)
              LOAD_ATTR               47 (isoformat + NULL|self)
              CALL                     0
              JUMP_FORWARD             1 (to L8)
      L7:     LOAD_CONST               5 (None)

118   L8:     LOAD_CONST              19 ('lineage')
              LOAD_GLOBAL             33 (dict + NULL)
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               50 (lineage)
              CALL                     1

119           LOAD_CONST              20 ('metadata')
              LOAD_GLOBAL             33 (dict + NULL)
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               52 (metadata)
              CALL                     1

104           BUILD_MAP               15
              RETURN_VALUE

Disassembly of <code object _get_db at 0x0000018C17FA3960, file "app\services\memory\store.py", line 127>:
127           RESUME                   0

134           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('get_supabase',))
              IMPORT_NAME              0 (app.db.supabase_client)
              IMPORT_FROM              1 (get_supabase)
              STORE_FAST               0 (get_supabase)
              POP_TOP

135           LOAD_FAST_BORROW         0 (get_supabase)
              PUSH_NULL
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\memory\store.py", line 138>:
138           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('op')

140           LOAD_CONST               2 ('str')

138           LOAD_CONST               3 ('record')

141           LOAD_CONST               4 ('MemoryRecord')

138           LOAD_CONST               5 ('decision')

142           LOAD_CONST               2 ('str')

138           LOAD_CONST               6 ('extra')

143           LOAD_CONST               7 ('Optional[Dict[str, Any]]')

138           LOAD_CONST               8 ('return')

144           LOAD_CONST               9 ('None')

138           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _safe_log_decision at 0x0000018C17F84850, file "app\services\memory\store.py", line 138>:
138           RESUME                   0

148           LOAD_CONST               1 ('op')
              LOAD_FAST                0 (op)

149           LOAD_CONST               2 ('memory_id')
              LOAD_FAST_BORROW         1 (record)
              LOAD_ATTR                0 (memory_id)

150           LOAD_CONST               3 ('brokerage_id')
              LOAD_FAST_BORROW         1 (record)
              LOAD_ATTR                2 (brokerage_id)

151           LOAD_CONST               4 ('kind')
              LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (record)
              LOAD_ATTR                6 (kind)
              LOAD_GLOBAL              8 (MemoryKind)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (record)
              LOAD_ATTR                6 (kind)
              LOAD_ATTR               10 (value)
              JUMP_FORWARD            20 (to L2)
      L1:     LOAD_GLOBAL             13 (str + NULL)
              LOAD_FAST_BORROW         1 (record)
              LOAD_ATTR                6 (kind)
              CALL                     1

152   L2:     LOAD_CONST               5 ('status')
              LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (record)
              LOAD_ATTR               14 (status)
              LOAD_GLOBAL             16 (MemoryStatus)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (record)
              LOAD_ATTR               14 (status)
              LOAD_ATTR               10 (value)
              JUMP_FORWARD            20 (to L4)
      L3:     LOAD_GLOBAL             13 (str + NULL)
              LOAD_FAST_BORROW         1 (record)
              LOAD_ATTR               14 (status)
              CALL                     1

153   L4:     LOAD_CONST               6 ('decision')
              LOAD_FAST_BORROW         2 (decision)

147           BUILD_MAP                6
              STORE_FAST               4 (fields)

155           LOAD_FAST_BORROW         3 (extra)
              TO_BOOL
              POP_JUMP_IF_FALSE       38 (to L8)
              NOT_TAKEN

156           LOAD_FAST_BORROW         3 (extra)
              LOAD_ATTR               19 (items + NULL|self)
              CALL                     0
              GET_ITER
      L5:     FOR_ITER                17 (to L7)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   86 (k, v)

157           LOAD_FAST_BORROW_LOAD_FAST_BORROW 84 (k, fields)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN

158           JUMP_BACKWARD           13 (to L5)

159   L6:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 100 (v, fields)
              LOAD_FAST_BORROW         5 (k)
              STORE_SUBSCR
              JUMP_BACKWARD           19 (to L5)

156   L7:     END_FOR
              POP_ITER

161   L8:     LOAD_GLOBAL             20 (logger)
              LOAD_ATTR               23 (info + NULL|self)
              LOAD_CONST               7 (' | ')
              LOAD_ATTR               25 (join + NULL|self)
              LOAD_CONST               8 (<code object <genexpr> at 0x0000018C180C4360, file "app\services\memory\store.py", line 161>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         4 (fields)
              LOAD_ATTR               19 (items + NULL|self)
              CALL                     0
              GET_ITER
              CALL                     0
              CALL                     1
              CALL                     1
              POP_TOP
              LOAD_CONST               9 (None)
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180C4360, file "app\services\memory\store.py", line 161>:
 161           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                14 (to L3)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   18 (k, v)
               LOAD_FAST_BORROW         1 (k)
               FORMAT_SIMPLE
               LOAD_CONST               0 ('=')
               LOAD_FAST_BORROW         2 (v)
               FORMAT_SIMPLE
               BUILD_STRING             3
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           16 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app\services\memory\store.py", line 164>:
164           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record')
              LOAD_CONST               2 ('MemoryRecord')
              LOAD_CONST               3 ('op')
              LOAD_CONST               4 ('str')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Optional[MemoryRecord]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _govern_or_drop at 0x0000018C17CD4970, file "app\services\memory\store.py", line 164>:
164           RESUME                   0

168           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (record)
              LOAD_GLOBAL              2 (MemoryRecord)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        27 (to L1)
              NOT_TAKEN

169           LOAD_GLOBAL              4 (logger)
              LOAD_ATTR                7 (warning + NULL|self)
              LOAD_FAST_BORROW         1 (op)
              FORMAT_SIMPLE
              LOAD_CONST               1 (' dropped | reason=not_a_memory_record')
              BUILD_STRING             2
              CALL                     1
              POP_TOP

170           LOAD_CONST               2 (None)
              RETURN_VALUE

172   L1:     LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR                8 (brokerage_id)
              TO_BOOL
              POP_JUMP_IF_FALSE       33 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR                8 (brokerage_id)
              LOAD_ATTR               11 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE        27 (to L3)
              NOT_TAKEN

173   L2:     LOAD_GLOBAL              4 (logger)
              LOAD_ATTR                7 (warning + NULL|self)
              LOAD_FAST_BORROW         1 (op)
              FORMAT_SIMPLE
              LOAD_CONST               3 (' dropped | reason=missing_brokerage_id')
              BUILD_STRING             2
              CALL                     1
              POP_TOP

174           LOAD_CONST               2 (None)
              RETURN_VALUE

176   L3:     LOAD_GLOBAL             13 (has_forbidden_transcript_field + NULL)
              LOAD_FAST_BORROW         0 (record)
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       19 (to L4)
              NOT_TAKEN

178           LOAD_GLOBAL             15 (_safe_log_decision + NULL)

179           LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (op, record)
              LOAD_CONST               4 ('dropped')

180           LOAD_CONST               5 ('reason')
              LOAD_CONST               6 ('forbidden_transcript_field')
              BUILD_MAP                1

178           LOAD_CONST               7 (('op', 'record', 'decision', 'extra'))
              CALL_KW                  4
              POP_TOP

182           LOAD_CONST               2 (None)
              RETURN_VALUE

184   L4:     LOAD_GLOBAL             17 (apply_memory_governance + NULL)
              LOAD_FAST_BORROW         0 (record)
              CALL                     1
              STORE_FAST               2 (governed)

186           LOAD_GLOBAL             19 (validate_memory_record + NULL)
              LOAD_FAST_BORROW         2 (governed)
              CALL                     1
              STORE_FAST               3 (errors)

187           LOAD_FAST_BORROW         3 (errors)
              TO_BOOL
              POP_JUMP_IF_FALSE       30 (to L5)
              NOT_TAKEN

188           LOAD_GLOBAL             15 (_safe_log_decision + NULL)

189           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (op, governed)
              LOAD_CONST               4 ('dropped')

190           LOAD_CONST               5 ('reason')
              LOAD_CONST               8 ('governance_validation_failed')

191           LOAD_CONST               9 ('error_count')
              LOAD_GLOBAL             21 (len + NULL)
              LOAD_FAST_BORROW         3 (errors)
              CALL                     1

190           BUILD_MAP                2

188           LOAD_CONST               7 (('op', 'record', 'decision', 'extra'))
              CALL_KW                  4
              POP_TOP

193           LOAD_CONST               2 (None)
              RETURN_VALUE

195   L5:     LOAD_GLOBAL             23 (should_persist_memory + NULL)
              LOAD_FAST_BORROW         2 (governed)
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_TRUE        19 (to L6)
              NOT_TAKEN

196           LOAD_GLOBAL             15 (_safe_log_decision + NULL)

197           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (op, governed)
              LOAD_CONST               4 ('dropped')

198           LOAD_CONST               5 ('reason')
              LOAD_CONST              10 ('should_persist_false')
              BUILD_MAP                1

196           LOAD_CONST               7 (('op', 'record', 'decision', 'extra'))
              CALL_KW                  4
              POP_TOP

200           LOAD_CONST               2 (None)
              RETURN_VALUE

202   L6:     LOAD_FAST_BORROW         2 (governed)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\memory\store.py", line 205>:
205           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_CONST               2 ('dict')
              LOAD_CONST               3 ('op')
              LOAD_CONST               4 ('str')
              LOAD_CONST               5 ('memory_id')
              LOAD_CONST               4 ('str')
              LOAD_CONST               6 ('return')
              LOAD_CONST               7 ('Optional[dict]')
              BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _execute_insert at 0x0000018C179A7290, file "app\services\memory\store.py", line 205>:
 205           RESUME                   0

 208           NOP

 209   L1:     LOAD_GLOBAL              1 (_get_db + NULL)
               CALL                     0
               STORE_FAST               3 (db)

 210           LOAD_FAST_BORROW         3 (db)
               LOAD_ATTR                3 (table + NULL|self)
               LOAD_GLOBAL              4 (_TABLE)
               CALL                     1
               LOAD_ATTR                7 (insert + NULL|self)
               LOAD_FAST_BORROW         0 (row)
               CALL                     1
               LOAD_ATTR                9 (execute + NULL|self)
               CALL                     0
               POP_TOP

 211           LOAD_FAST_BORROW         0 (row)
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 212           LOAD_GLOBAL             10 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       60 (to L7)
               NOT_TAKEN
               STORE_FAST               4 (e)

 213   L4:     LOAD_GLOBAL             12 (logger)
               LOAD_ATTR               15 (warning + NULL|self)

 214           LOAD_FAST                1 (op)
               FORMAT_SIMPLE
               LOAD_CONST               1 (' failed (non-critical) | memory_id=')
               LOAD_FAST                2 (memory_id)
               FORMAT_SIMPLE
               LOAD_CONST               2 (' | error_type=')

 215           LOAD_GLOBAL             17 (type + NULL)
               LOAD_FAST                4 (e)
               CALL                     1
               LOAD_ATTR               18 (__name__)
               FORMAT_SIMPLE

 214           BUILD_STRING             5

 213           CALL                     1
               POP_TOP

 217   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               4 (e)
               DELETE_FAST              4 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               4 (e)
               DELETE_FAST              4 (e)
               RERAISE                  1

 212   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app\services\memory\store.py", line 220>:
220           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_CONST               2 ('dict')
              LOAD_CONST               3 ('op')
              LOAD_CONST               4 ('str')
              LOAD_CONST               5 ('memory_id')
              LOAD_CONST               4 ('str')
              LOAD_CONST               6 ('return')
              LOAD_CONST               7 ('Optional[dict]')
              BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _execute_upsert at 0x0000018C1801C9E0, file "app\services\memory\store.py", line 220>:
 220           RESUME                   0

 222           NOP

 223   L1:     LOAD_GLOBAL              1 (_get_db + NULL)
               CALL                     0
               STORE_FAST               3 (db)

 224           LOAD_FAST_BORROW         3 (db)
               LOAD_ATTR                3 (table + NULL|self)
               LOAD_GLOBAL              4 (_TABLE)
               CALL                     1
               LOAD_ATTR                7 (upsert + NULL|self)
               LOAD_FAST_BORROW         0 (row)
               LOAD_CONST               1 ('memory_id')
               LOAD_CONST               2 (('on_conflict',))
               CALL_KW                  2
               LOAD_ATTR                9 (execute + NULL|self)
               CALL                     0
               POP_TOP

 225           LOAD_FAST_BORROW         0 (row)
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 226           LOAD_GLOBAL             10 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       60 (to L7)
               NOT_TAKEN
               STORE_FAST               4 (e)

 227   L4:     LOAD_GLOBAL             12 (logger)
               LOAD_ATTR               15 (warning + NULL|self)

 228           LOAD_FAST                1 (op)
               FORMAT_SIMPLE
               LOAD_CONST               3 (' failed (non-critical) | memory_id=')
               LOAD_FAST                2 (memory_id)
               FORMAT_SIMPLE
               LOAD_CONST               4 (' | error_type=')

 229           LOAD_GLOBAL             17 (type + NULL)
               LOAD_FAST                4 (e)
               CALL                     1
               LOAD_ATTR               18 (__name__)
               FORMAT_SIMPLE

 228           BUILD_STRING             5

 227           CALL                     1
               POP_TOP

 231   L5:     POP_EXCEPT
               LOAD_CONST               5 (None)
               STORE_FAST               4 (e)
               DELETE_FAST              4 (e)
               LOAD_CONST               5 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               5 (None)
               STORE_FAST               4 (e)
               DELETE_FAST              4 (e)
               RERAISE                  1

 226   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "app\services\memory\store.py", line 234>:
234           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('memory_id')

236           LOAD_CONST               2 ('str')

234           LOAD_CONST               3 ('brokerage_id')

237           LOAD_CONST               2 ('str')

234           LOAD_CONST               4 ('new_status')

238           LOAD_CONST               5 ('MemoryStatus')

234           LOAD_CONST               6 ('reason')

239           LOAD_CONST               2 ('str')

234           LOAD_CONST               7 ('op')

240           LOAD_CONST               2 ('str')

234           LOAD_CONST               8 ('return')

241           LOAD_CONST               9 ('Optional[dict]')

234           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _execute_status_update at 0x0000018C17EDEBC0, file "app\services\memory\store.py", line 234>:
 234           RESUME                   0

 245           NOP

 246   L1:     LOAD_GLOBAL              1 (_get_db + NULL)
               CALL                     0
               STORE_FAST               5 (db)

 248           LOAD_CONST               1 ('status')
               LOAD_FAST_BORROW         2 (new_status)
               LOAD_ATTR                2 (value)

 249           LOAD_CONST               2 ('metadata')

 250           LOAD_CONST               3 ('audit')

 251           LOAD_CONST               4 ('op')
               LOAD_FAST_BORROW         4 (op)

 252           LOAD_CONST               5 ('reason')
               LOAD_GLOBAL              5 (str + NULL)
               LOAD_FAST_BORROW         3 (reason)
               CALL                     1
               LOAD_CONST               6 (slice(None, 256, None))
               BINARY_OP               26 ([])

 253           LOAD_CONST               7 ('at')
               LOAD_GLOBAL              6 (datetime)
               LOAD_ATTR                8 (now)
               PUSH_NULL
               LOAD_GLOBAL             10 (timezone)
               LOAD_ATTR               12 (utc)
               CALL                     1
               LOAD_ATTR               15 (isoformat + NULL|self)
               CALL                     0

 250           BUILD_MAP                3

 249           BUILD_MAP                1

 247           BUILD_MAP                2
               STORE_FAST               6 (update)

 258           LOAD_FAST_BORROW         5 (db)
               LOAD_ATTR               17 (table + NULL|self)
               LOAD_GLOBAL             18 (_TABLE)
               CALL                     1

 259           LOAD_ATTR               21 (update + NULL|self)
               LOAD_FAST_BORROW         6 (update)
               CALL                     1

 260           LOAD_ATTR               23 (eq + NULL|self)
               LOAD_CONST               8 ('memory_id')
               LOAD_FAST_BORROW         0 (memory_id)
               CALL                     2

 261           LOAD_ATTR               23 (eq + NULL|self)
               LOAD_CONST               9 ('brokerage_id')
               LOAD_FAST_BORROW         1 (brokerage_id)
               CALL                     2

 262           LOAD_ATTR               25 (execute + NULL|self)
               CALL                     0

 257           STORE_FAST               7 (result)

 264           LOAD_GLOBAL             27 (getattr + NULL)
               LOAD_FAST_BORROW         7 (result)
               LOAD_CONST              10 ('data')
               LOAD_CONST              11 (None)
               CALL                     3
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_FAST                6 (update)
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 265           LOAD_GLOBAL             28 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       60 (to L7)
               NOT_TAKEN
               STORE_FAST               8 (e)

 266   L4:     LOAD_GLOBAL             30 (logger)
               LOAD_ATTR               33 (warning + NULL|self)

 267           LOAD_FAST                4 (op)
               FORMAT_SIMPLE
               LOAD_CONST              12 (' failed (non-critical) | memory_id=')
               LOAD_FAST                0 (memory_id)
               FORMAT_SIMPLE
               LOAD_CONST              13 (' | error_type=')

 268           LOAD_GLOBAL             35 (type + NULL)
               LOAD_FAST                8 (e)
               CALL                     1
               LOAD_ATTR               36 (__name__)
               FORMAT_SIMPLE

 267           BUILD_STRING             5

 266           CALL                     1
               POP_TOP

 270   L5:     POP_EXCEPT
               LOAD_CONST              11 (None)
               STORE_FAST               8 (e)
               DELETE_FAST              8 (e)
               LOAD_CONST              11 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST              11 (None)
               STORE_FAST               8 (e)
               DELETE_FAST              8 (e)
               RERAISE                  1

 265   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\store.py", line 277>:
277           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record')
              LOAD_CONST               2 ('MemoryRecord')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object insert_memory at 0x0000018C1794EBB0, file "app\services\memory\store.py", line 277>:
 277           RESUME                   0

 290           LOAD_GLOBAL              1 (_govern_or_drop + NULL)
               LOAD_FAST_BORROW         0 (record)
               LOAD_CONST               1 ('insert_memory')
               LOAD_CONST               2 (('op',))
               CALL_KW                  2
               STORE_FAST               1 (governed)

 291           LOAD_FAST_BORROW         1 (governed)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

 292           LOAD_CONST               3 (None)
               RETURN_VALUE

 294   L1:     NOP

 295   L2:     LOAD_GLOBAL              3 (prepare_memory_for_insert + NULL)
               LOAD_FAST_BORROW         1 (governed)
               CALL                     1
               STORE_FAST               2 (row)

 304   L3:     LOAD_GLOBAL             15 (_execute_insert + NULL)
               LOAD_FAST                2 (row)
               LOAD_CONST               1 ('insert_memory')
               LOAD_FAST                1 (governed)
               LOAD_ATTR               16 (memory_id)
               LOAD_CONST               9 (('op', 'memory_id'))
               CALL_KW                  3
               RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

 296           LOAD_GLOBAL              4 (TypeError)
               LOAD_GLOBAL              6 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       50 (to L8)
               NOT_TAKEN
               STORE_FAST               3 (e)

 297   L5:     LOAD_GLOBAL              9 (_safe_log_decision + NULL)

 298           LOAD_CONST               1 ('insert_memory')
               LOAD_FAST                1 (governed)
               LOAD_CONST               4 ('dropped')

 299           LOAD_CONST               5 ('reason')
               LOAD_CONST               6 ('prepare_failed')

 300           LOAD_CONST               7 ('error_type')
               LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                3 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)

 299           BUILD_MAP                2

 297           LOAD_CONST               8 (('op', 'record', 'decision', 'extra'))
               CALL_KW                  4
               POP_TOP

 302   L6:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               3 (e)
               DELETE_FAST              3 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L7:     LOAD_CONST               3 (None)
               STORE_FAST               3 (e)
               DELETE_FAST              3 (e)
               RERAISE                  1

 296   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L4 [0]
  L4 to L5 -> L9 [1] lasti
  L5 to L6 -> L7 [1] lasti
  L7 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\store.py", line 307>:
307           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record')
              LOAD_CONST               2 ('MemoryRecord')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object upsert_memory at 0x0000018C1794E810, file "app\services\memory\store.py", line 307>:
 307           RESUME                   0

 314           LOAD_GLOBAL              1 (_govern_or_drop + NULL)
               LOAD_FAST_BORROW         0 (record)
               LOAD_CONST               1 ('upsert_memory')
               LOAD_CONST               2 (('op',))
               CALL_KW                  2
               STORE_FAST               1 (governed)

 315           LOAD_FAST_BORROW         1 (governed)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

 316           LOAD_CONST               3 (None)
               RETURN_VALUE

 318   L1:     NOP

 319   L2:     LOAD_GLOBAL              3 (prepare_memory_for_insert + NULL)
               LOAD_FAST_BORROW         1 (governed)
               CALL                     1
               STORE_FAST               2 (row)

 328   L3:     LOAD_GLOBAL             15 (_execute_upsert + NULL)
               LOAD_FAST                2 (row)
               LOAD_CONST               1 ('upsert_memory')
               LOAD_FAST                1 (governed)
               LOAD_ATTR               16 (memory_id)
               LOAD_CONST               9 (('op', 'memory_id'))
               CALL_KW                  3
               RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

 320           LOAD_GLOBAL              4 (TypeError)
               LOAD_GLOBAL              6 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       50 (to L8)
               NOT_TAKEN
               STORE_FAST               3 (e)

 321   L5:     LOAD_GLOBAL              9 (_safe_log_decision + NULL)

 322           LOAD_CONST               1 ('upsert_memory')
               LOAD_FAST                1 (governed)
               LOAD_CONST               4 ('dropped')

 323           LOAD_CONST               5 ('reason')
               LOAD_CONST               6 ('prepare_failed')

 324           LOAD_CONST               7 ('error_type')
               LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                3 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)

 323           BUILD_MAP                2

 321           LOAD_CONST               8 (('op', 'record', 'decision', 'extra'))
               CALL_KW                  4
               POP_TOP

 326   L6:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               3 (e)
               DELETE_FAST              3 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L7:     LOAD_CONST               3 (None)
               STORE_FAST               3 (e)
               DELETE_FAST              3 (e)
               RERAISE                  1

 320   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L4 [0]
  L4 to L5 -> L9 [1] lasti
  L5 to L6 -> L7 [1] lasti
  L7 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "app\services\memory\store.py", line 335>:
335           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record_or_id')

336           LOAD_CONST               2 ('Union[MemoryRecord, str]')

335           LOAD_CONST               3 ('reason')

337           LOAD_CONST               4 ('str')

335           LOAD_CONST               5 ('brokerage_id')

339           LOAD_CONST               6 ('Optional[str]')

335           LOAD_CONST               7 ('return')

340           LOAD_CONST               8 ('Optional[dict]')

335           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object quarantine_memory at 0x0000018C177C69F0, file "app\services\memory\store.py", line 335>:
 335            RESUME                   0

 357            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (record_or_id)
                LOAD_GLOBAL              2 (MemoryRecord)
                CALL                     2
                TO_BOOL
                EXTENDED_ARG             1
                POP_JUMP_IF_FALSE      430 (to L9)
                NOT_TAKEN

 358            LOAD_FAST                0 (record_or_id)
                STORE_FAST               3 (record)

 360            LOAD_FAST_BORROW         3 (record)
                LOAD_ATTR                4 (brokerage_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       33 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (record)
                LOAD_ATTR                4 (brokerage_id)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        24 (to L2)
                NOT_TAKEN

 361    L1:     LOAD_GLOBAL              8 (logger)
                LOAD_ATTR               11 (warning + NULL|self)
                LOAD_CONST               1 ('quarantine_memory dropped | reason=missing_brokerage_id')
                CALL                     1
                POP_TOP

 362            LOAD_CONST               2 (None)
                RETURN_VALUE

 364    L2:     LOAD_GLOBAL             13 (has_forbidden_transcript_field + NULL)
                LOAD_FAST_BORROW         3 (record)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       20 (to L3)
                NOT_TAKEN

 365            LOAD_GLOBAL             15 (_safe_log_decision + NULL)

 366            LOAD_CONST               3 ('quarantine_memory')
                LOAD_FAST_BORROW         3 (record)
                LOAD_CONST               4 ('dropped')

 367            LOAD_CONST               5 ('reason')
                LOAD_CONST               6 ('forbidden_transcript_field')
                BUILD_MAP                1

 365            LOAD_CONST               7 (('op', 'record', 'decision', 'extra'))
                CALL_KW                  4
                POP_TOP

 369            LOAD_CONST               2 (None)
                RETURN_VALUE

 374    L3:     LOAD_GLOBAL             16 (dataclasses)
                LOAD_ATTR               18 (replace)
                PUSH_NULL
                LOAD_FAST_BORROW         3 (record)
                LOAD_GLOBAL             20 (MemoryStatus)
                LOAD_ATTR               22 (QUARANTINED)
                LOAD_CONST               8 (('status',))
                CALL_KW                  2
                STORE_FAST               4 (forced)

 375            LOAD_GLOBAL             25 (apply_memory_governance + NULL)
                LOAD_FAST_BORROW         4 (forced)
                CALL                     1
                STORE_FAST               5 (governed)

 380            LOAD_FAST_BORROW         5 (governed)
                LOAD_ATTR               26 (status)
                LOAD_GLOBAL             20 (MemoryStatus)
                LOAD_ATTR               22 (QUARANTINED)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       39 (to L4)
                NOT_TAKEN

 381            LOAD_GLOBAL             16 (dataclasses)
                LOAD_ATTR               18 (replace)
                PUSH_NULL
                LOAD_FAST_BORROW         5 (governed)
                LOAD_GLOBAL             20 (MemoryStatus)
                LOAD_ATTR               22 (QUARANTINED)
                LOAD_CONST               8 (('status',))
                CALL_KW                  2
                STORE_FAST               5 (governed)

 388    L4:     LOAD_GLOBAL             29 (validate_memory_record + NULL)
                LOAD_FAST_BORROW         5 (governed)
                CALL                     1
                STORE_FAST               6 (errors)

 389            LOAD_FAST_BORROW         6 (errors)
                TO_BOOL
                POP_JUMP_IF_FALSE       31 (to L5)
                NOT_TAKEN

 390            LOAD_GLOBAL             15 (_safe_log_decision + NULL)

 391            LOAD_CONST               3 ('quarantine_memory')
                LOAD_FAST_BORROW         5 (governed)
                LOAD_CONST               4 ('dropped')

 392            LOAD_CONST               5 ('reason')
                LOAD_CONST               9 ('governance_validation_failed')

 393            LOAD_CONST              10 ('error_count')
                LOAD_GLOBAL             31 (len + NULL)
                LOAD_FAST_BORROW         6 (errors)
                CALL                     1

 392            BUILD_MAP                2

 390            LOAD_CONST               7 (('op', 'record', 'decision', 'extra'))
                CALL_KW                  4
                POP_TOP

 395            LOAD_CONST               2 (None)
                RETURN_VALUE

 397    L5:     NOP

 398    L6:     LOAD_GLOBAL             33 (prepare_memory_for_insert + NULL)
                LOAD_FAST_BORROW         5 (governed)
                CALL                     1
                STORE_FAST               7 (row)

 410    L7:     LOAD_GLOBAL             43 (dict + NULL)
                LOAD_FAST                7 (row)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST              13 ('metadata')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L8:     CALL                     1
                STORE_FAST               9 (meta)

 412            LOAD_CONST              14 ('op')
                LOAD_CONST               3 ('quarantine_memory')

 413            LOAD_CONST               5 ('reason')
                LOAD_GLOBAL             47 (str + NULL)
                LOAD_FAST                1 (reason)
                CALL                     1
                LOAD_CONST              15 (slice(None, 256, None))
                BINARY_OP               26 ([])

 414            LOAD_CONST              16 ('at')
                LOAD_GLOBAL             48 (datetime)
                LOAD_ATTR               50 (now)
                PUSH_NULL
                LOAD_GLOBAL             52 (timezone)
                LOAD_ATTR               54 (utc)
                CALL                     1
                LOAD_ATTR               57 (isoformat + NULL|self)
                CALL                     0

 411            BUILD_MAP                3
                LOAD_FAST                9 (meta)
                LOAD_CONST              17 ('audit')
                STORE_SUBSCR

 416            LOAD_FAST_LOAD_FAST    151 (meta, row)
                LOAD_CONST              13 ('metadata')
                STORE_SUBSCR

 420            LOAD_GLOBAL             59 (_execute_upsert + NULL)

 421            LOAD_FAST                7 (row)
                LOAD_CONST               3 ('quarantine_memory')
                LOAD_FAST                5 (governed)
                LOAD_ATTR               60 (memory_id)

 420            LOAD_CONST              18 (('op', 'memory_id'))
                CALL_KW                  3
                RETURN_VALUE

 425    L9:     LOAD_FAST                0 (record_or_id)
                STORE_FAST              10 (memory_id)

 426            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW        10 (memory_id)
                LOAD_GLOBAL             46 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L10)
                NOT_TAKEN
                LOAD_FAST_BORROW        10 (memory_id)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        24 (to L11)
                NOT_TAKEN

 427   L10:     LOAD_GLOBAL              8 (logger)
                LOAD_ATTR               11 (warning + NULL|self)
                LOAD_CONST              19 ('quarantine_memory dropped | reason=invalid_memory_id')
                CALL                     1
                POP_TOP

 428            LOAD_CONST               2 (None)
                RETURN_VALUE

 429   L11:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (brokerage_id)
                LOAD_GLOBAL             46 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L12)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (brokerage_id)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        28 (to L13)
                NOT_TAKEN

 430   L12:     LOAD_GLOBAL              8 (logger)
                LOAD_ATTR               11 (warning + NULL|self)

 431            LOAD_CONST              20 ('quarantine_memory dropped | memory_id=')
                LOAD_FAST_BORROW        10 (memory_id)
                FORMAT_SIMPLE
                LOAD_CONST              21 (' | reason=missing_brokerage_id')
                BUILD_STRING             3

 430            CALL                     1
                POP_TOP

 434            LOAD_CONST               2 (None)
                RETURN_VALUE

 436   L13:     LOAD_GLOBAL             63 (_execute_status_update + NULL)

 437            LOAD_FAST_BORROW        10 (memory_id)

 438            LOAD_FAST_BORROW         2 (brokerage_id)

 439            LOAD_GLOBAL             20 (MemoryStatus)
                LOAD_ATTR               22 (QUARANTINED)

 440            LOAD_FAST_BORROW         1 (reason)

 441            LOAD_CONST               3 ('quarantine_memory')

 436            LOAD_CONST              22 (('memory_id', 'brokerage_id', 'new_status', 'reason', 'op'))
                CALL_KW                  5
                RETURN_VALUE

  --   L14:     PUSH_EXC_INFO

 399            LOAD_GLOBAL             34 (TypeError)
                LOAD_GLOBAL             36 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       50 (to L18)
                NOT_TAKEN
                STORE_FAST               8 (e)

 400   L15:     LOAD_GLOBAL             15 (_safe_log_decision + NULL)

 401            LOAD_CONST               3 ('quarantine_memory')
                LOAD_FAST                5 (governed)
                LOAD_CONST               4 ('dropped')

 402            LOAD_CONST               5 ('reason')
                LOAD_CONST              11 ('prepare_failed')

 403            LOAD_CONST              12 ('error_type')
                LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)

 402            BUILD_MAP                2

 400            LOAD_CONST               7 (('op', 'record', 'decision', 'extra'))
                CALL_KW                  4
                POP_TOP

 405   L16:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L17:     LOAD_CONST               2 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 399   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L6 to L7 -> L14 [0]
  L14 to L15 -> L19 [1] lasti
  L15 to L16 -> L17 [1] lasti
  L17 to L19 -> L19 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app\services\memory\store.py", line 445>:
445           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record_or_id')

446           LOAD_CONST               2 ('Union[MemoryRecord, str]')

445           LOAD_CONST               3 ('reason')

447           LOAD_CONST               4 ('str')

445           LOAD_CONST               5 ('brokerage_id')

449           LOAD_CONST               6 ('Optional[str]')

445           LOAD_CONST               7 ('return')

450           LOAD_CONST               8 ('Optional[dict]')

445           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object expire_memory at 0x0000018C17F84B70, file "app\services\memory\store.py", line 445>:
445           RESUME                   0

457           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (record_or_id)
              LOAD_GLOBAL              2 (MemoryRecord)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE      126 (to L3)
              NOT_TAKEN

458           LOAD_FAST                0 (record_or_id)
              STORE_FAST               3 (record)

459           LOAD_FAST_BORROW         3 (record)
              LOAD_ATTR                4 (brokerage_id)
              TO_BOOL
              POP_JUMP_IF_FALSE       33 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         3 (record)
              LOAD_ATTR                4 (brokerage_id)
              LOAD_ATTR                7 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE        24 (to L2)
              NOT_TAKEN

460   L1:     LOAD_GLOBAL              8 (logger)
              LOAD_ATTR               11 (warning + NULL|self)
              LOAD_CONST               1 ('expire_memory dropped | reason=missing_brokerage_id')
              CALL                     1
              POP_TOP

461           LOAD_CONST               2 (None)
              RETURN_VALUE

462   L2:     LOAD_GLOBAL             13 (_execute_status_update + NULL)

463           LOAD_FAST_BORROW         3 (record)
              LOAD_ATTR               14 (memory_id)

464           LOAD_FAST_BORROW         3 (record)
              LOAD_ATTR                4 (brokerage_id)

465           LOAD_GLOBAL             16 (MemoryStatus)
              LOAD_ATTR               18 (EXPIRED)

466           LOAD_FAST_BORROW         1 (reason)

467           LOAD_CONST               3 ('expire_memory')

462           LOAD_CONST               4 (('memory_id', 'brokerage_id', 'new_status', 'reason', 'op'))
              CALL_KW                  5
              RETURN_VALUE

470   L3:     LOAD_FAST                0 (record_or_id)
              STORE_FAST               4 (memory_id)

471           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         4 (memory_id)
              LOAD_GLOBAL             20 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         4 (memory_id)
              LOAD_ATTR                7 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE        24 (to L5)
              NOT_TAKEN

472   L4:     LOAD_GLOBAL              8 (logger)
              LOAD_ATTR               11 (warning + NULL|self)
              LOAD_CONST               5 ('expire_memory dropped | reason=invalid_memory_id')
              CALL                     1
              POP_TOP

473           LOAD_CONST               2 (None)
              RETURN_VALUE

474   L5:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (brokerage_id)
              LOAD_GLOBAL             20 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L6)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (brokerage_id)
              LOAD_ATTR                7 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE        28 (to L7)
              NOT_TAKEN

475   L6:     LOAD_GLOBAL              8 (logger)
              LOAD_ATTR               11 (warning + NULL|self)

476           LOAD_CONST               6 ('expire_memory dropped | memory_id=')
              LOAD_FAST_BORROW         4 (memory_id)
              FORMAT_SIMPLE
              LOAD_CONST               7 (' | reason=missing_brokerage_id')
              BUILD_STRING             3

475           CALL                     1
              POP_TOP

479           LOAD_CONST               2 (None)
              RETURN_VALUE

481   L7:     LOAD_GLOBAL             13 (_execute_status_update + NULL)

482           LOAD_FAST_BORROW         4 (memory_id)

483           LOAD_FAST_BORROW         2 (brokerage_id)

484           LOAD_GLOBAL             16 (MemoryStatus)
              LOAD_ATTR               18 (EXPIRED)

485           LOAD_FAST_BORROW         1 (reason)

486           LOAD_CONST               3 ('expire_memory')

481           LOAD_CONST               4 (('memory_id', 'brokerage_id', 'new_status', 'reason', 'op'))
              CALL_KW                  5
              RETURN_VALUE
```
