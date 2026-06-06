# scripts_readiness/reap_operator_audit_log

- **pyc:** `scripts\__pycache__\reap_operator_audit_log.cpython-314.pyc`
- **expected source path (absent):** `scripts/reap_operator_audit_log.py`
- **co_filename (from bytecode):** `scripts\reap_operator_audit_log.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS175 — Operator-driven audit-log retention reaper.

Deletes aged rows from ``pas_operator_actions_log``
(PAS174 v22 + PAS175 v23). Dry-run by default; ``--execute``
required to actually delete. NEVER touches recent rows.

Doctrine:

* **Dry-run by default.** ``--execute`` is required. Mirrors
  PAS167 / PAS168 / PAS172 reaper pattern.
* **Recent-row floor.** Default retention is 90 days; the
  age clamp is ``[60, 3650]`` days at the script layer. The
  v23 SQL policy enforces a **30-day SQL floor** that no
  reaper invocation can bypass — defence-in-depth.
* **Bounded delete count.** Default 1000 per run; hard cap
  5000.
* **Structural envelopes only.** Output is JSON / human-
  friendly counts. NEVER echoes per-row payload, actor_id,
  metadata, or any PII. The reaper reports the
  ``action_ids`` of deleted rows ONLY when the caller passes
  ``--json`` (so the operator can re-verify the chain
  integrity head) — still structural, never PII.
* **DB unavailable → exit 0** with skipped envelope.
* **Bad args → exit 2.**
* **NEVER raises.**
* **No scheduler / cron added.** Operator-driven only.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `argparse`, `datetime`, `get_supabase`, `json`, `logging`, `os`, `sys`, `timedelta`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_clamp`, `_get_db_safe`, `_now_iso`, `_print_summary`, `_safe_envelope`, `main`, `reap`

## Env-key candidates

`PAS175`

## String constants (redacted where noted)

