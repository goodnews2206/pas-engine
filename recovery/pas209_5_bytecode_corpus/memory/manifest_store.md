# memory/manifest_store

- **pyc:** `app\services\memory\__pycache__\manifest_store.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/manifest_store.py`
- **co_filename (from bytecode):** `app\services\memory\manifest_store.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144N — Signed manifest persistence.

Append-only store for PAS144L operator-approval manifests. Pairs with:
  * PAS144L — build_approval_manifest (the in-memory artefact)
  * PAS144M — rollout_ledger          (apply-side audit)
  * scripts/migrate_v13_memory_rollout_manifests.sql (the additive table)

PAS144M records *what happened*; PAS144N records *what was approved*.
Together they make every rollout decision reconstructible: the ledger
points at an approval_id, this store answers "what did the operator
actually sign?"

Hard contract — every public helper here:
  1. Validates the manifest via PAS144L's
     ``approval.validate_approval_manifest`` before writing. Invalid
     manifests are NEVER persisted.
  2. Requires tenant scope on tenant readers. ``brokerage_id`` is
     mandatory on the brokerage list helper; ``operator_id`` is
     mandatory on the operator list helper.
  3. ``get_manifest`` accepts an optional ``brokerage_id`` filter.
     When provided, it ALWAYS filters by brokerage_id; an unscoped
     fetch is reserved for admin/ops and must be deliberate at the
     call site.
  4. Caller-supplied ``limit`` is clamped to ``MAX_HISTORY_LIMIT``.
  5. There is NO unscoped brokerage list helper. Cross-tenant reads
     flow only through the operator-list helper or the explicit
     plan-hash lookup (``list_manifests_by_plan_hash`` is intentionally
     NOT exposed in PAS144N — adding it requires an explicit follow-up
     phase).
  6. Never raises on Supabase failure: returns a structured failure
     dict (writer) or empty list / None (readers).
  7. ``allowed_patch`` is constrained to the same single-flag shape
     as PAS144L. No widening here.
  8. Raw memory / prompt / transcript values cannot enter the
     persisted row — the evidence whitelist is closed, the validator
     refuses any unknown evidence key, and the writer re-strips
     forbidden top-level keys as defence-in-depth.

Public surface (deliberately tiny):
  - manifest_row_from_manifest(manifest)        -> dict | None
  - validate_manifest_row(row)                  -> list[str]
  - record_manifest(manifest)                   -> dict
  - get_manifest(approval_id, brokerage_id=None) -> dict | None
  - list_manifests_for_brokerage(
        brokerage_id, *, limit=50)              -> list[dict]
  - list_manifests_for_operator(
        operator_id, *, limit=50)               -> list[dict]

PAS144N explicitly does NOT build:
  * autonomous rollout (every manifest is operator-signed by contract);
  * automatic feature-flag changes;
  * widened config patching;
  * embeddings / vector helpers;
  * cross-tenant tenant-facing read paths;
  * a public plan-hash lookup helper.
```

## Imports

