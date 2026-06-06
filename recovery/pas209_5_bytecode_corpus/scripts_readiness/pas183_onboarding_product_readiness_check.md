# scripts_readiness/pas183_onboarding_product_readiness_check

- **pyc:** `scripts\__pycache__\pas183_onboarding_product_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas183_onboarding_product_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas183_onboarding_product_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS183 — Onboarding + product experience readiness gate.

Deterministic, non-mutating evaluator for "is PAS183 wired
correctly and free of regressions in the PAS160-PAS182 +
PAS-SECURITY-01/02/03/04 doctrine?".

Walks the repo and verifies:

  * PAS183 docs exist:
      - docs/orvn_brokerage_onboarding_protocol.md
      - docs/pas_customer_60_second_onboarding_flow.md
      - docs/pas_webapp_readiness_audit.md
      - docs/pas_mobile_oversight_readiness_audit.md
      - docs/pas_pilot_handoff_pack.md
  * Each doc carries its required structural clauses
    (no auto-approval, no Gmail/OAuth, no Composio, no LLM,
    no Memory Review changes, worker off by default,
    operator-only, PII-safe).
  * PAS160-PAS182 + PAS-SECURITY-01/02/03/04 readiness scripts
    still exist (no deletion under PAS183).
  * Memory Review surface (PAS147-PAS158) is intact.
  * audit_service.py STILL has no UPDATE / DELETE helpers.
  * Worker is off by default and not auto-started by main.py.
  * The single-file webapp is intact and references no
    forbidden capability (no AI chat, no Gmail OAuth, etc.).
  * Supports --summary-only / --json.
  * Exits 0 ready, 1 blockers, 2 bad args.
  * Never reads .env. Never touches production data.
```

## Imports

