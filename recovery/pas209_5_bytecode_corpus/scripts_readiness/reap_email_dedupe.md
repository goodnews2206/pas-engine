# scripts_readiness/reap_email_dedupe

- **pyc:** `scripts\__pycache__\reap_email_dedupe.cpython-314.pyc`
- **expected source path (absent):** `scripts/reap_email_dedupe.py`
- **co_filename (from bytecode):** `scripts\reap_email_dedupe.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS167 — Email dedupe reaper (operator-only).

Reaps expired rows from the PAS166 durable email-dedupe table
(``pas_email_dedupe_keys``). Operator-driven, dry-run-first,
no auto-schedule.

Doctrine:

* **Dry-run by default.** No row is deleted unless ``--execute``
  is supplied. The default invocation prints a count + a
  structural per-source breakdown only.
* **No PII echo.** The reaper NEVER prints the dedupe key,
  the body, the subject, the sender, the phone, the email,
  the name, or any other identifying field. The
  ``pas_email_dedupe_keys`` table doesn't carry those columns
  anyway (PAS166 doctrine), but the reaper's output is
  structural-only so a future schema regression couldn't
  leak through this surface.
* **No exception escapes.** Every error path produces a
  structural report and a documented exit code.
* **No .env read.** The Supabase client is resolved via the
  app's existing helper; an unconfigured client surfaces a
  ``durable_email_dedupe_unavailable`` skip and exits 0.
* **No Gmail / OAuth / inbox-scan / vendor / embedding import.**

Usage:
  python scripts/reap_email_dedupe.py
      [--brokerage-id BID]
      [--source SRC]
      [--older-than-hours N]   (default 24, clamp 1..168*30)
      [--limit N]              (default 500, clamp 1..5000)
      [--json]
      [--execute]              (required to delete)

Exit codes:
    0  — ok / skipped (DB unavailable)
    1  — failed (DB error during a real delete)
    2  — bad CLI arguments
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `argparse`, `datetime`, `get_supabase`, `json`, `logging`, `os`, `sys`, `timedelta`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_clamp`, `_delete_expired`, `_get_db_safe`, `_list_expired`, `_now_iso`, `_print_summary`, `_summarise_rows`, `main`, `reap`

## Env-key candidates

_none_

## String constants (redacted where noted)

