# optimization/strategies

- **pyc:** `app\services\optimization\__pycache__\strategies.cpython-314.pyc`
- **expected source path (absent):** `app\services\optimization/strategies.py`
- **co_filename (from bytecode):** `app\services\optimization\strategies.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** optimization

## Module docstring

```
PAS143A — Strategy variant registry.

Each StrategyVariant declares an `engine_overrides` dict that is
shallow-merged into the brokerage config consumed by PASEngine
(see PASEngine.__init__ for the keys it actually reads). Unrecognised
keys ride along as inert metadata so future engine knobs can be
declared here ahead of the engine plumbing.

Recognised brokerage keys today (from app/engine/state_machine.py):
  - agent_name                 (str)   — appears verbatim in greeting
  - ai_disclosure_enabled      (bool)  — toggles the recording line
  - transfer_enabled           (bool)  — gates _is_transfer_request
  - booking_enabled            (bool)  — gates _handle_booking
  - max_objection_attempts     (int)   — when objection→DONE fires
  - trained_booking_prompt     (str)   — replaces booking question
  - trained_objection_prompt   (str)   — used by handle_objection LLM
                                          (mocked in simulations, so this
                                          override has no observable
                                          effect at sim time)
```

## Imports

`Dict`, `FrozenSet`, `Tuple`, `dataclass`, `dataclasses`, `field`, `typing`

## Classes

`StrategyVariant`

## Functions / methods

`__annotate__`, `get_strategy`, `is_strategy_observable`

## Env-key candidates

`STRATEGIES`

## String constants (redacted where noted)

- '\nPAS143A — Strategy variant registry.\n\nEach StrategyVariant declares an `engine_overrides` dict that is\nshallow-merged into the brokerage config consumed by PASEngine\n(see PASEngine.__init__ for the keys it actually reads). Unrecognised\nkeys ride along as inert metadata so future engine knobs can be\ndeclared here ahead of the engine plumbing.\n\nRecognised brokerage keys today (from app/engine/state_machine.py):\n  - agent_name                 (str)   — appears verbatim in greeting\n  - ai_disclosure_enabled      (bool)  — toggles the recording line\n  - transfer_enabled           (bool)  — gates _is_transfer_request\n  - booking_enabled            (bool)  — gates _handle_booking\n  - max_objection_attempts     (int)   — when objection→DONE fires\n  - trained_booking_prompt     (str)   — replaces booking question\n  - trained_objection_prompt   (str)   — used by handle_objection LLM\n                                          (mocked in simulations, so this\n                                          override has no observable\n                                          effect at sim time)\n'
- 'agent_name'
- 'ai_disclosure_enabled'
- 'max_objection_attempts'
- 'StrategyVariant'
- 'direct_fast'
- 'Direct & fast'
- 'greeting'
- 'Brief identification, no preamble. Drops the AI disclosure to shorten the open.'
- 'Casey'
- 'warm_consultative'
- 'Warm consultative'
- 'Friendly tone with disclosure intact; aim is rapport before qualification.'
- 'Morgan'
- 'authoritative'
- 'Authoritative'
- 'Confident, agent-led posture. Discloses AI status to establish trust.'
- 'Director'
- 'hyper_brief'
- 'Hyper-brief'
- 'Tightest possible greeting; no name embellishment, no disclosure.'
- 'Alex'
- 'rebuttal_heavy'
- 'Rebuttal-heavy'
- 'objection'
- 'More objection attempts before bowing out — catches recoverable opposition.'
- 'trained_objection_prompt'
- 'Acknowledge briefly, then offer a concrete next step. Always end with a closed yes/no question.'
- 'consultative_redirect'
- 'Consultative redirect'
- 'Two attempts; uses a redirect-to-value prompt rather than a counter.'
- 'Acknowledge the concern, then redirect by asking what would be most useful for them right now.'
- 'curiosity_based'
- 'Curiosity-based'
- 'Two attempts; opens an open question to surface the underlying need.'
- "Respond with a single short, curious question that surfaces the lead's underlying concern. No selling language."
- 'soft_exit'
- 'Soft exit'
- 'Single attempt, then exit gracefully. Optimises for trust at the cost of conversion.'
- 'urgency_callback'
- 'Urgency callback'
- 'callback'
- 'Asks the lead to lock in a tight callback window. Metadata-only today.'
- 'urgent'
- 'callback_tone'
- 'flexible_callback'
- 'Flexible callback'
- 'Offers the lead any future time. Metadata-only today.'
- 'flexible'
- 'name'
- 'category'
- 'description'
- 'tags'
- 'engine_overrides'
- 'strategy'
- 'return'
- '\nReturns True iff at least one engine_overrides key is one PAS142\'s\nsimulation harness can actually exercise. Drives the report\'s\n`strategy_effective` flag and the recommendation that says "no\nstrategies are observable yet — rankings are infrastructure-only."\n'
- 'strategy_id'
- 'Lookup helper — returns None for unknown ids.'
- '_OBSERVABLE_KEYS'
- 'STRATEGIES'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C17F95E60, file "app\services\optimization\strategies.py", line 1>)
               MAKE_FUNCTION
               STORE_NAME              25 (__annotate__)
               BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               LOAD_CONST               0 ('\nPAS143A — Strategy variant registry.\n\nEach StrategyVariant declares an `engine_overrides` dict that is\nshallow-merged into the brokerage config consumed by PASEngine\n(see PASEngine.__init__ for the keys it actually reads). Unrecognised\nkeys ride along as inert metadata so future engine knobs can be\ndeclared here ahead of the engine plumbing.\n\nRecognised brokerage keys today (from app/engine/state_machine.py):\n  - agent_name                 (str)   — appears verbatim in greeting\n  - ai_disclosure_enabled      (bool)  — toggles the recording line\n  - transfer_enabled           (bool)  — gates _is_transfer_request\n  - booking_enabled            (bool)  — gates _handle_booking\n  - max_objection_attempts     (int)   — when objection→DONE fires\n  - trained_booking_prompt     (str)   — replaces booking question\n  - trained_objection_prompt   (str)   — used by handle_objection LLM\n                                          (mocked in simulations, so this\n                                          override has no observable\n                                          effect at sim time)\n')
               STORE_NAME               1 (__doc__)

  23           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('dataclass', 'field'))
               IMPORT_NAME              2 (dataclasses)
               IMPORT_FROM              3 (dataclass)
               STORE_NAME               3 (dataclass)
               IMPORT_FROM              4 (field)
               STORE_NAME               4 (field)
               POP_TOP

  24           LOAD_SMALL_INT           0
               LOAD_CONST               2 (('Dict', 'FrozenSet', 'Tuple'))
               IMPORT_NAME              5 (typing)
               IMPORT_FROM              6 (Dict)
               STORE_NAME               6 (Dict)
               IMPORT_FROM              7 (FrozenSet)
               STORE_NAME               7 (FrozenSet)
               IMPORT_FROM              8 (Tuple)
               STORE_NAME               8 (Tuple)
               POP_TOP

  31           LOAD_NAME                9 (frozenset)
               PUSH_NULL
               BUILD_SET                0
               LOAD_CONST              62 (frozenset({'agent_name', 'ai_disclosure_enabled', 'booking_enabled', 'transfer_enabled', 'max_objection_attempts', 'trained_booking_prompt'}))
               SET_UPDATE               1
               CALL                     1
               STORE_NAME              10 (_OBSERVABLE_KEYS)
               LOAD_NAME                0 (__conditional_annotations__)
               LOAD_SMALL_INT           0
               SET_ADD                  1
               POP_TOP

  41           LOAD_NAME                3 (dataclass)
               PUSH_NULL
               LOAD_CONST               6 (True)
               LOAD_CONST               7 (('frozen',))
               CALL_KW                  1

  42           LOAD_BUILD_CLASS
               PUSH_NULL
               LOAD_CONST               8 (<code object StrategyVariant at 0x0000018C18025D30, file "app\services\optimization\strategies.py", line 41>)
               MAKE_FUNCTION
               LOAD_CONST               9 ('StrategyVariant')
               CALL                     2

  41           CALL                     0

  42           STORE_NAME              11 (StrategyVariant)

  51           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C18025A30, file "app\services\optimization\strategies.py", line 51>)
               MAKE_FUNCTION
               LOAD_CONST              11 (<code object is_strategy_observable at 0x0000018C179C3A50, file "app\services\optimization\strategies.py", line 51>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              12 (is_strategy_observable)

  65           LOAD_NAME               11 (StrategyVariant)
               PUSH_NULL

  66           LOAD_CONST              12 ('direct_fast')

  67           LOAD_CONST              13 ('Direct & fast')

  68           LOAD_CONST              14 ('greeting')

  69           LOAD_CONST              15 ('Brief identification, no preamble. Drops the AI disclosure to shorten the open.')

  70           LOAD_CONST              63 (('greeting', 'brief'))

  72           LOAD_CONST               3 ('agent_name')
               LOAD_CONST              16 ('Casey')

  73           LOAD_CONST               4 ('ai_disclosure_enabled')
               LOAD_CONST              17 (False)

  71           BUILD_MAP                2

  65           LOAD_CONST              18 (('id', 'name', 'category', 'description', 'tags', 'engine_overrides'))
               CALL_KW                  6
               STORE_NAME              13 (_GREETING_DIRECT_FAST)

  77           LOAD_NAME               11 (StrategyVariant)
               PUSH_NULL

  78           LOAD_CONST              19 ('warm_consultative')

  79           LOAD_CONST              20 ('Warm consultative')

  80           LOAD_CONST              14 ('greeting')

  81           LOAD_CONST              21 ('Friendly tone with disclosure intact; aim is rapport before qualification.')

  82           LOAD_CONST              64 (('greeting', 'warm'))

  84           LOAD_CONST               3 ('agent_name')
               LOAD_CONST              22 ('Morgan')

  85           LOAD_CONST               4 ('ai_disclosure_enabled')
               LOAD_CONST               6 (True)

  83           BUILD_MAP                2

  77           LOAD_CONST              18 (('id', 'name', 'category', 'description', 'tags', 'engine_overrides'))
               CALL_KW                  6
               STORE_NAME              14 (_GREETING_WARM_CONSULTATIVE)

  89           LOAD_NAME               11 (StrategyVariant)
               PUSH_NULL

  90           LOAD_CONST              23 ('authoritative')

  91           LOAD_CONST              24 ('Authoritative')

  92           LOAD_CONST              14 ('greeting')

  93           LOAD_CONST              25 ('Confident, agent-led posture. Discloses AI status to establish trust.')

  94           LOAD_CONST              65 (('greeting', 'formal'))

  96           LOAD_CONST               3 ('agent_name')
               LOAD_CONST              26 ('Director')

  97           LOAD_CONST               4 ('ai_disclosure_enabled')
               LOAD_CONST               6 (True)

  95           BUILD_MAP                2

  89           LOAD_CONST              18 (('id', 'name', 'category', 'description', 'tags', 'engine_overrides'))
               CALL_KW                  6
               STORE_NAME              15 (_GREETING_AUTHORITATIVE)

 101           LOAD_NAME               11 (StrategyVariant)
               PUSH_NULL

 102           LOAD_CONST              27 ('hyper_brief')

 103           LOAD_CONST              28 ('Hyper-brief')

 104           LOAD_CONST              14 ('greeting')

 105           LOAD_CONST              29 ('Tightest possible greeting; no name embellishment, no disclosure.')

 106           LOAD_CONST              66 (('greeting', 'minimal'))

 108           LOAD_CONST               3 ('agent_name')
               LOAD_CONST              30 ('Alex')

 109           LOAD_CONST               4 ('ai_disclosure_enabled')
               LOAD_CONST              17 (False)

 107           BUILD_MAP                2

 101           LOAD_CONST              18 (('id', 'name', 'category', 'description', 'tags', 'engine_overrides'))
               CALL_KW                  6
               STORE_NAME              16 (_GREETING_HYPER_BRIEF)

 116           LOAD_NAME               11 (StrategyVariant)
               PUSH_NULL

 117           LOAD_CONST              31 ('rebuttal_heavy')

 118           LOAD_CONST              32 ('Rebuttal-heavy')

 119           LOAD_CONST              33 ('objection')

 120           LOAD_CONST              34 ('More objection attempts before bowing out — catches recoverable opposition.')

 121           LOAD_CONST              67 (('objection', 'persistent'))

 123           LOAD_CONST               5 ('max_objection_attempts')
               LOAD_SMALL_INT           3

 124           LOAD_CONST              35 ('trained_objection_prompt')

 125           LOAD_CONST              36 ('Acknowledge briefly, then offer a concrete next step. Always end with a closed yes/no question.')

 122           BUILD_MAP                2

 116           LOAD_CONST              18 (('id', 'name', 'category', 'description', 'tags', 'engine_overrides'))
               CALL_KW                  6
               STORE_NAME              17 (_OBJ_REBUTTAL_HEAVY)

 131           LOAD_NAME               11 (StrategyVariant)
               PUSH_NULL

 132           LOAD_CONST              37 ('consultative_redirect')

 133           LOAD_CONST              38 ('Consultative redirect')

 134           LOAD_CONST              33 ('objection')

 135           LOAD_CONST              39 ('Two attempts; uses a redirect-to-value prompt rather than a counter.')

 136           LOAD_CONST              68 (('objection', 'redirect'))

 138           LOAD_CONST               5 ('max_objection_attempts')
               LOAD_SMALL_INT           2

 139           LOAD_CONST              35 ('trained_objection_prompt')

 140           LOAD_CONST              40 ('Acknowledge the concern, then redirect by asking what would be most useful for them right now.')

 137           BUILD_MAP                2

 131           LOAD_CONST              18 (('id', 'name', 'category', 'description', 'tags', 'engine_overrides'))
               CALL_KW                  6
               STORE_NAME              18 (_OBJ_CONSULTATIVE_REDIRECT)

 146           LOAD_NAME               11 (StrategyVariant)
               PUSH_NULL

 147           LOAD_CONST              41 ('curiosity_based')

 148           LOAD_CONST              42 ('Curiosity-based')

 149           LOAD_CONST              33 ('objection')

 150           LOAD_CONST              43 ('Two attempts; opens an open question to surface the underlying need.')

 151           LOAD_CONST              69 (('objection', 'questioning'))

 153           LOAD_CONST               5 ('max_objection_attempts')
               LOAD_SMALL_INT           2

 154           LOAD_CONST              35 ('trained_objection_prompt')

 155           LOAD_CONST              44 ("Respond with a single short, curious question that surfaces the lead's underlying concern. No selling language.")

 152           BUILD_MAP                2

 146           LOAD_CONST              18 (('id', 'name', 'category', 'description', 'tags', 'engine_overrides'))
               CALL_KW                  6
               STORE_NAME              19 (_OBJ_CURIOSITY_BASED)

 161           LOAD_NAME               11 (StrategyVariant)
               PUSH_NULL

 162           LOAD_CONST              45 ('soft_exit')

 163           LOAD_CONST              46 ('Soft exit')

 164           LOAD_CONST              33 ('objection')

 165           LOAD_CONST              47 ('Single attempt, then exit gracefully. Optimises for trust at the cost of conversion.')

 166           LOAD_CONST              70 (('objection', 'conservative'))

 168           LOAD_CONST               5 ('max_objection_attempts')
               LOAD_SMALL_INT           1

 167           BUILD_MAP                1

 161           LOAD_CONST              18 (('id', 'name', 'category', 'description', 'tags', 'engine_overrides'))
               CALL_KW                  6
               STORE_NAME              20 (_OBJ_SOFT_EXIT)

 175           LOAD_NAME               11 (StrategyVariant)
               PUSH_NULL

 176           LOAD_CONST              48 ('urgency_callback')

 177           LOAD_CONST              49 ('Urgency callback')

 178           LOAD_CONST              50 ('callback')

 179           LOAD_CONST              51 ('Asks the lead to lock in a tight callback window. Metadata-only today.')

 180           LOAD_CONST              71 (('callback', 'urgent'))

 184           LOAD_CONST              53 ('callback_tone')
               LOAD_CONST              52 ('urgent')

 181           BUILD_MAP                1

 175           LOAD_CONST              18 (('id', 'name', 'category', 'description', 'tags', 'engine_overrides'))
               CALL_KW                  6
               STORE_NAME              21 (_CB_URGENCY_CALLBACK)

 188           LOAD_NAME               11 (StrategyVariant)
               PUSH_NULL

 189           LOAD_CONST              54 ('flexible_callback')

 190           LOAD_CONST              55 ('Flexible callback')

 191           LOAD_CONST              50 ('callback')

 192           LOAD_CONST              56 ('Offers the lead any future time. Metadata-only today.')

 193           LOAD_CONST              72 (('callback', 'flexible'))

 195           LOAD_CONST              53 ('callback_tone')
               LOAD_CONST              57 ('flexible')

 194           BUILD_MAP                1

 188           LOAD_CONST              18 (('id', 'name', 'category', 'description', 'tags', 'engine_overrides'))
               CALL_KW                  6
               STORE_NAME              22 (_CB_FLEXIBLE_CALLBACK)

 203           LOAD_NAME               13 (_GREETING_DIRECT_FAST)

 204           LOAD_NAME               14 (_GREETING_WARM_CONSULTATIVE)

 205           LOAD_NAME               15 (_GREETING_AUTHORITATIVE)

 206           LOAD_NAME               16 (_GREETING_HYPER_BRIEF)

 207           LOAD_NAME               17 (_OBJ_REBUTTAL_HEAVY)

 208           LOAD_NAME               18 (_OBJ_CONSULTATIVE_REDIRECT)

 209           LOAD_NAME               19 (_OBJ_CURIOSITY_BASED)

 210           LOAD_NAME               20 (_OBJ_SOFT_EXIT)

 211           LOAD_NAME               21 (_CB_URGENCY_CALLBACK)

 212           LOAD_NAME               22 (_CB_FLEXIBLE_CALLBACK)

 202           BUILD_TUPLE             10
               STORE_NAME              23 (STRATEGIES)
               LOAD_NAME                0 (__conditional_annotations__)
               LOAD_SMALL_INT           1
               SET_ADD                  1
               POP_TOP

 216           LOAD_CONST              58 (<code object __annotate__ at 0x0000018C18025130, file "app\services\optimization\strategies.py", line 216>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object get_strategy at 0x0000018C18053630, file "app\services\optimization\strategies.py", line 216>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              24 (get_strategy)
               LOAD_CONST              61 (None)
               RETURN_VALUE

Disassembly of <code object StrategyVariant at 0x0000018C18025D30, file "app\services\optimization\strategies.py", line 41>:
  --           MAKE_CELL                0 (__classdict__)

  41           RESUME                   0
               LOAD_NAME                0 (__name__)
               STORE_NAME               1 (__module__)
               LOAD_CONST               0 ('StrategyVariant')
               STORE_NAME               2 (__qualname__)
               LOAD_SMALL_INT          41
               STORE_NAME               3 (__firstlineno__)
               LOAD_LOCALS
               STORE_DEREF              0 (__classdict__)
               LOAD_FAST_BORROW         0 (__classdict__)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object __annotate__ at 0x0000018C17FE1920, file "app\services\optimization\strategies.py", line 41>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               STORE_NAME               4 (__annotate_func__)
               LOAD_CONST               2 (())
               STORE_NAME               5 (__static_attributes__)
               LOAD_FAST_BORROW         0 (__classdict__)
               STORE_NAME               6 (__classdictcell__)
               LOAD_CONST               3 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FE1920, file "app\services\optimization\strategies.py", line 41>:
  --           COPY_FREE_VARS           1

  41           RESUME                   0
               LOAD_FAST_BORROW         0 (format)
               LOAD_SMALL_INT           2
               COMPARE_OP             132 (>)
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN
               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
               RAISE_VARARGS            1
       L1:     BUILD_MAP                0

  43           LOAD_DEREF               1 (__classdict__)
               LOAD_FROM_DICT_OR_GLOBALS 0 (str)
               COPY                     2
               LOAD_CONST               1 ('id')

  41           STORE_SUBSCR

  44           LOAD_DEREF               1 (__classdict__)
               LOAD_FROM_DICT_OR_GLOBALS 0 (str)
               COPY                     2
               LOAD_CONST               2 ('name')

  41           STORE_SUBSCR

  45           LOAD_DEREF               1 (__classdict__)
               LOAD_FROM_DICT_OR_GLOBALS 0 (str)
               COPY                     2
               LOAD_CONST               3 ('category')

  41           STORE_SUBSCR

  46           LOAD_DEREF               1 (__classdict__)
               LOAD_FROM_DICT_OR_GLOBALS 0 (str)
               COPY                     2
               LOAD_CONST               4 ('description')

  41           STORE_SUBSCR

  47           LOAD_DEREF               1 (__classdict__)
               LOAD_FROM_DICT_OR_GLOBALS 1 (Tuple)
               LOAD_DEREF               1 (__classdict__)
               LOAD_FROM_DICT_OR_GLOBALS 0 (str)
               LOAD_CONST               5 (Ellipsis)
               BUILD_TUPLE              2
               BINARY_OP               26 ([])
               COPY                     2
               LOAD_CONST               6 ('tags')

  41           STORE_SUBSCR

  48           LOAD_DEREF               1 (__classdict__)
               LOAD_FROM_DICT_OR_GLOBALS 2 (Dict)
               COPY                     2
               LOAD_CONST               7 ('engine_overrides')

  41           STORE_SUBSCR
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app\services\optimization\strategies.py", line 51>:
 51           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('strategy')
              LOAD_CONST               2 ('StrategyVariant')
              LOAD_CONST               3 ('return')
              LOAD_GLOBAL              0 (bool)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object is_strategy_observable at 0x0000018C179C3A50, file "app\services\optimization\strategies.py", line 51>:
 51           RESUME                   0

 58           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (strategy)
              LOAD_ATTR                2 (engine_overrides)
              LOAD_GLOBAL              4 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 59           LOAD_CONST               1 (False)
              RETURN_VALUE

 60   L1:     LOAD_GLOBAL              6 (any)
              COPY                     1
              LOAD_COMMON_CONSTANT     4 (<built-in function any>)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE       52 (to L5)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 (<code object <genexpr> at 0x0000018C180E8030, file "app\services\optimization\strategies.py", line 60>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         0 (strategy)
              LOAD_ATTR                2 (engine_overrides)
              LOAD_ATTR                9 (keys + NULL|self)
              CALL                     0
              GET_ITER
              CALL                     0
      L2:     FOR_ITER                12 (to L4)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)
      L3:     POP_ITER
              LOAD_CONST               3 (True)
              RETURN_VALUE
      L4:     END_FOR
              POP_ITER
              LOAD_CONST               1 (False)
              RETURN_VALUE
      L5:     PUSH_NULL
              LOAD_CONST               2 (<code object <genexpr> at 0x0000018C180E8030, file "app\services\optimization\strategies.py", line 60>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         0 (strategy)
              LOAD_ATTR                2 (engine_overrides)
              LOAD_ATTR                9 (keys + NULL|self)
              CALL                     0
              GET_ITER
              CALL                     0
              CALL                     1
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180E8030, file "app\services\optimization\strategies.py", line 60>:
  60           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                13 (to L3)
               STORE_FAST_LOAD_FAST    17 (k, k)
               LOAD_GLOBAL              0 (_OBSERVABLE_KEYS)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           15 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "app\services\optimization\strategies.py", line 216>:
216           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('strategy_id')
              LOAD_GLOBAL              0 (str)
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object get_strategy at 0x0000018C18053630, file "app\services\optimization\strategies.py", line 216>:
216           RESUME                   0

218           LOAD_GLOBAL              0 (STRATEGIES)
              GET_ITER
      L1:     FOR_ITER                24 (to L3)
              STORE_FAST               1 (s)

219           LOAD_FAST_BORROW         1 (s)
              LOAD_ATTR                2 (id)
              LOAD_FAST_BORROW         0 (strategy_id)
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              JUMP_BACKWARD           22 (to L1)

220   L2:     LOAD_FAST_BORROW         1 (s)
              SWAP                     2
              POP_TOP
              RETURN_VALUE

218   L3:     END_FOR
              POP_ITER

221           LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17F95E60, file "app\services\optimization\strategies.py", line 1>:
  1           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     BUILD_MAP                0

 31           LOAD_SMALL_INT           0
              LOAD_GLOBAL              0 (__conditional_annotations__)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       21 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              2 (FrozenSet)
              LOAD_GLOBAL              4 (str)
              BINARY_OP               26 ([])
              COPY                     2
              LOAD_CONST               1 ('_OBSERVABLE_KEYS')

  1           STORE_SUBSCR

202   L2:     LOAD_SMALL_INT           1
              LOAD_GLOBAL              0 (__conditional_annotations__)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       23 (to L3)
              NOT_TAKEN
              LOAD_GLOBAL              6 (Tuple)
              LOAD_GLOBAL              8 (StrategyVariant)
              LOAD_CONST               2 (Ellipsis)
              BUILD_TUPLE              2
              BINARY_OP               26 ([])
              COPY                     2
              LOAD_CONST               3 ('STRATEGIES')

  1           STORE_SUBSCR
      L3:     RETURN_VALUE
```
