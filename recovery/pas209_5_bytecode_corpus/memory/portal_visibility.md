# memory/portal_visibility

- **pyc:** `app\services\memory\__pycache__\portal_visibility.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/portal_visibility.py`
- **co_filename (from bytecode):** `C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS146 — Portal-side PAS Brain visibility composer.

Read-only, tenant-scoped helper that wraps the existing PAS144B
(``queries.py``), PAS144M (``rollout_ledger.py``), and PAS144N
(``manifest_store.py``) readers and emits the three-card envelope
consumed by ``GET /portal/brain/visibility``.

Hard contract:
  * **Read-only.** Never writes, never mutates a record, never calls
    the rollout-apply or manifest-record paths.
  * **Tenant-scoped.** Every reader call passes ``brokerage_id``.
    There is no path through this helper that calls a cross-tenant
    operator-only reader, and the public surface refuses to operate
    without a valid brokerage dict.
  * **Feature-flagged off by default.** The flag is read from
    ``brokerage["brain_visibility_enabled"]`` (top level) OR
    ``brokerage["features"]["brain_visibility_enabled"]``. Only the
    literal Python ``True`` enables visibility — string ``"true"``,
    ``1``, ``"yes"`` are explicitly NOT enabled. When disabled,
    NO readers are called.
  * **Structural-only.** Cards carry counts and short status strings.
    Raw memory text, evidence payloads, plan blobs, manifest blobs,
    prompts, and transcripts are never surfaced.
  * **Fail closed without raising.** If any individual reader fails,
    the card for that section degrades to ``status="warning"`` with
    a structural ``detail`` token; the other cards are unaffected;
    the route never returns a 500 because of this helper.
  * **No widening of allowed config patching.** This module reads
    only — it cannot influence ``features.memory_injection_enabled``
    or any other tenant config.

Public surface (deliberately tiny):
  - brain_visibility_for_brokerage(brokerage) -> dict
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.services.memory`, `datetime`, `logging`, `manifest_store`, `queries`, `rollout_ledger`, `timedelta`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_disabled_envelope`, `_empty_card`, `_flag_enabled`, `_latest_manifest_card`, `_memory_candidates_card`, `_parse_iso`, `_rollout_decisions_card`, `_warning_card`, `brain_visibility_for_brokerage`

## Env-key candidates

`CANDIDATE`

## String constants (redacted where noted)

- '\nPAS146 — Portal-side PAS Brain visibility composer.\n\nRead-only, tenant-scoped helper that wraps the existing PAS144B\n(``queries.py``), PAS144M (``rollout_ledger.py``), and PAS144N\n(``manifest_store.py``) readers and emits the three-card envelope\nconsumed by ``GET /portal/brain/visibility``.\n\nHard contract:\n  * **Read-only.** Never writes, never mutates a record, never calls\n    the rollout-apply or manifest-record paths.\n  * **Tenant-scoped.** Every reader call passes ``brokerage_id``.\n    There is no path through this helper that calls a cross-tenant\n    operator-only reader, and the public surface refuses to operate\n    without a valid brokerage dict.\n  * **Feature-flagged off by default.** The flag is read from\n    ``brokerage["brain_visibility_enabled"]`` (top level) OR\n    ``brokerage["features"]["brain_visibility_enabled"]``. Only the\n    literal Python ``True`` enables visibility — string ``"true"``,\n    ``1``, ``"yes"`` are explicitly NOT enabled. When disabled,\n    NO readers are called.\n  * **Structural-only.** Cards carry counts and short status strings.\n    Raw memory text, evidence payloads, plan blobs, manifest blobs,\n    prompts, and transcripts are never surfaced.\n  * **Fail closed without raising.** If any individual reader fails,\n    the card for that section degrades to ``status="warning"`` with\n    a structural ``detail`` token; the other cards are unaffected;\n    the route never returns a 500 because of this helper.\n  * **No widening of allowed config patching.** This module reads\n    only — it cannot influence ``features.memory_injection_enabled``\n    or any other tenant config.\n\nPublic surface (deliberately tiny):\n  - brain_visibility_for_brokerage(brokerage) -> dict\n'
- 'pas.portal.brain_visibility'
- 'brain_visibility_enabled'
- 'memory_candidates'
- 'rollout_decisions_7d'
- 'latest_manifest'
- 'brokerage'
- 'Dict[str, Any]'
- 'return'
- 'bool'
- 'Strict-literal-True read of the brain_visibility_enabled flag.\n\nAccepts the flag at the top level (`brokerage[FLAG_KEY]`) OR\nunder `features` (`brokerage["features"][FLAG_KEY]`). Mirrors\nPAS144F/PAS144L\'s resolver doctrine — only the literal Python\n``True`` counts; strings, ints, and falsy values are explicitly\nNOT enabled.\n'
- 'features'
- 'The disabled-mode response shape. No reader is called when\nthe helper returns this. Tests pin this exact shape.'
- 'enabled'
- 'cards'
- 'warnings'
- 'brain_visibility_disabled'
- 'card_id'
- 'str'
- 'label'
- 'sub'
- 'A card shape used when a reader returns no usable data.'
- 'value'
- 'None'
- 'status'
- 'empty'
- 'detail'
- 'A card shape used when a reader failed. Never echoes payload\nvalues — `detail` is a short structural token.'
- 'n/a'
- 'warning'
- 'Any'
- 'Optional[datetime]'
- 'Coerce an ISO-8601 timestamp string into an aware datetime.\nReturns None for anything unparseable. Never raises.'
- '+00:00'
- 'brokerage_id'
- 'Count of memory records in CANDIDATE status for the tenant.'
- 'Memory Candidates'
- 'Pending review'
- 'CANDIDATE'
- 'brain_visibility candidates reader failed | brokerage='
- ' | error_type='
- 'reader_failed'
- 'unexpected_reader_shape'
- 'Count of rollout ledger rows in the last 7 days for the tenant.'
- 'Rollout Decisions'
- 'Last 7 days'
- 'brain_visibility ledger reader failed | brokerage='
- 'created_at'
- 'The recommended_action + approved_at of the latest signed manifest.'
- 'Latest Manifest'
- 'brain_visibility manifest reader failed | brokerage='
- 'No signed manifest yet'
- 'unexpected_row_shape'
- 'recommended_action'
- 'approved_at'
- 'No timestamp'
- 'Return the PAS Brain visibility envelope for the given brokerage.\n\nInput: the authenticated brokerage row (the dict returned by\n``app/db/brokerage_store.get_brokerage_by_api_key``).\n\nOutput shape:\n    {\n        "enabled":  bool,\n        "cards":    [<card>, <card>, <card>],\n        "warnings": [<short structural token>, ...],\n    }\n\nWhen the feature flag is OFF (default), every call returns:\n    {"enabled": False, "cards": [], "warnings": ["brain_visibility_disabled"]}\nand NO downstream reader is invoked.\n\nPure-ish: never writes, never mutates inputs. Never raises — a\nreader failure degrades the affected card to ``status="warning"``\nwhile the other two cards continue to render.\n'
- 'brain_visibility refused | reason=missing_or_invalid_brokerage_id'
- 'missing_brokerage_id'
- 'unknown_card_warning'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS146 — Portal-side PAS Brain visibility composer.\n\nRead-only, tenant-scoped helper that wraps the existing PAS144B\n(``queries.py``), PAS144M (``rollout_ledger.py``), and PAS144N\n(``manifest_store.py``) readers and emits the three-card envelope\nconsumed by ``GET /portal/brain/visibility``.\n\nHard contract:\n  * **Read-only.** Never writes, never mutates a record, never calls\n    the rollout-apply or manifest-record paths.\n  * **Tenant-scoped.** Every reader call passes ``brokerage_id``.\n    There is no path through this helper that calls a cross-tenant\n    operator-only reader, and the public surface refuses to operate\n    without a valid brokerage dict.\n  * **Feature-flagged off by default.** The flag is read from\n    ``brokerage["brain_visibility_enabled"]`` (top level) OR\n    ``brokerage["features"]["brain_visibility_enabled"]``. Only the\n    literal Python ``True`` enables visibility — string ``"true"``,\n    ``1``, ``"yes"`` are explicitly NOT enabled. When disabled,\n    NO readers are called.\n  * **Structural-only.** Cards carry counts and short status strings.\n    Raw memory text, evidence payloads, plan blobs, manifest blobs,\n    prompts, and transcripts are never surfaced.\n  * **Fail closed without raising.** If any individual reader fails,\n    the card for that section degrades to ``status="warning"`` with\n    a structural ``detail`` token; the other cards are unaffected;\n    the route never returns a 500 because of this helper.\n  * **No widening of allowed config patching.** This module reads\n    only — it cannot influence ``features.memory_injection_enabled``\n    or any other tenant config.\n\nPublic surface (deliberately tiny):\n  - brain_visibility_for_brokerage(brokerage) -> dict\n')
              STORE_NAME               0 (__doc__)

 37           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 39           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 40           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timedelta', 'timezone'))
              IMPORT_NAME              4 (datetime)
              IMPORT_FROM              4 (datetime)
              STORE_NAME               4 (datetime)
              IMPORT_FROM              5 (timedelta)
              STORE_NAME               5 (timedelta)
              IMPORT_FROM              6 (timezone)
              STORE_NAME               6 (timezone)
              POP_TOP

 41           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              7 (typing)
              IMPORT_FROM              8 (Any)
              STORE_NAME               8 (Any)
              IMPORT_FROM              9 (Dict)
              STORE_NAME               9 (Dict)
              IMPORT_FROM             10 (List)
              STORE_NAME              10 (List)
              IMPORT_FROM             11 (Optional)
              STORE_NAME              11 (Optional)
              POP_TOP

 43           LOAD_NAME                3 (logging)
              LOAD_ATTR               24 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.portal.brain_visibility')
              CALL                     1
              STORE_NAME              13 (logger)

 52           LOAD_CONST               6 ('brain_visibility_enabled')
              STORE_NAME              14 (_FLAG_KEY)

 56           LOAD_CONST               7 ('memory_candidates')
              STORE_NAME              15 (CARD_MEMORY_CANDIDATES)

 57           LOAD_CONST               8 ('rollout_decisions_7d')
              STORE_NAME              16 (CARD_ROLLOUT_DECISIONS)

 58           LOAD_CONST               9 ('latest_manifest')
              STORE_NAME              17 (CARD_LATEST_MANIFEST)

 61           LOAD_NAME               15 (CARD_MEMORY_CANDIDATES)

 62           LOAD_NAME               16 (CARD_ROLLOUT_DECISIONS)

 63           LOAD_NAME               17 (CARD_LATEST_MANIFEST)

 60           BUILD_TUPLE              3
              STORE_NAME              18 (CARD_IDS)

 68           LOAD_SMALL_INT         200
              STORE_NAME              19 (_MEMORY_CANDIDATES_CAP)

 69           LOAD_SMALL_INT         100
              STORE_NAME              20 (_ROLLOUT_LEDGER_CAP)

 70           LOAD_SMALL_INT           7
              STORE_NAME              21 (_ROLLOUT_WINDOW_DAYS)

 75           LOAD_SMALL_INT          50
              STORE_NAME              22 (_MEMORY_CANDIDATES_WARN_AT)

 82           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA2D30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 82>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _flag_enabled at 0x0000018C18048730, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 82>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              23 (_flag_enabled)

101           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA33C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 101>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _disabled_envelope at 0x0000018C17FA3690, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 101>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_disabled_envelope)

111           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C18025C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 111>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _empty_card at 0x0000018C17FA35A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 111>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_empty_card)

122           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18024C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 122>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _warning_card at 0x0000018C17FA3780, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 122>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_warning_card)

134           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA2C40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 134>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object _parse_iso at 0x0000018C17F0C960, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 134>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_parse_iso)

155           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA2100, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 155>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object _memory_candidates_card at 0x0000018C17D8E300, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 155>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_memory_candidates_card)

192           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3B40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 192>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object _rollout_decisions_card at 0x0000018C17D78680, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 192>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_rollout_decisions_card)

240           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA2880, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 240>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object _latest_manifest_card at 0x0000018C17F84AA0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 240>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_latest_manifest_card)

294           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA3C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 294>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object brain_visibility_for_brokerage at 0x0000018C17EA6B90, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 294>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (brain_visibility_for_brokerage)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 82>:
 82           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _flag_enabled at 0x0000018C18048730, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 82>:
 82           RESUME                   0

 91           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 92           LOAD_CONST               1 (False)
              RETURN_VALUE

 93   L1:     LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_GLOBAL              6 (_FLAG_KEY)
              CALL                     1
              LOAD_CONST               2 (True)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

 94           LOAD_CONST               2 (True)
              RETURN_VALUE

 95   L2:     LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               3 ('features')
              CALL                     1
              STORE_FAST               1 (features)

 96           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (features)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       28 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (features)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_GLOBAL              6 (_FLAG_KEY)
              CALL                     1
              LOAD_CONST               2 (True)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

 97           LOAD_CONST               2 (True)
              RETURN_VALUE

 98   L3:     LOAD_CONST               1 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 101>:
101           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _disabled_envelope at 0x0000018C17FA3690, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 101>:
101           RESUME                   0

105           LOAD_CONST               1 ('enabled')
              LOAD_CONST               2 (False)

106           LOAD_CONST               3 ('cards')
              BUILD_LIST               0

107           LOAD_CONST               4 ('warnings')
              LOAD_CONST               5 ('brain_visibility_disabled')
              BUILD_LIST               1

104           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 111>:
111           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('card_id')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('label')
              LOAD_CONST               2 ('str')
              LOAD_CONST               4 ('sub')
              LOAD_CONST               2 ('str')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Dict[str, Any]')
              BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _empty_card at 0x0000018C17FA35A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 111>:
111           RESUME                   0

114           LOAD_CONST               1 ('id')
              LOAD_FAST_BORROW         0 (card_id)

115           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         1 (label)

116           LOAD_CONST               3 ('value')
              LOAD_CONST               4 ('None')

117           LOAD_CONST               5 ('sub')
              LOAD_FAST_BORROW         2 (sub)

118           LOAD_CONST               6 ('status')
              LOAD_CONST               7 ('empty')

113           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 122>:
122           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('card_id')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('label')
              LOAD_CONST               2 ('str')
              LOAD_CONST               4 ('detail')
              LOAD_CONST               2 ('str')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Dict[str, Any]')
              BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _warning_card at 0x0000018C17FA3780, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 122>:
122           RESUME                   0

126           LOAD_CONST               1 ('id')
              LOAD_FAST_BORROW         0 (card_id)

127           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         1 (label)

128           LOAD_CONST               3 ('value')
              LOAD_CONST               4 ('n/a')

129           LOAD_CONST               5 ('sub')
              LOAD_FAST_BORROW         2 (detail)

130           LOAD_CONST               6 ('status')
              LOAD_CONST               7 ('warning')

125           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 134>:
134           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[datetime]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _parse_iso at 0x0000018C17F0C960, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 134>:
 134            RESUME                   0

 137            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN

 138    L1:     LOAD_CONST               1 (None)
                RETURN_VALUE

 139    L2:     LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               1 (s)

 141            LOAD_FAST_BORROW         1 (s)
                LOAD_ATTR                7 (endswith + NULL|self)
                LOAD_CONST               2 ('Z')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (s)
                LOAD_ATTR                9 (replace + NULL|self)
                LOAD_CONST               2 ('Z')
                LOAD_CONST               3 ('+00:00')
                CALL                     2
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_FAST                1 (s)
        L4:     STORE_FAST               1 (s)

 142            NOP

 143    L5:     LOAD_GLOBAL             10 (datetime)
                LOAD_ATTR               12 (fromisoformat)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (s)
                CALL                     1
                STORE_FAST               2 (dt)

 146    L6:     LOAD_FAST                2 (dt)
                LOAD_ATTR               16 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L7)
                NOT_TAKEN

 147            LOAD_FAST                2 (dt)
                LOAD_ATTR                9 (replace + NULL|self)
                LOAD_GLOBAL             18 (timezone)
                LOAD_ATTR               20 (utc)
                LOAD_CONST               4 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST               2 (dt)

 148    L7:     LOAD_FAST                2 (dt)
                RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

 144            LOAD_GLOBAL             14 (ValueError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L10)
                NOT_TAKEN
                POP_TOP

 145    L9:     POP_EXCEPT
                LOAD_CONST               1 (None)
                RETURN_VALUE

 144   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L8 [0]
  L8 to L9 -> L11 [1] lasti
  L10 to L11 -> L11 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 155>:
155           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _memory_candidates_card at 0x0000018C17D8E300, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 155>:
 155            RESUME                   0

 157            LOAD_CONST               1 ('Memory Candidates')
                STORE_FAST               1 (label)

 158            LOAD_CONST               2 ('Pending review')
                STORE_FAST               2 (sub_ok)

 159            NOP

 161    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               3 (('queries',))
                IMPORT_NAME              0 (app.services.memory)
                IMPORT_FROM              1 (queries)
                STORE_FAST               3 (queries_mod)
                POP_TOP

 162            LOAD_FAST_BORROW         3 (queries_mod)
                LOAD_ATTR                5 (list_memory_for_brokerage + NULL|self)

 163            LOAD_FAST_BORROW         0 (brokerage_id)

 164            LOAD_CONST               4 ('CANDIDATE')

 165            LOAD_GLOBAL              6 (_MEMORY_CANDIDATES_CAP)

 162            LOAD_CONST               5 (('status', 'limit'))
                CALL_KW                  3
                STORE_FAST               4 (rows)

 176    L2:     LOAD_GLOBAL             23 (isinstance + NULL)
                LOAD_FAST                4 (rows)
                LOAD_GLOBAL             24 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L3)
                NOT_TAKEN

 177            LOAD_GLOBAL             19 (_warning_card + NULL)

 178            LOAD_GLOBAL             20 (CARD_MEMORY_CANDIDATES)
                LOAD_FAST                1 (label)
                LOAD_CONST              10 ('unexpected_reader_shape')

 177            CALL                     3
                RETURN_VALUE

 181    L3:     LOAD_GLOBAL             27 (len + NULL)
                LOAD_FAST                4 (rows)
                CALL                     1
                STORE_FAST               6 (count)

 182            LOAD_FAST                6 (count)
                LOAD_GLOBAL             28 (_MEMORY_CANDIDATES_WARN_AT)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_CONST              11 ('warning')
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST              12 ('ok')
        L5:     STORE_FAST               7 (status)

 184            LOAD_CONST              13 ('id')
                LOAD_GLOBAL             20 (CARD_MEMORY_CANDIDATES)

 185            LOAD_CONST              14 ('label')
                LOAD_FAST                1 (label)

 186            LOAD_CONST              15 ('value')
                LOAD_FAST                6 (count)

 187            LOAD_CONST              16 ('sub')
                LOAD_FAST                2 (sub_ok)

 188            LOAD_CONST              17 ('status')
                LOAD_FAST                7 (status)

 183            BUILD_MAP                5
                RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 167            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       74 (to L11)
                NOT_TAKEN
                STORE_FAST               5 (e)

 168    L7:     LOAD_GLOBAL             10 (logger)
                LOAD_ATTR               13 (warning + NULL|self)

 169            LOAD_CONST               6 ('brain_visibility candidates reader failed | brokerage=')

 170            LOAD_FAST                0 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST               7 (' | error_type=')
                LOAD_GLOBAL             15 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               16 (__name__)
                FORMAT_SIMPLE

 169            BUILD_STRING             4

 168            CALL                     1
                POP_TOP

 172            LOAD_GLOBAL             19 (_warning_card + NULL)

 173            LOAD_GLOBAL             20 (CARD_MEMORY_CANDIDATES)
                LOAD_FAST                1 (label)
                LOAD_CONST               8 ('reader_failed')

 172            CALL                     3
        L8:     SWAP                     2
        L9:     POP_EXCEPT
                LOAD_CONST               9 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RETURN_VALUE

  --   L10:     LOAD_CONST               9 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 167   L11:     RERAISE                  0

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L6 [0]
  L6 to L7 -> L12 [1] lasti
  L7 to L8 -> L10 [1] lasti
  L8 to L9 -> L12 [1] lasti
  L10 to L12 -> L12 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 192>:
192           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _rollout_decisions_card at 0x0000018C17D78680, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 192>:
 192            RESUME                   0

 194            LOAD_CONST               1 ('Rollout Decisions')
                STORE_FAST               1 (label)

 195            LOAD_CONST               2 ('Last 7 days')
                STORE_FAST               2 (sub_ok)

 196            NOP

 197    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               3 (('rollout_ledger',))
                IMPORT_NAME              0 (app.services.memory)
                IMPORT_FROM              1 (rollout_ledger)
                STORE_FAST               3 (ledger_mod)
                POP_TOP

 198            LOAD_FAST_BORROW         3 (ledger_mod)
                LOAD_ATTR                5 (list_rollout_history_for_brokerage + NULL|self)

 199            LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_GLOBAL              6 (_ROLLOUT_LEDGER_CAP)

 198            LOAD_CONST               4 (('limit',))
                CALL_KW                  2
                STORE_FAST               4 (rows)

 210    L2:     LOAD_GLOBAL             23 (isinstance + NULL)
                LOAD_FAST                4 (rows)
                LOAD_GLOBAL             24 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L3)
                NOT_TAKEN

 211            LOAD_GLOBAL             19 (_warning_card + NULL)

 212            LOAD_GLOBAL             20 (CARD_ROLLOUT_DECISIONS)
                LOAD_FAST                1 (label)
                LOAD_CONST               9 ('unexpected_reader_shape')

 211            CALL                     3
                RETURN_VALUE

 215    L3:     LOAD_GLOBAL             26 (datetime)
                LOAD_ATTR               28 (now)
                PUSH_NULL
                LOAD_GLOBAL             30 (timezone)
                LOAD_ATTR               32 (utc)
                CALL                     1
                LOAD_GLOBAL             35 (timedelta + NULL)
                LOAD_GLOBAL             36 (_ROLLOUT_WINDOW_DAYS)
                LOAD_CONST              10 (('days',))
                CALL_KW                  1
                BINARY_OP               10 (-)
                STORE_FAST               6 (cutoff)

 216            LOAD_SMALL_INT           0
                STORE_FAST               7 (count)

 217            LOAD_FAST                4 (rows)
                GET_ITER
        L4:     FOR_ITER                85 (to L8)
                STORE_FAST               8 (row)

 218            LOAD_GLOBAL             23 (isinstance + NULL)
                LOAD_FAST                8 (row)
                LOAD_GLOBAL             38 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN

 219            JUMP_BACKWARD           27 (to L4)

 220    L5:     LOAD_GLOBAL             41 (_parse_iso + NULL)
                LOAD_FAST                8 (row)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST              11 ('created_at')
                CALL                     1
                CALL                     1
                STORE_FAST               9 (created_at)

 221            LOAD_FAST                9 (created_at)
                POP_JUMP_IF_NOT_NONE    12 (to L6)
                NOT_TAKEN

 224            LOAD_FAST                7 (count)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               7 (count)

 225            JUMP_BACKWARD           68 (to L4)

 226    L6:     LOAD_FAST_LOAD_FAST    150 (created_at, cutoff)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           76 (to L4)

 227    L7:     LOAD_FAST                7 (count)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               7 (count)
                JUMP_BACKWARD           87 (to L4)

 217    L8:     END_FOR
                POP_ITER

 232            LOAD_CONST              12 ('id')
                LOAD_GLOBAL             20 (CARD_ROLLOUT_DECISIONS)

 233            LOAD_CONST              13 ('label')
                LOAD_FAST                1 (label)

 234            LOAD_CONST              14 ('value')
                LOAD_FAST                7 (count)

 235            LOAD_CONST              15 ('sub')
                LOAD_FAST                2 (sub_ok)

 236            LOAD_CONST              16 ('status')
                LOAD_CONST              17 ('ok')

 231            BUILD_MAP                5
                RETURN_VALUE

  --    L9:     PUSH_EXC_INFO

 201            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       74 (to L14)
                NOT_TAKEN
                STORE_FAST               5 (e)

 202   L10:     LOAD_GLOBAL             10 (logger)
                LOAD_ATTR               13 (warning + NULL|self)

 203            LOAD_CONST               5 ('brain_visibility ledger reader failed | brokerage=')

 204            LOAD_FAST                0 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST               6 (' | error_type=')
                LOAD_GLOBAL             15 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               16 (__name__)
                FORMAT_SIMPLE

 203            BUILD_STRING             4

 202            CALL                     1
                POP_TOP

 206            LOAD_GLOBAL             19 (_warning_card + NULL)

 207            LOAD_GLOBAL             20 (CARD_ROLLOUT_DECISIONS)
                LOAD_FAST                1 (label)
                LOAD_CONST               7 ('reader_failed')

 206            CALL                     3
       L11:     SWAP                     2
       L12:     POP_EXCEPT
                LOAD_CONST               8 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RETURN_VALUE

  --   L13:     LOAD_CONST               8 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 201   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L9 [0]
  L9 to L10 -> L15 [1] lasti
  L10 to L11 -> L13 [1] lasti
  L11 to L12 -> L15 [1] lasti
  L13 to L15 -> L15 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 240>:
240           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _latest_manifest_card at 0x0000018C17F84AA0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 240>:
 240            RESUME                   0

 242            LOAD_CONST               1 ('Latest Manifest')
                STORE_FAST               1 (label)

 243            NOP

 244    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               2 (('manifest_store',))
                IMPORT_NAME              0 (app.services.memory)
                IMPORT_FROM              1 (manifest_store)
                STORE_FAST               2 (manifest_store)
                POP_TOP

 245            LOAD_FAST_BORROW         2 (manifest_store)
                LOAD_ATTR                5 (list_manifests_for_brokerage + NULL|self)

 246            LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_SMALL_INT           1

 245            LOAD_CONST               3 (('limit',))
                CALL_KW                  2
                STORE_FAST               3 (rows)

 257    L2:     LOAD_GLOBAL             21 (isinstance + NULL)
                LOAD_FAST                3 (rows)
                LOAD_GLOBAL             22 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L3)
                NOT_TAKEN

 258            LOAD_GLOBAL             17 (_warning_card + NULL)

 259            LOAD_GLOBAL             18 (CARD_LATEST_MANIFEST)
                LOAD_FAST                1 (label)
                LOAD_CONST               8 ('unexpected_reader_shape')

 258            CALL                     3
                RETURN_VALUE

 262    L3:     LOAD_FAST                3 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L4)
                NOT_TAKEN

 263            LOAD_GLOBAL             25 (_empty_card + NULL)

 264            LOAD_GLOBAL             18 (CARD_LATEST_MANIFEST)
                LOAD_FAST                1 (label)

 265            LOAD_CONST               9 ('No signed manifest yet')

 263            CALL                     3
                RETURN_VALUE

 268    L4:     LOAD_FAST                3 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                STORE_FAST               5 (row)

 269            LOAD_GLOBAL             21 (isinstance + NULL)
                LOAD_FAST                5 (row)
                LOAD_GLOBAL             26 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L5)
                NOT_TAKEN

 270            LOAD_GLOBAL             17 (_warning_card + NULL)

 271            LOAD_GLOBAL             18 (CARD_LATEST_MANIFEST)
                LOAD_FAST                1 (label)
                LOAD_CONST              10 ('unexpected_row_shape')

 270            CALL                     3
                RETURN_VALUE

 274    L5:     LOAD_FAST                5 (row)
                LOAD_ATTR               29 (get + NULL|self)
                LOAD_CONST              11 ('recommended_action')
                CALL                     1
                STORE_FAST               6 (action)

 275            LOAD_FAST                5 (row)
                LOAD_ATTR               29 (get + NULL|self)
                LOAD_CONST              12 ('approved_at')
                CALL                     1
                STORE_FAST               7 (approved_at)

 276            LOAD_GLOBAL             21 (isinstance + NULL)
                LOAD_FAST                6 (action)
                LOAD_GLOBAL             30 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        9 (to L6)
                NOT_TAKEN
                LOAD_FAST                6 (action)
                TO_BOOL
                POP_JUMP_IF_TRUE         4 (to L7)
                NOT_TAKEN

 277    L6:     LOAD_CONST              13 ('None')
                STORE_FAST               8 (action_value)
                JUMP_FORWARD             2 (to L8)

 279    L7:     LOAD_FAST                6 (action)
                STORE_FAST               8 (action_value)

 280    L8:     LOAD_GLOBAL             21 (isinstance + NULL)
                LOAD_FAST                7 (approved_at)
                LOAD_GLOBAL             30 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       11 (to L9)
                NOT_TAKEN
                LOAD_FAST                7 (approved_at)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_FAST                7 (approved_at)
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST              14 ('No timestamp')
       L10:     STORE_FAST               9 (sub)

 282            LOAD_CONST              15 ('id')
                LOAD_GLOBAL             18 (CARD_LATEST_MANIFEST)

 283            LOAD_CONST              16 ('label')
                LOAD_FAST                1 (label)

 284            LOAD_CONST              17 ('value')
                LOAD_FAST                8 (action_value)

 285            LOAD_CONST              18 ('sub')
                LOAD_FAST                9 (sub)

 286            LOAD_CONST              19 ('status')
                LOAD_CONST              20 ('ok')

 281            BUILD_MAP                5
                RETURN_VALUE

  --   L11:     PUSH_EXC_INFO

 248            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       74 (to L16)
                NOT_TAKEN
                STORE_FAST               4 (e)

 249   L12:     LOAD_GLOBAL              8 (logger)
                LOAD_ATTR               11 (warning + NULL|self)

 250            LOAD_CONST               4 ('brain_visibility manifest reader failed | brokerage=')

 251            LOAD_FAST                0 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST               5 (' | error_type=')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE

 250            BUILD_STRING             4

 249            CALL                     1
                POP_TOP

 253            LOAD_GLOBAL             17 (_warning_card + NULL)

 254            LOAD_GLOBAL             18 (CARD_LATEST_MANIFEST)
                LOAD_FAST                1 (label)
                LOAD_CONST               6 ('reader_failed')

 253            CALL                     3
       L13:     SWAP                     2
       L14:     POP_EXCEPT
                LOAD_CONST               7 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RETURN_VALUE

  --   L15:     LOAD_CONST               7 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 248   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L11 [0]
  L11 to L12 -> L17 [1] lasti
  L12 to L13 -> L15 [1] lasti
  L13 to L14 -> L17 [1] lasti
  L15 to L17 -> L17 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 294>:
294           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object brain_visibility_for_brokerage at 0x0000018C17EA6B90, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\portal_visibility.py", line 294>:
294           RESUME                   0

315           LOAD_GLOBAL              1 (_flag_enabled + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_TRUE        11 (to L1)
              NOT_TAKEN

316           LOAD_GLOBAL              3 (_disabled_envelope + NULL)
              CALL                     0
              RETURN_VALUE

319   L1:     LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('id')
              CALL                     1
              STORE_FAST               1 (brokerage_id)

320           LOAD_GLOBAL              7 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (brokerage_id)
              LOAD_GLOBAL              8 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (brokerage_id)
              LOAD_ATTR               11 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE        31 (to L3)
              NOT_TAKEN

324   L2:     LOAD_GLOBAL             12 (logger)
              LOAD_ATTR               15 (warning + NULL|self)

325           LOAD_CONST               2 ('brain_visibility refused | reason=missing_or_invalid_brokerage_id')

324           CALL                     1
              POP_TOP

328           LOAD_CONST               3 ('enabled')
              LOAD_CONST               4 (False)

329           LOAD_CONST               5 ('cards')
              BUILD_LIST               0

330           LOAD_CONST               6 ('warnings')
              LOAD_CONST               7 ('missing_brokerage_id')
              BUILD_LIST               1

327           BUILD_MAP                3
              RETURN_VALUE

333   L3:     LOAD_FAST_BORROW         1 (brokerage_id)
              LOAD_ATTR               11 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (brokerage_id)

335           LOAD_GLOBAL             17 (_memory_candidates_card + NULL)
              LOAD_FAST_BORROW         1 (brokerage_id)
              CALL                     1

336           LOAD_GLOBAL             19 (_rollout_decisions_card + NULL)
              LOAD_FAST_BORROW         1 (brokerage_id)
              CALL                     1

337           LOAD_GLOBAL             21 (_latest_manifest_card + NULL)
              LOAD_FAST_BORROW         1 (brokerage_id)
              CALL                     1

334           BUILD_LIST               3
              STORE_FAST               2 (cards)

339           BUILD_LIST               0
              STORE_FAST               3 (warnings)

340           LOAD_FAST_BORROW         2 (cards)
              GET_ITER
      L4:     FOR_ITER                69 (to L7)
              STORE_FAST               4 (c)

341           LOAD_FAST_BORROW         4 (c)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               8 ('status')
              CALL                     1
              LOAD_CONST               9 ('warning')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           27 (to L4)

342   L5:     LOAD_FAST                3 (warnings)
              LOAD_ATTR               23 (append + NULL|self)
              LOAD_FAST_BORROW         4 (c)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('id')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST              10 ('unknown_card_warning')
      L6:     CALL                     1
              POP_TOP
              JUMP_BACKWARD           71 (to L4)

340   L7:     END_FOR
              POP_ITER

345           LOAD_CONST               3 ('enabled')
              LOAD_CONST              11 (True)

346           LOAD_CONST               5 ('cards')
              LOAD_FAST_BORROW         2 (cards)

347           LOAD_CONST               6 ('warnings')
              LOAD_FAST_BORROW         3 (warnings)

344           BUILD_MAP                3
              RETURN_VALUE
```