- "\nPAS167 — Email dedupe reaper (operator-only).\n\nReaps expired rows from the PAS166 durable email-dedupe table\n(``pas_email_dedupe_keys``). Operator-driven, dry-run-first,\nno auto-schedule.\n\nDoctrine:\n\n* **Dry-run by default.** No row is deleted unless ``--execute``\n  is supplied. The default invocation prints a count + a\n  structural per-source breakdown only.\n* **No PII echo.** The reaper NEVER prints the dedupe key,\n  the body, the subject, the sender, the phone, the email,\n  the name, or any other identifying field. The\n  ``pas_email_dedupe_keys`` table doesn't carry those columns\n  anyway (PAS166 doctrine), but the reaper's output is\n  structural-only so a future schema regression couldn't\n  leak through this surface.\n* **No exception escapes.** Every error path produces a\n  structural report and a documented exit code.\n* **No .env read.** The Supabase client is resolved via the\n  app's existing helper; an unconfigured client surfaces a\n  ``durable_email_dedupe_unavailable`` skip and exits 0.\n* **No Gmail / OAuth / inbox-scan / vendor / embedding import.**\n\nUsage:\n  python scripts/reap_email_dedupe.py\n      [--brokerage-id BID]\n      [--source SRC]\n      [--older-than-hours N]   (default 24, clamp 1..168*30)\n      [--limit N]              (default 500, clamp 1..5000)\n      [--json]\n      [--execute]              (required to delete)\n\nExit codes:\n    0  — ok / skipped (DB unavailable)\n    1  — failed (DB error during a real delete)\n    2  — bad CLI arguments\n"
- 'utf-8'
- 'pas.scripts.reap_email_dedupe'
- 'pas_email_dedupe_keys'
- 'now'
- 'return'
- 'str'
- 'seconds'
- 'value'
- 'Any'
- 'int'
- 'default'
- 'Lazy Supabase client resolver. Returns the client OR\n``None`` on failure. NEVER raises.'
- 'reap_email_dedupe db client unavailable type='
- 'rows'
- 'List[Dict[str, Any]]'
- 'Dict[str, int]'
- "Bucket the (already fetched, no-PII) rows by source for\nthe structural report. NEVER touches PII fields — the\ntable doesn't carry any."
- 'source'
- 'unknown'
- 'brokerage_id'
- 'Optional[str]'
- 'older_than_iso'
- 'limit'
- 'Dict[str, Any]'
- 'Fetch up to ``limit`` rows whose ``expires_at`` is before\n``older_than_iso``. Returns a structural envelope. NEVER\nraises.'
- 'brokerage_id, source, created_at, expires_at'
- 'expires_at'
- 'data'
- 'status'
- '_list_expired db error type='
- 'failed'
- 'error_code'
- 'db_read_failed:'
- 'Delete rows whose ``expires_at`` is before\n``older_than_iso``. Returns a structural envelope with the\ndeleted-row count. NEVER raises.\n\nNote: supabase-py applies the filter set across the delete;\nwe depend on the WHERE clause + the closed table schema for\nsafety. The schema has NO PII columns, so a regression that\nover-deleted would not leak PII through this surface.\n'
- 'deleted'
- '_delete_expired db error type='
- 'db_write_failed:'
- 'older_than_hours'
- 'execute'
- 'bool'
- 'Optional[datetime]'
- 'Main reaper entrypoint. Returns a structural report.\n\nThe report shape (closed)::\n\n    {\n      "status":            "ok" | "skipped" | "failed",\n      "mode":              "dry-run" | "execute",\n      "older_than_hours":  int,\n      "limit":             int,\n      "older_than_iso":    "...",\n      "brokerage_id":      Optional[str],\n      "source":            Optional[str],\n      "candidate_count":   int,    # rows that match the filter\n      "deleted_count":     int,    # 0 in dry-run\n      "by_source":         {src: count, ...},\n      "warnings":          [<structural tokens>],\n      "error_code":        None | "<structural token>",\n    }\n'
- 'mode'
- 'dry-run'
- 'candidate_count'
- 'deleted_count'
- 'by_source'
- 'warnings'
- 'invalid_source'
- 'durable_email_dedupe_unavailable'
- 'skipped'
- 'db_read_failed'
- 'db_write_failed'
- 'argparse.ArgumentParser'
- 'reap_email_dedupe'
- 'PAS167 — Operator-only reaper for expired rows in pas_email_dedupe_keys. Dry-run by default; --execute is required to actually delete. NEVER prints dedupe keys or PII (the table has none).'
- '--brokerage-id'
- 'Optional brokerage scope.'
- '--source'
- 'Optional source scope. One of: '
- '--older-than-hours'
- 'Rows whose expires_at is older than this many hours are eligible. Clamped to ['
- ']. Default '
- '--limit'
- 'Cap on the candidate listing. Clamped to ['
- '--json'
- 'store_true'
- 'Emit the structural report as JSON on stdout.'
- '--execute'
- 'Actually delete the rows. Without this flag the reaper runs in dry-run mode and prints a count only.'
- 'report'
- 'None'
- '[PAS167-reaper] status='
- ' mode='
- ' older_than_hours='
- ' limit='
- ' candidates='
- ' deleted='
- '  warning: '
- '  error_code: '
- '  by_source:'
- '    '
- 'argv'
- 'Optional[List[str]]'

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ("\nPAS167 — Email dedupe reaper (operator-only).\n\nReaps expired rows from the PAS166 durable email-dedupe table\n(``pas_email_dedupe_keys``). Operator-driven, dry-run-first,\nno auto-schedule.\n\nDoctrine:\n\n* **Dry-run by default.** No row is deleted unless ``--execute``\n  is supplied. The default invocation prints a count + a\n  structural per-source breakdown only.\n* **No PII echo.** The reaper NEVER prints the dedupe key,\n  the body, the subject, the sender, the phone, the email,\n  the name, or any other identifying field. The\n  ``pas_email_dedupe_keys`` table doesn't carry those columns\n  anyway (PAS166 doctrine), but the reaper's output is\n  structural-only so a future schema regression couldn't\n  leak through this surface.\n* **No exception escapes.** Every error path produces a\n  structural report and a documented exit code.\n* **No .env read.** The Supabase client is resolved via the\n  app's existing helper; an unconfigured client surfaces a\n  ``durable_email_dedupe_unavailable`` skip and exits 0.\n* **No Gmail / OAuth / inbox-scan / vendor / embedding import.**\n\nUsage:\n  python scripts/reap_email_dedupe.py\n      [--brokerage-id BID]\n      [--source SRC]\n      [--older-than-hours N]   (default 24, clamp 1..168*30)\n      [--limit N]              (default 500, clamp 1..5000)\n      [--json]\n      [--execute]              (required to delete)\n\nExit codes:\n    0  — ok / skipped (DB unavailable)\n    1  — failed (DB error during a real delete)\n    2  — bad CLI arguments\n")
               STORE_NAME               0 (__doc__)

  42           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  44           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  45           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  46           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (logging)
               STORE_NAME               5 (logging)

  47           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (os)
               STORE_NAME               6 (os)

  48           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (sys)
               STORE_NAME               7 (sys)

  49           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timedelta', 'timezone'))
               IMPORT_NAME              8 (datetime)
               IMPORT_FROM              8 (datetime)
               STORE_NAME               8 (datetime)
               IMPORT_FROM              9 (timedelta)
               STORE_NAME               9 (timedelta)
               IMPORT_FROM             10 (timezone)
               STORE_NAME              10 (timezone)
               POP_TOP

  50           LOAD_SMALL_INT           0
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

  53           LOAD_NAME                7 (sys)
               LOAD_ATTR               32 (stdout)
               LOAD_NAME                7 (sys)
               LOAD_ATTR               34 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              18 (_stream)

  54           NOP

  55   L2:     LOAD_NAME               18 (_stream)
               LOAD_ATTR               39 (reconfigure + NULL|self)
               LOAD_CONST               5 ('utf-8')
               LOAD_CONST               6 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  53   L4:     END_FOR
               POP_ITER

  60           LOAD_NAME                5 (logging)
               LOAD_ATTR               42 (getLogger)
               PUSH_NULL
               LOAD_CONST               7 ('pas.scripts.reap_email_dedupe')
               CALL                     1
               STORE_NAME              22 (logger)

  63           LOAD_CONST               8 ('pas_email_dedupe_keys')
               STORE_NAME              23 (_TABLE)

  67           LOAD_CONST              32 (('zillow', 'realtor', 'facebook', 'website', 'generic_email', 'manual'))
               STORE_NAME              24 (_ALLOWED_SOURCES)

  73           LOAD_SMALL_INT          24
               STORE_NAME              25 (_DEFAULT_OLDER_THAN_HOURS)

  74           LOAD_SMALL_INT           1
               STORE_NAME              26 (_MIN_OLDER_THAN_HOURS)

  75           LOAD_CONST              33 (5040)
               STORE_NAME              27 (_MAX_OLDER_THAN_HOURS)

  76           LOAD_CONST               9 (500)
               STORE_NAME              28 (_DEFAULT_LIMIT)

  77           LOAD_SMALL_INT           1
               STORE_NAME              29 (_MIN_LIMIT)

  78           LOAD_CONST              10 (5000)
               STORE_NAME              30 (_MAX_LIMIT)

  85           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts\reap_email_dedupe.py", line 85>)
               MAKE_FUNCTION
               LOAD_CONST              12 (<code object _now_iso at 0x0000018C18038170, file "scripts\reap_email_dedupe.py", line 85>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_now_iso)

  89           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18026030, file "scripts\reap_email_dedupe.py", line 89>)
               MAKE_FUNCTION
               LOAD_CONST              14 (<code object _clamp at 0x0000018C18038A30, file "scripts\reap_email_dedupe.py", line 89>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_clamp)

 101           LOAD_CONST              15 (<code object _get_db_safe at 0x0000018C17FF10B0, file "scripts\reap_email_dedupe.py", line 101>)
               MAKE_FUNCTION
               STORE_NAME              33 (_get_db_safe)

 115           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts\reap_email_dedupe.py", line 115>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _summarise_rows at 0x0000018C18060F60, file "scripts\reap_email_dedupe.py", line 115>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_summarise_rows)

 132           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C18024C30, file "scripts\reap_email_dedupe.py", line 132>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _list_expired at 0x0000018C17D86090, file "scripts\reap_email_dedupe.py", line 132>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (_list_expired)

 171           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C18025030, file "scripts\reap_email_dedupe.py", line 171>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _delete_expired at 0x0000018C17ED19F0, file "scripts\reap_email_dedupe.py", line 171>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              36 (_delete_expired)

 211           LOAD_CONST              22 ('now')

 218           LOAD_CONST               2 (None)

 211           BUILD_MAP                1
               LOAD_CONST              23 (<code object __annotate__ at 0x0000018C1812C470, file "scripts\reap_email_dedupe.py", line 211>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object reap at 0x0000018C17D8BD50, file "scripts\reap_email_dedupe.py", line 211>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              37 (reap)

 376           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts\reap_email_dedupe.py", line 376>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object _build_parser at 0x0000018C181B03C0, file "scripts\reap_email_dedupe.py", line 376>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (_build_parser)

 428           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts\reap_email_dedupe.py", line 428>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object _print_summary at 0x0000018C17F7ECB0, file "scripts\reap_email_dedupe.py", line 428>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              39 (_print_summary)

 449           LOAD_CONST              34 ((None,))
               LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts\reap_email_dedupe.py", line 449>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object main at 0x0000018C17D869F0, file "scripts\reap_email_dedupe.py", line 449>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              40 (main)

 477           LOAD_NAME               41 (__name__)
               LOAD_CONST              31 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 478           LOAD_NAME                7 (sys)
               LOAD_ATTR               84 (exit)
               PUSH_NULL
               LOAD_NAME               40 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 477   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  56           LOAD_NAME               20 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

  57   L7:     POP_EXCEPT
               JUMP_BACKWARD          167 (to L1)

  56   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts\reap_email_dedupe.py", line 85>:
 85           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038170, file "scripts\reap_email_dedupe.py", line 85>:
 85           RESUME                   0

 86           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C18026030, file "scripts\reap_email_dedupe.py", line 89>:
 89           RESUME                   0
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

Disassembly of <code object _clamp at 0x0000018C18038A30, file "scripts\reap_email_dedupe.py", line 89>:
  89           RESUME                   0

  90           NOP

  91   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

  94   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

  95           LOAD_FAST                1 (lo)
               RETURN_VALUE

  96   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

  97           LOAD_FAST                2 (hi)
               RETURN_VALUE

  98   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

  92           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

  93           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

  92   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object _get_db_safe at 0x0000018C17FF10B0, file "scripts\reap_email_dedupe.py", line 101>:
 101           RESUME                   0

 104           NOP

 105   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 106           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 107           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 108   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 109           LOAD_CONST               2 ('reap_email_dedupe db client unavailable type=')

 110           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 109           BUILD_STRING             2

 108           CALL                     1
               POP_TOP

 112   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 107   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts\reap_email_dedupe.py", line 115>:
115           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rows')
              LOAD_CONST               2 ('List[Dict[str, Any]]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, int]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _summarise_rows at 0x0000018C18060F60, file "scripts\reap_email_dedupe.py", line 115>:
115           RESUME                   0

119           BUILD_MAP                0
              STORE_FAST               1 (out)

120           LOAD_FAST_BORROW         0 (rows)
              GET_ITER
      L1:     FOR_ITER                95 (to L5)
              STORE_FAST               2 (r)

121           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (r)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (r)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('source')
              CALL                     1
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 (None)
      L3:     STORE_FAST               3 (src)

122           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (src)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN

123           LOAD_CONST               3 ('unknown')
              STORE_FAST               3 (src)

124   L4:     LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_FAST_BORROW         3 (src)
              LOAD_SMALL_INT           0
              CALL                     2
              LOAD_SMALL_INT           1
              BINARY_OP                0 (+)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 19 (out, src)
              STORE_SUBSCR
              JUMP_BACKWARD           97 (to L1)

120   L5:     END_FOR
              POP_ITER

125           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "scripts\reap_email_dedupe.py", line 132>:
132           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

135           LOAD_CONST               2 ('Optional[str]')

132           LOAD_CONST               3 ('source')

136           LOAD_CONST               2 ('Optional[str]')

132           LOAD_CONST               4 ('older_than_iso')

137           LOAD_CONST               5 ('str')

132           LOAD_CONST               6 ('limit')

138           LOAD_CONST               7 ('int')

132           LOAD_CONST               8 ('return')

139           LOAD_CONST               9 ('Dict[str, Any]')

132           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _list_expired at 0x0000018C17D86090, file "scripts\reap_email_dedupe.py", line 132>:
 132            RESUME                   0

 143            NOP

 145    L1:     LOAD_FAST_BORROW         0 (db)
                LOAD_ATTR                1 (table + NULL|self)
                LOAD_GLOBAL              2 (_TABLE)
                CALL                     1

 146            LOAD_ATTR                5 (select + NULL|self)

 147            LOAD_CONST               1 ('brokerage_id, source, created_at, expires_at')

 146            CALL                     1

 149            LOAD_ATTR                7 (lt + NULL|self)
                LOAD_CONST               2 ('expires_at')
                LOAD_FAST_BORROW         3 (older_than_iso)
                CALL                     2

 150            LOAD_ATTR                9 (order + NULL|self)
                LOAD_CONST               2 ('expires_at')
                LOAD_CONST               3 (False)
                LOAD_CONST               4 (('desc',))
                CALL_KW                  2

 151            LOAD_ATTR               11 (limit + NULL|self)
                LOAD_FAST_BORROW         4 (limit)
                CALL                     1

 144            STORE_FAST               5 (query)

 153            LOAD_FAST_BORROW         1 (brokerage_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L4)
        L2:     NOT_TAKEN

 154    L3:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               13 (eq + NULL|self)
                LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST_BORROW         1 (brokerage_id)
                CALL                     2
                STORE_FAST               5 (query)

 155    L4:     LOAD_FAST_BORROW         2 (source)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L7)
        L5:     NOT_TAKEN

 156    L6:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               13 (eq + NULL|self)
                LOAD_CONST               6 ('source')
                LOAD_FAST_BORROW         2 (source)
                CALL                     2
                STORE_FAST               5 (query)

 157    L7:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               15 (execute + NULL|self)
                CALL                     0
                STORE_FAST               6 (result)

 158            LOAD_GLOBAL             17 (list + NULL)
                LOAD_GLOBAL             19 (getattr + NULL)
                LOAD_FAST_BORROW         6 (result)
                LOAD_CONST               7 ('data')
                LOAD_CONST               8 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                BUILD_LIST               0
       L10:     CALL                     1
                STORE_FAST               7 (rows)

 159            LOAD_CONST               9 ('status')
                LOAD_CONST              10 ('ok')
                LOAD_CONST              11 ('rows')
                LOAD_FAST_BORROW         7 (rows)
                BUILD_MAP                2
       L11:     RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 160            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       84 (to L17)
                NOT_TAKEN
                STORE_FAST               8 (e)

 161   L13:     LOAD_GLOBAL             22 (logger)
                LOAD_ATTR               25 (warning + NULL|self)

 162            LOAD_CONST              12 ('_list_expired db error type=')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 161            CALL                     1
                POP_TOP

 165            LOAD_CONST               9 ('status')
                LOAD_CONST              13 ('failed')

 166            LOAD_CONST              11 ('rows')
                BUILD_LIST               0

 167            LOAD_CONST              14 ('error_code')
                LOAD_CONST              15 ('db_read_failed:')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 164            BUILD_MAP                3
       L14:     SWAP                     2
       L15:     POP_EXCEPT
                LOAD_CONST               8 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RETURN_VALUE

  --   L16:     LOAD_CONST               8 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 160   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L12 [0]
  L3 to L5 -> L12 [0]
  L6 to L8 -> L12 [0]
  L9 to L11 -> L12 [0]
  L12 to L13 -> L18 [1] lasti
  L13 to L14 -> L16 [1] lasti
  L14 to L15 -> L18 [1] lasti
  L16 to L18 -> L18 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "scripts\reap_email_dedupe.py", line 171>:
171           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

174           LOAD_CONST               2 ('Optional[str]')

171           LOAD_CONST               3 ('source')

175           LOAD_CONST               2 ('Optional[str]')

171           LOAD_CONST               4 ('older_than_iso')

176           LOAD_CONST               5 ('str')

171           LOAD_CONST               6 ('return')

177           LOAD_CONST               7 ('Dict[str, Any]')

171           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _delete_expired at 0x0000018C17ED19F0, file "scripts\reap_email_dedupe.py", line 171>:
 171            RESUME                   0

 187            NOP

 189    L1:     LOAD_FAST_BORROW         0 (db)
                LOAD_ATTR                1 (table + NULL|self)
                LOAD_GLOBAL              2 (_TABLE)
                CALL                     1

 190            LOAD_ATTR                5 (delete + NULL|self)
                CALL                     0

 191            LOAD_ATTR                7 (lt + NULL|self)
                LOAD_CONST               1 ('expires_at')
                LOAD_FAST_BORROW         3 (older_than_iso)
                CALL                     2

 188            STORE_FAST               4 (query)

 193            LOAD_FAST_BORROW         1 (brokerage_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L4)
        L2:     NOT_TAKEN

 194    L3:     LOAD_FAST_BORROW         4 (query)
                LOAD_ATTR                9 (eq + NULL|self)
                LOAD_CONST               2 ('brokerage_id')
                LOAD_FAST_BORROW         1 (brokerage_id)
                CALL                     2
                STORE_FAST               4 (query)

 195    L4:     LOAD_FAST_BORROW         2 (source)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L7)
        L5:     NOT_TAKEN

 196    L6:     LOAD_FAST_BORROW         4 (query)
                LOAD_ATTR                9 (eq + NULL|self)
                LOAD_CONST               3 ('source')
                LOAD_FAST_BORROW         2 (source)
                CALL                     2
                STORE_FAST               4 (query)

 197    L7:     LOAD_FAST_BORROW         4 (query)
                LOAD_ATTR               11 (execute + NULL|self)
                CALL                     0
                STORE_FAST               5 (result)

 198            LOAD_GLOBAL             13 (list + NULL)
                LOAD_GLOBAL             15 (getattr + NULL)
                LOAD_FAST_BORROW         5 (result)
                LOAD_CONST               4 ('data')
                LOAD_CONST               5 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                BUILD_LIST               0
       L10:     CALL                     1
                STORE_FAST               6 (rows)

 199            LOAD_CONST               6 ('status')
                LOAD_CONST               7 ('ok')
                LOAD_CONST               8 ('deleted')
                LOAD_GLOBAL             17 (len + NULL)
                LOAD_FAST_BORROW         6 (rows)
                CALL                     1
                BUILD_MAP                2
       L11:     RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 200            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       84 (to L17)
                NOT_TAKEN
                STORE_FAST               7 (e)

 201   L13:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 202            LOAD_CONST               9 ('_delete_expired db error type=')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 201            CALL                     1
                POP_TOP

 205            LOAD_CONST               6 ('status')
                LOAD_CONST              10 ('failed')

 206            LOAD_CONST               8 ('deleted')
                LOAD_SMALL_INT           0

 207            LOAD_CONST              11 ('error_code')
                LOAD_CONST              12 ('db_write_failed:')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 204            BUILD_MAP                3
       L14:     SWAP                     2
       L15:     POP_EXCEPT
                LOAD_CONST               5 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L16:     LOAD_CONST               5 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 200   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L12 [0]
  L3 to L5 -> L12 [0]
  L6 to L8 -> L12 [0]
  L9 to L11 -> L12 [0]
  L12 to L13 -> L18 [1] lasti
  L13 to L14 -> L16 [1] lasti
  L14 to L15 -> L18 [1] lasti
  L16 to L18 -> L18 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C1812C470, file "scripts\reap_email_dedupe.py", line 211>:
211           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

213           LOAD_CONST               2 ('Optional[str]')

211           LOAD_CONST               3 ('source')

214           LOAD_CONST               2 ('Optional[str]')

211           LOAD_CONST               4 ('older_than_hours')

215           LOAD_CONST               5 ('int')

211           LOAD_CONST               6 ('limit')

216           LOAD_CONST               5 ('int')

211           LOAD_CONST               7 ('execute')

217           LOAD_CONST               8 ('bool')

211           LOAD_CONST               9 ('now')

218           LOAD_CONST              10 ('Optional[datetime]')

211           LOAD_CONST              11 ('return')

219           LOAD_CONST              12 ('Dict[str, Any]')

211           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object reap at 0x0000018C17D8BD50, file "scripts\reap_email_dedupe.py", line 211>:
211            RESUME                   0

239            LOAD_GLOBAL              1 (_clamp + NULL)

240            LOAD_FAST_BORROW         2 (older_than_hours)

241            LOAD_GLOBAL              2 (_MIN_OLDER_THAN_HOURS)

242            LOAD_GLOBAL              4 (_MAX_OLDER_THAN_HOURS)

243            LOAD_GLOBAL              6 (_DEFAULT_OLDER_THAN_HOURS)

239            CALL                     4
               STORE_FAST               2 (older_than_hours)

