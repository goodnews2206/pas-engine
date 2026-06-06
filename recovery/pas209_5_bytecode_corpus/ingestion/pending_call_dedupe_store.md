# ingestion/pending_call_dedupe_store

- **pyc:** `app\services\ingestion\__pycache__\pending_call_dedupe_store.cpython-314.pyc`
- **expected source path (absent):** `app\services\ingestion/pending_call_dedupe_store.py`
- **co_filename (from bytecode):** `app/services/ingestion/pending_call_dedupe_store.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** ingestion

## Module docstring

```
PAS171 — Durable pending-call dedupe store (Supabase-backed v1).

Multi-replica-safe, restart-safe replacement for the PAS170
process-local registry in
:mod:`app.services.ingestion.pending_call_dedupe`. The
process-local registry remains in place as a fallback when the
durable store is unavailable (table missing, DB unreachable,
client unconfigured).

Mirrors the PAS166 ↔ PAS165 pattern from
:mod:`app.services.ingestion.email_dedupe_store`. PAS171's job
is the parallel surface for *pending calls*.

Doctrine carried by every helper here:

* ``brokerage_id`` is REQUIRED on every read and write.
  NEVER read from any payload — resolved from auth in the
  calling layer and passed in as a kwarg.
* The dedupe key is stored in the table but is NEVER
  returned in the public envelope, NEVER logged, NEVER
  echoed in events.
* No raw phone / email / name / subject / body / property /
  notes / transcript columns. The table schema (proposal at
  ``scripts/migrate_v18_pending_call_dedupe.sql``) is
  structurally pinned to the dedupe key + tenant scope +
  closed source enum + lifecycle timestamps + a
  pending-call backlink.
* No exception escapes any public helper. DB unreachable /
  table missing / unique-constraint conflict are all
  surfaced as structural envelopes; the caller can then
  fall back to the PAS170 process-local registry.
* No Gmail / Google / inbox / OAuth / IMAP / POP3 import.
  No external vendor SDK. No embeddings / vector libs.
* Default policy is "enabled if Supabase reachable" —
  explicit OFF requires a literal opt-out token, matching
  the PAS166 doctrine.

