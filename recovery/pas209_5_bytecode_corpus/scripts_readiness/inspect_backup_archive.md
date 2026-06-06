# scripts_readiness/inspect_backup_archive

- **pyc:** `scripts\__pycache__\inspect_backup_archive.cpython-314.pyc`
- **expected source path (absent):** `scripts/inspect_backup_archive.py`
- **co_filename (from bytecode):** `scripts\inspect_backup_archive.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS143G — Offline archive inspection.

Reads ONLY the plaintext header of a .pasbak archive. Never decrypts
the payload. Never asks for a passphrase. Designed so an operator
auditing a recovered archive can answer "is this even the right
backup?" without exposing any secret material.

Usage:
  python scripts/inspect_backup_archive.py recovery/recovery_20260509.pasbak
  python scripts/inspect_backup_archive.py path/to/archive.pasbak --json

Exit codes:
    0  — header parsed, output emitted
    1  — archive missing / malformed / not a PASBAK file
    2  — bad CLI arguments
```

## Imports

`Optional`, `Path`, `__future__`, `annotations`, `argparse`, `importlib.util`, `json`, `os`, `pathlib`, `sys`, `typing`, `util`

## Classes

_none_

## Functions / methods

`__annotate__`, `_safe_inspect`, `_summarize_for_human`, `main`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS143G — Offline archive inspection.\n\nReads ONLY the plaintext header of a .pasbak archive. Never decrypts\nthe payload. Never asks for a passphrase. Designed so an operator\nauditing a recovered archive can answer "is this even the right\nbackup?" without exposing any secret material.\n\nUsage:\n  python scripts/inspect_backup_archive.py recovery/recovery_20260509.pasbak\n  python scripts/inspect_backup_archive.py path/to/archive.pasbak --json\n\nExit codes:\n    0  — header parsed, output emitted\n    1  — archive missing / malformed / not a PASBAK file\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'package_backup.py'
- 'package_backup_lib'
- 'path'
- 'Path'
- 'info'
- 'dict'
- 'return'
- 'str'
- 'header'
- 'PAS143G — archive inspection: '
- '  archive_version:   '
- 'version'
- '  (tool expects '
- '  encrypted:         '
- 'encrypted'
- '  total bytes:       '
- '  ciphertext bytes:  '
- 'ciphertext_len'
- '  salt bytes:        '
- 'salt'
- '  nonce bytes:       '
- 'nonce'
- '  mac bytes:         '
- 'mac'
- 'HEADER (plaintext recovery manifest)'
- '  created_at:        '
- 'created_at'
- '  tool_version:      '
- 'tool_version'
- '  file_count:        '
- 'file_count'
- '  plaintext sha256:  '
- 'sha256'
- 'verification_summary'
- '  verification:      present='
- 'present'
- ' all_passed='
- 'all_passed'
- ' checks_run='
- 'checks_run'
- ' checks_failed='
- 'checks_failed'
- 'included_files'
- '  included_files ('
- '; first '
- ' shown):'
- '    - '
- '    ... +'
- ' more'
- '========================================================================'
- '------------------------------------------------------------------------'
- '\nTry to inspect the archive; on failure, return an error dict\nrather than raising. The CLI translates this into an exit code.\n'
- '_error'
- 'archive not found: '
- 'archive_path'
- 'archive_version'
- 'salt_bytes'
- 'nonce_bytes'
- 'mac_bytes'
- 'ciphertext_bytes'
- 'total_bytes'
- 'argv'
- 'Optional[list]'
- 'int'
- 'inspect_backup_archive'
- 'PAS143G — read .pasbak header without decrypting.'
- 'archive'
- 'Path to the .pasbak file.'
- '--json'
- 'store_true'
- 'Emit JSON instead of the human view.'
- '[FAIL] '

## Disassembly

