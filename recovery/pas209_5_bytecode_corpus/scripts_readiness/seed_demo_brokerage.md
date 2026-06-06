# scripts_readiness/seed_demo_brokerage

- **pyc:** `scripts\__pycache__\seed_demo_brokerage.cpython-314.pyc`
- **expected source path (absent):** `scripts/seed_demo_brokerage.py`
- **co_filename (from bytecode):** `scripts\seed_demo_brokerage.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS138A — Seed: demo brokerage (Python, idempotent).

Why this exists:
    The PAS code path falls back to an in-memory _DEFAULT_BROKERAGE when
    `get_brokerage_by_id("demo")` returns no row, so /simulate-call and the
    web demo widget RUN — but `calls.brokerage_id` has a FK on
    `brokerages(id)`, so Supabase silently rejects every persisted row.
    Seeding a real `brokerages` row makes the default demo path durable
    end-to-end: calls persist, lead memory works, the dashboard sees runs.

This is the Python counterpart to scripts/seed_demo_brokerage.sql. The SQL
version stays as a manual fallback for the Supabase SQL Editor; this script
is the one to run from a CI/dev shell with a configured .env.

Behaviour:
  - Creates `brokerages.id = "demo"` if missing.
  - Updates the small set of identity fields (name, owner_email, active)
    on every run so a partially-seeded row gets brought to spec.
  - Never deletes anything. Never touches other brokerages. Never
    overwrites secrets/api_key/twilio_phone/notification_config.
  - Prints exactly one of: created | updated | skipped | error.

Run from project root with .env loaded:
    python scripts/seed_demo_brokerage.py

Exit codes:
    0  created | updated | skipped     (success)
    2  Supabase client init failed
    3  Supabase write failed
```

## Imports

`app.db.supabase_client`, `get_supabase`, `init_supabase`, `os`, `sys`

## Classes

_none_

## Functions / methods

`__annotate__`, `_fetch_existing`, `_insert_demo`, `_needs_update`, `_print`, `_safe_env_summary`, `_update_demo`, `main`

## Env-key candidates

`ENVIRONMENT`, `SUPABASE_SERVICE_KEY`, `SUPABASE_URL`

## String constants (redacted where noted)

