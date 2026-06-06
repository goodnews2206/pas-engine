# memory/approval

- **pyc:** `app\services\memory\__pycache__\approval.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/approval.py`
- **co_filename (from bytecode):** `app\services\memory\approval.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144L — Signed Operator Approval + Safe Apply Adapter.

Bridge layer between PAS144K's planning-only rollout module and the
brokerage feature-flag column. Adds the minimum machinery for an
operator-approved rollout plan to be applied to a brokerage config,
WITHOUT enabling autonomous rollout:

  * an approval manifest records *who* approved *which exact plan*
    (deterministic SHA-256 over canonical JSON) and *why*;
  * the manifest carries an ``allowed_patch`` whitelist that may only
    contain ``features.memory_injection_enabled: <bool>`` — anything
    broader is rejected before the DB write helper is reached;
  * ``apply_approved_rollout`` defaults to ``dry_run=True``; the live
    branch is only entered with an explicit ``dry_run=False`` and a
    structurally valid manifest;
  * the live branch fetches the current brokerage row, merges the
    single flag into ``features`` (so other flags are not clobbered),
    and writes via the existing
    :func:`app.db.brokerage_store.update_brokerage` helper with
    ``allow_privileged=True`` (the column is privileged per PAS143H);
  * every code path emits structural-only telemetry — no plan
    evidence, no memory text, no transcripts, no prompts.

Hard contract:
  * NO Supabase client imported here. The brokerage_store + event_logger
    helpers are imported lazily inside the apply path so a test
    environment without Supabase env vars can still import this
    module.
  * Manifests are NEVER mutated by callers of validate / apply.
  * Plans inside manifests are deep-copied on build so future
    mutation of the original plan dict cannot invalidate the hash.
  * Exceptions in the live apply path are caught and converted to a
    structured ``{applied: False, status: "apply_failed",
    error_code: ...}`` result. Raw exceptions never escape.
  * Only ``propose_enable`` and ``propose_disable`` plans are
    applyable. ``no_change`` / ``propose_hold`` / ``propose_investigate``
    require a different operator workflow and are rejected here.

Public surface (deliberately small):
  - APPLYABLE_ACTIONS                                       (frozenset)
  - APPROVAL_STATUS_PENDING_APPLY                            (str)
  - build_approval_manifest(plan, operator_id, reason=None)  -> dict
  - validate_approval_manifest(manifest)                     -> list[str]
  - apply_approved_rollout(manifest, *, dry_run=True)        -> dict
  - compute_plan_hash(plan)                                  -> str

PAS144L explicitly does NOT build:
  * autonomous rollout (every apply requires a signed manifest);
  * automatic memory writes;
  * embeddings / vector helpers;
  * runtime behaviour changes beyond the eventual operator-approved
    config change.
```

## Imports

`ACTION_PROPOSE_DISABLE`, `ACTION_PROPOSE_ENABLE`, `Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.brokerage_store`, `app.db.event_logger`, `copy`, `datetime`, `get_brokerage_by_id`, `hashlib`, `json`, `log_event`, `rollout`, `timezone`, `typing`, `update_brokerage`, `uuid`, `validate_rollout_plan`

## Classes

_none_

## Functions / methods

