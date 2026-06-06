# scripts_readiness/export_events

- **pyc:** `scripts\__pycache__\export_events.cpython-314.pyc`
- **expected source path (absent):** `scripts/export_events.py`
- **co_filename (from bytecode):** `scripts\export_events.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS143D — Export pas_events to newline-delimited JSON.

Operator-initiated. Reads ONLY the pas_events table. Outputs
backups/events/YYYYMMDD_HHMMSS/pas_events.jsonl + a manifest.

Safety contract:
  - Exports nothing beyond pas_events (no env vars, no secrets).
  - Warns clearly that input_text / output_text may contain PII.
  - --dry-run skips the Supabase call entirely.
  - Empty result still produces a valid manifest.
  - Pagination uses the existing intelligence.queries.recent_events
    helper, which caps at MAX_LIMIT (100) per call. Exporter loops
    using ascending order + offset.

Usage:
  python scripts/export_events.py --dry-run
  python scripts/export_events.py --brokerage-id remax-miami
  python scripts/export_events.py --since 2026-04-01 --limit 5000
  python scripts/export_events.py --output-dir /custom/path

Exit codes:
    0  — export written + manifest valid (or --dry-run succeeded)
    1  — export failed (Supabase unavailable, etc.)
    2  — bad CLI arguments
```

## Imports

