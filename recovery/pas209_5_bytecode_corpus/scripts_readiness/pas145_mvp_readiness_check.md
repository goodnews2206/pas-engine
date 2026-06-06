# scripts_readiness/pas145_mvp_readiness_check

- **pyc:** `scripts\__pycache__\pas145_mvp_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas145_mvp_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas145_mvp_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS145 — MVP operator readiness gate.

Deterministic, non-mutating evaluator for "is this checkout ready for
a brokerage MVP demo?". Walks the repo, confirms the runtime
substrate, the PAS144 memory substrate, the safety/readiness
substrate, and the demo surface, then emits a verdict
(READY_FOR_DEMO / READY_WITH_GAPS / NOT_READY) plus a machine-
readable ``pas145_mvp_readiness_report.json``.

This script never:
  * modifies files,
  * calls Supabase,
  * reads .env / secrets,
  * includes payload values in the report or summary,
  * touches the off-limits ``scripts/combined_supabase_migration.sql``.

It pairs with:
  * ``docs/pas145_operational_mvp_gap_audit.md`` — narrative source
    of truth for what counts as "ready";
  * ``docs/pas145_brokerage_demo_runbook.md`` — operator playbook;
  * ``docs/pas145_demo_scenario_manifest.md`` — demo narrative.

Usage:
  python scripts/pas145_mvp_readiness_check.py
  python scripts/pas145_mvp_readiness_check.py --strict
  python scripts/pas145_mvp_readiness_check.py --json
  python scripts/pas145_mvp_readiness_check.py --summary-only

Exit codes:
    0  — READY_FOR_DEMO (or READY_WITH_GAPS without --strict)
    1  — NOT_READY, or --strict and status != READY_FOR_DEMO
    2  — bad CLI arguments
```

## Imports

