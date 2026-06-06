# scripts_readiness/pas158_memory_review_readiness_check

- **pyc:** `scripts\__pycache__\pas158_memory_review_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas158_memory_review_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas158_memory_review_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS158 — Memory Review subsystem readiness gate.

Deterministic, non-mutating evaluator for "is the admin Memory
Review subsystem operator-ready?". Walks the repo, confirms the
per-phase docs from PAS147 → PAS157 plus the PAS158 runbook /
checklist exist, confirms the eight admin endpoints under
``/admin/memory/`` are declared, confirms the Memory Review tab
in the dashboard carries every expected control, and confirms
that the brokerage portal carries NONE of them and that the
Memory Review UI carries no forbidden mutation or raw-payload
tokens. Emits a verdict (READY / NOT_READY) plus a machine-
readable ``pas158_memory_review_readiness_report.json``.

This script never:
  * modifies files,
  * calls Supabase,
  * reads .env / secrets,
  * includes payload values in the report or summary,
  * touches the off-limits
    ``scripts/combined_supabase_migration.sql``.

Usage:
  python scripts/pas158_memory_review_readiness_check.py
  python scripts/pas158_memory_review_readiness_check.py --json
  python scripts/pas158_memory_review_readiness_check.py --summary-only
  python scripts/pas158_memory_review_readiness_check.py --strict

Exit codes:
    0  — READY  (or READY_WITH_INFO; --strict ignores INFO)
    1  — NOT_READY
    2  — bad CLI arguments
```

## Imports

