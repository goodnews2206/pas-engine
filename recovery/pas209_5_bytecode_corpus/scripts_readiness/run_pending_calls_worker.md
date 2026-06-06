# scripts_readiness/run_pending_calls_worker

- **pyc:** `scripts\__pycache__\run_pending_calls_worker.cpython-314.pyc`
- **expected source path (absent):** `scripts/run_pending_calls_worker.py`
- **co_filename (from bytecode):** `scripts\run_pending_calls_worker.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS162 — Pending-call worker CLI.

Operator-run trigger for ``app/services/ingestion/worker.py``.
Strictly opt-in: the worker is **off by default**, even when
this CLI is invoked. The runtime enable form is the env
variable ``PENDING_CALLS_WORKER_ENABLED=true`` (exact string).

Usage:
  python scripts/run_pending_calls_worker.py --once
  python scripts/run_pending_calls_worker.py --once --limit 10
  python scripts/run_pending_calls_worker.py --dry-run
  python scripts/run_pending_calls_worker.py --once --json
  python scripts/run_pending_calls_worker.py --once \
      --worker-id ops-alice

Flags:
  --once         Drain at most ``--limit`` due rows and exit.
                 PAS162 does not support continuous loops; the
                 default mode for the CLI IS ``--once``.
  --limit N      Cap on the number of rows processed (default 25;
                 clamped to 200 by the service layer).
  --worker-id S  Optional human-meaningful tag stored as
                 ``locked_by`` on each row.
  --json         Emit the full result JSON on stdout.
  --dry-run      List due rows without dialing or mutating any
                 row. Bypasses the enable flag for inspection.
                 Phone / email / name are NEVER printed.

Exit codes:
  0  — status ``ok`` / ``disabled`` / nothing due
  1  — status ``failed`` / status ``warning`` (with adapter
       missing or other actionable failures)
  2  — bad CLI arguments

This script never:
  * reads .env,
  * calls Supabase directly (it only invokes the worker module,
    which uses the existing project Supabase helper),
  * imports external vendor libraries,
  * imports embedding / vector libraries,
  * prints raw phone / email / name (the worker module already
    enforces this; the CLI is belt-and-braces here).
```

## Imports

