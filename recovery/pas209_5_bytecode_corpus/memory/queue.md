# memory/queue

- **pyc:** `app\services\memory\__pycache__\queue.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/queue.py`
- **co_filename (from bytecode):** `app\services\memory\queue.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144D — Memory review / expiration queue surfaces.

Tenant-scoped, read-only helpers that present the operator-facing
slices of ``pas_memory_records``:

  * the CANDIDATE review backlog,
  * the QUARANTINED queue,
  * the about-to-expire APPROVED queue,
  * the active / APPROVED queue.

Hard contract — every public helper in this module:

  1. Requires ``brokerage_id`` (tenant isolation, mandatory). There is
     no unscoped queue helper; that path remains
     ``queries.list_memory_admin_unscoped``.
  2. Clamps the caller-supplied ``limit`` to
     ``queries.MAX_QUERY_LIMIT`` (the single ceiling for every memory
     read surface).
  3. Touches ``pas_memory_records`` only — never the audit table, never
     any retrieval / similarity index (PAS144D does not build one).
  4. Returns pass-through dicts from the row. The PAS144A migration
     does not model raw transcript columns at all, so there is nothing
     to strip; the rule is kept explicit here because every queue
     surface is operator-facing.
  5. Never raises on Supabase failure. Returns ``[]`` instead.

PAS144D explicitly does NOT build:
  * retrieval / similarity search
  * embeddings / vector helpers
  * autonomous learning loops
  * runtime PAS Brain injection of memory rows
  * dashboard / UI surfaces
  * any automatic approval path

Public surface (deliberately small):
  - list_review_queue(brokerage_id, status="CANDIDATE",
                      kind=None, limit=50)
  - list_quarantine_queue(brokerage_id, limit=50)
  - list_expiring_memory(brokerage_id, within_days=7, limit=50)
  - list_approved_memory(brokerage_id, kind=None, limit=50)
```

## Imports

