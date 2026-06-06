# scripts_readiness/reap_callback_schedule

- **pyc:** `scripts\__pycache__\reap_callback_schedule.cpython-314.pyc`
- **expected source path (absent):** `scripts/reap_callback_schedule.py`
- **co_filename (from bytecode):** `scripts/reap_callback_schedule.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS172 — Operator reaper for the PAS171 callback schedule
durable store (``pas_callback_schedule``).

Closes the PAS171 §13 "promote operator-side reapers" item.
Terminal callback rows (``completed``, ``cancelled``,
``overdue``, ``failed``) accumulate forever unless an operator
removes them; this script IS that operator action.

Doctrine:

* **Dry-run by default.** ``--execute`` is required to delete.
* **Terminal-status only.** This reaper NEVER touches
  ``pending`` or ``reminded`` rows. Even if their
  ``scheduled_for`` is far in the past, only the
  ``mark_callback_overdue`` lifecycle helper may transition
  them out of pending — the reaper does NOT shortcut that.
* **Bounded delete count.** ``--limit`` caps rows removed
  per run (default 1000, hard cap 5000).
* **Age clamp.** ``--older-than-hours`` defaults to 168 (7
  days) and is clamped to ``[24, 24*30]``. Operator wants
  enough retention to investigate a recent incident before
  rows disappear.
* **Structural envelopes only.** NEVER echoes
  source_call_id contents, completed_by names, last_error_code
  strings, or any raw lead context. The script only emits
  counts.
* **DB unavailable → exit 0 with skipped envelope.**
* **No scheduler / cron added.** PAS172 does NOT automate
  execution.
* **NEVER raises.**

Usage:

    # Dry-run; print what *would* be reaped.
    python scripts/reap_callback_schedule.py

    # Reap rows older than 7 days, per-brokerage.
    python scripts/reap_callback_schedule.py \
        --brokerage-id brk-pilot --older-than-hours 168 \
        --limit 500 --execute

    # Restrict to a specific terminal status.
    python scripts/reap_callback_schedule.py \
        --status completed --older-than-hours 168 --execute

Exit codes:
    0  — completed successfully (including dry-run + skipped)
    2  — bad CLI arguments
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `argparse`, `datetime`, `get_supabase`, `json`, `logging`, `os`, `sys`, `timedelta`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_clamp`, `_get_db_safe`, `_now_iso`, `_print_summary`, `_safe_envelope`, `main`, `reap`

## Env-key candidates

`PAS172`

## String constants (redacted where noted)

