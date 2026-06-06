# memory/queries

- **pyc:** `app\services\memory\__pycache__\queries.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/queries.py`
- **co_filename (from bytecode):** `app\services\memory\queries.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144B — Tenant-scoped memory read helpers.

Read side of the memory store. Every public helper here REQUIRES a
``brokerage_id`` and scopes its query to that tenant. There is no
unscoped tenant helper; the only way to read across brokerages is the
explicitly named ``list_memory_admin_unscoped`` (server-to-server,
operator/audit use only — not an HTTP-exposed function).

Hard contract:
  * ``brokerage_id`` is mandatory on every tenant helper.
  * Caller-supplied ``limit`` is clamped to ``MAX_QUERY_LIMIT``.
  * Active queries exclude EXPIRED and (by default) future-only rows
    whose ``expires_at`` is in the past.
  * Returned rows are pass-through dicts from ``pas_memory_records``.
    The schema does not model raw transcript columns at all (see the
    PAS144A doctrine and the v10 migration), so there is nothing to
    strip — but we keep the rule explicit in the docstring.

Public surface:
  - list_memory_for_brokerage(brokerage_id, kind=None, status=None, limit=50)
  - get_memory_for_brokerage(memory_id, brokerage_id)
  - list_active_memory_for_brokerage(brokerage_id, kind=None, limit=50)
  - list_memory_admin_unscoped(kind=None, status=None, limit=50)
```

## Imports

