# scripts_readiness/pre_pas144_readiness_check

- **pyc:** `scripts\__pycache__\pre_pas144_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pre_pas144_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pre_pas144_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS143I — Pre-PAS144 operator readiness gate.

Deterministic, non-mutating evaluator. Walks the repo, checks the
substrate that PAS143D-H delivered, optionally consumes upstream report
JSON, and emits a verdict (PASS / PASS_WITH_WARNINGS / FAIL) plus a
machine-readable `pre_pas144_readiness_report.json`.

This script never:
  - modifies files,
  - calls Supabase,
  - reads .env / secrets,
  - includes payload values in the report or summary.

Usage:
  python scripts/pre_pas144_readiness_check.py
  python scripts/pre_pas144_readiness_check.py --strict
  python scripts/pre_pas144_readiness_check.py --json
  python scripts/pre_pas144_readiness_check.py \
      --security-report security_audit_report.json \
      --integrity-report integrity_check_report.json \
      --monitoring-report monitoring_report.json \
      --restore-report recovery/<ts>_restore_drill_report.json

Exit codes:
    0  — PASS (or PASS_WITH_WARNINGS without --strict)
    1  — FAIL, or --strict and status != PASS
    2  — bad CLI arguments
```

## Imports

`Iterable`, `List`, `Optional`, `Path`, `__future__`, `annotations`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_aggregate_status`, `_check`, `_coerce_count`, `_files_present`, `_now_iso`, `_operator_actions`, `_recommended_next_step`, `_safe_coerce_int`, `_safe_read_json`, `_summary_lines`, `check_gitignore_patterns`, `check_repository_hygiene`, `check_required_docs`, `check_required_migrations`, `check_required_scripts`, `evaluate_integrity_report`, `evaluate_monitoring_report`, `evaluate_readiness`, `evaluate_restore_report`, `evaluate_security_report`, `main`, `render_summary`

## Env-key candidates

`CRITICAL`, `FAIL`, `HIGH`, `PASS`, `PASS_WITH_WARNINGS`, `REQUIRED_DOCS`, `REQUIRED_GITIGNORE_PATTERNS`, `REQUIRED_MIGRATIONS`, `REQUIRED_SCRIPTS`, `UNKNOWN`, `WARN`, `YES`

## String constants (redacted where noted)

- '\nPAS143I — Pre-PAS144 operator readiness gate.\n\nDeterministic, non-mutating evaluator. Walks the repo, checks the\nsubstrate that PAS143D-H delivered, optionally consumes upstream report\nJSON, and emits a verdict (PASS / PASS_WITH_WARNINGS / FAIL) plus a\nmachine-readable `pre_pas144_readiness_report.json`.\n\nThis script never:\n  - modifies files,\n  - calls Supabase,\n  - reads .env / secrets,\n  - includes payload values in the report or summary.\n\nUsage:\n  python scripts/pre_pas144_readiness_check.py\n  python scripts/pre_pas144_readiness_check.py --strict\n  python scripts/pre_pas144_readiness_check.py --json\n  python scripts/pre_pas144_readiness_check.py \\\n      --security-report security_audit_report.json \\\n      --integrity-report integrity_check_report.json \\\n      --monitoring-report monitoring_report.json \\\n      --restore-report recovery/<ts>_restore_drill_report.json\n\nExit codes:\n    0  — PASS (or PASS_WITH_WARNINGS without --strict)\n    1  — FAIL, or --strict and status != PASS\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'tuple'
- 'REQUIRED_MIGRATIONS'
- 'REQUIRED_SCRIPTS'
- 'REQUIRED_DOCS'
- 'REQUIRED_GITIGNORE_PATTERNS'
- 'frozenset'
- '_HYGIENE_SKIP_DIRS'
- '_DANGEROUS_SUFFIXES'
- 'security_report'
- 'integrity_report'
- 'monitoring_report'
- 'restore_report'
- 'check_id'
- 'str'
- 'status'
- 'label'
- 'detail'
- 'return'
- 'dict'
- 'seconds'
- 'repo_root'
- 'rel_paths'
- 'Iterable[str]'
- 'Return {path: exists} for the given relative paths.'
- 'List[dict]'
- 'One check per required migration file.'
- 'migration:'
- 'PASS'
- 'FAIL'
- 'migration '
- 'present'
- 'missing at '
- 'script:'
- 'script '
- 'doc:'
- 'doc '
- 'Verify every required pattern appears in the repo .gitignore.'
- '.gitignore'
- 'gitignore:exists'
- '.gitignore present'
- 'missing at repo root'
- 'gitignore:readable'
- '.gitignore readable'
- 'unreadable ('
- ' found'
- 'gitignore:'
- '.gitignore protects '
- 'pattern present'
- 'pattern '
- ' missing — append to .gitignore'
- 'Walk the repo and FAIL if any dangerous artefact appears outside\nthe skip-dirs. Returns at least one summary check; one check per\ndiscovered offender.\n'
- 'hygiene:no_dangerous_artefacts'
- 'no tracked backup / archive / dump artefacts'
- 'filesystem walk clean'
- 'hygiene:tracked_artefact:'
- 'dangerous tracked artefact'
- ' matches a forbidden extension — remove from working tree'
- 'Optional[int]'
- 'Coerce *value* to int without raising. Returns None for malformed\ninputs so callers can fail closed instead of silently treating\ngarbage as zero. Accepts: int, bool, finite float, decimal/integer\nstrings (with surrounding whitespace). Rejects: None, empty string,\nnon-numeric strings ("unknown"), NaN/inf.'
- 'inf'
- '-inf'
- 'default'
- 'int'
- 'Severity-count coercion: missing-or-null treated as *default*;\neverything else routed through `_safe_coerce_int` (returns None on\nmalformed input).'
- 'path'
- 'Optional[str]'
- 'Optional[dict]'
- 'report'
- 'FAIL on any CRITICAL or HIGH severity finding. WARN if absent.\n\nReads severity counts from any of the supported emitter shapes:\n  - report["counts"]          (PAS143E security_audit.py emitter)\n  - report["by_severity"]\n  - report["severity_counts"]\nMissing keys default to 0; malformed values (e.g. "unknown") are\nrejected and fail closed — they must not silently PASS.'
- 'security:report'
- 'WARN'
- 'security audit report'
- 'not provided — gate downgraded to PASS_WITH_WARNINGS'
- 'security audit report unreadable'
- 'no severity counts under counts/by_severity/severity_counts — failing closed'
- 'CRITICAL'
- 'HIGH'
- 'security audit report has malformed severity counts'
- 'CRITICAL/HIGH could not be coerced to int (shape='
- ') — failing closed'
- 'security audit report has CRITICAL/HIGH'
- 'CRITICAL='
- ' HIGH='
- ' (shape='
- 'security audit report clean'
- 'CRITICAL=0 HIGH=0 (shape='
- 'FAIL when any check failed; WARN if absent.\n\nReads failure indicators from every supported emitter shape and\ntakes the worst (max) signal so a single mismatched shape cannot\nsilently PASS:\n  - report["counts"]["failed"]   (PAS143E integrity_check.py emitter)\n  - report["summary"]["failed"]\n  - report["failed_count"]\n  - report["results"][] / report["checks"][] sweep, where\n    any item with passed == False or status in {FAIL, FAILED, ERROR}\n    is counted as a failure.\nMalformed counts or fundamentally unreadable shapes fail closed.'
- 'integrity:report'
- 'integrity check report'
- 'counts'
- 'failed'
- 'counts.failed'
- 'counts(non-dict)'
- 'summary'
- 'summary.failed'
- 'summary(non-dict)'
- 'failed_count'
- 'results'
- 'checks'
- 'passed'
- 'results[]'
- 'results(non-list)'
- 'integrity check report has malformed shape'
- 'could not coerce: '
- ' — failing closed'
- 'integrity check report unreadable'
- 'no failure indicator (counts.failed / summary.failed / failed_count / results[]) — failing closed'
- 'integrity check report has failures'
- 'failed='
- ' (shapes='
- 'integrity check report clean'
- 'no failing checks (shapes='
- 'FAIL when safe_to_continue != True; WARN if absent.'
- 'monitoring:report'
- 'monitoring report'
- 'safe_to_continue'
- 'by_severity'
- 'monitoring safe_to_continue'
- 'monitoring not safe_to_continue'
- 'safe_to_continue='
- 'FAIL when restore_success != True; WARN if absent.'
- 'restore:report'
- 'restore drill report'
- 'restore_success'
- 'restore drill succeeded'
- 'restore_success=true'
- 'restore drill failed'
- 'restore_success='
- 'PASS_WITH_WARNINGS'
- 'safe_for_pas144'
- 'failures'
- 'warnings'
- 'List[str]'
- 'Return human-readable next steps for the operator.'
- 'Restore missing file referenced by '
- 'Append missing patterns to .gitignore (see §11 of the readiness doc).'
- "Remove tracked backup/dump/archive artefacts from the working tree; these patterns are .gitignore'd and must not appear in repo."
- 'Resolve CRITICAL/HIGH findings in security_audit_report.json, then re-run the gate.'
- 'Investigate failing checks in integrity_check_report.json, then re-run the gate.'
- 'Address monitoring alerts so safe_to_continue=true, then re-run the gate.'
- 'Re-run the restore drill until restore_success=true, then re-run the gate.'
- 'Provide --security-report path to re-evaluate.'
- 'Provide --integrity-report path to re-evaluate.'
- 'Provide --monitoring-report path to re-evaluate.'
- 'Provide --restore-report path to re-evaluate.'
- 'Initial each line of the §10 sign-off checklist before PAS144 begins.'
- 'Sign off on §10 of docs/pas143i_pre_pas144_readiness_gate.md and proceed to PAS144.'
- 'Provide every report (--security/--integrity/--monitoring/--restore) and re-run in --strict mode.'
- 'Resolve every FAIL above, then re-run pre_pas144_readiness_check.py --strict.'
- 'Pure evaluator. Returns the structured readiness report dict.'
- 'migrations'
- 'scripts'
- 'docs'
- 'gitignore_patterns'
- 'security'
- 'integrity'
- 'monitoring'
- 'restore'
- 'timestamp'
- 'required_files'
- 'reports_evaluated'
- 'operator_actions_required'
- 'recommended_next_step'
- 'tool_versions'
- 'python'
- 'platform'
- 'schema'
- 'pas143i.v1'
- 'PAS143I READINESS SUMMARY'
- 'Status: '
- 'UNKNOWN'
- 'Safe for PAS144: '
- 'YES'
- 'Checks:'
- 'Operator actions before PAS144:'
- 'Recommended next: '
- '-------------------------'
- 'argv'
- 'Optional[list]'
- 'pre_pas144_readiness_check'
- 'PAS143I — pre-PAS144 operator readiness gate.'
- '--repo-root'
- 'Repository root to evaluate (default: parent of scripts/).'
- '--security-report'
- 'Path to security_audit_report.json (optional).'
- '--integrity-report'
- 'Path to integrity_check_report.json (optional).'
- '--monitoring-report'
- 'Path to monitoring_report.json (optional).'
- '--restore-report'
- 'Path to restore_drill_report.json (optional).'
- '--json'
- 'store_true'
- 'Emit the readiness report as JSON instead of the human view.'
- '--strict'
- 'Exit 1 unless status == PASS (PASS_WITH_WARNINGS also exits 1).'
- '--output'
- 'Path to write pre_pas144_readiness_report.json (default: CWD).'
- 'security report'
- 'integrity report'
- 'pre_pas144_readiness_report.json'
- '  [warn] could not write '
- '  report: '

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS143I — Pre-PAS144 operator readiness gate.\n\nDeterministic, non-mutating evaluator. Walks the repo, checks the\nsubstrate that PAS143D-H delivered, optionally consumes upstream report\nJSON, and emits a verdict (PASS / PASS_WITH_WARNINGS / FAIL) plus a\nmachine-readable `pre_pas144_readiness_report.json`.\n\nThis script never:\n  - modifies files,\n  - calls Supabase,\n  - reads .env / secrets,\n  - includes payload values in the report or summary.\n\nUsage:\n  python scripts/pre_pas144_readiness_check.py\n  python scripts/pre_pas144_readiness_check.py --strict\n  python scripts/pre_pas144_readiness_check.py --json\n  python scripts/pre_pas144_readiness_check.py \\\n      --security-report security_audit_report.json \\\n      --integrity-report integrity_check_report.json \\\n      --monitoring-report monitoring_report.json \\\n      --restore-report recovery/<ts>_restore_drill_report.json\n\nExit codes:\n    0  — PASS (or PASS_WITH_WARNINGS without --strict)\n    1  — FAIL, or --strict and status != PASS\n    2  — bad CLI arguments\n')
               STORE_NAME               1 (__doc__)

  31           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  33           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (argparse)
               STORE_NAME               4 (argparse)

  34           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (json)
               STORE_NAME               5 (json)

  35           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (os)
               STORE_NAME               6 (os)

  36           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (sys)
               STORE_NAME               7 (sys)

  37           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              8 (datetime)
               IMPORT_FROM              8 (datetime)
               STORE_NAME               8 (datetime)
               IMPORT_FROM              9 (timezone)
               STORE_NAME               9 (timezone)
               POP_TOP

  38           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME             10 (pathlib)
               IMPORT_FROM             11 (Path)
               STORE_NAME              11 (Path)
               POP_TOP

  39           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('Iterable', 'List', 'Optional'))
               IMPORT_NAME             12 (typing)
               IMPORT_FROM             13 (Iterable)
               STORE_NAME              13 (Iterable)
               IMPORT_FROM             14 (List)
               STORE_NAME              14 (List)
               IMPORT_FROM             15 (Optional)
               STORE_NAME              15 (Optional)
               POP_TOP

  43           LOAD_NAME                7 (sys)
               LOAD_ATTR               32 (stdout)
               LOAD_NAME                7 (sys)
               LOAD_ATTR               34 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              18 (_stream)

  44           NOP

  45   L2:     LOAD_NAME               18 (_stream)
               LOAD_ATTR               39 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  43   L4:     END_FOR
               POP_ITER

  50           LOAD_NAME                6 (os)
               LOAD_ATTR               42 (path)
               LOAD_ATTR               45 (abspath + NULL|self)
               LOAD_NAME                6 (os)
               LOAD_ATTR               42 (path)
               LOAD_ATTR               47 (join + NULL|self)
               LOAD_NAME                6 (os)
               LOAD_ATTR               42 (path)
               LOAD_ATTR               49 (dirname + NULL|self)
               LOAD_NAME               25 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2
               CALL                     1
               STORE_NAME              26 (_REPO_ROOT_DEFAULT)

  58           LOAD_CONST              66 (('scripts/migrate_v8_event_contract.sql', 'scripts/migrate_v9_column_privileges.sql'))
               STORE_NAME              27 (REQUIRED_MIGRATIONS)
               LOAD_CONST               9 ('tuple')
               LOAD_NAME               28 (__annotations__)
               LOAD_CONST              10 ('REQUIRED_MIGRATIONS')
               STORE_SUBSCR

  63           LOAD_CONST              67 (('scripts/backup_database.py', 'scripts/verify_backup.py', 'scripts/package_backup.py', 'scripts/restore_drill.py', 'scripts/security_audit.py', 'scripts/integrity_check.py', 'scripts/run_monitoring_check.py'))
               STORE_NAME              29 (REQUIRED_SCRIPTS)
               LOAD_CONST               9 ('tuple')
               LOAD_NAME               28 (__annotations__)
               LOAD_CONST              11 ('REQUIRED_SCRIPTS')
               STORE_SUBSCR

  73           LOAD_CONST              68 (('docs/pas143d_data_durability_runbook.md', 'docs/pas143e_security_integrity_audit.md', 'docs/pas143g_restore_drill_runbook.md', 'docs/pas143h_rls_column_privilege_audit.md'))
               STORE_NAME              30 (REQUIRED_DOCS)
               LOAD_CONST               9 ('tuple')
               LOAD_NAME               28 (__annotations__)
               LOAD_CONST              12 ('REQUIRED_DOCS')
               STORE_SUBSCR

  80           LOAD_CONST              69 (('backups/', '*.dump', '*.backup', '*.jsonl', '*.pasbak', 'restore_drill_report.json', 'monitoring_report.json'))
               STORE_NAME              31 (REQUIRED_GITIGNORE_PATTERNS)
               LOAD_CONST               9 ('tuple')
               LOAD_NAME               28 (__annotations__)
               LOAD_CONST              13 ('REQUIRED_GITIGNORE_PATTERNS')
               STORE_SUBSCR

  92           LOAD_NAME               32 (frozenset)
               PUSH_NULL
               BUILD_SET                0
               LOAD_CONST              70 (frozenset({'recovery', '.tox', 'tests', '.pytest_cache', 'node_modules', '.venv', '.mypy_cache', 'backups', 'venv', '.git', '__pycache__'}))
               SET_UPDATE               1
               CALL                     1
               STORE_NAME              33 (_HYGIENE_SKIP_DIRS)
               LOAD_CONST              14 ('frozenset')
               LOAD_NAME               28 (__annotations__)
               LOAD_CONST              15 ('_HYGIENE_SKIP_DIRS')
               STORE_SUBSCR

 108           LOAD_CONST              71 (('.dump', '.backup', '.jsonl', '.pasbak'))
               STORE_NAME              34 (_DANGEROUS_SUFFIXES)
               LOAD_CONST               9 ('tuple')
               LOAD_NAME               28 (__annotations__)
               LOAD_CONST              16 ('_DANGEROUS_SUFFIXES')
               STORE_SUBSCR

 115           LOAD_CONST              72 (('',))
               LOAD_CONST              17 (<code object __annotate__ at 0x0000018C18024B30, file "scripts\pre_pas144_readiness_check.py", line 115>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object _check at 0x0000018C17FA2A60, file "scripts\pre_pas144_readiness_check.py", line 115>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              35 (_check)

 124           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts\pre_pas144_readiness_check.py", line 124>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object _now_iso at 0x0000018C18038170, file "scripts\pre_pas144_readiness_check.py", line 124>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              36 (_now_iso)

 132           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C18024C30, file "scripts\pre_pas144_readiness_check.py", line 132>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object _files_present at 0x0000018C18038A30, file "scripts\pre_pas144_readiness_check.py", line 132>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              37 (_files_present)

 138           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pre_pas144_readiness_check.py", line 138>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object check_required_migrations at 0x0000018C179A7290, file "scripts\pre_pas144_readiness_check.py", line 138>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (check_required_migrations)

 152           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts\pre_pas144_readiness_check.py", line 152>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object check_required_scripts at 0x0000018C1801C9E0, file "scripts\pre_pas144_readiness_check.py", line 152>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              39 (check_required_scripts)

 165           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts\pre_pas144_readiness_check.py", line 165>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object check_required_docs at 0x0000018C1801D1A0, file "scripts\pre_pas144_readiness_check.py", line 165>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              40 (check_required_docs)

 178           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pre_pas144_readiness_check.py", line 178>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object check_gitignore_patterns at 0x0000018C17F67A50, file "scripts\pre_pas144_readiness_check.py", line 178>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (check_gitignore_patterns)

 223           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pre_pas144_readiness_check.py", line 223>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object check_repository_hygiene at 0x0000018C17F75FB0, file "scripts\pre_pas144_readiness_check.py", line 223>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (check_repository_hygiene)

 270           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pre_pas144_readiness_check.py", line 270>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object _safe_coerce_int at 0x0000018C17D8BD50, file "scripts\pre_pas144_readiness_check.py", line 270>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_safe_coerce_int)

 305           LOAD_CONST              73 ((0,))
               LOAD_CONST              35 (<code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pre_pas144_readiness_check.py", line 305>)
               MAKE_FUNCTION
               LOAD_CONST              36 (<code object _coerce_count at 0x0000018C18025030, file "scripts\pre_pas144_readiness_check.py", line 305>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              44 (_coerce_count)

 314           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C18024E30, file "scripts\pre_pas144_readiness_check.py", line 314>)
               MAKE_FUNCTION
               LOAD_CONST              38 (<code object _safe_read_json at 0x0000018C179C3A50, file "scripts\pre_pas144_readiness_check.py", line 314>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (_safe_read_json)

 328           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C17FA2880, file "scripts\pre_pas144_readiness_check.py", line 328>)
               MAKE_FUNCTION
               LOAD_CONST              40 (<code object evaluate_security_report at 0x0000018C17E7E710, file "scripts\pre_pas144_readiness_check.py", line 328>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (evaluate_security_report)

 390           LOAD_CONST              41 (<code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pre_pas144_readiness_check.py", line 390>)
               MAKE_FUNCTION
               LOAD_CONST              42 (<code object evaluate_integrity_report at 0x0000018C17F7DED0, file "scripts\pre_pas144_readiness_check.py", line 390>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (evaluate_integrity_report)

 505           LOAD_CONST              43 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pre_pas144_readiness_check.py", line 505>)
               MAKE_FUNCTION
               LOAD_CONST              44 (<code object evaluate_monitoring_report at 0x0000018C17ECF000, file "scripts\pre_pas144_readiness_check.py", line 505>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (evaluate_monitoring_report)

 533           LOAD_CONST              45 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts\pre_pas144_readiness_check.py", line 533>)
               MAKE_FUNCTION
               LOAD_CONST              46 (<code object evaluate_restore_report at 0x0000018C17F95FD0, file "scripts\pre_pas144_readiness_check.py", line 533>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (evaluate_restore_report)

 562           LOAD_CONST              47 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pre_pas144_readiness_check.py", line 562>)
               MAKE_FUNCTION
               LOAD_CONST              48 (<code object _aggregate_status at 0x0000018C18060F60, file "scripts\pre_pas144_readiness_check.py", line 562>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (_aggregate_status)

 579           LOAD_CONST              49 (<code object __annotate__ at 0x0000018C18025130, file "scripts\pre_pas144_readiness_check.py", line 579>)
               MAKE_FUNCTION
               LOAD_CONST              50 (<code object _operator_actions at 0x0000018C17F7E6A0, file "scripts\pre_pas144_readiness_check.py", line 579>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (_operator_actions)

 628           LOAD_CONST              51 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pre_pas144_readiness_check.py", line 628>)
               MAKE_FUNCTION
               LOAD_CONST              52 (<code object _recommended_next_step at 0x0000018C18024930, file "scripts\pre_pas144_readiness_check.py", line 628>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (_recommended_next_step)

 640           LOAD_CONST              53 ('security_report')

 643           LOAD_CONST               2 (None)

 640           LOAD_CONST              54 ('integrity_report')

 644           LOAD_CONST               2 (None)

 640           LOAD_CONST              55 ('monitoring_report')

 645           LOAD_CONST               2 (None)

 640           LOAD_CONST              56 ('restore_report')

 646           LOAD_CONST               2 (None)

 640           BUILD_MAP                4
               LOAD_CONST              57 (<code object __annotate__ at 0x0000018C18024F30, file "scripts\pre_pas144_readiness_check.py", line 640>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object evaluate_readiness at 0x0000018C181B3050, file "scripts\pre_pas144_readiness_check.py", line 640>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              53 (evaluate_readiness)

 703           LOAD_CONST              59 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pre_pas144_readiness_check.py", line 703>)
               MAKE_FUNCTION
               LOAD_CONST              60 (<code object _summary_lines at 0x0000018C17E920A0, file "scripts\pre_pas144_readiness_check.py", line 703>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (_summary_lines)

 727           LOAD_CONST              61 (<code object __annotate__ at 0x0000018C17FA2790, file "scripts\pre_pas144_readiness_check.py", line 727>)
               MAKE_FUNCTION
               LOAD_CONST              62 (<code object render_summary at 0x0000018C1812C7A0, file "scripts\pre_pas144_readiness_check.py", line 727>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (render_summary)

 735           LOAD_CONST              74 ((None,))
               LOAD_CONST              63 (<code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pre_pas144_readiness_check.py", line 735>)
               MAKE_FUNCTION
               LOAD_CONST              64 (<code object main at 0x0000018C17D58AC0, file "scripts\pre_pas144_readiness_check.py", line 735>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              56 (main)

 814           LOAD_NAME               57 (__name__)
               LOAD_CONST              65 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       14 (to L5)
               NOT_TAKEN

 815           LOAD_NAME               58 (SystemExit)
               PUSH_NULL
               LOAD_NAME               56 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               RAISE_VARARGS            1

 814   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  46           LOAD_NAME               20 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  47   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          335 (to L1)

  46   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "scripts\pre_pas144_readiness_check.py", line 115>:
115           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('status')
              LOAD_CONST               2 ('str')
              LOAD_CONST               4 ('label')
              LOAD_CONST               2 ('str')
              LOAD_CONST               5 ('detail')
              LOAD_CONST               2 ('str')
              LOAD_CONST               6 ('return')
              LOAD_CONST               7 ('dict')
              BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA2A60, file "scripts\pre_pas144_readiness_check.py", line 115>:
115           RESUME                   0

117           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

118           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

119           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

120           LOAD_CONST               3 ('detail')
              LOAD_FAST_BORROW         3 (detail)

116           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts\pre_pas144_readiness_check.py", line 124>:
124           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038170, file "scripts\pre_pas144_readiness_check.py", line 124>:
124           RESUME                   0

125           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "scripts\pre_pas144_readiness_check.py", line 132>:
132           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('rel_paths')
              LOAD_CONST               4 ('Iterable[str]')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('dict')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _files_present at 0x0000018C18038A30, file "scripts\pre_pas144_readiness_check.py", line 132>:
 132           RESUME                   0

 134           LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               STORE_FAST               2 (root)

 135           LOAD_FAST_BORROW         1 (rel_paths)
               GET_ITER
               LOAD_FAST_AND_CLEAR      3 (p)
               SWAP                     2
       L1:     BUILD_MAP                0
               SWAP                     2
       L2:     FOR_ITER                25 (to L3)
               STORE_FAST_LOAD_FAST    51 (p, p)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (root, p)
               BINARY_OP               11 (/)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               MAP_ADD                  2
               JUMP_BACKWARD           27 (to L2)
       L3:     END_FOR
               POP_ITER
       L4:     SWAP                     2
               STORE_FAST               3 (p)
               RETURN_VALUE

  --   L5:     SWAP                     2
               POP_TOP

 135           SWAP                     2
               STORE_FAST               3 (p)
               RERAISE                  0
ExceptionTable:
  L1 to L4 -> L5 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pre_pas144_readiness_check.py", line 138>:
138           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_required_migrations at 0x0000018C179A7290, file "scripts\pre_pas144_readiness_check.py", line 138>:
138           RESUME                   0

140           BUILD_LIST               0
              STORE_FAST               1 (out)

141           LOAD_GLOBAL              1 (_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              LOAD_GLOBAL              2 (REQUIRED_MIGRATIONS)
              CALL                     2
              STORE_FAST               2 (presence)

142           LOAD_FAST_BORROW         2 (presence)
              LOAD_ATTR                5 (items + NULL|self)
              CALL                     0
              GET_ITER
      L1:     FOR_ITER               101 (to L6)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   52 (path, ok)

143           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

144           LOAD_CONST               1 ('migration:')
              LOAD_GLOBAL             11 (Path + NULL)
              LOAD_FAST_BORROW         3 (path)
              CALL                     1
              LOAD_ATTR               12 (name)
              FORMAT_SIMPLE
              BUILD_STRING             2

145           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               2 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               3 ('FAIL')

146   L3:     LOAD_CONST               4 ('migration ')
              LOAD_GLOBAL             11 (Path + NULL)
              LOAD_FAST_BORROW         3 (path)
              CALL                     1
              LOAD_ATTR               12 (name)
              FORMAT_SIMPLE
              BUILD_STRING             2

147           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               5 ('present')
              JUMP_FORWARD             4 (to L5)
      L4:     LOAD_CONST               6 ('missing at ')
              LOAD_FAST_BORROW         3 (path)
              FORMAT_SIMPLE
              BUILD_STRING             2

143   L5:     CALL                     4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          103 (to L1)

142   L6:     END_FOR
              POP_ITER

149           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts\pre_pas144_readiness_check.py", line 152>:
152           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_required_scripts at 0x0000018C1801C9E0, file "scripts\pre_pas144_readiness_check.py", line 152>:
152           RESUME                   0

153           BUILD_LIST               0
              STORE_FAST               1 (out)

154           LOAD_GLOBAL              1 (_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              LOAD_GLOBAL              2 (REQUIRED_SCRIPTS)
              CALL                     2
              STORE_FAST               2 (presence)

155           LOAD_FAST_BORROW         2 (presence)
              LOAD_ATTR                5 (items + NULL|self)
              CALL                     0
              GET_ITER
      L1:     FOR_ITER               101 (to L6)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   52 (path, ok)

156           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

157           LOAD_CONST               0 ('script:')
              LOAD_GLOBAL             11 (Path + NULL)
              LOAD_FAST_BORROW         3 (path)
              CALL                     1
              LOAD_ATTR               12 (name)
              FORMAT_SIMPLE
              BUILD_STRING             2

158           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

159   L3:     LOAD_CONST               3 ('script ')
              LOAD_GLOBAL             11 (Path + NULL)
              LOAD_FAST_BORROW         3 (path)
              CALL                     1
              LOAD_ATTR               12 (name)
              FORMAT_SIMPLE
              BUILD_STRING             2

160           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('present')
              JUMP_FORWARD             4 (to L5)
      L4:     LOAD_CONST               5 ('missing at ')
              LOAD_FAST_BORROW         3 (path)
              FORMAT_SIMPLE
              BUILD_STRING             2

156   L5:     CALL                     4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          103 (to L1)

155   L6:     END_FOR
              POP_ITER

162           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts\pre_pas144_readiness_check.py", line 165>:
165           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_required_docs at 0x0000018C1801D1A0, file "scripts\pre_pas144_readiness_check.py", line 165>:
165           RESUME                   0

166           BUILD_LIST               0
              STORE_FAST               1 (out)

167           LOAD_GLOBAL              1 (_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              LOAD_GLOBAL              2 (REQUIRED_DOCS)
              CALL                     2
              STORE_FAST               2 (presence)

168           LOAD_FAST_BORROW         2 (presence)
              LOAD_ATTR                5 (items + NULL|self)
              CALL                     0
              GET_ITER
      L1:     FOR_ITER               101 (to L6)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   52 (path, ok)

169           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

170           LOAD_CONST               0 ('doc:')
              LOAD_GLOBAL             11 (Path + NULL)
              LOAD_FAST_BORROW         3 (path)
              CALL                     1
              LOAD_ATTR               12 (name)
              FORMAT_SIMPLE
              BUILD_STRING             2

171           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

172   L3:     LOAD_CONST               3 ('doc ')
              LOAD_GLOBAL             11 (Path + NULL)
              LOAD_FAST_BORROW         3 (path)
              CALL                     1
              LOAD_ATTR               12 (name)
              FORMAT_SIMPLE
              BUILD_STRING             2

173           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('present')
              JUMP_FORWARD             4 (to L5)
      L4:     LOAD_CONST               5 ('missing at ')
              LOAD_FAST_BORROW         3 (path)
              FORMAT_SIMPLE
              BUILD_STRING             2

169   L5:     CALL                     4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          103 (to L1)

168   L6:     END_FOR
              POP_ITER

175           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pre_pas144_readiness_check.py", line 178>:
178           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_gitignore_patterns at 0x0000018C17F67A50, file "scripts\pre_pas144_readiness_check.py", line 178>:
 178            RESUME                   0

 180            BUILD_LIST               0
                STORE_FAST               1 (out)

 181            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               1 ('.gitignore')
                BINARY_OP               11 (/)
                STORE_FAST               2 (gi_path)

 182            LOAD_FAST_BORROW         2 (gi_path)
                LOAD_ATTR                3 (is_file + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        32 (to L1)
                NOT_TAKEN

 183            LOAD_FAST_BORROW         1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 184            LOAD_CONST               2 ('gitignore:exists')

 185            LOAD_CONST               3 ('FAIL')

 186            LOAD_CONST               4 ('.gitignore present')

 187            LOAD_CONST               5 ('missing at repo root')

 183            CALL                     4
                CALL                     1
                POP_TOP

 189            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 191    L1:     NOP

 192    L2:     LOAD_FAST_BORROW         2 (gi_path)
                LOAD_ATTR                9 (read_text + NULL|self)
                LOAD_CONST               6 ('utf-8')
                LOAD_CONST               7 (('encoding',))
                CALL_KW                  1
                STORE_FAST               3 (text)

 202    L3:     LOAD_FAST                1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 203            LOAD_CONST               2 ('gitignore:exists')

 204            LOAD_CONST              13 ('PASS')

 205            LOAD_CONST               4 ('.gitignore present')

 206            LOAD_FAST                2 (gi_path)
                LOAD_ATTR               16 (name)
                FORMAT_SIMPLE
                LOAD_CONST              14 (' found')
                BUILD_STRING             2

 202            CALL                     4
                CALL                     1
                POP_TOP

 211            LOAD_FAST                3 (text)
                LOAD_ATTR               19 (splitlines + NULL|self)
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      5 (ln)
                SWAP                     2
        L4:     BUILD_SET                0
                SWAP                     2
        L5:     FOR_ITER                81 (to L10)
                STORE_FAST_LOAD_FAST    85 (ln, ln)
                LOAD_ATTR               21 (strip + NULL|self)
                CALL                     0
                TO_BOOL
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           26 (to L5)
        L7:     LOAD_FAST                5 (ln)
                LOAD_ATTR               21 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               23 (startswith + NULL|self)
                LOAD_CONST              15 ('#')
                CALL                     1
                TO_BOOL
        L8:     POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           65 (to L5)
        L9:     LOAD_FAST                5 (ln)
                LOAD_ATTR               21 (strip + NULL|self)
                CALL                     0
                SET_ADD                  2
                JUMP_BACKWARD           83 (to L5)
       L10:     END_FOR
                POP_ITER
       L11:     STORE_FAST               6 (lines)
                STORE_FAST               5 (ln)

 212            LOAD_GLOBAL             24 (REQUIRED_GITIGNORE_PATTERNS)
                GET_ITER
       L12:     FOR_ITER                67 (to L17)
                STORE_FAST               7 (pat)

 213            LOAD_FAST_LOAD_FAST    118 (pat, lines)
                CONTAINS_OP              0 (in)
                STORE_FAST               8 (ok)

 214            LOAD_FAST                1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 215            LOAD_CONST              16 ('gitignore:')
                LOAD_FAST                7 (pat)
                FORMAT_SIMPLE
                BUILD_STRING             2

 216            LOAD_FAST                8 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN
                LOAD_CONST              13 ('PASS')
                JUMP_FORWARD             1 (to L14)
       L13:     LOAD_CONST               3 ('FAIL')

 217   L14:     LOAD_CONST              17 ('.gitignore protects ')
                LOAD_FAST                7 (pat)
                FORMAT_SIMPLE
                BUILD_STRING             2

 218            LOAD_FAST                8 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN
                LOAD_CONST              18 ('pattern present')
                JUMP_FORWARD             6 (to L16)
       L15:     LOAD_CONST              19 ('pattern ')
                LOAD_FAST                7 (pat)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              20 (' missing — append to .gitignore')
                BUILD_STRING             3

 214   L16:     CALL                     4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           69 (to L12)

 212   L17:     END_FOR
                POP_ITER

 220            LOAD_FAST                1 (out)
                RETURN_VALUE

  --   L18:     PUSH_EXC_INFO

 193            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       65 (to L23)
                NOT_TAKEN
                STORE_FAST               4 (e)

 194   L19:     LOAD_FAST                1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 195            LOAD_CONST               8 ('gitignore:readable')

 196            LOAD_CONST               3 ('FAIL')

 197            LOAD_CONST               9 ('.gitignore readable')

 198            LOAD_CONST              10 ('unreadable (')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST              11 (')')
                BUILD_STRING             3

 194            CALL                     4
                CALL                     1
                POP_TOP

 200            LOAD_FAST                1 (out)
       L20:     SWAP                     2
       L21:     POP_EXCEPT
                LOAD_CONST              12 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RETURN_VALUE

  --   L22:     LOAD_CONST              12 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 193   L23:     RERAISE                  0

  --   L24:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L25:     SWAP                     2
                POP_TOP

 211            SWAP                     2
                STORE_FAST               5 (ln)
                RERAISE                  0
ExceptionTable:
  L2 to L3 -> L18 [0]
  L4 to L6 -> L25 [2]
  L7 to L8 -> L25 [2]
  L9 to L11 -> L25 [2]
  L18 to L19 -> L24 [1] lasti
  L19 to L20 -> L22 [1] lasti
  L20 to L21 -> L24 [1] lasti
  L22 to L24 -> L24 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pre_pas144_readiness_check.py", line 223>:
223           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_repository_hygiene at 0x0000018C17F75FB0, file "scripts\pre_pas144_readiness_check.py", line 223>:
  --            MAKE_CELL               10 (lower)

 223            RESUME                   0

 228            BUILD_LIST               0
                STORE_FAST               1 (out)

 229            BUILD_LIST               0
                STORE_FAST               2 (offenders)

 230            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                STORE_FAST               3 (root)

 232            LOAD_GLOBAL              2 (os)
                LOAD_ATTR                4 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         3 (root)
                CALL                     1
                GET_ITER
        L1:     FOR_ITER               232 (to L16)
                UNPACK_SEQUENCE          3
                STORE_FAST_STORE_FAST   69 (dirpath, dirnames)
                STORE_FAST               6 (filenames)

 234            LOAD_FAST_BORROW         5 (dirnames)
                GET_ITER
                LOAD_FAST_AND_CLEAR      7 (d)
                SWAP                     2
        L2:     BUILD_LIST               0
                SWAP                     2
        L3:     FOR_ITER                17 (to L6)
                STORE_FAST_LOAD_FAST   119 (d, d)
                LOAD_GLOBAL              6 (_HYGIENE_SKIP_DIRS)
                CONTAINS_OP              1 (not in)
        L4:     POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           15 (to L3)
        L5:     LOAD_FAST_BORROW         7 (d)
                LIST_APPEND              2
                JUMP_BACKWARD           19 (to L3)
        L6:     END_FOR
                POP_ITER
        L7:     SWAP                     2
                STORE_FAST               7 (d)
                LOAD_FAST_BORROW         5 (dirnames)
                LOAD_CONST               1 (slice(None, None, None))
                STORE_SUBSCR

 236            LOAD_FAST_BORROW         6 (filenames)
                GET_ITER
        L8:     FOR_ITER               187 (to L15)
                STORE_FAST               8 (fname)

 237            LOAD_FAST_BORROW         8 (fname)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_DEREF             10 (lower)

 238            LOAD_GLOBAL             10 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       35 (to L12)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        10 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               2 (<code object <genexpr> at 0x0000018C18052F70, file "scripts\pre_pas144_readiness_check.py", line 238>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_GLOBAL             12 (_DANGEROUS_SUFFIXES)
                GET_ITER
                CALL                     0
        L9:     FOR_ITER                12 (to L11)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L9)
       L10:     POP_ITER
                LOAD_CONST               3 (True)
                JUMP_FORWARD            24 (to L13)
       L11:     END_FOR
                POP_ITER
                LOAD_CONST               4 (False)
                JUMP_FORWARD            20 (to L13)
       L12:     PUSH_NULL
                LOAD_FAST_BORROW        10 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               2 (<code object <genexpr> at 0x0000018C18052F70, file "scripts\pre_pas144_readiness_check.py", line 238>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_GLOBAL             12 (_DANGEROUS_SUFFIXES)
                GET_ITER
                CALL                     0
                CALL                     1
       L13:     TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           93 (to L8)

 239   L14:     LOAD_GLOBAL              2 (os)
                LOAD_ATTR               14 (path)
                LOAD_ATTR               17 (relpath + NULL|self)
                LOAD_GLOBAL              2 (os)
                LOAD_ATTR               14 (path)
                LOAD_ATTR               19 (join + NULL|self)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 72 (dirpath, fname)
                CALL                     2
                LOAD_FAST_BORROW         3 (root)
                CALL                     2
                LOAD_ATTR               21 (replace + NULL|self)
                LOAD_CONST               5 ('\\')
                LOAD_CONST               6 ('/')
                CALL                     2
                STORE_FAST               9 (rel)

 240            LOAD_FAST_BORROW         2 (offenders)
                LOAD_ATTR               23 (append + NULL|self)
                LOAD_FAST_BORROW         9 (rel)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          189 (to L8)

 236   L15:     END_FOR
                POP_ITER
                JUMP_BACKWARD          234 (to L1)

 232   L16:     END_FOR
                POP_ITER

 242            LOAD_FAST_BORROW         2 (offenders)
                TO_BOOL
                POP_JUMP_IF_TRUE        32 (to L17)
                NOT_TAKEN

 243            LOAD_FAST_BORROW         1 (out)
                LOAD_ATTR               23 (append + NULL|self)
                LOAD_GLOBAL             25 (_check + NULL)

 244            LOAD_CONST               7 ('hygiene:no_dangerous_artefacts')

 245            LOAD_CONST               8 ('PASS')

 246            LOAD_CONST               9 ('no tracked backup / archive / dump artefacts')

 247            LOAD_CONST              10 ('filesystem walk clean')

 243            CALL                     4
                CALL                     1
                POP_TOP

 249            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 252   L17:     LOAD_GLOBAL             27 (sorted + NULL)
                LOAD_FAST_BORROW         2 (offenders)
                CALL                     1
                GET_ITER
       L18:     FOR_ITER                38 (to L19)
                STORE_FAST               9 (rel)

 253            LOAD_FAST_BORROW         1 (out)
                LOAD_ATTR               23 (append + NULL|self)
                LOAD_GLOBAL             25 (_check + NULL)

 254            LOAD_CONST              11 ('hygiene:tracked_artefact:')
                LOAD_FAST_BORROW         9 (rel)
                FORMAT_SIMPLE
                BUILD_STRING             2

 255            LOAD_CONST              12 ('FAIL')

 256            LOAD_CONST              13 ('dangerous tracked artefact')

 257            LOAD_FAST_BORROW         9 (rel)
                FORMAT_SIMPLE
                LOAD_CONST              14 (' matches a forbidden extension — remove from working tree')
                BUILD_STRING             2

 253            CALL                     4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           40 (to L18)

 252   L19:     END_FOR
                POP_ITER

 259            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L20:     SWAP                     2
                POP_TOP

 234            SWAP                     2
                STORE_FAST               7 (d)
                RERAISE                  0
ExceptionTable:
  L2 to L4 -> L20 [3]
  L5 to L7 -> L20 [3]

Disassembly of <code object <genexpr> at 0x0000018C18052F70, file "scripts\pre_pas144_readiness_check.py", line 238>:
  --           COPY_FREE_VARS           1

 238           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                22 (to L3)
               STORE_FAST               1 (suf)
               LOAD_DEREF               2 (lower)
               LOAD_ATTR                1 (endswith + NULL|self)
               LOAD_FAST_BORROW         1 (suf)
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           24 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pre_pas144_readiness_check.py", line 270>:
270           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Optional[int]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _safe_coerce_int at 0x0000018C17D8BD50, file "scripts\pre_pas144_readiness_check.py", line 270>:
 270            RESUME                   0

 276            LOAD_FAST_BORROW         0 (value)
                POP_JUMP_IF_NOT_NONE     3 (to L1)
                NOT_TAKEN

 277            LOAD_CONST               1 (None)
                RETURN_VALUE

 278    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL              2 (bool)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L2)
                NOT_TAKEN

 279            LOAD_GLOBAL              5 (int + NULL)
                LOAD_FAST_BORROW         0 (value)
                CALL                     1
                RETURN_VALUE

 280    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL              4 (int)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN

 281            LOAD_FAST_BORROW         0 (value)
                RETURN_VALUE

 282    L3:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL              6 (float)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       49 (to L6)
                NOT_TAKEN

 283            LOAD_FAST_BORROW_LOAD_FAST_BORROW 0 (value, value)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN

 284            LOAD_CONST               1 (None)
                RETURN_VALUE

 285    L4:     LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL              7 (float + NULL)
                LOAD_CONST               2 ('inf')
                CALL                     1
                LOAD_GLOBAL              7 (float + NULL)
                LOAD_CONST               3 ('-inf')
                CALL                     1
                BUILD_TUPLE              2
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

 286            LOAD_CONST               1 (None)
                RETURN_VALUE

 287    L5:     LOAD_GLOBAL              5 (int + NULL)
                LOAD_FAST_BORROW         0 (value)
                CALL                     1
                RETURN_VALUE

 288    L6:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L10)
                NOT_TAKEN

 289            LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                STORE_FAST               1 (s)

 290            LOAD_FAST_BORROW         1 (s)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN

 291            LOAD_CONST               1 (None)
                RETURN_VALUE

 292    L7:     NOP

 293    L8:     LOAD_GLOBAL              5 (int + NULL)
                LOAD_FAST_BORROW         1 (s)
                CALL                     1
        L9:     RETURN_VALUE

 302   L10:     LOAD_CONST               1 (None)
                RETURN_VALUE

  --   L11:     PUSH_EXC_INFO

 294            LOAD_GLOBAL             12 (ValueError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       89 (to L24)
                NOT_TAKEN
                POP_TOP

 295   L12:     NOP

 296   L13:     LOAD_GLOBAL              7 (float + NULL)
                LOAD_FAST                1 (s)
                CALL                     1
                STORE_FAST               2 (f)
       L14:     JUMP_FORWARD            25 (to L20)

  --   L15:     PUSH_EXC_INFO

 297            LOAD_GLOBAL             12 (ValueError)
                LOAD_GLOBAL             14 (OverflowError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L18)
                NOT_TAKEN
                POP_TOP

 298   L16:     POP_EXCEPT
       L17:     POP_EXCEPT
                LOAD_CONST               1 (None)
                RETURN_VALUE

 297   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 299   L20:     LOAD_FAST_LOAD_FAST     34 (f, f)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_TRUE        28 (to L21)
                NOT_TAKEN
                LOAD_FAST                2 (f)
                LOAD_GLOBAL              7 (float + NULL)
                LOAD_CONST               2 ('inf')
                CALL                     1
                LOAD_GLOBAL              7 (float + NULL)
                LOAD_CONST               3 ('-inf')
                CALL                     1
                BUILD_TUPLE              2
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        4 (to L22)
                NOT_TAKEN

 300   L21:     POP_EXCEPT
                LOAD_CONST               1 (None)
                RETURN_VALUE

 301   L22:     LOAD_GLOBAL              5 (int + NULL)
                LOAD_FAST                2 (f)
                CALL                     1
                SWAP                     2
       L23:     POP_EXCEPT
                RETURN_VALUE

 294   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L8 to L9 -> L11 [0]
  L11 to L12 -> L25 [1] lasti
  L13 to L14 -> L15 [1]
  L14 to L15 -> L25 [1] lasti
  L15 to L16 -> L19 [2] lasti
  L16 to L17 -> L25 [1] lasti
  L18 to L19 -> L19 [2] lasti
  L19 to L21 -> L25 [1] lasti
  L22 to L23 -> L25 [1] lasti
  L24 to L25 -> L25 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pre_pas144_readiness_check.py", line 305>:
305           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('default')
              LOAD_CONST               2 ('int')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[int]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _coerce_count at 0x0000018C18025030, file "scripts\pre_pas144_readiness_check.py", line 305>:
305           RESUME                   0

309           LOAD_FAST_BORROW         0 (value)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

310           LOAD_FAST_BORROW         1 (default)
              RETURN_VALUE

311   L1:     LOAD_GLOBAL              1 (_safe_coerce_int + NULL)
              LOAD_FAST_BORROW         0 (value)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "scripts\pre_pas144_readiness_check.py", line 314>:
314           RESUME                   0
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
              LOAD_CONST               6 ('Optional[dict]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _safe_read_json at 0x0000018C179C3A50, file "scripts\pre_pas144_readiness_check.py", line 314>:
 314            RESUME                   0

 315            LOAD_FAST_BORROW         0 (path)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 316            LOAD_CONST               0 (None)
                RETURN_VALUE

 317    L1:     LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (path)
                CALL                     1
                STORE_FAST               2 (p)

 318            LOAD_FAST_BORROW         2 (p)
                LOAD_ATTR                3 (exists + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN

 319            LOAD_CONST               0 (None)
                RETURN_VALUE

 320    L2:     NOP

 321    L3:     LOAD_FAST_BORROW         2 (p)
                LOAD_ATTR                5 (read_text + NULL|self)
                LOAD_CONST               1 ('utf-8')
                LOAD_CONST               2 (('encoding',))
                CALL_KW                  1
                STORE_FAST               3 (text)

 322            LOAD_GLOBAL              6 (json)
                LOAD_ATTR                8 (loads)
                PUSH_NULL
                LOAD_FAST_BORROW         3 (text)
                CALL                     1
                STORE_FAST               4 (loaded)

 323            LOAD_GLOBAL             11 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (loaded)
                LOAD_GLOBAL             12 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (loaded)
        L4:     RETURN_VALUE
        L5:     LOAD_CONST               0 (None)
        L6:     RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 324            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

 325    L8:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 324    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L7 [0]
  L5 to L6 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "scripts\pre_pas144_readiness_check.py", line 328>:
328           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('Optional[dict]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object evaluate_security_report at 0x0000018C17E7E710, file "scripts\pre_pas144_readiness_check.py", line 328>:
328            RESUME                   0

337            LOAD_FAST_BORROW         0 (report)
               POP_JUMP_IF_NOT_NONE    16 (to L1)
               NOT_TAKEN

338            LOAD_GLOBAL              1 (_check + NULL)

339            LOAD_CONST               2 ('security:report')

340            LOAD_CONST               3 ('WARN')

341            LOAD_CONST               4 ('security audit report')

342            LOAD_CONST               5 ('not provided — gate downgraded to PASS_WITH_WARNINGS')

338            CALL                     4
               BUILD_LIST               1
               RETURN_VALUE

345    L1:     LOAD_CONST               1 (None)
               STORE_FAST               1 (sev_dict)

346            LOAD_CONST               1 (None)
               STORE_FAST               2 (shape_used)

347            LOAD_CONST              22 (('counts', 'by_severity', 'severity_counts'))
               GET_ITER
       L2:     FOR_ITER                48 (to L4)
               STORE_FAST               3 (shape)

348            LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_FAST_BORROW         3 (shape)
               CALL                     1
               STORE_FAST               4 (candidate)

349            LOAD_GLOBAL              5 (isinstance + NULL)
               LOAD_FAST_BORROW         4 (candidate)
               LOAD_GLOBAL              6 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               JUMP_BACKWARD           44 (to L2)

350    L3:     LOAD_FAST                4 (candidate)
               STORE_FAST               1 (sev_dict)

351            LOAD_FAST                3 (shape)
               STORE_FAST               2 (shape_used)

352            POP_TOP
               JUMP_FORWARD             2 (to L5)

347    L4:     END_FOR
               POP_ITER

354    L5:     LOAD_FAST_BORROW         1 (sev_dict)
               POP_JUMP_IF_NOT_NONE    16 (to L6)
               NOT_TAKEN

356            LOAD_GLOBAL              1 (_check + NULL)

357            LOAD_CONST               2 ('security:report')

358            LOAD_CONST               6 ('FAIL')

359            LOAD_CONST               7 ('security audit report unreadable')

360            LOAD_CONST               8 ('no severity counts under counts/by_severity/severity_counts — failing closed')

356            CALL                     4
               BUILD_LIST               1
               RETURN_VALUE

363    L6:     LOAD_GLOBAL              9 (_coerce_count + NULL)
               LOAD_FAST_BORROW         1 (sev_dict)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               9 ('CRITICAL')
               CALL                     1
               CALL                     1
               STORE_FAST               5 (crit)

364            LOAD_GLOBAL              9 (_coerce_count + NULL)
               LOAD_FAST_BORROW         1 (sev_dict)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              10 ('HIGH')
               CALL                     1
               CALL                     1
               STORE_FAST               6 (high)

366            LOAD_FAST_BORROW         5 (crit)
               POP_JUMP_IF_NONE         5 (to L7)
               NOT_TAKEN
               LOAD_FAST_BORROW         6 (high)
               POP_JUMP_IF_NOT_NONE    20 (to L8)
               NOT_TAKEN

367    L7:     LOAD_GLOBAL              1 (_check + NULL)

368            LOAD_CONST               2 ('security:report')

369            LOAD_CONST               6 ('FAIL')

370            LOAD_CONST              11 ('security audit report has malformed severity counts')

371            LOAD_CONST              12 ('CRITICAL/HIGH could not be coerced to int (shape=')
               LOAD_FAST_BORROW         2 (shape_used)
               FORMAT_SIMPLE
               LOAD_CONST              13 (') — failing closed')
               BUILD_STRING             3

367            CALL                     4
               BUILD_LIST               1
               RETURN_VALUE

374    L8:     LOAD_FAST_BORROW         5 (crit)
               LOAD_SMALL_INT           0
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_TRUE         8 (to L9)
               NOT_TAKEN
               LOAD_FAST_BORROW         6 (high)
               LOAD_SMALL_INT           0
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE       26 (to L10)
               NOT_TAKEN

375    L9:     LOAD_GLOBAL              1 (_check + NULL)

376            LOAD_CONST               2 ('security:report')

377            LOAD_CONST               6 ('FAIL')

378            LOAD_CONST              14 ('security audit report has CRITICAL/HIGH')

379            LOAD_CONST              15 ('CRITICAL=')
               LOAD_FAST_BORROW         5 (crit)
               FORMAT_SIMPLE
               LOAD_CONST              16 (' HIGH=')
               LOAD_FAST_BORROW         6 (high)
               FORMAT_SIMPLE
               LOAD_CONST              17 (' (shape=')
               LOAD_FAST_BORROW         2 (shape_used)
               FORMAT_SIMPLE
               LOAD_CONST              18 (')')
               BUILD_STRING             7

375            CALL                     4
               BUILD_LIST               1
               RETURN_VALUE

382   L10:     LOAD_GLOBAL              1 (_check + NULL)

383            LOAD_CONST               2 ('security:report')

384            LOAD_CONST              19 ('PASS')

385            LOAD_CONST              20 ('security audit report clean')

386            LOAD_CONST              21 ('CRITICAL=0 HIGH=0 (shape=')
               LOAD_FAST_BORROW         2 (shape_used)
               FORMAT_SIMPLE
               LOAD_CONST              18 (')')
               BUILD_STRING             3

382            CALL                     4
               BUILD_LIST               1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pre_pas144_readiness_check.py", line 390>:
390           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('Optional[dict]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object evaluate_integrity_report at 0x0000018C17F7DED0, file "scripts\pre_pas144_readiness_check.py", line 390>:
390            RESUME                   0

403            LOAD_FAST_BORROW         0 (report)
               POP_JUMP_IF_NOT_NONE    16 (to L1)
               NOT_TAKEN

404            LOAD_GLOBAL              1 (_check + NULL)

405            LOAD_CONST               1 ('integrity:report')

406            LOAD_CONST               2 ('WARN')

407            LOAD_CONST               3 ('integrity check report')

408            LOAD_CONST               4 ('not provided — gate downgraded to PASS_WITH_WARNINGS')

404            CALL                     4
               BUILD_LIST               1
               RETURN_VALUE

411    L1:     BUILD_LIST               0
               STORE_FAST               1 (indicators)

412            BUILD_LIST               0
               STORE_FAST               2 (shapes_seen)

413            BUILD_LIST               0
               STORE_FAST               3 (malformed_shapes)

415            LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               5 ('counts')
               CALL                     1
               STORE_FAST               4 (counts)

416            LOAD_GLOBAL              5 (isinstance + NULL)
               LOAD_FAST_BORROW         4 (counts)
               LOAD_GLOBAL              6 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE      101 (to L3)
               NOT_TAKEN
               LOAD_CONST               6 ('failed')
               LOAD_FAST_BORROW         4 (counts)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       94 (to L3)
               NOT_TAKEN

417            LOAD_GLOBAL              9 (_safe_coerce_int + NULL)
               LOAD_FAST_BORROW         4 (counts)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               6 ('failed')
               CALL                     1
               CALL                     1
               STORE_FAST               5 (v)

418            LOAD_FAST_BORROW         5 (v)
               POP_JUMP_IF_NOT_NONE    19 (to L2)
               NOT_TAKEN

419            LOAD_FAST_BORROW         3 (malformed_shapes)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               7 ('counts.failed')
               CALL                     1
               POP_TOP
               JUMP_FORWARD            88 (to L4)

421    L2:     LOAD_FAST_BORROW         1 (indicators)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (max + NULL)
               LOAD_SMALL_INT           0
               LOAD_FAST_BORROW         5 (v)
               CALL                     2
               CALL                     1
               POP_TOP

422            LOAD_FAST_BORROW         2 (shapes_seen)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               7 ('counts.failed')
               CALL                     1
               POP_TOP
               JUMP_FORWARD            43 (to L4)

423    L3:     LOAD_FAST_BORROW         4 (counts)
               POP_JUMP_IF_NONE        40 (to L4)
               NOT_TAKEN
               LOAD_GLOBAL              5 (isinstance + NULL)
               LOAD_FAST_BORROW         4 (counts)
               LOAD_GLOBAL              6 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L4)
               NOT_TAKEN

424            LOAD_FAST_BORROW         3 (malformed_shapes)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               8 ('counts(non-dict)')
               CALL                     1
               POP_TOP

426    L4:     LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               9 ('summary')
               CALL                     1
               STORE_FAST               6 (summary)

427            LOAD_GLOBAL              5 (isinstance + NULL)
               LOAD_FAST_BORROW         6 (summary)
               LOAD_GLOBAL              6 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE      101 (to L6)
               NOT_TAKEN
               LOAD_CONST               6 ('failed')
               LOAD_FAST_BORROW         6 (summary)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       94 (to L6)
               NOT_TAKEN

428            LOAD_GLOBAL              9 (_safe_coerce_int + NULL)
               LOAD_FAST_BORROW         6 (summary)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               6 ('failed')
               CALL                     1
               CALL                     1
               STORE_FAST               5 (v)

429            LOAD_FAST_BORROW         5 (v)
               POP_JUMP_IF_NOT_NONE    19 (to L5)
               NOT_TAKEN

430            LOAD_FAST_BORROW         3 (malformed_shapes)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              10 ('summary.failed')
               CALL                     1
               POP_TOP
               JUMP_FORWARD            88 (to L7)

432    L5:     LOAD_FAST_BORROW         1 (indicators)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (max + NULL)
               LOAD_SMALL_INT           0
               LOAD_FAST_BORROW         5 (v)
               CALL                     2
               CALL                     1
               POP_TOP

433            LOAD_FAST_BORROW         2 (shapes_seen)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              10 ('summary.failed')
               CALL                     1
               POP_TOP
               JUMP_FORWARD            43 (to L7)

434    L6:     LOAD_FAST_BORROW         6 (summary)
               POP_JUMP_IF_NONE        40 (to L7)
               NOT_TAKEN
               LOAD_GLOBAL              5 (isinstance + NULL)
               LOAD_FAST_BORROW         6 (summary)
               LOAD_GLOBAL              6 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L7)
               NOT_TAKEN

435            LOAD_FAST_BORROW         3 (malformed_shapes)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              11 ('summary(non-dict)')
               CALL                     1
               POP_TOP

437    L7:     LOAD_CONST              12 ('failed_count')
               LOAD_FAST_BORROW         0 (report)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       93 (to L9)
               NOT_TAKEN

438            LOAD_GLOBAL              9 (_safe_coerce_int + NULL)
               LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              12 ('failed_count')
               CALL                     1
               CALL                     1
               STORE_FAST               5 (v)

439            LOAD_FAST_BORROW         5 (v)
               POP_JUMP_IF_NOT_NONE    19 (to L8)
               NOT_TAKEN

440            LOAD_FAST_BORROW         3 (malformed_shapes)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              12 ('failed_count')
               CALL                     1
               POP_TOP
               JUMP_FORWARD            44 (to L9)

442    L8:     LOAD_FAST_BORROW         1 (indicators)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (max + NULL)
               LOAD_SMALL_INT           0
               LOAD_FAST_BORROW         5 (v)
               CALL                     2
               CALL                     1
               POP_TOP

443            LOAD_FAST_BORROW         2 (shapes_seen)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              12 ('failed_count')
               CALL                     1
               POP_TOP

445    L9:     LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              13 ('results')
               CALL                     1
               STORE_FAST               7 (results)

446            LOAD_FAST_BORROW         7 (results)
               POP_JUMP_IF_NOT_NONE    18 (to L10)
               NOT_TAKEN

447            LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              14 ('checks')
               CALL                     1
               STORE_FAST               7 (results)

448   L10:     LOAD_GLOBAL              5 (isinstance + NULL)
               LOAD_FAST_BORROW         7 (results)
               LOAD_GLOBAL             14 (list)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE      200 (to L17)
               NOT_TAKEN

449            LOAD_SMALL_INT           0
               STORE_FAST               8 (result_failures)

450            LOAD_FAST_BORROW         7 (results)
               GET_ITER
      L11:     FOR_ITER               156 (to L16)
               STORE_FAST               9 (r)

451            LOAD_GLOBAL              5 (isinstance + NULL)
               LOAD_FAST_BORROW         9 (r)
               LOAD_GLOBAL              6 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L12)
               NOT_TAKEN

453            LOAD_FAST_BORROW         8 (result_failures)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               8 (result_failures)

454            JUMP_BACKWARD           36 (to L11)

455   L12:     LOAD_CONST              15 (False)
               STORE_FAST              10 (failed_flag)

456            LOAD_FAST_BORROW         9 (r)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              16 ('passed')
               CALL                     1
               LOAD_CONST              15 (False)
               IS_OP                    0 (is)
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN

457            LOAD_CONST              17 (True)
               STORE_FAST              10 (failed_flag)

458   L13:     LOAD_FAST_BORROW         9 (r)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              18 ('status')
               CALL                     1
               STORE_FAST              11 (status)

459            LOAD_GLOBAL              5 (isinstance + NULL)
               LOAD_FAST_BORROW        11 (status)
               LOAD_GLOBAL             16 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       38 (to L14)
               NOT_TAKEN
               LOAD_FAST_BORROW        11 (status)
               LOAD_ATTR               19 (strip + NULL|self)
               CALL                     0
               LOAD_ATTR               21 (upper + NULL|self)
               CALL                     0
               LOAD_CONST              34 (('FAIL', 'FAILED', 'ERROR'))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L14)
               NOT_TAKEN

462            LOAD_CONST              17 (True)
               STORE_FAST              10 (failed_flag)

463   L14:     LOAD_FAST_BORROW        10 (failed_flag)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L15)
               NOT_TAKEN
               JUMP_BACKWARD          147 (to L11)

464   L15:     LOAD_FAST_BORROW         8 (result_failures)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               8 (result_failures)
               JUMP_BACKWARD          158 (to L11)

450   L16:     END_FOR
               POP_ITER

465            LOAD_FAST_BORROW         1 (indicators)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (result_failures)
               CALL                     1
               POP_TOP

466            LOAD_FAST_BORROW         2 (shapes_seen)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              20 ('results[]')
               CALL                     1
               POP_TOP
               JUMP_FORWARD            21 (to L18)

467   L17:     LOAD_FAST_BORROW         7 (results)
               POP_JUMP_IF_NONE        18 (to L18)
               NOT_TAKEN

469            LOAD_FAST_BORROW         3 (malformed_shapes)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              21 ('results(non-list)')
               CALL                     1
               POP_TOP

471   L18:     LOAD_FAST_BORROW         3 (malformed_shapes)
               TO_BOOL
               POP_JUMP_IF_FALSE       20 (to L19)
               NOT_TAKEN

472            LOAD_GLOBAL              1 (_check + NULL)

473            LOAD_CONST               1 ('integrity:report')

474            LOAD_CONST              19 ('FAIL')

475            LOAD_CONST              22 ('integrity check report has malformed shape')

476            LOAD_CONST              23 ('could not coerce: ')
               LOAD_FAST_BORROW         3 (malformed_shapes)
               FORMAT_SIMPLE
               LOAD_CONST              24 (' — failing closed')
               BUILD_STRING             3

472            CALL                     4
               BUILD_LIST               1
               RETURN_VALUE

479   L19:     LOAD_FAST_BORROW         2 (shapes_seen)
               TO_BOOL
               POP_JUMP_IF_TRUE        16 (to L20)
               NOT_TAKEN

481            LOAD_GLOBAL              1 (_check + NULL)

482            LOAD_CONST               1 ('integrity:report')

483            LOAD_CONST              19 ('FAIL')

484            LOAD_CONST              25 ('integrity check report unreadable')

485            LOAD_CONST              26 ('no failure indicator (counts.failed / summary.failed / failed_count / results[]) — failing closed')

481            CALL                     4
               BUILD_LIST               1
               RETURN_VALUE

489   L20:     LOAD_FAST_BORROW         1 (indicators)
               TO_BOOL
               POP_JUMP_IF_FALSE       12 (to L21)
               NOT_TAKEN
               LOAD_GLOBAL             13 (max + NULL)
               LOAD_FAST_BORROW         1 (indicators)
               CALL                     1
               JUMP_FORWARD             1 (to L22)
      L21:     LOAD_SMALL_INT           0
      L22:     STORE_FAST              12 (worst)

490            LOAD_FAST_BORROW        12 (worst)
               LOAD_SMALL_INT           0
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE       23 (to L23)
               NOT_TAKEN

491            LOAD_GLOBAL              1 (_check + NULL)

492            LOAD_CONST               1 ('integrity:report')

493            LOAD_CONST              19 ('FAIL')

494            LOAD_CONST              27 ('integrity check report has failures')

495            LOAD_CONST              28 ('failed=')
               LOAD_FAST_BORROW        12 (worst)
               FORMAT_SIMPLE
               LOAD_CONST              29 (' (shapes=')
               LOAD_FAST_BORROW         2 (shapes_seen)
               FORMAT_SIMPLE
               LOAD_CONST              30 (')')
               BUILD_STRING             5

491            CALL                     4
               BUILD_LIST               1
               RETURN_VALUE

497   L23:     LOAD_GLOBAL              1 (_check + NULL)

498            LOAD_CONST               1 ('integrity:report')

499            LOAD_CONST              31 ('PASS')

500            LOAD_CONST              32 ('integrity check report clean')

501            LOAD_CONST              33 ('no failing checks (shapes=')
               LOAD_FAST_BORROW         2 (shapes_seen)
               FORMAT_SIMPLE
               LOAD_CONST              30 (')')
               BUILD_STRING             3

497            CALL                     4
               BUILD_LIST               1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pre_pas144_readiness_check.py", line 505>:
505           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('Optional[dict]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object evaluate_monitoring_report at 0x0000018C17ECF000, file "scripts\pre_pas144_readiness_check.py", line 505>:
505           RESUME                   0

507           LOAD_FAST_BORROW         0 (report)
              POP_JUMP_IF_NOT_NONE    16 (to L1)
              NOT_TAKEN

508           LOAD_GLOBAL              1 (_check + NULL)

509           LOAD_CONST               1 ('monitoring:report')

510           LOAD_CONST               2 ('WARN')

511           LOAD_CONST               3 ('monitoring report')

512           LOAD_CONST               4 ('not provided — gate downgraded to PASS_WITH_WARNINGS')

508           CALL                     4
              BUILD_LIST               1
              RETURN_VALUE

514   L1:     LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               5 ('safe_to_continue')
              CALL                     1
              STORE_FAST               1 (safe)

515           LOAD_FAST_BORROW         1 (safe)
              LOAD_CONST               6 (True)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE      123 (to L5)
              NOT_TAKEN

516           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               7 ('by_severity')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L2:     STORE_FAST               2 (sev)

517           LOAD_GLOBAL              5 (int + NULL)
              LOAD_FAST_BORROW         2 (sev)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               8 ('CRITICAL')
              LOAD_SMALL_INT           0
              CALL                     2
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              LOAD_SMALL_INT           0
      L3:     CALL                     1
              STORE_FAST               3 (crit)

518           LOAD_GLOBAL              5 (int + NULL)
              LOAD_FAST_BORROW         2 (sev)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               9 ('HIGH')
              LOAD_SMALL_INT           0
              CALL                     2
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              POP_TOP
              LOAD_SMALL_INT           0
      L4:     CALL                     1
              STORE_FAST               4 (high)

519           LOAD_GLOBAL              1 (_check + NULL)

520           LOAD_CONST               1 ('monitoring:report')

521           LOAD_CONST              10 ('PASS')

522           LOAD_CONST              11 ('monitoring safe_to_continue')

523           LOAD_CONST              12 ('CRITICAL=')
              LOAD_FAST_BORROW         3 (crit)
              FORMAT_SIMPLE
              LOAD_CONST              13 (' HIGH=')
              LOAD_FAST_BORROW         4 (high)
              FORMAT_SIMPLE
              BUILD_STRING             4

519           CALL                     4
              BUILD_LIST               1
              RETURN_VALUE

525   L5:     LOAD_GLOBAL              1 (_check + NULL)

526           LOAD_CONST               1 ('monitoring:report')

527           LOAD_CONST              14 ('FAIL')

528           LOAD_CONST              15 ('monitoring not safe_to_continue')

529           LOAD_CONST              16 ('safe_to_continue=')
              LOAD_FAST_BORROW         1 (safe)
              CONVERT_VALUE            2 (repr)
              FORMAT_SIMPLE
              BUILD_STRING             2

525           CALL                     4
              BUILD_LIST               1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts\pre_pas144_readiness_check.py", line 533>:
533           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('Optional[dict]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object evaluate_restore_report at 0x0000018C17F95FD0, file "scripts\pre_pas144_readiness_check.py", line 533>:
533           RESUME                   0

535           LOAD_FAST_BORROW         0 (report)
              POP_JUMP_IF_NOT_NONE    16 (to L1)
              NOT_TAKEN

536           LOAD_GLOBAL              1 (_check + NULL)

537           LOAD_CONST               1 ('restore:report')

538           LOAD_CONST               2 ('WARN')

539           LOAD_CONST               3 ('restore drill report')

540           LOAD_CONST               4 ('not provided — gate downgraded to PASS_WITH_WARNINGS')

536           CALL                     4
              BUILD_LIST               1
              RETURN_VALUE

542   L1:     LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               5 ('restore_success')
              CALL                     1
              STORE_FAST               1 (success)

543           LOAD_FAST_BORROW         1 (success)
              LOAD_CONST               6 (True)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE       16 (to L2)
              NOT_TAKEN

544           LOAD_GLOBAL              1 (_check + NULL)

545           LOAD_CONST               1 ('restore:report')

546           LOAD_CONST               7 ('PASS')

547           LOAD_CONST               8 ('restore drill succeeded')

548           LOAD_CONST               9 ('restore_success=true')

544           CALL                     4
              BUILD_LIST               1
              RETURN_VALUE

550   L2:     LOAD_GLOBAL              1 (_check + NULL)

551           LOAD_CONST               1 ('restore:report')

552           LOAD_CONST              10 ('FAIL')

553           LOAD_CONST              11 ('restore drill failed')

554           LOAD_CONST              12 ('restore_success=')
              LOAD_FAST_BORROW         1 (success)
              CONVERT_VALUE            2 (repr)
              FORMAT_SIMPLE
              BUILD_STRING             2

550           CALL                     4
              BUILD_LIST               1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pre_pas144_readiness_check.py", line 562>:
562           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('checks')
              LOAD_CONST               2 ('List[dict]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('dict')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _aggregate_status at 0x0000018C18060F60, file "scripts\pre_pas144_readiness_check.py", line 562>:
 562            RESUME                   0

 563            LOAD_FAST_BORROW         0 (checks)
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2
        L2:     FOR_ITER                20 (to L5)
                STORE_FAST_LOAD_FAST    17 (c, c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))
        L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           18 (to L2)
        L4:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           22 (to L2)
        L5:     END_FOR
                POP_ITER
        L6:     STORE_FAST               2 (failures)
                STORE_FAST               1 (c)

 564            LOAD_FAST_BORROW         0 (checks)
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L7:     BUILD_LIST               0
                SWAP                     2
        L8:     FOR_ITER                20 (to L11)
                STORE_FAST_LOAD_FAST    17 (c, c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               2 ('WARN')
                COMPARE_OP              88 (bool(==))
        L9:     POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           18 (to L8)
       L10:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           22 (to L8)
       L11:     END_FOR
                POP_ITER
       L12:     STORE_FAST               3 (warnings)
                STORE_FAST               1 (c)

 565            LOAD_FAST_BORROW         2 (failures)
                TO_BOOL
                POP_JUMP_IF_FALSE        4 (to L13)
                NOT_TAKEN

 566            LOAD_CONST               1 ('FAIL')
                STORE_FAST               4 (status)
                JUMP_FORWARD            13 (to L15)

 567   L13:     LOAD_FAST_BORROW         3 (warnings)
                TO_BOOL
                POP_JUMP_IF_FALSE        4 (to L14)
                NOT_TAKEN

 568            LOAD_CONST               3 ('PASS_WITH_WARNINGS')
                STORE_FAST               4 (status)
                JUMP_FORWARD             2 (to L15)

 570   L14:     LOAD_CONST               4 ('PASS')
                STORE_FAST               4 (status)

 572   L15:     LOAD_CONST               0 ('status')
                LOAD_FAST_BORROW         4 (status)

 573            LOAD_CONST               5 ('safe_for_pas144')
                LOAD_FAST_BORROW         4 (status)
                LOAD_CONST               4 ('PASS')
                COMPARE_OP              72 (==)

 574            LOAD_CONST               6 ('failures')
                LOAD_FAST_BORROW         2 (failures)

 575            LOAD_CONST               7 ('warnings')
                LOAD_FAST_BORROW         3 (warnings)

 571            BUILD_MAP                4
                RETURN_VALUE

  --   L16:     SWAP                     2
                POP_TOP

 563            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L17:     SWAP                     2
                POP_TOP

 564            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L16 [2]
  L4 to L6 -> L16 [2]
  L7 to L9 -> L17 [2]
  L10 to L12 -> L17 [2]

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "scripts\pre_pas144_readiness_check.py", line 579>:
579           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('checks')
              LOAD_CONST               4 ('List[dict]')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('List[str]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _operator_actions at 0x0000018C17F7E6A0, file "scripts\pre_pas144_readiness_check.py", line 579>:
 579            RESUME                   0

 581            BUILD_LIST               0
                STORE_FAST               2 (actions)

 582            LOAD_FAST_BORROW         1 (checks)
                GET_ITER
                LOAD_FAST_AND_CLEAR      3 (c)
                SWAP                     2
        L1:     BUILD_SET                0
                SWAP                     2
        L2:     FOR_ITER                27 (to L5)
                STORE_FAST_LOAD_FAST    51 (c, c)
                LOAD_CONST               1 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               2 ('FAIL')
                COMPARE_OP              88 (bool(==))
        L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           18 (to L2)
        L4:     LOAD_FAST_BORROW         3 (c)
                LOAD_CONST               3 ('id')
                BINARY_OP               26 ([])
                SET_ADD                  2
                JUMP_BACKWARD           29 (to L2)
        L5:     END_FOR
                POP_ITER
        L6:     STORE_FAST               4 (fail_ids)
                STORE_FAST               3 (c)

 583            LOAD_FAST_BORROW         1 (checks)
                GET_ITER
                LOAD_FAST_AND_CLEAR      3 (c)
                SWAP                     2
        L7:     BUILD_SET                0
                SWAP                     2
        L8:     FOR_ITER                27 (to L11)
                STORE_FAST_LOAD_FAST    51 (c, c)
                LOAD_CONST               1 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               4 ('WARN')
                COMPARE_OP              88 (bool(==))
        L9:     POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           18 (to L8)
       L10:     LOAD_FAST_BORROW         3 (c)
                LOAD_CONST               3 ('id')
                BINARY_OP               26 ([])
                SET_ADD                  2
                JUMP_BACKWARD           29 (to L8)
       L11:     END_FOR
                POP_ITER
       L12:     STORE_FAST               5 (warn_ids)
                STORE_FAST               3 (c)

 586            LOAD_FAST_BORROW         1 (checks)
                GET_ITER
       L13:     FOR_ITER               150 (to L16)
                STORE_FAST               3 (c)

 587            LOAD_FAST_BORROW         3 (c)
                LOAD_CONST               1 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               2 ('FAIL')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L13)

 588   L14:     LOAD_FAST_BORROW         3 (c)
                LOAD_CONST               3 ('id')
                BINARY_OP               26 ([])
                LOAD_ATTR                1 (startswith + NULL|self)
                LOAD_CONST               5 ('migration:')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        63 (to L15)
                NOT_TAKEN

 589            LOAD_FAST_BORROW         3 (c)
                LOAD_CONST               3 ('id')
                BINARY_OP               26 ([])
                LOAD_ATTR                1 (startswith + NULL|self)
                LOAD_CONST               6 ('script:')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L15)
                NOT_TAKEN

 590            LOAD_FAST_BORROW         3 (c)
                LOAD_CONST               3 ('id')
                BINARY_OP               26 ([])
                LOAD_ATTR                1 (startswith + NULL|self)
                LOAD_CONST               7 ('doc:')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN
                JUMP_BACKWARD          111 (to L13)

 592   L15:     LOAD_FAST_BORROW         2 (actions)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST               8 ('Restore missing file referenced by ')
                LOAD_FAST_BORROW         3 (c)
                LOAD_CONST               3 ('id')
                BINARY_OP               26 ([])
                CONVERT_VALUE            1 (str)
                FORMAT_SIMPLE
                LOAD_CONST               9 (' (')
                LOAD_FAST_BORROW         3 (c)
                LOAD_CONST              10 ('detail')
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST              11 (').')
                BUILD_STRING             5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          152 (to L13)

 586   L16:     END_FOR
                POP_ITER

 594            LOAD_GLOBAL              4 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       28 (to L20)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              12 (<code object <genexpr> at 0x0000018C17FF10B0, file "scripts\pre_pas144_readiness_check.py", line 594>)
                MAKE_FUNCTION

 596            LOAD_FAST_BORROW         4 (fail_ids)
                GET_ITER

 594            CALL                     0
       L17:     FOR_ITER                12 (to L19)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L17)
       L18:     POP_ITER
                LOAD_CONST              13 (True)
                JUMP_FORWARD            17 (to L21)
       L19:     END_FOR
                POP_ITER
                LOAD_CONST              14 (False)
                JUMP_FORWARD            13 (to L21)
       L20:     PUSH_NULL
                LOAD_CONST              12 (<code object <genexpr> at 0x0000018C17FF10B0, file "scripts\pre_pas144_readiness_check.py", line 594>)
                MAKE_FUNCTION

 596            LOAD_FAST_BORROW         4 (fail_ids)
                GET_ITER

 594            CALL                     0
                CALL                     1
       L21:     TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L22)
                NOT_TAKEN

 597            LOAD_FAST_BORROW         2 (actions)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST              15 ('Append missing patterns to .gitignore (see §11 of the readiness doc).')
                CALL                     1
                POP_TOP

 599   L22:     LOAD_GLOBAL              4 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       28 (to L26)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              16 (<code object <genexpr> at 0x0000018C180532D0, file "scripts\pre_pas144_readiness_check.py", line 599>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         4 (fail_ids)
                GET_ITER
                CALL                     0
       L23:     FOR_ITER                12 (to L25)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L24)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L23)
       L24:     POP_ITER
                LOAD_CONST              13 (True)
                JUMP_FORWARD            17 (to L27)
       L25:     END_FOR
                POP_ITER
                LOAD_CONST              14 (False)
                JUMP_FORWARD            13 (to L27)
       L26:     PUSH_NULL
                LOAD_CONST              16 (<code object <genexpr> at 0x0000018C180532D0, file "scripts\pre_pas144_readiness_check.py", line 599>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         4 (fail_ids)
                GET_ITER
                CALL                     0
                CALL                     1
       L27:     TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L28)
                NOT_TAKEN

 600            LOAD_FAST_BORROW         2 (actions)
                LOAD_ATTR                3 (append + NULL|self)

 601            LOAD_CONST              17 ("Remove tracked backup/dump/archive artefacts from the working tree; these patterns are .gitignore'd and must not appear in repo.")

 600            CALL                     1
                POP_TOP

 605   L28:     LOAD_CONST              18 ('security:report')
                LOAD_FAST_BORROW         4 (fail_ids)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       18 (to L29)
                NOT_TAKEN

 606            LOAD_FAST_BORROW         2 (actions)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST              19 ('Resolve CRITICAL/HIGH findings in security_audit_report.json, then re-run the gate.')
                CALL                     1
                POP_TOP

 607   L29:     LOAD_CONST              20 ('integrity:report')
                LOAD_FAST_BORROW         4 (fail_ids)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       18 (to L30)
                NOT_TAKEN

 608            LOAD_FAST_BORROW         2 (actions)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST              21 ('Investigate failing checks in integrity_check_report.json, then re-run the gate.')
                CALL                     1
                POP_TOP

 609   L30:     LOAD_CONST              22 ('monitoring:report')
                LOAD_FAST_BORROW         4 (fail_ids)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       18 (to L31)
                NOT_TAKEN

 610            LOAD_FAST_BORROW         2 (actions)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST              23 ('Address monitoring alerts so safe_to_continue=true, then re-run the gate.')
                CALL                     1
                POP_TOP

 611   L31:     LOAD_CONST              24 ('restore:report')
                LOAD_FAST_BORROW         4 (fail_ids)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       18 (to L32)
                NOT_TAKEN

 612            LOAD_FAST_BORROW         2 (actions)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST              25 ('Re-run the restore drill until restore_success=true, then re-run the gate.')
                CALL                     1
                POP_TOP

 614   L32:     LOAD_CONST              18 ('security:report')
                LOAD_FAST_BORROW         5 (warn_ids)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       18 (to L33)
                NOT_TAKEN

 615            LOAD_FAST_BORROW         2 (actions)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST              26 ('Provide --security-report path to re-evaluate.')
                CALL                     1
                POP_TOP

 616   L33:     LOAD_CONST              20 ('integrity:report')
                LOAD_FAST_BORROW         5 (warn_ids)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       18 (to L34)
                NOT_TAKEN

 617            LOAD_FAST_BORROW         2 (actions)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST              27 ('Provide --integrity-report path to re-evaluate.')
                CALL                     1
                POP_TOP

 618   L34:     LOAD_CONST              22 ('monitoring:report')
                LOAD_FAST_BORROW         5 (warn_ids)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       18 (to L35)
                NOT_TAKEN

 619            LOAD_FAST_BORROW         2 (actions)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST              28 ('Provide --monitoring-report path to re-evaluate.')
                CALL                     1
                POP_TOP

 620   L35:     LOAD_CONST              24 ('restore:report')
                LOAD_FAST_BORROW         5 (warn_ids)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       18 (to L36)
                NOT_TAKEN

 621            LOAD_FAST_BORROW         2 (actions)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST              29 ('Provide --restore-report path to re-evaluate.')
                CALL                     1
                POP_TOP

 623   L36:     LOAD_FAST_BORROW         0 (status)
                LOAD_CONST              30 ('PASS')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       18 (to L37)
                NOT_TAKEN

 624            LOAD_FAST_BORROW         2 (actions)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST              31 ('Initial each line of the §10 sign-off checklist before PAS144 begins.')
                CALL                     1
                POP_TOP

 625   L37:     LOAD_FAST_BORROW         2 (actions)
                RETURN_VALUE

  --   L38:     SWAP                     2
                POP_TOP

 582            SWAP                     2
                STORE_FAST               3 (c)
                RERAISE                  0

  --   L39:     SWAP                     2
                POP_TOP

 583            SWAP                     2
                STORE_FAST               3 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L38 [2]
  L4 to L6 -> L38 [2]
  L7 to L9 -> L39 [2]
  L10 to L12 -> L39 [2]

Disassembly of <code object <genexpr> at 0x0000018C17FF10B0, file "scripts\pre_pas144_readiness_check.py", line 594>:
 594           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 596   L2:     FOR_ITER                73 (to L8)
               STORE_FAST               1 (i)

 594           LOAD_FAST_BORROW         1 (i)
               LOAD_ATTR                1 (startswith + NULL|self)
               LOAD_CONST               0 ('gitignore:')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       44 (to L7)
       L3:     NOT_TAKEN
       L4:     POP_TOP
               LOAD_FAST_BORROW         1 (i)
               LOAD_CONST               1 ('gitignore:exists')
               COMPARE_OP             103 (!=)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       31 (to L7)
       L5:     NOT_TAKEN
       L6:     POP_TOP

 595           LOAD_FAST_BORROW         1 (i)
               LOAD_ATTR                3 (endswith + NULL|self)
               LOAD_GLOBAL              5 (tuple + NULL)
               LOAD_GLOBAL              6 (REQUIRED_GITIGNORE_PATTERNS)
               CALL                     1
               CALL                     1

 594   L7:     YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

 596   L8:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L9:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L9 [0] lasti
  L4 to L5 -> L9 [0] lasti
  L6 to L9 -> L9 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C180532D0, file "scripts\pre_pas144_readiness_check.py", line 599>:
 599           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                21 (to L3)
               STORE_FAST_LOAD_FAST    17 (i, i)
               LOAD_ATTR                1 (startswith + NULL|self)
               LOAD_CONST               0 ('hygiene:tracked_artefact:')
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           23 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pre_pas144_readiness_check.py", line 628>:
628           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _recommended_next_step at 0x0000018C18024930, file "scripts\pre_pas144_readiness_check.py", line 628>:
628           RESUME                   0

629           LOAD_FAST_BORROW         0 (status)
              LOAD_CONST               0 ('PASS')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

630           LOAD_CONST               1 ('Sign off on §10 of docs/pas143i_pre_pas144_readiness_gate.md and proceed to PAS144.')
              RETURN_VALUE

631   L1:     LOAD_FAST_BORROW         0 (status)
              LOAD_CONST               2 ('PASS_WITH_WARNINGS')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

632           LOAD_CONST               3 ('Provide every report (--security/--integrity/--monitoring/--restore) and re-run in --strict mode.')
              RETURN_VALUE

633   L2:     LOAD_CONST               4 ('Resolve every FAIL above, then re-run pre_pas144_readiness_check.py --strict.')
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024F30, file "scripts\pre_pas144_readiness_check.py", line 640>:
640           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')

641           LOAD_CONST               2 ('str')

640           LOAD_CONST               3 ('security_report')

643           LOAD_CONST               4 ('Optional[dict]')

640           LOAD_CONST               5 ('integrity_report')

644           LOAD_CONST               4 ('Optional[dict]')

640           LOAD_CONST               6 ('monitoring_report')

645           LOAD_CONST               4 ('Optional[dict]')

640           LOAD_CONST               7 ('restore_report')

646           LOAD_CONST               4 ('Optional[dict]')

640           LOAD_CONST               8 ('return')

647           LOAD_CONST               9 ('dict')

640           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object evaluate_readiness at 0x0000018C181B3050, file "scripts\pre_pas144_readiness_check.py", line 640>:
 640            RESUME                   0

 649            BUILD_LIST               0
                STORE_FAST               5 (checks)

 650            LOAD_FAST_BORROW         5 (checks)
                LOAD_ATTR                1 (extend + NULL|self)
                LOAD_GLOBAL              3 (check_required_migrations + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                CALL                     1
                POP_TOP

 651            LOAD_FAST_BORROW         5 (checks)
                LOAD_ATTR                1 (extend + NULL|self)
                LOAD_GLOBAL              5 (check_required_scripts + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                CALL                     1
                POP_TOP

 652            LOAD_FAST_BORROW         5 (checks)
                LOAD_ATTR                1 (extend + NULL|self)
                LOAD_GLOBAL              7 (check_required_docs + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                CALL                     1
                POP_TOP

 653            LOAD_FAST_BORROW         5 (checks)
                LOAD_ATTR                1 (extend + NULL|self)
                LOAD_GLOBAL              9 (check_gitignore_patterns + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                CALL                     1
                POP_TOP

 654            LOAD_FAST_BORROW         5 (checks)
                LOAD_ATTR                1 (extend + NULL|self)
                LOAD_GLOBAL             11 (check_repository_hygiene + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                CALL                     1
                POP_TOP

 655            LOAD_FAST_BORROW         5 (checks)
                LOAD_ATTR                1 (extend + NULL|self)
                LOAD_GLOBAL             13 (evaluate_security_report + NULL)
                LOAD_FAST_BORROW         1 (security_report)
                CALL                     1
                CALL                     1
                POP_TOP

 656            LOAD_FAST_BORROW         5 (checks)
                LOAD_ATTR                1 (extend + NULL|self)
                LOAD_GLOBAL             15 (evaluate_integrity_report + NULL)
                LOAD_FAST_BORROW         2 (integrity_report)
                CALL                     1
                CALL                     1
                POP_TOP

 657            LOAD_FAST_BORROW         5 (checks)
                LOAD_ATTR                1 (extend + NULL|self)
                LOAD_GLOBAL             17 (evaluate_monitoring_report + NULL)
                LOAD_FAST_BORROW         3 (monitoring_report)
                CALL                     1
                CALL                     1
                POP_TOP

 658            LOAD_FAST_BORROW         5 (checks)
                LOAD_ATTR                1 (extend + NULL|self)
                LOAD_GLOBAL             19 (evaluate_restore_report + NULL)
                LOAD_FAST_BORROW         4 (restore_report)
                CALL                     1
                CALL                     1
                POP_TOP

 660            LOAD_GLOBAL             21 (_aggregate_status + NULL)
                LOAD_FAST_BORROW         5 (checks)
                CALL                     1
                STORE_FAST               6 (agg)

 662            BUILD_MAP                0
                STORE_FAST               7 (required_files)

 663            LOAD_GLOBAL             23 (_files_present + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                LOAD_GLOBAL             24 (REQUIRED_MIGRATIONS)
                CALL                     2
                LOAD_FAST_BORROW         7 (required_files)
                LOAD_CONST               1 ('migrations')
                STORE_SUBSCR

 664            LOAD_GLOBAL             23 (_files_present + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                LOAD_GLOBAL             26 (REQUIRED_SCRIPTS)
                CALL                     2
                LOAD_FAST_BORROW         7 (required_files)
                LOAD_CONST               2 ('scripts')
                STORE_SUBSCR

 665            LOAD_GLOBAL             23 (_files_present + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                LOAD_GLOBAL             28 (REQUIRED_DOCS)
                CALL                     2
                LOAD_FAST_BORROW         7 (required_files)
                LOAD_CONST               3 ('docs')
                STORE_SUBSCR

 671            LOAD_GLOBAL             31 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               4 ('.gitignore')
                BINARY_OP               11 (/)
                LOAD_ATTR               33 (is_file + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE      208 (to L15)
                NOT_TAKEN

 670            LOAD_GLOBAL             34 (REQUIRED_GITIGNORE_PATTERNS)
                GET_ITER

 666            LOAD_FAST_AND_CLEAR      8 (pat)
                LOAD_FAST_AND_CLEAR      9 (ln)
                SWAP                     3
        L1:     BUILD_MAP                0
                SWAP                     2

 670    L2:     FOR_ITER               188 (to L13)
                STORE_FAST               8 (pat)

 667            LOAD_FAST                8 (pat)

 669            LOAD_GLOBAL             31 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               4 ('.gitignore')
                BINARY_OP               11 (/)
                LOAD_ATTR               33 (is_file + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE      145 (to L11)
                NOT_TAKEN

 667            LOAD_FAST                8 (pat)
                LOAD_GLOBAL             31 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               4 ('.gitignore')
                BINARY_OP               11 (/)
                LOAD_ATTR               37 (read_text + NULL|self)
                LOAD_CONST               5 ('utf-8')
                LOAD_CONST               6 (('encoding',))
                CALL_KW                  1
                LOAD_ATTR               39 (splitlines + NULL|self)
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      9 (ln)
                SWAP                     2
        L3:     BUILD_SET                0
                SWAP                     2
        L4:     FOR_ITER                82 (to L9)
                STORE_FAST               9 (ln)

 668            LOAD_FAST_BORROW         9 (ln)
                LOAD_ATTR               41 (strip + NULL|self)
                CALL                     0
                TO_BOOL

 667    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L4)

 668    L6:     LOAD_FAST_BORROW         9 (ln)
                LOAD_ATTR               41 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               43 (startswith + NULL|self)
                LOAD_CONST               7 ('#')
                CALL                     1
                TO_BOOL

 667    L7:     POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           66 (to L4)
        L8:     LOAD_FAST_BORROW         9 (ln)
                LOAD_ATTR               41 (strip + NULL|self)
                CALL                     0
                SET_ADD                  2
                JUMP_BACKWARD           84 (to L4)
        L9:     END_FOR
                POP_ITER
       L10:     SWAP                     2
                STORE_FAST               9 (ln)
                CONTAINS_OP              0 (in)
                JUMP_FORWARD             1 (to L12)

 669   L11:     LOAD_CONST               8 (False)

 667   L12:     MAP_ADD                  2
                JUMP_BACKWARD          190 (to L2)

 670   L13:     END_FOR
                POP_ITER

 666   L14:     SWAP                     3
                STORE_FAST               9 (ln)
                STORE_FAST               8 (pat)
                JUMP_FORWARD            21 (to L20)

 671   L15:     LOAD_GLOBAL             34 (REQUIRED_GITIGNORE_PATTERNS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      8 (pat)
                SWAP                     2
       L16:     BUILD_MAP                0
                SWAP                     2
       L17:     FOR_ITER                 5 (to L18)
                STORE_FAST_LOAD_FAST   136 (pat, pat)
                LOAD_CONST               8 (False)
                MAP_ADD                  2
                JUMP_BACKWARD            7 (to L17)
       L18:     END_FOR
                POP_ITER
       L19:     SWAP                     2
                STORE_FAST               8 (pat)

 666   L20:     LOAD_FAST_BORROW         7 (required_files)
                LOAD_CONST               9 ('gitignore_patterns')
                STORE_SUBSCR

 674            LOAD_CONST              10 ('security')
                LOAD_FAST_BORROW         1 (security_report)
                LOAD_CONST              11 (None)
                IS_OP                    1 (is not)

 675            LOAD_CONST              12 ('integrity')
                LOAD_FAST_BORROW         2 (integrity_report)
                LOAD_CONST              11 (None)
                IS_OP                    1 (is not)

 676            LOAD_CONST              13 ('monitoring')
                LOAD_FAST_BORROW         3 (monitoring_report)
                LOAD_CONST              11 (None)
                IS_OP                    1 (is not)

 677            LOAD_CONST              14 ('restore')
                LOAD_FAST_BORROW         4 (restore_report)
                LOAD_CONST              11 (None)
                IS_OP                    1 (is not)

 673            BUILD_MAP                4
                STORE_FAST              10 (reports_evaluated)

 681            LOAD_CONST              15 ('status')
                LOAD_FAST_BORROW         6 (agg)
                LOAD_CONST              15 ('status')
                BINARY_OP               26 ([])

 682            LOAD_CONST              16 ('safe_for_pas144')
                LOAD_FAST_BORROW         6 (agg)
                LOAD_CONST              16 ('safe_for_pas144')
                BINARY_OP               26 ([])

 683            LOAD_CONST              17 ('timestamp')
                LOAD_GLOBAL             45 (_now_iso + NULL)
                CALL                     0

 684            LOAD_CONST              18 ('checks')
                LOAD_FAST_BORROW         5 (checks)

 685            LOAD_CONST              19 ('warnings')
                LOAD_FAST_BORROW         6 (agg)
                LOAD_CONST              19 ('warnings')
                BINARY_OP               26 ([])

 686            LOAD_CONST              20 ('failures')
                LOAD_FAST_BORROW         6 (agg)
                LOAD_CONST              20 ('failures')
                BINARY_OP               26 ([])

 687            LOAD_CONST              21 ('required_files')
                LOAD_FAST_BORROW         7 (required_files)

 688            LOAD_CONST              22 ('reports_evaluated')
                LOAD_FAST_BORROW        10 (reports_evaluated)

 689            LOAD_CONST              23 ('operator_actions_required')
                LOAD_GLOBAL             47 (_operator_actions + NULL)
                LOAD_FAST_BORROW         6 (agg)
                LOAD_CONST              15 ('status')
                BINARY_OP               26 ([])
                LOAD_FAST_BORROW         5 (checks)
                CALL                     2

 690            LOAD_CONST              24 ('recommended_next_step')
                LOAD_GLOBAL             49 (_recommended_next_step + NULL)
                LOAD_FAST_BORROW         6 (agg)
                LOAD_CONST              15 ('status')
                BINARY_OP               26 ([])
                CALL                     1

 691            LOAD_CONST              25 ('tool_versions')

 692            LOAD_CONST              26 ('python')
                LOAD_GLOBAL             50 (sys)
                LOAD_ATTR               52 (version)
                LOAD_ATTR               55 (split + NULL|self)
                CALL                     0
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])

 693            LOAD_CONST              27 ('platform')
                LOAD_GLOBAL             50 (sys)
                LOAD_ATTR               56 (platform)

 694            LOAD_CONST              28 ('schema')
                LOAD_CONST              29 ('pas143i.v1')

 691            BUILD_MAP                3

 680            BUILD_MAP               11
                RETURN_VALUE

  --   L21:     SWAP                     2
                POP_TOP

 667            SWAP                     2
                STORE_FAST               9 (ln)
                RERAISE                  0

  --   L22:     SWAP                     2
                POP_TOP

 666            SWAP                     3
                STORE_FAST               9 (ln)
                STORE_FAST               8 (pat)
                RERAISE                  0

  --   L23:     SWAP                     2
                POP_TOP

 671            SWAP                     2
                STORE_FAST               8 (pat)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L22 [3]
  L3 to L5 -> L21 [8]
  L6 to L7 -> L21 [8]
  L8 to L10 -> L21 [8]
  L10 to L14 -> L22 [3]
  L16 to L19 -> L23 [2]
  L21 to L22 -> L22 [3]

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pre_pas144_readiness_check.py", line 703>:
703           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('dict')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _summary_lines at 0x0000018C17E920A0, file "scripts\pre_pas144_readiness_check.py", line 703>:
703           RESUME                   0

704           BUILD_LIST               0
              STORE_FAST               1 (lines)

705           LOAD_FAST_BORROW         1 (lines)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST               0 ('PAS143I READINESS SUMMARY')
              CALL                     1
              POP_TOP

706           LOAD_FAST_BORROW         1 (lines)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST              23 ('-------------------------')
              CALL                     1
              POP_TOP

707           LOAD_FAST_BORROW         1 (lines)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST               1 ('Status: ')
              LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('UNKNOWN')
              CALL                     2
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP

708           LOAD_FAST                1 (lines)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST               4 ('Safe for PAS144: ')
              LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               5 ('safe_for_pas144')
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_CONST               6 ('YES')
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               7 ('NO')
      L2:     FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP

709           LOAD_FAST_BORROW         1 (lines)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST               8 ('')
              CALL                     1
              POP_TOP

710           LOAD_FAST_BORROW         1 (lines)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST               9 ('Checks:')
              CALL                     1
              POP_TOP

711           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              10 ('checks')
              BUILD_LIST               0
              CALL                     2
              GET_ITER
      L3:     FOR_ITER                74 (to L4)
              STORE_FAST               2 (c)

712           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               2 ('status')
              BINARY_OP               26 ([])
              STORE_FAST               3 (tag)

713           LOAD_CONST              11 ('[')
              LOAD_FAST_BORROW         3 (tag)
              FORMAT_SIMPLE
              LOAD_CONST              12 (']')
              BUILD_STRING             3
              STORE_FAST               4 (bracket)

715           LOAD_FAST_BORROW         1 (lines)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST              13 ('  ')
              LOAD_FAST_BORROW         4 (bracket)
              LOAD_CONST              14 ('<6')
              FORMAT_WITH_SPEC
              LOAD_CONST              15 (' ')
              LOAD_FAST_BORROW         2 (c)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              16 ('label')
              LOAD_FAST_BORROW         2 (c)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              17 ('id')
              LOAD_CONST               8 ('')
              CALL                     2
              CALL                     2
              FORMAT_SIMPLE
              BUILD_STRING             4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           76 (to L3)

711   L4:     END_FOR
              POP_ITER

716           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              18 ('operator_actions_required')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L5:     STORE_FAST               5 (actions)

717           LOAD_FAST_BORROW         5 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       79 (to L8)
              NOT_TAKEN

718           LOAD_FAST_BORROW         1 (lines)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST               8 ('')
              CALL                     1
              POP_TOP

719           LOAD_FAST_BORROW         1 (lines)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST              19 ('Operator actions before PAS144:')
              CALL                     1
              POP_TOP

720           LOAD_GLOBAL              5 (enumerate + NULL)
              LOAD_FAST_BORROW         5 (actions)
              LOAD_SMALL_INT           1
              CALL                     2
              GET_ITER
      L6:     FOR_ITER                28 (to L7)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST  103 (i, a)

721           LOAD_FAST_BORROW         1 (lines)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST              13 ('  ')
              LOAD_FAST_BORROW         6 (i)
              FORMAT_SIMPLE
              LOAD_CONST              20 ('. ')
              LOAD_FAST_BORROW         7 (a)
              FORMAT_SIMPLE
              BUILD_STRING             4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           30 (to L6)

720   L7:     END_FOR
              POP_ITER

722   L8:     LOAD_FAST_BORROW         1 (lines)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST               8 ('')
              CALL                     1
              POP_TOP

723           LOAD_FAST_BORROW         1 (lines)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST              21 ('Recommended next: ')
              LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              22 ('recommended_next_step')
              LOAD_CONST               8 ('')
              CALL                     2
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP

724           LOAD_FAST_BORROW         1 (lines)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2790, file "scripts\pre_pas144_readiness_check.py", line 727>:
727           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('dict')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object render_summary at 0x0000018C1812C7A0, file "scripts\pre_pas144_readiness_check.py", line 727>:
727           RESUME                   0

728           LOAD_CONST               0 ('\n')
              LOAD_ATTR                1 (join + NULL|self)
              LOAD_GLOBAL              3 (_summary_lines + NULL)
              LOAD_FAST_BORROW         0 (report)
              CALL                     1
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pre_pas144_readiness_check.py", line 735>:
735           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D58AC0, file "scripts\pre_pas144_readiness_check.py", line 735>:
 735            RESUME                   0

 736            LOAD_GLOBAL              0 (argparse)
                LOAD_ATTR                2 (ArgumentParser)
                PUSH_NULL

 737            LOAD_CONST               0 ('pre_pas144_readiness_check')

 738            LOAD_CONST               1 ('PAS143I — pre-PAS144 operator readiness gate.')

 736            LOAD_CONST               2 (('prog', 'description'))
                CALL_KW                  2
                STORE_FAST               1 (parser)

 740            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 741            LOAD_CONST               3 ('--repo-root')

 742            LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

 743            LOAD_CONST               4 ('Repository root to evaluate (default: parent of scripts/).')

 740            LOAD_CONST               5 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 745            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 746            LOAD_CONST               6 ('--security-report')

 747            LOAD_CONST               7 (None)

 748            LOAD_CONST               8 ('Path to security_audit_report.json (optional).')

 745            LOAD_CONST               5 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 750            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 751            LOAD_CONST               9 ('--integrity-report')

 752            LOAD_CONST               7 (None)

 753            LOAD_CONST              10 ('Path to integrity_check_report.json (optional).')

 750            LOAD_CONST               5 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 755            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 756            LOAD_CONST              11 ('--monitoring-report')

 757            LOAD_CONST               7 (None)

 758            LOAD_CONST              12 ('Path to monitoring_report.json (optional).')

 755            LOAD_CONST               5 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 760            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 761            LOAD_CONST              13 ('--restore-report')

 762            LOAD_CONST               7 (None)

 763            LOAD_CONST              14 ('Path to restore_drill_report.json (optional).')

 760            LOAD_CONST               5 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 765            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 766            LOAD_CONST              15 ('--json')

 767            LOAD_CONST              16 ('store_true')

 768            LOAD_CONST              17 ('Emit the readiness report as JSON instead of the human view.')

 765            LOAD_CONST              18 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 770            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 771            LOAD_CONST              19 ('--strict')

 772            LOAD_CONST              16 ('store_true')

 773            LOAD_CONST              20 ('Exit 1 unless status == PASS (PASS_WITH_WARNINGS also exits 1).')

 770            LOAD_CONST              18 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 775            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 776            LOAD_CONST              21 ('--output')

 777            LOAD_CONST               7 (None)

 778            LOAD_CONST              22 ('Path to write pre_pas144_readiness_report.json (default: CWD).')

 775            LOAD_CONST               5 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 780            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                9 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 782            LOAD_GLOBAL             11 (_safe_read_json + NULL)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               12 (security_report)
                LOAD_CONST              23 ('security report')
                CALL                     2
                STORE_FAST               3 (sec)

 783            LOAD_GLOBAL             11 (_safe_read_json + NULL)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               14 (integrity_report)
                LOAD_CONST              24 ('integrity report')
                CALL                     2
                STORE_FAST               4 (integ)

 784            LOAD_GLOBAL             11 (_safe_read_json + NULL)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               16 (monitoring_report)
                LOAD_CONST              25 ('monitoring report')
                CALL                     2
                STORE_FAST               5 (mon)

 785            LOAD_GLOBAL             11 (_safe_read_json + NULL)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               18 (restore_report)
                LOAD_CONST              26 ('restore drill report')
                CALL                     2
                STORE_FAST               6 (drill)

 787            LOAD_GLOBAL             21 (evaluate_readiness + NULL)

 788            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               22 (repo_root)

 789            LOAD_FAST_BORROW         3 (sec)

 790            LOAD_FAST_BORROW         4 (integ)

 791            LOAD_FAST_BORROW         5 (mon)

 792            LOAD_FAST_BORROW         6 (drill)

 787            LOAD_CONST              27 (('repo_root', 'security_report', 'integrity_report', 'monitoring_report', 'restore_report'))
                CALL_KW                  5
                STORE_FAST               7 (report)

 795            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               24 (output)
                TO_BOOL
                POP_JUMP_IF_FALSE       22 (to L1)
                NOT_TAKEN
                LOAD_GLOBAL             27 (Path + NULL)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               24 (output)
                CALL                     1
                JUMP_FORWARD            27 (to L2)
        L1:     LOAD_GLOBAL             26 (Path)
                LOAD_ATTR               28 (cwd)
                PUSH_NULL
                CALL                     0
                LOAD_CONST              28 ('pre_pas144_readiness_report.json')
                BINARY_OP               11 (/)
        L2:     STORE_FAST               8 (out_path)

 796            NOP

 797    L3:     LOAD_FAST_BORROW         8 (out_path)
                LOAD_ATTR               31 (write_text + NULL|self)
                LOAD_GLOBAL             32 (json)
                LOAD_ATTR               34 (dumps)
                PUSH_NULL
                LOAD_FAST_BORROW         7 (report)
                LOAD_SMALL_INT           2
                LOAD_CONST              29 (('indent',))
                CALL_KW                  2
                LOAD_CONST              30 ('utf-8')
                LOAD_CONST              31 (('encoding',))
                CALL_KW                  2
                POP_TOP

 801    L4:     LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               32 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L5)
                NOT_TAKEN

 802            LOAD_GLOBAL             39 (print + NULL)
                LOAD_GLOBAL             32 (json)
                LOAD_ATTR               34 (dumps)
                PUSH_NULL
                LOAD_FAST_BORROW         7 (report)
                LOAD_SMALL_INT           2
                LOAD_CONST              29 (('indent',))
                CALL_KW                  2
                CALL                     1
                POP_TOP
                JUMP_FORWARD            34 (to L6)

 804    L5:     LOAD_GLOBAL             39 (print + NULL)
                LOAD_GLOBAL             49 (render_summary + NULL)
                LOAD_FAST_BORROW         7 (report)
                CALL                     1
                CALL                     1
                POP_TOP

 805            LOAD_GLOBAL             39 (print + NULL)
                LOAD_CONST              35 ('  report: ')
                LOAD_FAST_BORROW         8 (out_path)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 807    L6:     LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               50 (strict)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L7)
                NOT_TAKEN
                LOAD_FAST_BORROW         7 (report)
                LOAD_ATTR               53 (get + NULL|self)
                LOAD_CONST              36 ('status')
                CALL                     1
                LOAD_CONST              37 ('PASS')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN

 808            LOAD_SMALL_INT           1
                RETURN_VALUE

 809    L7:     LOAD_FAST_BORROW         7 (report)
                LOAD_ATTR               53 (get + NULL|self)
                LOAD_CONST              36 ('status')
                CALL                     1
                LOAD_CONST              38 ('FAIL')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN

 810            LOAD_SMALL_INT           1
                RETURN_VALUE

 811    L8:     LOAD_SMALL_INT           0
                RETURN_VALUE

  --    L9:     PUSH_EXC_INFO

 798            LOAD_GLOBAL             36 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       63 (to L13)
                NOT_TAKEN
                STORE_FAST               9 (e)

 799   L10:     LOAD_GLOBAL             39 (print + NULL)
                LOAD_CONST              32 ('  [warn] could not write ')
                LOAD_FAST                8 (out_path)
                FORMAT_SIMPLE
                LOAD_CONST              33 (': ')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             4
                LOAD_GLOBAL             44 (sys)
                LOAD_ATTR               46 (stderr)
                LOAD_CONST              34 (('file',))
                CALL_KW                  2
                POP_TOP
       L11:     POP_EXCEPT
                LOAD_CONST               7 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                JUMP_BACKWARD_NO_INTERRUPT 222 (to L4)

  --   L12:     LOAD_CONST               7 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 798   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L9 [0]
  L9 to L10 -> L14 [1] lasti
  L10 to L11 -> L12 [1] lasti
  L12 to L14 -> L14 [1] lasti
```
