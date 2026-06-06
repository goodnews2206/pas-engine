# ingestion/email_ingestion

- **pyc:** `app\services\ingestion\__pycache__\email_ingestion.cpython-314.pyc`
- **expected source path (absent):** `app\services\ingestion/email_ingestion.py`
- **co_filename (from bytecode):** `app\services\ingestion\email_ingestion.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** ingestion

## Module docstring

```
PAS164 / PAS165 / PAS166 — Email lead ingestion service.

Wraps the pure :mod:`app.services.ingestion.email_parser`,
verifies the optional forwarder signature
(:mod:`app.services.ingestion.email_auth`), runs the email
through the durable dedupe store
(:mod:`app.services.ingestion.email_dedupe_store`) with a
process-local fallback (:mod:`app.services.ingestion.email_dedupe`),
and projects the parsed lead onto the PAS161 ``NormalizedLead``
shape so the PAS162 durable ``create_pending_call`` writer can
queue it.

PAS166 flow (extends the PAS165 flow):

    parse
      → resolve signature-required policy from brokerage row
      → verify forwarder signature  (soft pass when missing AND
                                     policy is not required;
                                     hard fail otherwise)
      → durable dedupe check + register  (multi-replica safe)
        → fall back to process-local dedupe if durable
          unavailable
      → convert to NormalizedLead
      → create_pending_call

NEVER auto-dials. NEVER stores the raw email body. NEVER
returns identifying fields beyond what PAS162 already echoes.
NEVER returns the forwarder signature, computed signature, or
dedupe key.

Hard doctrine:

* ``brokerage_id`` is REQUIRED from the caller. The body is
  never trusted — the caller is the auth layer.
* No raw body / subject / sender ever appears in the response
  envelope.
* No Gmail / Google / inbox / OAuth / IMAP / POP3 import. No
  external API call. No vendor SDK.
* On a parse with email but no phone, the ingestion service
  returns ``status="accepted"`` with ``call_queued=False`` and
  the structural warning ``email_lead_missing_phone`` — the
  lead is captured for forensic visibility but not handed to
  the dialing pipeline.
* On a parse failure, the ingestion service returns
  ``status="failed"`` with structural error tokens only.
* On a signature failure that hard-fails (invalid / malformed
  / required-but-missing), the ingestion service returns
  ``status="failed"`` BEFORE the dedupe register or the
  pending-call create — a forged forwarder must never see its
  forgery succeed even silently.
* On a duplicate (durable OR fallback), the ingestion service
  returns ``status="duplicate"`` with no pending-call create.
