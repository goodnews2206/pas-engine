# scripts_readiness/apply_memory_rollout_plan

- **pyc:** `scripts\__pycache__\apply_memory_rollout_plan.cpython-314.pyc`
- **expected source path (absent):** `scripts/apply_memory_rollout_plan.py`
- **co_filename (from bytecode):** `scripts\apply_memory_rollout_plan.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS144L — Apply Memory Rollout Plan CLI.

Reads a PAS144K-built rollout plan from disk, wraps it in an operator
approval manifest, validates it, and conditionally applies it via the
PAS144L safe-apply adapter.

Hard contract:
  * dry-run is the default. ``--apply`` is the only path that may
    write to the brokerage row.
  * the manifest's ``allowed_patch`` is restricted to
    ``features.memory_injection_enabled`` by the adapter — the CLI
    cannot widen it.
  * the report JSON carries structural fields only. No plan evidence
    is surfaced (the rollout module already strips it; the CLI mirrors
    the discipline with an allow-list).
  * exit codes:
      0 — dry-run validated OR live apply succeeded;
      1 — manifest invalid OR live apply failed;
      2 — bad CLI arguments / unreadable inputs.

Usage:
  python scripts/apply_memory_rollout_plan.py \
      --plan memory_rollout_plan.json --operator-id alice

  python scripts/apply_memory_rollout_plan.py \
      --plan memory_rollout_plan.json --operator-id alice \
      --reason "Booking-rate lift confirmed; ramp 1 brokerage." \
      --apply
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Path`, `__future__`, `annotations`, `app.services.memory`, `approval`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `rollout_ledger`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_exit_code`, `_print_summary`, `_read_json`, `_record_ledger_best_effort`, `_safe`, `_unwrap_plan_envelope`, `_write_report`, `main`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS144L — Apply Memory Rollout Plan CLI.\n\nReads a PAS144K-built rollout plan from disk, wraps it in an operator\napproval manifest, validates it, and conditionally applies it via the\nPAS144L safe-apply adapter.\n\nHard contract:\n  * dry-run is the default. ``--apply`` is the only path that may\n    write to the brokerage row.\n  * the manifest\'s ``allowed_patch`` is restricted to\n    ``features.memory_injection_enabled`` by the adapter — the CLI\n    cannot widen it.\n  * the report JSON carries structural fields only. No plan evidence\n    is surfaced (the rollout module already strips it; the CLI mirrors\n    the discipline with an allow-list).\n  * exit codes:\n      0 — dry-run validated OR live apply succeeded;\n      1 — manifest invalid OR live apply failed;\n      2 — bad CLI arguments / unreadable inputs.\n\nUsage:\n  python scripts/apply_memory_rollout_plan.py \\\n      --plan memory_rollout_plan.json --operator-id alice\n\n  python scripts/apply_memory_rollout_plan.py \\\n      --plan memory_rollout_plan.json --operator-id alice \\\n      --reason "Booking-rate lift confirmed; ramp 1 brokerage." \\\n      --apply\n'
- 'utf-8'
- 'memory_rollout_apply_report.json'
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
- 'data'
- 'Any'
- 'Accept either a raw plan dict or the PAS144K CLI envelope\n``{"plan": {...}, "generated_at": ...}``. Returns the inner plan or\n``None`` when nothing usable is present.'
- 'plan'
- 'recommended_action'
- 'Dict[str, Any]'
- 'fields'
- 'tuple'
- 'payload'
- 'None'
- '  [warn] failed to write report at '
- 'argparse.ArgumentParser'
- 'apply_memory_rollout_plan'
- 'PAS144L — Apply a PAS144K operator-approved rollout plan. Dry-run is the default; use --apply to actually write.'
- '--plan'
- 'Path to the PAS144K rollout plan JSON.'
- '--operator-id'
- 'Operator identifier (required) for the signed manifest.'
- '--reason'
- 'Optional free-text reason recorded on the manifest (length-capped, no PII enforcement here).'
- '--apply'
- 'store_true'
- 'Actually apply the patch. Without this flag the run is a dry-run regardless of --dry-run.'
- '--dry-run'
- 'Explicit dry-run flag. Default behaviour is dry-run; this flag is accepted for clarity. Ignored when --apply is set (--apply wins).'
- '--output'
- 'Where to write the structural apply report. Defaults to ./'
- '--json'
- 'Emit the report JSON on stdout in addition to the file.'
- '--record-ledger'
- 'PAS144M — After apply/dry-run, also record this rollout decision in the pas_memory_rollout_ledger table. The ledger write is best-effort: failure to record does NOT change the apply result or the CLI exit code. Default off.'
- 'result'
- 'operator_id'
- 'One-line operator summary. Never prints raw payload values.'
- 'status'
- 'applied'
- 'brokerage_id'
- 'target_enabled'
- 'n/a'
- 'error_code'
- ' error_code='
- '[brokerage='
- '] operator='
- ' action='
- ' target_enabled='
- ' applied='
- ' status='
- 'int'
- 'argv'
- 'Optional[List[str]]'
- 'error: --plan is required'
- 'error: --operator-id is required'
- 'rollout plan'
- 'error: rollout plan could not be read; cannot build manifest'
- 'error: rollout plan JSON is not a recognised plan shape'
- 'error: manifest build rejected: '
- 'generated_at'
- 'mode'
- 'apply'
- 'dry_run'
- 'manifest'
- 'ledger_status'
- 'Wrap the PAS144M ledger writer so a Supabase failure cannot\ncrash the apply CLI. Always returns a small structured dict\nsuitable for inclusion in the report envelope.'
- 'skipped'
- 'reason'
- 'import_failed:'
- 'failed'
- 'unhandled_exception:'
- 'errors'

## Disassembly

```
   0            RESUME                   0

   1            LOAD_CONST               0 ('\nPAS144L — Apply Memory Rollout Plan CLI.\n\nReads a PAS144K-built rollout plan from disk, wraps it in an operator\napproval manifest, validates it, and conditionally applies it via the\nPAS144L safe-apply adapter.\n\nHard contract:\n  * dry-run is the default. ``--apply`` is the only path that may\n    write to the brokerage row.\n  * the manifest\'s ``allowed_patch`` is restricted to\n    ``features.memory_injection_enabled`` by the adapter — the CLI\n    cannot widen it.\n  * the report JSON carries structural fields only. No plan evidence\n    is surfaced (the rollout module already strips it; the CLI mirrors\n    the discipline with an allow-list).\n  * exit codes:\n      0 — dry-run validated OR live apply succeeded;\n      1 — manifest invalid OR live apply failed;\n      2 — bad CLI arguments / unreadable inputs.\n\nUsage:\n  python scripts/apply_memory_rollout_plan.py \\\n      --plan memory_rollout_plan.json --operator-id alice\n\n  python scripts/apply_memory_rollout_plan.py \\\n      --plan memory_rollout_plan.json --operator-id alice \\\n      --reason "Booking-rate lift confirmed; ramp 1 brokerage." \\\n      --apply\n')
                STORE_NAME               0 (__doc__)

  32            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('annotations',))
                IMPORT_NAME              1 (__future__)
                IMPORT_FROM              2 (annotations)
                STORE_NAME               2 (annotations)
                POP_TOP

  34            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              3 (argparse)
                STORE_NAME               3 (argparse)

  35            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              4 (json)
                STORE_NAME               4 (json)

  36            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              5 (os)
                STORE_NAME               5 (os)

  37            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              6 (sys)
                STORE_NAME               6 (sys)

  38            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('datetime', 'timezone'))
                IMPORT_NAME              7 (datetime)
                IMPORT_FROM              7 (datetime)
                STORE_NAME               7 (datetime)
                IMPORT_FROM              8 (timezone)
                STORE_NAME               8 (timezone)
                POP_TOP

  39            LOAD_SMALL_INT           0
                LOAD_CONST               4 (('Path',))
                IMPORT_NAME              9 (pathlib)
                IMPORT_FROM             10 (Path)
                STORE_NAME              10 (Path)
                POP_TOP

  40            LOAD_SMALL_INT           0
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

  43            LOAD_NAME                6 (sys)
                LOAD_ATTR               32 (stdout)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               34 (stderr)
                BUILD_TUPLE              2
                GET_ITER
        L1:     FOR_ITER                22 (to L4)
                STORE_NAME              18 (_stream)

  44            NOP

  45    L2:     LOAD_NAME               18 (_stream)
                LOAD_ATTR               39 (reconfigure + NULL|self)
                LOAD_CONST               6 ('utf-8')
                LOAD_CONST               7 (('encoding',))
                CALL_KW                  1
                POP_TOP
        L3:     JUMP_BACKWARD           24 (to L1)

  43    L4:     END_FOR
                POP_ITER

  50            LOAD_NAME                5 (os)
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

  51            LOAD_NAME               26 (_REPO_ROOT)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               42 (path)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       29 (to L5)
                NOT_TAKEN

  52            LOAD_NAME                6 (sys)
                LOAD_ATTR               42 (path)
                LOAD_ATTR               55 (insert + NULL|self)
                LOAD_SMALL_INT           0
                LOAD_NAME               26 (_REPO_ROOT)
                CALL                     2
                POP_TOP

  55    L5:     LOAD_SMALL_INT           0
                LOAD_CONST               9 (('approval',))
                IMPORT_NAME             28 (app.services.memory)
                IMPORT_FROM             29 (approval)
                STORE_NAME              30 (approval_mod)
                POP_TOP

  58            LOAD_CONST              10 ('memory_rollout_apply_report.json')
                STORE_NAME              31 (REPORT_FILENAME)

  65            LOAD_CONST              30 (('brokerage_id', 'current_enabled', 'recommended_action', 'proposed_config_patch', 'reason', 'evidence', 'requires_operator_approval', 'safe_to_apply', 'warnings'))
                STORE_NAME              32 (_SAFE_PLAN_FIELDS)

  80            LOAD_CONST              31 (('applied', 'would_apply', 'status', 'error_code', 'errors', 'approval_id', 'brokerage_id', 'recommended_action', 'target_enabled', 'dry_run'))
                STORE_NAME              33 (_SAFE_RESULT_FIELDS)

  96            LOAD_CONST              32 (('approval_id', 'approved_at', 'operator_id', 'operator_reason', 'plan_hash', 'approval_status'))
                STORE_NAME              34 (_SAFE_MANIFEST_FIELDS)

 110            LOAD_CONST              11 (<code object __annotate__ at 0x0000018C18024930, file "scripts\apply_memory_rollout_plan.py", line 110>)
                MAKE_FUNCTION
                LOAD_CONST              12 (<code object _read_json at 0x0000018C17E93EF0, file "scripts\apply_memory_rollout_plan.py", line 110>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              35 (_read_json)

 129            LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA34B0, file "scripts\apply_memory_rollout_plan.py", line 129>)
                MAKE_FUNCTION
                LOAD_CONST              14 (<code object _unwrap_plan_envelope at 0x0000018C17F96140, file "scripts\apply_memory_rollout_plan.py", line 129>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              36 (_unwrap_plan_envelope)

 144            LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18026130, file "scripts\apply_memory_rollout_plan.py", line 144>)
                MAKE_FUNCTION
                LOAD_CONST              16 (<code object _safe at 0x0000018C17972D90, file "scripts\apply_memory_rollout_plan.py", line 144>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              37 (_safe)

 150            LOAD_CONST              17 (<code object __annotate__ at 0x0000018C18026530, file "scripts\apply_memory_rollout_plan.py", line 150>)
                MAKE_FUNCTION
                LOAD_CONST              18 (<code object _write_report at 0x0000018C180E8990, file "scripts\apply_memory_rollout_plan.py", line 150>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              38 (_write_report)

 168            LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts\apply_memory_rollout_plan.py", line 168>)
                MAKE_FUNCTION
                LOAD_CONST              20 (<code object _build_parser at 0x0000018C17D8D460, file "scripts\apply_memory_rollout_plan.py", line 168>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              39 (_build_parser)

 234            LOAD_CONST              21 (<code object __annotate__ at 0x0000018C18025F30, file "scripts\apply_memory_rollout_plan.py", line 234>)
                MAKE_FUNCTION
                LOAD_CONST              22 (<code object _print_summary at 0x0000018C17E93990, file "scripts\apply_memory_rollout_plan.py", line 234>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              40 (_print_summary)

 250            LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts\apply_memory_rollout_plan.py", line 250>)
                MAKE_FUNCTION
                LOAD_CONST              24 (<code object _exit_code at 0x0000018C180F4250, file "scripts\apply_memory_rollout_plan.py", line 250>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              41 (_exit_code)

 261            LOAD_CONST              33 ((None,))
                LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts\apply_memory_rollout_plan.py", line 261>)
                MAKE_FUNCTION
                LOAD_CONST              26 (<code object main at 0x0000018C17ED3D90, file "scripts\apply_memory_rollout_plan.py", line 261>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              42 (main)

 343            LOAD_CONST              27 (<code object __annotate__ at 0x0000018C18024E30, file "scripts\apply_memory_rollout_plan.py", line 343>)
                MAKE_FUNCTION
                LOAD_CONST              28 (<code object _record_ledger_best_effort at 0x0000018C17D8C5C0, file "scripts\apply_memory_rollout_plan.py", line 343>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              43 (_record_ledger_best_effort)

 373            LOAD_NAME               44 (__name__)
                LOAD_CONST              29 ('__main__')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       26 (to L6)
                NOT_TAKEN

 374            LOAD_NAME                6 (sys)
                LOAD_ATTR               90 (exit)
                PUSH_NULL
                LOAD_NAME               42 (main)
                PUSH_NULL
                CALL                     0
                CALL                     1
                POP_TOP
                LOAD_CONST               2 (None)
                RETURN_VALUE

 373    L6:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  46            LOAD_NAME               20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L9)
                NOT_TAKEN
                POP_TOP

  47    L8:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD          264 (to L1)

  46    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L7 [1]
  L7 to L8 -> L10 [2] lasti
  L9 to L10 -> L10 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "scripts\apply_memory_rollout_plan.py", line 110>:
110           RESUME                   0
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

Disassembly of <code object _read_json at 0x0000018C17E93EF0, file "scripts\apply_memory_rollout_plan.py", line 110>:
 110            RESUME                   0

 113            LOAD_FAST_BORROW         0 (path)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 114            LOAD_CONST               1 (None)
                RETURN_VALUE

 115    L1:     LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (path)
                CALL                     1
                STORE_FAST               2 (p)

 116            LOAD_FAST_BORROW         2 (p)
                LOAD_ATTR                3 (exists + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        36 (to L2)
                NOT_TAKEN

 117            LOAD_GLOBAL              5 (print + NULL)
                LOAD_CONST               2 ('  [warn] ')
                LOAD_FAST_BORROW         1 (label)
                FORMAT_SIMPLE
                LOAD_CONST               3 (': not found at ')
                LOAD_FAST_BORROW         0 (path)
                FORMAT_SIMPLE
                BUILD_STRING             4
                LOAD_GLOBAL              6 (sys)
                LOAD_ATTR                8 (stderr)
                LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 118            LOAD_CONST               1 (None)
                RETURN_VALUE

 119    L2:     NOP

 120    L3:     LOAD_GLOBAL             10 (json)
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

 121            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       65 (to L9)
                NOT_TAKEN
                STORE_FAST               3 (e)

 122    L6:     LOAD_GLOBAL              5 (print + NULL)

 123            LOAD_CONST               2 ('  [warn] ')
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

 124            LOAD_GLOBAL              6 (sys)
                LOAD_ATTR                8 (stderr)

 122            LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 126    L7:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                LOAD_CONST               1 (None)
                RETURN_VALUE

  --    L8:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 121    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L5 [0]
  L5 to L6 -> L10 [1] lasti
  L6 to L7 -> L8 [1] lasti
  L8 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "scripts\apply_memory_rollout_plan.py", line 129>:
129           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('data')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[Dict[str, Any]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _unwrap_plan_envelope at 0x0000018C17F96140, file "scripts\apply_memory_rollout_plan.py", line 129>:
129           RESUME                   0

133           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (data)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

134           LOAD_CONST               1 (None)
              RETURN_VALUE

135   L1:     LOAD_FAST_BORROW         0 (data)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('plan')
              CALL                     1
              STORE_FAST               1 (inner)

136           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (inner)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

137           LOAD_FAST_BORROW         1 (inner)
              RETURN_VALUE

139   L2:     LOAD_CONST               3 ('recommended_action')
              LOAD_FAST_BORROW         0 (data)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

140           LOAD_FAST_BORROW         0 (data)
              RETURN_VALUE

141   L3:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026130, file "scripts\apply_memory_rollout_plan.py", line 144>:
144           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('d')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('fields')
              LOAD_CONST               4 ('tuple')
              LOAD_CONST               5 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _safe at 0x0000018C17972D90, file "scripts\apply_memory_rollout_plan.py", line 144>:
 144           RESUME                   0

 145           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (d)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

 146           BUILD_MAP                0
               RETURN_VALUE

 147   L1:     LOAD_FAST_BORROW         1 (fields)
               GET_ITER
               LOAD_FAST_AND_CLEAR      2 (k)
               SWAP                     2
       L2:     BUILD_MAP                0
               SWAP                     2
       L3:     FOR_ITER                28 (to L6)
               STORE_FAST_LOAD_FAST    34 (k, k)
               LOAD_FAST_BORROW         0 (d)
               CONTAINS_OP              0 (in)
       L4:     POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)
       L5:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, d)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_FAST_BORROW         2 (k)
               CALL                     1
               MAP_ADD                  2
               JUMP_BACKWARD           30 (to L3)
       L6:     END_FOR
               POP_ITER
       L7:     SWAP                     2
               STORE_FAST               2 (k)
               RETURN_VALUE

  --   L8:     SWAP                     2
               POP_TOP

 147           SWAP                     2
               STORE_FAST               2 (k)
               RERAISE                  0
ExceptionTable:
  L2 to L4 -> L8 [2]
  L5 to L7 -> L8 [2]

Disassembly of <code object __annotate__ at 0x0000018C18026530, file "scripts\apply_memory_rollout_plan.py", line 150>:
150           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C180E8990, file "scripts\apply_memory_rollout_plan.py", line 150>:
 150           RESUME                   0

 151           NOP

 152   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 153           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 154           LOAD_CONST               3 ('utf-8')

 152           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 156           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 157   L4:     LOAD_GLOBAL             11 (print + NULL)

 158           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 159           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 158           BUILD_STRING             4

 160           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 157           LOAD_CONST               7 (('file',))
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

 156   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts\apply_memory_rollout_plan.py", line 168>:
168           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C17D8D460, file "scripts\apply_memory_rollout_plan.py", line 168>:
168           RESUME                   0

169           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

170           LOAD_CONST               0 ('apply_memory_rollout_plan')

172           LOAD_CONST               1 ('PAS144L — Apply a PAS144K operator-approved rollout plan. Dry-run is the default; use --apply to actually write.')

169           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

176           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

177           LOAD_CONST               3 ('--plan')

178           LOAD_CONST               4 (True)

179           LOAD_CONST               5 ('Path to the PAS144K rollout plan JSON.')

176           LOAD_CONST               6 (('required', 'help'))
              CALL_KW                  3
              POP_TOP

181           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

182           LOAD_CONST               7 ('--operator-id')

183           LOAD_CONST               4 (True)

184           LOAD_CONST               8 ('Operator identifier (required) for the signed manifest.')

181           LOAD_CONST               6 (('required', 'help'))
              CALL_KW                  3
              POP_TOP

186           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

187           LOAD_CONST               9 ('--reason')

188           LOAD_CONST              10 (None)

189           LOAD_CONST              11 ('Optional free-text reason recorded on the manifest (length-capped, no PII enforcement here).')

186           LOAD_CONST              12 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

192           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

193           LOAD_CONST              13 ('--apply')

194           LOAD_CONST              14 ('store_true')

195           LOAD_CONST              15 ('Actually apply the patch. Without this flag the run is a dry-run regardless of --dry-run.')

192           LOAD_CONST              16 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

198           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

199           LOAD_CONST              17 ('--dry-run')

200           LOAD_CONST              14 ('store_true')

201           LOAD_CONST               4 (True)

202           LOAD_CONST              18 ('Explicit dry-run flag. Default behaviour is dry-run; this flag is accepted for clarity. Ignored when --apply is set (--apply wins).')

198           LOAD_CONST              19 (('action', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

206           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

207           LOAD_CONST              20 ('--output')

208           LOAD_GLOBAL              6 (REPORT_FILENAME)

209           LOAD_CONST              21 ('Where to write the structural apply report. Defaults to ./')

210           LOAD_GLOBAL              6 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST              22 ('.')

209           BUILD_STRING             3

206           LOAD_CONST              12 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

212           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

213           LOAD_CONST              23 ('--json')

214           LOAD_CONST              14 ('store_true')

215           LOAD_CONST              24 ('Emit the report JSON on stdout in addition to the file.')

212           LOAD_CONST              16 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

217           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

218           LOAD_CONST              25 ('--record-ledger')

219           LOAD_CONST              14 ('store_true')

221           LOAD_CONST              26 ('PAS144M — After apply/dry-run, also record this rollout decision in the pas_memory_rollout_ledger table. The ledger write is best-effort: failure to record does NOT change the apply result or the CLI exit code. Default off.')

217           LOAD_CONST              16 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

227           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "scripts\apply_memory_rollout_plan.py", line 234>:
234           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('result')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('operator_id')
              LOAD_CONST               4 ('str')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('None')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _print_summary at 0x0000018C17E93990, file "scripts\apply_memory_rollout_plan.py", line 234>:
234           RESUME                   0

236           LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('status')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('?')
      L1:     STORE_FAST               2 (status)

237           LOAD_GLOBAL              3 (bool + NULL)
              LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('applied')
              CALL                     1
              CALL                     1
              STORE_FAST               3 (applied)

238           LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               4 ('brokerage_id')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               5 ('')
      L2:     STORE_FAST               4 (bid)

239           LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               6 ('recommended_action')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('?')
      L3:     STORE_FAST               5 (action)

240           LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               7 ('target_enabled')
              CALL                     1
              STORE_FAST               6 (target)

241           LOAD_FAST_BORROW         6 (target)
              POP_JUMP_IF_NOT_NONE     3 (to L4)
              NOT_TAKEN
              LOAD_CONST               9 ('n/a')
              JUMP_FORWARD            33 (to L5)
      L4:     LOAD_GLOBAL              5 (str + NULL)
              LOAD_GLOBAL              3 (bool + NULL)
              LOAD_FAST_BORROW         6 (target)
              CALL                     1
              CALL                     1
              LOAD_ATTR                7 (lower + NULL|self)
              CALL                     0
      L5:     STORE_FAST               7 (target_s)

242           LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              10 ('error_code')
              CALL                     1
              STORE_FAST               8 (err)

243           LOAD_FAST_BORROW         8 (err)
              TO_BOOL
              POP_JUMP_IF_FALSE        6 (to L6)
              NOT_TAKEN
              LOAD_CONST              11 (' error_code=')
              LOAD_FAST_BORROW         8 (err)
              FORMAT_SIMPLE
              BUILD_STRING             2
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST               5 ('')
      L7:     STORE_FAST               9 (err_s)

244           LOAD_GLOBAL              9 (print + NULL)

245           LOAD_CONST              12 ('[brokerage=')
              LOAD_FAST_BORROW         4 (bid)
              FORMAT_SIMPLE
              LOAD_CONST              13 ('] operator=')
              LOAD_FAST_BORROW         1 (operator_id)
              FORMAT_SIMPLE
              LOAD_CONST              14 (' action=')
              LOAD_FAST_BORROW         5 (action)
              FORMAT_SIMPLE
              LOAD_CONST              15 (' target_enabled=')

246           LOAD_FAST_BORROW         7 (target_s)
              FORMAT_SIMPLE
              LOAD_CONST              16 (' applied=')
              LOAD_FAST_BORROW         3 (applied)
              FORMAT_SIMPLE
              LOAD_CONST              17 (' status=')
              LOAD_FAST_BORROW         2 (status)
              FORMAT_SIMPLE
              LOAD_FAST_BORROW         9 (err_s)
              FORMAT_SIMPLE

245           BUILD_STRING            13

244           CALL                     1
              POP_TOP
              LOAD_CONST               8 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts\apply_memory_rollout_plan.py", line 250>:
250           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('result')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _exit_code at 0x0000018C180F4250, file "scripts\apply_memory_rollout_plan.py", line 250>:
250           RESUME                   0

251           LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('status')
              CALL                     1
              STORE_FAST               1 (status)

252           LOAD_FAST_BORROW         1 (status)
              LOAD_CONST               1 (('dry_run', 'applied'))
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

253           LOAD_SMALL_INT           0
              RETURN_VALUE

254   L1:     LOAD_SMALL_INT           1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts\apply_memory_rollout_plan.py", line 261>:
261           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17ED3D90, file "scripts\apply_memory_rollout_plan.py", line 261>:
 261            RESUME                   0

 262            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 263            NOP

 264    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 268    L2:     LOAD_FAST                2 (args)
                LOAD_ATTR               10 (plan)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L3:     LOAD_ATTR               13 (strip + NULL|self)
                CALL                     0
                STORE_FAST               4 (plan_path)

 269            LOAD_FAST                4 (plan_path)
                TO_BOOL
                POP_JUMP_IF_TRUE        30 (to L4)
                NOT_TAKEN

 270            LOAD_GLOBAL             15 (print + NULL)
                LOAD_CONST               3 ('error: --plan is required')
                LOAD_GLOBAL             16 (sys)
                LOAD_ATTR               18 (stderr)
                LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 271            LOAD_SMALL_INT           2
                RETURN_VALUE

 273    L4:     LOAD_FAST                2 (args)
                LOAD_ATTR               20 (operator_id)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L5:     LOAD_ATTR               13 (strip + NULL|self)
                CALL                     0
                STORE_FAST               5 (operator_id)

 274            LOAD_FAST                5 (operator_id)
                TO_BOOL
                POP_JUMP_IF_TRUE        30 (to L6)
                NOT_TAKEN

 275            LOAD_GLOBAL             15 (print + NULL)
                LOAD_CONST               5 ('error: --operator-id is required')
                LOAD_GLOBAL             16 (sys)
                LOAD_ATTR               18 (stderr)
                LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 276            LOAD_SMALL_INT           2
                RETURN_VALUE

 278    L6:     LOAD_GLOBAL             23 (_read_json + NULL)
                LOAD_FAST                4 (plan_path)
                LOAD_CONST               6 ('rollout plan')
                CALL                     2
                STORE_FAST               6 (raw)

 279            LOAD_FAST                6 (raw)
                POP_JUMP_IF_NOT_NONE    30 (to L7)
                NOT_TAKEN

 280            LOAD_GLOBAL             15 (print + NULL)

 281            LOAD_CONST               7 ('error: rollout plan could not be read; cannot build manifest')

 282            LOAD_GLOBAL             16 (sys)
                LOAD_ATTR               18 (stderr)

 280            LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 284            LOAD_SMALL_INT           2
                RETURN_VALUE

 286    L7:     LOAD_GLOBAL             25 (_unwrap_plan_envelope + NULL)
                LOAD_FAST                6 (raw)
                CALL                     1
                STORE_FAST               7 (plan)

 287            LOAD_FAST                7 (plan)
                POP_JUMP_IF_NOT_NONE    30 (to L8)
                NOT_TAKEN

 288            LOAD_GLOBAL             15 (print + NULL)

 289            LOAD_CONST               8 ('error: rollout plan JSON is not a recognised plan shape')

 290            LOAD_GLOBAL             16 (sys)
                LOAD_ATTR               18 (stderr)

 288            LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 292            LOAD_SMALL_INT           2
                RETURN_VALUE

 295    L8:     NOP

 296    L9:     LOAD_GLOBAL             26 (approval_mod)
                LOAD_ATTR               28 (build_approval_manifest)
                PUSH_NULL

 297            LOAD_FAST_LOAD_FAST    117 (plan, operator_id)
                LOAD_FAST                2 (args)
                LOAD_ATTR               30 (reason)

 296            LOAD_CONST               9 (('operator_id', 'reason'))
                CALL_KW                  3
                STORE_FAST               8 (manifest)

 309   L10:     LOAD_GLOBAL             39 (bool + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               40 (apply)
                CALL                     1
                STORE_FAST               9 (do_apply)

 310            LOAD_GLOBAL             26 (approval_mod)
                LOAD_ATTR               42 (apply_approved_rollout)
                PUSH_NULL

 311            LOAD_FAST_LOAD_FAST    137 (manifest, do_apply)
                TO_BOOL
                UNARY_NOT

 310            LOAD_CONST              11 (('dry_run',))
                CALL_KW                  2
                STORE_FAST              10 (result)

 314            LOAD_GLOBAL             45 (_safe + NULL)
                LOAD_FAST                8 (manifest)
                LOAD_GLOBAL             46 (_SAFE_MANIFEST_FIELDS)
                CALL                     2
                STORE_FAST              11 (safe_manifest)

 315            LOAD_GLOBAL             45 (_safe + NULL)
                LOAD_FAST               10 (result)
                LOAD_GLOBAL             48 (_SAFE_RESULT_FIELDS)
                CALL                     2
                STORE_FAST              12 (safe_result)

 318            LOAD_CONST              12 ('generated_at')
                LOAD_GLOBAL             50 (datetime)
                LOAD_ATTR               52 (now)
                PUSH_NULL
                LOAD_GLOBAL             54 (timezone)
                LOAD_ATTR               56 (utc)
                CALL                     1
                LOAD_ATTR               59 (isoformat + NULL|self)
                CALL                     0

 319            LOAD_CONST              13 ('mode')
                LOAD_FAST                9 (do_apply)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN
                LOAD_CONST              14 ('apply')
                JUMP_FORWARD             1 (to L12)
       L11:     LOAD_CONST              15 ('dry_run')

 320   L12:     LOAD_CONST              16 ('manifest')
                LOAD_FAST               11 (safe_manifest)

 321            LOAD_CONST              17 ('result')
                LOAD_FAST               12 (safe_result)

 317            BUILD_MAP                4
                STORE_FAST              13 (envelope)

 330            LOAD_FAST                2 (args)
                LOAD_ATTR               60 (record_ledger)
                TO_BOOL
                POP_JUMP_IF_FALSE       16 (to L13)
                NOT_TAKEN

 331            LOAD_GLOBAL             63 (_record_ledger_best_effort + NULL)
                LOAD_FAST_LOAD_FAST    138 (manifest, result)
                CALL                     2
                STORE_FAST              14 (ledger_status)

 332            LOAD_FAST_LOAD_FAST    237 (ledger_status, envelope)
                LOAD_CONST              18 ('ledger_status')
                STORE_SUBSCR

 334   L13:     LOAD_GLOBAL             65 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               66 (output)
                LOAD_FAST               13 (envelope)
                CALL                     2
                POP_TOP

 335            LOAD_GLOBAL             69 (_print_summary + NULL)
                LOAD_FAST_LOAD_FAST    197 (safe_result, operator_id)
                LOAD_CONST              19 (('operator_id',))
                CALL_KW                  2
                POP_TOP

 337            LOAD_FAST                2 (args)
                LOAD_ATTR               70 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L14)
                NOT_TAKEN

 338            LOAD_GLOBAL             15 (print + NULL)
                LOAD_GLOBAL             70 (json)
                LOAD_ATTR               72 (dumps)
                PUSH_NULL
                LOAD_FAST               13 (envelope)
                LOAD_SMALL_INT           2
                LOAD_CONST              20 (True)
                LOAD_CONST              21 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 340   L14:     LOAD_GLOBAL             75 (_exit_code + NULL)
                LOAD_FAST               12 (safe_result)
                CALL                     1
                RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 265            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L24)
                NOT_TAKEN
                STORE_FAST               3 (e)

 266   L16:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST              22 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L17)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L21)
       L17:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L20)
       L18:     NOT_TAKEN
       L19:     POP_TOP
                LOAD_SMALL_INT           0
       L20:     CALL                     1
       L21:     SWAP                     2
       L22:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L23:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 265   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L26:     PUSH_EXC_INFO

 299            LOAD_GLOBAL             32 (ValueError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L30)
                NOT_TAKEN
                STORE_FAST               3 (e)

 302   L27:     LOAD_GLOBAL             15 (print + NULL)

 303            LOAD_CONST              10 ('error: manifest build rejected: ')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 304            LOAD_GLOBAL             16 (sys)
                LOAD_ATTR               18 (stderr)

 302            LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 306   L28:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                LOAD_SMALL_INT           2
                RETURN_VALUE

  --   L29:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 299   L30:     RERAISE                  0

  --   L31:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L15 [0]
  L9 to L10 -> L26 [0]
  L15 to L16 -> L25 [1] lasti
  L16 to L18 -> L23 [1] lasti
  L19 to L21 -> L23 [1] lasti
  L21 to L22 -> L25 [1] lasti
  L23 to L25 -> L25 [1] lasti
  L26 to L27 -> L31 [1] lasti
  L27 to L28 -> L29 [1] lasti
  L29 to L31 -> L31 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "scripts\apply_memory_rollout_plan.py", line 343>:
343           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('manifest')

344           LOAD_CONST               2 ('Dict[str, Any]')

343           LOAD_CONST               3 ('result')

345           LOAD_CONST               2 ('Dict[str, Any]')

343           LOAD_CONST               4 ('return')

346           LOAD_CONST               2 ('Dict[str, Any]')

343           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _record_ledger_best_effort at 0x0000018C17D8C5C0, file "scripts\apply_memory_rollout_plan.py", line 343>:
 343            RESUME                   0

 350            NOP

 351    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('rollout_ledger',))
                IMPORT_NAME              0 (app.services.memory)
                IMPORT_FROM              1 (rollout_ledger)
                STORE_FAST               2 (ledger_mod)
                POP_TOP

 356    L2:     NOP

 357    L3:     LOAD_FAST                2 (ledger_mod)
                LOAD_ATTR               11 (record_rollout_ledger + NULL|self)

 358            LOAD_CONST               7 ('manifest')
                LOAD_FAST                0 (manifest)
                LOAD_CONST               8 ('result')
                LOAD_FAST                1 (result)
                BUILD_MAP                2

 357            CALL                     1
                STORE_FAST               4 (outcome)

 367    L4:     LOAD_CONST               2 ('status')
                LOAD_FAST                4 (outcome)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1

 368            LOAD_CONST               4 ('reason')
                LOAD_FAST                4 (outcome)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               4 ('reason')
                CALL                     1

 369            LOAD_CONST              11 ('errors')
                LOAD_FAST                4 (outcome)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              11 ('errors')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0

 366    L5:     BUILD_MAP                3
                RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 352            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       39 (to L11)
                NOT_TAKEN
                STORE_FAST               3 (e)

 353    L7:     LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('skipped')

 354            LOAD_CONST               4 ('reason')
                LOAD_CONST               5 ('import_failed:')
                LOAD_GLOBAL              7 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR                8 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 353            BUILD_MAP                2
        L8:     SWAP                     2
        L9:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L10:     LOAD_CONST               6 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 352   L11:     RERAISE                  0

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L13:     PUSH_EXC_INFO

 360            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       39 (to L18)
                NOT_TAKEN
                STORE_FAST               3 (e)

 361   L14:     LOAD_CONST               2 ('status')
                LOAD_CONST               9 ('failed')

 362            LOAD_CONST               4 ('reason')
                LOAD_CONST              10 ('unhandled_exception:')
                LOAD_GLOBAL              7 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR                8 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 361            BUILD_MAP                2
       L15:     SWAP                     2
       L16:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L17:     LOAD_CONST               6 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 360   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L6 [0]
  L3 to L4 -> L13 [0]
  L6 to L7 -> L12 [1] lasti
  L7 to L8 -> L10 [1] lasti
  L8 to L9 -> L12 [1] lasti
  L10 to L12 -> L12 [1] lasti
  L13 to L14 -> L19 [1] lasti
  L14 to L15 -> L17 [1] lasti
  L15 to L16 -> L19 [1] lasti
  L17 to L19 -> L19 [1] lasti
```