`__annotate__`, `_emit_event`, `_live_apply_flag`, `_sanitize_reason`, `_target_enabled`, `_validate_allowed_patch`, `apply_approved_rollout`, `build_approval_manifest`, `compute_plan_hash`, `validate_approval_manifest`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS144L — Signed Operator Approval + Safe Apply Adapter.\n\nBridge layer between PAS144K\'s planning-only rollout module and the\nbrokerage feature-flag column. Adds the minimum machinery for an\noperator-approved rollout plan to be applied to a brokerage config,\nWITHOUT enabling autonomous rollout:\n\n  * an approval manifest records *who* approved *which exact plan*\n    (deterministic SHA-256 over canonical JSON) and *why*;\n  * the manifest carries an ``allowed_patch`` whitelist that may only\n    contain ``features.memory_injection_enabled: <bool>`` — anything\n    broader is rejected before the DB write helper is reached;\n  * ``apply_approved_rollout`` defaults to ``dry_run=True``; the live\n    branch is only entered with an explicit ``dry_run=False`` and a\n    structurally valid manifest;\n  * the live branch fetches the current brokerage row, merges the\n    single flag into ``features`` (so other flags are not clobbered),\n    and writes via the existing\n    :func:`app.db.brokerage_store.update_brokerage` helper with\n    ``allow_privileged=True`` (the column is privileged per PAS143H);\n  * every code path emits structural-only telemetry — no plan\n    evidence, no memory text, no transcripts, no prompts.\n\nHard contract:\n  * NO Supabase client imported here. The brokerage_store + event_logger\n    helpers are imported lazily inside the apply path so a test\n    environment without Supabase env vars can still import this\n    module.\n  * Manifests are NEVER mutated by callers of validate / apply.\n  * Plans inside manifests are deep-copied on build so future\n    mutation of the original plan dict cannot invalidate the hash.\n  * Exceptions in the live apply path are caught and converted to a\n    structured ``{applied: False, status: "apply_failed",\n    error_code: ...}`` result. Raw exceptions never escape.\n  * Only ``propose_enable`` and ``propose_disable`` plans are\n    applyable. ``no_change`` / ``propose_hold`` / ``propose_investigate``\n    require a different operator workflow and are rejected here.\n\nPublic surface (deliberately small):\n  - APPLYABLE_ACTIONS                                       (frozenset)\n  - APPROVAL_STATUS_PENDING_APPLY                            (str)\n  - build_approval_manifest(plan, operator_id, reason=None)  -> dict\n  - validate_approval_manifest(manifest)                     -> list[str]\n  - apply_approved_rollout(manifest, *, dry_run=True)        -> dict\n  - compute_plan_hash(plan)                                  -> str\n\nPAS144L explicitly does NOT build:\n  * autonomous rollout (every apply requires a signed manifest);\n  * automatic memory writes;\n  * embeddings / vector helpers;\n  * runtime behaviour changes beyond the eventual operator-approved\n    config change.\n'
- 'approved_pending_apply'
- 'memory_injection_enabled'
- 'invalid_manifest'
- 'brokerage_not_found'
- 'db_write_failed'
- 'helper_import_failed'
- 'apply_exception'
- 'error_code'
- 'severity'
- 'info'
- 'dry_run'
- 'reason'
- 'Any'
- 'return'
- 'Optional[str]'
- 'Coerce + length-cap an operator-supplied reason string.'
- 'plan'
- 'Dict[str, Any]'
- 'str'
- 'Return a deterministic SHA-256 hex digest over the canonical\nJSON of ``plan``.\n\nCanonicalisation: ``json.dumps(plan, sort_keys=True,\nseparators=(",", ":"))``. Equal plans (same keys + values, any\ninsertion order) produce the same hash.\n\nPure. Never raises — non-serialisable values fall through ``default=str``.\n'
- 'utf-8'
- 'patch'
- 'List[str]'
- 'Return blockers for the allowed_patch shape.\n\nThe strict apply shape is ``{"features": {"memory_injection_enabled":\n<bool>}}`` — nothing else. An empty patch (which is what\nno_change / hold / investigate plans carry) fails here; that is\nintentional — non-applyable plans have a separate blocker upstream.\n'
- 'allowed_patch_must_be_dict'
- 'allowed_patch_has_disallowed_top_keys:'
- 'features'
- 'allowed_patch_features_must_be_dict'
- 'allowed_patch_features_has_disallowed_keys:'
- 'allowed_patch_flag_must_be_bool'
- 'manifest'
- 'Optional[bool]'
- 'Extract the bool flip target from a manifest. Returns None when\nthe patch is malformed.'
- 'allowed_patch'
- 'operator_id'
- 'Build a signed approval manifest for the given rollout plan.\n\nHard requirements (raise ``ValueError`` — these are caller bugs,\nnot policy decisions):\n  * ``operator_id`` is a non-empty string;\n  * ``plan`` is a dict.\n\nManifest fields:\n  * ``approval_id``     — fresh UUID4.\n  * ``approved_at``     — ISO-8601 UTC timestamp.\n  * ``operator_id``     — sanitised operator string.\n  * ``operator_reason`` — sanitised reason (length-capped) or None.\n  * ``plan_hash``       — deterministic SHA-256 over canonical\n                          JSON of ``plan``.\n  * ``plan``            — deep copy of the input plan so a later\n                          mutation of the original cannot\n                          invalidate the manifest\'s hash.\n  * ``allowed_patch``   — exact copy of ``plan.proposed_config_patch``\n                          (defensive copy).\n  * ``approval_status`` — ``APPROVAL_STATUS_PENDING_APPLY``.\n\nBuild does NOT enforce applyability — a propose_hold plan can be\nwrapped in a manifest. ``validate_approval_manifest`` is the gate\nthat says "this manifest can be applied". This split lets ops\nrecord what an operator approved even when they approved something\nPAS144L declines to apply autonomously.\n\nPure. No I/O. No DB. No mutation of the input plan dict.\n'
- 'operator_id is required (non-empty string)'
- 'plan must be a dict'
- 'proposed_config_patch'
- 'approval_id'
- 'approved_at'
- 'operator_reason'
- 'plan_hash'
- 'approval_status'
- "Return a list of human-readable blockers for the manifest.\n\nAn empty list means the manifest is structurally valid AND the\nunderlying plan is one that PAS144L is willing to apply (i.e. a\npropose_enable or propose_disable). Pure. Never raises.\n\nChecks (in order, but all run so the caller sees every blocker):\n  * manifest is a dict;\n  * approval_id present, non-empty string;\n  * approved_at present, string;\n  * operator_id present, non-empty string;\n  * approval_status == APPROVAL_STATUS_PENDING_APPLY;\n  * plan is a dict and passes ``validate_rollout_plan``;\n  * plan_hash matches the recomputed hash of ``plan``;\n  * plan recommended_action is in ``APPLYABLE_ACTIONS``;\n  * allowed_patch is exactly the documented shape;\n  * allowed_patch matches the plan's ``proposed_config_patch``;\n  * plan carries a non-empty brokerage_id (apply target).\n"
- 'manifest_must_be_dict'
- 'missing_approval_id'
- 'missing_approved_at'
- 'missing_operator_id'
- 'invalid_approval_status'
- 'missing_or_invalid_plan'
- 'plan:'
- 'plan_hash_mismatch'
- 'recommended_action'
- 'action_not_applyable:'
- 'brokerage_id'
- 'missing_brokerage_id'
- 'allowed_patch_mismatch_with_plan'
- 'event_type'
- 'target_enabled'
- 'bool'
- 'applied'
- 'Emit a single structural-only memory.rollout.* event.\n\nPayload carries only operator-decision metadata — no plan\nevidence, no memory text, no transcripts, no prompts. Lazily\nimports ``log_event`` so an environment that cannot import the\nevent logger (e.g. tests without Supabase) still works.\n'
- 'memory'
- 'memory_rollout'
- 'Merge-and-write the single flag through the brokerage_store helper.\n\nReturns ``{"ok": True}`` on success or ``{"ok": False,\n"error_code": <code>}`` on any failure. Never raises.\n\nSurgically scoped: fetches the current brokerage row, copies its\n``features`` dict, sets only ``memory_injection_enabled`` to the\ntarget value, and writes that merged dict back. This avoids\nclobbering unrelated feature flags — the brokerage_store helper\ntreats ``features`` as a whole-column replace.\n'
- 'detail'
- 'lookup:'
- 'update:'
- 'Apply an operator-approved rollout manifest.\n\nBehaviour:\n  * ``dry_run=True`` (default): validate the manifest; on success\n    return ``status="dry_run"``, ``applied=False``,\n    ``would_apply=True``. The DB write helper is NEVER called.\n  * ``dry_run=False``: validate the manifest; on success, write\n    the single flag through the brokerage_store helper and return\n    ``status="applied"``, ``applied=True``.\n  * Invalid manifest: return ``status="invalid_manifest"``,\n    ``applied=False``, ``would_apply=False`` and a populated\n    ``errors`` list. The DB write helper is NEVER called.\n  * Live apply failure: return ``status="apply_failed"``,\n    ``applied=False``, plus a structured ``error_code``.\n\nEvery branch emits a structural-only memory.rollout.* event so\nthe audit trail is independent of return-value handling. Never\nraises — exceptions in the live path are caught and reported as\nstructured errors.\n'
- 'memory.rollout.failed'
- 'warning'
- 'would_apply'
- 'status'
- 'errors'
- 'memory.rollout.approved'
- 'error'
- 'apply_failed'
- 'memory.rollout.applied'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS144L — Signed Operator Approval + Safe Apply Adapter.\n\nBridge layer between PAS144K\'s planning-only rollout module and the\nbrokerage feature-flag column. Adds the minimum machinery for an\noperator-approved rollout plan to be applied to a brokerage config,\nWITHOUT enabling autonomous rollout:\n\n  * an approval manifest records *who* approved *which exact plan*\n    (deterministic SHA-256 over canonical JSON) and *why*;\n  * the manifest carries an ``allowed_patch`` whitelist that may only\n    contain ``features.memory_injection_enabled: <bool>`` — anything\n    broader is rejected before the DB write helper is reached;\n  * ``apply_approved_rollout`` defaults to ``dry_run=True``; the live\n    branch is only entered with an explicit ``dry_run=False`` and a\n    structurally valid manifest;\n  * the live branch fetches the current brokerage row, merges the\n    single flag into ``features`` (so other flags are not clobbered),\n    and writes via the existing\n    :func:`app.db.brokerage_store.update_brokerage` helper with\n    ``allow_privileged=True`` (the column is privileged per PAS143H);\n  * every code path emits structural-only telemetry — no plan\n    evidence, no memory text, no transcripts, no prompts.\n\nHard contract:\n  * NO Supabase client imported here. The brokerage_store + event_logger\n    helpers are imported lazily inside the apply path so a test\n    environment without Supabase env vars can still import this\n    module.\n  * Manifests are NEVER mutated by callers of validate / apply.\n  * Plans inside manifests are deep-copied on build so future\n    mutation of the original plan dict cannot invalidate the hash.\n  * Exceptions in the live apply path are caught and converted to a\n    structured ``{applied: False, status: "apply_failed",\n    error_code: ...}`` result. Raw exceptions never escape.\n  * Only ``propose_enable`` and ``propose_disable`` plans are\n    applyable. ``no_change`` / ``propose_hold`` / ``propose_investigate``\n    require a different operator workflow and are rejected here.\n\nPublic surface (deliberately small):\n  - APPLYABLE_ACTIONS                                       (frozenset)\n  - APPROVAL_STATUS_PENDING_APPLY                            (str)\n  - build_approval_manifest(plan, operator_id, reason=None)  -> dict\n  - validate_approval_manifest(manifest)                     -> list[str]\n  - apply_approved_rollout(manifest, *, dry_run=True)        -> dict\n  - compute_plan_hash(plan)                                  -> str\n\nPAS144L explicitly does NOT build:\n  * autonomous rollout (every apply requires a signed manifest);\n  * automatic memory writes;\n  * embeddings / vector helpers;\n  * runtime behaviour changes beyond the eventual operator-approved\n    config change.\n')
              STORE_NAME               0 (__doc__)

 56           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 58           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (copy)
              STORE_NAME               3 (copy)

 59           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (hashlib)
              STORE_NAME               4 (hashlib)

 60           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              5 (json)
              STORE_NAME               5 (json)

 61           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              6 (uuid)
              STORE_NAME               6 (uuid)

 62           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timezone'))
              IMPORT_NAME              7 (datetime)
              IMPORT_FROM              7 (datetime)
              STORE_NAME               7 (datetime)
              IMPORT_FROM              8 (timezone)
              STORE_NAME               8 (timezone)
              POP_TOP

 63           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              9 (typing)
              IMPORT_FROM             10 (Any)
              STORE_NAME              10 (Any)
              IMPORT_FROM             11 (Dict)
              STORE_NAME              11 (Dict)
              IMPORT_FROM             12 (List)
              STORE_NAME              12 (List)
              IMPORT_FROM             13 (Optional)
              STORE_NAME              13 (Optional)
              POP_TOP

 65           LOAD_SMALL_INT           1
              LOAD_CONST               5 (('ACTION_PROPOSE_DISABLE', 'ACTION_PROPOSE_ENABLE', 'validate_rollout_plan'))
              IMPORT_NAME             14 (rollout)
              IMPORT_FROM             15 (ACTION_PROPOSE_DISABLE)
              STORE_NAME              15 (ACTION_PROPOSE_DISABLE)
              IMPORT_FROM             16 (ACTION_PROPOSE_ENABLE)
              STORE_NAME              16 (ACTION_PROPOSE_ENABLE)
              IMPORT_FROM             17 (validate_rollout_plan)
              STORE_NAME              17 (validate_rollout_plan)
              POP_TOP

 76           LOAD_NAME               18 (frozenset)
              PUSH_NULL

 77           LOAD_NAME               16 (ACTION_PROPOSE_ENABLE)

 78           LOAD_NAME               15 (ACTION_PROPOSE_DISABLE)

 76           BUILD_SET                2
              CALL                     1
              STORE_NAME              19 (APPLYABLE_ACTIONS)

 81           LOAD_CONST               6 ('approved_pending_apply')
              STORE_NAME              20 (APPROVAL_STATUS_PENDING_APPLY)

 85           LOAD_CONST               7 ('memory_injection_enabled')
              STORE_NAME              21 (_ALLOWED_FLAG)

 89           LOAD_CONST               8 (500)
              STORE_NAME              22 (_REASON_MAX_CHARS)

 94           LOAD_CONST               9 ('invalid_manifest')
              STORE_NAME              23 (ERROR_INVALID_MANIFEST)

 95           LOAD_CONST              10 ('brokerage_not_found')
              STORE_NAME              24 (ERROR_BROKERAGE_NOT_FOUND)

 96           LOAD_CONST              11 ('db_write_failed')
              STORE_NAME              25 (ERROR_DB_WRITE_FAILED)

 97           LOAD_CONST              12 ('helper_import_failed')
              STORE_NAME              26 (ERROR_HELPER_IMPORT_FAILED)

 98           LOAD_CONST              13 ('apply_exception')
              STORE_NAME              27 (ERROR_APPLY_EXCEPTION)