245            LOAD_GLOBAL              1 (_clamp + NULL)
               LOAD_FAST_BORROW         3 (limit)
               LOAD_GLOBAL              8 (_MIN_LIMIT)
               LOAD_GLOBAL             10 (_MAX_LIMIT)
               LOAD_GLOBAL             12 (_DEFAULT_LIMIT)
               CALL                     4
               STORE_FAST               3 (limit)

247            LOAD_FAST_BORROW         5 (now)
               POP_JUMP_IF_NOT_NONE    37 (to L1)
               NOT_TAKEN

248            LOAD_GLOBAL             14 (datetime)
               LOAD_ATTR               16 (now)
               PUSH_NULL
               LOAD_GLOBAL             18 (timezone)
               LOAD_ATTR               20 (utc)
               CALL                     1
               STORE_FAST               5 (now)

249    L1:     LOAD_FAST_BORROW         5 (now)
               LOAD_GLOBAL             23 (timedelta + NULL)
               LOAD_FAST_BORROW         2 (older_than_hours)
               LOAD_CONST               2 (('hours',))
               CALL_KW                  1
               BINARY_OP               10 (-)
               STORE_FAST               6 (cutoff)

250            LOAD_FAST_BORROW         6 (cutoff)
               LOAD_ATTR               25 (isoformat + NULL|self)
               LOAD_CONST               3 ('seconds')
               LOAD_CONST               4 (('timespec',))
               CALL_KW                  1
               STORE_FAST               7 (cutoff_iso)

