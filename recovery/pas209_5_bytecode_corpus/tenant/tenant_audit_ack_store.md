# tenant/tenant_audit_ack_store

- **pyc:** `app\services\tenant\__pycache__\tenant_audit_ack_store.cpython-314.pyc`
- **expected source path (absent):** `app\services\tenant/tenant_audit_ack_store.py`
- **co_filename (from bytecode):** `app\services\tenant\tenant_audit_ack_store.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** tenant

## Module docstring

```
PAS177 — Durable tenant audit acknowledgement store (Supabase-backed v1).

Append-only durable backing for tenant audit acknowledgements.
Persists to ``pas_tenant_audit_acknowledgements`` (proposal at
``scripts/migrate_v25_tenant_audit_acknowledgements.sql``).

Doctrine carried by every helper:

* **Append-only.** This module exposes only INSERT + read
  helpers. There is NO update helper, NO delete helper, NO
  mutation surface anywhere.
* **Closed actor_type + acknowledgement_type enums.** Mirror
  the v25 CHECK constraints; service-layer validation refuses
  anything outside the closed sets.
* **Closed metadata + notes_token allow-lists.** The JSONB
  payload is projected against ``ALLOWED_METADATA_KEYS`` at
  write time; the ``notes_token`` + ``actor_id`` fields are
  validated against the closed alphanumeric + dash +
  underscore character set.
* **No PII.** No phone / email / transcript / raw_payload /
  signature / secret / env_value / callback_notes /
  dedupe_key / raw_audit_metadata anywhere.
* **No exceptions escape.** DB unavailable → structural
  ``status="skipped"`` envelope. NEVER raises.
* **Bounded pagination.** Hard caps in the read helpers.
* **Brokerage scoped.** Every read and write requires a
  brokerage_id; cross-brokerage attempts return failed
  envelopes.
* **Idempotency awareness.** Repeated ACK for the same
  ``(brokerage_id, acknowledgement_type, audit_entry_id |
  merkle_root_id)`` returns ``duplicate=True`` without
  raising.