`Iterable`, `List`, `Optional`, `Path`, `__future__`, `annotations`, `app.services.intelligence.queries`, `argparse`, `datetime`, `hashlib`, `json`, `logging`, `os`, `pathlib`, `recent_events_unscoped`, `sys`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_print_status`, `_resolve_output_dir`, `build_manifest`, `export_events_paginated`, `main`, `now_stamp`, `sha256_of_file`, `write_jsonl`

## Env-key candidates

`FAIL`, `PASS`

## String constants (redacted where noted)

- '\nPAS143D — Export pas_events to newline-delimited JSON.\n\nOperator-initiated. Reads ONLY the pas_events table. Outputs\nbackups/events/YYYYMMDD_HHMMSS/pas_events.jsonl + a manifest.\n\nSafety contract:\n  - Exports nothing beyond pas_events (no env vars, no secrets).\n  - Warns clearly that input_text / output_text may contain PII.\n  - --dry-run skips the Supabase call entirely.\n  - Empty result still produces a valid manifest.\n  - Pagination uses the existing intelligence.queries.recent_events\n    helper, which caps at MAX_LIMIT (100) per call. Exporter loops\n    using ascending order + offset.\n\nUsage:\n  python scripts/export_events.py --dry-run\n  python scripts/export_events.py --brokerage-id remax-miami\n  python scripts/export_events.py --since 2026-04-01 --limit 5000\n  python scripts/export_events.py --output-dir /custom/path\n\nExit codes:\n    0  — export written + manifest valid (or --dry-run succeeded)\n    1  — export failed (Supabase unavailable, etc.)\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'page_size'
- 'return'
- 'str'
- '%Y%m%d_%H%M%S'
- 'rows'
- 'Iterable[dict]'
- 'path'
- 'Path'
- 'int'
- '\nWrite `rows` as newline-delimited JSON into `path`. Returns the\nnumber of rows actually written.\n'
- 'timestamp'
- 'brokerage_id'
- 'Optional[str]'
- 'since_iso'
- 'row_count'
- 'output_file'
- 'sha256'
- 'warnings'
- 'List[str]'
- 'truncated'
- 'bool'
- 'dict'
- 'tool'
- 'pas143d.export_events'
- 'table'
- 'pas_events'
- 'since'
- 'hard_limit'
- 'Optional[int]'
- 'List[dict]'
- "\nPage through pas_events using intelligence.queries.recent_events.\n\nReturns rows in chronological order (oldest first). Stops when\na page returns fewer than `page_size` rows OR `hard_limit` is hit.\nImported lazily so dry-run paths don't need Supabase available.\n"
- 'created_at'
- 'label'
- 'detail'
- 'None'
- 'PASS'
- 'FAIL'
- ' — '
- 'arg_value'
- 'backups'
- 'events'
- 'argv'
- 'Optional[list]'
- 'export_events'
- 'PAS143D — export pas_events to newline-delimited JSON.'
- '--brokerage-id'
- 'Restrict export to one brokerage tenant.'
- '--since'
- 'ISO timestamp; only events at or after this time.'
- '--limit'
- 'Hard cap on row count (after pagination).'
- '--dry-run'
- 'store_true'
- 'Print plan and write a zero-row manifest only.'
- '--output-dir'
- 'Override the default ./backups/events/ root.'
- '--page-size'
- 'Page size per Supabase request (default '
- '--limit must be positive'
- '--page-size must be in (0, 1000]'
- 'pas_events.jsonl'
- 'export_manifest.json'
- 'Output directory'
- 'Brokerage filter'
- 'Since filter'
- 'pas_events.input_text and output_text may contain PII (lead phone numbers, names, free-text utterances). Treat this file as confidential.'
- 'dry-run: no Supabase access performed'
- 'Dry-run manifest'
- 'export aborted: '
- 'Export complete'
- ' row(s) → '
- ' (sha256='
- 'n/a'
- 'export aborted'

## Disassembly

```
   0            RESUME                   0

   1            LOAD_CONST               0 ('\nPAS143D — Export pas_events to newline-delimited JSON.\n\nOperator-initiated. Reads ONLY the pas_events table. Outputs\nbackups/events/YYYYMMDD_HHMMSS/pas_events.jsonl + a manifest.\n\nSafety contract:\n  - Exports nothing beyond pas_events (no env vars, no secrets).\n  - Warns clearly that input_text / output_text may contain PII.\n  - --dry-run skips the Supabase call entirely.\n  - Empty result still produces a valid manifest.\n  - Pagination uses the existing intelligence.queries.recent_events\n    helper, which caps at MAX_LIMIT (100) per call. Exporter loops\n    using ascending order + offset.\n\nUsage:\n  python scripts/export_events.py --dry-run\n  python scripts/export_events.py --brokerage-id remax-miami\n  python scripts/export_events.py --since 2026-04-01 --limit 5000\n  python scripts/export_events.py --output-dir /custom/path\n\nExit codes:\n    0  — export written + manifest valid (or --dry-run succeeded)\n    1  — export failed (Supabase unavailable, etc.)\n    2  — bad CLI arguments\n')
                STORE_NAME               0 (__doc__)

  28            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('annotations',))
                IMPORT_NAME              1 (__future__)
                IMPORT_FROM              2 (annotations)
                STORE_NAME               2 (annotations)
                POP_TOP

  30            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              3 (argparse)
                STORE_NAME               3 (argparse)

  31            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              4 (datetime)
                STORE_NAME               5 (_dt)

  32            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              6 (hashlib)
                STORE_NAME               6 (hashlib)

  33            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              7 (json)
                STORE_NAME               7 (json)

  34            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              8 (logging)
                STORE_NAME               8 (logging)

  35            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              9 (os)
                STORE_NAME               9 (os)

  36            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME             10 (sys)
                STORE_NAME              10 (sys)

  37            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('Path',))
                IMPORT_NAME             11 (pathlib)
                IMPORT_FROM             12 (Path)
                STORE_NAME              12 (Path)
                POP_TOP

  38            LOAD_SMALL_INT           0
                LOAD_CONST               4 (('Iterable', 'List', 'Optional'))
                IMPORT_NAME             13 (typing)
                IMPORT_FROM             14 (Iterable)
                STORE_NAME              14 (Iterable)
                IMPORT_FROM             15 (List)
                STORE_NAME              15 (List)
                IMPORT_FROM             16 (Optional)
                STORE_NAME              16 (Optional)
                POP_TOP

  41            LOAD_NAME                9 (os)
                LOAD_ATTR               34 (path)
                LOAD_ATTR               37 (abspath + NULL|self)
                LOAD_NAME                9 (os)
                LOAD_ATTR               34 (path)
                LOAD_ATTR               39 (join + NULL|self)
                LOAD_NAME                9 (os)
                LOAD_ATTR               34 (path)
                LOAD_ATTR               41 (dirname + NULL|self)
                LOAD_NAME               21 (__file__)
                CALL                     1
                LOAD_CONST               5 ('..')
                CALL                     2
                CALL                     1
                STORE_NAME              22 (_REPO_ROOT)

  42            LOAD_NAME               22 (_REPO_ROOT)
                LOAD_NAME               10 (sys)
                LOAD_ATTR               34 (path)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       29 (to L1)
                NOT_TAKEN

  43            LOAD_NAME               10 (sys)
                LOAD_ATTR               34 (path)
                LOAD_ATTR               47 (insert + NULL|self)
                LOAD_SMALL_INT           0
                LOAD_NAME               22 (_REPO_ROOT)
                CALL                     2
                POP_TOP

  46    L1:     LOAD_NAME               10 (sys)
                LOAD_ATTR               48 (stdout)
                LOAD_NAME               10 (sys)
                LOAD_ATTR               50 (stderr)
                BUILD_TUPLE              2
                GET_ITER
        L2:     FOR_ITER                22 (to L5)
                STORE_NAME              26 (_stream)

  47            NOP

  48    L3:     LOAD_NAME               26 (_stream)
                LOAD_ATTR               55 (reconfigure + NULL|self)
                LOAD_CONST               6 ('utf-8')
                LOAD_CONST               7 (('encoding',))
                CALL_KW                  1
                POP_TOP
        L4:     JUMP_BACKWARD           24 (to L2)

  46    L5:     END_FOR
                POP_ITER

  55            LOAD_NAME                8 (logging)
                LOAD_ATTR               58 (basicConfig)
                PUSH_NULL
                LOAD_NAME                8 (logging)
                LOAD_ATTR               60 (WARNING)
                LOAD_CONST               8 (('level',))
                CALL_KW                  1
                POP_TOP

  64            LOAD_SMALL_INT         100
                STORE_NAME              31 (_DEFAULT_PAGE_SIZE)

  67            LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts\export_events.py", line 67>)
                MAKE_FUNCTION
                LOAD_CONST              10 (<code object now_stamp at 0x0000018C180110B0, file "scripts\export_events.py", line 67>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              32 (now_stamp)

  71            LOAD_CONST              11 (<code object __annotate__ at 0x0000018C18024F30, file "scripts\export_events.py", line 71>)
                MAKE_FUNCTION
                LOAD_CONST              12 (<code object write_jsonl at 0x0000018C179C3A50, file "scripts\export_events.py", line 71>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              33 (write_jsonl)

  85            LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts\export_events.py", line 85>)
                MAKE_FUNCTION
                LOAD_CONST              14 (<code object sha256_of_file at 0x0000018C17FEDA30, file "scripts\export_events.py", line 85>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              34 (sha256_of_file)

  96            LOAD_CONST              15 (<code object __annotate__ at 0x0000018C180F4140, file "scripts\export_events.py", line 96>)
                MAKE_FUNCTION
                LOAD_CONST              16 (<code object build_manifest at 0x0000018C17FF13B0, file "scripts\export_events.py", line 96>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              35 (build_manifest)

 123            LOAD_CONST              17 ('page_size')

 128            LOAD_NAME               31 (_DEFAULT_PAGE_SIZE)

 123            BUILD_MAP                1
                LOAD_CONST              18 (<code object __annotate__ at 0x0000018C18024E30, file "scripts\export_events.py", line 123>)
                MAKE_FUNCTION
                LOAD_CONST              19 (<code object export_events_paginated at 0x0000018C17F001D0, file "scripts\export_events.py", line 123>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
                STORE_NAME              36 (export_events_paginated)

 175            LOAD_CONST              27 (('',))
                LOAD_CONST              20 (<code object __annotate__ at 0x0000018C18026030, file "scripts\export_events.py", line 175>)
                MAKE_FUNCTION
                LOAD_CONST              21 (<code object _print_status at 0x0000018C18038170, file "scripts\export_events.py", line 175>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              37 (_print_status)

 183            LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA2D30, file "scripts\export_events.py", line 183>)
                MAKE_FUNCTION
                LOAD_CONST              23 (<code object _resolve_output_dir at 0x0000018C18011370, file "scripts\export_events.py", line 183>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              38 (_resolve_output_dir)

 188            LOAD_CONST              28 ((None,))
                LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts\export_events.py", line 188>)
                MAKE_FUNCTION
                LOAD_CONST              25 (<code object main at 0x0000018C17E590D0, file "scripts\export_events.py", line 188>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              39 (main)

 297            LOAD_NAME               40 (__name__)
                LOAD_CONST              26 ('__main__')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       14 (to L6)
                NOT_TAKEN

 298            LOAD_NAME               41 (SystemExit)
                PUSH_NULL
                LOAD_NAME               39 (main)
                PUSH_NULL
                CALL                     0
                CALL                     1
                RAISE_VARARGS            1

 297    L6:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  49            LOAD_NAME               28 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

  50    L8:     POP_EXCEPT
                JUMP_BACKWARD          145 (to L2)

  49    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L7 [1]
  L7 to L8 -> L10 [2] lasti
  L9 to L10 -> L10 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts\export_events.py", line 67>:
 67           RESUME                   0
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

Disassembly of <code object now_stamp at 0x0000018C180110B0, file "scripts\export_events.py", line 67>:
 67           RESUME                   0

 68           LOAD_GLOBAL              0 (_dt)
              LOAD_ATTR                2 (datetime)
              LOAD_ATTR                5 (now + NULL|self)
              LOAD_GLOBAL              0 (_dt)
              LOAD_ATTR                6 (timezone)
              LOAD_ATTR                8 (utc)
              CALL                     1
              LOAD_ATTR               11 (strftime + NULL|self)
              LOAD_CONST               0 ('%Y%m%d_%H%M%S')
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024F30, file "scripts\export_events.py", line 71>:
 71           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rows')
              LOAD_CONST               2 ('Iterable[dict]')
              LOAD_CONST               3 ('path')
              LOAD_CONST               4 ('Path')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('int')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object write_jsonl at 0x0000018C179C3A50, file "scripts\export_events.py", line 71>:
  71           RESUME                   0

  76           LOAD_SMALL_INT           0
               STORE_FAST               2 (n)

  77           LOAD_GLOBAL              1 (open + NULL)
               LOAD_FAST_BORROW         1 (path)
               LOAD_CONST               1 ('w')
               LOAD_CONST               2 ('utf-8')
               LOAD_CONST               3 ('\n')
               LOAD_CONST               4 (('encoding', 'newline'))
               CALL_KW                  4
               COPY                     1
               LOAD_SPECIAL             1 (__exit__)
               SWAP                     2
               SWAP                     3
               LOAD_SPECIAL             0 (__enter__)
               CALL                     0
       L1:     STORE_FAST               3 (f)

  78           LOAD_FAST_BORROW         0 (rows)
               GET_ITER
       L2:     FOR_ITER                73 (to L3)
               STORE_FAST               4 (row)

  79           LOAD_FAST_BORROW         3 (f)
               LOAD_ATTR                3 (write + NULL|self)
               LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         4 (row)
               LOAD_GLOBAL              8 (str)
               LOAD_CONST               5 (False)
               LOAD_CONST               6 (('default', 'ensure_ascii'))
               CALL_KW                  3
               CALL                     1
               POP_TOP

  80           LOAD_FAST_BORROW         3 (f)
               LOAD_ATTR                3 (write + NULL|self)
               LOAD_CONST               3 ('\n')
               CALL                     1
               POP_TOP

  81           LOAD_FAST_BORROW         2 (n)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (n)
               JUMP_BACKWARD           75 (to L2)

  78   L3:     END_FOR
               POP_ITER

  77   L4:     LOAD_CONST               7 (None)
               LOAD_CONST               7 (None)
               LOAD_CONST               7 (None)
               CALL                     3
               POP_TOP

  82           LOAD_FAST_BORROW         2 (n)
               RETURN_VALUE

  77   L5:     PUSH_EXC_INFO
               WITH_EXCEPT_START
               TO_BOOL
               POP_JUMP_IF_TRUE         2 (to L6)
               NOT_TAKEN
               RERAISE                  2
       L6:     POP_TOP
       L7:     POP_EXCEPT
               POP_TOP
               POP_TOP
               POP_TOP

  82           LOAD_FAST                2 (n)
               RETURN_VALUE

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L5 [2] lasti
  L5 to L7 -> L8 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts\export_events.py", line 85>:
 85           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('path')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object sha256_of_file at 0x0000018C17FEDA30, file "scripts\export_events.py", line 85>:
  --            MAKE_CELL                3 (f)

  85            RESUME                   0

  86            NOP

  87    L1:     LOAD_GLOBAL              0 (hashlib)
                LOAD_ATTR                2 (sha256)
                PUSH_NULL
                CALL                     0
                STORE_FAST               1 (h)

  88            LOAD_GLOBAL              5 (open + NULL)
                LOAD_FAST_BORROW         0 (path)
                LOAD_CONST               0 ('rb')
                CALL                     2
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L2:     STORE_DEREF              3 (f)

  89            LOAD_GLOBAL              7 (iter + NULL)
                LOAD_FAST_BORROW         3 (f)
                BUILD_TUPLE              1
                LOAD_CONST               1 (<code object <lambda> at 0x0000018C18025E30, file "scripts\export_events.py", line 89>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_CONST               2 (b'')
                CALL                     2
                GET_ITER
        L3:     FOR_ITER                20 (to L4)
                STORE_FAST               2 (chunk)

  90            LOAD_FAST_BORROW         1 (h)
                LOAD_ATTR                9 (update + NULL|self)
                LOAD_FAST_BORROW         2 (chunk)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           22 (to L3)

  89    L4:     END_FOR
                POP_ITER

  88    L5:     LOAD_CONST               3 (None)
                LOAD_CONST               3 (None)
                LOAD_CONST               3 (None)
                CALL                     3
                POP_TOP

  91    L6:     LOAD_FAST_BORROW         1 (h)
                LOAD_ATTR               11 (hexdigest + NULL|self)
                CALL                     0
        L7:     RETURN_VALUE

  88    L8:     PUSH_EXC_INFO
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
                JUMP_BACKWARD_NO_INTERRUPT 32 (to L6)

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L12:     PUSH_EXC_INFO

  92            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L14)
                NOT_TAKEN
                POP_TOP

  93   L13:     POP_EXCEPT
                LOAD_CONST               4 ('')
                RETURN_VALUE

  92   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L12 [0]
  L2 to L5 -> L8 [2] lasti
  L5 to L7 -> L12 [0]
  L8 to L10 -> L11 [4] lasti
  L10 to L12 -> L12 [0]
  L12 to L13 -> L15 [1] lasti
  L14 to L15 -> L15 [1] lasti

Disassembly of <code object <lambda> at 0x0000018C18025E30, file "scripts\export_events.py", line 89>:
  --           COPY_FREE_VARS           1

  89           RESUME                   0
               LOAD_DEREF               0 (f)
               LOAD_ATTR                1 (read + NULL|self)
               LOAD_CONST               1 (1048576)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180F4140, file "scripts\export_events.py", line 96>:
 96           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('timestamp')

 98           LOAD_CONST               2 ('str')

 96           LOAD_CONST               3 ('brokerage_id')

 99           LOAD_CONST               4 ('Optional[str]')

 96           LOAD_CONST               5 ('since_iso')

100           LOAD_CONST               4 ('Optional[str]')

 96           LOAD_CONST               6 ('row_count')

101           LOAD_CONST               7 ('int')

 96           LOAD_CONST               8 ('output_file')

102           LOAD_CONST               9 ('Path')

 96           LOAD_CONST              10 ('sha256')

103           LOAD_CONST               2 ('str')

 96           LOAD_CONST              11 ('warnings')

104           LOAD_CONST              12 ('List[str]')

 96           LOAD_CONST              13 ('page_size')

105           LOAD_CONST               7 ('int')

 96           LOAD_CONST              14 ('truncated')

106           LOAD_CONST              15 ('bool')

 96           LOAD_CONST              16 ('return')

107           LOAD_CONST              17 ('dict')

 96           BUILD_MAP               10
              RETURN_VALUE

Disassembly of <code object build_manifest at 0x0000018C17FF13B0, file "scripts\export_events.py", line 96>:
 96           RESUME                   0

109           LOAD_CONST               0 ('timestamp')
              LOAD_FAST                0 (timestamp)

110           LOAD_CONST               1 ('tool')
              LOAD_CONST               2 ('pas143d.export_events')

111           LOAD_CONST               3 ('table')
              LOAD_CONST               4 ('pas_events')

112           LOAD_CONST               5 ('brokerage_id')
              LOAD_FAST                1 (brokerage_id)

113           LOAD_CONST               6 ('since')
              LOAD_FAST                2 (since_iso)

114           LOAD_CONST               7 ('row_count')
              LOAD_GLOBAL              1 (int + NULL)
              LOAD_FAST_BORROW         3 (row_count)
              CALL                     1

115           LOAD_CONST               8 ('output_file')
              LOAD_FAST_BORROW         4 (output_file)
              LOAD_ATTR                2 (name)

116           LOAD_CONST               9 ('sha256')
              LOAD_FAST                5 (sha256)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST              10 ('')

117   L1:     LOAD_CONST              11 ('warnings')
              LOAD_GLOBAL              5 (list + NULL)
              LOAD_FAST_BORROW         6 (warnings)
              CALL                     1

118           LOAD_CONST              12 ('page_size')
              LOAD_GLOBAL              1 (int + NULL)
              LOAD_FAST_BORROW         7 (page_size)
              CALL                     1

119           LOAD_CONST              13 ('truncated')
              LOAD_GLOBAL              7 (bool + NULL)
              LOAD_FAST_BORROW         8 (truncated)
              CALL                     1

108           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "scripts\export_events.py", line 123>:
123           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

125           LOAD_CONST               2 ('Optional[str]')

123           LOAD_CONST               3 ('since_iso')

126           LOAD_CONST               2 ('Optional[str]')

123           LOAD_CONST               4 ('hard_limit')

127           LOAD_CONST               5 ('Optional[int]')

123           LOAD_CONST               6 ('page_size')

128           LOAD_CONST               7 ('int')

123           LOAD_CONST               8 ('return')

129           LOAD_CONST               9 ('List[dict]')

123           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object export_events_paginated at 0x0000018C17F001D0, file "scripts\export_events.py", line 123>:
123           RESUME                   0

141           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('recent_events_unscoped',))
              IMPORT_NAME              0 (app.services.intelligence.queries)
              IMPORT_FROM              1 (recent_events_unscoped)
              STORE_FAST               4 (recent_events_unscoped)
              POP_TOP

143           BUILD_LIST               0
              STORE_FAST               5 (collected)

144           LOAD_SMALL_INT           0
              STORE_FAST               6 (offset)

145   L1:     NOP

148           LOAD_FAST_BORROW         4 (recent_events_unscoped)
              PUSH_NULL

149           LOAD_FAST_BORROW         0 (brokerage_id)

150           LOAD_FAST_BORROW         1 (since_iso)

151           LOAD_FAST_BORROW         3 (page_size)

152           LOAD_FAST_BORROW         6 (offset)

148           LOAD_CONST               2 (('brokerage_id', 'since_iso', 'limit', 'offset'))
              CALL_KW                  4
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP

153           BUILD_LIST               0

148   L2:     STORE_FAST               7 (page)

154           LOAD_FAST_BORROW         7 (page)
              TO_BOOL
              POP_JUMP_IF_TRUE         2 (to L3)
              NOT_TAKEN

155           JUMP_FORWARD            65 (to L6)

156   L3:     LOAD_FAST_BORROW         5 (collected)
              LOAD_ATTR                5 (extend + NULL|self)
              LOAD_FAST_BORROW         7 (page)
              CALL                     1
              POP_TOP

157           LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         7 (page)
              CALL                     1
              LOAD_FAST_BORROW         3 (page_size)
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_FALSE        2 (to L4)
              NOT_TAKEN

158           JUMP_FORWARD            31 (to L6)

159   L4:     LOAD_FAST_BORROW         2 (hard_limit)
              POP_JUMP_IF_NONE        18 (to L5)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         5 (collected)
              CALL                     1
              LOAD_FAST_BORROW         2 (hard_limit)
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_FALSE        2 (to L5)
              NOT_TAKEN

160           JUMP_FORWARD            10 (to L6)

161   L5:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 99 (offset, page_size)
              BINARY_OP               13 (+=)
              STORE_FAST               6 (offset)
              JUMP_BACKWARD           97 (to L1)

163   L6:     LOAD_FAST_BORROW         2 (hard_limit)
              POP_JUMP_IF_NONE        22 (to L7)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         5 (collected)
              CALL                     1
              LOAD_FAST_BORROW         2 (hard_limit)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        6 (to L7)
              NOT_TAKEN

164           LOAD_FAST_BORROW         5 (collected)
              LOAD_CONST               3 (None)
              LOAD_FAST_BORROW         2 (hard_limit)
              BINARY_SLICE
              STORE_FAST               5 (collected)

167   L7:     LOAD_FAST_BORROW         5 (collected)
              LOAD_ATTR                9 (sort + NULL|self)
              LOAD_CONST               4 (<code object <lambda> at 0x0000018C180F4030, file "scripts\export_events.py", line 167>)
              MAKE_FUNCTION
              LOAD_CONST               5 (('key',))
              CALL_KW                  1
              POP_TOP

168           LOAD_FAST_BORROW         5 (collected)
              RETURN_VALUE

Disassembly of <code object <lambda> at 0x0000018C180F4030, file "scripts\export_events.py", line 167>:
167           RESUME                   0
              LOAD_FAST_BORROW         0 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('created_at')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026030, file "scripts\export_events.py", line 175>:
175           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('label')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('ok')
              LOAD_CONST               4 ('bool')
              LOAD_CONST               5 ('detail')
              LOAD_CONST               2 ('str')
              LOAD_CONST               6 ('return')
              LOAD_CONST               7 ('None')
              BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _print_status at 0x0000018C18038170, file "scripts\export_events.py", line 175>:
175           RESUME                   0

176           LOAD_FAST_BORROW         1 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_CONST               0 ('PASS')
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               1 ('FAIL')
      L2:     STORE_FAST               3 (tag)

177           LOAD_CONST               2 ('[')
              LOAD_FAST_BORROW         3 (tag)
              FORMAT_SIMPLE
              LOAD_CONST               3 ('] ')
              LOAD_FAST_BORROW         0 (label)
              FORMAT_SIMPLE
              BUILD_STRING             4
              STORE_FAST               4 (line)

178           LOAD_FAST_BORROW         2 (detail)
              TO_BOOL
              POP_JUMP_IF_FALSE       13 (to L3)
              NOT_TAKEN

179           LOAD_FAST_BORROW         4 (line)
              LOAD_CONST               4 (' — ')
              LOAD_FAST_BORROW         2 (detail)
              FORMAT_SIMPLE
              BUILD_STRING             2
              BINARY_OP               13 (+=)
              STORE_FAST               4 (line)

180   L3:     LOAD_GLOBAL              1 (print + NULL)
              LOAD_FAST_BORROW         4 (line)
              CALL                     1
              POP_TOP
              LOAD_CONST               5 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "scripts\export_events.py", line 183>:
183           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('arg_value')
              LOAD_CONST               2 ('Optional[str]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Path')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _resolve_output_dir at 0x0000018C18011370, file "scripts\export_events.py", line 183>:
183           RESUME                   0

184           LOAD_FAST_BORROW         0 (arg_value)
              TO_BOOL
              POP_JUMP_IF_FALSE       12 (to L1)
              NOT_TAKEN
              LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (arg_value)
              CALL                     1
              JUMP_FORWARD            34 (to L2)
      L1:     LOAD_GLOBAL              0 (Path)
              LOAD_ATTR                2 (cwd)
              PUSH_NULL
              CALL                     0
              LOAD_CONST               0 ('backups')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('events')
              BINARY_OP               11 (/)
      L2:     STORE_FAST               1 (base)

185           LOAD_FAST_BORROW         1 (base)
              LOAD_GLOBAL              5 (now_stamp + NULL)
              CALL                     0
              BINARY_OP               11 (/)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts\export_events.py", line 188>:
188           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('argv')
              LOAD_CONST               2 ('Optional[list]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object main at 0x0000018C17E590D0, file "scripts\export_events.py", line 188>:
 188            RESUME                   0

 189            LOAD_GLOBAL              0 (argparse)
                LOAD_ATTR                2 (ArgumentParser)
                PUSH_NULL

 190            LOAD_CONST               0 ('export_events')

 191            LOAD_CONST               1 ('PAS143D — export pas_events to newline-delimited JSON.')

 189            LOAD_CONST               2 (('prog', 'description'))
                CALL_KW                  2
                STORE_FAST               1 (parser)

 193            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST               3 ('--brokerage-id')
                LOAD_CONST               4 (None)

 194            LOAD_CONST               5 ('Restrict export to one brokerage tenant.')

 193            LOAD_CONST               6 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 195            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST               7 ('--since')
                LOAD_CONST               4 (None)

 196            LOAD_CONST               8 ('ISO timestamp; only events at or after this time.')

 195            LOAD_CONST               6 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 197            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST               9 ('--limit')
                LOAD_GLOBAL              6 (int)
                LOAD_CONST               4 (None)

 198            LOAD_CONST              10 ('Hard cap on row count (after pagination).')

 197            LOAD_CONST              11 (('type', 'default', 'help'))
                CALL_KW                  4
                POP_TOP

 199            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST              12 ('--dry-run')
                LOAD_CONST              13 ('store_true')

 200            LOAD_CONST              14 ('Print plan and write a zero-row manifest only.')

 199            LOAD_CONST              15 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 201            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST              16 ('--output-dir')
                LOAD_CONST               4 (None)

 202            LOAD_CONST              17 ('Override the default ./backups/events/ root.')

 201            LOAD_CONST               6 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 203            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST              18 ('--page-size')
                LOAD_GLOBAL              6 (int)
                LOAD_GLOBAL              8 (_DEFAULT_PAGE_SIZE)

 204            LOAD_CONST              19 ('Page size per Supabase request (default ')
                LOAD_GLOBAL              8 (_DEFAULT_PAGE_SIZE)
                FORMAT_SIMPLE
                LOAD_CONST              20 (').')
                BUILD_STRING             3

 203            LOAD_CONST              11 (('type', 'default', 'help'))
                CALL_KW                  4
                POP_TOP

 205            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR               11 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 207            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               12 (limit)
                POP_JUMP_IF_NONE        47 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               12 (limit)
                LOAD_SMALL_INT           0
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE       30 (to L1)
                NOT_TAKEN

 208            LOAD_GLOBAL             15 (print + NULL)
                LOAD_CONST              21 ('--limit must be positive')
                LOAD_GLOBAL             16 (sys)
                LOAD_ATTR               18 (stderr)
                LOAD_CONST              22 (('file',))
                CALL_KW                  2
                POP_TOP

 209            LOAD_SMALL_INT           2
                RETURN_VALUE

 210    L1:     LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               20 (page_size)
                LOAD_SMALL_INT           0
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_TRUE        18 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               20 (page_size)
                LOAD_CONST              23 (1000)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE       30 (to L3)
                NOT_TAKEN

 211    L2:     LOAD_GLOBAL             15 (print + NULL)
                LOAD_CONST              24 ('--page-size must be in (0, 1000]')
                LOAD_GLOBAL             16 (sys)
                LOAD_ATTR               18 (stderr)
                LOAD_CONST              22 (('file',))
                CALL_KW                  2
                POP_TOP

 212            LOAD_SMALL_INT           2
                RETURN_VALUE

 214    L3:     LOAD_GLOBAL             23 (_resolve_output_dir + NULL)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               24 (output_dir)
                CALL                     1
                STORE_FAST               3 (out_dir)

 215            LOAD_FAST_BORROW         3 (out_dir)
                LOAD_ATTR               27 (mkdir + NULL|self)
                LOAD_CONST              25 (True)
                LOAD_CONST              25 (True)
                LOAD_CONST              26 (('parents', 'exist_ok'))
                CALL_KW                  2
                POP_TOP

 216            LOAD_GLOBAL             29 (now_stamp + NULL)
                CALL                     0
                STORE_FAST               4 (timestamp)

 217            LOAD_FAST_BORROW         3 (out_dir)
                LOAD_CONST              27 ('pas_events.jsonl')
                BINARY_OP               11 (/)
                STORE_FAST               5 (jsonl_path)

 218            LOAD_FAST_BORROW         3 (out_dir)
                LOAD_CONST              28 ('export_manifest.json')
                BINARY_OP               11 (/)
                STORE_FAST               6 (manifest_path)

 220            LOAD_GLOBAL             31 (_print_status + NULL)
                LOAD_CONST              29 ('Output directory')
                LOAD_CONST              25 (True)
                LOAD_GLOBAL             33 (str + NULL)
                LOAD_FAST_BORROW         3 (out_dir)
                CALL                     1
                LOAD_CONST              30 (('ok', 'detail'))
                CALL_KW                  3
                POP_TOP

 221            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               34 (brokerage_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L4)
                NOT_TAKEN

 222            LOAD_GLOBAL             31 (_print_status + NULL)
                LOAD_CONST              31 ('Brokerage filter')
                LOAD_CONST              25 (True)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               34 (brokerage_id)
                LOAD_CONST              30 (('ok', 'detail'))
                CALL_KW                  3
                POP_TOP

 223    L4:     LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               36 (since)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L5)
                NOT_TAKEN

 224            LOAD_GLOBAL             31 (_print_status + NULL)
                LOAD_CONST              32 ('Since filter')
                LOAD_CONST              25 (True)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               36 (since)
                LOAD_CONST              30 (('ok', 'detail'))
                CALL_KW                  3
                POP_TOP

 228    L5:     LOAD_CONST              33 ('pas_events.input_text and output_text may contain PII (lead phone numbers, names, free-text utterances). Treat this file as confidential.')

 226            BUILD_LIST               1
                STORE_FAST               7 (warnings)

 233            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               38 (dry_run)
                TO_BOOL
                POP_JUMP_IF_FALSE      146 (to L6)
                NOT_TAKEN

 235            LOAD_GLOBAL             41 (write_jsonl + NULL)
                BUILD_LIST               0
                LOAD_FAST_BORROW         5 (jsonl_path)
                CALL                     2
                POP_TOP

 236            LOAD_GLOBAL             43 (build_manifest + NULL)

 237            LOAD_FAST_BORROW         4 (timestamp)

 238            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               34 (brokerage_id)

 239            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               36 (since)

 240            LOAD_SMALL_INT           0

 241            LOAD_FAST_BORROW         5 (jsonl_path)

 242            LOAD_GLOBAL             45 (sha256_of_file + NULL)
                LOAD_FAST_BORROW         5 (jsonl_path)
                CALL                     1

 243            LOAD_FAST_BORROW         7 (warnings)
                LOAD_CONST              34 ('dry-run: no Supabase access performed')
                BUILD_LIST               1
                BINARY_OP                0 (+)

 244            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               20 (page_size)

 245            LOAD_CONST              35 (False)

 236            LOAD_CONST              36 (('timestamp', 'brokerage_id', 'since_iso', 'row_count', 'output_file', 'sha256', 'warnings', 'page_size', 'truncated'))
                CALL_KW                  9
                STORE_FAST               8 (manifest)

 247            LOAD_FAST_BORROW         6 (manifest_path)
                LOAD_ATTR               47 (write_text + NULL|self)
                LOAD_GLOBAL             48 (json)
                LOAD_ATTR               50 (dumps)
                PUSH_NULL
                LOAD_FAST_BORROW         8 (manifest)
                LOAD_SMALL_INT           2
                LOAD_CONST              37 (('indent',))
                CALL_KW                  2
                LOAD_CONST              38 ('utf-8')
                LOAD_CONST              39 (('encoding',))
                CALL_KW                  2
                POP_TOP

 248            LOAD_GLOBAL             31 (_print_status + NULL)
                LOAD_CONST              40 ('Dry-run manifest')
                LOAD_CONST              25 (True)
                LOAD_GLOBAL             33 (str + NULL)
                LOAD_FAST_BORROW         6 (manifest_path)
                CALL                     1
                LOAD_CONST              30 (('ok', 'detail'))
                CALL_KW                  3
                POP_TOP

 249            LOAD_SMALL_INT           0
                RETURN_VALUE

 253    L6:     NOP

 254    L7:     LOAD_GLOBAL             53 (export_events_paginated + NULL)

 255            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               34 (brokerage_id)

 256            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               36 (since)

 257            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               12 (limit)

 258            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               20 (page_size)

 254            LOAD_CONST              41 (('brokerage_id', 'since_iso', 'hard_limit', 'page_size'))
                CALL_KW                  4
                STORE_FAST               9 (rows)

 264    L8:     LOAD_GLOBAL             41 (write_jsonl + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 149 (rows, jsonl_path)
                CALL                     2
                STORE_FAST              11 (n_written)

 265            LOAD_GLOBAL             45 (sha256_of_file + NULL)
                LOAD_FAST_BORROW         5 (jsonl_path)
                CALL                     1
                STORE_FAST              12 (sha)

 267            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               12 (limit)
                LOAD_CONST               4 (None)
                IS_OP                    1 (is not)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       15 (to L9)
                NOT_TAKEN
                POP_TOP

 268            LOAD_FAST_BORROW_LOAD_FAST_BORROW 178 (n_written, args)
                LOAD_ATTR               12 (limit)
                COMPARE_OP             172 (>=)

 266    L9:     STORE_FAST              13 (truncated)

 273            LOAD_GLOBAL             43 (build_manifest + NULL)

 274            LOAD_FAST_BORROW         4 (timestamp)

 275            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               34 (brokerage_id)

 276            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               36 (since)

 277            LOAD_FAST_BORROW        11 (n_written)

 278            LOAD_FAST_BORROW         5 (jsonl_path)

 279            LOAD_FAST_BORROW        12 (sha)

 280            LOAD_FAST_BORROW         7 (warnings)

 281            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               20 (page_size)

 282            LOAD_FAST_BORROW        13 (truncated)

 273            LOAD_CONST              36 (('timestamp', 'brokerage_id', 'since_iso', 'row_count', 'output_file', 'sha256', 'warnings', 'page_size', 'truncated'))
                CALL_KW                  9
                STORE_FAST               8 (manifest)

 284            LOAD_FAST_BORROW         6 (manifest_path)
                LOAD_ATTR               47 (write_text + NULL|self)
                LOAD_GLOBAL             48 (json)
                LOAD_ATTR               50 (dumps)
                PUSH_NULL
                LOAD_FAST_BORROW         8 (manifest)
                LOAD_SMALL_INT           2
                LOAD_CONST              37 (('indent',))
                CALL_KW                  2
                LOAD_CONST              38 ('utf-8')
                LOAD_CONST              39 (('encoding',))
                CALL_KW                  2
                POP_TOP

 286            LOAD_FAST_BORROW        11 (n_written)
                LOAD_SMALL_INT           0
                COMPARE_OP             172 (>=)
                STORE_FAST              14 (ok)

 287            LOAD_GLOBAL             31 (_print_status + NULL)

 288            LOAD_CONST              44 ('Export complete')

 289            LOAD_FAST               14 (ok)

 290            LOAD_FAST               11 (n_written)
                FORMAT_SIMPLE
                LOAD_CONST              45 (' row(s) → ')
                LOAD_FAST_BORROW         5 (jsonl_path)
                LOAD_ATTR               62 (name)
                FORMAT_SIMPLE
                LOAD_CONST              46 (' (sha256=')
                LOAD_FAST_BORROW        12 (sha)
                LOAD_CONST              47 (slice(None, 12, None))
                BINARY_OP               26 ([])
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              48 ('n/a')
       L10:     FORMAT_SIMPLE
                LOAD_CONST              49 ('…)')
                BUILD_STRING             6

 287            LOAD_CONST              30 (('ok', 'detail'))
                CALL_KW                  3
                POP_TOP

 292            LOAD_GLOBAL             64 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       28 (to L14)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              50 (<code object <genexpr> at 0x0000018C18025C30, file "scripts\export_events.py", line 292>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         7 (warnings)
                GET_ITER
                CALL                     0
       L11:     FOR_ITER                12 (to L13)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L11)
       L12:     POP_ITER
                LOAD_CONST              25 (True)
                JUMP_FORWARD            17 (to L15)
       L13:     END_FOR
                POP_ITER
                LOAD_CONST              35 (False)
                JUMP_FORWARD            13 (to L15)
       L14:     PUSH_NULL
                LOAD_CONST              50 (<code object <genexpr> at 0x0000018C18025C30, file "scripts\export_events.py", line 292>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         7 (warnings)
                GET_ITER
                CALL                     0
                CALL                     1
       L15:     TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L16)
                NOT_TAKEN

 293            LOAD_SMALL_INT           1
                RETURN_VALUE

 294   L16:     LOAD_SMALL_INT           0
                RETURN_VALUE

  --   L17:     PUSH_EXC_INFO

 260            LOAD_GLOBAL             54 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       56 (to L21)
                NOT_TAKEN
                STORE_FAST              10 (e)

 261   L18:     LOAD_FAST                7 (warnings)
                LOAD_ATTR               57 (append + NULL|self)
                LOAD_CONST              42 ('export aborted: ')
                LOAD_GLOBAL             59 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               60 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST              43 (': ')
                LOAD_FAST               10 (e)
                FORMAT_SIMPLE
                BUILD_STRING             4
                CALL                     1
                POP_TOP

 262            BUILD_LIST               0
                STORE_FAST               9 (rows)
       L19:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 327 (to L8)

  --   L20:     LOAD_CONST               4 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 260   L21:     RERAISE                  0

  --   L22:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L7 to L8 -> L17 [0]
  L17 to L18 -> L22 [1] lasti
  L18 to L19 -> L20 [1] lasti
  L20 to L22 -> L22 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C18025C30, file "scripts\export_events.py", line 292>:
 292           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                10 (to L3)
               STORE_FAST               1 (w)
               LOAD_CONST               0 ('export aborted')
               LOAD_FAST_BORROW         1 (w)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           12 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti
```