253            BUILD_LIST               0
               STORE_FAST               8 (warnings)

254            LOAD_GLOBAL             27 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (brokerage_id)
               LOAD_GLOBAL             28 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       39 (to L2)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (brokerage_id)
               LOAD_ATTR               31 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_FALSE       17 (to L2)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (brokerage_id)
               LOAD_ATTR               31 (strip + NULL|self)
               CALL                     0
               JUMP_FORWARD             1 (to L3)
       L2:     LOAD_CONST               1 (None)
       L3:     STORE_FAST               9 (bid)

255            LOAD_GLOBAL             27 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (source)
               LOAD_GLOBAL             28 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       39 (to L4)
               NOT_TAKEN
               LOAD_FAST_BORROW         1 (source)
               LOAD_ATTR               31 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_FALSE       17 (to L4)
               NOT_TAKEN
               LOAD_FAST_BORROW         1 (source)
               LOAD_ATTR               31 (strip + NULL|self)
               CALL                     0
               JUMP_FORWARD             1 (to L5)
       L4:     LOAD_CONST               1 (None)
       L5:     STORE_FAST              10 (src)

256            LOAD_FAST_BORROW        10 (src)
               POP_JUMP_IF_NONE        48 (to L8)
               NOT_TAKEN
               LOAD_FAST_BORROW        10 (src)
               LOAD_GLOBAL             32 (_ALLOWED_SOURCES)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       37 (to L8)
               NOT_TAKEN

258            LOAD_CONST               5 ('status')
               LOAD_CONST               6 ('failed')

259            LOAD_CONST               7 ('mode')
               LOAD_FAST_BORROW         4 (execute)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               8 ('execute')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               9 ('dry-run')

260    L7:     LOAD_CONST              10 ('older_than_hours')
               LOAD_FAST_BORROW         2 (older_than_hours)

261            LOAD_CONST              11 ('limit')
               LOAD_FAST_BORROW         3 (limit)

262            LOAD_CONST              12 ('older_than_iso')
               LOAD_FAST_BORROW         7 (cutoff_iso)

263            LOAD_CONST              13 ('brokerage_id')
               LOAD_FAST_BORROW         9 (bid)

264            LOAD_CONST              14 ('source')
               LOAD_FAST_BORROW        10 (src)

265            LOAD_CONST              15 ('candidate_count')
               LOAD_SMALL_INT           0

266            LOAD_CONST              16 ('deleted_count')
               LOAD_SMALL_INT           0

267            LOAD_CONST              17 ('by_source')
               BUILD_MAP                0

268            LOAD_CONST              18 ('warnings')
               LOAD_FAST_BORROW         8 (warnings)

269            LOAD_CONST              19 ('error_code')
               LOAD_CONST              20 ('invalid_source')

257            BUILD_MAP               12
               RETURN_VALUE

