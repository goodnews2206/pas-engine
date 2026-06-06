# ingestion/email_dedupe_store

- **pyc:** `app\services\ingestion\__pycache__\email_dedupe_store.cpython-314.pyc`
- **expected source path (absent):** `app\services\ingestion/email_dedupe_store.py`
- **co_filename (from bytecode):** `app\services\ingestion\email_dedupe_store.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** ingestion

## Module docstring

```
PAS166 — Durable email dedupe store (Supabase-backed v1).

Multi-replica-safe, restart-safe replacement for the
PAS165 process-local registry
(:mod:`app.services.ingestion.email_dedupe`). The
process-local registry remains in place as a fallback when
the durable store is unavailable (table missing, DB
unreachable, client unconfigured).

Doctrine carried by every helper here:

* ``brokerage_id`` is REQUIRED on every read and write.
  NEVER read from any payload — resolved from auth in the
  calling layer and passed in as a kwarg.
* The dedupe key is stored in the table but is NEVER
  returned in the public envelope, NEVER logged, NEVER
  echoed in events.
* No raw email body / subject / sender / phone / email /
  name / property / notes / transcript columns. The table
  schema (proposal at
  ``scripts/migrate_v15_email_dedupe.sql``) is structurally
  pinned to the dedupe key + tenant scope + lifecycle
  timestamps + a pending-call backlink.
* No exception escapes any public helper. DB unreachable /
  table missing / unique-constraint conflict are all
  surfaced as structural envelopes; the caller can then
  fall back to the PAS165 process-local registry.
* No Gmail / Google / inbox / OAuth / IMAP / POP3 import.
  No external vendor SDK. No embeddings / vector libs.

