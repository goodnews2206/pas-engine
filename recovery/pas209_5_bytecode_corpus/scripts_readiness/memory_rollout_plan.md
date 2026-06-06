# scripts_readiness/memory_rollout_plan

- **pyc:** `scripts\__pycache__\memory_rollout_plan.cpython-314.pyc`
- **expected source path (absent):** `scripts/memory_rollout_plan.py`
- **co_filename (from bytecode):** `scripts\memory_rollout_plan.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS144K — Operator-approved memory-rollout planner CLI.

Reads a PAS144J memory-impact report (and, optionally, the current
brokerage config), builds a proposed rollout plan via
:mod:`app.services.memory.rollout`, and writes the plan to disk.

Hard contract:
  * the CLI is **planning-only**. ``--approve-dry-run`` exercises the
    apply path with ``approve=True`` but the underlying
    ``apply_rollout_plan`` never writes — it returns
    ``status="approved_but_not_applied"``.
  * exit codes:
       0 — recommended action in {no_change, propose_hold, propose_enable}
       1 — recommended action in {propose_investigate, propose_disable}
       2 — bad CLI arguments / unreadable inputs
  * no raw memory / prompt / transcript content is ever surfaced in
    the plan; the rollout module's evidence whitelist closes that
    door, and the CLI re-projects through its own allow-list as a
    defence-in-depth.

Usage:
  python scripts/memory_rollout_plan.py \
      --impact-report memory_impact_report.json

  python scripts/memory_rollout_plan.py \
      --impact-report memory_impact_report.json \
      --current-config brokerage_brk-1.json \
      --json

  python scripts/memory_rollout_plan.py \
      --impact-report memory_impact_report.json --approve-dry-run
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Path`, `__future__`, `annotations`, `app.services.memory`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `rollout`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_exit_code`, `_print_summary`, `_read_json`, `_safe_plan`, `_write_report`, `main`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS144K — Operator-approved memory-rollout planner CLI.\n\nReads a PAS144J memory-impact report (and, optionally, the current\nbrokerage config), builds a proposed rollout plan via\n:mod:`app.services.memory.rollout`, and writes the plan to disk.\n\nHard contract:\n  * the CLI is **planning-only**. ``--approve-dry-run`` exercises the\n    apply path with ``approve=True`` but the underlying\n    ``apply_rollout_plan`` never writes — it returns\n    ``status="approved_but_not_applied"``.\n  * exit codes:\n       0 — recommended action in {no_change, propose_hold, propose_enable}\n       1 — recommended action in {propose_investigate, propose_disable}\n       2 — bad CLI arguments / unreadable inputs\n  * no raw memory / prompt / transcript content is ever surfaced in\n    the plan; the rollout module\'s evidence whitelist closes that\n    door, and the CLI re-projects through its own allow-list as a\n    defence-in-depth.\n\nUsage:\n  python scripts/memory_rollout_plan.py \\\n      --impact-report memory_impact_report.json\n\n  python scripts/memory_rollout_plan.py \\\n      --impact-report memory_impact_report.json \\\n      --current-config brokerage_brk-1.json \\\n      --json\n\n  python scripts/memory_rollout_plan.py \\\n      --impact-report memory_impact_report.json --approve-dry-run\n'
- 'utf-8'
- 'memory_rollout_plan.json'
- 'path'
- 'Optional[str]'
- 'label'
- 'str'
- 'return'
- 'Optional[Dict[str, Any]]'
- 'Read a JSON file. Returns None on missing file or parse failure;\nprints an operator hint to stderr. Never raises.'
- '  [warn] '
- ': not found at '
- ': unreadable ('
- 'plan'
- 'Dict[str, Any]'
- 'Project the plan through the closed allow-list.'
- 'payload'
- 'None'
- '  [warn] failed to write report at '
- 'argparse.ArgumentParser'
- 'memory_rollout_plan'
- 'PAS144K — Translate a PAS144J memory-impact report into an operator-approved rollout plan. Planning-only; never writes to Supabase.'
- '--impact-report'
- 'Path to the PAS144J impact report JSON.'
- '--current-config'
- 'Optional path to the current brokerage config JSON (determines whether memory injection is already enabled).'
- '--output'
- 'Where to write the structural plan. Defaults to ./'
- '--json'
- 'store_true'
- 'Emit the plan JSON on stdout in addition to the file.'
- '--approve-dry-run'
- 'Exercise the apply path with approve=True. PAS144K still does NOT write; the response is status="approved_but_not_applied".'
- 'One-line operator summary. Never prints raw payload values.'
- 'brokerage_id'
- 'recommended_action'
- 'reason'
- 'requires_operator_approval'
- 'current_enabled'
- '[brokerage='
- '] action='
- ' current_enabled='
- ' requires_approval='
- ' reason='
- 'int'
- 'argv'
- 'Optional[List[str]]'
- 'error: --impact-report is required'
- 'impact report'
- 'error: impact report could not be read; cannot build plan'
- 'current config'
- 'generated_at'
- 'status'
- 'applied'
- 'action'
- 'would_patch'
- 'phase'
- 'apply_result'

## Disassembly

```
   0            RESUME                   0

   1            LOAD_CONST               0 ('\nPAS144K — Operator-approved memory-rollout planner CLI.\n\nReads a PAS144J memory-impact report (and, optionally, the current\nbrokerage config), builds a proposed rollout plan via\n:mod:`app.services.memory.rollout`, and writes the plan to disk.\n\nHard contract:\n  * the CLI is **planning-only**. ``--approve-dry-run`` exercises the\n    apply path with ``approve=True`` but the underlying\n    ``apply_rollout_plan`` never writes — it returns\n    ``status="approved_but_not_applied"``.\n  * exit codes:\n       0 — recommended action in {no_change, propose_hold, propose_enable}\n       1 — recommended action in {propose_investigate, propose_disable}\n       2 — bad CLI arguments / unreadable inputs\n  * no raw memory / prompt / transcript content is ever surfaced in\n    the plan; the rollout module\'s evidence whitelist closes that\n    door, and the CLI re-projects through its own allow-list as a\n    defence-in-depth.\n\nUsage:\n  python scripts/memory_rollout_plan.py \\\n      --impact-report memory_impact_report.json\n\n  python scripts/memory_rollout_plan.py \\\n      --impact-report memory_impact_report.json \\\n      --current-config brokerage_brk-1.json \\\n      --json\n\n  python scripts/memory_rollout_plan.py \\\n      --impact-report memory_impact_report.json --approve-dry-run\n')
                STORE_NAME               0 (__doc__)

  35            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('annotations',))
                IMPORT_NAME              1 (__future__)
                IMPORT_FROM              2 (annotations)
                STORE_NAME               2 (annotations)
                POP_TOP

  37            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              3 (argparse)
                STORE_NAME               3 (argparse)

  38            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              4 (json)
                STORE_NAME               4 (json)

  39            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              5 (os)
                STORE_NAME               5 (os)

  40            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              6 (sys)
                STORE_NAME               6 (sys)

  41            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('datetime', 'timezone'))
                IMPORT_NAME              7 (datetime)
                IMPORT_FROM              7 (datetime)
                STORE_NAME               7 (datetime)
                IMPORT_FROM              8 (timezone)
                STORE_NAME               8 (timezone)
                POP_TOP

  42            LOAD_SMALL_INT           0
                LOAD_CONST               4 (('Path',))
                IMPORT_NAME              9 (pathlib)
                IMPORT_FROM             10 (Path)
                STORE_NAME              10 (Path)
                POP_TOP

  43            LOAD_SMALL_INT           0
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

  46            LOAD_NAME                6 (sys)
                LOAD_ATTR               32 (stdout)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               34 (stderr)
                BUILD_TUPLE              2
                GET_ITER
        L1:     FOR_ITER                22 (to L4)
                STORE_NAME              18 (_stream)

  47            NOP

  48    L2:     LOAD_NAME               18 (_stream)
                LOAD_ATTR               39 (reconfigure + NULL|self)
                LOAD_CONST               6 ('utf-8')
                LOAD_CONST               7 (('encoding',))
                CALL_KW                  1
                POP_TOP
        L3:     JUMP_BACKWARD           24 (to L1)

  46    L4:     END_FOR
                POP_ITER

  53            LOAD_NAME                5 (os)
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

  54            LOAD_NAME               26 (_REPO_ROOT)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               42 (path)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       29 (to L5)
                NOT_TAKEN

  55            LOAD_NAME                6 (sys)
                LOAD_ATTR               42 (path)
                LOAD_ATTR               55 (insert + NULL|self)
                LOAD_SMALL_INT           0
                LOAD_NAME               26 (_REPO_ROOT)
                CALL                     2
                POP_TOP

  58    L5:     LOAD_SMALL_INT           0
                LOAD_CONST               9 (('rollout',))
                IMPORT_NAME             28 (app.services.memory)
                IMPORT_FROM             29 (rollout)
                STORE_NAME              30 (rollout_mod)
                POP_TOP

  61            LOAD_CONST              10 ('memory_rollout_plan.json')
                STORE_NAME              31 (REPORT_FILENAME)

  68            LOAD_CONST              26 (('brokerage_id', 'current_enabled', 'recommended_action', 'proposed_config_patch', 'reason', 'evidence', 'requires_operator_approval', 'safe_to_apply', 'warnings'))
                STORE_NAME              32 (_SAFE_PLAN_FIELDS)

  82            LOAD_NAME               33 (frozenset)
                PUSH_NULL

  83            LOAD_NAME               30 (rollout_mod)
                LOAD_ATTR               68 (ACTION_PROPOSE_INVESTIGATE)

  84            LOAD_NAME               30 (rollout_mod)
                LOAD_ATTR               70 (ACTION_PROPOSE_DISABLE)

  82            BUILD_SET                2
                CALL                     1
                STORE_NAME              36 (_EXIT_ONE_ACTIONS)

  92            LOAD_CONST              11 (<code object __annotate__ at 0x0000018C18025C30, file "scripts\memory_rollout_plan.py", line 92>)
                MAKE_FUNCTION
                LOAD_CONST              12 (<code object _read_json at 0x0000018C17EA54C0, file "scripts\memory_rollout_plan.py", line 92>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              37 (_read_json)

 113            LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts\memory_rollout_plan.py", line 113>)
                MAKE_FUNCTION
                LOAD_CONST              14 (<code object _safe_plan at 0x0000018C17F96140, file "scripts\memory_rollout_plan.py", line 113>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              38 (_safe_plan)

 120            LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18024C30, file "scripts\memory_rollout_plan.py", line 120>)
                MAKE_FUNCTION
                LOAD_CONST              16 (<code object _write_report at 0x0000018C179C3A50, file "scripts\memory_rollout_plan.py", line 120>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              39 (_write_report)

 138            LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts\memory_rollout_plan.py", line 138>)
                MAKE_FUNCTION
                LOAD_CONST              18 (<code object _build_parser at 0x0000018C1801C7F0, file "scripts\memory_rollout_plan.py", line 138>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              40 (_build_parser)

 189            LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA34B0, file "scripts\memory_rollout_plan.py", line 189>)
                MAKE_FUNCTION
                LOAD_CONST              20 (<code object _print_summary at 0x0000018C17EC57C0, file "scripts\memory_rollout_plan.py", line 189>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              41 (_print_summary)

 202            LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts\memory_rollout_plan.py", line 202>)
                MAKE_FUNCTION
                LOAD_CONST              22 (<code object _exit_code at 0x0000018C18053870, file "scripts\memory_rollout_plan.py", line 202>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              42 (_exit_code)

 213            LOAD_CONST              27 ((None,))
                LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts\memory_rollout_plan.py", line 213>)
                MAKE_FUNCTION
                LOAD_CONST              24 (<code object main at 0x0000018C17F6F820, file "scripts\memory_rollout_plan.py", line 213>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              43 (main)

 271            LOAD_NAME               44 (__name__)
                LOAD_CONST              25 ('__main__')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       26 (to L6)
                NOT_TAKEN

 272            LOAD_NAME                6 (sys)
                LOAD_ATTR               90 (exit)
                PUSH_NULL
                LOAD_NAME               43 (main)
                PUSH_NULL
                CALL                     0
                CALL                     1
                POP_TOP
                LOAD_CONST               2 (None)
                RETURN_VALUE

 271    L6:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  49            LOAD_NAME               20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L9)
                NOT_TAKEN
                POP_TOP

  50    L8:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD          278 (to L1)

  49    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L7 [1]
  L7 to L8 -> L10 [2] lasti
  L9 to L10 -> L10 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "scripts\memory_rollout_plan.py", line 92>:
 92           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('path')
              LOAD_CONST               2 ('Optional[str]')
              LOAD_CONST               3 ('label')
              LOAD_CONST               4 ('str')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Optional[Dict[str, Any]]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _read_json at 0x0000018C17EA54C0, file "scripts\memory_rollout_plan.py", line 92>:
  92            RESUME                   0

  95            LOAD_FAST_BORROW         0 (path)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

  96            LOAD_CONST               1 (None)
                RETURN_VALUE

  97    L1:     LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (path)
                CALL                     1
                STORE_FAST               2 (p)

  98            LOAD_FAST_BORROW         2 (p)
                LOAD_ATTR                3 (exists + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        36 (to L2)
                NOT_TAKEN

  99            LOAD_GLOBAL              5 (print + NULL)

 100            LOAD_CONST               2 ('  [warn] ')
                LOAD_FAST_BORROW         1 (label)
                FORMAT_SIMPLE
                LOAD_CONST               3 (': not found at ')
                LOAD_FAST_BORROW         0 (path)
                FORMAT_SIMPLE
                BUILD_STRING             4
                LOAD_GLOBAL              6 (sys)
                LOAD_ATTR                8 (stderr)

  99            LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 102            LOAD_CONST               1 (None)
                RETURN_VALUE

 103    L2:     NOP

 104    L3:     LOAD_GLOBAL             10 (json)
                LOAD_ATTR               12 (loads)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (p)
                LOAD_ATTR               15 (read_text + NULL|self)
                LOAD_CONST               5 ('utf-8')
                LOAD_CONST               6 (('encoding',))
                CALL_KW                  1
                CALL                     1
        L4:     RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 105            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       65 (to L9)
                NOT_TAKEN
                STORE_FAST               3 (e)

 106    L6:     LOAD_GLOBAL              5 (print + NULL)

 107            LOAD_CONST               2 ('  [warn] ')
                LOAD_FAST                1 (label)
                FORMAT_SIMPLE
                LOAD_CONST               7 (': unreadable (')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST               8 (')')
                BUILD_STRING             5

 108            LOAD_GLOBAL              6 (sys)
                LOAD_ATTR                8 (stderr)

 106            LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 110    L7:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                LOAD_CONST               1 (None)
                RETURN_VALUE

  --    L8:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 105    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L5 [0]
  L5 to L6 -> L10 [1] lasti
  L6 to L7 -> L8 [1] lasti
  L8 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts\memory_rollout_plan.py", line 113>:
113           RESUME                   0
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

Disassembly of <code object _safe_plan at 0x0000018C17F96140, file "scripts\memory_rollout_plan.py", line 113>:
 113           RESUME                   0

 115           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (plan)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

 116           BUILD_MAP                0
               RETURN_VALUE

 117   L1:     LOAD_GLOBAL              4 (_SAFE_PLAN_FIELDS)
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

 117           SWAP                     2
               STORE_FAST               1 (k)
               RERAISE                  0
ExceptionTable:
  L2 to L4 -> L8 [2]
  L5 to L7 -> L8 [2]

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "scripts\memory_rollout_plan.py", line 120>:
120           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C179C3A50, file "scripts\memory_rollout_plan.py", line 120>:
 120           RESUME                   0

 121           NOP

 122   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 123           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 124           LOAD_CONST               3 ('utf-8')

 122           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 126           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 127   L4:     LOAD_GLOBAL             11 (print + NULL)

 128           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 129           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 128           BUILD_STRING             4

 130           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 127           LOAD_CONST               7 (('file',))
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

 126   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts\memory_rollout_plan.py", line 138>:
138           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1801C7F0, file "scripts\memory_rollout_plan.py", line 138>:
138           RESUME                   0

139           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

140           LOAD_CONST               0 ('memory_rollout_plan')

142           LOAD_CONST               1 ('PAS144K — Translate a PAS144J memory-impact report into an operator-approved rollout plan. Planning-only; never writes to Supabase.')

139           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

147           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

148           LOAD_CONST               3 ('--impact-report')

149           LOAD_CONST               4 (True)

150           LOAD_CONST               5 ('Path to the PAS144J impact report JSON.')

147           LOAD_CONST               6 (('required', 'help'))
              CALL_KW                  3
              POP_TOP

152           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

153           LOAD_CONST               7 ('--current-config')

154           LOAD_CONST               8 (None)

156           LOAD_CONST               9 ('Optional path to the current brokerage config JSON (determines whether memory injection is already enabled).')

152           LOAD_CONST              10 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

160           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

161           LOAD_CONST              11 ('--output')

162           LOAD_GLOBAL              6 (REPORT_FILENAME)

164           LOAD_CONST              12 ('Where to write the structural plan. Defaults to ./')

165           LOAD_GLOBAL              6 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST              13 ('.')

164           BUILD_STRING             3

160           LOAD_CONST              10 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

168           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

169           LOAD_CONST              14 ('--json')

170           LOAD_CONST              15 ('store_true')

171           LOAD_CONST              16 ('Emit the plan JSON on stdout in addition to the file.')

168           LOAD_CONST              17 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

173           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

174           LOAD_CONST              18 ('--approve-dry-run')

175           LOAD_CONST              15 ('store_true')

177           LOAD_CONST              19 ('Exercise the apply path with approve=True. PAS144K still does NOT write; the response is status="approved_but_not_applied".')

173           LOAD_CONST              17 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

182           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "scripts\memory_rollout_plan.py", line 189>:
189           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('plan')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _print_summary at 0x0000018C17EC57C0, file "scripts\memory_rollout_plan.py", line 189>:
189           RESUME                   0

191           LOAD_FAST_BORROW         0 (plan)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('brokerage_id')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               1 (bid)

192           LOAD_FAST_BORROW         0 (plan)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('recommended_action')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('?')
      L2:     STORE_FAST               2 (action)

193           LOAD_FAST_BORROW         0 (plan)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               5 ('reason')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('?')
      L3:     STORE_FAST               3 (reason)

194           LOAD_GLOBAL              3 (bool + NULL)
              LOAD_FAST_BORROW         0 (plan)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               6 ('requires_operator_approval')
              CALL                     1
              CALL                     1
              STORE_FAST               4 (requires)

195           LOAD_GLOBAL              3 (bool + NULL)
              LOAD_FAST_BORROW         0 (plan)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               7 ('current_enabled')
              CALL                     1
              CALL                     1
              STORE_FAST               5 (enabled)

196           LOAD_GLOBAL              5 (print + NULL)

197           LOAD_CONST               8 ('[brokerage=')
              LOAD_FAST_BORROW         1 (bid)
              FORMAT_SIMPLE
              LOAD_CONST               9 ('] action=')
              LOAD_FAST_BORROW         2 (action)
              FORMAT_SIMPLE
              LOAD_CONST              10 (' current_enabled=')
              LOAD_FAST_BORROW         5 (enabled)
              FORMAT_SIMPLE
              LOAD_CONST              11 (' requires_approval=')

198           LOAD_FAST_BORROW         4 (requires)
              FORMAT_SIMPLE
              LOAD_CONST              12 (' reason=')
              LOAD_FAST_BORROW         3 (reason)
              FORMAT_SIMPLE

197           BUILD_STRING            10

196           CALL                     1
              POP_TOP
              LOAD_CONST              13 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts\memory_rollout_plan.py", line 202>:
202           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('plan')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _exit_code at 0x0000018C18053870, file "scripts\memory_rollout_plan.py", line 202>:
202           RESUME                   0

203           LOAD_FAST_BORROW         0 (plan)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('recommended_action')
              CALL                     1
              STORE_FAST               1 (action)

204           LOAD_FAST_BORROW         1 (action)
              LOAD_GLOBAL              2 (_EXIT_ONE_ACTIONS)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

205           LOAD_SMALL_INT           1
              RETURN_VALUE

206   L1:     LOAD_SMALL_INT           0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts\memory_rollout_plan.py", line 213>:
213           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17F6F820, file "scripts\memory_rollout_plan.py", line 213>:
 213            RESUME                   0

 214            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 215            NOP

 216    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 220    L2:     LOAD_FAST                2 (args)
                LOAD_ATTR               10 (impact_report)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L3:     LOAD_ATTR               13 (strip + NULL|self)
                CALL                     0
                STORE_FAST               4 (impact_path)

 221            LOAD_FAST                4 (impact_path)
                TO_BOOL
                POP_JUMP_IF_TRUE        30 (to L4)
                NOT_TAKEN

 222            LOAD_GLOBAL             15 (print + NULL)
                LOAD_CONST               3 ('error: --impact-report is required')
                LOAD_GLOBAL             16 (sys)
                LOAD_ATTR               18 (stderr)
                LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 223            LOAD_SMALL_INT           2
                RETURN_VALUE

 225    L4:     LOAD_GLOBAL             21 (_read_json + NULL)
                LOAD_FAST                4 (impact_path)
                LOAD_CONST               5 ('impact report')
                CALL                     2
                STORE_FAST               5 (impact_report)

 226            LOAD_FAST                5 (impact_report)
                POP_JUMP_IF_NOT_NONE    30 (to L5)
                NOT_TAKEN

 227            LOAD_GLOBAL             15 (print + NULL)

 228            LOAD_CONST               6 ('error: impact report could not be read; cannot build plan')

 229            LOAD_GLOBAL             16 (sys)
                LOAD_ATTR               18 (stderr)

 227            LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 231            LOAD_SMALL_INT           2
                RETURN_VALUE

 235    L5:     LOAD_FAST                2 (args)
                LOAD_ATTR               22 (current_config)
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L6)
                NOT_TAKEN

 233            LOAD_GLOBAL             21 (_read_json + NULL)

 234            LOAD_FAST                2 (args)
                LOAD_ATTR               22 (current_config)
                LOAD_CONST               7 ('current config')

 233            CALL                     2
                JUMP_FORWARD             1 (to L7)

 235    L6:     LOAD_CONST               1 (None)

 233    L7:     STORE_FAST               6 (current_config)

 237            LOAD_GLOBAL             24 (rollout_mod)
                LOAD_ATTR               26 (build_rollout_plan)
                PUSH_NULL

 238            LOAD_FAST_LOAD_FAST     86 (impact_report, current_config)

 237            LOAD_CONST               8 (('current_config',))
                CALL_KW                  2
                STORE_FAST               7 (plan)

 241            LOAD_CONST               1 (None)
                STORE_FAST               8 (apply_result)

 242            LOAD_FAST                2 (args)
                LOAD_ATTR               28 (approve_dry_run)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L8)
                NOT_TAKEN

 243            LOAD_GLOBAL             24 (rollout_mod)
                LOAD_ATTR               30 (apply_rollout_plan)
                PUSH_NULL
                LOAD_FAST                7 (plan)
                LOAD_CONST               9 (True)
                LOAD_CONST              10 (('approve',))
                CALL_KW                  2
                STORE_FAST               8 (apply_result)

 245    L8:     LOAD_GLOBAL             33 (_safe_plan + NULL)
                LOAD_FAST                7 (plan)
                CALL                     1
                STORE_FAST               9 (safe_plan)

 247            LOAD_CONST              11 ('generated_at')
                LOAD_GLOBAL             34 (datetime)
                LOAD_ATTR               36 (now)
                PUSH_NULL
                LOAD_GLOBAL             38 (timezone)
                LOAD_ATTR               40 (utc)
                CALL                     1
                LOAD_ATTR               43 (isoformat + NULL|self)
                CALL                     0

 248            LOAD_CONST              12 ('plan')
                LOAD_FAST                9 (safe_plan)

 246            BUILD_MAP                2
                STORE_FAST              10 (envelope)

 250            LOAD_FAST                8 (apply_result)
                POP_JUMP_IF_NONE       127 (to L10)
                NOT_TAKEN

 254            LOAD_CONST              13 ('status')
                LOAD_FAST                8 (apply_result)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST              13 ('status')
                CALL                     1

 255            LOAD_CONST              14 ('applied')
                LOAD_GLOBAL             47 (bool + NULL)
                LOAD_FAST                8 (apply_result)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST              14 ('applied')
                CALL                     1
                CALL                     1

 256            LOAD_CONST              15 ('brokerage_id')
                LOAD_FAST                8 (apply_result)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST              15 ('brokerage_id')
                CALL                     1

 257            LOAD_CONST              16 ('action')
                LOAD_FAST                8 (apply_result)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST              16 ('action')
                CALL                     1

 258            LOAD_CONST              17 ('would_patch')
                LOAD_FAST                8 (apply_result)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST              17 ('would_patch')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0

 259    L9:     LOAD_CONST              18 ('phase')
                LOAD_FAST                8 (apply_result)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST              18 ('phase')
                CALL                     1

 253            BUILD_MAP                6
                LOAD_FAST               10 (envelope)
                LOAD_CONST              19 ('apply_result')
                STORE_SUBSCR

 262   L10:     LOAD_GLOBAL             49 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               50 (output)
                LOAD_FAST               10 (envelope)
                CALL                     2
                POP_TOP

 263            LOAD_GLOBAL             53 (_print_summary + NULL)
                LOAD_FAST                9 (safe_plan)
                CALL                     1
                POP_TOP

 265            LOAD_FAST                2 (args)
                LOAD_ATTR               54 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L11)
                NOT_TAKEN

 266            LOAD_GLOBAL             15 (print + NULL)
                LOAD_GLOBAL             54 (json)
                LOAD_ATTR               56 (dumps)
                PUSH_NULL
                LOAD_FAST               10 (envelope)
                LOAD_SMALL_INT           2
                LOAD_CONST               9 (True)
                LOAD_CONST              20 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 268   L11:     LOAD_GLOBAL             59 (_exit_code + NULL)
                LOAD_FAST                9 (safe_plan)
                CALL                     1
                RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 217            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L21)
                NOT_TAKEN
                STORE_FAST               3 (e)

 218   L13:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST              21 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L18)
       L14:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L17)
       L15:     NOT_TAKEN
       L16:     POP_TOP
                LOAD_SMALL_INT           0
       L17:     CALL                     1
       L18:     SWAP                     2
       L19:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L20:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 217   L21:     RERAISE                  0

  --   L22:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L12 [0]
  L12 to L13 -> L22 [1] lasti
  L13 to L15 -> L20 [1] lasti
  L16 to L18 -> L20 [1] lasti
  L18 to L19 -> L22 [1] lasti
  L20 to L22 -> L22 [1] lasti
```
