# routes/lead_ingestion

- **pyc:** `app\routes\__pycache__\lead_ingestion.cpython-314.pyc`
- **expected source path (absent):** `app\routes/lead_ingestion.py`
- **co_filename (from bytecode):** `app/routes/lead_ingestion.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** routes

## Module docstring

```
PAS161 — Lead ingestion webhook routes.

Four endpoints:

    POST /webhooks/generic
    POST /webhooks/zapier
    POST /webhooks/followupboss
    POST /webhooks/gohighlevel

Doctrine:

* **Auth:** every route requires ``X-API-Key`` via the existing
  ``require_brokerage`` dependency. Tenant scope (the
  ``brokerage_id``) is resolved from auth only — the body is
  **never** trusted for that field.
* **Normalisation:** each route dispatches to the matching
  pure normalizer in ``app.services.ingestion.normalizers``.
  Normalizers never raise; bad input produces a structural
  ``status: "failed"`` envelope.
* **Pending-call handoff:** an accepted lead is recorded in
  the process-local pending-call registry (``app.services.
  ingestion.pending_calls``). PAS161 does NOT auto-dial.
* **Response shape:** closed-allow-list dict with ``status``,
  ``source``, ``brokerage_id``, ``lead_id`` (the
  pending_call_id), ``call_queued``, and a list of
  structural ``warnings``. Never the raw payload, never an
  email, never a name.
* **Event logging:** every accepted / failed ingest writes
  one structural event via ``app.db.event_logger.log_event``.
  Allowed payload keys are enforced here (closed allow-list).
  Forbidden keys (phone, email, name, transcript, notes, raw
  payload) are never written.
```

## Imports

`APIRouter`, `Any`, `Body`, `Callable`, `Depends`, `Dict`, `HTTPException`, `NormalizedLead`, `Optional`, `__future__`, `annotations`, `app.db.event_logger`, `app.routes.portal`, `app.services.ingestion.contracts`, `app.services.ingestion.normalizers`, `app.services.ingestion.pending_calls`, `app.services.security.rate_limit`, `check_rate_limit`, `create_pending_call`, `enqueue_pending_call`, `fastapi`, `log_event`, `logging`, `normalize_followupboss_payload`, `normalize_generic_webhook`, `normalize_gohighlevel_payload`, `normalize_zapier_payload`, `rate_limit_public_error`, `require_brokerage`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_ingest`, `_lead_from_dict`, `_log_event_safe`, `_strip_error_tail`, `webhook_followupboss`, `webhook_generic`, `webhook_gohighlevel`, `webhook_zapier`

## Env-key candidates

`TENANT`

## String constants (redacted where noted)

