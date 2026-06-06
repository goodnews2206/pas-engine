# memory/rollout_ledger

- **pyc:** `app\services\memory\__pycache__\rollout_ledger.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/rollout_ledger.py`
- **co_filename (from bytecode):** `app\services\memory\rollout_ledger.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144M — Memory Rollout Ledger.

Durable, structural-only audit ledger for every operator-approved
memory-rollout decision. Pairs with:
  * PAS144K — rollout planner (decides the action)
  * PAS144L — signed approval + safe apply (records the operator's
              intent and executes the change)
  * scripts/migrate_v12_memory_rollout_ledger.sql (the additive table)
  * scripts/memory_rollout_history.py (the operator-history CLI)

This module is the seam between an in-memory PAS144L apply report and
the ``pas_memory_rollout_ledger`` table. It also exposes tenant-scoped
read helpers so a future dashboard / PAS Brain UI can surface rollout
history without going through PostgREST directly.

Hard contract — every public helper here:
  1. Requires tenant scope on tenant readers — ``brokerage_id`` is
     mandatory on the brokerage history helper; ``operator_id`` is
     mandatory on the operator history helper.
  2. There is NO unscoped tenant reader. Cross-tenant reads only flow
     through the operator-history helper, which is intentionally
     named to make the cross-tenant nature obvious.
  3. Caller-supplied ``limit`` is clamped to ``MAX_HISTORY_LIMIT``.
  4. Never raises on Supabase failure: returns ``[]`` (for readers) or
     a structured failure dict (for the writer).
  5. Never echoes raw memory / prompt / transcript values into the
     ledger row — the evidence whitelist is closed and re-applied as
     defence-in-depth even though PAS144K already filtered upstream.
  6. ``allowed_patch`` is constrained to the same single-flag shape as
     PAS144L — no widening here.

Public surface (deliberately tiny):
  - ledger_row_from_apply_report(report)       -> dict | None
  - validate_ledger_row(row)                   -> list[str]
  - record_rollout_ledger(report)              -> dict
  - list_rollout_history_for_brokerage(
        brokerage_id, *, limit=50)             -> list[dict]
  - list_rollout_history_for_operator(
        operator_id, *, limit=50)              -> list[dict]

PAS144M explicitly does NOT build:
  * autonomous rollout (each row is operator-signed by contract);
  * automatic memory writes;
  * widened config patching (allowed_patch stays single-flag);
  * embeddings / vector helpers;
  * any cross-tenant tenant-facing read path;
  * any dashboard / UI integration.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `VALID_ACTIONS`, `__future__`, `annotations`, `app.db.supabase_client`, `get_supabase`, `logging`, `rollout`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_limit`, `_coerce_apply_status`, `_derive_target_enabled`, `_get_db`, `_normalise_allowed_patch`, `_safe_evidence`, `_safe_warnings`, `_strip_forbidden`, `ledger_row_from_apply_report`, `list_rollout_history_for_brokerage`, `list_rollout_history_for_operator`, `record_rollout_ledger`, `validate_ledger_row`

## Env-key candidates

_none_

## String constants (redacted where noted)