Public surface:

  * ``durable_pending_call_dedupe_enabled(config_or_env=None)``
  * ``register_durable_pending_call_dedupe(...)``
  * ``is_duplicate_durable_pending_call_dedupe(...)``
  * ``mark_durable_pending_call_duplicate_seen(...)``
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `datetime`, `get_supabase`, `logging`, `os`, `timedelta`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_ttl_hours`, `_get_db_safe`, `_is_unique_violation`, `_iso`, `_now_dt`, `_safe_envelope`, `_validate_inputs`, `durable_pending_call_dedupe_enabled`, `is_duplicate_durable_pending_call_dedupe`, `mark_durable_pending_call_duplicate_seen`, `register_durable_pending_call_dedupe`

## Env-key candidates

`PAS_PENDING_CALL_DEDUPE_DURABLE_ENABLED`

## String constants (redacted where noted)

- '\nPAS171 — Durable pending-call dedupe store (Supabase-backed v1).\n\nMulti-replica-safe, restart-safe replacement for the PAS170\nprocess-local registry in\n:mod:`app.services.ingestion.pending_call_dedupe`. The\nprocess-local registry remains in place as a fallback when the\ndurable store is unavailable (table missing, DB unreachable,\nclient unconfigured).\n\nMirrors the PAS166 ↔ PAS165 pattern from\n:mod:`app.services.ingestion.email_dedupe_store`. PAS171\'s job\nis the parallel surface for *pending calls*.\n\nDoctrine carried by every helper here:\n\n* ``brokerage_id`` is REQUIRED on every read and write.\n  NEVER read from any payload — resolved from auth in the\n  calling layer and passed in as a kwarg.\n* The dedupe key is stored in the table but is NEVER\n  returned in the public envelope, NEVER logged, NEVER\n  echoed in events.\n* No raw phone / email / name / subject / body / property /\n  notes / transcript columns. The table schema (proposal at\n  ``scripts/migrate_v18_pending_call_dedupe.sql``) is\n  structurally pinned to the dedupe key + tenant scope +\n  closed source enum + lifecycle timestamps + a\n  pending-call backlink.\n* No exception escapes any public helper. DB unreachable /\n  table missing / unique-constraint conflict are all\n  surfaced as structural envelopes; the caller can then\n  fall back to the PAS170 process-local registry.\n* No Gmail / Google / inbox / OAuth / IMAP / POP3 import.\n  No external vendor SDK. No embeddings / vector libs.\n* Default policy is "enabled if Supabase reachable" —\n  explicit OFF requires a literal opt-out token, matching\n  the PAS166 doctrine.\n\nPublic surface:\n\n  * ``durable_pending_call_dedupe_enabled(config_or_env=None)``\n  * ``register_durable_pending_call_dedupe(...)``\n  * ``is_duplicate_durable_pending_call_dedupe(...)``\n  * ``mark_durable_pending_call_duplicate_seen(...)``\n'
- 'pas.ingestion.pending_call_dedupe_store'
- 'pas_pending_call_dedupe'
- 'PAS_PENDING_CALL_DEDUPE_DURABLE_ENABLED'
- 'duplicate'
- 'warnings'
- 'error_code'
- 'pending_call_id'
- 'ttl_hours'
- 'now'
- 'Any'
- 'return'
- 'datetime'
- '+00:00'
- 'str'
- 'seconds'
- 'value'
- 'int'
- 'Lazy resolver for the Supabase client. NEVER raises.'
- 'pending_call_dedupe_store db client unavailable type='
- 'config_or_env'
- 'bool'
- 'Resolve whether durable pending-call dedupe is enabled.\n\nPrecedence (first match wins):\n\n1. ``config_or_env`` — if it is a dict carrying the key\n   ``pending_call_dedupe_durable_enabled`` (literal\n   True / False), that wins. Per-brokerage rows may\n   opt in or out without touching the env.\n2. ``PAS_PENDING_CALL_DEDUPE_DURABLE_ENABLED``: explicit\n   "false" / "0" / "no" / "off" / "disabled" disables.\n   Anything else (including unset) defaults to ENABLED.\n3. Default: ENABLED (the safest default for pilot\n   brokerages — restart / replica safety is the whole\n   point of PAS171).\n\nNEVER raises.\n'
- 'pending_call_dedupe_durable_enabled'
- 'status'
- 'Optional[List[str]]'
- 'Optional[str]'
- 'Dict[str, Any]'
- 'brokerage_id'
- 'dedupe_key'
- 'source'
- 'Return a structural error code if any input is invalid.\nNEVER echoes the offending value.'
- 'missing_brokerage_id'
- 'missing_dedupe_key'
- 'invalid_dedupe_key_shape'
- '0123456789abcdef'
- 'invalid_source'
- 'exc'
- 'BaseException'
- 'Best-effort detection of a Postgres / Supabase unique-\nconstraint violation. The supabase-py client exposes the\nPG error code via different shapes depending on version;\nwe look for the canonical SQLSTATE 23505 in any string-\nish attribute on the exception. NEVER raises.'
- '23505'
- 'duplicate key value violates unique constraint'
- 'already exists'
- 'Insert ``dedupe_key`` into the durable store, scoped to\n``brokerage_id``. Returns a structural envelope.\n\nOutcomes:\n\n* ``status="ok", duplicate=False`` — fresh insert.\n* ``status="ok", duplicate=True``  — unique-constraint\n  conflict; the caller should treat as "already seen".\n* ``status="warning"`` — DB unavailable / table missing.\n  The caller MUST fall back to the PAS170 process-local\n  registry.\n* ``status="failed"`` — input validation error.\n\nNEVER raises. NEVER returns the dedupe key. NEVER returns\nraw lead fields.\n'
- 'failed'
- 'warning'
- 'durable_pending_call_dedupe_unavailable'
- 'created_at'
- 'expires_at'
- 'first_seen_pending_call_id'
- 'register_durable_pending_call_dedupe db error type='
- 'db_write_failed:'
- 'Check whether ``dedupe_key`` exists in the durable store\nfor ``brokerage_id`` AND has not yet expired.\n\nReturns a structural envelope. NEVER raises. NEVER returns\nthe dedupe key.\n'
- 'dedupe_key, expires_at'
- 'data'
- 'is_duplicate_durable_pending_call_dedupe db error type='
- 'db_read_failed:'
- 'Increment the ``duplicate_count`` on the existing row\nfor ``dedupe_key`` (scoped to ``brokerage_id``) and stamp\n``last_duplicate_at``.\n\nPerforms a read-then-write so the increment is structural;\na future migration may add a SQL function for atomic\nincrement.\n\nReturns a structural envelope. NEVER raises. NEVER returns\nthe dedupe key.\n'
- 'duplicate_count'
- 'pending_call_dedupe_row_not_found'
- 'last_duplicate_at'
- 'pending_call_dedupe_update_returned_no_rows'
- 'mark_durable_pending_call_duplicate_seen db error type='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS171 — Durable pending-call dedupe store (Supabase-backed v1).\n\nMulti-replica-safe, restart-safe replacement for the PAS170\nprocess-local registry in\n:mod:`app.services.ingestion.pending_call_dedupe`. The\nprocess-local registry remains in place as a fallback when the\ndurable store is unavailable (table missing, DB unreachable,\nclient unconfigured).\n\nMirrors the PAS166 ↔ PAS165 pattern from\n:mod:`app.services.ingestion.email_dedupe_store`. PAS171\'s job\nis the parallel surface for *pending calls*.\n\nDoctrine carried by every helper here:\n\n* ``brokerage_id`` is REQUIRED on every read and write.\n  NEVER read from any payload — resolved from auth in the\n  calling layer and passed in as a kwarg.\n* The dedupe key is stored in the table but is NEVER\n  returned in the public envelope, NEVER logged, NEVER\n  echoed in events.\n* No raw phone / email / name / subject / body / property /\n  notes / transcript columns. The table schema (proposal at\n  ``scripts/migrate_v18_pending_call_dedupe.sql``) is\n  structurally pinned to the dedupe key + tenant scope +\n  closed source enum + lifecycle timestamps + a\n  pending-call backlink.\n* No exception escapes any public helper. DB unreachable /\n  table missing / unique-constraint conflict are all\n  surfaced as structural envelopes; the caller can then\n  fall back to the PAS170 process-local registry.\n* No Gmail / Google / inbox / OAuth / IMAP / POP3 import.\n  No external vendor SDK. No embeddings / vector libs.\n* Default policy is "enabled if Supabase reachable" —\n  explicit OFF requires a literal opt-out token, matching\n  the PAS166 doctrine.\n\nPublic surface:\n\n  * ``durable_pending_call_dedupe_enabled(config_or_env=None)``\n  * ``register_durable_pending_call_dedupe(...)``\n  * ``is_duplicate_durable_pending_call_dedupe(...)``\n  * ``mark_durable_pending_call_duplicate_seen(...)``\n')
              STORE_NAME               0 (__doc__)

 47           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 49           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 50           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (os)
              STORE_NAME               4 (os)

 51           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timedelta', 'timezone'))
              IMPORT_NAME              5 (datetime)
              IMPORT_FROM              5 (datetime)
              STORE_NAME               5 (datetime)
              IMPORT_FROM              6 (timedelta)
              STORE_NAME               6 (timedelta)
              IMPORT_FROM              7 (timezone)
              STORE_NAME               7 (timezone)
              POP_TOP

 52           LOAD_SMALL_INT           0
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

 55           LOAD_NAME                3 (logging)
              LOAD_ATTR               26 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.ingestion.pending_call_dedupe_store')
              CALL                     1
              STORE_NAME              14 (logger)

 63           LOAD_SMALL_INT          24
              STORE_NAME              15 (_DEFAULT_TTL_HOURS)

 64           LOAD_SMALL_INT           1
              STORE_NAME              16 (_MIN_TTL_HOURS)

 65           LOAD_SMALL_INT         168
              STORE_NAME              17 (_MAX_TTL_HOURS)

 67           LOAD_CONST               6 ('pas_pending_call_dedupe')
              STORE_NAME              18 (_TABLE)

 72           LOAD_CONST               7 ('PAS_PENDING_CALL_DEDUPE_DURABLE_ENABLED')
              STORE_NAME              19 (_ENV_ENABLE_FLAG)

 73           LOAD_CONST              36 (('false', '0', 'no', 'off', 'disabled'))
              STORE_NAME              20 (_ENV_DISABLE_FALSE_LITERALS)

 80           LOAD_CONST              37 ((None,))
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA2880, file "app/services/ingestion/pending_call_dedupe_store.py", line 80>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object _now_dt at 0x0000018C17D6DFC0, file "app/services/ingestion/pending_call_dedupe_store.py", line 80>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              21 (_now_dt)

 96           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA21F0, file "app/services/ingestion/pending_call_dedupe_store.py", line 96>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _iso at 0x0000018C18025C30, file "app/services/ingestion/pending_call_dedupe_store.py", line 96>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (_iso)

100           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA2A60, file "app/services/ingestion/pending_call_dedupe_store.py", line 100>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _clamp_ttl_hours at 0x0000018C17F95FD0, file "app/services/ingestion/pending_call_dedupe_store.py", line 100>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              23 (_clamp_ttl_hours)

112           LOAD_CONST              14 (<code object _get_db_safe at 0x0000018C17FF13B0, file "app/services/ingestion/pending_call_dedupe_store.py", line 112>)
              MAKE_FUNCTION
              STORE_NAME              24 (_get_db_safe)

125           LOAD_CONST              37 ((None,))
              LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA3690, file "app/services/ingestion/pending_call_dedupe_store.py", line 125>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object durable_pending_call_dedupe_enabled at 0x0000018C17F01040, file "app/services/ingestion/pending_call_dedupe_store.py", line 125>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              25 (durable_pending_call_dedupe_enabled)

156           LOAD_CONST              17 ('duplicate')

159           LOAD_CONST              18 (False)

156           LOAD_CONST              19 ('warnings')

160           LOAD_CONST               2 (None)

156           LOAD_CONST              20 ('error_code')

161           LOAD_CONST               2 (None)

156           BUILD_MAP                3
              LOAD_CONST              21 (<code object __annotate__ at 0x0000018C18025A30, file "app/services/ingestion/pending_call_dedupe_store.py", line 156>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _safe_envelope at 0x0000018C18052F70, file "app/services/ingestion/pending_call_dedupe_store.py", line 156>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              26 (_safe_envelope)

171           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C18024D30, file "app/services/ingestion/pending_call_dedupe_store.py", line 171>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object _validate_inputs at 0x0000018C17CC2960, file "app/services/ingestion/pending_call_dedupe_store.py", line 171>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_validate_inputs)

194           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA2C40, file "app/services/ingestion/pending_call_dedupe_store.py", line 194>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object _is_unique_violation at 0x0000018C17F96590, file "app/services/ingestion/pending_call_dedupe_store.py", line 194>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_is_unique_violation)

217           LOAD_CONST              27 ('pending_call_id')

222           LOAD_CONST               2 (None)

217           LOAD_CONST              28 ('ttl_hours')

223           LOAD_NAME               15 (_DEFAULT_TTL_HOURS)

217           LOAD_CONST              29 ('now')

224           LOAD_CONST               2 (None)

217           BUILD_MAP                3
              LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FBFEE0, file "app/services/ingestion/pending_call_dedupe_store.py", line 217>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object register_durable_pending_call_dedupe at 0x0000018C17F844B0, file "app/services/ingestion/pending_call_dedupe_store.py", line 217>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              29 (register_durable_pending_call_dedupe)

294           LOAD_CONST              29 ('now')

298           LOAD_CONST               2 (None)

294           BUILD_MAP                1
              LOAD_CONST              32 (<code object __annotate__ at 0x0000018C18025230, file "app/services/ingestion/pending_call_dedupe_store.py", line 294>)
              MAKE_FUNCTION
              LOAD_CONST              33 (<code object is_duplicate_durable_pending_call_dedupe at 0x0000018C17ED0510, file "app/services/ingestion/pending_call_dedupe_store.py", line 294>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              30 (is_duplicate_durable_pending_call_dedupe)

350           LOAD_CONST              29 ('now')

354           LOAD_CONST               2 (None)

350           BUILD_MAP                1
              LOAD_CONST              34 (<code object __annotate__ at 0x0000018C18025630, file "app/services/ingestion/pending_call_dedupe_store.py", line 350>)
              MAKE_FUNCTION
              LOAD_CONST              35 (<code object mark_durable_pending_call_duplicate_seen at 0x0000018C17ED7660, file "app/services/ingestion/pending_call_dedupe_store.py", line 350>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              31 (mark_durable_pending_call_duplicate_seen)

436           BUILD_LIST               0
              LOAD_CONST              38 (('durable_pending_call_dedupe_enabled', 'register_durable_pending_call_dedupe', 'is_duplicate_durable_pending_call_dedupe', 'mark_durable_pending_call_duplicate_seen'))
              LIST_EXTEND              1
              STORE_NAME              32 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app/services/ingestion/pending_call_dedupe_store.py", line 80>:
 80           RESUME                   0
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

Disassembly of <code object _now_dt at 0x0000018C17D6DFC0, file "app/services/ingestion/pending_call_dedupe_store.py", line 80>:
  80            RESUME                   0

  81            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (now)
                LOAD_GLOBAL              2 (datetime)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       78 (to L2)
                NOT_TAKEN

  82            LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L1)
                NOT_TAKEN

  83            LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                RETURN_VALUE

  84    L1:     LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

  85    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (now)
                LOAD_GLOBAL             14 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      117 (to L6)
                NOT_TAKEN

  86            NOP

  87    L3:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               16 (fromisoformat)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_CONST               2 ('Z')
                LOAD_CONST               3 ('+00:00')
                CALL                     2
                CALL                     1
                STORE_FAST               1 (dt)

  88            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L4)
                NOT_TAKEN

  89            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST               1 (dt)

  90    L4:     LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
        L5:     RETURN_VALUE

  93    L6:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               20 (now)
                PUSH_NULL
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  91            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        4 (to L9)
                NOT_TAKEN
                POP_TOP

  92    L8:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 49 (to L6)

  91    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app/services/ingestion/pending_call_dedupe_store.py", line 96>:
 96           RESUME                   0
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

Disassembly of <code object _iso at 0x0000018C18025C30, file "app/services/ingestion/pending_call_dedupe_store.py", line 96>:
 96           RESUME                   0

 97           LOAD_FAST_BORROW         0 (dt)
              LOAD_ATTR                1 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app/services/ingestion/pending_call_dedupe_store.py", line 100>:
100           RESUME                   0
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

Disassembly of <code object _clamp_ttl_hours at 0x0000018C17F95FD0, file "app/services/ingestion/pending_call_dedupe_store.py", line 100>:
 100           RESUME                   0

 101           NOP

 102   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (v)

 105   L2:     LOAD_FAST                1 (v)
               LOAD_GLOBAL              8 (_MIN_TTL_HOURS)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        7 (to L3)
               NOT_TAKEN

 106           LOAD_GLOBAL              8 (_MIN_TTL_HOURS)
               RETURN_VALUE

 107   L3:     LOAD_FAST                1 (v)
               LOAD_GLOBAL             10 (_MAX_TTL_HOURS)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 108           LOAD_GLOBAL             10 (_MAX_TTL_HOURS)
               RETURN_VALUE

 109   L4:     LOAD_FAST                1 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 103           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

 104           LOAD_GLOBAL              6 (_DEFAULT_TTL_HOURS)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 103   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object _get_db_safe at 0x0000018C17FF13B0, file "app/services/ingestion/pending_call_dedupe_store.py", line 112>:
 112           RESUME                   0

 114           NOP

 115   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 116           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 117           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 118   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 119           LOAD_CONST               2 ('pending_call_dedupe_store db client unavailable type=')

 120           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 119           BUILD_STRING             2

 118           CALL                     1
               POP_TOP

 122   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 117   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app/services/ingestion/pending_call_dedupe_store.py", line 125>:
125           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('config_or_env')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object durable_pending_call_dedupe_enabled at 0x0000018C17F01040, file "app/services/ingestion/pending_call_dedupe_store.py", line 125>:
125           RESUME                   0

143           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (config_or_env)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       34 (to L2)
              NOT_TAKEN

144           LOAD_FAST_BORROW         0 (config_or_env)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('pending_call_dedupe_durable_enabled')
              CALL                     1
              STORE_FAST               1 (explicit)

145           LOAD_FAST_BORROW         1 (explicit)
              LOAD_CONST               2 (True)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

146           LOAD_CONST               2 (True)
              RETURN_VALUE

147   L1:     LOAD_FAST_BORROW         1 (explicit)
              LOAD_CONST               3 (False)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

148           LOAD_CONST               3 (False)
              RETURN_VALUE

149   L2:     LOAD_GLOBAL              6 (os)
              LOAD_ATTR                8 (environ)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_GLOBAL             10 (_ENV_ENABLE_FLAG)
              CALL                     1
              STORE_FAST               2 (raw)

150           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (raw)
              LOAD_GLOBAL             12 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       42 (to L3)
              NOT_TAKEN

151           LOAD_FAST_BORROW         2 (raw)
              LOAD_ATTR               15 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR               17 (lower + NULL|self)
              CALL                     0
              LOAD_GLOBAL             18 (_ENV_DISABLE_FALSE_LITERALS)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

152           LOAD_CONST               3 (False)
              RETURN_VALUE

153   L3:     LOAD_CONST               2 (True)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app/services/ingestion/pending_call_dedupe_store.py", line 156>:
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

156           LOAD_CONST               3 ('duplicate')

159           LOAD_CONST               4 ('bool')

156           LOAD_CONST               5 ('warnings')

160           LOAD_CONST               6 ('Optional[List[str]]')

156           LOAD_CONST               7 ('error_code')

161           LOAD_CONST               8 ('Optional[str]')

156           LOAD_CONST               9 ('return')

162           LOAD_CONST              10 ('Dict[str, Any]')

156           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C18052F70, file "app/services/ingestion/pending_call_dedupe_store.py", line 156>:
156           RESUME                   0

164           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

165           LOAD_CONST               1 ('duplicate')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         1 (duplicate)
              CALL                     1

166           LOAD_CONST               2 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                2 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

167           LOAD_CONST               3 ('error_code')
              LOAD_FAST_BORROW         3 (error_code)

163           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024D30, file "app/services/ingestion/pending_call_dedupe_store.py", line 171>:
171           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

173           LOAD_CONST               2 ('Any')

171           LOAD_CONST               3 ('dedupe_key')

174           LOAD_CONST               2 ('Any')

171           LOAD_CONST               4 ('source')

175           LOAD_CONST               2 ('Any')

171           LOAD_CONST               5 ('return')

176           LOAD_CONST               6 ('Optional[str]')

171           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _validate_inputs at 0x0000018C17CC2960, file "app/services/ingestion/pending_call_dedupe_store.py", line 171>:
171            RESUME                   0

179            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (brokerage_id)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L1)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (brokerage_id)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

180    L1:     LOAD_CONST               1 ('missing_brokerage_id')
               RETURN_VALUE

181    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (dedupe_key)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L3)
               NOT_TAKEN
               LOAD_FAST_BORROW         1 (dedupe_key)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN

182    L3:     LOAD_CONST               2 ('missing_dedupe_key')
               RETURN_VALUE

183    L4:     LOAD_GLOBAL              7 (len + NULL)
               LOAD_FAST_BORROW         1 (dedupe_key)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               CALL                     1
               LOAD_SMALL_INT          64
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN

184            LOAD_CONST               3 ('invalid_dedupe_key_shape')
               RETURN_VALUE

185    L5:     LOAD_FAST_BORROW         1 (dedupe_key)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               GET_ITER
       L6:     FOR_ITER                13 (to L8)
               STORE_FAST               3 (ch)

186            LOAD_FAST_BORROW         3 (ch)
               LOAD_CONST               4 ('0123456789abcdef')
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_TRUE         3 (to L7)
               NOT_TAKEN
               JUMP_BACKWARD           12 (to L6)

187    L7:     POP_TOP
               LOAD_CONST               3 ('invalid_dedupe_key_shape')
               RETURN_VALUE

185    L8:     END_FOR
               POP_ITER

188            LOAD_FAST_BORROW         2 (source)
               POP_JUMP_IF_NONE        47 (to L10)
               NOT_TAKEN

189            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (source)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L9)
               NOT_TAKEN
               LOAD_FAST_BORROW         2 (source)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L10)
               NOT_TAKEN

190    L9:     LOAD_CONST               6 ('invalid_source')
               RETURN_VALUE

191   L10:     LOAD_CONST               5 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app/services/ingestion/pending_call_dedupe_store.py", line 194>:
194           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('exc')
              LOAD_CONST               2 ('BaseException')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _is_unique_violation at 0x0000018C17F96590, file "app/services/ingestion/pending_call_dedupe_store.py", line 194>:
 194           RESUME                   0

 200           NOP

 201   L1:     LOAD_GLOBAL              1 (repr + NULL)
               LOAD_FAST_BORROW         0 (exc)
               CALL                     1
               STORE_FAST               1 (s)

 204   L2:     LOAD_CONST               2 ('23505')
               LOAD_FAST                1 (s)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 205           LOAD_CONST               3 (True)
               RETURN_VALUE

 206   L3:     LOAD_FAST                1 (s)
               LOAD_ATTR                5 (lower + NULL|self)
               CALL                     0
               STORE_FAST               2 (lowered)

 208           LOAD_CONST               4 ('duplicate key value violates unique constraint')
               LOAD_FAST                2 (lowered)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L4)
               NOT_TAKEN
               POP_TOP

 209           LOAD_CONST               5 ('already exists')
               LOAD_FAST                2 (lowered)
               CONTAINS_OP              0 (in)

 207   L4:     RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 202           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L7)
               NOT_TAKEN
               POP_TOP

 203   L6:     POP_EXCEPT
               LOAD_CONST               1 (False)
               RETURN_VALUE

 202   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FBFEE0, file "app/services/ingestion/pending_call_dedupe_store.py", line 217>:
217           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

219           LOAD_CONST               2 ('str')

217           LOAD_CONST               3 ('dedupe_key')

220           LOAD_CONST               2 ('str')

217           LOAD_CONST               4 ('source')

221           LOAD_CONST               2 ('str')

217           LOAD_CONST               5 ('pending_call_id')

222           LOAD_CONST               6 ('Optional[str]')

217           LOAD_CONST               7 ('ttl_hours')

223           LOAD_CONST               8 ('int')

217           LOAD_CONST               9 ('now')

224           LOAD_CONST              10 ('Any')

217           LOAD_CONST              11 ('return')

225           LOAD_CONST              12 ('Dict[str, Any]')

217           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object register_durable_pending_call_dedupe at 0x0000018C17F844B0, file "app/services/ingestion/pending_call_dedupe_store.py", line 217>:
 217            RESUME                   0

 242            LOAD_GLOBAL              1 (_validate_inputs + NULL)

 243            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage_id, dedupe_key)
                LOAD_FAST_BORROW         2 (source)

 242            LOAD_CONST               1 (('brokerage_id', 'dedupe_key', 'source'))
                CALL_KW                  3
                STORE_FAST               6 (err)

 245            LOAD_FAST_BORROW         6 (err)
                POP_JUMP_IF_NONE        14 (to L1)
                NOT_TAKEN

 246            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               3 ('failed')
                LOAD_FAST_BORROW         6 (err)
                LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 248    L1:     LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               7 (bid)

 249            LOAD_FAST_BORROW         1 (dedupe_key)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR                7 (lower + NULL|self)
                CALL                     0
                STORE_FAST               8 (key)

 250            LOAD_FAST_BORROW         2 (source)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR                7 (lower + NULL|self)
                CALL                     0
                STORE_FAST               9 (src)

 252            LOAD_GLOBAL              9 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST              10 (db)

 253            LOAD_FAST_BORROW        10 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L2)
                NOT_TAKEN

 254            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 255            LOAD_CONST               5 ('warning')

 256            LOAD_CONST               6 ('durable_pending_call_dedupe_unavailable')
                BUILD_LIST               1

 257            LOAD_CONST               6 ('durable_pending_call_dedupe_unavailable')

 254            LOAD_CONST               7 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 260    L2:     LOAD_GLOBAL             11 (_clamp_ttl_hours + NULL)
                LOAD_FAST_BORROW         4 (ttl_hours)
                CALL                     1
                STORE_FAST              11 (ttl)

 261            LOAD_GLOBAL             13 (_now_dt + NULL)
                LOAD_FAST_BORROW         5 (now)
                CALL                     1
                STORE_FAST              12 (now_dt)

 262            LOAD_FAST_BORROW        12 (now_dt)
                LOAD_GLOBAL             15 (timedelta + NULL)
                LOAD_FAST_BORROW        11 (ttl)
                LOAD_CONST               8 (('hours',))
                CALL_KW                  1
                BINARY_OP                0 (+)
                STORE_FAST              13 (expires_dt)

 265            LOAD_CONST               9 ('dedupe_key')
                LOAD_FAST_BORROW         8 (key)

 266            LOAD_CONST              10 ('brokerage_id')
                LOAD_FAST_BORROW         7 (bid)

 267            LOAD_CONST              11 ('source')
                LOAD_FAST_BORROW         9 (src)

 268            LOAD_CONST              12 ('created_at')
                LOAD_GLOBAL             17 (_iso + NULL)
                LOAD_FAST_BORROW        12 (now_dt)
                CALL                     1

 269            LOAD_CONST              13 ('expires_at')
                LOAD_GLOBAL             17 (_iso + NULL)
                LOAD_FAST_BORROW        13 (expires_dt)
                CALL                     1

 264            BUILD_MAP                5
                STORE_FAST              14 (row)

 271            LOAD_GLOBAL             19 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (pending_call_id)
                LOAD_GLOBAL             20 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (pending_call_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       20 (to L3)
                NOT_TAKEN

 272            LOAD_FAST_BORROW         3 (pending_call_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                LOAD_FAST_BORROW        14 (row)
                LOAD_CONST              14 ('first_seen_pending_call_id')
                STORE_SUBSCR

 274    L3:     NOP

 275    L4:     LOAD_FAST_BORROW        10 (db)
                LOAD_ATTR               23 (table + NULL|self)
                LOAD_GLOBAL             24 (_TABLE)
                CALL                     1
                LOAD_ATTR               27 (insert + NULL|self)
                LOAD_FAST_BORROW        14 (row)
                CALL                     1
                LOAD_ATTR               29 (execute + NULL|self)
                CALL                     0
                POP_TOP

 276            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST              15 ('ok')
                LOAD_CONST              16 (False)
                LOAD_CONST              17 (('status', 'duplicate'))
                CALL_KW                  2
        L5:     RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 277            LOAD_GLOBAL             30 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      127 (to L14)
                NOT_TAKEN
                STORE_FAST              15 (e)

 278    L7:     LOAD_GLOBAL             33 (_is_unique_violation + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L10)
                NOT_TAKEN

 279            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST              15 ('ok')
                LOAD_CONST              18 (True)
                LOAD_CONST              17 (('status', 'duplicate'))
                CALL_KW                  2
        L8:     SWAP                     2
        L9:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RETURN_VALUE

 280   L10:     LOAD_GLOBAL             34 (logger)
                LOAD_ATTR               37 (warning + NULL|self)

 281            LOAD_CONST              19 ('register_durable_pending_call_dedupe db error type=')

 282            LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)
                FORMAT_SIMPLE

 281            BUILD_STRING             2

 280            CALL                     1
                POP_TOP

 284            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 285            LOAD_CONST               5 ('warning')

 287            LOAD_CONST               6 ('durable_pending_call_dedupe_unavailable')

 288            LOAD_CONST              20 ('db_write_failed:')
                LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 286            BUILD_LIST               2

 290            LOAD_CONST               6 ('durable_pending_call_dedupe_unavailable')

 284            LOAD_CONST               7 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
       L11:     SWAP                     2
       L12:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RETURN_VALUE

  --   L13:     LOAD_CONST               2 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RERAISE                  1

 277   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L6 [0]
  L6 to L7 -> L15 [1] lasti
  L7 to L8 -> L13 [1] lasti
  L8 to L9 -> L15 [1] lasti
  L10 to L11 -> L13 [1] lasti
  L11 to L12 -> L15 [1] lasti
  L13 to L15 -> L15 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025230, file "app/services/ingestion/pending_call_dedupe_store.py", line 294>:
294           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

296           LOAD_CONST               2 ('str')

294           LOAD_CONST               3 ('dedupe_key')

297           LOAD_CONST               2 ('str')

294           LOAD_CONST               4 ('now')

298           LOAD_CONST               5 ('Any')

294           LOAD_CONST               6 ('return')

299           LOAD_CONST               7 ('Dict[str, Any]')

294           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object is_duplicate_durable_pending_call_dedupe at 0x0000018C17ED0510, file "app/services/ingestion/pending_call_dedupe_store.py", line 294>:
 294            RESUME                   0

 306            LOAD_GLOBAL              1 (_validate_inputs + NULL)

 307            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage_id, dedupe_key)
                LOAD_CONST               1 (None)

 306            LOAD_CONST               2 (('brokerage_id', 'dedupe_key', 'source'))
                CALL_KW                  3
                STORE_FAST               3 (err)

 309            LOAD_FAST_BORROW         3 (err)
                POP_JUMP_IF_NONE        14 (to L1)
                NOT_TAKEN

 310            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               3 ('failed')
                LOAD_FAST_BORROW         3 (err)
                LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 312    L1:     LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               4 (bid)

 313            LOAD_FAST_BORROW         1 (dedupe_key)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR                7 (lower + NULL|self)
                CALL                     0
                STORE_FAST               5 (key)

 314            LOAD_GLOBAL              9 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               6 (db)

 315            LOAD_FAST_BORROW         6 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L2)
                NOT_TAKEN

 316            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 317            LOAD_CONST               5 ('warning')

 318            LOAD_CONST               6 ('durable_pending_call_dedupe_unavailable')
                BUILD_LIST               1

 319            LOAD_CONST               6 ('durable_pending_call_dedupe_unavailable')

 316            LOAD_CONST               7 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 322    L2:     LOAD_GLOBAL             11 (_iso + NULL)
                LOAD_GLOBAL             13 (_now_dt + NULL)
                LOAD_FAST_BORROW         2 (now)
                CALL                     1
                CALL                     1
                STORE_FAST               7 (when)

 323            NOP

 325    L3:     LOAD_FAST_BORROW         6 (db)
                LOAD_ATTR               15 (table + NULL|self)
                LOAD_GLOBAL             16 (_TABLE)
                CALL                     1

 326            LOAD_ATTR               19 (select + NULL|self)
                LOAD_CONST               8 ('dedupe_key, expires_at')
                CALL                     1

 327            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST               9 ('brokerage_id')
                LOAD_FAST_BORROW         4 (bid)
                CALL                     2

 328            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST              10 ('dedupe_key')
                LOAD_FAST_BORROW         5 (key)
                CALL                     2

 329            LOAD_ATTR               23 (gt + NULL|self)
                LOAD_CONST              11 ('expires_at')
                LOAD_FAST_BORROW         7 (when)
                CALL                     2

 330            LOAD_ATTR               25 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 331            LOAD_ATTR               27 (execute + NULL|self)
                CALL                     0

 324            STORE_FAST               8 (result)

 333            LOAD_GLOBAL             29 (list + NULL)
                LOAD_GLOBAL             31 (getattr + NULL)
                LOAD_FAST_BORROW         8 (result)
                LOAD_CONST              12 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L4:     CALL                     1
                STORE_FAST               9 (rows)

 334            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST              13 ('ok')
                LOAD_GLOBAL             33 (bool + NULL)
                LOAD_FAST_BORROW         9 (rows)
                CALL                     1
                LOAD_CONST              14 (('status', 'duplicate'))
                CALL_KW                  2
        L5:     RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 335            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       92 (to L11)
                NOT_TAKEN
                STORE_FAST              10 (e)

 336    L7:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 337            LOAD_CONST              15 ('is_duplicate_durable_pending_call_dedupe db error type=')

 338            LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE

 337            BUILD_STRING             2

 336            CALL                     1
                POP_TOP

 340            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 341            LOAD_CONST               5 ('warning')

 343            LOAD_CONST               6 ('durable_pending_call_dedupe_unavailable')

 344            LOAD_CONST              16 ('db_read_failed:')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 342            BUILD_LIST               2

 346            LOAD_CONST               6 ('durable_pending_call_dedupe_unavailable')

 340            LOAD_CONST               7 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
        L8:     SWAP                     2
        L9:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RETURN_VALUE

  --   L10:     LOAD_CONST               1 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 335   L11:     RERAISE                  0

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L6 [0]
  L6 to L7 -> L12 [1] lasti
  L7 to L8 -> L10 [1] lasti
  L8 to L9 -> L12 [1] lasti
  L10 to L12 -> L12 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025630, file "app/services/ingestion/pending_call_dedupe_store.py", line 350>:
350           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

352           LOAD_CONST               2 ('str')

350           LOAD_CONST               3 ('dedupe_key')

353           LOAD_CONST               2 ('str')

350           LOAD_CONST               4 ('now')

354           LOAD_CONST               5 ('Any')

350           LOAD_CONST               6 ('return')

355           LOAD_CONST               7 ('Dict[str, Any]')

350           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object mark_durable_pending_call_duplicate_seen at 0x0000018C17ED7660, file "app/services/ingestion/pending_call_dedupe_store.py", line 350>:
 350            RESUME                   0

 367            LOAD_GLOBAL              1 (_validate_inputs + NULL)

 368            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage_id, dedupe_key)
                LOAD_CONST               1 (None)

 367            LOAD_CONST               2 (('brokerage_id', 'dedupe_key', 'source'))
                CALL_KW                  3
                STORE_FAST               3 (err)

 370            LOAD_FAST_BORROW         3 (err)
                POP_JUMP_IF_NONE        14 (to L1)
                NOT_TAKEN

 371            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               3 ('failed')
                LOAD_FAST_BORROW         3 (err)
                LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 373    L1:     LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               4 (bid)

 374            LOAD_FAST_BORROW         1 (dedupe_key)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR                7 (lower + NULL|self)
                CALL                     0
                STORE_FAST               5 (key)

 375            LOAD_GLOBAL              9 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               6 (db)

 376            LOAD_FAST_BORROW         6 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L2)
                NOT_TAKEN

 377            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 378            LOAD_CONST               5 ('warning')

 379            LOAD_CONST               6 ('durable_pending_call_dedupe_unavailable')
                BUILD_LIST               1

 380            LOAD_CONST               6 ('durable_pending_call_dedupe_unavailable')

 377            LOAD_CONST               7 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 383    L2:     LOAD_GLOBAL             11 (_iso + NULL)
                LOAD_GLOBAL             13 (_now_dt + NULL)
                LOAD_FAST_BORROW         2 (now)
                CALL                     1
                CALL                     1
                STORE_FAST               7 (now_iso)

 384            NOP

 386    L3:     LOAD_FAST_BORROW         6 (db)
                LOAD_ATTR               15 (table + NULL|self)
                LOAD_GLOBAL             16 (_TABLE)
                CALL                     1

 387            LOAD_ATTR               19 (select + NULL|self)
                LOAD_CONST               8 ('duplicate_count')
                CALL                     1

 388            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST               9 ('brokerage_id')
                LOAD_FAST_BORROW         4 (bid)
                CALL                     2

 389            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST              10 ('dedupe_key')
                LOAD_FAST_BORROW         5 (key)
                CALL                     2

 390            LOAD_ATTR               23 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 391            LOAD_ATTR               25 (execute + NULL|self)
                CALL                     0

 385            STORE_FAST               8 (result)

 393            LOAD_GLOBAL             27 (list + NULL)
                LOAD_GLOBAL             29 (getattr + NULL)
                LOAD_FAST_BORROW         8 (result)
                LOAD_CONST              11 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L4:     CALL                     1
                STORE_FAST               9 (rows)

 394            LOAD_FAST_BORROW         9 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        16 (to L8)
        L5:     NOT_TAKEN

 395    L6:     LOAD_GLOBAL              3 (_safe_envelope + NULL)

 396            LOAD_CONST               5 ('warning')

 397            LOAD_CONST              12 ('pending_call_dedupe_row_not_found')
                BUILD_LIST               1

 398            LOAD_CONST              12 ('pending_call_dedupe_row_not_found')

 395            LOAD_CONST               7 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
        L7:     RETURN_VALUE

 400    L8:     LOAD_FAST_BORROW         9 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               8 ('duplicate_count')
                CALL                     1
                STORE_FAST              10 (current)

 401            LOAD_GLOBAL             33 (isinstance + NULL)
                LOAD_FAST_BORROW        10 (current)
                LOAD_GLOBAL             34 (int)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L9)
                NOT_TAKEN
                LOAD_FAST_BORROW        10 (current)
                LOAD_SMALL_INT           0
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN

 402    L9:     LOAD_SMALL_INT           0
                STORE_FAST              10 (current)

 404   L10:     LOAD_CONST               8 ('duplicate_count')
                LOAD_FAST_BORROW        10 (current)
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)

 405            LOAD_CONST              13 ('last_duplicate_at')
                LOAD_FAST_BORROW         7 (now_iso)

 403            BUILD_MAP                2
                STORE_FAST              11 (patch)

 408            LOAD_FAST_BORROW         6 (db)
                LOAD_ATTR               15 (table + NULL|self)
                LOAD_GLOBAL             16 (_TABLE)
                CALL                     1

 409            LOAD_ATTR               37 (update + NULL|self)
                LOAD_FAST_BORROW        11 (patch)
                CALL                     1

 410            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST               9 ('brokerage_id')
                LOAD_FAST_BORROW         4 (bid)
                CALL                     2

 411            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST              10 ('dedupe_key')
                LOAD_FAST_BORROW         5 (key)
                CALL                     2

 412            LOAD_ATTR               25 (execute + NULL|self)
                CALL                     0

 407            STORE_FAST              12 (update_result)

 414            LOAD_GLOBAL             27 (list + NULL)
                LOAD_GLOBAL             29 (getattr + NULL)
                LOAD_FAST_BORROW        12 (update_result)
                LOAD_CONST              11 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                BUILD_LIST               0
       L13:     CALL                     1
                STORE_FAST              13 (updated_rows)

 415            LOAD_FAST_BORROW        13 (updated_rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L17)
       L14:     NOT_TAKEN

 416   L15:     LOAD_GLOBAL              3 (_safe_envelope + NULL)

 417            LOAD_CONST               5 ('warning')

 418            LOAD_CONST              14 ('pending_call_dedupe_update_returned_no_rows')
                BUILD_LIST               1

 416            LOAD_CONST              15 (('status', 'warnings'))
                CALL_KW                  2
       L16:     RETURN_VALUE

 420   L17:     LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST              16 ('ok')
                LOAD_CONST              17 (True)
                LOAD_CONST              18 (('status', 'duplicate'))
                CALL_KW                  2
       L18:     RETURN_VALUE

  --   L19:     PUSH_EXC_INFO

 421            LOAD_GLOBAL             38 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       92 (to L24)
                NOT_TAKEN
                STORE_FAST              14 (e)

 422   L20:     LOAD_GLOBAL             40 (logger)
                LOAD_ATTR               43 (warning + NULL|self)

 423            LOAD_CONST              19 ('mark_durable_pending_call_duplicate_seen db error type=')

 424            LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE

 423            BUILD_STRING             2

 422            CALL                     1
                POP_TOP

 426            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 427            LOAD_CONST               5 ('warning')

 429            LOAD_CONST               6 ('durable_pending_call_dedupe_unavailable')

 430            LOAD_CONST              20 ('db_write_failed:')
                LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 428            BUILD_LIST               2

 432            LOAD_CONST               6 ('durable_pending_call_dedupe_unavailable')

 426            LOAD_CONST               7 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
       L21:     SWAP                     2
       L22:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RETURN_VALUE

  --   L23:     LOAD_CONST               1 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RERAISE                  1

 421   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L19 [0]
  L6 to L7 -> L19 [0]
  L8 to L11 -> L19 [0]
  L12 to L14 -> L19 [0]
  L15 to L16 -> L19 [0]
  L17 to L18 -> L19 [0]
  L19 to L20 -> L25 [1] lasti
  L20 to L21 -> L23 [1] lasti
  L21 to L22 -> L25 [1] lasti
  L23 to L25 -> L25 [1] lasti
```