105           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\approval.py", line 105>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _sanitize_reason at 0x0000018C180483B0, file "app\services\memory\approval.py", line 105>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_sanitize_reason)

122           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\memory\approval.py", line 122>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object compute_plan_hash at 0x0000018C17FF13B0, file "app\services\memory\approval.py", line 122>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (compute_plan_hash)

138           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\approval.py", line 138>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object _validate_allowed_patch at 0x0000018C17EDAA70, file "app\services\memory\approval.py", line 138>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_validate_allowed_patch)

175           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA3B40, file "app\services\memory\approval.py", line 175>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object _target_enabled at 0x0000018C179C3C30, file "app\services\memory\approval.py", line 175>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_target_enabled)

194           LOAD_CONST              37 ((None,))
              LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18024930, file "app\services\memory\approval.py", line 194>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object build_approval_manifest at 0x0000018C17D6DFC0, file "app\services\memory\approval.py", line 194>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              32 (build_approval_manifest)

252           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA21F0, file "app\services\memory\approval.py", line 252>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object validate_approval_manifest at 0x0000018C177C5700, file "app\services\memory\approval.py", line 252>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (validate_approval_manifest)

333           LOAD_CONST              26 ('error_code')

342           LOAD_CONST               2 (None)

333           LOAD_CONST              27 ('severity')

343           LOAD_CONST              28 ('info')

