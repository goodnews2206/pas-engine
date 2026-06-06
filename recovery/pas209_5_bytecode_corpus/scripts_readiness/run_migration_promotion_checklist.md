# scripts_readiness/run_migration_promotion_checklist

- **pyc:** `scripts\__pycache__\run_migration_promotion_checklist.cpython-314.pyc`
- **expected source path (absent):** `scripts/run_migration_promotion_checklist.py`
- **co_filename (from bytecode):** `scripts\run_migration_promotion_checklist.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS188 — Operator-run migration-promotion checklist
generator.

Reads a single ``scripts/migrate_vNN_*.sql`` file and
emits a structured checklist the operator walks through
**by hand** when promoting that migration to a Supabase
project. The checklist mirrors
``docs/pas186_final_pilot_cutover.md`` § 2 verbatim.

**This script DOES NOT execute the migration.** It does
not connect to Supabase. It does not run any SQL. It does
not modify Supabase config. It only reads the SQL file
from disk and produces a checklist.

Usage:

    python scripts/run_migration_promotion_checklist.py \
        --migration scripts/migrate_v35_cutover_approvals.sql \
        [--output migration_promotion_v35.json] \
        [--summary-only] [--json]

Exit codes:
  0 — checklist produced; promotion criteria appear safe
      to walk through (no destructive SQL detected)
  1 — migration appears destructive (DROP / ALTER ... DROP /
      TRUNCATE detected); operator must NOT promote
  2 — bad CLI args / file not found
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Path`, `__future__`, `annotations`, `argparse`, `datetime`, `hashlib`, `json`, `os`, `pathlib`, `re`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_checklist`, `_build_parser`, `_is_proposal`, `_migration_version`, `_scan_additive`, `_scan_destructive`, `_strip_sql_comments`, `_summarise`, `main`

## Env-key candidates

`BLOCK_DESTRUCTIVE`, `PAS188`, `SAFE_TO_WALK`

## String constants (redacted where noted)

- '\nPAS188 — Operator-run migration-promotion checklist\ngenerator.\n\nReads a single ``scripts/migrate_vNN_*.sql`` file and\nemits a structured checklist the operator walks through\n**by hand** when promoting that migration to a Supabase\nproject. The checklist mirrors\n``docs/pas186_final_pilot_cutover.md`` § 2 verbatim.\n\n**This script DOES NOT execute the migration.** It does\nnot connect to Supabase. It does not run any SQL. It does\nnot modify Supabase config. It only reads the SQL file\nfrom disk and produces a checklist.\n\nUsage:\n\n    python scripts/run_migration_promotion_checklist.py \\\n        --migration scripts/migrate_v35_cutover_approvals.sql \\\n        [--output migration_promotion_v35.json] \\\n        [--summary-only] [--json]\n\nExit codes:\n  0 — checklist produced; promotion criteria appear safe\n      to walk through (no destructive SQL detected)\n  1 — migration appears destructive (DROP / ALTER ... DROP /\n      TRUNCATE detected); operator must NOT promote\n  2 — bad CLI args / file not found\n'
- 'utf-8'
- 'src'
- 'str'
- 'return'
- '--[^\\n]*'
- '/\\*.*?\\*/'
- 'List[str]'
- 'bool'
- 'PROPOSAL ONLY'
- 'PROPOSAL-ONLY'
- 'path'
- 'Path'
- 'Optional[int]'
- 'migrate_v'
- '.sql'
- 'Dict[str, Any]'
- 'replace'
- 'BLOCK_DESTRUCTIVE'
- 'SAFE_TO_WALK'
- 'WARNING: migration header does not mention PROPOSAL ONLY. Confirm intent before promoting.'
- 'WARNING: no additive SQL pattern detected. Confirm migration actually creates something.'
- 'phase'
- 'PAS188'
- 'tool'
- 'run_migration_promotion_checklist'
- 'migration_path'
- 'migration_version'
- 'migration_sha256'
- 'is_proposal'
- 'destructive_hits'
- 'additive_hits'
- 'verdict'
- 'notes'
- 'generated_at'
- 'seconds'
- 'promotion_steps'
- 'key'
- 'label'
- 'done'
- 'report'
- '[PAS188-promo] migration='
- ' verdict='
- '  sha256: '
- '  proposal_header_present: '
- '  DESTRUCTIVE_HITS:'
- '    - '
- '  destructive_hits: none'
- '  additive_hits: '
- '  note: '
- '  promotion_steps:'
- '    [ ] '
- '<22'
- ' — '
- 'argparse.ArgumentParser'
- 'PAS188 — Operator-run migration-promotion checklist. Read-only — never executes the migration, never connects to Supabase. Just inspects the SQL file and emits a checklist mirroring docs/pas186_final_pilot_cutover.md § 2.'
- '--migration'
- 'Path to the migrate_vNN_*.sql file to inspect.'
- '--output'
- 'Output JSON path (default: migration_promotion_vNN.json).'
- '--summary-only'
- 'store_true'
- "Don't write report file; print summary only."
- '--json'
- 'Print the full checklist JSON to stdout.'
- 'argv'
- 'Optional[List[str]]'
- 'int'
- 'error: migration file not found: '
- 'error: could not read '
- 'migration_promotion_v'
- '.json'
- 'migration_promotion_'
- '[PAS188-promo] checklist written to '
- '  [warn] failed to write checklist at '

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ('\nPAS188 — Operator-run migration-promotion checklist\ngenerator.\n\nReads a single ``scripts/migrate_vNN_*.sql`` file and\nemits a structured checklist the operator walks through\n**by hand** when promoting that migration to a Supabase\nproject. The checklist mirrors\n``docs/pas186_final_pilot_cutover.md`` § 2 verbatim.\n\n**This script DOES NOT execute the migration.** It does\nnot connect to Supabase. It does not run any SQL. It does\nnot modify Supabase config. It only reads the SQL file\nfrom disk and produces a checklist.\n\nUsage:\n\n    python scripts/run_migration_promotion_checklist.py \\\n        --migration scripts/migrate_v35_cutover_approvals.sql \\\n        [--output migration_promotion_v35.json] \\\n        [--summary-only] [--json]\n\nExit codes:\n  0 — checklist produced; promotion criteria appear safe\n      to walk through (no destructive SQL detected)\n  1 — migration appears destructive (DROP / ALTER ... DROP /\n      TRUNCATE detected); operator must NOT promote\n  2 — bad CLI args / file not found\n')
               STORE_NAME               0 (__doc__)

  31           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  33           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  34           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (hashlib)
               STORE_NAME               4 (hashlib)

  35           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (json)
               STORE_NAME               5 (json)

  36           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (os)
               STORE_NAME               6 (os)

  37           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (re)
               STORE_NAME               7 (re)

  38           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              8 (sys)
               STORE_NAME               8 (sys)

  39           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              9 (datetime)
               IMPORT_FROM              9 (datetime)
               STORE_NAME               9 (datetime)
               IMPORT_FROM             10 (timezone)
               STORE_NAME              10 (timezone)
               POP_TOP

  40           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME             11 (pathlib)
               IMPORT_FROM             12 (Path)
               STORE_NAME              12 (Path)
               POP_TOP

  41           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('Any', 'Dict', 'List', 'Optional'))
               IMPORT_NAME             13 (typing)
               IMPORT_FROM             14 (Any)
               STORE_NAME              14 (Any)
               IMPORT_FROM             15 (Dict)
               STORE_NAME              15 (Dict)
               IMPORT_FROM             16 (List)
               STORE_NAME              16 (List)
               IMPORT_FROM             17 (Optional)
               STORE_NAME              17 (Optional)
               POP_TOP

  44           LOAD_NAME                8 (sys)
               LOAD_ATTR               36 (stdout)
               LOAD_NAME                8 (sys)
               LOAD_ATTR               38 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              20 (_stream)

  45           NOP

  46   L2:     LOAD_NAME               20 (_stream)
               LOAD_ATTR               43 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  44   L4:     END_FOR
               POP_ITER

  55           LOAD_CONST              27 (('\\bDROP\\s+TABLE\\b', '\\bDROP\\s+COLUMN\\b', '\\bDROP\\s+POLICY\\b', '\\bDROP\\s+CONSTRAINT\\b', '\\bDROP\\s+INDEX\\b', '\\bDROP\\s+FUNCTION\\b', '\\bDROP\\s+TRIGGER\\b', '\\bTRUNCATE\\b', '\\bALTER\\s+TABLE\\s+[^;]*\\bDROP\\b', '\\bDELETE\\s+FROM\\b'))
               STORE_NAME              23 (_DESTRUCTIVE_PATTERNS)

  68           LOAD_CONST              28 (('\\bCREATE\\s+TABLE\\b', '\\bCREATE\\s+INDEX\\b', '\\bCREATE\\s+POLICY\\b', '\\bALTER\\s+TABLE\\s+[^;]*\\bADD\\b', '\\bENABLE\\s+ROW\\s+LEVEL\\s+SECURITY\\b'))
               STORE_NAME              24 (_ADDITIVE_PATTERNS)

  77           LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts\run_migration_promotion_checklist.py", line 77>)
               MAKE_FUNCTION
               LOAD_CONST               9 (<code object _strip_sql_comments at 0x0000018C17972D90, file "scripts\run_migration_promotion_checklist.py", line 77>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              25 (_strip_sql_comments)

  84           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts\run_migration_promotion_checklist.py", line 84>)
               MAKE_FUNCTION
               LOAD_CONST              11 (<code object _scan_destructive at 0x0000018C17FA92F0, file "scripts\run_migration_promotion_checklist.py", line 84>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              26 (_scan_destructive)

  93           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts\run_migration_promotion_checklist.py", line 93>)
               MAKE_FUNCTION
               LOAD_CONST              13 (<code object _scan_additive at 0x0000018C1800ABF0, file "scripts\run_migration_promotion_checklist.py", line 93>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              27 (_scan_additive)

 102           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts\run_migration_promotion_checklist.py", line 102>)
               MAKE_FUNCTION
               LOAD_CONST              15 (<code object _is_proposal at 0x0000018C18053E10, file "scripts\run_migration_promotion_checklist.py", line 102>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (_is_proposal)

 107           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts\run_migration_promotion_checklist.py", line 107>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _migration_version at 0x0000018C17F01250, file "scripts\run_migration_promotion_checklist.py", line 107>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              29 (_migration_version)

 123           LOAD_CONST              29 ((('read_end_to_end', 'Operator has read the script end-to-end.'), ('verified_additive', 'Operator has confirmed the script is additive (no DROP / ALTER ... DROP / TRUNCATE / DELETE).'), ('verified_no_upstream', "Operator has grep'd the codebase and confirmed no upstream code path requires the pre-migration schema."), ('applied_in_transaction', "Operator has applied the script in the Supabase SQL editor with 'Run as transaction' ON."), ('verified_schema_delta', 'Operator has verified the intended schema delta is present (column / table / RLS policy as documented in the migration header).'), ('logged_in_ops_log', 'Operator has recorded the migration in the ops log with the executed SHA-256 of the script content + the verification query result.')))
               STORE_NAME              30 (_PROMOTION_STEPS)

 133           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C18026130, file "scripts\run_migration_promotion_checklist.py", line 133>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _build_checklist at 0x0000018C17EDEBC0, file "scripts\run_migration_promotion_checklist.py", line 133>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_build_checklist)

 170           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts\run_migration_promotion_checklist.py", line 170>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _summarise at 0x0000018C18644C40, file "scripts\run_migration_promotion_checklist.py", line 170>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_summarise)

 199           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts\run_migration_promotion_checklist.py", line 199>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _build_parser at 0x0000018C18060F60, file "scripts\run_migration_promotion_checklist.py", line 199>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              33 (_build_parser)

 227           LOAD_CONST              30 ((None,))
               LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts\run_migration_promotion_checklist.py", line 227>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object main at 0x0000018C17E93990, file "scripts\run_migration_promotion_checklist.py", line 227>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              34 (main)

 277           LOAD_NAME               35 (__name__)
               LOAD_CONST              26 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 278           LOAD_NAME                8 (sys)
               LOAD_ATTR               72 (exit)
               PUSH_NULL
               LOAD_NAME               34 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 277   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  47           LOAD_NAME               22 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

  48   L7:     POP_EXCEPT
               JUMP_BACKWARD          132 (to L1)

  47   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts\run_migration_promotion_checklist.py", line 77>:
 77           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('src')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _strip_sql_comments at 0x0000018C17972D90, file "scripts\run_migration_promotion_checklist.py", line 77>:
 77           RESUME                   0

 79           LOAD_GLOBAL              0 (re)
              LOAD_ATTR                2 (sub)
              PUSH_NULL
              LOAD_CONST               0 ('--[^\\n]*')
              LOAD_CONST               1 ('')
              LOAD_FAST_BORROW         0 (src)
              CALL                     3
              STORE_FAST               1 (no_line)

 80           LOAD_GLOBAL              0 (re)
              LOAD_ATTR                2 (sub)
              PUSH_NULL
              LOAD_CONST               2 ('/\\*.*?\\*/')
              LOAD_CONST               1 ('')
              LOAD_FAST_BORROW         1 (no_line)
              LOAD_GLOBAL              0 (re)
              LOAD_ATTR                4 (DOTALL)
              LOAD_CONST               3 (('flags',))
              CALL_KW                  4
              STORE_FAST               2 (no_block)

 81           LOAD_FAST_BORROW         2 (no_block)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts\run_migration_promotion_checklist.py", line 84>:
 84           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('src')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _scan_destructive at 0x0000018C17FA92F0, file "scripts\run_migration_promotion_checklist.py", line 84>:
 84           RESUME                   0

 85           LOAD_GLOBAL              1 (_strip_sql_comments + NULL)
              LOAD_FAST_BORROW         0 (src)
              CALL                     1
              LOAD_ATTR                3 (upper + NULL|self)
              CALL                     0
              STORE_FAST               1 (code)

 86           BUILD_LIST               0
              STORE_FAST               2 (out)

 87           LOAD_GLOBAL              4 (_DESTRUCTIVE_PATTERNS)
              GET_ITER
      L1:     FOR_ITER                50 (to L3)
              STORE_FAST               3 (pat)

 88           LOAD_GLOBAL              6 (re)
              LOAD_ATTR                8 (search)
              PUSH_NULL
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (pat, code)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              JUMP_BACKWARD           33 (to L1)

 89   L2:     LOAD_FAST_BORROW         2 (out)
              LOAD_ATTR               11 (append + NULL|self)
              LOAD_FAST_BORROW         3 (pat)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           52 (to L1)

 87   L3:     END_FOR
              POP_ITER

 90           LOAD_FAST_BORROW         2 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts\run_migration_promotion_checklist.py", line 93>:
 93           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('src')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _scan_additive at 0x0000018C1800ABF0, file "scripts\run_migration_promotion_checklist.py", line 93>:
 93           RESUME                   0

 94           LOAD_GLOBAL              1 (_strip_sql_comments + NULL)
              LOAD_FAST_BORROW         0 (src)
              CALL                     1
              LOAD_ATTR                3 (upper + NULL|self)
              CALL                     0
              STORE_FAST               1 (code)

 95           BUILD_LIST               0
              STORE_FAST               2 (out)

 96           LOAD_GLOBAL              4 (_ADDITIVE_PATTERNS)
              GET_ITER
      L1:     FOR_ITER                50 (to L3)
              STORE_FAST               3 (pat)

 97           LOAD_GLOBAL              6 (re)
              LOAD_ATTR                8 (search)
              PUSH_NULL
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (pat, code)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              JUMP_BACKWARD           33 (to L1)

 98   L2:     LOAD_FAST_BORROW         2 (out)
              LOAD_ATTR               11 (append + NULL|self)
              LOAD_FAST_BORROW         3 (pat)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           52 (to L1)

 96   L3:     END_FOR
              POP_ITER

 99           LOAD_FAST_BORROW         2 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts\run_migration_promotion_checklist.py", line 102>:
102           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('src')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _is_proposal at 0x0000018C18053E10, file "scripts\run_migration_promotion_checklist.py", line 102>:
102           RESUME                   0

103           LOAD_FAST_BORROW         0 (src)
              LOAD_ATTR                1 (upper + NULL|self)
              CALL                     0
              STORE_FAST               1 (upper)

104           LOAD_CONST               0 ('PROPOSAL ONLY')
              LOAD_FAST_BORROW         1 (upper)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('PROPOSAL-ONLY')
              LOAD_FAST_BORROW         1 (upper)
              CONTAINS_OP              0 (in)
      L1:     RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts\run_migration_promotion_checklist.py", line 107>:
107           RESUME                   0
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
              LOAD_CONST               4 ('Optional[int]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _migration_version at 0x0000018C17F01250, file "scripts\run_migration_promotion_checklist.py", line 107>:
 107           RESUME                   0

 108           LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                0 (name)
               STORE_FAST               1 (name)

 109           LOAD_FAST_BORROW         1 (name)
               LOAD_ATTR                3 (startswith + NULL|self)
               LOAD_CONST               0 ('migrate_v')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       24 (to L1)
               NOT_TAKEN
               LOAD_FAST_BORROW         1 (name)
               LOAD_ATTR                5 (endswith + NULL|self)
               LOAD_CONST               1 ('.sql')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

 110   L1:     LOAD_CONST               2 (None)
               RETURN_VALUE

 111   L2:     NOP

 112   L3:     LOAD_FAST_BORROW         1 (name)
               LOAD_GLOBAL              7 (len + NULL)
               LOAD_CONST               0 ('migrate_v')
               CALL                     1
               LOAD_CONST               2 (None)
               BINARY_SLICE
               STORE_FAST               2 (tail)

 113           LOAD_FAST_BORROW         2 (tail)
               LOAD_ATTR                9 (split + NULL|self)
               LOAD_CONST               3 ('_')
               LOAD_SMALL_INT           1
               CALL                     2
               LOAD_SMALL_INT           0
               BINARY_OP               26 ([])
               LOAD_ATTR                9 (split + NULL|self)
               LOAD_CONST               4 ('.')
               LOAD_SMALL_INT           1
               CALL                     2
               LOAD_SMALL_INT           0
               BINARY_OP               26 ([])
               STORE_FAST               3 (num_str)

 114           LOAD_GLOBAL             11 (int + NULL)
               LOAD_FAST_BORROW         3 (num_str)
               CALL                     1
       L4:     RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 115           LOAD_GLOBAL             12 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L7)
               NOT_TAKEN
               POP_TOP

 116   L6:     POP_EXCEPT
               LOAD_CONST               2 (None)
               RETURN_VALUE

 115   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L3 to L4 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026130, file "scripts\run_migration_promotion_checklist.py", line 133>:
133           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('path')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('src')
              LOAD_CONST               4 ('str')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Dict[str, Any]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _build_checklist at 0x0000018C17EDEBC0, file "scripts\run_migration_promotion_checklist.py", line 133>:
 133           RESUME                   0

 134           LOAD_GLOBAL              1 (_scan_destructive + NULL)
               LOAD_FAST_BORROW         1 (src)
               CALL                     1
               STORE_FAST               2 (destructive)

 135           LOAD_GLOBAL              3 (_scan_additive + NULL)
               LOAD_FAST_BORROW         1 (src)
               CALL                     1
               STORE_FAST               3 (additive)

 136           LOAD_GLOBAL              5 (_is_proposal + NULL)
               LOAD_FAST_BORROW         1 (src)
               CALL                     1
               STORE_FAST               4 (proposal)

 137           LOAD_GLOBAL              7 (_migration_version + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               STORE_FAST               5 (version)

 138           LOAD_GLOBAL              8 (hashlib)
               LOAD_ATTR               10 (sha256)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (src)
               LOAD_ATTR               13 (encode + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('errors',))
               CALL_KW                  2
               CALL                     1
               LOAD_ATTR               15 (hexdigest + NULL|self)
               CALL                     0
               STORE_FAST               6 (sha256)

 139           LOAD_FAST_BORROW         2 (destructive)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN
               LOAD_CONST               3 ('BLOCK_DESTRUCTIVE')
               JUMP_FORWARD             1 (to L2)
       L1:     LOAD_CONST               4 ('SAFE_TO_WALK')
       L2:     STORE_FAST               7 (verdict)

 140           BUILD_LIST               0
               STORE_FAST               8 (notes)

 141           LOAD_FAST_BORROW         4 (proposal)
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L3)
               NOT_TAKEN

 142           LOAD_FAST_BORROW         8 (notes)
               LOAD_ATTR               17 (append + NULL|self)

 143           LOAD_CONST               5 ('WARNING: migration header does not mention PROPOSAL ONLY. Confirm intent before promoting.')

 142           CALL                     1
               POP_TOP

 146   L3:     LOAD_FAST_BORROW         3 (additive)
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L4)
               NOT_TAKEN

 147           LOAD_FAST_BORROW         8 (notes)
               LOAD_ATTR               17 (append + NULL|self)

 148           LOAD_CONST               6 ('WARNING: no additive SQL pattern detected. Confirm migration actually creates something.')

 147           CALL                     1
               POP_TOP

 152   L4:     LOAD_CONST               7 ('phase')
               LOAD_CONST               8 ('PAS188')

 153           LOAD_CONST               9 ('tool')
               LOAD_CONST              10 ('run_migration_promotion_checklist')

 154           LOAD_CONST              11 ('migration_path')
               LOAD_GLOBAL             19 (str + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1

 155           LOAD_CONST              12 ('migration_version')
               LOAD_FAST                5 (version)

 156           LOAD_CONST              13 ('migration_sha256')
               LOAD_FAST                6 (sha256)

 157           LOAD_CONST              14 ('is_proposal')
               LOAD_FAST                4 (proposal)

 158           LOAD_CONST              15 ('destructive_hits')
               LOAD_FAST                2 (destructive)

 159           LOAD_CONST              16 ('additive_hits')
               LOAD_FAST                3 (additive)

 160           LOAD_CONST              17 ('verdict')
               LOAD_FAST                7 (verdict)

 161           LOAD_CONST              18 ('notes')
               LOAD_FAST                8 (notes)

 162           LOAD_CONST              19 ('generated_at')
               LOAD_GLOBAL             20 (datetime)
               LOAD_ATTR               22 (now)
               PUSH_NULL
               LOAD_GLOBAL             24 (timezone)
               LOAD_ATTR               26 (utc)
               CALL                     1
               LOAD_ATTR               29 (isoformat + NULL|self)
               LOAD_CONST              20 ('seconds')
               LOAD_CONST              21 (('timespec',))
               CALL_KW                  1

 163           LOAD_CONST              22 ('promotion_steps')

 165           LOAD_GLOBAL             30 (_PROMOTION_STEPS)
               GET_ITER

 163           LOAD_FAST_AND_CLEAR      9 (k)
               LOAD_FAST_AND_CLEAR     10 (label)
               SWAP                     3
       L5:     BUILD_LIST               0
               SWAP                     2

 165   L6:     FOR_ITER                13 (to L7)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST  154 (k, label)

 164           LOAD_CONST              23 ('key')
               LOAD_FAST_BORROW         9 (k)
               LOAD_CONST              24 ('label')
               LOAD_FAST_BORROW        10 (label)
               LOAD_CONST              25 ('done')
               LOAD_CONST              26 (False)
               BUILD_MAP                3
               LIST_APPEND              2
               JUMP_BACKWARD           15 (to L6)

 165   L7:     END_FOR
               POP_ITER

 163   L8:     SWAP                     3
               STORE_FAST              10 (label)
               STORE_FAST               9 (k)

 151           BUILD_MAP               12
               RETURN_VALUE

  --   L9:     SWAP                     2
               POP_TOP

 163           SWAP                     3
               STORE_FAST              10 (label)
               STORE_FAST               9 (k)
               RERAISE                  0
ExceptionTable:
  L5 to L8 -> L9 [26]

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts\run_migration_promotion_checklist.py", line 170>:
170           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _summarise at 0x0000018C18644C40, file "scripts\run_migration_promotion_checklist.py", line 170>:
170           RESUME                   0

171           BUILD_LIST               0
              STORE_FAST               1 (out)

172           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                1 (append + NULL|self)

173           LOAD_CONST               0 ('[PAS188-promo] migration=')
              LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('migration_path')
              BINARY_OP               26 ([])
              CALL                     1
              LOAD_ATTR                4 (name)
              FORMAT_SIMPLE
              LOAD_CONST               2 (' v')

174           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               3 ('migration_version')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST               4 (' verdict=')

175           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

173           BUILD_STRING             6

172           CALL                     1
              POP_TOP

177           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST               6 ('  sha256: ')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('migration_sha256')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP

178           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST               8 ('  proposal_header_present: ')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('is_proposal')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP

179           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              10 ('destructive_hits')
              BINARY_OP               26 ([])
              TO_BOOL
              POP_JUMP_IF_FALSE       55 (to L3)
              NOT_TAKEN

180           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST              11 ('  DESTRUCTIVE_HITS:')
              CALL                     1
              POP_TOP

181           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              10 ('destructive_hits')
              BINARY_OP               26 ([])
              GET_ITER
      L1:     FOR_ITER                23 (to L2)
              STORE_FAST               2 (h)

182           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST              12 ('    - ')
              LOAD_FAST_BORROW         2 (h)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           25 (to L1)

181   L2:     END_FOR
              POP_ITER
              JUMP_FORWARD            17 (to L4)

184   L3:     LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST              13 ('  destructive_hits: none')
              CALL                     1
              POP_TOP

185   L4:     LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              14 ('additive_hits')
              BINARY_OP               26 ([])
              TO_BOOL
              POP_JUMP_IF_FALSE       47 (to L5)
              NOT_TAKEN

186           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST              15 ('  additive_hits: ')
              LOAD_CONST              16 (', ')
              LOAD_ATTR                9 (join + NULL|self)
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              14 ('additive_hits')
              BINARY_OP               26 ([])
              CALL                     1
              BINARY_OP                0 (+)
              CALL                     1
              POP_TOP

187   L5:     LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              17 ('notes')
              BINARY_OP               26 ([])
              GET_ITER
      L6:     FOR_ITER                23 (to L7)
              STORE_FAST               3 (note)

188           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST              18 ('  note: ')
              LOAD_FAST_BORROW         3 (note)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           25 (to L6)

187   L7:     END_FOR
              POP_ITER

189           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST              19 ('  promotion_steps:')
              CALL                     1
              POP_TOP

190           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              20 ('promotion_steps')
              BINARY_OP               26 ([])
              GET_ITER
      L8:     FOR_ITER                41 (to L9)
              STORE_FAST               4 (step)

191           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST              21 ('    [ ] ')
              LOAD_FAST_BORROW         4 (step)
              LOAD_CONST              22 ('key')
              BINARY_OP               26 ([])
              LOAD_CONST              23 ('<22')
              FORMAT_WITH_SPEC
              LOAD_CONST              24 (' — ')
              LOAD_FAST_BORROW         4 (step)
              LOAD_CONST              25 ('label')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           43 (to L8)

190   L9:     END_FOR
              POP_ITER

192           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts\run_migration_promotion_checklist.py", line 199>:
199           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('argparse.ArgumentParser')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _build_parser at 0x0000018C18060F60, file "scripts\run_migration_promotion_checklist.py", line 199>:
199           RESUME                   0

200           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

201           LOAD_CONST               0 ('run_migration_promotion_checklist')

203           LOAD_CONST               1 ('PAS188 — Operator-run migration-promotion checklist. Read-only — never executes the migration, never connects to Supabase. Just inspects the SQL file and emits a checklist mirroring docs/pas186_final_pilot_cutover.md § 2.')

200           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

210           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

211           LOAD_CONST               3 ('--migration')

212           LOAD_CONST               4 (True)

213           LOAD_CONST               5 ('Path to the migrate_vNN_*.sql file to inspect.')

210           LOAD_CONST               6 (('required', 'help'))
              CALL_KW                  3
              POP_TOP

215           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

216           LOAD_CONST               7 ('--output')

217           LOAD_CONST               8 (None)

218           LOAD_CONST               9 ('Output JSON path (default: migration_promotion_vNN.json).')

215           LOAD_CONST              10 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

220           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              11 ('--summary-only')
              LOAD_CONST              12 ('store_true')

221           LOAD_CONST              13 ("Don't write report file; print summary only.")

220           LOAD_CONST              14 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

222           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              15 ('--json')
              LOAD_CONST              12 ('store_true')

223           LOAD_CONST              16 ('Print the full checklist JSON to stdout.')

222           LOAD_CONST              14 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

224           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts\run_migration_promotion_checklist.py", line 227>:
227           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('argv')
              LOAD_CONST               2 ('Optional[List[str]]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object main at 0x0000018C17E93990, file "scripts\run_migration_promotion_checklist.py", line 227>:
 227            RESUME                   0

 228            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 229            NOP

 230    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 234    L2:     LOAD_GLOBAL             11 (Path + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               12 (migration)
                CALL                     1
                STORE_FAST               4 (path)

 235            LOAD_FAST                4 (path)
                LOAD_ATTR               15 (is_file + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L3)
                NOT_TAKEN

 236            LOAD_GLOBAL             17 (print + NULL)
                LOAD_CONST               2 ('error: migration file not found: ')
                LOAD_FAST                4 (path)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             18 (sys)
                LOAD_ATTR               20 (stderr)
                LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 237            LOAD_SMALL_INT           2
                RETURN_VALUE

 239    L3:     NOP

 240    L4:     LOAD_FAST                4 (path)
                LOAD_ATTR               23 (read_text + NULL|self)
                LOAD_CONST               4 ('utf-8')
                LOAD_CONST               5 ('replace')
                LOAD_CONST               6 (('encoding', 'errors'))
                CALL_KW                  2
                STORE_FAST               5 (src)

 248    L5:     LOAD_GLOBAL             31 (_build_checklist + NULL)
                LOAD_FAST_LOAD_FAST     69 (path, src)
                LOAD_CONST               9 (('path', 'src'))
                CALL_KW                  2
                STORE_FAST               6 (report)

 249            LOAD_GLOBAL             33 (_summarise + NULL)
                LOAD_FAST                6 (report)
                CALL                     1
                GET_ITER
        L6:     FOR_ITER                14 (to L7)
                STORE_FAST               7 (line)

 250            LOAD_GLOBAL             17 (print + NULL)
                LOAD_FAST                7 (line)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           16 (to L6)

 249    L7:     END_FOR
                POP_ITER

 252            LOAD_FAST                2 (args)
                LOAD_ATTR               34 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE       137 (to L15)
                NOT_TAKEN

 253            LOAD_FAST                6 (report)
                LOAD_ATTR               37 (get + NULL|self)
                LOAD_CONST              10 ('migration_version')
                CALL                     1
                STORE_FAST               8 (version)

 256            LOAD_FAST                8 (version)
                POP_JUMP_IF_NONE         7 (to L8)
                NOT_TAKEN

 255            LOAD_CONST              11 ('migration_promotion_v')
                LOAD_FAST                8 (version)
                FORMAT_SIMPLE
                LOAD_CONST              12 ('.json')
                BUILD_STRING             3
                JUMP_FORWARD            15 (to L9)

 257    L8:     LOAD_CONST              13 ('migration_promotion_')
                LOAD_FAST                4 (path)
                LOAD_ATTR               38 (stem)
                FORMAT_SIMPLE
                LOAD_CONST              12 ('.json')
                BUILD_STRING             3

 254    L9:     STORE_FAST               9 (default_out)

 259            LOAD_FAST                2 (args)
                LOAD_ATTR               40 (output)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST                9 (default_out)
       L10:     STORE_FAST              10 (out_path)

 260            NOP

 261   L11:     LOAD_GLOBAL             43 (open + NULL)
                LOAD_FAST               10 (out_path)
                LOAD_CONST              14 ('w')
                LOAD_CONST               4 ('utf-8')
                LOAD_CONST              15 (('encoding',))
                CALL_KW                  3
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
       L12:     STORE_FAST              11 (fp)

 262            LOAD_GLOBAL             44 (json)
                LOAD_ATTR               46 (dump)
                PUSH_NULL
                LOAD_FAST_LOAD_FAST    107 (report, fp)
                LOAD_SMALL_INT           2
                LOAD_CONST              16 (True)
                LOAD_CONST              17 (('indent', 'sort_keys'))
                CALL_KW                  4
                POP_TOP

 261   L13:     LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     3
                POP_TOP

 263   L14:     LOAD_GLOBAL             17 (print + NULL)
                LOAD_CONST              18 ('[PAS188-promo] checklist written to ')
                LOAD_FAST               10 (out_path)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 271   L15:     LOAD_FAST                2 (args)
                LOAD_ATTR               44 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L16)
                NOT_TAKEN

 272            LOAD_GLOBAL             17 (print + NULL)
                LOAD_GLOBAL             44 (json)
                LOAD_ATTR               48 (dumps)
                PUSH_NULL
                LOAD_FAST                6 (report)
                LOAD_SMALL_INT           2
                LOAD_CONST              16 (True)
                LOAD_CONST              17 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 274   L16:     LOAD_FAST                6 (report)
                LOAD_CONST              20 ('verdict')
                BINARY_OP               26 ([])
                LOAD_CONST              21 ('SAFE_TO_WALK')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L17)
                NOT_TAKEN
                LOAD_SMALL_INT           0
                RETURN_VALUE
       L17:     LOAD_SMALL_INT           1
                RETURN_VALUE

  --   L18:     PUSH_EXC_INFO

 231            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L27)
                NOT_TAKEN
                STORE_FAST               3 (e)

 232   L19:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST              22 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L20)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L24)
       L20:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L23)
       L21:     NOT_TAKEN
       L22:     POP_TOP
                LOAD_SMALL_INT           0
       L23:     CALL                     1
       L24:     SWAP                     2
       L25:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L26:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 231   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L29:     PUSH_EXC_INFO

 241            LOAD_GLOBAL             24 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       64 (to L33)
                NOT_TAKEN
                STORE_FAST               3 (e)

 242   L30:     LOAD_GLOBAL             17 (print + NULL)

 243            LOAD_CONST               7 ('error: could not read ')
                LOAD_FAST                4 (path)
                FORMAT_SIMPLE
                LOAD_CONST               8 (': ')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             4

 244            LOAD_GLOBAL             18 (sys)
                LOAD_ATTR               20 (stderr)

 242            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 246   L31:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                LOAD_SMALL_INT           2
                RETURN_VALUE

  --   L32:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 241   L33:     RERAISE                  0

  --   L34:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 261   L35:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L36)
                NOT_TAKEN
                RERAISE                  2
       L36:     POP_TOP
       L37:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_BACKWARD_NO_INTERRUPT 251 (to L14)

  --   L38:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L39:     PUSH_EXC_INFO

 264            LOAD_GLOBAL             24 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       64 (to L43)
                NOT_TAKEN
                STORE_FAST               3 (e)

 265   L40:     LOAD_GLOBAL             17 (print + NULL)

 266            LOAD_CONST              19 ('  [warn] failed to write checklist at ')
                LOAD_FAST               10 (out_path)
                FORMAT_SIMPLE
                LOAD_CONST               8 (': ')

 267            LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE

 266            BUILD_STRING             4

 268            LOAD_GLOBAL             18 (sys)
                LOAD_ATTR               20 (stderr)

 265            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP
       L41:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 309 (to L15)

  --   L42:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 264   L43:     RERAISE                  0

  --   L44:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L18 [0]
  L4 to L5 -> L29 [0]
  L11 to L12 -> L39 [0]
  L12 to L13 -> L35 [2] lasti
  L13 to L15 -> L39 [0]
  L18 to L19 -> L28 [1] lasti
  L19 to L21 -> L26 [1] lasti
  L22 to L24 -> L26 [1] lasti
  L24 to L25 -> L28 [1] lasti
  L26 to L28 -> L28 [1] lasti
  L29 to L30 -> L34 [1] lasti
  L30 to L31 -> L32 [1] lasti
  L32 to L34 -> L34 [1] lasti
  L35 to L37 -> L38 [4] lasti
  L37 to L39 -> L39 [0]
  L39 to L40 -> L44 [1] lasti
  L40 to L41 -> L42 [1] lasti
  L42 to L44 -> L44 [1] lasti
```