272    L8:     LOAD_GLOBAL             35 (_get_db_safe + NULL)
               CALL                     0
               STORE_FAST              11 (db)

273            LOAD_FAST_BORROW        11 (db)
               POP_JUMP_IF_NOT_NONE    54 (to L11)
               NOT_TAKEN

274            LOAD_FAST_BORROW         8 (warnings)
               LOAD_ATTR               37 (append + NULL|self)
               LOAD_CONST              21 ('durable_email_dedupe_unavailable')
               CALL                     1
               POP_TOP

276            LOAD_CONST               5 ('status')
               LOAD_CONST              22 ('skipped')

277            LOAD_CONST               7 ('mode')
               LOAD_FAST_BORROW         4 (execute)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               8 ('execute')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               9 ('dry-run')

278   L10:     LOAD_CONST              10 ('older_than_hours')
               LOAD_FAST_BORROW         2 (older_than_hours)

279            LOAD_CONST              11 ('limit')
               LOAD_FAST_BORROW         3 (limit)

280            LOAD_CONST              12 ('older_than_iso')
               LOAD_FAST_BORROW         7 (cutoff_iso)

281            LOAD_CONST              13 ('brokerage_id')
               LOAD_FAST_BORROW         9 (bid)

282            LOAD_CONST              14 ('source')
               LOAD_FAST_BORROW        10 (src)

283            LOAD_CONST              15 ('candidate_count')
               LOAD_SMALL_INT           0

284            LOAD_CONST              16 ('deleted_count')
               LOAD_SMALL_INT           0

285            LOAD_CONST              17 ('by_source')
               BUILD_MAP                0

286            LOAD_CONST              18 ('warnings')
               LOAD_FAST_BORROW         8 (warnings)

287            LOAD_CONST              19 ('error_code')
               LOAD_CONST               1 (None)

275            BUILD_MAP               12
               RETURN_VALUE

292   L11:     LOAD_GLOBAL             39 (_list_expired + NULL)

293            LOAD_FAST_BORROW        11 (db)

294            LOAD_FAST_BORROW         9 (bid)

295            LOAD_FAST_BORROW        10 (src)

296            LOAD_FAST_BORROW         7 (cutoff_iso)

297            LOAD_FAST_BORROW         3 (limit)

292            LOAD_CONST              23 (('brokerage_id', 'source', 'older_than_iso', 'limit'))
               CALL_KW                  5
               STORE_FAST              12 (listing)

299            LOAD_FAST_BORROW        12 (listing)
               LOAD_CONST               5 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST              24 ('ok')
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE       62 (to L15)
               NOT_TAKEN

301            LOAD_CONST               5 ('status')
               LOAD_CONST               6 ('failed')

302            LOAD_CONST               7 ('mode')
               LOAD_FAST_BORROW         4 (execute)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_CONST               8 ('execute')
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST               9 ('dry-run')

303   L13:     LOAD_CONST              10 ('older_than_hours')
               LOAD_FAST                2 (older_than_hours)

304            LOAD_CONST              11 ('limit')
               LOAD_FAST                3 (limit)

305            LOAD_CONST              12 ('older_than_iso')
               LOAD_FAST                7 (cutoff_iso)

306            LOAD_CONST              13 ('brokerage_id')
               LOAD_FAST                9 (bid)

307            LOAD_CONST              14 ('source')
               LOAD_FAST               10 (src)

308            LOAD_CONST              15 ('candidate_count')
               LOAD_SMALL_INT           0

309            LOAD_CONST              16 ('deleted_count')
               LOAD_SMALL_INT           0

310            LOAD_CONST              17 ('by_source')
               BUILD_MAP                0

311            LOAD_CONST              18 ('warnings')
               LOAD_FAST                8 (warnings)

312            LOAD_CONST              19 ('error_code')
               LOAD_FAST_BORROW        12 (listing)
               LOAD_ATTR               41 (get + NULL|self)
               LOAD_CONST              19 ('error_code')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L14)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              25 ('db_read_failed')

300   L14:     BUILD_MAP               12
               RETURN_VALUE

314   L15:     LOAD_FAST_BORROW        12 (listing)
               LOAD_CONST              26 ('rows')
               BINARY_OP               26 ([])
               STORE_FAST              13 (rows)

315            LOAD_GLOBAL             43 (_summarise_rows + NULL)
               LOAD_FAST_BORROW        13 (rows)
               CALL                     1
               STORE_FAST              14 (bucketed)

316            LOAD_GLOBAL             45 (len + NULL)
               LOAD_FAST_BORROW        13 (rows)
               CALL                     1
               STORE_FAST              15 (candidate_count)

318            LOAD_FAST_BORROW         4 (execute)
               TO_BOOL
               POP_JUMP_IF_TRUE        27 (to L16)
               NOT_TAKEN

320            LOAD_CONST               5 ('status')
               LOAD_CONST              24 ('ok')

321            LOAD_CONST               7 ('mode')
               LOAD_CONST               9 ('dry-run')

322            LOAD_CONST              10 ('older_than_hours')
               LOAD_FAST_BORROW         2 (older_than_hours)

323            LOAD_CONST              11 ('limit')
               LOAD_FAST_BORROW         3 (limit)

324            LOAD_CONST              12 ('older_than_iso')
               LOAD_FAST_BORROW         7 (cutoff_iso)

325            LOAD_CONST              13 ('brokerage_id')
               LOAD_FAST_BORROW         9 (bid)

326            LOAD_CONST              14 ('source')
               LOAD_FAST_BORROW        10 (src)

327            LOAD_CONST              15 ('candidate_count')
               LOAD_FAST_BORROW        15 (candidate_count)

328            LOAD_CONST              16 ('deleted_count')
               LOAD_SMALL_INT           0

329            LOAD_CONST              17 ('by_source')
               LOAD_FAST_BORROW        14 (bucketed)

330            LOAD_CONST              18 ('warnings')
               LOAD_FAST_BORROW         8 (warnings)

331            LOAD_CONST              19 ('error_code')
               LOAD_CONST               1 (None)

