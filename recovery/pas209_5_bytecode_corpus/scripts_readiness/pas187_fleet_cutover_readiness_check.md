# scripts_readiness/pas187_fleet_cutover_readiness_check

- **pyc:** `scripts\__pycache__\pas187_fleet_cutover_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas187_fleet_cutover_readiness_check.py`
- **co_filename (from bytecode):** `scripts/pas187_fleet_cutover_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS187 — Fleet observability + two-person cutover discipline
+ daily ops checklist readiness gate.

Deterministic, non-mutating evaluator for "is PAS187 wired
correctly, additive-only, and free of regressions across
the PAS160-PAS186 + PAS-SECURITY-01/02/03/04 doctrine?".

Walks the repo and verifies:

  * PAS187 surfaces exist (docs / scripts / tests / services
    / route / migrations).
  * Two-person-approval semantics visible in the
    cutover_approval service.
  * Self-second-approval explicitly blocked.
  * No scheduler / cron / autonomous remediation in PAS187
    surfaces.
  * No PII exposure: forbidden-token scanner present in
    each service file.
  * No Gmail / google-auth / IMAP / POP3 / Composio /
    TrustClaw / embedding / vector imports.
  * No Memory Review changes (carry-forward).
  * Worker remains OFF by default.
  * All PAS160-PAS186 + security readiness scripts still
    on disk.
  * Operator fleet router mounted in app/main.py.
  * Event-contract carries the eight PAS187 event types.

Read-only: never reads .env, never touches Supabase, never
executes a deploy / migration / network call.

Exit codes:
  0 — READY
  1 — NOT_READY (one or more BLOCK checks failed)
  2 — bad CLI args
```

## Imports

