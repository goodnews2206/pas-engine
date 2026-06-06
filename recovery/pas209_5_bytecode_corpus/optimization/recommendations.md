# optimization/recommendations

- **pyc:** `app\services\optimization\__pycache__\recommendations.cpython-314.pyc`
- **expected source path (absent):** `app\services\optimization/recommendations.py`
- **co_filename (from bytecode):** `C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** optimization

## Module docstring

```
PAS143C — Optimization recommendation layer.

Bridge from the deterministic measurement substrate (matrix → metrics →
ranking → report) to plain-English recommendations a brokerage owner
or operator can act on.

Doctrine: Apple-level simple, Claude-level functional. The titles must
sound like a smart operator briefing a broker — never raw metric names,
never "divergence rate", never "replay score". The complexity stays
inside `evidence` for the curious; the title and `recommended_action`
must read in one breath.

Pure function. No LLMs, no I/O, no randomness.

Public surface:
  generate_recommendations(report_or_matrix)  → list[dict]
  summarize_recommendations(recommendations)  → str (CLI block)

Each recommendation dict carries:
  id, priority (high|medium|low), audience (broker|operator|system),
  title, insight, recommended_action, evidence, affected_personality,
  affected_strategy, expected_impact, confidence (low|medium|high).
```

## Imports

`Dict`, `List`, `Optional`, `Tuple`, `compute_matrix_metrics`, `generate_optimization_report`, `metrics`, `report`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_avoid_recommendation`, `_avoid_title`, `_confidence_from_n`, `_high_dropoff_recommendation`, `_high_frustration_recommendation`, `_infra_only_recommendation`, `_looks_like_report`, `_pretty_personality`, `_pretty_strategy`, `_tied_top_recommendation`, `_use_recommendation`, `_use_title`, `generate_recommendations`, `summarize_recommendations`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS143C — Optimization recommendation layer.\n\nBridge from the deterministic measurement substrate (matrix → metrics →\nranking → report) to plain-English recommendations a brokerage owner\nor operator can act on.\n\nDoctrine: Apple-level simple, Claude-level functional. The titles must\nsound like a smart operator briefing a broker — never raw metric names,\nnever "divergence rate", never "replay score". The complexity stays\ninside `evidence` for the curious; the title and `recommended_action`\nmust read in one breath.\n\nPure function. No LLMs, no I/O, no randomness.\n\nPublic surface:\n  generate_recommendations(report_or_matrix)  → list[dict]\n  summarize_recommendations(recommendations)  → str (CLI block)\n\nEach recommendation dict carries:\n  id, priority (high|medium|low), audience (broker|operator|system),\n  title, insight, recommended_action, evidence, affected_personality,\n  affected_strategy, expected_impact, confidence (low|medium|high).\n'
- 'impatient'
- 'Warm, long responses lose impatient leads.'
- 'Heavy rebuttals exhaust impatient leads.'
- 'Consultative back-and-forth tires out impatient leads.'
- 'skeptical'
- 'Skeptical leads escalate under authoritative tone.'
- 'Pushing back hard turns skeptical leads off.'
- 'distrustful'
- 'Distrustful leads react badly to authoritative tone.'
- 'Distrustful leads shut down when pushed.'
- 'Distrustful leads need warmth — hyper-brief feels dismissive.'
- 'aggressive'
- 'Aggressive leads push back harder when rebutted.'
- 'Aggressive leads escalate under authoritative tone.'
- 'busy'
- 'Busy leads drop when responses are long and warm.'
- 'Busy leads drop when objection handling drags.'
- "Busy leads can't sit through consultative redirects."
- 'comparison_shopper'
- 'Comparison shoppers shut down on heavy rebuttals.'
- 'Comparison shoppers need more reassurance than hyper-brief offers.'
- 'Comparison shoppers want consultation, not authority.'
- 'luxury_buyer'
- 'Luxury buyers expect more than a hyper-brief opening.'
- 'Luxury buyers want pacing — direct & fast feels rushed.'
- 'emotional'
- 'Emotional leads need warmth — authoritative tone backfires.'
- 'Emotional leads need warmth — heavy rebuttal escalates them.'
- 'Impatient leads need a shorter opening.'
- 'Skeptical leads need consultative reassurance.'
- 'Distrustful leads need warmth and time.'
- 'Aggressive leads need a calmer, lower-pressure flow.'
- 'Busy leads need an immediate callback offer.'
- 'Comparison shoppers want consultative answers.'
- 'Luxury buyers expect a formal, paced flow.'
- 'Emotional leads need warmth, not pressure.'
- 'analytical'
- 'Analytical leads want structured, methodical answers.'
- 'motivated'
- 'These leads are usually flexible — investigate why this style is failing.'
- 'Impatient leads convert best on the briefest opening.'
- 'Impatient leads convert with direct, fast openings.'
- 'Soft exits stop impatient leads from churning.'
- 'Skeptical leads open up under consultative questions.'
- 'Skeptical leads engage when led by curiosity.'
- 'Warm consultative openings build trust with skeptical leads.'
- 'Distrustful leads warm up to a consultative opening.'
- 'Distrustful leads soften under a consultative redirect.'
- 'Soft exits de-escalate aggressive leads cleanly.'
- 'Curiosity questions disarm aggressive leads.'
- 'Busy leads accept an urgent callback offer.'
- 'Busy leads accept a flexible callback offer.'
- 'Busy leads stay engaged with the briefest possible flow.'
- 'Comparison shoppers convert under consultative answers.'
- 'Curiosity-led answers reassure comparison shoppers.'
- 'Warm consultative answers convert comparison shoppers.'
- 'Luxury buyers convert under a warm consultative open.'
- 'An authoritative tone reassures luxury buyers.'
- 'Warm consultative answers ease emotional leads in.'
- 'Analytical leads engage with structured consultative replies.'
- 'Use a brief, direct style for impatient leads.'
- 'Use consultative styles for skeptical leads.'
- 'Use warm consultative styles for distrustful leads.'
- 'Use calm, low-pressure styles for aggressive leads.'
- 'Use callback-friendly styles for busy leads.'
- 'Use consultative styles for comparison shoppers.'
- 'Use formal, paced styles for luxury buyers.'
- 'Use warm styles for emotional leads.'
- 'Use structured styles for analytical leads.'
- 'Almost any reasonable style converts motivated leads.'
- 'high'
- 'medium'
- 'low'
- 'pid'
- 'return'
- 'sid'
- 'strategy_id'
- 'personality_id'
- 'This style is not a fit for these leads.'
- 'Use the '
- ' style for these leads.'
- 'cell'
- 'pass_rate'
- 'booked_rate'
- 'avoid_'
- 'priority'
- 'audience'
- 'broker'
- 'title'
- 'insight'
- ' leads completed '
- '.0%'
- ' of calls under '
- ' (out of '
- ' call(s)).'
- 'recommended_action'
- 'Route '
- ' leads away from the '
- ' flow until the pattern improves.'
- 'evidence'
- " simulated call(s) with personality '"
- "' under strategy '"
- "': pass "
- ', booked '
- 'affected_personality'
- 'affected_strategy'
- 'expected_impact'
- 'Higher conversion rate for this personality bucket.'
- 'confidence'
- 'use_'
- '_for_'
- 'Prefer the '
- " flow when the lead profile looks like '"
- 'Sustains the strong conversion pattern already observed.'
- 'avg_frustration'
- 'high_frustration'
- 'Calls are running hot — shorter answers will reduce friction.'
- 'Across the run, leads accumulated meaningful frustration before the call ended. That signals tone or response length is fighting the lead, not the other way around.'
- 'Shorten PAS responses and soften the booking ask. Pilot a brief / consultative style and re-measure.'
- 'Average frustration '
- ' across the matrix.'
- 'Lower mid-call drop-off, higher bookings.'
- 'dropoff_rate'
- 'high_dropoff'
- 'Leads are dropping mid-call — offer the callback option earlier.'
- 'A significant share of calls ended with the lead simply disengaging. Most of those leads will respond to a callback if one is offered before they leave.'
- 'Move the callback offer earlier in the script and route busy / impatient leads to a callback flow by default.'
- 'Drop-off rate '
- 'Recover bookings that would otherwise be lost.'
- 'tied_strategy_ids'
- 'top_tied_collect_more'
- 'operator'
- 'Top-performing styles are too close to call — gather more conversations before locking one in.'
- "Several styles are scoring identically. That usually means the current scenario set isn't broad enough to differentiate them."
- "Run more scenarios, especially for personality types that haven't been exercised yet, and re-run the matrix."
- 'Tied at the top: '
- 'Higher confidence in the eventual winner.'
- 'infra_ready_engine_inert'
- 'system'
- "Optimization infrastructure is ready, but call behaviour isn't yet using these styles."
- 'The matrix and metrics are wired end-to-end, but no strategy in this run actually changes how PAS speaks to a lead. Rankings are infrastructure-only.'
- 'Wire one strategy override (e.g. greeting tone or callback phrasing) into the engine, then re-run the matrix to see real outcome differences.'
- 'No strategy in this matrix is engine-effective.'
- 'Unlocks the rest of the recommendation surface.'
- 'A report has ranked_strategies; a raw matrix has results.'
- 'ranked_strategies'
- 'report_or_matrix'
- '\nConvert an optimization report (or a raw matrix) into ordered,\nbusiness-readable recommendations.\n\nAccepts either:\n  - the full dict from `generate_optimization_report`, or\n  - the raw `run_strategy_matrix` dict (compute_metrics + report\n    are run internally — operator can call either).\n\nSorted high → medium → low priority, with deterministic id-based\ntie-break inside each priority bucket. Empty / malformed input\nreturns []. Never raises.\n'
- 'metrics'
- 'total_runs'
- 'behavior_summary'
- 'personality_insights'
- 'by_strategy_personality'
- 'any_strategy_effective'
- 'score'
- 'recommendations'
- '\nRender the recommendation list as the human-readable block the CLI\nprints when --recommendations is supplied. Empty input returns a\nsingle explanatory line.\n'
- 'No actionable recommendations from this batch.'
- '. ['
- '   Action: '
- '   Evidence: '
- '_AVOID_PAIR_TITLES'
- '_AVOID_FALLBACK_BY_PERSONALITY'
- '_USE_PAIR_TITLES'
- '_USE_FALLBACK_BY_PERSONALITY'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           LOAD_CONST             105 (<code object __annotate__ at 0x0000018C17F60830, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 1>)
               MAKE_FUNCTION
               STORE_NAME              30 (__annotate__)
               BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               LOAD_CONST               0 ('\nPAS143C — Optimization recommendation layer.\n\nBridge from the deterministic measurement substrate (matrix → metrics →\nranking → report) to plain-English recommendations a brokerage owner\nor operator can act on.\n\nDoctrine: Apple-level simple, Claude-level functional. The titles must\nsound like a smart operator briefing a broker — never raw metric names,\nnever "divergence rate", never "replay score". The complexity stays\ninside `evidence` for the curious; the title and `recommended_action`\nmust read in one breath.\n\nPure function. No LLMs, no I/O, no randomness.\n\nPublic surface:\n  generate_recommendations(report_or_matrix)  → list[dict]\n  summarize_recommendations(recommendations)  → str (CLI block)\n\nEach recommendation dict carries:\n  id, priority (high|medium|low), audience (broker|operator|system),\n  title, insight, recommended_action, evidence, affected_personality,\n  affected_strategy, expected_impact, confidence (low|medium|high).\n')
               STORE_NAME               1 (__doc__)

  26           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('Dict', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME              2 (typing)
               IMPORT_FROM              3 (Dict)
               STORE_NAME               3 (Dict)
               IMPORT_FROM              4 (List)
               STORE_NAME               4 (List)
               IMPORT_FROM              5 (Optional)
               STORE_NAME               5 (Optional)
               IMPORT_FROM              6 (Tuple)
               STORE_NAME               6 (Tuple)
               POP_TOP

  28           LOAD_SMALL_INT           1
               LOAD_CONST               2 (('compute_matrix_metrics',))
               IMPORT_NAME              7 (metrics)
               IMPORT_FROM              8 (compute_matrix_metrics)
               STORE_NAME               8 (compute_matrix_metrics)
               POP_TOP

  29           LOAD_SMALL_INT           1
               LOAD_CONST               3 (('generate_optimization_report',))
               IMPORT_NAME              9 (report)
               IMPORT_FROM             10 (generate_optimization_report)
               STORE_NAME              10 (generate_optimization_report)
               POP_TOP

  38           BUILD_MAP                0

  39           LOAD_CONST             107 (('impatient', 'warm_consultative'))
               LOAD_CONST               5 ('Warm, long responses lose impatient leads.')

  38           MAP_ADD                  1

  40           LOAD_CONST             108 (('impatient', 'rebuttal_heavy'))
               LOAD_CONST               6 ('Heavy rebuttals exhaust impatient leads.')

  38           MAP_ADD                  1

  41           LOAD_CONST             109 (('impatient', 'consultative_redirect'))
               LOAD_CONST               7 ('Consultative back-and-forth tires out impatient leads.')

  38           MAP_ADD                  1

  42           LOAD_CONST             110 (('skeptical', 'authoritative'))
               LOAD_CONST               9 ('Skeptical leads escalate under authoritative tone.')

  38           MAP_ADD                  1

  43           LOAD_CONST             111 (('skeptical', 'rebuttal_heavy'))
               LOAD_CONST              10 ('Pushing back hard turns skeptical leads off.')

  38           MAP_ADD                  1

  44           LOAD_CONST             112 (('distrustful', 'authoritative'))
               LOAD_CONST              12 ('Distrustful leads react badly to authoritative tone.')

  38           MAP_ADD                  1

  45           LOAD_CONST             113 (('distrustful', 'rebuttal_heavy'))
               LOAD_CONST              13 ('Distrustful leads shut down when pushed.')

  38           MAP_ADD                  1

  46           LOAD_CONST             114 (('distrustful', 'hyper_brief'))
               LOAD_CONST              14 ('Distrustful leads need warmth — hyper-brief feels dismissive.')

  38           MAP_ADD                  1

  47           LOAD_CONST             115 (('aggressive', 'rebuttal_heavy'))
               LOAD_CONST              16 ('Aggressive leads push back harder when rebutted.')

  38           MAP_ADD                  1

  48           LOAD_CONST             116 (('aggressive', 'authoritative'))
               LOAD_CONST              17 ('Aggressive leads escalate under authoritative tone.')

  38           MAP_ADD                  1

  49           LOAD_CONST             117 (('busy', 'warm_consultative'))
               LOAD_CONST              19 ('Busy leads drop when responses are long and warm.')

  38           MAP_ADD                  1

  50           LOAD_CONST             118 (('busy', 'rebuttal_heavy'))
               LOAD_CONST              20 ('Busy leads drop when objection handling drags.')

  38           MAP_ADD                  1

  51           LOAD_CONST             119 (('busy', 'consultative_redirect'))
               LOAD_CONST              21 ("Busy leads can't sit through consultative redirects.")

  38           MAP_ADD                  1

  52           LOAD_CONST             120 (('comparison_shopper', 'rebuttal_heavy'))
               LOAD_CONST              23 ('Comparison shoppers shut down on heavy rebuttals.')

  38           MAP_ADD                  1

  53           LOAD_CONST             121 (('comparison_shopper', 'hyper_brief'))
               LOAD_CONST              24 ('Comparison shoppers need more reassurance than hyper-brief offers.')

  38           MAP_ADD                  1

  54           LOAD_CONST             122 (('comparison_shopper', 'authoritative'))
               LOAD_CONST              25 ('Comparison shoppers want consultation, not authority.')

  38           MAP_ADD                  1

  55           LOAD_CONST             123 (('luxury_buyer', 'hyper_brief'))
               LOAD_CONST              27 ('Luxury buyers expect more than a hyper-brief opening.')

  38           MAP_ADD                  1

  56           LOAD_CONST             124 (('luxury_buyer', 'direct_fast'))
               LOAD_CONST              28 ('Luxury buyers want pacing — direct & fast feels rushed.')

  57           LOAD_CONST             125 (('emotional', 'authoritative'))
               LOAD_CONST              30 ('Emotional leads need warmth — authoritative tone backfires.')

  58           LOAD_CONST             126 (('emotional', 'rebuttal_heavy'))
               LOAD_CONST              31 ('Emotional leads need warmth — heavy rebuttal escalates them.')

  38           BUILD_MAP                3
               DICT_UPDATE              1
               STORE_NAME              11 (_AVOID_PAIR_TITLES)
               LOAD_NAME                0 (__conditional_annotations__)
               LOAD_SMALL_INT           0
               SET_ADD                  1
               POP_TOP

  62           LOAD_CONST               4 ('impatient')
               LOAD_CONST              32 ('Impatient leads need a shorter opening.')

  63           LOAD_CONST               8 ('skeptical')
               LOAD_CONST              33 ('Skeptical leads need consultative reassurance.')

  64           LOAD_CONST              11 ('distrustful')
               LOAD_CONST              34 ('Distrustful leads need warmth and time.')

  65           LOAD_CONST              15 ('aggressive')
               LOAD_CONST              35 ('Aggressive leads need a calmer, lower-pressure flow.')

  66           LOAD_CONST              18 ('busy')
               LOAD_CONST              36 ('Busy leads need an immediate callback offer.')

  67           LOAD_CONST              22 ('comparison_shopper')
               LOAD_CONST              37 ('Comparison shoppers want consultative answers.')

  68           LOAD_CONST              26 ('luxury_buyer')
               LOAD_CONST              38 ('Luxury buyers expect a formal, paced flow.')

  69           LOAD_CONST              29 ('emotional')
               LOAD_CONST              39 ('Emotional leads need warmth, not pressure.')

  70           LOAD_CONST              40 ('analytical')
               LOAD_CONST              41 ('Analytical leads want structured, methodical answers.')

  71           LOAD_CONST              42 ('motivated')
               LOAD_CONST              43 ('These leads are usually flexible — investigate why this style is failing.')

  61           BUILD_MAP               10
               STORE_NAME              12 (_AVOID_FALLBACK_BY_PERSONALITY)
               LOAD_NAME                0 (__conditional_annotations__)
               LOAD_SMALL_INT           1
               SET_ADD                  1
               POP_TOP

  75           BUILD_MAP                0

  76           LOAD_CONST             127 (('impatient', 'hyper_brief'))
               LOAD_CONST              44 ('Impatient leads convert best on the briefest opening.')

  75           MAP_ADD                  1

  77           LOAD_CONST             128 (('impatient', 'direct_fast'))
               LOAD_CONST              45 ('Impatient leads convert with direct, fast openings.')

  75           MAP_ADD                  1

  78           LOAD_CONST             129 (('impatient', 'soft_exit'))
               LOAD_CONST              46 ('Soft exits stop impatient leads from churning.')

  75           MAP_ADD                  1

  79           LOAD_CONST             130 (('skeptical', 'consultative_redirect'))
               LOAD_CONST              47 ('Skeptical leads open up under consultative questions.')

  75           MAP_ADD                  1

  80           LOAD_CONST             131 (('skeptical', 'curiosity_based'))
               LOAD_CONST              48 ('Skeptical leads engage when led by curiosity.')

  75           MAP_ADD                  1

  81           LOAD_CONST             132 (('skeptical', 'warm_consultative'))
               LOAD_CONST              49 ('Warm consultative openings build trust with skeptical leads.')

  75           MAP_ADD                  1

  82           LOAD_CONST             133 (('distrustful', 'warm_consultative'))
               LOAD_CONST              50 ('Distrustful leads warm up to a consultative opening.')

  75           MAP_ADD                  1

  83           LOAD_CONST             134 (('distrustful', 'consultative_redirect'))
               LOAD_CONST              51 ('Distrustful leads soften under a consultative redirect.')

  75           MAP_ADD                  1

  84           LOAD_CONST             135 (('aggressive', 'soft_exit'))
               LOAD_CONST              52 ('Soft exits de-escalate aggressive leads cleanly.')

  75           MAP_ADD                  1

  85           LOAD_CONST             136 (('aggressive', 'curiosity_based'))
               LOAD_CONST              53 ('Curiosity questions disarm aggressive leads.')

  75           MAP_ADD                  1

  86           LOAD_CONST             137 (('busy', 'urgency_callback'))
               LOAD_CONST              54 ('Busy leads accept an urgent callback offer.')

  75           MAP_ADD                  1

  87           LOAD_CONST             138 (('busy', 'flexible_callback'))
               LOAD_CONST              55 ('Busy leads accept a flexible callback offer.')

  75           MAP_ADD                  1

  88           LOAD_CONST             139 (('busy', 'hyper_brief'))
               LOAD_CONST              56 ('Busy leads stay engaged with the briefest possible flow.')

  75           MAP_ADD                  1

  89           LOAD_CONST             140 (('comparison_shopper', 'consultative_redirect'))
               LOAD_CONST              57 ('Comparison shoppers convert under consultative answers.')

  75           MAP_ADD                  1

  90           LOAD_CONST             141 (('comparison_shopper', 'curiosity_based'))
               LOAD_CONST              58 ('Curiosity-led answers reassure comparison shoppers.')

  75           MAP_ADD                  1

  91           LOAD_CONST             142 (('comparison_shopper', 'warm_consultative'))
               LOAD_CONST              59 ('Warm consultative answers convert comparison shoppers.')

  75           MAP_ADD                  1

  92           LOAD_CONST             143 (('luxury_buyer', 'warm_consultative'))
               LOAD_CONST              60 ('Luxury buyers convert under a warm consultative open.')

  75           MAP_ADD                  1

  93           LOAD_CONST             144 (('luxury_buyer', 'authoritative'))
               LOAD_CONST              61 ('An authoritative tone reassures luxury buyers.')

  94           LOAD_CONST             145 (('emotional', 'warm_consultative'))
               LOAD_CONST              62 ('Warm consultative answers ease emotional leads in.')

  95           LOAD_CONST             146 (('analytical', 'consultative_redirect'))
               LOAD_CONST              63 ('Analytical leads engage with structured consultative replies.')

  75           BUILD_MAP                3
               DICT_UPDATE              1
               STORE_NAME              13 (_USE_PAIR_TITLES)
               LOAD_NAME                0 (__conditional_annotations__)
               LOAD_SMALL_INT           2
               SET_ADD                  1
               POP_TOP

  99           LOAD_CONST               4 ('impatient')
               LOAD_CONST              64 ('Use a brief, direct style for impatient leads.')

 100           LOAD_CONST               8 ('skeptical')
               LOAD_CONST              65 ('Use consultative styles for skeptical leads.')

 101           LOAD_CONST              11 ('distrustful')
               LOAD_CONST              66 ('Use warm consultative styles for distrustful leads.')

 102           LOAD_CONST              15 ('aggressive')
               LOAD_CONST              67 ('Use calm, low-pressure styles for aggressive leads.')

 103           LOAD_CONST              18 ('busy')
               LOAD_CONST              68 ('Use callback-friendly styles for busy leads.')

 104           LOAD_CONST              22 ('comparison_shopper')
               LOAD_CONST              69 ('Use consultative styles for comparison shoppers.')

 105           LOAD_CONST              26 ('luxury_buyer')
               LOAD_CONST              70 ('Use formal, paced styles for luxury buyers.')

 106           LOAD_CONST              29 ('emotional')
               LOAD_CONST              71 ('Use warm styles for emotional leads.')

 107           LOAD_CONST              40 ('analytical')
               LOAD_CONST              72 ('Use structured styles for analytical leads.')

 108           LOAD_CONST              42 ('motivated')
               LOAD_CONST              73 ('Almost any reasonable style converts motivated leads.')

  98           BUILD_MAP               10
               STORE_NAME              14 (_USE_FALLBACK_BY_PERSONALITY)
               LOAD_NAME                0 (__conditional_annotations__)
               LOAD_SMALL_INT           3
               SET_ADD                  1
               POP_TOP

 112           LOAD_CONST              74 (<code object __annotate__ at 0x0000018C18052F70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 112>)
               MAKE_FUNCTION
               LOAD_CONST              75 (<code object _pretty_personality at 0x0000018C180E8030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 112>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              15 (_pretty_personality)

 118           LOAD_CONST              76 (<code object __annotate__ at 0x0000018C18053630, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 118>)
               MAKE_FUNCTION
               LOAD_CONST              77 (<code object _pretty_strategy at 0x0000018C180E8140, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 118>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              16 (_pretty_strategy)

 124           LOAD_CONST              78 (<code object __annotate__ at 0x0000018C180E8250, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 124>)
               MAKE_FUNCTION
               LOAD_CONST              79 (<code object _avoid_title at 0x0000018C18038670, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 124>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              17 (_avoid_title)

 134           LOAD_CONST              80 (<code object __annotate__ at 0x0000018C180E8360, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 134>)
               MAKE_FUNCTION
               LOAD_CONST              81 (<code object _use_title at 0x0000018C17FE1920, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 134>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              18 (_use_title)

 148           LOAD_CONST              82 ('high')
               LOAD_SMALL_INT           0
               LOAD_CONST              83 ('medium')
               LOAD_SMALL_INT           1
               LOAD_CONST              84 ('low')
               LOAD_SMALL_INT           2
               BUILD_MAP                3
               STORE_NAME              19 (_PRIORITY_ORDER)

 151           LOAD_CONST              85 (<code object __annotate__ at 0x0000018C18025130, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 151>)
               MAKE_FUNCTION
               LOAD_CONST              86 (<code object _confidence_from_n at 0x0000018C18025030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 151>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              20 (_confidence_from_n)

 159           LOAD_CONST              87 (<code object __annotate__ at 0x0000018C18053CF0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 159>)
               MAKE_FUNCTION
               LOAD_CONST              88 (<code object _avoid_recommendation at 0x0000018C17D8E300, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 159>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              21 (_avoid_recommendation)

 188           LOAD_CONST              89 (<code object __annotate__ at 0x0000018C18053750, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 188>)
               MAKE_FUNCTION
               LOAD_CONST              90 (<code object _use_recommendation at 0x0000018C17ECEB60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 188>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              22 (_use_recommendation)

 217           LOAD_CONST              91 (<code object __annotate__ at 0x0000018C18026130, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 217>)
               MAKE_FUNCTION
               LOAD_CONST              92 (<code object _high_frustration_recommendation at 0x0000018C180E8470, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 217>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              23 (_high_frustration_recommendation)

 240           LOAD_CONST              93 (<code object __annotate__ at 0x0000018C18026230, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 240>)
               MAKE_FUNCTION
               LOAD_CONST              94 (<code object _high_dropoff_recommendation at 0x0000018C180E8580, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 240>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              24 (_high_dropoff_recommendation)

 263           LOAD_CONST              95 (<code object __annotate__ at 0x0000018C18053BD0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 263>)
               MAKE_FUNCTION
               LOAD_CONST              96 (<code object _tied_top_recommendation at 0x0000018C1802C9B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 263>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              25 (_tied_top_recommendation)

 288           LOAD_CONST              97 (<code object __annotate__ at 0x0000018C18024B30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 288>)
               MAKE_FUNCTION
               LOAD_CONST              98 (<code object _infra_only_recommendation at 0x0000018C180E8690, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 288>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              26 (_infra_only_recommendation)

 319           LOAD_CONST              99 (<code object __annotate__ at 0x0000018C18026330, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 319>)
               MAKE_FUNCTION
               LOAD_CONST             100 (<code object _looks_like_report at 0x0000018C180E87A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 319>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              27 (_looks_like_report)

 324           LOAD_CONST             101 (<code object __annotate__ at 0x0000018C180533F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 324>)
               MAKE_FUNCTION
               LOAD_CONST             102 (<code object generate_recommendations at 0x0000018C17E042A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 324>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (generate_recommendations)

 432           LOAD_CONST             103 (<code object __annotate__ at 0x0000018C180531B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 432>)
               MAKE_FUNCTION
               LOAD_CONST             104 (<code object summarize_recommendations at 0x0000018C17CD1200, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 432>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              29 (summarize_recommendations)
               LOAD_CONST             106 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18052F70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 112>:
112           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('pid')
              LOAD_GLOBAL              0 (Optional)
              LOAD_GLOBAL              2 (str)
              BINARY_OP               26 ([])
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              2 (str)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _pretty_personality at 0x0000018C180E8030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 112>:
112           RESUME                   0

113           LOAD_FAST_BORROW         0 (pid)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

114           LOAD_CONST               0 ('')
              RETURN_VALUE

115   L1:     LOAD_FAST_BORROW         0 (pid)
              LOAD_ATTR                1 (replace + NULL|self)
              LOAD_CONST               1 ('_')
              LOAD_CONST               2 (' ')
              CALL                     2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18053630, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 118>:
118           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('sid')
              LOAD_GLOBAL              0 (Optional)
              LOAD_GLOBAL              2 (str)
              BINARY_OP               26 ([])
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              2 (str)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _pretty_strategy at 0x0000018C180E8140, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 118>:
118           RESUME                   0

119           LOAD_FAST_BORROW         0 (sid)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

120           LOAD_CONST               0 ('')
              RETURN_VALUE

121   L1:     LOAD_FAST_BORROW         0 (sid)
              LOAD_ATTR                1 (replace + NULL|self)
              LOAD_CONST               1 ('_')
              LOAD_CONST               2 (' ')
              CALL                     2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180E8250, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 124>:
124           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('strategy_id')
              LOAD_GLOBAL              0 (str)
              LOAD_CONST               2 ('personality_id')
              LOAD_GLOBAL              0 (str)
              LOAD_CONST               3 ('return')
              LOAD_GLOBAL              0 (str)
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _avoid_title at 0x0000018C18038670, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 124>:
124           RESUME                   0

125           LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (personality_id, strategy_id)
              BUILD_TUPLE              2
              STORE_FAST               2 (pair)

126           LOAD_FAST_BORROW         2 (pair)
              LOAD_GLOBAL              0 (_AVOID_PAIR_TITLES)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       14 (to L1)
              NOT_TAKEN

127           LOAD_GLOBAL              0 (_AVOID_PAIR_TITLES)
              LOAD_FAST_BORROW         2 (pair)
              BINARY_OP               26 ([])
              RETURN_VALUE

128   L1:     LOAD_GLOBAL              2 (_AVOID_FALLBACK_BY_PERSONALITY)
              LOAD_ATTR                5 (get + NULL|self)

129           LOAD_FAST_BORROW         1 (personality_id)

130           LOAD_CONST               0 ('This style is not a fit for these leads.')

128           CALL                     2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180E8360, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 134>:
134           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('strategy_id')
              LOAD_GLOBAL              0 (str)
              LOAD_CONST               2 ('personality_id')
              LOAD_GLOBAL              0 (str)
              LOAD_CONST               3 ('return')
              LOAD_GLOBAL              0 (str)
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _use_title at 0x0000018C17FE1920, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 134>:
134           RESUME                   0

135           LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (personality_id, strategy_id)
              BUILD_TUPLE              2
              STORE_FAST               2 (pair)

136           LOAD_FAST_BORROW         2 (pair)
              LOAD_GLOBAL              0 (_USE_PAIR_TITLES)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       14 (to L1)
              NOT_TAKEN

137           LOAD_GLOBAL              0 (_USE_PAIR_TITLES)
              LOAD_FAST_BORROW         2 (pair)
              BINARY_OP               26 ([])
              RETURN_VALUE

138   L1:     LOAD_GLOBAL              2 (_USE_FALLBACK_BY_PERSONALITY)
              LOAD_ATTR                5 (get + NULL|self)

139           LOAD_FAST_BORROW         1 (personality_id)

140           LOAD_CONST               0 ('Use the ')
              LOAD_GLOBAL              7 (_pretty_strategy + NULL)
              LOAD_FAST_BORROW         0 (strategy_id)
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST               1 (' style for these leads.')
              BUILD_STRING             3

138           CALL                     2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 151>:
151           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('n')
              LOAD_GLOBAL              0 (int)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              2 (str)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _confidence_from_n at 0x0000018C18025030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 151>:
151           RESUME                   0

152           LOAD_FAST_BORROW         0 (n)
              LOAD_SMALL_INT           3
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

153           LOAD_CONST               1 ('high')
              RETURN_VALUE

154   L1:     LOAD_FAST_BORROW         0 (n)
              LOAD_SMALL_INT           2
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

155           LOAD_CONST               2 ('medium')
              RETURN_VALUE

156   L2:     LOAD_CONST               3 ('low')
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18053CF0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 159>:
159           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('strategy_id')
              LOAD_GLOBAL              0 (str)
              LOAD_CONST               2 ('personality_id')
              LOAD_GLOBAL              0 (str)
              LOAD_CONST               3 ('cell')
              LOAD_GLOBAL              2 (dict)
              LOAD_CONST               4 ('return')
              LOAD_GLOBAL              2 (dict)
              BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _avoid_recommendation at 0x0000018C17D8E300, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 159>:
159           RESUME                   0

160           LOAD_FAST_BORROW         2 (cell)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('pass_rate')
              LOAD_CONST               1 (0.0)
              CALL                     2
              STORE_FAST               3 (pass_rate)

161           LOAD_FAST_BORROW         2 (cell)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               2 ('booked_rate')
              LOAD_CONST               1 (0.0)
              CALL                     2
              STORE_FAST               4 (booked_rate)

162           LOAD_FAST_BORROW         2 (cell)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('n')
              LOAD_SMALL_INT           0
              CALL                     2
              STORE_FAST               5 (n)

164           LOAD_CONST               4 ('id')
              LOAD_CONST               5 ('avoid_')
              LOAD_FAST_BORROW         0 (strategy_id)
              FORMAT_SIMPLE
              LOAD_CONST               6 ('_')
              LOAD_FAST_BORROW         1 (personality_id)
              FORMAT_SIMPLE
              BUILD_STRING             4

165           LOAD_CONST               7 ('priority')
              LOAD_FAST_BORROW         3 (pass_rate)
              LOAD_CONST               1 (0.0)
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_CONST               8 ('high')
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               9 ('medium')

166   L2:     LOAD_CONST              10 ('audience')
              LOAD_CONST              11 ('broker')

167           LOAD_CONST              12 ('title')
              LOAD_GLOBAL              3 (_avoid_title + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (strategy_id, personality_id)
              CALL                     2

168           LOAD_CONST              13 ('insight')

169           LOAD_GLOBAL              5 (_pretty_personality + NULL)
              LOAD_FAST_BORROW         1 (personality_id)
              CALL                     1
              LOAD_ATTR                7 (capitalize + NULL|self)
              CALL                     0
              FORMAT_SIMPLE
              LOAD_CONST              14 (' leads completed ')

170           LOAD_FAST_BORROW         3 (pass_rate)
              LOAD_CONST              15 ('.0%')
              FORMAT_WITH_SPEC
              LOAD_CONST              16 (' of calls under ')

171           LOAD_GLOBAL              9 (_pretty_strategy + NULL)
              LOAD_FAST_BORROW         0 (strategy_id)
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              17 (' (out of ')
              LOAD_FAST_BORROW         5 (n)
              FORMAT_SIMPLE
              LOAD_CONST              18 (' call(s)).')

169           BUILD_STRING             8

173           LOAD_CONST              19 ('recommended_action')

174           LOAD_CONST              20 ('Route ')
              LOAD_GLOBAL              5 (_pretty_personality + NULL)
              LOAD_FAST_BORROW         1 (personality_id)
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              21 (' leads away from the ')

175           LOAD_GLOBAL              9 (_pretty_strategy + NULL)
              LOAD_FAST_BORROW         0 (strategy_id)
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              22 (' flow until the pattern improves.')

174           BUILD_STRING             5

177           LOAD_CONST              23 ('evidence')

178           LOAD_FAST_BORROW         5 (n)
              FORMAT_SIMPLE
              LOAD_CONST              24 (" simulated call(s) with personality '")
              LOAD_FAST_BORROW         1 (personality_id)
              FORMAT_SIMPLE
              LOAD_CONST              25 ("' under strategy '")

179           LOAD_FAST_BORROW         0 (strategy_id)
              FORMAT_SIMPLE
              LOAD_CONST              26 ("': pass ")
              LOAD_FAST_BORROW         3 (pass_rate)
              LOAD_CONST              15 ('.0%')
              FORMAT_WITH_SPEC
              LOAD_CONST              27 (', booked ')
              LOAD_FAST_BORROW         4 (booked_rate)
              LOAD_CONST              15 ('.0%')
              FORMAT_WITH_SPEC
              LOAD_CONST              28 ('.')

178           BUILD_STRING            10

181           LOAD_CONST              29 ('affected_personality')
              LOAD_FAST_BORROW         1 (personality_id)

182           LOAD_CONST              30 ('affected_strategy')
              LOAD_FAST_BORROW         0 (strategy_id)

183           LOAD_CONST              31 ('expected_impact')
              LOAD_CONST              32 ('Higher conversion rate for this personality bucket.')

184           LOAD_CONST              33 ('confidence')
              LOAD_GLOBAL             11 (_confidence_from_n + NULL)
              LOAD_FAST_BORROW         5 (n)
              CALL                     1

163           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18053750, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 188>:
188           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('strategy_id')
              LOAD_GLOBAL              0 (str)
              LOAD_CONST               2 ('personality_id')
              LOAD_GLOBAL              0 (str)
              LOAD_CONST               3 ('cell')
              LOAD_GLOBAL              2 (dict)
              LOAD_CONST               4 ('return')
              LOAD_GLOBAL              2 (dict)
              BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _use_recommendation at 0x0000018C17ECEB60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 188>:
188           RESUME                   0

189           LOAD_FAST_BORROW         2 (cell)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('pass_rate')
              LOAD_CONST               1 (0.0)
              CALL                     2
              STORE_FAST               3 (pass_rate)

190           LOAD_FAST_BORROW         2 (cell)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               2 ('booked_rate')
              LOAD_CONST               1 (0.0)
              CALL                     2
              STORE_FAST               4 (booked_rate)

191           LOAD_FAST_BORROW         2 (cell)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('n')
              LOAD_SMALL_INT           0
              CALL                     2
              STORE_FAST               5 (n)

193           LOAD_CONST               4 ('id')
              LOAD_CONST               5 ('use_')
              LOAD_FAST_BORROW         0 (strategy_id)
              FORMAT_SIMPLE
              LOAD_CONST               6 ('_for_')
              LOAD_FAST_BORROW         1 (personality_id)
              FORMAT_SIMPLE
              BUILD_STRING             4

194           LOAD_CONST               7 ('priority')
              LOAD_CONST               8 ('medium')

195           LOAD_CONST               9 ('audience')
              LOAD_CONST              10 ('broker')

196           LOAD_CONST              11 ('title')
              LOAD_GLOBAL              3 (_use_title + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (strategy_id, personality_id)
              CALL                     2

197           LOAD_CONST              12 ('insight')

198           LOAD_GLOBAL              5 (_pretty_personality + NULL)
              LOAD_FAST_BORROW         1 (personality_id)
              CALL                     1
              LOAD_ATTR                7 (capitalize + NULL|self)
              CALL                     0
              FORMAT_SIMPLE
              LOAD_CONST              13 (' leads completed ')

199           LOAD_FAST_BORROW         3 (pass_rate)
              LOAD_CONST              14 ('.0%')
              FORMAT_WITH_SPEC
              LOAD_CONST              15 (' of calls under ')

200           LOAD_GLOBAL              9 (_pretty_strategy + NULL)
              LOAD_FAST_BORROW         0 (strategy_id)
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              16 (' (out of ')
              LOAD_FAST_BORROW         5 (n)
              FORMAT_SIMPLE
              LOAD_CONST              17 (' call(s)).')

198           BUILD_STRING             8

202           LOAD_CONST              18 ('recommended_action')

203           LOAD_CONST              19 ('Prefer the ')
              LOAD_GLOBAL              9 (_pretty_strategy + NULL)
              LOAD_FAST_BORROW         0 (strategy_id)
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              20 (" flow when the lead profile looks like '")

204           LOAD_FAST_BORROW         1 (personality_id)
              FORMAT_SIMPLE
              LOAD_CONST              21 ("'.")

203           BUILD_STRING             5

206           LOAD_CONST              22 ('evidence')

207           LOAD_FAST_BORROW         5 (n)
              FORMAT_SIMPLE
              LOAD_CONST              23 (" simulated call(s) with personality '")
              LOAD_FAST_BORROW         1 (personality_id)
              FORMAT_SIMPLE
              LOAD_CONST              24 ("' under strategy '")

208           LOAD_FAST_BORROW         0 (strategy_id)
              FORMAT_SIMPLE
              LOAD_CONST              25 ("': pass ")
              LOAD_FAST_BORROW         3 (pass_rate)
              LOAD_CONST              14 ('.0%')
              FORMAT_WITH_SPEC
              LOAD_CONST              26 (', booked ')
              LOAD_FAST_BORROW         4 (booked_rate)
              LOAD_CONST              14 ('.0%')
              FORMAT_WITH_SPEC
              LOAD_CONST              27 ('.')

207           BUILD_STRING            10

210           LOAD_CONST              28 ('affected_personality')
              LOAD_FAST_BORROW         1 (personality_id)

211           LOAD_CONST              29 ('affected_strategy')
              LOAD_FAST_BORROW         0 (strategy_id)

212           LOAD_CONST              30 ('expected_impact')
              LOAD_CONST              31 ('Sustains the strong conversion pattern already observed.')

213           LOAD_CONST              32 ('confidence')
              LOAD_GLOBAL             11 (_confidence_from_n + NULL)
              LOAD_FAST_BORROW         5 (n)
              CALL                     1

192           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026130, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 217>:
217           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('avg_frustration')
              LOAD_GLOBAL              0 (float)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              2 (dict)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _high_frustration_recommendation at 0x0000018C180E8470, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 217>:
217           RESUME                   0

219           LOAD_CONST               0 ('id')
              LOAD_CONST               1 ('high_frustration')

220           LOAD_CONST               2 ('priority')
              LOAD_CONST               3 ('high')

221           LOAD_CONST               4 ('audience')
              LOAD_CONST               5 ('broker')

222           LOAD_CONST               6 ('title')
              LOAD_CONST               7 ('Calls are running hot — shorter answers will reduce friction.')

223           LOAD_CONST               8 ('insight')

224           LOAD_CONST               9 ('Across the run, leads accumulated meaningful frustration before the call ended. That signals tone or response length is fighting the lead, not the other way around.')

228           LOAD_CONST              10 ('recommended_action')

229           LOAD_CONST              11 ('Shorten PAS responses and soften the booking ask. Pilot a brief / consultative style and re-measure.')

232           LOAD_CONST              12 ('evidence')
              LOAD_CONST              13 ('Average frustration ')
              LOAD_FAST_BORROW         0 (avg_frustration)
              FORMAT_SIMPLE
              LOAD_CONST              14 (' across the matrix.')
              BUILD_STRING             3

233           LOAD_CONST              15 ('affected_personality')
              LOAD_CONST              16 (None)

234           LOAD_CONST              17 ('affected_strategy')
              LOAD_CONST              16 (None)

235           LOAD_CONST              18 ('expected_impact')
              LOAD_CONST              19 ('Lower mid-call drop-off, higher bookings.')

236           LOAD_CONST              20 ('confidence')
              LOAD_CONST              21 ('medium')

218           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026230, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 240>:
240           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('dropoff_rate')
              LOAD_GLOBAL              0 (float)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              2 (dict)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _high_dropoff_recommendation at 0x0000018C180E8580, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 240>:
240           RESUME                   0

242           LOAD_CONST               0 ('id')
              LOAD_CONST               1 ('high_dropoff')

243           LOAD_CONST               2 ('priority')
              LOAD_CONST               3 ('high')

244           LOAD_CONST               4 ('audience')
              LOAD_CONST               5 ('broker')

245           LOAD_CONST               6 ('title')
              LOAD_CONST               7 ('Leads are dropping mid-call — offer the callback option earlier.')

246           LOAD_CONST               8 ('insight')

247           LOAD_CONST               9 ('A significant share of calls ended with the lead simply disengaging. Most of those leads will respond to a callback if one is offered before they leave.')

251           LOAD_CONST              10 ('recommended_action')

252           LOAD_CONST              11 ('Move the callback offer earlier in the script and route busy / impatient leads to a callback flow by default.')

255           LOAD_CONST              12 ('evidence')
              LOAD_CONST              13 ('Drop-off rate ')
              LOAD_FAST_BORROW         0 (dropoff_rate)
              LOAD_CONST              14 ('.0%')
              FORMAT_WITH_SPEC
              LOAD_CONST              15 (' across the matrix.')
              BUILD_STRING             3

256           LOAD_CONST              16 ('affected_personality')
              LOAD_CONST              17 (None)

257           LOAD_CONST              18 ('affected_strategy')
              LOAD_CONST              17 (None)

258           LOAD_CONST              19 ('expected_impact')
              LOAD_CONST              20 ('Recover bookings that would otherwise be lost.')

259           LOAD_CONST              21 ('confidence')
              LOAD_CONST              22 ('medium')

241           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18053BD0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 263>:
263           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('tied_strategy_ids')
              LOAD_GLOBAL              0 (List)
              LOAD_GLOBAL              2 (str)
              BINARY_OP               26 ([])
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              4 (dict)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _tied_top_recommendation at 0x0000018C1802C9B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 263>:
263           RESUME                   0

265           LOAD_CONST               0 ('id')
              LOAD_CONST               1 ('top_tied_collect_more')

266           LOAD_CONST               2 ('priority')
              LOAD_CONST               3 ('low')

267           LOAD_CONST               4 ('audience')
              LOAD_CONST               5 ('operator')

268           LOAD_CONST               6 ('title')

269           LOAD_CONST               7 ('Top-performing styles are too close to call — gather more conversations before locking one in.')

272           LOAD_CONST               8 ('insight')

273           LOAD_CONST               9 ("Several styles are scoring identically. That usually means the current scenario set isn't broad enough to differentiate them.")

276           LOAD_CONST              10 ('recommended_action')

277           LOAD_CONST              11 ("Run more scenarios, especially for personality types that haven't been exercised yet, and re-run the matrix.")

280           LOAD_CONST              12 ('evidence')
              LOAD_CONST              13 ('Tied at the top: ')
              LOAD_CONST              14 (', ')
              LOAD_ATTR                1 (join + NULL|self)
              LOAD_FAST_BORROW         0 (tied_strategy_ids)
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              15 ('.')
              BUILD_STRING             3

281           LOAD_CONST              16 ('affected_personality')
              LOAD_CONST              17 (None)

282           LOAD_CONST              18 ('affected_strategy')
              LOAD_CONST              17 (None)

283           LOAD_CONST              19 ('expected_impact')
              LOAD_CONST              20 ('Higher confidence in the eventual winner.')

284           LOAD_CONST              21 ('confidence')
              LOAD_CONST              22 ('medium')

264           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 288>:
288           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_GLOBAL              0 (dict)
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _infra_only_recommendation at 0x0000018C180E8690, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 288>:
288           RESUME                   0

290           LOAD_CONST               0 ('id')
              LOAD_CONST               1 ('infra_ready_engine_inert')

291           LOAD_CONST               2 ('priority')
              LOAD_CONST               3 ('medium')

292           LOAD_CONST               4 ('audience')
              LOAD_CONST               5 ('system')

293           LOAD_CONST               6 ('title')

294           LOAD_CONST               7 ("Optimization infrastructure is ready, but call behaviour isn't yet using these styles.")

297           LOAD_CONST               8 ('insight')

298           LOAD_CONST               9 ('The matrix and metrics are wired end-to-end, but no strategy in this run actually changes how PAS speaks to a lead. Rankings are infrastructure-only.')

302           LOAD_CONST              10 ('recommended_action')

303           LOAD_CONST              11 ('Wire one strategy override (e.g. greeting tone or callback phrasing) into the engine, then re-run the matrix to see real outcome differences.')

307           LOAD_CONST              12 ('evidence')
              LOAD_CONST              13 ('No strategy in this matrix is engine-effective.')

308           LOAD_CONST              14 ('affected_personality')
              LOAD_CONST              15 (None)

309           LOAD_CONST              16 ('affected_strategy')
              LOAD_CONST              15 (None)

310           LOAD_CONST              17 ('expected_impact')
              LOAD_CONST              18 ('Unlocks the rest of the recommendation surface.')

311           LOAD_CONST              19 ('confidence')
              LOAD_CONST              20 ('high')

289           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026330, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 319>:
319           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('d')
              LOAD_GLOBAL              0 (dict)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              2 (bool)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _looks_like_report at 0x0000018C180E87A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 319>:
319           RESUME                   0

321           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (d)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        6 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('ranked_strategies')
              LOAD_FAST_BORROW         0 (d)
              CONTAINS_OP              0 (in)
      L1:     RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180533F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 324>:
324           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report_or_matrix')
              LOAD_GLOBAL              0 (dict)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              2 (List)
              LOAD_GLOBAL              0 (dict)
              BINARY_OP               26 ([])
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object generate_recommendations at 0x0000018C17E042A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 324>:
 324            RESUME                   0

 338            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (report_or_matrix)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 339            BUILD_LIST               0
                RETURN_VALUE

 341    L1:     LOAD_GLOBAL              5 (_looks_like_report + NULL)
                LOAD_FAST_BORROW         0 (report_or_matrix)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        4 (to L2)
                NOT_TAKEN

 342            LOAD_FAST                0 (report_or_matrix)
                STORE_FAST               1 (report)
                JUMP_FORWARD            11 (to L3)

 344    L2:     LOAD_GLOBAL              7 (generate_optimization_report + NULL)
                LOAD_FAST_BORROW         0 (report_or_matrix)
                CALL                     1
                STORE_FAST               1 (report)

 346    L3:     LOAD_FAST_BORROW         1 (report)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               1 ('metrics')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L4:     STORE_FAST               2 (metrics)

 350            LOAD_FAST_BORROW         2 (metrics)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               2 ('total_runs')
                LOAD_SMALL_INT           0
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN

 351            BUILD_LIST               0
                RETURN_VALUE

 353    L5:     LOAD_FAST_BORROW         1 (report)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               3 ('behavior_summary')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L6:     STORE_FAST               3 (behaviour)

 354            LOAD_FAST_BORROW         1 (report)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               4 ('personality_insights')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L7:     STORE_FAST               4 (personality_insights)

 355            LOAD_FAST_BORROW         2 (metrics)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               5 ('by_strategy_personality')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L8:     STORE_FAST               5 (cross)

 356            LOAD_FAST_BORROW         1 (report)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               6 ('ranked_strategies')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L9:     STORE_FAST               6 (ranked)

 357            LOAD_GLOBAL             11 (bool + NULL)
                LOAD_FAST_BORROW         1 (report)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               7 ('any_strategy_effective')
                CALL                     1
                CALL                     1
                STORE_FAST               7 (any_effective)

 359            BUILD_LIST               0
                STORE_FAST               8 (recs)

 363            LOAD_FAST_BORROW         7 (any_effective)
                TO_BOOL
                POP_JUMP_IF_TRUE        26 (to L10)
                NOT_TAKEN

 364            LOAD_FAST_BORROW         8 (recs)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_GLOBAL             15 (_infra_only_recommendation + NULL)
                CALL                     0
                CALL                     1
                POP_TOP

 375   L10:     LOAD_GLOBAL             17 (set + NULL)
                CALL                     0
                STORE_FAST               9 (seen_avoid)

 377            LOAD_FAST_BORROW         5 (cross)
                LOAD_ATTR               19 (items + NULL|self)
                CALL                     0
                GET_ITER
       L11:     FOR_ITER               110 (to L16)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  171 (sid, by_p)

 378            LOAD_FAST_BORROW        11 (by_p)
                LOAD_ATTR               19 (items + NULL|self)
                CALL                     0
                GET_ITER
       L12:     FOR_ITER                85 (to L15)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  205 (pid, cell)

 379            LOAD_FAST_BORROW        13 (cell)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               8 ('pass_rate')
                LOAD_CONST               9 (1.0)
                CALL                     2
                LOAD_CONST              10 (0.3)
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN
                JUMP_BACKWARD           30 (to L12)
       L13:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 172 (sid, pid)
                BUILD_TUPLE              2
                LOAD_FAST_BORROW         9 (seen_avoid)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           40 (to L12)

 380   L14:     LOAD_FAST_BORROW         8 (recs)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_GLOBAL             21 (_avoid_recommendation + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 172 (sid, pid)
                LOAD_FAST_BORROW        13 (cell)
                CALL                     3
                CALL                     1
                POP_TOP

 381            LOAD_FAST_BORROW         9 (seen_avoid)
                LOAD_ATTR               23 (add + NULL|self)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 172 (sid, pid)
                BUILD_TUPLE              2
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           87 (to L12)

 378   L15:     END_FOR
                POP_ITER
                JUMP_BACKWARD          112 (to L11)

 377   L16:     END_FOR
                POP_ITER

 384            BUILD_MAP                0
                STORE_FAST              14 (by_personality)

 385            LOAD_FAST_BORROW         5 (cross)
                LOAD_ATTR               19 (items + NULL|self)
                CALL                     0
                GET_ITER
       L17:     FOR_ITER                64 (to L20)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  171 (sid, by_p)

 386            LOAD_FAST_BORROW        11 (by_p)
                LOAD_ATTR               19 (items + NULL|self)
                CALL                     0
                GET_ITER
       L18:     FOR_ITER                39 (to L19)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  205 (pid, cell)

 387            LOAD_FAST_BORROW        14 (by_personality)
                LOAD_ATTR               25 (setdefault + NULL|self)
                LOAD_FAST_BORROW        12 (pid)
                BUILD_LIST               0
                CALL                     2
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 173 (sid, cell)
                BUILD_TUPLE              2
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           41 (to L18)

 386   L19:     END_FOR
                POP_ITER
                JUMP_BACKWARD           66 (to L17)

 385   L20:     END_FOR
                POP_ITER

 389            LOAD_FAST_BORROW        14 (by_personality)
                LOAD_ATTR               19 (items + NULL|self)
                CALL                     0
                GET_ITER
       L21:     FOR_ITER                89 (to L23)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  207 (pid, items)

 393            LOAD_FAST_BORROW        12 (pid)
                BUILD_TUPLE              1
                LOAD_CONST              11 (<code object _key at 0x0000018C17972550, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 393>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_FAST              16 (_key)

 402            LOAD_GLOBAL             27 (sorted + NULL)
                LOAD_FAST_BORROW        15 (items)
                LOAD_FAST_BORROW        16 (_key)
                LOAD_CONST              12 (('key',))
                CALL_KW                  2
                STORE_FAST              17 (ranked_items)

 403            LOAD_FAST_BORROW        17 (ranked_items)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                UNPACK_SEQUENCE          2
                STORE_FAST              18 (best_sid)
                STORE_FAST              19 (best_cell)

 404            LOAD_FAST_BORROW        19 (best_cell)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               8 ('pass_rate')
                LOAD_CONST              13 (0.0)
                CALL                     2
                LOAD_CONST              14 (0.9)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_TRUE         3 (to L22)
                NOT_TAKEN
                JUMP_BACKWARD           61 (to L21)

 405   L22:     LOAD_FAST_BORROW         8 (recs)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_GLOBAL             29 (_use_recommendation + NULL)
                LOAD_FAST_BORROW        18 (best_sid)
                LOAD_FAST_BORROW        12 (pid)
                LOAD_FAST_BORROW        19 (best_cell)
                CALL                     3
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           91 (to L21)

 389   L23:     END_FOR
                POP_ITER

 408            LOAD_FAST_BORROW         3 (behaviour)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              15 ('avg_frustration')
                LOAD_CONST              13 (0.0)
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L24)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              13 (0.0)
       L24:     STORE_FAST              20 (avg_frust)

 409            LOAD_FAST_BORROW        20 (avg_frust)
                LOAD_CONST              16 (0.4)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       27 (to L25)
                NOT_TAKEN

 410            LOAD_FAST_BORROW         8 (recs)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_GLOBAL             31 (_high_frustration_recommendation + NULL)
                LOAD_FAST_BORROW        20 (avg_frust)
                CALL                     1
                CALL                     1
                POP_TOP

 413   L25:     LOAD_FAST_BORROW         3 (behaviour)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              17 ('dropoff_rate')
                LOAD_CONST              13 (0.0)
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L26)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              13 (0.0)
       L26:     STORE_FAST              21 (dropoff)

 414            LOAD_FAST_BORROW        21 (dropoff)
                LOAD_CONST              18 (0.15)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       27 (to L27)
                NOT_TAKEN

 415            LOAD_FAST_BORROW         8 (recs)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_GLOBAL             33 (_high_dropoff_recommendation + NULL)
                LOAD_FAST_BORROW        21 (dropoff)
                CALL                     1
                CALL                     1
                POP_TOP

 418   L27:     LOAD_GLOBAL             35 (len + NULL)
                LOAD_FAST_BORROW         6 (ranked)
                CALL                     1
                LOAD_SMALL_INT           2
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE      164 (to L34)
                NOT_TAKEN
                LOAD_GLOBAL             37 (abs + NULL)
                LOAD_FAST_BORROW         6 (ranked)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_CONST              19 ('score')
                BINARY_OP               26 ([])
                LOAD_FAST_BORROW         6 (ranked)
                LOAD_SMALL_INT           1
                BINARY_OP               26 ([])
                LOAD_CONST              19 ('score')
                BINARY_OP               26 ([])
                BINARY_OP               10 (-)
                CALL                     1
                LOAD_CONST              20 (1e-06)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE      113 (to L34)
                NOT_TAKEN

 421            LOAD_FAST_BORROW         6 (ranked)
                GET_ITER

 419            LOAD_FAST_AND_CLEAR     22 (r)
                SWAP                     2
       L28:     BUILD_LIST               0
                SWAP                     2

 421   L29:     FOR_ITER                58 (to L32)
                STORE_FAST              22 (r)

 422            LOAD_GLOBAL             37 (abs + NULL)
                LOAD_FAST_BORROW        22 (r)
                LOAD_CONST              19 ('score')
                BINARY_OP               26 ([])
                LOAD_FAST_BORROW         6 (ranked)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_CONST              19 ('score')
                BINARY_OP               26 ([])
                BINARY_OP               10 (-)
                CALL                     1
                LOAD_CONST              20 (1e-06)
                COMPARE_OP              18 (bool(<))

 420   L30:     POP_JUMP_IF_TRUE         3 (to L31)
                NOT_TAKEN
                JUMP_BACKWARD           49 (to L29)
       L31:     LOAD_FAST_BORROW        22 (r)
                LOAD_CONST              21 ('strategy_id')
                BINARY_OP               26 ([])
                LIST_APPEND              2
                JUMP_BACKWARD           60 (to L29)

 421   L32:     END_FOR
                POP_ITER

 419   L33:     STORE_FAST              23 (tied_ids)
                STORE_FAST              22 (r)

 424            LOAD_GLOBAL             35 (len + NULL)
                LOAD_FAST_BORROW        23 (tied_ids)
                CALL                     1
                LOAD_SMALL_INT           2
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       27 (to L34)
                NOT_TAKEN

 425            LOAD_FAST_BORROW         8 (recs)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_GLOBAL             39 (_tied_top_recommendation + NULL)
                LOAD_FAST_BORROW        23 (tied_ids)
                CALL                     1
                CALL                     1
                POP_TOP

 428   L34:     LOAD_FAST_BORROW         8 (recs)
                LOAD_ATTR               41 (sort + NULL|self)
                LOAD_CONST              22 (<code object <lambda> at 0x0000018C18053990, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 428>)
                MAKE_FUNCTION
                LOAD_CONST              12 (('key',))
                CALL_KW                  1
                POP_TOP

 429            LOAD_FAST_BORROW         8 (recs)
                RETURN_VALUE

  --   L35:     SWAP                     2
                POP_TOP

 419            SWAP                     2
                STORE_FAST              22 (r)
                RERAISE                  0
ExceptionTable:
  L28 to L30 -> L35 [2]
  L31 to L33 -> L35 [2]

Disassembly of <code object _key at 0x0000018C17972550, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 393>:
393           RESUME                   0

394           LOAD_FAST_BORROW         0 (kv)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   35 (sid, cell)

395           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (_pid, sid)
              BUILD_TUPLE              2
              LOAD_GLOBAL              0 (_USE_PAIR_TITLES)
              CONTAINS_OP              0 (in)
              STORE_FAST               4 (has_specific)

397           LOAD_FAST_BORROW         3 (cell)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               0 ('pass_rate')
              LOAD_CONST               1 (0.0)
              CALL                     2
              UNARY_NEGATIVE

398           LOAD_FAST_BORROW         3 (cell)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               2 ('booked_rate')
              LOAD_CONST               1 (0.0)
              CALL                     2
              UNARY_NEGATIVE

399           LOAD_FAST_BORROW         4 (has_specific)
              TO_BOOL
              POP_JUMP_IF_FALSE        5 (to L1)
              NOT_TAKEN
              LOAD_SMALL_INT           0

400           LOAD_FAST_BORROW         2 (sid)

396           BUILD_TUPLE              4
              RETURN_VALUE

399   L1:     LOAD_SMALL_INT           1

400           LOAD_FAST_BORROW         2 (sid)

396           BUILD_TUPLE              4
              RETURN_VALUE

Disassembly of <code object <lambda> at 0x0000018C18053990, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 428>:
428           RESUME                   0
              LOAD_GLOBAL              0 (_PRIORITY_ORDER)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_FAST_BORROW         0 (r)
              LOAD_CONST               0 ('priority')
              BINARY_OP               26 ([])
              LOAD_SMALL_INT           3
              CALL                     2
              LOAD_FAST_BORROW         0 (r)
              LOAD_CONST               1 ('id')
              BINARY_OP               26 ([])
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180531B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 432>:
432           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendations')
              LOAD_GLOBAL              0 (List)
              LOAD_GLOBAL              2 (dict)
              BINARY_OP               26 ([])
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              4 (str)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object summarize_recommendations at 0x0000018C17CD1200, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 432>:
432           RESUME                   0

438           LOAD_FAST_BORROW         0 (recommendations)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

439           LOAD_CONST               1 ('No actionable recommendations from this batch.')
              RETURN_VALUE

441   L1:     BUILD_LIST               0
              STORE_FAST               1 (lines)

442           LOAD_GLOBAL              1 (enumerate + NULL)
              LOAD_FAST_BORROW         0 (recommendations)
              LOAD_SMALL_INT           1
              LOAD_CONST               2 (('start',))
              CALL_KW                  2
              GET_ITER
      L2:     FOR_ITER               168 (to L5)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   35 (i, r)

443           LOAD_FAST_BORROW         1 (lines)
              LOAD_ATTR                3 (append + NULL|self)
              LOAD_FAST_BORROW         2 (i)
              FORMAT_SIMPLE
              LOAD_CONST               3 ('. [')
              LOAD_FAST_BORROW         3 (r)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               4 ('priority')
              LOAD_CONST               5 ('?')
              CALL                     2
              LOAD_ATTR                7 (title + NULL|self)
              CALL                     0
              FORMAT_SIMPLE
              LOAD_CONST               6 ('] ')
              LOAD_FAST_BORROW         3 (r)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               7 ('title')
              LOAD_CONST               8 ('')
              CALL                     2
              FORMAT_SIMPLE
              BUILD_STRING             5
              CALL                     1
              POP_TOP

444           LOAD_FAST_BORROW         3 (r)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               9 ('recommended_action')
              CALL                     1
              STORE_FAST               4 (action)

445           LOAD_FAST_BORROW         4 (action)
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L3)
              NOT_TAKEN

446           LOAD_FAST_BORROW         1 (lines)
              LOAD_ATTR                3 (append + NULL|self)
              LOAD_CONST              10 ('   Action: ')
              LOAD_FAST_BORROW         4 (action)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP

447   L3:     LOAD_FAST_BORROW         3 (r)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST              11 ('evidence')
              CALL                     1
              STORE_FAST               5 (evidence)

448           LOAD_FAST_BORROW         5 (evidence)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD          148 (to L2)

449   L4:     LOAD_FAST_BORROW         1 (lines)
              LOAD_ATTR                3 (append + NULL|self)
              LOAD_CONST              12 ('   Evidence: ')
              LOAD_FAST_BORROW         5 (evidence)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          170 (to L2)

442   L5:     END_FOR
              POP_ITER

450           LOAD_CONST              13 ('\n')
              LOAD_ATTR                9 (join + NULL|self)
              LOAD_FAST_BORROW         1 (lines)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17F60830, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\optimization\recommendations.py", line 1>:
  1           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     BUILD_MAP                0

 38           LOAD_SMALL_INT           0
              LOAD_GLOBAL              0 (__conditional_annotations__)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       44 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              2 (Dict)
              LOAD_GLOBAL              4 (Tuple)
              LOAD_GLOBAL              6 (str)
              LOAD_GLOBAL              6 (str)
              BUILD_TUPLE              2
              BINARY_OP               26 ([])
              LOAD_GLOBAL              6 (str)
              BUILD_TUPLE              2
              BINARY_OP               26 ([])
              COPY                     2
              LOAD_CONST               1 ('_AVOID_PAIR_TITLES')

  1           STORE_SUBSCR

 61   L2:     LOAD_SMALL_INT           1
              LOAD_GLOBAL              0 (__conditional_annotations__)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       27 (to L3)
              NOT_TAKEN
              LOAD_GLOBAL              2 (Dict)
              LOAD_GLOBAL              6 (str)
              LOAD_GLOBAL              6 (str)
              BUILD_TUPLE              2
              BINARY_OP               26 ([])
              COPY                     2
              LOAD_CONST               2 ('_AVOID_FALLBACK_BY_PERSONALITY')

  1           STORE_SUBSCR

 75   L3:     LOAD_SMALL_INT           2
              LOAD_GLOBAL              0 (__conditional_annotations__)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       44 (to L4)
              NOT_TAKEN
              LOAD_GLOBAL              2 (Dict)
              LOAD_GLOBAL              4 (Tuple)
              LOAD_GLOBAL              6 (str)
              LOAD_GLOBAL              6 (str)
              BUILD_TUPLE              2
              BINARY_OP               26 ([])
              LOAD_GLOBAL              6 (str)
              BUILD_TUPLE              2
              BINARY_OP               26 ([])
              COPY                     2
              LOAD_CONST               3 ('_USE_PAIR_TITLES')

  1           STORE_SUBSCR

 98   L4:     LOAD_SMALL_INT           3
              LOAD_GLOBAL              0 (__conditional_annotations__)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       27 (to L5)
              NOT_TAKEN
              LOAD_GLOBAL              2 (Dict)
              LOAD_GLOBAL              6 (str)
              LOAD_GLOBAL              6 (str)
              BUILD_TUPLE              2
              BINARY_OP               26 ([])
              COPY                     2
              LOAD_CONST               4 ('_USE_FALLBACK_BY_PERSONALITY')

  1           STORE_SUBSCR
      L5:     RETURN_VALUE
```
