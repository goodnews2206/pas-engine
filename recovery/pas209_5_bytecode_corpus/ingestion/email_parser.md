# ingestion/email_parser

- **pyc:** `app\services\ingestion\__pycache__\email_parser.cpython-314.pyc`
- **expected source path (absent):** `app\services\ingestion/email_parser.py`
- **co_filename (from bytecode):** `app\services\ingestion\email_parser.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** ingestion

## Module docstring

```
PAS164 — Email lead parser.

Pure parsing layer that converts a brokerage lead-source email
(Zillow Premier Agent, Realtor.com, Facebook lead-form
notification, generic website / contact-form email, or any
other plain text email) into a structural lead dict suitable
for the PAS161 NormalizedLead pipeline.

Hard doctrine carried by every helper here:

* The parser is a pure function. It NEVER raises on malformed
  input. Every recoverable failure surfaces a structural
  envelope.
* The parser NEVER echoes the raw email body in errors,
  warnings, logs, or the returned dict. The body is read,
  trimmed to a hard cap, and then dropped — only the extracted
  fields survive.
* The parser NEVER returns ``raw_email`` / ``raw_body`` /
  ``full_email`` / ``transcript`` / ``subject`` / ``sender``
  keys.
* No Gmail / Google API import. No inbox traversal. The parser
  only sees what the caller hands in.
* No external vendor. No embeddings, no LLM, no vector store.
* ``brokerage_id`` is NEVER read from the email body — that
  comes from auth in the calling layer.

The output shape is always::

    {
      "status":         "ok" | "failed",
      "source":         "zillow" | "realtor" | "facebook"
                          | "website" | "generic_email",
      "lead":           dict | None,
      "call_eligible":  bool,
      "warnings":       [<structural tokens>],
      "errors":         [<structural tokens>],
    }