- "\nPAS144M — Memory Rollout Ledger.\n\nDurable, structural-only audit ledger for every operator-approved\nmemory-rollout decision. Pairs with:\n  * PAS144K — rollout planner (decides the action)\n  * PAS144L — signed approval + safe apply (records the operator's\n              intent and executes the change)\n  * scripts/migrate_v12_memory_rollout_ledger.sql (the additive table)\n  * scripts/memory_rollout_history.py (the operator-history CLI)\n\nThis module is the seam between an in-memory PAS144L apply report and\nthe ``pas_memory_rollout_ledger`` table. It also exposes tenant-scoped\nread helpers so a future dashboard / PAS Brain UI can surface rollout\nhistory without going through PostgREST directly.\n\nHard contract — every public helper here:\n  1. Requires tenant scope on tenant readers — ``brokerage_id`` is\n     mandatory on the brokerage history helper; ``operator_id`` is\n     mandatory on the operator history helper.\n  2. There is NO unscoped tenant reader. Cross-tenant reads only flow\n     through the operator-history helper, which is intentionally\n     named to make the cross-tenant nature obvious.\n  3. Caller-supplied ``limit`` is clamped to ``MAX_HISTORY_LIMIT``.\n  4. Never raises on Supabase failure: returns ``[]`` (for readers) or\n     a structured failure dict (for the writer).\n  5. Never echoes raw memory / prompt / transcript values into the\n     ledger row — the evidence whitelist is closed and re-applied as\n     defence-in-depth even though PAS144K already filtered upstream.\n  6. ``allowed_patch`` is constrained to the same single-flag shape as\n     PAS144L — no widening here.\n\nPublic surface (deliberately tiny):\n  - ledger_row_from_apply_report(report)       -> dict | None\n  - validate_ledger_row(row)                   -> list[str]\n  - record_rollout_ledger(report)              -> dict\n  - list_rollout_history_for_brokerage(\n        brokerage_id, *, limit=50)             -> list[dict]\n  - list_rollout_history_for_operator(\n        operator_id, *, limit=50)              -> list[dict]\n\nPAS144M explicitly does NOT build:\n  * autonomous rollout (each row is operator-signed by contract);\n  * automatic memory writes;\n  * widened config patching (allowed_patch stays single-flag);\n  * embeddings / vector helpers;\n  * any cross-tenant tenant-facing read path;\n  * any dashboard / UI integration.\n"
- 'pas.memory.rollout_ledger'
- 'pas_memory_rollout_ledger'
- 'dry_run'
- 'applied'
- 'apply_failed'
- 'invalid_manifest'
- 'approved_pending_apply'
- 'memory_injection_enabled'
- 'limit'
- 'Lazy Supabase resolver. Mirrors review.py / queries.py so unit\ntests can patch ``app.db.supabase_client.get_supabase``.'
- 'Any'
- 'return'
- 'int'
- 'evidence'
- 'Dict[str, Any]'
- 'Project evidence through the closed PAS144J whitelist.'
- 'warnings'
- 'List[str]'
- 'Normalise a warnings field into a list of short strings.'
- 'patch'
- 'Return a defensively-trimmed allowed_patch.\n\nAccepts only:\n  * an empty dict — recorded as {};\n  * {"features": {"memory_injection_enabled": <bool>}} — recorded\n    verbatim.\n\nAnything else collapses to {} so a regressed upstream cannot leak\narbitrary keys into the ledger.\n'
- 'features'
- 'allowed_patch'
- 'result'
- 'Optional[bool]'
- "Prefer the patch's flag; fall back to result.target_enabled."
- 'target_enabled'
- 'str'
- "Map an apply-result status string to the ledger's closed enum."
- 'status'
- 'row'
- 'Drop any forbidden raw-payload keys from a row dict.\n\nDefence-in-depth: the builder never reads such keys, but if a\ncaller hand-rolls a row dict (or a future regression sneaks a key\nin), this strip ensures the ledger insert never carries one.\n'
- 'report'
- 'Optional[Dict[str, Any]]'
- 'Build a structural-only ledger row from a PAS144L apply report.\n\nCanonical input shape:\n    {\n        "manifest": {\n            "approval_id":     str,\n            "operator_id":     str,\n            "plan_hash":       str,\n            "approval_status": str,\n            "allowed_patch":   dict,\n            "plan": {\n                "brokerage_id":         str,\n                "recommended_action":   str,\n                "evidence":             dict,   # PAS144K whitelist\n                "warnings":             list[str],\n                ...\n            },\n        },\n        "result": {\n            "applied":             bool,\n            "dry_run":             bool,\n            "status":              "dry_run" | "applied"\n                                   | "apply_failed" | "invalid_manifest",\n            "error_code":          str | None,\n            "brokerage_id":        str | None,\n            "recommended_action":  str | None,\n            "target_enabled":      bool | None,\n        },\n    }\n\nReturns ``None`` when the report is structurally unusable\n(missing approval_id, missing brokerage_id, missing plan_hash, or\nnothing dict-shaped). Never raises.\n\nThe returned dict contains structural fields only — raw memory,\ntranscript, prompt, or evidence-payload content can never enter\nit because the evidence whitelist is closed and forbidden keys\nare stripped as the final step.\n'
- 'manifest'
- 'plan'
- 'approval_id'
- 'operator_id'
- 'plan_hash'
- 'approval_status'
- 'brokerage_id'
- 'recommended_action'
- 'error_code'
- 'apply_status'
- 'Return a list of human-readable blockers for a ledger row.\n\nAn empty list means the row is structurally valid and safe to\ninsert into ``pas_memory_rollout_ledger``. Pure. Never raises.\n'
- 'row_must_be_dict'
- 'missing_approval_id'
- 'missing_brokerage_id'
- 'missing_operator_id'
- 'missing_plan_hash'
- 'invalid_recommended_action:'
- 'invalid_approval_status:'
- 'invalid_apply_status:'
- 'invalid_dry_run'
- 'invalid_applied'
- 'applied_but_dry_run'
- 'applied_but_wrong_apply_status'
- 'invalid_target_enabled'
- 'invalid_error_code_type'
- 'error_code_too_long'
- 'invalid_allowed_patch_type'
- 'allowed_patch_has_disallowed_top_keys:'
- 'allowed_patch_features_must_be_dict'
- 'allowed_patch_features_has_disallowed_keys:'
- 'allowed_patch_flag_must_be_bool'
- 'invalid_evidence_type'
- 'evidence_has_disallowed_key:'
- 'invalid_warnings_type'
- 'row_has_forbidden_key:'
- 'Build, validate, and insert a single ledger row from an apply\nreport.\n\nReturn shape:\n  * ``{"status": "ok",      "ledger_row": {...}}`` on success.\n  * ``{"status": "skipped", "reason":     "<short token>"}`` when\n    the report cannot be coerced into a row (the builder returned\n    ``None``).\n  * ``{"status": "failed",  "errors":     [...]}`` when the row\n    is malformed.\n  * ``{"status": "failed",  "errors":     ["db_write_failed:..."]}``\n    when the Supabase insert fails. Never raises.\n'
- 'skipped'
- 'reason'
- 'unrecognised_apply_report_shape'
- 'failed'
- 'errors'
- 'data'
- 'ledger_row'
- 'record_rollout_ledger insert failed (non-critical) | brokerage='
- ' | error_type='
- 'db_write_failed:'
- 'List[Dict[str, Any]]'
- 'Return rollout-ledger rows for ``brokerage_id`` newest-first.\n\nTenant-scoped: a missing brokerage_id returns ``[]``. Caller-\nsupplied ``limit`` is clamped to ``MAX_HISTORY_LIMIT``. Never\nraises on Supabase failure.\n'
- 'list_rollout_history_for_brokerage dropped | reason=missing_brokerage_id'
- 'created_at'
- 'list_rollout_history_for_brokerage failed (non-critical) | brokerage='
- 'Return rollout-ledger rows for ``operator_id`` newest-first.\n\nOperator-scoped (intentionally cross-tenant — operators may\nlegally oversee multiple brokerages). Never exposed via tenant-\nfacing HTTP routes. A missing operator_id returns ``[]``. Caller-\nsupplied ``limit`` is clamped to ``MAX_HISTORY_LIMIT``. Never\nraises on Supabase failure.\n'
- 'list_rollout_history_for_operator dropped | reason=missing_operator_id'
- 'list_rollout_history_for_operator failed (non-critical) | operator='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ("\nPAS144M — Memory Rollout Ledger.\n\nDurable, structural-only audit ledger for every operator-approved\nmemory-rollout decision. Pairs with:\n  * PAS144K — rollout planner (decides the action)\n  * PAS144L — signed approval + safe apply (records the operator's\n              intent and executes the change)\n  * scripts/migrate_v12_memory_rollout_ledger.sql (the additive table)\n  * scripts/memory_rollout_history.py (the operator-history CLI)\n\nThis module is the seam between an in-memory PAS144L apply report and\nthe ``pas_memory_rollout_ledger`` table. It also exposes tenant-scoped\nread helpers so a future dashboard / PAS Brain UI can surface rollout\nhistory without going through PostgREST directly.\n\nHard contract — every public helper here:\n  1. Requires tenant scope on tenant readers — ``brokerage_id`` is\n     mandatory on the brokerage history helper; ``operator_id`` is\n     mandatory on the operator history helper.\n  2. There is NO unscoped tenant reader. Cross-tenant reads only flow\n     through the operator-history helper, which is intentionally\n     named to make the cross-tenant nature obvious.\n  3. Caller-supplied ``limit`` is clamped to ``MAX_HISTORY_LIMIT``.\n  4. Never raises on Supabase failure: returns ``[]`` (for readers) or\n     a structured failure dict (for the writer).\n  5. Never echoes raw memory / prompt / transcript values into the\n     ledger row — the evidence whitelist is closed and re-applied as\n     defence-in-depth even though PAS144K already filtered upstream.\n  6. ``allowed_patch`` is constrained to the same single-flag shape as\n     PAS144L — no widening here.\n\nPublic surface (deliberately tiny):\n  - ledger_row_from_apply_report(report)       -> dict | None\n  - validate_ledger_row(row)                   -> list[str]\n  - record_rollout_ledger(report)              -> dict\n  - list_rollout_history_for_brokerage(\n        brokerage_id, *, limit=50)             -> list[dict]\n  - list_rollout_history_for_operator(\n        operator_id, *, limit=50)              -> list[dict]\n\nPAS144M explicitly does NOT build:\n  * autonomous rollout (each row is operator-signed by contract);\n  * automatic memory writes;\n  * widened config patching (allowed_patch stays single-flag);\n  * embeddings / vector helpers;\n  * any cross-tenant tenant-facing read path;\n  * any dashboard / UI integration.\n")
              STORE_NAME               0 (__doc__)

 51           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 53           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 54           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (List)
              STORE_NAME               7 (List)
              IMPORT_FROM              8 (Optional)
              STORE_NAME               8 (Optional)
              POP_TOP

 56           LOAD_SMALL_INT           1
              LOAD_CONST               4 (('VALID_ACTIONS',))
              IMPORT_NAME              9 (rollout)
              IMPORT_FROM             10 (VALID_ACTIONS)
              STORE_NAME              10 (VALID_ACTIONS)
              POP_TOP

 58           LOAD_NAME                3 (logging)
              LOAD_ATTR               22 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.memory.rollout_ledger')
              CALL                     1
              STORE_NAME              12 (logger)

 65           LOAD_CONST               6 ('pas_memory_rollout_ledger')
              STORE_NAME              13 (_TABLE)

 70           LOAD_SMALL_INT         200
              STORE_NAME              14 (MAX_HISTORY_LIMIT)

 71           LOAD_SMALL_INT          50
              STORE_NAME              15 (DEFAULT_HISTORY_LIMIT)

 74           LOAD_CONST               7 ('dry_run')
              STORE_NAME              16 (APPLY_STATUS_DRY_RUN)

 75           LOAD_CONST               8 ('applied')
              STORE_NAME              17 (APPLY_STATUS_APPLIED)

 76           LOAD_CONST               9 ('apply_failed')
              STORE_NAME              18 (APPLY_STATUS_APPLY_FAILED)

 77           LOAD_CONST              10 ('invalid_manifest')
              STORE_NAME              19 (APPLY_STATUS_INVALID_MANIFEST)

 79           LOAD_NAME               20 (frozenset)
              PUSH_NULL

 80           LOAD_NAME               16 (APPLY_STATUS_DRY_RUN)

 81           LOAD_NAME               17 (APPLY_STATUS_APPLIED)

 82           LOAD_NAME               18 (APPLY_STATUS_APPLY_FAILED)

 83           LOAD_NAME               19 (APPLY_STATUS_INVALID_MANIFEST)

 79           BUILD_SET                4
              CALL                     1
              STORE_NAME              21 (VALID_APPLY_STATUSES)

 89           LOAD_CONST              11 ('approved_pending_apply')
              STORE_NAME              22 (APPROVAL_STATUS_PENDING_APPLY)

 90           LOAD_NAME               20 (frozenset)
              PUSH_NULL
              LOAD_NAME               22 (APPROVAL_STATUS_PENDING_APPLY)
              BUILD_SET                1
              CALL                     1
              STORE_NAME              23 (VALID_APPROVAL_STATUSES)

 93           LOAD_CONST              12 ('memory_injection_enabled')
              STORE_NAME              24 (_ALLOWED_FLAG)

 98           LOAD_CONST              39 (('total_calls', 'memory_succeeded_calls', 'non_memory_calls', 'booking_rate_with_memory', 'booking_rate_without_memory', 'callback_rate_with_memory', 'callback_rate_without_memory', 'provider_failure_rate_with_memory', 'provider_failure_rate_without_memory', 'lift_booking_rate', 'lift_callback_rate', 'health_status', 'rollout_recommendation'))
              STORE_NAME              25 (_SAFE_EVIDENCE_FIELDS)

