# ingestion/pending_calls

- **pyc:** `app\services\ingestion\__pycache__\pending_calls.cpython-314.pyc`
- **expected source path (absent):** `app\services\ingestion/pending_calls.py`
- **co_filename (from bytecode):** `app\services\ingestion\pending_calls.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** ingestion

## Module docstring

```
PAS161 — Pending-call durability layer (process-local v1).

Doctrine:

* A real production deployment needs a durable ``pending_calls``
  table so an in-flight lead survives a uvicorn restart, crash,
  or rolling deploy. PAS161 ships the **interface** for that
  durability layer plus a **process-local fallback** so
  development / pilot work can proceed today.
* Every enqueue call surfaces a structural warning
  ``pending_calls_store_is_process_local`` so the operator
  cannot accidentally treat the in-memory dict as durable.
* A proposal-only migration script (``scripts/proposal_v14_
  pending_calls.sql``) describes the durable table. PAS161 does
  NOT execute it; promoting the proposal into a real migration
  is a separate phase.
* This layer NEVER stores raw payloads — only the normalised
  envelope (``NormalizedLead.to_dict()`` result, the same
  forbidden-key-stripped projection routes return).
* This layer NEVER auto-dials in PAS161. It accepts and
  records the lead; a future phase wires a dialing worker.
  Every enqueue surfaces ``dial_not_initiated_in_pas161``.
