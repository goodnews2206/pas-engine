# memory/review

- **pyc:** `app\services\memory\__pycache__\review.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/review.py`
- **co_filename (from bytecode):** `app\services\memory\review.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144C — Memory review + promotion workflow.

Controlled, tenant-scoped, audited status transitions on
``pas_memory_records`` rows. Every transition routes through a single
review-event row in ``pas_memory_review_events`` (created by
``scripts/migrate_v11_memory_review_audit.sql``).

Hard contract — every public helper in this module:
  1. Requires ``brokerage_id`` (tenant isolation, mandatory).
  2. Fetches the existing memory row tenant-scoped BEFORE attempting
     a status transition. A cross-tenant ``memory_id`` simply will not
     be found and the call is rejected with a structured failure dict.
  3. Validates the transition via ``audit.validate_review_transition``
     BEFORE writing anything. Invalid transitions never reach the DB.
  4. Writes the audit row AFTER the status update succeeds. If the
     update succeeds but the audit write fails, the response carries
     a ``warning`` status — we do NOT fake full success.
  5. Never raises on Supabase failure: returns a structured failure
     dict instead.
  6. Refuses to approve a DANGEROUS-kind memory through any path
     other than the SECURITY/ADMIN QUARANTINED → APPROVED edge.

Return-shape contract (see helpers below):
  Success            : {"status": "ok",        "memory_id": ..., ...}
  Partial / warning  : {"status": "warning",   "warnings": [...], ...}
  Refused / failure  : {"status": "failed",    "errors":   [...], ...}

Public surface (deliberately tiny):
  - approve_memory(memory_id, brokerage_id, actor_type, actor_id=None,
                   reason=None)
  - reject_memory(memory_id, brokerage_id, actor_type, actor_id=None,
                  reason=None)
  - quarantine_memory_by_id(memory_id, brokerage_id, actor_type,
                            actor_id=None, reason=None)
  - expire_memory_by_id(memory_id, brokerage_id, actor_type,
                        actor_id=None, reason=None)
  - list_memory_review_events(memory_id, brokerage_id)

PAS144C explicitly does NOT build:
  * retrieval / similarity search
  * embeddings / vector helpers
  * dashboard or PAS Brain UI changes
  * autonomous learning loop
  * any path that auto-approves a CANDIDATE memory
```

## Imports