`List`, `Optional`, `Path`, `__future__`, `annotations`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_checklist_invariants`, `check_cutover_two_person_visible`, `check_doc_no_forbidden_scope`, `check_doc_required_clauses`, `check_event_contract_has_pas187_types`, `check_fleet_status_invariants`, `check_main_mounts_fleet_router`, `check_memory_review_intact`, `check_no_automatic_stage_mutation`, `check_no_tenant_mutation_surface`, `check_pas187_files_present`, `check_prior_phases_intact`, `check_self_no_env_or_db`, `check_self_second_approval_blocked`, `check_service_no_forbidden_imports`, `check_service_no_raw_key_reveal`, `check_service_no_scheduler_or_loop`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `NOT_READY`, `PAS187`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS187 — Fleet observability + two-person cutover discipline\n+ daily ops checklist readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS187 wired\ncorrectly, additive-only, and free of regressions across\nthe PAS160-PAS186 + PAS-SECURITY-01/02/03/04 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS187 surfaces exist (docs / scripts / tests / services\n    / route / migrations).\n  * Two-person-approval semantics visible in the\n    cutover_approval service.\n  * Self-second-approval explicitly blocked.\n  * No scheduler / cron / autonomous remediation in PAS187\n    surfaces.\n  * No PII exposure: forbidden-token scanner present in\n    each service file.\n  * No Gmail / google-auth / IMAP / POP3 / Composio /\n    TrustClaw / embedding / vector imports.\n  * No Memory Review changes (carry-forward).\n  * Worker remains OFF by default.\n  * All PAS160-PAS186 + security readiness scripts still\n    on disk.\n  * Operator fleet router mounted in app/main.py.\n  * Event-contract carries the eight PAS187 event types.\n\nRead-only: never reads .env, never touches Supabase, never\nexecutes a deploy / migration / network call.\n\nExit codes:\n  0 — READY\n  1 — NOT_READY (one or more BLOCK checks failed)\n  2 — bad CLI args\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'app/routes/operator_fleet.py'
- 'app/services/events/contract.py'
- 'severity'
- 'detail'
- 'pas187_fleet_cutover_readiness_report.json'
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
- 'Required PAS187 artefact present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS187 must not delete'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS187 must not touch'
- 'app'
- 'services'
- 'ingestion'
- 'worker.py'
- '_ENV_FLAG_ENABLED_LITERAL = "true"'
- "_ENV_FLAG_ENABLED_LITERAL = 'true'"
- 'worker:off_by_default'
- 'Pending-call worker is OFF by default'
- 'missing strict enable-literal constant'
- 'doc:'
- ':clause:'
- ' carries clause: '
- 'missing any of: '
- 'doc_scope:'
- ' introduces no out-of-scope feature token'
- 'disqualifying: '
- 'service_imports:'
- ' contains no forbidden import'
- 'service_scheduler:'
- ' contains no scheduler / cron / autonomous loop'
- 'service_raw_key:'
- ' carries no raw-key reveal token'
- 'app/services/operator/cutover_approval.py'
- 'cutover:token:'
- 'cutover_approval.py carries: '
- 'token missing'
- 'Verify the application layer explicitly rejects\nself-second-approval, and the DB CHECK constraint name\nappears in the v35 migration.'
- 'scripts/migrate_v35_cutover_approvals.sql'
- 'self_second_approval_forbidden'
- 'first_actor'
- 'first_approved_by_actor_id'
- 'self_second_approval:app_layer'
- 'cutover_approval.py rejects self-second-approval at the app layer'
- 'rejection logic not present'
- 'pas_cutover_distinct_approvers_chk'
- 'second_approved_by_actor_id'
- 'self_second_approval:db_layer'
- 'v35 migration carries distinct-approvers CHECK constraint'
- 'CHECK constraint missing'
- "The cutover service must NOT directly mutate the\nbrokerage's pilot_stage. That mutation is reserved for\nPAS173's mark_pilot_stage dispatcher."
- 'cutover:no_automatic_stage_mutation'
- 'cutover_approval.py does NOT auto-mutate brokerage pilot stage'
- 'app/services/operator/daily_ops_checklist.py'
- 'checklist:token:'
- 'daily_ops_checklist.py carries: '
- 'app/services/operator/fleet_status.py'
- 'fleet:token:'
- 'fleet_status.py carries: '
- 'contract:event:'
- 'events/contract.py carries event_type literal: '
- 'literal missing — contract drift'
- 'app/main.py'
- 'main:mount:'
- 'app/main.py contains: '
- 'mount missing — route inaccessible'
- 'Sanity: PAS187 added no tenant-mutation route.\nScan the operator-fleet route for any tenant_ prefix.'
- 'fleet_route:no_tenant_surface'
- ' declares no tenant surface'
- 'dotenv import'
- 'supabase import'
- 'load_dotenv('
- 'load_dotenv() call'
- 'environ read'
- 'get_supabase'
- 'supabase client call'
- 'self_check:no_env_or_db_or_network'
- 'PAS187 readiness checker never reads .env / touches DB / hits network'
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS187'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas187_fleet_cutover_readiness_check'
- 'PAS187 — Fleet observability + two-person cutover discipline + daily ops checklist readiness gate. Read-only — never reads .env, never touches Supabase, never executes a deploy / migration.'
- '--repo-root'
- '--output'
- '--json'
- 'store_true'
- '--summary-only'
- '--strict'
- 'report'
- 'None'
- '[PAS187] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS187] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS187 — Fleet observability + two-person cutover discipline\n+ daily ops checklist readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS187 wired\ncorrectly, additive-only, and free of regressions across\nthe PAS160-PAS186 + PAS-SECURITY-01/02/03/04 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS187 surfaces exist (docs / scripts / tests / services\n    / route / migrations).\n  * Two-person-approval semantics visible in the\n    cutover_approval service.\n  * Self-second-approval explicitly blocked.\n  * No scheduler / cron / autonomous remediation in PAS187\n    surfaces.\n  * No PII exposure: forbidden-token scanner present in\n    each service file.\n  * No Gmail / google-auth / IMAP / POP3 / Composio /\n    TrustClaw / embedding / vector imports.\n  * No Memory Review changes (carry-forward).\n  * Worker remains OFF by default.\n  * All PAS160-PAS186 + security readiness scripts still\n    on disk.\n  * Operator fleet router mounted in app/main.py.\n  * Event-contract carries the eight PAS187 event types.\n\nRead-only: never reads .env, never touches Supabase, never\nexecutes a deploy / migration / network call.\n\nExit codes:\n  0 — READY\n  1 — NOT_READY (one or more BLOCK checks failed)\n  2 — bad CLI args\n')
               STORE_NAME               0 (__doc__)

  38           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  40           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  41           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  42           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  43           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  44           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  45           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  46           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  49           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  50           NOP

  51   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  49   L4:     END_FOR
               POP_ITER

  56           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  57           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  56           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  61           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  62           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  64           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  71           LOAD_CONST              77 (('docs/pas187_fleet_observability_cutover.md', 'scripts/pas187_fleet_cutover_readiness_check.py', 'scripts/migrate_v35_cutover_approvals.sql', 'scripts/migrate_v36_daily_ops_checklist_runs.sql', 'app/services/operator/fleet_status.py', 'app/services/operator/cutover_approval.py', 'app/services/operator/daily_ops_checklist.py', 'app/routes/operator_fleet.py', 'tests/mvp/test_pas187_fleet_cutover.py'))
               STORE_NAME              28 (PAS187_FILES)

  85           LOAD_CONST              78 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py', 'scripts/pas172_pilot_operations_readiness_check.py', 'scripts/pas173_brokerage_operator_readiness_check.py', 'scripts/pas174_operator_audit_readiness_check.py', 'scripts/pas175_audit_integrity_readiness_check.py', 'scripts/pas176_audit_chain_readiness_check.py', 'scripts/pas177_tenant_audit_verification_readiness_check.py', 'scripts/pas178_audit_window_chain_readiness_check.py', 'scripts/pas179_controlled_learning_readiness_check.py', 'scripts/pas180_learning_review_readiness_check.py', 'scripts/pas181_manual_test_harness_readiness_check.py', 'scripts/pas182_adaptive_memory_bridge_readiness_check.py', 'scripts/pas183_onboarding_product_readiness_check.py', 'scripts/pas184_pilot_experience_readiness_check.py', 'scripts/pas186_final_cutover_readiness_check.py', 'scripts/pas_security_01_hardening_readiness_check.py', 'scripts/pas_security_02_rate_limit_scanner_readiness_check.py', 'scripts/pas_security_03_admin_webhook_ci_readiness_check.py', 'scripts/pas_security_04_operator_reveal_https_readiness_check.py'))
               STORE_NAME              29 (PRIOR_PHASE_FILES)

 121           LOAD_CONST              79 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              30 (MEMORY_REVIEW_FILES)

 132           LOAD_CONST              80 ((('docs/pas187_fleet_observability_cutover.md', (('purpose', ('purpose',)), ('relationship-to-pas186', ('relationship to pas186',)), ('fleet-observability-doctrine', ('fleet observability doctrine',)), ('two-person-cutover-doctrine', ('two-person cutover doctrine',)), ('no-self-second-approval', ('no self-second-approval', 'self-second-approval')), ('daily-checklist-discipline', ('daily checklist discipline',)), ('stop-the-rollout-doctrine', ('stop-the-rollout',)), ('escalation-workflow', ('escalation workflow',)), ('rollout-tier-doctrine', ('rollout tier doctrine',)), ('rollback-workflow', ('rollback workflow',)), ('no-autonomous-remediation', ('no autonomous remediation',)), ('no-gmail-oauth', ('no gmail',)), ('no-composio', ('composio',)), ('remaining-limitations', ('remaining limitations',)), ('intentionally-does-not-build', ('intentionally does not build', 'does not build')))),))
               STORE_NAME              31 (DOC_REQUIRED_CLAUSES)

 156           LOAD_CONST              81 (('gmail oauth integration', 'composio integration', 'trustclaw', 'auto-approve memory', 'ai chat assistant enabled', 'embedding model', 'vector database', 'imap inbox scanner', 'pop3 inbox scanner'))
               STORE_NAME              32 (FORBIDDEN_DOC_TOKENS)

 172           LOAD_CONST              82 (('app/services/operator/fleet_status.py', 'app/services/operator/cutover_approval.py', 'app/services/operator/daily_ops_checklist.py', 'app/routes/operator_fleet.py'))
               STORE_NAME              33 (SERVICE_FILES)

 179           LOAD_CONST              83 (('from googleapiclient', 'import googleapiclient', 'from google.oauth2', 'import google.oauth2', 'from google_auth_oauthlib', 'import google_auth_oauthlib', 'from imaplib', 'import imaplib', 'from poplib', 'import poplib', 'from composio', 'import composio', 'from trustclaw', 'import trustclaw', 'from chromadb', 'import chromadb', 'from pinecone', 'import pinecone', 'from pgvector', 'import pgvector', 'from sentence_transformers', 'import sentence_transformers', 'from openai', 'import openai'))
               STORE_NAME              34 (FORBIDDEN_IMPORT_PREFIXES)

 209           LOAD_CONST              84 (('apscheduler.schedulers', 'from celery', 'import celery', 'from croniter', 'import croniter', 'asyncio.create_task(auto_', 'schedule.every(', 'while True:'))
               STORE_NAME              35 (FORBIDDEN_SERVICE_TOKENS)

 222           LOAD_CONST              85 (('"raw_api_key":', "'raw_api_key':", '"plaintext_key":', "'plaintext_key':", '"api_key_plain":', "'api_key_plain':"))
               STORE_NAME              36 (FORBIDDEN_RAW_KEY_TOKENS)

 234           LOAD_CONST              12 ('app/routes/operator_fleet.py')
               STORE_NAME              37 (FLEET_ROUTE_FILE)

 239           LOAD_CONST              86 (('def approve_cutover_first', 'def approve_cutover_second', 'self_second_approval_forbidden', 'first_approved_by_actor_id', 'second_approved_by_actor_id'))
               STORE_NAME              38 (CUTOVER_REQUIRED_TOKENS)

 250           LOAD_CONST              87 (('def build_daily_ops_checklist', 'def complete_daily_ops_checklist', 'def daily_ops_checklist_report', 'def fleet_daily_ops_summary'))
               STORE_NAME              39 (CHECKLIST_REQUIRED_TOKENS)

 259           LOAD_CONST              88 (('def fleet_chain_status_report', 'def fleet_brokerage_health_summary', 'def fleet_rollout_readiness_summary', 'def fleet_exception_report', 'action_required'))
               STORE_NAME              40 (FLEET_STATUS_REQUIRED_TOKENS)

 269           LOAD_CONST              13 ('app/services/events/contract.py')
               STORE_NAME              41 (EVENT_CONTRACT_FILE)

 270           LOAD_CONST              89 (('"fleet.status.generated"', '"fleet.rollout_readiness.generated"', '"cutover.requested"', '"cutover.first_approved"', '"cutover.second_approved"', '"cutover.rejected"', '"daily_ops.checklist.completed"', '"daily_ops.checklist.failed"'))
               STORE_NAME              42 (EVENT_CONTRACT_REQUIRED_EVENT_TYPES)

 283           LOAD_CONST              90 (('operator_fleet_router', 'from app.routes.operator_fleet import'))
               STORE_NAME              43 (MAIN_PY_REQUIRED_MOUNT_TOKENS)

 293           LOAD_CONST              14 ('severity')
               LOAD_NAME               27 (SEVERITY_BLOCK)
               LOAD_CONST              15 ('detail')
               LOAD_CONST              16 ('')
               BUILD_MAP                2
               LOAD_CONST              17 (<code object __annotate__ at 0x0000018C18024E30, file "scripts/pas187_fleet_cutover_readiness_check.py", line 293>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object _check at 0x0000018C17FA23D0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 293>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              44 (_check)

 303           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts/pas187_fleet_cutover_readiness_check.py", line 303>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object _now_iso at 0x0000018C18038CB0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 303>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (_now_iso)

 307           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts/pas187_fleet_cutover_readiness_check.py", line 307>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object _read_text at 0x0000018C18053630, file "scripts/pas187_fleet_cutover_readiness_check.py", line 307>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (_read_text)

 314           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts/pas187_fleet_cutover_readiness_check.py", line 314>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object _strip_python_comments_and_strings at 0x0000018C17EDA550, file "scripts/pas187_fleet_cutover_readiness_check.py", line 314>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (_strip_python_comments_and_strings)

 355           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 355>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object check_pas187_files_present at 0x0000018C180612C0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 355>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_pas187_files_present)

 368           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 368>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts/pas187_fleet_cutover_readiness_check.py", line 368>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_prior_phases_intact)

 381           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA3D20, file "scripts/pas187_fleet_cutover_readiness_check.py", line 381>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object check_memory_review_intact at 0x0000018C180608A0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 381>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_memory_review_intact)

 394           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA1D40, file "scripts/pas187_fleet_cutover_readiness_check.py", line 394>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object check_worker_off_by_default at 0x0000018C1794ED80, file "scripts/pas187_fleet_cutover_readiness_check.py", line 394>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_worker_off_by_default)

 409           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C17FA2880, file "scripts/pas187_fleet_cutover_readiness_check.py", line 409>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object check_doc_required_clauses at 0x0000018C17D8AFF0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 409>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_doc_required_clauses)

 426           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C17FA2B50, file "scripts/pas187_fleet_cutover_readiness_check.py", line 426>)
               MAKE_FUNCTION
               LOAD_CONST              36 (<code object check_doc_no_forbidden_scope at 0x0000018C17ECF940, file "scripts/pas187_fleet_cutover_readiness_check.py", line 426>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_doc_no_forbidden_scope)

 441           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 441>)
               MAKE_FUNCTION
               LOAD_CONST              38 (<code object check_service_no_forbidden_imports at 0x0000018C17F78470, file "scripts/pas187_fleet_cutover_readiness_check.py", line 441>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_service_no_forbidden_imports)

 463           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts/pas187_fleet_cutover_readiness_check.py", line 463>)
               MAKE_FUNCTION
               LOAD_CONST              40 (<code object check_service_no_scheduler_or_loop at 0x0000018C17ECE910, file "scripts/pas187_fleet_cutover_readiness_check.py", line 463>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_service_no_scheduler_or_loop)

 482           LOAD_CONST              41 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts/pas187_fleet_cutover_readiness_check.py", line 482>)
               MAKE_FUNCTION
               LOAD_CONST              42 (<code object check_service_no_raw_key_reveal at 0x0000018C182DCE60, file "scripts/pas187_fleet_cutover_readiness_check.py", line 482>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_service_no_raw_key_reveal)

 500           LOAD_CONST              43 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts/pas187_fleet_cutover_readiness_check.py", line 500>)
               MAKE_FUNCTION
               LOAD_CONST              44 (<code object check_cutover_two_person_visible at 0x0000018C1794E9E0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 500>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_cutover_two_person_visible)

 515           LOAD_CONST              45 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 515>)
               MAKE_FUNCTION
               LOAD_CONST              46 (<code object check_self_second_approval_blocked at 0x0000018C17F797B0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 515>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_self_second_approval_blocked)

 546           LOAD_CONST              47 (<code object __annotate__ at 0x0000018C17FA26A0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 546>)
               MAKE_FUNCTION
               LOAD_CONST              48 (<code object check_no_automatic_stage_mutation at 0x0000018C17ED8FB0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 546>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_no_automatic_stage_mutation)

 573           LOAD_CONST              49 (<code object __annotate__ at 0x0000018C17FA2790, file "scripts/pas187_fleet_cutover_readiness_check.py", line 573>)
               MAKE_FUNCTION
               LOAD_CONST              50 (<code object check_checklist_invariants at 0x0000018C1794EF50, file "scripts/pas187_fleet_cutover_readiness_check.py", line 573>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_checklist_invariants)

 588           LOAD_CONST              51 (<code object __annotate__ at 0x0000018C17FA22E0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 588>)
               MAKE_FUNCTION
               LOAD_CONST              52 (<code object check_fleet_status_invariants at 0x0000018C1794F120, file "scripts/pas187_fleet_cutover_readiness_check.py", line 588>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (check_fleet_status_invariants)

 603           LOAD_CONST              53 (<code object __annotate__ at 0x0000018C17FA24C0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 603>)
               MAKE_FUNCTION
               LOAD_CONST              54 (<code object check_event_contract_has_pas187_types at 0x0000018C1794F2F0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 603>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (check_event_contract_has_pas187_types)

 618           LOAD_CONST              55 (<code object __annotate__ at 0x0000018C17FA25B0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 618>)
               MAKE_FUNCTION
               LOAD_CONST              56 (<code object check_main_mounts_fleet_router at 0x0000018C1794F4C0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 618>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (check_main_mounts_fleet_router)

 633           LOAD_CONST              57 (<code object __annotate__ at 0x0000018C17FA2D30, file "scripts/pas187_fleet_cutover_readiness_check.py", line 633>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object check_no_tenant_mutation_surface at 0x0000018C182DC320, file "scripts/pas187_fleet_cutover_readiness_check.py", line 633>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (check_no_tenant_mutation_surface)

 653           LOAD_CONST              59 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts/pas187_fleet_cutover_readiness_check.py", line 653>)
               MAKE_FUNCTION
               LOAD_CONST              60 (<code object check_self_no_env_or_db at 0x0000018C17EA57B0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 653>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (check_self_no_env_or_db)

 701           LOAD_CONST              61 (<code object __annotate__ at 0x0000018C17FA2C40, file "scripts/pas187_fleet_cutover_readiness_check.py", line 701>)
               MAKE_FUNCTION
               LOAD_CONST              62 (<code object _aggregate at 0x0000018C17FA92F0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 701>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (_aggregate)

 710           LOAD_CONST              63 (<code object __annotate__ at 0x0000018C181152F0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 710>)
               MAKE_FUNCTION
               LOAD_CONST              64 (<code object _operator_actions at 0x0000018C18048C70, file "scripts/pas187_fleet_cutover_readiness_check.py", line 710>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (_operator_actions)

 720           LOAD_CONST              65 (<code object __annotate__ at 0x0000018C181153E0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 720>)
               MAKE_FUNCTION
               LOAD_CONST              66 (<code object evaluate at 0x0000018C17E951B0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 720>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              68 (evaluate)

 757           LOAD_CONST              67 ('pas187_fleet_cutover_readiness_report.json')
               STORE_NAME              69 (REPORT_FILENAME)

 760           LOAD_CONST              68 (<code object __annotate__ at 0x0000018C181154D0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 760>)
               MAKE_FUNCTION
               LOAD_CONST              69 (<code object _build_parser at 0x0000018C179C3C30, file "scripts/pas187_fleet_cutover_readiness_check.py", line 760>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              70 (_build_parser)

 778           LOAD_CONST              70 (<code object __annotate__ at 0x0000018C181155C0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 778>)
               MAKE_FUNCTION
               LOAD_CONST              71 (<code object _print_summary at 0x0000018C17D8E300, file "scripts/pas187_fleet_cutover_readiness_check.py", line 778>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              71 (_print_summary)

 796           LOAD_CONST              72 (<code object __annotate__ at 0x0000018C18026430, file "scripts/pas187_fleet_cutover_readiness_check.py", line 796>)
               MAKE_FUNCTION
               LOAD_CONST              73 (<code object _write_report at 0x0000018C179C3E10, file "scripts/pas187_fleet_cutover_readiness_check.py", line 796>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              72 (_write_report)

 810           LOAD_CONST              91 ((None,))
               LOAD_CONST              74 (<code object __annotate__ at 0x0000018C18115980, file "scripts/pas187_fleet_cutover_readiness_check.py", line 810>)
               MAKE_FUNCTION
               LOAD_CONST              75 (<code object main at 0x0000018C17D884E0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 810>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              73 (main)

 835           LOAD_NAME               74 (__name__)
               LOAD_CONST              76 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 836           LOAD_NAME                6 (sys)
               LOAD_ATTR              150 (exit)
               PUSH_NULL
               LOAD_NAME               73 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 835   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  52           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  53   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          371 (to L1)

  52   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "scripts/pas187_fleet_cutover_readiness_check.py", line 293>:
293           RESUME                   0
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
              LOAD_CONST               5 ('severity')
              LOAD_CONST               2 ('str')
              LOAD_CONST               6 ('detail')
              LOAD_CONST               2 ('str')
              LOAD_CONST               7 ('return')
              LOAD_CONST               8 ('dict')
              BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA23D0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 293>:
293           RESUME                   0

295           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

296           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

297           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

298           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

299           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

294           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts/pas187_fleet_cutover_readiness_check.py", line 303>:
303           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038CB0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 303>:
303           RESUME                   0

304           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts/pas187_fleet_cutover_readiness_check.py", line 307>:
307           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053630, file "scripts/pas187_fleet_cutover_readiness_check.py", line 307>:
 307           RESUME                   0

 308           NOP

 309   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 310           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 311   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 310   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts/pas187_fleet_cutover_readiness_check.py", line 314>:
314           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17EDA550, file "scripts/pas187_fleet_cutover_readiness_check.py", line 314>:
314            RESUME                   0

317            BUILD_LIST               0
               STORE_FAST               1 (out)

318            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

319    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

320            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

321            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

322            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

323            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

324            JUMP_FORWARD           240 (to L13)

325    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

326            JUMP_BACKWARD           59 (to L1)

327    L3:     LOAD_FAST_BORROW         0 (src)
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

328    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

329            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

330            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

331            JUMP_FORWARD           138 (to L13)

332    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

333            JUMP_BACKWARD          161 (to L1)

334    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

335            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

336            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

337    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

338            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

339            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

340            JUMP_BACKWARD           30 (to L7)

341    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

342    L9:     JUMP_FORWARD            11 (to L11)

343   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

344   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

345            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

346   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

347            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

348   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 355>:
355           RESUME                   0
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

Disassembly of <code object check_pas187_files_present at 0x0000018C180612C0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 355>:
355           RESUME                   0

356           BUILD_LIST               0
              STORE_FAST               1 (out)

357           LOAD_GLOBAL              0 (PAS187_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

358           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

359           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

360           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

361           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

362   L3:     LOAD_CONST               3 ('Required PAS187 artefact present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

363           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

359   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

357   L6:     END_FOR
              POP_ITER

365           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 368>:
368           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts/pas187_fleet_cutover_readiness_check.py", line 368>:
368           RESUME                   0

369           BUILD_LIST               0
              STORE_FAST               1 (out)

370           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

371           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

372           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

373           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

374           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

375   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

376           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS187 must not delete')

372   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

370   L6:     END_FOR
              POP_ITER

378           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "scripts/pas187_fleet_cutover_readiness_check.py", line 381>:
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

Disassembly of <code object check_memory_review_intact at 0x0000018C180608A0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 381>:
381           RESUME                   0

382           BUILD_LIST               0
              STORE_FAST               1 (out)

383           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

384           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

385           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

386           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

387           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

388   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

389           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS187 must not touch')

385   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

383   L6:     END_FOR
              POP_ITER

391           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "scripts/pas187_fleet_cutover_readiness_check.py", line 394>:
394           RESUME                   0
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C1794ED80, file "scripts/pas187_fleet_cutover_readiness_check.py", line 394>:
394           RESUME                   0

395           LOAD_GLOBAL              1 (Path + NULL)
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
              STORE_FAST               1 (p)

396           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         1 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               2 (src)

398           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         2 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

399           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         2 (src)
              CONTAINS_OP              0 (in)

397   L2:     STORE_FAST               3 (ok)

401           LOAD_GLOBAL              5 (_check + NULL)

402           LOAD_CONST               7 ('worker:off_by_default')

403           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

404   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default')

405           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        9 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')

401           LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              BUILD_LIST               1
              RETURN_VALUE

405   L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

401           LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              BUILD_LIST               1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "scripts/pas187_fleet_cutover_readiness_check.py", line 409>:
409           RESUME                   0
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

Disassembly of <code object check_doc_required_clauses at 0x0000018C17D8AFF0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 409>:
  --            MAKE_CELL                9 (lower)

 409            RESUME                   0

 410            BUILD_LIST               0
                STORE_FAST               1 (out)

 411            LOAD_GLOBAL              0 (DOC_REQUIRED_CLAUSES)
                GET_ITER
        L1:     FOR_ITER               208 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   35 (relpath, clauses)

 412            LOAD_GLOBAL              3 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_FAST_BORROW         2 (relpath)
                BINARY_OP               11 (/)
                STORE_FAST               4 (fp)

 413            LOAD_GLOBAL              5 (_read_text + NULL)
                LOAD_FAST_BORROW         4 (fp)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 ('')
        L2:     STORE_FAST               5 (src)

 414            LOAD_FAST_BORROW         5 (src)
                LOAD_ATTR                7 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              9 (lower)

 415            LOAD_FAST_BORROW         3 (clauses)
                GET_ITER
        L3:     FOR_ITER               142 (to L13)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  103 (name, phrases)

 416            LOAD_GLOBAL              8 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L7)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         9 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18025730, file "scripts/pas187_fleet_cutover_readiness_check.py", line 416>)
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
                LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18025730, file "scripts/pas187_fleet_cutover_readiness_check.py", line 416>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         7 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L8:     STORE_FAST               8 (present)

 417            LOAD_FAST                1 (out)
                LOAD_ATTR               11 (append + NULL|self)
                LOAD_GLOBAL             13 (_check + NULL)

 418            LOAD_CONST               4 ('doc:')
                LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                LOAD_CONST               5 (':clause:')
                LOAD_FAST_BORROW         6 (name)
                FORMAT_SIMPLE
                BUILD_STRING             4

 419            LOAD_FAST_BORROW         8 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST               6 ('PASS')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               7 ('FAIL')

 420   L10:     LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                LOAD_CONST               8 (' carries clause: ')
                LOAD_FAST_BORROW         6 (name)
                FORMAT_SIMPLE
                BUILD_STRING             3

 421            LOAD_FAST_BORROW         8 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN
                LOAD_CONST               0 ('')
                JUMP_FORWARD            19 (to L12)
       L11:     LOAD_CONST               9 ('missing any of: ')
                LOAD_CONST              10 (', ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         7 (phrases)
                CALL                     1
                FORMAT_SIMPLE
                BUILD_STRING             2

 417   L12:     LOAD_CONST              11 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          144 (to L3)

 415   L13:     END_FOR
                POP_ITER
                JUMP_BACKWARD          210 (to L1)

 411   L14:     END_FOR
                POP_ITER

 423            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025730, file "scripts/pas187_fleet_cutover_readiness_check.py", line 416>:
  --           COPY_FREE_VARS           1

 416           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "scripts/pas187_fleet_cutover_readiness_check.py", line 426>:
426           RESUME                   0
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

Disassembly of <code object check_doc_no_forbidden_scope at 0x0000018C17ECF940, file "scripts/pas187_fleet_cutover_readiness_check.py", line 426>:
 426            RESUME                   0

 427            BUILD_LIST               0
                STORE_FAST               1 (out)

 428            LOAD_GLOBAL              0 (DOC_REQUIRED_CLAUSES)
                GET_ITER
        L1:     FOR_ITER               165 (to L13)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   35 (relpath, _)

 429            LOAD_GLOBAL              3 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_FAST_BORROW         2 (relpath)
                BINARY_OP               11 (/)
                STORE_FAST               4 (fp)

 430            LOAD_GLOBAL              5 (_read_text + NULL)
                LOAD_FAST_BORROW         4 (fp)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 ('')
        L2:     LOAD_ATTR                7 (lower + NULL|self)
                CALL                     0
                STORE_FAST               5 (src)

 431            LOAD_GLOBAL              8 (FORBIDDEN_DOC_TOKENS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      6 (t)
                SWAP                     2
        L3:     BUILD_LIST               0
                SWAP                     2
        L4:     FOR_ITER                13 (to L7)
                STORE_FAST_LOAD_FAST   102 (t, t)
                LOAD_FAST_BORROW         5 (src)
                CONTAINS_OP              0 (in)
        L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L4)
        L6:     LOAD_FAST_BORROW         6 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L4)
        L7:     END_FOR
                POP_ITER
        L8:     STORE_FAST               7 (bad)
                STORE_FAST               6 (t)

 432            LOAD_FAST                1 (out)
                LOAD_ATTR               11 (append + NULL|self)
                LOAD_GLOBAL             13 (_check + NULL)

 433            LOAD_CONST               1 ('doc_scope:')
                LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                BUILD_STRING             2

 434            LOAD_FAST_BORROW         7 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST               2 ('FAIL')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               3 ('PASS')

 435   L10:     LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                LOAD_CONST               4 (' introduces no out-of-scope feature token')
                BUILD_STRING             2

 436            LOAD_FAST_BORROW         7 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L11)
                NOT_TAKEN
                LOAD_CONST               5 ('disqualifying: ')
                LOAD_CONST               6 (', ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         7 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L12)
       L11:     LOAD_CONST               0 ('')

 432   L12:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          167 (to L1)

 428   L13:     END_FOR
                POP_ITER

 438            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L14:     SWAP                     2
                POP_TOP

 431            SWAP                     2
                STORE_FAST               6 (t)
                RERAISE                  0
ExceptionTable:
  L3 to L5 -> L14 [3]
  L6 to L8 -> L14 [3]

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 441>:
441           RESUME                   0
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

Disassembly of <code object check_service_no_forbidden_imports at 0x0000018C17F78470, file "scripts/pas187_fleet_cutover_readiness_check.py", line 441>:
441            RESUME                   0

442            BUILD_LIST               0
               STORE_FAST               1 (out)

443            LOAD_GLOBAL              0 (SERVICE_FILES)
               GET_ITER
       L1:     FOR_ITER               228 (to L12)
               STORE_FAST               2 (relpath)

444            LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         2 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               3 (fp)

445            LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         3 (fp)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L2:     STORE_FAST               4 (src)

446            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         4 (src)
               CALL                     1
               STORE_FAST               5 (executable)

447            BUILD_LIST               0
               STORE_FAST               6 (bad)

448            LOAD_FAST_BORROW         5 (executable)
               LOAD_ATTR                9 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L3:     FOR_ITER                75 (to L7)
               STORE_FAST               7 (line)

449            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

450            LOAD_GLOBAL             12 (FORBIDDEN_IMPORT_PREFIXES)
               GET_ITER
       L4:     FOR_ITER                46 (to L6)
               STORE_FAST               9 (pref)

451            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (pref)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L4)

452    L5:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_FAST_BORROW         9 (pref)
               CALL                     1
               POP_TOP

453            POP_TOP
               JUMP_BACKWARD           73 (to L3)

450    L6:     END_FOR
               POP_ITER
               JUMP_BACKWARD           77 (to L3)

448    L7:     END_FOR
               POP_ITER

454            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

455            LOAD_CONST               1 ('service_imports:')
               LOAD_FAST_BORROW         2 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

456            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               2 ('FAIL')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               3 ('PASS')

457    L9:     LOAD_FAST_BORROW         2 (relpath)
               FORMAT_SIMPLE
               LOAD_CONST               4 (' contains no forbidden import')
               BUILD_STRING             2

458            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L10)
               NOT_TAKEN
               LOAD_CONST               5 ('disqualifying: ')
               LOAD_CONST               6 (', ')
               LOAD_ATTR               21 (join + NULL|self)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST               0 ('')

454   L11:     LOAD_CONST               7 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          230 (to L1)

443   L12:     END_FOR
               POP_ITER

460            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts/pas187_fleet_cutover_readiness_check.py", line 463>:
463           RESUME                   0
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

Disassembly of <code object check_service_no_scheduler_or_loop at 0x0000018C17ECE910, file "scripts/pas187_fleet_cutover_readiness_check.py", line 463>:
463            RESUME                   0

464            BUILD_LIST               0
               STORE_FAST               1 (out)

465            LOAD_GLOBAL              0 (SERVICE_FILES)
               GET_ITER
       L1:     FOR_ITER               171 (to L10)
               STORE_FAST               2 (relpath)

466            LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         2 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               3 (fp)

467            LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         3 (fp)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L2:     STORE_FAST               4 (src)

468            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         4 (src)
               CALL                     1
               STORE_FAST               5 (executable)

469            BUILD_LIST               0
               STORE_FAST               6 (bad)

470            LOAD_GLOBAL              8 (FORBIDDEN_SERVICE_TOKENS)
               GET_ITER
       L3:     FOR_ITER                28 (to L5)
               STORE_FAST               7 (tok)

471            LOAD_FAST_BORROW_LOAD_FAST_BORROW 117 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)

472    L4:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         7 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L3)

470    L5:     END_FOR
               POP_ITER

473            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

474            LOAD_CONST               1 ('service_scheduler:')
               LOAD_FAST_BORROW         2 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

475            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               2 ('FAIL')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               3 ('PASS')

476    L7:     LOAD_FAST_BORROW         2 (relpath)
               FORMAT_SIMPLE
               LOAD_CONST               4 (' contains no scheduler / cron / autonomous loop')
               BUILD_STRING             2

477            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L8)
               NOT_TAKEN
               LOAD_CONST               5 ('disqualifying: ')
               LOAD_CONST               6 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               0 ('')

473    L9:     LOAD_CONST               7 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          173 (to L1)

465   L10:     END_FOR
               POP_ITER

479            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts/pas187_fleet_cutover_readiness_check.py", line 482>:
482           RESUME                   0
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

Disassembly of <code object check_service_no_raw_key_reveal at 0x0000018C182DCE60, file "scripts/pas187_fleet_cutover_readiness_check.py", line 482>:
482            RESUME                   0

483            BUILD_LIST               0
               STORE_FAST               1 (out)

484            LOAD_GLOBAL              0 (SERVICE_FILES)
               GET_ITER
       L1:     FOR_ITER               160 (to L10)
               STORE_FAST               2 (relpath)

485            LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         2 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               3 (fp)

486            LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         3 (fp)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L2:     STORE_FAST               4 (src)

487            BUILD_LIST               0
               STORE_FAST               5 (bad)

488            LOAD_GLOBAL              6 (FORBIDDEN_RAW_KEY_TOKENS)
               GET_ITER
       L3:     FOR_ITER                28 (to L5)
               STORE_FAST               6 (tok)

489            LOAD_FAST_BORROW_LOAD_FAST_BORROW 100 (tok, src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)

490    L4:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_FAST_BORROW         6 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L3)

488    L5:     END_FOR
               POP_ITER

491            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

492            LOAD_CONST               1 ('service_raw_key:')
               LOAD_FAST_BORROW         2 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

493            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               2 ('FAIL')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               3 ('PASS')

494    L7:     LOAD_FAST_BORROW         2 (relpath)
               FORMAT_SIMPLE
               LOAD_CONST               4 (' carries no raw-key reveal token')
               BUILD_STRING             2

495            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L8)
               NOT_TAKEN
               LOAD_CONST               5 ('disqualifying: ')
               LOAD_CONST               6 (', ')
               LOAD_ATTR               13 (join + NULL|self)
               LOAD_FAST_BORROW         5 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               0 ('')

491    L9:     LOAD_CONST               7 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          162 (to L1)

484   L10:     END_FOR
               POP_ITER

497            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts/pas187_fleet_cutover_readiness_check.py", line 500>:
500           RESUME                   0
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

Disassembly of <code object check_cutover_two_person_visible at 0x0000018C1794E9E0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 500>:
500           RESUME                   0

501           BUILD_LIST               0
              STORE_FAST               1 (out)

502           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app/services/operator/cutover_approval.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (fp)

503           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (fp)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     STORE_FAST               3 (src)

504           LOAD_GLOBAL              4 (CUTOVER_REQUIRED_TOKENS)
              GET_ITER
      L2:     FOR_ITER                70 (to L7)
              STORE_FAST               4 (tok)

505           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

506           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

507           LOAD_CONST               2 ('cutover:token:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               3 (slice(None, 60, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

508           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               4 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               5 ('FAIL')

509   L4:     LOAD_CONST               6 ('cutover_approval.py carries: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

510           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               1 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               7 ('token missing')

506   L6:     LOAD_CONST               8 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           72 (to L2)

504   L7:     END_FOR
              POP_ITER

512           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 515>:
515           RESUME                   0
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

Disassembly of <code object check_self_second_approval_blocked at 0x0000018C17F797B0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 515>:
515            RESUME                   0

519            BUILD_LIST               0
               STORE_FAST               1 (out)

520            LOAD_GLOBAL              1 (_read_text + NULL)
               LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               1 ('app/services/operator/cutover_approval.py')
               BINARY_OP               11 (/)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               2 (svc)

521            LOAD_GLOBAL              1 (_read_text + NULL)
               LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               3 ('scripts/migrate_v35_cutover_approvals.sql')
               BINARY_OP               11 (/)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L2:     STORE_FAST               3 (sql)

523            LOAD_CONST               4 ('self_second_approval_forbidden')
               LOAD_FAST_BORROW         2 (svc)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       19 (to L3)
               NOT_TAKEN
               POP_TOP

524            LOAD_CONST               5 ('first_actor')
               LOAD_FAST_BORROW         2 (svc)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               6 ('first_approved_by_actor_id')
               LOAD_FAST_BORROW         2 (svc)
               CONTAINS_OP              0 (in)

523    L3:     STORE_FAST               4 (svc_check)

526            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

527            LOAD_CONST               7 ('self_second_approval:app_layer')

528            LOAD_FAST_BORROW         4 (svc_check)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN
               LOAD_CONST               8 ('PASS')
               JUMP_FORWARD             1 (to L5)
       L4:     LOAD_CONST               9 ('FAIL')

529    L5:     LOAD_CONST              10 ('cutover_approval.py rejects self-second-approval at the app layer')

530            LOAD_FAST_BORROW         4 (svc_check)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST              11 ('rejection logic not present')

526    L7:     LOAD_CONST              12 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

533            LOAD_CONST              13 ('pas_cutover_distinct_approvers_chk')
               LOAD_FAST_BORROW         3 (sql)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       19 (to L8)
               NOT_TAKEN
               POP_TOP

534            LOAD_CONST               6 ('first_approved_by_actor_id')
               LOAD_FAST_BORROW         3 (sql)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

535            LOAD_CONST              14 ('second_approved_by_actor_id')
               LOAD_FAST_BORROW         3 (sql)
               CONTAINS_OP              0 (in)

533    L8:     STORE_FAST               5 (sql_check)

537            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

538            LOAD_CONST              15 ('self_second_approval:db_layer')

539            LOAD_FAST_BORROW         5 (sql_check)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               8 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               9 ('FAIL')

540   L10:     LOAD_CONST              16 ('v35 migration carries distinct-approvers CHECK constraint')

541            LOAD_FAST_BORROW         5 (sql_check)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              17 ('CHECK constraint missing')

537   L12:     LOAD_CONST              12 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

543            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 546>:
546           RESUME                   0
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

Disassembly of <code object check_no_automatic_stage_mutation at 0x0000018C17ED8FB0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 546>:
546           RESUME                   0

550           BUILD_LIST               0
              STORE_FAST               1 (out)

551           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               1 ('app/services/operator/cutover_approval.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (fp)

552           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (fp)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

553           LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (executable)

554           BUILD_LIST               0
              STORE_FAST               5 (bad)

555           LOAD_CONST              10 (('set_brokerage_stage(', 'update_brokerage_stage(', 'mark_pilot_stage(', 'promote_brokerage('))
              STORE_FAST               6 (forbidden)

561           LOAD_FAST_BORROW         6 (forbidden)
              GET_ITER
      L2:     FOR_ITER                28 (to L4)
              STORE_FAST               7 (tok)

562           LOAD_FAST_BORROW_LOAD_FAST_BORROW 116 (tok, executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

563   L3:     LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_FAST_BORROW         7 (tok)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           30 (to L2)

561   L4:     END_FOR
              POP_ITER

564           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

565           LOAD_CONST               3 ('cutover:no_automatic_stage_mutation')

566           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('FAIL')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               5 ('PASS')

567   L6:     LOAD_CONST               6 ('cutover_approval.py does NOT auto-mutate brokerage pilot stage')

568           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L7)
              NOT_TAKEN
              LOAD_CONST               7 ('disqualifying: ')
              LOAD_CONST               8 (', ')
              LOAD_ATTR               11 (join + NULL|self)
              LOAD_FAST_BORROW         5 (bad)
              CALL                     1
              BINARY_OP                0 (+)
              JUMP_FORWARD             1 (to L8)
      L7:     LOAD_CONST               2 ('')

564   L8:     LOAD_CONST               9 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

570           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2790, file "scripts/pas187_fleet_cutover_readiness_check.py", line 573>:
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

Disassembly of <code object check_checklist_invariants at 0x0000018C1794EF50, file "scripts/pas187_fleet_cutover_readiness_check.py", line 573>:
573           RESUME                   0

574           BUILD_LIST               0
              STORE_FAST               1 (out)

575           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app/services/operator/daily_ops_checklist.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (fp)

576           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (fp)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     STORE_FAST               3 (src)

577           LOAD_GLOBAL              4 (CHECKLIST_REQUIRED_TOKENS)
              GET_ITER
      L2:     FOR_ITER                70 (to L7)
              STORE_FAST               4 (tok)

578           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

579           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

580           LOAD_CONST               2 ('checklist:token:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               3 (slice(None, 60, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

581           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               4 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               5 ('FAIL')

582   L4:     LOAD_CONST               6 ('daily_ops_checklist.py carries: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

583           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               1 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               7 ('token missing')

579   L6:     LOAD_CONST               8 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           72 (to L2)

577   L7:     END_FOR
              POP_ITER

585           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 588>:
588           RESUME                   0
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

Disassembly of <code object check_fleet_status_invariants at 0x0000018C1794F120, file "scripts/pas187_fleet_cutover_readiness_check.py", line 588>:
588           RESUME                   0

589           BUILD_LIST               0
              STORE_FAST               1 (out)

590           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app/services/operator/fleet_status.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (fp)

591           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (fp)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     STORE_FAST               3 (src)

592           LOAD_GLOBAL              4 (FLEET_STATUS_REQUIRED_TOKENS)
              GET_ITER
      L2:     FOR_ITER                70 (to L7)
              STORE_FAST               4 (tok)

593           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

594           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

595           LOAD_CONST               2 ('fleet:token:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               3 (slice(None, 60, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

596           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               4 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               5 ('FAIL')

597   L4:     LOAD_CONST               6 ('fleet_status.py carries: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

598           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               1 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               7 ('token missing')

594   L6:     LOAD_CONST               8 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           72 (to L2)

592   L7:     END_FOR
              POP_ITER

600           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 603>:
603           RESUME                   0
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

Disassembly of <code object check_event_contract_has_pas187_types at 0x0000018C1794F2F0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 603>:
603           RESUME                   0

604           BUILD_LIST               0
              STORE_FAST               1 (out)

605           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_GLOBAL              2 (EVENT_CONTRACT_FILE)
              BINARY_OP               11 (/)
              STORE_FAST               2 (fp)

606           LOAD_GLOBAL              5 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (fp)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               0 ('')
      L1:     STORE_FAST               3 (src)

607           LOAD_GLOBAL              6 (EVENT_CONTRACT_REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                63 (to L7)
              STORE_FAST               4 (tok)

608           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

609           LOAD_FAST                1 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_GLOBAL             11 (_check + NULL)

610           LOAD_CONST               1 ('contract:event:')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

611           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               2 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               3 ('FAIL')

612   L4:     LOAD_CONST               4 ('events/contract.py carries event_type literal: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

613           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               0 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               5 ('literal missing — contract drift')

609   L6:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           65 (to L2)

607   L7:     END_FOR
              POP_ITER

615           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 618>:
618           RESUME                   0
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

Disassembly of <code object check_main_mounts_fleet_router at 0x0000018C1794F4C0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 618>:
618           RESUME                   0

619           BUILD_LIST               0
              STORE_FAST               1 (out)

620           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app/main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (fp)

621           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (fp)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     STORE_FAST               3 (src)

622           LOAD_GLOBAL              4 (MAIN_PY_REQUIRED_MOUNT_TOKENS)
              GET_ITER
      L2:     FOR_ITER                70 (to L7)
              STORE_FAST               4 (tok)

623           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

624           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

625           LOAD_CONST               2 ('main:mount:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               3 (slice(None, 60, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

626           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               4 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               5 ('FAIL')

627   L4:     LOAD_CONST               6 ('app/main.py contains: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

628           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               1 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               7 ('mount missing — route inaccessible')

624   L6:     LOAD_CONST               8 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           72 (to L2)

622   L7:     END_FOR
              POP_ITER

630           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "scripts/pas187_fleet_cutover_readiness_check.py", line 633>:
633           RESUME                   0
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

Disassembly of <code object check_no_tenant_mutation_surface at 0x0000018C182DC320, file "scripts/pas187_fleet_cutover_readiness_check.py", line 633>:
633           RESUME                   0

636           BUILD_LIST               0
              STORE_FAST               1 (out)

637           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_GLOBAL              2 (FLEET_ROUTE_FILE)
              BINARY_OP               11 (/)
              STORE_FAST               2 (fp)

638           LOAD_GLOBAL              5 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (fp)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     STORE_FAST               3 (src)

639           LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (executable)

640           BUILD_LIST               0
              STORE_FAST               5 (bad)

641           LOAD_CONST               9 (('/tenant/', 'tenant_router', 'X-API-Key'))
              GET_ITER
      L2:     FOR_ITER                28 (to L4)
              STORE_FAST               6 (tok)

642           LOAD_FAST_BORROW_LOAD_FAST_BORROW 100 (tok, executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

643   L3:     LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_FAST_BORROW         6 (tok)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           30 (to L2)

641   L4:     END_FOR
              POP_ITER

644           LOAD_FAST                1 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_GLOBAL             11 (_check + NULL)

645           LOAD_CONST               2 ('fleet_route:no_tenant_surface')

646           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               3 ('FAIL')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               4 ('PASS')

647   L6:     LOAD_GLOBAL              2 (FLEET_ROUTE_FILE)
              FORMAT_SIMPLE
              LOAD_CONST               5 (' declares no tenant surface')
              BUILD_STRING             2

648           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L7)
              NOT_TAKEN
              LOAD_CONST               6 ('disqualifying: ')
              LOAD_CONST               7 (', ')
              LOAD_ATTR               13 (join + NULL|self)
              LOAD_FAST_BORROW         5 (bad)
              CALL                     1
              BINARY_OP                0 (+)
              JUMP_FORWARD             1 (to L8)
      L7:     LOAD_CONST               1 ('')

644   L8:     LOAD_CONST               8 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

650           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts/pas187_fleet_cutover_readiness_check.py", line 653>:
653           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17EA57B0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 653>:
653            RESUME                   0

656            BUILD_LIST               0
               STORE_FAST               1 (out)

657            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               STORE_FAST               2 (fp)

658            LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (fp)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

659            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

660            BUILD_LIST               0
               STORE_FAST               5 (bad)

661            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR                9 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (line)

662            LOAD_FAST_BORROW         6 (line)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

663            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

664            JUMP_BACKWARD           29 (to L2)

665    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

666            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

667    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

668            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

669    L5:     LOAD_CONST               3 ('load_dotenv(')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

670            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

671    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

672            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

673    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

674    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

661    L9:     END_FOR
               POP_ITER

675            LOAD_CONST              18 (('subprocess.run(', 'subprocess.call(', 'requests.get(', 'requests.post(', 'httpx.get(', 'httpx.post(', 'urllib.request.urlopen(', 'git push', 'railway deploy'))
               GET_ITER
      L10:     FOR_ITER                28 (to L12)
               STORE_FAST               8 (tok)

686            LOAD_FAST_BORROW_LOAD_FAST_BORROW 132 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L11)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L10)

687   L11:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         8 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L10)

675   L12:     END_FOR
               POP_ITER

688            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

689            LOAD_CONST               8 ('self_check:no_env_or_db_or_network')

690            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST              10 ('PASS')

691   L14:     LOAD_CONST              11 ('PAS187 readiness checker never reads .env / touches DB / hits network')

692            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L15)
               NOT_TAKEN
               LOAD_CONST              12 ('disqualifying: ')
               LOAD_CONST              13 (', ')
               LOAD_ATTR               19 (join + NULL|self)
               LOAD_FAST_BORROW         5 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L16)
      L15:     LOAD_CONST               0 ('')

688   L16:     LOAD_CONST              14 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

694            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "scripts/pas187_fleet_cutover_readiness_check.py", line 701>:
701           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17FA92F0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 701>:
 701            RESUME                   0

 702            LOAD_FAST_BORROW         0 (checks)
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2
        L2:     FOR_ITER                48 (to L7)
                STORE_FAST_LOAD_FAST    17 (c, c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))
        L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           18 (to L2)
        L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))
        L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           46 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           50 (to L2)
        L7:     END_FOR
                POP_ITER
        L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 704            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L9)
                NOT_TAKEN
                LOAD_GLOBAL              4 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L10)
        L9:     LOAD_GLOBAL              6 (VERDICT_READY)

 705   L10:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 706            LOAD_CONST               5 ('info')
                BUILD_LIST               0

 703            BUILD_MAP                3
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 702            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L11 [2]
  L4 to L5 -> L11 [2]
  L6 to L8 -> L11 [2]

Disassembly of <code object __annotate__ at 0x0000018C181152F0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 710>:
710           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C18048C70, file "scripts/pas187_fleet_cutover_readiness_check.py", line 710>:
710           RESUME                   0

711           BUILD_LIST               0
              STORE_FAST               1 (out)

712           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

713           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

714           JUMP_BACKWARD           19 (to L1)

715   L2:     LOAD_FAST_BORROW         2 (c)
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

716           LOAD_FAST                1 (out)
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

712   L5:     END_FOR
              POP_ITER

717           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181153E0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 720>:
720           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17E951B0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 720>:
720           RESUME                   0

721           BUILD_LIST               0
              STORE_FAST               1 (checks)

722           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_pas187_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

723           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

724           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

725           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

726           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_doc_required_clauses + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

727           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_doc_no_forbidden_scope + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

728           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_service_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

729           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_service_no_scheduler_or_loop + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

730           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_service_no_raw_key_reveal + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

731           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_cutover_two_person_visible + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

732           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_self_second_approval_blocked + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

733           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_no_automatic_stage_mutation + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

734           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             27 (check_checklist_invariants + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

735           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             29 (check_fleet_status_invariants + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

736           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             31 (check_event_contract_has_pas187_types + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

737           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             33 (check_main_mounts_fleet_router + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

738           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             35 (check_no_tenant_mutation_surface + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

739           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             37 (check_self_no_env_or_db + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

741           LOAD_GLOBAL             39 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

743           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS187')

744           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             41 (_now_iso + NULL)
              CALL                     0

745           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

746           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             42 (VERDICT_READY)
              COMPARE_OP              72 (==)

747           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             45 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

748           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             45 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

749           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             45 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

750           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             47 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18128270, file "scripts/pas187_fleet_cutover_readiness_check.py", line 750>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

751           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             47 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18128390, file "scripts/pas187_fleet_cutover_readiness_check.py", line 751>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

752           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

753           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             49 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

742           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18128270, file "scripts/pas187_fleet_cutover_readiness_check.py", line 750>:
 750           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18128390, file "scripts/pas187_fleet_cutover_readiness_check.py", line 751>:
 751           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C181154D0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 760>:
760           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C179C3C30, file "scripts/pas187_fleet_cutover_readiness_check.py", line 760>:
760           RESUME                   0

761           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

762           LOAD_CONST               0 ('pas187_fleet_cutover_readiness_check')

764           LOAD_CONST               1 ('PAS187 — Fleet observability + two-person cutover discipline + daily ops checklist readiness gate. Read-only — never reads .env, never touches Supabase, never executes a deploy / migration.')

761           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

770           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

771           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               5 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

772           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               6 ('--json')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

773           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               9 ('--summary-only')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

774           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              10 ('--strict')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

775           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181155C0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 778>:
778           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8E300, file "scripts/pas187_fleet_cutover_readiness_check.py", line 778>:
778           RESUME                   0

779           LOAD_GLOBAL              1 (print + NULL)

780           LOAD_CONST               0 ('[PAS187] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

781           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

782           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

783           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

784           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

785           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

780           BUILD_STRING            12

779           CALL                     1
              POP_TOP

787           LOAD_FAST_BORROW         0 (report)
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

788           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

789           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS187] operator actions:')
              CALL                     1
              POP_TOP

790           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

791           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

790   L3:     END_FOR
              POP_ITER

792           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

793           LOAD_GLOBAL              1 (print + NULL)
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

792   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

788   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "scripts/pas187_fleet_cutover_readiness_check.py", line 796>:
796           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C179C3E10, file "scripts/pas187_fleet_cutover_readiness_check.py", line 796>:
 796           RESUME                   0

 797           NOP

 798   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 799           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 800           LOAD_CONST               3 ('utf-8')

 798           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 802           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 803   L4:     LOAD_GLOBAL             11 (print + NULL)

 804           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 805           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 804           BUILD_STRING             4

 806           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 803           LOAD_CONST               7 (('file',))
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

 802   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18115980, file "scripts/pas187_fleet_cutover_readiness_check.py", line 810>:
810           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D884E0, file "scripts/pas187_fleet_cutover_readiness_check.py", line 810>:
 810            RESUME                   0

 811            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 812            NOP

 813    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 817    L2:     LOAD_GLOBAL             10 (os)
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

 818            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 819            LOAD_GLOBAL             23 (print + NULL)
                LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)
                LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 820            LOAD_SMALL_INT           2
                RETURN_VALUE

 822    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 824            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 825            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 827    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 829            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 830            LOAD_GLOBAL             23 (print + NULL)
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

 832    L6:     LOAD_FAST                5 (report)
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

 814            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 815    L9:     LOAD_FAST                3 (e)
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

 814   L17:     RERAISE                  0

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
