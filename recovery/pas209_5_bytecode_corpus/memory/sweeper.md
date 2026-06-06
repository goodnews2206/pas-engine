# memory/sweeper

- **pyc:** `app\services\memory\__pycache__\sweeper.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/sweeper.py`
- **co_filename (from bytecode):** `app\services\memory\sweeper.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144D — Memory expiration sweep.

System utility that walks ``pas_memory_records`` for a single tenant,
finds rows whose ``expires_at`` has lapsed, and transitions them to
EXPIRED via the audited PAS144C ``review.expire_memory_by_id`` path.

Hard contract — every public helper in this module:

  1. Requires ``brokerage_id`` (tenant isolation, mandatory). There is
     no unscoped sweep helper; an operator who wants to sweep every
     tenant runs the CLI once per ``--brokerage-id``.
  2. Only considers rows whose status is one of
     ``APPROVED`` / ``CANDIDATE`` / ``OPERATIONAL``.  In the current
     schema "OPERATIONAL" is a *kind*, not a status — but PAS144A's
     status set was deliberately conservative, so we accept the status
     here defensively in case a downstream caller (or a future
     migration) introduces it. Records in any of those states with an
     ``expires_at <= now`` are eligible for expiration.
  3. NEVER expires a ``kind == COMPLIANCE`` record. Regulatory facts
     do not decay on a TTL clock; operator removal is the only path.
     (``contracts.DEFAULT_TTL_DAYS[COMPLIANCE]`` is ``None`` precisely
     for this reason; the guard here is belt-and-suspenders in case a
     legacy row carries a non-null ``expires_at``.)
  4. Uses ``review.expire_memory_by_id`` for the transition so the
     audit trail in ``pas_memory_review_events`` is preserved. We do
     NOT patch the records table directly.
  5. Returns a structured report dict — never raises into the caller.
     A Supabase failure during the find phase produces an empty
     ``results`` list and a warning entry.

Report shape (stable, machine-readable):

    {
        "brokerage_id": "<tenant>",
        "checked":      <int>,          # candidates considered
        "expired":      <int>,          # successful EXPIRED transitions
        "failed":       <int>,          # transitions that did not succeed
        "results":      [
            {
                "memory_id":  "...",
                "kind":       "...",
                "status":     "ok" | "warning" | "failed",
                "from_status": "...",
                "to_status":   "EXPIRED" | None,
                "review_id":   "..."   # present on ok/warning
            },
            ...
        ],
        "warnings":     ["..."],        # non-fatal notes (e.g. supabase_unavailable)
    }

PAS144D explicitly does NOT build:
  * cross-tenant batch sweep
  * scheduling / cron daemon
  * retrieval / similarity search
  * embeddings / vector helpers
  * autonomous learning loops
  * any auto-approval path
```

## Imports

