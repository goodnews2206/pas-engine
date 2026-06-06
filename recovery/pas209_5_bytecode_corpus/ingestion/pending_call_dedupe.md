# ingestion/pending_call_dedupe

- **pyc:** `app\services\ingestion\__pycache__\pending_call_dedupe.cpython-314.pyc`
- **expected source path (absent):** `app\services\ingestion/pending_call_dedupe.py`
- **co_filename (from bytecode):** `app/services/ingestion/pending_call_dedupe.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** ingestion

## Module docstring

```
PAS170 — Pending-call dedupe (process-local v1).

**PAS171 update:** when ``brokerage_id`` is supplied,
``register_pending_call_dedupe`` and
``is_duplicate_pending_call`` consult the durable Supabase
store first (see
:mod:`app.services.ingestion.pending_call_dedupe_store`).
The durable layer's ``status="ok"`` answer is authoritative;
``status="warning"`` (DB unavailable) falls back to the
process-local registry below, mirroring the PAS166 ↔ PAS165
fallback for email dedupe. The public surface is unchanged
— callers that omit ``brokerage_id`` still get process-local
v1 semantics exactly as before.

Closes the "same lead enqueued twice → two outbound dials"
gap identified in PAS-AUDIT-01 §C4. PAS166 added durable
dedupe for inbound *emails*; this module adds the symmetric
guard for *pending calls* themselves so that two webhook
submissions (or one email forwarder + one webhook) for the
same lead within the dedupe window do NOT result in two
Twilio dials.

Doctrine carried by every helper here:

* Per-brokerage scope. The dedupe key is keyed on
  ``(brokerage_id, source, normalized_phone)`` — never on a
  cross-tenant identifier. Two brokerages forwarding the same
  E.164 phone do NOT collide.
* Phone-only identity. If no phone is present (email-only
  contact) the dedupe is a structural skip — we never emit
  a duplicate, but we also never block the call_eligible=False
  capture path.
* No raw payload storage. The registry stores a sha256 of the
  ``(brokerage|source|phone)`` tuple plus a created-at
  timestamp. No phone digits, no name, no email, no notes.
* No dedupe key returned to the API caller. The route's
  response envelope NEVER carries the key. Operator-facing
  reports surface only structural counts.
* Process-local with explicit warning. Mirrors the PAS165
  process-local email-dedupe doctrine: ``pending_call_dedupe_
  store_is_process_local`` is added to every register so the
  operator dashboard can count "we are running on the
  fallback".
* Cross-restart safety is a follow-on phase. PAS170 ships
  the *interface* + the process-local fallback; a future
  durable replacement (PAS171+) will mirror PAS166 ↔ PAS165.
* RLock-protected. Opportunistic cleanup on every check /
  register call.
* Every public helper is non-raising; failures degrade to
  "not a duplicate" so the dedupe layer can never block
  legitimate dialing on its own bug.