- '\nPAS175 — Operator-driven audit-log retention reaper.\n\nDeletes aged rows from ``pas_operator_actions_log``\n(PAS174 v22 + PAS175 v23). Dry-run by default; ``--execute``\nrequired to actually delete. NEVER touches recent rows.\n\nDoctrine:\n\n* **Dry-run by default.** ``--execute`` is required. Mirrors\n  PAS167 / PAS168 / PAS172 reaper pattern.\n* **Recent-row floor.** Default retention is 90 days; the\n  age clamp is ``[60, 3650]`` days at the script layer. The\n  v23 SQL policy enforces a **30-day SQL floor** that no\n  reaper invocation can bypass — defence-in-depth.\n* **Bounded delete count.** Default 1000 per run; hard cap\n  5000.\n* **Structural envelopes only.** Output is JSON / human-\n  friendly counts. NEVER echoes per-row payload, actor_id,\n  metadata, or any PII. The reaper reports the\n  ``action_ids`` of deleted rows ONLY when the caller passes\n  ``--json`` (so the operator can re-verify the chain\n  integrity head) — still structural, never PII.\n* **DB unavailable → exit 0** with skipped envelope.\n* **Bad args → exit 2.**\n* **NEVER raises.**\n* **No scheduler / cron added.** Operator-driven only.\n'
- 'utf-8'
- 'pas.scripts.reap_operator_audit_log'
- 'pas_operator_actions_log'
- 'candidate_count'
- 'deleted_count'
- 'skipped_count'
- 'failed_count'
- 'candidate_ids'
- 'warnings'
- 'error_code'
- 'older_than_days'
- 'limit'
- 'dry_run'
- 'now'
- 'return'
- 'str'
- 'seconds'
- 'reap_operator_audit_log db client unavailable type='
- 'value'
- 'Any'
- 'int'
- 'default'
- 'status'
- 'bool'
- 'Optional[List[str]]'
- 'Optional[str]'
- 'Dict[str, Any]'
- 'phase'
- 'PAS175'
- 'reaper'
- 'operator_audit_log'
- 'candidate_action_ids'
- 'generated_at'
- 'Optional[datetime]'
- 'Reap rows older than ``older_than_days`` from the\noperator audit log. NEVER raises.'
- 'skipped'
- 'audit_store_unavailable'
- 'action_id, occurred_at'
- 'occurred_at'
- 'data'
- 'reap_operator_audit_log read error type='
- 'db_read_failed:'
- 'action_id'
- 'db_delete_failed:'
- 'reap_operator_audit_log delete error type='
- 'partial_failure'
- 'reaper_partial_failure'
- 'argparse.ArgumentParser'
- 'reap_operator_audit_log'
- 'PAS175 — Reap aged rows from pas_operator_actions_log. Dry-run by default; --execute required. v23 SQL policy enforces a 30-day floor; the script clamps to 60 days minimum.'
- '--older-than-days'
- 'Reap rows older than this many days (clamped to ['
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
- '[PAS175/reap_operator_audit_log] status='
- ' dry_run='
- ' older_than_days='
- ' candidates='
- ' deleted='
- ' skipped='
- ' failed='
- '  warn: '
- 'argv'

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ('\nPAS175 — Operator-driven audit-log retention reaper.\n\nDeletes aged rows from ``pas_operator_actions_log``\n(PAS174 v22 + PAS175 v23). Dry-run by default; ``--execute``\nrequired to actually delete. NEVER touches recent rows.\n\nDoctrine:\n\n* **Dry-run by default.** ``--execute`` is required. Mirrors\n  PAS167 / PAS168 / PAS172 reaper pattern.\n* **Recent-row floor.** Default retention is 90 days; the\n  age clamp is ``[60, 3650]`` days at the script layer. The\n  v23 SQL policy enforces a **30-day SQL floor** that no\n  reaper invocation can bypass — defence-in-depth.\n* **Bounded delete count.** Default 1000 per run; hard cap\n  5000.\n* **Structural envelopes only.** Output is JSON / human-\n  friendly counts. NEVER echoes per-row payload, actor_id,\n  metadata, or any PII. The reaper reports the\n  ``action_ids`` of deleted rows ONLY when the caller passes\n  ``--json`` (so the operator can re-verify the chain\n  integrity head) — still structural, never PII.\n* **DB unavailable → exit 0** with skipped envelope.\n* **Bad args → exit 2.**\n* **NEVER raises.**\n* **No scheduler / cron added.** Operator-driven only.\n')
               STORE_NAME               0 (__doc__)

  30           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  32           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  33           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  34           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (logging)
               STORE_NAME               5 (logging)

  35           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (os)
               STORE_NAME               6 (os)

  36           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (sys)
               STORE_NAME               7 (sys)

  37           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timedelta', 'timezone'))
               IMPORT_NAME              8 (datetime)
               IMPORT_FROM              8 (datetime)
               STORE_NAME               8 (datetime)
               IMPORT_FROM              9 (timedelta)
               STORE_NAME               9 (timedelta)
               IMPORT_FROM             10 (timezone)
               STORE_NAME              10 (timezone)
               POP_TOP

  38           LOAD_SMALL_INT           0
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

  41           LOAD_NAME                7 (sys)
               LOAD_ATTR               32 (stdout)
               LOAD_NAME                7 (sys)
               LOAD_ATTR               34 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              18 (_stream)

  42           NOP

  43   L2:     LOAD_NAME               18 (_stream)
               LOAD_ATTR               39 (reconfigure + NULL|self)
               LOAD_CONST               5 ('utf-8')
               LOAD_CONST               6 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  41   L4:     END_FOR
               POP_ITER

  48           LOAD_NAME                7 (sys)
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

  51           LOAD_NAME                5 (logging)
               LOAD_ATTR               54 (getLogger)
               PUSH_NULL
               LOAD_CONST               8 ('pas.scripts.reap_operator_audit_log')
               CALL                     1
               STORE_NAME              28 (logger)

  54           LOAD_CONST               9 ('pas_operator_actions_log')
               STORE_NAME              29 (_TABLE)

  58           LOAD_SMALL_INT          90
               STORE_NAME              30 (_DEFAULT_OLDER_THAN_DAYS)

  59           LOAD_SMALL_INT          60
               STORE_NAME              31 (_MIN_OLDER_THAN_DAYS)

  60           LOAD_CONST              40 (3650)
               STORE_NAME              32 (_MAX_OLDER_THAN_DAYS)

  62           LOAD_CONST              10 (1000)
               STORE_NAME              33 (_DEFAULT_LIMIT)

  63           LOAD_CONST              11 (5000)
               STORE_NAME              34 (_HARD_CAP_LIMIT)

  66           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts\reap_operator_audit_log.py", line 66>)
               MAKE_FUNCTION
               LOAD_CONST              13 (<code object _now_iso at 0x0000018C180388F0, file "scripts\reap_operator_audit_log.py", line 66>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (_now_iso)

  70           LOAD_CONST              14 (<code object _get_db_safe at 0x0000018C17FF0DB0, file "scripts\reap_operator_audit_log.py", line 70>)
               MAKE_FUNCTION
               STORE_NAME              36 (_get_db_safe)

  82           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18026130, file "scripts\reap_operator_audit_log.py", line 82>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _clamp at 0x0000018C18038CB0, file "scripts\reap_operator_audit_log.py", line 82>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              37 (_clamp)

  94           LOAD_CONST              17 ('candidate_count')

 100           LOAD_SMALL_INT           0

  94           LOAD_CONST              18 ('deleted_count')

 101           LOAD_SMALL_INT           0

  94           LOAD_CONST              19 ('skipped_count')

 102           LOAD_SMALL_INT           0

  94           LOAD_CONST              20 ('failed_count')

 103           LOAD_SMALL_INT           0

  94           LOAD_CONST              21 ('candidate_ids')

 104           LOAD_CONST               2 (None)

  94           LOAD_CONST              22 ('warnings')

 105           LOAD_CONST               2 (None)

  94           LOAD_CONST              23 ('error_code')

 106           LOAD_CONST               2 (None)

  94           BUILD_MAP                7
               LOAD_CONST              24 (<code object __annotate__ at 0x0000018C18053090, file "scripts\reap_operator_audit_log.py", line 94>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object _safe_envelope at 0x0000018C17FF0C30, file "scripts\reap_operator_audit_log.py", line 94>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              38 (_safe_envelope)

 126           LOAD_CONST              26 ('older_than_days')

 128           LOAD_NAME               30 (_DEFAULT_OLDER_THAN_DAYS)

 126           LOAD_CONST              27 ('limit')

 129           LOAD_NAME               33 (_DEFAULT_LIMIT)

 126           LOAD_CONST              28 ('dry_run')

 130           LOAD_CONST              29 (True)

 126           LOAD_CONST              30 ('now')

 131           LOAD_CONST               2 (None)

 126           BUILD_MAP                4
               LOAD_CONST              31 (<code object __annotate__ at 0x0000018C18024B30, file "scripts\reap_operator_audit_log.py", line 126>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object reap at 0x0000018C17F6C2B0, file "scripts\reap_operator_audit_log.py", line 126>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              39 (reap)

 244           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts\reap_operator_audit_log.py", line 244>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object _build_parser at 0x0000018C17EC46C0, file "scripts\reap_operator_audit_log.py", line 244>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              40 (_build_parser)

 276           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts\reap_operator_audit_log.py", line 276>)
               MAKE_FUNCTION
               LOAD_CONST              36 (<code object _print_summary at 0x0000018C179A7290, file "scripts\reap_operator_audit_log.py", line 276>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (_print_summary)

 291           LOAD_CONST              41 ((None,))
               LOAD_CONST              37 (<code object __annotate__ at 0x0000018C17FA3D20, file "scripts\reap_operator_audit_log.py", line 291>)
               MAKE_FUNCTION
               LOAD_CONST              38 (<code object main at 0x0000018C17CD07C0, file "scripts\reap_operator_audit_log.py", line 291>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              42 (main)

 312           LOAD_NAME               43 (__name__)
               LOAD_CONST              39 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 313           LOAD_NAME                7 (sys)
               LOAD_ATTR               88 (exit)
               PUSH_NULL
               LOAD_NAME               42 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 312   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  44           LOAD_NAME               20 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  45   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          278 (to L1)

  44   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts\reap_operator_audit_log.py", line 66>:
 66           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C180388F0, file "scripts\reap_operator_audit_log.py", line 66>:
 66           RESUME                   0

 67           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object _get_db_safe at 0x0000018C17FF0DB0, file "scripts\reap_operator_audit_log.py", line 70>:
  70           RESUME                   0

  71           NOP

  72   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

  73           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

  74           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

  75   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

  76           LOAD_CONST               2 ('reap_operator_audit_log db client unavailable type=')

  77           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

  76           BUILD_STRING             2

  75           CALL                     1
               POP_TOP

  79   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

  74   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026130, file "scripts\reap_operator_audit_log.py", line 82>:
 82           RESUME                   0
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

Disassembly of <code object _clamp at 0x0000018C18038CB0, file "scripts\reap_operator_audit_log.py", line 82>:
  82           RESUME                   0

  83           NOP

  84   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

  87   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

  88           LOAD_FAST                1 (lo)
               RETURN_VALUE

  89   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

  90           LOAD_FAST                2 (hi)
               RETURN_VALUE

  91   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

  85           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

  86           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

  85   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18053090, file "scripts\reap_operator_audit_log.py", line 94>:
 94           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

 96           LOAD_CONST               2 ('str')

 94           LOAD_CONST               3 ('dry_run')

 97           LOAD_CONST               4 ('bool')

 94           LOAD_CONST               5 ('older_than_days')

 98           LOAD_CONST               6 ('int')

 94           LOAD_CONST               7 ('limit')

 99           LOAD_CONST               6 ('int')

 94           LOAD_CONST               8 ('candidate_count')

100           LOAD_CONST               6 ('int')

 94           LOAD_CONST               9 ('deleted_count')

101           LOAD_CONST               6 ('int')

 94           LOAD_CONST              10 ('skipped_count')

102           LOAD_CONST               6 ('int')

 94           LOAD_CONST              11 ('failed_count')

103           LOAD_CONST               6 ('int')

 94           LOAD_CONST              12 ('candidate_ids')

104           LOAD_CONST              13 ('Optional[List[str]]')

 94           LOAD_CONST              14 ('warnings')

105           LOAD_CONST              13 ('Optional[List[str]]')

 94           LOAD_CONST              15 ('error_code')

106           LOAD_CONST              16 ('Optional[str]')

 94           LOAD_CONST              17 ('return')

107           LOAD_CONST              18 ('Dict[str, Any]')

 94           BUILD_MAP               12
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C17FF0C30, file "scripts\reap_operator_audit_log.py", line 94>:
 94           RESUME                   0

109           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS175')

110           LOAD_CONST               2 ('reaper')
              LOAD_CONST               3 ('operator_audit_log')

111           LOAD_CONST               4 ('status')
              LOAD_FAST                0 (status)

112           LOAD_CONST               5 ('dry_run')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         1 (dry_run)
              CALL                     1

113           LOAD_CONST               6 ('older_than_days')
              LOAD_FAST                2 (older_than_days)

114           LOAD_CONST               7 ('limit')
              LOAD_FAST                3 (limit)

115           LOAD_CONST               8 ('candidate_count')
              LOAD_FAST                4 (candidate_count)

116           LOAD_CONST               9 ('deleted_count')
              LOAD_FAST                5 (deleted_count)

117           LOAD_CONST              10 ('skipped_count')
              LOAD_FAST                6 (skipped_count)

118           LOAD_CONST              11 ('failed_count')
              LOAD_FAST                7 (failed_count)

119           LOAD_CONST              12 ('candidate_action_ids')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                8 (candidate_ids)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

120           LOAD_CONST              13 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                9 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L2:     CALL                     1

121           LOAD_CONST              14 ('error_code')
              LOAD_FAST_BORROW        10 (error_code)

122           LOAD_CONST              15 ('generated_at')
              LOAD_GLOBAL              5 (_now_iso + NULL)
              CALL                     0

108           BUILD_MAP               14
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "scripts\reap_operator_audit_log.py", line 126>:
126           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('older_than_days')

128           LOAD_CONST               2 ('int')

126           LOAD_CONST               3 ('limit')

129           LOAD_CONST               2 ('int')

126           LOAD_CONST               4 ('dry_run')

130           LOAD_CONST               5 ('bool')

126           LOAD_CONST               6 ('now')

131           LOAD_CONST               7 ('Optional[datetime]')

126           LOAD_CONST               8 ('return')

132           LOAD_CONST               9 ('Dict[str, Any]')

126           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object reap at 0x0000018C17F6C2B0, file "scripts\reap_operator_audit_log.py", line 126>:
 126            RESUME                   0

 135            LOAD_GLOBAL              1 (_clamp + NULL)

 136            LOAD_FAST_BORROW         0 (older_than_days)
                LOAD_GLOBAL              2 (_MIN_OLDER_THAN_DAYS)

 137            LOAD_GLOBAL              4 (_MAX_OLDER_THAN_DAYS)
                LOAD_GLOBAL              6 (_DEFAULT_OLDER_THAN_DAYS)

 135            CALL                     4
                STORE_FAST               4 (days)

 139            LOAD_GLOBAL              1 (_clamp + NULL)
                LOAD_FAST_BORROW         1 (limit)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              8 (_HARD_CAP_LIMIT)
                LOAD_GLOBAL             10 (_DEFAULT_LIMIT)
                CALL                     4
                STORE_FAST               5 (capped_limit)

 141            LOAD_GLOBAL             13 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (now)
                LOAD_GLOBAL             14 (datetime)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       21 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (now)
                LOAD_ATTR               16 (tzinfo)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L1)
                NOT_TAKEN
                LOAD_FAST                3 (now)
                JUMP_FORWARD            35 (to L2)

 142    L1:     LOAD_GLOBAL             14 (datetime)
                LOAD_ATTR               18 (now)
                PUSH_NULL
                LOAD_GLOBAL             20 (timezone)
                LOAD_ATTR               22 (utc)
                CALL                     1

 140    L2:     STORE_FAST               6 (now_dt)

 144            LOAD_FAST_BORROW         6 (now_dt)
                LOAD_GLOBAL             25 (timedelta + NULL)
                LOAD_FAST_BORROW         4 (days)
                LOAD_CONST               1 (('days',))
                CALL_KW                  1
                BINARY_OP               10 (-)
                LOAD_ATTR               27 (isoformat + NULL|self)
                LOAD_CONST               2 ('seconds')
                LOAD_CONST               3 (('timespec',))
                CALL_KW                  1
                STORE_FAST               7 (cutoff_iso)

 146            LOAD_GLOBAL             29 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               8 (db)

 147            LOAD_FAST_BORROW         8 (db)
                POP_JUMP_IF_NOT_NONE    18 (to L3)
                NOT_TAKEN

 148            LOAD_GLOBAL             31 (_safe_envelope + NULL)

 149            LOAD_CONST               5 ('skipped')

 150            LOAD_FAST_BORROW         2 (dry_run)

 151            LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (days, capped_limit)

 152            LOAD_CONST               6 ('audit_store_unavailable')
                BUILD_LIST               1

 153            LOAD_CONST               6 ('audit_store_unavailable')

 148            LOAD_CONST               7 (('status', 'dry_run', 'older_than_days', 'limit', 'warnings', 'error_code'))
                CALL_KW                  6
                RETURN_VALUE

 157    L3:     NOP

 159    L4:     LOAD_FAST_BORROW         8 (db)
                LOAD_ATTR               33 (table + NULL|self)
                LOAD_GLOBAL             34 (_TABLE)
                CALL                     1

 160            LOAD_ATTR               37 (select + NULL|self)
                LOAD_CONST               8 ('action_id, occurred_at')
                CALL                     1

 161            LOAD_ATTR               39 (lt + NULL|self)
                LOAD_CONST               9 ('occurred_at')
                LOAD_FAST_BORROW         7 (cutoff_iso)
                CALL                     2

 162            LOAD_ATTR               41 (order + NULL|self)
                LOAD_CONST               9 ('occurred_at')
                LOAD_CONST              10 (False)
                LOAD_CONST              11 (('desc',))
                CALL_KW                  2

 163            LOAD_ATTR               43 (limit + NULL|self)
                LOAD_FAST_BORROW         5 (capped_limit)
                CALL                     1

 164            LOAD_ATTR               45 (execute + NULL|self)
                CALL                     0

 158            STORE_FAST               9 (result)

 166            LOAD_GLOBAL             47 (list + NULL)
                LOAD_GLOBAL             49 (getattr + NULL)
                LOAD_FAST_BORROW         9 (result)
                LOAD_CONST              12 ('data')
                LOAD_CONST               4 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                BUILD_LIST               0
        L7:     CALL                     1
                STORE_FAST              10 (rows)

 180    L8:     LOAD_GLOBAL             61 (len + NULL)
                LOAD_FAST               10 (rows)
                CALL                     1
                STORE_FAST              12 (candidate_count)

 182            LOAD_FAST               10 (rows)
                GET_ITER

 181            LOAD_FAST_AND_CLEAR     13 (r)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 182   L10:     FOR_ITER                75 (to L15)
                STORE_FAST              13 (r)

 183            LOAD_GLOBAL             13 (isinstance + NULL)
                LOAD_FAST               13 (r)
                LOAD_GLOBAL             62 (dict)
                CALL                     2
                TO_BOOL

 182   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L10)

 183   L12:     LOAD_GLOBAL             13 (isinstance + NULL)
                LOAD_FAST               13 (r)
                LOAD_ATTR               65 (get + NULL|self)
                LOAD_CONST              15 ('action_id')
                CALL                     1
                LOAD_GLOBAL             66 (str)
                CALL                     2
                TO_BOOL

 182   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           66 (to L10)
       L14:     LOAD_FAST               13 (r)
                LOAD_CONST              15 ('action_id')
                BINARY_OP               26 ([])
                LIST_APPEND              2
                JUMP_BACKWARD           77 (to L10)
       L15:     END_FOR
                POP_ITER

 181   L16:     STORE_FAST              14 (candidate_ids)
                STORE_FAST              13 (r)

 186            LOAD_FAST                2 (dry_run)
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L17)
                NOT_TAKEN

 187            LOAD_GLOBAL             31 (_safe_envelope + NULL)

 188            LOAD_CONST              16 ('ok')

 189            LOAD_CONST              17 (True)

 190            LOAD_FAST_LOAD_FAST     69 (days, capped_limit)

 191            LOAD_FAST               12 (candidate_count)

 192            LOAD_FAST               14 (candidate_ids)

 187            LOAD_CONST              18 (('status', 'dry_run', 'older_than_days', 'limit', 'candidate_count', 'candidate_ids'))
                CALL_KW                  6
                RETURN_VALUE

 195   L17:     LOAD_SMALL_INT           0
                STORE_FAST              15 (deleted)

 196            LOAD_SMALL_INT           0
                STORE_FAST              16 (skipped)

 197            LOAD_SMALL_INT           0
                STORE_FAST              17 (failed)

 198            BUILD_LIST               0
                STORE_FAST              18 (warnings)

 199            LOAD_FAST               10 (rows)
                GET_ITER
       L18:     FOR_ITER               161 (to L23)
                STORE_FAST              19 (row)

 200            LOAD_GLOBAL             13 (isinstance + NULL)
                LOAD_FAST               19 (row)
                LOAD_GLOBAL             62 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L19)
                NOT_TAKEN

 201            LOAD_FAST               16 (skipped)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              16 (skipped)

 202            JUMP_BACKWARD           36 (to L18)

 203   L19:     LOAD_FAST               19 (row)
                LOAD_ATTR               65 (get + NULL|self)
                LOAD_CONST              15 ('action_id')
                CALL                     1
                STORE_FAST              20 (aid)

 204            LOAD_GLOBAL             13 (isinstance + NULL)
                LOAD_FAST               20 (aid)
                LOAD_GLOBAL             66 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L20)
                NOT_TAKEN

 205            LOAD_FAST               16 (skipped)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              16 (skipped)

 206            JUMP_BACKWARD           86 (to L18)

 207   L20:     NOP

 214   L21:     LOAD_FAST                8 (db)
                LOAD_ATTR               33 (table + NULL|self)
                LOAD_GLOBAL             34 (_TABLE)
                CALL                     1

 215            LOAD_ATTR               69 (delete + NULL|self)
                CALL                     0

 216            LOAD_ATTR               71 (eq + NULL|self)
                LOAD_CONST              15 ('action_id')
                LOAD_FAST               20 (aid)
                CALL                     2

 217            LOAD_ATTR               45 (execute + NULL|self)
                CALL                     0
                POP_TOP

 219            LOAD_FAST               15 (deleted)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              15 (deleted)
       L22:     JUMP_BACKWARD          163 (to L18)

 199   L23:     END_FOR
                POP_ITER

 230            LOAD_GLOBAL             31 (_safe_envelope + NULL)

 231            LOAD_FAST               17 (failed)
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L24)
                NOT_TAKEN
                LOAD_CONST              16 ('ok')
                JUMP_FORWARD             1 (to L25)
       L24:     LOAD_CONST              21 ('partial_failure')

 232   L25:     LOAD_CONST              10 (False)

 233            LOAD_FAST_LOAD_FAST     69 (days, capped_limit)

 234            LOAD_FAST               12 (candidate_count)

 235            LOAD_FAST               15 (deleted)

 236            LOAD_FAST               16 (skipped)

 237            LOAD_FAST               17 (failed)

 238            LOAD_FAST               14 (candidate_ids)

 239            LOAD_FAST               18 (warnings)

 240            LOAD_FAST               17 (failed)
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        8 (to L26)
                NOT_TAKEN
                LOAD_CONST               4 (None)

 230            LOAD_CONST              23 (('status', 'dry_run', 'older_than_days', 'limit', 'candidate_count', 'deleted_count', 'skipped_count', 'failed_count', 'candidate_ids', 'warnings', 'error_code'))
                CALL_KW                 11
                RETURN_VALUE

 240   L26:     LOAD_CONST              22 ('reaper_partial_failure')

 230            LOAD_CONST              23 (('status', 'dry_run', 'older_than_days', 'limit', 'candidate_count', 'deleted_count', 'skipped_count', 'failed_count', 'candidate_ids', 'warnings', 'error_code'))
                CALL_KW                 11
                RETURN_VALUE

  --   L27:     PUSH_EXC_INFO

 167            LOAD_GLOBAL             50 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       93 (to L32)
                NOT_TAKEN
                STORE_FAST              11 (e)

 168   L28:     LOAD_GLOBAL             52 (logger)
                LOAD_ATTR               55 (warning + NULL|self)

 169            LOAD_CONST              13 ('reap_operator_audit_log read error type=')

 170            LOAD_GLOBAL             57 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               58 (__name__)
                FORMAT_SIMPLE

 169            BUILD_STRING             2

 168            CALL                     1
                POP_TOP

 172            LOAD_GLOBAL             31 (_safe_envelope + NULL)

 173            LOAD_CONST               5 ('skipped')

 174            LOAD_FAST                2 (dry_run)

 175            LOAD_FAST_LOAD_FAST     69 (days, capped_limit)

 176            LOAD_CONST              14 ('db_read_failed:')
                LOAD_GLOBAL             57 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               58 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 177            LOAD_CONST               6 ('audit_store_unavailable')

 172            LOAD_CONST               7 (('status', 'dry_run', 'older_than_days', 'limit', 'warnings', 'error_code'))
                CALL_KW                  6
       L29:     SWAP                     2
       L30:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RETURN_VALUE

  --   L31:     LOAD_CONST               4 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 167   L32:     RERAISE                  0

  --   L33:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L34:     SWAP                     2
                POP_TOP

 181            SWAP                     2
                STORE_FAST              13 (r)
                RERAISE                  0

  --   L35:     PUSH_EXC_INFO

 220            LOAD_GLOBAL             50 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      113 (to L40)
                NOT_TAKEN
                STORE_FAST              11 (e)

 221   L36:     LOAD_FAST               17 (failed)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              17 (failed)

 222            LOAD_CONST              19 ('db_delete_failed:')
                LOAD_GLOBAL             57 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               58 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                STORE_FAST              21 (code)

 223            LOAD_FAST               21 (code)
                LOAD_FAST               18 (warnings)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       18 (to L37)
                NOT_TAKEN

 224            LOAD_FAST               18 (warnings)
                LOAD_ATTR               73 (append + NULL|self)
                LOAD_FAST               21 (code)
                CALL                     1
                POP_TOP

 225   L37:     LOAD_GLOBAL             52 (logger)
                LOAD_ATTR               55 (warning + NULL|self)

 226            LOAD_CONST              20 ('reap_operator_audit_log delete error type=')

 227            LOAD_GLOBAL             57 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               58 (__name__)
                FORMAT_SIMPLE

 226            BUILD_STRING             2

 225            CALL                     1
                POP_TOP
       L38:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD          438 (to L18)

  --   L39:     LOAD_CONST               4 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 220   L40:     RERAISE                  0

  --   L41:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L27 [0]
  L6 to L8 -> L27 [0]
  L9 to L11 -> L34 [2]
  L12 to L13 -> L34 [2]
  L14 to L16 -> L34 [2]
  L21 to L22 -> L35 [1]
  L27 to L28 -> L33 [1] lasti
  L28 to L29 -> L31 [1] lasti
  L29 to L30 -> L33 [1] lasti
  L31 to L33 -> L33 [1] lasti
  L35 to L36 -> L41 [2] lasti
  L36 to L38 -> L39 [2] lasti
  L39 to L41 -> L41 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts\reap_operator_audit_log.py", line 244>:
244           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C17EC46C0, file "scripts\reap_operator_audit_log.py", line 244>:
244           RESUME                   0

245           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

246           LOAD_CONST               0 ('reap_operator_audit_log')

248           LOAD_CONST               1 ('PAS175 — Reap aged rows from pas_operator_actions_log. Dry-run by default; --execute required. v23 SQL policy enforces a 30-day floor; the script clamps to 60 days minimum.')

245           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

254           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

255           LOAD_CONST               3 ('--older-than-days')
              LOAD_GLOBAL              6 (int)
              LOAD_GLOBAL              8 (_DEFAULT_OLDER_THAN_DAYS)

256           LOAD_CONST               4 ('Reap rows older than this many days (clamped to [')

257           LOAD_GLOBAL             10 (_MIN_OLDER_THAN_DAYS)
              FORMAT_SIMPLE
              LOAD_CONST               5 (',')
              LOAD_GLOBAL             12 (_MAX_OLDER_THAN_DAYS)
              FORMAT_SIMPLE
              LOAD_CONST               6 ('], default ')

258           LOAD_GLOBAL              8 (_DEFAULT_OLDER_THAN_DAYS)
              FORMAT_SIMPLE
              LOAD_CONST               7 (').')

256           BUILD_STRING             7

254           LOAD_CONST               8 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

