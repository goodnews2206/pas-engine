# scripts_readiness/backfill_operator_audit_hashes

- **pyc:** `scripts\__pycache__\backfill_operator_audit_hashes.cpython-314.pyc`
- **expected source path (absent):** `scripts/backfill_operator_audit_hashes.py`
- **co_filename (from bytecode):** `scripts\backfill_operator_audit_hashes.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS176 — Pre-v23 audit-row hash backfill (operator-driven).

Computes ``prev_hash`` + ``row_hash`` for audit rows that
landed BEFORE the PAS175 v23 migration added the hash
columns. Dry-run by default; ``--execute`` required to
write. ``--force`` permitted but PAS176's v24 SQL policy
refuses force-overwrites — see operator notes below.

Doctrine:

* **Dry-run by default.** ``--execute`` required.
* **Null-only by default.** The v24 SQL policy
  ``pas_operator_actions_log_service_role_null_only_update``
  allows UPDATE only when ``row_hash IS NULL``. Already-
  hashed rows are NEVER touched by the default backfill.
* **--force is honoured at the script layer but the SQL
  layer refuses force-overwrites in PAS176.** Operators
  who genuinely need to rewrite existing hashes must
  promote an additional one-shot UPDATE policy NOT shipped
  in v24. The script logs the attempt and surfaces the
  SQL failure as a structural warning.
* **NEVER rewrites the audit row's content.** Only the
  hash columns. The canonical row fields (action_id,
  occurred_at, brokerage_id, actor_type, actor_id, action,
  target_type, target_id, status, warning_count,
  metadata) are read but never modified.
* **NEVER raises.**
* **DB unavailable → exit 0** with skipped envelope.
* **Bad args → exit 2.**
* **No autonomous remediation.** The backfill is a one-shot
  operator action; no scheduler / cron / startup hook.

Usage:

    # Dry-run; report which rows lack hashes.
    python scripts/backfill_operator_audit_hashes.py

    # Compute + write hashes for null rows.
    python scripts/backfill_operator_audit_hashes.py --execute

    # Attempt to overwrite existing hashes (will fail at v24
    # SQL layer unless the operator separately promoted the
    # force-update policy).
    python scripts/backfill_operator_audit_hashes.py --execute --force
```

## Imports

