# scripts_readiness/verify_backup

- **pyc:** `scripts\__pycache__\verify_backup.cpython-314.pyc`
- **expected source path (absent):** `scripts/verify_backup.py`
- **co_filename (from bytecode):** `C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS143D — Verify a backup directory before trusting it.

Runs the cheap, offline portion of restore-readiness:
  - manifest exists and is JSON
  - referenced dump file exists and is non-empty
  - SHA-256 matches the manifest's recorded hash
  - sibling pas_events JSONL (if present) parses + count matches manifest
  - if pg_restore is on PATH, run `pg_restore --list` against the dump
    to prove its table-of-contents is readable (no actual restore is run)

Writes verification_report.json into the backup directory.

`--strict` makes any of the failure modes terminate non-zero.

Usage:
  python scripts/verify_backup.py backups/20260509_141500/
  python scripts/verify_backup.py backups/20260509_141500/ --strict

Exit codes:
    0  — verification passed (warnings allowed unless --strict)
    1  — verification failed
    2  — bad CLI arguments
```

## Imports

`List`, `Optional`, `Path`, `Tuple`, `__future__`, `annotations`, `argparse`, `datetime`, `hashlib`, `json`, `pathlib`, `shutil`, `subprocess`, `sys`, `typing`

## Classes

`_Status`

## Functions / methods

`__annotate__`, `count_jsonl_rows`, `detect_pg_restore`, `load_json`, `main`, `pg_restore_toc_check`, `sha256_of_file`, `verify_backup`

## Env-key candidates

`FAIL`, `PASS`

## String constants (redacted where noted)