260           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

261           LOAD_CONST               9 ('--limit')
              LOAD_GLOBAL              6 (int)
              LOAD_GLOBAL             14 (_DEFAULT_LIMIT)

262           LOAD_CONST              10 ('Hard cap on rows deleted per run (default ')

263           LOAD_GLOBAL             14 (_DEFAULT_LIMIT)
              FORMAT_SIMPLE
              LOAD_CONST              11 (', max ')
              LOAD_GLOBAL             16 (_HARD_CAP_LIMIT)
              FORMAT_SIMPLE
              LOAD_CONST               7 (').')

262           BUILD_STRING             5

260           LOAD_CONST               8 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

265           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

266           LOAD_CONST              12 ('--execute')
              LOAD_CONST              13 ('store_true')

267           LOAD_CONST              14 ('Actually delete rows. Without this flag the script runs in dry-run mode.')

265           LOAD_CONST              15 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

269           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

270           LOAD_CONST              16 ('--json')
              LOAD_CONST              13 ('store_true')

271           LOAD_CONST              17 ('Emit JSON on stdout instead of the human summary.')

269           LOAD_CONST              15 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

273           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts\reap_operator_audit_log.py", line 276>:
276           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C179A7290, file "scripts\reap_operator_audit_log.py", line 276>:
276           RESUME                   0