- '\nPAS172 — Operator reaper for the PAS171 callback schedule\ndurable store (``pas_callback_schedule``).\n\nCloses the PAS171 §13 "promote operator-side reapers" item.\nTerminal callback rows (``completed``, ``cancelled``,\n``overdue``, ``failed``) accumulate forever unless an operator\nremoves them; this script IS that operator action.\n\nDoctrine:\n\n* **Dry-run by default.** ``--execute`` is required to delete.\n* **Terminal-status only.** This reaper NEVER touches\n  ``pending`` or ``reminded`` rows. Even if their\n  ``scheduled_for`` is far in the past, only the\n  ``mark_callback_overdue`` lifecycle helper may transition\n  them out of pending — the reaper does NOT shortcut that.\n* **Bounded delete count.** ``--limit`` caps rows removed\n  per run (default 1000, hard cap 5000).\n* **Age clamp.** ``--older-than-hours`` defaults to 168 (7\n  days) and is clamped to ``[24, 24*30]``. Operator wants\n  enough retention to investigate a recent incident before\n  rows disappear.\n* **Structural envelopes only.** NEVER echoes\n  source_call_id contents, completed_by names, last_error_code\n  strings, or any raw lead context. The script only emits\n  counts.\n* **DB unavailable → exit 0 with skipped envelope.**\n* **No scheduler / cron added.** PAS172 does NOT automate\n  execution.\n* **NEVER raises.**\n\nUsage:\n\n    # Dry-run; print what *would* be reaped.\n    python scripts/reap_callback_schedule.py\n\n    # Reap rows older than 7 days, per-brokerage.\n    python scripts/reap_callback_schedule.py \\\n        --brokerage-id brk-pilot --older-than-hours 168 \\\n        --limit 500 --execute\n\n    # Restrict to a specific terminal status.\n    python scripts/reap_callback_schedule.py \\\n        --status completed --older-than-hours 168 --execute\n\nExit codes:\n    0  — completed successfully (including dry-run + skipped)\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'pas.scripts.reap_callback_schedule'
- 'pas_callback_schedule'
- 'candidate_count'
- 'deleted_count'
- 'skipped_count'
- 'failed_count'
- 'warnings'
- 'error_code'
- 'brokerage_id'
- 'filter_status'
- 'older_than_hours'
- 'limit'
- 'dry_run'
- 'now'
- 'return'
- 'str'
- 'seconds'
- 'reap_callback_schedule db client unavailable type='
- 'value'
- 'Any'
- 'int'
- 'default'
- 'status'
- 'bool'
- 'Optional[str]'
- 'Optional[List[str]]'
- 'Dict[str, Any]'
- 'phase'
- 'PAS172'
- 'reaper'
- 'callback_schedule'
- 'generated_at'
- 'Optional[datetime]'
- 'Reap terminal callback rows. Always returns a structural\nenvelope. NEVER raises.'
- 'failed'
- 'invalid_filter_status'
- 'skipped'
- 'durable_callback_schedule_unavailable'
- 'callback_id, brokerage_id, status, updated_at'
- 'updated_at'
- 'data'
- 'reap_callback_schedule read error type='
- 'db_read_failed:'
- 'callback_id'
- 'db_delete_failed:'
- 'reap_callback_schedule delete error type='
- 'partial_failure'
- 'reaper_partial_failure'
- 'argparse.ArgumentParser'
- 'reap_callback_schedule'
- 'PAS172 — Reap terminal callback rows from the PAS171 durable store. Dry-run by default; --execute required to delete. NEVER touches pending / reminded rows. NEVER echoes raw lead context.'
- '--brokerage-id'
- 'Scope the reap to a single brokerage (default: all).'
- '--status'
- 'Restrict to one terminal status (default: all terminal statuses).'
- '--older-than-hours'
- 'Reap rows whose updated_at is older than this many hours (clamped to ['
- '], default '
- '--limit'
- 'Hard cap on rows deleted per run (default '
- ', max '
- '--execute'
- 'store_true'
- 'Actually delete rows. Without this flag the script runs in dry-run mode.'
- '--json'
- 'Emit JSON on stdout instead of the human summary.'
- 'env'
- 'None'
- '[PAS172/reap_callback_schedule] status='
- ' dry_run='
- ' brokerage_id='
- ' filter_status='
- ' candidates='
- ' deleted='
- ' skipped='
- ' failed='
- '  warn: '
- 'argv'

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ('\nPAS172 — Operator reaper for the PAS171 callback schedule\ndurable store (``pas_callback_schedule``).\n\nCloses the PAS171 §13 "promote operator-side reapers" item.\nTerminal callback rows (``completed``, ``cancelled``,\n``overdue``, ``failed``) accumulate forever unless an operator\nremoves them; this script IS that operator action.\n\nDoctrine:\n\n* **Dry-run by default.** ``--execute`` is required to delete.\n* **Terminal-status only.** This reaper NEVER touches\n  ``pending`` or ``reminded`` rows. Even if their\n  ``scheduled_for`` is far in the past, only the\n  ``mark_callback_overdue`` lifecycle helper may transition\n  them out of pending — the reaper does NOT shortcut that.\n* **Bounded delete count.** ``--limit`` caps rows removed\n  per run (default 1000, hard cap 5000).\n* **Age clamp.** ``--older-than-hours`` defaults to 168 (7\n  days) and is clamped to ``[24, 24*30]``. Operator wants\n  enough retention to investigate a recent incident before\n  rows disappear.\n* **Structural envelopes only.** NEVER echoes\n  source_call_id contents, completed_by names, last_error_code\n  strings, or any raw lead context. The script only emits\n  counts.\n* **DB unavailable → exit 0 with skipped envelope.**\n* **No scheduler / cron added.** PAS172 does NOT automate\n  execution.\n* **NEVER raises.**\n\nUsage:\n\n    # Dry-run; print what *would* be reaped.\n    python scripts/reap_callback_schedule.py\n\n    # Reap rows older than 7 days, per-brokerage.\n    python scripts/reap_callback_schedule.py \\\n        --brokerage-id brk-pilot --older-than-hours 168 \\\n        --limit 500 --execute\n\n    # Restrict to a specific terminal status.\n    python scripts/reap_callback_schedule.py \\\n        --status completed --older-than-hours 168 --execute\n\nExit codes:\n    0  — completed successfully (including dry-run + skipped)\n    2  — bad CLI arguments\n')
               STORE_NAME               0 (__doc__)

  52           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  54           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  55           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  56           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (logging)
               STORE_NAME               5 (logging)

  57           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (os)
               STORE_NAME               6 (os)

  58           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (sys)
               STORE_NAME               7 (sys)

  59           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timedelta', 'timezone'))
               IMPORT_NAME              8 (datetime)
               IMPORT_FROM              8 (datetime)
               STORE_NAME               8 (datetime)
               IMPORT_FROM              9 (timedelta)
               STORE_NAME               9 (timedelta)
               IMPORT_FROM             10 (timezone)
               STORE_NAME              10 (timezone)
               POP_TOP

  60           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
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

  63           LOAD_NAME                7 (sys)
               LOAD_ATTR               32 (stdout)
               LOAD_NAME                7 (sys)
               LOAD_ATTR               34 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              18 (_stream)

  64           NOP

  65   L2:     LOAD_NAME               18 (_stream)
               LOAD_ATTR               39 (reconfigure + NULL|self)
               LOAD_CONST               5 ('utf-8')
               LOAD_CONST               6 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  63   L4:     END_FOR
               POP_ITER

  70           LOAD_NAME                7 (sys)
               LOAD_ATTR               42 (path)
               LOAD_ATTR               45 (insert + NULL|self)
               LOAD_SMALL_INT           0
               LOAD_NAME                6 (os)
               LOAD_ATTR               42 (path)
               LOAD_ATTR               47 (abspath + NULL|self)
               LOAD_NAME                6 (os)
               LOAD_ATTR               42 (path)
               LOAD_ATTR               49 (join + NULL|self)
               LOAD_NAME                6 (os)
               LOAD_ATTR               42 (path)
               LOAD_ATTR               51 (dirname + NULL|self)
               LOAD_NAME               26 (__file__)
               CALL                     1
               LOAD_CONST               7 ('..')
               CALL                     2
               CALL                     1
               CALL                     2
               POP_TOP

  73           LOAD_NAME                5 (logging)
               LOAD_ATTR               54 (getLogger)
               PUSH_NULL
               LOAD_CONST               8 ('pas.scripts.reap_callback_schedule')
               CALL                     1
               STORE_NAME              28 (logger)

  76           LOAD_CONST               9 ('pas_callback_schedule')
               STORE_NAME              29 (_TABLE)

  79           LOAD_CONST              41 (('completed', 'cancelled', 'overdue', 'failed'))
               STORE_NAME              30 (TERMINAL_STATUSES)

  81           LOAD_SMALL_INT         168
               STORE_NAME              31 (_DEFAULT_OLDER_THAN_HOURS)

  82           LOAD_SMALL_INT          24
               STORE_NAME              32 (_MIN_OLDER_THAN_HOURS)

  83           LOAD_CONST              42 (720)
               STORE_NAME              33 (_MAX_OLDER_THAN_HOURS)

  85           LOAD_CONST              10 (1000)
               STORE_NAME              34 (_DEFAULT_LIMIT)

  86           LOAD_CONST              11 (5000)
               STORE_NAME              35 (_HARD_CAP_LIMIT)

  89           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts/reap_callback_schedule.py", line 89>)
               MAKE_FUNCTION
               LOAD_CONST              13 (<code object _now_iso at 0x0000018C180388F0, file "scripts/reap_callback_schedule.py", line 89>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              36 (_now_iso)

  93           LOAD_CONST              14 (<code object _get_db_safe at 0x0000018C17FF1230, file "scripts/reap_callback_schedule.py", line 93>)
               MAKE_FUNCTION
               STORE_NAME              37 (_get_db_safe)

 105           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18025830, file "scripts/reap_callback_schedule.py", line 105>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _clamp at 0x0000018C18038CB0, file "scripts/reap_callback_schedule.py", line 105>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (_clamp)

 117           LOAD_CONST              17 ('candidate_count')

 125           LOAD_SMALL_INT           0

 117           LOAD_CONST              18 ('deleted_count')

 126           LOAD_SMALL_INT           0

 117           LOAD_CONST              19 ('skipped_count')

 127           LOAD_SMALL_INT           0

 117           LOAD_CONST              20 ('failed_count')

 128           LOAD_SMALL_INT           0

 117           LOAD_CONST              21 ('warnings')

 129           LOAD_CONST               2 (None)

 117           LOAD_CONST              22 ('error_code')

 130           LOAD_CONST               2 (None)

 117           BUILD_MAP                6
               LOAD_CONST              23 (<code object __annotate__ at 0x0000018C18053E10, file "scripts/reap_callback_schedule.py", line 117>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object _safe_envelope at 0x0000018C17972D90, file "scripts/reap_callback_schedule.py", line 117>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              39 (_safe_envelope)

 151           LOAD_CONST              25 ('brokerage_id')

 153           LOAD_CONST               2 (None)

 151           LOAD_CONST              26 ('filter_status')

 154           LOAD_CONST               2 (None)

 151           LOAD_CONST              27 ('older_than_hours')

 155           LOAD_NAME               31 (_DEFAULT_OLDER_THAN_HOURS)

 151           LOAD_CONST              28 ('limit')

 156           LOAD_NAME               34 (_DEFAULT_LIMIT)

 151           LOAD_CONST              29 ('dry_run')

 157           LOAD_CONST              30 (True)

 151           LOAD_CONST              31 ('now')

 158           LOAD_CONST               2 (None)

 151           BUILD_MAP                6
               LOAD_CONST              32 (<code object __annotate__ at 0x0000018C1812C140, file "scripts/reap_callback_schedule.py", line 151>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object reap at 0x0000018C17F722B0, file "scripts/reap_callback_schedule.py", line 151>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              40 (reap)

 285           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA34B0, file "scripts/reap_callback_schedule.py", line 285>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object _build_parser at 0x0000018C17CD0F70, file "scripts/reap_callback_schedule.py", line 285>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (_build_parser)

 325           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts/reap_callback_schedule.py", line 325>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object _print_summary at 0x0000018C17FEDE30, file "scripts/reap_callback_schedule.py", line 325>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (_print_summary)

 341           LOAD_CONST              43 ((None,))
               LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts/reap_callback_schedule.py", line 341>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object main at 0x0000018C17F78570, file "scripts/reap_callback_schedule.py", line 341>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              43 (main)

 364           LOAD_NAME               44 (__name__)
               LOAD_CONST              40 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 365           LOAD_NAME                7 (sys)
               LOAD_ATTR               90 (exit)
               PUSH_NULL
               LOAD_NAME               43 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 364   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  66           LOAD_NAME               20 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  67   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          282 (to L1)

  66   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts/reap_callback_schedule.py", line 89>:
 89           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C180388F0, file "scripts/reap_callback_schedule.py", line 89>:
 89           RESUME                   0

 90           LOAD_GLOBAL              0 (datetime)
              LOAD_ATTR                2 (now)
              PUSH_NULL
              LOAD_GLOBAL              4 (timezone)
              LOAD_ATTR                6 (utc)
              CALL                     1
              LOAD_ATTR                9 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object _get_db_safe at 0x0000018C17FF1230, file "scripts/reap_callback_schedule.py", line 93>:
  93           RESUME                   0

  94           NOP

  95   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

  96           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

  97           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

  98   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

  99           LOAD_CONST               2 ('reap_callback_schedule db client unavailable type=')

 100           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

  99           BUILD_STRING             2

  98           CALL                     1
               POP_TOP

 102   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
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

Disassembly of <code object __annotate__ at 0x0000018C18025830, file "scripts/reap_callback_schedule.py", line 105>:
105           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('lo')
              LOAD_CONST               4 ('int')
              LOAD_CONST               5 ('hi')
              LOAD_CONST               4 ('int')
              LOAD_CONST               6 ('default')
              LOAD_CONST               4 ('int')
              LOAD_CONST               7 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _clamp at 0x0000018C18038CB0, file "scripts/reap_callback_schedule.py", line 105>:
 105           RESUME                   0

 106           NOP

 107   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

 110   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 111           LOAD_FAST                1 (lo)
               RETURN_VALUE

 112   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 113           LOAD_FAST                2 (hi)
               RETURN_VALUE

 114   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 108           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

 109           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 108   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18053E10, file "scripts/reap_callback_schedule.py", line 117>:
117           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

119           LOAD_CONST               2 ('str')

117           LOAD_CONST               3 ('dry_run')

120           LOAD_CONST               4 ('bool')

117           LOAD_CONST               5 ('brokerage_id')

121           LOAD_CONST               6 ('Optional[str]')

117           LOAD_CONST               7 ('filter_status')

122           LOAD_CONST               6 ('Optional[str]')

117           LOAD_CONST               8 ('older_than_hours')

123           LOAD_CONST               9 ('int')

117           LOAD_CONST              10 ('limit')

124           LOAD_CONST               9 ('int')

117           LOAD_CONST              11 ('candidate_count')

125           LOAD_CONST               9 ('int')

117           LOAD_CONST              12 ('deleted_count')

126           LOAD_CONST               9 ('int')

117           LOAD_CONST              13 ('skipped_count')

127           LOAD_CONST               9 ('int')

117           LOAD_CONST              14 ('failed_count')

128           LOAD_CONST               9 ('int')

117           LOAD_CONST              15 ('warnings')

129           LOAD_CONST              16 ('Optional[List[str]]')

117           LOAD_CONST              17 ('error_code')

130           LOAD_CONST               6 ('Optional[str]')

117           LOAD_CONST              18 ('return')

131           LOAD_CONST              19 ('Dict[str, Any]')

117           BUILD_MAP               13
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C17972D90, file "scripts/reap_callback_schedule.py", line 117>:
117           RESUME                   0

133           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS172')

134           LOAD_CONST               2 ('reaper')
              LOAD_CONST               3 ('callback_schedule')

135           LOAD_CONST               4 ('status')
              LOAD_FAST                0 (status)

136           LOAD_CONST               5 ('dry_run')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         1 (dry_run)
              CALL                     1

137           LOAD_CONST               6 ('brokerage_id')
              LOAD_FAST                2 (brokerage_id)

138           LOAD_CONST               7 ('filter_status')
              LOAD_FAST                3 (filter_status)

139           LOAD_CONST               8 ('older_than_hours')
              LOAD_FAST                4 (older_than_hours)

140           LOAD_CONST               9 ('limit')
              LOAD_FAST                5 (limit)

141           LOAD_CONST              10 ('candidate_count')
              LOAD_FAST                6 (candidate_count)

142           LOAD_CONST              11 ('deleted_count')
              LOAD_FAST                7 (deleted_count)

143           LOAD_CONST              12 ('skipped_count')
              LOAD_FAST                8 (skipped_count)

144           LOAD_CONST              13 ('failed_count')
              LOAD_FAST                9 (failed_count)

145           LOAD_CONST              14 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST               10 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

146           LOAD_CONST              15 ('error_code')
              LOAD_FAST_BORROW        11 (error_code)

147           LOAD_CONST              16 ('generated_at')
              LOAD_GLOBAL              5 (_now_iso + NULL)
              CALL                     0

132           BUILD_MAP               15
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C1812C140, file "scripts/reap_callback_schedule.py", line 151>:
151           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

153           LOAD_CONST               2 ('Optional[str]')

151           LOAD_CONST               3 ('filter_status')

154           LOAD_CONST               2 ('Optional[str]')

151           LOAD_CONST               4 ('older_than_hours')

155           LOAD_CONST               5 ('int')

151           LOAD_CONST               6 ('limit')

156           LOAD_CONST               5 ('int')

151           LOAD_CONST               7 ('dry_run')

157           LOAD_CONST               8 ('bool')

151           LOAD_CONST               9 ('now')

158           LOAD_CONST              10 ('Optional[datetime]')

151           LOAD_CONST              11 ('return')

159           LOAD_CONST              12 ('Dict[str, Any]')

151           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object reap at 0x0000018C17F722B0, file "scripts/reap_callback_schedule.py", line 151>:
 151            RESUME                   0

 162            LOAD_FAST_BORROW         1 (filter_status)
                POP_JUMP_IF_NONE        28 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (filter_status)
                LOAD_GLOBAL              0 (TERMINAL_STATUSES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       17 (to L1)
                NOT_TAKEN

 163            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 164            LOAD_CONST               2 ('failed')

 165            LOAD_FAST_BORROW_LOAD_FAST_BORROW 64 (dry_run, brokerage_id)

 166            LOAD_FAST_BORROW         1 (filter_status)

 167            LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (older_than_hours, limit)

 168            LOAD_CONST               3 ('invalid_filter_status')

 163            LOAD_CONST               4 (('status', 'dry_run', 'brokerage_id', 'filter_status', 'older_than_hours', 'limit', 'error_code'))
                CALL_KW                  7
                RETURN_VALUE

 170    L1:     LOAD_GLOBAL              5 (_clamp + NULL)

 171            LOAD_FAST_BORROW         2 (older_than_hours)
                LOAD_GLOBAL              6 (_MIN_OLDER_THAN_HOURS)

 172            LOAD_GLOBAL              8 (_MAX_OLDER_THAN_HOURS)
                LOAD_GLOBAL             10 (_DEFAULT_OLDER_THAN_HOURS)

 170            CALL                     4
                STORE_FAST               6 (hours)

 174            LOAD_GLOBAL              5 (_clamp + NULL)
                LOAD_FAST_BORROW         3 (limit)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL             12 (_HARD_CAP_LIMIT)
                LOAD_GLOBAL             14 (_DEFAULT_LIMIT)
                CALL                     4
                STORE_FAST               7 (capped_limit)

 177            LOAD_GLOBAL             17 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_GLOBAL             18 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR               21 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L2)
                NOT_TAKEN

 176            LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR               21 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L3)

 178    L2:     LOAD_CONST               1 (None)

 175    L3:     STORE_FAST               8 (bid)

 181            LOAD_GLOBAL             17 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (now)
                LOAD_GLOBAL             22 (datetime)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       21 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         5 (now)
                LOAD_ATTR               24 (tzinfo)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_FAST                5 (now)
                JUMP_FORWARD            35 (to L5)

 182    L4:     LOAD_GLOBAL             22 (datetime)
                LOAD_ATTR               26 (now)
                PUSH_NULL
                LOAD_GLOBAL             28 (timezone)
                LOAD_ATTR               30 (utc)
                CALL                     1

 180    L5:     STORE_FAST               9 (now_dt)

 184            LOAD_FAST_BORROW         9 (now_dt)
                LOAD_GLOBAL             33 (timedelta + NULL)
                LOAD_FAST_BORROW         6 (hours)
                LOAD_CONST               5 (('hours',))
                CALL_KW                  1
                BINARY_OP               10 (-)
                LOAD_ATTR               35 (isoformat + NULL|self)
                LOAD_CONST               6 ('seconds')
                LOAD_CONST               7 (('timespec',))
                CALL_KW                  1
                STORE_FAST              10 (cutoff_iso)

 186            LOAD_GLOBAL             37 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST              11 (db)

 187            LOAD_FAST_BORROW        11 (db)
                POP_JUMP_IF_NOT_NONE    19 (to L6)
                NOT_TAKEN

 188            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 189            LOAD_CONST               8 ('skipped')

 190            LOAD_FAST_BORROW_LOAD_FAST_BORROW 72 (dry_run, bid)

 191            LOAD_FAST_BORROW         1 (filter_status)

 192            LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (hours, capped_limit)

 193            LOAD_CONST               9 ('durable_callback_schedule_unavailable')
                BUILD_LIST               1

 194            LOAD_CONST               9 ('durable_callback_schedule_unavailable')

 188            LOAD_CONST              10 (('status', 'dry_run', 'brokerage_id', 'filter_status', 'older_than_hours', 'limit', 'warnings', 'error_code'))
                CALL_KW                  8
                RETURN_VALUE

 198    L6:     NOP

 200    L7:     LOAD_FAST_BORROW        11 (db)
                LOAD_ATTR               39 (table + NULL|self)
                LOAD_GLOBAL             40 (_TABLE)
                CALL                     1

 201            LOAD_ATTR               43 (select + NULL|self)
                LOAD_CONST              11 ('callback_id, brokerage_id, status, updated_at')
                CALL                     1

 202            LOAD_ATTR               45 (lt + NULL|self)
                LOAD_CONST              12 ('updated_at')
                LOAD_FAST_BORROW        10 (cutoff_iso)
                CALL                     2

 203            LOAD_ATTR               47 (order + NULL|self)
                LOAD_CONST              12 ('updated_at')
                LOAD_CONST              13 (False)
                LOAD_CONST              14 (('desc',))
                CALL_KW                  2

 204            LOAD_ATTR               49 (limit + NULL|self)
                LOAD_FAST_BORROW         7 (capped_limit)
                CALL                     1

 199            STORE_FAST              12 (query)

 206            LOAD_FAST_BORROW         8 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L10)
        L8:     NOT_TAKEN

 207    L9:     LOAD_FAST_BORROW        12 (query)
                LOAD_ATTR               51 (eq + NULL|self)
                LOAD_CONST              15 ('brokerage_id')
                LOAD_FAST_BORROW         8 (bid)
                CALL                     2
                STORE_FAST              12 (query)

 208   L10:     LOAD_FAST_BORROW         1 (filter_status)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L13)
       L11:     NOT_TAKEN

 209   L12:     LOAD_FAST_BORROW        12 (query)
                LOAD_ATTR               51 (eq + NULL|self)
                LOAD_CONST              16 ('status')
                LOAD_FAST_BORROW         1 (filter_status)
                CALL                     2
                STORE_FAST              12 (query)

 210   L13:     LOAD_FAST_BORROW        12 (query)
                LOAD_ATTR               53 (execute + NULL|self)
                CALL                     0
                STORE_FAST              13 (result)

 211            LOAD_GLOBAL             55 (list + NULL)
                LOAD_GLOBAL             57 (getattr + NULL)
                LOAD_FAST_BORROW        13 (result)
                LOAD_CONST              17 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
       L14:     NOT_TAKEN
       L15:     POP_TOP
                BUILD_LIST               0
       L16:     CALL                     1
                STORE_FAST              14 (rows)

 228   L17:     LOAD_FAST               14 (rows)
                GET_ITER

 227            LOAD_FAST_AND_CLEAR     16 (r)
                SWAP                     2
       L18:     BUILD_LIST               0
                SWAP                     2

 228   L19:     FOR_ITER                57 (to L24)
                STORE_FAST              16 (r)

 229            LOAD_GLOBAL             17 (isinstance + NULL)
                LOAD_FAST               16 (r)
                LOAD_GLOBAL             68 (dict)
                CALL                     2
                TO_BOOL

 228   L20:     POP_JUMP_IF_TRUE         3 (to L21)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L19)

 229   L21:     LOAD_FAST               16 (r)
                LOAD_ATTR               71 (get + NULL|self)
                LOAD_CONST              16 ('status')
                CALL                     1
                LOAD_GLOBAL              0 (TERMINAL_STATUSES)
                CONTAINS_OP              0 (in)

 228   L22:     POP_JUMP_IF_TRUE         3 (to L23)
                NOT_TAKEN
                JUMP_BACKWARD           55 (to L19)
       L23:     LOAD_FAST               16 (r)
                LIST_APPEND              2
                JUMP_BACKWARD           59 (to L19)
       L24:     END_FOR
                POP_ITER

 227   L25:     STORE_FAST              17 (candidates)
                STORE_FAST              16 (r)

 231            LOAD_GLOBAL             73 (len + NULL)
                LOAD_FAST               17 (candidates)
                CALL                     1
                STORE_FAST              18 (candidate_count)

 233            LOAD_FAST                4 (dry_run)
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L26)
                NOT_TAKEN

 234            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 235            LOAD_CONST              20 ('ok')

 236            LOAD_CONST              21 (True)
                LOAD_FAST                8 (bid)

 237            LOAD_FAST                1 (filter_status)

 238            LOAD_FAST_LOAD_FAST    103 (hours, capped_limit)

 239            LOAD_FAST               18 (candidate_count)

 234            LOAD_CONST              22 (('status', 'dry_run', 'brokerage_id', 'filter_status', 'older_than_hours', 'limit', 'candidate_count'))
                CALL_KW                  7
                RETURN_VALUE

 242   L26:     LOAD_SMALL_INT           0
                STORE_FAST              19 (deleted)

 243            LOAD_SMALL_INT           0
                STORE_FAST              20 (skipped)

 244            LOAD_SMALL_INT           0
                STORE_FAST              21 (failed)

 245            BUILD_LIST               0
                STORE_FAST              22 (warnings)

 246            LOAD_FAST               17 (candidates)
                GET_ITER
       L27:     FOR_ITER               183 (to L32)
                STORE_FAST              23 (row)

 247            LOAD_FAST               23 (row)
                LOAD_ATTR               71 (get + NULL|self)
                LOAD_CONST              23 ('callback_id')
                CALL                     1
                STORE_FAST              24 (cid)

 248            LOAD_FAST               23 (row)
                LOAD_ATTR               71 (get + NULL|self)
                LOAD_CONST              15 ('brokerage_id')
                CALL                     1
                STORE_FAST              25 (row_bid)

 249            LOAD_GLOBAL             17 (isinstance + NULL)
                LOAD_FAST               24 (cid)
                LOAD_GLOBAL             18 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L28)
                NOT_TAKEN
                LOAD_GLOBAL             17 (isinstance + NULL)
                LOAD_FAST               25 (row_bid)
                LOAD_GLOBAL             18 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L29)
                NOT_TAKEN

 250   L28:     LOAD_FAST               20 (skipped)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              20 (skipped)

 251            JUMP_BACKWARD           92 (to L27)

 252   L29:     NOP

 254   L30:     LOAD_FAST               11 (db)
                LOAD_ATTR               39 (table + NULL|self)
                LOAD_GLOBAL             40 (_TABLE)
                CALL                     1

 255            LOAD_ATTR               75 (delete + NULL|self)
                CALL                     0

 256            LOAD_ATTR               51 (eq + NULL|self)
                LOAD_CONST              23 ('callback_id')
                LOAD_FAST               24 (cid)
                CALL                     2

 257            LOAD_ATTR               51 (eq + NULL|self)
                LOAD_CONST              15 ('brokerage_id')
                LOAD_FAST               25 (row_bid)
                CALL                     2

 258            LOAD_ATTR               53 (execute + NULL|self)
                CALL                     0
                POP_TOP

 260            LOAD_FAST               19 (deleted)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              19 (deleted)
       L31:     JUMP_BACKWARD          185 (to L27)

 246   L32:     END_FOR
                POP_ITER

 271            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 272            LOAD_FAST               21 (failed)
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L33)
                NOT_TAKEN
                LOAD_CONST              20 ('ok')
                JUMP_FORWARD             1 (to L34)
       L33:     LOAD_CONST              26 ('partial_failure')

 273   L34:     LOAD_CONST              13 (False)
                LOAD_FAST                8 (bid)

 274            LOAD_FAST                1 (filter_status)

 275            LOAD_FAST_LOAD_FAST    103 (hours, capped_limit)

 276            LOAD_FAST               18 (candidate_count)

 277            LOAD_FAST               19 (deleted)

 278            LOAD_FAST               20 (skipped)

 279            LOAD_FAST               21 (failed)

 280            LOAD_FAST               22 (warnings)

 281            LOAD_FAST               21 (failed)
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        8 (to L35)
                NOT_TAKEN
                LOAD_CONST               1 (None)

 271            LOAD_CONST              28 (('status', 'dry_run', 'brokerage_id', 'filter_status', 'older_than_hours', 'limit', 'candidate_count', 'deleted_count', 'skipped_count', 'failed_count', 'warnings', 'error_code'))
                CALL_KW                 12
                RETURN_VALUE

 281   L35:     LOAD_CONST              27 ('reaper_partial_failure')

 271            LOAD_CONST              28 (('status', 'dry_run', 'brokerage_id', 'filter_status', 'older_than_hours', 'limit', 'candidate_count', 'deleted_count', 'skipped_count', 'failed_count', 'warnings', 'error_code'))
                CALL_KW                 12
                RETURN_VALUE

  --   L36:     PUSH_EXC_INFO

 212            LOAD_GLOBAL             58 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       94 (to L41)
                NOT_TAKEN
                STORE_FAST              15 (e)

 213   L37:     LOAD_GLOBAL             60 (logger)
                LOAD_ATTR               63 (warning + NULL|self)

 214            LOAD_CONST              18 ('reap_callback_schedule read error type=')
                LOAD_GLOBAL             65 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               66 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 213            CALL                     1
                POP_TOP

 216            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 217            LOAD_CONST               8 ('skipped')

 218            LOAD_FAST_LOAD_FAST     72 (dry_run, bid)

 219            LOAD_FAST                1 (filter_status)

 220            LOAD_FAST_LOAD_FAST    103 (hours, capped_limit)

 221            LOAD_CONST              19 ('db_read_failed:')
                LOAD_GLOBAL             65 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               66 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 222            LOAD_CONST               9 ('durable_callback_schedule_unavailable')

 216            LOAD_CONST              10 (('status', 'dry_run', 'brokerage_id', 'filter_status', 'older_than_hours', 'limit', 'warnings', 'error_code'))
                CALL_KW                  8
       L38:     SWAP                     2
       L39:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RETURN_VALUE

  --   L40:     LOAD_CONST               1 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RERAISE                  1

 212   L41:     RERAISE                  0

  --   L42:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L43:     SWAP                     2
                POP_TOP

 227            SWAP                     2
                STORE_FAST              16 (r)
                RERAISE                  0

  --   L44:     PUSH_EXC_INFO

 261            LOAD_GLOBAL             58 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      113 (to L49)
                NOT_TAKEN
                STORE_FAST              15 (e)

 262   L45:     LOAD_FAST               21 (failed)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              21 (failed)

 263            LOAD_CONST              24 ('db_delete_failed:')
                LOAD_GLOBAL             65 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               66 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                STORE_FAST              26 (code)

 264            LOAD_FAST               26 (code)
                LOAD_FAST               22 (warnings)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       18 (to L46)
                NOT_TAKEN

 265            LOAD_FAST               22 (warnings)
                LOAD_ATTR               77 (append + NULL|self)
                LOAD_FAST               26 (code)
                CALL                     1
                POP_TOP

 266   L46:     LOAD_GLOBAL             60 (logger)
                LOAD_ATTR               63 (warning + NULL|self)

 267            LOAD_CONST              25 ('reap_callback_schedule delete error type=')

 268            LOAD_GLOBAL             65 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               66 (__name__)
                FORMAT_SIMPLE

 267            BUILD_STRING             2

 266            CALL                     1
                POP_TOP
       L47:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD          462 (to L27)

  --   L48:     LOAD_CONST               1 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RERAISE                  1

 261   L49:     RERAISE                  0

  --   L50:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L7 to L8 -> L36 [0]
  L9 to L11 -> L36 [0]
  L12 to L14 -> L36 [0]
  L15 to L17 -> L36 [0]
  L18 to L20 -> L43 [2]
  L21 to L22 -> L43 [2]
  L23 to L25 -> L43 [2]
  L30 to L31 -> L44 [1]
  L36 to L37 -> L42 [1] lasti
  L37 to L38 -> L40 [1] lasti
  L38 to L39 -> L42 [1] lasti
  L40 to L42 -> L42 [1] lasti
  L44 to L45 -> L50 [2] lasti
  L45 to L47 -> L48 [2] lasti
  L48 to L50 -> L50 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "scripts/reap_callback_schedule.py", line 285>:
285           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C17CD0F70, file "scripts/reap_callback_schedule.py", line 285>:
285           RESUME                   0

286           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

287           LOAD_CONST               0 ('reap_callback_schedule')

289           LOAD_CONST               1 ('PAS172 — Reap terminal callback rows from the PAS171 durable store. Dry-run by default; --execute required to delete. NEVER touches pending / reminded rows. NEVER echoes raw lead context.')

286           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

295           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

296           LOAD_CONST               3 ('--brokerage-id')
              LOAD_CONST               4 (None)

297           LOAD_CONST               5 ('Scope the reap to a single brokerage (default: all).')

295           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

299           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

300           LOAD_CONST               7 ('--status')
              LOAD_CONST               4 (None)
              LOAD_GLOBAL              7 (list + NULL)
              LOAD_GLOBAL              8 (TERMINAL_STATUSES)
              CALL                     1

301           LOAD_CONST               8 ('Restrict to one terminal status (default: all terminal statuses).')

299           LOAD_CONST               9 (('default', 'choices', 'help'))
              CALL_KW                  4
              POP_TOP

303           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

304           LOAD_CONST              10 ('--older-than-hours')
              LOAD_GLOBAL             10 (int)
              LOAD_GLOBAL             12 (_DEFAULT_OLDER_THAN_HOURS)