333           BUILD_MAP                2
              LOAD_CONST              29 (<code object __annotate__ at 0x0000018C18090250, file "app\services\memory\approval.py", line 333>)
              MAKE_FUNCTION
              LOAD_CONST              30 (<code object _emit_event at 0x0000018C1796DBD0, file "app\services\memory\approval.py", line 333>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              34 (_emit_event)

385           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\memory\approval.py", line 385>)
              MAKE_FUNCTION
              LOAD_CONST              32 (<code object _live_apply_flag at 0x0000018C17EA7700, file "app\services\memory\approval.py", line 385>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              35 (_live_apply_flag)

443           LOAD_CONST              33 ('dry_run')

446           LOAD_CONST              34 (True)

443           BUILD_MAP                1
              LOAD_CONST              35 (<code object __annotate__ at 0x0000018C18025230, file "app\services\memory\approval.py", line 443>)
              MAKE_FUNCTION
              LOAD_CONST              36 (<code object apply_approved_rollout at 0x0000018C17ED3800, file "app\services\memory\approval.py", line 443>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              36 (apply_approved_rollout)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\approval.py", line 105>:
105           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('reason')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _sanitize_reason at 0x0000018C180483B0, file "app\services\memory\approval.py", line 105>:
 105           RESUME                   0

 107           LOAD_FAST_BORROW         0 (reason)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

 108           LOAD_CONST               1 (None)
               RETURN_VALUE

 109   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (reason)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        13 (to L3)
               NOT_TAKEN

 110           NOP

 111   L2:     LOAD_GLOBAL              3 (str + NULL)
               LOAD_FAST_BORROW         0 (reason)
               CALL                     1
               STORE_FAST               0 (reason)

 114   L3:     LOAD_FAST_BORROW         0 (reason)
               LOAD_ATTR                7 (strip + NULL|self)
               CALL                     0
               STORE_FAST               0 (reason)

 115           LOAD_FAST_BORROW         0 (reason)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN

 116           LOAD_CONST               1 (None)
               RETURN_VALUE

 117   L4:     LOAD_GLOBAL              9 (len + NULL)
               LOAD_FAST_BORROW         0 (reason)
               CALL                     1
               LOAD_GLOBAL             10 (_REASON_MAX_CHARS)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE       10 (to L5)
               NOT_TAKEN

 118           LOAD_FAST_BORROW         0 (reason)
               LOAD_CONST               1 (None)
               LOAD_GLOBAL             10 (_REASON_MAX_CHARS)
               BINARY_SLICE
               RETURN_VALUE

 119   L5:     LOAD_FAST_BORROW         0 (reason)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

 112           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

 113   L7:     POP_EXCEPT
               LOAD_CONST               1 (None)
               RETURN_VALUE

 112   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\memory\approval.py", line 122>:
122           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('plan')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object compute_plan_hash at 0x0000018C17FF13B0, file "app\services\memory\approval.py", line 122>:
122           RESUME                   0

132           LOAD_GLOBAL              0 (json)
              LOAD_ATTR                2 (dumps)
              PUSH_NULL

133           LOAD_FAST_BORROW         0 (plan)
              LOAD_CONST               1 (True)
              LOAD_CONST               4 ((',', ':'))
              LOAD_GLOBAL              4 (str)

132           LOAD_CONST               2 (('sort_keys', 'separators', 'default'))
              CALL_KW                  4
              STORE_FAST               1 (canonical)

135           LOAD_GLOBAL              6 (hashlib)
              LOAD_ATTR                8 (sha256)
              PUSH_NULL
              LOAD_FAST_BORROW         1 (canonical)
              LOAD_ATTR               11 (encode + NULL|self)
              LOAD_CONST               3 ('utf-8')
              CALL                     1
              CALL                     1
              LOAD_ATTR               13 (hexdigest + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\approval.py", line 138>:
138           RESUME                   0
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
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _validate_allowed_patch at 0x0000018C17EDAA70, file "app\services\memory\approval.py", line 138>:
138           RESUME                   0

146           BUILD_LIST               0
              STORE_FAST               1 (errors)

147           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (patch)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         4 (to L1)
              NOT_TAKEN

148           LOAD_CONST               1 ('allowed_patch_must_be_dict')
              BUILD_LIST               1
              RETURN_VALUE

151   L1:     LOAD_GLOBAL              5 (sorted + NULL)
              LOAD_CONST               2 (<code object <genexpr> at 0x0000018C180908B0, file "app\services\memory\approval.py", line 151>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         0 (patch)
              LOAD_ATTR                7 (keys + NULL|self)
              CALL                     0
              GET_ITER
              CALL                     0
              CALL                     1
              STORE_FAST               2 (extra_top)

152           LOAD_FAST_BORROW         2 (extra_top)
              TO_BOOL
              POP_JUMP_IF_FALSE       40 (to L2)
              NOT_TAKEN

153           LOAD_FAST_BORROW         1 (errors)
              LOAD_ATTR                9 (append + NULL|self)

154           LOAD_CONST               3 ('allowed_patch_has_disallowed_top_keys:')
              LOAD_CONST               4 (',')
              LOAD_ATTR               11 (join + NULL|self)
              LOAD_FAST_BORROW         2 (extra_top)
              CALL                     1
              BINARY_OP                0 (+)

153           CALL                     1
              POP_TOP

157   L2:     LOAD_FAST_BORROW         0 (patch)
              LOAD_ATTR               13 (get + NULL|self)
              LOAD_CONST               5 ('features')
              CALL                     1
              STORE_FAST               3 (features)

158           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (features)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        20 (to L3)
              NOT_TAKEN

159           LOAD_FAST_BORROW         1 (errors)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_CONST               6 ('allowed_patch_features_must_be_dict')
              CALL                     1
              POP_TOP

160           LOAD_FAST_BORROW         1 (errors)
              RETURN_VALUE

162   L3:     LOAD_GLOBAL              5 (sorted + NULL)
              LOAD_CONST               7 (<code object <genexpr> at 0x0000018C18090360, file "app\services\memory\approval.py", line 162>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         3 (features)
              LOAD_ATTR                7 (keys + NULL|self)
              CALL                     0
              GET_ITER
              CALL                     0
              CALL                     1
              STORE_FAST               4 (extra_feat)

163           LOAD_FAST_BORROW         4 (extra_feat)
              TO_BOOL
              POP_JUMP_IF_FALSE       40 (to L4)
              NOT_TAKEN

164           LOAD_FAST_BORROW         1 (errors)
              LOAD_ATTR                9 (append + NULL|self)

165           LOAD_CONST               8 ('allowed_patch_features_has_disallowed_keys:')
              LOAD_CONST               4 (',')
              LOAD_ATTR               11 (join + NULL|self)
              LOAD_FAST_BORROW         4 (extra_feat)
              CALL                     1
              BINARY_OP                0 (+)

164           CALL                     1
              POP_TOP

168   L4:     LOAD_FAST_BORROW         3 (features)
              LOAD_ATTR               13 (get + NULL|self)
              LOAD_GLOBAL             14 (_ALLOWED_FLAG)
              CALL                     1
              STORE_FAST               5 (flag)

169           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         5 (flag)
              LOAD_GLOBAL             16 (bool)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        18 (to L5)
              NOT_TAKEN

170           LOAD_FAST_BORROW         1 (errors)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_CONST               9 ('allowed_patch_flag_must_be_bool')
              CALL                     1
              POP_TOP

172   L5:     LOAD_FAST_BORROW         1 (errors)
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180908B0, file "app\services\memory\approval.py", line 151>:
 151           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18090360, file "app\services\memory\approval.py", line 162>:
 162           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app\services\memory\approval.py", line 175>:
175           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('manifest')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[bool]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _target_enabled at 0x0000018C179C3C30, file "app\services\memory\approval.py", line 175>:
175           RESUME                   0

178           LOAD_FAST_BORROW         0 (manifest)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('allowed_patch')
              CALL                     1
              STORE_FAST               1 (patch)

179           LOAD_GLOBAL              3 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (patch)
              LOAD_GLOBAL              4 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

180           LOAD_CONST               2 (None)
              RETURN_VALUE

181   L1:     LOAD_FAST_BORROW         1 (patch)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('features')
              CALL                     1
              STORE_FAST               2 (features)

182           LOAD_GLOBAL              3 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (features)
              LOAD_GLOBAL              4 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

183           LOAD_CONST               2 (None)
              RETURN_VALUE

184   L2:     LOAD_FAST_BORROW         2 (features)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_GLOBAL              6 (_ALLOWED_FLAG)
              CALL                     1
              STORE_FAST               3 (flag)

185           LOAD_GLOBAL              3 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (flag)
              LOAD_GLOBAL              8 (bool)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

186           LOAD_FAST_BORROW         3 (flag)
              RETURN_VALUE

187   L3:     LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app\services\memory\approval.py", line 194>:
194           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('plan')

195           LOAD_CONST               2 ('Dict[str, Any]')

194           LOAD_CONST               3 ('operator_id')

196           LOAD_CONST               4 ('str')

194           LOAD_CONST               5 ('reason')

197           LOAD_CONST               6 ('Optional[str]')

194           LOAD_CONST               7 ('return')

198           LOAD_CONST               2 ('Dict[str, Any]')

194           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object build_approval_manifest at 0x0000018C17D6DFC0, file "app\services\memory\approval.py", line 194>:
194           RESUME                   0

228           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (operator_id)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (operator_id)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE        12 (to L2)
              NOT_TAKEN

229   L1:     LOAD_GLOBAL              7 (ValueError + NULL)
              LOAD_CONST               1 ('operator_id is required (non-empty string)')
              CALL                     1
              RAISE_VARARGS            1

230   L2:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (plan)
              LOAD_GLOBAL              8 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        12 (to L3)
              NOT_TAKEN

231           LOAD_GLOBAL              7 (ValueError + NULL)
              LOAD_CONST               2 ('plan must be a dict')
              CALL                     1
              RAISE_VARARGS            1

233   L3:     LOAD_GLOBAL             10 (copy)
              LOAD_ATTR               12 (deepcopy)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (plan)
              CALL                     1
              STORE_FAST               3 (plan_copy)

234           LOAD_GLOBAL             10 (copy)
              LOAD_ATTR               12 (deepcopy)
              PUSH_NULL
              LOAD_FAST_BORROW         3 (plan_copy)
              LOAD_ATTR               15 (get + NULL|self)
              LOAD_CONST               3 ('proposed_config_patch')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L4:     CALL                     1
              STORE_FAST               4 (allowed_patch)

237           LOAD_CONST               4 ('approval_id')
              LOAD_GLOBAL              3 (str + NULL)
              LOAD_GLOBAL             16 (uuid)
              LOAD_ATTR               18 (uuid4)
              PUSH_NULL
              CALL                     0
              CALL                     1

238           LOAD_CONST               5 ('approved_at')
              LOAD_GLOBAL             20 (datetime)
              LOAD_ATTR               22 (now)
              PUSH_NULL
              LOAD_GLOBAL             24 (timezone)
              LOAD_ATTR               26 (utc)
              CALL                     1
              LOAD_ATTR               29 (isoformat + NULL|self)
              CALL                     0

239           LOAD_CONST               6 ('operator_id')
              LOAD_FAST_BORROW         1 (operator_id)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0

240           LOAD_CONST               7 ('operator_reason')
              LOAD_GLOBAL             31 (_sanitize_reason + NULL)
              LOAD_FAST_BORROW         2 (reason)
              CALL                     1

241           LOAD_CONST               8 ('plan_hash')
              LOAD_GLOBAL             33 (compute_plan_hash + NULL)
              LOAD_FAST_BORROW         3 (plan_copy)
              CALL                     1

242           LOAD_CONST               9 ('plan')
              LOAD_FAST_BORROW         3 (plan_copy)

243           LOAD_CONST              10 ('allowed_patch')
              LOAD_FAST_BORROW         4 (allowed_patch)

244           LOAD_CONST              11 ('approval_status')
              LOAD_GLOBAL             34 (APPROVAL_STATUS_PENDING_APPLY)

236           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app\services\memory\approval.py", line 252>:
252           RESUME                   0
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
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object validate_approval_manifest at 0x0000018C177C5700, file "app\services\memory\approval.py", line 252>:
252            RESUME                   0

272            BUILD_LIST               0
               STORE_FAST               1 (errors)

274            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (manifest)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L1)
               NOT_TAKEN

275            LOAD_CONST               1 ('manifest_must_be_dict')
               BUILD_LIST               1
               RETURN_VALUE

278    L1:     LOAD_FAST_BORROW         0 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               2 ('approval_id')
               CALL                     1
               STORE_FAST               2 (approval_id)

279            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (approval_id)
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L2)
               NOT_TAKEN
               LOAD_FAST_BORROW         2 (approval_id)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L3)
               NOT_TAKEN

280    L2:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               3 ('missing_approval_id')
               CALL                     1
               POP_TOP

282    L3:     LOAD_FAST_BORROW         0 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               4 ('approved_at')
               CALL                     1
               STORE_FAST               3 (approved_at)

283            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         3 (approved_at)
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L4)
               NOT_TAKEN
               LOAD_FAST_BORROW         3 (approved_at)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L5)
               NOT_TAKEN

284    L4:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               5 ('missing_approved_at')
               CALL                     1
               POP_TOP

286    L5:     LOAD_FAST_BORROW         0 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               6 ('operator_id')
               CALL                     1
               STORE_FAST               4 (operator_id)

287            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         4 (operator_id)
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L6)
               NOT_TAKEN
               LOAD_FAST_BORROW         4 (operator_id)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L7)
               NOT_TAKEN