Public surface:
  * ``build_pending_call_dedupe_key(brokerage_id, source, phone)``
  * ``is_duplicate_pending_call(key, *, now=None)``
  * ``register_pending_call_dedupe(key, *, source=None, now=None)``
  * ``cleanup_expired_pending_call_dedupe(*, now=None)``
  * ``reset_pending_call_dedupe_for_tests()``
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.services.ingestion.pending_call_dedupe_store`, `datetime`, `durable_pending_call_dedupe_enabled`, `hashlib`, `is_duplicate_durable_pending_call_dedupe`, `logging`, `register_durable_pending_call_dedupe`, `threading`, `timedelta`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_hash`, `_iso`, `_normalise_brokerage`, `_normalise_phone`, `_normalise_source`, `_now_dt`, `_opportunistic_cleanup_locked`, `_peek_pending_call_dedupe_for_tests`, `_safe_str`, `build_pending_call_dedupe_key`, `cleanup_expired_pending_call_dedupe`, `is_duplicate_pending_call`, `register_pending_call_dedupe`, `reset_pending_call_dedupe_for_tests`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS170 — Pending-call dedupe (process-local v1).\n\n**PAS171 update:** when ``brokerage_id`` is supplied,\n``register_pending_call_dedupe`` and\n``is_duplicate_pending_call`` consult the durable Supabase\nstore first (see\n:mod:`app.services.ingestion.pending_call_dedupe_store`).\nThe durable layer\'s ``status="ok"`` answer is authoritative;\n``status="warning"`` (DB unavailable) falls back to the\nprocess-local registry below, mirroring the PAS166 ↔ PAS165\nfallback for email dedupe. The public surface is unchanged\n— callers that omit ``brokerage_id`` still get process-local\nv1 semantics exactly as before.\n\nCloses the "same lead enqueued twice → two outbound dials"\ngap identified in PAS-AUDIT-01 §C4. PAS166 added durable\ndedupe for inbound *emails*; this module adds the symmetric\nguard for *pending calls* themselves so that two webhook\nsubmissions (or one email forwarder + one webhook) for the\nsame lead within the dedupe window do NOT result in two\nTwilio dials.\n\nDoctrine carried by every helper here:\n\n* Per-brokerage scope. The dedupe key is keyed on\n  ``(brokerage_id, source, normalized_phone)`` — never on a\n  cross-tenant identifier. Two brokerages forwarding the same\n  E.164 phone do NOT collide.\n* Phone-only identity. If no phone is present (email-only\n  contact) the dedupe is a structural skip — we never emit\n  a duplicate, but we also never block the call_eligible=False\n  capture path.\n* No raw payload storage. The registry stores a sha256 of the\n  ``(brokerage|source|phone)`` tuple plus a created-at\n  timestamp. No phone digits, no name, no email, no notes.\n* No dedupe key returned to the API caller. The route\'s\n  response envelope NEVER carries the key. Operator-facing\n  reports surface only structural counts.\n* Process-local with explicit warning. Mirrors the PAS165\n  process-local email-dedupe doctrine: ``pending_call_dedupe_\n  store_is_process_local`` is added to every register so the\n  operator dashboard can count "we are running on the\n  fallback".\n* Cross-restart safety is a follow-on phase. PAS170 ships\n  the *interface* + the process-local fallback; a future\n  durable replacement (PAS171+) will mirror PAS166 ↔ PAS165.\n* RLock-protected. Opportunistic cleanup on every check /\n  register call.\n* Every public helper is non-raising; failures degrade to\n  "not a duplicate" so the dedupe layer can never block\n  legitimate dialing on its own bug.\n\nPublic surface:\n  * ``build_pending_call_dedupe_key(brokerage_id, source, phone)``\n  * ``is_duplicate_pending_call(key, *, now=None)``\n  * ``register_pending_call_dedupe(key, *, source=None, now=None)``\n  * ``cleanup_expired_pending_call_dedupe(*, now=None)``\n  * ``reset_pending_call_dedupe_for_tests()``\n'
- 'pas.ingestion.pending_call_dedupe'
- 'Dict[str, Dict[str, Any]]'
- '_DEDUPE_REGISTRY'
- 'now'
- 'brokerage_id'
- 'source'
- 'Any'
- 'return'
- 'datetime'
- '+00:00'
- 'str'
- 'seconds'
- 'utf-8'
- 'replace'
- 'unknown'
- 'phone'
- "Reduce a phone to digits-only with a leading ``+`` when\none was present. Mirrors the PAS165 / PAS166 normalisation\nspirit. Returns empty string when no plausible phone was\nsupplied — caller treats empty as 'no dedupe possible'."
- 'text'
- '_hash unexpected error type='
- 'Optional[str]'
- 'Build a deterministic SHA-256 hex digest representing the\n"identity" of a pending-call enqueue.\n\nAlgorithm::\n\n    normalized_brokerage_id + "|"\n    + normalized_source       + "|"\n    + normalized_phone\n    → sha256(<that string>) → hex\n\nProperties:\n  * deterministic (no timestamps, no UUIDs);\n  * **brokerage-scoped**: two brokerages forwarding the\n    same phone do NOT collide;\n  * returns ``""`` when phone is missing (caller treats\n    empty as \'no dedupe possible\' — never duplicate);\n  * never raises.\n'
- 'now_dt'
- 'int'
- 'created_at'
- 'dedupe_key'
- 'bool'
- 'Return True when ``dedupe_key`` is already present and\nnot yet expired. Empty key → always False (no dedupe\npossible). NEVER raises. NEVER echoes the key.\n\nPAS171: when ``brokerage_id`` is supplied AND the durable\nstore is enabled, consult the durable store first. A\ndurable ``status="ok"`` answer is authoritative; a\ndurable ``status="warning"`` (DB unavailable) falls back\nto the process-local registry below.\n'
- 'status'
- 'duplicate'
- 'is_duplicate_pending_call durable lookup error type='
- 'Dict[str, Any]'
- 'Register a dedupe key. If the key is already present\nAND not yet expired, returns ``status="duplicate"``.\nOtherwise inserts the key and returns ``status="registered"``.\n\nReturns a closed-shape envelope::\n\n    {\n      "status":   "registered" | "duplicate" | "skipped" | "failed",\n      "source":   str,\n      "warnings": [<structural tokens>],\n    }\n\n``status="skipped"`` is returned for an empty / missing\nkey — that means the caller didn\'t have enough info\n(typically a missing phone) to dedupe at all. Skip is NOT\na duplicate; the caller proceeds.\n\nPAS171: when ``brokerage_id`` is supplied AND the durable\nstore is enabled, attempt the durable insert first. A\ndurable ``status="ok", duplicate=False`` returns\n``status="registered"`` and surfaces the\n``pending_call_dedupe_store_is_durable`` warning (so the\noperator dashboard can confirm we are NOT on the\nfallback). A durable ``status="ok", duplicate=True``\nreturns ``status="duplicate"``. A durable\n``status="warning"`` (DB unavailable) falls back to the\nprocess-local registry below.\n\nNEVER raises. NEVER echoes the key.\n'
- 'skipped'
- 'warnings'
- 'pending_call_dedupe_skipped_no_phone'
- 'duplicate_pending_call_suppressed'
- 'pending_call_dedupe_store_is_durable'
- 'registered'
- 'register_pending_call_dedupe durable insert error type='
- 'pending_call_dedupe_store_is_process_local'
- 'Operator-callable cleanup. Returns the count removed +\nremaining + TTL. NEVER raises.'
- 'removed'
- 'remaining'
- 'ttl_seconds'
- 'None'
- 'Test-only helper to flush the registry between tests.'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS170 — Pending-call dedupe (process-local v1).\n\n**PAS171 update:** when ``brokerage_id`` is supplied,\n``register_pending_call_dedupe`` and\n``is_duplicate_pending_call`` consult the durable Supabase\nstore first (see\n:mod:`app.services.ingestion.pending_call_dedupe_store`).\nThe durable layer\'s ``status="ok"`` answer is authoritative;\n``status="warning"`` (DB unavailable) falls back to the\nprocess-local registry below, mirroring the PAS166 ↔ PAS165\nfallback for email dedupe. The public surface is unchanged\n— callers that omit ``brokerage_id`` still get process-local\nv1 semantics exactly as before.\n\nCloses the "same lead enqueued twice → two outbound dials"\ngap identified in PAS-AUDIT-01 §C4. PAS166 added durable\ndedupe for inbound *emails*; this module adds the symmetric\nguard for *pending calls* themselves so that two webhook\nsubmissions (or one email forwarder + one webhook) for the\nsame lead within the dedupe window do NOT result in two\nTwilio dials.\n\nDoctrine carried by every helper here:\n\n* Per-brokerage scope. The dedupe key is keyed on\n  ``(brokerage_id, source, normalized_phone)`` — never on a\n  cross-tenant identifier. Two brokerages forwarding the same\n  E.164 phone do NOT collide.\n* Phone-only identity. If no phone is present (email-only\n  contact) the dedupe is a structural skip — we never emit\n  a duplicate, but we also never block the call_eligible=False\n  capture path.\n* No raw payload storage. The registry stores a sha256 of the\n  ``(brokerage|source|phone)`` tuple plus a created-at\n  timestamp. No phone digits, no name, no email, no notes.\n* No dedupe key returned to the API caller. The route\'s\n  response envelope NEVER carries the key. Operator-facing\n  reports surface only structural counts.\n* Process-local with explicit warning. Mirrors the PAS165\n  process-local email-dedupe doctrine: ``pending_call_dedupe_\n  store_is_process_local`` is added to every register so the\n  operator dashboard can count "we are running on the\n  fallback".\n* Cross-restart safety is a follow-on phase. PAS170 ships\n  the *interface* + the process-local fallback; a future\n  durable replacement (PAS171+) will mirror PAS166 ↔ PAS165.\n* RLock-protected. Opportunistic cleanup on every check /\n  register call.\n* Every public helper is non-raising; failures degrade to\n  "not a duplicate" so the dedupe layer can never block\n  legitimate dialing on its own bug.\n\nPublic surface:\n  * ``build_pending_call_dedupe_key(brokerage_id, source, phone)``\n  * ``is_duplicate_pending_call(key, *, now=None)``\n  * ``register_pending_call_dedupe(key, *, source=None, now=None)``\n  * ``cleanup_expired_pending_call_dedupe(*, now=None)``\n  * ``reset_pending_call_dedupe_for_tests()``\n')
               STORE_NAME               1 (__doc__)

  62           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  64           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (hashlib)
               STORE_NAME               4 (hashlib)

  65           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (logging)
               STORE_NAME               5 (logging)

  66           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (threading)
               STORE_NAME               6 (threading)

  67           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timedelta', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timedelta)
               STORE_NAME               8 (timedelta)
               IMPORT_FROM              9 (timezone)
               STORE_NAME               9 (timezone)
               POP_TOP

  68           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
               IMPORT_NAME             10 (typing)
               IMPORT_FROM             11 (Any)
               STORE_NAME              11 (Any)
               IMPORT_FROM             12 (Dict)
               STORE_NAME              12 (Dict)
               IMPORT_FROM             13 (List)
               STORE_NAME              13 (List)
               IMPORT_FROM             14 (Optional)
               STORE_NAME              14 (Optional)
               POP_TOP

  71           LOAD_NAME                5 (logging)
               LOAD_ATTR               30 (getLogger)
               PUSH_NULL
               LOAD_CONST               5 ('pas.ingestion.pending_call_dedupe')
               CALL                     1
               STORE_NAME              16 (logger)

  79           LOAD_CONST              39 (86400)
               STORE_NAME              17 (PENDING_CALL_DEDUPE_TTL_SECONDS)

  86           BUILD_MAP                0
               STORE_NAME              18 (_DEDUPE_REGISTRY)
               LOAD_CONST               6 ('Dict[str, Dict[str, Any]]')
               LOAD_NAME               19 (__annotations__)
               LOAD_CONST               7 ('_DEDUPE_REGISTRY')
               STORE_SUBSCR

  87           LOAD_NAME                6 (threading)
               LOAD_ATTR               40 (RLock)
               PUSH_NULL
               CALL                     0
               STORE_NAME              21 (_DEDUPE_LOCK)

  90           LOAD_CONST              40 ((None,))
               LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA35A0, file "app/services/ingestion/pending_call_dedupe.py", line 90>)
               MAKE_FUNCTION
               LOAD_CONST               9 (<code object _now_dt at 0x0000018C17F84190, file "app/services/ingestion/pending_call_dedupe.py", line 90>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              22 (_now_dt)

 106           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA34B0, file "app/services/ingestion/pending_call_dedupe.py", line 106>)
               MAKE_FUNCTION
               LOAD_CONST              11 (<code object _iso at 0x0000018C18025E30, file "app/services/ingestion/pending_call_dedupe.py", line 106>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              23 (_iso)

 114           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA3B40, file "app/services/ingestion/pending_call_dedupe.py", line 114>)
               MAKE_FUNCTION
               LOAD_CONST              13 (<code object _safe_str at 0x0000018C1794EBB0, file "app/services/ingestion/pending_call_dedupe.py", line 114>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              24 (_safe_str)

 130           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA3C30, file "app/services/ingestion/pending_call_dedupe.py", line 130>)
               MAKE_FUNCTION
               LOAD_CONST              15 (<code object _normalise_brokerage at 0x0000018C18090690, file "app/services/ingestion/pending_call_dedupe.py", line 130>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              25 (_normalise_brokerage)

 134           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA3780, file "app/services/ingestion/pending_call_dedupe.py", line 134>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _normalise_source at 0x0000018C18038B70, file "app/services/ingestion/pending_call_dedupe.py", line 134>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              26 (_normalise_source)

 139           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3870, file "app/services/ingestion/pending_call_dedupe.py", line 139>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _normalise_phone at 0x0000018C18060390, file "app/services/ingestion/pending_call_dedupe.py", line 139>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              27 (_normalise_phone)

 154           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA3960, file "app/services/ingestion/pending_call_dedupe.py", line 154>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _hash at 0x0000018C17EC4B00, file "app/services/ingestion/pending_call_dedupe.py", line 154>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (_hash)

 170           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18024930, file "app/services/ingestion/pending_call_dedupe.py", line 170>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object build_pending_call_dedupe_key at 0x0000018C17F95CF0, file "app/services/ingestion/pending_call_dedupe.py", line 170>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              29 (build_pending_call_dedupe_key)

 203           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3A50, file "app/services/ingestion/pending_call_dedupe.py", line 203>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object _opportunistic_cleanup_locked at 0x0000018C17EDA8B0, file "app/services/ingestion/pending_call_dedupe.py", line 203>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              30 (_opportunistic_cleanup_locked)

 234           LOAD_CONST              26 ('now')

 237           LOAD_CONST               2 (None)

 234           LOAD_CONST              27 ('brokerage_id')

 238           LOAD_CONST               2 (None)

 234           BUILD_MAP                2
               LOAD_CONST              28 (<code object __annotate__ at 0x0000018C18025730, file "app/services/ingestion/pending_call_dedupe.py", line 234>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object is_duplicate_pending_call at 0x0000018C17D78310, file "app/services/ingestion/pending_call_dedupe.py", line 234>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              31 (is_duplicate_pending_call)

 281           LOAD_CONST              30 ('source')

 284           LOAD_CONST               2 (None)

 281           LOAD_CONST              26 ('now')

 285           LOAD_CONST               2 (None)

 281           LOAD_CONST              27 ('brokerage_id')

 286           LOAD_CONST               2 (None)

 281           BUILD_MAP                3
               LOAD_CONST              31 (<code object __annotate__ at 0x0000018C18025330, file "app/services/ingestion/pending_call_dedupe.py", line 281>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object register_pending_call_dedupe at 0x0000018C17ED5A80, file "app/services/ingestion/pending_call_dedupe.py", line 281>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              32 (register_pending_call_dedupe)

 392           LOAD_CONST              26 ('now')

 394           LOAD_CONST               2 (None)

 392           BUILD_MAP                1
               LOAD_CONST              33 (<code object __annotate__ at 0x0000018C17FA2D30, file "app/services/ingestion/pending_call_dedupe.py", line 392>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object cleanup_expired_pending_call_dedupe at 0x0000018C17FA92F0, file "app/services/ingestion/pending_call_dedupe.py", line 392>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              33 (cleanup_expired_pending_call_dedupe)

 409           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C17FA2E20, file "app/services/ingestion/pending_call_dedupe.py", line 409>)
               MAKE_FUNCTION
               LOAD_CONST              36 (<code object reset_pending_call_dedupe_for_tests at 0x0000018C18010F50, file "app/services/ingestion/pending_call_dedupe.py", line 409>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (reset_pending_call_dedupe_for_tests)

 415           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C17FA2F10, file "app/services/ingestion/pending_call_dedupe.py", line 415>)
               MAKE_FUNCTION
               LOAD_CONST              38 (<code object _peek_pending_call_dedupe_for_tests at 0x0000018C1796DBD0, file "app/services/ingestion/pending_call_dedupe.py", line 415>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (_peek_pending_call_dedupe_for_tests)

 420           BUILD_LIST               0
               LOAD_CONST              41 (('PENDING_CALL_DEDUPE_TTL_SECONDS', 'build_pending_call_dedupe_key', 'is_duplicate_pending_call', 'register_pending_call_dedupe', 'cleanup_expired_pending_call_dedupe', 'reset_pending_call_dedupe_for_tests'))
               LIST_EXTEND              1
               STORE_NAME              36 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app/services/ingestion/pending_call_dedupe.py", line 90>:
 90           RESUME                   0
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

Disassembly of <code object _now_dt at 0x0000018C17F84190, file "app/services/ingestion/pending_call_dedupe.py", line 90>:
  90            RESUME                   0

  91            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (now)
                LOAD_GLOBAL              2 (datetime)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       78 (to L2)
                NOT_TAKEN

  92            LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L1)
                NOT_TAKEN

  93            LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                RETURN_VALUE

  94    L1:     LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

  95    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (now)
                LOAD_GLOBAL             14 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      117 (to L6)
                NOT_TAKEN

  96            NOP

  97    L3:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               16 (fromisoformat)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_CONST               2 ('Z')
                LOAD_CONST               3 ('+00:00')
                CALL                     2
                CALL                     1
                STORE_FAST               1 (dt)

  98            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L4)
                NOT_TAKEN

  99            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST               1 (dt)

 100    L4:     LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
        L5:     RETURN_VALUE

 103    L6:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               20 (now)
                PUSH_NULL
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 101            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        4 (to L9)
                NOT_TAKEN
                POP_TOP

 102    L8:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 49 (to L6)

 101    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app/services/ingestion/pending_call_dedupe.py", line 106>:
106           RESUME                   0
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

Disassembly of <code object _iso at 0x0000018C18025E30, file "app/services/ingestion/pending_call_dedupe.py", line 106>:
106           RESUME                   0

107           LOAD_FAST_BORROW         0 (dt)
              LOAD_ATTR                1 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app/services/ingestion/pending_call_dedupe.py", line 114>:
114           RESUME                   0
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
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_str at 0x0000018C1794EBB0, file "app/services/ingestion/pending_call_dedupe.py", line 114>:
 114            RESUME                   0

 115            LOAD_FAST_BORROW         0 (v)
                POP_JUMP_IF_NOT_NONE     3 (to L1)
                NOT_TAKEN

 116            LOAD_CONST               1 ('')
                RETURN_VALUE

 117    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (v)
                LOAD_GLOBAL              2 (bytes)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       21 (to L4)
                NOT_TAKEN

 118            NOP

 119    L2:     LOAD_FAST_BORROW         0 (v)
                LOAD_ATTR                5 (decode + NULL|self)
                LOAD_CONST               2 ('utf-8')
                LOAD_CONST               3 ('replace')
                LOAD_CONST               4 (('errors',))
                CALL_KW                  2
        L3:     RETURN_VALUE

 122    L4:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (v)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        13 (to L7)
                NOT_TAKEN

 123            NOP

 124    L5:     LOAD_GLOBAL              9 (str + NULL)
                LOAD_FAST_BORROW         0 (v)
                CALL                     1
        L6:     RETURN_VALUE

 127    L7:     LOAD_FAST_BORROW         0 (v)
                RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

 120            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L10)
                NOT_TAKEN
                POP_TOP

 121    L9:     POP_EXCEPT
                LOAD_CONST               1 ('')
                RETURN_VALUE

 120   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L12:     PUSH_EXC_INFO

 125            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L14)
                NOT_TAKEN
                POP_TOP

 126   L13:     POP_EXCEPT
                LOAD_CONST               1 ('')
                RETURN_VALUE

 125   L14:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app/services/ingestion/pending_call_dedupe.py", line 130>:
130           RESUME                   0
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
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _normalise_brokerage at 0x0000018C18090690, file "app/services/ingestion/pending_call_dedupe.py", line 130>:
130           RESUME                   0

131           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (brokerage_id)
              CALL                     1
              LOAD_ATTR                3 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app/services/ingestion/pending_call_dedupe.py", line 134>:
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

Disassembly of <code object _normalise_source at 0x0000018C18038B70, file "app/services/ingestion/pending_call_dedupe.py", line 134>:
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app/services/ingestion/pending_call_dedupe.py", line 139>:
139           RESUME                   0
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

Disassembly of <code object _normalise_phone at 0x0000018C18060390, file "app/services/ingestion/pending_call_dedupe.py", line 139>:
139           RESUME                   0

144           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (phone)
              CALL                     1
              LOAD_ATTR                3 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

145           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

146           LOAD_CONST               1 ('')
              RETURN_VALUE

147   L1:     LOAD_FAST_BORROW         1 (s)
              LOAD_ATTR                5 (startswith + NULL|self)
              LOAD_CONST               2 ('+')
              CALL                     1
              STORE_FAST               2 (plus_seen)

148           LOAD_CONST               1 ('')
              LOAD_ATTR                7 (join + NULL|self)
              LOAD_CONST               3 (<code object <genexpr> at 0x0000018C17C49B80, file "app/services/ingestion/pending_call_dedupe.py", line 148>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (s)
              GET_ITER
              CALL                     0
              CALL                     1
              STORE_FAST               3 (digits)

149           LOAD_FAST_BORROW         3 (digits)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

150           LOAD_CONST               1 ('')
              RETURN_VALUE

151   L2:     LOAD_FAST_BORROW         2 (plus_seen)
              TO_BOOL
              POP_JUMP_IF_FALSE       10 (to L3)
              NOT_TAKEN
              LOAD_CONST               2 ('+')
              LOAD_FAST_BORROW         3 (digits)
              BINARY_OP                0 (+)
              RETURN_VALUE
      L3:     LOAD_FAST                3 (digits)
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C17C49B80, file "app/services/ingestion/pending_call_dedupe.py", line 148>:
 148           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                30 (to L5)
               STORE_FAST_LOAD_FAST    17 (c, c)
               LOAD_ATTR                1 (isdigit + NULL|self)
               CALL                     0
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           26 (to L2)
       L4:     LOAD_FAST_BORROW         1 (c)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           32 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app/services/ingestion/pending_call_dedupe.py", line 154>:
154           RESUME                   0
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

Disassembly of <code object _hash at 0x0000018C17EC4B00, file "app/services/ingestion/pending_call_dedupe.py", line 154>:
 154           RESUME                   0

 155           NOP

 156   L1:     LOAD_GLOBAL              0 (hashlib)
               LOAD_ATTR                2 (sha256)
               PUSH_NULL

 157           LOAD_FAST_BORROW         0 (text)
               LOAD_ATTR                5 (encode + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('errors',))
               CALL_KW                  2

 156           CALL                     1

 158           LOAD_ATTR                7 (hexdigest + NULL|self)
               CALL                     0

 156   L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 159           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       90 (to L8)
               NOT_TAKEN
               STORE_FAST               1 (e)

 160   L4:     LOAD_GLOBAL             10 (logger)
               LOAD_ATTR               13 (warning + NULL|self)

 161           LOAD_CONST               3 ('_hash unexpected error type=')
               LOAD_GLOBAL             15 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               16 (__name__)
               FORMAT_SIMPLE
               BUILD_STRING             2

 160           CALL                     1
               POP_TOP

 163           LOAD_GLOBAL              0 (hashlib)
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

 159   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L9 [1] lasti
  L4 to L5 -> L7 [1] lasti
  L5 to L6 -> L9 [1] lasti
  L7 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app/services/ingestion/pending_call_dedupe.py", line 170>:
170           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

172           LOAD_CONST               2 ('Optional[str]')

170           LOAD_CONST               3 ('source')

173           LOAD_CONST               2 ('Optional[str]')

170           LOAD_CONST               4 ('phone')

174           LOAD_CONST               2 ('Optional[str]')

170           LOAD_CONST               5 ('return')

175           LOAD_CONST               6 ('str')

170           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object build_pending_call_dedupe_key at 0x0000018C17F95CF0, file "app/services/ingestion/pending_call_dedupe.py", line 170>:
170           RESUME                   0

194           LOAD_GLOBAL              1 (_normalise_brokerage + NULL)
              LOAD_FAST_BORROW         0 (brokerage_id)
              CALL                     1
              STORE_FAST               3 (bid)

195           LOAD_GLOBAL              3 (_normalise_source + NULL)
              LOAD_FAST_BORROW         1 (source)
              CALL                     1
              STORE_FAST               4 (src)

196           LOAD_GLOBAL              5 (_normalise_phone + NULL)
              LOAD_FAST_BORROW         2 (phone)
              CALL                     1
              STORE_FAST               5 (ph)

197           LOAD_FAST_BORROW         3 (bid)
              TO_BOOL
              POP_JUMP_IF_FALSE        9 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         5 (ph)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

198   L1:     LOAD_CONST               1 ('')
              RETURN_VALUE

199   L2:     LOAD_FAST_BORROW         3 (bid)
              FORMAT_SIMPLE
              LOAD_CONST               2 ('|')
              LOAD_FAST_BORROW         4 (src)
              FORMAT_SIMPLE
              LOAD_CONST               2 ('|')
              LOAD_FAST_BORROW         5 (ph)
              FORMAT_SIMPLE
              BUILD_STRING             5
              STORE_FAST               6 (canonical)

200           LOAD_GLOBAL              7 (_hash + NULL)
              LOAD_FAST_BORROW         6 (canonical)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app/services/ingestion/pending_call_dedupe.py", line 203>:
203           RESUME                   0
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

Disassembly of <code object _opportunistic_cleanup_locked at 0x0000018C17EDA8B0, file "app/services/ingestion/pending_call_dedupe.py", line 203>:
 203            RESUME                   0

 204            LOAD_GLOBAL              0 (_DEDUPE_REGISTRY)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 205            LOAD_SMALL_INT           0
                RETURN_VALUE

 206    L1:     LOAD_FAST_BORROW         0 (now_dt)
                LOAD_GLOBAL              3 (timedelta + NULL)
                LOAD_GLOBAL              4 (PENDING_CALL_DEDUPE_TTL_SECONDS)
                LOAD_CONST               1 (('seconds',))
                CALL_KW                  1
                BINARY_OP               10 (-)
                STORE_FAST               1 (cutoff)

 207            BUILD_LIST               0
                STORE_FAST               2 (expired_keys)

 208            LOAD_GLOBAL              0 (_DEDUPE_REGISTRY)
                LOAD_ATTR                7 (items + NULL|self)
                CALL                     0
                GET_ITER
        L2:     FOR_ITER               173 (to L7)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   52 (key, meta)

 209            LOAD_FAST_BORROW         4 (meta)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               2 ('created_at')
                CALL                     1
                STORE_FAST               5 (created)

 210            LOAD_GLOBAL             11 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (created)
                LOAD_GLOBAL             12 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        20 (to L3)
                NOT_TAKEN

 211            LOAD_FAST_BORROW         2 (expired_keys)
                LOAD_ATTR               15 (append + NULL|self)
                LOAD_FAST_BORROW         3 (key)
                CALL                     1
                POP_TOP

 212            JUMP_BACKWARD           63 (to L2)

 213    L3:     NOP

 214    L4:     LOAD_GLOBAL             16 (datetime)
                LOAD_ATTR               18 (fromisoformat)
                PUSH_NULL

 215            LOAD_FAST_BORROW         5 (created)
                LOAD_ATTR               21 (replace + NULL|self)
                LOAD_CONST               3 ('Z')
                LOAD_CONST               4 ('+00:00')
                CALL                     2

 214            CALL                     1
                STORE_FAST               6 (created_dt)

 217            LOAD_FAST_BORROW         6 (created_dt)
                LOAD_ATTR               22 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L5)
                NOT_TAKEN

 218            LOAD_FAST_BORROW         6 (created_dt)
                LOAD_ATTR               21 (replace + NULL|self)
                LOAD_GLOBAL             24 (timezone)
                LOAD_ATTR               26 (utc)
                LOAD_CONST               5 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST               6 (created_dt)

 222    L5:     LOAD_FAST_LOAD_FAST     97 (created_dt, cutoff)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD          156 (to L2)

 223    L6:     LOAD_FAST                2 (expired_keys)
                LOAD_ATTR               15 (append + NULL|self)
                LOAD_FAST                3 (key)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          175 (to L2)

 208    L7:     END_FOR
                POP_ITER

 224            LOAD_SMALL_INT           0
                STORE_FAST               7 (removed)

 225            LOAD_FAST_BORROW         2 (expired_keys)
                GET_ITER
        L8:     FOR_ITER                20 (to L11)
                STORE_FAST               8 (k)

 226            NOP

 227    L9:     LOAD_GLOBAL              0 (_DEDUPE_REGISTRY)
                LOAD_FAST_BORROW         8 (k)
                DELETE_SUBSCR

 228            LOAD_FAST_BORROW         7 (removed)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               7 (removed)
       L10:     JUMP_BACKWARD           22 (to L8)

 225   L11:     END_FOR
                POP_ITER

 231            LOAD_FAST_BORROW         7 (removed)
                RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 219            LOAD_GLOBAL             28 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       22 (to L14)
                NOT_TAKEN
                POP_TOP

 220            LOAD_FAST                2 (expired_keys)
                LOAD_ATTR               15 (append + NULL|self)
                LOAD_FAST                3 (key)
                CALL                     1
                POP_TOP

 221   L13:     POP_EXCEPT
                JUMP_BACKWARD          238 (to L2)

 219   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L16:     PUSH_EXC_INFO

 229            LOAD_GLOBAL             30 (KeyError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L18)
                NOT_TAKEN
                POP_TOP

 230   L17:     POP_EXCEPT
                JUMP_BACKWARD           75 (to L8)

 229   L18:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app/services/ingestion/pending_call_dedupe.py", line 234>:
234           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('dedupe_key')

235           LOAD_CONST               2 ('str')

234           LOAD_CONST               3 ('now')

237           LOAD_CONST               4 ('Any')

234           LOAD_CONST               5 ('brokerage_id')

238           LOAD_CONST               6 ('Optional[str]')

234           LOAD_CONST               7 ('return')

239           LOAD_CONST               8 ('bool')

234           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object is_duplicate_pending_call at 0x0000018C17D78310, file "app/services/ingestion/pending_call_dedupe.py", line 234>:
 234            RESUME                   0

 250            LOAD_GLOBAL              1 (isinstance + NULL)
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

 251    L1:     LOAD_CONST               1 (False)
                RETURN_VALUE

 254    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (brokerage_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      104 (to L7)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       82 (to L7)
                NOT_TAKEN

 255            NOP

 256    L3:     LOAD_SMALL_INT           0
                LOAD_CONST               2 (('durable_pending_call_dedupe_enabled', 'is_duplicate_durable_pending_call_dedupe'))
                IMPORT_NAME              3 (app.services.ingestion.pending_call_dedupe_store)
                IMPORT_FROM              4 (durable_pending_call_dedupe_enabled)
                STORE_FAST               3 (durable_pending_call_dedupe_enabled)
                IMPORT_FROM              5 (is_duplicate_durable_pending_call_dedupe)
                STORE_FAST               4 (is_duplicate_durable_pending_call_dedupe)
                POP_TOP

 260            LOAD_FAST_BORROW         3 (durable_pending_call_dedupe_enabled)
                PUSH_NULL
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       60 (to L7)
        L4:     NOT_TAKEN

 261    L5:     LOAD_FAST_BORROW         4 (is_duplicate_durable_pending_call_dedupe)
                PUSH_NULL

 262            LOAD_FAST_BORROW         2 (brokerage_id)

 263            LOAD_FAST_BORROW         0 (dedupe_key)

 264            LOAD_FAST_BORROW         1 (now)

 261            LOAD_CONST               3 (('brokerage_id', 'dedupe_key', 'now'))
                CALL_KW                  3
                STORE_FAST               5 (env)

 266            LOAD_FAST_BORROW         5 (env)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               4 ('status')
                CALL                     1
                LOAD_CONST               5 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       27 (to L7)
                NOT_TAKEN

 267            LOAD_GLOBAL             15 (bool + NULL)
                LOAD_FAST_BORROW         5 (env)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               6 ('duplicate')
                CALL                     1
                CALL                     1
        L6:     RETURN_VALUE

 275    L7:     LOAD_GLOBAL             27 (_now_dt + NULL)
                LOAD_FAST_BORROW         1 (now)
                CALL                     1
                STORE_FAST               7 (now_dt)

 276            LOAD_GLOBAL             28 (_DEDUPE_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L8:     POP_TOP

 277            LOAD_GLOBAL             31 (_opportunistic_cleanup_locked + NULL)
                LOAD_FAST_BORROW         7 (now_dt)
                CALL                     1
                POP_TOP

 278            LOAD_GLOBAL             32 (_DEDUPE_REGISTRY)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_FAST_BORROW         0 (dedupe_key)
                CALL                     1
                LOAD_CONST               8 (None)
                IS_OP                    1 (is not)

 276    L9:     SWAP                     3
                SWAP                     2
                LOAD_CONST               8 (None)
                LOAD_CONST               8 (None)
                LOAD_CONST               8 (None)
                CALL                     3
                POP_TOP
                RETURN_VALUE

  --   L10:     PUSH_EXC_INFO

 269            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       54 (to L14)
                NOT_TAKEN
                STORE_FAST               6 (e)

 270   L11:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 271            LOAD_CONST               7 ('is_duplicate_pending_call durable lookup error type=')

 272            LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE

 271            BUILD_STRING             2

 270            CALL                     1
                POP_TOP
       L12:     POP_EXCEPT
                LOAD_CONST               8 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                JUMP_BACKWARD_NO_INTERRUPT 129 (to L7)

  --   L13:     LOAD_CONST               8 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 269   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 276   L16:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L17)
                NOT_TAKEN
                RERAISE                  2
       L17:     POP_TOP
       L18:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                LOAD_CONST               8 (None)
                RETURN_VALUE

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L10 [0]
  L5 to L6 -> L10 [0]
  L8 to L9 -> L16 [2] lasti
  L10 to L11 -> L15 [1] lasti
  L11 to L12 -> L13 [1] lasti
  L13 to L15 -> L15 [1] lasti
  L16 to L18 -> L19 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025330, file "app/services/ingestion/pending_call_dedupe.py", line 281>:
281           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('dedupe_key')

282           LOAD_CONST               2 ('str')

281           LOAD_CONST               3 ('source')

284           LOAD_CONST               4 ('Optional[str]')

281           LOAD_CONST               5 ('now')

285           LOAD_CONST               6 ('Any')

281           LOAD_CONST               7 ('brokerage_id')

286           LOAD_CONST               4 ('Optional[str]')

281           LOAD_CONST               8 ('return')

287           LOAD_CONST               9 ('Dict[str, Any]')

281           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object register_pending_call_dedupe at 0x0000018C17ED5A80, file "app/services/ingestion/pending_call_dedupe.py", line 281>:
 281            RESUME                   0

 318            LOAD_GLOBAL              1 (isinstance + NULL)
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
                POP_JUMP_IF_TRUE        19 (to L2)
                NOT_TAKEN

 320    L1:     LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('skipped')

 321            LOAD_CONST               3 ('source')
                LOAD_GLOBAL              7 (_normalise_source + NULL)
                LOAD_FAST_BORROW         1 (source)
                CALL                     1

 322            LOAD_CONST               4 ('warnings')
                LOAD_CONST               5 ('pending_call_dedupe_skipped_no_phone')
                BUILD_LIST               1

 319            BUILD_MAP                3
                RETURN_VALUE

 324    L2:     LOAD_FAST_BORROW         1 (source)
                POP_JUMP_IF_NONE        12 (to L3)
                NOT_TAKEN
                LOAD_GLOBAL              7 (_normalise_source + NULL)
                LOAD_FAST_BORROW         1 (source)
                CALL                     1
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               7 ('unknown')
        L4:     STORE_FAST               4 (src)

 327            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (brokerage_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      121 (to L13)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       99 (to L13)
                NOT_TAKEN

 328            NOP

 329    L5:     LOAD_SMALL_INT           0
                LOAD_CONST               8 (('durable_pending_call_dedupe_enabled', 'register_durable_pending_call_dedupe'))
                IMPORT_NAME              4 (app.services.ingestion.pending_call_dedupe_store)
                IMPORT_FROM              5 (durable_pending_call_dedupe_enabled)
                STORE_FAST               5 (durable_pending_call_dedupe_enabled)
                IMPORT_FROM              6 (register_durable_pending_call_dedupe)
                STORE_FAST               6 (register_durable_pending_call_dedupe)
                POP_TOP

 333            LOAD_FAST_BORROW         5 (durable_pending_call_dedupe_enabled)
                PUSH_NULL
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       77 (to L13)
        L6:     NOT_TAKEN

 334    L7:     LOAD_FAST_BORROW         6 (register_durable_pending_call_dedupe)
                PUSH_NULL

 335            LOAD_FAST_BORROW         3 (brokerage_id)

 336            LOAD_FAST_BORROW         0 (dedupe_key)

 337            LOAD_FAST_BORROW         4 (src)

 338            LOAD_FAST_BORROW         2 (now)

 334            LOAD_CONST               9 (('brokerage_id', 'dedupe_key', 'source', 'now'))
                CALL_KW                  4
                STORE_FAST               7 (env)

 340            LOAD_FAST_BORROW         7 (env)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               1 ('status')
                CALL                     1
                LOAD_CONST              10 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       43 (to L13)
                NOT_TAKEN

 341            LOAD_FAST_BORROW         7 (env)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              11 ('duplicate')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       11 (to L11)
        L8:     NOT_TAKEN

 343    L9:     LOAD_CONST               1 ('status')
                LOAD_CONST              11 ('duplicate')

 344            LOAD_CONST               3 ('source')
                LOAD_FAST_BORROW         4 (src)

 345            LOAD_CONST               4 ('warnings')

 346            LOAD_CONST              12 ('duplicate_pending_call_suppressed')

 347            LOAD_CONST              13 ('pending_call_dedupe_store_is_durable')

 345            BUILD_LIST               2

 342            BUILD_MAP                3
       L10:     RETURN_VALUE

 351   L11:     LOAD_CONST               1 ('status')
                LOAD_CONST              14 ('registered')

 352            LOAD_CONST               3 ('source')
                LOAD_FAST_BORROW         4 (src)

 353            LOAD_CONST               4 ('warnings')

 354            LOAD_CONST              13 ('pending_call_dedupe_store_is_durable')

 353            BUILD_LIST               1

 350            BUILD_MAP                3
       L12:     RETURN_VALUE

 367   L13:     LOAD_GLOBAL             27 (_now_dt + NULL)
                LOAD_FAST_BORROW         2 (now)
                CALL                     1
                STORE_FAST               9 (now_dt)

 368            LOAD_GLOBAL             29 (_iso + NULL)
                LOAD_FAST_BORROW         9 (now_dt)
                CALL                     1
                STORE_FAST              10 (iso)

 369            LOAD_GLOBAL             30 (_DEDUPE_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
       L14:     POP_TOP

 370            LOAD_GLOBAL             33 (_opportunistic_cleanup_locked + NULL)
                LOAD_FAST_BORROW         9 (now_dt)
                CALL                     1
                POP_TOP

 371            LOAD_GLOBAL             34 (_DEDUPE_REGISTRY)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_FAST_BORROW         0 (dedupe_key)
                CALL                     1
                STORE_FAST              11 (existing)

 372            LOAD_FAST_BORROW        11 (existing)
                POP_JUMP_IF_NONE        46 (to L19)
                NOT_TAKEN

 374            LOAD_CONST               1 ('status')
                LOAD_CONST              11 ('duplicate')

 375            LOAD_CONST               3 ('source')
                LOAD_FAST_BORROW        11 (existing)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               3 ('source')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L17)
       L15:     NOT_TAKEN
       L16:     POP_TOP
                LOAD_FAST                4 (src)

 376   L17:     LOAD_CONST               4 ('warnings')

 377            LOAD_CONST              12 ('duplicate_pending_call_suppressed')

 378            LOAD_CONST              16 ('pending_call_dedupe_store_is_process_local')

 376            BUILD_LIST               2

 373            BUILD_MAP                3

 369   L18:     SWAP                     3
                SWAP                     2
                LOAD_CONST               6 (None)
                LOAD_CONST               6 (None)
                LOAD_CONST               6 (None)
                CALL                     3
                POP_TOP
                RETURN_VALUE

 382   L19:     LOAD_CONST              17 ('created_at')
                LOAD_FAST_BORROW        10 (iso)

 383            LOAD_CONST               3 ('source')
                LOAD_FAST_BORROW         4 (src)

 381            BUILD_MAP                2
                LOAD_GLOBAL             34 (_DEDUPE_REGISTRY)
                LOAD_FAST_BORROW         0 (dedupe_key)
                STORE_SUBSCR

 386            LOAD_CONST               1 ('status')
                LOAD_CONST              14 ('registered')

 387            LOAD_CONST               3 ('source')
                LOAD_FAST_BORROW         4 (src)

 388            LOAD_CONST               4 ('warnings')
                LOAD_CONST              16 ('pending_call_dedupe_store_is_process_local')
                BUILD_LIST               1

 385            BUILD_MAP                3

 369   L20:     SWAP                     3
                SWAP                     2
                LOAD_CONST               6 (None)
                LOAD_CONST               6 (None)
                LOAD_CONST               6 (None)
                CALL                     3
                POP_TOP
                RETURN_VALUE

  --   L21:     PUSH_EXC_INFO

 361            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       54 (to L25)
                NOT_TAKEN
                STORE_FAST               8 (e)

 362   L22:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 363            LOAD_CONST              15 ('register_pending_call_dedupe durable insert error type=')

 364            LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE

 363            BUILD_STRING             2

 362            CALL                     1
                POP_TOP
       L23:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                JUMP_BACKWARD_NO_INTERRUPT 209 (to L13)

  --   L24:     LOAD_CONST               6 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 361   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 369   L27:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L28)
                NOT_TAKEN
                RERAISE                  2
       L28:     POP_TOP
       L29:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                LOAD_CONST               6 (None)
                RETURN_VALUE

  --   L30:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L21 [0]
  L7 to L8 -> L21 [0]
  L9 to L10 -> L21 [0]
  L11 to L12 -> L21 [0]
  L14 to L15 -> L27 [2] lasti
  L16 to L18 -> L27 [2] lasti
  L19 to L20 -> L27 [2] lasti
  L21 to L22 -> L26 [1] lasti
  L22 to L23 -> L24 [1] lasti
  L24 to L26 -> L26 [1] lasti
  L27 to L29 -> L30 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app/services/ingestion/pending_call_dedupe.py", line 392>:
392           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('now')

394           LOAD_CONST               2 ('Any')

392           LOAD_CONST               3 ('return')

395           LOAD_CONST               4 ('Dict[str, Any]')

392           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object cleanup_expired_pending_call_dedupe at 0x0000018C17FA92F0, file "app/services/ingestion/pending_call_dedupe.py", line 392>:
 392           RESUME                   0

 398           LOAD_GLOBAL              1 (_now_dt + NULL)
               LOAD_FAST_BORROW         0 (now)
               CALL                     1
               STORE_FAST               1 (now_dt)

 399           LOAD_GLOBAL              2 (_DEDUPE_LOCK)
               COPY                     1
               LOAD_SPECIAL             1 (__exit__)
               SWAP                     2
               SWAP                     3
               LOAD_SPECIAL             0 (__enter__)
               CALL                     0
       L1:     POP_TOP

 400           LOAD_GLOBAL              5 (_opportunistic_cleanup_locked + NULL)
               LOAD_FAST_BORROW         1 (now_dt)
               CALL                     1
               STORE_FAST               2 (removed)

 402           LOAD_CONST               1 ('status')
               LOAD_CONST               2 ('ok')

 403           LOAD_CONST               3 ('removed')
               LOAD_FAST_BORROW         2 (removed)

 404           LOAD_CONST               4 ('remaining')
               LOAD_GLOBAL              7 (len + NULL)
               LOAD_GLOBAL              8 (_DEDUPE_REGISTRY)
               CALL                     1

 405           LOAD_CONST               5 ('ttl_seconds')
               LOAD_GLOBAL             10 (PENDING_CALL_DEDUPE_TTL_SECONDS)

 401           BUILD_MAP                4

 399   L2:     SWAP                     3
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app/services/ingestion/pending_call_dedupe.py", line 409>:
409           RESUME                   0
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

Disassembly of <code object reset_pending_call_dedupe_for_tests at 0x0000018C18010F50, file "app/services/ingestion/pending_call_dedupe.py", line 409>:
 409           RESUME                   0

 411           LOAD_GLOBAL              0 (_DEDUPE_LOCK)
               COPY                     1
               LOAD_SPECIAL             1 (__exit__)
               SWAP                     2
               SWAP                     3
               LOAD_SPECIAL             0 (__enter__)
               CALL                     0
       L1:     POP_TOP

 412           LOAD_GLOBAL              2 (_DEDUPE_REGISTRY)
               LOAD_ATTR                5 (clear + NULL|self)
               CALL                     0
               POP_TOP

 411   L2:     LOAD_CONST               1 (None)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "app/services/ingestion/pending_call_dedupe.py", line 415>:
415           RESUME                   0
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

Disassembly of <code object _peek_pending_call_dedupe_for_tests at 0x0000018C1796DBD0, file "app/services/ingestion/pending_call_dedupe.py", line 415>:
 415            RESUME                   0

 416            LOAD_GLOBAL              0 (_DEDUPE_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L1:     POP_TOP

 417            LOAD_GLOBAL              2 (_DEDUPE_REGISTRY)
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

 416    L6:     SWAP                     3
                SWAP                     2
                LOAD_CONST               0 (None)
                LOAD_CONST               0 (None)
                LOAD_CONST               0 (None)
                CALL                     3
                POP_TOP
                RETURN_VALUE

  --    L7:     SWAP                     2
                POP_TOP

 417            SWAP                     3
                STORE_FAST               1 (v)
                STORE_FAST               0 (k)
                RERAISE                  0

 416    L8:     PUSH_EXC_INFO
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
                LOAD_CONST               0 (None)
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
