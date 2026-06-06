# security/api_key_reveal

- **pyc:** `app\services\security\__pycache__\api_key_reveal.cpython-314.pyc`
- **expected source path (absent):** `app\services\security/api_key_reveal.py`
- **co_filename (from bytecode):** `app/services/security/api_key_reveal.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** security

## Module docstring

```
PAS-SECURITY-04 — One-time API-key reveal service.

Implements the token-issue / verify / attempt-tracking
surface for a one-time raw-key reveal on a rotated tenant
API key. The token machinery is fully functional; the actual
raw-key payload is **deferred** because PAS does not yet have
a vetted key-generation pipeline that holds the raw key
briefly during the reveal window.

Doctrine carried from
[docs/pas_api_key_delivery_doctrine.md](../../../docs/pas_api_key_delivery_doctrine.md):

* **One-time only.** Once `revealed_at` is set, every
  subsequent reveal attempt returns
  ``error_code="reveal_already_consumed"``.
* **Short-lived.** Reveal tokens expire (default 5 minutes
  after `effective_at`). Service refuses to reveal after
  expiry.
* **Hashed tokens only.** v34 schema stores the sha256 hex of
  the token, not the raw token. The raw token is returned
  to the operator exactly once at issuance.
* **Raw key NEVER stored.** PAS does not persist the raw key
  in any column. The deferred-raw-key behaviour returns
  ``status="deferred"`` + ``error_code="raw_key_reveal_unsupported"``
  until PAS-SECURITY-05+ wires a vetted ephemeral storage
  channel.
* **Audit-logged.** Every reveal attempt — success, expired,
  already-consumed, deferred — writes a PAS174 audit row via
  ``log_operator_action``.
* **Rate-limited at the route layer** (PAS-SECURITY-02
  ``api_key_rotation`` surface — 3/hour/brokerage).
* **NEVER raises.**