117           LOAD_NAME               20 (frozenset)
              PUSH_NULL
              BUILD_SET                0
              LOAD_CONST              40 (frozenset({'memory_content', 'full_transcript', 'items', 'output_text', 'turns_text', 'formatted', 'utterances', 'raw_transcript', 'input_text', 'transcript', 'base_prompt', 'prompt', 'injected_prompt', 'messages', 'raw_prompt'}))
              SET_UPDATE               1
              CALL                     1
              STORE_NAME              26 (_FORBIDDEN_KEYS)

130           LOAD_CONST              13 (<code object _get_db at 0x0000018C17FA34B0, file "app\services\memory\rollout_ledger.py", line 130>)
              MAKE_FUNCTION
              STORE_NAME              27 (_get_db)

137           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\rollout_ledger.py", line 137>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _clamp_limit at 0x0000018C17FF1530, file "app\services\memory\rollout_ledger.py", line 137>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_clamp_limit)

149           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA2C40, file "app\services\memory\rollout_ledger.py", line 149>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _safe_evidence at 0x0000018C17F95CF0, file "app\services\memory\rollout_ledger.py", line 149>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_safe_evidence)

160           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA2100, file "app\services\memory\rollout_ledger.py", line 160>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object _safe_warnings at 0x0000018C1794E9E0, file "app\services\memory\rollout_ledger.py", line 160>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_safe_warnings)

171           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA21F0, file "app\services\memory\rollout_ledger.py", line 171>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object _normalise_allowed_patch at 0x0000018C17D6DFC0, file "app\services\memory\rollout_ledger.py", line 171>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_normalise_allowed_patch)

199           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18025230, file "app\services\memory\rollout_ledger.py", line 199>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object _derive_target_enabled at 0x0000018C17D77E00, file "app\services\memory\rollout_ledger.py", line 199>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_derive_target_enabled)

212           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA30F0, file "app\services\memory\rollout_ledger.py", line 212>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object _coerce_apply_status at 0x0000018C17FF0C30, file "app\services\memory\rollout_ledger.py", line 212>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_coerce_apply_status)

220           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA31E0, file "app\services\memory\rollout_ledger.py", line 220>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object _strip_forbidden at 0x0000018C18038B70, file "app\services\memory\rollout_ledger.py", line 220>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              34 (_strip_forbidden)

236           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA32D0, file "app\services\memory\rollout_ledger.py", line 236>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object ledger_row_from_apply_report at 0x0000018C17E04B30, file "app\services\memory\rollout_ledger.py", line 236>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              35 (ledger_row_from_apply_report)

354           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA1D40, file "app\services\memory\rollout_ledger.py", line 354>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object validate_ledger_row at 0x0000018C17D516D0, file "app\services\memory\rollout_ledger.py", line 354>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              36 (validate_ledger_row)

