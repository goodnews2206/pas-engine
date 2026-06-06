# scripts_readiness/security_audit

- **pyc:** `scripts\__pycache__\security_audit.cpython-314.pyc`
- **expected source path (absent):** `scripts/security_audit.py`
- **co_filename (from bytecode):** `C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS143E — Static security & integrity audit scanner.

Walks the repo and surfaces:
  - hardcoded secrets / API keys / tokens / DB URLs
  - committed backup or log artefacts
  - stray `print(` calls in production code
  - wildcard CORS that isn't gated by environment
  - silent broad `except Exception` blocks (no logger, no re-raise)
  - dangerous TODO / FIXME / XXX markers (auth / secret / tenant / pii)
  - logging that may leak transcripts, payloads, or PII
  - query functions where brokerage_id is OPTIONAL

Defensive-only — never modifies files. Severity levels:
  CRITICAL > HIGH > MEDIUM > LOW > INFO

Usage:
  python scripts/security_audit.py
  python scripts/security_audit.py --strict      # exit 1 on HIGH+
  python scripts/security_audit.py --json        # machine output
  python scripts/security_audit.py --summary-only

Always writes:
  security_audit_report.json   (next to the script's CWD)

Exit codes:
    0  — passed (no findings at or above threshold)
    1  — findings at threshold (only with --strict)
    2  — bad CLI arguments
```

## Imports

`Iterable`, `List`, `Optional`, `Path`, `Tuple`, `__future__`, `annotations`, `argparse`, `ast`, `dataclass`, `dataclasses`, `datetime`, `field`, `json`, `os`, `pathlib`, `re`, `sys`, `timezone`, `typing`

## Classes

`AuditReport`, `Finding`

## Functions / methods

`__annotate__`, `_ast_walk`, `_function_body_calls`, `_is_self_file`, `_iter_source_files`, `_password_looks_like_placeholder`, `_print_human`, `_rel`, `check_committed_backup_artifacts`, `check_dangerous_todos`, `check_full_payload_print_or_log`, `check_literal_secrets`, `check_optional_brokerage_id`, `check_pii_logging`, `check_print_statements`, `check_silent_broad_except`, `check_wildcard_cors`, `main`, `run_audit`

## Env-key candidates

`CRITICAL`, `ENVIRONMENT`, `HIGH`, `INFO`, `LOW`, `MEDIUM`

## String constants (redacted where noted)

- "\nPAS143E — Static security & integrity audit scanner.\n\nWalks the repo and surfaces:\n  - hardcoded secrets / API keys / tokens / DB URLs\n  - committed backup or log artefacts\n  - stray `print(` calls in production code\n  - wildcard CORS that isn't gated by environment\n  - silent broad `except Exception` blocks (no logger, no re-raise)\n  - dangerous TODO / FIXME / XXX markers (auth / secret / tenant / pii)\n  - logging that may leak transcripts, payloads, or PII\n  - query functions where brokerage_id is OPTIONAL\n\nDefensive-only — never modifies files. Severity levels:\n  CRITICAL > HIGH > MEDIUM > LOW > INFO\n\nUsage:\n  python scripts/security_audit.py\n  python scripts/security_audit.py --strict      # exit 1 on HIGH+\n  python scripts/security_audit.py --json        # machine output\n  python scripts/security_audit.py --summary-only\n\nAlways writes:\n  security_audit_report.json   (next to the script's CWD)\n\nExit codes:\n    0  — passed (no findings at or above threshold)\n    1  — findings at threshold (only with --strict)\n    2  — bad CLI arguments\n"
- 'utf-8'
- 'CRITICAL'
- 'HIGH'
- 'Finding'
- 'scripts/security_audit.py'
- 'scripts/integrity_check.py'
- 'eyJhbGciOiJIUzI1Ni[A-Za-z0-9_\\-\\.]{20,}'
- 'secret'
- 'Supabase / JWT HS256 token literal in source'
- 'sb_[a-z]+_[A-Za-z0-9_\\-]{30,}'
- 'Supabase service-role key literal'
- 'AC[a-f0-9]{32}\\b'
- 'Twilio Account SID literal'
- '\\bSK[a-f0-9]{32}\\b'
- 'Twilio API Key SID literal'
- '\\bre_[A-Za-z0-9_\\-]{20,}'
- 'Resend API key literal'
- 'sk-[A-Za-z0-9]{20,}'
- 'OpenAI / Anthropic style key literal'
- 'postgres(?:ql)?://[^:\\s\'\\"]+:([^@\\s\'\\"]+)@'
- 'Postgres URL with embedded credentials'
- 'List[Tuple[re.Pattern, str, str, str]]'
- '_LITERAL_SECRET_PATTERNS'
- '\\b(TODO|FIXME|XXX|HACK)\\b'
- 'AuditReport'
- 'str'
- 'severity'
- 'title'
- 'file'
- 'int'
- 'line'
- 'detail'
- 'category'
- 'suggestion'
- 'return'
- 'dict'
- 'value'
- 'bool'
- 'True iff the matched password portion is obviously fake.'
- '*<>x?'
- 'repo_root'
- 'Path'
- 'Iterable[Path]'
- 'path'
- 'rel_path'
- 'List[Finding]'
- 'ignore'
- 'postgres'
- 'secret_'
- 'Literal matches pattern (fingerprint='
- 'Move to env var; rotate the credential immediately.'
- 'Flag any *.dump / *.backup / *.jsonl / *.log under app|scripts|tests.'
- 'artifact_'
- 'Forbidden backup/log artefact under '
- 'File extension '
- ' should never be tracked.'
- 'repo_hygiene'
- 'Add to .gitignore + delete from working tree.'
- 'Stray `print(` in production app/ code (scripts/* are CLIs — print is fine).'
- '^\\s*print\\s*\\('
- 'app'
- '*.py'
- 'print_'
- 'MEDIUM'
- '`print(` in production app code'
- 'Use logger.* instead — print bypasses log levels and rotation.'
- 'logging'
- 'Replace with logger.info/debug/warning.'
- 'Optional[ast.Module]'
- 'Flag bare `except Exception:` blocks whose body is only `pass` or\na return without any logger call. Each such block silently swallows\nthe failure.'
- 'silent_except_'
- 'LOW'
- 'Broad `except Exception` with no logger call'
- 'Failure silently swallowed; debugging future incidents will be harder.'
- 'error_handling'
- 'Add a logger.warning call with type(e).__name__.'
- 'body'
- 'list'
- 'logger'
- 'Look for CORSMiddleware allow_origins=[\'*\'] not gated by an\nenvironment check. The current main.py gates wildcard with\n\'if ENVIRONMENT == "development"\', which is fine — we only flag\nungated wildcards.'
- 'allow_origins=["*"]'
- "allow_origins = ['*']"
- 'allow_origins = ["*"]'
- 'cors_'
- 'INFO'
- 'Wildcard CORS gated by environment'
- 'Ungated wildcard CORS'
- 'Acceptable for dev only.'
- 'Production exposure risk.'
- 'cors'
- 'None.'
- 'Restrict allow_origins to the production hostnames.'
- 'ENVIRONMENT'
- 'development'
- 'is_dev'
- 'Flag TODO / FIXME / XXX whose surrounding context mentions\nauth / secret / tenant / brokerage / pii / validation.'
- 'todo_'
- 'TODO / FIXME mentioning sensitive concern'
- "Marker '"
- "' near sensitive token; review and resolve."
- 'tooling'
- 'Resolve or downgrade the comment with a tracked ticket id.'
- 'Heuristic — flag logger.* calls in production paths whose\nmessage string mentions transcript / payload / phone / etc.\n\nPAS143F1: recognise calls that have already been routed through a\n`safe_transcript_preview` / `safe_payload_summary` / `redact_pii`\nhelper, AND recognise length-only metadata of the form\n`len(transcript)` / `chars=len(...)` — both forms are sanctioned\nand must not be flagged.'
- 'logger\\.(debug|info|warning|error|exception)\\s*\\(([^)]*)\\)'
- 'len('
- 'transcript'
- 'websocket'
- 'pii_log_'
- 'Logger may emit PII / payload'
- 'Token(s) detected in log args: '
- 'Truncate, redact, or downgrade to debug.'
- 'node'
- 'ast.FunctionDef'
- 'name'
- 'True iff the function body contains a Call to a function named `name`.'
- 'Audit query helpers in services/intelligence + services/replay +\nservices/workflows — flag every public function whose `brokerage_id`\nparameter has a default of None.\n\nPAS143F1: skip functions whose body calls `require_tenant_or_unscoped`\n(the hardening sentinel) and skip explicit `*_unscoped` wrappers\n(those are the *sanctioned* unscoped path).'
- 'services'
- 'intelligence'
- 'queries.py'
- 'workflows'
- 'replay'
- 'event_reader.py'
- '_unscoped'
- 'require_tenant_or_unscoped'
- 'brokerage_id'
- 'tenant_optional_'
- '()` accepts brokerage_id=None'
- 'Tenant filter is OPTIONAL — caller-side mistake could return cross-tenant rows.'
- 'tenant_isolation'
- 'Make brokerage_id required, or add an admin kwarg + assert when None is allowed.'
- 'Flag `logger.X(payload)` / `print(payload)` / `logger.X(row)`\nwhere the only argument is a dict-like local. Heuristic.'
- '(logger\\.\\w+|print)\\s*\\(\\s*(payload|row|metadata|transcript|lead_data)\\s*\\)'
- 'full_payload_log_'
- 'Full payload-shaped object logged or printed'
- 'Argument: '
- ' — likely contains nested PII.'
- 'Log a small summary (id + length) or redact before printing.'
- 'generated_at'
- 'findings'
- 'tool'
- 'pas143e.security_audit'
- 'counts'
- 'report'
- 'summary_only'
- 'None'
- 'PAS143E — SECURITY & INTEGRITY AUDIT'
- '  No findings.'
- '  ['
- '        '
- '        → '
- '========================================================================'
- '------------------------------------------------------------------------'
- 'argv'
- 'Optional[list]'
- 'security_audit'
- 'PAS143E — static security & integrity scanner.'
- '--strict'
- 'store_true'
- 'Exit non-zero if any HIGH or CRITICAL finding is present.'
- '--json'
- 'Emit the report as JSON.'
- '--summary-only'
- 'Print only the severity counts.'
- '--repo-root'
- "Override the repo root (defaults to script's parent dir)."
- 'security_audit_report.json'
- 'WARNING: could not write report: '
- '  report: '

## Disassembly

```
  --            MAKE_CELL                2 (__conditional_annotations__)

   0            RESUME                   0

   1            BUILD_SET                0
                STORE_NAME               0 (__conditional_annotations__)
                SETUP_ANNOTATIONS
                LOAD_CONST               0 ("\nPAS143E — Static security & integrity audit scanner.\n\nWalks the repo and surfaces:\n  - hardcoded secrets / API keys / tokens / DB URLs\n  - committed backup or log artefacts\n  - stray `print(` calls in production code\n  - wildcard CORS that isn't gated by environment\n  - silent broad `except Exception` blocks (no logger, no re-raise)\n  - dangerous TODO / FIXME / XXX markers (auth / secret / tenant / pii)\n  - logging that may leak transcripts, payloads, or PII\n  - query functions where brokerage_id is OPTIONAL\n\nDefensive-only — never modifies files. Severity levels:\n  CRITICAL > HIGH > MEDIUM > LOW > INFO\n\nUsage:\n  python scripts/security_audit.py\n  python scripts/security_audit.py --strict      # exit 1 on HIGH+\n  python scripts/security_audit.py --json        # machine output\n  python scripts/security_audit.py --summary-only\n\nAlways writes:\n  security_audit_report.json   (next to the script's CWD)\n\nExit codes:\n    0  — passed (no findings at or above threshold)\n    1  — findings at threshold (only with --strict)\n    2  — bad CLI arguments\n")
                STORE_NAME               1 (__doc__)

  32            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('annotations',))
                IMPORT_NAME              2 (__future__)
                IMPORT_FROM              3 (annotations)
                STORE_NAME               3 (annotations)
                POP_TOP

  34            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              4 (argparse)
                STORE_NAME               4 (argparse)

  35            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              5 (ast)
                STORE_NAME               5 (ast)

  36            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              6 (json)
                STORE_NAME               6 (json)

  37            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              7 (os)
                STORE_NAME               7 (os)

  38            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              8 (re)
                STORE_NAME               8 (re)

  39            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              9 (sys)
                STORE_NAME               9 (sys)

  40            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('dataclass', 'field'))
                IMPORT_NAME             10 (dataclasses)
                IMPORT_FROM             11 (dataclass)
                STORE_NAME              11 (dataclass)
                IMPORT_FROM             12 (field)
                STORE_NAME              12 (field)
                POP_TOP

  41            LOAD_SMALL_INT           0
                LOAD_CONST               4 (('datetime', 'timezone'))
                IMPORT_NAME             13 (datetime)
                IMPORT_FROM             13 (datetime)
                STORE_NAME              13 (datetime)
                IMPORT_FROM             14 (timezone)
                STORE_NAME              14 (timezone)
                POP_TOP

  42            LOAD_SMALL_INT           0
                LOAD_CONST               5 (('Path',))
                IMPORT_NAME             15 (pathlib)
                IMPORT_FROM             16 (Path)
                STORE_NAME              16 (Path)
                POP_TOP

  43            LOAD_SMALL_INT           0
                LOAD_CONST               6 (('Iterable', 'List', 'Optional', 'Tuple'))
                IMPORT_NAME             17 (typing)
                IMPORT_FROM             18 (Iterable)
                STORE_NAME              18 (Iterable)
                IMPORT_FROM             19 (List)
                STORE_NAME              19 (List)
                IMPORT_FROM             20 (Optional)
                STORE_NAME              20 (Optional)
                IMPORT_FROM             21 (Tuple)
                STORE_NAME              21 (Tuple)
                POP_TOP

  47            LOAD_NAME                9 (sys)
                LOAD_ATTR               44 (stdout)
                LOAD_NAME                9 (sys)
                LOAD_ATTR               46 (stderr)
                BUILD_TUPLE              2
                GET_ITER
        L1:     FOR_ITER                22 (to L4)
                STORE_NAME              24 (_stream)

  48            NOP

  49    L2:     LOAD_NAME               24 (_stream)
                LOAD_ATTR               51 (reconfigure + NULL|self)
                LOAD_CONST               7 ('utf-8')
                LOAD_CONST               8 (('encoding',))
                CALL_KW                  1
                POP_TOP
        L3:     JUMP_BACKWARD           24 (to L1)

  47    L4:     END_FOR
                POP_ITER

  58            LOAD_CONST              72 (('CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'INFO'))
                STORE_NAME              27 (SEVERITIES)

  59            LOAD_NAME               28 (enumerate)
                PUSH_NULL
                LOAD_NAME               27 (SEVERITIES)
                CALL                     1
                GET_ITER
                LOAD_FAST_AND_CLEAR      0 (i)
                LOAD_FAST_AND_CLEAR      1 (s)
                SWAP                     3
        L5:     BUILD_MAP                0
                SWAP                     2
        L6:     FOR_ITER                 7 (to L7)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST    1 (i, s)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (s, i)
                MAP_ADD                  2
                JUMP_BACKWARD            9 (to L6)
        L7:     END_FOR
                POP_ITER
        L8:     SWAP                     3
                STORE_FAST               1 (s)
                STORE_FAST               0 (i)
                STORE_NAME              29 (_SEVERITY_RANK)

  62            LOAD_NAME               11 (dataclass)

  63            LOAD_BUILD_CLASS
                PUSH_NULL
                LOAD_CONST              11 (<code object Finding at 0x0000018C17FE17D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 62>)
                MAKE_FUNCTION
                LOAD_CONST              12 ('Finding')
                CALL                     2

  62            CALL                     0

  63            STORE_NAME              30 (Finding)

  93            LOAD_CONST              73 (('app', 'scripts'))
                STORE_NAME              31 (_SCAN_DIRS)

  96            BUILD_SET                0
                LOAD_CONST              74 (frozenset({'dist', 'static', '.pytest_cache', 'node_modules', '.venv', 'build', 'venv', 'combined_supabase_migration.sql', '.git', '__pycache__'}))
                SET_UPDATE               1
                STORE_NAME              32 (_EXCLUDE_PATH_PARTS)

 109            LOAD_CONST              13 ('scripts/security_audit.py')

 110            LOAD_CONST              14 ('scripts/integrity_check.py')

 108            BUILD_SET                2
                STORE_NAME              33 (_SELF_FILES)

 120            LOAD_NAME                8 (re)
                LOAD_ATTR               68 (compile)
                PUSH_NULL
                LOAD_CONST              15 ('eyJhbGciOiJIUzI1Ni[A-Za-z0-9_\\-\\.]{20,}')
                CALL                     1

 121            LOAD_CONST               9 ('CRITICAL')
                LOAD_CONST              16 ('secret')
                LOAD_CONST              17 ('Supabase / JWT HS256 token literal in source')

 120            BUILD_TUPLE              4

 122            LOAD_NAME                8 (re)
                LOAD_ATTR               68 (compile)
                PUSH_NULL
                LOAD_CONST              18 ('sb_[a-z]+_[A-Za-z0-9_\\-]{30,}')
                CALL                     1

 123            LOAD_CONST               9 ('CRITICAL')
                LOAD_CONST              16 ('secret')
                LOAD_CONST              19 ('Supabase service-role key literal')

 122            BUILD_TUPLE              4

 124            LOAD_NAME                8 (re)
                LOAD_ATTR               68 (compile)
                PUSH_NULL
                LOAD_CONST              20 ('AC[a-f0-9]{32}\\b')
                CALL                     1

 125            LOAD_CONST               9 ('CRITICAL')
                LOAD_CONST              16 ('secret')
                LOAD_CONST              21 ('Twilio Account SID literal')

 124            BUILD_TUPLE              4

 126            LOAD_NAME                8 (re)
                LOAD_ATTR               68 (compile)
                PUSH_NULL
                LOAD_CONST              22 ('\\bSK[a-f0-9]{32}\\b')
                CALL                     1

 127            LOAD_CONST               9 ('CRITICAL')
                LOAD_CONST              16 ('secret')
                LOAD_CONST              23 ('Twilio API Key SID literal')

 126            BUILD_TUPLE              4

 128            LOAD_NAME                8 (re)
                LOAD_ATTR               68 (compile)
                PUSH_NULL
                LOAD_CONST              24 ('\\bre_[A-Za-z0-9_\\-]{20,}')
                CALL                     1

 129            LOAD_CONST              10 ('HIGH')
                LOAD_CONST              16 ('secret')
                LOAD_CONST              25 ('Resend API key literal')

 128            BUILD_TUPLE              4

 130            LOAD_NAME                8 (re)
                LOAD_ATTR               68 (compile)
                PUSH_NULL
                LOAD_CONST              26 ('sk-[A-Za-z0-9]{20,}')
                CALL                     1

 131            LOAD_CONST              10 ('HIGH')
                LOAD_CONST              16 ('secret')
                LOAD_CONST              27 ('OpenAI / Anthropic style key literal')

 130            BUILD_TUPLE              4

 132            LOAD_NAME                8 (re)
                LOAD_ATTR               68 (compile)
                PUSH_NULL
                LOAD_CONST              28 ('postgres(?:ql)?://[^:\\s\'\\"]+:([^@\\s\'\\"]+)@')
                CALL                     1

 133            LOAD_CONST              10 ('HIGH')
                LOAD_CONST              16 ('secret')
                LOAD_CONST              29 ('Postgres URL with embedded credentials')

 132            BUILD_TUPLE              4

 119            BUILD_LIST               7
                STORE_NAME              35 (_LITERAL_SECRET_PATTERNS)
                LOAD_CONST              30 ('List[Tuple[re.Pattern, str, str, str]]')
                LOAD_NAME               36 (__annotations__)
                LOAD_CONST              31 ('_LITERAL_SECRET_PATTERNS')
                STORE_SUBSCR

 140            LOAD_NAME               37 (frozenset)
                PUSH_NULL
                BUILD_SET                0
                LOAD_CONST              75 (frozenset({'p', 'xxx', 'your_password', 'dummy', 'test', 'secret', '****', 'u', '{password}', 'example', 'password', '<your-password>', 'hunter2', 'redacted', 'pwd', '<password>', 'xxxx', 'changeme', '***'}))
                SET_UPDATE               1
                CALL                     1
                STORE_NAME              38 (_POSTGRES_PASSWORD_PLACEHOLDERS)

 148            LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA3E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 148>)
                MAKE_FUNCTION
                LOAD_CONST              33 (<code object _password_looks_like_placeholder at 0x0000018C17972550, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 148>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              39 (_password_looks_like_placeholder)

 161            LOAD_NAME                8 (re)
                LOAD_ATTR               68 (compile)
                PUSH_NULL
                LOAD_CONST              34 ('\\b(TODO|FIXME|XXX|HACK)\\b')
                LOAD_NAME                8 (re)
                LOAD_ATTR               80 (IGNORECASE)
                CALL                     2
                STORE_NAME              41 (_TODO_RE)

 162            LOAD_CONST              76 (('auth', 'secret', 'key', 'tenant', 'brokerage', 'permission', 'rbac', 'rls', 'pii', 'leak', 'validate'))
                STORE_NAME              42 (_TODO_DANGER_TOKENS)

 171            LOAD_CONST              77 (('transcript', 'phone_number', 'lead_name', 'lead_data', 'payload', 'raw_text', 'full_response'))
                STORE_NAME              43 (_PII_TOKENS_IN_LOG)

 181            LOAD_CONST              35 (<code object __annotate__ at 0x0000018C17FA3960, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 181>)
                MAKE_FUNCTION
                LOAD_CONST              36 (<code object _iter_source_files at 0x0000018C17CD2160, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 181>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              44 (_iter_source_files)

 196            LOAD_CONST              37 (<code object __annotate__ at 0x0000018C18025C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 196>)
                MAKE_FUNCTION
                LOAD_CONST              38 (<code object _rel at 0x0000018C17972D90, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 196>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              45 (_rel)

 203            LOAD_CONST              39 (<code object __annotate__ at 0x0000018C17FA2E20, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 203>)
                MAKE_FUNCTION
                LOAD_CONST              40 (<code object _is_self_file at 0x0000018C17FA3C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 203>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              46 (_is_self_file)

 211            LOAD_CONST              41 (<code object __annotate__ at 0x0000018C17FA3D20, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 211>)
                MAKE_FUNCTION
                LOAD_CONST              42 (<code object check_literal_secrets at 0x0000018C181B0890, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 211>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              47 (check_literal_secrets)

 246            LOAD_CONST              43 (<code object __annotate__ at 0x0000018C17FA2A60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 246>)
                MAKE_FUNCTION
                LOAD_CONST              44 (<code object check_committed_backup_artifacts at 0x0000018C17ED1F80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 246>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              48 (check_committed_backup_artifacts)

 272            LOAD_CONST              45 (<code object __annotate__ at 0x0000018C17FA2970, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 272>)
                MAKE_FUNCTION
                LOAD_CONST              46 (<code object check_print_statements at 0x0000018C18646C00, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 272>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              49 (check_print_statements)

 298            LOAD_CONST              47 (<code object __annotate__ at 0x0000018C17FA23D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 298>)
                MAKE_FUNCTION
                LOAD_CONST              48 (<code object _ast_walk at 0x0000018C17FE1290, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 298>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              50 (_ast_walk)

 305            LOAD_CONST              49 (<code object __annotate__ at 0x0000018C17FA3B40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 305>)
                MAKE_FUNCTION
                LOAD_CONST              50 (<code object check_silent_broad_except at 0x0000018C17D83FE0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 305>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              51 (check_silent_broad_except)

 364            LOAD_CONST              51 (<code object __annotate__ at 0x0000018C17FA35A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 364>)
                MAKE_FUNCTION
                LOAD_CONST              52 (<code object check_wildcard_cors at 0x0000018C17D6DFC0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 364>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              52 (check_wildcard_cors)

 403            LOAD_CONST              53 (<code object __annotate__ at 0x0000018C17FA1D40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 403>)
                MAKE_FUNCTION
                LOAD_CONST              54 (<code object check_dangerous_todos at 0x0000018C17E88A00, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 403>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              53 (check_dangerous_todos)

 439            LOAD_CONST              78 (('safe_transcript_preview', 'safe_payload_summary', 'redact_pii'))
                STORE_NAME              54 (_REDACTION_HELPER_TOKENS)

 446            LOAD_CONST              55 (<code object __annotate__ at 0x0000018C17FA2880, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 446>)
                MAKE_FUNCTION
                LOAD_CONST              56 (<code object check_pii_logging at 0x0000018C181A1B70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 446>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              55 (check_pii_logging)

 501            LOAD_CONST              57 (<code object __annotate__ at 0x0000018C18026430, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 501>)
                MAKE_FUNCTION
                LOAD_CONST              58 (<code object _function_body_calls at 0x0000018C17ECF000, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 501>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              56 (_function_body_calls)

 514            LOAD_CONST              59 (<code object __annotate__ at 0x0000018C17FA2100, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 514>)
                MAKE_FUNCTION
                LOAD_CONST              60 (<code object check_optional_brokerage_id at 0x0000018C17F78C70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 514>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              57 (check_optional_brokerage_id)

 592            LOAD_CONST              61 (<code object __annotate__ at 0x0000018C17FA26A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 592>)
                MAKE_FUNCTION
                LOAD_CONST              62 (<code object check_full_payload_print_or_log at 0x0000018C17CD4970, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 592>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              58 (check_full_payload_print_or_log)

 624            LOAD_NAME               11 (dataclass)

 625            LOAD_BUILD_CLASS
                PUSH_NULL
                LOAD_CONST              63 (<code object AuditReport at 0x0000018C180396B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 624>)
                MAKE_FUNCTION
                LOAD_CONST              64 ('AuditReport')
                CALL                     2

 624            CALL                     0

 625            STORE_NAME              59 (AuditReport)

 649            LOAD_CONST              65 (<code object __annotate__ at 0x0000018C17FA25B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 649>)
                MAKE_FUNCTION
                LOAD_CONST              66 (<code object run_audit at 0x0000018C17D789F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 649>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              60 (run_audit)

 672            LOAD_CONST              67 (<code object __annotate__ at 0x0000018C18025F30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 672>)
                MAKE_FUNCTION
                LOAD_CONST              68 (<code object _print_human at 0x0000018C17D7D500, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 672>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              61 (_print_human)

 699            LOAD_CONST              79 ((None,))
                LOAD_CONST              69 (<code object __annotate__ at 0x0000018C17FA2D30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 699>)
                MAKE_FUNCTION
                LOAD_CONST              70 (<code object main at 0x0000018C182E2020, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 699>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              62 (main)

 738            LOAD_NAME               63 (__name__)
                LOAD_CONST              71 ('__main__')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       14 (to L9)
                NOT_TAKEN

 739            LOAD_NAME               64 (SystemExit)
                PUSH_NULL
                LOAD_NAME               62 (main)
                PUSH_NULL
                CALL                     0
                CALL                     1
                RAISE_VARARGS            1

 738    L9:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L10:     PUSH_EXC_INFO

  50            LOAD_NAME               26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L12)
                NOT_TAKEN
                POP_TOP

  51   L11:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD          438 (to L1)

  50   L12:     RERAISE                  0

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L14:     SWAP                     2
                POP_TOP

  59            SWAP                     3
                STORE_FAST               1 (s)
                STORE_FAST               0 (i)
                RERAISE                  0
ExceptionTable:
  L2 to L3 -> L10 [1]
  L5 to L8 -> L14 [3]
  L10 to L11 -> L13 [2] lasti
  L12 to L13 -> L13 [2] lasti

Disassembly of <code object Finding at 0x0000018C17FE17D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 62>:
 62           RESUME                   0
              LOAD_NAME                0 (__name__)
              STORE_NAME               1 (__module__)
              LOAD_CONST               0 ('Finding')
              STORE_NAME               2 (__qualname__)
              LOAD_SMALL_INT          62
              STORE_NAME               3 (__firstlineno__)
              SETUP_ANNOTATIONS

 64           LOAD_CONST               1 ('str')
              LOAD_NAME                4 (__annotations__)
              LOAD_CONST               2 ('id')
              STORE_SUBSCR

 65           LOAD_CONST               1 ('str')
              LOAD_NAME                4 (__annotations__)
              LOAD_CONST               3 ('severity')
              STORE_SUBSCR

 66           LOAD_CONST               1 ('str')
              LOAD_NAME                4 (__annotations__)
              LOAD_CONST               4 ('title')
              STORE_SUBSCR

 67           LOAD_CONST               1 ('str')
              LOAD_NAME                4 (__annotations__)
              LOAD_CONST               5 ('file')
              STORE_SUBSCR

 68           LOAD_CONST               6 ('int')
              LOAD_NAME                4 (__annotations__)
              LOAD_CONST               7 ('line')
              STORE_SUBSCR

 69           LOAD_CONST               1 ('str')
              LOAD_NAME                4 (__annotations__)
              LOAD_CONST               8 ('detail')
              STORE_SUBSCR

 70           LOAD_CONST               1 ('str')
              LOAD_NAME                4 (__annotations__)
              LOAD_CONST               9 ('category')
              STORE_SUBSCR

 71           LOAD_CONST              10 ('')
              STORE_NAME               5 (suggestion)
              LOAD_CONST               1 ('str')
              LOAD_NAME                4 (__annotations__)
              LOAD_CONST              11 ('suggestion')
              STORE_SUBSCR

 73           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA31E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 73>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object to_dict at 0x0000018C1804D070, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 73>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME               6 (to_dict)
              LOAD_CONST              14 (())
              STORE_NAME               7 (__static_attributes__)
              LOAD_CONST              15 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 73>:
 73           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('dict')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object to_dict at 0x0000018C1804D070, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 73>:
 73           RESUME                   0

 75           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (id)

 76           LOAD_CONST               1 ('severity')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                2 (severity)

 77           LOAD_CONST               2 ('title')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                4 (title)

 78           LOAD_CONST               3 ('file')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                6 (file)

 79           LOAD_CONST               4 ('line')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                8 (line)

 80           LOAD_CONST               5 ('detail')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               10 (detail)

 81           LOAD_CONST               6 ('category')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               12 (category)

 82           LOAD_CONST               7 ('suggestion')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               14 (suggestion)

 74           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 148>:
148           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _password_looks_like_placeholder at 0x0000018C17972550, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 148>:
148           RESUME                   0

150           LOAD_FAST_BORROW         0 (value)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

151           LOAD_CONST               1 (True)
              RETURN_VALUE

152   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                1 (lower + NULL|self)
              CALL                     0
              STORE_FAST               1 (v)

153           LOAD_FAST_BORROW         1 (v)
              LOAD_GLOBAL              2 (_POSTGRES_PASSWORD_PLACEHOLDERS)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

154           LOAD_CONST               1 (True)
              RETURN_VALUE

156   L2:     LOAD_GLOBAL              5 (set + NULL)
              LOAD_FAST_BORROW         1 (v)
              CALL                     1
              LOAD_GLOBAL              5 (set + NULL)
              LOAD_CONST               2 ('*<>x?')
              CALL                     1
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

157           LOAD_CONST               1 (True)
              RETURN_VALUE

158   L3:     LOAD_CONST               3 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 181>:
181           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Iterable[Path]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _iter_source_files at 0x0000018C17CD2160, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 181>:
 181            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 182            LOAD_GLOBAL              0 (_SCAN_DIRS)
                GET_ITER
        L2:     FOR_ITER               200 (to L19)
                STORE_FAST               1 (d)

 183            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (repo_root, d)
                BINARY_OP               11 (/)
                STORE_FAST               2 (base)

 184            LOAD_FAST_BORROW         2 (base)
                LOAD_ATTR                3 (exists + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN

 185            JUMP_BACKWARD           35 (to L2)

 186    L3:     LOAD_FAST_BORROW         2 (base)
                LOAD_ATTR                5 (rglob + NULL|self)
                LOAD_CONST               0 ('*')
                CALL                     1
                GET_ITER
        L4:     FOR_ITER               144 (to L18)
                STORE_FAST               3 (path)

 187            LOAD_FAST_BORROW         3 (path)
                LOAD_ATTR                7 (is_file + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN

 188            JUMP_BACKWARD           27 (to L4)

 189    L5:     LOAD_GLOBAL              8 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       38 (to L12)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18128030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 189>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         3 (path)
                LOAD_ATTR               10 (parts)
                GET_ITER
                CALL                     0
        L8:     FOR_ITER                12 (to L11)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L9:     NOT_TAKEN
                JUMP_BACKWARD           11 (to L8)
       L10:     POP_ITER
                LOAD_CONST               2 (True)
                JUMP_FORWARD            27 (to L13)
       L11:     END_FOR
                POP_ITER
                LOAD_CONST               3 (False)
                JUMP_FORWARD            23 (to L13)
       L12:     PUSH_NULL
                LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18128030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 189>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         3 (path)
                LOAD_ATTR               10 (parts)
                GET_ITER
                CALL                     0
                CALL                     1
       L13:     TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L16)
       L14:     NOT_TAKEN

 190   L15:     JUMP_BACKWARD          107 (to L4)

 191   L16:     LOAD_FAST_BORROW         3 (path)
                LOAD_ATTR               12 (suffix)
                LOAD_ATTR               15 (lower + NULL|self)
                CALL                     0
                LOAD_CONST               5 (('.py', '.sql', '.html', '.js', '.json'))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L17)
                NOT_TAKEN

 192            JUMP_BACKWARD          140 (to L4)

 193   L17:     LOAD_FAST_BORROW         3 (path)
                YIELD_VALUE              0
                RESUME                   5
                POP_TOP
                JUMP_BACKWARD          146 (to L4)

 186   L18:     END_FOR
                POP_ITER
                JUMP_BACKWARD          202 (to L2)

 182   L19:     END_FOR
                POP_ITER
                LOAD_CONST               4 (None)
                RETURN_VALUE

  --   L20:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L6 -> L20 [0] lasti
  L7 to L9 -> L20 [0] lasti
  L10 to L14 -> L20 [0] lasti
  L15 to L20 -> L20 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18128030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 189>:
 189           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                13 (to L3)
               STORE_FAST_LOAD_FAST    17 (part, part)
               LOAD_GLOBAL              0 (_EXCLUDE_PATH_PARTS)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           15 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 196>:
196           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('path')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('str')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _rel at 0x0000018C17972D90, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 196>:
 196           RESUME                   0

 197           NOP

 198   L1:     LOAD_GLOBAL              1 (str + NULL)
               LOAD_FAST_BORROW         1 (path)
               LOAD_ATTR                3 (relative_to + NULL|self)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               LOAD_ATTR                5 (replace + NULL|self)
               LOAD_CONST               0 ('\\')
               LOAD_CONST               1 ('/')
               CALL                     2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 199           LOAD_GLOBAL              6 (ValueError)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       15 (to L5)
               NOT_TAKEN
               POP_TOP

 200           LOAD_GLOBAL              1 (str + NULL)
               LOAD_FAST                1 (path)
               CALL                     1
               SWAP                     2
       L4:     POP_EXCEPT
               RETURN_VALUE

 199   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 203>:
203           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rel_path')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _is_self_file at 0x0000018C17FA3C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 203>:
203           RESUME                   0

204           LOAD_FAST_BORROW         0 (rel_path)
              LOAD_GLOBAL              0 (_SELF_FILES)
              CONTAINS_OP              0 (in)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 211>:
211           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Finding]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_literal_secrets at 0x0000018C181B0890, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 211>:
 211            RESUME                   0

 212            BUILD_LIST               0
                STORE_FAST               1 (out)

 213            LOAD_GLOBAL              1 (_iter_source_files + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                GET_ITER
        L1:     EXTENDED_ARG             1
                FOR_ITER               329 (to L11)
                STORE_FAST               2 (path)

 214            LOAD_GLOBAL              3 (_rel + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (repo_root, path)
                CALL                     2
                STORE_FAST               3 (rel)

 215            LOAD_GLOBAL              5 (_is_self_file + NULL)
                LOAD_FAST_BORROW         3 (rel)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN

 216            JUMP_BACKWARD           34 (to L1)

 217    L2:     NOP

 218    L3:     LOAD_FAST_BORROW         2 (path)
                LOAD_ATTR                7 (read_text + NULL|self)
                LOAD_CONST               0 ('utf-8')
                LOAD_CONST               1 ('ignore')
                LOAD_CONST               2 (('encoding', 'errors'))
                CALL_KW                  2
                STORE_FAST               4 (text)

 221    L4:     LOAD_GLOBAL             10 (_LITERAL_SECRET_PATTERNS)
                GET_ITER
        L5:     EXTENDED_ARG             1
                FOR_ITER               264 (to L10)
                UNPACK_SEQUENCE          4
                STORE_FAST_STORE_FAST   86 (regex, severity)
                STORE_FAST_STORE_FAST  120 (category, title)

 222            LOAD_FAST                5 (regex)
                LOAD_ATTR               13 (finditer + NULL|self)
                LOAD_FAST                4 (text)
                CALL                     1
                GET_ITER
        L6:     FOR_ITER               236 (to L9)
                STORE_FAST               9 (m)

 223            LOAD_FAST                4 (text)
                LOAD_ATTR               15 (count + NULL|self)
                LOAD_CONST               3 ('\n')
                LOAD_SMALL_INT           0
                LOAD_FAST                9 (m)
                LOAD_ATTR               17 (start + NULL|self)
                CALL                     0
                CALL                     3
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                STORE_FAST              10 (line_no)

 224            LOAD_FAST                9 (m)
                LOAD_ATTR               19 (group + NULL|self)
                LOAD_SMALL_INT           0
                CALL                     1
                STORE_FAST              11 (preview)

 226            LOAD_CONST               4 ('postgres')
                LOAD_FAST               11 (preview)
                LOAD_ATTR               21 (lower + NULL|self)
                CALL                     0
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       75 (to L8)
                NOT_TAKEN
                LOAD_FAST                9 (m)
                LOAD_ATTR               22 (lastindex)
                TO_BOOL
                POP_JUMP_IF_FALSE       57 (to L8)
                NOT_TAKEN

 227            LOAD_FAST                9 (m)
                LOAD_ATTR               19 (group + NULL|self)
                LOAD_FAST                9 (m)
                LOAD_ATTR               22 (lastindex)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               5 ('')
        L7:     STORE_FAST              12 (pwd)

 228            LOAD_GLOBAL             25 (_password_looks_like_placeholder + NULL)
                LOAD_FAST               12 (pwd)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN

 229            JUMP_BACKWARD          155 (to L6)

 232    L8:     LOAD_FAST               11 (preview)
                LOAD_CONST               6 (slice(None, 12, None))
                BINARY_OP               26 ([])
                LOAD_CONST               7 ('…')
                BINARY_OP                0 (+)
                STORE_FAST              13 (fingerprint)

 233            LOAD_FAST                1 (out)
                LOAD_ATTR               27 (append + NULL|self)
                LOAD_GLOBAL             29 (Finding + NULL)

 234            LOAD_CONST               8 ('secret_')
                LOAD_FAST                5 (regex)
                LOAD_ATTR               30 (pattern)
                LOAD_CONST               9 (slice(None, 20, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST              10 ('_')
                LOAD_FAST                3 (rel)
                FORMAT_SIMPLE
                LOAD_CONST              10 ('_')
                LOAD_FAST               10 (line_no)
                FORMAT_SIMPLE
                BUILD_STRING             6

 235            LOAD_FAST                6 (severity)

 236            LOAD_FAST                8 (title)

 237            LOAD_FAST                3 (rel)

 238            LOAD_FAST               10 (line_no)

 239            LOAD_CONST              11 ('Literal matches pattern (fingerprint=')
                LOAD_FAST               13 (fingerprint)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              12 (').')
                BUILD_STRING             3

 240            LOAD_FAST                7 (category)

 241            LOAD_CONST              13 ('Move to env var; rotate the credential immediately.')

 233            LOAD_CONST              14 (('id', 'severity', 'title', 'file', 'line', 'detail', 'category', 'suggestion'))
                CALL_KW                  8
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          238 (to L6)

 222    L9:     END_FOR
                POP_ITER
                EXTENDED_ARG             1
                JUMP_BACKWARD          267 (to L5)

 221   L10:     END_FOR
                POP_ITER
                EXTENDED_ARG             1
                JUMP_BACKWARD          332 (to L1)

 213   L11:     END_FOR
                POP_ITER

 243            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 219            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L14)
                NOT_TAKEN
                POP_TOP

 220   L13:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD          351 (to L1)

 219   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L12 [1]
  L12 to L13 -> L15 [2] lasti
  L14 to L15 -> L15 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 246>:
246           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Finding]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_committed_backup_artifacts at 0x0000018C17ED1F80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 246>:
246           RESUME                   0

248           BUILD_LIST               0
              STORE_FAST               1 (out)

249           LOAD_CONST              11 (('.dump', '.backup', '.jsonl', '.log'))
              STORE_FAST               2 (forbidden)

250           LOAD_CONST              12 (('app', 'scripts', 'tests', 'docs'))
              GET_ITER
      L1:     FOR_ITER               182 (to L7)
              STORE_FAST               3 (d)

251           LOAD_FAST_BORROW_LOAD_FAST_BORROW 3 (repo_root, d)
              BINARY_OP               11 (/)
              STORE_FAST               4 (base)

252           LOAD_FAST_BORROW         4 (base)
              LOAD_ATTR                1 (exists + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

253           JUMP_BACKWARD           35 (to L1)

254   L2:     LOAD_FAST_BORROW         4 (base)
              LOAD_ATTR                3 (rglob + NULL|self)
              LOAD_CONST               1 ('*')
              CALL                     1
              GET_ITER
      L3:     FOR_ITER               126 (to L6)
              STORE_FAST               5 (path)

255           LOAD_FAST_BORROW         5 (path)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN

256           JUMP_BACKWARD           27 (to L3)

257   L4:     LOAD_FAST_BORROW         5 (path)
              LOAD_ATTR                6 (suffix)
              LOAD_ATTR                9 (lower + NULL|self)
              CALL                     0
              LOAD_FAST_BORROW         2 (forbidden)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           60 (to L3)

258   L5:     LOAD_GLOBAL             11 (_rel + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (repo_root, path)
              CALL                     2
              STORE_FAST               6 (rel)

259           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR               13 (append + NULL|self)
              LOAD_GLOBAL             15 (Finding + NULL)

260           LOAD_CONST               2 ('artifact_')
              LOAD_FAST_BORROW         6 (rel)
              FORMAT_SIMPLE
              BUILD_STRING             2

261           LOAD_CONST               3 ('HIGH')

262           LOAD_CONST               4 ('Forbidden backup/log artefact under ')
              LOAD_FAST_BORROW         3 (d)
              FORMAT_SIMPLE
              LOAD_CONST               5 ('/')
              BUILD_STRING             3

263           LOAD_FAST_BORROW         6 (rel)

264           LOAD_SMALL_INT           0

265           LOAD_CONST               6 ('File extension ')
              LOAD_FAST_BORROW         5 (path)
              LOAD_ATTR                6 (suffix)
              FORMAT_SIMPLE
              LOAD_CONST               7 (' should never be tracked.')
              BUILD_STRING             3

266           LOAD_CONST               8 ('repo_hygiene')

267           LOAD_CONST               9 ('Add to .gitignore + delete from working tree.')

259           LOAD_CONST              10 (('id', 'severity', 'title', 'file', 'line', 'detail', 'category', 'suggestion'))
              CALL_KW                  8
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          128 (to L3)

254   L6:     END_FOR
              POP_ITER
              JUMP_BACKWARD          184 (to L1)

250   L7:     END_FOR
              POP_ITER

269           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 272>:
272           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Finding]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_print_statements at 0x0000018C18646C00, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 272>:
 272            RESUME                   0

 274            BUILD_LIST               0
                STORE_FAST               1 (out)

 275            LOAD_GLOBAL              0 (re)
                LOAD_ATTR                2 (compile)
                PUSH_NULL
                LOAD_CONST               1 ('^\\s*print\\s*\\(')
                LOAD_GLOBAL              0 (re)
                LOAD_ATTR                4 (MULTILINE)
                CALL                     2
                STORE_FAST               2 (pattern)

 276            LOAD_FAST_BORROW         0 (repo_root)
                LOAD_CONST               2 ('app')
                BINARY_OP               11 (/)
                LOAD_ATTR                7 (rglob + NULL|self)
                LOAD_CONST               3 ('*.py')
                CALL                     1
                GET_ITER
        L1:     FOR_ITER               225 (to L12)
                STORE_FAST               3 (path)

 277            LOAD_GLOBAL              8 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       38 (to L5)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               4 (<code object <genexpr> at 0x0000018C18128470, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 277>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         3 (path)
                LOAD_ATTR               10 (parts)
                GET_ITER
                CALL                     0
        L2:     FOR_ITER                12 (to L4)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L2)
        L3:     POP_ITER
                LOAD_CONST               5 (True)
                JUMP_FORWARD            27 (to L6)
        L4:     END_FOR
                POP_ITER
                LOAD_CONST               6 (False)
                JUMP_FORWARD            23 (to L6)
        L5:     PUSH_NULL
                LOAD_CONST               4 (<code object <genexpr> at 0x0000018C18128470, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 277>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         3 (path)
                LOAD_ATTR               10 (parts)
                GET_ITER
                CALL                     0
                CALL                     1
        L6:     TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN

 278            JUMP_BACKWARD           83 (to L1)

 279    L7:     NOP

 280    L8:     LOAD_FAST_BORROW         3 (path)
                LOAD_ATTR               13 (read_text + NULL|self)
                LOAD_CONST               7 ('utf-8')
                LOAD_CONST               8 ('ignore')
                LOAD_CONST               9 (('encoding', 'errors'))
                CALL_KW                  2
                STORE_FAST               4 (text)

 283    L9:     LOAD_FAST                2 (pattern)
                LOAD_ATTR               17 (finditer + NULL|self)
                LOAD_FAST                4 (text)
                CALL                     1
                GET_ITER
       L10:     FOR_ITER               101 (to L11)
                STORE_FAST               5 (m)

 284            LOAD_FAST                4 (text)
                LOAD_ATTR               19 (count + NULL|self)
                LOAD_CONST              10 ('\n')
                LOAD_SMALL_INT           0
                LOAD_FAST                5 (m)
                LOAD_ATTR               21 (start + NULL|self)
                CALL                     0
                CALL                     3
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                STORE_FAST               6 (line_no)

 285            LOAD_FAST                1 (out)
                LOAD_ATTR               23 (append + NULL|self)
                LOAD_GLOBAL             25 (Finding + NULL)

 286            LOAD_CONST              11 ('print_')
                LOAD_GLOBAL             27 (_rel + NULL)
                LOAD_FAST_LOAD_FAST      3 (repo_root, path)
                CALL                     2
                FORMAT_SIMPLE
                LOAD_CONST              12 ('_')
                LOAD_FAST                6 (line_no)
                FORMAT_SIMPLE
                BUILD_STRING             4

 287            LOAD_CONST              13 ('MEDIUM')

 288            LOAD_CONST              14 ('`print(` in production app code')

 289            LOAD_GLOBAL             27 (_rel + NULL)
                LOAD_FAST_LOAD_FAST      3 (repo_root, path)
                CALL                     2

 290            LOAD_FAST                6 (line_no)

 291            LOAD_CONST              15 ('Use logger.* instead — print bypasses log levels and rotation.')

 292            LOAD_CONST              16 ('logging')

 293            LOAD_CONST              17 ('Replace with logger.info/debug/warning.')

 285            LOAD_CONST              18 (('id', 'severity', 'title', 'file', 'line', 'detail', 'category', 'suggestion'))
                CALL_KW                  8
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          103 (to L10)

 283   L11:     END_FOR
                POP_ITER
                JUMP_BACKWARD          227 (to L1)

 276   L12:     END_FOR
                POP_ITER

 295            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L13:     PUSH_EXC_INFO

 281            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L15)
                NOT_TAKEN
                POP_TOP

 282   L14:     POP_EXCEPT
                JUMP_BACKWARD          245 (to L1)

 281   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L8 to L9 -> L13 [1]
  L13 to L14 -> L16 [2] lasti
  L15 to L16 -> L16 [2] lasti

Disassembly of <code object <genexpr> at 0x0000018C18128470, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 277>:
 277           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                13 (to L3)
               STORE_FAST_LOAD_FAST    17 (part, part)
               LOAD_GLOBAL              0 (_EXCLUDE_PATH_PARTS)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           15 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 298>:
298           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('path')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[ast.Module]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _ast_walk at 0x0000018C17FE1290, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 298>:
 298           RESUME                   0

 299           NOP

 300   L1:     LOAD_GLOBAL              0 (ast)
               LOAD_ATTR                2 (parse)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                5 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('ignore')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
               CALL                     1
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 301           LOAD_GLOBAL              6 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 302   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 301   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 305>:
305           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Finding]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_silent_broad_except at 0x0000018C17D83FE0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 305>:
305            RESUME                   0

309            BUILD_LIST               0
               STORE_FAST               1 (out)

311            LOAD_CONST               1 (<code object __annotate__ at 0x0000018C17FA33C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 311>)
               MAKE_FUNCTION
               LOAD_CONST               2 (<code object _body_logs_or_raises at 0x0000018C17E95590, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 311>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_FAST               2 (_body_logs_or_raises)

330            LOAD_FAST_BORROW         0 (repo_root)
               LOAD_CONST               3 ('app')
               BINARY_OP               11 (/)
               LOAD_ATTR                1 (rglob + NULL|self)
               LOAD_CONST               4 ('*.py')
               CALL                     1
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               379 (to L16)
               STORE_FAST               3 (path)

331            LOAD_GLOBAL              2 (any)
               COPY                     1
               LOAD_COMMON_CONSTANT     4 (<built-in function any>)
               IS_OP                    0 (is)
               POP_JUMP_IF_FALSE       38 (to L5)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               5 (<code object <genexpr> at 0x0000018C18128580, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 331>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         3 (path)
               LOAD_ATTR                4 (parts)
               GET_ITER
               CALL                     0
       L2:     FOR_ITER                12 (to L4)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L2)
       L3:     POP_ITER
               LOAD_CONST               6 (True)
               JUMP_FORWARD            27 (to L6)
       L4:     END_FOR
               POP_ITER
               LOAD_CONST               7 (False)
               JUMP_FORWARD            23 (to L6)
       L5:     PUSH_NULL
               LOAD_CONST               5 (<code object <genexpr> at 0x0000018C18128580, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 331>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         3 (path)
               LOAD_ATTR                4 (parts)
               GET_ITER
               CALL                     0
               CALL                     1
       L6:     TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN

332            JUMP_BACKWARD           84 (to L1)

333    L7:     LOAD_GLOBAL              7 (_ast_walk + NULL)
               LOAD_FAST_BORROW         3 (path)
               CALL                     1
               STORE_FAST               4 (tree)

334            LOAD_FAST_BORROW         4 (tree)
               POP_JUMP_IF_NOT_NONE     3 (to L8)
               NOT_TAKEN

335            JUMP_BACKWARD          101 (to L1)

336    L8:     LOAD_GLOBAL              8 (ast)
               LOAD_ATTR               10 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         4 (tree)
               CALL                     1
               GET_ITER
       L9:     FOR_ITER               252 (to L15)
               STORE_FAST               5 (node)

337            LOAD_GLOBAL             13 (isinstance + NULL)
               LOAD_FAST_BORROW         5 (node)
               LOAD_GLOBAL              8 (ast)
               LOAD_ATTR               14 (ExceptHandler)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L10)
               NOT_TAKEN

338            JUMP_BACKWARD           37 (to L9)

340   L10:     LOAD_FAST_BORROW         5 (node)
               LOAD_ATTR               16 (type)
               STORE_FAST               6 (t)

342            LOAD_FAST_BORROW         6 (t)
               LOAD_CONST               8 (None)
               IS_OP                    0 (is)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        50 (to L11)
               NOT_TAKEN
               POP_TOP

343            LOAD_GLOBAL             13 (isinstance + NULL)
               LOAD_FAST_BORROW         6 (t)
               LOAD_GLOBAL              8 (ast)
               LOAD_ATTR               18 (Name)
               CALL                     2
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       16 (to L11)
               NOT_TAKEN
               POP_TOP
               LOAD_FAST_BORROW         6 (t)
               LOAD_ATTR               20 (id)
               LOAD_CONST              17 (('Exception', 'BaseException'))
               CONTAINS_OP              0 (in)

341   L11:     STORE_FAST               7 (broad)

345            LOAD_FAST_BORROW         7 (broad)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L12)
               NOT_TAKEN

346            JUMP_BACKWARD          120 (to L9)

347   L12:     LOAD_FAST_BORROW         2 (_body_logs_or_raises)
               PUSH_NULL
               LOAD_FAST_BORROW         5 (node)
               LOAD_ATTR               22 (body)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN

348            JUMP_BACKWARD          146 (to L9)

350   L13:     LOAD_GLOBAL             25 (len + NULL)
               LOAD_FAST_BORROW         5 (node)
               LOAD_ATTR               22 (body)
               CALL                     1
               LOAD_SMALL_INT           3
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_TRUE         3 (to L14)
               NOT_TAKEN
               JUMP_BACKWARD          174 (to L9)

351   L14:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR               27 (append + NULL|self)
               LOAD_GLOBAL             29 (Finding + NULL)

352            LOAD_CONST               9 ('silent_except_')
               LOAD_GLOBAL             31 (_rel + NULL)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 3 (repo_root, path)
               CALL                     2
               FORMAT_SIMPLE
               LOAD_CONST              10 ('_')
               LOAD_FAST_BORROW         5 (node)
               LOAD_ATTR               32 (lineno)
               FORMAT_SIMPLE
               BUILD_STRING             4

353            LOAD_CONST              11 ('LOW')

354            LOAD_CONST              12 ('Broad `except Exception` with no logger call')

355            LOAD_GLOBAL             31 (_rel + NULL)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 3 (repo_root, path)
               CALL                     2

356            LOAD_FAST_BORROW         5 (node)
               LOAD_ATTR               32 (lineno)

357            LOAD_CONST              13 ('Failure silently swallowed; debugging future incidents will be harder.')

358            LOAD_CONST              14 ('error_handling')

359            LOAD_CONST              15 ('Add a logger.warning call with type(e).__name__.')

351            LOAD_CONST              16 (('id', 'severity', 'title', 'file', 'line', 'detail', 'category', 'suggestion'))
               CALL_KW                  8
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          254 (to L9)

336   L15:     END_FOR
               POP_ITER
               EXTENDED_ARG             1
               JUMP_BACKWARD          382 (to L1)

330   L16:     END_FOR
               POP_ITER

361            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 311>:
311           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')
              LOAD_CONST               2 ('list')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _body_logs_or_raises at 0x0000018C17E95590, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 311>:
311           RESUME                   0

312           LOAD_GLOBAL              0 (ast)
              LOAD_ATTR                2 (walk)
              PUSH_NULL
              LOAD_GLOBAL              0 (ast)
              LOAD_ATTR                4 (Module)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (body)
              BUILD_LIST               0
              LOAD_CONST               0 (('body', 'type_ignores'))
              CALL_KW                  2
              CALL                     1
              GET_ITER
      L1:     EXTENDED_ARG             1
              FOR_ITER               260 (to L7)
              STORE_FAST               1 (node)

313           LOAD_GLOBAL              7 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (node)
              LOAD_GLOBAL              0 (ast)
              LOAD_ATTR                8 (Raise)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        4 (to L2)
              NOT_TAKEN

314           POP_TOP
              LOAD_CONST               1 (True)
              RETURN_VALUE

315   L2:     LOAD_GLOBAL              7 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (node)
              LOAD_GLOBAL              0 (ast)
              LOAD_ATTR               10 (Call)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           73 (to L1)

316   L3:     LOAD_FAST_BORROW         1 (node)
              LOAD_ATTR               12 (func)
              STORE_FAST               2 (func)

318           LOAD_GLOBAL              7 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (func)
              LOAD_GLOBAL              0 (ast)
              LOAD_ATTR               14 (Attribute)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       90 (to L4)
              NOT_TAKEN
              LOAD_GLOBAL              7 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (func)
              LOAD_ATTR               16 (value)
              LOAD_GLOBAL              0 (ast)
              LOAD_ATTR               18 (Name)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       48 (to L4)
              NOT_TAKEN

319           LOAD_FAST_BORROW         2 (func)
              LOAD_ATTR               16 (value)
              LOAD_ATTR               20 (id)
              LOAD_CONST               2 ('logger')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       21 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (func)
              LOAD_ATTR               22 (attr)
              LOAD_CONST               4 (('debug', 'info', 'warning', 'error', 'critical', 'exception'))
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        4 (to L4)
              NOT_TAKEN

322           POP_TOP
              LOAD_CONST               1 (True)
              RETURN_VALUE

324   L4:     LOAD_GLOBAL              7 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (func)
              LOAD_GLOBAL              0 (ast)
              LOAD_ATTR               14 (Attribute)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD          240 (to L1)
      L5:     LOAD_FAST_BORROW         2 (func)
              LOAD_ATTR               22 (attr)
              LOAD_CONST               5 (('warn', 'warning', 'error', 'critical', 'exception'))
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         4 (to L6)
              NOT_TAKEN
              EXTENDED_ARG             1
              JUMP_BACKWARD          260 (to L1)

327   L6:     POP_TOP
              LOAD_CONST               1 (True)
              RETURN_VALUE

312   L7:     END_FOR
              POP_ITER

328           LOAD_CONST               3 (False)
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18128580, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 331>:
 331           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                13 (to L3)
               STORE_FAST_LOAD_FAST    17 (part, part)
               LOAD_GLOBAL              0 (_EXCLUDE_PATH_PARTS)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           15 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 364>:
364           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Finding]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_wildcard_cors at 0x0000018C17D6DFC0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 364>:
 364            RESUME                   0

 369            BUILD_LIST               0
                STORE_FAST               1 (out)

 370            LOAD_FAST_BORROW         0 (repo_root)
                LOAD_CONST               1 ('app')
                BINARY_OP               11 (/)
                LOAD_ATTR                1 (rglob + NULL|self)
                LOAD_CONST               2 ('*.py')
                CALL                     1
                GET_ITER
        L1:     EXTENDED_ARG             1
                FOR_ITER               299 (to L21)
                STORE_FAST               2 (path)

 371            NOP

 372    L2:     LOAD_FAST_BORROW         2 (path)
                LOAD_ATTR                3 (read_text + NULL|self)
                LOAD_CONST               3 ('utf-8')
                LOAD_CONST               4 ('ignore')
                LOAD_CONST               5 (('encoding', 'errors'))
                CALL_KW                  2
                STORE_FAST               3 (text)

 375    L3:     LOAD_CONST               6 ('allow_origins=["*"]')
                LOAD_FAST                3 (text)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       17 (to L4)
                NOT_TAKEN
                LOAD_CONST               7 ("allow_origins = ['*']")
                LOAD_FAST                3 (text)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       10 (to L4)
                NOT_TAKEN

 376            LOAD_CONST               8 ('allow_origins = ["*"]')
                LOAD_FAST                3 (text)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN

 377            JUMP_BACKWARD           47 (to L1)

 379    L4:     LOAD_GLOBAL              7 (enumerate + NULL)
                LOAD_FAST                3 (text)
                LOAD_ATTR                9 (splitlines + NULL|self)
                CALL                     0
                LOAD_SMALL_INT           1
                LOAD_CONST               9 (('start',))
                CALL_KW                  2
                GET_ITER
        L5:     FOR_ITER               221 (to L20)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   69 (i, line)

 380            LOAD_CONST               6 ('allow_origins=["*"]')
                LOAD_FAST                5 (line)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE        17 (to L6)
                NOT_TAKEN
                LOAD_CONST               8 ('allow_origins = ["*"]')
                LOAD_FAST                5 (line)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE        10 (to L6)
                NOT_TAKEN

 381            LOAD_CONST               7 ("allow_origins = ['*']")
                LOAD_FAST                5 (line)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           28 (to L5)

 382    L6:     LOAD_FAST                3 (text)
                LOAD_ATTR                9 (splitlines + NULL|self)
                CALL                     0
                LOAD_GLOBAL             11 (max + NULL)
                LOAD_SMALL_INT           0
                LOAD_FAST                4 (i)
                LOAD_SMALL_INT           8
                BINARY_OP               10 (-)
                CALL                     2
                LOAD_FAST                4 (i)
                LOAD_SMALL_INT           2
                BINARY_OP                0 (+)
                BINARY_SLICE
                STORE_FAST               6 (window_lines)

 383            LOAD_GLOBAL             12 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       28 (to L10)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              10 (<code object <genexpr> at 0x0000018C1802CC10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 383>)
                MAKE_FUNCTION

 385            LOAD_FAST                6 (window_lines)
                GET_ITER

 383            CALL                     0
        L7:     FOR_ITER                12 (to L9)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L7)
        L8:     POP_ITER
                LOAD_CONST              11 (True)
                JUMP_FORWARD            17 (to L11)
        L9:     END_FOR
                POP_ITER
                LOAD_CONST              12 (False)
                JUMP_FORWARD            13 (to L11)
       L10:     PUSH_NULL
                LOAD_CONST              10 (<code object <genexpr> at 0x0000018C1802CC10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 383>)
                MAKE_FUNCTION

 385            LOAD_FAST                6 (window_lines)
                GET_ITER

 383            CALL                     0
                CALL                     1
       L11:     STORE_FAST               7 (gated)

 387            LOAD_FAST                1 (out)
                LOAD_ATTR               15 (append + NULL|self)
                LOAD_GLOBAL             17 (Finding + NULL)

 388            LOAD_CONST              13 ('cors_')
                LOAD_GLOBAL             19 (_rel + NULL)
                LOAD_FAST_LOAD_FAST      2 (repo_root, path)
                CALL                     2
                FORMAT_SIMPLE
                LOAD_CONST              14 ('_')
                LOAD_FAST                4 (i)
                FORMAT_SIMPLE
                BUILD_STRING             4

 389            LOAD_FAST                7 (gated)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN
                LOAD_CONST              15 ('INFO')
                JUMP_FORWARD             1 (to L13)
       L12:     LOAD_CONST              16 ('HIGH')

 390   L13:     LOAD_FAST                7 (gated)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN
                LOAD_CONST              17 ('Wildcard CORS gated by environment')
                JUMP_FORWARD             1 (to L15)

 391   L14:     LOAD_CONST              18 ('Ungated wildcard CORS')

 392   L15:     LOAD_GLOBAL             19 (_rel + NULL)
                LOAD_FAST_LOAD_FAST      2 (repo_root, path)
                CALL                     2

 393            LOAD_FAST                4 (i)

 394            LOAD_FAST                7 (gated)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L16)
                NOT_TAKEN
                LOAD_CONST              19 ('Acceptable for dev only.')
                JUMP_FORWARD             1 (to L17)

 395   L16:     LOAD_CONST              20 ('Production exposure risk.')

 396   L17:     LOAD_CONST              21 ('cors')

 397            LOAD_FAST                7 (gated)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L18)
                NOT_TAKEN
                LOAD_CONST              22 ('None.')
                JUMP_FORWARD             1 (to L19)

 398   L18:     LOAD_CONST              23 ('Restrict allow_origins to the production hostnames.')

 387   L19:     LOAD_CONST              24 (('id', 'severity', 'title', 'file', 'line', 'detail', 'category', 'suggestion'))
                CALL_KW                  8
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          223 (to L5)

 379   L20:     END_FOR
                POP_ITER
                EXTENDED_ARG             1
                JUMP_BACKWARD          302 (to L1)

 370   L21:     END_FOR
                POP_ITER

 400            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L22:     PUSH_EXC_INFO

 373            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L24)
                NOT_TAKEN
                POP_TOP

 374   L23:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD          321 (to L1)

 373   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L22 [1]
  L22 to L23 -> L25 [2] lasti
  L24 to L25 -> L25 [2] lasti

Disassembly of <code object <genexpr> at 0x0000018C1802CC10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 383>:
 383           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 385   L2:     FOR_ITER                36 (to L8)
               STORE_FAST               1 (w)

 384           LOAD_CONST               0 ('ENVIRONMENT')
               LOAD_FAST_BORROW         1 (w)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        19 (to L7)
       L3:     NOT_TAKEN
       L4:     POP_TOP
               LOAD_CONST               1 ('development')
               LOAD_FAST_BORROW         1 (w)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L7)
       L5:     NOT_TAKEN
       L6:     POP_TOP
               LOAD_CONST               2 ('is_dev')
               LOAD_FAST_BORROW         1 (w)
               CONTAINS_OP              0 (in)
       L7:     YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           38 (to L2)

 385   L8:     END_FOR
               POP_ITER
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L9:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L9 [0] lasti
  L4 to L5 -> L9 [0] lasti
  L6 to L9 -> L9 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 403>:
403           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Finding]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_dangerous_todos at 0x0000018C17E88A00, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 403>:
  --            MAKE_CELL                9 (line_text)

 403            RESUME                   0

 406            BUILD_LIST               0
                STORE_FAST               1 (out)

 407            LOAD_GLOBAL              1 (_iter_source_files + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                GET_ITER
        L1:     EXTENDED_ARG             1
                FOR_ITER               365 (to L14)
                STORE_FAST               2 (path)

 408            LOAD_GLOBAL              3 (_rel + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (repo_root, path)
                CALL                     2
                STORE_FAST               3 (rel)

 409            LOAD_GLOBAL              5 (_is_self_file + NULL)
                LOAD_FAST_BORROW         3 (rel)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN

 410            JUMP_BACKWARD           34 (to L1)

 411    L2:     NOP

 412    L3:     LOAD_FAST_BORROW         2 (path)
                LOAD_ATTR                7 (read_text + NULL|self)
                LOAD_CONST               1 ('utf-8')
                LOAD_CONST               2 ('ignore')
                LOAD_CONST               3 (('encoding', 'errors'))
                CALL_KW                  2
                STORE_FAST               4 (text)

 415    L4:     LOAD_GLOBAL             10 (_TODO_RE)
                LOAD_ATTR               13 (finditer + NULL|self)
                LOAD_FAST                4 (text)
                CALL                     1
                GET_ITER
        L5:     EXTENDED_ARG             1
                FOR_ITER               285 (to L13)
                STORE_FAST               5 (m)

 416            LOAD_FAST                4 (text)
                LOAD_ATTR               15 (count + NULL|self)
                LOAD_CONST               4 ('\n')
                LOAD_SMALL_INT           0
                LOAD_FAST                5 (m)
                LOAD_ATTR               17 (start + NULL|self)
                CALL                     0
                CALL                     3
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                STORE_FAST               6 (line_no)

 418            LOAD_FAST                4 (text)
                LOAD_ATTR               19 (rfind + NULL|self)
                LOAD_CONST               4 ('\n')
                LOAD_SMALL_INT           0
                LOAD_FAST                5 (m)
                LOAD_ATTR               17 (start + NULL|self)
                CALL                     0
                CALL                     3
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                STORE_FAST               7 (line_start)

 419            LOAD_FAST                4 (text)
                LOAD_ATTR               21 (find + NULL|self)
                LOAD_CONST               4 ('\n')
                LOAD_FAST                5 (m)
                LOAD_ATTR               17 (start + NULL|self)
                CALL                     0
                CALL                     2
                STORE_FAST               8 (line_end)

 420            LOAD_FAST                8 (line_end)
                LOAD_SMALL_INT           0
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE       12 (to L6)
                NOT_TAKEN

 421            LOAD_GLOBAL             23 (len + NULL)
                LOAD_FAST                4 (text)
                CALL                     1
                STORE_FAST               8 (line_end)

 422    L6:     LOAD_FAST_LOAD_FAST     71 (text, line_start)
                LOAD_FAST                8 (line_end)
                BINARY_SLICE
                LOAD_ATTR               25 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              9 (line_text)

 423            LOAD_GLOBAL             26 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       35 (to L10)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST                9 (line_text)
                BUILD_TUPLE              1
                LOAD_CONST               5 (<code object <genexpr> at 0x0000018C18024F30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 423>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_GLOBAL             28 (_TODO_DANGER_TOKENS)
                GET_ITER
                CALL                     0
        L7:     FOR_ITER                12 (to L9)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L7)
        L8:     POP_ITER
                LOAD_CONST               6 (True)
                JUMP_FORWARD            24 (to L11)
        L9:     END_FOR
                POP_ITER
                LOAD_CONST               7 (False)
                JUMP_FORWARD            20 (to L11)
       L10:     PUSH_NULL
                LOAD_FAST                9 (line_text)
                BUILD_TUPLE              1
                LOAD_CONST               5 (<code object <genexpr> at 0x0000018C18024F30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 423>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_GLOBAL             28 (_TODO_DANGER_TOKENS)
                GET_ITER
                CALL                     0
                CALL                     1
       L11:     TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD          226 (to L5)

 424   L12:     LOAD_FAST                1 (out)
                LOAD_ATTR               31 (append + NULL|self)
                LOAD_GLOBAL             33 (Finding + NULL)

 425            LOAD_CONST               8 ('todo_')
                LOAD_FAST                3 (rel)
                FORMAT_SIMPLE
                LOAD_CONST               9 ('_')
                LOAD_FAST                6 (line_no)
                FORMAT_SIMPLE
                BUILD_STRING             4

 426            LOAD_CONST              10 ('MEDIUM')

 427            LOAD_CONST              11 ('TODO / FIXME mentioning sensitive concern')

 428            LOAD_FAST                3 (rel)

 429            LOAD_FAST                6 (line_no)

 430            LOAD_CONST              12 ("Marker '")
                LOAD_FAST                5 (m)
                LOAD_ATTR               35 (group + NULL|self)
                LOAD_SMALL_INT           0
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              13 ("' near sensitive token; review and resolve.")
                BUILD_STRING             3

 431            LOAD_CONST              14 ('tooling')

 432            LOAD_CONST              15 ('Resolve or downgrade the comment with a tracked ticket id.')

 424            LOAD_CONST              16 (('id', 'severity', 'title', 'file', 'line', 'detail', 'category', 'suggestion'))
                CALL_KW                  8
                CALL                     1
                POP_TOP
                EXTENDED_ARG             1
                JUMP_BACKWARD          288 (to L5)

 415   L13:     END_FOR
                POP_ITER
                EXTENDED_ARG             1
                JUMP_BACKWARD          368 (to L1)

 407   L14:     END_FOR
                POP_ITER

 434            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 413            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L17)
                NOT_TAKEN
                POP_TOP

 414   L16:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD          387 (to L1)

 413   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L15 [1]
  L15 to L16 -> L18 [2] lasti
  L17 to L18 -> L18 [2] lasti

Disassembly of <code object <genexpr> at 0x0000018C18024F30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 423>:
  --           COPY_FREE_VARS           1

 423           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (tok, tok)
               LOAD_DEREF               2 (line_text)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           11 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 446>:
446           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Finding]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_pii_logging at 0x0000018C181A1B70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 446>:
  --            MAKE_CELL               10 (args)
                MAKE_CELL               11 (args_lower)

 446            RESUME                   0

 455            BUILD_LIST               0
                STORE_FAST               1 (out)

 456            LOAD_GLOBAL              0 (re)
                LOAD_ATTR                2 (compile)
                PUSH_NULL

 457            LOAD_CONST               1 ('logger\\.(debug|info|warning|error|exception)\\s*\\(([^)]*)\\)')

 458            LOAD_GLOBAL              0 (re)
                LOAD_ATTR                4 (MULTILINE)

 456            CALL                     2
                STORE_FAST               2 (pattern)

 460            LOAD_FAST_BORROW         0 (repo_root)
                LOAD_CONST               2 ('app')
                BINARY_OP               11 (/)
                LOAD_ATTR                7 (rglob + NULL|self)
                LOAD_CONST               3 ('*.py')
                CALL                     1
                GET_ITER
        L1:     EXTENDED_ARG             1
                FOR_ITER               445 (to L32)
                STORE_FAST               3 (path)

 461            NOP

 462    L2:     LOAD_FAST_BORROW         3 (path)
                LOAD_ATTR                9 (read_text + NULL|self)
                LOAD_CONST               4 ('utf-8')
                LOAD_CONST               5 ('ignore')
                LOAD_CONST               6 (('encoding', 'errors'))
                CALL_KW                  2
                STORE_FAST               4 (text)

 465    L3:     LOAD_FAST                2 (pattern)
                LOAD_ATTR               13 (finditer + NULL|self)
                LOAD_FAST                4 (text)
                CALL                     1
                GET_ITER
        L4:     EXTENDED_ARG             1
                FOR_ITER               399 (to L31)
                STORE_FAST               5 (m)

 466            LOAD_FAST                5 (m)
                LOAD_ATTR               15 (group + NULL|self)
                LOAD_SMALL_INT           2
                CALL                     1
                STORE_DEREF             10 (args)

 467            LOAD_DEREF              10 (args)
                LOAD_ATTR               17 (lower + NULL|self)
                CALL                     0
                STORE_DEREF             11 (args_lower)

 468            LOAD_GLOBAL             18 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       35 (to L8)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST               11 (args_lower)
                BUILD_TUPLE              1
                LOAD_CONST               7 (<code object <genexpr> at 0x0000018C18024B30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 468>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_GLOBAL             20 (_PII_TOKENS_IN_LOG)
                GET_ITER
                CALL                     0
        L5:     FOR_ITER                12 (to L7)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)
        L6:     POP_ITER
                LOAD_CONST               8 (True)
                JUMP_FORWARD            24 (to L9)
        L7:     END_FOR
                POP_ITER
                LOAD_CONST               9 (False)
                JUMP_FORWARD            20 (to L9)
        L8:     PUSH_NULL
                LOAD_FAST               11 (args_lower)
                BUILD_TUPLE              1
                LOAD_CONST               7 (<code object <genexpr> at 0x0000018C18024B30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 468>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_GLOBAL             20 (_PII_TOKENS_IN_LOG)
                GET_ITER
                CALL                     0
                CALL                     1
        L9:     TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN

 469            JUMP_BACKWARD          111 (to L4)

 471   L10:     LOAD_GLOBAL             18 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       35 (to L14)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST               10 (args)
                BUILD_TUPLE              1
                LOAD_CONST              10 (<code object <genexpr> at 0x0000018C18025030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 471>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_GLOBAL             22 (_REDACTION_HELPER_TOKENS)
                GET_ITER
                CALL                     0
       L11:     FOR_ITER                12 (to L13)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L11)
       L12:     POP_ITER
                LOAD_CONST               8 (True)
                JUMP_FORWARD            24 (to L15)
       L13:     END_FOR
                POP_ITER
                LOAD_CONST               9 (False)
                JUMP_FORWARD            20 (to L15)
       L14:     PUSH_NULL
                LOAD_FAST               10 (args)
                BUILD_TUPLE              1
                LOAD_CONST              10 (<code object <genexpr> at 0x0000018C18025030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 471>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_GLOBAL             22 (_REDACTION_HELPER_TOKENS)
                GET_ITER
                CALL                     0
                CALL                     1
       L15:     TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L16)
                NOT_TAKEN

 472            JUMP_BACKWARD          185 (to L4)

 475   L16:     LOAD_CONST              11 ('len(')
                LOAD_DEREF              10 (args)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       68 (to L22)
                NOT_TAKEN
                LOAD_GLOBAL             18 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L20)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST               10 (args)
                BUILD_TUPLE              1
                LOAD_CONST              12 (<code object <genexpr> at 0x0000018C18024930, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 475>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 476            LOAD_CONST              25 (('{transcript}', '{transcript!r}', '{response_text}', '{response_text!r}', '{payload}', '{payload!r}', '{lead_data}', '{lead_data!r}'))
                GET_ITER

 475            CALL                     0
       L17:     FOR_ITER                12 (to L19)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L17)
       L18:     POP_ITER
                LOAD_CONST               8 (True)
                JUMP_FORWARD            20 (to L21)
       L19:     END_FOR
                POP_ITER
                LOAD_CONST               9 (False)
                JUMP_FORWARD            16 (to L21)
       L20:     PUSH_NULL
                LOAD_FAST               10 (args)
                BUILD_TUPLE              1
                LOAD_CONST              12 (<code object <genexpr> at 0x0000018C18024930, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 475>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 476            LOAD_CONST              25 (('{transcript}', '{transcript!r}', '{response_text}', '{response_text!r}', '{payload}', '{payload!r}', '{lead_data}', '{lead_data!r}'))
                GET_ITER

 475            CALL                     0
                CALL                     1
       L21:     TO_BOOL
                POP_JUMP_IF_TRUE         4 (to L22)
                NOT_TAKEN

 481            EXTENDED_ARG             1
                JUMP_BACKWARD          259 (to L4)

 482   L22:     LOAD_FAST                4 (text)
                LOAD_ATTR               25 (count + NULL|self)
                LOAD_CONST              13 ('\n')
                LOAD_SMALL_INT           0
                LOAD_FAST                5 (m)
                LOAD_ATTR               27 (start + NULL|self)
                CALL                     0
                CALL                     3
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                STORE_FAST               6 (line_no)

 483            LOAD_GLOBAL             29 (_rel + NULL)
                LOAD_FAST_LOAD_FAST      3 (repo_root, path)
                CALL                     2
                STORE_FAST               7 (rel)

 486            LOAD_CONST              14 ('transcript')
                LOAD_DEREF              11 (args_lower)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       10 (to L23)
                NOT_TAKEN
                LOAD_CONST              15 ('websocket')
                LOAD_FAST                7 (rel)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L23)
                NOT_TAKEN
                LOAD_CONST              16 ('HIGH')
                JUMP_FORWARD             1 (to L24)
       L23:     LOAD_CONST              17 ('MEDIUM')
       L24:     STORE_FAST               8 (sev)

 487            LOAD_FAST                1 (out)
                LOAD_ATTR               31 (append + NULL|self)
                LOAD_GLOBAL             33 (Finding + NULL)

 488            LOAD_CONST              18 ('pii_log_')
                LOAD_FAST                7 (rel)
                FORMAT_SIMPLE
                LOAD_CONST              19 ('_')
                LOAD_FAST                6 (line_no)
                FORMAT_SIMPLE
                BUILD_STRING             4

 489            LOAD_FAST                8 (sev)

 490            LOAD_CONST              20 ('Logger may emit PII / payload')

 491            LOAD_FAST                7 (rel)

 492            LOAD_FAST                6 (line_no)

 493            LOAD_CONST              21 ('Token(s) detected in log args: ')

 494            LOAD_GLOBAL             20 (_PII_TOKENS_IN_LOG)
                GET_ITER
                LOAD_FAST_AND_CLEAR      9 (t)
                SWAP                     2
       L25:     BUILD_LIST               0
                SWAP                     2
       L26:     FOR_ITER                13 (to L29)
                STORE_FAST_LOAD_FAST   153 (t, t)
                LOAD_DEREF              11 (args_lower)
                CONTAINS_OP              0 (in)
       L27:     POP_JUMP_IF_TRUE         3 (to L28)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L26)
       L28:     LOAD_FAST                9 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L26)
       L29:     END_FOR
                POP_ITER
       L30:     SWAP                     2
                STORE_FAST               9 (t)
                FORMAT_SIMPLE

 493            BUILD_STRING             2

 495            LOAD_CONST              22 ('logging')

 496            LOAD_CONST              23 ('Truncate, redact, or downgrade to debug.')

 487            LOAD_CONST              24 (('id', 'severity', 'title', 'file', 'line', 'detail', 'category', 'suggestion'))
                CALL_KW                  8
                CALL                     1
                POP_TOP
                EXTENDED_ARG             1
                JUMP_BACKWARD          402 (to L4)

 465   L31:     END_FOR
                POP_ITER
                EXTENDED_ARG             1
                JUMP_BACKWARD          448 (to L1)

 460   L32:     END_FOR
                POP_ITER

 498            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L33:     PUSH_EXC_INFO

 463            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L35)
                NOT_TAKEN
                POP_TOP

 464   L34:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD          467 (to L1)

 463   L35:     RERAISE                  0

  --   L36:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L37:     SWAP                     2
                POP_TOP

 494            SWAP                     2
                STORE_FAST               9 (t)
                RERAISE                  0
ExceptionTable:
  L2 to L3 -> L33 [1]
  L25 to L27 -> L37 [14]
  L28 to L30 -> L37 [14]
  L33 to L34 -> L36 [2] lasti
  L35 to L36 -> L36 [2] lasti

Disassembly of <code object <genexpr> at 0x0000018C18024B30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 468>:
  --           COPY_FREE_VARS           1

 468           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (tok, tok)
               LOAD_DEREF               2 (args_lower)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           11 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18025030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 471>:
  --           COPY_FREE_VARS           1

 471           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (t, t)
               LOAD_DEREF               2 (args)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           11 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18024930, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 475>:
  --           COPY_FREE_VARS           1

 475           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 476   L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (bare, bare)
               LOAD_DEREF               2 (args)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           11 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 501>:
501           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('node')
              LOAD_CONST               2 ('ast.FunctionDef')
              LOAD_CONST               3 ('name')
              LOAD_CONST               4 ('str')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('bool')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _function_body_calls at 0x0000018C17ECF000, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 501>:
501           RESUME                   0

503           LOAD_GLOBAL              0 (ast)
              LOAD_ATTR                2 (walk)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (node)
              CALL                     1
              GET_ITER
      L1:     FOR_ITER               155 (to L6)
              STORE_FAST               2 (child)

504           LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (child)
              LOAD_GLOBAL              0 (ast)
              LOAD_ATTR                6 (Call)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

505           JUMP_BACKWARD           37 (to L1)

506   L2:     LOAD_FAST_BORROW         2 (child)
              LOAD_ATTR                8 (func)
              STORE_FAST               3 (f)

507           LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (f)
              LOAD_GLOBAL              0 (ast)
              LOAD_ATTR               10 (Name)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         3 (f)
              LOAD_ATTR               12 (id)
              LOAD_FAST_BORROW         1 (name)
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        4 (to L3)
              NOT_TAKEN

508           POP_TOP
              LOAD_CONST               1 (True)
              RETURN_VALUE

509   L3:     LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (f)
              LOAD_GLOBAL              0 (ast)
              LOAD_ATTR               14 (Attribute)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD          135 (to L1)
      L4:     LOAD_FAST_BORROW         3 (f)
              LOAD_ATTR               16 (attr)
              LOAD_FAST_BORROW         1 (name)
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD          154 (to L1)

510   L5:     POP_TOP
              LOAD_CONST               1 (True)
              RETURN_VALUE

503   L6:     END_FOR
              POP_ITER

511           LOAD_CONST               2 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 514>:
514           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Finding]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_optional_brokerage_id at 0x0000018C17F78C70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 514>:
 514            RESUME                   0

 522            BUILD_LIST               0
                STORE_FAST               1 (out)

 524            LOAD_FAST_BORROW         0 (repo_root)
                LOAD_CONST               1 ('app')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('services')
                BINARY_OP               11 (/)
                LOAD_CONST               3 ('intelligence')
                BINARY_OP               11 (/)
                LOAD_CONST               4 ('queries.py')
                BINARY_OP               11 (/)

 525            LOAD_FAST_BORROW         0 (repo_root)
                LOAD_CONST               1 ('app')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('services')
                BINARY_OP               11 (/)
                LOAD_CONST               5 ('workflows')
                BINARY_OP               11 (/)
                LOAD_CONST               4 ('queries.py')
                BINARY_OP               11 (/)

 526            LOAD_FAST_BORROW         0 (repo_root)
                LOAD_CONST               1 ('app')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('services')
                BINARY_OP               11 (/)
                LOAD_CONST               6 ('replay')
                BINARY_OP               11 (/)
                LOAD_CONST               7 ('event_reader.py')
                BINARY_OP               11 (/)

 523            BUILD_TUPLE              3
                STORE_FAST               2 (targets)

 528            LOAD_FAST_BORROW         2 (targets)
                GET_ITER
        L1:     EXTENDED_ARG             3
                FOR_ITER               790 (to L23)
                STORE_FAST               3 (path)

 529            LOAD_FAST_BORROW         3 (path)
                LOAD_ATTR                1 (exists + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN

 530            JUMP_BACKWARD           28 (to L1)

 531    L2:     LOAD_GLOBAL              3 (_ast_walk + NULL)
                LOAD_FAST_BORROW         3 (path)
                CALL                     1
                STORE_FAST               4 (tree)

 532            LOAD_FAST_BORROW         4 (tree)
                POP_JUMP_IF_NOT_NONE     3 (to L3)
                NOT_TAKEN

 533            JUMP_BACKWARD           45 (to L1)

 534    L3:     LOAD_GLOBAL              4 (ast)
                LOAD_ATTR                6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         4 (tree)
                CALL                     1
                GET_ITER
        L4:     EXTENDED_ARG             2
                FOR_ITER               718 (to L22)
                STORE_FAST               5 (node)

 535            LOAD_GLOBAL              9 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (node)
                LOAD_GLOBAL              4 (ast)
                LOAD_ATTR               10 (FunctionDef)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN

 536            JUMP_BACKWARD           38 (to L4)

 537    L5:     LOAD_FAST_BORROW         5 (node)
                LOAD_ATTR               12 (name)
                LOAD_ATTR               15 (startswith + NULL|self)
                LOAD_CONST               9 ('_')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN

 538            JUMP_BACKWARD           73 (to L4)

 541    L6:     LOAD_FAST_BORROW         5 (node)
                LOAD_ATTR               12 (name)
                LOAD_ATTR               17 (endswith + NULL|self)
                LOAD_CONST              10 ('_unscoped')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN

 542            JUMP_BACKWARD          108 (to L4)

 547    L7:     LOAD_GLOBAL             19 (_function_body_calls + NULL)
                LOAD_FAST_BORROW         5 (node)
                LOAD_CONST              11 ('require_tenant_or_unscoped')
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN

 548            JUMP_BACKWARD          128 (to L4)

 549    L8:     LOAD_FAST_BORROW         5 (node)
                LOAD_ATTR               20 (args)
                STORE_FAST               6 (args)

 550            LOAD_GLOBAL             23 (list + NULL)
                LOAD_FAST_BORROW         6 (args)
                LOAD_ATTR               20 (args)
                CALL                     1
                LOAD_GLOBAL             23 (list + NULL)
                LOAD_FAST_BORROW         6 (args)
                LOAD_ATTR               24 (kwonlyargs)
                CALL                     1
                BINARY_OP                0 (+)
                STORE_FAST               7 (all_args)

 551            LOAD_GLOBAL             27 (enumerate + NULL)
                LOAD_FAST_BORROW         7 (all_args)
                CALL                     1
                GET_ITER
        L9:     EXTENDED_ARG             2
                FOR_ITER               515 (to L21)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  137 (i, a)

 552            LOAD_FAST_BORROW         9 (a)
                LOAD_ATTR               28 (arg)
                LOAD_CONST              12 ('brokerage_id')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN

 553            JUMP_BACKWARD           25 (to L9)

 555   L10:     LOAD_CONST              13 (False)
                STORE_FAST              10 (has_default)

 556            LOAD_CONST              13 (False)
                STORE_FAST              11 (default_is_none)

 557            LOAD_FAST_BORROW_LOAD_FAST_BORROW 150 (a, args)
                LOAD_ATTR               24 (kwonlyargs)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE      193 (to L15)
                NOT_TAKEN

 558            LOAD_FAST_BORROW         6 (args)
                LOAD_ATTR               24 (kwonlyargs)
                LOAD_ATTR               31 (index + NULL|self)
                LOAD_FAST_BORROW         9 (a)
                CALL                     1
                STORE_FAST              12 (idx)

 559            LOAD_FAST_BORROW        12 (idx)
                LOAD_GLOBAL             33 (len + NULL)
                LOAD_FAST_BORROW         6 (args)
                LOAD_ATTR               34 (kw_defaults)
                CALL                     1
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE       20 (to L11)
                NOT_TAKEN
                LOAD_FAST_BORROW         6 (args)
                LOAD_ATTR               34 (kw_defaults)
                LOAD_FAST_BORROW        12 (idx)
                BINARY_OP               26 ([])
                JUMP_FORWARD             1 (to L12)
       L11:     LOAD_CONST               8 (None)
       L12:     STORE_FAST              13 (d)

 560            LOAD_FAST_BORROW        13 (d)
                LOAD_CONST               8 (None)
                IS_OP                    1 (is not)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        54 (to L13)
                NOT_TAKEN
                POP_TOP

 561            LOAD_FAST_BORROW        12 (idx)
                LOAD_GLOBAL             33 (len + NULL)
                LOAD_FAST_BORROW         6 (args)
                LOAD_ATTR               34 (kw_defaults)
                CALL                     1
                COMPARE_OP               2 (<)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       22 (to L13)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         6 (args)
                LOAD_ATTR               34 (kw_defaults)
                LOAD_FAST_BORROW        12 (idx)
                BINARY_OP               26 ([])
                LOAD_CONST               8 (None)
                IS_OP                    0 (is)

 560   L13:     STORE_FAST              10 (has_default)

 563            LOAD_FAST_BORROW        13 (d)
                POP_JUMP_IF_NONE        49 (to L14)
                NOT_TAKEN
                LOAD_GLOBAL              9 (isinstance + NULL)
                LOAD_FAST_BORROW        13 (d)
                LOAD_GLOBAL              4 (ast)
                LOAD_ATTR               36 (Constant)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L14)
                NOT_TAKEN
                LOAD_FAST_BORROW        13 (d)
                LOAD_ATTR               38 (value)
                POP_JUMP_IF_NOT_NONE     3 (to L14)
                NOT_TAKEN

 564            LOAD_CONST              14 (True)
                STORE_FAST              11 (default_is_none)

  --   L14:     JUMP_FORWARD           171 (to L18)

 566   L15:     LOAD_GLOBAL             33 (len + NULL)
                LOAD_FAST_BORROW         6 (args)
                LOAD_ATTR               20 (args)
                CALL                     1
                STORE_FAST              14 (pos_count)

 567            LOAD_FAST_BORROW         6 (args)
                LOAD_ATTR               40 (defaults)
                STORE_FAST              15 (defaults)

 568            LOAD_FAST_BORROW         6 (args)
                LOAD_ATTR               20 (args)
                LOAD_ATTR               31 (index + NULL|self)
                LOAD_FAST_BORROW         9 (a)
                CALL                     1
                STORE_FAST              16 (pos_idx)

 569            LOAD_FAST_BORROW        16 (pos_idx)
                LOAD_FAST_BORROW        14 (pos_count)
                LOAD_GLOBAL             33 (len + NULL)
                LOAD_FAST_BORROW        15 (defaults)
                CALL                     1
                BINARY_OP               10 (-)
                BINARY_OP               10 (-)
                STORE_FAST              17 (default_idx)

 570            LOAD_SMALL_INT           0
                LOAD_FAST               17 (default_idx)
                SWAP                     2
                COPY                     2
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE       17 (to L16)
                NOT_TAKEN
                LOAD_GLOBAL             33 (len + NULL)
                LOAD_FAST_BORROW        15 (defaults)
                CALL                     1
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE       63 (to L18)
                NOT_TAKEN
                JUMP_FORWARD             2 (to L17)
       L16:     POP_TOP
                JUMP_FORWARD            59 (to L18)

 571   L17:     LOAD_CONST              14 (True)
                STORE_FAST              10 (has_default)

 572            LOAD_FAST_BORROW        15 (defaults)
                LOAD_FAST_BORROW        17 (default_idx)
                BINARY_OP               26 ([])
                STORE_FAST              13 (d)

 573            LOAD_GLOBAL              9 (isinstance + NULL)
                LOAD_FAST_BORROW        13 (d)
                LOAD_GLOBAL              4 (ast)
                LOAD_ATTR               36 (Constant)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L18)
                NOT_TAKEN
                LOAD_FAST_BORROW        13 (d)
                LOAD_ATTR               38 (value)
                POP_JUMP_IF_NOT_NONE     3 (to L18)
                NOT_TAKEN

 574            LOAD_CONST              14 (True)
                STORE_FAST              11 (default_is_none)

 575   L18:     LOAD_FAST_BORROW        10 (has_default)
                TO_BOOL
                POP_JUMP_IF_TRUE         4 (to L19)
                NOT_TAKEN
                EXTENDED_ARG             1
                JUMP_BACKWARD          419 (to L9)
       L19:     LOAD_FAST_BORROW        11 (default_is_none)
                TO_BOOL
                POP_JUMP_IF_TRUE         4 (to L20)
                NOT_TAKEN
                EXTENDED_ARG             1
                JUMP_BACKWARD          430 (to L9)

 576   L20:     LOAD_GLOBAL             43 (_rel + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 3 (repo_root, path)
                CALL                     2
                STORE_FAST              18 (rel)

 577            LOAD_FAST_BORROW         1 (out)
                LOAD_ATTR               45 (append + NULL|self)
                LOAD_GLOBAL             47 (Finding + NULL)

 578            LOAD_CONST              15 ('tenant_optional_')
                LOAD_FAST_BORROW        18 (rel)
                FORMAT_SIMPLE
                LOAD_CONST               9 ('_')
                LOAD_FAST_BORROW         5 (node)
                LOAD_ATTR               12 (name)
                FORMAT_SIMPLE
                BUILD_STRING             4

 579            LOAD_CONST              16 ('HIGH')

 580            LOAD_CONST              17 ('`')
                LOAD_FAST_BORROW         5 (node)
                LOAD_ATTR               12 (name)
                FORMAT_SIMPLE
                LOAD_CONST              18 ('()` accepts brokerage_id=None')
                BUILD_STRING             3

 581            LOAD_FAST_BORROW        18 (rel)

 582            LOAD_FAST_BORROW         5 (node)
                LOAD_ATTR               48 (lineno)

 583            LOAD_CONST              19 ('Tenant filter is OPTIONAL — caller-side mistake could return cross-tenant rows.')

 585            LOAD_CONST              20 ('tenant_isolation')

 586            LOAD_CONST              21 ('Make brokerage_id required, or add an admin kwarg + assert when None is allowed.')

 577            LOAD_CONST              22 (('id', 'severity', 'title', 'file', 'line', 'detail', 'category', 'suggestion'))
                CALL_KW                  8
                CALL                     1
                POP_TOP
                EXTENDED_ARG             2
                JUMP_BACKWARD          518 (to L9)

 551   L21:     END_FOR
                POP_ITER
                EXTENDED_ARG             2
                JUMP_BACKWARD          721 (to L4)

 534   L22:     END_FOR
                POP_ITER
                EXTENDED_ARG             3
                JUMP_BACKWARD          793 (to L1)

 528   L23:     END_FOR
                POP_ITER

 589            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 592>:
592           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Finding]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_full_payload_print_or_log at 0x0000018C17CD4970, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 592>:
 592            RESUME                   0

 595            BUILD_LIST               0
                STORE_FAST               1 (out)

 596            LOAD_GLOBAL              0 (re)
                LOAD_ATTR                2 (compile)
                PUSH_NULL

 597            LOAD_CONST               1 ('(logger\\.\\w+|print)\\s*\\(\\s*(payload|row|metadata|transcript|lead_data)\\s*\\)')

 598            LOAD_GLOBAL              0 (re)
                LOAD_ATTR                4 (MULTILINE)

 596            CALL                     2
                STORE_FAST               2 (pattern)

 600            LOAD_FAST_BORROW         0 (repo_root)
                LOAD_CONST               2 ('app')
                BINARY_OP               11 (/)
                LOAD_ATTR                7 (rglob + NULL|self)
                LOAD_CONST               3 ('*.py')
                CALL                     1
                GET_ITER
        L1:     FOR_ITER               164 (to L6)
                STORE_FAST               3 (path)

 601            NOP

 602    L2:     LOAD_FAST_BORROW         3 (path)
                LOAD_ATTR                9 (read_text + NULL|self)
                LOAD_CONST               4 ('utf-8')
                LOAD_CONST               5 ('ignore')
                LOAD_CONST               6 (('encoding', 'errors'))
                CALL_KW                  2
                STORE_FAST               4 (text)

 605    L3:     LOAD_FAST                2 (pattern)
                LOAD_ATTR               13 (finditer + NULL|self)
                LOAD_FAST                4 (text)
                CALL                     1
                GET_ITER
        L4:     FOR_ITER               120 (to L5)
                STORE_FAST               5 (m)

 606            LOAD_FAST                4 (text)
                LOAD_ATTR               15 (count + NULL|self)
                LOAD_CONST               7 ('\n')
                LOAD_SMALL_INT           0
                LOAD_FAST                5 (m)
                LOAD_ATTR               17 (start + NULL|self)
                CALL                     0
                CALL                     3
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                STORE_FAST               6 (line_no)

 607            LOAD_FAST                1 (out)
                LOAD_ATTR               19 (append + NULL|self)
                LOAD_GLOBAL             21 (Finding + NULL)

 608            LOAD_CONST               8 ('full_payload_log_')
                LOAD_GLOBAL             23 (_rel + NULL)
                LOAD_FAST_LOAD_FAST      3 (repo_root, path)
                CALL                     2
                FORMAT_SIMPLE
                LOAD_CONST               9 ('_')
                LOAD_FAST                6 (line_no)
                FORMAT_SIMPLE
                BUILD_STRING             4

 609            LOAD_CONST              10 ('HIGH')

 610            LOAD_CONST              11 ('Full payload-shaped object logged or printed')

 611            LOAD_GLOBAL             23 (_rel + NULL)
                LOAD_FAST_LOAD_FAST      3 (repo_root, path)
                CALL                     2

 612            LOAD_FAST                6 (line_no)

 613            LOAD_CONST              12 ('Argument: ')
                LOAD_FAST                5 (m)
                LOAD_ATTR               25 (group + NULL|self)
                LOAD_SMALL_INT           2
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              13 (' — likely contains nested PII.')
                BUILD_STRING             3

 614            LOAD_CONST              14 ('logging')

 615            LOAD_CONST              15 ('Log a small summary (id + length) or redact before printing.')

 607            LOAD_CONST              16 (('id', 'severity', 'title', 'file', 'line', 'detail', 'category', 'suggestion'))
                CALL_KW                  8
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          122 (to L4)

 605    L5:     END_FOR
                POP_ITER
                JUMP_BACKWARD          166 (to L1)

 600    L6:     END_FOR
                POP_ITER

 617            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 603            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

 604    L8:     POP_EXCEPT
                JUMP_BACKWARD          184 (to L1)

 603    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L7 [1]
  L7 to L8 -> L10 [2] lasti
  L9 to L10 -> L10 [2] lasti

Disassembly of <code object AuditReport at 0x0000018C180396B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 624>:
624           RESUME                   0
              LOAD_NAME                0 (__name__)
              STORE_NAME               1 (__module__)
              LOAD_CONST               0 ('AuditReport')
              STORE_NAME               2 (__qualname__)
              LOAD_CONST               1 (624)
              STORE_NAME               3 (__firstlineno__)
              SETUP_ANNOTATIONS

626           LOAD_CONST               2 ('str')
              LOAD_NAME                4 (__annotations__)
              LOAD_CONST               3 ('repo_root')
              STORE_SUBSCR

627           LOAD_CONST               2 ('str')
              LOAD_NAME                4 (__annotations__)
              LOAD_CONST               4 ('generated_at')
              STORE_SUBSCR

628           LOAD_NAME                5 (field)
              PUSH_NULL
              LOAD_NAME                6 (list)
              LOAD_CONST               5 (('default_factory',))
              CALL_KW                  1
              STORE_NAME               7 (findings)
              LOAD_CONST               6 ('List[Finding]')
              LOAD_NAME                4 (__annotations__)
              LOAD_CONST               7 ('findings')
              STORE_SUBSCR

630           LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA2790, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 630>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object by_severity at 0x0000018C180606F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 630>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME               8 (by_severity)

636           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA22E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 636>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object counts at 0x0000018C17FE1530, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 636>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME               9 (counts)

639           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA24C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 639>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object to_dict at 0x0000018C1800AF10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 639>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              10 (to_dict)
              LOAD_CONST              14 (())
              STORE_NAME              11 (__static_attributes__)
              LOAD_CONST              15 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2790, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 630>:
630           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('dict')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object by_severity at 0x0000018C180606F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 630>:
 630           RESUME                   0

 631           LOAD_GLOBAL              0 (SEVERITIES)
               GET_ITER
               LOAD_FAST_AND_CLEAR      1 (s)
               SWAP                     2
       L1:     BUILD_MAP                0
               SWAP                     2
       L2:     FOR_ITER                 5 (to L3)
               STORE_FAST_LOAD_FAST    17 (s, s)
               BUILD_LIST               0
               MAP_ADD                  2
               JUMP_BACKWARD            7 (to L2)
       L3:     END_FOR
               POP_ITER
       L4:     STORE_FAST               2 (out)
               STORE_FAST               1 (s)

 632           LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                2 (findings)
               GET_ITER
       L5:     FOR_ITER                60 (to L6)
               STORE_FAST               3 (f)

 633           LOAD_FAST_BORROW         2 (out)
               LOAD_ATTR                5 (setdefault + NULL|self)
               LOAD_FAST_BORROW         3 (f)
               LOAD_ATTR                6 (severity)
               BUILD_LIST               0
               CALL                     2
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_FAST_BORROW         3 (f)
               LOAD_ATTR               11 (to_dict + NULL|self)
               CALL                     0
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           62 (to L5)

 632   L6:     END_FOR
               POP_ITER

 634           LOAD_FAST_BORROW         2 (out)
               RETURN_VALUE

  --   L7:     SWAP                     2
               POP_TOP

 631           SWAP                     2
               STORE_FAST               1 (s)
               RERAISE                  0
ExceptionTable:
  L1 to L4 -> L7 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 636>:
636           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('dict')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object counts at 0x0000018C17FE1530, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 636>:
  --           MAKE_CELL                1 (s)

 636           RESUME                   0

 637           LOAD_GLOBAL              0 (SEVERITIES)
               GET_ITER
               LOAD_FAST_AND_CLEAR      1 (s)
               MAKE_CELL                1 (s)
               SWAP                     2
       L1:     BUILD_MAP                0
               SWAP                     2
       L2:     FOR_ITER                35 (to L3)
               STORE_DEREF              1 (s)
               LOAD_DEREF               1 (s)
               LOAD_GLOBAL              3 (sum + NULL)
               LOAD_FAST_BORROW         1 (s)
               BUILD_TUPLE              1
               LOAD_CONST               0 (<code object <genexpr> at 0x0000018C180533F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 637>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                4 (findings)
               GET_ITER
               CALL                     0
               CALL                     1
               MAP_ADD                  2
               JUMP_BACKWARD           37 (to L2)
       L3:     END_FOR
               POP_ITER
       L4:     SWAP                     2
               STORE_FAST               1 (s)
               RETURN_VALUE

  --   L5:     SWAP                     2
               POP_TOP

 637           SWAP                     2
               STORE_FAST               1 (s)
               RERAISE                  0
ExceptionTable:
  L1 to L4 -> L5 [2]

Disassembly of <code object <genexpr> at 0x0000018C180533F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 637>:
  --           COPY_FREE_VARS           1

 637           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                25 (to L5)
               STORE_FAST_LOAD_FAST    17 (f, f)
               LOAD_ATTR                0 (severity)
               LOAD_DEREF               2 (s)
               COMPARE_OP              88 (bool(==))
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           21 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           27 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 639>:
639           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('dict')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object to_dict at 0x0000018C1800AF10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 639>:
 639           RESUME                   0

 641           LOAD_CONST               0 ('tool')
               LOAD_CONST               1 ('pas143e.security_audit')

 642           LOAD_CONST               2 ('repo_root')
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                0 (repo_root)

 643           LOAD_CONST               3 ('generated_at')
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                2 (generated_at)

 644           LOAD_CONST               4 ('counts')
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                5 (counts + NULL|self)
               CALL                     0

 645           LOAD_CONST               5 ('findings')
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                6 (findings)
               GET_ITER
               LOAD_FAST_AND_CLEAR      1 (f)
               SWAP                     2
       L1:     BUILD_LIST               0
               SWAP                     2
       L2:     FOR_ITER                18 (to L3)
               STORE_FAST_LOAD_FAST    17 (f, f)
               LOAD_ATTR                9 (to_dict + NULL|self)
               CALL                     0
               LIST_APPEND              2
               JUMP_BACKWARD           20 (to L2)
       L3:     END_FOR
               POP_ITER
       L4:     SWAP                     2
               STORE_FAST               1 (f)

 640           BUILD_MAP                5
               RETURN_VALUE

  --   L5:     SWAP                     2
               POP_TOP

 645           SWAP                     2
               STORE_FAST               1 (f)
               RERAISE                  0
ExceptionTable:
  L1 to L4 -> L5 [11]

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 649>:
649           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('AuditReport')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object run_audit at 0x0000018C17D789F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 649>:
649           RESUME                   0

650           BUILD_LIST               0
              STORE_FAST               1 (findings)

651           LOAD_FAST_BORROW         1 (findings)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_literal_secrets + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

652           LOAD_FAST_BORROW         1 (findings)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_committed_backup_artifacts + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

653           LOAD_FAST_BORROW         1 (findings)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_print_statements + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

654           LOAD_FAST_BORROW         1 (findings)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_silent_broad_except + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

655           LOAD_FAST_BORROW         1 (findings)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_wildcard_cors + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

656           LOAD_FAST_BORROW         1 (findings)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_dangerous_todos + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

657           LOAD_FAST_BORROW         1 (findings)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_pii_logging + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

658           LOAD_FAST_BORROW         1 (findings)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_optional_brokerage_id + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

659           LOAD_FAST_BORROW         1 (findings)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_full_payload_print_or_log + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

660           LOAD_FAST_BORROW         1 (findings)
              LOAD_ATTR               21 (sort + NULL|self)
              LOAD_CONST               0 (<code object <lambda> at 0x0000018C1802C620, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 660>)
              MAKE_FUNCTION
              LOAD_CONST               1 (('key',))
              CALL_KW                  1
              POP_TOP

661           LOAD_GLOBAL             23 (AuditReport + NULL)

662           LOAD_GLOBAL             25 (str + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1

663           LOAD_GLOBAL             26 (datetime)
              LOAD_ATTR               28 (now)
              PUSH_NULL
              LOAD_GLOBAL             30 (timezone)
              LOAD_ATTR               32 (utc)
              CALL                     1
              LOAD_ATTR               35 (isoformat + NULL|self)
              CALL                     0

664           LOAD_FAST_BORROW         1 (findings)

661           LOAD_CONST               2 (('repo_root', 'generated_at', 'findings'))
              CALL_KW                  3
              RETURN_VALUE

Disassembly of <code object <lambda> at 0x0000018C1802C620, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 660>:
660           RESUME                   0
              LOAD_GLOBAL              0 (_SEVERITY_RANK)
              LOAD_FAST_BORROW         0 (f)
              LOAD_ATTR                2 (severity)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW         0 (f)
              LOAD_ATTR                4 (file)
              LOAD_FAST_BORROW         0 (f)
              LOAD_ATTR                6 (line)
              BUILD_TUPLE              3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 672>:
672           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('AuditReport')
              LOAD_CONST               3 ('summary_only')
              LOAD_CONST               4 ('bool')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('None')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _print_human at 0x0000018C17D7D500, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 672>:
672            RESUME                   0

673            LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                1 (counts + NULL|self)
               CALL                     0
               STORE_FAST               2 (counts)

674            LOAD_GLOBAL              3 (print + NULL)
               LOAD_CONST              12 ('========================================================================')
               CALL                     1
               POP_TOP

675            LOAD_GLOBAL              3 (print + NULL)
               LOAD_CONST               1 ('PAS143E — SECURITY & INTEGRITY AUDIT')
               CALL                     1
               POP_TOP

676            LOAD_GLOBAL              3 (print + NULL)
               LOAD_CONST              13 ('------------------------------------------------------------------------')
               CALL                     1
               POP_TOP

677            LOAD_GLOBAL              4 (SEVERITIES)
               GET_ITER
       L1:     FOR_ITER                37 (to L2)
               STORE_FAST               3 (sev)

678            LOAD_GLOBAL              3 (print + NULL)
               LOAD_CONST               2 ('  ')
               LOAD_FAST_BORROW         3 (sev)
               LOAD_CONST               3 ('<8')
               FORMAT_WITH_SPEC
               LOAD_CONST               2 ('  ')
               LOAD_FAST_BORROW         2 (counts)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_FAST_BORROW         3 (sev)
               LOAD_SMALL_INT           0
               CALL                     2
               FORMAT_SIMPLE
               BUILD_STRING             4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           39 (to L1)

677    L2:     END_FOR
               POP_ITER

679            LOAD_GLOBAL              3 (print + NULL)
               LOAD_CONST              13 ('------------------------------------------------------------------------')
               CALL                     1
               POP_TOP

681            LOAD_FAST_BORROW         1 (summary_only)
               TO_BOOL
               POP_JUMP_IF_FALSE       14 (to L3)
               NOT_TAKEN

682            LOAD_GLOBAL              3 (print + NULL)
               LOAD_CONST              12 ('========================================================================')
               CALL                     1
               POP_TOP

683            LOAD_CONST               4 (None)
               RETURN_VALUE

685    L3:     LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                8 (findings)
               TO_BOOL
               POP_JUMP_IF_TRUE        13 (to L4)
               NOT_TAKEN

686            LOAD_GLOBAL              3 (print + NULL)
               LOAD_CONST               5 ('  No findings.')
               CALL                     1
               POP_TOP
               JUMP_FORWARD           203 (to L11)

688    L4:     LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                8 (findings)
               GET_ITER
       L5:     FOR_ITER               187 (to L10)
               STORE_FAST               4 (f)

689            LOAD_FAST_BORROW         4 (f)
               LOAD_ATTR               10 (line)
               TO_BOOL
               POP_JUMP_IF_FALSE       16 (to L6)
               NOT_TAKEN
               LOAD_CONST               6 (':')
               LOAD_FAST_BORROW         4 (f)
               LOAD_ATTR               10 (line)
               FORMAT_SIMPLE
               BUILD_STRING             2
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               7 ('')
       L7:     STORE_FAST               5 (line_loc)

690            LOAD_GLOBAL              3 (print + NULL)
               LOAD_CONST               8 ('  [')
               LOAD_FAST_BORROW         4 (f)
               LOAD_ATTR               12 (severity)
               FORMAT_SIMPLE
               LOAD_CONST               9 ('] ')
               LOAD_FAST_BORROW         4 (f)
               LOAD_ATTR               14 (title)
               FORMAT_SIMPLE
               BUILD_STRING             4
               CALL                     1
               POP_TOP

691            LOAD_GLOBAL              3 (print + NULL)
               LOAD_CONST              10 ('        ')
               LOAD_FAST_BORROW         4 (f)
               LOAD_ATTR               16 (file)
               FORMAT_SIMPLE
               LOAD_FAST_BORROW         5 (line_loc)
               FORMAT_SIMPLE
               BUILD_STRING             3
               CALL                     1
               POP_TOP

692            LOAD_FAST_BORROW         4 (f)
               LOAD_ATTR               18 (detail)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L8)
               NOT_TAKEN

693            LOAD_GLOBAL              3 (print + NULL)
               LOAD_CONST              10 ('        ')
               LOAD_FAST_BORROW         4 (f)
               LOAD_ATTR               18 (detail)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

694    L8:     LOAD_FAST_BORROW         4 (f)
               LOAD_ATTR               20 (suggestion)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD          163 (to L5)

695    L9:     LOAD_GLOBAL              3 (print + NULL)
               LOAD_CONST              11 ('        → ')
               LOAD_FAST_BORROW         4 (f)
               LOAD_ATTR               20 (suggestion)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          189 (to L5)

688   L10:     END_FOR
               POP_ITER

696   L11:     LOAD_GLOBAL              3 (print + NULL)
               LOAD_CONST              12 ('========================================================================')
               CALL                     1
               POP_TOP
               LOAD_CONST               4 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 699>:
699           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('argv')
              LOAD_CONST               2 ('Optional[list]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object main at 0x0000018C182E2020, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\security_audit.py", line 699>:
 699            RESUME                   0

 700            LOAD_GLOBAL              0 (argparse)
                LOAD_ATTR                2 (ArgumentParser)
                PUSH_NULL

 701            LOAD_CONST               0 ('security_audit')

 702            LOAD_CONST               1 ('PAS143E — static security & integrity scanner.')

 700            LOAD_CONST               2 (('prog', 'description'))
                CALL_KW                  2
                STORE_FAST               1 (parser)

 704            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST               3 ('--strict')
                LOAD_CONST               4 ('store_true')

 705            LOAD_CONST               5 ('Exit non-zero if any HIGH or CRITICAL finding is present.')

 704            LOAD_CONST               6 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 706            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST               7 ('--json')
                LOAD_CONST               4 ('store_true')

 707            LOAD_CONST               8 ('Emit the report as JSON.')

 706            LOAD_CONST               6 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 708            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST               9 ('--summary-only')
                LOAD_CONST               4 ('store_true')

 709            LOAD_CONST              10 ('Print only the severity counts.')

 708            LOAD_CONST               6 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 710            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST              11 ('--repo-root')
                LOAD_CONST              12 (None)

 711            LOAD_CONST              13 ("Override the repo root (defaults to script's parent dir).")

 710            LOAD_CONST              14 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 712            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                7 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 714            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR                8 (repo_root)
                TO_BOOL
                POP_JUMP_IF_FALSE       22 (to L1)
                NOT_TAKEN
                LOAD_GLOBAL             11 (Path + NULL)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR                8 (repo_root)
                CALL                     1
                JUMP_FORWARD            45 (to L2)
        L1:     LOAD_GLOBAL             11 (Path + NULL)
                LOAD_GLOBAL             12 (__file__)
                CALL                     1
                LOAD_ATTR               15 (resolve + NULL|self)
                CALL                     0
                LOAD_ATTR               16 (parents)
                LOAD_SMALL_INT           1
                BINARY_OP               26 ([])
        L2:     STORE_FAST               3 (repo_root)

 715            LOAD_GLOBAL             19 (run_audit + NULL)
                LOAD_FAST_BORROW         3 (repo_root)
                CALL                     1
                STORE_FAST               4 (report)

 718            LOAD_GLOBAL             10 (Path)
                LOAD_ATTR               20 (cwd)
                PUSH_NULL
                CALL                     0
                LOAD_CONST              15 ('security_audit_report.json')
                BINARY_OP               11 (/)
                STORE_FAST               5 (report_path)

 719            NOP

 720    L3:     LOAD_FAST_BORROW         5 (report_path)
                LOAD_ATTR               23 (write_text + NULL|self)
                LOAD_GLOBAL             24 (json)
                LOAD_ATTR               26 (dumps)
                PUSH_NULL
                LOAD_FAST_BORROW         4 (report)
                LOAD_ATTR               29 (to_dict + NULL|self)
                CALL                     0
                LOAD_SMALL_INT           2
                LOAD_CONST              16 (('indent',))
                CALL_KW                  2
                LOAD_CONST              17 ('utf-8')
                LOAD_CONST              18 (('encoding',))
                CALL_KW                  2
                POP_TOP

 724    L4:     LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               24 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       49 (to L5)
                NOT_TAKEN

 725            LOAD_GLOBAL             33 (print + NULL)
                LOAD_GLOBAL             24 (json)
                LOAD_ATTR               26 (dumps)
                PUSH_NULL
                LOAD_FAST_BORROW         4 (report)
                LOAD_ATTR               29 (to_dict + NULL|self)
                CALL                     0
                LOAD_SMALL_INT           2
                LOAD_CONST              16 (('indent',))
                CALL_KW                  2
                CALL                     1
                POP_TOP
                JUMP_FORWARD            54 (to L6)

 727    L5:     LOAD_GLOBAL             39 (_print_human + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (report, args)
                LOAD_ATTR               40 (summary_only)
                LOAD_CONST              21 (('summary_only',))
                CALL_KW                  2
                POP_TOP

 728            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               40 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L6)
                NOT_TAKEN

 729            LOAD_GLOBAL             33 (print + NULL)
                LOAD_CONST              22 ('  report: ')
                LOAD_FAST_BORROW         5 (report_path)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 731    L6:     LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               42 (strict)
                TO_BOOL
                POP_JUMP_IF_FALSE       79 (to L7)
                NOT_TAKEN

 732            LOAD_FAST_BORROW         4 (report)
                LOAD_ATTR               45 (counts + NULL|self)
                CALL                     0
                LOAD_ATTR               47 (get + NULL|self)
                LOAD_CONST              23 ('CRITICAL')
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_FAST_BORROW         4 (report)
                LOAD_ATTR               45 (counts + NULL|self)
                CALL                     0
                LOAD_ATTR               47 (get + NULL|self)
                LOAD_CONST              24 ('HIGH')
                LOAD_SMALL_INT           0
                CALL                     2
                BINARY_OP                0 (+)
                STORE_FAST               7 (critical_or_high)

 733            LOAD_FAST_BORROW         7 (critical_or_high)
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN

 734            LOAD_SMALL_INT           1
                RETURN_VALUE

 735    L7:     LOAD_SMALL_INT           0
                RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

 721            LOAD_GLOBAL             30 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       42 (to L12)
                NOT_TAKEN
                STORE_FAST               6 (e)

 722    L9:     LOAD_GLOBAL             33 (print + NULL)
                LOAD_CONST              19 ('WARNING: could not write report: ')
                LOAD_FAST                6 (e)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             34 (sys)
                LOAD_ATTR               36 (stderr)
                LOAD_CONST              20 (('file',))
                CALL_KW                  2
                POP_TOP
       L10:     POP_EXCEPT
                LOAD_CONST              12 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 265 (to L4)

  --   L11:     LOAD_CONST              12 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 721   L12:     RERAISE                  0

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L8 [0]
  L8 to L9 -> L13 [1] lasti
  L9 to L10 -> L11 [1] lasti
  L11 to L13 -> L13 [1] lasti
```
