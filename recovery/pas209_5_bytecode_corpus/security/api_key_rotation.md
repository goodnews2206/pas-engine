# security/api_key_rotation

- **pyc:** `app\services\security\__pycache__\api_key_rotation.cpython-314.pyc`
- **expected source path (absent):** `app\services\security/api_key_rotation.py`
- **co_filename (from bytecode):** `app/services/security/api_key_rotation.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** security

## Module docstring

```
PAS-SECURITY-02 — Tenant-initiated / operator-approved API-key
rotation service.

Wraps the v32 ``pas_api_key_rotation_events`` table with the
strict transition table mirroring PAS180's
recommendation_review pattern:

    REQUESTED  → APPROVED   (operator)
    REQUESTED  → CANCELLED  (tenant or operator)
    REQUESTED  → FAILED     (system / operator on validation failure)
    APPROVED   → ROTATED    (operator-driven; requires existing
                              key-generation helper)
    APPROVED   → FAILED     (operator-driven on failure)
    APPROVED   → CANCELLED  (operator-driven)

Doctrine:

* **No raw API keys anywhere.** Fingerprints only —
  ``fingerprint_api_key(key)`` is sha256 hex over the bounded
  key string. The table refuses to store any other
  representation of the key.
* **No raw-key echo.** No public envelope ever carries a key.
  When PAS-SECURITY-02 successfully rotates a key, the new
  raw key is delivered via the **existing secure delivery
  channel** (operator-supplied) — not via the rotation row.
  Without an existing safe delivery channel, the rotation
  helper returns ``status="deferred"`` and the row stays in
  ``APPROVED`` for operator follow-up.
* **NEVER raises.** All failures return structural envelopes.
* **No exception text in public envelopes.** All errors use
  closed structural ``error_code`` tokens.
* **Append-only audit trail.** Every transition writes a
  PAS174 audit row via ``log_operator_action``.