460           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA23D0, file "app\services\memory\rollout_ledger.py", line 460>)
              MAKE_FUNCTION
              LOAD_CONST              33 (<code object record_rollout_ledger at 0x0000018C17EE1CC0, file "app\services\memory\rollout_ledger.py", line 460>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              37 (record_rollout_ledger)

512           LOAD_CONST              34 ('limit')

515           LOAD_NAME               15 (DEFAULT_HISTORY_LIMIT)

512           BUILD_MAP                1
              LOAD_CONST              35 (<code object __annotate__ at 0x0000018C18024B30, file "app\services\memory\rollout_ledger.py", line 512>)
              MAKE_FUNCTION
              LOAD_CONST              36 (<code object list_rollout_history_for_brokerage at 0x0000018C17D81A00, file "app\services\memory\rollout_ledger.py", line 512>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              38 (list_rollout_history_for_brokerage)

550           LOAD_CONST              34 ('limit')

553           LOAD_NAME               15 (DEFAULT_HISTORY_LIMIT)

550           BUILD_MAP                1
              LOAD_CONST              37 (<code object __annotate__ at 0x0000018C18025930, file "app\services\memory\rollout_ledger.py", line 550>)
              MAKE_FUNCTION
              LOAD_CONST              38 (<code object list_rollout_history_for_operator at 0x0000018C17D7D400, file "app\services\memory\rollout_ledger.py", line 550>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              39 (list_rollout_history_for_operator)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object _get_db at 0x0000018C17FA34B0, file "app\services\memory\rollout_ledger.py", line 130>:
130           RESUME                   0

133           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('get_supabase',))
              IMPORT_NAME              0 (app.db.supabase_client)
              IMPORT_FROM              1 (get_supabase)
              STORE_FAST               0 (get_supabase)
              POP_TOP

134           LOAD_FAST_BORROW         0 (get_supabase)
              PUSH_NULL
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\rollout_ledger.py", line 137>:
137           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('limit')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _clamp_limit at 0x0000018C17FF1530, file "app\services\memory\rollout_ledger.py", line 137>:
 137           RESUME                   0

 138           LOAD_FAST_BORROW         0 (limit)
               POP_JUMP_IF_NOT_NONE     7 (to L1)
               NOT_TAKEN

 139           LOAD_GLOBAL              0 (DEFAULT_HISTORY_LIMIT)
               RETURN_VALUE

 140   L1:     NOP

 141   L2:     LOAD_GLOBAL              3 (int + NULL)
               LOAD_FAST_BORROW         0 (limit)
               CALL                     1
               STORE_FAST               1 (n)

 144   L3:     LOAD_FAST                1 (n)
               LOAD_SMALL_INT           0
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 145           LOAD_GLOBAL              0 (DEFAULT_HISTORY_LIMIT)
               RETURN_VALUE

 146   L4:     LOAD_GLOBAL              9 (min + NULL)
               LOAD_FAST                1 (n)
               LOAD_GLOBAL             10 (MAX_HISTORY_LIMIT)
               CALL                     2
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 142           LOAD_GLOBAL              4 (TypeError)
               LOAD_GLOBAL              6 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

 143           LOAD_GLOBAL              0 (DEFAULT_HISTORY_LIMIT)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 142   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app\services\memory\rollout_ledger.py", line 149>:
149           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('evidence')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_evidence at 0x0000018C17F95CF0, file "app\services\memory\rollout_ledger.py", line 149>:
 149           RESUME                   0

 151           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (evidence)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

 152           BUILD_MAP                0
               RETURN_VALUE

 155   L1:     LOAD_GLOBAL              4 (_SAFE_EVIDENCE_FIELDS)
               GET_ITER

 153           LOAD_FAST_AND_CLEAR      1 (k)
               SWAP                     2
       L2:     BUILD_MAP                0
               SWAP                     2

 155   L3:     FOR_ITER                28 (to L6)
               STORE_FAST               1 (k)

 156           LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (k, evidence)
               CONTAINS_OP              0 (in)

 154   L4:     POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)
       L5:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (k, evidence)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_FAST_BORROW         1 (k)
               CALL                     1
               MAP_ADD                  2
               JUMP_BACKWARD           30 (to L3)

 155   L6:     END_FOR
               POP_ITER

 153   L7:     SWAP                     2
               STORE_FAST               1 (k)
               RETURN_VALUE

  --   L8:     SWAP                     2
               POP_TOP

 153           SWAP                     2
               STORE_FAST               1 (k)
               RERAISE                  0
ExceptionTable:
  L2 to L4 -> L8 [2]
  L5 to L7 -> L8 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app\services\memory\rollout_ledger.py", line 160>:
160           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('warnings')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_warnings at 0x0000018C1794E9E0, file "app\services\memory\rollout_ledger.py", line 160>:
160           RESUME                   0

162           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (warnings)
              LOAD_GLOBAL              2 (list)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

163           BUILD_LIST               0
              RETURN_VALUE

164   L1:     BUILD_LIST               0
              STORE_FAST               1 (out)

165           LOAD_FAST_BORROW         0 (warnings)
              GET_ITER
      L2:     FOR_ITER                89 (to L5)
              STORE_FAST               2 (w)

166           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (w)
              LOAD_GLOBAL              4 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           27 (to L2)
      L3:     LOAD_FAST_BORROW         2 (w)
              LOAD_ATTR                7 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD           51 (to L2)

167   L4:     LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_FAST_BORROW         2 (w)
              LOAD_ATTR                7 (strip + NULL|self)
              CALL                     0
              LOAD_CONST               1 (slice(None, 200, None))
              BINARY_OP               26 ([])
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           91 (to L2)

165   L5:     END_FOR
              POP_ITER

168           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app\services\memory\rollout_ledger.py", line 171>:
171           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('patch')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _normalise_allowed_patch at 0x0000018C17D6DFC0, file "app\services\memory\rollout_ledger.py", line 171>:
 171            RESUME                   0

 182            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (patch)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        9 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (patch)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN

 183    L1:     BUILD_MAP                0
                RETURN_VALUE

 184    L2:     LOAD_FAST_BORROW         0 (patch)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               1 ('features')
                CALL                     1
                STORE_FAST               1 (features)

 185            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (features)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN

 186            BUILD_MAP                0
                RETURN_VALUE

 187    L3:     LOAD_FAST_BORROW         1 (features)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_GLOBAL              6 (_ALLOWED_FLAG)
                CALL                     1
                STORE_FAST               2 (flag)

 188            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (flag)
                LOAD_GLOBAL              8 (bool)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN

 189            BUILD_MAP                0
                RETURN_VALUE

 190    L4:     LOAD_FAST_BORROW         0 (patch)
                LOAD_ATTR               11 (keys + NULL|self)
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      3 (k)
                SWAP                     2
        L5:     BUILD_LIST               0
                SWAP                     2
        L6:     FOR_ITER                13 (to L9)
                STORE_FAST_LOAD_FAST    51 (k, k)
                LOAD_CONST               1 ('features')
                COMPARE_OP             119 (bool(!=))
        L7:     POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L6)
        L8:     LOAD_FAST_BORROW         3 (k)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L6)
        L9:     END_FOR
                POP_ITER
       L10:     STORE_FAST               4 (extra_top)
                STORE_FAST               3 (k)

 191            LOAD_FAST_BORROW         1 (features)
                LOAD_ATTR               11 (keys + NULL|self)
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      3 (k)
                SWAP                     2
       L11:     BUILD_LIST               0
                SWAP                     2
       L12:     FOR_ITER                17 (to L15)
                STORE_FAST_LOAD_FAST    51 (k, k)
                LOAD_GLOBAL              6 (_ALLOWED_FLAG)
                COMPARE_OP             119 (bool(!=))
       L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           15 (to L12)
       L14:     LOAD_FAST_BORROW         3 (k)
                LIST_APPEND              2
                JUMP_BACKWARD           19 (to L12)
       L15:     END_FOR
                POP_ITER
       L16:     STORE_FAST               5 (extra_feat)
                STORE_FAST               3 (k)

 192            LOAD_FAST_BORROW         4 (extra_top)
                TO_BOOL
                POP_JUMP_IF_TRUE         9 (to L17)
                NOT_TAKEN
                LOAD_FAST_BORROW         5 (extra_feat)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L18)
                NOT_TAKEN

 195   L17:     BUILD_MAP                0
                RETURN_VALUE

 196   L18:     LOAD_CONST               1 ('features')
                LOAD_GLOBAL              6 (_ALLOWED_FLAG)
                LOAD_FAST_BORROW         2 (flag)
                BUILD_MAP                1
                BUILD_MAP                1
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 190            SWAP                     2
                STORE_FAST               3 (k)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 191            SWAP                     2
                STORE_FAST               3 (k)
                RERAISE                  0
ExceptionTable:
  L5 to L7 -> L19 [2]
  L8 to L10 -> L19 [2]
  L11 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C18025230, file "app\services\memory\rollout_ledger.py", line 199>:
199           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('allowed_patch')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('result')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('Optional[bool]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _derive_target_enabled at 0x0000018C17D77E00, file "app\services\memory\rollout_ledger.py", line 199>:
199           RESUME                   0

201           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (allowed_patch)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (allowed_patch)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('features')
              CALL                     1
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               2 (None)
      L2:     STORE_FAST               2 (features)

202           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (features)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       46 (to L3)
              NOT_TAKEN

203           LOAD_FAST_BORROW         2 (features)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_GLOBAL              6 (_ALLOWED_FLAG)
              CALL                     1
              STORE_FAST               3 (flag)

204           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (flag)
              LOAD_GLOBAL              8 (bool)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

205           LOAD_FAST_BORROW         3 (flag)
              RETURN_VALUE

206   L3:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (result)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (result)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               3 ('target_enabled')
              CALL                     1
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               2 (None)
      L5:     STORE_FAST               4 (target)

207           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         4 (target)
              LOAD_GLOBAL              8 (bool)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN

208           LOAD_FAST_BORROW         4 (target)
              RETURN_VALUE

209   L6:     LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "app\services\memory\rollout_ledger.py", line 212>:
212           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('result')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _coerce_apply_status at 0x0000018C17FF0C30, file "app\services\memory\rollout_ledger.py", line 212>:
212           RESUME                   0

214           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (result)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (result)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('status')
              CALL                     1
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               2 (None)
      L2:     STORE_FAST               1 (raw)

215           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (raw)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       14 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (raw)
              LOAD_GLOBAL              8 (VALID_APPLY_STATUSES)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

216           LOAD_FAST_BORROW         1 (raw)
              RETURN_VALUE

217   L3:     LOAD_GLOBAL             10 (APPLY_STATUS_INVALID_MANIFEST)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "app\services\memory\rollout_ledger.py", line 220>:
220           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _strip_forbidden at 0x0000018C18038B70, file "app\services\memory\rollout_ledger.py", line 220>:
 220           RESUME                   0

 228           LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                1 (items + NULL|self)
               CALL                     0
               GET_ITER

 227           LOAD_FAST_AND_CLEAR      1 (k)
               LOAD_FAST_AND_CLEAR      2 (v)
               SWAP                     3
       L1:     BUILD_MAP                0
               SWAP                     2

 228   L2:     FOR_ITER                20 (to L5)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   18 (k, v)
               LOAD_FAST_BORROW         1 (k)
               LOAD_GLOBAL              2 (_FORBIDDEN_KEYS)
               CONTAINS_OP              1 (not in)
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           18 (to L2)
       L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (k, v)
               MAP_ADD                  2
               JUMP_BACKWARD           22 (to L2)
       L5:     END_FOR
               POP_ITER

 227   L6:     SWAP                     3
               STORE_FAST               2 (v)
               STORE_FAST               1 (k)
               RETURN_VALUE

  --   L7:     SWAP                     2
               POP_TOP

 227           SWAP                     3
               STORE_FAST               2 (v)
               STORE_FAST               1 (k)
               RERAISE                  0
ExceptionTable:
  L1 to L3 -> L7 [3]
  L4 to L6 -> L7 [3]

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "app\services\memory\rollout_ledger.py", line 236>:
236           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')

237           LOAD_CONST               2 ('Any')

236           LOAD_CONST               3 ('return')

238           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

236           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object ledger_row_from_apply_report at 0x0000018C17E04B30, file "app\services\memory\rollout_ledger.py", line 236>:
236            RESUME                   0

278            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (report)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

279            LOAD_CONST               1 (None)
               RETURN_VALUE

281    L1:     LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               2 ('manifest')
               CALL                     1
               STORE_FAST               1 (manifest)

282            LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               3 ('result')
               CALL                     1
               STORE_FAST               2 (result)

283            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (manifest)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L2)
               NOT_TAKEN
               LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (result)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