- '\nPAS161 — Lead ingestion webhook routes.\n\nFour endpoints:\n\n    POST /webhooks/generic\n    POST /webhooks/zapier\n    POST /webhooks/followupboss\n    POST /webhooks/gohighlevel\n\nDoctrine:\n\n* **Auth:** every route requires ``X-API-Key`` via the existing\n  ``require_brokerage`` dependency. Tenant scope (the\n  ``brokerage_id``) is resolved from auth only — the body is\n  **never** trusted for that field.\n* **Normalisation:** each route dispatches to the matching\n  pure normalizer in ``app.services.ingestion.normalizers``.\n  Normalizers never raise; bad input produces a structural\n  ``status: "failed"`` envelope.\n* **Pending-call handoff:** an accepted lead is recorded in\n  the process-local pending-call registry (``app.services.\n  ingestion.pending_calls``). PAS161 does NOT auto-dial.\n* **Response shape:** closed-allow-list dict with ``status``,\n  ``source``, ``brokerage_id``, ``lead_id`` (the\n  pending_call_id), ``call_queued``, and a list of\n  structural ``warnings``. Never the raw payload, never an\n  email, never a name.\n* **Event logging:** every accepted / failed ingest writes\n  one structural event via ``app.db.event_logger.log_event``.\n  Allowed payload keys are enforced here (closed allow-list).\n  Forbidden keys (phone, email, name, transcript, notes, raw\n  payload) are never written.\n'
- 'pas.routes.lead_ingestion'
- 'lead_id'
- 'brokerage_id'
- 'severity'
- 'info'
- 'payload'
- '/generic'
- '/zapier'
- '/followupboss'
- '/gohighlevel'
- 'event_type'
- 'str'
- 'Optional[str]'
- 'Optional[Dict[str, Any]]'
- 'return'
- 'None'
- 'Best-effort structural event write. Never raises; payload\nis allow-list-filtered before write.'
- 'lead_ingestion'
- 'ingestion'
- 'log_event failed (non-critical) event_type='
- ' err_type='
- 'brokerage'
- 'Dict[str, Any]'
- 'body'
- 'Any'
- 'normalizer'
- 'Callable[[Any], Dict[str, Any]]'
- 'source_label'
- 'Common ingest pipeline: normalise → enqueue → respond.\n\nReturns the closed-allow-list response dict directly.\nNever raises; never echoes the raw payload.\n'
- 'Invalid brokerage auth'
- 'generic'
- 'webhook_generic'
- 'zapier'
- 'webhook_zapier'
- 'followupboss'
- 'webhook_followupboss'
- 'gohighlevel'
- 'webhook_gohighlevel'
- 'TENANT'
- 'allowed'
- 'status'
- 'failed'
- 'errors'
- 'normalizer_returned_non_dict'
- 'normalize_failed'
- 'lead.ingestion.failed'
- 'warning'
- 'source'
- 'warning_count'
- 'pending_call_id'
- 'call_queued'
- 'warnings'
- 'lead'
- 'lead_from_dict failed (non-critical) err='
- 'lead_object_construction_failed'
- 'accepted'
- 'lead.ingested'
- 'has_email'
- 'has_budget'
- 'has_timeline'
- 'call.pending_created'
- 'token'
- 'For a token like ``normalizer_exception:RuntimeError`` we\nkeep the prefix only. For pure structural tokens (e.g.\n``missing_phone``) the value is returned unchanged.'
- 'NormalizedLead'
- 'Reconstruct a ``NormalizedLead`` from the dict the\nnormalizer returned. The normalizer already stripped\nforbidden keys via ``NormalizedLead.to_dict()``, so this\nreconstruction is bounded to safe fields.'
- 'phone'
- 'unknown'
- 'full_name'
- 'first_name'
- 'last_name'
- 'email'
- 'intent'
- 'property_address'
- 'city'
- 'state'
- 'budget'
- 'timeline'
- 'notes'
- 'raw_source_ref'
- 'metadata'
- 'Generic lead webhook. Tenant-scoped via X-API-Key.\n\nNEVER accepts ``brokerage_id`` from the body. Returns the\nclosed-allow-list response. Raw payload never echoed; the\nonly field-shaped echo is ``phone`` via the pending-call\nacknowledgement.\n'
- 'Zapier-shape lead webhook. Same auth + doctrine as\n``/webhooks/generic``.'
- 'Follow Up Boss lead webhook. Same auth + doctrine.\n\nHMAC signature verification (PAS161 ships\n``verify_hmac_signature`` but does not wire it here —\nsignature header naming + per-tenant secret storage is a\nfollow-on phase). For PAS161 the API-key gate is the\nauth path.'
- 'GoHighLevel lead webhook. Same auth + doctrine. HMAC\nwiring deferred (see ``/followupboss``).'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS161 — Lead ingestion webhook routes.\n\nFour endpoints:\n\n    POST /webhooks/generic\n    POST /webhooks/zapier\n    POST /webhooks/followupboss\n    POST /webhooks/gohighlevel\n\nDoctrine:\n\n* **Auth:** every route requires ``X-API-Key`` via the existing\n  ``require_brokerage`` dependency. Tenant scope (the\n  ``brokerage_id``) is resolved from auth only — the body is\n  **never** trusted for that field.\n* **Normalisation:** each route dispatches to the matching\n  pure normalizer in ``app.services.ingestion.normalizers``.\n  Normalizers never raise; bad input produces a structural\n  ``status: "failed"`` envelope.\n* **Pending-call handoff:** an accepted lead is recorded in\n  the process-local pending-call registry (``app.services.\n  ingestion.pending_calls``). PAS161 does NOT auto-dial.\n* **Response shape:** closed-allow-list dict with ``status``,\n  ``source``, ``brokerage_id``, ``lead_id`` (the\n  pending_call_id), ``call_queued``, and a list of\n  structural ``warnings``. Never the raw payload, never an\n  email, never a name.\n* **Event logging:** every accepted / failed ingest writes\n  one structural event via ``app.db.event_logger.log_event``.\n  Allowed payload keys are enforced here (closed allow-list).\n  Forbidden keys (phone, email, name, transcript, notes, raw\n  payload) are never written.\n')
              STORE_NAME               0 (__doc__)

 36           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 38           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 39           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Callable', 'Dict', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Callable)
              STORE_NAME               6 (Callable)
              IMPORT_FROM              7 (Dict)
              STORE_NAME               7 (Dict)
              IMPORT_FROM              8 (Optional)
              STORE_NAME               8 (Optional)
              POP_TOP

 41           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('APIRouter', 'Body', 'Depends', 'HTTPException'))
              IMPORT_NAME              9 (fastapi)
              IMPORT_FROM             10 (APIRouter)
              STORE_NAME              10 (APIRouter)
              IMPORT_FROM             11 (Body)
              STORE_NAME              11 (Body)
              IMPORT_FROM             12 (Depends)
              STORE_NAME              12 (Depends)
              IMPORT_FROM             13 (HTTPException)
              STORE_NAME              13 (HTTPException)
              POP_TOP

 43           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('require_brokerage',))
              IMPORT_NAME             14 (app.routes.portal)
              IMPORT_FROM             15 (require_brokerage)
              STORE_NAME              15 (require_brokerage)
              POP_TOP

 44           LOAD_SMALL_INT           0
              LOAD_CONST               6 (('NormalizedLead',))
              IMPORT_NAME             16 (app.services.ingestion.contracts)
              IMPORT_FROM             17 (NormalizedLead)
              STORE_NAME              17 (NormalizedLead)
              POP_TOP

 45           LOAD_SMALL_INT           0
              LOAD_CONST               7 (('normalize_followupboss_payload', 'normalize_generic_webhook', 'normalize_gohighlevel_payload', 'normalize_zapier_payload'))
              IMPORT_NAME             18 (app.services.ingestion.normalizers)
              IMPORT_FROM             19 (normalize_followupboss_payload)
              STORE_NAME              19 (normalize_followupboss_payload)
              IMPORT_FROM             20 (normalize_generic_webhook)
              STORE_NAME              20 (normalize_generic_webhook)
              IMPORT_FROM             21 (normalize_gohighlevel_payload)
              STORE_NAME              21 (normalize_gohighlevel_payload)
              IMPORT_FROM             22 (normalize_zapier_payload)
              STORE_NAME              22 (normalize_zapier_payload)
              POP_TOP

 51           LOAD_SMALL_INT           0
              LOAD_CONST               8 (('create_pending_call', 'enqueue_pending_call'))
              IMPORT_NAME             23 (app.services.ingestion.pending_calls)
              IMPORT_FROM             24 (create_pending_call)
              STORE_NAME              24 (create_pending_call)
              IMPORT_FROM             25 (enqueue_pending_call)
              STORE_NAME              25 (enqueue_pending_call)
              POP_TOP

 56           LOAD_NAME               10 (APIRouter)
              PUSH_NULL
              CALL                     0
              STORE_NAME              26 (router)

 57           LOAD_NAME                3 (logging)
              LOAD_ATTR               54 (getLogger)
              PUSH_NULL
              LOAD_CONST               9 ('pas.routes.lead_ingestion')
              CALL                     1
              STORE_NAME              28 (logger)

 64           LOAD_CONST              36 (('source', 'lead_id', 'has_email', 'has_budget', 'has_timeline', 'call_queued', 'warning_count'))
              STORE_NAME              29 (_EVENT_PAYLOAD_ALLOWED)

 71           LOAD_CONST              11 ('brokerage_id')

 74           LOAD_CONST               2 (None)

 71           LOAD_CONST              10 ('lead_id')

 75           LOAD_CONST               2 (None)

 71           LOAD_CONST              12 ('severity')

 76           LOAD_CONST              13 ('info')

 71           LOAD_CONST              14 ('payload')

 77           LOAD_CONST               2 (None)

 71           BUILD_MAP                4
              LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18025530, file "app/routes/lead_ingestion.py", line 71>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _log_event_safe at 0x0000018C17E949B0, file "app/routes/lead_ingestion.py", line 71>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              30 (_log_event_safe)

