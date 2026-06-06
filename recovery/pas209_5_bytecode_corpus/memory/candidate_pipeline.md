# memory/candidate_pipeline

- **pyc:** `app\services\memory\__pycache__\candidate_pipeline.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/candidate_pipeline.py`
- **co_filename (from bytecode):** `app\services\memory\candidate_pipeline.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS163 — Memory candidate pipeline.

Connects post-call observability (a completed call OR a replay
reconstruction) to the PAS Brain Memory Review console by
generating CANDIDATE-status memory records. The pipeline never
auto-approves, never stores raw transcripts, never writes
DANGEROUS / EPHEMERAL records, and never raises into its caller.

Doctrine:

* **Tenant pin from argument only.** Every public function
  requires ``brokerage_id`` as an explicit argument. The
  pipeline never reads ``brokerage_id`` from a payload, lead
  dict, replay bundle, or event row. Whatever appears on the
  input under that key is OVERWRITTEN by the explicit argument
  before classification runs.

* **CANDIDATE only.** Promotion past CANDIDATE is the operator's
  responsibility in the Memory Review UI. This pipeline never
  writes APPROVED, never writes REJECTED, never auto-approves.

* **No DANGEROUS / EPHEMERAL writes from this pipeline.** The
  underlying ``classify_memory_candidate`` is allowed to
  emit DANGEROUS (for prompt-injection) and EPHEMERAL (for
  single-event observations). This pipeline filters those out
  — DANGEROUS quarantine remains the classifier + governance
  layer's job, not the call→memory glue.

* **No raw transcript / raw payload.** The classifier already
  produces a summary/evidence-only record. As belt-and-braces,
  the pipeline strips any evidence key on the raw-text deny-list
  before handing the record off to the storage helper.

* **Fail closed.** Every public function returns a structural
  envelope. Exceptions are caught and surfaced as ``failed``
  with a structural error code. No call to this module can
  break the caller (worker, replay seed, runtime hook).

* **No LLM. No embeddings. No vector DB.** Classification is the
  same deterministic pure function the PAS144 brain ships.

Public surface:

  - build_memory_candidate_from_call(event_bundle, *, brokerage_id)
      -> dict | None
  - generate_memory_candidates_for_call(call_id, brokerage_id,
                                        actor_type, actor_id)
      -> dict
  - generate_memory_candidates_from_replay(replay_or_events, *,
                                           brokerage_id,
                                           actor_type, actor_id)
      -> dict
```

## Imports