284    L2:     LOAD_CONST               1 (None)
               RETURN_VALUE

286    L3:     LOAD_FAST_BORROW         1 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               4 ('plan')
               CALL                     1
               STORE_FAST               3 (plan)

287            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         3 (plan)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN
               LOAD_FAST                3 (plan)
               JUMP_FORWARD             1 (to L5)
       L4:     BUILD_MAP                0
       L5:     STORE_FAST               3 (plan)

289            LOAD_FAST_BORROW         1 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               5 ('approval_id')
               CALL                     1
               STORE_FAST               4 (approval_id)

290            LOAD_FAST_BORROW         1 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               6 ('operator_id')
               CALL                     1
               STORE_FAST               5 (operator_id)

291            LOAD_FAST_BORROW         1 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               7 ('plan_hash')
               CALL                     1
               STORE_FAST               6 (plan_hash)

292            LOAD_FAST_BORROW         1 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               8 ('approval_status')
               CALL                     1
               STORE_FAST               7 (approval_status)

293            LOAD_GLOBAL              7 (_normalise_allowed_patch + NULL)
               LOAD_FAST_BORROW         1 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               9 ('allowed_patch')
               CALL                     1
               CALL                     1
               STORE_FAST               8 (allowed_patch)

297            LOAD_FAST_BORROW         3 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              10 ('brokerage_id')
               CALL                     1
               STORE_FAST               9 (brokerage_id)

298            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         9 (brokerage_id)
               LOAD_GLOBAL              8 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L6)
               NOT_TAKEN
               LOAD_FAST_BORROW         9 (brokerage_id)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L7)
               NOT_TAKEN

299    L6:     LOAD_FAST_BORROW         2 (result)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              10 ('brokerage_id')
               CALL                     1
               STORE_FAST               9 (brokerage_id)

300    L7:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         9 (brokerage_id)
               LOAD_GLOBAL              8 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L8)
               NOT_TAKEN
               LOAD_FAST_BORROW         9 (brokerage_id)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN

301    L8:     LOAD_CONST               1 (None)
               RETURN_VALUE

303    L9:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         4 (approval_id)
               LOAD_GLOBAL              8 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L10)
               NOT_TAKEN
               LOAD_FAST_BORROW         4 (approval_id)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L11)
               NOT_TAKEN

304   L10:     LOAD_CONST               1 (None)
               RETURN_VALUE

305   L11:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         5 (operator_id)
               LOAD_GLOBAL              8 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L12)
               NOT_TAKEN
               LOAD_FAST_BORROW         5 (operator_id)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L13)
               NOT_TAKEN

306   L12:     LOAD_CONST               1 (None)
               RETURN_VALUE

307   L13:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         6 (plan_hash)
               LOAD_GLOBAL              8 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L14)
               NOT_TAKEN
               LOAD_FAST_BORROW         6 (plan_hash)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L15)
               NOT_TAKEN

308   L14:     LOAD_CONST               1 (None)
               RETURN_VALUE

311   L15:     LOAD_FAST_BORROW         3 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              11 ('recommended_action')
               CALL                     1
               STORE_FAST              10 (recommended_action)

312            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW        10 (recommended_action)
               LOAD_GLOBAL              8 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        9 (to L16)
               NOT_TAKEN
               LOAD_FAST_BORROW        10 (recommended_action)
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L17)
               NOT_TAKEN

313   L16:     LOAD_FAST_BORROW         2 (result)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              11 ('recommended_action')
               CALL                     1
               STORE_FAST              10 (recommended_action)

314   L17:     LOAD_FAST_BORROW        10 (recommended_action)
               LOAD_GLOBAL             12 (VALID_ACTIONS)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE        3 (to L18)
               NOT_TAKEN

315            LOAD_CONST               1 (None)
               RETURN_VALUE

317   L18:     LOAD_GLOBAL             15 (_coerce_apply_status + NULL)
               LOAD_FAST_BORROW         2 (result)
               CALL                     1
               STORE_FAST              11 (apply_status)

318            LOAD_GLOBAL             17 (bool + NULL)
               LOAD_FAST_BORROW         2 (result)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              12 ('dry_run')
               CALL                     1
               CALL                     1
               STORE_FAST              12 (dry_run)

319            LOAD_GLOBAL             17 (bool + NULL)
               LOAD_FAST_BORROW         2 (result)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              13 ('applied')
               CALL                     1
               CALL                     1
               STORE_FAST              13 (applied)

320            LOAD_FAST_BORROW         2 (result)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              14 ('error_code')
               CALL                     1
               STORE_FAST              14 (error_code)

321            LOAD_FAST_BORROW        14 (error_code)
               POP_JUMP_IF_NONE        34 (to L19)
               NOT_TAKEN
               LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW        14 (error_code)
               LOAD_GLOBAL              8 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L19)
               NOT_TAKEN

322            LOAD_GLOBAL              9 (str + NULL)
               LOAD_FAST_BORROW        14 (error_code)
               CALL                     1
               STORE_FAST              14 (error_code)

323   L19:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW        14 (error_code)
               LOAD_GLOBAL              8 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       26 (to L20)
               NOT_TAKEN
               LOAD_GLOBAL             19 (len + NULL)
               LOAD_FAST_BORROW        14 (error_code)
               CALL                     1
               LOAD_SMALL_INT         128
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE       10 (to L20)
               NOT_TAKEN

324            LOAD_FAST_BORROW        14 (error_code)
               LOAD_CONST              15 (slice(None, 128, None))
               BINARY_OP               26 ([])
               STORE_FAST              14 (error_code)

326   L20:     LOAD_GLOBAL             21 (_derive_target_enabled + NULL)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 130 (allowed_patch, result)
               CALL                     2
               STORE_FAST              15 (target_enabled)

328            LOAD_GLOBAL             23 (_safe_evidence + NULL)
               LOAD_FAST_BORROW         3 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              16 ('evidence')
               CALL                     1
               CALL                     1
               STORE_FAST              16 (evidence)

329            LOAD_GLOBAL             25 (_safe_warnings + NULL)
               LOAD_FAST_BORROW         3 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              17 ('warnings')
               CALL                     1
               CALL                     1
               STORE_FAST              17 (warnings)

332            LOAD_CONST               5 ('approval_id')
               LOAD_FAST_BORROW         4 (approval_id)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0

333            LOAD_CONST              10 ('brokerage_id')
               LOAD_FAST_BORROW         9 (brokerage_id)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0

334            LOAD_CONST               6 ('operator_id')
               LOAD_FAST_BORROW         5 (operator_id)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0