`Any`, `Dict`, `GENESIS_HASH`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `app.services.operator.audit_integrity`, `argparse`, `compute_row_hash`, `datetime`, `get_supabase`, `json`, `logging`, `os`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_clamp`, `_get_db_safe`, `_now_iso`, `_print_summary`, `_safe_envelope`, `backfill`, `main`

## Env-key candidates

`PAS176`

## String constants (redacted where noted)

- "\nPAS176 — Pre-v23 audit-row hash backfill (operator-driven).\n\nComputes ``prev_hash`` + ``row_hash`` for audit rows that\nlanded BEFORE the PAS175 v23 migration added the hash\ncolumns. Dry-run by default; ``--execute`` required to\nwrite. ``--force`` permitted but PAS176's v24 SQL policy\nrefuses force-overwrites — see operator notes below.\n\nDoctrine:\n\n* **Dry-run by default.** ``--execute`` required.\n* **Null-only by default.** The v24 SQL policy\n  ``pas_operator_actions_log_service_role_null_only_update``\n  allows UPDATE only when ``row_hash IS NULL``. Already-\n  hashed rows are NEVER touched by the default backfill.\n* **--force is honoured at the script layer but the SQL\n  layer refuses force-overwrites in PAS176.** Operators\n  who genuinely need to rewrite existing hashes must\n  promote an additional one-shot UPDATE policy NOT shipped\n  in v24. The script logs the attempt and surfaces the\n  SQL failure as a structural warning.\n* **NEVER rewrites the audit row's content.** Only the\n  hash columns. The canonical row fields (action_id,\n  occurred_at, brokerage_id, actor_type, actor_id, action,\n  target_type, target_id, status, warning_count,\n  metadata) are read but never modified.\n* **NEVER raises.**\n* **DB unavailable → exit 0** with skipped envelope.\n* **Bad args → exit 2.**\n* **No autonomous remediation.** The backfill is a one-shot\n  operator action; no scheduler / cron / startup hook.\n\nUsage:\n\n    # Dry-run; report which rows lack hashes.\n    python scripts/backfill_operator_audit_hashes.py\n\n    # Compute + write hashes for null rows.\n    python scripts/backfill_operator_audit_hashes.py --execute\n\n    # Attempt to overwrite existing hashes (will fail at v24\n    # SQL layer unless the operator separately promoted the\n    # force-update policy).\n    python scripts/backfill_operator_audit_hashes.py --execute --force\n"
- 'utf-8'
- 'pas.scripts.backfill_operator_audit_hashes'
- 'pas_operator_actions_log'
- 'candidate_count'
- 'written_count'
- 'skipped_count'
- 'failed_count'
- 'warnings'
- 'error_code'
- 'limit'
- 'dry_run'
- 'force'
- 'return'
- 'str'
- 'seconds'
- 'backfill_operator_audit_hashes db client unavailable type='
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
- 'PAS176'
- 'backfill'
- 'operator_audit_hashes'
- 'generated_at'
- 'Backfill prev_hash + row_hash for audit rows that\ncurrently lack them. NEVER raises.'
- 'skipped'
- 'audit_store_unavailable'
- 'action_id, occurred_at, brokerage_id, actor_type, actor_id, action, target_type, target_id, status, warning_count, metadata, prev_hash, row_hash'
- 'occurred_at'
- 'data'
- 'backfill_operator_audit_hashes read error type='
- 'db_read_failed:'
- 'prev_hash'
- 'row_hash'
- 'action_id'
- 'force_overwrite_refused_by_policy'
- 'db_write_failed:'
- 'backfill_operator_audit_hashes update error action_id='
- ' type='
- 'partial_failure'
- 'backfill_partial_failure'
- 'argparse.ArgumentParser'
- 'backfill_operator_audit_hashes'
- "PAS176 — Backfill prev_hash / row_hash for pre-v23 audit rows. Dry-run by default; --execute required. --force attempts to overwrite existing hashes; PAS176's v24 SQL policy refuses force-overwrites without a separately-promoted force-update policy."
- '--limit'
- 'Max audit rows to process per run (default '
- ', max '
- '--execute'
- 'store_true'
- 'Actually write hashes. Without this flag the script runs in dry-run mode.'
- '--force'
- "Attempt to overwrite already-hashed rows. PAS176's v24 SQL policy refuses overwrites; use --force ONLY when the operator has separately promoted a one-shot force-update policy NOT shipped in v24."
- '--json'
- 'Emit JSON on stdout instead of the human summary.'
- 'env'
- 'None'
- '[PAS176/backfill_operator_audit_hashes] status='
- ' dry_run='
- ' force='
- ' candidates='
- ' written='
- ' skipped='
- ' failed='
- '  warn: '
- 'argv'

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ("\nPAS176 — Pre-v23 audit-row hash backfill (operator-driven).\n\nComputes ``prev_hash`` + ``row_hash`` for audit rows that\nlanded BEFORE the PAS175 v23 migration added the hash\ncolumns. Dry-run by default; ``--execute`` required to\nwrite. ``--force`` permitted but PAS176's v24 SQL policy\nrefuses force-overwrites — see operator notes below.\n\nDoctrine:\n\n* **Dry-run by default.** ``--execute`` required.\n* **Null-only by default.** The v24 SQL policy\n  ``pas_operator_actions_log_service_role_null_only_update``\n  allows UPDATE only when ``row_hash IS NULL``. Already-\n  hashed rows are NEVER touched by the default backfill.\n* **--force is honoured at the script layer but the SQL\n  layer refuses force-overwrites in PAS176.** Operators\n  who genuinely need to rewrite existing hashes must\n  promote an additional one-shot UPDATE policy NOT shipped\n  in v24. The script logs the attempt and surfaces the\n  SQL failure as a structural warning.\n* **NEVER rewrites the audit row's content.** Only the\n  hash columns. The canonical row fields (action_id,\n  occurred_at, brokerage_id, actor_type, actor_id, action,\n  target_type, target_id, status, warning_count,\n  metadata) are read but never modified.\n* **NEVER raises.**\n* **DB unavailable → exit 0** with skipped envelope.\n* **Bad args → exit 2.**\n* **No autonomous remediation.** The backfill is a one-shot\n  operator action; no scheduler / cron / startup hook.\n\nUsage:\n\n    # Dry-run; report which rows lack hashes.\n    python scripts/backfill_operator_audit_hashes.py\n\n    # Compute + write hashes for null rows.\n    python scripts/backfill_operator_audit_hashes.py --execute\n\n    # Attempt to overwrite existing hashes (will fail at v24\n    # SQL layer unless the operator separately promoted the\n    # force-update policy).\n    python scripts/backfill_operator_audit_hashes.py --execute --force\n")
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
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              8 (datetime)
               IMPORT_FROM              8 (datetime)
               STORE_NAME               8 (datetime)
               IMPORT_FROM              9 (timezone)
               STORE_NAME               9 (timezone)
               POP_TOP

  56           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
               IMPORT_NAME             10 (typing)
               IMPORT_FROM             11 (Any)
               STORE_NAME              11 (Any)
               IMPORT_FROM             12 (Dict)
               STORE_NAME              12 (Dict)
               IMPORT_FROM             13 (List)
               STORE_NAME              13 (List)
               IMPORT_FROM             14 (Optional)
               STORE_NAME              14 (Optional)
               POP_TOP

  59           LOAD_NAME                7 (sys)
               LOAD_ATTR               30 (stdout)
               LOAD_NAME                7 (sys)
               LOAD_ATTR               32 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              17 (_stream)

  60           NOP

  61   L2:     LOAD_NAME               17 (_stream)
               LOAD_ATTR               37 (reconfigure + NULL|self)
               LOAD_CONST               5 ('utf-8')
               LOAD_CONST               6 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  59   L4:     END_FOR
               POP_ITER

  66           LOAD_NAME                7 (sys)
               LOAD_ATTR               40 (path)
               LOAD_ATTR               43 (insert + NULL|self)
               LOAD_SMALL_INT           0
               LOAD_NAME                6 (os)
               LOAD_ATTR               40 (path)
               LOAD_ATTR               45 (abspath + NULL|self)
               LOAD_NAME                6 (os)
               LOAD_ATTR               40 (path)
               LOAD_ATTR               47 (join + NULL|self)
               LOAD_NAME                6 (os)
               LOAD_ATTR               40 (path)
               LOAD_ATTR               49 (dirname + NULL|self)
               LOAD_NAME               25 (__file__)
               CALL                     1
               LOAD_CONST               7 ('..')
               CALL                     2
               CALL                     1
               CALL                     2
               POP_TOP

  69           LOAD_NAME                5 (logging)
               LOAD_ATTR               52 (getLogger)
               PUSH_NULL
               LOAD_CONST               8 ('pas.scripts.backfill_operator_audit_hashes')
               CALL                     1
               STORE_NAME              27 (logger)

  72           LOAD_CONST               9 ('pas_operator_actions_log')
               STORE_NAME              28 (_TABLE)

  74           LOAD_CONST              10 (1000)
               STORE_NAME              29 (_DEFAULT_LIMIT)

  75           LOAD_CONST              11 (10000)
               STORE_NAME              30 (_HARD_CAP_LIMIT)

  78           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts\backfill_operator_audit_hashes.py", line 78>)
               MAKE_FUNCTION
               LOAD_CONST              13 (<code object _now_iso at 0x0000018C18038DF0, file "scripts\backfill_operator_audit_hashes.py", line 78>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_now_iso)

  82           LOAD_CONST              14 (<code object _get_db_safe at 0x0000018C17FF1230, file "scripts\backfill_operator_audit_hashes.py", line 82>)
               MAKE_FUNCTION
               STORE_NAME              32 (_get_db_safe)

  94           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18024C30, file "scripts\backfill_operator_audit_hashes.py", line 94>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _clamp at 0x0000018C18038B70, file "scripts\backfill_operator_audit_hashes.py", line 94>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              33 (_clamp)

 106           LOAD_CONST              17 ('candidate_count')

 112           LOAD_SMALL_INT           0

 106           LOAD_CONST              18 ('written_count')

 113           LOAD_SMALL_INT           0

 106           LOAD_CONST              19 ('skipped_count')

 114           LOAD_SMALL_INT           0

 106           LOAD_CONST              20 ('failed_count')

 115           LOAD_SMALL_INT           0

 106           LOAD_CONST              21 ('warnings')

 116           LOAD_CONST               2 (None)

 106           LOAD_CONST              22 ('error_code')

 117           LOAD_CONST               2 (None)

 106           BUILD_MAP                6
               LOAD_CONST              23 (<code object __annotate__ at 0x0000018C18053E10, file "scripts\backfill_operator_audit_hashes.py", line 106>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object _safe_envelope at 0x0000018C17F96420, file "scripts\backfill_operator_audit_hashes.py", line 106>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              34 (_safe_envelope)

 136           LOAD_CONST              25 ('limit')

 138           LOAD_NAME               29 (_DEFAULT_LIMIT)

 136           LOAD_CONST              26 ('dry_run')

 139           LOAD_CONST              27 (True)

 136           LOAD_CONST              28 ('force')

 140           LOAD_CONST              29 (False)

 136           BUILD_MAP                3
               LOAD_CONST              30 (<code object __annotate__ at 0x0000018C18025E30, file "scripts\backfill_operator_audit_hashes.py", line 136>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object backfill at 0x0000018C17D51940, file "scripts\backfill_operator_audit_hashes.py", line 136>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              35 (backfill)

 290           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA2D30, file "scripts\backfill_operator_audit_hashes.py", line 290>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object _build_parser at 0x0000018C179C3E10, file "scripts\backfill_operator_audit_hashes.py", line 290>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              36 (_build_parser)

 325           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts\backfill_operator_audit_hashes.py", line 325>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object _print_summary at 0x0000018C1801C410, file "scripts\backfill_operator_audit_hashes.py", line 325>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              37 (_print_summary)

 340           LOAD_CONST              39 ((None,))
               LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA3000, file "scripts\backfill_operator_audit_hashes.py", line 340>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object main at 0x0000018C17CD0F70, file "scripts\backfill_operator_audit_hashes.py", line 340>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              38 (main)

 361           LOAD_NAME               39 (__name__)
               LOAD_CONST              38 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 362           LOAD_NAME                7 (sys)
               LOAD_ATTR               80 (exit)
               PUSH_NULL
               LOAD_NAME               38 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 361   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  62           LOAD_NAME               19 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  63   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          268 (to L1)

  62   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts\backfill_operator_audit_hashes.py", line 78>:
 78           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038DF0, file "scripts\backfill_operator_audit_hashes.py", line 78>:
 78           RESUME                   0

 79           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object _get_db_safe at 0x0000018C17FF1230, file "scripts\backfill_operator_audit_hashes.py", line 82>:
  82           RESUME                   0

  83           NOP

  84   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

  85           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

  86           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

  87   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

  88           LOAD_CONST               2 ('backfill_operator_audit_hashes db client unavailable type=')

  89           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

  88           BUILD_STRING             2

  87           CALL                     1
               POP_TOP

  91   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

  86   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "scripts\backfill_operator_audit_hashes.py", line 94>:
 94           RESUME                   0
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

Disassembly of <code object _clamp at 0x0000018C18038B70, file "scripts\backfill_operator_audit_hashes.py", line 94>:
  94           RESUME                   0

  95           NOP

  96   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

  99   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 100           LOAD_FAST                1 (lo)
               RETURN_VALUE

 101   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 102           LOAD_FAST                2 (hi)
               RETURN_VALUE

 103   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

  97           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

  98           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

  97   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18053E10, file "scripts\backfill_operator_audit_hashes.py", line 106>:
106           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

108           LOAD_CONST               2 ('str')

106           LOAD_CONST               3 ('dry_run')

109           LOAD_CONST               4 ('bool')

106           LOAD_CONST               5 ('force')

110           LOAD_CONST               4 ('bool')

106           LOAD_CONST               6 ('limit')

111           LOAD_CONST               7 ('int')

106           LOAD_CONST               8 ('candidate_count')

112           LOAD_CONST               7 ('int')

106           LOAD_CONST               9 ('written_count')

113           LOAD_CONST               7 ('int')

106           LOAD_CONST              10 ('skipped_count')

114           LOAD_CONST               7 ('int')

106           LOAD_CONST              11 ('failed_count')

115           LOAD_CONST               7 ('int')

106           LOAD_CONST              12 ('warnings')

116           LOAD_CONST              13 ('Optional[List[str]]')

106           LOAD_CONST              14 ('error_code')

117           LOAD_CONST              15 ('Optional[str]')

106           LOAD_CONST              16 ('return')

118           LOAD_CONST              17 ('Dict[str, Any]')

106           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C17F96420, file "scripts\backfill_operator_audit_hashes.py", line 106>:
106           RESUME                   0

120           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS176')

121           LOAD_CONST               2 ('backfill')
              LOAD_CONST               3 ('operator_audit_hashes')

122           LOAD_CONST               4 ('status')
              LOAD_FAST                0 (status)

123           LOAD_CONST               5 ('dry_run')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         1 (dry_run)
              CALL                     1

124           LOAD_CONST               6 ('force')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         2 (force)
              CALL                     1

125           LOAD_CONST               7 ('limit')
              LOAD_FAST                3 (limit)

126           LOAD_CONST               8 ('candidate_count')
              LOAD_FAST                4 (candidate_count)

127           LOAD_CONST               9 ('written_count')
              LOAD_FAST                5 (written_count)

128           LOAD_CONST              10 ('skipped_count')
              LOAD_FAST                6 (skipped_count)

129           LOAD_CONST              11 ('failed_count')
              LOAD_FAST                7 (failed_count)

130           LOAD_CONST              12 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                8 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

131           LOAD_CONST              13 ('error_code')
              LOAD_FAST_BORROW         9 (error_code)

132           LOAD_CONST              14 ('generated_at')
              LOAD_GLOBAL              5 (_now_iso + NULL)
              CALL                     0

119           BUILD_MAP               13
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "scripts\backfill_operator_audit_hashes.py", line 136>:
136           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('limit')

138           LOAD_CONST               2 ('int')

136           LOAD_CONST               3 ('dry_run')

139           LOAD_CONST               4 ('bool')

136           LOAD_CONST               5 ('force')

140           LOAD_CONST               4 ('bool')

136           LOAD_CONST               6 ('return')

141           LOAD_CONST               7 ('Dict[str, Any]')

136           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object backfill at 0x0000018C17D51940, file "scripts\backfill_operator_audit_hashes.py", line 136>:
 136            RESUME                   0

 144            LOAD_GLOBAL              1 (_clamp + NULL)
                LOAD_FAST_BORROW         0 (limit)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              2 (_HARD_CAP_LIMIT)
                LOAD_GLOBAL              4 (_DEFAULT_LIMIT)
                CALL                     4
                STORE_FAST               3 (capped_limit)

 145            LOAD_GLOBAL              7 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               4 (db)

 146            LOAD_FAST_BORROW         4 (db)
                POP_JUMP_IF_NOT_NONE    18 (to L1)
                NOT_TAKEN

 147            LOAD_GLOBAL              9 (_safe_envelope + NULL)

 148            LOAD_CONST               2 ('skipped')

 149            LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (dry_run, force)
                LOAD_FAST_BORROW         3 (capped_limit)

 150            LOAD_CONST               3 ('audit_store_unavailable')
                BUILD_LIST               1

 151            LOAD_CONST               3 ('audit_store_unavailable')

 147            LOAD_CONST               4 (('status', 'dry_run', 'force', 'limit', 'warnings', 'error_code'))
                CALL_KW                  6
                RETURN_VALUE

 158    L1:     NOP

 160    L2:     LOAD_FAST_BORROW         4 (db)
                LOAD_ATTR               11 (table + NULL|self)
                LOAD_GLOBAL             12 (_TABLE)
                CALL                     1

 161            LOAD_ATTR               15 (select + NULL|self)

 162            LOAD_CONST               5 ('action_id, occurred_at, brokerage_id, actor_type, actor_id, action, target_type, target_id, status, warning_count, metadata, prev_hash, row_hash')

 161            CALL                     1

 166            LOAD_ATTR               17 (order + NULL|self)
                LOAD_CONST               6 ('occurred_at')
                LOAD_CONST               7 (False)
                LOAD_CONST               8 (('desc',))
                CALL_KW                  2

 167            LOAD_ATTR               19 (limit + NULL|self)
                LOAD_FAST_BORROW         3 (capped_limit)
                CALL                     1

 168            LOAD_ATTR               21 (execute + NULL|self)
                CALL                     0

 159            STORE_FAST               5 (result)

 170            LOAD_GLOBAL             23 (list + NULL)
                LOAD_GLOBAL             25 (getattr + NULL)
                LOAD_FAST_BORROW         5 (result)
                LOAD_CONST               9 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
        L3:     NOT_TAKEN
        L4:     POP_TOP
                BUILD_LIST               0
        L5:     CALL                     1
                STORE_FAST               6 (rows)

 183    L6:     LOAD_FAST                6 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L7)
                NOT_TAKEN

 184            LOAD_GLOBAL              9 (_safe_envelope + NULL)

 185            LOAD_CONST              12 ('ok')

 186            LOAD_FAST_LOAD_FAST     18 (dry_run, force)
                LOAD_FAST                3 (capped_limit)

 184            LOAD_CONST              13 (('status', 'dry_run', 'force', 'limit'))
                CALL_KW                  4
                RETURN_VALUE

 189    L7:     LOAD_SMALL_INT           0
                LOAD_CONST              14 (('compute_row_hash', 'GENESIS_HASH'))
                IMPORT_NAME             18 (app.services.operator.audit_integrity)
                IMPORT_FROM             19 (compute_row_hash)
                STORE_FAST               8 (compute_row_hash)
                IMPORT_FROM             20 (GENESIS_HASH)
                STORE_FAST               9 (GENESIS_HASH)
                POP_TOP

 194            LOAD_SMALL_INT           0
                STORE_FAST              10 (candidate_count)

 195            LOAD_FAST                6 (rows)
                GET_ITER
        L8:     FOR_ITER               186 (to L13)
                STORE_FAST              11 (r)

 196            LOAD_GLOBAL             43 (isinstance + NULL)
                LOAD_FAST               11 (r)
                LOAD_GLOBAL             44 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN

 197            JUMP_BACKWARD           27 (to L8)

 198    L9:     LOAD_GLOBAL             43 (isinstance + NULL)
                LOAD_FAST               11 (r)
                LOAD_ATTR               47 (get + NULL|self)
                LOAD_CONST              15 ('prev_hash')
                CALL                     1
                LOAD_GLOBAL             48 (str)
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       24 (to L10)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST               11 (r)
                LOAD_CONST              15 ('prev_hash')
                BINARY_OP               26 ([])
                LOAD_ATTR               51 (strip + NULL|self)
                CALL                     0
       L10:     STORE_FAST              12 (has_prev)

 199            LOAD_GLOBAL             43 (isinstance + NULL)
                LOAD_FAST               11 (r)
                LOAD_ATTR               47 (get + NULL|self)
                LOAD_CONST              16 ('row_hash')
                CALL                     1
                LOAD_GLOBAL             48 (str)
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       24 (to L11)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST               11 (r)
                LOAD_CONST              16 ('row_hash')
                BINARY_OP               26 ([])
                LOAD_ATTR               51 (strip + NULL|self)
                CALL                     0
       L11:     STORE_FAST              13 (has_row)

 200            LOAD_FAST                2 (force)
                TO_BOOL
                POP_JUMP_IF_TRUE        19 (to L12)
                NOT_TAKEN
                LOAD_FAST               12 (has_prev)
                TO_BOOL
                POP_JUMP_IF_FALSE       11 (to L12)
                NOT_TAKEN
                LOAD_FAST               13 (has_row)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD          177 (to L8)

 201   L12:     LOAD_FAST               10 (candidate_count)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              10 (candidate_count)
                JUMP_BACKWARD          188 (to L8)

 195   L13:     END_FOR
                POP_ITER

 203            LOAD_FAST                1 (dry_run)
                TO_BOOL
                POP_JUMP_IF_FALSE       16 (to L14)
                NOT_TAKEN

 204            LOAD_GLOBAL              9 (_safe_envelope + NULL)

 205            LOAD_CONST              12 ('ok')

 206            LOAD_CONST              17 (True)
                LOAD_FAST_LOAD_FAST     35 (force, capped_limit)

 207            LOAD_FAST               10 (candidate_count)

 204            LOAD_CONST              18 (('status', 'dry_run', 'force', 'limit', 'candidate_count'))
                CALL_KW                  5
                RETURN_VALUE

 211   L14:     LOAD_FAST                9 (GENESIS_HASH)
                STORE_FAST              14 (expected_prev)

 212            LOAD_SMALL_INT           0
                STORE_FAST              15 (written)

 213            LOAD_SMALL_INT           0
                STORE_FAST              16 (skipped)

 214            LOAD_SMALL_INT           0
                STORE_FAST              17 (failed)

 215            BUILD_LIST               0
                STORE_FAST              18 (warnings)

 217            LOAD_FAST                6 (rows)
                GET_ITER
       L15:     EXTENDED_ARG             1
                FOR_ITER               475 (to L36)
                STORE_FAST              11 (r)

 218            LOAD_GLOBAL             43 (isinstance + NULL)
                LOAD_FAST               11 (r)
                LOAD_GLOBAL             44 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L16)
                NOT_TAKEN

 219            LOAD_FAST               16 (skipped)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              16 (skipped)

 220            JUMP_BACKWARD           37 (to L15)

 221   L16:     LOAD_GLOBAL             43 (isinstance + NULL)
                LOAD_FAST               11 (r)
                LOAD_ATTR               47 (get + NULL|self)
                LOAD_CONST              15 ('prev_hash')
                CALL                     1
                LOAD_GLOBAL             48 (str)
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       24 (to L17)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST               11 (r)
                LOAD_CONST              15 ('prev_hash')
                BINARY_OP               26 ([])
                LOAD_ATTR               51 (strip + NULL|self)
                CALL                     0
       L17:     STORE_FAST              12 (has_prev)

 222            LOAD_GLOBAL             43 (isinstance + NULL)
                LOAD_FAST               11 (r)
                LOAD_ATTR               47 (get + NULL|self)
                LOAD_CONST              16 ('row_hash')
                CALL                     1
                LOAD_GLOBAL             48 (str)
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       24 (to L18)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST               11 (r)
                LOAD_CONST              16 ('row_hash')
                BINARY_OP               26 ([])
                LOAD_ATTR               51 (strip + NULL|self)
                CALL                     0
       L18:     STORE_FAST              13 (has_row)

 223            LOAD_FAST                8 (compute_row_hash)
                PUSH_NULL
                LOAD_FAST_LOAD_FAST    235 (expected_prev, r)
                CALL                     2
                STORE_FAST              19 (recomputed_hash)

 224            LOAD_FAST                2 (force)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L20)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST               12 (has_prev)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L19)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST               13 (has_row)
       L19:     TO_BOOL
                UNARY_NOT
       L20:     STORE_FAST              20 (needs_write)

 225            LOAD_FAST               20 (needs_write)
                TO_BOOL
                POP_JUMP_IF_FALSE      228 (to L34)
                NOT_TAKEN

 227            LOAD_CONST              15 ('prev_hash')
                LOAD_FAST               14 (expected_prev)

 228            LOAD_CONST              16 ('row_hash')
                LOAD_FAST               19 (recomputed_hash)

 226            BUILD_MAP                2
                STORE_FAST              21 (patch)

 230            LOAD_FAST               11 (r)
                LOAD_ATTR               47 (get + NULL|self)
                LOAD_CONST              19 ('action_id')
                CALL                     1
                STORE_FAST              22 (aid)

 231            LOAD_GLOBAL             43 (isinstance + NULL)
                LOAD_FAST               22 (aid)
                LOAD_GLOBAL             48 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L21)
                NOT_TAKEN

 232            LOAD_FAST               16 (skipped)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              16 (skipped)

 236            LOAD_FAST               19 (recomputed_hash)
                STORE_FAST              14 (expected_prev)

 237            EXTENDED_ARG             1
                JUMP_BACKWARD          263 (to L15)

 238   L21:     NOP

 240   L22:     LOAD_FAST                4 (db)
                LOAD_ATTR               11 (table + NULL|self)
                LOAD_GLOBAL             12 (_TABLE)
                CALL                     1

 241            LOAD_ATTR               53 (update + NULL|self)
                LOAD_FAST               21 (patch)
                CALL                     1

 242            LOAD_ATTR               55 (eq + NULL|self)
                LOAD_CONST              19 ('action_id')
                LOAD_FAST               22 (aid)
                CALL                     2

 243            LOAD_ATTR               21 (execute + NULL|self)
                CALL                     0

 239            STORE_FAST              23 (upd)

 245            LOAD_GLOBAL             23 (list + NULL)
                LOAD_GLOBAL             25 (getattr + NULL)
                LOAD_FAST               23 (upd)
                LOAD_CONST               9 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L25)
       L23:     NOT_TAKEN
       L24:     POP_TOP
                BUILD_LIST               0
       L25:     CALL                     1
                STORE_FAST              24 (updated_rows)

 246            LOAD_FAST               24 (updated_rows)
                TO_BOOL
                POP_JUMP_IF_FALSE       11 (to L29)
       L26:     NOT_TAKEN

 247   L27:     LOAD_FAST               15 (written)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              15 (written)
       L28:     JUMP_FORWARD            51 (to L34)

 249   L29:     LOAD_FAST               16 (skipped)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              16 (skipped)

 256            LOAD_FAST                2 (force)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L34)
       L30:     NOT_TAKEN
       L31:     LOAD_FAST               13 (has_row)
                TO_BOOL
                POP_JUMP_IF_FALSE       27 (to L34)
       L32:     NOT_TAKEN

 257   L33:     LOAD_CONST              20 ('force_overwrite_refused_by_policy')
                STORE_FAST              25 (code)

 258            LOAD_FAST               25 (code)
                LOAD_FAST               18 (warnings)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       18 (to L34)
                NOT_TAKEN

 259            LOAD_FAST               18 (warnings)
                LOAD_ATTR               57 (append + NULL|self)
                LOAD_FAST               25 (code)
                CALL                     1
                POP_TOP

 272   L34:     LOAD_FAST               13 (has_row)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L35)
                NOT_TAKEN
                LOAD_FAST                2 (force)
                TO_BOOL
                POP_JUMP_IF_TRUE        27 (to L35)
                NOT_TAKEN

 273            LOAD_FAST               11 (r)
                LOAD_CONST              16 ('row_hash')
                BINARY_OP               26 ([])
                LOAD_ATTR               51 (strip + NULL|self)
                CALL                     0
                STORE_FAST              14 (expected_prev)
                EXTENDED_ARG             1
                JUMP_BACKWARD          473 (to L15)

 275   L35:     LOAD_FAST               19 (recomputed_hash)
                STORE_FAST              14 (expected_prev)
                EXTENDED_ARG             1
                JUMP_BACKWARD          478 (to L15)

 217   L36:     END_FOR
                POP_ITER

 277            LOAD_FAST               17 (failed)
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L37)
                NOT_TAKEN
                LOAD_CONST              12 ('ok')
                JUMP_FORWARD             1 (to L38)
       L37:     LOAD_CONST              24 ('partial_failure')
       L38:     STORE_FAST              26 (overall)

 278            LOAD_GLOBAL              9 (_safe_envelope + NULL)

 279            LOAD_FAST               26 (overall)

 280            LOAD_CONST               7 (False)
                LOAD_FAST_LOAD_FAST     35 (force, capped_limit)

 281            LOAD_FAST               10 (candidate_count)

 282            LOAD_FAST               15 (written)

 283            LOAD_FAST               16 (skipped)

 284            LOAD_FAST               17 (failed)

 285            LOAD_FAST               18 (warnings)

 286            LOAD_FAST               26 (overall)
                LOAD_CONST              12 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        8 (to L39)
                NOT_TAKEN
                LOAD_CONST               1 (None)

 278            LOAD_CONST              26 (('status', 'dry_run', 'force', 'limit', 'candidate_count', 'written_count', 'skipped_count', 'failed_count', 'warnings', 'error_code'))
                CALL_KW                 10
                RETURN_VALUE

 286   L39:     LOAD_CONST              25 ('backfill_partial_failure')

 278            LOAD_CONST              26 (('status', 'dry_run', 'force', 'limit', 'candidate_count', 'written_count', 'skipped_count', 'failed_count', 'warnings', 'error_code'))
                CALL_KW                 10
                RETURN_VALUE

  --   L40:     PUSH_EXC_INFO

 171            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       93 (to L45)
                NOT_TAKEN
                STORE_FAST               7 (e)

 172   L41:     LOAD_GLOBAL             28 (logger)
                LOAD_ATTR               31 (warning + NULL|self)

 173            LOAD_CONST              10 ('backfill_operator_audit_hashes read error type=')

 174            LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE

 173            BUILD_STRING             2

 172            CALL                     1
                POP_TOP

 176            LOAD_GLOBAL              9 (_safe_envelope + NULL)

 177            LOAD_CONST               2 ('skipped')

 178            LOAD_FAST_LOAD_FAST     18 (dry_run, force)
                LOAD_FAST                3 (capped_limit)

 179            LOAD_CONST              11 ('db_read_failed:')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 180            LOAD_CONST               3 ('audit_store_unavailable')

 176            LOAD_CONST               4 (('status', 'dry_run', 'force', 'limit', 'warnings', 'error_code'))
                CALL_KW                  6
       L42:     SWAP                     2
       L43:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L44:     LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 171   L45:     RERAISE                  0

  --   L46:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L47:     PUSH_EXC_INFO

 260            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      115 (to L52)
                NOT_TAKEN
                STORE_FAST               7 (e)

 261   L48:     LOAD_FAST               17 (failed)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              17 (failed)

 262            LOAD_CONST              21 ('db_write_failed:')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                STORE_FAST              25 (code)

 263            LOAD_FAST               25 (code)
                LOAD_FAST               18 (warnings)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       18 (to L49)
                NOT_TAKEN

 264            LOAD_FAST               18 (warnings)
                LOAD_ATTR               57 (append + NULL|self)
                LOAD_FAST               25 (code)
                CALL                     1
                POP_TOP

 265   L49:     LOAD_GLOBAL             28 (logger)
                LOAD_ATTR               31 (warning + NULL|self)

 266            LOAD_CONST              22 ('backfill_operator_audit_hashes update error action_id=')

 267            LOAD_FAST               22 (aid)
                FORMAT_SIMPLE
                LOAD_CONST              23 (' type=')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE

 266            BUILD_STRING             4

 265            CALL                     1
                POP_TOP
       L50:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 320 (to L34)

  --   L51:     LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 260   L52:     RERAISE                  0

  --   L53:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L40 [0]
  L4 to L6 -> L40 [0]
  L22 to L23 -> L47 [1]
  L24 to L26 -> L47 [1]
  L27 to L28 -> L47 [1]
  L29 to L30 -> L47 [1]
  L31 to L32 -> L47 [1]
  L33 to L34 -> L47 [1]
  L40 to L41 -> L46 [1] lasti
  L41 to L42 -> L44 [1] lasti
  L42 to L43 -> L46 [1] lasti
  L44 to L46 -> L46 [1] lasti
  L47 to L48 -> L53 [2] lasti
  L48 to L50 -> L51 [2] lasti
  L51 to L53 -> L53 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "scripts\backfill_operator_audit_hashes.py", line 290>:
290           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C179C3E10, file "scripts\backfill_operator_audit_hashes.py", line 290>:
290           RESUME                   0

291           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

292           LOAD_CONST               0 ('backfill_operator_audit_hashes')

294           LOAD_CONST               1 ("PAS176 — Backfill prev_hash / row_hash for pre-v23 audit rows. Dry-run by default; --execute required. --force attempts to overwrite existing hashes; PAS176's v24 SQL policy refuses force-overwrites without a separately-promoted force-update policy.")

291           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

301           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

302           LOAD_CONST               3 ('--limit')
              LOAD_GLOBAL              6 (int)
              LOAD_GLOBAL              8 (_DEFAULT_LIMIT)

303           LOAD_CONST               4 ('Max audit rows to process per run (default ')
              LOAD_GLOBAL              8 (_DEFAULT_LIMIT)
              FORMAT_SIMPLE
              LOAD_CONST               5 (', max ')
              LOAD_GLOBAL             10 (_HARD_CAP_LIMIT)
              FORMAT_SIMPLE
              LOAD_CONST               6 (').')
              BUILD_STRING             5

301           LOAD_CONST               7 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

305           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

306           LOAD_CONST               8 ('--execute')
              LOAD_CONST               9 ('store_true')

307           LOAD_CONST              10 ('Actually write hashes. Without this flag the script runs in dry-run mode.')

305           LOAD_CONST              11 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

309           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

310           LOAD_CONST              12 ('--force')
              LOAD_CONST               9 ('store_true')

312           LOAD_CONST              13 ("Attempt to overwrite already-hashed rows. PAS176's v24 SQL policy refuses overwrites; use --force ONLY when the operator has separately promoted a one-shot force-update policy NOT shipped in v24.")

309           LOAD_CONST              11 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

318           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

319           LOAD_CONST              14 ('--json')
              LOAD_CONST               9 ('store_true')

320           LOAD_CONST              15 ('Emit JSON on stdout instead of the human summary.')

318           LOAD_CONST              11 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

322           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts\backfill_operator_audit_hashes.py", line 325>:
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

Disassembly of <code object _print_summary at 0x0000018C1801C410, file "scripts\backfill_operator_audit_hashes.py", line 325>:
325           RESUME                   0

326           LOAD_GLOBAL              1 (print + NULL)

327           LOAD_CONST               0 ('[PAS176/backfill_operator_audit_hashes] status=')

328           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               1 ('status')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' dry_run=')

329           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               3 ('dry_run')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' force=')

330           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               5 ('force')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' candidates=')

331           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               7 ('candidate_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' written=')

332           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               9 ('written_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' skipped=')

333           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST              11 ('skipped_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              12 (' failed=')

334           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST              13 ('failed_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

327           BUILD_STRING            14

326           CALL                     1
              POP_TOP

336           LOAD_FAST_BORROW         0 (env)
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

337           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              16 ('  warn: ')
              LOAD_FAST_BORROW         1 (w)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

336   L3:     END_FOR
              POP_ITER
              LOAD_CONST              17 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "scripts\backfill_operator_audit_hashes.py", line 340>:
340           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17CD0F70, file "scripts\backfill_operator_audit_hashes.py", line 340>:
 340            RESUME                   0

 341            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 342            NOP

 343    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 347    L2:     LOAD_GLOBAL             11 (backfill + NULL)

 348            LOAD_FAST                2 (args)
                LOAD_ATTR               12 (limit)

 349            LOAD_FAST                2 (args)
                LOAD_ATTR               14 (execute)
                TO_BOOL
                UNARY_NOT

 350            LOAD_FAST                2 (args)
                LOAD_ATTR               16 (force)

 347            LOAD_CONST               2 (('limit', 'dry_run', 'force'))
                CALL_KW                  3
                STORE_FAST               4 (env)

 353            LOAD_FAST                2 (args)
                LOAD_ATTR               18 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       37 (to L3)
                NOT_TAKEN

 354            LOAD_GLOBAL             21 (print + NULL)
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

 358            LOAD_SMALL_INT           0
                RETURN_VALUE

 356    L3:     LOAD_GLOBAL             25 (_print_summary + NULL)
                LOAD_FAST                4 (env)
                CALL                     1
                POP_TOP

 358            LOAD_SMALL_INT           0
                RETURN_VALUE

  --    L4:     PUSH_EXC_INFO

 344            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L13)
                NOT_TAKEN
                STORE_FAST               3 (e)

 345    L5:     LOAD_FAST                3 (e)
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

 344   L13:     RERAISE                  0

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