107           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C18025130, file "app/routes/lead_ingestion.py", line 107>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _ingest at 0x0000018C17ED68E0, file "app/routes/lead_ingestion.py", line 107>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_ingest)

266           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA3A50, file "app/routes/lead_ingestion.py", line 266>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _strip_error_tail at 0x0000018C18011210, file "app/routes/lead_ingestion.py", line 266>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_strip_error_tail)

283           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA2A60, file "app/routes/lead_ingestion.py", line 283>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _lead_from_dict at 0x0000018C18325360, file "app/routes/lead_ingestion.py", line 283>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_lead_from_dict)

312           LOAD_NAME               26 (router)
              LOAD_ATTR               69 (post + NULL|self)
              LOAD_CONST              23 ('/generic')
              CALL                     1

314           LOAD_NAME               11 (Body)
              PUSH_NULL
              LOAD_CONST              24 (Ellipsis)
              CALL                     1

315           LOAD_NAME               12 (Depends)
              PUSH_NULL
              LOAD_NAME               15 (require_brokerage)
              CALL                     1

313           BUILD_TUPLE              2
              LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA3000, file "app/routes/lead_ingestion.py", line 313>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object webhook_generic at 0x0000018C18026530, file "app/routes/lead_ingestion.py", line 312>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

312           CALL                     0

313           STORE_NAME              35 (webhook_generic)

327           LOAD_NAME               26 (router)
              LOAD_ATTR               69 (post + NULL|self)
              LOAD_CONST              27 ('/zapier')
              CALL                     1

329           LOAD_NAME               11 (Body)
              PUSH_NULL
              LOAD_CONST              24 (Ellipsis)
              CALL                     1

330           LOAD_NAME               12 (Depends)
              PUSH_NULL
              LOAD_NAME               15 (require_brokerage)
              CALL                     1

328           BUILD_TUPLE              2
              LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA33C0, file "app/routes/lead_ingestion.py", line 328>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object webhook_zapier at 0x0000018C18026130, file "app/routes/lead_ingestion.py", line 327>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

327           CALL                     0

328           STORE_NAME              36 (webhook_zapier)

337           LOAD_NAME               26 (router)
              LOAD_ATTR               69 (post + NULL|self)
              LOAD_CONST              30 ('/followupboss')
              CALL                     1

339           LOAD_NAME               11 (Body)
              PUSH_NULL
              LOAD_CONST              24 (Ellipsis)
              CALL                     1

340           LOAD_NAME               12 (Depends)
              PUSH_NULL
              LOAD_NAME               15 (require_brokerage)
              CALL                     1