335            LOAD_CONST              11 ('recommended_action')
               LOAD_FAST               10 (recommended_action)

336            LOAD_CONST              18 ('target_enabled')
               LOAD_FAST               15 (target_enabled)

337            LOAD_CONST               7 ('plan_hash')
               LOAD_FAST_BORROW         6 (plan_hash)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0

338            LOAD_CONST               8 ('approval_status')
               LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         7 (approval_status)
               LOAD_GLOBAL              8 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L21)
               NOT_TAKEN
               LOAD_FAST                7 (approval_status)
               JUMP_FORWARD             5 (to L22)
      L21:     LOAD_GLOBAL             26 (APPROVAL_STATUS_PENDING_APPLY)

339   L22:     LOAD_CONST              19 ('apply_status')
               LOAD_FAST_BORROW        11 (apply_status)

340            LOAD_CONST              12 ('dry_run')
               LOAD_FAST_BORROW        12 (dry_run)

341            LOAD_CONST              13 ('applied')
               LOAD_FAST_BORROW        13 (applied)

342            LOAD_CONST              14 ('error_code')
               LOAD_FAST_BORROW        14 (error_code)

343            LOAD_CONST               9 ('allowed_patch')
               LOAD_FAST_BORROW         8 (allowed_patch)

344            LOAD_CONST              16 ('evidence')
               LOAD_FAST_BORROW        16 (evidence)

345            LOAD_CONST              17 ('warnings')
               LOAD_FAST_BORROW        17 (warnings)

331            BUILD_MAP               14
               STORE_FAST              18 (row)

347            LOAD_GLOBAL             29 (_strip_forbidden + NULL)
               LOAD_FAST_BORROW        18 (row)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "app\services\memory\rollout_ledger.py", line 354>:
354           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object validate_ledger_row at 0x0000018C17D516D0, file "app\services\memory\rollout_ledger.py", line 354>:
354            RESUME                   0

360            BUILD_LIST               0
               STORE_FAST               1 (errors)

361            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (row)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L1)
               NOT_TAKEN

362            LOAD_CONST               1 ('row_must_be_dict')
               BUILD_LIST               1
               RETURN_VALUE

364    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               2 ('approval_id')
               CALL                     1
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       30 (to L2)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (row)
               LOAD_CONST               2 ('approval_id')
               BINARY_OP               26 ([])
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L3)
               NOT_TAKEN

365    L2:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               3 ('missing_approval_id')
               CALL                     1
               POP_TOP

366    L3:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               4 ('brokerage_id')
               CALL                     1
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       30 (to L4)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (row)
               LOAD_CONST               4 ('brokerage_id')
               BINARY_OP               26 ([])
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L5)
               NOT_TAKEN

367    L4:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               5 ('missing_brokerage_id')
               CALL                     1
               POP_TOP

368    L5:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               6 ('operator_id')
               CALL                     1
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       30 (to L6)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (row)
               LOAD_CONST               6 ('operator_id')
               BINARY_OP               26 ([])
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L7)
               NOT_TAKEN

369    L6:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               7 ('missing_operator_id')
               CALL                     1
               POP_TOP

370    L7:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               8 ('plan_hash')
               CALL                     1
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       30 (to L8)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (row)
               LOAD_CONST               8 ('plan_hash')
               BINARY_OP               26 ([])
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L9)
               NOT_TAKEN

371    L8:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               9 ('missing_plan_hash')
               CALL                     1
               POP_TOP

373    L9:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              10 ('recommended_action')
               CALL                     1
               STORE_FAST               2 (action)

374            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (action)
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       12 (to L10)
               NOT_TAKEN
               LOAD_FAST_BORROW         2 (action)
               LOAD_GLOBAL             12 (VALID_ACTIONS)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       22 (to L11)
               NOT_TAKEN

375   L10:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              11 ('invalid_recommended_action:')
               LOAD_FAST_BORROW         2 (action)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

377   L11:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              12 ('approval_status')
               CALL                     1
               STORE_FAST               3 (approval_status)

378            LOAD_FAST_BORROW         3 (approval_status)
               LOAD_GLOBAL             14 (VALID_APPROVAL_STATUSES)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       22 (to L12)
               NOT_TAKEN

379            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              13 ('invalid_approval_status:')
               LOAD_FAST_BORROW         3 (approval_status)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

381   L12:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              14 ('apply_status')
               CALL                     1
               STORE_FAST               4 (apply_status)

382            LOAD_FAST_BORROW         4 (apply_status)
               LOAD_GLOBAL             16 (VALID_APPLY_STATUSES)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       22 (to L13)
               NOT_TAKEN

383            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              15 ('invalid_apply_status:')
               LOAD_FAST_BORROW         4 (apply_status)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

385   L13:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              16 ('dry_run')
               CALL                     1
               LOAD_GLOBAL             18 (bool)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L14)
               NOT_TAKEN

386            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              17 ('invalid_dry_run')
               CALL                     1
               POP_TOP

387   L14:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              18 ('applied')
               CALL                     1
               LOAD_GLOBAL             18 (bool)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L15)
               NOT_TAKEN

388            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              19 ('invalid_applied')
               CALL                     1
               POP_TOP

392   L15:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              18 ('applied')
               CALL                     1
               LOAD_CONST              20 (True)
               IS_OP                    0 (is)
               POP_JUMP_IF_FALSE       82 (to L17)
               NOT_TAKEN

393            LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              16 ('dry_run')
               CALL                     1
               LOAD_CONST              20 (True)
               IS_OP                    0 (is)
               POP_JUMP_IF_FALSE       18 (to L16)
               NOT_TAKEN

394            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              21 ('applied_but_dry_run')
               CALL                     1
               POP_TOP

395   L16:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              14 ('apply_status')
               CALL                     1
               LOAD_GLOBAL             20 (APPLY_STATUS_APPLIED)
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE       18 (to L17)
               NOT_TAKEN

396            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              22 ('applied_but_wrong_apply_status')
               CALL                     1
               POP_TOP

398   L17:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              23 ('target_enabled')
               CALL                     1
               STORE_FAST               5 (target_enabled)

399            LOAD_FAST_BORROW         5 (target_enabled)
               POP_JUMP_IF_NONE        40 (to L18)
               NOT_TAKEN
               LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         5 (target_enabled)
               LOAD_GLOBAL             18 (bool)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L18)
               NOT_TAKEN

400            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              24 ('invalid_target_enabled')
               CALL                     1
               POP_TOP

402   L18:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              25 ('error_code')
               CALL                     1
               STORE_FAST               6 (error_code)

403            LOAD_FAST_BORROW         6 (error_code)
               POP_JUMP_IF_NONE        74 (to L20)
               NOT_TAKEN

404            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         6 (error_code)
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        19 (to L19)
               NOT_TAKEN

405            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              26 ('invalid_error_code_type')
               CALL                     1
               POP_TOP
               JUMP_FORWARD            33 (to L20)

406   L19:     LOAD_GLOBAL             23 (len + NULL)
               LOAD_FAST_BORROW         6 (error_code)
               CALL                     1
               LOAD_SMALL_INT         128
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE       18 (to L20)
               NOT_TAKEN

407            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              27 ('error_code_too_long')
               CALL                     1
               POP_TOP

410   L20:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              28 ('allowed_patch')
               CALL                     1
               STORE_FAST               7 (patch)

411            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         7 (patch)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        20 (to L21)
               NOT_TAKEN

412            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              29 ('invalid_allowed_patch_type')
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_FORWARD           284 (to L25)

413   L21:     LOAD_FAST_BORROW         7 (patch)
               TO_BOOL
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      276 (to L25)
               NOT_TAKEN