`Iterable`, `List`, `Optional`, `Path`, `Tuple`, `__future__`, `annotations`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_check_files`, `_now_iso`, `_operator_actions`, `_pas148_section`, `_print_summary`, `_read_text`, `_strip_js_comments_and_strings`, `_write_report`, `check_admin_routes`, `check_dashboard_ui_tokens`, `check_forbidden_raw_fields_in_ui`, `check_forbidden_ui_controls`, `check_no_env_read`, `check_offlimits_present`, `check_phase_docs`, `check_portal_isolation`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `FORBIDDEN_PORTAL_TOKENS`, `FORBIDDEN_RAW_FIELDS_IN_UI`, `FORBIDDEN_UI_CONTROLS`, `INFO`, `NOT_READY`, `OFFLIMITS_FILES`, `PAS158`, `PASS`, `READY`, `REQUIRED_ADMIN_ROUTES`, `REQUIRED_PHASE_DOCS`, `REQUIRED_UI_TOKENS`

## String constants (redacted where noted)

- '\nPAS158 — Memory Review subsystem readiness gate.\n\nDeterministic, non-mutating evaluator for "is the admin Memory\nReview subsystem operator-ready?". Walks the repo, confirms the\nper-phase docs from PAS147 → PAS157 plus the PAS158 runbook /\nchecklist exist, confirms the eight admin endpoints under\n``/admin/memory/`` are declared, confirms the Memory Review tab\nin the dashboard carries every expected control, and confirms\nthat the brokerage portal carries NONE of them and that the\nMemory Review UI carries no forbidden mutation or raw-payload\ntokens. Emits a verdict (READY / NOT_READY) plus a machine-\nreadable ``pas158_memory_review_readiness_report.json``.\n\nThis script never:\n  * modifies files,\n  * calls Supabase,\n  * reads .env / secrets,\n  * includes payload values in the report or summary,\n  * touches the off-limits\n    ``scripts/combined_supabase_migration.sql``.\n\nUsage:\n  python scripts/pas158_memory_review_readiness_check.py\n  python scripts/pas158_memory_review_readiness_check.py --json\n  python scripts/pas158_memory_review_readiness_check.py --summary-only\n  python scripts/pas158_memory_review_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (or READY_WITH_INFO; --strict ignores INFO)\n    1  — NOT_READY\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'Tuple[str, ...]'
- 'REQUIRED_PHASE_DOCS'
- 'Tuple[Tuple[str, Tuple[str, ...]], ...]'
- 'REQUIRED_ADMIN_ROUTES'
- 'REQUIRED_UI_TOKENS'
- 'FORBIDDEN_PORTAL_TOKENS'
- 'FORBIDDEN_UI_CONTROLS'
- 'FORBIDDEN_RAW_FIELDS_IN_UI'
- 'OFFLIMITS_FILES'
- 'severity'
- 'detail'
- 'pas158_memory_review_readiness_report.json'
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
- 'repo_root'
- 'paths'
- 'Iterable[str]'
- 'prefix'
- 'label_fmt'
- 'List[dict]'
- 'PASS'
- 'FAIL'
- 'src'
- 'Mirror of the test-suite helper. Strips /* ... */, //,\nand string literals (single/double/template) so executable\nJS identifiers are isolated for substring checks.'
- 'dashboard_src'
- 'Extract the PAS148 Memory Review block. The start marker\nsits INSIDE a /* ... */ banner comment; back up to the\npreceding ``/*`` so the JS-comment stripper sees a well-\nformed comment open. Same pattern as the per-phase tests.'
- 'PAS148 — Admin-only Memory Review UI'
- 'PAS148: end of Memory Review admin section'
- 'doc'
- 'Required doc present: {p}'
- 'app'
- 'routes'
- 'admin.py'
- 'admin_routes:source_missing'
- 'app/routes/admin.py is missing'
- 'cannot inspect routes — admin.py not readable'
- 'admin_routes:'
- 'admin route declared: '
- 'none of accepted declarations present: '
- ' | '
- 'static'
- 'dashboard'
- 'index.html'
- 'dashboard_ui:source_missing'
- 'app/static/dashboard/index.html is missing'
- 'cannot inspect dashboard tokens'
- 'dashboard_ui:'
- 'Memory Review UI surface present: '
- 'missing tokens: '
- 'portal.py'
- 'portal_isolation:source_missing'
- 'app/routes/portal.py is missing'
- 'cannot verify tenant-portal isolation'
- 'portal_isolation:no_memory_review_endpoints'
- 'tenant portal carries no Memory Review endpoints / imports'
- 'tokens leaked into portal.py: '
- 'No expire / quarantine buttons, no bulk actions, no\nrollout/apply/manifest controls, no freeform edit affordances\nanywhere in the PAS148 Memory Review section.'
- 'forbidden_ui:section_missing'
- 'PAS148 Memory Review marker block not found'
- 'cannot scope forbidden-token search'
- 'PAS156 — Client-side-only alert bookmarks'
- 'PAS156: end of client-side-only alert bookmarks'
- 'forbidden_ui:'
- 'Memory Review section does not surface '
- 'forbidden token '
- ' found'
- 'type="checkbox"'
- 'forbidden_ui:no_bulk_row_checkboxes'
- 'Memory Review section has no bulk-row checkboxes'
- 'type="checkbox" present outside PAS156 bookmark block'
- "No transcript/evidence/metadata/raw_prompt/memory_content\nin EXECUTABLE Memory Review UI code (banner comments and\ndocstring prose are OK — they're stripped before checking)."
- 'forbidden_raw_field:'
- 'Memory Review executable UI does not reference '
- 'executable JS referenced '
- 'offlimits:'
- 'Off-limits file present (do not modify): '
- 'missing — restore from git history; do not edit'
- 'Self-check: this readiness script must NOT read .env. We\nassert that fact by line-level source-text inspection — only\n*code lines* (not literal-listing comments / tuples) count as\na violation.\n\nImplementation: a line is a violation only if it starts with\n``import``, ``from``, or contains an unbracketed function-\ncall form like ``load_dotenv()`` outside any quote context.\nWe do NOT scan literal-string contents — otherwise this\nhelper would self-trigger on the very tokens it bans.\n'
- 'self_check:source_unreadable'
- 'PAS158 readiness checker could not read its own source'
- 'source-text self-check skipped'
- 'dotenv import'
- 'load_dotenv()'
- 'load_dotenv() call'
- 'direct .env path'
- 'self_check:no_env_read'
- 'PAS158 readiness checker never reads .env'
- 'disqualifying code-line patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- 'doc:'
- '[BLOCK] Required doc missing: '
- ' — author or restore ('
- '[BLOCK] Admin route missing: '
- ' — verify app/routes/admin.py ('
- '[BLOCK] Dashboard surface missing: '
- ' — verify the Memory Review tab markup ('
- 'portal_isolation:'
- '[BLOCK] Tenant portal leak: '
- ' — remove the Memory Review reference from portal.py ('
- '[BLOCK] Forbidden Memory Review control present: '
- '[BLOCK] Forbidden raw-payload reference in UI: '
- '[BLOCK] Off-limits file missing: '
- 'self_check:'
- '] PAS158 self-check failed: '
- ' — '
- 'see report'
- 'phase'
- 'PAS158'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas158_memory_review_readiness_check'
- 'PAS158 — Evaluate Memory Review subsystem readiness. Read-only. Does not touch Supabase, .env, or any tenant data.'
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
- 'Exit 1 unless verdict == READY (default policy is the same).'
- 'report'
- 'None'
- '[PAS158] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS158] operator actions:'
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
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS158 — Memory Review subsystem readiness gate.\n\nDeterministic, non-mutating evaluator for "is the admin Memory\nReview subsystem operator-ready?". Walks the repo, confirms the\nper-phase docs from PAS147 → PAS157 plus the PAS158 runbook /\nchecklist exist, confirms the eight admin endpoints under\n``/admin/memory/`` are declared, confirms the Memory Review tab\nin the dashboard carries every expected control, and confirms\nthat the brokerage portal carries NONE of them and that the\nMemory Review UI carries no forbidden mutation or raw-payload\ntokens. Emits a verdict (READY / NOT_READY) plus a machine-\nreadable ``pas158_memory_review_readiness_report.json``.\n\nThis script never:\n  * modifies files,\n  * calls Supabase,\n  * reads .env / secrets,\n  * includes payload values in the report or summary,\n  * touches the off-limits\n    ``scripts/combined_supabase_migration.sql``.\n\nUsage:\n  python scripts/pas158_memory_review_readiness_check.py\n  python scripts/pas158_memory_review_readiness_check.py --json\n  python scripts/pas158_memory_review_readiness_check.py --summary-only\n  python scripts/pas158_memory_review_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (or READY_WITH_INFO; --strict ignores INFO)\n    1  — NOT_READY\n    2  — bad CLI arguments\n')
               STORE_NAME               1 (__doc__)

  35           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  37           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (argparse)
               STORE_NAME               4 (argparse)

  38           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (json)
               STORE_NAME               5 (json)

  39           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (os)
               STORE_NAME               6 (os)

  40           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (sys)
               STORE_NAME               7 (sys)

  41           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              8 (datetime)
               IMPORT_FROM              8 (datetime)
               STORE_NAME               8 (datetime)
               IMPORT_FROM              9 (timezone)
               STORE_NAME               9 (timezone)
               POP_TOP

  42           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME             10 (pathlib)
               IMPORT_FROM             11 (Path)
               STORE_NAME              11 (Path)
               POP_TOP

  43           LOAD_SMALL_INT           0
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

  48           LOAD_NAME                7 (sys)
               LOAD_ATTR               34 (stdout)
               LOAD_NAME                7 (sys)
               LOAD_ATTR               36 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              19 (_stream)

  49           NOP

  50   L2:     LOAD_NAME               19 (_stream)
               LOAD_ATTR               41 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  48   L4:     END_FOR
               POP_ITER

  55           LOAD_NAME                6 (os)
               LOAD_ATTR               44 (path)
               LOAD_ATTR               47 (abspath + NULL|self)

  56           LOAD_NAME                6 (os)
               LOAD_ATTR               44 (path)
               LOAD_ATTR               49 (join + NULL|self)
               LOAD_NAME                6 (os)
               LOAD_ATTR               44 (path)
               LOAD_ATTR               51 (dirname + NULL|self)
               LOAD_NAME               26 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  55           CALL                     1
               STORE_NAME              27 (_REPO_ROOT_DEFAULT)

  64           LOAD_CONST               9 ('READY')
               STORE_NAME              28 (VERDICT_READY)

  65           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              29 (VERDICT_NOT_READY)

  67           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              30 (SEVERITY_BLOCK)

  68           LOAD_CONST              12 ('INFO')
               STORE_NAME              31 (SEVERITY_INFO)

  75           LOAD_CONST              69 (('docs/pas147_operator_memory_review_console.md', 'docs/pas148_operator_memory_review_ui.md', 'docs/pas149_memory_review_history.md', 'docs/pas150_memory_review_stats.md', 'docs/pas151_memory_review_timeseries.md', 'docs/pas152_memory_review_csv_export.md', 'docs/pas153_memory_review_csv_filters.md', 'docs/pas154_memory_review_actor_catalog.md', 'docs/pas155_memory_review_operator_alerts.md', 'docs/pas156_memory_review_alert_bookmarks.md', 'docs/pas157_memory_review_help_layer.md', 'docs/pas158_memory_review_operations_runbook.md', 'docs/pas158_demo_simulation_checklist.md'))
               STORE_NAME              32 (REQUIRED_PHASE_DOCS)
               LOAD_CONST              13 ('Tuple[str, ...]')
               LOAD_NAME               33 (__annotations__)
               LOAD_CONST              14 ('REQUIRED_PHASE_DOCS')
               STORE_SUBSCR

  96           LOAD_CONST              70 ((('review-queue', ('@router.get("/memory/review-queue")',)), ('review-summary', ('@router.get("/memory/review-summary")',)), ('review-action', ('@router.post("/memory/{memory_id}/review")',)), ('review-history', ('@router.get("/memory/{memory_id}/history")',)), ('review-stats', ('@router.get("/memory/review-stats")',)), ('review-events-csv', ('@router.get("/memory/review-events.csv")',)), ('review-actors', ('@router.get("/memory/review-actors")',)), ('review-alerts', ('@router.get("/memory/review-alerts")',))))
               STORE_NAME              34 (REQUIRED_ADMIN_ROUTES)
               LOAD_CONST              15 ('Tuple[Tuple[str, Tuple[str, ...]], ...]')
               LOAD_NAME               33 (__annotations__)
               LOAD_CONST              16 ('REQUIRED_ADMIN_ROUTES')
               STORE_SUBSCR

 112           LOAD_CONST              71 ((('memory-review-tab', ('aMemoryReviewContent', 'Memory Review')), ('approve-control', ('>Approve<',)), ('reject-control', ('>Reject<',)), ('history-control', ('>View History<',)), ('stats-panel', ('id="memReviewStats"',)), ('timeseries-panel', ('id="memReviewTimeSeries"',)), ('csv-export', ('>Export CSV<', 'memReviewExportCsvBtn')), ('export-filters', ('id="memReviewExportStatus"', 'id="memReviewExportActorType"', 'id="memReviewExportActorId"')), ('actor-catalog', ('id="memReviewActors"', 'id="memReviewActorList"')), ('alert-panel', ('id="memReviewAlerts"',)), ('bookmarks', ('id="memReviewAlertBookmarks"', 'PAS156_ALLOWED_ALERT_TYPES')), ('help-guide', ('id="memReviewHelpGuide"', 'PAS157_ALERT_HELP'))))
               STORE_NAME              35 (REQUIRED_UI_TOKENS)
               LOAD_CONST              15 ('Tuple[Tuple[str, Tuple[str, ...]], ...]')
               LOAD_NAME               33 (__annotations__)
               LOAD_CONST              17 ('REQUIRED_UI_TOKENS')
               STORE_SUBSCR

 136           LOAD_CONST              72 (('/memory/review-queue', '/memory/review-summary', '/memory/review-stats', '/memory/review-actors', '/memory/review-alerts', '/memory/review-events.csv', 'memory_review_events_csv_for_brokerage', 'review_stats_for_brokerage', 'review_actors_for_brokerage', 'review_alerts_for_brokerage', 'summarize_review_actors', 'summarize_review_alerts'))
               STORE_NAME              36 (FORBIDDEN_PORTAL_TOKENS)
               LOAD_CONST              13 ('Tuple[str, ...]')
               LOAD_NAME               33 (__annotations__)
               LOAD_CONST              18 ('FORBIDDEN_PORTAL_TOKENS')
               STORE_SUBSCR

 155           LOAD_CONST              73 (('>Expire<', '>Quarantine<', 'Approve All', 'Reject All', 'bulk_approve', 'bulkApprove', 'bulk_reject', 'bulkReject', 'selectAll', 'select_all', 'Apply Manifest', 'rollback_manifest', 'apply_manifest', '>Apply<', 'rollout_plan', 'Edit Title', 'Edit Summary', 'Save Title', 'Save Summary', 'editTitle', 'updateTitle'))
               STORE_NAME              37 (FORBIDDEN_UI_CONTROLS)
               LOAD_CONST              13 ('Tuple[str, ...]')
               LOAD_NAME               33 (__annotations__)
               LOAD_CONST              19 ('FORBIDDEN_UI_CONTROLS')
               STORE_SUBSCR

 188           LOAD_CONST              74 (('transcript', 'evidence', 'metadata', 'raw_prompt', 'memory_content'))
               STORE_NAME              38 (FORBIDDEN_RAW_FIELDS_IN_UI)
               LOAD_CONST              13 ('Tuple[str, ...]')
               LOAD_NAME               33 (__annotations__)
               LOAD_CONST              20 ('FORBIDDEN_RAW_FIELDS_IN_UI')
               STORE_SUBSCR

 198           LOAD_CONST              75 (('scripts/combined_supabase_migration.sql',))
               STORE_NAME              39 (OFFLIMITS_FILES)
               LOAD_CONST              13 ('Tuple[str, ...]')
               LOAD_NAME               33 (__annotations__)
               LOAD_CONST              21 ('OFFLIMITS_FILES')
               STORE_SUBSCR

 207           LOAD_CONST              22 ('severity')

 212           LOAD_NAME               30 (SEVERITY_BLOCK)

 207           LOAD_CONST              23 ('detail')

 213           LOAD_CONST              24 ('')

 207           BUILD_MAP                2
               LOAD_CONST              25 (<code object __annotate__ at 0x0000018C18025730, file "scripts\pas158_memory_review_readiness_check.py", line 207>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object _check at 0x0000018C17FA3E10, file "scripts\pas158_memory_review_readiness_check.py", line 207>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              40 (_check)

 224           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas158_memory_review_readiness_check.py", line 224>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object _now_iso at 0x0000018C18038B70, file "scripts\pas158_memory_review_readiness_check.py", line 224>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (_now_iso)

 232           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts\pas158_memory_review_readiness_check.py", line 232>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object _read_text at 0x0000018C18053990, file "scripts\pas158_memory_review_readiness_check.py", line 232>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (_read_text)

 239           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C18024F30, file "scripts\pas158_memory_review_readiness_check.py", line 239>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object _check_files at 0x0000018C1794ED80, file "scripts\pas158_memory_review_readiness_check.py", line 239>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_check_files)

 259           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas158_memory_review_readiness_check.py", line 259>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object _strip_js_comments_and_strings at 0x0000018C17ED92F0, file "scripts\pas158_memory_review_readiness_check.py", line 259>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_strip_js_comments_and_strings)

 299           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas158_memory_review_readiness_check.py", line 299>)
               MAKE_FUNCTION
               LOAD_CONST              36 (<code object _pas148_section at 0x0000018C180488F0, file "scripts\pas158_memory_review_readiness_check.py", line 299>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (_pas148_section)

 320           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas158_memory_review_readiness_check.py", line 320>)
               MAKE_FUNCTION
               LOAD_CONST              38 (<code object check_phase_docs at 0x0000018C18026030, file "scripts\pas158_memory_review_readiness_check.py", line 320>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_phase_docs)

 329           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas158_memory_review_readiness_check.py", line 329>)
               MAKE_FUNCTION
               LOAD_CONST              40 (<code object check_admin_routes at 0x0000018C17D7CE20, file "scripts\pas158_memory_review_readiness_check.py", line 329>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_admin_routes)

 356           LOAD_CONST              41 (<code object __annotate__ at 0x0000018C17FA2010, file "scripts\pas158_memory_review_readiness_check.py", line 356>)
               MAKE_FUNCTION
               LOAD_CONST              42 (<code object check_dashboard_ui_tokens at 0x0000018C17D7D0F0, file "scripts\pas158_memory_review_readiness_check.py", line 356>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_dashboard_ui_tokens)

 384           LOAD_CONST              43 (<code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas158_memory_review_readiness_check.py", line 384>)
               MAKE_FUNCTION
               LOAD_CONST              44 (<code object check_portal_isolation at 0x0000018C17CC1F60, file "scripts\pas158_memory_review_readiness_check.py", line 384>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_portal_isolation)

 411           LOAD_CONST              45 (<code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas158_memory_review_readiness_check.py", line 411>)
               MAKE_FUNCTION
               LOAD_CONST              46 (<code object check_forbidden_ui_controls at 0x0000018C17EDA2D0, file "scripts\pas158_memory_review_readiness_check.py", line 411>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_forbidden_ui_controls)

 468           LOAD_CONST              47 (<code object __annotate__ at 0x0000018C17FA25B0, file "scripts\pas158_memory_review_readiness_check.py", line 468>)
               MAKE_FUNCTION
               LOAD_CONST              48 (<code object check_forbidden_raw_fields_in_ui at 0x0000018C17E58540, file "scripts\pas158_memory_review_readiness_check.py", line 468>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_forbidden_raw_fields_in_ui)

 493           LOAD_CONST              49 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pas158_memory_review_readiness_check.py", line 493>)
               MAKE_FUNCTION
               LOAD_CONST              50 (<code object check_offlimits_present at 0x0000018C179C3C30, file "scripts\pas158_memory_review_readiness_check.py", line 493>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_offlimits_present)

 508           LOAD_CONST              51 (<code object __annotate__ at 0x0000018C17FA2D30, file "scripts\pas158_memory_review_readiness_check.py", line 508>)
               MAKE_FUNCTION
               LOAD_CONST              52 (<code object check_no_env_read at 0x0000018C17E57A10, file "scripts\pas158_memory_review_readiness_check.py", line 508>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_no_env_read)

 569           LOAD_CONST              53 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas158_memory_review_readiness_check.py", line 569>)
               MAKE_FUNCTION
               LOAD_CONST              54 (<code object _aggregate at 0x0000018C17EC4F40, file "scripts\pas158_memory_review_readiness_check.py", line 569>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (_aggregate)

 582           LOAD_CONST              55 (<code object __annotate__ at 0x0000018C17FA2C40, file "scripts\pas158_memory_review_readiness_check.py", line 582>)
               MAKE_FUNCTION
               LOAD_CONST              56 (<code object _operator_actions at 0x0000018C181A3890, file "scripts\pas158_memory_review_readiness_check.py", line 582>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (_operator_actions)

 635           LOAD_CONST              57 (<code object __annotate__ at 0x0000018C17FA3690, file "scripts\pas158_memory_review_readiness_check.py", line 635>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object evaluate at 0x0000018C17F83F30, file "scripts\pas158_memory_review_readiness_check.py", line 635>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (evaluate)

 667           LOAD_CONST              59 ('pas158_memory_review_readiness_report.json')
               STORE_NAME              57 (REPORT_FILENAME)

 670           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C17FA3870, file "scripts\pas158_memory_review_readiness_check.py", line 670>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object _build_parser at 0x0000018C1801C7F0, file "scripts\pas158_memory_review_readiness_check.py", line 670>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (_build_parser)

 707           LOAD_CONST              62 (<code object __annotate__ at 0x0000018C17FA3000, file "scripts\pas158_memory_review_readiness_check.py", line 707>)
               MAKE_FUNCTION
               LOAD_CONST              63 (<code object _print_summary at 0x0000018C17D8E300, file "scripts\pas158_memory_review_readiness_check.py", line 707>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (_print_summary)

 725           LOAD_CONST              64 (<code object __annotate__ at 0x0000018C18024930, file "scripts\pas158_memory_review_readiness_check.py", line 725>)
               MAKE_FUNCTION
               LOAD_CONST              65 (<code object _write_report at 0x0000018C18104030, file "scripts\pas158_memory_review_readiness_check.py", line 725>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (_write_report)

 739           LOAD_CONST              76 ((None,))
               LOAD_CONST              66 (<code object __annotate__ at 0x0000018C180FC210, file "scripts\pas158_memory_review_readiness_check.py", line 739>)
               MAKE_FUNCTION
               LOAD_CONST              67 (<code object main at 0x0000018C17F842E0, file "scripts\pas158_memory_review_readiness_check.py", line 739>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              61 (main)

 768           LOAD_NAME               62 (__name__)
               LOAD_CONST              68 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 769           LOAD_NAME                7 (sys)
               LOAD_ATTR              126 (exit)
               PUSH_NULL
               LOAD_NAME               61 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 768   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  51           LOAD_NAME               21 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  52   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          342 (to L1)

  51   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "scripts\pas158_memory_review_readiness_check.py", line 207>:
207           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

208           LOAD_CONST               2 ('str')

207           LOAD_CONST               3 ('status')

209           LOAD_CONST               2 ('str')

207           LOAD_CONST               4 ('label')

210           LOAD_CONST               2 ('str')

207           LOAD_CONST               5 ('severity')

212           LOAD_CONST               2 ('str')

207           LOAD_CONST               6 ('detail')

213           LOAD_CONST               2 ('str')

207           LOAD_CONST               7 ('return')

214           LOAD_CONST               8 ('dict')

207           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA3E10, file "scripts\pas158_memory_review_readiness_check.py", line 207>:
207           RESUME                   0

216           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

217           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

218           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

219           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

220           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

215           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas158_memory_review_readiness_check.py", line 224>:
224           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038B70, file "scripts\pas158_memory_review_readiness_check.py", line 224>:
224           RESUME                   0

225           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts\pas158_memory_review_readiness_check.py", line 232>:
232           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053990, file "scripts\pas158_memory_review_readiness_check.py", line 232>:
 232           RESUME                   0

 233           NOP

 234   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 235           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 236   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 235   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024F30, file "scripts\pas158_memory_review_readiness_check.py", line 239>:
239           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')

240           LOAD_CONST               2 ('str')

239           LOAD_CONST               3 ('paths')

241           LOAD_CONST               4 ('Iterable[str]')

239           LOAD_CONST               5 ('prefix')

242           LOAD_CONST               2 ('str')

239           LOAD_CONST               6 ('label_fmt')

243           LOAD_CONST               2 ('str')

239           LOAD_CONST               7 ('return')

244           LOAD_CONST               8 ('List[dict]')

239           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _check_files at 0x0000018C1794ED80, file "scripts\pas158_memory_review_readiness_check.py", line 239>:
239           RESUME                   0

245           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              STORE_FAST               4 (root)

246           BUILD_LIST               0
              STORE_FAST               5 (out)

247           LOAD_FAST_BORROW         1 (paths)
              GET_ITER
      L1:     FOR_ITER               101 (to L6)
              STORE_FAST               6 (p)

248           LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (root, p)
              BINARY_OP               11 (/)
              LOAD_ATTR                3 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               7 (ok)

249           LOAD_FAST                5 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

250           LOAD_FAST_BORROW         2 (prefix)
              FORMAT_SIMPLE
              LOAD_CONST               0 (':')
              LOAD_FAST_BORROW         6 (p)
              FORMAT_SIMPLE
              BUILD_STRING             3

251           LOAD_FAST_BORROW         7 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

252   L3:     LOAD_FAST_BORROW         3 (label_fmt)
              LOAD_ATTR                9 (format + NULL|self)
              LOAD_FAST_BORROW         6 (p)
              LOAD_CONST               3 (('p',))
              CALL_KW                  1

253           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

254           LOAD_FAST_BORROW         7 (ok)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              LOAD_FAST                6 (p)
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               4 ('')

249   L5:     LOAD_CONST               5 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          103 (to L1)

247   L6:     END_FOR
              POP_ITER

256           LOAD_FAST_BORROW         5 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas158_memory_review_readiness_check.py", line 259>:
259           RESUME                   0
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

Disassembly of <code object _strip_js_comments_and_strings at 0x0000018C17ED92F0, file "scripts\pas158_memory_review_readiness_check.py", line 259>:
259            RESUME                   0

263            BUILD_LIST               0
               STORE_FAST               1 (out)

264            LOAD_SMALL_INT           0
               STORE_FAST               2 (i)

265            LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST               3 (n)

266    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      307 (to L12)
               NOT_TAKEN

267            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

268            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('/')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       79 (to L3)
               NOT_TAKEN
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               LOAD_FAST_BORROW         3 (n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       65 (to L3)
               NOT_TAKEN
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               BINARY_OP               26 ([])
               LOAD_CONST               2 ('*')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       45 (to L3)
               NOT_TAKEN

269            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               3 ('*/')
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           2
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               5 (end)

270            LOAD_FAST_BORROW         5 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

271            JUMP_FORWARD           224 (to L12)

272    L2:     LOAD_FAST_BORROW         5 (end)
               LOAD_SMALL_INT           2
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

273            JUMP_BACKWARD          100 (to L1)

274    L3:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('/')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       72 (to L5)
               NOT_TAKEN
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               LOAD_FAST_BORROW         3 (n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       58 (to L5)
               NOT_TAKEN
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               BINARY_OP               26 ([])
               LOAD_CONST               1 ('/')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L5)
               NOT_TAKEN

275            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               4 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               6 (j)

276            LOAD_FAST_BORROW         6 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L4)
               NOT_TAKEN

277            JUMP_FORWARD           146 (to L12)

278    L4:     LOAD_FAST_BORROW         6 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

279            JUMP_BACKWARD          178 (to L1)

280    L5:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               8 (('"', "'", '`'))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE      100 (to L11)
               NOT_TAKEN

