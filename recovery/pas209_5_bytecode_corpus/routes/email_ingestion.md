# routes/email_ingestion

- **pyc:** `app\routes\__pycache__\email_ingestion.cpython-314.pyc`
- **expected source path (absent):** `app\routes/email_ingestion.py`
- **co_filename (from bytecode):** `app/routes/email_ingestion.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** routes

## Module docstring

```
PAS164/PAS165 — Email lead ingestion routes.

Two endpoints:

    POST /email-ingestion/parse    (admin-only diagnostic)
    POST /email-ingestion/ingest   (brokerage-auth; verifies
                                    optional X-Forwarder-
                                    Signature and dedupes
                                    before queuing the
                                    pending call)

Doctrine:

* ``/parse`` is admin-only (X-Admin-Key). It returns the
  structural parser output without queuing a pending call,
  without verifying any signature, and without writing to the
  dedupe registry. Useful for operators who need to test a
  sample lead-source email before turning the brokerage's
  email forwarding rule on. NEVER returns the raw body.
* ``/ingest`` requires X-API-Key (brokerage auth). The
  brokerage scope is resolved from auth — the body is NEVER
  trusted for ``brokerage_id``. The route reads the optional
  ``X-Forwarder-Signature`` header and resolves the
  brokerage's forwarder secret from the authenticated row.
  PAS165 soft-rollout policy: missing signature / missing
  secret → ingestion still allowed with a structural
  warning. Invalid / malformed signature → ``status="failed"``.
* No Gmail OAuth, no inbox scanning, no external API call. The
  routes only see the JSON the caller posted.
* Event logging is allow-list-filtered. Forbidden keys
  (phone / email / name / subject / body / property /
  transcript / raw_payload / signature / dedupe_key) are
  NEVER written.
