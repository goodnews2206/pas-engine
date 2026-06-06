# ingestion/email_dedupe

- **pyc:** `app\services\ingestion\__pycache__\email_dedupe.cpython-314.pyc`
- **expected source path (absent):** `app\services\ingestion/email_dedupe.py`
- **co_filename (from bytecode):** `app\services\ingestion\email_dedupe.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** ingestion

## Module docstring

```
PAS165 — Email lead deduplication (process-local v1).

Deterministic dedupe key + 24-hour TTL registry so that a
forwarder-loop or a manual re-forward of the same Zillow /
Realtor / Facebook / website lead email does NOT produce two
pending calls (which would cause PAS to dial the same lead
twice — an instant trust-killer for any real brokerage demo).

Doctrine carried by every helper here:

* The dedupe key NEVER includes a timestamp, a UUID, or any
  randomness. Two callers given the same email payload must
  produce the same key.
* The dedupe key NEVER includes ``brokerage_id``. The PAS165
  scope is "is this exact email being ingested twice?" — the
  brokerage is resolved from auth and is orthogonal to the
  dedupe identity.
* The dedupe key is NEVER returned to the route caller.
* The dedupe key is NEVER placed in an event payload.
* The raw body is NEVER persisted by the dedupe layer. The
  body excerpt is hashed and the hash is what enters the key.
* The registry is process-local. A real durable replacement
  (Redis / a Supabase table with a unique index) is a future
  phase. Every check / register surfaces the limitation as
  ``email_dedupe_store_is_process_local`` so the operator
  cannot mistake the in-memory map for durable dedupe.
* The registry is RLock-protected. Expired entries are
  cleaned opportunistically on every check / register call.
* Every public helper is non-raising; failures degrade to
  "not a duplicate" so the dedupe layer can never block
  legitimate ingestion on its own bug.

