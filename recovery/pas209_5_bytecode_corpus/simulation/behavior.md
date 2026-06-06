# simulation/behavior

- **pyc:** `app\services\simulation\__pycache__\behavior.cpython-314.pyc`
- **expected source path (absent):** `app\services\simulation/behavior.py`
- **co_filename (from bytecode):** `app\services\simulation\behavior.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** simulation

## Module docstring

```
PAS143B — Behavioral divergence layer.

Pure deterministic functions only. No randomness, no I/O, no LLMs.
Same inputs always produce the same outputs — that property is the
core invariant of the optimization framework, and is asserted in
tests/simulation/test_behavior.py.

The module exposes three things:

  1. LeadPersonality dataclass + the PERSONALITIES registry.
  2. STRATEGY_TRAITS — implicit "style" of each PAS143A strategy.
  3. Two pure functions:
       advance_behavior_state(...)
       compute_behavioral_modifiers(...)

The simulation runner calls (3) on every lead-side turn. The
modifiers tell the runner whether the lead disengages, escalates,
declines at booking, or recovers — *deterministically* parameterised
by personality × strategy × conversation progression.
```

## Imports

`Dict`, `FrozenSet`, `Optional`, `Tuple`, `dataclass`, `dataclasses`, `typing`

## Classes

`LeadPersonality`

## Functions / methods

`__annotate__`, `advance_behavior_state`, `compute_behavioral_modifiers`, `get_personality`, `get_strategy_traits`

## Env-key candidates

`BEHAVIOR_STATES`, `BOOKING`, `ESCALATION_INJECTION_TEXT`, `PERSONALITIES`, `STRATEGY_TRAITS`, `TRIGGER_THRESHOLD`

## String constants (redacted where noted)

- '\nPAS143B — Behavioral divergence layer.\n\nPure deterministic functions only. No randomness, no I/O, no LLMs.\nSame inputs always produce the same outputs — that property is the\ncore invariant of the optimization framework, and is asserted in\ntests/simulation/test_behavior.py.\n\nThe module exposes three things:\n\n  1. LeadPersonality dataclass + the PERSONALITIES registry.\n  2. STRATEGY_TRAITS — implicit "style" of each PAS143A strategy.\n  3. Two pure functions:\n       advance_behavior_state(...)\n       compute_behavioral_modifiers(...)\n\nThe simulation runner calls (3) on every lead-side turn. The\nmodifiers tell the runner whether the lead disengages, escalates,\ndeclines at booking, or recovers — *deterministically* parameterised\nby personality × strategy × conversation progression.\n'
- 'skeptical'
- 'LeadPersonality'
- 'impatient'
- 'Impatient'
- 'Wants to wrap up. Punishes verbose / multi-turn flows.'
- 'Skeptical'
- 'Needs consultative rapport. Escalates under authoritative tone.'
- 'aggressive'
- 'Aggressive'
- 'Quick to push back. Persistent rebuttals make it worse.'
- 'analytical'
- 'Analytical'
- 'Methodical. Cooperates if the conversation feels structured.'
- 'emotional'
- 'Emotional'
- 'Tone-sensitive. Reacts to warmth or coldness more than content.'
- 'comparison_shopper'
- 'Comparison shopper'
- 'Asks about value. Closes only after consultative reassurance.'
- 'distrustful'
- 'Distrustful'
- 'Doubts intent. Authoritative tone backfires; consultative recovers.'
- 'busy'
- 'Busy'
- 'No time right now. Strongly prefers a callback to engagement.'
- 'motivated'
- 'Motivated'
- 'Ready to convert. Tolerates almost any reasonable strategy.'
- 'luxury_buyer'
- 'Luxury buyer'
- 'Expects formality. Hyper-brief or casual flows feel discounted.'
- 'direct_fast'
- 'brevity'
- 'formality'
- 'persistence'
- 'consultative'
- 'warmth'
- 'callback_friendly'
- 'warm_consultative'
- 'authoritative'
- 'hyper_brief'
- 'rebuttal_heavy'
- 'consultative_redirect'
- 'curiosity_based'
- 'soft_exit'
- 'urgency_callback'
- 'flexible_callback'
- 'engine_state'
- 'this is not working for me — please remove me from your list.'
- '\nAll trait values are floats in [0.0, 1.0]:\n  patience                  — tolerance for verbose / multi-turn flows\n  skepticism                — needs reassurance; distrusts authority\n  aggression                — quick to escalate when challenged\n  trust_threshold           — how much rapport is needed to convert\n  callback_preference       — leans toward "call me back" over engagement\n  escalation_sensitivity    — small triggers cause objections\n  qualification_cooperation — readily provides intent / budget / timeline\n'
- 'name'
- 'description'
- 'patience'
- 'skepticism'
- 'aggression'
- 'trust_threshold'
- 'callback_preference'
- 'escalation_sensitivity'
- 'qualification_cooperation'
- 'personality_id'
- 'return'
- 'strategy_id'
- 'current_state'
- 'lead_personality'
- 'event_type'
- 'objection_count'
- 'turn_count'
- '\nPure deterministic state transition.\n\nInputs:\n  current_state   — previous behavior state (one of BEHAVIOR_STATES)\n  strategy_id     — PAS143A strategy id (None ⇒ no signal)\n  lead_personality — LeadPersonality | None\n  event_type      — last engine event (e.g. "lead.uttered",\n                    "objection.detected", "lead.extracted",\n                    "callback.requested", "booking.attempted")\n  objection_count — total objections recorded for this call\n  turn_count      — 1-indexed lead turn we just processed\n\nReturns:\n  {\n    "next_state":         str,\n    "trust_delta":        float,   # signed — applied to trust score\n    "frustration_delta":  float,   # non-negative\n    "recovery_delta":     float,   # non-negative\n  }\n\nNever raises.\n'
- 'neutral'
- 'lead.uttered'
- 'warming'
- 'lead.extracted'
- 'engaged'
- 'objection.detected'
- 'frustrated'
- 'hostile'
- 'callback.requested'
- 'dropping'
- 'next_state'
- 'trust_delta'
- 'frustration_delta'
- 'recovery_delta'
- 'behavior_state'
- '\nPure deterministic action recommender.\n\nReturns four risk/bonus values in [0.0, 1.0]:\n\n  drop_risk            — lead disengages and stops responding\n  escalation_risk      — lead injects a hostile objection (terminating)\n  booking_failure_risk — lead refuses at booking (book_appointment fails)\n  recovery_bonus       — strategy "saves" a skeptical lead\n  qualification_bonus  — informational; lead provides extra qualifying data\n\nConvention: the runner treats >= 0.5 on drop / escalation / booking\nas "trigger". Lower values are observational only (still surfaced\nin the result dict via trust/frustration scores).\n\nNever raises. Returns all zeros when personality or strategy_id\nis unknown — i.e. no behavioural divergence applied (this is what\nPAS142 tests rely on for backwards compatibility).\n'
- 'drop_risk'
- 'escalation_risk'
- 'booking_failure_risk'
- 'recovery_bonus'
- 'qualification_bonus'
- 'BOOKING'
- 'BEHAVIOR_STATES'
- 'PERSONALITIES'
- 'STRATEGY_TRAITS'
- '_NEUTRAL_TRAITS'
- 'TRIGGER_THRESHOLD'
- 'ESCALATION_INJECTION_TEXT'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           LOAD_CONST              83 (<code object __annotate__ at 0x0000018C17CC2460, file "app\services\simulation\behavior.py", line 1>)
               MAKE_FUNCTION
               STORE_NAME              20 (__annotate__)
               BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               LOAD_CONST               0 ('\nPAS143B — Behavioral divergence layer.\n\nPure deterministic functions only. No randomness, no I/O, no LLMs.\nSame inputs always produce the same outputs — that property is the\ncore invariant of the optimization framework, and is asserted in\ntests/simulation/test_behavior.py.\n\nThe module exposes three things:\n\n  1. LeadPersonality dataclass + the PERSONALITIES registry.\n  2. STRATEGY_TRAITS — implicit "style" of each PAS143A strategy.\n  3. Two pure functions:\n       advance_behavior_state(...)\n       compute_behavioral_modifiers(...)\n\nThe simulation runner calls (3) on every lead-side turn. The\nmodifiers tell the runner whether the lead disengages, escalates,\ndeclines at booking, or recovers — *deterministically* parameterised\nby personality × strategy × conversation progression.\n')
               STORE_NAME               1 (__doc__)

  23           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('dataclass',))
               IMPORT_NAME              2 (dataclasses)
               IMPORT_FROM              3 (dataclass)
               STORE_NAME               3 (dataclass)
               POP_TOP

  24           LOAD_SMALL_INT           0
               LOAD_CONST               2 (('Dict', 'FrozenSet', 'Optional', 'Tuple'))
               IMPORT_NAME              4 (typing)
               IMPORT_FROM              5 (Dict)
               STORE_NAME               5 (Dict)
               IMPORT_FROM              6 (FrozenSet)
               STORE_NAME               6 (FrozenSet)
               IMPORT_FROM              7 (Optional)
               STORE_NAME               7 (Optional)
               IMPORT_FROM              8 (Tuple)
               STORE_NAME               8 (Tuple)
               POP_TOP

  34           LOAD_CONST              84 (('neutral', 'warming', 'engaged', 'skeptical', 'frustrated', 'hostile', 'dropping'))
               STORE_NAME               9 (BEHAVIOR_STATES)
               LOAD_NAME                0 (__conditional_annotations__)
               LOAD_SMALL_INT           0
               SET_ADD                  1
               POP_TOP

  45           LOAD_NAME                3 (dataclass)
               PUSH_NULL
               LOAD_CONST               4 (True)
               LOAD_CONST               5 (('frozen',))
               CALL_KW                  1

  46           LOAD_BUILD_CLASS
               PUSH_NULL
               LOAD_CONST               6 (<code object LeadPersonality at 0x0000018C18026430, file "app\services\simulation\behavior.py", line 45>)
               MAKE_FUNCTION
               LOAD_CONST               7 ('LeadPersonality')
               CALL                     2

  45           CALL                     0

  46           STORE_NAME              10 (LeadPersonality)

  70           LOAD_NAME               10 (LeadPersonality)
               PUSH_NULL

  71           LOAD_CONST               8 ('impatient')

  72           LOAD_CONST               9 ('Impatient')

  73           LOAD_CONST              10 ('Wants to wrap up. Punishes verbose / multi-turn flows.')

  74           LOAD_CONST              11 (0.15)

  75           LOAD_CONST              12 (0.3)

  76           LOAD_CONST              13 (0.4)

  77           LOAD_CONST              13 (0.4)

  78           LOAD_CONST              14 (0.2)

  79           LOAD_CONST              15 (0.5)

  80           LOAD_CONST              15 (0.5)

  70           LOAD_CONST              16 (('id', 'name', 'description', 'patience', 'skepticism', 'aggression', 'trust_threshold', 'callback_preference', 'escalation_sensitivity', 'qualification_cooperation'))
               CALL_KW                 10

  82           LOAD_NAME               10 (LeadPersonality)
               PUSH_NULL

  83           LOAD_CONST               3 ('skeptical')

  84           LOAD_CONST              17 ('Skeptical')

  85           LOAD_CONST              18 ('Needs consultative rapport. Escalates under authoritative tone.')

  86           LOAD_CONST              19 (0.6)

  87           LOAD_CONST              20 (0.85)

  88           LOAD_CONST              12 (0.3)

  89           LOAD_CONST              21 (0.8)

  90           LOAD_CONST              12 (0.3)

  91           LOAD_CONST              22 (0.55)

  92           LOAD_CONST              13 (0.4)

  82           LOAD_CONST              16 (('id', 'name', 'description', 'patience', 'skepticism', 'aggression', 'trust_threshold', 'callback_preference', 'escalation_sensitivity', 'qualification_cooperation'))
               CALL_KW                 10

  94           LOAD_NAME               10 (LeadPersonality)
               PUSH_NULL

  95           LOAD_CONST              23 ('aggressive')

  96           LOAD_CONST              24 ('Aggressive')

  97           LOAD_CONST              25 ('Quick to push back. Persistent rebuttals make it worse.')

  98           LOAD_CONST              12 (0.3)

  99           LOAD_CONST              15 (0.5)

 100           LOAD_CONST              20 (0.85)

 101           LOAD_CONST              22 (0.55)

 102           LOAD_CONST              14 (0.2)

 103           LOAD_CONST              20 (0.85)

 104           LOAD_CONST              26 (0.45)

  94           LOAD_CONST              16 (('id', 'name', 'description', 'patience', 'skepticism', 'aggression', 'trust_threshold', 'callback_preference', 'escalation_sensitivity', 'qualification_cooperation'))
               CALL_KW                 10

 106           LOAD_NAME               10 (LeadPersonality)
               PUSH_NULL

 107           LOAD_CONST              27 ('analytical')

 108           LOAD_CONST              28 ('Analytical')

 109           LOAD_CONST              29 ('Methodical. Cooperates if the conversation feels structured.')

 110           LOAD_CONST              30 (0.75)

 111           LOAD_CONST              22 (0.55)

 112           LOAD_CONST              31 (0.25)

 113           LOAD_CONST              19 (0.6)

 114           LOAD_CONST              32 (0.35)

 115           LOAD_CONST              12 (0.3)

 116           LOAD_CONST              21 (0.8)

 106           LOAD_CONST              16 (('id', 'name', 'description', 'patience', 'skepticism', 'aggression', 'trust_threshold', 'callback_preference', 'escalation_sensitivity', 'qualification_cooperation'))
               CALL_KW                 10

 118           LOAD_NAME               10 (LeadPersonality)
               PUSH_NULL

 119           LOAD_CONST              33 ('emotional')

 120           LOAD_CONST              34 ('Emotional')

 121           LOAD_CONST              35 ('Tone-sensitive. Reacts to warmth or coldness more than content.')

 122           LOAD_CONST              15 (0.5)

 123           LOAD_CONST              13 (0.4)

 124           LOAD_CONST              22 (0.55)

 125           LOAD_CONST              36 (0.65)

 126           LOAD_CONST              13 (0.4)

 127           LOAD_CONST              37 (0.7)

 128           LOAD_CONST              19 (0.6)

 118           LOAD_CONST              16 (('id', 'name', 'description', 'patience', 'skepticism', 'aggression', 'trust_threshold', 'callback_preference', 'escalation_sensitivity', 'qualification_cooperation'))
               CALL_KW                 10

 130           LOAD_NAME               10 (LeadPersonality)
               PUSH_NULL

 131           LOAD_CONST              38 ('comparison_shopper')

 132           LOAD_CONST              39 ('Comparison shopper')

 133           LOAD_CONST              40 ('Asks about value. Closes only after consultative reassurance.')

 134           LOAD_CONST              36 (0.65)

 135           LOAD_CONST              37 (0.7)

 136           LOAD_CONST              31 (0.25)

 137           LOAD_CONST              37 (0.7)

 138           LOAD_CONST              12 (0.3)

 139           LOAD_CONST              32 (0.35)

 140           LOAD_CONST              36 (0.65)

 130           LOAD_CONST              16 (('id', 'name', 'description', 'patience', 'skepticism', 'aggression', 'trust_threshold', 'callback_preference', 'escalation_sensitivity', 'qualification_cooperation'))
               CALL_KW                 10

 142           LOAD_NAME               10 (LeadPersonality)
               PUSH_NULL

 143           LOAD_CONST              41 ('distrustful')

 144           LOAD_CONST              42 ('Distrustful')

 145           LOAD_CONST              43 ('Doubts intent. Authoritative tone backfires; consultative recovers.')

 146           LOAD_CONST              26 (0.45)

 147           LOAD_CONST              21 (0.8)

 148           LOAD_CONST              26 (0.45)

 149           LOAD_CONST              20 (0.85)

 150           LOAD_CONST              13 (0.4)

 151           LOAD_CONST              36 (0.65)

 152           LOAD_CONST              13 (0.4)

 142           LOAD_CONST              16 (('id', 'name', 'description', 'patience', 'skepticism', 'aggression', 'trust_threshold', 'callback_preference', 'escalation_sensitivity', 'qualification_cooperation'))
               CALL_KW                 10

 154           LOAD_NAME               10 (LeadPersonality)
               PUSH_NULL

 155           LOAD_CONST              44 ('busy')

 156           LOAD_CONST              45 ('Busy')

 157           LOAD_CONST              46 ('No time right now. Strongly prefers a callback to engagement.')

 158           LOAD_CONST              14 (0.2)

 159           LOAD_CONST              12 (0.3)

 160           LOAD_CONST              12 (0.3)

 161           LOAD_CONST              13 (0.4)

 162           LOAD_CONST              20 (0.85)

 163           LOAD_CONST              13 (0.4)

 164           LOAD_CONST              22 (0.55)

 154           LOAD_CONST              16 (('id', 'name', 'description', 'patience', 'skepticism', 'aggression', 'trust_threshold', 'callback_preference', 'escalation_sensitivity', 'qualification_cooperation'))
               CALL_KW                 10

 166           LOAD_NAME               10 (LeadPersonality)
               PUSH_NULL

 167           LOAD_CONST              47 ('motivated')

 168           LOAD_CONST              48 ('Motivated')

 169           LOAD_CONST              49 ('Ready to convert. Tolerates almost any reasonable strategy.')

 170           LOAD_CONST              20 (0.85)

 171           LOAD_CONST              31 (0.25)

 172           LOAD_CONST              14 (0.2)

 173           LOAD_CONST              12 (0.3)

 174           LOAD_CONST              14 (0.2)

 175           LOAD_CONST              14 (0.2)

 176           LOAD_CONST              50 (0.9)

 166           LOAD_CONST              16 (('id', 'name', 'description', 'patience', 'skepticism', 'aggression', 'trust_threshold', 'callback_preference', 'escalation_sensitivity', 'qualification_cooperation'))
               CALL_KW                 10

 178           LOAD_NAME               10 (LeadPersonality)
               PUSH_NULL

 179           LOAD_CONST              51 ('luxury_buyer')

 180           LOAD_CONST              52 ('Luxury buyer')

 181           LOAD_CONST              53 ('Expects formality. Hyper-brief or casual flows feel discounted.')

 182           LOAD_CONST              37 (0.7)

 183           LOAD_CONST              22 (0.55)

 184           LOAD_CONST              14 (0.2)

 185           LOAD_CONST              36 (0.65)

 186           LOAD_CONST              12 (0.3)

 187           LOAD_CONST              13 (0.4)

 188           LOAD_CONST              37 (0.7)

 178           LOAD_CONST              16 (('id', 'name', 'description', 'patience', 'skepticism', 'aggression', 'trust_threshold', 'callback_preference', 'escalation_sensitivity', 'qualification_cooperation'))
               CALL_KW                 10

  69           BUILD_TUPLE             10
               STORE_NAME              11 (PERSONALITIES)
               LOAD_NAME                0 (__conditional_annotations__)
               LOAD_SMALL_INT           1
               SET_ADD                  1
               POP_TOP

 193           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C17C49B80, file "app\services\simulation\behavior.py", line 193>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object get_personality at 0x0000018C1802CC10, file "app\services\simulation\behavior.py", line 193>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              12 (get_personality)

 219           LOAD_CONST              56 ('direct_fast')
               LOAD_CONST              57 ('brevity')
               LOAD_CONST              20 (0.85)
               LOAD_CONST              58 ('formality')
               LOAD_CONST              13 (0.4)
               LOAD_CONST              59 ('persistence')
               LOAD_CONST              22 (0.55)

 220           LOAD_CONST              60 ('consultative')
               LOAD_CONST              14 (0.2)
               LOAD_CONST              61 ('warmth')
               LOAD_CONST              32 (0.35)
               LOAD_CONST              62 ('callback_friendly')
               LOAD_CONST              14 (0.2)

 219           BUILD_MAP                6

 221           LOAD_CONST              63 ('warm_consultative')
               LOAD_CONST              57 ('brevity')
               LOAD_CONST              14 (0.2)
               LOAD_CONST              58 ('formality')
               LOAD_CONST              13 (0.4)
               LOAD_CONST              59 ('persistence')
               LOAD_CONST              22 (0.55)

 222           LOAD_CONST              60 ('consultative')
               LOAD_CONST              20 (0.85)
               LOAD_CONST              61 ('warmth')
               LOAD_CONST              20 (0.85)
               LOAD_CONST              62 ('callback_friendly')
               LOAD_CONST              32 (0.35)

 221           BUILD_MAP                6

 223           LOAD_CONST              64 ('authoritative')
               LOAD_CONST              57 ('brevity')
               LOAD_CONST              15 (0.5)
               LOAD_CONST              58 ('formality')
               LOAD_CONST              50 (0.9)
               LOAD_CONST              59 ('persistence')
               LOAD_CONST              30 (0.75)

 224           LOAD_CONST              60 ('consultative')
               LOAD_CONST              14 (0.2)
               LOAD_CONST              61 ('warmth')
               LOAD_CONST              14 (0.2)
               LOAD_CONST              62 ('callback_friendly')
               LOAD_CONST              14 (0.2)

 223           BUILD_MAP                6

 225           LOAD_CONST              65 ('hyper_brief')
               LOAD_CONST              57 ('brevity')
               LOAD_CONST              66 (0.95)
               LOAD_CONST              58 ('formality')
               LOAD_CONST              12 (0.3)
               LOAD_CONST              59 ('persistence')
               LOAD_CONST              13 (0.4)

 226           LOAD_CONST              60 ('consultative')
               LOAD_CONST              67 (0.1)
               LOAD_CONST              61 ('warmth')
               LOAD_CONST              12 (0.3)
               LOAD_CONST              62 ('callback_friendly')
               LOAD_CONST              14 (0.2)

 225           BUILD_MAP                6

 227           LOAD_CONST              68 ('rebuttal_heavy')
               LOAD_CONST              57 ('brevity')
               LOAD_CONST              32 (0.35)
               LOAD_CONST              58 ('formality')
               LOAD_CONST              22 (0.55)
               LOAD_CONST              59 ('persistence')
               LOAD_CONST              66 (0.95)

 228           LOAD_CONST              60 ('consultative')
               LOAD_CONST              11 (0.15)
               LOAD_CONST              61 ('warmth')
               LOAD_CONST              12 (0.3)
               LOAD_CONST              62 ('callback_friendly')
               LOAD_CONST              67 (0.1)

 227           BUILD_MAP                6

 229           LOAD_CONST              69 ('consultative_redirect')
               LOAD_CONST              57 ('brevity')
               LOAD_CONST              13 (0.4)
               LOAD_CONST              58 ('formality')
               LOAD_CONST              13 (0.4)
               LOAD_CONST              59 ('persistence')
               LOAD_CONST              15 (0.5)

 230           LOAD_CONST              60 ('consultative')
               LOAD_CONST              50 (0.9)
               LOAD_CONST              61 ('warmth')
               LOAD_CONST              36 (0.65)
               LOAD_CONST              62 ('callback_friendly')
               LOAD_CONST              12 (0.3)

 229           BUILD_MAP                6

 231           LOAD_CONST              70 ('curiosity_based')
               LOAD_CONST              57 ('brevity')
               LOAD_CONST              22 (0.55)
               LOAD_CONST              58 ('formality')
               LOAD_CONST              32 (0.35)
               LOAD_CONST              59 ('persistence')
               LOAD_CONST              26 (0.45)

 232           LOAD_CONST              60 ('consultative')
               LOAD_CONST              20 (0.85)
               LOAD_CONST              61 ('warmth')
               LOAD_CONST              22 (0.55)
               LOAD_CONST              62 ('callback_friendly')
               LOAD_CONST              31 (0.25)

 231           BUILD_MAP                6

 233           LOAD_CONST              71 ('soft_exit')
               LOAD_CONST              57 ('brevity')
               LOAD_CONST              36 (0.65)
               LOAD_CONST              58 ('formality')
               LOAD_CONST              13 (0.4)
               LOAD_CONST              59 ('persistence')
               LOAD_CONST              67 (0.1)

 234           LOAD_CONST              60 ('consultative')
               LOAD_CONST              13 (0.4)
               LOAD_CONST              61 ('warmth')
               LOAD_CONST              22 (0.55)
               LOAD_CONST              62 ('callback_friendly')
               LOAD_CONST              12 (0.3)

 233           BUILD_MAP                6

 235           LOAD_CONST              72 ('urgency_callback')
               LOAD_CONST              57 ('brevity')
               LOAD_CONST              22 (0.55)
               LOAD_CONST              58 ('formality')
               LOAD_CONST              15 (0.5)
               LOAD_CONST              59 ('persistence')
               LOAD_CONST              15 (0.5)

 236           LOAD_CONST              60 ('consultative')
               LOAD_CONST              12 (0.3)
               LOAD_CONST              61 ('warmth')
               LOAD_CONST              13 (0.4)
               LOAD_CONST              62 ('callback_friendly')
               LOAD_CONST              66 (0.95)

 235           BUILD_MAP                6

 237           LOAD_CONST              73 ('flexible_callback')
               LOAD_CONST              57 ('brevity')
               LOAD_CONST              22 (0.55)
               LOAD_CONST              58 ('formality')
               LOAD_CONST              13 (0.4)
               LOAD_CONST              59 ('persistence')
               LOAD_CONST              26 (0.45)

 238           LOAD_CONST              60 ('consultative')
               LOAD_CONST              26 (0.45)
               LOAD_CONST              61 ('warmth')
               LOAD_CONST              36 (0.65)
               LOAD_CONST              62 ('callback_friendly')
               LOAD_CONST              66 (0.95)

 237           BUILD_MAP                6

 218           BUILD_MAP               10
               STORE_NAME              13 (STRATEGY_TRAITS)
               LOAD_NAME                0 (__conditional_annotations__)
               LOAD_SMALL_INT           2
               SET_ADD                  1
               POP_TOP

 244           LOAD_CONST              57 ('brevity')
               LOAD_CONST              15 (0.5)
               LOAD_CONST              58 ('formality')
               LOAD_CONST              15 (0.5)
               LOAD_CONST              59 ('persistence')
               LOAD_CONST              15 (0.5)

 245           LOAD_CONST              60 ('consultative')
               LOAD_CONST              15 (0.5)
               LOAD_CONST              61 ('warmth')
               LOAD_CONST              15 (0.5)
               LOAD_CONST              62 ('callback_friendly')
               LOAD_CONST              15 (0.5)

 243           BUILD_MAP                6
               STORE_NAME              14 (_NEUTRAL_TRAITS)
               LOAD_NAME                0 (__conditional_annotations__)
               LOAD_SMALL_INT           3
               SET_ADD                  1
               POP_TOP

 249           LOAD_CONST              74 (<code object __annotate__ at 0x0000018C180392F0, file "app\services\simulation\behavior.py", line 249>)
               MAKE_FUNCTION
               LOAD_CONST              75 (<code object get_strategy_traits at 0x0000018C17FE1680, file "app\services\simulation\behavior.py", line 249>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              15 (get_strategy_traits)

 259           LOAD_CONST              76 (<code object __annotate__ at 0x0000018C17F95E60, file "app\services\simulation\behavior.py", line 259>)
               MAKE_FUNCTION
               LOAD_CONST              77 (<code object advance_behavior_state at 0x0000018C17ED9FB0, file "app\services\simulation\behavior.py", line 259>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              16 (advance_behavior_state)

 396           LOAD_CONST              78 ('engine_state')

 403           LOAD_CONST              79 (None)

 396           BUILD_MAP                1
               LOAD_CONST              80 (<code object __annotate__ at 0x0000018C17FF1230, file "app\services\simulation\behavior.py", line 396>)
               MAKE_FUNCTION
               LOAD_CONST              81 (<code object compute_behavioral_modifiers at 0x0000018C18248570, file "app\services\simulation\behavior.py", line 396>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              17 (compute_behavioral_modifiers)

 508           LOAD_CONST              15 (0.5)
               STORE_NAME              18 (TRIGGER_THRESHOLD)
               LOAD_NAME                0 (__conditional_annotations__)
               LOAD_SMALL_INT           4
               SET_ADD                  1
               POP_TOP

 516           LOAD_CONST              82 ('this is not working for me — please remove me from your list.')

 515           STORE_NAME              19 (ESCALATION_INJECTION_TEXT)
               LOAD_NAME                0 (__conditional_annotations__)
               LOAD_SMALL_INT           5
               SET_ADD                  1
               POP_TOP
               LOAD_CONST              79 (None)
               RETURN_VALUE

Disassembly of <code object LeadPersonality at 0x0000018C18026430, file "app\services\simulation\behavior.py", line 45>:
  --           MAKE_CELL                0 (__classdict__)

  45           RESUME                   0
               LOAD_NAME                0 (__name__)
               STORE_NAME               1 (__module__)
               LOAD_CONST               0 ('LeadPersonality')
               STORE_NAME               2 (__qualname__)
               LOAD_SMALL_INT          45
               STORE_NAME               3 (__firstlineno__)
               LOAD_LOCALS
               STORE_DEREF              0 (__classdict__)

  47           LOAD_CONST               1 ('\nAll trait values are floats in [0.0, 1.0]:\n  patience                  — tolerance for verbose / multi-turn flows\n  skepticism                — needs reassurance; distrusts authority\n  aggression                — quick to escalate when challenged\n  trust_threshold           — how much rapport is needed to convert\n  callback_preference       — leans toward "call me back" over engagement\n  escalation_sensitivity    — small triggers cause objections\n  qualification_cooperation — readily provides intent / budget / timeline\n')
               STORE_NAME               4 (__doc__)

  45           LOAD_FAST_BORROW         0 (__classdict__)
               BUILD_TUPLE              1
               LOAD_CONST               2 (<code object __annotate__ at 0x0000018C17F96140, file "app\services\simulation\behavior.py", line 45>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               STORE_NAME               5 (__annotate_func__)
               LOAD_CONST               3 (())
               STORE_NAME               6 (__static_attributes__)
               LOAD_FAST_BORROW         0 (__classdict__)
               STORE_NAME               7 (__classdictcell__)
               LOAD_CONST               4 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17F96140, file "app\services\simulation\behavior.py", line 45>:
  --           COPY_FREE_VARS           1

  45           RESUME                   0
               LOAD_FAST_BORROW         0 (format)
               LOAD_SMALL_INT           2
               COMPARE_OP             132 (>)
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN
               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
               RAISE_VARARGS            1
       L1:     BUILD_MAP                0

  57           LOAD_DEREF               1 (__classdict__)
               LOAD_FROM_DICT_OR_GLOBALS 0 (str)
               COPY                     2
               LOAD_CONST               1 ('id')

  45           STORE_SUBSCR

  58           LOAD_DEREF               1 (__classdict__)
               LOAD_FROM_DICT_OR_GLOBALS 0 (str)
               COPY                     2
               LOAD_CONST               2 ('name')

  45           STORE_SUBSCR

  59           LOAD_DEREF               1 (__classdict__)
               LOAD_FROM_DICT_OR_GLOBALS 0 (str)
               COPY                     2
               LOAD_CONST               3 ('description')

  45           STORE_SUBSCR

  60           LOAD_DEREF               1 (__classdict__)
               LOAD_FROM_DICT_OR_GLOBALS 1 (float)
               COPY                     2
               LOAD_CONST               4 ('patience')

  45           STORE_SUBSCR

  61           LOAD_DEREF               1 (__classdict__)
               LOAD_FROM_DICT_OR_GLOBALS 1 (float)
               COPY                     2
               LOAD_CONST               5 ('skepticism')

  45           STORE_SUBSCR

  62           LOAD_DEREF               1 (__classdict__)
               LOAD_FROM_DICT_OR_GLOBALS 1 (float)
               COPY                     2
               LOAD_CONST               6 ('aggression')

  45           STORE_SUBSCR

  63           LOAD_DEREF               1 (__classdict__)
               LOAD_FROM_DICT_OR_GLOBALS 1 (float)
               COPY                     2
               LOAD_CONST               7 ('trust_threshold')

  45           STORE_SUBSCR

  64           LOAD_DEREF               1 (__classdict__)
               LOAD_FROM_DICT_OR_GLOBALS 1 (float)
               COPY                     2
               LOAD_CONST               8 ('callback_preference')

  45           STORE_SUBSCR

  65           LOAD_DEREF               1 (__classdict__)
               LOAD_FROM_DICT_OR_GLOBALS 1 (float)
               COPY                     2
               LOAD_CONST               9 ('escalation_sensitivity')

  45           STORE_SUBSCR

  66           LOAD_DEREF               1 (__classdict__)
               LOAD_FROM_DICT_OR_GLOBALS 1 (float)
               COPY                     2
               LOAD_CONST              10 ('qualification_cooperation')

  45           STORE_SUBSCR
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17C49B80, file "app\services\simulation\behavior.py", line 193>:
193           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('personality_id')
              LOAD_GLOBAL              0 (Optional)
              LOAD_GLOBAL              2 (str)
              BINARY_OP               26 ([])
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              0 (Optional)
              LOAD_GLOBAL              4 (LeadPersonality)
              BINARY_OP               26 ([])
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object get_personality at 0x0000018C1802CC10, file "app\services\simulation\behavior.py", line 193>:
193           RESUME                   0

194           LOAD_FAST_BORROW         0 (personality_id)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

195           LOAD_CONST               0 (None)
              RETURN_VALUE

196   L1:     LOAD_GLOBAL              0 (PERSONALITIES)
              GET_ITER
      L2:     FOR_ITER                24 (to L4)
              STORE_FAST               1 (p)

197           LOAD_FAST_BORROW         1 (p)
              LOAD_ATTR                2 (id)
              LOAD_FAST_BORROW         0 (personality_id)
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           22 (to L2)

198   L3:     LOAD_FAST_BORROW         1 (p)
              SWAP                     2
              POP_TOP
              RETURN_VALUE

196   L4:     END_FOR
              POP_ITER

199           LOAD_CONST               0 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180392F0, file "app\services\simulation\behavior.py", line 249>:
249           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('strategy_id')
              LOAD_GLOBAL              0 (Optional)
              LOAD_GLOBAL              2 (str)
              BINARY_OP               26 ([])
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              4 (Dict)
              LOAD_GLOBAL              2 (str)
              LOAD_GLOBAL              6 (float)
              BUILD_TUPLE              2
              BINARY_OP               26 ([])
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object get_strategy_traits at 0x0000018C17FE1680, file "app\services\simulation\behavior.py", line 249>:
249           RESUME                   0

250           LOAD_FAST_BORROW         0 (strategy_id)
              TO_BOOL
              POP_JUMP_IF_TRUE        16 (to L1)
              NOT_TAKEN

251           LOAD_GLOBAL              1 (dict + NULL)
              LOAD_GLOBAL              2 (_NEUTRAL_TRAITS)
              CALL                     1
              RETURN_VALUE

252   L1:     LOAD_GLOBAL              1 (dict + NULL)
              LOAD_GLOBAL              4 (STRATEGY_TRAITS)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_FAST_BORROW         0 (strategy_id)
              LOAD_GLOBAL              2 (_NEUTRAL_TRAITS)
              CALL                     2
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17F95E60, file "app\services\simulation\behavior.py", line 259>:
259           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('current_state')

261           LOAD_GLOBAL              0 (str)

259           LOAD_CONST               2 ('strategy_id')

262           LOAD_GLOBAL              2 (Optional)
              LOAD_GLOBAL              0 (str)
              BINARY_OP               26 ([])

259           LOAD_CONST               3 ('lead_personality')

263           LOAD_GLOBAL              2 (Optional)
              LOAD_GLOBAL              4 (LeadPersonality)
              BINARY_OP               26 ([])

259           LOAD_CONST               4 ('event_type')

264           LOAD_GLOBAL              0 (str)

259           LOAD_CONST               5 ('objection_count')

265           LOAD_GLOBAL              6 (int)

259           LOAD_CONST               6 ('turn_count')

266           LOAD_GLOBAL              6 (int)

259           LOAD_CONST               7 ('return')

267           LOAD_GLOBAL              8 (dict)

259           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object advance_behavior_state at 0x0000018C17ED9FB0, file "app\services\simulation\behavior.py", line 259>:
259            RESUME                   0

291            LOAD_FAST_BORROW         0 (current_state)
               LOAD_GLOBAL              0 (BEHAVIOR_STATES)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN
               LOAD_FAST                0 (current_state)
               JUMP_FORWARD             1 (to L2)
       L1:     LOAD_CONST               1 ('neutral')
       L2:     STORE_FAST               6 (next_state)

292            LOAD_CONST               2 (0.0)
               STORE_FAST               7 (trust_delta)

293            LOAD_CONST               2 (0.0)
               STORE_FAST               8 (frustration_delta)

294            LOAD_CONST               2 (0.0)
               STORE_FAST               9 (recovery_delta)

296            LOAD_FAST                2 (lead_personality)
               STORE_FAST              10 (p)

297            LOAD_GLOBAL              3 (get_strategy_traits + NULL)
               LOAD_FAST_BORROW         1 (strategy_id)
               CALL                     1
               STORE_FAST              11 (s)

300            LOAD_FAST_BORROW         5 (turn_count)
               LOAD_SMALL_INT           1
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE       76 (to L5)
               NOT_TAKEN
               LOAD_FAST_BORROW         3 (event_type)
               LOAD_CONST               3 ('lead.uttered')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       69 (to L5)
               NOT_TAKEN

301            LOAD_FAST_BORROW        10 (p)
               POP_JUMP_IF_NONE        30 (to L3)
               NOT_TAKEN
               LOAD_FAST_BORROW        10 (p)
               LOAD_ATTR                4 (aggression)
               LOAD_CONST               4 (0.7)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       13 (to L3)
               NOT_TAKEN

302            LOAD_CONST               5 ('skeptical')
               STORE_FAST               6 (next_state)

303            LOAD_FAST_BORROW         7 (trust_delta)
               LOAD_CONST               6 (0.05)
               BINARY_OP               23 (-=)
               STORE_FAST               7 (trust_delta)
               JUMP_FORWARD            35 (to L5)

304    L3:     LOAD_FAST_BORROW        10 (p)
               POP_JUMP_IF_NONE        21 (to L4)
               NOT_TAKEN
               LOAD_FAST_BORROW        10 (p)
               LOAD_ATTR                6 (skepticism)
               LOAD_CONST               4 (0.7)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE        4 (to L4)
               NOT_TAKEN

305            LOAD_CONST               5 ('skeptical')
               STORE_FAST               6 (next_state)
               JUMP_FORWARD            11 (to L5)

307    L4:     LOAD_CONST               7 ('warming')
               STORE_FAST               6 (next_state)

308            LOAD_FAST_BORROW         7 (trust_delta)
               LOAD_CONST               6 (0.05)
               BINARY_OP               13 (+=)
               STORE_FAST               7 (trust_delta)

311    L5:     LOAD_FAST_BORROW         3 (event_type)
               LOAD_CONST               8 ('lead.extracted')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       19 (to L6)
               NOT_TAKEN

312            LOAD_FAST_BORROW         7 (trust_delta)
               LOAD_CONST               9 (0.1)
               BINARY_OP               13 (+=)
               STORE_FAST               7 (trust_delta)

313            LOAD_FAST_BORROW         6 (next_state)
               LOAD_CONST              32 (('neutral', 'warming'))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN

314            LOAD_CONST              10 ('engaged')
               STORE_FAST               6 (next_state)

317    L6:     LOAD_FAST_BORROW         3 (event_type)
               LOAD_CONST              11 ('objection.detected')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       48 (to L10)
               NOT_TAKEN

318            LOAD_FAST_BORROW         8 (frustration_delta)
               LOAD_CONST              12 (0.2)
               BINARY_OP               13 (+=)
               STORE_FAST               8 (frustration_delta)

319            LOAD_FAST_BORROW         6 (next_state)
               LOAD_CONST              33 (('warming', 'engaged', 'neutral'))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        4 (to L7)
               NOT_TAKEN

320            LOAD_CONST               5 ('skeptical')
               STORE_FAST               6 (next_state)
               JUMP_FORWARD            19 (to L9)

321    L7:     LOAD_FAST_BORROW         6 (next_state)
               LOAD_CONST               5 ('skeptical')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        4 (to L8)
               NOT_TAKEN

322            LOAD_CONST              13 ('frustrated')
               STORE_FAST               6 (next_state)
               JUMP_FORWARD             9 (to L9)

323    L8:     LOAD_FAST_BORROW         6 (next_state)
               LOAD_CONST              13 ('frustrated')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN

324            LOAD_CONST              14 ('hostile')
               STORE_FAST               6 (next_state)

325    L9:     LOAD_FAST_BORROW         4 (objection_count)
               LOAD_SMALL_INT           2
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN

326            LOAD_CONST              14 ('hostile')
               STORE_FAST               6 (next_state)

329   L10:     LOAD_FAST_BORROW         3 (event_type)
               LOAD_CONST              15 ('callback.requested')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       36 (to L12)
               NOT_TAKEN

333            LOAD_FAST_BORROW        10 (p)
               POP_JUMP_IF_NONE        30 (to L11)
               NOT_TAKEN
               LOAD_FAST_BORROW        10 (p)
               LOAD_ATTR                8 (callback_preference)
               LOAD_CONST              16 (0.6)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       13 (to L11)
               NOT_TAKEN

334            LOAD_CONST              10 ('engaged')
               STORE_FAST               6 (next_state)

335            LOAD_FAST_BORROW         7 (trust_delta)
               LOAD_CONST               6 (0.05)
               BINARY_OP               13 (+=)
               STORE_FAST               7 (trust_delta)
               JUMP_FORWARD             2 (to L12)

337   L11:     LOAD_CONST               7 ('warming')
               STORE_FAST               6 (next_state)

342   L12:     LOAD_FAST_BORROW        11 (s)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_CONST              17 ('consultative')
               LOAD_CONST              18 (0.5)
               CALL                     2
               LOAD_CONST               4 (0.7)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       49 (to L13)
               NOT_TAKEN

343            LOAD_FAST_BORROW        10 (p)
               POP_JUMP_IF_NONE        45 (to L13)
               NOT_TAKEN

344            LOAD_FAST_BORROW        10 (p)
               LOAD_ATTR                6 (skepticism)
               LOAD_CONST              16 (0.6)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       28 (to L13)
               NOT_TAKEN

345            LOAD_FAST_BORROW         6 (next_state)
               LOAD_CONST              34 (('skeptical', 'frustrated'))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       21 (to L13)
               NOT_TAKEN

347            LOAD_FAST_BORROW         9 (recovery_delta)
               LOAD_CONST              19 (0.15)
               BINARY_OP               13 (+=)
               STORE_FAST               9 (recovery_delta)

348            LOAD_FAST_BORROW         7 (trust_delta)
               LOAD_CONST               6 (0.05)
               BINARY_OP               13 (+=)
               STORE_FAST               7 (trust_delta)

349            LOAD_CONST              10 ('engaged')
               STORE_FAST               6 (next_state)

353   L13:     LOAD_FAST_BORROW        11 (s)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_CONST              20 ('formality')
               LOAD_CONST              18 (0.5)
               CALL                     2
               LOAD_CONST              21 (0.8)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       47 (to L14)
               NOT_TAKEN

354            LOAD_FAST_BORROW        10 (p)
               POP_JUMP_IF_NONE        43 (to L14)
               NOT_TAKEN

355            LOAD_FAST_BORROW        10 (p)
               LOAD_ATTR                6 (skepticism)
               LOAD_CONST               4 (0.7)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       26 (to L14)
               NOT_TAKEN

356            LOAD_FAST_BORROW         3 (event_type)
               LOAD_CONST               3 ('lead.uttered')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       19 (to L14)
               NOT_TAKEN

358            LOAD_FAST_BORROW         8 (frustration_delta)
               LOAD_CONST               9 (0.1)
               BINARY_OP               13 (+=)
               STORE_FAST               8 (frustration_delta)

359            LOAD_FAST_BORROW         6 (next_state)
               LOAD_CONST              10 ('engaged')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        3 (to L14)
               NOT_TAKEN

360            LOAD_CONST               5 ('skeptical')
               STORE_FAST               6 (next_state)

364   L14:     LOAD_FAST_BORROW        11 (s)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_CONST              22 ('brevity')
               LOAD_CONST              18 (0.5)
               CALL                     2
               LOAD_CONST              23 (0.3)
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE       47 (to L15)
               NOT_TAKEN

365            LOAD_FAST_BORROW        10 (p)
               POP_JUMP_IF_NONE        43 (to L15)
               NOT_TAKEN

366            LOAD_FAST_BORROW        10 (p)
               LOAD_ATTR               12 (patience)
               LOAD_CONST              23 (0.3)
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE       26 (to L15)
               NOT_TAKEN

367            LOAD_FAST_BORROW         3 (event_type)
               LOAD_CONST               3 ('lead.uttered')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       19 (to L15)
               NOT_TAKEN

369            LOAD_FAST_BORROW         8 (frustration_delta)
               LOAD_CONST              19 (0.15)
               BINARY_OP               13 (+=)
               STORE_FAST               8 (frustration_delta)

370            LOAD_FAST_BORROW         6 (next_state)
               LOAD_CONST              35 (('warming', 'engaged'))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L15)
               NOT_TAKEN

371            LOAD_CONST               5 ('skeptical')
               STORE_FAST               6 (next_state)

375   L15:     LOAD_FAST_BORROW        11 (s)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_CONST              24 ('persistence')
               LOAD_CONST              18 (0.5)
               CALL                     2
               LOAD_CONST              25 (0.85)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       38 (to L16)
               NOT_TAKEN

376            LOAD_FAST_BORROW        10 (p)
               POP_JUMP_IF_NONE        34 (to L16)
               NOT_TAKEN

377            LOAD_FAST_BORROW        10 (p)
               LOAD_ATTR                4 (aggression)
               LOAD_CONST               4 (0.7)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       17 (to L16)
               NOT_TAKEN

378            LOAD_FAST_BORROW         3 (event_type)
               LOAD_CONST              36 (('objection.detected', 'lead.uttered'))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       10 (to L16)
               NOT_TAKEN

380            LOAD_FAST_BORROW         8 (frustration_delta)
               LOAD_CONST               9 (0.1)
               BINARY_OP               13 (+=)
               STORE_FAST               8 (frustration_delta)

383   L16:     LOAD_FAST_LOAD_FAST    134 (frustration_delta, next_state)
               LOAD_CONST              14 ('hostile')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        3 (to L17)
               NOT_TAKEN
               LOAD_CONST              12 (0.2)
               JUMP_FORWARD             1 (to L18)
      L17:     LOAD_CONST               2 (0.0)
      L18:     BINARY_OP                0 (+)
               LOAD_CONST              23 (0.3)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       31 (to L19)
               NOT_TAKEN

384            LOAD_FAST_BORROW         6 (next_state)
               LOAD_CONST              37 (('frustrated', 'hostile'))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       24 (to L19)
               NOT_TAKEN

385            LOAD_FAST_BORROW        10 (p)
               POP_JUMP_IF_NONE        20 (to L19)
               NOT_TAKEN
               LOAD_FAST_BORROW        10 (p)
               LOAD_ATTR               12 (patience)
               LOAD_CONST              26 (0.35)
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE        3 (to L19)
               NOT_TAKEN

386            LOAD_CONST              27 ('dropping')
               STORE_FAST               6 (next_state)

389   L19:     LOAD_CONST              28 ('next_state')
               LOAD_FAST_BORROW         6 (next_state)

390            LOAD_CONST              29 ('trust_delta')
               LOAD_FAST_BORROW         7 (trust_delta)

391            LOAD_CONST              30 ('frustration_delta')
               LOAD_FAST_BORROW         8 (frustration_delta)

392            LOAD_CONST              31 ('recovery_delta')
               LOAD_FAST_BORROW         9 (recovery_delta)

388            BUILD_MAP                4
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FF1230, file "app\services\simulation\behavior.py", line 396>:
396           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('strategy_id')

398           LOAD_GLOBAL              0 (Optional)
              LOAD_GLOBAL              2 (str)
              BINARY_OP               26 ([])

396           LOAD_CONST               2 ('lead_personality')

399           LOAD_GLOBAL              0 (Optional)
              LOAD_GLOBAL              4 (LeadPersonality)
              BINARY_OP               26 ([])

396           LOAD_CONST               3 ('behavior_state')

400           LOAD_GLOBAL              2 (str)

396           LOAD_CONST               4 ('turn_count')

401           LOAD_GLOBAL              6 (int)

396           LOAD_CONST               5 ('objection_count')

402           LOAD_GLOBAL              6 (int)

396           LOAD_CONST               6 ('engine_state')

403           LOAD_GLOBAL              0 (Optional)
              LOAD_GLOBAL              2 (str)
              BINARY_OP               26 ([])

396           LOAD_CONST               7 ('return')

404           LOAD_GLOBAL              8 (dict)

396           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object compute_behavioral_modifiers at 0x0000018C18248570, file "app\services\simulation\behavior.py", line 396>:
396            RESUME                   0

424            LOAD_CONST               1 (0.0)
               STORE_FAST               6 (drop)

425            LOAD_CONST               1 (0.0)
               STORE_FAST               7 (escalate)

426            LOAD_CONST               1 (0.0)
               STORE_FAST               8 (booking_fail)

427            LOAD_CONST               1 (0.0)
               STORE_FAST               9 (recovery)

428            LOAD_CONST               1 (0.0)
               STORE_FAST              10 (qualification)

430            LOAD_FAST_BORROW         1 (lead_personality)
               POP_JUMP_IF_NONE         9 (to L1)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (strategy_id)
               TO_BOOL
               POP_JUMP_IF_TRUE        13 (to L2)
               NOT_TAKEN

432    L1:     LOAD_CONST               2 ('drop_risk')
               LOAD_CONST               1 (0.0)

433            LOAD_CONST               3 ('escalation_risk')
               LOAD_CONST               1 (0.0)

434            LOAD_CONST               4 ('booking_failure_risk')
               LOAD_CONST               1 (0.0)

435            LOAD_CONST               5 ('recovery_bonus')
               LOAD_CONST               1 (0.0)

436            LOAD_CONST               6 ('qualification_bonus')
               LOAD_CONST               1 (0.0)

431            BUILD_MAP                5
               RETURN_VALUE

439    L2:     LOAD_FAST                1 (lead_personality)
               STORE_FAST              11 (p)

440            LOAD_GLOBAL              1 (get_strategy_traits + NULL)
               LOAD_FAST_BORROW         0 (strategy_id)
               CALL                     1
               STORE_FAST              12 (s)

444            LOAD_FAST_BORROW        11 (p)
               LOAD_ATTR                2 (patience)
               LOAD_CONST               7 (0.3)
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE       40 (to L3)
               NOT_TAKEN
               LOAD_FAST_BORROW        12 (s)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               8 ('brevity')
               LOAD_CONST               9 (0.5)
               CALL                     2
               LOAD_CONST               7 (0.3)
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE       17 (to L3)
               NOT_TAKEN
               LOAD_FAST_BORROW         3 (turn_count)
               LOAD_SMALL_INT           2
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       10 (to L3)
               NOT_TAKEN

445            LOAD_FAST_BORROW         6 (drop)
               LOAD_CONST              10 (0.6)
               BINARY_OP               13 (+=)
               STORE_FAST               6 (drop)

450    L3:     LOAD_FAST_BORROW        11 (p)
               LOAD_ATTR                6 (callback_preference)
               LOAD_CONST              11 (0.7)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       40 (to L4)
               NOT_TAKEN

451            LOAD_FAST_BORROW        12 (s)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              12 ('callback_friendly')
               LOAD_CONST               9 (0.5)
               CALL                     2
               LOAD_CONST              13 (0.4)
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE       17 (to L4)
               NOT_TAKEN

452            LOAD_FAST_BORROW         3 (turn_count)
               LOAD_SMALL_INT           4
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       10 (to L4)
               NOT_TAKEN

454            LOAD_FAST_BORROW         6 (drop)
               LOAD_CONST              14 (0.55)
               BINARY_OP               13 (+=)
               STORE_FAST               6 (drop)

457    L4:     LOAD_FAST_BORROW        11 (p)
               LOAD_ATTR                8 (aggression)
               LOAD_CONST              11 (0.7)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       40 (to L5)
               NOT_TAKEN
               LOAD_FAST_BORROW        12 (s)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              15 ('persistence')
               LOAD_CONST               9 (0.5)
               CALL                     2
               LOAD_CONST              16 (0.85)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       17 (to L5)
               NOT_TAKEN
               LOAD_FAST_BORROW         3 (turn_count)
               LOAD_SMALL_INT           2
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       10 (to L5)
               NOT_TAKEN

458            LOAD_FAST_BORROW         7 (escalate)
               LOAD_CONST              14 (0.55)
               BINARY_OP               13 (+=)
               STORE_FAST               7 (escalate)

461    L5:     LOAD_FAST_BORROW        11 (p)
               LOAD_ATTR               10 (skepticism)
               LOAD_CONST              11 (0.7)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       40 (to L6)
               NOT_TAKEN
               LOAD_FAST_BORROW        12 (s)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              17 ('formality')
               LOAD_CONST               9 (0.5)
               CALL                     2
               LOAD_CONST              18 (0.8)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       17 (to L6)
               NOT_TAKEN
               LOAD_FAST_BORROW         3 (turn_count)
               LOAD_SMALL_INT           2
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       10 (to L6)
               NOT_TAKEN

462            LOAD_FAST_BORROW         7 (escalate)
               LOAD_CONST              14 (0.55)
               BINARY_OP               13 (+=)
               STORE_FAST               7 (escalate)

466    L6:     LOAD_FAST_BORROW        11 (p)
               LOAD_ATTR               10 (skepticism)
               LOAD_CONST              10 (0.6)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       64 (to L8)
               NOT_TAKEN

467            LOAD_FAST_BORROW        11 (p)
               LOAD_ATTR               12 (trust_threshold)
               LOAD_CONST              19 (0.65)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       47 (to L8)
               NOT_TAKEN

468            LOAD_FAST_BORROW        12 (s)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              20 ('consultative')
               LOAD_CONST               9 (0.5)
               CALL                     2
               LOAD_CONST              21 (0.25)
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE       24 (to L8)
               NOT_TAKEN

469            LOAD_FAST_BORROW         5 (engine_state)
               LOAD_CONST              22 ('BOOKING')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_TRUE         8 (to L7)
               NOT_TAKEN
               LOAD_FAST_BORROW         2 (behavior_state)
               LOAD_CONST              27 (('skeptical', 'frustrated'))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       10 (to L8)
               NOT_TAKEN

471    L7:     LOAD_FAST_BORROW         8 (booking_fail)
               LOAD_CONST              14 (0.55)
               BINARY_OP               13 (+=)
               STORE_FAST               8 (booking_fail)

475    L8:     LOAD_FAST_BORROW        11 (p)
               LOAD_ATTR               12 (trust_threshold)
               LOAD_CONST              18 (0.8)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       40 (to L9)
               NOT_TAKEN

476            LOAD_FAST_BORROW        12 (s)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              23 ('warmth')
               LOAD_CONST               9 (0.5)
               CALL                     2
               LOAD_CONST               7 (0.3)
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE       17 (to L9)
               NOT_TAKEN

477            LOAD_FAST_BORROW         5 (engine_state)
               LOAD_CONST              22 ('BOOKING')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       10 (to L9)
               NOT_TAKEN

479            LOAD_FAST_BORROW         8 (booking_fail)
               LOAD_CONST              14 (0.55)
               BINARY_OP               13 (+=)
               STORE_FAST               8 (booking_fail)

483    L9:     LOAD_FAST_BORROW        11 (p)
               LOAD_ATTR               14 (id)
               LOAD_CONST              24 ('luxury_buyer')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       40 (to L10)
               NOT_TAKEN

484            LOAD_FAST_BORROW        12 (s)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               8 ('brevity')
               LOAD_CONST               9 (0.5)
               CALL                     2
               LOAD_CONST              25 (0.9)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       17 (to L10)
               NOT_TAKEN

485            LOAD_FAST_BORROW         5 (engine_state)
               LOAD_CONST              22 ('BOOKING')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       10 (to L10)
               NOT_TAKEN

487            LOAD_FAST_BORROW         8 (booking_fail)
               LOAD_CONST              14 (0.55)
               BINARY_OP               13 (+=)
               STORE_FAST               8 (booking_fail)

490   L10:     LOAD_FAST_BORROW        11 (p)
               LOAD_ATTR               10 (skepticism)
               LOAD_CONST              10 (0.6)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       33 (to L11)
               NOT_TAKEN
               LOAD_FAST_BORROW        12 (s)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              20 ('consultative')
               LOAD_CONST               9 (0.5)
               CALL                     2
               LOAD_CONST              11 (0.7)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       10 (to L11)
               NOT_TAKEN

491            LOAD_FAST_BORROW         9 (recovery)
               LOAD_CONST               9 (0.5)
               BINARY_OP               13 (+=)
               STORE_FAST               9 (recovery)

494   L11:     LOAD_FAST_BORROW        10 (qualification)
               LOAD_GLOBAL             17 (min + NULL)
               LOAD_FAST_BORROW        11 (p)
               LOAD_ATTR               18 (qualification_cooperation)
               LOAD_CONST               9 (0.5)
               BINARY_OP                5 (*)
               LOAD_CONST               9 (0.5)
               CALL                     2
               BINARY_OP               13 (+=)
               STORE_FAST              10 (qualification)

498            LOAD_CONST               2 ('drop_risk')
               LOAD_GLOBAL             17 (min + NULL)
               LOAD_FAST_BORROW         6 (drop)
               LOAD_CONST              26 (1.0)
               CALL                     2

499            LOAD_CONST               3 ('escalation_risk')
               LOAD_GLOBAL             17 (min + NULL)
               LOAD_FAST_BORROW         7 (escalate)
               LOAD_CONST              26 (1.0)
               CALL                     2

500            LOAD_CONST               4 ('booking_failure_risk')
               LOAD_GLOBAL             17 (min + NULL)
               LOAD_FAST_BORROW         8 (booking_fail)
               LOAD_CONST              26 (1.0)
               CALL                     2

501            LOAD_CONST               5 ('recovery_bonus')
               LOAD_GLOBAL             17 (min + NULL)
               LOAD_FAST_BORROW         9 (recovery)
               LOAD_CONST              26 (1.0)
               CALL                     2

502            LOAD_CONST               6 ('qualification_bonus')
               LOAD_GLOBAL             17 (min + NULL)
               LOAD_FAST_BORROW        10 (qualification)
               LOAD_CONST              26 (1.0)
               CALL                     2

497            BUILD_MAP                5
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17CC2460, file "app\services\simulation\behavior.py", line 1>:
  1           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     BUILD_MAP                0

 34           LOAD_SMALL_INT           0
              LOAD_GLOBAL              0 (__conditional_annotations__)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       23 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              2 (Tuple)
              LOAD_GLOBAL              4 (str)
              LOAD_CONST               1 (Ellipsis)
              BUILD_TUPLE              2
              BINARY_OP               26 ([])
              COPY                     2
              LOAD_CONST               2 ('BEHAVIOR_STATES')

  1           STORE_SUBSCR

 69   L2:     LOAD_SMALL_INT           1
              LOAD_GLOBAL              0 (__conditional_annotations__)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       23 (to L3)
              NOT_TAKEN
              LOAD_GLOBAL              2 (Tuple)
              LOAD_GLOBAL              6 (LeadPersonality)
              LOAD_CONST               1 (Ellipsis)
              BUILD_TUPLE              2
              BINARY_OP               26 ([])
              COPY                     2
              LOAD_CONST               3 ('PERSONALITIES')

  1           STORE_SUBSCR

218   L3:     LOAD_SMALL_INT           2
              LOAD_GLOBAL              0 (__conditional_annotations__)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       44 (to L4)
              NOT_TAKEN
              LOAD_GLOBAL              8 (Dict)
              LOAD_GLOBAL              4 (str)
              LOAD_GLOBAL              8 (Dict)
              LOAD_GLOBAL              4 (str)
              LOAD_GLOBAL             10 (float)
              BUILD_TUPLE              2
              BINARY_OP               26 ([])
              BUILD_TUPLE              2
              BINARY_OP               26 ([])
              COPY                     2
              LOAD_CONST               4 ('STRATEGY_TRAITS')

  1           STORE_SUBSCR

243   L4:     LOAD_SMALL_INT           3
              LOAD_GLOBAL              0 (__conditional_annotations__)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       27 (to L5)
              NOT_TAKEN
              LOAD_GLOBAL              8 (Dict)
              LOAD_GLOBAL              4 (str)
              LOAD_GLOBAL             10 (float)
              BUILD_TUPLE              2
              BINARY_OP               26 ([])
              COPY                     2
              LOAD_CONST               5 ('_NEUTRAL_TRAITS')

  1           STORE_SUBSCR

508   L5:     LOAD_SMALL_INT           4
              LOAD_GLOBAL              0 (__conditional_annotations__)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       10 (to L6)
              NOT_TAKEN
              LOAD_GLOBAL             10 (float)
              COPY                     2
              LOAD_CONST               6 ('TRIGGER_THRESHOLD')

  1           STORE_SUBSCR

515   L6:     LOAD_SMALL_INT           5
              LOAD_GLOBAL              0 (__conditional_annotations__)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       10 (to L7)
              NOT_TAKEN
              LOAD_GLOBAL              4 (str)
              COPY                     2
              LOAD_CONST               7 ('ESCALATION_INJECTION_TEXT')

  1           STORE_SUBSCR
      L7:     RETURN_VALUE
```