`List`, `MemoryKind`, `MemoryStatus`, `Optional`, `Union`, `__future__`, `annotations`, `app.db.supabase_client`, `contracts`, `datetime`, `get_supabase`, `logging`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_limit`, `_coerce_kind`, `_coerce_status`, `_get_db`, `_now_iso`, `get_memory_for_brokerage`, `list_active_memory_for_brokerage`, `list_memory_admin_unscoped`, `list_memory_for_brokerage`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS144B — Tenant-scoped memory read helpers.\n\nRead side of the memory store. Every public helper here REQUIRES a\n``brokerage_id`` and scopes its query to that tenant. There is no\nunscoped tenant helper; the only way to read across brokerages is the\nexplicitly named ``list_memory_admin_unscoped`` (server-to-server,\noperator/audit use only — not an HTTP-exposed function).\n\nHard contract:\n  * ``brokerage_id`` is mandatory on every tenant helper.\n  * Caller-supplied ``limit`` is clamped to ``MAX_QUERY_LIMIT``.\n  * Active queries exclude EXPIRED and (by default) future-only rows\n    whose ``expires_at`` is in the past.\n  * Returned rows are pass-through dicts from ``pas_memory_records``.\n    The schema does not model raw transcript columns at all (see the\n    PAS144A doctrine and the v10 migration), so there is nothing to\n    strip — but we keep the rule explicit in the docstring.\n\nPublic surface:\n  - list_memory_for_brokerage(brokerage_id, kind=None, status=None, limit=50)\n  - get_memory_for_brokerage(memory_id, brokerage_id)\n  - list_active_memory_for_brokerage(brokerage_id, kind=None, limit=50)\n  - list_memory_admin_unscoped(kind=None, status=None, limit=50)\n'
- 'pas.memory.queries'
- 'pas_memory_records'
- 'kind'
- 'status'
- 'limit'
- 'Lazy Supabase resolver. Mirrors the pattern in store.py so unit\ntests can patch ``app.db.supabase_client.get_supabase``.'
- 'Union[None, str, MemoryKind]'
- 'return'
- 'Optional[str]'
- 'queries: ignoring unknown kind='
- 'Union[None, str, MemoryStatus]'
- 'queries: ignoring unknown status='
- 'Optional[int]'
- 'int'
- 'str'
- 'brokerage_id'
- 'List[dict]'
- 'Return memory rows for ``brokerage_id``, optionally filtered by\n``kind`` and ``status``. Limit is clamped to ``MAX_QUERY_LIMIT``.\n\nReturns ``[]`` on missing brokerage_id, on Supabase failure, or\nwhen no rows match. Never raises into the caller.\n'
- 'list_memory_for_brokerage dropped | reason=missing_brokerage_id'
- 'created_at'
- 'data'
- 'list_memory_for_brokerage failed (non-critical) | brokerage='
- ' | error_type='
- 'memory_id'
- 'Optional[dict]'
- "Fetch a single memory row by ``memory_id`` *scoped to*\n``brokerage_id``. Returns ``None`` when the row is missing or the\ntenant does not own it.\n\nThe scope is enforced by the WHERE clause itself — even if a\ncaller knows the global ``memory_id``, they cannot peek into\nanother brokerage's row through this helper.\n"
- 'get_memory_for_brokerage dropped | reason=invalid_memory_id'
- 'get_memory_for_brokerage dropped | reason=missing_brokerage_id'
- 'get_memory_for_brokerage failed (non-critical) | memory_id='
- 'Return *active* memory rows for ``brokerage_id``.\n\n"Active" means:\n  * status NOT IN (EXPIRED, REJECTED, QUARANTINED)\n  * expires_at IS NULL OR expires_at > NOW()\n\nThe runtime should consume only active memory when shaping calls;\nQUARANTINED rows are visible only via ``list_memory_for_brokerage``\n(which is the operator-review surface).\n'
- 'list_active_memory_for_brokerage dropped | reason=missing_brokerage_id'
- 'expires_at.is.null,expires_at.gt.'
- 'confidence'
- 'expires_at'
- '+00:00'
- 'list_active_memory_for_brokerage failed (non-critical) | brokerage='
- 'Cross-tenant read for operator audits / DANGEROUS-row review.\n\nNAMED EXPLICITLY so a code reviewer cannot miss it. Never wire this\ninto any tenant-facing route. There is no implicit "list all\nmemory" — callers must reach for *this* function deliberately.\n\nReturns ``[]`` on Supabase failure.\n'
- 'list_memory_admin_unscoped failed (non-critical) | error_type='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS144B — Tenant-scoped memory read helpers.\n\nRead side of the memory store. Every public helper here REQUIRES a\n``brokerage_id`` and scopes its query to that tenant. There is no\nunscoped tenant helper; the only way to read across brokerages is the\nexplicitly named ``list_memory_admin_unscoped`` (server-to-server,\noperator/audit use only — not an HTTP-exposed function).\n\nHard contract:\n  * ``brokerage_id`` is mandatory on every tenant helper.\n  * Caller-supplied ``limit`` is clamped to ``MAX_QUERY_LIMIT``.\n  * Active queries exclude EXPIRED and (by default) future-only rows\n    whose ``expires_at`` is in the past.\n  * Returned rows are pass-through dicts from ``pas_memory_records``.\n    The schema does not model raw transcript columns at all (see the\n    PAS144A doctrine and the v10 migration), so there is nothing to\n    strip — but we keep the rule explicit in the docstring.\n\nPublic surface:\n  - list_memory_for_brokerage(brokerage_id, kind=None, status=None, limit=50)\n  - get_memory_for_brokerage(memory_id, brokerage_id)\n  - list_active_memory_for_brokerage(brokerage_id, kind=None, limit=50)\n  - list_memory_admin_unscoped(kind=None, status=None, limit=50)\n')
              STORE_NAME               0 (__doc__)

 27           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 29           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 30           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timezone'))
              IMPORT_NAME              4 (datetime)
              IMPORT_FROM              4 (datetime)
              STORE_NAME               4 (datetime)
              IMPORT_FROM              5 (timezone)
              STORE_NAME               5 (timezone)
              POP_TOP

 31           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('List', 'Optional', 'Union'))
              IMPORT_NAME              6 (typing)
              IMPORT_FROM              7 (List)
              STORE_NAME               7 (List)
              IMPORT_FROM              8 (Optional)
              STORE_NAME               8 (Optional)
              IMPORT_FROM              9 (Union)
              STORE_NAME               9 (Union)
              POP_TOP

 33           LOAD_SMALL_INT           1
              LOAD_CONST               5 (('MemoryKind', 'MemoryStatus'))
              IMPORT_NAME             10 (contracts)
              IMPORT_FROM             11 (MemoryKind)
              STORE_NAME              11 (MemoryKind)
              IMPORT_FROM             12 (MemoryStatus)
              STORE_NAME              12 (MemoryStatus)
              POP_TOP

 35           LOAD_NAME                3 (logging)
              LOAD_ATTR               26 (getLogger)
              PUSH_NULL
              LOAD_CONST               6 ('pas.memory.queries')
              CALL                     1
              STORE_NAME              14 (logger)

 38           LOAD_CONST               7 ('pas_memory_records')
              STORE_NAME              15 (_TABLE)

 43           LOAD_SMALL_INT         200
              STORE_NAME              16 (MAX_QUERY_LIMIT)

 44           LOAD_SMALL_INT          50
              STORE_NAME              17 (DEFAULT_QUERY_LIMIT)

 51           LOAD_CONST               8 (<code object _get_db at 0x0000018C17FA34B0, file "app\services\memory\queries.py", line 51>)
              MAKE_FUNCTION
              STORE_NAME              18 (_get_db)

 58           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\queries.py", line 58>)
              MAKE_FUNCTION
              LOAD_CONST              10 (<code object _coerce_kind at 0x0000018C17FEDA30, file "app\services\memory\queries.py", line 58>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              19 (_coerce_kind)

 73           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\queries.py", line 73>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object _coerce_status at 0x0000018C17FEDC30, file "app\services\memory\queries.py", line 73>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              20 (_coerce_status)

 87           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA2E20, file "app\services\memory\queries.py", line 87>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object _clamp_limit at 0x0000018C17FF0DB0, file "app\services\memory\queries.py", line 87>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (_clamp_limit)

 99           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA21F0, file "app\services\memory\queries.py", line 99>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _now_iso at 0x0000018C18038B70, file "app\services\memory\queries.py", line 99>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (_now_iso)

107           LOAD_CONST              17 ('kind')

110           LOAD_CONST               2 (None)

107           LOAD_CONST              18 ('status')

111           LOAD_CONST               2 (None)

107           LOAD_CONST              19 ('limit')

112           LOAD_NAME               17 (DEFAULT_QUERY_LIMIT)

107           BUILD_MAP                3
              LOAD_CONST              20 (<code object __annotate__ at 0x0000018C18025730, file "app\services\memory\queries.py", line 107>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object list_memory_for_brokerage at 0x0000018C17F846F0, file "app\services\memory\queries.py", line 107>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              23 (list_memory_for_brokerage)

146           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18025E30, file "app\services\memory\queries.py", line 146>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object get_memory_for_brokerage at 0x0000018C17D51540, file "app\services\memory\queries.py", line 146>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (get_memory_for_brokerage)

184           LOAD_CONST              17 ('kind')

187           LOAD_CONST               2 (None)

184           LOAD_CONST              19 ('limit')

188           LOAD_NAME               17 (DEFAULT_QUERY_LIMIT)

184           BUILD_MAP                2
              LOAD_CONST              24 (<code object __annotate__ at 0x0000018C18025830, file "app\services\memory\queries.py", line 184>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object list_active_memory_for_brokerage at 0x0000018C17E942E0, file "app\services\memory\queries.py", line 184>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              25 (list_active_memory_for_brokerage)

269           LOAD_CONST              17 ('kind')

271           LOAD_CONST               2 (None)

269           LOAD_CONST              18 ('status')

272           LOAD_CONST               2 (None)

269           LOAD_CONST              19 ('limit')

273           LOAD_NAME               17 (DEFAULT_QUERY_LIMIT)

269           BUILD_MAP                3
              LOAD_CONST              26 (<code object __annotate__ at 0x0000018C18024D30, file "app\services\memory\queries.py", line 269>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object list_memory_admin_unscoped at 0x0000018C17E94A90, file "app\services\memory\queries.py", line 269>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              26 (list_memory_admin_unscoped)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object _get_db at 0x0000018C17FA34B0, file "app\services\memory\queries.py", line 51>:
 51           RESUME                   0

 54           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('get_supabase',))
              IMPORT_NAME              0 (app.db.supabase_client)
              IMPORT_FROM              1 (get_supabase)
              STORE_FAST               0 (get_supabase)
              POP_TOP

 55           LOAD_FAST_BORROW         0 (get_supabase)
              PUSH_NULL
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\queries.py", line 58>:
 58           RESUME                   0
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

Disassembly of <code object _coerce_kind at 0x0000018C17FEDA30, file "app\services\memory\queries.py", line 58>:
  58           RESUME                   0

  59           LOAD_FAST_BORROW         0 (kind)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

  60           LOAD_CONST               0 (None)
               RETURN_VALUE

  61   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (kind)
               LOAD_GLOBAL              2 (MemoryKind)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       13 (to L2)
               NOT_TAKEN

  62           LOAD_FAST_BORROW         0 (kind)
               LOAD_ATTR                4 (value)
               RETURN_VALUE

  63   L2:     LOAD_GLOBAL              1 (isinstance + NULL)
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

  65           NOP

  66   L3:     LOAD_GLOBAL              3 (MemoryKind + NULL)
               LOAD_FAST_BORROW         0 (kind)
               CALL                     1
               LOAD_ATTR                4 (value)
       L4:     RETURN_VALUE

  70   L5:     LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  67           LOAD_GLOBAL             10 (ValueError)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       30 (to L8)
               NOT_TAKEN
               POP_TOP

  68           LOAD_GLOBAL             12 (logger)
               LOAD_ATTR               15 (warning + NULL|self)
               LOAD_CONST               1 ('queries: ignoring unknown kind=')
               LOAD_FAST                0 (kind)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

  69   L7:     POP_EXCEPT
               LOAD_CONST               0 (None)
               RETURN_VALUE

  67   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L3 to L4 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\queries.py", line 73>:
 73           RESUME                   0
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

Disassembly of <code object _coerce_status at 0x0000018C17FEDC30, file "app\services\memory\queries.py", line 73>:
  73           RESUME                   0

  74           LOAD_FAST_BORROW         0 (status)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

  75           LOAD_CONST               0 (None)
               RETURN_VALUE

  76   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (status)
               LOAD_GLOBAL              2 (MemoryStatus)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       13 (to L2)
               NOT_TAKEN

  77           LOAD_FAST_BORROW         0 (status)
               LOAD_ATTR                4 (value)
               RETURN_VALUE

  78   L2:     LOAD_GLOBAL              1 (isinstance + NULL)
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

  79           NOP

  80   L3:     LOAD_GLOBAL              3 (MemoryStatus + NULL)
               LOAD_FAST_BORROW         0 (status)
               CALL                     1
               LOAD_ATTR                4 (value)
       L4:     RETURN_VALUE

  84   L5:     LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  81           LOAD_GLOBAL             10 (ValueError)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       30 (to L8)
               NOT_TAKEN
               POP_TOP

  82           LOAD_GLOBAL             12 (logger)
               LOAD_ATTR               15 (warning + NULL|self)
               LOAD_CONST               1 ('queries: ignoring unknown status=')
               LOAD_FAST                0 (status)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

  83   L7:     POP_EXCEPT
               LOAD_CONST               0 (None)
               RETURN_VALUE

  81   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L3 to L4 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app\services\memory\queries.py", line 87>:
 87           RESUME                   0
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

Disassembly of <code object _clamp_limit at 0x0000018C17FF0DB0, file "app\services\memory\queries.py", line 87>:
  87           RESUME                   0

  88           LOAD_FAST_BORROW         0 (limit)
               POP_JUMP_IF_NOT_NONE     7 (to L1)
               NOT_TAKEN

  89           LOAD_GLOBAL              0 (DEFAULT_QUERY_LIMIT)
               RETURN_VALUE

  90   L1:     NOP

  91   L2:     LOAD_GLOBAL              3 (int + NULL)
               LOAD_FAST_BORROW         0 (limit)
               CALL                     1
               STORE_FAST               1 (n)

  94   L3:     LOAD_FAST                1 (n)
               LOAD_SMALL_INT           0
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

  95           LOAD_GLOBAL              0 (DEFAULT_QUERY_LIMIT)
               RETURN_VALUE

  96   L4:     LOAD_GLOBAL              9 (min + NULL)
               LOAD_FAST                1 (n)
               LOAD_GLOBAL             10 (MAX_QUERY_LIMIT)
               CALL                     2
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

  92           LOAD_GLOBAL              4 (TypeError)
               LOAD_GLOBAL              6 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

  93           LOAD_GLOBAL              0 (DEFAULT_QUERY_LIMIT)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

  92   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app\services\memory\queries.py", line 99>:
 99           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038B70, file "app\services\memory\queries.py", line 99>:
 99           RESUME                   0

100           LOAD_GLOBAL              0 (datetime)
              LOAD_ATTR                2 (now)
              PUSH_NULL
              LOAD_GLOBAL              4 (timezone)
              LOAD_ATTR                6 (utc)
              CALL                     1
              LOAD_ATTR                9 (isoformat + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app\services\memory\queries.py", line 107>:
107           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

108           LOAD_CONST               2 ('str')

107           LOAD_CONST               3 ('kind')

110           LOAD_CONST               4 ('Union[None, str, MemoryKind]')

107           LOAD_CONST               5 ('status')

111           LOAD_CONST               6 ('Union[None, str, MemoryStatus]')

107           LOAD_CONST               7 ('limit')

112           LOAD_CONST               8 ('int')

107           LOAD_CONST               9 ('return')

113           LOAD_CONST              10 ('List[dict]')

107           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object list_memory_for_brokerage at 0x0000018C17F846F0, file "app\services\memory\queries.py", line 107>:
 107            RESUME                   0

 120            LOAD_GLOBAL              1 (isinstance + NULL)
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

 121    L1:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)
                LOAD_CONST               1 ('list_memory_for_brokerage dropped | reason=missing_brokerage_id')
                CALL                     1
                POP_TOP

 122            BUILD_LIST               0
                RETURN_VALUE

 124    L2:     LOAD_GLOBAL             11 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         3 (limit)
                CALL                     1
                STORE_FAST               4 (capped)

 125            LOAD_GLOBAL             13 (_coerce_kind + NULL)
                LOAD_FAST_BORROW         1 (kind)
                CALL                     1
                STORE_FAST               5 (kind_value)

 126            LOAD_GLOBAL             15 (_coerce_status + NULL)
                LOAD_FAST_BORROW         2 (status)
                CALL                     1
                STORE_FAST               6 (status_value)

 128            NOP

 129    L3:     LOAD_GLOBAL             17 (_get_db + NULL)
                CALL                     0
                STORE_FAST               7 (db)

 130            LOAD_FAST_BORROW         7 (db)
                LOAD_ATTR               19 (table + NULL|self)
                LOAD_GLOBAL             20 (_TABLE)
                CALL                     1
                LOAD_ATTR               23 (select + NULL|self)
                LOAD_CONST               2 ('*')
                CALL                     1
                LOAD_ATTR               25 (eq + NULL|self)
                LOAD_CONST               3 ('brokerage_id')
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     2
                STORE_FAST               8 (q)

 131            LOAD_FAST_BORROW         5 (kind_value)
                POP_JUMP_IF_NONE        19 (to L4)
                NOT_TAKEN

 132            LOAD_FAST_BORROW         8 (q)
                LOAD_ATTR               25 (eq + NULL|self)
                LOAD_CONST               5 ('kind')
                LOAD_FAST_BORROW         5 (kind_value)
                CALL                     2
                STORE_FAST               8 (q)

 133    L4:     LOAD_FAST_BORROW         6 (status_value)
                POP_JUMP_IF_NONE        19 (to L5)
                NOT_TAKEN

 134            LOAD_FAST_BORROW         8 (q)
                LOAD_ATTR               25 (eq + NULL|self)
                LOAD_CONST               6 ('status')
                LOAD_FAST_BORROW         6 (status_value)
                CALL                     2
                STORE_FAST               8 (q)

 135    L5:     LOAD_FAST_BORROW         8 (q)
                LOAD_ATTR               27 (order + NULL|self)
                LOAD_CONST               7 ('created_at')
                LOAD_CONST               8 (True)
                LOAD_CONST               9 (('desc',))
                CALL_KW                  2
                LOAD_ATTR               29 (limit + NULL|self)
                LOAD_FAST_BORROW         4 (capped)
                CALL                     1
                STORE_FAST               8 (q)

 136            LOAD_FAST_BORROW         8 (q)
                LOAD_ATTR               31 (execute + NULL|self)
                CALL                     0
                STORE_FAST               9 (result)

 137            LOAD_GLOBAL             33 (list + NULL)
                LOAD_GLOBAL             35 (getattr + NULL)
                LOAD_FAST_BORROW         9 (result)
                LOAD_CONST              10 ('data')
                LOAD_CONST               4 (None)
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

 138            LOAD_GLOBAL             36 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       59 (to L15)
                NOT_TAKEN
                STORE_FAST              10 (e)

 139   L11:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 140            LOAD_CONST              11 ('list_memory_for_brokerage failed (non-critical) | brokerage=')

 141            LOAD_FAST                0 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST              12 (' | error_type=')
                LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)
                FORMAT_SIMPLE

 140            BUILD_STRING             4

 139            CALL                     1
                POP_TOP

 143            BUILD_LIST               0
       L12:     SWAP                     2
       L13:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RETURN_VALUE

  --   L14:     LOAD_CONST               4 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 138   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L6 -> L10 [0]
  L7 to L9 -> L10 [0]
  L10 to L11 -> L16 [1] lasti
  L11 to L12 -> L14 [1] lasti
  L12 to L13 -> L16 [1] lasti
  L14 to L16 -> L16 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app\services\memory\queries.py", line 146>:
146           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('memory_id')

147           LOAD_CONST               2 ('str')

146           LOAD_CONST               3 ('brokerage_id')

147           LOAD_CONST               2 ('str')

146           LOAD_CONST               4 ('return')

148           LOAD_CONST               5 ('Optional[dict]')

146           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object get_memory_for_brokerage at 0x0000018C17D51540, file "app\services\memory\queries.py", line 146>:
 146            RESUME                   0

 157            LOAD_GLOBAL              1 (isinstance + NULL)
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
                POP_JUMP_IF_TRUE        24 (to L2)
                NOT_TAKEN

 158    L1:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)
                LOAD_CONST               1 ('get_memory_for_brokerage dropped | reason=invalid_memory_id')
                CALL                     1
                POP_TOP

 159            LOAD_CONST               2 (None)
                RETURN_VALUE

 160    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
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
                POP_JUMP_IF_TRUE        24 (to L4)
                NOT_TAKEN

 161    L3:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)
                LOAD_CONST               3 ('get_memory_for_brokerage dropped | reason=missing_brokerage_id')
                CALL                     1
                POP_TOP

 162            LOAD_CONST               2 (None)
                RETURN_VALUE

 164    L4:     NOP

 165    L5:     LOAD_GLOBAL             11 (_get_db + NULL)
                CALL                     0
                STORE_FAST               2 (db)

 167            LOAD_FAST_BORROW         2 (db)
                LOAD_ATTR               13 (table + NULL|self)
                LOAD_GLOBAL             14 (_TABLE)
                CALL                     1

 168            LOAD_ATTR               17 (select + NULL|self)
                LOAD_CONST               4 ('*')
                CALL                     1

 169            LOAD_ATTR               19 (eq + NULL|self)
                LOAD_CONST               5 ('memory_id')
                LOAD_FAST_BORROW         0 (memory_id)
                CALL                     2

 170            LOAD_ATTR               19 (eq + NULL|self)
                LOAD_CONST               6 ('brokerage_id')
                LOAD_FAST_BORROW         1 (brokerage_id)
                CALL                     2

 171            LOAD_ATTR               21 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 172            LOAD_ATTR               23 (execute + NULL|self)
                CALL                     0

 166            STORE_FAST               3 (result)

 174            LOAD_GLOBAL             25 (getattr + NULL)
                LOAD_FAST_BORROW         3 (result)
                LOAD_CONST               7 ('data')
                LOAD_CONST               2 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                BUILD_LIST               0
        L8:     STORE_FAST               4 (rows)

 175            LOAD_FAST_BORROW         4 (rows)
                TO_BOOL
                POP_JUMP_IF_FALSE       10 (to L12)
        L9:     NOT_TAKEN
       L10:     LOAD_FAST_BORROW         4 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
       L11:     RETURN_VALUE
       L12:     LOAD_CONST               2 (None)
       L13:     RETURN_VALUE

  --   L14:     PUSH_EXC_INFO

 176            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       58 (to L18)
                NOT_TAKEN
                STORE_FAST               5 (e)

 177   L15:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 178            LOAD_CONST               8 ('get_memory_for_brokerage failed (non-critical) | memory_id=')

 179            LOAD_FAST                0 (memory_id)
                FORMAT_SIMPLE
                LOAD_CONST               9 (' | error_type=')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 178            BUILD_STRING             4

 177            CALL                     1
                POP_TOP

 181   L16:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L17:     LOAD_CONST               2 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 176   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L14 [0]
  L7 to L9 -> L14 [0]
  L10 to L11 -> L14 [0]
  L12 to L13 -> L14 [0]
  L14 to L15 -> L19 [1] lasti
  L15 to L16 -> L17 [1] lasti
  L17 to L19 -> L19 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025830, file "app\services\memory\queries.py", line 184>:
184           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

185           LOAD_CONST               2 ('str')

184           LOAD_CONST               3 ('kind')

187           LOAD_CONST               4 ('Union[None, str, MemoryKind]')

184           LOAD_CONST               5 ('limit')

188           LOAD_CONST               6 ('int')

184           LOAD_CONST               7 ('return')

189           LOAD_CONST               8 ('List[dict]')

184           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object list_active_memory_for_brokerage at 0x0000018C17E942E0, file "app\services\memory\queries.py", line 184>:
 184            RESUME                   0

 200            LOAD_GLOBAL              1 (isinstance + NULL)
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

 201    L1:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 202            LOAD_CONST               1 ('list_active_memory_for_brokerage dropped | reason=missing_brokerage_id')

 201            CALL                     1
                POP_TOP

 204            BUILD_LIST               0
                RETURN_VALUE

 206    L2:     LOAD_GLOBAL             11 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1
                STORE_FAST               3 (capped)

 207            LOAD_GLOBAL             13 (_coerce_kind + NULL)
                LOAD_FAST_BORROW         1 (kind)
                CALL                     1
                STORE_FAST               4 (kind_value)

 209            NOP

 210    L3:     LOAD_GLOBAL             15 (_get_db + NULL)
                CALL                     0
                STORE_FAST               5 (db)

 211            LOAD_FAST_BORROW         5 (db)
                LOAD_ATTR               17 (table + NULL|self)
                LOAD_GLOBAL             18 (_TABLE)
                CALL                     1
                LOAD_ATTR               21 (select + NULL|self)
                LOAD_CONST               2 ('*')
                CALL                     1
                LOAD_ATTR               23 (eq + NULL|self)
                LOAD_CONST               3 ('brokerage_id')
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     2
                STORE_FAST               6 (q)

 212            LOAD_FAST_BORROW         4 (kind_value)
                POP_JUMP_IF_NONE        19 (to L4)
                NOT_TAKEN

 213            LOAD_FAST_BORROW         6 (q)
                LOAD_ATTR               23 (eq + NULL|self)
                LOAD_CONST               5 ('kind')
                LOAD_FAST_BORROW         4 (kind_value)
                CALL                     2
                STORE_FAST               6 (q)

 216    L4:     LOAD_CONST               6 ('(')
                LOAD_GLOBAL             24 (MemoryStatus)
                LOAD_ATTR               26 (EXPIRED)
                LOAD_ATTR               28 (value)
                FORMAT_SIMPLE
                LOAD_CONST               7 (',')

 217            LOAD_GLOBAL             24 (MemoryStatus)
                LOAD_ATTR               30 (REJECTED)
                LOAD_ATTR               28 (value)
                FORMAT_SIMPLE
                LOAD_CONST               7 (',')

 218            LOAD_GLOBAL             24 (MemoryStatus)
                LOAD_ATTR               32 (QUARANTINED)
                LOAD_ATTR               28 (value)
                FORMAT_SIMPLE
                LOAD_CONST               8 (')')

 216            BUILD_STRING             7

 215            STORE_FAST               7 (excluded_statuses)

 222            LOAD_FAST_BORROW         6 (q)
                LOAD_ATTR               34 (not_)
                LOAD_ATTR               37 (in_ + NULL|self)
                LOAD_CONST               9 ('status')

 223            LOAD_GLOBAL             24 (MemoryStatus)
                LOAD_ATTR               26 (EXPIRED)
                LOAD_ATTR               28 (value)

 224            LOAD_GLOBAL             24 (MemoryStatus)
                LOAD_ATTR               30 (REJECTED)
                LOAD_ATTR               28 (value)

 225            LOAD_GLOBAL             24 (MemoryStatus)
                LOAD_ATTR               32 (QUARANTINED)
                LOAD_ATTR               28 (value)

 222            BUILD_LIST               3
                CALL                     2
                STORE_FAST               6 (q)

 227            LOAD_FAST_BORROW         6 (q)
                LOAD_ATTR               39 (or_ + NULL|self)
                LOAD_CONST              10 ('expires_at.is.null,expires_at.gt.')
                LOAD_GLOBAL             41 (_now_iso + NULL)
                CALL                     0
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                STORE_FAST               6 (q)

 228            LOAD_FAST_BORROW         6 (q)
                LOAD_ATTR               43 (order + NULL|self)
                LOAD_CONST              11 ('confidence')
                LOAD_CONST              12 (True)
                LOAD_CONST              13 (('desc',))
                CALL_KW                  2
                LOAD_ATTR               45 (limit + NULL|self)
                LOAD_FAST_BORROW         3 (capped)
                CALL                     1
                STORE_FAST               6 (q)

 229            LOAD_FAST_BORROW         6 (q)
                LOAD_ATTR               47 (execute + NULL|self)
                CALL                     0
                STORE_FAST               8 (result)

 230            LOAD_GLOBAL             49 (list + NULL)
                LOAD_GLOBAL             51 (getattr + NULL)
                LOAD_FAST_BORROW         8 (result)
                LOAD_CONST              14 ('data')
                LOAD_CONST               4 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L5:     CALL                     1
                STORE_FAST               9 (rows)

 235            LOAD_GLOBAL             52 (datetime)
                LOAD_ATTR               54 (now)
                PUSH_NULL
                LOAD_GLOBAL             56 (timezone)
                LOAD_ATTR               58 (utc)
                CALL                     1
                STORE_FAST              10 (now)

 236            BUILD_LIST               0
                STORE_FAST              11 (out)

 237            LOAD_FAST_BORROW         9 (rows)
                GET_ITER
        L6:     EXTENDED_ARG             1
                FOR_ITER               264 (to L13)
                STORE_FAST              12 (r)

 238            LOAD_FAST_BORROW        12 (r)
                LOAD_ATTR               61 (get + NULL|self)
                LOAD_CONST               9 ('status')
                CALL                     1

 239            LOAD_GLOBAL             24 (MemoryStatus)
                LOAD_ATTR               26 (EXPIRED)
                LOAD_ATTR               28 (value)

 240            LOAD_GLOBAL             24 (MemoryStatus)
                LOAD_ATTR               30 (REJECTED)
                LOAD_ATTR               28 (value)

 241            LOAD_GLOBAL             24 (MemoryStatus)
                LOAD_ATTR               32 (QUARANTINED)
                LOAD_ATTR               28 (value)

 238            BUILD_SET                3
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN

 243            JUMP_BACKWARD          103 (to L6)

 244    L7:     LOAD_FAST_BORROW        12 (r)
                LOAD_ATTR               61 (get + NULL|self)
                LOAD_CONST              15 ('expires_at')
                CALL                     1
                STORE_FAST              13 (exp)

 245            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW        13 (exp)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      106 (to L12)
                NOT_TAKEN
                LOAD_FAST_BORROW        13 (exp)
                TO_BOOL
                POP_JUMP_IF_FALSE       98 (to L12)
        L8:     NOT_TAKEN

 246            NOP

 247    L9:     LOAD_GLOBAL             52 (datetime)
                LOAD_ATTR               62 (fromisoformat)
                PUSH_NULL
                LOAD_FAST_BORROW        13 (exp)
                LOAD_ATTR               65 (replace + NULL|self)
                LOAD_CONST              16 ('Z')
                LOAD_CONST              17 ('+00:00')
                CALL                     2
                CALL                     1
                STORE_FAST              14 (expires_at)

 250   L10:     LOAD_FAST_BORROW        14 (expires_at)
                POP_JUMP_IF_NONE        55 (to L12)
                NOT_TAKEN

 251            LOAD_FAST_BORROW        14 (expires_at)
                LOAD_ATTR               68 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L11)
                NOT_TAKEN

 252            LOAD_FAST_BORROW        14 (expires_at)
                LOAD_ATTR               65 (replace + NULL|self)
                LOAD_GLOBAL             56 (timezone)
                LOAD_ATTR               58 (utc)
                LOAD_CONST              18 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST              14 (expires_at)

 253   L11:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 234 (expires_at, now)
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN

 254            JUMP_BACKWARD          247 (to L6)

 255   L12:     LOAD_FAST_BORROW        11 (out)
                LOAD_ATTR               71 (append + NULL|self)
                LOAD_FAST_BORROW        12 (r)
                CALL                     1
                POP_TOP
                EXTENDED_ARG             1
                JUMP_BACKWARD          267 (to L6)

 237   L13:     END_FOR
                POP_ITER

 256            LOAD_FAST_BORROW        11 (out)
       L14:     RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 248            LOAD_GLOBAL             66 (ValueError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L17)
                NOT_TAKEN
                POP_TOP

 249            LOAD_CONST               4 (None)
                STORE_FAST              14 (expires_at)
       L16:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 97 (to L10)

 248   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L19:     PUSH_EXC_INFO

 257            LOAD_GLOBAL             72 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       59 (to L24)
                NOT_TAKEN
                STORE_FAST              15 (e)

 258   L20:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 259            LOAD_CONST              19 ('list_active_memory_for_brokerage failed (non-critical) | brokerage=')

 260            LOAD_FAST                0 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST              20 (' | error_type=')
                LOAD_GLOBAL             75 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               76 (__name__)
                FORMAT_SIMPLE

 259            BUILD_STRING             4

 258            CALL                     1
                POP_TOP

 262            BUILD_LIST               0
       L21:     SWAP                     2
       L22:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RETURN_VALUE

  --   L23:     LOAD_CONST               4 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RERAISE                  1

 257   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L8 -> L19 [0]
  L9 to L10 -> L15 [1]
  L10 to L14 -> L19 [0]
  L15 to L16 -> L18 [2] lasti
  L16 to L17 -> L19 [0]
  L17 to L18 -> L18 [2] lasti
  L18 to L19 -> L19 [0]
  L19 to L20 -> L25 [1] lasti
  L20 to L21 -> L23 [1] lasti
  L21 to L22 -> L25 [1] lasti
  L23 to L25 -> L25 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024D30, file "app\services\memory\queries.py", line 269>:
269           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('kind')

271           LOAD_CONST               2 ('Union[None, str, MemoryKind]')

269           LOAD_CONST               3 ('status')

272           LOAD_CONST               4 ('Union[None, str, MemoryStatus]')

269           LOAD_CONST               5 ('limit')

273           LOAD_CONST               6 ('int')

269           LOAD_CONST               7 ('return')

274           LOAD_CONST               8 ('List[dict]')

269           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object list_memory_admin_unscoped at 0x0000018C17E94A90, file "app\services\memory\queries.py", line 269>:
 269            RESUME                   0

 283            LOAD_GLOBAL              1 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1
                STORE_FAST               3 (capped)

 284            LOAD_GLOBAL              3 (_coerce_kind + NULL)
                LOAD_FAST_BORROW         0 (kind)
                CALL                     1
                STORE_FAST               4 (kind_value)

 285            LOAD_GLOBAL              5 (_coerce_status + NULL)
                LOAD_FAST_BORROW         1 (status)
                CALL                     1
                STORE_FAST               5 (status_value)

 287            NOP

 288    L1:     LOAD_GLOBAL              7 (_get_db + NULL)
                CALL                     0
                STORE_FAST               6 (db)

 289            LOAD_FAST_BORROW         6 (db)
                LOAD_ATTR                9 (table + NULL|self)
                LOAD_GLOBAL             10 (_TABLE)
                CALL                     1
                LOAD_ATTR               13 (select + NULL|self)
                LOAD_CONST               1 ('*')
                CALL                     1
                STORE_FAST               7 (q)

 290            LOAD_FAST_BORROW         4 (kind_value)
                POP_JUMP_IF_NONE        19 (to L2)
                NOT_TAKEN

 291            LOAD_FAST_BORROW         7 (q)
                LOAD_ATTR               15 (eq + NULL|self)
                LOAD_CONST               3 ('kind')
                LOAD_FAST_BORROW         4 (kind_value)
                CALL                     2
                STORE_FAST               7 (q)

 292    L2:     LOAD_FAST_BORROW         5 (status_value)
                POP_JUMP_IF_NONE        19 (to L3)
                NOT_TAKEN

 293            LOAD_FAST_BORROW         7 (q)
                LOAD_ATTR               15 (eq + NULL|self)
                LOAD_CONST               4 ('status')
                LOAD_FAST_BORROW         5 (status_value)
                CALL                     2
                STORE_FAST               7 (q)

 294    L3:     LOAD_FAST_BORROW         7 (q)
                LOAD_ATTR               17 (order + NULL|self)
                LOAD_CONST               5 ('created_at')
                LOAD_CONST               6 (True)
                LOAD_CONST               7 (('desc',))
                CALL_KW                  2
                LOAD_ATTR               19 (limit + NULL|self)
                LOAD_FAST_BORROW         3 (capped)
                CALL                     1
                STORE_FAST               7 (q)

 295            LOAD_FAST_BORROW         7 (q)
                LOAD_ATTR               21 (execute + NULL|self)
                CALL                     0
                STORE_FAST               8 (result)

 296            LOAD_GLOBAL             23 (list + NULL)
                LOAD_GLOBAL             25 (getattr + NULL)
                LOAD_FAST_BORROW         8 (result)
                LOAD_CONST               8 ('data')
                LOAD_CONST               2 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
        L4:     NOT_TAKEN
        L5:     POP_TOP
                BUILD_LIST               0
        L6:     CALL                     1
        L7:     RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

 297            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       56 (to L13)
                NOT_TAKEN
                STORE_FAST               9 (e)

 298    L9:     LOAD_GLOBAL             28 (logger)
                LOAD_ATTR               31 (warning + NULL|self)

 299            LOAD_CONST               9 ('list_memory_admin_unscoped failed (non-critical) | error_type=')

 300            LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE

 299            BUILD_STRING             2

 298            CALL                     1
                POP_TOP

 302            BUILD_LIST               0
       L10:     SWAP                     2
       L11:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RETURN_VALUE

  --   L12:     LOAD_CONST               2 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 297   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L4 -> L8 [0]
  L5 to L7 -> L8 [0]
  L8 to L9 -> L14 [1] lasti
  L9 to L10 -> L12 [1] lasti
  L10 to L11 -> L14 [1] lasti
  L12 to L14 -> L14 [1] lasti
```