`Any`, `Dict`, `List`, `MemoryKind`, `MemoryRecord`, `MemoryStatus`, `Optional`, `__future__`, `annotations`, `app.services.memory.store`, `classifier`, `classify_memory_candidate`, `classify_replay_pattern`, `contracts`, `dataclasses`, `has_forbidden_transcript_field`, `insert_memory`, `logging`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_candidate_from_bundle`, `_empty_report`, `_patterns_to_candidates`, `_persist`, `_records_from_bundles`, `_resolve_insert_memory_helper`, `_run_pipeline_on_bundles`, `_run_pipeline_on_records`, `_sanitize_evidence`, `_sanitize_value`, `_terminal_outcome_from_events`, `build_memory_candidate_from_call`, `generate_memory_candidates_for_call`, `generate_memory_candidates_from_replay`

## Env-key candidates

`SYSTEM`

## String constants (redacted where noted)

- "\nPAS163 — Memory candidate pipeline.\n\nConnects post-call observability (a completed call OR a replay\nreconstruction) to the PAS Brain Memory Review console by\ngenerating CANDIDATE-status memory records. The pipeline never\nauto-approves, never stores raw transcripts, never writes\nDANGEROUS / EPHEMERAL records, and never raises into its caller.\n\nDoctrine:\n\n* **Tenant pin from argument only.** Every public function\n  requires ``brokerage_id`` as an explicit argument. The\n  pipeline never reads ``brokerage_id`` from a payload, lead\n  dict, replay bundle, or event row. Whatever appears on the\n  input under that key is OVERWRITTEN by the explicit argument\n  before classification runs.\n\n* **CANDIDATE only.** Promotion past CANDIDATE is the operator's\n  responsibility in the Memory Review UI. This pipeline never\n  writes APPROVED, never writes REJECTED, never auto-approves.\n\n* **No DANGEROUS / EPHEMERAL writes from this pipeline.** The\n  underlying ``classify_memory_candidate`` is allowed to\n  emit DANGEROUS (for prompt-injection) and EPHEMERAL (for\n  single-event observations). This pipeline filters those out\n  — DANGEROUS quarantine remains the classifier + governance\n  layer's job, not the call→memory glue.\n\n* **No raw transcript / raw payload.** The classifier already\n  produces a summary/evidence-only record. As belt-and-braces,\n  the pipeline strips any evidence key on the raw-text deny-list\n  before handing the record off to the storage helper.\n\n* **Fail closed.** Every public function returns a structural\n  envelope. Exceptions are caught and surfaced as ``failed``\n  with a structural error code. No call to this module can\n  break the caller (worker, replay seed, runtime hook).\n\n* **No LLM. No embeddings. No vector DB.** Classification is the\n  same deterministic pure function the PAS144 brain ships.\n\nPublic surface:\n\n  - build_memory_candidate_from_call(event_bundle, *, brokerage_id)\n      -> dict | None\n  - generate_memory_candidates_for_call(call_id, brokerage_id,\n                                        actor_type, actor_id)\n      -> dict\n  - generate_memory_candidates_from_replay(replay_or_events, *,\n                                           brokerage_id,\n                                           actor_type, actor_id)\n      -> dict\n"
- 'pas.memory.candidate_pipeline'
- 'status'
- 'warnings'
- 'results'
- 'candidates_created'
- 'failed'
- 'actor_type'
- 'SYSTEM'
- 'actor_id'
- 'brokerage_id'
- 'Optional[str]'
- 'str'
- 'Optional[List[str]]'
- 'Optional[List[Dict[str, Any]]]'
- 'int'
- 'return'
- 'Dict[str, Any]'
- 'Any'
- 'Bound a single evidence value to a structural shape. Strings\nare capped; lists are truncated; dicts are flattened to a count\nplaceholder; everything else passes through.'
- '_keys'
- 'evidence'
- 'Strip forbidden keys and bound the value shape. Returns a\nfresh dict — never mutates the input.'
- 'bundle'
- 'Optional[MemoryRecord]'
- 'Produce a single CANDIDATE-status MemoryRecord from a call /\nreplay bundle. Returns None when the bundle has no useful signal\nor when the classifier emits a kind this pipeline refuses to\nsurface (DANGEROUS, EPHEMERAL).\n\nNEVER raises. The classifier is pure-Python and bounded, but we\ncatch exceptions so a malformed bundle cannot escape upward.'
- 'candidate_pipeline classify exception brokerage='
- ' type='
- 'Resolve the PAS144B storage helper. Returns the callable or\nNone when the storage module is unavailable. Never raises.'
- 'record'
- 'MemoryRecord'
- 'Write the candidate via the PAS144B insert helper. The\nhelper is governance-gated and tenant-pinned; we surface its\nresult as a small structural envelope.'
- 'skipped'
- 'memory_id'
- 'missing_storage_helper'
- 'candidate_pipeline persist exception brokerage='
- 'storage_insert_failed:'
- 'storage_dropped_record'
- 'call_record_or_event_bundle'
- 'Optional[Dict[str, Any]]'
- 'Build (but do NOT persist) a CANDIDATE memory record dict\nfrom a call record or event bundle.\n\nReturns the dict form of the MemoryRecord, or None when the\nbundle yields no surfaceable candidate. Never raises.\n\n``brokerage_id`` is required; passing an empty / non-string\nvalue returns None.\n'
- 'call_id'
- 'Generate CANDIDATE memory record(s) for a completed call.\n\nPAS163 does NOT fetch the call from the database directly —\nthe seed and runtime hook hand the bundle in via\n``generate_memory_candidates_from_replay``. This entry point\nsurfaces the structural shape callers expect from a future\nDB-backed variant; for now it builds a minimal event bundle\nfrom ``call_id`` and runs the same classifier path.\n\nReturns the closed-shape report. Never raises.\n'
- 'missing_brokerage_id'
- 'missing_call_id'
- 'replay_or_events'
- 'Generate CANDIDATE memory record(s) from a replay\nreconstruction or a list of events.\n\nAccepts either:\n  * a replay reconstruction dict (as produced by\n    ``app/services/replay/reconstruction.py:reconstruct_call``);\n  * a list of normalized events (mostly for testing — we wrap\n    the list into a minimal reconstruction-shaped dict).\n\nReturns the closed-shape report. Never raises.\n'
- 'candidate_pipeline replay-pattern exception brokerage='
- 'events_count'
- 'final_outcome'
- 'missing_lifecycle_steps'
- 'replay_or_events_bad_shape'
- 'events'
- 'List[Any]'
- 'event_type'
- 'call.failed'
- 'outcome_state'
- 'payload'
- 'outcome'
- 'bundles'
- 'List[Dict[str, Any]]'
- 'List[Optional[MemoryRecord]]'
- 'patterns'
- 'List[MemoryRecord]'
- "Sanitise + force-CANDIDATE the classifier's replay-pattern\nrecords. DANGEROUS and EPHEMERAL records are dropped (returned\nas None placeholders so the caller's counters stay aligned)."
- 'records'
- 'kind'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ("\nPAS163 — Memory candidate pipeline.\n\nConnects post-call observability (a completed call OR a replay\nreconstruction) to the PAS Brain Memory Review console by\ngenerating CANDIDATE-status memory records. The pipeline never\nauto-approves, never stores raw transcripts, never writes\nDANGEROUS / EPHEMERAL records, and never raises into its caller.\n\nDoctrine:\n\n* **Tenant pin from argument only.** Every public function\n  requires ``brokerage_id`` as an explicit argument. The\n  pipeline never reads ``brokerage_id`` from a payload, lead\n  dict, replay bundle, or event row. Whatever appears on the\n  input under that key is OVERWRITTEN by the explicit argument\n  before classification runs.\n\n* **CANDIDATE only.** Promotion past CANDIDATE is the operator's\n  responsibility in the Memory Review UI. This pipeline never\n  writes APPROVED, never writes REJECTED, never auto-approves.\n\n* **No DANGEROUS / EPHEMERAL writes from this pipeline.** The\n  underlying ``classify_memory_candidate`` is allowed to\n  emit DANGEROUS (for prompt-injection) and EPHEMERAL (for\n  single-event observations). This pipeline filters those out\n  — DANGEROUS quarantine remains the classifier + governance\n  layer's job, not the call→memory glue.\n\n* **No raw transcript / raw payload.** The classifier already\n  produces a summary/evidence-only record. As belt-and-braces,\n  the pipeline strips any evidence key on the raw-text deny-list\n  before handing the record off to the storage helper.\n\n* **Fail closed.** Every public function returns a structural\n  envelope. Exceptions are caught and surfaced as ``failed``\n  with a structural error code. No call to this module can\n  break the caller (worker, replay seed, runtime hook).\n\n* **No LLM. No embeddings. No vector DB.** Classification is the\n  same deterministic pure function the PAS144 brain ships.\n\nPublic surface:\n\n  - build_memory_candidate_from_call(event_bundle, *, brokerage_id)\n      -> dict | None\n  - generate_memory_candidates_for_call(call_id, brokerage_id,\n                                        actor_type, actor_id)\n      -> dict\n  - generate_memory_candidates_from_replay(replay_or_events, *,\n                                           brokerage_id,\n                                           actor_type, actor_id)\n      -> dict\n")
              STORE_NAME               0 (__doc__)

 56           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 58           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (dataclasses)
              STORE_NAME               3 (dataclasses)

 59           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (logging)
              STORE_NAME               4 (logging)

 60           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              5 (typing)
              IMPORT_FROM              6 (Any)
              STORE_NAME               6 (Any)
              IMPORT_FROM              7 (Dict)
              STORE_NAME               7 (Dict)
              IMPORT_FROM              8 (List)
              STORE_NAME               8 (List)
              IMPORT_FROM              9 (Optional)
              STORE_NAME               9 (Optional)
              POP_TOP

 62           LOAD_SMALL_INT           1
              LOAD_CONST               4 (('classify_memory_candidate', 'classify_replay_pattern'))
              IMPORT_NAME             10 (classifier)
              IMPORT_FROM             11 (classify_memory_candidate)
              STORE_NAME              11 (classify_memory_candidate)
              IMPORT_FROM             12 (classify_replay_pattern)
              STORE_NAME              12 (classify_replay_pattern)
              POP_TOP

 66           LOAD_SMALL_INT           1
              LOAD_CONST               5 (('MemoryKind', 'MemoryRecord', 'MemoryStatus', 'has_forbidden_transcript_field'))
              IMPORT_NAME             13 (contracts)
              IMPORT_FROM             14 (MemoryKind)
              STORE_NAME              14 (MemoryKind)
              IMPORT_FROM             15 (MemoryRecord)
              STORE_NAME              15 (MemoryRecord)
              IMPORT_FROM             16 (MemoryStatus)
              STORE_NAME              16 (MemoryStatus)
              IMPORT_FROM             17 (has_forbidden_transcript_field)
              STORE_NAME              17 (has_forbidden_transcript_field)
              POP_TOP

 73           LOAD_NAME                4 (logging)
              LOAD_ATTR               36 (getLogger)
              PUSH_NULL
              LOAD_CONST               6 ('pas.memory.candidate_pipeline')
              CALL                     1
              STORE_NAME              19 (logger)

 80           LOAD_CONST               7 ('status')

 83           LOAD_CONST               8 ('ok')

 80           LOAD_CONST               9 ('warnings')

 84           LOAD_CONST               2 (None)

 80           LOAD_CONST              10 ('results')

 85           LOAD_CONST               2 (None)

 80           LOAD_CONST              11 ('candidates_created')

 86           LOAD_SMALL_INT           0

 80           LOAD_CONST              12 ('failed')

 87           LOAD_SMALL_INT           0

 80           BUILD_MAP                5
              LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18090690, file "app\services\memory\candidate_pipeline.py", line 80>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object _empty_report at 0x0000018C18010F50, file "app\services\memory\candidate_pipeline.py", line 80>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              20 (_empty_report)

108           LOAD_NAME               21 (frozenset)
              PUSH_NULL
              BUILD_SET                0
              LOAD_CONST              44 (frozenset({'raw_payload', 'name', 'transcript', 'prompt', 'full_name', 'full_transcript', 'turns_text', 'utterances', 'raw_transcript', 'messages', 'raw_text', 'evidence_text', 'phone', 'transcripts', 'injected_prompt', 'raw_prompt', 'output_text', 'email', 'full_payload', 'input_text'}))
              SET_UPDATE               1
              CALL                     1
              STORE_NAME              22 (_FORBIDDEN_EVIDENCE_KEYS)

121           LOAD_SMALL_INT          16
              STORE_NAME              23 (_MAX_EVIDENCE_KEYS)

122           LOAD_CONST              15 (256)
              STORE_NAME              24 (_MAX_EVIDENCE_STR_LEN)

123           LOAD_SMALL_INT          10
              STORE_NAME              25 (_MAX_EVIDENCE_LIST_LEN)

126           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA2D30, file "app\services\memory\candidate_pipeline.py", line 126>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _sanitize_value at 0x0000018C17D6DFC0, file "app\services\memory\candidate_pipeline.py", line 126>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_sanitize_value)

152           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3960, file "app\services\memory\candidate_pipeline.py", line 152>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object _sanitize_evidence at 0x0000018C179A7290, file "app\services\memory\candidate_pipeline.py", line 152>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_sanitize_evidence)

174           LOAD_CONST              20 ('actor_type')

178           LOAD_CONST              21 ('SYSTEM')

174           LOAD_CONST              22 ('actor_id')

179           LOAD_CONST               2 (None)

174           BUILD_MAP                2
              LOAD_CONST              23 (<code object __annotate__ at 0x0000018C18024E30, file "app\services\memory\candidate_pipeline.py", line 174>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object _candidate_from_bundle at 0x0000018C17E8DE50, file "app\services\memory\candidate_pipeline.py", line 174>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              28 (_candidate_from_bundle)

254           LOAD_CONST              25 (<code object _resolve_insert_memory_helper at 0x0000018C1802C4F0, file "app\services\memory\candidate_pipeline.py", line 254>)
              MAKE_FUNCTION
              STORE_NAME              29 (_resolve_insert_memory_helper)

266           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\memory\candidate_pipeline.py", line 266>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object _persist at 0x0000018C17CC2460, file "app\services\memory\candidate_pipeline.py", line 266>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_persist)

309           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\memory\candidate_pipeline.py", line 309>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object build_memory_candidate_from_call at 0x0000018C1794E810, file "app\services\memory\candidate_pipeline.py", line 309>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (build_memory_candidate_from_call)

337           LOAD_CONST              45 (('SYSTEM', None))
              LOAD_CONST              30 (<code object __annotate__ at 0x0000018C18025230, file "app\services\memory\candidate_pipeline.py", line 337>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object generate_memory_candidates_for_call at 0x0000018C17ED5400, file "app\services\memory\candidate_pipeline.py", line 337>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              32 (generate_memory_candidates_for_call)

384           LOAD_CONST              20 ('actor_type')

388           LOAD_CONST              21 ('SYSTEM')

384           LOAD_CONST              22 ('actor_id')

389           LOAD_CONST               2 (None)

384           BUILD_MAP                2
              LOAD_CONST              32 (<code object __annotate__ at 0x0000018C18025D30, file "app\services\memory\candidate_pipeline.py", line 384>)
              MAKE_FUNCTION
              LOAD_CONST              33 (<code object generate_memory_candidates_from_replay at 0x0000018C17D7C560, file "app\services\memory\candidate_pipeline.py", line 384>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              33 (generate_memory_candidates_from_replay)

469           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA35A0, file "app\services\memory\candidate_pipeline.py", line 469>)
              MAKE_FUNCTION
              LOAD_CONST              35 (<code object _terminal_outcome_from_events at 0x0000018C17F0C960, file "app\services\memory\candidate_pipeline.py", line 469>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              34 (_terminal_outcome_from_events)

487           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C18025030, file "app\services\memory\candidate_pipeline.py", line 487>)
              MAKE_FUNCTION
              LOAD_CONST              37 (<code object _records_from_bundles at 0x0000018C1802C9B0, file "app\services\memory\candidate_pipeline.py", line 487>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              35 (_records_from_bundles)

504           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C18025E30, file "app\services\memory\candidate_pipeline.py", line 504>)
              MAKE_FUNCTION
              LOAD_CONST              39 (<code object _patterns_to_candidates at 0x0000018C17F78460, file "app\services\memory\candidate_pipeline.py", line 504>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              36 (_patterns_to_candidates)

539           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C18024B30, file "app\services\memory\candidate_pipeline.py", line 539>)
              MAKE_FUNCTION
              LOAD_CONST              41 (<code object _run_pipeline_on_bundles at 0x0000018C18090030, file "app\services\memory\candidate_pipeline.py", line 539>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              37 (_run_pipeline_on_bundles)

553           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C18025F30, file "app\services\memory\candidate_pipeline.py", line 553>)
              MAKE_FUNCTION
              LOAD_CONST              43 (<code object _run_pipeline_on_records at 0x0000018C17F731A0, file "app\services\memory\candidate_pipeline.py", line 553>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              38 (_run_pipeline_on_records)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18090690, file "app\services\memory\candidate_pipeline.py", line 80>:
 80           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

 81           LOAD_CONST               2 ('Optional[str]')

 80           LOAD_CONST               3 ('status')

 83           LOAD_CONST               4 ('str')

 80           LOAD_CONST               5 ('warnings')

 84           LOAD_CONST               6 ('Optional[List[str]]')

 80           LOAD_CONST               7 ('results')

 85           LOAD_CONST               8 ('Optional[List[Dict[str, Any]]]')

 80           LOAD_CONST               9 ('candidates_created')

 86           LOAD_CONST              10 ('int')

 80           LOAD_CONST              11 ('failed')

 87           LOAD_CONST              10 ('int')

 80           LOAD_CONST              12 ('return')

 88           LOAD_CONST              13 ('Dict[str, Any]')

 80           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object _empty_report at 0x0000018C18010F50, file "app\services\memory\candidate_pipeline.py", line 80>:
 80           RESUME                   0

 90           LOAD_CONST               0 ('status')
              LOAD_FAST                1 (status)

 91           LOAD_CONST               1 ('brokerage_id')
              LOAD_FAST                0 (brokerage_id)

 92           LOAD_CONST               2 ('candidates_created')
              LOAD_GLOBAL              1 (int + NULL)
              LOAD_FAST_BORROW         4 (candidates_created)
              CALL                     1

 93           LOAD_CONST               3 ('failed')
              LOAD_GLOBAL              1 (int + NULL)
              LOAD_FAST_BORROW         5 (failed)
              CALL                     1

 94           LOAD_CONST               4 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                2 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

 95           LOAD_CONST               5 ('results')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                3 (results)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L2:     CALL                     1

 89           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app\services\memory\candidate_pipeline.py", line 126>:
126           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('v')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('Any')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _sanitize_value at 0x0000018C17D6DFC0, file "app\services\memory\candidate_pipeline.py", line 126>:
126            RESUME                   0

130            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (v)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       10 (to L1)
               NOT_TAKEN

131            LOAD_FAST_BORROW         0 (v)
               LOAD_CONST               1 (None)
               LOAD_GLOBAL              4 (_MAX_EVIDENCE_STR_LEN)
               BINARY_SLICE
               RETURN_VALUE

132    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (v)
               LOAD_GLOBAL              6 (list)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE      165 (to L7)
               NOT_TAKEN

133            BUILD_LIST               0
               STORE_FAST               1 (out)

134            LOAD_FAST_BORROW         0 (v)
               LOAD_CONST               1 (None)
               LOAD_GLOBAL              8 (_MAX_EVIDENCE_LIST_LEN)
               BINARY_SLICE
               GET_ITER
       L2:     FOR_ITER               147 (to L6)
               STORE_FAST               2 (item)

135            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (item)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       27 (to L3)
               NOT_TAKEN

136            LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         2 (item)
               LOAD_CONST               1 (None)
               LOAD_GLOBAL              4 (_MAX_EVIDENCE_STR_LEN)
               BINARY_SLICE
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           51 (to L2)

137    L3:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (item)
               LOAD_GLOBAL             12 (int)
               LOAD_GLOBAL             14 (float)
               LOAD_GLOBAL             16 (bool)
               BUILD_TUPLE              3
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         5 (to L4)
               NOT_TAKEN
               LOAD_FAST_BORROW         2 (item)
               POP_JUMP_IF_NOT_NONE    20 (to L5)
               NOT_TAKEN

138    L4:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         2 (item)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          107 (to L2)

143    L5:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               2 ('<')
               LOAD_GLOBAL             19 (type + NULL)
               LOAD_FAST_BORROW         2 (item)
               CALL                     1
               LOAD_ATTR               20 (__name__)
               FORMAT_SIMPLE
               LOAD_CONST               3 ('>')
               BUILD_STRING             3
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          149 (to L2)

134    L6:     END_FOR
               POP_ITER

144            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

145    L7:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (v)
               LOAD_GLOBAL             22 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       14 (to L8)
               NOT_TAKEN

146            LOAD_CONST               4 ('_keys')
               LOAD_GLOBAL             25 (len + NULL)
               LOAD_FAST_BORROW         0 (v)
               CALL                     1
               BUILD_MAP                1
               RETURN_VALUE

147    L8:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (v)
               LOAD_GLOBAL             12 (int)
               LOAD_GLOBAL             14 (float)
               LOAD_GLOBAL             16 (bool)
               BUILD_TUPLE              3
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         5 (to L9)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (v)
               POP_JUMP_IF_NOT_NONE     3 (to L10)
               NOT_TAKEN

148    L9:     LOAD_FAST_BORROW         0 (v)
               RETURN_VALUE

149   L10:     LOAD_CONST               2 ('<')
               LOAD_GLOBAL             19 (type + NULL)
               LOAD_FAST_BORROW         0 (v)
               CALL                     1
               LOAD_ATTR               20 (__name__)
               FORMAT_SIMPLE
               LOAD_CONST               3 ('>')
               BUILD_STRING             3
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app\services\memory\candidate_pipeline.py", line 152>:
152           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('evidence')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _sanitize_evidence at 0x0000018C179A7290, file "app\services\memory\candidate_pipeline.py", line 152>:
152           RESUME                   0

155           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (evidence)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

156           BUILD_MAP                0
              RETURN_VALUE

157   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

158           LOAD_FAST_BORROW         0 (evidence)
              LOAD_ATTR                5 (items + NULL|self)
              CALL                     0
              GET_ITER
      L2:     FOR_ITER                92 (to L6)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   35 (k, v)

159           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (k)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

160           JUMP_BACKWARD           29 (to L2)

161   L3:     LOAD_FAST_BORROW         2 (k)
              LOAD_ATTR                9 (lower + NULL|self)
              CALL                     0
              LOAD_GLOBAL             10 (_FORBIDDEN_EVIDENCE_KEYS)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN

162           JUMP_BACKWARD           56 (to L2)

163   L4:     LOAD_GLOBAL             13 (_sanitize_value + NULL)
              LOAD_FAST_BORROW         3 (v)
              CALL                     1
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, k)
              STORE_SUBSCR

164           LOAD_GLOBAL             15 (len + NULL)
              LOAD_FAST_BORROW         1 (out)
              CALL                     1
              LOAD_GLOBAL             16 (_MAX_EVIDENCE_KEYS)
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           91 (to L2)

165   L5:     POP_TOP

166           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

158   L6:     END_FOR
              POP_ITER

166           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app\services\memory\candidate_pipeline.py", line 174>:
174           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('bundle')

175           LOAD_CONST               2 ('Dict[str, Any]')

174           LOAD_CONST               3 ('brokerage_id')

177           LOAD_CONST               4 ('str')

174           LOAD_CONST               5 ('actor_type')

178           LOAD_CONST               4 ('str')

174           LOAD_CONST               6 ('actor_id')

179           LOAD_CONST               7 ('Optional[str]')

174           LOAD_CONST               8 ('return')

180           LOAD_CONST               9 ('Optional[MemoryRecord]')

174           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _candidate_from_bundle at 0x0000018C17E8DE50, file "app\services\memory\candidate_pipeline.py", line 174>:
 174            RESUME                   0

 188            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (bundle)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 189            LOAD_CONST               1 (None)
                RETURN_VALUE

 193    L1:     LOAD_GLOBAL              3 (dict + NULL)
                LOAD_FAST_BORROW         0 (bundle)
                CALL                     1
                STORE_FAST               4 (classifier_input)

 194            LOAD_FAST_BORROW_LOAD_FAST_BORROW 20 (brokerage_id, classifier_input)
                LOAD_CONST               2 ('brokerage_id')
                STORE_SUBSCR

 196            NOP

 197    L2:     LOAD_GLOBAL              5 (classify_memory_candidate + NULL)
                LOAD_FAST_BORROW         4 (classifier_input)
                CALL                     1
                STORE_FAST               5 (rec)

 205    L3:     LOAD_FAST                5 (rec)
                POP_JUMP_IF_NOT_NONE     3 (to L4)
                NOT_TAKEN

 206            LOAD_CONST               1 (None)
                RETURN_VALUE

 207    L4:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST                5 (rec)
                LOAD_GLOBAL             16 (MemoryRecord)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN

 208            LOAD_CONST               1 (None)
                RETURN_VALUE

 214    L5:     LOAD_FAST                5 (rec)
                LOAD_ATTR               18 (kind)
                LOAD_GLOBAL             20 (MemoryKind)
                LOAD_ATTR               22 (DANGEROUS)
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN

 215            LOAD_CONST               1 (None)
                RETURN_VALUE

 216    L6:     LOAD_FAST                5 (rec)
                LOAD_ATTR               18 (kind)
                LOAD_GLOBAL             20 (MemoryKind)
                LOAD_ATTR               24 (EPHEMERAL)
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN

 217            LOAD_CONST               1 (None)
                RETURN_VALUE

 220    L7:     LOAD_GLOBAL             27 (_sanitize_evidence + NULL)
                LOAD_FAST                5 (rec)
                LOAD_ATTR               28 (evidence)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L8:     CALL                     1
                STORE_FAST               7 (safe_evidence)

 226            LOAD_GLOBAL              3 (dict + NULL)
                LOAD_FAST                5 (rec)
                LOAD_ATTR               30 (lineage)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L9:     CALL                     1
                STORE_FAST               8 (lineage)

 227            LOAD_FAST                8 (lineage)
                LOAD_ATTR               33 (setdefault + NULL|self)
                LOAD_CONST               5 ('actor_type')
                LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST                2 (actor_type)
                LOAD_GLOBAL             34 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_FAST                2 (actor_type)
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST               6 ('SYSTEM')
       L11:     CALL                     2
                POP_TOP

 228            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST                3 (actor_id)
                LOAD_GLOBAL             34 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       55 (to L12)
                NOT_TAKEN
                LOAD_FAST                3 (actor_id)
                LOAD_ATTR               37 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       33 (to L12)
                NOT_TAKEN

 229            LOAD_FAST                8 (lineage)
                LOAD_ATTR               33 (setdefault + NULL|self)
                LOAD_CONST               7 ('actor_id')
                LOAD_FAST                3 (actor_id)
                LOAD_ATTR               37 (strip + NULL|self)
                CALL                     0
                CALL                     2
                POP_TOP

 233   L12:     LOAD_GLOBAL             38 (dataclasses)
                LOAD_ATTR               40 (replace)
                PUSH_NULL

 234            LOAD_FAST                5 (rec)

 235            LOAD_GLOBAL             42 (MemoryStatus)
                LOAD_ATTR               44 (CANDIDATE)

 236            LOAD_FAST                7 (safe_evidence)

 237            LOAD_FAST                8 (lineage)

 233            LOAD_CONST               8 (('status', 'evidence', 'lineage'))
                CALL_KW                  4
                STORE_FAST               9 (candidate)

 244            LOAD_GLOBAL             47 (has_forbidden_transcript_field + NULL)
                LOAD_FAST                9 (candidate)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN

 245            LOAD_CONST               1 (None)
                RETURN_VALUE

 247   L13:     LOAD_FAST                9 (candidate)
                RETURN_VALUE

  --   L14:     PUSH_EXC_INFO

 198            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       58 (to L18)
                NOT_TAKEN
                STORE_FAST               6 (e)

 199   L15:     LOAD_GLOBAL              8 (logger)
                LOAD_ATTR               11 (warning + NULL|self)

 200            LOAD_CONST               3 ('candidate_pipeline classify exception brokerage=')

 201            LOAD_FAST                1 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST               4 (' type=')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE

 200            BUILD_STRING             4

 199            CALL                     1
                POP_TOP

 203   L16:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                LOAD_CONST               1 (None)
                RETURN_VALUE

  --   L17:     LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 198   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L14 [0]
  L14 to L15 -> L19 [1] lasti
  L15 to L16 -> L17 [1] lasti
  L17 to L19 -> L19 [1] lasti

Disassembly of <code object _resolve_insert_memory_helper at 0x0000018C1802C4F0, file "app\services\memory\candidate_pipeline.py", line 254>:
 254           RESUME                   0

 257           NOP

 258   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('insert_memory',))
               IMPORT_NAME              0 (app.services.memory.store)
               IMPORT_FROM              1 (insert_memory)
               STORE_FAST               0 (insert_memory)
               POP_TOP

 259           LOAD_GLOBAL              5 (callable + NULL)
               LOAD_FAST_BORROW         0 (insert_memory)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 260           LOAD_FAST_BORROW         0 (insert_memory)
       L2:     RETURN_VALUE

 259   L3:     NOP

 263           LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

 261           LOAD_GLOBAL              6 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L6)
               NOT_TAKEN
               POP_TOP

 262   L5:     POP_EXCEPT

 263           LOAD_CONST               2 (None)
               RETURN_VALUE

 261   L6:     RERAISE                  0

  --   L7:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L4 [0]
  L4 to L5 -> L7 [1] lasti
  L6 to L7 -> L7 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\memory\candidate_pipeline.py", line 266>:
266           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record')
              LOAD_CONST               2 ('MemoryRecord')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _persist at 0x0000018C17CC2460, file "app\services\memory\candidate_pipeline.py", line 266>:
 266            RESUME                   0

 270            LOAD_GLOBAL              1 (_resolve_insert_memory_helper + NULL)
                CALL                     0
                STORE_FAST               1 (insert)

 271            LOAD_FAST_BORROW         1 (insert)
                POP_JUMP_IF_NOT_NONE    20 (to L1)
                NOT_TAKEN

 273            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('skipped')

 274            LOAD_CONST               4 ('memory_id')
                LOAD_FAST_BORROW         0 (record)
                LOAD_ATTR                2 (memory_id)

 275            LOAD_CONST               5 ('warnings')
                LOAD_CONST               6 ('missing_storage_helper')
                BUILD_LIST               1

 272            BUILD_MAP                3
                RETURN_VALUE

 277    L1:     NOP

 278    L2:     LOAD_FAST_BORROW         1 (insert)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (record)
                CALL                     1
                STORE_FAST               2 (row)

 289    L3:     LOAD_FAST                2 (row)
                TO_BOOL
                POP_JUMP_IF_TRUE        20 (to L4)
                NOT_TAKEN

 294            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('skipped')

 295            LOAD_CONST               4 ('memory_id')
                LOAD_FAST                0 (record)
                LOAD_ATTR                2 (memory_id)

 296            LOAD_CONST               5 ('warnings')
                LOAD_CONST              11 ('storage_dropped_record')
                BUILD_LIST               1

 293            BUILD_MAP                3
                RETURN_VALUE

 299    L4:     LOAD_CONST               2 ('status')
                LOAD_CONST              12 ('ok')

 300            LOAD_CONST               4 ('memory_id')
                LOAD_FAST                0 (record)
                LOAD_ATTR                2 (memory_id)

 301            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 298            BUILD_MAP                3
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 279            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      108 (to L10)
                NOT_TAKEN
                STORE_FAST               3 (e)

 280    L6:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 281            LOAD_CONST               7 ('candidate_pipeline persist exception brokerage=')

 282            LOAD_FAST                0 (record)
                LOAD_ATTR               10 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST               8 (' type=')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE

 281            BUILD_STRING             4

 280            CALL                     1
                POP_TOP

 285            LOAD_CONST               2 ('status')
                LOAD_CONST               9 ('failed')

 286            LOAD_CONST               4 ('memory_id')
                LOAD_FAST                0 (record)
                LOAD_ATTR                2 (memory_id)

 287            LOAD_CONST               5 ('warnings')
                LOAD_CONST              10 ('storage_insert_failed:')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 284            BUILD_MAP                3
        L7:     SWAP                     2
        L8:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --    L9:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 279   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L5 [0]
  L5 to L6 -> L11 [1] lasti
  L6 to L7 -> L9 [1] lasti
  L7 to L8 -> L11 [1] lasti
  L9 to L11 -> L11 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\memory\candidate_pipeline.py", line 309>:
309           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('call_record_or_event_bundle')

310           LOAD_CONST               2 ('Any')

309           LOAD_CONST               3 ('brokerage_id')

312           LOAD_CONST               4 ('str')

309           LOAD_CONST               5 ('return')

313           LOAD_CONST               6 ('Optional[Dict[str, Any]]')

309           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object build_memory_candidate_from_call at 0x0000018C1794E810, file "app\services\memory\candidate_pipeline.py", line 309>:
309           RESUME                   0

323           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (brokerage_id)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (brokerage_id)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

324   L1:     LOAD_CONST               1 (None)
              RETURN_VALUE

325   L2:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (call_record_or_event_bundle)
              LOAD_GLOBAL              6 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

326           LOAD_CONST               1 (None)
              RETURN_VALUE

327   L3:     LOAD_FAST_BORROW         1 (brokerage_id)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (bid)

328           LOAD_GLOBAL              9 (_candidate_from_bundle + NULL)

329           LOAD_FAST_BORROW         0 (call_record_or_event_bundle)

330           LOAD_FAST_BORROW         2 (bid)

328           LOAD_CONST               2 (('brokerage_id',))
              CALL_KW                  2
              STORE_FAST               3 (rec)

332           LOAD_FAST_BORROW         3 (rec)
              POP_JUMP_IF_NOT_NONE     3 (to L4)
              NOT_TAKEN

333           LOAD_CONST               1 (None)
              RETURN_VALUE

334   L4:     LOAD_FAST_BORROW         3 (rec)
              LOAD_ATTR               11 (to_dict + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025230, file "app\services\memory\candidate_pipeline.py", line 337>:
337           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('call_id')

338           LOAD_CONST               2 ('str')

337           LOAD_CONST               3 ('brokerage_id')

339           LOAD_CONST               2 ('str')

337           LOAD_CONST               4 ('actor_type')

340           LOAD_CONST               2 ('str')

337           LOAD_CONST               5 ('actor_id')

341           LOAD_CONST               6 ('Optional[str]')

337           LOAD_CONST               7 ('return')

342           LOAD_CONST               8 ('Dict[str, Any]')

337           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object generate_memory_candidates_for_call at 0x0000018C17ED5400, file "app\services\memory\candidate_pipeline.py", line 337>:
337           RESUME                   0

354           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (brokerage_id)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (brokerage_id)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE        16 (to L2)
              NOT_TAKEN

355   L1:     LOAD_GLOBAL              7 (_empty_report + NULL)

356           LOAD_CONST               1 (None)

357           LOAD_CONST               2 ('failed')

358           LOAD_CONST               3 ('missing_brokerage_id')
              BUILD_LIST               1

355           LOAD_CONST               4 (('status', 'warnings'))
              CALL_KW                  3
              RETURN_VALUE

360   L2:     LOAD_FAST_BORROW         1 (brokerage_id)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               4 (bid)

361           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (call_id)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (call_id)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE        16 (to L4)
              NOT_TAKEN

362   L3:     LOAD_GLOBAL              7 (_empty_report + NULL)

363           LOAD_FAST_BORROW         4 (bid)

364           LOAD_CONST               2 ('failed')

365           LOAD_CONST               5 ('missing_call_id')
              BUILD_LIST               1

362           LOAD_CONST               4 (('status', 'warnings'))
              CALL_KW                  3
              RETURN_VALUE

369   L4:     LOAD_CONST               6 ('call_id')
              LOAD_FAST_BORROW         0 (call_id)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0

370           LOAD_CONST               7 ('brokerage_id')
              LOAD_FAST_BORROW         4 (bid)

368           BUILD_MAP                2
              STORE_FAST               5 (bundle)

378           LOAD_GLOBAL              9 (_run_pipeline_on_bundles + NULL)

379           LOAD_FAST_BORROW         5 (bundle)
              BUILD_LIST               1
              LOAD_FAST_BORROW         4 (bid)

380           LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (actor_type, actor_id)

378           LOAD_CONST               8 (('brokerage_id', 'actor_type', 'actor_id'))
              CALL_KW                  4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\services\memory\candidate_pipeline.py", line 384>:
384           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('replay_or_events')

385           LOAD_CONST               2 ('Any')

384           LOAD_CONST               3 ('brokerage_id')

387           LOAD_CONST               4 ('str')

384           LOAD_CONST               5 ('actor_type')

388           LOAD_CONST               4 ('str')

384           LOAD_CONST               6 ('actor_id')

389           LOAD_CONST               7 ('Optional[str]')

384           LOAD_CONST               8 ('return')

390           LOAD_CONST               9 ('Dict[str, Any]')

384           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object generate_memory_candidates_from_replay at 0x0000018C17D7C560, file "app\services\memory\candidate_pipeline.py", line 384>:
 384            RESUME                   0

 402            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        16 (to L2)
                NOT_TAKEN

 403    L1:     LOAD_GLOBAL              7 (_empty_report + NULL)

 404            LOAD_CONST               1 (None)

 405            LOAD_CONST               2 ('failed')

 406            LOAD_CONST               3 ('missing_brokerage_id')
                BUILD_LIST               1

 403            LOAD_CONST               4 (('status', 'warnings'))
                CALL_KW                  3
                RETURN_VALUE

 408    L2:     LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               4 (bid)

 410            BUILD_LIST               0
                STORE_FAST               5 (bundles)

 411            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (replay_or_events)
                LOAD_GLOBAL              8 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       87 (to L5)
                NOT_TAKEN

 413            LOAD_GLOBAL              9 (dict + NULL)
                LOAD_FAST_BORROW         0 (replay_or_events)
                CALL                     1
                STORE_FAST               6 (reconstruction)

 414            LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (bid, reconstruction)
                LOAD_CONST               5 ('brokerage_id')
                STORE_SUBSCR

 415            LOAD_FAST_BORROW         5 (bundles)
                LOAD_ATTR               11 (append + NULL|self)
                LOAD_FAST_BORROW         6 (reconstruction)
                CALL                     1
                POP_TOP

 421            NOP

 422    L3:     LOAD_GLOBAL             13 (classify_replay_pattern + NULL)
                LOAD_FAST_BORROW         6 (reconstruction)
                CALL                     1
                STORE_FAST               7 (patterns)

 433    L4:     LOAD_GLOBAL             25 (_run_pipeline_on_records + NULL)

 434            LOAD_GLOBAL             27 (_records_from_bundles + NULL)

 435            LOAD_FAST_BORROW_LOAD_FAST_BORROW 84 (bundles, bid)

 436            LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (actor_type, actor_id)

 434            LOAD_CONST               8 (('brokerage_id', 'actor_type', 'actor_id'))
                CALL_KW                  4

 437            LOAD_GLOBAL             29 (_patterns_to_candidates + NULL)

 438            LOAD_FAST_BORROW_LOAD_FAST_BORROW 114 (patterns, actor_type)
                LOAD_FAST_BORROW         3 (actor_id)

 437            LOAD_CONST               9 (('actor_type', 'actor_id'))
                CALL_KW                  3

 434            BINARY_OP                0 (+)

 440            LOAD_FAST_BORROW         4 (bid)

 433            LOAD_CONST              10 (('brokerage_id',))
                CALL_KW                  2
                RETURN_VALUE

 443    L5:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (replay_or_events)
                LOAD_GLOBAL             30 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       59 (to L6)
                NOT_TAKEN

 447            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST_BORROW         4 (bid)

 448            LOAD_CONST              11 ('events_count')
                LOAD_GLOBAL             33 (len + NULL)
                LOAD_FAST_BORROW         0 (replay_or_events)
                CALL                     1

 449            LOAD_CONST              12 ('final_outcome')
                LOAD_GLOBAL             35 (_terminal_outcome_from_events + NULL)
                LOAD_FAST_BORROW         0 (replay_or_events)
                CALL                     1

 450            LOAD_CONST              13 ('missing_lifecycle_steps')
                BUILD_LIST               0

 446            BUILD_MAP                4
                STORE_FAST               6 (reconstruction)

 452            LOAD_FAST_BORROW         5 (bundles)
                LOAD_ATTR               11 (append + NULL|self)
                LOAD_FAST_BORROW         6 (reconstruction)
                CALL                     1
                POP_TOP

 453            LOAD_GLOBAL             37 (_run_pipeline_on_bundles + NULL)

 454            LOAD_FAST_BORROW_LOAD_FAST_BORROW 84 (bundles, bid)

 455            LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (actor_type, actor_id)

 453            LOAD_CONST               8 (('brokerage_id', 'actor_type', 'actor_id'))
                CALL_KW                  4
                RETURN_VALUE

 458    L6:     LOAD_GLOBAL              7 (_empty_report + NULL)

 459            LOAD_FAST_BORROW         4 (bid)

 460            LOAD_CONST               2 ('failed')

 461            LOAD_CONST              14 ('replay_or_events_bad_shape')
                BUILD_LIST               1

 458            LOAD_CONST               4 (('status', 'warnings'))
                CALL_KW                  3
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 423            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       59 (to L11)
                NOT_TAKEN
                STORE_FAST               8 (e)

 424    L8:     LOAD_GLOBAL             16 (logger)
                LOAD_ATTR               19 (warning + NULL|self)

 425            LOAD_CONST               6 ('candidate_pipeline replay-pattern exception brokerage=')

 426            LOAD_FAST                4 (bid)
                FORMAT_SIMPLE
                LOAD_CONST               7 (' type=')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE

 425            BUILD_STRING             4

 424            CALL                     1
                POP_TOP

 428            BUILD_LIST               0
                STORE_FAST               7 (patterns)
        L9:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                JUMP_BACKWARD_NO_INTERRUPT 201 (to L4)

  --   L10:     LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 423   L11:     RERAISE                  0

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L7 [0]
  L7 to L8 -> L12 [1] lasti
  L8 to L9 -> L10 [1] lasti
  L10 to L12 -> L12 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app\services\memory\candidate_pipeline.py", line 469>:
469           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('events')
              LOAD_CONST               2 ('List[Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _terminal_outcome_from_events at 0x0000018C17F0C960, file "app\services\memory\candidate_pipeline.py", line 469>:
469           RESUME                   0

470           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (events)
              LOAD_GLOBAL              2 (list)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

471           LOAD_CONST               0 (None)
              RETURN_VALUE

472   L1:     LOAD_CONST               0 (None)
              STORE_FAST               1 (last)

473           LOAD_FAST_BORROW         0 (events)
              GET_ITER
      L2:     FOR_ITER               156 (to L9)
              STORE_FAST               2 (ev)

474           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (ev)
              LOAD_GLOBAL              4 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

475           JUMP_BACKWARD           27 (to L2)

476   L3:     LOAD_FAST_BORROW         2 (ev)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               1 ('event_type')
              CALL                     1
              LOAD_CONST               7 (('call.ended', 'call.ended_with_callback', 'call.failed'))
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD           51 (to L2)

479   L4:     LOAD_FAST_BORROW         2 (ev)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               3 ('outcome_state')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE        43 (to L6)
              NOT_TAKEN
              POP_TOP
              LOAD_FAST_BORROW         2 (ev)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               4 ('payload')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L5:     LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               5 ('outcome')
              CALL                     1
      L6:     STORE_FAST               3 (oc)

480           LOAD_FAST_BORROW         3 (oc)
              TO_BOOL
              POP_JUMP_IF_FALSE        5 (to L7)
              NOT_TAKEN

481           LOAD_FAST                3 (oc)
              STORE_FAST               1 (last)
              JUMP_BACKWARD          130 (to L2)

482   L7:     LOAD_FAST_BORROW         2 (ev)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               1 ('event_type')
              CALL                     1
              LOAD_CONST               2 ('call.failed')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_TRUE         3 (to L8)
              NOT_TAKEN
              JUMP_BACKWARD          154 (to L2)

483   L8:     LOAD_CONST               6 ('failed')
              STORE_FAST               1 (last)
              JUMP_BACKWARD          158 (to L2)

473   L9:     END_FOR
              POP_ITER

484           LOAD_FAST_BORROW         1 (last)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "app\services\memory\candidate_pipeline.py", line 487>:
487           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('bundles')

488           LOAD_CONST               2 ('List[Dict[str, Any]]')

487           LOAD_CONST               3 ('brokerage_id')

490           LOAD_CONST               4 ('str')

487           LOAD_CONST               5 ('actor_type')

491           LOAD_CONST               4 ('str')

487           LOAD_CONST               6 ('actor_id')

492           LOAD_CONST               7 ('Optional[str]')

487           LOAD_CONST               8 ('return')

493           LOAD_CONST               9 ('List[Optional[MemoryRecord]]')

487           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _records_from_bundles at 0x0000018C1802C9B0, file "app\services\memory\candidate_pipeline.py", line 487>:
487           RESUME                   0

494           BUILD_LIST               0
              STORE_FAST               4 (out)

495           LOAD_FAST_BORROW         0 (bundles)
              GET_ITER
      L1:     FOR_ITER                33 (to L2)
              STORE_FAST               5 (b)

496           LOAD_GLOBAL              1 (_candidate_from_bundle + NULL)

497           LOAD_FAST_BORROW_LOAD_FAST_BORROW 81 (b, brokerage_id)

498           LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (actor_type, actor_id)

496           LOAD_CONST               0 (('brokerage_id', 'actor_type', 'actor_id'))
              CALL_KW                  4
              STORE_FAST               6 (rec)

500           LOAD_FAST_BORROW         4 (out)
              LOAD_ATTR                3 (append + NULL|self)
              LOAD_FAST_BORROW         6 (rec)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           35 (to L1)

495   L2:     END_FOR
              POP_ITER

501           LOAD_FAST_BORROW         4 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app\services\memory\candidate_pipeline.py", line 504>:
504           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('patterns')

505           LOAD_CONST               2 ('List[MemoryRecord]')

504           LOAD_CONST               3 ('actor_type')

507           LOAD_CONST               4 ('str')

504           LOAD_CONST               5 ('actor_id')

508           LOAD_CONST               6 ('Optional[str]')

504           LOAD_CONST               7 ('return')

509           LOAD_CONST               8 ('List[Optional[MemoryRecord]]')

504           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _patterns_to_candidates at 0x0000018C17F78460, file "app\services\memory\candidate_pipeline.py", line 504>:
504            RESUME                   0

513            BUILD_LIST               0
               STORE_FAST               3 (out)

514            LOAD_FAST                0 (patterns)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L1:     GET_ITER
       L2:     EXTENDED_ARG             1
               FOR_ITER               385 (to L11)
               STORE_FAST               4 (rec)

515            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         4 (rec)
               LOAD_GLOBAL              2 (MemoryRecord)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        20 (to L3)
               NOT_TAKEN

516            LOAD_FAST_BORROW         3 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               1 (None)
               CALL                     1
               POP_TOP

517            JUMP_BACKWARD           45 (to L2)

518    L3:     LOAD_FAST_BORROW         4 (rec)
               LOAD_ATTR                6 (kind)
               LOAD_GLOBAL              8 (MemoryKind)
               LOAD_ATTR               10 (DANGEROUS)
               LOAD_GLOBAL              8 (MemoryKind)
               LOAD_ATTR               12 (EPHEMERAL)
               BUILD_TUPLE              2
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       20 (to L4)
               NOT_TAKEN

519            LOAD_FAST_BORROW         3 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               1 (None)
               CALL                     1
               POP_TOP

520            JUMP_BACKWARD          111 (to L2)

521    L4:     LOAD_GLOBAL             15 (_sanitize_evidence + NULL)
               LOAD_FAST_BORROW         4 (rec)
               LOAD_ATTR               16 (evidence)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
       L5:     CALL                     1
               STORE_FAST               5 (safe_evidence)

522            LOAD_GLOBAL             19 (dict + NULL)
               LOAD_FAST_BORROW         4 (rec)
               LOAD_ATTR               20 (lineage)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
       L6:     CALL                     1
               STORE_FAST               6 (lineage)

523            LOAD_FAST                6 (lineage)
               LOAD_ATTR               23 (setdefault + NULL|self)
               LOAD_CONST               2 ('actor_type')
               LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (actor_type)
               LOAD_GLOBAL             24 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_FAST                1 (actor_type)
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               3 ('SYSTEM')
       L8:     CALL                     2
               POP_TOP

524            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (actor_id)
               LOAD_GLOBAL             24 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       55 (to L9)
               NOT_TAKEN
               LOAD_FAST_BORROW         2 (actor_id)
               LOAD_ATTR               27 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_FALSE       33 (to L9)
               NOT_TAKEN

525            LOAD_FAST_BORROW         6 (lineage)
               LOAD_ATTR               23 (setdefault + NULL|self)
               LOAD_CONST               4 ('actor_id')
               LOAD_FAST_BORROW         2 (actor_id)
               LOAD_ATTR               27 (strip + NULL|self)
               CALL                     0
               CALL                     2
               POP_TOP

526    L9:     LOAD_GLOBAL             28 (dataclasses)
               LOAD_ATTR               30 (replace)
               PUSH_NULL

527            LOAD_FAST_BORROW         4 (rec)

528            LOAD_GLOBAL             32 (MemoryStatus)
               LOAD_ATTR               34 (CANDIDATE)

529            LOAD_FAST_BORROW         5 (safe_evidence)

530            LOAD_FAST_BORROW         6 (lineage)

526            LOAD_CONST               5 (('status', 'evidence', 'lineage'))
               CALL_KW                  4
               STORE_FAST               7 (candidate)

532            LOAD_GLOBAL             37 (has_forbidden_transcript_field + NULL)
               LOAD_FAST_BORROW         7 (candidate)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       21 (to L10)
               NOT_TAKEN

533            LOAD_FAST_BORROW         3 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               1 (None)
               CALL                     1
               POP_TOP

534            EXTENDED_ARG             1
               JUMP_BACKWARD          368 (to L2)

535   L10:     LOAD_FAST_BORROW         3 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_FAST_BORROW         7 (candidate)
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          388 (to L2)

514   L11:     END_FOR
               POP_ITER

536            LOAD_FAST_BORROW         3 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app\services\memory\candidate_pipeline.py", line 539>:
539           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('bundles')

540           LOAD_CONST               2 ('List[Dict[str, Any]]')

539           LOAD_CONST               3 ('brokerage_id')

542           LOAD_CONST               4 ('str')

539           LOAD_CONST               5 ('actor_type')

543           LOAD_CONST               4 ('str')

539           LOAD_CONST               6 ('actor_id')

544           LOAD_CONST               7 ('Optional[str]')

539           LOAD_CONST               8 ('return')

545           LOAD_CONST               9 ('Dict[str, Any]')

539           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _run_pipeline_on_bundles at 0x0000018C18090030, file "app\services\memory\candidate_pipeline.py", line 539>:
539           RESUME                   0

546           LOAD_GLOBAL              1 (_records_from_bundles + NULL)

547           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (bundles, brokerage_id)

548           LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (actor_type, actor_id)

546           LOAD_CONST               0 (('brokerage_id', 'actor_type', 'actor_id'))
              CALL_KW                  4
              STORE_FAST               4 (records)

550           LOAD_GLOBAL              3 (_run_pipeline_on_records + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 65 (records, brokerage_id)
              LOAD_CONST               1 (('brokerage_id',))
              CALL_KW                  2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "app\services\memory\candidate_pipeline.py", line 553>:
553           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('records')

554           LOAD_CONST               2 ('List[Optional[MemoryRecord]]')

553           LOAD_CONST               3 ('brokerage_id')

556           LOAD_CONST               4 ('str')

553           LOAD_CONST               5 ('return')

557           LOAD_CONST               6 ('Dict[str, Any]')

553           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _run_pipeline_on_records at 0x0000018C17F731A0, file "app\services\memory\candidate_pipeline.py", line 553>:
553            RESUME                   0

558            BUILD_LIST               0
               STORE_FAST               2 (results)

559            BUILD_LIST               0
               STORE_FAST               3 (warnings)

560            LOAD_SMALL_INT           0
               STORE_FAST               4 (created)

561            LOAD_SMALL_INT           0
               STORE_FAST               5 (failed)

562            LOAD_CONST               1 (False)
               STORE_FAST               6 (missing_storage)

564            LOAD_FAST_BORROW         0 (records)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               323 (to L14)
               STORE_FAST               7 (rec)

565            LOAD_FAST_BORROW         7 (rec)
               POP_JUMP_IF_NOT_NONE     3 (to L2)
               NOT_TAKEN

566            JUMP_BACKWARD           10 (to L1)

567    L2:     LOAD_GLOBAL              1 (_persist + NULL)
               LOAD_FAST_BORROW         7 (rec)
               CALL                     1
               STORE_FAST               8 (env)

568            LOAD_FAST                2 (results)
               LOAD_ATTR                3 (append + NULL|self)

569            LOAD_CONST               2 ('memory_id')
               LOAD_FAST_BORROW         8 (env)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               2 ('memory_id')
               CALL                     1

570            LOAD_CONST               3 ('status')
               LOAD_FAST_BORROW         8 (env)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               3 ('status')
               CALL                     1

571            LOAD_CONST               4 ('kind')
               LOAD_GLOBAL              7 (isinstance + NULL)
               LOAD_FAST_BORROW         7 (rec)
               LOAD_ATTR                8 (kind)
               LOAD_GLOBAL             10 (MemoryKind)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L3)
               NOT_TAKEN
               LOAD_FAST_BORROW         7 (rec)
               LOAD_ATTR                8 (kind)
               LOAD_ATTR               12 (value)
               JUMP_FORWARD            20 (to L4)
       L3:     LOAD_GLOBAL             15 (str + NULL)
               LOAD_FAST_BORROW         7 (rec)
               LOAD_ATTR                8 (kind)
               CALL                     1

568    L4:     BUILD_MAP                3
               CALL                     1
               POP_TOP

573            LOAD_FAST_BORROW         8 (env)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               3 ('status')
               CALL                     1
               LOAD_CONST               5 ('ok')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L5)
               NOT_TAKEN

574            LOAD_FAST_BORROW         4 (created)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               4 (created)
               JUMP_BACKWARD          180 (to L1)

575    L5:     LOAD_FAST_BORROW         8 (env)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               3 ('status')
               CALL                     1
               LOAD_CONST               6 ('skipped')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       63 (to L10)
               NOT_TAKEN

576            LOAD_FAST_BORROW         8 (env)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               7 ('warnings')
               BUILD_LIST               0
               CALL                     2
               GET_ITER
       L6:     FOR_ITER                37 (to L9)
               STORE_FAST               9 (w)

577            LOAD_FAST_BORROW         9 (w)
               LOAD_CONST               8 ('missing_storage_helper')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN

578            LOAD_CONST               9 (True)
               STORE_FAST               6 (missing_storage)

579    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 147 (w, warnings)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           20 (to L6)

580    L8:     LOAD_FAST_BORROW         3 (warnings)
               LOAD_ATTR                3 (append + NULL|self)
               LOAD_FAST_BORROW         9 (w)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           39 (to L6)

576    L9:     END_FOR
               POP_ITER
               EXTENDED_ARG             1
               JUMP_BACKWARD          264 (to L1)

582   L10:     LOAD_FAST_BORROW         5 (failed)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (failed)

583            LOAD_FAST_BORROW         8 (env)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               7 ('warnings')
               BUILD_LIST               0
               CALL                     2
               GET_ITER
      L11:     FOR_ITER                28 (to L13)
               STORE_FAST               9 (w)

584            LOAD_FAST_BORROW_LOAD_FAST_BORROW 147 (w, warnings)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_TRUE         3 (to L12)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L11)

585   L12:     LOAD_FAST_BORROW         3 (warnings)
               LOAD_ATTR                3 (append + NULL|self)
               LOAD_FAST_BORROW         9 (w)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L11)

583   L13:     END_FOR
               POP_ITER
               EXTENDED_ARG             1
               JUMP_BACKWARD          326 (to L1)

564   L14:     END_FOR
               POP_ITER

587            LOAD_FAST_BORROW         6 (missing_storage)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L16)
               NOT_TAKEN
               LOAD_FAST_BORROW         4 (created)
               LOAD_SMALL_INT           0
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       36 (to L16)
               NOT_TAKEN
               LOAD_FAST_BORROW         5 (failed)
               LOAD_SMALL_INT           0
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       29 (to L16)
               NOT_TAKEN

588            LOAD_GLOBAL             17 (_empty_report + NULL)

589            LOAD_FAST                1 (brokerage_id)

590            LOAD_CONST               6 ('skipped')

591            LOAD_SMALL_INT           0

592            LOAD_SMALL_INT           0

593            LOAD_FAST                3 (warnings)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L15)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               8 ('missing_storage_helper')
               BUILD_LIST               1

594   L15:     LOAD_FAST_BORROW         2 (results)

588            LOAD_CONST              10 (('status', 'candidates_created', 'failed', 'warnings', 'results'))
               CALL_KW                  6
               RETURN_VALUE

597   L16:     LOAD_FAST_BORROW         2 (results)
               TO_BOOL
               POP_JUMP_IF_TRUE        16 (to L17)
               NOT_TAKEN

598            LOAD_GLOBAL             17 (_empty_report + NULL)

599            LOAD_FAST_BORROW         1 (brokerage_id)

600            LOAD_CONST               5 ('ok')

601            LOAD_FAST_BORROW         3 (warnings)

602            BUILD_LIST               0

598            LOAD_CONST              11 (('status', 'warnings', 'results'))
               CALL_KW                  4
               RETURN_VALUE

605   L17:     LOAD_CONST               5 ('ok')
               STORE_FAST              10 (overall)

606            LOAD_FAST_BORROW         5 (failed)
               TO_BOOL
               POP_JUMP_IF_FALSE       10 (to L18)
               NOT_TAKEN
               LOAD_FAST_BORROW         4 (created)
               LOAD_SMALL_INT           0
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        3 (to L18)
               NOT_TAKEN

607            LOAD_CONST              12 ('failed')
               STORE_FAST              10 (overall)

608   L18:     LOAD_GLOBAL             17 (_empty_report + NULL)

609            LOAD_FAST_BORROW         1 (brokerage_id)

610            LOAD_FAST_BORROW        10 (overall)

611            LOAD_FAST_BORROW         4 (created)

612            LOAD_FAST_BORROW         5 (failed)

613            LOAD_FAST_BORROW         3 (warnings)

614            LOAD_FAST_BORROW         2 (results)

608            LOAD_CONST              10 (('status', 'candidates_created', 'failed', 'warnings', 'results'))
               CALL_KW                  6
               RETURN_VALUE
```