281            LOAD_FAST                4 (ch)
               STORE_FAST               7 (quote)

282            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               6 (j)

283    L6:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 99 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       71 (to L10)
               NOT_TAKEN

284            LOAD_FAST_BORROW_LOAD_FAST_BORROW 6 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               6 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L7)
               NOT_TAKEN

285            LOAD_FAST_BORROW         6 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               6 (j)

286            JUMP_BACKWARD           30 (to L6)

287    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 6 (src, j)
               BINARY_OP               26 ([])
               LOAD_FAST_BORROW         7 (quote)
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        2 (to L8)
               NOT_TAKEN

288            JUMP_FORWARD            32 (to L10)

289    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 6 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               4 ('\n')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        9 (to L9)
               NOT_TAKEN
               LOAD_FAST_BORROW         7 (quote)
               LOAD_CONST               5 ('`')
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE        2 (to L9)
               NOT_TAKEN

290            JUMP_FORWARD            11 (to L10)

291    L9:     LOAD_FAST_BORROW         6 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               6 (j)
               JUMP_BACKWARD           76 (to L6)

292   L10:     LOAD_FAST_BORROW         6 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

293            EXTENDED_ARG             1
               JUMP_BACKWARD          284 (to L1)

294   L11:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

295            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          313 (to L1)