```

## Imports

`Any`, `Dict`, `List`, `NormalizedLead`, `Optional`, `__future__`, `annotations`, `app.db.event_logger`, `app.db.supabase_client`, `app.services.ingestion.contracts`, `app.services.ingestion.pending_call_dedupe`, `app.services.operator.circuit_breaker_policy`, `build_pending_call_dedupe_key`, `dataclass`, `dataclasses`, `datetime`, `field`, `get_supabase`, `log_event_bg`, `logging`, `os`, `register_pending_call_dedupe`, `should_block_new_outbound_for_brokerage`, `threading`, `timezone`, `typing`, `uuid`

## Classes

`PendingCallEnvelope`

## Functions / methods

`__annotate__`, `_brokerage_id_from_brokerage`, `_clamp_list_limit`, `_fallback_to_process_local`, `_get_db_safe`, `_now_iso`, `_peek_pending_calls`, `_reset_pending_calls_for_tests`, `_safe_envelope`, `_update_row_with_tenant_pin`, `cancel_pending_call`, `create_pending_call`, `enqueue_pending_call`, `list_due_pending_calls`, `mark_pending_call_dialed`, `mark_pending_call_dialing`, `mark_pending_call_failed`, `pending_call_row_from_normalized_lead`, `prepare_pending_call`, `validate_pending_call_row`

## Env-key candidates

`CANCELLED`, `DIALED`, `DIALING`, `FAILED`, `PENDING`

## String constants (redacted where noted)

- '\nPAS161 — Pending-call durability layer (process-local v1).\n\nDoctrine:\n\n* A real production deployment needs a durable ``pending_calls``\n  table so an in-flight lead survives a uvicorn restart, crash,\n  or rolling deploy. PAS161 ships the **interface** for that\n  durability layer plus a **process-local fallback** so\n  development / pilot work can proceed today.\n* Every enqueue call surfaces a structural warning\n  ``pending_calls_store_is_process_local`` so the operator\n  cannot accidentally treat the in-memory dict as durable.\n* A proposal-only migration script (``scripts/proposal_v14_\n  pending_calls.sql``) describes the durable table. PAS161 does\n  NOT execute it; promoting the proposal into a real migration\n  is a separate phase.\n* This layer NEVER stores raw payloads — only the normalised\n  envelope (``NormalizedLead.to_dict()`` result, the same\n  forbidden-key-stripped projection routes return).\n* This layer NEVER auto-dials in PAS161. It accepts and\n  records the lead; a future phase wires a dialing worker.\n  Every enqueue surfaces ``dial_not_initiated_in_pas161``.\n'
- 'pas.ingestion.pending_calls'
- 'PendingCallEnvelope'
- 'Dict[str, PendingCallEnvelope]'
- '_PENDING_CALLS'
- 'pas_pending_calls'
- 'pending_call_id'
- 'brokerage_id'
- 'source'
- 'call_queued'
- 'warnings'
- 'extra_warnings'
- "Closed-shape record of one ingested lead awaiting dial.\n\nCarried in the in-memory ``_PENDING_CALLS`` registry. NEVER\nserialised to a database in this phase. NEVER includes raw\npayload, secrets, or fields outside the normalised lead's\nclosed allow-list.\n"
- 'str'
- 'phone'
- 'Dict[str, Any]'
- 'lead'
- 'queued_at'
- 'List[str]'
- 'return'
- 'seconds'
- 'brokerage'
- 'Any'
- 'Optional[str]'
- 'Resolve the canonical brokerage id from whatever shape\n``require_brokerage`` handed back. Defensive — we accept a\ndict (current behaviour) or any object exposing ``.id``.\nNever reads ``brokerage_id`` from a payload.'
- 'normalized_lead'
- 'NormalizedLead'
- 'Build (but do NOT enqueue) a ``PendingCallEnvelope`` for the\ngiven normalised lead.\n\nUse this when the caller wants to inspect / hand off the\nenvelope without immediately writing it to the registry.\n\nRaises ``ValueError`` only on programmer error (missing\n``brokerage`` or wrong ``normalized_lead`` shape). Both\nare surfaced as structural exception classes — the callers\nin this codebase guard against them upstream so this is\nfail-fast for tests, not for runtime.\n'
- 'brokerage_id_unresolved_from_auth'
- 'normalized_lead_not_a_NormalizedLead'
- 'normalized_lead_missing_phone'
- 'unknown'
- 'Record a pending call in the process-local registry and\nreturn a structural acknowledgement.\n\nReturns::\n\n    {\n        "status":          "accepted",\n        "pending_call_id": str,\n        "brokerage_id":    str,\n        "phone":           str,\n        "source":          str,\n        "call_queued":     False,    # PAS161 does not dial\n        "warnings":        [\n            "pending_calls_store_is_process_local",\n            "dial_not_initiated_in_pas161",\n            ... any normalizer warnings ...\n        ],\n    }\n\nNEVER returns the raw payload, the email, the name, or any\nother identifying field beyond ``phone`` (which is the\nminimum needed for an operator to confirm the right lead).\nThe phone is necessarily echoed because it is the dial\ntarget; suppressing it would defeat the acknowledgement.\n'
- 'pending_calls_store_is_process_local'
- 'dial_not_initiated_in_pas161'
- 'pending_call_recorded id='
- ' brokerage='
- ' source='
- 'status'
- 'accepted'
- 'List[Dict[str, Any]]'
- 'Test-only helper: snapshot the current registry contents.\n\nModule-private (underscore prefix). Not part of the public\npackage surface; not exported via ``__init__``. Tests import\nit directly. Production callers must not depend on this.\n'
- 'None'
- 'Test-only helper to flush the registry between tests.\nModule-private; not exported.'
- 'Lazy resolver for the existing Supabase client. Returns\nthe client object or ``None`` if the module / client cannot\nbe imported. Never raises.'
- 'pending_calls db client unavailable type='
- 'Project a ``NormalizedLead`` into a database row dict\ncompatible with the ``pas_pending_calls`` schema.\n\n``brokerage_id`` MUST come from auth — this helper does NOT\nread ``brokerage_id`` from the lead dict. The fact that\n``FORBIDDEN_NORMALIZED_KEYS`` includes ``brokerage_id``\nmeans the dict the normalizer produced cannot carry one;\nthis helper double-pins it.\n'
- 'brokerage_id_required'
- 'manual'
- 'metadata'
- 'lead_id'
- 'lead_phone'
- 'lead_email'
- 'email'
- 'lead_name'
- 'full_name'
- 'intent'
- 'budget'
- 'timeline'
- 'property_address'
- 'PENDING'
- 'attempts'
- 'max_attempts'
- 'row'
- "Return a list of structural error tokens for ``row``.\nEmpty list means ``row`` is a valid pending-call insert\npayload. NEVER echoes the row's values."
- 'row_not_a_dict'
- 'missing_brokerage_id'
- 'missing_lead_phone'
- 'invalid_status'
- 'invalid_source'
- 'invalid_attempts'
- 'invalid_max_attempts'
- 'forbidden_column_in_row'
- 'bool'
- 'Optional[List[str]]'
- 'Closed-shape envelope returned by ``create_pending_call``.\nIdentifying fields beyond ``pending_call_id`` /\n``brokerage_id`` / ``source`` are deliberately omitted —\nno phone / email / name in the public envelope.'
- 'Persist a pending call into the durable ``pas_pending_\ncalls`` table. Falls back safely on DB unavailability.\n\nReturn shape (always 200 from the caller\'s perspective)::\n\n    {\n      "status":          "accepted" | "failed" | "duplicate",\n      "pending_call_id": "<uuid>" | None,\n      "brokerage_id":    "<resolved from auth>",\n      "source":          "<closed enum>",\n      "call_queued":     True  if durable insert succeeded\n                         False if fallback / failure / duplicate,\n      "warnings":        [<structural tokens>],\n    }\n\nDoctrine:\n  * ``brokerage_id`` resolved from ``brokerage`` ONLY.\n  * Phone / email / name NEVER appear in the envelope.\n  * On DB unavailability the row is also written to the\n    PAS161 process-local registry so the operator still has\n    a forensic trail; the warning\n    ``pending_call_store_unavailable`` plus\n    ``pending_calls_store_is_process_local`` surface so\n    nobody mistakes the fallback for the durable path.\n  * On validation failure (e.g. missing phone in the\n    normalized lead) returns ``status="failed"`` with\n    structural error tokens.\n  * **PAS170:** before inserting, the per-brokerage\n    pending-call dedupe registry is consulted. If the\n    same ``(brokerage_id, source, normalised_phone)``\n    tuple was already enqueued within the last 24 h,\n    this helper returns ``status="duplicate"`` with no\n    DB insert and the warning\n    ``duplicate_pending_call_suppressed``. Phone-less\n    leads cannot be deduped structurally — they pass\n    through with ``pending_call_dedupe_skipped_no_phone``.\n'
- 'failed'
- 'circuit_breaker.outbound_blocked'
- 'route'
- 'create_pending_call'
- 'blocked'
- 'action_required'
- 'operator_must_reset_breaker_to_resume'
- 'brokerage_circuit_breaker_tripped'
- 'duplicate'
- 'create_pending_call dedupe layer error type='
- 'pending_call_dedupe_failed:'
- 'row_build_failed:'
- 'ValueError'
- 'create_pending_call row builder unexpected error type='
- 'pending_call_store_unavailable'
- 'data'
- 'pending_call_created id='
- 'pending_call db insert failed (non-critical) brokerage='
- ' type='
- 'db_write_failed:'
- 'Mirror the PAS161 process-local enqueue when the DB path\nrefuses. Surfaces explicit structural warnings so the caller\ncannot mistake the fallback for durable storage. Returns a\nclosed-shape envelope. NEVER raises.'
- 'pending_call fallback envelope build failed type='
- 'fallback_envelope_failed:'
- 'value'
- 'int'
- 'Clamp to [1, _PENDING_CALLS_LIST_MAX].'
- 'limit'
- 'now'
- 'worker_id'
- "Return up to ``limit`` PENDING pending-call rows whose\n``next_attempt_at`` is at or before ``now``. ``brokerage_id``\nis NOT pinned here — the worker drains across tenants, and\nevery per-row write helper still enforces the tenant pin.\n\nOn DB unavailability returns an empty list (the worker\ntreats that as 'nothing to do today, surface warning').\nNever raises."
- 'pending_call_id, brokerage_id, source, lead_id, lead_phone, lead_email, lead_name, intent, budget, timeline, property_address, metadata, status, attempts, max_attempts, next_attempt_at, created_at'
- 'next_attempt_at'
- 'list_due_pending_calls db error (non-critical) type='
- 'patch'
- 'op_label'
- 'Apply ``patch`` to a pending-call row, filtered by BOTH\n``pending_call_id`` and ``brokerage_id``. Returns a closed-\nshape envelope. NEVER reads brokerage_id from elsewhere.\nNEVER raises.'
- 'missing_pending_call_id'
- 'pending_call_not_found_or_cross_tenant'
- ' db error (non-critical) id='
- 'DIALING'
- 'locked_at'
- 'locked_by'
- 'mark_pending_call_dialing'
- 'call_sid'
- 'Transition the row to DIALED. We do NOT store the\nTwilio call_sid as a column in this proposal (would need a\nschema change); a future phase adds it. For now we surface\nit in the envelope only.'
- 'DIALED'
- 'mark_pending_call_dialed'
- 'error_code'
- 'retry'
- 'Transition the row to FAILED (or back to PENDING if\n``retry`` is True and we have attempts remaining). The\nerror_code MUST be a structural identifier (e.g.\n``outbound_dial_adapter_missing`` /\n``twilio_create_failed``); raw exception text must never\nbe passed in here.'
- 'unknown_error'
- 'FAILED'
- 'last_error_code'
- 'last_error_at'
- 'mark_pending_call_failed'
- 'reason'
- 'Operator cancel. Sets status=CANCELLED. ``reason`` is a\nstructural token only (no free-text). Anything else is\ncoerced to ``operator_cancelled``.'
- 'operator_cancelled'
- 'CANCELLED'
- 'cancel_pending_call'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS161 — Pending-call durability layer (process-local v1).\n\nDoctrine:\n\n* A real production deployment needs a durable ``pending_calls``\n  table so an in-flight lead survives a uvicorn restart, crash,\n  or rolling deploy. PAS161 ships the **interface** for that\n  durability layer plus a **process-local fallback** so\n  development / pilot work can proceed today.\n* Every enqueue call surfaces a structural warning\n  ``pending_calls_store_is_process_local`` so the operator\n  cannot accidentally treat the in-memory dict as durable.\n* A proposal-only migration script (``scripts/proposal_v14_\n  pending_calls.sql``) describes the durable table. PAS161 does\n  NOT execute it; promoting the proposal into a real migration\n  is a separate phase.\n* This layer NEVER stores raw payloads — only the normalised\n  envelope (``NormalizedLead.to_dict()`` result, the same\n  forbidden-key-stripped projection routes return).\n* This layer NEVER auto-dials in PAS161. It accepts and\n  records the lead; a future phase wires a dialing worker.\n  Every enqueue surfaces ``dial_not_initiated_in_pas161``.\n')
               STORE_NAME               1 (__doc__)

  26           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  28           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  29           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (threading)
               STORE_NAME               5 (threading)

  30           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (uuid)
               STORE_NAME               6 (uuid)

  31           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('dataclass', 'field'))
               IMPORT_NAME              7 (dataclasses)
               IMPORT_FROM              8 (dataclass)
               STORE_NAME               8 (dataclass)
               IMPORT_FROM              9 (field)
               STORE_NAME               9 (field)
               POP_TOP

  32           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('datetime', 'timezone'))
               IMPORT_NAME             10 (datetime)
               IMPORT_FROM             10 (datetime)
               STORE_NAME              10 (datetime)
               IMPORT_FROM             11 (timezone)
               STORE_NAME              11 (timezone)
               POP_TOP

  33           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('Any', 'Dict', 'List', 'Optional'))
               IMPORT_NAME             12 (typing)
               IMPORT_FROM             13 (Any)
               STORE_NAME              13 (Any)
               IMPORT_FROM             14 (Dict)
               STORE_NAME              14 (Dict)
               IMPORT_FROM             15 (List)
               STORE_NAME              15 (List)
               IMPORT_FROM             16 (Optional)
               STORE_NAME              16 (Optional)
               POP_TOP

  35           LOAD_SMALL_INT           0
               LOAD_CONST               6 (('NormalizedLead',))
               IMPORT_NAME             17 (app.services.ingestion.contracts)
               IMPORT_FROM             18 (NormalizedLead)
               STORE_NAME              18 (NormalizedLead)
               POP_TOP

  37           LOAD_NAME                4 (logging)
               LOAD_ATTR               38 (getLogger)
               PUSH_NULL
               LOAD_CONST               7 ('pas.ingestion.pending_calls')
               CALL                     1
               STORE_NAME              20 (logger)

  44           LOAD_NAME                8 (dataclass)

  45           LOAD_BUILD_CLASS
               PUSH_NULL
               LOAD_CONST               8 (<code object PendingCallEnvelope at 0x0000018C17FE17D0, file "app\services\ingestion\pending_calls.py", line 44>)
               MAKE_FUNCTION
               LOAD_CONST               9 ('PendingCallEnvelope')
               CALL                     2

  44           CALL                     0

  45           STORE_NAME              21 (PendingCallEnvelope)

  84           BUILD_MAP                0
               STORE_NAME              22 (_PENDING_CALLS)
               LOAD_CONST              10 ('Dict[str, PendingCallEnvelope]')
               LOAD_NAME               23 (__annotations__)
               LOAD_CONST              11 ('_PENDING_CALLS')
               STORE_SUBSCR

  85           LOAD_NAME                5 (threading)
               LOAD_ATTR               48 (RLock)
               PUSH_NULL
               CALL                     0
               STORE_NAME              25 (_PENDING_CALLS_LOCK)

  88           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA21F0, file "app\services\ingestion\pending_calls.py", line 88>)
               MAKE_FUNCTION
               LOAD_CONST              13 (<code object _now_iso at 0x0000018C180388F0, file "app\services\ingestion\pending_calls.py", line 88>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              26 (_now_iso)

  92           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA2A60, file "app\services\ingestion\pending_calls.py", line 92>)
               MAKE_FUNCTION
               LOAD_CONST              15 (<code object _brokerage_id_from_brokerage at 0x0000018C17ECEDB0, file "app\services\ingestion\pending_calls.py", line 92>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              27 (_brokerage_id_from_brokerage)

 114           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\ingestion\pending_calls.py", line 114>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object prepare_pending_call at 0x0000018C17F84C90, file "app\services\ingestion\pending_calls.py", line 114>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (prepare_pending_call)

 152           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C18025A30, file "app\services\ingestion\pending_calls.py", line 152>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object enqueue_pending_call at 0x0000018C17E57280, file "app\services\ingestion\pending_calls.py", line 152>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              29 (enqueue_pending_call)

 206           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\ingestion\pending_calls.py", line 206>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _peek_pending_calls at 0x0000018C1804CD30, file "app\services\ingestion\pending_calls.py", line 206>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              30 (_peek_pending_calls)

 217           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\ingestion\pending_calls.py", line 217>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _reset_pending_calls_for_tests at 0x0000018C17972D90, file "app\services\ingestion\pending_calls.py", line 217>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_reset_pending_calls_for_tests)

 256           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME             32 (os)
               STORE_NAME              32 (os)

 258           LOAD_CONST              57 (('PENDING', 'LOCKED', 'DIALING', 'DIALED', 'FAILED', 'CANCELLED'))
               STORE_NAME              33 (ALLOWED_PENDING_CALL_STATUSES)

 262           LOAD_CONST              58 (('generic', 'zapier', 'followupboss', 'gohighlevel', 'manual'))
               STORE_NAME              34 (ALLOWED_PENDING_CALL_SOURCES)

 267           LOAD_SMALL_INT         200
               STORE_NAME              35 (_PENDING_CALLS_LIST_MAX)

 269           LOAD_CONST              24 ('pas_pending_calls')
               STORE_NAME              36 (_TABLE_PENDING_CALLS)

 272           LOAD_CONST              25 (<code object _get_db_safe at 0x0000018C17FF10B0, file "app\services\ingestion\pending_calls.py", line 272>)
               MAKE_FUNCTION
               STORE_NAME              37 (_get_db_safe)

 286           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C18024D30, file "app\services\ingestion\pending_calls.py", line 286>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object pending_call_row_from_normalized_lead at 0x0000018C17ED5190, file "app\services\ingestion\pending_calls.py", line 286>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (pending_call_row_from_normalized_lead)

 331           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3780, file "app\services\ingestion\pending_calls.py", line 331>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object validate_pending_call_row at 0x0000018C17F81560, file "app\services\ingestion\pending_calls.py", line 331>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              39 (validate_pending_call_row)

 371           LOAD_CONST              30 ('pending_call_id')

 374           LOAD_CONST               2 (None)

 371           LOAD_CONST              31 ('brokerage_id')

 375           LOAD_CONST               2 (None)

 371           LOAD_CONST              32 ('source')

 376           LOAD_CONST               2 (None)

 371           LOAD_CONST              33 ('call_queued')

 377           LOAD_CONST              34 (False)

 371           LOAD_CONST              35 ('warnings')

 378           LOAD_CONST               2 (None)

 371           BUILD_MAP                5
               LOAD_CONST              36 (<code object __annotate__ at 0x0000018C180907A0, file "app\services\ingestion\pending_calls.py", line 371>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object _safe_envelope at 0x0000018C180531B0, file "app\services\ingestion\pending_calls.py", line 371>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              40 (_safe_envelope)

 394           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C18025230, file "app\services\ingestion\pending_calls.py", line 394>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object create_pending_call at 0x0000018C17ED7A80, file "app\services\ingestion\pending_calls.py", line 394>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (create_pending_call)

 613           LOAD_CONST              40 ('extra_warnings')

 618           LOAD_CONST               2 (None)

 613           BUILD_MAP                1
               LOAD_CONST              41 (<code object __annotate__ at 0x0000018C18025B30, file "app\services\ingestion\pending_calls.py", line 613>)
               MAKE_FUNCTION
               LOAD_CONST              42 (<code object _fallback_to_process_local at 0x0000018C17E57B50, file "app\services\ingestion\pending_calls.py", line 613>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              42 (_fallback_to_process_local)

 657           LOAD_CONST              43 (<code object __annotate__ at 0x0000018C17FA3870, file "app\services\ingestion\pending_calls.py", line 657>)
               MAKE_FUNCTION
               LOAD_CONST              44 (<code object _clamp_list_limit at 0x0000018C18010B30, file "app\services\ingestion\pending_calls.py", line 657>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_clamp_list_limit)

 672           LOAD_CONST              59 ((50, None, None))
               LOAD_CONST              45 (<code object __annotate__ at 0x0000018C18025030, file "app\services\ingestion\pending_calls.py", line 672>)
               MAKE_FUNCTION
               LOAD_CONST              46 (<code object list_due_pending_calls at 0x0000018C17ED6780, file "app\services\ingestion\pending_calls.py", line 672>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              44 (list_due_pending_calls)

 718           LOAD_CONST              47 (<code object __annotate__ at 0x0000018C18024E30, file "app\services\ingestion\pending_calls.py", line 718>)
               MAKE_FUNCTION
               LOAD_CONST              48 (<code object _update_row_with_tenant_pin at 0x0000018C17ED0840, file "app\services\ingestion\pending_calls.py", line 718>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (_update_row_with_tenant_pin)

 786           LOAD_CONST              60 ((None,))
               LOAD_CONST              49 (<code object __annotate__ at 0x0000018C18024F30, file "app\services\ingestion\pending_calls.py", line 786>)
               MAKE_FUNCTION
               LOAD_CONST              50 (<code object mark_pending_call_dialing at 0x0000018C18038A30, file "app\services\ingestion\pending_calls.py", line 786>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              46 (mark_pending_call_dialing)

 802           LOAD_CONST              60 ((None,))
               LOAD_CONST              51 (<code object __annotate__ at 0x0000018C18025530, file "app\services\ingestion\pending_calls.py", line 802>)
               MAKE_FUNCTION
               LOAD_CONST              52 (<code object mark_pending_call_dialed at 0x0000018C17FF0DB0, file "app\services\ingestion\pending_calls.py", line 802>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              47 (mark_pending_call_dialed)

 821           LOAD_CONST              61 ((False,))
               LOAD_CONST              53 (<code object __annotate__ at 0x0000018C18025830, file "app\services\ingestion\pending_calls.py", line 821>)
               MAKE_FUNCTION
               LOAD_CONST              54 (<code object mark_pending_call_failed at 0x0000018C17FF0C30, file "app\services\ingestion\pending_calls.py", line 821>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              48 (mark_pending_call_failed)

 846           LOAD_CONST              60 ((None,))
               LOAD_CONST              55 (<code object __annotate__ at 0x0000018C18025130, file "app\services\ingestion\pending_calls.py", line 846>)
               MAKE_FUNCTION
               LOAD_CONST              56 (<code object cancel_pending_call at 0x0000018C18060A50, file "app\services\ingestion\pending_calls.py", line 846>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              49 (cancel_pending_call)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object PendingCallEnvelope at 0x0000018C17FE17D0, file "app\services\ingestion\pending_calls.py", line 44>:
 44           RESUME                   0
              LOAD_NAME                0 (__name__)
              STORE_NAME               1 (__module__)
              LOAD_CONST               0 ('PendingCallEnvelope')
              STORE_NAME               2 (__qualname__)
              LOAD_SMALL_INT          44
              STORE_NAME               3 (__firstlineno__)
              SETUP_ANNOTATIONS

 46           LOAD_CONST               1 ("Closed-shape record of one ingested lead awaiting dial.\n\nCarried in the in-memory ``_PENDING_CALLS`` registry. NEVER\nserialised to a database in this phase. NEVER includes raw\npayload, secrets, or fields outside the normalised lead's\nclosed allow-list.\n")
              STORE_NAME               4 (__doc__)

 53           LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               3 ('pending_call_id')
              STORE_SUBSCR

 54           LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               4 ('brokerage_id')
              STORE_SUBSCR

 55           LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               5 ('phone')
              STORE_SUBSCR

 56           LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               6 ('source')
              STORE_SUBSCR

 57           LOAD_CONST               7 ('Dict[str, Any]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               8 ('lead')
              STORE_SUBSCR

 58           LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               9 ('queued_at')
              STORE_SUBSCR

 59           LOAD_NAME                6 (field)
              PUSH_NULL
              LOAD_NAME                7 (list)
              LOAD_CONST              10 (('default_factory',))
              CALL_KW                  1
              STORE_NAME               8 (warnings)
              LOAD_CONST              11 ('List[str]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              12 ('warnings')
              STORE_SUBSCR

 61           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA2880, file "app\services\ingestion\pending_calls.py", line 61>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object to_dict at 0x0000018C17FA92F0, file "app\services\ingestion\pending_calls.py", line 61>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME               9 (to_dict)
              LOAD_CONST              15 (())
              STORE_NAME              10 (__static_attributes__)
              LOAD_CONST              16 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app\services\ingestion\pending_calls.py", line 61>:
 61           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object to_dict at 0x0000018C17FA92F0, file "app\services\ingestion\pending_calls.py", line 61>:
 61           RESUME                   0

 63           LOAD_CONST               0 ('pending_call_id')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (pending_call_id)

 64           LOAD_CONST               1 ('brokerage_id')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                2 (brokerage_id)

 65           LOAD_CONST               2 ('phone')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                4 (phone)

 66           LOAD_CONST               3 ('source')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                6 (source)

 67           LOAD_CONST               4 ('lead')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                8 (lead)

 68           LOAD_CONST               5 ('queued_at')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               10 (queued_at)

 69           LOAD_CONST               6 ('warnings')
              LOAD_GLOBAL             13 (list + NULL)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               14 (warnings)
              CALL                     1

 62           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app\services\ingestion\pending_calls.py", line 88>:
 88           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _now_iso at 0x0000018C180388F0, file "app\services\ingestion\pending_calls.py", line 88>:
 88           RESUME                   0

 89           LOAD_GLOBAL              0 (datetime)
              LOAD_ATTR                2 (now)
              PUSH_NULL
              LOAD_GLOBAL              4 (timezone)
              LOAD_ATTR                6 (utc)
              CALL                     1
              LOAD_ATTR                9 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app\services\ingestion\pending_calls.py", line 92>:
 92           RESUME                   0
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
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _brokerage_id_from_brokerage at 0x0000018C17ECEDB0, file "app\services\ingestion\pending_calls.py", line 92>:
 92           RESUME                   0

 97           LOAD_FAST_BORROW         0 (brokerage)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

 98           LOAD_CONST               1 (None)
              RETURN_VALUE

 99   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       80 (to L3)
              NOT_TAKEN

100           LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('id')
              CALL                     1
              STORE_FAST               1 (v)

101           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (v)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       39 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (v)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN

102           LOAD_FAST_BORROW         1 (v)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

103   L2:     LOAD_CONST               1 (None)
              RETURN_VALUE

104   L3:     LOAD_GLOBAL             11 (getattr + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_CONST               2 ('id')
              LOAD_CONST               1 (None)
              CALL                     3
              STORE_FAST               2 (bid)

105           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (bid)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       39 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (bid)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L4)
              NOT_TAKEN

106           LOAD_FAST_BORROW         2 (bid)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

107   L4:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\ingestion\pending_calls.py", line 114>:
114           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')

115           LOAD_CONST               2 ('Any')

114           LOAD_CONST               3 ('normalized_lead')

116           LOAD_CONST               4 ('NormalizedLead')

114           LOAD_CONST               5 ('return')

117           LOAD_CONST               6 ('PendingCallEnvelope')

114           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object prepare_pending_call at 0x0000018C17F84C90, file "app\services\ingestion\pending_calls.py", line 114>:
114           RESUME                   0

130           LOAD_GLOBAL              1 (_brokerage_id_from_brokerage + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              CALL                     1
              STORE_FAST               2 (brokerage_id)

131           LOAD_FAST_BORROW         2 (brokerage_id)
              TO_BOOL
              POP_JUMP_IF_TRUE        12 (to L1)
              NOT_TAKEN

132           LOAD_GLOBAL              3 (ValueError + NULL)
              LOAD_CONST               1 ('brokerage_id_unresolved_from_auth')
              CALL                     1
              RAISE_VARARGS            1

133   L1:     LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (normalized_lead)
              LOAD_GLOBAL              6 (NormalizedLead)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        12 (to L2)
              NOT_TAKEN

134           LOAD_GLOBAL              3 (ValueError + NULL)
              LOAD_CONST               2 ('normalized_lead_not_a_NormalizedLead')
              CALL                     1
              RAISE_VARARGS            1

135   L2:     LOAD_FAST_BORROW         1 (normalized_lead)
              LOAD_ATTR                9 (to_dict + NULL|self)
              CALL                     0
              STORE_FAST               3 (lead_dict)

136           LOAD_FAST_BORROW         3 (lead_dict)
              LOAD_ATTR               11 (get + NULL|self)
              LOAD_CONST               3 ('phone')
              CALL                     1
              STORE_FAST               4 (phone)

137           LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         4 (phone)
              LOAD_GLOBAL             12 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         4 (phone)
              LOAD_ATTR               15 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE        12 (to L4)
              NOT_TAKEN

138   L3:     LOAD_GLOBAL              3 (ValueError + NULL)
              LOAD_CONST               4 ('normalized_lead_missing_phone')
              CALL                     1
              RAISE_VARARGS            1

140   L4:     LOAD_GLOBAL             17 (PendingCallEnvelope + NULL)

141           LOAD_GLOBAL             13 (str + NULL)
              LOAD_GLOBAL             18 (uuid)
              LOAD_ATTR               20 (uuid4)
              PUSH_NULL
              CALL                     0
              CALL                     1

142           LOAD_FAST                2 (brokerage_id)

143           LOAD_FAST_BORROW         4 (phone)
              LOAD_ATTR               15 (strip + NULL|self)
              CALL                     0

144           LOAD_FAST_BORROW         3 (lead_dict)
              LOAD_ATTR               11 (get + NULL|self)
              LOAD_CONST               5 ('source')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               6 ('unknown')

145   L5:     LOAD_FAST_BORROW         3 (lead_dict)

146           LOAD_GLOBAL             23 (_now_iso + NULL)
              CALL                     0

147           BUILD_LIST               0

140           LOAD_CONST               7 (('pending_call_id', 'brokerage_id', 'phone', 'source', 'lead', 'queued_at', 'warnings'))
              CALL_KW                  7
              STORE_FAST               5 (envelope)

149           LOAD_FAST_BORROW         5 (envelope)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app\services\ingestion\pending_calls.py", line 152>:
152           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')

153           LOAD_CONST               2 ('Any')

152           LOAD_CONST               3 ('normalized_lead')

154           LOAD_CONST               4 ('NormalizedLead')

152           LOAD_CONST               5 ('return')

155           LOAD_CONST               6 ('Dict[str, Any]')

152           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object enqueue_pending_call at 0x0000018C17E57280, file "app\services\ingestion\pending_calls.py", line 152>:
 152           RESUME                   0

 181           LOAD_GLOBAL              1 (prepare_pending_call + NULL)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage, normalized_lead)
               CALL                     2
               STORE_FAST               2 (envelope)

 184           LOAD_FAST_BORROW         2 (envelope)
               LOAD_ATTR                2 (warnings)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               1 ('pending_calls_store_is_process_local')
               CALL                     1
               POP_TOP

 185           LOAD_FAST_BORROW         2 (envelope)
               LOAD_ATTR                2 (warnings)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               2 ('dial_not_initiated_in_pas161')
               CALL                     1
               POP_TOP

 187           LOAD_GLOBAL              6 (_PENDING_CALLS_LOCK)
               COPY                     1
               LOAD_SPECIAL             1 (__exit__)
               SWAP                     2
               SWAP                     3
               LOAD_SPECIAL             0 (__enter__)
               CALL                     0
       L1:     POP_TOP

 188           LOAD_FAST_BORROW         2 (envelope)
               LOAD_GLOBAL              8 (_PENDING_CALLS)
               LOAD_FAST_BORROW         2 (envelope)
               LOAD_ATTR               10 (pending_call_id)
               STORE_SUBSCR

 187   L2:     LOAD_CONST               3 (None)
               LOAD_CONST               3 (None)
               LOAD_CONST               3 (None)
               CALL                     3
               POP_TOP

 190   L3:     LOAD_GLOBAL             12 (logger)
               LOAD_ATTR               15 (info + NULL|self)

 191           LOAD_CONST               4 ('pending_call_recorded id=')
               LOAD_FAST_BORROW         2 (envelope)
               LOAD_ATTR               10 (pending_call_id)
               FORMAT_SIMPLE
               LOAD_CONST               5 (' brokerage=')

 192           LOAD_FAST_BORROW         2 (envelope)
               LOAD_ATTR               16 (brokerage_id)
               FORMAT_SIMPLE
               LOAD_CONST               6 (' source=')
               LOAD_FAST_BORROW         2 (envelope)
               LOAD_ATTR               18 (source)
               FORMAT_SIMPLE

 191           BUILD_STRING             6

 190           CALL                     1
               POP_TOP

 196           LOAD_CONST               7 ('status')
               LOAD_CONST               8 ('accepted')

 197           LOAD_CONST               9 ('pending_call_id')
               LOAD_FAST_BORROW         2 (envelope)
               LOAD_ATTR               10 (pending_call_id)

 198           LOAD_CONST              10 ('brokerage_id')
               LOAD_FAST_BORROW         2 (envelope)
               LOAD_ATTR               16 (brokerage_id)

 199           LOAD_CONST              11 ('phone')
               LOAD_FAST_BORROW         2 (envelope)
               LOAD_ATTR               20 (phone)

 200           LOAD_CONST              12 ('source')
               LOAD_FAST_BORROW         2 (envelope)
               LOAD_ATTR               18 (source)

 201           LOAD_CONST              13 ('call_queued')
               LOAD_CONST              14 (False)

 202           LOAD_CONST              15 ('warnings')
               LOAD_GLOBAL             23 (list + NULL)
               LOAD_FAST_BORROW         2 (envelope)
               LOAD_ATTR                2 (warnings)
               CALL                     1

 195           BUILD_MAP                7
               RETURN_VALUE

 187   L4:     PUSH_EXC_INFO
               WITH_EXCEPT_START
               TO_BOOL
               POP_JUMP_IF_TRUE         2 (to L5)
               NOT_TAKEN
               RERAISE                  2
       L5:     POP_TOP
       L6:     POP_EXCEPT
               POP_TOP
               POP_TOP
               POP_TOP
               JUMP_BACKWARD_NO_INTERRUPT 151 (to L3)

  --   L7:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L4 [2] lasti
  L4 to L6 -> L7 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\ingestion\pending_calls.py", line 206>:
206           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('List[Dict[str, Any]]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _peek_pending_calls at 0x0000018C1804CD30, file "app\services\ingestion\pending_calls.py", line 206>:
 206            RESUME                   0

 213            LOAD_GLOBAL              0 (_PENDING_CALLS_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L1:     POP_TOP

 214            LOAD_GLOBAL              2 (_PENDING_CALLS)
                LOAD_ATTR                5 (values + NULL|self)
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      0 (env)
                SWAP                     2
        L2:     BUILD_LIST               0
                SWAP                     2
        L3:     FOR_ITER                18 (to L4)
                STORE_FAST_LOAD_FAST     0 (env, env)
                LOAD_ATTR                7 (to_dict + NULL|self)
                CALL                     0
                LIST_APPEND              2
                JUMP_BACKWARD           20 (to L3)
        L4:     END_FOR
                POP_ITER
        L5:     SWAP                     2
                STORE_FAST               0 (env)

 213    L6:     SWAP                     3
                SWAP                     2
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     3
                POP_TOP
                RETURN_VALUE

  --    L7:     SWAP                     2
                POP_TOP

 214            SWAP                     2
                STORE_FAST               0 (env)
                RERAISE                  0

 213    L8:     PUSH_EXC_INFO
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
  L2 to L5 -> L7 [4]
  L5 to L6 -> L8 [2] lasti
  L7 to L8 -> L8 [2] lasti
  L8 to L10 -> L11 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\ingestion\pending_calls.py", line 217>:
217           RESUME                   0
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

Disassembly of <code object _reset_pending_calls_for_tests at 0x0000018C17972D90, file "app\services\ingestion\pending_calls.py", line 217>:
 217           RESUME                   0

 220           LOAD_GLOBAL              0 (_PENDING_CALLS_LOCK)
               COPY                     1
               LOAD_SPECIAL             1 (__exit__)
               SWAP                     2
               SWAP                     3
               LOAD_SPECIAL             0 (__enter__)
               CALL                     0
       L1:     POP_TOP

 221           LOAD_GLOBAL              2 (_PENDING_CALLS)
               LOAD_ATTR                5 (clear + NULL|self)
               CALL                     0
               POP_TOP

 220   L2:     LOAD_CONST               1 (None)
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

Disassembly of <code object _get_db_safe at 0x0000018C17FF10B0, file "app\services\ingestion\pending_calls.py", line 272>:
 272           RESUME                   0

 276           NOP

 277   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 278           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 279           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 280   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 281           LOAD_CONST               2 ('pending_calls db client unavailable type=')
               LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE
               BUILD_STRING             2

 280           CALL                     1
               POP_TOP

 283   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 279   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024D30, file "app\services\ingestion\pending_calls.py", line 286>:
286           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

287           LOAD_CONST               2 ('Any')

286           LOAD_CONST               3 ('normalized_lead')

288           LOAD_CONST               4 ('NormalizedLead')

286           LOAD_CONST               5 ('return')

289           LOAD_CONST               6 ('Dict[str, Any]')

286           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object pending_call_row_from_normalized_lead at 0x0000018C17ED5190, file "app\services\ingestion\pending_calls.py", line 286>:
286           RESUME                   0

299           LOAD_GLOBAL              1 (isinstance + NULL)
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
              POP_JUMP_IF_TRUE        12 (to L2)
              NOT_TAKEN

300   L1:     LOAD_GLOBAL              7 (ValueError + NULL)
              LOAD_CONST               1 ('brokerage_id_required')
              CALL                     1
              RAISE_VARARGS            1

301   L2:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (normalized_lead)
              LOAD_GLOBAL              8 (NormalizedLead)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        12 (to L3)
              NOT_TAKEN

302           LOAD_GLOBAL              7 (ValueError + NULL)
              LOAD_CONST               2 ('normalized_lead_not_a_NormalizedLead')
              CALL                     1
              RAISE_VARARGS            1

303   L3:     LOAD_FAST_BORROW         1 (normalized_lead)
              LOAD_ATTR               11 (to_dict + NULL|self)
              CALL                     0
              STORE_FAST               2 (lead)

305           LOAD_FAST_BORROW         2 (lead)
              LOAD_ATTR               13 (get + NULL|self)
              LOAD_CONST               3 ('source')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('manual')
      L4:     STORE_FAST               3 (source)

306           LOAD_FAST_BORROW         3 (source)
              LOAD_GLOBAL             14 (ALLOWED_PENDING_CALL_SOURCES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN

307           LOAD_CONST               4 ('manual')
              STORE_FAST               3 (source)

309   L5:     LOAD_FAST_BORROW         2 (lead)
              LOAD_ATTR               13 (get + NULL|self)
              LOAD_CONST               5 ('metadata')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L6:     STORE_FAST               4 (metadata)

310           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         4 (metadata)
              LOAD_GLOBAL             16 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L7)
              NOT_TAKEN

311           BUILD_MAP                0
              STORE_FAST               4 (metadata)

314   L7:     LOAD_CONST               6 ('brokerage_id')
              LOAD_FAST_BORROW         0 (brokerage_id)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0

315           LOAD_CONST               3 ('source')
              LOAD_FAST_BORROW         3 (source)

316           LOAD_CONST               7 ('lead_id')
              LOAD_FAST_BORROW         2 (lead)
              LOAD_ATTR               13 (get + NULL|self)
              LOAD_CONST               7 ('lead_id')
              CALL                     1

317           LOAD_CONST               8 ('lead_phone')
              LOAD_FAST_BORROW         2 (lead)
              LOAD_CONST               9 ('phone')
              BINARY_OP               26 ([])

318           LOAD_CONST              10 ('lead_email')
              LOAD_FAST_BORROW         2 (lead)
              LOAD_ATTR               13 (get + NULL|self)
              LOAD_CONST              11 ('email')
              CALL                     1

319           LOAD_CONST              12 ('lead_name')
              LOAD_FAST_BORROW         2 (lead)
              LOAD_ATTR               13 (get + NULL|self)
              LOAD_CONST              13 ('full_name')
              CALL                     1

320           LOAD_CONST              14 ('intent')
              LOAD_FAST_BORROW         2 (lead)
              LOAD_ATTR               13 (get + NULL|self)
              LOAD_CONST              14 ('intent')
              CALL                     1

321           LOAD_CONST              15 ('budget')
              LOAD_FAST_BORROW         2 (lead)
              LOAD_ATTR               13 (get + NULL|self)
              LOAD_CONST              15 ('budget')
              CALL                     1

322           LOAD_CONST              16 ('timeline')
              LOAD_FAST_BORROW         2 (lead)
              LOAD_ATTR               13 (get + NULL|self)
              LOAD_CONST              16 ('timeline')
              CALL                     1

323           LOAD_CONST              17 ('property_address')
              LOAD_FAST_BORROW         2 (lead)
              LOAD_ATTR               13 (get + NULL|self)
              LOAD_CONST              17 ('property_address')
              CALL                     1

324           LOAD_CONST               5 ('metadata')
              LOAD_FAST_BORROW         4 (metadata)

325           LOAD_CONST              18 ('status')
              LOAD_CONST              19 ('PENDING')

326           LOAD_CONST              20 ('attempts')
              LOAD_SMALL_INT           0

327           LOAD_CONST              21 ('max_attempts')
              LOAD_SMALL_INT           1

313           BUILD_MAP               14
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app\services\ingestion\pending_calls.py", line 331>:
331           RESUME                   0
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
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object validate_pending_call_row at 0x0000018C17F81560, file "app\services\ingestion\pending_calls.py", line 331>:
331            RESUME                   0

335            BUILD_LIST               0
               STORE_FAST               1 (errors)

336            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (row)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L1)
               NOT_TAKEN

337            LOAD_CONST               1 ('row_not_a_dict')
               BUILD_LIST               1
               RETURN_VALUE

338    L1:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               2 ('brokerage_id')
               CALL                     1
               STORE_FAST               2 (bid)

339            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (bid)
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L2)
               NOT_TAKEN
               LOAD_FAST_BORROW         2 (bid)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L3)
               NOT_TAKEN

340    L2:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               3 ('missing_brokerage_id')
               CALL                     1
               POP_TOP

341    L3:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               4 ('lead_phone')
               CALL                     1
               STORE_FAST               3 (phone)

342            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         3 (phone)
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L4)
               NOT_TAKEN
               LOAD_FAST_BORROW         3 (phone)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L5)
               NOT_TAKEN

343    L4:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               5 ('missing_lead_phone')
               CALL                     1
               POP_TOP

344    L5:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               6 ('status')
               LOAD_CONST               7 ('PENDING')
               CALL                     2
               STORE_FAST               4 (status)

345            LOAD_FAST_BORROW         4 (status)
               LOAD_GLOBAL             12 (ALLOWED_PENDING_CALL_STATUSES)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

346            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               8 ('invalid_status')
               CALL                     1
               POP_TOP

347    L6:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               9 ('source')
               CALL                     1
               STORE_FAST               5 (source)

348            LOAD_FAST_BORROW         5 (source)
               LOAD_GLOBAL             14 (ALLOWED_PENDING_CALL_SOURCES)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

349            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              10 ('invalid_source')
               CALL                     1
               POP_TOP

350    L7:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              11 ('attempts')
               LOAD_SMALL_INT           0
               CALL                     2
               STORE_FAST               6 (attempts)

351            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         6 (attempts)
               LOAD_GLOBAL             16 (int)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        8 (to L8)
               NOT_TAKEN
               LOAD_FAST_BORROW         6 (attempts)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       18 (to L9)
               NOT_TAKEN

352    L8:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              12 ('invalid_attempts')
               CALL                     1
               POP_TOP

353    L9:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              13 ('max_attempts')
               LOAD_SMALL_INT           1
               CALL                     2
               STORE_FAST               7 (max_attempts)

354            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         7 (max_attempts)
               LOAD_GLOBAL             16 (int)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        8 (to L10)
               NOT_TAKEN
               LOAD_FAST_BORROW         7 (max_attempts)
               LOAD_SMALL_INT           1
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       18 (to L11)
               NOT_TAKEN

355   L10:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              14 ('invalid_max_attempts')
               CALL                     1
               POP_TOP

357   L11:     LOAD_CONST              16 (('raw_payload', 'transcript', 'evidence', 'metadata_blob', 'messages', 'utterances', 'input_text', 'output_text', 'memory_content', 'raw_text', 'raw_prompt', 'injected_prompt', 'api_key', 'X-API-Key'))
               GET_ITER
      L12:     FOR_ITER                29 (to L14)
               STORE_FAST               8 (forbidden)

365            LOAD_FAST_BORROW_LOAD_FAST_BORROW 128 (forbidden, row)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L13)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L12)

366   L13:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              15 ('forbidden_column_in_row')
               CALL                     1
               POP_TOP

367            POP_TOP

368            LOAD_FAST_BORROW         1 (errors)
               RETURN_VALUE

357   L14:     END_FOR
               POP_ITER

368            LOAD_FAST_BORROW         1 (errors)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180907A0, file "app\services\ingestion\pending_calls.py", line 371>:
371           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

372           LOAD_CONST               2 ('str')

371           LOAD_CONST               3 ('pending_call_id')

374           LOAD_CONST               4 ('Optional[str]')

371           LOAD_CONST               5 ('brokerage_id')

375           LOAD_CONST               4 ('Optional[str]')

371           LOAD_CONST               6 ('source')

376           LOAD_CONST               4 ('Optional[str]')

371           LOAD_CONST               7 ('call_queued')

377           LOAD_CONST               8 ('bool')

371           LOAD_CONST               9 ('warnings')

378           LOAD_CONST              10 ('Optional[List[str]]')

371           LOAD_CONST              11 ('return')

379           LOAD_CONST              12 ('Dict[str, Any]')

371           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C180531B0, file "app\services\ingestion\pending_calls.py", line 371>:
371           RESUME                   0

385           LOAD_CONST               1 ('status')
              LOAD_FAST                0 (status)

386           LOAD_CONST               2 ('pending_call_id')
              LOAD_FAST                1 (pending_call_id)

387           LOAD_CONST               3 ('brokerage_id')
              LOAD_FAST                2 (brokerage_id)

388           LOAD_CONST               4 ('source')
              LOAD_FAST                3 (source)

389           LOAD_CONST               5 ('call_queued')
              LOAD_FAST                4 (call_queued)

390           LOAD_CONST               6 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                5 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

384           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025230, file "app\services\ingestion\pending_calls.py", line 394>:
394           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')

395           LOAD_CONST               2 ('Any')

394           LOAD_CONST               3 ('normalized_lead')

396           LOAD_CONST               4 ('NormalizedLead')

394           LOAD_CONST               5 ('return')

397           LOAD_CONST               6 ('Dict[str, Any]')

394           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object create_pending_call at 0x0000018C17ED7A80, file "app\services\ingestion\pending_calls.py", line 394>:
 394            RESUME                   0

 435            LOAD_GLOBAL              1 (_brokerage_id_from_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               2 (brokerage_id)

 436            LOAD_FAST_BORROW         2 (brokerage_id)
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L1)
                NOT_TAKEN

 437            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 438            LOAD_CONST               1 ('failed')

 439            LOAD_CONST               2 ('brokerage_id_unresolved_from_auth')
                BUILD_LIST               1

 437            LOAD_CONST               3 (('warnings',))
                CALL_KW                  2
                RETURN_VALUE

 457    L1:     NOP

 458    L2:     LOAD_SMALL_INT           0
                LOAD_CONST               4 (('should_block_new_outbound_for_brokerage',))
                IMPORT_NAME              2 (app.services.operator.circuit_breaker_policy)
                IMPORT_FROM              3 (should_block_new_outbound_for_brokerage)
                STORE_FAST               3 (should_block_new_outbound_for_brokerage)
                POP_TOP

 461            LOAD_FAST_BORROW         3 (should_block_new_outbound_for_brokerage)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (brokerage_id)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L7)
        L3:     NOT_TAKEN

 462            NOP

 463    L4:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('log_event_bg',))
                IMPORT_NAME              4 (app.db.event_logger)
                IMPORT_FROM              5 (log_event_bg)
                STORE_FAST               4 (log_event_bg)
                POP_TOP

 464            LOAD_FAST_BORROW         4 (log_event_bg)
                PUSH_NULL
                LOAD_CONST               6 ('circuit_breaker.outbound_blocked')

 465            LOAD_CONST               7 ('brokerage_id')
                LOAD_FAST_BORROW         2 (brokerage_id)

 466            LOAD_CONST               8 ('route')
                LOAD_CONST               9 ('create_pending_call')

 467            LOAD_CONST              10 ('status')
                LOAD_CONST              11 ('blocked')

 468            LOAD_CONST              12 ('action_required')
                LOAD_CONST              13 ('operator_must_reset_breaker_to_resume')

 464            BUILD_MAP                4
                CALL                     2
                POP_TOP

 472    L5:     LOAD_GLOBAL              3 (_safe_envelope + NULL)

 473            LOAD_CONST               1 ('failed')

 474            LOAD_CONST              14 ('brokerage_circuit_breaker_tripped')
                BUILD_LIST               1

 472            LOAD_CONST               3 (('warnings',))
                CALL_KW                  2
        L6:     RETURN_VALUE

 461    L7:     NOP

 489    L8:     NOP

 490    L9:     LOAD_SMALL_INT           0
                LOAD_CONST              15 (('build_pending_call_dedupe_key', 'register_pending_call_dedupe'))
                IMPORT_NAME              7 (app.services.ingestion.pending_call_dedupe)
                IMPORT_FROM              8 (build_pending_call_dedupe_key)
                STORE_FAST               5 (build_pending_call_dedupe_key)
                IMPORT_FROM              9 (register_pending_call_dedupe)
                STORE_FAST               6 (register_pending_call_dedupe)
                POP_TOP

 496            LOAD_GLOBAL             21 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (normalized_lead)
                LOAD_GLOBAL             22 (NormalizedLead)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L10)
                NOT_TAKEN

 495            LOAD_FAST_BORROW         1 (normalized_lead)
                LOAD_ATTR               24 (phone)
                JUMP_FORWARD             1 (to L11)

 496   L10:     LOAD_CONST              16 (None)

 494   L11:     STORE_FAST               7 (_phone_for_dedupe)

 500            LOAD_GLOBAL             21 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (normalized_lead)
                LOAD_GLOBAL             22 (NormalizedLead)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L12)
                NOT_TAKEN

 499            LOAD_FAST_BORROW         1 (normalized_lead)
                LOAD_ATTR               26 (source)
                JUMP_FORWARD             1 (to L13)

 500   L12:     LOAD_CONST              16 (None)

 498   L13:     STORE_FAST               8 (_source_for_dedupe)

 502            LOAD_FAST_BORROW         5 (build_pending_call_dedupe_key)
                PUSH_NULL

 503            LOAD_FAST_BORROW         2 (brokerage_id)

 504            LOAD_FAST_BORROW         8 (_source_for_dedupe)

 505            LOAD_FAST_BORROW         7 (_phone_for_dedupe)

 502            LOAD_CONST              17 (('brokerage_id', 'source', 'phone'))
                CALL_KW                  3
                STORE_FAST               9 (_dedupe_key)

 512            LOAD_FAST_BORROW         6 (register_pending_call_dedupe)
                PUSH_NULL

 513            LOAD_FAST_BORROW         9 (_dedupe_key)

 514            LOAD_FAST_BORROW         8 (_source_for_dedupe)

 515            LOAD_FAST_BORROW         2 (brokerage_id)

 512            LOAD_CONST              18 (('source', 'brokerage_id'))
                CALL_KW                  3
                STORE_FAST              10 (_dedupe_env)

 517            LOAD_FAST_BORROW        10 (_dedupe_env)
                LOAD_ATTR               29 (get + NULL|self)
                LOAD_CONST              10 ('status')
                CALL                     1
                LOAD_CONST              19 ('duplicate')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       61 (to L21)
                NOT_TAKEN

 521            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 522            LOAD_CONST              19 ('duplicate')

 523            LOAD_FAST                2 (brokerage_id)

 524            LOAD_FAST                8 (_source_for_dedupe)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
       L14:     NOT_TAKEN
       L15:     POP_TOP
                LOAD_CONST              20 ('unknown')

 525   L16:     LOAD_CONST              21 (False)

 526            LOAD_GLOBAL             31 (list + NULL)
                LOAD_FAST_BORROW        10 (_dedupe_env)
                LOAD_ATTR               29 (get + NULL|self)
                LOAD_CONST              22 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L19)
       L17:     NOT_TAKEN
       L18:     POP_TOP
                BUILD_LIST               0
       L19:     CALL                     1

 521            LOAD_CONST              23 (('brokerage_id', 'source', 'call_queued', 'warnings'))
                CALL_KW                  5
       L20:     RETURN_VALUE

 528   L21:     LOAD_GLOBAL             31 (list + NULL)
                LOAD_FAST_BORROW        10 (_dedupe_env)
                LOAD_ATTR               29 (get + NULL|self)
                LOAD_CONST              22 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L24)
       L22:     NOT_TAKEN
       L23:     POP_TOP
                BUILD_LIST               0
       L24:     CALL                     1
                STORE_FAST              11 (_dedupe_warnings)

 537   L25:     NOP

 538   L26:     LOAD_GLOBAL             41 (pending_call_row_from_normalized_lead + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (brokerage_id, normalized_lead)
                CALL                     2
                STORE_FAST              13 (row)

 556   L27:     LOAD_GLOBAL             47 (validate_pending_call_row + NULL)
                LOAD_FAST               13 (row)
                CALL                     1
                STORE_FAST              15 (errors)

 557            LOAD_FAST               15 (errors)
                TO_BOOL
                POP_JUMP_IF_FALSE       15 (to L28)
                NOT_TAKEN

 558            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 559            LOAD_CONST               1 ('failed')

 560            LOAD_FAST                2 (brokerage_id)

 561            LOAD_FAST               15 (errors)

 558            LOAD_CONST              28 (('brokerage_id', 'warnings'))
                CALL_KW                  3
                RETURN_VALUE

 564   L28:     LOAD_FAST               13 (row)
                LOAD_CONST              30 ('source')
                BINARY_OP               26 ([])
                STORE_FAST              16 (source)

 567            LOAD_GLOBAL             49 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST              17 (db)

 568            LOAD_FAST               17 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L29)
                NOT_TAKEN

 569            LOAD_GLOBAL             51 (_fallback_to_process_local + NULL)

 570            LOAD_FAST_LOAD_FAST     33 (brokerage_id, normalized_lead)
                LOAD_FAST               16 (source)

 571            LOAD_CONST              31 ('pending_call_store_unavailable')
                BUILD_LIST               1

 569            LOAD_CONST              32 (('extra_warnings',))
                CALL_KW                  4
                RETURN_VALUE

 574   L29:     NOP

 575   L30:     LOAD_FAST               17 (db)
                LOAD_ATTR               53 (table + NULL|self)
                LOAD_GLOBAL             54 (_TABLE_PENDING_CALLS)
                CALL                     1
                LOAD_ATTR               57 (insert + NULL|self)
                LOAD_FAST               13 (row)
                CALL                     1
                LOAD_ATTR               59 (execute + NULL|self)
                CALL                     0
                STORE_FAST              18 (result)

 576            LOAD_GLOBAL             31 (list + NULL)
                LOAD_GLOBAL             61 (getattr + NULL)
                LOAD_FAST               18 (result)
                LOAD_CONST              33 ('data')
                LOAD_CONST              16 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L33)
       L31:     NOT_TAKEN
       L32:     POP_TOP
                BUILD_LIST               0
       L33:     CALL                     1
                STORE_FAST              19 (data)

 577            LOAD_FAST               19 (data)
                TO_BOOL
                POP_JUMP_IF_TRUE        16 (to L37)
       L34:     NOT_TAKEN

 578   L35:     LOAD_GLOBAL             51 (_fallback_to_process_local + NULL)

 579            LOAD_FAST_LOAD_FAST     33 (brokerage_id, normalized_lead)
                LOAD_FAST               16 (source)

 580            LOAD_CONST              31 ('pending_call_store_unavailable')
                BUILD_LIST               1

 578            LOAD_CONST              32 (('extra_warnings',))
                CALL_KW                  4
       L36:     RETURN_VALUE

 582   L37:     LOAD_FAST               19 (data)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_ATTR               29 (get + NULL|self)
                LOAD_CONST              34 ('pending_call_id')
                CALL                     1
                STORE_FAST              20 (pending_call_id)

 583            LOAD_FAST               20 (pending_call_id)
                TO_BOOL
                POP_JUMP_IF_TRUE        16 (to L41)
       L38:     NOT_TAKEN

 585   L39:     LOAD_GLOBAL             51 (_fallback_to_process_local + NULL)

 586            LOAD_FAST_LOAD_FAST     33 (brokerage_id, normalized_lead)
                LOAD_FAST               16 (source)

 587            LOAD_CONST              31 ('pending_call_store_unavailable')
                BUILD_LIST               1

 585            LOAD_CONST              32 (('extra_warnings',))
                CALL_KW                  4
       L40:     RETURN_VALUE

 589   L41:     LOAD_GLOBAL             32 (logger)
                LOAD_ATTR               63 (info + NULL|self)

 590            LOAD_CONST              35 ('pending_call_created id=')
                LOAD_FAST               20 (pending_call_id)
                FORMAT_SIMPLE
                LOAD_CONST              36 (' brokerage=')

 591            LOAD_FAST                2 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST              37 (' source=')
                LOAD_FAST               16 (source)
                FORMAT_SIMPLE

 590            BUILD_STRING             6

 589            CALL                     1
                POP_TOP

 593            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 594            LOAD_CONST              38 ('accepted')

 595            LOAD_GLOBAL             65 (str + NULL)
                LOAD_FAST               20 (pending_call_id)
                CALL                     1

 596            LOAD_FAST                2 (brokerage_id)

 597            LOAD_FAST               16 (source)

 598            LOAD_CONST              39 (True)

 599            LOAD_GLOBAL             31 (list + NULL)
                LOAD_FAST               11 (_dedupe_warnings)
                CALL                     1

 593            LOAD_CONST              40 (('pending_call_id', 'brokerage_id', 'source', 'call_queued', 'warnings'))
                CALL_KW                  6
       L42:     RETURN_VALUE

  --   L43:     PUSH_EXC_INFO

 470            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L45)
                NOT_TAKEN
                POP_TOP

 471   L44:     POP_EXCEPT
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 551 (to L5)

 470   L45:     RERAISE                  0

  --   L46:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L47:     PUSH_EXC_INFO

 476            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L49)
                NOT_TAKEN
                POP_TOP

 479   L48:     POP_EXCEPT
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 554 (to L8)

 476   L49:     RERAISE                  0

  --   L50:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L51:     PUSH_EXC_INFO

 529            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       80 (to L55)
                NOT_TAKEN
                STORE_FAST              12 (_e)

 530   L52:     LOAD_GLOBAL             32 (logger)
                LOAD_ATTR               35 (warning + NULL|self)

 531            LOAD_CONST              24 ('create_pending_call dedupe layer error type=')

 532            LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST               12 (_e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE

 531            BUILD_STRING             2

 530            CALL                     1
                POP_TOP

 534            LOAD_CONST              25 ('pending_call_dedupe_failed:')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST               12 (_e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1
                STORE_FAST              11 (_dedupe_warnings)
       L53:     POP_EXCEPT
                LOAD_CONST              16 (None)
                STORE_FAST              12 (_e)
                DELETE_FAST             12 (_e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 422 (to L25)

  --   L54:     LOAD_CONST              16 (None)
                STORE_FAST              12 (_e)
                DELETE_FAST             12 (_e)
                RERAISE                  1

 529   L55:     RERAISE                  0

  --   L56:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L57:     PUSH_EXC_INFO

 539            LOAD_GLOBAL             42 (ValueError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       66 (to L64)
                NOT_TAKEN
                STORE_FAST              14 (e)

 540   L58:     LOAD_GLOBAL              3 (_safe_envelope + NULL)

 541            LOAD_CONST               1 ('failed')

 542            LOAD_FAST                2 (brokerage_id)

 543            LOAD_CONST              26 ('row_build_failed:')
                LOAD_FAST               14 (e)
                LOAD_ATTR               44 (args)
                TO_BOOL
                POP_JUMP_IF_FALSE       20 (to L59)
                NOT_TAKEN
                LOAD_FAST               14 (e)
                LOAD_ATTR               44 (args)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                JUMP_FORWARD             1 (to L60)
       L59:     LOAD_CONST              27 ('ValueError')
       L60:     FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 540            LOAD_CONST              28 (('brokerage_id', 'warnings'))
                CALL_KW                  3
       L61:     SWAP                     2
       L62:     POP_EXCEPT
                LOAD_CONST              16 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RETURN_VALUE

  --   L63:     LOAD_CONST              16 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RERAISE                  1

 545   L64:     LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L71)
       L65:     NOT_TAKEN
       L66:     STORE_FAST              14 (e)

 546   L67:     LOAD_GLOBAL             32 (logger)
                LOAD_ATTR               35 (warning + NULL|self)

 547            LOAD_CONST              29 ('create_pending_call row builder unexpected error type=')

 548            LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE

 547            BUILD_STRING             2

 546            CALL                     1
                POP_TOP

 550            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 551            LOAD_CONST               1 ('failed')

 552            LOAD_FAST                2 (brokerage_id)

 553            LOAD_CONST              26 ('row_build_failed:')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 550            LOAD_CONST              28 (('brokerage_id', 'warnings'))
                CALL_KW                  3
       L68:     SWAP                     2
       L69:     POP_EXCEPT
                LOAD_CONST              16 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RETURN_VALUE

  --   L70:     LOAD_CONST              16 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RERAISE                  1

 545   L71:     RERAISE                  0

  --   L72:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L73:     PUSH_EXC_INFO

 601            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L78)
                NOT_TAKEN
                STORE_FAST              14 (e)

 602   L74:     LOAD_GLOBAL             32 (logger)
                LOAD_ATTR               35 (warning + NULL|self)

 603            LOAD_CONST              41 ('pending_call db insert failed (non-critical) brokerage=')

 604            LOAD_FAST                2 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST              37 (' source=')
                LOAD_FAST               16 (source)
                FORMAT_SIMPLE
                LOAD_CONST              42 (' type=')

 605            LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE

 603            BUILD_STRING             6

 602            CALL                     1
                POP_TOP

 607            LOAD_GLOBAL             51 (_fallback_to_process_local + NULL)

 608            LOAD_FAST_LOAD_FAST     33 (brokerage_id, normalized_lead)
                LOAD_FAST               16 (source)

 609            LOAD_CONST              43 ('db_write_failed:')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 607            LOAD_CONST              32 (('extra_warnings',))
                CALL_KW                  4
       L75:     SWAP                     2
       L76:     POP_EXCEPT
                LOAD_CONST              16 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RETURN_VALUE

  --   L77:     LOAD_CONST              16 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RERAISE                  1

 601   L78:     RERAISE                  0

  --   L79:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L47 [0]
  L4 to L5 -> L43 [0]
  L5 to L6 -> L47 [0]
  L9 to L14 -> L51 [0]
  L15 to L17 -> L51 [0]
  L18 to L20 -> L51 [0]
  L21 to L22 -> L51 [0]
  L23 to L25 -> L51 [0]
  L26 to L27 -> L57 [0]
  L30 to L31 -> L73 [0]
  L32 to L34 -> L73 [0]
  L35 to L36 -> L73 [0]
  L37 to L38 -> L73 [0]
  L39 to L40 -> L73 [0]
  L41 to L42 -> L73 [0]
  L43 to L44 -> L46 [1] lasti
  L44 to L45 -> L47 [0]
  L45 to L46 -> L46 [1] lasti
  L46 to L47 -> L47 [0]
  L47 to L48 -> L50 [1] lasti
  L49 to L50 -> L50 [1] lasti
  L51 to L52 -> L56 [1] lasti
  L52 to L53 -> L54 [1] lasti
  L54 to L56 -> L56 [1] lasti
  L57 to L58 -> L72 [1] lasti
  L58 to L61 -> L63 [1] lasti
  L61 to L62 -> L72 [1] lasti
  L63 to L65 -> L72 [1] lasti
  L66 to L67 -> L72 [1] lasti
  L67 to L68 -> L70 [1] lasti
  L68 to L69 -> L72 [1] lasti
  L70 to L72 -> L72 [1] lasti
  L73 to L74 -> L79 [1] lasti
  L74 to L75 -> L77 [1] lasti
  L75 to L76 -> L79 [1] lasti
  L77 to L79 -> L79 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025B30, file "app\services\ingestion\pending_calls.py", line 613>:
613           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

614           LOAD_CONST               2 ('str')

613           LOAD_CONST               3 ('normalized_lead')

615           LOAD_CONST               4 ('NormalizedLead')

613           LOAD_CONST               5 ('source')

616           LOAD_CONST               2 ('str')

613           LOAD_CONST               6 ('extra_warnings')

618           LOAD_CONST               7 ('Optional[List[str]]')

613           LOAD_CONST               8 ('return')

619           LOAD_CONST               9 ('Dict[str, Any]')

613           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _fallback_to_process_local at 0x0000018C17E57B50, file "app\services\ingestion\pending_calls.py", line 613>:
 613            RESUME                   0

 624            LOAD_GLOBAL              1 (list + NULL)
                LOAD_FAST                3 (extra_warnings)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L1:     CALL                     1
                STORE_FAST               4 (warnings)

 625            LOAD_FAST_BORROW         4 (warnings)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST               1 ('pending_calls_store_is_process_local')
                CALL                     1
                POP_TOP

 626            NOP

 627    L2:     LOAD_GLOBAL              5 (prepare_pending_call + NULL)
                LOAD_CONST               2 ('id')
                LOAD_FAST_BORROW         0 (brokerage_id)
                BUILD_MAP                1
                LOAD_FAST_BORROW         1 (normalized_lead)
                CALL                     2
                STORE_FAST               5 (envelope)

 641    L3:     LOAD_GLOBAL             18 (_PENDING_CALLS_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L4:     POP_TOP

 642            LOAD_FAST                5 (envelope)
                LOAD_GLOBAL             20 (_PENDING_CALLS)
                LOAD_FAST                5 (envelope)
                LOAD_ATTR               22 (pending_call_id)
                STORE_SUBSCR

 641    L5:     LOAD_CONST               8 (None)
                LOAD_CONST               8 (None)
                LOAD_CONST               8 (None)
                CALL                     3
                POP_TOP

 643    L6:     LOAD_GLOBAL             17 (_safe_envelope + NULL)

 644            LOAD_CONST               9 ('accepted')

 645            LOAD_FAST                5 (envelope)
                LOAD_ATTR               22 (pending_call_id)

 646            LOAD_FAST                0 (brokerage_id)

 647            LOAD_FAST                2 (source)

 648            LOAD_CONST               6 (False)

 649            LOAD_FAST                4 (warnings)

 643            LOAD_CONST              10 (('pending_call_id', 'brokerage_id', 'source', 'call_queued', 'warnings'))
                CALL_KW                  6
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 628            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      109 (to L12)
                NOT_TAKEN
                STORE_FAST               6 (e)

 629    L8:     LOAD_GLOBAL              8 (logger)
                LOAD_ATTR               11 (warning + NULL|self)

 630            LOAD_CONST               3 ('pending_call fallback envelope build failed type=')

 631            LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE

 630            BUILD_STRING             2

 629            CALL                     1
                POP_TOP

 633            LOAD_FAST                4 (warnings)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST               4 ('fallback_envelope_failed:')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 634            LOAD_GLOBAL             17 (_safe_envelope + NULL)

 635            LOAD_CONST               5 ('failed')

 636            LOAD_FAST                0 (brokerage_id)

 637            LOAD_FAST                2 (source)

 638            LOAD_CONST               6 (False)

 639            LOAD_FAST                4 (warnings)

 634            LOAD_CONST               7 (('brokerage_id', 'source', 'call_queued', 'warnings'))
                CALL_KW                  5
        L9:     SWAP                     2
       L10:     POP_EXCEPT
                LOAD_CONST               8 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --   L11:     LOAD_CONST               8 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 628   L12:     RERAISE                  0

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 641   L14:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L15)
                NOT_TAKEN
                RERAISE                  2
       L15:     POP_TOP
       L16:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_BACKWARD_NO_INTERRUPT 165 (to L6)

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L7 [0]
  L4 to L5 -> L14 [2] lasti
  L7 to L8 -> L13 [1] lasti
  L8 to L9 -> L11 [1] lasti
  L9 to L10 -> L13 [1] lasti
  L11 to L13 -> L13 [1] lasti
  L14 to L16 -> L17 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\services\ingestion\pending_calls.py", line 657>:
657           RESUME                   0
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

Disassembly of <code object _clamp_list_limit at 0x0000018C18010B30, file "app\services\ingestion\pending_calls.py", line 657>:
 657           RESUME                   0

 659           LOAD_FAST_BORROW         0 (value)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

 660           LOAD_SMALL_INT          50
               RETURN_VALUE

 661   L1:     NOP

 662   L2:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (n)

 665   L3:     LOAD_FAST                1 (n)
               LOAD_SMALL_INT           0
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 666           LOAD_SMALL_INT          50
               RETURN_VALUE

 667   L4:     LOAD_FAST                1 (n)
               LOAD_GLOBAL              6 (_PENDING_CALLS_LIST_MAX)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        7 (to L5)
               NOT_TAKEN

 668           LOAD_GLOBAL              6 (_PENDING_CALLS_LIST_MAX)
               RETURN_VALUE

 669   L5:     LOAD_FAST                1 (n)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

 663           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

 664   L7:     POP_EXCEPT
               LOAD_SMALL_INT          50
               RETURN_VALUE

 663   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "app\services\ingestion\pending_calls.py", line 672>:
672           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('limit')

673           LOAD_CONST               2 ('Any')

672           LOAD_CONST               3 ('now')

674           LOAD_CONST               2 ('Any')

672           LOAD_CONST               4 ('worker_id')

675           LOAD_CONST               5 ('Optional[str]')

672           LOAD_CONST               6 ('return')

676           LOAD_CONST               7 ('List[Dict[str, Any]]')

672           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object list_due_pending_calls at 0x0000018C17ED6780, file "app\services\ingestion\pending_calls.py", line 672>:
 672            RESUME                   0

 685            LOAD_GLOBAL              1 (_clamp_list_limit + NULL)
                LOAD_FAST_BORROW         0 (limit)
                CALL                     1
                STORE_FAST               3 (capped)

 686            LOAD_GLOBAL              3 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               4 (db)

 687            LOAD_FAST_BORROW         4 (db)
                POP_JUMP_IF_NOT_NONE     3 (to L1)
                NOT_TAKEN

 688            BUILD_LIST               0
                RETURN_VALUE

 689    L1:     NOP

 690    L2:     LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (now)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_FAST                1 (now)
                JUMP_FORWARD             9 (to L4)
        L3:     LOAD_GLOBAL              9 (_now_iso + NULL)
                CALL                     0
        L4:     STORE_FAST               5 (when)

 692            LOAD_FAST_BORROW         4 (db)
                LOAD_ATTR               11 (table + NULL|self)
                LOAD_GLOBAL             12 (_TABLE_PENDING_CALLS)
                CALL                     1

 693            LOAD_ATTR               15 (select + NULL|self)

 694            LOAD_CONST               2 ('pending_call_id, brokerage_id, source, lead_id, lead_phone, lead_email, lead_name, intent, budget, timeline, property_address, metadata, status, attempts, max_attempts, next_attempt_at, created_at')

 693            CALL                     1

 700            LOAD_ATTR               17 (eq + NULL|self)
                LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('PENDING')
                CALL                     2

 701            LOAD_ATTR               19 (lte + NULL|self)
                LOAD_CONST               5 ('next_attempt_at')
                LOAD_FAST_BORROW         5 (when)
                CALL                     2

 702            LOAD_ATTR               21 (order + NULL|self)
                LOAD_CONST               5 ('next_attempt_at')
                LOAD_CONST               6 (False)
                LOAD_CONST               7 (('desc',))
                CALL_KW                  2

 703            LOAD_ATTR               23 (limit + NULL|self)
                LOAD_FAST_BORROW         3 (capped)
                CALL                     1

 691            STORE_FAST               6 (query)

 705            LOAD_FAST_BORROW         6 (query)
                LOAD_ATTR               25 (execute + NULL|self)
                CALL                     0
                STORE_FAST               7 (result)

 706            LOAD_GLOBAL             27 (list + NULL)
                LOAD_GLOBAL             29 (getattr + NULL)
                LOAD_FAST_BORROW         7 (result)
                LOAD_CONST               8 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                BUILD_LIST               0
        L7:     CALL                     1
                STORE_FAST               8 (rows)

 707            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         8 (rows)
                LOAD_GLOBAL             26 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN

 708            BUILD_LIST               0
        L8:     RETURN_VALUE

 709    L9:     LOAD_FAST_BORROW         8 (rows)
       L10:     RETURN_VALUE

  --   L11:     PUSH_EXC_INFO

 710            LOAD_GLOBAL             30 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       56 (to L16)
                NOT_TAKEN
                STORE_FAST               9 (e)

 711   L12:     LOAD_GLOBAL             32 (logger)
                LOAD_ATTR               35 (warning + NULL|self)

 712            LOAD_CONST               9 ('list_due_pending_calls db error (non-critical) type=')

 713            LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE

 712            BUILD_STRING             2

 711            CALL                     1
                POP_TOP

 715            BUILD_LIST               0
       L13:     SWAP                     2
       L14:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RETURN_VALUE

  --   L15:     LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 710   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L5 -> L11 [0]
  L6 to L8 -> L11 [0]
  L9 to L10 -> L11 [0]
  L11 to L12 -> L17 [1] lasti
  L12 to L13 -> L15 [1] lasti
  L13 to L14 -> L17 [1] lasti
  L15 to L17 -> L17 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app\services\ingestion\pending_calls.py", line 718>:
718           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('pending_call_id')

719           LOAD_CONST               2 ('str')

718           LOAD_CONST               3 ('brokerage_id')

720           LOAD_CONST               2 ('str')

718           LOAD_CONST               4 ('patch')

721           LOAD_CONST               5 ('Dict[str, Any]')

718           LOAD_CONST               6 ('op_label')

723           LOAD_CONST               2 ('str')

718           LOAD_CONST               7 ('return')

724           LOAD_CONST               5 ('Dict[str, Any]')

718           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _update_row_with_tenant_pin at 0x0000018C17ED0840, file "app\services\ingestion\pending_calls.py", line 718>:
 718            RESUME                   0

 729            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L2)
                NOT_TAKEN

 731    L1:     LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 732            LOAD_CONST               3 ('pending_call_id')
                LOAD_FAST_BORROW         0 (pending_call_id)

 733            LOAD_CONST               4 ('brokerage_id')
                LOAD_CONST               5 (None)

 734            LOAD_CONST               6 ('warnings')
                LOAD_CONST               7 ('missing_brokerage_id')
                BUILD_LIST               1

 730            BUILD_MAP                4
                RETURN_VALUE

 736    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (pending_call_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (pending_call_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L4)
                NOT_TAKEN

 738    L3:     LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 739            LOAD_CONST               3 ('pending_call_id')
                LOAD_CONST               5 (None)

 740            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         1 (brokerage_id)

 741            LOAD_CONST               6 ('warnings')
                LOAD_CONST               8 ('missing_pending_call_id')
                BUILD_LIST               1

 737            BUILD_MAP                4
                RETURN_VALUE

 743    L4:     LOAD_GLOBAL              7 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               4 (db)

 744            LOAD_FAST_BORROW         4 (db)
                POP_JUMP_IF_NOT_NONE    12 (to L5)
                NOT_TAKEN

 746            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 747            LOAD_CONST               3 ('pending_call_id')
                LOAD_FAST_BORROW         0 (pending_call_id)

 748            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         1 (brokerage_id)

 749            LOAD_CONST               6 ('warnings')
                LOAD_CONST               9 ('pending_call_store_unavailable')
                BUILD_LIST               1

 745            BUILD_MAP                4
                RETURN_VALUE

 751    L5:     NOP

 753    L6:     LOAD_FAST_BORROW         4 (db)
                LOAD_ATTR                9 (table + NULL|self)
                LOAD_GLOBAL             10 (_TABLE_PENDING_CALLS)
                CALL                     1

 754            LOAD_ATTR               13 (update + NULL|self)
                LOAD_FAST_BORROW         2 (patch)
                CALL                     1

 755            LOAD_ATTR               15 (eq + NULL|self)
                LOAD_CONST               3 ('pending_call_id')
                LOAD_FAST_BORROW         0 (pending_call_id)
                CALL                     2

 756            LOAD_ATTR               15 (eq + NULL|self)
                LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         1 (brokerage_id)
                CALL                     2

 757            LOAD_ATTR               17 (execute + NULL|self)
                CALL                     0

 752            STORE_FAST               5 (result)

 759            LOAD_GLOBAL             19 (list + NULL)
                LOAD_GLOBAL             21 (getattr + NULL)
                LOAD_FAST_BORROW         5 (result)
                LOAD_CONST              10 ('data')
                LOAD_CONST               5 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
        L7:     NOT_TAKEN
        L8:     POP_TOP
                BUILD_LIST               0
        L9:     CALL                     1
                STORE_FAST               6 (rows)

 760            LOAD_FAST_BORROW         6 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L13)
       L10:     NOT_TAKEN

 762   L11:     LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 763            LOAD_CONST               3 ('pending_call_id')
                LOAD_FAST_BORROW         0 (pending_call_id)

 764            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         1 (brokerage_id)

 765            LOAD_CONST               6 ('warnings')
                LOAD_CONST              11 ('pending_call_not_found_or_cross_tenant')
                BUILD_LIST               1

 761            BUILD_MAP                4
       L12:     RETURN_VALUE

 768   L13:     LOAD_CONST               1 ('status')
                LOAD_CONST              12 ('ok')

 769            LOAD_CONST               3 ('pending_call_id')
                LOAD_FAST_BORROW         0 (pending_call_id)

 770            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         1 (brokerage_id)

 771            LOAD_CONST               6 ('warnings')
                BUILD_LIST               0

 767            BUILD_MAP                4
       L14:     RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 773            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       92 (to L20)
                NOT_TAKEN
                STORE_FAST               7 (e)

 774   L16:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 775            LOAD_FAST                3 (op_label)
                FORMAT_SIMPLE
                LOAD_CONST              13 (' db error (non-critical) id=')

 776            LOAD_FAST                0 (pending_call_id)
                FORMAT_SIMPLE
                LOAD_CONST              14 (' type=')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 775            BUILD_STRING             5

 774            CALL                     1
                POP_TOP

 779            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 780            LOAD_CONST               3 ('pending_call_id')
                LOAD_FAST                0 (pending_call_id)

 781            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                1 (brokerage_id)

 782            LOAD_CONST               6 ('warnings')
                LOAD_CONST              15 ('db_write_failed:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 778            BUILD_MAP                4
       L17:     SWAP                     2
       L18:     POP_EXCEPT
                LOAD_CONST               5 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L19:     LOAD_CONST               5 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 773   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L6 to L7 -> L15 [0]
  L8 to L10 -> L15 [0]
  L11 to L12 -> L15 [0]
  L13 to L14 -> L15 [0]
  L15 to L16 -> L21 [1] lasti
  L16 to L17 -> L19 [1] lasti
  L17 to L18 -> L21 [1] lasti
  L19 to L21 -> L21 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024F30, file "app\services\ingestion\pending_calls.py", line 786>:
786           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('pending_call_id')

787           LOAD_CONST               2 ('str')

786           LOAD_CONST               3 ('brokerage_id')

788           LOAD_CONST               2 ('str')

786           LOAD_CONST               4 ('worker_id')

789           LOAD_CONST               5 ('Optional[str]')

786           LOAD_CONST               6 ('return')

790           LOAD_CONST               7 ('Dict[str, Any]')

786           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object mark_pending_call_dialing at 0x0000018C18038A30, file "app\services\ingestion\pending_calls.py", line 786>:
786           RESUME                   0

792           LOAD_CONST               0 ('status')
              LOAD_CONST               1 ('DIALING')

793           LOAD_CONST               2 ('locked_at')
              LOAD_GLOBAL              1 (_now_iso + NULL)
              CALL                     0

794           LOAD_CONST               3 ('locked_by')
              LOAD_GLOBAL              3 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (worker_id)
              LOAD_GLOBAL              4 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_FAST                2 (worker_id)
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               4 (None)

791   L2:     BUILD_MAP                3
              STORE_FAST               3 (patch)

796           LOAD_GLOBAL              7 (_update_row_with_tenant_pin + NULL)

797           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (pending_call_id, brokerage_id)
              LOAD_FAST_BORROW         3 (patch)

798           LOAD_CONST               5 ('mark_pending_call_dialing')

796           LOAD_CONST               6 (('op_label',))
              CALL_KW                  4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "app\services\ingestion\pending_calls.py", line 802>:
802           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('pending_call_id')

803           LOAD_CONST               2 ('str')

802           LOAD_CONST               3 ('brokerage_id')

804           LOAD_CONST               2 ('str')

802           LOAD_CONST               4 ('call_sid')

805           LOAD_CONST               5 ('Optional[str]')

802           LOAD_CONST               6 ('return')

806           LOAD_CONST               7 ('Dict[str, Any]')

802           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object mark_pending_call_dialed at 0x0000018C17FF0DB0, file "app\services\ingestion\pending_calls.py", line 802>:
802           RESUME                   0

811           LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('DIALED')
              BUILD_MAP                1
              STORE_FAST               3 (patch)

812           LOAD_GLOBAL              1 (_update_row_with_tenant_pin + NULL)

813           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (pending_call_id, brokerage_id)
              LOAD_FAST_BORROW         3 (patch)

814           LOAD_CONST               3 ('mark_pending_call_dialed')

812           LOAD_CONST               4 (('op_label',))
              CALL_KW                  4
              STORE_FAST               4 (env)

816           LOAD_GLOBAL              3 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (call_sid)
              LOAD_GLOBAL              4 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       42 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (call_sid)
              LOAD_ATTR                7 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       20 (to L1)
              NOT_TAKEN

817           LOAD_FAST_BORROW         2 (call_sid)
              LOAD_ATTR                7 (strip + NULL|self)
              CALL                     0
              LOAD_FAST_BORROW         4 (env)
              LOAD_CONST               5 ('call_sid')
              STORE_SUBSCR

818   L1:     LOAD_FAST_BORROW         4 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025830, file "app\services\ingestion\pending_calls.py", line 821>:
821           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('pending_call_id')

822           LOAD_CONST               2 ('str')

821           LOAD_CONST               3 ('brokerage_id')

823           LOAD_CONST               2 ('str')

821           LOAD_CONST               4 ('error_code')

824           LOAD_CONST               2 ('str')

821           LOAD_CONST               5 ('retry')

825           LOAD_CONST               6 ('bool')

821           LOAD_CONST               7 ('return')

826           LOAD_CONST               8 ('Dict[str, Any]')

821           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object mark_pending_call_failed at 0x0000018C17FF0C30, file "app\services\ingestion\pending_calls.py", line 821>:
821           RESUME                   0

833           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (error_code)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (error_code)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

834   L1:     LOAD_CONST               1 ('unknown_error')
              STORE_FAST               2 (error_code)

836   L2:     LOAD_CONST               2 ('status')
              LOAD_FAST_BORROW         3 (retry)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              LOAD_CONST               3 ('FAILED')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               4 ('PENDING')

837   L4:     LOAD_CONST               5 ('last_error_code')
              LOAD_FAST_BORROW         2 (error_code)

838           LOAD_CONST               6 ('last_error_at')
              LOAD_GLOBAL              7 (_now_iso + NULL)
              CALL                     0

835           BUILD_MAP                3
              STORE_FAST               4 (patch)

840           LOAD_GLOBAL              9 (_update_row_with_tenant_pin + NULL)

841           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (pending_call_id, brokerage_id)
              LOAD_FAST_BORROW         4 (patch)

842           LOAD_CONST               7 ('mark_pending_call_failed')

840           LOAD_CONST               8 (('op_label',))
              CALL_KW                  4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "app\services\ingestion\pending_calls.py", line 846>:
846           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('pending_call_id')

847           LOAD_CONST               2 ('str')

846           LOAD_CONST               3 ('brokerage_id')

848           LOAD_CONST               2 ('str')

846           LOAD_CONST               4 ('reason')

849           LOAD_CONST               5 ('Optional[str]')

846           LOAD_CONST               6 ('return')

850           LOAD_CONST               7 ('Dict[str, Any]')

846           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object cancel_pending_call at 0x0000018C18060A50, file "app\services\ingestion\pending_calls.py", line 846>:
846           RESUME                   0

854           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (reason)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       56 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (reason)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       34 (to L1)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         2 (reason)
              CALL                     1
              LOAD_SMALL_INT          64
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_FALSE       18 (to L1)
              NOT_TAKEN

855           LOAD_FAST_BORROW         2 (reason)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               3 (code)
              JUMP_FORWARD             2 (to L2)

857   L1:     LOAD_CONST               1 ('operator_cancelled')
              STORE_FAST               3 (code)

859   L2:     LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('CANCELLED')

860           LOAD_CONST               4 ('last_error_code')
              LOAD_FAST_BORROW         3 (code)

861           LOAD_CONST               5 ('last_error_at')
              LOAD_GLOBAL              9 (_now_iso + NULL)
              CALL                     0

858           BUILD_MAP                3
              STORE_FAST               4 (patch)

863           LOAD_GLOBAL             11 (_update_row_with_tenant_pin + NULL)

864           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (pending_call_id, brokerage_id)
              LOAD_FAST_BORROW         4 (patch)

865           LOAD_CONST               6 ('cancel_pending_call')

863           LOAD_CONST               7 (('op_label',))
              CALL_KW                  4
              RETURN_VALUE
```