```

## Imports

`ALLOWED_EMAIL_LEAD_SOURCES`, `APIRouter`, `Any`, `BaseModel`, `Body`, `Depends`, `Dict`, `HTTPException`, `Header`, `Optional`, `__future__`, `annotations`, `app.db.event_logger`, `app.routes.admin`, `app.routes.portal`, `app.services.ingestion.email_forwarder_secret_store`, `app.services.ingestion.email_ingestion`, `app.services.ingestion.email_parser`, `app.services.security.rate_limit`, `check_rate_limit`, `fastapi`, `get_email_forwarder_secret`, `ingest_email_lead`, `log_event`, `logging`, `parse_email_lead`, `pydantic`, `rate_limit_public_error`, `require_admin`, `require_brokerage`, `typing`

## Classes

`EmailIngestionBody`

## Functions / methods

`__annotate__`, `_classify_ingest_event`, `_coerce_body_to_dict`, `_emit_observability`, `_emit_secret_store_observability`, `_log_event_safe`, `_public_parse_envelope`, `_resolve_forwarder_secret`, `_scrub_source_hint`, `email_ingest`, `email_parse`

## Env-key candidates

`TENANT`

## String constants (redacted where noted)

- '\nPAS164/PAS165 — Email lead ingestion routes.\n\nTwo endpoints:\n\n    POST /email-ingestion/parse    (admin-only diagnostic)\n    POST /email-ingestion/ingest   (brokerage-auth; verifies\n                                    optional X-Forwarder-\n                                    Signature and dedupes\n                                    before queuing the\n                                    pending call)\n\nDoctrine:\n\n* ``/parse`` is admin-only (X-Admin-Key). It returns the\n  structural parser output without queuing a pending call,\n  without verifying any signature, and without writing to the\n  dedupe registry. Useful for operators who need to test a\n  sample lead-source email before turning the brokerage\'s\n  email forwarding rule on. NEVER returns the raw body.\n* ``/ingest`` requires X-API-Key (brokerage auth). The\n  brokerage scope is resolved from auth — the body is NEVER\n  trusted for ``brokerage_id``. The route reads the optional\n  ``X-Forwarder-Signature`` header and resolves the\n  brokerage\'s forwarder secret from the authenticated row.\n  PAS165 soft-rollout policy: missing signature / missing\n  secret → ingestion still allowed with a structural\n  warning. Invalid / malformed signature → ``status="failed"``.\n* No Gmail OAuth, no inbox scanning, no external API call. The\n  routes only see the JSON the caller posted.\n* Event logging is allow-list-filtered. Forbidden keys\n  (phone / email / name / subject / body / property /\n  transcript / raw_payload / signature / dedupe_key) are\n  NEVER written.\n'
- 'pas.routes.email_ingestion'
- 'email_forwarder_secret'
- 'EmailIngestionBody'
- 'brokerage_id'
- 'severity'
- 'info'
- 'payload'
- '/parse'
- '/ingest'
- 'X-Forwarder-Signature'
- 'router'
- 'Shared shape for both endpoints. ``source_hint`` is\noptional and validated against the closed enum at the route\nlevel — bad hints are silently ignored, never echoed.'
- 'Optional[str]'
- 'subject'
- 'sender'
- 'body'
- 'source_hint'
- 'event_type'
- 'str'
- 'Optional[Dict[str, Any]]'
- 'return'
- 'None'
- 'Best-effort structural event write. NEVER raises. Payload\nis allow-list-filtered before write.'
- 'email_ingestion'
- 'ingestion'
- 'log_event failed (non-critical) event_type='
- ' err_type='
- 'Any'
- 'Dict[str, Any]'
- 'Coerce the request body into a dict the parser can read.\n\nAccepts the typed ``EmailIngestionBody`` model OR a free-\nform dict (FastAPI will hand back the model when validated).\nNEVER raises.\n'
- 'model_dump'
- 'hint'
- 'brokerage'
- "Resolve the brokerage's forwarder secret via the PAS167\nsecret-store helper. Returns the helper's full structural\nenvelope so the route can react to a decrypt failure and\nfire the appropriate observability events.\n\nThe caller MUST treat the returned ``secret`` field as\nin-process only — it never leaves this module. NEVER\nraises. NEVER echoes the secret in errors / warnings."
- 'status'
- 'missing'
- 'secret'
- 'encryption_enabled'
- 'plaintext_fallback'
- 'migration_status'
- 'warnings'
- 'error_code'
- 'parsed'
- "Project the parser's full envelope into the public response\nshape exposed by ``/parse``. The parsed lead's identifying\nfields (phone / email / name / property) are intentionally\nsuppressed in the public response — admins who need them\nshould consult the source email directly."
- 'failed'
- 'source'
- 'generic_email'
- 'call_eligible'
- 'errors'
- 'parser_returned_non_dict'
- 'lead'
- 'phone'
- 'email'
- 'has_phone'
- 'has_email'
- 'result'
- 'Pick the structural outcome event type for an ingest\nresult.\n\nOutcome map:\n  * status="duplicate" → email.lead.duplicate\n  * status="failed" with required-policy error\n    → email.forwarder.signature_required_missing\n  * status="failed" with secret-missing error\n    → email.forwarder.secret_missing\n  * status="failed" with other forwarder_signature_* error\n    → email.forwarder.signature_invalid\n  * status="failed" otherwise → email.lead.failed\n  * status="accepted" + call_eligible → email.lead.ingested\n  * status="accepted" + not call_eligible\n    → email.lead.not_call_eligible\n\nSoft-rollout / dedupe observability events fire IN ADDITION\nto the outcome event — see ``_emit_observability``.\n'
- 'duplicate'
- 'email.lead.duplicate'
- 'accepted'
- 'email.lead.ingested'
- 'email.lead.not_call_eligible'
- 'forwarder_signature_required'
- 'email.forwarder.signature_required_missing'
- 'forwarder_secret_missing'
- 'email.forwarder.secret_missing'
- 'forwarder_signature'
- 'email.forwarder.signature_invalid'
- 'email.lead.failed'
- 'Emit the soft-rollout forwarder events + the PAS166\ndurable-dedupe observability events based on the\ningestion-service warnings + flags. The outcome event is\nemitted separately by the caller.'
- 'forwarder_verified'
- 'forwarder_required'
- 'dedupe_durable'
- 'warning_count'
- 'forwarder_signature_unconfigured'
- 'email.forwarder.signature_unconfigured'
- 'forwarder_signature_missing'
- 'email.forwarder.signature_missing'
- 'email.forwarder.verified'
- 'email_dedupe_fallback_process_local'
- 'email.dedupe.fallback_process_local'
- 'warning'
- 'email.dedupe.durable_registered'
- 'email.dedupe.durable_duplicate'
- 'secret_env'
- 'Emit the PAS167 secret-store observability events based\non the secret-store envelope. Payload is structural only.'
- 'email.forwarder.secret.plaintext_fallback'
- 'email.forwarder.secret.encrypted'
- 'email.forwarder.secret.decrypt_failed'
- 'bool'
- 'Admin-only diagnostic parser. Runs the email parser\nagainst the supplied subject / sender / body and returns the\nstructural envelope WITHOUT queuing a pending call, without\nverifying any signature, and without touching the dedupe\nregistry.\n\nNEVER returns the raw body, the parsed phone / email / name,\nor any identifying field. Use ``/ingest`` for production\nflow.\n'
- 'email.lead.parsed'
- 'none'
- 'x_forwarder_signature'
- 'TENANT'
- 'allowed'
- 'Invalid brokerage auth'
- 'lead_id'
- 'pending_call_id'
- 'call_queued'
- 'forwarder_secret_decrypt_failed'
- 'service_returned_non_dict'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS164/PAS165 — Email lead ingestion routes.\n\nTwo endpoints:\n\n    POST /email-ingestion/parse    (admin-only diagnostic)\n    POST /email-ingestion/ingest   (brokerage-auth; verifies\n                                    optional X-Forwarder-\n                                    Signature and dedupes\n                                    before queuing the\n                                    pending call)\n\nDoctrine:\n\n* ``/parse`` is admin-only (X-Admin-Key). It returns the\n  structural parser output without queuing a pending call,\n  without verifying any signature, and without writing to the\n  dedupe registry. Useful for operators who need to test a\n  sample lead-source email before turning the brokerage\'s\n  email forwarding rule on. NEVER returns the raw body.\n* ``/ingest`` requires X-API-Key (brokerage auth). The\n  brokerage scope is resolved from auth — the body is NEVER\n  trusted for ``brokerage_id``. The route reads the optional\n  ``X-Forwarder-Signature`` header and resolves the\n  brokerage\'s forwarder secret from the authenticated row.\n  PAS165 soft-rollout policy: missing signature / missing\n  secret → ingestion still allowed with a structural\n  warning. Invalid / malformed signature → ``status="failed"``.\n* No Gmail OAuth, no inbox scanning, no external API call. The\n  routes only see the JSON the caller posted.\n* Event logging is allow-list-filtered. Forbidden keys\n  (phone / email / name / subject / body / property /\n  transcript / raw_payload / signature / dedupe_key) are\n  NEVER written.\n')
              STORE_NAME               0 (__doc__)

 37           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 39           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 40           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (Optional)
              STORE_NAME               7 (Optional)
              POP_TOP

 42           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('APIRouter', 'Body', 'Depends', 'Header', 'HTTPException'))
              IMPORT_NAME              8 (fastapi)
              IMPORT_FROM              9 (APIRouter)
              STORE_NAME               9 (APIRouter)
              IMPORT_FROM             10 (Body)
              STORE_NAME              10 (Body)
              IMPORT_FROM             11 (Depends)
              STORE_NAME              11 (Depends)
              IMPORT_FROM             12 (Header)
              STORE_NAME              12 (Header)
              IMPORT_FROM             13 (HTTPException)
              STORE_NAME              13 (HTTPException)
              POP_TOP

 43           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('BaseModel',))
              IMPORT_NAME             14 (pydantic)
              IMPORT_FROM             15 (BaseModel)
              STORE_NAME              15 (BaseModel)
              POP_TOP

 45           LOAD_SMALL_INT           0
              LOAD_CONST               6 (('require_admin',))
              IMPORT_NAME             16 (app.routes.admin)
              IMPORT_FROM             17 (require_admin)
              STORE_NAME              17 (require_admin)
              POP_TOP

 46           LOAD_SMALL_INT           0
              LOAD_CONST               7 (('require_brokerage',))
              IMPORT_NAME             18 (app.routes.portal)
              IMPORT_FROM             19 (require_brokerage)
              STORE_NAME              19 (require_brokerage)
              POP_TOP

 47           LOAD_SMALL_INT           0
              LOAD_CONST               8 (('get_email_forwarder_secret',))
              IMPORT_NAME             20 (app.services.ingestion.email_forwarder_secret_store)
              IMPORT_FROM             21 (get_email_forwarder_secret)
              STORE_NAME              21 (get_email_forwarder_secret)
              POP_TOP

 50           LOAD_SMALL_INT           0
              LOAD_CONST               9 (('ingest_email_lead',))
              IMPORT_NAME             22 (app.services.ingestion.email_ingestion)
              IMPORT_FROM             23 (ingest_email_lead)
              STORE_NAME              23 (ingest_email_lead)
              POP_TOP

 51           LOAD_SMALL_INT           0
              LOAD_CONST              10 (('ALLOWED_EMAIL_LEAD_SOURCES', 'parse_email_lead'))
              IMPORT_NAME             24 (app.services.ingestion.email_parser)
              IMPORT_FROM             25 (ALLOWED_EMAIL_LEAD_SOURCES)
              STORE_NAME              25 (ALLOWED_EMAIL_LEAD_SOURCES)
              IMPORT_FROM             26 (parse_email_lead)
              STORE_NAME              26 (parse_email_lead)
              POP_TOP

 57           LOAD_NAME                9 (APIRouter)
              PUSH_NULL
              CALL                     0
              STORE_NAME              27 (router)

 58           LOAD_NAME                3 (logging)
              LOAD_ATTR               56 (getLogger)
              PUSH_NULL
              LOAD_CONST              11 ('pas.routes.email_ingestion')
              CALL                     1
              STORE_NAME              29 (logger)

 66           LOAD_CONST              46 (('source', 'has_phone', 'has_email', 'call_eligible', 'call_queued', 'warning_count', 'error_code', 'forwarder_verified', 'forwarder_required', 'dedupe_durable', 'duplicate', 'encryption_enabled', 'plaintext_fallback', 'dry_run', 'deleted_count', 'limit', 'older_than_hours', 'rotated_count', 'skipped_count', 'failed_count', 'kid'))
              STORE_NAME              30 (_EVENT_PAYLOAD_ALLOWED)

102           LOAD_CONST              12 ('email_forwarder_secret')
              STORE_NAME              31 (_FORWARDER_SECRET_FIELD)

103           LOAD_CONST              47 (('features', 'config'))
              STORE_NAME              32 (_FORWARDER_SECRET_NEST_KEYS)

110           LOAD_BUILD_CLASS
              PUSH_NULL
              LOAD_CONST              13 (<code object EmailIngestionBody at 0x0000018C1802C620, file "app/routes/email_ingestion.py", line 110>)
              MAKE_FUNCTION
              LOAD_CONST              14 ('EmailIngestionBody')
              LOAD_NAME               15 (BaseModel)
              CALL                     3
              STORE_NAME              33 (EmailIngestionBody)

124           LOAD_CONST              15 ('brokerage_id')

127           LOAD_CONST               2 (None)

124           LOAD_CONST              16 ('severity')

128           LOAD_CONST              17 ('info')

124           LOAD_CONST              18 ('payload')

129           LOAD_CONST               2 (None)

124           BUILD_MAP                3
              LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18025D30, file "app/routes/email_ingestion.py", line 124>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _log_event_safe at 0x0000018C17E93C90, file "app/routes/email_ingestion.py", line 124>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              34 (_log_event_safe)

162           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA3960, file "app/routes/email_ingestion.py", line 162>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _coerce_body_to_dict at 0x0000018C17F01670, file "app/routes/email_ingestion.py", line 162>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              35 (_coerce_body_to_dict)

183           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA2970, file "app/routes/email_ingestion.py", line 183>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object _scrub_source_hint at 0x0000018C18053870, file "app/routes/email_ingestion.py", line 183>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              36 (_scrub_source_hint)

191           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA23D0, file "app/routes/email_ingestion.py", line 191>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object _resolve_forwarder_secret at 0x0000018C18038670, file "app/routes/email_ingestion.py", line 191>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              37 (_resolve_forwarder_secret)

213           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA2100, file "app/routes/email_ingestion.py", line 213>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object _public_parse_envelope at 0x0000018C17ED0560, file "app/routes/email_ingestion.py", line 213>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              38 (_public_parse_envelope)

241           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA2B50, file "app/routes/email_ingestion.py", line 241>)
              MAKE_FUNCTION
              LOAD_CONST              30 (<code object _classify_ingest_event at 0x0000018C17EC57C0, file "app/routes/email_ingestion.py", line 241>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              39 (_classify_ingest_event)

280           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C18025030, file "app/routes/email_ingestion.py", line 280>)
              MAKE_FUNCTION
              LOAD_CONST              32 (<code object _emit_observability at 0x0000018C17ED94C0, file "app/routes/email_ingestion.py", line 280>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              40 (_emit_observability)

346           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C18025A30, file "app/routes/email_ingestion.py", line 346>)
              MAKE_FUNCTION
              LOAD_CONST              34 (<code object _emit_secret_store_observability at 0x0000018C17ED9FB0, file "app/routes/email_ingestion.py", line 346>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              41 (_emit_secret_store_observability)

405           LOAD_NAME               27 (router)
              LOAD_ATTR               85 (post + NULL|self)
              LOAD_CONST              35 ('/parse')
              CALL                     1

407           LOAD_NAME               10 (Body)
              PUSH_NULL
              LOAD_CONST              36 (Ellipsis)
              CALL                     1

408           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               17 (require_admin)
              CALL                     1

406           BUILD_TUPLE              2
              LOAD_CONST              37 (<code object __annotate__ at 0x0000018C17FA32D0, file "app/routes/email_ingestion.py", line 406>)
              MAKE_FUNCTION
              LOAD_CONST              38 (<code object email_parse at 0x0000018C17EDA310, file "app/routes/email_ingestion.py", line 405>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

405           CALL                     0

406           STORE_NAME              43 (email_parse)

445           LOAD_NAME               27 (router)
              LOAD_ATTR               85 (post + NULL|self)
              LOAD_CONST              39 ('/ingest')
              CALL                     1

447           LOAD_NAME               10 (Body)
              PUSH_NULL
              LOAD_CONST              36 (Ellipsis)
              CALL                     1

448           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               19 (require_brokerage)
              CALL                     1

449           LOAD_NAME               12 (Header)
              PUSH_NULL

450           LOAD_CONST               2 (None)

451           LOAD_CONST              40 ('X-Forwarder-Signature')

452           LOAD_CONST              41 (False)

449           LOAD_CONST              42 (('default', 'alias', 'convert_underscores'))
              CALL_KW                  3

446           BUILD_TUPLE              3
              LOAD_CONST              43 (<code object __annotate__ at 0x0000018C18024C30, file "app/routes/email_ingestion.py", line 446>)
              MAKE_FUNCTION
              LOAD_CONST              44 (<code object email_ingest at 0x0000018C17ED3710, file "app/routes/email_ingestion.py", line 445>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

445           CALL                     0

446           STORE_NAME              44 (email_ingest)

623           LOAD_CONST              45 ('router')
              BUILD_LIST               1
              STORE_NAME              45 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object EmailIngestionBody at 0x0000018C1802C620, file "app/routes/email_ingestion.py", line 110>:
110           RESUME                   0
              LOAD_NAME                0 (__name__)
              STORE_NAME               1 (__module__)
              LOAD_CONST               0 ('EmailIngestionBody')
              STORE_NAME               2 (__qualname__)
              LOAD_SMALL_INT         110
              STORE_NAME               3 (__firstlineno__)
              SETUP_ANNOTATIONS

111           LOAD_CONST               1 ('Shared shape for both endpoints. ``source_hint`` is\noptional and validated against the closed enum at the route\nlevel — bad hints are silently ignored, never echoed.')
              STORE_NAME               4 (__doc__)

114           LOAD_CONST               2 (None)
              STORE_NAME               5 (subject)
              LOAD_CONST               3 ('Optional[str]')
              LOAD_NAME                6 (__annotations__)
              LOAD_CONST               4 ('subject')
              STORE_SUBSCR

115           LOAD_CONST               2 (None)
              STORE_NAME               7 (sender)
              LOAD_CONST               3 ('Optional[str]')
              LOAD_NAME                6 (__annotations__)
              LOAD_CONST               5 ('sender')
              STORE_SUBSCR

116           LOAD_CONST               2 (None)
              STORE_NAME               8 (body)
              LOAD_CONST               3 ('Optional[str]')
              LOAD_NAME                6 (__annotations__)
              LOAD_CONST               6 ('body')
              STORE_SUBSCR

117           LOAD_CONST               2 (None)
              STORE_NAME               9 (source_hint)
              LOAD_CONST               3 ('Optional[str]')
              LOAD_NAME                6 (__annotations__)
              LOAD_CONST               7 ('source_hint')
              STORE_SUBSCR
              LOAD_CONST               8 (())
              STORE_NAME              10 (__static_attributes__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app/routes/email_ingestion.py", line 124>:
124           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('event_type')

125           LOAD_CONST               2 ('str')

124           LOAD_CONST               3 ('brokerage_id')

127           LOAD_CONST               4 ('Optional[str]')

124           LOAD_CONST               5 ('severity')

128           LOAD_CONST               2 ('str')

124           LOAD_CONST               6 ('payload')

129           LOAD_CONST               7 ('Optional[Dict[str, Any]]')

124           LOAD_CONST               8 ('return')

130           LOAD_CONST               9 ('None')

124           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _log_event_safe at 0x0000018C17E93C90, file "app/routes/email_ingestion.py", line 124>:
 124            RESUME                   0

 133            NOP

 134    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('log_event',))
                IMPORT_NAME              0 (app.db.event_logger)
                IMPORT_FROM              1 (log_event)
                STORE_FAST               4 (log_event)
                POP_TOP

 137    L2:     BUILD_MAP                0
                STORE_FAST               5 (safe_payload)

 138            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST                3 (payload)
                LOAD_GLOBAL              8 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       32 (to L6)
                NOT_TAKEN

 139            LOAD_GLOBAL             10 (_EVENT_PAYLOAD_ALLOWED)
                GET_ITER
        L3:     FOR_ITER                21 (to L5)
                STORE_FAST               6 (k)

 140            LOAD_FAST_LOAD_FAST     99 (k, payload)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L3)

 141    L4:     LOAD_FAST_LOAD_FAST     54 (payload, k)
                BINARY_OP               26 ([])
                LOAD_FAST_LOAD_FAST     86 (safe_payload, k)
                STORE_SUBSCR
                JUMP_BACKWARD           23 (to L3)

 139    L5:     END_FOR
                POP_ITER

 142    L6:     NOP

 143    L7:     LOAD_FAST                4 (log_event)
                PUSH_NULL

 144            LOAD_FAST                0 (event_type)

 145            LOAD_FAST                1 (brokerage_id)

 146            LOAD_FAST                2 (severity)

 147            LOAD_FAST                5 (safe_payload)

 148            LOAD_CONST               3 ('email_ingestion')

 149            LOAD_CONST               4 ('ingestion')

 143            LOAD_CONST               5 (('brokerage_id', 'severity', 'payload', 'event_source', 'event_category'))
                CALL_KW                  6
                POP_TOP
        L8:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L9:     PUSH_EXC_INFO

 135            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L11)
                NOT_TAKEN
                POP_TOP

 136   L10:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 135   L11:     RERAISE                  0

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L13:     PUSH_EXC_INFO

 151            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       58 (to L17)
                NOT_TAKEN
                STORE_FAST               7 (e)

 152   L14:     LOAD_GLOBAL             12 (logger)
                LOAD_ATTR               15 (warning + NULL|self)

 153            LOAD_CONST               6 ('log_event failed (non-critical) event_type=')
                LOAD_FAST                0 (event_type)
                FORMAT_SIMPLE
                LOAD_CONST               7 (' err_type=')

 154            LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE

 153            BUILD_STRING             4

 152            CALL                     1
                POP_TOP
       L15:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L16:     LOAD_CONST               2 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 151   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L9 [0]
  L7 to L8 -> L13 [0]
  L9 to L10 -> L12 [1] lasti
  L11 to L12 -> L12 [1] lasti
  L13 to L14 -> L18 [1] lasti
  L14 to L15 -> L16 [1] lasti
  L16 to L18 -> L18 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app/routes/email_ingestion.py", line 162>:
162           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _coerce_body_to_dict at 0x0000018C17F01670, file "app/routes/email_ingestion.py", line 162>:
162           RESUME                   0

169           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (body)
              LOAD_GLOBAL              2 (EmailIngestionBody)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       52 (to L3)
              NOT_TAKEN

170           LOAD_GLOBAL              5 (hasattr + NULL)
              LOAD_FAST_BORROW         0 (body)
              LOAD_CONST               1 ('model_dump')
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (body)
              LOAD_ATTR                7 (model_dump + NULL|self)
              CALL                     0
              JUMP_FORWARD            15 (to L2)
      L1:     LOAD_FAST_BORROW         0 (body)
              LOAD_ATTR                9 (dict + NULL|self)
              CALL                     0
      L2:     STORE_FAST               1 (d)
              JUMP_FORWARD            27 (to L5)

171   L3:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (body)
              LOAD_GLOBAL              8 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        4 (to L4)
              NOT_TAKEN

172           LOAD_FAST                0 (body)
              STORE_FAST               1 (d)
              JUMP_FORWARD             2 (to L5)

174   L4:     BUILD_MAP                0
              RETURN_VALUE

176   L5:     LOAD_CONST               2 ('subject')
              LOAD_FAST_BORROW         1 (d)
              LOAD_ATTR               11 (get + NULL|self)
              LOAD_CONST               2 ('subject')
              CALL                     1

177           LOAD_CONST               3 ('sender')
              LOAD_FAST_BORROW         1 (d)
              LOAD_ATTR               11 (get + NULL|self)
              LOAD_CONST               3 ('sender')
              CALL                     1

178           LOAD_CONST               4 ('body')
              LOAD_FAST_BORROW         1 (d)
              LOAD_ATTR               11 (get + NULL|self)
              LOAD_CONST               4 ('body')
              CALL                     1

175           BUILD_MAP                3
              STORE_FAST               2 (out)

180           LOAD_FAST_BORROW         2 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app/routes/email_ingestion.py", line 183>:
183           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('hint')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _scrub_source_hint at 0x0000018C18053870, file "app/routes/email_ingestion.py", line 183>:
183           RESUME                   0

184           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (hint)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

185           LOAD_CONST               0 (None)
              RETURN_VALUE

186   L1:     LOAD_FAST_BORROW         0 (hint)
              LOAD_GLOBAL              4 (ALLOWED_EMAIL_LEAD_SOURCES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

187           LOAD_CONST               0 (None)
              RETURN_VALUE

188   L2:     LOAD_FAST_BORROW         0 (hint)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app/routes/email_ingestion.py", line 191>:
191           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _resolve_forwarder_secret at 0x0000018C18038670, file "app/routes/email_ingestion.py", line 191>:
191           RESUME                   0

200           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        17 (to L1)
              NOT_TAKEN

202           LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('missing')

203           LOAD_CONST               3 ('secret')
              LOAD_CONST               4 (None)

204           LOAD_CONST               5 ('encryption_enabled')
              LOAD_CONST               6 (False)

205           LOAD_CONST               7 ('plaintext_fallback')
              LOAD_CONST               6 (False)

206           LOAD_CONST               8 ('migration_status')
              LOAD_CONST               4 (None)

207           LOAD_CONST               9 ('warnings')
              BUILD_LIST               0

208           LOAD_CONST              10 ('error_code')
              LOAD_CONST               4 (None)

201           BUILD_MAP                7
              RETURN_VALUE

210   L1:     LOAD_GLOBAL              5 (get_email_forwarder_secret + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app/routes/email_ingestion.py", line 213>:
213           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('parsed')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _public_parse_envelope at 0x0000018C17ED0560, file "app/routes/email_ingestion.py", line 213>:
213           RESUME                   0

219           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (parsed)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        14 (to L1)
              NOT_TAKEN

221           LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('failed')

222           LOAD_CONST               3 ('source')
              LOAD_CONST               4 ('generic_email')

223           LOAD_CONST               5 ('call_eligible')
              LOAD_CONST               6 (False)

224           LOAD_CONST               7 ('warnings')
              BUILD_LIST               0

225           LOAD_CONST               8 ('errors')
              LOAD_CONST               9 ('parser_returned_non_dict')
              BUILD_LIST               1

220           BUILD_MAP                5
              RETURN_VALUE

227   L1:     LOAD_FAST_BORROW         0 (parsed)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST              10 ('lead')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L2:     STORE_FAST               1 (lead_dict)

228           LOAD_GLOBAL              7 (bool + NULL)
              LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (lead_dict)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L3)
              NOT_TAKEN
              POP_TOP
              LOAD_FAST_BORROW         1 (lead_dict)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST              11 ('phone')
              CALL                     1
      L3:     CALL                     1
              STORE_FAST               2 (has_phone)

229           LOAD_GLOBAL              7 (bool + NULL)
              LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (lead_dict)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L4)
              NOT_TAKEN
              POP_TOP
              LOAD_FAST_BORROW         1 (lead_dict)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST              12 ('email')
              CALL                     1
      L4:     CALL                     1
              STORE_FAST               3 (has_email)

231           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         0 (parsed)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('status')
              CALL                     1

232           LOAD_CONST               3 ('source')
              LOAD_FAST_BORROW         0 (parsed)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               3 ('source')
              CALL                     1

233           LOAD_CONST               5 ('call_eligible')
              LOAD_GLOBAL              7 (bool + NULL)
              LOAD_FAST_BORROW         0 (parsed)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               5 ('call_eligible')
              CALL                     1
              CALL                     1

234           LOAD_CONST              13 ('has_phone')
              LOAD_FAST                2 (has_phone)

235           LOAD_CONST              14 ('has_email')
              LOAD_FAST                3 (has_email)

236           LOAD_CONST               7 ('warnings')
              LOAD_GLOBAL              9 (list + NULL)
              LOAD_FAST_BORROW         0 (parsed)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               7 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L5:     CALL                     1

237           LOAD_CONST               8 ('errors')
              LOAD_GLOBAL              9 (list + NULL)
              LOAD_FAST_BORROW         0 (parsed)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               8 ('errors')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L6:     CALL                     1

230           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app/routes/email_ingestion.py", line 241>:
241           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('result')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _classify_ingest_event at 0x0000018C17EC57C0, file "app/routes/email_ingestion.py", line 241>:
241           RESUME                   0

261           LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('status')
              CALL                     1
              STORE_FAST               1 (status)

262           LOAD_FAST_BORROW         1 (status)
              LOAD_CONST               2 ('duplicate')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

263           LOAD_CONST               3 ('email.lead.duplicate')
              RETURN_VALUE

264   L1:     LOAD_FAST_BORROW         1 (status)
              LOAD_CONST               4 ('accepted')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       37 (to L3)
              NOT_TAKEN

265           LOAD_GLOBAL              3 (bool + NULL)
              LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               5 ('call_eligible')
              CALL                     1
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

266           LOAD_CONST               6 ('email.lead.ingested')
              RETURN_VALUE

267   L2:     LOAD_CONST               7 ('email.lead.not_call_eligible')
              RETURN_VALUE

269   L3:     LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               8 ('errors')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L4:     STORE_FAST               2 (errors)

270           LOAD_FAST_BORROW         2 (errors)
              TO_BOOL
              POP_JUMP_IF_FALSE       10 (to L5)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (errors)
              LOAD_SMALL_INT           0
              BINARY_OP               26 ([])
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               9 ('')
      L6:     STORE_FAST               3 (err)

271           LOAD_FAST_BORROW         3 (err)
              LOAD_CONST              10 ('forwarder_signature_required')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L7)
              NOT_TAKEN

272           LOAD_CONST              11 ('email.forwarder.signature_required_missing')
              RETURN_VALUE

273   L7:     LOAD_FAST_BORROW         3 (err)
              LOAD_CONST              12 ('forwarder_secret_missing')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L8)
              NOT_TAKEN

274           LOAD_CONST              13 ('email.forwarder.secret_missing')
              RETURN_VALUE

275   L8:     LOAD_FAST_BORROW         3 (err)
              LOAD_ATTR                5 (startswith + NULL|self)
              LOAD_CONST              14 ('forwarder_signature')
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L9)
              NOT_TAKEN

276           LOAD_CONST              15 ('email.forwarder.signature_invalid')
              RETURN_VALUE

277   L9:     LOAD_CONST              16 ('email.lead.failed')
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "app/routes/email_ingestion.py", line 280>:
280           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('result')

281           LOAD_CONST               2 ('Dict[str, Any]')

280           LOAD_CONST               3 ('brokerage_id')

283           LOAD_CONST               4 ('str')

280           LOAD_CONST               5 ('return')

284           LOAD_CONST               6 ('None')

280           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _emit_observability at 0x0000018C17ED94C0, file "app/routes/email_ingestion.py", line 280>:
280           RESUME                   0

289           LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               1 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1
              STORE_FAST               2 (warnings)

291           LOAD_CONST               2 ('source')
              LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               2 ('source')
              CALL                     1

292           LOAD_CONST               3 ('forwarder_verified')
              LOAD_GLOBAL              5 (bool + NULL)
              LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               3 ('forwarder_verified')
              CALL                     1
              CALL                     1

293           LOAD_CONST               4 ('forwarder_required')
              LOAD_GLOBAL              5 (bool + NULL)
              LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               4 ('forwarder_required')
              CALL                     1
              CALL                     1

294           LOAD_CONST               5 ('dedupe_durable')
              LOAD_GLOBAL              5 (bool + NULL)
              LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               5 ('dedupe_durable')
              CALL                     1
              CALL                     1

295           LOAD_CONST               6 ('warning_count')
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         2 (warnings)
              CALL                     1

290           BUILD_MAP                5
              STORE_FAST               3 (payload)

298           LOAD_CONST               7 ('forwarder_signature_unconfigured')
              LOAD_FAST_BORROW         2 (warnings)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       16 (to L2)
              NOT_TAKEN

299           LOAD_GLOBAL              9 (_log_event_safe + NULL)

300           LOAD_CONST               8 ('email.forwarder.signature_unconfigured')

301           LOAD_FAST_BORROW         1 (brokerage_id)

302           LOAD_CONST               9 ('info')

303           LOAD_FAST_BORROW         3 (payload)

299           LOAD_CONST              10 (('brokerage_id', 'severity', 'payload'))
              CALL_KW                  4
              POP_TOP

305   L2:     LOAD_CONST              11 ('forwarder_signature_missing')
              LOAD_FAST_BORROW         2 (warnings)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       16 (to L3)
              NOT_TAKEN

306           LOAD_GLOBAL              9 (_log_event_safe + NULL)

307           LOAD_CONST              12 ('email.forwarder.signature_missing')

308           LOAD_FAST_BORROW         1 (brokerage_id)

309           LOAD_CONST               9 ('info')

310           LOAD_FAST_BORROW         3 (payload)

306           LOAD_CONST              10 (('brokerage_id', 'severity', 'payload'))
              CALL_KW                  4
              POP_TOP

312   L3:     LOAD_GLOBAL              5 (bool + NULL)
              LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               3 ('forwarder_verified')
              CALL                     1
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       16 (to L4)
              NOT_TAKEN

313           LOAD_GLOBAL              9 (_log_event_safe + NULL)

314           LOAD_CONST              13 ('email.forwarder.verified')

315           LOAD_FAST_BORROW         1 (brokerage_id)

316           LOAD_CONST               9 ('info')

317           LOAD_FAST_BORROW         3 (payload)

313           LOAD_CONST              10 (('brokerage_id', 'severity', 'payload'))
              CALL_KW                  4
              POP_TOP

320   L4:     LOAD_CONST              14 ('email_dedupe_fallback_process_local')
              LOAD_FAST_BORROW         2 (warnings)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       16 (to L5)
              NOT_TAKEN

321           LOAD_GLOBAL              9 (_log_event_safe + NULL)

322           LOAD_CONST              15 ('email.dedupe.fallback_process_local')

323           LOAD_FAST_BORROW         1 (brokerage_id)

324           LOAD_CONST              16 ('warning')

325           LOAD_FAST_BORROW         3 (payload)

321           LOAD_CONST              10 (('brokerage_id', 'severity', 'payload'))
              CALL_KW                  4
              POP_TOP

327   L5:     LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              17 ('status')
              CALL                     1
              LOAD_CONST              18 ('accepted')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       48 (to L6)
              NOT_TAKEN
              LOAD_GLOBAL              5 (bool + NULL)
              LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               5 ('dedupe_durable')
              CALL                     1
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       16 (to L6)
              NOT_TAKEN

328           LOAD_GLOBAL              9 (_log_event_safe + NULL)

329           LOAD_CONST              19 ('email.dedupe.durable_registered')

330           LOAD_FAST_BORROW         1 (brokerage_id)

331           LOAD_CONST               9 ('info')

332           LOAD_FAST_BORROW         3 (payload)

328           LOAD_CONST              10 (('brokerage_id', 'severity', 'payload'))
              CALL_KW                  4
              POP_TOP

335   L6:     LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              17 ('status')
              CALL                     1
              LOAD_CONST              20 ('duplicate')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       52 (to L8)
              NOT_TAKEN

336           LOAD_GLOBAL              5 (bool + NULL)
              LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               5 ('dedupe_durable')
              CALL                     1
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L7)
              NOT_TAKEN

338           LOAD_GLOBAL              9 (_log_event_safe + NULL)

339           LOAD_CONST              21 ('email.dedupe.durable_duplicate')

340           LOAD_FAST_BORROW         1 (brokerage_id)

341           LOAD_CONST               9 ('info')

342           LOAD_FAST_BORROW         3 (payload)

338           LOAD_CONST              10 (('brokerage_id', 'severity', 'payload'))
              CALL_KW                  4
              POP_TOP
              LOAD_CONST              22 (None)
              RETURN_VALUE

336   L7:     LOAD_CONST              22 (None)
              RETURN_VALUE

335   L8:     LOAD_CONST              22 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app/routes/email_ingestion.py", line 346>:
346           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('secret_env')

347           LOAD_CONST               2 ('Dict[str, Any]')

346           LOAD_CONST               3 ('brokerage_id')

349           LOAD_CONST               4 ('str')

346           LOAD_CONST               5 ('return')

350           LOAD_CONST               6 ('None')

346           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _emit_secret_store_observability at 0x0000018C17ED9FB0, file "app/routes/email_ingestion.py", line 346>:
346           RESUME                   0

353           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (secret_env)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

354           LOAD_CONST               1 (None)
              RETURN_VALUE

356   L1:     LOAD_CONST               2 ('encryption_enabled')
              LOAD_GLOBAL              5 (bool + NULL)
              LOAD_FAST_BORROW         0 (secret_env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               2 ('encryption_enabled')
              CALL                     1
              CALL                     1

357           LOAD_CONST               3 ('plaintext_fallback')
              LOAD_GLOBAL              5 (bool + NULL)
              LOAD_FAST_BORROW         0 (secret_env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               3 ('plaintext_fallback')
              CALL                     1
              CALL                     1

358           LOAD_CONST               4 ('warning_count')
              LOAD_GLOBAL              9 (len + NULL)
              LOAD_FAST_BORROW         0 (secret_env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               5 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L2:     CALL                     1

355           BUILD_MAP                3
              STORE_FAST               2 (payload)

360           LOAD_FAST_BORROW         0 (secret_env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               6 ('status')
              CALL                     1
              LOAD_CONST               7 ('ok')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE      101 (to L5)
              NOT_TAKEN

361           LOAD_GLOBAL              5 (bool + NULL)
              LOAD_FAST_BORROW         0 (secret_env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               3 ('plaintext_fallback')
              CALL                     1
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L3)
              NOT_TAKEN

362           LOAD_GLOBAL             11 (_log_event_safe + NULL)

363           LOAD_CONST               8 ('email.forwarder.secret.plaintext_fallback')

364           LOAD_FAST_BORROW         1 (brokerage_id)

365           LOAD_CONST               9 ('warning')

366           LOAD_FAST_BORROW         2 (payload)

362           LOAD_CONST              10 (('brokerage_id', 'severity', 'payload'))
              CALL_KW                  4
              POP_TOP
              LOAD_CONST               1 (None)
              RETURN_VALUE

368   L3:     LOAD_GLOBAL              5 (bool + NULL)
              LOAD_FAST_BORROW         0 (secret_env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               2 ('encryption_enabled')
              CALL                     1
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L4)
              NOT_TAKEN

369           LOAD_GLOBAL             11 (_log_event_safe + NULL)

370           LOAD_CONST              11 ('email.forwarder.secret.encrypted')

371           LOAD_FAST_BORROW         1 (brokerage_id)

372           LOAD_CONST              12 ('info')

373           LOAD_FAST_BORROW         2 (payload)

369           LOAD_CONST              10 (('brokerage_id', 'severity', 'payload'))
              CALL_KW                  4
              POP_TOP
              LOAD_CONST               1 (None)
              RETURN_VALUE

368   L4:     LOAD_CONST               1 (None)
              RETURN_VALUE

375   L5:     LOAD_FAST_BORROW         0 (secret_env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               6 ('status')
              CALL                     1
              LOAD_CONST              13 ('failed')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       59 (to L7)
              NOT_TAKEN

385           LOAD_FAST_BORROW         0 (secret_env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST              14 ('error_code')
              CALL                     1
              STORE_FAST               3 (code)

386           LOAD_FAST_BORROW         3 (code)
              LOAD_CONST              16 (('forwarder_secret_decrypt_failed', 'crypto_unavailable', 'crypto_key_missing'))
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       33 (to L6)
              NOT_TAKEN

391           LOAD_GLOBAL              3 (dict + NULL)
              LOAD_FAST_BORROW         2 (payload)
              CALL                     1
              STORE_FAST               4 (payload_failed)

392           LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (code, payload_failed)
              LOAD_CONST              14 ('error_code')
              STORE_SUBSCR

393           LOAD_GLOBAL             11 (_log_event_safe + NULL)

394           LOAD_CONST              15 ('email.forwarder.secret.decrypt_failed')

395           LOAD_FAST_BORROW         1 (brokerage_id)

396           LOAD_CONST               9 ('warning')

397           LOAD_FAST_BORROW         4 (payload_failed)

393           LOAD_CONST              10 (('brokerage_id', 'severity', 'payload'))
              CALL_KW                  4
              POP_TOP
              LOAD_CONST               1 (None)
              RETURN_VALUE

386   L6:     LOAD_CONST               1 (None)
              RETURN_VALUE

375   L7:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "app/routes/email_ingestion.py", line 406>:
406           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')

407           LOAD_CONST               2 ('EmailIngestionBody')

406           LOAD_CONST               3 ('_')

408           LOAD_CONST               4 ('bool')

406           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object email_parse at 0x0000018C17EDA310, file "app/routes/email_ingestion.py", line 405>:
 405            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 420            LOAD_GLOBAL              1 (_coerce_body_to_dict + NULL)
                LOAD_FAST_BORROW         0 (body)
                CALL                     1
                STORE_FAST               2 (coerced)

 421            LOAD_GLOBAL              3 (_scrub_source_hint + NULL)
                LOAD_GLOBAL              5 (getattr + NULL)
                LOAD_FAST_BORROW         0 (body)
                LOAD_CONST               1 ('source_hint')
                LOAD_CONST               2 (None)
                CALL                     3
                CALL                     1
                STORE_FAST               3 (source_hint)

 423            LOAD_GLOBAL              7 (parse_email_lead + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (coerced, source_hint)
                LOAD_CONST               3 (('source_hint',))
                CALL_KW                  2
                STORE_FAST               4 (parsed)

 424            LOAD_GLOBAL              9 (_public_parse_envelope + NULL)
                LOAD_FAST_BORROW         4 (parsed)
                CALL                     1
                STORE_FAST               5 (public)

 426            LOAD_GLOBAL             11 (_log_event_safe + NULL)

 427            LOAD_CONST               4 ('email.lead.parsed')

 428            LOAD_CONST               2 (None)

 429            LOAD_CONST               5 ('info')

 431            LOAD_CONST               6 ('source')
                LOAD_FAST_BORROW         5 (public)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               6 ('source')
                CALL                     1

 432            LOAD_CONST               7 ('has_phone')
                LOAD_FAST_BORROW         5 (public)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               7 ('has_phone')
                CALL                     1

 433            LOAD_CONST               8 ('has_email')
                LOAD_FAST_BORROW         5 (public)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               8 ('has_email')
                CALL                     1

 434            LOAD_CONST               9 ('call_eligible')
                LOAD_FAST_BORROW         5 (public)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               9 ('call_eligible')
                CALL                     1

 435            LOAD_CONST              10 ('warning_count')
                LOAD_GLOBAL             15 (len + NULL)
                LOAD_FAST_BORROW         5 (public)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              11 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L2:     CALL                     1

 436            LOAD_CONST              12 ('error_code')

 438            LOAD_FAST_BORROW         5 (public)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              13 ('status')
                CALL                     1
                LOAD_CONST              14 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       46 (to L9)
                NOT_TAKEN

 437            LOAD_FAST_BORROW         5 (public)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              15 ('errors')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         4 (to L5)
        L3:     NOT_TAKEN
        L4:     POP_TOP
                LOAD_CONST               2 (None)
                BUILD_LIST               1
        L5:     LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                LOAD_CONST              16 ('none')

  --    L8:     JUMP_FORWARD             1 (to L10)

 438    L9:     LOAD_CONST              16 ('none')

 430   L10:     BUILD_MAP                6

 426            LOAD_CONST              17 (('brokerage_id', 'severity', 'payload'))
                CALL_KW                  4
                POP_TOP

 442            LOAD_FAST_BORROW         5 (public)
                RETURN_VALUE

  --   L11:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L11 [0] lasti
  L4 to L6 -> L11 [0] lasti
  L7 to L11 -> L11 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app/routes/email_ingestion.py", line 446>:
446           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')

447           LOAD_CONST               2 ('EmailIngestionBody')

446           LOAD_CONST               3 ('brokerage')

448           LOAD_CONST               4 ('Dict[str, Any]')

446           LOAD_CONST               5 ('x_forwarder_signature')

449           LOAD_CONST               6 ('Optional[str]')

446           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object email_ingest at 0x0000018C17ED3710, file "app/routes/email_ingestion.py", line 445>:
 445            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 460    L2:     NOP

 461    L3:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('check_rate_limit', 'rate_limit_public_error'))
                IMPORT_NAME              0 (app.services.security.rate_limit)
                IMPORT_FROM              1 (check_rate_limit)
                STORE_FAST               3 (check_rate_limit)
                IMPORT_FROM              2 (rate_limit_public_error)
                STORE_FAST               4 (rate_limit_public_error)
                POP_TOP

 464            LOAD_FAST                3 (check_rate_limit)
                PUSH_NULL

 465            LOAD_CONST               2 ('email_ingestion')

 466            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (brokerage)
                LOAD_GLOBAL              8 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (brokerage)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               3 ('id')
                CALL                     1
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               4 (None)

 467    L5:     LOAD_CONST               5 ('TENANT')

 464            LOAD_CONST               6 (('surface', 'brokerage_id', 'actor_type'))
                CALL_KW                  3
                STORE_FAST               5 (_rl_verdict)

 469            LOAD_FAST_BORROW         5 (_rl_verdict)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               7 ('allowed')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         9 (to L9)
        L6:     NOT_TAKEN

 470    L7:     LOAD_FAST_BORROW         4 (rate_limit_public_error)
                PUSH_NULL
                LOAD_FAST_BORROW         5 (_rl_verdict)
                CALL                     1
        L8:     RETURN_VALUE

 469    L9:     NOP

 474   L10:     NOP

 489            LOAD_FAST                1 (brokerage)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                BUILD_MAP                0
       L13:     LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               3 ('id')
                CALL                     1
                STORE_FAST               6 (brokerage_id)

 490            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         6 (brokerage_id)
                LOAD_GLOBAL             14 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L15)
                NOT_TAKEN
                LOAD_FAST_BORROW         6 (brokerage_id)
                LOAD_ATTR               17 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L16)
       L14:     NOT_TAKEN

 491   L15:     LOAD_GLOBAL             19 (HTTPException + NULL)
                LOAD_CONST               8 (401)
                LOAD_CONST               9 ('Invalid brokerage auth')
                LOAD_CONST              10 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 493   L16:     LOAD_GLOBAL             21 (_coerce_body_to_dict + NULL)
                LOAD_FAST_BORROW         0 (body)
                CALL                     1
                STORE_FAST               7 (coerced)

 494            LOAD_GLOBAL             23 (_scrub_source_hint + NULL)
                LOAD_GLOBAL             25 (getattr + NULL)
                LOAD_FAST_BORROW         0 (body)
                LOAD_CONST              11 ('source_hint')
                LOAD_CONST               4 (None)
                CALL                     3
                CALL                     1
                STORE_FAST               8 (source_hint)

 501            LOAD_GLOBAL             27 (_resolve_forwarder_secret + NULL)
                LOAD_FAST_BORROW         1 (brokerage)
                CALL                     1
                STORE_FAST               9 (secret_env)

 505            LOAD_GLOBAL             29 (_emit_secret_store_observability + NULL)

 506            LOAD_FAST_BORROW_LOAD_FAST_BORROW 150 (secret_env, brokerage_id)

 505            LOAD_CONST              12 (('brokerage_id',))
                CALL_KW                  2
                POP_TOP

 509            LOAD_FAST_BORROW         9 (secret_env)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              13 ('status')
                CALL                     1
                LOAD_CONST              14 ('failed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE      206 (to L23)
                NOT_TAKEN

 512            LOAD_CONST              13 ('status')
                LOAD_CONST              14 ('failed')

 513            LOAD_CONST              15 ('brokerage_id')
                LOAD_FAST                6 (brokerage_id)

 514            LOAD_CONST              16 ('source')
                LOAD_CONST              17 ('generic_email')

 515            LOAD_CONST              18 ('lead_id')
                LOAD_CONST               4 (None)

 516            LOAD_CONST              19 ('pending_call_id')
                LOAD_CONST               4 (None)

 517            LOAD_CONST              20 ('call_queued')
                LOAD_CONST              21 (False)

 518            LOAD_CONST              22 ('call_eligible')
                LOAD_CONST              21 (False)

 519            LOAD_CONST              23 ('duplicate')
                LOAD_CONST              21 (False)

 520            LOAD_CONST              24 ('forwarder_verified')
                LOAD_CONST              21 (False)

 521            LOAD_CONST              25 ('forwarder_required')
                LOAD_CONST              21 (False)

 522            LOAD_CONST              26 ('dedupe_durable')
                LOAD_CONST              21 (False)

 523            LOAD_CONST              27 ('warnings')
                LOAD_GLOBAL             31 (list + NULL)
                LOAD_FAST_BORROW         9 (secret_env)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              27 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L19)
       L17:     NOT_TAKEN
       L18:     POP_TOP
                BUILD_LIST               0
       L19:     CALL                     1

 524            LOAD_CONST              28 ('errors')

 525            LOAD_FAST_BORROW         9 (secret_env)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              29 ('error_code')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L22)
       L20:     NOT_TAKEN
       L21:     POP_TOP

 526            LOAD_CONST              30 ('forwarder_secret_decrypt_failed')

 524   L22:     BUILD_LIST               1

 511            BUILD_MAP               13
                STORE_FAST              10 (result)

 529            LOAD_GLOBAL             33 (_log_event_safe + NULL)

 530            LOAD_CONST              31 ('email.lead.failed')

 531            LOAD_FAST_BORROW         6 (brokerage_id)

 532            LOAD_CONST              32 ('warning')

 534            LOAD_CONST              16 ('source')
                LOAD_CONST              17 ('generic_email')

 535            LOAD_CONST              22 ('call_eligible')
                LOAD_CONST              21 (False)

 536            LOAD_CONST              20 ('call_queued')
                LOAD_CONST              21 (False)

 537            LOAD_CONST              33 ('warning_count')
                LOAD_GLOBAL             35 (len + NULL)
                LOAD_FAST_BORROW        10 (result)
                LOAD_CONST              27 ('warnings')
                BINARY_OP               26 ([])
                CALL                     1

 538            LOAD_CONST              29 ('error_code')
                LOAD_FAST_BORROW        10 (result)
                LOAD_CONST              28 ('errors')
                BINARY_OP               26 ([])
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])

 539            LOAD_CONST              24 ('forwarder_verified')
                LOAD_CONST              21 (False)

 540            LOAD_CONST              25 ('forwarder_required')
                LOAD_CONST              21 (False)

 541            LOAD_CONST              26 ('dedupe_durable')
                LOAD_CONST              21 (False)

 542            LOAD_CONST              23 ('duplicate')
                LOAD_CONST              21 (False)

 543            LOAD_CONST              34 ('encryption_enabled')
                LOAD_GLOBAL             37 (bool + NULL)
                LOAD_FAST_BORROW         9 (secret_env)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              34 ('encryption_enabled')
                CALL                     1
                CALL                     1

 544            LOAD_CONST              35 ('plaintext_fallback')
                LOAD_GLOBAL             37 (bool + NULL)
                LOAD_FAST_BORROW         9 (secret_env)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              35 ('plaintext_fallback')
                CALL                     1
                CALL                     1

 533            BUILD_MAP               11

 529            LOAD_CONST              36 (('brokerage_id', 'severity', 'payload'))
                CALL_KW                  4
                POP_TOP

 547            LOAD_FAST_BORROW        10 (result)
                RETURN_VALUE

 549   L23:     LOAD_FAST_BORROW         9 (secret_env)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              37 ('secret')
                CALL                     1
                STORE_FAST              11 (forwarder_secret)

 551            LOAD_GLOBAL             39 (ingest_email_lead + NULL)

 552            LOAD_FAST_BORROW         6 (brokerage_id)

 553            LOAD_FAST_BORROW         7 (coerced)

 554            LOAD_FAST_BORROW         8 (source_hint)

 555            LOAD_FAST_BORROW         2 (x_forwarder_signature)

 556            LOAD_FAST_BORROW        11 (forwarder_secret)

 560            LOAD_FAST_BORROW         1 (brokerage)

 551            LOAD_CONST              38 (('source_hint', 'forwarder_signature', 'forwarder_secret', 'brokerage'))
                CALL_KW                  6
                STORE_FAST              10 (result)

 565            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW        10 (result)
                LOAD_GLOBAL              8 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      100 (to L34)
                NOT_TAKEN

 566            LOAD_GLOBAL             31 (list + NULL)
                LOAD_FAST_BORROW        10 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              27 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L26)
       L24:     NOT_TAKEN
       L25:     POP_TOP
                BUILD_LIST               0
       L26:     CALL                     1
                STORE_FAST              12 (merged_warnings)

 567            LOAD_FAST_BORROW         9 (secret_env)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              27 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L29)
       L27:     NOT_TAKEN
       L28:     POP_TOP
                BUILD_LIST               0
       L29:     GET_ITER
       L30:     FOR_ITER                28 (to L33)
                STORE_FAST              13 (w)

 568            LOAD_FAST_BORROW_LOAD_FAST_BORROW 220 (w, merged_warnings)
                CONTAINS_OP              1 (not in)
       L31:     POP_JUMP_IF_TRUE         3 (to L32)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L30)

 569   L32:     LOAD_FAST_BORROW        12 (merged_warnings)
                LOAD_ATTR               41 (append + NULL|self)
                LOAD_FAST_BORROW        13 (w)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           30 (to L30)

 567   L33:     END_FOR
                POP_ITER

 570            LOAD_FAST_BORROW_LOAD_FAST_BORROW 202 (merged_warnings, result)
                LOAD_CONST              27 ('warnings')
                STORE_SUBSCR

 572   L34:     LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW        10 (result)
                LOAD_GLOBAL              8 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        30 (to L35)
                NOT_TAKEN

 574            LOAD_CONST              13 ('status')
                LOAD_CONST              14 ('failed')

 575            LOAD_CONST              15 ('brokerage_id')
                LOAD_FAST_BORROW         6 (brokerage_id)

 576            LOAD_CONST              16 ('source')
                LOAD_CONST              17 ('generic_email')

 577            LOAD_CONST              18 ('lead_id')
                LOAD_CONST               4 (None)

 578            LOAD_CONST              19 ('pending_call_id')
                LOAD_CONST               4 (None)

 579            LOAD_CONST              20 ('call_queued')
                LOAD_CONST              21 (False)

 580            LOAD_CONST              22 ('call_eligible')
                LOAD_CONST              21 (False)

 581            LOAD_CONST              23 ('duplicate')
                LOAD_CONST              21 (False)

 582            LOAD_CONST              24 ('forwarder_verified')
                LOAD_CONST              21 (False)

 583            LOAD_CONST              25 ('forwarder_required')
                LOAD_CONST              21 (False)

 584            LOAD_CONST              26 ('dedupe_durable')
                LOAD_CONST              21 (False)

 585            LOAD_CONST              27 ('warnings')
                BUILD_LIST               0

 586            LOAD_CONST              28 ('errors')
                LOAD_CONST              39 ('service_returned_non_dict')
                BUILD_LIST               1

 573            BUILD_MAP               13
                STORE_FAST              10 (result)

 590   L35:     LOAD_GLOBAL             43 (_classify_ingest_event + NULL)
                LOAD_FAST_BORROW        10 (result)
                CALL                     1
                STORE_FAST              14 (event_type)

 591            LOAD_FAST_BORROW        10 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              13 ('status')
                CALL                     1
                LOAD_CONST              14 ('failed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L36)
                NOT_TAKEN
                LOAD_CONST              32 ('warning')
                JUMP_FORWARD             1 (to L37)
       L36:     LOAD_CONST              40 ('info')
       L37:     STORE_FAST              15 (severity)

 592            LOAD_GLOBAL             31 (list + NULL)
                LOAD_FAST_BORROW        10 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              27 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L40)
       L38:     NOT_TAKEN
       L39:     POP_TOP
                BUILD_LIST               0
       L40:     CALL                     1
                STORE_FAST              16 (warnings)

 593            LOAD_GLOBAL             31 (list + NULL)
                LOAD_FAST_BORROW        10 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              28 ('errors')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L43)
       L41:     NOT_TAKEN
       L42:     POP_TOP
                BUILD_LIST               0
       L43:     CALL                     1
                STORE_FAST              17 (errors)

 594            LOAD_GLOBAL             33 (_log_event_safe + NULL)

 595            LOAD_FAST               14 (event_type)

 596            LOAD_FAST                6 (brokerage_id)

 597            LOAD_FAST               15 (severity)

 599            LOAD_CONST              16 ('source')
                LOAD_FAST_BORROW        10 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              16 ('source')
                CALL                     1

 600            LOAD_CONST              22 ('call_eligible')
                LOAD_GLOBAL             37 (bool + NULL)
                LOAD_FAST_BORROW        10 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              22 ('call_eligible')
                CALL                     1
                CALL                     1

 601            LOAD_CONST              20 ('call_queued')
                LOAD_GLOBAL             37 (bool + NULL)
                LOAD_FAST_BORROW        10 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              20 ('call_queued')
                CALL                     1
                CALL                     1

 602            LOAD_CONST              33 ('warning_count')
                LOAD_GLOBAL             35 (len + NULL)
                LOAD_FAST_BORROW        16 (warnings)
                CALL                     1

 603            LOAD_CONST              29 ('error_code')
                LOAD_FAST_BORROW        17 (errors)
                TO_BOOL
                POP_JUMP_IF_FALSE       10 (to L44)
                NOT_TAKEN
                LOAD_FAST_BORROW        17 (errors)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                JUMP_FORWARD             1 (to L45)
       L44:     LOAD_CONST              41 ('none')

 604   L45:     LOAD_CONST              24 ('forwarder_verified')
                LOAD_GLOBAL             37 (bool + NULL)
                LOAD_FAST_BORROW        10 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              24 ('forwarder_verified')
                CALL                     1
                CALL                     1

 605            LOAD_CONST              25 ('forwarder_required')
                LOAD_GLOBAL             37 (bool + NULL)
                LOAD_FAST_BORROW        10 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              25 ('forwarder_required')
                CALL                     1
                CALL                     1

 606            LOAD_CONST              26 ('dedupe_durable')
                LOAD_GLOBAL             37 (bool + NULL)
                LOAD_FAST_BORROW        10 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              26 ('dedupe_durable')
                CALL                     1
                CALL                     1

 607            LOAD_CONST              23 ('duplicate')
                LOAD_GLOBAL             37 (bool + NULL)
                LOAD_FAST_BORROW        10 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              23 ('duplicate')
                CALL                     1
                CALL                     1

 598            BUILD_MAP                9

 594            LOAD_CONST              36 (('brokerage_id', 'severity', 'payload'))
                CALL_KW                  4
                POP_TOP

 612            LOAD_GLOBAL             45 (_emit_observability + NULL)

 613            LOAD_FAST_BORROW_LOAD_FAST_BORROW 166 (result, brokerage_id)

 612            LOAD_CONST              12 (('brokerage_id',))
                CALL_KW                  2
                POP_TOP

 620            LOAD_FAST_BORROW        10 (result)
                RETURN_VALUE

  --   L46:     PUSH_EXC_INFO

 471            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L48)
                NOT_TAKEN
                POP_TOP

 473   L47:     POP_EXCEPT
                EXTENDED_ARG             3
                JUMP_BACKWARD_NO_INTERRUPT 929 (to L10)

 471   L48:     RERAISE                  0

  --   L49:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L50:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L50 [0] lasti
  L3 to L6 -> L46 [0]
  L7 to L8 -> L46 [0]
  L8 to L11 -> L50 [0] lasti
  L12 to L14 -> L50 [0] lasti
  L15 to L17 -> L50 [0] lasti
  L18 to L20 -> L50 [0] lasti
  L21 to L24 -> L50 [0] lasti
  L25 to L27 -> L50 [0] lasti
  L28 to L31 -> L50 [0] lasti
  L32 to L38 -> L50 [0] lasti
  L39 to L41 -> L50 [0] lasti
  L42 to L46 -> L50 [0] lasti
  L46 to L47 -> L49 [1] lasti
  L47 to L48 -> L50 [0] lasti
  L48 to L49 -> L49 [1] lasti
  L49 to L50 -> L50 [0] lasti
```