319            BUILD_MAP               12
               RETURN_VALUE

335   L16:     LOAD_GLOBAL             47 (_delete_expired + NULL)

336            LOAD_FAST_BORROW        11 (db)

337            LOAD_FAST_BORROW         9 (bid)

338            LOAD_FAST_BORROW        10 (src)

339            LOAD_FAST_BORROW         7 (cutoff_iso)

335            LOAD_CONST              27 (('brokerage_id', 'source', 'older_than_iso'))
               CALL_KW                  4
               STORE_FAST              16 (delete_env)

341            LOAD_FAST_BORROW        16 (delete_env)
               LOAD_CONST               5 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST              24 ('ok')
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE       52 (to L18)
               NOT_TAKEN

343            LOAD_CONST               5 ('status')
               LOAD_CONST               6 ('failed')

344            LOAD_CONST               7 ('mode')
               LOAD_CONST               8 ('execute')

345            LOAD_CONST              10 ('older_than_hours')
               LOAD_FAST                2 (older_than_hours)

346            LOAD_CONST              11 ('limit')
               LOAD_FAST                3 (limit)

347            LOAD_CONST              12 ('older_than_iso')
               LOAD_FAST                7 (cutoff_iso)

348            LOAD_CONST              13 ('brokerage_id')
               LOAD_FAST                9 (bid)

349            LOAD_CONST              14 ('source')
               LOAD_FAST               10 (src)

350            LOAD_CONST              15 ('candidate_count')
               LOAD_FAST               15 (candidate_count)

351            LOAD_CONST              16 ('deleted_count')
               LOAD_SMALL_INT           0

352            LOAD_CONST              17 ('by_source')
               LOAD_FAST               14 (bucketed)

353            LOAD_CONST              18 ('warnings')
               LOAD_FAST                8 (warnings)

354            LOAD_CONST              19 ('error_code')
               LOAD_FAST_BORROW        16 (delete_env)
               LOAD_ATTR               41 (get + NULL|self)
               LOAD_CONST              19 ('error_code')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L17)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              28 ('db_write_failed')

342   L17:     BUILD_MAP               12
               RETURN_VALUE

357   L18:     LOAD_CONST               5 ('status')
               LOAD_CONST              24 ('ok')

358            LOAD_CONST               7 ('mode')
               LOAD_CONST               8 ('execute')

359            LOAD_CONST              10 ('older_than_hours')
               LOAD_FAST_BORROW         2 (older_than_hours)

360            LOAD_CONST              11 ('limit')
               LOAD_FAST_BORROW         3 (limit)

361            LOAD_CONST              12 ('older_than_iso')
               LOAD_FAST_BORROW         7 (cutoff_iso)

362            LOAD_CONST              13 ('brokerage_id')
               LOAD_FAST_BORROW         9 (bid)

363            LOAD_CONST              14 ('source')
               LOAD_FAST_BORROW        10 (src)

364            LOAD_CONST              15 ('candidate_count')
               LOAD_FAST_BORROW        15 (candidate_count)

365            LOAD_CONST              16 ('deleted_count')
               LOAD_GLOBAL             49 (int + NULL)
               LOAD_FAST_BORROW        16 (delete_env)
               LOAD_ATTR               41 (get + NULL|self)
               LOAD_CONST              29 ('deleted')
               LOAD_SMALL_INT           0
               CALL                     2
               CALL                     1

366            LOAD_CONST              17 ('by_source')
               LOAD_FAST_BORROW        14 (bucketed)

367            LOAD_CONST              18 ('warnings')
               LOAD_FAST_BORROW         8 (warnings)

368            LOAD_CONST              19 ('error_code')
               LOAD_CONST               1 (None)

356            BUILD_MAP               12
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts\reap_email_dedupe.py", line 376>:
376           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C181B03C0, file "scripts\reap_email_dedupe.py", line 376>:
376           RESUME                   0

377           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

378           LOAD_CONST               0 ('reap_email_dedupe')

380           LOAD_CONST               1 ('PAS167 — Operator-only reaper for expired rows in pas_email_dedupe_keys. Dry-run by default; --execute is required to actually delete. NEVER prints dedupe keys or PII (the table has none).')

377           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

386           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

387           LOAD_CONST               3 ('--brokerage-id')
              LOAD_CONST               4 (None)

388           LOAD_CONST               5 ('Optional brokerage scope.')

386           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

390           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

391           LOAD_CONST               7 ('--source')
              LOAD_CONST               4 (None)

393           LOAD_CONST               8 ('Optional source scope. One of: ')

394           LOAD_CONST               9 (', ')
              LOAD_ATTR                7 (join + NULL|self)
              LOAD_GLOBAL              8 (_ALLOWED_SOURCES)
              CALL                     1

393           BINARY_OP                0 (+)

390           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

397           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

398           LOAD_CONST              10 ('--older-than-hours')
              LOAD_GLOBAL             10 (int)
              LOAD_GLOBAL             12 (_DEFAULT_OLDER_THAN_HOURS)

400           LOAD_CONST              11 ('Rows whose expires_at is older than this many hours are eligible. Clamped to [')

402           LOAD_GLOBAL             14 (_MIN_OLDER_THAN_HOURS)
              FORMAT_SIMPLE
              LOAD_CONST               9 (', ')
              LOAD_GLOBAL             16 (_MAX_OLDER_THAN_HOURS)
              FORMAT_SIMPLE
              LOAD_CONST              12 (']. Default ')

403           LOAD_GLOBAL             12 (_DEFAULT_OLDER_THAN_HOURS)
              FORMAT_SIMPLE
              LOAD_CONST              13 ('.')

400           BUILD_STRING             7

397           LOAD_CONST              14 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

406           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

407           LOAD_CONST              15 ('--limit')
              LOAD_GLOBAL             10 (int)
              LOAD_GLOBAL             18 (_DEFAULT_LIMIT)

409           LOAD_CONST              16 ('Cap on the candidate listing. Clamped to [')