Public surface:

  * ``durable_email_dedupe_enabled(config_or_env=None)``
  * ``register_email_dedupe_key(...)``
  * ``is_duplicate_email_dedupe_key(...)``
  * ``mark_email_duplicate_seen(...)``
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `datetime`, `get_supabase`, `logging`, `os`, `timedelta`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_ttl_hours`, `_get_db_safe`, `_is_unique_violation`, `_iso`, `_now_dt`, `_safe_envelope`, `_validate_inputs`, `durable_email_dedupe_enabled`, `is_duplicate_email_dedupe_key`, `mark_email_duplicate_seen`, `register_email_dedupe_key`

## Env-key candidates

`ALLOWED_DEDUPE_SOURCES`, `PAS_EMAIL_DEDUPE_DURABLE_ENABLED`

## String constants (redacted where noted)

- '\nPAS166 — Durable email dedupe store (Supabase-backed v1).\n\nMulti-replica-safe, restart-safe replacement for the\nPAS165 process-local registry\n(:mod:`app.services.ingestion.email_dedupe`). The\nprocess-local registry remains in place as a fallback when\nthe durable store is unavailable (table missing, DB\nunreachable, client unconfigured).\n\nDoctrine carried by every helper here:\n\n* ``brokerage_id`` is REQUIRED on every read and write.\n  NEVER read from any payload — resolved from auth in the\n  calling layer and passed in as a kwarg.\n* The dedupe key is stored in the table but is NEVER\n  returned in the public envelope, NEVER logged, NEVER\n  echoed in events.\n* No raw email body / subject / sender / phone / email /\n  name / property / notes / transcript columns. The table\n  schema (proposal at\n  ``scripts/migrate_v15_email_dedupe.sql``) is structurally\n  pinned to the dedupe key + tenant scope + lifecycle\n  timestamps + a pending-call backlink.\n* No exception escapes any public helper. DB unreachable /\n  table missing / unique-constraint conflict are all\n  surfaced as structural envelopes; the caller can then\n  fall back to the PAS165 process-local registry.\n* No Gmail / Google / inbox / OAuth / IMAP / POP3 import.\n  No external vendor SDK. No embeddings / vector libs.\n\nPublic surface:\n\n  * ``durable_email_dedupe_enabled(config_or_env=None)``\n  * ``register_email_dedupe_key(...)``\n  * ``is_duplicate_email_dedupe_key(...)``\n  * ``mark_email_duplicate_seen(...)``\n'
- 'pas.ingestion.email_dedupe_store'
- 'tuple'
- 'ALLOWED_DEDUPE_SOURCES'
- 'pas_email_dedupe_keys'
- 'PAS_EMAIL_DEDUPE_DURABLE_ENABLED'
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
- 'Clamp ``value`` to ``[_MIN_TTL_HOURS, _MAX_TTL_HOURS]``.\nNon-numeric falls back to the default. NEVER raises.'
- 'Lazy resolver for the Supabase client. Returns the\nclient object or ``None`` if the module / client cannot\nbe imported. NEVER raises.'
- 'email_dedupe_store db client unavailable type='
- 'config_or_env'
- 'bool'
- 'Resolve whether durable dedupe is enabled.\n\nPrecedence (first match wins):\n\n1. ``config_or_env`` — if it is a dict carrying the key\n   ``email_dedupe_durable_enabled`` (literal True / False),\n   that wins.  This lets a per-brokerage row opt-in or\n   opt-out without touching the env.\n2. The environment variable ``PAS_EMAIL_DEDUPE_DURABLE_\n   ENABLED``: explicit "false" / "0" / "no" / "off" /\n   "disabled" disables.  Anything else (including unset)\n   defaults to ENABLED.\n3. Default: ENABLED (the safest default for pilot brokerages\n   — restart / replica safety is the whole point of PAS166).\n\nNEVER raises.\n'
- 'email_dedupe_durable_enabled'
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
- 'Insert ``dedupe_key`` into the durable store, scoped to\n``brokerage_id``. Returns a structural envelope.\n\nOutcomes:\n\n* ``status="ok", duplicate=False`` — fresh insert.\n* ``status="ok", duplicate=True``  — unique-constraint\n  conflict; the caller should treat as "already seen".\n* ``status="warning"`` — DB unavailable / table missing.\n  The caller MUST fall back to the PAS165 process-local\n  registry.\n* ``status="failed"`` — input validation error.\n\nNEVER raises. NEVER returns the dedupe key. NEVER returns\nraw email fields.\n'
- 'failed'
- 'warning'
- 'durable_email_dedupe_unavailable'
- 'created_at'
- 'expires_at'
- 'first_seen_pending_call_id'
- 'register_email_dedupe_key db error type='
- 'db_write_failed:'
- 'Check whether ``dedupe_key`` exists in the durable store\nfor ``brokerage_id`` AND has not yet expired.\n\nReturns a structural envelope. NEVER raises. NEVER returns\nthe dedupe key.\n'
- 'dedupe_key, expires_at'
- 'data'
- 'is_duplicate_email_dedupe_key db error type='
- 'db_read_failed:'
- 'Increment the ``duplicate_count`` on the existing row\nfor ``dedupe_key`` (scoped to ``brokerage_id``) and stamp\n``last_duplicate_at``.\n\nPerforms a read-then-write so the increment is structural;\na future migration may add a SQL function for atomic\nincrement.\n\nReturns a structural envelope. NEVER raises. NEVER returns\nthe dedupe key.\n'
- 'duplicate_count'
- 'email_dedupe_row_not_found'
- 'last_duplicate_at'
- 'email_dedupe_update_returned_no_rows'
- 'mark_email_duplicate_seen db error type='

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS166 — Durable email dedupe store (Supabase-backed v1).\n\nMulti-replica-safe, restart-safe replacement for the\nPAS165 process-local registry\n(:mod:`app.services.ingestion.email_dedupe`). The\nprocess-local registry remains in place as a fallback when\nthe durable store is unavailable (table missing, DB\nunreachable, client unconfigured).\n\nDoctrine carried by every helper here:\n\n* ``brokerage_id`` is REQUIRED on every read and write.\n  NEVER read from any payload — resolved from auth in the\n  calling layer and passed in as a kwarg.\n* The dedupe key is stored in the table but is NEVER\n  returned in the public envelope, NEVER logged, NEVER\n  echoed in events.\n* No raw email body / subject / sender / phone / email /\n  name / property / notes / transcript columns. The table\n  schema (proposal at\n  ``scripts/migrate_v15_email_dedupe.sql``) is structurally\n  pinned to the dedupe key + tenant scope + lifecycle\n  timestamps + a pending-call backlink.\n* No exception escapes any public helper. DB unreachable /\n  table missing / unique-constraint conflict are all\n  surfaced as structural envelopes; the caller can then\n  fall back to the PAS165 process-local registry.\n* No Gmail / Google / inbox / OAuth / IMAP / POP3 import.\n  No external vendor SDK. No embeddings / vector libs.\n\nPublic surface:\n\n  * ``durable_email_dedupe_enabled(config_or_env=None)``\n  * ``register_email_dedupe_key(...)``\n  * ``is_duplicate_email_dedupe_key(...)``\n  * ``mark_email_duplicate_seen(...)``\n')
               STORE_NAME               1 (__doc__)

  40           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  42           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  43           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  44           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timedelta', 'timezone'))
               IMPORT_NAME              6 (datetime)
               IMPORT_FROM              6 (datetime)
               STORE_NAME               6 (datetime)
               IMPORT_FROM              7 (timedelta)
               STORE_NAME               7 (timedelta)
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

  48           LOAD_NAME                4 (logging)
               LOAD_ATTR               28 (getLogger)
               PUSH_NULL
               LOAD_CONST               5 ('pas.ingestion.email_dedupe_store')
               CALL                     1
               STORE_NAME              15 (logger)

  57           LOAD_CONST              38 (('zillow', 'realtor', 'facebook', 'website', 'generic_email', 'manual'))
               STORE_NAME              16 (ALLOWED_DEDUPE_SOURCES)
               LOAD_CONST               6 ('tuple')
               LOAD_NAME               17 (__annotations__)
               LOAD_CONST               7 ('ALLOWED_DEDUPE_SOURCES')
               STORE_SUBSCR

  65           LOAD_SMALL_INT          24
               STORE_NAME              18 (_DEFAULT_TTL_HOURS)

  66           LOAD_SMALL_INT           1
               STORE_NAME              19 (_MIN_TTL_HOURS)

  67           LOAD_SMALL_INT         168
               STORE_NAME              20 (_MAX_TTL_HOURS)

  69           LOAD_CONST               8 ('pas_email_dedupe_keys')
               STORE_NAME              21 (_TABLE)

  75           LOAD_CONST               9 ('PAS_EMAIL_DEDUPE_DURABLE_ENABLED')
               STORE_NAME              22 (_ENV_ENABLE_FLAG)

  76           LOAD_CONST              39 (('false', '0', 'no', 'off', 'disabled'))
               STORE_NAME              23 (_ENV_DISABLE_FALSE_LITERALS)

  83           LOAD_CONST              40 ((None,))
               LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA3780, file "app\services\ingestion\email_dedupe_store.py", line 83>)
               MAKE_FUNCTION
               LOAD_CONST              11 (<code object _now_dt at 0x0000018C17D6DFC0, file "app\services\ingestion\email_dedupe_store.py", line 83>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              24 (_now_dt)

  99           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA3960, file "app\services\ingestion\email_dedupe_store.py", line 99>)
               MAKE_FUNCTION
               LOAD_CONST              13 (<code object _iso at 0x0000018C18025A30, file "app\services\ingestion\email_dedupe_store.py", line 99>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              25 (_iso)

 103           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA3A50, file "app\services\ingestion\email_dedupe_store.py", line 103>)
               MAKE_FUNCTION
               LOAD_CONST              15 (<code object _clamp_ttl_hours at 0x0000018C17F95CF0, file "app\services\ingestion\email_dedupe_store.py", line 103>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              26 (_clamp_ttl_hours)

 117           LOAD_CONST              16 (<code object _get_db_safe at 0x0000018C17FF0C30, file "app\services\ingestion\email_dedupe_store.py", line 117>)
               MAKE_FUNCTION
               STORE_NAME              27 (_get_db_safe)

 132           LOAD_CONST              40 ((None,))
               LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA2D30, file "app\services\ingestion\email_dedupe_store.py", line 132>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object durable_email_dedupe_enabled at 0x0000018C17F005F0, file "app\services\ingestion\email_dedupe_store.py", line 132>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              28 (durable_email_dedupe_enabled)

 163           LOAD_CONST              19 ('duplicate')

 166           LOAD_CONST              20 (False)

 163           LOAD_CONST              21 ('warnings')

 167           LOAD_CONST               2 (None)

 163           LOAD_CONST              22 ('error_code')

 168           LOAD_CONST               2 (None)

 163           BUILD_MAP                3
               LOAD_CONST              23 (<code object __annotate__ at 0x0000018C18025B30, file "app\services\ingestion\email_dedupe_store.py", line 163>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object _safe_envelope at 0x0000018C18053510, file "app\services\ingestion\email_dedupe_store.py", line 163>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              29 (_safe_envelope)

 178           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\ingestion\email_dedupe_store.py", line 178>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object _validate_inputs at 0x0000018C17D8E300, file "app\services\ingestion\email_dedupe_store.py", line 178>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              30 (_validate_inputs)

 201           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA2E20, file "app\services\ingestion\email_dedupe_store.py", line 201>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object _is_unique_violation at 0x0000018C17F95E60, file "app\services\ingestion\email_dedupe_store.py", line 201>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_is_unique_violation)

 224           LOAD_CONST              29 ('pending_call_id')

 229           LOAD_CONST               2 (None)

 224           LOAD_CONST              30 ('ttl_hours')

 230           LOAD_NAME               18 (_DEFAULT_TTL_HOURS)

 224           LOAD_CONST              31 ('now')

 231           LOAD_CONST               2 (None)

 224           BUILD_MAP                3
               LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FBFEE0, file "app\services\ingestion\email_dedupe_store.py", line 224>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object register_email_dedupe_key at 0x0000018C17ED5770, file "app\services\ingestion\email_dedupe_store.py", line 224>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              32 (register_email_dedupe_key)

 305           LOAD_CONST              31 ('now')

 309           LOAD_CONST               2 (None)

 305           BUILD_MAP                1
               LOAD_CONST              34 (<code object __annotate__ at 0x0000018C18025D30, file "app\services\ingestion\email_dedupe_store.py", line 305>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object is_duplicate_email_dedupe_key at 0x0000018C17ED5F20, file "app\services\ingestion\email_dedupe_store.py", line 305>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              33 (is_duplicate_email_dedupe_key)

 362           LOAD_CONST              31 ('now')

 366           LOAD_CONST               2 (None)

 362           BUILD_MAP                1
               LOAD_CONST              36 (<code object __annotate__ at 0x0000018C18025E30, file "app\services\ingestion\email_dedupe_store.py", line 362>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object mark_email_duplicate_seen at 0x0000018C17ED6800, file "app\services\ingestion\email_dedupe_store.py", line 362>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              34 (mark_email_duplicate_seen)

 448           BUILD_LIST               0
               LOAD_CONST              41 (('ALLOWED_DEDUPE_SOURCES', 'durable_email_dedupe_enabled', 'register_email_dedupe_key', 'is_duplicate_email_dedupe_key', 'mark_email_duplicate_seen'))
               LIST_EXTEND              1
               STORE_NAME              35 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app\services\ingestion\email_dedupe_store.py", line 83>:
 83           RESUME                   0
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

Disassembly of <code object _now_dt at 0x0000018C17D6DFC0, file "app\services\ingestion\email_dedupe_store.py", line 83>:
  83            RESUME                   0

  84            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (now)
                LOAD_GLOBAL              2 (datetime)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       78 (to L2)
                NOT_TAKEN

  85            LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L1)
                NOT_TAKEN

  86            LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                RETURN_VALUE

  87    L1:     LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

  88    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (now)
                LOAD_GLOBAL             14 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      117 (to L6)
                NOT_TAKEN

  89            NOP

  90    L3:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               16 (fromisoformat)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_CONST               2 ('Z')
                LOAD_CONST               3 ('+00:00')
                CALL                     2
                CALL                     1
                STORE_FAST               1 (dt)

  91            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L4)
                NOT_TAKEN

  92            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST               1 (dt)

  93    L4:     LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
        L5:     RETURN_VALUE

  96    L6:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               20 (now)
                PUSH_NULL
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  94            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        4 (to L9)
                NOT_TAKEN
                POP_TOP

  95    L8:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 49 (to L6)

  94    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app\services\ingestion\email_dedupe_store.py", line 99>:
 99           RESUME                   0
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

Disassembly of <code object _iso at 0x0000018C18025A30, file "app\services\ingestion\email_dedupe_store.py", line 99>:
 99           RESUME                   0

100           LOAD_FAST_BORROW         0 (dt)
              LOAD_ATTR                1 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app\services\ingestion\email_dedupe_store.py", line 103>:
103           RESUME                   0
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

Disassembly of <code object _clamp_ttl_hours at 0x0000018C17F95CF0, file "app\services\ingestion\email_dedupe_store.py", line 103>:
 103           RESUME                   0

 106           NOP

 107   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (v)

 110   L2:     LOAD_FAST                1 (v)
               LOAD_GLOBAL              8 (_MIN_TTL_HOURS)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        7 (to L3)
               NOT_TAKEN

 111           LOAD_GLOBAL              8 (_MIN_TTL_HOURS)
               RETURN_VALUE

 112   L3:     LOAD_FAST                1 (v)
               LOAD_GLOBAL             10 (_MAX_TTL_HOURS)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 113           LOAD_GLOBAL             10 (_MAX_TTL_HOURS)
               RETURN_VALUE

 114   L4:     LOAD_FAST                1 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 108           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

 109           LOAD_GLOBAL              6 (_DEFAULT_TTL_HOURS)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 108   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object _get_db_safe at 0x0000018C17FF0C30, file "app\services\ingestion\email_dedupe_store.py", line 117>:
 117           RESUME                   0

 121           NOP

 122   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 123           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 124           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 125   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 126           LOAD_CONST               2 ('email_dedupe_store db client unavailable type=')

 127           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 126           BUILD_STRING             2

 125           CALL                     1
               POP_TOP

 129   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 124   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app\services\ingestion\email_dedupe_store.py", line 132>:
132           RESUME                   0
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

Disassembly of <code object durable_email_dedupe_enabled at 0x0000018C17F005F0, file "app\services\ingestion\email_dedupe_store.py", line 132>:
132           RESUME                   0

150           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (config_or_env)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       34 (to L2)
              NOT_TAKEN

151           LOAD_FAST_BORROW         0 (config_or_env)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('email_dedupe_durable_enabled')
              CALL                     1
              STORE_FAST               1 (explicit)

152           LOAD_FAST_BORROW         1 (explicit)
              LOAD_CONST               2 (True)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

153           LOAD_CONST               2 (True)
              RETURN_VALUE

154   L1:     LOAD_FAST_BORROW         1 (explicit)
              LOAD_CONST               3 (False)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

155           LOAD_CONST               3 (False)
              RETURN_VALUE

156   L2:     LOAD_GLOBAL              6 (os)
              LOAD_ATTR                8 (environ)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_GLOBAL             10 (_ENV_ENABLE_FLAG)
              CALL                     1
              STORE_FAST               2 (raw)

157           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (raw)
              LOAD_GLOBAL             12 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       42 (to L3)
              NOT_TAKEN

158           LOAD_FAST_BORROW         2 (raw)
              LOAD_ATTR               15 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR               17 (lower + NULL|self)
              CALL                     0
              LOAD_GLOBAL             18 (_ENV_DISABLE_FALSE_LITERALS)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

159           LOAD_CONST               3 (False)
              RETURN_VALUE

160   L3:     LOAD_CONST               2 (True)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025B30, file "app\services\ingestion\email_dedupe_store.py", line 163>:
163           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

165           LOAD_CONST               2 ('str')

163           LOAD_CONST               3 ('duplicate')

166           LOAD_CONST               4 ('bool')

163           LOAD_CONST               5 ('warnings')

167           LOAD_CONST               6 ('Optional[List[str]]')

163           LOAD_CONST               7 ('error_code')

168           LOAD_CONST               8 ('Optional[str]')

163           LOAD_CONST               9 ('return')

169           LOAD_CONST              10 ('Dict[str, Any]')

163           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C18053510, file "app\services\ingestion\email_dedupe_store.py", line 163>:
163           RESUME                   0

171           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

172           LOAD_CONST               1 ('duplicate')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         1 (duplicate)
              CALL                     1

173           LOAD_CONST               2 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                2 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

174           LOAD_CONST               3 ('error_code')
              LOAD_FAST_BORROW         3 (error_code)

170           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\ingestion\email_dedupe_store.py", line 178>:
178           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

180           LOAD_CONST               2 ('Any')

178           LOAD_CONST               3 ('dedupe_key')

181           LOAD_CONST               2 ('Any')

178           LOAD_CONST               4 ('source')

182           LOAD_CONST               2 ('Any')

178           LOAD_CONST               5 ('return')

183           LOAD_CONST               6 ('Optional[str]')

178           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _validate_inputs at 0x0000018C17D8E300, file "app\services\ingestion\email_dedupe_store.py", line 178>:
178            RESUME                   0

186            LOAD_GLOBAL              1 (isinstance + NULL)
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

187    L1:     LOAD_CONST               1 ('missing_brokerage_id')
               RETURN_VALUE

188    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
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

189    L3:     LOAD_CONST               2 ('missing_dedupe_key')
               RETURN_VALUE

190    L4:     LOAD_GLOBAL              7 (len + NULL)
               LOAD_FAST_BORROW         1 (dedupe_key)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               CALL                     1
               LOAD_SMALL_INT          64
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN

191            LOAD_CONST               3 ('invalid_dedupe_key_shape')
               RETURN_VALUE

192    L5:     LOAD_FAST_BORROW         1 (dedupe_key)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               GET_ITER
       L6:     FOR_ITER                13 (to L8)
               STORE_FAST               3 (ch)

193            LOAD_FAST_BORROW         3 (ch)
               LOAD_CONST               4 ('0123456789abcdef')
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_TRUE         3 (to L7)
               NOT_TAKEN
               JUMP_BACKWARD           12 (to L6)

194    L7:     POP_TOP
               LOAD_CONST               3 ('invalid_dedupe_key_shape')
               RETURN_VALUE

192    L8:     END_FOR
               POP_ITER

195            LOAD_FAST_BORROW         2 (source)
               POP_JUMP_IF_NONE        36 (to L10)
               NOT_TAKEN

196            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (source)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       12 (to L9)
               NOT_TAKEN
               LOAD_FAST_BORROW         2 (source)
               LOAD_GLOBAL              8 (ALLOWED_DEDUPE_SOURCES)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN

197    L9:     LOAD_CONST               6 ('invalid_source')
               RETURN_VALUE

198   L10:     LOAD_CONST               5 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app\services\ingestion\email_dedupe_store.py", line 201>:
201           RESUME                   0
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

Disassembly of <code object _is_unique_violation at 0x0000018C17F95E60, file "app\services\ingestion\email_dedupe_store.py", line 201>:
 201           RESUME                   0

 207           NOP

 208   L1:     LOAD_GLOBAL              1 (repr + NULL)
               LOAD_FAST_BORROW         0 (exc)
               CALL                     1
               STORE_FAST               1 (s)

 211   L2:     LOAD_CONST               2 ('23505')
               LOAD_FAST                1 (s)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 212           LOAD_CONST               3 (True)
               RETURN_VALUE

 213   L3:     LOAD_FAST                1 (s)
               LOAD_ATTR                5 (lower + NULL|self)
               CALL                     0
               STORE_FAST               2 (lowered)

 215           LOAD_CONST               4 ('duplicate key value violates unique constraint')
               LOAD_FAST                2 (lowered)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L4)
               NOT_TAKEN
               POP_TOP

 216           LOAD_CONST               5 ('already exists')
               LOAD_FAST                2 (lowered)
               CONTAINS_OP              0 (in)

 214   L4:     RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 209           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L7)
               NOT_TAKEN
               POP_TOP

 210   L6:     POP_EXCEPT
               LOAD_CONST               1 (False)
               RETURN_VALUE

 209   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FBFEE0, file "app\services\ingestion\email_dedupe_store.py", line 224>:
224           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

226           LOAD_CONST               2 ('str')

224           LOAD_CONST               3 ('dedupe_key')

227           LOAD_CONST               2 ('str')

224           LOAD_CONST               4 ('source')

228           LOAD_CONST               2 ('str')

224           LOAD_CONST               5 ('pending_call_id')

229           LOAD_CONST               6 ('Optional[str]')

224           LOAD_CONST               7 ('ttl_hours')

230           LOAD_CONST               8 ('int')

224           LOAD_CONST               9 ('now')

231           LOAD_CONST              10 ('Any')

224           LOAD_CONST              11 ('return')

232           LOAD_CONST              12 ('Dict[str, Any]')

224           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object register_email_dedupe_key at 0x0000018C17ED5770, file "app\services\ingestion\email_dedupe_store.py", line 224>:
 224            RESUME                   0

 249            LOAD_GLOBAL              1 (_validate_inputs + NULL)

 250            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage_id, dedupe_key)
                LOAD_FAST_BORROW         2 (source)

 249            LOAD_CONST               1 (('brokerage_id', 'dedupe_key', 'source'))
                CALL_KW                  3
                STORE_FAST               6 (err)

 252            LOAD_FAST_BORROW         6 (err)
                POP_JUMP_IF_NONE        14 (to L1)
                NOT_TAKEN

 253            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               3 ('failed')
                LOAD_FAST_BORROW         6 (err)
                LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 255    L1:     LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               7 (bid)

 256            LOAD_FAST_BORROW         1 (dedupe_key)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR                7 (lower + NULL|self)
                CALL                     0
                STORE_FAST               8 (key)

 257            LOAD_FAST                2 (source)
                STORE_FAST               9 (src)

 259            LOAD_GLOBAL              9 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST              10 (db)

 260            LOAD_FAST_BORROW        10 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L2)
                NOT_TAKEN

 261            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 262            LOAD_CONST               5 ('warning')

 263            LOAD_CONST               6 ('durable_email_dedupe_unavailable')
                BUILD_LIST               1

 264            LOAD_CONST               6 ('durable_email_dedupe_unavailable')

 261            LOAD_CONST               7 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 267    L2:     LOAD_GLOBAL             11 (_clamp_ttl_hours + NULL)
                LOAD_FAST_BORROW         4 (ttl_hours)
                CALL                     1
                STORE_FAST              11 (ttl)

 268            LOAD_GLOBAL             13 (_now_dt + NULL)
                LOAD_FAST_BORROW         5 (now)
                CALL                     1
                STORE_FAST              12 (now_dt)

 269            LOAD_FAST_BORROW        12 (now_dt)
                LOAD_GLOBAL             15 (timedelta + NULL)
                LOAD_FAST_BORROW        11 (ttl)
                LOAD_CONST               8 (('hours',))
                CALL_KW                  1
                BINARY_OP                0 (+)
                STORE_FAST              13 (expires_dt)

 272            LOAD_CONST               9 ('dedupe_key')
                LOAD_FAST_BORROW         8 (key)

 273            LOAD_CONST              10 ('brokerage_id')
                LOAD_FAST_BORROW         7 (bid)

 274            LOAD_CONST              11 ('source')
                LOAD_FAST_BORROW         9 (src)

 275            LOAD_CONST              12 ('created_at')
                LOAD_GLOBAL             17 (_iso + NULL)
                LOAD_FAST_BORROW        12 (now_dt)
                CALL                     1

 276            LOAD_CONST              13 ('expires_at')
                LOAD_GLOBAL             17 (_iso + NULL)
                LOAD_FAST_BORROW        13 (expires_dt)
                CALL                     1

 271            BUILD_MAP                5
                STORE_FAST              14 (row)

 278            LOAD_GLOBAL             19 (isinstance + NULL)
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

 279            LOAD_FAST_BORROW         3 (pending_call_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                LOAD_FAST_BORROW        14 (row)
                LOAD_CONST              14 ('first_seen_pending_call_id')
                STORE_SUBSCR

 281    L3:     NOP

 282    L4:     LOAD_FAST_BORROW        10 (db)
                LOAD_ATTR               23 (table + NULL|self)
                LOAD_GLOBAL             24 (_TABLE)
                CALL                     1
                LOAD_ATTR               27 (insert + NULL|self)
                LOAD_FAST_BORROW        14 (row)
                CALL                     1
                LOAD_ATTR               29 (execute + NULL|self)
                CALL                     0
                POP_TOP

 283            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 284            LOAD_CONST              15 ('ok')
                LOAD_CONST              16 (False)

 283            LOAD_CONST              17 (('status', 'duplicate'))
                CALL_KW                  2
        L5:     RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 286            LOAD_GLOBAL             30 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      127 (to L14)
                NOT_TAKEN
                STORE_FAST              15 (e)

 287    L7:     LOAD_GLOBAL             33 (_is_unique_violation + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L10)
                NOT_TAKEN

 289            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 290            LOAD_CONST              15 ('ok')
                LOAD_CONST              18 (True)

 289            LOAD_CONST              17 (('status', 'duplicate'))
                CALL_KW                  2
        L8:     SWAP                     2
        L9:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RETURN_VALUE

 292   L10:     LOAD_GLOBAL             34 (logger)
                LOAD_ATTR               37 (warning + NULL|self)

 293            LOAD_CONST              19 ('register_email_dedupe_key db error type=')
                LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 292            CALL                     1
                POP_TOP

 295            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 296            LOAD_CONST               5 ('warning')

 298            LOAD_CONST               6 ('durable_email_dedupe_unavailable')

 299            LOAD_CONST              20 ('db_write_failed:')
                LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 297            BUILD_LIST               2

 301            LOAD_CONST               6 ('durable_email_dedupe_unavailable')

 295            LOAD_CONST               7 (('status', 'warnings', 'error_code'))
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

 286   L14:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\services\ingestion\email_dedupe_store.py", line 305>:
305           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

307           LOAD_CONST               2 ('str')

305           LOAD_CONST               3 ('dedupe_key')

308           LOAD_CONST               2 ('str')

305           LOAD_CONST               4 ('now')

309           LOAD_CONST               5 ('Any')

305           LOAD_CONST               6 ('return')

310           LOAD_CONST               7 ('Dict[str, Any]')

305           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object is_duplicate_email_dedupe_key at 0x0000018C17ED5F20, file "app\services\ingestion\email_dedupe_store.py", line 305>:
 305            RESUME                   0

 317            LOAD_GLOBAL              1 (_validate_inputs + NULL)

 318            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage_id, dedupe_key)
                LOAD_CONST               1 (None)

 317            LOAD_CONST               2 (('brokerage_id', 'dedupe_key', 'source'))
                CALL_KW                  3
                STORE_FAST               3 (err)

 320            LOAD_FAST_BORROW         3 (err)
                POP_JUMP_IF_NONE        14 (to L1)
                NOT_TAKEN

 321            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               3 ('failed')
                LOAD_FAST_BORROW         3 (err)
                LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 323    L1:     LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               4 (bid)

 324            LOAD_FAST_BORROW         1 (dedupe_key)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR                7 (lower + NULL|self)
                CALL                     0
                STORE_FAST               5 (key)

 325            LOAD_GLOBAL              9 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               6 (db)

 326            LOAD_FAST_BORROW         6 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L2)
                NOT_TAKEN

 327            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 328            LOAD_CONST               5 ('warning')

 329            LOAD_CONST               6 ('durable_email_dedupe_unavailable')
                BUILD_LIST               1

 330            LOAD_CONST               6 ('durable_email_dedupe_unavailable')

 327            LOAD_CONST               7 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 333    L2:     LOAD_GLOBAL             11 (_iso + NULL)
                LOAD_GLOBAL             13 (_now_dt + NULL)
                LOAD_FAST_BORROW         2 (now)
                CALL                     1
                CALL                     1
                STORE_FAST               7 (when)

 334            NOP

 336    L3:     LOAD_FAST_BORROW         6 (db)
                LOAD_ATTR               15 (table + NULL|self)
                LOAD_GLOBAL             16 (_TABLE)
                CALL                     1

 337            LOAD_ATTR               19 (select + NULL|self)
                LOAD_CONST               8 ('dedupe_key, expires_at')
                CALL                     1

 338            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST               9 ('brokerage_id')
                LOAD_FAST_BORROW         4 (bid)
                CALL                     2

 339            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST              10 ('dedupe_key')
                LOAD_FAST_BORROW         5 (key)
                CALL                     2

 340            LOAD_ATTR               23 (gt + NULL|self)
                LOAD_CONST              11 ('expires_at')
                LOAD_FAST_BORROW         7 (when)
                CALL                     2

 341            LOAD_ATTR               25 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 342            LOAD_ATTR               27 (execute + NULL|self)
                CALL                     0

 335            STORE_FAST               8 (result)

 344            LOAD_GLOBAL             29 (list + NULL)
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

 345            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 346            LOAD_CONST              13 ('ok')
                LOAD_GLOBAL             33 (bool + NULL)
                LOAD_FAST_BORROW         9 (rows)
                CALL                     1

 345            LOAD_CONST              14 (('status', 'duplicate'))
                CALL_KW                  2
        L5:     RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 348            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       92 (to L11)
                NOT_TAKEN
                STORE_FAST              10 (e)

 349    L7:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 350            LOAD_CONST              15 ('is_duplicate_email_dedupe_key db error type=')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 349            CALL                     1
                POP_TOP

 352            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 353            LOAD_CONST               5 ('warning')

 355            LOAD_CONST               6 ('durable_email_dedupe_unavailable')

 356            LOAD_CONST              16 ('db_read_failed:')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 354            BUILD_LIST               2

 358            LOAD_CONST               6 ('durable_email_dedupe_unavailable')

 352            LOAD_CONST               7 (('status', 'warnings', 'error_code'))
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

 348   L11:     RERAISE                  0

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L6 [0]
  L6 to L7 -> L12 [1] lasti
  L7 to L8 -> L10 [1] lasti
  L8 to L9 -> L12 [1] lasti
  L10 to L12 -> L12 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app\services\ingestion\email_dedupe_store.py", line 362>:
362           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

364           LOAD_CONST               2 ('str')

362           LOAD_CONST               3 ('dedupe_key')

365           LOAD_CONST               2 ('str')

362           LOAD_CONST               4 ('now')

366           LOAD_CONST               5 ('Any')

362           LOAD_CONST               6 ('return')

367           LOAD_CONST               7 ('Dict[str, Any]')

362           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object mark_email_duplicate_seen at 0x0000018C17ED6800, file "app\services\ingestion\email_dedupe_store.py", line 362>:
 362            RESUME                   0

 379            LOAD_GLOBAL              1 (_validate_inputs + NULL)

 380            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage_id, dedupe_key)
                LOAD_CONST               1 (None)

 379            LOAD_CONST               2 (('brokerage_id', 'dedupe_key', 'source'))
                CALL_KW                  3
                STORE_FAST               3 (err)

 382            LOAD_FAST_BORROW         3 (err)
                POP_JUMP_IF_NONE        14 (to L1)
                NOT_TAKEN

 383            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               3 ('failed')
                LOAD_FAST_BORROW         3 (err)
                LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 385    L1:     LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               4 (bid)

 386            LOAD_FAST_BORROW         1 (dedupe_key)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR                7 (lower + NULL|self)
                CALL                     0
                STORE_FAST               5 (key)

 387            LOAD_GLOBAL              9 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               6 (db)

 388            LOAD_FAST_BORROW         6 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L2)
                NOT_TAKEN

 389            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 390            LOAD_CONST               5 ('warning')

 391            LOAD_CONST               6 ('durable_email_dedupe_unavailable')
                BUILD_LIST               1

 392            LOAD_CONST               6 ('durable_email_dedupe_unavailable')

 389            LOAD_CONST               7 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 395    L2:     LOAD_GLOBAL             11 (_iso + NULL)
                LOAD_GLOBAL             13 (_now_dt + NULL)
                LOAD_FAST_BORROW         2 (now)
                CALL                     1
                CALL                     1
                STORE_FAST               7 (now_iso)

 396            NOP

 399    L3:     LOAD_FAST_BORROW         6 (db)
                LOAD_ATTR               15 (table + NULL|self)
                LOAD_GLOBAL             16 (_TABLE)
                CALL                     1

 400            LOAD_ATTR               19 (select + NULL|self)
                LOAD_CONST               8 ('duplicate_count')
                CALL                     1

 401            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST               9 ('brokerage_id')
                LOAD_FAST_BORROW         4 (bid)
                CALL                     2

 402            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST              10 ('dedupe_key')
                LOAD_FAST_BORROW         5 (key)
                CALL                     2

 403            LOAD_ATTR               23 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 404            LOAD_ATTR               25 (execute + NULL|self)
                CALL                     0

 398            STORE_FAST               8 (result)

 406            LOAD_GLOBAL             27 (list + NULL)
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

 407            LOAD_FAST_BORROW         9 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        16 (to L8)
        L5:     NOT_TAKEN

 408    L6:     LOAD_GLOBAL              3 (_safe_envelope + NULL)

 409            LOAD_CONST               5 ('warning')

 410            LOAD_CONST              12 ('email_dedupe_row_not_found')
                BUILD_LIST               1

 411            LOAD_CONST              12 ('email_dedupe_row_not_found')

 408            LOAD_CONST               7 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
        L7:     RETURN_VALUE

 413    L8:     LOAD_FAST_BORROW         9 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               8 ('duplicate_count')
                CALL                     1
                STORE_FAST              10 (current)

 414            LOAD_GLOBAL             33 (isinstance + NULL)
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

 415    L9:     LOAD_SMALL_INT           0
                STORE_FAST              10 (current)

 417   L10:     LOAD_CONST               8 ('duplicate_count')
                LOAD_FAST_BORROW        10 (current)
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)

 418            LOAD_CONST              13 ('last_duplicate_at')
                LOAD_FAST_BORROW         7 (now_iso)

 416            BUILD_MAP                2
                STORE_FAST              11 (patch)

 421            LOAD_FAST_BORROW         6 (db)
                LOAD_ATTR               15 (table + NULL|self)
                LOAD_GLOBAL             16 (_TABLE)
                CALL                     1

 422            LOAD_ATTR               37 (update + NULL|self)
                LOAD_FAST_BORROW        11 (patch)
                CALL                     1

 423            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST               9 ('brokerage_id')
                LOAD_FAST_BORROW         4 (bid)
                CALL                     2

 424            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST              10 ('dedupe_key')
                LOAD_FAST_BORROW         5 (key)
                CALL                     2

 425            LOAD_ATTR               25 (execute + NULL|self)
                CALL                     0

 420            STORE_FAST              12 (update_result)

 427            LOAD_GLOBAL             27 (list + NULL)
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

 428            LOAD_FAST_BORROW        13 (updated_rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L17)
       L14:     NOT_TAKEN

 429   L15:     LOAD_GLOBAL              3 (_safe_envelope + NULL)

 430            LOAD_CONST               5 ('warning')

 431            LOAD_CONST              14 ('email_dedupe_update_returned_no_rows')
                BUILD_LIST               1

 429            LOAD_CONST              15 (('status', 'warnings'))
                CALL_KW                  2
       L16:     RETURN_VALUE

 433   L17:     LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST              16 ('ok')
                LOAD_CONST              17 (True)
                LOAD_CONST              18 (('status', 'duplicate'))
                CALL_KW                  2
       L18:     RETURN_VALUE

  --   L19:     PUSH_EXC_INFO

 434            LOAD_GLOBAL             38 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       92 (to L24)
                NOT_TAKEN
                STORE_FAST              14 (e)

 435   L20:     LOAD_GLOBAL             40 (logger)
                LOAD_ATTR               43 (warning + NULL|self)

 436            LOAD_CONST              19 ('mark_email_duplicate_seen db error type=')
                LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 435            CALL                     1
                POP_TOP

 438            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 439            LOAD_CONST               5 ('warning')

 441            LOAD_CONST               6 ('durable_email_dedupe_unavailable')

 442            LOAD_CONST              20 ('db_write_failed:')
                LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 440            BUILD_LIST               2

 444            LOAD_CONST               6 ('durable_email_dedupe_unavailable')

 438            LOAD_CONST               7 (('status', 'warnings', 'error_code'))
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

 434   L24:     RERAISE                  0

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
