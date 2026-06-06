# scripts_readiness/run_daily_ops_checklist_report

- **pyc:** `scripts\__pycache__\run_daily_ops_checklist_report.cpython-314.pyc`
- **expected source path (absent):** `scripts/run_daily_ops_checklist_report.py`
- **co_filename (from bytecode):** `scripts/run_daily_ops_checklist_report.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS188 — Operator-run daily ops checklist report runner.

A **read-only** Python script the daily-ops operator runs
ONCE PER DAY by hand. Walks the existing /ops/* HTTP
endpoints, composes a fleet-wide checklist report, prints
an ANSI-coloured summary, and writes
``daily_ops_report_YYYY-MM-DD.json``.

This script is the operator-side tool requested by
PAS186 § 11 (operational scaling roadmap). It is NOT a
scheduler. It is NOT a cron job. It does NOT install
itself anywhere. It does NOT auto-remediate. It simply
queries existing read-only endpoints and produces a
report file.

Usage:

    python scripts/run_daily_ops_checklist_report.py \
        --base-url https://<pas-prod-url> \
        --admin-key-env ADMIN_API_KEY \
        [--brokerage-ids b1,b2,b3] \
        [--output daily_ops_report_2026-05-17.json] \
        [--summary-only] [--json]

Exit codes:
  0 — all endpoints responded; report written
  1 — one or more endpoints returned non-2xx (operator
      should investigate)
  2 — bad CLI args / missing admin key
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `argparse`, `date`, `datetime`, `json`, `os`, `sys`, `time`, `timezone`, `typing`, `urllib.error`, `urllib.request`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_compose_report`, `_fetch`, `_maybe_notify`, `_now_iso`, `_slack_notify`, `_summarise`, `_today_iso`, `main`

## Env-key candidates

`ADMIN_API_KEY`, `DEGRADED`, `GET`, `PAS188`, `PAS_BASE_URL`, `POST`

## String constants (redacted where noted)

