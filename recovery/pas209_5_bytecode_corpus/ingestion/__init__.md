# ingestion/__init__

- **pyc:** `app\services\ingestion\__pycache__\__init__.cpython-314.pyc`
- **expected source path (absent):** `app\services\ingestion/__init__.py`
- **co_filename (from bytecode):** `app\services\ingestion\__init__.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** ingestion

## Module docstring

```
PAS161 — Lead ingestion subsystem.

Public surface intended to be imported from
``app/routes/lead_ingestion.py`` only. The package provides:

* ``contracts.NormalizedLead`` — the canonical normalized lead
  shape produced by every provider normalizer.
* ``normalizers`` — provider-specific normalizers (generic,
  Zapier, Follow Up Boss, GoHighLevel).
* ``security`` — shared-secret + HMAC verification helpers.
* ``pending_calls`` — enqueue / prepare helpers for the
  durable pending-call handoff layer.

Doctrine carried by every module in this package:

* ``brokerage_id`` is NEVER accepted from a payload. It is
  resolved from auth (``require_brokerage``) only.
* Raw payloads are NEVER stored, logged, or echoed in errors.
* Normalizers are pure; they never raise on malformed input.
* No external vendor / embedding / vector dependencies.
* No Memory Review module is imported or modified.
```

## Imports

`ALLOWED_METADATA_KEYS`, `FORBIDDEN_NORMALIZED_KEYS`, `NormalizedLead`, `PendingCallEnvelope`, `app.services.ingestion.contracts`, `app.services.ingestion.normalizers`, `app.services.ingestion.pending_calls`, `app.services.ingestion.security`, `enqueue_pending_call`, `normalize_followupboss_payload`, `normalize_generic_webhook`, `normalize_gohighlevel_payload`, `normalize_zapier_payload`, `prepare_pending_call`, `verify_hmac_signature`, `verify_shared_secret`

## Classes

_none_

## Functions / methods

_none_

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS161 — Lead ingestion subsystem.\n\nPublic surface intended to be imported from\n``app/routes/lead_ingestion.py`` only. The package provides:\n\n* ``contracts.NormalizedLead`` — the canonical normalized lead\n  shape produced by every provider normalizer.\n* ``normalizers`` — provider-specific normalizers (generic,\n  Zapier, Follow Up Boss, GoHighLevel).\n* ``security`` — shared-secret + HMAC verification helpers.\n* ``pending_calls`` — enqueue / prepare helpers for the\n  durable pending-call handoff layer.\n\nDoctrine carried by every module in this package:\n\n* ``brokerage_id`` is NEVER accepted from a payload. It is\n  resolved from auth (``require_brokerage``) only.\n* Raw payloads are NEVER stored, logged, or echoed in errors.\n* Normalizers are pure; they never raise on malformed input.\n* No external vendor / embedding / vector dependencies.\n* No Memory Review module is imported or modified.\n'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS161 — Lead ingestion subsystem.\n\nPublic surface intended to be imported from\n``app/routes/lead_ingestion.py`` only. The package provides:\n\n* ``contracts.NormalizedLead`` — the canonical normalized lead\n  shape produced by every provider normalizer.\n* ``normalizers`` — provider-specific normalizers (generic,\n  Zapier, Follow Up Boss, GoHighLevel).\n* ``security`` — shared-secret + HMAC verification helpers.\n* ``pending_calls`` — enqueue / prepare helpers for the\n  durable pending-call handoff layer.\n\nDoctrine carried by every module in this package:\n\n* ``brokerage_id`` is NEVER accepted from a payload. It is\n  resolved from auth (``require_brokerage``) only.\n* Raw payloads are NEVER stored, logged, or echoed in errors.\n* Normalizers are pure; they never raise on malformed input.\n* No external vendor / embedding / vector dependencies.\n* No Memory Review module is imported or modified.\n')
              STORE_NAME               0 (__doc__)

 25           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('NormalizedLead', 'ALLOWED_METADATA_KEYS', 'FORBIDDEN_NORMALIZED_KEYS'))
              IMPORT_NAME              1 (app.services.ingestion.contracts)
              IMPORT_FROM              2 (NormalizedLead)
              STORE_NAME               2 (NormalizedLead)
              IMPORT_FROM              3 (ALLOWED_METADATA_KEYS)
              STORE_NAME               3 (ALLOWED_METADATA_KEYS)
              IMPORT_FROM              4 (FORBIDDEN_NORMALIZED_KEYS)
              STORE_NAME               4 (FORBIDDEN_NORMALIZED_KEYS)
              POP_TOP

 30           LOAD_SMALL_INT           0
              LOAD_CONST               2 (('normalize_generic_webhook', 'normalize_zapier_payload', 'normalize_followupboss_payload', 'normalize_gohighlevel_payload'))
              IMPORT_NAME              5 (app.services.ingestion.normalizers)
              IMPORT_FROM              6 (normalize_generic_webhook)
              STORE_NAME               6 (normalize_generic_webhook)
              IMPORT_FROM              7 (normalize_zapier_payload)
              STORE_NAME               7 (normalize_zapier_payload)
              IMPORT_FROM              8 (normalize_followupboss_payload)
              STORE_NAME               8 (normalize_followupboss_payload)
              IMPORT_FROM              9 (normalize_gohighlevel_payload)
              STORE_NAME               9 (normalize_gohighlevel_payload)
              POP_TOP

 36           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('verify_shared_secret', 'verify_hmac_signature'))
              IMPORT_NAME             10 (app.services.ingestion.security)
              IMPORT_FROM             11 (verify_shared_secret)
              STORE_NAME              11 (verify_shared_secret)
              IMPORT_FROM             12 (verify_hmac_signature)
              STORE_NAME              12 (verify_hmac_signature)
              POP_TOP

 40           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('prepare_pending_call', 'enqueue_pending_call', 'PendingCallEnvelope'))
              IMPORT_NAME             13 (app.services.ingestion.pending_calls)
              IMPORT_FROM             14 (prepare_pending_call)
              STORE_NAME              14 (prepare_pending_call)
              IMPORT_FROM             15 (enqueue_pending_call)
              STORE_NAME              15 (enqueue_pending_call)
              IMPORT_FROM             16 (PendingCallEnvelope)
              STORE_NAME              16 (PendingCallEnvelope)
              POP_TOP

 46           BUILD_LIST               0
              LOAD_CONST               6 (('NormalizedLead', 'ALLOWED_METADATA_KEYS', 'FORBIDDEN_NORMALIZED_KEYS', 'normalize_generic_webhook', 'normalize_zapier_payload', 'normalize_followupboss_payload', 'normalize_gohighlevel_payload', 'verify_shared_secret', 'verify_hmac_signature', 'prepare_pending_call', 'enqueue_pending_call', 'PendingCallEnvelope'))
              LIST_EXTEND              1
              STORE_NAME              17 (__all__)
              LOAD_CONST               5 (None)
              RETURN_VALUE
```