```
   0            RESUME                   0

   1            LOAD_CONST               0 ('\nPAS143G — Offline archive inspection.\n\nReads ONLY the plaintext header of a .pasbak archive. Never decrypts\nthe payload. Never asks for a passphrase. Designed so an operator\nauditing a recovered archive can answer "is this even the right\nbackup?" without exposing any secret material.\n\nUsage:\n  python scripts/inspect_backup_archive.py recovery/recovery_20260509.pasbak\n  python scripts/inspect_backup_archive.py path/to/archive.pasbak --json\n\nExit codes:\n    0  — header parsed, output emitted\n    1  — archive missing / malformed / not a PASBAK file\n    2  — bad CLI arguments\n')
                STORE_NAME               0 (__doc__)

  19            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('annotations',))
                IMPORT_NAME              1 (__future__)
                IMPORT_FROM              2 (annotations)
                STORE_NAME               2 (annotations)
                POP_TOP

  21            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              3 (argparse)
                STORE_NAME               3 (argparse)

  22            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              4 (json)
                STORE_NAME               4 (json)

  23            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              5 (os)
                STORE_NAME               5 (os)

  24            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              6 (sys)
                STORE_NAME               6 (sys)

  25            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('Path',))
                IMPORT_NAME              7 (pathlib)
                IMPORT_FROM              8 (Path)
                STORE_NAME               8 (Path)
                POP_TOP

  26            LOAD_SMALL_INT           0
                LOAD_CONST               4 (('Optional',))
                IMPORT_NAME              9 (typing)
                IMPORT_FROM             10 (Optional)
                STORE_NAME              10 (Optional)
                POP_TOP

  29            LOAD_NAME                6 (sys)
                LOAD_ATTR               22 (stdout)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               24 (stderr)
                BUILD_TUPLE              2
                GET_ITER
        L1:     FOR_ITER                22 (to L4)
                STORE_NAME              13 (_stream)

  30            NOP

  31    L2:     LOAD_NAME               13 (_stream)
                LOAD_ATTR               29 (reconfigure + NULL|self)
                LOAD_CONST               5 ('utf-8')
                LOAD_CONST               6 (('encoding',))
                CALL_KW                  1
                POP_TOP
        L3:     JUMP_BACKWARD           24 (to L1)

  29    L4:     END_FOR
                POP_ITER

  36            LOAD_NAME                5 (os)
                LOAD_ATTR               32 (path)
                LOAD_ATTR               35 (abspath + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               32 (path)
                LOAD_ATTR               37 (join + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               32 (path)
                LOAD_ATTR               39 (dirname + NULL|self)
                LOAD_NAME               20 (__file__)
                CALL                     1
                LOAD_CONST               7 ('..')
                CALL                     2
                CALL                     1
                STORE_NAME              21 (_REPO_ROOT)

  37            LOAD_NAME               21 (_REPO_ROOT)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               32 (path)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       29 (to L5)
                NOT_TAKEN

  38            LOAD_NAME                6 (sys)
                LOAD_ATTR               32 (path)
                LOAD_ATTR               45 (insert + NULL|self)
                LOAD_SMALL_INT           0
                LOAD_NAME               21 (_REPO_ROOT)
                CALL                     2
                POP_TOP

  43    L5:     LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME             23 (importlib.util)
                IMPORT_FROM             24 (util)
                STORE_NAME              25 (_ilu)
                POP_TOP

  44            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('Path',))
                IMPORT_NAME              7 (pathlib)
                IMPORT_FROM              8 (Path)
                STORE_NAME              26 (_Path)
                POP_TOP

  46            LOAD_NAME               26 (_Path)
                PUSH_NULL
                LOAD_NAME               20 (__file__)
                CALL                     1
                LOAD_ATTR               55 (resolve + NULL|self)
                CALL                     0
                LOAD_ATTR               56 (parent)
                LOAD_CONST               8 ('package_backup.py')
                BINARY_OP               11 (/)
                STORE_NAME              29 (_pb_path)

  47            LOAD_NAME               25 (_ilu)
                LOAD_ATTR               60 (spec_from_file_location)
                PUSH_NULL
                LOAD_CONST               9 ('package_backup_lib')
                LOAD_NAME               29 (_pb_path)
                CALL                     2
                STORE_NAME              31 (_spec)

  48            LOAD_NAME               25 (_ilu)
                LOAD_ATTR               64 (module_from_spec)
                PUSH_NULL
                LOAD_NAME               31 (_spec)
                CALL                     1
                STORE_NAME              33 (_pb)

  49            LOAD_NAME               33 (_pb)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               68 (modules)
                LOAD_NAME               31 (_spec)
                LOAD_ATTR               70 (name)
                STORE_SUBSCR

  50            LOAD_NAME               31 (_spec)
                LOAD_ATTR               72 (loader)
                LOAD_ATTR               75 (exec_module + NULL|self)
                LOAD_NAME               33 (_pb)
                CALL                     1
                POP_TOP

  52            LOAD_NAME               33 (_pb)
                LOAD_ATTR               76 (read_archive_header)
                STORE_NAME              38 (read_archive_header)

  53            LOAD_NAME               33 (_pb)
                LOAD_ATTR               78 (ARCHIVE_VERSION)
                STORE_NAME              39 (ARCHIVE_VERSION)

  54            LOAD_NAME               33 (_pb)
                LOAD_ATTR               80 (MAGIC)
                STORE_NAME              40 (MAGIC)

  57            LOAD_CONST              10 (<code object __annotate__ at 0x0000018C18025E30, file "scripts\inspect_backup_archive.py", line 57>)
                MAKE_FUNCTION
                LOAD_CONST              11 (<code object _summarize_for_human at 0x0000018C18353D20, file "scripts\inspect_backup_archive.py", line 57>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              41 (_summarize_for_human)

 102            LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts\inspect_backup_archive.py", line 102>)
                MAKE_FUNCTION
                LOAD_CONST              13 (<code object _safe_inspect at 0x0000018C17EE1CC0, file "scripts\inspect_backup_archive.py", line 102>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              42 (_safe_inspect)

 129            LOAD_CONST              17 ((None,))
                LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts\inspect_backup_archive.py", line 129>)
                MAKE_FUNCTION
                LOAD_CONST              15 (<code object main at 0x0000018C17ED9010, file "scripts\inspect_backup_archive.py", line 129>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              43 (main)

 161            LOAD_NAME               44 (__name__)
                LOAD_CONST              16 ('__main__')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       14 (to L6)
                NOT_TAKEN

 162            LOAD_NAME               45 (SystemExit)
                PUSH_NULL
                LOAD_NAME               43 (main)
                PUSH_NULL
                CALL                     0
                CALL                     1
                RAISE_VARARGS            1

 161    L6:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  32            LOAD_NAME               15 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L9)
                NOT_TAKEN
                POP_TOP

  33    L8:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD          378 (to L1)

  32    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L7 [1]
  L7 to L8 -> L10 [2] lasti
  L9 to L10 -> L10 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "scripts\inspect_backup_archive.py", line 57>:
 57           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('path')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('info')
              LOAD_CONST               4 ('dict')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('str')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _summarize_for_human at 0x0000018C18353D20, file "scripts\inspect_backup_archive.py", line 57>:
 57            RESUME                   0

 58            LOAD_FAST_BORROW         1 (info)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('header')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
       L1:     STORE_FAST               2 (header)

 59            LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                3 (exists + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_FALSE       27 (to L2)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                5 (stat + NULL|self)
               CALL                     0
               LOAD_ATTR                6 (st_size)
               JUMP_FORWARD             1 (to L3)
       L2:     LOAD_SMALL_INT           0
       L3:     STORE_FAST               3 (size)

 61            BUILD_LIST               0
               STORE_FAST               4 (lines)

 62            LOAD_FAST_BORROW         4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              45 ('========================================================================')
               CALL                     1
               POP_TOP

 63            LOAD_FAST_BORROW         4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST               1 ('PAS143G — archive inspection: ')
               LOAD_FAST_BORROW         0 (path)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 64            LOAD_FAST_BORROW         4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              46 ('------------------------------------------------------------------------')
               CALL                     1
               POP_TOP

 65            LOAD_FAST_BORROW         4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST               2 ('  archive_version:   ')
               LOAD_FAST_BORROW         1 (info)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               3 ('version')
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST               4 ('  (tool expects ')

 66            LOAD_GLOBAL             10 (ARCHIVE_VERSION)
               FORMAT_SIMPLE
               LOAD_CONST               5 (')')

 65            BUILD_STRING             5
               CALL                     1
               POP_TOP

 67            LOAD_FAST_BORROW         4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST               6 ('  encrypted:         ')
               LOAD_FAST_BORROW         1 (info)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               7 ('encrypted')
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 68            LOAD_FAST_BORROW         4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST               8 ('  total bytes:       ')
               LOAD_FAST_BORROW         3 (size)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 69            LOAD_FAST_BORROW         4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST               9 ('  ciphertext bytes:  ')
               LOAD_FAST_BORROW         1 (info)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              10 ('ciphertext_len')
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 70            LOAD_FAST                4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              11 ('  salt bytes:        ')
               LOAD_GLOBAL             13 (len + NULL)
               LOAD_FAST_BORROW         1 (info)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              12 ('salt')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              13 (b'')
       L4:     CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 71            LOAD_FAST                4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              14 ('  nonce bytes:       ')
               LOAD_GLOBAL             13 (len + NULL)
               LOAD_FAST_BORROW         1 (info)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              15 ('nonce')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              13 (b'')
       L5:     CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 72            LOAD_FAST                4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              16 ('  mac bytes:         ')
               LOAD_GLOBAL             13 (len + NULL)
               LOAD_FAST_BORROW         1 (info)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              17 ('mac')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              13 (b'')
       L6:     CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 73            LOAD_FAST_BORROW         4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              46 ('------------------------------------------------------------------------')
               CALL                     1
               POP_TOP

 77            LOAD_FAST_BORROW         4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              18 ('HEADER (plaintext recovery manifest)')
               CALL                     1
               POP_TOP

 78            LOAD_FAST_BORROW         4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              19 ('  created_at:        ')
               LOAD_FAST_BORROW         2 (header)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              20 ('created_at')
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 79            LOAD_FAST_BORROW         4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              21 ('  tool_version:      ')
               LOAD_FAST_BORROW         2 (header)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              22 ('tool_version')
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 80            LOAD_FAST_BORROW         4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              23 ('  file_count:        ')
               LOAD_FAST_BORROW         2 (header)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              24 ('file_count')
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 81            LOAD_FAST_BORROW         4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              25 ('  plaintext sha256:  ')
               LOAD_FAST_BORROW         2 (header)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              26 ('sha256')
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 82            LOAD_FAST_BORROW         2 (header)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              27 ('verification_summary')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L7)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
       L7:     STORE_FAST               5 (vsum)

 83            LOAD_FAST_BORROW         4 (lines)
               LOAD_ATTR                9 (append + NULL|self)

 84            LOAD_CONST              28 ('  verification:      present=')

 85            LOAD_FAST_BORROW         5 (vsum)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              29 ('present')
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              30 (' all_passed=')

 86            LOAD_FAST_BORROW         5 (vsum)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              31 ('all_passed')
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              32 (' checks_run=')

 87            LOAD_FAST_BORROW         5 (vsum)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              33 ('checks_run')
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              34 (' checks_failed=')

 88            LOAD_FAST_BORROW         5 (vsum)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              35 ('checks_failed')
               CALL                     1
               FORMAT_SIMPLE

 84            BUILD_STRING             8

 83            CALL                     1
               POP_TOP

 91            LOAD_FAST_BORROW         2 (header)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              36 ('included_files')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L8:     STORE_FAST               6 (files)

 92            LOAD_SMALL_INT          25
               STORE_FAST               7 (cap)

 93            LOAD_FAST_BORROW         4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              37 ('  included_files (')
               LOAD_GLOBAL             13 (len + NULL)
               LOAD_FAST_BORROW         6 (files)
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              38 ('; first ')
               LOAD_GLOBAL             15 (min + NULL)
               LOAD_FAST_BORROW         7 (cap)
               LOAD_GLOBAL             13 (len + NULL)
               LOAD_FAST_BORROW         6 (files)
               CALL                     1
               CALL                     2
               FORMAT_SIMPLE
               LOAD_CONST              39 (' shown):')
               BUILD_STRING             5
               CALL                     1
               POP_TOP

 94            LOAD_FAST_BORROW         6 (files)
               LOAD_CONST              40 (None)
               LOAD_FAST_BORROW         7 (cap)
               BINARY_SLICE
               GET_ITER
       L9:     FOR_ITER                23 (to L10)
               STORE_FAST               8 (n)

 95            LOAD_FAST_BORROW         4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              41 ('    - ')
               LOAD_FAST_BORROW         8 (n)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           25 (to L9)

 94   L10:     END_FOR
               POP_ITER

 96            LOAD_GLOBAL             13 (len + NULL)
               LOAD_FAST_BORROW         6 (files)
               CALL                     1
               LOAD_FAST_BORROW         7 (cap)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE       38 (to L11)
               NOT_TAKEN

 97            LOAD_FAST_BORROW         4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              42 ('    ... +')
               LOAD_GLOBAL             13 (len + NULL)
               LOAD_FAST_BORROW         6 (files)
               CALL                     1
               LOAD_FAST_BORROW         7 (cap)
               BINARY_OP               10 (-)
               FORMAT_SIMPLE
               LOAD_CONST              43 (' more')
               BUILD_STRING             3
               CALL                     1
               POP_TOP

 98   L11:     LOAD_FAST_BORROW         4 (lines)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              45 ('========================================================================')
               CALL                     1
               POP_TOP

 99            LOAD_CONST              44 ('\n')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         4 (lines)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts\inspect_backup_archive.py", line 102>:
102           RESUME                   0
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
              LOAD_CONST               4 ('dict')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_inspect at 0x0000018C17EE1CC0, file "scripts\inspect_backup_archive.py", line 102>:
 102            RESUME                   0

 107            LOAD_FAST_BORROW         0 (path)
                LOAD_ATTR                1 (exists + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         8 (to L1)
                NOT_TAKEN

 108            LOAD_CONST               1 ('_error')
                LOAD_CONST               2 ('archive not found: ')
                LOAD_FAST_BORROW         0 (path)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_MAP                1
                RETURN_VALUE

 109    L1:     NOP

 110    L2:     LOAD_GLOBAL              3 (read_archive_header + NULL)
                LOAD_FAST_BORROW         0 (path)
                CALL                     1
                STORE_FAST               1 (info)

 117    L3:     LOAD_CONST               5 ('archive_path')
                LOAD_GLOBAL             11 (str + NULL)
                LOAD_FAST                0 (path)
                CALL                     1

 118            LOAD_CONST               6 ('archive_version')
                LOAD_FAST                1 (info)
                LOAD_CONST               7 ('version')
                BINARY_OP               26 ([])

 119            LOAD_CONST               8 ('encrypted')
                LOAD_FAST                1 (info)
                LOAD_CONST               8 ('encrypted')
                BINARY_OP               26 ([])

 120            LOAD_CONST               9 ('salt_bytes')
                LOAD_GLOBAL             13 (len + NULL)
                LOAD_FAST                1 (info)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              10 ('salt')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              11 (b'')
        L4:     CALL                     1

 121            LOAD_CONST              12 ('nonce_bytes')
                LOAD_GLOBAL             13 (len + NULL)
                LOAD_FAST                1 (info)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              13 ('nonce')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              11 (b'')
        L5:     CALL                     1

 122            LOAD_CONST              14 ('mac_bytes')
                LOAD_GLOBAL             13 (len + NULL)
                LOAD_FAST                1 (info)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              15 ('mac')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              11 (b'')
        L6:     CALL                     1

 123            LOAD_CONST              16 ('ciphertext_bytes')
                LOAD_FAST                1 (info)
                LOAD_CONST              17 ('ciphertext_len')
                BINARY_OP               26 ([])

 124            LOAD_CONST              18 ('total_bytes')
                LOAD_FAST                0 (path)
                LOAD_ATTR               17 (stat + NULL|self)
                CALL                     0
                LOAD_ATTR               18 (st_size)

 125            LOAD_CONST              19 ('header')
                LOAD_FAST                1 (info)
                LOAD_CONST              19 ('header')
                BINARY_OP               26 ([])

 116            BUILD_MAP                9
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 111            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       39 (to L12)
                NOT_TAKEN
                STORE_FAST               2 (e)

 112    L8:     LOAD_CONST               1 ('_error')
                LOAD_GLOBAL              7 (type + NULL)
                LOAD_FAST                2 (e)
                CALL                     1
                LOAD_ATTR                8 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST               3 (': ')
                LOAD_FAST                2 (e)
                FORMAT_SIMPLE
                BUILD_STRING             3
                BUILD_MAP                1
        L9:     SWAP                     2
       L10:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                RETURN_VALUE

  --   L11:     LOAD_CONST               4 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                RERAISE                  1

 111   L12:     RERAISE                  0

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L7 [0]
  L7 to L8 -> L13 [1] lasti
  L8 to L9 -> L11 [1] lasti
  L9 to L10 -> L13 [1] lasti
  L11 to L13 -> L13 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts\inspect_backup_archive.py", line 129>:
129           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17ED9010, file "scripts\inspect_backup_archive.py", line 129>:
129           RESUME                   0

130           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

131           LOAD_CONST               0 ('inspect_backup_archive')

132           LOAD_CONST               1 ('PAS143G — read .pasbak header without decrypting.')

130           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               1 (parser)

134           LOAD_FAST_BORROW         1 (parser)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               3 ('archive')
              LOAD_CONST               4 ('Path to the .pasbak file.')
              LOAD_CONST               5 (('help',))
              CALL_KW                  2
              POP_TOP

135           LOAD_FAST_BORROW         1 (parser)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               6 ('--json')
              LOAD_CONST               7 ('store_true')

136           LOAD_CONST               8 ('Emit JSON instead of the human view.')

135           LOAD_CONST               9 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

137           LOAD_FAST_BORROW         1 (parser)
              LOAD_ATTR                7 (parse_args + NULL|self)
              LOAD_FAST_BORROW         0 (argv)
              CALL                     1
              STORE_FAST               2 (args)

139           LOAD_GLOBAL              9 (Path + NULL)
              LOAD_FAST_BORROW         2 (args)
              LOAD_ATTR               10 (archive)
              CALL                     1
              STORE_FAST               3 (path)

140           LOAD_GLOBAL             13 (_safe_inspect + NULL)
              LOAD_FAST_BORROW         3 (path)
              CALL                     1
              STORE_FAST               4 (result)

142           LOAD_CONST              10 ('_error')
              LOAD_FAST_BORROW         4 (result)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       40 (to L1)
              NOT_TAKEN

143           LOAD_GLOBAL             15 (print + NULL)
              LOAD_CONST              11 ('[FAIL] ')
              LOAD_FAST_BORROW         4 (result)
              LOAD_CONST              10 ('_error')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2
              LOAD_GLOBAL             16 (sys)
              LOAD_ATTR               18 (stderr)
              LOAD_CONST              12 (('file',))
              CALL_KW                  2
              POP_TOP

144           LOAD_SMALL_INT           1
              RETURN_VALUE

146   L1:     LOAD_FAST_BORROW         2 (args)
              LOAD_ATTR               20 (json)
              TO_BOOL
              POP_JUMP_IF_FALSE       36 (to L2)
              NOT_TAKEN

147           LOAD_GLOBAL             15 (print + NULL)
              LOAD_GLOBAL             20 (json)
              LOAD_ATTR               22 (dumps)
              PUSH_NULL
              LOAD_FAST_BORROW         4 (result)
              LOAD_SMALL_INT           2
              LOAD_CONST              13 (('indent',))
              CALL_KW                  2
              CALL                     1
              POP_TOP

158           LOAD_SMALL_INT           0
              RETURN_VALUE

149   L2:     LOAD_GLOBAL             15 (print + NULL)
              LOAD_GLOBAL             25 (_summarize_for_human + NULL)
              LOAD_FAST_BORROW         3 (path)

150           LOAD_CONST              14 ('version')
              LOAD_FAST_BORROW         4 (result)
              LOAD_CONST              15 ('archive_version')
              BINARY_OP               26 ([])

151           LOAD_CONST              16 ('encrypted')
              LOAD_FAST_BORROW         4 (result)
              LOAD_CONST              16 ('encrypted')
              BINARY_OP               26 ([])

152           LOAD_CONST              17 ('salt')
              LOAD_CONST              18 (b'x')
              LOAD_FAST_BORROW         4 (result)
              LOAD_CONST              19 ('salt_bytes')
              BINARY_OP               26 ([])
              BINARY_OP                5 (*)

153           LOAD_CONST              20 ('nonce')
              LOAD_CONST              18 (b'x')
              LOAD_FAST_BORROW         4 (result)
              LOAD_CONST              21 ('nonce_bytes')
              BINARY_OP               26 ([])
              BINARY_OP                5 (*)

154           LOAD_CONST              22 ('mac')
              LOAD_CONST              18 (b'x')
              LOAD_FAST_BORROW         4 (result)
              LOAD_CONST              23 ('mac_bytes')
              BINARY_OP               26 ([])
              BINARY_OP                5 (*)

155           LOAD_CONST              24 ('ciphertext_len')
              LOAD_FAST_BORROW         4 (result)
              LOAD_CONST              25 ('ciphertext_bytes')
              BINARY_OP               26 ([])

156           LOAD_CONST              26 ('header')
              LOAD_FAST_BORROW         4 (result)
              LOAD_CONST              26 ('header')
              BINARY_OP               26 ([])

149           BUILD_MAP                7
              CALL                     2
              CALL                     1
              POP_TOP

158           LOAD_SMALL_INT           0
              RETURN_VALUE
```