288    L6:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               7 ('missing_operator_id')
               CALL                     1
               POP_TOP

290    L7:     LOAD_FAST_BORROW         0 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               8 ('approval_status')
               CALL                     1
               LOAD_GLOBAL             12 (APPROVAL_STATUS_PENDING_APPLY)
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE       18 (to L8)
               NOT_TAKEN

291            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               9 ('invalid_approval_status')
               CALL                     1
               POP_TOP

294    L8:     LOAD_FAST_BORROW         0 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              10 ('plan')
               CALL                     1
               STORE_FAST               5 (plan)

295            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         5 (plan)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        20 (to L9)
               NOT_TAKEN

296            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              11 ('missing_or_invalid_plan')
               CALL                     1
               POP_TOP

298            LOAD_FAST_BORROW         1 (errors)
               RETURN_VALUE

300    L9:     LOAD_GLOBAL             15 (validate_rollout_plan + NULL)
               LOAD_FAST_BORROW         5 (plan)
               CALL                     1
               STORE_FAST               6 (plan_errors)

301            LOAD_FAST_BORROW         6 (plan_errors)
               GET_ITER
      L10:     FOR_ITER                23 (to L11)
               STORE_FAST               7 (e)

302            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              12 ('plan:')
               LOAD_FAST_BORROW         7 (e)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           25 (to L10)

301   L11:     END_FOR
               POP_ITER

304            LOAD_FAST_BORROW         0 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              13 ('plan_hash')
               CALL                     1
               STORE_FAST               8 (stored_hash)

305            LOAD_GLOBAL             17 (compute_plan_hash + NULL)
               LOAD_FAST_BORROW         5 (plan)
               CALL                     1
               STORE_FAST               9 (recomputed)

306            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         8 (stored_hash)
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        7 (to L12)
               NOT_TAKEN
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (stored_hash, recomputed)
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE       18 (to L13)
               NOT_TAKEN

307   L12:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              14 ('plan_hash_mismatch')
               CALL                     1
               POP_TOP

310   L13:     LOAD_FAST_BORROW         5 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              15 ('recommended_action')
               CALL                     1
               STORE_FAST              10 (action)

311            LOAD_FAST_BORROW        10 (action)
               LOAD_GLOBAL             18 (APPLYABLE_ACTIONS)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       22 (to L14)
               NOT_TAKEN

312            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              16 ('action_not_applyable:')
               LOAD_FAST_BORROW        10 (action)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

314   L14:     LOAD_FAST_BORROW         5 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              17 ('brokerage_id')
               CALL                     1
               STORE_FAST              11 (brokerage_id)