- '\nPAS138A — Seed: demo brokerage (Python, idempotent).\n\nWhy this exists:\n    The PAS code path falls back to an in-memory _DEFAULT_BROKERAGE when\n    `get_brokerage_by_id("demo")` returns no row, so /simulate-call and the\n    web demo widget RUN — but `calls.brokerage_id` has a FK on\n    `brokerages(id)`, so Supabase silently rejects every persisted row.\n    Seeding a real `brokerages` row makes the default demo path durable\n    end-to-end: calls persist, lead memory works, the dashboard sees runs.\n\nThis is the Python counterpart to scripts/seed_demo_brokerage.sql. The SQL\nversion stays as a manual fallback for the Supabase SQL Editor; this script\nis the one to run from a CI/dev shell with a configured .env.\n\nBehaviour:\n  - Creates `brokerages.id = "demo"` if missing.\n  - Updates the small set of identity fields (name, owner_email, active)\n    on every run so a partially-seeded row gets brought to spec.\n  - Never deletes anything. Never touches other brokerages. Never\n    overwrites secrets/api_key/twilio_phone/notification_config.\n  - Prints exactly one of: created | updated | skipped | error.\n\nRun from project root with .env loaded:\n    python scripts/seed_demo_brokerage.py\n\nExit codes:\n    0  created | updated | skipped     (success)\n    2  Supabase client init failed\n    3  Supabase write failed\n'
- 'demo'
- 'ORVN Demo Realty'
- 'Alex'
- 'demo@orvnlabs.com'
- 'msg'
- 'return'
- "One-line summary of which env we're targeting — never echoes secrets."
- 'SUPABASE_URL'
- 'ENVIRONMENT'
- 'development'
- 'SUPABASE_SERVICE_KEY'
- '(unset)'
- 'env='
- ' supabase_host='
- ' service_key_set='
- 'brokerages'
- 'id, name, owner_email, active'
- 'existing'
- 'name'
- 'owner_email'
- 'active'
- 'agent_name'
- '== PAS138A demo brokerage seed =='
- 'target: brokerages.id = '
- 'error: Supabase client init failed: '
- 'error: lookup of brokerages.id='
- ' failed: '
- 'error: insert of brokerages.id='
- 'created: brokerages.id='
- ' name='
- ' owner_email='
- ' active=true'
- 'skipped: brokerages.id='
- ' already matches target (name='
- ', owner_email='
- ', active='
- 'error: update of brokerages.id='
- ' -> '
- 'updated: brokerages.id={!r} | {}'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS138A — Seed: demo brokerage (Python, idempotent).\n\nWhy this exists:\n    The PAS code path falls back to an in-memory _DEFAULT_BROKERAGE when\n    `get_brokerage_by_id("demo")` returns no row, so /simulate-call and the\n    web demo widget RUN — but `calls.brokerage_id` has a FK on\n    `brokerages(id)`, so Supabase silently rejects every persisted row.\n    Seeding a real `brokerages` row makes the default demo path durable\n    end-to-end: calls persist, lead memory works, the dashboard sees runs.\n\nThis is the Python counterpart to scripts/seed_demo_brokerage.sql. The SQL\nversion stays as a manual fallback for the Supabase SQL Editor; this script\nis the one to run from a CI/dev shell with a configured .env.\n\nBehaviour:\n  - Creates `brokerages.id = "demo"` if missing.\n  - Updates the small set of identity fields (name, owner_email, active)\n    on every run so a partially-seeded row gets brought to spec.\n  - Never deletes anything. Never touches other brokerages. Never\n    overwrites secrets/api_key/twilio_phone/notification_config.\n  - Prints exactly one of: created | updated | skipped | error.\n\nRun from project root with .env loaded:\n    python scripts/seed_demo_brokerage.py\n\nExit codes:\n    0  created | updated | skipped     (success)\n    2  Supabase client init failed\n    3  Supabase write failed\n')
              STORE_NAME               0 (__doc__)

 33           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              1 (os)
              STORE_NAME               1 (os)

 34           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              2 (sys)
              STORE_NAME               2 (sys)

 36           LOAD_NAME                2 (sys)
              LOAD_ATTR                6 (path)
              LOAD_ATTR                9 (insert + NULL|self)
              LOAD_SMALL_INT           0
              LOAD_NAME                1 (os)
              LOAD_ATTR                6 (path)
              LOAD_ATTR               11 (abspath + NULL|self)
              LOAD_NAME                1 (os)
              LOAD_ATTR                6 (path)
              LOAD_ATTR               13 (dirname + NULL|self)
              LOAD_NAME                1 (os)
              LOAD_ATTR                6 (path)
              LOAD_ATTR               13 (dirname + NULL|self)
              LOAD_NAME                7 (__file__)
              CALL                     1
              CALL                     1
              CALL                     1
              CALL                     2
              POP_TOP

 38           LOAD_SMALL_INT           0
              LOAD_CONST               2 (('init_supabase', 'get_supabase'))
              IMPORT_NAME              8 (app.db.supabase_client)
              IMPORT_FROM              9 (init_supabase)
              STORE_NAME               9 (init_supabase)
              IMPORT_FROM             10 (get_supabase)
              STORE_NAME              10 (get_supabase)
              POP_TOP

 40           LOAD_CONST               3 ('demo')
              STORE_NAME              11 (DEMO_ID)

 41           LOAD_CONST               4 ('ORVN Demo Realty')
              STORE_NAME              12 (DEMO_NAME)

 42           LOAD_CONST               5 ('Alex')
              STORE_NAME              13 (DEMO_AGENT_NAME)

 43           LOAD_CONST               6 ('demo@orvnlabs.com')
              STORE_NAME              14 (DEMO_OWNER_EMAIL)

 49           LOAD_CONST              22 (('name', 'owner_email', 'active'))
              STORE_NAME              15 (_IDENTITY_FIELDS)

 52           LOAD_CONST               7 (<code object __annotate__ at 0x0000018C18025C30, file "scripts\seed_demo_brokerage.py", line 52>)
              MAKE_FUNCTION
              LOAD_CONST               8 (<code object _print at 0x0000018C17FA32D0, file "scripts\seed_demo_brokerage.py", line 52>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              16 (_print)

 56           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C18025130, file "scripts\seed_demo_brokerage.py", line 56>)
              MAKE_FUNCTION
              LOAD_CONST              10 (<code object _safe_env_summary at 0x0000018C17D77E00, file "scripts\seed_demo_brokerage.py", line 56>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              17 (_safe_env_summary)

 65           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C18024F30, file "scripts\seed_demo_brokerage.py", line 65>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object _fetch_existing at 0x0000018C1794E810, file "scripts\seed_demo_brokerage.py", line 65>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              18 (_fetch_existing)

 77           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18026030, file "scripts\seed_demo_brokerage.py", line 77>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object _needs_update at 0x0000018C1804D550, file "scripts\seed_demo_brokerage.py", line 77>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              19 (_needs_update)

 86           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts\seed_demo_brokerage.py", line 86>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _insert_demo at 0x0000018C17F96590, file "scripts\seed_demo_brokerage.py", line 86>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              20 (_insert_demo)

 97           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts\seed_demo_brokerage.py", line 97>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _update_demo at 0x0000018C17FF13B0, file "scripts\seed_demo_brokerage.py", line 97>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (_update_demo)

106           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18025030, file "scripts\seed_demo_brokerage.py", line 106>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object main at 0x0000018C17F792D0, file "scripts\seed_demo_brokerage.py", line 106>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (main)

163           LOAD_NAME               23 (__name__)
              LOAD_CONST              21 ('__main__')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       26 (to L1)
              NOT_TAKEN

164           LOAD_NAME                2 (sys)
              LOAD_ATTR               48 (exit)
              PUSH_NULL
              LOAD_NAME               22 (main)
              PUSH_NULL
              CALL                     0
              CALL                     1
              POP_TOP
              LOAD_CONST               1 (None)
              RETURN_VALUE

163   L1:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "scripts\seed_demo_brokerage.py", line 52>:
 52           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('msg')
              LOAD_GLOBAL              0 (str)
              LOAD_CONST               2 ('return')
              LOAD_CONST               3 (None)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _print at 0x0000018C17FA32D0, file "scripts\seed_demo_brokerage.py", line 52>:
 52           RESUME                   0

 53           LOAD_GLOBAL              1 (print + NULL)
              LOAD_FAST_BORROW         0 (msg)
              LOAD_CONST               0 (True)
              LOAD_CONST               1 (('flush',))
              CALL_KW                  2
              POP_TOP
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "scripts\seed_demo_brokerage.py", line 56>:
 56           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_GLOBAL              0 (str)
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _safe_env_summary at 0x0000018C17D77E00, file "scripts\seed_demo_brokerage.py", line 56>:
 56           RESUME                   0

 58           LOAD_GLOBAL              0 (os)
              LOAD_ATTR                2 (environ)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('SUPABASE_URL')
              LOAD_CONST               2 ('')
              CALL                     2
              STORE_FAST               0 (url)

 59           LOAD_GLOBAL              0 (os)
              LOAD_ATTR                2 (environ)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               3 ('ENVIRONMENT')
              LOAD_CONST               4 ('development')
              CALL                     2
              STORE_FAST               1 (env)

 60           LOAD_GLOBAL              7 (bool + NULL)
              LOAD_GLOBAL              0 (os)
              LOAD_ATTR                2 (environ)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               5 ('SUPABASE_SERVICE_KEY')
              LOAD_CONST               2 ('')
              CALL                     2
              CALL                     1
              STORE_FAST               2 (have_key)

 61           LOAD_FAST_BORROW         0 (url)
              TO_BOOL
              POP_JUMP_IF_FALSE       49 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (url)
              LOAD_ATTR                9 (split + NULL|self)
              LOAD_CONST               6 ('//')
              LOAD_SMALL_INT           1
              CALL                     2
              LOAD_CONST              12 (-1)
              BINARY_OP               26 ([])
              LOAD_ATTR                9 (split + NULL|self)
              LOAD_CONST               7 ('/')
              LOAD_SMALL_INT           1
              CALL                     2
              LOAD_SMALL_INT           0
              BINARY_OP               26 ([])
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               8 ('(unset)')
      L2:     STORE_FAST               3 (host)

 62           LOAD_CONST               9 ('env=')
              LOAD_FAST_BORROW         1 (env)
              FORMAT_SIMPLE
              LOAD_CONST              10 (' supabase_host=')
              LOAD_FAST_BORROW         3 (host)
              FORMAT_SIMPLE
              LOAD_CONST              11 (' service_key_set=')
              LOAD_FAST_BORROW         2 (have_key)
              FORMAT_SIMPLE
              BUILD_STRING             6
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024F30, file "scripts\seed_demo_brokerage.py", line 65>:
 65           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_GLOBAL              0 (dict)
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _fetch_existing at 0x0000018C1794E810, file "scripts\seed_demo_brokerage.py", line 65>:
 65           RESUME                   0

 67           LOAD_FAST_BORROW         0 (db)
              LOAD_ATTR                1 (table + NULL|self)
              LOAD_CONST               0 ('brokerages')
              CALL                     1

 68           LOAD_ATTR                3 (select + NULL|self)
              LOAD_CONST               1 ('id, name, owner_email, active')
              CALL                     1

 69           LOAD_ATTR                5 (eq + NULL|self)
              LOAD_CONST               2 ('id')
              LOAD_GLOBAL              6 (DEMO_ID)
              CALL                     2

 70           LOAD_ATTR                9 (limit + NULL|self)
              LOAD_SMALL_INT           1
              CALL                     1

 71           LOAD_ATTR               11 (execute + NULL|self)
              CALL                     0

 66           STORE_FAST               1 (res)

 73           LOAD_FAST_BORROW         1 (res)
              LOAD_ATTR               12 (data)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     STORE_FAST               2 (rows)

 74           LOAD_FAST_BORROW         2 (rows)
              TO_BOOL
              POP_JUMP_IF_FALSE       10 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (rows)
              LOAD_SMALL_INT           0
              BINARY_OP               26 ([])
              RETURN_VALUE
      L2:     BUILD_MAP                0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026030, file "scripts\seed_demo_brokerage.py", line 77>:
 77           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('existing')
              LOAD_GLOBAL              0 (dict)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              2 (bool)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _needs_update at 0x0000018C1804D550, file "scripts\seed_demo_brokerage.py", line 77>:
  --           MAKE_CELL                0 (existing)

  77           RESUME                   0

  79           LOAD_CONST               0 ('name')
               LOAD_GLOBAL              0 (DEMO_NAME)

  80           LOAD_CONST               1 ('owner_email')
               LOAD_GLOBAL              2 (DEMO_OWNER_EMAIL)

  81           LOAD_CONST               2 ('active')
               LOAD_CONST               3 (True)

  78           BUILD_MAP                3
               STORE_FAST               1 (target)

  83           LOAD_GLOBAL              4 (any)
               COPY                     1
               LOAD_COMMON_CONSTANT     4 (<built-in function any>)
               IS_OP                    0 (is)
               POP_JUMP_IF_FALSE       45 (to L4)
               NOT_TAKEN
               POP_TOP
               LOAD_FAST_BORROW         0 (existing)
               BUILD_TUPLE              1
               LOAD_CONST               4 (<code object <genexpr> at 0x0000018C18038670, file "scripts\seed_demo_brokerage.py", line 83>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               LOAD_FAST_BORROW         1 (target)
               LOAD_ATTR                7 (items + NULL|self)
               CALL                     0
               GET_ITER
               CALL                     0
       L1:     FOR_ITER                12 (to L3)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L1)
       L2:     POP_ITER
               LOAD_CONST               3 (True)
               RETURN_VALUE
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               5 (False)
               RETURN_VALUE
       L4:     PUSH_NULL
               LOAD_FAST_BORROW         0 (existing)
               BUILD_TUPLE              1
               LOAD_CONST               4 (<code object <genexpr> at 0x0000018C18038670, file "scripts\seed_demo_brokerage.py", line 83>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               LOAD_FAST_BORROW         1 (target)
               LOAD_ATTR                7 (items + NULL|self)
               CALL                     0
               GET_ITER
               CALL                     0
               CALL                     1
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18038670, file "scripts\seed_demo_brokerage.py", line 83>:
  --           COPY_FREE_VARS           1

  83           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                37 (to L6)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   18 (k, v)
               LOAD_DEREF               3 (existing)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_FAST_BORROW         1 (k)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
       L3:     NOT_TAKEN
       L4:     POP_TOP
               LOAD_CONST               0 (None)
       L5:     LOAD_FAST_BORROW         2 (v)
               COMPARE_OP             103 (!=)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           39 (to L2)
       L6:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L7:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L7 [0] lasti
  L4 to L7 -> L7 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts\seed_demo_brokerage.py", line 86>:
 86           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 (None)
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _insert_demo at 0x0000018C17F96590, file "scripts\seed_demo_brokerage.py", line 86>:
 86           RESUME                   0

 88           LOAD_CONST               0 ('id')
              LOAD_GLOBAL              0 (DEMO_ID)

 89           LOAD_CONST               1 ('name')
              LOAD_GLOBAL              2 (DEMO_NAME)

 90           LOAD_CONST               2 ('agent_name')
              LOAD_GLOBAL              4 (DEMO_AGENT_NAME)

 91           LOAD_CONST               3 ('owner_email')
              LOAD_GLOBAL              6 (DEMO_OWNER_EMAIL)

 92           LOAD_CONST               4 ('active')
              LOAD_CONST               5 (True)

 87           BUILD_MAP                5
              STORE_FAST               1 (payload)

 94           LOAD_FAST_BORROW         0 (db)
              LOAD_ATTR                9 (table + NULL|self)
              LOAD_CONST               6 ('brokerages')
              CALL                     1
              LOAD_ATTR               11 (insert + NULL|self)
              LOAD_FAST_BORROW         1 (payload)
              CALL                     1
              LOAD_ATTR               13 (execute + NULL|self)
              CALL                     0
              POP_TOP
              LOAD_CONST               7 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts\seed_demo_brokerage.py", line 97>:
 97           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 (None)
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _update_demo at 0x0000018C17FF13B0, file "scripts\seed_demo_brokerage.py", line 97>:
 97           RESUME                   0

 99           LOAD_CONST               0 ('name')
              LOAD_GLOBAL              0 (DEMO_NAME)

100           LOAD_CONST               1 ('owner_email')
              LOAD_GLOBAL              2 (DEMO_OWNER_EMAIL)

101           LOAD_CONST               2 ('active')
              LOAD_CONST               3 (True)

 98           BUILD_MAP                3
              STORE_FAST               1 (payload)

103           LOAD_FAST_BORROW         0 (db)
              LOAD_ATTR                5 (table + NULL|self)
              LOAD_CONST               4 ('brokerages')
              CALL                     1
              LOAD_ATTR                7 (update + NULL|self)
              LOAD_FAST_BORROW         1 (payload)
              CALL                     1
              LOAD_ATTR                9 (eq + NULL|self)
              LOAD_CONST               5 ('id')
              LOAD_GLOBAL             10 (DEMO_ID)
              CALL                     2
              LOAD_ATTR               13 (execute + NULL|self)
              CALL                     0
              POP_TOP
              LOAD_CONST               6 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "scripts\seed_demo_brokerage.py", line 106>:
106           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_GLOBAL              0 (int)
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object main at 0x0000018C17F792D0, file "scripts\seed_demo_brokerage.py", line 106>:
 106            RESUME                   0

 107            LOAD_GLOBAL              1 (_print + NULL)
                LOAD_CONST               0 ('== PAS138A demo brokerage seed ==')
                CALL                     1
                POP_TOP

 108            LOAD_GLOBAL              1 (_print + NULL)
                LOAD_GLOBAL              3 (_safe_env_summary + NULL)
                CALL                     0
                CALL                     1
                POP_TOP

 109            LOAD_GLOBAL              1 (_print + NULL)
                LOAD_CONST               1 ('target: brokerages.id = ')
                LOAD_GLOBAL              4 (DEMO_ID)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 110            LOAD_GLOBAL              1 (_print + NULL)
                LOAD_CONST               2 ('')
                CALL                     1
                POP_TOP

 112            NOP

 113    L1:     LOAD_GLOBAL              7 (init_supabase + NULL)
                CALL                     0
                POP_TOP

 118    L2:     LOAD_GLOBAL             15 (get_supabase + NULL)
                CALL                     0
                STORE_FAST               1 (db)

 120            NOP

 121    L3:     LOAD_GLOBAL             17 (_fetch_existing + NULL)
                LOAD_FAST                1 (db)
                CALL                     1
                STORE_FAST               2 (existing)

 127    L4:     LOAD_FAST                2 (existing)
                TO_BOOL
                POP_JUMP_IF_TRUE        51 (to L7)
                NOT_TAKEN

 128            NOP

 129    L5:     LOAD_GLOBAL             19 (_insert_demo + NULL)
                LOAD_FAST                1 (db)
                CALL                     1
                POP_TOP

 134    L6:     LOAD_GLOBAL              1 (_print + NULL)
                LOAD_CONST               9 ('created: brokerages.id=')
                LOAD_GLOBAL              4 (DEMO_ID)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              10 (' name=')

 135            LOAD_GLOBAL             20 (DEMO_NAME)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              11 (' owner_email=')
                LOAD_GLOBAL             22 (DEMO_OWNER_EMAIL)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              12 (' active=true')

 134            BUILD_STRING             7
                CALL                     1
                POP_TOP

 136            LOAD_SMALL_INT           0
                RETURN_VALUE

 138    L7:     LOAD_GLOBAL             25 (_needs_update + NULL)
                LOAD_FAST                2 (existing)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        79 (to L8)
                NOT_TAKEN

 139            LOAD_GLOBAL              1 (_print + NULL)
                LOAD_CONST              13 ('skipped: brokerages.id=')
                LOAD_GLOBAL              4 (DEMO_ID)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              14 (' already matches target (name=')

 140            LOAD_FAST                2 (existing)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              15 ('name')
                CALL                     1
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              16 (', owner_email=')

 141            LOAD_FAST                2 (existing)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              17 ('owner_email')
                CALL                     1
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              18 (', active=')

 142            LOAD_FAST                2 (existing)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              19 ('active')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              20 (')')

 139            BUILD_STRING             9
                CALL                     1
                POP_TOP

 143            LOAD_SMALL_INT           0
                RETURN_VALUE

 145    L8:     NOP

 146    L9:     LOAD_GLOBAL             29 (_update_demo + NULL)
                LOAD_FAST                1 (db)
                CALL                     1
                POP_TOP

 152   L10:     BUILD_LIST               0
                STORE_FAST               3 (diffs)

 153            LOAD_CONST              15 ('name')
                LOAD_GLOBAL             20 (DEMO_NAME)
                LOAD_CONST              17 ('owner_email')
                LOAD_GLOBAL             22 (DEMO_OWNER_EMAIL)
                LOAD_CONST              19 ('active')
                LOAD_CONST              22 (True)
                BUILD_MAP                3
                STORE_FAST               4 (target)

 154            LOAD_GLOBAL             30 (_IDENTITY_FIELDS)
                GET_ITER
       L11:     FOR_ITER                63 (to L13)
                STORE_FAST               5 (k)

 155            LOAD_FAST                2 (existing)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_FAST                5 (k)
                CALL                     1
                STORE_FAST               6 (before)

 156            LOAD_FAST_LOAD_FAST     69 (target, k)
                BINARY_OP               26 ([])
                STORE_FAST               7 (after)

 157            LOAD_FAST_LOAD_FAST    103 (before, after)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           36 (to L11)

 158   L12:     LOAD_FAST                3 (diffs)
                LOAD_ATTR               33 (append + NULL|self)
                LOAD_FAST                5 (k)
                FORMAT_SIMPLE
                LOAD_CONST               4 (': ')
                LOAD_FAST                6 (before)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              23 (' -> ')
                LOAD_FAST                7 (after)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                BUILD_STRING             5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           65 (to L11)

 154   L13:     END_FOR
                POP_ITER

 159            LOAD_GLOBAL              1 (_print + NULL)
                LOAD_CONST              24 ('updated: brokerages.id={!r} | {}')
                LOAD_ATTR               35 (format + NULL|self)
                LOAD_GLOBAL              4 (DEMO_ID)
                LOAD_CONST              25 ('; ')
                LOAD_ATTR               37 (join + NULL|self)
                LOAD_FAST                3 (diffs)
                CALL                     1
                CALL                     2
                CALL                     1
                POP_TOP

 160            LOAD_SMALL_INT           0
                RETURN_VALUE

  --   L14:     PUSH_EXC_INFO

 114            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       48 (to L18)
                NOT_TAKEN
                STORE_FAST               0 (e)

 115   L15:     LOAD_GLOBAL              1 (_print + NULL)
                LOAD_CONST               3 ('error: Supabase client init failed: ')
                LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                0 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST               4 (': ')
                LOAD_FAST                0 (e)
                FORMAT_SIMPLE
                BUILD_STRING             4
                CALL                     1
                POP_TOP

 116   L16:     POP_EXCEPT
                LOAD_CONST               5 (None)
                STORE_FAST               0 (e)
                DELETE_FAST              0 (e)
                LOAD_SMALL_INT           2
                RETURN_VALUE

  --   L17:     LOAD_CONST               5 (None)
                STORE_FAST               0 (e)
                DELETE_FAST              0 (e)
                RERAISE                  1

 114   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L20:     PUSH_EXC_INFO

 122            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       56 (to L24)
                NOT_TAKEN
                STORE_FAST               0 (e)

 123   L21:     LOAD_GLOBAL              1 (_print + NULL)
                LOAD_CONST               6 ('error: lookup of brokerages.id=')
                LOAD_GLOBAL              4 (DEMO_ID)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST               7 (' failed: ')

 124            LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                0 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST               4 (': ')
                LOAD_FAST                0 (e)
                FORMAT_SIMPLE

 123            BUILD_STRING             6
                CALL                     1
                POP_TOP

 125   L22:     POP_EXCEPT
                LOAD_CONST               5 (None)
                STORE_FAST               0 (e)
                DELETE_FAST              0 (e)
                LOAD_SMALL_INT           3
                RETURN_VALUE

  --   L23:     LOAD_CONST               5 (None)
                STORE_FAST               0 (e)
                DELETE_FAST              0 (e)
                RERAISE                  1

 122   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L26:     PUSH_EXC_INFO

 130            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       56 (to L30)
                NOT_TAKEN
                STORE_FAST               0 (e)

 131   L27:     LOAD_GLOBAL              1 (_print + NULL)
                LOAD_CONST               8 ('error: insert of brokerages.id=')
                LOAD_GLOBAL              4 (DEMO_ID)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST               7 (' failed: ')

 132            LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                0 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST               4 (': ')
                LOAD_FAST                0 (e)
                FORMAT_SIMPLE

 131            BUILD_STRING             6
                CALL                     1
                POP_TOP

 133   L28:     POP_EXCEPT
                LOAD_CONST               5 (None)
                STORE_FAST               0 (e)
                DELETE_FAST              0 (e)
                LOAD_SMALL_INT           3
                RETURN_VALUE

  --   L29:     LOAD_CONST               5 (None)
                STORE_FAST               0 (e)
                DELETE_FAST              0 (e)
                RERAISE                  1

 130   L30:     RERAISE                  0

  --   L31:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L32:     PUSH_EXC_INFO

 147            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       56 (to L36)
                NOT_TAKEN
                STORE_FAST               0 (e)

 148   L33:     LOAD_GLOBAL              1 (_print + NULL)
                LOAD_CONST              21 ('error: update of brokerages.id=')
                LOAD_GLOBAL              4 (DEMO_ID)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST               7 (' failed: ')

 149            LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                0 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST               4 (': ')
                LOAD_FAST                0 (e)
                FORMAT_SIMPLE

 148            BUILD_STRING             6
                CALL                     1
                POP_TOP

 150   L34:     POP_EXCEPT
                LOAD_CONST               5 (None)
                STORE_FAST               0 (e)
                DELETE_FAST              0 (e)
                LOAD_SMALL_INT           3
                RETURN_VALUE

  --   L35:     LOAD_CONST               5 (None)
                STORE_FAST               0 (e)
                DELETE_FAST              0 (e)
                RERAISE                  1

 147   L36:     RERAISE                  0

  --   L37:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L14 [0]
  L3 to L4 -> L20 [0]
  L5 to L6 -> L26 [0]
  L9 to L10 -> L32 [0]
  L14 to L15 -> L19 [1] lasti
  L15 to L16 -> L17 [1] lasti
  L17 to L19 -> L19 [1] lasti
  L20 to L21 -> L25 [1] lasti
  L21 to L22 -> L23 [1] lasti
  L23 to L25 -> L25 [1] lasti
  L26 to L27 -> L31 [1] lasti
  L27 to L28 -> L29 [1] lasti
  L29 to L31 -> L31 [1] lasti
  L32 to L33 -> L37 [1] lasti
  L33 to L34 -> L35 [1] lasti
  L35 to L37 -> L37 [1] lasti
```