``, `Any`, `Dict`, `List`, `Optional`, `VALID_ACTIONS`, `__future__`, `annotations`, `app.db.supabase_client`, `approval`, `get_supabase`, `logging`, `rollout`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_limit`, `_derive_target_enabled`, `_get_db`, `_normalise_allowed_patch`, `_strip_forbidden`, `get_manifest`, `list_manifests_for_brokerage`, `list_manifests_for_operator`, `manifest_row_from_manifest`, `record_manifest`, `validate_manifest_row`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS144N — Signed manifest persistence.\n\nAppend-only store for PAS144L operator-approval manifests. Pairs with:\n  * PAS144L — build_approval_manifest (the in-memory artefact)\n  * PAS144M — rollout_ledger          (apply-side audit)\n  * scripts/migrate_v13_memory_rollout_manifests.sql (the additive table)\n\nPAS144M records *what happened*; PAS144N records *what was approved*.\nTogether they make every rollout decision reconstructible: the ledger\npoints at an approval_id, this store answers "what did the operator\nactually sign?"\n\nHard contract — every public helper here:\n  1. Validates the manifest via PAS144L\'s\n     ``approval.validate_approval_manifest`` before writing. Invalid\n     manifests are NEVER persisted.\n  2. Requires tenant scope on tenant readers. ``brokerage_id`` is\n     mandatory on the brokerage list helper; ``operator_id`` is\n     mandatory on the operator list helper.\n  3. ``get_manifest`` accepts an optional ``brokerage_id`` filter.\n     When provided, it ALWAYS filters by brokerage_id; an unscoped\n     fetch is reserved for admin/ops and must be deliberate at the\n     call site.\n  4. Caller-supplied ``limit`` is clamped to ``MAX_HISTORY_LIMIT``.\n  5. There is NO unscoped brokerage list helper. Cross-tenant reads\n     flow only through the operator-list helper or the explicit\n     plan-hash lookup (``list_manifests_by_plan_hash`` is intentionally\n     NOT exposed in PAS144N — adding it requires an explicit follow-up\n     phase).\n  6. Never raises on Supabase failure: returns a structured failure\n     dict (writer) or empty list / None (readers).\n  7. ``allowed_patch`` is constrained to the same single-flag shape\n     as PAS144L. No widening here.\n  8. Raw memory / prompt / transcript values cannot enter the\n     persisted row — the evidence whitelist is closed, the validator\n     refuses any unknown evidence key, and the writer re-strips\n     forbidden top-level keys as defence-in-depth.\n\nPublic surface (deliberately tiny):\n  - manifest_row_from_manifest(manifest)        -> dict | None\n  - validate_manifest_row(row)                  -> list[str]\n  - record_manifest(manifest)                   -> dict\n  - get_manifest(approval_id, brokerage_id=None) -> dict | None\n  - list_manifests_for_brokerage(\n        brokerage_id, *, limit=50)              -> list[dict]\n  - list_manifests_for_operator(\n        operator_id, *, limit=50)               -> list[dict]\n\nPAS144N explicitly does NOT build:\n  * autonomous rollout (every manifest is operator-signed by contract);\n  * automatic feature-flag changes;\n  * widened config patching;\n  * embeddings / vector helpers;\n  * cross-tenant tenant-facing read paths;\n  * a public plan-hash lookup helper.\n'
- 'pas.memory.manifest_store'
- 'pas_memory_rollout_manifests'
- 'memory_injection_enabled'
- 'limit'
- 'Lazy Supabase resolver. Mirrors review.py / queries.py /\nrollout_ledger.py so unit tests can patch\n``app.db.supabase_client.get_supabase``.'
- 'Any'
- 'return'
- 'int'
- 'patch'
- 'Dict[str, Any]'
- 'Return a defensively-trimmed allowed_patch.\n\nAccepts only:\n  * empty dict — recorded as {};\n  * {"features": {"memory_injection_enabled": <bool>}} verbatim.\n\nAnything else collapses to {} so a regressed upstream cannot leak\narbitrary keys into the row.\n'
- 'features'
- 'allowed_patch'
- 'Optional[bool]'
- 'row'
- 'Drop any forbidden raw-payload keys from the top level of a row.\n\nDefence-in-depth: the builder never reads such keys, but if a\ncaller hand-rolls a row dict (or a future regression sneaks a key\nin), this strip ensures the manifest insert never carries one.\n'
- 'manifest'
- 'Optional[Dict[str, Any]]'
- "Build a structural row from a PAS144L manifest.\n\nThe manifest is expected to be the dict produced by\n:func:`approval.build_approval_manifest`. Returns ``None`` when\nthe manifest is structurally unusable. Never raises.\n\nThe returned dict carries the manifest envelope's identity fields\nplus the full plan + manifest JSONB blobs (so a future audit can\nrecompute the plan_hash and verify nothing has been tampered with).\nRaw memory / prompt / transcript values cannot enter because:\n  1. PAS144K's evidence whitelist already filters the plan;\n  2. PAS144L's manifest envelope carries no plan-side text;\n  3. ``_strip_forbidden`` removes any bolted-on forbidden top-\n     level key as the final step.\n"
- 'approval_id'
- 'operator_id'
- 'plan_hash'
- 'approval_status'
- 'approved_at'
- 'operator_reason'
- 'plan'
- 'brokerage_id'
- 'recommended_action'
- 'target_enabled'
- 'List[str]'
- 'Return a list of human-readable blockers for a manifest row.\n\nPure. Never raises. Empty list ⇒ row is safe to insert.\n\nLayered checks:\n  * envelope identity fields present and well-typed;\n  * recommended_action in the closed set;\n  * approval_status in ``VALID_APPROVAL_STATUSES``;\n  * allowed_patch is exactly the documented shape or empty;\n  * target_enabled is bool or None;\n  * the embedded manifest passes PAS144L\n    ``validate_approval_manifest`` (catches plan_hash drift,\n    plan-shape regressions, etc.);\n  * no forbidden top-level raw-payload keys on the row.\n'
- 'row_must_be_dict'
- 'missing_approval_id'
- 'missing_brokerage_id'
- 'missing_operator_id'
- 'missing_plan_hash'
- 'missing_approved_at'
- 'invalid_recommended_action:'
- 'invalid_approval_status:'
- 'invalid_target_enabled'
- 'invalid_allowed_patch_type'
- 'allowed_patch_has_disallowed_top_keys:'
- 'allowed_patch_features_must_be_dict'
- 'allowed_patch_features_has_disallowed_keys:'
- 'allowed_patch_flag_must_be_bool'
- 'invalid_plan_type'
- 'invalid_manifest_type'
- 'manifest:'
- 'evidence'
- 'plan_evidence_has_disallowed_key:'
- 'row_has_forbidden_key:'
- 'Persist a signed PAS144L manifest. Never raises.\n\nPipeline:\n  1. Build the row via :func:`manifest_row_from_manifest`. A\n     ``None`` return means the manifest is structurally unusable\n     → ``{"status": "skipped", ...}``.\n  2. Run :func:`validate_manifest_row` (which internally runs\n     PAS144L\'s validator). Any blocker yields\n     ``{"status": "failed", "errors": [...]}``.\n  3. INSERT into ``pas_memory_rollout_manifests``. Supabase\n     failure yields a structured ``{"status": "failed", "errors":\n     ["db_write_failed:..."]}`` — never an exception.\n'
- 'status'
- 'skipped'
- 'reason'
- 'unrecognised_manifest_shape'
- 'failed'
- 'errors'
- 'data'
- 'record_manifest insert failed (non-critical) | brokerage='
- ' | error_type='
- 'db_write_failed:'
- 'str'
- 'Optional[str]'
- 'Fetch a single manifest row by ``approval_id``.\n\nWhen ``brokerage_id`` is supplied, the query is filtered to that\ntenant — a cross-tenant ``approval_id`` will simply not be found\nand ``None`` is returned. Admin/ops callers may pass\n``brokerage_id=None`` to look up by approval_id alone; that call\nsite MUST be deliberate (the unscoped form is not used by any\ntenant-facing route).\n\nReturns ``None`` on missing approval_id, on Supabase failure, or\nwhen no row matches. Never raises.\n'
- 'get_manifest dropped | reason=invalid_approval_id'
- 'get_manifest dropped | reason=invalid_brokerage_id'
- 'get_manifest failed (non-critical) | approval_id='
- 'List[Dict[str, Any]]'
- 'Return manifest rows for ``brokerage_id`` newest-first.\n\nTenant-scoped: missing/invalid ``brokerage_id`` returns ``[]``.\nCaller-supplied ``limit`` is clamped to ``MAX_HISTORY_LIMIT``.\nNever raises on Supabase failure.\n'
- 'list_manifests_for_brokerage dropped | reason=missing_brokerage_id'
- 'created_at'
- 'list_manifests_for_brokerage failed (non-critical) | brokerage='
- 'Return manifest rows for ``operator_id`` newest-first.\n\nOperator-scoped (intentionally cross-tenant — operators may\nlegally oversee multiple brokerages). Never exposed via tenant-\nfacing HTTP routes. Missing/invalid ``operator_id`` returns ``[]``.\nCaller-supplied ``limit`` is clamped to ``MAX_HISTORY_LIMIT``.\nNever raises on Supabase failure.\n'
- 'list_manifests_for_operator dropped | reason=missing_operator_id'
- 'list_manifests_for_operator failed (non-critical) | operator='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS144N — Signed manifest persistence.\n\nAppend-only store for PAS144L operator-approval manifests. Pairs with:\n  * PAS144L — build_approval_manifest (the in-memory artefact)\n  * PAS144M — rollout_ledger          (apply-side audit)\n  * scripts/migrate_v13_memory_rollout_manifests.sql (the additive table)\n\nPAS144M records *what happened*; PAS144N records *what was approved*.\nTogether they make every rollout decision reconstructible: the ledger\npoints at an approval_id, this store answers "what did the operator\nactually sign?"\n\nHard contract — every public helper here:\n  1. Validates the manifest via PAS144L\'s\n     ``approval.validate_approval_manifest`` before writing. Invalid\n     manifests are NEVER persisted.\n  2. Requires tenant scope on tenant readers. ``brokerage_id`` is\n     mandatory on the brokerage list helper; ``operator_id`` is\n     mandatory on the operator list helper.\n  3. ``get_manifest`` accepts an optional ``brokerage_id`` filter.\n     When provided, it ALWAYS filters by brokerage_id; an unscoped\n     fetch is reserved for admin/ops and must be deliberate at the\n     call site.\n  4. Caller-supplied ``limit`` is clamped to ``MAX_HISTORY_LIMIT``.\n  5. There is NO unscoped brokerage list helper. Cross-tenant reads\n     flow only through the operator-list helper or the explicit\n     plan-hash lookup (``list_manifests_by_plan_hash`` is intentionally\n     NOT exposed in PAS144N — adding it requires an explicit follow-up\n     phase).\n  6. Never raises on Supabase failure: returns a structured failure\n     dict (writer) or empty list / None (readers).\n  7. ``allowed_patch`` is constrained to the same single-flag shape\n     as PAS144L. No widening here.\n  8. Raw memory / prompt / transcript values cannot enter the\n     persisted row — the evidence whitelist is closed, the validator\n     refuses any unknown evidence key, and the writer re-strips\n     forbidden top-level keys as defence-in-depth.\n\nPublic surface (deliberately tiny):\n  - manifest_row_from_manifest(manifest)        -> dict | None\n  - validate_manifest_row(row)                  -> list[str]\n  - record_manifest(manifest)                   -> dict\n  - get_manifest(approval_id, brokerage_id=None) -> dict | None\n  - list_manifests_for_brokerage(\n        brokerage_id, *, limit=50)              -> list[dict]\n  - list_manifests_for_operator(\n        operator_id, *, limit=50)               -> list[dict]\n\nPAS144N explicitly does NOT build:\n  * autonomous rollout (every manifest is operator-signed by contract);\n  * automatic feature-flag changes;\n  * widened config patching;\n  * embeddings / vector helpers;\n  * cross-tenant tenant-facing read paths;\n  * a public plan-hash lookup helper.\n')
              STORE_NAME               0 (__doc__)

 59           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 61           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 62           LOAD_SMALL_INT           0
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

 64           LOAD_SMALL_INT           1
              LOAD_CONST               4 (('approval',))
              IMPORT_NAME              9
              IMPORT_FROM             10 (approval)
              STORE_NAME              11 (approval_mod)
              POP_TOP

 65           LOAD_SMALL_INT           1
              LOAD_CONST               5 (('VALID_ACTIONS',))
              IMPORT_NAME             12 (rollout)
              IMPORT_FROM             13 (VALID_ACTIONS)
              STORE_NAME              13 (VALID_ACTIONS)
              POP_TOP

 67           LOAD_NAME                3 (logging)
              LOAD_ATTR               28 (getLogger)
              PUSH_NULL
              LOAD_CONST               6 ('pas.memory.manifest_store')
              CALL                     1
              STORE_NAME              15 (logger)

 74           LOAD_CONST               7 ('pas_memory_rollout_manifests')
              STORE_NAME              16 (_TABLE)

 78           LOAD_SMALL_INT         200
              STORE_NAME              17 (MAX_HISTORY_LIMIT)

 79           LOAD_SMALL_INT          50
              STORE_NAME              18 (DEFAULT_HISTORY_LIMIT)

 81           LOAD_NAME               11 (approval_mod)
              LOAD_ATTR               38 (APPROVAL_STATUS_PENDING_APPLY)
              STORE_NAME              19 (APPROVAL_STATUS_PENDING_APPLY)

 82           LOAD_NAME               20 (frozenset)
              PUSH_NULL
              LOAD_NAME               19 (APPROVAL_STATUS_PENDING_APPLY)
              BUILD_SET                1
              CALL                     1
              STORE_NAME              21 (VALID_APPROVAL_STATUSES)

 85           LOAD_CONST               8 ('memory_injection_enabled')
              STORE_NAME              22 (_ALLOWED_FLAG)

 90           LOAD_NAME               20 (frozenset)
              PUSH_NULL
              BUILD_SET                0
              LOAD_CONST              31 (frozenset({'provider_failure_rate_without_memory', 'memory_succeeded_calls', 'health_status', 'rollout_recommendation', 'total_calls', 'callback_rate_with_memory', 'callback_rate_without_memory', 'lift_callback_rate', 'lift_booking_rate', 'booking_rate_without_memory', 'booking_rate_with_memory', 'non_memory_calls', 'provider_failure_rate_with_memory'}))
              SET_UPDATE               1
              CALL                     1
              STORE_NAME              23 (_SAFE_EVIDENCE_FIELDS)

111           LOAD_NAME               20 (frozenset)
              PUSH_NULL
              BUILD_SET                0
              LOAD_CONST              32 (frozenset({'memory_content', 'full_transcript', 'items', 'output_text', 'turns_text', 'formatted', 'utterances', 'raw_transcript', 'input_text', 'transcript', 'base_prompt', 'prompt', 'injected_prompt', 'messages', 'raw_prompt'}))
              SET_UPDATE               1
              CALL                     1
              STORE_NAME              24 (_FORBIDDEN_ROW_KEYS)

124           LOAD_CONST               9 (<code object _get_db at 0x0000018C17FA3960, file "app\services\memory\manifest_store.py", line 124>)
              MAKE_FUNCTION
              STORE_NAME              25 (_get_db)

132           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA2D30, file "app\services\memory\manifest_store.py", line 132>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _clamp_limit at 0x0000018C17FF0F30, file "app\services\memory\manifest_store.py", line 132>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_clamp_limit)

144           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA33C0, file "app\services\memory\manifest_store.py", line 144>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _normalise_allowed_patch at 0x0000018C17CD4970, file "app\services\memory\manifest_store.py", line 144>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_normalise_allowed_patch)

169           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\manifest_store.py", line 169>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _derive_target_enabled at 0x0000018C180608A0, file "app\services\memory\manifest_store.py", line 169>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_derive_target_enabled)

178           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA35A0, file "app\services\memory\manifest_store.py", line 178>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _strip_forbidden at 0x0000018C18039070, file "app\services\memory\manifest_store.py", line 178>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_strip_forbidden)

192           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3780, file "app\services\memory\manifest_store.py", line 192>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object manifest_row_from_manifest at 0x0000018C17E951D0, file "app\services\memory\manifest_store.py", line 192>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (manifest_row_from_manifest)

265           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA2C40, file "app\services\memory\manifest_store.py", line 265>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object validate_manifest_row at 0x0000018C181B0BF0, file "app\services\memory\manifest_store.py", line 265>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (validate_manifest_row)

371           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA2100, file "app\services\memory\manifest_store.py", line 371>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object record_manifest at 0x0000018C17EE1CC0, file "app\services\memory\manifest_store.py", line 371>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (record_manifest)

423           LOAD_CONST              33 ((None,))
              LOAD_CONST              24 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\memory\manifest_store.py", line 423>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object get_manifest at 0x0000018C17F84A20, file "app\services\memory\manifest_store.py", line 423>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              33 (get_manifest)

469           LOAD_CONST              26 ('limit')

472           LOAD_NAME               18 (DEFAULT_HISTORY_LIMIT)

469           BUILD_MAP                1
              LOAD_CONST              27 (<code object __annotate__ at 0x0000018C18024D30, file "app\services\memory\manifest_store.py", line 469>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object list_manifests_for_brokerage at 0x0000018C17E932B0, file "app\services\memory\manifest_store.py", line 469>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              34 (list_manifests_for_brokerage)

507           LOAD_CONST              26 ('limit')

510           LOAD_NAME               18 (DEFAULT_HISTORY_LIMIT)

507           BUILD_MAP                1
              LOAD_CONST              29 (<code object __annotate__ at 0x0000018C18024E30, file "app\services\memory\manifest_store.py", line 507>)
              MAKE_FUNCTION
              LOAD_CONST              30 (<code object list_manifests_for_operator at 0x0000018C17E935F0, file "app\services\memory\manifest_store.py", line 507>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              35 (list_manifests_for_operator)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object _get_db at 0x0000018C17FA3960, file "app\services\memory\manifest_store.py", line 124>:
124           RESUME                   0

128           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('get_supabase',))
              IMPORT_NAME              0 (app.db.supabase_client)
              IMPORT_FROM              1 (get_supabase)
              STORE_FAST               0 (get_supabase)
              POP_TOP

129           LOAD_FAST_BORROW         0 (get_supabase)
              PUSH_NULL
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app\services\memory\manifest_store.py", line 132>:
132           RESUME                   0
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

Disassembly of <code object _clamp_limit at 0x0000018C17FF0F30, file "app\services\memory\manifest_store.py", line 132>:
 132           RESUME                   0

 133           LOAD_FAST_BORROW         0 (limit)
               POP_JUMP_IF_NOT_NONE     7 (to L1)
               NOT_TAKEN

 134           LOAD_GLOBAL              0 (DEFAULT_HISTORY_LIMIT)
               RETURN_VALUE

 135   L1:     NOP

 136   L2:     LOAD_GLOBAL              3 (int + NULL)
               LOAD_FAST_BORROW         0 (limit)
               CALL                     1
               STORE_FAST               1 (n)

 139   L3:     LOAD_FAST                1 (n)
               LOAD_SMALL_INT           0
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 140           LOAD_GLOBAL              0 (DEFAULT_HISTORY_LIMIT)
               RETURN_VALUE

 141   L4:     LOAD_GLOBAL              9 (min + NULL)
               LOAD_FAST                1 (n)
               LOAD_GLOBAL             10 (MAX_HISTORY_LIMIT)
               CALL                     2
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 137           LOAD_GLOBAL              4 (TypeError)
               LOAD_GLOBAL              6 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

 138           LOAD_GLOBAL              0 (DEFAULT_HISTORY_LIMIT)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 137   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app\services\memory\manifest_store.py", line 144>:
144           RESUME                   0
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

Disassembly of <code object _normalise_allowed_patch at 0x0000018C17CD4970, file "app\services\memory\manifest_store.py", line 144>:
 144            RESUME                   0

 154            LOAD_GLOBAL              1 (isinstance + NULL)
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

 155    L1:     BUILD_MAP                0
                RETURN_VALUE

 156    L2:     LOAD_FAST_BORROW         0 (patch)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               1 ('features')
                CALL                     1
                STORE_FAST               1 (features)

 157            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (features)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN

 158            BUILD_MAP                0
                RETURN_VALUE

 159    L3:     LOAD_FAST_BORROW         1 (features)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_GLOBAL              6 (_ALLOWED_FLAG)
                CALL                     1
                STORE_FAST               2 (flag)

 160            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (flag)
                LOAD_GLOBAL              8 (bool)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN

 161            BUILD_MAP                0
                RETURN_VALUE

 162    L4:     LOAD_FAST_BORROW         0 (patch)
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

 163            LOAD_FAST_BORROW         1 (features)
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

 164            LOAD_FAST_BORROW         4 (extra_top)
                TO_BOOL
                POP_JUMP_IF_TRUE         9 (to L17)
                NOT_TAKEN
                LOAD_FAST_BORROW         5 (extra_feat)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L18)
                NOT_TAKEN

 165   L17:     BUILD_MAP                0
                RETURN_VALUE

 166   L18:     LOAD_CONST               1 ('features')
                LOAD_GLOBAL              6 (_ALLOWED_FLAG)
                LOAD_FAST_BORROW         2 (flag)
                BUILD_MAP                1
                BUILD_MAP                1
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 162            SWAP                     2
                STORE_FAST               3 (k)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 163            SWAP                     2
                STORE_FAST               3 (k)
                RERAISE                  0
ExceptionTable:
  L5 to L7 -> L19 [2]
  L8 to L10 -> L19 [2]
  L11 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\manifest_store.py", line 169>:
169           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('allowed_patch')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[bool]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _derive_target_enabled at 0x0000018C180608A0, file "app\services\memory\manifest_store.py", line 169>:
169           RESUME                   0

170           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (allowed_patch)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (allowed_patch)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               0 ('features')
              CALL                     1
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               1 (None)
      L2:     STORE_FAST               1 (features)

171           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (features)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       46 (to L3)
              NOT_TAKEN

172           LOAD_FAST_BORROW         1 (features)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_GLOBAL              6 (_ALLOWED_FLAG)
              CALL                     1
              STORE_FAST               2 (flag)

173           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (flag)
              LOAD_GLOBAL              8 (bool)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

174           LOAD_FAST_BORROW         2 (flag)
              RETURN_VALUE

175   L3:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app\services\memory\manifest_store.py", line 178>:
178           RESUME                   0
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

Disassembly of <code object _strip_forbidden at 0x0000018C18039070, file "app\services\memory\manifest_store.py", line 178>:
 178           RESUME                   0

 185           LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                1 (items + NULL|self)
               CALL                     0
               GET_ITER
               LOAD_FAST_AND_CLEAR      1 (k)
               LOAD_FAST_AND_CLEAR      2 (v)
               SWAP                     3
       L1:     BUILD_MAP                0
               SWAP                     2
       L2:     FOR_ITER                20 (to L5)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   18 (k, v)
               LOAD_FAST_BORROW         1 (k)
               LOAD_GLOBAL              2 (_FORBIDDEN_ROW_KEYS)
               CONTAINS_OP              1 (not in)
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           18 (to L2)
       L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (k, v)
               MAP_ADD                  2
               JUMP_BACKWARD           22 (to L2)
       L5:     END_FOR
               POP_ITER
       L6:     SWAP                     3
               STORE_FAST               2 (v)
               STORE_FAST               1 (k)
               RETURN_VALUE

  --   L7:     SWAP                     2
               POP_TOP

 185           SWAP                     3
               STORE_FAST               2 (v)
               STORE_FAST               1 (k)
               RERAISE                  0
ExceptionTable:
  L1 to L3 -> L7 [3]
  L4 to L6 -> L7 [3]

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app\services\memory\manifest_store.py", line 192>:
192           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('manifest')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[Dict[str, Any]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object manifest_row_from_manifest at 0x0000018C17E951D0, file "app\services\memory\manifest_store.py", line 192>:
192            RESUME                   0

208            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (manifest)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

209            LOAD_CONST               1 (None)
               RETURN_VALUE

211    L1:     LOAD_FAST_BORROW         0 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               2 ('approval_id')
               CALL                     1
               STORE_FAST               1 (approval_id)

212            LOAD_FAST_BORROW         0 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               3 ('operator_id')
               CALL                     1
               STORE_FAST               2 (operator_id)

213            LOAD_FAST_BORROW         0 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               4 ('plan_hash')
               CALL                     1
               STORE_FAST               3 (plan_hash)

214            LOAD_FAST_BORROW         0 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               5 ('approval_status')
               CALL                     1
               STORE_FAST               4 (approval_status)

215            LOAD_FAST_BORROW         0 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               6 ('approved_at')
               CALL                     1
               STORE_FAST               5 (approved_at)

216            LOAD_FAST_BORROW         0 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               7 ('operator_reason')
               CALL                     1
               STORE_FAST               6 (operator_reason)

217            LOAD_GLOBAL              7 (_normalise_allowed_patch + NULL)
               LOAD_FAST_BORROW         0 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               8 ('allowed_patch')
               CALL                     1
               CALL                     1
               STORE_FAST               7 (allowed_patch)

219            LOAD_FAST_BORROW         0 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               9 ('plan')
               CALL                     1
               STORE_FAST               8 (plan)

220            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         8 (plan)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN
               LOAD_FAST                8 (plan)
               JUMP_FORWARD             1 (to L3)
       L2:     BUILD_MAP                0
       L3:     STORE_FAST               8 (plan)

222            LOAD_FAST_BORROW         8 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              10 ('brokerage_id')
               CALL                     1
               STORE_FAST               9 (brokerage_id)

223            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         9 (brokerage_id)
               LOAD_GLOBAL              8 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L4)
               NOT_TAKEN
               LOAD_FAST_BORROW         9 (brokerage_id)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN

224    L4:     LOAD_CONST               1 (None)
               RETURN_VALUE

225    L5:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (approval_id)
               LOAD_GLOBAL              8 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L6)
               NOT_TAKEN
               LOAD_FAST_BORROW         1 (approval_id)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L7)
               NOT_TAKEN

226    L6:     LOAD_CONST               1 (None)
               RETURN_VALUE

227    L7:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (operator_id)
               LOAD_GLOBAL              8 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L8)
               NOT_TAKEN
               LOAD_FAST_BORROW         2 (operator_id)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN

228    L8:     LOAD_CONST               1 (None)
               RETURN_VALUE

229    L9:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         3 (plan_hash)
               LOAD_GLOBAL              8 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L10)
               NOT_TAKEN
               LOAD_FAST_BORROW         3 (plan_hash)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L11)
               NOT_TAKEN

230   L10:     LOAD_CONST               1 (None)
               RETURN_VALUE

231   L11:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         5 (approved_at)
               LOAD_GLOBAL              8 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L12)
               NOT_TAKEN
               LOAD_FAST_BORROW         5 (approved_at)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L13)
               NOT_TAKEN

232   L12:     LOAD_CONST               1 (None)
               RETURN_VALUE

234   L13:     LOAD_FAST_BORROW         8 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              11 ('recommended_action')
               CALL                     1
               STORE_FAST              10 (recommended_action)

235            LOAD_FAST_BORROW        10 (recommended_action)
               LOAD_GLOBAL             12 (VALID_ACTIONS)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE        3 (to L14)
               NOT_TAKEN

236            LOAD_CONST               1 (None)
               RETURN_VALUE

238   L14:     LOAD_GLOBAL             15 (_derive_target_enabled + NULL)
               LOAD_FAST_BORROW         7 (allowed_patch)
               CALL                     1
               STORE_FAST              11 (target_enabled)

245            LOAD_CONST               2 ('approval_id')
               LOAD_FAST_BORROW         1 (approval_id)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0

246            LOAD_CONST              10 ('brokerage_id')
               LOAD_FAST_BORROW         9 (brokerage_id)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0

247            LOAD_CONST               3 ('operator_id')
               LOAD_FAST_BORROW         2 (operator_id)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0

248            LOAD_CONST               4 ('plan_hash')
               LOAD_FAST_BORROW         3 (plan_hash)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0

249            LOAD_CONST              11 ('recommended_action')
               LOAD_FAST               10 (recommended_action)

250            LOAD_CONST              12 ('target_enabled')
               LOAD_FAST               11 (target_enabled)

251            LOAD_CONST               5 ('approval_status')
               LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         4 (approval_status)
               LOAD_GLOBAL              8 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L15)
               NOT_TAKEN
               LOAD_FAST                4 (approval_status)
               JUMP_FORWARD             5 (to L16)
      L15:     LOAD_GLOBAL             16 (APPROVAL_STATUS_PENDING_APPLY)

252   L16:     LOAD_CONST               8 ('allowed_patch')
               LOAD_FAST                7 (allowed_patch)

253            LOAD_CONST               9 ('plan')
               LOAD_FAST                8 (plan)

254            LOAD_CONST              13 ('manifest')
               LOAD_FAST                0 (manifest)

255            LOAD_CONST               7 ('operator_reason')
               LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         6 (operator_reason)
               LOAD_GLOBAL              8 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L17)
               NOT_TAKEN
               LOAD_FAST                6 (operator_reason)
               JUMP_FORWARD             1 (to L18)
      L17:     LOAD_CONST               1 (None)

256   L18:     LOAD_CONST               6 ('approved_at')
               LOAD_FAST_BORROW         5 (approved_at)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0

244            BUILD_MAP               12
               STORE_FAST              12 (row)

258            LOAD_GLOBAL             19 (_strip_forbidden + NULL)
               LOAD_FAST_BORROW        12 (row)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app\services\memory\manifest_store.py", line 265>:
265           RESUME                   0
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

Disassembly of <code object validate_manifest_row at 0x0000018C181B0BF0, file "app\services\memory\manifest_store.py", line 265>:
265            RESUME                   0

281            BUILD_LIST               0
               STORE_FAST               1 (errors)

282            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (row)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L1)
               NOT_TAKEN

283            LOAD_CONST               1 ('row_must_be_dict')
               BUILD_LIST               1
               RETURN_VALUE

285    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
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

286    L2:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               3 ('missing_approval_id')
               CALL                     1
               POP_TOP

287    L3:     LOAD_GLOBAL              1 (isinstance + NULL)
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

288    L4:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               5 ('missing_brokerage_id')
               CALL                     1
               POP_TOP

289    L5:     LOAD_GLOBAL              1 (isinstance + NULL)
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

290    L6:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               7 ('missing_operator_id')
               CALL                     1
               POP_TOP

291    L7:     LOAD_GLOBAL              1 (isinstance + NULL)
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

292    L8:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               9 ('missing_plan_hash')
               CALL                     1
               POP_TOP

293    L9:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              10 ('approved_at')
               CALL                     1
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       30 (to L10)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (row)
               LOAD_CONST              10 ('approved_at')
               BINARY_OP               26 ([])
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L11)
               NOT_TAKEN

294   L10:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              11 ('missing_approved_at')
               CALL                     1
               POP_TOP

296   L11:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              12 ('recommended_action')
               CALL                     1
               STORE_FAST               2 (action)

297            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (action)
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       12 (to L12)
               NOT_TAKEN
               LOAD_FAST_BORROW         2 (action)
               LOAD_GLOBAL             12 (VALID_ACTIONS)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       22 (to L13)
               NOT_TAKEN

298   L12:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              13 ('invalid_recommended_action:')
               LOAD_FAST_BORROW         2 (action)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

300   L13:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              14 ('approval_status')
               CALL                     1
               STORE_FAST               3 (approval_status)

301            LOAD_FAST_BORROW         3 (approval_status)
               LOAD_GLOBAL             14 (VALID_APPROVAL_STATUSES)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       22 (to L14)
               NOT_TAKEN

302            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              15 ('invalid_approval_status:')
               LOAD_FAST_BORROW         3 (approval_status)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

304   L14:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              16 ('target_enabled')
               CALL                     1
               STORE_FAST               4 (target_enabled)

305            LOAD_FAST_BORROW         4 (target_enabled)
               POP_JUMP_IF_NONE        40 (to L15)
               NOT_TAKEN
               LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         4 (target_enabled)
               LOAD_GLOBAL             16 (bool)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L15)
               NOT_TAKEN

306            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              17 ('invalid_target_enabled')
               CALL                     1
               POP_TOP

309   L15:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              18 ('allowed_patch')
               CALL                     1
               STORE_FAST               5 (patch)

310            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         5 (patch)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        20 (to L16)
               NOT_TAKEN

311            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              19 ('invalid_allowed_patch_type')
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_FORWARD           284 (to L20)

312   L16:     LOAD_FAST_BORROW         5 (patch)
               TO_BOOL
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      276 (to L20)
               NOT_TAKEN

313            LOAD_GLOBAL             19 (sorted + NULL)
               LOAD_CONST              20 (<code object <genexpr> at 0x0000018C17FBFEE0, file "app\services\memory\manifest_store.py", line 313>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         5 (patch)
               LOAD_ATTR               21 (keys + NULL|self)
               CALL                     0
               GET_ITER
               CALL                     0
               CALL                     1
               STORE_FAST               6 (extra_top)

314            LOAD_FAST_BORROW         6 (extra_top)
               TO_BOOL
               POP_JUMP_IF_FALSE       40 (to L17)
               NOT_TAKEN

315            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)

316            LOAD_CONST              21 ('allowed_patch_has_disallowed_top_keys:')
               LOAD_CONST              22 (',')
               LOAD_ATTR               23 (join + NULL|self)
               LOAD_FAST_BORROW         6 (extra_top)
               CALL                     1
               BINARY_OP                0 (+)

315            CALL                     1
               POP_TOP

318   L17:     LOAD_FAST_BORROW         5 (patch)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              23 ('features')
               CALL                     1
               STORE_FAST               7 (features)

319            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         7 (features)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        19 (to L18)
               NOT_TAKEN

320            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              24 ('allowed_patch_features_must_be_dict')
               CALL                     1
               POP_TOP
               JUMP_FORWARD           139 (to L20)

322   L18:     LOAD_GLOBAL             19 (sorted + NULL)
               LOAD_CONST              25 (<code object <genexpr> at 0x0000018C180C4030, file "app\services\memory\manifest_store.py", line 322>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         7 (features)
               LOAD_ATTR               21 (keys + NULL|self)
               CALL                     0
               GET_ITER
               CALL                     0
               CALL                     1
               STORE_FAST               8 (extra_feat)

323            LOAD_FAST_BORROW         8 (extra_feat)
               TO_BOOL
               POP_JUMP_IF_FALSE       40 (to L19)
               NOT_TAKEN

324            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)

325            LOAD_CONST              26 ('allowed_patch_features_has_disallowed_keys:')
               LOAD_CONST              22 (',')
               LOAD_ATTR               23 (join + NULL|self)
               LOAD_FAST_BORROW         8 (extra_feat)
               CALL                     1
               BINARY_OP                0 (+)

324            CALL                     1
               POP_TOP

327   L19:     LOAD_FAST_BORROW         7 (features)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_GLOBAL             24 (_ALLOWED_FLAG)
               CALL                     1
               STORE_FAST               9 (flag)

328            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         9 (flag)
               LOAD_GLOBAL             16 (bool)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L20)
               NOT_TAKEN

329            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              27 ('allowed_patch_flag_must_be_bool')
               CALL                     1
               POP_TOP

332   L20:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              28 ('plan')
               CALL                     1
               STORE_FAST              10 (plan)

333            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW        10 (plan)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L21)
               NOT_TAKEN

334            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              29 ('invalid_plan_type')
               CALL                     1
               POP_TOP

336   L21:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              30 ('manifest')
               CALL                     1
               STORE_FAST              11 (manifest)

337            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW        11 (manifest)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        19 (to L22)
               NOT_TAKEN

338            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              31 ('invalid_manifest_type')
               CALL                     1
               POP_TOP
               JUMP_FORWARD            49 (to L25)

344   L22:     LOAD_GLOBAL             26 (approval_mod)
               LOAD_ATTR               28 (validate_approval_manifest)
               PUSH_NULL
               LOAD_FAST_BORROW        11 (manifest)
               CALL                     1
               GET_ITER
      L23:     FOR_ITER                23 (to L24)
               STORE_FAST              12 (e)

345            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              32 ('manifest:')
               LOAD_FAST_BORROW        12 (e)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           25 (to L23)

344   L24:     END_FOR
               POP_ITER

350   L25:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW        10 (plan)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       96 (to L29)
               NOT_TAKEN

351            LOAD_FAST_BORROW        10 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              33 ('evidence')
               CALL                     1
               STORE_FAST              13 (evidence)

352            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW        13 (evidence)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       57 (to L29)
               NOT_TAKEN

353            LOAD_FAST_BORROW        13 (evidence)
               LOAD_ATTR               21 (keys + NULL|self)
               CALL                     0
               GET_ITER
      L26:     FOR_ITER                36 (to L28)
               STORE_FAST              14 (k)

354            LOAD_FAST_BORROW        14 (k)
               LOAD_GLOBAL             30 (_SAFE_EVIDENCE_FIELDS)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_TRUE         3 (to L27)
               NOT_TAKEN
               JUMP_BACKWARD           16 (to L26)

355   L27:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              34 ('plan_evidence_has_disallowed_key:')
               LOAD_FAST_BORROW        14 (k)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

356            POP_TOP
               JUMP_FORWARD             2 (to L29)

353   L28:     END_FOR
               POP_ITER

359   L29:     LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR               21 (keys + NULL|self)
               CALL                     0
               GET_ITER
      L30:     FOR_ITER                37 (to L32)
               STORE_FAST              14 (k)

360            LOAD_FAST_BORROW        14 (k)
               LOAD_GLOBAL             32 (_FORBIDDEN_ROW_KEYS)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L31)
               NOT_TAKEN
               JUMP_BACKWARD           16 (to L30)

361   L31:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              35 ('row_has_forbidden_key:')
               LOAD_FAST_BORROW        14 (k)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

362            POP_TOP

364            LOAD_FAST_BORROW         1 (errors)
               RETURN_VALUE

359   L32:     END_FOR
               POP_ITER

364            LOAD_FAST_BORROW         1 (errors)
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C17FBFEE0, file "app\services\memory\manifest_store.py", line 313>:
 313           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C180C4030, file "app\services\memory\manifest_store.py", line 322>:
 322           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app\services\memory\manifest_store.py", line 371>:
371           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('manifest')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object record_manifest at 0x0000018C17EE1CC0, file "app\services\memory\manifest_store.py", line 371>:
 371            RESUME                   0

 385            LOAD_GLOBAL              1 (manifest_row_from_manifest + NULL)
                LOAD_FAST_BORROW         0 (manifest)
                CALL                     1
                STORE_FAST               1 (row)

 386            LOAD_FAST_BORROW         1 (row)
                POP_JUMP_IF_NOT_NONE     7 (to L1)
                NOT_TAKEN

 388            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('skipped')

 389            LOAD_CONST               4 ('reason')
                LOAD_CONST               5 ('unrecognised_manifest_shape')

 387            BUILD_MAP                2
                RETURN_VALUE

 392    L1:     LOAD_GLOBAL              3 (validate_manifest_row + NULL)
                LOAD_FAST_BORROW         1 (row)
                CALL                     1
                STORE_FAST               2 (errors)

 393            LOAD_FAST_BORROW         2 (errors)
                TO_BOOL
                POP_JUMP_IF_FALSE       16 (to L2)
                NOT_TAKEN

 395            LOAD_CONST               2 ('status')
                LOAD_CONST               6 ('failed')

 396            LOAD_CONST               7 ('errors')
                LOAD_GLOBAL              5 (list + NULL)
                LOAD_FAST_BORROW         2 (errors)
                CALL                     1

 394            BUILD_MAP                2
                RETURN_VALUE

 399    L2:     NOP

 400    L3:     LOAD_GLOBAL              7 (_get_db + NULL)
                CALL                     0
                STORE_FAST               3 (db)

 401            LOAD_FAST_BORROW         3 (db)
                LOAD_ATTR                9 (table + NULL|self)
                LOAD_GLOBAL             10 (_TABLE)
                CALL                     1
                LOAD_ATTR               13 (insert + NULL|self)
                LOAD_FAST_BORROW         1 (row)
                CALL                     1
                LOAD_ATTR               15 (execute + NULL|self)
                CALL                     0
                STORE_FAST               4 (result)

 402            LOAD_GLOBAL             17 (getattr + NULL)
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

 404            LOAD_CONST               2 ('status')
                LOAD_CONST               9 ('ok')

 405            LOAD_CONST              10 ('row')
                LOAD_FAST_BORROW         5 (inserted)
                TO_BOOL
                POP_JUMP_IF_FALSE       11 (to L10)
        L7:     NOT_TAKEN
        L8:     LOAD_FAST_BORROW         5 (inserted)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])

 403            BUILD_MAP                2
        L9:     RETURN_VALUE

 405   L10:     LOAD_FAST                1 (row)

 403            BUILD_MAP                2
       L11:     RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 407            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      101 (to L17)
                NOT_TAKEN
                STORE_FAST               6 (e)

 408   L13:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 409            LOAD_CONST              11 ('record_manifest insert failed (non-critical) | brokerage=')

 410            LOAD_FAST                1 (row)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              13 (' | error_type=')

 411            LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE

 409            BUILD_STRING             4

 408            CALL                     1
                POP_TOP

 414            LOAD_CONST               2 ('status')
                LOAD_CONST               6 ('failed')

 415            LOAD_CONST               7 ('errors')
                LOAD_CONST              14 ('db_write_failed:')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 413            BUILD_MAP                2
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

 407   L17:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\memory\manifest_store.py", line 423>:
423           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('approval_id')

424           LOAD_CONST               2 ('str')

423           LOAD_CONST               3 ('brokerage_id')

425           LOAD_CONST               4 ('Optional[str]')

423           LOAD_CONST               5 ('return')

426           LOAD_CONST               6 ('Optional[Dict[str, Any]]')

423           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object get_manifest at 0x0000018C17F84A20, file "app\services\memory\manifest_store.py", line 423>:
 423            RESUME                   0

 439            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (approval_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (approval_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        24 (to L2)
                NOT_TAKEN

 440    L1:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 441            LOAD_CONST               1 ('get_manifest dropped | reason=invalid_approval_id')

 440            CALL                     1
                POP_TOP

 443            LOAD_CONST               2 (None)
                RETURN_VALUE

 445    L2:     LOAD_FAST_BORROW         1 (brokerage_id)
                POP_JUMP_IF_NONE        68 (to L4)
                NOT_TAKEN

 446            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        24 (to L4)
                NOT_TAKEN

 448    L3:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 449            LOAD_CONST               3 ('get_manifest dropped | reason=invalid_brokerage_id')

 448            CALL                     1
                POP_TOP

 451            LOAD_CONST               2 (None)
                RETURN_VALUE

 453    L4:     NOP

 454    L5:     LOAD_GLOBAL             11 (_get_db + NULL)
                CALL                     0
                STORE_FAST               2 (db)

 455            LOAD_FAST_BORROW         2 (db)
                LOAD_ATTR               13 (table + NULL|self)
                LOAD_GLOBAL             14 (_TABLE)
                CALL                     1
                LOAD_ATTR               17 (select + NULL|self)
                LOAD_CONST               4 ('*')
                CALL                     1
                LOAD_ATTR               19 (eq + NULL|self)
                LOAD_CONST               5 ('approval_id')
                LOAD_FAST_BORROW         0 (approval_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                CALL                     2
                STORE_FAST               3 (q)

 456            LOAD_FAST_BORROW         1 (brokerage_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       33 (to L6)
                NOT_TAKEN

 457            LOAD_FAST_BORROW         3 (q)
                LOAD_ATTR               19 (eq + NULL|self)
                LOAD_CONST               6 ('brokerage_id')
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                CALL                     2
                STORE_FAST               3 (q)

 458    L6:     LOAD_FAST_BORROW         3 (q)
                LOAD_ATTR               21 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1
                LOAD_ATTR               23 (execute + NULL|self)
                CALL                     0
                STORE_FAST               4 (result)

 459            LOAD_GLOBAL             25 (getattr + NULL)
                LOAD_FAST_BORROW         4 (result)
                LOAD_CONST               7 ('data')
                LOAD_CONST               2 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
        L7:     NOT_TAKEN
        L8:     POP_TOP
                BUILD_LIST               0
        L9:     STORE_FAST               5 (rows)

 460            LOAD_FAST_BORROW         5 (rows)
                TO_BOOL
                POP_JUMP_IF_FALSE       10 (to L13)
       L10:     NOT_TAKEN
       L11:     LOAD_FAST_BORROW         5 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
       L12:     RETURN_VALUE
       L13:     LOAD_CONST               2 (None)
       L14:     RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 461            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       58 (to L19)
                NOT_TAKEN
                STORE_FAST               6 (e)

 462   L16:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 463            LOAD_CONST               8 ('get_manifest failed (non-critical) | approval_id=')

 464            LOAD_FAST                0 (approval_id)
                FORMAT_SIMPLE
                LOAD_CONST               9 (' | error_type=')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 463            BUILD_STRING             4

 462            CALL                     1
                POP_TOP

 466   L17:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L18:     LOAD_CONST               2 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 461   L19:     RERAISE                  0

  --   L20:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L7 -> L15 [0]
  L8 to L10 -> L15 [0]
  L11 to L12 -> L15 [0]
  L13 to L14 -> L15 [0]
  L15 to L16 -> L20 [1] lasti
  L16 to L17 -> L18 [1] lasti
  L18 to L20 -> L20 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024D30, file "app\services\memory\manifest_store.py", line 469>:
469           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

470           LOAD_CONST               2 ('str')

469           LOAD_CONST               3 ('limit')

472           LOAD_CONST               4 ('int')

469           LOAD_CONST               5 ('return')

473           LOAD_CONST               6 ('List[Dict[str, Any]]')

469           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object list_manifests_for_brokerage at 0x0000018C17E932B0, file "app\services\memory\manifest_store.py", line 469>:
 469            RESUME                   0

 480            LOAD_GLOBAL              1 (isinstance + NULL)
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

 481    L1:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 482            LOAD_CONST               1 ('list_manifests_for_brokerage dropped | reason=missing_brokerage_id')

 481            CALL                     1
                POP_TOP

 485            BUILD_LIST               0
                RETURN_VALUE

 487    L2:     LOAD_GLOBAL             11 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         1 (limit)
                CALL                     1
                STORE_FAST               2 (capped)

 488            NOP

 489    L3:     LOAD_GLOBAL             13 (_get_db + NULL)
                CALL                     0
                STORE_FAST               3 (db)

 491            LOAD_FAST_BORROW         3 (db)
                LOAD_ATTR               15 (table + NULL|self)
                LOAD_GLOBAL             16 (_TABLE)
                CALL                     1

 492            LOAD_ATTR               19 (select + NULL|self)
                LOAD_CONST               2 ('*')
                CALL                     1

 493            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST               3 ('brokerage_id')
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                CALL                     2

 494            LOAD_ATTR               23 (order + NULL|self)
                LOAD_CONST               4 ('created_at')
                LOAD_CONST               5 (True)
                LOAD_CONST               6 (('desc',))
                CALL_KW                  2

 495            LOAD_ATTR               25 (limit + NULL|self)
                LOAD_FAST_BORROW         2 (capped)
                CALL                     1

 496            LOAD_ATTR               27 (execute + NULL|self)
                CALL                     0

 490            STORE_FAST               4 (result)

 498            LOAD_GLOBAL             29 (list + NULL)
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

 499            LOAD_GLOBAL             32 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       59 (to L11)
                NOT_TAKEN
                STORE_FAST               5 (e)

 500    L7:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 501            LOAD_CONST               9 ('list_manifests_for_brokerage failed (non-critical) | brokerage=')

 502            LOAD_FAST                0 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST              10 (' | error_type=')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE

 501            BUILD_STRING             4

 500            CALL                     1
                POP_TOP

 504            BUILD_LIST               0
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

 499   L11:     RERAISE                  0

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L6 [0]
  L6 to L7 -> L12 [1] lasti
  L7 to L8 -> L10 [1] lasti
  L8 to L9 -> L12 [1] lasti
  L10 to L12 -> L12 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app\services\memory\manifest_store.py", line 507>:
507           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('operator_id')

508           LOAD_CONST               2 ('str')

507           LOAD_CONST               3 ('limit')

510           LOAD_CONST               4 ('int')

507           LOAD_CONST               5 ('return')

511           LOAD_CONST               6 ('List[Dict[str, Any]]')

507           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object list_manifests_for_operator at 0x0000018C17E935F0, file "app\services\memory\manifest_store.py", line 507>:
 507            RESUME                   0

 520            LOAD_GLOBAL              1 (isinstance + NULL)
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

 521    L1:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 522            LOAD_CONST               1 ('list_manifests_for_operator dropped | reason=missing_operator_id')

 521            CALL                     1
                POP_TOP

 525            BUILD_LIST               0
                RETURN_VALUE

 527    L2:     LOAD_GLOBAL             11 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         1 (limit)
                CALL                     1
                STORE_FAST               2 (capped)

 528            NOP

 529    L3:     LOAD_GLOBAL             13 (_get_db + NULL)
                CALL                     0
                STORE_FAST               3 (db)

 531            LOAD_FAST_BORROW         3 (db)
                LOAD_ATTR               15 (table + NULL|self)
                LOAD_GLOBAL             16 (_TABLE)
                CALL                     1

 532            LOAD_ATTR               19 (select + NULL|self)
                LOAD_CONST               2 ('*')
                CALL                     1

 533            LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST               3 ('operator_id')
                LOAD_FAST_BORROW         0 (operator_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                CALL                     2

 534            LOAD_ATTR               23 (order + NULL|self)
                LOAD_CONST               4 ('created_at')
                LOAD_CONST               5 (True)
                LOAD_CONST               6 (('desc',))
                CALL_KW                  2

 535            LOAD_ATTR               25 (limit + NULL|self)
                LOAD_FAST_BORROW         2 (capped)
                CALL                     1

 536            LOAD_ATTR               27 (execute + NULL|self)
                CALL                     0

 530            STORE_FAST               4 (result)

 538            LOAD_GLOBAL             29 (list + NULL)
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

 539            LOAD_GLOBAL             32 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       59 (to L11)
                NOT_TAKEN
                STORE_FAST               5 (e)

 540    L7:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 541            LOAD_CONST               9 ('list_manifests_for_operator failed (non-critical) | operator=')

 542            LOAD_FAST                0 (operator_id)
                FORMAT_SIMPLE
                LOAD_CONST              10 (' | error_type=')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE

 541            BUILD_STRING             4

 540            CALL                     1
                POP_TOP

 544            BUILD_LIST               0
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

 539   L11:     RERAISE                  0

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