``, `Any`, `Dict`, `List`, `MemoryKind`, `MemoryStatus`, `Optional`, `Union`, `__future__`, `annotations`, `app.db.supabase_client`, `contracts`, `datetime`, `get_supabase`, `logging`, `queries`, `timedelta`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_limit`, `_coerce_kind`, `_coerce_status`, `_get_db`, `_now`, `_within_days`, `list_approved_memory`, `list_expiring_memory`, `list_quarantine_queue`, `list_review_queue`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS144D — Memory review / expiration queue surfaces.\n\nTenant-scoped, read-only helpers that present the operator-facing\nslices of ``pas_memory_records``:\n\n  * the CANDIDATE review backlog,\n  * the QUARANTINED queue,\n  * the about-to-expire APPROVED queue,\n  * the active / APPROVED queue.\n\nHard contract — every public helper in this module:\n\n  1. Requires ``brokerage_id`` (tenant isolation, mandatory). There is\n     no unscoped queue helper; that path remains\n     ``queries.list_memory_admin_unscoped``.\n  2. Clamps the caller-supplied ``limit`` to\n     ``queries.MAX_QUERY_LIMIT`` (the single ceiling for every memory\n     read surface).\n  3. Touches ``pas_memory_records`` only — never the audit table, never\n     any retrieval / similarity index (PAS144D does not build one).\n  4. Returns pass-through dicts from the row. The PAS144A migration\n     does not model raw transcript columns at all, so there is nothing\n     to strip; the rule is kept explicit here because every queue\n     surface is operator-facing.\n  5. Never raises on Supabase failure. Returns ``[]`` instead.\n\nPAS144D explicitly does NOT build:\n  * retrieval / similarity search\n  * embeddings / vector helpers\n  * autonomous learning loops\n  * runtime PAS Brain injection of memory rows\n  * dashboard / UI surfaces\n  * any automatic approval path\n\nPublic surface (deliberately small):\n  - list_review_queue(brokerage_id, status="CANDIDATE",\n                      kind=None, limit=50)\n  - list_quarantine_queue(brokerage_id, limit=50)\n  - list_expiring_memory(brokerage_id, within_days=7, limit=50)\n  - list_approved_memory(brokerage_id, kind=None, limit=50)\n'
- 'pas.memory.queue'
- 'pas_memory_records'
- 'status'
- 'kind'
- 'limit'
- 'within_days'
- 'Lazy Supabase resolver. Mirrors store.py / queries.py so unit\ntests can patch ``app.db.supabase_client.get_supabase``.'
- 'Union[None, str, MemoryKind]'
- 'return'
- 'Optional[str]'
- 'queue: ignoring unknown kind='
- 'Union[None, str, MemoryStatus]'
- 'queue: ignoring unknown status='
- 'Optional[int]'
- 'int'
- 'Share the single ceiling defined in queries.MAX_QUERY_LIMIT.\n\nWe do not import the queries.* defaults to avoid a hidden coupling\non the default value — we want our own default-50 behaviour but\nthe same ceiling as the read layer.\n'
- 'days'
- 'Any'
- 'Sanitize the within_days window. Negative / non-int → 7 days.'
- 'datetime'
- 'brokerage_id'
- 'str'
- 'Union[str, MemoryStatus]'
- 'List[Dict[str, Any]]'
- 'Return the operator review queue for ``brokerage_id``.\n\nDefault is the CANDIDATE backlog — rows that governance let through\nbut no human has approved yet. Sorted by ``confidence`` desc,\nthen ``outcome_weight`` desc, then ``created_at`` desc, so the most\npromising candidates surface first.\n\nA caller can pass ``status="QUARANTINED"`` (or any MemoryStatus\nvalue) to repurpose this helper for a non-CANDIDATE review slice —\nwe deliberately do NOT hard-code CANDIDATE, since the same sort\norder is what an operator wants when triaging quarantine too.\nUnknown / invalid status strings fall back to CANDIDATE rather than\nsilently widening the query.\n\nReturns ``[]`` on missing brokerage_id or on Supabase failure.\nNever raises into the caller.\n'
- 'list_review_queue dropped | reason=missing_brokerage_id'
- 'confidence'
- 'outcome_weight'
- 'created_at'
- 'data'
- 'list_review_queue failed (non-critical) | brokerage='
- ' | error_type='
- 'Return QUARANTINED memory for ``brokerage_id``.\n\nSorted by ``created_at`` desc — the most recently quarantined\nrecords surface first, which is what an operator on call typically\nwants. Quarantine is a triage list, not a leaderboard, so we do not\nsort by confidence here.\n\nReturns ``[]`` on missing brokerage_id or on Supabase failure.\n'
- 'list_quarantine_queue dropped | reason=missing_brokerage_id'
- 'list_quarantine_queue failed (non-critical) | brokerage='
- "Return APPROVED memory whose ``expires_at`` lands inside the\nnext ``within_days`` days.\n\nStrictly future-facing: rows that have already expired (i.e.\n``expires_at <= now``) are NOT included — those are the sweeper's\njob, not an operator-review surface. Sort order is ``expires_at``\nascending so the most urgent rows surface first.\n\nReturns ``[]`` on missing brokerage_id or on Supabase failure.\n"
- 'list_expiring_memory dropped | reason=missing_brokerage_id'
- 'expires_at'
- 'list_expiring_memory failed (non-critical) | brokerage='
- '+00:00'
- 'Return currently-APPROVED, not-yet-expired, not-quarantined,\nnot-rejected memory for ``brokerage_id``.\n\n"Approved queue" excludes:\n  * EXPIRED / REJECTED / QUARANTINED rows;\n  * rows whose ``expires_at`` is in the past.\n\nPAS144D does NOT wire this into retrieval — the runtime does not\nyet consume memory at all. This helper exists for the operator-\nreview surface (and the sweeper-adjacent UIs that PAS144E will\nbuild) so they have a single, defensible "what\'s currently live"\nview.\n\nReturns ``[]`` on missing brokerage_id or on Supabase failure.\n'
- 'list_approved_memory dropped | reason=missing_brokerage_id'
- 'list_approved_memory failed (non-critical) | brokerage='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS144D — Memory review / expiration queue surfaces.\n\nTenant-scoped, read-only helpers that present the operator-facing\nslices of ``pas_memory_records``:\n\n  * the CANDIDATE review backlog,\n  * the QUARANTINED queue,\n  * the about-to-expire APPROVED queue,\n  * the active / APPROVED queue.\n\nHard contract — every public helper in this module:\n\n  1. Requires ``brokerage_id`` (tenant isolation, mandatory). There is\n     no unscoped queue helper; that path remains\n     ``queries.list_memory_admin_unscoped``.\n  2. Clamps the caller-supplied ``limit`` to\n     ``queries.MAX_QUERY_LIMIT`` (the single ceiling for every memory\n     read surface).\n  3. Touches ``pas_memory_records`` only — never the audit table, never\n     any retrieval / similarity index (PAS144D does not build one).\n  4. Returns pass-through dicts from the row. The PAS144A migration\n     does not model raw transcript columns at all, so there is nothing\n     to strip; the rule is kept explicit here because every queue\n     surface is operator-facing.\n  5. Never raises on Supabase failure. Returns ``[]`` instead.\n\nPAS144D explicitly does NOT build:\n  * retrieval / similarity search\n  * embeddings / vector helpers\n  * autonomous learning loops\n  * runtime PAS Brain injection of memory rows\n  * dashboard / UI surfaces\n  * any automatic approval path\n\nPublic surface (deliberately small):\n  - list_review_queue(brokerage_id, status="CANDIDATE",\n                      kind=None, limit=50)\n  - list_quarantine_queue(brokerage_id, limit=50)\n  - list_expiring_memory(brokerage_id, within_days=7, limit=50)\n  - list_approved_memory(brokerage_id, kind=None, limit=50)\n')
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
              LOAD_CONST               3 (('datetime', 'timedelta', 'timezone'))
              IMPORT_NAME              4 (datetime)
              IMPORT_FROM              4 (datetime)
              STORE_NAME               4 (datetime)
              IMPORT_FROM              5 (timedelta)
              STORE_NAME               5 (timedelta)
              IMPORT_FROM              6 (timezone)
              STORE_NAME               6 (timezone)
              POP_TOP

 48           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional', 'Union'))
              IMPORT_NAME              7 (typing)
              IMPORT_FROM              8 (Any)
              STORE_NAME               8 (Any)
              IMPORT_FROM              9 (Dict)
              STORE_NAME               9 (Dict)
              IMPORT_FROM             10 (List)
              STORE_NAME              10 (List)
              IMPORT_FROM             11 (Optional)
              STORE_NAME              11 (Optional)
              IMPORT_FROM             12 (Union)
              STORE_NAME              12 (Union)
              POP_TOP

 50           LOAD_SMALL_INT           1
              LOAD_CONST               5 (('queries',))
              IMPORT_NAME             13
              IMPORT_FROM             14 (queries)
              STORE_NAME              15 (queries_mod)
              POP_TOP

 51           LOAD_SMALL_INT           1
              LOAD_CONST               6 (('MemoryKind', 'MemoryStatus'))
              IMPORT_NAME             16 (contracts)
              IMPORT_FROM             17 (MemoryKind)
              STORE_NAME              17 (MemoryKind)
              IMPORT_FROM             18 (MemoryStatus)
              STORE_NAME              18 (MemoryStatus)
              POP_TOP

 53           LOAD_NAME                3 (logging)
              LOAD_ATTR               38 (getLogger)
              PUSH_NULL
              LOAD_CONST               7 ('pas.memory.queue')
              CALL                     1
              STORE_NAME              20 (logger)

 56           LOAD_CONST               8 ('pas_memory_records')
              STORE_NAME              21 (_TABLE)

 63           LOAD_CONST               9 (<code object _get_db at 0x0000018C17FA2D30, file "app\services\memory\queue.py", line 63>)
              MAKE_FUNCTION
              STORE_NAME              22 (_get_db)

 70           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA33C0, file "app\services\memory\queue.py", line 70>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _coerce_kind at 0x0000018C17FED630, file "app\services\memory\queue.py", line 70>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              23 (_coerce_kind)

 84           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\queue.py", line 84>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _coerce_status at 0x0000018C17FED830, file "app\services\memory\queue.py", line 84>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_coerce_status)

 98           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA35A0, file "app\services\memory\queue.py", line 98>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _clamp_limit at 0x0000018C1794EBB0, file "app\services\memory\queue.py", line 98>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_clamp_limit)

116           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA3780, file "app\services\memory\queue.py", line 116>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _within_days at 0x0000018C1802C880, file "app\services\memory\queue.py", line 116>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_within_days)

127           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA2C40, file "app\services\memory\queue.py", line 127>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object _now at 0x0000018C18053CF0, file "app\services\memory\queue.py", line 127>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_now)

135           LOAD_CONST              20 ('status')

138           LOAD_NAME               18 (MemoryStatus)
              LOAD_ATTR               56 (CANDIDATE)

135           LOAD_CONST              21 ('kind')

139           LOAD_CONST               2 (None)

135           LOAD_CONST              22 ('limit')

140           LOAD_NAME               15 (queries_mod)
              LOAD_ATTR               58 (DEFAULT_QUERY_LIMIT)

135           BUILD_MAP                3
              LOAD_CONST              23 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\memory\queue.py", line 135>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object list_review_queue at 0x0000018C17F82110, file "app\services\memory\queue.py", line 135>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              30 (list_review_queue)

201           LOAD_CONST              22 ('limit')

204           LOAD_NAME               15 (queries_mod)
              LOAD_ATTR               58 (DEFAULT_QUERY_LIMIT)

201           BUILD_MAP                1
              LOAD_CONST              25 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\memory\queue.py", line 201>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object list_quarantine_queue at 0x0000018C17ED9FB0, file "app\services\memory\queue.py", line 201>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              31 (list_quarantine_queue)

245           LOAD_CONST              27 ('within_days')

248           LOAD_SMALL_INT           7

245           LOAD_CONST              22 ('limit')

249           LOAD_NAME               15 (queries_mod)
              LOAD_ATTR               58 (DEFAULT_QUERY_LIMIT)

245           BUILD_MAP                2
              LOAD_CONST              28 (<code object __annotate__ at 0x0000018C18024E30, file "app\services\memory\queue.py", line 245>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object list_expiring_memory at 0x0000018C177AE550, file "app\services\memory\queue.py", line 245>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              32 (list_expiring_memory)

317           LOAD_CONST              21 ('kind')

320           LOAD_CONST               2 (None)

317           LOAD_CONST              22 ('limit')

321           LOAD_NAME               15 (queries_mod)
              LOAD_ATTR               58 (DEFAULT_QUERY_LIMIT)

317           BUILD_MAP                2
              LOAD_CONST              30 (<code object __annotate__ at 0x0000018C18025030, file "app\services\memory\queue.py", line 317>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object list_approved_memory at 0x0000018C17ED68D0, file "app\services\memory\queue.py", line 317>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              33 (list_approved_memory)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object _get_db at 0x0000018C17FA2D30, file "app\services\memory\queue.py", line 63>:
 63           RESUME                   0

 66           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('get_supabase',))
              IMPORT_NAME              0 (app.db.supabase_client)
              IMPORT_FROM              1 (get_supabase)
              STORE_FAST               0 (get_supabase)
              POP_TOP

 67           LOAD_FAST_BORROW         0 (get_supabase)
              PUSH_NULL
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app\services\memory\queue.py", line 70>:
 70           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('kind')
              LOAD_CONST               2 ('Union[None, str, MemoryKind]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _coerce_kind at 0x0000018C17FED630, file "app\services\memory\queue.py", line 70>:
  70           RESUME                   0

  71           LOAD_FAST_BORROW         0 (kind)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

  72           LOAD_CONST               0 (None)
               RETURN_VALUE

  73   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (kind)
               LOAD_GLOBAL              2 (MemoryKind)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       13 (to L2)
               NOT_TAKEN

  74           LOAD_FAST_BORROW         0 (kind)
               LOAD_ATTR                4 (value)
               RETURN_VALUE

  75   L2:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (kind)
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       45 (to L5)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (kind)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L5)
               NOT_TAKEN

  76           NOP

  77   L3:     LOAD_GLOBAL              3 (MemoryKind + NULL)
               LOAD_FAST_BORROW         0 (kind)
               CALL                     1
               LOAD_ATTR                4 (value)
       L4:     RETURN_VALUE

  81   L5:     LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  78           LOAD_GLOBAL             10 (ValueError)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       30 (to L8)
               NOT_TAKEN
               POP_TOP

  79           LOAD_GLOBAL             12 (logger)
               LOAD_ATTR               15 (warning + NULL|self)
               LOAD_CONST               1 ('queue: ignoring unknown kind=')
               LOAD_FAST                0 (kind)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

  80   L7:     POP_EXCEPT
               LOAD_CONST               0 (None)
               RETURN_VALUE

  78   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L3 to L4 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\queue.py", line 84>:
 84           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('Union[None, str, MemoryStatus]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _coerce_status at 0x0000018C17FED830, file "app\services\memory\queue.py", line 84>:
  84           RESUME                   0

  85           LOAD_FAST_BORROW         0 (status)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

  86           LOAD_CONST               0 (None)
               RETURN_VALUE

  87   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (status)
               LOAD_GLOBAL              2 (MemoryStatus)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       13 (to L2)
               NOT_TAKEN

  88           LOAD_FAST_BORROW         0 (status)
               LOAD_ATTR                4 (value)
               RETURN_VALUE

  89   L2:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (status)
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       45 (to L5)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (status)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L5)
               NOT_TAKEN

  90           NOP

  91   L3:     LOAD_GLOBAL              3 (MemoryStatus + NULL)
               LOAD_FAST_BORROW         0 (status)
               CALL                     1
               LOAD_ATTR                4 (value)
       L4:     RETURN_VALUE

  95   L5:     LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  92           LOAD_GLOBAL             10 (ValueError)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       30 (to L8)
               NOT_TAKEN
               POP_TOP

  93           LOAD_GLOBAL             12 (logger)
               LOAD_ATTR               15 (warning + NULL|self)
               LOAD_CONST               1 ('queue: ignoring unknown status=')
               LOAD_FAST                0 (status)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

  94   L7:     POP_EXCEPT
               LOAD_CONST               0 (None)
               RETURN_VALUE

  92   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L3 to L4 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app\services\memory\queue.py", line 98>:
 98           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('limit')
              LOAD_CONST               2 ('Optional[int]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _clamp_limit at 0x0000018C1794EBB0, file "app\services\memory\queue.py", line 98>:
  98           RESUME                   0

 105           LOAD_FAST_BORROW         0 (limit)
               POP_JUMP_IF_NOT_NONE    17 (to L1)
               NOT_TAKEN

 106           LOAD_GLOBAL              0 (queries_mod)
               LOAD_ATTR                2 (DEFAULT_QUERY_LIMIT)
               RETURN_VALUE

 107   L1:     NOP

 108   L2:     LOAD_GLOBAL              5 (int + NULL)
               LOAD_FAST_BORROW         0 (limit)
               CALL                     1
               STORE_FAST               1 (n)

 111   L3:     LOAD_FAST                1 (n)
               LOAD_SMALL_INT           0
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE       17 (to L4)
               NOT_TAKEN

 112           LOAD_GLOBAL              0 (queries_mod)
               LOAD_ATTR                2 (DEFAULT_QUERY_LIMIT)
               RETURN_VALUE

 113   L4:     LOAD_GLOBAL             11 (min + NULL)
               LOAD_FAST                1 (n)
               LOAD_GLOBAL              0 (queries_mod)
               LOAD_ATTR               12 (MAX_QUERY_LIMIT)
               CALL                     2
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 109           LOAD_GLOBAL              6 (TypeError)
               LOAD_GLOBAL              8 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       20 (to L7)
               NOT_TAKEN
               POP_TOP

 110           LOAD_GLOBAL              0 (queries_mod)
               LOAD_ATTR                2 (DEFAULT_QUERY_LIMIT)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 109   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app\services\memory\queue.py", line 116>:
116           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('days')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _within_days at 0x0000018C1802C880, file "app\services\memory\queue.py", line 116>:
 116           RESUME                   0

 118           NOP

 119   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (days)
               CALL                     1
               STORE_FAST               1 (n)

 122   L2:     LOAD_FAST                1 (n)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 123           LOAD_SMALL_INT           7
               RETURN_VALUE

 124   L3:     LOAD_FAST                1 (n)
               RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

 120           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L6)
               NOT_TAKEN
               POP_TOP

 121   L5:     POP_EXCEPT
               LOAD_SMALL_INT           7
               RETURN_VALUE

 120   L6:     RERAISE                  0

  --   L7:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L4 [0]
  L4 to L5 -> L7 [1] lasti
  L6 to L7 -> L7 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app\services\memory\queue.py", line 127>:
127           RESUME                   0
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

Disassembly of <code object _now at 0x0000018C18053CF0, file "app\services\memory\queue.py", line 127>:
127           RESUME                   0

128           LOAD_GLOBAL              0 (datetime)
              LOAD_ATTR                2 (now)
              PUSH_NULL
              LOAD_GLOBAL              4 (timezone)
              LOAD_ATTR                6 (utc)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\memory\queue.py", line 135>:
135           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

136           LOAD_CONST               2 ('str')

135           LOAD_CONST               3 ('status')

138           LOAD_CONST               4 ('Union[str, MemoryStatus]')

135           LOAD_CONST               5 ('kind')

139           LOAD_CONST               6 ('Union[None, str, MemoryKind]')

135           LOAD_CONST               7 ('limit')

140           LOAD_CONST               8 ('int')

135           LOAD_CONST               9 ('return')

141           LOAD_CONST              10 ('List[Dict[str, Any]]')

135           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object list_review_queue at 0x0000018C17F82110, file "app\services\memory\queue.py", line 135>:
 135            RESUME                   0

 159            LOAD_GLOBAL              1 (isinstance + NULL)
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

 160    L1:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)
                LOAD_CONST               1 ('list_review_queue dropped | reason=missing_brokerage_id')
                CALL                     1
                POP_TOP

 161            BUILD_LIST               0
                RETURN_VALUE

 163    L2:     LOAD_GLOBAL             11 (_coerce_status + NULL)
                LOAD_FAST_BORROW         1 (status)
                CALL                     1
                STORE_FAST               4 (status_value)

 164            LOAD_FAST_BORROW         4 (status_value)
                POP_JUMP_IF_NOT_NONE    27 (to L3)
                NOT_TAKEN

 165            LOAD_GLOBAL             12 (MemoryStatus)
                LOAD_ATTR               14 (CANDIDATE)
                LOAD_ATTR               16 (value)
                STORE_FAST               4 (status_value)

 167    L3:     LOAD_GLOBAL             19 (_coerce_kind + NULL)
                LOAD_FAST_BORROW         2 (kind)
                CALL                     1
                STORE_FAST               5 (kind_value)

 168            LOAD_GLOBAL             21 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         3 (limit)
                CALL                     1
                STORE_FAST               6 (capped)

 170            NOP

 171    L4:     LOAD_GLOBAL             23 (_get_db + NULL)
                CALL                     0
                STORE_FAST               7 (db)

 173            LOAD_FAST_BORROW         7 (db)
                LOAD_ATTR               25 (table + NULL|self)
                LOAD_GLOBAL             26 (_TABLE)
                CALL                     1

 174            LOAD_ATTR               29 (select + NULL|self)
                LOAD_CONST               3 ('*')
                CALL                     1

 175            LOAD_ATTR               31 (eq + NULL|self)
                LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                CALL                     2

 176            LOAD_ATTR               31 (eq + NULL|self)
                LOAD_CONST               5 ('status')
                LOAD_FAST_BORROW         4 (status_value)
                CALL                     2

 172            STORE_FAST               8 (q)

 178            LOAD_FAST_BORROW         5 (kind_value)
                POP_JUMP_IF_NONE        19 (to L5)
                NOT_TAKEN

 179            LOAD_FAST_BORROW         8 (q)
                LOAD_ATTR               31 (eq + NULL|self)
                LOAD_CONST               6 ('kind')
                LOAD_FAST_BORROW         5 (kind_value)
                CALL                     2
                STORE_FAST               8 (q)

 183    L5:     LOAD_FAST_BORROW         8 (q)
                LOAD_ATTR               33 (order + NULL|self)
                LOAD_CONST               7 ('confidence')
                LOAD_CONST               8 (True)
                LOAD_CONST               9 (('desc',))
                CALL_KW                  2
                STORE_FAST               8 (q)

 184            LOAD_FAST_BORROW         8 (q)
                LOAD_ATTR               33 (order + NULL|self)
                LOAD_CONST              10 ('outcome_weight')
                LOAD_CONST               8 (True)
                LOAD_CONST               9 (('desc',))
                CALL_KW                  2
                STORE_FAST               8 (q)

 185            LOAD_FAST_BORROW         8 (q)
                LOAD_ATTR               33 (order + NULL|self)
                LOAD_CONST              11 ('created_at')
                LOAD_CONST               8 (True)
                LOAD_CONST               9 (('desc',))
                CALL_KW                  2
                STORE_FAST               8 (q)

 186            LOAD_FAST_BORROW         8 (q)
                LOAD_ATTR               35 (limit + NULL|self)
                LOAD_FAST_BORROW         6 (capped)
                CALL                     1
                STORE_FAST               8 (q)

 187            LOAD_FAST_BORROW         8 (q)
                LOAD_ATTR               37 (execute + NULL|self)
                CALL                     0
                STORE_FAST               9 (result)

 188            LOAD_GLOBAL             39 (list + NULL)
                LOAD_GLOBAL             41 (getattr + NULL)
                LOAD_FAST_BORROW         9 (result)
                LOAD_CONST              12 ('data')
                LOAD_CONST               2 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                BUILD_LIST               0
        L8:     CALL                     1
        L9:     RETURN_VALUE

  --   L10:     PUSH_EXC_INFO

 189            LOAD_GLOBAL             42 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       59 (to L15)
                NOT_TAKEN
                STORE_FAST              10 (e)

 190   L11:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 191            LOAD_CONST              13 ('list_review_queue failed (non-critical) | brokerage=')

 192            LOAD_FAST                0 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST              14 (' | error_type=')
                LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE

 191            BUILD_STRING             4

 190            CALL                     1
                POP_TOP

 194            BUILD_LIST               0
       L12:     SWAP                     2
       L13:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RETURN_VALUE

  --   L14:     LOAD_CONST               2 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 189   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L6 -> L10 [0]
  L7 to L9 -> L10 [0]
  L10 to L11 -> L16 [1] lasti
  L11 to L12 -> L14 [1] lasti
  L12 to L13 -> L16 [1] lasti
  L14 to L16 -> L16 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\memory\queue.py", line 201>:
201           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

202           LOAD_CONST               2 ('str')

201           LOAD_CONST               3 ('limit')

204           LOAD_CONST               4 ('int')

201           LOAD_CONST               5 ('return')

205           LOAD_CONST               6 ('List[Dict[str, Any]]')

201           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object list_quarantine_queue at 0x0000018C17ED9FB0, file "app\services\memory\queue.py", line 201>:
 201            RESUME                   0

 215            LOAD_GLOBAL              1 (isinstance + NULL)
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

 216    L1:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)
                LOAD_CONST               1 ('list_quarantine_queue dropped | reason=missing_brokerage_id')
                CALL                     1
                POP_TOP

 217            BUILD_LIST               0
                RETURN_VALUE

 219    L2:     LOAD_GLOBAL             11 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         1 (limit)
                CALL                     1
                STORE_FAST               2 (capped)

 221            NOP

 222    L3:     LOAD_GLOBAL             13 (_get_db + NULL)
                CALL                     0
                STORE_FAST               3 (db)

 224            LOAD_FAST_BORROW         3 (db)
                LOAD_ATTR               15 (table + NULL|self)
                LOAD_GLOBAL             16 (_TABLE)
                CALL                     1

 225            LOAD_ATTR               19 (select + NULL|self)
                LOAD_CONST               2 ('*')
                CALL                     1

 226            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST               3 ('brokerage_id')
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                CALL                     2

 227            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST               4 ('status')
                LOAD_GLOBAL             22 (MemoryStatus)
                LOAD_ATTR               24 (QUARANTINED)
                LOAD_ATTR               26 (value)
                CALL                     2

 228            LOAD_ATTR               29 (order + NULL|self)
                LOAD_CONST               5 ('created_at')
                LOAD_CONST               6 (True)
                LOAD_CONST               7 (('desc',))
                CALL_KW                  2

 229            LOAD_ATTR               31 (limit + NULL|self)
                LOAD_FAST_BORROW         2 (capped)
                CALL                     1

 223            STORE_FAST               4 (q)

 231            LOAD_FAST_BORROW         4 (q)
                LOAD_ATTR               33 (execute + NULL|self)
                CALL                     0
                STORE_FAST               5 (result)

 232            LOAD_GLOBAL             35 (list + NULL)
                LOAD_GLOBAL             37 (getattr + NULL)
                LOAD_FAST_BORROW         5 (result)
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
        L5:     RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 233            LOAD_GLOBAL             38 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       59 (to L11)
                NOT_TAKEN
                STORE_FAST               6 (e)

 234    L7:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 235            LOAD_CONST              10 ('list_quarantine_queue failed (non-critical) | brokerage=')

 236            LOAD_FAST                0 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST              11 (' | error_type=')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE

 235            BUILD_STRING             4

 234            CALL                     1
                POP_TOP

 238            BUILD_LIST               0
        L8:     SWAP                     2
        L9:     POP_EXCEPT
                LOAD_CONST               9 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --   L10:     LOAD_CONST               9 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 233   L11:     RERAISE                  0

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L6 [0]
  L6 to L7 -> L12 [1] lasti
  L7 to L8 -> L10 [1] lasti
  L8 to L9 -> L12 [1] lasti
  L10 to L12 -> L12 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app\services\memory\queue.py", line 245>:
245           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

246           LOAD_CONST               2 ('str')

245           LOAD_CONST               3 ('within_days')

248           LOAD_CONST               4 ('int')

245           LOAD_CONST               5 ('limit')

249           LOAD_CONST               4 ('int')

245           LOAD_CONST               6 ('return')

250           LOAD_CONST               7 ('List[Dict[str, Any]]')

245           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object list_expiring_memory at 0x0000018C177AE550, file "app\services\memory\queue.py", line 245>:
 245            RESUME                   0

 261            LOAD_GLOBAL              1 (isinstance + NULL)
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

 262    L1:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)
                LOAD_CONST               1 ('list_expiring_memory dropped | reason=missing_brokerage_id')
                CALL                     1
                POP_TOP

 263            BUILD_LIST               0
                RETURN_VALUE

 265    L2:     LOAD_GLOBAL             11 (_within_days + NULL)
                LOAD_FAST_BORROW         1 (within_days)
                CALL                     1
                STORE_FAST               3 (window_days)

 266            LOAD_GLOBAL             13 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1
                STORE_FAST               4 (capped)

 267            LOAD_GLOBAL             15 (_now + NULL)
                CALL                     0
                STORE_FAST               5 (now)

 268            LOAD_FAST_BORROW         5 (now)
                LOAD_GLOBAL             17 (timedelta + NULL)
                LOAD_FAST_BORROW         3 (window_days)
                LOAD_CONST               2 (('days',))
                CALL_KW                  1
                BINARY_OP                0 (+)
                STORE_FAST               6 (deadline)

 270            NOP

 271    L3:     LOAD_GLOBAL             19 (_get_db + NULL)
                CALL                     0
                STORE_FAST               7 (db)

 273            LOAD_FAST_BORROW         7 (db)
                LOAD_ATTR               21 (table + NULL|self)
                LOAD_GLOBAL             22 (_TABLE)
                CALL                     1

 274            LOAD_ATTR               25 (select + NULL|self)
                LOAD_CONST               3 ('*')
                CALL                     1

 275            LOAD_ATTR               27 (eq + NULL|self)
                LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                CALL                     2

 276            LOAD_ATTR               27 (eq + NULL|self)
                LOAD_CONST               5 ('status')
                LOAD_GLOBAL             28 (MemoryStatus)
                LOAD_ATTR               30 (APPROVED)
                LOAD_ATTR               32 (value)
                CALL                     2

 277            LOAD_ATTR               35 (order + NULL|self)
                LOAD_CONST               6 ('expires_at')
                LOAD_CONST               7 (False)
                LOAD_CONST               8 (('desc',))
                CALL_KW                  2

 278            LOAD_ATTR               37 (limit + NULL|self)
                LOAD_FAST_BORROW         4 (capped)
                CALL                     1

 272            STORE_FAST               8 (q)

 280            LOAD_FAST_BORROW         8 (q)
                LOAD_ATTR               39 (execute + NULL|self)
                CALL                     0
                STORE_FAST               9 (result)

 281            LOAD_GLOBAL             41 (list + NULL)
                LOAD_GLOBAL             43 (getattr + NULL)
                LOAD_FAST_BORROW         9 (result)
                LOAD_CONST               9 ('data')
                LOAD_CONST              10 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L4:     CALL                     1
                STORE_FAST              10 (rows)

 292    L5:     BUILD_LIST               0
                STORE_FAST              12 (out)

 293            LOAD_FAST               10 (rows)
                GET_ITER
        L6:     FOR_ITER               170 (to L14)
                STORE_FAST              13 (r)

 294            LOAD_FAST               13 (r)
                LOAD_ATTR               51 (get + NULL|self)
                LOAD_CONST               6 ('expires_at')
                CALL                     1
                STORE_FAST              14 (exp)

 295            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST               14 (exp)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        9 (to L7)
                NOT_TAKEN
                LOAD_FAST               14 (exp)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN

 298    L7:     JUMP_BACKWARD           52 (to L6)

 299    L8:     NOP

 300    L9:     LOAD_GLOBAL             52 (datetime)
                LOAD_ATTR               54 (fromisoformat)
                PUSH_NULL
                LOAD_FAST               14 (exp)
                LOAD_ATTR               57 (replace + NULL|self)
                LOAD_CONST              13 ('Z')
                LOAD_CONST              14 ('+00:00')
                CALL                     2
                CALL                     1
                STORE_FAST              15 (expires_at)

 303   L10:     LOAD_FAST               15 (expires_at)
                LOAD_ATTR               60 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L11)
                NOT_TAKEN

 304            LOAD_FAST               15 (expires_at)
                LOAD_ATTR               57 (replace + NULL|self)
                LOAD_GLOBAL             62 (timezone)
                LOAD_ATTR               64 (utc)
                LOAD_CONST              15 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST              15 (expires_at)

 305   L11:     LOAD_FAST_LOAD_FAST    245 (expires_at, now)
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN

 306            JUMP_BACKWARD          145 (to L6)

 307   L12:     LOAD_FAST_LOAD_FAST    246 (expires_at, deadline)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN

 308            JUMP_BACKWARD          153 (to L6)

 309   L13:     LOAD_FAST               12 (out)
                LOAD_ATTR               67 (append + NULL|self)
                LOAD_FAST               13 (r)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          172 (to L6)

 293   L14:     END_FOR
                POP_ITER

 310            LOAD_FAST               12 (out)
                RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 282            LOAD_GLOBAL             44 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       59 (to L20)
                NOT_TAKEN
                STORE_FAST              11 (e)

 283   L16:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 284            LOAD_CONST              11 ('list_expiring_memory failed (non-critical) | brokerage=')

 285            LOAD_FAST                0 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST              12 (' | error_type=')
                LOAD_GLOBAL             47 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               48 (__name__)
                FORMAT_SIMPLE

 284            BUILD_STRING             4

 283            CALL                     1
                POP_TOP

 287            BUILD_LIST               0
       L17:     SWAP                     2
       L18:     POP_EXCEPT
                LOAD_CONST              10 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RETURN_VALUE

  --   L19:     LOAD_CONST              10 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 282   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L22:     PUSH_EXC_INFO

 301            LOAD_GLOBAL             58 (ValueError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L24)
                NOT_TAKEN
                POP_TOP

 302   L23:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD          263 (to L6)

 301   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L15 [0]
  L9 to L10 -> L22 [1]
  L15 to L16 -> L21 [1] lasti
  L16 to L17 -> L19 [1] lasti
  L17 to L18 -> L21 [1] lasti
  L19 to L21 -> L21 [1] lasti
  L22 to L23 -> L25 [2] lasti
  L24 to L25 -> L25 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "app\services\memory\queue.py", line 317>:
317           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

318           LOAD_CONST               2 ('str')

317           LOAD_CONST               3 ('kind')

320           LOAD_CONST               4 ('Union[None, str, MemoryKind]')

317           LOAD_CONST               5 ('limit')

321           LOAD_CONST               6 ('int')

317           LOAD_CONST               7 ('return')

322           LOAD_CONST               8 ('List[Dict[str, Any]]')

317           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object list_approved_memory at 0x0000018C17ED68D0, file "app\services\memory\queue.py", line 317>:
 317            RESUME                   0

 338            LOAD_GLOBAL              1 (isinstance + NULL)
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

 339    L1:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)
                LOAD_CONST               1 ('list_approved_memory dropped | reason=missing_brokerage_id')
                CALL                     1
                POP_TOP

 340            BUILD_LIST               0
                RETURN_VALUE

 342    L2:     LOAD_GLOBAL             11 (_coerce_kind + NULL)
                LOAD_FAST_BORROW         1 (kind)
                CALL                     1
                STORE_FAST               3 (kind_value)

 343            LOAD_GLOBAL             13 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1
                STORE_FAST               4 (capped)

 344            LOAD_GLOBAL             15 (_now + NULL)
                CALL                     0
                STORE_FAST               5 (now)

 346            NOP

 347    L3:     LOAD_GLOBAL             17 (_get_db + NULL)
                CALL                     0
                STORE_FAST               6 (db)

 349            LOAD_FAST_BORROW         6 (db)
                LOAD_ATTR               19 (table + NULL|self)
                LOAD_GLOBAL             20 (_TABLE)
                CALL                     1

 350            LOAD_ATTR               23 (select + NULL|self)
                LOAD_CONST               2 ('*')
                CALL                     1

 351            LOAD_ATTR               25 (eq + NULL|self)
                LOAD_CONST               3 ('brokerage_id')
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                CALL                     2

 352            LOAD_ATTR               25 (eq + NULL|self)
                LOAD_CONST               4 ('status')
                LOAD_GLOBAL             26 (MemoryStatus)
                LOAD_ATTR               28 (APPROVED)
                LOAD_ATTR               30 (value)
                CALL                     2

 348            STORE_FAST               7 (q)

 354            LOAD_FAST_BORROW         3 (kind_value)
                POP_JUMP_IF_NONE        19 (to L4)
                NOT_TAKEN

 355            LOAD_FAST_BORROW         7 (q)
                LOAD_ATTR               25 (eq + NULL|self)
                LOAD_CONST               6 ('kind')
                LOAD_FAST_BORROW         3 (kind_value)
                CALL                     2
                STORE_FAST               7 (q)

 356    L4:     LOAD_FAST_BORROW         7 (q)
                LOAD_ATTR               33 (order + NULL|self)
                LOAD_CONST               7 ('confidence')
                LOAD_CONST               8 (True)
                LOAD_CONST               9 (('desc',))
                CALL_KW                  2
                STORE_FAST               7 (q)

 357            LOAD_FAST_BORROW         7 (q)
                LOAD_ATTR               33 (order + NULL|self)
                LOAD_CONST              10 ('created_at')
                LOAD_CONST               8 (True)
                LOAD_CONST               9 (('desc',))
                CALL_KW                  2
                STORE_FAST               7 (q)

 358            LOAD_FAST_BORROW         7 (q)
                LOAD_ATTR               35 (limit + NULL|self)
                LOAD_FAST_BORROW         4 (capped)
                CALL                     1
                STORE_FAST               7 (q)

 359            LOAD_FAST_BORROW         7 (q)
                LOAD_ATTR               37 (execute + NULL|self)
                CALL                     0
                STORE_FAST               8 (result)

 360            LOAD_GLOBAL             39 (list + NULL)
                LOAD_GLOBAL             41 (getattr + NULL)
                LOAD_FAST_BORROW         8 (result)
                LOAD_CONST              11 ('data')
                LOAD_CONST               5 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                BUILD_LIST               0
        L7:     CALL                     1
                STORE_FAST               9 (rows)

 374    L8:     BUILD_LIST               0
                STORE_FAST              11 (out)

 376            LOAD_GLOBAL             26 (MemoryStatus)
                LOAD_ATTR               48 (EXPIRED)
                LOAD_ATTR               30 (value)

 377            LOAD_GLOBAL             26 (MemoryStatus)
                LOAD_ATTR               50 (REJECTED)
                LOAD_ATTR               30 (value)

 378            LOAD_GLOBAL             26 (MemoryStatus)
                LOAD_ATTR               52 (QUARANTINED)
                LOAD_ATTR               30 (value)

 375            BUILD_SET                3
                STORE_FAST              12 (excluded_statuses)

 380            LOAD_FAST                9 (rows)
                GET_ITER
        L9:     FOR_ITER               188 (to L15)
                STORE_FAST              13 (r)

 381            LOAD_FAST               13 (r)
                LOAD_ATTR               55 (get + NULL|self)
                LOAD_CONST               4 ('status')
                CALL                     1
                LOAD_FAST               12 (excluded_statuses)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN

 382            JUMP_BACKWARD           27 (to L9)

 383   L10:     LOAD_FAST               13 (r)
                LOAD_ATTR               55 (get + NULL|self)
                LOAD_CONST              14 ('expires_at')
                CALL                     1
                STORE_FAST              14 (exp)

 384            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST               14 (exp)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      106 (to L14)
                NOT_TAKEN
                LOAD_FAST               14 (exp)
                TO_BOOL
                POP_JUMP_IF_FALSE       98 (to L14)
                NOT_TAKEN

 385            NOP

 386   L11:     LOAD_GLOBAL             56 (datetime)
                LOAD_ATTR               58 (fromisoformat)
                PUSH_NULL
                LOAD_FAST               14 (exp)
                LOAD_ATTR               61 (replace + NULL|self)
                LOAD_CONST              15 ('Z')
                LOAD_CONST              16 ('+00:00')
                CALL                     2
                CALL                     1
                STORE_FAST              15 (expires_at)

 389   L12:     LOAD_FAST               15 (expires_at)
                POP_JUMP_IF_NONE        55 (to L14)
                NOT_TAKEN

 390            LOAD_FAST               15 (expires_at)
                LOAD_ATTR               64 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L13)
                NOT_TAKEN

 391            LOAD_FAST               15 (expires_at)
                LOAD_ATTR               61 (replace + NULL|self)
                LOAD_GLOBAL             66 (timezone)
                LOAD_ATTR               68 (utc)
                LOAD_CONST              17 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST              15 (expires_at)

 392   L13:     LOAD_FAST_LOAD_FAST    245 (expires_at, now)
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN

 393            JUMP_BACKWARD          171 (to L9)

 394   L14:     LOAD_FAST               11 (out)
                LOAD_ATTR               71 (append + NULL|self)
                LOAD_FAST               13 (r)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          190 (to L9)

 380   L15:     END_FOR
                POP_ITER

 395            LOAD_FAST               11 (out)
                RETURN_VALUE

  --   L16:     PUSH_EXC_INFO

 361            LOAD_GLOBAL             42 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       59 (to L21)
                NOT_TAKEN
                STORE_FAST              10 (e)

 362   L17:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 363            LOAD_CONST              12 ('list_approved_memory failed (non-critical) | brokerage=')

 364            LOAD_FAST                0 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST              13 (' | error_type=')
                LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE

 363            BUILD_STRING             4

 362            CALL                     1
                POP_TOP

 366            BUILD_LIST               0
       L18:     SWAP                     2
       L19:     POP_EXCEPT
                LOAD_CONST               5 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RETURN_VALUE

  --   L20:     LOAD_CONST               5 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 361   L21:     RERAISE                  0

  --   L22:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L23:     PUSH_EXC_INFO

 387            LOAD_GLOBAL             62 (ValueError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L25)
                NOT_TAKEN
                POP_TOP

 388            LOAD_CONST               5 (None)
                STORE_FAST              15 (expires_at)
       L24:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 168 (to L12)

 387   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L16 [0]
  L6 to L8 -> L16 [0]
  L11 to L12 -> L23 [1]
  L16 to L17 -> L22 [1] lasti
  L17 to L18 -> L20 [1] lasti
  L18 to L19 -> L22 [1] lasti
  L20 to L22 -> L22 [1] lasti
  L23 to L24 -> L26 [2] lasti
  L25 to L26 -> L26 [2] lasti
```
