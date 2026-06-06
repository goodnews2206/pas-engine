# memory/__init__

- **pyc:** `app\services\memory\__pycache__\__init__.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/__init__.py`
- **co_filename (from bytecode):** `app\services\memory\__init__.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144A — Operational Memory module.

Contracts, classifier, and governance for PAS Brain memory.
Storage / retrieval / vectorization are explicitly out of scope at
this stage (see docs/pas144a_memory_contracts.md).
```

## Imports

`CANDIDATE_CONFIDENCE_THRESHOLD`, `DEFAULT_TTL_DAYS`, `MemoryKind`, `MemoryRecord`, `MemorySource`, `MemoryStatus`, `OPERATIONAL_OUTCOME_WEIGHT_THRESHOLD`, `apply_memory_governance`, `classifier`, `classify_memory_candidate`, `classify_optimization_recommendation`, `classify_replay_pattern`, `contracts`, `governance`, `has_forbidden_transcript_field`, `memory_ttl_for_kind`, `new_memory_id`, `should_persist_memory`, `should_quarantine_memory`, `validate_memory_record`

## Classes

_none_

## Functions / methods

_none_

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS144A — Operational Memory module.\n\nContracts, classifier, and governance for PAS Brain memory.\nStorage / retrieval / vectorization are explicitly out of scope at\nthis stage (see docs/pas144a_memory_contracts.md).\n'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS144A — Operational Memory module.\n\nContracts, classifier, and governance for PAS Brain memory.\nStorage / retrieval / vectorization are explicitly out of scope at\nthis stage (see docs/pas144a_memory_contracts.md).\n')
              STORE_NAME               0 (__doc__)

  9           LOAD_SMALL_INT           1
              LOAD_CONST               1 (('CANDIDATE_CONFIDENCE_THRESHOLD', 'DEFAULT_TTL_DAYS', 'MemoryKind', 'MemoryRecord', 'MemorySource', 'MemoryStatus', 'OPERATIONAL_OUTCOME_WEIGHT_THRESHOLD', 'has_forbidden_transcript_field', 'new_memory_id'))
              IMPORT_NAME              1 (contracts)
              IMPORT_FROM              2 (CANDIDATE_CONFIDENCE_THRESHOLD)
              STORE_NAME               2 (CANDIDATE_CONFIDENCE_THRESHOLD)
              IMPORT_FROM              3 (DEFAULT_TTL_DAYS)
              STORE_NAME               3 (DEFAULT_TTL_DAYS)
              IMPORT_FROM              4 (MemoryKind)
              STORE_NAME               4 (MemoryKind)
              IMPORT_FROM              5 (MemoryRecord)
              STORE_NAME               5 (MemoryRecord)
              IMPORT_FROM              6 (MemorySource)
              STORE_NAME               6 (MemorySource)
              IMPORT_FROM              7 (MemoryStatus)
              STORE_NAME               7 (MemoryStatus)
              IMPORT_FROM              8 (OPERATIONAL_OUTCOME_WEIGHT_THRESHOLD)
              STORE_NAME               8 (OPERATIONAL_OUTCOME_WEIGHT_THRESHOLD)
              IMPORT_FROM              9 (has_forbidden_transcript_field)
              STORE_NAME               9 (has_forbidden_transcript_field)
              IMPORT_FROM             10 (new_memory_id)
              STORE_NAME              10 (new_memory_id)
              POP_TOP

 20           LOAD_SMALL_INT           1
              LOAD_CONST               2 (('classify_memory_candidate', 'classify_optimization_recommendation', 'classify_replay_pattern'))
              IMPORT_NAME             11 (classifier)
              IMPORT_FROM             12 (classify_memory_candidate)
              STORE_NAME              12 (classify_memory_candidate)
              IMPORT_FROM             13 (classify_optimization_recommendation)
              STORE_NAME              13 (classify_optimization_recommendation)
              IMPORT_FROM             14 (classify_replay_pattern)
              STORE_NAME              14 (classify_replay_pattern)
              POP_TOP

 25           LOAD_SMALL_INT           1
              LOAD_CONST               3 (('apply_memory_governance', 'memory_ttl_for_kind', 'should_persist_memory', 'should_quarantine_memory', 'validate_memory_record'))
              IMPORT_NAME             15 (governance)
              IMPORT_FROM             16 (apply_memory_governance)
              STORE_NAME              16 (apply_memory_governance)
              IMPORT_FROM             17 (memory_ttl_for_kind)
              STORE_NAME              17 (memory_ttl_for_kind)
              IMPORT_FROM             18 (should_persist_memory)
              STORE_NAME              18 (should_persist_memory)
              IMPORT_FROM             19 (should_quarantine_memory)
              STORE_NAME              19 (should_quarantine_memory)
              IMPORT_FROM             20 (validate_memory_record)
              STORE_NAME              20 (validate_memory_record)
              POP_TOP

 33           BUILD_LIST               0
              LOAD_CONST               5 (('MemoryKind', 'MemorySource', 'MemoryStatus', 'MemoryRecord', 'DEFAULT_TTL_DAYS', 'CANDIDATE_CONFIDENCE_THRESHOLD', 'OPERATIONAL_OUTCOME_WEIGHT_THRESHOLD', 'new_memory_id', 'has_forbidden_transcript_field', 'classify_memory_candidate', 'classify_replay_pattern', 'classify_optimization_recommendation', 'validate_memory_record', 'should_persist_memory', 'should_quarantine_memory', 'memory_ttl_for_kind', 'apply_memory_governance'))
              LIST_EXTEND              1
              STORE_NAME              21 (__all__)
              LOAD_CONST               4 (None)
              RETURN_VALUE
```