305           LOAD_CONST              11 ('Reap rows whose updated_at is older than this many hours (clamped to [')

306           LOAD_GLOBAL             14 (_MIN_OLDER_THAN_HOURS)
              FORMAT_SIMPLE
              LOAD_CONST              12 (',')
              LOAD_GLOBAL             16 (_MAX_OLDER_THAN_HOURS)
              FORMAT_SIMPLE
              LOAD_CONST              13 ('], default ')

307           LOAD_GLOBAL             12 (_DEFAULT_OLDER_THAN_HOURS)
              FORMAT_SIMPLE
              LOAD_CONST              14 (').')

305           BUILD_STRING             7

303           LOAD_CONST              15 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

309           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

310           LOAD_CONST              16 ('--limit')
              LOAD_GLOBAL             10 (int)
              LOAD_GLOBAL             18 (_DEFAULT_LIMIT)

311           LOAD_CONST              17 ('Hard cap on rows deleted per run (default ')
              LOAD_GLOBAL             18 (_DEFAULT_LIMIT)
              FORMAT_SIMPLE
              LOAD_CONST              18 (', max ')

312           LOAD_GLOBAL             20 (_HARD_CAP_LIMIT)
              FORMAT_SIMPLE
              LOAD_CONST              14 (').')

311           BUILD_STRING             5