338           BUILD_TUPLE              2
              LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA35A0, file "app/routes/lead_ingestion.py", line 338>)
              MAKE_FUNCTION
              LOAD_CONST              32 (<code object webhook_followupboss at 0x0000018C18026230, file "app/routes/lead_ingestion.py", line 337>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

337           CALL                     0

338           STORE_NAME              37 (webhook_followupboss)

353           LOAD_NAME               26 (router)
              LOAD_ATTR               69 (post + NULL|self)
              LOAD_CONST              33 ('/gohighlevel')
              CALL                     1

355           LOAD_NAME               11 (Body)
              PUSH_NULL
              LOAD_CONST              24 (Ellipsis)
              CALL                     1

356           LOAD_NAME               12 (Depends)
              PUSH_NULL
              LOAD_NAME               15 (require_brokerage)
              CALL                     1

354           BUILD_TUPLE              2
              LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA2880, file "app/routes/lead_ingestion.py", line 354>)
              MAKE_FUNCTION
              LOAD_CONST              35 (<code object webhook_gohighlevel at 0x0000018C18024B30, file "app/routes/lead_ingestion.py", line 353>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

353           CALL                     0

354           STORE_NAME              38 (webhook_gohighlevel)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "app/routes/lead_ingestion.py", line 71>:
 71           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('event_type')

 72           LOAD_CONST               2 ('str')

 71           LOAD_CONST               3 ('brokerage_id')

 74           LOAD_CONST               4 ('Optional[str]')

 71           LOAD_CONST               5 ('lead_id')

 75           LOAD_CONST               4 ('Optional[str]')

 71           LOAD_CONST               6 ('severity')

 76           LOAD_CONST               2 ('str')

 71           LOAD_CONST               7 ('payload')

 77           LOAD_CONST               8 ('Optional[Dict[str, Any]]')

 71           LOAD_CONST               9 ('return')

 78           LOAD_CONST              10 ('None')

 71           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _log_event_safe at 0x0000018C17E949B0, file "app/routes/lead_ingestion.py", line 71>:
  71            RESUME                   0

  81            NOP

  82    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('log_event',))
                IMPORT_NAME              0 (app.db.event_logger)
                IMPORT_FROM              1 (log_event)
                STORE_FAST               5 (log_event)
                POP_TOP

  85    L2:     BUILD_MAP                0
                STORE_FAST               6 (safe_payload)

  86            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST                4 (payload)
                LOAD_GLOBAL              8 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       32 (to L6)
                NOT_TAKEN

  87            LOAD_GLOBAL             10 (_EVENT_PAYLOAD_ALLOWED)
                GET_ITER
        L3:     FOR_ITER                21 (to L5)
                STORE_FAST               7 (k)

  88            LOAD_FAST_LOAD_FAST    116 (k, payload)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L3)

  89    L4:     LOAD_FAST_LOAD_FAST     71 (payload, k)
                BINARY_OP               26 ([])
                LOAD_FAST_LOAD_FAST    103 (safe_payload, k)
                STORE_SUBSCR
                JUMP_BACKWARD           23 (to L3)

  87    L5:     END_FOR
                POP_ITER

  90    L6:     NOP

  91    L7:     LOAD_FAST                5 (log_event)
                PUSH_NULL

  92            LOAD_FAST                0 (event_type)

  93            LOAD_FAST                1 (brokerage_id)

  94            LOAD_FAST                2 (lead_id)

  95            LOAD_FAST                3 (severity)

  96            LOAD_FAST                6 (safe_payload)

  97            LOAD_CONST               3 ('lead_ingestion')

  98            LOAD_CONST               4 ('ingestion')

  91            LOAD_CONST               5 (('brokerage_id', 'lead_id', 'severity', 'payload', 'event_source', 'event_category'))
                CALL_KW                  7
                POP_TOP
        L8:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L9:     PUSH_EXC_INFO

  83            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L11)
                NOT_TAKEN
                POP_TOP

  84   L10:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

  83   L11:     RERAISE                  0

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L13:     PUSH_EXC_INFO

 100            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       58 (to L17)
                NOT_TAKEN
                STORE_FAST               8 (e)

 101   L14:     LOAD_GLOBAL             12 (logger)
                LOAD_ATTR               15 (warning + NULL|self)

 102            LOAD_CONST               6 ('log_event failed (non-critical) event_type=')
                LOAD_FAST                0 (event_type)
                FORMAT_SIMPLE
                LOAD_CONST               7 (' err_type=')

 103            LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE

 102            BUILD_STRING             4

 101            CALL                     1
                POP_TOP
       L15:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L16:     LOAD_CONST               2 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 100   L17:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "app/routes/lead_ingestion.py", line 107>:
107           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')

108           LOAD_CONST               2 ('Dict[str, Any]')

107           LOAD_CONST               3 ('body')

109           LOAD_CONST               4 ('Any')

107           LOAD_CONST               5 ('normalizer')

110           LOAD_CONST               6 ('Callable[[Any], Dict[str, Any]]')

107           LOAD_CONST               7 ('source_label')

111           LOAD_CONST               8 ('str')

107           LOAD_CONST               9 ('return')

112           LOAD_CONST               2 ('Dict[str, Any]')