```

## Imports

`ALLOWED_EMAIL_LEAD_SOURCES`, `Any`, `Dict`, `List`, `NormalizedLead`, `Optional`, `__future__`, `annotations`, `app.services.ingestion.contracts`, `app.services.ingestion.email_auth`, `app.services.ingestion.email_dedupe`, `app.services.ingestion.email_dedupe_store`, `app.services.ingestion.email_parser`, `app.services.ingestion.pending_calls`, `build_email_dedupe_key`, `create_pending_call`, `durable_email_dedupe_enabled`, `is_duplicate_email_dedupe_key`, `logging`, `mark_email_duplicate_seen`, `parse_email_lead`, `register_email_dedupe_key`, `register_email_lead_dedupe`, `typing`, `verify_forwarder_signature`

## Classes

_none_

## Functions / methods

`__annotate__`, `_accepted`, `_attempt_durable_register`, `_coerce_email_components`, `_duplicate`, `_envelope`, `_failed`, `_normalized_lead_from_parsed`, `_process_local_register`, `email_forwarder_signature_required`, `ingest_email_lead`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS164 / PAS165 / PAS166 — Email lead ingestion service.\n\nWraps the pure :mod:`app.services.ingestion.email_parser`,\nverifies the optional forwarder signature\n(:mod:`app.services.ingestion.email_auth`), runs the email\nthrough the durable dedupe store\n(:mod:`app.services.ingestion.email_dedupe_store`) with a\nprocess-local fallback (:mod:`app.services.ingestion.email_dedupe`),\nand projects the parsed lead onto the PAS161 ``NormalizedLead``\nshape so the PAS162 durable ``create_pending_call`` writer can\nqueue it.\n\nPAS166 flow (extends the PAS165 flow):\n\n    parse\n      → resolve signature-required policy from brokerage row\n      → verify forwarder signature  (soft pass when missing AND\n                                     policy is not required;\n                                     hard fail otherwise)\n      → durable dedupe check + register  (multi-replica safe)\n        → fall back to process-local dedupe if durable\n          unavailable\n      → convert to NormalizedLead\n      → create_pending_call\n\nNEVER auto-dials. NEVER stores the raw email body. NEVER\nreturns identifying fields beyond what PAS162 already echoes.\nNEVER returns the forwarder signature, computed signature, or\ndedupe key.\n\nHard doctrine:\n\n* ``brokerage_id`` is REQUIRED from the caller. The body is\n  never trusted — the caller is the auth layer.\n* No raw body / subject / sender ever appears in the response\n  envelope.\n* No Gmail / Google / inbox / OAuth / IMAP / POP3 import. No\n  external API call. No vendor SDK.\n* On a parse with email but no phone, the ingestion service\n  returns ``status="accepted"`` with ``call_queued=False`` and\n  the structural warning ``email_lead_missing_phone`` — the\n  lead is captured for forensic visibility but not handed to\n  the dialing pipeline.\n* On a parse failure, the ingestion service returns\n  ``status="failed"`` with structural error tokens only.\n* On a signature failure that hard-fails (invalid / malformed\n  / required-but-missing), the ingestion service returns\n  ``status="failed"`` BEFORE the dedupe register or the\n  pending-call create — a forged forwarder must never see its\n  forgery succeed even silently.\n* On a duplicate (durable OR fallback), the ingestion service\n  returns ``status="duplicate"`` with no pending-call create.\n'
- 'pas.ingestion.email_ingestion'
- 'lead_id'
- 'pending_call_id'
- 'call_queued'
- 'call_eligible'
- 'duplicate'
- 'forwarder_verified'
- 'forwarder_required'
- 'dedupe_durable'
- 'warnings'
- 'errors'
- 'email_forwarder_signature_required'
- 'source_hint'
- 'forwarder_signature'
- 'forwarder_secret'
- 'brokerage'
- 'ingest_email_lead'
- 'status'
- 'str'
- 'brokerage_id'
- 'Optional[str]'
- 'source'
- 'bool'
- 'Optional[List[str]]'
- 'return'
- 'Dict[str, Any]'
- 'failed'
- 'accepted'
- 'Optional[Dict[str, Any]]'
- 'Resolve whether the brokerage requires a verified\nforwarder signature.\n\nStrict-literal-True policy: the value must be exactly the\nPython ``True`` object. Anything else (None, missing,\n``False``, the string ``"true"``, the integer ``1``, the\nstring ``"yes"``, …) yields ``False``. This deliberately\ncloses the "truthy" attack surface — a misconfigured\nbrokerage row that landed a string in this slot does NOT\nsilently flip the policy on.\n\nProbes the top-level field plus a bounded list of nested\nholders (``features`` / ``config``). NEVER raises.\n'
- 'parsed_lead'
- 'Optional[NormalizedLead]'
- 'Project the parser output dict onto the PAS161\n``NormalizedLead`` shape. The ``source`` carried on the\nNormalizedLead is intentionally collapsed to ``"manual"``\nbecause the PAS162 ``create_pending_call`` writer\nconstrains the source to a closed enum that does not\ninclude the email-source labels — the actual email source\nsurvives in the response envelope and (where the PAS161\nmetadata allow-list permits it) in the lead\'s metadata.\n\nReturns ``None`` when the parsed dict has no usable phone.\n'
- 'phone'
- 'metadata'
- 'manual'
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
- 'raw_email'
- 'Any'
- "Pull (subject, sender, body) from the caller's raw_email\nso the signature verifier and the dedupe key builder can\nuse the same canonical inputs the parser sees. NEVER\nraises."
- 'subject'
- 'sender'
- 'body'
- 'Subject'
- 'from'
- 'From'
- 'text'
- 'body_plain'
- 'html'
- 'body_html'
- 'dedupe_key'
- 'Try the durable register path first.\n\nReturns a normalised dict::\n\n    {\n      "outcome":        "registered" | "duplicate" | "fallback",\n      "durable":        bool,   # True iff the durable path actually wrote\n      "warnings":       [...],\n    }\n\nA ``"fallback"`` outcome means the durable layer was\nunreachable and the caller should retry with the PAS165\nprocess-local registry.\n'
- '_attempt_durable_register unexpected error type='
- 'outcome'
- 'fallback'
- 'durable'
- 'durable_email_dedupe_unavailable'
- 'durable_register_exception:'
- 'email_dedupe_fallback_process_local'
- 'registered'
- 'Fallback registrar — wraps the PAS165 process-local\nregistrar. Returns a normalised dict in the same shape as\n``_attempt_durable_register``.'
- '_process_local_register error type='
- 'process_local_register_failed:'
- 'Parse, verify forwarder signature, dedupe (durable +\nfallback), and (when eligible) queue a pending call.\n\nReturns the closed-shape envelope::\n\n    {\n      "status":             "accepted" | "failed" | "duplicate",\n      "brokerage_id":       "<from caller>",\n      "source":             "<one of ALLOWED_EMAIL_LEAD_SOURCES>",\n      "lead_id":            None,\n      "pending_call_id":    None | "<uuid>",\n      "call_queued":        bool,\n      "call_eligible":      bool,\n      "duplicate":          bool,\n      "forwarder_verified": bool,\n      "forwarder_required": bool,\n      "dedupe_durable":     bool,\n      "warnings":           [<structural tokens>],\n      "errors":             [<structural tokens>],\n    }\n\nNEVER returns the raw body / subject / sender / phone /\nemail / name / signature / dedupe key.\nNEVER reads ``brokerage_id`` from the raw email.\nNEVER raises.\n'
- 'generic_email'
- 'missing_brokerage_id'
- 'ingest_email_lead parser unexpected error type='
- 'parser_exception:'
- 'parser_returned_non_dict'
- 'verified'
- 'error_code'
- 'forwarder_signature_unconfigured'
- 'forwarder_secret_missing'
- 'forwarder_signature_missing'
- 'forwarder_signature_required'
- 'valid'
- 'forwarder_signature_invalid'
- 'email_parse_failed'
- 'lead'
- 'ingest_email_lead dedupe key build error type='
- 'dedupe_key_build_failed:'
- 'mark_email_duplicate_seen non-critical error type='
- 'email_lead_missing_phone'
- 'email_lead_no_phone source='
- ' brokerage='
- 'ingest_email_lead lead build error type='
- 'lead_build_failed:'
- 'lead_object_construction_failed'
- 'ingest_email_lead pending_call create error type='
- 'email_dedupe_registered_but_pending_call_failed'
- 'pending_call_create_failed:'
- 'pending_call_create_non_dict'
- 'pending_call_store_unavailable'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS164 / PAS165 / PAS166 — Email lead ingestion service.\n\nWraps the pure :mod:`app.services.ingestion.email_parser`,\nverifies the optional forwarder signature\n(:mod:`app.services.ingestion.email_auth`), runs the email\nthrough the durable dedupe store\n(:mod:`app.services.ingestion.email_dedupe_store`) with a\nprocess-local fallback (:mod:`app.services.ingestion.email_dedupe`),\nand projects the parsed lead onto the PAS161 ``NormalizedLead``\nshape so the PAS162 durable ``create_pending_call`` writer can\nqueue it.\n\nPAS166 flow (extends the PAS165 flow):\n\n    parse\n      → resolve signature-required policy from brokerage row\n      → verify forwarder signature  (soft pass when missing AND\n                                     policy is not required;\n                                     hard fail otherwise)\n      → durable dedupe check + register  (multi-replica safe)\n        → fall back to process-local dedupe if durable\n          unavailable\n      → convert to NormalizedLead\n      → create_pending_call\n\nNEVER auto-dials. NEVER stores the raw email body. NEVER\nreturns identifying fields beyond what PAS162 already echoes.\nNEVER returns the forwarder signature, computed signature, or\ndedupe key.\n\nHard doctrine:\n\n* ``brokerage_id`` is REQUIRED from the caller. The body is\n  never trusted — the caller is the auth layer.\n* No raw body / subject / sender ever appears in the response\n  envelope.\n* No Gmail / Google / inbox / OAuth / IMAP / POP3 import. No\n  external API call. No vendor SDK.\n* On a parse with email but no phone, the ingestion service\n  returns ``status="accepted"`` with ``call_queued=False`` and\n  the structural warning ``email_lead_missing_phone`` — the\n  lead is captured for forensic visibility but not handed to\n  the dialing pipeline.\n* On a parse failure, the ingestion service returns\n  ``status="failed"`` with structural error tokens only.\n* On a signature failure that hard-fails (invalid / malformed\n  / required-but-missing), the ingestion service returns\n  ``status="failed"`` BEFORE the dedupe register or the\n  pending-call create — a forged forwarder must never see its\n  forgery succeed even silently.\n* On a duplicate (durable OR fallback), the ingestion service\n  returns ``status="duplicate"`` with no pending-call create.\n')
              STORE_NAME               0 (__doc__)

 56           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 58           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 59           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (List)
              STORE_NAME               7 (List)
              IMPORT_FROM              8 (Optional)
              STORE_NAME               8 (Optional)
              POP_TOP

 61           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('NormalizedLead',))
              IMPORT_NAME              9 (app.services.ingestion.contracts)
              IMPORT_FROM             10 (NormalizedLead)
              STORE_NAME              10 (NormalizedLead)
              POP_TOP

 62           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('verify_forwarder_signature',))
              IMPORT_NAME             11 (app.services.ingestion.email_auth)
              IMPORT_FROM             12 (verify_forwarder_signature)
              STORE_NAME              12 (verify_forwarder_signature)
              POP_TOP

 63           LOAD_SMALL_INT           0
              LOAD_CONST               6 (('build_email_dedupe_key', 'register_email_lead_dedupe'))
              IMPORT_NAME             13 (app.services.ingestion.email_dedupe)
              IMPORT_FROM             14 (build_email_dedupe_key)
              STORE_NAME              14 (build_email_dedupe_key)
              IMPORT_FROM             15 (register_email_lead_dedupe)
              STORE_NAME              15 (register_email_lead_dedupe)
              POP_TOP

 67           LOAD_SMALL_INT           0
              LOAD_CONST               7 (('durable_email_dedupe_enabled', 'is_duplicate_email_dedupe_key', 'mark_email_duplicate_seen', 'register_email_dedupe_key'))
              IMPORT_NAME             16 (app.services.ingestion.email_dedupe_store)
              IMPORT_FROM             17 (durable_email_dedupe_enabled)
              STORE_NAME              17 (durable_email_dedupe_enabled)
              IMPORT_FROM             18 (is_duplicate_email_dedupe_key)
              STORE_NAME              18 (is_duplicate_email_dedupe_key)
              IMPORT_FROM             19 (mark_email_duplicate_seen)
              STORE_NAME              19 (mark_email_duplicate_seen)
              IMPORT_FROM             20 (register_email_dedupe_key)
              STORE_NAME              20 (register_email_dedupe_key)
              POP_TOP

 73           LOAD_SMALL_INT           0
              LOAD_CONST               8 (('ALLOWED_EMAIL_LEAD_SOURCES', 'parse_email_lead'))
              IMPORT_NAME             21 (app.services.ingestion.email_parser)
              IMPORT_FROM             22 (ALLOWED_EMAIL_LEAD_SOURCES)
              STORE_NAME              22 (ALLOWED_EMAIL_LEAD_SOURCES)
              IMPORT_FROM             23 (parse_email_lead)
              STORE_NAME              23 (parse_email_lead)
              POP_TOP

 77           LOAD_SMALL_INT           0
              LOAD_CONST               9 (('create_pending_call',))
              IMPORT_NAME             24 (app.services.ingestion.pending_calls)
              IMPORT_FROM             25 (create_pending_call)
              STORE_NAME              25 (create_pending_call)
              POP_TOP

 82           LOAD_NAME                3 (logging)
              LOAD_ATTR               52 (getLogger)
              PUSH_NULL
              LOAD_CONST              10 ('pas.ingestion.email_ingestion')
              CALL                     1
              STORE_NAME              27 (logger)

 89           LOAD_CONST              11 ('lead_id')

 94           LOAD_CONST               2 (None)

 89           LOAD_CONST              12 ('pending_call_id')

 95           LOAD_CONST               2 (None)

 89           LOAD_CONST              13 ('call_queued')

 96           LOAD_CONST              14 (False)

 89           LOAD_CONST              15 ('call_eligible')

 97           LOAD_CONST              14 (False)

 89           LOAD_CONST              16 ('duplicate')

 98           LOAD_CONST              14 (False)

 89           LOAD_CONST              17 ('forwarder_verified')

 99           LOAD_CONST              14 (False)

 89           LOAD_CONST              18 ('forwarder_required')

100           LOAD_CONST              14 (False)

 89           LOAD_CONST              19 ('dedupe_durable')

101           LOAD_CONST              14 (False)

 89           LOAD_CONST              20 ('warnings')

102           LOAD_CONST               2 (None)

 89           LOAD_CONST              21 ('errors')

103           LOAD_CONST               2 (None)

 89           BUILD_MAP               10
              LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18053090, file "app\services\ingestion\email_ingestion.py", line 89>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object _envelope at 0x0000018C1794E9E0, file "app\services\ingestion\email_ingestion.py", line 89>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              28 (_envelope)

122           LOAD_CONST              20 ('warnings')

126           LOAD_CONST               2 (None)

122           LOAD_CONST              21 ('errors')

127           LOAD_CONST               2 (None)

122           LOAD_CONST              17 ('forwarder_verified')

128           LOAD_CONST              14 (False)

122           LOAD_CONST              18 ('forwarder_required')

129           LOAD_CONST              14 (False)

122           LOAD_CONST              19 ('dedupe_durable')

130           LOAD_CONST              14 (False)

122           BUILD_MAP                5
              LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FBFEE0, file "app\services\ingestion\email_ingestion.py", line 122>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object _failed at 0x0000018C18025B30, file "app\services\ingestion\email_ingestion.py", line 122>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              29 (_failed)

144           LOAD_CONST              20 ('warnings')

155           LOAD_CONST               2 (None)

144           BUILD_MAP                1
              LOAD_CONST              26 (<code object __annotate__ at 0x0000018C180531B0, file "app\services\ingestion\email_ingestion.py", line 144>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object _accepted at 0x0000018C18025D30, file "app\services\ingestion\email_ingestion.py", line 144>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              30 (_accepted)

173           LOAD_CONST              20 ('warnings')

180           LOAD_CONST               2 (None)

173           BUILD_MAP                1
              LOAD_CONST              28 (<code object __annotate__ at 0x0000018C18090030, file "app\services\ingestion\email_ingestion.py", line 173>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object _duplicate at 0x0000018C18025E30, file "app\services\ingestion\email_ingestion.py", line 173>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              31 (_duplicate)

202           LOAD_CONST              30 ('email_forwarder_signature_required')
              STORE_NAME              32 (_REQUIRED_FLAG_KEY)

203           LOAD_CONST              48 (('features', 'config'))
              STORE_NAME              33 (_REQUIRED_FLAG_NESTS)

206           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA1E30, file "app\services\ingestion\email_ingestion.py", line 206>)
              MAKE_FUNCTION
              LOAD_CONST              32 (<code object email_forwarder_signature_required at 0x0000018C179A7290, file "app\services\ingestion\email_ingestion.py", line 206>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              34 (email_forwarder_signature_required)

239           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C18025930, file "app\services\ingestion\email_ingestion.py", line 239>)
              MAKE_FUNCTION
              LOAD_CONST              34 (<code object _normalized_lead_from_parsed at 0x0000018C17D6DFC0, file "app\services\ingestion\email_ingestion.py", line 239>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              35 (_normalized_lead_from_parsed)

282           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C17FA2880, file "app\services\ingestion\email_ingestion.py", line 282>)
              MAKE_FUNCTION
              LOAD_CONST              36 (<code object _coerce_email_components at 0x0000018C17ED5770, file "app\services\ingestion\email_ingestion.py", line 282>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              36 (_coerce_email_components)

314           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C18024B30, file "app\services\ingestion\email_ingestion.py", line 314>)
              MAKE_FUNCTION
              LOAD_CONST              38 (<code object _attempt_durable_register at 0x0000018C17ED5AC0, file "app\services\ingestion\email_ingestion.py", line 314>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              37 (_attempt_durable_register)

387           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C18024D30, file "app\services\ingestion\email_ingestion.py", line 387>)
              MAKE_FUNCTION
              LOAD_CONST              40 (<code object _process_local_register at 0x0000018C17ED5E60, file "app\services\ingestion\email_ingestion.py", line 387>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              38 (_process_local_register)

429           LOAD_CONST              41 ('source_hint')

433           LOAD_CONST               2 (None)

429           LOAD_CONST              42 ('forwarder_signature')

434           LOAD_CONST               2 (None)

429           LOAD_CONST              43 ('forwarder_secret')

435           LOAD_CONST               2 (None)

429           LOAD_CONST              44 ('brokerage')

436           LOAD_CONST               2 (None)

429           BUILD_MAP                4
              LOAD_CONST              45 (<code object __annotate__ at 0x0000018C18090140, file "app\services\ingestion\email_ingestion.py", line 429>)
              MAKE_FUNCTION
              LOAD_CONST              46 (<code object ingest_email_lead at 0x0000018C17D7FBE0, file "app\services\ingestion\email_ingestion.py", line 429>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              39 (ingest_email_lead)

775           LOAD_CONST              30 ('email_forwarder_signature_required')

776           LOAD_CONST              47 ('ingest_email_lead')

774           BUILD_LIST               2
              STORE_NAME              40 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18053090, file "app\services\ingestion\email_ingestion.py", line 89>:
 89           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

 91           LOAD_CONST               2 ('str')

 89           LOAD_CONST               3 ('brokerage_id')

 92           LOAD_CONST               4 ('Optional[str]')

 89           LOAD_CONST               5 ('source')

 93           LOAD_CONST               2 ('str')

 89           LOAD_CONST               6 ('lead_id')

 94           LOAD_CONST               4 ('Optional[str]')

 89           LOAD_CONST               7 ('pending_call_id')

 95           LOAD_CONST               4 ('Optional[str]')

 89           LOAD_CONST               8 ('call_queued')

 96           LOAD_CONST               9 ('bool')

 89           LOAD_CONST              10 ('call_eligible')

 97           LOAD_CONST               9 ('bool')

 89           LOAD_CONST              11 ('duplicate')

 98           LOAD_CONST               9 ('bool')

 89           LOAD_CONST              12 ('forwarder_verified')

 99           LOAD_CONST               9 ('bool')

 89           LOAD_CONST              13 ('forwarder_required')

100           LOAD_CONST               9 ('bool')

 89           LOAD_CONST              14 ('dedupe_durable')

101           LOAD_CONST               9 ('bool')

 89           LOAD_CONST              15 ('warnings')

102           LOAD_CONST              16 ('Optional[List[str]]')

 89           LOAD_CONST              17 ('errors')

103           LOAD_CONST              16 ('Optional[List[str]]')

 89           LOAD_CONST              18 ('return')

104           LOAD_CONST              19 ('Dict[str, Any]')

 89           BUILD_MAP               14
              RETURN_VALUE

Disassembly of <code object _envelope at 0x0000018C1794E9E0, file "app\services\ingestion\email_ingestion.py", line 89>:
 89           RESUME                   0

106           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

107           LOAD_CONST               1 ('brokerage_id')
              LOAD_FAST                1 (brokerage_id)

108           LOAD_CONST               2 ('source')
              LOAD_FAST                2 (source)

109           LOAD_CONST               3 ('lead_id')
              LOAD_FAST                3 (lead_id)

110           LOAD_CONST               4 ('pending_call_id')
              LOAD_FAST                4 (pending_call_id)

111           LOAD_CONST               5 ('call_queued')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         5 (call_queued)
              CALL                     1

112           LOAD_CONST               6 ('call_eligible')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         6 (call_eligible)
              CALL                     1

113           LOAD_CONST               7 ('duplicate')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         7 (duplicate)
              CALL                     1

114           LOAD_CONST               8 ('forwarder_verified')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         8 (forwarder_verified)
              CALL                     1

115           LOAD_CONST               9 ('forwarder_required')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         9 (forwarder_required)
              CALL                     1

116           LOAD_CONST              10 ('dedupe_durable')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW        10 (dedupe_durable)
              CALL                     1

117           LOAD_CONST              11 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST               11 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

118           LOAD_CONST              12 ('errors')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST               12 (errors)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L2:     CALL                     1

105           BUILD_MAP               13
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FBFEE0, file "app\services\ingestion\email_ingestion.py", line 122>:
122           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

124           LOAD_CONST               2 ('Optional[str]')

122           LOAD_CONST               3 ('source')

125           LOAD_CONST               4 ('str')

122           LOAD_CONST               5 ('warnings')

126           LOAD_CONST               6 ('Optional[List[str]]')

122           LOAD_CONST               7 ('errors')

127           LOAD_CONST               6 ('Optional[List[str]]')

122           LOAD_CONST               8 ('forwarder_verified')

128           LOAD_CONST               9 ('bool')

122           LOAD_CONST              10 ('forwarder_required')

129           LOAD_CONST               9 ('bool')

122           LOAD_CONST              11 ('dedupe_durable')

130           LOAD_CONST               9 ('bool')

122           LOAD_CONST              12 ('return')

131           LOAD_CONST              13 ('Dict[str, Any]')

122           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object _failed at 0x0000018C18025B30, file "app\services\ingestion\email_ingestion.py", line 122>:
122           RESUME                   0

132           LOAD_GLOBAL              1 (_envelope + NULL)

133           LOAD_CONST               0 ('failed')

134           LOAD_FAST_BORROW         0 (brokerage_id)

135           LOAD_FAST_BORROW         1 (source)

136           LOAD_FAST_BORROW         2 (warnings)

137           LOAD_FAST_BORROW         3 (errors)

138           LOAD_FAST_BORROW         4 (forwarder_verified)

139           LOAD_FAST_BORROW         5 (forwarder_required)

140           LOAD_FAST_BORROW         6 (dedupe_durable)

132           LOAD_CONST               1 (('status', 'brokerage_id', 'source', 'warnings', 'errors', 'forwarder_verified', 'forwarder_required', 'dedupe_durable'))
              CALL_KW                  8
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180531B0, file "app\services\ingestion\email_ingestion.py", line 144>:
144           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

146           LOAD_CONST               2 ('str')

144           LOAD_CONST               3 ('source')

147           LOAD_CONST               2 ('str')

144           LOAD_CONST               4 ('lead_id')

148           LOAD_CONST               5 ('Optional[str]')

144           LOAD_CONST               6 ('pending_call_id')

149           LOAD_CONST               5 ('Optional[str]')

144           LOAD_CONST               7 ('call_queued')

150           LOAD_CONST               8 ('bool')

144           LOAD_CONST               9 ('call_eligible')

151           LOAD_CONST               8 ('bool')

144           LOAD_CONST              10 ('forwarder_verified')

152           LOAD_CONST               8 ('bool')

144           LOAD_CONST              11 ('forwarder_required')

153           LOAD_CONST               8 ('bool')

144           LOAD_CONST              12 ('dedupe_durable')

154           LOAD_CONST               8 ('bool')

144           LOAD_CONST              13 ('warnings')

155           LOAD_CONST              14 ('Optional[List[str]]')

144           LOAD_CONST              15 ('return')

156           LOAD_CONST              16 ('Dict[str, Any]')

144           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object _accepted at 0x0000018C18025D30, file "app\services\ingestion\email_ingestion.py", line 144>:
144           RESUME                   0

157           LOAD_GLOBAL              1 (_envelope + NULL)

158           LOAD_CONST               0 ('accepted')

159           LOAD_FAST_BORROW         0 (brokerage_id)

160           LOAD_FAST_BORROW         1 (source)

161           LOAD_FAST_BORROW         2 (lead_id)

162           LOAD_FAST_BORROW         3 (pending_call_id)

163           LOAD_FAST_BORROW         4 (call_queued)

164           LOAD_FAST_BORROW         5 (call_eligible)

165           LOAD_CONST               1 (False)

166           LOAD_FAST_BORROW         6 (forwarder_verified)

167           LOAD_FAST_BORROW         7 (forwarder_required)

168           LOAD_FAST_BORROW         8 (dedupe_durable)

169           LOAD_FAST_BORROW         9 (warnings)

157           LOAD_CONST               2 (('status', 'brokerage_id', 'source', 'lead_id', 'pending_call_id', 'call_queued', 'call_eligible', 'duplicate', 'forwarder_verified', 'forwarder_required', 'dedupe_durable', 'warnings'))
              CALL_KW                 12
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18090030, file "app\services\ingestion\email_ingestion.py", line 173>:
173           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

175           LOAD_CONST               2 ('str')

173           LOAD_CONST               3 ('source')

176           LOAD_CONST               2 ('str')

173           LOAD_CONST               4 ('forwarder_verified')

177           LOAD_CONST               5 ('bool')

173           LOAD_CONST               6 ('forwarder_required')

178           LOAD_CONST               5 ('bool')

173           LOAD_CONST               7 ('dedupe_durable')

179           LOAD_CONST               5 ('bool')

173           LOAD_CONST               8 ('warnings')

180           LOAD_CONST               9 ('Optional[List[str]]')

173           LOAD_CONST              10 ('return')

181           LOAD_CONST              11 ('Dict[str, Any]')

173           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object _duplicate at 0x0000018C18025E30, file "app\services\ingestion\email_ingestion.py", line 173>:
173           RESUME                   0

182           LOAD_GLOBAL              1 (_envelope + NULL)

183           LOAD_CONST               0 ('duplicate')

184           LOAD_FAST_BORROW         0 (brokerage_id)

185           LOAD_FAST_BORROW         1 (source)

186           LOAD_CONST               1 (None)

187           LOAD_CONST               1 (None)

188           LOAD_CONST               2 (False)

189           LOAD_CONST               3 (True)

190           LOAD_CONST               3 (True)

191           LOAD_FAST_BORROW         2 (forwarder_verified)

192           LOAD_FAST_BORROW         3 (forwarder_required)

193           LOAD_FAST_BORROW         4 (dedupe_durable)

194           LOAD_FAST_BORROW         5 (warnings)

182           LOAD_CONST               4 (('status', 'brokerage_id', 'source', 'lead_id', 'pending_call_id', 'call_queued', 'call_eligible', 'duplicate', 'forwarder_verified', 'forwarder_required', 'dedupe_durable', 'warnings'))
              CALL_KW                 12
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "app\services\ingestion\email_ingestion.py", line 206>:
206           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')
              LOAD_CONST               2 ('Optional[Dict[str, Any]]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object email_forwarder_signature_required at 0x0000018C179A7290, file "app\services\ingestion\email_ingestion.py", line 206>:
206           RESUME                   0

221           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

222           LOAD_CONST               1 (False)
              RETURN_VALUE

223   L1:     LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_GLOBAL              6 (_REQUIRED_FLAG_KEY)
              CALL                     1
              STORE_FAST               1 (top)

224           LOAD_FAST_BORROW         1 (top)
              LOAD_CONST               2 (True)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

225           LOAD_CONST               2 (True)
              RETURN_VALUE

226   L2:     LOAD_GLOBAL              8 (_REQUIRED_FLAG_NESTS)
              GET_ITER
      L3:     FOR_ITER                74 (to L6)
              STORE_FAST               2 (holder_key)

227           LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_FAST_BORROW         2 (holder_key)
              CALL                     1
              STORE_FAST               3 (holder)

228           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (holder)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD           44 (to L3)

229   L4:     LOAD_FAST_BORROW         3 (holder)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_GLOBAL              6 (_REQUIRED_FLAG_KEY)
              CALL                     1
              STORE_FAST               4 (v)

230           LOAD_FAST_BORROW         4 (v)
              LOAD_CONST               2 (True)
              IS_OP                    0 (is)
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           73 (to L3)

231   L5:     POP_TOP
              LOAD_CONST               2 (True)
              RETURN_VALUE

226   L6:     END_FOR
              POP_ITER

232           LOAD_CONST               1 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app\services\ingestion\email_ingestion.py", line 239>:
239           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('parsed_lead')

240           LOAD_CONST               2 ('Dict[str, Any]')

239           LOAD_CONST               3 ('source')

242           LOAD_CONST               4 ('str')

239           LOAD_CONST               5 ('return')

243           LOAD_CONST               6 ('Optional[NormalizedLead]')

239           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _normalized_lead_from_parsed at 0x0000018C17D6DFC0, file "app\services\ingestion\email_ingestion.py", line 239>:
239           RESUME                   0

255           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (parsed_lead)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

256           LOAD_CONST               1 (None)
              RETURN_VALUE

257   L1:     LOAD_FAST_BORROW         0 (parsed_lead)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('phone')
              CALL                     1
              STORE_FAST               2 (phone)

258           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (phone)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (phone)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

259   L2:     LOAD_CONST               1 (None)
              RETURN_VALUE

260   L3:     LOAD_FAST_BORROW         0 (parsed_lead)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               3 ('metadata')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L4:     STORE_FAST               3 (metadata)

261           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (metadata)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN

262           BUILD_MAP                0
              STORE_FAST               3 (metadata)

263   L5:     LOAD_GLOBAL             11 (NormalizedLead + NULL)

264           LOAD_FAST_BORROW         2 (phone)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0

265           LOAD_CONST               4 ('manual')

266           LOAD_FAST_BORROW         0 (parsed_lead)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               5 ('full_name')
              CALL                     1

267           LOAD_FAST_BORROW         0 (parsed_lead)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               6 ('first_name')
              CALL                     1

268           LOAD_FAST_BORROW         0 (parsed_lead)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               7 ('last_name')
              CALL                     1

269           LOAD_FAST_BORROW         0 (parsed_lead)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               8 ('email')
              CALL                     1

270           LOAD_FAST_BORROW         0 (parsed_lead)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               9 ('intent')
              CALL                     1

271           LOAD_FAST_BORROW         0 (parsed_lead)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST              10 ('property_address')
              CALL                     1

272           LOAD_FAST_BORROW         0 (parsed_lead)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST              11 ('city')
              CALL                     1

273           LOAD_FAST_BORROW         0 (parsed_lead)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST              12 ('state')
              CALL                     1

274           LOAD_FAST_BORROW         0 (parsed_lead)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST              13 ('budget')
              CALL                     1

275           LOAD_FAST_BORROW         0 (parsed_lead)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST              14 ('timeline')
              CALL                     1

276           LOAD_FAST_BORROW         0 (parsed_lead)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST              15 ('notes')
              CALL                     1

277           LOAD_FAST_BORROW         0 (parsed_lead)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST              16 ('raw_source_ref')
              CALL                     1

278           LOAD_GLOBAL              3 (dict + NULL)
              LOAD_FAST_BORROW         3 (metadata)
              CALL                     1

263           LOAD_CONST              17 (('phone', 'source', 'full_name', 'first_name', 'last_name', 'email', 'intent', 'property_address', 'city', 'state', 'budget', 'timeline', 'notes', 'raw_source_ref', 'metadata'))
              CALL_KW                 15
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app\services\ingestion\email_ingestion.py", line 282>:
282           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('raw_email')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _coerce_email_components at 0x0000018C17ED5770, file "app\services\ingestion\email_ingestion.py", line 282>:
 282            RESUME                   0

 287            LOAD_CONST               1 ('subject')
                LOAD_CONST               2 (None)
                LOAD_CONST               3 ('sender')
                LOAD_CONST               2 (None)
                LOAD_CONST               4 ('body')
                LOAD_CONST               2 (None)
                BUILD_MAP                3
                STORE_FAST               1 (out)

 288            NOP

 289    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (raw_email)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L3)
                NOT_TAKEN

 290            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (raw_email, out)
                LOAD_CONST               4 ('body')
                STORE_SUBSCR

 307    L2:     LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 291    L3:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (raw_email)
                LOAD_GLOBAL              4 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      236 (to L21)
                NOT_TAKEN

 292            LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               1 ('subject')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L6)
        L4:     NOT_TAKEN
        L5:     POP_TOP
                LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               5 ('Subject')
                CALL                     1
        L6:     LOAD_FAST_BORROW         1 (out)
                LOAD_CONST               1 ('subject')
                STORE_SUBSCR

 294            LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               3 ('sender')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        43 (to L11)
        L7:     NOT_TAKEN
        L8:     POP_TOP

 295            LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               6 ('from')
                CALL                     1

 294            COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP

 296            LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               7 ('From')
                CALL                     1

 293   L11:     LOAD_FAST_BORROW         1 (out)
                LOAD_CONST               3 ('sender')
                STORE_SUBSCR

 299            LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               4 ('body')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        93 (to L20)
       L12:     NOT_TAKEN
       L13:     POP_TOP

 300            LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               8 ('text')
                CALL                     1

 299            COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        68 (to L20)
       L14:     NOT_TAKEN
       L15:     POP_TOP

 301            LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               9 ('body_plain')
                CALL                     1

 299            COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        43 (to L20)
       L16:     NOT_TAKEN
       L17:     POP_TOP

 302            LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST              10 ('html')
                CALL                     1

 299            COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L20)
       L18:     NOT_TAKEN
       L19:     POP_TOP

 303            LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST              11 ('body_html')
                CALL                     1

 298   L20:     LOAD_FAST_BORROW         1 (out)
                LOAD_CONST               4 ('body')
                STORE_SUBSCR

 307   L21:     LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L22:     PUSH_EXC_INFO

 305            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L24)
                NOT_TAKEN
                POP_TOP

 306   L23:     POP_EXCEPT

 307            LOAD_FAST                1 (out)
                RETURN_VALUE

 305   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L22 [0]
  L3 to L4 -> L22 [0]
  L5 to L7 -> L22 [0]
  L8 to L9 -> L22 [0]
  L10 to L12 -> L22 [0]
  L13 to L14 -> L22 [0]
  L15 to L16 -> L22 [0]
  L17 to L18 -> L22 [0]
  L19 to L21 -> L22 [0]
  L22 to L23 -> L25 [1] lasti
  L24 to L25 -> L25 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app\services\ingestion\email_ingestion.py", line 314>:
314           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

316           LOAD_CONST               2 ('str')

314           LOAD_CONST               3 ('dedupe_key')

317           LOAD_CONST               2 ('str')

314           LOAD_CONST               4 ('source')

318           LOAD_CONST               2 ('str')

314           LOAD_CONST               5 ('return')

319           LOAD_CONST               6 ('Dict[str, Any]')

314           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _attempt_durable_register at 0x0000018C17ED5AC0, file "app\services\ingestion\email_ingestion.py", line 314>:
 314            RESUME                   0

 334            BUILD_LIST               0
                STORE_FAST               3 (warnings)

 335            NOP

 336    L1:     LOAD_GLOBAL              1 (register_email_dedupe_key + NULL)

 337            LOAD_FAST_BORROW         0 (brokerage_id)

 338            LOAD_FAST_BORROW         1 (dedupe_key)

 339            LOAD_FAST_BORROW         2 (source)

 336            LOAD_CONST               1 (('brokerage_id', 'dedupe_key', 'source'))
                CALL_KW                  3
                STORE_FAST               4 (env)

 354    L2:     LOAD_GLOBAL             13 (isinstance + NULL)
                LOAD_FAST                4 (env)
                LOAD_GLOBAL             14 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L3)
                NOT_TAKEN

 356            LOAD_CONST               3 ('outcome')
                LOAD_CONST               4 ('fallback')

 357            LOAD_CONST               5 ('durable')
                LOAD_CONST               6 (False)

 358            LOAD_CONST               7 ('warnings')

 359            LOAD_CONST               8 ('durable_email_dedupe_unavailable')

 360            LOAD_CONST              10 ('email_dedupe_fallback_process_local')

 358            BUILD_LIST               2

 355            BUILD_MAP                3
                RETURN_VALUE

 363    L3:     LOAD_FAST                4 (env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                STORE_FAST               6 (status)

 364            LOAD_FAST                6 (status)
                LOAD_CONST              13 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE      108 (to L7)
                NOT_TAKEN

 365            LOAD_FAST                4 (env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              14 ('duplicate')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       43 (to L5)
                NOT_TAKEN

 367            LOAD_CONST               3 ('outcome')
                LOAD_CONST              14 ('duplicate')

 368            LOAD_CONST               5 ('durable')
                LOAD_CONST              15 (True)

 369            LOAD_CONST               7 ('warnings')
                LOAD_GLOBAL             19 (list + NULL)
                LOAD_FAST                4 (env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               7 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L4:     CALL                     1

 366            BUILD_MAP                3
                RETURN_VALUE

 372    L5:     LOAD_CONST               3 ('outcome')
                LOAD_CONST              16 ('registered')

 373            LOAD_CONST               5 ('durable')
                LOAD_CONST              15 (True)

 374            LOAD_CONST               7 ('warnings')
                LOAD_GLOBAL             19 (list + NULL)
                LOAD_FAST                4 (env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               7 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L6:     CALL                     1

 371            BUILD_MAP                3
                RETURN_VALUE

 377    L7:     LOAD_GLOBAL             19 (list + NULL)
                LOAD_FAST                4 (env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               7 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L8:     CALL                     1
                STORE_FAST               7 (warns)

 378            LOAD_CONST              10 ('email_dedupe_fallback_process_local')
                LOAD_FAST                7 (warns)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       18 (to L9)
                NOT_TAKEN

 379            LOAD_FAST                7 (warns)
                LOAD_ATTR               21 (append + NULL|self)
                LOAD_CONST              10 ('email_dedupe_fallback_process_local')
                CALL                     1
                POP_TOP

 381    L9:     LOAD_CONST               3 ('outcome')
                LOAD_CONST               4 ('fallback')

 382            LOAD_CONST               5 ('durable')
                LOAD_CONST               6 (False)

 383            LOAD_CONST               7 ('warnings')
                LOAD_FAST                7 (warns)

 380            BUILD_MAP                3
                RETURN_VALUE

  --   L10:     PUSH_EXC_INFO

 341            LOAD_GLOBAL              2 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       87 (to L15)
                NOT_TAKEN
                STORE_FAST               5 (e)

 342   L11:     LOAD_GLOBAL              4 (logger)
                LOAD_ATTR                7 (warning + NULL|self)

 343            LOAD_CONST               2 ('_attempt_durable_register unexpected error type=')
                LOAD_GLOBAL              9 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               10 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 342            CALL                     1
                POP_TOP

 346            LOAD_CONST               3 ('outcome')
                LOAD_CONST               4 ('fallback')

 347            LOAD_CONST               5 ('durable')
                LOAD_CONST               6 (False)

 348            LOAD_CONST               7 ('warnings')

 349            LOAD_CONST               8 ('durable_email_dedupe_unavailable')

 350            LOAD_CONST               9 ('durable_register_exception:')
                LOAD_GLOBAL              9 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               10 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 351            LOAD_CONST              10 ('email_dedupe_fallback_process_local')

 348            BUILD_LIST               3

 345            BUILD_MAP                3
       L12:     SWAP                     2
       L13:     POP_EXCEPT
                LOAD_CONST              11 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RETURN_VALUE

  --   L14:     LOAD_CONST              11 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 341   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L10 [0]
  L10 to L11 -> L16 [1] lasti
  L11 to L12 -> L14 [1] lasti
  L12 to L13 -> L16 [1] lasti
  L14 to L16 -> L16 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024D30, file "app\services\ingestion\email_ingestion.py", line 387>:
387           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('dedupe_key')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('source')
              LOAD_CONST               2 ('str')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('Dict[str, Any]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _process_local_register at 0x0000018C17ED5E60, file "app\services\ingestion\email_ingestion.py", line 387>:
 387            RESUME                   0

 391            BUILD_LIST               0
                STORE_FAST               2 (warnings)

 392            NOP

 393    L1:     LOAD_GLOBAL              1 (register_email_lead_dedupe + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (dedupe_key, source)
                LOAD_CONST               1 (('source',))
                CALL_KW                  2
                STORE_FAST               3 (env)

 405    L2:     LOAD_GLOBAL             13 (isinstance + NULL)
                LOAD_FAST                3 (env)
                LOAD_GLOBAL             14 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         9 (to L3)
                NOT_TAKEN

 407            LOAD_CONST               3 ('outcome')
                LOAD_CONST               4 ('registered')

 408            LOAD_CONST               5 ('durable')
                LOAD_CONST               6 (False)

 409            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 406            BUILD_MAP                3
                RETURN_VALUE

 411    L3:     LOAD_FAST                3 (env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              10 ('status')
                CALL                     1
                STORE_FAST               5 (status)

 412            LOAD_FAST                5 (status)
                LOAD_CONST              11 ('duplicate')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       43 (to L5)
                NOT_TAKEN

 414            LOAD_CONST               3 ('outcome')
                LOAD_CONST              11 ('duplicate')

 415            LOAD_CONST               5 ('durable')
                LOAD_CONST               6 (False)

 416            LOAD_CONST               7 ('warnings')
                LOAD_GLOBAL             19 (list + NULL)
                LOAD_FAST                3 (env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               7 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L4:     CALL                     1

 413            BUILD_MAP                3
                RETURN_VALUE

 419    L5:     LOAD_CONST               3 ('outcome')
                LOAD_CONST               4 ('registered')

 420            LOAD_CONST               5 ('durable')
                LOAD_CONST               6 (False)

 421            LOAD_CONST               7 ('warnings')
                LOAD_GLOBAL             19 (list + NULL)
                LOAD_FAST                3 (env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               7 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L6:     CALL                     1

 418            BUILD_MAP                3
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 394            LOAD_GLOBAL              2 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       85 (to L12)
                NOT_TAKEN
                STORE_FAST               4 (e)

 395    L8:     LOAD_GLOBAL              4 (logger)
                LOAD_ATTR                7 (warning + NULL|self)

 396            LOAD_CONST               2 ('_process_local_register error type=')
                LOAD_GLOBAL              9 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               10 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 395            CALL                     1
                POP_TOP

 399            LOAD_CONST               3 ('outcome')
                LOAD_CONST               4 ('registered')

 400            LOAD_CONST               5 ('durable')
                LOAD_CONST               6 (False)

 401            LOAD_CONST               7 ('warnings')

 402            LOAD_CONST               8 ('process_local_register_failed:')
                LOAD_GLOBAL              9 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               10 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 401            BUILD_LIST               1

 398            BUILD_MAP                3
        L9:     SWAP                     2
       L10:     POP_EXCEPT
                LOAD_CONST               9 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RETURN_VALUE

  --   L11:     LOAD_CONST               9 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 394   L12:     RERAISE                  0

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L7 [0]
  L7 to L8 -> L13 [1] lasti
  L8 to L9 -> L11 [1] lasti
  L9 to L10 -> L13 [1] lasti
  L11 to L13 -> L13 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18090140, file "app\services\ingestion\email_ingestion.py", line 429>:
429           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

430           LOAD_CONST               2 ('Any')

429           LOAD_CONST               3 ('raw_email')

431           LOAD_CONST               2 ('Any')

429           LOAD_CONST               4 ('source_hint')

433           LOAD_CONST               5 ('Optional[str]')

429           LOAD_CONST               6 ('forwarder_signature')

434           LOAD_CONST               5 ('Optional[str]')

429           LOAD_CONST               7 ('forwarder_secret')

435           LOAD_CONST               5 ('Optional[str]')

429           LOAD_CONST               8 ('brokerage')

436           LOAD_CONST               9 ('Optional[Dict[str, Any]]')

429           LOAD_CONST              10 ('return')

437           LOAD_CONST              11 ('Dict[str, Any]')

429           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object ingest_email_lead at 0x0000018C17D7FBE0, file "app\services\ingestion\email_ingestion.py", line 429>:
 429            RESUME                   0

 465            LOAD_GLOBAL              1 (isinstance + NULL)
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
                POP_JUMP_IF_TRUE        16 (to L2)
                NOT_TAKEN

 466    L1:     LOAD_GLOBAL              7 (_failed + NULL)

 467            LOAD_CONST               1 (None)

 468            LOAD_CONST               2 ('generic_email')

 469            LOAD_CONST               3 ('missing_brokerage_id')
                BUILD_LIST               1

 466            LOAD_CONST               4 (('brokerage_id', 'source', 'errors'))
                CALL_KW                  3
                RETURN_VALUE

 471    L2:     LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               6 (bid)

 475            LOAD_GLOBAL              9 (email_forwarder_signature_required + NULL)
                LOAD_FAST_BORROW         5 (brokerage)
                CALL                     1
                STORE_FAST               7 (forwarder_required)

 478            NOP

 479    L3:     LOAD_GLOBAL             11 (parse_email_lead + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (raw_email, source_hint)
                LOAD_CONST               5 (('source_hint',))
                CALL_KW                  2
                STORE_FAST               8 (parsed)

 492    L4:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST                8 (parsed)
                LOAD_GLOBAL             22 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        17 (to L5)
                NOT_TAKEN

 493            LOAD_GLOBAL              7 (_failed + NULL)

 494            LOAD_FAST                6 (bid)

 495            LOAD_CONST               2 ('generic_email')

 496            LOAD_CONST               9 ('parser_returned_non_dict')
                BUILD_LIST               1

 497            LOAD_FAST                7 (forwarder_required)

 493            LOAD_CONST               8 (('brokerage_id', 'source', 'errors', 'forwarder_required'))
                CALL_KW                  4
                RETURN_VALUE

 500    L5:     LOAD_FAST                8 (parsed)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              10 ('source')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('generic_email')
        L6:     STORE_FAST              10 (source)

 501            LOAD_FAST               10 (source)
                LOAD_GLOBAL             26 (ALLOWED_EMAIL_LEAD_SOURCES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN

 502            LOAD_CONST               2 ('generic_email')
                STORE_FAST              10 (source)

 504    L7:     LOAD_GLOBAL             29 (list + NULL)
                LOAD_FAST                8 (parsed)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              11 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L8:     CALL                     1
                STORE_FAST              11 (parser_warnings)

 505            LOAD_GLOBAL             29 (list + NULL)
                LOAD_FAST                8 (parsed)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              12 ('errors')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L9:     CALL                     1
                STORE_FAST              12 (parser_errors)

 508            LOAD_GLOBAL             31 (_coerce_email_components + NULL)
                LOAD_FAST                1 (raw_email)
                CALL                     1
                STORE_FAST              13 (components)

 509            LOAD_GLOBAL             33 (verify_forwarder_signature + NULL)

 510            LOAD_FAST               13 (components)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              13 ('sender')
                CALL                     1

 511            LOAD_FAST               13 (components)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              14 ('subject')
                CALL                     1

 512            LOAD_FAST               13 (components)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              15 ('body')
                CALL                     1

 513            LOAD_FAST                3 (forwarder_signature)

 514            LOAD_FAST                4 (forwarder_secret)

 509            LOAD_CONST              16 (('sender', 'subject', 'body', 'provided_signature', 'secret'))
                CALL_KW                  5
                STORE_FAST              14 (sig_envelope)

 516            LOAD_GLOBAL             35 (bool + NULL)
                LOAD_FAST               14 (sig_envelope)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              17 ('verified')
                CALL                     1
                CALL                     1
                STORE_FAST              15 (forwarder_verified)

 517            LOAD_GLOBAL             29 (list + NULL)
                LOAD_FAST               14 (sig_envelope)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              11 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L10:     CALL                     1
                STORE_FAST              16 (sig_warnings)

 518            LOAD_FAST               14 (sig_envelope)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              18 ('error_code')
                CALL                     1
                STORE_FAST              17 (sig_error)

 521            LOAD_FAST                7 (forwarder_required)
                TO_BOOL
                POP_JUMP_IF_FALSE       65 (to L12)
                NOT_TAKEN

 523            LOAD_CONST              19 ('forwarder_signature_unconfigured')
                LOAD_FAST               16 (sig_warnings)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       26 (to L11)
                NOT_TAKEN

 524            LOAD_GLOBAL              7 (_failed + NULL)

 525            LOAD_FAST                6 (bid)

 526            LOAD_FAST               10 (source)

 527            LOAD_FAST               11 (parser_warnings)
                LOAD_FAST               16 (sig_warnings)
                BINARY_OP                0 (+)

 528            LOAD_CONST              20 ('forwarder_secret_missing')
                BUILD_LIST               1

 529            LOAD_CONST              21 (False)

 530            LOAD_CONST              22 (True)

 524            LOAD_CONST              23 (('brokerage_id', 'source', 'warnings', 'errors', 'forwarder_verified', 'forwarder_required'))
                CALL_KW                  6
                RETURN_VALUE

 533   L11:     LOAD_CONST              24 ('forwarder_signature_missing')
                LOAD_FAST               16 (sig_warnings)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       26 (to L12)
                NOT_TAKEN

 534            LOAD_GLOBAL              7 (_failed + NULL)

 535            LOAD_FAST                6 (bid)

 536            LOAD_FAST               10 (source)

 537            LOAD_FAST               11 (parser_warnings)
                LOAD_FAST               16 (sig_warnings)
                BINARY_OP                0 (+)

 538            LOAD_CONST              25 ('forwarder_signature_required')
                BUILD_LIST               1

 539            LOAD_CONST              21 (False)

 540            LOAD_CONST              22 (True)

 534            LOAD_CONST              23 (('brokerage_id', 'source', 'warnings', 'errors', 'forwarder_verified', 'forwarder_required'))
                CALL_KW                  6
                RETURN_VALUE

 546   L12:     LOAD_FAST               14 (sig_envelope)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              26 ('valid')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        38 (to L14)
                NOT_TAKEN

 547            LOAD_FAST               11 (parser_warnings)
                LOAD_FAST               16 (sig_warnings)
                BINARY_OP                0 (+)
                STORE_FAST              18 (combined)

 548            LOAD_GLOBAL              7 (_failed + NULL)

 549            LOAD_FAST                6 (bid)

 550            LOAD_FAST               10 (source)

 551            LOAD_FAST               18 (combined)

 552            LOAD_FAST               17 (sig_error)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              27 ('forwarder_signature_invalid')
       L13:     BUILD_LIST               1

 553            LOAD_CONST              21 (False)

 554            LOAD_FAST                7 (forwarder_required)

 548            LOAD_CONST              23 (('brokerage_id', 'source', 'warnings', 'errors', 'forwarder_verified', 'forwarder_required'))
                CALL_KW                  6
                RETURN_VALUE

 558   L14:     LOAD_FAST                8 (parsed)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              28 ('status')
                CALL                     1
                LOAD_CONST              29 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       36 (to L16)
                NOT_TAKEN

 559            LOAD_GLOBAL              7 (_failed + NULL)

 560            LOAD_FAST                6 (bid)

 561            LOAD_FAST               10 (source)

 562            LOAD_FAST               11 (parser_warnings)
                LOAD_FAST               16 (sig_warnings)
                BINARY_OP                0 (+)

 563            LOAD_FAST               12 (parser_errors)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         4 (to L15)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              30 ('email_parse_failed')
                BUILD_LIST               1

 564   L15:     LOAD_FAST               15 (forwarder_verified)

 565            LOAD_FAST                7 (forwarder_required)

 559            LOAD_CONST              23 (('brokerage_id', 'source', 'warnings', 'errors', 'forwarder_verified', 'forwarder_required'))
                CALL_KW                  6
                RETURN_VALUE

 568   L16:     LOAD_FAST                8 (parsed)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              31 ('lead')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L17)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
       L17:     STORE_FAST              19 (parsed_lead)

 569            LOAD_GLOBAL             35 (bool + NULL)
                LOAD_FAST                8 (parsed)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              32 ('call_eligible')
                CALL                     1
                CALL                     1
                STORE_FAST              20 (call_eligible)

 572            BUILD_LIST               0
                STORE_FAST              21 (dedupe_warnings)

 573            LOAD_CONST              21 (False)
                STORE_FAST              22 (dedupe_durable_used)

 574            LOAD_CONST              33 ('registered')
                STORE_FAST              23 (dedupe_outcome)

 575            NOP

 576   L18:     LOAD_GLOBAL             37 (build_email_dedupe_key + NULL)

 577            LOAD_FAST               10 (source)

 578            LOAD_FAST               13 (components)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              13 ('sender')
                CALL                     1

 579            LOAD_FAST               13 (components)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              14 ('subject')
                CALL                     1

 580            LOAD_FAST               13 (components)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              15 ('body')
                CALL                     1

 581            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST               19 (parsed_lead)
                LOAD_GLOBAL             22 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L19)
                NOT_TAKEN
                LOAD_FAST               19 (parsed_lead)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              34 ('phone')
                CALL                     1
                JUMP_FORWARD             1 (to L20)
       L19:     LOAD_CONST               1 (None)

 582   L20:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST               19 (parsed_lead)
                LOAD_GLOBAL             22 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L21)
                NOT_TAKEN
                LOAD_FAST               19 (parsed_lead)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              35 ('email')
                CALL                     1
                JUMP_FORWARD             1 (to L22)
       L21:     LOAD_CONST               1 (None)

 576   L22:     LOAD_CONST              36 (('source', 'sender', 'subject', 'body', 'phone', 'email'))
                CALL_KW                  6
                STORE_FAST              24 (dedupe_key)

 594   L23:     LOAD_FAST               24 (dedupe_key)
                TO_BOOL
                POP_JUMP_IF_FALSE      222 (to L34)
                NOT_TAKEN
                LOAD_GLOBAL             41 (durable_email_dedupe_enabled + NULL)
                LOAD_FAST                5 (brokerage)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE      205 (to L34)
                NOT_TAKEN

 595            LOAD_GLOBAL             43 (_attempt_durable_register + NULL)

 596            LOAD_FAST                6 (bid)

 597            LOAD_FAST               24 (dedupe_key)

 598            LOAD_FAST               10 (source)

 595            LOAD_CONST              40 (('brokerage_id', 'dedupe_key', 'source'))
                CALL_KW                  3
                STORE_FAST              25 (durable_result)

 600            LOAD_FAST               25 (durable_result)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              11 ('warnings')
                BUILD_LIST               0
                CALL                     2
                GET_ITER
       L24:     FOR_ITER                29 (to L26)
                STORE_FAST              26 (w)

 601            LOAD_FAST               26 (w)
                LOAD_FAST               21 (dedupe_warnings)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_TRUE         3 (to L25)
                NOT_TAKEN
                JUMP_BACKWARD           12 (to L24)

 602   L25:     LOAD_FAST               21 (dedupe_warnings)
                LOAD_ATTR               39 (append + NULL|self)
                LOAD_FAST               26 (w)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           31 (to L24)

 600   L26:     END_FOR
                POP_ITER

 603            LOAD_FAST               25 (durable_result)
                LOAD_CONST              41 ('outcome')
                BINARY_OP               26 ([])
                LOAD_CONST              42 ('fallback')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       76 (to L30)
                NOT_TAKEN

 606            LOAD_GLOBAL             45 (_process_local_register + NULL)
                LOAD_FAST               24 (dedupe_key)
                LOAD_FAST               10 (source)
                CALL                     2
                STORE_FAST              27 (local_result)

 607            LOAD_FAST               27 (local_result)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              11 ('warnings')
                BUILD_LIST               0
                CALL                     2
                GET_ITER
       L27:     FOR_ITER                29 (to L29)
                STORE_FAST              26 (w)

 608            LOAD_FAST               26 (w)
                LOAD_FAST               21 (dedupe_warnings)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_TRUE         3 (to L28)
                NOT_TAKEN
                JUMP_BACKWARD           12 (to L27)

 609   L28:     LOAD_FAST               21 (dedupe_warnings)
                LOAD_ATTR               39 (append + NULL|self)
                LOAD_FAST               26 (w)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           31 (to L27)

 607   L29:     END_FOR
                POP_ITER

 610            LOAD_FAST               27 (local_result)
                LOAD_CONST              41 ('outcome')
                BINARY_OP               26 ([])
                STORE_FAST              23 (dedupe_outcome)

 611            LOAD_CONST              21 (False)
                STORE_FAST              22 (dedupe_durable_used)
                JUMP_FORWARD           132 (to L38)

 613   L30:     LOAD_FAST               25 (durable_result)
                LOAD_CONST              41 ('outcome')
                BINARY_OP               26 ([])
                STORE_FAST              23 (dedupe_outcome)

 614            LOAD_GLOBAL             35 (bool + NULL)
                LOAD_FAST               25 (durable_result)
                LOAD_CONST              43 ('durable')
                BINARY_OP               26 ([])
                CALL                     1
                STORE_FAST              22 (dedupe_durable_used)

 617            LOAD_FAST               23 (dedupe_outcome)
                LOAD_CONST              44 ('duplicate')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       16 (to L33)
                NOT_TAKEN

 618            NOP

 619   L31:     LOAD_GLOBAL             47 (mark_email_duplicate_seen + NULL)

 620            LOAD_FAST                6 (bid)

 621            LOAD_FAST               24 (dedupe_key)

 619            LOAD_CONST              45 (('brokerage_id', 'dedupe_key'))
                CALL_KW                  2
                POP_TOP
       L32:     JUMP_FORWARD            83 (to L38)

 617   L33:     JUMP_FORWARD            82 (to L38)

 628   L34:     LOAD_FAST               24 (dedupe_key)
                TO_BOOL
                POP_JUMP_IF_FALSE       75 (to L38)
                NOT_TAKEN

 630            LOAD_GLOBAL             45 (_process_local_register + NULL)
                LOAD_FAST               24 (dedupe_key)
                LOAD_FAST               10 (source)
                CALL                     2
                STORE_FAST              27 (local_result)

 631            LOAD_FAST               27 (local_result)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              11 ('warnings')
                BUILD_LIST               0
                CALL                     2
                GET_ITER
       L35:     FOR_ITER                29 (to L37)
                STORE_FAST              26 (w)

 632            LOAD_FAST               26 (w)
                LOAD_FAST               21 (dedupe_warnings)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_TRUE         3 (to L36)
                NOT_TAKEN
                JUMP_BACKWARD           12 (to L35)

 633   L36:     LOAD_FAST               21 (dedupe_warnings)
                LOAD_ATTR               39 (append + NULL|self)
                LOAD_FAST               26 (w)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           31 (to L35)

 631   L37:     END_FOR
                POP_ITER

 634            LOAD_FAST               27 (local_result)
                LOAD_CONST              41 ('outcome')
                BINARY_OP               26 ([])
                STORE_FAST              23 (dedupe_outcome)

 635            LOAD_CONST              21 (False)
                STORE_FAST              22 (dedupe_durable_used)

 637   L38:     LOAD_FAST               23 (dedupe_outcome)
                LOAD_CONST              44 ('duplicate')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       34 (to L39)
                NOT_TAKEN

 638            LOAD_FAST               11 (parser_warnings)
                LOAD_FAST               16 (sig_warnings)
                BINARY_OP                0 (+)
                LOAD_FAST               21 (dedupe_warnings)
                BINARY_OP                0 (+)
                STORE_FAST              18 (combined)

 639            LOAD_GLOBAL             51 (_duplicate + NULL)

 640            LOAD_FAST                6 (bid)

 641            LOAD_FAST               10 (source)

 642            LOAD_FAST               15 (forwarder_verified)

 643            LOAD_FAST                7 (forwarder_required)

 644            LOAD_FAST               22 (dedupe_durable_used)

 645            LOAD_FAST               18 (combined)

 639            LOAD_CONST              47 (('brokerage_id', 'source', 'forwarder_verified', 'forwarder_required', 'dedupe_durable', 'warnings'))
                CALL_KW                  6
                RETURN_VALUE

 648   L39:     LOAD_FAST               20 (call_eligible)
                TO_BOOL
                POP_JUMP_IF_TRUE        87 (to L41)
                NOT_TAKEN

 649            LOAD_CONST              48 ('email_lead_missing_phone')
                LOAD_FAST               11 (parser_warnings)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       18 (to L40)
                NOT_TAKEN

 650            LOAD_FAST               11 (parser_warnings)
                LOAD_ATTR               39 (append + NULL|self)
                LOAD_CONST              48 ('email_lead_missing_phone')
                CALL                     1
                POP_TOP

 651   L40:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               53 (info + NULL|self)

 652            LOAD_CONST              49 ('email_lead_no_phone source=')
                LOAD_FAST               10 (source)
                FORMAT_SIMPLE
                LOAD_CONST              50 (' brokerage=')
                LOAD_FAST                6 (bid)
                FORMAT_SIMPLE
                BUILD_STRING             4

 651            CALL                     1
                POP_TOP

 654            LOAD_GLOBAL             55 (_accepted + NULL)

 655            LOAD_FAST                6 (bid)

 656            LOAD_FAST               10 (source)

 657            LOAD_CONST               1 (None)

 658            LOAD_CONST               1 (None)

 659            LOAD_CONST              21 (False)

 660            LOAD_CONST              21 (False)

 661            LOAD_FAST               15 (forwarder_verified)

 662            LOAD_FAST                7 (forwarder_required)

 663            LOAD_FAST               22 (dedupe_durable_used)

 664            LOAD_FAST               11 (parser_warnings)
                LOAD_FAST               16 (sig_warnings)
                BINARY_OP                0 (+)
                LOAD_FAST               21 (dedupe_warnings)
                BINARY_OP                0 (+)

 654            LOAD_CONST              51 (('brokerage_id', 'source', 'lead_id', 'pending_call_id', 'call_queued', 'call_eligible', 'forwarder_verified', 'forwarder_required', 'dedupe_durable', 'warnings'))
                CALL_KW                 10
                RETURN_VALUE

 668   L41:     NOP

 669   L42:     LOAD_GLOBAL             57 (_normalized_lead_from_parsed + NULL)

 670            LOAD_FAST               19 (parsed_lead)
                LOAD_FAST               10 (source)

 669            LOAD_CONST              52 (('source',))
                CALL_KW                  2
                STORE_FAST              28 (normalized)

 687   L43:     LOAD_FAST               28 (normalized)
                POP_JUMP_IF_NOT_NONE    34 (to L44)
                NOT_TAKEN

 688            LOAD_GLOBAL              7 (_failed + NULL)

 689            LOAD_FAST                6 (bid)

 690            LOAD_FAST               10 (source)

 691            LOAD_FAST               11 (parser_warnings)
                LOAD_FAST               16 (sig_warnings)
                BINARY_OP                0 (+)
                LOAD_FAST               21 (dedupe_warnings)
                BINARY_OP                0 (+)

 692            LOAD_CONST              56 ('lead_object_construction_failed')
                BUILD_LIST               1

 693            LOAD_FAST               15 (forwarder_verified)

 694            LOAD_FAST                7 (forwarder_required)

 695            LOAD_FAST               22 (dedupe_durable_used)

 688            LOAD_CONST              55 (('brokerage_id', 'source', 'warnings', 'errors', 'forwarder_verified', 'forwarder_required', 'dedupe_durable'))
                CALL_KW                  7
                RETURN_VALUE

 699   L44:     NOP

 700   L45:     LOAD_GLOBAL             59 (create_pending_call + NULL)
                LOAD_CONST              57 ('id')
                LOAD_FAST                6 (bid)
                BUILD_MAP                1
                LOAD_FAST               28 (normalized)
                CALL                     2
                STORE_FAST              29 (ack)

 721   L46:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST               29 (ack)
                LOAD_GLOBAL             22 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        34 (to L47)
                NOT_TAKEN

 722            LOAD_GLOBAL              7 (_failed + NULL)

 723            LOAD_FAST                6 (bid)

 724            LOAD_FAST               10 (source)

 725            LOAD_FAST               11 (parser_warnings)
                LOAD_FAST               16 (sig_warnings)
                BINARY_OP                0 (+)
                LOAD_FAST               21 (dedupe_warnings)
                BINARY_OP                0 (+)

 726            LOAD_CONST              61 ('pending_call_create_non_dict')
                BUILD_LIST               1

 727            LOAD_FAST               15 (forwarder_verified)

 728            LOAD_FAST                7 (forwarder_required)

 729            LOAD_FAST               22 (dedupe_durable_used)

 722            LOAD_CONST              55 (('brokerage_id', 'source', 'warnings', 'errors', 'forwarder_verified', 'forwarder_required', 'dedupe_durable'))
                CALL_KW                  7
                RETURN_VALUE

 732   L47:     LOAD_GLOBAL             29 (list + NULL)
                LOAD_FAST               29 (ack)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              11 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L48)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L48:     CALL                     1
                STORE_FAST              30 (ack_warnings)

 734            LOAD_FAST               11 (parser_warnings)
                LOAD_FAST               16 (sig_warnings)
                BINARY_OP                0 (+)
                LOAD_FAST               21 (dedupe_warnings)
                BINARY_OP                0 (+)
                LOAD_FAST               30 (ack_warnings)
                BINARY_OP                0 (+)

 733            STORE_FAST              31 (combined_warnings)

 737            LOAD_FAST               29 (ack)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              28 ('status')
                CALL                     1
                LOAD_CONST              62 ('accepted')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       37 (to L50)
                NOT_TAKEN

 742            LOAD_FAST               23 (dedupe_outcome)
                LOAD_CONST              33 ('registered')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       11 (to L49)
                NOT_TAKEN

 744            LOAD_FAST               31 (combined_warnings)

 745            LOAD_CONST              59 ('email_dedupe_registered_but_pending_call_failed')
                BUILD_LIST               1

 744            BINARY_OP                0 (+)

 743            STORE_FAST              31 (combined_warnings)

 747   L49:     LOAD_GLOBAL              7 (_failed + NULL)

 748            LOAD_FAST                6 (bid)

 749            LOAD_FAST               10 (source)

 750            LOAD_FAST               31 (combined_warnings)

 751            LOAD_CONST              63 ('pending_call_store_unavailable')
                BUILD_LIST               1

 752            LOAD_FAST               15 (forwarder_verified)

 753            LOAD_FAST                7 (forwarder_required)

 754            LOAD_FAST               22 (dedupe_durable_used)

 747            LOAD_CONST              55 (('brokerage_id', 'source', 'warnings', 'errors', 'forwarder_verified', 'forwarder_required', 'dedupe_durable'))
                CALL_KW                  7
                RETURN_VALUE

 757   L50:     LOAD_FAST               29 (ack)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              64 ('pending_call_id')
                CALL                     1
                STORE_FAST              32 (pending_call_id)

 758            LOAD_GLOBAL             35 (bool + NULL)
                LOAD_FAST               29 (ack)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              65 ('call_queued')
                LOAD_CONST              21 (False)
                CALL                     2
                CALL                     1
                STORE_FAST              33 (call_queued)

 760            LOAD_GLOBAL             55 (_accepted + NULL)

 761            LOAD_FAST                6 (bid)

 762            LOAD_FAST               10 (source)

 763            LOAD_CONST               1 (None)

 764            LOAD_FAST               32 (pending_call_id)

 765            LOAD_FAST               33 (call_queued)

 766            LOAD_CONST              22 (True)

 767            LOAD_FAST               15 (forwarder_verified)

 768            LOAD_FAST                7 (forwarder_required)

 769            LOAD_FAST               22 (dedupe_durable_used)

 770            LOAD_FAST               31 (combined_warnings)

 760            LOAD_CONST              51 (('brokerage_id', 'source', 'lead_id', 'pending_call_id', 'call_queued', 'call_eligible', 'forwarder_verified', 'forwarder_required', 'dedupe_durable', 'warnings'))
                CALL_KW                 10
                RETURN_VALUE

  --   L51:     PUSH_EXC_INFO

 480            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       92 (to L56)
                NOT_TAKEN
                STORE_FAST               9 (e)

 481   L52:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 482            LOAD_CONST               6 ('ingest_email_lead parser unexpected error type=')

 483            LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE

 482            BUILD_STRING             2

 481            CALL                     1
                POP_TOP

 485            LOAD_GLOBAL              7 (_failed + NULL)

 486            LOAD_FAST                6 (bid)

 487            LOAD_CONST               2 ('generic_email')

 488            LOAD_CONST               7 ('parser_exception:')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 489            LOAD_FAST                7 (forwarder_required)

 485            LOAD_CONST               8 (('brokerage_id', 'source', 'errors', 'forwarder_required'))
                CALL_KW                  4
       L53:     SWAP                     2
       L54:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RETURN_VALUE

  --   L55:     LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 480   L56:     RERAISE                  0

  --   L57:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L58:     PUSH_EXC_INFO

 584            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       96 (to L62)
                NOT_TAKEN
                STORE_FAST               9 (e)

 585   L59:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 586            LOAD_CONST              37 ('ingest_email_lead dedupe key build error type=')

 587            LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE

 586            BUILD_STRING             2

 585            CALL                     1
                POP_TOP

 589            LOAD_CONST              38 ('')
                STORE_FAST              24 (dedupe_key)

 590            LOAD_FAST               21 (dedupe_warnings)
                LOAD_ATTR               39 (append + NULL|self)
                LOAD_CONST              39 ('dedupe_key_build_failed:')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP
       L60:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                EXTENDED_ARG             3
                JUMP_BACKWARD_NO_INTERRUPT 954 (to L23)

  --   L61:     LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 584   L62:     RERAISE                  0

  --   L63:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L64:     PUSH_EXC_INFO

 623            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L68)
                NOT_TAKEN
                STORE_FAST               9 (e)

 624   L65:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               49 (debug + NULL|self)

 625            LOAD_CONST              46 ('mark_email_duplicate_seen non-critical error type=')

 626            LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE

 625            BUILD_STRING             2

 624            CALL                     1
                POP_TOP
       L66:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 711 (to L38)

  --   L67:     LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 623   L68:     RERAISE                  0

  --   L69:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L70:     PUSH_EXC_INFO

 672            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      109 (to L75)
                NOT_TAKEN
                STORE_FAST               9 (e)

 673   L71:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 674            LOAD_CONST              53 ('ingest_email_lead lead build error type=')

 675            LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE

 674            BUILD_STRING             2

 673            CALL                     1
                POP_TOP

 677            LOAD_GLOBAL              7 (_failed + NULL)

 678            LOAD_FAST                6 (bid)

 679            LOAD_FAST               10 (source)

 680            LOAD_FAST               11 (parser_warnings)
                LOAD_FAST               16 (sig_warnings)
                BINARY_OP                0 (+)
                LOAD_FAST               21 (dedupe_warnings)
                BINARY_OP                0 (+)

 681            LOAD_CONST              54 ('lead_build_failed:')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 682            LOAD_FAST               15 (forwarder_verified)

 683            LOAD_FAST                7 (forwarder_required)

 684            LOAD_FAST               22 (dedupe_durable_used)

 677            LOAD_CONST              55 (('brokerage_id', 'source', 'warnings', 'errors', 'forwarder_verified', 'forwarder_required', 'dedupe_durable'))
                CALL_KW                  7
       L72:     SWAP                     2
       L73:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RETURN_VALUE

  --   L74:     LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 672   L75:     RERAISE                  0

  --   L76:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L77:     PUSH_EXC_INFO

 701            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      140 (to L84)
                NOT_TAKEN
                STORE_FAST               9 (e)

 702   L78:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 703            LOAD_CONST              58 ('ingest_email_lead pending_call create error type=')

 704            LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE

 703            BUILD_STRING             2

 702            CALL                     1
                POP_TOP

 706            LOAD_GLOBAL              7 (_failed + NULL)

 707            LOAD_FAST                6 (bid)

 708            LOAD_FAST               10 (source)

 712            LOAD_FAST               23 (dedupe_outcome)
                LOAD_CONST              33 ('registered')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       25 (to L79)
                NOT_TAKEN

 710            LOAD_FAST               11 (parser_warnings)
                LOAD_FAST               16 (sig_warnings)
                BINARY_OP                0 (+)
                LOAD_FAST               21 (dedupe_warnings)
                BINARY_OP                0 (+)

 711            LOAD_CONST              59 ('email_dedupe_registered_but_pending_call_failed')
                BUILD_LIST               1

 710            BINARY_OP                0 (+)
                JUMP_FORWARD            15 (to L80)

 713   L79:     LOAD_FAST               11 (parser_warnings)
                LOAD_FAST               16 (sig_warnings)
                BINARY_OP                0 (+)
                LOAD_FAST               21 (dedupe_warnings)
                BINARY_OP                0 (+)

 715   L80:     LOAD_CONST              60 ('pending_call_create_failed:')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 716            LOAD_FAST               15 (forwarder_verified)

 717            LOAD_FAST                7 (forwarder_required)

 718            LOAD_FAST               22 (dedupe_durable_used)

 706            LOAD_CONST              55 (('brokerage_id', 'source', 'warnings', 'errors', 'forwarder_verified', 'forwarder_required', 'dedupe_durable'))
                CALL_KW                  7
       L81:     SWAP                     2
       L82:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RETURN_VALUE

  --   L83:     LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 701   L84:     RERAISE                  0

  --   L85:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L51 [0]
  L18 to L23 -> L58 [0]
  L31 to L32 -> L64 [0]
  L42 to L43 -> L70 [0]
  L45 to L46 -> L77 [0]
  L51 to L52 -> L57 [1] lasti
  L52 to L53 -> L55 [1] lasti
  L53 to L54 -> L57 [1] lasti
  L55 to L57 -> L57 [1] lasti
  L58 to L59 -> L63 [1] lasti
  L59 to L60 -> L61 [1] lasti
  L61 to L63 -> L63 [1] lasti
  L64 to L65 -> L69 [1] lasti
  L65 to L66 -> L67 [1] lasti
  L67 to L69 -> L69 [1] lasti
  L70 to L71 -> L76 [1] lasti
  L71 to L72 -> L74 [1] lasti
  L72 to L73 -> L76 [1] lasti
  L74 to L76 -> L76 [1] lasti
  L77 to L78 -> L85 [1] lasti
  L78 to L81 -> L83 [1] lasti
  L81 to L82 -> L85 [1] lasti
  L83 to L85 -> L85 [1] lasti
```