410           LOAD_GLOBAL             20 (_MIN_LIMIT)
              FORMAT_SIMPLE
              LOAD_CONST               9 (', ')
              LOAD_GLOBAL             22 (_MAX_LIMIT)
              FORMAT_SIMPLE
              LOAD_CONST              12 (']. Default ')
              LOAD_GLOBAL             18 (_DEFAULT_LIMIT)
              FORMAT_SIMPLE
              LOAD_CONST              13 ('.')

409           BUILD_STRING             7

406           LOAD_CONST              14 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

413           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

414           LOAD_CONST              17 ('--json')
              LOAD_CONST              18 ('store_true')

415           LOAD_CONST              19 ('Emit the structural report as JSON on stdout.')

413           LOAD_CONST              20 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

417           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

418           LOAD_CONST              21 ('--execute')
              LOAD_CONST              18 ('store_true')

420           LOAD_CONST              22 ('Actually delete the rows. Without this flag the reaper runs in dry-run mode and prints a count only.')

417           LOAD_CONST              20 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

425           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts\reap_email_dedupe.py", line 428>:
428           RESUME                   0
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
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _print_summary at 0x0000018C17F7ECB0, file "scripts\reap_email_dedupe.py", line 428>:
428           RESUME                   0

429           LOAD_GLOBAL              1 (print + NULL)

430           LOAD_CONST               0 ('[PAS167-reaper] status=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('status')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' mode=')

431           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('mode')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' older_than_hours=')

432           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('older_than_hours')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' limit=')

433           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('limit')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' candidates=')

434           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('candidate_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' deleted=')

435           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('deleted_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

430           BUILD_STRING            12

429           CALL                     1
              POP_TOP

437           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              12 ('warnings')
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       31 (to L3)
              NOT_TAKEN

438           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              12 ('warnings')
              BINARY_OP               26 ([])
              GET_ITER
      L1:     FOR_ITER                17 (to L2)
              STORE_FAST               1 (w)

439           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('  warning: ')
              LOAD_FAST_BORROW         1 (w)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L1)

438   L2:     END_FOR
              POP_ITER

440   L3:     LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              14 ('error_code')
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       22 (to L4)
              NOT_TAKEN

441           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  error_code: ')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              14 ('error_code')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP

442   L4:     LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              16 ('by_source')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L5:     STORE_FAST               2 (by_src)

443           LOAD_FAST_BORROW         2 (by_src)
              TO_BOOL
              POP_JUMP_IF_FALSE       69 (to L8)
              NOT_TAKEN

444           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              17 ('  by_source:')
              CALL                     1
              POP_TOP

445           LOAD_GLOBAL              5 (sorted + NULL)
              LOAD_FAST_BORROW         2 (by_src)
              LOAD_ATTR                7 (keys + NULL|self)
              CALL                     0
              CALL                     1
              GET_ITER
      L6:     FOR_ITER                26 (to L7)
              STORE_FAST               3 (src)

446           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              18 ('    ')
              LOAD_FAST_BORROW         3 (src)
              FORMAT_SIMPLE
              LOAD_CONST              19 (': ')
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (by_src, src)
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           28 (to L6)

445   L7:     END_FOR
              POP_ITER
              LOAD_CONST              20 (None)
              RETURN_VALUE

443   L8:     LOAD_CONST              20 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts\reap_email_dedupe.py", line 449>:
449           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D869F0, file "scripts\reap_email_dedupe.py", line 449>:
 449            RESUME                   0

 450            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 451            NOP

 452    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 456    L2:     LOAD_GLOBAL             11 (reap + NULL)

 457            LOAD_FAST                2 (args)
                LOAD_ATTR               12 (brokerage_id)

 458            LOAD_FAST                2 (args)
                LOAD_ATTR               14 (source)

 459            LOAD_FAST                2 (args)
                LOAD_ATTR               16 (older_than_hours)

 460            LOAD_FAST                2 (args)
                LOAD_ATTR               18 (limit)

 461            LOAD_GLOBAL             21 (bool + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               22 (execute)
                CALL                     1

 456            LOAD_CONST               2 (('brokerage_id', 'source', 'older_than_hours', 'limit', 'execute'))
                CALL_KW                  5
                STORE_FAST               4 (report)

 464            LOAD_FAST                2 (args)
                LOAD_ATTR               24 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       36 (to L3)
                NOT_TAKEN

 465            LOAD_GLOBAL             27 (print + NULL)
                LOAD_GLOBAL             24 (json)
                LOAD_ATTR               28 (dumps)
                PUSH_NULL
                LOAD_FAST                4 (report)
                LOAD_SMALL_INT           2
                LOAD_CONST               3 (True)
                LOAD_CONST               4 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP
                JUMP_FORWARD            11 (to L4)

 467    L3:     LOAD_GLOBAL             31 (_print_summary + NULL)
                LOAD_FAST                4 (report)
                CALL                     1
                POP_TOP

 469    L4:     LOAD_FAST                4 (report)
                LOAD_ATTR               33 (get + NULL|self)
                LOAD_CONST               5 ('status')
                CALL                     1
                STORE_FAST               5 (status)

 470            LOAD_FAST                5 (status)
                LOAD_CONST               6 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_TRUE         8 (to L5)
                NOT_TAKEN
                LOAD_FAST                5 (status)
                LOAD_CONST               7 ('skipped')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN

 471    L5:     LOAD_SMALL_INT           0
                RETURN_VALUE

 472    L6:     LOAD_FAST                5 (status)
                LOAD_CONST               8 ('failed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN

 473            LOAD_SMALL_INT           1
                RETURN_VALUE

 474    L7:     LOAD_SMALL_INT           1
                RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

 453            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 454    L9:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST               9 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L14)
       L10:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                LOAD_SMALL_INT           0
       L13:     CALL                     1
       L14:     SWAP                     2
       L15:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L16:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 453   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L8 [0]
  L8 to L9 -> L18 [1] lasti
  L9 to L11 -> L16 [1] lasti
  L12 to L14 -> L16 [1] lasti
  L14 to L15 -> L18 [1] lasti
  L16 to L18 -> L18 [1] lasti
```