277           LOAD_GLOBAL              1 (print + NULL)

278           LOAD_CONST               0 ('[PAS175/reap_operator_audit_log] status=')

279           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               1 ('status')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' dry_run=')

280           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               3 ('dry_run')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' older_than_days=')

281           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               5 ('older_than_days')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' candidates=')

282           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               7 ('candidate_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' deleted=')

283           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               9 ('deleted_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' skipped=')

284           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST              11 ('skipped_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              12 (' failed=')

285           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST              13 ('failed_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

278           BUILD_STRING            14

277           CALL                     1
              POP_TOP

287           LOAD_FAST_BORROW         0 (env)
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

288           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              16 ('  warn: ')
              LOAD_FAST_BORROW         1 (w)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

287   L3:     END_FOR
              POP_ITER
              LOAD_CONST              17 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "scripts\reap_operator_audit_log.py", line 291>:
291           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17CD07C0, file "scripts\reap_operator_audit_log.py", line 291>:
 291            RESUME                   0

 292            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 293            NOP

 294    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 298    L2:     LOAD_GLOBAL             11 (reap + NULL)

 299            LOAD_FAST                2 (args)
                LOAD_ATTR               12 (older_than_days)

 300            LOAD_FAST                2 (args)
                LOAD_ATTR               14 (limit)

 301            LOAD_FAST                2 (args)
                LOAD_ATTR               16 (execute)
                TO_BOOL
                UNARY_NOT

 298            LOAD_CONST               2 (('older_than_days', 'limit', 'dry_run'))
                CALL_KW                  3
                STORE_FAST               4 (env)

 304            LOAD_FAST                2 (args)
                LOAD_ATTR               18 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       37 (to L3)
                NOT_TAKEN

 305            LOAD_GLOBAL             21 (print + NULL)
                LOAD_GLOBAL             18 (json)
                LOAD_ATTR               22 (dumps)
                PUSH_NULL
                LOAD_FAST                4 (env)
                LOAD_SMALL_INT           2
                LOAD_CONST               3 (True)
                LOAD_CONST               4 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 309            LOAD_SMALL_INT           0
                RETURN_VALUE

 307    L3:     LOAD_GLOBAL             25 (_print_summary + NULL)
                LOAD_FAST                4 (env)
                CALL                     1
                POP_TOP

 309            LOAD_SMALL_INT           0
                RETURN_VALUE

  --    L4:     PUSH_EXC_INFO

 295            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L13)
                NOT_TAKEN
                STORE_FAST               3 (e)

 296    L5:     LOAD_FAST                3 (e)
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

 295   L13:     RERAISE                  0

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