296   L12:     LOAD_CONST               7 ('')
               LOAD_ATTR                7 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas158_memory_review_readiness_check.py", line 299>:
299           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('dashboard_src')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _pas148_section at 0x0000018C180488F0, file "scripts\pas158_memory_review_readiness_check.py", line 299>:
299           RESUME                   0

304           LOAD_CONST               1 ('PAS148 — Admin-only Memory Review UI')
              STORE_FAST               1 (start_marker)

305           LOAD_CONST               2 ('PAS148: end of Memory Review admin section')
              STORE_FAST               2 (end_marker)

306           LOAD_FAST_BORROW         0 (dashboard_src)
              LOAD_ATTR                1 (find + NULL|self)
              LOAD_FAST_BORROW         1 (start_marker)
              CALL                     1
              STORE_FAST               3 (start)

307           LOAD_FAST                0 (dashboard_src)
              LOAD_ATTR                1 (find + NULL|self)
              LOAD_FAST_LOAD_FAST     35 (end_marker, start)
              LOAD_SMALL_INT           0
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_FALSE       10 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         3 (start)
              LOAD_SMALL_INT           1
              BINARY_OP                0 (+)
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_SMALL_INT           0
      L2:     CALL                     2
              STORE_FAST               4 (end)

308           LOAD_FAST_BORROW         3 (start)
              LOAD_SMALL_INT           0
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_TRUE         7 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (end, start)
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN

309   L3:     LOAD_CONST               3 (None)
              RETURN_VALUE

310   L4:     LOAD_FAST_BORROW         0 (dashboard_src)
              LOAD_ATTR                3 (rfind + NULL|self)
              LOAD_CONST               4 ('/*')
              LOAD_SMALL_INT           0
              LOAD_FAST_BORROW         3 (start)
              CALL                     3
              STORE_FAST               5 (block_open)

311           LOAD_FAST_BORROW         5 (block_open)
              LOAD_SMALL_INT           0
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN

312           LOAD_FAST                5 (block_open)
              STORE_FAST               3 (start)

313   L5:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 3 (dashboard_src, start)
              LOAD_FAST_BORROW         4 (end)
              LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         2 (end_marker)
              CALL                     1
              BINARY_OP                0 (+)
              BINARY_SLICE
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas158_memory_review_readiness_check.py", line 320>:
320           RESUME                   0
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

Disassembly of <code object check_phase_docs at 0x0000018C18026030, file "scripts\pas158_memory_review_readiness_check.py", line 320>:
320           RESUME                   0

321           LOAD_GLOBAL              1 (_check_files + NULL)

322           LOAD_FAST_BORROW         0 (repo_root)

323           LOAD_GLOBAL              2 (REQUIRED_PHASE_DOCS)

324           LOAD_CONST               0 ('doc')

325           LOAD_CONST               1 ('Required doc present: {p}')

321           LOAD_CONST               2 (('prefix', 'label_fmt'))
              CALL_KW                  4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas158_memory_review_readiness_check.py", line 329>:
329           RESUME                   0
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