`List`, `Optional`, `__future__`, `annotations`, `app.services.ingestion.worker`, `argparse`, `dry_run_pending_calls`, `json`, `os`, `pending_calls_worker_enabled`, `run_pending_calls_once`, `sys`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_print_dry_run`, `_print_summary`, `main`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS162 — Pending-call worker CLI.\n\nOperator-run trigger for ``app/services/ingestion/worker.py``.\nStrictly opt-in: the worker is **off by default**, even when\nthis CLI is invoked. The runtime enable form is the env\nvariable ``PENDING_CALLS_WORKER_ENABLED=true`` (exact string).\n\nUsage:\n  python scripts/run_pending_calls_worker.py --once\n  python scripts/run_pending_calls_worker.py --once --limit 10\n  python scripts/run_pending_calls_worker.py --dry-run\n  python scripts/run_pending_calls_worker.py --once --json\n  python scripts/run_pending_calls_worker.py --once \\\n      --worker-id ops-alice\n\nFlags:\n  --once         Drain at most ``--limit`` due rows and exit.\n                 PAS162 does not support continuous loops; the\n                 default mode for the CLI IS ``--once``.\n  --limit N      Cap on the number of rows processed (default 25;\n                 clamped to 200 by the service layer).\n  --worker-id S  Optional human-meaningful tag stored as\n                 ``locked_by`` on each row.\n  --json         Emit the full result JSON on stdout.\n  --dry-run      List due rows without dialing or mutating any\n                 row. Bypasses the enable flag for inspection.\n                 Phone / email / name are NEVER printed.\n\nExit codes:\n  0  — status ``ok`` / ``disabled`` / nothing due\n  1  — status ``failed`` / status ``warning`` (with adapter\n       missing or other actionable failures)\n  2  — bad CLI arguments\n\nThis script never:\n  * reads .env,\n  * calls Supabase directly (it only invokes the worker module,\n    which uses the existing project Supabase helper),\n  * imports external vendor libraries,\n  * imports embedding / vector libraries,\n  * prints raw phone / email / name (the worker module already\n    enforces this; the CLI is belt-and-braces here).\n'
- 'utf-8'
- 'return'
- 'argparse.ArgumentParser'
- 'run_pending_calls_worker'
- 'PAS162 — Operator-run pending-call worker. Drains due rows from pas_pending_calls and dials via the existing outbound adapter. OFF by default.'
- '--once'
- 'store_true'
- 'Drain at most --limit due rows and exit. PAS162 does NOT support continuous loops; this flag is kept for explicit operator intent.'
- '--limit'
- 'Maximum rows to consider in one drain (default 25).'
- '--worker-id'
- 'Optional human-readable tag stored as locked_by.'
- '--json'
- 'Emit the full result JSON on stdout.'
- '--dry-run'
- 'List due rows WITHOUT dialing or mutating any row. Bypasses the enable flag for inspection. Phone / email / name are never printed.'
- 'payload'
- 'dict'
- 'None'
- 'status'
- 'checked'
- 'dialed'
- 'failed'
- 'warnings'
- '[PAS162-worker] status='
- ' checked='
- ' dialed='
- ' failed='
- ' warning_count='
- '  - warning: '
- '  ... and '
- ' more'
- 'CLI dry-run output. PII-safe by construction: the\nunderlying ``dry_run_pending_calls`` summary already omits\nphone / email / name.'
- 'results'
- '[PAS162-worker DRY RUN] status='
- ' due_rows='
- 'pending_call_id'
- 'source'
- 'attempt'
- 'max_attempts'
- 'next_attempt_at'
- '  - pending_call_id='
- ' source='
- ' attempt='
- ' due_at='
- 'argv'
- 'Optional[List[str]]'
- 'int'
- 'error: cannot import worker module: '
- 'error: --once is required (PAS162 does not support continuous loops; use cron / systemd timer for scheduling).'
- 'disabled'
- 'worker_disabled_by_flag'

## Disassembly

```
   0            RESUME                   0

   1            LOAD_CONST               0 ('\nPAS162 — Pending-call worker CLI.\n\nOperator-run trigger for ``app/services/ingestion/worker.py``.\nStrictly opt-in: the worker is **off by default**, even when\nthis CLI is invoked. The runtime enable form is the env\nvariable ``PENDING_CALLS_WORKER_ENABLED=true`` (exact string).\n\nUsage:\n  python scripts/run_pending_calls_worker.py --once\n  python scripts/run_pending_calls_worker.py --once --limit 10\n  python scripts/run_pending_calls_worker.py --dry-run\n  python scripts/run_pending_calls_worker.py --once --json\n  python scripts/run_pending_calls_worker.py --once \\\n      --worker-id ops-alice\n\nFlags:\n  --once         Drain at most ``--limit`` due rows and exit.\n                 PAS162 does not support continuous loops; the\n                 default mode for the CLI IS ``--once``.\n  --limit N      Cap on the number of rows processed (default 25;\n                 clamped to 200 by the service layer).\n  --worker-id S  Optional human-meaningful tag stored as\n                 ``locked_by`` on each row.\n  --json         Emit the full result JSON on stdout.\n  --dry-run      List due rows without dialing or mutating any\n                 row. Bypasses the enable flag for inspection.\n                 Phone / email / name are NEVER printed.\n\nExit codes:\n  0  — status ``ok`` / ``disabled`` / nothing due\n  1  — status ``failed`` / status ``warning`` (with adapter\n       missing or other actionable failures)\n  2  — bad CLI arguments\n\nThis script never:\n  * reads .env,\n  * calls Supabase directly (it only invokes the worker module,\n    which uses the existing project Supabase helper),\n  * imports external vendor libraries,\n  * imports embedding / vector libraries,\n  * prints raw phone / email / name (the worker module already\n    enforces this; the CLI is belt-and-braces here).\n')
                STORE_NAME               0 (__doc__)

  46            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('annotations',))
                IMPORT_NAME              1 (__future__)
                IMPORT_FROM              2 (annotations)
                STORE_NAME               2 (annotations)
                POP_TOP

  48            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              3 (argparse)
                STORE_NAME               3 (argparse)

  49            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              4 (json)
                STORE_NAME               4 (json)

  50            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              5 (os)
                STORE_NAME               5 (os)

  51            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              6 (sys)
                STORE_NAME               6 (sys)

  52            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('List', 'Optional'))
                IMPORT_NAME              7 (typing)
                IMPORT_FROM              8 (List)
                STORE_NAME               8 (List)
                IMPORT_FROM              9 (Optional)
                STORE_NAME               9 (Optional)
                POP_TOP

  57            LOAD_NAME                6 (sys)
                LOAD_ATTR               20 (stdout)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               22 (stderr)
                BUILD_TUPLE              2
                GET_ITER
        L1:     FOR_ITER                22 (to L4)
                STORE_NAME              12 (_stream)

  58            NOP

  59    L2:     LOAD_NAME               12 (_stream)
                LOAD_ATTR               27 (reconfigure + NULL|self)
                LOAD_CONST               4 ('utf-8')
                LOAD_CONST               5 (('encoding',))
                CALL_KW                  1
                POP_TOP
        L3:     JUMP_BACKWARD           24 (to L1)

  57    L4:     END_FOR
                POP_ITER

  66            LOAD_NAME                5 (os)
                LOAD_ATTR               30 (path)
                LOAD_ATTR               33 (abspath + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               30 (path)
                LOAD_ATTR               35 (join + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               30 (path)
                LOAD_ATTR               37 (dirname + NULL|self)
                LOAD_NAME               19 (__file__)
                CALL                     1
                LOAD_CONST               6 ('..')
                CALL                     2
                CALL                     1
                STORE_NAME              20 (_REPO_ROOT)

  67            LOAD_NAME               20 (_REPO_ROOT)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               30 (path)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       29 (to L5)
                NOT_TAKEN

  68            LOAD_NAME                6 (sys)
                LOAD_ATTR               30 (path)
                LOAD_ATTR               43 (insert + NULL|self)
                LOAD_SMALL_INT           0
                LOAD_NAME               20 (_REPO_ROOT)
                CALL                     2
                POP_TOP

  71    L5:     LOAD_CONST               7 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts\run_pending_calls_worker.py", line 71>)
                MAKE_FUNCTION
                LOAD_CONST               8 (<code object _build_parser at 0x0000018C179A7290, file "scripts\run_pending_calls_worker.py", line 71>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              22 (_build_parser)

 111            LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts\run_pending_calls_worker.py", line 111>)
                MAKE_FUNCTION
                LOAD_CONST              10 (<code object _print_summary at 0x0000018C17ED9100, file "scripts\run_pending_calls_worker.py", line 111>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              23 (_print_summary)

 130            LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts\run_pending_calls_worker.py", line 130>)
                MAKE_FUNCTION
                LOAD_CONST              12 (<code object _print_dry_run at 0x0000018C17E7E240, file "scripts\run_pending_calls_worker.py", line 130>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              24 (_print_dry_run)

 156            LOAD_CONST              16 ((None,))
                LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts\run_pending_calls_worker.py", line 156>)
                MAKE_FUNCTION
                LOAD_CONST              14 (<code object main at 0x0000018C177B0120, file "scripts\run_pending_calls_worker.py", line 156>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              25 (main)

 238            LOAD_NAME               26 (__name__)
                LOAD_CONST              15 ('__main__')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       26 (to L6)
                NOT_TAKEN

 239            LOAD_NAME                6 (sys)
                LOAD_ATTR               54 (exit)
                PUSH_NULL
                LOAD_NAME               25 (main)
                PUSH_NULL
                CALL                     0
                CALL                     1
                POP_TOP
                LOAD_CONST               2 (None)
                RETURN_VALUE

 238    L6:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  60            LOAD_NAME               14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

  61    L8:     POP_EXCEPT
                JUMP_BACKWARD          219 (to L1)

  60    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L7 [1]
  L7 to L8 -> L10 [2] lasti
  L9 to L10 -> L10 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts\run_pending_calls_worker.py", line 71>:
 71           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C179A7290, file "scripts\run_pending_calls_worker.py", line 71>:
 71           RESUME                   0

 72           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

 73           LOAD_CONST               0 ('run_pending_calls_worker')

 75           LOAD_CONST               1 ('PAS162 — Operator-run pending-call worker. Drains due rows from pas_pending_calls and dials via the existing outbound adapter. OFF by default.')

 72           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

 80           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

 81           LOAD_CONST               3 ('--once')
              LOAD_CONST               4 ('store_true')

 83           LOAD_CONST               5 ('Drain at most --limit due rows and exit. PAS162 does NOT support continuous loops; this flag is kept for explicit operator intent.')

 80           LOAD_CONST               6 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

 88           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

 89           LOAD_CONST               7 ('--limit')
              LOAD_GLOBAL              6 (int)
              LOAD_SMALL_INT          25

 90           LOAD_CONST               8 ('Maximum rows to consider in one drain (default 25).')

 88           LOAD_CONST               9 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

 92           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

 93           LOAD_CONST              10 ('--worker-id')
              LOAD_GLOBAL              8 (str)
              LOAD_CONST              11 (None)

 94           LOAD_CONST              12 ('Optional human-readable tag stored as locked_by.')

 92           LOAD_CONST               9 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

 96           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

 97           LOAD_CONST              13 ('--json')
              LOAD_CONST               4 ('store_true')

 98           LOAD_CONST              14 ('Emit the full result JSON on stdout.')

 96           LOAD_CONST               6 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

100           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

101           LOAD_CONST              15 ('--dry-run')
              LOAD_CONST               4 ('store_true')

103           LOAD_CONST              16 ('List due rows WITHOUT dialing or mutating any row. Bypasses the enable flag for inspection. Phone / email / name are never printed.')

100           LOAD_CONST               6 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

108           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts\run_pending_calls_worker.py", line 111>:
111           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('payload')
              LOAD_CONST               2 ('dict')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _print_summary at 0x0000018C17ED9100, file "scripts\run_pending_calls_worker.py", line 111>:
111           RESUME                   0

112           LOAD_FAST_BORROW         0 (payload)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('status')
              CALL                     1
              STORE_FAST               1 (status)

113           LOAD_FAST_BORROW         0 (payload)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('checked')
              LOAD_SMALL_INT           0
              CALL                     2
              STORE_FAST               2 (checked)

114           LOAD_FAST_BORROW         0 (payload)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               2 ('dialed')
              LOAD_SMALL_INT           0
              CALL                     2
              STORE_FAST               3 (dialed)

115           LOAD_FAST_BORROW         0 (payload)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('failed')
              LOAD_SMALL_INT           0
              CALL                     2
              STORE_FAST               4 (failed)

116           LOAD_FAST_BORROW         0 (payload)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               4 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     STORE_FAST               5 (warnings)

117           LOAD_GLOBAL              3 (print + NULL)

118           LOAD_CONST               5 ('[PAS162-worker] status=')
              LOAD_FAST_BORROW         1 (status)
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checked=')

119           LOAD_FAST_BORROW         2 (checked)
              FORMAT_SIMPLE
              LOAD_CONST               7 (' dialed=')
              LOAD_FAST_BORROW         3 (dialed)
              FORMAT_SIMPLE
              LOAD_CONST               8 (' failed=')
              LOAD_FAST_BORROW         4 (failed)
              FORMAT_SIMPLE
              LOAD_CONST               9 (' warning_count=')

120           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         5 (warnings)
              CALL                     1
              FORMAT_SIMPLE

118           BUILD_STRING            10

117           CALL                     1
              POP_TOP

122           LOAD_FAST_BORROW         5 (warnings)
              TO_BOOL
              POP_JUMP_IF_FALSE       82 (to L5)
              NOT_TAKEN

124           LOAD_FAST_BORROW         5 (warnings)
              LOAD_CONST              10 (slice(None, 10, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               6 (w)

125           LOAD_GLOBAL              3 (print + NULL)
              LOAD_CONST              11 ('  - warning: ')
              LOAD_FAST_BORROW         6 (w)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

124   L3:     END_FOR
              POP_ITER

126           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         5 (warnings)
              CALL                     1
              LOAD_SMALL_INT          10
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

127           LOAD_GLOBAL              3 (print + NULL)
              LOAD_CONST              12 ('  ... and ')
              LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         5 (warnings)
              CALL                     1
              LOAD_SMALL_INT          10
              BINARY_OP               10 (-)
              FORMAT_SIMPLE
              LOAD_CONST              13 (' more')
              BUILD_STRING             3
              CALL                     1
              POP_TOP
              LOAD_CONST              14 (None)
              RETURN_VALUE

126   L4:     LOAD_CONST              14 (None)
              RETURN_VALUE

122   L5:     LOAD_CONST              14 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts\run_pending_calls_worker.py", line 130>:
130           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('payload')
              LOAD_CONST               2 ('dict')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _print_dry_run at 0x0000018C17E7E240, file "scripts\run_pending_calls_worker.py", line 130>:
130           RESUME                   0

134           LOAD_FAST_BORROW         0 (payload)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('status')
              CALL                     1
              STORE_FAST               1 (status)

135           LOAD_FAST_BORROW         0 (payload)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               2 ('checked')
              LOAD_SMALL_INT           0
              CALL                     2
              STORE_FAST               2 (checked)

136           LOAD_FAST_BORROW         0 (payload)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('results')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     STORE_FAST               3 (rows)

137           LOAD_GLOBAL              3 (print + NULL)

138           LOAD_CONST               4 ('[PAS162-worker DRY RUN] status=')
              LOAD_FAST_BORROW         1 (status)
              FORMAT_SIMPLE
              LOAD_CONST               5 (' due_rows=')
              LOAD_FAST_BORROW         2 (checked)
              FORMAT_SIMPLE
              BUILD_STRING             4

137           CALL                     1
              POP_TOP

140           LOAD_FAST_BORROW         3 (rows)
              LOAD_CONST               6 (slice(None, 50, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER               114 (to L3)
              STORE_FAST               4 (row)

143           LOAD_FAST_BORROW         4 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               7 ('pending_call_id')
              CALL                     1
              STORE_FAST               5 (pcid)

144           LOAD_FAST_BORROW         4 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               8 ('source')
              CALL                     1
              STORE_FAST               6 (source)

145           LOAD_FAST_BORROW         4 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               9 ('attempt')
              CALL                     1
              STORE_FAST               7 (att)

146           LOAD_FAST_BORROW         4 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              10 ('max_attempts')
              CALL                     1
              STORE_FAST               8 (maxatt)

147           LOAD_FAST_BORROW         4 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              11 ('next_attempt_at')
              CALL                     1
              STORE_FAST               9 (nextat)

148           LOAD_GLOBAL              3 (print + NULL)

149           LOAD_CONST              12 ('  - pending_call_id=')
              LOAD_FAST_BORROW         5 (pcid)
              FORMAT_SIMPLE
              LOAD_CONST              13 (' source=')
              LOAD_FAST_BORROW         6 (source)
              FORMAT_SIMPLE
              LOAD_CONST              14 (' attempt=')

150           LOAD_FAST_BORROW         7 (att)
              FORMAT_SIMPLE
              LOAD_CONST              15 ('/')
              LOAD_FAST_BORROW         8 (maxatt)
              FORMAT_SIMPLE
              LOAD_CONST              16 (' due_at=')
              LOAD_FAST_BORROW         9 (nextat)
              FORMAT_SIMPLE

149           BUILD_STRING            10

148           CALL                     1
              POP_TOP
              JUMP_BACKWARD          116 (to L2)

140   L3:     END_FOR
              POP_ITER

152           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         3 (rows)
              CALL                     1
              LOAD_SMALL_INT          50
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

153           LOAD_GLOBAL              3 (print + NULL)
              LOAD_CONST              17 ('  ... and ')
              LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         3 (rows)
              CALL                     1
              LOAD_SMALL_INT          50
              BINARY_OP               10 (-)
              FORMAT_SIMPLE
              LOAD_CONST              18 (' more')
              BUILD_STRING             3
              CALL                     1
              POP_TOP
              LOAD_CONST              19 (None)
              RETURN_VALUE

152   L4:     LOAD_CONST              19 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts\run_pending_calls_worker.py", line 156>:
156           RESUME                   0
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

Disassembly of <code object main at 0x0000018C177B0120, file "scripts\run_pending_calls_worker.py", line 156>:
 156            RESUME                   0

 157            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 158            NOP

 159    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 166    L2:     NOP

 167    L3:     LOAD_SMALL_INT           0
                LOAD_CONST               2 (('dry_run_pending_calls', 'pending_calls_worker_enabled', 'run_pending_calls_once'))
                IMPORT_NAME              5 (app.services.ingestion.worker)
                IMPORT_FROM              6 (dry_run_pending_calls)
                STORE_FAST               4 (dry_run_pending_calls)
                IMPORT_FROM              7 (pending_calls_worker_enabled)
                STORE_FAST               5 (pending_calls_worker_enabled)
                IMPORT_FROM              8 (run_pending_calls_once)
                STORE_FAST               6 (run_pending_calls_once)
                POP_TOP

 181    L4:     LOAD_FAST                2 (args)
                LOAD_ATTR               30 (dry_run)
                TO_BOOL
                POP_JUMP_IF_FALSE      120 (to L7)
                NOT_TAKEN

 182            LOAD_FAST                4 (dry_run_pending_calls)
                PUSH_NULL

 183            LOAD_FAST                2 (args)
                LOAD_ATTR               32 (limit)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (worker_id)

 182            LOAD_CONST               5 (('limit', 'worker_id'))
                CALL_KW                  2
                STORE_FAST               7 (payload)

 185            LOAD_GLOBAL             37 (_print_dry_run + NULL)
                LOAD_FAST                7 (payload)
                CALL                     1
                POP_TOP

 186            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L5)
                NOT_TAKEN

 187            LOAD_GLOBAL             21 (print + NULL)
                LOAD_GLOBAL             38 (json)
                LOAD_ATTR               40 (dumps)
                PUSH_NULL
                LOAD_FAST                7 (payload)
                LOAD_SMALL_INT           2
                LOAD_CONST               6 (True)
                LOAD_CONST               7 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 190    L5:     LOAD_FAST                7 (payload)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST               8 ('status')
                CALL                     1
                LOAD_CONST               9 ('failed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_SMALL_INT           1
                RETURN_VALUE
        L6:     LOAD_SMALL_INT           0
                RETURN_VALUE

 195    L7:     LOAD_FAST                2 (args)
                LOAD_ATTR               44 (once)
                TO_BOOL
                POP_JUMP_IF_TRUE        30 (to L8)
                NOT_TAKEN

 196            LOAD_GLOBAL             21 (print + NULL)

 197            LOAD_CONST              10 ('error: --once is required (PAS162 does not support continuous loops; use cron / systemd timer for scheduling).')

 200            LOAD_GLOBAL             26 (sys)
                LOAD_ATTR               28 (stderr)

 196            LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 202            LOAD_SMALL_INT           2
                RETURN_VALUE

 205    L8:     LOAD_FAST                5 (pending_calls_worker_enabled)
                PUSH_NULL
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        81 (to L10)
                NOT_TAKEN

 211            LOAD_CONST               8 ('status')
                LOAD_CONST              11 ('disabled')

 212            LOAD_CONST              12 ('checked')
                LOAD_SMALL_INT           0

 213            LOAD_CONST              13 ('dialed')
                LOAD_SMALL_INT           0

 214            LOAD_CONST               9 ('failed')
                LOAD_SMALL_INT           0

 215            LOAD_CONST              14 ('results')
                BUILD_LIST               0

 216            LOAD_CONST              15 ('warnings')
                LOAD_CONST              16 ('worker_disabled_by_flag')
                BUILD_LIST               1

 210            BUILD_MAP                6
                STORE_FAST               7 (payload)

 218            LOAD_GLOBAL             47 (_print_summary + NULL)
                LOAD_FAST                7 (payload)
                CALL                     1
                POP_TOP

 219            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L9)
                NOT_TAKEN

 220            LOAD_GLOBAL             21 (print + NULL)
                LOAD_GLOBAL             38 (json)
                LOAD_ATTR               40 (dumps)
                PUSH_NULL
                LOAD_FAST                7 (payload)
                LOAD_SMALL_INT           2
                LOAD_CONST               6 (True)
                LOAD_CONST               7 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 221    L9:     LOAD_SMALL_INT           0
                RETURN_VALUE

 223   L10:     LOAD_FAST                6 (run_pending_calls_once)
                PUSH_NULL

 224            LOAD_FAST                2 (args)
                LOAD_ATTR               32 (limit)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (worker_id)

 223            LOAD_CONST               5 (('limit', 'worker_id'))
                CALL_KW                  2
                STORE_FAST               7 (payload)

 226            LOAD_GLOBAL             47 (_print_summary + NULL)
                LOAD_FAST                7 (payload)
                CALL                     1
                POP_TOP

 227            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L11)
                NOT_TAKEN

 228            LOAD_GLOBAL             21 (print + NULL)
                LOAD_GLOBAL             38 (json)
                LOAD_ATTR               40 (dumps)
                PUSH_NULL
                LOAD_FAST                7 (payload)
                LOAD_SMALL_INT           2
                LOAD_CONST               6 (True)
                LOAD_CONST               7 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 230   L11:     LOAD_FAST                7 (payload)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST               8 ('status')
                CALL                     1
                STORE_FAST               8 (status)

 231            LOAD_FAST                8 (status)
                LOAD_CONST              18 (('ok', 'disabled'))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN

 232            LOAD_SMALL_INT           0
                RETURN_VALUE

 235   L12:     LOAD_SMALL_INT           1
                RETURN_VALUE

  --   L13:     PUSH_EXC_INFO

 160            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L22)
                NOT_TAKEN
                STORE_FAST               3 (e)

 161   L14:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST              17 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L19)
       L15:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
       L16:     NOT_TAKEN
       L17:     POP_TOP
                LOAD_SMALL_INT           0
       L18:     CALL                     1
       L19:     SWAP                     2
       L20:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L21:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 160   L22:     RERAISE                  0

  --   L23:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L24:     PUSH_EXC_INFO

 172            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L28)
                NOT_TAKEN
                STORE_FAST               3 (e)

 173   L25:     LOAD_GLOBAL             21 (print + NULL)

 174            LOAD_CONST               3 ('error: cannot import worker module: ')

 175            LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE

 174            BUILD_STRING             2

 176            LOAD_GLOBAL             26 (sys)
                LOAD_ATTR               28 (stderr)

 173            LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 178   L26:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                LOAD_SMALL_INT           2
                RETURN_VALUE

  --   L27:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 172   L28:     RERAISE                  0

  --   L29:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L13 [0]
  L3 to L4 -> L24 [0]
  L13 to L14 -> L23 [1] lasti
  L14 to L16 -> L21 [1] lasti
  L17 to L19 -> L21 [1] lasti
  L19 to L20 -> L23 [1] lasti
  L21 to L23 -> L23 [1] lasti
  L24 to L25 -> L29 [1] lasti
  L25 to L26 -> L27 [1] lasti
  L27 to L29 -> L29 [1] lasti
```
