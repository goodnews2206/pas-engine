# scripts_readiness/backup_database

- **pyc:** `scripts\__pycache__\backup_database.cpython-314.pyc`
- **expected source path (absent):** `scripts/backup_database.py`
- **co_filename (from bytecode):** `scripts\backup_database.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS143D — Operator-initiated PostgreSQL backup wrapper.

Reads SUPABASE_DB_URL (preferred) or DATABASE_URL from the env, then
shells out to `pg_dump` (custom format) and writes the dump + a
manifest + a SHA-256 checksum into ./backups/YYYYMMDD_HHMMSS/.

Safety contract:
  - Never prints the full DB URL.
  - Never logs passwords.
  - Refuses production unless --confirm-production is explicitly passed.
    Production is detected by hostname containing 'prod', 'production',
    or 'live'.
  - --dry-run prints what would happen without invoking pg_dump.
  - Does NOT upload backups anywhere.

Usage:
  python scripts/backup_database.py --dry-run
  python scripts/backup_database.py
  python scripts/backup_database.py --confirm-production
  python scripts/backup_database.py --schema-only
  python scripts/backup_database.py --data-only
  python scripts/backup_database.py --output-dir /custom/path

Exit codes:
    0  — backup written + manifest valid (or --dry-run succeeded)
    2  — bad CLI arguments
    3  — DB URL missing
    4  — production refused without --confirm-production
    5  — pg_dump missing or failed
```

## Imports

