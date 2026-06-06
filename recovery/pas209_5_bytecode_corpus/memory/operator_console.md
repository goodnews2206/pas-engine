# memory/operator_console

- **pyc:** `app\services\memory\__pycache__\operator_console.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/operator_console.py`
- **co_filename (from bytecode):** `C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS147 — Operator memory review console.

Operator/admin-facing surface for inspecting and acting on memory
records. Wraps PAS144B (tenant-scoped reads) and PAS144C (audited
transition helpers) so the admin route stays small, never writes
directly to ``pas_memory_records``, and never echoes raw memory
content.

Hard contract:
  * **Tenant-scoped.** Every read and every mutation requires an
    explicit ``brokerage_id``. There is no path through this module
    that calls an unscoped helper.
  * **Audited mutations only.** ``review_memory_as_operator``
    dispatches to ``review.approve_memory`` /
    ``review.reject_memory`` / ``review.expire_memory_by_id`` /
    ``review.quarantine_memory_by_id``. Direct
    ``store.upsert_memory_record`` or Supabase calls are forbidden
    here — every mutation is recorded in
    ``pas_memory_review_events`` via the PAS144C audit table.
  * **Structural-only output.** Queue items are projected through a
    closed allow-list (``_SAFE_QUEUE_FIELDS``). Forbidden raw-payload
    keys — evidence, metadata, lineage, transcript, raw_text,
    raw_prompt, etc. — are NEVER surfaced to the operator UI.
  * **Length-capped text.** ``title`` and ``summary`` are short
    structural fields by PAS144A contract; the projection applies a
    defence-in-depth length cap so a regression upstream cannot
    spill long blobs.
  * **Fail-closed without raising.** A Supabase failure on the
    read path returns ``count=0`` with a warning token; a failure on
    the mutation path surfaces a structured ``{"status": "failed",
    "errors": [...]}`` response. Neither raises into the caller.

Public surface (deliberately small):
  - list_memory_review_queue_for_operator(brokerage_id, *,
        status="CANDIDATE", limit=50) -> dict
  - memory_review_summary_for_operator(brokerage_id) -> dict
  - review_memory_as_operator(memory_id, brokerage_id, action,
        operator_id, *, reason=None) -> dict
  - ALLOWED_ACTIONS                                 (frozenset)
  - OPERATOR_ACTOR_TYPE                             (str constant)
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.services.memory`, `logging`, `queries`, `review`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_limit`, `_coerce_status`, `_project_queue_item`, `_truncate`, `list_memory_review_queue_for_operator`, `memory_review_summary_for_operator`, `review_memory_as_operator`

## Env-key candidates

`CANDIDATE`, `OPERATOR`

## String constants (redacted where noted)

- '\nPAS147 — Operator memory review console.\n\nOperator/admin-facing surface for inspecting and acting on memory\nrecords. Wraps PAS144B (tenant-scoped reads) and PAS144C (audited\ntransition helpers) so the admin route stays small, never writes\ndirectly to ``pas_memory_records``, and never echoes raw memory\ncontent.\n\nHard contract:\n  * **Tenant-scoped.** Every read and every mutation requires an\n    explicit ``brokerage_id``. There is no path through this module\n    that calls an unscoped helper.\n  * **Audited mutations only.** ``review_memory_as_operator``\n    dispatches to ``review.approve_memory`` /\n    ``review.reject_memory`` / ``review.expire_memory_by_id`` /\n    ``review.quarantine_memory_by_id``. Direct\n    ``store.upsert_memory_record`` or Supabase calls are forbidden\n    here — every mutation is recorded in\n    ``pas_memory_review_events`` via the PAS144C audit table.\n  * **Structural-only output.** Queue items are projected through a\n    closed allow-list (``_SAFE_QUEUE_FIELDS``). Forbidden raw-payload\n    keys — evidence, metadata, lineage, transcript, raw_text,\n    raw_prompt, etc. — are NEVER surfaced to the operator UI.\n  * **Length-capped text.** ``title`` and ``summary`` are short\n    structural fields by PAS144A contract; the projection applies a\n    defence-in-depth length cap so a regression upstream cannot\n    spill long blobs.\n  * **Fail-closed without raising.** A Supabase failure on the\n    read path returns ``count=0`` with a warning token; a failure on\n    the mutation path surfaces a structured ``{"status": "failed",\n    "errors": [...]}`` response. Neither raises into the caller.\n\nPublic surface (deliberately small):\n  - list_memory_review_queue_for_operator(brokerage_id, *,\n        status="CANDIDATE", limit=50) -> dict\n  - memory_review_summary_for_operator(brokerage_id) -> dict\n  - review_memory_as_operator(memory_id, brokerage_id, action,\n        operator_id, *, reason=None) -> dict\n  - ALLOWED_ACTIONS                                 (frozenset)\n  - OPERATOR_ACTOR_TYPE                             (str constant)\n'
- 'pas.memory.operator_console'
- 'OPERATOR'
- 'approve'
- 'reject'
- 'expire'
- 'quarantine'
- 'CANDIDATE'
- 'status'
- 'limit'
- 'reason'
- 'value'
- 'Any'
- 'return'
- 'int'
- 'Coerce a caller-supplied limit; clamp to ``[1, MAX_QUEUE_LIMIT]``.'
- 'max_chars'
- 'Optional[str]'
- 'row'
- 'Optional[Dict[str, Any]]'
- 'Project a memory row through the closed safe-field allow-list.\n\nReturns ``None`` for malformed input (non-dict, missing memory_id).\nForbidden keys (evidence / metadata / lineage / transcript /\nraw_text / messages / utterances / raw_prompt / injected_prompt)\ncannot enter the output because only ``_SAFE_QUEUE_FIELDS`` are\ncopied in.\n'
- 'memory_id'
- 'title'
- 'summary'
- "Normalise a caller-supplied status string. Returns None on\nmalformed input — callers treat None as 'no status filter'."
- 'brokerage_id'
- 'str'
- 'Dict[str, Any]'
- 'Return the memory review queue for a tenant, tenant-scoped.\n\nBehaviour:\n  * ``brokerage_id`` is REQUIRED. Missing / non-string / empty\n    returns ``{"status": "failed", "errors": ["missing_brokerage_id"]}``.\n  * ``status`` defaults to CANDIDATE. Unknown statuses are\n    treated as "no filter" with a warning token.\n  * ``limit`` is clamped to ``MAX_QUEUE_LIMIT``.\n\nResponse shape (success):\n    {\n        "status":       "ok",\n        "brokerage_id": "<id>",\n        "status_filter": "CANDIDATE" | None,\n        "count":        <int>,\n        "items":        [<projected queue item>, ...],\n        "warnings":     [<str>, ...],\n    }\n\nNever raises. A Supabase failure returns ``status="ok"``,\n``count=0``, ``items=[]``, and a warning token in ``warnings``.\n'
- 'failed'
- 'errors'
- 'missing_brokerage_id'
- 'unknown_status_ignored:'
- 'operator_console queue reader failed (non-critical) | brokerage='
- ' | error_type='
- 'status_filter'
- 'count'
- 'items'
- 'warnings'
- 'reader_failed'
- 'unexpected_reader_shape'
- 'result_truncated_at_limit'
- 'Counts of memory records by status for one tenant.\n\nReads the recent slice (capped at ``MAX_QUEUE_LIMIT``) and groups\nby status client-side. Returns:\n\n    {\n        "status":       "ok",\n        "brokerage_id": "<id>",\n        "counts":       {"CANDIDATE": N, "APPROVED": N, ...},\n        "total":        <int>,\n        "warnings":     [<str>, ...],\n    }\n\nEvery closed-status key (CANDIDATE / APPROVED / QUARANTINED /\nEXPIRED / REJECTED) is always present in ``counts`` so the\ndownstream UI can rely on the schema regardless of the input.\n'
- 'operator_console summary reader failed (non-critical) | brokerage='
- 'counts'
- 'total'
- 'unknown_status_in_row:'
- 'action'
- 'operator_id'
- 'Apply an audited memory transition as an operator.\n\nDispatches to one of the four PAS144C review helpers:\n  * ``approve``    → ``review.approve_memory``\n  * ``reject``     → ``review.reject_memory``\n  * ``expire``     → ``review.expire_memory_by_id``\n  * ``quarantine`` → ``review.quarantine_memory_by_id``\n\nEvery call uses ``actor_type=OPERATOR`` and forwards\n``operator_id`` as ``actor_id``. The mutation is recorded in\n``pas_memory_review_events`` by the PAS144C helper.\n\nReturns the structured response from the underlying helper:\n  * Success      → ``{"status": "ok", "memory_id": ..., ...}``\n  * Warning      → ``{"status": "warning", "warnings": [...], ...}``\n  * Failure      → ``{"status": "failed", "errors": [...], ...}``\n\nHard input checks:\n  * ``memory_id`` non-empty string.\n  * ``brokerage_id`` non-empty string (tenant scope).\n  * ``operator_id`` non-empty string (audit trail).\n  * ``action`` ∈ ``ALLOWED_ACTIONS``.\n\nNever raises. Caller-bugs surface as ``status="failed"``.\n'
- 'missing_memory_id'
- 'missing_operator_id'
- 'invalid_action:'
- 'review_helper_import_failed:'
- 'review_helper_exception:'
- 'unexpected_review_helper_shape'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS147 — Operator memory review console.\n\nOperator/admin-facing surface for inspecting and acting on memory\nrecords. Wraps PAS144B (tenant-scoped reads) and PAS144C (audited\ntransition helpers) so the admin route stays small, never writes\ndirectly to ``pas_memory_records``, and never echoes raw memory\ncontent.\n\nHard contract:\n  * **Tenant-scoped.** Every read and every mutation requires an\n    explicit ``brokerage_id``. There is no path through this module\n    that calls an unscoped helper.\n  * **Audited mutations only.** ``review_memory_as_operator``\n    dispatches to ``review.approve_memory`` /\n    ``review.reject_memory`` / ``review.expire_memory_by_id`` /\n    ``review.quarantine_memory_by_id``. Direct\n    ``store.upsert_memory_record`` or Supabase calls are forbidden\n    here — every mutation is recorded in\n    ``pas_memory_review_events`` via the PAS144C audit table.\n  * **Structural-only output.** Queue items are projected through a\n    closed allow-list (``_SAFE_QUEUE_FIELDS``). Forbidden raw-payload\n    keys — evidence, metadata, lineage, transcript, raw_text,\n    raw_prompt, etc. — are NEVER surfaced to the operator UI.\n  * **Length-capped text.** ``title`` and ``summary`` are short\n    structural fields by PAS144A contract; the projection applies a\n    defence-in-depth length cap so a regression upstream cannot\n    spill long blobs.\n  * **Fail-closed without raising.** A Supabase failure on the\n    read path returns ``count=0`` with a warning token; a failure on\n    the mutation path surfaces a structured ``{"status": "failed",\n    "errors": [...]}`` response. Neither raises into the caller.\n\nPublic surface (deliberately small):\n  - list_memory_review_queue_for_operator(brokerage_id, *,\n        status="CANDIDATE", limit=50) -> dict\n  - memory_review_summary_for_operator(brokerage_id) -> dict\n  - review_memory_as_operator(memory_id, brokerage_id, action,\n        operator_id, *, reason=None) -> dict\n  - ALLOWED_ACTIONS                                 (frozenset)\n  - OPERATOR_ACTOR_TYPE                             (str constant)\n')
              STORE_NAME               0 (__doc__)

 44           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 46           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 47           LOAD_SMALL_INT           0
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

 49           LOAD_NAME                3 (logging)
              LOAD_ATTR               18 (getLogger)
              PUSH_NULL
              LOAD_CONST               4 ('pas.memory.operator_console')
              CALL                     1
              STORE_NAME              10 (logger)

 60           LOAD_CONST               5 ('OPERATOR')
              STORE_NAME              11 (OPERATOR_ACTOR_TYPE)

 64           LOAD_CONST               6 ('approve')
              STORE_NAME              12 (ACTION_APPROVE)

 65           LOAD_CONST               7 ('reject')
              STORE_NAME              13 (ACTION_REJECT)

 66           LOAD_CONST               8 ('expire')
              STORE_NAME              14 (ACTION_EXPIRE)

 67           LOAD_CONST               9 ('quarantine')
              STORE_NAME              15 (ACTION_QUARANTINE)

 69           LOAD_NAME               16 (frozenset)
              PUSH_NULL

 70           LOAD_NAME               12 (ACTION_APPROVE)

 71           LOAD_NAME               13 (ACTION_REJECT)

 72           LOAD_NAME               14 (ACTION_EXPIRE)

 73           LOAD_NAME               15 (ACTION_QUARANTINE)

 69           BUILD_SET                4
              CALL                     1
              STORE_NAME              17 (ALLOWED_ACTIONS)

 79           LOAD_CONST              29 (('CANDIDATE', 'APPROVED', 'QUARANTINED', 'EXPIRED', 'REJECTED'))
              STORE_NAME              18 (_KNOWN_STATUSES)

 85           LOAD_CONST              30 (('memory_id', 'brokerage_id', 'kind', 'source', 'status', 'title', 'summary', 'confidence', 'outcome_weight', 'created_at', 'expires_at'))
              STORE_NAME              19 (_SAFE_QUEUE_FIELDS)

103           LOAD_SMALL_INT         200
              STORE_NAME              20 (_TITLE_MAX_CHARS)

104           LOAD_CONST              12 (400)
              STORE_NAME              21 (_SUMMARY_MAX_CHARS)

108           LOAD_SMALL_INT          50
              STORE_NAME              22 (DEFAULT_QUEUE_LIMIT)

109           LOAD_SMALL_INT         200
              STORE_NAME              23 (MAX_QUEUE_LIMIT)

116           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA34B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 116>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object _clamp_limit at 0x0000018C17FF10B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 116>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_clamp_limit)

129           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18025730, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 129>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _truncate at 0x0000018C1800AD80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 129>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_truncate)

141           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA2B50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 141>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _project_queue_item at 0x0000018C17D77E00, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 141>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_project_queue_item)

170           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA3870, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 170>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _coerce_status at 0x0000018C17FF13B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 170>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_coerce_status)

190           LOAD_CONST              11 ('status')

193           LOAD_CONST              10 ('CANDIDATE')

190           LOAD_CONST              21 ('limit')

194           LOAD_NAME               22 (DEFAULT_QUEUE_LIMIT)

190           BUILD_MAP                2
              LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18025E30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 190>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object list_memory_review_queue_for_operator at 0x0000018C17EA7750, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 190>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              28 (list_memory_review_queue_for_operator)

286           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA2E20, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 286>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object memory_review_summary_for_operator at 0x0000018C17E92A10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 286>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (memory_review_summary_for_operator)

370           LOAD_CONST              26 ('reason')

376           LOAD_CONST               2 (None)

370           BUILD_MAP                1
              LOAD_CONST              27 (<code object __annotate__ at 0x0000018C18025830, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 370>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object review_memory_as_operator at 0x0000018C17D51FD0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 370>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              30 (review_memory_as_operator)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 116>:
116           RESUME                   0
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

Disassembly of <code object _clamp_limit at 0x0000018C17FF10B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 116>:
 116           RESUME                   0

 118           LOAD_FAST_BORROW         0 (value)
               POP_JUMP_IF_NOT_NONE     7 (to L1)
               NOT_TAKEN

 119           LOAD_GLOBAL              0 (DEFAULT_QUEUE_LIMIT)
               RETURN_VALUE

 120   L1:     NOP

 121   L2:     LOAD_GLOBAL              3 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (n)

 124   L3:     LOAD_FAST                1 (n)
               LOAD_SMALL_INT           0
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 125           LOAD_GLOBAL              0 (DEFAULT_QUEUE_LIMIT)
               RETURN_VALUE

 126   L4:     LOAD_GLOBAL              9 (min + NULL)
               LOAD_FAST                1 (n)
               LOAD_GLOBAL             10 (MAX_QUEUE_LIMIT)
               CALL                     2
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 122           LOAD_GLOBAL              4 (TypeError)
               LOAD_GLOBAL              6 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

 123           LOAD_GLOBAL              0 (DEFAULT_QUEUE_LIMIT)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 122   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 129>:
129           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('max_chars')
              LOAD_CONST               4 ('int')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Optional[str]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _truncate at 0x0000018C1800AD80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 129>:
 129            RESUME                   0

 130            LOAD_FAST_BORROW         0 (value)
                POP_JUMP_IF_NOT_NONE     3 (to L1)
                NOT_TAKEN

 131            LOAD_CONST               0 (None)
                RETURN_VALUE

 132    L1:     NOP

 133    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_FAST                0 (value)
                JUMP_FORWARD            10 (to L4)
        L3:     LOAD_GLOBAL              3 (str + NULL)
                LOAD_FAST_BORROW         0 (value)
                CALL                     1
        L4:     STORE_FAST               2 (s)

 136    L5:     LOAD_FAST                2 (s)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN

 137            LOAD_CONST               1 ('')
                RETURN_VALUE

 138    L6:     LOAD_GLOBAL              7 (len + NULL)
                LOAD_FAST                2 (s)
                CALL                     1
                LOAD_FAST                1 (max_chars)
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN
                LOAD_FAST                2 (s)
                RETURN_VALUE
        L7:     LOAD_FAST                2 (s)
                LOAD_CONST               0 (None)
                LOAD_FAST                1 (max_chars)
                BINARY_SLICE
                RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

 134            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L10)
                NOT_TAKEN
                POP_TOP

 135    L9:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 134   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L5 -> L8 [0]
  L8 to L9 -> L11 [1] lasti
  L10 to L11 -> L11 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 141>:
141           RESUME                   0
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

Disassembly of <code object _project_queue_item at 0x0000018C17D77E00, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 141>:
141           RESUME                   0

150           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

151           LOAD_CONST               1 (None)
              RETURN_VALUE

152   L1:     LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('memory_id')
              CALL                     1
              STORE_FAST               1 (memory_id)

153           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (memory_id)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (memory_id)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

154   L2:     LOAD_CONST               1 (None)
              RETURN_VALUE

156   L3:     BUILD_MAP                0
              STORE_FAST               2 (out)

157           LOAD_GLOBAL             10 (_SAFE_QUEUE_FIELDS)
              GET_ITER
      L4:     FOR_ITER                77 (to L8)
              STORE_FAST               3 (key)

158           LOAD_FAST_BORROW_LOAD_FAST_BORROW 48 (key, row)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN

159           JUMP_BACKWARD           11 (to L4)

160   L5:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 3 (row, key)
              BINARY_OP               26 ([])
              STORE_FAST               4 (val)

161           LOAD_FAST_BORROW         3 (key)
              LOAD_CONST               3 ('title')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       21 (to L6)
              NOT_TAKEN

162           LOAD_GLOBAL             13 (_truncate + NULL)
              LOAD_FAST_BORROW         4 (val)
              LOAD_GLOBAL             14 (_TITLE_MAX_CHARS)
              CALL                     2
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (out, key)
              STORE_SUBSCR
              JUMP_BACKWARD           46 (to L4)

163   L6:     LOAD_FAST_BORROW         3 (key)
              LOAD_CONST               4 ('summary')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       21 (to L7)
              NOT_TAKEN

164           LOAD_GLOBAL             13 (_truncate + NULL)
              LOAD_FAST_BORROW         4 (val)
              LOAD_GLOBAL             16 (_SUMMARY_MAX_CHARS)
              CALL                     2
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (out, key)
              STORE_SUBSCR
              JUMP_BACKWARD           73 (to L4)

166   L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (val, out)
              LOAD_FAST_BORROW         3 (key)
              STORE_SUBSCR
              JUMP_BACKWARD           79 (to L4)

157   L8:     END_FOR
              POP_ITER

167           LOAD_FAST_BORROW         2 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 170>:
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

Disassembly of <code object _coerce_status at 0x0000018C17FF13B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 170>:
170           RESUME                   0

173           LOAD_FAST_BORROW         0 (value)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

174           LOAD_CONST               1 (None)
              RETURN_VALUE

175   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

176           LOAD_CONST               1 (None)
              RETURN_VALUE

177   L2:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

178           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

179           LOAD_CONST               1 (None)
              RETURN_VALUE

180   L3:     LOAD_FAST_BORROW         1 (s)
              LOAD_ATTR                7 (upper + NULL|self)
              CALL                     0
              STORE_FAST               2 (upper)

181           LOAD_FAST_BORROW         2 (upper)
              LOAD_GLOBAL              8 (_KNOWN_STATUSES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN

182           LOAD_CONST               1 (None)
              RETURN_VALUE

183   L4:     LOAD_FAST_BORROW         2 (upper)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 190>:
190           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

191           LOAD_CONST               2 ('str')

190           LOAD_CONST               3 ('status')

193           LOAD_CONST               2 ('str')

190           LOAD_CONST               4 ('limit')

194           LOAD_CONST               5 ('int')

190           LOAD_CONST               6 ('return')

195           LOAD_CONST               7 ('Dict[str, Any]')

190           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object list_memory_review_queue_for_operator at 0x0000018C17EA7750, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 190>:
 190            RESUME                   0

 218            LOAD_GLOBAL              1 (isinstance + NULL)
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
                POP_JUMP_IF_TRUE         8 (to L2)
                NOT_TAKEN

 220    L1:     LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 221            LOAD_CONST               3 ('errors')
                LOAD_CONST               4 ('missing_brokerage_id')
                BUILD_LIST               1

 219            BUILD_MAP                2
                RETURN_VALUE

 223    L2:     LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               0 (brokerage_id)

 225            BUILD_LIST               0
                STORE_FAST               3 (warnings)

 226            LOAD_GLOBAL              7 (_coerce_status + NULL)
                LOAD_FAST_BORROW         1 (status)
                CALL                     1
                STORE_FAST               4 (status_filter)

 227            LOAD_FAST_BORROW         1 (status)
                POP_JUMP_IF_NONE        26 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (status_filter)
                POP_JUMP_IF_NOT_NONE    22 (to L3)
                NOT_TAKEN

 228            LOAD_FAST_BORROW         3 (warnings)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST               6 ('unknown_status_ignored:')
                LOAD_FAST_BORROW         1 (status)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 230    L3:     LOAD_GLOBAL             11 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1
                STORE_FAST               5 (capped)

 234            NOP

 235    L4:     LOAD_SMALL_INT           0
                LOAD_CONST               7 (('queries',))
                IMPORT_NAME              6 (app.services.memory)
                IMPORT_FROM              7 (queries)
                STORE_FAST               6 (queries_mod)
                POP_TOP

 236            LOAD_FAST_BORROW         6 (queries_mod)
                LOAD_ATTR               17 (list_memory_for_brokerage + NULL|self)

 237            LOAD_FAST_BORROW_LOAD_FAST_BORROW 4 (brokerage_id, status_filter)
                LOAD_FAST_BORROW         5 (capped)

 236            LOAD_CONST               8 (('status', 'limit'))
                CALL_KW                  3
                STORE_FAST               7 (rows)

 253    L5:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST                7 (rows)
                LOAD_GLOBAL             28 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L6)
                NOT_TAKEN

 255            LOAD_CONST               1 ('status')
                LOAD_CONST              11 ('ok')

 256            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST                0 (brokerage_id)

 257            LOAD_CONST              13 ('status_filter')
                LOAD_FAST                4 (status_filter)

 258            LOAD_CONST              14 ('count')
                LOAD_SMALL_INT           0

 259            LOAD_CONST              15 ('items')
                BUILD_LIST               0

 260            LOAD_CONST              16 ('warnings')
                LOAD_FAST                3 (warnings)
                LOAD_CONST              18 ('unexpected_reader_shape')
                BUILD_LIST               1
                BINARY_OP                0 (+)

 254            BUILD_MAP                6
                RETURN_VALUE

 263    L6:     BUILD_LIST               0
                STORE_FAST               9 (items)

 264            LOAD_FAST                7 (rows)
                GET_ITER
        L7:     FOR_ITER                37 (to L9)
                STORE_FAST              10 (row)

 265            LOAD_GLOBAL             31 (_project_queue_item + NULL)
                LOAD_FAST               10 (row)
                CALL                     1
                STORE_FAST              11 (proj)

 266            LOAD_FAST               11 (proj)
                POP_JUMP_IF_NOT_NONE     3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           20 (to L7)

 267    L8:     LOAD_FAST                9 (items)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_FAST               11 (proj)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           39 (to L7)

 264    L9:     END_FOR
                POP_ITER

 269            LOAD_GLOBAL             33 (len + NULL)
                LOAD_FAST                9 (items)
                CALL                     1
                LOAD_FAST                5 (capped)
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       18 (to L10)
                NOT_TAKEN

 270            LOAD_FAST                3 (warnings)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST              19 ('result_truncated_at_limit')
                CALL                     1
                POP_TOP

 273   L10:     LOAD_CONST               1 ('status')
                LOAD_CONST              11 ('ok')

 274            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST                0 (brokerage_id)

 275            LOAD_CONST              13 ('status_filter')
                LOAD_FAST                4 (status_filter)

 276            LOAD_CONST              14 ('count')
                LOAD_GLOBAL             33 (len + NULL)
                LOAD_FAST                9 (items)
                CALL                     1

 277            LOAD_CONST              15 ('items')
                LOAD_FAST                9 (items)

 278            LOAD_CONST              16 ('warnings')
                LOAD_FAST                3 (warnings)

 272            BUILD_MAP                6
                RETURN_VALUE

  --   L11:     PUSH_EXC_INFO

 239            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       79 (to L16)
                NOT_TAKEN
                STORE_FAST               8 (e)

 240   L12:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 241            LOAD_CONST               9 ('operator_console queue reader failed (non-critical) | brokerage=')

 242            LOAD_FAST                0 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST              10 (' | error_type=')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE

 241            BUILD_STRING             4

 240            CALL                     1
                POP_TOP

 245            LOAD_CONST               1 ('status')
                LOAD_CONST              11 ('ok')

 246            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST                0 (brokerage_id)

 247            LOAD_CONST              13 ('status_filter')
                LOAD_FAST                4 (status_filter)

 248            LOAD_CONST              14 ('count')
                LOAD_SMALL_INT           0

 249            LOAD_CONST              15 ('items')
                BUILD_LIST               0

 250            LOAD_CONST              16 ('warnings')
                LOAD_FAST                3 (warnings)
                LOAD_CONST              17 ('reader_failed')
                BUILD_LIST               1
                BINARY_OP                0 (+)

 244            BUILD_MAP                6
       L13:     SWAP                     2
       L14:     POP_EXCEPT
                LOAD_CONST               5 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RETURN_VALUE

  --   L15:     LOAD_CONST               5 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 239   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L11 [0]
  L11 to L12 -> L17 [1] lasti
  L12 to L13 -> L15 [1] lasti
  L13 to L14 -> L17 [1] lasti
  L15 to L17 -> L17 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 286>:
286           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

287           LOAD_CONST               2 ('str')

286           LOAD_CONST               3 ('return')

288           LOAD_CONST               4 ('Dict[str, Any]')

286           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object memory_review_summary_for_operator at 0x0000018C17E92A10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 286>:
 286            RESUME                   0

 306            LOAD_GLOBAL              1 (isinstance + NULL)
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
                POP_JUMP_IF_TRUE         8 (to L2)
                NOT_TAKEN

 308    L1:     LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 309            LOAD_CONST               3 ('errors')
                LOAD_CONST               4 ('missing_brokerage_id')
                BUILD_LIST               1

 307            BUILD_MAP                2
                RETURN_VALUE

 311    L2:     LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               0 (brokerage_id)

 313            LOAD_GLOBAL              6 (_KNOWN_STATUSES)
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (s)
                SWAP                     2
        L3:     BUILD_MAP                0
                SWAP                     2
        L4:     FOR_ITER                 5 (to L5)
                STORE_FAST_LOAD_FAST    17 (s, s)
                LOAD_SMALL_INT           0
                MAP_ADD                  2
                JUMP_BACKWARD            7 (to L4)
        L5:     END_FOR
                POP_ITER
        L6:     STORE_FAST               2 (counts)
                STORE_FAST               1 (s)

 314            BUILD_LIST               0
                STORE_FAST               3 (warnings)

 316            NOP

 317    L7:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('queries',))
                IMPORT_NAME              4 (app.services.memory)
                IMPORT_FROM              5 (queries)
                STORE_FAST               4 (queries_mod)
                POP_TOP

 318            LOAD_FAST_BORROW         4 (queries_mod)
                LOAD_ATTR               13 (list_memory_for_brokerage + NULL|self)

 319            LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_CONST               6 (None)
                LOAD_GLOBAL             14 (MAX_QUEUE_LIMIT)

 318            LOAD_CONST               7 (('status', 'limit'))
                CALL_KW                  3
                STORE_FAST               5 (rows)

 334    L8:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST                5 (rows)
                LOAD_GLOBAL             26 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L9)
                NOT_TAKEN

 336            LOAD_CONST               1 ('status')
                LOAD_CONST              10 ('ok')

 337            LOAD_CONST              11 ('brokerage_id')
                LOAD_FAST                0 (brokerage_id)

 338            LOAD_CONST              12 ('counts')
                LOAD_FAST                2 (counts)

 339            LOAD_CONST              13 ('total')
                LOAD_SMALL_INT           0

 340            LOAD_CONST              14 ('warnings')
                LOAD_CONST              16 ('unexpected_reader_shape')
                BUILD_LIST               1

 335            BUILD_MAP                5
                RETURN_VALUE

 343    L9:     LOAD_SMALL_INT           0
                STORE_FAST               7 (total)

 344            LOAD_FAST                5 (rows)
                GET_ITER
       L10:     FOR_ITER               124 (to L13)
                STORE_FAST               8 (row)

 345            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST                8 (row)
                LOAD_GLOBAL             28 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN

 346            JUMP_BACKWARD           27 (to L10)

 347   L11:     LOAD_FAST                8 (row)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               1 ('status')
                CALL                     1
                STORE_FAST               1 (s)

 348            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST                1 (s)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       38 (to L12)
                NOT_TAKEN
                LOAD_FAST_LOAD_FAST     18 (s, counts)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       32 (to L12)
                NOT_TAKEN

 349            LOAD_FAST_LOAD_FAST     33 (counts, s)
                COPY                     2
                COPY                     2
                BINARY_OP               26 ([])
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                SWAP                     3
                SWAP                     2
                STORE_SUBSCR

 350            LOAD_FAST                7 (total)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               7 (total)
                JUMP_BACKWARD          103 (to L10)

 352   L12:     LOAD_FAST                3 (warnings)
                LOAD_ATTR               33 (append + NULL|self)
                LOAD_CONST              17 ('unknown_status_in_row:')
                LOAD_FAST                1 (s)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          126 (to L10)

 344   L13:     END_FOR
                POP_ITER

 354            LOAD_GLOBAL             35 (len + NULL)
                LOAD_FAST                5 (rows)
                CALL                     1
                LOAD_GLOBAL             14 (MAX_QUEUE_LIMIT)
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       18 (to L14)
                NOT_TAKEN

 355            LOAD_FAST                3 (warnings)
                LOAD_ATTR               33 (append + NULL|self)
                LOAD_CONST              18 ('result_truncated_at_limit')
                CALL                     1
                POP_TOP

 358   L14:     LOAD_CONST               1 ('status')
                LOAD_CONST              10 ('ok')

 359            LOAD_CONST              11 ('brokerage_id')
                LOAD_FAST                0 (brokerage_id)

 360            LOAD_CONST              12 ('counts')
                LOAD_FAST                2 (counts)

 361            LOAD_CONST              13 ('total')
                LOAD_FAST                7 (total)

 362            LOAD_CONST              14 ('warnings')
                LOAD_FAST                3 (warnings)

 357            BUILD_MAP                5
                RETURN_VALUE

  --   L15:     SWAP                     2
                POP_TOP

 313            SWAP                     2
                STORE_FAST               1 (s)
                RERAISE                  0

  --   L16:     PUSH_EXC_INFO

 321            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       70 (to L21)
                NOT_TAKEN
                STORE_FAST               6 (e)

 322   L17:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 323            LOAD_CONST               8 ('operator_console summary reader failed (non-critical) | brokerage=')

 324            LOAD_FAST                0 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST               9 (' | error_type=')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE

 323            BUILD_STRING             4

 322            CALL                     1
                POP_TOP

 327            LOAD_CONST               1 ('status')
                LOAD_CONST              10 ('ok')

 328            LOAD_CONST              11 ('brokerage_id')
                LOAD_FAST                0 (brokerage_id)

 329            LOAD_CONST              12 ('counts')
                LOAD_FAST                2 (counts)

 330            LOAD_CONST              13 ('total')
                LOAD_SMALL_INT           0

 331            LOAD_CONST              14 ('warnings')
                LOAD_CONST              15 ('reader_failed')
                BUILD_LIST               1

 326            BUILD_MAP                5
       L18:     SWAP                     2
       L19:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --   L20:     LOAD_CONST               6 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 321   L21:     RERAISE                  0

  --   L22:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L6 -> L15 [2]
  L7 to L8 -> L16 [0]
  L16 to L17 -> L22 [1] lasti
  L17 to L18 -> L20 [1] lasti
  L18 to L19 -> L22 [1] lasti
  L20 to L22 -> L22 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025830, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 370>:
370           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('memory_id')

371           LOAD_CONST               2 ('str')

370           LOAD_CONST               3 ('brokerage_id')

372           LOAD_CONST               2 ('str')

370           LOAD_CONST               4 ('action')

373           LOAD_CONST               2 ('str')

370           LOAD_CONST               5 ('operator_id')

374           LOAD_CONST               2 ('str')

370           LOAD_CONST               6 ('reason')

376           LOAD_CONST               7 ('Optional[str]')

370           LOAD_CONST               8 ('return')

377           LOAD_CONST               9 ('Dict[str, Any]')

370           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object review_memory_as_operator at 0x0000018C17D51FD0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\operator_console.py", line 370>:
 370            RESUME                   0

 403            BUILD_LIST               0
                STORE_FAST               5 (errors)

 404            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (memory_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (memory_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L2)
                NOT_TAKEN

 405    L1:     LOAD_FAST_BORROW         5 (errors)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_CONST               1 ('missing_memory_id')
                CALL                     1
                POP_TOP

 406    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L4)
                NOT_TAKEN

 407    L3:     LOAD_FAST_BORROW         5 (errors)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_CONST               2 ('missing_brokerage_id')
                CALL                     1
                POP_TOP

 408    L4:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (operator_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (operator_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L6)
                NOT_TAKEN

 409    L5:     LOAD_FAST_BORROW         5 (errors)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_CONST               3 ('missing_operator_id')
                CALL                     1
                POP_TOP

 410    L6:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (action)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       40 (to L7)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (action)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                LOAD_GLOBAL             10 (ALLOWED_ACTIONS)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       22 (to L8)
                NOT_TAKEN

 411    L7:     LOAD_FAST_BORROW         5 (errors)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_CONST               4 ('invalid_action:')
                LOAD_FAST_BORROW         2 (action)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 413    L8:     LOAD_FAST_BORROW         5 (errors)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L9)
                NOT_TAKEN

 415            LOAD_CONST               5 ('status')
                LOAD_CONST               6 ('failed')

 416            LOAD_CONST               7 ('errors')
                LOAD_FAST_BORROW         5 (errors)

 414            BUILD_MAP                2
                RETURN_VALUE

 419    L9:     LOAD_FAST                0 (memory_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               0 (memory_id)

 420            LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               1 (brokerage_id)

 421            LOAD_FAST_BORROW         3 (operator_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               3 (operator_id)

 422            LOAD_FAST_BORROW         2 (action)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               2 (action)

 426            NOP

 427   L10:     LOAD_SMALL_INT           0
                LOAD_CONST               8 (('review',))
                IMPORT_NAME              6 (app.services.memory)
                IMPORT_FROM              7 (review)
                STORE_FAST               6 (review_mod)
                POP_TOP

 435   L11:     LOAD_GLOBAL             22 (ACTION_APPROVE)
                LOAD_FAST                6 (review_mod)
                LOAD_ATTR               24 (approve_memory)

 436            LOAD_GLOBAL             26 (ACTION_REJECT)
                LOAD_FAST                6 (review_mod)
                LOAD_ATTR               28 (reject_memory)

 437            LOAD_GLOBAL             30 (ACTION_EXPIRE)
                LOAD_FAST                6 (review_mod)
                LOAD_ATTR               32 (expire_memory_by_id)

 438            LOAD_GLOBAL             34 (ACTION_QUARANTINE)
                LOAD_FAST                6 (review_mod)
                LOAD_ATTR               36 (quarantine_memory_by_id)

 434            BUILD_MAP                4

 439            LOAD_FAST                2 (action)

 434            BINARY_OP               26 ([])
                STORE_FAST               8 (helper)

 441            NOP

 442   L12:     LOAD_FAST                8 (helper)
                PUSH_NULL

 443            LOAD_FAST                0 (memory_id)

 444            LOAD_FAST                1 (brokerage_id)

 445            LOAD_GLOBAL             38 (OPERATOR_ACTOR_TYPE)

 446            LOAD_FAST                3 (operator_id)

 447            LOAD_FAST                4 (reason)

 442            LOAD_CONST              11 (('actor_type', 'actor_id', 'reason'))
                CALL_KW                  5
                STORE_FAST               9 (result)

 457   L13:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST                9 (result)
                LOAD_GLOBAL             40 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         8 (to L14)
                NOT_TAKEN

 459            LOAD_CONST               5 ('status')
                LOAD_CONST               6 ('failed')

 460            LOAD_CONST               7 ('errors')
                LOAD_CONST              13 ('unexpected_review_helper_shape')
                BUILD_LIST               1

 458            BUILD_MAP                2
                RETURN_VALUE

 462   L14:     LOAD_FAST                9 (result)
                RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 428            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       40 (to L20)
                NOT_TAKEN
                STORE_FAST               7 (e)

 430   L16:     LOAD_CONST               5 ('status')
                LOAD_CONST               6 ('failed')

 431            LOAD_CONST               7 ('errors')
                LOAD_CONST               9 ('review_helper_import_failed:')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 429            BUILD_MAP                2
       L17:     SWAP                     2
       L18:     POP_EXCEPT
                LOAD_CONST              10 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L19:     LOAD_CONST              10 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 428   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L22:     PUSH_EXC_INFO

 449            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       40 (to L27)
                NOT_TAKEN
                STORE_FAST               7 (e)

 453   L23:     LOAD_CONST               5 ('status')
                LOAD_CONST               6 ('failed')

 454            LOAD_CONST               7 ('errors')
                LOAD_CONST              12 ('review_helper_exception:')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 452            BUILD_MAP                2
       L24:     SWAP                     2
       L25:     POP_EXCEPT
                LOAD_CONST              10 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L26:     LOAD_CONST              10 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 449   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L10 to L11 -> L15 [0]
  L12 to L13 -> L22 [0]
  L15 to L16 -> L21 [1] lasti
  L16 to L17 -> L19 [1] lasti
  L17 to L18 -> L21 [1] lasti
  L19 to L21 -> L21 [1] lasti
  L22 to L23 -> L28 [1] lasti
  L23 to L24 -> L26 [1] lasti
  L24 to L25 -> L28 [1] lasti
  L26 to L28 -> L28 [1] lasti
```
