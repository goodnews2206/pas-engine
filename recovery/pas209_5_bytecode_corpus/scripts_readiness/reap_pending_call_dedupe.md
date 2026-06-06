# scripts_readiness/reap_pending_call_dedupe

- **pyc:** `scripts\__pycache__\reap_pending_call_dedupe.cpython-314.pyc`
- **expected source path (absent):** `scripts/reap_pending_call_dedupe.py`
- **co_filename (from bytecode):** `scripts/reap_pending_call_dedupe.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS172 — Operator reaper for the PAS171 pending-call dedupe
durable store (``pas_pending_call_dedupe``).

Closes the PAS171 §13 "promote operator-side reapers" item. The
durable dedupe rows have a fixed TTL (default 24h, max 168h),
but nothing in PAS171 actually deletes expired rows — they sit
in the table until an operator action removes them. This script
IS that operator action.

Doctrine:

* **Dry-run by default.** ``--execute`` is required to actually
  delete. Mirrors the PAS167 / PAS168 reaper pattern.
* **Bounded delete count.** ``--limit`` caps the number of
  rows removed per run (default 1000, hard cap 5000) so an
  operator typo cannot wipe the table.
* **TTL / age clamp.** ``--older-than-hours`` defaults to 24
  (the PAS171 default TTL) and is clamped to ``[1, 168]``.
  Rows newer than the cutoff are NEVER touched.
* **Structural envelopes only.** Output is JSON / human-friendly
  but NEVER echoes the dedupe key. NEVER echoes raw lead
  context. NEVER echoes secrets.
* **DB unavailable → exit 0 with skipped envelope.** The
  operator can rerun without inventing a recovery path.
* **No scheduler / cron added.** PAS172 does NOT automate
  this script's execution.
* **NEVER raises.**

Usage:

    # Dry-run; print what *would* be reaped.
    python scripts/reap_pending_call_dedupe.py

    # Reap rows older than 24h, per-brokerage.
    python scripts/reap_pending_call_dedupe.py \
        --brokerage-id brk-pilot --older-than-hours 24 \
        --limit 500 --execute

    # Emit JSON for piping into a dashboard.
    python scripts/reap_pending_call_dedupe.py --json

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

- '\nPAS172 — Operator reaper for the PAS171 pending-call dedupe\ndurable store (``pas_pending_call_dedupe``).\n\nCloses the PAS171 §13 "promote operator-side reapers" item. The\ndurable dedupe rows have a fixed TTL (default 24h, max 168h),\nbut nothing in PAS171 actually deletes expired rows — they sit\nin the table until an operator action removes them. This script\nIS that operator action.\n\nDoctrine:\n\n* **Dry-run by default.** ``--execute`` is required to actually\n  delete. Mirrors the PAS167 / PAS168 reaper pattern.\n* **Bounded delete count.** ``--limit`` caps the number of\n  rows removed per run (default 1000, hard cap 5000) so an\n  operator typo cannot wipe the table.\n* **TTL / age clamp.** ``--older-than-hours`` defaults to 24\n  (the PAS171 default TTL) and is clamped to ``[1, 168]``.\n  Rows newer than the cutoff are NEVER touched.\n* **Structural envelopes only.** Output is JSON / human-friendly\n  but NEVER echoes the dedupe key. NEVER echoes raw lead\n  context. NEVER echoes secrets.\n* **DB unavailable → exit 0 with skipped envelope.** The\n  operator can rerun without inventing a recovery path.\n* **No scheduler / cron added.** PAS172 does NOT automate\n  this script\'s execution.\n* **NEVER raises.**\n\nUsage:\n\n    # Dry-run; print what *would* be reaped.\n    python scripts/reap_pending_call_dedupe.py\n\n    # Reap rows older than 24h, per-brokerage.\n    python scripts/reap_pending_call_dedupe.py \\\n        --brokerage-id brk-pilot --older-than-hours 24 \\\n        --limit 500 --execute\n\n    # Emit JSON for piping into a dashboard.\n    python scripts/reap_pending_call_dedupe.py --json\n\nExit codes:\n    0  — completed successfully (including dry-run + skipped)\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'pas.scripts.reap_pending_call_dedupe'
- 'pas_pending_call_dedupe'
- 'candidate_count'
- 'deleted_count'
- 'skipped_count'
- 'failed_count'
- 'warnings'
- 'error_code'
- 'brokerage_id'
- 'older_than_hours'
- 'limit'
- 'dry_run'
- 'now'
- 'return'
- 'str'
- 'seconds'
- 'reap_pending_call_dedupe db client unavailable type='
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
- 'pending_call_dedupe'
- 'generated_at'
- 'Optional[datetime]'
- 'Reap expired pending-call dedupe rows.\n\nAlways returns a structural envelope. NEVER raises.\n'
- 'skipped'
- 'durable_pending_call_dedupe_unavailable'
- 'dedupe_key, brokerage_id, source, expires_at'
- 'expires_at'
- 'data'
- 'reap_pending_call_dedupe read error type='
- 'db_read_failed:'
- 'dedupe_key'
- 'db_delete_failed:'
- 'reap_pending_call_dedupe delete error type='
- 'partial_failure'
- 'reaper_partial_failure'
- 'argparse.ArgumentParser'
- 'reap_pending_call_dedupe'
- 'PAS172 — Reap expired pending-call dedupe rows from the PAS171 durable store. Dry-run by default; --execute required to delete. NEVER echoes the dedupe key. NEVER echoes raw lead context.'
- '--brokerage-id'
- 'Scope the reap to a single brokerage (default: all brokerages).'
- '--older-than-hours'
- 'Reap rows whose expires_at is older than this many hours (clamped to ['
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
- '[PAS172/reap_pending_call_dedupe] status='
- ' dry_run='
- ' brokerage_id='
- ' candidates='
- ' deleted='
- ' skipped='
- ' failed='
- '  warn: '
- 'argv'

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ('\nPAS172 — Operator reaper for the PAS171 pending-call dedupe\ndurable store (``pas_pending_call_dedupe``).\n\nCloses the PAS171 §13 "promote operator-side reapers" item. The\ndurable dedupe rows have a fixed TTL (default 24h, max 168h),\nbut nothing in PAS171 actually deletes expired rows — they sit\nin the table until an operator action removes them. This script\nIS that operator action.\n\nDoctrine:\n\n* **Dry-run by default.** ``--execute`` is required to actually\n  delete. Mirrors the PAS167 / PAS168 reaper pattern.\n* **Bounded delete count.** ``--limit`` caps the number of\n  rows removed per run (default 1000, hard cap 5000) so an\n  operator typo cannot wipe the table.\n* **TTL / age clamp.** ``--older-than-hours`` defaults to 24\n  (the PAS171 default TTL) and is clamped to ``[1, 168]``.\n  Rows newer than the cutoff are NEVER touched.\n* **Structural envelopes only.** Output is JSON / human-friendly\n  but NEVER echoes the dedupe key. NEVER echoes raw lead\n  context. NEVER echoes secrets.\n* **DB unavailable → exit 0 with skipped envelope.** The\n  operator can rerun without inventing a recovery path.\n* **No scheduler / cron added.** PAS172 does NOT automate\n  this script\'s execution.\n* **NEVER raises.**\n\nUsage:\n\n    # Dry-run; print what *would* be reaped.\n    python scripts/reap_pending_call_dedupe.py\n\n    # Reap rows older than 24h, per-brokerage.\n    python scripts/reap_pending_call_dedupe.py \\\n        --brokerage-id brk-pilot --older-than-hours 24 \\\n        --limit 500 --execute\n\n    # Emit JSON for piping into a dashboard.\n    python scripts/reap_pending_call_dedupe.py --json\n\nExit codes:\n    0  — completed successfully (including dry-run + skipped)\n    2  — bad CLI arguments\n')
               STORE_NAME               0 (__doc__)

  48           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  50           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  51           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  52           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (logging)
               STORE_NAME               5 (logging)

  53           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (os)
               STORE_NAME               6 (os)

  54           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (sys)
               STORE_NAME               7 (sys)

  55           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timedelta', 'timezone'))
               IMPORT_NAME              8 (datetime)
               IMPORT_FROM              8 (datetime)
               STORE_NAME               8 (datetime)
               IMPORT_FROM              9 (timedelta)
               STORE_NAME               9 (timedelta)
               IMPORT_FROM             10 (timezone)
               STORE_NAME              10 (timezone)
               POP_TOP

  56           LOAD_SMALL_INT           0
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

  59           LOAD_NAME                7 (sys)
               LOAD_ATTR               32 (stdout)
               LOAD_NAME                7 (sys)
               LOAD_ATTR               34 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              18 (_stream)

  60           NOP

  61   L2:     LOAD_NAME               18 (_stream)
               LOAD_ATTR               39 (reconfigure + NULL|self)
               LOAD_CONST               5 ('utf-8')
               LOAD_CONST               6 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  59   L4:     END_FOR
               POP_ITER

  66           LOAD_NAME                7 (sys)
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

  69           LOAD_NAME                5 (logging)
               LOAD_ATTR               54 (getLogger)
               PUSH_NULL
               LOAD_CONST               8 ('pas.scripts.reap_pending_call_dedupe')
               CALL                     1
               STORE_NAME              28 (logger)

  72           LOAD_CONST               9 ('pas_pending_call_dedupe')
               STORE_NAME              29 (_TABLE)

  74           LOAD_SMALL_INT          24
               STORE_NAME              30 (_DEFAULT_OLDER_THAN_HOURS)

  75           LOAD_SMALL_INT           1
               STORE_NAME              31 (_MIN_OLDER_THAN_HOURS)

  76           LOAD_SMALL_INT         168
               STORE_NAME              32 (_MAX_OLDER_THAN_HOURS)

  78           LOAD_CONST              10 (1000)
               STORE_NAME              33 (_DEFAULT_LIMIT)

  79           LOAD_CONST              11 (5000)
               STORE_NAME              34 (_HARD_CAP_LIMIT)

  82           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts/reap_pending_call_dedupe.py", line 82>)
               MAKE_FUNCTION
               LOAD_CONST              13 (<code object _now_iso at 0x0000018C18038170, file "scripts/reap_pending_call_dedupe.py", line 82>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (_now_iso)

  86           LOAD_CONST              14 (<code object _get_db_safe at 0x0000018C17FF13B0, file "scripts/reap_pending_call_dedupe.py", line 86>)
               MAKE_FUNCTION
               STORE_NAME              36 (_get_db_safe)

  98           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18026030, file "scripts/reap_pending_call_dedupe.py", line 98>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _clamp at 0x0000018C18038A30, file "scripts/reap_pending_call_dedupe.py", line 98>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              37 (_clamp)

 110           LOAD_CONST              17 ('candidate_count')

 117           LOAD_SMALL_INT           0

 110           LOAD_CONST              18 ('deleted_count')

 118           LOAD_SMALL_INT           0

 110           LOAD_CONST              19 ('skipped_count')

 119           LOAD_SMALL_INT           0

 110           LOAD_CONST              20 ('failed_count')

 120           LOAD_SMALL_INT           0

 110           LOAD_CONST              21 ('warnings')

 121           LOAD_CONST               2 (None)

 110           LOAD_CONST              22 ('error_code')

 122           LOAD_CONST               2 (None)

 110           BUILD_MAP                6
               LOAD_CONST              23 (<code object __annotate__ at 0x0000018C180532D0, file "scripts/reap_pending_call_dedupe.py", line 110>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object _safe_envelope at 0x0000018C17972D90, file "scripts/reap_pending_call_dedupe.py", line 110>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              38 (_safe_envelope)

 142           LOAD_CONST              25 ('brokerage_id')

 144           LOAD_CONST               2 (None)

 142           LOAD_CONST              26 ('older_than_hours')

 145           LOAD_NAME               30 (_DEFAULT_OLDER_THAN_HOURS)

 142           LOAD_CONST              27 ('limit')

 146           LOAD_NAME               33 (_DEFAULT_LIMIT)

 142           LOAD_CONST              28 ('dry_run')

 147           LOAD_CONST              29 (True)

 142           LOAD_CONST              30 ('now')

 148           LOAD_CONST               2 (None)

 142           BUILD_MAP                5
               LOAD_CONST              31 (<code object __annotate__ at 0x0000018C18025830, file "scripts/reap_pending_call_dedupe.py", line 142>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object reap at 0x0000018C17E04B30, file "scripts/reap_pending_call_dedupe.py", line 142>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              39 (reap)

 262           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts/reap_pending_call_dedupe.py", line 262>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object _build_parser at 0x0000018C17ECE910, file "scripts/reap_pending_call_dedupe.py", line 262>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              40 (_build_parser)

 298           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts/reap_pending_call_dedupe.py", line 298>)
               MAKE_FUNCTION
               LOAD_CONST              36 (<code object _print_summary at 0x0000018C1801C9E0, file "scripts/reap_pending_call_dedupe.py", line 298>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (_print_summary)

 313           LOAD_CONST              40 ((None,))
               LOAD_CONST              37 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts/reap_pending_call_dedupe.py", line 313>)
               MAKE_FUNCTION
               LOAD_CONST              38 (<code object main at 0x0000018C181B03C0, file "scripts/reap_pending_call_dedupe.py", line 313>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              42 (main)

 337           LOAD_NAME               43 (__name__)
               LOAD_CONST              39 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 338           LOAD_NAME                7 (sys)
               LOAD_ATTR               88 (exit)
               PUSH_NULL
               LOAD_NAME               42 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 337   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  62           LOAD_NAME               20 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  63   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          278 (to L1)

  62   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts/reap_pending_call_dedupe.py", line 82>:
 82           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038170, file "scripts/reap_pending_call_dedupe.py", line 82>:
 82           RESUME                   0

 83           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object _get_db_safe at 0x0000018C17FF13B0, file "scripts/reap_pending_call_dedupe.py", line 86>:
  86           RESUME                   0

  87           NOP

  88   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

  89           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

  90           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

  91   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

  92           LOAD_CONST               2 ('reap_pending_call_dedupe db client unavailable type=')

  93           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

  92           BUILD_STRING             2

  91           CALL                     1
               POP_TOP

  95   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

  90   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026030, file "scripts/reap_pending_call_dedupe.py", line 98>:
 98           RESUME                   0
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

Disassembly of <code object _clamp at 0x0000018C18038A30, file "scripts/reap_pending_call_dedupe.py", line 98>:
  98           RESUME                   0

  99           NOP

 100   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

 103   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 104           LOAD_FAST                1 (lo)
               RETURN_VALUE

 105   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 106           LOAD_FAST                2 (hi)
               RETURN_VALUE

 107   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 101           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

 102           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 101   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C180532D0, file "scripts/reap_pending_call_dedupe.py", line 110>:
110           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

112           LOAD_CONST               2 ('str')

110           LOAD_CONST               3 ('dry_run')

113           LOAD_CONST               4 ('bool')

110           LOAD_CONST               5 ('brokerage_id')

114           LOAD_CONST               6 ('Optional[str]')

110           LOAD_CONST               7 ('older_than_hours')

115           LOAD_CONST               8 ('int')

110           LOAD_CONST               9 ('limit')

116           LOAD_CONST               8 ('int')

110           LOAD_CONST              10 ('candidate_count')

117           LOAD_CONST               8 ('int')

110           LOAD_CONST              11 ('deleted_count')

118           LOAD_CONST               8 ('int')

110           LOAD_CONST              12 ('skipped_count')

119           LOAD_CONST               8 ('int')

110           LOAD_CONST              13 ('failed_count')

120           LOAD_CONST               8 ('int')

110           LOAD_CONST              14 ('warnings')

121           LOAD_CONST              15 ('Optional[List[str]]')

110           LOAD_CONST              16 ('error_code')

122           LOAD_CONST               6 ('Optional[str]')

110           LOAD_CONST              17 ('return')

123           LOAD_CONST              18 ('Dict[str, Any]')

110           BUILD_MAP               12
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C17972D90, file "scripts/reap_pending_call_dedupe.py", line 110>:
110           RESUME                   0

125           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS172')

126           LOAD_CONST               2 ('reaper')
              LOAD_CONST               3 ('pending_call_dedupe')

127           LOAD_CONST               4 ('status')
              LOAD_FAST                0 (status)

128           LOAD_CONST               5 ('dry_run')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         1 (dry_run)
              CALL                     1

129           LOAD_CONST               6 ('brokerage_id')
              LOAD_FAST                2 (brokerage_id)

130           LOAD_CONST               7 ('older_than_hours')
              LOAD_FAST                3 (older_than_hours)

131           LOAD_CONST               8 ('limit')
              LOAD_FAST                4 (limit)

132           LOAD_CONST               9 ('candidate_count')
              LOAD_FAST                5 (candidate_count)

133           LOAD_CONST              10 ('deleted_count')
              LOAD_FAST                6 (deleted_count)

134           LOAD_CONST              11 ('skipped_count')
              LOAD_FAST                7 (skipped_count)

135           LOAD_CONST              12 ('failed_count')
              LOAD_FAST                8 (failed_count)

136           LOAD_CONST              13 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                9 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

137           LOAD_CONST              14 ('error_code')
              LOAD_FAST_BORROW        10 (error_code)

138           LOAD_CONST              15 ('generated_at')
              LOAD_GLOBAL              5 (_now_iso + NULL)
              CALL                     0

124           BUILD_MAP               14
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025830, file "scripts/reap_pending_call_dedupe.py", line 142>:
142           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

144           LOAD_CONST               2 ('Optional[str]')

142           LOAD_CONST               3 ('older_than_hours')

145           LOAD_CONST               4 ('int')

142           LOAD_CONST               5 ('limit')

146           LOAD_CONST               4 ('int')

142           LOAD_CONST               6 ('dry_run')

147           LOAD_CONST               7 ('bool')

142           LOAD_CONST               8 ('now')

148           LOAD_CONST               9 ('Optional[datetime]')

142           LOAD_CONST              10 ('return')

149           LOAD_CONST              11 ('Dict[str, Any]')

142           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object reap at 0x0000018C17E04B30, file "scripts/reap_pending_call_dedupe.py", line 142>:
 142            RESUME                   0

 154            LOAD_GLOBAL              1 (_clamp + NULL)

 155            LOAD_FAST_BORROW         1 (older_than_hours)
                LOAD_GLOBAL              2 (_MIN_OLDER_THAN_HOURS)

 156            LOAD_GLOBAL              4 (_MAX_OLDER_THAN_HOURS)
                LOAD_GLOBAL              6 (_DEFAULT_OLDER_THAN_HOURS)

 154            CALL                     4
                STORE_FAST               5 (hours)

 158            LOAD_GLOBAL              1 (_clamp + NULL)
                LOAD_FAST_BORROW         2 (limit)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              8 (_HARD_CAP_LIMIT)
                LOAD_GLOBAL             10 (_DEFAULT_LIMIT)
                CALL                     4
                STORE_FAST               6 (capped_limit)

 161            LOAD_GLOBAL             13 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_GLOBAL             14 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR               17 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L1)
                NOT_TAKEN

 160            LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR               17 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L2)

 162    L1:     LOAD_CONST               1 (None)

 159    L2:     STORE_FAST               7 (bid)

 165            LOAD_GLOBAL             13 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (now)
                LOAD_GLOBAL             18 (datetime)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       21 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (now)
                LOAD_ATTR               20 (tzinfo)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_FAST                4 (now)
                JUMP_FORWARD            35 (to L4)

 166    L3:     LOAD_GLOBAL             18 (datetime)
                LOAD_ATTR               22 (now)
                PUSH_NULL
                LOAD_GLOBAL             24 (timezone)
                LOAD_ATTR               26 (utc)
                CALL                     1

 164    L4:     STORE_FAST               8 (now_dt)

 168            LOAD_FAST_BORROW         8 (now_dt)
                LOAD_GLOBAL             29 (timedelta + NULL)
                LOAD_FAST_BORROW         5 (hours)
                LOAD_CONST               2 (('hours',))
                CALL_KW                  1
                BINARY_OP               10 (-)
                LOAD_ATTR               31 (isoformat + NULL|self)
                LOAD_CONST               3 ('seconds')
                LOAD_CONST               4 (('timespec',))
                CALL_KW                  1
                STORE_FAST               9 (cutoff_iso)

 170            LOAD_GLOBAL             33 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST              10 (db)

 171            LOAD_FAST_BORROW        10 (db)
                POP_JUMP_IF_NOT_NONE    18 (to L5)
                NOT_TAKEN

 172            LOAD_GLOBAL             35 (_safe_envelope + NULL)

 173            LOAD_CONST               5 ('skipped')

 174            LOAD_FAST_BORROW_LOAD_FAST_BORROW 55 (dry_run, bid)

 175            LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (hours, capped_limit)

 176            LOAD_CONST               6 ('durable_pending_call_dedupe_unavailable')
                BUILD_LIST               1

 177            LOAD_CONST               6 ('durable_pending_call_dedupe_unavailable')

 172            LOAD_CONST               7 (('status', 'dry_run', 'brokerage_id', 'older_than_hours', 'limit', 'warnings', 'error_code'))
                CALL_KW                  7
                RETURN_VALUE

 181    L5:     NOP

 183    L6:     LOAD_FAST_BORROW        10 (db)
                LOAD_ATTR               37 (table + NULL|self)
                LOAD_GLOBAL             38 (_TABLE)
                CALL                     1

 184            LOAD_ATTR               41 (select + NULL|self)
                LOAD_CONST               8 ('dedupe_key, brokerage_id, source, expires_at')
                CALL                     1

 185            LOAD_ATTR               43 (lt + NULL|self)
                LOAD_CONST               9 ('expires_at')
                LOAD_FAST_BORROW         9 (cutoff_iso)
                CALL                     2

 186            LOAD_ATTR               45 (order + NULL|self)
                LOAD_CONST               9 ('expires_at')
                LOAD_CONST              10 (False)
                LOAD_CONST              11 (('desc',))
                CALL_KW                  2

 187            LOAD_ATTR               47 (limit + NULL|self)
                LOAD_FAST_BORROW         6 (capped_limit)
                CALL                     1

 182            STORE_FAST              11 (query)

 189            LOAD_FAST_BORROW         7 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L9)
        L7:     NOT_TAKEN

 190    L8:     LOAD_FAST_BORROW        11 (query)
                LOAD_ATTR               49 (eq + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST_BORROW         7 (bid)
                CALL                     2
                STORE_FAST              11 (query)

 191    L9:     LOAD_FAST_BORROW        11 (query)
                LOAD_ATTR               51 (execute + NULL|self)
                CALL                     0
                STORE_FAST              12 (result)

 192            LOAD_GLOBAL             53 (list + NULL)
                LOAD_GLOBAL             55 (getattr + NULL)
                LOAD_FAST_BORROW        12 (result)
                LOAD_CONST              13 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
       L10:     NOT_TAKEN
       L11:     POP_TOP
                BUILD_LIST               0
       L12:     CALL                     1
                STORE_FAST              13 (rows)

 206   L13:     LOAD_GLOBAL             67 (len + NULL)
                LOAD_FAST               13 (rows)
                CALL                     1
                STORE_FAST              15 (candidate_count)

 208            LOAD_FAST                3 (dry_run)
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L14)
                NOT_TAKEN

 209            LOAD_GLOBAL             35 (_safe_envelope + NULL)

 210            LOAD_CONST              16 ('ok')

 211            LOAD_CONST              17 (True)
                LOAD_FAST                7 (bid)

 212            LOAD_FAST_LOAD_FAST     86 (hours, capped_limit)

 213            LOAD_FAST               15 (candidate_count)

 209            LOAD_CONST              18 (('status', 'dry_run', 'brokerage_id', 'older_than_hours', 'limit', 'candidate_count'))
                CALL_KW                  6
                RETURN_VALUE

 217   L14:     LOAD_SMALL_INT           0
                STORE_FAST              16 (deleted)

 218            LOAD_SMALL_INT           0
                STORE_FAST              17 (skipped)

 219            LOAD_SMALL_INT           0
                STORE_FAST              18 (failed)

 220            BUILD_LIST               0
                STORE_FAST              19 (warnings)

 221            LOAD_FAST               13 (rows)
                GET_ITER
       L15:     FOR_ITER               216 (to L21)
                STORE_FAST              20 (row)

 222            LOAD_GLOBAL             13 (isinstance + NULL)
                LOAD_FAST               20 (row)
                LOAD_GLOBAL             68 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L16)
                NOT_TAKEN

 223            LOAD_FAST               17 (skipped)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              17 (skipped)

 224            JUMP_BACKWARD           36 (to L15)

 225   L16:     LOAD_FAST               20 (row)
                LOAD_ATTR               71 (get + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                CALL                     1
                STORE_FAST              21 (row_bid)

 226            LOAD_FAST               20 (row)
                LOAD_ATTR               71 (get + NULL|self)
                LOAD_CONST              19 ('dedupe_key')
                CALL                     1
                STORE_FAST              22 (row_key)

 227            LOAD_GLOBAL             13 (isinstance + NULL)
                LOAD_FAST               21 (row_bid)
                LOAD_GLOBAL             14 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL             13 (isinstance + NULL)
                LOAD_FAST               22 (row_key)
                LOAD_GLOBAL             14 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L18)
                NOT_TAKEN

 228   L17:     LOAD_FAST               17 (skipped)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              17 (skipped)

 229            JUMP_BACKWARD          125 (to L15)

 230   L18:     NOP

 232   L19:     LOAD_FAST               10 (db)
                LOAD_ATTR               37 (table + NULL|self)
                LOAD_GLOBAL             38 (_TABLE)
                CALL                     1

 233            LOAD_ATTR               73 (delete + NULL|self)
                CALL                     0

 234            LOAD_ATTR               49 (eq + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST               21 (row_bid)
                CALL                     2

 235            LOAD_ATTR               49 (eq + NULL|self)
                LOAD_CONST              19 ('dedupe_key')
                LOAD_FAST               22 (row_key)
                CALL                     2

 236            LOAD_ATTR               51 (execute + NULL|self)
                CALL                     0
                POP_TOP

 238            LOAD_FAST               16 (deleted)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              16 (deleted)
       L20:     JUMP_BACKWARD          218 (to L15)

 221   L21:     END_FOR
                POP_ITER

 249            LOAD_GLOBAL             35 (_safe_envelope + NULL)

 250            LOAD_FAST               18 (failed)
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L22)
                NOT_TAKEN
                LOAD_CONST              16 ('ok')
                JUMP_FORWARD             1 (to L23)
       L22:     LOAD_CONST              22 ('partial_failure')

 251   L23:     LOAD_CONST              10 (False)
                LOAD_FAST                7 (bid)

 252            LOAD_FAST_LOAD_FAST     86 (hours, capped_limit)

 253            LOAD_FAST               15 (candidate_count)

 254            LOAD_FAST               16 (deleted)

 255            LOAD_FAST               17 (skipped)

 256            LOAD_FAST               18 (failed)

 257            LOAD_FAST               19 (warnings)

 258            LOAD_FAST               18 (failed)
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        8 (to L24)
                NOT_TAKEN
                LOAD_CONST               1 (None)

 249            LOAD_CONST              24 (('status', 'dry_run', 'brokerage_id', 'older_than_hours', 'limit', 'candidate_count', 'deleted_count', 'skipped_count', 'failed_count', 'warnings', 'error_code'))
                CALL_KW                 11
                RETURN_VALUE

 258   L24:     LOAD_CONST              23 ('reaper_partial_failure')

 249            LOAD_CONST              24 (('status', 'dry_run', 'brokerage_id', 'older_than_hours', 'limit', 'candidate_count', 'deleted_count', 'skipped_count', 'failed_count', 'warnings', 'error_code'))
                CALL_KW                 11
                RETURN_VALUE

  --   L25:     PUSH_EXC_INFO

 193            LOAD_GLOBAL             56 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       93 (to L30)
                NOT_TAKEN
                STORE_FAST              14 (e)

 194   L26:     LOAD_GLOBAL             58 (logger)
                LOAD_ATTR               61 (warning + NULL|self)

 195            LOAD_CONST              14 ('reap_pending_call_dedupe read error type=')

 196            LOAD_GLOBAL             63 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               64 (__name__)
                FORMAT_SIMPLE

 195            BUILD_STRING             2

 194            CALL                     1
                POP_TOP

 198            LOAD_GLOBAL             35 (_safe_envelope + NULL)

 199            LOAD_CONST               5 ('skipped')

 200            LOAD_FAST_LOAD_FAST     55 (dry_run, bid)

 201            LOAD_FAST_LOAD_FAST     86 (hours, capped_limit)

 202            LOAD_CONST              15 ('db_read_failed:')
                LOAD_GLOBAL             63 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               64 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 203            LOAD_CONST               6 ('durable_pending_call_dedupe_unavailable')

 198            LOAD_CONST               7 (('status', 'dry_run', 'brokerage_id', 'older_than_hours', 'limit', 'warnings', 'error_code'))
                CALL_KW                  7
       L27:     SWAP                     2
       L28:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RETURN_VALUE

  --   L29:     LOAD_CONST               1 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RERAISE                  1

 193   L30:     RERAISE                  0

  --   L31:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L32:     PUSH_EXC_INFO

 239            LOAD_GLOBAL             56 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      113 (to L37)
                NOT_TAKEN
                STORE_FAST              14 (e)

 240   L33:     LOAD_FAST               18 (failed)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              18 (failed)

 241            LOAD_CONST              20 ('db_delete_failed:')
                LOAD_GLOBAL             63 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               64 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                STORE_FAST              23 (code)

 242            LOAD_FAST               23 (code)
                LOAD_FAST               19 (warnings)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       18 (to L34)
                NOT_TAKEN

 243            LOAD_FAST               19 (warnings)
                LOAD_ATTR               75 (append + NULL|self)
                LOAD_FAST               23 (code)
                CALL                     1
                POP_TOP

 244   L34:     LOAD_GLOBAL             58 (logger)
                LOAD_ATTR               61 (warning + NULL|self)

 245            LOAD_CONST              21 ('reap_pending_call_dedupe delete error type=')

 246            LOAD_GLOBAL             63 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               64 (__name__)
                FORMAT_SIMPLE

 245            BUILD_STRING             2

 244            CALL                     1
                POP_TOP
       L35:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD          488 (to L15)

  --   L36:     LOAD_CONST               1 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RERAISE                  1

 239   L37:     RERAISE                  0

  --   L38:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L6 to L7 -> L25 [0]
  L8 to L10 -> L25 [0]
  L11 to L13 -> L25 [0]
  L19 to L20 -> L32 [1]
  L25 to L26 -> L31 [1] lasti
  L26 to L27 -> L29 [1] lasti
  L27 to L28 -> L31 [1] lasti
  L29 to L31 -> L31 [1] lasti
  L32 to L33 -> L38 [2] lasti
  L33 to L35 -> L36 [2] lasti
  L36 to L38 -> L38 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts/reap_pending_call_dedupe.py", line 262>:
262           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C17ECE910, file "scripts/reap_pending_call_dedupe.py", line 262>:
262           RESUME                   0

263           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

264           LOAD_CONST               0 ('reap_pending_call_dedupe')

266           LOAD_CONST               1 ('PAS172 — Reap expired pending-call dedupe rows from the PAS171 durable store. Dry-run by default; --execute required to delete. NEVER echoes the dedupe key. NEVER echoes raw lead context.')

263           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

272           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

273           LOAD_CONST               3 ('--brokerage-id')
              LOAD_CONST               4 (None)

274           LOAD_CONST               5 ('Scope the reap to a single brokerage (default: all brokerages).')

272           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

276           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

277           LOAD_CONST               7 ('--older-than-hours')
              LOAD_GLOBAL              6 (int)
              LOAD_GLOBAL              8 (_DEFAULT_OLDER_THAN_HOURS)

278           LOAD_CONST               8 ('Reap rows whose expires_at is older than this many hours (clamped to [')

279           LOAD_GLOBAL             10 (_MIN_OLDER_THAN_HOURS)
              FORMAT_SIMPLE
              LOAD_CONST               9 (',')
              LOAD_GLOBAL             12 (_MAX_OLDER_THAN_HOURS)
              FORMAT_SIMPLE
              LOAD_CONST              10 ('], default ')

280           LOAD_GLOBAL              8 (_DEFAULT_OLDER_THAN_HOURS)
              FORMAT_SIMPLE
              LOAD_CONST              11 (').')

278           BUILD_STRING             7

276           LOAD_CONST              12 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

282           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

283           LOAD_CONST              13 ('--limit')
              LOAD_GLOBAL              6 (int)
              LOAD_GLOBAL             14 (_DEFAULT_LIMIT)

284           LOAD_CONST              14 ('Hard cap on rows deleted per run (default ')
              LOAD_GLOBAL             14 (_DEFAULT_LIMIT)
              FORMAT_SIMPLE
              LOAD_CONST              15 (', max ')

285           LOAD_GLOBAL             16 (_HARD_CAP_LIMIT)
              FORMAT_SIMPLE
              LOAD_CONST              11 (').')

284           BUILD_STRING             5

282           LOAD_CONST              12 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

287           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

288           LOAD_CONST              16 ('--execute')
              LOAD_CONST              17 ('store_true')

289           LOAD_CONST              18 ('Actually delete rows. Without this flag the script runs in dry-run mode.')

287           LOAD_CONST              19 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

291           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

292           LOAD_CONST              20 ('--json')
              LOAD_CONST              17 ('store_true')

293           LOAD_CONST              21 ('Emit JSON on stdout instead of the human summary.')

291           LOAD_CONST              19 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

295           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts/reap_pending_call_dedupe.py", line 298>:
298           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C1801C9E0, file "scripts/reap_pending_call_dedupe.py", line 298>:
298           RESUME                   0

299           LOAD_GLOBAL              1 (print + NULL)

300           LOAD_CONST               0 ('[PAS172/reap_pending_call_dedupe] status=')

301           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               1 ('status')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' dry_run=')

302           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               3 ('dry_run')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' brokerage_id=')

303           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               5 ('brokerage_id')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' candidates=')

304           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               7 ('candidate_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' deleted=')

305           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               9 ('deleted_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' skipped=')

306           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST              11 ('skipped_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              12 (' failed=')

307           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST              13 ('failed_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

300           BUILD_STRING            14

299           CALL                     1
              POP_TOP

309           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              14 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     LOAD_CONST              15 (slice(None, 10, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               1 (w)

310           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              16 ('  warn: ')
              LOAD_FAST_BORROW         1 (w)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

309   L3:     END_FOR
              POP_ITER
              LOAD_CONST              17 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts/reap_pending_call_dedupe.py", line 313>:
313           RESUME                   0
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

Disassembly of <code object main at 0x0000018C181B03C0, file "scripts/reap_pending_call_dedupe.py", line 313>:
 313            RESUME                   0

 314            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 315            NOP

 316    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 320    L2:     LOAD_GLOBAL             11 (reap + NULL)

 321            LOAD_FAST                2 (args)
                LOAD_ATTR               12 (brokerage_id)

 322            LOAD_FAST                2 (args)
                LOAD_ATTR               14 (older_than_hours)

 323            LOAD_FAST                2 (args)
                LOAD_ATTR               16 (limit)

 324            LOAD_FAST                2 (args)
                LOAD_ATTR               18 (execute)
                TO_BOOL
                UNARY_NOT

 320            LOAD_CONST               2 (('brokerage_id', 'older_than_hours', 'limit', 'dry_run'))
                CALL_KW                  4
                STORE_FAST               4 (env)

 327            LOAD_FAST                2 (args)
                LOAD_ATTR               20 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       37 (to L3)
                NOT_TAKEN

 328            LOAD_GLOBAL             23 (print + NULL)
                LOAD_GLOBAL             20 (json)
                LOAD_ATTR               24 (dumps)
                PUSH_NULL
                LOAD_FAST                4 (env)
                LOAD_SMALL_INT           2
                LOAD_CONST               3 (True)
                LOAD_CONST               4 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 334            LOAD_SMALL_INT           0
                RETURN_VALUE

 330    L3:     LOAD_GLOBAL             27 (_print_summary + NULL)
                LOAD_FAST                4 (env)
                CALL                     1
                POP_TOP

 334            LOAD_SMALL_INT           0
                RETURN_VALUE

  --    L4:     PUSH_EXC_INFO

 317            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L13)
                NOT_TAKEN
                STORE_FAST               3 (e)

 318    L5:     LOAD_FAST                3 (e)
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

 317   L13:     RERAISE                  0

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