107           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _ingest at 0x0000018C17ED68E0, file "app/routes/lead_ingestion.py", line 107>:
 107            RESUME                   0

 118            LOAD_FAST                0 (brokerage)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L1:     LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               1 ('id')
                CALL                     1
                STORE_FAST               4 (brokerage_id)

 119            LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (brokerage_id)
                LOAD_GLOBAL              4 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (brokerage_id)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L3)
                NOT_TAKEN

 122    L2:     LOAD_GLOBAL              9 (HTTPException + NULL)
                LOAD_CONST               2 (401)
                LOAD_CONST               3 ('Invalid brokerage auth')
                LOAD_CONST               4 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 128    L3:     NOP

 129    L4:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('check_rate_limit', 'rate_limit_public_error'))
                IMPORT_NAME              5 (app.services.security.rate_limit)
                IMPORT_FROM              6 (check_rate_limit)
                STORE_FAST               5 (check_rate_limit)
                IMPORT_FROM              7 (rate_limit_public_error)
                STORE_FAST               6 (rate_limit_public_error)
                POP_TOP

 133            LOAD_FAST_BORROW         3 (source_label)
                LOAD_CONST               6 ('generic')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_CONST               7 ('webhook_generic')
                JUMP_FORWARD            28 (to L9)

 134    L5:     LOAD_FAST_BORROW         3 (source_label)
                LOAD_CONST               8 ('zapier')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_CONST               9 ('webhook_zapier')
                JUMP_FORWARD            19 (to L9)

 135    L6:     LOAD_FAST_BORROW         3 (source_label)
                LOAD_CONST              10 ('followupboss')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN
                LOAD_CONST              11 ('webhook_followupboss')
                JUMP_FORWARD            10 (to L9)

 136    L7:     LOAD_FAST_BORROW         3 (source_label)
                LOAD_CONST              12 ('gohighlevel')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST              13 ('webhook_gohighlevel')
                JUMP_FORWARD             1 (to L9)

 137    L8:     LOAD_CONST              14 (None)

 132    L9:     STORE_FAST               7 (_wh_surface)

 139            LOAD_FAST_BORROW         7 (_wh_surface)
                POP_JUMP_IF_NONE        43 (to L13)
                NOT_TAKEN

 140            LOAD_FAST_BORROW         5 (check_rate_limit)
                PUSH_NULL

 141            LOAD_FAST_BORROW         7 (_wh_surface)

 142            LOAD_FAST_BORROW         4 (brokerage_id)

 143            LOAD_CONST              15 ('TENANT')

 140            LOAD_CONST              16 (('surface', 'brokerage_id', 'actor_type'))
                CALL_KW                  3
                STORE_FAST               8 (_rl_verdict)

 145            LOAD_FAST_BORROW         8 (_rl_verdict)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              17 ('allowed')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         9 (to L13)
       L10:     NOT_TAKEN

 146   L11:     LOAD_FAST_BORROW         6 (rate_limit_public_error)
                PUSH_NULL
                LOAD_FAST_BORROW         8 (_rl_verdict)
                CALL                     1
       L12:     RETURN_VALUE

 152   L13:     LOAD_FAST                2 (normalizer)
                PUSH_NULL
                LOAD_FAST                1 (body)
                CALL                     1
                STORE_FAST               9 (result)

 153            LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST                9 (result)
                LOAD_GLOBAL             18 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         8 (to L14)
                NOT_TAKEN

 156            LOAD_CONST              18 ('status')
                LOAD_CONST              19 ('failed')
                LOAD_CONST              20 ('errors')
                LOAD_CONST              21 ('normalizer_returned_non_dict')
                BUILD_LIST               1
                BUILD_MAP                2
                STORE_FAST               9 (result)

 158   L14:     LOAD_FAST                9 (result)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              18 ('status')
                CALL                     1
                LOAD_CONST              22 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE      123 (to L22)
                NOT_TAKEN

 159            LOAD_FAST                9 (result)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              20 ('errors')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         4 (to L15)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              23 ('normalize_failed')
                BUILD_LIST               1
       L15:     STORE_FAST              10 (errors)

 164            LOAD_FAST               10 (errors)
                GET_ITER
                LOAD_FAST_AND_CLEAR     11 (e)
                SWAP                     2
       L16:     BUILD_LIST               0
                SWAP                     2
       L17:     FOR_ITER                38 (to L20)
                STORE_FAST              11 (e)
                LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST               11 (e)
                LOAD_GLOBAL              4 (str)
                CALL                     2
                TO_BOOL
       L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L17)
       L19:     LOAD_GLOBAL             21 (_strip_error_tail + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LIST_APPEND              2
                JUMP_BACKWARD           40 (to L17)
       L20:     END_FOR
                POP_ITER
       L21:     STORE_FAST              12 (safe_errors)
                STORE_FAST              11 (e)

 165            LOAD_GLOBAL             23 (_log_event_safe + NULL)

 166            LOAD_CONST              24 ('lead.ingestion.failed')

 167            LOAD_FAST                4 (brokerage_id)

 168            LOAD_CONST              25 ('warning')

 170            LOAD_CONST              26 ('source')
                LOAD_FAST                3 (source_label)

 171            LOAD_CONST              27 ('warning_count')
                LOAD_GLOBAL             25 (len + NULL)
                LOAD_FAST               12 (safe_errors)
                CALL                     1

 169            BUILD_MAP                2

 165            LOAD_CONST              28 (('brokerage_id', 'severity', 'payload'))
                CALL_KW                  4
                POP_TOP

 175            LOAD_CONST              18 ('status')
                LOAD_CONST              19 ('failed')

 176            LOAD_CONST              26 ('source')
                LOAD_FAST                3 (source_label)

 177            LOAD_CONST              29 ('brokerage_id')
                LOAD_FAST                4 (brokerage_id)

 178            LOAD_CONST              30 ('lead_id')
                LOAD_CONST              14 (None)

 179            LOAD_CONST              31 ('pending_call_id')
                LOAD_CONST              14 (None)

 180            LOAD_CONST              32 ('call_queued')
                LOAD_CONST              33 (False)

 181            LOAD_CONST              34 ('warnings')
                LOAD_FAST               12 (safe_errors)

 174            BUILD_MAP                7
                RETURN_VALUE

 186   L22:     LOAD_FAST                9 (result)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              35 ('lead')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L23)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
       L23:     STORE_FAST              13 (lead_dict)

 187            NOP

 188   L24:     LOAD_GLOBAL             27 (_lead_from_dict + NULL)
                LOAD_FAST               13 (lead_dict)
                CALL                     1
                STORE_FAST              14 (lead_obj)

 213   L25:     LOAD_GLOBAL             37 (create_pending_call + NULL)
                LOAD_FAST_LOAD_FAST     14 (brokerage, lead_obj)
                CALL                     2
                STORE_FAST              15 (ack)

 214            LOAD_GLOBAL             39 (list + NULL)
                LOAD_FAST                9 (result)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              34 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L26)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L26:     CALL                     1
                LOAD_GLOBAL             39 (list + NULL)
                LOAD_FAST               15 (ack)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              34 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L27)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L27:     CALL                     1
                BINARY_OP                0 (+)
                STORE_FAST              16 (warnings)

 216            LOAD_FAST               15 (ack)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              31 ('pending_call_id')
                CALL                     1
                STORE_FAST              17 (pending_call_id)

 217            LOAD_GLOBAL             41 (bool + NULL)
                LOAD_FAST               15 (ack)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              32 ('call_queued')
                LOAD_CONST              33 (False)
                CALL                     2
                CALL                     1
                STORE_FAST              18 (call_queued)

 218            LOAD_FAST               15 (ack)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              18 ('status')
                CALL                     1
                LOAD_CONST              38 ('accepted')
                COMPARE_OP             103 (!=)
                STORE_FAST              19 (durable_failure)

 222            LOAD_GLOBAL             23 (_log_event_safe + NULL)

 223            LOAD_CONST              39 ('lead.ingested')

 224            LOAD_FAST                4 (brokerage_id)

 225            LOAD_FAST               17 (pending_call_id)

 226            LOAD_CONST              40 ('info')

 228            LOAD_CONST              26 ('source')
                LOAD_FAST                3 (source_label)

 229            LOAD_CONST              30 ('lead_id')
                LOAD_FAST               17 (pending_call_id)

 230            LOAD_CONST              41 ('has_email')
                LOAD_GLOBAL             41 (bool + NULL)
                LOAD_FAST               14 (lead_obj)
                LOAD_ATTR               42 (email)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       27 (to L28)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST               14 (lead_obj)
                LOAD_ATTR               42 (email)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
       L28:     CALL                     1

 231            LOAD_CONST              42 ('has_budget')
                LOAD_GLOBAL             41 (bool + NULL)
                LOAD_FAST               14 (lead_obj)
                LOAD_ATTR               44 (budget)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       27 (to L29)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST               14 (lead_obj)
                LOAD_ATTR               44 (budget)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
       L29:     CALL                     1

 232            LOAD_CONST              43 ('has_timeline')
                LOAD_GLOBAL             41 (bool + NULL)
                LOAD_FAST               14 (lead_obj)
                LOAD_ATTR               46 (timeline)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       27 (to L30)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST               14 (lead_obj)
                LOAD_ATTR               46 (timeline)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
       L30:     CALL                     1

 233            LOAD_CONST              32 ('call_queued')
                LOAD_FAST               18 (call_queued)

 234            LOAD_CONST              27 ('warning_count')
                LOAD_GLOBAL             25 (len + NULL)
                LOAD_FAST               16 (warnings)
                CALL                     1

 227            BUILD_MAP                7

 222            LOAD_CONST              44 (('brokerage_id', 'lead_id', 'severity', 'payload'))
                CALL_KW                  5
                POP_TOP

 239            LOAD_FAST               17 (pending_call_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       34 (to L31)
                NOT_TAKEN

 240            LOAD_GLOBAL             23 (_log_event_safe + NULL)

 241            LOAD_CONST              45 ('call.pending_created')

 242            LOAD_FAST                4 (brokerage_id)

 243            LOAD_FAST               17 (pending_call_id)

 244            LOAD_CONST              40 ('info')

 246            LOAD_CONST              26 ('source')
                LOAD_FAST                3 (source_label)

 247            LOAD_CONST              30 ('lead_id')
                LOAD_FAST               17 (pending_call_id)

 248            LOAD_CONST              32 ('call_queued')
                LOAD_FAST               18 (call_queued)

 249            LOAD_CONST              27 ('warning_count')
                LOAD_GLOBAL             25 (len + NULL)
                LOAD_FAST               16 (warnings)
                CALL                     1

 245            BUILD_MAP                4

 240            LOAD_CONST              44 (('brokerage_id', 'lead_id', 'severity', 'payload'))
                CALL_KW                  5
                POP_TOP

 254   L31:     LOAD_CONST              18 ('status')
                LOAD_FAST               19 (durable_failure)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L32)
                NOT_TAKEN
                LOAD_CONST              19 ('failed')
                JUMP_FORWARD             1 (to L33)
       L32:     LOAD_CONST              38 ('accepted')

 255   L33:     LOAD_CONST              26 ('source')
                LOAD_FAST                3 (source_label)

 256            LOAD_CONST              29 ('brokerage_id')
                LOAD_FAST                4 (brokerage_id)

 259            LOAD_CONST              30 ('lead_id')
                LOAD_FAST               14 (lead_obj)
                LOAD_ATTR               48 (lead_id)

 260            LOAD_CONST              31 ('pending_call_id')
                LOAD_FAST               17 (pending_call_id)

 261            LOAD_CONST              32 ('call_queued')
                LOAD_FAST               18 (call_queued)

 262            LOAD_CONST              34 ('warnings')
                LOAD_FAST               16 (warnings)

 253            BUILD_MAP                7
                RETURN_VALUE

  --   L34:     PUSH_EXC_INFO

 147            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L36)
                NOT_TAKEN
                POP_TOP

 149   L35:     POP_EXCEPT
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 661 (to L13)

 147   L36:     RERAISE                  0

  --   L37:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L38:     SWAP                     2
                POP_TOP

 164            SWAP                     2
                STORE_FAST              11 (e)
                RERAISE                  0

  --   L39:     PUSH_EXC_INFO

 189            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       90 (to L44)
                NOT_TAKEN
                STORE_FAST              11 (e)

 190   L40:     LOAD_GLOBAL             28 (logger)
                LOAD_ATTR               31 (warning + NULL|self)

 191            LOAD_CONST              36 ('lead_from_dict failed (non-critical) err=')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 190            CALL                     1
                POP_TOP

 193            LOAD_GLOBAL             23 (_log_event_safe + NULL)

 194            LOAD_CONST              24 ('lead.ingestion.failed')

 195            LOAD_FAST                4 (brokerage_id)

 196            LOAD_CONST              25 ('warning')

 197            LOAD_CONST              26 ('source')
                LOAD_FAST                3 (source_label)
                LOAD_CONST              27 ('warning_count')
                LOAD_SMALL_INT           1
                BUILD_MAP                2

 193            LOAD_CONST              28 (('brokerage_id', 'severity', 'payload'))
                CALL_KW                  4
                POP_TOP

 200            LOAD_CONST              18 ('status')
                LOAD_CONST              19 ('failed')

 201            LOAD_CONST              26 ('source')
                LOAD_FAST                3 (source_label)

 202            LOAD_CONST              29 ('brokerage_id')
                LOAD_FAST                4 (brokerage_id)

 203            LOAD_CONST              30 ('lead_id')
                LOAD_CONST              14 (None)

 204            LOAD_CONST              31 ('pending_call_id')
                LOAD_CONST              14 (None)

 205            LOAD_CONST              32 ('call_queued')
                LOAD_CONST              33 (False)

 206            LOAD_CONST              34 ('warnings')
                LOAD_CONST              37 ('lead_object_construction_failed')
                BUILD_LIST               1

 199            BUILD_MAP                7
       L41:     SWAP                     2
       L42:     POP_EXCEPT
                LOAD_CONST              14 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RETURN_VALUE

  --   L43:     LOAD_CONST              14 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 189   L44:     RERAISE                  0

  --   L45:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L10 -> L34 [0]
  L11 to L12 -> L34 [0]
  L16 to L18 -> L38 [2]
  L19 to L21 -> L38 [2]
  L24 to L25 -> L39 [0]
  L34 to L35 -> L37 [1] lasti
  L36 to L37 -> L37 [1] lasti
  L39 to L40 -> L45 [1] lasti
  L40 to L41 -> L43 [1] lasti
  L41 to L42 -> L45 [1] lasti
  L43 to L45 -> L45 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app/routes/lead_ingestion.py", line 266>:
266           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('token')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _strip_error_tail at 0x0000018C18011210, file "app/routes/lead_ingestion.py", line 266>:
266           RESUME                   0

270           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (token)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

271           LOAD_CONST               1 ('normalize_failed')
              RETURN_VALUE

272   L1:     LOAD_CONST               2 (':')
              LOAD_FAST_BORROW         0 (token)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

273           LOAD_FAST_BORROW         0 (token)
              RETURN_VALUE

274   L2:     LOAD_FAST_BORROW         0 (token)
              LOAD_ATTR                5 (partition + NULL|self)
              LOAD_CONST               2 (':')
              CALL                     1
              UNPACK_SEQUENCE          3
              STORE_FAST               1 (head)
              POP_TOP
              STORE_FAST               2 (_)

275           LOAD_FAST_BORROW         1 (head)
              LOAD_CONST               3 (('normalizer_exception', 'metadata_keys_dropped'))
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

279           LOAD_FAST_BORROW         1 (head)
              RETURN_VALUE

280   L3:     LOAD_FAST_BORROW         0 (token)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app/routes/lead_ingestion.py", line 283>:
283           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('d')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('NormalizedLead')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _lead_from_dict at 0x0000018C18325360, file "app/routes/lead_ingestion.py", line 283>:
 283           RESUME                   0

 288           LOAD_GLOBAL              1 (NormalizedLead + NULL)
               LOAD_CONST              18 (())
               BUILD_MAP                0
               LOAD_CONST               1 ('phone')

 289           LOAD_FAST_BORROW         0 (d)
               LOAD_CONST               1 ('phone')
               BINARY_OP               26 ([])
               MAP_ADD                  1

 288           LOAD_CONST               2 ('source')

 290           LOAD_FAST_BORROW         0 (d)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               2 ('source')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('unknown')

  --   L1:     MAP_ADD                  1

 288           LOAD_CONST               4 ('lead_id')

 291           LOAD_FAST_BORROW         0 (d)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               4 ('lead_id')
               CALL                     1
               MAP_ADD                  1

 288           LOAD_CONST               5 ('full_name')

 292           LOAD_FAST_BORROW         0 (d)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               5 ('full_name')
               CALL                     1
               MAP_ADD                  1

 288           LOAD_CONST               6 ('first_name')

 293           LOAD_FAST_BORROW         0 (d)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               6 ('first_name')
               CALL                     1
               MAP_ADD                  1

 288           LOAD_CONST               7 ('last_name')

 294           LOAD_FAST_BORROW         0 (d)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               7 ('last_name')
               CALL                     1
               MAP_ADD                  1

 288           LOAD_CONST               8 ('email')

 295           LOAD_FAST_BORROW         0 (d)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               8 ('email')
               CALL                     1
               MAP_ADD                  1

 288           LOAD_CONST               9 ('intent')

 296           LOAD_FAST_BORROW         0 (d)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               9 ('intent')
               CALL                     1
               MAP_ADD                  1

 288           LOAD_CONST              10 ('property_address')

 297           LOAD_FAST_BORROW         0 (d)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              10 ('property_address')
               CALL                     1
               MAP_ADD                  1

 288           LOAD_CONST              11 ('city')

 298           LOAD_FAST_BORROW         0 (d)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              11 ('city')
               CALL                     1
               MAP_ADD                  1

 288           LOAD_CONST              12 ('state')

 299           LOAD_FAST_BORROW         0 (d)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              12 ('state')
               CALL                     1
               MAP_ADD                  1

 288           LOAD_CONST              13 ('budget')

 300           LOAD_FAST_BORROW         0 (d)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              13 ('budget')
               CALL                     1
               MAP_ADD                  1

 288           LOAD_CONST              14 ('timeline')

 301           LOAD_FAST_BORROW         0 (d)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              14 ('timeline')
               CALL                     1
               MAP_ADD                  1

 288           LOAD_CONST              15 ('notes')

 302           LOAD_FAST_BORROW         0 (d)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              15 ('notes')
               CALL                     1
               MAP_ADD                  1

 288           LOAD_CONST              16 ('raw_source_ref')

 303           LOAD_FAST_BORROW         0 (d)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              16 ('raw_source_ref')
               CALL                     1
               MAP_ADD                  1

 288           LOAD_CONST              17 ('metadata')

 304           LOAD_GLOBAL              5 (dict + NULL)
               LOAD_FAST_BORROW         0 (d)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              17 ('metadata')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
       L2:     CALL                     1
               MAP_ADD                  1

 288           CALL_FUNCTION_EX
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "app/routes/lead_ingestion.py", line 313>:
313           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')