`List`, `Optional`, `Path`, `__future__`, `annotations`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_audit_service_invariant`, `check_doc_no_forbidden_scope`, `check_doc_required_clauses`, `check_files_present`, `check_memory_review_intact`, `check_no_startup_worker`, `check_prior_phases_intact`, `check_self_no_env_or_db`, `check_webapp_intact`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `NOT_READY`, `PAS183`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS183 — Onboarding + product experience readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS183 wired\ncorrectly and free of regressions in the PAS160-PAS182 +\nPAS-SECURITY-01/02/03/04 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS183 docs exist:\n      - docs/orvn_brokerage_onboarding_protocol.md\n      - docs/pas_customer_60_second_onboarding_flow.md\n      - docs/pas_webapp_readiness_audit.md\n      - docs/pas_mobile_oversight_readiness_audit.md\n      - docs/pas_pilot_handoff_pack.md\n  * Each doc carries its required structural clauses\n    (no auto-approval, no Gmail/OAuth, no Composio, no LLM,\n    no Memory Review changes, worker off by default,\n    operator-only, PII-safe).\n  * PAS160-PAS182 + PAS-SECURITY-01/02/03/04 readiness scripts\n    still exist (no deletion under PAS183).\n  * Memory Review surface (PAS147-PAS158) is intact.\n  * audit_service.py STILL has no UPDATE / DELETE helpers.\n  * Worker is off by default and not auto-started by main.py.\n  * The single-file webapp is intact and references no\n    forbidden capability (no AI chat, no Gmail OAuth, etc.).\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env. Never touches production data.\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'docs/orvn_brokerage_onboarding_protocol.md'
- 'docs/pas_customer_60_second_onboarding_flow.md'
- 'docs/pas_webapp_readiness_audit.md'
- 'docs/pas_mobile_oversight_readiness_audit.md'
- 'docs/pas_pilot_handoff_pack.md'
- 'app/static/dashboard/index.html'
- 'severity'
- 'detail'
- 'pas183_onboarding_product_readiness_report.json'
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
- 'Required PAS183 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS183 must not delete'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS183 must not touch'
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
- 'PAS174-PAS182 invariant: audit_service has no UPDATE /\nDELETE helpers. PAS183 must preserve.'
- 'operator'
- 'audit_service.py'
- 'audit_service:append_only_carry'
- 'Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)'
- 'docs:'
- ':clause:'
- ' carries clause: '
- 'expected one of: '
- ' | '
- 'Each PAS183 doc must NOT mention forbidden scope additions\n(Gmail OAuth, Composio, IMAP, embeddings, AI chat assistant).\nMentions of NEGATION (e.g. "no Gmail OAuth") ARE allowed —\nthe scan is for the bare token to appear in a positive\ncontext.'
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
- 'Webapp dashboard file present: '
- 'PAS183 must not delete the dashboard'
- 'webapp:anchor:'
- 'Webapp carries structural anchor: '
- 'missing anchor '
- ':no_forbidden_capability'
- 'Webapp does not carry forbidden capability tokens'
- 'forbidden tokens: '
- 'dotenv import'
- 'supabase import'
- 'load_dotenv()'
- 'load_dotenv() call'
- 'environ read'
- 'get_supabase'
- 'supabase client call'
- 'self_check:no_env_or_db'
- 'PAS183 readiness checker never reads .env / touches DB'
- 'disqualifying patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS183'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 🔒 '<REDACTED:high-entropy blob, len=41>'
- 'PAS183 — Evaluate onboarding + product experience readiness (docs + webapp + prior-phase carry-forward). Read-only — never reads .env, never touches Supabase, never runs a migration.'
- '--repo-root'
- '--output'
- '--json'
- 'store_true'
- '--summary-only'
- '--strict'
- 'report'
- 'None'
- '[PAS183] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS183] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS183 — Onboarding + product experience readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS183 wired\ncorrectly and free of regressions in the PAS160-PAS182 +\nPAS-SECURITY-01/02/03/04 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS183 docs exist:\n      - docs/orvn_brokerage_onboarding_protocol.md\n      - docs/pas_customer_60_second_onboarding_flow.md\n      - docs/pas_webapp_readiness_audit.md\n      - docs/pas_mobile_oversight_readiness_audit.md\n      - docs/pas_pilot_handoff_pack.md\n  * Each doc carries its required structural clauses\n    (no auto-approval, no Gmail/OAuth, no Composio, no LLM,\n    no Memory Review changes, worker off by default,\n    operator-only, PII-safe).\n  * PAS160-PAS182 + PAS-SECURITY-01/02/03/04 readiness scripts\n    still exist (no deletion under PAS183).\n  * Memory Review surface (PAS147-PAS158) is intact.\n  * audit_service.py STILL has no UPDATE / DELETE helpers.\n  * Worker is off by default and not auto-started by main.py.\n  * The single-file webapp is intact and references no\n    forbidden capability (no AI chat, no Gmail OAuth, etc.).\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env. Never touches production data.\n')
               STORE_NAME               0 (__doc__)

  32           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  34           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  35           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  36           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  37           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  38           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  39           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  40           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  43           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  44           NOP

  45   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  43   L4:     END_FOR
               POP_ITER

  50           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  51           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  50           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  55           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  56           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  58           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  65           LOAD_CONST              65 (('docs/orvn_brokerage_onboarding_protocol.md', 'docs/pas_customer_60_second_onboarding_flow.md', 'docs/pas_webapp_readiness_audit.md', 'docs/pas_mobile_oversight_readiness_audit.md', 'docs/pas_pilot_handoff_pack.md'))
               STORE_NAME              28 (REQUIRED_DOCS)

  73           LOAD_CONST              66 (('tests/mvp/test_pas183_onboarding_product_readiness.py',))
               STORE_NAME              29 (REQUIRED_TESTS)

  77           LOAD_CONST              67 (('scripts/pas183_onboarding_product_readiness_check.py',))
               STORE_NAME              30 (REQUIRED_SCRIPTS)

  81           LOAD_CONST              68 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py', 'scripts/pas172_pilot_operations_readiness_check.py', 'scripts/pas173_brokerage_operator_readiness_check.py', 'scripts/pas174_operator_audit_readiness_check.py', 'scripts/pas175_audit_integrity_readiness_check.py', 'scripts/pas176_audit_chain_readiness_check.py', 'scripts/pas177_tenant_audit_verification_readiness_check.py', 'scripts/pas178_audit_window_chain_readiness_check.py', 'scripts/pas179_controlled_learning_readiness_check.py', 'scripts/pas180_learning_review_readiness_check.py', 'scripts/pas181_manual_test_harness_readiness_check.py', 'scripts/pas182_adaptive_memory_bridge_readiness_check.py', 'scripts/pas_security_01_hardening_readiness_check.py', 'scripts/pas_security_02_rate_limit_scanner_readiness_check.py', 'scripts/pas_security_03_admin_webhook_ci_readiness_check.py', 'scripts/pas_security_04_operator_reveal_https_readiness_check.py'))
               STORE_NAME              31 (PRIOR_PHASE_FILES)

 113           LOAD_CONST              69 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              32 (MEMORY_REVIEW_FILES)

 122           LOAD_CONST              17 ('app/static/dashboard/index.html')
               STORE_NAME              33 (DASHBOARD_FILE)

 129           LOAD_CONST              12 ('docs/orvn_brokerage_onboarding_protocol.md')
               LOAD_CONST              70 ((('hard-constraints', ('hard constraints',)), ('no-auto-approval', ('no auto-approval',)), ('no-gmail', ('no gmail',)), ('no-composio', ('no composio',)), ('no-crm', ('no crm integration',)), ('worker-off', ('worker stays off', 'worker remains off')), ('twilio-setup', ('twilio setup',)), ('email-forwarder', ('email forwarder',)), ('slack-ops-only', ('ops-only',)), ('cal.com', ('cal.com',)), ('api-key', ('api key handling',)), ('migration', ('migration posture',)), ('smoke-tests', ('smoke tests',)), ('go-live', ('go-live checklist',)), ('rollback', ('rollback plan',)), ('enterprise', ('enterprise customization', 'enterprise customisation'))))

 149           LOAD_CONST              13 ('docs/pas_customer_60_second_onboarding_flow.md')
               LOAD_CONST              71 ((('60-second', ('60-second', '60 second')), ('what-pas-does', ('what pas does',)), ('what-broker-does', ('what the broker needs to do',)), ('where-to-find', ('where to find',)), ('support', ('contact orvn support', 'how to contact orvn support')), ('do-not-touch', ('not to touch', 'do not touch', 'do not edit')), ('no-auto-approval', ('do not approve memory', 'no auto-approval', 'memory review console'))))

 162           LOAD_CONST              14 ('docs/pas_webapp_readiness_audit.md')
               LOAD_CONST              72 ((('no-redesign', ('no ui redesign',)), ('no-memory-review-change', ('memory review ui changes', 'memory review (pas147')), ('desktop-layout', ('desktop layout',)), ('mobile-oversight', ('mobile oversight',)), ('navigation', ('navigation clarity', 'navigation')), ('dashboard-density', ('dashboard density',)), ('loading-state', ('loading',)), ('empty-state', ('empty',)), ('error-state', ('error',)), ('auth-state', ('auth',)), ('tenant-safe', ('tenant-safe',)), ('no-pii-leak', ('no pii leak', 'no pii leaks', 'pii audit')), ('deliberately-not-built', ('deliberately not', 'intentionally not built', 'not in pas183 scope'))))

 183           LOAD_CONST              15 ('docs/pas_mobile_oversight_readiness_audit.md')
               LOAD_CONST              73 ((('oversight-not-operation', ('supervision, not operation', 'oversight, not operation')), ('no-native-app', ('no mobile native app', 'no native ios')), ('viewport', ('viewport',)), ('breakpoints', ('breakpoint',)), ('read-only', ('read-only',)), ('pii-safety', ('pii safety',)), ('auth', ('auth on mobile', 'auth')), ('deliberately-not-built', ('deliberately not', 'intentionally not built', 'not in pas183 scope'))))

 198           LOAD_CONST              16 ('docs/pas_pilot_handoff_pack.md')
               LOAD_CONST              74 ((('pilot-scope', ('pilot scope',)), ('what-pas-does', ('what pas will do',)), ('what-pas-does-not', ('what pas will not do',)), ('support-hours', ('support hours',)), ('escalation', ('escalation path',)), ('success-metrics', ('success metrics',)), ('known-limitations', ('known limitations',)), ('broker-expectations', ('broker expectations',)), ('orvn-responsibilities', ('orvn operator responsibilities', 'orvn labs commits')), ('data-privacy', ('data + privacy', 'data and privacy', 'privacy posture')), ('rollback-exit', ('rollback', 'exit')), ('sign-off', ('sign-off',)), ('no-auto-renewal', ('no automatic auto-renewal', 'no auto-renewal'))))

 128           BUILD_MAP                5
               STORE_NAME              34 (DOC_REQUIRED_CLAUSES)

 223           LOAD_CONST              75 (('gmail oauth', 'imap', 'pop3', 'composio', 'trustclaw', 'auto-approve', 'auto approve', 'ai chat assistant', 'embedding', 'vector database', 'vector db'))
               STORE_NAME              35 (FORBIDDEN_DOC_TOKENS)

 239           LOAD_CONST              76 (('gmail oauth', 'google.oauth2', 'composio', 'trustclaw', 'ai chat assistant', 'chatgpt assistant', 'anthropic api key'))
               STORE_NAME              36 (FORBIDDEN_WEBAPP_TOKENS)

 254           LOAD_CONST              18 ('severity')

 256           LOAD_NAME               27 (SEVERITY_BLOCK)

 254           LOAD_CONST              19 ('detail')

 256           LOAD_CONST              20 ('')

 254           BUILD_MAP                2
               LOAD_CONST              21 (<code object __annotate__ at 0x0000018C18025130, file "scripts\pas183_onboarding_product_readiness_check.py", line 254>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object _check at 0x0000018C17FA31E0, file "scripts\pas183_onboarding_product_readiness_check.py", line 254>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              37 (_check)

 267           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas183_onboarding_product_readiness_check.py", line 267>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object _now_iso at 0x0000018C18038170, file "scripts\pas183_onboarding_product_readiness_check.py", line 267>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (_now_iso)

 271           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts\pas183_onboarding_product_readiness_check.py", line 271>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object _read_text at 0x0000018C18053870, file "scripts\pas183_onboarding_product_readiness_check.py", line 271>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              39 (_read_text)

 278           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas183_onboarding_product_readiness_check.py", line 278>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object _strip_python_comments_and_strings at 0x0000018C17ED9FB0, file "scripts\pas183_onboarding_product_readiness_check.py", line 278>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              40 (_strip_python_comments_and_strings)

 317           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas183_onboarding_product_readiness_check.py", line 317>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object check_files_present at 0x0000018C1794ED80, file "scripts\pas183_onboarding_product_readiness_check.py", line 317>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (check_files_present)

 330           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C18114120, file "scripts\pas183_onboarding_product_readiness_check.py", line 330>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object check_prior_phases_intact at 0x0000018C18061110, file "scripts\pas183_onboarding_product_readiness_check.py", line 330>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (check_prior_phases_intact)

 343           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C18114210, file "scripts\pas183_onboarding_product_readiness_check.py", line 343>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object check_memory_review_intact at 0x0000018C18060DB0, file "scripts\pas183_onboarding_product_readiness_check.py", line 343>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (check_memory_review_intact)

 356           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C18114300, file "scripts\pas183_onboarding_product_readiness_check.py", line 356>)
               MAKE_FUNCTION
               LOAD_CONST              36 (<code object check_worker_off_by_default at 0x0000018C179C3A50, file "scripts\pas183_onboarding_product_readiness_check.py", line 356>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (check_worker_off_by_default)

 373           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C181143F0, file "scripts\pas183_onboarding_product_readiness_check.py", line 373>)
               MAKE_FUNCTION
               LOAD_CONST              38 (<code object check_no_startup_worker at 0x0000018C17D86AE0, file "scripts\pas183_onboarding_product_readiness_check.py", line 373>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (check_no_startup_worker)

 396           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C181145D0, file "scripts\pas183_onboarding_product_readiness_check.py", line 396>)
               MAKE_FUNCTION
               LOAD_CONST              40 (<code object check_audit_service_invariant at 0x0000018C182DD0A0, file "scripts\pas183_onboarding_product_readiness_check.py", line 396>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_audit_service_invariant)

 423           LOAD_CONST              41 (<code object __annotate__ at 0x0000018C181146C0, file "scripts\pas183_onboarding_product_readiness_check.py", line 423>)
               MAKE_FUNCTION
               LOAD_CONST              42 (<code object check_doc_required_clauses at 0x0000018C17E7F520, file "scripts\pas183_onboarding_product_readiness_check.py", line 423>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_doc_required_clauses)

 441           LOAD_CONST              43 (<code object __annotate__ at 0x0000018C181148A0, file "scripts\pas183_onboarding_product_readiness_check.py", line 441>)
               MAKE_FUNCTION
               LOAD_CONST              44 (<code object check_doc_no_forbidden_scope at 0x0000018C181A0570, file "scripts\pas183_onboarding_product_readiness_check.py", line 441>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_doc_no_forbidden_scope)

 488           LOAD_CONST              45 (<code object __annotate__ at 0x0000018C18114990, file "scripts\pas183_onboarding_product_readiness_check.py", line 488>)
               MAKE_FUNCTION
               LOAD_CONST              46 (<code object check_webapp_intact at 0x0000018C17D893A0, file "scripts\pas183_onboarding_product_readiness_check.py", line 488>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_webapp_intact)

 530           LOAD_CONST              47 (<code object __annotate__ at 0x0000018C18114A80, file "scripts\pas183_onboarding_product_readiness_check.py", line 530>)
               MAKE_FUNCTION
               LOAD_CONST              48 (<code object check_self_no_env_or_db at 0x0000018C17D89750, file "scripts\pas183_onboarding_product_readiness_check.py", line 530>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_self_no_env_or_db)

 563           LOAD_CONST              49 (<code object __annotate__ at 0x0000018C18114B70, file "scripts\pas183_onboarding_product_readiness_check.py", line 563>)
               MAKE_FUNCTION
               LOAD_CONST              50 (<code object _aggregate at 0x0000018C1800B0A0, file "scripts\pas183_onboarding_product_readiness_check.py", line 563>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (_aggregate)

 575           LOAD_CONST              51 (<code object __annotate__ at 0x0000018C18114C60, file "scripts\pas183_onboarding_product_readiness_check.py", line 575>)
               MAKE_FUNCTION
               LOAD_CONST              52 (<code object _operator_actions at 0x0000018C180483B0, file "scripts\pas183_onboarding_product_readiness_check.py", line 575>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (_operator_actions)

 585           LOAD_CONST              53 (<code object __annotate__ at 0x0000018C18114D50, file "scripts\pas183_onboarding_product_readiness_check.py", line 585>)
               MAKE_FUNCTION
               LOAD_CONST              54 (<code object evaluate at 0x0000018C17F7D130, file "scripts\pas183_onboarding_product_readiness_check.py", line 585>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (evaluate)

 614           LOAD_CONST              55 ('pas183_onboarding_product_readiness_report.json')
               STORE_NAME              54 (REPORT_FILENAME)

 617           LOAD_CONST              56 (<code object __annotate__ at 0x0000018C18114E40, file "scripts\pas183_onboarding_product_readiness_check.py", line 617>)
               MAKE_FUNCTION
               LOAD_CONST              57 (<code object _build_parser at 0x0000018C180FC990, file "scripts\pas183_onboarding_product_readiness_check.py", line 617>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (_build_parser)

 635           LOAD_CONST              58 (<code object __annotate__ at 0x0000018C18114F30, file "scripts\pas183_onboarding_product_readiness_check.py", line 635>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object _print_summary at 0x0000018C17D8CD10, file "scripts\pas183_onboarding_product_readiness_check.py", line 635>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (_print_summary)

 653           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C18024C30, file "scripts\pas183_onboarding_product_readiness_check.py", line 653>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object _write_report at 0x0000018C180FC7B0, file "scripts\pas183_onboarding_product_readiness_check.py", line 653>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (_write_report)

 667           LOAD_CONST              77 ((None,))
               LOAD_CONST              62 (<code object __annotate__ at 0x0000018C18115020, file "scripts\pas183_onboarding_product_readiness_check.py", line 667>)
               MAKE_FUNCTION
               LOAD_CONST              63 (<code object main at 0x0000018C17D884E0, file "scripts\pas183_onboarding_product_readiness_check.py", line 667>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              58 (main)

 692           LOAD_NAME               59 (__name__)
               LOAD_CONST              64 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 693           LOAD_NAME                6 (sys)
               LOAD_ATTR              120 (exit)
               PUSH_NULL
               LOAD_NAME               58 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 692   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  46           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  47   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          319 (to L1)

  46   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "scripts\pas183_onboarding_product_readiness_check.py", line 254>:
254           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

255           LOAD_CONST               2 ('str')

254           LOAD_CONST               3 ('status')

255           LOAD_CONST               2 ('str')

254           LOAD_CONST               4 ('label')

255           LOAD_CONST               2 ('str')

254           LOAD_CONST               5 ('severity')

256           LOAD_CONST               2 ('str')

254           LOAD_CONST               6 ('detail')

256           LOAD_CONST               2 ('str')

254           LOAD_CONST               7 ('return')

257           LOAD_CONST               8 ('dict')

254           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA31E0, file "scripts\pas183_onboarding_product_readiness_check.py", line 254>:
254           RESUME                   0

259           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

260           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

261           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

262           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

263           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

258           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas183_onboarding_product_readiness_check.py", line 267>:
267           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038170, file "scripts\pas183_onboarding_product_readiness_check.py", line 267>:
267           RESUME                   0

268           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts\pas183_onboarding_product_readiness_check.py", line 271>:
271           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053870, file "scripts\pas183_onboarding_product_readiness_check.py", line 271>:
 271           RESUME                   0

 272           NOP

 273   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 274           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 275   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 274   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas183_onboarding_product_readiness_check.py", line 278>:
278           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17ED9FB0, file "scripts\pas183_onboarding_product_readiness_check.py", line 278>:
278            RESUME                   0

279            BUILD_LIST               0
               STORE_FAST               1 (out)

280            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

281    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

282            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

283            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

284            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

285            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

286            JUMP_FORWARD           240 (to L13)

287    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

288            JUMP_BACKWARD           59 (to L1)

289    L3:     LOAD_FAST_BORROW         0 (src)
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

290    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

291            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

292            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

293            JUMP_FORWARD           138 (to L13)

294    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

295            JUMP_BACKWARD          161 (to L1)

296    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

297            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

298            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

299    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

300            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

301            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

302            JUMP_BACKWARD           30 (to L7)

303    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

304    L9:     JUMP_FORWARD            11 (to L11)

305   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

306   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

307            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

308   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

309            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

310   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas183_onboarding_product_readiness_check.py", line 317>:
317           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C1794ED80, file "scripts\pas183_onboarding_product_readiness_check.py", line 317>:
317           RESUME                   0

318           BUILD_LIST               0
              STORE_FAST               1 (out)

319           LOAD_GLOBAL              0 (REQUIRED_DOCS)
              LOAD_GLOBAL              2 (REQUIRED_TESTS)
              BINARY_OP                0 (+)
              LOAD_GLOBAL              4 (REQUIRED_SCRIPTS)
              BINARY_OP                0 (+)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

320           LOAD_GLOBAL              7 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                9 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

321           LOAD_FAST                1 (out)
              LOAD_ATTR               11 (append + NULL|self)
              LOAD_GLOBAL             13 (_check + NULL)

322           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

323           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

324   L3:     LOAD_CONST               3 ('Required PAS183 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

325           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

321   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

319   L6:     END_FOR
              POP_ITER

327           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114120, file "scripts\pas183_onboarding_product_readiness_check.py", line 330>:
330           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C18061110, file "scripts\pas183_onboarding_product_readiness_check.py", line 330>:
330           RESUME                   0

331           BUILD_LIST               0
              STORE_FAST               1 (out)

332           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

333           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

334           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

335           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

336           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

337   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

338           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS183 must not delete')

334   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

332   L6:     END_FOR
              POP_ITER

340           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114210, file "scripts\pas183_onboarding_product_readiness_check.py", line 343>:
343           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18060DB0, file "scripts\pas183_onboarding_product_readiness_check.py", line 343>:
343           RESUME                   0

344           BUILD_LIST               0
              STORE_FAST               1 (out)

345           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

346           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

347           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

348           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

349           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

350   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

351           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS183 must not touch')

347   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

345   L6:     END_FOR
              POP_ITER

353           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114300, file "scripts\pas183_onboarding_product_readiness_check.py", line 356>:
356           RESUME                   0
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C179C3A50, file "scripts\pas183_onboarding_product_readiness_check.py", line 356>:
356           RESUME                   0

357           BUILD_LIST               0
              STORE_FAST               1 (out)

358           LOAD_GLOBAL              1 (Path + NULL)
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

359           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

361           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

362           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

360   L2:     STORE_FAST               4 (literal_ok)

364           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

365           LOAD_CONST               7 ('worker:off_by_default')

366           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

367   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default')

368           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

364   L6:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

370           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181143F0, file "scripts\pas183_onboarding_product_readiness_check.py", line 373>:
373           RESUME                   0
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

Disassembly of <code object check_no_startup_worker at 0x0000018C17D86AE0, file "scripts\pas183_onboarding_product_readiness_check.py", line 373>:
373           RESUME                   0

374           BUILD_LIST               0
              STORE_FAST               1 (out)

375           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

376           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

377           LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (executable)

378           BUILD_LIST               0
              STORE_FAST               5 (bad)

379           LOAD_CONST               3 ('from app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L2)
              NOT_TAKEN

380           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               4 ('from app.services.ingestion.worker import …')
              CALL                     1
              POP_TOP

381   L2:     LOAD_CONST               5 ('import app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L3)
              NOT_TAKEN

382           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               5 ('import app.services.ingestion.worker')
              CALL                     1
              POP_TOP

383   L3:     LOAD_CONST               6 ('run_worker_loop')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L4)
              NOT_TAKEN

384           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               7 ('run_worker_loop reference')
              CALL                     1
              POP_TOP

385   L4:     LOAD_CONST               8 ('process_pending_call(')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L5)
              NOT_TAKEN

386           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               9 ('process_pending_call call')
              CALL                     1
              POP_TOP

387   L5:     LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

388           LOAD_CONST              10 ('main:no_startup_worker')

389           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST              11 ('FAIL')
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST              12 ('PASS')

390   L7:     LOAD_CONST              13 ('FastAPI lifespan does not auto-start the pending-call worker')

391           LOAD_FAST_BORROW         5 (bad)
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

387   L9:     LOAD_CONST              16 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

393           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181145D0, file "scripts\pas183_onboarding_product_readiness_check.py", line 396>:
396           RESUME                   0
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

Disassembly of <code object check_audit_service_invariant at 0x0000018C182DD0A0, file "scripts\pas183_onboarding_product_readiness_check.py", line 396>:
396           RESUME                   0

399           BUILD_LIST               0
              STORE_FAST               1 (out)

400           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               1 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('operator')
              BINARY_OP               11 (/)
              LOAD_CONST               4 ('audit_service.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

401           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               5 ('')
      L1:     STORE_FAST               3 (src)

402           LOAD_CONST              13 (('def update_audit_', 'def delete_audit_', 'def update_operator_audit_', 'def delete_operator_audit_', 'def mutate_audit_', 'def truncate_audit_'))
              STORE_FAST               4 (forbidden)

410           BUILD_LIST               0
              STORE_FAST               5 (bad)

411           LOAD_FAST_BORROW         4 (forbidden)
              GET_ITER
      L2:     FOR_ITER                28 (to L4)
              STORE_FAST               6 (tok)

412           LOAD_FAST_BORROW_LOAD_FAST_BORROW 99 (tok, src)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

413   L3:     LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW         6 (tok)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           30 (to L2)

411   L4:     END_FOR
              POP_ITER

414           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

415           LOAD_CONST               6 ('audit_service:append_only_carry')

416           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               7 ('FAIL')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               8 ('PASS')

417   L6:     LOAD_CONST               9 ('Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)')

418           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L7)
              NOT_TAKEN
              LOAD_CONST              10 ('disqualifying tokens: ')
              LOAD_CONST              11 (', ')
              LOAD_ATTR                9 (join + NULL|self)
              LOAD_FAST_BORROW         5 (bad)
              CALL                     1
              BINARY_OP                0 (+)
              JUMP_FORWARD             1 (to L8)
      L7:     LOAD_CONST               5 ('')

414   L8:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

420           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181146C0, file "scripts\pas183_onboarding_product_readiness_check.py", line 423>:
423           RESUME                   0
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

Disassembly of <code object check_doc_required_clauses at 0x0000018C17E7F520, file "scripts\pas183_onboarding_product_readiness_check.py", line 423>:
  --            MAKE_CELL                9 (lower)

 423            RESUME                   0

 424            BUILD_LIST               0
                STORE_FAST               1 (out)

 425            LOAD_GLOBAL              0 (DOC_REQUIRED_CLAUSES)
                LOAD_ATTR                3 (items + NULL|self)
                CALL                     0
                GET_ITER
        L1:     FOR_ITER               212 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   35 (relpath, clauses)

 426            LOAD_GLOBAL              5 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_FAST_BORROW         2 (relpath)
                BINARY_OP               11 (/)
                STORE_FAST               4 (p)

 427            LOAD_GLOBAL              7 (_read_text + NULL)
                LOAD_FAST_BORROW         4 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 ('')
        L2:     STORE_FAST               5 (src)

 428            LOAD_FAST_BORROW         5 (src)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              9 (lower)

 429            LOAD_FAST_BORROW         3 (clauses)
                GET_ITER
        L3:     FOR_ITER               146 (to L13)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  103 (name, phrases)

 430            LOAD_GLOBAL             10 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L7)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         9 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18025C30, file "scripts\pas183_onboarding_product_readiness_check.py", line 430>)
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
                LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18025C30, file "scripts\pas183_onboarding_product_readiness_check.py", line 430>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         7 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L8:     STORE_FAST               8 (present)

 431            LOAD_FAST                1 (out)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_GLOBAL             15 (_check + NULL)

 432            LOAD_CONST               4 ('docs:')
                LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                LOAD_CONST               5 (':clause:')
                LOAD_FAST_BORROW         6 (name)
                FORMAT_SIMPLE
                BUILD_STRING             4

 433            LOAD_FAST_BORROW         8 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST               6 ('PASS')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               7 ('FAIL')

 434   L10:     LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                LOAD_CONST               8 (' carries clause: ')
                LOAD_FAST_BORROW         6 (name)
                FORMAT_SIMPLE
                BUILD_STRING             3

 436            LOAD_FAST_BORROW         8 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L11)
                NOT_TAKEN

 435            LOAD_CONST               9 ('expected one of: ')
                LOAD_CONST              10 (' | ')
                LOAD_ATTR               17 (join + NULL|self)
                LOAD_FAST_BORROW         7 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L12)

 436   L11:     LOAD_CONST               0 ('')

 431   L12:     LOAD_CONST              11 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L3)

 429   L13:     END_FOR
                POP_ITER
                JUMP_BACKWARD          214 (to L1)

 425   L14:     END_FOR
                POP_ITER

 438            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025C30, file "scripts\pas183_onboarding_product_readiness_check.py", line 430>:
  --           COPY_FREE_VARS           1

 430           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C181148A0, file "scripts\pas183_onboarding_product_readiness_check.py", line 441>:
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

Disassembly of <code object check_doc_no_forbidden_scope at 0x0000018C181A0570, file "scripts\pas183_onboarding_product_readiness_check.py", line 441>:
441            RESUME                   0

447            BUILD_LIST               0
               STORE_FAST               1 (out)

448            LOAD_GLOBAL              0 (REQUIRED_DOCS)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               431 (to L13)
               STORE_FAST               2 (relpath)

449            LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         2 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               3 (p)

450            LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         3 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               4 (src)

451            LOAD_FAST_BORROW         4 (src)
               LOAD_ATTR                7 (lower + NULL|self)
               CALL                     0
               STORE_FAST               5 (lower)

452            BUILD_LIST               0
               STORE_FAST               6 (bad)

453            LOAD_GLOBAL              8 (FORBIDDEN_DOC_TOKENS)
               GET_ITER
       L3:     EXTENDED_ARG             1
               FOR_ITER               262 (to L8)
               STORE_FAST               7 (tok)

456            LOAD_FAST_BORROW         5 (lower)
               LOAD_ATTR               11 (find + NULL|self)
               LOAD_FAST_BORROW         7 (tok)
               CALL                     1
               STORE_FAST               8 (idx)

457    L4:     LOAD_FAST_BORROW         8 (idx)
               LOAD_SMALL_INT           0
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           30 (to L3)

459    L5:     LOAD_GLOBAL             13 (max + NULL)
               LOAD_SMALL_INT           0
               LOAD_FAST_BORROW         8 (idx)
               LOAD_SMALL_INT          30
               BINARY_OP               10 (-)
               CALL                     2
               STORE_FAST               9 (window_start)

460            LOAD_FAST_BORROW_LOAD_FAST_BORROW 89 (lower, window_start)
               LOAD_FAST_BORROW         8 (idx)
               BINARY_SLICE
               STORE_FAST              10 (preceding)

462            LOAD_CONST               2 ('no ')
               LOAD_FAST_BORROW        10 (preceding)
               LOAD_CONST              22 (-12)
               LOAD_CONST               3 (None)
               BINARY_SLICE
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE       135 (to L6)
               NOT_TAKEN
               POP_TOP

463            LOAD_CONST               4 ('no-')
               LOAD_FAST_BORROW        10 (preceding)
               LOAD_CONST              22 (-12)
               LOAD_CONST               3 (None)
               BINARY_SLICE
               CONTAINS_OP              0 (in)

462            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE       119 (to L6)
               NOT_TAKEN
               POP_TOP

464            LOAD_CONST               5 ('❌')
               LOAD_FAST_BORROW        10 (preceding)
               CONTAINS_OP              0 (in)

462            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE       106 (to L6)
               NOT_TAKEN
               POP_TOP

465            LOAD_CONST               6 ('do not')
               LOAD_FAST_BORROW        10 (preceding)
               CONTAINS_OP              0 (in)

462            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        93 (to L6)
               NOT_TAKEN
               POP_TOP

466            LOAD_CONST               7 ("doesn't")
               LOAD_FAST_BORROW        10 (preceding)
               CONTAINS_OP              0 (in)

462            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        80 (to L6)
               NOT_TAKEN
               POP_TOP

467            LOAD_CONST               8 ('does not')
               LOAD_FAST_BORROW        10 (preceding)
               CONTAINS_OP              0 (in)

462            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        67 (to L6)
               NOT_TAKEN
               POP_TOP

468            LOAD_CONST               9 ('never ')
               LOAD_FAST_BORROW        10 (preceding)
               LOAD_CONST              23 (-15)
               LOAD_CONST               3 (None)
               BINARY_SLICE
               CONTAINS_OP              0 (in)

462            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        51 (to L6)
               NOT_TAKEN
               POP_TOP

469            LOAD_CONST              10 ('without ')
               LOAD_FAST_BORROW        10 (preceding)
               LOAD_CONST              23 (-15)
               LOAD_CONST               3 (None)
               BINARY_SLICE
               CONTAINS_OP              0 (in)

462            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        35 (to L6)
               NOT_TAKEN
               POP_TOP

470            LOAD_CONST              11 ('out of scope')
               LOAD_FAST_BORROW        10 (preceding)
               CONTAINS_OP              0 (in)

462            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        22 (to L6)
               NOT_TAKEN
               POP_TOP

471            LOAD_CONST              12 ('not ')
               LOAD_FAST_BORROW        10 (preceding)
               LOAD_CONST              24 (-10)
               LOAD_CONST               3 (None)
               BINARY_SLICE
               CONTAINS_OP              0 (in)

462            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L6)
               NOT_TAKEN
               POP_TOP

472            LOAD_CONST              13 ('deferred')
               LOAD_FAST_BORROW        10 (preceding)
               CONTAINS_OP              0 (in)

461    L6:     STORE_FAST              11 (negated)

474            LOAD_FAST_BORROW        11 (negated)
               TO_BOOL
               POP_JUMP_IF_TRUE        20 (to L7)
               NOT_TAKEN

475            LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         7 (tok)
               CALL                     1
               POP_TOP

476            JUMP_BACKWARD          230 (to L3)

477    L7:     LOAD_FAST_BORROW         5 (lower)
               LOAD_ATTR               11 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (tok, idx)
               LOAD_GLOBAL             17 (len + NULL)
               LOAD_FAST_BORROW         7 (tok)
               CALL                     1
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               8 (idx)
               JUMP_BACKWARD          244 (to L4)

453    L8:     END_FOR
               POP_ITER

478            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

479            LOAD_CONST              14 ('docs:')
               LOAD_FAST_BORROW         2 (relpath)
               FORMAT_SIMPLE
               LOAD_CONST              15 (':no_forbidden_scope')
               BUILD_STRING             3

480            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST              16 ('FAIL')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST              17 ('PASS')

481   L10:     LOAD_FAST_BORROW         2 (relpath)
               FORMAT_SIMPLE
               LOAD_CONST              18 (' does not introduce forbidden scope tokens')
               BUILD_STRING             2

483            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L11)
               NOT_TAKEN

482            LOAD_CONST              19 ('positive mentions of: ')
               LOAD_CONST              20 (', ')
               LOAD_ATTR               21 (join + NULL|self)
               LOAD_GLOBAL             23 (sorted + NULL)
               LOAD_GLOBAL             25 (set + NULL)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               CALL                     1
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L12)

483   L11:     LOAD_CONST               1 ('')

478   L12:     LOAD_CONST              21 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          434 (to L1)

448   L13:     END_FOR
               POP_ITER

485            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114990, file "scripts\pas183_onboarding_product_readiness_check.py", line 488>:
488           RESUME                   0
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

Disassembly of <code object check_webapp_intact at 0x0000018C17D893A0, file "scripts\pas183_onboarding_product_readiness_check.py", line 488>:
488            RESUME                   0

489            BUILD_LIST               0
               STORE_FAST               1 (out)

490            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_GLOBAL              2 (DASHBOARD_FILE)
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

491            LOAD_FAST_BORROW         2 (p)
               LOAD_ATTR                5 (is_file + NULL|self)
               CALL                     0
               STORE_FAST               3 (ok)

492            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

493            LOAD_CONST               0 ('webapp:')
               LOAD_GLOBAL              2 (DASHBOARD_FILE)
               FORMAT_SIMPLE
               BUILD_STRING             2

494            LOAD_FAST_BORROW         3 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN
               LOAD_CONST               1 ('PASS')
               JUMP_FORWARD             1 (to L2)
       L1:     LOAD_CONST               2 ('FAIL')

495    L2:     LOAD_CONST               3 ('Webapp dashboard file present: ')
               LOAD_GLOBAL              2 (DASHBOARD_FILE)
               FORMAT_SIMPLE
               BUILD_STRING             2

496            LOAD_FAST_BORROW         3 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               5 ('PAS183 must not delete the dashboard')

492    L4:     LOAD_CONST               6 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

498            LOAD_FAST_BORROW         3 (ok)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN

499            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

500    L5:     LOAD_GLOBAL             11 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L6:     STORE_FAST               4 (src)

501            LOAD_FAST_BORROW         4 (src)
               LOAD_ATTR               13 (lower + NULL|self)
               CALL                     0
               STORE_FAST               5 (lower)

503            LOAD_CONST              14 ((('viewport', 'name="viewport"'), ('login-screen', '.login-screen'), ('empty-box', '.empty-box'), ('media-query', '@media')))
               STORE_FAST               6 (required_anchors)

509            LOAD_FAST_BORROW         6 (required_anchors)
               GET_ITER
       L7:     FOR_ITER                61 (to L12)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST  120 (name, anchor)

510            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

511            LOAD_CONST               7 ('webapp:anchor:')
               LOAD_FAST_BORROW         7 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

512            LOAD_FAST_BORROW_LOAD_FAST_BORROW 132 (anchor, src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               1 ('PASS')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               2 ('FAIL')

513    L9:     LOAD_CONST               8 ('Webapp carries structural anchor: ')
               LOAD_FAST_BORROW         7 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

514            LOAD_FAST_BORROW_LOAD_FAST_BORROW 132 (anchor, src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             5 (to L11)
      L10:     LOAD_CONST               9 ('missing anchor ')
               LOAD_FAST_BORROW         8 (anchor)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2

510   L11:     LOAD_CONST               6 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           63 (to L7)

509   L12:     END_FOR
               POP_ITER

516            BUILD_LIST               0
               STORE_FAST               9 (bad)

517            LOAD_GLOBAL             14 (FORBIDDEN_WEBAPP_TOKENS)
               GET_ITER
      L13:     FOR_ITER                28 (to L15)
               STORE_FAST              10 (tok)

518            LOAD_FAST_BORROW_LOAD_FAST_BORROW 165 (tok, lower)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L14)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L13)

519   L14:     LOAD_FAST_BORROW         9 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW        10 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L13)

517   L15:     END_FOR
               POP_ITER

520            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

521            LOAD_CONST               0 ('webapp:')
               LOAD_GLOBAL              2 (DASHBOARD_FILE)
               FORMAT_SIMPLE
               LOAD_CONST              10 (':no_forbidden_capability')
               BUILD_STRING             3

522            LOAD_FAST_BORROW         9 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L16)
               NOT_TAKEN
               LOAD_CONST               2 ('FAIL')
               JUMP_FORWARD             1 (to L17)
      L16:     LOAD_CONST               1 ('PASS')

523   L17:     LOAD_CONST              11 ('Webapp does not carry forbidden capability tokens')

525            LOAD_FAST_BORROW         9 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L18)
               NOT_TAKEN

524            LOAD_CONST              12 ('forbidden tokens: ')
               LOAD_CONST              13 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_GLOBAL             19 (sorted + NULL)
               LOAD_GLOBAL             21 (set + NULL)
               LOAD_FAST_BORROW         9 (bad)
               CALL                     1
               CALL                     1
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L19)

525   L18:     LOAD_CONST               4 ('')

520   L19:     LOAD_CONST               6 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

527            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114A80, file "scripts\pas183_onboarding_product_readiness_check.py", line 530>:
530           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17D89750, file "scripts\pas183_onboarding_product_readiness_check.py", line 530>:
530            RESUME                   0

531            BUILD_LIST               0
               STORE_FAST               1 (out)

532            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

533            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

534            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

535            BUILD_LIST               0
               STORE_FAST               5 (bad)

536            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR               11 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (raw_line)

537            LOAD_FAST_BORROW         6 (raw_line)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

538            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

539            JUMP_BACKWARD           29 (to L2)

540    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

541            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

542    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

543            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

544    L5:     LOAD_CONST               3 ('load_dotenv()')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

545            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

546    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

547            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

548    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

549    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

536    L9:     END_FOR
               POP_ITER

550            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

551            LOAD_CONST               8 ('self_check:no_env_or_db')

552            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              10 ('PASS')

553   L11:     LOAD_CONST              11 ('PAS183 readiness checker never reads .env / touches DB')

554            LOAD_FAST_BORROW         5 (bad)
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

550   L13:     LOAD_CONST              14 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

556            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114B70, file "scripts\pas183_onboarding_product_readiness_check.py", line 563>:
563           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C1800B0A0, file "scripts\pas183_onboarding_product_readiness_check.py", line 563>:
 563            RESUME                   0

 565            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 564            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 565    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 566            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 565    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 566    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 565    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 564    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 569            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L9)
                NOT_TAKEN
                LOAD_GLOBAL              4 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L10)
        L9:     LOAD_GLOBAL              6 (VERDICT_READY)

 570   L10:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 571            LOAD_CONST               5 ('info')
                BUILD_LIST               0

 568            BUILD_MAP                3
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 564            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L11 [2]
  L4 to L5 -> L11 [2]
  L6 to L8 -> L11 [2]

Disassembly of <code object __annotate__ at 0x0000018C18114C60, file "scripts\pas183_onboarding_product_readiness_check.py", line 575>:
575           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C180483B0, file "scripts\pas183_onboarding_product_readiness_check.py", line 575>:
575           RESUME                   0

576           BUILD_LIST               0
              STORE_FAST               1 (out)

577           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

578           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

579           JUMP_BACKWARD           19 (to L1)

580   L2:     LOAD_FAST_BORROW         2 (c)
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

581           LOAD_FAST                1 (out)
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

577   L5:     END_FOR
              POP_ITER

582           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114D50, file "scripts\pas183_onboarding_product_readiness_check.py", line 585>:
585           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17F7D130, file "scripts\pas183_onboarding_product_readiness_check.py", line 585>:
585           RESUME                   0

586           BUILD_LIST               0
              STORE_FAST               1 (checks)

587           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

588           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

589           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

590           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

591           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_no_startup_worker + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

592           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_audit_service_invariant + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

593           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_doc_required_clauses + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

594           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_doc_no_forbidden_scope + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

595           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_webapp_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

596           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_self_no_env_or_db + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

598           LOAD_GLOBAL             23 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

600           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS183')

601           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             25 (_now_iso + NULL)
              CALL                     0

602           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

603           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             26 (VERDICT_READY)
              COMPARE_OP              72 (==)

604           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             29 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

605           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             29 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

606           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             29 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

607           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             31 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053990, file "scripts\pas183_onboarding_product_readiness_check.py", line 607>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

608           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             31 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18052F70, file "scripts\pas183_onboarding_product_readiness_check.py", line 608>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

609           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

610           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             33 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

599           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053990, file "scripts\pas183_onboarding_product_readiness_check.py", line 607>:
 607           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18052F70, file "scripts\pas183_onboarding_product_readiness_check.py", line 608>:
 608           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C18114E40, file "scripts\pas183_onboarding_product_readiness_check.py", line 617>:
617           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C180FC990, file "scripts\pas183_onboarding_product_readiness_check.py", line 617>:
617           RESUME                   0

618           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

619           LOAD_CONST               0 ('pas183_onboarding_product_readiness_check')

621           LOAD_CONST               1 ('PAS183 — Evaluate onboarding + product experience readiness (docs + webapp + prior-phase carry-forward). Read-only — never reads .env, never touches Supabase, never runs a migration.')

618           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

627           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

628           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               5 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

629           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               6 ('--json')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

630           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               9 ('--summary-only')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

631           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              10 ('--strict')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

632           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114F30, file "scripts\pas183_onboarding_product_readiness_check.py", line 635>:
635           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8CD10, file "scripts\pas183_onboarding_product_readiness_check.py", line 635>:
635           RESUME                   0

636           LOAD_GLOBAL              1 (print + NULL)

637           LOAD_CONST               0 ('[PAS183] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

638           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

639           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

640           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

641           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

642           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

637           BUILD_STRING            12

636           CALL                     1
              POP_TOP

644           LOAD_FAST_BORROW         0 (report)
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

645           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

646           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS183] operator actions:')
              CALL                     1
              POP_TOP

647           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

648           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

647   L3:     END_FOR
              POP_ITER

649           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

650           LOAD_GLOBAL              1 (print + NULL)
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

649   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

645   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "scripts\pas183_onboarding_product_readiness_check.py", line 653>:
653           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C180FC7B0, file "scripts\pas183_onboarding_product_readiness_check.py", line 653>:
 653           RESUME                   0

 654           NOP

 655   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 656           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 657           LOAD_CONST               3 ('utf-8')

 655           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 659           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 660   L4:     LOAD_GLOBAL             11 (print + NULL)

 661           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 662           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 661           BUILD_STRING             4

 663           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 660           LOAD_CONST               7 (('file',))
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

 659   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18115020, file "scripts\pas183_onboarding_product_readiness_check.py", line 667>:
667           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D884E0, file "scripts\pas183_onboarding_product_readiness_check.py", line 667>:
 667            RESUME                   0

 668            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 669            NOP

 670    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 674    L2:     LOAD_GLOBAL             10 (os)
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

 675            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 676            LOAD_GLOBAL             23 (print + NULL)
                LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)
                LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 677            LOAD_SMALL_INT           2
                RETURN_VALUE

 679    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 681            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 682            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 684    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 686            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 687            LOAD_GLOBAL             23 (print + NULL)
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

 689    L6:     LOAD_FAST                5 (report)
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

 671            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 672    L9:     LOAD_FAST                3 (e)
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

 671   L17:     RERAISE                  0

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