``call_eligible`` mirrors PAS161's "phone is required to dial"
rule: True only when a usable phone digit-set was extracted.
A parsed lead with email-only contact returns ``call_eligible
= False`` and surfaces ``email_lead_missing_phone`` so the
ingestion layer can decide whether to retain or drop it.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `logging`, `re`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_label_value_map`, `_cap_body`, `_ensure_text`, `_extract_lead_core`, `_first_alias`, `_looks_like_html`, `_normalise_intent`, `_sanitize_phone`, `_scan_budget`, `_scan_email`, `_scan_phone`, `_scrub_forbidden_keys`, `_split_full_name`, `_strip_html`, `_truncate_field`, `detect_email_lead_source`, `extract_lead_fields_from_email`, `parse_email_lead`

## Env-key candidates

`ALLOWED_EMAIL_LEAD_SOURCES`, `ALLOWED_EMAIL_METADATA_KEYS`, `FORBIDDEN_PARSER_OUTPUT_KEYS`

## String constants (redacted where noted)

- '\nPAS164 — Email lead parser.\n\nPure parsing layer that converts a brokerage lead-source email\n(Zillow Premier Agent, Realtor.com, Facebook lead-form\nnotification, generic website / contact-form email, or any\nother plain text email) into a structural lead dict suitable\nfor the PAS161 NormalizedLead pipeline.\n\nHard doctrine carried by every helper here:\n\n* The parser is a pure function. It NEVER raises on malformed\n  input. Every recoverable failure surfaces a structural\n  envelope.\n* The parser NEVER echoes the raw email body in errors,\n  warnings, logs, or the returned dict. The body is read,\n  trimmed to a hard cap, and then dropped — only the extracted\n  fields survive.\n* The parser NEVER returns ``raw_email`` / ``raw_body`` /\n  ``full_email`` / ``transcript`` / ``subject`` / ``sender``\n  keys.\n* No Gmail / Google API import. No inbox traversal. The parser\n  only sees what the caller hands in.\n* No external vendor. No embeddings, no LLM, no vector store.\n* ``brokerage_id`` is NEVER read from the email body — that\n  comes from auth in the calling layer.\n\nThe output shape is always::\n\n    {\n      "status":         "ok" | "failed",\n      "source":         "zillow" | "realtor" | "facebook"\n                          | "website" | "generic_email",\n      "lead":           dict | None,\n      "call_eligible":  bool,\n      "warnings":       [<structural tokens>],\n      "errors":         [<structural tokens>],\n    }\n\n``call_eligible`` mirrors PAS161\'s "phone is required to dial"\nrule: True only when a usable phone digit-set was extracted.\nA parsed lead with email-only contact returns ``call_eligible\n= False`` and surfaces ``email_lead_missing_phone`` so the\ningestion layer can decide whether to retain or drop it.\n'
- 'pas.ingestion.email_parser'
- 'Tuple[str, ...]'
- 'ALLOWED_EMAIL_LEAD_SOURCES'
- 'ALLOWED_EMAIL_METADATA_KEYS'
- 'FORBIDDEN_PARSER_OUTPUT_KEYS'
- 'Tuple[Tuple[str, Tuple[str, ...]], ...]'
- '_SOURCE_PATTERNS'
- '(?:\\+?1[\\s\\-.]?)?\\(?\\d{3}\\)?[\\s\\-.]?\\d{3}[\\s\\-.]?\\d{4}'
- '\\+\\d{1,3}[\\s\\-.]?\\d{3,}[\\s\\-.]?\\d{3,}'
- '[A-Za-z0-9._%+\\-]+@[A-Za-z0-9.\\-]+\\.[A-Za-z]{2,}'
- '\\$\\s?\\d{1,3}(?:[\\.,]\\d{3})*(?:k|K|m|M)?'
- '^[\\s>*\\-]*([A-Za-z][A-Za-z \\-/]{0,40}?)[\\s]*[:=][\\s]*(.*)$'
- '<(script|style)[^>]*>.*?</\\1>'
- '<[^>]+>'
- 'source_hint'
- 'subject'
- 'Optional[str]'
- 'sender'
- 'body'
- 'return'
- 'str'
- 'Best-effort lead-source classification.\n\nReturns one of ``ALLOWED_EMAIL_LEAD_SOURCES``. Falls back to\n``generic_email`` when no pattern matches. NEVER raises.\nNEVER echoes the input strings in logs.\n'
- 'generic_email'
- 'value'
- 'Any'
- 'Coerce ``value`` to a stripped string or None. NEVER raises.'
- 'utf-8'
- 'replace'
- 'Tuple[str, List[str]]'
- 'Return a body slice bounded by ``EMAIL_BODY_MAX_BYTES``.\n\nThe cap applies to BOTH bytes and chars (UTF-8 worst case\nexpands by 4x; we cap on chars after a safe approximation).\nReturns ``(capped_text, warnings)``. NEVER raises.\n'
- 'email_body_capped'
- 'ignore'
- 'Crude HTML stripper. NEVER raises.'
- '[\\t\\r\\f\\v]+'
- '[ ]{2,}'
- '_strip_html error type='
- 'warnings'
- 'List[str]'
- 'token'
- 'Truncate a free-text field to ``EMAIL_FIELD_MAX_CHARS``.'
- 'bool'
- '<br'
- '<html'
- 'Dict[str, str]'
- 'Walk the body line-by-line and build a label→value map for\n``Field: value`` pairs. Lower-cases labels; preserves value\ncasing. Later occurrences of the same label OVERWRITE earlier\nones — we trust the latest field in the email.\n\nBounded — only the first 1024 lines are processed.\n'
- 'label_map'
- 'aliases'
- 'full_name'
- 'Tuple[Optional[str], Optional[str]]'
- 'raw'
- 'Reduce ``raw`` to a normalised phone-shaped string or None.\n\nReturns the digits-only payload prefixed with ``+`` when we\ncan confidently shape it. Mirrors the simpler form of the\nPAS161 phone sanitizer; the PAS161 layer will re-normalise\nto E.164 before enqueuing. NEVER raises.\n'
- 'text'
- 'Scan free-form text for the first phone-shaped substring.\n\nPrefers an explicit ``+CC`` international number, falls back\nto a 10-digit US-shaped number. NEVER raises.\n'
- 'buy'
- 'buying'
- 'buyer'
- 'purchase'
- 'purchasing'
- 'sell'
- 'selling'
- 'seller'
- 'list'
- 'listing'
- 'rent'
- 'renting'
- 'renter'
- 'lease'
- 'leasing'
- 'body_text'
- 'source'
- 'Tuple[Dict[str, Any], List[str]]'
- 'Produce a structural lead dict from a (capped, HTML-stripped)\nbody plus the sender hint. Returns ``(lead_dict, warnings)``.\nNEVER raises.\n'
- 'name_truncated'
- 'email_truncated'
- 'property_address_truncated'
- 'city_truncated'
- 'state_truncated'
- 'budget_truncated'
- 'timeline_truncated'
- 'notes_truncated'
- 'metadata_truncated'
- 'lead_source'
- 'campaign'
- 'property_type'
- 'email_source'
- 'email:'
- 'first_name'
- 'last_name'
- 'phone'
- 'email'
- 'property_address'
- 'city'
- 'state'
- 'budget'
- 'timeline'
- 'notes'
- 'intent'
- 'raw_source_ref'
- 'metadata'
- 'lead'
- 'Dict[str, Any]'
- 'Belt-and-braces: strip any forbidden top-level key from\nthe lead dict. The builder never adds them, but a future\nregression that bypassed the builder cannot escape this.'
- 'Lower-level helper used by ``parse_email_lead``. Returns the\nsame envelope shape (``status`` / ``source`` / ``lead`` /\n``call_eligible`` / ``warnings`` / ``errors``).\n\nExposed publicly so an admin diagnostic can call it directly\nwithout going through the dict-vs-string normalisation in\n``parse_email_lead``. NEVER raises.\n'
- 'email_body_html_stripped'
- 'extract_lead_fields_from_email unexpected error type='
- 'status'
- 'failed'
- 'call_eligible'
- 'errors'
- 'parser_exception:'
- 'email_lead_no_contact'
- 'email_lead_missing_phone'
- 'raw_email'
- 'Parse a raw email payload into a structural lead dict.\n\n``raw_email`` may be:\n\n* a ``str`` — treated as the email body. ``subject`` and\n  ``sender`` are unknown (None).\n* a ``dict`` — read ``subject`` / ``sender`` / ``body``\n  keys (with a few common aliases). Anything else is\n  ignored. The dict is NOT echoed in the response.\n\nReturns the closed-shape envelope documented at module top.\nNEVER raises. NEVER echoes the raw body in errors.\n'
- 'Subject'
- 'from'
- 'From'
- 'body_plain'
- 'html'
- 'body_html'
- 'email_input_missing'
- 'email_input_unsupported_type'
- 'parse_email_lead input coercion failed type='
- 'email_input_empty'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS164 — Email lead parser.\n\nPure parsing layer that converts a brokerage lead-source email\n(Zillow Premier Agent, Realtor.com, Facebook lead-form\nnotification, generic website / contact-form email, or any\nother plain text email) into a structural lead dict suitable\nfor the PAS161 NormalizedLead pipeline.\n\nHard doctrine carried by every helper here:\n\n* The parser is a pure function. It NEVER raises on malformed\n  input. Every recoverable failure surfaces a structural\n  envelope.\n* The parser NEVER echoes the raw email body in errors,\n  warnings, logs, or the returned dict. The body is read,\n  trimmed to a hard cap, and then dropped — only the extracted\n  fields survive.\n* The parser NEVER returns ``raw_email`` / ``raw_body`` /\n  ``full_email`` / ``transcript`` / ``subject`` / ``sender``\n  keys.\n* No Gmail / Google API import. No inbox traversal. The parser\n  only sees what the caller hands in.\n* No external vendor. No embeddings, no LLM, no vector store.\n* ``brokerage_id`` is NEVER read from the email body — that\n  comes from auth in the calling layer.\n\nThe output shape is always::\n\n    {\n      "status":         "ok" | "failed",\n      "source":         "zillow" | "realtor" | "facebook"\n                          | "website" | "generic_email",\n      "lead":           dict | None,\n      "call_eligible":  bool,\n      "warnings":       [<structural tokens>],\n      "errors":         [<structural tokens>],\n    }\n\n``call_eligible`` mirrors PAS161\'s "phone is required to dial"\nrule: True only when a usable phone digit-set was extracted.\nA parsed lead with email-only contact returns ``call_eligible\n= False`` and surfaces ``email_lead_missing_phone`` so the\ningestion layer can decide whether to retain or drop it.\n')
               STORE_NAME               1 (__doc__)

  47           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  49           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  50           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (re)
               STORE_NAME               5 (re)

  51           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME              6 (typing)
               IMPORT_FROM              7 (Any)
               STORE_NAME               7 (Any)
               IMPORT_FROM              8 (Dict)
               STORE_NAME               8 (Dict)
               IMPORT_FROM              9 (List)
               STORE_NAME               9 (List)
               IMPORT_FROM             10 (Optional)
               STORE_NAME              10 (Optional)
               IMPORT_FROM             11 (Tuple)
               STORE_NAME              11 (Tuple)
               POP_TOP

  54           LOAD_NAME                4 (logging)
               LOAD_ATTR               24 (getLogger)
               PUSH_NULL
               LOAD_CONST               4 ('pas.ingestion.email_parser')
               CALL                     1
               STORE_NAME              13 (logger)

  64           LOAD_CONST              56 (('zillow', 'realtor', 'facebook', 'website', 'generic_email'))
               STORE_NAME              14 (ALLOWED_EMAIL_LEAD_SOURCES)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               15 (__annotations__)
               LOAD_CONST               6 ('ALLOWED_EMAIL_LEAD_SOURCES')
               STORE_SUBSCR

  76           LOAD_CONST              57 (('lead_source', 'campaign', 'property_type', 'email_source'))
               STORE_NAME              16 (ALLOWED_EMAIL_METADATA_KEYS)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               15 (__annotations__)
               LOAD_CONST               7 ('ALLOWED_EMAIL_METADATA_KEYS')
               STORE_SUBSCR

  89           LOAD_CONST              58 (('raw_email', 'raw_body', 'full_email', 'full_body', 'email_body', 'body', 'subject', 'sender', 'transcript', 'raw_transcript', 'full_transcript', 'raw_payload', 'full_payload', 'messages', 'utterances', 'input_text', 'output_text', 'memory_content', 'raw_text', 'raw_prompt', 'injected_prompt', 'brokerage_id', 'api_key', 'X-API-Key'))
               STORE_NAME              17 (FORBIDDEN_PARSER_OUTPUT_KEYS)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               15 (__annotations__)
               LOAD_CONST               8 ('FORBIDDEN_PARSER_OUTPUT_KEYS')
               STORE_SUBSCR

 123           LOAD_CONST              59 (65536)
               STORE_NAME              18 (EMAIL_BODY_MAX_BYTES)

 128           LOAD_CONST               9 (256)
               STORE_NAME              19 (EMAIL_FIELD_MAX_CHARS)

 138           LOAD_CONST              60 ((('zillow', ('zillow.com', 'premieragent.zillow', 'premier agent', 'new lead from zillow', '@zillow.', 'zillowgroup.com')), ('realtor', ('realtor.com', '@realtor.', 'move.com', 'new lead from realtor', 'opcity')), ('facebook', ('facebook.com', '@fb.com', '@facebookmail.com', 'facebook lead', 'lead form', 'lead ad', 'instant form')), ('website', ('contact form', 'website lead', 'from your website', 'new website inquiry', 'contact-form', 'wpforms', 'gravity forms'))))
               STORE_NAME              20 (_SOURCE_PATTERNS)
               LOAD_CONST              10 ('Tuple[Tuple[str, Tuple[str, ...]], ...]')
               LOAD_NAME               15 (__annotations__)
               LOAD_CONST              11 ('_SOURCE_PATTERNS')
               STORE_SUBSCR

 175           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C18025630, file "app\services\ingestion\email_parser.py", line 175>)
               MAKE_FUNCTION
               LOAD_CONST              13 (<code object detect_email_lead_source at 0x0000018C1801C9E0, file "app\services\ingestion\email_parser.py", line 175>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              21 (detect_email_lead_source)

 208           LOAD_NAME                5 (re)
               LOAD_ATTR               44 (compile)
               PUSH_NULL

 209           LOAD_CONST              14 ('(?:\\+?1[\\s\\-.]?)?\\(?\\d{3}\\)?[\\s\\-.]?\\d{3}[\\s\\-.]?\\d{4}')

 208           CALL                     1
               STORE_NAME              23 (_PHONE_RE)

 211           LOAD_NAME                5 (re)
               LOAD_ATTR               44 (compile)
               PUSH_NULL
               LOAD_CONST              15 ('\\+\\d{1,3}[\\s\\-.]?\\d{3,}[\\s\\-.]?\\d{3,}')
               CALL                     1
               STORE_NAME              24 (_INTL_PHONE_RE)

 212           LOAD_NAME                5 (re)
               LOAD_ATTR               44 (compile)
               PUSH_NULL

 213           LOAD_CONST              16 ('[A-Za-z0-9._%+\\-]+@[A-Za-z0-9.\\-]+\\.[A-Za-z]{2,}')

 212           CALL                     1
               STORE_NAME              25 (_EMAIL_RE)

 215           LOAD_NAME                5 (re)
               LOAD_ATTR               44 (compile)
               PUSH_NULL

 216           LOAD_CONST              17 ('\\$\\s?\\d{1,3}(?:[\\.,]\\d{3})*(?:k|K|m|M)?')

 215           CALL                     1
               STORE_NAME              26 (_BUDGET_RE)

 224           LOAD_NAME                5 (re)
               LOAD_ATTR               44 (compile)
               PUSH_NULL

 225           LOAD_CONST              18 ('^[\\s>*\\-]*([A-Za-z][A-Za-z \\-/]{0,40}?)[\\s]*[:=][\\s]*(.*)$')

 226           LOAD_NAME                5 (re)
               LOAD_ATTR               54 (MULTILINE)

 224           CALL                     2
               STORE_NAME              28 (_LABEL_VALUE_RE)

 233           LOAD_NAME                5 (re)
               LOAD_ATTR               44 (compile)
               PUSH_NULL

 234           LOAD_CONST              19 ('<(script|style)[^>]*>.*?</\\1>')

 235           LOAD_NAME                5 (re)
               LOAD_ATTR               58 (DOTALL)
               LOAD_NAME                5 (re)
               LOAD_ATTR               60 (IGNORECASE)
               BINARY_OP                7 (|)

 233           CALL                     2
               STORE_NAME              31 (_HTML_SCRIPT_STYLE_RE)

 237           LOAD_NAME                5 (re)
               LOAD_ATTR               44 (compile)
               PUSH_NULL
               LOAD_CONST              20 ('<[^>]+>')
               CALL                     1
               STORE_NAME              32 (_HTML_TAG_RE)

 238           LOAD_CONST              61 ((('&nbsp;', ' '), ('&amp;', '&'), ('&lt;', '<'), ('&gt;', '>'), ('&quot;', '"'), ('&#39;', "'"), ('&apos;', "'")))
               STORE_NAME              33 (_HTML_ENTITIES)

 246           LOAD_CONST              62 (('name', 'full name', 'lead name', 'contact name', 'client name', 'from'))
               STORE_NAME              34 (_ALIAS_NAME)

 250           LOAD_CONST              63 (('first name', 'given name', 'firstname'))
               STORE_NAME              35 (_ALIAS_FIRST_NAME)

 251           LOAD_CONST              64 (('last name', 'surname', 'family name', 'lastname'))
               STORE_NAME              36 (_ALIAS_LAST_NAME)

 252           LOAD_CONST              65 (('phone', 'phone number', 'mobile', 'mobile phone', 'contact number', 'best phone', 'cell', 'cell phone', 'telephone'))
               STORE_NAME              37 (_ALIAS_PHONE)

 257           LOAD_CONST              66 (('email', 'email address', 'e-mail', 'best email'))
               STORE_NAME              38 (_ALIAS_EMAIL)

 260           LOAD_CONST              67 (('property address', 'property', 'address', 'listing address', 'subject property', 'home of interest', 'interested in'))
               STORE_NAME              39 (_ALIAS_PROPERTY)

 264           LOAD_CONST              68 (('city', 'town'))
               STORE_NAME              40 (_ALIAS_CITY)

 265           LOAD_CONST              69 (('state', 'region', 'province'))
               STORE_NAME              41 (_ALIAS_STATE)

 266           LOAD_CONST              70 (('budget', 'price', 'price range', 'max price', 'max budget', 'purchase price'))
               STORE_NAME              42 (_ALIAS_BUDGET)

 270           LOAD_CONST              71 (('timeline', 'timeframe', 'move in date', 'move-in date', 'moving in', 'buy timeframe', 'when'))
               STORE_NAME              43 (_ALIAS_TIMELINE)

 274           LOAD_CONST              72 (('notes', 'note', 'comments', 'comment', 'message', 'additional information', 'more info', 'additional notes'))
               STORE_NAME              44 (_ALIAS_NOTES)

 278           LOAD_CONST              73 (('intent', 'transaction type', 'deal type', 'type', 'looking to', 'i want to'))
               STORE_NAME              45 (_ALIAS_INTENT)

 282           LOAD_CONST              74 (('lead source', 'source', 'from'))
               STORE_NAME              46 (_ALIAS_LEAD_SOURCE)

 285           LOAD_CONST              75 (('campaign', 'ad campaign'))
               STORE_NAME              47 (_ALIAS_CAMPAIGN)

 288           LOAD_CONST              76 (('property type', 'home type'))
               STORE_NAME              48 (_ALIAS_PROPERTY_TYPE)

 297           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA33C0, file "app\services\ingestion\email_parser.py", line 297>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object _ensure_text at 0x0000018C17D8E300, file "app\services\ingestion\email_parser.py", line 297>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (_ensure_text)

 319           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\ingestion\email_parser.py", line 319>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object _cap_body at 0x0000018C17F0C960, file "app\services\ingestion\email_parser.py", line 319>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (_cap_body)

 349           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA3B40, file "app\services\ingestion\email_parser.py", line 349>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object _strip_html at 0x0000018C17CC1F60, file "app\services\ingestion\email_parser.py", line 349>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (_strip_html)

 369           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\ingestion\email_parser.py", line 369>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object _truncate_field at 0x0000018C17972D90, file "app\services\ingestion\email_parser.py", line 369>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (_truncate_field)

 379           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA3C30, file "app\services\ingestion\email_parser.py", line 379>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object _looks_like_html at 0x0000018C17FF0C30, file "app\services\ingestion\email_parser.py", line 379>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (_looks_like_html)

 386           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA3780, file "app\services\ingestion\email_parser.py", line 386>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object _build_label_value_map at 0x0000018C17CC2960, file "app\services\ingestion\email_parser.py", line 386>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (_build_label_value_map)

 418           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C18025A30, file "app\services\ingestion\email_parser.py", line 418>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object _first_alias at 0x0000018C18038B70, file "app\services\ingestion\email_parser.py", line 418>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (_first_alias)

 428           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C17FA3960, file "app\services\ingestion\email_parser.py", line 428>)
               MAKE_FUNCTION
               LOAD_CONST              36 (<code object _split_full_name at 0x0000018C18060390, file "app\services\ingestion\email_parser.py", line 428>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (_split_full_name)

 439           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C17FA3A50, file "app\services\ingestion\email_parser.py", line 439>)
               MAKE_FUNCTION
               LOAD_CONST              38 (<code object _sanitize_phone at 0x0000018C17D44220, file "app\services\ingestion\email_parser.py", line 439>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (_sanitize_phone)

 473           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C17FA2D30, file "app\services\ingestion\email_parser.py", line 473>)
               MAKE_FUNCTION
               LOAD_CONST              40 (<code object _scan_phone at 0x0000018C1794ED80, file "app\services\ingestion\email_parser.py", line 473>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (_scan_phone)

 490           LOAD_CONST              41 (<code object __annotate__ at 0x0000018C17FA2E20, file "app\services\ingestion\email_parser.py", line 490>)
               MAKE_FUNCTION
               LOAD_CONST              42 (<code object _scan_email at 0x0000018C17FE17D0, file "app\services\ingestion\email_parser.py", line 490>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (_scan_email)

 497           LOAD_CONST              43 (<code object __annotate__ at 0x0000018C17FA2F10, file "app\services\ingestion\email_parser.py", line 497>)
               MAKE_FUNCTION
               LOAD_CONST              44 (<code object _scan_budget at 0x0000018C17F95E60, file "app\services\ingestion\email_parser.py", line 497>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (_scan_budget)

 506           LOAD_CONST              45 (<code object __annotate__ at 0x0000018C17FA3D20, file "app\services\ingestion\email_parser.py", line 506>)
               MAKE_FUNCTION
               LOAD_CONST              46 (<code object _normalise_intent at 0x0000018C179C3A50, file "app\services\ingestion\email_parser.py", line 506>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (_normalise_intent)

 531           LOAD_CONST              47 (<code object __annotate__ at 0x0000018C18024930, file "app\services\ingestion\email_parser.py", line 531>)
               MAKE_FUNCTION
               LOAD_CONST              48 (<code object _extract_lead_core at 0x0000018C17ED7C70, file "app\services\ingestion\email_parser.py", line 531>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (_extract_lead_core)

 650           LOAD_CONST              49 (<code object __annotate__ at 0x0000018C17FA3F00, file "app\services\ingestion\email_parser.py", line 650>)
               MAKE_FUNCTION
               LOAD_CONST              50 (<code object _scrub_forbidden_keys at 0x0000018C17ED8340, file "app\services\ingestion\email_parser.py", line 650>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (_scrub_forbidden_keys)

 674           LOAD_CONST              77 ((None,))
               LOAD_CONST              51 (<code object __annotate__ at 0x0000018C18025730, file "app\services\ingestion\email_parser.py", line 674>)
               MAKE_FUNCTION
               LOAD_CONST              52 (<code object extract_lead_fields_from_email at 0x0000018C17D465D0, file "app\services\ingestion\email_parser.py", line 674>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              64 (extract_lead_fields_from_email)

 763           LOAD_CONST              53 ('source_hint')

 766           LOAD_CONST               2 (None)

 763           BUILD_MAP                1
               LOAD_CONST              54 (<code object __annotate__ at 0x0000018C18025330, file "app\services\ingestion\email_parser.py", line 763>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object parse_email_lead at 0x0000018C17ED1120, file "app\services\ingestion\email_parser.py", line 763>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              65 (parse_email_lead)

 864           BUILD_LIST               0
               LOAD_CONST              78 (('ALLOWED_EMAIL_LEAD_SOURCES', 'ALLOWED_EMAIL_METADATA_KEYS', 'FORBIDDEN_PARSER_OUTPUT_KEYS', 'EMAIL_BODY_MAX_BYTES', 'EMAIL_FIELD_MAX_CHARS', 'detect_email_lead_source', 'extract_lead_fields_from_email', 'parse_email_lead'))
               LIST_EXTEND              1
               STORE_NAME              66 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025630, file "app\services\ingestion\email_parser.py", line 175>:
175           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('subject')

176           LOAD_CONST               2 ('Optional[str]')

175           LOAD_CONST               3 ('sender')

177           LOAD_CONST               2 ('Optional[str]')

175           LOAD_CONST               4 ('body')

178           LOAD_CONST               2 ('Optional[str]')

175           LOAD_CONST               5 ('return')

179           LOAD_CONST               6 ('str')

175           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object detect_email_lead_source at 0x0000018C1801C9E0, file "app\services\ingestion\email_parser.py", line 175>:
175            RESUME                   0

186            BUILD_LIST               0
               STORE_FAST               3 (haystack_parts)

187            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (subject, sender)
               LOAD_FAST_BORROW         2 (body)
               BUILD_TUPLE              3
               GET_ITER
       L1:     FOR_ITER                68 (to L4)
               STORE_FAST               4 (v)

188            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         4 (v)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               JUMP_BACKWARD           27 (to L1)
       L2:     LOAD_FAST_BORROW         4 (v)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               JUMP_BACKWARD           37 (to L1)

189    L3:     LOAD_FAST_BORROW         3 (haystack_parts)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_FAST_BORROW         4 (v)
               LOAD_ATTR                7 (lower + NULL|self)
               CALL                     0
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           70 (to L1)

187    L4:     END_FOR
               POP_ITER

190            LOAD_FAST_BORROW         3 (haystack_parts)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN

191            LOAD_CONST               1 ('generic_email')
               RETURN_VALUE

192    L5:     LOAD_CONST               2 ('\n')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         3 (haystack_parts)
               CALL                     1
               STORE_FAST               5 (haystack)

193            LOAD_GLOBAL             10 (_SOURCE_PATTERNS)
               GET_ITER
       L6:     FOR_ITER                26 (to L10)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST  103 (source, patterns)

194            LOAD_FAST_BORROW         7 (patterns)
               GET_ITER
       L7:     FOR_ITER                15 (to L9)
               STORE_FAST               8 (p)

195            LOAD_FAST_BORROW_LOAD_FAST_BORROW 133 (p, haystack)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L7)

196    L8:     LOAD_FAST_BORROW         6 (source)
               SWAP                     2
               POP_TOP
               SWAP                     2
               POP_TOP
               RETURN_VALUE

194    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD           28 (to L6)

193   L10:     END_FOR
               POP_ITER

197            LOAD_CONST               1 ('generic_email')
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app\services\ingestion\email_parser.py", line 297>:
297           RESUME                   0
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
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _ensure_text at 0x0000018C17D8E300, file "app\services\ingestion\email_parser.py", line 297>:
 297            RESUME                   0

 299            LOAD_FAST_BORROW         0 (value)
                POP_JUMP_IF_NOT_NONE     3 (to L1)
                NOT_TAKEN

 300            LOAD_CONST               1 (None)
                RETURN_VALUE

 301    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL              2 (bool)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN

 302            LOAD_CONST               1 (None)
                RETURN_VALUE

 303    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL              4 (int)
                LOAD_GLOBAL              6 (float)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L5)
                NOT_TAKEN

 304            NOP

 305    L3:     LOAD_GLOBAL              9 (str + NULL)
                LOAD_FAST_BORROW         0 (value)
                CALL                     1
        L4:     RETURN_VALUE

 308    L5:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL             12 (bytes)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       21 (to L7)
                NOT_TAKEN

 309            NOP

 310    L6:     LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR               15 (decode + NULL|self)
                LOAD_CONST               2 ('utf-8')
                LOAD_CONST               3 ('replace')
                LOAD_CONST               4 (('errors',))
                CALL_KW                  2
                STORE_FAST               0 (value)

 313    L7:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN

 314            LOAD_CONST               1 (None)
                RETURN_VALUE

 315    L8:     LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR               17 (strip + NULL|self)
                CALL                     0
                STORE_FAST               1 (s)

 316            LOAD_FAST                1 (s)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               1 (None)
        L9:     RETURN_VALUE

  --   L10:     PUSH_EXC_INFO

 306            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L12)
                NOT_TAKEN
                POP_TOP

 307   L11:     POP_EXCEPT
                LOAD_CONST               1 (None)
                RETURN_VALUE

 306   L12:     RERAISE                  0

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L14:     PUSH_EXC_INFO

 311            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L16)
                NOT_TAKEN
                POP_TOP

 312   L15:     POP_EXCEPT
                LOAD_CONST               1 (None)
                RETURN_VALUE

 311   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L10 [0]
  L6 to L7 -> L14 [0]
  L10 to L11 -> L13 [1] lasti
  L12 to L13 -> L13 [1] lasti
  L14 to L15 -> L17 [1] lasti
  L16 to L17 -> L17 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\ingestion\email_parser.py", line 319>:
319           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Tuple[str, List[str]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _cap_body at 0x0000018C17F0C960, file "app\services\ingestion\email_parser.py", line 319>:
319           RESUME                   0

326           BUILD_LIST               0
              STORE_FAST               1 (warnings)

327           LOAD_GLOBAL              1 (_ensure_text + NULL)
              LOAD_FAST_BORROW         0 (body)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     STORE_FAST               2 (s)

328           LOAD_FAST_BORROW         2 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         5 (to L2)
              NOT_TAKEN

329           LOAD_CONST               1 ('')
              LOAD_FAST_BORROW         1 (warnings)
              BUILD_TUPLE              2
              RETURN_VALUE

334   L2:     LOAD_GLOBAL              2 (EMAIL_BODY_MAX_BYTES)
              STORE_FAST               3 (char_cap)

335           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         2 (s)
              CALL                     1
              LOAD_FAST_BORROW         3 (char_cap)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       23 (to L3)
              NOT_TAKEN

336           LOAD_FAST_BORROW         2 (s)
              LOAD_CONST               2 (None)
              LOAD_FAST_BORROW         3 (char_cap)
              BINARY_SLICE
              STORE_FAST               2 (s)

337           LOAD_FAST_BORROW         1 (warnings)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               3 ('email_body_capped')
              CALL                     1
              POP_TOP

338   L3:     LOAD_FAST_BORROW         2 (s)
              LOAD_ATTR                9 (encode + NULL|self)
              LOAD_CONST               4 ('utf-8')
              LOAD_CONST               5 ('replace')
              LOAD_CONST               6 (('errors',))
              CALL_KW                  2
              STORE_FAST               4 (encoded)

339           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         4 (encoded)
              CALL                     1
              LOAD_GLOBAL              2 (EMAIL_BODY_MAX_BYTES)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       51 (to L4)
              NOT_TAKEN

341           LOAD_FAST_BORROW         4 (encoded)
              LOAD_CONST               2 (None)
              LOAD_GLOBAL              2 (EMAIL_BODY_MAX_BYTES)
              BINARY_SLICE
              LOAD_ATTR               11 (decode + NULL|self)

342           LOAD_CONST               4 ('utf-8')
              LOAD_CONST               7 ('ignore')

341           LOAD_CONST               6 (('errors',))
              CALL_KW                  2
              STORE_FAST               2 (s)

344           LOAD_CONST               3 ('email_body_capped')
              LOAD_FAST_BORROW         1 (warnings)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       18 (to L4)
              NOT_TAKEN

345           LOAD_FAST_BORROW         1 (warnings)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               3 ('email_body_capped')
              CALL                     1
              POP_TOP

346   L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (s, warnings)
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app\services\ingestion\email_parser.py", line 349>:
349           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _strip_html at 0x0000018C17CC1F60, file "app\services\ingestion\email_parser.py", line 349>:
 349            RESUME                   0

 351            LOAD_FAST_BORROW         0 (body)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 352            LOAD_CONST               1 ('')
                RETURN_VALUE

 353    L1:     NOP

 354    L2:     LOAD_GLOBAL              0 (_HTML_SCRIPT_STYLE_RE)
                LOAD_ATTR                3 (sub + NULL|self)
                LOAD_CONST               2 (' ')
                LOAD_FAST_BORROW         0 (body)
                CALL                     2
                STORE_FAST               1 (cleaned)

 355            LOAD_GLOBAL              4 (_HTML_TAG_RE)
                LOAD_ATTR                3 (sub + NULL|self)
                LOAD_CONST               2 (' ')
                LOAD_FAST_BORROW         1 (cleaned)
                CALL                     2
                STORE_FAST               1 (cleaned)

 356            LOAD_GLOBAL              6 (_HTML_ENTITIES)
                GET_ITER
        L3:     FOR_ITER                22 (to L4)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   35 (entity, replacement)

 357            LOAD_FAST_BORROW         1 (cleaned)
                LOAD_ATTR                9 (replace + NULL|self)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (entity, replacement)
                CALL                     2
                STORE_FAST               1 (cleaned)
                JUMP_BACKWARD           24 (to L3)

 356    L4:     END_FOR
                POP_ITER

 361            LOAD_GLOBAL             10 (re)
                LOAD_ATTR                2 (sub)
                PUSH_NULL
                LOAD_CONST               3 ('[\\t\\r\\f\\v]+')
                LOAD_CONST               2 (' ')
                LOAD_FAST_BORROW         1 (cleaned)
                CALL                     3
                STORE_FAST               1 (cleaned)

 362            LOAD_GLOBAL             10 (re)
                LOAD_ATTR                2 (sub)
                PUSH_NULL
                LOAD_CONST               4 ('[ ]{2,}')
                LOAD_CONST               2 (' ')
                LOAD_FAST_BORROW         1 (cleaned)
                CALL                     3
                STORE_FAST               1 (cleaned)

 363            LOAD_FAST_BORROW         1 (cleaned)
        L5:     RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 364            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       56 (to L11)
                NOT_TAKEN
                STORE_FAST               4 (e)

 365    L7:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (debug + NULL|self)
                LOAD_CONST               5 ('_strip_html error type=')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 366            LOAD_FAST                0 (body)
        L8:     SWAP                     2
        L9:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RETURN_VALUE

  --   L10:     LOAD_CONST               6 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 364   L11:     RERAISE                  0

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L5 -> L6 [0]
  L6 to L7 -> L12 [1] lasti
  L7 to L8 -> L10 [1] lasti
  L8 to L9 -> L12 [1] lasti
  L10 to L12 -> L12 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\ingestion\email_parser.py", line 369>:
369           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Optional[str]')
              LOAD_CONST               3 ('warnings')
              LOAD_CONST               4 ('List[str]')
              LOAD_CONST               5 ('token')
              LOAD_CONST               6 ('str')
              LOAD_CONST               7 ('return')
              LOAD_CONST               2 ('Optional[str]')
              BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _truncate_field at 0x0000018C17972D90, file "app\services\ingestion\email_parser.py", line 369>:
369           RESUME                   0

371           LOAD_FAST_BORROW         0 (value)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

372           LOAD_CONST               1 (None)
              RETURN_VALUE

373   L1:     LOAD_GLOBAL              1 (len + NULL)
              LOAD_FAST_BORROW         0 (value)
              CALL                     1
              LOAD_GLOBAL              2 (EMAIL_FIELD_MAX_CHARS)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       41 (to L2)
              NOT_TAKEN

374           LOAD_FAST_BORROW         1 (warnings)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW         2 (token)
              CALL                     1
              POP_TOP

375           LOAD_FAST_BORROW         0 (value)
              LOAD_CONST               1 (None)
              LOAD_GLOBAL              2 (EMAIL_FIELD_MAX_CHARS)
              BINARY_SLICE
              LOAD_ATTR                7 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

376   L2:     LOAD_FAST_BORROW         0 (value)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app\services\ingestion\email_parser.py", line 379>:
379           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _looks_like_html at 0x0000018C17FF0C30, file "app\services\ingestion\email_parser.py", line 379>:
379           RESUME                   0

380           LOAD_GLOBAL              1 (_ensure_text + NULL)
              LOAD_FAST_BORROW         0 (body)
              CALL                     1
              STORE_FAST               1 (s)

381           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

382           LOAD_CONST               0 (False)
              RETURN_VALUE

383   L1:     LOAD_CONST               1 ('</')
              LOAD_FAST_BORROW         1 (s)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE        47 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('<br')
              LOAD_FAST_BORROW         1 (s)
              LOAD_ATTR                3 (lower + NULL|self)
              CALL                     0
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE        20 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               3 ('<html')
              LOAD_FAST_BORROW         1 (s)
              LOAD_ATTR                3 (lower + NULL|self)
              CALL                     0
              CONTAINS_OP              0 (in)
      L2:     RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app\services\ingestion\email_parser.py", line 386>:
386           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _build_label_value_map at 0x0000018C17CC2960, file "app\services\ingestion\email_parser.py", line 386>:
386            RESUME                   0

394            BUILD_MAP                0
               STORE_FAST               1 (out)

395            LOAD_FAST_BORROW         0 (body)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

396            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

397    L1:     LOAD_SMALL_INT           0
               STORE_FAST               2 (line_count)

398            LOAD_GLOBAL              0 (_LABEL_VALUE_RE)
               LOAD_ATTR                3 (finditer + NULL|self)
               LOAD_FAST_BORROW         0 (body)
               CALL                     1
               GET_ITER
       L2:     FOR_ITER               167 (to L10)
               STORE_FAST               3 (match)

399            LOAD_FAST_BORROW         2 (line_count)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (line_count)

400            LOAD_FAST_BORROW         2 (line_count)
               LOAD_CONST               1 (1024)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        4 (to L3)
               NOT_TAKEN

401            POP_TOP

415            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

402    L3:     LOAD_FAST_BORROW         3 (match)
               LOAD_ATTR                5 (group + NULL|self)
               LOAD_SMALL_INT           1
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L4:     LOAD_ATTR                7 (strip + NULL|self)
               CALL                     0
               LOAD_ATTR                9 (lower + NULL|self)
               CALL                     0
               STORE_FAST               4 (label)

403            LOAD_FAST_BORROW         3 (match)
               LOAD_ATTR                5 (group + NULL|self)
               LOAD_SMALL_INT           2
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L5:     LOAD_ATTR                7 (strip + NULL|self)
               CALL                     0
               STORE_FAST               5 (value)

404            LOAD_FAST_BORROW         4 (label)
               TO_BOOL
               POP_JUMP_IF_FALSE        9 (to L6)
               NOT_TAKEN
               LOAD_FAST_BORROW         5 (value)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L7)
               NOT_TAKEN

405    L6:     JUMP_BACKWARD          136 (to L2)

408    L7:     LOAD_GLOBAL             11 (len + NULL)
               LOAD_FAST_BORROW         4 (label)
               CALL                     1
               LOAD_SMALL_INT          40
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN

409            JUMP_BACKWARD          154 (to L2)

412    L8:     LOAD_FAST_BORROW         5 (value)
               LOAD_CONST               3 (('-', '--', '---'))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN

413            JUMP_BACKWARD          163 (to L2)

414    L9:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 81 (value, out)
               LOAD_FAST_BORROW         4 (label)
               STORE_SUBSCR
               JUMP_BACKWARD          169 (to L2)

398   L10:     END_FOR
               POP_ITER

415            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app\services\ingestion\email_parser.py", line 418>:
418           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('label_map')
              LOAD_CONST               2 ('Dict[str, str]')
              LOAD_CONST               3 ('aliases')
              LOAD_CONST               4 ('Tuple[str, ...]')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Optional[str]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _first_alias at 0x0000018C18038B70, file "app\services\ingestion\email_parser.py", line 418>:
418           RESUME                   0

419           LOAD_FAST_BORROW         0 (label_map)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

420           LOAD_CONST               0 (None)
              RETURN_VALUE

421   L1:     LOAD_FAST_BORROW         1 (aliases)
              GET_ITER
      L2:     FOR_ITER                32 (to L4)
              STORE_FAST               2 (a)

422           LOAD_FAST_BORROW         0 (label_map)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_FAST_BORROW         2 (a)
              CALL                     1
              STORE_FAST               3 (v)

423           LOAD_FAST_BORROW         3 (v)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           30 (to L2)

424   L3:     LOAD_FAST_BORROW         3 (v)
              SWAP                     2
              POP_TOP
              RETURN_VALUE

421   L4:     END_FOR
              POP_ITER

425           LOAD_CONST               0 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app\services\ingestion\email_parser.py", line 428>:
428           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('full_name')
              LOAD_CONST               2 ('Optional[str]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Tuple[Optional[str], Optional[str]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _split_full_name at 0x0000018C18060390, file "app\services\ingestion\email_parser.py", line 428>:
428           RESUME                   0

429           LOAD_FAST_BORROW         0 (full_name)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

430           LOAD_CONST               3 ((None, None))
              RETURN_VALUE

431   L1:     LOAD_FAST_BORROW         0 (full_name)
              LOAD_ATTR                1 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR                3 (split + NULL|self)
              CALL                     0
              STORE_FAST               1 (parts)

432           LOAD_FAST_BORROW         1 (parts)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

433           LOAD_CONST               3 ((None, None))
              RETURN_VALUE

434   L2:     LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (parts)
              CALL                     1
              LOAD_SMALL_INT           1
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       12 (to L3)
              NOT_TAKEN

435           LOAD_FAST_BORROW         1 (parts)
              LOAD_SMALL_INT           0
              BINARY_OP               26 ([])
              LOAD_CONST               0 (None)
              BUILD_TUPLE              2
              RETURN_VALUE

436   L3:     LOAD_FAST_BORROW         1 (parts)
              LOAD_SMALL_INT           0
              BINARY_OP               26 ([])
              LOAD_CONST               1 (' ')
              LOAD_ATTR                7 (join + NULL|self)
              LOAD_FAST_BORROW         1 (parts)
              LOAD_CONST               2 (slice(1, None, None))
              BINARY_OP               26 ([])
              CALL                     1
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app\services\ingestion\email_parser.py", line 439>:
439           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('raw')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _sanitize_phone at 0x0000018C17D44220, file "app\services\ingestion\email_parser.py", line 439>:
439            RESUME                   0

447            LOAD_GLOBAL              1 (_ensure_text + NULL)
               LOAD_FAST_BORROW         0 (raw)
               CALL                     1
               STORE_FAST               1 (s)

448            LOAD_FAST_BORROW         1 (s)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

449            LOAD_CONST               1 (None)
               RETURN_VALUE

451    L1:     LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR                3 (lower + NULL|self)
               CALL                     0
               STORE_FAST               2 (lower)

452            LOAD_CONST               7 (('ext', ' x ', ';', ','))
               GET_ITER
       L2:     FOR_ITER                39 (to L4)
               STORE_FAST               3 (sep)

453            LOAD_FAST_BORROW         2 (lower)
               LOAD_ATTR                5 (find + NULL|self)
               LOAD_FAST_BORROW         3 (sep)
               CALL                     1
               STORE_FAST               4 (idx)

454            LOAD_FAST_BORROW         4 (idx)
               LOAD_SMALL_INT           0
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               JUMP_BACKWARD           29 (to L2)

455    L3:     LOAD_FAST_BORROW         1 (s)
               LOAD_CONST               1 (None)
               LOAD_FAST_BORROW         4 (idx)
               BINARY_SLICE
               STORE_FAST               1 (s)

456            LOAD_FAST_BORROW         2 (lower)
               LOAD_CONST               1 (None)
               LOAD_FAST_BORROW         4 (idx)
               BINARY_SLICE
               STORE_FAST               2 (lower)

457            POP_TOP
               JUMP_FORWARD             2 (to L5)

452    L4:     END_FOR
               POP_ITER

458    L5:     LOAD_FAST_BORROW         1 (s)
               LOAD_ATTR                7 (lstrip + NULL|self)
               CALL                     0
               LOAD_ATTR                9 (startswith + NULL|self)
               LOAD_CONST               2 ('+')
               CALL                     1
               STORE_FAST               5 (plus_seen)

459            LOAD_CONST               3 ('')
               LOAD_ATTR               11 (join + NULL|self)
               LOAD_CONST               4 (<code object <genexpr> at 0x0000018C17C49B80, file "app\services\ingestion\email_parser.py", line 459>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (s)
               GET_ITER
               CALL                     0
               CALL                     1
               STORE_FAST               6 (digits)

460            LOAD_FAST_BORROW         6 (digits)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN

461            LOAD_CONST               1 (None)
               RETURN_VALUE

462    L6:     LOAD_FAST_BORROW         5 (plus_seen)
               TO_BOOL
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN

463            LOAD_CONST               2 ('+')
               LOAD_FAST_BORROW         6 (digits)
               BINARY_OP                0 (+)
               RETURN_VALUE

464    L7:     LOAD_GLOBAL             13 (len + NULL)
               LOAD_FAST_BORROW         6 (digits)
               CALL                     1
               LOAD_SMALL_INT          10
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       10 (to L8)
               NOT_TAKEN

465            LOAD_CONST               5 ('+1')
               LOAD_FAST_BORROW         6 (digits)
               BINARY_OP                0 (+)
               RETURN_VALUE

466    L8:     LOAD_GLOBAL             13 (len + NULL)
               LOAD_FAST_BORROW         6 (digits)
               CALL                     1
               LOAD_SMALL_INT          11
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       33 (to L9)
               NOT_TAKEN
               LOAD_FAST_BORROW         6 (digits)
               LOAD_ATTR                9 (startswith + NULL|self)
               LOAD_CONST               6 ('1')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       10 (to L9)
               NOT_TAKEN

467            LOAD_CONST               2 ('+')
               LOAD_FAST_BORROW         6 (digits)
               BINARY_OP                0 (+)
               RETURN_VALUE

468    L9:     LOAD_GLOBAL             13 (len + NULL)
               LOAD_FAST_BORROW         6 (digits)
               CALL                     1
               LOAD_SMALL_INT           7
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       10 (to L10)
               NOT_TAKEN

469            LOAD_CONST               2 ('+')
               LOAD_FAST_BORROW         6 (digits)
               BINARY_OP                0 (+)
               RETURN_VALUE

470   L10:     LOAD_CONST               1 (None)
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C17C49B80, file "app\services\ingestion\email_parser.py", line 459>:
 459           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                30 (to L5)
               STORE_FAST_LOAD_FAST    17 (c, c)
               LOAD_ATTR                1 (isdigit + NULL|self)
               CALL                     0
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           26 (to L2)
       L4:     LOAD_FAST_BORROW         1 (c)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           32 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app\services\ingestion\email_parser.py", line 473>:
473           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('text')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _scan_phone at 0x0000018C1794ED80, file "app\services\ingestion\email_parser.py", line 473>:
473           RESUME                   0

479           LOAD_FAST_BORROW         0 (text)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

480           LOAD_CONST               1 (None)
              RETURN_VALUE

481   L1:     LOAD_GLOBAL              0 (_INTL_PHONE_RE)
              LOAD_ATTR                3 (search + NULL|self)
              LOAD_FAST_BORROW         0 (text)
              CALL                     1
              STORE_FAST               1 (m)

482           LOAD_FAST_BORROW         1 (m)
              TO_BOOL
              POP_JUMP_IF_FALSE       27 (to L2)
              NOT_TAKEN

483           LOAD_GLOBAL              5 (_sanitize_phone + NULL)
              LOAD_FAST_BORROW         1 (m)
              LOAD_ATTR                7 (group + NULL|self)
              LOAD_SMALL_INT           0
              CALL                     1
              CALL                     1
              RETURN_VALUE

484   L2:     LOAD_GLOBAL              8 (_PHONE_RE)
              LOAD_ATTR                3 (search + NULL|self)
              LOAD_FAST_BORROW         0 (text)
              CALL                     1
              STORE_FAST               1 (m)

485           LOAD_FAST_BORROW         1 (m)
              TO_BOOL
              POP_JUMP_IF_FALSE       27 (to L3)
              NOT_TAKEN

486           LOAD_GLOBAL              5 (_sanitize_phone + NULL)
              LOAD_FAST_BORROW         1 (m)
              LOAD_ATTR                7 (group + NULL|self)
              LOAD_SMALL_INT           0
              CALL                     1
              CALL                     1
              RETURN_VALUE

487   L3:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app\services\ingestion\email_parser.py", line 490>:
490           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('text')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _scan_email at 0x0000018C17FE17D0, file "app\services\ingestion\email_parser.py", line 490>:
490           RESUME                   0

491           LOAD_FAST_BORROW         0 (text)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

492           LOAD_CONST               0 (None)
              RETURN_VALUE

493   L1:     LOAD_GLOBAL              0 (_EMAIL_RE)
              LOAD_ATTR                3 (search + NULL|self)
              LOAD_FAST_BORROW         0 (text)
              CALL                     1
              STORE_FAST               1 (m)

494           LOAD_FAST_BORROW         1 (m)
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (m)
              LOAD_ATTR                5 (group + NULL|self)
              LOAD_SMALL_INT           0
              CALL                     1
              RETURN_VALUE
      L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "app\services\ingestion\email_parser.py", line 497>:
497           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('text')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _scan_budget at 0x0000018C17F95E60, file "app\services\ingestion\email_parser.py", line 497>:
497           RESUME                   0

498           LOAD_FAST_BORROW         0 (text)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

499           LOAD_CONST               0 (None)
              RETURN_VALUE

500   L1:     LOAD_GLOBAL              0 (_BUDGET_RE)
              LOAD_ATTR                3 (search + NULL|self)
              LOAD_FAST_BORROW         0 (text)
              CALL                     1
              STORE_FAST               1 (m)

501           LOAD_FAST_BORROW         1 (m)
              TO_BOOL
              POP_JUMP_IF_FALSE       32 (to L2)
              NOT_TAKEN

502           LOAD_FAST_BORROW         1 (m)
              LOAD_ATTR                5 (group + NULL|self)
              LOAD_SMALL_INT           0
              CALL                     1
              LOAD_ATTR                7 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

503   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "app\services\ingestion\email_parser.py", line 506>:
506           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Optional[str]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _normalise_intent at 0x0000018C179C3A50, file "app\services\ingestion\email_parser.py", line 506>:
506           RESUME                   0

507           LOAD_FAST_BORROW         0 (value)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

508           LOAD_CONST               0 (None)
              RETURN_VALUE

509   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                1 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR                3 (lower + NULL|self)
              CALL                     0
              STORE_FAST               1 (v)

511           LOAD_CONST               1 ('buy')
              LOAD_CONST               2 ('buying')
              LOAD_CONST               2 ('buying')
              LOAD_CONST               2 ('buying')
              LOAD_CONST               3 ('buyer')
              LOAD_CONST               2 ('buying')

512           LOAD_CONST               4 ('purchase')
              LOAD_CONST               2 ('buying')
              LOAD_CONST               5 ('purchasing')
              LOAD_CONST               2 ('buying')

513           LOAD_CONST               6 ('sell')
              LOAD_CONST               7 ('selling')
              LOAD_CONST               7 ('selling')
              LOAD_CONST               7 ('selling')
              LOAD_CONST               8 ('seller')
              LOAD_CONST               7 ('selling')

514           LOAD_CONST               9 ('list')
              LOAD_CONST               7 ('selling')
              LOAD_CONST              10 ('listing')
              LOAD_CONST               7 ('selling')

515           LOAD_CONST              11 ('rent')
              LOAD_CONST              12 ('renting')
              LOAD_CONST              12 ('renting')
              LOAD_CONST              12 ('renting')
              LOAD_CONST              13 ('renter')
              LOAD_CONST              12 ('renting')

516           LOAD_CONST              14 ('lease')
              LOAD_CONST              12 ('renting')
              LOAD_CONST              15 ('leasing')
              LOAD_CONST              12 ('renting')

510           BUILD_MAP               15
              STORE_FAST               2 (mapping)

519           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (v, mapping)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        9 (to L2)
              NOT_TAKEN

520           LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (mapping, v)
              BINARY_OP               26 ([])
              RETURN_VALUE

521   L2:     LOAD_FAST_BORROW         2 (mapping)
              LOAD_ATTR                5 (items + NULL|self)
              CALL                     0
              GET_ITER
      L3:     FOR_ITER                15 (to L5)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   52 (k, mapped)

522           LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (k, v)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD           13 (to L3)

523   L4:     LOAD_FAST_BORROW         4 (mapped)
              SWAP                     2
              POP_TOP
              RETURN_VALUE

521   L5:     END_FOR
              POP_ITER

524           LOAD_FAST_BORROW         1 (v)
              LOAD_CONST              16 (slice(None, 40, None))
              BINARY_OP               26 ([])
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app\services\ingestion\email_parser.py", line 531>:
531           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body_text')

532           LOAD_CONST               2 ('str')

531           LOAD_CONST               3 ('sender')

534           LOAD_CONST               4 ('Optional[str]')

531           LOAD_CONST               5 ('source')

535           LOAD_CONST               2 ('str')

531           LOAD_CONST               6 ('return')

536           LOAD_CONST               7 ('Tuple[Dict[str, Any], List[str]]')

531           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _extract_lead_core at 0x0000018C17ED7C70, file "app\services\ingestion\email_parser.py", line 531>:
531            RESUME                   0

541            BUILD_LIST               0
               STORE_FAST               3 (warnings)

542            LOAD_GLOBAL              1 (_build_label_value_map + NULL)
               LOAD_FAST_BORROW         0 (body_text)
               CALL                     1
               STORE_FAST               4 (label_map)

545            LOAD_GLOBAL              3 (_first_alias + NULL)
               LOAD_FAST_BORROW         4 (label_map)
               LOAD_GLOBAL              4 (_ALIAS_NAME)
               CALL                     2
               STORE_FAST               5 (full_name)

546            LOAD_GLOBAL              3 (_first_alias + NULL)
               LOAD_FAST_BORROW         4 (label_map)
               LOAD_GLOBAL              6 (_ALIAS_FIRST_NAME)
               CALL                     2
               STORE_FAST               6 (first_name)

547            LOAD_GLOBAL              3 (_first_alias + NULL)
               LOAD_FAST_BORROW         4 (label_map)
               LOAD_GLOBAL              8 (_ALIAS_LAST_NAME)
               CALL                     2
               STORE_FAST               7 (last_name)

548            LOAD_FAST_BORROW         6 (first_name)
               TO_BOOL
               POP_JUMP_IF_TRUE        30 (to L1)
               NOT_TAKEN
               LOAD_FAST_BORROW         7 (last_name)
               TO_BOOL
               POP_JUMP_IF_TRUE        22 (to L1)
               NOT_TAKEN
               LOAD_FAST_BORROW         5 (full_name)
               TO_BOOL
               POP_JUMP_IF_FALSE       14 (to L1)
               NOT_TAKEN

549            LOAD_GLOBAL             11 (_split_full_name + NULL)
               LOAD_FAST_BORROW         5 (full_name)
               CALL                     1
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST  103 (first_name, last_name)

550    L1:     LOAD_FAST_BORROW         6 (first_name)
               TO_BOOL
               POP_JUMP_IF_TRUE         9 (to L2)
               NOT_TAKEN
               LOAD_FAST_BORROW         7 (last_name)
               TO_BOOL
               POP_JUMP_IF_FALSE       44 (to L4)
               NOT_TAKEN
       L2:     LOAD_FAST_BORROW         5 (full_name)
               TO_BOOL
               POP_JUMP_IF_TRUE        36 (to L4)
               NOT_TAKEN

551            LOAD_CONST               1 (' ')
               LOAD_ATTR               13 (join + NULL|self)
               LOAD_CONST               2 (<code object <genexpr> at 0x0000018C180907A0, file "app\services\ingestion\email_parser.py", line 551>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (first_name, last_name)
               BUILD_TUPLE              2
               GET_ITER
               CALL                     0
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 (None)
       L3:     STORE_FAST               5 (full_name)

553    L4:     LOAD_GLOBAL             15 (_truncate_field + NULL)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (full_name, warnings)
               LOAD_CONST               4 ('name_truncated')
               CALL                     3
               STORE_FAST               5 (full_name)

554            LOAD_GLOBAL             15 (_truncate_field + NULL)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 99 (first_name, warnings)
               LOAD_CONST               4 ('name_truncated')
               CALL                     3
               STORE_FAST               6 (first_name)

555            LOAD_GLOBAL             15 (_truncate_field + NULL)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 115 (last_name, warnings)
               LOAD_CONST               4 ('name_truncated')
               CALL                     3
               STORE_FAST               7 (last_name)

558            LOAD_GLOBAL              3 (_first_alias + NULL)
               LOAD_FAST_BORROW         4 (label_map)
               LOAD_GLOBAL             16 (_ALIAS_PHONE)
               CALL                     2
               STORE_FAST               8 (phone_raw)

559            LOAD_FAST_BORROW         8 (phone_raw)
               TO_BOOL
               POP_JUMP_IF_FALSE       12 (to L5)
               NOT_TAKEN
               LOAD_GLOBAL             19 (_sanitize_phone + NULL)
               LOAD_FAST_BORROW         8 (phone_raw)
               CALL                     1
               JUMP_FORWARD             1 (to L6)
       L5:     LOAD_CONST               3 (None)
       L6:     STORE_FAST               9 (phone)

560            LOAD_FAST_BORROW         9 (phone)
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L7)
               NOT_TAKEN

561            LOAD_GLOBAL             21 (_scan_phone + NULL)
               LOAD_FAST_BORROW         0 (body_text)
               CALL                     1
               STORE_FAST               9 (phone)

564    L7:     LOAD_GLOBAL              3 (_first_alias + NULL)
               LOAD_FAST_BORROW         4 (label_map)
               LOAD_GLOBAL             22 (_ALIAS_EMAIL)
               CALL                     2
               STORE_FAST              10 (email)

565            LOAD_FAST_BORROW        10 (email)
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L8)
               NOT_TAKEN

566            LOAD_GLOBAL             25 (_scan_email + NULL)
               LOAD_FAST_BORROW         0 (body_text)
               CALL                     1
               STORE_FAST              10 (email)

569    L8:     LOAD_FAST_BORROW        10 (email)
               TO_BOOL
               POP_JUMP_IF_FALSE       74 (to L9)
               NOT_TAKEN
               LOAD_GLOBAL             27 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (sender)
               LOAD_GLOBAL             28 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       52 (to L9)
               NOT_TAKEN

570            LOAD_FAST_BORROW        10 (email)
               LOAD_ATTR               31 (lower + NULL|self)
               CALL                     0
               LOAD_FAST_BORROW         1 (sender)
               LOAD_ATTR               33 (strip + NULL|self)
               CALL                     0
               LOAD_ATTR               31 (lower + NULL|self)
               CALL                     0
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN

571            LOAD_CONST               3 (None)
               STORE_FAST              10 (email)

572    L9:     LOAD_FAST_BORROW        10 (email)
               TO_BOOL
               POP_JUMP_IF_FALSE       13 (to L10)
               NOT_TAKEN

573            LOAD_GLOBAL             15 (_truncate_field + NULL)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 163 (email, warnings)
               LOAD_CONST               5 ('email_truncated')
               CALL                     3
               STORE_FAST              10 (email)

576   L10:     LOAD_GLOBAL             15 (_truncate_field + NULL)

577            LOAD_GLOBAL              3 (_first_alias + NULL)
               LOAD_FAST_BORROW         4 (label_map)
               LOAD_GLOBAL             34 (_ALIAS_PROPERTY)
               CALL                     2

578            LOAD_FAST_BORROW         3 (warnings)
               LOAD_CONST               6 ('property_address_truncated')

576            CALL                     3
               STORE_FAST              11 (property_address)

580            LOAD_GLOBAL             15 (_truncate_field + NULL)

581            LOAD_GLOBAL              3 (_first_alias + NULL)
               LOAD_FAST_BORROW         4 (label_map)
               LOAD_GLOBAL             36 (_ALIAS_CITY)
               CALL                     2

582            LOAD_FAST_BORROW         3 (warnings)
               LOAD_CONST               7 ('city_truncated')

580            CALL                     3
               STORE_FAST              12 (city)

584            LOAD_GLOBAL             15 (_truncate_field + NULL)

585            LOAD_GLOBAL              3 (_first_alias + NULL)
               LOAD_FAST_BORROW         4 (label_map)
               LOAD_GLOBAL             38 (_ALIAS_STATE)
               CALL                     2

586            LOAD_FAST_BORROW         3 (warnings)
               LOAD_CONST               8 ('state_truncated')

584            CALL                     3
               STORE_FAST              13 (state)

590            LOAD_GLOBAL              3 (_first_alias + NULL)
               LOAD_FAST_BORROW         4 (label_map)
               LOAD_GLOBAL             40 (_ALIAS_BUDGET)
               CALL                     2
               STORE_FAST              14 (budget)

591            LOAD_FAST_BORROW        14 (budget)
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L11)
               NOT_TAKEN

592            LOAD_GLOBAL             43 (_scan_budget + NULL)
               LOAD_FAST_BORROW         0 (body_text)
               CALL                     1
               STORE_FAST              14 (budget)

593   L11:     LOAD_GLOBAL             15 (_truncate_field + NULL)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 227 (budget, warnings)
               LOAD_CONST               9 ('budget_truncated')
               CALL                     3
               STORE_FAST              14 (budget)

594            LOAD_GLOBAL             15 (_truncate_field + NULL)

595            LOAD_GLOBAL              3 (_first_alias + NULL)
               LOAD_FAST_BORROW         4 (label_map)
               LOAD_GLOBAL             44 (_ALIAS_TIMELINE)
               CALL                     2

596            LOAD_FAST_BORROW         3 (warnings)
               LOAD_CONST              10 ('timeline_truncated')

594            CALL                     3
               STORE_FAST              15 (timeline)

600            LOAD_GLOBAL             15 (_truncate_field + NULL)

601            LOAD_GLOBAL              3 (_first_alias + NULL)
               LOAD_FAST_BORROW         4 (label_map)
               LOAD_GLOBAL             46 (_ALIAS_NOTES)
               CALL                     2

602            LOAD_FAST_BORROW         3 (warnings)
               LOAD_CONST              11 ('notes_truncated')

600            CALL                     3
               STORE_FAST              16 (notes)

604            LOAD_GLOBAL             49 (_normalise_intent + NULL)

605            LOAD_GLOBAL              3 (_first_alias + NULL)
               LOAD_FAST_BORROW         4 (label_map)
               LOAD_GLOBAL             50 (_ALIAS_INTENT)
               CALL                     2

604            CALL                     1
               STORE_FAST              17 (intent)

609            BUILD_MAP                0
               STORE_FAST              18 (metadata)

610            LOAD_GLOBAL              3 (_first_alias + NULL)
               LOAD_FAST_BORROW         4 (label_map)
               LOAD_GLOBAL             52 (_ALIAS_LEAD_SOURCE)
               CALL                     2
               STORE_FAST              19 (lead_source)

611            LOAD_FAST_BORROW        19 (lead_source)
               TO_BOOL
               POP_JUMP_IF_FALSE       17 (to L12)
               NOT_TAKEN

612            LOAD_GLOBAL             15 (_truncate_field + NULL)

613            LOAD_FAST_BORROW        19 (lead_source)
               LOAD_FAST_BORROW         3 (warnings)
               LOAD_CONST              12 ('metadata_truncated')

612            CALL                     3
               LOAD_FAST_BORROW        18 (metadata)
               LOAD_CONST              13 ('lead_source')
               STORE_SUBSCR

615   L12:     LOAD_GLOBAL              3 (_first_alias + NULL)
               LOAD_FAST_BORROW         4 (label_map)
               LOAD_GLOBAL             54 (_ALIAS_CAMPAIGN)
               CALL                     2
               STORE_FAST              20 (campaign)

616            LOAD_FAST_BORROW        20 (campaign)
               TO_BOOL
               POP_JUMP_IF_FALSE       17 (to L13)
               NOT_TAKEN

617            LOAD_GLOBAL             15 (_truncate_field + NULL)

618            LOAD_FAST_BORROW        20 (campaign)
               LOAD_FAST_BORROW         3 (warnings)
               LOAD_CONST              12 ('metadata_truncated')

617            CALL                     3
               LOAD_FAST_BORROW        18 (metadata)
               LOAD_CONST              14 ('campaign')
               STORE_SUBSCR

620   L13:     LOAD_GLOBAL              3 (_first_alias + NULL)
               LOAD_FAST_BORROW         4 (label_map)
               LOAD_GLOBAL             56 (_ALIAS_PROPERTY_TYPE)
               CALL                     2
               STORE_FAST              21 (property_type)

621            LOAD_FAST_BORROW        21 (property_type)
               TO_BOOL
               POP_JUMP_IF_FALSE       17 (to L14)
               NOT_TAKEN

622            LOAD_GLOBAL             15 (_truncate_field + NULL)

623            LOAD_FAST_BORROW        21 (property_type)
               LOAD_FAST_BORROW         3 (warnings)
               LOAD_CONST              12 ('metadata_truncated')

622            CALL                     3
               LOAD_FAST_BORROW        18 (metadata)
               LOAD_CONST              15 ('property_type')
               STORE_SUBSCR

627   L14:     LOAD_FAST_BORROW         2 (source)
               LOAD_FAST_BORROW        18 (metadata)
               LOAD_CONST              16 ('email_source')
               STORE_SUBSCR

629            LOAD_CONST              17 ('email:')
               LOAD_FAST_BORROW         2 (source)
               FORMAT_SIMPLE
               BUILD_STRING             2
               STORE_FAST              22 (raw_source_ref)

632            LOAD_CONST              18 ('full_name')
               LOAD_FAST_BORROW         5 (full_name)

633            LOAD_CONST              19 ('first_name')
               LOAD_FAST_BORROW         6 (first_name)

634            LOAD_CONST              20 ('last_name')
               LOAD_FAST_BORROW         7 (last_name)

635            LOAD_CONST              21 ('phone')
               LOAD_FAST_BORROW         9 (phone)

636            LOAD_CONST              22 ('email')
               LOAD_FAST_BORROW        10 (email)

637            LOAD_CONST              23 ('property_address')
               LOAD_FAST_BORROW        11 (property_address)

638            LOAD_CONST              24 ('city')
               LOAD_FAST_BORROW        12 (city)

639            LOAD_CONST              25 ('state')
               LOAD_FAST_BORROW        13 (state)

640            LOAD_CONST              26 ('budget')
               LOAD_FAST_BORROW        14 (budget)

641            LOAD_CONST              27 ('timeline')
               LOAD_FAST_BORROW        15 (timeline)

642            LOAD_CONST              28 ('notes')
               LOAD_FAST_BORROW        16 (notes)

643            LOAD_CONST              29 ('intent')
               LOAD_FAST_BORROW        17 (intent)

644            LOAD_CONST              30 ('raw_source_ref')
               LOAD_FAST_BORROW        22 (raw_source_ref)

645            LOAD_CONST              31 ('metadata')
               LOAD_FAST_BORROW        18 (metadata)

631            BUILD_MAP               14
               STORE_FAST              23 (lead)

647            LOAD_FAST_BORROW        23 (lead)
               LOAD_FAST_BORROW         3 (warnings)
               BUILD_TUPLE              2
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180907A0, file "app\services\ingestion\email_parser.py", line 551>:
 551           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L5)
               STORE_FAST_LOAD_FAST    17 (p, p)
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           12 (to L2)
       L4:     LOAD_FAST_BORROW         1 (p)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           18 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "app\services\ingestion\email_parser.py", line 650>:
650           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('lead')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _scrub_forbidden_keys at 0x0000018C17ED8340, file "app\services\ingestion\email_parser.py", line 650>:
 650            RESUME                   0

 654            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (lead)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 655            BUILD_MAP                0
                RETURN_VALUE

 656    L1:     LOAD_GLOBAL              4 (FORBIDDEN_PARSER_OUTPUT_KEYS)
                GET_ITER
        L2:     FOR_ITER                21 (to L3)
                STORE_FAST               1 (k)

 657            LOAD_FAST_BORROW         0 (lead)
                LOAD_ATTR                7 (pop + NULL|self)
                LOAD_FAST_BORROW         1 (k)
                LOAD_CONST               1 (None)
                CALL                     2
                POP_TOP
                JUMP_BACKWARD           23 (to L2)

 656    L3:     END_FOR
                POP_ITER

 659            LOAD_FAST_BORROW         0 (lead)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               2 ('metadata')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L4:     STORE_FAST               2 (meta)

 660            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (meta)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN

 661            BUILD_MAP                0
                STORE_FAST               2 (meta)

 664    L5:     LOAD_GLOBAL             10 (ALLOWED_EMAIL_METADATA_KEYS)
                GET_ITER

 662            LOAD_FAST_AND_CLEAR      1 (k)
                SWAP                     2
        L6:     BUILD_MAP                0
                SWAP                     2

 664    L7:     FOR_ITER                32 (to L12)
                STORE_FAST               1 (k)

 665            LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (k, meta)
                CONTAINS_OP              0 (in)

 663    L8:     POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L7)

 665    L9:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (meta, k)
                BINARY_OP               26 ([])

 663   L10:     POP_JUMP_IF_NOT_NONE     3 (to L11)
                NOT_TAKEN
                JUMP_BACKWARD           23 (to L7)
       L11:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (k, meta)
                LOAD_FAST_BORROW         1 (k)
                BINARY_OP               26 ([])
                MAP_ADD                  2
                JUMP_BACKWARD           34 (to L7)

 664   L12:     END_FOR
                POP_ITER

 662   L13:     SWAP                     2
                STORE_FAST               1 (k)
                LOAD_FAST_BORROW         0 (lead)
                LOAD_CONST               2 ('metadata')
                STORE_SUBSCR

 667            LOAD_FAST_BORROW         0 (lead)
                RETURN_VALUE

  --   L14:     SWAP                     2
                POP_TOP

 662            SWAP                     2
                STORE_FAST               1 (k)
                RERAISE                  0
ExceptionTable:
  L6 to L8 -> L14 [2]
  L9 to L10 -> L14 [2]
  L11 to L13 -> L14 [2]

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app\services\ingestion\email_parser.py", line 674>:
674           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('subject')

675           LOAD_CONST               2 ('Optional[str]')

674           LOAD_CONST               3 ('sender')

676           LOAD_CONST               2 ('Optional[str]')

674           LOAD_CONST               4 ('body')

677           LOAD_CONST               2 ('Optional[str]')

674           LOAD_CONST               5 ('source_hint')

678           LOAD_CONST               2 ('Optional[str]')

674           LOAD_CONST               6 ('return')

679           LOAD_CONST               7 ('Dict[str, Any]')

674           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object extract_lead_fields_from_email at 0x0000018C17D465D0, file "app\services\ingestion\email_parser.py", line 674>:
 674            RESUME                   0

 688            BUILD_LIST               0
                STORE_FAST               4 (warnings)

 689            BUILD_LIST               0
                STORE_FAST               5 (errors)

 691            LOAD_GLOBAL              1 (_cap_body + NULL)
                LOAD_FAST_BORROW         2 (body)
                CALL                     1
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  103 (body_text, body_warns)

 692            LOAD_FAST_BORROW         4 (warnings)
                LOAD_ATTR                3 (extend + NULL|self)
                LOAD_FAST_BORROW         7 (body_warns)
                CALL                     1
                POP_TOP

 693            LOAD_GLOBAL              5 (_looks_like_html + NULL)
                LOAD_FAST_BORROW         2 (body)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       29 (to L1)
                NOT_TAKEN

 694            LOAD_GLOBAL              7 (_strip_html + NULL)
                LOAD_FAST_BORROW         6 (body_text)
                CALL                     1
                STORE_FAST               6 (body_text)

 695            LOAD_FAST_BORROW         4 (warnings)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST               1 ('email_body_html_stripped')
                CALL                     1
                POP_TOP

 699    L1:     LOAD_FAST_BORROW         3 (source_hint)
                LOAD_GLOBAL             10 (ALLOWED_EMAIL_LEAD_SOURCES)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN

 698            LOAD_FAST                3 (source_hint)
                JUMP_FORWARD            11 (to L3)

 700    L2:     LOAD_GLOBAL             13 (detect_email_lead_source + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (subject, sender)
                LOAD_FAST_BORROW         6 (body_text)
                CALL                     3

 697    L3:     STORE_FAST               8 (source)

 703            NOP

 704    L4:     LOAD_GLOBAL             15 (_extract_lead_core + NULL)

 705            LOAD_FAST_BORROW_LOAD_FAST_BORROW 97 (body_text, sender)
                LOAD_FAST_BORROW         8 (source)

 704            LOAD_CONST               2 (('sender', 'source'))
                CALL_KW                  3
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  154 (lead, lead_warns)

 707            LOAD_FAST_BORROW         4 (warnings)
                LOAD_ATTR                3 (extend + NULL|self)
                LOAD_FAST_BORROW        10 (lead_warns)
                CALL                     1
                POP_TOP

 725    L5:     LOAD_GLOBAL             29 (_scrub_forbidden_keys + NULL)
                LOAD_FAST                9 (lead)
                CALL                     1
                STORE_FAST               9 (lead)

 727            LOAD_GLOBAL             31 (bool + NULL)
                LOAD_FAST                9 (lead)
                LOAD_ATTR               33 (get + NULL|self)
                LOAD_CONST              14 ('phone')
                CALL                     1
                CALL                     1
                STORE_FAST              12 (has_phone)

 728            LOAD_GLOBAL             31 (bool + NULL)
                LOAD_FAST                9 (lead)
                LOAD_ATTR               33 (get + NULL|self)
                LOAD_CONST              15 ('email')
                CALL                     1
                CALL                     1
                STORE_FAST              13 (has_email)

 730            LOAD_FAST               12 (has_phone)
                TO_BOOL
                POP_JUMP_IF_TRUE        58 (to L6)
                NOT_TAKEN
                LOAD_FAST               13 (has_email)
                TO_BOOL
                POP_JUMP_IF_TRUE        50 (to L6)
                NOT_TAKEN

 731            LOAD_FAST                5 (errors)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST              16 ('email_lead_no_contact')
                CALL                     1
                POP_TOP

 733            LOAD_CONST               4 ('status')
                LOAD_CONST               5 ('failed')

 734            LOAD_CONST               6 ('source')
                LOAD_FAST                8 (source)

 735            LOAD_CONST               7 ('lead')
                LOAD_CONST               8 (None)

 736            LOAD_CONST               9 ('call_eligible')
                LOAD_CONST              10 (False)

 737            LOAD_CONST              11 ('warnings')
                LOAD_GLOBAL             27 (list + NULL)
                LOAD_FAST                4 (warnings)
                CALL                     1

 738            LOAD_CONST              12 ('errors')
                LOAD_GLOBAL             27 (list + NULL)
                LOAD_FAST                5 (errors)
                CALL                     1

 732            BUILD_MAP                6
                RETURN_VALUE

 741    L6:     LOAD_FAST               12 (has_phone)
                TO_BOOL
                POP_JUMP_IF_TRUE        50 (to L7)
                NOT_TAKEN

 743            LOAD_FAST                4 (warnings)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST              17 ('email_lead_missing_phone')
                CALL                     1
                POP_TOP

 745            LOAD_CONST               4 ('status')
                LOAD_CONST              18 ('ok')

 746            LOAD_CONST               6 ('source')
                LOAD_FAST                8 (source)

 747            LOAD_CONST               7 ('lead')
                LOAD_FAST                9 (lead)

 748            LOAD_CONST               9 ('call_eligible')
                LOAD_CONST              10 (False)

 749            LOAD_CONST              11 ('warnings')
                LOAD_GLOBAL             27 (list + NULL)
                LOAD_FAST                4 (warnings)
                CALL                     1

 750            LOAD_CONST              12 ('errors')
                LOAD_GLOBAL             27 (list + NULL)
                LOAD_FAST                5 (errors)
                CALL                     1

 744            BUILD_MAP                6
                RETURN_VALUE

 754    L7:     LOAD_CONST               4 ('status')
                LOAD_CONST              18 ('ok')

 755            LOAD_CONST               6 ('source')
                LOAD_FAST                8 (source)

 756            LOAD_CONST               7 ('lead')
                LOAD_FAST                9 (lead)

 757            LOAD_CONST               9 ('call_eligible')
                LOAD_CONST              19 (True)

 758            LOAD_CONST              11 ('warnings')
                LOAD_GLOBAL             27 (list + NULL)
                LOAD_FAST                4 (warnings)
                CALL                     1

 759            LOAD_CONST              12 ('errors')
                LOAD_GLOBAL             27 (list + NULL)
                LOAD_FAST                5 (errors)
                CALL                     1

 753            BUILD_MAP                6
                RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

 708            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      100 (to L13)
                NOT_TAKEN
                STORE_FAST              11 (e)

 712    L9:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 713            LOAD_CONST               3 ('extract_lead_fields_from_email unexpected error type=')

 714            LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE

 713            BUILD_STRING             2

 712            CALL                     1
                POP_TOP

 717            LOAD_CONST               4 ('status')
                LOAD_CONST               5 ('failed')

 718            LOAD_CONST               6 ('source')
                LOAD_FAST                8 (source)

 719            LOAD_CONST               7 ('lead')
                LOAD_CONST               8 (None)

 720            LOAD_CONST               9 ('call_eligible')
                LOAD_CONST              10 (False)

 721            LOAD_CONST              11 ('warnings')
                LOAD_GLOBAL             27 (list + NULL)
                LOAD_FAST                4 (warnings)
                CALL                     1

 722            LOAD_CONST              12 ('errors')
                LOAD_CONST              13 ('parser_exception:')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 716            BUILD_MAP                6
       L10:     SWAP                     2
       L11:     POP_EXCEPT
                LOAD_CONST               8 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RETURN_VALUE

  --   L12:     LOAD_CONST               8 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 708   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L8 [0]
  L8 to L9 -> L14 [1] lasti
  L9 to L10 -> L12 [1] lasti
  L10 to L11 -> L14 [1] lasti
  L12 to L14 -> L14 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025330, file "app\services\ingestion\email_parser.py", line 763>:
763           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('raw_email')

764           LOAD_CONST               2 ('Any')

763           LOAD_CONST               3 ('source_hint')

766           LOAD_CONST               4 ('Optional[str]')

763           LOAD_CONST               5 ('return')

767           LOAD_CONST               6 ('Dict[str, Any]')

763           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object parse_email_lead at 0x0000018C17ED1120, file "app\services\ingestion\email_parser.py", line 763>:
 763            RESUME                   0

 781            LOAD_FAST_BORROW         1 (source_hint)
                POP_JUMP_IF_NONE        25 (to L1)
                NOT_TAKEN
                LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (source_hint)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 782            LOAD_CONST               1 (None)
                STORE_FAST               1 (source_hint)

 783    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (source_hint)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       14 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (source_hint)
                LOAD_GLOBAL              4 (ALLOWED_EMAIL_LEAD_SOURCES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN

 785            LOAD_CONST               1 (None)
                STORE_FAST               1 (source_hint)

 788    L2:     LOAD_CONST               1 (None)
                STORE_FAST               2 (subject)

 789            LOAD_CONST               1 (None)
                STORE_FAST               3 (sender)

 790            LOAD_CONST               1 (None)
                STORE_FAST               4 (body)

 792            NOP

 793    L3:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (raw_email)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        5 (to L5)
                NOT_TAKEN

 794            LOAD_FAST                0 (raw_email)
                STORE_FAST               4 (body)
        L4:     EXTENDED_ARG             1
                JUMP_FORWARD           310 (to L28)

 795    L5:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (raw_email)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      255 (to L24)
                NOT_TAKEN

 796            LOAD_GLOBAL              9 (_ensure_text + NULL)

 797            LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               2 ('subject')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP

 798            LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               3 ('Subject')
                CALL                     1

 796    L8:     CALL                     1
                STORE_FAST               2 (subject)

 800            LOAD_GLOBAL              9 (_ensure_text + NULL)

 801            LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               4 ('sender')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        43 (to L13)
        L9:     NOT_TAKEN
       L10:     POP_TOP

 802            LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               5 ('from')
                CALL                     1

 801            COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP

 803            LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               6 ('From')
                CALL                     1

 800   L13:     CALL                     1
                STORE_FAST               3 (sender)

 805            LOAD_GLOBAL              9 (_ensure_text + NULL)

 806            LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               7 ('body')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        93 (to L22)
       L14:     NOT_TAKEN
       L15:     POP_TOP

 807            LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               8 ('text')
                CALL                     1

 806            COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        68 (to L22)
       L16:     NOT_TAKEN
       L17:     POP_TOP

 808            LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               9 ('body_plain')
                CALL                     1

 806            COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        43 (to L22)
       L18:     NOT_TAKEN
       L19:     POP_TOP

 809            LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              10 ('html')
                CALL                     1

 806            COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L22)
       L20:     NOT_TAKEN
       L21:     POP_TOP

 810            LOAD_FAST_BORROW         0 (raw_email)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              11 ('body_html')
                CALL                     1

 805   L22:     CALL                     1
                STORE_FAST               4 (body)
       L23:     JUMP_FORWARD            34 (to L28)

 812   L24:     LOAD_FAST_BORROW         0 (raw_email)
                POP_JUMP_IF_NOT_NONE    16 (to L26)
                NOT_TAKEN

 814            LOAD_CONST              12 ('status')
                LOAD_CONST              13 ('failed')

 815            LOAD_CONST              14 ('source')
                LOAD_CONST              15 ('generic_email')

 816            LOAD_CONST              16 ('lead')
                LOAD_CONST               1 (None)

 817            LOAD_CONST              17 ('call_eligible')
                LOAD_CONST              18 (False)

 818            LOAD_CONST              19 ('warnings')
                BUILD_LIST               0

 819            LOAD_CONST              20 ('errors')
                LOAD_CONST              21 ('email_input_missing')
                BUILD_LIST               1

 813            BUILD_MAP                6
       L25:     RETURN_VALUE

 825   L26:     LOAD_CONST              12 ('status')
                LOAD_CONST              13 ('failed')

 826            LOAD_CONST              14 ('source')
                LOAD_CONST              15 ('generic_email')

 827            LOAD_CONST              16 ('lead')
                LOAD_CONST               1 (None)

 828            LOAD_CONST              17 ('call_eligible')
                LOAD_CONST              18 (False)

 829            LOAD_CONST              19 ('warnings')
                BUILD_LIST               0

 830            LOAD_CONST              20 ('errors')
                LOAD_CONST              22 ('email_input_unsupported_type')
                BUILD_LIST               1

 824            BUILD_MAP                6
       L27:     RETURN_VALUE

 846   L28:     LOAD_FAST_BORROW         4 (body)
                TO_BOOL
                POP_JUMP_IF_TRUE        32 (to L29)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (subject)
                TO_BOOL
                POP_JUMP_IF_TRUE        24 (to L29)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (sender)
                TO_BOOL
                POP_JUMP_IF_TRUE        16 (to L29)
                NOT_TAKEN

 848            LOAD_CONST              12 ('status')
                LOAD_CONST              13 ('failed')

 849            LOAD_CONST              14 ('source')
                LOAD_CONST              15 ('generic_email')

 850            LOAD_CONST              16 ('lead')
                LOAD_CONST               1 (None)

 851            LOAD_CONST              17 ('call_eligible')
                LOAD_CONST              18 (False)

 852            LOAD_CONST              19 ('warnings')
                BUILD_LIST               0

 853            LOAD_CONST              20 ('errors')
                LOAD_CONST              25 ('email_input_empty')
                BUILD_LIST               1

 847            BUILD_MAP                6
                RETURN_VALUE

 856   L29:     LOAD_GLOBAL             23 (extract_lead_fields_from_email + NULL)

 857            LOAD_FAST_BORROW         2 (subject)

 858            LOAD_FAST_BORROW         3 (sender)

 859            LOAD_FAST_BORROW         4 (body)

 860            LOAD_FAST_BORROW         1 (source_hint)

 856            LOAD_CONST              26 (('subject', 'sender', 'body', 'source_hint'))
                CALL_KW                  4
                RETURN_VALUE

  --   L30:     PUSH_EXC_INFO

 832            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L35)
                NOT_TAKEN
                STORE_FAST               5 (e)

 833   L31:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 834            LOAD_CONST              23 ('parse_email_lead input coercion failed type=')

 835            LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE

 834            BUILD_STRING             2

 833            CALL                     1
                POP_TOP

 838            LOAD_CONST              12 ('status')
                LOAD_CONST              13 ('failed')

 839            LOAD_CONST              14 ('source')
                LOAD_CONST              15 ('generic_email')

 840            LOAD_CONST              16 ('lead')
                LOAD_CONST               1 (None)

 841            LOAD_CONST              17 ('call_eligible')
                LOAD_CONST              18 (False)

 842            LOAD_CONST              19 ('warnings')
                BUILD_LIST               0

 843            LOAD_CONST              20 ('errors')
                LOAD_CONST              24 ('parser_exception:')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 837            BUILD_MAP                6
       L32:     SWAP                     2
       L33:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RETURN_VALUE

  --   L34:     LOAD_CONST               1 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 832   L35:     RERAISE                  0

  --   L36:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L30 [0]
  L5 to L6 -> L30 [0]
  L7 to L9 -> L30 [0]
  L10 to L11 -> L30 [0]
  L12 to L14 -> L30 [0]
  L15 to L16 -> L30 [0]
  L17 to L18 -> L30 [0]
  L19 to L20 -> L30 [0]
  L21 to L23 -> L30 [0]
  L24 to L25 -> L30 [0]
  L26 to L27 -> L30 [0]
  L30 to L31 -> L36 [1] lasti
  L31 to L32 -> L34 [1] lasti
  L32 to L33 -> L36 [1] lasti
  L34 to L36 -> L36 [1] lasti
```
