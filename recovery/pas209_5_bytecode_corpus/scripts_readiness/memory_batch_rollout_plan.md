# scripts_readiness/memory_batch_rollout_plan

- **pyc:** `scripts\__pycache__\memory_batch_rollout_plan.cpython-314.pyc`
- **expected source path (absent):** `scripts/memory_batch_rollout_plan.py`
- **co_filename (from bytecode):** `scripts\memory_batch_rollout_plan.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS144N — Batch rollout planner CLI.

Reads N PAS144J impact reports (one per brokerage) plus an optional
map of current brokerage configs, builds a batch rollout plan via
:mod:`app.services.memory.batch_rollout`, and writes the batch plan
to disk.

Hard contract:
  * the CLI is **planning-only**. There is no apply path.
  * exit codes:
       0 — no propose_disable / propose_investigate in the batch
       1 — at least one propose_disable / propose_investigate
       2 — bad CLI arguments / unreadable inputs
  * never echoes raw payload values — the rollout module's evidence
    whitelist closes that door upstream, and the CLI re-projects
    through its own field allow-list as defence-in-depth.

Usage:
  python scripts/memory_batch_rollout_plan.py \
      --impact-reports-dir ./reports

  python scripts/memory_batch_rollout_plan.py \
      --impact-report a.json --impact-report b.json \
      --current-configs configs.json
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Path`, `__future__`, `annotations`, `app.services.memory`, `argparse`, `batch_rollout`, `json`, `os`, `pathlib`, `rollout`, `sys`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_exit_code`, `_gather_impact_reports`, `_print_summary`, `_read_json`, `_safe_plan`, `_write_report`, `main`

## Env-key candidates

_none_

## String constants (redacted where noted)

- "\nPAS144N — Batch rollout planner CLI.\n\nReads N PAS144J impact reports (one per brokerage) plus an optional\nmap of current brokerage configs, builds a batch rollout plan via\n:mod:`app.services.memory.batch_rollout`, and writes the batch plan\nto disk.\n\nHard contract:\n  * the CLI is **planning-only**. There is no apply path.\n  * exit codes:\n       0 — no propose_disable / propose_investigate in the batch\n       1 — at least one propose_disable / propose_investigate\n       2 — bad CLI arguments / unreadable inputs\n  * never echoes raw payload values — the rollout module's evidence\n    whitelist closes that door upstream, and the CLI re-projects\n    through its own field allow-list as defence-in-depth.\n\nUsage:\n  python scripts/memory_batch_rollout_plan.py \\\n      --impact-reports-dir ./reports\n\n  python scripts/memory_batch_rollout_plan.py \\\n      --impact-report a.json --impact-report b.json \\\n      --current-configs configs.json\n"
- 'utf-8'
- 'memory_batch_rollout_plan.json'
- 'path'
- 'str'
- 'label'
- 'return'
- 'Optional[Dict[str, Any]]'
- '  [warn] '
- ': not found at '
- ': unreadable ('
- 'dir_path'
- 'Optional[str]'
- 'file_paths'
- 'List[str]'
- 'List[Dict[str, Any]]'
- 'Collect impact-report dicts from a directory and/or file paths.\n\nFiles that cannot be parsed are skipped with a stderr warning;\nthey do not crash the run. Non-dict JSON contents are also skipped.\n'
- '  [warn] impact-reports-dir: not a directory at '
- '*.json'
- 'impact report '
- 'plan'
- 'Dict[str, Any]'
- 'payload'
- 'None'
- '  [warn] failed to write report at '
- 'argparse.ArgumentParser'
- 'memory_batch_rollout_plan'
- 'PAS144N — Build a multi-brokerage rollout plan from a set of PAS144J impact reports. Planning-only; never writes to Supabase or any brokerage row.'
- '--impact-reports-dir'
- 'Optional directory of PAS144J impact-report JSON files (*.json). All files are read in sorted order.'
- '--impact-report'
- 'append'
- 'Path to a single PAS144J impact-report JSON. Repeatable. At least one of --impact-reports-dir / --impact-report must be provided.'
- '--current-configs'
- 'Optional JSON file containing a map keyed by brokerage_id of current brokerage configs. Used by the planner to decide whether memory injection is already enabled per tenant.'
- '--output'
- 'Where to write the batch plan. Defaults to ./'
- '--json'
- 'store_true'
- 'Emit the batch plan JSON on stdout in addition to the file.'
- 'summary'
- 'action_counts'
- '[batch='
- 'batch_id'
- '] total='
- 'total_brokerages'
- ' applyable='
- 'applyable_count'
- ' requires_approval='
- 'requires_approval_count'
- ' no_change='
- 'no_change'
- ' propose_enable='
- 'propose_enable'
- ' propose_disable='
- 'propose_disable'
- ' propose_hold='
- 'propose_hold'
- ' propose_investigate='
- 'propose_investigate'
- ' warnings='
- 'warning_count'
- 'batch_plan'
- 'int'
- 'argv'
- 'Optional[List[str]]'
- 'error: at least one of --impact-reports-dir / --impact-report is required'
- 'error: no usable impact reports found; cannot build batch plan'
- 'current configs'
- 'configs'
- 'plans'
- 'created_at'
- 'warnings'

## Disassembly

```
   0            RESUME                   0

   1            LOAD_CONST               0 ("\nPAS144N — Batch rollout planner CLI.\n\nReads N PAS144J impact reports (one per brokerage) plus an optional\nmap of current brokerage configs, builds a batch rollout plan via\n:mod:`app.services.memory.batch_rollout`, and writes the batch plan\nto disk.\n\nHard contract:\n  * the CLI is **planning-only**. There is no apply path.\n  * exit codes:\n       0 — no propose_disable / propose_investigate in the batch\n       1 — at least one propose_disable / propose_investigate\n       2 — bad CLI arguments / unreadable inputs\n  * never echoes raw payload values — the rollout module's evidence\n    whitelist closes that door upstream, and the CLI re-projects\n    through its own field allow-list as defence-in-depth.\n\nUsage:\n  python scripts/memory_batch_rollout_plan.py \\\n      --impact-reports-dir ./reports\n\n  python scripts/memory_batch_rollout_plan.py \\\n      --impact-report a.json --impact-report b.json \\\n      --current-configs configs.json\n")
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
                IMPORT_NAME              4 (json)
                STORE_NAME               4 (json)

  32            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              5 (os)
                STORE_NAME               5 (os)

  33            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              6 (sys)
                STORE_NAME               6 (sys)

  34            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('Path',))
                IMPORT_NAME              7 (pathlib)
                IMPORT_FROM              8 (Path)
                STORE_NAME               8 (Path)
                POP_TOP

  35            LOAD_SMALL_INT           0
                LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
                IMPORT_NAME              9 (typing)
                IMPORT_FROM             10 (Any)
                STORE_NAME              10 (Any)
                IMPORT_FROM             11 (Dict)
                STORE_NAME              11 (Dict)
                IMPORT_FROM             12 (List)
                STORE_NAME              12 (List)
                IMPORT_FROM             13 (Optional)
                STORE_NAME              13 (Optional)
                POP_TOP

  38            LOAD_NAME                6 (sys)
                LOAD_ATTR               28 (stdout)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               30 (stderr)
                BUILD_TUPLE              2
                GET_ITER
        L1:     FOR_ITER                22 (to L4)
                STORE_NAME              16 (_stream)

  39            NOP

  40    L2:     LOAD_NAME               16 (_stream)
                LOAD_ATTR               35 (reconfigure + NULL|self)
                LOAD_CONST               5 ('utf-8')
                LOAD_CONST               6 (('encoding',))
                CALL_KW                  1
                POP_TOP
        L3:     JUMP_BACKWARD           24 (to L1)

  38    L4:     END_FOR
                POP_ITER

  45            LOAD_NAME                5 (os)
                LOAD_ATTR               38 (path)
                LOAD_ATTR               41 (abspath + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               38 (path)
                LOAD_ATTR               43 (join + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               38 (path)
                LOAD_ATTR               45 (dirname + NULL|self)
                LOAD_NAME               23 (__file__)
                CALL                     1
                LOAD_CONST               7 ('..')
                CALL                     2
                CALL                     1
                STORE_NAME              24 (_REPO_ROOT)

  46            LOAD_NAME               24 (_REPO_ROOT)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               38 (path)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       29 (to L5)
                NOT_TAKEN

  47            LOAD_NAME                6 (sys)
                LOAD_ATTR               38 (path)
                LOAD_ATTR               51 (insert + NULL|self)
                LOAD_SMALL_INT           0
                LOAD_NAME               24 (_REPO_ROOT)
                CALL                     2
                POP_TOP

  50    L5:     LOAD_SMALL_INT           0
                LOAD_CONST               8 (('batch_rollout',))
                IMPORT_NAME             26 (app.services.memory)
                IMPORT_FROM             27 (batch_rollout)
                STORE_NAME              28 (batch_mod)
                POP_TOP

  51            LOAD_SMALL_INT           0
                LOAD_CONST               9 (('rollout',))
                IMPORT_NAME             26 (app.services.memory)
                IMPORT_FROM             29 (rollout)
                STORE_NAME              30 (rollout_mod)
                POP_TOP

  54            LOAD_CONST              10 ('memory_batch_rollout_plan.json')
                STORE_NAME              31 (REPORT_FILENAME)

  59            LOAD_CONST              28 (('brokerage_id', 'current_enabled', 'recommended_action', 'proposed_config_patch', 'reason', 'evidence', 'requires_operator_approval', 'safe_to_apply', 'warnings'))
                STORE_NAME              32 (_SAFE_PLAN_FIELDS)

  72            LOAD_NAME               33 (frozenset)
                PUSH_NULL

  73            LOAD_NAME               30 (rollout_mod)
                LOAD_ATTR               68 (ACTION_PROPOSE_INVESTIGATE)

  74            LOAD_NAME               30 (rollout_mod)
                LOAD_ATTR               70 (ACTION_PROPOSE_DISABLE)

  72            BUILD_SET                2
                CALL                     1
                STORE_NAME              36 (_EXIT_ONE_ACTIONS)

  82            LOAD_CONST              11 (<code object __annotate__ at 0x0000018C18026030, file "scripts\memory_batch_rollout_plan.py", line 82>)
                MAKE_FUNCTION
                LOAD_CONST              12 (<code object _read_json at 0x0000018C17ECF940, file "scripts\memory_batch_rollout_plan.py", line 82>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              37 (_read_json)

  99            LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18024E30, file "scripts\memory_batch_rollout_plan.py", line 99>)
                MAKE_FUNCTION
                LOAD_CONST              14 (<code object _gather_impact_reports at 0x0000018C17D7C560, file "scripts\memory_batch_rollout_plan.py", line 99>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              38 (_gather_impact_reports)

 132            LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA30F0, file "scripts\memory_batch_rollout_plan.py", line 132>)
                MAKE_FUNCTION
                LOAD_CONST              16 (<code object _safe_plan at 0x0000018C17F96590, file "scripts\memory_batch_rollout_plan.py", line 132>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              39 (_safe_plan)

 138            LOAD_CONST              17 (<code object __annotate__ at 0x0000018C18025F30, file "scripts\memory_batch_rollout_plan.py", line 138>)
                MAKE_FUNCTION
                LOAD_CONST              18 (<code object _write_report at 0x0000018C179C3C30, file "scripts\memory_batch_rollout_plan.py", line 138>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              40 (_write_report)

 156            LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts\memory_batch_rollout_plan.py", line 156>)
                MAKE_FUNCTION
                LOAD_CONST              20 (<code object _build_parser at 0x0000018C1801C7F0, file "scripts\memory_batch_rollout_plan.py", line 156>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              41 (_build_parser)

 210            LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA2010, file "scripts\memory_batch_rollout_plan.py", line 210>)
                MAKE_FUNCTION
                LOAD_CONST              22 (<code object _print_summary at 0x0000018C17E59E70, file "scripts\memory_batch_rollout_plan.py", line 210>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              42 (_print_summary)

 226            LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA24C0, file "scripts\memory_batch_rollout_plan.py", line 226>)
                MAKE_FUNCTION
                LOAD_CONST              24 (<code object _exit_code at 0x0000018C18010B30, file "scripts\memory_batch_rollout_plan.py", line 226>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              43 (_exit_code)

 238            LOAD_CONST              29 ((None,))
                LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA25B0, file "scripts\memory_batch_rollout_plan.py", line 238>)
                MAKE_FUNCTION
                LOAD_CONST              26 (<code object main at 0x0000018C17D515B0, file "scripts\memory_batch_rollout_plan.py", line 238>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              44 (main)

 300            LOAD_NAME               45 (__name__)
                LOAD_CONST              27 ('__main__')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       26 (to L6)
                NOT_TAKEN

 301            LOAD_NAME                6 (sys)
                LOAD_ATTR               92 (exit)
                PUSH_NULL
                LOAD_NAME               44 (main)
                PUSH_NULL
                CALL                     0
                CALL                     1
                POP_TOP
                LOAD_CONST               2 (None)
                RETURN_VALUE

 300    L6:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  41            LOAD_NAME               18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L9)
                NOT_TAKEN
                POP_TOP

  42    L8:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD          290 (to L1)

  41    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L7 [1]
  L7 to L8 -> L10 [2] lasti
  L9 to L10 -> L10 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026030, file "scripts\memory_batch_rollout_plan.py", line 82>:
 82           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('path')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('label')
              LOAD_CONST               2 ('str')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('Optional[Dict[str, Any]]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _read_json at 0x0000018C17ECF940, file "scripts\memory_batch_rollout_plan.py", line 82>:
  82           RESUME                   0

  83           LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               STORE_FAST               2 (p)

  84           LOAD_FAST_BORROW         2 (p)
               LOAD_ATTR                3 (exists + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        36 (to L1)
               NOT_TAKEN

  85           LOAD_GLOBAL              5 (print + NULL)

  86           LOAD_CONST               0 ('  [warn] ')
               LOAD_FAST_BORROW         1 (label)
               FORMAT_SIMPLE
               LOAD_CONST               1 (': not found at ')
               LOAD_FAST_BORROW         0 (path)
               FORMAT_SIMPLE
               BUILD_STRING             4
               LOAD_GLOBAL              6 (sys)
               LOAD_ATTR                8 (stderr)

  85           LOAD_CONST               2 (('file',))
               CALL_KW                  2
               POP_TOP

  88           LOAD_CONST               3 (None)
               RETURN_VALUE

  89   L1:     NOP

  90   L2:     LOAD_GLOBAL             10 (json)
               LOAD_ATTR               12 (loads)
               PUSH_NULL
               LOAD_FAST_BORROW         2 (p)
               LOAD_ATTR               15 (read_text + NULL|self)
               LOAD_CONST               4 ('utf-8')
               LOAD_CONST               5 (('encoding',))
               CALL_KW                  1
               CALL                     1
       L3:     RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

  91           LOAD_GLOBAL             16 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       65 (to L8)
               NOT_TAKEN
               STORE_FAST               3 (e)

  92   L5:     LOAD_GLOBAL              5 (print + NULL)

  93           LOAD_CONST               0 ('  [warn] ')
               LOAD_FAST                1 (label)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': unreadable (')
               LOAD_GLOBAL             19 (type + NULL)
               LOAD_FAST                3 (e)
               CALL                     1
               LOAD_ATTR               20 (__name__)
               FORMAT_SIMPLE
               LOAD_CONST               7 (')')
               BUILD_STRING             5

  94           LOAD_GLOBAL              6 (sys)
               LOAD_ATTR                8 (stderr)

  92           LOAD_CONST               2 (('file',))
               CALL_KW                  2
               POP_TOP

  96   L6:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               3 (e)
               DELETE_FAST              3 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L7:     LOAD_CONST               3 (None)
               STORE_FAST               3 (e)
               DELETE_FAST              3 (e)
               RERAISE                  1

  91   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L4 [0]
  L4 to L5 -> L9 [1] lasti
  L5 to L6 -> L7 [1] lasti
  L7 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "scripts\memory_batch_rollout_plan.py", line 99>:
 99           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('dir_path')

100           LOAD_CONST               2 ('Optional[str]')

 99           LOAD_CONST               3 ('file_paths')

101           LOAD_CONST               4 ('List[str]')

 99           LOAD_CONST               5 ('return')

102           LOAD_CONST               6 ('List[Dict[str, Any]]')

 99           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _gather_impact_reports at 0x0000018C17D7C560, file "scripts\memory_batch_rollout_plan.py", line 99>:
 99           RESUME                   0

108           BUILD_LIST               0
              STORE_FAST               2 (reports)

110           LOAD_FAST_BORROW         0 (dir_path)
              TO_BOOL
              POP_JUMP_IF_FALSE      173 (to L5)
              NOT_TAKEN

111           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (dir_path)
              CALL                     1
              STORE_FAST               3 (d)

112           LOAD_FAST_BORROW         3 (d)
              LOAD_ATTR                3 (is_dir + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE        32 (to L1)
              NOT_TAKEN

113           LOAD_GLOBAL              5 (print + NULL)

114           LOAD_CONST               1 ('  [warn] impact-reports-dir: not a directory at ')
              LOAD_FAST_BORROW         0 (dir_path)
              FORMAT_SIMPLE
              BUILD_STRING             2

115           LOAD_GLOBAL              6 (sys)
              LOAD_ATTR                8 (stderr)

113           LOAD_CONST               2 (('file',))
              CALL_KW                  2
              POP_TOP
              JUMP_FORWARD           108 (to L5)

119   L1:     LOAD_GLOBAL             11 (sorted + NULL)
              LOAD_FAST_BORROW         3 (d)
              LOAD_ATTR               13 (glob + NULL|self)
              LOAD_CONST               3 ('*.json')
              CALL                     1
              CALL                     1
              GET_ITER
      L2:     FOR_ITER                78 (to L4)
              STORE_FAST               4 (p)

120           LOAD_GLOBAL             15 (_read_json + NULL)
              LOAD_GLOBAL             17 (str + NULL)
              LOAD_FAST_BORROW         4 (p)
              CALL                     1
              LOAD_CONST               4 ('impact report ')
              LOAD_FAST_BORROW         4 (p)
              LOAD_ATTR               18 (name)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     2
              STORE_FAST               5 (data)

121           LOAD_GLOBAL             21 (isinstance + NULL)
              LOAD_FAST_BORROW         5 (data)
              LOAD_GLOBAL             22 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           61 (to L2)

122   L3:     LOAD_FAST_BORROW         2 (reports)
              LOAD_ATTR               25 (append + NULL|self)
              LOAD_FAST_BORROW         5 (data)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           80 (to L2)

119   L4:     END_FOR
              POP_ITER

124   L5:     LOAD_FAST                1 (file_paths)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L6:     GET_ITER
      L7:     FOR_ITER                59 (to L9)
              STORE_FAST               6 (path)

125           LOAD_GLOBAL             15 (_read_json + NULL)
              LOAD_FAST_BORROW         6 (path)
              LOAD_CONST               4 ('impact report ')
              LOAD_FAST_BORROW         6 (path)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     2
              STORE_FAST               5 (data)

126           LOAD_GLOBAL             21 (isinstance + NULL)
              LOAD_FAST_BORROW         5 (data)
              LOAD_GLOBAL             22 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L8)
              NOT_TAKEN
              JUMP_BACKWARD           42 (to L7)

127   L8:     LOAD_FAST_BORROW         2 (reports)
              LOAD_ATTR               25 (append + NULL|self)
              LOAD_FAST_BORROW         5 (data)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           61 (to L7)

124   L9:     END_FOR
              POP_ITER

129           LOAD_FAST_BORROW         2 (reports)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "scripts\memory_batch_rollout_plan.py", line 132>:
132           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('plan')
              LOAD_CONST               2 ('Optional[Dict[str, Any]]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_plan at 0x0000018C17F96590, file "scripts\memory_batch_rollout_plan.py", line 132>:
 132           RESUME                   0

 133           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (plan)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

 134           BUILD_MAP                0
               RETURN_VALUE

 135   L1:     LOAD_GLOBAL              4 (_SAFE_PLAN_FIELDS)
               GET_ITER
               LOAD_FAST_AND_CLEAR      1 (k)
               SWAP                     2
       L2:     BUILD_MAP                0
               SWAP                     2
       L3:     FOR_ITER                28 (to L6)
               STORE_FAST_LOAD_FAST    17 (k, k)
               LOAD_FAST_BORROW         0 (plan)
               CONTAINS_OP              0 (in)
       L4:     POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)
       L5:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (k, plan)
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

 135           SWAP                     2
               STORE_FAST               1 (k)
               RERAISE                  0
ExceptionTable:
  L2 to L4 -> L8 [2]
  L5 to L7 -> L8 [2]

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "scripts\memory_batch_rollout_plan.py", line 138>:
138           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C179C3C30, file "scripts\memory_batch_rollout_plan.py", line 138>:
 138           RESUME                   0

 139           NOP

 140   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 141           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 142           LOAD_CONST               3 ('utf-8')

 140           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 144           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 145   L4:     LOAD_GLOBAL             11 (print + NULL)

 146           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 147           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 146           BUILD_STRING             4

 148           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 145           LOAD_CONST               7 (('file',))
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

 144   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts\memory_batch_rollout_plan.py", line 156>:
156           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1801C7F0, file "scripts\memory_batch_rollout_plan.py", line 156>:
156           RESUME                   0

157           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

158           LOAD_CONST               0 ('memory_batch_rollout_plan')

160           LOAD_CONST               1 ('PAS144N — Build a multi-brokerage rollout plan from a set of PAS144J impact reports. Planning-only; never writes to Supabase or any brokerage row.')

157           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

165           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

166           LOAD_CONST               3 ('--impact-reports-dir')

167           LOAD_CONST               4 (None)

169           LOAD_CONST               5 ('Optional directory of PAS144J impact-report JSON files (*.json). All files are read in sorted order.')

165           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

173           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

174           LOAD_CONST               7 ('--impact-report')

175           LOAD_CONST               8 ('append')

176           BUILD_LIST               0

178           LOAD_CONST               9 ('Path to a single PAS144J impact-report JSON. Repeatable. At least one of --impact-reports-dir / --impact-report must be provided.')

173           LOAD_CONST              10 (('action', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

183           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

184           LOAD_CONST              11 ('--current-configs')

185           LOAD_CONST               4 (None)

187           LOAD_CONST              12 ('Optional JSON file containing a map keyed by brokerage_id of current brokerage configs. Used by the planner to decide whether memory injection is already enabled per tenant.')

183           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

193           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

194           LOAD_CONST              13 ('--output')

195           LOAD_GLOBAL              6 (REPORT_FILENAME)

196           LOAD_CONST              14 ('Where to write the batch plan. Defaults to ./')
              LOAD_GLOBAL              6 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST              15 ('.')
              BUILD_STRING             3

193           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

198           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

199           LOAD_CONST              16 ('--json')

200           LOAD_CONST              17 ('store_true')

201           LOAD_CONST              18 ('Emit the batch plan JSON on stdout in addition to the file.')

198           LOAD_CONST              19 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

203           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "scripts\memory_batch_rollout_plan.py", line 210>:
210           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('summary')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _print_summary at 0x0000018C17E59E70, file "scripts\memory_batch_rollout_plan.py", line 210>:
210           RESUME                   0

211           LOAD_FAST_BORROW         0 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('action_counts')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L1:     STORE_FAST               1 (counts)

212           LOAD_GLOBAL              3 (print + NULL)

213           LOAD_CONST               1 ('[batch=')
              LOAD_FAST_BORROW         0 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               2 ('batch_id')
              LOAD_CONST               3 ('?')
              CALL                     2
              FORMAT_SIMPLE
              LOAD_CONST               4 ('] total=')

214           LOAD_FAST_BORROW         0 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               5 ('total_brokerages')
              LOAD_SMALL_INT           0
              CALL                     2
              FORMAT_SIMPLE
              LOAD_CONST               6 (' applyable=')

215           LOAD_FAST_BORROW         0 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               7 ('applyable_count')
              LOAD_SMALL_INT           0
              CALL                     2
              FORMAT_SIMPLE
              LOAD_CONST               8 (' requires_approval=')

216           LOAD_FAST_BORROW         0 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               9 ('requires_approval_count')
              LOAD_SMALL_INT           0
              CALL                     2
              FORMAT_SIMPLE
              LOAD_CONST              10 (' no_change=')

217           LOAD_FAST_BORROW         1 (counts)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              11 ('no_change')
              LOAD_SMALL_INT           0
              CALL                     2
              FORMAT_SIMPLE
              LOAD_CONST              12 (' propose_enable=')

218           LOAD_FAST_BORROW         1 (counts)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              13 ('propose_enable')
              LOAD_SMALL_INT           0
              CALL                     2
              FORMAT_SIMPLE
              LOAD_CONST              14 (' propose_disable=')

219           LOAD_FAST_BORROW         1 (counts)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              15 ('propose_disable')
              LOAD_SMALL_INT           0
              CALL                     2
              FORMAT_SIMPLE
              LOAD_CONST              16 (' propose_hold=')

220           LOAD_FAST_BORROW         1 (counts)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              17 ('propose_hold')
              LOAD_SMALL_INT           0
              CALL                     2
              FORMAT_SIMPLE
              LOAD_CONST              18 (' propose_investigate=')

221           LOAD_FAST_BORROW         1 (counts)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              19 ('propose_investigate')
              LOAD_SMALL_INT           0
              CALL                     2
              FORMAT_SIMPLE
              LOAD_CONST              20 (' warnings=')

222           LOAD_FAST_BORROW         0 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              21 ('warning_count')
              LOAD_SMALL_INT           0
              CALL                     2
              FORMAT_SIMPLE

213           BUILD_STRING            20

212           CALL                     1
              POP_TOP
              LOAD_CONST              22 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "scripts\memory_batch_rollout_plan.py", line 226>:
226           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('batch_plan')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _exit_code at 0x0000018C18010B30, file "scripts\memory_batch_rollout_plan.py", line 226>:
226           RESUME                   0

227           LOAD_FAST_BORROW         0 (batch_plan)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('action_counts')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L1:     STORE_FAST               1 (counts)

228           LOAD_GLOBAL              2 (_EXIT_ONE_ACTIONS)
              GET_ITER
      L2:     FOR_ITER                29 (to L4)
              STORE_FAST               2 (action)

229           LOAD_FAST_BORROW         1 (counts)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_FAST_BORROW         2 (action)
              LOAD_SMALL_INT           0
              CALL                     2
              LOAD_SMALL_INT           0
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           28 (to L2)

230   L3:     POP_TOP
              LOAD_SMALL_INT           1
              RETURN_VALUE

228   L4:     END_FOR
              POP_ITER

231           LOAD_SMALL_INT           0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "scripts\memory_batch_rollout_plan.py", line 238>:
238           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D515B0, file "scripts\memory_batch_rollout_plan.py", line 238>:
 238            RESUME                   0

 239            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 240            NOP

 241    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 245    L2:     LOAD_FAST                2 (args)
                LOAD_ATTR               10 (impact_reports_dir)
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
        L4:     STORE_FAST               4 (dir_path)

 246            LOAD_GLOBAL             15 (list + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               16 (impact_report)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L5:     CALL                     1
                STORE_FAST               5 (file_paths)

 247            LOAD_FAST                4 (dir_path)
                TO_BOOL
                POP_JUMP_IF_TRUE        38 (to L6)
                NOT_TAKEN
                LOAD_FAST                5 (file_paths)
                TO_BOOL
                POP_JUMP_IF_TRUE        30 (to L6)
                NOT_TAKEN

 248            LOAD_GLOBAL             19 (print + NULL)

 249            LOAD_CONST               3 ('error: at least one of --impact-reports-dir / --impact-report is required')

 251            LOAD_GLOBAL             20 (sys)
                LOAD_ATTR               22 (stderr)

 248            LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 253            LOAD_SMALL_INT           2
                RETURN_VALUE

 255    L6:     LOAD_GLOBAL             25 (_gather_impact_reports + NULL)
                LOAD_FAST_LOAD_FAST     69 (dir_path, file_paths)
                CALL                     2
                STORE_FAST               6 (reports)

 256            LOAD_FAST                6 (reports)
                TO_BOOL
                POP_JUMP_IF_TRUE        30 (to L7)
                NOT_TAKEN

 257            LOAD_GLOBAL             19 (print + NULL)

 258            LOAD_CONST               5 ('error: no usable impact reports found; cannot build batch plan')

 259            LOAD_GLOBAL             20 (sys)
                LOAD_ATTR               22 (stderr)

 257            LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 261            LOAD_SMALL_INT           2
                RETURN_VALUE

 263    L7:     LOAD_CONST               1 (None)
                STORE_FAST               7 (current_configs)

 264            LOAD_FAST                2 (args)
                LOAD_ATTR               26 (current_configs)
                TO_BOOL
                POP_JUMP_IF_FALSE       88 (to L10)
                NOT_TAKEN

 265            LOAD_GLOBAL             29 (_read_json + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               26 (current_configs)
                LOAD_CONST               6 ('current configs')
                CALL                     2
                STORE_FAST               8 (cfg_data)

 266            LOAD_GLOBAL             31 (isinstance + NULL)
                LOAD_FAST                8 (cfg_data)
                LOAD_GLOBAL             32 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       44 (to L10)
                NOT_TAKEN

 269            LOAD_FAST                8 (cfg_data)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST               7 ('configs')
                CALL                     1
                STORE_FAST               9 (inner)

 270            LOAD_GLOBAL             31 (isinstance + NULL)
                LOAD_FAST                9 (inner)
                LOAD_GLOBAL             32 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_FAST                9 (inner)
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_FAST                8 (cfg_data)
        L9:     STORE_FAST               7 (current_configs)

 272   L10:     LOAD_GLOBAL             36 (batch_mod)
                LOAD_ATTR               38 (build_batch_rollout_plan)
                PUSH_NULL

 273            LOAD_FAST_LOAD_FAST    103 (reports, current_configs)

 272            LOAD_CONST               8 (('current_configs',))
                CALL_KW                  2
                STORE_FAST              10 (batch_plan)

 278            LOAD_FAST               10 (batch_plan)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST               9 ('plans')
                BUILD_LIST               0
                CALL                     2
                GET_ITER
                LOAD_FAST_AND_CLEAR     11 (p)
                SWAP                     2
       L11:     BUILD_LIST               0
                SWAP                     2
       L12:     FOR_ITER                14 (to L13)
                STORE_FAST              11 (p)
                LOAD_GLOBAL             41 (_safe_plan + NULL)
                LOAD_FAST               11 (p)
                CALL                     1
                LIST_APPEND              2
                JUMP_BACKWARD           16 (to L12)
       L13:     END_FOR
                POP_ITER
       L14:     STORE_FAST              12 (safe_plans)
                STORE_FAST              11 (p)

 280            LOAD_CONST              10 ('batch_id')
                LOAD_FAST               10 (batch_plan)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST              10 ('batch_id')
                CALL                     1

 281            LOAD_CONST              11 ('created_at')
                LOAD_FAST               10 (batch_plan)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST              11 ('created_at')
                CALL                     1

 282            LOAD_CONST              12 ('total_brokerages')
                LOAD_FAST               10 (batch_plan)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST              12 ('total_brokerages')
                CALL                     1

 283            LOAD_CONST              13 ('action_counts')
                LOAD_FAST               10 (batch_plan)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST              13 ('action_counts')
                CALL                     1

 284            LOAD_CONST              14 ('warnings')
                LOAD_FAST               10 (batch_plan)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST              14 ('warnings')
                CALL                     1

 285            LOAD_CONST               9 ('plans')
                LOAD_FAST               12 (safe_plans)

 279            BUILD_MAP                6
                STORE_FAST              13 (envelope)

 288            LOAD_GLOBAL             36 (batch_mod)
                LOAD_ATTR               42 (batch_plan_summary)
                PUSH_NULL
                LOAD_FAST               10 (batch_plan)
                CALL                     1
                STORE_FAST              14 (summary)

 289            LOAD_FAST_LOAD_FAST    237 (summary, envelope)
                LOAD_CONST              15 ('summary')
                STORE_SUBSCR

 291            LOAD_GLOBAL             45 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               46 (output)
                LOAD_FAST               13 (envelope)
                CALL                     2
                POP_TOP

 292            LOAD_GLOBAL             49 (_print_summary + NULL)
                LOAD_FAST               14 (summary)
                CALL                     1
                POP_TOP

 294            LOAD_FAST                2 (args)
                LOAD_ATTR               50 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L15)
                NOT_TAKEN

 295            LOAD_GLOBAL             19 (print + NULL)
                LOAD_GLOBAL             50 (json)
                LOAD_ATTR               52 (dumps)
                PUSH_NULL
                LOAD_FAST               13 (envelope)
                LOAD_SMALL_INT           2
                LOAD_CONST              16 (True)
                LOAD_CONST              17 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 297   L15:     LOAD_GLOBAL             55 (_exit_code + NULL)
                LOAD_FAST               10 (batch_plan)
                CALL                     1
                RETURN_VALUE

  --   L16:     PUSH_EXC_INFO

 242            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L25)
                NOT_TAKEN
                STORE_FAST               3 (e)

 243   L17:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST              18 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L18)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L22)
       L18:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L21)
       L19:     NOT_TAKEN
       L20:     POP_TOP
                LOAD_SMALL_INT           0
       L21:     CALL                     1
       L22:     SWAP                     2
       L23:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L24:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 242   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L27:     SWAP                     2
                POP_TOP

 278            SWAP                     2
                STORE_FAST              11 (p)
                RERAISE                  0
ExceptionTable:
  L1 to L2 -> L16 [0]
  L11 to L14 -> L27 [2]
  L16 to L17 -> L26 [1] lasti
  L17 to L19 -> L24 [1] lasti
  L20 to L22 -> L24 [1] lasti
  L22 to L23 -> L26 [1] lasti
  L24 to L26 -> L26 [1] lasti
```