- "\nPAS143D — Verify a backup directory before trusting it.\n\nRuns the cheap, offline portion of restore-readiness:\n  - manifest exists and is JSON\n  - referenced dump file exists and is non-empty\n  - SHA-256 matches the manifest's recorded hash\n  - sibling pas_events JSONL (if present) parses + count matches manifest\n  - if pg_restore is on PATH, run `pg_restore --list` against the dump\n    to prove its table-of-contents is readable (no actual restore is run)\n\nWrites verification_report.json into the backup directory.\n\n`--strict` makes any of the failure modes terminate non-zero.\n\nUsage:\n  python scripts/verify_backup.py backups/20260509_141500/\n  python scripts/verify_backup.py backups/20260509_141500/ --strict\n\nExit codes:\n    0  — verification passed (warnings allowed unless --strict)\n    1  — verification failed\n    2  — bad CLI arguments\n"
- 'utf-8'
- '_Status'
- 'path'
- 'Path'
- 'return'
- 'str'
- 'Optional[dict]'
- 'Tuple[int, List[str]]'
- "\nReturn (count_of_valid_rows, list_of_parse_errors).\nEach parse error is a short string ('line N: <type>').\nEmpty files return (0, []).\n"
- 'file missing: '
- 'line '
- 'read failure: '
- 'bool'
- 'pg_restore'
- 'dump_path'
- 'Tuple[bool, str]'
- 'Run `pg_restore --list <dump>` to validate the table of contents.'
- '--list'
- 'Tiny accumulator so the report has a deterministic shape.'
- 'None'
- 'name'
- 'detail'
- 'PASS'
- 'FAIL'
- ' — '
- 'backup_dir'
- 'dict'
- '\nPure entry-point used by tests. Returns the report dict that\n`verification_report.json` records on disk. Never raises.\n'
- 'timestamp'
- 'tool'
- 'pas143d.verify_backup'
- 'checks'
- 'manifest'
- 'events'
- 'all_passed'
- 'Backup directory exists'
- 'backup_manifest.json'
- 'backup_manifest.json present + parses'
- 'missing or malformed'
- 'dump_file'
- 'Referenced dump file exists'
- 'missing'
- 'dump_size_bytes'
- 'Dump non-empty'
- ' bytes (manifest expected '
- 'sha256'
- 'Manifest carries sha256'
- 'field absent or empty'
- 'SHA-256 matches manifest'
- '… vs '
- 'pas_events.jsonl'
- 'export_manifest.json'
- 'Event manifest present ('
- 'row_count'
- 'Event JSONL parses ('
- ' valid row(s); '
- ' parse error(s)'
- 'Event row count matches manifest ('
- 'counted '
- ' vs manifest '
- 'parse_errors'
- 'pg_restore --list (dump TOC)'
- 'skipped (pg_restore not on PATH)'
- 'argv'
- 'Optional[list]'
- 'int'
- 'verify_backup'
- 'PAS143D — verify a backup directory before trusting it.'
- 'Path to the backup directory to verify.'
- '--strict'
- 'store_true'
- 'Fail with non-zero exit on any failed check (incl. checksum mismatch).'
- 'verification_report.json'
- '  report: '
- '  WARNING: could not write verification_report.json: '

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ("\nPAS143D — Verify a backup directory before trusting it.\n\nRuns the cheap, offline portion of restore-readiness:\n  - manifest exists and is JSON\n  - referenced dump file exists and is non-empty\n  - SHA-256 matches the manifest's recorded hash\n  - sibling pas_events JSONL (if present) parses + count matches manifest\n  - if pg_restore is on PATH, run `pg_restore --list` against the dump\n    to prove its table-of-contents is readable (no actual restore is run)\n\nWrites verification_report.json into the backup directory.\n\n`--strict` makes any of the failure modes terminate non-zero.\n\nUsage:\n  python scripts/verify_backup.py backups/20260509_141500/\n  python scripts/verify_backup.py backups/20260509_141500/ --strict\n\nExit codes:\n    0  — verification passed (warnings allowed unless --strict)\n    1  — verification failed\n    2  — bad CLI arguments\n")
               STORE_NAME               0 (__doc__)

  26           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  28           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  29           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (datetime)
               STORE_NAME               5 (_dt)

  30           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (hashlib)
               STORE_NAME               6 (hashlib)

  31           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (json)
               STORE_NAME               7 (json)

  32           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              8 (shutil)
               STORE_NAME               8 (shutil)

  33           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              9 (subprocess)
               STORE_NAME               9 (subprocess)

  34           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME             10 (sys)
               STORE_NAME              10 (sys)

  35           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('Path',))
               IMPORT_NAME             11 (pathlib)
               IMPORT_FROM             12 (Path)
               STORE_NAME              12 (Path)
               POP_TOP

  36           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('List', 'Optional', 'Tuple'))
               IMPORT_NAME             13 (typing)
               IMPORT_FROM             14 (List)
               STORE_NAME              14 (List)
               IMPORT_FROM             15 (Optional)
               STORE_NAME              15 (Optional)
               IMPORT_FROM             16 (Tuple)
               STORE_NAME              16 (Tuple)
               POP_TOP

  40           LOAD_NAME               10 (sys)
               LOAD_ATTR               34 (stdout)
               LOAD_NAME               10 (sys)
               LOAD_ATTR               36 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              19 (_stream)

  41           NOP

  42   L2:     LOAD_NAME               19 (_stream)
               LOAD_ATTR               41 (reconfigure + NULL|self)
               LOAD_CONST               5 ('utf-8')
               LOAD_CONST               6 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  40   L4:     END_FOR
               POP_ITER

  51           LOAD_CONST               7 (<code object __annotate__ at 0x0000018C17FA2F10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 51>)
               MAKE_FUNCTION
               LOAD_CONST               8 (<code object sha256_of_file at 0x0000018C17FEDC30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 51>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              22 (sha256_of_file)

  62           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA31E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 62>)
               MAKE_FUNCTION
               LOAD_CONST              10 (<code object load_json at 0x0000018C17FF13B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 62>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              23 (load_json)

  71           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA3780, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 71>)
               MAKE_FUNCTION
               LOAD_CONST              12 (<code object count_jsonl_rows at 0x0000018C17F2F290, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 71>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              24 (count_jsonl_rows)

  97           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA3E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 97>)
               MAKE_FUNCTION
               LOAD_CONST              14 (<code object detect_pg_restore at 0x0000018C1812C140, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 97>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              25 (detect_pg_restore)

 101           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA3A50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 101>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object pg_restore_toc_check at 0x0000018C17EC57C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 101>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              26 (pg_restore_toc_check)

 120           LOAD_BUILD_CLASS
               PUSH_NULL
               LOAD_CONST              17 (<code object _Status at 0x0000018C18053E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 120>)
               MAKE_FUNCTION
               LOAD_CONST              18 ('_Status')
               CALL                     2
               STORE_NAME              27 (_Status)

 140           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA3D20, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 140>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object verify_backup at 0x0000018C181B30E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 140>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (verify_backup)

 245           LOAD_CONST              24 ((None,))
               LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA2A60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 245>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object main at 0x0000018C17ED93D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 245>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              29 (main)

 277           LOAD_NAME               30 (__name__)
               LOAD_CONST              23 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       14 (to L5)
               NOT_TAKEN

 278           LOAD_NAME               31 (SystemExit)
               PUSH_NULL
               LOAD_NAME               29 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               RAISE_VARARGS            1

 277   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  43           LOAD_NAME               21 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

  44   L7:     POP_EXCEPT
               JUMP_BACKWARD          112 (to L1)

  43   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 51>:
 51           RESUME                   0
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

Disassembly of <code object sha256_of_file at 0x0000018C17FEDC30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 51>:
  --            MAKE_CELL                3 (f)

  51            RESUME                   0

  52            NOP

  53    L1:     LOAD_GLOBAL              0 (hashlib)
                LOAD_ATTR                2 (sha256)
                PUSH_NULL
                CALL                     0
                STORE_FAST               1 (h)

  54            LOAD_GLOBAL              5 (open + NULL)
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

  55            LOAD_GLOBAL              7 (iter + NULL)
                LOAD_FAST_BORROW         3 (f)
                BUILD_TUPLE              1
                LOAD_CONST               1 (<code object <lambda> at 0x0000018C18025530, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 55>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_CONST               2 (b'')
                CALL                     2
                GET_ITER
        L3:     FOR_ITER                20 (to L4)
                STORE_FAST               2 (chunk)

  56            LOAD_FAST_BORROW         1 (h)
                LOAD_ATTR                9 (update + NULL|self)
                LOAD_FAST_BORROW         2 (chunk)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           22 (to L3)

  55    L4:     END_FOR
                POP_ITER

  54    L5:     LOAD_CONST               3 (None)
                LOAD_CONST               3 (None)
                LOAD_CONST               3 (None)
                CALL                     3
                POP_TOP

  57    L6:     LOAD_FAST_BORROW         1 (h)
                LOAD_ATTR               11 (hexdigest + NULL|self)
                CALL                     0
        L7:     RETURN_VALUE

  54    L8:     PUSH_EXC_INFO
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

  58            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L14)
                NOT_TAKEN
                POP_TOP

  59   L13:     POP_EXCEPT
                LOAD_CONST               4 ('')
                RETURN_VALUE

  58   L14:     RERAISE                  0

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

Disassembly of <code object <lambda> at 0x0000018C18025530, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 55>:
  --           COPY_FREE_VARS           1

  55           RESUME                   0
               LOAD_DEREF               0 (f)
               LOAD_ATTR                1 (read + NULL|self)
               LOAD_CONST               1 (1048576)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 62>:
 62           RESUME                   0
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
              LOAD_CONST               4 ('Optional[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object load_json at 0x0000018C17FF13B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 62>:
  62           RESUME                   0

  63           LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (exists + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

  64           LOAD_CONST               0 (None)
               RETURN_VALUE

  65   L1:     NOP

  66   L2:     LOAD_GLOBAL              2 (json)
               LOAD_ATTR                4 (loads)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                7 (read_text + NULL|self)
               LOAD_CONST               1 ('utf-8')
               LOAD_CONST               2 (('encoding',))
               CALL_KW                  1
               CALL                     1
       L3:     RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

  67           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L6)
               NOT_TAKEN
               POP_TOP

  68   L5:     POP_EXCEPT
               LOAD_CONST               0 (None)
               RETURN_VALUE

  67   L6:     RERAISE                  0

  --   L7:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L4 [0]
  L4 to L5 -> L7 [1] lasti
  L6 to L7 -> L7 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 71>:
 71           RESUME                   0
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
              LOAD_CONST               4 ('Tuple[int, List[str]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object count_jsonl_rows at 0x0000018C17F2F290, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 71>:
  71            RESUME                   0

  77            BUILD_LIST               0
                STORE_FAST               1 (errors)

  78            LOAD_SMALL_INT           0
                STORE_FAST               2 (count)

  79            LOAD_FAST_BORROW         0 (path)
                LOAD_ATTR                1 (exists + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        19 (to L1)
                NOT_TAKEN

  80            LOAD_SMALL_INT           0
                LOAD_CONST               1 ('file missing: ')
                LOAD_FAST_BORROW         0 (path)
                LOAD_ATTR                2 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1
                BUILD_TUPLE              2
                RETURN_VALUE

  81    L1:     NOP

  82    L2:     LOAD_GLOBAL              5 (open + NULL)
                LOAD_FAST_BORROW         0 (path)
                LOAD_CONST               2 ('r')
                LOAD_CONST               3 ('utf-8')
                LOAD_CONST               4 (('encoding',))
                CALL_KW                  3
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L3:     STORE_FAST               3 (f)

  83            LOAD_GLOBAL              7 (enumerate + NULL)
                LOAD_FAST_BORROW         3 (f)
                LOAD_SMALL_INT           1
                LOAD_CONST               5 (('start',))
                CALL_KW                  2
                GET_ITER
        L4:     FOR_ITER                61 (to L8)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   69 (i, line)

  84            LOAD_FAST_BORROW         5 (line)
                LOAD_ATTR                9 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN

  86            JUMP_BACKWARD           29 (to L4)

  87    L5:     NOP

  88    L6:     LOAD_GLOBAL             10 (json)
                LOAD_ATTR               12 (loads)
                PUSH_NULL
                LOAD_FAST_BORROW         5 (line)
                CALL                     1
                POP_TOP

  89            LOAD_FAST_BORROW         2 (count)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               2 (count)
        L7:     JUMP_BACKWARD           63 (to L4)

  83    L8:     END_FOR
                POP_ITER

  82    L9:     LOAD_CONST               8 (None)
                LOAD_CONST               8 (None)
                LOAD_CONST               8 (None)
                CALL                     3
                POP_TOP

  94   L10:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (count, errors)
                BUILD_TUPLE              2
                RETURN_VALUE

  --   L11:     PUSH_EXC_INFO

  90            LOAD_GLOBAL             10 (json)
                LOAD_ATTR               14 (JSONDecodeError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       54 (to L15)
                NOT_TAKEN
                STORE_FAST               6 (e)

  91   L12:     LOAD_FAST                1 (errors)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_CONST               6 ('line ')
                LOAD_FAST                4 (i)
                FORMAT_SIMPLE
                LOAD_CONST               7 (': ')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             4
                CALL                     1
                POP_TOP
       L13:     POP_EXCEPT
                LOAD_CONST               8 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                JUMP_BACKWARD          145 (to L4)

  --   L14:     LOAD_CONST               8 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

  90   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

  82   L17:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L18)
                NOT_TAKEN
                RERAISE                  2
       L18:     POP_TOP
       L19:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP

  94   L20:     LOAD_FAST_LOAD_FAST     33 (count, errors)
                BUILD_TUPLE              2
                RETURN_VALUE

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L22:     PUSH_EXC_INFO

  92            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L26)
                NOT_TAKEN
                STORE_FAST               6 (e)

  93   L23:     LOAD_FAST                1 (errors)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_CONST               9 ('read failure: ')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST               7 (': ')
                LOAD_FAST                6 (e)
                FORMAT_SIMPLE
                BUILD_STRING             4
                CALL                     1
                POP_TOP
       L24:     POP_EXCEPT
                LOAD_CONST               8 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)

  94            LOAD_FAST_LOAD_FAST     33 (count, errors)
                BUILD_TUPLE              2
                RETURN_VALUE

  --   L25:     LOAD_CONST               8 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

  92   L26:     RERAISE                  0

  --   L27:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L22 [0]
  L3 to L5 -> L17 [2] lasti
  L6 to L7 -> L11 [3]
  L7 to L9 -> L17 [2] lasti
  L9 to L10 -> L22 [0]
  L11 to L12 -> L16 [4] lasti
  L12 to L13 -> L14 [4] lasti
  L13 to L14 -> L17 [2] lasti
  L14 to L16 -> L16 [4] lasti
  L16 to L17 -> L17 [2] lasti
  L17 to L19 -> L21 [4] lasti
  L19 to L20 -> L22 [0]
  L21 to L22 -> L22 [0]
  L22 to L23 -> L27 [1] lasti
  L23 to L24 -> L25 [1] lasti
  L25 to L27 -> L27 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 97>:
 97           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('bool')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object detect_pg_restore at 0x0000018C1812C140, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 97>:
 97           RESUME                   0

 98           LOAD_GLOBAL              0 (shutil)
              LOAD_ATTR                2 (which)
              PUSH_NULL
              LOAD_CONST               0 ('pg_restore')
              CALL                     1
              LOAD_CONST               1 (None)
              IS_OP                    1 (is not)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 101>:
101           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('dump_path')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Tuple[bool, str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object pg_restore_toc_check at 0x0000018C17EC57C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 101>:
 101            RESUME                   0

 103            NOP

 104    L1:     LOAD_GLOBAL              0 (subprocess)
                LOAD_ATTR                2 (run)
                PUSH_NULL

 105            LOAD_CONST               1 ('pg_restore')
                LOAD_CONST               2 ('--list')
                LOAD_GLOBAL              5 (str + NULL)
                LOAD_FAST_BORROW         0 (dump_path)
                CALL                     1
                BUILD_LIST               3

 106            LOAD_CONST               3 (True)
                LOAD_CONST               3 (True)
                LOAD_CONST               4 (False)
                LOAD_SMALL_INT          60

 104            LOAD_CONST               5 (('capture_output', 'text', 'check', 'timeout'))
                CALL_KW                  5
                STORE_FAST               1 (out)

 110    L2:     LOAD_FAST                1 (out)
                LOAD_ATTR               12 (returncode)
                LOAD_SMALL_INT           0
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       46 (to L4)
                NOT_TAKEN

 112            LOAD_CONST               4 (False)
                LOAD_FAST                1 (out)
                LOAD_ATTR               14 (stderr)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               8 ('')
        L3:     LOAD_CONST               9 (slice(None, 500, None))
                BINARY_OP               26 ([])
                LOAD_ATTR               17 (strip + NULL|self)
                CALL                     0
                BUILD_TUPLE              2
                RETURN_VALUE

 113    L4:     LOAD_CONST              10 ((True, 'TOC readable'))
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 108            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       39 (to L10)
                NOT_TAKEN
                STORE_FAST               2 (e)

 109    L6:     LOAD_CONST               4 (False)
                LOAD_GLOBAL              9 (type + NULL)
                LOAD_FAST                2 (e)
                CALL                     1
                LOAD_ATTR               10 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST               6 (': ')
                LOAD_FAST                2 (e)
                FORMAT_SIMPLE
                BUILD_STRING             3
                BUILD_TUPLE              2
        L7:     SWAP                     2
        L8:     POP_EXCEPT
                LOAD_CONST               7 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                RETURN_VALUE

  --    L9:     LOAD_CONST               7 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                RERAISE                  1

 108   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L11 [1] lasti
  L6 to L7 -> L9 [1] lasti
  L7 to L8 -> L11 [1] lasti
  L9 to L11 -> L11 [1] lasti

Disassembly of <code object _Status at 0x0000018C18053E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 120>:
120           RESUME                   0
              LOAD_NAME                0 (__name__)
              STORE_NAME               1 (__module__)
              LOAD_CONST               0 ('_Status')
              STORE_NAME               2 (__qualname__)
              LOAD_SMALL_INT         120
              STORE_NAME               3 (__firstlineno__)

121           LOAD_CONST               1 ('Tiny accumulator so the report has a deterministic shape.')
              STORE_NAME               4 (__doc__)

123           LOAD_CONST               2 (<code object __annotate__ at 0x0000018C17FA3F00, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 123>)
              MAKE_FUNCTION
              LOAD_CONST               3 (<code object __init__ at 0x0000018C17FA3960, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 123>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME               5 (__init__)

126           LOAD_CONST              10 (('',))
              LOAD_CONST               4 (<code object __annotate__ at 0x0000018C18024B30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 126>)
              MAKE_FUNCTION
              LOAD_CONST               5 (<code object add at 0x0000018C17FA92F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 126>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME               6 (add)

135           LOAD_NAME                7 (property)

136           LOAD_CONST               6 (<code object __annotate__ at 0x0000018C17FA3C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 136>)
              MAKE_FUNCTION
              LOAD_CONST               7 (<code object all_passed at 0x0000018C17F96140, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 135>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)

135           CALL                     0

136           STORE_NAME               8 (all_passed)
              LOAD_CONST               8 (('checks',))
              STORE_NAME               9 (__static_attributes__)
              LOAD_CONST               9 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 123>:
123           RESUME                   0
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

Disassembly of <code object __init__ at 0x0000018C17FA3960, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 123>:
123           RESUME                   0

124           BUILD_LIST               0
              LOAD_FAST_BORROW         0 (self)
              STORE_ATTR               0 (checks)
              LOAD_CONST               0 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 126>:
126           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('name')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('ok')
              LOAD_CONST               4 ('bool')
              LOAD_CONST               5 ('detail')
              LOAD_CONST               2 ('str')
              LOAD_CONST               6 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object add at 0x0000018C17FA92F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 126>:
126           RESUME                   0

127           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (checks)
              LOAD_ATTR                3 (append + NULL|self)
              LOAD_CONST               0 ('name')
              LOAD_FAST_BORROW         1 (name)
              LOAD_CONST               1 ('ok')
              LOAD_GLOBAL              5 (bool + NULL)
              LOAD_FAST_BORROW         2 (ok)
              CALL                     1
              LOAD_CONST               2 ('detail')
              LOAD_FAST_BORROW         3 (detail)
              BUILD_MAP                3
              CALL                     1
              POP_TOP

128           LOAD_FAST_BORROW         2 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_CONST               3 ('PASS')
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               4 ('FAIL')
      L2:     STORE_FAST               4 (tag)

129           LOAD_CONST               5 ('[')
              LOAD_FAST_BORROW         4 (tag)
              FORMAT_SIMPLE
              LOAD_CONST               6 ('] ')
              LOAD_FAST_BORROW         1 (name)
              FORMAT_SIMPLE
              BUILD_STRING             4
              STORE_FAST               5 (line)

130           LOAD_FAST_BORROW         3 (detail)
              TO_BOOL
              POP_JUMP_IF_FALSE       13 (to L3)
              NOT_TAKEN

131           LOAD_FAST_BORROW         5 (line)
              LOAD_CONST               7 (' — ')
              LOAD_FAST_BORROW         3 (detail)
              FORMAT_SIMPLE
              BUILD_STRING             2
              BINARY_OP               13 (+=)
              STORE_FAST               5 (line)

132   L3:     LOAD_GLOBAL              7 (print + NULL)
              LOAD_FAST_BORROW         5 (line)
              CALL                     1
              POP_TOP

133           LOAD_FAST_BORROW         2 (ok)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 136>:
136           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('bool')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object all_passed at 0x0000018C17F96140, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 135>:
135           RESUME                   0

137           LOAD_GLOBAL              0 (all)
              COPY                     1
              LOAD_COMMON_CONSTANT     3 (<built-in function all>)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE       38 (to L4)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               0 (<code object <genexpr> at 0x0000018C1812C250, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 137>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                2 (checks)
              GET_ITER
              CALL                     0
      L1:     FOR_ITER                12 (to L3)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L1)
      L2:     POP_ITER
              LOAD_CONST               1 (False)
              RETURN_VALUE
      L3:     END_FOR
              POP_ITER
              LOAD_CONST               2 (True)
              RETURN_VALUE
      L4:     PUSH_NULL
              LOAD_CONST               0 (<code object <genexpr> at 0x0000018C1812C250, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 137>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                2 (checks)
              GET_ITER
              CALL                     0
              CALL                     1
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C1812C250, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 137>:
 137           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                13 (to L3)
               STORE_FAST_LOAD_FAST    17 (c, c)
               LOAD_CONST               0 ('ok')
               BINARY_OP               26 ([])
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           15 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 140>:
140           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('backup_dir')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('dict')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object verify_backup at 0x0000018C181B30E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 140>:
140            RESUME                   0

145            LOAD_GLOBAL              1 (_Status + NULL)
               CALL                     0
               STORE_FAST               1 (s)

147            LOAD_CONST               1 ('backup_dir')
               LOAD_GLOBAL              3 (str + NULL)
               LOAD_FAST_BORROW         0 (backup_dir)
               CALL                     1

148            LOAD_CONST               2 ('timestamp')
               LOAD_GLOBAL              4 (_dt)
               LOAD_ATTR                6 (datetime)
               LOAD_ATTR                9 (now + NULL|self)
               LOAD_GLOBAL              4 (_dt)
               LOAD_ATTR               10 (timezone)
               LOAD_ATTR               12 (utc)
               CALL                     1
               LOAD_ATTR               15 (isoformat + NULL|self)
               CALL                     0

149            LOAD_CONST               3 ('tool')
               LOAD_CONST               4 ('pas143d.verify_backup')

150            LOAD_CONST               5 ('checks')
               BUILD_LIST               0

151            LOAD_CONST               6 ('manifest')
               LOAD_CONST               7 (None)

152            LOAD_CONST               8 ('events')
               BUILD_LIST               0

153            LOAD_CONST               9 ('all_passed')
               LOAD_CONST              10 (False)

146            BUILD_MAP                7
               STORE_FAST               2 (findings)

156            LOAD_FAST_BORROW         0 (backup_dir)
               LOAD_ATTR               17 (exists + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L1)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (backup_dir)
               LOAD_ATTR               19 (is_dir + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        46 (to L2)
               NOT_TAKEN

157    L1:     LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR               21 (add + NULL|self)
               LOAD_CONST              11 ('Backup directory exists')
               LOAD_CONST              10 (False)
               LOAD_GLOBAL              3 (str + NULL)
               LOAD_FAST_BORROW         0 (backup_dir)
               CALL                     1
               CALL                     3
               POP_TOP

158            LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR               22 (checks)
               LOAD_FAST_BORROW         2 (findings)
               LOAD_CONST               5 ('checks')
               STORE_SUBSCR

159            LOAD_FAST_BORROW         2 (findings)
               RETURN_VALUE

160    L2:     LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR               21 (add + NULL|self)
               LOAD_CONST              11 ('Backup directory exists')
               LOAD_CONST              12 (True)
               LOAD_GLOBAL              3 (str + NULL)
               LOAD_FAST_BORROW         0 (backup_dir)
               CALL                     1
               CALL                     3
               POP_TOP

163            LOAD_FAST_BORROW         0 (backup_dir)
               LOAD_CONST              13 ('backup_manifest.json')
               BINARY_OP               11 (/)
               STORE_FAST               3 (manifest_path)

164            LOAD_GLOBAL             25 (load_json + NULL)
               LOAD_FAST_BORROW         3 (manifest_path)
               CALL                     1
               STORE_FAST               4 (manifest)

165            LOAD_FAST_BORROW         4 (manifest)
               POP_JUMP_IF_NOT_NONE    37 (to L3)
               NOT_TAKEN

166            LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR               21 (add + NULL|self)
               LOAD_CONST              14 ('backup_manifest.json present + parses')
               LOAD_CONST              10 (False)

167            LOAD_CONST              15 ('missing or malformed')

166            CALL                     3
               POP_TOP

168            LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR               22 (checks)
               LOAD_FAST_BORROW         2 (findings)
               LOAD_CONST               5 ('checks')
               STORE_SUBSCR

169            LOAD_FAST_BORROW         2 (findings)
               RETURN_VALUE

170    L3:     LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR               21 (add + NULL|self)
               LOAD_CONST              14 ('backup_manifest.json present + parses')
               LOAD_CONST              12 (True)
               CALL                     2
               POP_TOP

171            LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (manifest, findings)
               LOAD_CONST               6 ('manifest')
               STORE_SUBSCR

174            LOAD_FAST_BORROW         4 (manifest)
               LOAD_ATTR               27 (get + NULL|self)
               LOAD_CONST              16 ('dump_file')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              17 ('')
       L4:     STORE_FAST               5 (dump_name)

175            LOAD_FAST_BORROW         5 (dump_name)
               TO_BOOL
               POP_JUMP_IF_FALSE        9 (to L5)
               NOT_TAKEN
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (backup_dir, dump_name)
               BINARY_OP               11 (/)
               JUMP_FORWARD             1 (to L6)
       L5:     LOAD_CONST               7 (None)
       L6:     STORE_FAST               6 (dump_path)

176            LOAD_FAST_BORROW         5 (dump_name)
               TO_BOOL
               POP_JUMP_IF_FALSE       27 (to L7)
               NOT_TAKEN
               LOAD_FAST_BORROW         6 (dump_path)
               POP_JUMP_IF_NONE        23 (to L7)
               NOT_TAKEN
               LOAD_FAST_BORROW         6 (dump_path)
               LOAD_ATTR               17 (exists + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        47 (to L9)
               NOT_TAKEN

177    L7:     LOAD_FAST                1 (s)
               LOAD_ATTR               21 (add + NULL|self)
               LOAD_CONST              18 ('Referenced dump file exists')
               LOAD_CONST              10 (False)
               LOAD_FAST                5 (dump_name)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              19 ('missing')
       L8:     CALL                     3
               POP_TOP

178            LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR               22 (checks)
               LOAD_FAST_BORROW         2 (findings)
               LOAD_CONST               5 ('checks')
               STORE_SUBSCR

179            LOAD_FAST_BORROW         2 (findings)
               RETURN_VALUE

180    L9:     LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR               21 (add + NULL|self)
               LOAD_CONST              18 ('Referenced dump file exists')
               LOAD_CONST              12 (True)
               LOAD_FAST_BORROW         6 (dump_path)
               LOAD_ATTR               28 (name)
               CALL                     3
               POP_TOP

183            LOAD_FAST_BORROW         6 (dump_path)
               LOAD_ATTR               31 (stat + NULL|self)
               CALL                     0
               LOAD_ATTR               32 (st_size)
               STORE_FAST               7 (size)

184            LOAD_FAST_BORROW         4 (manifest)
               LOAD_ATTR               27 (get + NULL|self)
               LOAD_CONST              20 ('dump_size_bytes')
               LOAD_SMALL_INT           0
               CALL                     2
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L10)
               NOT_TAKEN
               POP_TOP
               LOAD_SMALL_INT           0
      L10:     STORE_FAST               8 (expected_size)

185            LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR               21 (add + NULL|self)
               LOAD_CONST              21 ('Dump non-empty')
               LOAD_FAST_BORROW         7 (size)
               LOAD_SMALL_INT           0
               COMPARE_OP             132 (>)
               LOAD_FAST_BORROW         7 (size)
               FORMAT_SIMPLE
               LOAD_CONST              22 (' bytes (manifest expected ')
               LOAD_FAST_BORROW         8 (expected_size)
               FORMAT_SIMPLE
               LOAD_CONST              23 (')')
               BUILD_STRING             4
               CALL                     3
               POP_TOP

188            LOAD_GLOBAL             35 (sha256_of_file + NULL)
               LOAD_FAST_BORROW         6 (dump_path)
               CALL                     1
               STORE_FAST               9 (actual)

189            LOAD_FAST_BORROW         4 (manifest)
               LOAD_ATTR               27 (get + NULL|self)
               LOAD_CONST              24 ('sha256')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L11)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              17 ('')
      L11:     STORE_FAST              10 (expected)

190            LOAD_FAST_BORROW        10 (expected)
               TO_BOOL
               POP_JUMP_IF_TRUE        21 (to L12)
               NOT_TAKEN

191            LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR               21 (add + NULL|self)
               LOAD_CONST              25 ('Manifest carries sha256')
               LOAD_CONST              10 (False)
               LOAD_CONST              26 ('field absent or empty')
               CALL                     3
               POP_TOP
               JUMP_FORWARD            41 (to L13)

193   L12:     LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR               21 (add + NULL|self)

194            LOAD_CONST              27 ('SHA-256 matches manifest')

195            LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (actual, expected)
               COMPARE_OP              72 (==)

196            LOAD_FAST_BORROW         9 (actual)
               LOAD_CONST              28 (slice(None, 12, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST              29 ('… vs ')
               LOAD_FAST_BORROW        10 (expected)
               LOAD_CONST              28 (slice(None, 12, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST              30 ('…')
               BUILD_STRING             4

193            CALL                     3
               POP_TOP

200   L13:     LOAD_FAST_BORROW         0 (backup_dir)
               LOAD_CONST               8 ('events')
               BINARY_OP               11 (/)
               STORE_FAST              11 (events_dir)

201            LOAD_FAST_BORROW        11 (events_dir)
               LOAD_ATTR               17 (exists + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_FALSE       27 (to L14)
               NOT_TAKEN
               LOAD_GLOBAL             37 (list + NULL)
               LOAD_FAST_BORROW        11 (events_dir)
               LOAD_ATTR               39 (rglob + NULL|self)
               LOAD_CONST              31 ('pas_events.jsonl')
               CALL                     1
               CALL                     1
               JUMP_FORWARD             1 (to L15)
      L14:     BUILD_LIST               0
      L15:     STORE_FAST              12 (event_jsonls)

202            LOAD_FAST_BORROW        12 (event_jsonls)
               GET_ITER
      L16:     EXTENDED_ARG             1
               FOR_ITER               271 (to L18)
               STORE_FAST              13 (ev_path)

203            LOAD_FAST_BORROW        13 (ev_path)
               LOAD_ATTR               40 (parent)
               LOAD_CONST              32 ('export_manifest.json')
               BINARY_OP               11 (/)
               STORE_FAST              14 (ev_manifest_path)

204            LOAD_GLOBAL             25 (load_json + NULL)
               LOAD_FAST_BORROW        14 (ev_manifest_path)
               CALL                     1
               STORE_FAST              15 (ev_manifest)

205            LOAD_FAST_BORROW        15 (ev_manifest)
               POP_JUMP_IF_NOT_NONE    46 (to L17)
               NOT_TAKEN

206            LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR               21 (add + NULL|self)
               LOAD_CONST              33 ('Event manifest present (')
               LOAD_FAST_BORROW        13 (ev_path)
               LOAD_ATTR               40 (parent)
               LOAD_ATTR               28 (name)
               FORMAT_SIMPLE
               LOAD_CONST              23 (')')
               BUILD_STRING             3

207            LOAD_CONST              10 (False)
               LOAD_CONST              15 ('missing or malformed')

206            CALL                     3
               POP_TOP

208            JUMP_BACKWARD           83 (to L16)

209   L17:     LOAD_GLOBAL             43 (count_jsonl_rows + NULL)
               LOAD_FAST_BORROW        13 (ev_path)
               CALL                     1
               UNPACK_SEQUENCE          2
               STORE_FAST              16 (n)
               STORE_FAST              17 (parse_errors)

210            LOAD_FAST_BORROW        15 (ev_manifest)
               LOAD_ATTR               27 (get + NULL|self)
               LOAD_CONST              34 ('row_count')
               LOAD_CONST              45 (-1)
               CALL                     2
               STORE_FAST              18 (recorded)

211            LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR               21 (add + NULL|self)

212            LOAD_CONST              35 ('Event JSONL parses (')
               LOAD_FAST_BORROW        13 (ev_path)
               LOAD_ATTR               40 (parent)
               LOAD_ATTR               28 (name)
               FORMAT_SIMPLE
               LOAD_CONST              23 (')')
               BUILD_STRING             3

213            LOAD_FAST_BORROW        17 (parse_errors)
               TO_BOOL
               UNARY_NOT

214            LOAD_FAST_BORROW        16 (n)
               FORMAT_SIMPLE
               LOAD_CONST              36 (' valid row(s); ')
               LOAD_GLOBAL             45 (len + NULL)
               LOAD_FAST_BORROW        17 (parse_errors)
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              37 (' parse error(s)')
               BUILD_STRING             4

211            CALL                     3
               POP_TOP

216            LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR               21 (add + NULL|self)

217            LOAD_CONST              38 ('Event row count matches manifest (')
               LOAD_FAST_BORROW        13 (ev_path)
               LOAD_ATTR               40 (parent)
               LOAD_ATTR               28 (name)
               FORMAT_SIMPLE
               LOAD_CONST              23 (')')
               BUILD_STRING             3

218            LOAD_FAST_BORROW        16 (n)
               LOAD_FAST_BORROW        18 (recorded)
               COMPARE_OP              72 (==)

219            LOAD_CONST              39 ('counted ')
               LOAD_FAST_BORROW        16 (n)
               FORMAT_SIMPLE
               LOAD_CONST              40 (' vs manifest ')
               LOAD_FAST_BORROW        18 (recorded)
               FORMAT_SIMPLE
               BUILD_STRING             4

216            CALL                     3
               POP_TOP

221            LOAD_FAST_BORROW         2 (findings)
               LOAD_CONST               8 ('events')
               BINARY_OP               26 ([])
               LOAD_ATTR               47 (append + NULL|self)

222            LOAD_CONST              41 ('path')
               LOAD_GLOBAL              3 (str + NULL)
               LOAD_FAST_BORROW        13 (ev_path)
               CALL                     1

223            LOAD_CONST              34 ('row_count')
               LOAD_FAST_BORROW        16 (n)

224            LOAD_CONST              42 ('parse_errors')
               LOAD_FAST_BORROW        17 (parse_errors)

225            LOAD_CONST               6 ('manifest')
               LOAD_FAST_BORROW        15 (ev_manifest)

221            BUILD_MAP                4
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          274 (to L16)

202   L18:     END_FOR
               POP_ITER

229            LOAD_GLOBAL             49 (detect_pg_restore + NULL)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_FALSE       35 (to L19)
               NOT_TAKEN

230            LOAD_GLOBAL             51 (pg_restore_toc_check + NULL)
               LOAD_FAST_BORROW         6 (dump_path)
               CALL                     1
               UNPACK_SEQUENCE          2
               STORE_FAST              19 (ok)
               STORE_FAST              20 (detail)

231            LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR               21 (add + NULL|self)
               LOAD_CONST              43 ('pg_restore --list (dump TOC)')
               LOAD_FAST_BORROW        19 (ok)
               LOAD_FAST_BORROW        20 (detail)
               CALL                     3
               POP_TOP
               JUMP_FORWARD            19 (to L20)

234   L19:     LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR               21 (add + NULL|self)
               LOAD_CONST              43 ('pg_restore --list (dump TOC)')
               LOAD_CONST              12 (True)
               LOAD_CONST              44 ('skipped (pg_restore not on PATH)')
               CALL                     3
               POP_TOP

236   L20:     LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR               22 (checks)
               LOAD_FAST_BORROW         2 (findings)
               LOAD_CONST               5 ('checks')
               STORE_SUBSCR

237            LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR               52 (all_passed)
               LOAD_FAST_BORROW         2 (findings)
               LOAD_CONST               9 ('all_passed')
               STORE_SUBSCR

238            LOAD_FAST_BORROW         2 (findings)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 245>:
245           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17ED93D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\verify_backup.py", line 245>:
 245            RESUME                   0

 246            LOAD_GLOBAL              0 (argparse)
                LOAD_ATTR                2 (ArgumentParser)
                PUSH_NULL

 247            LOAD_CONST               0 ('verify_backup')

 248            LOAD_CONST               1 ('PAS143D — verify a backup directory before trusting it.')

 246            LOAD_CONST               2 (('prog', 'description'))
                CALL_KW                  2
                STORE_FAST               1 (parser)

 250            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST               3 ('backup_dir')
                LOAD_CONST               4 ('Path to the backup directory to verify.')
                LOAD_CONST               5 (('help',))
                CALL_KW                  2
                POP_TOP

 251            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 252            LOAD_CONST               6 ('--strict')
                LOAD_CONST               7 ('store_true')

 253            LOAD_CONST               8 ('Fail with non-zero exit on any failed check (incl. checksum mismatch).')

 251            LOAD_CONST               9 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 255            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                7 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 257            LOAD_GLOBAL              9 (Path + NULL)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               10 (backup_dir)
                CALL                     1
                STORE_FAST               3 (backup_dir)

 258            LOAD_GLOBAL             13 (verify_backup + NULL)
                LOAD_FAST_BORROW         3 (backup_dir)
                CALL                     1
                STORE_FAST               4 (findings)

 262            LOAD_FAST_BORROW         3 (backup_dir)
                LOAD_ATTR               15 (exists + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       88 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (backup_dir)
                LOAD_ATTR               17 (is_dir + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       66 (to L2)
                NOT_TAKEN

 263            LOAD_FAST_BORROW         3 (backup_dir)
                LOAD_CONST              10 ('verification_report.json')
                BINARY_OP               11 (/)
                STORE_FAST               5 (report_path)

 264            NOP

 265    L1:     LOAD_FAST_BORROW         5 (report_path)
                LOAD_ATTR               19 (write_text + NULL|self)
                LOAD_GLOBAL             20 (json)
                LOAD_ATTR               22 (dumps)
                PUSH_NULL
                LOAD_FAST_BORROW         4 (findings)
                LOAD_SMALL_INT           2
                LOAD_CONST              11 (('indent',))
                CALL_KW                  2
                LOAD_CONST              12 ('utf-8')
                LOAD_CONST              13 (('encoding',))
                CALL_KW                  2
                POP_TOP

 266            LOAD_GLOBAL             25 (print + NULL)
                LOAD_CONST              14 ('  report: ')
                LOAD_FAST_BORROW         5 (report_path)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 271    L2:     LOAD_GLOBAL             33 (bool + NULL)
                LOAD_FAST_BORROW         4 (findings)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST              18 ('all_passed')
                CALL                     1
                CALL                     1
                STORE_FAST               7 (ok)

 272            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               36 (strict)
                TO_BOOL
                POP_JUMP_IF_FALSE       11 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         7 (ok)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN

 273            LOAD_SMALL_INT           1
                RETURN_VALUE

 274    L3:     LOAD_FAST_BORROW         7 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_SMALL_INT           0
                RETURN_VALUE
        L4:     LOAD_SMALL_INT           1
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 267            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       41 (to L9)
                NOT_TAKEN
                STORE_FAST               6 (e)

 268    L6:     LOAD_GLOBAL             25 (print + NULL)
                LOAD_CONST              15 ('  WARNING: could not write verification_report.json: ')
                LOAD_FAST                6 (e)
                FORMAT_SIMPLE
                BUILD_STRING             2

 269            LOAD_GLOBAL             28 (sys)
                LOAD_ATTR               30 (stderr)

 268            LOAD_CONST              16 (('file',))
                CALL_KW                  2
                POP_TOP
        L7:     POP_EXCEPT
                LOAD_CONST              17 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                JUMP_BACKWARD_NO_INTERRUPT 112 (to L2)

  --    L8:     LOAD_CONST              17 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 267    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L10 [1] lasti
  L6 to L7 -> L8 [1] lasti
  L8 to L10 -> L10 [1] lasti
```
