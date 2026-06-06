# scripts_readiness/memory_rollout_history

- **pyc:** `scripts\__pycache__\memory_rollout_history.cpython-314.pyc`
- **expected source path (absent):** `scripts/memory_rollout_history.py`
- **co_filename (from bytecode):** `scripts\memory_rollout_history.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS144M — Memory Rollout History CLI.

Read-only operator inspection of the
``pas_memory_rollout_ledger`` table created by PAS144M.

Usage:
  python scripts/memory_rollout_history.py --brokerage-id brk-1
  python scripts/memory_rollout_history.py --operator-id alice
  python scripts/memory_rollout_history.py \
      --brokerage-id brk-1 --operator-id alice --limit 20

Hard contract:
  * read-only — this CLI never writes to the ledger or the
    brokerage row;
  * at least one of ``--brokerage-id`` / ``--operator-id`` is
    required;
  * when both are provided, the brokerage-history reader is the
    source of truth (so RLS-like tenant scoping always applies) and
    rows are then filtered client-side to the requested operator_id;
  * never echoes raw payload values — the ledger row schema is
    structural by contract, but the CLI also re-projects through a
    closed allow-list as defence-in-depth;
  * exit codes:
       0 — success (zero or more rows returned);
       2 — bad CLI arguments / unreadable inputs.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Path`, `__future__`, `annotations`, `app.services.memory`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `rollout_ledger`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_print_summary`, `_safe_row`, `_write_report`, `main`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS144M — Memory Rollout History CLI.\n\nRead-only operator inspection of the\n``pas_memory_rollout_ledger`` table created by PAS144M.\n\nUsage:\n  python scripts/memory_rollout_history.py --brokerage-id brk-1\n  python scripts/memory_rollout_history.py --operator-id alice\n  python scripts/memory_rollout_history.py \\\n      --brokerage-id brk-1 --operator-id alice --limit 20\n\nHard contract:\n  * read-only — this CLI never writes to the ledger or the\n    brokerage row;\n  * at least one of ``--brokerage-id`` / ``--operator-id`` is\n    required;\n  * when both are provided, the brokerage-history reader is the\n    source of truth (so RLS-like tenant scoping always applies) and\n    rows are then filtered client-side to the requested operator_id;\n  * never echoes raw payload values — the ledger row schema is\n    structural by contract, but the CLI also re-projects through a\n    closed allow-list as defence-in-depth;\n  * exit codes:\n       0 — success (zero or more rows returned);\n       2 — bad CLI arguments / unreadable inputs.\n'
- 'utf-8'
- 'memory_rollout_history_report.json'
- 'row'
- 'Dict[str, Any]'
- 'return'
- 'path'
- 'str'
- 'payload'
- 'None'
- '  [warn] failed to write report at '
- 'argparse.ArgumentParser'
- 'memory_rollout_history'
- 'PAS144M — Inspect operator-approved memory-rollout history from the pas_memory_rollout_ledger table. Read-only.'
- '--brokerage-id'
- 'Tenant scope — list ledger entries for this brokerage. At least one of --brokerage-id / --operator-id is required.'
- '--operator-id'
- 'Operator scope — list ledger entries written by this operator. Combined with --brokerage-id, this filters the tenant-scoped list to a single operator.'
- '--limit'
- 'Maximum number of rows to return (clamped to '
- '--output'
- 'Where to write the structural history report. Defaults to ./'
- '--json'
- 'store_true'
- 'Emit the report JSON on stdout in addition to the file.'
- 'rows'
- 'List[Dict[str, Any]]'
- 'brokerage_id'
- 'Optional[str]'
- 'operator_id'
- 'scope'
- '[scope='
- ' brokerage='
- ' operator='
- '] rows='
- ' applied='
- ' dry_run='
- ' failed='
- 'applied'
- 'apply_status'
- 'dry_run'
- 'argv'
- 'Optional[List[str]]'
- 'int'
- 'error: at least one of --brokerage-id / --operator-id is required'
- 'brokerage+operator_filter'
- 'brokerage'
- 'operator'
- 'generated_at'
- 'limit'
- 'count'

## Disassembly

```
   0            RESUME                   0

   1            LOAD_CONST               0 ('\nPAS144M — Memory Rollout History CLI.\n\nRead-only operator inspection of the\n``pas_memory_rollout_ledger`` table created by PAS144M.\n\nUsage:\n  python scripts/memory_rollout_history.py --brokerage-id brk-1\n  python scripts/memory_rollout_history.py --operator-id alice\n  python scripts/memory_rollout_history.py \\\n      --brokerage-id brk-1 --operator-id alice --limit 20\n\nHard contract:\n  * read-only — this CLI never writes to the ledger or the\n    brokerage row;\n  * at least one of ``--brokerage-id`` / ``--operator-id`` is\n    required;\n  * when both are provided, the brokerage-history reader is the\n    source of truth (so RLS-like tenant scoping always applies) and\n    rows are then filtered client-side to the requested operator_id;\n  * never echoes raw payload values — the ledger row schema is\n    structural by contract, but the CLI also re-projects through a\n    closed allow-list as defence-in-depth;\n  * exit codes:\n       0 — success (zero or more rows returned);\n       2 — bad CLI arguments / unreadable inputs.\n')
                STORE_NAME               0 (__doc__)

  29            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('annotations',))
                IMPORT_NAME              1 (__future__)
                IMPORT_FROM              2 (annotations)
                STORE_NAME               2 (annotations)
                POP_TOP

  31            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              3 (argparse)
                STORE_NAME               3 (argparse)

  32            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              4 (json)
                STORE_NAME               4 (json)

  33            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              5 (os)
                STORE_NAME               5 (os)

  34            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              6 (sys)
                STORE_NAME               6 (sys)

  35            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('datetime', 'timezone'))
                IMPORT_NAME              7 (datetime)
                IMPORT_FROM              7 (datetime)
                STORE_NAME               7 (datetime)
                IMPORT_FROM              8 (timezone)
                STORE_NAME               8 (timezone)
                POP_TOP

  36            LOAD_SMALL_INT           0
                LOAD_CONST               4 (('Path',))
                IMPORT_NAME              9 (pathlib)
                IMPORT_FROM             10 (Path)
                STORE_NAME              10 (Path)
                POP_TOP

  37            LOAD_SMALL_INT           0
                LOAD_CONST               5 (('Any', 'Dict', 'List', 'Optional'))
                IMPORT_NAME             11 (typing)
                IMPORT_FROM             12 (Any)
                STORE_NAME              12 (Any)
                IMPORT_FROM             13 (Dict)
                STORE_NAME              13 (Dict)
                IMPORT_FROM             14 (List)
                STORE_NAME              14 (List)
                IMPORT_FROM             15 (Optional)
                STORE_NAME              15 (Optional)
                POP_TOP

  40            LOAD_NAME                6 (sys)
                LOAD_ATTR               32 (stdout)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               34 (stderr)
                BUILD_TUPLE              2
                GET_ITER
        L1:     FOR_ITER                22 (to L4)
                STORE_NAME              18 (_stream)

  41            NOP

  42    L2:     LOAD_NAME               18 (_stream)
                LOAD_ATTR               39 (reconfigure + NULL|self)
                LOAD_CONST               6 ('utf-8')
                LOAD_CONST               7 (('encoding',))
                CALL_KW                  1
                POP_TOP
        L3:     JUMP_BACKWARD           24 (to L1)

  40    L4:     END_FOR
                POP_ITER

  47            LOAD_NAME                5 (os)
                LOAD_ATTR               42 (path)
                LOAD_ATTR               45 (abspath + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               42 (path)
                LOAD_ATTR               47 (join + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               42 (path)
                LOAD_ATTR               49 (dirname + NULL|self)
                LOAD_NAME               25 (__file__)
                CALL                     1
                LOAD_CONST               8 ('..')
                CALL                     2
                CALL                     1
                STORE_NAME              26 (_REPO_ROOT)

  48            LOAD_NAME               26 (_REPO_ROOT)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               42 (path)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       29 (to L5)
                NOT_TAKEN

  49            LOAD_NAME                6 (sys)
                LOAD_ATTR               42 (path)
                LOAD_ATTR               55 (insert + NULL|self)
                LOAD_SMALL_INT           0
                LOAD_NAME               26 (_REPO_ROOT)
                CALL                     2
                POP_TOP

  52    L5:     LOAD_SMALL_INT           0
                LOAD_CONST               9 (('rollout_ledger',))
                IMPORT_NAME             28 (app.services.memory)
                IMPORT_FROM             29 (rollout_ledger)
                STORE_NAME              30 (ledger_mod)
                POP_TOP

  55            LOAD_CONST              10 ('memory_rollout_history_report.json')
                STORE_NAME              31 (REPORT_FILENAME)

  61            LOAD_CONST              22 (('ledger_id', 'approval_id', 'brokerage_id', 'operator_id', 'recommended_action', 'target_enabled', 'plan_hash', 'approval_status', 'apply_status', 'dry_run', 'applied', 'error_code', 'allowed_patch', 'evidence', 'warnings', 'created_at'))
                STORE_NAME              32 (_SAFE_LEDGER_FIELDS)

  85            LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts\memory_rollout_history.py", line 85>)
                MAKE_FUNCTION
                LOAD_CONST              12 (<code object _safe_row at 0x0000018C17F95E60, file "scripts\memory_rollout_history.py", line 85>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              33 (_safe_row)

  91            LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18024F30, file "scripts\memory_rollout_history.py", line 91>)
                MAKE_FUNCTION
                LOAD_CONST              14 (<code object _write_report at 0x0000018C179A7290, file "scripts\memory_rollout_history.py", line 91>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              34 (_write_report)

 109            LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA3F00, file "scripts\memory_rollout_history.py", line 109>)
                MAKE_FUNCTION
                LOAD_CONST              16 (<code object _build_parser at 0x0000018C17D76780, file "scripts\memory_rollout_history.py", line 109>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              35 (_build_parser)

 163            LOAD_CONST              17 (<code object __annotate__ at 0x0000018C18026030, file "scripts\memory_rollout_history.py", line 163>)
                MAKE_FUNCTION
                LOAD_CONST              18 (<code object _print_summary at 0x0000018C180483B0, file "scripts\memory_rollout_history.py", line 163>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              36 (_print_summary)

 186            LOAD_CONST              23 ((None,))
                LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA2010, file "scripts\memory_rollout_history.py", line 186>)
                MAKE_FUNCTION
                LOAD_CONST              20 (<code object main at 0x0000018C17F71B00, file "scripts\memory_rollout_history.py", line 186>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              37 (main)

 252            LOAD_NAME               38 (__name__)
                LOAD_CONST              21 ('__main__')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       26 (to L6)
                NOT_TAKEN

 253            LOAD_NAME                6 (sys)
                LOAD_ATTR               78 (exit)
                PUSH_NULL
                LOAD_NAME               37 (main)
                PUSH_NULL
                CALL                     0
                CALL                     1
                POP_TOP
                LOAD_CONST               2 (None)
                RETURN_VALUE

 252    L6:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  43            LOAD_NAME               20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

  44    L8:     POP_EXCEPT
                JUMP_BACKWARD          235 (to L1)

  43    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L7 [1]
  L7 to L8 -> L10 [2] lasti
  L9 to L10 -> L10 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts\memory_rollout_history.py", line 85>:
 85           RESUME                   0
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
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_row at 0x0000018C17F95E60, file "scripts\memory_rollout_history.py", line 85>:
  85           RESUME                   0

  86           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (row)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

  87           BUILD_MAP                0
               RETURN_VALUE

  88   L1:     LOAD_GLOBAL              4 (_SAFE_LEDGER_FIELDS)
               GET_ITER
               LOAD_FAST_AND_CLEAR      1 (k)
               SWAP                     2
       L2:     BUILD_MAP                0
               SWAP                     2
       L3:     FOR_ITER                28 (to L6)
               STORE_FAST_LOAD_FAST    17 (k, k)
               LOAD_FAST_BORROW         0 (row)
               CONTAINS_OP              0 (in)
       L4:     POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)
       L5:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (k, row)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_FAST_BORROW         1 (k)
               CALL                     1
               MAP_ADD                  2
               JUMP_BACKWARD           30 (to L3)
       L6:     END_FOR
               POP_ITER
       L7:     SWAP                     2
               STORE_FAST               1 (k)
               RETURN_VALUE

  --   L8:     SWAP                     2
               POP_TOP

  88           SWAP                     2
               STORE_FAST               1 (k)
               RERAISE                  0
ExceptionTable:
  L2 to L4 -> L8 [2]
  L5 to L7 -> L8 [2]

Disassembly of <code object __annotate__ at 0x0000018C18024F30, file "scripts\memory_rollout_history.py", line 91>:
 91           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('path')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('payload')
              LOAD_CONST               4 ('Dict[str, Any]')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('None')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _write_report at 0x0000018C179A7290, file "scripts\memory_rollout_history.py", line 91>:
  91           RESUME                   0

  92           NOP

  93   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

  94           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_GLOBAL              8 (str)
               LOAD_CONST               2 (('indent', 'sort_keys', 'default'))
               CALL_KW                  4

  95           LOAD_CONST               3 ('utf-8')

  93           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

  97           LOAD_GLOBAL             10 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

  98   L4:     LOAD_GLOBAL             13 (print + NULL)

  99           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 100           LOAD_GLOBAL             15 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               16 (__name__)
               FORMAT_SIMPLE

  99           BUILD_STRING             4

 101           LOAD_GLOBAL             18 (sys)
               LOAD_ATTR               20 (stderr)

  98           LOAD_CONST               7 (('file',))
               CALL_KW                  2
               POP_TOP
       L5:     POP_EXCEPT
               LOAD_CONST               8 (None)
               STORE_FAST               2 (e)
               DELETE_FAST              2 (e)
               LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               8 (None)
               STORE_FAST               2 (e)
               DELETE_FAST              2 (e)
               RERAISE                  1

  97   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "scripts\memory_rollout_history.py", line 109>:
109           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C17D76780, file "scripts\memory_rollout_history.py", line 109>:
109           RESUME                   0

110           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

111           LOAD_CONST               0 ('memory_rollout_history')

113           LOAD_CONST               1 ('PAS144M — Inspect operator-approved memory-rollout history from the pas_memory_rollout_ledger table. Read-only.')

110           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

117           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

118           LOAD_CONST               3 ('--brokerage-id')

119           LOAD_CONST               4 (None)

121           LOAD_CONST               5 ('Tenant scope — list ledger entries for this brokerage. At least one of --brokerage-id / --operator-id is required.')

117           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

125           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

126           LOAD_CONST               7 ('--operator-id')

127           LOAD_CONST               4 (None)

129           LOAD_CONST               8 ('Operator scope — list ledger entries written by this operator. Combined with --brokerage-id, this filters the tenant-scoped list to a single operator.')

125           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

134           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

135           LOAD_CONST               9 ('--limit')

136           LOAD_GLOBAL              6 (int)

137           LOAD_GLOBAL              8 (ledger_mod)
              LOAD_ATTR               10 (DEFAULT_HISTORY_LIMIT)

139           LOAD_CONST              10 ('Maximum number of rows to return (clamped to ')

140           LOAD_GLOBAL              8 (ledger_mod)
              LOAD_ATTR               12 (MAX_HISTORY_LIMIT)
              FORMAT_SIMPLE
              LOAD_CONST              11 (').')

139           BUILD_STRING             3

134           LOAD_CONST              12 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

143           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

144           LOAD_CONST              13 ('--output')

145           LOAD_GLOBAL             14 (REPORT_FILENAME)

147           LOAD_CONST              14 ('Where to write the structural history report. Defaults to ./')

148           LOAD_GLOBAL             14 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST              15 ('.')

147           BUILD_STRING             3

143           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

151           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

152           LOAD_CONST              16 ('--json')

153           LOAD_CONST              17 ('store_true')

154           LOAD_CONST              18 ('Emit the report JSON on stdout in addition to the file.')

151           LOAD_CONST              19 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

156           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026030, file "scripts\memory_rollout_history.py", line 163>:
163           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rows')

164           LOAD_CONST               2 ('List[Dict[str, Any]]')

163           LOAD_CONST               3 ('brokerage_id')

166           LOAD_CONST               4 ('Optional[str]')

163           LOAD_CONST               5 ('operator_id')

167           LOAD_CONST               4 ('Optional[str]')

163           LOAD_CONST               6 ('scope')

168           LOAD_CONST               7 ('str')

163           LOAD_CONST               8 ('return')

169           LOAD_CONST               9 ('None')

163           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _print_summary at 0x0000018C180483B0, file "scripts\memory_rollout_history.py", line 163>:
163           RESUME                   0

170           LOAD_GLOBAL              1 (sum + NULL)
              LOAD_CONST               0 (<code object <genexpr> at 0x0000018C1802C620, file "scripts\memory_rollout_history.py", line 170>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         0 (rows)
              GET_ITER
              CALL                     0
              CALL                     1
              STORE_FAST               4 (applied)

171           LOAD_GLOBAL              1 (sum + NULL)
              LOAD_CONST               1 (<code object <genexpr> at 0x0000018C1802CC10, file "scripts\memory_rollout_history.py", line 171>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         0 (rows)
              GET_ITER
              CALL                     0
              CALL                     1
              STORE_FAST               5 (dry_run)

172           LOAD_GLOBAL              1 (sum + NULL)
              LOAD_CONST               2 (<code object <genexpr> at 0x0000018C1802C9B0, file "scripts\memory_rollout_history.py", line 172>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         0 (rows)
              GET_ITER
              CALL                     0
              CALL                     1
              STORE_FAST               6 (failed)

175           LOAD_GLOBAL              3 (print + NULL)

176           LOAD_CONST               3 ('[scope=')
              LOAD_FAST                3 (scope)
              FORMAT_SIMPLE
              LOAD_CONST               4 (' brokerage=')
              LOAD_FAST                1 (brokerage_id)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               5 ('-')
      L1:     FORMAT_SIMPLE
              LOAD_CONST               6 (' operator=')

177           LOAD_FAST                2 (operator_id)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               5 ('-')
      L2:     FORMAT_SIMPLE
              LOAD_CONST               7 ('] rows=')
              LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         0 (rows)
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST               8 (' applied=')

178           LOAD_FAST_BORROW         4 (applied)
              FORMAT_SIMPLE
              LOAD_CONST               9 (' dry_run=')
              LOAD_FAST_BORROW         5 (dry_run)
              FORMAT_SIMPLE
              LOAD_CONST              10 (' failed=')
              LOAD_FAST_BORROW         6 (failed)
              FORMAT_SIMPLE

176           BUILD_STRING            14

175           CALL                     1
              POP_TOP
              LOAD_CONST              11 (None)
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C1802C620, file "scripts\memory_rollout_history.py", line 170>:
 170           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                29 (to L5)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('applied')
               CALL                     1
               LOAD_CONST               1 (True)
               IS_OP                    0 (is)
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           25 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           31 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C1802CC10, file "scripts\memory_rollout_history.py", line 171>:
 171           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                30 (to L5)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('apply_status')
               CALL                     1
               LOAD_CONST               1 ('dry_run')
               COMPARE_OP              88 (bool(==))
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           26 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           32 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C1802C9B0, file "scripts\memory_rollout_history.py", line 172>:
 172           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                30 (to L5)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('apply_status')
               CALL                     1
               LOAD_CONST               2 (('apply_failed', 'invalid_manifest'))
               CONTAINS_OP              0 (in)
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           26 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           32 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "scripts\memory_rollout_history.py", line 186>:
186           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17F71B00, file "scripts\memory_rollout_history.py", line 186>:
 186            RESUME                   0

 187            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 188            NOP

 189    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 193    L2:     LOAD_FAST                2 (args)
                LOAD_ATTR               10 (brokerage_id)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L3:     LOAD_ATTR               13 (strip + NULL|self)
                CALL                     0
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               1 (None)
        L4:     STORE_FAST               4 (brokerage_id)

 194            LOAD_FAST                2 (args)
                LOAD_ATTR               14 (operator_id)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L5:     LOAD_ATTR               13 (strip + NULL|self)
                CALL                     0
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               1 (None)
        L6:     STORE_FAST               5 (operator_id)

 196            LOAD_FAST                4 (brokerage_id)
                TO_BOOL
                POP_JUMP_IF_TRUE        38 (to L7)
                NOT_TAKEN
                LOAD_FAST                5 (operator_id)
                TO_BOOL
                POP_JUMP_IF_TRUE        30 (to L7)
                NOT_TAKEN

 197            LOAD_GLOBAL             17 (print + NULL)

 198            LOAD_CONST               3 ('error: at least one of --brokerage-id / --operator-id is required')

 199            LOAD_GLOBAL             18 (sys)
                LOAD_ATTR               20 (stderr)

 197            LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 201            LOAD_SMALL_INT           2
                RETURN_VALUE

 208    L7:     LOAD_FAST                4 (brokerage_id)
                TO_BOOL
                POP_JUMP_IF_FALSE      113 (to L18)
                NOT_TAKEN

 209            LOAD_GLOBAL             22 (ledger_mod)
                LOAD_ATTR               24 (list_rollout_history_for_brokerage)
                PUSH_NULL

 210            LOAD_FAST_LOAD_FAST     66 (brokerage_id, args)
                LOAD_ATTR               26 (limit)

 209            LOAD_CONST               5 (('limit',))
                CALL_KW                  2
                STORE_FAST               6 (rows)

 212            LOAD_FAST                5 (operator_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       69 (to L17)
                NOT_TAKEN

 214            LOAD_FAST                6 (rows)
                GET_ITER

 213            LOAD_FAST_AND_CLEAR      7 (r)
                SWAP                     2
        L8:     BUILD_LIST               0
                SWAP                     2

 214    L9:     FOR_ITER                53 (to L15)
                STORE_FAST               7 (r)

 215            LOAD_FAST                7 (r)
                LOAD_ATTR               29 (get + NULL|self)
                LOAD_CONST               6 ('operator_id')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
       L10:     NOT_TAKEN
       L11:     POP_TOP
                LOAD_CONST               2 ('')
       L12:     LOAD_ATTR               13 (strip + NULL|self)
                CALL                     0
                LOAD_FAST                5 (operator_id)
                COMPARE_OP              88 (bool(==))

 214   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           51 (to L9)
       L14:     LOAD_FAST                7 (r)
                LIST_APPEND              2
                JUMP_BACKWARD           55 (to L9)
       L15:     END_FOR
                POP_ITER

 213   L16:     STORE_FAST               6 (rows)
                STORE_FAST               7 (r)

 217            LOAD_CONST               7 ('brokerage+operator_filter')
                STORE_FAST               8 (scope)
                JUMP_FORWARD            49 (to L20)

 219   L17:     LOAD_CONST               8 ('brokerage')
                STORE_FAST               8 (scope)
                JUMP_FORWARD            46 (to L20)

 222   L18:     LOAD_GLOBAL             22 (ledger_mod)
                LOAD_ATTR               30 (list_rollout_history_for_operator)
                PUSH_NULL

 223            LOAD_FAST                5 (operator_id)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
       L19:     LOAD_FAST                2 (args)
                LOAD_ATTR               26 (limit)

 222            LOAD_CONST               5 (('limit',))
                CALL_KW                  2
                STORE_FAST               6 (rows)

 225            LOAD_CONST               9 ('operator')
                STORE_FAST               8 (scope)

 227   L20:     LOAD_FAST                6 (rows)
                GET_ITER
                LOAD_FAST_AND_CLEAR      7 (r)
                SWAP                     2
       L21:     BUILD_LIST               0
                SWAP                     2
       L22:     FOR_ITER                14 (to L23)
                STORE_FAST               7 (r)
                LOAD_GLOBAL             33 (_safe_row + NULL)
                LOAD_FAST                7 (r)
                CALL                     1
                LIST_APPEND              2
                JUMP_BACKWARD           16 (to L22)
       L23:     END_FOR
                POP_ITER
       L24:     STORE_FAST               9 (safe_rows)
                STORE_FAST               7 (r)

 229            LOAD_CONST              10 ('generated_at')
                LOAD_GLOBAL             34 (datetime)
                LOAD_ATTR               36 (now)
                PUSH_NULL
                LOAD_GLOBAL             38 (timezone)
                LOAD_ATTR               40 (utc)
                CALL                     1
                LOAD_ATTR               43 (isoformat + NULL|self)
                CALL                     0

 230            LOAD_CONST              11 ('scope')
                LOAD_FAST                8 (scope)

 231            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST                4 (brokerage_id)

 232            LOAD_CONST               6 ('operator_id')
                LOAD_FAST                5 (operator_id)

 233            LOAD_CONST              13 ('limit')
                LOAD_FAST                2 (args)
                LOAD_ATTR               26 (limit)

 234            LOAD_CONST              14 ('count')
                LOAD_GLOBAL             45 (len + NULL)
                LOAD_FAST                9 (safe_rows)
                CALL                     1

 235            LOAD_CONST              15 ('rows')
                LOAD_FAST                9 (safe_rows)

 228            BUILD_MAP                7
                STORE_FAST              10 (envelope)

 238            LOAD_GLOBAL             47 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               48 (output)
                LOAD_FAST               10 (envelope)
                CALL                     2
                POP_TOP

 239            LOAD_GLOBAL             51 (_print_summary + NULL)

 240            LOAD_FAST                9 (safe_rows)

 241            LOAD_FAST                4 (brokerage_id)

 242            LOAD_FAST                5 (operator_id)

 243            LOAD_FAST                8 (scope)

 239            LOAD_CONST              16 (('brokerage_id', 'operator_id', 'scope'))
                CALL_KW                  4
                POP_TOP

 246            LOAD_FAST                2 (args)
                LOAD_ATTR               52 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       40 (to L25)
                NOT_TAKEN

 247            LOAD_GLOBAL             17 (print + NULL)
                LOAD_GLOBAL             52 (json)
                LOAD_ATTR               54 (dumps)
                PUSH_NULL
                LOAD_FAST               10 (envelope)
                LOAD_SMALL_INT           2
                LOAD_CONST              17 (True)
                LOAD_GLOBAL             56 (str)
                LOAD_CONST              18 (('indent', 'sort_keys', 'default'))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 249   L25:     LOAD_SMALL_INT           0
                RETURN_VALUE

  --   L26:     PUSH_EXC_INFO

 190            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L35)
                NOT_TAKEN
                STORE_FAST               3 (e)

 191   L27:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST              19 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L28)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L32)
       L28:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L31)
       L29:     NOT_TAKEN
       L30:     POP_TOP
                LOAD_SMALL_INT           0
       L31:     CALL                     1
       L32:     SWAP                     2
       L33:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L34:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 190   L35:     RERAISE                  0

  --   L36:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L37:     SWAP                     2
                POP_TOP

 213            SWAP                     2
                STORE_FAST               7 (r)
                RERAISE                  0

  --   L38:     SWAP                     2
                POP_TOP

 227            SWAP                     2
                STORE_FAST               7 (r)
                RERAISE                  0
ExceptionTable:
  L1 to L2 -> L26 [0]
  L8 to L10 -> L37 [2]
  L11 to L13 -> L37 [2]
  L14 to L16 -> L37 [2]
  L21 to L24 -> L38 [2]
  L26 to L27 -> L36 [1] lasti
  L27 to L29 -> L34 [1] lasti
  L30 to L32 -> L34 [1] lasti
  L32 to L33 -> L36 [1] lasti
  L34 to L36 -> L36 [1] lasti
```