315            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW        11 (brokerage_id)
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L15)
               NOT_TAKEN
               LOAD_FAST_BORROW        11 (brokerage_id)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L16)
               NOT_TAKEN

316   L15:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              18 ('missing_brokerage_id')
               CALL                     1
               POP_TOP

319   L16:     LOAD_FAST_BORROW         0 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              19 ('allowed_patch')
               CALL                     1
               STORE_FAST              12 (patch)

320            LOAD_GLOBAL             21 (_validate_allowed_patch + NULL)
               LOAD_FAST_BORROW        12 (patch)
               CALL                     1
               GET_ITER
      L17:     FOR_ITER                20 (to L18)
               STORE_FAST               7 (e)

321            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         7 (e)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           22 (to L17)

320   L18:     END_FOR
               POP_ITER

323            LOAD_FAST_BORROW_LOAD_FAST_BORROW 197 (patch, plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              20 ('proposed_config_patch')
               CALL                     1
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE       18 (to L19)
               NOT_TAKEN

324            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              21 ('allowed_patch_mismatch_with_plan')
               CALL                     1
               POP_TOP

326   L19:     LOAD_FAST_BORROW         1 (errors)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18090250, file "app\services\memory\approval.py", line 333>:
333           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('event_type')

334           LOAD_CONST               2 ('str')

333           LOAD_CONST               3 ('approval_id')

336           LOAD_CONST               4 ('Optional[str]')

333           LOAD_CONST               5 ('brokerage_id')

337           LOAD_CONST               4 ('Optional[str]')

333           LOAD_CONST               6 ('recommended_action')

338           LOAD_CONST               4 ('Optional[str]')

333           LOAD_CONST               7 ('target_enabled')

339           LOAD_CONST               8 ('Optional[bool]')

333           LOAD_CONST               9 ('dry_run')

340           LOAD_CONST              10 ('bool')

333           LOAD_CONST              11 ('applied')

341           LOAD_CONST              10 ('bool')

333           LOAD_CONST              12 ('error_code')

342           LOAD_CONST               4 ('Optional[str]')

333           LOAD_CONST              13 ('severity')

343           LOAD_CONST               2 ('str')

333           LOAD_CONST              14 ('return')

344           LOAD_CONST              10 ('bool')

333           BUILD_MAP               10
              RETURN_VALUE

Disassembly of <code object _emit_event at 0x0000018C1796DBD0, file "app\services\memory\approval.py", line 333>:
 333            RESUME                   0

 352            NOP

 353    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('log_event',))
                IMPORT_NAME              0 (app.db.event_logger)
                IMPORT_FROM              1 (log_event)
                STORE_FAST               9 (log_event)
                POP_TOP

 358    L2:     LOAD_CONST               3 ('approval_id')
                LOAD_FAST                1 (approval_id)

 359            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                2 (brokerage_id)

 360            LOAD_CONST               5 ('recommended_action')
                LOAD_FAST                3 (recommended_action)

 361            LOAD_CONST               6 ('target_enabled')
                LOAD_FAST                4 (target_enabled)

 362            LOAD_CONST               7 ('dry_run')
                LOAD_GLOBAL              7 (bool + NULL)
                LOAD_FAST                5 (dry_run)
                CALL                     1

 363            LOAD_CONST               8 ('applied')
                LOAD_GLOBAL              7 (bool + NULL)
                LOAD_FAST                6 (applied)
                CALL                     1

 357            BUILD_MAP                6
                STORE_FAST              10 (payload)

 365            LOAD_FAST                7 (error_code)
                TO_BOOL
                POP_JUMP_IF_FALSE        5 (to L3)
                NOT_TAKEN

 366            LOAD_FAST_LOAD_FAST    122 (error_code, payload)
                LOAD_CONST               9 ('error_code')
                STORE_SUBSCR

 368    L3:     NOP

 369    L4:     LOAD_FAST                9 (log_event)
                PUSH_NULL

 370            LOAD_FAST                0 (event_type)

 371            LOAD_FAST                2 (brokerage_id)

 372            LOAD_CONST              10 ('memory')

 373            LOAD_CONST              11 ('memory_rollout')

 374            LOAD_FAST                8 (severity)

 375            LOAD_FAST               10 (payload)

 369            LOAD_CONST              12 (('brokerage_id', 'event_category', 'event_source', 'severity', 'payload'))
                CALL_KW                  6
        L5:     RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 354            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L8)
                NOT_TAKEN
                POP_TOP

 355    L7:     POP_EXCEPT
                LOAD_CONST               2 (False)
                RETURN_VALUE

 354    L8:     RERAISE                  0

  --    L9:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L10:     PUSH_EXC_INFO

 377            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L12)
                NOT_TAKEN
                POP_TOP

 378   L11:     POP_EXCEPT
                LOAD_CONST               2 (False)
                RETURN_VALUE

 377   L12:     RERAISE                  0

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L6 [0]
  L4 to L5 -> L10 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti
  L10 to L11 -> L13 [1] lasti
  L12 to L13 -> L13 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\memory\approval.py", line 385>:
385           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

386           LOAD_CONST               2 ('str')

385           LOAD_CONST               3 ('target_enabled')

387           LOAD_CONST               4 ('bool')

385           LOAD_CONST               5 ('return')

388           LOAD_CONST               6 ('Dict[str, Any]')