`Optional`, `Path`, `Tuple`, `__future__`, `annotations`, `argparse`, `datetime`, `hashlib`, `json`, `os`, `pathlib`, `shutil`, `subprocess`, `sys`, `typing`, `urllib.parse`, `urlparse`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_pg_dump_cmd`, `_print_status`, `_resolve_output_dir`, `build_manifest`, `detect_pg_dump_version`, `is_production_url`, `main`, `mask_db_url`, `now_stamp`, `resolve_db_url`, `sha256_of_file`

## Env-key candidates

`DATABASE_URL`, `FAIL`, `PASS`, `SUPABASE_DB_URL`

## String constants (redacted where noted)

- "\nPAS143D — Operator-initiated PostgreSQL backup wrapper.\n\nReads SUPABASE_DB_URL (preferred) or DATABASE_URL from the env, then\nshells out to `pg_dump` (custom format) and writes the dump + a\nmanifest + a SHA-256 checksum into ./backups/YYYYMMDD_HHMMSS/.\n\nSafety contract:\n  - Never prints the full DB URL.\n  - Never logs passwords.\n  - Refuses production unless --confirm-production is explicitly passed.\n    Production is detected by hostname containing 'prod', 'production',\n    or 'live'.\n  - --dry-run prints what would happen without invoking pg_dump.\n  - Does NOT upload backups anywhere.\n\nUsage:\n  python scripts/backup_database.py --dry-run\n  python scripts/backup_database.py\n  python scripts/backup_database.py --confirm-production\n  python scripts/backup_database.py --schema-only\n  python scripts/backup_database.py --data-only\n  python scripts/backup_database.py --output-dir /custom/path\n\nExit codes:\n    0  — backup written + manifest valid (or --dry-run succeeded)\n    2  — bad CLI arguments\n    3  — DB URL missing\n    4  — production refused without --confirm-production\n    5  — pg_dump missing or failed\n"
- 'utf-8'
- 'return'
- 'Optional[str]'
- '\nReturn the operator-supplied DB URL or None.\n\nPreference order:\n  1. SUPABASE_DB_URL  — explicit, recommended\n  2. DATABASE_URL     — generic Postgres convention\n\nBoth are read directly from os.environ; neither is required to\nexist anywhere else in the codebase.\n'
- 'SUPABASE_DB_URL'
- 'DATABASE_URL'
- 'url'
- 'str'
- "\nRender a DB URL with password + most of the host stripped out.\nThe password between ':' and '@' is replaced with '***'. The host\nkeeps its top-level token only (rest is replaced with '...').\nExample:\n  'postgresql://postgres:secret@db.live.supabase.co:5432/postgres'\n  → 'postgresql://postgres:***@***.supabase.co:5432/postgres'\n"
- 'postgresql'
- 'postgres'
- '***.'
- '***'
- '://'
- ':***@'
- '<masked>'
- 'bool'
- '\nReturn True iff the host portion of `url` contains any production\ntoken. Operator must explicitly opt in with --confirm-production\nbefore the backup proceeds.\n'
- 'path'
- 'Path'
- "Stream-hash a file; never raises (returns '' on error)."
- 'Return `pg_dump --version` first line, or None when not on PATH.'
- 'pg_dump'
- '--version'
- '%Y%m%d_%H%M%S'
- 'timestamp'
- 'db_url'
- 'mode'
- 'schema_only'
- 'data_only'
- 'dump_path'
- 'dump_size_bytes'
- 'int'
- 'sha256'
- 'pg_dump_version'
- 'dict'
- 'Pure manifest builder; tests assert on the shape it returns.'
- 'hostname'
- 'dump_file'
- 'tool'
- 'pas143d.backup_database'
- 'label'
- 'detail'
- 'None'
- 'PASS'
- 'FAIL'
- ' — '
- 'list'
- "\nCompose the pg_dump argv. Custom format ('-F c') for restore-friendly\noutput. -w avoids pg_dump prompting for a password (must be in URL).\n"
- '--schema-only'
- '--data-only'
- 'arg_value'
- 'backups'
- 'argv'
- 'Optional[list]'
- 'backup_database'
- 'PAS143D — operator-initiated PostgreSQL backup wrapper.'
- '--dry-run'
- 'store_true'
- 'Print what would happen without invoking pg_dump.'
- '--confirm-production'
- 'REQUIRED to run against a production-looking host.'
- '--output-dir'
- 'Override the default ./backups/ root.'
- 'Dump schema only (no row data).'
- 'Dump data only (no schema definitions).'
- '--schema-only and --data-only are mutually exclusive.'
- 'DB URL resolution'
- 'Set SUPABASE_DB_URL or DATABASE_URL before running.'
- 'DB URL resolved'
- 'Production safety'
- 'Host looks like production. Re-run with --confirm-production.'
- 'confirmed'
- 'non-production host'
- 'Output directory'
- 'pas_'
- '.dump'
- 'pg_dump availability'
- 'not installed'
- 'dry-run'
- 'Dry-run manifest preview'
- 'pg_dump missing'
- 'Install postgresql-client or use --dry-run.'
- '  $ '
- 'pg_dump invocation'
- '<DB_URL_REDACTED>'
- 'pg_dump exit'
- 'rc='
- 'live'
- 'backup_manifest.json'
- 'Backup complete'
- ' bytes), sha256='
- '  manifest: '

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ("\nPAS143D — Operator-initiated PostgreSQL backup wrapper.\n\nReads SUPABASE_DB_URL (preferred) or DATABASE_URL from the env, then\nshells out to `pg_dump` (custom format) and writes the dump + a\nmanifest + a SHA-256 checksum into ./backups/YYYYMMDD_HHMMSS/.\n\nSafety contract:\n  - Never prints the full DB URL.\n  - Never logs passwords.\n  - Refuses production unless --confirm-production is explicitly passed.\n    Production is detected by hostname containing 'prod', 'production',\n    or 'live'.\n  - --dry-run prints what would happen without invoking pg_dump.\n  - Does NOT upload backups anywhere.\n\nUsage:\n  python scripts/backup_database.py --dry-run\n  python scripts/backup_database.py\n  python scripts/backup_database.py --confirm-production\n  python scripts/backup_database.py --schema-only\n  python scripts/backup_database.py --data-only\n  python scripts/backup_database.py --output-dir /custom/path\n\nExit codes:\n    0  — backup written + manifest valid (or --dry-run succeeded)\n    2  — bad CLI arguments\n    3  — DB URL missing\n    4  — production refused without --confirm-production\n    5  — pg_dump missing or failed\n")
               STORE_NAME               0 (__doc__)

  33           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  35           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  36           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (datetime)
               STORE_NAME               5 (_dt)

  37           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (hashlib)
               STORE_NAME               6 (hashlib)

  38           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (json)
               STORE_NAME               7 (json)

  39           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              8 (os)
               STORE_NAME               8 (os)

  40           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              9 (shutil)
               STORE_NAME               9 (shutil)

  41           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME             10 (subprocess)
               STORE_NAME              10 (subprocess)

  42           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME             11 (sys)
               STORE_NAME              11 (sys)

  43           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('Path',))
               IMPORT_NAME             12 (pathlib)
               IMPORT_FROM             13 (Path)
               STORE_NAME              13 (Path)
               POP_TOP

  44           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Optional', 'Tuple'))
               IMPORT_NAME             14 (typing)
               IMPORT_FROM             15 (Optional)
               STORE_NAME              15 (Optional)
               IMPORT_FROM             16 (Tuple)
               STORE_NAME              16 (Tuple)
               POP_TOP

  45           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('urlparse',))
               IMPORT_NAME             17 (urllib.parse)
               IMPORT_FROM             18 (urlparse)
               STORE_NAME              18 (urlparse)
               POP_TOP

  50           LOAD_NAME               11 (sys)
               LOAD_ATTR               38 (stdout)
               LOAD_NAME               11 (sys)
               LOAD_ATTR               40 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              21 (_stream)

  51           NOP

  52   L2:     LOAD_NAME               21 (_stream)
               LOAD_ATTR               45 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  50   L4:     END_FOR
               POP_ITER

  61           LOAD_CONST              31 (('prod', 'production', 'live'))
               STORE_NAME              24 (PRODUCTION_HOSTNAME_TOKENS)

  64           LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA34B0, file "scripts\backup_database.py", line 64>)
               MAKE_FUNCTION
               LOAD_CONST               9 (<code object resolve_db_url at 0x0000018C17FF10B0, file "scripts\backup_database.py", line 64>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              25 (resolve_db_url)

  78           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts\backup_database.py", line 78>)
               MAKE_FUNCTION
               LOAD_CONST              11 (<code object mask_db_url at 0x0000018C17F79E80, file "scripts\backup_database.py", line 78>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              26 (mask_db_url)

 111           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts\backup_database.py", line 111>)
               MAKE_FUNCTION
               LOAD_CONST              13 (<code object is_production_url at 0x0000018C179A7290, file "scripts\backup_database.py", line 111>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              27 (is_production_url)

 126           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts\backup_database.py", line 126>)
               MAKE_FUNCTION
               LOAD_CONST              15 (<code object sha256_of_file at 0x0000018C17FED830, file "scripts\backup_database.py", line 126>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (sha256_of_file)

 138           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA2C40, file "scripts\backup_database.py", line 138>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object detect_pg_dump_version at 0x0000018C17FEDC30, file "scripts\backup_database.py", line 138>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              29 (detect_pg_dump_version)

 153           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts\backup_database.py", line 153>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object now_stamp at 0x0000018C17972D90, file "scripts\backup_database.py", line 153>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              30 (now_stamp)

 157           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FBFEE0, file "scripts\backup_database.py", line 157>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object build_manifest at 0x0000018C180E8030, file "scripts\backup_database.py", line 157>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (build_manifest)

 193           LOAD_CONST              32 (('',))
               LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18026130, file "scripts\backup_database.py", line 193>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _print_status at 0x0000018C18039070, file "scripts\backup_database.py", line 193>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              32 (_print_status)

 201           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C18026530, file "scripts\backup_database.py", line 201>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object _build_pg_dump_cmd at 0x0000018C17FF0C30, file "scripts\backup_database.py", line 201>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              33 (_build_pg_dump_cmd)

 215           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA3690, file "scripts\backup_database.py", line 215>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object _resolve_output_dir at 0x0000018C17972550, file "scripts\backup_database.py", line 215>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_resolve_output_dir)

 220           LOAD_CONST              33 ((None,))
               LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3870, file "scripts\backup_database.py", line 220>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object main at 0x0000018C17E57E60, file "scripts\backup_database.py", line 220>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              35 (main)

 376           LOAD_NAME               36 (__name__)
               LOAD_CONST              30 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       14 (to L5)
               NOT_TAKEN

 377           LOAD_NAME               37 (SystemExit)
               PUSH_NULL
               LOAD_NAME               35 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               RAISE_VARARGS            1

 376   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  53           LOAD_NAME               23 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

  54   L7:     POP_EXCEPT
               JUMP_BACKWARD          130 (to L1)

  53   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "scripts\backup_database.py", line 64>:
 64           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Optional[str]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object resolve_db_url at 0x0000018C17FF10B0, file "scripts\backup_database.py", line 64>:
 64           RESUME                   0

 75           LOAD_GLOBAL              0 (os)
              LOAD_ATTR                2 (environ)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('SUPABASE_DB_URL')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE        42 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_GLOBAL              0 (os)
              LOAD_ATTR                2 (environ)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('DATABASE_URL')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               3 (None)
      L1:     RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts\backup_database.py", line 78>:
 78           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('url')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object mask_db_url at 0x0000018C17F79E80, file "scripts\backup_database.py", line 78>:
  78            RESUME                   0

  87            LOAD_FAST_BORROW         0 (url)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

  88            LOAD_CONST               1 ('')
                RETURN_VALUE

  89    L1:     NOP

  90    L2:     LOAD_GLOBAL              1 (urlparse + NULL)
                LOAD_FAST_BORROW         0 (url)
                CALL                     1
                STORE_FAST               1 (parsed)

  91            LOAD_FAST_BORROW         1 (parsed)
                LOAD_ATTR                2 (scheme)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
        L3:     NOT_TAKEN
        L4:     POP_TOP
                LOAD_CONST               2 ('postgresql')
        L5:     STORE_FAST               2 (scheme)

  92            LOAD_FAST_BORROW         1 (parsed)
                LOAD_ATTR                4 (username)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                LOAD_CONST               3 ('postgres')
        L8:     STORE_FAST               3 (username)

  93            LOAD_FAST_BORROW         1 (parsed)
                LOAD_ATTR                6 (hostname)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                LOAD_CONST               4 ('?')
       L11:     STORE_FAST               4 (host)

  94            LOAD_FAST_BORROW         1 (parsed)
                LOAD_ATTR                8 (port)
                TO_BOOL
                POP_JUMP_IF_FALSE       16 (to L14)
       L12:     NOT_TAKEN
       L13:     LOAD_CONST               5 (':')
                LOAD_FAST_BORROW         1 (parsed)
                LOAD_ATTR                8 (port)
                FORMAT_SIMPLE
                BUILD_STRING             2
                JUMP_FORWARD             1 (to L15)
       L14:     LOAD_CONST               1 ('')
       L15:     STORE_FAST               5 (port)

  95            LOAD_FAST_BORROW         1 (parsed)
                LOAD_ATTR               10 (path)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
       L16:     NOT_TAKEN
       L17:     POP_TOP
                LOAD_CONST               1 ('')
       L18:     STORE_FAST               6 (path)

  98            LOAD_CONST               6 ('.')
                LOAD_FAST_BORROW         4 (host)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       76 (to L21)
                NOT_TAKEN

  99            LOAD_FAST_BORROW         4 (host)
                LOAD_ATTR               13 (partition + NULL|self)
                LOAD_CONST               6 ('.')
                CALL                     1
                UNPACK_SEQUENCE          3
                STORE_FAST_STORE_FAST  120 (head, _)
                STORE_FAST               9 (tail)

 100            LOAD_CONST               6 ('.')
                LOAD_FAST_BORROW         9 (tail)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       21 (to L19)
                NOT_TAKEN
                LOAD_FAST_BORROW         9 (tail)
                LOAD_ATTR               15 (split + NULL|self)
                LOAD_CONST               6 ('.')
                CALL                     1
                LOAD_CONST              13 (-2)
                LOAD_CONST               7 (None)
                BINARY_SLICE
                JUMP_FORWARD             2 (to L20)
       L19:     LOAD_FAST_BORROW         9 (tail)
                BUILD_LIST               1
       L20:     STORE_FAST              10 (tail_top)

 101            LOAD_CONST               8 ('***.')
                LOAD_CONST               6 ('.')
                LOAD_ATTR               17 (join + NULL|self)
                LOAD_FAST_BORROW        10 (tail_top)
                CALL                     1
                BINARY_OP                0 (+)
                STORE_FAST              11 (masked_host)
                JUMP_FORWARD             2 (to L22)

 103   L21:     LOAD_CONST               9 ('***')
                STORE_FAST              11 (masked_host)

 105   L22:     LOAD_FAST_BORROW         2 (scheme)
                FORMAT_SIMPLE
                LOAD_CONST              10 ('://')
                LOAD_FAST_BORROW         3 (username)
                FORMAT_SIMPLE
                LOAD_CONST              11 (':***@')
                LOAD_FAST_BORROW        11 (masked_host)
                FORMAT_SIMPLE
                LOAD_FAST_BORROW         5 (port)
                FORMAT_SIMPLE
                LOAD_FAST_BORROW         6 (path)
                FORMAT_SIMPLE
                BUILD_STRING             7
       L23:     RETURN_VALUE

  --   L24:     PUSH_EXC_INFO

 106            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L26)
                NOT_TAKEN
                POP_TOP

 108   L25:     POP_EXCEPT
                LOAD_CONST              12 ('<masked>')
                RETURN_VALUE

 106   L26:     RERAISE                  0

  --   L27:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L24 [0]
  L4 to L6 -> L24 [0]
  L7 to L9 -> L24 [0]
  L10 to L12 -> L24 [0]
  L13 to L16 -> L24 [0]
  L17 to L23 -> L24 [0]
  L24 to L25 -> L27 [1] lasti
  L26 to L27 -> L27 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts\backup_database.py", line 111>:
111           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('url')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object is_production_url at 0x0000018C179A7290, file "scripts\backup_database.py", line 111>:
  --            MAKE_CELL                1 (host)

 111            RESUME                   0

 117            LOAD_FAST_BORROW         0 (url)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 118            LOAD_CONST               1 (False)
                RETURN_VALUE

 119    L1:     NOP

 120    L2:     LOAD_GLOBAL              1 (urlparse + NULL)
                LOAD_FAST_BORROW         0 (url)
                CALL                     1
                LOAD_ATTR                2 (hostname)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
        L3:     NOT_TAKEN
        L4:     POP_TOP
                LOAD_CONST               2 ('')
        L5:     LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              1 (host)

 123    L6:     LOAD_GLOBAL              8 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       35 (to L10)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST                1 (host)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025730, file "scripts\backup_database.py", line 123>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_GLOBAL             10 (PRODUCTION_HOSTNAME_TOKENS)
                GET_ITER
                CALL                     0
        L7:     FOR_ITER                12 (to L9)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L7)
        L8:     POP_ITER
                LOAD_CONST               4 (True)
                RETURN_VALUE
        L9:     END_FOR
                POP_ITER
                LOAD_CONST               1 (False)
                RETURN_VALUE
       L10:     PUSH_NULL
                LOAD_FAST                1 (host)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025730, file "scripts\backup_database.py", line 123>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_GLOBAL             10 (PRODUCTION_HOSTNAME_TOKENS)
                GET_ITER
                CALL                     0
                CALL                     1
                RETURN_VALUE

  --   L11:     PUSH_EXC_INFO

 121            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L13)
                NOT_TAKEN
                POP_TOP

 122   L12:     POP_EXCEPT
                LOAD_CONST               1 (False)
                RETURN_VALUE

 121   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L11 [0]
  L4 to L6 -> L11 [0]
  L11 to L12 -> L14 [1] lasti
  L13 to L14 -> L14 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C18025730, file "scripts\backup_database.py", line 123>:
  --           COPY_FREE_VARS           1

 123           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (tok, tok)
               LOAD_DEREF               2 (host)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           11 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts\backup_database.py", line 126>:
126           RESUME                   0
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

Disassembly of <code object sha256_of_file at 0x0000018C17FED830, file "scripts\backup_database.py", line 126>:
  --            MAKE_CELL                3 (f)

 126            RESUME                   0

 128            NOP

 129    L1:     LOAD_GLOBAL              0 (hashlib)
                LOAD_ATTR                2 (sha256)
                PUSH_NULL
                CALL                     0
                STORE_FAST               1 (h)

 130            LOAD_GLOBAL              5 (open + NULL)
                LOAD_FAST_BORROW         0 (path)
                LOAD_CONST               1 ('rb')
                CALL                     2
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L2:     STORE_DEREF              3 (f)

 131            LOAD_GLOBAL              7 (iter + NULL)
                LOAD_FAST_BORROW         3 (f)
                BUILD_TUPLE              1
                LOAD_CONST               2 (<code object <lambda> at 0x0000018C18024930, file "scripts\backup_database.py", line 131>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_CONST               3 (b'')
                CALL                     2
                GET_ITER
        L3:     FOR_ITER                20 (to L4)
                STORE_FAST               2 (chunk)

 132            LOAD_FAST_BORROW         1 (h)
                LOAD_ATTR                9 (update + NULL|self)
                LOAD_FAST_BORROW         2 (chunk)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           22 (to L3)

 131    L4:     END_FOR
                POP_ITER

 130    L5:     LOAD_CONST               4 (None)
                LOAD_CONST               4 (None)
                LOAD_CONST               4 (None)
                CALL                     3
                POP_TOP

 133    L6:     LOAD_FAST_BORROW         1 (h)
                LOAD_ATTR               11 (hexdigest + NULL|self)
                CALL                     0
        L7:     RETURN_VALUE

 130    L8:     PUSH_EXC_INFO
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

 134            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L14)
                NOT_TAKEN
                POP_TOP

 135   L13:     POP_EXCEPT
                LOAD_CONST               5 ('')
                RETURN_VALUE

 134   L14:     RERAISE                  0

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

Disassembly of <code object <lambda> at 0x0000018C18024930, file "scripts\backup_database.py", line 131>:
  --           COPY_FREE_VARS           1

 131           RESUME                   0
               LOAD_DEREF               0 (f)
               LOAD_ATTR                1 (read + NULL|self)
               LOAD_CONST               1 (1048576)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "scripts\backup_database.py", line 138>:
138           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Optional[str]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object detect_pg_dump_version at 0x0000018C17FEDC30, file "scripts\backup_database.py", line 138>:
 138            RESUME                   0

 140            LOAD_GLOBAL              0 (shutil)
                LOAD_ATTR                2 (which)
                PUSH_NULL
                LOAD_CONST               1 ('pg_dump')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 141            LOAD_CONST               2 (None)
                RETURN_VALUE

 142    L1:     NOP

 143    L2:     LOAD_GLOBAL              4 (subprocess)
                LOAD_ATTR                6 (run)
                PUSH_NULL

 144            LOAD_CONST               1 ('pg_dump')
                LOAD_CONST               3 ('--version')
                BUILD_LIST               2

 145            LOAD_CONST               4 (True)
                LOAD_CONST               4 (True)
                LOAD_CONST               5 (False)
                LOAD_SMALL_INT          10

 143            LOAD_CONST               6 (('capture_output', 'text', 'check', 'timeout'))
                CALL_KW                  5
                STORE_FAST               0 (out)

 147            LOAD_FAST_BORROW         0 (out)
                LOAD_ATTR                8 (stdout)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
        L3:     NOT_TAKEN
        L4:     POP_TOP
                LOAD_CONST               7 ('')
        L5:     LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               13 (splitlines + NULL|self)
                CALL                     0
                STORE_FAST               1 (first)

 148            LOAD_FAST_BORROW         1 (first)
                TO_BOOL
                POP_JUMP_IF_FALSE       10 (to L9)
        L6:     NOT_TAKEN
        L7:     LOAD_FAST_BORROW         1 (first)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
        L8:     RETURN_VALUE
        L9:     LOAD_CONST               2 (None)
       L10:     RETURN_VALUE

  --   L11:     PUSH_EXC_INFO

 149            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L13)
                NOT_TAKEN
                POP_TOP

 150   L12:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 149   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L11 [0]
  L4 to L6 -> L11 [0]
  L7 to L8 -> L11 [0]
  L9 to L10 -> L11 [0]
  L11 to L12 -> L14 [1] lasti
  L13 to L14 -> L14 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts\backup_database.py", line 153>:
153           RESUME                   0
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

Disassembly of <code object now_stamp at 0x0000018C17972D90, file "scripts\backup_database.py", line 153>:
153           RESUME                   0

154           LOAD_GLOBAL              0 (_dt)
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

Disassembly of <code object __annotate__ at 0x0000018C17FBFEE0, file "scripts\backup_database.py", line 157>:
157           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('timestamp')

159           LOAD_CONST               2 ('str')

157           LOAD_CONST               3 ('db_url')

160           LOAD_CONST               2 ('str')

157           LOAD_CONST               4 ('mode')

161           LOAD_CONST               2 ('str')

157           LOAD_CONST               5 ('schema_only')

162           LOAD_CONST               6 ('bool')

157           LOAD_CONST               7 ('data_only')

163           LOAD_CONST               6 ('bool')

157           LOAD_CONST               8 ('dump_path')

164           LOAD_CONST               9 ('Path')

157           LOAD_CONST              10 ('dump_size_bytes')

165           LOAD_CONST              11 ('int')

157           LOAD_CONST              12 ('sha256')

166           LOAD_CONST               2 ('str')

157           LOAD_CONST              13 ('pg_dump_version')

167           LOAD_CONST              14 ('Optional[str]')

157           LOAD_CONST              15 ('return')

168           LOAD_CONST              16 ('dict')

157           BUILD_MAP               10
              RETURN_VALUE

Disassembly of <code object build_manifest at 0x0000018C180E8030, file "scripts\backup_database.py", line 157>:
 157            RESUME                   0

 170            LOAD_CONST               1 ('')
                STORE_FAST               9 (parsed_host)

 171            NOP

 172    L1:     LOAD_GLOBAL              1 (urlparse + NULL)
                LOAD_FAST_BORROW         1 (db_url)
                CALL                     1
                LOAD_ATTR                2 (hostname)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
        L2:     NOT_TAKEN
        L3:     POP_TOP
                LOAD_CONST               1 ('')
        L4:     STORE_FAST               9 (parsed_host)

 176    L5:     LOAD_CONST               2 ('timestamp')
                LOAD_FAST                0 (timestamp)

 177            LOAD_CONST               3 ('hostname')
                LOAD_FAST                9 (parsed_host)

 178            LOAD_CONST               4 ('mode')
                LOAD_FAST                2 (mode)

 179            LOAD_CONST               5 ('schema_only')
                LOAD_GLOBAL              7 (bool + NULL)
                LOAD_FAST_BORROW         3 (schema_only)
                CALL                     1

 180            LOAD_CONST               6 ('data_only')
                LOAD_GLOBAL              7 (bool + NULL)
                LOAD_FAST_BORROW         4 (data_only)
                CALL                     1

 181            LOAD_CONST               7 ('dump_file')
                LOAD_FAST_BORROW         5 (dump_path)
                LOAD_ATTR                8 (name)

 182            LOAD_CONST               8 ('dump_size_bytes')
                LOAD_GLOBAL             11 (int + NULL)
                LOAD_FAST                6 (dump_size_bytes)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
        L6:     CALL                     1

 183            LOAD_CONST               9 ('sha256')
                LOAD_FAST                7 (sha256)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               1 ('')

 184    L7:     LOAD_CONST              10 ('pg_dump_version')
                LOAD_FAST_BORROW         8 (pg_dump_version)

 185            LOAD_CONST              11 ('tool')
                LOAD_CONST              12 ('pas143d.backup_database')

 175            BUILD_MAP               10
                RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

 173            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        4 (to L10)
                NOT_TAKEN
                POP_TOP

 174    L9:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 92 (to L5)

 173   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L8 [0]
  L3 to L5 -> L8 [0]
  L8 to L9 -> L11 [1] lasti
  L10 to L11 -> L11 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026130, file "scripts\backup_database.py", line 193>:
193           RESUME                   0
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

Disassembly of <code object _print_status at 0x0000018C18039070, file "scripts\backup_database.py", line 193>:
193           RESUME                   0

194           LOAD_FAST_BORROW         1 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_CONST               0 ('PASS')
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               1 ('FAIL')
      L2:     STORE_FAST               3 (tag)

195           LOAD_CONST               2 ('[')
              LOAD_FAST_BORROW         3 (tag)
              FORMAT_SIMPLE
              LOAD_CONST               3 ('] ')
              LOAD_FAST_BORROW         0 (label)
              FORMAT_SIMPLE
              BUILD_STRING             4
              STORE_FAST               4 (line)

196           LOAD_FAST_BORROW         2 (detail)
              TO_BOOL
              POP_JUMP_IF_FALSE       13 (to L3)
              NOT_TAKEN

197           LOAD_FAST_BORROW         4 (line)
              LOAD_CONST               4 (' — ')
              LOAD_FAST_BORROW         2 (detail)
              FORMAT_SIMPLE
              BUILD_STRING             2
              BINARY_OP               13 (+=)
              STORE_FAST               4 (line)

198   L3:     LOAD_GLOBAL              1 (print + NULL)
              LOAD_FAST_BORROW         4 (line)
              CALL                     1
              POP_TOP
              LOAD_CONST               5 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026530, file "scripts\backup_database.py", line 201>:
201           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('db_url')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('dump_path')
              LOAD_CONST               4 ('Path')
              LOAD_CONST               5 ('schema_only')
              LOAD_CONST               6 ('bool')
              LOAD_CONST               7 ('data_only')
              LOAD_CONST               6 ('bool')
              LOAD_CONST               8 ('return')
              LOAD_CONST               9 ('list')
              BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _build_pg_dump_cmd at 0x0000018C17FF0C30, file "scripts\backup_database.py", line 201>:
201           RESUME                   0

206           LOAD_CONST               1 ('pg_dump')
              LOAD_CONST               2 ('-F')
              LOAD_CONST               3 ('c')
              LOAD_CONST               4 ('-w')
              LOAD_CONST               5 ('-f')
              LOAD_GLOBAL              1 (str + NULL)
              LOAD_FAST_BORROW         1 (dump_path)
              CALL                     1
              BUILD_LIST               6
              STORE_FAST               4 (cmd)

207           LOAD_FAST_BORROW         2 (schema_only)
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L1)
              NOT_TAKEN

208           LOAD_FAST_BORROW         4 (cmd)
              LOAD_ATTR                3 (append + NULL|self)
              LOAD_CONST               6 ('--schema-only')
              CALL                     1
              POP_TOP

209   L1:     LOAD_FAST_BORROW         3 (data_only)
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L2)
              NOT_TAKEN

210           LOAD_FAST_BORROW         4 (cmd)
              LOAD_ATTR                3 (append + NULL|self)
              LOAD_CONST               7 ('--data-only')
              CALL                     1
              POP_TOP

211   L2:     LOAD_FAST_BORROW         4 (cmd)
              LOAD_ATTR                3 (append + NULL|self)
              LOAD_FAST_BORROW         0 (db_url)
              CALL                     1
              POP_TOP

212           LOAD_FAST_BORROW         4 (cmd)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "scripts\backup_database.py", line 215>:
215           RESUME                   0
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

Disassembly of <code object _resolve_output_dir at 0x0000018C17972550, file "scripts\backup_database.py", line 215>:
215           RESUME                   0

216           LOAD_FAST_BORROW         0 (arg_value)
              TO_BOOL
              POP_JUMP_IF_FALSE       12 (to L1)
              NOT_TAKEN
              LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (arg_value)
              CALL                     1
              JUMP_FORWARD            27 (to L2)
      L1:     LOAD_GLOBAL              0 (Path)
              LOAD_ATTR                2 (cwd)
              PUSH_NULL
              CALL                     0
              LOAD_CONST               0 ('backups')
              BINARY_OP               11 (/)
      L2:     STORE_FAST               1 (base)

217           LOAD_FAST_BORROW         1 (base)
              LOAD_GLOBAL              5 (now_stamp + NULL)
              CALL                     0
              BINARY_OP               11 (/)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "scripts\backup_database.py", line 220>:
220           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17E57E60, file "scripts\backup_database.py", line 220>:
 220            RESUME                   0

 221            LOAD_GLOBAL              0 (argparse)
                LOAD_ATTR                2 (ArgumentParser)
                PUSH_NULL

 222            LOAD_CONST               0 ('backup_database')

 223            LOAD_CONST               1 ('PAS143D — operator-initiated PostgreSQL backup wrapper.')

 221            LOAD_CONST               2 (('prog', 'description'))
                CALL_KW                  2
                STORE_FAST               1 (parser)

 225            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 226            LOAD_CONST               3 ('--dry-run')
                LOAD_CONST               4 ('store_true')

 227            LOAD_CONST               5 ('Print what would happen without invoking pg_dump.')

 225            LOAD_CONST               6 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 229            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 230            LOAD_CONST               7 ('--confirm-production')
                LOAD_CONST               4 ('store_true')

 231            LOAD_CONST               8 ('REQUIRED to run against a production-looking host.')

 229            LOAD_CONST               6 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 233            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 234            LOAD_CONST               9 ('--output-dir')
                LOAD_CONST              10 (None)

 235            LOAD_CONST              11 ('Override the default ./backups/ root.')

 233            LOAD_CONST              12 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 237            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 238            LOAD_CONST              13 ('--schema-only')
                LOAD_CONST               4 ('store_true')

 239            LOAD_CONST              14 ('Dump schema only (no row data).')

 237            LOAD_CONST               6 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 241            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 242            LOAD_CONST              15 ('--data-only')
                LOAD_CONST               4 ('store_true')

 243            LOAD_CONST              16 ('Dump data only (no schema definitions).')

 241            LOAD_CONST               6 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 245            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                7 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 247            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR                8 (schema_only)
                TO_BOOL
                POP_JUMP_IF_FALSE       48 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               10 (data_only)
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L1)
                NOT_TAKEN

 248            LOAD_GLOBAL             13 (print + NULL)
                LOAD_CONST              17 ('--schema-only and --data-only are mutually exclusive.')
                LOAD_GLOBAL             14 (sys)
                LOAD_ATTR               16 (stderr)
                LOAD_CONST              18 (('file',))
                CALL_KW                  2
                POP_TOP

 249            LOAD_SMALL_INT           2
                RETURN_VALUE

 252    L1:     LOAD_GLOBAL             19 (resolve_db_url + NULL)
                CALL                     0
                STORE_FAST               3 (db_url)

 253            LOAD_FAST_BORROW         3 (db_url)
                TO_BOOL
                POP_JUMP_IF_TRUE        17 (to L2)
                NOT_TAKEN

 254            LOAD_GLOBAL             21 (_print_status + NULL)

 255            LOAD_CONST              19 ('DB URL resolution')

 256            LOAD_CONST              20 (False)

 257            LOAD_CONST              21 ('Set SUPABASE_DB_URL or DATABASE_URL before running.')

 254            LOAD_CONST              22 (('ok', 'detail'))
                CALL_KW                  3
                POP_TOP

 259            LOAD_SMALL_INT           3
                RETURN_VALUE

 261    L2:     LOAD_GLOBAL             23 (mask_db_url + NULL)
                LOAD_FAST_BORROW         3 (db_url)
                CALL                     1
                STORE_FAST               4 (masked)

 262            LOAD_GLOBAL             21 (_print_status + NULL)
                LOAD_CONST              23 ('DB URL resolved')
                LOAD_CONST              24 (True)
                LOAD_FAST_BORROW         4 (masked)
                LOAD_CONST              22 (('ok', 'detail'))
                CALL_KW                  3
                POP_TOP

 265            LOAD_GLOBAL             25 (is_production_url + NULL)
                LOAD_FAST_BORROW         3 (db_url)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               26 (confirm_production)
                TO_BOOL
                POP_JUMP_IF_TRUE        17 (to L3)
                NOT_TAKEN

 266            LOAD_GLOBAL             21 (_print_status + NULL)

 267            LOAD_CONST              25 ('Production safety')

 268            LOAD_CONST              20 (False)

 269            LOAD_CONST              26 ('Host looks like production. Re-run with --confirm-production.')

 266            LOAD_CONST              22 (('ok', 'detail'))
                CALL_KW                  3
                POP_TOP

 271            LOAD_SMALL_INT           4
                RETURN_VALUE

 272    L3:     LOAD_GLOBAL             21 (_print_status + NULL)

 273            LOAD_CONST              25 ('Production safety')

 274            LOAD_CONST              24 (True)

 275            LOAD_GLOBAL             25 (is_production_url + NULL)
                LOAD_FAST_BORROW         3 (db_url)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_CONST              27 ('confirmed')
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST              28 ('non-production host')

 272    L5:     LOAD_CONST              22 (('ok', 'detail'))
                CALL_KW                  3
                POP_TOP

 279            LOAD_GLOBAL             29 (_resolve_output_dir + NULL)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               30 (output_dir)
                CALL                     1
                STORE_FAST               5 (out_dir)

 280            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               32 (dry_run)
                TO_BOOL
                POP_JUMP_IF_TRUE        20 (to L6)
                NOT_TAKEN

 281            LOAD_FAST_BORROW         5 (out_dir)
                LOAD_ATTR               35 (mkdir + NULL|self)
                LOAD_CONST              24 (True)
                LOAD_CONST              24 (True)
                LOAD_CONST              29 (('parents', 'exist_ok'))
                CALL_KW                  2
                POP_TOP

 282    L6:     LOAD_GLOBAL             21 (_print_status + NULL)
                LOAD_CONST              30 ('Output directory')
                LOAD_CONST              24 (True)
                LOAD_GLOBAL             37 (str + NULL)
                LOAD_FAST_BORROW         5 (out_dir)
                CALL                     1
                LOAD_CONST              22 (('ok', 'detail'))
                CALL_KW                  3
                POP_TOP

 284            LOAD_GLOBAL             39 (now_stamp + NULL)
                CALL                     0
                STORE_FAST               6 (timestamp)

 285            LOAD_FAST_BORROW         5 (out_dir)
                LOAD_CONST              31 ('pas_')
                LOAD_FAST_BORROW         6 (timestamp)
                FORMAT_SIMPLE
                LOAD_CONST              32 ('.dump')
                BUILD_STRING             3
                BINARY_OP               11 (/)
                STORE_FAST               7 (dump_path)

 287            LOAD_GLOBAL             41 (detect_pg_dump_version + NULL)
                CALL                     0
                STORE_FAST               8 (pg_dump_version)

 288            LOAD_GLOBAL             21 (_print_status + NULL)

 289            LOAD_CONST              33 ('pg_dump availability')

 290            LOAD_FAST_BORROW         8 (pg_dump_version)
                LOAD_CONST              10 (None)
                IS_OP                    1 (is not)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        13 (to L7)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               32 (dry_run)

 291    L7:     LOAD_FAST                8 (pg_dump_version)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              34 ('not installed')

 288    L8:     LOAD_CONST              22 (('ok', 'detail'))
                CALL_KW                  3
                POP_TOP

 295            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               32 (dry_run)
                TO_BOOL
                POP_JUMP_IF_FALSE       89 (to L9)
                NOT_TAKEN

 296            LOAD_GLOBAL             43 (build_manifest + NULL)

 297            LOAD_FAST_BORROW         6 (timestamp)

 298            LOAD_FAST_BORROW         3 (db_url)

 299            LOAD_CONST              35 ('dry-run')

 300            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR                8 (schema_only)

 301            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               10 (data_only)

 302            LOAD_FAST_BORROW         7 (dump_path)

 303            LOAD_SMALL_INT           0

 304            LOAD_CONST              36 ('')

 305            LOAD_FAST_BORROW         8 (pg_dump_version)

 296            LOAD_CONST              37 (('timestamp', 'db_url', 'mode', 'schema_only', 'data_only', 'dump_path', 'dump_size_bytes', 'sha256', 'pg_dump_version'))
                CALL_KW                  9
                STORE_FAST               9 (manifest)

 307            LOAD_GLOBAL             21 (_print_status + NULL)
                LOAD_CONST              38 ('Dry-run manifest preview')
                LOAD_CONST              24 (True)
                LOAD_CONST              39 (('ok',))
                CALL_KW                  2
                POP_TOP

 308            LOAD_GLOBAL             13 (print + NULL)
                LOAD_GLOBAL             44 (json)
                LOAD_ATTR               46 (dumps)
                PUSH_NULL
                LOAD_FAST_BORROW         9 (manifest)
                LOAD_SMALL_INT           2
                LOAD_CONST              40 (('indent',))
                CALL_KW                  2
                CALL                     1
                POP_TOP

 309            LOAD_SMALL_INT           0
                RETURN_VALUE

 312    L9:     LOAD_FAST_BORROW         8 (pg_dump_version)
                POP_JUMP_IF_NOT_NONE    17 (to L10)
                NOT_TAKEN

 313            LOAD_GLOBAL             21 (_print_status + NULL)

 314            LOAD_CONST              41 ('pg_dump missing')

 315            LOAD_CONST              20 (False)

 316            LOAD_CONST              42 ('Install postgresql-client or use --dry-run.')

 313            LOAD_CONST              22 (('ok', 'detail'))
                CALL_KW                  3
                POP_TOP

 318            LOAD_SMALL_INT           5
                RETURN_VALUE

 321   L10:     LOAD_GLOBAL             49 (_build_pg_dump_cmd + NULL)

 322            LOAD_FAST_BORROW_LOAD_FAST_BORROW 55 (db_url, dump_path)

 323            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR                8 (schema_only)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               10 (data_only)

 321            LOAD_CONST              43 (('schema_only', 'data_only'))
                CALL_KW                  4
                STORE_FAST              10 (cmd)

 326            LOAD_FAST_BORROW        10 (cmd)
                LOAD_ATTR               51 (copy + NULL|self)
                CALL                     0
                STORE_FAST              11 (redacted)

 327            LOAD_FAST_BORROW_LOAD_FAST_BORROW 75 (masked, redacted)
                LOAD_CONST              62 (-1)
                STORE_SUBSCR

 328            LOAD_GLOBAL             13 (print + NULL)
                LOAD_CONST              44 ('  $ ')
                LOAD_CONST              45 (' ')
                LOAD_ATTR               53 (join + NULL|self)
                LOAD_FAST_BORROW        11 (redacted)
                CALL                     1
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 330            NOP

 331   L11:     LOAD_GLOBAL             54 (subprocess)
                LOAD_ATTR               56 (run)
                PUSH_NULL
                LOAD_FAST_BORROW        10 (cmd)
                LOAD_CONST              24 (True)
                LOAD_CONST              24 (True)
                LOAD_CONST              20 (False)
                LOAD_CONST              46 (('capture_output', 'text', 'check'))
                CALL_KW                  4
                STORE_FAST              12 (result)

 336   L12:     LOAD_FAST               12 (result)
                LOAD_ATTR               64 (returncode)
                LOAD_SMALL_INT           0
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE      154 (to L19)
                NOT_TAKEN

 340            LOAD_FAST               12 (result)
                LOAD_ATTR               16 (stderr)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              36 ('')
       L13:     LOAD_CONST              48 (slice(None, 600, None))
                BINARY_OP               26 ([])
                STORE_FAST              14 (err)

 342            LOAD_FAST                3 (db_url)
                BUILD_TUPLE              1
                GET_ITER
       L14:     FOR_ITER                39 (to L17)
                STORE_FAST              15 (needle)

 343            LOAD_FAST               15 (needle)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN
                JUMP_BACKWARD           13 (to L14)
       L15:     LOAD_FAST_LOAD_FAST    254 (needle, err)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                JUMP_BACKWARD           21 (to L14)

 344   L16:     LOAD_FAST               14 (err)
                LOAD_ATTR               67 (replace + NULL|self)
                LOAD_FAST               15 (needle)
                LOAD_CONST              49 ('<DB_URL_REDACTED>')
                CALL                     2
                STORE_FAST              14 (err)
                JUMP_BACKWARD           41 (to L14)

 342   L17:     END_FOR
                POP_ITER

 345            LOAD_GLOBAL             21 (_print_status + NULL)
                LOAD_CONST              50 ('pg_dump exit')
                LOAD_CONST              20 (False)
                LOAD_CONST              51 ('rc=')
                LOAD_FAST               12 (result)
                LOAD_ATTR               64 (returncode)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_CONST              22 (('ok', 'detail'))
                CALL_KW                  3
                POP_TOP

 346            LOAD_FAST               14 (err)
                LOAD_ATTR               69 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       28 (to L18)
                NOT_TAKEN

 347            LOAD_GLOBAL             13 (print + NULL)
                LOAD_FAST               14 (err)
                LOAD_GLOBAL             14 (sys)
                LOAD_ATTR               16 (stderr)
                LOAD_CONST              18 (('file',))
                CALL_KW                  2
                POP_TOP

 348   L18:     LOAD_SMALL_INT           5
                RETURN_VALUE

 351   L19:     LOAD_FAST                7 (dump_path)
                LOAD_ATTR               71 (exists + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       27 (to L20)
                NOT_TAKEN
                LOAD_FAST                7 (dump_path)
                LOAD_ATTR               73 (stat + NULL|self)
                CALL                     0
                LOAD_ATTR               74 (st_size)
                JUMP_FORWARD             1 (to L21)
       L20:     LOAD_SMALL_INT           0
       L21:     STORE_FAST              16 (size)

 352            LOAD_GLOBAL             77 (sha256_of_file + NULL)
                LOAD_FAST                7 (dump_path)
                CALL                     1
                STORE_FAST              17 (sha)

 353            LOAD_GLOBAL             43 (build_manifest + NULL)

 354            LOAD_FAST                6 (timestamp)

 355            LOAD_FAST                3 (db_url)

 356            LOAD_CONST              52 ('live')

 357            LOAD_FAST                2 (args)
                LOAD_ATTR                8 (schema_only)

 358            LOAD_FAST                2 (args)
                LOAD_ATTR               10 (data_only)

 359            LOAD_FAST                7 (dump_path)

 360            LOAD_FAST               16 (size)

 361            LOAD_FAST               17 (sha)

 362            LOAD_FAST                8 (pg_dump_version)

 353            LOAD_CONST              37 (('timestamp', 'db_url', 'mode', 'schema_only', 'data_only', 'dump_path', 'dump_size_bytes', 'sha256', 'pg_dump_version'))
                CALL_KW                  9
                STORE_FAST               9 (manifest)

 364            LOAD_FAST                5 (out_dir)
                LOAD_CONST              53 ('backup_manifest.json')
                BINARY_OP               11 (/)
                STORE_FAST              18 (manifest_path)

 365            LOAD_FAST               18 (manifest_path)
                LOAD_ATTR               79 (write_text + NULL|self)
                LOAD_GLOBAL             44 (json)
                LOAD_ATTR               46 (dumps)
                PUSH_NULL
                LOAD_FAST                9 (manifest)
                LOAD_SMALL_INT           2
                LOAD_CONST              40 (('indent',))
                CALL_KW                  2
                LOAD_CONST              54 ('utf-8')
                LOAD_CONST              55 (('encoding',))
                CALL_KW                  2
                POP_TOP

 367            LOAD_GLOBAL             21 (_print_status + NULL)

 368            LOAD_CONST              56 ('Backup complete')

 369            LOAD_FAST               16 (size)
                LOAD_SMALL_INT           0
                COMPARE_OP             132 (>)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L22)
                NOT_TAKEN
                POP_TOP
                LOAD_GLOBAL             81 (bool + NULL)
                LOAD_FAST               17 (sha)
                CALL                     1

 370   L22:     LOAD_FAST                7 (dump_path)
                LOAD_ATTR               82 (name)
                FORMAT_SIMPLE
                LOAD_CONST              57 (' (')
                LOAD_FAST               16 (size)
                FORMAT_SIMPLE
                LOAD_CONST              58 (' bytes), sha256=')
                LOAD_FAST               17 (sha)
                LOAD_CONST              59 (slice(None, 12, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST              60 ('…')
                BUILD_STRING             6

 367            LOAD_CONST              22 (('ok', 'detail'))
                CALL_KW                  3
                POP_TOP

 372            LOAD_GLOBAL             13 (print + NULL)
                LOAD_CONST              61 ('  manifest: ')
                LOAD_FAST               18 (manifest_path)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 373            LOAD_SMALL_INT           0
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 332            LOAD_GLOBAL             58 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       45 (to L27)
                NOT_TAKEN
                STORE_FAST              13 (e)

 333   L24:     LOAD_GLOBAL             21 (_print_status + NULL)
                LOAD_CONST              47 ('pg_dump invocation')
                LOAD_CONST              20 (False)
                LOAD_GLOBAL             61 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               62 (__name__)
                LOAD_CONST              22 (('ok', 'detail'))
                CALL_KW                  3
                POP_TOP

 334   L25:     POP_EXCEPT
                LOAD_CONST              10 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                LOAD_SMALL_INT           5
                RETURN_VALUE

  --   L26:     LOAD_CONST              10 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RERAISE                  1

 332   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L11 to L12 -> L23 [0]
  L23 to L24 -> L28 [1] lasti
  L24 to L25 -> L26 [1] lasti
  L26 to L28 -> L28 [1] lasti
```