Disassembly of <code object check_admin_routes at 0x0000018C17D7CE20, file "scripts\pas158_memory_review_readiness_check.py", line 329>:
  --            MAKE_CELL                6 (src)

 329            RESUME                   0

 330            BUILD_LIST               0
                STORE_FAST               1 (out)

 331            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('app')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('routes')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('admin.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (admin_path)

 332            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (admin_path)
                CALL                     1
                STORE_DEREF              6 (src)

 333            LOAD_DEREF               6 (src)
                POP_JUMP_IF_NOT_NONE    38 (to L1)
                NOT_TAKEN

 334            LOAD_FAST_BORROW         1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 335            LOAD_CONST               3 ('admin_routes:source_missing')

 336            LOAD_CONST               4 ('FAIL')

 337            LOAD_CONST               5 ('app/routes/admin.py is missing')

 338            LOAD_GLOBAL              8 (SEVERITY_BLOCK)

 339            LOAD_CONST               6 ('cannot inspect routes — admin.py not readable')

 334            LOAD_CONST               7 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 341            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 342    L1:     LOAD_GLOBAL             10 (REQUIRED_ADMIN_ROUTES)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   52 (logical, decls)

 343            LOAD_GLOBAL             12 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         6 (src)
                BUILD_TUPLE              1
                LOAD_CONST               8 (<code object <genexpr> at 0x0000018C18025F30, file "scripts\pas158_memory_review_readiness_check.py", line 343>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         4 (decls)
                GET_ITER
                CALL                     0
        L3:     FOR_ITER                12 (to L5)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L3)
        L4:     POP_ITER
                LOAD_CONST               9 (True)
                JUMP_FORWARD            20 (to L7)
        L5:     END_FOR
                POP_ITER
                LOAD_CONST              10 (False)
                JUMP_FORWARD            16 (to L7)
        L6:     PUSH_NULL
                LOAD_FAST_BORROW         6 (src)
                BUILD_TUPLE              1
                LOAD_CONST               8 (<code object <genexpr> at 0x0000018C18025F30, file "scripts\pas158_memory_review_readiness_check.py", line 343>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         4 (decls)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               5 (found)

 344            LOAD_FAST                1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 345            LOAD_CONST              11 ('admin_routes:')
                LOAD_FAST_BORROW         3 (logical)
                FORMAT_SIMPLE
                BUILD_STRING             2

 346            LOAD_FAST_BORROW         5 (found)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST              12 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               4 ('FAIL')

 347    L9:     LOAD_CONST              13 ('admin route declared: ')
                LOAD_FAST_BORROW         3 (logical)
                FORMAT_SIMPLE
                BUILD_STRING             2

 348            LOAD_GLOBAL              8 (SEVERITY_BLOCK)

 349            LOAD_FAST_BORROW         5 (found)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_CONST              14 ('')
                JUMP_FORWARD            23 (to L11)

 350   L10:     LOAD_CONST              15 ('none of accepted declarations present: ')
                LOAD_CONST              16 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         4 (decls)
                CALL                     1
                BINARY_OP                0 (+)

 344   L11:     LOAD_CONST               7 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 342   L12:     END_FOR
                POP_ITER

 353            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025F30, file "scripts\pas158_memory_review_readiness_check.py", line 343>:
  --           COPY_FREE_VARS           1

 343           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (d, d)
               LOAD_DEREF               2 (src)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "scripts\pas158_memory_review_readiness_check.py", line 356>:
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

Disassembly of <code object check_dashboard_ui_tokens at 0x0000018C17D7D0F0, file "scripts\pas158_memory_review_readiness_check.py", line 356>:
 356            RESUME                   0

 357            BUILD_LIST               0
                STORE_FAST               1 (out)

 358            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('app')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('static')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('dashboard')
                BINARY_OP               11 (/)
                LOAD_CONST               3 ('index.html')
                BINARY_OP               11 (/)
                STORE_FAST               2 (dashboard_path)

 359            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (dashboard_path)
                CALL                     1
                STORE_FAST               3 (src)

 360            LOAD_FAST_BORROW         3 (src)
                POP_JUMP_IF_NOT_NONE    38 (to L1)
                NOT_TAKEN

 361            LOAD_FAST_BORROW         1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 362            LOAD_CONST               4 ('dashboard_ui:source_missing')

 363            LOAD_CONST               5 ('FAIL')

 364            LOAD_CONST               6 ('app/static/dashboard/index.html is missing')

 365            LOAD_GLOBAL              8 (SEVERITY_BLOCK)

 366            LOAD_CONST               7 ('cannot inspect dashboard tokens')

 361            LOAD_CONST               8 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 368            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 369    L1:     LOAD_GLOBAL             10 (REQUIRED_UI_TOKENS)
                GET_ITER
        L2:     FOR_ITER               120 (to L13)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   69 (logical, tokens)

 370            LOAD_FAST_BORROW         5 (tokens)
                GET_ITER
                LOAD_FAST_AND_CLEAR      6 (t)
                SWAP                     2
        L3:     BUILD_LIST               0
                SWAP                     2
        L4:     FOR_ITER                13 (to L7)
                STORE_FAST_LOAD_FAST   102 (t, t)
                LOAD_FAST_BORROW         3 (src)
                CONTAINS_OP              1 (not in)
        L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L4)
        L6:     LOAD_FAST_BORROW         6 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L4)
        L7:     END_FOR
                POP_ITER
        L8:     STORE_FAST               7 (missing)
                STORE_FAST               6 (t)

 371            LOAD_FAST_BORROW         7 (missing)
                TO_BOOL
                UNARY_NOT
                STORE_FAST               8 (ok)

 372            LOAD_FAST                1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 373            LOAD_CONST               9 ('dashboard_ui:')
                LOAD_FAST_BORROW         4 (logical)
                FORMAT_SIMPLE
                BUILD_STRING             2

 374            LOAD_FAST_BORROW         8 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST              10 ('PASS')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               5 ('FAIL')

 375   L10:     LOAD_CONST              11 ('Memory Review UI surface present: ')
                LOAD_FAST_BORROW         4 (logical)
                FORMAT_SIMPLE
                BUILD_STRING             2

 376            LOAD_GLOBAL              8 (SEVERITY_BLOCK)

 377            LOAD_FAST_BORROW         8 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN
                LOAD_CONST              12 ('')
                JUMP_FORWARD            23 (to L12)

 378   L11:     LOAD_CONST              13 ('missing tokens: ')
                LOAD_CONST              14 (', ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         7 (missing)
                CALL                     1
                BINARY_OP                0 (+)

 372   L12:     LOAD_CONST               8 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          122 (to L2)

 369   L13:     END_FOR
                POP_ITER

 381            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L14:     SWAP                     2
                POP_TOP

 370            SWAP                     2
                STORE_FAST               6 (t)
                RERAISE                  0
ExceptionTable:
  L3 to L5 -> L14 [3]
  L6 to L8 -> L14 [3]

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas158_memory_review_readiness_check.py", line 384>:
384           RESUME                   0
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

Disassembly of <code object check_portal_isolation at 0x0000018C17CC1F60, file "scripts\pas158_memory_review_readiness_check.py", line 384>:
 384            RESUME                   0

 385            BUILD_LIST               0
                STORE_FAST               1 (out)

 386            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('app')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('routes')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('portal.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (portal_path)

 387            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (portal_path)
                CALL                     1
                STORE_FAST               3 (src)

 388            LOAD_FAST_BORROW         3 (src)
                POP_JUMP_IF_NOT_NONE    38 (to L1)
                NOT_TAKEN

 389            LOAD_FAST_BORROW         1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 390            LOAD_CONST               3 ('portal_isolation:source_missing')

 391            LOAD_CONST               4 ('FAIL')

 392            LOAD_CONST               5 ('app/routes/portal.py is missing')

 393            LOAD_GLOBAL              8 (SEVERITY_BLOCK)

 394            LOAD_CONST               6 ('cannot verify tenant-portal isolation')

 389            LOAD_CONST               7 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 396            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 397    L1:     LOAD_GLOBAL             10 (FORBIDDEN_PORTAL_TOKENS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      4 (t)
                SWAP                     2
        L2:     BUILD_LIST               0
                SWAP                     2
        L3:     FOR_ITER                13 (to L6)
                STORE_FAST_LOAD_FAST    68 (t, t)
                LOAD_FAST_BORROW         3 (src)
                CONTAINS_OP              0 (in)
        L4:     POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L3)
        L5:     LOAD_FAST_BORROW         4 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L3)
        L6:     END_FOR
                POP_ITER
        L7:     STORE_FAST               5 (found)
                STORE_FAST               4 (t)

 398            LOAD_FAST_BORROW         5 (found)
                TO_BOOL
                UNARY_NOT
                STORE_FAST               6 (ok)

 399            LOAD_FAST                1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 400            LOAD_CONST               8 ('portal_isolation:no_memory_review_endpoints')

 401            LOAD_FAST_BORROW         6 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               9 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               4 ('FAIL')

 402    L9:     LOAD_CONST              10 ('tenant portal carries no Memory Review endpoints / imports')

 403            LOAD_GLOBAL              8 (SEVERITY_BLOCK)

 404            LOAD_FAST_BORROW         6 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_CONST              11 ('')
                JUMP_FORWARD            23 (to L11)

 405   L10:     LOAD_CONST              12 ('tokens leaked into portal.py: ')
                LOAD_CONST              13 (', ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         5 (found)
                CALL                     1
                BINARY_OP                0 (+)

 399   L11:     LOAD_CONST               7 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 408            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L12:     SWAP                     2
                POP_TOP

 397            SWAP                     2
                STORE_FAST               4 (t)
                RERAISE                  0
ExceptionTable:
  L2 to L4 -> L12 [2]
  L5 to L7 -> L12 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas158_memory_review_readiness_check.py", line 411>:
411           RESUME                   0
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

Disassembly of <code object check_forbidden_ui_controls at 0x0000018C17EDA2D0, file "scripts\pas158_memory_review_readiness_check.py", line 411>:
411            RESUME                   0

415            BUILD_LIST               0
               STORE_FAST               1 (out)

416            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               1 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('static')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('dashboard')
               BINARY_OP               11 (/)
               LOAD_CONST               4 ('index.html')
               BINARY_OP               11 (/)
               STORE_FAST               2 (dashboard_path)

417            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (dashboard_path)
               CALL                     1
               STORE_FAST               3 (src)

418            LOAD_FAST_BORROW         3 (src)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

421            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

422    L1:     LOAD_GLOBAL              5 (_pas148_section + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (section)

423            LOAD_FAST_BORROW         4 (section)
               POP_JUMP_IF_NOT_NONE    38 (to L2)
               NOT_TAKEN

424            LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

425            LOAD_CONST               6 ('forbidden_ui:section_missing')

426            LOAD_CONST               7 ('FAIL')

427            LOAD_CONST               8 ('PAS148 Memory Review marker block not found')

428            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

429            LOAD_CONST               9 ('cannot scope forbidden-token search')

424            LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

431            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

437    L2:     LOAD_FAST_BORROW         4 (section)
               LOAD_ATTR               13 (find + NULL|self)
               LOAD_CONST              11 ('PAS156 — Client-side-only alert bookmarks')
               CALL                     1
               STORE_FAST               5 (m_start)

438            LOAD_FAST_BORROW         4 (section)
               LOAD_ATTR               13 (find + NULL|self)
               LOAD_CONST              12 ('PAS156: end of client-side-only alert bookmarks')
               CALL                     1
               STORE_FAST               6 (m_end)

439            LOAD_FAST_BORROW         5 (m_start)
               LOAD_SMALL_INT           0
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       78 (to L3)
               NOT_TAKEN
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 101 (m_end, m_start)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE       72 (to L3)
               NOT_TAKEN

440            LOAD_FAST_BORROW         4 (section)
               LOAD_ATTR               15 (rfind + NULL|self)
               LOAD_CONST              13 ('/*')
               LOAD_SMALL_INT           0
               LOAD_FAST_BORROW         5 (m_start)
               CALL                     3
               STORE_FAST               7 (block_open)

441            LOAD_FAST_BORROW         4 (section)
               LOAD_ATTR               13 (find + NULL|self)
               LOAD_CONST              14 ('*/')
               LOAD_FAST_BORROW         6 (m_end)
               CALL                     2
               STORE_FAST               8 (block_close)

442            LOAD_FAST_BORROW         7 (block_open)
               LOAD_SMALL_INT           0
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       28 (to L3)
               NOT_TAKEN
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (block_close, m_end)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE       22 (to L3)
               NOT_TAKEN

443            LOAD_FAST_BORROW         4 (section)
               LOAD_CONST               5 (None)
               LOAD_FAST_BORROW         7 (block_open)
               BINARY_SLICE
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 72 (section, block_close)
               LOAD_SMALL_INT           2
               BINARY_OP                0 (+)
               LOAD_CONST               5 (None)
               BINARY_SLICE
               BINARY_OP                0 (+)
               STORE_FAST               4 (section)

445    L3:     LOAD_GLOBAL             16 (FORBIDDEN_UI_CONTROLS)
               GET_ITER
       L4:     FOR_ITER                74 (to L9)
               STORE_FAST               9 (tok)

446            LOAD_FAST_BORROW_LOAD_FAST_BORROW 148 (tok, section)
               CONTAINS_OP              0 (in)
               STORE_FAST              10 (present)

447            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

448            LOAD_CONST              15 ('forbidden_ui:')
               LOAD_FAST_BORROW         9 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

449            LOAD_FAST_BORROW        10 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               7 ('FAIL')
               JUMP_FORWARD             1 (to L6)
       L5:     LOAD_CONST              16 ('PASS')

450    L6:     LOAD_CONST              17 ('Memory Review section does not surface ')
               LOAD_FAST_BORROW         9 (tok)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2

451            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

452            LOAD_FAST_BORROW        10 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        8 (to L7)
               NOT_TAKEN
               LOAD_CONST              18 ('forbidden token ')
               LOAD_FAST_BORROW         9 (tok)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               LOAD_CONST              19 (' found')
               BUILD_STRING             3
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST              20 ('')

447    L8:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           76 (to L4)

445    L9:     END_FOR
               POP_ITER

456            LOAD_CONST              21 ('type="checkbox"')
               LOAD_FAST_BORROW         4 (section)
               CONTAINS_OP              0 (in)
               STORE_FAST              11 (bulk_checkbox)

457            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

458            LOAD_CONST              22 ('forbidden_ui:no_bulk_row_checkboxes')

459            LOAD_FAST_BORROW        11 (bulk_checkbox)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               7 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              16 ('PASS')

460   L11:     LOAD_CONST              23 ('Memory Review section has no bulk-row checkboxes')

461            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

463            LOAD_FAST_BORROW        11 (bulk_checkbox)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN

462            LOAD_CONST              24 ('type="checkbox" present outside PAS156 bookmark block')
               JUMP_FORWARD             1 (to L13)

463   L12:     LOAD_CONST              20 ('')

457   L13:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

465            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "scripts\pas158_memory_review_readiness_check.py", line 468>:
468           RESUME                   0
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

Disassembly of <code object check_forbidden_raw_fields_in_ui at 0x0000018C17E58540, file "scripts\pas158_memory_review_readiness_check.py", line 468>:
468           RESUME                   0

472           BUILD_LIST               0
              STORE_FAST               1 (out)

473           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               1 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('static')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('dashboard')
              BINARY_OP               11 (/)
              LOAD_CONST               4 ('index.html')
              BINARY_OP               11 (/)
              STORE_FAST               2 (dashboard_path)

474           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (dashboard_path)
              CALL                     1
              STORE_FAST               3 (src)

475           LOAD_FAST_BORROW         3 (src)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

476           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

477   L1:     LOAD_GLOBAL              5 (_pas148_section + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (section)

478           LOAD_FAST_BORROW         4 (section)
              POP_JUMP_IF_NOT_NONE     3 (to L2)
              NOT_TAKEN

479           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

480   L2:     LOAD_GLOBAL              7 (_strip_js_comments_and_strings + NULL)
              LOAD_FAST_BORROW         4 (section)
              CALL                     1
              STORE_FAST               5 (executable)

481           LOAD_GLOBAL              8 (FORBIDDEN_RAW_FIELDS_IN_UI)
              GET_ITER
      L3:     FOR_ITER                73 (to L8)
              STORE_FAST               6 (field)

482           LOAD_FAST_BORROW_LOAD_FAST_BORROW 101 (field, executable)
              CONTAINS_OP              0 (in)
              STORE_FAST               7 (present)

483           LOAD_FAST                1 (out)
              LOAD_ATTR               11 (append + NULL|self)
              LOAD_GLOBAL             13 (_check + NULL)

484           LOAD_CONST               5 ('forbidden_raw_field:')
              LOAD_FAST_BORROW         6 (field)
              FORMAT_SIMPLE
              BUILD_STRING             2

485           LOAD_FAST_BORROW         7 (present)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               6 ('FAIL')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               7 ('PASS')

486   L5:     LOAD_CONST               8 ('Memory Review executable UI does not reference ')
              LOAD_FAST_BORROW         6 (field)
              CONVERT_VALUE            2 (repr)
              FORMAT_SIMPLE
              BUILD_STRING             2

487           LOAD_GLOBAL             14 (SEVERITY_BLOCK)

488           LOAD_FAST_BORROW         7 (present)
              TO_BOOL
              POP_JUMP_IF_FALSE        7 (to L6)
              NOT_TAKEN
              LOAD_CONST               9 ('executable JS referenced ')
              LOAD_FAST_BORROW         6 (field)
              CONVERT_VALUE            2 (repr)
              FORMAT_SIMPLE
              BUILD_STRING             2
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST              10 ('')

483   L7:     LOAD_CONST              11 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L3)

481   L8:     END_FOR
              POP_ITER

490           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pas158_memory_review_readiness_check.py", line 493>:
493           RESUME                   0
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

Disassembly of <code object check_offlimits_present at 0x0000018C179C3C30, file "scripts\pas158_memory_review_readiness_check.py", line 493>:
 493           RESUME                   0

 504           LOAD_GLOBAL              0 (OFFLIMITS_FILES)
               GET_ITER

 494           LOAD_FAST_AND_CLEAR      1 (p)
               SWAP                     2
       L1:     BUILD_LIST               0
               SWAP                     2

 504   L2:     FOR_ITER               109 (to L7)
               STORE_FAST               1 (p)

 495           LOAD_GLOBAL              3 (_check + NULL)

 496           LOAD_CONST               0 ('offlimits:')
               LOAD_FAST_BORROW         1 (p)
               FORMAT_SIMPLE
               BUILD_STRING             2

 497           LOAD_GLOBAL              5 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         1 (p)
               BINARY_OP               11 (/)
               LOAD_ATTR                7 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               1 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               2 ('FAIL')

 498   L4:     LOAD_CONST               3 ('Off-limits file present (do not modify): ')
               LOAD_FAST_BORROW         1 (p)
               FORMAT_SIMPLE
               BUILD_STRING             2

 499           LOAD_GLOBAL              8 (SEVERITY_BLOCK)

 500           LOAD_GLOBAL              5 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         1 (p)
               BINARY_OP               11 (/)
               LOAD_ATTR                7 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L6)

 501   L5:     LOAD_CONST               5 ('missing — restore from git history; do not edit')

 495   L6:     LOAD_CONST               6 (('severity', 'detail'))
               CALL_KW                  5
               LIST_APPEND              2
               JUMP_BACKWARD          111 (to L2)

 504   L7:     END_FOR
               POP_ITER

 494   L8:     SWAP                     2
               STORE_FAST               1 (p)
               RETURN_VALUE

  --   L9:     SWAP                     2
               POP_TOP

 494           SWAP                     2
               STORE_FAST               1 (p)
               RERAISE                  0
ExceptionTable:
  L1 to L8 -> L9 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "scripts\pas158_memory_review_readiness_check.py", line 508>:
508           RESUME                   0
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

Disassembly of <code object check_no_env_read at 0x0000018C17E57A10, file "scripts\pas158_memory_review_readiness_check.py", line 508>:
508            RESUME                   0

520            BUILD_LIST               0
               STORE_FAST               1 (out)

521            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

522            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               STORE_FAST               3 (src)

523            LOAD_FAST_BORROW         3 (src)
               POP_JUMP_IF_NOT_NONE    38 (to L1)
               NOT_TAKEN

524            LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

525            LOAD_CONST               1 ('self_check:source_unreadable')

526            LOAD_CONST               2 ('FAIL')

527            LOAD_CONST               3 ('PAS158 readiness checker could not read its own source')

528            LOAD_GLOBAL             12 (SEVERITY_INFO)

529            LOAD_CONST               4 ('source-text self-check skipped')

524            LOAD_CONST               5 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

531            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

533    L1:     BUILD_LIST               0
               STORE_FAST               4 (bad)

534            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR               15 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               189 (to L8)
               STORE_FAST               5 (raw_line)

535            LOAD_FAST_BORROW         5 (raw_line)
               LOAD_ATTR               17 (strip + NULL|self)
               CALL                     0
               STORE_FAST               6 (stripped)

539            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               19 (startswith + NULL|self)
               LOAD_CONST               6 ('#')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

540            JUMP_BACKWARD           44 (to L2)

542    L3:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               19 (startswith + NULL|self)
               LOAD_CONST              17 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

543            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST               7 ('dotenv import')
               CALL                     1
               POP_TOP

547    L4:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               19 (startswith + NULL|self)
               LOAD_CONST               8 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        24 (to L5)
               NOT_TAKEN

548            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               21 (endswith + NULL|self)
               LOAD_CONST               8 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

549    L5:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST               9 ('load_dotenv() call')
               CALL                     1
               POP_TOP

551    L6:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               19 (startswith + NULL|self)
               LOAD_CONST              18 (('.env', "Path('.env')", 'Path(".env")'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L7)
               NOT_TAKEN
               JUMP_BACKWARD          172 (to L2)

552    L7:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              10 ('direct .env path')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          191 (to L2)

534    L8:     END_FOR
               POP_ITER

554            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

555            LOAD_CONST              11 ('self_check:no_env_read')

556            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               2 ('FAIL')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST              12 ('PASS')

557   L10:     LOAD_CONST              13 ('PAS158 readiness checker never reads .env')

558            LOAD_GLOBAL             22 (SEVERITY_BLOCK)

560            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L11)
               NOT_TAKEN

559            LOAD_CONST              14 ('disqualifying code-line patterns: ')
               LOAD_CONST              15 (', ')
               LOAD_ATTR               25 (join + NULL|self)
               LOAD_FAST_BORROW         4 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L12)

560   L11:     LOAD_CONST              16 ('')

554   L12:     LOAD_CONST               5 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

562            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas158_memory_review_readiness_check.py", line 569>:
569           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17EC4F40, file "scripts\pas158_memory_review_readiness_check.py", line 569>:
 569            RESUME                   0

 571            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 570            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 571    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 572            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 571    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 572    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 571    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 570    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 575            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 574            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 575   L10:     FOR_ITER                49 (to L15)
                STORE_FAST               1 (c)

 576            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 575   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L10)

 576   L12:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_INFO)
                COMPARE_OP              88 (bool(==))

 575   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L10)
       L14:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L10)
       L15:     END_FOR
                POP_ITER

 574   L16:     STORE_FAST               3 (info)
                STORE_FAST               1 (c)

 578            LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L18)
       L17:     LOAD_GLOBAL              8 (VERDICT_READY)
       L18:     STORE_FAST               4 (verdict)

 579            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         4 (verdict)
                LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)
                LOAD_CONST               5 ('info')
                LOAD_FAST_BORROW         3 (info)
                BUILD_MAP                3
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 570            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 574            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L5 -> L19 [2]
  L6 to L8 -> L19 [2]
  L9 to L11 -> L20 [2]
  L12 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "scripts\pas158_memory_review_readiness_check.py", line 582>:
582           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C181A3890, file "scripts\pas158_memory_review_readiness_check.py", line 582>:
582            RESUME                   0

583            BUILD_LIST               0
               STORE_FAST               1 (actions)

584            LOAD_FAST_BORROW         0 (checks)
               GET_ITER
       L1:     EXTENDED_ARG             2
               FOR_ITER               524 (to L14)
               STORE_FAST               2 (c)

585            LOAD_FAST_BORROW         2 (c)
               LOAD_CONST               0 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST               1 ('FAIL')
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN

586            JUMP_BACKWARD           20 (to L1)

587    L2:     LOAD_FAST_BORROW         2 (c)
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

588            LOAD_FAST_BORROW         2 (c)
               LOAD_CONST               3 ('id')
               BINARY_OP               26 ([])
               STORE_FAST               4 (cid)

589            LOAD_FAST_BORROW         2 (c)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               4 ('detail')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               5 ('')
       L4:     STORE_FAST               5 (detail)

590            LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST               6 ('doc:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       27 (to L5)
               NOT_TAKEN

591            LOAD_FAST_BORROW         1 (actions)
               LOAD_ATTR                7 (append + NULL|self)

592            LOAD_CONST               7 ('[BLOCK] Required doc missing: ')
               LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST               8 (' — author or restore (')

593            LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')

592            BUILD_STRING             5

591            CALL                     1
               POP_TOP
               JUMP_BACKWARD          136 (to L1)

595    L5:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              10 ('admin_routes:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       27 (to L6)
               NOT_TAKEN

596            LOAD_FAST_BORROW         1 (actions)
               LOAD_ATTR                7 (append + NULL|self)

597            LOAD_CONST              11 ('[BLOCK] Admin route missing: ')
               LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              12 (' — verify app/routes/admin.py (')

598            LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')

597            BUILD_STRING             5

596            CALL                     1
               POP_TOP
               JUMP_BACKWARD          185 (to L1)

600    L6:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              13 ('dashboard_ui:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       27 (to L7)
               NOT_TAKEN

601            LOAD_FAST_BORROW         1 (actions)
               LOAD_ATTR                7 (append + NULL|self)

602            LOAD_CONST              14 ('[BLOCK] Dashboard surface missing: ')
               LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              15 (' — verify the Memory Review tab markup (')

603            LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')

602            BUILD_STRING             5

601            CALL                     1
               POP_TOP
               JUMP_BACKWARD          234 (to L1)

605    L7:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              16 ('portal_isolation:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       28 (to L8)
               NOT_TAKEN

606            LOAD_FAST_BORROW         1 (actions)
               LOAD_ATTR                7 (append + NULL|self)

607            LOAD_CONST              17 ('[BLOCK] Tenant portal leak: ')
               LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              18 (' — remove the Memory Review reference from portal.py (')

608            LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')

607            BUILD_STRING             5

606            CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          284 (to L1)

610    L8:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              19 ('forbidden_ui:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       28 (to L9)
               NOT_TAKEN

611            LOAD_FAST_BORROW         1 (actions)
               LOAD_ATTR                7 (append + NULL|self)

612            LOAD_CONST              20 ('[BLOCK] Forbidden Memory Review control present: ')

613            LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              21 (' (')
               LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')

612            BUILD_STRING             5

611            CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          334 (to L1)

615    L9:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              22 ('forbidden_raw_field:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       28 (to L10)
               NOT_TAKEN

616            LOAD_FAST_BORROW         1 (actions)
               LOAD_ATTR                7 (append + NULL|self)

617            LOAD_CONST              23 ('[BLOCK] Forbidden raw-payload reference in UI: ')

618            LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              21 (' (')
               LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')

617            BUILD_STRING             5

616            CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          384 (to L1)

620   L10:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              24 ('offlimits:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       28 (to L11)
               NOT_TAKEN

621            LOAD_FAST_BORROW         1 (actions)
               LOAD_ATTR                7 (append + NULL|self)

622            LOAD_CONST              25 ('[BLOCK] Off-limits file missing: ')
               LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              21 (' (')
               LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')
               BUILD_STRING             5

621            CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          434 (to L1)

624   L11:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              26 ('self_check:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       31 (to L12)
               NOT_TAKEN

625            LOAD_FAST_BORROW         1 (actions)
               LOAD_ATTR                7 (append + NULL|self)

626            LOAD_CONST              27 ('[')
               LOAD_FAST_BORROW         3 (sev)
               FORMAT_SIMPLE
               LOAD_CONST              28 ('] PAS158 self-check failed: ')
               LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              21 (' (')
               LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')
               BUILD_STRING             7

625            CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          487 (to L1)

629   L12:     LOAD_FAST                1 (actions)
               LOAD_ATTR                7 (append + NULL|self)

630            LOAD_CONST              27 ('[')
               LOAD_FAST                3 (sev)
               FORMAT_SIMPLE
               LOAD_CONST              29 ('] ')
               LOAD_FAST                4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              30 (' — ')
               LOAD_FAST                5 (detail)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L13)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              31 ('see report')
      L13:     FORMAT_SIMPLE
               LOAD_CONST              32 ('.')
               BUILD_STRING             7

629            CALL                     1
               POP_TOP
               EXTENDED_ARG             2
               JUMP_BACKWARD          527 (to L1)

584   L14:     END_FOR
               POP_ITER

632            LOAD_FAST_BORROW         1 (actions)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "scripts\pas158_memory_review_readiness_check.py", line 635>:
635           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17F83F30, file "scripts\pas158_memory_review_readiness_check.py", line 635>:
635           RESUME                   0

636           BUILD_LIST               0
              STORE_FAST               1 (checks)

637           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_phase_docs + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

638           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_admin_routes + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

639           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_dashboard_ui_tokens + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

640           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_portal_isolation + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

641           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_forbidden_ui_controls + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

642           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_forbidden_raw_fields_in_ui + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

643           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_offlimits_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

644           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_no_env_read + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

646           LOAD_GLOBAL             19 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

648           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS158')

649           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             21 (_now_iso + NULL)
              CALL                     0

650           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

651           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             22 (VERDICT_READY)
              COMPARE_OP              72 (==)

652           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             25 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

653           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             25 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

654           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             25 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

655           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             27 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053E10, file "scripts\pas158_memory_review_readiness_check.py", line 655>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

656           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             27 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053CF0, file "scripts\pas158_memory_review_readiness_check.py", line 656>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

657           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

658           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             29 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

647           BUILD_MAP               11
              STORE_FAST               3 (report)

660           LOAD_FAST_BORROW         3 (report)
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053E10, file "scripts\pas158_memory_review_readiness_check.py", line 655>:
 655           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053CF0, file "scripts\pas158_memory_review_readiness_check.py", line 656>:
 656           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "scripts\pas158_memory_review_readiness_check.py", line 670>:
670           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1801C7F0, file "scripts\pas158_memory_review_readiness_check.py", line 670>:
670           RESUME                   0

671           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

672           LOAD_CONST               0 ('pas158_memory_review_readiness_check')

674           LOAD_CONST               1 ('PAS158 — Evaluate Memory Review subsystem readiness. Read-only. Does not touch Supabase, .env, or any tenant data.')

671           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

679           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

680           LOAD_CONST               3 ('--repo-root')

681           LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

682           LOAD_CONST               4 ('Repo root to evaluate (default: parent of this script).')

679           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

684           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

685           LOAD_CONST               6 ('--output')

686           LOAD_GLOBAL              8 (REPORT_FILENAME)

687           LOAD_CONST               7 ('Where to write the JSON report (default ./')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST               8 (').')
              BUILD_STRING             3

684           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

689           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

690           LOAD_CONST               9 ('--json')

691           LOAD_CONST              10 ('store_true')

692           LOAD_CONST              11 ('Emit the report JSON on stdout in addition to the file.')

689           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

694           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

695           LOAD_CONST              13 ('--summary-only')

696           LOAD_CONST              10 ('store_true')

697           LOAD_CONST              14 ('Skip writing the full report file; print verdict only.')

694           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

699           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

700           LOAD_CONST              15 ('--strict')

701           LOAD_CONST              10 ('store_true')

702           LOAD_CONST              16 ('Exit 1 unless verdict == READY (default policy is the same).')

699           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

704           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "scripts\pas158_memory_review_readiness_check.py", line 707>:
707           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8E300, file "scripts\pas158_memory_review_readiness_check.py", line 707>:
707           RESUME                   0

708           LOAD_GLOBAL              1 (print + NULL)

709           LOAD_CONST               0 ('[PAS158] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

710           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

711           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

712           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

713           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

714           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

709           BUILD_STRING            12

708           CALL                     1
              POP_TOP

716           LOAD_FAST_BORROW         0 (report)
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

717           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

718           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS158] operator actions:')
              CALL                     1
              POP_TOP

719           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 20, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

720           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

719   L3:     END_FOR
              POP_ITER

721           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          20
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

722           LOAD_GLOBAL              1 (print + NULL)
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

721   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

717   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "scripts\pas158_memory_review_readiness_check.py", line 725>:
725           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C18104030, file "scripts\pas158_memory_review_readiness_check.py", line 725>:
 725           RESUME                   0

 726           NOP

 727   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 728           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 729           LOAD_CONST               3 ('utf-8')

 727           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 731           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 732   L4:     LOAD_GLOBAL             11 (print + NULL)

 733           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 734           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 733           BUILD_STRING             4

 735           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 732           LOAD_CONST               7 (('file',))
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

 731   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C180FC210, file "scripts\pas158_memory_review_readiness_check.py", line 739>:
739           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17F842E0, file "scripts\pas158_memory_review_readiness_check.py", line 739>:
 739            RESUME                   0

 740            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 741            NOP

 742    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 746    L2:     LOAD_GLOBAL             10 (os)
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

 747            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 748            LOAD_GLOBAL             23 (print + NULL)

 749            LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2

 750            LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)

 748            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 752            LOAD_SMALL_INT           2
                RETURN_VALUE

 754    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 756            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 757            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 759    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 761            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 762            LOAD_GLOBAL             23 (print + NULL)
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

 765    L6:     LOAD_FAST                5 (report)
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

 743            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 744    L9:     LOAD_FAST                3 (e)
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

 743   L17:     RERAISE                  0

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