414            LOAD_GLOBAL             25 (sorted + NULL)
               LOAD_CONST              30 (<code object <genexpr> at 0x0000018C180C4140, file "app\services\memory\rollout_ledger.py", line 414>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         7 (patch)
               LOAD_ATTR               27 (keys + NULL|self)
               CALL                     0
               GET_ITER
               CALL                     0
               CALL                     1
               STORE_FAST               8 (extra_top)

415            LOAD_FAST_BORROW         8 (extra_top)
               TO_BOOL
               POP_JUMP_IF_FALSE       40 (to L22)
               NOT_TAKEN

416            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)

417            LOAD_CONST              31 ('allowed_patch_has_disallowed_top_keys:')
               LOAD_CONST              32 (',')
               LOAD_ATTR               29 (join + NULL|self)
               LOAD_FAST_BORROW         8 (extra_top)
               CALL                     1
               BINARY_OP                0 (+)

416            CALL                     1
               POP_TOP

419   L22:     LOAD_FAST_BORROW         7 (patch)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              33 ('features')
               CALL                     1
               STORE_FAST               9 (features)

420            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         9 (features)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        19 (to L23)
               NOT_TAKEN

421            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              34 ('allowed_patch_features_must_be_dict')
               CALL                     1
               POP_TOP
               JUMP_FORWARD           139 (to L25)

423   L23:     LOAD_GLOBAL             25 (sorted + NULL)
               LOAD_CONST              35 (<code object <genexpr> at 0x0000018C180C4250, file "app\services\memory\rollout_ledger.py", line 423>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         9 (features)
               LOAD_ATTR               27 (keys + NULL|self)
               CALL                     0
               GET_ITER
               CALL                     0
               CALL                     1
               STORE_FAST              10 (extra_feat)

424            LOAD_FAST_BORROW        10 (extra_feat)
               TO_BOOL
               POP_JUMP_IF_FALSE       40 (to L24)
               NOT_TAKEN

425            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)

426            LOAD_CONST              36 ('allowed_patch_features_has_disallowed_keys:')
               LOAD_CONST              32 (',')
               LOAD_ATTR               29 (join + NULL|self)
               LOAD_FAST_BORROW        10 (extra_feat)
               CALL                     1
               BINARY_OP                0 (+)

425            CALL                     1
               POP_TOP

428   L24:     LOAD_FAST_BORROW         9 (features)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_GLOBAL             30 (_ALLOWED_FLAG)
               CALL                     1
               STORE_FAST              11 (flag)

429            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW        11 (flag)
               LOAD_GLOBAL             18 (bool)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L25)
               NOT_TAKEN

430            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              37 ('allowed_patch_flag_must_be_bool')
               CALL                     1
               POP_TOP

433   L25:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              38 ('evidence')
               CALL                     1
               STORE_FAST              12 (evidence)

434            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW        12 (evidence)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        19 (to L26)
               NOT_TAKEN

435            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              39 ('invalid_evidence_type')
               CALL                     1
               POP_TOP
               JUMP_FORWARD            56 (to L30)

437   L26:     LOAD_FAST_BORROW        12 (evidence)
               LOAD_ATTR               27 (keys + NULL|self)
               CALL                     0
               GET_ITER
      L27:     FOR_ITER                36 (to L29)
               STORE_FAST              13 (k)

438            LOAD_FAST_BORROW        13 (k)
               LOAD_GLOBAL             32 (_SAFE_EVIDENCE_FIELDS)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_TRUE         3 (to L28)
               NOT_TAKEN
               JUMP_BACKWARD           16 (to L27)

439   L28:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              40 ('evidence_has_disallowed_key:')
               LOAD_FAST_BORROW        13 (k)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

440            POP_TOP
               JUMP_FORWARD             2 (to L30)

437   L29:     END_FOR
               POP_ITER

443   L30:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              41 ('warnings')
               CALL                     1
               STORE_FAST              14 (warnings)

444            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW        14 (warnings)
               LOAD_GLOBAL             34 (list)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L31)
               NOT_TAKEN

445            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              42 ('invalid_warnings_type')
               CALL                     1
               POP_TOP

448   L31:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR               27 (keys + NULL|self)
               CALL                     0
               GET_ITER
      L32:     FOR_ITER                37 (to L34)
               STORE_FAST              13 (k)

449            LOAD_FAST_BORROW        13 (k)
               LOAD_GLOBAL             36 (_FORBIDDEN_KEYS)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L33)
               NOT_TAKEN
               JUMP_BACKWARD           16 (to L32)

450   L33:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              43 ('row_has_forbidden_key:')
               LOAD_FAST_BORROW        13 (k)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

451            POP_TOP

453            LOAD_FAST_BORROW         1 (errors)
               RETURN_VALUE

448   L34:     END_FOR
               POP_ITER

453            LOAD_FAST_BORROW         1 (errors)
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180C4140, file "app\services\memory\rollout_ledger.py", line 414>:
 414           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                15 (to L5)
               STORE_FAST_LOAD_FAST    17 (k, k)
               LOAD_CONST               0 ('features')
               COMPARE_OP             119 (bool(!=))
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L2)
       L4:     LOAD_FAST_BORROW         1 (k)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           17 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C180C4250, file "app\services\memory\rollout_ledger.py", line 423>:
 423           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                19 (to L5)
               STORE_FAST_LOAD_FAST    17 (k, k)
               LOAD_GLOBAL              0 (_ALLOWED_FLAG)
               COMPARE_OP             119 (bool(!=))
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           15 (to L2)
       L4:     LOAD_FAST_BORROW         1 (k)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           21 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app\services\memory\rollout_ledger.py", line 460>:
460           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object record_rollout_ledger at 0x0000018C17EE1CC0, file "app\services\memory\rollout_ledger.py", line 460>:
 460            RESUME                   0

 474            LOAD_GLOBAL              1 (ledger_row_from_apply_report + NULL)
                LOAD_FAST_BORROW         0 (report)
                CALL                     1
                STORE_FAST               1 (row)

 475            LOAD_FAST_BORROW         1 (row)
                POP_JUMP_IF_NOT_NONE     7 (to L1)
                NOT_TAKEN

 477            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('skipped')

 478            LOAD_CONST               4 ('reason')
                LOAD_CONST               5 ('unrecognised_apply_report_shape')

 476            BUILD_MAP                2
                RETURN_VALUE

 481    L1:     LOAD_GLOBAL              3 (validate_ledger_row + NULL)
                LOAD_FAST_BORROW         1 (row)
                CALL                     1
                STORE_FAST               2 (errors)

 482            LOAD_FAST_BORROW         2 (errors)
                TO_BOOL
                POP_JUMP_IF_FALSE       16 (to L2)
                NOT_TAKEN

 484            LOAD_CONST               2 ('status')
                LOAD_CONST               6 ('failed')

 485            LOAD_CONST               7 ('errors')
                LOAD_GLOBAL              5 (list + NULL)
                LOAD_FAST_BORROW         2 (errors)
                CALL                     1

 483            BUILD_MAP                2
                RETURN_VALUE

 488    L2:     NOP

 489    L3:     LOAD_GLOBAL              7 (_get_db + NULL)
                CALL                     0
                STORE_FAST               3 (db)

 490            LOAD_FAST_BORROW         3 (db)
                LOAD_ATTR                9 (table + NULL|self)
                LOAD_GLOBAL             10 (_TABLE)
                CALL                     1
                LOAD_ATTR               13 (insert + NULL|self)
                LOAD_FAST_BORROW         1 (row)
                CALL                     1
                LOAD_ATTR               15 (execute + NULL|self)
                CALL                     0
                STORE_FAST               4 (result)

 491            LOAD_GLOBAL             17 (getattr + NULL)
                LOAD_FAST_BORROW         4 (result)
                LOAD_CONST               8 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
        L4:     NOT_TAKEN
        L5:     POP_TOP
                BUILD_LIST               0
        L6:     STORE_FAST               5 (inserted)

 493            LOAD_CONST               2 ('status')
                LOAD_CONST               9 ('ok')

 494            LOAD_CONST              10 ('ledger_row')
                LOAD_FAST_BORROW         5 (inserted)
                TO_BOOL
                POP_JUMP_IF_FALSE       11 (to L10)
        L7:     NOT_TAKEN
        L8:     LOAD_FAST_BORROW         5 (inserted)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])

 492            BUILD_MAP                2
        L9:     RETURN_VALUE

 494   L10:     LOAD_FAST                1 (row)

 492            BUILD_MAP                2
       L11:     RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 496            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      101 (to L17)
                NOT_TAKEN
                STORE_FAST               6 (e)

 497   L13:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 498            LOAD_CONST              11 ('record_rollout_ledger insert failed (non-critical) | brokerage=')

 499            LOAD_FAST                1 (row)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              13 (' | error_type=')

 500            LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE

 498            BUILD_STRING             4

 497            CALL                     1
                POP_TOP

 503            LOAD_CONST               2 ('status')
                LOAD_CONST               6 ('failed')

 504            LOAD_CONST               7 ('errors')
                LOAD_CONST              14 ('db_write_failed:')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 502            BUILD_MAP                2
       L14:     SWAP                     2
       L15:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --   L16:     LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 496   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L12 [0]
  L5 to L7 -> L12 [0]
  L8 to L9 -> L12 [0]
  L10 to L11 -> L12 [0]
  L12 to L13 -> L18 [1] lasti
  L13 to L14 -> L16 [1] lasti
  L14 to L15 -> L18 [1] lasti
  L16 to L18 -> L18 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app\services\memory\rollout_ledger.py", line 512>:
512           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

513           LOAD_CONST               2 ('str')

512           LOAD_CONST               3 ('limit')

515           LOAD_CONST               4 ('int')

512           LOAD_CONST               5 ('return')

516           LOAD_CONST               6 ('List[Dict[str, Any]]')

512           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object list_rollout_history_for_brokerage at 0x0000018C17D81A00, file "app\services\memory\rollout_ledger.py", line 512>:
 512            RESUME                   0

 523            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        24 (to L2)
                NOT_TAKEN

 524    L1:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 525            LOAD_CONST               1 ('list_rollout_history_for_brokerage dropped | reason=missing_brokerage_id')

 524            CALL                     1
                POP_TOP

 528            BUILD_LIST               0
                RETURN_VALUE

 530    L2:     LOAD_GLOBAL             11 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         1 (limit)
                CALL                     1
                STORE_FAST               2 (capped)

 531            NOP

 532    L3:     LOAD_GLOBAL             13 (_get_db + NULL)
                CALL                     0
                STORE_FAST               3 (db)

 534            LOAD_FAST_BORROW         3 (db)
                LOAD_ATTR               15 (table + NULL|self)
                LOAD_GLOBAL             16 (_TABLE)
                CALL                     1

 535            LOAD_ATTR               19 (select + NULL|self)
                LOAD_CONST               2 ('*')
                CALL                     1

 536            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST               3 ('brokerage_id')
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                CALL                     2

 537            LOAD_ATTR               23 (order + NULL|self)
                LOAD_CONST               4 ('created_at')
                LOAD_CONST               5 (True)
                LOAD_CONST               6 (('desc',))
                CALL_KW                  2

 538            LOAD_ATTR               25 (limit + NULL|self)
                LOAD_FAST_BORROW         2 (capped)
                CALL                     1

 539            LOAD_ATTR               27 (execute + NULL|self)
                CALL                     0

 533            STORE_FAST               4 (result)

 541            LOAD_GLOBAL             29 (list + NULL)
                LOAD_GLOBAL             31 (getattr + NULL)
                LOAD_FAST_BORROW         4 (result)
                LOAD_CONST               7 ('data')
                LOAD_CONST               8 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L4:     CALL                     1
        L5:     RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 542            LOAD_GLOBAL             32 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       59 (to L11)
                NOT_TAKEN
                STORE_FAST               5 (e)

 543    L7:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 544            LOAD_CONST               9 ('list_rollout_history_for_brokerage failed (non-critical) | brokerage=')

 545            LOAD_FAST                0 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST              10 (' | error_type=')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE

 544            BUILD_STRING             4

 543            CALL                     1
                POP_TOP

 547            BUILD_LIST               0
        L8:     SWAP                     2
        L9:     POP_EXCEPT
                LOAD_CONST               8 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RETURN_VALUE

  --   L10:     LOAD_CONST               8 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 542   L11:     RERAISE                  0

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L6 [0]
  L6 to L7 -> L12 [1] lasti
  L7 to L8 -> L10 [1] lasti
  L8 to L9 -> L12 [1] lasti
  L10 to L12 -> L12 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app\services\memory\rollout_ledger.py", line 550>:
550           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('operator_id')

551           LOAD_CONST               2 ('str')

550           LOAD_CONST               3 ('limit')

553           LOAD_CONST               4 ('int')

550           LOAD_CONST               5 ('return')

554           LOAD_CONST               6 ('List[Dict[str, Any]]')

550           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object list_rollout_history_for_operator at 0x0000018C17D7D400, file "app\services\memory\rollout_ledger.py", line 550>:
 550            RESUME                   0

 563            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (operator_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (operator_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        24 (to L2)
                NOT_TAKEN

 564    L1:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 565            LOAD_CONST               1 ('list_rollout_history_for_operator dropped | reason=missing_operator_id')

 564            CALL                     1
                POP_TOP

 568            BUILD_LIST               0
                RETURN_VALUE

 570    L2:     LOAD_GLOBAL             11 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         1 (limit)
                CALL                     1
                STORE_FAST               2 (capped)

 571            NOP

 572    L3:     LOAD_GLOBAL             13 (_get_db + NULL)
                CALL                     0
                STORE_FAST               3 (db)

 574            LOAD_FAST_BORROW         3 (db)
                LOAD_ATTR               15 (table + NULL|self)
                LOAD_GLOBAL             16 (_TABLE)
                CALL                     1

 575            LOAD_ATTR               19 (select + NULL|self)
                LOAD_CONST               2 ('*')
                CALL                     1

 576            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST               3 ('operator_id')
                LOAD_FAST_BORROW         0 (operator_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                CALL                     2

 577            LOAD_ATTR               23 (order + NULL|self)
                LOAD_CONST               4 ('created_at')
                LOAD_CONST               5 (True)
                LOAD_CONST               6 (('desc',))
                CALL_KW                  2

 578            LOAD_ATTR               25 (limit + NULL|self)
                LOAD_FAST_BORROW         2 (capped)
                CALL                     1

 579            LOAD_ATTR               27 (execute + NULL|self)
                CALL                     0

 573            STORE_FAST               4 (result)

 581            LOAD_GLOBAL             29 (list + NULL)
                LOAD_GLOBAL             31 (getattr + NULL)
                LOAD_FAST_BORROW         4 (result)
                LOAD_CONST               7 ('data')
                LOAD_CONST               8 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L4:     CALL                     1
        L5:     RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 582            LOAD_GLOBAL             32 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       59 (to L11)
                NOT_TAKEN
                STORE_FAST               5 (e)

 583    L7:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 584            LOAD_CONST               9 ('list_rollout_history_for_operator failed (non-critical) | operator=')

 585            LOAD_FAST                0 (operator_id)
                FORMAT_SIMPLE
                LOAD_CONST              10 (' | error_type=')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE

 584            BUILD_STRING             4

 583            CALL                     1
                POP_TOP

 587            BUILD_LIST               0
        L8:     SWAP                     2
        L9:     POP_EXCEPT
                LOAD_CONST               8 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RETURN_VALUE

  --   L10:     LOAD_CONST               8 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 582   L11:     RERAISE                  0

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L6 [0]
  L6 to L7 -> L12 [1] lasti
  L7 to L8 -> L10 [1] lasti
  L8 to L9 -> L12 [1] lasti
  L10 to L12 -> L12 [1] lasti
```