314           LOAD_CONST               2 ('Any')

313           LOAD_CONST               3 ('brokerage')

315           LOAD_CONST               4 ('Dict[str, Any]')

313           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object webhook_generic at 0x0000018C18026530, file "app/routes/lead_ingestion.py", line 312>:
 312           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 324           LOAD_GLOBAL              1 (_ingest + NULL)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (brokerage, body)
               LOAD_GLOBAL              2 (normalize_generic_webhook)
               LOAD_CONST               1 ('generic')
               CALL                     4
               RETURN_VALUE

  --   L2:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L2 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app/routes/lead_ingestion.py", line 328>:
328           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')

329           LOAD_CONST               2 ('Any')

328           LOAD_CONST               3 ('brokerage')

330           LOAD_CONST               4 ('Dict[str, Any]')

328           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object webhook_zapier at 0x0000018C18026130, file "app/routes/lead_ingestion.py", line 327>:
 327           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 334           LOAD_GLOBAL              1 (_ingest + NULL)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (brokerage, body)
               LOAD_GLOBAL              2 (normalize_zapier_payload)
               LOAD_CONST               1 ('zapier')
               CALL                     4
               RETURN_VALUE

  --   L2:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L2 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app/routes/lead_ingestion.py", line 338>:
338           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')

339           LOAD_CONST               2 ('Any')

338           LOAD_CONST               3 ('brokerage')

340           LOAD_CONST               4 ('Dict[str, Any]')

338           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object webhook_followupboss at 0x0000018C18026230, file "app/routes/lead_ingestion.py", line 337>:
 337           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 349           LOAD_GLOBAL              1 (_ingest + NULL)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (brokerage, body)
               LOAD_GLOBAL              2 (normalize_followupboss_payload)

 350           LOAD_CONST               1 ('followupboss')

 349           CALL                     4
               RETURN_VALUE

  --   L2:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L2 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app/routes/lead_ingestion.py", line 354>:
354           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')

355           LOAD_CONST               2 ('Any')

354           LOAD_CONST               3 ('brokerage')

356           LOAD_CONST               4 ('Dict[str, Any]')

354           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object webhook_gohighlevel at 0x0000018C18024B30, file "app/routes/lead_ingestion.py", line 353>:
 353           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 360           LOAD_GLOBAL              1 (_ingest + NULL)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (brokerage, body)
               LOAD_GLOBAL              2 (normalize_gohighlevel_payload)

 361           LOAD_CONST               1 ('gohighlevel')

 360           CALL                     4
               RETURN_VALUE

  --   L2:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L2 [0] lasti
```