``, `Any`, `Dict`, `List`, `MemoryKind`, `MemoryStatus`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `audit`, `contracts`, `datetime`, `get_supabase`, `logging`, `queries`, `store`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_execute_review_insert`, `_execute_status_update`, `_failure`, `_get_db`, `_run_transition`, `_safe_log_decision`, `_validate_actor_type`, `approve_memory`, `expire_memory_by_id`, `list_memory_review_events`, `quarantine_memory_by_id`, `reject_memory`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS144C — Memory review + promotion workflow.\n\nControlled, tenant-scoped, audited status transitions on\n``pas_memory_records`` rows. Every transition routes through a single\nreview-event row in ``pas_memory_review_events`` (created by\n``scripts/migrate_v11_memory_review_audit.sql``).\n\nHard contract — every public helper in this module:\n  1. Requires ``brokerage_id`` (tenant isolation, mandatory).\n  2. Fetches the existing memory row tenant-scoped BEFORE attempting\n     a status transition. A cross-tenant ``memory_id`` simply will not\n     be found and the call is rejected with a structured failure dict.\n  3. Validates the transition via ``audit.validate_review_transition``\n     BEFORE writing anything. Invalid transitions never reach the DB.\n  4. Writes the audit row AFTER the status update succeeds. If the\n     update succeeds but the audit write fails, the response carries\n     a ``warning`` status — we do NOT fake full success.\n  5. Never raises on Supabase failure: returns a structured failure\n     dict instead.\n  6. Refuses to approve a DANGEROUS-kind memory through any path\n     other than the SECURITY/ADMIN QUARANTINED → APPROVED edge.\n\nReturn-shape contract (see helpers below):\n  Success            : {"status": "ok",        "memory_id": ..., ...}\n  Partial / warning  : {"status": "warning",   "warnings": [...], ...}\n  Refused / failure  : {"status": "failed",    "errors":   [...], ...}\n\nPublic surface (deliberately tiny):\n  - approve_memory(memory_id, brokerage_id, actor_type, actor_id=None,\n                   reason=None)\n  - reject_memory(memory_id, brokerage_id, actor_type, actor_id=None,\n                  reason=None)\n  - quarantine_memory_by_id(memory_id, brokerage_id, actor_type,\n                            actor_id=None, reason=None)\n  - expire_memory_by_id(memory_id, brokerage_id, actor_type,\n                        actor_id=None, reason=None)\n  - list_memory_review_events(memory_id, brokerage_id)\n\nPAS144C explicitly does NOT build:\n  * retrieval / similarity search\n  * embeddings / vector helpers\n  * dashboard or PAS Brain UI changes\n  * autonomous learning loop\n  * any path that auto-approves a CANDIDATE memory\n'
- 'pas.memory.review'
- 'pas_memory_records'
- 'pas_memory_review_events'
- 'memory_id'
- 'brokerage_id'
- 'from_status'
- 'to_status'
- 'extra'
- 'limit'
- 'Lazy Supabase resolver. Mirrors store.py / queries.py so unit\ntests can patch ``app.db.supabase_client.get_supabase``.'
- 'errors'
- 'List[str]'
- 'Optional[str]'
- 'return'
- 'Dict[str, Any]'
- 'Structured failure dict — uniform shape across every helper.'
- 'status'
- 'failed'
- 'actor_type'
- 'Any'
- 'Return the actor_type string if valid, else None.'
- 'str'
- 'decision'
- 'Optional[Dict[str, Any]]'
- 'None'
- 'Structured, non-sensitive log line. Never echoes reason/metadata\nvalues; only structural facts (memory_id, brokerage_id, decision).'
- ' | '
- 'new_status'
- 'MemoryStatus'
- "Patch a single ``pas_memory_records`` row's status, tenant-\nscoped via brokerage_id. Fail-safe: returns None on Supabase\nerror, never raises.\n\nDeliberately does NOT stamp a per-write audit blob into\nmetadata — the audit trail is the separate ``pas_memory_review_events``\ntable. Mixing both surfaces would create two competing sources\nof truth.\n"
- 'data'
- ' status update failed (non-critical) | memory_id='
- ' | error_type='
- 'row'
- 'Insert one row into ``pas_memory_review_events``. Fail-safe.'
- ' audit insert failed (non-critical) | memory_id='
- 'target_status'
- 'actor_id'
- 'reason'
- 'enforce_transition_table'
- 'bool'
- 'extra_dangerous_check'
- 'Shared body of every transition helper.\n\nSteps (the order is load-bearing — see module docstring):\n  1. structural input checks (brokerage_id, memory_id, actor_type);\n  2. tenant-scoped fetch of the existing record;\n  3. transition validation against the audit table;\n  4. dangerous-kind guard rail when ``extra_dangerous_check`` is\n     True (only the SECURITY/ADMIN QUARANTINED → APPROVED edge may\n     touch a DANGEROUS-kind record);\n  5. status update;\n  6. audit-row insert;\n  7. structured return dict.\n'
- 'refused'
- 'missing_brokerage_id'
- 'brokerage_id is required (tenant isolation)'
- 'missing_memory_id'
- 'memory_id is required'
- 'invalid_actor_type'
- 'actor_type must be one of '
- '; got '
- 'memory_not_found'
- 'memory not found for brokerage'
- 'kind'
- 'invalid_transition'
- 'dangerous_normal_approval_blocked'
- 'DANGEROUS-kind memory cannot be approved through normal approval; requires SECURITY or ADMIN actor'
- 'status update failed (storage unavailable)'
- 'warning'
- 'audit_event_build_failed'
- 'error_type'
- 'warnings'
- 'audit_event_build_failed:'
- 'audit_write_failed'
- 'review_id'
- 'Promote a memory to APPROVED.\n\nLegal entry transitions (per ``audit.VALID_TRANSITIONS``):\n  * CANDIDATE   → APPROVED  (any allowed actor_type)\n  * QUARANTINED → APPROVED  (SECURITY or ADMIN only)\n\nAdditional guard: DANGEROUS-kind records can only reach APPROVED\nvia the SECURITY/ADMIN edge — never through a CANDIDATE actor\n(those records are already QUARANTINED by governance, but the\nextra check protects against future regressions).\n'
- 'approve_memory'
- 'Reject a memory.\n\nLegal entry transitions:\n  * CANDIDATE   → REJECTED\n  * QUARANTINED → REJECTED\n'
- 'reject_memory'
- 'Move an APPROVED memory to EXPIRED.\n\nLegal entry transition:\n  * APPROVED → EXPIRED\n'
- 'expire_memory_by_id'
- 'Move an existing memory to QUARANTINED.\n\nQuarantine is not in ``audit.VALID_TRANSITIONS`` because it is a\ndefensive action — any allowed actor may move a record into\nquarantine regardless of its current state (except EXPIRED /\nREJECTED — those are terminal). We therefore skip the transition\ntable here but still record the action in the audit trail.\n\nTenant-scoped: cross-tenant memory_ids cannot be quarantined.\n'
- 'quarantine_memory_by_id'
- 'cannot quarantine memory in terminal status '
- 'int'
- 'List[Dict[str, Any]]'
- 'Return audit events for a single memory, tenant-scoped.\n\nReturns ``[]`` on missing brokerage_id, missing memory_id, or any\nSupabase failure. Never raises.\n'
- 'list_memory_review_events dropped | reason=missing_brokerage_id'
- 'list_memory_review_events dropped | reason=invalid_memory_id'
- 'created_at'
- 'list_memory_review_events failed (non-critical) | memory_id='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS144C — Memory review + promotion workflow.\n\nControlled, tenant-scoped, audited status transitions on\n``pas_memory_records`` rows. Every transition routes through a single\nreview-event row in ``pas_memory_review_events`` (created by\n``scripts/migrate_v11_memory_review_audit.sql``).\n\nHard contract — every public helper in this module:\n  1. Requires ``brokerage_id`` (tenant isolation, mandatory).\n  2. Fetches the existing memory row tenant-scoped BEFORE attempting\n     a status transition. A cross-tenant ``memory_id`` simply will not\n     be found and the call is rejected with a structured failure dict.\n  3. Validates the transition via ``audit.validate_review_transition``\n     BEFORE writing anything. Invalid transitions never reach the DB.\n  4. Writes the audit row AFTER the status update succeeds. If the\n     update succeeds but the audit write fails, the response carries\n     a ``warning`` status — we do NOT fake full success.\n  5. Never raises on Supabase failure: returns a structured failure\n     dict instead.\n  6. Refuses to approve a DANGEROUS-kind memory through any path\n     other than the SECURITY/ADMIN QUARANTINED → APPROVED edge.\n\nReturn-shape contract (see helpers below):\n  Success            : {"status": "ok",        "memory_id": ..., ...}\n  Partial / warning  : {"status": "warning",   "warnings": [...], ...}\n  Refused / failure  : {"status": "failed",    "errors":   [...], ...}\n\nPublic surface (deliberately tiny):\n  - approve_memory(memory_id, brokerage_id, actor_type, actor_id=None,\n                   reason=None)\n  - reject_memory(memory_id, brokerage_id, actor_type, actor_id=None,\n                  reason=None)\n  - quarantine_memory_by_id(memory_id, brokerage_id, actor_type,\n                            actor_id=None, reason=None)\n  - expire_memory_by_id(memory_id, brokerage_id, actor_type,\n                        actor_id=None, reason=None)\n  - list_memory_review_events(memory_id, brokerage_id)\n\nPAS144C explicitly does NOT build:\n  * retrieval / similarity search\n  * embeddings / vector helpers\n  * dashboard or PAS Brain UI changes\n  * autonomous learning loop\n  * any path that auto-approves a CANDIDATE memory\n')
              STORE_NAME               0 (__doc__)

 48           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 50           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 51           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timezone'))
              IMPORT_NAME              4 (datetime)
              IMPORT_FROM              4 (datetime)
              STORE_NAME               4 (datetime)
              IMPORT_FROM              5 (timezone)
              STORE_NAME               5 (timezone)
              POP_TOP

 52           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              6 (typing)
              IMPORT_FROM              7 (Any)
              STORE_NAME               7 (Any)
              IMPORT_FROM              8 (Dict)
              STORE_NAME               8 (Dict)
              IMPORT_FROM              9 (List)
              STORE_NAME               9 (List)
              IMPORT_FROM             10 (Optional)
              STORE_NAME              10 (Optional)
              POP_TOP

 54           LOAD_SMALL_INT           1
              LOAD_CONST               5 (('MemoryKind', 'MemoryStatus'))
              IMPORT_NAME             11 (contracts)
              IMPORT_FROM             12 (MemoryKind)
              STORE_NAME              12 (MemoryKind)
              IMPORT_FROM             13 (MemoryStatus)
              STORE_NAME              13 (MemoryStatus)
              POP_TOP

 55           LOAD_SMALL_INT           1
              LOAD_CONST               6 (('audit',))
              IMPORT_NAME             14
              IMPORT_FROM             15 (audit)
              STORE_NAME              16 (audit_mod)
              POP_TOP

 56           LOAD_SMALL_INT           1
              LOAD_CONST               7 (('queries',))
              IMPORT_NAME             14
              IMPORT_FROM             17 (queries)
              STORE_NAME              18 (queries_mod)
              POP_TOP

 57           LOAD_SMALL_INT           1
              LOAD_CONST               8 (('store',))
              IMPORT_NAME             14
              IMPORT_FROM             19 (store)
              STORE_NAME              20 (store_mod)
              POP_TOP

 59           LOAD_NAME                3 (logging)
              LOAD_ATTR               42 (getLogger)
              PUSH_NULL
              LOAD_CONST               9 ('pas.memory.review')
              CALL                     1
              STORE_NAME              22 (logger)

 62           LOAD_CONST              10 ('pas_memory_records')
              STORE_NAME              23 (_TABLE_RECORDS)

 63           LOAD_CONST              11 ('pas_memory_review_events')
              STORE_NAME              24 (_TABLE_REVIEW)

 70           LOAD_CONST              12 (<code object _get_db at 0x0000018C17FA34B0, file "app\services\memory\review.py", line 70>)
              MAKE_FUNCTION
              STORE_NAME              25 (_get_db)

 77           LOAD_CONST              13 ('memory_id')

 80           LOAD_CONST               2 (None)

 77           LOAD_CONST              14 ('brokerage_id')

 81           LOAD_CONST               2 (None)

 77           LOAD_CONST              15 ('from_status')

 82           LOAD_CONST               2 (None)

 77           LOAD_CONST              16 ('to_status')

 83           LOAD_CONST               2 (None)

 77           BUILD_MAP                4
              LOAD_CONST              17 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\memory\review.py", line 77>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _failure at 0x0000018C18038B70, file "app\services\memory\review.py", line 77>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              26 (_failure)

101           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\review.py", line 101>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _validate_actor_type at 0x0000018C17C49B80, file "app\services\memory\review.py", line 101>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_validate_actor_type)

108           LOAD_CONST              21 ('extra')

114           LOAD_CONST               2 (None)

108           BUILD_MAP                1
              LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18025230, file "app\services\memory\review.py", line 108>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object _safe_log_decision at 0x0000018C179C3A50, file "app\services\memory\review.py", line 108>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              28 (_safe_log_decision)

132           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C18024B30, file "app\services\memory\review.py", line 132>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object _execute_status_update at 0x0000018C17D8D460, file "app\services\memory\review.py", line 132>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_execute_status_update)

167           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C18024E30, file "app\services\memory\review.py", line 167>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object _execute_review_insert at 0x0000018C17FEDA30, file "app\services\memory\review.py", line 167>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_execute_review_insert)

190           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C180C4470, file "app\services\memory\review.py", line 190>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object _run_transition at 0x0000018C17ED7F00, file "app\services\memory\review.py", line 190>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_run_transition)

396           LOAD_CONST              41 ((None, None))
              LOAD_CONST              30 (<code object __annotate__ at 0x0000018C18025D30, file "app\services\memory\review.py", line 396>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object approve_memory at 0x0000018C18053E10, file "app\services\memory\review.py", line 396>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              32 (approve_memory)

424           LOAD_CONST              41 ((None, None))
              LOAD_CONST              32 (<code object __annotate__ at 0x0000018C18025530, file "app\services\memory\review.py", line 424>)
              MAKE_FUNCTION
              LOAD_CONST              33 (<code object reject_memory at 0x0000018C18053090, file "app\services\memory\review.py", line 424>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              33 (reject_memory)

447           LOAD_CONST              41 ((None, None))
              LOAD_CONST              34 (<code object __annotate__ at 0x0000018C18025130, file "app\services\memory\review.py", line 447>)
              MAKE_FUNCTION
              LOAD_CONST              35 (<code object expire_memory_by_id at 0x0000018C18052F70, file "app\services\memory\review.py", line 447>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              34 (expire_memory_by_id)

469           LOAD_CONST              41 ((None, None))
              LOAD_CONST              36 (<code object __annotate__ at 0x0000018C18025A30, file "app\services\memory\review.py", line 469>)
              MAKE_FUNCTION
              LOAD_CONST              37 (<code object quarantine_memory_by_id at 0x0000018C17D94CE0, file "app\services\memory\review.py", line 469>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              35 (quarantine_memory_by_id)

598           LOAD_CONST              38 ('limit')

602           LOAD_SMALL_INT          50

598           BUILD_MAP                1
              LOAD_CONST              39 (<code object __annotate__ at 0x0000018C18025B30, file "app\services\memory\review.py", line 598>)
              MAKE_FUNCTION
              LOAD_CONST              40 (<code object list_memory_review_events at 0x0000018C17D7D6B0, file "app\services\memory\review.py", line 598>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              36 (list_memory_review_events)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object _get_db at 0x0000018C17FA34B0, file "app\services\memory\review.py", line 70>:
 70           RESUME                   0

 73           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('get_supabase',))
              IMPORT_NAME              0 (app.db.supabase_client)
              IMPORT_FROM              1 (get_supabase)
              STORE_FAST               0 (get_supabase)
              POP_TOP

 74           LOAD_FAST_BORROW         0 (get_supabase)
              PUSH_NULL
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\memory\review.py", line 77>:
 77           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('errors')

 79           LOAD_CONST               2 ('List[str]')

 77           LOAD_CONST               3 ('memory_id')

 80           LOAD_CONST               4 ('Optional[str]')

 77           LOAD_CONST               5 ('brokerage_id')

 81           LOAD_CONST               4 ('Optional[str]')

 77           LOAD_CONST               6 ('from_status')

 82           LOAD_CONST               4 ('Optional[str]')

 77           LOAD_CONST               7 ('to_status')

 83           LOAD_CONST               4 ('Optional[str]')

 77           LOAD_CONST               8 ('return')

 84           LOAD_CONST               9 ('Dict[str, Any]')

 77           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _failure at 0x0000018C18038B70, file "app\services\memory\review.py", line 77>:
 77           RESUME                   0

 87           LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('failed')

 88           LOAD_CONST               3 ('errors')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST_BORROW         0 (errors)
              CALL                     1

 86           BUILD_MAP                2
              STORE_FAST               5 (out)

 90           LOAD_FAST_BORROW         1 (memory_id)
              POP_JUMP_IF_NONE         5 (to L1)
              NOT_TAKEN

 91           LOAD_FAST_BORROW_LOAD_FAST_BORROW 21 (memory_id, out)
              LOAD_CONST               4 ('memory_id')
              STORE_SUBSCR

 92   L1:     LOAD_FAST_BORROW         2 (brokerage_id)
              POP_JUMP_IF_NONE         5 (to L2)
              NOT_TAKEN

 93           LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (brokerage_id, out)
              LOAD_CONST               5 ('brokerage_id')
              STORE_SUBSCR

 94   L2:     LOAD_FAST_BORROW         3 (from_status)
              POP_JUMP_IF_NONE         5 (to L3)
              NOT_TAKEN

 95           LOAD_FAST_BORROW_LOAD_FAST_BORROW 53 (from_status, out)
              LOAD_CONST               6 ('from_status')
              STORE_SUBSCR

 96   L3:     LOAD_FAST_BORROW         4 (to_status)
              POP_JUMP_IF_NONE         5 (to L4)
              NOT_TAKEN

 97           LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (to_status, out)
              LOAD_CONST               7 ('to_status')
              STORE_SUBSCR

 98   L4:     LOAD_FAST_BORROW         5 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\review.py", line 101>:
101           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('actor_type')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _validate_actor_type at 0x0000018C17C49B80, file "app\services\memory\review.py", line 101>:
101           RESUME                   0

103           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (actor_type)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       24 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (actor_type)
              LOAD_GLOBAL              4 (audit_mod)
              LOAD_ATTR                6 (ALLOWED_ACTOR_TYPES)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

104           LOAD_FAST_BORROW         0 (actor_type)
              RETURN_VALUE

105   L1:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025230, file "app\services\memory\review.py", line 108>:
108           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('op')

110           LOAD_CONST               2 ('str')

108           LOAD_CONST               3 ('memory_id')

111           LOAD_CONST               4 ('Optional[str]')

108           LOAD_CONST               5 ('brokerage_id')

112           LOAD_CONST               4 ('Optional[str]')

108           LOAD_CONST               6 ('decision')

113           LOAD_CONST               2 ('str')

108           LOAD_CONST               7 ('extra')

114           LOAD_CONST               8 ('Optional[Dict[str, Any]]')

108           LOAD_CONST               9 ('return')

115           LOAD_CONST              10 ('None')

108           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _safe_log_decision at 0x0000018C179C3A50, file "app\services\memory\review.py", line 108>:
108           RESUME                   0

119           LOAD_CONST               1 ('op')
              LOAD_FAST                0 (op)

120           LOAD_CONST               2 ('memory_id')
              LOAD_FAST                1 (memory_id)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               3 ('')

121   L1:     LOAD_CONST               4 ('brokerage_id')
              LOAD_FAST                2 (brokerage_id)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               3 ('')

122   L2:     LOAD_CONST               5 ('decision')
              LOAD_FAST_BORROW         3 (decision)

118           BUILD_MAP                4
              STORE_FAST               5 (fields)

124           LOAD_FAST_BORROW         4 (extra)
              TO_BOOL
              POP_JUMP_IF_FALSE       38 (to L6)
              NOT_TAKEN

125           LOAD_FAST_BORROW         4 (extra)
              LOAD_ATTR                1 (items + NULL|self)
              CALL                     0
              GET_ITER
      L3:     FOR_ITER                17 (to L5)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST  103 (k, v)

126           LOAD_FAST_BORROW_LOAD_FAST_BORROW 101 (k, fields)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN

127           JUMP_BACKWARD           13 (to L3)

128   L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 117 (v, fields)
              LOAD_FAST_BORROW         6 (k)
              STORE_SUBSCR
              JUMP_BACKWARD           19 (to L3)

125   L5:     END_FOR
              POP_ITER

129   L6:     LOAD_GLOBAL              2 (logger)
              LOAD_ATTR                5 (info + NULL|self)
              LOAD_CONST               6 (' | ')
              LOAD_ATTR                7 (join + NULL|self)
              LOAD_CONST               7 (<code object <genexpr> at 0x0000018C17FBFEE0, file "app\services\memory\review.py", line 129>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         5 (fields)
              LOAD_ATTR                1 (items + NULL|self)
              CALL                     0
              GET_ITER
              CALL                     0
              CALL                     1
              CALL                     1
              POP_TOP
              LOAD_CONST               8 (None)
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C17FBFEE0, file "app\services\memory\review.py", line 129>:
 129           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                14 (to L3)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   18 (k, v)
               LOAD_FAST_BORROW         1 (k)
               FORMAT_SIMPLE
               LOAD_CONST               0 ('=')
               LOAD_FAST_BORROW         2 (v)
               FORMAT_SIMPLE
               BUILD_STRING             3
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           16 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app\services\memory\review.py", line 132>:
132           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('memory_id')

134           LOAD_CONST               2 ('str')

132           LOAD_CONST               3 ('brokerage_id')

135           LOAD_CONST               2 ('str')

132           LOAD_CONST               4 ('new_status')

136           LOAD_CONST               5 ('MemoryStatus')

132           LOAD_CONST               6 ('op')

137           LOAD_CONST               2 ('str')

132           LOAD_CONST               7 ('return')

138           LOAD_CONST               8 ('Optional[Dict[str, Any]]')

132           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _execute_status_update at 0x0000018C17D8D460, file "app\services\memory\review.py", line 132>:
 132            RESUME                   0

 148            NOP

 149    L1:     LOAD_GLOBAL              1 (_get_db + NULL)
                CALL                     0
                STORE_FAST               4 (db)

 150            LOAD_CONST               1 ('status')
                LOAD_FAST_BORROW         2 (new_status)
                LOAD_ATTR                2 (value)
                BUILD_MAP                1
                STORE_FAST               5 (update)

 152            LOAD_FAST_BORROW         4 (db)
                LOAD_ATTR                5 (table + NULL|self)
                LOAD_GLOBAL              6 (_TABLE_RECORDS)
                CALL                     1

 153            LOAD_ATTR                9 (update + NULL|self)
                LOAD_FAST_BORROW         5 (update)
                CALL                     1

 154            LOAD_ATTR               11 (eq + NULL|self)
                LOAD_CONST               2 ('memory_id')
                LOAD_FAST_BORROW         0 (memory_id)
                CALL                     2

 155            LOAD_ATTR               11 (eq + NULL|self)
                LOAD_CONST               3 ('brokerage_id')
                LOAD_FAST_BORROW         1 (brokerage_id)
                CALL                     2

 156            LOAD_ATTR               13 (execute + NULL|self)
                CALL                     0

 151            STORE_FAST               6 (result)

 158            LOAD_GLOBAL             15 (getattr + NULL)
                LOAD_FAST_BORROW         6 (result)
                LOAD_CONST               4 ('data')
                LOAD_CONST               5 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
        L2:     NOT_TAKEN
        L3:     POP_TOP
                LOAD_FAST                5 (update)
        L4:     RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 159            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       60 (to L9)
                NOT_TAKEN
                STORE_FAST               7 (e)

 160    L6:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 161            LOAD_FAST                3 (op)
                FORMAT_SIMPLE
                LOAD_CONST               6 (' status update failed (non-critical) | memory_id=')

 162            LOAD_FAST                0 (memory_id)
                FORMAT_SIMPLE
                LOAD_CONST               7 (' | error_type=')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE

 161            BUILD_STRING             5

 160            CALL                     1
                POP_TOP

 164    L7:     POP_EXCEPT
                LOAD_CONST               5 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                LOAD_CONST               5 (None)
                RETURN_VALUE

  --    L8:     LOAD_CONST               5 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 159    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L3 to L4 -> L5 [0]
  L5 to L6 -> L10 [1] lasti
  L6 to L7 -> L8 [1] lasti
  L8 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app\services\memory\review.py", line 167>:
167           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')

168           LOAD_CONST               2 ('Dict[str, Any]')

167           LOAD_CONST               3 ('op')

170           LOAD_CONST               4 ('str')

167           LOAD_CONST               5 ('return')

171           LOAD_CONST               6 ('Optional[Dict[str, Any]]')

167           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _execute_review_insert at 0x0000018C17FEDA30, file "app\services\memory\review.py", line 167>:
 167           RESUME                   0

 173           NOP

 174   L1:     LOAD_GLOBAL              1 (_get_db + NULL)
               CALL                     0
               STORE_FAST               2 (db)

 175           LOAD_FAST_BORROW         2 (db)
               LOAD_ATTR                3 (table + NULL|self)
               LOAD_GLOBAL              4 (_TABLE_REVIEW)
               CALL                     1
               LOAD_ATTR                7 (insert + NULL|self)
               LOAD_FAST_BORROW         0 (row)
               CALL                     1
               LOAD_ATTR                9 (execute + NULL|self)
               CALL                     0
               POP_TOP

 176           LOAD_FAST_BORROW         0 (row)
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 177           LOAD_GLOBAL             10 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       75 (to L7)
               NOT_TAKEN
               STORE_FAST               3 (e)

 178   L4:     LOAD_GLOBAL             12 (logger)
               LOAD_ATTR               15 (warning + NULL|self)

 179           LOAD_FAST                1 (op)
               FORMAT_SIMPLE
               LOAD_CONST               1 (' audit insert failed (non-critical) | memory_id=')

 180           LOAD_FAST                0 (row)
               LOAD_ATTR               17 (get + NULL|self)
               LOAD_CONST               2 ('memory_id')
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST               3 (' | error_type=')

 181           LOAD_GLOBAL             19 (type + NULL)
               LOAD_FAST                3 (e)
               CALL                     1
               LOAD_ATTR               20 (__name__)
               FORMAT_SIMPLE

 179           BUILD_STRING             5

 178           CALL                     1
               POP_TOP

 183   L5:     POP_EXCEPT
               LOAD_CONST               4 (None)
               STORE_FAST               3 (e)
               DELETE_FAST              3 (e)
               LOAD_CONST               4 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               4 (None)
               STORE_FAST               3 (e)
               DELETE_FAST              3 (e)
               RERAISE                  1

 177   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C180C4470, file "app\services\memory\review.py", line 190>:
190           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('op')

192           LOAD_CONST               2 ('str')

190           LOAD_CONST               3 ('memory_id')

193           LOAD_CONST               4 ('Any')

190           LOAD_CONST               5 ('brokerage_id')

194           LOAD_CONST               4 ('Any')

190           LOAD_CONST               6 ('target_status')

195           LOAD_CONST               7 ('MemoryStatus')

190           LOAD_CONST               8 ('actor_type')

196           LOAD_CONST               4 ('Any')

190           LOAD_CONST               9 ('actor_id')

197           LOAD_CONST              10 ('Optional[str]')

190           LOAD_CONST              11 ('reason')

198           LOAD_CONST              10 ('Optional[str]')

190           LOAD_CONST              12 ('enforce_transition_table')

199           LOAD_CONST              13 ('bool')

190           LOAD_CONST              14 ('extra_dangerous_check')

200           LOAD_CONST              13 ('bool')

190           LOAD_CONST              15 ('return')

201           LOAD_CONST              16 ('Dict[str, Any]')

190           BUILD_MAP               10
              RETURN_VALUE

Disassembly of <code object _run_transition at 0x0000018C17ED7F00, file "app\services\memory\review.py", line 190>:
 190            RESUME                   0

 216            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (brokerage_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        89 (to L5)
                NOT_TAKEN

 217    L1:     LOAD_GLOBAL              7 (_safe_log_decision + NULL)

 218            LOAD_FAST_LOAD_FAST      1 (op, memory_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              3 (str + NULL)
                LOAD_FAST_BORROW         1 (memory_id)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               1 ('')

 219    L3:     LOAD_CONST               1 ('')
                LOAD_CONST               2 ('refused')

 220            LOAD_CONST               3 ('reason')
                LOAD_CONST               4 ('missing_brokerage_id')
                BUILD_MAP                1

 217            LOAD_CONST               5 (('op', 'memory_id', 'brokerage_id', 'decision', 'extra'))
                CALL_KW                  5
                POP_TOP

 222            LOAD_GLOBAL              9 (_failure + NULL)

 223            LOAD_CONST               6 ('brokerage_id is required (tenant isolation)')
                BUILD_LIST               1

 224            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (memory_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L4)
                NOT_TAKEN
                LOAD_GLOBAL              3 (str + NULL)
                LOAD_FAST_BORROW         1 (memory_id)
                CALL                     1

 222            LOAD_CONST               8 (('errors', 'memory_id'))
                CALL_KW                  2
                RETURN_VALUE

 224    L4:     LOAD_CONST               7 (None)

 222            LOAD_CONST               8 (('errors', 'memory_id'))
                CALL_KW                  2
                RETURN_VALUE

 226    L5:     LOAD_FAST_BORROW         2 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               2 (brokerage_id)

 228            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (memory_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L6)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (memory_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L7)
                NOT_TAKEN

 229    L6:     LOAD_GLOBAL              7 (_safe_log_decision + NULL)

 230            LOAD_FAST_BORROW         0 (op)
                LOAD_CONST               1 ('')
                LOAD_FAST_BORROW         2 (brokerage_id)

 231            LOAD_CONST               2 ('refused')
                LOAD_CONST               3 ('reason')
                LOAD_CONST               9 ('missing_memory_id')
                BUILD_MAP                1

 229            LOAD_CONST               5 (('op', 'memory_id', 'brokerage_id', 'decision', 'extra'))
                CALL_KW                  5
                POP_TOP

 233            LOAD_GLOBAL              9 (_failure + NULL)

 234            LOAD_CONST              10 ('memory_id is required')
                BUILD_LIST               1

 235            LOAD_FAST_BORROW         2 (brokerage_id)

 233            LOAD_CONST              11 (('errors', 'brokerage_id'))
                CALL_KW                  2
                RETURN_VALUE

 237    L7:     LOAD_FAST_BORROW         1 (memory_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               1 (memory_id)

 239            LOAD_GLOBAL             11 (_validate_actor_type + NULL)
                LOAD_FAST_BORROW         4 (actor_type)
                CALL                     1
                STORE_FAST               9 (valid_actor)

 240            LOAD_FAST_BORROW         9 (valid_actor)
                POP_JUMP_IF_NOT_NONE    62 (to L8)
                NOT_TAKEN

 241            LOAD_GLOBAL              7 (_safe_log_decision + NULL)

 242            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (op, memory_id)
                LOAD_FAST_BORROW         2 (brokerage_id)

 243            LOAD_CONST               2 ('refused')
                LOAD_CONST               3 ('reason')
                LOAD_CONST              12 ('invalid_actor_type')
                BUILD_MAP                1

 241            LOAD_CONST               5 (('op', 'memory_id', 'brokerage_id', 'decision', 'extra'))
                CALL_KW                  5
                POP_TOP

 245            LOAD_GLOBAL              9 (_failure + NULL)

 247            LOAD_CONST              13 ('actor_type must be one of ')

 248            LOAD_GLOBAL             13 (sorted + NULL)
                LOAD_GLOBAL             14 (audit_mod)
                LOAD_ATTR               16 (ALLOWED_ACTOR_TYPES)
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              14 ('; got ')
                LOAD_FAST_BORROW         4 (actor_type)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE

 247            BUILD_STRING             4

 246            BUILD_LIST               1

 250            LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (memory_id, brokerage_id)

 245            LOAD_CONST              15 (('errors', 'memory_id', 'brokerage_id'))
                CALL_KW                  3
                RETURN_VALUE

 254    L8:     LOAD_GLOBAL             18 (queries_mod)
                LOAD_ATTR               20 (get_memory_for_brokerage)
                PUSH_NULL
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (memory_id, brokerage_id)
                CALL                     2
                STORE_FAST              10 (existing)

 255            LOAD_FAST_BORROW        10 (existing)
                TO_BOOL
                POP_JUMP_IF_TRUE        43 (to L9)
                NOT_TAKEN

 256            LOAD_GLOBAL              7 (_safe_log_decision + NULL)

 257            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (op, memory_id)
                LOAD_FAST_BORROW         2 (brokerage_id)

 258            LOAD_CONST               2 ('refused')
                LOAD_CONST               3 ('reason')
                LOAD_CONST              16 ('memory_not_found')
                BUILD_MAP                1

 256            LOAD_CONST               5 (('op', 'memory_id', 'brokerage_id', 'decision', 'extra'))
                CALL_KW                  5
                POP_TOP

 260            LOAD_GLOBAL              9 (_failure + NULL)

 261            LOAD_CONST              17 ('memory not found for brokerage')
                BUILD_LIST               1

 262            LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (memory_id, brokerage_id)

 263            LOAD_FAST_BORROW         3 (target_status)
                LOAD_ATTR               22 (value)

 260            LOAD_CONST              18 (('errors', 'memory_id', 'brokerage_id', 'to_status'))
                CALL_KW                  4
                RETURN_VALUE

 266    L9:     LOAD_FAST_BORROW        10 (existing)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              19 ('status')
                CALL                     1
                STORE_FAST              11 (from_status)

 267            LOAD_FAST_BORROW        10 (existing)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              20 ('kind')
                CALL                     1
                STORE_FAST              12 (kind)

 270            LOAD_FAST_BORROW         7 (enforce_transition_table)
                TO_BOOL
                POP_JUMP_IF_FALSE      127 (to L12)
                NOT_TAKEN

 271            LOAD_GLOBAL             14 (audit_mod)
                LOAD_ATTR               26 (validate_review_transition)
                PUSH_NULL

 272            LOAD_FAST_BORROW_LOAD_FAST_BORROW 179 (from_status, target_status)
                LOAD_ATTR               22 (value)
                LOAD_FAST_BORROW         9 (valid_actor)

 271            LOAD_CONST              21 (('actor_type',))
                CALL_KW                  3
                STORE_FAST              13 (errors)

 274            LOAD_FAST_BORROW        13 (errors)
                TO_BOOL
                POP_JUMP_IF_FALSE       85 (to L12)
                NOT_TAKEN

 275            LOAD_GLOBAL              7 (_safe_log_decision + NULL)

 276            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (op, memory_id)
                LOAD_FAST_BORROW         2 (brokerage_id)

 277            LOAD_CONST               2 ('refused')

 278            LOAD_CONST               3 ('reason')
                LOAD_CONST              22 ('invalid_transition')

 279            LOAD_CONST              23 ('from_status')
                LOAD_GLOBAL              3 (str + NULL)
                LOAD_FAST_BORROW        11 (from_status)
                CALL                     1

 280            LOAD_CONST              24 ('to_status')
                LOAD_FAST_BORROW         3 (target_status)
                LOAD_ATTR               22 (value)

 278            BUILD_MAP                3

 275            LOAD_CONST               5 (('op', 'memory_id', 'brokerage_id', 'decision', 'extra'))
                CALL_KW                  5
                POP_TOP

 282            LOAD_GLOBAL              9 (_failure + NULL)

 283            LOAD_FAST_LOAD_FAST    209 (errors, memory_id)

 284            LOAD_FAST                2 (brokerage_id)

 285            LOAD_FAST_BORROW        11 (from_status)
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L10)
                NOT_TAKEN
                LOAD_GLOBAL              3 (str + NULL)
                LOAD_FAST_BORROW        11 (from_status)
                CALL                     1
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST               7 (None)

 286   L11:     LOAD_FAST_BORROW         3 (target_status)
                LOAD_ATTR               22 (value)

 282            LOAD_CONST              25 (('errors', 'memory_id', 'brokerage_id', 'from_status', 'to_status'))
                CALL_KW                  5
                RETURN_VALUE

 294   L12:     LOAD_FAST_BORROW         8 (extra_dangerous_check)
                TO_BOOL
                POP_JUMP_IF_FALSE      122 (to L15)
                NOT_TAKEN

 295            LOAD_FAST_BORROW        12 (kind)
                LOAD_GLOBAL             28 (MemoryKind)
                LOAD_ATTR               30 (DANGEROUS)
                LOAD_ATTR               22 (value)
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       91 (to L15)
                NOT_TAKEN

 296            LOAD_FAST_BORROW         3 (target_status)
                LOAD_GLOBAL             32 (MemoryStatus)
                LOAD_ATTR               34 (APPROVED)
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       70 (to L15)
                NOT_TAKEN

 297            LOAD_FAST_BORROW         9 (valid_actor)
                LOAD_CONST              43 (frozenset({'ADMIN', 'SECURITY'}))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       63 (to L15)
                NOT_TAKEN

 299            LOAD_GLOBAL              7 (_safe_log_decision + NULL)

 300            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (op, memory_id)
                LOAD_FAST_BORROW         2 (brokerage_id)

 301            LOAD_CONST               2 ('refused')

 302            LOAD_CONST               3 ('reason')
                LOAD_CONST              26 ('dangerous_normal_approval_blocked')
                BUILD_MAP                1

 299            LOAD_CONST               5 (('op', 'memory_id', 'brokerage_id', 'decision', 'extra'))
                CALL_KW                  5
                POP_TOP

 304            LOAD_GLOBAL              9 (_failure + NULL)

 306            LOAD_CONST              27 ('DANGEROUS-kind memory cannot be approved through normal approval; requires SECURITY or ADMIN actor')

 305            BUILD_LIST               1

 309            LOAD_FAST_LOAD_FAST     18 (memory_id, brokerage_id)

 310            LOAD_FAST_BORROW        11 (from_status)
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L13)
                NOT_TAKEN
                LOAD_GLOBAL              3 (str + NULL)
                LOAD_FAST_BORROW        11 (from_status)
                CALL                     1
                JUMP_FORWARD             1 (to L14)
       L13:     LOAD_CONST               7 (None)

 311   L14:     LOAD_FAST_BORROW         3 (target_status)
                LOAD_ATTR               22 (value)

 304            LOAD_CONST              25 (('errors', 'memory_id', 'brokerage_id', 'from_status', 'to_status'))
                CALL_KW                  5
                RETURN_VALUE

 315   L15:     LOAD_GLOBAL             37 (_execute_status_update + NULL)

 316            LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (memory_id, brokerage_id)

 317            LOAD_FAST_BORROW_LOAD_FAST_BORROW 48 (target_status, op)

 315            LOAD_CONST              28 (('memory_id', 'brokerage_id', 'new_status', 'op'))
                CALL_KW                  4
                STORE_FAST              14 (updated)

 319            LOAD_FAST_BORROW        14 (updated)
                POP_JUMP_IF_NOT_NONE    46 (to L18)
                NOT_TAKEN

 320            LOAD_GLOBAL              9 (_failure + NULL)

 321            LOAD_CONST              29 ('status update failed (storage unavailable)')
                BUILD_LIST               1

 322            LOAD_FAST_LOAD_FAST     18 (memory_id, brokerage_id)

 323            LOAD_FAST_BORROW        11 (from_status)
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L16)
                NOT_TAKEN
                LOAD_GLOBAL              3 (str + NULL)
                LOAD_FAST_BORROW        11 (from_status)
                CALL                     1
                JUMP_FORWARD             1 (to L17)
       L16:     LOAD_CONST               7 (None)

 324   L17:     LOAD_FAST_BORROW         3 (target_status)
                LOAD_ATTR               22 (value)

 320            LOAD_CONST              25 (('errors', 'memory_id', 'brokerage_id', 'from_status', 'to_status'))
                CALL_KW                  5
                RETURN_VALUE

 328   L18:     NOP

 329   L19:     LOAD_GLOBAL             14 (audit_mod)
                LOAD_ATTR               38 (build_review_event)
                PUSH_NULL

 330            LOAD_FAST_BORROW         1 (memory_id)

 331            LOAD_FAST_BORROW         2 (brokerage_id)

 332            LOAD_FAST_BORROW        11 (from_status)

 333            LOAD_FAST_BORROW         3 (target_status)
                LOAD_ATTR               22 (value)

 334            LOAD_FAST_BORROW         9 (valid_actor)

 335            LOAD_FAST_BORROW         5 (actor_id)

 336            LOAD_FAST_BORROW         6 (reason)

 329            LOAD_CONST              30 (('memory_id', 'brokerage_id', 'from_status', 'to_status', 'actor_type', 'actor_id', 'reason'))
                CALL_KW                  7
                STORE_FAST              15 (event)

 338            LOAD_GLOBAL             14 (audit_mod)
                LOAD_ATTR               40 (review_event_to_row)
                PUSH_NULL
                LOAD_FAST_BORROW        15 (event)
                CALL                     1
                STORE_FAST              16 (row)

 358   L20:     LOAD_GLOBAL             51 (_execute_review_insert + NULL)
                LOAD_FAST               16 (row)
                LOAD_FAST                0 (op)
                LOAD_CONST              38 (('op',))
                CALL_KW                  2
                STORE_FAST              18 (inserted)

 359            LOAD_FAST               18 (inserted)
                POP_JUMP_IF_NOT_NONE    52 (to L21)
                NOT_TAKEN

 360            LOAD_GLOBAL              7 (_safe_log_decision + NULL)

 361            LOAD_FAST_LOAD_FAST      1 (op, memory_id)
                LOAD_FAST                2 (brokerage_id)

 362            LOAD_CONST              31 ('warning')

 363            LOAD_CONST               3 ('reason')
                LOAD_CONST              39 ('audit_write_failed')
                BUILD_MAP                1

 360            LOAD_CONST               5 (('op', 'memory_id', 'brokerage_id', 'decision', 'extra'))
                CALL_KW                  5
                POP_TOP

 366            LOAD_CONST              19 ('status')
                LOAD_CONST              31 ('warning')

 367            LOAD_CONST              34 ('memory_id')
                LOAD_FAST                1 (memory_id)

 368            LOAD_CONST              35 ('brokerage_id')
                LOAD_FAST                2 (brokerage_id)

 369            LOAD_CONST              23 ('from_status')
                LOAD_FAST               11 (from_status)

 370            LOAD_CONST              24 ('to_status')
                LOAD_FAST                3 (target_status)
                LOAD_ATTR               22 (value)

 371            LOAD_CONST              40 ('review_id')
                LOAD_FAST               15 (event)
                LOAD_CONST              40 ('review_id')
                BINARY_OP               26 ([])

 372            LOAD_CONST              36 ('warnings')
                LOAD_CONST              39 ('audit_write_failed')
                BUILD_LIST               1

 365            BUILD_MAP                7
                RETURN_VALUE

 375   L21:     LOAD_GLOBAL              7 (_safe_log_decision + NULL)

 376            LOAD_FAST_LOAD_FAST      1 (op, memory_id)
                LOAD_FAST                2 (brokerage_id)

 377            LOAD_CONST              41 ('ok')

 378            LOAD_CONST              23 ('from_status')
                LOAD_GLOBAL              3 (str + NULL)
                LOAD_FAST               11 (from_status)
                CALL                     1

 379            LOAD_CONST              24 ('to_status')
                LOAD_FAST                3 (target_status)
                LOAD_ATTR               22 (value)

 380            LOAD_CONST              42 ('actor_type')
                LOAD_FAST                9 (valid_actor)

 378            BUILD_MAP                3

 375            LOAD_CONST               5 (('op', 'memory_id', 'brokerage_id', 'decision', 'extra'))
                CALL_KW                  5
                POP_TOP

 383            LOAD_CONST              19 ('status')
                LOAD_CONST              41 ('ok')

 384            LOAD_CONST              34 ('memory_id')
                LOAD_FAST                1 (memory_id)

 385            LOAD_CONST              35 ('brokerage_id')
                LOAD_FAST                2 (brokerage_id)

 386            LOAD_CONST              23 ('from_status')
                LOAD_FAST               11 (from_status)

 387            LOAD_CONST              24 ('to_status')
                LOAD_FAST                3 (target_status)
                LOAD_ATTR               22 (value)

 388            LOAD_CONST              40 ('review_id')
                LOAD_FAST               15 (event)
                LOAD_CONST              40 ('review_id')
                BINARY_OP               26 ([])

 382            BUILD_MAP                6
                RETURN_VALUE

  --   L22:     PUSH_EXC_INFO

 339            LOAD_GLOBAL             42 (TypeError)
                LOAD_GLOBAL             44 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       96 (to L27)
                NOT_TAKEN
                STORE_FAST              17 (e)

 343   L23:     LOAD_GLOBAL              7 (_safe_log_decision + NULL)

 344            LOAD_FAST_LOAD_FAST      1 (op, memory_id)
                LOAD_FAST                2 (brokerage_id)

 345            LOAD_CONST              31 ('warning')

 346            LOAD_CONST               3 ('reason')
                LOAD_CONST              32 ('audit_event_build_failed')

 347            LOAD_CONST              33 ('error_type')
                LOAD_GLOBAL             47 (type + NULL)
                LOAD_FAST               17 (e)
                CALL                     1
                LOAD_ATTR               48 (__name__)

 346            BUILD_MAP                2

 343            LOAD_CONST               5 (('op', 'memory_id', 'brokerage_id', 'decision', 'extra'))
                CALL_KW                  5
                POP_TOP

 350            LOAD_CONST              19 ('status')
                LOAD_CONST              31 ('warning')

 351            LOAD_CONST              34 ('memory_id')
                LOAD_FAST                1 (memory_id)

 352            LOAD_CONST              35 ('brokerage_id')
                LOAD_FAST                2 (brokerage_id)

 353            LOAD_CONST              23 ('from_status')
                LOAD_FAST               11 (from_status)

 354            LOAD_CONST              24 ('to_status')
                LOAD_FAST                3 (target_status)
                LOAD_ATTR               22 (value)

 355            LOAD_CONST              36 ('warnings')
                LOAD_CONST              37 ('audit_event_build_failed:')
                LOAD_GLOBAL             47 (type + NULL)
                LOAD_FAST               17 (e)
                CALL                     1
                LOAD_ATTR               48 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 349            BUILD_MAP                6
       L24:     SWAP                     2
       L25:     POP_EXCEPT
                LOAD_CONST               7 (None)
                STORE_FAST              17 (e)
                DELETE_FAST             17 (e)
                RETURN_VALUE

  --   L26:     LOAD_CONST               7 (None)
                STORE_FAST              17 (e)
                DELETE_FAST             17 (e)
                RERAISE                  1

 339   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L19 to L20 -> L22 [0]
  L22 to L23 -> L28 [1] lasti
  L23 to L24 -> L26 [1] lasti
  L24 to L25 -> L28 [1] lasti
  L26 to L28 -> L28 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\services\memory\review.py", line 396>:
396           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('memory_id')

397           LOAD_CONST               2 ('str')

396           LOAD_CONST               3 ('brokerage_id')

398           LOAD_CONST               2 ('str')

396           LOAD_CONST               4 ('actor_type')

399           LOAD_CONST               2 ('str')

396           LOAD_CONST               5 ('actor_id')

400           LOAD_CONST               6 ('Optional[str]')

396           LOAD_CONST               7 ('reason')

401           LOAD_CONST               6 ('Optional[str]')

396           LOAD_CONST               8 ('return')

402           LOAD_CONST               9 ('Dict[str, Any]')

396           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object approve_memory at 0x0000018C18053E10, file "app\services\memory\review.py", line 396>:
396           RESUME                   0

414           LOAD_GLOBAL              1 (_run_transition + NULL)

415           LOAD_CONST               1 ('approve_memory')

416           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (memory_id, brokerage_id)

417           LOAD_GLOBAL              2 (MemoryStatus)
              LOAD_ATTR                4 (APPROVED)

418           LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (actor_type, actor_id)
              LOAD_FAST_BORROW         4 (reason)

419           LOAD_CONST               2 (True)

420           LOAD_CONST               2 (True)

414           LOAD_CONST               3 (('op', 'memory_id', 'brokerage_id', 'target_status', 'actor_type', 'actor_id', 'reason', 'enforce_transition_table', 'extra_dangerous_check'))
              CALL_KW                  9
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "app\services\memory\review.py", line 424>:
424           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('memory_id')

425           LOAD_CONST               2 ('str')

424           LOAD_CONST               3 ('brokerage_id')

426           LOAD_CONST               2 ('str')

424           LOAD_CONST               4 ('actor_type')

427           LOAD_CONST               2 ('str')

424           LOAD_CONST               5 ('actor_id')

428           LOAD_CONST               6 ('Optional[str]')

424           LOAD_CONST               7 ('reason')

429           LOAD_CONST               6 ('Optional[str]')

424           LOAD_CONST               8 ('return')

430           LOAD_CONST               9 ('Dict[str, Any]')

424           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object reject_memory at 0x0000018C18053090, file "app\services\memory\review.py", line 424>:
424           RESUME                   0

437           LOAD_GLOBAL              1 (_run_transition + NULL)

438           LOAD_CONST               1 ('reject_memory')

439           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (memory_id, brokerage_id)

440           LOAD_GLOBAL              2 (MemoryStatus)
              LOAD_ATTR                4 (REJECTED)

441           LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (actor_type, actor_id)
              LOAD_FAST_BORROW         4 (reason)

442           LOAD_CONST               2 (True)

443           LOAD_CONST               3 (False)

437           LOAD_CONST               4 (('op', 'memory_id', 'brokerage_id', 'target_status', 'actor_type', 'actor_id', 'reason', 'enforce_transition_table', 'extra_dangerous_check'))
              CALL_KW                  9
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "app\services\memory\review.py", line 447>:
447           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('memory_id')

448           LOAD_CONST               2 ('str')

447           LOAD_CONST               3 ('brokerage_id')

449           LOAD_CONST               2 ('str')

447           LOAD_CONST               4 ('actor_type')

450           LOAD_CONST               2 ('str')

447           LOAD_CONST               5 ('actor_id')

451           LOAD_CONST               6 ('Optional[str]')

447           LOAD_CONST               7 ('reason')

452           LOAD_CONST               6 ('Optional[str]')

447           LOAD_CONST               8 ('return')

453           LOAD_CONST               9 ('Dict[str, Any]')

447           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object expire_memory_by_id at 0x0000018C18052F70, file "app\services\memory\review.py", line 447>:
447           RESUME                   0

459           LOAD_GLOBAL              1 (_run_transition + NULL)

460           LOAD_CONST               1 ('expire_memory_by_id')

461           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (memory_id, brokerage_id)

462           LOAD_GLOBAL              2 (MemoryStatus)
              LOAD_ATTR                4 (EXPIRED)

463           LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (actor_type, actor_id)
              LOAD_FAST_BORROW         4 (reason)

464           LOAD_CONST               2 (True)

465           LOAD_CONST               3 (False)

459           LOAD_CONST               4 (('op', 'memory_id', 'brokerage_id', 'target_status', 'actor_type', 'actor_id', 'reason', 'enforce_transition_table', 'extra_dangerous_check'))
              CALL_KW                  9
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app\services\memory\review.py", line 469>:
469           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('memory_id')

470           LOAD_CONST               2 ('str')

469           LOAD_CONST               3 ('brokerage_id')

471           LOAD_CONST               2 ('str')

469           LOAD_CONST               4 ('actor_type')

472           LOAD_CONST               2 ('str')

469           LOAD_CONST               5 ('actor_id')

473           LOAD_CONST               6 ('Optional[str]')

469           LOAD_CONST               7 ('reason')

474           LOAD_CONST               6 ('Optional[str]')

469           LOAD_CONST               8 ('return')

475           LOAD_CONST               9 ('Dict[str, Any]')

469           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object quarantine_memory_by_id at 0x0000018C17D94CE0, file "app\services\memory\review.py", line 469>:
 469            RESUME                   0

 489            LOAD_GLOBAL              1 (isinstance + NULL)
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
                POP_JUMP_IF_TRUE        90 (to L5)
                NOT_TAKEN

 490    L1:     LOAD_GLOBAL              7 (_safe_log_decision + NULL)

 491            LOAD_CONST               1 ('quarantine_memory_by_id')

 492            LOAD_FAST_BORROW         0 (memory_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              3 (str + NULL)
                LOAD_FAST_BORROW         0 (memory_id)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               2 ('')

 493    L3:     LOAD_CONST               2 ('')
                LOAD_CONST               3 ('refused')

 494            LOAD_CONST               4 ('reason')
                LOAD_CONST               5 ('missing_brokerage_id')
                BUILD_MAP                1

 490            LOAD_CONST               6 (('op', 'memory_id', 'brokerage_id', 'decision', 'extra'))
                CALL_KW                  5
                POP_TOP

 496            LOAD_GLOBAL              9 (_failure + NULL)

 497            LOAD_CONST               7 ('brokerage_id is required (tenant isolation)')
                BUILD_LIST               1

 498            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (memory_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L4)
                NOT_TAKEN
                LOAD_GLOBAL              3 (str + NULL)
                LOAD_FAST_BORROW         0 (memory_id)
                CALL                     1

 496            LOAD_CONST               9 (('errors', 'memory_id'))
                CALL_KW                  2
                RETURN_VALUE

 498    L4:     LOAD_CONST               8 (None)

 496            LOAD_CONST               9 (('errors', 'memory_id'))
                CALL_KW                  2
                RETURN_VALUE

 500    L5:     LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               1 (brokerage_id)

 502            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (memory_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L6)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (memory_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L7)
                NOT_TAKEN

 503    L6:     LOAD_GLOBAL              9 (_failure + NULL)

 504            LOAD_CONST              10 ('memory_id is required')
                BUILD_LIST               1

 505            LOAD_FAST_BORROW         1 (brokerage_id)

 503            LOAD_CONST              11 (('errors', 'brokerage_id'))
                CALL_KW                  2
                RETURN_VALUE

 507    L7:     LOAD_FAST_BORROW         0 (memory_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               0 (memory_id)

 509            LOAD_GLOBAL             11 (_validate_actor_type + NULL)
                LOAD_FAST_BORROW         2 (actor_type)
                CALL                     1
                STORE_FAST               5 (valid_actor)

 510            LOAD_FAST_BORROW         5 (valid_actor)
                POP_JUMP_IF_NOT_NONE    45 (to L8)
                NOT_TAKEN

 511            LOAD_GLOBAL              9 (_failure + NULL)

 513            LOAD_CONST              12 ('actor_type must be one of ')

 514            LOAD_GLOBAL             13 (sorted + NULL)
                LOAD_GLOBAL             14 (audit_mod)
                LOAD_ATTR               16 (ALLOWED_ACTOR_TYPES)
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              13 ('; got ')
                LOAD_FAST_BORROW         2 (actor_type)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE

 513            BUILD_STRING             4

 512            BUILD_LIST               1

 516            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (memory_id, brokerage_id)

 511            LOAD_CONST              14 (('errors', 'memory_id', 'brokerage_id'))
                CALL_KW                  3
                RETURN_VALUE

 519    L8:     LOAD_GLOBAL             18 (queries_mod)
                LOAD_ATTR               20 (get_memory_for_brokerage)
                PUSH_NULL
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (memory_id, brokerage_id)
                CALL                     2
                STORE_FAST               6 (existing)

 520            LOAD_FAST_BORROW         6 (existing)
                TO_BOOL
                POP_JUMP_IF_TRUE        40 (to L9)
                NOT_TAKEN

 521            LOAD_GLOBAL              9 (_failure + NULL)

 522            LOAD_CONST              15 ('memory not found for brokerage')
                BUILD_LIST               1

 523            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (memory_id, brokerage_id)

 524            LOAD_GLOBAL             22 (MemoryStatus)
                LOAD_ATTR               24 (QUARANTINED)
                LOAD_ATTR               26 (value)

 521            LOAD_CONST              16 (('errors', 'memory_id', 'brokerage_id', 'to_status'))
                CALL_KW                  4
                RETURN_VALUE

 527    L9:     LOAD_FAST_BORROW         6 (existing)
                LOAD_ATTR               29 (get + NULL|self)
                LOAD_CONST              17 ('status')
                CALL                     1
                STORE_FAST               7 (from_status)

 528            LOAD_FAST_BORROW         7 (from_status)
                LOAD_GLOBAL             22 (MemoryStatus)
                LOAD_ATTR               30 (REJECTED)
                LOAD_ATTR               26 (value)
                LOAD_GLOBAL             22 (MemoryStatus)
                LOAD_ATTR               32 (EXPIRED)
                LOAD_ATTR               26 (value)
                BUILD_TUPLE              2
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       44 (to L10)
                NOT_TAKEN

 529            LOAD_GLOBAL              9 (_failure + NULL)

 531            LOAD_CONST              18 ('cannot quarantine memory in terminal status ')
                LOAD_FAST_BORROW         7 (from_status)
                FORMAT_SIMPLE
                BUILD_STRING             2

 530            BUILD_LIST               1

 533            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (memory_id, brokerage_id)

 534            LOAD_FAST_BORROW         7 (from_status)

 535            LOAD_GLOBAL             22 (MemoryStatus)
                LOAD_ATTR               24 (QUARANTINED)
                LOAD_ATTR               26 (value)

 529            LOAD_CONST              19 (('errors', 'memory_id', 'brokerage_id', 'from_status', 'to_status'))
                CALL_KW                  5
                RETURN_VALUE

 540   L10:     LOAD_GLOBAL             34 (store_mod)
                LOAD_ATTR               36 (quarantine_memory)
                PUSH_NULL

 541            LOAD_FAST_LOAD_FAST      4 (memory_id, reason)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
       L11:     LOAD_FAST_BORROW         1 (brokerage_id)

 540            LOAD_CONST              20 (('reason', 'brokerage_id'))
                CALL_KW                  3
                STORE_FAST               8 (updated)

 543            LOAD_FAST_BORROW         8 (updated)
                POP_JUMP_IF_NOT_NONE    41 (to L12)
                NOT_TAKEN

 544            LOAD_GLOBAL              9 (_failure + NULL)

 545            LOAD_CONST              21 ('status update failed (storage unavailable)')
                BUILD_LIST               1

 546            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (memory_id, brokerage_id)

 547            LOAD_FAST_BORROW         7 (from_status)

 548            LOAD_GLOBAL             22 (MemoryStatus)
                LOAD_ATTR               24 (QUARANTINED)
                LOAD_ATTR               26 (value)

 544            LOAD_CONST              19 (('errors', 'memory_id', 'brokerage_id', 'from_status', 'to_status'))
                CALL_KW                  5
                RETURN_VALUE

 551   L12:     NOP

 552   L13:     LOAD_GLOBAL             14 (audit_mod)
                LOAD_ATTR               38 (build_review_event)
                PUSH_NULL

 553            LOAD_FAST_BORROW         0 (memory_id)

 554            LOAD_FAST_BORROW         1 (brokerage_id)

 555            LOAD_FAST_BORROW         7 (from_status)

 556            LOAD_GLOBAL             22 (MemoryStatus)
                LOAD_ATTR               24 (QUARANTINED)
                LOAD_ATTR               26 (value)

 557            LOAD_FAST_BORROW         5 (valid_actor)

 558            LOAD_FAST_BORROW         3 (actor_id)

 559            LOAD_FAST_BORROW         4 (reason)

 552            LOAD_CONST              22 (('memory_id', 'brokerage_id', 'from_status', 'to_status', 'actor_type', 'actor_id', 'reason'))
                CALL_KW                  7
                STORE_FAST               9 (event)

 561            LOAD_GLOBAL             14 (audit_mod)
                LOAD_ATTR               40 (review_event_to_row)
                PUSH_NULL
                LOAD_FAST_BORROW         9 (event)
                CALL                     1
                STORE_FAST              10 (row)

 572   L14:     LOAD_GLOBAL             51 (_execute_review_insert + NULL)
                LOAD_FAST               10 (row)
                LOAD_CONST               1 ('quarantine_memory_by_id')
                LOAD_CONST              30 (('op',))
                CALL_KW                  2
                STORE_FAST              12 (inserted)

 573            LOAD_FAST               12 (inserted)
                POP_JUMP_IF_NOT_NONE    49 (to L15)
                NOT_TAKEN

 575            LOAD_CONST              17 ('status')
                LOAD_CONST              23 ('warning')

 576            LOAD_CONST              24 ('memory_id')
                LOAD_FAST                0 (memory_id)

 577            LOAD_CONST              25 ('brokerage_id')
                LOAD_FAST                1 (brokerage_id)

 578            LOAD_CONST              26 ('from_status')
                LOAD_FAST                7 (from_status)

 579            LOAD_CONST              27 ('to_status')
                LOAD_GLOBAL             22 (MemoryStatus)
                LOAD_ATTR               24 (QUARANTINED)
                LOAD_ATTR               26 (value)

 580            LOAD_CONST              31 ('review_id')
                LOAD_FAST                9 (event)
                LOAD_CONST              31 ('review_id')
                BINARY_OP               26 ([])

 581            LOAD_CONST              28 ('warnings')
                LOAD_CONST              32 ('audit_write_failed')
                BUILD_LIST               1

 574            BUILD_MAP                7
                RETURN_VALUE

 585   L15:     LOAD_CONST              17 ('status')
                LOAD_CONST              33 ('ok')

 586            LOAD_CONST              24 ('memory_id')
                LOAD_FAST                0 (memory_id)

 587            LOAD_CONST              25 ('brokerage_id')
                LOAD_FAST                1 (brokerage_id)

 588            LOAD_CONST              26 ('from_status')
                LOAD_FAST                7 (from_status)

 589            LOAD_CONST              27 ('to_status')
                LOAD_GLOBAL             22 (MemoryStatus)
                LOAD_ATTR               24 (QUARANTINED)
                LOAD_ATTR               26 (value)

 590            LOAD_CONST              31 ('review_id')
                LOAD_FAST                9 (event)
                LOAD_CONST              31 ('review_id')
                BINARY_OP               26 ([])

 584            BUILD_MAP                6
                RETURN_VALUE

  --   L16:     PUSH_EXC_INFO

 562            LOAD_GLOBAL             42 (TypeError)
                LOAD_GLOBAL             44 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       72 (to L21)
                NOT_TAKEN
                STORE_FAST              11 (e)

 564   L17:     LOAD_CONST              17 ('status')
                LOAD_CONST              23 ('warning')

 565            LOAD_CONST              24 ('memory_id')
                LOAD_FAST                0 (memory_id)

 566            LOAD_CONST              25 ('brokerage_id')
                LOAD_FAST                1 (brokerage_id)

 567            LOAD_CONST              26 ('from_status')
                LOAD_FAST                7 (from_status)

 568            LOAD_CONST              27 ('to_status')
                LOAD_GLOBAL             22 (MemoryStatus)
                LOAD_ATTR               24 (QUARANTINED)
                LOAD_ATTR               26 (value)

 569            LOAD_CONST              28 ('warnings')
                LOAD_CONST              29 ('audit_event_build_failed:')
                LOAD_GLOBAL             47 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               48 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 563            BUILD_MAP                6
       L18:     SWAP                     2
       L19:     POP_EXCEPT
                LOAD_CONST               8 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RETURN_VALUE

  --   L20:     LOAD_CONST               8 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 562   L21:     RERAISE                  0

  --   L22:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L13 to L14 -> L16 [0]
  L16 to L17 -> L22 [1] lasti
  L17 to L18 -> L20 [1] lasti
  L18 to L19 -> L22 [1] lasti
  L20 to L22 -> L22 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025B30, file "app\services\memory\review.py", line 598>:
598           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('memory_id')

599           LOAD_CONST               2 ('str')

598           LOAD_CONST               3 ('brokerage_id')

600           LOAD_CONST               2 ('str')

598           LOAD_CONST               4 ('limit')

602           LOAD_CONST               5 ('int')

598           LOAD_CONST               6 ('return')

603           LOAD_CONST               7 ('List[Dict[str, Any]]')

598           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object list_memory_review_events at 0x0000018C17D7D6B0, file "app\services\memory\review.py", line 598>:
 598            RESUME                   0

 609            LOAD_GLOBAL              1 (isinstance + NULL)
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
                POP_JUMP_IF_TRUE        24 (to L2)
                NOT_TAKEN

 610    L1:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 611            LOAD_CONST               1 ('list_memory_review_events dropped | reason=missing_brokerage_id')

 610            CALL                     1
                POP_TOP

 613            BUILD_LIST               0
                RETURN_VALUE

 614    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (memory_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (memory_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        24 (to L4)
                NOT_TAKEN

 615    L3:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 616            LOAD_CONST               2 ('list_memory_review_events dropped | reason=invalid_memory_id')

 615            CALL                     1
                POP_TOP

 618            BUILD_LIST               0
                RETURN_VALUE

 620    L4:     NOP

 621    L5:     LOAD_GLOBAL             11 (max + NULL)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL             13 (min + NULL)
                LOAD_GLOBAL             15 (int + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1
                LOAD_GLOBAL             16 (queries_mod)
                LOAD_ATTR               18 (MAX_QUERY_LIMIT)
                CALL                     2
                CALL                     2
                STORE_FAST               3 (capped)

 625    L6:     NOP

 626    L7:     LOAD_GLOBAL             27 (_get_db + NULL)
                CALL                     0
                STORE_FAST               4 (db)

 628            LOAD_FAST_BORROW         4 (db)
                LOAD_ATTR               29 (table + NULL|self)
                LOAD_GLOBAL             30 (_TABLE_REVIEW)
                CALL                     1

 629            LOAD_ATTR               33 (select + NULL|self)
                LOAD_CONST               3 ('*')
                CALL                     1

 630            LOAD_ATTR               35 (eq + NULL|self)
                LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                CALL                     2

 631            LOAD_ATTR               35 (eq + NULL|self)
                LOAD_CONST               5 ('memory_id')
                LOAD_FAST_BORROW         0 (memory_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                CALL                     2

 632            LOAD_ATTR               37 (order + NULL|self)
                LOAD_CONST               6 ('created_at')
                LOAD_CONST               7 (True)
                LOAD_CONST               8 (('desc',))
                CALL_KW                  2

 633            LOAD_ATTR               39 (limit + NULL|self)
                LOAD_FAST_BORROW         3 (capped)
                CALL                     1

 634            LOAD_ATTR               41 (execute + NULL|self)
                CALL                     0

 627            STORE_FAST               5 (result)

 636            LOAD_GLOBAL             43 (list + NULL)
                LOAD_GLOBAL             45 (getattr + NULL)
                LOAD_FAST_BORROW         5 (result)
                LOAD_CONST               9 ('data')
                LOAD_CONST              10 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L8:     CALL                     1
        L9:     RETURN_VALUE

  --   L10:     PUSH_EXC_INFO

 622            LOAD_GLOBAL             20 (TypeError)
                LOAD_GLOBAL             22 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       20 (to L12)
                NOT_TAKEN
                POP_TOP

 623            LOAD_GLOBAL             16 (queries_mod)
                LOAD_ATTR               24 (DEFAULT_QUERY_LIMIT)
                STORE_FAST               3 (capped)
       L11:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 220 (to L6)

 622   L12:     RERAISE                  0

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L14:     PUSH_EXC_INFO

 637            LOAD_GLOBAL             46 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       59 (to L19)
                NOT_TAKEN
                STORE_FAST               6 (e)

 638   L15:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 639            LOAD_CONST              11 ('list_memory_review_events failed (non-critical) | memory_id=')

 640            LOAD_FAST                0 (memory_id)
                FORMAT_SIMPLE
                LOAD_CONST              12 (' | error_type=')
                LOAD_GLOBAL             49 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               50 (__name__)
                FORMAT_SIMPLE

 639            BUILD_STRING             4

 638            CALL                     1
                POP_TOP

 642            BUILD_LIST               0
       L16:     SWAP                     2
       L17:     POP_EXCEPT
                LOAD_CONST              10 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --   L18:     LOAD_CONST              10 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 637   L19:     RERAISE                  0

  --   L20:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L10 [0]
  L7 to L9 -> L14 [0]
  L10 to L11 -> L13 [1] lasti
  L12 to L13 -> L13 [1] lasti
  L14 to L15 -> L20 [1] lasti
  L15 to L16 -> L18 [1] lasti
  L16 to L17 -> L20 [1] lasti
  L18 to L20 -> L20 [1] lasti
```