Public surface:

  * ``build_email_dedupe_key(...)``
  * ``is_duplicate_email_lead(key, *, now=None)``
  * ``register_email_lead_dedupe(key, *, source=None, now=None)``
  * ``cleanup_expired_dedupe_entries(*, now=None)``
  * ``reset_email_dedupe_registry_for_tests()``
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `datetime`, `hashlib`, `logging`, `re`, `threading`, `timedelta`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_hash`, `_iso`, `_normalise_body_excerpt`, `_normalise_email`, `_normalise_phone`, `_normalise_phone_or_email`, `_normalise_sender`, `_normalise_source`, `_normalise_subject`, `_now_dt`, `_opportunistic_cleanup_locked`, `_peek_dedupe_registry_for_tests`, `_safe_str`, `build_email_dedupe_key`, `cleanup_expired_dedupe_entries`, `is_duplicate_email_lead`, `register_email_lead_dedupe`, `reset_email_dedupe_registry_for_tests`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS165 — Email lead deduplication (process-local v1).\n\nDeterministic dedupe key + 24-hour TTL registry so that a\nforwarder-loop or a manual re-forward of the same Zillow /\nRealtor / Facebook / website lead email does NOT produce two\npending calls (which would cause PAS to dial the same lead\ntwice — an instant trust-killer for any real brokerage demo).\n\nDoctrine carried by every helper here:\n\n* The dedupe key NEVER includes a timestamp, a UUID, or any\n  randomness. Two callers given the same email payload must\n  produce the same key.\n* The dedupe key NEVER includes ``brokerage_id``. The PAS165\n  scope is "is this exact email being ingested twice?" — the\n  brokerage is resolved from auth and is orthogonal to the\n  dedupe identity.\n* The dedupe key is NEVER returned to the route caller.\n* The dedupe key is NEVER placed in an event payload.\n* The raw body is NEVER persisted by the dedupe layer. The\n  body excerpt is hashed and the hash is what enters the key.\n* The registry is process-local. A real durable replacement\n  (Redis / a Supabase table with a unique index) is a future\n  phase. Every check / register surfaces the limitation as\n  ``email_dedupe_store_is_process_local`` so the operator\n  cannot mistake the in-memory map for durable dedupe.\n* The registry is RLock-protected. Expired entries are\n  cleaned opportunistically on every check / register call.\n* Every public helper is non-raising; failures degrade to\n  "not a duplicate" so the dedupe layer can never block\n  legitimate ingestion on its own bug.\n\nPublic surface:\n\n  * ``build_email_dedupe_key(...)``\n  * ``is_duplicate_email_lead(key, *, now=None)``\n  * ``register_email_lead_dedupe(key, *, source=None, now=None)``\n  * ``cleanup_expired_dedupe_entries(*, now=None)``\n  * ``reset_email_dedupe_registry_for_tests()``\n'
- 'pas.ingestion.email_dedupe'
- '\\s+'
- '<(script|style)[^>]*>.*?</\\1>'
- '<[^>]+>'
- 'Dict[str, Dict[str, Any]]'
- '_DEDUPE_REGISTRY'
- 'now'
- 'source'
- 'Any'
- 'return'
- 'datetime'
- 'Return ``now`` as an aware UTC datetime. NEVER raises.'
- '+00:00'
- 'str'
- 'seconds'
- 'val'
- 'utf-8'
- 'replace'
- 'unknown'
- 'sender'
- 'subject'
- 'phone'
- 'email'
- 'Identity component for the dedupe key. Phone wins when\npresent (PAS dials phones, not emails); email is the\nfallback.'
- 'phone:'
- 'email:'
- 'anon:'
- 'body'
- 'Strip HTML, collapse whitespace, lower-case, take the\nfirst ``_BODY_EXCERPT_MAX_CHARS`` characters. The full body\nis NEVER stored; only this normalised excerpt is hashed.'
- 'text'
- '_hash unexpected error type='
- 'Optional[str]'
- 'Build a deterministic SHA-256 hex digest representing the\n"identity" of an inbound forwarded email.\n\nAlgorithm::\n\n    normalized_source\n    + "|" + normalized_sender\n    + "|" + normalized_subject\n    + "|" + normalized_phone_or_email\n    + "|" + sha256(normalized_body_excerpt)\n    → sha256(<that string>) → hex\n\nProperties:\n  * deterministic (no timestamps, no UUIDs);\n  * does NOT include ``brokerage_id``;\n  * never raises;\n  * the body excerpt is HASHED before being inserted into\n    the canonical string, so the registry never holds the\n    raw body even transiently.\n'
- 'now_dt'
- 'int'
- 'Caller MUST hold ``_DEDUPE_LOCK``. Removes expired\nentries and returns the count removed. NEVER raises.'
- 'created_at'
- 'dedupe_key'
- 'bool'
- 'Return True when ``dedupe_key`` is present in the\nregistry and not yet expired. NEVER raises. NEVER echoes\nthe key in logs.'
- 'Dict[str, Any]'
- "Register a dedupe key. If the key is already present\n(and not yet expired) the registration is a no-op; the\nreturn envelope's ``status`` is ``duplicate``. Otherwise\nthe key is inserted with the current timestamp and\n``status`` is ``registered``.\n\nReturns a closed-shape envelope. NEVER raises. NEVER\nechoes the key.\n\nThe envelope is structural ONLY — no key, no body, no\nphone/email/name — so it is safe for the caller to log /\nforward.\n"
- 'status'
- 'failed'
- 'warnings'
- 'missing_dedupe_key'
- 'duplicate'
- 'duplicate_email_lead'
- 'email_dedupe_store_is_process_local'
- 'registered'
- 'Operator-callable cleanup. Returns the count of removed\nentries. NEVER raises.'
- 'removed'
- 'remaining'
- 'ttl_seconds'
- 'None'
- 'Test-only helper to flush the registry between tests.'
- 'Test-only snapshot. Returns a shallow copy.'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS165 — Email lead deduplication (process-local v1).\n\nDeterministic dedupe key + 24-hour TTL registry so that a\nforwarder-loop or a manual re-forward of the same Zillow /\nRealtor / Facebook / website lead email does NOT produce two\npending calls (which would cause PAS to dial the same lead\ntwice — an instant trust-killer for any real brokerage demo).\n\nDoctrine carried by every helper here:\n\n* The dedupe key NEVER includes a timestamp, a UUID, or any\n  randomness. Two callers given the same email payload must\n  produce the same key.\n* The dedupe key NEVER includes ``brokerage_id``. The PAS165\n  scope is "is this exact email being ingested twice?" — the\n  brokerage is resolved from auth and is orthogonal to the\n  dedupe identity.\n* The dedupe key is NEVER returned to the route caller.\n* The dedupe key is NEVER placed in an event payload.\n* The raw body is NEVER persisted by the dedupe layer. The\n  body excerpt is hashed and the hash is what enters the key.\n* The registry is process-local. A real durable replacement\n  (Redis / a Supabase table with a unique index) is a future\n  phase. Every check / register surfaces the limitation as\n  ``email_dedupe_store_is_process_local`` so the operator\n  cannot mistake the in-memory map for durable dedupe.\n* The registry is RLock-protected. Expired entries are\n  cleaned opportunistically on every check / register call.\n* Every public helper is non-raising; failures degrade to\n  "not a duplicate" so the dedupe layer can never block\n  legitimate ingestion on its own bug.\n\nPublic surface:\n\n  * ``build_email_dedupe_key(...)``\n  * ``is_duplicate_email_lead(key, *, now=None)``\n  * ``register_email_lead_dedupe(key, *, source=None, now=None)``\n  * ``cleanup_expired_dedupe_entries(*, now=None)``\n  * ``reset_email_dedupe_registry_for_tests()``\n')
               STORE_NAME               1 (__doc__)

  43           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  45           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (hashlib)
               STORE_NAME               4 (hashlib)

  46           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (logging)
               STORE_NAME               5 (logging)

  47           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (re)
               STORE_NAME               6 (re)

  48           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (threading)
               STORE_NAME               7 (threading)

  49           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timedelta', 'timezone'))
               IMPORT_NAME              8 (datetime)
               IMPORT_FROM              8 (datetime)
               STORE_NAME               8 (datetime)
               IMPORT_FROM              9 (timedelta)
               STORE_NAME               9 (timedelta)
               IMPORT_FROM             10 (timezone)
               STORE_NAME              10 (timezone)
               POP_TOP

  50           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (Any)
               STORE_NAME              12 (Any)
               IMPORT_FROM             13 (Dict)
               STORE_NAME              13 (Dict)
               IMPORT_FROM             14 (List)
               STORE_NAME              14 (List)
               IMPORT_FROM             15 (Optional)
               STORE_NAME              15 (Optional)
               POP_TOP

  53           LOAD_NAME                5 (logging)
               LOAD_ATTR               32 (getLogger)
               PUSH_NULL
               LOAD_CONST               5 ('pas.ingestion.email_dedupe')
               CALL                     1
               STORE_NAME              17 (logger)

  63           LOAD_CONST              50 (86400)
               STORE_NAME              18 (DEDUPE_TTL_SECONDS)

  69           LOAD_CONST               6 (4096)
               STORE_NAME              19 (_BODY_EXCERPT_MAX_CHARS)

  72           LOAD_NAME                6 (re)
               LOAD_ATTR               40 (compile)
               PUSH_NULL
               LOAD_CONST               7 ('\\s+')
               CALL                     1
               STORE_NAME              21 (_WS_RE)

  78           LOAD_NAME                6 (re)
               LOAD_ATTR               40 (compile)
               PUSH_NULL

  79           LOAD_CONST               8 ('<(script|style)[^>]*>.*?</\\1>')

  80           LOAD_NAME                6 (re)
               LOAD_ATTR               44 (DOTALL)
               LOAD_NAME                6 (re)
               LOAD_ATTR               46 (IGNORECASE)
               BINARY_OP                7 (|)

  78           CALL                     2
               STORE_NAME              24 (_HTML_SCRIPT_STYLE_RE)

  82           LOAD_NAME                6 (re)
               LOAD_ATTR               40 (compile)
               PUSH_NULL
               LOAD_CONST               9 ('<[^>]+>')
               CALL                     1
               STORE_NAME              25 (_HTML_TAG_RE)

  89           BUILD_MAP                0
               STORE_NAME              26 (_DEDUPE_REGISTRY)
               LOAD_CONST              10 ('Dict[str, Dict[str, Any]]')
               LOAD_NAME               27 (__annotations__)
               LOAD_CONST              11 ('_DEDUPE_REGISTRY')
               STORE_SUBSCR

  90           LOAD_NAME                7 (threading)
               LOAD_ATTR               56 (RLock)
               PUSH_NULL
               CALL                     0
               STORE_NAME              29 (_DEDUPE_LOCK)

  93           LOAD_CONST              51 ((None,))
               LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA1E30, file "app\services\ingestion\email_dedupe.py", line 93>)
               MAKE_FUNCTION
               LOAD_CONST              13 (<code object _now_dt at 0x0000018C17ED0510, file "app\services\ingestion\email_dedupe.py", line 93>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              30 (_now_dt)

 110           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA33C0, file "app\services\ingestion\email_dedupe.py", line 110>)
               MAKE_FUNCTION
               LOAD_CONST              15 (<code object _iso at 0x0000018C18025930, file "app\services\ingestion\email_dedupe.py", line 110>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_iso)

 118           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\ingestion\email_dedupe.py", line 118>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _safe_str at 0x0000018C1794EBB0, file "app\services\ingestion\email_dedupe.py", line 118>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_safe_str)

 134           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3B40, file "app\services\ingestion\email_dedupe.py", line 134>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _normalise_source at 0x0000018C18038670, file "app\services\ingestion\email_dedupe.py", line 134>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              33 (_normalise_source)

 139           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA3C30, file "app\services\ingestion\email_dedupe.py", line 139>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _normalise_sender at 0x0000018C17C49B80, file "app\services\ingestion\email_dedupe.py", line 139>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_normalise_sender)

 144           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3D20, file "app\services\ingestion\email_dedupe.py", line 144>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _normalise_subject at 0x0000018C17FE13E0, file "app\services\ingestion\email_dedupe.py", line 144>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (_normalise_subject)

 150           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3E10, file "app\services\ingestion\email_dedupe.py", line 150>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object _normalise_phone at 0x0000018C17F96140, file "app\services\ingestion\email_dedupe.py", line 150>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              36 (_normalise_phone)

 158           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA3F00, file "app\services\ingestion\email_dedupe.py", line 158>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object _normalise_email at 0x0000018C1802C4F0, file "app\services\ingestion\email_dedupe.py", line 158>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              37 (_normalise_email)

 163           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\ingestion\email_dedupe.py", line 163>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object _normalise_phone_or_email at 0x0000018C18038CB0, file "app\services\ingestion\email_dedupe.py", line 163>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (_normalise_phone_or_email)

 176           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA2010, file "app\services\ingestion\email_dedupe.py", line 176>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object _normalise_body_excerpt at 0x0000018C17EDAC30, file "app\services\ingestion\email_dedupe.py", line 176>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              39 (_normalise_body_excerpt)

 196           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA2100, file "app\services\ingestion\email_dedupe.py", line 196>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object _hash at 0x0000018C17EC57C0, file "app\services\ingestion\email_dedupe.py", line 196>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              40 (_hash)

 212           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C18090690, file "app\services\ingestion\email_dedupe.py", line 212>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object build_email_dedupe_key at 0x0000018C17FA92F0, file "app\services\ingestion\email_dedupe.py", line 212>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (build_email_dedupe_key)

 251           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA21F0, file "app\services\ingestion\email_dedupe.py", line 251>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object _opportunistic_cleanup_locked at 0x0000018C17ED3F20, file "app\services\ingestion\email_dedupe.py", line 251>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (_opportunistic_cleanup_locked)

 284           LOAD_CONST              38 ('now')

 287           LOAD_CONST               2 (None)

 284           BUILD_MAP                1
               LOAD_CONST              39 (<code object __annotate__ at 0x0000018C18024930, file "app\services\ingestion\email_dedupe.py", line 284>)
               MAKE_FUNCTION
               LOAD_CONST              40 (<code object is_duplicate_email_lead at 0x0000018C179A7290, file "app\services\ingestion\email_dedupe.py", line 284>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              43 (is_duplicate_email_lead)

 301           LOAD_CONST              41 ('source')

 304           LOAD_CONST               2 (None)

 301           LOAD_CONST              38 ('now')

 305           LOAD_CONST               2 (None)

 301           BUILD_MAP                2
               LOAD_CONST              42 (<code object __annotate__ at 0x0000018C18025630, file "app\services\ingestion\email_dedupe.py", line 301>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object register_email_lead_dedupe at 0x0000018C18190440, file "app\services\ingestion\email_dedupe.py", line 301>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              44 (register_email_lead_dedupe)

 351           LOAD_CONST              38 ('now')

 353           LOAD_CONST               2 (None)

 351           BUILD_MAP                1
               LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA2A60, file "app\services\ingestion\email_dedupe.py", line 351>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object cleanup_expired_dedupe_entries at 0x0000018C1800ABF0, file "app\services\ingestion\email_dedupe.py", line 351>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              45 (cleanup_expired_dedupe_entries)

 368           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\ingestion\email_dedupe.py", line 368>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object reset_email_dedupe_registry_for_tests at 0x0000018C17972550, file "app\services\ingestion\email_dedupe.py", line 368>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (reset_email_dedupe_registry_for_tests)

 374           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA2C40, file "app\services\ingestion\email_dedupe.py", line 374>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object _peek_dedupe_registry_for_tests at 0x0000018C1804C9F0, file "app\services\ingestion\email_dedupe.py", line 374>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (_peek_dedupe_registry_for_tests)

 380           BUILD_LIST               0
               LOAD_CONST              52 (('DEDUPE_TTL_SECONDS', 'build_email_dedupe_key', 'is_duplicate_email_lead', 'register_email_lead_dedupe', 'cleanup_expired_dedupe_entries', 'reset_email_dedupe_registry_for_tests'))
               LIST_EXTEND              1
               STORE_NAME              48 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "app\services\ingestion\email_dedupe.py", line 93>:
 93           RESUME                   0
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

Disassembly of <code object _now_dt at 0x0000018C17ED0510, file "app\services\ingestion\email_dedupe.py", line 93>:
  93            RESUME                   0

  95            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (now)
                LOAD_GLOBAL              2 (datetime)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       78 (to L2)
                NOT_TAKEN

  96            LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L1)
                NOT_TAKEN

  97            LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                RETURN_VALUE

  98    L1:     LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

  99    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (now)
                LOAD_GLOBAL             14 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      117 (to L6)
                NOT_TAKEN

 100            NOP

 101    L3:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               16 (fromisoformat)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_CONST               2 ('Z')
                LOAD_CONST               3 ('+00:00')
                CALL                     2
                CALL                     1
                STORE_FAST               1 (dt)

 102            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L4)
                NOT_TAKEN

 103            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST               1 (dt)

 104    L4:     LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
        L5:     RETURN_VALUE

 107    L6:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               20 (now)
                PUSH_NULL
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 105            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        4 (to L9)
                NOT_TAKEN
                POP_TOP

 106    L8:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 49 (to L6)

 105    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app\services\ingestion\email_dedupe.py", line 110>:
110           RESUME                   0
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

Disassembly of <code object _iso at 0x0000018C18025930, file "app\services\ingestion\email_dedupe.py", line 110>:
110           RESUME                   0

111           LOAD_FAST_BORROW         0 (dt)
              LOAD_ATTR                1 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\ingestion\email_dedupe.py", line 118>:
118           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('val')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_str at 0x0000018C1794EBB0, file "app\services\ingestion\email_dedupe.py", line 118>:
 118            RESUME                   0

 119            LOAD_FAST_BORROW         0 (val)
                POP_JUMP_IF_NOT_NONE     3 (to L1)
                NOT_TAKEN

 120            LOAD_CONST               1 ('')
                RETURN_VALUE

 121    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (val)
                LOAD_GLOBAL              2 (bytes)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       21 (to L4)
                NOT_TAKEN

 122            NOP

 123    L2:     LOAD_FAST_BORROW         0 (val)
                LOAD_ATTR                5 (decode + NULL|self)
                LOAD_CONST               2 ('utf-8')
                LOAD_CONST               3 ('replace')
                LOAD_CONST               4 (('errors',))
                CALL_KW                  2
        L3:     RETURN_VALUE

 126    L4:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (val)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        13 (to L7)
                NOT_TAKEN

 127            NOP

 128    L5:     LOAD_GLOBAL              9 (str + NULL)
                LOAD_FAST_BORROW         0 (val)
                CALL                     1
        L6:     RETURN_VALUE

 131    L7:     LOAD_FAST_BORROW         0 (val)
                RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

 124            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L10)
                NOT_TAKEN
                POP_TOP

 125    L9:     POP_EXCEPT
                LOAD_CONST               1 ('')
                RETURN_VALUE

 124   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L12:     PUSH_EXC_INFO

 129            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L14)
                NOT_TAKEN
                POP_TOP

 130   L13:     POP_EXCEPT
                LOAD_CONST               1 ('')
                RETURN_VALUE

 129   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L8 [0]
  L5 to L6 -> L12 [0]
  L8 to L9 -> L11 [1] lasti
  L10 to L11 -> L11 [1] lasti
  L12 to L13 -> L15 [1] lasti
  L14 to L15 -> L15 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app\services\ingestion\email_dedupe.py", line 134>:
134           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('source')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _normalise_source at 0x0000018C18038670, file "app\services\ingestion\email_dedupe.py", line 134>:
134           RESUME                   0

135           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (source)
              CALL                     1
              LOAD_ATTR                3 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR                5 (lower + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

136           LOAD_FAST                1 (s)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               0 ('unknown')
      L1:     RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app\services\ingestion\email_dedupe.py", line 139>:
139           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('sender')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _normalise_sender at 0x0000018C17C49B80, file "app\services\ingestion\email_dedupe.py", line 139>:
139           RESUME                   0

140           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (sender)
              CALL                     1
              LOAD_ATTR                3 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR                5 (lower + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

141           LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "app\services\ingestion\email_dedupe.py", line 144>:
144           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('subject')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _normalise_subject at 0x0000018C17FE13E0, file "app\services\ingestion\email_dedupe.py", line 144>:
144           RESUME                   0

145           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (subject)
              CALL                     1
              STORE_FAST               1 (s)

146           LOAD_GLOBAL              2 (_WS_RE)
              LOAD_ATTR                5 (sub + NULL|self)
              LOAD_CONST               0 (' ')
              LOAD_FAST_BORROW         1 (s)
              CALL                     2
              LOAD_ATTR                7 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR                9 (lower + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

147           LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "app\services\ingestion\email_dedupe.py", line 150>:
150           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('phone')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _normalise_phone at 0x0000018C17F96140, file "app\services\ingestion\email_dedupe.py", line 150>:
150           RESUME                   0

151           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (phone)
              CALL                     1
              LOAD_ATTR                3 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

152           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

153           LOAD_CONST               0 ('')
              RETURN_VALUE

154   L1:     LOAD_CONST               0 ('')
              LOAD_ATTR                5 (join + NULL|self)
              LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18038A30, file "app\services\ingestion\email_dedupe.py", line 154>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (s)
              GET_ITER
              CALL                     0
              CALL                     1
              STORE_FAST               2 (digits)

155           LOAD_FAST_BORROW         2 (digits)
              LOAD_ATTR                7 (lower + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18038A30, file "app\services\ingestion\email_dedupe.py", line 154>:
 154           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                37 (to L5)
               STORE_FAST_LOAD_FAST    17 (c, c)
               LOAD_ATTR                1 (isdigit + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        10 (to L4)
               NOT_TAKEN
               LOAD_FAST_BORROW         1 (c)
               LOAD_CONST               0 ('+')
               COMPARE_OP              88 (bool(==))
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           33 (to L2)
       L4:     LOAD_FAST_BORROW         1 (c)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           39 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "app\services\ingestion\email_dedupe.py", line 158>:
158           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('email')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _normalise_email at 0x0000018C1802C4F0, file "app\services\ingestion\email_dedupe.py", line 158>:
158           RESUME                   0

159           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (email)
              CALL                     1
              LOAD_ATTR                3 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR                5 (lower + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

160           LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\ingestion\email_dedupe.py", line 163>:
163           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('phone')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('email')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('str')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _normalise_phone_or_email at 0x0000018C18038CB0, file "app\services\ingestion\email_dedupe.py", line 163>:
163           RESUME                   0

167           LOAD_GLOBAL              1 (_normalise_phone + NULL)
              LOAD_FAST_BORROW         0 (phone)
              CALL                     1
              STORE_FAST               2 (p)

168           LOAD_FAST_BORROW         2 (p)
              TO_BOOL
              POP_JUMP_IF_FALSE        6 (to L1)
              NOT_TAKEN

169           LOAD_CONST               1 ('phone:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2
              RETURN_VALUE

170   L1:     LOAD_GLOBAL              3 (_normalise_email + NULL)
              LOAD_FAST_BORROW         1 (email)
              CALL                     1
              STORE_FAST               3 (e)

171           LOAD_FAST_BORROW         3 (e)
              TO_BOOL
              POP_JUMP_IF_FALSE        6 (to L2)
              NOT_TAKEN

172           LOAD_CONST               2 ('email:')
              LOAD_FAST_BORROW         3 (e)
              FORMAT_SIMPLE
              BUILD_STRING             2
              RETURN_VALUE

173   L2:     LOAD_CONST               3 ('anon:')
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "app\services\ingestion\email_dedupe.py", line 176>:
176           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _normalise_body_excerpt at 0x0000018C17EDAC30, file "app\services\ingestion\email_dedupe.py", line 176>:
 176           RESUME                   0

 180           LOAD_GLOBAL              1 (_safe_str + NULL)
               LOAD_FAST_BORROW         0 (body)
               CALL                     1
               STORE_FAST               1 (s)

 181           LOAD_FAST_BORROW         1 (s)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

 182           LOAD_CONST               1 ('')
               RETURN_VALUE

 183   L1:     NOP

 184   L2:     LOAD_GLOBAL              2 (_HTML_SCRIPT_STYLE_RE)
               LOAD_ATTR                5 (sub + NULL|self)
               LOAD_CONST               2 (' ')
               LOAD_FAST_BORROW         1 (s)
               CALL                     2
               STORE_FAST               1 (s)

 185           LOAD_GLOBAL              6 (_HTML_TAG_RE)
               LOAD_ATTR                5 (sub + NULL|self)
               LOAD_CONST               2 (' ')
               LOAD_FAST_BORROW         1 (s)
               CALL                     2
               STORE_FAST               1 (s)

 190   L3:     LOAD_GLOBAL             10 (_WS_RE)
               LOAD_ATTR                5 (sub + NULL|self)
               LOAD_CONST               2 (' ')
               LOAD_FAST_BORROW         1 (s)
               CALL                     2
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               LOAD_ATTR               15 (lower + NULL|self)
               CALL                     0
               STORE_FAST               1 (s)

 191           LOAD_GLOBAL             17 (len + NULL)
               LOAD_FAST_BORROW         1 (s)
               CALL                     1
               LOAD_GLOBAL             18 (_BODY_EXCERPT_MAX_CHARS)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE       10 (to L4)
               NOT_TAKEN

 192           LOAD_FAST_BORROW         1 (s)
               LOAD_CONST               3 (None)
               LOAD_GLOBAL             18 (_BODY_EXCERPT_MAX_CHARS)
               BINARY_SLICE
               STORE_FAST               1 (s)

 193   L4:     LOAD_FAST_BORROW         1 (s)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 186           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        4 (to L7)
               NOT_TAKEN
               POP_TOP

 189   L6:     POP_EXCEPT
               JUMP_BACKWARD_NO_INTERRUPT 94 (to L3)

 186   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app\services\ingestion\email_dedupe.py", line 196>:
196           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('text')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _hash at 0x0000018C17EC57C0, file "app\services\ingestion\email_dedupe.py", line 196>:
 196           RESUME                   0

 197           NOP

 198   L1:     LOAD_GLOBAL              0 (hashlib)
               LOAD_ATTR                2 (sha256)
               PUSH_NULL

 199           LOAD_FAST_BORROW         0 (text)
               LOAD_ATTR                5 (encode + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('errors',))
               CALL_KW                  2

 198           CALL                     1

 200           LOAD_ATTR                7 (hexdigest + NULL|self)
               CALL                     0

 198   L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 201           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       90 (to L8)
               NOT_TAKEN
               STORE_FAST               1 (e)

 202   L4:     LOAD_GLOBAL             10 (logger)
               LOAD_ATTR               13 (warning + NULL|self)

 203           LOAD_CONST               3 ('_hash unexpected error type=')
               LOAD_GLOBAL             15 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               16 (__name__)
               FORMAT_SIMPLE
               BUILD_STRING             2

 202           CALL                     1
               POP_TOP

 205           LOAD_GLOBAL              0 (hashlib)
               LOAD_ATTR                2 (sha256)
               PUSH_NULL
               LOAD_CONST               4 (b'')
               CALL                     1
               LOAD_ATTR                7 (hexdigest + NULL|self)
               CALL                     0
       L5:     SWAP                     2
       L6:     POP_EXCEPT
               LOAD_CONST               5 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RETURN_VALUE

  --   L7:     LOAD_CONST               5 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 201   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L9 [1] lasti
  L4 to L5 -> L7 [1] lasti
  L5 to L6 -> L9 [1] lasti
  L7 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18090690, file "app\services\ingestion\email_dedupe.py", line 212>:
212           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('source')

214           LOAD_CONST               2 ('Optional[str]')

212           LOAD_CONST               3 ('sender')

215           LOAD_CONST               2 ('Optional[str]')

212           LOAD_CONST               4 ('subject')

216           LOAD_CONST               2 ('Optional[str]')

212           LOAD_CONST               5 ('body')

217           LOAD_CONST               2 ('Optional[str]')

212           LOAD_CONST               6 ('phone')

218           LOAD_CONST               2 ('Optional[str]')

212           LOAD_CONST               7 ('email')

219           LOAD_CONST               2 ('Optional[str]')

212           LOAD_CONST               8 ('return')

220           LOAD_CONST               9 ('str')

212           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object build_email_dedupe_key at 0x0000018C17FA92F0, file "app\services\ingestion\email_dedupe.py", line 212>:
212           RESUME                   0

241           LOAD_GLOBAL              1 (_normalise_source + NULL)
              LOAD_FAST_BORROW         0 (source)
              CALL                     1
              STORE_FAST               6 (src_n)

242           LOAD_GLOBAL              3 (_normalise_sender + NULL)
              LOAD_FAST_BORROW         1 (sender)
              CALL                     1
              STORE_FAST               7 (sender_n)

243           LOAD_GLOBAL              5 (_normalise_subject + NULL)
              LOAD_FAST_BORROW         2 (subject)
              CALL                     1
              STORE_FAST               8 (subject_n)

244           LOAD_GLOBAL              7 (_normalise_phone_or_email + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (phone, email)
              CALL                     2
              STORE_FAST               9 (ident_n)

245           LOAD_GLOBAL              9 (_normalise_body_excerpt + NULL)
              LOAD_FAST_BORROW         3 (body)
              CALL                     1
              STORE_FAST              10 (body_n)

246           LOAD_GLOBAL             11 (_hash + NULL)
              LOAD_FAST_BORROW        10 (body_n)
              CALL                     1
              STORE_FAST              11 (body_h)

247           LOAD_FAST_BORROW         6 (src_n)
              FORMAT_SIMPLE
              LOAD_CONST               1 ('|')
              LOAD_FAST_BORROW         7 (sender_n)
              FORMAT_SIMPLE
              LOAD_CONST               1 ('|')
              LOAD_FAST_BORROW         8 (subject_n)
              FORMAT_SIMPLE
              LOAD_CONST               1 ('|')
              LOAD_FAST_BORROW         9 (ident_n)
              FORMAT_SIMPLE
              LOAD_CONST               1 ('|')
              LOAD_FAST_BORROW        11 (body_h)
              FORMAT_SIMPLE
              BUILD_STRING             9
              STORE_FAST              12 (canonical)

248           LOAD_GLOBAL             11 (_hash + NULL)
              LOAD_FAST_BORROW        12 (canonical)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app\services\ingestion\email_dedupe.py", line 251>:
251           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('now_dt')
              LOAD_CONST               2 ('datetime')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _opportunistic_cleanup_locked at 0x0000018C17ED3F20, file "app\services\ingestion\email_dedupe.py", line 251>:
 251            RESUME                   0

 254            LOAD_GLOBAL              0 (_DEDUPE_REGISTRY)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 255            LOAD_SMALL_INT           0
                RETURN_VALUE

 256    L1:     LOAD_FAST_BORROW         0 (now_dt)
                LOAD_GLOBAL              3 (timedelta + NULL)
                LOAD_GLOBAL              4 (DEDUPE_TTL_SECONDS)
                LOAD_CONST               1 (('seconds',))
                CALL_KW                  1
                BINARY_OP               10 (-)
                STORE_FAST               1 (cutoff)

 257            LOAD_SMALL_INT           0
                STORE_FAST               2 (removed)

 258            BUILD_LIST               0
                STORE_FAST               3 (expired_keys)

 259            LOAD_GLOBAL              0 (_DEDUPE_REGISTRY)
                LOAD_ATTR                7 (items + NULL|self)
                CALL                     0
                GET_ITER
        L2:     FOR_ITER               173 (to L7)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   69 (key, meta)

 260            LOAD_FAST_BORROW         5 (meta)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               2 ('created_at')
                CALL                     1
                STORE_FAST               6 (created)

 261            LOAD_GLOBAL             11 (isinstance + NULL)
                LOAD_FAST_BORROW         6 (created)
                LOAD_GLOBAL             12 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        20 (to L3)
                NOT_TAKEN

 262            LOAD_FAST_BORROW         3 (expired_keys)
                LOAD_ATTR               15 (append + NULL|self)
                LOAD_FAST_BORROW         4 (key)
                CALL                     1
                POP_TOP

 263            JUMP_BACKWARD           63 (to L2)

 264    L3:     NOP

 265    L4:     LOAD_GLOBAL             16 (datetime)
                LOAD_ATTR               18 (fromisoformat)
                PUSH_NULL

 266            LOAD_FAST_BORROW         6 (created)
                LOAD_ATTR               21 (replace + NULL|self)
                LOAD_CONST               3 ('Z')
                LOAD_CONST               4 ('+00:00')
                CALL                     2

 265            CALL                     1
                STORE_FAST               7 (created_dt)

 268            LOAD_FAST_BORROW         7 (created_dt)
                LOAD_ATTR               22 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L5)
                NOT_TAKEN

 269            LOAD_FAST_BORROW         7 (created_dt)
                LOAD_ATTR               21 (replace + NULL|self)
                LOAD_GLOBAL             24 (timezone)
                LOAD_ATTR               26 (utc)
                LOAD_CONST               5 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST               7 (created_dt)

 273    L5:     LOAD_FAST_LOAD_FAST    113 (created_dt, cutoff)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD          156 (to L2)

 274    L6:     LOAD_FAST                3 (expired_keys)
                LOAD_ATTR               15 (append + NULL|self)
                LOAD_FAST                4 (key)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          175 (to L2)

 259    L7:     END_FOR
                POP_ITER

 275            LOAD_FAST_BORROW         3 (expired_keys)
                GET_ITER
        L8:     FOR_ITER                20 (to L11)
                STORE_FAST               4 (key)

 276            NOP

 277    L9:     LOAD_GLOBAL              0 (_DEDUPE_REGISTRY)
                LOAD_FAST_BORROW         4 (key)
                DELETE_SUBSCR

 278            LOAD_FAST_BORROW         2 (removed)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               2 (removed)
       L10:     JUMP_BACKWARD           22 (to L8)

 275   L11:     END_FOR
                POP_ITER

 281            LOAD_FAST_BORROW         2 (removed)
                RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 270            LOAD_GLOBAL             28 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       22 (to L14)
                NOT_TAKEN
                POP_TOP

 271            LOAD_FAST                3 (expired_keys)
                LOAD_ATTR               15 (append + NULL|self)
                LOAD_FAST                4 (key)
                CALL                     1
                POP_TOP

 272   L13:     POP_EXCEPT
                JUMP_BACKWARD          236 (to L2)

 270   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L16:     PUSH_EXC_INFO

 279            LOAD_GLOBAL             30 (KeyError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L18)
                NOT_TAKEN
                POP_TOP

 280   L17:     POP_EXCEPT
                JUMP_BACKWARD           75 (to L8)

 279   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L12 [1]
  L9 to L10 -> L16 [1]
  L12 to L13 -> L15 [2] lasti
  L14 to L15 -> L15 [2] lasti
  L16 to L17 -> L19 [2] lasti
  L18 to L19 -> L19 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app\services\ingestion\email_dedupe.py", line 284>:
284           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('dedupe_key')

285           LOAD_CONST               2 ('str')

284           LOAD_CONST               3 ('now')

287           LOAD_CONST               4 ('Any')

284           LOAD_CONST               5 ('return')

288           LOAD_CONST               6 ('bool')

284           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object is_duplicate_email_lead at 0x0000018C179A7290, file "app\services\ingestion\email_dedupe.py", line 284>:
 284           RESUME                   0

 292           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (dedupe_key)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L1)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (dedupe_key)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

 293   L1:     LOAD_CONST               1 (False)
               RETURN_VALUE

 294   L2:     LOAD_GLOBAL              7 (_now_dt + NULL)
               LOAD_FAST_BORROW         1 (now)
               CALL                     1
               STORE_FAST               2 (now_dt)

 295           LOAD_GLOBAL              8 (_DEDUPE_LOCK)
               COPY                     1
               LOAD_SPECIAL             1 (__exit__)
               SWAP                     2
               SWAP                     3
               LOAD_SPECIAL             0 (__enter__)
               CALL                     0
       L3:     POP_TOP

 296           LOAD_GLOBAL             11 (_opportunistic_cleanup_locked + NULL)
               LOAD_FAST_BORROW         2 (now_dt)
               CALL                     1
               POP_TOP

 297           LOAD_GLOBAL             12 (_DEDUPE_REGISTRY)
               LOAD_ATTR               15 (get + NULL|self)
               LOAD_FAST_BORROW         0 (dedupe_key)
               CALL                     1
               STORE_FAST               3 (meta)

 298           LOAD_FAST_BORROW         3 (meta)
               LOAD_CONST               2 (None)
               IS_OP                    1 (is not)

 295   L4:     SWAP                     3
               SWAP                     2
               LOAD_CONST               2 (None)
               LOAD_CONST               2 (None)
               LOAD_CONST               2 (None)
               CALL                     3
               POP_TOP
               RETURN_VALUE
       L5:     PUSH_EXC_INFO
               WITH_EXCEPT_START
               TO_BOOL
               POP_JUMP_IF_TRUE         2 (to L6)
               NOT_TAKEN
               RERAISE                  2
       L6:     POP_TOP
       L7:     POP_EXCEPT
               POP_TOP
               POP_TOP
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L3 to L4 -> L5 [2] lasti
  L5 to L7 -> L8 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025630, file "app\services\ingestion\email_dedupe.py", line 301>:
301           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('dedupe_key')

302           LOAD_CONST               2 ('str')

301           LOAD_CONST               3 ('source')

304           LOAD_CONST               4 ('Optional[str]')

301           LOAD_CONST               5 ('now')

305           LOAD_CONST               6 ('Any')

301           LOAD_CONST               7 ('return')

306           LOAD_CONST               8 ('Dict[str, Any]')

301           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object register_email_lead_dedupe at 0x0000018C18190440, file "app\services\ingestion\email_dedupe.py", line 301>:
 301            RESUME                   0

 320            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (dedupe_key)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (dedupe_key)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         8 (to L2)
                NOT_TAKEN

 322    L1:     LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 323            LOAD_CONST               3 ('warnings')
                LOAD_CONST               4 ('missing_dedupe_key')
                BUILD_LIST               1

 321            BUILD_MAP                2
                RETURN_VALUE

 325    L2:     LOAD_FAST_BORROW         1 (source)
                POP_JUMP_IF_NONE        12 (to L3)
                NOT_TAKEN
                LOAD_GLOBAL              7 (_normalise_source + NULL)
                LOAD_FAST_BORROW         1 (source)
                CALL                     1
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               6 ('unknown')
        L4:     STORE_FAST               3 (src)

 326            LOAD_GLOBAL              9 (_now_dt + NULL)
                LOAD_FAST_BORROW         2 (now)
                CALL                     1
                STORE_FAST               4 (now_dt)

 327            LOAD_GLOBAL             11 (_iso + NULL)
                LOAD_FAST_BORROW         4 (now_dt)
                CALL                     1
                STORE_FAST               5 (iso)

 328            LOAD_GLOBAL             12 (_DEDUPE_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L5:     POP_TOP

 329            LOAD_GLOBAL             15 (_opportunistic_cleanup_locked + NULL)
                LOAD_FAST_BORROW         4 (now_dt)
                CALL                     1
                POP_TOP

 330            LOAD_GLOBAL             16 (_DEDUPE_REGISTRY)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_FAST_BORROW         0 (dedupe_key)
                CALL                     1
                STORE_FAST               6 (existing)

 331            LOAD_FAST_BORROW         6 (existing)
                POP_JUMP_IF_NONE        46 (to L10)
                NOT_TAKEN

 333            LOAD_CONST               1 ('status')
                LOAD_CONST               7 ('duplicate')

 334            LOAD_CONST               8 ('source')
                LOAD_FAST_BORROW         6 (existing)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               8 ('source')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                LOAD_FAST                3 (src)

 335    L8:     LOAD_CONST               3 ('warnings')

 336            LOAD_CONST               9 ('duplicate_email_lead')

 337            LOAD_CONST              10 ('email_dedupe_store_is_process_local')

 335            BUILD_LIST               2

 332            BUILD_MAP                3

 328    L9:     SWAP                     3
                SWAP                     2
                LOAD_CONST               5 (None)
                LOAD_CONST               5 (None)
                LOAD_CONST               5 (None)
                CALL                     3
                POP_TOP
                RETURN_VALUE

 341   L10:     LOAD_CONST              11 ('created_at')
                LOAD_FAST_BORROW         5 (iso)

 342            LOAD_CONST               8 ('source')
                LOAD_FAST_BORROW         3 (src)

 340            BUILD_MAP                2
                LOAD_GLOBAL             16 (_DEDUPE_REGISTRY)
                LOAD_FAST_BORROW         0 (dedupe_key)
                STORE_SUBSCR

 345            LOAD_CONST               1 ('status')
                LOAD_CONST              12 ('registered')

 346            LOAD_CONST               8 ('source')
                LOAD_FAST_BORROW         3 (src)

 347            LOAD_CONST               3 ('warnings')
                LOAD_CONST              10 ('email_dedupe_store_is_process_local')
                BUILD_LIST               1

 344            BUILD_MAP                3

 328   L11:     SWAP                     3
                SWAP                     2
                LOAD_CONST               5 (None)
                LOAD_CONST               5 (None)
                LOAD_CONST               5 (None)
                CALL                     3
                POP_TOP
                RETURN_VALUE
       L12:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L13)
                NOT_TAKEN
                RERAISE                  2
       L13:     POP_TOP
       L14:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                LOAD_CONST               5 (None)
                RETURN_VALUE

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L12 [2] lasti
  L7 to L9 -> L12 [2] lasti
  L10 to L11 -> L12 [2] lasti
  L12 to L14 -> L15 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app\services\ingestion\email_dedupe.py", line 351>:
351           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('now')

353           LOAD_CONST               2 ('Any')

351           LOAD_CONST               3 ('return')

354           LOAD_CONST               4 ('Dict[str, Any]')

351           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object cleanup_expired_dedupe_entries at 0x0000018C1800ABF0, file "app\services\ingestion\email_dedupe.py", line 351>:
 351           RESUME                   0

 357           LOAD_GLOBAL              1 (_now_dt + NULL)
               LOAD_FAST_BORROW         0 (now)
               CALL                     1
               STORE_FAST               1 (now_dt)

 358           LOAD_GLOBAL              2 (_DEDUPE_LOCK)
               COPY                     1
               LOAD_SPECIAL             1 (__exit__)
               SWAP                     2
               SWAP                     3
               LOAD_SPECIAL             0 (__enter__)
               CALL                     0
       L1:     POP_TOP

 359           LOAD_GLOBAL              5 (_opportunistic_cleanup_locked + NULL)
               LOAD_FAST_BORROW         1 (now_dt)
               CALL                     1
               STORE_FAST               2 (removed)

 361           LOAD_CONST               1 ('status')
               LOAD_CONST               2 ('ok')

 362           LOAD_CONST               3 ('removed')
               LOAD_FAST_BORROW         2 (removed)

 363           LOAD_CONST               4 ('remaining')
               LOAD_GLOBAL              7 (len + NULL)
               LOAD_GLOBAL              8 (_DEDUPE_REGISTRY)
               CALL                     1

 364           LOAD_CONST               5 ('ttl_seconds')
               LOAD_GLOBAL             10 (DEDUPE_TTL_SECONDS)

 360           BUILD_MAP                4

 358   L2:     SWAP                     3
               SWAP                     2
               LOAD_CONST               6 (None)
               LOAD_CONST               6 (None)
               LOAD_CONST               6 (None)
               CALL                     3
               POP_TOP
               RETURN_VALUE
       L3:     PUSH_EXC_INFO
               WITH_EXCEPT_START
               TO_BOOL
               POP_JUMP_IF_TRUE         2 (to L4)
               NOT_TAKEN
               RERAISE                  2
       L4:     POP_TOP
       L5:     POP_EXCEPT
               POP_TOP
               POP_TOP
               POP_TOP
               LOAD_CONST               6 (None)
               RETURN_VALUE

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [2] lasti
  L3 to L5 -> L6 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\ingestion\email_dedupe.py", line 368>:
368           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('None')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object reset_email_dedupe_registry_for_tests at 0x0000018C17972550, file "app\services\ingestion\email_dedupe.py", line 368>:
 368           RESUME                   0

 370           LOAD_GLOBAL              0 (_DEDUPE_LOCK)
               COPY                     1
               LOAD_SPECIAL             1 (__exit__)
               SWAP                     2
               SWAP                     3
               LOAD_SPECIAL             0 (__enter__)
               CALL                     0
       L1:     POP_TOP

 371           LOAD_GLOBAL              2 (_DEDUPE_REGISTRY)
               LOAD_ATTR                5 (clear + NULL|self)
               CALL                     0
               POP_TOP

 370   L2:     LOAD_CONST               1 (None)
               LOAD_CONST               1 (None)
               LOAD_CONST               1 (None)
               CALL                     3
               POP_TOP
               LOAD_CONST               1 (None)
               RETURN_VALUE
       L3:     PUSH_EXC_INFO
               WITH_EXCEPT_START
               TO_BOOL
               POP_JUMP_IF_TRUE         2 (to L4)
               NOT_TAKEN
               RERAISE                  2
       L4:     POP_TOP
       L5:     POP_EXCEPT
               POP_TOP
               POP_TOP
               POP_TOP
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [2] lasti
  L3 to L5 -> L6 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app\services\ingestion\email_dedupe.py", line 374>:
374           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Dict[str, Dict[str, Any]]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _peek_dedupe_registry_for_tests at 0x0000018C1804C9F0, file "app\services\ingestion\email_dedupe.py", line 374>:
 374            RESUME                   0

 376            LOAD_GLOBAL              0 (_DEDUPE_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L1:     POP_TOP

 377            LOAD_GLOBAL              2 (_DEDUPE_REGISTRY)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      0 (k)
                LOAD_FAST_AND_CLEAR      1 (v)
                SWAP                     3
        L2:     BUILD_MAP                0
                SWAP                     2
        L3:     FOR_ITER                17 (to L4)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST    1 (k, v)
                LOAD_FAST_BORROW         0 (k)
                LOAD_GLOBAL              7 (dict + NULL)
                LOAD_FAST_BORROW         1 (v)
                CALL                     1
                MAP_ADD                  2
                JUMP_BACKWARD           19 (to L3)
        L4:     END_FOR
                POP_ITER
        L5:     SWAP                     3
                STORE_FAST               1 (v)
                STORE_FAST               0 (k)

 376    L6:     SWAP                     3
                SWAP                     2
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     3
                POP_TOP
                RETURN_VALUE

  --    L7:     SWAP                     2
                POP_TOP

 377            SWAP                     3
                STORE_FAST               1 (v)
                STORE_FAST               0 (k)
                RERAISE                  0

 376    L8:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L9)
                NOT_TAKEN
                RERAISE                  2
        L9:     POP_TOP
       L10:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                LOAD_CONST               1 (None)
                RETURN_VALUE

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L8 [2] lasti
  L2 to L5 -> L7 [5]
  L5 to L6 -> L8 [2] lasti
  L7 to L8 -> L8 [2] lasti
  L8 to L10 -> L11 [4] lasti
```