- '\nPAS188 — Operator-run daily ops checklist report runner.\n\nA **read-only** Python script the daily-ops operator runs\nONCE PER DAY by hand. Walks the existing /ops/* HTTP\nendpoints, composes a fleet-wide checklist report, prints\nan ANSI-coloured summary, and writes\n``daily_ops_report_YYYY-MM-DD.json``.\n\nThis script is the operator-side tool requested by\nPAS186 § 11 (operational scaling roadmap). It is NOT a\nscheduler. It is NOT a cron job. It does NOT install\nitself anywhere. It does NOT auto-remediate. It simply\nqueries existing read-only endpoints and produces a\nreport file.\n\nUsage:\n\n    python scripts/run_daily_ops_checklist_report.py \\\n        --base-url https://<pas-prod-url> \\\n        --admin-key-env ADMIN_API_KEY \\\n        [--brokerage-ids b1,b2,b3] \\\n        [--output daily_ops_report_2026-05-17.json] \\\n        [--summary-only] [--json]\n\nExit codes:\n  0 — all endpoints responded; report written\n  1 — one or more endpoints returned non-2xx (operator\n      should investigate)\n  2 — bad CLI args / missing admin key\n'
- 'utf-8'
- 'timeout'
- 'return'
- 'str'
- 'seconds'
- 'base_url'
- 'path'
- 'admin_key'
- 'float'
- 'Dict[str, Any]'
- 'X-Admin-Key'
- 'Accept'
- 'application/json'
- 'User-Agent'
- 'pas-daily-ops-runner/1.0'
- 'GET'
- 'http_status'
- 'body'
- 'raw'
- 'non-dict response'
- 'error'
- 'http_error:'
- 'transport_error:'
- 'report'
- 'List[str]'
- 'sections'
- '[PAS188-runner] date='
- 'run_date'
- ' verdict='
- 'verdict'
- ' endpoints='
- 'endpoint_count'
- ' ok='
- 'ok_count'
- ' failed='
- 'failed_count'
- '[ok]'
- '[FAIL]'
- '<20'
- ' http='
- 'webhook_url'
- 'PAS190 — best-effort Slack notify. Never raises. The\nwebhook URL is NEVER printed. Returns a structural\nenvelope describing the attempt.\n\nThe Slack message is a single line — no PII, no\noperator notes, no webhook echo. The runner prints\nonly the attempt status (ok / failed / skipped).'
- 'status'
- 'skipped'
- 'attempted'
- 'text'
- '[PAS190] daily ops report verdict='
- ' run_date='
- 'payload_encode_failed'
- 'Content-Type'
- 'POST'
- 'failed'
- 'unexpected:'
- 'notify_on_failure'
- 'bool'
- 'notify_on_warning'
- "Decide whether to fire the Slack notify based on the\niteration's verdict + flags."
- 'reason'
- 'no_webhook'
- 'no_notify_flag'
- 'verdict_not_eligible'
- 'brokerage_ids'
- 'Optional[List[str]]'
- 'Dict[str, Dict[str, Any]]'
- 'phase'
- 'PAS188'
- 'tool'
- 'run_daily_ops_checklist_report'
- 'generated_at'
- 'DEGRADED'
- 'argparse.ArgumentParser'
- 'PAS188 — Operator-run daily ops checklist report. Read-only HTTP. Never modifies anything. Not a cron job.'
- '--base-url'
- 'PAS_BASE_URL'
- 'http://localhost:8000'
- 'Base URL of the PAS deployment (default: $PAS_BASE_URL or localhost:8000).'
- '--admin-key-env'
- 'ADMIN_API_KEY'
- "Environment variable name containing the operator's admin API key."
- '--brokerage-ids'
- 'Optional comma-separated list of brokerage_ids to scope the report (informational; the routes still return fleet-wide data).'
- '--output'
- 'Output JSON path (default: daily_ops_report_YYYY-MM-DD.json).'
- '--timeout'
- 'Per-endpoint timeout in seconds (default '
- '--summary-only'
- 'store_true'
- "Don't write report file; print summary only."
- '--json'
- 'Print the full report JSON to stdout.'
- '--dry-run'
- 'Do not actually call endpoints; print the planned actions only.'
- '--watch'
- 'PAS189 — Loop --max-runs times with --interval-seconds between runs. Not a scheduler; not a daemon.'
- '--interval-seconds'
- 'PAS189 — Seconds between iterations (min '
- ', max '
- ', default '
- '--max-runs'
- 'PAS189 — Hard cap on the watch loop (min 1, max '
- '--slack-webhook-url'
- 'PAS190 — Optional Slack incoming-webhook URL. Posts a structural one-line summary on amber/red. The URL is NEVER printed. Failure to notify never fails the runner.'
- '--notify-on-failure'
- 'PAS190 — Post to the Slack webhook when any endpoint in the iteration returns non-2xx.'
- '--notify-on-warning'
- 'PAS190 — Post to the Slack webhook on partial failure (one or more endpoints DEGRADED but the overall verdict is not OK).'
- 'argv'
- 'int'
- 'error: environment variable '
- ' is empty; set it to your admin API key and re-run.'
- 'error: --base-url required.'
- '[dry-run] would GET '
- '[PAS189-watch] starting bounded watch loop: interval='
- 's max_runs='
- 'run_index'
- 'run_total'
- 'daily_ops_report_'
- '_run_'
- '.json'
- '[PAS189-watch] report written to '
- '  [warn] failed to write report at '
- '[PAS190-notify] slack_notify status='
- '[PAS189-watch] interrupted by user — exiting.'
- '[PAS189-watch] watch loop complete: runs='
- ' interval='
- '[PAS188-runner] report written to '

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ('\nPAS188 — Operator-run daily ops checklist report runner.\n\nA **read-only** Python script the daily-ops operator runs\nONCE PER DAY by hand. Walks the existing /ops/* HTTP\nendpoints, composes a fleet-wide checklist report, prints\nan ANSI-coloured summary, and writes\n``daily_ops_report_YYYY-MM-DD.json``.\n\nThis script is the operator-side tool requested by\nPAS186 § 11 (operational scaling roadmap). It is NOT a\nscheduler. It is NOT a cron job. It does NOT install\nitself anywhere. It does NOT auto-remediate. It simply\nqueries existing read-only endpoints and produces a\nreport file.\n\nUsage:\n\n    python scripts/run_daily_ops_checklist_report.py \\\n        --base-url https://<pas-prod-url> \\\n        --admin-key-env ADMIN_API_KEY \\\n        [--brokerage-ids b1,b2,b3] \\\n        [--output daily_ops_report_2026-05-17.json] \\\n        [--summary-only] [--json]\n\nExit codes:\n  0 — all endpoints responded; report written\n  1 — one or more endpoints returned non-2xx (operator\n      should investigate)\n  2 — bad CLI args / missing admin key\n')
               STORE_NAME               0 (__doc__)

  33           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  35           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  36           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  37           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  38           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  39           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (time)
               STORE_NAME               7 (time)

  40           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              8 (urllib.error)
               STORE_NAME               9 (urllib)

  41           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME             10 (urllib.request)
               STORE_NAME               9 (urllib)

  42           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('date', 'datetime', 'timezone'))
               IMPORT_NAME             11 (datetime)
               IMPORT_FROM             12 (date)
               STORE_NAME              12 (date)
               IMPORT_FROM             11 (datetime)
               STORE_NAME              11 (datetime)
               IMPORT_FROM             13 (timezone)
               STORE_NAME              13 (timezone)
               POP_TOP

  43           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
               IMPORT_NAME             14 (typing)
               IMPORT_FROM             15 (Any)
               STORE_NAME              15 (Any)
               IMPORT_FROM             16 (Dict)
               STORE_NAME              16 (Dict)
               IMPORT_FROM             17 (List)
               STORE_NAME              17 (List)
               IMPORT_FROM             18 (Optional)
               STORE_NAME              18 (Optional)
               POP_TOP

  46           LOAD_NAME                6 (sys)
               LOAD_ATTR               38 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               40 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              21 (_stream)

  47           NOP

  48   L2:     LOAD_NAME               21 (_stream)
               LOAD_ATTR               45 (reconfigure + NULL|self)
               LOAD_CONST               5 ('utf-8')
               LOAD_CONST               6 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  46   L4:     END_FOR
               POP_ITER

  53           LOAD_CONST               7 (15.0)
               STORE_NAME              24 (_DEFAULT_TIMEOUT)

  57           LOAD_CONST               8 (8.0)
               STORE_NAME              25 (_SLACK_NOTIFY_TIMEOUT)

  58           LOAD_CONST               9 (2048)
               STORE_NAME              26 (_SLACK_PAYLOAD_MAX_LEN)

  62           LOAD_SMALL_INT          60
               STORE_NAME              27 (_WATCH_INTERVAL_MIN)

  63           LOAD_CONST              10 (3600)
               STORE_NAME              28 (_WATCH_INTERVAL_MAX)

  64           LOAD_CONST              11 (300)
               STORE_NAME              29 (_WATCH_INTERVAL_DEFAULT)

  65           LOAD_CONST              12 (288)
               STORE_NAME              30 (_WATCH_MAX_RUNS_HARD)

  66           LOAD_SMALL_INT          12
               STORE_NAME              31 (_WATCH_MAX_RUNS_DEFAULT)

  73           LOAD_CONST              33 ((('fleet_status', '/ops/fleet/status?limit=200'), ('fleet_exceptions', '/ops/fleet/exceptions?limit=200'), ('fleet_rollout', '/ops/fleet/rollout-readiness?limit=200'), ('cutovers', '/ops/cutovers?limit=200'), ('daily_checklists', '/ops/daily-checklists?limit=200'), ('incidents_open', '/ops/incidents?status=OPEN&limit=200'), ('circuit_breakers', '/ops/circuit-breakers?limit=200'), ('learning_dashboard', '/ops/learning/dashboard'), ('pending_queue', '/ops/pending-calls/queue'), ('stale_dialing', '/ops/recovery/stale-dialing')))
               STORE_NAME              32 (_ENDPOINTS)

  91           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts/run_daily_ops_checklist_report.py", line 91>)
               MAKE_FUNCTION
               LOAD_CONST              14 (<code object _today_iso at 0x0000018C18052F70, file "scripts/run_daily_ops_checklist_report.py", line 91>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              33 (_today_iso)

  95           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts/run_daily_ops_checklist_report.py", line 95>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _now_iso at 0x0000018C18038A30, file "scripts/run_daily_ops_checklist_report.py", line 95>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_now_iso)

  99           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C18025830, file "scripts/run_daily_ops_checklist_report.py", line 99>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object _fetch at 0x0000018C17EA4720, file "scripts/run_daily_ops_checklist_report.py", line 99>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (_fetch)

 147           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts/run_daily_ops_checklist_report.py", line 147>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object _summarise at 0x0000018C17F7ECB0, file "scripts/run_daily_ops_checklist_report.py", line 147>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              36 (_summarise)

 166           LOAD_CONST              21 ('timeout')

 170           LOAD_NAME               25 (_SLACK_NOTIFY_TIMEOUT)

 166           BUILD_MAP                1
               LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18026030, file "scripts/run_daily_ops_checklist_report.py", line 166>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _slack_notify at 0x0000018C17ED9FB0, file "scripts/run_daily_ops_checklist_report.py", line 166>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              37 (_slack_notify)

 236           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C18024C30, file "scripts/run_daily_ops_checklist_report.py", line 236>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object _maybe_notify at 0x0000018C17D87580, file "scripts/run_daily_ops_checklist_report.py", line 236>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (_maybe_notify)

 261           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C18024B30, file "scripts/run_daily_ops_checklist_report.py", line 261>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object _compose_report at 0x0000018C179C3C30, file "scripts/run_daily_ops_checklist_report.py", line 261>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              39 (_compose_report)

 288           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts/run_daily_ops_checklist_report.py", line 288>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object _build_parser at 0x0000018C182DB4B0, file "scripts/run_daily_ops_checklist_report.py", line 288>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              40 (_build_parser)

 365           LOAD_CONST              34 ((None,))
               LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts/run_daily_ops_checklist_report.py", line 365>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object main at 0x0000018C17EA5CC0, file "scripts/run_daily_ops_checklist_report.py", line 365>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              41 (main)

 524           LOAD_NAME               42 (__name__)
               LOAD_CONST              32 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 525           LOAD_NAME                6 (sys)
               LOAD_ATTR               86 (exit)
               PUSH_NULL
               LOAD_NAME               41 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 524   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  49           LOAD_NAME               23 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

  50   L7:     POP_EXCEPT
               JUMP_BACKWARD          148 (to L1)

  49   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts/run_daily_ops_checklist_report.py", line 91>:
 91           RESUME                   0
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

Disassembly of <code object _today_iso at 0x0000018C18052F70, file "scripts/run_daily_ops_checklist_report.py", line 91>:
 91           RESUME                   0

 92           LOAD_GLOBAL              0 (date)
              LOAD_ATTR                2 (today)
              PUSH_NULL
              CALL                     0
              LOAD_ATTR                5 (isoformat + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts/run_daily_ops_checklist_report.py", line 95>:
 95           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038A30, file "scripts/run_daily_ops_checklist_report.py", line 95>:
 95           RESUME                   0

 96           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C18025830, file "scripts/run_daily_ops_checklist_report.py", line 99>:
 99           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('base_url')

100           LOAD_CONST               2 ('str')

 99           LOAD_CONST               3 ('path')

101           LOAD_CONST               2 ('str')

 99           LOAD_CONST               4 ('admin_key')

102           LOAD_CONST               2 ('str')

 99           LOAD_CONST               5 ('timeout')

103           LOAD_CONST               6 ('float')

 99           LOAD_CONST               7 ('return')

104           LOAD_CONST               8 ('Dict[str, Any]')

 99           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _fetch at 0x0000018C17EA4720, file "scripts/run_daily_ops_checklist_report.py", line 99>:
  99            RESUME                   0

 105            LOAD_FAST_BORROW         0 (base_url)
                LOAD_ATTR                1 (rstrip + NULL|self)
                LOAD_CONST               0 ('/')
                CALL                     1
                LOAD_FAST_BORROW         1 (path)
                BINARY_OP                0 (+)
                STORE_FAST               4 (url)

 106            LOAD_GLOBAL              2 (urllib)
                LOAD_ATTR                4 (request)
                LOAD_ATTR                7 (Request + NULL|self)

 107            LOAD_FAST_BORROW         4 (url)

 109            LOAD_CONST               1 ('X-Admin-Key')
                LOAD_FAST_BORROW         2 (admin_key)

 110            LOAD_CONST               2 ('Accept')
                LOAD_CONST               3 ('application/json')

 111            LOAD_CONST               4 ('User-Agent')
                LOAD_CONST               5 ('pas-daily-ops-runner/1.0')

 108            BUILD_MAP                3

 113            LOAD_CONST               6 ('GET')

 106            LOAD_CONST               7 (('headers', 'method'))
                CALL_KW                  3
                STORE_FAST               5 (req)

 115            NOP

 116    L1:     LOAD_GLOBAL              2 (urllib)
                LOAD_ATTR                4 (request)
                LOAD_ATTR                9 (urlopen + NULL|self)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (req, timeout)
                LOAD_CONST               8 (('timeout',))
                CALL_KW                  2
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L2:     STORE_FAST               6 (resp)

 117            LOAD_FAST_BORROW         6 (resp)
                LOAD_ATTR               10 (status)
                STORE_FAST               7 (status)

 118            LOAD_FAST_BORROW         6 (resp)
                LOAD_ATTR               13 (read + NULL|self)
                CALL                     0
                STORE_FAST               8 (raw)

 116    L3:     LOAD_CONST               9 (None)
                LOAD_CONST               9 (None)
                LOAD_CONST               9 (None)
                CALL                     3
                POP_TOP

 119    L4:     LOAD_FAST_CHECK          8 (raw)
                TO_BOOL
                POP_JUMP_IF_FALSE       38 (to L7)
        L5:     NOT_TAKEN
        L6:     LOAD_GLOBAL             14 (json)
                LOAD_ATTR               16 (loads)
                PUSH_NULL
                LOAD_FAST_BORROW         8 (raw)
                LOAD_ATTR               19 (decode + NULL|self)
                LOAD_CONST              10 ('utf-8')
                CALL                     1
                CALL                     1
                JUMP_FORWARD             1 (to L8)
        L7:     BUILD_MAP                0
        L8:     STORE_FAST               9 (body)

 121            LOAD_CONST              11 ('http_status')
                LOAD_GLOBAL             21 (int + NULL)
                LOAD_FAST_CHECK          7 (status)
                CALL                     1

 122            LOAD_CONST              12 ('ok')
                LOAD_SMALL_INT         200
                LOAD_GLOBAL             21 (int + NULL)
                LOAD_FAST_BORROW         7 (status)
                CALL                     1
                SWAP                     2
                COPY                     2
                COMPARE_OP              42 (<=)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L9)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              13 (300)
                COMPARE_OP               2 (<)
                JUMP_FORWARD             2 (to L10)
        L9:     SWAP                     2
                POP_TOP

 123   L10:     LOAD_CONST              14 ('body')
                LOAD_GLOBAL             23 (isinstance + NULL)
                LOAD_FAST_BORROW         9 (body)
                LOAD_GLOBAL             24 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN
                LOAD_FAST                9 (body)
                JUMP_FORWARD             3 (to L12)
       L11:     LOAD_CONST              15 ('raw')
                LOAD_CONST              16 ('non-dict response')
                BUILD_MAP                1

 124   L12:     LOAD_CONST              17 ('error')
                LOAD_CONST               9 (None)

 120            BUILD_MAP                4
       L13:     RETURN_VALUE

 116   L14:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L15)
                NOT_TAKEN
                RERAISE                  2
       L15:     POP_TOP
       L16:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_BACKWARD_NO_INTERRUPT 137 (to L4)

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L18:     PUSH_EXC_INFO

 126            LOAD_GLOBAL              2 (urllib)
                LOAD_ATTR               26 (error)
                LOAD_ATTR               28 (HTTPError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      171 (to L37)
                NOT_TAKEN
                STORE_FAST              10 (e)

 127   L19:     NOP

 128   L20:     LOAD_FAST               10 (e)
                LOAD_ATTR               13 (read + NULL|self)
                CALL                     0
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L21)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              18 (b'')
       L21:     STORE_FAST               8 (raw)

 129            LOAD_FAST                8 (raw)
                TO_BOOL
                POP_JUMP_IF_FALSE       38 (to L24)
       L22:     NOT_TAKEN
       L23:     LOAD_GLOBAL             14 (json)
                LOAD_ATTR               16 (loads)
                PUSH_NULL
                LOAD_FAST                8 (raw)
                LOAD_ATTR               19 (decode + NULL|self)
                LOAD_CONST              10 ('utf-8')
                CALL                     1
                CALL                     1
                JUMP_FORWARD             1 (to L25)
       L24:     BUILD_MAP                0
       L25:     STORE_FAST               9 (body)
       L26:     JUMP_FORWARD            19 (to L31)

  --   L27:     PUSH_EXC_INFO

 130            LOAD_GLOBAL             30 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L29)
                NOT_TAKEN
                POP_TOP

 131            BUILD_MAP                0
                STORE_FAST               9 (body)
       L28:     POP_EXCEPT
                JUMP_FORWARD             4 (to L31)

 130   L29:     RERAISE                  0

  --   L30:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 133   L31:     LOAD_CONST              11 ('http_status')
                LOAD_GLOBAL             21 (int + NULL)
                LOAD_FAST               10 (e)
                LOAD_ATTR               32 (code)
                CALL                     1

 134            LOAD_CONST              12 ('ok')
                LOAD_CONST              19 (False)

 135            LOAD_CONST              14 ('body')
                LOAD_GLOBAL             23 (isinstance + NULL)
                LOAD_FAST                9 (body)
                LOAD_GLOBAL             24 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L32)
                NOT_TAKEN
                LOAD_FAST                9 (body)
                JUMP_FORWARD             1 (to L33)
       L32:     BUILD_MAP                0

 136   L33:     LOAD_CONST              17 ('error')
                LOAD_CONST              20 ('http_error:')
                LOAD_FAST               10 (e)
                LOAD_ATTR               32 (code)
                FORMAT_SIMPLE
                BUILD_STRING             2

 132            BUILD_MAP                4
       L34:     SWAP                     2
       L35:     POP_EXCEPT
                LOAD_CONST               9 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RETURN_VALUE

  --   L36:     LOAD_CONST               9 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 138   L37:     LOAD_GLOBAL             30 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       43 (to L44)
       L38:     NOT_TAKEN
       L39:     STORE_FAST              10 (e)

 140   L40:     LOAD_CONST              11 ('http_status')
                LOAD_SMALL_INT           0

 141            LOAD_CONST              12 ('ok')
                LOAD_CONST              19 (False)

 142            LOAD_CONST              14 ('body')
                BUILD_MAP                0

 143            LOAD_CONST              17 ('error')
                LOAD_CONST              21 ('transport_error:')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 139            BUILD_MAP                4
       L41:     SWAP                     2
       L42:     POP_EXCEPT
                LOAD_CONST               9 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RETURN_VALUE

  --   L43:     LOAD_CONST               9 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 138   L44:     RERAISE                  0

  --   L45:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L18 [0]
  L2 to L3 -> L14 [2] lasti
  L3 to L5 -> L18 [0]
  L6 to L13 -> L18 [0]
  L14 to L16 -> L17 [4] lasti
  L16 to L18 -> L18 [0]
  L18 to L19 -> L45 [1] lasti
  L20 to L22 -> L27 [1]
  L23 to L26 -> L27 [1]
  L26 to L27 -> L36 [1] lasti
  L27 to L28 -> L30 [2] lasti
  L28 to L29 -> L36 [1] lasti
  L29 to L30 -> L30 [2] lasti
  L30 to L34 -> L36 [1] lasti
  L34 to L35 -> L45 [1] lasti
  L36 to L38 -> L45 [1] lasti
  L39 to L40 -> L45 [1] lasti
  L40 to L41 -> L43 [1] lasti
  L41 to L42 -> L45 [1] lasti
  L43 to L45 -> L45 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts/run_daily_ops_checklist_report.py", line 147>:
147           RESUME                   0
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
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _summarise at 0x0000018C17F7ECB0, file "scripts/run_daily_ops_checklist_report.py", line 147>:
147           RESUME                   0

148           BUILD_LIST               0
              STORE_FAST               1 (out)

149           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('sections')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L1:     STORE_FAST               2 (sections)

150           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                3 (append + NULL|self)

151           LOAD_CONST               1 ('[PAS188-runner] date=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               2 ('run_date')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST               3 (' verdict=')

152           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               4 ('verdict')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST               5 (' endpoints=')

153           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               6 ('endpoint_count')
              LOAD_SMALL_INT           0
              CALL                     2
              FORMAT_SIMPLE
              LOAD_CONST               7 (' ok=')

154           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               8 ('ok_count')
              LOAD_SMALL_INT           0
              CALL                     2
              FORMAT_SIMPLE
              LOAD_CONST               9 (' failed=')

155           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              10 ('failed_count')
              LOAD_SMALL_INT           0
              CALL                     2
              FORMAT_SIMPLE

151           BUILD_STRING            10

150           CALL                     1
              POP_TOP

157           LOAD_FAST_BORROW         2 (sections)
              LOAD_ATTR                5 (items + NULL|self)
              CALL                     0
              GET_ITER
      L2:     FOR_ITER               108 (to L6)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   52 (name, payload)

158           LOAD_FAST_BORROW         4 (payload)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              11 ('http_status')
              CALL                     1
              STORE_FAST               5 (http)

159           LOAD_FAST_BORROW         4 (payload)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              12 ('ok')
              CALL                     1
              STORE_FAST               6 (ok)

160           LOAD_FAST_BORROW         4 (payload)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              13 ('error')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST              14 ('')
      L3:     STORE_FAST               7 (err)

161           LOAD_FAST_BORROW         6 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST              15 ('[ok]')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST              16 ('[FAIL]')
      L5:     STORE_FAST               8 (marker)

162           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                3 (append + NULL|self)
              LOAD_CONST              17 ('  ')
              LOAD_FAST_BORROW         8 (marker)
              FORMAT_SIMPLE
              LOAD_CONST              18 (' ')
              LOAD_FAST_BORROW         3 (name)
              LOAD_CONST              19 ('<20')
              FORMAT_WITH_SPEC
              LOAD_CONST              20 (' http=')
              LOAD_FAST_BORROW         5 (http)
              FORMAT_SIMPLE
              LOAD_CONST              18 (' ')
              LOAD_FAST_BORROW         7 (err)
              FORMAT_SIMPLE
              BUILD_STRING             8
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          110 (to L2)

157   L6:     END_FOR
              POP_ITER

163           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026030, file "scripts/run_daily_ops_checklist_report.py", line 166>:
166           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('webhook_url')

168           LOAD_CONST               2 ('str')

166           LOAD_CONST               3 ('report')

169           LOAD_CONST               4 ('Dict[str, Any]')

166           LOAD_CONST               5 ('timeout')

170           LOAD_CONST               6 ('float')

166           LOAD_CONST               7 ('return')

171           LOAD_CONST               4 ('Dict[str, Any]')

166           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _slack_notify at 0x0000018C17ED9FB0, file "scripts/run_daily_ops_checklist_report.py", line 166>:
 166            RESUME                   0

 180            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('skipped')

 181            LOAD_CONST               3 ('attempted')
                LOAD_CONST               4 (False)

 182            LOAD_CONST               5 ('http_status')
                LOAD_SMALL_INT           0

 183            LOAD_CONST               6 ('error')
                LOAD_CONST               7 (None)

 179            BUILD_MAP                4
                STORE_FAST               3 (out)

 185            NOP

 186    L1:     LOAD_FAST                0 (webhook_url)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
        L2:     NOT_TAKEN
        L3:     POP_TOP
                LOAD_CONST               8 ('')
        L4:     LOAD_ATTR                1 (strip + NULL|self)
                CALL                     0
                STORE_FAST               4 (url)

 187            LOAD_FAST_BORROW         4 (url)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L5:     NOT_TAKEN

 188    L6:     LOAD_FAST_BORROW         3 (out)
        L7:     RETURN_VALUE

 191    L8:     LOAD_CONST               9 ('text')

 192            LOAD_CONST              10 ('[PAS190] daily ops report verdict=')
                LOAD_FAST_BORROW         1 (report)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              11 ('verdict')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              12 (' endpoints=')

 193            LOAD_FAST_BORROW         1 (report)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              13 ('endpoint_count')
                LOAD_SMALL_INT           0
                CALL                     2
                FORMAT_SIMPLE
                LOAD_CONST              14 (' ok=')

 194            LOAD_FAST_BORROW         1 (report)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              15 ('ok_count')
                LOAD_SMALL_INT           0
                CALL                     2
                FORMAT_SIMPLE
                LOAD_CONST              16 (' failed=')

 195            LOAD_FAST_BORROW         1 (report)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              17 ('failed_count')
                LOAD_SMALL_INT           0
                CALL                     2
                FORMAT_SIMPLE
                LOAD_CONST              18 (' run_date=')

 196            LOAD_FAST_BORROW         1 (report)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              19 ('run_date')
                CALL                     1
                FORMAT_SIMPLE

 192            BUILD_STRING            10

 197            LOAD_CONST               7 (None)
                LOAD_GLOBAL              4 (_SLACK_PAYLOAD_MAX_LEN)

 191            BINARY_SLICE

 190            BUILD_MAP                1
                STORE_FAST               5 (payload)

 199    L9:     NOP

 200   L10:     LOAD_GLOBAL              6 (json)
                LOAD_ATTR                8 (dumps)
                PUSH_NULL
                LOAD_FAST_BORROW         5 (payload)
                CALL                     1
                LOAD_ATTR               11 (encode + NULL|self)
                LOAD_CONST              20 ('utf-8')
                CALL                     1
                STORE_FAST               6 (data)

 204   L11:     LOAD_GLOBAL             14 (urllib)
                LOAD_ATTR               16 (request)
                LOAD_ATTR               19 (Request + NULL|self)

 205            LOAD_FAST                4 (url)

 206            LOAD_FAST                6 (data)

 208            LOAD_CONST              22 ('Content-Type')
                LOAD_CONST              23 ('application/json')

 209            LOAD_CONST              24 ('User-Agent')
                LOAD_CONST              25 ('pas-daily-ops-runner/1.0')

 207            BUILD_MAP                2

 211            LOAD_CONST              26 ('POST')

 204            LOAD_CONST              27 (('data', 'headers', 'method'))
                CALL_KW                  4
                STORE_FAST               7 (req)

 213            LOAD_CONST              28 (True)
                LOAD_FAST                3 (out)
                LOAD_CONST               3 ('attempted')
                STORE_SUBSCR

 214   L12:     NOP

 215   L13:     LOAD_GLOBAL             14 (urllib)
                LOAD_ATTR               16 (request)
                LOAD_ATTR               21 (urlopen + NULL|self)
                LOAD_FAST_LOAD_FAST    114 (req, timeout)
                LOAD_CONST              29 (('timeout',))
                CALL_KW                  2
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
       L14:     STORE_FAST               8 (resp)

 216            LOAD_GLOBAL             23 (int + NULL)
                LOAD_FAST                8 (resp)
                LOAD_ATTR               24 (status)
                CALL                     1
                LOAD_FAST                3 (out)
                LOAD_CONST               5 ('http_status')
                STORE_SUBSCR

 215   L15:     LOAD_CONST               7 (None)
                LOAD_CONST               7 (None)
                LOAD_CONST               7 (None)
                CALL                     3
                POP_TOP

 218   L16:     LOAD_SMALL_INT         200
                LOAD_FAST                3 (out)
                LOAD_CONST               5 ('http_status')
                BINARY_OP               26 ([])
                SWAP                     2
                COPY                     2
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE        8 (to L17)
                NOT_TAKEN
                LOAD_CONST              30 (300)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        6 (to L19)
                NOT_TAKEN
                JUMP_FORWARD             2 (to L18)
       L17:     POP_TOP
                JUMP_FORWARD             2 (to L19)
       L18:     LOAD_CONST              31 ('ok')
                JUMP_FORWARD             1 (to L20)
       L19:     LOAD_CONST              32 ('failed')

 217   L20:     LOAD_FAST                3 (out)
                LOAD_CONST               1 ('status')
                STORE_SUBSCR

 220            LOAD_FAST                3 (out)
       L21:     RETURN_VALUE

  --   L22:     PUSH_EXC_INFO

 201            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       14 (to L25)
                NOT_TAKEN
                POP_TOP

 202            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('skipped')
                LOAD_CONST               3 ('attempted')
                LOAD_CONST               4 (False)

 203            LOAD_CONST               5 ('http_status')
                LOAD_SMALL_INT           0
                LOAD_CONST               6 ('error')
                LOAD_CONST              21 ('payload_encode_failed')

 202            BUILD_MAP                4
                SWAP                     2
       L23:     POP_EXCEPT
       L24:     RETURN_VALUE

 201   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 215   L27:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L28)
                NOT_TAKEN
                RERAISE                  2
       L28:     POP_TOP
       L29:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_BACKWARD_NO_INTERRUPT 77 (to L16)

  --   L30:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L31:     PUSH_EXC_INFO

 221            LOAD_GLOBAL             14 (urllib)
                LOAD_ATTR               26 (error)
                LOAD_ATTR               28 (HTTPError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       60 (to L37)
                NOT_TAKEN
                STORE_FAST               9 (e)

 222   L32:     LOAD_GLOBAL             23 (int + NULL)
                LOAD_FAST                9 (e)
                LOAD_ATTR               30 (code)
                CALL                     1
                LOAD_FAST                3 (out)
                LOAD_CONST               5 ('http_status')
                STORE_SUBSCR

 223            LOAD_CONST              32 ('failed')
                LOAD_FAST                3 (out)
                LOAD_CONST               1 ('status')
                STORE_SUBSCR

 224            LOAD_CONST              33 ('http_error:')
                LOAD_FAST                9 (e)
                LOAD_ATTR               30 (code)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_FAST                3 (out)
                LOAD_CONST               6 ('error')
                STORE_SUBSCR

 225            LOAD_FAST                3 (out)
       L33:     SWAP                     2
       L34:     POP_EXCEPT
                LOAD_CONST               7 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
       L35:     RETURN_VALUE

  --   L36:     LOAD_CONST               7 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 226   L37:     LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       45 (to L45)
       L38:     NOT_TAKEN
       L39:     STORE_FAST               9 (e)

 227   L40:     LOAD_CONST              32 ('failed')
                LOAD_FAST                3 (out)
                LOAD_CONST               1 ('status')
                STORE_SUBSCR

 228            LOAD_CONST              34 ('transport_error:')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_FAST                3 (out)
                LOAD_CONST               6 ('error')
                STORE_SUBSCR

 229            LOAD_FAST                3 (out)
       L41:     SWAP                     2
       L42:     POP_EXCEPT
                LOAD_CONST               7 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
       L43:     RETURN_VALUE

  --   L44:     LOAD_CONST               7 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 226   L45:     RERAISE                  0

  --   L46:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L47:     PUSH_EXC_INFO

 230            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       43 (to L52)
                NOT_TAKEN
                STORE_FAST               9 (e)

 231   L48:     LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('skipped')
                LOAD_CONST               3 ('attempted')
                LOAD_CONST               4 (False)

 232            LOAD_CONST               5 ('http_status')
                LOAD_SMALL_INT           0

 233            LOAD_CONST               6 ('error')
                LOAD_CONST              35 ('unexpected:')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 231            BUILD_MAP                4
       L49:     SWAP                     2
       L50:     POP_EXCEPT
                LOAD_CONST               7 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RETURN_VALUE

  --   L51:     LOAD_CONST               7 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 230   L52:     RERAISE                  0

  --   L53:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L47 [0]
  L3 to L5 -> L47 [0]
  L6 to L7 -> L47 [0]
  L8 to L9 -> L47 [0]
  L10 to L11 -> L22 [0]
  L11 to L12 -> L47 [0]
  L13 to L14 -> L31 [0]
  L14 to L15 -> L27 [2] lasti
  L15 to L21 -> L31 [0]
  L22 to L23 -> L26 [1] lasti
  L23 to L24 -> L47 [0]
  L25 to L26 -> L26 [1] lasti
  L26 to L27 -> L47 [0]
  L27 to L29 -> L30 [4] lasti
  L29 to L31 -> L31 [0]
  L31 to L32 -> L46 [1] lasti
  L32 to L33 -> L36 [1] lasti
  L33 to L34 -> L46 [1] lasti
  L34 to L35 -> L47 [0]
  L36 to L38 -> L46 [1] lasti
  L39 to L40 -> L46 [1] lasti
  L40 to L41 -> L44 [1] lasti
  L41 to L42 -> L46 [1] lasti
  L42 to L43 -> L47 [0]
  L44 to L46 -> L46 [1] lasti
  L46 to L47 -> L47 [0]
  L47 to L48 -> L53 [1] lasti
  L48 to L49 -> L51 [1] lasti
  L49 to L50 -> L53 [1] lasti
  L51 to L53 -> L53 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "scripts/run_daily_ops_checklist_report.py", line 236>:
236           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('webhook_url')

238           LOAD_CONST               2 ('str')

236           LOAD_CONST               3 ('notify_on_failure')

239           LOAD_CONST               4 ('bool')

236           LOAD_CONST               5 ('notify_on_warning')

240           LOAD_CONST               4 ('bool')

236           LOAD_CONST               6 ('report')

241           LOAD_CONST               7 ('Dict[str, Any]')

236           LOAD_CONST               8 ('return')

242           LOAD_CONST               7 ('Dict[str, Any]')

236           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _maybe_notify at 0x0000018C17D87580, file "scripts/run_daily_ops_checklist_report.py", line 236>:
236           RESUME                   0

245           LOAD_FAST                0 (webhook_url)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     LOAD_ATTR                1 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         9 (to L2)
              NOT_TAKEN

246           LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('skipped')
              LOAD_CONST               4 ('attempted')
              LOAD_CONST               5 (False)

247           LOAD_CONST               6 ('reason')
              LOAD_CONST               7 ('no_webhook')

246           BUILD_MAP                3
              RETURN_VALUE

248   L2:     LOAD_FAST_BORROW         1 (notify_on_failure)
              TO_BOOL
              POP_JUMP_IF_TRUE        17 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (notify_on_warning)
              TO_BOOL
              POP_JUMP_IF_TRUE         9 (to L3)
              NOT_TAKEN

249           LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('skipped')
              LOAD_CONST               4 ('attempted')
              LOAD_CONST               5 (False)

250           LOAD_CONST               6 ('reason')
              LOAD_CONST               8 ('no_notify_flag')

249           BUILD_MAP                3
              RETURN_VALUE

251   L3:     LOAD_FAST_BORROW         3 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               9 ('verdict')
              CALL                     1
              STORE_FAST               4 (verdict)

252           LOAD_GLOBAL              5 (int + NULL)
              LOAD_FAST_BORROW         3 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              10 ('failed_count')
              LOAD_SMALL_INT           0
              CALL                     2
              CALL                     1
              STORE_FAST               5 (failed_count)

253           LOAD_FAST_BORROW         5 (failed_count)
              LOAD_SMALL_INT           0
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       21 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (notify_on_failure)
              TO_BOOL
              POP_JUMP_IF_FALSE       13 (to L4)
              NOT_TAKEN

254           LOAD_GLOBAL              7 (_slack_notify + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 3 (webhook_url, report)
              LOAD_CONST              11 (('webhook_url', 'report'))
              CALL_KW                  2
              RETURN_VALUE

255   L4:     LOAD_FAST_BORROW         4 (verdict)
              LOAD_CONST              12 ('OK')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE       21 (to L5)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (notify_on_warning)
              TO_BOOL
              POP_JUMP_IF_FALSE       13 (to L5)
              NOT_TAKEN

256           LOAD_GLOBAL              7 (_slack_notify + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 3 (webhook_url, report)
              LOAD_CONST              11 (('webhook_url', 'report'))
              CALL_KW                  2
              RETURN_VALUE

257   L5:     LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('skipped')
              LOAD_CONST               4 ('attempted')
              LOAD_CONST               5 (False)

258           LOAD_CONST               6 ('reason')
              LOAD_CONST              13 ('verdict_not_eligible')

257           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "scripts/run_daily_ops_checklist_report.py", line 261>:
261           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('base_url')

263           LOAD_CONST               2 ('str')

261           LOAD_CONST               3 ('brokerage_ids')

264           LOAD_CONST               4 ('Optional[List[str]]')

261           LOAD_CONST               5 ('sections')

265           LOAD_CONST               6 ('Dict[str, Dict[str, Any]]')

261           LOAD_CONST               7 ('return')

266           LOAD_CONST               8 ('Dict[str, Any]')

261           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _compose_report at 0x0000018C179C3C30, file "scripts/run_daily_ops_checklist_report.py", line 261>:
261           RESUME                   0

267           LOAD_GLOBAL              1 (sum + NULL)
              LOAD_CONST               0 (<code object <genexpr> at 0x0000018C1802C9B0, file "scripts/run_daily_ops_checklist_report.py", line 267>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         2 (sections)
              LOAD_ATTR                3 (values + NULL|self)
              CALL                     0
              GET_ITER
              CALL                     0
              CALL                     1
              STORE_FAST               3 (ok_count)

268           LOAD_GLOBAL              1 (sum + NULL)
              LOAD_CONST               1 (<code object <genexpr> at 0x0000018C1802CD40, file "scripts/run_daily_ops_checklist_report.py", line 268>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         2 (sections)
              LOAD_ATTR                3 (values + NULL|self)
              CALL                     0
              GET_ITER
              CALL                     0
              CALL                     1
              STORE_FAST               4 (failed_count)

270           LOAD_CONST               2 ('phase')
              LOAD_CONST               3 ('PAS188')

271           LOAD_CONST               4 ('tool')
              LOAD_CONST               5 ('run_daily_ops_checklist_report')

272           LOAD_CONST               6 ('base_url')
              LOAD_FAST                0 (base_url)

273           LOAD_CONST               7 ('brokerage_ids')
              LOAD_FAST                1 (brokerage_ids)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0

274   L1:     LOAD_CONST               8 ('run_date')
              LOAD_GLOBAL              5 (_today_iso + NULL)
              CALL                     0

275           LOAD_CONST               9 ('generated_at')
              LOAD_GLOBAL              7 (_now_iso + NULL)
              CALL                     0

276           LOAD_CONST              10 ('verdict')
              LOAD_FAST_BORROW         4 (failed_count)
              LOAD_SMALL_INT           0
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST              11 ('OK')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST              12 ('DEGRADED')

277   L3:     LOAD_CONST              13 ('endpoint_count')
              LOAD_GLOBAL              9 (len + NULL)
              LOAD_FAST_BORROW         2 (sections)
              CALL                     1

278           LOAD_CONST              14 ('ok_count')
              LOAD_FAST_BORROW         3 (ok_count)

279           LOAD_CONST              15 ('failed_count')
              LOAD_FAST_BORROW         4 (failed_count)

280           LOAD_CONST              16 ('sections')
              LOAD_FAST_BORROW         2 (sections)

269           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C1802C9B0, file "scripts/run_daily_ops_checklist_report.py", line 267>:
 267           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                31 (to L5)
               STORE_FAST_LOAD_FAST    17 (s, s)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('ok')
               CALL                     1
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           27 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           33 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C1802CD40, file "scripts/run_daily_ops_checklist_report.py", line 268>:
 268           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                31 (to L5)
               STORE_FAST_LOAD_FAST    17 (s, s)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('ok')
               CALL                     1
               TO_BOOL
       L3:     POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           27 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           33 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts/run_daily_ops_checklist_report.py", line 288>:
288           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C182DB4B0, file "scripts/run_daily_ops_checklist_report.py", line 288>:
288           RESUME                   0

289           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

290           LOAD_CONST               0 ('run_daily_ops_checklist_report')

292           LOAD_CONST               1 ('PAS188 — Operator-run daily ops checklist report. Read-only HTTP. Never modifies anything. Not a cron job.')

289           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

296           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

297           LOAD_CONST               3 ('--base-url')

298           LOAD_GLOBAL              6 (os)
              LOAD_ATTR                8 (environ)
              LOAD_ATTR               11 (get + NULL|self)
              LOAD_CONST               4 ('PAS_BASE_URL')
              LOAD_CONST               5 ('http://localhost:8000')
              CALL                     2

299           LOAD_CONST               6 ('Base URL of the PAS deployment (default: $PAS_BASE_URL or localhost:8000).')

296           LOAD_CONST               7 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

301           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

302           LOAD_CONST               8 ('--admin-key-env')

303           LOAD_CONST               9 ('ADMIN_API_KEY')

304           LOAD_CONST              10 ("Environment variable name containing the operator's admin API key.")

301           LOAD_CONST               7 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

306           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

307           LOAD_CONST              11 ('--brokerage-ids')

308           LOAD_CONST              12 (None)

309           LOAD_CONST              13 ('Optional comma-separated list of brokerage_ids to scope the report (informational; the routes still return fleet-wide data).')

306           LOAD_CONST               7 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

311           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

312           LOAD_CONST              14 ('--output')

313           LOAD_CONST              12 (None)

314           LOAD_CONST              15 ('Output JSON path (default: daily_ops_report_YYYY-MM-DD.json).')

311           LOAD_CONST               7 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

316           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

317           LOAD_CONST              16 ('--timeout')

318           LOAD_GLOBAL             12 (float)

319           LOAD_GLOBAL             14 (_DEFAULT_TIMEOUT)

320           LOAD_CONST              17 ('Per-endpoint timeout in seconds (default ')
              LOAD_GLOBAL             14 (_DEFAULT_TIMEOUT)
              FORMAT_SIMPLE
              LOAD_CONST              18 (').')
              BUILD_STRING             3

316           LOAD_CONST              19 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

322           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              20 ('--summary-only')
              LOAD_CONST              21 ('store_true')

323           LOAD_CONST              22 ("Don't write report file; print summary only.")

322           LOAD_CONST              23 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

324           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              24 ('--json')
              LOAD_CONST              21 ('store_true')

325           LOAD_CONST              25 ('Print the full report JSON to stdout.')

324           LOAD_CONST              23 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

326           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              26 ('--dry-run')
              LOAD_CONST              21 ('store_true')

327           LOAD_CONST              27 ('Do not actually call endpoints; print the planned actions only.')

326           LOAD_CONST              23 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

332           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              28 ('--watch')
              LOAD_CONST              21 ('store_true')

333           LOAD_CONST              29 ('PAS189 — Loop --max-runs times with --interval-seconds between runs. Not a scheduler; not a daemon.')

332           LOAD_CONST              23 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

336           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              30 ('--interval-seconds')
              LOAD_GLOBAL             16 (int)
              LOAD_GLOBAL             18 (_WATCH_INTERVAL_DEFAULT)

337           LOAD_CONST              31 ('PAS189 — Seconds between iterations (min ')

338           LOAD_GLOBAL             20 (_WATCH_INTERVAL_MIN)
              FORMAT_SIMPLE
              LOAD_CONST              32 (', max ')

339           LOAD_GLOBAL             22 (_WATCH_INTERVAL_MAX)
              FORMAT_SIMPLE
              LOAD_CONST              33 (', default ')

340           LOAD_GLOBAL             18 (_WATCH_INTERVAL_DEFAULT)
              FORMAT_SIMPLE
              LOAD_CONST              18 (').')

337           BUILD_STRING             7

336           LOAD_CONST              19 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

341           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              34 ('--max-runs')
              LOAD_GLOBAL             16 (int)
              LOAD_GLOBAL             24 (_WATCH_MAX_RUNS_DEFAULT)

342           LOAD_CONST              35 ('PAS189 — Hard cap on the watch loop (min 1, max ')

343           LOAD_GLOBAL             26 (_WATCH_MAX_RUNS_HARD)
              FORMAT_SIMPLE
              LOAD_CONST              33 (', default ')

344           LOAD_GLOBAL             24 (_WATCH_MAX_RUNS_DEFAULT)
              FORMAT_SIMPLE
              LOAD_CONST              18 (').')

342           BUILD_STRING             5

341           LOAD_CONST              19 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

350           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              36 ('--slack-webhook-url')
              LOAD_CONST              37 ('')

351           LOAD_CONST              38 ('PAS190 — Optional Slack incoming-webhook URL. Posts a structural one-line summary on amber/red. The URL is NEVER printed. Failure to notify never fails the runner.')

350           LOAD_CONST               7 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

355           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              39 ('--notify-on-failure')
              LOAD_CONST              21 ('store_true')

356           LOAD_CONST              40 ('PAS190 — Post to the Slack webhook when any endpoint in the iteration returns non-2xx.')

355           LOAD_CONST              23 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

358           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              41 ('--notify-on-warning')
              LOAD_CONST              21 ('store_true')

359           LOAD_CONST              42 ('PAS190 — Post to the Slack webhook on partial failure (one or more endpoints DEGRADED but the overall verdict is not OK).')

358           LOAD_CONST              23 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

362           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts/run_daily_ops_checklist_report.py", line 365>:
365           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17EA5CC0, file "scripts/run_daily_ops_checklist_report.py", line 365>:
 365            RESUME                   0

 366            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 367            NOP

 368    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 372    L2:     LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (environ)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_FAST                2 (args)
                LOAD_ATTR               16 (admin_key_env)
                CALL                     1
                STORE_FAST               4 (admin_key)

 373            LOAD_FAST                4 (admin_key)
                TO_BOOL
                POP_JUMP_IF_TRUE        44 (to L3)
                NOT_TAKEN

 374            LOAD_GLOBAL             19 (print + NULL)

 375            LOAD_CONST               2 ('error: environment variable ')
                LOAD_FAST                2 (args)
                LOAD_ATTR               16 (admin_key_env)
                FORMAT_SIMPLE
                LOAD_CONST               3 (' is empty; set it to your admin API key and re-run.')
                BUILD_STRING             3

 377            LOAD_GLOBAL             20 (sys)
                LOAD_ATTR               22 (stderr)

 374            LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 379            LOAD_SMALL_INT           2
                RETURN_VALUE

 381    L3:     LOAD_CONST               1 (None)
                STORE_FAST               5 (brokerage_ids)

 382            LOAD_FAST                2 (args)
                LOAD_ATTR               24 (brokerage_ids)
                TO_BOOL
                POP_JUMP_IF_FALSE       80 (to L10)
                NOT_TAKEN

 384            LOAD_FAST                2 (args)
                LOAD_ATTR               24 (brokerage_ids)
                LOAD_ATTR               27 (split + NULL|self)
                LOAD_CONST               5 (',')
                CALL                     1
                GET_ITER

 383            LOAD_FAST_AND_CLEAR      6 (s)
                SWAP                     2
        L4:     BUILD_LIST               0
                SWAP                     2

 384    L5:     FOR_ITER                42 (to L8)
                STORE_FAST_LOAD_FAST   102 (s, s)
                LOAD_ATTR               29 (strip + NULL|self)
                CALL                     0
                TO_BOOL
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           26 (to L5)
        L7:     LOAD_FAST                6 (s)
                LOAD_ATTR               29 (strip + NULL|self)
                CALL                     0
                LIST_APPEND              2
                JUMP_BACKWARD           44 (to L5)
        L8:     END_FOR
                POP_ITER

 383    L9:     STORE_FAST               5 (brokerage_ids)
                STORE_FAST               6 (s)

 387   L10:     LOAD_FAST                2 (args)
                LOAD_ATTR               30 (base_url)
                LOAD_ATTR               29 (strip + NULL|self)
                CALL                     0
                STORE_FAST               7 (base_url)

 388            LOAD_FAST                7 (base_url)
                TO_BOOL
                POP_JUMP_IF_TRUE        30 (to L11)
                NOT_TAKEN

 389            LOAD_GLOBAL             19 (print + NULL)
                LOAD_CONST               6 ('error: --base-url required.')
                LOAD_GLOBAL             20 (sys)
                LOAD_ATTR               22 (stderr)
                LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 390            LOAD_SMALL_INT           2
                RETURN_VALUE

 392   L11:     LOAD_FAST                2 (args)
                LOAD_ATTR               32 (dry_run)
                TO_BOOL
                POP_JUMP_IF_FALSE       54 (to L14)
                NOT_TAKEN

 393            LOAD_GLOBAL             34 (_ENDPOINTS)
                GET_ITER
       L12:     FOR_ITER                41 (to L13)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  137 (name, path)

 394            LOAD_GLOBAL             19 (print + NULL)
                LOAD_CONST               7 ('[dry-run] would GET ')
                LOAD_FAST                7 (base_url)
                LOAD_ATTR               37 (rstrip + NULL|self)
                LOAD_CONST               8 ('/')
                CALL                     1
                LOAD_FAST                9 (path)
                BINARY_OP                0 (+)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           43 (to L12)

 393   L13:     END_FOR
                POP_ITER

 395            LOAD_SMALL_INT           0
                RETURN_VALUE

 398   L14:     LOAD_FAST                2 (args)
                LOAD_ATTR               38 (watch)
                TO_BOOL
                EXTENDED_ARG             2
                POP_JUMP_IF_FALSE      682 (to L47)
                NOT_TAKEN

 399            LOAD_GLOBAL             41 (max + NULL)
                LOAD_GLOBAL             42 (_WATCH_INTERVAL_MIN)

 400            LOAD_GLOBAL             45 (min + NULL)
                LOAD_GLOBAL             46 (_WATCH_INTERVAL_MAX)

 401            LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               48 (interval_seconds)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         7 (to L15)
                NOT_TAKEN
                POP_TOP
                LOAD_GLOBAL             50 (_WATCH_INTERVAL_DEFAULT)
       L15:     CALL                     1

 400            CALL                     2

 399            CALL                     2
                STORE_FAST              10 (interval)

 402            LOAD_GLOBAL             41 (max + NULL)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL             45 (min + NULL)
                LOAD_GLOBAL             52 (_WATCH_MAX_RUNS_HARD)

 403            LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               54 (max_runs)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         7 (to L16)
                NOT_TAKEN
                POP_TOP
                LOAD_GLOBAL             56 (_WATCH_MAX_RUNS_DEFAULT)
       L16:     CALL                     1

 402            CALL                     2
                CALL                     2
                STORE_FAST              11 (max_runs)

 404            LOAD_GLOBAL             19 (print + NULL)

 405            LOAD_CONST               9 ('[PAS189-watch] starting bounded watch loop: interval=')

 406            LOAD_FAST               10 (interval)
                FORMAT_SIMPLE
                LOAD_CONST              10 ('s max_runs=')
                LOAD_FAST               11 (max_runs)
                FORMAT_SIMPLE

 405            BUILD_STRING             4

 404            CALL                     1
                POP_TOP

 408            LOAD_CONST              11 (False)
                STORE_FAST              12 (final_failed)

 409            NOP

 410   L17:     LOAD_GLOBAL             59 (range + NULL)
                LOAD_FAST               11 (max_runs)
                CALL                     1
                GET_ITER
       L18:     EXTENDED_ARG             1
                FOR_ITER               493 (to L44)
                STORE_FAST              13 (run_idx)

 411            BUILD_MAP                0
                STORE_FAST              14 (sections_iter)

 412            LOAD_GLOBAL             34 (_ENDPOINTS)
                GET_ITER
       L19:     FOR_ITER                29 (to L20)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  137 (name, path)

 413            LOAD_GLOBAL             61 (_fetch + NULL)

 414            LOAD_FAST_LOAD_FAST    121 (base_url, path)
                LOAD_FAST_LOAD_FAST     66 (admin_key, args)
                LOAD_ATTR               62 (timeout)

 413            CALL                     4
                LOAD_FAST_LOAD_FAST    232 (sections_iter, name)
                STORE_SUBSCR
                JUMP_BACKWARD           31 (to L19)

 412   L20:     END_FOR
                POP_ITER

 416            LOAD_GLOBAL             65 (_compose_report + NULL)

 417            LOAD_FAST                7 (base_url)

 418            LOAD_FAST                5 (brokerage_ids)

 419            LOAD_FAST               14 (sections_iter)

 416            LOAD_CONST              12 (('base_url', 'brokerage_ids', 'sections'))
                CALL_KW                  3
                STORE_FAST              15 (report_iter)

 421            LOAD_FAST               13 (run_idx)
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST               15 (report_iter)
                LOAD_CONST              13 ('run_index')
                STORE_SUBSCR

 422            LOAD_FAST_LOAD_FAST    191 (max_runs, report_iter)
                LOAD_CONST              14 ('run_total')
                STORE_SUBSCR

 423            LOAD_GLOBAL             67 (_summarise + NULL)
                LOAD_FAST               15 (report_iter)
                CALL                     1
                GET_ITER
       L21:     FOR_ITER                14 (to L22)
                STORE_FAST              16 (line)

 424            LOAD_GLOBAL             19 (print + NULL)
                LOAD_FAST               16 (line)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           16 (to L21)

 423   L22:     END_FOR
                POP_ITER

 425            LOAD_FAST                2 (args)
                LOAD_ATTR               68 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE       117 (to L33)
       L23:     NOT_TAKEN

 427   L24:     LOAD_FAST                2 (args)
                LOAD_ATTR               70 (output)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L27)
       L25:     NOT_TAKEN
       L26:     POP_TOP

 428            LOAD_CONST              15 ('daily_ops_report_')
                LOAD_GLOBAL             73 (_today_iso + NULL)
                CALL                     0
                FORMAT_SIMPLE
                LOAD_CONST              16 ('_run_')
                LOAD_FAST               13 (run_idx)
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                FORMAT_SIMPLE
                LOAD_CONST              17 ('.json')
                BUILD_STRING             5

 426   L27:     STORE_FAST              17 (out_path)

 430   L28:     NOP

 431   L29:     LOAD_GLOBAL             75 (open + NULL)
                LOAD_FAST               17 (out_path)
                LOAD_CONST              18 ('w')
                LOAD_CONST              19 ('utf-8')
                LOAD_CONST              20 (('encoding',))
                CALL_KW                  3
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
       L30:     STORE_FAST              18 (fp)

 432            LOAD_GLOBAL             76 (json)
                LOAD_ATTR               78 (dump)
                PUSH_NULL
                LOAD_FAST               15 (report_iter)
                LOAD_FAST               18 (fp)
                LOAD_SMALL_INT           2
                LOAD_CONST              21 (True)
                LOAD_CONST              22 (('indent', 'sort_keys'))
                CALL_KW                  4
                POP_TOP

 431   L31:     LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     3
                POP_TOP

 433   L32:     LOAD_GLOBAL             19 (print + NULL)
                LOAD_CONST              23 ('[PAS189-watch] report written to ')
                LOAD_FAST               17 (out_path)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 440   L33:     LOAD_FAST                2 (args)
                LOAD_ATTR               76 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L36)
       L34:     NOT_TAKEN

 441   L35:     LOAD_GLOBAL             19 (print + NULL)
                LOAD_GLOBAL             76 (json)
                LOAD_ATTR               86 (dumps)
                PUSH_NULL
                LOAD_FAST               15 (report_iter)
                LOAD_SMALL_INT           2
                LOAD_CONST              21 (True)
                LOAD_CONST              22 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 443   L36:     LOAD_GLOBAL             89 (_maybe_notify + NULL)

 444            LOAD_FAST                2 (args)
                LOAD_ATTR               90 (slack_webhook_url)

 445            LOAD_FAST                2 (args)
                LOAD_ATTR               92 (notify_on_failure)

 446            LOAD_FAST                2 (args)
                LOAD_ATTR               94 (notify_on_warning)

 447            LOAD_FAST               15 (report_iter)

 443            LOAD_CONST              26 (('webhook_url', 'notify_on_failure', 'notify_on_warning', 'report'))
                CALL_KW                  4
                STORE_FAST              19 (notify_res)

 449            LOAD_FAST               19 (notify_res)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              27 ('attempted')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       49 (to L37)
                NOT_TAKEN

 452            LOAD_GLOBAL             19 (print + NULL)

 453            LOAD_CONST              28 ('[PAS190-notify] slack_notify status=')

 454            LOAD_FAST               19 (notify_res)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              29 ('status')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              30 (' http=')

 455            LOAD_FAST               19 (notify_res)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              31 ('http_status')
                LOAD_SMALL_INT           0
                CALL                     2
                FORMAT_SIMPLE

 453            BUILD_STRING             4

 452            CALL                     1
                POP_TOP

 457   L37:     LOAD_FAST               15 (report_iter)
                LOAD_CONST              32 ('failed_count')
                BINARY_OP               26 ([])
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L38)
                NOT_TAKEN

 458            LOAD_CONST              21 (True)
                STORE_FAST              12 (final_failed)

 459   L38:     LOAD_FAST               13 (run_idx)
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST               11 (max_runs)
                COMPARE_OP              18 (bool(<))
       L39:     POP_JUMP_IF_TRUE         4 (to L40)
                NOT_TAKEN
                EXTENDED_ARG             1
                JUMP_BACKWARD          439 (to L18)

 462   L40:     LOAD_FAST               10 (interval)
                STORE_FAST              20 (remaining)

 463   L41:     LOAD_FAST               20 (remaining)
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
       L42:     POP_JUMP_IF_TRUE         4 (to L43)
                NOT_TAKEN
                EXTENDED_ARG             1
                JUMP_BACKWARD          451 (to L18)

 464   L43:     LOAD_GLOBAL             45 (min + NULL)
                LOAD_SMALL_INT           2
                LOAD_FAST               20 (remaining)
                CALL                     2
                STORE_FAST              21 (slice_s)

 465            LOAD_GLOBAL             96 (time)
                LOAD_ATTR               98 (sleep)
                PUSH_NULL
                LOAD_FAST               21 (slice_s)
                CALL                     1
                POP_TOP

 466            LOAD_FAST               20 (remaining)
                LOAD_FAST               21 (slice_s)
                BINARY_OP               23 (-=)
                STORE_FAST              20 (remaining)
                JUMP_BACKWARD           55 (to L41)

 410   L44:     END_FOR
                POP_ITER

 470   L45:     LOAD_GLOBAL             19 (print + NULL)

 471            LOAD_CONST              34 ('[PAS189-watch] watch loop complete: runs=')

 472            LOAD_FAST               11 (max_runs)
                FORMAT_SIMPLE
                LOAD_CONST              35 (' interval=')
                LOAD_FAST               10 (interval)
                FORMAT_SIMPLE
                LOAD_CONST              36 ('s')

 471            BUILD_STRING             5

 470            CALL                     1
                POP_TOP

 474            LOAD_FAST               12 (final_failed)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L46)
                NOT_TAKEN
                LOAD_SMALL_INT           1
                RETURN_VALUE
       L46:     LOAD_SMALL_INT           0
                RETURN_VALUE

 477   L47:     BUILD_MAP                0
                STORE_FAST              22 (sections)

 478            LOAD_GLOBAL             34 (_ENDPOINTS)
                GET_ITER
       L48:     FOR_ITER                30 (to L49)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  137 (name, path)

 479            LOAD_GLOBAL             61 (_fetch + NULL)
                LOAD_FAST_LOAD_FAST    121 (base_url, path)
                LOAD_FAST_LOAD_FAST     66 (admin_key, args)
                LOAD_ATTR               62 (timeout)
                CALL                     4
                LOAD_FAST               22 (sections)
                LOAD_FAST                8 (name)
                STORE_SUBSCR
                JUMP_BACKWARD           32 (to L48)

 478   L49:     END_FOR
                POP_ITER

 481            LOAD_GLOBAL             65 (_compose_report + NULL)

 482            LOAD_FAST                7 (base_url)

 483            LOAD_FAST                5 (brokerage_ids)

 484            LOAD_FAST               22 (sections)

 481            LOAD_CONST              12 (('base_url', 'brokerage_ids', 'sections'))
                CALL_KW                  3
                STORE_FAST              23 (report)

 487            LOAD_GLOBAL             67 (_summarise + NULL)
                LOAD_FAST               23 (report)
                CALL                     1
                GET_ITER
       L50:     FOR_ITER                14 (to L51)
                STORE_FAST              16 (line)

 488            LOAD_GLOBAL             19 (print + NULL)
                LOAD_FAST               16 (line)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           16 (to L50)

 487   L51:     END_FOR
                POP_ITER

 490            LOAD_FAST                2 (args)
                LOAD_ATTR               68 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE       107 (to L57)
                NOT_TAKEN

 491            LOAD_FAST                2 (args)
                LOAD_ATTR               70 (output)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L52)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              15 ('daily_ops_report_')
                LOAD_GLOBAL             73 (_today_iso + NULL)
                CALL                     0
                FORMAT_SIMPLE
                LOAD_CONST              17 ('.json')
                BUILD_STRING             3
       L52:     STORE_FAST              17 (out_path)

 492            NOP

 493   L53:     LOAD_GLOBAL             75 (open + NULL)
                LOAD_FAST               17 (out_path)
                LOAD_CONST              18 ('w')
                LOAD_CONST              19 ('utf-8')
                LOAD_CONST              20 (('encoding',))
                CALL_KW                  3
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
       L54:     STORE_FAST              18 (fp)

 494            LOAD_GLOBAL             76 (json)
                LOAD_ATTR               78 (dump)
                PUSH_NULL
                LOAD_FAST               23 (report)
                LOAD_FAST               18 (fp)
                LOAD_SMALL_INT           2
                LOAD_CONST              21 (True)
                LOAD_CONST              22 (('indent', 'sort_keys'))
                CALL_KW                  4
                POP_TOP

 493   L55:     LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     3
                POP_TOP

 495   L56:     LOAD_GLOBAL             19 (print + NULL)
                LOAD_CONST              37 ('[PAS188-runner] report written to ')
                LOAD_FAST               17 (out_path)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 503   L57:     LOAD_FAST                2 (args)
                LOAD_ATTR               76 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L58)
                NOT_TAKEN

 504            LOAD_GLOBAL             19 (print + NULL)
                LOAD_GLOBAL             76 (json)
                LOAD_ATTR               86 (dumps)
                PUSH_NULL
                LOAD_FAST               23 (report)
                LOAD_SMALL_INT           2
                LOAD_CONST              21 (True)
                LOAD_CONST              22 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 507   L58:     LOAD_GLOBAL             89 (_maybe_notify + NULL)

 508            LOAD_FAST                2 (args)
                LOAD_ATTR               90 (slack_webhook_url)

 509            LOAD_FAST                2 (args)
                LOAD_ATTR               92 (notify_on_failure)

 510            LOAD_FAST                2 (args)
                LOAD_ATTR               94 (notify_on_warning)

 511            LOAD_FAST               23 (report)

 507            LOAD_CONST              26 (('webhook_url', 'notify_on_failure', 'notify_on_warning', 'report'))
                CALL_KW                  4
                STORE_FAST              19 (notify_res)

 513            LOAD_FAST               19 (notify_res)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              27 ('attempted')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       49 (to L59)
                NOT_TAKEN

 515            LOAD_GLOBAL             19 (print + NULL)

 516            LOAD_CONST              28 ('[PAS190-notify] slack_notify status=')

 517            LOAD_FAST               19 (notify_res)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              29 ('status')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              30 (' http=')

 518            LOAD_FAST               19 (notify_res)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              31 ('http_status')
                LOAD_SMALL_INT           0
                CALL                     2
                FORMAT_SIMPLE

 516            BUILD_STRING             4

 515            CALL                     1
                POP_TOP

 521   L59:     LOAD_FAST               23 (report)
                LOAD_CONST              32 ('failed_count')
                BINARY_OP               26 ([])
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L60)
                NOT_TAKEN
                LOAD_SMALL_INT           0
                RETURN_VALUE
       L60:     LOAD_SMALL_INT           1
                RETURN_VALUE

  --   L61:     PUSH_EXC_INFO

 369            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L70)
                NOT_TAKEN
                STORE_FAST               3 (e)

 370   L62:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST              38 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L63)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L67)
       L63:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L66)
       L64:     NOT_TAKEN
       L65:     POP_TOP
                LOAD_SMALL_INT           0
       L66:     CALL                     1
       L67:     SWAP                     2
       L68:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L69:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 369   L70:     RERAISE                  0

  --   L71:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L72:     SWAP                     2
                POP_TOP

 383            SWAP                     2
                STORE_FAST               6 (s)
                RERAISE                  0

 431   L73:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L74)
                NOT_TAKEN
                RERAISE                  2
       L74:     POP_TOP
       L75:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                EXTENDED_ARG             3
                JUMP_BACKWARD_NO_INTERRUPT 795 (to L32)

  --   L76:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L77:     PUSH_EXC_INFO

 434            LOAD_GLOBAL             80 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       64 (to L81)
                NOT_TAKEN
                STORE_FAST               3 (e)

 435   L78:     LOAD_GLOBAL             19 (print + NULL)

 436            LOAD_CONST              24 ('  [warn] failed to write report at ')
                LOAD_FAST               17 (out_path)
                FORMAT_SIMPLE
                LOAD_CONST              25 (': ')

 437            LOAD_GLOBAL             83 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               84 (__name__)
                FORMAT_SIMPLE

 436            BUILD_STRING             4

 438            LOAD_GLOBAL             20 (sys)
                LOAD_ATTR               22 (stderr)

 435            LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP
       L79:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                EXTENDED_ARG             3
                JUMP_BACKWARD_NO_INTERRUPT 853 (to L33)

  --   L80:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 434   L81:     RERAISE                  0

  --   L82:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L83:     PUSH_EXC_INFO

 467            LOAD_GLOBAL            100 (KeyboardInterrupt)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       29 (to L87)
                NOT_TAKEN
                POP_TOP

 468            LOAD_GLOBAL             19 (print + NULL)
                LOAD_CONST              33 ('[PAS189-watch] interrupted by user — exiting.')
                CALL                     1
                POP_TOP

 469            LOAD_FAST               12 (final_failed)
                TO_BOOL
                POP_JUMP_IF_FALSE        5 (to L85)
                NOT_TAKEN
                LOAD_SMALL_INT           1
                SWAP                     2
       L84:     POP_EXCEPT
                RETURN_VALUE
       L85:     LOAD_SMALL_INT           0
                SWAP                     2
       L86:     POP_EXCEPT
                RETURN_VALUE

 467   L87:     RERAISE                  0

  --   L88:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 493   L89:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L90)
                NOT_TAKEN
                RERAISE                  2
       L90:     POP_TOP
       L91:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 435 (to L56)

  --   L92:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L93:     PUSH_EXC_INFO

 496            LOAD_GLOBAL             80 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       64 (to L97)
                NOT_TAKEN
                STORE_FAST               3 (e)

 497   L94:     LOAD_GLOBAL             19 (print + NULL)

 498            LOAD_CONST              24 ('  [warn] failed to write report at ')
                LOAD_FAST               17 (out_path)
                FORMAT_SIMPLE
                LOAD_CONST              25 (': ')

 499            LOAD_GLOBAL             83 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               84 (__name__)
                FORMAT_SIMPLE

 498            BUILD_STRING             4

 500            LOAD_GLOBAL             20 (sys)
                LOAD_ATTR               22 (stderr)

 497            LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP
       L95:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 493 (to L57)

  --   L96:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 496   L97:     RERAISE                  0

  --   L98:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L61 [0]
  L4 to L6 -> L72 [2]
  L7 to L9 -> L72 [2]
  L17 to L23 -> L83 [0]
  L24 to L25 -> L83 [0]
  L26 to L28 -> L83 [0]
  L29 to L30 -> L77 [1]
  L30 to L31 -> L73 [3] lasti
  L31 to L33 -> L77 [1]
  L33 to L34 -> L83 [0]
  L35 to L39 -> L83 [0]
  L40 to L42 -> L83 [0]
  L43 to L45 -> L83 [0]
  L53 to L54 -> L93 [0]
  L54 to L55 -> L89 [2] lasti
  L55 to L57 -> L93 [0]
  L61 to L62 -> L71 [1] lasti
  L62 to L64 -> L69 [1] lasti
  L65 to L67 -> L69 [1] lasti
  L67 to L68 -> L71 [1] lasti
  L69 to L71 -> L71 [1] lasti
  L73 to L75 -> L76 [5] lasti
  L75 to L77 -> L77 [1]
  L77 to L78 -> L82 [2] lasti
  L78 to L79 -> L80 [2] lasti
  L79 to L80 -> L83 [0]
  L80 to L82 -> L82 [2] lasti
  L82 to L83 -> L83 [0]
  L83 to L84 -> L88 [1] lasti
  L85 to L86 -> L88 [1] lasti
  L87 to L88 -> L88 [1] lasti
  L89 to L91 -> L92 [4] lasti
  L91 to L93 -> L93 [0]
  L93 to L94 -> L98 [1] lasti
  L94 to L95 -> L96 [1] lasti
  L96 to L98 -> L98 [1] lasti
```