Public surface:

  * ``REVEAL_TOKEN_TTL_SECONDS``                   — closed constant.
  * ``ALLOWED_REVEAL_STATUSES``                    — closed enum.
  * ``create_one_time_reveal_token(...)``          — operator issuance.
  * ``verify_one_time_reveal_token(...)``          — hash compare + expiry.
  * ``reveal_rotated_api_key_once(...)``           — deferred raw-key payload.
  * ``mark_reveal_attempt(...)``                   — attempt counter bump.
  * ``reveal_status(...)``                         — read-only.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `app.db.supabase_client`, `app.services.operator.audit_service`, `datetime`, `get_supabase`, `hashlib`, `log_operator_action`, `logging`, `secrets`, `timedelta`, `timezone`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_audit`, `_bound_brokerage_id`, `_bound_id`, `_get_db_safe`, `_iso`, `_lookup_rotation`, `_now_dt`, `_project_row`, `_safe_envelope`, `_sha256_hex`, `create_one_time_reveal_token`, `mark_reveal_attempt`, `reveal_rotated_api_key_once`, `reveal_status`, `verify_one_time_reveal_token`

## Env-key candidates

`ALLOWED_REVEAL_STATUSES`, `APPROVED`, `FAILED`, `OPERATOR`, `REVEAL_TOKEN_TTL_SECONDS`, `SUCCESS`

## String constants (redacted where noted)

- '\nPAS-SECURITY-04 — One-time API-key reveal service.\n\nImplements the token-issue / verify / attempt-tracking\nsurface for a one-time raw-key reveal on a rotated tenant\nAPI key. The token machinery is fully functional; the actual\nraw-key payload is **deferred** because PAS does not yet have\na vetted key-generation pipeline that holds the raw key\nbriefly during the reveal window.\n\nDoctrine carried from\n[docs/pas_api_key_delivery_doctrine.md](../../../docs/pas_api_key_delivery_doctrine.md):\n\n* **One-time only.** Once `revealed_at` is set, every\n  subsequent reveal attempt returns\n  ``error_code="reveal_already_consumed"``.\n* **Short-lived.** Reveal tokens expire (default 5 minutes\n  after `effective_at`). Service refuses to reveal after\n  expiry.\n* **Hashed tokens only.** v34 schema stores the sha256 hex of\n  the token, not the raw token. The raw token is returned\n  to the operator exactly once at issuance.\n* **Raw key NEVER stored.** PAS does not persist the raw key\n  in any column. The deferred-raw-key behaviour returns\n  ``status="deferred"`` + ``error_code="raw_key_reveal_unsupported"``\n  until PAS-SECURITY-05+ wires a vetted ephemeral storage\n  channel.\n* **Audit-logged.** Every reveal attempt — success, expired,\n  already-consumed, deferred — writes a PAS174 audit row via\n  ``log_operator_action``.\n* **Rate-limited at the route layer** (PAS-SECURITY-02\n  ``api_key_rotation`` surface — 3/hour/brokerage).\n* **NEVER raises.**\n\nPublic surface:\n\n  * ``REVEAL_TOKEN_TTL_SECONDS``                   — closed constant.\n  * ``ALLOWED_REVEAL_STATUSES``                    — closed enum.\n  * ``create_one_time_reveal_token(...)``          — operator issuance.\n  * ``verify_one_time_reveal_token(...)``          — hash compare + expiry.\n  * ``reveal_rotated_api_key_once(...)``           — deferred raw-key payload.\n  * ``mark_reveal_attempt(...)``                   — attempt counter bump.\n  * ``reveal_status(...)``                         — read-only.\n'
- 'pas.security.api_key_reveal'
- 'pas_api_key_rotation_events'
- 'int'
- 'REVEAL_TOKEN_TTL_SECONDS'
- 'Tuple[str, ...]'
- 'ALLOWED_REVEAL_STATUSES'
- 'brokerage_id'
- 'actor_type'
- 'actor_id'
- 'warning_count'
- 'rotation'
- 'reveal_token'
- 'raw_api_key'
- 'expires_at'
- 'warnings'
- 'error_code'
- 'one_time'
- 'OPERATOR'
- 'audit_status'
- 'SUCCESS'
- 'event'
- 'security.api_key_reveal.event'
- 'ttl_seconds'
- 'success'
- 'return'
- 'datetime'
- 'str'
- 'seconds'
- 'api_key_reveal db client unavailable type='
- 'value'
- 'Any'
- 'Optional[str]'
- 'max_len'
- 🔒 '<REDACTED:high-entropy blob, len=64>'
- 'utf-8'
- 'row'
- 'Optional[Dict[str, Any]]'
- 'status'
- 'Optional[List[str]]'
- 'bool'
- 'Dict[str, Any]'
- 'rotation_id'
- 'data'
- '_lookup_rotation error type='
- 'action'
- 'record'
- 'FAILED'
- 'api_key_rotation_event'
- '_audit api_key_reveal error type='
- 'Optional[int]'
- 'Operator-driven token issuance. NEVER raises.\n\nGenerates a 32-byte URL-safe token (≈43 chars), stores its\nsha256 hex in the row, and returns the **raw token to the\ncaller exactly once**. The caller is responsible for\ndelivering the token to the tenant through the existing\nsecure channel (Tier A in pas_api_key_delivery_doctrine.md).\n\nThe reveal endpoint later requires the tenant to present\nthis token; the service compares the sha256 hex against\nthe stored hash. Mismatches fail closed.\n'
- 'failed'
- 'invalid_actor_type'
- 'invalid_actor_id'
- 'invalid_rotation_id'
- 'skipped'
- 'api_key_rotation_store_unavailable'
- 'rotation_not_found'
- 'APPROVED'
- 'rotation_not_in_approved_state'
- 'rotation_status:'
- 'revealed_at'
- 'reveal_already_consumed'
- 'reveal_token_hash'
- 'reveal_token_expires_at'
- 'create_one_time_reveal_token update error type='
- 'db_write_failed:'
- 'policy_refused_or_no_rows'
- 'issue_reveal_token'
- 'security.api_key_reveal.created'
- 'raw_token'
- 'Verify the raw token against the stored hash. NEVER\nraises. NEVER echoes the token. Returns:\n\n  * ``status="ok"``                       — token valid + unexpired + unrevealed.\n  * ``status="reveal_token_invalid"``    — hash mismatch.\n  * ``status="reveal_token_expired"``    — TTL elapsed.\n  * ``status="reveal_already_consumed"`` — already revealed.\n  * ``status="rotation_not_found"``      — bad rotation id or cross-brokerage.\n'
- 'reveal_token_invalid'
- 'rotation_not_found_or_cross_brokerage'
- '+00:00'
- 'reveal_token_expired'
- 'reveal_attempt_count'
- 'reveal_attempt_limit_exceeded'
- 'Increment reveal_attempt_count + (on success) stamp\nrevealed_at. NEVER raises.'
- 'mark_reveal_attempt update error type='
- 'The actual raw-key reveal path. NEVER raises.\n\nPAS-SECURITY-04 invariant: PAS does NOT have a vetted\nephemeral key-storage channel that can safely hold the\nraw key for the reveal window. The function therefore\nreturns ``status="deferred"`` + ``error_code="raw_key_reveal_unsupported"``\nUNLESS a future PAS-SECURITY-05+ phase wires the safe\nstorage surface.\n\nThe function STILL:\n  * Verifies the token (catches replay / wrong-token).\n  * Records the attempt (audit + counter).\n  * Returns the closed envelope.\n\nThis means the operator can build the tenant-facing flow\nend-to-end today; the actual raw key delivery still goes\nthrough Tier A / Tier B until the PAS-SECURITY-05 ephemeral\nstorage lands.\n'
- 'missing_brokerage_id'
- 'reveal_rotated_api_key'
- 'security.api_key_reveal.failed'
- 'raw_key_reveal_unsupported'
- 'deferred'
- 'Read-only status of the reveal token + counter.\nNEVER raises. NEVER returns the raw token or key.'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS-SECURITY-04 — One-time API-key reveal service.\n\nImplements the token-issue / verify / attempt-tracking\nsurface for a one-time raw-key reveal on a rotated tenant\nAPI key. The token machinery is fully functional; the actual\nraw-key payload is **deferred** because PAS does not yet have\na vetted key-generation pipeline that holds the raw key\nbriefly during the reveal window.\n\nDoctrine carried from\n[docs/pas_api_key_delivery_doctrine.md](../../../docs/pas_api_key_delivery_doctrine.md):\n\n* **One-time only.** Once `revealed_at` is set, every\n  subsequent reveal attempt returns\n  ``error_code="reveal_already_consumed"``.\n* **Short-lived.** Reveal tokens expire (default 5 minutes\n  after `effective_at`). Service refuses to reveal after\n  expiry.\n* **Hashed tokens only.** v34 schema stores the sha256 hex of\n  the token, not the raw token. The raw token is returned\n  to the operator exactly once at issuance.\n* **Raw key NEVER stored.** PAS does not persist the raw key\n  in any column. The deferred-raw-key behaviour returns\n  ``status="deferred"`` + ``error_code="raw_key_reveal_unsupported"``\n  until PAS-SECURITY-05+ wires a vetted ephemeral storage\n  channel.\n* **Audit-logged.** Every reveal attempt — success, expired,\n  already-consumed, deferred — writes a PAS174 audit row via\n  ``log_operator_action``.\n* **Rate-limited at the route layer** (PAS-SECURITY-02\n  ``api_key_rotation`` surface — 3/hour/brokerage).\n* **NEVER raises.**\n\nPublic surface:\n\n  * ``REVEAL_TOKEN_TTL_SECONDS``                   — closed constant.\n  * ``ALLOWED_REVEAL_STATUSES``                    — closed enum.\n  * ``create_one_time_reveal_token(...)``          — operator issuance.\n  * ``verify_one_time_reveal_token(...)``          — hash compare + expiry.\n  * ``reveal_rotated_api_key_once(...)``           — deferred raw-key payload.\n  * ``mark_reveal_attempt(...)``                   — attempt counter bump.\n  * ``reveal_status(...)``                         — read-only.\n')
               STORE_NAME               1 (__doc__)

  46           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  48           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (hashlib)
               STORE_NAME               4 (hashlib)

  49           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (logging)
               STORE_NAME               5 (logging)

  50           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (secrets)
               STORE_NAME               6 (secrets)

  51           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (uuid)
               STORE_NAME               7 (uuid)

  52           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timedelta', 'timezone'))
               IMPORT_NAME              8 (datetime)
               IMPORT_FROM              8 (datetime)
               STORE_NAME               8 (datetime)
               IMPORT_FROM              9 (timedelta)
               STORE_NAME               9 (timedelta)
               IMPORT_FROM             10 (timezone)
               STORE_NAME              10 (timezone)
               POP_TOP

  53           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (Any)
               STORE_NAME              12 (Any)
               IMPORT_FROM             13 (Dict)
               STORE_NAME              13 (Dict)
               IMPORT_FROM             14 (List)
               STORE_NAME              14 (List)
               IMPORT_FROM             15 (Optional)
               STORE_NAME              15 (Optional)
               IMPORT_FROM             16 (Tuple)
               STORE_NAME              16 (Tuple)
               POP_TOP

  56           LOAD_NAME                5 (logging)
               LOAD_ATTR               34 (getLogger)
               PUSH_NULL
               LOAD_CONST               5 ('pas.security.api_key_reveal')
               CALL                     1
               STORE_NAME              18 (logger)

  59           LOAD_CONST               6 ('pas_api_key_rotation_events')
               STORE_NAME              19 (_TABLE)

  64           LOAD_CONST               7 (300)
               STORE_NAME              20 (REVEAL_TOKEN_TTL_SECONDS)
               LOAD_CONST               8 ('int')
               LOAD_NAME               21 (__annotations__)
               LOAD_CONST               9 ('REVEAL_TOKEN_TTL_SECONDS')
               STORE_SUBSCR

  68           LOAD_CONST              60 (('ok', 'deferred', 'reveal_already_consumed', 'reveal_token_expired', 'reveal_token_invalid', 'reveal_attempt_limit_exceeded', 'rotation_not_found', 'skipped', 'failed'))
               STORE_NAME              22 (ALLOWED_REVEAL_STATUSES)
               LOAD_CONST              10 ('Tuple[str, ...]')
               LOAD_NAME               21 (__annotations__)
               LOAD_CONST              11 ('ALLOWED_REVEAL_STATUSES')
               STORE_SUBSCR

  82           LOAD_SMALL_INT         200
               STORE_NAME              23 (_BROKERAGE_ID_MAX_LEN)

  83           LOAD_SMALL_INT         200
               STORE_NAME              24 (_ROTATION_ID_MAX_LEN)

  84           LOAD_SMALL_INT         200
               STORE_NAME              25 (_ACTOR_ID_MAX_LEN)

  85           LOAD_SMALL_INT          32
               STORE_NAME              26 (_RAW_TOKEN_BYTES)

  86           LOAD_SMALL_INT           5
               STORE_NAME              27 (_MAX_ATTEMPTS)

  89           LOAD_CONST              61 (('rotation_id', 'brokerage_id', 'requested_at', 'actor_type', 'actor_id', 'status', 'previous_key_fingerprint', 'new_key_fingerprint', 'effective_at', 'warning_count', 'metadata', 'reveal_token_hash', 'reveal_token_expires_at', 'revealed_at', 'reveal_attempt_count'))
               STORE_NAME              28 (_STRUCTURAL_COLUMNS)

 113           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA3780, file "app/services/security/api_key_reveal.py", line 113>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _now_dt at 0x0000018C18053870, file "app/services/security/api_key_reveal.py", line 113>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              29 (_now_dt)

 117           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3690, file "app/services/security/api_key_reveal.py", line 117>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _iso at 0x0000018C18025C30, file "app/services/security/api_key_reveal.py", line 117>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              30 (_iso)

 121           LOAD_CONST              20 (<code object _get_db_safe at 0x0000018C17FF10B0, file "app/services/security/api_key_reveal.py", line 121>)
               MAKE_FUNCTION
               STORE_NAME              31 (_get_db_safe)

 132           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA1E30, file "app/services/security/api_key_reveal.py", line 132>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object _bound_brokerage_id at 0x0000018C17F96420, file "app/services/security/api_key_reveal.py", line 132>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_bound_brokerage_id)

 141           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C18026430, file "app/services/security/api_key_reveal.py", line 141>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object _bound_id at 0x0000018C1796DBD0, file "app/services/security/api_key_reveal.py", line 141>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              33 (_bound_id)

 159           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA30F0, file "app/services/security/api_key_reveal.py", line 159>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object _sha256_hex at 0x0000018C18038670, file "app/services/security/api_key_reveal.py", line 159>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_sha256_hex)

 163           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA2E20, file "app/services/security/api_key_reveal.py", line 163>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object _project_row at 0x0000018C17FE1680, file "app/services/security/api_key_reveal.py", line 163>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (_project_row)

 173           LOAD_CONST              29 ('rotation')

 176           LOAD_CONST               2 (None)

 173           LOAD_CONST              30 ('reveal_token')

 177           LOAD_CONST               2 (None)

 173           LOAD_CONST              31 ('raw_api_key')

 178           LOAD_CONST               2 (None)

 173           LOAD_CONST              32 ('expires_at')

 179           LOAD_CONST               2 (None)

 173           LOAD_CONST              33 ('warnings')

 180           LOAD_CONST               2 (None)

 173           LOAD_CONST              34 ('error_code')

 181           LOAD_CONST               2 (None)

 173           LOAD_CONST              35 ('one_time')

 182           LOAD_CONST              36 (False)

 173           BUILD_MAP                7
               LOAD_CONST              37 (<code object __annotate__ at 0x0000018C17FBFEE0, file "app/services/security/api_key_reveal.py", line 173>)
               MAKE_FUNCTION
               LOAD_CONST              38 (<code object _safe_envelope at 0x0000018C17C49B80, file "app/services/security/api_key_reveal.py", line 173>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              36 (_safe_envelope)

 203           LOAD_CONST              12 ('brokerage_id')

 207           LOAD_CONST               2 (None)

 203           BUILD_MAP                1
               LOAD_CONST              39 (<code object __annotate__ at 0x0000018C18025830, file "app/services/security/api_key_reveal.py", line 203>)
               MAKE_FUNCTION
               LOAD_CONST              40 (<code object _lookup_rotation at 0x0000018C17EE1CC0, file "app/services/security/api_key_reveal.py", line 203>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              37 (_lookup_rotation)

 230           LOAD_CONST              13 ('actor_type')

 234           LOAD_CONST              41 ('OPERATOR')

 230           LOAD_CONST              14 ('actor_id')

 235           LOAD_CONST               2 (None)

 230           LOAD_CONST              42 ('audit_status')

 236           LOAD_CONST              43 ('SUCCESS')

 230           LOAD_CONST              34 ('error_code')

 237           LOAD_CONST               2 (None)

 230           LOAD_CONST              44 ('event')

 238           LOAD_CONST              45 ('security.api_key_reveal.event')

 230           LOAD_CONST              15 ('warning_count')

 239           LOAD_SMALL_INT           0

 230           BUILD_MAP                6
               LOAD_CONST              46 (<code object __annotate__ at 0x0000018C1812C030, file "app/services/security/api_key_reveal.py", line 230>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object _audit at 0x0000018C179A7290, file "app/services/security/api_key_reveal.py", line 230>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              38 (_audit)

 269           LOAD_CONST              13 ('actor_type')

 272           LOAD_CONST              41 ('OPERATOR')

 269           LOAD_CONST              14 ('actor_id')

 273           LOAD_CONST               2 (None)

 269           LOAD_CONST              48 ('ttl_seconds')

 274           LOAD_CONST               2 (None)

 269           BUILD_MAP                3
               LOAD_CONST              49 (<code object __annotate__ at 0x0000018C18024B30, file "app/services/security/api_key_reveal.py", line 269>)
               MAKE_FUNCTION
               LOAD_CONST              50 (<code object create_one_time_reveal_token at 0x0000018C17F3B130, file "app/services/security/api_key_reveal.py", line 269>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              39 (create_one_time_reveal_token)

 383           LOAD_CONST              12 ('brokerage_id')

 387           LOAD_CONST               2 (None)

 383           BUILD_MAP                1
               LOAD_CONST              51 (<code object __annotate__ at 0x0000018C18025130, file "app/services/security/api_key_reveal.py", line 383>)
               MAKE_FUNCTION
               LOAD_CONST              52 (<code object verify_one_time_reveal_token at 0x0000018C17F41160, file "app/services/security/api_key_reveal.py", line 383>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              40 (verify_one_time_reveal_token)

 478           LOAD_CONST              53 ('success')

 481           LOAD_CONST              36 (False)

 478           LOAD_CONST              12 ('brokerage_id')

 482           LOAD_CONST               2 (None)

 478           BUILD_MAP                2
               LOAD_CONST              54 (<code object __annotate__ at 0x0000018C18026030, file "app/services/security/api_key_reveal.py", line 478>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object mark_reveal_attempt at 0x0000018C1778AA50, file "app/services/security/api_key_reveal.py", line 478>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              41 (mark_reveal_attempt)

 544           LOAD_CONST              56 (<code object __annotate__ at 0x0000018C18025030, file "app/services/security/api_key_reveal.py", line 544>)
               MAKE_FUNCTION
               LOAD_CONST              57 (<code object reveal_rotated_api_key_once at 0x0000018C17F74290, file "app/services/security/api_key_reveal.py", line 544>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (reveal_rotated_api_key_once)

 631           LOAD_CONST              58 (<code object __annotate__ at 0x0000018C18024930, file "app/services/security/api_key_reveal.py", line 631>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object reveal_status at 0x0000018C1801C410, file "app/services/security/api_key_reveal.py", line 631>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (reveal_status)

 663           BUILD_LIST               0
               LOAD_CONST              62 (('REVEAL_TOKEN_TTL_SECONDS', 'ALLOWED_REVEAL_STATUSES', 'create_one_time_reveal_token', 'verify_one_time_reveal_token', 'reveal_rotated_api_key_once', 'mark_reveal_attempt', 'reveal_status'))
               LIST_EXTEND              1
               STORE_NAME              44 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app/services/security/api_key_reveal.py", line 113>:
113           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('datetime')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _now_dt at 0x0000018C18053870, file "app/services/security/api_key_reveal.py", line 113>:
113           RESUME                   0

114           LOAD_GLOBAL              0 (datetime)
              LOAD_ATTR                2 (now)
              PUSH_NULL
              LOAD_GLOBAL              4 (timezone)
              LOAD_ATTR                6 (utc)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app/services/security/api_key_reveal.py", line 117>:
117           RESUME                   0
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

Disassembly of <code object _iso at 0x0000018C18025C30, file "app/services/security/api_key_reveal.py", line 117>:
117           RESUME                   0

118           LOAD_FAST_BORROW         0 (dt)
              LOAD_ATTR                1 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object _get_db_safe at 0x0000018C17FF10B0, file "app/services/security/api_key_reveal.py", line 121>:
 121           RESUME                   0

 122           NOP

 123   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 124           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 125           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 126   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 127           LOAD_CONST               2 ('api_key_reveal db client unavailable type=')
               LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE
               BUILD_STRING             2

 126           CALL                     1
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

 125   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "app/services/security/api_key_reveal.py", line 132>:
132           RESUME                   0
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

Disassembly of <code object _bound_brokerage_id at 0x0000018C17F96420, file "app/services/security/api_key_reveal.py", line 132>:
132           RESUME                   0

133           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

134           LOAD_CONST               0 (None)
              RETURN_VALUE

135   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

136           LOAD_FAST_BORROW         1 (s)
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

137   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

138   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "app/services/security/api_key_reveal.py", line 141>:
141           RESUME                   0
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

Disassembly of <code object _bound_id at 0x0000018C1796DBD0, file "app/services/security/api_key_reveal.py", line 141>:
141           RESUME                   0

142           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

143           LOAD_CONST               0 (None)
              RETURN_VALUE

144   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (s)

145           LOAD_FAST_BORROW         2 (s)
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

146   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

148   L3:     LOAD_GLOBAL              9 (set + NULL)

149           LOAD_CONST               1 ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_')

148           CALL                     1
              STORE_FAST               3 (keep)

153           LOAD_FAST_BORROW         2 (s)
              GET_ITER
      L4:     FOR_ITER                12 (to L6)
              STORE_FAST               4 (ch)

154           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (ch, keep)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L4)

155   L5:     POP_TOP
              LOAD_CONST               0 (None)
              RETURN_VALUE

153   L6:     END_FOR
              POP_ITER

156           LOAD_FAST_BORROW         2 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "app/services/security/api_key_reveal.py", line 159>:
159           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _sha256_hex at 0x0000018C18038670, file "app/services/security/api_key_reveal.py", line 159>:
159           RESUME                   0

160           LOAD_GLOBAL              0 (hashlib)
              LOAD_ATTR                2 (sha256)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (encode + NULL|self)
              LOAD_CONST               0 ('utf-8')
              CALL                     1
              CALL                     1
              LOAD_ATTR                7 (hexdigest + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app/services/security/api_key_reveal.py", line 163>:
163           RESUME                   0
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

Disassembly of <code object _project_row at 0x0000018C17FE1680, file "app/services/security/api_key_reveal.py", line 163>:
163           RESUME                   0

164           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

165           LOAD_CONST               0 (None)
              RETURN_VALUE

166   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

167           LOAD_GLOBAL              4 (_STRUCTURAL_COLUMNS)
              GET_ITER
      L2:     FOR_ITER                21 (to L4)
              STORE_FAST               2 (col)

168           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (col, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

169   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, col)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, col)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L2)

167   L4:     END_FOR
              POP_ITER

170           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FBFEE0, file "app/services/security/api_key_reveal.py", line 173>:
173           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

175           LOAD_CONST               2 ('str')

173           LOAD_CONST               3 ('rotation')

176           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

173           LOAD_CONST               5 ('reveal_token')

177           LOAD_CONST               6 ('Optional[str]')

173           LOAD_CONST               7 ('raw_api_key')

178           LOAD_CONST               6 ('Optional[str]')

173           LOAD_CONST               8 ('expires_at')

179           LOAD_CONST               6 ('Optional[str]')

173           LOAD_CONST               9 ('warnings')

180           LOAD_CONST              10 ('Optional[List[str]]')

173           LOAD_CONST              11 ('error_code')

181           LOAD_CONST               6 ('Optional[str]')

173           LOAD_CONST              12 ('one_time')

182           LOAD_CONST              13 ('bool')

173           LOAD_CONST              14 ('return')

183           LOAD_CONST              15 ('Dict[str, Any]')

173           BUILD_MAP                9
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C17C49B80, file "app/services/security/api_key_reveal.py", line 173>:
173           RESUME                   0

185           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

186           LOAD_CONST               1 ('rotation')
              LOAD_FAST                1 (rotation)

191           LOAD_CONST               2 ('reveal_token')
              LOAD_FAST                2 (reveal_token)

195           LOAD_CONST               3 ('raw_api_key')
              LOAD_FAST                3 (raw_api_key)

196           LOAD_CONST               4 ('expires_at')
              LOAD_FAST                4 (expires_at)

197           LOAD_CONST               5 ('one_time')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         7 (one_time)
              CALL                     1

198           LOAD_CONST               6 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                5 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

199           LOAD_CONST               7 ('error_code')
              LOAD_FAST_BORROW         6 (error_code)

184           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025830, file "app/services/security/api_key_reveal.py", line 203>:
203           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('db')

204           LOAD_CONST               2 ('Any')

203           LOAD_CONST               3 ('rotation_id')

206           LOAD_CONST               4 ('str')

203           LOAD_CONST               5 ('brokerage_id')

207           LOAD_CONST               6 ('Optional[str]')

203           LOAD_CONST               7 ('return')

208           LOAD_CONST               8 ('Optional[Dict[str, Any]]')

203           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _lookup_rotation at 0x0000018C17EE1CC0, file "app/services/security/api_key_reveal.py", line 203>:
 203            RESUME                   0

 209            NOP

 211    L1:     LOAD_FAST_BORROW         0 (db)
                LOAD_ATTR                1 (table + NULL|self)
                LOAD_GLOBAL              2 (_TABLE)
                CALL                     1

 212            LOAD_ATTR                5 (select + NULL|self)
                LOAD_CONST               0 (',')
                LOAD_ATTR                7 (join + NULL|self)
                LOAD_GLOBAL              8 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 213            LOAD_ATTR               11 (eq + NULL|self)
                LOAD_CONST               1 ('rotation_id')
                LOAD_FAST_BORROW         1 (rotation_id)
                CALL                     2

 214            LOAD_ATTR               13 (limit + NULL|self)
                LOAD_SMALL_INT           2
                CALL                     1

 210            STORE_FAST               3 (query)

 216            LOAD_FAST_BORROW         2 (brokerage_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L4)
        L2:     NOT_TAKEN

 217    L3:     LOAD_FAST_BORROW         3 (query)
                LOAD_ATTR               11 (eq + NULL|self)
                LOAD_CONST               2 ('brokerage_id')
                LOAD_FAST_BORROW         2 (brokerage_id)
                CALL                     2
                STORE_FAST               3 (query)

 218    L4:     LOAD_FAST_BORROW         3 (query)
                LOAD_ATTR               15 (execute + NULL|self)
                CALL                     0
                STORE_FAST               4 (result)

 219            LOAD_GLOBAL             17 (list + NULL)
                LOAD_GLOBAL             19 (getattr + NULL)
                LOAD_FAST_BORROW         4 (result)
                LOAD_CONST               3 ('data')
                LOAD_CONST               4 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                BUILD_LIST               0
        L7:     CALL                     1
                STORE_FAST               5 (rows)

 220            LOAD_FAST_BORROW         5 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
        L8:     NOT_TAKEN

 221            LOAD_CONST               4 (None)
                RETURN_VALUE

 222    L9:     LOAD_GLOBAL             21 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_GLOBAL             22 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       10 (to L11)
                NOT_TAKEN
                LOAD_FAST_BORROW         5 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
       L10:     RETURN_VALUE
       L11:     LOAD_CONST               4 (None)
       L12:     RETURN_VALUE

  --   L13:     PUSH_EXC_INFO

 223            LOAD_GLOBAL             24 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L17)
                NOT_TAKEN
                STORE_FAST               6 (e)

 224   L14:     LOAD_GLOBAL             26 (logger)
                LOAD_ATTR               29 (warning + NULL|self)

 225            LOAD_CONST               5 ('_lookup_rotation error type=')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 224            CALL                     1
                POP_TOP

 227   L15:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                LOAD_CONST               4 (None)
                RETURN_VALUE

  --   L16:     LOAD_CONST               4 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 223   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L13 [0]
  L3 to L5 -> L13 [0]
  L6 to L8 -> L13 [0]
  L9 to L10 -> L13 [0]
  L11 to L12 -> L13 [0]
  L13 to L14 -> L18 [1] lasti
  L14 to L15 -> L16 [1] lasti
  L16 to L18 -> L18 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C1812C030, file "app/services/security/api_key_reveal.py", line 230>:
230           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('action')

232           LOAD_CONST               2 ('str')

230           LOAD_CONST               3 ('record')

233           LOAD_CONST               4 ('Dict[str, Any]')

230           LOAD_CONST               5 ('actor_type')

234           LOAD_CONST               2 ('str')

230           LOAD_CONST               6 ('actor_id')

235           LOAD_CONST               7 ('Optional[str]')

230           LOAD_CONST               8 ('audit_status')

236           LOAD_CONST               2 ('str')

230           LOAD_CONST               9 ('error_code')

237           LOAD_CONST               7 ('Optional[str]')

230           LOAD_CONST              10 ('event')

238           LOAD_CONST               2 ('str')

230           LOAD_CONST              11 ('warning_count')

239           LOAD_CONST              12 ('int')

230           LOAD_CONST              13 ('return')

240           LOAD_CONST              14 ('Optional[Dict[str, Any]]')

230           BUILD_MAP                9
              RETURN_VALUE

Disassembly of <code object _audit at 0x0000018C179A7290, file "app/services/security/api_key_reveal.py", line 230>:
 230            RESUME                   0

 241            NOP

 242    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('log_operator_action',))
                IMPORT_NAME              0 (app.services.operator.audit_service)
                IMPORT_FROM              1 (log_operator_action)
                STORE_FAST               8 (log_operator_action)
                POP_TOP

 243            LOAD_FAST_BORROW         2 (actor_type)
                LOAD_CONST              13 (('OPERATOR', 'ADMIN', 'SYSTEM'))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN
                LOAD_FAST                2 (actor_type)
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               2 ('OPERATOR')
        L3:     STORE_FAST               9 (mapped_actor)

 244            LOAD_FAST                8 (log_operator_action)
                PUSH_NULL

 245            LOAD_FAST_BORROW         1 (record)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               3 ('brokerage_id')
                CALL                     1

 246            LOAD_FAST                9 (mapped_actor)

 247            LOAD_FAST                3 (actor_id)

 248            LOAD_FAST                0 (action)

 249            LOAD_FAST_BORROW         5 (error_code)
                POP_JUMP_IF_NOT_NONE     3 (to L4)
                NOT_TAKEN
                LOAD_CONST               5 ('SUCCESS')
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               6 ('FAILED')

 250    L5:     LOAD_CONST               7 ('api_key_rotation_event')

 251            LOAD_FAST_BORROW         1 (record)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               8 ('rotation_id')
                CALL                     1

 252            LOAD_FAST_BORROW         7 (warning_count)

 254            LOAD_CONST               9 ('event')
                LOAD_FAST_BORROW         6 (event)

 255            LOAD_CONST              10 ('error_code')
                LOAD_FAST_BORROW         5 (error_code)

 253            BUILD_MAP                2

 244            LOAD_CONST              11 (('brokerage_id', 'actor_type', 'actor_id', 'action', 'status', 'target_type', 'target_id', 'warning_count', 'metadata'))
                CALL_KW                  9
        L6:     RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 258            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L11)
                NOT_TAKEN
                STORE_FAST              10 (e)

 259    L8:     LOAD_GLOBAL              8 (logger)
                LOAD_ATTR               11 (warning + NULL|self)

 260            LOAD_CONST              12 ('_audit api_key_reveal error type=')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 259            CALL                     1
                POP_TOP

 262    L9:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                LOAD_CONST               4 (None)
                RETURN_VALUE

  --   L10:     LOAD_CONST               4 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 258   L11:     RERAISE                  0

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L6 -> L7 [0]
  L7 to L8 -> L12 [1] lasti
  L8 to L9 -> L10 [1] lasti
  L10 to L12 -> L12 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app/services/security/api_key_reveal.py", line 269>:
269           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rotation_id')

271           LOAD_CONST               2 ('str')

269           LOAD_CONST               3 ('actor_type')

272           LOAD_CONST               2 ('str')

269           LOAD_CONST               4 ('actor_id')

273           LOAD_CONST               5 ('Optional[str]')

269           LOAD_CONST               6 ('ttl_seconds')

274           LOAD_CONST               7 ('Optional[int]')

269           LOAD_CONST               8 ('return')

275           LOAD_CONST               9 ('Dict[str, Any]')

269           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object create_one_time_reveal_token at 0x0000018C17F3B130, file "app/services/security/api_key_reveal.py", line 269>:
 269            RESUME                   0

 288            LOAD_FAST_BORROW         1 (actor_type)
                LOAD_CONST              34 (('OPERATOR', 'ADMIN'))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       14 (to L1)
                NOT_TAKEN

 289            LOAD_GLOBAL              1 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               2 ('invalid_actor_type')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 290    L1:     LOAD_FAST_BORROW         2 (actor_id)
                POP_JUMP_IF_NONE        17 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              3 (_bound_id + NULL)
                LOAD_FAST_BORROW         2 (actor_id)
                LOAD_GLOBAL              4 (_ACTOR_ID_MAX_LEN)
                CALL                     2
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               4 (None)
        L3:     STORE_FAST               4 (actor)

 291            LOAD_FAST_BORROW         2 (actor_id)
                POP_JUMP_IF_NONE        18 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (actor)
                POP_JUMP_IF_NOT_NONE    14 (to L4)
                NOT_TAKEN

 292            LOAD_GLOBAL              1 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               5 ('invalid_actor_id')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 293    L4:     LOAD_GLOBAL              3 (_bound_id + NULL)
                LOAD_FAST_BORROW         0 (rotation_id)
                LOAD_GLOBAL              6 (_ROTATION_ID_MAX_LEN)
                CALL                     2
                STORE_FAST               5 (rid)

 294            LOAD_FAST_BORROW         5 (rid)
                POP_JUMP_IF_NOT_NONE    14 (to L5)
                NOT_TAKEN

 295            LOAD_GLOBAL              1 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               6 ('invalid_rotation_id')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 297    L5:     LOAD_GLOBAL              8 (REVEAL_TOKEN_TTL_SECONDS)
                STORE_FAST               6 (ttl)

 298            NOP

 299    L6:     LOAD_FAST_BORROW         3 (ttl_seconds)
                POP_JUMP_IF_NONE        32 (to L7)
                NOT_TAKEN

 300            LOAD_GLOBAL             11 (max + NULL)
                LOAD_SMALL_INT          60
                LOAD_GLOBAL             13 (min + NULL)
                LOAD_GLOBAL             15 (int + NULL)
                LOAD_FAST_BORROW         3 (ttl_seconds)
                CALL                     1
                LOAD_CONST               7 (3600)
                CALL                     2
                CALL                     2
                STORE_FAST               6 (ttl)

 304    L7:     LOAD_GLOBAL             21 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               7 (db)

 305            LOAD_FAST                7 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L8)
                NOT_TAKEN

 306            LOAD_GLOBAL              1 (_safe_envelope + NULL)

 307            LOAD_CONST               8 ('skipped')

 308            LOAD_CONST               9 ('api_key_rotation_store_unavailable')
                BUILD_LIST               1

 309            LOAD_CONST               9 ('api_key_rotation_store_unavailable')

 306            LOAD_CONST              10 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 312    L8:     LOAD_GLOBAL             23 (_lookup_rotation + NULL)
                LOAD_FAST_LOAD_FAST    117 (db, rid)
                LOAD_CONST              11 (('rotation_id',))
                CALL_KW                  2
                STORE_FAST               8 (current)

 313            LOAD_FAST                8 (current)
                POP_JUMP_IF_NOT_NONE    14 (to L9)
                NOT_TAKEN

 314            LOAD_GLOBAL              1 (_safe_envelope + NULL)

 315            LOAD_CONST               1 ('failed')
                LOAD_CONST              12 ('rotation_not_found')

 314            LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 317    L9:     LOAD_FAST                8 (current)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              13 ('status')
                CALL                     1
                LOAD_CONST              14 ('APPROVED')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       34 (to L10)
                NOT_TAKEN

 318            LOAD_GLOBAL              1 (_safe_envelope + NULL)

 319            LOAD_CONST               1 ('failed')

 320            LOAD_CONST              15 ('rotation_not_in_approved_state')

 321            LOAD_CONST              16 ('rotation_status:')
                LOAD_FAST                8 (current)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              13 ('status')
                CALL                     1
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 318            LOAD_CONST              17 (('status', 'error_code', 'warnings'))
                CALL_KW                  3
                RETURN_VALUE

 323   L10:     LOAD_FAST                8 (current)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              18 ('revealed_at')
                CALL                     1
                POP_JUMP_IF_NONE        14 (to L11)
                NOT_TAKEN

 324            LOAD_GLOBAL              1 (_safe_envelope + NULL)

 325            LOAD_CONST              19 ('reveal_already_consumed')

 326            LOAD_CONST              19 ('reveal_already_consumed')

 324            LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 329   L11:     LOAD_GLOBAL             26 (secrets)
                LOAD_ATTR               28 (token_urlsafe)
                PUSH_NULL
                LOAD_GLOBAL             30 (_RAW_TOKEN_BYTES)
                CALL                     1
                STORE_FAST               9 (raw_token)

 330            LOAD_GLOBAL             33 (_sha256_hex + NULL)
                LOAD_FAST                9 (raw_token)
                CALL                     1
                STORE_FAST              10 (token_hash)

 331            LOAD_GLOBAL             35 (_now_dt + NULL)
                CALL                     0
                LOAD_GLOBAL             37 (timedelta + NULL)
                LOAD_FAST                6 (ttl)
                LOAD_CONST              20 (('seconds',))
                CALL_KW                  1
                BINARY_OP                0 (+)
                STORE_FAST              11 (expires_at)

 332            LOAD_GLOBAL             39 (_iso + NULL)
                LOAD_FAST               11 (expires_at)
                CALL                     1
                STORE_FAST              12 (expires_iso)

 335            LOAD_CONST              21 ('reveal_token_hash')
                LOAD_FAST               10 (token_hash)

 336            LOAD_CONST              22 ('reveal_token_expires_at')
                LOAD_FAST               12 (expires_iso)

 334            BUILD_MAP                2
                STORE_FAST              13 (patch)

 338            NOP

 340   L12:     LOAD_FAST                7 (db)
                LOAD_ATTR               41 (table + NULL|self)
                LOAD_GLOBAL             42 (_TABLE)
                CALL                     1

 341            LOAD_ATTR               45 (update + NULL|self)
                LOAD_FAST               13 (patch)
                CALL                     1

 342            LOAD_ATTR               47 (eq + NULL|self)
                LOAD_CONST              23 ('rotation_id')
                LOAD_FAST                5 (rid)
                CALL                     2

 343            LOAD_ATTR               49 (execute + NULL|self)
                CALL                     0

 339            STORE_FAST              14 (upd)

 345            LOAD_GLOBAL             51 (list + NULL)
                LOAD_GLOBAL             53 (getattr + NULL)
                LOAD_FAST               14 (upd)
                LOAD_CONST              24 ('data')
                LOAD_CONST               4 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L13:     CALL                     1
                STORE_FAST              15 (rows_after)

 356   L14:     LOAD_FAST               15 (rows_after)
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L15)
                NOT_TAKEN

 357            LOAD_GLOBAL              1 (_safe_envelope + NULL)

 358            LOAD_CONST               1 ('failed')

 359            LOAD_CONST              27 ('policy_refused_or_no_rows')

 357            LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 362   L15:     LOAD_GLOBAL             65 (_project_row + NULL)
                LOAD_FAST               15 (rows_after)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                STORE_FAST              17 (new_record)

 363            LOAD_GLOBAL             67 (_audit + NULL)

 364            LOAD_CONST              28 ('issue_reveal_token')

 365            LOAD_FAST               17 (new_record)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST                8 (current)

 366   L16:     LOAD_FAST                1 (actor_type)

 367            LOAD_FAST                4 (actor)

 368            LOAD_CONST              29 ('security.api_key_reveal.created')

 363            LOAD_CONST              30 (('action', 'record', 'actor_type', 'actor_id', 'event'))
                CALL_KW                  5
                POP_TOP

 370            LOAD_GLOBAL              1 (_safe_envelope + NULL)

 371            LOAD_CONST              31 ('ok')

 372            LOAD_FAST               17 (new_record)

 373            LOAD_FAST                9 (raw_token)

 374            LOAD_FAST               12 (expires_iso)

 375            LOAD_CONST              32 (True)

 370            LOAD_CONST              33 (('status', 'rotation', 'reveal_token', 'expires_at', 'one_time'))
                CALL_KW                  5
                RETURN_VALUE

  --   L17:     PUSH_EXC_INFO

 301            LOAD_GLOBAL             16 (TypeError)
                LOAD_GLOBAL             18 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       11 (to L19)
                NOT_TAKEN
                POP_TOP

 302            LOAD_GLOBAL              8 (REVEAL_TOKEN_TTL_SECONDS)
                STORE_FAST               6 (ttl)
       L18:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 432 (to L7)

 301   L19:     RERAISE                  0

  --   L20:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L21:     PUSH_EXC_INFO

 346            LOAD_GLOBAL             54 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L26)
                NOT_TAKEN
                STORE_FAST              16 (e)

 347   L22:     LOAD_GLOBAL             56 (logger)
                LOAD_ATTR               59 (warning + NULL|self)

 348            LOAD_CONST              25 ('create_one_time_reveal_token update error type=')

 349            LOAD_GLOBAL             61 (type + NULL)
                LOAD_FAST               16 (e)
                CALL                     1
                LOAD_ATTR               62 (__name__)
                FORMAT_SIMPLE

 348            BUILD_STRING             2

 347            CALL                     1
                POP_TOP

 351            LOAD_GLOBAL              1 (_safe_envelope + NULL)

 352            LOAD_CONST               8 ('skipped')

 353            LOAD_CONST              26 ('db_write_failed:')
                LOAD_GLOBAL             61 (type + NULL)
                LOAD_FAST               16 (e)
                CALL                     1
                LOAD_ATTR               62 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 354            LOAD_CONST               9 ('api_key_rotation_store_unavailable')

 351            LOAD_CONST              10 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
       L23:     SWAP                     2
       L24:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              16 (e)
                DELETE_FAST             16 (e)
                RETURN_VALUE

  --   L25:     LOAD_CONST               4 (None)
                STORE_FAST              16 (e)
                DELETE_FAST             16 (e)
                RERAISE                  1

 346   L26:     RERAISE                  0

  --   L27:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L6 to L7 -> L17 [0]
  L12 to L14 -> L21 [0]
  L17 to L18 -> L20 [1] lasti
  L19 to L20 -> L20 [1] lasti
  L21 to L22 -> L27 [1] lasti
  L22 to L23 -> L25 [1] lasti
  L23 to L24 -> L27 [1] lasti
  L25 to L27 -> L27 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "app/services/security/api_key_reveal.py", line 383>:
383           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rotation_id')

385           LOAD_CONST               2 ('str')

383           LOAD_CONST               3 ('raw_token')

386           LOAD_CONST               2 ('str')

383           LOAD_CONST               4 ('brokerage_id')

387           LOAD_CONST               5 ('Optional[str]')

383           LOAD_CONST               6 ('return')

388           LOAD_CONST               7 ('Dict[str, Any]')

383           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object verify_one_time_reveal_token at 0x0000018C17F41160, file "app/services/security/api_key_reveal.py", line 383>:
 383            RESUME                   0

 398            LOAD_GLOBAL              1 (_bound_id + NULL)
                LOAD_FAST_BORROW         0 (rotation_id)
                LOAD_GLOBAL              2 (_ROTATION_ID_MAX_LEN)
                CALL                     2
                STORE_FAST               3 (rid)

 399            LOAD_FAST_BORROW         3 (rid)
                POP_JUMP_IF_NOT_NONE    14 (to L1)
                NOT_TAKEN

 400            LOAD_GLOBAL              5 (_safe_envelope + NULL)
                LOAD_CONST               2 ('failed')
                LOAD_CONST               3 ('invalid_rotation_id')
                LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 401    L1:     LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (raw_token)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (raw_token)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L3)
                NOT_TAKEN

 402    L2:     LOAD_GLOBAL              5 (_safe_envelope + NULL)

 403            LOAD_CONST               5 ('reveal_token_invalid')

 404            LOAD_CONST               5 ('reveal_token_invalid')

 402            LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 406    L3:     LOAD_FAST_BORROW         2 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L4)
                NOT_TAKEN
                LOAD_GLOBAL             13 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         2 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               1 (None)
        L5:     STORE_FAST               4 (bid)

 407            LOAD_GLOBAL             15 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               5 (db)

 408            LOAD_FAST_BORROW         5 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L6)
                NOT_TAKEN

 409            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 410            LOAD_CONST               6 ('skipped')

 411            LOAD_CONST               7 ('api_key_rotation_store_unavailable')
                BUILD_LIST               1

 412            LOAD_CONST               7 ('api_key_rotation_store_unavailable')

 409            LOAD_CONST               8 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 414    L6:     LOAD_GLOBAL             17 (_lookup_rotation + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (db, rid)
                LOAD_FAST_BORROW         4 (bid)
                LOAD_CONST               9 (('rotation_id', 'brokerage_id'))
                CALL_KW                  3
                STORE_FAST               6 (current)

 415            LOAD_FAST_BORROW         6 (current)
                POP_JUMP_IF_NOT_NONE    14 (to L7)
                NOT_TAKEN

 416            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 417            LOAD_CONST              10 ('rotation_not_found')

 418            LOAD_CONST              11 ('rotation_not_found_or_cross_brokerage')

 416            LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 420    L7:     LOAD_FAST_BORROW         6 (current)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              12 ('revealed_at')
                CALL                     1
                POP_JUMP_IF_NONE        24 (to L8)
                NOT_TAKEN

 421            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 422            LOAD_CONST              13 ('reveal_already_consumed')

 423            LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST_BORROW         6 (current)
                CALL                     1

 424            LOAD_CONST              13 ('reveal_already_consumed')

 421            LOAD_CONST              14 (('status', 'rotation', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 426    L8:     LOAD_FAST_BORROW         6 (current)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              15 ('reveal_token_hash')
                CALL                     1
                STORE_FAST               7 (stored_hash)

 427            LOAD_FAST_BORROW         6 (current)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              16 ('reveal_token_expires_at')
                CALL                     1
                STORE_FAST               8 (expires_at)

 428            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         7 (stored_hash)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L9)
                NOT_TAKEN
                LOAD_FAST_BORROW         7 (stored_hash)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        24 (to L10)
                NOT_TAKEN

 429    L9:     LOAD_GLOBAL              5 (_safe_envelope + NULL)

 430            LOAD_CONST               5 ('reveal_token_invalid')

 431            LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST_BORROW         6 (current)
                CALL                     1

 432            LOAD_CONST               5 ('reveal_token_invalid')

 429            LOAD_CONST              14 (('status', 'rotation', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 434   L10:     LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         8 (expires_at)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      133 (to L15)
                NOT_TAKEN
                LOAD_FAST_BORROW         8 (expires_at)
                TO_BOOL
                POP_JUMP_IF_FALSE      125 (to L15)
                NOT_TAKEN

 435            NOP

 436   L11:     LOAD_GLOBAL             22 (datetime)
                LOAD_ATTR               24 (fromisoformat)
                PUSH_NULL
                LOAD_FAST_BORROW         8 (expires_at)
                LOAD_ATTR               27 (replace + NULL|self)
                LOAD_CONST              17 ('Z')
                LOAD_CONST              18 ('+00:00')
                CALL                     2
                CALL                     1
                STORE_FAST               9 (exp_dt)

 437            LOAD_FAST_BORROW         9 (exp_dt)
                LOAD_ATTR               28 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L12)
                NOT_TAKEN

 438            LOAD_FAST_BORROW         9 (exp_dt)
                LOAD_ATTR               27 (replace + NULL|self)
                LOAD_GLOBAL             30 (timezone)
                LOAD_ATTR               32 (utc)
                LOAD_CONST              19 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST               9 (exp_dt)

 439   L12:     LOAD_GLOBAL             35 (_now_dt + NULL)
                CALL                     0
                LOAD_FAST_BORROW         9 (exp_dt)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE       24 (to L14)
                NOT_TAKEN

 440            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 441            LOAD_CONST              20 ('reveal_token_expired')

 442            LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST_BORROW         6 (current)
                CALL                     1

 443            LOAD_CONST              20 ('reveal_token_expired')

 440            LOAD_CONST              14 (('status', 'rotation', 'error_code'))
                CALL_KW                  3
       L13:     RETURN_VALUE

 439   L14:     NOP

 452   L15:     NOP

 453   L16:     LOAD_GLOBAL             39 (int + NULL)
                LOAD_FAST_BORROW         6 (current)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              21 ('reveal_attempt_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L19)
       L17:     NOT_TAKEN
       L18:     POP_TOP
                LOAD_SMALL_INT           0
       L19:     CALL                     1
                STORE_FAST              10 (attempts)

 456   L20:     LOAD_FAST_BORROW        10 (attempts)
                LOAD_GLOBAL             44 (_MAX_ATTEMPTS)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       24 (to L21)
                NOT_TAKEN

 457            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 458            LOAD_CONST              22 ('reveal_attempt_limit_exceeded')

 459            LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST_BORROW         6 (current)
                CALL                     1

 460            LOAD_CONST              22 ('reveal_attempt_limit_exceeded')

 457            LOAD_CONST              14 (('status', 'rotation', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 465   L21:     LOAD_GLOBAL             47 (_sha256_hex + NULL)
                LOAD_FAST_BORROW         1 (raw_token)
                CALL                     1
                STORE_FAST              11 (incoming_hash)

 466            LOAD_FAST_BORROW_LOAD_FAST_BORROW 183 (incoming_hash, stored_hash)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       24 (to L22)
                NOT_TAKEN

 467            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 468            LOAD_CONST               5 ('reveal_token_invalid')

 469            LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST_BORROW         6 (current)
                CALL                     1

 470            LOAD_CONST               5 ('reveal_token_invalid')

 467            LOAD_CONST              14 (('status', 'rotation', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 472   L22:     LOAD_GLOBAL              5 (_safe_envelope + NULL)

 473            LOAD_CONST              23 ('ok')

 474            LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST_BORROW         6 (current)
                CALL                     1

 472            LOAD_CONST              24 (('status', 'rotation'))
                CALL_KW                  2
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 445            LOAD_GLOBAL             36 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       27 (to L25)
                NOT_TAKEN
                POP_TOP

 446            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 447            LOAD_CONST               5 ('reveal_token_invalid')

 448            LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST                6 (current)
                CALL                     1

 449            LOAD_CONST               5 ('reveal_token_invalid')

 446            LOAD_CONST              14 (('status', 'rotation', 'error_code'))
                CALL_KW                  3
                SWAP                     2
       L24:     POP_EXCEPT
                RETURN_VALUE

 445   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L27:     PUSH_EXC_INFO

 454            LOAD_GLOBAL             40 (TypeError)
                LOAD_GLOBAL             42 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L29)
                NOT_TAKEN
                POP_TOP

 455            LOAD_SMALL_INT           0
                STORE_FAST              10 (attempts)
       L28:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 157 (to L20)

 454   L29:     RERAISE                  0

  --   L30:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L11 to L13 -> L23 [0]
  L16 to L17 -> L27 [0]
  L18 to L20 -> L27 [0]
  L23 to L24 -> L26 [1] lasti
  L25 to L26 -> L26 [1] lasti
  L27 to L28 -> L30 [1] lasti
  L29 to L30 -> L30 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026030, file "app/services/security/api_key_reveal.py", line 478>:
478           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rotation_id')

480           LOAD_CONST               2 ('str')

478           LOAD_CONST               3 ('success')

481           LOAD_CONST               4 ('bool')

478           LOAD_CONST               5 ('brokerage_id')

482           LOAD_CONST               6 ('Optional[str]')

478           LOAD_CONST               7 ('return')

483           LOAD_CONST               8 ('Dict[str, Any]')

478           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object mark_reveal_attempt at 0x0000018C1778AA50, file "app/services/security/api_key_reveal.py", line 478>:
 478            RESUME                   0

 486            LOAD_GLOBAL              1 (_bound_id + NULL)
                LOAD_FAST_BORROW         0 (rotation_id)
                LOAD_GLOBAL              2 (_ROTATION_ID_MAX_LEN)
                CALL                     2
                STORE_FAST               3 (rid)

 487            LOAD_FAST_BORROW         3 (rid)
                POP_JUMP_IF_NOT_NONE    14 (to L1)
                NOT_TAKEN

 488            LOAD_GLOBAL              5 (_safe_envelope + NULL)
                LOAD_CONST               2 ('failed')
                LOAD_CONST               3 ('invalid_rotation_id')
                LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 489    L1:     LOAD_FAST_BORROW         2 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              7 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         2 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               1 (None)
        L3:     STORE_FAST               4 (bid)

 490            LOAD_GLOBAL              9 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               5 (db)

 491            LOAD_FAST_BORROW         5 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L4)
                NOT_TAKEN

 492            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 493            LOAD_CONST               5 ('skipped')

 494            LOAD_CONST               6 ('api_key_rotation_store_unavailable')
                BUILD_LIST               1

 495            LOAD_CONST               6 ('api_key_rotation_store_unavailable')

 492            LOAD_CONST               7 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 497    L4:     LOAD_GLOBAL             11 (_lookup_rotation + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (db, rid)
                LOAD_FAST_BORROW         4 (bid)
                LOAD_CONST               8 (('rotation_id', 'brokerage_id'))
                CALL_KW                  3
                STORE_FAST               6 (current)

 498            LOAD_FAST_BORROW         6 (current)
                POP_JUMP_IF_NOT_NONE    14 (to L5)
                NOT_TAKEN

 499            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 500            LOAD_CONST               9 ('rotation_not_found')

 501            LOAD_CONST              10 ('rotation_not_found_or_cross_brokerage')

 499            LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 503    L5:     NOP

 504    L6:     LOAD_GLOBAL             13 (int + NULL)
                LOAD_FAST_BORROW         6 (current)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              11 ('reveal_attempt_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
        L7:     NOT_TAKEN
        L8:     POP_TOP
                LOAD_SMALL_INT           0
        L9:     CALL                     1
                STORE_FAST               7 (attempts)

 508   L10:     LOAD_CONST              11 ('reveal_attempt_count')
                LOAD_FAST_BORROW         7 (attempts)
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)

 507            BUILD_MAP                1
                STORE_FAST               8 (patch)

 510            LOAD_FAST_BORROW         1 (success)
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L11)
                NOT_TAKEN
                LOAD_FAST_BORROW         6 (current)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              12 ('revealed_at')
                CALL                     1
                POP_JUMP_IF_NOT_NONE    23 (to L11)
                NOT_TAKEN

 511            LOAD_GLOBAL             21 (_iso + NULL)
                LOAD_GLOBAL             23 (_now_dt + NULL)
                CALL                     0
                CALL                     1
                LOAD_FAST_BORROW         8 (patch)
                LOAD_CONST              12 ('revealed_at')
                STORE_SUBSCR

 512   L11:     NOP

 514   L12:     LOAD_FAST_BORROW         5 (db)
                LOAD_ATTR               25 (table + NULL|self)
                LOAD_GLOBAL             26 (_TABLE)
                CALL                     1

 515            LOAD_ATTR               29 (update + NULL|self)
                LOAD_FAST_BORROW         8 (patch)
                CALL                     1

 516            LOAD_ATTR               31 (eq + NULL|self)
                LOAD_CONST              13 ('rotation_id')
                LOAD_FAST_BORROW         3 (rid)
                CALL                     2

 517            LOAD_ATTR               33 (execute + NULL|self)
                CALL                     0

 513            STORE_FAST               9 (upd)

 519            LOAD_GLOBAL             35 (list + NULL)
                LOAD_GLOBAL             37 (getattr + NULL)
                LOAD_FAST_BORROW         9 (upd)
                LOAD_CONST              14 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
       L13:     NOT_TAKEN
       L14:     POP_TOP
                BUILD_LIST               0
       L15:     CALL                     1
                STORE_FAST              10 (rows_after)

 529   L16:     LOAD_FAST               10 (rows_after)
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L17)
                NOT_TAKEN

 530            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 531            LOAD_CONST               2 ('failed')

 532            LOAD_CONST              17 ('policy_refused_or_no_rows')

 530            LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 534   L17:     LOAD_GLOBAL              5 (_safe_envelope + NULL)

 535            LOAD_CONST              18 ('ok')

 536            LOAD_GLOBAL             49 (_project_row + NULL)
                LOAD_FAST               10 (rows_after)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1

 534            LOAD_CONST              19 (('status', 'rotation'))
                CALL_KW                  2
                RETURN_VALUE

  --   L18:     PUSH_EXC_INFO

 505            LOAD_GLOBAL             16 (TypeError)
                LOAD_GLOBAL             18 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L20)
                NOT_TAKEN
                POP_TOP

 506            LOAD_SMALL_INT           0
                STORE_FAST               7 (attempts)
       L19:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 230 (to L10)

 505   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L22:     PUSH_EXC_INFO

 520            LOAD_GLOBAL             38 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L27)
                NOT_TAKEN
                STORE_FAST              11 (e)

 521   L23:     LOAD_GLOBAL             40 (logger)
                LOAD_ATTR               43 (warning + NULL|self)

 522            LOAD_CONST              15 ('mark_reveal_attempt update error type=')
                LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 521            CALL                     1
                POP_TOP

 524            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 525            LOAD_CONST               5 ('skipped')

 526            LOAD_CONST              16 ('db_write_failed:')
                LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 527            LOAD_CONST               6 ('api_key_rotation_store_unavailable')

 524            LOAD_CONST               7 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
       L24:     SWAP                     2
       L25:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RETURN_VALUE

  --   L26:     LOAD_CONST               1 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 520   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L6 to L7 -> L18 [0]
  L8 to L10 -> L18 [0]
  L12 to L13 -> L22 [0]
  L14 to L16 -> L22 [0]
  L18 to L19 -> L21 [1] lasti
  L20 to L21 -> L21 [1] lasti
  L22 to L23 -> L28 [1] lasti
  L23 to L24 -> L26 [1] lasti
  L24 to L25 -> L28 [1] lasti
  L26 to L28 -> L28 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "app/services/security/api_key_reveal.py", line 544>:
544           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rotation_id')

546           LOAD_CONST               2 ('str')

544           LOAD_CONST               3 ('raw_token')

547           LOAD_CONST               2 ('str')

544           LOAD_CONST               4 ('brokerage_id')

548           LOAD_CONST               5 ('Any')

544           LOAD_CONST               6 ('return')

549           LOAD_CONST               7 ('Dict[str, Any]')

544           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object reveal_rotated_api_key_once at 0x0000018C17F74290, file "app/services/security/api_key_reveal.py", line 544>:
 544            RESUME                   0

 569            LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         2 (brokerage_id)
                CALL                     1
                STORE_FAST               3 (bid)

 570            LOAD_FAST_BORROW         3 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L1)
                NOT_TAKEN

 571            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               2 ('failed')
                LOAD_CONST               3 ('missing_brokerage_id')
                LOAD_CONST               4 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 572    L1:     LOAD_GLOBAL              5 (verify_one_time_reveal_token + NULL)

 573            LOAD_FAST_BORROW         0 (rotation_id)

 574            LOAD_FAST_BORROW         1 (raw_token)

 575            LOAD_FAST_BORROW         3 (bid)

 572            LOAD_CONST               5 (('rotation_id', 'raw_token', 'brokerage_id'))
                CALL_KW                  3
                STORE_FAST               4 (verify)

 577            LOAD_FAST_BORROW         4 (verify)
                LOAD_CONST               6 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               7 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       89 (to L5)
                NOT_TAKEN

 579            NOP

 580    L2:     LOAD_GLOBAL              7 (mark_reveal_attempt + NULL)

 581            LOAD_FAST_BORROW         0 (rotation_id)

 582            LOAD_CONST               8 (False)

 583            LOAD_FAST_BORROW         3 (bid)

 580            LOAD_CONST               9 (('rotation_id', 'success', 'brokerage_id'))
                CALL_KW                  3
                POP_TOP

 587    L3:     LOAD_FAST_BORROW         4 (verify)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              10 ('rotation')
                CALL                     1
                STORE_FAST               5 (rotation)

 588            LOAD_GLOBAL             13 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (rotation)
                LOAD_GLOBAL             14 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       33 (to L4)
                NOT_TAKEN

 589            LOAD_GLOBAL             17 (_audit + NULL)

 590            LOAD_CONST              11 ('reveal_rotated_api_key')

 591            LOAD_FAST_BORROW         5 (rotation)

 592            LOAD_CONST              12 ('FAILED')

 593            LOAD_FAST_BORROW         4 (verify)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              13 ('error_code')
                CALL                     1

 594            LOAD_CONST              14 ('security.api_key_reveal.failed')

 595            LOAD_SMALL_INT           1

 589            LOAD_CONST              15 (('action', 'record', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  6
                POP_TOP

 597    L4:     LOAD_FAST_BORROW         4 (verify)
                RETURN_VALUE

 600    L5:     LOAD_FAST_BORROW         4 (verify)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              10 ('rotation')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L6:     STORE_FAST               5 (rotation)

 604            LOAD_GLOBAL              7 (mark_reveal_attempt + NULL)

 605            LOAD_FAST_BORROW         0 (rotation_id)

 606            LOAD_CONST               8 (False)

 607            LOAD_FAST_BORROW         3 (bid)

 604            LOAD_CONST               9 (('rotation_id', 'success', 'brokerage_id'))
                CALL_KW                  3
                POP_TOP

 609            LOAD_GLOBAL             17 (_audit + NULL)

 610            LOAD_CONST              11 ('reveal_rotated_api_key')

 611            LOAD_FAST_BORROW         5 (rotation)

 612            LOAD_CONST              12 ('FAILED')

 613            LOAD_CONST              16 ('raw_key_reveal_unsupported')

 614            LOAD_CONST              14 ('security.api_key_reveal.failed')

 615            LOAD_SMALL_INT           0

 609            LOAD_CONST              15 (('action', 'record', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  6
                POP_TOP

 617            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 618            LOAD_CONST              17 ('deferred')

 619            LOAD_FAST_BORROW         5 (rotation)

 621            LOAD_CONST               1 (None)

 622            LOAD_CONST              16 ('raw_key_reveal_unsupported')
                BUILD_LIST               1

 623            LOAD_CONST              16 ('raw_key_reveal_unsupported')

 617            LOAD_CONST              18 (('status', 'rotation', 'raw_api_key', 'warnings', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 585            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        4 (to L9)
                NOT_TAKEN
                POP_TOP

 586    L8:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 161 (to L3)

 585    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app/services/security/api_key_reveal.py", line 631>:
631           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rotation_id')

633           LOAD_CONST               2 ('str')

631           LOAD_CONST               3 ('brokerage_id')

634           LOAD_CONST               4 ('Any')

631           LOAD_CONST               5 ('return')

635           LOAD_CONST               6 ('Dict[str, Any]')

631           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object reveal_status at 0x0000018C1801C410, file "app/services/security/api_key_reveal.py", line 631>:
631           RESUME                   0

638           LOAD_GLOBAL              1 (_bound_id + NULL)
              LOAD_FAST_BORROW         0 (rotation_id)
              LOAD_GLOBAL              2 (_ROTATION_ID_MAX_LEN)
              CALL                     2
              STORE_FAST               2 (rid)

639           LOAD_FAST_BORROW         2 (rid)
              POP_JUMP_IF_NOT_NONE    14 (to L1)
              NOT_TAKEN

640           LOAD_GLOBAL              5 (_safe_envelope + NULL)
              LOAD_CONST               1 ('failed')
              LOAD_CONST               2 ('invalid_rotation_id')
              LOAD_CONST               3 (('status', 'error_code'))
              CALL_KW                  2
              RETURN_VALUE

641   L1:     LOAD_GLOBAL              7 (_bound_brokerage_id + NULL)
              LOAD_FAST_BORROW         1 (brokerage_id)
              CALL                     1
              STORE_FAST               3 (bid)

642           LOAD_FAST_BORROW         3 (bid)
              POP_JUMP_IF_NOT_NONE    14 (to L2)
              NOT_TAKEN

643           LOAD_GLOBAL              5 (_safe_envelope + NULL)
              LOAD_CONST               1 ('failed')
              LOAD_CONST               4 ('missing_brokerage_id')
              LOAD_CONST               3 (('status', 'error_code'))
              CALL_KW                  2
              RETURN_VALUE

644   L2:     LOAD_GLOBAL              9 (_get_db_safe + NULL)
              CALL                     0
              STORE_FAST               4 (db)

645           LOAD_FAST_BORROW         4 (db)
              POP_JUMP_IF_NOT_NONE    16 (to L3)
              NOT_TAKEN

646           LOAD_GLOBAL              5 (_safe_envelope + NULL)

647           LOAD_CONST               5 ('skipped')

648           LOAD_CONST               6 ('api_key_rotation_store_unavailable')
              BUILD_LIST               1

649           LOAD_CONST               6 ('api_key_rotation_store_unavailable')

646           LOAD_CONST               7 (('status', 'warnings', 'error_code'))
              CALL_KW                  3
              RETURN_VALUE

651   L3:     LOAD_GLOBAL             11 (_lookup_rotation + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (db, rid)
              LOAD_FAST_BORROW         3 (bid)
              LOAD_CONST               8 (('rotation_id', 'brokerage_id'))
              CALL_KW                  3
              STORE_FAST               5 (current)

652           LOAD_FAST_BORROW         5 (current)
              POP_JUMP_IF_NOT_NONE    14 (to L4)
              NOT_TAKEN

653           LOAD_GLOBAL              5 (_safe_envelope + NULL)

654           LOAD_CONST               9 ('rotation_not_found')

655           LOAD_CONST              10 ('rotation_not_found_or_cross_brokerage')

653           LOAD_CONST               3 (('status', 'error_code'))
              CALL_KW                  2
              RETURN_VALUE

657   L4:     LOAD_GLOBAL              5 (_safe_envelope + NULL)

658           LOAD_CONST              11 ('ok')

659           LOAD_GLOBAL             13 (_project_row + NULL)
              LOAD_FAST_BORROW         5 (current)
              CALL                     1

657           LOAD_CONST              12 (('status', 'rotation'))
              CALL_KW                  2
              RETURN_VALUE
```