Public surface:

  * ``ALLOWED_ROTATION_STATUSES``                      — closed enum.
  * ``ALLOWED_ACTOR_TYPES``                            — closed enum.
  * ``ALLOWED_TRANSITIONS``                            — closed map.
  * ``fingerprint_api_key(key)``                       — sha256 hex.
  * ``request_api_key_rotation(...)``                  — tenant entry.
  * ``approve_api_key_rotation(...)``                  — operator approve.
  * ``cancel_api_key_rotation(...)``                   — tenant or operator.
  * ``fail_api_key_rotation(...)``                     — operator / system.
  * ``rotate_api_key_if_helper_available(...)``        — operator commit.
  * ``api_key_rotation_status(brokerage_id, rotation_id)`` — read.
  * ``list_api_key_rotation_events(brokerage_id, ...)`` — bounded read.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `app.db.supabase_client`, `app.services.operator.audit_service`, `datetime`, `get_supabase`, `hashlib`, `log_operator_action`, `logging`, `timezone`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_audit`, `_bound_actor_id`, `_bound_brokerage_id`, `_bound_id`, `_get_db_safe`, `_iso`, `_lookup_rotation`, `_now_dt`, `_project_metadata`, `_project_row`, `_safe_envelope`, `_transition`, `_validate_transition`, `api_key_rotation_status`, `approve_api_key_rotation`, `cancel_api_key_rotation`, `fail_api_key_rotation`, `fingerprint_api_key`, `list_api_key_rotation_events`, `request_api_key_rotation`, `rotate_api_key_if_helper_available`

## Env-key candidates

`ALLOWED_ACTOR_TYPES`, `ALLOWED_ROTATION_METADATA_KEYS`, `ALLOWED_ROTATION_STATUSES`, `ALLOWED_TRANSITIONS`, `APPROVED`, `CANCELLED`, `FAILED`, `OPERATOR`, `REQUESTED`, `ROTATED`, `SUCCESS`, `TENANT`

## String constants (redacted where noted)

- '\nPAS-SECURITY-02 — Tenant-initiated / operator-approved API-key\nrotation service.\n\nWraps the v32 ``pas_api_key_rotation_events`` table with the\nstrict transition table mirroring PAS180\'s\nrecommendation_review pattern:\n\n    REQUESTED  → APPROVED   (operator)\n    REQUESTED  → CANCELLED  (tenant or operator)\n    REQUESTED  → FAILED     (system / operator on validation failure)\n    APPROVED   → ROTATED    (operator-driven; requires existing\n                              key-generation helper)\n    APPROVED   → FAILED     (operator-driven on failure)\n    APPROVED   → CANCELLED  (operator-driven)\n\nDoctrine:\n\n* **No raw API keys anywhere.** Fingerprints only —\n  ``fingerprint_api_key(key)`` is sha256 hex over the bounded\n  key string. The table refuses to store any other\n  representation of the key.\n* **No raw-key echo.** No public envelope ever carries a key.\n  When PAS-SECURITY-02 successfully rotates a key, the new\n  raw key is delivered via the **existing secure delivery\n  channel** (operator-supplied) — not via the rotation row.\n  Without an existing safe delivery channel, the rotation\n  helper returns ``status="deferred"`` and the row stays in\n  ``APPROVED`` for operator follow-up.\n* **NEVER raises.** All failures return structural envelopes.\n* **No exception text in public envelopes.** All errors use\n  closed structural ``error_code`` tokens.\n* **Append-only audit trail.** Every transition writes a\n  PAS174 audit row via ``log_operator_action``.\n\nPublic surface:\n\n  * ``ALLOWED_ROTATION_STATUSES``                      — closed enum.\n  * ``ALLOWED_ACTOR_TYPES``                            — closed enum.\n  * ``ALLOWED_TRANSITIONS``                            — closed map.\n  * ``fingerprint_api_key(key)``                       — sha256 hex.\n  * ``request_api_key_rotation(...)``                  — tenant entry.\n  * ``approve_api_key_rotation(...)``                  — operator approve.\n  * ``cancel_api_key_rotation(...)``                   — tenant or operator.\n  * ``fail_api_key_rotation(...)``                     — operator / system.\n  * ``rotate_api_key_if_helper_available(...)``        — operator commit.\n  * ``api_key_rotation_status(brokerage_id, rotation_id)`` — read.\n  * ``list_api_key_rotation_events(brokerage_id, ...)`` — bounded read.\n'
- 'pas.security.api_key_rotation'
- 'pas_api_key_rotation_events'
- 'REQUESTED'
- 'APPROVED'
- 'Tuple[str, ...]'
- 'ALLOWED_ROTATION_STATUSES'
- 'TENANT'
- 'OPERATOR'
- 'ALLOWED_ACTOR_TYPES'
- 'Dict[str, Tuple[str, ...]]'
- 'ALLOWED_TRANSITIONS'
- 'event'
- 'warning_count'
- 'error_code'
- 'ALLOWED_ROTATION_METADATA_KEYS'
- 🔒 '<REDACTED:high-entropy blob, len=64>'
- 'rotation_id'
- 'actor_type'
- 'actor_id'
- 'status'
- 'record'
- 'transition'
- 'audit_row'
- 'warnings'
- 'target_status'
- 'audit_status'
- 'SUCCESS'
- 'previous_api_key'
- 'security.api_key_rotation.event'
- 'extra_patch'
- 'new_api_key'
- 'limit'
- 'return'
- 'datetime'
- 'str'
- 'seconds'
- 'api_key_rotation db client unavailable type='
- 'value'
- 'Any'
- 'Optional[str]'
- 'max_len'
- 'int'
- 'key'
- 'sha256 hex fingerprint of an API key. NEVER returns\nthe key itself. Returns None for malformed input.'
- 'utf-8'
- 'fingerprint_api_key error type='
- 'metadata'
- 'Dict[str, Any]'
- 'row'
- 'Optional[Dict[str, Any]]'
- 'Optional[List[str]]'
- 'from_status'
- 'to_status'
- 'invalid_target_status'
- 'walk_back_to_requested_forbidden'
- 'missing_current_status'
- 'invalid_transition'
- 'action'
- 'Best-effort PAS174 audit row. NEVER raises.'
- 'brokerage_id'
- 'FAILED'
- 'api_key_rotation_event'
- '_audit api_key_rotation error type='
- 'data'
- '_lookup_rotation error type='
- 'Tenant entry point. Inserts a REQUESTED row with the\nprevious-key fingerprint. NEVER stores the raw key.\nNEVER raises.'
- 'failed'
- 'invalid_actor_type'
- 'invalid_actor_id'
- 'missing_brokerage_id'
- 'invalid_previous_api_key'
- 'skipped'
- 'api_key_rotation_store_unavailable'
- 'requested_at'
- 'previous_key_fingerprint'
- 'new_key_fingerprint'
- 'effective_at'
- 'security.api_key_rotation.requested'
- 'operator_command'
- 'request_api_key_rotation'
- 'request_api_key_rotation insert error type='
- 'db_write_failed:'
- 'from'
- 'Generic transition core. NEVER raises.'
- 'invalid_rotation_id'
- 'rotation_not_found'
- 'transition_api_key_rotation_'
- 'security.api_key_rotation.failed'
- 'transition_to_'
- '_transition update error type='
- 'policy_refused_or_no_rows'
- 'Operator approval. Transitions REQUESTED → APPROVED.\nActor MUST be OPERATOR or ADMIN. NEVER raises.'
- 'security.api_key_rotation.approved'
- 'Cancel a REQUESTED / APPROVED rotation. Tenant OR\noperator may call. NEVER raises.'
- 'CANCELLED'
- 'Operator-driven failure transition for a REQUESTED or\nAPPROVED rotation. NEVER raises.'
- 'Operator-driven commit step. Transitions APPROVED →\nROTATED. NEVER echoes the raw key.\n\nBehaviour:\n  * If ``new_api_key`` is provided, its sha256 fingerprint\n    is recorded and the row transitions to ROTATED. The\n    actual key delivery is the operator\'s responsibility\n    (secure existing channel) — the row never carries\n    the raw key.\n  * If ``new_api_key`` is None, the row stays in APPROVED\n    and the envelope reports ``status="deferred"``. PAS-\n    SECURITY-02 does NOT generate a new API key itself\n    because PAS lacks a vetted secure-delivery channel\n    for the raw key. Operators promote a separate\n    rotation surface (e.g. PAS175\'s\n    ``rotate_brokerage_api_key`` action) and supply the\n    generated key here.\n\nNEVER raises.\n'
- 'deferred'
- 'api_key_delivery_channel_unavailable'
- 'invalid_new_api_key'
- 'ROTATED'
- 'security.api_key_rotation.completed'
- 'Read either a single rotation row (when rotation_id is\ngiven) or the most-recent rotation row for the brokerage.\nNEVER raises. NEVER returns a raw key.'
- 'api_key_rotation_status read error type='
- 'db_read_failed:'
- 'rotation_not_found_or_cross_brokerage'
- 'rows'
- 'count'
- 'invalid_status'
- 'list_api_key_rotation_events read error type='

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS-SECURITY-02 — Tenant-initiated / operator-approved API-key\nrotation service.\n\nWraps the v32 ``pas_api_key_rotation_events`` table with the\nstrict transition table mirroring PAS180\'s\nrecommendation_review pattern:\n\n    REQUESTED  → APPROVED   (operator)\n    REQUESTED  → CANCELLED  (tenant or operator)\n    REQUESTED  → FAILED     (system / operator on validation failure)\n    APPROVED   → ROTATED    (operator-driven; requires existing\n                              key-generation helper)\n    APPROVED   → FAILED     (operator-driven on failure)\n    APPROVED   → CANCELLED  (operator-driven)\n\nDoctrine:\n\n* **No raw API keys anywhere.** Fingerprints only —\n  ``fingerprint_api_key(key)`` is sha256 hex over the bounded\n  key string. The table refuses to store any other\n  representation of the key.\n* **No raw-key echo.** No public envelope ever carries a key.\n  When PAS-SECURITY-02 successfully rotates a key, the new\n  raw key is delivered via the **existing secure delivery\n  channel** (operator-supplied) — not via the rotation row.\n  Without an existing safe delivery channel, the rotation\n  helper returns ``status="deferred"`` and the row stays in\n  ``APPROVED`` for operator follow-up.\n* **NEVER raises.** All failures return structural envelopes.\n* **No exception text in public envelopes.** All errors use\n  closed structural ``error_code`` tokens.\n* **Append-only audit trail.** Every transition writes a\n  PAS174 audit row via ``log_operator_action``.\n\nPublic surface:\n\n  * ``ALLOWED_ROTATION_STATUSES``                      — closed enum.\n  * ``ALLOWED_ACTOR_TYPES``                            — closed enum.\n  * ``ALLOWED_TRANSITIONS``                            — closed map.\n  * ``fingerprint_api_key(key)``                       — sha256 hex.\n  * ``request_api_key_rotation(...)``                  — tenant entry.\n  * ``approve_api_key_rotation(...)``                  — operator approve.\n  * ``cancel_api_key_rotation(...)``                   — tenant or operator.\n  * ``fail_api_key_rotation(...)``                     — operator / system.\n  * ``rotate_api_key_if_helper_available(...)``        — operator commit.\n  * ``api_key_rotation_status(brokerage_id, rotation_id)`` — read.\n  * ``list_api_key_rotation_events(brokerage_id, ...)`` — bounded read.\n')
               STORE_NAME               1 (__doc__)

  51           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  53           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (hashlib)
               STORE_NAME               4 (hashlib)

  54           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (logging)
               STORE_NAME               5 (logging)

  55           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (uuid)
               STORE_NAME               6 (uuid)

  56           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  57           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME              9 (typing)
               IMPORT_FROM             10 (Any)
               STORE_NAME              10 (Any)
               IMPORT_FROM             11 (Dict)
               STORE_NAME              11 (Dict)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               IMPORT_FROM             14 (Tuple)
               STORE_NAME              14 (Tuple)
               POP_TOP

  60           LOAD_NAME                5 (logging)
               LOAD_ATTR               30 (getLogger)
               PUSH_NULL
               LOAD_CONST               5 ('pas.security.api_key_rotation')
               CALL                     1
               STORE_NAME              16 (logger)

  63           LOAD_CONST               6 ('pas_api_key_rotation_events')
               STORE_NAME              17 (_TABLE)

  67           LOAD_CONST              80 (('REQUESTED', 'APPROVED', 'ROTATED', 'FAILED', 'CANCELLED'))
               STORE_NAME              18 (ALLOWED_ROTATION_STATUSES)
               LOAD_CONST               9 ('Tuple[str, ...]')
               LOAD_NAME               19 (__annotations__)
               LOAD_CONST              10 ('ALLOWED_ROTATION_STATUSES')
               STORE_SUBSCR

  71           LOAD_CONST              81 (('TENANT', 'OPERATOR', 'ADMIN', 'SYSTEM'))
               STORE_NAME              20 (ALLOWED_ACTOR_TYPES)
               LOAD_CONST               9 ('Tuple[str, ...]')
               LOAD_NAME               19 (__annotations__)
               LOAD_CONST              13 ('ALLOWED_ACTOR_TYPES')
               STORE_SUBSCR

  78           LOAD_CONST               7 ('REQUESTED')
               LOAD_CONST              82 (('APPROVED', 'CANCELLED', 'FAILED'))

  79           LOAD_CONST               8 ('APPROVED')
               LOAD_CONST              83 (('ROTATED', 'FAILED', 'CANCELLED'))

  77           BUILD_MAP                2
               STORE_NAME              21 (ALLOWED_TRANSITIONS)
               LOAD_CONST              14 ('Dict[str, Tuple[str, ...]]')
               LOAD_NAME               19 (__annotations__)
               LOAD_CONST              15 ('ALLOWED_TRANSITIONS')
               STORE_SUBSCR

  84           LOAD_CONST              84 (('event', 'previous_key_fingerprint', 'new_key_fingerprint', 'warning_count', 'error_code', 'operator_command'))
               STORE_NAME              22 (ALLOWED_ROTATION_METADATA_KEYS)
               LOAD_CONST               9 ('Tuple[str, ...]')
               LOAD_NAME               19 (__annotations__)
               LOAD_CONST              19 ('ALLOWED_ROTATION_METADATA_KEYS')
               STORE_SUBSCR

  95           LOAD_SMALL_INT         200
               STORE_NAME              23 (_BROKERAGE_ID_MAX_LEN)

  96           LOAD_SMALL_INT         200
               STORE_NAME              24 (_ACTOR_ID_MAX_LEN)

  97           LOAD_SMALL_INT         200
               STORE_NAME              25 (_ROTATION_ID_MAX_LEN)

  98           LOAD_CONST              20 (1024)
               STORE_NAME              26 (_API_KEY_MAX_LEN)

  99           LOAD_CONST              21 (500)
               STORE_NAME              27 (_LIST_HARD_CAP)

 100           LOAD_SMALL_INT          50
               STORE_NAME              28 (_DEFAULT_LIMIT)

 103           LOAD_CONST              22 ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_')

 102           STORE_NAME              29 (_ALLOWED_TOKEN_CHARS)

 110           LOAD_CONST              85 (('rotation_id', 'brokerage_id', 'requested_at', 'actor_type', 'actor_id', 'status', 'previous_key_fingerprint', 'new_key_fingerprint', 'effective_at', 'warning_count', 'metadata'))
               STORE_NAME              30 (_STRUCTURAL_COLUMNS)

 129           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA2F10, file "app/services/security/api_key_rotation.py", line 129>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object _now_dt at 0x0000018C18053E10, file "app/services/security/api_key_rotation.py", line 129>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_now_dt)

 133           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA3E10, file "app/services/security/api_key_rotation.py", line 133>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object _iso at 0x0000018C18024C30, file "app/services/security/api_key_rotation.py", line 133>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_iso)

 137           LOAD_CONST              31 (<code object _get_db_safe at 0x0000018C17FF13B0, file "app/services/security/api_key_rotation.py", line 137>)
               MAKE_FUNCTION
               STORE_NAME              33 (_get_db_safe)

 149           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA3A50, file "app/services/security/api_key_rotation.py", line 149>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object _bound_brokerage_id at 0x0000018C17F96140, file "app/services/security/api_key_rotation.py", line 149>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_bound_brokerage_id)

 158           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C18025F30, file "app/services/security/api_key_rotation.py", line 158>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object _bound_id at 0x0000018C17FA92F0, file "app/services/security/api_key_rotation.py", line 158>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (_bound_id)

 170           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA3F00, file "app/services/security/api_key_rotation.py", line 170>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object _bound_actor_id at 0x0000018C18026630, file "app/services/security/api_key_rotation.py", line 170>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              36 (_bound_actor_id)

 174           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA3960, file "app/services/security/api_key_rotation.py", line 174>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object fingerprint_api_key at 0x0000018C17D85FD0, file "app/services/security/api_key_rotation.py", line 174>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              37 (fingerprint_api_key)

 191           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA32D0, file "app/services/security/api_key_rotation.py", line 191>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object _project_metadata at 0x0000018C17FEDC30, file "app/services/security/api_key_rotation.py", line 191>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (_project_metadata)

 206           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA3C30, file "app/services/security/api_key_rotation.py", line 206>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object _project_row at 0x0000018C1804D3B0, file "app/services/security/api_key_rotation.py", line 206>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              39 (_project_row)

 217           LOAD_CONST              44 ('record')

 220           LOAD_CONST               2 (None)

 217           LOAD_CONST              45 ('transition')

 221           LOAD_CONST               2 (None)

 217           LOAD_CONST              46 ('audit_row')

 222           LOAD_CONST               2 (None)

 217           LOAD_CONST              47 ('warnings')

 223           LOAD_CONST               2 (None)

 217           LOAD_CONST              18 ('error_code')

 224           LOAD_CONST               2 (None)

 217           BUILD_MAP                5
               LOAD_CONST              48 (<code object __annotate__ at 0x0000018C1812C140, file "app/services/security/api_key_rotation.py", line 217>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object _safe_envelope at 0x0000018C18053990, file "app/services/security/api_key_rotation.py", line 217>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              40 (_safe_envelope)

 236           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C18024E30, file "app/services/security/api_key_rotation.py", line 236>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object _validate_transition at 0x0000018C17FE1290, file "app/services/security/api_key_rotation.py", line 236>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (_validate_transition)

 254           LOAD_CONST              52 ('target_status')

 258           LOAD_CONST               2 (None)

 254           LOAD_CONST              24 ('actor_type')

 259           LOAD_CONST              12 ('OPERATOR')

 254           LOAD_CONST              25 ('actor_id')

 260           LOAD_CONST               2 (None)

 254           LOAD_CONST              53 ('audit_status')

 261           LOAD_CONST              54 ('SUCCESS')

 254           LOAD_CONST              18 ('error_code')

 262           LOAD_CONST               2 (None)

 254           LOAD_CONST              16 ('event')

 263           LOAD_CONST               2 (None)

 254           LOAD_CONST              17 ('warning_count')

 264           LOAD_SMALL_INT           0

 254           BUILD_MAP                7
               LOAD_CONST              55 (<code object __annotate__ at 0x0000018C1812C250, file "app/services/security/api_key_rotation.py", line 254>)
               MAKE_FUNCTION
               LOAD_CONST              56 (<code object _audit at 0x0000018C17F003E0, file "app/services/security/api_key_rotation.py", line 254>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              42 (_audit)

 295           LOAD_CONST              57 (<code object __annotate__ at 0x0000018C18025A30, file "app/services/security/api_key_rotation.py", line 295>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object _lookup_rotation at 0x0000018C17CD4970, file "app/services/security/api_key_rotation.py", line 295>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_lookup_rotation)

 323           LOAD_CONST              24 ('actor_type')

 326           LOAD_CONST              11 ('TENANT')

 323           LOAD_CONST              25 ('actor_id')

 327           LOAD_CONST               2 (None)

 323           LOAD_CONST              59 ('previous_api_key')

 328           LOAD_CONST               2 (None)

 323           BUILD_MAP                3
               LOAD_CONST              60 (<code object __annotate__ at 0x0000018C18025230, file "app/services/security/api_key_rotation.py", line 323>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object request_api_key_rotation at 0x0000018C17D8BD40, file "app/services/security/api_key_rotation.py", line 323>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              44 (request_api_key_rotation)

 408           LOAD_CONST              25 ('actor_id')

 413           LOAD_CONST               2 (None)

 408           LOAD_CONST              16 ('event')

 414           LOAD_CONST              62 ('security.api_key_rotation.event')

 408           LOAD_CONST              63 ('extra_patch')

 415           LOAD_CONST               2 (None)

 408           LOAD_CONST              18 ('error_code')

 416           LOAD_CONST               2 (None)

 408           BUILD_MAP                4
               LOAD_CONST              64 (<code object __annotate__ at 0x0000018C1812C360, file "app/services/security/api_key_rotation.py", line 408>)
               MAKE_FUNCTION
               LOAD_CONST              65 (<code object _transition at 0x0000018C182F65F0, file "app/services/security/api_key_rotation.py", line 408>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              45 (_transition)

 533           LOAD_CONST              24 ('actor_type')

 536           LOAD_CONST              12 ('OPERATOR')

 533           LOAD_CONST              25 ('actor_id')

 537           LOAD_CONST               2 (None)

 533           BUILD_MAP                2
               LOAD_CONST              66 (<code object __annotate__ at 0x0000018C18025730, file "app/services/security/api_key_rotation.py", line 533>)
               MAKE_FUNCTION
               LOAD_CONST              67 (<code object approve_api_key_rotation at 0x0000018C18053750, file "app/services/security/api_key_rotation.py", line 533>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              46 (approve_api_key_rotation)

 552           LOAD_CONST              24 ('actor_type')

 555           LOAD_CONST              12 ('OPERATOR')

 552           LOAD_CONST              25 ('actor_id')

 556           LOAD_CONST               2 (None)

 552           BUILD_MAP                2
               LOAD_CONST              68 (<code object __annotate__ at 0x0000018C18025E30, file "app/services/security/api_key_rotation.py", line 552>)
               MAKE_FUNCTION
               LOAD_CONST              69 (<code object cancel_api_key_rotation at 0x0000018C1802CE70, file "app/services/security/api_key_rotation.py", line 552>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              47 (cancel_api_key_rotation)

 571           LOAD_CONST              24 ('actor_type')

 574           LOAD_CONST              12 ('OPERATOR')

 571           LOAD_CONST              25 ('actor_id')

 575           LOAD_CONST               2 (None)

 571           LOAD_CONST              18 ('error_code')

 576           LOAD_CONST               2 (None)

 571           BUILD_MAP                3
               LOAD_CONST              70 (<code object __annotate__ at 0x0000018C18026530, file "app/services/security/api_key_rotation.py", line 571>)
               MAKE_FUNCTION
               LOAD_CONST              71 (<code object fail_api_key_rotation at 0x0000018C180532D0, file "app/services/security/api_key_rotation.py", line 571>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              48 (fail_api_key_rotation)

 592           LOAD_CONST              72 ('new_api_key')

 595           LOAD_CONST               2 (None)

 592           LOAD_CONST              24 ('actor_type')

 596           LOAD_CONST              12 ('OPERATOR')

 592           LOAD_CONST              25 ('actor_id')

 597           LOAD_CONST               2 (None)

 592           BUILD_MAP                3
               LOAD_CONST              73 (<code object __annotate__ at 0x0000018C18026330, file "app/services/security/api_key_rotation.py", line 592>)
               MAKE_FUNCTION
               LOAD_CONST              74 (<code object rotate_api_key_if_helper_available at 0x0000018C17D77E00, file "app/services/security/api_key_rotation.py", line 592>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              49 (rotate_api_key_if_helper_available)

 657           LOAD_CONST              23 ('rotation_id')

 660           LOAD_CONST               2 (None)

 657           BUILD_MAP                1
               LOAD_CONST              75 (<code object __annotate__ at 0x0000018C18025930, file "app/services/security/api_key_rotation.py", line 657>)
               MAKE_FUNCTION
               LOAD_CONST              76 (<code object api_key_rotation_status at 0x0000018C1778B3F0, file "app/services/security/api_key_rotation.py", line 657>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              50 (api_key_rotation_status)

 734           LOAD_CONST              26 ('status')

 737           LOAD_CONST               2 (None)

 734           LOAD_CONST              77 ('limit')

 738           LOAD_NAME               28 (_DEFAULT_LIMIT)

 734           BUILD_MAP                2
               LOAD_CONST              78 (<code object __annotate__ at 0x0000018C18025B30, file "app/services/security/api_key_rotation.py", line 734>)
               MAKE_FUNCTION
               LOAD_CONST              79 (<code object list_api_key_rotation_events at 0x0000018C18300120, file "app/services/security/api_key_rotation.py", line 734>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              51 (list_api_key_rotation_events)

 804           BUILD_LIST               0
               LOAD_CONST              86 (('ALLOWED_ROTATION_STATUSES', 'ALLOWED_ACTOR_TYPES', 'ALLOWED_TRANSITIONS', 'ALLOWED_ROTATION_METADATA_KEYS', 'fingerprint_api_key', 'request_api_key_rotation', 'approve_api_key_rotation', 'cancel_api_key_rotation', 'fail_api_key_rotation', 'rotate_api_key_if_helper_available', 'api_key_rotation_status', 'list_api_key_rotation_events'))
               LIST_EXTEND              1
               STORE_NAME              52 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "app/services/security/api_key_rotation.py", line 129>:
129           RESUME                   0
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

Disassembly of <code object _now_dt at 0x0000018C18053E10, file "app/services/security/api_key_rotation.py", line 129>:
129           RESUME                   0

130           LOAD_GLOBAL              0 (datetime)
              LOAD_ATTR                2 (now)
              PUSH_NULL
              LOAD_GLOBAL              4 (timezone)
              LOAD_ATTR                6 (utc)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "app/services/security/api_key_rotation.py", line 133>:
133           RESUME                   0
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

Disassembly of <code object _iso at 0x0000018C18024C30, file "app/services/security/api_key_rotation.py", line 133>:
133           RESUME                   0

134           LOAD_FAST_BORROW         0 (dt)
              LOAD_ATTR                1 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object _get_db_safe at 0x0000018C17FF13B0, file "app/services/security/api_key_rotation.py", line 137>:
 137           RESUME                   0

 138           NOP

 139   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 140           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 141           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 142   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 143           LOAD_CONST               2 ('api_key_rotation db client unavailable type=')

 144           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 143           BUILD_STRING             2

 142           CALL                     1
               POP_TOP

 146   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 141   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app/services/security/api_key_rotation.py", line 149>:
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

Disassembly of <code object _bound_brokerage_id at 0x0000018C17F96140, file "app/services/security/api_key_rotation.py", line 149>:
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
              LOAD_GLOBAL              8 (_BROKERAGE_ID_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

154   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

155   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "app/services/security/api_key_rotation.py", line 158>:
158           RESUME                   0
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

Disassembly of <code object _bound_id at 0x0000018C17FA92F0, file "app/services/security/api_key_rotation.py", line 158>:
158           RESUME                   0

159           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

160           LOAD_CONST               0 (None)
              RETURN_VALUE

161   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (s)

162           LOAD_FAST_BORROW         2 (s)
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

163   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

164   L3:     LOAD_FAST_BORROW         2 (s)
              GET_ITER
      L4:     FOR_ITER                17 (to L6)
              STORE_FAST               3 (ch)

165           LOAD_FAST_BORROW         3 (ch)
              LOAD_GLOBAL              8 (_ALLOWED_TOKEN_CHARS)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           16 (to L4)

166   L5:     POP_TOP
              LOAD_CONST               0 (None)
              RETURN_VALUE

164   L6:     END_FOR
              POP_ITER

167           LOAD_FAST_BORROW         2 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "app/services/security/api_key_rotation.py", line 170>:
170           RESUME                   0
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

Disassembly of <code object _bound_actor_id at 0x0000018C18026630, file "app/services/security/api_key_rotation.py", line 170>:
170           RESUME                   0

171           LOAD_GLOBAL              1 (_bound_id + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (_ACTOR_ID_MAX_LEN)
              CALL                     2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app/services/security/api_key_rotation.py", line 174>:
174           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('key')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object fingerprint_api_key at 0x0000018C17D85FD0, file "app/services/security/api_key_rotation.py", line 174>:
 174            RESUME                   0

 177            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (key)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 178            LOAD_CONST               1 (None)
                RETURN_VALUE

 179    L1:     LOAD_FAST_BORROW         0 (key)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               1 (s)

 180            LOAD_FAST_BORROW         1 (s)
                TO_BOOL
                POP_JUMP_IF_FALSE       21 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              7 (len + NULL)
                LOAD_FAST_BORROW         1 (s)
                CALL                     1
                LOAD_GLOBAL              8 (_API_KEY_MAX_LEN)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN

 181    L2:     LOAD_CONST               1 (None)
                RETURN_VALUE

 182    L3:     NOP

 183    L4:     LOAD_GLOBAL             10 (hashlib)
                LOAD_ATTR               12 (sha256)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (s)
                LOAD_ATTR               15 (encode + NULL|self)
                LOAD_CONST               2 ('utf-8')
                CALL                     1
                CALL                     1
                LOAD_ATTR               17 (hexdigest + NULL|self)
                CALL                     0
        L5:     RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 184            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L10)
                NOT_TAKEN
                STORE_FAST               2 (e)

 185    L7:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 186            LOAD_CONST               3 ('fingerprint_api_key error type=')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                2 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 185            CALL                     1
                POP_TOP

 188    L8:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                LOAD_CONST               1 (None)
                RETURN_VALUE

  --    L9:     LOAD_CONST               1 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                RERAISE                  1

 184   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L6 [0]
  L6 to L7 -> L11 [1] lasti
  L7 to L8 -> L9 [1] lasti
  L9 to L11 -> L11 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "app/services/security/api_key_rotation.py", line 191>:
191           RESUME                   0
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

Disassembly of <code object _project_metadata at 0x0000018C17FEDC30, file "app/services/security/api_key_rotation.py", line 191>:
191           RESUME                   0

192           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (metadata)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

193           BUILD_MAP                0
              RETURN_VALUE

194   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

195           LOAD_GLOBAL              4 (ALLOWED_ROTATION_METADATA_KEYS)
              GET_ITER
      L2:     FOR_ITER               108 (to L8)
              STORE_FAST               2 (k)

196           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, metadata)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

197           JUMP_BACKWARD           11 (to L2)

198   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (metadata, k)
              BINARY_OP               26 ([])
              STORE_FAST               3 (v)

199           LOAD_FAST_BORROW         3 (v)
              POP_JUMP_IF_NONE        34 (to L4)
              NOT_TAKEN
              LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (v)
              LOAD_GLOBAL              6 (bool)
              LOAD_GLOBAL              8 (int)
              LOAD_GLOBAL             10 (float)
              BUILD_TUPLE              3
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        7 (to L5)
              NOT_TAKEN

200   L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD           62 (to L2)

201   L5:     LOAD_GLOBAL              1 (isinstance + NULL)
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

202   L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD          110 (to L2)

195   L8:     END_FOR
              POP_ITER

203           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app/services/security/api_key_rotation.py", line 206>:
206           RESUME                   0
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

Disassembly of <code object _project_row at 0x0000018C1804D3B0, file "app/services/security/api_key_rotation.py", line 206>:
206           RESUME                   0

207           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

208           LOAD_CONST               0 (None)
              RETURN_VALUE

209   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

210           LOAD_GLOBAL              4 (_STRUCTURAL_COLUMNS)
              GET_ITER
      L2:     FOR_ITER                21 (to L4)
              STORE_FAST               2 (col)

211           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (col, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

212   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, col)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, col)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L2)

210   L4:     END_FOR
              POP_ITER

213           LOAD_GLOBAL              7 (_project_metadata + NULL)
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

214           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C1812C140, file "app/services/security/api_key_rotation.py", line 217>:
217           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

219           LOAD_CONST               2 ('str')

217           LOAD_CONST               3 ('record')

220           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

217           LOAD_CONST               5 ('transition')

221           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

217           LOAD_CONST               6 ('audit_row')

222           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

217           LOAD_CONST               7 ('warnings')

223           LOAD_CONST               8 ('Optional[List[str]]')

217           LOAD_CONST               9 ('error_code')

224           LOAD_CONST              10 ('Optional[str]')

217           LOAD_CONST              11 ('return')

225           LOAD_CONST              12 ('Dict[str, Any]')

217           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C18053990, file "app/services/security/api_key_rotation.py", line 217>:
217           RESUME                   0

227           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

228           LOAD_CONST               1 ('record')
              LOAD_FAST                1 (record)

229           LOAD_CONST               2 ('transition')
              LOAD_FAST                2 (transition)

230           LOAD_CONST               3 ('audit_row')
              LOAD_FAST                3 (audit_row)

231           LOAD_CONST               4 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                4 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

232           LOAD_CONST               5 ('error_code')
              LOAD_FAST_BORROW         5 (error_code)

226           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app/services/security/api_key_rotation.py", line 236>:
236           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('from_status')

238           LOAD_CONST               2 ('Optional[str]')

236           LOAD_CONST               3 ('to_status')

239           LOAD_CONST               4 ('str')

236           LOAD_CONST               5 ('return')

240           LOAD_CONST               2 ('Optional[str]')

236           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _validate_transition at 0x0000018C17FE1290, file "app/services/security/api_key_rotation.py", line 236>:
236           RESUME                   0

241           LOAD_FAST_BORROW         1 (to_status)
              LOAD_GLOBAL              0 (ALLOWED_ROTATION_STATUSES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

242           LOAD_CONST               0 ('invalid_target_status')
              RETURN_VALUE

243   L1:     LOAD_FAST_BORROW         1 (to_status)
              LOAD_CONST               1 ('REQUESTED')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

244           LOAD_CONST               2 ('walk_back_to_requested_forbidden')
              RETURN_VALUE

245   L2:     LOAD_FAST_BORROW         0 (from_status)
              POP_JUMP_IF_NOT_NONE     3 (to L3)
              NOT_TAKEN

246           LOAD_CONST               4 ('missing_current_status')
              RETURN_VALUE

247   L3:     LOAD_FAST_BORROW         0 (from_status)
              LOAD_GLOBAL              2 (ALLOWED_TRANSITIONS)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN

248           LOAD_CONST               5 ('invalid_transition')
              RETURN_VALUE

249   L4:     LOAD_FAST_BORROW         1 (to_status)
              LOAD_GLOBAL              2 (ALLOWED_TRANSITIONS)
              LOAD_FAST_BORROW         0 (from_status)
              BINARY_OP               26 ([])
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN

250           LOAD_CONST               5 ('invalid_transition')
              RETURN_VALUE

251   L5:     LOAD_CONST               3 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C1812C250, file "app/services/security/api_key_rotation.py", line 254>:
254           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record')

256           LOAD_CONST               2 ('Dict[str, Any]')

254           LOAD_CONST               3 ('action')

257           LOAD_CONST               4 ('str')

254           LOAD_CONST               5 ('target_status')

258           LOAD_CONST               6 ('Optional[str]')

254           LOAD_CONST               7 ('actor_type')

259           LOAD_CONST               4 ('str')

254           LOAD_CONST               8 ('actor_id')

260           LOAD_CONST               6 ('Optional[str]')

254           LOAD_CONST               9 ('audit_status')

261           LOAD_CONST               4 ('str')

254           LOAD_CONST              10 ('error_code')

262           LOAD_CONST               6 ('Optional[str]')

254           LOAD_CONST              11 ('event')

263           LOAD_CONST               6 ('Optional[str]')

254           LOAD_CONST              12 ('warning_count')

264           LOAD_CONST              13 ('int')

254           LOAD_CONST              14 ('return')

265           LOAD_CONST              15 ('Optional[Dict[str, Any]]')

254           BUILD_MAP               10
              RETURN_VALUE

Disassembly of <code object _audit at 0x0000018C17F003E0, file "app/services/security/api_key_rotation.py", line 254>:
 254            RESUME                   0

 267            NOP

 268    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('log_operator_action',))
                IMPORT_NAME              0 (app.services.operator.audit_service)
                IMPORT_FROM              1 (log_operator_action)
                STORE_FAST               9 (log_operator_action)
                POP_TOP

 272            LOAD_FAST_BORROW         3 (actor_type)
                LOAD_CONST              15 (('OPERATOR', 'ADMIN', 'SYSTEM'))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN
                LOAD_FAST                3 (actor_type)
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               2 ('OPERATOR')
        L3:     STORE_FAST              10 (mapped_actor)

 273            LOAD_FAST                9 (log_operator_action)
                PUSH_NULL

 274            LOAD_FAST_BORROW         0 (record)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               3 ('brokerage_id')
                CALL                     1

 275            LOAD_FAST               10 (mapped_actor)

 276            LOAD_FAST                4 (actor_id)

 277            LOAD_FAST                1 (action)

 278            LOAD_FAST_BORROW         6 (error_code)
                POP_JUMP_IF_NOT_NONE     3 (to L4)
                NOT_TAKEN
                LOAD_CONST               5 ('SUCCESS')
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               6 ('FAILED')

 279    L5:     LOAD_CONST               7 ('api_key_rotation_event')

 280            LOAD_FAST_BORROW         0 (record)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               8 ('rotation_id')
                CALL                     1

 281            LOAD_FAST                8 (warning_count)

 283            LOAD_CONST               9 ('event')
                LOAD_FAST                7 (event)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                LOAD_CONST              10 ('security.api_key_rotation.event')

 284    L8:     LOAD_CONST              11 ('target_status')
                LOAD_FAST_BORROW         2 (target_status)

 285            LOAD_CONST              12 ('error_code')
                LOAD_FAST_BORROW         6 (error_code)

 282            BUILD_MAP                3

 273            LOAD_CONST              13 (('brokerage_id', 'actor_type', 'actor_id', 'action', 'status', 'target_type', 'target_id', 'warning_count', 'metadata'))
                CALL_KW                  9
        L9:     RETURN_VALUE

  --   L10:     PUSH_EXC_INFO

 288            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L14)
                NOT_TAKEN
                STORE_FAST              11 (e)

 289   L11:     LOAD_GLOBAL              8 (logger)
                LOAD_ATTR               11 (warning + NULL|self)

 290            LOAD_CONST              14 ('_audit api_key_rotation error type=')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 289            CALL                     1
                POP_TOP

 292   L12:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                LOAD_CONST               4 (None)
                RETURN_VALUE

  --   L13:     LOAD_CONST               4 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 288   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L6 -> L10 [0]
  L7 to L9 -> L10 [0]
  L10 to L11 -> L15 [1] lasti
  L11 to L12 -> L13 [1] lasti
  L13 to L15 -> L15 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app/services/security/api_key_rotation.py", line 295>:
295           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('db')

296           LOAD_CONST               2 ('Any')

295           LOAD_CONST               3 ('rotation_id')

298           LOAD_CONST               4 ('str')

295           LOAD_CONST               5 ('return')

299           LOAD_CONST               6 ('Optional[Dict[str, Any]]')

295           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _lookup_rotation at 0x0000018C17CD4970, file "app/services/security/api_key_rotation.py", line 295>:
 295            RESUME                   0

 300            NOP

 302    L1:     LOAD_FAST_BORROW         0 (db)
                LOAD_ATTR                1 (table + NULL|self)
                LOAD_GLOBAL              2 (_TABLE)
                CALL                     1

 303            LOAD_ATTR                5 (select + NULL|self)
                LOAD_CONST               0 (',')
                LOAD_ATTR                7 (join + NULL|self)
                LOAD_GLOBAL              8 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 304            LOAD_ATTR               11 (eq + NULL|self)
                LOAD_CONST               1 ('rotation_id')
                LOAD_FAST_BORROW         1 (rotation_id)
                CALL                     2

 305            LOAD_ATTR               13 (limit + NULL|self)
                LOAD_SMALL_INT           2
                CALL                     1

 306            LOAD_ATTR               15 (execute + NULL|self)
                CALL                     0

 301            STORE_FAST               2 (result)

 308            LOAD_GLOBAL             17 (list + NULL)
                LOAD_GLOBAL             19 (getattr + NULL)
                LOAD_FAST_BORROW         2 (result)
                LOAD_CONST               2 ('data')
                LOAD_CONST               3 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
        L2:     NOT_TAKEN
        L3:     POP_TOP
                BUILD_LIST               0
        L4:     CALL                     1
                STORE_FAST               3 (rows)

 309            LOAD_FAST_BORROW         3 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
        L5:     NOT_TAKEN

 310            LOAD_CONST               3 (None)
                RETURN_VALUE

 311    L6:     LOAD_GLOBAL             21 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_GLOBAL             22 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       10 (to L8)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
        L7:     RETURN_VALUE
        L8:     LOAD_CONST               3 (None)
        L9:     RETURN_VALUE

  --   L10:     PUSH_EXC_INFO

 312            LOAD_GLOBAL             24 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L14)
                NOT_TAKEN
                STORE_FAST               4 (e)

 313   L11:     LOAD_GLOBAL             26 (logger)
                LOAD_ATTR               29 (warning + NULL|self)

 314            LOAD_CONST               4 ('_lookup_rotation error type=')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 313            CALL                     1
                POP_TOP

 316   L12:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                LOAD_CONST               3 (None)
                RETURN_VALUE

  --   L13:     LOAD_CONST               3 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 312   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L10 [0]
  L3 to L5 -> L10 [0]
  L6 to L7 -> L10 [0]
  L8 to L9 -> L10 [0]
  L10 to L11 -> L15 [1] lasti
  L11 to L12 -> L13 [1] lasti
  L13 to L15 -> L15 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025230, file "app/services/security/api_key_rotation.py", line 323>:
323           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

325           LOAD_CONST               2 ('Any')

323           LOAD_CONST               3 ('actor_type')

326           LOAD_CONST               4 ('str')

323           LOAD_CONST               5 ('actor_id')

327           LOAD_CONST               6 ('Optional[str]')

323           LOAD_CONST               7 ('previous_api_key')

328           LOAD_CONST               6 ('Optional[str]')

323           LOAD_CONST               8 ('return')

329           LOAD_CONST               9 ('Dict[str, Any]')

323           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object request_api_key_rotation at 0x0000018C17D8BD40, file "app/services/security/api_key_rotation.py", line 323>:
 323            RESUME                   0

 333            LOAD_FAST_BORROW         1 (actor_type)
                LOAD_GLOBAL              0 (ALLOWED_ACTOR_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       14 (to L1)
                NOT_TAKEN

 334            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               2 ('invalid_actor_type')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 335    L1:     LOAD_FAST_BORROW         2 (actor_id)
                POP_JUMP_IF_NONE        12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              5 (_bound_actor_id + NULL)
                LOAD_FAST_BORROW         2 (actor_id)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               4 (None)
        L3:     STORE_FAST               4 (actor)

 336            LOAD_FAST_BORROW         2 (actor_id)
                POP_JUMP_IF_NONE        18 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (actor)
                POP_JUMP_IF_NOT_NONE    14 (to L4)
                NOT_TAKEN

 337            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               5 ('invalid_actor_id')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 338    L4:     LOAD_GLOBAL              7 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               5 (bid)

 339            LOAD_FAST_BORROW         5 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L5)
                NOT_TAKEN

 340            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               6 ('missing_brokerage_id')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 342    L5:     LOAD_CONST               4 (None)
                STORE_FAST               6 (prev_fp)

 343            LOAD_FAST_BORROW         3 (previous_api_key)
                POP_JUMP_IF_NONE        29 (to L6)
                NOT_TAKEN

 344            LOAD_GLOBAL              9 (fingerprint_api_key + NULL)
                LOAD_FAST_BORROW         3 (previous_api_key)
                CALL                     1
                STORE_FAST               6 (prev_fp)

 345            LOAD_FAST_BORROW         6 (prev_fp)
                POP_JUMP_IF_NOT_NONE    14 (to L6)
                NOT_TAKEN

 346            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 347            LOAD_CONST               1 ('failed')
                LOAD_CONST               7 ('invalid_previous_api_key')

 346            LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 350    L6:     LOAD_GLOBAL             11 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               7 (db)

 351            LOAD_FAST_BORROW         7 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L7)
                NOT_TAKEN

 352            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 353            LOAD_CONST               8 ('skipped')

 354            LOAD_CONST               9 ('api_key_rotation_store_unavailable')
                BUILD_LIST               1

 355            LOAD_CONST               9 ('api_key_rotation_store_unavailable')

 352            LOAD_CONST              10 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 359    L7:     LOAD_CONST              11 ('rotation_id')
                LOAD_GLOBAL             13 (str + NULL)
                LOAD_GLOBAL             14 (uuid)
                LOAD_ATTR               16 (uuid4)
                PUSH_NULL
                CALL                     0
                CALL                     1

 360            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST_BORROW         5 (bid)

 361            LOAD_CONST              13 ('requested_at')
                LOAD_GLOBAL             19 (_iso + NULL)
                LOAD_GLOBAL             21 (_now_dt + NULL)
                CALL                     0
                CALL                     1

 362            LOAD_CONST              14 ('actor_type')
                LOAD_FAST_BORROW         1 (actor_type)

 363            LOAD_CONST              15 ('actor_id')
                LOAD_FAST_BORROW         4 (actor)

 364            LOAD_CONST              16 ('status')
                LOAD_CONST              17 ('REQUESTED')

 365            LOAD_CONST              18 ('previous_key_fingerprint')
                LOAD_FAST_BORROW         6 (prev_fp)

 366            LOAD_CONST              19 ('new_key_fingerprint')
                LOAD_CONST               4 (None)

 367            LOAD_CONST              20 ('effective_at')
                LOAD_CONST               4 (None)

 368            LOAD_CONST              21 ('warning_count')
                LOAD_SMALL_INT           0

 369            LOAD_CONST              22 ('metadata')
                LOAD_GLOBAL             23 (_project_metadata + NULL)

 370            LOAD_CONST              23 ('event')
                LOAD_CONST              24 ('security.api_key_rotation.requested')

 371            LOAD_CONST              18 ('previous_key_fingerprint')
                LOAD_FAST_BORROW         6 (prev_fp)

 372            LOAD_CONST              25 ('operator_command')
                LOAD_CONST              26 ('request_api_key_rotation')

 369            BUILD_MAP                3
                CALL                     1

 358            BUILD_MAP               11
                STORE_FAST               8 (row)

 375            NOP

 376    L8:     LOAD_FAST_BORROW         7 (db)
                LOAD_ATTR               25 (table + NULL|self)
                LOAD_GLOBAL             26 (_TABLE)
                CALL                     1
                LOAD_ATTR               29 (insert + NULL|self)
                LOAD_FAST_BORROW         8 (row)
                CALL                     1
                LOAD_ATTR               31 (execute + NULL|self)
                CALL                     0
                STORE_FAST               9 (result)

 377            LOAD_GLOBAL             33 (list + NULL)
                LOAD_GLOBAL             35 (getattr + NULL)
                LOAD_FAST_BORROW         9 (result)
                LOAD_CONST              27 ('data')
                LOAD_CONST               4 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L9:     CALL                     1
                STORE_FAST              10 (rows)

 378            LOAD_FAST_BORROW        10 (rows)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L12)
       L10:     NOT_TAKEN
       L11:     LOAD_GLOBAL             37 (_project_row + NULL)
                LOAD_FAST_BORROW        10 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                JUMP_FORWARD            10 (to L13)
       L12:     LOAD_GLOBAL             37 (_project_row + NULL)
                LOAD_FAST_BORROW         8 (row)
                CALL                     1
       L13:     STORE_FAST              11 (proj)

 388   L14:     LOAD_GLOBAL             49 (_audit + NULL)

 389            LOAD_FAST               11 (proj)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST                8 (row)

 390   L15:     LOAD_CONST              26 ('request_api_key_rotation')

 391            LOAD_CONST              17 ('REQUESTED')

 392            LOAD_FAST                1 (actor_type)

 393            LOAD_FAST                4 (actor)

 394            LOAD_CONST              24 ('security.api_key_rotation.requested')

 388            LOAD_CONST              30 (('record', 'action', 'target_status', 'actor_type', 'actor_id', 'event'))
                CALL_KW                  6
                STORE_FAST              13 (audit_env)

 396            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 397            LOAD_CONST              31 ('ok')

 398            LOAD_FAST               11 (proj)

 399            LOAD_CONST              32 ('from')
                LOAD_CONST               4 (None)
                LOAD_CONST              33 ('to')
                LOAD_CONST              17 ('REQUESTED')
                LOAD_CONST              31 ('ok')
                LOAD_CONST              34 (True)
                BUILD_MAP                3

 400            LOAD_FAST               13 (audit_env)

 396            LOAD_CONST              35 (('status', 'record', 'transition', 'audit_row'))
                CALL_KW                  4
                RETURN_VALUE

  --   L16:     PUSH_EXC_INFO

 379            LOAD_GLOBAL             38 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L21)
                NOT_TAKEN
                STORE_FAST              12 (e)

 380   L17:     LOAD_GLOBAL             40 (logger)
                LOAD_ATTR               43 (warning + NULL|self)

 381            LOAD_CONST              28 ('request_api_key_rotation insert error type=')
                LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 380            CALL                     1
                POP_TOP

 383            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 384            LOAD_CONST               8 ('skipped')

 385            LOAD_CONST              29 ('db_write_failed:')
                LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 386            LOAD_CONST               9 ('api_key_rotation_store_unavailable')

 383            LOAD_CONST              10 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
       L18:     SWAP                     2
       L19:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RETURN_VALUE

  --   L20:     LOAD_CONST               4 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RERAISE                  1

 379   L21:     RERAISE                  0

  --   L22:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L8 to L10 -> L16 [0]
  L11 to L14 -> L16 [0]
  L16 to L17 -> L22 [1] lasti
  L17 to L18 -> L20 [1] lasti
  L18 to L19 -> L22 [1] lasti
  L20 to L22 -> L22 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C1812C360, file "app/services/security/api_key_rotation.py", line 408>:
408           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rotation_id')

410           LOAD_CONST               2 ('str')

408           LOAD_CONST               3 ('to_status')

411           LOAD_CONST               2 ('str')

408           LOAD_CONST               4 ('actor_type')

412           LOAD_CONST               2 ('str')

408           LOAD_CONST               5 ('actor_id')

413           LOAD_CONST               6 ('Optional[str]')

408           LOAD_CONST               7 ('event')

414           LOAD_CONST               2 ('str')

408           LOAD_CONST               8 ('extra_patch')

415           LOAD_CONST               9 ('Optional[Dict[str, Any]]')

408           LOAD_CONST              10 ('error_code')

416           LOAD_CONST               6 ('Optional[str]')

408           LOAD_CONST              11 ('return')

417           LOAD_CONST              12 ('Dict[str, Any]')

408           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object _transition at 0x0000018C182F65F0, file "app/services/security/api_key_rotation.py", line 408>:
 408            RESUME                   0

 419            LOAD_FAST_BORROW         2 (actor_type)
                LOAD_GLOBAL              0 (ALLOWED_ACTOR_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       14 (to L1)
                NOT_TAKEN

 420            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               2 ('invalid_actor_type')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 421    L1:     LOAD_FAST_BORROW         3 (actor_id)
                POP_JUMP_IF_NONE        12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              5 (_bound_actor_id + NULL)
                LOAD_FAST_BORROW         3 (actor_id)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               4 (None)
        L3:     STORE_FAST               7 (actor)

 422            LOAD_FAST_BORROW         3 (actor_id)
                POP_JUMP_IF_NONE        18 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         7 (actor)
                POP_JUMP_IF_NOT_NONE    14 (to L4)
                NOT_TAKEN

 423            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               5 ('invalid_actor_id')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 424    L4:     LOAD_GLOBAL              7 (_bound_id + NULL)
                LOAD_FAST_BORROW         0 (rotation_id)
                LOAD_GLOBAL              8 (_ROTATION_ID_MAX_LEN)
                CALL                     2
                STORE_FAST               8 (rid)

 425            LOAD_FAST_BORROW         8 (rid)
                POP_JUMP_IF_NOT_NONE    14 (to L5)
                NOT_TAKEN

 426            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               6 ('invalid_rotation_id')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 428    L5:     LOAD_GLOBAL             11 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               9 (db)

 429            LOAD_FAST_BORROW         9 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L6)
                NOT_TAKEN

 430            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 431            LOAD_CONST               7 ('skipped')

 432            LOAD_CONST               8 ('api_key_rotation_store_unavailable')
                BUILD_LIST               1

 433            LOAD_CONST               8 ('api_key_rotation_store_unavailable')

 430            LOAD_CONST               9 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 436    L6:     LOAD_GLOBAL             13 (_lookup_rotation + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 152 (db, rid)
                LOAD_CONST              10 (('rotation_id',))
                CALL_KW                  2
                STORE_FAST              10 (current)

 437            LOAD_FAST_BORROW        10 (current)
                POP_JUMP_IF_NOT_NONE    14 (to L7)
                NOT_TAKEN

 438            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 439            LOAD_CONST               1 ('failed')

 440            LOAD_CONST              11 ('rotation_not_found')

 438            LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 442    L7:     LOAD_GLOBAL             15 (_validate_transition + NULL)

 443            LOAD_FAST_BORROW        10 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1

 444            LOAD_FAST_BORROW         1 (to_status)

 442            LOAD_CONST              13 (('from_status', 'to_status'))
                CALL_KW                  2
                STORE_FAST              11 (err)

 446            LOAD_FAST_BORROW        11 (err)
                POP_JUMP_IF_NONE        84 (to L8)
                NOT_TAKEN

 447            LOAD_GLOBAL             19 (_audit + NULL)

 448            LOAD_FAST_BORROW        10 (current)

 449            LOAD_CONST              14 ('transition_api_key_rotation_')
                LOAD_FAST_BORROW         1 (to_status)
                LOAD_ATTR               21 (lower + NULL|self)
                CALL                     0
                FORMAT_SIMPLE
                BUILD_STRING             2

 450            LOAD_FAST_BORROW         1 (to_status)

 451            LOAD_FAST_BORROW         2 (actor_type)

 452            LOAD_FAST_BORROW         7 (actor)

 453            LOAD_CONST              15 ('FAILED')

 454            LOAD_FAST_BORROW        11 (err)

 455            LOAD_CONST              16 ('security.api_key_rotation.failed')

 456            LOAD_SMALL_INT           1

 447            LOAD_CONST              17 (('record', 'action', 'target_status', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                STORE_FAST              12 (audit_env)

 458            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 459            LOAD_CONST               1 ('failed')

 460            LOAD_GLOBAL             23 (_project_row + NULL)
                LOAD_FAST_BORROW        10 (current)
                CALL                     1

 461            LOAD_CONST              18 ('from')
                LOAD_FAST_BORROW        10 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              19 ('to')
                LOAD_FAST_BORROW         1 (to_status)
                LOAD_CONST              20 ('ok')
                LOAD_CONST              21 (False)
                BUILD_MAP                3

 462            LOAD_FAST_BORROW        12 (audit_env)

 463            LOAD_FAST_BORROW        11 (err)

 458            LOAD_CONST              22 (('status', 'record', 'transition', 'audit_row', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

 466    L8:     LOAD_FAST_BORROW        10 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              23 ('metadata')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L9:     STORE_FAST              13 (md)

 468            LOAD_CONST              12 ('status')
                LOAD_FAST                1 (to_status)

 469            LOAD_CONST              23 ('metadata')
                LOAD_GLOBAL             25 (_project_metadata + NULL)
                BUILD_MAP                0

 470            LOAD_GLOBAL             27 (isinstance + NULL)
                LOAD_FAST_BORROW        13 (md)
                LOAD_GLOBAL             28 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_FAST               13 (md)
                JUMP_FORWARD             1 (to L11)
       L10:     BUILD_MAP                0

 469   L11:     DICT_UPDATE              1

 471            LOAD_CONST              24 ('event')
                LOAD_FAST_BORROW         4 (event)

 472            LOAD_CONST              25 ('operator_command')
                LOAD_CONST              26 ('transition_to_')
                LOAD_FAST_BORROW         1 (to_status)
                LOAD_ATTR               21 (lower + NULL|self)
                CALL                     0
                FORMAT_SIMPLE
                BUILD_STRING             2

 473            LOAD_CONST              27 ('error_code')
                LOAD_FAST_BORROW         6 (error_code)

 469            BUILD_MAP                3
                DICT_UPDATE              1
                CALL                     1

 467            BUILD_MAP                2
                STORE_FAST              14 (patch)

 476            LOAD_GLOBAL             27 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (extra_patch)
                LOAD_GLOBAL             28 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       31 (to L14)
                NOT_TAKEN

 477            LOAD_FAST_BORROW         5 (extra_patch)
                LOAD_ATTR               31 (items + NULL|self)
                CALL                     0
                GET_ITER
       L12:     FOR_ITER                10 (to L13)
                UNPACK_SEQUENCE          2
                STORE_FAST              15 (k)
                STORE_FAST              16 (v)

 478            LOAD_FAST_BORROW        16 (v)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 239 (patch, k)
                STORE_SUBSCR
                JUMP_BACKWARD           12 (to L12)

 477   L13:     END_FOR
                POP_ITER

 480   L14:     NOP

 482   L15:     LOAD_FAST_BORROW         9 (db)
                LOAD_ATTR               33 (table + NULL|self)
                LOAD_GLOBAL             34 (_TABLE)
                CALL                     1

 483            LOAD_ATTR               37 (update + NULL|self)
                LOAD_FAST_BORROW        14 (patch)
                CALL                     1

 484            LOAD_ATTR               39 (eq + NULL|self)
                LOAD_CONST              28 ('rotation_id')
                LOAD_FAST_BORROW         8 (rid)
                CALL                     2

 485            LOAD_ATTR               41 (execute + NULL|self)
                CALL                     0

 481            STORE_FAST              17 (upd)

 487            LOAD_GLOBAL             43 (list + NULL)
                LOAD_GLOBAL             45 (getattr + NULL)
                LOAD_FAST_BORROW        17 (upd)
                LOAD_CONST              29 ('data')
                LOAD_CONST               4 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
       L16:     NOT_TAKEN
       L17:     POP_TOP
                BUILD_LIST               0
       L18:     CALL                     1
                STORE_FAST              18 (rows_after)

 497   L19:     LOAD_FAST               18 (rows_after)
                TO_BOOL
                POP_JUMP_IF_TRUE        84 (to L20)
                NOT_TAKEN

 498            LOAD_GLOBAL             19 (_audit + NULL)

 499            LOAD_FAST               10 (current)

 500            LOAD_CONST              14 ('transition_api_key_rotation_')
                LOAD_FAST                1 (to_status)
                LOAD_ATTR               21 (lower + NULL|self)
                CALL                     0
                FORMAT_SIMPLE
                BUILD_STRING             2

 501            LOAD_FAST                1 (to_status)

 502            LOAD_FAST                2 (actor_type)

 503            LOAD_FAST                7 (actor)

 504            LOAD_CONST              15 ('FAILED')

 505            LOAD_CONST              32 ('policy_refused_or_no_rows')

 506            LOAD_CONST              16 ('security.api_key_rotation.failed')

 507            LOAD_SMALL_INT           1

 498            LOAD_CONST              17 (('record', 'action', 'target_status', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                STORE_FAST              12 (audit_env)

 509            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 510            LOAD_CONST               1 ('failed')

 511            LOAD_GLOBAL             23 (_project_row + NULL)
                LOAD_FAST               10 (current)
                CALL                     1

 512            LOAD_CONST              18 ('from')
                LOAD_FAST               10 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              19 ('to')
                LOAD_FAST                1 (to_status)
                LOAD_CONST              20 ('ok')
                LOAD_CONST              21 (False)
                BUILD_MAP                3

 513            LOAD_FAST               12 (audit_env)

 514            LOAD_CONST              32 ('policy_refused_or_no_rows')

 509            LOAD_CONST              22 (('status', 'record', 'transition', 'audit_row', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

 516   L20:     LOAD_GLOBAL             23 (_project_row + NULL)
                LOAD_FAST               18 (rows_after)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                STORE_FAST              20 (new_record)

 517            LOAD_GLOBAL             19 (_audit + NULL)

 518            LOAD_FAST               20 (new_record)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L21)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST               10 (current)

 519   L21:     LOAD_CONST              14 ('transition_api_key_rotation_')
                LOAD_FAST                1 (to_status)
                LOAD_ATTR               21 (lower + NULL|self)
                CALL                     0
                FORMAT_SIMPLE
                BUILD_STRING             2

 520            LOAD_FAST                1 (to_status)

 521            LOAD_FAST                2 (actor_type)

 522            LOAD_FAST                7 (actor)

 523            LOAD_FAST                4 (event)

 517            LOAD_CONST              33 (('record', 'action', 'target_status', 'actor_type', 'actor_id', 'event'))
                CALL_KW                  6
                STORE_FAST              12 (audit_env)

 525            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 526            LOAD_CONST              20 ('ok')

 527            LOAD_FAST               20 (new_record)

 528            LOAD_CONST              18 ('from')
                LOAD_FAST               10 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              19 ('to')
                LOAD_FAST                1 (to_status)
                LOAD_CONST              20 ('ok')
                LOAD_CONST              34 (True)
                BUILD_MAP                3

 529            LOAD_FAST               12 (audit_env)

 525            LOAD_CONST              35 (('status', 'record', 'transition', 'audit_row'))
                CALL_KW                  4
                RETURN_VALUE

  --   L22:     PUSH_EXC_INFO

 488            LOAD_GLOBAL             46 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L27)
                NOT_TAKEN
                STORE_FAST              19 (e)

 489   L23:     LOAD_GLOBAL             48 (logger)
                LOAD_ATTR               51 (warning + NULL|self)

 490            LOAD_CONST              30 ('_transition update error type=')
                LOAD_GLOBAL             53 (type + NULL)
                LOAD_FAST               19 (e)
                CALL                     1
                LOAD_ATTR               54 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 489            CALL                     1
                POP_TOP

 492            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 493            LOAD_CONST               7 ('skipped')

 494            LOAD_CONST              31 ('db_write_failed:')
                LOAD_GLOBAL             53 (type + NULL)
                LOAD_FAST               19 (e)
                CALL                     1
                LOAD_ATTR               54 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 495            LOAD_CONST               8 ('api_key_rotation_store_unavailable')

 492            LOAD_CONST               9 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
       L24:     SWAP                     2
       L25:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              19 (e)
                DELETE_FAST             19 (e)
                RETURN_VALUE

  --   L26:     LOAD_CONST               4 (None)
                STORE_FAST              19 (e)
                DELETE_FAST             19 (e)
                RERAISE                  1

 488   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L15 to L16 -> L22 [0]
  L17 to L19 -> L22 [0]
  L22 to L23 -> L28 [1] lasti
  L23 to L24 -> L26 [1] lasti
  L24 to L25 -> L28 [1] lasti
  L26 to L28 -> L28 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app/services/security/api_key_rotation.py", line 533>:
533           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rotation_id')

535           LOAD_CONST               2 ('str')

533           LOAD_CONST               3 ('actor_type')

536           LOAD_CONST               2 ('str')

533           LOAD_CONST               4 ('actor_id')

537           LOAD_CONST               5 ('Optional[str]')

533           LOAD_CONST               6 ('return')

538           LOAD_CONST               7 ('Dict[str, Any]')

533           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object approve_api_key_rotation at 0x0000018C18053750, file "app/services/security/api_key_rotation.py", line 533>:
533           RESUME                   0

541           LOAD_FAST_BORROW         1 (actor_type)
              LOAD_CONST               7 (('OPERATOR', 'ADMIN'))
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       14 (to L1)
              NOT_TAKEN

542           LOAD_GLOBAL              1 (_safe_envelope + NULL)
              LOAD_CONST               1 ('failed')
              LOAD_CONST               2 ('invalid_actor_type')
              LOAD_CONST               3 (('status', 'error_code'))
              CALL_KW                  2
              RETURN_VALUE

543   L1:     LOAD_GLOBAL              3 (_transition + NULL)

544           LOAD_FAST_BORROW         0 (rotation_id)

545           LOAD_CONST               4 ('APPROVED')

546           LOAD_FAST_BORROW         1 (actor_type)

547           LOAD_FAST_BORROW         2 (actor_id)

548           LOAD_CONST               5 ('security.api_key_rotation.approved')

543           LOAD_CONST               6 (('rotation_id', 'to_status', 'actor_type', 'actor_id', 'event'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app/services/security/api_key_rotation.py", line 552>:
552           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rotation_id')

554           LOAD_CONST               2 ('str')

552           LOAD_CONST               3 ('actor_type')

555           LOAD_CONST               2 ('str')

552           LOAD_CONST               4 ('actor_id')

556           LOAD_CONST               5 ('Optional[str]')

552           LOAD_CONST               6 ('return')

557           LOAD_CONST               7 ('Dict[str, Any]')

552           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object cancel_api_key_rotation at 0x0000018C1802CE70, file "app/services/security/api_key_rotation.py", line 552>:
552           RESUME                   0

560           LOAD_FAST_BORROW         1 (actor_type)
              LOAD_GLOBAL              0 (ALLOWED_ACTOR_TYPES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       14 (to L1)
              NOT_TAKEN

561           LOAD_GLOBAL              3 (_safe_envelope + NULL)
              LOAD_CONST               1 ('failed')
              LOAD_CONST               2 ('invalid_actor_type')
              LOAD_CONST               3 (('status', 'error_code'))
              CALL_KW                  2
              RETURN_VALUE

562   L1:     LOAD_GLOBAL              5 (_transition + NULL)

563           LOAD_FAST_BORROW         0 (rotation_id)

564           LOAD_CONST               4 ('CANCELLED')

565           LOAD_FAST_BORROW         1 (actor_type)

566           LOAD_FAST_BORROW         2 (actor_id)

567           LOAD_CONST               5 ('security.api_key_rotation.failed')

562           LOAD_CONST               6 (('rotation_id', 'to_status', 'actor_type', 'actor_id', 'event'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026530, file "app/services/security/api_key_rotation.py", line 571>:
571           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rotation_id')

573           LOAD_CONST               2 ('str')

571           LOAD_CONST               3 ('actor_type')

574           LOAD_CONST               2 ('str')

571           LOAD_CONST               4 ('actor_id')

575           LOAD_CONST               5 ('Optional[str]')

571           LOAD_CONST               6 ('error_code')

576           LOAD_CONST               5 ('Optional[str]')

571           LOAD_CONST               7 ('return')

577           LOAD_CONST               8 ('Dict[str, Any]')

571           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object fail_api_key_rotation at 0x0000018C180532D0, file "app/services/security/api_key_rotation.py", line 571>:
571           RESUME                   0

580           LOAD_FAST_BORROW         1 (actor_type)
              LOAD_CONST               7 (('OPERATOR', 'ADMIN', 'SYSTEM'))
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       14 (to L1)
              NOT_TAKEN

581           LOAD_GLOBAL              1 (_safe_envelope + NULL)
              LOAD_CONST               1 ('failed')
              LOAD_CONST               2 ('invalid_actor_type')
              LOAD_CONST               3 (('status', 'error_code'))
              CALL_KW                  2
              RETURN_VALUE

582   L1:     LOAD_GLOBAL              3 (_transition + NULL)

583           LOAD_FAST_BORROW         0 (rotation_id)

584           LOAD_CONST               4 ('FAILED')

585           LOAD_FAST_BORROW         1 (actor_type)

586           LOAD_FAST_BORROW         2 (actor_id)

587           LOAD_CONST               5 ('security.api_key_rotation.failed')

588           LOAD_FAST_BORROW         3 (error_code)

582           LOAD_CONST               6 (('rotation_id', 'to_status', 'actor_type', 'actor_id', 'event', 'error_code'))
              CALL_KW                  6
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026330, file "app/services/security/api_key_rotation.py", line 592>:
592           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rotation_id')

594           LOAD_CONST               2 ('str')

592           LOAD_CONST               3 ('new_api_key')

595           LOAD_CONST               4 ('Optional[str]')

592           LOAD_CONST               5 ('actor_type')

596           LOAD_CONST               2 ('str')

592           LOAD_CONST               6 ('actor_id')

597           LOAD_CONST               4 ('Optional[str]')

592           LOAD_CONST               7 ('return')

598           LOAD_CONST               8 ('Dict[str, Any]')

592           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object rotate_api_key_if_helper_available at 0x0000018C17D77E00, file "app/services/security/api_key_rotation.py", line 592>:
592           RESUME                   0

619           LOAD_FAST_BORROW         2 (actor_type)
              LOAD_CONST              16 (('OPERATOR', 'ADMIN'))
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       14 (to L1)
              NOT_TAKEN

620           LOAD_GLOBAL              1 (_safe_envelope + NULL)
              LOAD_CONST               1 ('failed')
              LOAD_CONST               2 ('invalid_actor_type')
              LOAD_CONST               3 (('status', 'error_code'))
              CALL_KW                  2
              RETURN_VALUE

621   L1:     LOAD_FAST_BORROW         3 (actor_id)
              POP_JUMP_IF_NONE        12 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              3 (_bound_actor_id + NULL)
              LOAD_FAST_BORROW         3 (actor_id)
              CALL                     1
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               4 (None)
      L3:     STORE_FAST               4 (actor)

622           LOAD_FAST_BORROW         3 (actor_id)
              POP_JUMP_IF_NONE        18 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         4 (actor)
              POP_JUMP_IF_NOT_NONE    14 (to L4)
              NOT_TAKEN

623           LOAD_GLOBAL              1 (_safe_envelope + NULL)
              LOAD_CONST               1 ('failed')
              LOAD_CONST               5 ('invalid_actor_id')
              LOAD_CONST               3 (('status', 'error_code'))
              CALL_KW                  2
              RETURN_VALUE

624   L4:     LOAD_GLOBAL              5 (_bound_id + NULL)
              LOAD_FAST_BORROW         0 (rotation_id)
              LOAD_GLOBAL              6 (_ROTATION_ID_MAX_LEN)
              CALL                     2
              STORE_FAST               5 (rid)

625           LOAD_FAST_BORROW         5 (rid)
              POP_JUMP_IF_NOT_NONE    14 (to L5)
              NOT_TAKEN

626           LOAD_GLOBAL              1 (_safe_envelope + NULL)
              LOAD_CONST               1 ('failed')
              LOAD_CONST               6 ('invalid_rotation_id')
              LOAD_CONST               3 (('status', 'error_code'))
              CALL_KW                  2
              RETURN_VALUE

628   L5:     LOAD_FAST_BORROW         1 (new_api_key)
              POP_JUMP_IF_NOT_NONE    16 (to L6)
              NOT_TAKEN

630           LOAD_GLOBAL              1 (_safe_envelope + NULL)

631           LOAD_CONST               7 ('deferred')

632           LOAD_CONST               8 ('api_key_delivery_channel_unavailable')
              BUILD_LIST               1

633           LOAD_CONST               8 ('api_key_delivery_channel_unavailable')

630           LOAD_CONST               9 (('status', 'warnings', 'error_code'))
              CALL_KW                  3
              RETURN_VALUE

636   L6:     LOAD_GLOBAL              9 (fingerprint_api_key + NULL)
              LOAD_FAST_BORROW         1 (new_api_key)
              CALL                     1
              STORE_FAST               6 (new_fp)

637           LOAD_FAST_BORROW         6 (new_fp)
              POP_JUMP_IF_NOT_NONE    14 (to L7)
              NOT_TAKEN

638           LOAD_GLOBAL              1 (_safe_envelope + NULL)
              LOAD_CONST               1 ('failed')
              LOAD_CONST              10 ('invalid_new_api_key')
              LOAD_CONST               3 (('status', 'error_code'))
              CALL_KW                  2
              RETURN_VALUE

640   L7:     LOAD_GLOBAL             11 (_transition + NULL)

641           LOAD_FAST_BORROW         5 (rid)

642           LOAD_CONST              11 ('ROTATED')

643           LOAD_FAST_BORROW         2 (actor_type)

644           LOAD_FAST_BORROW         4 (actor)

645           LOAD_CONST              12 ('security.api_key_rotation.completed')

647           LOAD_CONST              13 ('new_key_fingerprint')
              LOAD_FAST_BORROW         6 (new_fp)

648           LOAD_CONST              14 ('effective_at')
              LOAD_GLOBAL             13 (_iso + NULL)
              LOAD_GLOBAL             15 (_now_dt + NULL)
              CALL                     0
              CALL                     1

646           BUILD_MAP                2

640           LOAD_CONST              15 (('rotation_id', 'to_status', 'actor_type', 'actor_id', 'event', 'extra_patch'))
              CALL_KW                  6
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app/services/security/api_key_rotation.py", line 657>:
657           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

659           LOAD_CONST               2 ('Any')

657           LOAD_CONST               3 ('rotation_id')

660           LOAD_CONST               4 ('Optional[str]')

657           LOAD_CONST               5 ('return')

661           LOAD_CONST               6 ('Dict[str, Any]')

657           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object api_key_rotation_status at 0x0000018C1778B3F0, file "app/services/security/api_key_rotation.py", line 657>:
 657            RESUME                   0

 665            LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               2 (bid)

 666            LOAD_FAST_BORROW         2 (bid)
                POP_JUMP_IF_NOT_NONE    11 (to L1)
                NOT_TAKEN

 668            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 669            LOAD_CONST               4 ('record')
                LOAD_CONST               1 (None)

 670            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 671            LOAD_CONST               6 ('error_code')
                LOAD_CONST               7 ('missing_brokerage_id')

 667            BUILD_MAP                4
                RETURN_VALUE

 673    L1:     LOAD_GLOBAL              3 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               3 (db)

 674            LOAD_FAST_BORROW         3 (db)
                POP_JUMP_IF_NOT_NONE    12 (to L2)
                NOT_TAKEN

 676            LOAD_CONST               2 ('status')
                LOAD_CONST               8 ('skipped')

 677            LOAD_CONST               4 ('record')
                LOAD_CONST               1 (None)

 678            LOAD_CONST               5 ('warnings')
                LOAD_CONST               9 ('api_key_rotation_store_unavailable')
                BUILD_LIST               1

 679            LOAD_CONST               6 ('error_code')
                LOAD_CONST               9 ('api_key_rotation_store_unavailable')

 675            BUILD_MAP                4
                RETURN_VALUE

 681    L2:     NOP

 682    L3:     LOAD_FAST_BORROW         1 (rotation_id)
                POP_JUMP_IF_NONE       148 (to L6)
                NOT_TAKEN

 683            LOAD_GLOBAL              5 (_bound_id + NULL)
                LOAD_FAST_BORROW         1 (rotation_id)
                LOAD_GLOBAL              6 (_ROTATION_ID_MAX_LEN)
                CALL                     2
                STORE_FAST               4 (rid)

 684            LOAD_FAST_BORROW         4 (rid)
                POP_JUMP_IF_NOT_NONE    11 (to L5)
                NOT_TAKEN

 686            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 687            LOAD_CONST               4 ('record')
                LOAD_CONST               1 (None)

 688            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 689            LOAD_CONST               6 ('error_code')
                LOAD_CONST              10 ('invalid_rotation_id')

 685            BUILD_MAP                4
        L4:     RETURN_VALUE

 692    L5:     LOAD_FAST_BORROW         3 (db)
                LOAD_ATTR                9 (table + NULL|self)
                LOAD_GLOBAL             10 (_TABLE)
                CALL                     1

 693            LOAD_ATTR               13 (select + NULL|self)
                LOAD_CONST              11 (',')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_GLOBAL             16 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 694            LOAD_ATTR               19 (eq + NULL|self)
                LOAD_CONST              12 ('rotation_id')
                LOAD_FAST_BORROW         4 (rid)
                CALL                     2

 695            LOAD_ATTR               19 (eq + NULL|self)
                LOAD_CONST              13 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)
                CALL                     2

 696            LOAD_ATTR               21 (limit + NULL|self)
                LOAD_SMALL_INT           2
                CALL                     1

 697            LOAD_ATTR               23 (execute + NULL|self)
                CALL                     0

 691            STORE_FAST               5 (result)
                JUMP_FORWARD           117 (to L7)

 701    L6:     LOAD_FAST_BORROW         3 (db)
                LOAD_ATTR                9 (table + NULL|self)
                LOAD_GLOBAL             10 (_TABLE)
                CALL                     1

 702            LOAD_ATTR               13 (select + NULL|self)
                LOAD_CONST              11 (',')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_GLOBAL             16 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 703            LOAD_ATTR               19 (eq + NULL|self)
                LOAD_CONST              13 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)
                CALL                     2

 704            LOAD_ATTR               25 (order + NULL|self)
                LOAD_CONST              14 ('requested_at')
                LOAD_CONST              15 (True)
                LOAD_CONST              16 (('desc',))
                CALL_KW                  2

 705            LOAD_ATTR               21 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 706            LOAD_ATTR               23 (execute + NULL|self)
                CALL                     0

 700            STORE_FAST               5 (result)

 708    L7:     LOAD_GLOBAL             27 (list + NULL)
                LOAD_GLOBAL             29 (getattr + NULL)
                LOAD_FAST_BORROW         5 (result)
                LOAD_CONST              17 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                BUILD_LIST               0
       L10:     CALL                     1
                STORE_FAST               6 (rows)

 719   L11:     LOAD_FAST                6 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L12)
                NOT_TAKEN

 721            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 722            LOAD_CONST               4 ('record')
                LOAD_CONST               1 (None)

 723            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 724            LOAD_CONST               6 ('error_code')
                LOAD_CONST              20 ('rotation_not_found_or_cross_brokerage')

 720            BUILD_MAP                4
                RETURN_VALUE

 727   L12:     LOAD_CONST               2 ('status')
                LOAD_CONST              21 ('ok')

 728            LOAD_CONST               4 ('record')
                LOAD_GLOBAL             41 (_project_row + NULL)
                LOAD_FAST                6 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1

 729            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 730            LOAD_CONST               6 ('error_code')
                LOAD_CONST               1 (None)

 726            BUILD_MAP                4
                RETURN_VALUE

  --   L13:     PUSH_EXC_INFO

 709            LOAD_GLOBAL             30 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       87 (to L18)
                NOT_TAKEN
                STORE_FAST               7 (e)

 710   L14:     LOAD_GLOBAL             32 (logger)
                LOAD_ATTR               35 (warning + NULL|self)

 711            LOAD_CONST              18 ('api_key_rotation_status read error type=')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 710            CALL                     1
                POP_TOP

 714            LOAD_CONST               2 ('status')
                LOAD_CONST               8 ('skipped')

 715            LOAD_CONST               4 ('record')
                LOAD_CONST               1 (None)

 716            LOAD_CONST               5 ('warnings')
                LOAD_CONST              19 ('db_read_failed:')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 717            LOAD_CONST               6 ('error_code')
                LOAD_CONST               9 ('api_key_rotation_store_unavailable')

 713            BUILD_MAP                4
       L15:     SWAP                     2
       L16:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L17:     LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 709   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L13 [0]
  L5 to L8 -> L13 [0]
  L9 to L11 -> L13 [0]
  L13 to L14 -> L19 [1] lasti
  L14 to L15 -> L17 [1] lasti
  L15 to L16 -> L19 [1] lasti
  L17 to L19 -> L19 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025B30, file "app/services/security/api_key_rotation.py", line 734>:
734           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

736           LOAD_CONST               2 ('Any')

734           LOAD_CONST               3 ('status')

737           LOAD_CONST               4 ('Optional[str]')

734           LOAD_CONST               5 ('limit')

738           LOAD_CONST               6 ('int')

734           LOAD_CONST               7 ('return')

739           LOAD_CONST               8 ('Dict[str, Any]')

734           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object list_api_key_rotation_events at 0x0000018C18300120, file "app/services/security/api_key_rotation.py", line 734>:
 734            RESUME                   0

 740            LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               3 (bid)

 741            LOAD_FAST_BORROW         3 (bid)
                POP_JUMP_IF_NOT_NONE    13 (to L1)
                NOT_TAKEN

 743            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 744            LOAD_CONST               3 ('rows')
                BUILD_LIST               0

 745            LOAD_CONST               4 ('count')
                LOAD_SMALL_INT           0

 746            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 747            LOAD_CONST               6 ('error_code')
                LOAD_CONST               7 ('missing_brokerage_id')

 742            BUILD_MAP                5
                RETURN_VALUE

 749    L1:     LOAD_FAST_BORROW         1 (status)
                POP_JUMP_IF_NONE        24 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (status)
                LOAD_GLOBAL              2 (ALLOWED_ROTATION_STATUSES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       13 (to L2)
                NOT_TAKEN

 751            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 752            LOAD_CONST               3 ('rows')
                BUILD_LIST               0

 753            LOAD_CONST               4 ('count')
                LOAD_SMALL_INT           0

 754            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 755            LOAD_CONST               6 ('error_code')
                LOAD_CONST               8 ('invalid_status')

 750            BUILD_MAP                5
                RETURN_VALUE

 757    L2:     NOP

 758    L3:     LOAD_GLOBAL              5 (max + NULL)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              7 (min + NULL)
                LOAD_GLOBAL              9 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (limit)
                LOAD_GLOBAL             10 (int)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L4)
                NOT_TAKEN
                LOAD_GLOBAL             11 (int + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1
                JUMP_FORWARD             5 (to L5)
        L4:     LOAD_GLOBAL             12 (_DEFAULT_LIMIT)
        L5:     LOAD_GLOBAL             14 (_LIST_HARD_CAP)
                CALL                     2
                CALL                     2
                STORE_FAST               4 (capped)

 761    L6:     LOAD_GLOBAL             21 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               5 (db)

 762            LOAD_FAST_BORROW         5 (db)
                POP_JUMP_IF_NOT_NONE    14 (to L7)
                NOT_TAKEN

 764            LOAD_CONST               1 ('status')
                LOAD_CONST               9 ('skipped')

 765            LOAD_CONST               3 ('rows')
                BUILD_LIST               0

 766            LOAD_CONST               4 ('count')
                LOAD_SMALL_INT           0

 767            LOAD_CONST               5 ('warnings')
                LOAD_CONST              10 ('api_key_rotation_store_unavailable')
                BUILD_LIST               1

 768            LOAD_CONST               6 ('error_code')
                LOAD_CONST              10 ('api_key_rotation_store_unavailable')

 763            BUILD_MAP                5
                RETURN_VALUE

 770    L7:     NOP

 772    L8:     LOAD_FAST_BORROW         5 (db)
                LOAD_ATTR               23 (table + NULL|self)
                LOAD_GLOBAL             24 (_TABLE)
                CALL                     1

 773            LOAD_ATTR               27 (select + NULL|self)
                LOAD_CONST              11 (',')
                LOAD_ATTR               29 (join + NULL|self)
                LOAD_GLOBAL             30 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 774            LOAD_ATTR               33 (eq + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)
                CALL                     2

 775            LOAD_ATTR               35 (order + NULL|self)
                LOAD_CONST              13 ('requested_at')
                LOAD_CONST              14 (True)
                LOAD_CONST              15 (('desc',))
                CALL_KW                  2

 776            LOAD_ATTR               37 (limit + NULL|self)
                LOAD_FAST_BORROW         4 (capped)
                CALL                     1

 771            STORE_FAST               6 (query)

 778            LOAD_FAST_BORROW         1 (status)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L11)
        L9:     NOT_TAKEN

 779   L10:     LOAD_FAST_BORROW         6 (query)
                LOAD_ATTR               33 (eq + NULL|self)
                LOAD_CONST               1 ('status')
                LOAD_FAST_BORROW         1 (status)
                CALL                     2
                STORE_FAST               6 (query)

 780   L11:     LOAD_FAST_BORROW         6 (query)
                LOAD_ATTR               39 (execute + NULL|self)
                CALL                     0
                STORE_FAST               7 (result)

 781            LOAD_GLOBAL             41 (list + NULL)
                LOAD_GLOBAL             43 (getattr + NULL)
                LOAD_FAST_BORROW         7 (result)
                LOAD_CONST              16 ('data')
                LOAD_CONST               0 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
       L12:     NOT_TAKEN
       L13:     POP_TOP
                BUILD_LIST               0
       L14:     CALL                     1
                STORE_FAST               8 (rows)

 782            LOAD_CONST              17 (<code object <genexpr> at 0x0000018C1812C690, file "app/services/security/api_key_rotation.py", line 782>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         8 (rows)
                GET_ITER
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      9 (p)
                SWAP                     2
       L15:     BUILD_LIST               0
                SWAP                     2
       L16:     FOR_ITER                10 (to L19)
                STORE_FAST_LOAD_FAST   153 (p, p)
       L17:     POP_JUMP_IF_NOT_NONE     3 (to L18)
                NOT_TAKEN
                JUMP_BACKWARD            8 (to L16)
       L18:     LOAD_FAST_BORROW         9 (p)
                LIST_APPEND              2
                JUMP_BACKWARD           12 (to L16)
       L19:     END_FOR
                POP_ITER
       L20:     STORE_FAST              10 (projected)
                STORE_FAST               9 (p)

 784            LOAD_CONST               1 ('status')
                LOAD_CONST              18 ('ok')

 785            LOAD_CONST               3 ('rows')
                LOAD_FAST_BORROW        10 (projected)

 786            LOAD_CONST               4 ('count')
                LOAD_GLOBAL             45 (len + NULL)
                LOAD_FAST_BORROW        10 (projected)
                CALL                     1

 787            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 788            LOAD_CONST               6 ('error_code')
                LOAD_CONST               0 (None)

 783            BUILD_MAP                5
       L21:     RETURN_VALUE

  --   L22:     PUSH_EXC_INFO

 759            LOAD_GLOBAL             16 (TypeError)
                LOAD_GLOBAL             18 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       11 (to L24)
                NOT_TAKEN
                POP_TOP

 760            LOAD_GLOBAL             12 (_DEFAULT_LIMIT)
                STORE_FAST               4 (capped)
       L23:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 281 (to L6)

 759   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L26:     SWAP                     2
                POP_TOP

 782            SWAP                     2
                STORE_FAST               9 (p)
                RERAISE                  0

  --   L27:     PUSH_EXC_INFO

 790            LOAD_GLOBAL             46 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       89 (to L32)
                NOT_TAKEN
                STORE_FAST              11 (e)

 791   L28:     LOAD_GLOBAL             48 (logger)
                LOAD_ATTR               51 (warning + NULL|self)

 792            LOAD_CONST              19 ('list_api_key_rotation_events read error type=')

 793            LOAD_GLOBAL             53 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               54 (__name__)
                FORMAT_SIMPLE

 792            BUILD_STRING             2

 791            CALL                     1
                POP_TOP

 796            LOAD_CONST               1 ('status')
                LOAD_CONST               9 ('skipped')

 797            LOAD_CONST               3 ('rows')
                BUILD_LIST               0

 798            LOAD_CONST               4 ('count')
                LOAD_SMALL_INT           0

 799            LOAD_CONST               5 ('warnings')
                LOAD_CONST              20 ('db_read_failed:')
                LOAD_GLOBAL             53 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               54 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 800            LOAD_CONST               6 ('error_code')
                LOAD_CONST              10 ('api_key_rotation_store_unavailable')

 795            BUILD_MAP                5
       L29:     SWAP                     2
       L30:     POP_EXCEPT
                LOAD_CONST               0 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RETURN_VALUE

  --   L31:     LOAD_CONST               0 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 790   L32:     RERAISE                  0

  --   L33:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L6 -> L22 [0]
  L8 to L9 -> L27 [0]
  L10 to L12 -> L27 [0]
  L13 to L15 -> L27 [0]
  L15 to L17 -> L26 [2]
  L18 to L20 -> L26 [2]
  L20 to L21 -> L27 [0]
  L22 to L23 -> L25 [1] lasti
  L24 to L25 -> L25 [1] lasti
  L26 to L27 -> L27 [0]
  L27 to L28 -> L33 [1] lasti
  L28 to L29 -> L31 [1] lasti
  L29 to L30 -> L33 [1] lasti
  L31 to L33 -> L33 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C1812C690, file "app/services/security/api_key_rotation.py", line 782>:
 782           RETURN_GENERATOR
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
```