385           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _live_apply_flag at 0x0000018C17EA7700, file "app\services\memory\approval.py", line 385>:
 385            RESUME                   0

 400            NOP

 401    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('get_brokerage_by_id', 'update_brokerage'))
                IMPORT_NAME              0 (app.db.brokerage_store)
                IMPORT_FROM              1 (get_brokerage_by_id)
                STORE_FAST               2 (get_brokerage_by_id)
                IMPORT_FROM              2 (update_brokerage)
                STORE_FAST               3 (update_brokerage)
                POP_TOP

 408    L2:     NOP

 409    L3:     LOAD_FAST                2 (get_brokerage_by_id)
                PUSH_NULL
                LOAD_FAST                0 (brokerage_id)
                CALL                     1
                STORE_FAST               5 (current)

 417    L4:     LOAD_GLOBAL             17 (isinstance + NULL)
                LOAD_FAST                5 (current)
                LOAD_GLOBAL             18 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L5)
                NOT_TAKEN
                LOAD_FAST                5 (current)
                LOAD_ATTR               21 (get + NULL|self)
                LOAD_CONST               8 ('id')
                CALL                     1
                LOAD_FAST                0 (brokerage_id)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       11 (to L6)
                NOT_TAKEN

 418    L5:     LOAD_CONST               2 ('ok')
                LOAD_CONST               3 (False)
                LOAD_CONST               4 ('error_code')
                LOAD_GLOBAL             22 (ERROR_BROKERAGE_NOT_FOUND)
                BUILD_MAP                2
                RETURN_VALUE

 420    L6:     LOAD_GLOBAL             19 (dict + NULL)
                LOAD_FAST                5 (current)
                LOAD_ATTR               21 (get + NULL|self)
                LOAD_CONST               9 ('features')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L7:     CALL                     1
                STORE_FAST               6 (current_features)

 421            LOAD_GLOBAL             25 (bool + NULL)
                LOAD_FAST                1 (target_enabled)
                CALL                     1
                LOAD_FAST                6 (current_features)
                LOAD_GLOBAL             26 (_ALLOWED_FLAG)
                STORE_SUBSCR

 423            NOP

 424    L8:     LOAD_FAST                3 (update_brokerage)
                PUSH_NULL

 425            LOAD_FAST                0 (brokerage_id)

 426            LOAD_CONST               9 ('features')
                LOAD_FAST                6 (current_features)
                BUILD_MAP                1

 427            LOAD_CONST              10 (True)

 424            LOAD_CONST              11 (('allow_privileged',))
                CALL_KW                  3
                STORE_FAST               7 (ok)

 433    L9:     LOAD_FAST                7 (ok)
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L10)
                NOT_TAKEN

 434            LOAD_CONST               2 ('ok')
                LOAD_CONST               3 (False)
                LOAD_CONST               4 ('error_code')
                LOAD_GLOBAL             28 (ERROR_DB_WRITE_FAILED)
                BUILD_MAP                2
                RETURN_VALUE

 436   L10:     LOAD_CONST               2 ('ok')
                LOAD_CONST              10 (True)
                BUILD_MAP                1
                RETURN_VALUE

  --   L11:     PUSH_EXC_INFO

 404            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       42 (to L16)
                NOT_TAKEN
                STORE_FAST               4 (e)

 405   L12:     LOAD_CONST               2 ('ok')
                LOAD_CONST               3 (False)
                LOAD_CONST               4 ('error_code')
                LOAD_GLOBAL              8 (ERROR_HELPER_IMPORT_FAILED)

 406            LOAD_CONST               5 ('detail')
                LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)

 405            BUILD_MAP                3
       L13:     SWAP                     2
       L14:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RETURN_VALUE

  --   L15:     LOAD_CONST               6 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 404   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L18:     PUSH_EXC_INFO

 410            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       45 (to L23)
                NOT_TAKEN
                STORE_FAST               4 (e)

 411   L19:     LOAD_CONST               2 ('ok')
                LOAD_CONST               3 (False)
                LOAD_CONST               4 ('error_code')
                LOAD_GLOBAL             14 (ERROR_APPLY_EXCEPTION)

 412            LOAD_CONST               5 ('detail')
                LOAD_CONST               7 ('lookup:')
                LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 411            BUILD_MAP                3
       L20:     SWAP                     2
       L21:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RETURN_VALUE

  --   L22:     LOAD_CONST               6 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 410   L23:     RERAISE                  0

  --   L24:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L25:     PUSH_EXC_INFO

 429            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       45 (to L30)
                NOT_TAKEN
                STORE_FAST               4 (e)

 430   L26:     LOAD_CONST               2 ('ok')
                LOAD_CONST               3 (False)
                LOAD_CONST               4 ('error_code')
                LOAD_GLOBAL             14 (ERROR_APPLY_EXCEPTION)

 431            LOAD_CONST               5 ('detail')
                LOAD_CONST              12 ('update:')
                LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 430            BUILD_MAP                3
       L27:     SWAP                     2
       L28:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RETURN_VALUE

  --   L29:     LOAD_CONST               6 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 429   L30:     RERAISE                  0

  --   L31:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L11 [0]
  L3 to L4 -> L18 [0]
  L8 to L9 -> L25 [0]
  L11 to L12 -> L17 [1] lasti
  L12 to L13 -> L15 [1] lasti
  L13 to L14 -> L17 [1] lasti
  L15 to L17 -> L17 [1] lasti
  L18 to L19 -> L24 [1] lasti
  L19 to L20 -> L22 [1] lasti
  L20 to L21 -> L24 [1] lasti
  L22 to L24 -> L24 [1] lasti
  L25 to L26 -> L31 [1] lasti
  L26 to L27 -> L29 [1] lasti
  L27 to L28 -> L31 [1] lasti
  L29 to L31 -> L31 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025230, file "app\services\memory\approval.py", line 443>:
443           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('manifest')

444           LOAD_CONST               2 ('Dict[str, Any]')

443           LOAD_CONST               3 ('dry_run')

446           LOAD_CONST               4 ('bool')

443           LOAD_CONST               5 ('return')

447           LOAD_CONST               2 ('Dict[str, Any]')

443           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object apply_approved_rollout at 0x0000018C17ED3800, file "app\services\memory\approval.py", line 443>:
443            RESUME                   0

469            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (manifest)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L1)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               1 ('plan')
               CALL                     1
               JUMP_FORWARD             1 (to L2)
       L1:     LOAD_CONST               2 (None)
       L2:     STORE_FAST               2 (plan)

470            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (plan)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_FAST                2 (plan)
               JUMP_FORWARD             1 (to L4)
       L3:     BUILD_MAP                0
       L4:     STORE_FAST               2 (plan)

471            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (manifest)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (manifest)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               3 ('approval_id')
               CALL                     1
               JUMP_FORWARD             1 (to L6)
       L5:     LOAD_CONST               2 (None)
       L6:     STORE_FAST               3 (approval_id)

472            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               4 ('brokerage_id')
               CALL                     1
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN
               LOAD_FAST_BORROW         2 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               4 ('brokerage_id')
               CALL                     1
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               2 (None)
       L8:     STORE_FAST               4 (brokerage_id)

473            LOAD_FAST_BORROW         2 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               5 ('recommended_action')
               CALL                     1
               STORE_FAST               5 (recommended_action)

474            LOAD_GLOBAL              9 (_target_enabled + NULL)
               LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (manifest)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_FAST                0 (manifest)
               JUMP_FORWARD             1 (to L10)
       L9:     BUILD_MAP                0
      L10:     CALL                     1
               STORE_FAST               6 (target_enabled)

476            LOAD_GLOBAL             11 (validate_approval_manifest + NULL)
               LOAD_FAST_BORROW         0 (manifest)
               CALL                     1
               STORE_FAST               7 (errors)

477            LOAD_FAST_BORROW         7 (errors)
               TO_BOOL
               POP_JUMP_IF_FALSE       78 (to L11)
               NOT_TAKEN

478            LOAD_GLOBAL             13 (_emit_event + NULL)

479            LOAD_CONST               6 ('memory.rollout.failed')

480            LOAD_FAST_BORROW         3 (approval_id)

481            LOAD_FAST_BORROW         4 (brokerage_id)

482            LOAD_FAST_BORROW         5 (recommended_action)

483            LOAD_FAST_BORROW         6 (target_enabled)

484            LOAD_GLOBAL             15 (bool + NULL)
               LOAD_FAST_BORROW         1 (dry_run)
               CALL                     1

485            LOAD_CONST               7 (False)

486            LOAD_GLOBAL             16 (ERROR_INVALID_MANIFEST)

487            LOAD_CONST               8 ('warning')

478            LOAD_CONST               9 (('approval_id', 'brokerage_id', 'recommended_action', 'target_enabled', 'dry_run', 'applied', 'error_code', 'severity'))
               CALL_KW                  9
               POP_TOP

490            LOAD_CONST              10 ('applied')
               LOAD_CONST               7 (False)

491            LOAD_CONST              11 ('would_apply')
               LOAD_CONST               7 (False)

492            LOAD_CONST              12 ('status')
               LOAD_CONST              13 ('invalid_manifest')