309           LOAD_CONST              15 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

314           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

315           LOAD_CONST              19 ('--execute')
              LOAD_CONST              20 ('store_true')

316           LOAD_CONST              21 ('Actually delete rows. Without this flag the script runs in dry-run mode.')

314           LOAD_CONST              22 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

318           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

319           LOAD_CONST              23 ('--json')
              LOAD_CONST              20 ('store_true')

320           LOAD_CONST              24 ('Emit JSON on stdout instead of the human summary.')

318           LOAD_CONST              22 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

322           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts/reap_callback_schedule.py", line 325>:
325           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('env')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _print_summary at 0x0000018C17FEDE30, file "scripts/reap_callback_schedule.py", line 325>:
325           RESUME                   0

326           LOAD_GLOBAL              1 (print + NULL)

327           LOAD_CONST               0 ('[PAS172/reap_callback_schedule] status=')

328           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               1 ('status')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' dry_run=')

329           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               3 ('dry_run')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' brokerage_id=')

330           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               5 ('brokerage_id')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' filter_status=')

331           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               7 ('filter_status')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' candidates=')

332           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               9 ('candidate_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' deleted=')

333           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST              11 ('deleted_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              12 (' skipped=')

334           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST              13 ('skipped_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              14 (' failed=')

335           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST              15 ('failed_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

327           BUILD_STRING            16

326           CALL                     1
              POP_TOP

337           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              16 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     LOAD_CONST              17 (slice(None, 10, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               1 (w)

338           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              18 ('  warn: ')
              LOAD_FAST_BORROW         1 (w)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

337   L3:     END_FOR
              POP_ITER
              LOAD_CONST              19 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts/reap_callback_schedule.py", line 341>:
341           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17F78570, file "scripts/reap_callback_schedule.py", line 341>:
 341            RESUME                   0

 342            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 343            NOP

 344    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 348    L2:     LOAD_GLOBAL             11 (reap + NULL)

 349            LOAD_FAST                2 (args)
                LOAD_ATTR               12 (brokerage_id)

 350            LOAD_FAST                2 (args)
                LOAD_ATTR               14 (status)

 351            LOAD_FAST                2 (args)
                LOAD_ATTR               16 (older_than_hours)

 352            LOAD_FAST                2 (args)
                LOAD_ATTR               18 (limit)

 353            LOAD_FAST                2 (args)
                LOAD_ATTR               20 (execute)
                TO_BOOL
                UNARY_NOT

 348            LOAD_CONST               2 (('brokerage_id', 'filter_status', 'older_than_hours', 'limit', 'dry_run'))
                CALL_KW                  5
                STORE_FAST               4 (env)

 356            LOAD_FAST                2 (args)
                LOAD_ATTR               22 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       37 (to L3)
                NOT_TAKEN

 357            LOAD_GLOBAL             25 (print + NULL)
                LOAD_GLOBAL             22 (json)
                LOAD_ATTR               26 (dumps)
                PUSH_NULL
                LOAD_FAST                4 (env)
                LOAD_SMALL_INT           2
                LOAD_CONST               3 (True)
                LOAD_CONST               4 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 361            LOAD_SMALL_INT           0
                RETURN_VALUE

 359    L3:     LOAD_GLOBAL             29 (_print_summary + NULL)
                LOAD_FAST                4 (env)
                CALL                     1
                POP_TOP

 361            LOAD_SMALL_INT           0
                RETURN_VALUE

  --    L4:     PUSH_EXC_INFO

 345            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L13)
                NOT_TAKEN
                STORE_FAST               3 (e)

 346    L5:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST               5 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L10)
        L6:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
        L7:     NOT_TAKEN
        L8:     POP_TOP
                LOAD_SMALL_INT           0
        L9:     CALL                     1
       L10:     SWAP                     2
       L11:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L12:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 345   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L4 [0]
  L4 to L5 -> L14 [1] lasti
  L5 to L7 -> L12 [1] lasti
  L8 to L10 -> L12 [1] lasti
  L10 to L11 -> L14 [1] lasti
  L12 to L14 -> L14 [1] lasti
```
