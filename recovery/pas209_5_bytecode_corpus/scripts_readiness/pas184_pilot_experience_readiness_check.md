# scripts_readiness/pas184_pilot_experience_readiness_check

- **pyc:** `scripts\__pycache__\pas184_pilot_experience_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas184_pilot_experience_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas184_pilot_experience_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS184 — Pilot experience polish readiness gate.

Deterministic, non-mutating evaluator for "is PAS184 wired
correctly and free of regressions in the PAS160-PAS183 +
PAS-SECURITY-01/02/03/04 doctrine?".

Walks the repo and verifies:

  * PAS184 surfaces exist:
      - docs/pas184_pilot_experience_polish.md
      - docs/orvn_active_pilot_operating_playbook.md
      - app/routes/operator_learning_dashboard.py
      - scripts/pas184_pilot_experience_readiness_check.py
      - tests/mvp/test_pas184_pilot_experience_polish.py
  * Each PAS184 doc carries its required structural clauses.
  * No PAS184 doc introduces forbidden scope tokens in a
    positive sense.
  * The webapp HTML still carries:
      - `.pas-error-banner` class definition
      - `.pas-skeleton` class definition
      - the `window.PAS` JS helper namespace
      - `errorBannerHtml` / `skeletonRowsHtml` helper functions
  * The webapp does NOT introduce forbidden capability tokens.
  * `operator_learning_dashboard.py` carries:
      - `@router.get("/dashboard")` route
      - `require_admin(` definition
      - `check_rate_limit` + `surface="admin"` (PAS-SECURITY-04
        pattern)
      - NO `@router.post` declaration
      - NO live-mutation imports
      - aggregates the PAS180 / PAS181 / PAS182 read helpers
  * `app/main.py` mounts `operator_learning_dashboard_router`.
  * Memory Review surface (PAS147-PAS158) intact.
  * audit_service.py has no UPDATE / DELETE helpers.
  * Worker OFF by default and not auto-started.
  * All PAS160-PAS183 + PAS-SECURITY-01/02/03/04 readiness
    scripts still exist.
  * Supports `--summary-only` / `--json`.
  * Exits 0 ready, 1 blockers, 2 bad args.
  * Never reads .env.
  * Never touches production data.
```

## Imports

`List`, `Optional`, `Path`, `__future__`, `annotations`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_audit_service_invariant`, `check_dashboard_route`, `check_doc_no_forbidden_scope`, `check_doc_required_clauses`, `check_files_present`, `check_main_router_mount`, `check_memory_review_intact`, `check_no_startup_worker`, `check_prior_phases_intact`, `check_self_no_env_or_db`, `check_webapp_anchors`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `NOT_READY`, `PAS184`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS184 — Pilot experience polish readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS184 wired\ncorrectly and free of regressions in the PAS160-PAS183 +\nPAS-SECURITY-01/02/03/04 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS184 surfaces exist:\n      - docs/pas184_pilot_experience_polish.md\n      - docs/orvn_active_pilot_operating_playbook.md\n      - app/routes/operator_learning_dashboard.py\n      - scripts/pas184_pilot_experience_readiness_check.py\n      - tests/mvp/test_pas184_pilot_experience_polish.py\n  * Each PAS184 doc carries its required structural clauses.\n  * No PAS184 doc introduces forbidden scope tokens in a\n    positive sense.\n  * The webapp HTML still carries:\n      - `.pas-error-banner` class definition\n      - `.pas-skeleton` class definition\n      - the `window.PAS` JS helper namespace\n      - `errorBannerHtml` / `skeletonRowsHtml` helper functions\n  * The webapp does NOT introduce forbidden capability tokens.\n  * `operator_learning_dashboard.py` carries:\n      - `@router.get("/dashboard")` route\n      - `require_admin(` definition\n      - `check_rate_limit` + `surface="admin"` (PAS-SECURITY-04\n        pattern)\n      - NO `@router.post` declaration\n      - NO live-mutation imports\n      - aggregates the PAS180 / PAS181 / PAS182 read helpers\n  * `app/main.py` mounts `operator_learning_dashboard_router`.\n  * Memory Review surface (PAS147-PAS158) intact.\n  * audit_service.py has no UPDATE / DELETE helpers.\n  * Worker OFF by default and not auto-started.\n  * All PAS160-PAS183 + PAS-SECURITY-01/02/03/04 readiness\n    scripts still exist.\n  * Supports `--summary-only` / `--json`.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'docs/pas184_pilot_experience_polish.md'
- 'docs/orvn_active_pilot_operating_playbook.md'
- 'app/routes/operator_learning_dashboard.py'
- 'app/static/dashboard/index.html'
- 'severity'
- 'detail'
- 'pas184_pilot_experience_readiness_report.json'
- 'check_id'
- 'str'
- 'status'
- 'label'
- 'return'
- 'dict'
- 'seconds'
- 'path'
- 'Path'
- 'Optional[str]'
- 'replace'
- 'src'
- '"""'
- "'''"
- 'repo_root'
- 'List[dict]'
- 'file:'
- 'PASS'
- 'FAIL'
- 'Required PAS184 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS184 must not delete'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS184 must not touch'
- 'app'
- 'services'
- 'ingestion'
- 'worker.py'
- '_ENV_FLAG_ENABLED_LITERAL = "true"'
- "_ENV_FLAG_ENABLED_LITERAL = 'true'"
- 'worker:off_by_default'
- 'Pending-call worker is OFF by default'
- 'missing strict enable-literal constant'
- 'main.py'
- 'from app.services.ingestion.worker'
- 'from app.services.ingestion.worker import …'
- 'import app.services.ingestion.worker'
- 'run_worker_loop'
- 'run_worker_loop reference'
- 'process_pending_call('
- 'process_pending_call call'
- 'main:no_startup_worker'
- 'FastAPI lifespan does not auto-start the pending-call worker'
- 'disqualifying tokens: '
- 'operator'
- 'audit_service.py'
- 'audit_service:append_only_carry'
- 'Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)'
- 'docs:'
- ':clause:'
- ' carries clause: '
- 'expected one of: '
- ' | '
- 'no '
- 'no-'
- 'do not'
- "doesn't"
- 'does not'
- 'never '
- 'without '
- 'out of scope'
- 'not '
- 'deferred'
- ':no_forbidden_scope'
- ' does not introduce forbidden scope tokens'
- 'positive mentions of: '
- 'webapp:'
- 'Webapp carries anchor: '
- 'missing anchor '
- 'webapp:no_forbidden_capability'
- 'Webapp does not carry forbidden capability tokens'
- 'forbidden tokens: '
- 'dashboard_route:'
- ' missing'
- 'route file missing'
- 'Operator learning dashboard route token: '
- 'missing token '
- 'dashboard_route:no_'
- 'Operator learning dashboard route has no '
- ' declared in executable source'
- 'dashboard_route:no_live_mutation_imports'
- 'Operator learning dashboard route has no live-mutation imports'
- 'forbidden imports: '
- 'main:mount:'
- 'app/main.py mounts '
- 'missing mount token '
- 'dotenv import'
- 'supabase import'
- 'load_dotenv()'
- 'load_dotenv() call'
- 'environ read'
- 'get_supabase'
- 'supabase client call'
- 'self_check:no_env_or_db'
- 'PAS184 readiness checker never reads .env / touches DB'
- 'disqualifying patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS184'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas184_pilot_experience_readiness_check'
- 'PAS184 — Evaluate pilot experience polish (error banner + skeleton + ops playbook + read-only operator dashboard). Read-only — never reads .env, never touches Supabase, never runs a migration.'
- '--repo-root'
- '--output'
- '--json'
- 'store_true'
- '--summary-only'
- '--strict'
- 'report'
- 'None'
- '[PAS184] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS184] operator actions:'
- '  - '
- '  ... and '
- ' more (see report file)'
- 'payload'
- '  [warn] failed to write report at '
- 'argv'
- 'Optional[List[str]]'
- 'int'
- 'error: --repo-root not a directory: '

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ('\nPAS184 — Pilot experience polish readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS184 wired\ncorrectly and free of regressions in the PAS160-PAS183 +\nPAS-SECURITY-01/02/03/04 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS184 surfaces exist:\n      - docs/pas184_pilot_experience_polish.md\n      - docs/orvn_active_pilot_operating_playbook.md\n      - app/routes/operator_learning_dashboard.py\n      - scripts/pas184_pilot_experience_readiness_check.py\n      - tests/mvp/test_pas184_pilot_experience_polish.py\n  * Each PAS184 doc carries its required structural clauses.\n  * No PAS184 doc introduces forbidden scope tokens in a\n    positive sense.\n  * The webapp HTML still carries:\n      - `.pas-error-banner` class definition\n      - `.pas-skeleton` class definition\n      - the `window.PAS` JS helper namespace\n      - `errorBannerHtml` / `skeletonRowsHtml` helper functions\n  * The webapp does NOT introduce forbidden capability tokens.\n  * `operator_learning_dashboard.py` carries:\n      - `@router.get("/dashboard")` route\n      - `require_admin(` definition\n      - `check_rate_limit` + `surface="admin"` (PAS-SECURITY-04\n        pattern)\n      - NO `@router.post` declaration\n      - NO live-mutation imports\n      - aggregates the PAS180 / PAS181 / PAS182 read helpers\n  * `app/main.py` mounts `operator_learning_dashboard_router`.\n  * Memory Review surface (PAS147-PAS158) intact.\n  * audit_service.py has no UPDATE / DELETE helpers.\n  * Worker OFF by default and not auto-started.\n  * All PAS160-PAS183 + PAS-SECURITY-01/02/03/04 readiness\n    scripts still exist.\n  * Supports `--summary-only` / `--json`.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n')
               STORE_NAME               0 (__doc__)

  45           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  47           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  48           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  49           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  50           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  51           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  52           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  53           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  56           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  57           NOP

  58   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  56   L4:     END_FOR
               POP_ITER

  63           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  64           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  63           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  68           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  69           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  71           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  78           LOAD_CONST              67 (('docs/pas184_pilot_experience_polish.md', 'docs/orvn_active_pilot_operating_playbook.md', 'app/routes/operator_learning_dashboard.py', 'scripts/pas184_pilot_experience_readiness_check.py', 'tests/mvp/test_pas184_pilot_experience_polish.py'))
               STORE_NAME              28 (REQUIRED_FILES)

  86           LOAD_CONST              15 ('app/static/dashboard/index.html')
               STORE_NAME              29 (DASHBOARD_FILE)

  88           LOAD_CONST              68 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py', 'scripts/pas172_pilot_operations_readiness_check.py', 'scripts/pas173_brokerage_operator_readiness_check.py', 'scripts/pas174_operator_audit_readiness_check.py', 'scripts/pas175_audit_integrity_readiness_check.py', 'scripts/pas176_audit_chain_readiness_check.py', 'scripts/pas177_tenant_audit_verification_readiness_check.py', 'scripts/pas178_audit_window_chain_readiness_check.py', 'scripts/pas179_controlled_learning_readiness_check.py', 'scripts/pas180_learning_review_readiness_check.py', 'scripts/pas181_manual_test_harness_readiness_check.py', 'scripts/pas182_adaptive_memory_bridge_readiness_check.py', 'scripts/pas183_onboarding_product_readiness_check.py', 'scripts/pas_security_01_hardening_readiness_check.py', 'scripts/pas_security_02_rate_limit_scanner_readiness_check.py', 'scripts/pas_security_03_admin_webhook_ci_readiness_check.py', 'scripts/pas_security_04_operator_reveal_https_readiness_check.py'))
               STORE_NAME              30 (PRIOR_PHASE_FILES)

 121           LOAD_CONST              69 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              31 (MEMORY_REVIEW_FILES)

 134           LOAD_CONST              12 ('docs/pas184_pilot_experience_polish.md')
               LOAD_CONST              70 ((('hard-constraints', ('hard constraints',)), ('no-broad-redesign', ('no broad ui redesign',)), ('no-memory-review', ('no memory review ui', 'memory review ui')), ('no-gmail', ('no gmail',)), ('no-composio', ('no composio',)), ('no-ai-chat', ('no ai chat',)), ('error-banner', ('error banner',)), ('skeleton', ('skeleton',)), ('operator-dashboard', ('operator learning dashboard', 'learning dashboard')), ('read-only', ('read-only',)), ('never-raises', ('never raises',)), ('worker-off', ('worker remains off', 'worker stays off')), ('deliberately-not-built', ('deliberately not build', 'deliberately does not', 'deliberately not'))))

 154           LOAD_CONST              13 ('docs/orvn_active_pilot_operating_playbook.md')
               LOAD_CONST              71 ((('week-0', ('week 0',)), ('week-1', ('week 1',)), ('week-2', ('week 2',)), ('daily-health-snapshot', ('daily health snapshot', '6-point')), ('escalation', ('escalation',)), ('metrics', ('metrics',)), ('rollback', ('rollback',)), ('daily-checks', ('daily',)), ('no-auto-approval', ('auto-approve memory', 'auto approve memory')), ('no-gmail', ('no gmail',)), ('no-composio', ('no composio',)), ('end-of-week-4', ('end of week 4', 'week 4 pilot review'))))

 133           BUILD_MAP                2
               STORE_NAME              32 (DOC_REQUIRED_CLAUSES)

 176           LOAD_CONST              72 (('gmail oauth', 'imap', 'pop3', 'composio', 'trustclaw', 'auto-approve', 'auto approve', 'ai chat assistant', 'embedding', 'vector database', 'vector db'))
               STORE_NAME              33 (FORBIDDEN_DOC_TOKENS)

 192           LOAD_CONST              73 (('gmail oauth', 'google.oauth2', 'composio', 'trustclaw', 'ai chat assistant', 'chatgpt assistant', 'anthropic api key'))
               STORE_NAME              34 (FORBIDDEN_WEBAPP_TOKENS)

 204           LOAD_CONST              74 ((('pas184:error-banner-class', '.pas-error-banner'), ('pas184:skeleton-class', '.pas-skeleton'), ('pas184:js-namespace', 'window.PAS'), ('pas184:js-error-helper', 'errorBannerHtml'), ('pas184:js-skeleton-helper', 'skeletonRowsHtml'), ('pas184:js-error-code-label', 'errorCodeLabel'), ('pas184:legacy-loading-box', '.loading-box'), ('pas184:legacy-spinner', '.spinner'), ('pas184:legacy-empty-box', '.empty-box')))
               STORE_NAME              35 (WEBAPP_REQUIRED_ANCHORS)

 218           LOAD_CONST              14 ('app/routes/operator_learning_dashboard.py')
               STORE_NAME              36 (DASHBOARD_ROUTE_FILE)

 219           LOAD_CONST              75 (('@router.get("/dashboard")', 'def require_admin(', 'check_rate_limit', 'surface="admin"', 'list_learning_recommendations', 'manual_test_run_report', 'adaptive_memory_bridge_report', '_scan_for_forbidden', '_final_envelope'))
               STORE_NAME              37 (DASHBOARD_REQUIRED_TOKENS)

 231           LOAD_CONST              76 (('@router.post', '@router.patch', '@router.delete'))
               STORE_NAME              38 (DASHBOARD_FORBIDDEN_TOKENS)

 239           LOAD_CONST              77 (('from app.engine.state_machine', 'import app.engine.state_machine', 'from app.services.memory.review', 'import app.services.memory.review', 'from app.services.memory.approval', 'import app.services.memory.approval', 'from app.services.booking', 'import app.services.booking', 'from app.services.outbound', 'import app.services.outbound', 'from app.services.worker', 'import app.services.worker', 'from app.services.ingestion.worker', 'import app.services.ingestion.worker', 'from app.services.slack', 'import app.services.slack', 'from anthropic', 'import anthropic', 'from openai', 'import openai', 'import chromadb', 'import pinecone', 'from pinecone', 'import pgvector', 'from pgvector'))
               STORE_NAME              39 (DASHBOARD_FORBIDDEN_IMPORT_PREFIXES)

 272           LOAD_CONST              16 ('severity')

 274           LOAD_NAME               27 (SEVERITY_BLOCK)

 272           LOAD_CONST              17 ('detail')

 274           LOAD_CONST              18 ('')

 272           BUILD_MAP                2
               LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18025530, file "scripts\pas184_pilot_experience_readiness_check.py", line 272>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object _check at 0x0000018C17FA3B40, file "scripts\pas184_pilot_experience_readiness_check.py", line 272>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              40 (_check)

 285           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pas184_pilot_experience_readiness_check.py", line 285>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object _now_iso at 0x0000018C18038F30, file "scripts\pas184_pilot_experience_readiness_check.py", line 285>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (_now_iso)

 289           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts\pas184_pilot_experience_readiness_check.py", line 289>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object _read_text at 0x0000018C18053AB0, file "scripts\pas184_pilot_experience_readiness_check.py", line 289>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (_read_text)

 296           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts\pas184_pilot_experience_readiness_check.py", line 296>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object _strip_python_comments_and_strings at 0x0000018C17D52020, file "scripts\pas184_pilot_experience_readiness_check.py", line 296>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_strip_python_comments_and_strings)

 335           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas184_pilot_experience_readiness_check.py", line 335>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object check_files_present at 0x0000018C180612C0, file "scripts\pas184_pilot_experience_readiness_check.py", line 335>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (check_files_present)

 348           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas184_pilot_experience_readiness_check.py", line 348>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts\pas184_pilot_experience_readiness_check.py", line 348>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (check_prior_phases_intact)

 361           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas184_pilot_experience_readiness_check.py", line 361>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object check_memory_review_intact at 0x0000018C180608A0, file "scripts\pas184_pilot_experience_readiness_check.py", line 361>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_memory_review_intact)

 374           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas184_pilot_experience_readiness_check.py", line 374>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object check_worker_off_by_default at 0x0000018C179C3C30, file "scripts\pas184_pilot_experience_readiness_check.py", line 374>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_worker_off_by_default)

 391           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas184_pilot_experience_readiness_check.py", line 391>)
               MAKE_FUNCTION
               LOAD_CONST              36 (<code object check_no_startup_worker at 0x0000018C17D872F0, file "scripts\pas184_pilot_experience_readiness_check.py", line 391>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_no_startup_worker)

 414           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas184_pilot_experience_readiness_check.py", line 414>)
               MAKE_FUNCTION
               LOAD_CONST              38 (<code object check_audit_service_invariant at 0x0000018C182DC9E0, file "scripts\pas184_pilot_experience_readiness_check.py", line 414>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_audit_service_invariant)

 439           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pas184_pilot_experience_readiness_check.py", line 439>)
               MAKE_FUNCTION
               LOAD_CONST              40 (<code object check_doc_required_clauses at 0x0000018C17E7E760, file "scripts\pas184_pilot_experience_readiness_check.py", line 439>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_doc_required_clauses)

 457           LOAD_CONST              41 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas184_pilot_experience_readiness_check.py", line 457>)
               MAKE_FUNCTION
               LOAD_CONST              42 (<code object check_doc_no_forbidden_scope at 0x0000018C17D83B90, file "scripts\pas184_pilot_experience_readiness_check.py", line 457>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_doc_no_forbidden_scope)

 498           LOAD_CONST              43 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas184_pilot_experience_readiness_check.py", line 498>)
               MAKE_FUNCTION
               LOAD_CONST              44 (<code object check_webapp_anchors at 0x0000018C17F78AB0, file "scripts\pas184_pilot_experience_readiness_check.py", line 498>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_webapp_anchors)

 525           LOAD_CONST              45 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas184_pilot_experience_readiness_check.py", line 525>)
               MAKE_FUNCTION
               LOAD_CONST              46 (<code object check_dashboard_route at 0x0000018C1778B3F0, file "scripts\pas184_pilot_experience_readiness_check.py", line 525>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_dashboard_route)

 573           LOAD_CONST              47 (<code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas184_pilot_experience_readiness_check.py", line 573>)
               MAKE_FUNCTION
               LOAD_CONST              48 (<code object check_main_router_mount at 0x0000018C180FC5D0, file "scripts\pas184_pilot_experience_readiness_check.py", line 573>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_main_router_mount)

 591           LOAD_CONST              49 (<code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas184_pilot_experience_readiness_check.py", line 591>)
               MAKE_FUNCTION
               LOAD_CONST              50 (<code object check_self_no_env_or_db at 0x0000018C17D88130, file "scripts\pas184_pilot_experience_readiness_check.py", line 591>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_self_no_env_or_db)

 624           LOAD_CONST              51 (<code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas184_pilot_experience_readiness_check.py", line 624>)
               MAKE_FUNCTION
               LOAD_CONST              52 (<code object _aggregate at 0x0000018C17FA92F0, file "scripts\pas184_pilot_experience_readiness_check.py", line 624>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (_aggregate)

 636           LOAD_CONST              53 (<code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas184_pilot_experience_readiness_check.py", line 636>)
               MAKE_FUNCTION
               LOAD_CONST              54 (<code object _operator_actions at 0x0000018C18048AB0, file "scripts\pas184_pilot_experience_readiness_check.py", line 636>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (_operator_actions)

 646           LOAD_CONST              55 (<code object __annotate__ at 0x0000018C17FA25B0, file "scripts\pas184_pilot_experience_readiness_check.py", line 646>)
               MAKE_FUNCTION
               LOAD_CONST              56 (<code object evaluate at 0x0000018C17EDA310, file "scripts\pas184_pilot_experience_readiness_check.py", line 646>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (evaluate)

 677           LOAD_CONST              57 ('pas184_pilot_experience_readiness_report.json')
               STORE_NAME              59 (REPORT_FILENAME)

 680           LOAD_CONST              58 (<code object __annotate__ at 0x0000018C17FA2D30, file "scripts\pas184_pilot_experience_readiness_check.py", line 680>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object _build_parser at 0x0000018C180FCB70, file "scripts\pas184_pilot_experience_readiness_check.py", line 680>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (_build_parser)

 698           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas184_pilot_experience_readiness_check.py", line 698>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object _print_summary at 0x0000018C17D8E300, file "scripts\pas184_pilot_experience_readiness_check.py", line 698>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (_print_summary)

 716           LOAD_CONST              62 (<code object __annotate__ at 0x0000018C18026530, file "scripts\pas184_pilot_experience_readiness_check.py", line 716>)
               MAKE_FUNCTION
               LOAD_CONST              63 (<code object _write_report at 0x0000018C180FC210, file "scripts\pas184_pilot_experience_readiness_check.py", line 716>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (_write_report)

 730           LOAD_CONST              78 ((None,))
               LOAD_CONST              64 (<code object __annotate__ at 0x0000018C17FA2C40, file "scripts\pas184_pilot_experience_readiness_check.py", line 730>)
               MAKE_FUNCTION
               LOAD_CONST              65 (<code object main at 0x0000018C17D88FF0, file "scripts\pas184_pilot_experience_readiness_check.py", line 730>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              63 (main)

 755           LOAD_NAME               64 (__name__)
               LOAD_CONST              66 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 756           LOAD_NAME                6 (sys)
               LOAD_ATTR              130 (exit)
               PUSH_NULL
               LOAD_NAME               63 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 755   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  59           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  60   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          331 (to L1)

  59   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "scripts\pas184_pilot_experience_readiness_check.py", line 272>:
272           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

273           LOAD_CONST               2 ('str')

272           LOAD_CONST               3 ('status')

273           LOAD_CONST               2 ('str')

272           LOAD_CONST               4 ('label')

273           LOAD_CONST               2 ('str')

272           LOAD_CONST               5 ('severity')

274           LOAD_CONST               2 ('str')

272           LOAD_CONST               6 ('detail')

274           LOAD_CONST               2 ('str')

272           LOAD_CONST               7 ('return')

275           LOAD_CONST               8 ('dict')

272           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA3B40, file "scripts\pas184_pilot_experience_readiness_check.py", line 272>:
272           RESUME                   0

277           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

278           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

279           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

280           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

281           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

276           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pas184_pilot_experience_readiness_check.py", line 285>:
285           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038F30, file "scripts\pas184_pilot_experience_readiness_check.py", line 285>:
285           RESUME                   0

286           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts\pas184_pilot_experience_readiness_check.py", line 289>:
289           RESUME                   0
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
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _read_text at 0x0000018C18053AB0, file "scripts\pas184_pilot_experience_readiness_check.py", line 289>:
 289           RESUME                   0

 290           NOP

 291   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 292           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 293   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 292   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts\pas184_pilot_experience_readiness_check.py", line 296>:
296           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('src')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17D52020, file "scripts\pas184_pilot_experience_readiness_check.py", line 296>:
296            RESUME                   0

297            BUILD_LIST               0
               STORE_FAST               1 (out)

298            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

299    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

300            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

301            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

302            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

303            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

304            JUMP_FORWARD           240 (to L13)

305    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

306            JUMP_BACKWARD           59 (to L1)

307    L3:     LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST               3 ('"""')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        25 (to L4)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST               4 ("'''")
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       55 (to L6)
               NOT_TAKEN

308    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

309            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

310            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

311            JUMP_FORWARD           138 (to L13)

312    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

313            JUMP_BACKWARD          161 (to L1)

314    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

315            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

316            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

317    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

318            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

319            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

320            JUMP_BACKWARD           30 (to L7)

321    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_FAST_BORROW         6 (quote)
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_TRUE        14 (to L9)
               NOT_TAKEN
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               2 ('\n')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        2 (to L10)
               NOT_TAKEN

322    L9:     JUMP_FORWARD            11 (to L11)

323   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

324   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

325            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

326   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

327            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

328   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas184_pilot_experience_readiness_check.py", line 335>:
335           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C180612C0, file "scripts\pas184_pilot_experience_readiness_check.py", line 335>:
335           RESUME                   0

336           BUILD_LIST               0
              STORE_FAST               1 (out)

337           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

338           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

339           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

340           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

341           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

342   L3:     LOAD_CONST               3 ('Required PAS184 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

343           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

339   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

337   L6:     END_FOR
              POP_ITER

345           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas184_pilot_experience_readiness_check.py", line 348>:
348           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts\pas184_pilot_experience_readiness_check.py", line 348>:
348           RESUME                   0

349           BUILD_LIST               0
              STORE_FAST               1 (out)

350           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

351           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

352           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

353           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

354           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

355   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

356           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS184 must not delete')

352   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

350   L6:     END_FOR
              POP_ITER

358           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas184_pilot_experience_readiness_check.py", line 361>:
361           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C180608A0, file "scripts\pas184_pilot_experience_readiness_check.py", line 361>:
361           RESUME                   0

362           BUILD_LIST               0
              STORE_FAST               1 (out)

363           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

364           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

365           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

366           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

367           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

368   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

369           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS184 must not touch')

365   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

363   L6:     END_FOR
              POP_ITER

371           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas184_pilot_experience_readiness_check.py", line 374>:
374           RESUME                   0
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C179C3C30, file "scripts\pas184_pilot_experience_readiness_check.py", line 374>:
374           RESUME                   0

375           BUILD_LIST               0
              STORE_FAST               1 (out)

376           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('ingestion')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('worker.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

377           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

379           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

380           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

378   L2:     STORE_FAST               4 (literal_ok)

382           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

383           LOAD_CONST               7 ('worker:off_by_default')

384           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

385   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default')

386           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

382   L6:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

388           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas184_pilot_experience_readiness_check.py", line 391>:
391           RESUME                   0
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

Disassembly of <code object check_no_startup_worker at 0x0000018C17D872F0, file "scripts\pas184_pilot_experience_readiness_check.py", line 391>:
391           RESUME                   0

392           BUILD_LIST               0
              STORE_FAST               1 (out)

393           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

394           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

395           LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (executable)

396           BUILD_LIST               0
              STORE_FAST               5 (bad)

397           LOAD_CONST               3 ('from app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L2)
              NOT_TAKEN

398           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               4 ('from app.services.ingestion.worker import …')
              CALL                     1
              POP_TOP

399   L2:     LOAD_CONST               5 ('import app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L3)
              NOT_TAKEN

400           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               5 ('import app.services.ingestion.worker')
              CALL                     1
              POP_TOP

401   L3:     LOAD_CONST               6 ('run_worker_loop')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L4)
              NOT_TAKEN

402           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               7 ('run_worker_loop reference')
              CALL                     1
              POP_TOP

403   L4:     LOAD_CONST               8 ('process_pending_call(')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L5)
              NOT_TAKEN

404           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               9 ('process_pending_call call')
              CALL                     1
              POP_TOP

405   L5:     LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

406           LOAD_CONST              10 ('main:no_startup_worker')

407           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST              11 ('FAIL')
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST              12 ('PASS')

408   L7:     LOAD_CONST              13 ('FastAPI lifespan does not auto-start the pending-call worker')

409           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L8)
              NOT_TAKEN
              LOAD_CONST              14 ('disqualifying tokens: ')
              LOAD_CONST              15 (', ')
              LOAD_ATTR               11 (join + NULL|self)
              LOAD_FAST_BORROW         5 (bad)
              CALL                     1
              BINARY_OP                0 (+)
              JUMP_FORWARD             1 (to L9)
      L8:     LOAD_CONST               2 ('')

405   L9:     LOAD_CONST              16 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

411           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas184_pilot_experience_readiness_check.py", line 414>:
414           RESUME                   0
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

Disassembly of <code object check_audit_service_invariant at 0x0000018C182DC9E0, file "scripts\pas184_pilot_experience_readiness_check.py", line 414>:
414           RESUME                   0

415           BUILD_LIST               0
              STORE_FAST               1 (out)

416           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('operator')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('audit_service.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

417           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

418           LOAD_CONST              12 (('def update_audit_', 'def delete_audit_', 'def update_operator_audit_', 'def delete_operator_audit_', 'def mutate_audit_', 'def truncate_audit_'))
              STORE_FAST               4 (forbidden)

426           BUILD_LIST               0
              STORE_FAST               5 (bad)

427           LOAD_FAST_BORROW         4 (forbidden)
              GET_ITER
      L2:     FOR_ITER                28 (to L4)
              STORE_FAST               6 (tok)

428           LOAD_FAST_BORROW_LOAD_FAST_BORROW 99 (tok, src)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

429   L3:     LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW         6 (tok)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           30 (to L2)

427   L4:     END_FOR
              POP_ITER

430           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

431           LOAD_CONST               5 ('audit_service:append_only_carry')

432           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               6 ('FAIL')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               7 ('PASS')

433   L6:     LOAD_CONST               8 ('Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)')

434           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L7)
              NOT_TAKEN
              LOAD_CONST               9 ('disqualifying tokens: ')
              LOAD_CONST              10 (', ')
              LOAD_ATTR                9 (join + NULL|self)
              LOAD_FAST_BORROW         5 (bad)
              CALL                     1
              BINARY_OP                0 (+)
              JUMP_FORWARD             1 (to L8)
      L7:     LOAD_CONST               4 ('')

430   L8:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

436           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pas184_pilot_experience_readiness_check.py", line 439>:
439           RESUME                   0
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

Disassembly of <code object check_doc_required_clauses at 0x0000018C17E7E760, file "scripts\pas184_pilot_experience_readiness_check.py", line 439>:
  --            MAKE_CELL                9 (lower)

 439            RESUME                   0

 440            BUILD_LIST               0
                STORE_FAST               1 (out)

 441            LOAD_GLOBAL              0 (DOC_REQUIRED_CLAUSES)
                LOAD_ATTR                3 (items + NULL|self)
                CALL                     0
                GET_ITER
        L1:     FOR_ITER               212 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   35 (relpath, clauses)

 442            LOAD_GLOBAL              5 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_FAST_BORROW         2 (relpath)
                BINARY_OP               11 (/)
                STORE_FAST               4 (p)

 443            LOAD_GLOBAL              7 (_read_text + NULL)
                LOAD_FAST_BORROW         4 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 ('')
        L2:     STORE_FAST               5 (src)

 444            LOAD_FAST_BORROW         5 (src)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              9 (lower)

 445            LOAD_FAST_BORROW         3 (clauses)
                GET_ITER
        L3:     FOR_ITER               146 (to L13)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  103 (name, phrases)

 446            LOAD_GLOBAL             10 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L7)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         9 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18024E30, file "scripts\pas184_pilot_experience_readiness_check.py", line 446>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         7 (phrases)
                GET_ITER
                CALL                     0
        L4:     FOR_ITER                12 (to L6)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L4)
        L5:     POP_ITER
                LOAD_CONST               2 (True)
                JUMP_FORWARD            20 (to L8)
        L6:     END_FOR
                POP_ITER
                LOAD_CONST               3 (False)
                JUMP_FORWARD            16 (to L8)
        L7:     PUSH_NULL
                LOAD_FAST_BORROW         9 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18024E30, file "scripts\pas184_pilot_experience_readiness_check.py", line 446>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         7 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L8:     STORE_FAST               8 (present)

 447            LOAD_FAST                1 (out)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_GLOBAL             15 (_check + NULL)

 448            LOAD_CONST               4 ('docs:')
                LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                LOAD_CONST               5 (':clause:')
                LOAD_FAST_BORROW         6 (name)
                FORMAT_SIMPLE
                BUILD_STRING             4

 449            LOAD_FAST_BORROW         8 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST               6 ('PASS')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               7 ('FAIL')

 450   L10:     LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                LOAD_CONST               8 (' carries clause: ')
                LOAD_FAST_BORROW         6 (name)
                FORMAT_SIMPLE
                BUILD_STRING             3

 452            LOAD_FAST_BORROW         8 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L11)
                NOT_TAKEN

 451            LOAD_CONST               9 ('expected one of: ')
                LOAD_CONST              10 (' | ')
                LOAD_ATTR               17 (join + NULL|self)
                LOAD_FAST_BORROW         7 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L12)

 452   L11:     LOAD_CONST               0 ('')

 447   L12:     LOAD_CONST              11 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L3)

 445   L13:     END_FOR
                POP_ITER
                JUMP_BACKWARD          214 (to L1)

 441   L14:     END_FOR
                POP_ITER

 454            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18024E30, file "scripts\pas184_pilot_experience_readiness_check.py", line 446>:
  --           COPY_FREE_VARS           1

 446           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (p, p)
               LOAD_DEREF               2 (lower)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas184_pilot_experience_readiness_check.py", line 457>:
457           RESUME                   0
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

Disassembly of <code object check_doc_no_forbidden_scope at 0x0000018C17D83B90, file "scripts\pas184_pilot_experience_readiness_check.py", line 457>:
457            RESUME                   0

458            BUILD_LIST               0
               STORE_FAST               1 (out)

459            LOAD_CONST              22 (('docs/pas184_pilot_experience_polish.md', 'docs/orvn_active_pilot_operating_playbook.md'))
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               430 (to L13)
               STORE_FAST               2 (relpath)

463            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         2 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               3 (p)

464            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         3 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               4 (src)

465            LOAD_FAST_BORROW         4 (src)
               LOAD_ATTR                5 (lower + NULL|self)
               CALL                     0
               STORE_FAST               5 (lower)

466            BUILD_LIST               0
               STORE_FAST               6 (bad)

467            LOAD_GLOBAL              6 (FORBIDDEN_DOC_TOKENS)
               GET_ITER
       L3:     EXTENDED_ARG             1
               FOR_ITER               261 (to L8)
               STORE_FAST               7 (tok)

468            LOAD_FAST_BORROW         5 (lower)
               LOAD_ATTR                9 (find + NULL|self)
               LOAD_FAST_BORROW         7 (tok)
               CALL                     1
               STORE_FAST               8 (idx)

469    L4:     LOAD_FAST_BORROW         8 (idx)
               LOAD_SMALL_INT           0
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           30 (to L3)

470    L5:     LOAD_FAST_BORROW         5 (lower)
               LOAD_GLOBAL             11 (max + NULL)
               LOAD_SMALL_INT           0
               LOAD_FAST_BORROW         8 (idx)
               LOAD_SMALL_INT          30
               BINARY_OP               10 (-)
               CALL                     2
               LOAD_FAST_BORROW         8 (idx)
               BINARY_SLICE
               STORE_FAST               9 (preceding)

472            LOAD_CONST               2 ('no ')
               LOAD_FAST_BORROW         9 (preceding)
               LOAD_CONST              23 (-12)
               LOAD_CONST               3 (None)
               BINARY_SLICE
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE       135 (to L6)
               NOT_TAKEN
               POP_TOP

473            LOAD_CONST               4 ('no-')
               LOAD_FAST_BORROW         9 (preceding)
               LOAD_CONST              23 (-12)
               LOAD_CONST               3 (None)
               BINARY_SLICE
               CONTAINS_OP              0 (in)

472            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE       119 (to L6)
               NOT_TAKEN
               POP_TOP

474            LOAD_CONST               5 ('❌')
               LOAD_FAST_BORROW         9 (preceding)
               CONTAINS_OP              0 (in)

472            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE       106 (to L6)
               NOT_TAKEN
               POP_TOP

475            LOAD_CONST               6 ('do not')
               LOAD_FAST_BORROW         9 (preceding)
               CONTAINS_OP              0 (in)

472            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        93 (to L6)
               NOT_TAKEN
               POP_TOP

476            LOAD_CONST               7 ("doesn't")
               LOAD_FAST_BORROW         9 (preceding)
               CONTAINS_OP              0 (in)

472            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        80 (to L6)
               NOT_TAKEN
               POP_TOP

477            LOAD_CONST               8 ('does not')
               LOAD_FAST_BORROW         9 (preceding)
               CONTAINS_OP              0 (in)

472            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        67 (to L6)
               NOT_TAKEN
               POP_TOP

478            LOAD_CONST               9 ('never ')
               LOAD_FAST_BORROW         9 (preceding)
               LOAD_CONST              24 (-15)
               LOAD_CONST               3 (None)
               BINARY_SLICE
               CONTAINS_OP              0 (in)

472            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        51 (to L6)
               NOT_TAKEN
               POP_TOP

479            LOAD_CONST              10 ('without ')
               LOAD_FAST_BORROW         9 (preceding)
               LOAD_CONST              24 (-15)
               LOAD_CONST               3 (None)
               BINARY_SLICE
               CONTAINS_OP              0 (in)

472            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        35 (to L6)
               NOT_TAKEN
               POP_TOP

480            LOAD_CONST              11 ('out of scope')
               LOAD_FAST_BORROW         9 (preceding)
               CONTAINS_OP              0 (in)

472            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        22 (to L6)
               NOT_TAKEN
               POP_TOP

481            LOAD_CONST              12 ('not ')
               LOAD_FAST_BORROW         9 (preceding)
               LOAD_CONST              25 (-10)
               LOAD_CONST               3 (None)
               BINARY_SLICE
               CONTAINS_OP              0 (in)

472            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L6)
               NOT_TAKEN
               POP_TOP

482            LOAD_CONST              13 ('deferred')
               LOAD_FAST_BORROW         9 (preceding)
               CONTAINS_OP              0 (in)

471    L6:     STORE_FAST              10 (negated)

484            LOAD_FAST_BORROW        10 (negated)
               TO_BOOL
               POP_JUMP_IF_TRUE        20 (to L7)
               NOT_TAKEN

485            LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_FAST_BORROW         7 (tok)
               CALL                     1
               POP_TOP

486            JUMP_BACKWARD          229 (to L3)

487    L7:     LOAD_FAST_BORROW         5 (lower)
               LOAD_ATTR                9 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (tok, idx)
               LOAD_GLOBAL             15 (len + NULL)
               LOAD_FAST_BORROW         7 (tok)
               CALL                     1
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               8 (idx)
               JUMP_BACKWARD          243 (to L4)

467    L8:     END_FOR
               POP_ITER

488            LOAD_FAST                1 (out)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

489            LOAD_CONST              14 ('docs:')
               LOAD_FAST_BORROW         2 (relpath)
               FORMAT_SIMPLE
               LOAD_CONST              15 (':no_forbidden_scope')
               BUILD_STRING             3

490            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST              16 ('FAIL')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST              17 ('PASS')

491   L10:     LOAD_FAST_BORROW         2 (relpath)
               FORMAT_SIMPLE
               LOAD_CONST              18 (' does not introduce forbidden scope tokens')
               BUILD_STRING             2

493            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L11)
               NOT_TAKEN

492            LOAD_CONST              19 ('positive mentions of: ')
               LOAD_CONST              20 (', ')
               LOAD_ATTR               19 (join + NULL|self)
               LOAD_GLOBAL             21 (sorted + NULL)
               LOAD_GLOBAL             23 (set + NULL)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               CALL                     1
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L12)

493   L11:     LOAD_CONST               1 ('')

488   L12:     LOAD_CONST              21 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          433 (to L1)

459   L13:     END_FOR
               POP_ITER

495            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas184_pilot_experience_readiness_check.py", line 498>:
498           RESUME                   0
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

Disassembly of <code object check_webapp_anchors at 0x0000018C17F78AB0, file "scripts\pas184_pilot_experience_readiness_check.py", line 498>:
498            RESUME                   0

499            BUILD_LIST               0
               STORE_FAST               1 (out)

500            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_GLOBAL              2 (DASHBOARD_FILE)
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

501            LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

502            LOAD_GLOBAL              6 (WEBAPP_REQUIRED_ANCHORS)
               GET_ITER
       L2:     FOR_ITER                61 (to L7)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   69 (name, anchor)

503            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

504            LOAD_CONST               1 ('webapp:')
               LOAD_FAST_BORROW         4 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

505            LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (anchor, src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               2 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               3 ('FAIL')

506    L4:     LOAD_CONST               4 ('Webapp carries anchor: ')
               LOAD_FAST_BORROW         4 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

507            LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (anchor, src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               0 ('')
               JUMP_FORWARD             5 (to L6)
       L5:     LOAD_CONST               5 ('missing anchor ')
               LOAD_FAST_BORROW         5 (anchor)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2

503    L6:     LOAD_CONST               6 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           63 (to L2)

502    L7:     END_FOR
               POP_ITER

510            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR               13 (lower + NULL|self)
               CALL                     0
               STORE_FAST               6 (lower)

511            BUILD_LIST               0
               STORE_FAST               7 (bad)

512            LOAD_GLOBAL             14 (FORBIDDEN_WEBAPP_TOKENS)
               GET_ITER
       L8:     FOR_ITER                28 (to L10)
               STORE_FAST               8 (tok)

513            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (tok, lower)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L8)

514    L9:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_FAST_BORROW         8 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L8)

512   L10:     END_FOR
               POP_ITER

515            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

516            LOAD_CONST               7 ('webapp:no_forbidden_capability')

517            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               2 ('PASS')

518   L12:     LOAD_CONST               8 ('Webapp does not carry forbidden capability tokens')

520            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L13)
               NOT_TAKEN

519            LOAD_CONST               9 ('forbidden tokens: ')
               LOAD_CONST              10 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_GLOBAL             19 (sorted + NULL)
               LOAD_GLOBAL             21 (set + NULL)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               CALL                     1
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)

520   L13:     LOAD_CONST               0 ('')

515   L14:     LOAD_CONST               6 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

522            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas184_pilot_experience_readiness_check.py", line 525>:
525           RESUME                   0
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

Disassembly of <code object check_dashboard_route at 0x0000018C1778B3F0, file "scripts\pas184_pilot_experience_readiness_check.py", line 525>:
525            RESUME                   0

526            BUILD_LIST               0
               STORE_FAST               1 (out)

527            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_GLOBAL              2 (DASHBOARD_ROUTE_FILE)
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

528            LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

529            LOAD_FAST_BORROW         3 (src)
               TO_BOOL
               POP_JUMP_IF_TRUE        47 (to L2)
               NOT_TAKEN

530            LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

531            LOAD_CONST               1 ('dashboard_route:')
               LOAD_GLOBAL              2 (DASHBOARD_ROUTE_FILE)
               FORMAT_SIMPLE
               BUILD_STRING             2

532            LOAD_CONST               2 ('FAIL')

533            LOAD_GLOBAL              2 (DASHBOARD_ROUTE_FILE)
               FORMAT_SIMPLE
               LOAD_CONST               3 (' missing')
               BUILD_STRING             2

534            LOAD_CONST               4 ('route file missing')

530            LOAD_CONST               5 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

536            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

537    L2:     LOAD_GLOBAL             10 (DASHBOARD_REQUIRED_TOKENS)
               GET_ITER
       L3:     FOR_ITER                73 (to L8)
               STORE_FAST               4 (tok)

538            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

539            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

540            LOAD_CONST               1 ('dashboard_route:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               6 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

541            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L5)
       L4:     LOAD_CONST               2 ('FAIL')

542    L5:     LOAD_CONST               8 ('Operator learning dashboard route token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

543            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               0 ('')
               JUMP_FORWARD             4 (to L7)
       L6:     LOAD_CONST               9 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

539    L7:     LOAD_CONST               5 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L3)

537    L8:     END_FOR
               POP_ITER

545            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

546            LOAD_GLOBAL             14 (DASHBOARD_FORBIDDEN_TOKENS)
               GET_ITER
       L9:     FOR_ITER                66 (to L14)
               STORE_FAST               4 (tok)

547            LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (tok, executable)
               CONTAINS_OP              0 (in)
               STORE_FAST               7 (present)

548            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

549            LOAD_CONST              10 ('dashboard_route:no_')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

550            LOAD_FAST_BORROW         7 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               2 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST               7 ('PASS')

551   L11:     LOAD_CONST              11 ('Operator learning dashboard route has no ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

552            LOAD_FAST_BORROW         7 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L12)
               NOT_TAKEN
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               LOAD_CONST              12 (' declared in executable source')
               BUILD_STRING             2
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST               0 ('')

548   L13:     LOAD_CONST               5 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           68 (to L9)

546   L14:     END_FOR
               POP_ITER

555            BUILD_LIST               0
               STORE_FAST               8 (bad)

556            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR               17 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
      L15:     FOR_ITER               107 (to L21)
               STORE_FAST               9 (line)

557            LOAD_FAST_BORROW         9 (line)
               LOAD_ATTR               19 (strip + NULL|self)
               CALL                     0
               STORE_FAST              10 (stripped)

558            LOAD_FAST_BORROW        10 (stripped)
               TO_BOOL
               POP_JUMP_IF_FALSE       24 (to L16)
               NOT_TAKEN
               LOAD_FAST_BORROW        10 (stripped)
               LOAD_ATTR               21 (startswith + NULL|self)
               LOAD_CONST              13 ('#')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L17)
               NOT_TAKEN

559   L16:     JUMP_BACKWARD           52 (to L15)

560   L17:     LOAD_GLOBAL             22 (DASHBOARD_FORBIDDEN_IMPORT_PREFIXES)
               GET_ITER
      L18:     FOR_ITER                45 (to L20)
               STORE_FAST              11 (prefix)

561            LOAD_FAST_BORROW        10 (stripped)
               LOAD_ATTR               21 (startswith + NULL|self)
               LOAD_FAST_BORROW        11 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L19)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L18)

562   L19:     LOAD_FAST_BORROW         8 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW        11 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L18)

560   L20:     END_FOR
               POP_ITER
               JUMP_BACKWARD          109 (to L15)

556   L21:     END_FOR
               POP_ITER

563            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

564            LOAD_CONST              14 ('dashboard_route:no_live_mutation_imports')

565            LOAD_FAST_BORROW         8 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L22)
               NOT_TAKEN
               LOAD_CONST               2 ('FAIL')
               JUMP_FORWARD             1 (to L23)
      L22:     LOAD_CONST               7 ('PASS')

566   L23:     LOAD_CONST              15 ('Operator learning dashboard route has no live-mutation imports')

568            LOAD_FAST_BORROW         8 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L24)
               NOT_TAKEN

567            LOAD_CONST              16 ('forbidden imports: ')
               LOAD_CONST              17 (', ')
               LOAD_ATTR               25 (join + NULL|self)
               LOAD_GLOBAL             27 (sorted + NULL)
               LOAD_GLOBAL             29 (set + NULL)
               LOAD_FAST_BORROW         8 (bad)
               CALL                     1
               CALL                     1
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L25)

568   L24:     LOAD_CONST               0 ('')

563   L25:     LOAD_CONST               5 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

570            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas184_pilot_experience_readiness_check.py", line 573>:
573           RESUME                   0
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

Disassembly of <code object check_main_router_mount at 0x0000018C180FC5D0, file "scripts\pas184_pilot_experience_readiness_check.py", line 573>:
573           RESUME                   0

574           BUILD_LIST               0
              STORE_FAST               1 (out)

575           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

576           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

577           LOAD_CONST              10 (('operator_learning_dashboard_router',))
              STORE_FAST               4 (required)

580           LOAD_FAST_BORROW         4 (required)
              GET_ITER
      L2:     FOR_ITER                74 (to L7)
              STORE_FAST               5 (tok)

581           LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               6 (ok)

582           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

583           LOAD_CONST               3 ('main:mount:')
              LOAD_FAST_BORROW         5 (tok)
              LOAD_CONST               4 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

584           LOAD_FAST_BORROW         6 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               5 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               6 ('FAIL')

585   L4:     LOAD_CONST               7 ('app/main.py mounts ')
              LOAD_FAST_BORROW         5 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

586           LOAD_FAST_BORROW         6 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               2 ('')
              JUMP_FORWARD             5 (to L6)
      L5:     LOAD_CONST               8 ('missing mount token ')
              LOAD_FAST_BORROW         5 (tok)
              CONVERT_VALUE            2 (repr)
              FORMAT_SIMPLE
              BUILD_STRING             2

582   L6:     LOAD_CONST               9 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           76 (to L2)

580   L7:     END_FOR
              POP_ITER

588           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas184_pilot_experience_readiness_check.py", line 591>:
591           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17D88130, file "scripts\pas184_pilot_experience_readiness_check.py", line 591>:
591            RESUME                   0

592            BUILD_LIST               0
               STORE_FAST               1 (out)

593            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

594            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

595            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

596            BUILD_LIST               0
               STORE_FAST               5 (bad)

597            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR               11 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (raw_line)

598            LOAD_FAST_BORROW         6 (raw_line)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

599            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

600            JUMP_BACKWARD           29 (to L2)

601    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

602            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

603    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

604            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

605    L5:     LOAD_CONST               3 ('load_dotenv()')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

606            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

607    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

608            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

609    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

610    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

597    L9:     END_FOR
               POP_ITER

611            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

612            LOAD_CONST               8 ('self_check:no_env_or_db')

613            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              10 ('PASS')

614   L11:     LOAD_CONST              11 ('PAS184 readiness checker never reads .env / touches DB')

615            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L12)
               NOT_TAKEN
               LOAD_CONST              12 ('disqualifying patterns: ')
               LOAD_CONST              13 (', ')
               LOAD_ATTR               21 (join + NULL|self)
               LOAD_FAST_BORROW         5 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST               0 ('')

611   L13:     LOAD_CONST              14 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

617            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas184_pilot_experience_readiness_check.py", line 624>:
624           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17FA92F0, file "scripts\pas184_pilot_experience_readiness_check.py", line 624>:
 624            RESUME                   0

 626            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 625            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 626    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 627            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 626    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 627    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 626    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 625    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 630            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L9)
                NOT_TAKEN
                LOAD_GLOBAL              4 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L10)
        L9:     LOAD_GLOBAL              6 (VERDICT_READY)

 631   L10:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 632            LOAD_CONST               5 ('info')
                BUILD_LIST               0

 629            BUILD_MAP                3
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 625            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L11 [2]
  L4 to L5 -> L11 [2]
  L6 to L8 -> L11 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas184_pilot_experience_readiness_check.py", line 636>:
636           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C18048AB0, file "scripts\pas184_pilot_experience_readiness_check.py", line 636>:
636           RESUME                   0

637           BUILD_LIST               0
              STORE_FAST               1 (out)

638           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

639           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

640           JUMP_BACKWARD           19 (to L1)

641   L2:     LOAD_FAST_BORROW         2 (c)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               2 ('severity')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         7 (to L3)
              NOT_TAKEN
              POP_TOP
              LOAD_GLOBAL              2 (SEVERITY_BLOCK)
      L3:     STORE_FAST               3 (sev)

642           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_CONST               3 ('[')
              LOAD_FAST                3 (sev)
              FORMAT_SIMPLE
              LOAD_CONST               4 ('] ')
              LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               5 ('id')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' — ')
              LOAD_FAST_BORROW         2 (c)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               7 ('detail')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               8 ('see report')
      L4:     FORMAT_SIMPLE
              LOAD_CONST               9 ('.')
              BUILD_STRING             7
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          111 (to L1)

638   L5:     END_FOR
              POP_ITER

643           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "scripts\pas184_pilot_experience_readiness_check.py", line 646>:
646           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17EDA310, file "scripts\pas184_pilot_experience_readiness_check.py", line 646>:
646           RESUME                   0

647           BUILD_LIST               0
              STORE_FAST               1 (checks)

648           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

649           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

650           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

651           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

652           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_no_startup_worker + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

653           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_audit_service_invariant + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

654           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_doc_required_clauses + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

655           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_doc_no_forbidden_scope + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

656           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_webapp_anchors + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

657           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_dashboard_route + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

658           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_main_router_mount + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

659           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_self_no_env_or_db + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

661           LOAD_GLOBAL             27 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

663           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS184')

664           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             29 (_now_iso + NULL)
              CALL                     0

665           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

666           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             30 (VERDICT_READY)
              COMPARE_OP              72 (==)

667           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

668           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

669           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

670           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             35 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053510, file "scripts\pas184_pilot_experience_readiness_check.py", line 670>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

671           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             35 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053CF0, file "scripts\pas184_pilot_experience_readiness_check.py", line 671>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

672           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

673           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             37 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

662           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053510, file "scripts\pas184_pilot_experience_readiness_check.py", line 670>:
 670           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053CF0, file "scripts\pas184_pilot_experience_readiness_check.py", line 671>:
 671           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "scripts\pas184_pilot_experience_readiness_check.py", line 680>:
680           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C180FCB70, file "scripts\pas184_pilot_experience_readiness_check.py", line 680>:
680           RESUME                   0

681           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

682           LOAD_CONST               0 ('pas184_pilot_experience_readiness_check')

684           LOAD_CONST               1 ('PAS184 — Evaluate pilot experience polish (error banner + skeleton + ops playbook + read-only operator dashboard). Read-only — never reads .env, never touches Supabase, never runs a migration.')

681           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

690           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

691           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               5 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

692           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               6 ('--json')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

693           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               9 ('--summary-only')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

694           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              10 ('--strict')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

695           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas184_pilot_experience_readiness_check.py", line 698>:
698           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8E300, file "scripts\pas184_pilot_experience_readiness_check.py", line 698>:
698           RESUME                   0

699           LOAD_GLOBAL              1 (print + NULL)

700           LOAD_CONST               0 ('[PAS184] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

701           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

702           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

703           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

704           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

705           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

700           BUILD_STRING            12

699           CALL                     1
              POP_TOP

707           LOAD_FAST_BORROW         0 (report)
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

708           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

709           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS184] operator actions:')
              CALL                     1
              POP_TOP

710           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

711           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

710   L3:     END_FOR
              POP_ITER

712           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

713           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              16 ('  ... and ')
              LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              BINARY_OP               10 (-)
              FORMAT_SIMPLE
              LOAD_CONST              17 (' more (see report file)')
              BUILD_STRING             3
              CALL                     1
              POP_TOP
              LOAD_CONST              18 (None)
              RETURN_VALUE

712   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

708   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026530, file "scripts\pas184_pilot_experience_readiness_check.py", line 716>:
716           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C180FC210, file "scripts\pas184_pilot_experience_readiness_check.py", line 716>:
 716           RESUME                   0

 717           NOP

 718   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 719           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 720           LOAD_CONST               3 ('utf-8')

 718           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 722           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 723   L4:     LOAD_GLOBAL             11 (print + NULL)

 724           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 725           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 724           BUILD_STRING             4

 726           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 723           LOAD_CONST               7 (('file',))
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

 722   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "scripts\pas184_pilot_experience_readiness_check.py", line 730>:
730           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D88FF0, file "scripts\pas184_pilot_experience_readiness_check.py", line 730>:
 730            RESUME                   0

 731            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 732            NOP

 733    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 737    L2:     LOAD_GLOBAL             10 (os)
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

 738            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 739            LOAD_GLOBAL             23 (print + NULL)
                LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)
                LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 740            LOAD_SMALL_INT           2
                RETURN_VALUE

 742    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 744            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 745            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 747    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 749            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 750            LOAD_GLOBAL             23 (print + NULL)
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

 752    L6:     LOAD_FAST                5 (report)
                LOAD_CONST               6 ('verdict')
                BINARY_OP               26 ([])
                LOAD_GLOBAL             42 (VERDICT_READY)
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN
                LOAD_SMALL_INT           0
                RETURN_VALUE
        L7:     LOAD_SMALL_INT           1
                RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

 734            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 735    L9:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST               7 ((0, None))
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

 734   L17:     RERAISE                  0

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