493            LOAD_CONST              14 ('error_code')
               LOAD_GLOBAL             16 (ERROR_INVALID_MANIFEST)

494            LOAD_CONST              15 ('errors')
               LOAD_GLOBAL             19 (list + NULL)
               LOAD_FAST_BORROW         7 (errors)
               CALL                     1

495            LOAD_CONST               3 ('approval_id')
               LOAD_FAST_BORROW         3 (approval_id)

496            LOAD_CONST               4 ('brokerage_id')
               LOAD_FAST_BORROW         4 (brokerage_id)

497            LOAD_CONST               5 ('recommended_action')
               LOAD_FAST_BORROW         5 (recommended_action)

498            LOAD_CONST              16 ('target_enabled')
               LOAD_FAST_BORROW         6 (target_enabled)

499            LOAD_CONST              17 ('dry_run')
               LOAD_GLOBAL             15 (bool + NULL)
               LOAD_FAST_BORROW         1 (dry_run)
               CALL                     1

489            BUILD_MAP               10
               RETURN_VALUE

504   L11:     LOAD_GLOBAL             13 (_emit_event + NULL)

505            LOAD_CONST              18 ('memory.rollout.approved')

506            LOAD_FAST_BORROW         3 (approval_id)

507            LOAD_FAST_BORROW         4 (brokerage_id)

508            LOAD_FAST_BORROW         5 (recommended_action)

509            LOAD_FAST_BORROW         6 (target_enabled)

510            LOAD_GLOBAL             15 (bool + NULL)
               LOAD_FAST_BORROW         1 (dry_run)
               CALL                     1

511            LOAD_CONST               7 (False)

504            LOAD_CONST              19 (('approval_id', 'brokerage_id', 'recommended_action', 'target_enabled', 'dry_run', 'applied'))
               CALL_KW                  7
               POP_TOP

514            LOAD_FAST_BORROW         1 (dry_run)
               TO_BOOL
               POP_JUMP_IF_FALSE       21 (to L12)
               NOT_TAKEN

516            LOAD_CONST              10 ('applied')
               LOAD_CONST               7 (False)

517            LOAD_CONST              11 ('would_apply')
               LOAD_CONST              20 (True)

518            LOAD_CONST              12 ('status')
               LOAD_CONST              17 ('dry_run')

519            LOAD_CONST              14 ('error_code')
               LOAD_CONST               2 (None)

520            LOAD_CONST               3 ('approval_id')
               LOAD_FAST_BORROW         3 (approval_id)

521            LOAD_CONST               4 ('brokerage_id')
               LOAD_FAST_BORROW         4 (brokerage_id)

522            LOAD_CONST               5 ('recommended_action')
               LOAD_FAST_BORROW         5 (recommended_action)

523            LOAD_CONST              16 ('target_enabled')
               LOAD_FAST_BORROW         6 (target_enabled)

524            LOAD_CONST              17 ('dry_run')
               LOAD_CONST              20 (True)

515            BUILD_MAP                9
               RETURN_VALUE

530   L12:     LOAD_GLOBAL             21 (_live_apply_flag + NULL)
               LOAD_FAST                4 (brokerage_id)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L13)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              21 ('')
      L13:     LOAD_GLOBAL             15 (bool + NULL)
               LOAD_FAST_BORROW         6 (target_enabled)
               CALL                     1
               CALL                     2
               STORE_FAST               8 (result)

532            LOAD_FAST_BORROW         8 (result)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              22 ('ok')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        81 (to L15)
               NOT_TAKEN

533            LOAD_GLOBAL              7 (str + NULL)
               LOAD_FAST_BORROW         8 (result)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              14 ('error_code')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         7 (to L14)
               NOT_TAKEN
               POP_TOP
               LOAD_GLOBAL             22 (ERROR_APPLY_EXCEPTION)
      L14:     CALL                     1
               STORE_FAST               9 (error_code)

534            LOAD_GLOBAL             13 (_emit_event + NULL)

535            LOAD_CONST               6 ('memory.rollout.failed')

536            LOAD_FAST_BORROW         3 (approval_id)

537            LOAD_FAST_BORROW         4 (brokerage_id)

538            LOAD_FAST_BORROW         5 (recommended_action)

539            LOAD_FAST_BORROW         6 (target_enabled)

540            LOAD_CONST               7 (False)

541            LOAD_CONST               7 (False)

542            LOAD_FAST_BORROW         9 (error_code)

543            LOAD_CONST              23 ('error')

534            LOAD_CONST               9 (('approval_id', 'brokerage_id', 'recommended_action', 'target_enabled', 'dry_run', 'applied', 'error_code', 'severity'))
               CALL_KW                  9
               POP_TOP

546            LOAD_CONST              10 ('applied')
               LOAD_CONST               7 (False)

547            LOAD_CONST              11 ('would_apply')
               LOAD_CONST              20 (True)

548            LOAD_CONST              12 ('status')
               LOAD_CONST              24 ('apply_failed')

549            LOAD_CONST              14 ('error_code')
               LOAD_FAST_BORROW         9 (error_code)

550            LOAD_CONST               3 ('approval_id')
               LOAD_FAST_BORROW         3 (approval_id)

551            LOAD_CONST               4 ('brokerage_id')
               LOAD_FAST_BORROW         4 (brokerage_id)

552            LOAD_CONST               5 ('recommended_action')
               LOAD_FAST_BORROW         5 (recommended_action)

553            LOAD_CONST              16 ('target_enabled')
               LOAD_FAST_BORROW         6 (target_enabled)

554            LOAD_CONST              17 ('dry_run')
               LOAD_CONST               7 (False)

545            BUILD_MAP                9
               RETURN_VALUE

557   L15:     LOAD_GLOBAL             13 (_emit_event + NULL)

558            LOAD_CONST              25 ('memory.rollout.applied')

559            LOAD_FAST_BORROW         3 (approval_id)

560            LOAD_FAST_BORROW         4 (brokerage_id)

561            LOAD_FAST_BORROW         5 (recommended_action)

562            LOAD_FAST_BORROW         6 (target_enabled)

563            LOAD_CONST               7 (False)

564            LOAD_CONST              20 (True)

557            LOAD_CONST              19 (('approval_id', 'brokerage_id', 'recommended_action', 'target_enabled', 'dry_run', 'applied'))
               CALL_KW                  7
               POP_TOP

567            LOAD_CONST              10 ('applied')
               LOAD_CONST              20 (True)

568            LOAD_CONST              11 ('would_apply')
               LOAD_CONST              20 (True)

569            LOAD_CONST              12 ('status')
               LOAD_CONST              10 ('applied')

570            LOAD_CONST              14 ('error_code')
               LOAD_CONST               2 (None)

571            LOAD_CONST               3 ('approval_id')
               LOAD_FAST_BORROW         3 (approval_id)

572            LOAD_CONST               4 ('brokerage_id')
               LOAD_FAST_BORROW         4 (brokerage_id)

573            LOAD_CONST               5 ('recommended_action')
               LOAD_FAST_BORROW         5 (recommended_action)

574            LOAD_CONST              16 ('target_enabled')
               LOAD_FAST_BORROW         6 (target_enabled)

575            LOAD_CONST              17 ('dry_run')
               LOAD_CONST               7 (False)

566            BUILD_MAP                9
               RETURN_VALUE
```