Public surface:

  * ``ALLOWED_ACTOR_TYPES``
  * ``ALLOWED_ACKNOWLEDGEMENT_TYPES``
  * ``ALLOWED_METADATA_KEYS``
  * ``record_tenant_audit_acknowledgement(...)``
  * ``list_tenant_audit_acknowledgements(...)``
  * ``tenant_acknowledgement_summary(...)``
  * ``acknowledgement_exists(...)``
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `datetime`, `get_supabase`, `logging`, `timezone`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_bound_brokerage_id`, `_bound_str_token`, `_bound_uuid_like`, `_clamp_limit`, `_get_db_safe`, `_iso`, `_list_envelope`, `_now_dt`, `_project_metadata`, `_project_row`, `_safe_envelope`, `_validate_ack_type`, `_validate_actor_type`, `acknowledgement_exists`, `list_tenant_audit_acknowledgements`, `record_tenant_audit_acknowledgement`, `tenant_acknowledgement_summary`

## Env-key candidates

`AUDIT_ENTRY_VIEWED`, `TENANT`

## String constants (redacted where noted)

- '\nPAS177 — Durable tenant audit acknowledgement store (Supabase-backed v1).\n\nAppend-only durable backing for tenant audit acknowledgements.\nPersists to ``pas_tenant_audit_acknowledgements`` (proposal at\n``scripts/migrate_v25_tenant_audit_acknowledgements.sql``).\n\nDoctrine carried by every helper:\n\n* **Append-only.** This module exposes only INSERT + read\n  helpers. There is NO update helper, NO delete helper, NO\n  mutation surface anywhere.\n* **Closed actor_type + acknowledgement_type enums.** Mirror\n  the v25 CHECK constraints; service-layer validation refuses\n  anything outside the closed sets.\n* **Closed metadata + notes_token allow-lists.** The JSONB\n  payload is projected against ``ALLOWED_METADATA_KEYS`` at\n  write time; the ``notes_token`` + ``actor_id`` fields are\n  validated against the closed alphanumeric + dash +\n  underscore character set.\n* **No PII.** No phone / email / transcript / raw_payload /\n  signature / secret / env_value / callback_notes /\n  dedupe_key / raw_audit_metadata anywhere.\n* **No exceptions escape.** DB unavailable → structural\n  ``status="skipped"`` envelope. NEVER raises.\n* **Bounded pagination.** Hard caps in the read helpers.\n* **Brokerage scoped.** Every read and write requires a\n  brokerage_id; cross-brokerage attempts return failed\n  envelopes.\n* **Idempotency awareness.** Repeated ACK for the same\n  ``(brokerage_id, acknowledgement_type, audit_entry_id |\n  merkle_root_id)`` returns ``duplicate=True`` without\n  raising.\n\nPublic surface:\n\n  * ``ALLOWED_ACTOR_TYPES``\n  * ``ALLOWED_ACKNOWLEDGEMENT_TYPES``\n  * ``ALLOWED_METADATA_KEYS``\n  * ``record_tenant_audit_acknowledgement(...)``\n  * ``list_tenant_audit_acknowledgements(...)``\n  * ``tenant_acknowledgement_summary(...)``\n  * ``acknowledgement_exists(...)``\n'
- 'pas.tenant.audit_ack_store'
- 'pas_tenant_audit_acknowledgements'
- 'TENANT'
- 'error_code'
- 🔒 '<REDACTED:high-entropy blob, len=64>'
- 'brokerage_id'
- 'audit_entry_id'
- 'merkle_root_id'
- 'actor_type'
- 'actor_id'
- 'acknowledgement_type'
- 'notes_token'
- 'metadata'
- 'duplicate'
- 'ack_row'
- 'warnings'
- 'rows'
- 'count'
- 'limit'
- 'filter_ack_type'
- 'now'
- 'Any'
- 'return'
- 'datetime'
- 'str'
- 'seconds'
- 'tenant_audit_ack_store db client unavailable type='
- 'value'
- 'max_len'
- 'int'
- 'Optional[str]'
- 'Bounded + closed-character-set string validation.\nNEVER raises. Returns None on invalid input.'
- 'Accepts UUID-shaped or opaque ID strings up to ``max_len``.\nNEVER raises.'
- 'Dict[str, Any]'
- 'row'
- 'Optional[Dict[str, Any]]'
- 'status'
- 'bool'
- 'Optional[List[str]]'
- 'Optional[List[Dict[str, Any]]]'
- 'invalid_actor_type'
- 'invalid_acknowledgement_type'
- 'Record a tenant audit acknowledgement. Append-only;\nidempotent for repeated ACK of the same logical target.\n\nReturns a structural envelope. NEVER raises. NEVER returns\nraw payload / secrets / PII.\n\nOutcomes:\n  * ``status="ok", duplicate=False`` — fresh insert.\n  * ``status="ok", duplicate=True``  — same logical ACK\n    already exists; the caller treats as success.\n  * ``status="skipped"`` — DB unavailable.\n  * ``status="failed"`` — input validation error.\n'
- 'failed'
- 'missing_brokerage_id'
- 'invalid_actor_id'
- 'invalid_notes_token'
- 'AUDIT_ENTRY_VIEWED'
- 'missing_audit_entry_id'
- 'missing_merkle_root_id'
- 'skipped'
- 'tenant_audit_ack_store_unavailable'
- 'data'
- 'record_tenant_audit_acknowledgement idempotency read error type='
- 'acknowledgement_id'
- 'acknowledged_at'
- 'record_tenant_audit_acknowledgement db error type='
- 'db_write_failed:'
- "Read the brokerage's acknowledgements, optionally filtered\nby acknowledgement_type. NEVER raises. NEVER returns PII."
- 'list_tenant_audit_acknowledgements read error type='
- 'db_read_failed:'
- 'Existence check for a specific logical acknowledgement.\nNEVER raises.'
- 'exists'
- 'acknowledgement_exists read error type='
- "Structural summary of the brokerage's acknowledgements.\nReturns counts by acknowledgement_type. NEVER raises.\nNEVER returns per-row payload."
- 'by_type'
- 'total'
- 'tenant_acknowledgement_summary read error type='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS177 — Durable tenant audit acknowledgement store (Supabase-backed v1).\n\nAppend-only durable backing for tenant audit acknowledgements.\nPersists to ``pas_tenant_audit_acknowledgements`` (proposal at\n``scripts/migrate_v25_tenant_audit_acknowledgements.sql``).\n\nDoctrine carried by every helper:\n\n* **Append-only.** This module exposes only INSERT + read\n  helpers. There is NO update helper, NO delete helper, NO\n  mutation surface anywhere.\n* **Closed actor_type + acknowledgement_type enums.** Mirror\n  the v25 CHECK constraints; service-layer validation refuses\n  anything outside the closed sets.\n* **Closed metadata + notes_token allow-lists.** The JSONB\n  payload is projected against ``ALLOWED_METADATA_KEYS`` at\n  write time; the ``notes_token`` + ``actor_id`` fields are\n  validated against the closed alphanumeric + dash +\n  underscore character set.\n* **No PII.** No phone / email / transcript / raw_payload /\n  signature / secret / env_value / callback_notes /\n  dedupe_key / raw_audit_metadata anywhere.\n* **No exceptions escape.** DB unavailable → structural\n  ``status="skipped"`` envelope. NEVER raises.\n* **Bounded pagination.** Hard caps in the read helpers.\n* **Brokerage scoped.** Every read and write requires a\n  brokerage_id; cross-brokerage attempts return failed\n  envelopes.\n* **Idempotency awareness.** Repeated ACK for the same\n  ``(brokerage_id, acknowledgement_type, audit_entry_id |\n  merkle_root_id)`` returns ``duplicate=True`` without\n  raising.\n\nPublic surface:\n\n  * ``ALLOWED_ACTOR_TYPES``\n  * ``ALLOWED_ACKNOWLEDGEMENT_TYPES``\n  * ``ALLOWED_METADATA_KEYS``\n  * ``record_tenant_audit_acknowledgement(...)``\n  * ``list_tenant_audit_acknowledgements(...)``\n  * ``tenant_acknowledgement_summary(...)``\n  * ``acknowledgement_exists(...)``\n')
              STORE_NAME               0 (__doc__)

 46           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 48           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 49           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (uuid)
              STORE_NAME               4 (uuid)

 50           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timezone'))
              IMPORT_NAME              5 (datetime)
              IMPORT_FROM              5 (datetime)
              STORE_NAME               5 (datetime)
              IMPORT_FROM              6 (timezone)
              STORE_NAME               6 (timezone)
              POP_TOP

 51           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              7 (typing)
              IMPORT_FROM              8 (Any)
              STORE_NAME               8 (Any)
              IMPORT_FROM              9 (Dict)
              STORE_NAME               9 (Dict)
              IMPORT_FROM             10 (List)
              STORE_NAME              10 (List)
              IMPORT_FROM             11 (Optional)
              STORE_NAME              11 (Optional)
              POP_TOP

 54           LOAD_NAME                3 (logging)
              LOAD_ATTR               24 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.tenant.audit_ack_store')
              CALL                     1
              STORE_NAME              13 (logger)

 57           LOAD_CONST               6 ('pas_tenant_audit_acknowledgements')
              STORE_NAME              14 (_TABLE)

 61           LOAD_CONST              61 (('TENANT', 'OPERATOR', 'ADMIN', 'SYSTEM'))
              STORE_NAME              15 (ALLOWED_ACTOR_TYPES)

 68           LOAD_CONST              62 (('AUDIT_ENTRY_VIEWED', 'AUDIT_WINDOW_ACKNOWLEDGED', 'MERKLE_ROOT_ACKNOWLEDGED', 'CHAIN_STATUS_VIEWED'))
              STORE_NAME              16 (ALLOWED_ACKNOWLEDGEMENT_TYPES)

 76           LOAD_CONST              63 (('event', 'chain_status', 'rows_in_window', 'warning_count', 'error_code', 'proof_generated', 'proof_valid', 'merkle_root_fingerprint'))
              STORE_NAME              17 (ALLOWED_METADATA_KEYS)

 90           LOAD_CONST               9 ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_')

 89           STORE_NAME              18 (_ALLOWED_TOKEN_CHARS)

 96           LOAD_SMALL_INT         200
              STORE_NAME              19 (_BROKERAGE_ID_MAX_LEN)

 97           LOAD_SMALL_INT         200
              STORE_NAME              20 (_ACTOR_ID_MAX_LEN)

 98           LOAD_SMALL_INT         200
              STORE_NAME              21 (_NOTES_TOKEN_MAX_LEN)

 99           LOAD_SMALL_INT         200
              STORE_NAME              22 (_AUDIT_ENTRY_ID_MAX_LEN)

100           LOAD_SMALL_INT         200
              STORE_NAME              23 (_MERKLE_ROOT_ID_MAX_LEN)

102           LOAD_CONST              10 (500)
              STORE_NAME              24 (_LIST_HARD_CAP)

103           LOAD_SMALL_INT          50
              STORE_NAME              25 (_DEFAULT_LIMIT)

109           LOAD_CONST              64 (('acknowledgement_id', 'brokerage_id', 'audit_entry_id', 'merkle_root_id', 'acknowledged_at', 'actor_type', 'actor_id', 'acknowledgement_type', 'notes_token', 'metadata'))
              STORE_NAME              26 (_STRUCTURAL_COLUMNS)

127           LOAD_CONST              65 ((None,))
              LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA21F0, file "app\services\tenant\tenant_audit_ack_store.py", line 127>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _now_dt at 0x0000018C179C3A50, file "app\services\tenant\tenant_audit_ack_store.py", line 127>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              27 (_now_dt)

135           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA2F10, file "app\services\tenant\tenant_audit_ack_store.py", line 135>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _iso at 0x0000018C18025A30, file "app\services\tenant\tenant_audit_ack_store.py", line 135>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_iso)

139           LOAD_CONST              23 (<code object _get_db_safe at 0x0000018C17FF1230, file "app\services\tenant\tenant_audit_ack_store.py", line 139>)
              MAKE_FUNCTION
              STORE_NAME              29 (_get_db_safe)

151           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\tenant\tenant_audit_ack_store.py", line 151>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object _bound_str_token at 0x0000018C179C3C30, file "app\services\tenant\tenant_audit_ack_store.py", line 151>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_bound_str_token)

166           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA31E0, file "app\services\tenant\tenant_audit_ack_store.py", line 166>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object _bound_brokerage_id at 0x0000018C17F96140, file "app\services\tenant\tenant_audit_ack_store.py", line 166>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_bound_brokerage_id)

175           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C18025E30, file "app\services\tenant\tenant_audit_ack_store.py", line 175>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object _bound_uuid_like at 0x0000018C17972D90, file "app\services\tenant\tenant_audit_ack_store.py", line 175>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_bound_uuid_like)

186           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\tenant\tenant_audit_ack_store.py", line 186>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object _project_metadata at 0x0000018C17FEDE30, file "app\services\tenant\tenant_audit_ack_store.py", line 186>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_project_metadata)

202           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA3960, file "app\services\tenant\tenant_audit_ack_store.py", line 202>)
              MAKE_FUNCTION
              LOAD_CONST              33 (<code object _project_row at 0x0000018C1796DBD0, file "app\services\tenant\tenant_audit_ack_store.py", line 202>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              34 (_project_row)

213           LOAD_CONST              34 ('duplicate')

216           LOAD_CONST              35 (False)

213           LOAD_CONST              36 ('ack_row')

217           LOAD_CONST               2 (None)

213           LOAD_CONST              37 ('warnings')

218           LOAD_CONST               2 (None)

213           LOAD_CONST               8 ('error_code')

219           LOAD_CONST               2 (None)

213           BUILD_MAP                4
              LOAD_CONST              38 (<code object __annotate__ at 0x0000018C18026330, file "app\services\tenant\tenant_audit_ack_store.py", line 213>)
              MAKE_FUNCTION
              LOAD_CONST              39 (<code object _safe_envelope at 0x0000018C1802C9B0, file "app\services\tenant\tenant_audit_ack_store.py", line 213>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              35 (_safe_envelope)

230           LOAD_CONST              11 ('brokerage_id')

233           LOAD_CONST               2 (None)

230           LOAD_CONST              40 ('rows')

234           LOAD_CONST               2 (None)

230           LOAD_CONST              41 ('count')

235           LOAD_SMALL_INT           0

230           LOAD_CONST              42 ('limit')

236           LOAD_NAME               25 (_DEFAULT_LIMIT)

230           LOAD_CONST              43 ('filter_ack_type')

237           LOAD_CONST               2 (None)

230           LOAD_CONST              37 ('warnings')

238           LOAD_CONST               2 (None)

230           LOAD_CONST               8 ('error_code')

239           LOAD_CONST               2 (None)

230           BUILD_MAP                7
              LOAD_CONST              44 (<code object __annotate__ at 0x0000018C18128360, file "app\services\tenant\tenant_audit_ack_store.py", line 230>)
              MAKE_FUNCTION
              LOAD_CONST              45 (<code object _list_envelope at 0x0000018C17FE1920, file "app\services\tenant\tenant_audit_ack_store.py", line 230>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              36 (_list_envelope)

253           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA3F00, file "app\services\tenant\tenant_audit_ack_store.py", line 253>)
              MAKE_FUNCTION
              LOAD_CONST              47 (<code object _clamp_limit at 0x0000018C17972550, file "app\services\tenant\tenant_audit_ack_store.py", line 253>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              37 (_clamp_limit)

265           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA1E30, file "app\services\tenant\tenant_audit_ack_store.py", line 265>)
              MAKE_FUNCTION
              LOAD_CONST              49 (<code object _validate_actor_type at 0x0000018C17FA32D0, file "app\services\tenant\tenant_audit_ack_store.py", line 265>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              38 (_validate_actor_type)

271           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C17FA3E10, file "app\services\tenant\tenant_audit_ack_store.py", line 271>)
              MAKE_FUNCTION
              LOAD_CONST              51 (<code object _validate_ack_type at 0x0000018C17FA3A50, file "app\services\tenant\tenant_audit_ack_store.py", line 271>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              39 (_validate_ack_type)

281           LOAD_CONST              14 ('actor_type')

285           LOAD_CONST               7 ('TENANT')

281           LOAD_CONST              15 ('actor_id')

286           LOAD_CONST               2 (None)

281           LOAD_CONST              12 ('audit_entry_id')

287           LOAD_CONST               2 (None)

281           LOAD_CONST              13 ('merkle_root_id')

288           LOAD_CONST               2 (None)

281           LOAD_CONST              17 ('notes_token')

289           LOAD_CONST               2 (None)

281           LOAD_CONST              18 ('metadata')

290           LOAD_CONST               2 (None)

281           LOAD_CONST              52 ('now')

291           LOAD_CONST               2 (None)

281           BUILD_MAP                7
              LOAD_CONST              53 (<code object __annotate__ at 0x0000018C18128250, file "app\services\tenant\tenant_audit_ack_store.py", line 281>)
              MAKE_FUNCTION
              LOAD_CONST              54 (<code object record_tenant_audit_acknowledgement at 0x0000018C182F6E80, file "app\services\tenant\tenant_audit_ack_store.py", line 281>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              40 (record_tenant_audit_acknowledgement)

425           LOAD_CONST              16 ('acknowledgement_type')

428           LOAD_CONST               2 (None)

425           LOAD_CONST              42 ('limit')

429           LOAD_NAME               25 (_DEFAULT_LIMIT)

425           BUILD_MAP                2
              LOAD_CONST              55 (<code object __annotate__ at 0x0000018C18024E30, file "app\services\tenant\tenant_audit_ack_store.py", line 425>)
              MAKE_FUNCTION
              LOAD_CONST              56 (<code object list_tenant_audit_acknowledgements at 0x0000018C17ED4910, file "app\services\tenant\tenant_audit_ack_store.py", line 425>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              41 (list_tenant_audit_acknowledgements)

488           LOAD_CONST              12 ('audit_entry_id')

492           LOAD_CONST               2 (None)

488           LOAD_CONST              13 ('merkle_root_id')

493           LOAD_CONST               2 (None)

488           BUILD_MAP                2
              LOAD_CONST              57 (<code object __annotate__ at 0x0000018C18025F30, file "app\services\tenant\tenant_audit_ack_store.py", line 488>)
              MAKE_FUNCTION
              LOAD_CONST              58 (<code object acknowledgement_exists at 0x0000018C17E881E0, file "app\services\tenant\tenant_audit_ack_store.py", line 488>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              42 (acknowledgement_exists)

555           LOAD_CONST              59 (<code object __annotate__ at 0x0000018C17FA30F0, file "app\services\tenant\tenant_audit_ack_store.py", line 555>)
              MAKE_FUNCTION
              LOAD_CONST              60 (<code object tenant_acknowledgement_summary at 0x0000018C182E4030, file "app\services\tenant\tenant_audit_ack_store.py", line 555>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              43 (tenant_acknowledgement_summary)

620           BUILD_LIST               0
              LOAD_CONST              66 (('ALLOWED_ACTOR_TYPES', 'ALLOWED_ACKNOWLEDGEMENT_TYPES', 'ALLOWED_METADATA_KEYS', 'record_tenant_audit_acknowledgement', 'list_tenant_audit_acknowledgements', 'tenant_acknowledgement_summary', 'acknowledgement_exists'))
              LIST_EXTEND              1
              STORE_NAME              44 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app\services\tenant\tenant_audit_ack_store.py", line 127>:
127           RESUME                   0
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

Disassembly of <code object _now_dt at 0x0000018C179C3A50, file "app\services\tenant\tenant_audit_ack_store.py", line 127>:
127           RESUME                   0

128           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (now)
              LOAD_GLOBAL              2 (datetime)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       78 (to L2)
              NOT_TAKEN

129           LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR                4 (tzinfo)
              POP_JUMP_IF_NOT_NONE    33 (to L1)
              NOT_TAKEN

130           LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR                7 (replace + NULL|self)
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              LOAD_CONST               1 (('tzinfo',))
              CALL_KW                  1
              RETURN_VALUE

131   L1:     LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR               13 (astimezone + NULL|self)
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              CALL                     1
              RETURN_VALUE

132   L2:     LOAD_GLOBAL              2 (datetime)
              LOAD_ATTR               14 (now)
              PUSH_NULL
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "app\services\tenant\tenant_audit_ack_store.py", line 135>:
135           RESUME                   0
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

Disassembly of <code object _iso at 0x0000018C18025A30, file "app\services\tenant\tenant_audit_ack_store.py", line 135>:
135           RESUME                   0

136           LOAD_FAST_BORROW         0 (dt)
              LOAD_ATTR                1 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object _get_db_safe at 0x0000018C17FF1230, file "app\services\tenant\tenant_audit_ack_store.py", line 139>:
 139           RESUME                   0

 140           NOP

 141   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 142           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 143           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 144   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 145           LOAD_CONST               2 ('tenant_audit_ack_store db client unavailable type=')

 146           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 145           BUILD_STRING             2

 144           CALL                     1
               POP_TOP

 148   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 143   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\tenant\tenant_audit_ack_store.py", line 151>:
151           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('max_len')
              LOAD_CONST               4 ('int')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Optional[str]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _bound_str_token at 0x0000018C179C3C30, file "app\services\tenant\tenant_audit_ack_store.py", line 151>:
151           RESUME                   0

154           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

155           LOAD_CONST               1 (None)
              RETURN_VALUE

156   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (s)

157           LOAD_FAST_BORROW         2 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

158           LOAD_CONST               1 (None)
              RETURN_VALUE

159   L2:     LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         2 (s)
              CALL                     1
              LOAD_FAST_BORROW         1 (max_len)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

160           LOAD_CONST               1 (None)
              RETURN_VALUE

161   L3:     LOAD_GLOBAL              8 (any)
              COPY                     1
              LOAD_COMMON_CONSTANT     4 (<built-in function any>)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE       28 (to L7)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 (<code object <genexpr> at 0x0000018C17FBFEE0, file "app\services\tenant\tenant_audit_ack_store.py", line 161>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         2 (s)
              GET_ITER
              CALL                     0
      L4:     FOR_ITER                12 (to L6)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L4)
      L5:     POP_ITER
              LOAD_CONST               3 (True)
              JUMP_FORWARD            17 (to L8)
      L6:     END_FOR
              POP_ITER
              LOAD_CONST               4 (False)
              JUMP_FORWARD            13 (to L8)
      L7:     PUSH_NULL
              LOAD_CONST               2 (<code object <genexpr> at 0x0000018C17FBFEE0, file "app\services\tenant\tenant_audit_ack_store.py", line 161>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         2 (s)
              GET_ITER
              CALL                     0
              CALL                     1
      L8:     TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L9)
              NOT_TAKEN

162           LOAD_CONST               1 (None)
              RETURN_VALUE

163   L9:     LOAD_FAST_BORROW         2 (s)
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C17FBFEE0, file "app\services\tenant\tenant_audit_ack_store.py", line 161>:
 161           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "app\services\tenant\tenant_audit_ack_store.py", line 166>:
166           RESUME                   0
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

Disassembly of <code object _bound_brokerage_id at 0x0000018C17F96140, file "app\services\tenant\tenant_audit_ack_store.py", line 166>:
166           RESUME                   0

167           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

168           LOAD_CONST               0 (None)
              RETURN_VALUE

169   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

170           LOAD_FAST_BORROW         1 (s)
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

171   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

172   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app\services\tenant\tenant_audit_ack_store.py", line 175>:
175           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('max_len')
              LOAD_CONST               4 ('int')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Optional[str]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _bound_uuid_like at 0x0000018C17972D90, file "app\services\tenant\tenant_audit_ack_store.py", line 175>:
175           RESUME                   0

178           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

179           LOAD_CONST               1 (None)
              RETURN_VALUE

180   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (s)

181           LOAD_FAST_BORROW         2 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         2 (s)
              CALL                     1
              LOAD_FAST_BORROW         1 (max_len)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

182   L2:     LOAD_CONST               1 (None)
              RETURN_VALUE

183   L3:     LOAD_FAST_BORROW         2 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\tenant\tenant_audit_ack_store.py", line 186>:
186           RESUME                   0
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

Disassembly of <code object _project_metadata at 0x0000018C17FEDE30, file "app\services\tenant\tenant_audit_ack_store.py", line 186>:
186           RESUME                   0

187           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (metadata)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

188           BUILD_MAP                0
              RETURN_VALUE

189   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

190           LOAD_GLOBAL              4 (ALLOWED_METADATA_KEYS)
              GET_ITER
      L2:     FOR_ITER               108 (to L8)
              STORE_FAST               2 (k)

191           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, metadata)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

192           JUMP_BACKWARD           11 (to L2)

193   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (metadata, k)
              BINARY_OP               26 ([])
              STORE_FAST               3 (v)

194           LOAD_FAST_BORROW         3 (v)
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

195   L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD           62 (to L2)

196   L5:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (v)
              LOAD_GLOBAL             12 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              JUMP_BACKWARD           86 (to L2)

197   L6:     LOAD_GLOBAL             15 (len + NULL)
              LOAD_FAST_BORROW         3 (v)
              CALL                     1
              LOAD_SMALL_INT         200
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_TRUE         3 (to L7)
              NOT_TAKEN
              JUMP_BACKWARD          104 (to L2)

198   L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD          110 (to L2)

190   L8:     END_FOR
              POP_ITER

199           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app\services\tenant\tenant_audit_ack_store.py", line 202>:
202           RESUME                   0
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

Disassembly of <code object _project_row at 0x0000018C1796DBD0, file "app\services\tenant\tenant_audit_ack_store.py", line 202>:
202           RESUME                   0

203           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

204           LOAD_CONST               0 (None)
              RETURN_VALUE

205   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

206           LOAD_GLOBAL              4 (_STRUCTURAL_COLUMNS)
              GET_ITER
      L2:     FOR_ITER                21 (to L4)
              STORE_FAST               2 (col)

207           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (col, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

208   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, col)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, col)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L2)

206   L4:     END_FOR
              POP_ITER

209           LOAD_GLOBAL              7 (_project_metadata + NULL)
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

210           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026330, file "app\services\tenant\tenant_audit_ack_store.py", line 213>:
213           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

215           LOAD_CONST               2 ('str')

213           LOAD_CONST               3 ('duplicate')

216           LOAD_CONST               4 ('bool')

213           LOAD_CONST               5 ('ack_row')

217           LOAD_CONST               6 ('Optional[Dict[str, Any]]')

213           LOAD_CONST               7 ('warnings')

218           LOAD_CONST               8 ('Optional[List[str]]')

213           LOAD_CONST               9 ('error_code')

219           LOAD_CONST              10 ('Optional[str]')

213           LOAD_CONST              11 ('return')

220           LOAD_CONST              12 ('Dict[str, Any]')

213           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C1802C9B0, file "app\services\tenant\tenant_audit_ack_store.py", line 213>:
213           RESUME                   0

222           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

223           LOAD_CONST               1 ('duplicate')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         1 (duplicate)
              CALL                     1

224           LOAD_CONST               2 ('ack_row')
              LOAD_FAST                2 (ack_row)

225           LOAD_CONST               3 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                3 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

226           LOAD_CONST               4 ('error_code')
              LOAD_FAST_BORROW         4 (error_code)

221           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18128360, file "app\services\tenant\tenant_audit_ack_store.py", line 230>:
230           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

232           LOAD_CONST               2 ('str')

230           LOAD_CONST               3 ('brokerage_id')

233           LOAD_CONST               4 ('Optional[str]')

230           LOAD_CONST               5 ('rows')

234           LOAD_CONST               6 ('Optional[List[Dict[str, Any]]]')

230           LOAD_CONST               7 ('count')

235           LOAD_CONST               8 ('int')

230           LOAD_CONST               9 ('limit')

236           LOAD_CONST               8 ('int')

230           LOAD_CONST              10 ('filter_ack_type')

237           LOAD_CONST               4 ('Optional[str]')

230           LOAD_CONST              11 ('warnings')

238           LOAD_CONST              12 ('Optional[List[str]]')

230           LOAD_CONST              13 ('error_code')

239           LOAD_CONST               4 ('Optional[str]')

230           LOAD_CONST              14 ('return')

240           LOAD_CONST              15 ('Dict[str, Any]')

230           BUILD_MAP                9
              RETURN_VALUE

Disassembly of <code object _list_envelope at 0x0000018C17FE1920, file "app\services\tenant\tenant_audit_ack_store.py", line 230>:
230           RESUME                   0

242           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

243           LOAD_CONST               1 ('brokerage_id')
              LOAD_FAST                1 (brokerage_id)

244           LOAD_CONST               2 ('rows')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                2 (rows)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

245           LOAD_CONST               3 ('count')
              LOAD_FAST                3 (count)

246           LOAD_CONST               4 ('limit')
              LOAD_FAST                4 (limit)

247           LOAD_CONST               5 ('filter_ack_type')
              LOAD_FAST                5 (filter_ack_type)

248           LOAD_CONST               6 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                6 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L2:     CALL                     1

249           LOAD_CONST               7 ('error_code')
              LOAD_FAST_BORROW         7 (error_code)

241           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "app\services\tenant\tenant_audit_ack_store.py", line 253>:
253           RESUME                   0
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

Disassembly of <code object _clamp_limit at 0x0000018C17972550, file "app\services\tenant\tenant_audit_ack_store.py", line 253>:
 253           RESUME                   0

 254           NOP

 255   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (v)

 258   L2:     LOAD_FAST                1 (v)
               LOAD_SMALL_INT           1
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 259           LOAD_SMALL_INT           1
               RETURN_VALUE

 260   L3:     LOAD_FAST                1 (v)
               LOAD_GLOBAL              8 (_LIST_HARD_CAP)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 261           LOAD_GLOBAL              8 (_LIST_HARD_CAP)
               RETURN_VALUE

 262   L4:     LOAD_FAST                1 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 256           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

 257           LOAD_GLOBAL              6 (_DEFAULT_LIMIT)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 256   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "app\services\tenant\tenant_audit_ack_store.py", line 265>:
265           RESUME                   0
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

Disassembly of <code object _validate_actor_type at 0x0000018C17FA32D0, file "app\services\tenant\tenant_audit_ack_store.py", line 265>:
265           RESUME                   0

266           LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              0 (ALLOWED_ACTOR_TYPES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

267           LOAD_CONST               0 ('invalid_actor_type')
              RETURN_VALUE

268   L1:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "app\services\tenant\tenant_audit_ack_store.py", line 271>:
271           RESUME                   0
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

Disassembly of <code object _validate_ack_type at 0x0000018C17FA3A50, file "app\services\tenant\tenant_audit_ack_store.py", line 271>:
271           RESUME                   0

272           LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              0 (ALLOWED_ACKNOWLEDGEMENT_TYPES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

273           LOAD_CONST               0 ('invalid_acknowledgement_type')
              RETURN_VALUE

274   L1:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18128250, file "app\services\tenant\tenant_audit_ack_store.py", line 281>:
281           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

283           LOAD_CONST               2 ('str')

281           LOAD_CONST               3 ('acknowledgement_type')

284           LOAD_CONST               2 ('str')

281           LOAD_CONST               4 ('actor_type')

285           LOAD_CONST               2 ('str')

281           LOAD_CONST               5 ('actor_id')

286           LOAD_CONST               6 ('Optional[str]')

281           LOAD_CONST               7 ('audit_entry_id')

287           LOAD_CONST               6 ('Optional[str]')

281           LOAD_CONST               8 ('merkle_root_id')

288           LOAD_CONST               6 ('Optional[str]')

281           LOAD_CONST               9 ('notes_token')

289           LOAD_CONST               6 ('Optional[str]')

281           LOAD_CONST              10 ('metadata')

290           LOAD_CONST              11 ('Optional[Dict[str, Any]]')

281           LOAD_CONST              12 ('now')

291           LOAD_CONST              13 ('Any')

281           LOAD_CONST              14 ('return')

292           LOAD_CONST              15 ('Dict[str, Any]')

281           BUILD_MAP               10
              RETURN_VALUE

Disassembly of <code object record_tenant_audit_acknowledgement at 0x0000018C182F6E80, file "app\services\tenant\tenant_audit_ack_store.py", line 281>:
 281            RESUME                   0

 306            LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               9 (bid)

 307            LOAD_FAST_BORROW         9 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L1)
                NOT_TAKEN

 308            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 309            LOAD_CONST               2 ('failed')
                LOAD_CONST               3 ('missing_brokerage_id')

 308            LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 311    L1:     LOAD_GLOBAL              5 (_validate_actor_type + NULL)
                LOAD_FAST_BORROW         2 (actor_type)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L2)
                NOT_TAKEN
                POP_TOP
                LOAD_GLOBAL              7 (_validate_ack_type + NULL)
                LOAD_FAST_BORROW         1 (acknowledgement_type)
                CALL                     1
        L2:     STORE_FAST              10 (err)

 312            LOAD_FAST_BORROW        10 (err)
                POP_JUMP_IF_NONE        14 (to L3)
                NOT_TAKEN

 313            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               2 ('failed')
                LOAD_FAST_BORROW        10 (err)
                LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 316    L3:     LOAD_CONST               1 (None)
                STORE_FAST              11 (bounded_actor_id)

 317            LOAD_FAST_BORROW         3 (actor_id)
                POP_JUMP_IF_NONE        34 (to L4)
                NOT_TAKEN

 318            LOAD_GLOBAL              9 (_bound_str_token + NULL)
                LOAD_FAST_BORROW         3 (actor_id)
                LOAD_GLOBAL             10 (_ACTOR_ID_MAX_LEN)
                CALL                     2
                STORE_FAST              11 (bounded_actor_id)

 319            LOAD_FAST_BORROW        11 (bounded_actor_id)
                POP_JUMP_IF_NOT_NONE    14 (to L4)
                NOT_TAKEN

 320            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 321            LOAD_CONST               2 ('failed')
                LOAD_CONST               5 ('invalid_actor_id')

 320            LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 324    L4:     LOAD_CONST               1 (None)
                STORE_FAST              12 (bounded_notes_token)

 325            LOAD_FAST_BORROW         6 (notes_token)
                POP_JUMP_IF_NONE        34 (to L5)
                NOT_TAKEN

 326            LOAD_GLOBAL              9 (_bound_str_token + NULL)
                LOAD_FAST_BORROW         6 (notes_token)
                LOAD_GLOBAL             12 (_NOTES_TOKEN_MAX_LEN)
                CALL                     2
                STORE_FAST              12 (bounded_notes_token)

 327            LOAD_FAST_BORROW        12 (bounded_notes_token)
                POP_JUMP_IF_NOT_NONE    14 (to L5)
                NOT_TAKEN

 328            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 329            LOAD_CONST               2 ('failed')
                LOAD_CONST               6 ('invalid_notes_token')

 328            LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 332    L5:     LOAD_FAST_BORROW         4 (audit_entry_id)
                POP_JUMP_IF_NONE        17 (to L6)
                NOT_TAKEN

 331            LOAD_GLOBAL             15 (_bound_uuid_like + NULL)
                LOAD_FAST_BORROW         4 (audit_entry_id)
                LOAD_GLOBAL             16 (_AUDIT_ENTRY_ID_MAX_LEN)
                CALL                     2
                JUMP_FORWARD             1 (to L7)

 332    L6:     LOAD_CONST               1 (None)

 331    L7:     STORE_FAST              13 (bounded_entry_id)

 334            LOAD_FAST_BORROW         5 (merkle_root_id)
                POP_JUMP_IF_NONE        17 (to L8)
                NOT_TAKEN

 333            LOAD_GLOBAL             15 (_bound_uuid_like + NULL)
                LOAD_FAST_BORROW         5 (merkle_root_id)
                LOAD_GLOBAL             18 (_MERKLE_ROOT_ID_MAX_LEN)
                CALL                     2
                JUMP_FORWARD             1 (to L9)

 334    L8:     LOAD_CONST               1 (None)

 333    L9:     STORE_FAST              14 (bounded_merkle_id)

 339            LOAD_FAST_BORROW         1 (acknowledgement_type)
                LOAD_CONST               7 ('AUDIT_ENTRY_VIEWED')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       18 (to L10)
                NOT_TAKEN
                LOAD_FAST_BORROW        13 (bounded_entry_id)
                POP_JUMP_IF_NOT_NONE    14 (to L10)
                NOT_TAKEN

 340            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 341            LOAD_CONST               2 ('failed')
                LOAD_CONST               8 ('missing_audit_entry_id')

 340            LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 343   L10:     LOAD_FAST_BORROW         1 (acknowledgement_type)
                LOAD_CONST              32 (('MERKLE_ROOT_ACKNOWLEDGED', 'AUDIT_WINDOW_ACKNOWLEDGED'))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       18 (to L11)
                NOT_TAKEN

 345            LOAD_FAST_BORROW        14 (bounded_merkle_id)
                POP_JUMP_IF_NOT_NONE    14 (to L11)
                NOT_TAKEN

 346            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 347            LOAD_CONST               2 ('failed')
                LOAD_CONST               9 ('missing_merkle_root_id')

 346            LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 350   L11:     LOAD_GLOBAL             21 (_project_metadata + NULL)
                LOAD_FAST_BORROW         7 (metadata)
                CALL                     1
                STORE_FAST              15 (md)

 352            LOAD_GLOBAL             23 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST              16 (db)

 353            LOAD_FAST_BORROW        16 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L12)
                NOT_TAKEN

 354            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 355            LOAD_CONST              10 ('skipped')

 356            LOAD_CONST              11 ('tenant_audit_ack_store_unavailable')
                BUILD_LIST               1

 357            LOAD_CONST              11 ('tenant_audit_ack_store_unavailable')

 354            LOAD_CONST              12 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 363   L12:     NOP

 365   L13:     LOAD_FAST_BORROW        16 (db)
                LOAD_ATTR               25 (table + NULL|self)
                LOAD_GLOBAL             26 (_TABLE)
                CALL                     1

 366            LOAD_ATTR               29 (select + NULL|self)
                LOAD_CONST              13 (',')
                LOAD_ATTR               31 (join + NULL|self)
                LOAD_GLOBAL             32 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 367            LOAD_ATTR               35 (eq + NULL|self)
                LOAD_CONST              14 ('brokerage_id')
                LOAD_FAST_BORROW         9 (bid)
                CALL                     2

 368            LOAD_ATTR               35 (eq + NULL|self)
                LOAD_CONST              15 ('acknowledgement_type')
                LOAD_FAST_BORROW         1 (acknowledgement_type)
                CALL                     2

 369            LOAD_ATTR               37 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 364            STORE_FAST              17 (query)

 371            LOAD_FAST_BORROW        13 (bounded_entry_id)
                POP_JUMP_IF_NONE        19 (to L14)
                NOT_TAKEN

 372            LOAD_FAST_BORROW        17 (query)
                LOAD_ATTR               35 (eq + NULL|self)
                LOAD_CONST              16 ('audit_entry_id')
                LOAD_FAST_BORROW        13 (bounded_entry_id)
                CALL                     2
                STORE_FAST              17 (query)

 373   L14:     LOAD_FAST_BORROW        14 (bounded_merkle_id)
                POP_JUMP_IF_NONE        19 (to L15)
                NOT_TAKEN

 374            LOAD_FAST_BORROW        17 (query)
                LOAD_ATTR               35 (eq + NULL|self)
                LOAD_CONST              17 ('merkle_root_id')
                LOAD_FAST_BORROW        14 (bounded_merkle_id)
                CALL                     2
                STORE_FAST              17 (query)

 375   L15:     LOAD_GLOBAL             39 (list + NULL)
                LOAD_GLOBAL             41 (getattr + NULL)
                LOAD_FAST_BORROW        17 (query)
                LOAD_ATTR               43 (execute + NULL|self)
                CALL                     0
                LOAD_CONST              18 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
       L16:     NOT_TAKEN
       L17:     POP_TOP
                BUILD_LIST               0
       L18:     CALL                     1
                STORE_FAST              18 (existing)

 383   L19:     LOAD_FAST_BORROW        18 (existing)
                TO_BOOL
                POP_JUMP_IF_FALSE       31 (to L20)
                NOT_TAKEN

 384            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 385            LOAD_CONST              20 ('ok')

 386            LOAD_CONST              21 (True)

 387            LOAD_GLOBAL             55 (_project_row + NULL)
                LOAD_FAST_BORROW        18 (existing)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1

 384            LOAD_CONST              22 (('status', 'duplicate', 'ack_row'))
                CALL_KW                  3
                RETURN_VALUE

 391   L20:     LOAD_GLOBAL             57 (_iso + NULL)
                LOAD_GLOBAL             59 (_now_dt + NULL)
                LOAD_FAST_BORROW         8 (now)
                CALL                     1
                CALL                     1
                STORE_FAST              20 (iso_now)

 393            LOAD_CONST              23 ('acknowledgement_id')
                LOAD_GLOBAL             61 (str + NULL)
                LOAD_GLOBAL             62 (uuid)
                LOAD_ATTR               64 (uuid4)
                PUSH_NULL
                CALL                     0
                CALL                     1

 394            LOAD_CONST              14 ('brokerage_id')
                LOAD_FAST_BORROW         9 (bid)

 395            LOAD_CONST              16 ('audit_entry_id')
                LOAD_FAST_BORROW        13 (bounded_entry_id)

 396            LOAD_CONST              17 ('merkle_root_id')
                LOAD_FAST_BORROW        14 (bounded_merkle_id)

 397            LOAD_CONST              24 ('acknowledged_at')
                LOAD_FAST_BORROW        20 (iso_now)

 398            LOAD_CONST              25 ('actor_type')
                LOAD_FAST_BORROW         2 (actor_type)

 399            LOAD_CONST              26 ('actor_id')
                LOAD_FAST_BORROW        11 (bounded_actor_id)

 400            LOAD_CONST              15 ('acknowledgement_type')
                LOAD_FAST_BORROW         1 (acknowledgement_type)

 401            LOAD_CONST              27 ('notes_token')
                LOAD_FAST_BORROW        12 (bounded_notes_token)

 402            LOAD_CONST              28 ('metadata')
                LOAD_FAST_BORROW        15 (md)

 392            BUILD_MAP               10
                STORE_FAST              21 (row)

 404            NOP

 405   L21:     LOAD_FAST_BORROW        16 (db)
                LOAD_ATTR               25 (table + NULL|self)
                LOAD_GLOBAL             26 (_TABLE)
                CALL                     1
                LOAD_ATTR               67 (insert + NULL|self)
                LOAD_FAST_BORROW        21 (row)
                CALL                     1
                LOAD_ATTR               43 (execute + NULL|self)
                CALL                     0
                STORE_FAST              22 (result)

 406            LOAD_GLOBAL             39 (list + NULL)
                LOAD_GLOBAL             41 (getattr + NULL)
                LOAD_FAST_BORROW        22 (result)
                LOAD_CONST              18 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L22)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L22:     CALL                     1
                STORE_FAST              23 (rows)

 407            LOAD_FAST_BORROW        23 (rows)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L25)
       L23:     NOT_TAKEN
       L24:     LOAD_GLOBAL             55 (_project_row + NULL)
                LOAD_FAST_BORROW        23 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                JUMP_FORWARD            10 (to L26)
       L25:     LOAD_GLOBAL             55 (_project_row + NULL)
                LOAD_FAST_BORROW        21 (row)
                CALL                     1
       L26:     STORE_FAST              24 (proj)

 408            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST              20 ('ok')
                LOAD_CONST              29 (False)
                LOAD_FAST_BORROW        24 (proj)
                LOAD_CONST              22 (('status', 'duplicate', 'ack_row'))
                CALL_KW                  3
       L27:     RETURN_VALUE

  --   L28:     PUSH_EXC_INFO

 376            LOAD_GLOBAL             44 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       57 (to L32)
                NOT_TAKEN
                STORE_FAST              19 (e)

 377   L29:     LOAD_GLOBAL             46 (logger)
                LOAD_ATTR               49 (warning + NULL|self)

 378            LOAD_CONST              19 ('record_tenant_audit_acknowledgement idempotency read error type=')

 379            LOAD_GLOBAL             51 (type + NULL)
                LOAD_FAST               19 (e)
                CALL                     1
                LOAD_ATTR               52 (__name__)
                FORMAT_SIMPLE

 378            BUILD_STRING             2

 377            CALL                     1
                POP_TOP

 381            BUILD_LIST               0
                STORE_FAST              18 (existing)
       L30:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              19 (e)
                DELETE_FAST             19 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 304 (to L19)

  --   L31:     LOAD_CONST               1 (None)
                STORE_FAST              19 (e)
                DELETE_FAST             19 (e)
                RERAISE                  1

 376   L32:     RERAISE                  0

  --   L33:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L34:     PUSH_EXC_INFO

 409            LOAD_GLOBAL             44 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L39)
                NOT_TAKEN
                STORE_FAST              19 (e)

 410   L35:     LOAD_GLOBAL             46 (logger)
                LOAD_ATTR               49 (warning + NULL|self)

 411            LOAD_CONST              30 ('record_tenant_audit_acknowledgement db error type=')

 412            LOAD_GLOBAL             51 (type + NULL)
                LOAD_FAST               19 (e)
                CALL                     1
                LOAD_ATTR               52 (__name__)
                FORMAT_SIMPLE

 411            BUILD_STRING             2

 410            CALL                     1
                POP_TOP

 414            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 415            LOAD_CONST              10 ('skipped')

 416            LOAD_CONST              31 ('db_write_failed:')
                LOAD_GLOBAL             51 (type + NULL)
                LOAD_FAST               19 (e)
                CALL                     1
                LOAD_ATTR               52 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 417            LOAD_CONST              11 ('tenant_audit_ack_store_unavailable')

 414            LOAD_CONST              12 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
       L36:     SWAP                     2
       L37:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              19 (e)
                DELETE_FAST             19 (e)
                RETURN_VALUE

  --   L38:     LOAD_CONST               1 (None)
                STORE_FAST              19 (e)
                DELETE_FAST             19 (e)
                RERAISE                  1

 409   L39:     RERAISE                  0

  --   L40:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L13 to L16 -> L28 [0]
  L17 to L19 -> L28 [0]
  L21 to L23 -> L34 [0]
  L24 to L27 -> L34 [0]
  L28 to L29 -> L33 [1] lasti
  L29 to L30 -> L31 [1] lasti
  L31 to L33 -> L33 [1] lasti
  L34 to L35 -> L40 [1] lasti
  L35 to L36 -> L38 [1] lasti
  L36 to L37 -> L40 [1] lasti
  L38 to L40 -> L40 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app\services\tenant\tenant_audit_ack_store.py", line 425>:
425           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

426           LOAD_CONST               2 ('str')

425           LOAD_CONST               3 ('acknowledgement_type')

428           LOAD_CONST               4 ('Optional[str]')

425           LOAD_CONST               5 ('limit')

429           LOAD_CONST               6 ('Any')

425           LOAD_CONST               7 ('return')

430           LOAD_CONST               8 ('Dict[str, Any]')

425           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object list_tenant_audit_acknowledgements at 0x0000018C17ED4910, file "app\services\tenant\tenant_audit_ack_store.py", line 425>:
 425            RESUME                   0

 433            LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               3 (bid)

 434            LOAD_FAST_BORROW         3 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L1)
                NOT_TAKEN

 435            LOAD_GLOBAL              3 (_list_envelope + NULL)

 436            LOAD_CONST               2 ('failed')

 437            LOAD_CONST               3 ('missing_brokerage_id')

 435            LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 439    L1:     LOAD_FAST_BORROW         1 (acknowledgement_type)
                POP_JUMP_IF_NONE        27 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (acknowledgement_type)
                LOAD_GLOBAL              4 (ALLOWED_ACKNOWLEDGEMENT_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       16 (to L2)
                NOT_TAKEN

 440            LOAD_GLOBAL              3 (_list_envelope + NULL)

 441            LOAD_CONST               2 ('failed')

 442            LOAD_FAST_BORROW         3 (bid)

 443            LOAD_FAST_BORROW         1 (acknowledgement_type)

 444            LOAD_CONST               5 ('invalid_acknowledgement_type')

 440            LOAD_CONST               6 (('status', 'brokerage_id', 'filter_ack_type', 'error_code'))
                CALL_KW                  4
                RETURN_VALUE

 446    L2:     LOAD_GLOBAL              7 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1
                STORE_FAST               4 (capped)

 447            LOAD_GLOBAL              9 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               5 (db)

 448            LOAD_FAST_BORROW         5 (db)
                POP_JUMP_IF_NOT_NONE    18 (to L3)
                NOT_TAKEN

 449            LOAD_GLOBAL              3 (_list_envelope + NULL)

 450            LOAD_CONST               7 ('skipped')
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (bid, capped)

 451            LOAD_FAST_BORROW         1 (acknowledgement_type)

 452            LOAD_CONST               8 ('tenant_audit_ack_store_unavailable')
                BUILD_LIST               1

 453            LOAD_CONST               8 ('tenant_audit_ack_store_unavailable')

 449            LOAD_CONST               9 (('status', 'brokerage_id', 'limit', 'filter_ack_type', 'warnings', 'error_code'))
                CALL_KW                  6
                RETURN_VALUE

 455    L3:     NOP

 457    L4:     LOAD_FAST_BORROW         5 (db)
                LOAD_ATTR               11 (table + NULL|self)
                LOAD_GLOBAL             12 (_TABLE)
                CALL                     1

 458            LOAD_ATTR               15 (select + NULL|self)
                LOAD_CONST              10 (',')
                LOAD_ATTR               17 (join + NULL|self)
                LOAD_GLOBAL             18 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 459            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST              11 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)
                CALL                     2

 460            LOAD_ATTR               23 (order + NULL|self)
                LOAD_CONST              12 ('acknowledged_at')
                LOAD_CONST              13 (True)
                LOAD_CONST              14 (('desc',))
                CALL_KW                  2

 461            LOAD_ATTR               25 (limit + NULL|self)
                LOAD_FAST_BORROW         4 (capped)
                CALL                     1

 456            STORE_FAST               6 (query)

 463            LOAD_FAST_BORROW         1 (acknowledgement_type)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L7)
        L5:     NOT_TAKEN

 464    L6:     LOAD_FAST_BORROW         6 (query)
                LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST              15 ('acknowledgement_type')
                LOAD_FAST_BORROW         1 (acknowledgement_type)
                CALL                     2
                STORE_FAST               6 (query)

 465    L7:     LOAD_FAST_BORROW         6 (query)
                LOAD_ATTR               27 (execute + NULL|self)
                CALL                     0
                STORE_FAST               7 (result)

 466            LOAD_GLOBAL             29 (list + NULL)
                LOAD_GLOBAL             31 (getattr + NULL)
                LOAD_FAST_BORROW         7 (result)
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
                STORE_FAST               8 (rows)

 467            LOAD_CONST              17 (<code object <genexpr> at 0x0000018C18128470, file "app\services\tenant\tenant_audit_ack_store.py", line 467>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         8 (rows)
                GET_ITER
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      9 (p)
                SWAP                     2
       L11:     BUILD_LIST               0
                SWAP                     2
       L12:     FOR_ITER                10 (to L15)
                STORE_FAST_LOAD_FAST   153 (p, p)
       L13:     POP_JUMP_IF_NOT_NONE     3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD            8 (to L12)
       L14:     LOAD_FAST_BORROW         9 (p)
                LIST_APPEND              2
                JUMP_BACKWARD           12 (to L12)
       L15:     END_FOR
                POP_ITER
       L16:     STORE_FAST              10 (projected)
                STORE_FAST               9 (p)

 468            LOAD_GLOBAL              3 (_list_envelope + NULL)

 469            LOAD_CONST              18 ('ok')

 470            LOAD_FAST_BORROW         3 (bid)

 471            LOAD_FAST_BORROW        10 (projected)
                LOAD_GLOBAL             33 (len + NULL)
                LOAD_FAST_BORROW        10 (projected)
                CALL                     1

 472            LOAD_FAST_BORROW         4 (capped)

 473            LOAD_FAST_BORROW         1 (acknowledgement_type)

 468            LOAD_CONST              19 (('status', 'brokerage_id', 'rows', 'count', 'limit', 'filter_ack_type'))
                CALL_KW                  6
       L17:     RETURN_VALUE

  --   L18:     SWAP                     2
                POP_TOP

 467            SWAP                     2
                STORE_FAST               9 (p)
                RERAISE                  0

  --   L19:     PUSH_EXC_INFO

 475            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       93 (to L24)
                NOT_TAKEN
                STORE_FAST              11 (e)

 476   L20:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 477            LOAD_CONST              20 ('list_tenant_audit_acknowledgements read error type=')

 478            LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE

 477            BUILD_STRING             2

 476            CALL                     1
                POP_TOP

 480            LOAD_GLOBAL              3 (_list_envelope + NULL)

 481            LOAD_CONST               7 ('skipped')
                LOAD_FAST_LOAD_FAST     52 (bid, capped)

 482            LOAD_FAST                1 (acknowledgement_type)

 483            LOAD_CONST              21 ('db_read_failed:')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 484            LOAD_CONST               8 ('tenant_audit_ack_store_unavailable')

 480            LOAD_CONST               9 (('status', 'brokerage_id', 'limit', 'filter_ack_type', 'warnings', 'error_code'))
                CALL_KW                  6
       L21:     SWAP                     2
       L22:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RETURN_VALUE

  --   L23:     LOAD_CONST               1 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 475   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L19 [0]
  L6 to L8 -> L19 [0]
  L9 to L11 -> L19 [0]
  L11 to L13 -> L18 [2]
  L14 to L16 -> L18 [2]
  L16 to L17 -> L19 [0]
  L18 to L19 -> L19 [0]
  L19 to L20 -> L25 [1] lasti
  L20 to L21 -> L23 [1] lasti
  L21 to L22 -> L25 [1] lasti
  L23 to L25 -> L25 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C18128470, file "app\services\tenant\tenant_audit_ack_store.py", line 467>:
 467           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (_project_row + NULL)
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

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "app\services\tenant\tenant_audit_ack_store.py", line 488>:
488           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

490           LOAD_CONST               2 ('str')

488           LOAD_CONST               3 ('acknowledgement_type')

491           LOAD_CONST               2 ('str')

488           LOAD_CONST               4 ('audit_entry_id')

492           LOAD_CONST               5 ('Optional[str]')

488           LOAD_CONST               6 ('merkle_root_id')

493           LOAD_CONST               5 ('Optional[str]')

488           LOAD_CONST               7 ('return')

494           LOAD_CONST               8 ('Dict[str, Any]')

488           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object acknowledgement_exists at 0x0000018C17E881E0, file "app\services\tenant\tenant_audit_ack_store.py", line 488>:
 488            RESUME                   0

 497            LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               4 (bid)

 498            LOAD_FAST_BORROW         4 (bid)
                POP_JUMP_IF_NOT_NONE    11 (to L1)
                NOT_TAKEN

 500            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 501            LOAD_CONST               4 ('exists')
                LOAD_CONST               5 (False)

 502            LOAD_CONST               6 ('error_code')
                LOAD_CONST               7 ('missing_brokerage_id')

 503            LOAD_CONST               8 ('warnings')
                BUILD_LIST               0

 499            BUILD_MAP                4
                RETURN_VALUE

 505    L1:     LOAD_FAST_BORROW         1 (acknowledgement_type)
                LOAD_GLOBAL              2 (ALLOWED_ACKNOWLEDGEMENT_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       11 (to L2)
                NOT_TAKEN

 507            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 508            LOAD_CONST               4 ('exists')
                LOAD_CONST               5 (False)

 509            LOAD_CONST               6 ('error_code')
                LOAD_CONST               9 ('invalid_acknowledgement_type')

 510            LOAD_CONST               8 ('warnings')
                BUILD_LIST               0

 506            BUILD_MAP                4
                RETURN_VALUE

 513    L2:     LOAD_FAST_BORROW         2 (audit_entry_id)
                POP_JUMP_IF_NONE        17 (to L3)
                NOT_TAKEN

 512            LOAD_GLOBAL              5 (_bound_uuid_like + NULL)
                LOAD_FAST_BORROW         2 (audit_entry_id)
                LOAD_GLOBAL              6 (_AUDIT_ENTRY_ID_MAX_LEN)
                CALL                     2
                JUMP_FORWARD             1 (to L4)

 513    L3:     LOAD_CONST               1 (None)

 512    L4:     STORE_FAST               5 (bounded_entry_id)

 515            LOAD_FAST_BORROW         3 (merkle_root_id)
                POP_JUMP_IF_NONE        17 (to L5)
                NOT_TAKEN

 514            LOAD_GLOBAL              5 (_bound_uuid_like + NULL)
                LOAD_FAST_BORROW         3 (merkle_root_id)
                LOAD_GLOBAL              8 (_MERKLE_ROOT_ID_MAX_LEN)
                CALL                     2
                JUMP_FORWARD             1 (to L6)

 515    L5:     LOAD_CONST               1 (None)

 514    L6:     STORE_FAST               6 (bounded_merkle_id)

 516            LOAD_GLOBAL             11 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               7 (db)

 517            LOAD_FAST_BORROW         7 (db)
                POP_JUMP_IF_NOT_NONE    12 (to L7)
                NOT_TAKEN

 519            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('skipped')

 520            LOAD_CONST               4 ('exists')
                LOAD_CONST               5 (False)

 521            LOAD_CONST               8 ('warnings')
                LOAD_CONST              11 ('tenant_audit_ack_store_unavailable')
                BUILD_LIST               1

 522            LOAD_CONST               6 ('error_code')
                LOAD_CONST              11 ('tenant_audit_ack_store_unavailable')

 518            BUILD_MAP                4
                RETURN_VALUE

 524    L7:     NOP

 526    L8:     LOAD_FAST_BORROW         7 (db)
                LOAD_ATTR               13 (table + NULL|self)
                LOAD_GLOBAL             14 (_TABLE)
                CALL                     1

 527            LOAD_ATTR               17 (select + NULL|self)
                LOAD_CONST              12 ('acknowledgement_id')
                CALL                     1

 528            LOAD_ATTR               19 (eq + NULL|self)
                LOAD_CONST              13 ('brokerage_id')
                LOAD_FAST_BORROW         4 (bid)
                CALL                     2

 529            LOAD_ATTR               19 (eq + NULL|self)
                LOAD_CONST              14 ('acknowledgement_type')
                LOAD_FAST_BORROW         1 (acknowledgement_type)
                CALL                     2

 530            LOAD_ATTR               21 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 525            STORE_FAST               8 (query)

 532            LOAD_FAST_BORROW         5 (bounded_entry_id)
                POP_JUMP_IF_NONE        19 (to L9)
                NOT_TAKEN

 533            LOAD_FAST_BORROW         8 (query)
                LOAD_ATTR               19 (eq + NULL|self)
                LOAD_CONST              15 ('audit_entry_id')
                LOAD_FAST_BORROW         5 (bounded_entry_id)
                CALL                     2
                STORE_FAST               8 (query)

 534    L9:     LOAD_FAST_BORROW         6 (bounded_merkle_id)
                POP_JUMP_IF_NONE        19 (to L10)
                NOT_TAKEN

 535            LOAD_FAST_BORROW         8 (query)
                LOAD_ATTR               19 (eq + NULL|self)
                LOAD_CONST              16 ('merkle_root_id')
                LOAD_FAST_BORROW         6 (bounded_merkle_id)
                CALL                     2
                STORE_FAST               8 (query)

 536   L10:     LOAD_GLOBAL             23 (list + NULL)
                LOAD_GLOBAL             25 (getattr + NULL)
                LOAD_FAST_BORROW         8 (query)
                LOAD_ATTR               27 (execute + NULL|self)
                CALL                     0
                LOAD_CONST              17 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                BUILD_LIST               0
       L13:     CALL                     1
                STORE_FAST               9 (rows)

 538            LOAD_CONST               2 ('status')
                LOAD_CONST              18 ('ok')

 539            LOAD_CONST               4 ('exists')
                LOAD_GLOBAL             29 (bool + NULL)
                LOAD_FAST_BORROW         9 (rows)
                CALL                     1

 540            LOAD_CONST               8 ('warnings')
                BUILD_LIST               0

 541            LOAD_CONST               6 ('error_code')
                LOAD_CONST               1 (None)

 537            BUILD_MAP                4
       L14:     RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 543            LOAD_GLOBAL             30 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       87 (to L20)
                NOT_TAKEN
                STORE_FAST              10 (e)

 544   L16:     LOAD_GLOBAL             32 (logger)
                LOAD_ATTR               35 (warning + NULL|self)

 545            LOAD_CONST              19 ('acknowledgement_exists read error type=')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 544            CALL                     1
                POP_TOP

 548            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('skipped')

 549            LOAD_CONST               4 ('exists')
                LOAD_CONST               5 (False)

 550            LOAD_CONST               8 ('warnings')
                LOAD_CONST              20 ('db_read_failed:')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 551            LOAD_CONST               6 ('error_code')
                LOAD_CONST              11 ('tenant_audit_ack_store_unavailable')

 547            BUILD_MAP                4
       L17:     SWAP                     2
       L18:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RETURN_VALUE

  --   L19:     LOAD_CONST               1 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 543   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L8 to L11 -> L15 [0]
  L12 to L14 -> L15 [0]
  L15 to L16 -> L21 [1] lasti
  L16 to L17 -> L19 [1] lasti
  L17 to L18 -> L21 [1] lasti
  L19 to L21 -> L21 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "app\services\tenant\tenant_audit_ack_store.py", line 555>:
555           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

556           LOAD_CONST               2 ('str')

555           LOAD_CONST               3 ('return')

557           LOAD_CONST               4 ('Dict[str, Any]')

555           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object tenant_acknowledgement_summary at 0x0000018C182E4030, file "app\services\tenant\tenant_audit_ack_store.py", line 555>:
 555            RESUME                   0

 561            LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               1 (bid)

 562            LOAD_FAST_BORROW         1 (bid)
                POP_JUMP_IF_NOT_NONE    15 (to L1)
                NOT_TAKEN

 564            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 565            LOAD_CONST               4 ('brokerage_id')
                LOAD_CONST               1 (None)

 566            LOAD_CONST               5 ('by_type')
                BUILD_MAP                0

 567            LOAD_CONST               6 ('total')
                LOAD_SMALL_INT           0

 568            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 569            LOAD_CONST               8 ('error_code')
                LOAD_CONST               9 ('missing_brokerage_id')

 563            BUILD_MAP                6
                RETURN_VALUE

 571    L1:     LOAD_GLOBAL              3 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               2 (db)

 572            LOAD_FAST_BORROW         2 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L2)
                NOT_TAKEN

 574            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('skipped')

 575            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         1 (bid)

 576            LOAD_CONST               5 ('by_type')
                BUILD_MAP                0

 577            LOAD_CONST               6 ('total')
                LOAD_SMALL_INT           0

 578            LOAD_CONST               7 ('warnings')
                LOAD_CONST              11 ('tenant_audit_ack_store_unavailable')
                BUILD_LIST               1

 579            LOAD_CONST               8 ('error_code')
                LOAD_CONST              11 ('tenant_audit_ack_store_unavailable')

 573            BUILD_MAP                6
                RETURN_VALUE

 581    L2:     NOP

 583    L3:     LOAD_FAST_BORROW         2 (db)
                LOAD_ATTR                5 (table + NULL|self)
                LOAD_GLOBAL              6 (_TABLE)
                CALL                     1

 584            LOAD_ATTR                9 (select + NULL|self)
                LOAD_CONST              12 ('acknowledgement_type')
                CALL                     1

 585            LOAD_ATTR               11 (eq + NULL|self)
                LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         1 (bid)
                CALL                     2

 586            LOAD_ATTR               13 (limit + NULL|self)
                LOAD_GLOBAL             14 (_LIST_HARD_CAP)
                CALL                     1

 587            LOAD_ATTR               17 (execute + NULL|self)
                CALL                     0

 582            STORE_FAST               3 (result)

 589            LOAD_GLOBAL             19 (list + NULL)
                LOAD_GLOBAL             21 (getattr + NULL)
                LOAD_FAST_BORROW         3 (result)
                LOAD_CONST              13 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
        L4:     NOT_TAKEN
        L5:     POP_TOP
                BUILD_LIST               0
        L6:     CALL                     1
                STORE_FAST               4 (rows)

 603    L7:     BUILD_MAP                0
                STORE_FAST               6 (by_type)

 604            LOAD_FAST                4 (rows)
                GET_ITER
        L8:     FOR_ITER               108 (to L12)
                STORE_FAST               7 (r)

 605            LOAD_GLOBAL             33 (isinstance + NULL)
                LOAD_FAST                7 (r)
                LOAD_GLOBAL             34 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN

 606            JUMP_BACKWARD           27 (to L8)

 607    L9:     LOAD_FAST                7 (r)
                LOAD_ATTR               37 (get + NULL|self)
                LOAD_CONST              12 ('acknowledgement_type')
                CALL                     1
                STORE_FAST               8 (t)

 608            LOAD_GLOBAL             33 (isinstance + NULL)
                LOAD_FAST                8 (t)
                LOAD_GLOBAL             38 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           68 (to L8)
       L10:     LOAD_FAST                8 (t)
                LOAD_GLOBAL             40 (ALLOWED_ACKNOWLEDGEMENT_TYPES)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                JUMP_BACKWARD           81 (to L8)

 609   L11:     LOAD_FAST                6 (by_type)
                LOAD_ATTR               37 (get + NULL|self)
                LOAD_FAST                8 (t)
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST_LOAD_FAST    104 (by_type, t)
                STORE_SUBSCR
                JUMP_BACKWARD          110 (to L8)

 604   L12:     END_FOR
                POP_ITER

 611            LOAD_CONST               2 ('status')
                LOAD_CONST              16 ('ok')

 612            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                1 (bid)

 613            LOAD_CONST               5 ('by_type')
                LOAD_FAST                6 (by_type)

 614            LOAD_CONST               6 ('total')
                LOAD_GLOBAL             43 (sum + NULL)
                LOAD_FAST                6 (by_type)
                LOAD_ATTR               45 (values + NULL|self)
                CALL                     0
                CALL                     1

 615            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 616            LOAD_CONST               8 ('error_code')
                LOAD_CONST               1 (None)

 610            BUILD_MAP                6
                RETURN_VALUE

  --   L13:     PUSH_EXC_INFO

 590            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L18)
                NOT_TAKEN
                STORE_FAST               5 (e)

 591   L14:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 592            LOAD_CONST              14 ('tenant_acknowledgement_summary read error type=')

 593            LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 592            BUILD_STRING             2

 591            CALL                     1
                POP_TOP

 596            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('skipped')

 597            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                1 (bid)

 598            LOAD_CONST               5 ('by_type')
                BUILD_MAP                0

 599            LOAD_CONST               6 ('total')
                LOAD_SMALL_INT           0

 600            LOAD_CONST               7 ('warnings')
                LOAD_CONST              15 ('db_read_failed:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 601            LOAD_CONST               8 ('error_code')
                LOAD_CONST              11 ('tenant_audit_ack_store_unavailable')

 595            BUILD_MAP                6
       L15:     SWAP                     2
       L16:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RETURN_VALUE

  --   L17:     LOAD_CONST               1 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 590   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L13 [0]
  L5 to L7 -> L13 [0]
  L13 to L14 -> L19 [1] lasti
  L14 to L15 -> L17 [1] lasti
  L15 to L16 -> L19 [1] lasti
  L17 to L19 -> L19 [1] lasti
```