`Iterable`, `List`, `Optional`, `Path`, `Tuple`, `__future__`, `annotations`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_aggregate_status`, `_build_parser`, `_check`, `_check_files`, `_files_present`, `_now_iso`, `_operator_actions`, `_print_summary`, `_write_report`, `check_env_var_documentation`, `check_offlimits_present`, `check_optional_demo_surface`, `check_optional_docs`, `check_repository_hygiene`, `check_required_docs`, `check_required_memory`, `check_required_memory_clis`, `check_required_migrations`, `check_required_runtime`, `check_required_safety`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `GAP`, `INFO`, `NOT_READY`, `OFFLIMITS_FILES`, `OPTIONAL_DEMO_SURFACE`, `OPTIONAL_DOCS`, `PAS145`, `PASS`, `READY_FOR_DEMO`, `READY_WITH_GAPS`, `REQUIRED_DOCS`, `REQUIRED_ENV_VAR_NAMES`, `REQUIRED_MEMORY`, `REQUIRED_MEMORY_CLIS`, `REQUIRED_MIGRATIONS`, `REQUIRED_RUNTIME`, `REQUIRED_SAFETY`

## String constants (redacted where noted)

- '\nPAS145 — MVP operator readiness gate.\n\nDeterministic, non-mutating evaluator for "is this checkout ready for\na brokerage MVP demo?". Walks the repo, confirms the runtime\nsubstrate, the PAS144 memory substrate, the safety/readiness\nsubstrate, and the demo surface, then emits a verdict\n(READY_FOR_DEMO / READY_WITH_GAPS / NOT_READY) plus a machine-\nreadable ``pas145_mvp_readiness_report.json``.\n\nThis script never:\n  * modifies files,\n  * calls Supabase,\n  * reads .env / secrets,\n  * includes payload values in the report or summary,\n  * touches the off-limits ``scripts/combined_supabase_migration.sql``.\n\nIt pairs with:\n  * ``docs/pas145_operational_mvp_gap_audit.md`` — narrative source\n    of truth for what counts as "ready";\n  * ``docs/pas145_brokerage_demo_runbook.md`` — operator playbook;\n  * ``docs/pas145_demo_scenario_manifest.md`` — demo narrative.\n\nUsage:\n  python scripts/pas145_mvp_readiness_check.py\n  python scripts/pas145_mvp_readiness_check.py --strict\n  python scripts/pas145_mvp_readiness_check.py --json\n  python scripts/pas145_mvp_readiness_check.py --summary-only\n\nExit codes:\n    0  — READY_FOR_DEMO (or READY_WITH_GAPS without --strict)\n    1  — NOT_READY, or --strict and status != READY_FOR_DEMO\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'READY_FOR_DEMO'
- 'READY_WITH_GAPS'
- 'NOT_READY'
- 'Tuple[str, ...]'
- 'REQUIRED_RUNTIME'
- 'REQUIRED_MEMORY'
- 'REQUIRED_SAFETY'
- 'REQUIRED_MEMORY_CLIS'
- 'REQUIRED_MIGRATIONS'
- 'REQUIRED_DOCS'
- 'OPTIONAL_DEMO_SURFACE'
- 'OPTIONAL_DOCS'
- 'REQUIRED_ENV_VAR_NAMES'
- 'OFFLIMITS_FILES'
- '_DANGEROUS_SUFFIXES'
- '_DANGEROUS_TOPLEVEL'
- 'frozenset'
- '_HYGIENE_SKIP_DIRS'
- 'BLOCK'
- 'GAP'
- 'INFO'
- 'severity'
- 'detail'
- 'pas145_mvp_readiness_report.json'
- 'check_id'
- 'str'
- 'status'
- 'label'
- 'return'
- 'dict'
- "Return a structural check dict. Status is 'PASS' | 'FAIL'.\n\n`severity` controls how a failure rolls up:\n  * BLOCK — fails → NOT_READY\n  * GAP   — fails → READY_WITH_GAPS at worst\n  * INFO  — never gates the verdict (purely informational)\n"
- 'seconds'
- 'repo_root'
- 'rel_paths'
- 'Iterable[str]'
- 'paths'
- 'prefix'
- 'label_prefix'
- 'List[dict]'
- 'PASS'
- 'FAIL'
- 'present'
- 'missing at '
- 'runtime'
- 'memory'
- 'memory module'
- 'safety'
- 'safety script'
- 'memory_cli'
- 'memory CLI'
- 'migration'
- 'doc'
- 'demo'
- 'demo surface'
- 'optional_doc'
- 'optional doc'
- 'Off-limits files are policy: they must stay present and\nuntouched. We only check presence here (the "untouched" half is\na code-review policy, not a runtime check). Missing → BLOCK; the\noperator probably deleted something they shouldn\'t have.'
- 'offlimits'
- 'off-limits file'
- 'Walk .env.example and confirm every required env-var NAME is\nmentioned. We do NOT read .env, never echo values, and never\nfail the gate on a value being unset — only on documentation\nbeing missing.\n'
- '.env.example'
- 'env:example_present'
- '.env.example present'
- "missing at repo root — demo operators can't configure"
- 'env:example_readable'
- '.env.example readable'
- 'unreadable ('
- 'found'
- 'env:'
- '.env.example documents '
- 'documented'
- 'missing from .env.example'
- 'Flag tracked backup/archive/dump artefacts outside the\nwell-known staging dirs, plus dangerous top-level report files\nat the repo root.'
- 'hygiene:no_dangerous_artefacts'
- 'no tracked backup / archive / dump artefacts'
- 'filesystem walk clean'
- 'hygiene:tracked_artefact:'
- 'dangerous tracked artefact'
- ' — remove from working tree'
- 'checks'
- 'verdict'
- 'blockers'
- 'gaps'
- 'failures'
- 'List[str]'
- 'Surface human-readable next steps. No secret values.'
- '[BLOCK] Restore missing file referenced by '
- 'migration:'
- '[BLOCK] Migration proposal missing: '
- ' — recreate from PAS144 phase notes ('
- 'doc:'
- '[BLOCK] Required doc missing: '
- ' — author or restore ('
- 'offlimits:'
- '[BLOCK] Off-limits file missing: '
- ' — restore from git history; do not modify ('
- 'demo:'
- '[GAP] Demo surface missing: '
- ' — restore before live demo ('
- 'optional_doc:'
- '[GAP] Optional doc missing: '
- ' — author when convenient ('
- '[GAP] .env.example documentation issue: '
- '[BLOCK] Repo hygiene: '
- ' — remove the file before committing.'
- ' — '
- 'see report for context'
- 'Run every check and return the full report dict.'
- 'phase'
- 'PAS145'
- 'generated_at'
- 'ready_for_demo'
- 'blocker_count'
- 'gap_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas145_mvp_readiness_check'
- 'PAS145 — Evaluate brokerage-MVP demo readiness. Read-only. Does not touch Supabase, .env, or any tenant data.'
- '--repo-root'
- 'Repo root to evaluate (default: parent of this script).'
- '--output'
- 'Where to write the JSON report (default ./'
- '--json'
- 'store_true'
- 'Emit the report JSON on stdout in addition to the file.'
- '--summary-only'
- 'Skip writing the full report file; print verdict only.'
- '--strict'
- 'Exit 1 unless verdict == READY_FOR_DEMO.'
- 'report'
- 'None'
- '[PAS145] verdict='
- ' blockers='
- ' gaps='
- ' checks='
- ' pass='
- ' fail='
- '[PAS145] operator actions:'
- '  - '
- '  ... and '
- ' more (see report file)'
- 'path'
- 'payload'
- '  [warn] failed to write report at '
- 'argv'
- 'Optional[List[str]]'
- 'int'
- 'error: --repo-root not a directory: '

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS145 — MVP operator readiness gate.\n\nDeterministic, non-mutating evaluator for "is this checkout ready for\na brokerage MVP demo?". Walks the repo, confirms the runtime\nsubstrate, the PAS144 memory substrate, the safety/readiness\nsubstrate, and the demo surface, then emits a verdict\n(READY_FOR_DEMO / READY_WITH_GAPS / NOT_READY) plus a machine-\nreadable ``pas145_mvp_readiness_report.json``.\n\nThis script never:\n  * modifies files,\n  * calls Supabase,\n  * reads .env / secrets,\n  * includes payload values in the report or summary,\n  * touches the off-limits ``scripts/combined_supabase_migration.sql``.\n\nIt pairs with:\n  * ``docs/pas145_operational_mvp_gap_audit.md`` — narrative source\n    of truth for what counts as "ready";\n  * ``docs/pas145_brokerage_demo_runbook.md`` — operator playbook;\n  * ``docs/pas145_demo_scenario_manifest.md`` — demo narrative.\n\nUsage:\n  python scripts/pas145_mvp_readiness_check.py\n  python scripts/pas145_mvp_readiness_check.py --strict\n  python scripts/pas145_mvp_readiness_check.py --json\n  python scripts/pas145_mvp_readiness_check.py --summary-only\n\nExit codes:\n    0  — READY_FOR_DEMO (or READY_WITH_GAPS without --strict)\n    1  — NOT_READY, or --strict and status != READY_FOR_DEMO\n    2  — bad CLI arguments\n')
               STORE_NAME               1 (__doc__)

  36           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  38           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (argparse)
               STORE_NAME               4 (argparse)

  39           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (json)
               STORE_NAME               5 (json)

  40           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (os)
               STORE_NAME               6 (os)

  41           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (sys)
               STORE_NAME               7 (sys)

  42           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              8 (datetime)
               IMPORT_FROM              8 (datetime)
               STORE_NAME               8 (datetime)
               IMPORT_FROM              9 (timezone)
               STORE_NAME               9 (timezone)
               POP_TOP

  43           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME             10 (pathlib)
               IMPORT_FROM             11 (Path)
               STORE_NAME              11 (Path)
               POP_TOP

  44           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('Iterable', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME             12 (typing)
               IMPORT_FROM             13 (Iterable)
               STORE_NAME              13 (Iterable)
               IMPORT_FROM             14 (List)
               STORE_NAME              14 (List)
               IMPORT_FROM             15 (Optional)
               STORE_NAME              15 (Optional)
               IMPORT_FROM             16 (Tuple)
               STORE_NAME              16 (Tuple)
               POP_TOP

  49           LOAD_NAME                7 (sys)
               LOAD_ATTR               34 (stdout)
               LOAD_NAME                7 (sys)
               LOAD_ATTR               36 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              19 (_stream)

  50           NOP

  51   L2:     LOAD_NAME               19 (_stream)
               LOAD_ATTR               41 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  49   L4:     END_FOR
               POP_ITER

  56           LOAD_NAME                6 (os)
               LOAD_ATTR               44 (path)
               LOAD_ATTR               47 (abspath + NULL|self)

  57           LOAD_NAME                6 (os)
               LOAD_ATTR               44 (path)
               LOAD_ATTR               49 (join + NULL|self)
               LOAD_NAME                6 (os)
               LOAD_ATTR               44 (path)
               LOAD_ATTR               51 (dirname + NULL|self)
               LOAD_NAME               26 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  56           CALL                     1
               STORE_NAME              27 (_REPO_ROOT_DEFAULT)

  65           LOAD_CONST               9 ('READY_FOR_DEMO')
               STORE_NAME              28 (VERDICT_READY_FOR_DEMO)

  66           LOAD_CONST              10 ('READY_WITH_GAPS')
               STORE_NAME              29 (VERDICT_READY_WITH_GAPS)

  67           LOAD_CONST              11 ('NOT_READY')
               STORE_NAME              30 (VERDICT_NOT_READY)

  81           LOAD_CONST              79 (('app/main.py', 'app/config.py', 'app/engine/state_machine.py', 'app/routes/twilio_webhook.py', 'app/routes/outbound.py', 'app/routes/websocket_handler.py', 'app/routes/portal.py', 'app/routes/admin.py', 'app/routes/events.py', 'app/routes/simulate.py', 'app/db/supabase_client.py', 'app/db/brokerage_store.py', 'app/db/call_logger.py', 'app/db/lead_memory.py', 'app/db/event_logger.py', 'app/db/booking_store.py', 'app/db/audit_log.py', 'app/services/llm/claude_client.py', 'app/services/booking/calcom_client.py', 'app/services/events/contract.py'))
               STORE_NAME              31 (REQUIRED_RUNTIME)
               LOAD_CONST              12 ('Tuple[str, ...]')
               LOAD_NAME               32 (__annotations__)
               LOAD_CONST              13 ('REQUIRED_RUNTIME')
               STORE_SUBSCR

 111           LOAD_CONST              80 (('app/services/memory/contracts.py', 'app/services/memory/governance.py', 'app/services/memory/classifier.py', 'app/services/memory/store.py', 'app/services/memory/queries.py', 'app/services/memory/audit.py', 'app/services/memory/review.py', 'app/services/memory/diagnostics.py', 'app/services/memory/formatter.py', 'app/services/memory/ranking.py', 'app/services/memory/retrieval.py', 'app/services/memory/sweeper.py', 'app/services/memory/injection.py', 'app/services/memory/queue.py', 'app/services/memory/impact.py', 'app/services/memory/rollout.py', 'app/services/memory/approval.py', 'app/services/memory/rollout_ledger.py', 'app/services/memory/manifest_store.py', 'app/services/memory/batch_rollout.py'))
               STORE_NAME              33 (REQUIRED_MEMORY)
               LOAD_CONST              12 ('Tuple[str, ...]')
               LOAD_NAME               32 (__annotations__)
               LOAD_CONST              14 ('REQUIRED_MEMORY')
               STORE_SUBSCR

 142           LOAD_CONST              81 (('scripts/backup_database.py', 'scripts/verify_backup.py', 'scripts/package_backup.py', 'scripts/restore_drill.py', 'scripts/security_audit.py', 'scripts/integrity_check.py', 'scripts/run_monitoring_check.py', 'scripts/pre_pas144_readiness_check.py'))
               STORE_NAME              34 (REQUIRED_SAFETY)
               LOAD_CONST              12 ('Tuple[str, ...]')
               LOAD_NAME               32 (__annotations__)
               LOAD_CONST              15 ('REQUIRED_SAFETY')
               STORE_SUBSCR

 154           LOAD_CONST              82 (('scripts/memory_diagnostics.py', 'scripts/memory_expiration_sweep.py', 'scripts/memory_impact_report.py', 'scripts/memory_rollout_plan.py', 'scripts/apply_memory_rollout_plan.py', 'scripts/memory_rollout_history.py', 'scripts/memory_batch_rollout_plan.py'))
               STORE_NAME              35 (REQUIRED_MEMORY_CLIS)
               LOAD_CONST              12 ('Tuple[str, ...]')
               LOAD_NAME               32 (__annotations__)
               LOAD_CONST              16 ('REQUIRED_MEMORY_CLIS')
               STORE_SUBSCR

 165           LOAD_CONST              83 (('scripts/migrate_v8_event_contract.sql', 'scripts/migrate_v9_column_privileges.sql', 'scripts/migrate_v10_memory_store.sql', 'scripts/migrate_v11_memory_review_audit.sql', 'scripts/migrate_v12_memory_rollout_ledger.sql', 'scripts/migrate_v13_memory_rollout_manifests.sql'))
               STORE_NAME              36 (REQUIRED_MIGRATIONS)
               LOAD_CONST              12 ('Tuple[str, ...]')
               LOAD_NAME               32 (__annotations__)
               LOAD_CONST              17 ('REQUIRED_MIGRATIONS')
               STORE_SUBSCR

 174           LOAD_CONST              84 (('docs/pas143d_data_durability_runbook.md', 'docs/pas143e_security_integrity_audit.md', 'docs/pas143g_restore_drill_runbook.md', 'docs/pas143h_rls_column_privilege_audit.md', 'docs/pas143i_pre_pas144_readiness_gate.md', 'docs/pas144a_memory_contracts.md', 'docs/pas145_operational_mvp_gap_audit.md', 'docs/pas145_brokerage_demo_runbook.md', 'docs/pas145_demo_scenario_manifest.md'))
               STORE_NAME              37 (REQUIRED_DOCS)
               LOAD_CONST              12 ('Tuple[str, ...]')
               LOAD_NAME               32 (__annotations__)
               LOAD_CONST              18 ('REQUIRED_DOCS')
               STORE_SUBSCR

 187           LOAD_CONST              85 (('scripts/seed_demo_brokerage.py', 'scripts/wf_seed_demo_call.py', 'scripts/run_simulations.py', 'app/static/dashboard/index.html', '.env.example'))
               STORE_NAME              38 (OPTIONAL_DEMO_SURFACE)
               LOAD_CONST              12 ('Tuple[str, ...]')
               LOAD_NAME               32 (__annotations__)
               LOAD_CONST              19 ('OPTIONAL_DEMO_SURFACE')
               STORE_SUBSCR

 196           LOAD_CONST              86 (('docs/pas136_dashboard_rebuild_plan.md', 'docs/pas138_sales_demo_checklist.md'))
               STORE_NAME              39 (OPTIONAL_DOCS)
               LOAD_CONST              12 ('Tuple[str, ...]')
               LOAD_NAME               32 (__annotations__)
               LOAD_CONST              20 ('OPTIONAL_DOCS')
               STORE_SUBSCR

 204           LOAD_CONST              87 (('SUPABASE_URL', 'SUPABASE_SERVICE_KEY', 'TWILIO_ACCOUNT_SID', 'TWILIO_AUTH_TOKEN', 'TWILIO_PHONE_NUMBER', 'DEEPGRAM_API_KEY', 'ELEVENLABS_API_KEY', 'ELEVENLABS_VOICE_ID', 'CALCOM_API_KEY', 'LLM_PROVIDER'))
               STORE_NAME              40 (REQUIRED_ENV_VAR_NAMES)
               LOAD_CONST              12 ('Tuple[str, ...]')
               LOAD_NAME               32 (__annotations__)
               LOAD_CONST              21 ('REQUIRED_ENV_VAR_NAMES')
               STORE_SUBSCR

 222           LOAD_CONST              88 (('scripts/combined_supabase_migration.sql',))
               STORE_NAME              41 (OFFLIMITS_FILES)
               LOAD_CONST              12 ('Tuple[str, ...]')
               LOAD_NAME               32 (__annotations__)
               LOAD_CONST              22 ('OFFLIMITS_FILES')
               STORE_SUBSCR

 229           LOAD_CONST              89 (('.dump', '.backup', '.jsonl', '.pasbak'))
               STORE_NAME              42 (_DANGEROUS_SUFFIXES)
               LOAD_CONST              12 ('Tuple[str, ...]')
               LOAD_NAME               32 (__annotations__)
               LOAD_CONST              23 ('_DANGEROUS_SUFFIXES')
               STORE_SUBSCR

 234           LOAD_CONST              90 (('restore_drill_report.json', 'monitoring_report.json'))
               STORE_NAME              43 (_DANGEROUS_TOPLEVEL)
               LOAD_CONST              12 ('Tuple[str, ...]')
               LOAD_NAME               32 (__annotations__)
               LOAD_CONST              24 ('_DANGEROUS_TOPLEVEL')
               STORE_SUBSCR

 241           LOAD_NAME               44 (frozenset)
               PUSH_NULL
               BUILD_SET                0
               LOAD_CONST              91 (frozenset({'recovery', '.tox', 'tests', '.pytest_cache', 'node_modules', '.venv', '.mypy_cache', 'backups', 'venv', '.git', '__pycache__'}))
               SET_UPDATE               1
               CALL                     1
               STORE_NAME              45 (_HYGIENE_SKIP_DIRS)
               LOAD_CONST              25 ('frozenset')
               LOAD_NAME               32 (__annotations__)
               LOAD_CONST              26 ('_HYGIENE_SKIP_DIRS')
               STORE_SUBSCR

 255           LOAD_CONST              27 ('BLOCK')
               STORE_NAME              46 (SEVERITY_BLOCK)

 256           LOAD_CONST              28 ('GAP')
               STORE_NAME              47 (SEVERITY_GAP)

 257           LOAD_CONST              29 ('INFO')
               STORE_NAME              48 (SEVERITY_INFO)

 260           LOAD_CONST              30 ('severity')

 265           LOAD_NAME               46 (SEVERITY_BLOCK)

 260           LOAD_CONST              31 ('detail')

 266           LOAD_CONST              32 ('')

 260           BUILD_MAP                2
               LOAD_CONST              33 (<code object __annotate__ at 0x0000018C18024C30, file "scripts\pas145_mvp_readiness_check.py", line 260>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object _check at 0x0000018C17FA2F10, file "scripts\pas145_mvp_readiness_check.py", line 260>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              49 (_check)

 284           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C17FA34B0, file "scripts\pas145_mvp_readiness_check.py", line 284>)
               MAKE_FUNCTION
               LOAD_CONST              36 (<code object _now_iso at 0x0000018C18038DF0, file "scripts\pas145_mvp_readiness_check.py", line 284>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (_now_iso)

 292           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C18025030, file "scripts\pas145_mvp_readiness_check.py", line 292>)
               MAKE_FUNCTION
               LOAD_CONST              38 (<code object _files_present at 0x0000018C180388F0, file "scripts\pas145_mvp_readiness_check.py", line 292>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (_files_present)

 297           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C18025A30, file "scripts\pas145_mvp_readiness_check.py", line 297>)
               MAKE_FUNCTION
               LOAD_CONST              40 (<code object _check_files at 0x0000018C1801C9E0, file "scripts\pas145_mvp_readiness_check.py", line 297>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (_check_files)

 318           LOAD_CONST              41 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts\pas145_mvp_readiness_check.py", line 318>)
               MAKE_FUNCTION
               LOAD_CONST              42 (<code object check_required_runtime at 0x0000018C17FBFEE0, file "scripts\pas145_mvp_readiness_check.py", line 318>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_required_runtime)

 327           LOAD_CONST              43 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts\pas145_mvp_readiness_check.py", line 327>)
               MAKE_FUNCTION
               LOAD_CONST              44 (<code object check_required_memory at 0x0000018C180F4250, file "scripts\pas145_mvp_readiness_check.py", line 327>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_required_memory)

 336           LOAD_CONST              45 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas145_mvp_readiness_check.py", line 336>)
               MAKE_FUNCTION
               LOAD_CONST              46 (<code object check_required_safety at 0x0000018C180F4140, file "scripts\pas145_mvp_readiness_check.py", line 336>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_required_safety)

 345           LOAD_CONST              47 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas145_mvp_readiness_check.py", line 345>)
               MAKE_FUNCTION
               LOAD_CONST              48 (<code object check_required_memory_clis at 0x0000018C180F4030, file "scripts\pas145_mvp_readiness_check.py", line 345>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_required_memory_clis)

 354           LOAD_CONST              49 (<code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas145_mvp_readiness_check.py", line 354>)
               MAKE_FUNCTION
               LOAD_CONST              50 (<code object check_required_migrations at 0x0000018C180F4690, file "scripts\pas145_mvp_readiness_check.py", line 354>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_required_migrations)

 363           LOAD_CONST              51 (<code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas145_mvp_readiness_check.py", line 363>)
               MAKE_FUNCTION
               LOAD_CONST              52 (<code object check_required_docs at 0x0000018C180F47A0, file "scripts\pas145_mvp_readiness_check.py", line 363>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_required_docs)

 372           LOAD_CONST              53 (<code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas145_mvp_readiness_check.py", line 372>)
               MAKE_FUNCTION
               LOAD_CONST              54 (<code object check_optional_demo_surface at 0x0000018C180F48B0, file "scripts\pas145_mvp_readiness_check.py", line 372>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_optional_demo_surface)

 381           LOAD_CONST              55 (<code object __annotate__ at 0x0000018C17FA2100, file "scripts\pas145_mvp_readiness_check.py", line 381>)
               MAKE_FUNCTION
               LOAD_CONST              56 (<code object check_optional_docs at 0x0000018C180F49C0, file "scripts\pas145_mvp_readiness_check.py", line 381>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_optional_docs)

 390           LOAD_CONST              57 (<code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas145_mvp_readiness_check.py", line 390>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object check_offlimits_present at 0x0000018C180F4AD0, file "scripts\pas145_mvp_readiness_check.py", line 390>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (check_offlimits_present)

 403           LOAD_CONST              59 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pas145_mvp_readiness_check.py", line 403>)
               MAKE_FUNCTION
               LOAD_CONST              60 (<code object check_env_var_documentation at 0x0000018C17D81580, file "scripts\pas145_mvp_readiness_check.py", line 403>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (check_env_var_documentation)

 453           LOAD_CONST              61 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts\pas145_mvp_readiness_check.py", line 453>)
               MAKE_FUNCTION
               LOAD_CONST              62 (<code object check_repository_hygiene at 0x0000018C17E7F070, file "scripts\pas145_mvp_readiness_check.py", line 453>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (check_repository_hygiene)

 500           LOAD_CONST              63 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas145_mvp_readiness_check.py", line 500>)
               MAKE_FUNCTION
               LOAD_CONST              64 (<code object _aggregate_status at 0x0000018C17ECF000, file "scripts\pas145_mvp_readiness_check.py", line 500>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (_aggregate_status)

 520           LOAD_CONST              65 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas145_mvp_readiness_check.py", line 520>)
               MAKE_FUNCTION
               LOAD_CONST              66 (<code object _operator_actions at 0x0000018C17D7C920, file "scripts\pas145_mvp_readiness_check.py", line 520>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (_operator_actions)

 578           LOAD_CONST              67 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas145_mvp_readiness_check.py", line 578>)
               MAKE_FUNCTION
               LOAD_CONST              68 (<code object evaluate at 0x0000018C17F80AE0, file "scripts\pas145_mvp_readiness_check.py", line 578>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (evaluate)

 615           LOAD_CONST              69 ('pas145_mvp_readiness_report.json')
               STORE_NAME              67 (REPORT_FILENAME)

 618           LOAD_CONST              70 (<code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas145_mvp_readiness_check.py", line 618>)
               MAKE_FUNCTION
               LOAD_CONST              71 (<code object _build_parser at 0x0000018C1801CBD0, file "scripts\pas145_mvp_readiness_check.py", line 618>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              68 (_build_parser)

 655           LOAD_CONST              72 (<code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas145_mvp_readiness_check.py", line 655>)
               MAKE_FUNCTION
               LOAD_CONST              73 (<code object _print_summary at 0x0000018C17D8D460, file "scripts\pas145_mvp_readiness_check.py", line 655>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              69 (_print_summary)

 674           LOAD_CONST              74 (<code object __annotate__ at 0x0000018C18024B30, file "scripts\pas145_mvp_readiness_check.py", line 674>)
               MAKE_FUNCTION
               LOAD_CONST              75 (<code object _write_report at 0x0000018C179C3A50, file "scripts\pas145_mvp_readiness_check.py", line 674>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              70 (_write_report)

 688           LOAD_CONST              92 ((None,))
               LOAD_CONST              76 (<code object __annotate__ at 0x0000018C180FC030, file "scripts\pas145_mvp_readiness_check.py", line 688>)
               MAKE_FUNCTION
               LOAD_CONST              77 (<code object main at 0x0000018C17F7A470, file "scripts\pas145_mvp_readiness_check.py", line 688>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              71 (main)

 719           LOAD_NAME               72 (__name__)
               LOAD_CONST              78 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 720           LOAD_NAME                7 (sys)
               LOAD_ATTR              146 (exit)
               PUSH_NULL
               LOAD_NAME               71 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 719   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  52           LOAD_NAME               21 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  53   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          402 (to L1)

  52   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "scripts\pas145_mvp_readiness_check.py", line 260>:
260           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

261           LOAD_CONST               2 ('str')

260           LOAD_CONST               3 ('status')

262           LOAD_CONST               2 ('str')

260           LOAD_CONST               4 ('label')

263           LOAD_CONST               2 ('str')

260           LOAD_CONST               5 ('severity')

265           LOAD_CONST               2 ('str')

260           LOAD_CONST               6 ('detail')

266           LOAD_CONST               2 ('str')

260           LOAD_CONST               7 ('return')

267           LOAD_CONST               8 ('dict')

260           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA2F10, file "scripts\pas145_mvp_readiness_check.py", line 260>:
260           RESUME                   0

276           LOAD_CONST               1 ('id')
              LOAD_FAST_BORROW         0 (check_id)

277           LOAD_CONST               2 ('status')
              LOAD_FAST_BORROW         1 (status)

278           LOAD_CONST               3 ('label')
              LOAD_FAST_BORROW         2 (label)

279           LOAD_CONST               4 ('severity')
              LOAD_FAST_BORROW         3 (severity)

280           LOAD_CONST               5 ('detail')
              LOAD_FAST_BORROW         4 (detail)

275           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "scripts\pas145_mvp_readiness_check.py", line 284>:
284           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038DF0, file "scripts\pas145_mvp_readiness_check.py", line 284>:
284           RESUME                   0

285           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "scripts\pas145_mvp_readiness_check.py", line 292>:
292           RESUME                   0
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

Disassembly of <code object _files_present at 0x0000018C180388F0, file "scripts\pas145_mvp_readiness_check.py", line 292>:
 292           RESUME                   0

 293           LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               STORE_FAST               2 (root)

 294           LOAD_FAST_BORROW         1 (rel_paths)
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

 294           SWAP                     2
               STORE_FAST               3 (p)
               RERAISE                  0
ExceptionTable:
  L1 to L4 -> L5 [2]

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "scripts\pas145_mvp_readiness_check.py", line 297>:
297           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')

298           LOAD_CONST               2 ('str')

297           LOAD_CONST               3 ('paths')

299           LOAD_CONST               4 ('Iterable[str]')

297           LOAD_CONST               5 ('severity')

301           LOAD_CONST               2 ('str')

297           LOAD_CONST               6 ('prefix')

302           LOAD_CONST               2 ('str')

297           LOAD_CONST               7 ('label_prefix')

303           LOAD_CONST               2 ('str')

297           LOAD_CONST               8 ('return')

304           LOAD_CONST               9 ('List[dict]')

297           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check_files at 0x0000018C1801C9E0, file "scripts\pas145_mvp_readiness_check.py", line 297>:
297           RESUME                   0

305           BUILD_LIST               0
              STORE_FAST               5 (out)

306           LOAD_GLOBAL              1 (_files_present + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (repo_root, paths)
              CALL                     2
              STORE_FAST               6 (presence)

307           LOAD_FAST_BORROW         6 (presence)
              LOAD_ATTR                3 (items + NULL|self)
              CALL                     0
              GET_ITER
      L1:     FOR_ITER               107 (to L6)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST  120 (path, ok)

308           LOAD_FAST                5 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

309           LOAD_FAST_BORROW         3 (prefix)
              FORMAT_SIMPLE
              LOAD_CONST               0 (':')
              LOAD_GLOBAL              9 (Path + NULL)
              LOAD_FAST_BORROW         7 (path)
              CALL                     1
              LOAD_ATTR               10 (name)
              FORMAT_SIMPLE
              BUILD_STRING             3

310           LOAD_FAST_BORROW         8 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

311   L3:     LOAD_FAST_BORROW         4 (label_prefix)
              FORMAT_SIMPLE
              LOAD_CONST               3 (' ')
              LOAD_GLOBAL              9 (Path + NULL)
              LOAD_FAST_BORROW         7 (path)
              CALL                     1
              LOAD_ATTR               10 (name)
              FORMAT_SIMPLE
              BUILD_STRING             3

312           LOAD_FAST                2 (severity)

313           LOAD_FAST_BORROW         8 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('present')
              JUMP_FORWARD             4 (to L5)
      L4:     LOAD_CONST               5 ('missing at ')
              LOAD_FAST_BORROW         7 (path)
              FORMAT_SIMPLE
              BUILD_STRING             2

308   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          109 (to L1)

307   L6:     END_FOR
              POP_ITER

315           LOAD_FAST_BORROW         5 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts\pas145_mvp_readiness_check.py", line 318>:
318           RESUME                   0
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

Disassembly of <code object check_required_runtime at 0x0000018C17FBFEE0, file "scripts\pas145_mvp_readiness_check.py", line 318>:
318           RESUME                   0

319           LOAD_GLOBAL              1 (_check_files + NULL)

320           LOAD_FAST_BORROW         0 (repo_root)
              LOAD_GLOBAL              2 (REQUIRED_RUNTIME)

321           LOAD_GLOBAL              4 (SEVERITY_BLOCK)

322           LOAD_CONST               0 ('runtime')

323           LOAD_CONST               0 ('runtime')

319           LOAD_CONST               1 (('severity', 'prefix', 'label_prefix'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts\pas145_mvp_readiness_check.py", line 327>:
327           RESUME                   0
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

Disassembly of <code object check_required_memory at 0x0000018C180F4250, file "scripts\pas145_mvp_readiness_check.py", line 327>:
327           RESUME                   0

328           LOAD_GLOBAL              1 (_check_files + NULL)

329           LOAD_FAST_BORROW         0 (repo_root)
              LOAD_GLOBAL              2 (REQUIRED_MEMORY)

330           LOAD_GLOBAL              4 (SEVERITY_BLOCK)

331           LOAD_CONST               0 ('memory')

332           LOAD_CONST               1 ('memory module')

328           LOAD_CONST               2 (('severity', 'prefix', 'label_prefix'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas145_mvp_readiness_check.py", line 336>:
336           RESUME                   0
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

Disassembly of <code object check_required_safety at 0x0000018C180F4140, file "scripts\pas145_mvp_readiness_check.py", line 336>:
336           RESUME                   0

337           LOAD_GLOBAL              1 (_check_files + NULL)

338           LOAD_FAST_BORROW         0 (repo_root)
              LOAD_GLOBAL              2 (REQUIRED_SAFETY)

339           LOAD_GLOBAL              4 (SEVERITY_BLOCK)

340           LOAD_CONST               0 ('safety')

341           LOAD_CONST               1 ('safety script')

337           LOAD_CONST               2 (('severity', 'prefix', 'label_prefix'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas145_mvp_readiness_check.py", line 345>:
345           RESUME                   0
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

Disassembly of <code object check_required_memory_clis at 0x0000018C180F4030, file "scripts\pas145_mvp_readiness_check.py", line 345>:
345           RESUME                   0

346           LOAD_GLOBAL              1 (_check_files + NULL)

347           LOAD_FAST_BORROW         0 (repo_root)
              LOAD_GLOBAL              2 (REQUIRED_MEMORY_CLIS)

348           LOAD_GLOBAL              4 (SEVERITY_BLOCK)

349           LOAD_CONST               0 ('memory_cli')

350           LOAD_CONST               1 ('memory CLI')

346           LOAD_CONST               2 (('severity', 'prefix', 'label_prefix'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas145_mvp_readiness_check.py", line 354>:
354           RESUME                   0
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

Disassembly of <code object check_required_migrations at 0x0000018C180F4690, file "scripts\pas145_mvp_readiness_check.py", line 354>:
354           RESUME                   0

355           LOAD_GLOBAL              1 (_check_files + NULL)

356           LOAD_FAST_BORROW         0 (repo_root)
              LOAD_GLOBAL              2 (REQUIRED_MIGRATIONS)

357           LOAD_GLOBAL              4 (SEVERITY_BLOCK)

358           LOAD_CONST               0 ('migration')

359           LOAD_CONST               0 ('migration')

355           LOAD_CONST               1 (('severity', 'prefix', 'label_prefix'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas145_mvp_readiness_check.py", line 363>:
363           RESUME                   0
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

Disassembly of <code object check_required_docs at 0x0000018C180F47A0, file "scripts\pas145_mvp_readiness_check.py", line 363>:
363           RESUME                   0

364           LOAD_GLOBAL              1 (_check_files + NULL)

365           LOAD_FAST_BORROW         0 (repo_root)
              LOAD_GLOBAL              2 (REQUIRED_DOCS)

366           LOAD_GLOBAL              4 (SEVERITY_BLOCK)

367           LOAD_CONST               0 ('doc')

368           LOAD_CONST               0 ('doc')

364           LOAD_CONST               1 (('severity', 'prefix', 'label_prefix'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas145_mvp_readiness_check.py", line 372>:
372           RESUME                   0
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

Disassembly of <code object check_optional_demo_surface at 0x0000018C180F48B0, file "scripts\pas145_mvp_readiness_check.py", line 372>:
372           RESUME                   0

373           LOAD_GLOBAL              1 (_check_files + NULL)

374           LOAD_FAST_BORROW         0 (repo_root)
              LOAD_GLOBAL              2 (OPTIONAL_DEMO_SURFACE)

375           LOAD_GLOBAL              4 (SEVERITY_GAP)

376           LOAD_CONST               0 ('demo')

377           LOAD_CONST               1 ('demo surface')

373           LOAD_CONST               2 (('severity', 'prefix', 'label_prefix'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "scripts\pas145_mvp_readiness_check.py", line 381>:
381           RESUME                   0
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

Disassembly of <code object check_optional_docs at 0x0000018C180F49C0, file "scripts\pas145_mvp_readiness_check.py", line 381>:
381           RESUME                   0

382           LOAD_GLOBAL              1 (_check_files + NULL)

383           LOAD_FAST_BORROW         0 (repo_root)
              LOAD_GLOBAL              2 (OPTIONAL_DOCS)

384           LOAD_GLOBAL              4 (SEVERITY_GAP)

385           LOAD_CONST               0 ('optional_doc')

386           LOAD_CONST               1 ('optional doc')

382           LOAD_CONST               2 (('severity', 'prefix', 'label_prefix'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas145_mvp_readiness_check.py", line 390>:
390           RESUME                   0
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

Disassembly of <code object check_offlimits_present at 0x0000018C180F4AD0, file "scripts\pas145_mvp_readiness_check.py", line 390>:
390           RESUME                   0

395           LOAD_GLOBAL              1 (_check_files + NULL)

396           LOAD_FAST_BORROW         0 (repo_root)
              LOAD_GLOBAL              2 (OFFLIMITS_FILES)

397           LOAD_GLOBAL              4 (SEVERITY_BLOCK)

398           LOAD_CONST               1 ('offlimits')

399           LOAD_CONST               2 ('off-limits file')

395           LOAD_CONST               3 (('severity', 'prefix', 'label_prefix'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pas145_mvp_readiness_check.py", line 403>:
403           RESUME                   0
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

Disassembly of <code object check_env_var_documentation at 0x0000018C17D81580, file "scripts\pas145_mvp_readiness_check.py", line 403>:
 403            RESUME                   0

 409            BUILD_LIST               0
                STORE_FAST               1 (out)

 410            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               1 ('.env.example')
                BINARY_OP               11 (/)
                STORE_FAST               2 (example)

 411            LOAD_FAST_BORROW         2 (example)
                LOAD_ATTR                3 (is_file + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        38 (to L1)
                NOT_TAKEN

 412            LOAD_FAST_BORROW         1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 413            LOAD_CONST               2 ('env:example_present')

 414            LOAD_CONST               3 ('FAIL')

 415            LOAD_CONST               4 ('.env.example present')

 416            LOAD_GLOBAL              8 (SEVERITY_GAP)

 417            LOAD_CONST               5 ("missing at repo root — demo operators can't configure")

 412            LOAD_CONST               6 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 419            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 421    L1:     NOP

 422    L2:     LOAD_FAST_BORROW         2 (example)
                LOAD_ATTR               11 (read_text + NULL|self)
                LOAD_CONST               7 ('utf-8')
                LOAD_CONST               8 (('encoding',))
                CALL_KW                  1
                STORE_FAST               3 (text)

 433    L3:     LOAD_FAST                1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 434            LOAD_CONST               2 ('env:example_present')

 435            LOAD_CONST              14 ('PASS')

 436            LOAD_CONST               4 ('.env.example present')

 437            LOAD_GLOBAL             18 (SEVERITY_INFO)

 438            LOAD_CONST              15 ('found')

 433            LOAD_CONST               6 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 441            LOAD_GLOBAL             20 (REQUIRED_ENV_VAR_NAMES)
                GET_ITER
        L4:     FOR_ITER                68 (to L9)
                STORE_FAST               5 (name)

 442            LOAD_FAST_LOAD_FAST     83 (name, text)
                CONTAINS_OP              0 (in)
                STORE_FAST               6 (ok)

 443            LOAD_FAST                1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 444            LOAD_CONST              16 ('env:')
                LOAD_FAST                5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 445            LOAD_FAST                6 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_CONST              14 ('PASS')
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               3 ('FAIL')

 446    L6:     LOAD_CONST              17 ('.env.example documents ')
                LOAD_FAST                5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 447            LOAD_GLOBAL              8 (SEVERITY_GAP)

 448            LOAD_FAST                6 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN
                LOAD_CONST              18 ('documented')
                JUMP_FORWARD             1 (to L8)
        L7:     LOAD_CONST              19 ('missing from .env.example')

 443    L8:     LOAD_CONST               6 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           70 (to L4)

 441    L9:     END_FOR
                POP_ITER

 450            LOAD_FAST                1 (out)
                RETURN_VALUE

  --   L10:     PUSH_EXC_INFO

 423            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       71 (to L15)
                NOT_TAKEN
                STORE_FAST               4 (e)

 424   L11:     LOAD_FAST                1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 425            LOAD_CONST               9 ('env:example_readable')

 426            LOAD_CONST               3 ('FAIL')

 427            LOAD_CONST              10 ('.env.example readable')

 428            LOAD_GLOBAL              8 (SEVERITY_GAP)

 429            LOAD_CONST              11 ('unreadable (')
                LOAD_GLOBAL             15 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               16 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST              12 (')')
                BUILD_STRING             3

 424            LOAD_CONST               6 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 431            LOAD_FAST                1 (out)
       L12:     SWAP                     2
       L13:     POP_EXCEPT
                LOAD_CONST              13 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RETURN_VALUE

  --   L14:     LOAD_CONST              13 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 423   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L10 [0]
  L10 to L11 -> L16 [1] lasti
  L11 to L12 -> L14 [1] lasti
  L12 to L13 -> L16 [1] lasti
  L14 to L16 -> L16 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts\pas145_mvp_readiness_check.py", line 453>:
453           RESUME                   0
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

Disassembly of <code object check_repository_hygiene at 0x0000018C17E7F070, file "scripts\pas145_mvp_readiness_check.py", line 453>:
  --            MAKE_CELL               11 (lower)

 453            RESUME                   0

 457            BUILD_LIST               0
                STORE_FAST               1 (out)

 458            BUILD_LIST               0
                STORE_FAST               2 (offenders)

 459            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                STORE_FAST               3 (root)

 461            LOAD_GLOBAL              2 (os)
                LOAD_ATTR                4 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         3 (root)
                CALL                     1
                GET_ITER
        L1:     FOR_ITER               232 (to L16)
                UNPACK_SEQUENCE          3
                STORE_FAST_STORE_FAST   69 (dirpath, dirnames)
                STORE_FAST               6 (filenames)

 462            LOAD_FAST_BORROW         5 (dirnames)
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

 463            LOAD_FAST_BORROW         6 (filenames)
                GET_ITER
        L8:     FOR_ITER               187 (to L15)
                STORE_FAST               8 (fname)

 464            LOAD_FAST_BORROW         8 (fname)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_DEREF             11 (lower)

 465            LOAD_GLOBAL             10 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       35 (to L12)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        11 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               2 (<code object <genexpr> at 0x0000018C18053AB0, file "scripts\pas145_mvp_readiness_check.py", line 465>)
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
                LOAD_FAST_BORROW        11 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               2 (<code object <genexpr> at 0x0000018C18053AB0, file "scripts\pas145_mvp_readiness_check.py", line 465>)
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

 466   L14:     LOAD_GLOBAL              2 (os)
                LOAD_ATTR               14 (path)
                LOAD_ATTR               17 (relpath + NULL|self)

 467            LOAD_GLOBAL              2 (os)
                LOAD_ATTR               14 (path)
                LOAD_ATTR               19 (join + NULL|self)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 72 (dirpath, fname)
                CALL                     2
                LOAD_FAST_BORROW         3 (root)

 466            CALL                     2

 468            LOAD_ATTR               21 (replace + NULL|self)
                LOAD_CONST               5 ('\\')
                LOAD_CONST               6 ('/')
                CALL                     2

 466            STORE_FAST               9 (rel)

 469            LOAD_FAST_BORROW         2 (offenders)
                LOAD_ATTR               23 (append + NULL|self)
                LOAD_FAST_BORROW         9 (rel)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          189 (to L8)

 463   L15:     END_FOR
                POP_ITER
                JUMP_BACKWARD          234 (to L1)

 461   L16:     END_FOR
                POP_ITER

 471            LOAD_GLOBAL             24 (_DANGEROUS_TOPLEVEL)
                GET_ITER
       L17:     FOR_ITER                50 (to L19)
                STORE_FAST              10 (top)

 472            LOAD_FAST_BORROW_LOAD_FAST_BORROW 58 (root, top)
                BINARY_OP               11 (/)
                LOAD_ATTR               27 (is_file + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
                NOT_TAKEN
                JUMP_BACKWARD           33 (to L17)

 473   L18:     LOAD_FAST_BORROW         2 (offenders)
                LOAD_ATTR               23 (append + NULL|self)
                LOAD_FAST_BORROW        10 (top)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           52 (to L17)

 471   L19:     END_FOR
                POP_ITER

 475            LOAD_FAST_BORROW         2 (offenders)
                TO_BOOL
                POP_JUMP_IF_TRUE        38 (to L20)
                NOT_TAKEN

 476            LOAD_FAST_BORROW         1 (out)
                LOAD_ATTR               23 (append + NULL|self)
                LOAD_GLOBAL             29 (_check + NULL)

 477            LOAD_CONST               7 ('hygiene:no_dangerous_artefacts')

 478            LOAD_CONST               8 ('PASS')

 479            LOAD_CONST               9 ('no tracked backup / archive / dump artefacts')

 480            LOAD_GLOBAL             30 (SEVERITY_INFO)

 481            LOAD_CONST              10 ('filesystem walk clean')

 476            LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 483            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 485   L20:     LOAD_GLOBAL             33 (sorted + NULL)
                LOAD_GLOBAL             35 (set + NULL)
                LOAD_FAST_BORROW         2 (offenders)
                CALL                     1
                CALL                     1
                GET_ITER
       L21:     FOR_ITER                44 (to L22)
                STORE_FAST               9 (rel)

 486            LOAD_FAST_BORROW         1 (out)
                LOAD_ATTR               23 (append + NULL|self)
                LOAD_GLOBAL             29 (_check + NULL)

 487            LOAD_CONST              12 ('hygiene:tracked_artefact:')
                LOAD_FAST_BORROW         9 (rel)
                FORMAT_SIMPLE
                BUILD_STRING             2

 488            LOAD_CONST              13 ('FAIL')

 489            LOAD_CONST              14 ('dangerous tracked artefact')

 490            LOAD_GLOBAL             36 (SEVERITY_BLOCK)

 491            LOAD_FAST_BORROW         9 (rel)
                FORMAT_SIMPLE
                LOAD_CONST              15 (' — remove from working tree')
                BUILD_STRING             2

 486            LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           46 (to L21)

 485   L22:     END_FOR
                POP_ITER

 493            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L23:     SWAP                     2
                POP_TOP

 462            SWAP                     2
                STORE_FAST               7 (d)
                RERAISE                  0
ExceptionTable:
  L2 to L4 -> L23 [3]
  L5 to L7 -> L23 [3]

Disassembly of <code object <genexpr> at 0x0000018C18053AB0, file "scripts\pas145_mvp_readiness_check.py", line 465>:
  --           COPY_FREE_VARS           1

 465           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas145_mvp_readiness_check.py", line 500>:
500           RESUME                   0
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

Disassembly of <code object _aggregate_status at 0x0000018C17ECF000, file "scripts\pas145_mvp_readiness_check.py", line 500>:
 500            RESUME                   0

 501            LOAD_FAST_BORROW         0 (checks)
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

 502            LOAD_FAST_BORROW         2 (failures)
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L7:     BUILD_LIST               0
                SWAP                     2
        L8:     FOR_ITER                32 (to L11)
                STORE_FAST_LOAD_FAST    17 (c, c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))
        L9:     POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           30 (to L8)
       L10:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           34 (to L8)
       L11:     END_FOR
                POP_ITER
       L12:     STORE_FAST               3 (blockers)
                STORE_FAST               1 (c)

 503            LOAD_FAST_BORROW         2 (failures)
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
       L13:     BUILD_LIST               0
                SWAP                     2
       L14:     FOR_ITER                32 (to L17)
                STORE_FAST_LOAD_FAST    17 (c, c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_GAP)
                COMPARE_OP              88 (bool(==))
       L15:     POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                JUMP_BACKWARD           30 (to L14)
       L16:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           34 (to L14)
       L17:     END_FOR
                POP_ITER
       L18:     STORE_FAST               4 (gaps)
                STORE_FAST               1 (c)

 505            LOAD_FAST_BORROW         3 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L19)
                NOT_TAKEN

 506            LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                STORE_FAST               5 (verdict)
                JUMP_FORWARD            21 (to L21)

 507   L19:     LOAD_FAST_BORROW         4 (gaps)
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L20)
                NOT_TAKEN

 508            LOAD_GLOBAL              8 (VERDICT_READY_WITH_GAPS)
                STORE_FAST               5 (verdict)
                JUMP_FORWARD             6 (to L21)

 510   L20:     LOAD_GLOBAL             10 (VERDICT_READY_FOR_DEMO)
                STORE_FAST               5 (verdict)

 513   L21:     LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         5 (verdict)

 514            LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         3 (blockers)

 515            LOAD_CONST               5 ('gaps')
                LOAD_FAST_BORROW         4 (gaps)

 516            LOAD_CONST               6 ('failures')
                LOAD_FAST_BORROW         2 (failures)

 512            BUILD_MAP                4
                RETURN_VALUE

  --   L22:     SWAP                     2
                POP_TOP

 501            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L23:     SWAP                     2
                POP_TOP

 502            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L24:     SWAP                     2
                POP_TOP

 503            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L22 [2]
  L4 to L6 -> L22 [2]
  L7 to L9 -> L23 [2]
  L10 to L12 -> L23 [2]
  L13 to L15 -> L24 [2]
  L16 to L18 -> L24 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas145_mvp_readiness_check.py", line 520>:
520           RESUME                   0
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
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _operator_actions at 0x0000018C17D7C920, file "scripts\pas145_mvp_readiness_check.py", line 520>:
520            RESUME                   0

522            BUILD_LIST               0
               STORE_FAST               1 (actions)

523            LOAD_FAST_BORROW         0 (checks)
               GET_ITER
       L1:     EXTENDED_ARG             2
               FOR_ITER               518 (to L14)
               STORE_FAST               2 (c)

524            LOAD_FAST_BORROW         2 (c)
               LOAD_CONST               1 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST               2 ('FAIL')
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN

525            JUMP_BACKWARD           20 (to L1)

526    L2:     LOAD_FAST_BORROW         2 (c)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               3 ('severity')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         7 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_GLOBAL              2 (SEVERITY_BLOCK)
       L3:     STORE_FAST               3 (sev)

527            LOAD_FAST_BORROW         2 (c)
               LOAD_CONST               4 ('id')
               BINARY_OP               26 ([])
               STORE_FAST               4 (cid)

528            LOAD_FAST_BORROW         2 (c)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               5 ('detail')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               6 ('')
       L4:     STORE_FAST               5 (detail)

529            LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              35 (('runtime:', 'memory:', 'safety:', 'memory_cli:'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       27 (to L5)
               NOT_TAKEN

530            LOAD_FAST_BORROW         1 (actions)
               LOAD_ATTR                7 (append + NULL|self)

531            LOAD_CONST               7 ('[BLOCK] Restore missing file referenced by ')
               LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST               8 (' (')
               LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')
               BUILD_STRING             5

530            CALL                     1
               POP_TOP
               JUMP_BACKWARD          136 (to L1)

533    L5:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              10 ('migration:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       27 (to L6)
               NOT_TAKEN

534            LOAD_FAST_BORROW         1 (actions)
               LOAD_ATTR                7 (append + NULL|self)

535            LOAD_CONST              11 ('[BLOCK] Migration proposal missing: ')
               LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              12 (' — recreate from PAS144 phase notes (')

536            LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')

535            BUILD_STRING             5

534            CALL                     1
               POP_TOP
               JUMP_BACKWARD          185 (to L1)

538    L6:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              13 ('doc:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       27 (to L7)
               NOT_TAKEN

539            LOAD_FAST_BORROW         1 (actions)
               LOAD_ATTR                7 (append + NULL|self)

540            LOAD_CONST              14 ('[BLOCK] Required doc missing: ')
               LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              15 (' — author or restore (')

541            LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')

540            BUILD_STRING             5

539            CALL                     1
               POP_TOP
               JUMP_BACKWARD          234 (to L1)

543    L7:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              16 ('offlimits:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       28 (to L8)
               NOT_TAKEN

544            LOAD_FAST_BORROW         1 (actions)
               LOAD_ATTR                7 (append + NULL|self)

545            LOAD_CONST              17 ('[BLOCK] Off-limits file missing: ')
               LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              18 (' — restore from git history; do not modify (')

546            LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')

545            BUILD_STRING             5

544            CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          284 (to L1)

548    L8:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              19 ('demo:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       28 (to L9)
               NOT_TAKEN

549            LOAD_FAST_BORROW         1 (actions)
               LOAD_ATTR                7 (append + NULL|self)

550            LOAD_CONST              20 ('[GAP] Demo surface missing: ')
               LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              21 (' — restore before live demo (')

551            LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')

550            BUILD_STRING             5

549            CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          334 (to L1)

553    L9:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              22 ('optional_doc:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       28 (to L10)
               NOT_TAKEN

554            LOAD_FAST_BORROW         1 (actions)
               LOAD_ATTR                7 (append + NULL|self)

555            LOAD_CONST              23 ('[GAP] Optional doc missing: ')
               LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              24 (' — author when convenient (')

556            LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')

555            BUILD_STRING             5

554            CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          384 (to L1)

558   L10:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              25 ('env:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       28 (to L11)
               NOT_TAKEN

559            LOAD_FAST_BORROW         1 (actions)
               LOAD_ATTR                7 (append + NULL|self)

560            LOAD_CONST              26 ('[GAP] .env.example documentation issue: ')
               LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST               8 (' (')
               LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')
               BUILD_STRING             5

559            CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          434 (to L1)

562   L11:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              27 ('hygiene:tracked_artefact:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L12)
               NOT_TAKEN

563            LOAD_FAST_BORROW         1 (actions)
               LOAD_ATTR                7 (append + NULL|self)

564            LOAD_CONST              28 ('[BLOCK] Repo hygiene: ')
               LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              29 (' — remove the file before committing.')
               BUILD_STRING             3

563            CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          481 (to L1)

568   L12:     LOAD_FAST                1 (actions)
               LOAD_ATTR                7 (append + NULL|self)

569            LOAD_CONST              30 ('[')
               LOAD_FAST                3 (sev)
               FORMAT_SIMPLE
               LOAD_CONST              31 ('] ')
               LOAD_FAST                4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              32 (' — ')
               LOAD_FAST                5 (detail)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L13)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              33 ('see report for context')
      L13:     FORMAT_SIMPLE
               LOAD_CONST              34 ('.')
               BUILD_STRING             7

568            CALL                     1
               POP_TOP
               EXTENDED_ARG             2
               JUMP_BACKWARD          521 (to L1)

523   L14:     END_FOR
               POP_ITER

571            LOAD_FAST_BORROW         1 (actions)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas145_mvp_readiness_check.py", line 578>:
578           RESUME                   0
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
              LOAD_CONST               4 ('dict')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object evaluate at 0x0000018C17F80AE0, file "scripts\pas145_mvp_readiness_check.py", line 578>:
578           RESUME                   0

580           BUILD_LIST               0
              STORE_FAST               1 (checks)

582           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_required_runtime + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

583           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_required_memory + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

584           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_required_safety + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

585           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_required_memory_clis + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

586           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_required_migrations + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

587           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_required_docs + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

588           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_optional_demo_surface + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

589           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_optional_docs + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

590           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_offlimits_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

591           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_env_var_documentation + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

592           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_repository_hygiene + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

594           LOAD_GLOBAL             25 (_aggregate_status + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

596           LOAD_CONST               1 ('phase')
              LOAD_CONST               2 ('PAS145')

597           LOAD_CONST               3 ('generated_at')
              LOAD_GLOBAL             27 (_now_iso + NULL)
              CALL                     0

598           LOAD_CONST               4 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               4 ('verdict')
              BINARY_OP               26 ([])

599           LOAD_CONST               5 ('ready_for_demo')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               4 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             28 (VERDICT_READY_FOR_DEMO)
              COMPARE_OP              72 (==)

600           LOAD_CONST               6 ('blocker_count')
              LOAD_GLOBAL             31 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               7 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

601           LOAD_CONST               8 ('gap_count')
              LOAD_GLOBAL             31 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               9 ('gaps')
              BINARY_OP               26 ([])
              CALL                     1

602           LOAD_CONST              10 ('check_count')
              LOAD_GLOBAL             31 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

603           LOAD_CONST              11 ('pass_count')
              LOAD_GLOBAL             33 (sum + NULL)
              LOAD_CONST              12 (<code object <genexpr> at 0x0000018C18053510, file "scripts\pas145_mvp_readiness_check.py", line 603>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

604           LOAD_CONST              13 ('fail_count')
              LOAD_GLOBAL             33 (sum + NULL)
              LOAD_CONST              14 (<code object <genexpr> at 0x0000018C18053BD0, file "scripts\pas145_mvp_readiness_check.py", line 604>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

605           LOAD_CONST              15 ('checks')
              LOAD_FAST_BORROW         1 (checks)

606           LOAD_CONST              16 ('operator_actions')
              LOAD_GLOBAL             35 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

595           BUILD_MAP               11
              STORE_FAST               3 (report)

608           LOAD_FAST_BORROW         3 (report)
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053510, file "scripts\pas145_mvp_readiness_check.py", line 603>:
 603           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                22 (to L5)
               STORE_FAST_LOAD_FAST    17 (c, c)
               LOAD_CONST               0 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST               1 ('PASS')
               COMPARE_OP              88 (bool(==))
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           18 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           24 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18053BD0, file "scripts\pas145_mvp_readiness_check.py", line 604>:
 604           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                22 (to L5)
               STORE_FAST_LOAD_FAST    17 (c, c)
               LOAD_CONST               0 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST               1 ('FAIL')
               COMPARE_OP              88 (bool(==))
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           18 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           24 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas145_mvp_readiness_check.py", line 618>:
618           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1801CBD0, file "scripts\pas145_mvp_readiness_check.py", line 618>:
618           RESUME                   0

619           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

620           LOAD_CONST               0 ('pas145_mvp_readiness_check')

622           LOAD_CONST               1 ('PAS145 — Evaluate brokerage-MVP demo readiness. Read-only. Does not touch Supabase, .env, or any tenant data.')

619           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

627           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

628           LOAD_CONST               3 ('--repo-root')

629           LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

630           LOAD_CONST               4 ('Repo root to evaluate (default: parent of this script).')

627           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

632           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

633           LOAD_CONST               6 ('--output')

634           LOAD_GLOBAL              8 (REPORT_FILENAME)

635           LOAD_CONST               7 ('Where to write the JSON report (default ./')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST               8 (').')
              BUILD_STRING             3

632           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

637           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

638           LOAD_CONST               9 ('--json')

639           LOAD_CONST              10 ('store_true')

640           LOAD_CONST              11 ('Emit the report JSON on stdout in addition to the file.')

637           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

642           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

643           LOAD_CONST              13 ('--summary-only')

644           LOAD_CONST              10 ('store_true')

645           LOAD_CONST              14 ('Skip writing the full report file; print verdict only.')

642           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

647           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

648           LOAD_CONST              15 ('--strict')

649           LOAD_CONST              10 ('store_true')

650           LOAD_CONST              16 ('Exit 1 unless verdict == READY_FOR_DEMO.')

647           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

652           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas145_mvp_readiness_check.py", line 655>:
655           RESUME                   0
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
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _print_summary at 0x0000018C17D8D460, file "scripts\pas145_mvp_readiness_check.py", line 655>:
655           RESUME                   0

656           LOAD_GLOBAL              1 (print + NULL)

657           LOAD_CONST               0 ('[PAS145] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

658           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' gaps=')

659           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('gap_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

660           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

661           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

662           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

657           BUILD_STRING            12

656           CALL                     1
              POP_TOP

664           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              12 ('operator_actions')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     STORE_FAST               1 (actions)

665           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

666           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS145] operator actions:')
              CALL                     1
              POP_TOP

668           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 20, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

669           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

668   L3:     END_FOR
              POP_ITER

670           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          20
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

671           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              16 ('  ... and ')
              LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          20
              BINARY_OP               10 (-)
              FORMAT_SIMPLE
              LOAD_CONST              17 (' more (see report file)')
              BUILD_STRING             3
              CALL                     1
              POP_TOP
              LOAD_CONST              18 (None)
              RETURN_VALUE

670   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

665   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "scripts\pas145_mvp_readiness_check.py", line 674>:
674           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('path')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('payload')
              LOAD_CONST               4 ('dict')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('None')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _write_report at 0x0000018C179C3A50, file "scripts\pas145_mvp_readiness_check.py", line 674>:
 674           RESUME                   0

 675           NOP

 676   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 677           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 678           LOAD_CONST               3 ('utf-8')

 676           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 680           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 681   L4:     LOAD_GLOBAL             11 (print + NULL)

 682           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 683           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 682           BUILD_STRING             4

 684           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 681           LOAD_CONST               7 (('file',))
               CALL_KW                  2
               POP_TOP
       L5:     POP_EXCEPT
               LOAD_CONST               8 (None)
               STORE_FAST               2 (e)
               DELETE_FAST              2 (e)
               LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               8 (None)
               STORE_FAST               2 (e)
               DELETE_FAST              2 (e)
               RERAISE                  1

 680   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C180FC030, file "scripts\pas145_mvp_readiness_check.py", line 688>:
688           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17F7A470, file "scripts\pas145_mvp_readiness_check.py", line 688>:
 688            RESUME                   0

 689            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 690            NOP

 691    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 695    L2:     LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               15 (abspath + NULL|self)
                LOAD_FAST                2 (args)
                LOAD_ATTR               16 (repo_root)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         7 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_GLOBAL             18 (_REPO_ROOT_DEFAULT)
        L3:     CALL                     1
                STORE_FAST               4 (repo_root)

 696            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 697            LOAD_GLOBAL             23 (print + NULL)

 698            LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2

 699            LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)

 697            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 701            LOAD_SMALL_INT           2
                RETURN_VALUE

 703    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 705            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 706            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 708    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 710            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 711            LOAD_GLOBAL             23 (print + NULL)
                LOAD_GLOBAL             38 (json)
                LOAD_ATTR               40 (dumps)
                PUSH_NULL
                LOAD_FAST                5 (report)
                LOAD_SMALL_INT           2
                LOAD_CONST               4 (True)
                LOAD_CONST               5 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 713    L6:     LOAD_FAST                2 (args)
                LOAD_ATTR               42 (strict)
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L8)
                NOT_TAKEN

 714            LOAD_FAST                5 (report)
                LOAD_CONST               6 ('verdict')
                BINARY_OP               26 ([])
                LOAD_GLOBAL             44 (VERDICT_READY_FOR_DEMO)
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN
                LOAD_SMALL_INT           0
                RETURN_VALUE
        L7:     LOAD_SMALL_INT           1
                RETURN_VALUE

 716    L8:     LOAD_FAST                5 (report)
                LOAD_CONST               6 ('verdict')
                BINARY_OP               26 ([])
                LOAD_GLOBAL             46 (VERDICT_NOT_READY)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_SMALL_INT           0
                RETURN_VALUE
        L9:     LOAD_SMALL_INT           1
                RETURN_VALUE

  --   L10:     PUSH_EXC_INFO

 692            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L19)
                NOT_TAKEN
                STORE_FAST               3 (e)

 693   L11:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST               7 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L16)
       L12:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
       L13:     NOT_TAKEN
       L14:     POP_TOP
                LOAD_SMALL_INT           0
       L15:     CALL                     1
       L16:     SWAP                     2
       L17:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L18:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 692   L19:     RERAISE                  0

  --   L20:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L10 [0]
  L10 to L11 -> L20 [1] lasti
  L11 to L13 -> L18 [1] lasti
  L14 to L16 -> L18 [1] lasti
  L16 to L17 -> L20 [1] lasti
  L18 to L20 -> L20 [1] lasti
```
