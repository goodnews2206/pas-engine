# memory/classifier

- **pyc:** `app\services\memory\__pycache__\classifier.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/classifier.py`
- **co_filename (from bytecode):** `app\services\memory\classifier.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144A — Deterministic memory classifiers.

Pure functions that turn observed events / replay reconstructions /
optimization recommendations into well-formed `MemoryRecord`
candidates. No I/O, no LLM, no embeddings, no learning.

Classifiers ENFORCE three rules at the source:

  1. Tenant isolation — `brokerage_id` is required; absent ⇒ no record.
  2. No raw transcripts — even when input carries `turns[].text`, the
     emitted MemoryRecord stores summaries/counts/categories only.
  3. Adversarial input → DANGEROUS — any prompt-injection-shaped phrase
     in the input collapses the candidate to MemoryKind.DANGEROUS with
     status QUARANTINED, regardless of how positive the surrounding
     outcome looks.

Public surface:
  - classify_memory_candidate(event_or_reconstruction)        -> Optional[MemoryRecord]
  - classify_replay_pattern(reconstruction)                   -> list[MemoryRecord]
  - classify_optimization_recommendation(rec, brokerage_id)   -> Optional[MemoryRecord]
```

## Imports

`Any`, `CANDIDATE_CONFIDENCE_THRESHOLD`, `Dict`, `Iterable`, `List`, `MemoryKind`, `MemoryRecord`, `MemorySource`, `MemoryStatus`, `Optional`, `__future__`, `annotations`, `contracts`, `new_memory_id`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_candidate_from_event`, `_candidate_from_reconstruction`, `_extract_text_signals`, `_looks_like_prompt_injection`, `_make_dangerous_record`, `classify_memory_candidate`, `classify_optimization_recommendation`, `classify_replay_pattern`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS144A — Deterministic memory classifiers.\n\nPure functions that turn observed events / replay reconstructions /\noptimization recommendations into well-formed `MemoryRecord`\ncandidates. No I/O, no LLM, no embeddings, no learning.\n\nClassifiers ENFORCE three rules at the source:\n\n  1. Tenant isolation — `brokerage_id` is required; absent ⇒ no record.\n  2. No raw transcripts — even when input carries `turns[].text`, the\n     emitted MemoryRecord stores summaries/counts/categories only.\n  3. Adversarial input → DANGEROUS — any prompt-injection-shaped phrase\n     in the input collapses the candidate to MemoryKind.DANGEROUS with\n     status QUARANTINED, regardless of how positive the surrounding\n     outcome looks.\n\nPublic surface:\n  - classify_memory_candidate(event_or_reconstruction)        -> Optional[MemoryRecord]\n  - classify_replay_pattern(reconstruction)                   -> list[MemoryRecord]\n  - classify_optimization_recommendation(rec, brokerage_id)   -> Optional[MemoryRecord]\n'
- 'booked'
- 'callback'
- 'callback_scheduled'
- 'transferred'
- 'not_booked'
- 'no_outcome'
- 'Dict[str, float]'
- '_OUTCOME_WEIGHTS'
- 'high'
- 'medium'
- 'low'
- '_RECOMMENDATION_CONFIDENCE'
- '_RECOMMENDATION_PRIORITY_WEIGHT'
- 'lineage'
- 'metadata'
- 'texts'
- 'Iterable[Any]'
- 'return'
- 'bool'
- 'True iff any string in *texts* contains a known injection\npattern. Non-string inputs are skipped silently.'
- 'payload'
- 'dict'
- 'List[str]'
- 'Pull the *small set* of string fields the classifier scans for\nadversarial patterns. The classifier inspects these but never\ncopies them verbatim into the resulting MemoryRecord.'
- 'extracted_fields'
- 'turns'
- 'brokerage_id'
- 'str'
- 'source'
- 'MemorySource'
- 'reason'
- 'Optional[Dict[str, Any]]'
- 'MemoryRecord'
- 'All adversarial paths funnel through here so the dangerous\nrecord shape is identical regardless of where it was detected.\nNever echoes the offending input text back into evidence.'
- 'Suspicious input quarantined'
- 'Input matched a prompt-injection-shaped pattern; memory candidate quarantined for operator review.'
- 'signal'
- 'matched_injection_pattern'
- 'source_kind'
- 'adversarial_detector'
- 'event_or_reconstruction'
- 'Optional[MemoryRecord]'
- 'Decide whether an arbitrary event or reconstruction dict should\nbecome a memory candidate.\n\nReturns:\n  - MemoryRecord (DANGEROUS / QUARANTINED) on adversarial input\n  - MemoryRecord (OPERATIONAL / CANDIDATE) on a positive outcome\n  - low-confidence MemoryRecord (EPHEMERAL) on a non-replayable\n    but non-empty input\n  - None when no useful signal is present\n'
- 'prompt_injection_phrase'
- 'call_id'
- 'memory_candidate'
- 'final_outcome'
- 'missing_lifecycle_steps'
- 'reconstruction'
- 'List[MemoryRecord]'
- 'Mine a reconstructed call for every memory pattern it implies.\n\nEmits at most:\n  - one DANGEROUS record (shorts everything else if injection found)\n  - one OPERATIONAL outcome-pattern record (if outcome is positive)\n  - one OPERATIONAL lifecycle-gap record (if steps were missed and\n    the outcome was not booked)\n'
- 'prompt_injection_in_reconstruction'
- 'replay_reconstruction'
- 'is_replayable'
- 'Successful pattern: '
- 'Reconstructed call closed with outcome='
- 'events_count'
- ' events, '
- ' missing lifecycle steps.'
- 'outcome'
- 'extracted_field_names'
- 'replay_pattern_outcome'
- 'Lifecycle gap detected'
- 'Reconstruction missed '
- ' lifecycle step(s); outcome='
- 'unknown'
- 'missing'
- 'replay_pattern_gap'
- 'recommendation'
- 'Promote a high-confidence optimization recommendation into an\nOPTIMIZATION-kind memory candidate.\n\nDrops the recommendation (returns None) when:\n  - input shape is not a dict\n  - brokerage_id is missing\n  - audience is not actionable (broker / operator)\n  - confidence falls below the candidate threshold\n'
- 'title'
- 'insight'
- 'recommended_action'
- 'prompt_injection_in_recommendation'
- 'recommendation_id'
- 'optimization_recommendation'
- 'audience'
- 'confidence'
- 'priority'
- 'Optimization recommendation'
- 'expected_impact'
- 'affected_personality'
- 'affected_strategy'
- 'rec'
- 'Outcome learned: '
- 'Reconstruction observed'
- 'Reconstruction closed with outcome='
- ' missing step(s).'
- 'memory_candidate_reconstruction'
- 'event'
- 'event_type'
- 'Event observed: '
- 'Single event '
- ' captured.'
- 'actor'
- 'workflow_stage'
- 'event_id'
- 'memory_candidate_event'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS144A — Deterministic memory classifiers.\n\nPure functions that turn observed events / replay reconstructions /\noptimization recommendations into well-formed `MemoryRecord`\ncandidates. No I/O, no LLM, no embeddings, no learning.\n\nClassifiers ENFORCE three rules at the source:\n\n  1. Tenant isolation — `brokerage_id` is required; absent ⇒ no record.\n  2. No raw transcripts — even when input carries `turns[].text`, the\n     emitted MemoryRecord stores summaries/counts/categories only.\n  3. Adversarial input → DANGEROUS — any prompt-injection-shaped phrase\n     in the input collapses the candidate to MemoryKind.DANGEROUS with\n     status QUARANTINED, regardless of how positive the surrounding\n     outcome looks.\n\nPublic surface:\n  - classify_memory_candidate(event_or_reconstruction)        -> Optional[MemoryRecord]\n  - classify_replay_pattern(reconstruction)                   -> list[MemoryRecord]\n  - classify_optimization_recommendation(rec, brokerage_id)   -> Optional[MemoryRecord]\n')
               STORE_NAME               1 (__doc__)

  24           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  26           LOAD_SMALL_INT           0
               LOAD_CONST               2 (('Any', 'Dict', 'Iterable', 'List', 'Optional'))
               IMPORT_NAME              4 (typing)
               IMPORT_FROM              5 (Any)
               STORE_NAME               5 (Any)
               IMPORT_FROM              6 (Dict)
               STORE_NAME               6 (Dict)
               IMPORT_FROM              7 (Iterable)
               STORE_NAME               7 (Iterable)
               IMPORT_FROM              8 (List)
               STORE_NAME               8 (List)
               IMPORT_FROM              9 (Optional)
               STORE_NAME               9 (Optional)
               POP_TOP

  28           LOAD_SMALL_INT           1
               LOAD_CONST               3 (('CANDIDATE_CONFIDENCE_THRESHOLD', 'MemoryKind', 'MemoryRecord', 'MemorySource', 'MemoryStatus', 'new_memory_id'))
               IMPORT_NAME             10 (contracts)
               IMPORT_FROM             11 (CANDIDATE_CONFIDENCE_THRESHOLD)
               STORE_NAME              11 (CANDIDATE_CONFIDENCE_THRESHOLD)
               IMPORT_FROM             12 (MemoryKind)
               STORE_NAME              12 (MemoryKind)
               IMPORT_FROM             13 (MemoryRecord)
               STORE_NAME              13 (MemoryRecord)
               IMPORT_FROM             14 (MemorySource)
               STORE_NAME              14 (MemorySource)
               IMPORT_FROM             15 (MemoryStatus)
               STORE_NAME              15 (MemoryStatus)
               IMPORT_FROM             16 (new_memory_id)
               STORE_NAME              16 (new_memory_id)
               POP_TOP

  46           LOAD_CONST              44 (('ignore previous instructions', 'ignore all previous', 'ignore the above', 'disregard previous', 'disregard the above', 'forget previous instructions', 'forget all previous', 'you are now', 'act as ', 'pretend to be', 'roleplay as', 'from now on you', 'system prompt', 'developer mode', 'jailbreak', 'reveal your instructions', 'your real instructions', 'your original instructions', 'show me the system'))
               STORE_NAME              17 (_PROMPT_INJECTION_PATTERNS)

  69           LOAD_NAME               18 (frozenset)
               PUSH_NULL
               BUILD_SET                0
               LOAD_CONST              45 (frozenset({'booked', 'callback_scheduled', 'callback'}))
               SET_UPDATE               1
               CALL                     1
               STORE_NAME              19 (_POSITIVE_OUTCOMES)

  73           LOAD_CONST               4 ('booked')
               LOAD_CONST               7 (0.85)

  74           LOAD_CONST               5 ('callback')
               LOAD_CONST               8 (0.65)

  75           LOAD_CONST               6 ('callback_scheduled')
               LOAD_CONST               8 (0.65)

  76           LOAD_CONST               9 ('transferred')
               LOAD_CONST              10 (0.5)

  77           LOAD_CONST              11 ('not_booked')
               LOAD_CONST              12 (0.35)

  78           LOAD_CONST              13 ('no_outcome')
               LOAD_CONST              14 (0.2)

  72           BUILD_MAP                6
               STORE_NAME              20 (_OUTCOME_WEIGHTS)
               LOAD_CONST              15 ('Dict[str, float]')
               LOAD_NAME               21 (__annotations__)
               LOAD_CONST              16 ('_OUTCOME_WEIGHTS')
               STORE_SUBSCR

  84           LOAD_CONST              17 ('high')
               LOAD_CONST               7 (0.85)

  85           LOAD_CONST              18 ('medium')
               LOAD_CONST               8 (0.65)

  86           LOAD_CONST              19 ('low')
               LOAD_CONST              20 (0.4)

  83           BUILD_MAP                3
               STORE_NAME              22 (_RECOMMENDATION_CONFIDENCE)
               LOAD_CONST              15 ('Dict[str, float]')
               LOAD_NAME               21 (__annotations__)
               LOAD_CONST              21 ('_RECOMMENDATION_CONFIDENCE')
               STORE_SUBSCR

  92           LOAD_CONST              17 ('high')
               LOAD_CONST              22 (0.75)

  93           LOAD_CONST              18 ('medium')
               LOAD_CONST              23 (0.6)

  94           LOAD_CONST              19 ('low')
               LOAD_CONST              10 (0.5)

  91           BUILD_MAP                3
               STORE_NAME              23 (_RECOMMENDATION_PRIORITY_WEIGHT)
               LOAD_CONST              15 ('Dict[str, float]')
               LOAD_NAME               21 (__annotations__)
               LOAD_CONST              24 ('_RECOMMENDATION_PRIORITY_WEIGHT')
               STORE_SUBSCR

  98           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\classifier.py", line 98>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object _looks_like_prompt_injection at 0x0000018C17FF0DB0, file "app\services\memory\classifier.py", line 98>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              24 (_looks_like_prompt_injection)

 111           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA2E20, file "app\services\memory\classifier.py", line 111>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object _extract_text_signals at 0x0000018C17ED8100, file "app\services\memory\classifier.py", line 111>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              25 (_extract_text_signals)

 146           LOAD_CONST              29 ('lineage')

 151           LOAD_CONST              30 (None)

 146           LOAD_CONST              31 ('metadata')

 152           LOAD_CONST              30 (None)

 146           BUILD_MAP                2
               LOAD_CONST              32 (<code object __annotate__ at 0x0000018C18024D30, file "app\services\memory\classifier.py", line 146>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object _make_dangerous_record at 0x0000018C1804C9F0, file "app\services\memory\classifier.py", line 146>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              26 (_make_dangerous_record)

 180           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\classifier.py", line 180>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object classify_memory_candidate at 0x0000018C17D8E300, file "app\services\memory\classifier.py", line 180>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              27 (classify_memory_candidate)

 221           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA3B40, file "app\services\memory\classifier.py", line 221>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object classify_replay_pattern at 0x0000018C17EDA610, file "app\services\memory\classifier.py", line 221>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (classify_replay_pattern)

 316           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C18025830, file "app\services\memory\classifier.py", line 316>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object classify_optimization_recommendation at 0x0000018C17F75630, file "app\services\memory\classifier.py", line 316>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              29 (classify_optimization_recommendation)

 395           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C18025930, file "app\services\memory\classifier.py", line 395>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object _candidate_from_reconstruction at 0x0000018C17F7B110, file "app\services\memory\classifier.py", line 395>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              30 (_candidate_from_reconstruction)

 442           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\memory\classifier.py", line 442>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object _candidate_from_event at 0x0000018C17D8C5C0, file "app\services\memory\classifier.py", line 442>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_candidate_from_event)
               LOAD_CONST              30 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\classifier.py", line 98>:
 98           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('texts')
              LOAD_CONST               2 ('Iterable[Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _looks_like_prompt_injection at 0x0000018C17FF0DB0, file "app\services\memory\classifier.py", line 98>:
 98           RESUME                   0

101           LOAD_FAST_BORROW         0 (texts)
              GET_ITER
      L1:     FOR_ITER                74 (to L7)
              STORE_FAST               1 (raw)

102           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (raw)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        9 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (raw)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

103   L2:     JUMP_BACKWARD           35 (to L1)

104   L3:     LOAD_FAST_BORROW         1 (raw)
              LOAD_ATTR                5 (lower + NULL|self)
              CALL                     0
              STORE_FAST               2 (lower)

105           LOAD_GLOBAL              6 (_PROMPT_INJECTION_PATTERNS)
              GET_ITER
      L4:     FOR_ITER                13 (to L6)
              STORE_FAST               3 (pat)

106           LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (pat, lower)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L4)

107   L5:     POP_TOP
              POP_TOP
              LOAD_CONST               1 (True)
              RETURN_VALUE

105   L6:     END_FOR
              POP_ITER
              JUMP_BACKWARD           76 (to L1)

101   L7:     END_FOR
              POP_ITER

108           LOAD_CONST               2 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app\services\memory\classifier.py", line 111>:
111           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('payload')
              LOAD_CONST               2 ('dict')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _extract_text_signals at 0x0000018C17ED8100, file "app\services\memory\classifier.py", line 111>:
111            RESUME                   0

115            BUILD_LIST               0
               STORE_FAST               1 (signals)

117            LOAD_CONST               4 (('title', 'summary', 'intent', 'extracted_value', 'evidence_text', 'recommended_action', 'insight', 'input_text', 'output_text'))
               GET_ITER
       L1:     FOR_ITER                61 (to L3)
               STORE_FAST               2 (key)

120            LOAD_FAST_BORROW         0 (payload)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_FAST_BORROW         2 (key)
               CALL                     1
               STORE_FAST               3 (v)

121            LOAD_GLOBAL              3 (isinstance + NULL)
               LOAD_FAST_BORROW         3 (v)
               LOAD_GLOBAL              4 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               JUMP_BACKWARD           44 (to L1)

122    L2:     LOAD_FAST_BORROW         1 (signals)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         3 (v)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           63 (to L1)

117    L3:     END_FOR
               POP_ITER

124            LOAD_FAST_BORROW         0 (payload)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               1 ('extracted_fields')
               CALL                     1
               STORE_FAST               4 (extracted)

125            LOAD_GLOBAL              3 (isinstance + NULL)
               LOAD_FAST_BORROW         4 (extracted)
               LOAD_GLOBAL              8 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       65 (to L7)
               NOT_TAKEN

126            LOAD_FAST_BORROW         4 (extracted)
               LOAD_ATTR               11 (values + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER                44 (to L6)
               STORE_FAST               3 (v)

127            LOAD_GLOBAL              3 (isinstance + NULL)
               LOAD_FAST_BORROW         3 (v)
               LOAD_GLOBAL              4 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           27 (to L4)

128    L5:     LOAD_FAST_BORROW         1 (signals)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         3 (v)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           46 (to L4)

126    L6:     END_FOR
               POP_ITER

133    L7:     LOAD_FAST_BORROW         0 (payload)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               2 ('turns')
               CALL                     1
               STORE_FAST               5 (turns)

134            LOAD_GLOBAL              3 (isinstance + NULL)
               LOAD_FAST_BORROW         5 (turns)
               LOAD_GLOBAL             12 (list)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE      108 (to L14)
               NOT_TAKEN

135            LOAD_FAST_BORROW         5 (turns)
               LOAD_CONST               3 (slice(None, 8, None))
               BINARY_OP               26 ([])
               GET_ITER
       L8:     FOR_ITER                94 (to L13)
               STORE_FAST               6 (t)

136            LOAD_GLOBAL              3 (isinstance + NULL)
               LOAD_FAST_BORROW         6 (t)
               LOAD_GLOBAL              8 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN

137            JUMP_BACKWARD           27 (to L8)

138    L9:     LOAD_CONST               5 (('text', 'input_text', 'output_text', 'utterance'))
               GET_ITER
      L10:     FOR_ITER                61 (to L12)
               STORE_FAST               7 (k)

139            LOAD_FAST_BORROW         6 (t)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_FAST_BORROW         7 (k)
               CALL                     1
               STORE_FAST               3 (v)

140            LOAD_GLOBAL              3 (isinstance + NULL)
               LOAD_FAST_BORROW         3 (v)
               LOAD_GLOBAL              4 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L11)
               NOT_TAKEN
               JUMP_BACKWARD           44 (to L10)

141   L11:     LOAD_FAST_BORROW         1 (signals)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         3 (v)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           63 (to L10)

138   L12:     END_FOR
               POP_ITER
               JUMP_BACKWARD           96 (to L8)

135   L13:     END_FOR
               POP_ITER

143   L14:     LOAD_FAST_BORROW         1 (signals)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024D30, file "app\services\memory\classifier.py", line 146>:
146           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

148           LOAD_CONST               2 ('str')

146           LOAD_CONST               3 ('source')

149           LOAD_CONST               4 ('MemorySource')

146           LOAD_CONST               5 ('reason')

150           LOAD_CONST               2 ('str')

146           LOAD_CONST               6 ('lineage')

151           LOAD_CONST               7 ('Optional[Dict[str, Any]]')

146           LOAD_CONST               8 ('metadata')

152           LOAD_CONST               7 ('Optional[Dict[str, Any]]')

146           LOAD_CONST               9 ('return')

153           LOAD_CONST              10 ('MemoryRecord')

146           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _make_dangerous_record at 0x0000018C1804C9F0, file "app\services\memory\classifier.py", line 146>:
146           RESUME                   0

157           LOAD_GLOBAL              1 (MemoryRecord + NULL)

158           LOAD_GLOBAL              3 (new_memory_id + NULL)
              CALL                     0

159           LOAD_FAST                0 (brokerage_id)

160           LOAD_GLOBAL              4 (MemoryKind)
              LOAD_ATTR                6 (DANGEROUS)

161           LOAD_FAST                1 (source)

162           LOAD_GLOBAL              8 (MemoryStatus)
              LOAD_ATTR               10 (QUARANTINED)

163           LOAD_CONST               1 ('Suspicious input quarantined')

165           LOAD_CONST               2 ('Input matched a prompt-injection-shaped pattern; memory candidate quarantined for operator review.')

168           LOAD_CONST               3 ('reason')
              LOAD_FAST_BORROW         2 (reason)
              LOAD_CONST               4 ('signal')
              LOAD_CONST               5 ('matched_injection_pattern')
              BUILD_MAP                2

169           LOAD_CONST               6 (0.5)

170           LOAD_CONST               7 (0.0)

171           LOAD_GLOBAL             13 (dict + NULL)
              LOAD_FAST                3 (lineage)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         5 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               8 ('source_kind')
              LOAD_CONST               9 ('adversarial_detector')
              BUILD_MAP                1
      L1:     CALL                     1

172           LOAD_GLOBAL             13 (dict + NULL)
              LOAD_FAST                4 (metadata)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L2:     CALL                     1

157           LOAD_CONST              10 (('memory_id', 'brokerage_id', 'kind', 'source', 'status', 'title', 'summary', 'evidence', 'confidence', 'outcome_weight', 'lineage', 'metadata'))
              CALL_KW                 12
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\classifier.py", line 180>:
180           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('event_or_reconstruction')
              LOAD_CONST               2 ('dict')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[MemoryRecord]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object classify_memory_candidate at 0x0000018C17D8E300, file "app\services\memory\classifier.py", line 180>:
180           RESUME                   0

191           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (event_or_reconstruction)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

192           LOAD_CONST               1 (None)
              RETURN_VALUE

194   L1:     LOAD_FAST_BORROW         0 (event_or_reconstruction)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('brokerage_id')
              CALL                     1
              STORE_FAST               1 (brokerage_id)

195           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (brokerage_id)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (brokerage_id)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

196   L2:     LOAD_CONST               1 (None)
              RETURN_VALUE

198   L3:     LOAD_GLOBAL             11 (_looks_like_prompt_injection + NULL)
              LOAD_GLOBAL             13 (_extract_text_signals + NULL)
              LOAD_FAST_BORROW         0 (event_or_reconstruction)
              CALL                     1
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       49 (to L4)
              NOT_TAKEN

199           LOAD_GLOBAL             15 (_make_dangerous_record + NULL)

200           LOAD_FAST_BORROW         1 (brokerage_id)

201           LOAD_GLOBAL             16 (MemorySource)
              LOAD_ATTR               18 (CALL)

202           LOAD_CONST               3 ('prompt_injection_phrase')

204           LOAD_CONST               4 ('call_id')
              LOAD_FAST_BORROW         0 (event_or_reconstruction)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               4 ('call_id')
              CALL                     1

205           LOAD_CONST               5 ('source_kind')
              LOAD_CONST               6 ('memory_candidate')

203           BUILD_MAP                2

199           LOAD_CONST               7 (('brokerage_id', 'source', 'reason', 'lineage'))
              CALL_KW                  4
              RETURN_VALUE

213   L4:     LOAD_CONST               8 ('final_outcome')
              LOAD_FAST_BORROW         0 (event_or_reconstruction)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         8 (to L5)
              NOT_TAKEN

214           LOAD_CONST               9 ('missing_lifecycle_steps')
              LOAD_FAST_BORROW         0 (event_or_reconstruction)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       12 (to L6)
              NOT_TAKEN

216   L5:     LOAD_GLOBAL             21 (_candidate_from_reconstruction + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (event_or_reconstruction, brokerage_id)
              CALL                     2
              RETURN_VALUE

218   L6:     LOAD_GLOBAL             23 (_candidate_from_event + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (event_or_reconstruction, brokerage_id)
              CALL                     2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app\services\memory\classifier.py", line 221>:
221           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('reconstruction')
              LOAD_CONST               2 ('dict')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[MemoryRecord]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object classify_replay_pattern at 0x0000018C17EDA610, file "app\services\memory\classifier.py", line 221>:
221            RESUME                   0

230            BUILD_LIST               0
               STORE_FAST               1 (out)

232            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (reconstruction)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

233            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

235    L1:     LOAD_FAST_BORROW         0 (reconstruction)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               1 ('brokerage_id')
               CALL                     1
               STORE_FAST               2 (brokerage_id)

236            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (brokerage_id)
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L2)
               NOT_TAKEN
               LOAD_FAST_BORROW         2 (brokerage_id)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

237    L2:     LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

239    L3:     LOAD_GLOBAL             11 (_looks_like_prompt_injection + NULL)
               LOAD_GLOBAL             13 (_extract_text_signals + NULL)
               LOAD_FAST_BORROW         0 (reconstruction)
               CALL                     1
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       66 (to L4)
               NOT_TAKEN

240            LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_make_dangerous_record + NULL)

241            LOAD_FAST_BORROW         2 (brokerage_id)

242            LOAD_GLOBAL             18 (MemorySource)
               LOAD_ATTR               20 (REPLAY)

243            LOAD_CONST               2 ('prompt_injection_in_reconstruction')

245            LOAD_CONST               3 ('call_id')
               LOAD_FAST_BORROW         0 (reconstruction)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               3 ('call_id')
               CALL                     1

246            LOAD_CONST               4 ('source_kind')
               LOAD_CONST               5 ('replay_reconstruction')

244            BUILD_MAP                2

240            LOAD_CONST               6 (('brokerage_id', 'source', 'reason', 'lineage'))
               CALL_KW                  4
               CALL                     1
               POP_TOP

249            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

251    L4:     LOAD_FAST_BORROW         0 (reconstruction)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               7 ('final_outcome')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               8 ('')
       L5:     LOAD_ATTR               23 (lower + NULL|self)
               CALL                     0
               STORE_FAST               3 (final)

252            LOAD_FAST_BORROW         0 (reconstruction)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               9 ('is_replayable')
               CALL                     1
               STORE_FAST               4 (is_replayable)

253            LOAD_GLOBAL             25 (list + NULL)
               LOAD_FAST_BORROW         0 (reconstruction)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              10 ('missing_lifecycle_steps')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L6:     CALL                     1
               STORE_FAST               5 (missing)

256            LOAD_FAST_BORROW         4 (is_replayable)
               LOAD_CONST              11 (False)
               IS_OP                    0 (is)
               POP_JUMP_IF_FALSE       14 (to L7)
               NOT_TAKEN
               LOAD_FAST_BORROW         3 (final)
               LOAD_GLOBAL             26 (_POSITIVE_OUTCOMES)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN

257            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

259    L7:     LOAD_FAST_BORROW         3 (final)
               LOAD_GLOBAL             26 (_POSITIVE_OUTCOMES)
               CONTAINS_OP              0 (in)
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      296 (to L11)
               NOT_TAKEN

260            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             29 (MemoryRecord + NULL)

261            LOAD_GLOBAL             31 (new_memory_id + NULL)
               CALL                     0

262            LOAD_FAST                2 (brokerage_id)

263            LOAD_GLOBAL             32 (MemoryKind)
               LOAD_ATTR               34 (OPERATIONAL)

264            LOAD_GLOBAL             18 (MemorySource)
               LOAD_ATTR               20 (REPLAY)

265            LOAD_GLOBAL             36 (MemoryStatus)
               LOAD_ATTR               38 (CANDIDATE)

266            LOAD_CONST              12 ('Successful pattern: ')
               LOAD_FAST_BORROW         3 (final)
               FORMAT_SIMPLE
               BUILD_STRING             2

268            LOAD_CONST              13 ('Reconstructed call closed with outcome=')
               LOAD_FAST                3 (final)
               FORMAT_SIMPLE
               LOAD_CONST              14 ('; ')

269            LOAD_GLOBAL             41 (int + NULL)
               LOAD_FAST_BORROW         0 (reconstruction)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              15 ('events_count')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               POP_TOP
               LOAD_SMALL_INT           0
       L8:     CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              16 (' events, ')

270            LOAD_GLOBAL             43 (len + NULL)
               LOAD_FAST_BORROW         5 (missing)
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              17 (' missing lifecycle steps.')

268            BUILD_STRING             7

273            LOAD_CONST              18 ('outcome')
               LOAD_FAST                3 (final)

274            LOAD_CONST              15 ('events_count')
               LOAD_GLOBAL             41 (int + NULL)
               LOAD_FAST_BORROW         0 (reconstruction)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              15 ('events_count')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               POP_TOP
               LOAD_SMALL_INT           0
       L9:     CALL                     1

275            LOAD_CONST              10 ('missing_lifecycle_steps')
               LOAD_FAST_BORROW         5 (missing)
               LOAD_CONST              19 (slice(None, 10, None))
               BINARY_OP               26 ([])

276            LOAD_CONST              20 ('extracted_field_names')
               LOAD_GLOBAL             45 (sorted + NULL)
               LOAD_GLOBAL             25 (list + NULL)

277            LOAD_FAST_BORROW         0 (reconstruction)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              21 ('extracted_fields')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L10)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
      L10:     LOAD_ATTR               47 (keys + NULL|self)
               CALL                     0

276            CALL                     1
               CALL                     1

278            LOAD_CONST              19 (slice(None, 10, None))

276            BINARY_OP               26 ([])

272            BUILD_MAP                4

280            LOAD_CONST              22 (0.7)

281            LOAD_GLOBAL             48 (_OUTCOME_WEIGHTS)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_FAST_BORROW         3 (final)
               LOAD_CONST              23 (0.6)
               CALL                     2

283            LOAD_CONST               3 ('call_id')
               LOAD_FAST_BORROW         0 (reconstruction)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               3 ('call_id')
               CALL                     1

284            LOAD_CONST               4 ('source_kind')
               LOAD_CONST              24 ('replay_pattern_outcome')

282            BUILD_MAP                2

260            LOAD_CONST              25 (('memory_id', 'brokerage_id', 'kind', 'source', 'status', 'title', 'summary', 'evidence', 'confidence', 'outcome_weight', 'lineage'))
               CALL_KW                 11
               CALL                     1
               POP_TOP

288   L11:     LOAD_FAST_BORROW         5 (missing)
               TO_BOOL
               POP_JUMP_IF_FALSE      197 (to L15)
               NOT_TAKEN
               LOAD_FAST_BORROW         3 (final)
               LOAD_CONST              34 (frozenset({'booked'}))
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE      190 (to L15)
               NOT_TAKEN

289            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             29 (MemoryRecord + NULL)

290            LOAD_GLOBAL             31 (new_memory_id + NULL)
               CALL                     0

291            LOAD_FAST                2 (brokerage_id)

292            LOAD_GLOBAL             32 (MemoryKind)
               LOAD_ATTR               34 (OPERATIONAL)

293            LOAD_GLOBAL             18 (MemorySource)
               LOAD_ATTR               20 (REPLAY)

294            LOAD_GLOBAL             36 (MemoryStatus)
               LOAD_ATTR               38 (CANDIDATE)

295            LOAD_CONST              26 ('Lifecycle gap detected')

297            LOAD_CONST              27 ('Reconstruction missed ')
               LOAD_GLOBAL             43 (len + NULL)
               LOAD_FAST_BORROW         5 (missing)
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              28 (' lifecycle step(s); outcome=')

298            LOAD_FAST                3 (final)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L12)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              29 ('unknown')
      L12:     FORMAT_SIMPLE
               LOAD_CONST              30 ('.')

297            BUILD_STRING             5

301            LOAD_CONST              31 ('missing')
               LOAD_FAST_BORROW         5 (missing)
               LOAD_CONST              19 (slice(None, 10, None))
               BINARY_OP               26 ([])

302            LOAD_CONST              18 ('outcome')
               LOAD_FAST                3 (final)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L13)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              29 ('unknown')

303   L13:     LOAD_CONST              15 ('events_count')
               LOAD_GLOBAL             41 (int + NULL)
               LOAD_FAST_BORROW         0 (reconstruction)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              15 ('events_count')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L14)
               NOT_TAKEN
               POP_TOP
               LOAD_SMALL_INT           0
      L14:     CALL                     1

300            BUILD_MAP                3

305            LOAD_CONST              23 (0.6)

306            LOAD_CONST              32 (0.55)

308            LOAD_CONST               3 ('call_id')
               LOAD_FAST_BORROW         0 (reconstruction)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               3 ('call_id')
               CALL                     1

309            LOAD_CONST               4 ('source_kind')
               LOAD_CONST              33 ('replay_pattern_gap')

307            BUILD_MAP                2

289            LOAD_CONST              25 (('memory_id', 'brokerage_id', 'kind', 'source', 'status', 'title', 'summary', 'evidence', 'confidence', 'outcome_weight', 'lineage'))
               CALL_KW                 11
               CALL                     1
               POP_TOP

313   L15:     LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025830, file "app\services\memory\classifier.py", line 316>:
316           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendation')

317           LOAD_CONST               2 ('dict')

316           LOAD_CONST               3 ('brokerage_id')

317           LOAD_CONST               4 ('str')

316           LOAD_CONST               5 ('return')

318           LOAD_CONST               6 ('Optional[MemoryRecord]')

316           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object classify_optimization_recommendation at 0x0000018C17F75630, file "app\services\memory\classifier.py", line 316>:
 316            RESUME                   0

 328            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (recommendation)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 329            LOAD_CONST               1 (None)
                RETURN_VALUE

 330    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_GLOBAL              4 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN

 331    L2:     LOAD_CONST               1 (None)
                RETURN_VALUE

 334    L3:     LOAD_FAST_BORROW         0 (recommendation)
                LOAD_ATTR                9 (items + NULL|self)
                CALL                     0
                GET_ITER

 333            LOAD_FAST_AND_CLEAR      2 (k)
                LOAD_FAST_AND_CLEAR      3 (v)
                SWAP                     3
        L4:     BUILD_LIST               0
                SWAP                     2

 334    L5:     FOR_ITER                40 (to L10)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   35 (k, v)

 335            LOAD_FAST_BORROW         2 (k)
                LOAD_CONST              22 (('title', 'insight', 'recommended_action'))
                CONTAINS_OP              0 (in)

 334    L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           14 (to L5)

 335    L7:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (v)
                LOAD_GLOBAL              4 (str)
                CALL                     2
                TO_BOOL

 334    L8:     POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           38 (to L5)
        L9:     LOAD_FAST_BORROW         3 (v)
                LIST_APPEND              2
                JUMP_BACKWARD           42 (to L5)
       L10:     END_FOR
                POP_ITER

 333   L11:     STORE_FAST               4 (text_signals)
                STORE_FAST               2 (k)
                STORE_FAST               3 (v)

 337            LOAD_GLOBAL             11 (_looks_like_prompt_injection + NULL)
                LOAD_FAST_BORROW         4 (text_signals)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       49 (to L12)
                NOT_TAKEN

 338            LOAD_GLOBAL             13 (_make_dangerous_record + NULL)

 339            LOAD_FAST_BORROW         1 (brokerage_id)

 340            LOAD_GLOBAL             14 (MemorySource)
                LOAD_ATTR               16 (OPTIMIZATION)

 341            LOAD_CONST               5 ('prompt_injection_in_recommendation')

 343            LOAD_CONST               6 ('recommendation_id')
                LOAD_FAST_BORROW         0 (recommendation)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               7 ('id')
                CALL                     1

 344            LOAD_CONST               8 ('source_kind')
                LOAD_CONST               9 ('optimization_recommendation')

 342            BUILD_MAP                2

 338            LOAD_CONST              10 (('brokerage_id', 'source', 'reason', 'lineage'))
                CALL_KW                  4
                RETURN_VALUE

 348   L12:     LOAD_FAST_BORROW         0 (recommendation)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              11 ('audience')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              12 ('')
       L13:     LOAD_ATTR               21 (lower + NULL|self)
                CALL                     0
                STORE_FAST               5 (audience)

 349            LOAD_FAST_BORROW         5 (audience)
                LOAD_CONST              23 (frozenset({'operator', 'broker'}))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN

 350            LOAD_CONST               1 (None)
                RETURN_VALUE

 352   L14:     LOAD_FAST_BORROW         0 (recommendation)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              13 ('confidence')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              12 ('')
       L15:     LOAD_ATTR               21 (lower + NULL|self)
                CALL                     0
                STORE_FAST               6 (confidence_label)

 353            LOAD_GLOBAL             22 (_RECOMMENDATION_CONFIDENCE)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_FAST_BORROW         6 (confidence_label)
                LOAD_CONST              14 (0.5)
                CALL                     2
                STORE_FAST               7 (confidence_val)

 354            LOAD_FAST_BORROW         7 (confidence_val)
                LOAD_GLOBAL             24 (CANDIDATE_CONFIDENCE_THRESHOLD)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L16)
                NOT_TAKEN

 355            LOAD_CONST               1 (None)
                RETURN_VALUE

 357   L16:     LOAD_FAST_BORROW         0 (recommendation)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              15 ('priority')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L17)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              12 ('')
       L17:     LOAD_ATTR               21 (lower + NULL|self)
                CALL                     0
                STORE_FAST               8 (priority)

 358            LOAD_GLOBAL             26 (_RECOMMENDATION_PRIORITY_WEIGHT)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_FAST_BORROW         8 (priority)
                LOAD_CONST              14 (0.5)
                CALL                     2
                STORE_FAST               9 (outcome_weight)

 360            LOAD_FAST_BORROW         0 (recommendation)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               2 ('title')
                CALL                     1
                STORE_FAST              10 (title)

 361            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW        10 (title)
                LOAD_GLOBAL              4 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L18)
                NOT_TAKEN
                LOAD_FAST_BORROW        10 (title)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN

 362   L18:     LOAD_CONST              16 ('Optimization recommendation')
                STORE_FAST              10 (title)

 364   L19:     LOAD_FAST_BORROW         0 (recommendation)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               3 ('insight')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        28 (to L20)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         0 (recommendation)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               4 ('recommended_action')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L20)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              12 ('')
       L20:     STORE_FAST              11 (insight)

 365            LOAD_GLOBAL              5 (str + NULL)
                LOAD_FAST_BORROW        11 (insight)
                CALL                     1
                LOAD_CONST              17 (slice(None, 512, None))
                BINARY_OP               26 ([])
                STORE_FAST              12 (summary)

 367            LOAD_GLOBAL             29 (MemoryRecord + NULL)

 368            LOAD_GLOBAL             31 (new_memory_id + NULL)
                CALL                     0

 369            LOAD_FAST_BORROW         1 (brokerage_id)

 370            LOAD_GLOBAL             32 (MemoryKind)
                LOAD_ATTR               16 (OPTIMIZATION)

 371            LOAD_GLOBAL             14 (MemorySource)
                LOAD_ATTR               16 (OPTIMIZATION)

 372            LOAD_GLOBAL             34 (MemoryStatus)
                LOAD_ATTR               36 (CANDIDATE)

 373            LOAD_FAST_BORROW        10 (title)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0

 374            LOAD_FAST_BORROW        12 (summary)

 376            LOAD_CONST              15 ('priority')
                LOAD_FAST_BORROW         8 (priority)

 377            LOAD_CONST              11 ('audience')
                LOAD_FAST_BORROW         5 (audience)

 378            LOAD_CONST              18 ('expected_impact')
                LOAD_FAST_BORROW         0 (recommendation)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              18 ('expected_impact')
                CALL                     1

 379            LOAD_CONST              19 ('affected_personality')
                LOAD_FAST_BORROW         0 (recommendation)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              19 ('affected_personality')
                CALL                     1

 380            LOAD_CONST              20 ('affected_strategy')
                LOAD_FAST_BORROW         0 (recommendation)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              20 ('affected_strategy')
                CALL                     1

 375            BUILD_MAP                5

 382            LOAD_FAST_BORROW         7 (confidence_val)

 383            LOAD_FAST_BORROW         9 (outcome_weight)

 385            LOAD_CONST               6 ('recommendation_id')
                LOAD_FAST_BORROW         0 (recommendation)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               7 ('id')
                CALL                     1

 386            LOAD_CONST               8 ('source_kind')
                LOAD_CONST               9 ('optimization_recommendation')

 384            BUILD_MAP                2

 367            LOAD_CONST              21 (('memory_id', 'brokerage_id', 'kind', 'source', 'status', 'title', 'summary', 'evidence', 'confidence', 'outcome_weight', 'lineage'))
                CALL_KW                 11
                RETURN_VALUE

  --   L21:     SWAP                     2
                POP_TOP

 333            SWAP                     3
                STORE_FAST               3 (v)
                STORE_FAST               2 (k)
                RERAISE                  0
ExceptionTable:
  L4 to L6 -> L21 [3]
  L7 to L8 -> L21 [3]
  L9 to L11 -> L21 [3]

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app\services\memory\classifier.py", line 395>:
395           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rec')

396           LOAD_CONST               2 ('dict')

395           LOAD_CONST               3 ('brokerage_id')

396           LOAD_CONST               4 ('str')

395           LOAD_CONST               5 ('return')

397           LOAD_CONST               6 ('Optional[MemoryRecord]')

395           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _candidate_from_reconstruction at 0x0000018C17F7B110, file "app\services\memory\classifier.py", line 395>:
395            RESUME                   0

398            LOAD_FAST_BORROW         0 (rec)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('final_outcome')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L1:     LOAD_ATTR                3 (lower + NULL|self)
               CALL                     0
               STORE_FAST               2 (final)

399            LOAD_FAST_BORROW         0 (rec)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               2 ('is_replayable')
               CALL                     1
               STORE_FAST               3 (is_replayable)

400            LOAD_GLOBAL              5 (list + NULL)
               LOAD_FAST_BORROW         0 (rec)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               3 ('missing_lifecycle_steps')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L2:     CALL                     1
               STORE_FAST               4 (missing)

401            LOAD_GLOBAL              7 (int + NULL)
               LOAD_FAST_BORROW         0 (rec)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               4 ('events_count')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_SMALL_INT           0
       L3:     CALL                     1
               STORE_FAST               5 (events_count)

403            LOAD_FAST_BORROW         3 (is_replayable)
               LOAD_CONST               5 (False)
               IS_OP                    0 (is)
               POP_JUMP_IF_FALSE       14 (to L4)
               NOT_TAKEN
               LOAD_FAST_BORROW         2 (final)
               LOAD_GLOBAL              8 (_POSITIVE_OUTCOMES)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

404            LOAD_CONST               6 (None)
               RETURN_VALUE

406    L4:     LOAD_FAST_BORROW         2 (final)
               LOAD_GLOBAL              8 (_POSITIVE_OUTCOMES)
               CONTAINS_OP              0 (in)
               STORE_FAST               6 (positive)

408            LOAD_FAST_BORROW         6 (positive)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               7 (0.7)
               JUMP_FORWARD            11 (to L7)
       L5:     LOAD_FAST_BORROW         3 (is_replayable)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               8 (0.45)
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               9 (0.3)
       L7:     STORE_FAST               7 (confidence)

409            LOAD_GLOBAL             10 (_OUTCOME_WEIGHTS)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_FAST_LOAD_FAST     38 (final, positive)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               9 (0.3)
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST              10 (0.2)
       L9:     CALL                     2
               STORE_FAST               8 (outcome_weight)

411            LOAD_FAST_BORROW         6 (positive)
               TO_BOOL
               POP_JUMP_IF_FALSE       17 (to L10)
               NOT_TAKEN
               LOAD_GLOBAL             12 (MemoryKind)
               LOAD_ATTR               14 (OPERATIONAL)
               JUMP_FORWARD            15 (to L11)
      L10:     LOAD_GLOBAL             12 (MemoryKind)
               LOAD_ATTR               16 (EPHEMERAL)
      L11:     STORE_FAST               9 (kind)

413            LOAD_GLOBAL             19 (MemoryRecord + NULL)

414            LOAD_GLOBAL             21 (new_memory_id + NULL)
               CALL                     0

415            LOAD_FAST                1 (brokerage_id)

416            LOAD_FAST                9 (kind)

417            LOAD_GLOBAL             22 (MemorySource)
               LOAD_ATTR               24 (REPLAY)

418            LOAD_GLOBAL             26 (MemoryStatus)
               LOAD_ATTR               28 (CANDIDATE)

420            LOAD_FAST_BORROW         6 (positive)
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L12)
               NOT_TAKEN
               LOAD_CONST              11 ('Outcome learned: ')
               LOAD_FAST_BORROW         2 (final)
               FORMAT_SIMPLE
               BUILD_STRING             2
               JUMP_FORWARD             1 (to L13)

421   L12:     LOAD_CONST              12 ('Reconstruction observed')

424   L13:     LOAD_CONST              13 ('Reconstruction closed with outcome=')
               LOAD_FAST                2 (final)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L14)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              14 ('unknown')
      L14:     FORMAT_SIMPLE
               LOAD_CONST              15 ('; ')

425            LOAD_FAST_BORROW         5 (events_count)
               FORMAT_SIMPLE
               LOAD_CONST              16 (' events, ')
               LOAD_GLOBAL             31 (len + NULL)
               LOAD_FAST_BORROW         4 (missing)
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              17 (' missing step(s).')

424            BUILD_STRING             7

428            LOAD_CONST              18 ('outcome')
               LOAD_FAST                2 (final)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L15)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              14 ('unknown')

429   L15:     LOAD_CONST               4 ('events_count')
               LOAD_FAST_BORROW         5 (events_count)

430            LOAD_CONST               2 ('is_replayable')
               LOAD_GLOBAL             33 (bool + NULL)
               LOAD_FAST_BORROW         3 (is_replayable)
               CALL                     1

431            LOAD_CONST               3 ('missing_lifecycle_steps')
               LOAD_FAST_BORROW         4 (missing)
               LOAD_CONST              19 (slice(None, 10, None))
               BINARY_OP               26 ([])

427            BUILD_MAP                4

433            LOAD_FAST_BORROW         7 (confidence)

434            LOAD_FAST_BORROW         8 (outcome_weight)

436            LOAD_CONST              20 ('call_id')
               LOAD_FAST_BORROW         0 (rec)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              20 ('call_id')
               CALL                     1

437            LOAD_CONST              21 ('source_kind')
               LOAD_CONST              22 ('memory_candidate_reconstruction')

435            BUILD_MAP                2

413            LOAD_CONST              23 (('memory_id', 'brokerage_id', 'kind', 'source', 'status', 'title', 'summary', 'evidence', 'confidence', 'outcome_weight', 'lineage'))
               CALL_KW                 11
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\memory\classifier.py", line 442>:
442           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('event')
              LOAD_CONST               2 ('dict')
              LOAD_CONST               3 ('brokerage_id')
              LOAD_CONST               4 ('str')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Optional[MemoryRecord]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _candidate_from_event at 0x0000018C17D8C5C0, file "app\services\memory\classifier.py", line 442>:
442           RESUME                   0

443           LOAD_FAST_BORROW         0 (event)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('event_type')
              CALL                     1
              STORE_FAST               2 (event_type)

444           LOAD_GLOBAL              3 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (event_type)
              LOAD_GLOBAL              4 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        9 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (event_type)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

445   L1:     LOAD_CONST               1 (None)
              RETURN_VALUE

449   L2:     LOAD_GLOBAL              7 (MemoryRecord + NULL)

450           LOAD_GLOBAL              9 (new_memory_id + NULL)
              CALL                     0

451           LOAD_FAST_BORROW         1 (brokerage_id)

452           LOAD_GLOBAL             10 (MemoryKind)
              LOAD_ATTR               12 (EPHEMERAL)

453           LOAD_GLOBAL             14 (MemorySource)
              LOAD_ATTR               16 (CALL)

454           LOAD_GLOBAL             18 (MemoryStatus)
              LOAD_ATTR               20 (CANDIDATE)

455           LOAD_CONST               2 ('Event observed: ')
              LOAD_FAST_BORROW         2 (event_type)
              FORMAT_SIMPLE
              BUILD_STRING             2

456           LOAD_CONST               3 ('Single event ')
              LOAD_FAST_BORROW         2 (event_type)
              FORMAT_SIMPLE
              LOAD_CONST               4 (' captured.')
              BUILD_STRING             3

458           LOAD_CONST               0 ('event_type')
              LOAD_FAST_BORROW         2 (event_type)

459           LOAD_CONST               5 ('actor')
              LOAD_FAST_BORROW         0 (event)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               5 ('actor')
              CALL                     1

460           LOAD_CONST               6 ('workflow_stage')
              LOAD_FAST_BORROW         0 (event)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               6 ('workflow_stage')
              CALL                     1

457           BUILD_MAP                3

462           LOAD_CONST               7 (0.4)

463           LOAD_CONST               8 (0.2)

465           LOAD_CONST               9 ('call_id')
              LOAD_FAST_BORROW         0 (event)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               9 ('call_id')
              CALL                     1

466           LOAD_CONST              10 ('event_id')
              LOAD_FAST_BORROW         0 (event)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              10 ('event_id')
              CALL                     1

467           LOAD_CONST              11 ('source_kind')
              LOAD_CONST              12 ('memory_candidate_event')

464           BUILD_MAP                3

449           LOAD_CONST              13 (('memory_id', 'brokerage_id', 'kind', 'source', 'status', 'title', 'summary', 'evidence', 'confidence', 'outcome_weight', 'lineage'))
              CALL_KW                 11
              RETURN_VALUE
```