``, `Any`, `Dict`, `List`, `MemoryKind`, `MemoryStatus`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `contracts`, `datetime`, `get_supabase`, `logging`, `queries`, `review`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_limit`, `_get_db`, `_is_compliance_kind`, `_parse_expires_at`, `_resolve_now`, `expire_due_memory`, `find_expired_memory`

## Env-key candidates

`OPERATIONAL`, `SYSTEM`

## String constants (redacted where noted)

- '\nPAS144D — Memory expiration sweep.\n\nSystem utility that walks ``pas_memory_records`` for a single tenant,\nfinds rows whose ``expires_at`` has lapsed, and transitions them to\nEXPIRED via the audited PAS144C ``review.expire_memory_by_id`` path.\n\nHard contract — every public helper in this module:\n\n  1. Requires ``brokerage_id`` (tenant isolation, mandatory). There is\n     no unscoped sweep helper; an operator who wants to sweep every\n     tenant runs the CLI once per ``--brokerage-id``.\n  2. Only considers rows whose status is one of\n     ``APPROVED`` / ``CANDIDATE`` / ``OPERATIONAL``.  In the current\n     schema "OPERATIONAL" is a *kind*, not a status — but PAS144A\'s\n     status set was deliberately conservative, so we accept the status\n     here defensively in case a downstream caller (or a future\n     migration) introduces it. Records in any of those states with an\n     ``expires_at <= now`` are eligible for expiration.\n  3. NEVER expires a ``kind == COMPLIANCE`` record. Regulatory facts\n     do not decay on a TTL clock; operator removal is the only path.\n     (``contracts.DEFAULT_TTL_DAYS[COMPLIANCE]`` is ``None`` precisely\n     for this reason; the guard here is belt-and-suspenders in case a\n     legacy row carries a non-null ``expires_at``.)\n  4. Uses ``review.expire_memory_by_id`` for the transition so the\n     audit trail in ``pas_memory_review_events`` is preserved. We do\n     NOT patch the records table directly.\n  5. Returns a structured report dict — never raises into the caller.\n     A Supabase failure during the find phase produces an empty\n     ``results`` list and a warning entry.\n\nReport shape (stable, machine-readable):\n\n    {\n        "brokerage_id": "<tenant>",\n        "checked":      <int>,          # candidates considered\n        "expired":      <int>,          # successful EXPIRED transitions\n        "failed":       <int>,          # transitions that did not succeed\n        "results":      [\n            {\n                "memory_id":  "...",\n                "kind":       "...",\n                "status":     "ok" | "warning" | "failed",\n                "from_status": "...",\n                "to_status":   "EXPIRED" | None,\n                "review_id":   "..."   # present on ok/warning\n            },\n            ...\n        ],\n        "warnings":     ["..."],        # non-fatal notes (e.g. supabase_unavailable)\n    }\n\nPAS144D explicitly does NOT build:\n  * cross-tenant batch sweep\n  * scheduling / cron daemon\n  * retrieval / similarity search\n  * embeddings / vector helpers\n  * autonomous learning loops\n  * any auto-approval path\n'
- 'pas.memory.sweeper'
- 'pas_memory_records'
- 'OPERATIONAL'
- 'now'
- 'limit'
- 'actor_type'
- 'SYSTEM'
- 'actor_id'
- 'reason'
- 'Lazy Supabase resolver. Mirrors store.py / queries.py / queue.py\nso unit tests can patch ``app.db.supabase_client.get_supabase``.'
- 'Any'
- 'return'
- 'datetime'
- 'Caller may pass an explicit ``now`` for deterministic tests.'
- 'int'
- 'row'
- 'Dict[str, Any]'
- 'bool'
- 'COMPLIANCE rows are exempt regardless of expires_at.'
- 'kind'
- 'value'
- 'Optional[datetime]'
- 'Parse an ISO-8601 ``expires_at`` value. Returns None if absent\nor unparsable — both are treated as "not yet expired".'
- '+00:00'
- 'brokerage_id'
- 'str'
- 'List[Dict[str, Any]]'
- 'Return the tenant-scoped rows that have reached or passed their\n``expires_at``.\n\nEligibility rules (the order is documented intentionally):\n  1. ``brokerage_id`` must match;\n  2. ``status`` must be in ``SWEEPABLE_STATUSES``;\n  3. ``kind`` must NOT be COMPLIANCE;\n  4. ``expires_at`` must be a parseable ISO-8601 timestamp;\n  5. ``expires_at <= now``.\n\nRows lacking ``expires_at`` are never considered expired (TTL of\n``None`` is a deliberate "no expiry" choice elsewhere in the\ncontract).\n\nReturns ``[]`` on missing brokerage_id or any Supabase failure.\nNever raises.\n'
- 'find_expired_memory dropped | reason=missing_brokerage_id'
- 'status'
- 'expires_at'
- 'data'
- 'find_expired_memory failed (non-critical) | brokerage='
- ' | error_type='
- 'Optional[str]'
- 'Find expired rows for ``brokerage_id`` and transition each via\n``review.expire_memory_by_id``.\n\nWhy route through PAS144C instead of patching the row directly:\n  * the transition table refuses CANDIDATE → EXPIRED;\n  * the audit row in ``pas_memory_review_events`` is the only\n    long-lived record of *why* a memory was retired.\nPAS144C will refuse CANDIDATE rows even though they live in\n``SWEEPABLE_STATUSES`` for FIND purposes — that refusal lands in\nthe report as a ``failed`` entry, NOT as a thrown exception, and\nthe underlying record is unaffected. That is the correct behaviour\ntoday: a CANDIDATE that has lapsed its TTL is a backlog problem an\noperator needs to triage, not a row the SYSTEM can quietly retire.\n\nReport shape — see the module docstring.\n\nNever raises. Supabase failures during the find phase produce an\nempty results list and a ``supabase_unavailable`` warning; per-row\nfailures during the transition phase are accumulated in the\n``failed`` counter and the per-row entry.\n'
- 'checked'
- 'expired'
- 'failed'
- 'results'
- 'warnings'
- 'missing_brokerage_id'
- 'expire_due_memory dropped | reason=missing_brokerage_id'
- 'invalid_actor_type_defaulted'
- 'memory_id'
- 'from_status'
- 'to_status'
- 'errors'
- 'row missing memory_id'
- 'review_id'
- 'warning'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS144D — Memory expiration sweep.\n\nSystem utility that walks ``pas_memory_records`` for a single tenant,\nfinds rows whose ``expires_at`` has lapsed, and transitions them to\nEXPIRED via the audited PAS144C ``review.expire_memory_by_id`` path.\n\nHard contract — every public helper in this module:\n\n  1. Requires ``brokerage_id`` (tenant isolation, mandatory). There is\n     no unscoped sweep helper; an operator who wants to sweep every\n     tenant runs the CLI once per ``--brokerage-id``.\n  2. Only considers rows whose status is one of\n     ``APPROVED`` / ``CANDIDATE`` / ``OPERATIONAL``.  In the current\n     schema "OPERATIONAL" is a *kind*, not a status — but PAS144A\'s\n     status set was deliberately conservative, so we accept the status\n     here defensively in case a downstream caller (or a future\n     migration) introduces it. Records in any of those states with an\n     ``expires_at <= now`` are eligible for expiration.\n  3. NEVER expires a ``kind == COMPLIANCE`` record. Regulatory facts\n     do not decay on a TTL clock; operator removal is the only path.\n     (``contracts.DEFAULT_TTL_DAYS[COMPLIANCE]`` is ``None`` precisely\n     for this reason; the guard here is belt-and-suspenders in case a\n     legacy row carries a non-null ``expires_at``.)\n  4. Uses ``review.expire_memory_by_id`` for the transition so the\n     audit trail in ``pas_memory_review_events`` is preserved. We do\n     NOT patch the records table directly.\n  5. Returns a structured report dict — never raises into the caller.\n     A Supabase failure during the find phase produces an empty\n     ``results`` list and a warning entry.\n\nReport shape (stable, machine-readable):\n\n    {\n        "brokerage_id": "<tenant>",\n        "checked":      <int>,          # candidates considered\n        "expired":      <int>,          # successful EXPIRED transitions\n        "failed":       <int>,          # transitions that did not succeed\n        "results":      [\n            {\n                "memory_id":  "...",\n                "kind":       "...",\n                "status":     "ok" | "warning" | "failed",\n                "from_status": "...",\n                "to_status":   "EXPIRED" | None,\n                "review_id":   "..."   # present on ok/warning\n            },\n            ...\n        ],\n        "warnings":     ["..."],        # non-fatal notes (e.g. supabase_unavailable)\n    }\n\nPAS144D explicitly does NOT build:\n  * cross-tenant batch sweep\n  * scheduling / cron daemon\n  * retrieval / similarity search\n  * embeddings / vector helpers\n  * autonomous learning loops\n  * any auto-approval path\n')
              STORE_NAME               0 (__doc__)

 62           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 64           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 65           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timezone'))
              IMPORT_NAME              4 (datetime)
              IMPORT_FROM              4 (datetime)
              STORE_NAME               4 (datetime)
              IMPORT_FROM              5 (timezone)
              STORE_NAME               5 (timezone)
              POP_TOP

 66           LOAD_SMALL_INT           0
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

 68           LOAD_SMALL_INT           1
              LOAD_CONST               5 (('queries',))
              IMPORT_NAME             11
              IMPORT_FROM             12 (queries)
              STORE_NAME              13 (queries_mod)
              POP_TOP

 69           LOAD_SMALL_INT           1
              LOAD_CONST               6 (('review',))
              IMPORT_NAME             11
              IMPORT_FROM             14 (review)
              STORE_NAME              15 (review_mod)
              POP_TOP

 70           LOAD_SMALL_INT           1
              LOAD_CONST               7 (('MemoryKind', 'MemoryStatus'))
              IMPORT_NAME             16 (contracts)
              IMPORT_FROM             17 (MemoryKind)
              STORE_NAME              17 (MemoryKind)
              IMPORT_FROM             18 (MemoryStatus)
              STORE_NAME              18 (MemoryStatus)
              POP_TOP

 72           LOAD_NAME                3 (logging)
              LOAD_ATTR               38 (getLogger)
              PUSH_NULL
              LOAD_CONST               8 ('pas.memory.sweeper')
              CALL                     1
              STORE_NAME              20 (logger)

 75           LOAD_CONST               9 ('pas_memory_records')
              STORE_NAME              21 (_TABLE)

 81           LOAD_NAME               22 (frozenset)
              PUSH_NULL

 82           LOAD_NAME               18 (MemoryStatus)
              LOAD_ATTR               46 (APPROVED)
              LOAD_ATTR               48 (value)

 83           LOAD_NAME               18 (MemoryStatus)
              LOAD_ATTR               50 (CANDIDATE)
              LOAD_ATTR               48 (value)

 84           LOAD_CONST              10 ('OPERATIONAL')

 81           BUILD_SET                3
              CALL                     1
              STORE_NAME              26 (SWEEPABLE_STATUSES)

 90           LOAD_NAME               13 (queries_mod)
              LOAD_ATTR               54 (MAX_QUERY_LIMIT)
              STORE_NAME              28 (SWEEP_HARD_LIMIT)

 97           LOAD_CONST              11 (<code object _get_db at 0x0000018C17FA33C0, file "app\services\memory\sweeper.py", line 97>)
              MAKE_FUNCTION
              STORE_NAME              29 (_get_db)

104           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\memory\sweeper.py", line 104>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _resolve_now at 0x0000018C180608A0, file "app\services\memory\sweeper.py", line 104>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_resolve_now)

113           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\sweeper.py", line 113>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _clamp_limit at 0x0000018C17FA92F0, file "app\services\memory\sweeper.py", line 113>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_clamp_limit)

123           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA2C40, file "app\services\memory\sweeper.py", line 123>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _is_compliance_kind at 0x0000018C1802C880, file "app\services\memory\sweeper.py", line 123>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_is_compliance_kind)

128           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA2100, file "app\services\memory\sweeper.py", line 128>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object _parse_expires_at at 0x0000018C1801CBD0, file "app\services\memory\sweeper.py", line 128>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_parse_expires_at)

146           LOAD_CONST              20 ('now')

149           LOAD_CONST               2 (None)

146           LOAD_CONST              21 ('limit')

150           LOAD_NAME               13 (queries_mod)
              LOAD_ATTR               68 (DEFAULT_QUERY_LIMIT)

146           BUILD_MAP                2
              LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18024E30, file "app\services\memory\sweeper.py", line 146>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object find_expired_memory at 0x0000018C17E91250, file "app\services\memory\sweeper.py", line 146>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              35 (find_expired_memory)

218           LOAD_CONST              24 ('actor_type')

221           LOAD_CONST              25 ('SYSTEM')

218           LOAD_CONST              26 ('actor_id')

222           LOAD_CONST               2 (None)

218           LOAD_CONST              27 ('reason')

223           LOAD_CONST               2 (None)

218           LOAD_CONST              20 ('now')

224           LOAD_CONST               2 (None)

218           LOAD_CONST              21 ('limit')

225           LOAD_NAME               13 (queries_mod)
              LOAD_ATTR               68 (DEFAULT_QUERY_LIMIT)

218           BUILD_MAP                5
              LOAD_CONST              28 (<code object __annotate__ at 0x0000018C180C4250, file "app\services\memory\sweeper.py", line 218>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object expire_due_memory at 0x0000018C177C5700, file "app\services\memory\sweeper.py", line 218>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              36 (expire_due_memory)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object _get_db at 0x0000018C17FA33C0, file "app\services\memory\sweeper.py", line 97>:
 97           RESUME                   0

100           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('get_supabase',))
              IMPORT_NAME              0 (app.db.supabase_client)
              IMPORT_FROM              1 (get_supabase)
              STORE_FAST               0 (get_supabase)
              POP_TOP

101           LOAD_FAST_BORROW         0 (get_supabase)
              PUSH_NULL
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\memory\sweeper.py", line 104>:
104           RESUME                   0
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

Disassembly of <code object _resolve_now at 0x0000018C180608A0, file "app\services\memory\sweeper.py", line 104>:
104           RESUME                   0

106           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (now)
              LOAD_GLOBAL              2 (datetime)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       49 (to L2)
              NOT_TAKEN

107           LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR                4 (tzinfo)
              POP_JUMP_IF_NOT_NONE    33 (to L1)
              NOT_TAKEN

108           LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR                7 (replace + NULL|self)
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              LOAD_CONST               1 (('tzinfo',))
              CALL_KW                  1
              RETURN_VALUE

109   L1:     LOAD_FAST_BORROW         0 (now)
              RETURN_VALUE

110   L2:     LOAD_GLOBAL              2 (datetime)
              LOAD_ATTR               12 (now)
              PUSH_NULL
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\sweeper.py", line 113>:
113           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('limit')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _clamp_limit at 0x0000018C17FA92F0, file "app\services\memory\sweeper.py", line 113>:
 113           RESUME                   0

 114           NOP

 115   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (limit)
               CALL                     1
               STORE_FAST               1 (n)

 118   L2:     LOAD_FAST                1 (n)
               LOAD_SMALL_INT           0
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE       17 (to L3)
               NOT_TAKEN

 119           LOAD_GLOBAL              6 (queries_mod)
               LOAD_ATTR                8 (DEFAULT_QUERY_LIMIT)
               RETURN_VALUE

 120   L3:     LOAD_GLOBAL             11 (min + NULL)
               LOAD_FAST                1 (n)
               LOAD_GLOBAL             12 (SWEEP_HARD_LIMIT)
               CALL                     2
               RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

 116           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       20 (to L6)
               NOT_TAKEN
               POP_TOP

 117           LOAD_GLOBAL              6 (queries_mod)
               LOAD_ATTR                8 (DEFAULT_QUERY_LIMIT)
               SWAP                     2
       L5:     POP_EXCEPT
               RETURN_VALUE

 116   L6:     RERAISE                  0

  --   L7:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L4 [0]
  L4 to L5 -> L7 [1] lasti
  L6 to L7 -> L7 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app\services\memory\sweeper.py", line 123>:
123           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _is_compliance_kind at 0x0000018C1802C880, file "app\services\memory\sweeper.py", line 123>:
123           RESUME                   0

125           LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('kind')
              CALL                     1
              LOAD_GLOBAL              2 (MemoryKind)
              LOAD_ATTR                4 (COMPLIANCE)
              LOAD_ATTR                6 (value)
              COMPARE_OP              72 (==)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app\services\memory\sweeper.py", line 128>:
128           RESUME                   0
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
              LOAD_CONST               4 ('Optional[datetime]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _parse_expires_at at 0x0000018C1801CBD0, file "app\services\memory\sweeper.py", line 128>:
 128           RESUME                   0

 131           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (value)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        9 (to L1)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (value)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

 132   L1:     LOAD_CONST               1 (None)
               RETURN_VALUE

 133   L2:     NOP

 134   L3:     LOAD_GLOBAL              4 (datetime)
               LOAD_ATTR                6 (fromisoformat)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (value)
               LOAD_ATTR                9 (replace + NULL|self)
               LOAD_CONST               2 ('Z')
               LOAD_CONST               3 ('+00:00')
               CALL                     2
               CALL                     1
               STORE_FAST               1 (ts)

 137   L4:     LOAD_FAST                1 (ts)
               LOAD_ATTR               12 (tzinfo)
               POP_JUMP_IF_NOT_NONE    33 (to L5)
               NOT_TAKEN

 138           LOAD_FAST                1 (ts)
               LOAD_ATTR                9 (replace + NULL|self)
               LOAD_GLOBAL             14 (timezone)
               LOAD_ATTR               16 (utc)
               LOAD_CONST               4 (('tzinfo',))
               CALL_KW                  1
               STORE_FAST               1 (ts)

 139   L5:     LOAD_FAST                1 (ts)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

 135           LOAD_GLOBAL             10 (ValueError)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

 136   L7:     POP_EXCEPT
               LOAD_CONST               1 (None)
               RETURN_VALUE

 135   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L3 to L4 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app\services\memory\sweeper.py", line 146>:
146           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

147           LOAD_CONST               2 ('str')

146           LOAD_CONST               3 ('now')

149           LOAD_CONST               4 ('Optional[datetime]')

146           LOAD_CONST               5 ('limit')

150           LOAD_CONST               6 ('int')

146           LOAD_CONST               7 ('return')

151           LOAD_CONST               8 ('List[Dict[str, Any]]')

146           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object find_expired_memory at 0x0000018C17E91250, file "app\services\memory\sweeper.py", line 146>:
 146            RESUME                   0

 169            LOAD_GLOBAL              1 (isinstance + NULL)
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
                POP_JUMP_IF_TRUE        24 (to L2)
                NOT_TAKEN

 170    L1:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)
                LOAD_CONST               1 ('find_expired_memory dropped | reason=missing_brokerage_id')
                CALL                     1
                POP_TOP

 171            BUILD_LIST               0
                RETURN_VALUE

 173    L2:     LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               3 (bid)

 174            LOAD_GLOBAL             11 (_resolve_now + NULL)
                LOAD_FAST_BORROW         1 (now)
                CALL                     1
                STORE_FAST               4 (cutoff)

 175            LOAD_GLOBAL             13 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1
                STORE_FAST               5 (capped)

 177            NOP

 178    L3:     LOAD_GLOBAL             15 (_get_db + NULL)
                CALL                     0
                STORE_FAST               6 (db)

 180            LOAD_FAST_BORROW         6 (db)
                LOAD_ATTR               17 (table + NULL|self)
                LOAD_GLOBAL             18 (_TABLE)
                CALL                     1

 181            LOAD_ATTR               21 (select + NULL|self)
                LOAD_CONST               2 ('*')
                CALL                     1

 182            LOAD_ATTR               23 (eq + NULL|self)
                LOAD_CONST               3 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)
                CALL                     2

 183            LOAD_ATTR               25 (in_ + NULL|self)
                LOAD_CONST               4 ('status')
                LOAD_GLOBAL             27 (sorted + NULL)
                LOAD_GLOBAL             28 (SWEEPABLE_STATUSES)
                CALL                     1
                CALL                     2

 184            LOAD_ATTR               31 (order + NULL|self)
                LOAD_CONST               5 ('expires_at')
                LOAD_CONST               6 (False)
                LOAD_CONST               7 (('desc',))
                CALL_KW                  2

 185            LOAD_ATTR               33 (limit + NULL|self)
                LOAD_FAST_BORROW         5 (capped)
                CALL                     1

 179            STORE_FAST               7 (q)

 187            LOAD_FAST_BORROW         7 (q)
                LOAD_ATTR               35 (execute + NULL|self)
                CALL                     0
                STORE_FAST               8 (result)

 188            LOAD_GLOBAL             37 (list + NULL)
                LOAD_GLOBAL             39 (getattr + NULL)
                LOAD_FAST_BORROW         8 (result)
                LOAD_CONST               8 ('data')
                LOAD_CONST               9 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L4:     CALL                     1
                STORE_FAST               9 (rows)

 196    L5:     BUILD_LIST               0
                STORE_FAST              11 (out)

 197            LOAD_FAST                9 (rows)
                GET_ITER
        L6:     FOR_ITER               107 (to L11)
                STORE_FAST              12 (r)

 201            LOAD_FAST               12 (r)
                LOAD_ATTR               47 (get + NULL|self)
                LOAD_CONST               4 ('status')
                CALL                     1
                LOAD_GLOBAL             28 (SWEEPABLE_STATUSES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN

 202            JUMP_BACKWARD           31 (to L6)

 203    L7:     LOAD_GLOBAL             49 (_is_compliance_kind + NULL)
                LOAD_FAST               12 (r)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN

 204            JUMP_BACKWARD           50 (to L6)

 205    L8:     LOAD_GLOBAL             51 (_parse_expires_at + NULL)
                LOAD_FAST               12 (r)
                LOAD_ATTR               47 (get + NULL|self)
                LOAD_CONST               5 ('expires_at')
                CALL                     1
                CALL                     1
                STORE_FAST              13 (exp)

 206            LOAD_FAST               13 (exp)
                POP_JUMP_IF_NOT_NONE     3 (to L9)
                NOT_TAKEN

 207            JUMP_BACKWARD           82 (to L6)

 208    L9:     LOAD_FAST_LOAD_FAST    212 (exp, cutoff)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN

 209            JUMP_BACKWARD           90 (to L6)

 210   L10:     LOAD_FAST               11 (out)
                LOAD_ATTR               53 (append + NULL|self)
                LOAD_FAST               12 (r)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          109 (to L6)

 197   L11:     END_FOR
                POP_ITER

 211            LOAD_FAST               11 (out)
                RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 189            LOAD_GLOBAL             40 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       59 (to L17)
                NOT_TAKEN
                STORE_FAST              10 (e)

 190   L13:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 191            LOAD_CONST              10 ('find_expired_memory failed (non-critical) | brokerage=')

 192            LOAD_FAST                3 (bid)
                FORMAT_SIMPLE
                LOAD_CONST              11 (' | error_type=')
                LOAD_GLOBAL             43 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               44 (__name__)
                FORMAT_SIMPLE

 191            BUILD_STRING             4

 190            CALL                     1
                POP_TOP

 194            BUILD_LIST               0
       L14:     SWAP                     2
       L15:     POP_EXCEPT
                LOAD_CONST               9 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RETURN_VALUE

  --   L16:     LOAD_CONST               9 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 189   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L12 [0]
  L12 to L13 -> L18 [1] lasti
  L13 to L14 -> L16 [1] lasti
  L14 to L15 -> L18 [1] lasti
  L16 to L18 -> L18 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C180C4250, file "app\services\memory\sweeper.py", line 218>:
218           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

219           LOAD_CONST               2 ('str')

218           LOAD_CONST               3 ('actor_type')

221           LOAD_CONST               2 ('str')

218           LOAD_CONST               4 ('actor_id')

222           LOAD_CONST               5 ('Optional[str]')

218           LOAD_CONST               6 ('reason')

223           LOAD_CONST               5 ('Optional[str]')

218           LOAD_CONST               7 ('now')

224           LOAD_CONST               8 ('Optional[datetime]')

218           LOAD_CONST               9 ('limit')

225           LOAD_CONST              10 ('int')

218           LOAD_CONST              11 ('return')

226           LOAD_CONST              12 ('Dict[str, Any]')

218           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object expire_due_memory at 0x0000018C177C5700, file "app\services\memory\sweeper.py", line 218>:
218            RESUME                   0

249            LOAD_CONST               1 ('brokerage_id')
               LOAD_CONST               2 ('')

250            LOAD_CONST               3 ('checked')
               LOAD_SMALL_INT           0

251            LOAD_CONST               4 ('expired')
               LOAD_SMALL_INT           0

252            LOAD_CONST               5 ('failed')
               LOAD_SMALL_INT           0

253            LOAD_CONST               6 ('results')
               BUILD_LIST               0

254            LOAD_CONST               7 ('warnings')
               BUILD_LIST               0

248            BUILD_MAP                6
               STORE_FAST               6 (report)

257            LOAD_GLOBAL              1 (isinstance + NULL)
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
               POP_JUMP_IF_TRUE        48 (to L2)
               NOT_TAKEN

258    L1:     LOAD_FAST_BORROW         6 (report)
               LOAD_CONST               7 ('warnings')
               BINARY_OP               26 ([])
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_CONST               8 ('missing_brokerage_id')
               CALL                     1
               POP_TOP

259            LOAD_GLOBAL              8 (logger)
               LOAD_ATTR               11 (warning + NULL|self)
               LOAD_CONST               9 ('expire_due_memory dropped | reason=missing_brokerage_id')
               CALL                     1
               POP_TOP

260            LOAD_FAST_BORROW         6 (report)
               RETURN_VALUE

262    L2:     LOAD_FAST_BORROW         0 (brokerage_id)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (bid)

263            LOAD_FAST_BORROW_LOAD_FAST_BORROW 118 (bid, report)
               LOAD_CONST               1 ('brokerage_id')
               STORE_SUBSCR

265            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (actor_type)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L3)
               NOT_TAKEN
               LOAD_FAST_BORROW         1 (actor_type)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        27 (to L4)
               NOT_TAKEN

266    L3:     LOAD_FAST_BORROW         6 (report)
               LOAD_CONST               7 ('warnings')
               BINARY_OP               26 ([])
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_CONST              10 ('invalid_actor_type_defaulted')
               CALL                     1
               POP_TOP

267            LOAD_CONST              11 ('SYSTEM')
               STORE_FAST               1 (actor_type)

269    L4:     LOAD_GLOBAL             13 (find_expired_memory + NULL)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 116 (bid, now)
               LOAD_FAST_BORROW         5 (limit)
               LOAD_CONST              12 (('now', 'limit'))
               CALL_KW                  3
               STORE_FAST               8 (candidates)

270            LOAD_GLOBAL             15 (len + NULL)
               LOAD_FAST_BORROW         8 (candidates)
               CALL                     1
               LOAD_FAST_BORROW         6 (report)
               LOAD_CONST               3 ('checked')
               STORE_SUBSCR

271            LOAD_FAST_BORROW         8 (candidates)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN

275            LOAD_FAST_BORROW         6 (report)
               RETURN_VALUE

277    L5:     LOAD_FAST_BORROW         8 (candidates)
               GET_ITER
       L6:     EXTENDED_ARG             1
               FOR_ITER               452 (to L15)
               STORE_FAST               9 (row)

278            LOAD_FAST_BORROW         9 (row)
               LOAD_ATTR               17 (get + NULL|self)
               LOAD_CONST              13 ('memory_id')
               CALL                     1
               STORE_FAST              10 (memory_id)

279            LOAD_FAST_BORROW         9 (row)
               LOAD_ATTR               17 (get + NULL|self)
               LOAD_CONST              14 ('kind')
               CALL                     1
               STORE_FAST              11 (kind)

280            LOAD_FAST_BORROW         9 (row)
               LOAD_ATTR               17 (get + NULL|self)
               LOAD_CONST              15 ('status')
               CALL                     1
               STORE_FAST              12 (from_status)

281            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW        10 (memory_id)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L7)
               NOT_TAKEN
               LOAD_FAST_BORROW        10 (memory_id)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        61 (to L8)
               NOT_TAKEN

282    L7:     LOAD_FAST_BORROW         6 (report)
               LOAD_CONST               5 ('failed')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR

283            LOAD_FAST_BORROW         6 (report)
               LOAD_CONST               6 ('results')
               BINARY_OP               26 ([])
               LOAD_ATTR                7 (append + NULL|self)

284            LOAD_CONST              13 ('memory_id')
               LOAD_CONST              16 (None)

285            LOAD_CONST              14 ('kind')
               LOAD_FAST_BORROW        11 (kind)

286            LOAD_CONST              15 ('status')
               LOAD_CONST               5 ('failed')

287            LOAD_CONST              17 ('from_status')
               LOAD_FAST_BORROW        12 (from_status)

288            LOAD_CONST              18 ('to_status')
               LOAD_CONST              16 (None)

289            LOAD_CONST              19 ('errors')
               LOAD_CONST              20 ('row missing memory_id')
               BUILD_LIST               1

283            BUILD_MAP                6
               CALL                     1
               POP_TOP

291            JUMP_BACKWARD          159 (to L6)

293    L8:     LOAD_GLOBAL             18 (review_mod)
               LOAD_ATTR               20 (expire_memory_by_id)
               PUSH_NULL

294            LOAD_FAST_BORROW        10 (memory_id)

295            LOAD_FAST_BORROW         7 (bid)

296            LOAD_FAST_BORROW         1 (actor_type)

297            LOAD_FAST_BORROW         2 (actor_id)

298            LOAD_FAST_BORROW         3 (reason)

293            LOAD_CONST              21 (('memory_id', 'brokerage_id', 'actor_type', 'actor_id', 'reason'))
               CALL_KW                  5
               STORE_FAST              13 (outcome)

302            LOAD_CONST              13 ('memory_id')
               LOAD_FAST_BORROW        10 (memory_id)

303            LOAD_CONST              14 ('kind')
               LOAD_FAST_BORROW        11 (kind)

304            LOAD_CONST              15 ('status')
               LOAD_FAST_BORROW        13 (outcome)
               LOAD_ATTR               17 (get + NULL|self)
               LOAD_CONST              15 ('status')
               CALL                     1

305            LOAD_CONST              17 ('from_status')
               LOAD_FAST_BORROW        13 (outcome)
               LOAD_ATTR               17 (get + NULL|self)
               LOAD_CONST              17 ('from_status')
               LOAD_FAST_BORROW        12 (from_status)
               CALL                     2

306            LOAD_CONST              18 ('to_status')
               LOAD_FAST_BORROW        13 (outcome)
               LOAD_ATTR               17 (get + NULL|self)
               LOAD_CONST              18 ('to_status')
               CALL                     1

301            BUILD_MAP                5
               STORE_FAST              14 (entry)

308            LOAD_CONST              22 ('review_id')
               LOAD_FAST_BORROW        13 (outcome)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       13 (to L9)
               NOT_TAKEN

309            LOAD_FAST_BORROW        13 (outcome)
               LOAD_CONST              22 ('review_id')
               BINARY_OP               26 ([])
               LOAD_FAST_BORROW        14 (entry)
               LOAD_CONST              22 ('review_id')
               STORE_SUBSCR

310    L9:     LOAD_CONST               7 ('warnings')
               LOAD_FAST_BORROW        13 (outcome)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       22 (to L10)
               NOT_TAKEN

311            LOAD_GLOBAL             23 (list + NULL)
               LOAD_FAST_BORROW        13 (outcome)
               LOAD_CONST               7 ('warnings')
               BINARY_OP               26 ([])
               CALL                     1
               LOAD_FAST_BORROW        14 (entry)
               LOAD_CONST               7 ('warnings')
               STORE_SUBSCR

312   L10:     LOAD_CONST              19 ('errors')
               LOAD_FAST_BORROW        13 (outcome)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       22 (to L11)
               NOT_TAKEN

313            LOAD_GLOBAL             23 (list + NULL)
               LOAD_FAST_BORROW        13 (outcome)
               LOAD_CONST              19 ('errors')
               BINARY_OP               26 ([])
               CALL                     1
               LOAD_FAST_BORROW        14 (entry)
               LOAD_CONST              19 ('errors')
               STORE_SUBSCR

315   L11:     LOAD_FAST_BORROW        13 (outcome)
               LOAD_ATTR               17 (get + NULL|self)
               LOAD_CONST              15 ('status')
               CALL                     1
               LOAD_CONST              23 ('ok')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       23 (to L12)
               NOT_TAKEN

316            LOAD_FAST_BORROW         6 (report)
               LOAD_CONST               4 ('expired')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR
               JUMP_FORWARD            65 (to L14)

317   L12:     LOAD_FAST_BORROW        13 (outcome)
               LOAD_ATTR               17 (get + NULL|self)
               LOAD_CONST              15 ('status')
               CALL                     1
               LOAD_CONST              24 ('warning')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       23 (to L13)
               NOT_TAKEN

322            LOAD_FAST_BORROW         6 (report)
               LOAD_CONST               4 ('expired')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR
               JUMP_FORWARD            21 (to L14)

324   L13:     LOAD_FAST_BORROW         6 (report)
               LOAD_CONST               5 ('failed')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR

326   L14:     LOAD_FAST_BORROW         6 (report)
               LOAD_CONST               6 ('results')
               BINARY_OP               26 ([])
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW        14 (entry)
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          455 (to L6)

277   L15:     END_FOR
               POP_ITER

328            LOAD_FAST_BORROW         6 (report)
               RETURN_VALUE
```
