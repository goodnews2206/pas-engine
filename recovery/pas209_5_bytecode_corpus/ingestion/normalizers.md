# ingestion/normalizers

- **pyc:** `app\services\ingestion\__pycache__\normalizers.cpython-314.pyc`
- **expected source path (absent):** `app\services\ingestion/normalizers.py`
- **co_filename (from bytecode):** `app\services\ingestion\normalizers.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** ingestion

## Module docstring

```
PAS161 — Provider-specific normalizers.

Every normalizer is a **pure function**:

* Accepts a payload (typically ``dict``).
* Returns either::

      {"status": "ok",     "lead": NormalizedLead, "warnings": [...]}
      {"status": "failed", "errors": [...]}

* **Never raises** — even on malformed input, non-dict, ``None``,
  or unexpected types.
* **Never echoes raw values** in the ``errors`` list. Error
  tokens are structural identifiers only.
* **Never reads** ``brokerage_id`` / ``api_key`` from the body.

Phone handling: the spec requires a phone. Bad / missing phone
→ ``status: "failed"``. E.164 is the preferred shape; common
US-shaped inputs (10 digits, ``1XXXXXXXXXX`` 11 digits) are
auto-prefixed with ``+1`` and a ``phone_normalised_to_us_e164``
warning surfaces so the operator knows.

Metadata: each normalizer may set keys on the lead's
``metadata`` dict, but only keys in
``contracts.ALLOWED_METADATA_KEYS`` survive the
``NormalizedLead.to_dict()`` serialisation step. The
normalizers know about that allow-list and don't waste effort
setting forbidden keys.
```

## Imports

`ALLOWED_METADATA_KEYS`, `Any`, `Dict`, `List`, `NormalizedLead`, `Optional`, `Tuple`, `__future__`, `annotations`, `app.services.ingestion.contracts`, `logging`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_lead_from_aliases`, `_collect_allowed_metadata`, `_failed`, `_first_present`, `_normalise_intent`, `_ok`, `_safe_str`, `_sanitize_phone`, `_split_full_name`, `normalize_followupboss_payload`, `normalize_generic_webhook`, `normalize_gohighlevel_payload`, `normalize_zapier_payload`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS161 — Provider-specific normalizers.\n\nEvery normalizer is a **pure function**:\n\n* Accepts a payload (typically ``dict``).\n* Returns either::\n\n      {"status": "ok",     "lead": NormalizedLead, "warnings": [...]}\n      {"status": "failed", "errors": [...]}\n\n* **Never raises** — even on malformed input, non-dict, ``None``,\n  or unexpected types.\n* **Never echoes raw values** in the ``errors`` list. Error\n  tokens are structural identifiers only.\n* **Never reads** ``brokerage_id`` / ``api_key`` from the body.\n\nPhone handling: the spec requires a phone. Bad / missing phone\n→ ``status: "failed"``. E.164 is the preferred shape; common\nUS-shaped inputs (10 digits, ``1XXXXXXXXXX`` 11 digits) are\nauto-prefixed with ``+1`` and a ``phone_normalised_to_us_e164``\nwarning surfaces so the operator knows.\n\nMetadata: each normalizer may set keys on the lead\'s\n``metadata`` dict, but only keys in\n``contracts.ALLOWED_METADATA_KEYS`` survive the\n``NormalizedLead.to_dict()`` serialisation step. The\nnormalizers know about that allow-list and don\'t waste effort\nsetting forbidden keys.\n'
- 'pas.ingestion.normalizers'
- 'lead_id_aliases'
- 'val'
- 'Any'
- 'return'
- 'Optional[str]'
- 'Return a trimmed string for non-empty ``val`` or ``None``.'
- 'payload'
- 'Dict[str, Any]'
- 'aliases'
- 'Tuple[str, ...]'
- 'Return the first non-empty string under any alias key, or\n``None``. Never echoes the value in errors.'
- 'raw'
- 'Tuple[Optional[str], List[str]]'
- 'Sanitize a free-form phone string into E.164 if possible.\n\nReturns ``(cleaned_or_None, warnings)``. ``cleaned_or_None``\nis the E.164-shaped string (``+XXXXXXXXXXX``) or ``None`` if\nthe input could not be coerced to anything phone-shaped.\n\nRecognised shapes:\n  * Already E.164 (``+...`` followed by digits) — returned\n    as-is.\n  * 10 digits, US-shaped — prefixed ``+1`` with the warning\n    ``phone_normalised_to_us_e164``.\n  * 11 digits starting with ``1`` — prefixed ``+`` with the\n    same warning.\n  * Other digit-only forms — returned as ``+`` plus the\n    digits, with ``phone_not_clearly_e164`` warning. The\n    caller may still reject downstream.\n  * Empty / non-string / no digits — ``(None, [warn])``.\n\nStripping rules: whitespace, parentheses, hyphens, dots,\nunderscores, and ``ext`` extensions are removed. Embedded\n``ext`` / ``x`` extensions are dropped (the call leg uses\nthe trunk, not the extension).\n'
- 'phone_missing'
- 'phone_not_a_string'
- 'phone_empty'
- 'phone_no_digits'
- 'phone_normalised_to_us_e164'
- 'phone_not_clearly_e164'
- 'value'
- "Map common buy/sell/rent variants to PAS's canonical form,\nmatching ``app/routes/outbound.py`` LeadPayload behaviour."
- 'buy'
- 'buying'
- 'buyer'
- 'sell'
- 'selling'
- 'seller'
- 'rent'
- 'renting'
- 'renter'
- 'lease'
- 'leasing'
- 'full_name'
- 'Tuple[Optional[str], Optional[str]]'
- 'Best-effort split of a full name into first / last. Never\noverrides explicit first/last fields from the payload.'
- 'Tuple[Dict[str, Any], List[str]]'
- 'Pull only the allow-listed metadata keys from the payload.\n\nReturns ``(metadata_dict, warnings)``. Unknown / forbidden /\nnon-string keys are silently dropped (warning counts them\naggregate; never echoes the offending key/value).\n'
- 'metadata_keys_dropped:'
- 'source'
- 'str'
- 'Tuple[Optional[NormalizedLead], List[str], List[str]]'
- 'Common alias-based builder used by every normalizer.\n\nReturns ``(lead_or_None, warnings, errors)``. If ``errors``\nis non-empty the caller MUST return the ``failed`` envelope\nand discard the partial lead.\n'
- 'payload_not_a_dict'
- 'missing_phone'
- ':lead:'
- 'phone'
- 'lead_id'
- 'first_name'
- 'last_name'
- 'email'
- 'intent'
- 'property_address'
- 'city'
- 'state'
- 'budget'
- 'timeline'
- 'notes'
- 'raw_source_ref'
- 'metadata'
- 'lead'
- 'NormalizedLead'
- 'warnings'
- 'List[str]'
- 'status'
- 'errors'
- 'failed'
- 'Generic-shape normalizer.\n\nAccepts a free-form dict. Walks the standard alias maps for\nphone / email / name / intent / notes / budget / timeline /\naddress / metadata. ``source`` is set to ``"generic"``.\n'
- 'generic'
- 'normalize_failed'
- 'normalize_generic_webhook unexpected error type='
- 'normalizer_exception:'
- 'Zapier-shape normalizer.\n\nZapier zaps are typically flat dicts with provider-original\nkeys passed through. The alias map handles the common\nshapes; this normalizer additionally surfaces\n``zapier_step`` / ``zap_id`` if present as the\n``raw_source_ref``.\n'
- 'zapier'
- 'zapier:'
- 'zap:'
- ':step:'
- 'step:'
- 'normalize_zapier_payload unexpected error type='
- 'Follow Up Boss-shape normalizer.\n\nFUB lead-created webhooks deliver a payload that may nest\nthe lead under ``person`` or ``lead``. Phones often live as\na list of ``{"value": "..."}`` objects under ``phones``,\nsimilar for emails. This normalizer flattens those nests\nbefore handing off to the common alias builder.\n'
- 'phones'
- 'phoneNumbers'
- 'emails'
- 'emailAddresses'
- 'name'
- 'firstName'
- 'lastName'
- 'lead_source'
- 'followupboss'
- 'normalize_followupboss_payload unexpected error type='
- 'GoHighLevel-shape normalizer.\n\nGHL lead webhooks deliver a contact-shaped dict with\ntop-level ``firstName`` / ``lastName`` / ``email`` / ``phone``\nfields. Some installations nest under ``contact`` or\n``data``. This normalizer unwraps then hands off to the\ncommon alias builder.\n'
- 'leadSource'
- 'campaign'
- 'gohighlevel'
- 'normalize_gohighlevel_payload unexpected error type='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS161 — Provider-specific normalizers.\n\nEvery normalizer is a **pure function**:\n\n* Accepts a payload (typically ``dict``).\n* Returns either::\n\n      {"status": "ok",     "lead": NormalizedLead, "warnings": [...]}\n      {"status": "failed", "errors": [...]}\n\n* **Never raises** — even on malformed input, non-dict, ``None``,\n  or unexpected types.\n* **Never echoes raw values** in the ``errors`` list. Error\n  tokens are structural identifiers only.\n* **Never reads** ``brokerage_id`` / ``api_key`` from the body.\n\nPhone handling: the spec requires a phone. Bad / missing phone\n→ ``status: "failed"``. E.164 is the preferred shape; common\nUS-shaped inputs (10 digits, ``1XXXXXXXXXX`` 11 digits) are\nauto-prefixed with ``+1`` and a ``phone_normalised_to_us_e164``\nwarning surfaces so the operator knows.\n\nMetadata: each normalizer may set keys on the lead\'s\n``metadata`` dict, but only keys in\n``contracts.ALLOWED_METADATA_KEYS`` survive the\n``NormalizedLead.to_dict()`` serialisation step. The\nnormalizers know about that allow-list and don\'t waste effort\nsetting forbidden keys.\n')
              STORE_NAME               0 (__doc__)

 32           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 34           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 35           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional', 'Tuple'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (List)
              STORE_NAME               7 (List)
              IMPORT_FROM              8 (Optional)
              STORE_NAME               8 (Optional)
              IMPORT_FROM              9 (Tuple)
              STORE_NAME               9 (Tuple)
              POP_TOP

 37           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('NormalizedLead', 'ALLOWED_METADATA_KEYS'))
              IMPORT_NAME             10 (app.services.ingestion.contracts)
              IMPORT_FROM             11 (NormalizedLead)
              STORE_NAME              11 (NormalizedLead)
              IMPORT_FROM             12 (ALLOWED_METADATA_KEYS)
              STORE_NAME              12 (ALLOWED_METADATA_KEYS)
              POP_TOP

 42           LOAD_NAME                3 (logging)
              LOAD_ATTR               26 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.ingestion.normalizers')
              CALL                     1
              STORE_NAME              14 (logger)

 52           LOAD_CONST              33 (('phone', 'phone_number', 'mobile', 'mobile_phone', 'cell', 'cellphone', 'telephone'))
              STORE_NAME              15 (_PHONE_ALIASES)

 56           LOAD_CONST              34 (('email', 'email_address', 'emailAddress'))
              STORE_NAME              16 (_EMAIL_ALIASES)

 59           LOAD_CONST              35 (('first_name', 'firstName', 'firstname', 'given_name', 'givenName'))
              STORE_NAME              17 (_FIRST_NAME_ALIASES)

 63           LOAD_CONST              36 (('last_name', 'lastName', 'lastname', 'family_name', 'familyName', 'surname'))
              STORE_NAME              18 (_LAST_NAME_ALIASES)

 67           LOAD_CONST              37 (('name', 'full_name', 'fullName', 'fullname', 'display_name', 'displayName'))
              STORE_NAME              19 (_FULL_NAME_ALIASES)

 71           LOAD_CONST              38 (('notes', 'note', 'message', 'description', 'comment', 'comments'))
              STORE_NAME              20 (_NOTES_ALIASES)

 74           LOAD_CONST              39 (('budget', 'price', 'price_range', 'priceRange', 'max_price'))
              STORE_NAME              21 (_BUDGET_ALIASES)

 77           LOAD_CONST              40 (('timeline', 'move_timeline', 'moveTimeline', 'timeframe', 'time_frame', 'movein', 'move_in_date'))
              STORE_NAME              22 (_TIMELINE_ALIASES)

 81           LOAD_CONST              41 (('intent', 'lead_intent', 'transaction_type', 'transactionType', 'deal_type', 'dealType'))
              STORE_NAME              23 (_INTENT_ALIASES)

 85           LOAD_CONST              42 (('property_address', 'propertyAddress', 'address', 'street', 'street_address', 'streetAddress'))
              STORE_NAME              24 (_PROPERTY_ADDRESS_ALIASES)

 89           LOAD_CONST              43 (('city', 'town'))
              STORE_NAME              25 (_CITY_ALIASES)

 90           LOAD_CONST              44 (('state', 'region', 'province'))
              STORE_NAME              26 (_STATE_ALIASES)

 91           LOAD_CONST              45 (('id', 'lead_id', 'leadId', 'contact_id', 'contactId'))
              STORE_NAME              27 (_LEAD_ID_ALIASES)

100           LOAD_CONST               6 (<code object __annotate__ at 0x0000018C17FA1E30, file "app\services\ingestion\normalizers.py", line 100>)
              MAKE_FUNCTION
              LOAD_CONST               7 (<code object _safe_str at 0x0000018C1794E9E0, file "app\services\ingestion\normalizers.py", line 100>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_safe_str)

116           LOAD_CONST               8 (<code object __annotate__ at 0x0000018C18025D30, file "app\services\ingestion\normalizers.py", line 116>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object _first_present at 0x0000018C17FF10B0, file "app\services\ingestion\normalizers.py", line 116>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_first_present)

129           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA2880, file "app\services\ingestion\normalizers.py", line 129>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _sanitize_phone at 0x0000018C181EAC10, file "app\services\ingestion\normalizers.py", line 129>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_sanitize_phone)

198           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA2100, file "app\services\ingestion\normalizers.py", line 198>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _normalise_intent at 0x0000018C17FF1230, file "app\services\ingestion\normalizers.py", line 198>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_normalise_intent)

213           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA21F0, file "app\services\ingestion\normalizers.py", line 213>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _split_full_name at 0x0000018C180606F0, file "app\services\ingestion\normalizers.py", line 213>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_split_full_name)

226           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA2A60, file "app\services\ingestion\normalizers.py", line 226>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _collect_allowed_metadata at 0x0000018C1794E810, file "app\services\ingestion\normalizers.py", line 226>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_collect_allowed_metadata)

254           LOAD_CONST              18 ('lead_id_aliases')

258           LOAD_NAME               27 (_LEAD_ID_ALIASES)

254           BUILD_MAP                1
              LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18024B30, file "app\services\ingestion\normalizers.py", line 254>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _build_lead_from_aliases at 0x0000018C17ED6BB0, file "app\services\ingestion\normalizers.py", line 254>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              34 (_build_lead_from_aliases)

331           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\ingestion\normalizers.py", line 331>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _ok at 0x0000018C18090030, file "app\services\ingestion\normalizers.py", line 331>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              35 (_ok)

339           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA3000, file "app\services\ingestion\normalizers.py", line 339>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object _failed at 0x0000018C17FA30F0, file "app\services\ingestion\normalizers.py", line 339>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              36 (_failed)

346           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA31E0, file "app\services\ingestion\normalizers.py", line 346>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object normalize_generic_webhook at 0x0000018C17EC4F40, file "app\services\ingestion\normalizers.py", line 346>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              37 (normalize_generic_webhook)

370           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA32D0, file "app\services\ingestion\normalizers.py", line 370>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object normalize_zapier_payload at 0x0000018C17ED7510, file "app\services\ingestion\normalizers.py", line 370>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              38 (normalize_zapier_payload)

424           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA1D40, file "app\services\ingestion\normalizers.py", line 424>)
              MAKE_FUNCTION
              LOAD_CONST              30 (<code object normalize_followupboss_payload at 0x0000018C17D455D0, file "app\services\ingestion\normalizers.py", line 424>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              39 (normalize_followupboss_payload)

495           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA23D0, file "app\services\ingestion\normalizers.py", line 495>)
              MAKE_FUNCTION
              LOAD_CONST              32 (<code object normalize_gohighlevel_payload at 0x0000018C17ED7080, file "app\services\ingestion\normalizers.py", line 495>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              40 (normalize_gohighlevel_payload)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "app\services\ingestion\normalizers.py", line 100>:
100           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('val')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_str at 0x0000018C1794E9E0, file "app\services\ingestion\normalizers.py", line 100>:
100           RESUME                   0

102           LOAD_FAST_BORROW         0 (val)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

103           LOAD_CONST               1 (None)
              RETURN_VALUE

104   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (val)
              LOAD_GLOBAL              2 (bool)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

105           LOAD_CONST               1 (None)
              RETURN_VALUE

106   L2:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (val)
              LOAD_GLOBAL              4 (int)
              LOAD_GLOBAL              6 (float)
              BUILD_TUPLE              2
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       13 (to L3)
              NOT_TAKEN

107           LOAD_GLOBAL              9 (str + NULL)
              LOAD_FAST_BORROW         0 (val)
              CALL                     1
              STORE_FAST               1 (s)
              JUMP_FORWARD            27 (to L5)

108   L3:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (val)
              LOAD_GLOBAL              8 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        4 (to L4)
              NOT_TAKEN

109           LOAD_FAST                0 (val)
              STORE_FAST               1 (s)
              JUMP_FORWARD             2 (to L5)

111   L4:     LOAD_CONST               1 (None)
              RETURN_VALUE

112   L5:     LOAD_FAST_BORROW         1 (s)
              LOAD_ATTR               11 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

113           LOAD_FAST                1 (s)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 (None)
      L6:     RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\services\ingestion\normalizers.py", line 116>:
116           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('payload')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('aliases')
              LOAD_CONST               4 ('Tuple[str, ...]')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Optional[str]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _first_present at 0x0000018C17FF10B0, file "app\services\ingestion\normalizers.py", line 116>:
116           RESUME                   0

119           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (payload)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

120           LOAD_CONST               1 (None)
              RETURN_VALUE

121   L1:     LOAD_FAST_BORROW         1 (aliases)
              GET_ITER
      L2:     FOR_ITER                49 (to L5)
              STORE_FAST               2 (k)

122           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, payload)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

123   L3:     LOAD_GLOBAL              5 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (payload)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_FAST_BORROW         2 (k)
              CALL                     1
              CALL                     1
              STORE_FAST               3 (v)

124           LOAD_FAST_BORROW         3 (v)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD           47 (to L2)

125   L4:     LOAD_FAST_BORROW         3 (v)
              SWAP                     2
              POP_TOP
              RETURN_VALUE

121   L5:     END_FOR
              POP_ITER

126           LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app\services\ingestion\normalizers.py", line 129>:
129           RESUME                   0
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
              LOAD_CONST               4 ('Tuple[Optional[str], List[str]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _sanitize_phone at 0x0000018C181EAC10, file "app\services\ingestion\normalizers.py", line 129>:
129            RESUME                   0

153            BUILD_LIST               0
               STORE_FAST               1 (warnings)

154            LOAD_FAST_BORROW         0 (raw)
               POP_JUMP_IF_NOT_NONE     6 (to L1)
               NOT_TAKEN

155            LOAD_CONST               1 (None)
               LOAD_CONST               2 ('phone_missing')
               BUILD_LIST               1
               BUILD_TUPLE              2
               RETURN_VALUE

156    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (raw)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        55 (to L3)
               NOT_TAKEN

157            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (raw)
               LOAD_GLOBAL              4 (int)
               LOAD_GLOBAL              6 (float)
               BUILD_TUPLE              2
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       22 (to L2)
               NOT_TAKEN

158            LOAD_GLOBAL              3 (str + NULL)
               LOAD_GLOBAL              5 (int + NULL)
               LOAD_FAST_BORROW         0 (raw)
               CALL                     1
               CALL                     1
               STORE_FAST               0 (raw)
               JUMP_FORWARD             5 (to L3)

160    L2:     LOAD_CONST               1 (None)
               LOAD_CONST               3 ('phone_not_a_string')
               BUILD_LIST               1
               BUILD_TUPLE              2
               RETURN_VALUE

162    L3:     LOAD_FAST_BORROW         0 (raw)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               2 (s)

163            LOAD_FAST_BORROW         2 (s)
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L4)
               NOT_TAKEN

164            LOAD_CONST               1 (None)
               LOAD_CONST               4 ('phone_empty')
               BUILD_LIST               1
               BUILD_TUPLE              2
               RETURN_VALUE

169    L4:     LOAD_FAST_BORROW         2 (s)
               LOAD_ATTR               11 (lower + NULL|self)
               CALL                     0
               STORE_FAST               3 (lower)

170            LOAD_CONST              13 (('ext', ' x ', ';', ','))
               GET_ITER
       L5:     FOR_ITER                39 (to L7)
               STORE_FAST               4 (sep)

171            LOAD_FAST_BORROW         3 (lower)
               LOAD_ATTR               13 (find + NULL|self)
               LOAD_FAST_BORROW         4 (sep)
               CALL                     1
               STORE_FAST               5 (idx)

172            LOAD_FAST_BORROW         5 (idx)
               LOAD_SMALL_INT           0
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               JUMP_BACKWARD           29 (to L5)

173    L6:     LOAD_FAST_BORROW         2 (s)
               LOAD_CONST               1 (None)
               LOAD_FAST_BORROW         5 (idx)
               BINARY_SLICE
               STORE_FAST               2 (s)

174            LOAD_FAST_BORROW         3 (lower)
               LOAD_CONST               1 (None)
               LOAD_FAST_BORROW         5 (idx)
               BINARY_SLICE
               STORE_FAST               3 (lower)

175            POP_TOP
               JUMP_FORWARD             2 (to L8)

170    L7:     END_FOR
               POP_ITER

177    L8:     LOAD_FAST_BORROW         2 (s)
               LOAD_ATTR               15 (lstrip + NULL|self)
               CALL                     0
               LOAD_ATTR               17 (startswith + NULL|self)
               LOAD_CONST               5 ('+')
               CALL                     1
               STORE_FAST               6 (plus_seen)

178            LOAD_CONST               6 ('')
               LOAD_ATTR               19 (join + NULL|self)
               LOAD_CONST               7 (<code object <genexpr> at 0x0000018C1802C750, file "app\services\ingestion\normalizers.py", line 178>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         2 (s)
               GET_ITER
               CALL                     0
               CALL                     1
               STORE_FAST               7 (digits)

179            LOAD_FAST_BORROW         7 (digits)
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L9)
               NOT_TAKEN

180            LOAD_CONST               1 (None)
               LOAD_CONST               8 ('phone_no_digits')
               BUILD_LIST               1
               BUILD_TUPLE              2
               RETURN_VALUE

182    L9:     LOAD_FAST_BORROW         6 (plus_seen)
               TO_BOOL
               POP_JUMP_IF_FALSE       12 (to L10)
               NOT_TAKEN

183            LOAD_CONST               5 ('+')
               LOAD_FAST_BORROW         7 (digits)
               BINARY_OP                0 (+)
               LOAD_FAST_BORROW         1 (warnings)
               BUILD_TUPLE              2
               RETURN_VALUE

185   L10:     LOAD_GLOBAL             21 (len + NULL)
               LOAD_FAST_BORROW         7 (digits)
               CALL                     1
               LOAD_SMALL_INT          10
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       29 (to L11)
               NOT_TAKEN

186            LOAD_FAST_BORROW         1 (warnings)
               LOAD_ATTR               23 (append + NULL|self)
               LOAD_CONST               9 ('phone_normalised_to_us_e164')
               CALL                     1
               POP_TOP

187            LOAD_CONST              10 ('+1')
               LOAD_FAST_BORROW         7 (digits)
               BINARY_OP                0 (+)
               LOAD_FAST_BORROW         1 (warnings)
               BUILD_TUPLE              2
               RETURN_VALUE

189   L11:     LOAD_GLOBAL             21 (len + NULL)
               LOAD_FAST_BORROW         7 (digits)
               CALL                     1
               LOAD_SMALL_INT          11
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       52 (to L12)
               NOT_TAKEN
               LOAD_FAST_BORROW         7 (digits)
               LOAD_ATTR               17 (startswith + NULL|self)
               LOAD_CONST              11 ('1')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       29 (to L12)
               NOT_TAKEN

190            LOAD_FAST_BORROW         1 (warnings)
               LOAD_ATTR               23 (append + NULL|self)
               LOAD_CONST               9 ('phone_normalised_to_us_e164')
               CALL                     1
               POP_TOP

191            LOAD_CONST               5 ('+')
               LOAD_FAST_BORROW         7 (digits)
               BINARY_OP                0 (+)
               LOAD_FAST_BORROW         1 (warnings)
               BUILD_TUPLE              2
               RETURN_VALUE

194   L12:     LOAD_FAST_BORROW         1 (warnings)
               LOAD_ATTR               23 (append + NULL|self)
               LOAD_CONST              12 ('phone_not_clearly_e164')
               CALL                     1
               POP_TOP

195            LOAD_CONST               5 ('+')
               LOAD_FAST_BORROW         7 (digits)
               BINARY_OP                0 (+)
               LOAD_FAST_BORROW         1 (warnings)
               BUILD_TUPLE              2
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C1802C750, file "app\services\ingestion\normalizers.py", line 178>:
 178           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app\services\ingestion\normalizers.py", line 198>:
198           RESUME                   0
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

Disassembly of <code object _normalise_intent at 0x0000018C17FF1230, file "app\services\ingestion\normalizers.py", line 198>:
198           RESUME                   0

201           LOAD_FAST_BORROW         0 (value)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

202           LOAD_CONST               1 (None)
              RETURN_VALUE

203   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                1 (lower + NULL|self)
              CALL                     0
              LOAD_ATTR                3 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (v)

205           LOAD_CONST               2 ('buy')
              LOAD_CONST               3 ('buying')
              LOAD_CONST               3 ('buying')
              LOAD_CONST               3 ('buying')
              LOAD_CONST               4 ('buyer')
              LOAD_CONST               3 ('buying')

206           LOAD_CONST               5 ('sell')
              LOAD_CONST               6 ('selling')
              LOAD_CONST               6 ('selling')
              LOAD_CONST               6 ('selling')
              LOAD_CONST               7 ('seller')
              LOAD_CONST               6 ('selling')

207           LOAD_CONST               8 ('rent')
              LOAD_CONST               9 ('renting')
              LOAD_CONST               9 ('renting')
              LOAD_CONST               9 ('renting')
              LOAD_CONST              10 ('renter')
              LOAD_CONST               9 ('renting')

208           LOAD_CONST              11 ('lease')
              LOAD_CONST               9 ('renting')
              LOAD_CONST              12 ('leasing')
              LOAD_CONST               9 ('renting')

204           BUILD_MAP               11
              STORE_FAST               2 (mapping)

210           LOAD_FAST_BORROW         2 (mapping)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 17 (v, v)
              CALL                     2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app\services\ingestion\normalizers.py", line 213>:
213           RESUME                   0
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

Disassembly of <code object _split_full_name at 0x0000018C180606F0, file "app\services\ingestion\normalizers.py", line 213>:
213           RESUME                   0

216           LOAD_FAST_BORROW         0 (full_name)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

217           LOAD_CONST               4 ((None, None))
              RETURN_VALUE

218   L1:     LOAD_FAST_BORROW         0 (full_name)
              LOAD_ATTR                1 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR                3 (split + NULL|self)
              CALL                     0
              STORE_FAST               1 (parts)

219           LOAD_FAST_BORROW         1 (parts)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

220           LOAD_CONST               4 ((None, None))
              RETURN_VALUE

221   L2:     LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (parts)
              CALL                     1
              LOAD_SMALL_INT           1
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       12 (to L3)
              NOT_TAKEN

222           LOAD_FAST_BORROW         1 (parts)
              LOAD_SMALL_INT           0
              BINARY_OP               26 ([])
              LOAD_CONST               1 (None)
              BUILD_TUPLE              2
              RETURN_VALUE

223   L3:     LOAD_FAST_BORROW         1 (parts)
              LOAD_SMALL_INT           0
              BINARY_OP               26 ([])
              LOAD_CONST               2 (' ')
              LOAD_ATTR                7 (join + NULL|self)
              LOAD_FAST_BORROW         1 (parts)
              LOAD_CONST               3 (slice(1, None, None))
              BINARY_OP               26 ([])
              CALL                     1
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app\services\ingestion\normalizers.py", line 226>:
226           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('payload')

227           LOAD_CONST               2 ('Any')

226           LOAD_CONST               3 ('return')

228           LOAD_CONST               4 ('Tuple[Dict[str, Any], List[str]]')

226           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _collect_allowed_metadata at 0x0000018C1794E810, file "app\services\ingestion\normalizers.py", line 226>:
226           RESUME                   0

235           BUILD_MAP                0
              STORE_FAST               1 (out)

236           BUILD_LIST               0
              STORE_FAST               2 (warnings)

237           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (payload)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         4 (to L1)
              NOT_TAKEN

238           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, warnings)
              BUILD_TUPLE              2
              RETURN_VALUE

239   L1:     LOAD_SMALL_INT           0
              STORE_FAST               3 (dropped)

240           LOAD_FAST_BORROW         0 (payload)
              LOAD_ATTR                5 (items + NULL|self)
              CALL                     0
              GET_ITER
      L2:     FOR_ITER                43 (to L5)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   69 (k, v)

241           LOAD_FAST_BORROW         4 (k)
              LOAD_GLOBAL              6 (ALLOWED_METADATA_KEYS)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       28 (to L4)
              NOT_TAKEN

242           LOAD_GLOBAL              9 (_safe_str + NULL)
              LOAD_FAST_BORROW         5 (v)
              CALL                     1
              STORE_FAST               6 (s)

243           LOAD_FAST_BORROW         6 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE        7 (to L3)
              NOT_TAKEN

244           LOAD_FAST_BORROW_LOAD_FAST_BORROW 97 (s, out)
              LOAD_FAST_BORROW         4 (k)
              STORE_SUBSCR
              JUMP_BACKWARD           41 (to L2)

243   L3:     JUMP_BACKWARD           43 (to L2)

248   L4:     JUMP_BACKWARD           45 (to L2)

240   L5:     END_FOR
              POP_ITER

249           LOAD_FAST_BORROW         3 (dropped)
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L6)
              NOT_TAKEN

250           LOAD_FAST_BORROW         2 (warnings)
              LOAD_ATTR               11 (append + NULL|self)
              LOAD_CONST               1 ('metadata_keys_dropped:')
              LOAD_FAST_BORROW         3 (dropped)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP

251   L6:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, warnings)
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app\services\ingestion\normalizers.py", line 254>:
254           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('payload')

255           LOAD_CONST               2 ('Any')

254           LOAD_CONST               3 ('source')

257           LOAD_CONST               4 ('str')

254           LOAD_CONST               5 ('lead_id_aliases')

258           LOAD_CONST               6 ('Tuple[str, ...]')

254           LOAD_CONST               7 ('return')

259           LOAD_CONST               8 ('Tuple[Optional[NormalizedLead], List[str], List[str]]')

254           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _build_lead_from_aliases at 0x0000018C17ED6BB0, file "app\services\ingestion\normalizers.py", line 254>:
254           RESUME                   0

266           BUILD_LIST               0
              STORE_FAST               3 (errors)

267           BUILD_LIST               0
              STORE_FAST               4 (warnings)

269           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (payload)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         7 (to L1)
              NOT_TAKEN

270           LOAD_CONST               1 (None)
              LOAD_FAST_BORROW         4 (warnings)
              LOAD_CONST               2 ('payload_not_a_dict')
              BUILD_LIST               1
              BUILD_TUPLE              3
              RETURN_VALUE

272   L1:     LOAD_GLOBAL              5 (_first_present + NULL)
              LOAD_FAST_BORROW         0 (payload)
              LOAD_GLOBAL              6 (_PHONE_ALIASES)
              CALL                     2
              STORE_FAST               5 (phone_raw)

273           LOAD_GLOBAL              9 (_sanitize_phone + NULL)
              LOAD_FAST_BORROW         5 (phone_raw)
              CALL                     1
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST  103 (cleaned_phone, phone_warns)

274           LOAD_FAST_BORROW         4 (warnings)
              LOAD_ATTR               11 (extend + NULL|self)
              LOAD_FAST_BORROW         7 (phone_warns)
              CALL                     1
              POP_TOP

275           LOAD_FAST_BORROW         6 (cleaned_phone)
              POP_JUMP_IF_NOT_NONE    22 (to L2)
              NOT_TAKEN

277           LOAD_FAST_BORROW         3 (errors)
              LOAD_ATTR               13 (append + NULL|self)
              LOAD_CONST               3 ('missing_phone')
              CALL                     1
              POP_TOP

278           LOAD_CONST               1 (None)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (warnings, errors)
              BUILD_TUPLE              3
              RETURN_VALUE

280   L2:     LOAD_GLOBAL              5 (_first_present + NULL)
              LOAD_FAST_BORROW         0 (payload)
              LOAD_GLOBAL             14 (_EMAIL_ALIASES)
              CALL                     2
              STORE_FAST               8 (email)

281           LOAD_GLOBAL              5 (_first_present + NULL)
              LOAD_FAST_BORROW         0 (payload)
              LOAD_GLOBAL             16 (_FIRST_NAME_ALIASES)
              CALL                     2
              STORE_FAST               9 (first_name)

282           LOAD_GLOBAL              5 (_first_present + NULL)
              LOAD_FAST_BORROW         0 (payload)
              LOAD_GLOBAL             18 (_LAST_NAME_ALIASES)
              CALL                     2
              STORE_FAST              10 (last_name)

283           LOAD_GLOBAL              5 (_first_present + NULL)
              LOAD_FAST_BORROW         0 (payload)
              LOAD_GLOBAL             20 (_FULL_NAME_ALIASES)
              CALL                     2
              STORE_FAST              11 (full_name)

284           LOAD_FAST_BORROW         9 (first_name)
              TO_BOOL
              POP_JUMP_IF_TRUE        30 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW        10 (last_name)
              TO_BOOL
              POP_JUMP_IF_TRUE        22 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW        11 (full_name)
              TO_BOOL
              POP_JUMP_IF_FALSE       14 (to L3)
              NOT_TAKEN

285           LOAD_GLOBAL             23 (_split_full_name + NULL)
              LOAD_FAST_BORROW        11 (full_name)
              CALL                     1
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST  154 (first_name, last_name)

286   L3:     LOAD_FAST_BORROW         9 (first_name)
              TO_BOOL
              POP_JUMP_IF_TRUE         9 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW        10 (last_name)
              TO_BOOL
              POP_JUMP_IF_FALSE       44 (to L6)
              NOT_TAKEN
      L4:     LOAD_FAST_BORROW        11 (full_name)
              TO_BOOL
              POP_JUMP_IF_TRUE        36 (to L6)
              NOT_TAKEN

287           LOAD_CONST               4 (' ')
              LOAD_ATTR               25 (join + NULL|self)
              LOAD_CONST               5 (<code object <genexpr> at 0x0000018C18090140, file "app\services\ingestion\normalizers.py", line 287>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (first_name, last_name)
              BUILD_TUPLE              2
              GET_ITER
              CALL                     0
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 (None)
      L5:     STORE_FAST              11 (full_name)

289   L6:     LOAD_GLOBAL             27 (_normalise_intent + NULL)
              LOAD_GLOBAL              5 (_first_present + NULL)
              LOAD_FAST_BORROW         0 (payload)
              LOAD_GLOBAL             28 (_INTENT_ALIASES)
              CALL                     2
              CALL                     1
              STORE_FAST              12 (intent)

290           LOAD_GLOBAL              5 (_first_present + NULL)
              LOAD_FAST_BORROW         0 (payload)
              LOAD_GLOBAL             30 (_NOTES_ALIASES)
              CALL                     2
              STORE_FAST              13 (notes)

291           LOAD_GLOBAL              5 (_first_present + NULL)
              LOAD_FAST_BORROW         0 (payload)
              LOAD_GLOBAL             32 (_BUDGET_ALIASES)
              CALL                     2
              STORE_FAST              14 (budget)

292           LOAD_GLOBAL              5 (_first_present + NULL)
              LOAD_FAST_BORROW         0 (payload)
              LOAD_GLOBAL             34 (_TIMELINE_ALIASES)
              CALL                     2
              STORE_FAST              15 (timeline)

293           LOAD_GLOBAL              5 (_first_present + NULL)
              LOAD_FAST_BORROW         0 (payload)
              LOAD_GLOBAL             36 (_PROPERTY_ADDRESS_ALIASES)
              CALL                     2
              STORE_FAST              16 (property_address)

294           LOAD_GLOBAL              5 (_first_present + NULL)
              LOAD_FAST_BORROW         0 (payload)
              LOAD_GLOBAL             38 (_CITY_ALIASES)
              CALL                     2
              STORE_FAST              17 (city)

295           LOAD_GLOBAL              5 (_first_present + NULL)
              LOAD_FAST_BORROW         0 (payload)
              LOAD_GLOBAL             40 (_STATE_ALIASES)
              CALL                     2
              STORE_FAST              18 (state)

296           LOAD_GLOBAL              5 (_first_present + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (payload, lead_id_aliases)
              CALL                     2
              STORE_FAST              19 (lead_id)

298           LOAD_GLOBAL             43 (_collect_allowed_metadata + NULL)
              LOAD_FAST_BORROW         0 (payload)
              CALL                     1
              UNPACK_SEQUENCE          2
              STORE_FAST              20 (metadata)
              STORE_FAST              21 (meta_warns)

299           LOAD_FAST_BORROW         4 (warnings)
              LOAD_ATTR               11 (extend + NULL|self)
              LOAD_FAST_BORROW        21 (meta_warns)
              CALL                     1
              POP_TOP

301           LOAD_CONST               1 (None)
              STORE_FAST              22 (raw_source_ref)

302           LOAD_FAST_BORROW        19 (lead_id)
              TO_BOOL
              POP_JUMP_IF_FALSE        8 (to L7)
              NOT_TAKEN

304           LOAD_FAST_BORROW         1 (source)
              FORMAT_SIMPLE
              LOAD_CONST               6 (':lead:')
              LOAD_FAST_BORROW        19 (lead_id)
              FORMAT_SIMPLE
              BUILD_STRING             3
              STORE_FAST              22 (raw_source_ref)

306   L7:     LOAD_GLOBAL             45 (NormalizedLead + NULL)
              LOAD_CONST              23 (())
              BUILD_MAP                0
              LOAD_CONST               7 ('phone')

307           LOAD_FAST_BORROW         6 (cleaned_phone)
              MAP_ADD                  1

306           LOAD_CONST               8 ('source')

308           LOAD_FAST_BORROW         1 (source)
              MAP_ADD                  1

306           LOAD_CONST               9 ('lead_id')

309           LOAD_FAST_BORROW        19 (lead_id)
              MAP_ADD                  1

306           LOAD_CONST              10 ('full_name')

310           LOAD_FAST_BORROW        11 (full_name)
              MAP_ADD                  1

306           LOAD_CONST              11 ('first_name')

311           LOAD_FAST_BORROW         9 (first_name)
              MAP_ADD                  1

306           LOAD_CONST              12 ('last_name')

312           LOAD_FAST_BORROW        10 (last_name)
              MAP_ADD                  1

306           LOAD_CONST              13 ('email')

313           LOAD_FAST_BORROW         8 (email)
              MAP_ADD                  1

306           LOAD_CONST              14 ('intent')

314           LOAD_FAST_BORROW        12 (intent)
              MAP_ADD                  1

306           LOAD_CONST              15 ('property_address')

315           LOAD_FAST_BORROW        16 (property_address)
              MAP_ADD                  1

306           LOAD_CONST              16 ('city')

316           LOAD_FAST_BORROW        17 (city)
              MAP_ADD                  1

306           LOAD_CONST              17 ('state')

317           LOAD_FAST_BORROW        18 (state)
              MAP_ADD                  1

306           LOAD_CONST              18 ('budget')

318           LOAD_FAST_BORROW        14 (budget)
              MAP_ADD                  1

306           LOAD_CONST              19 ('timeline')

319           LOAD_FAST_BORROW        15 (timeline)
              MAP_ADD                  1

306           LOAD_CONST              20 ('notes')

320           LOAD_FAST_BORROW        13 (notes)
              MAP_ADD                  1

306           LOAD_CONST              21 ('raw_source_ref')

321           LOAD_FAST_BORROW        22 (raw_source_ref)
              MAP_ADD                  1

306           LOAD_CONST              22 ('metadata')

322           LOAD_FAST_BORROW        20 (metadata)
              MAP_ADD                  1

306           CALL_FUNCTION_EX
              STORE_FAST              23 (lead)

324           LOAD_FAST_BORROW        23 (lead)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (warnings, errors)
              BUILD_TUPLE              3
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18090140, file "app\services\ingestion\normalizers.py", line 287>:
 287           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\ingestion\normalizers.py", line 331>:
331           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('lead')
              LOAD_CONST               2 ('NormalizedLead')
              LOAD_CONST               3 ('warnings')
              LOAD_CONST               4 ('List[str]')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Dict[str, Any]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _ok at 0x0000018C18090030, file "app\services\ingestion\normalizers.py", line 331>:
331           RESUME                   0

333           LOAD_CONST               0 ('status')
              LOAD_CONST               1 ('ok')

334           LOAD_CONST               2 ('lead')
              LOAD_FAST_BORROW         0 (lead)
              LOAD_ATTR                1 (to_dict + NULL|self)
              CALL                     0

335           LOAD_CONST               3 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST_BORROW         1 (warnings)
              CALL                     1

332           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "app\services\ingestion\normalizers.py", line 339>:
339           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('errors')
              LOAD_CONST               2 ('List[str]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _failed at 0x0000018C17FA30F0, file "app\services\ingestion\normalizers.py", line 339>:
339           RESUME                   0

341           LOAD_CONST               0 ('status')
              LOAD_CONST               1 ('failed')

342           LOAD_CONST               2 ('errors')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST_BORROW         0 (errors)
              CALL                     1

340           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "app\services\ingestion\normalizers.py", line 346>:
346           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('payload')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object normalize_generic_webhook at 0x0000018C17EC4F40, file "app\services\ingestion\normalizers.py", line 346>:
 346            RESUME                   0

 353            NOP

 354    L1:     LOAD_GLOBAL              1 (_build_lead_from_aliases + NULL)

 355            LOAD_FAST_BORROW         0 (payload)
                LOAD_CONST               1 ('generic')

 354            LOAD_CONST               2 (('source',))
                CALL_KW                  2
                UNPACK_SEQUENCE          3
                STORE_FAST_STORE_FAST   18 (lead, warnings)
                STORE_FAST               3 (errors)

 357            LOAD_FAST_BORROW         3 (errors)
                TO_BOOL
                POP_JUMP_IF_TRUE         5 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (lead)
                POP_JUMP_IF_NOT_NONE    23 (to L7)
                NOT_TAKEN

 358    L2:     LOAD_GLOBAL              3 (_failed + NULL)
                LOAD_FAST                3 (errors)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         4 (to L5)
        L3:     NOT_TAKEN
        L4:     POP_TOP
                LOAD_CONST               4 ('normalize_failed')
                BUILD_LIST               1
        L5:     CALL                     1
        L6:     RETURN_VALUE

 359    L7:     LOAD_GLOBAL              5 (_ok + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (lead, warnings)
                CALL                     2
        L8:     RETURN_VALUE

  --    L9:     PUSH_EXC_INFO

 360            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       88 (to L14)
                NOT_TAKEN
                STORE_FAST               4 (e)

 363   L10:     LOAD_GLOBAL              8 (logger)
                LOAD_ATTR               11 (warning + NULL|self)

 364            LOAD_CONST               5 ('normalize_generic_webhook unexpected error type=')

 365            LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE

 364            BUILD_STRING             2

 363            CALL                     1
                POP_TOP

 367            LOAD_GLOBAL              3 (_failed + NULL)
                LOAD_CONST               6 ('normalizer_exception:')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1
                CALL                     1
       L11:     SWAP                     2
       L12:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RETURN_VALUE

  --   L13:     LOAD_CONST               3 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 360   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L9 [0]
  L4 to L6 -> L9 [0]
  L7 to L8 -> L9 [0]
  L9 to L10 -> L15 [1] lasti
  L10 to L11 -> L13 [1] lasti
  L11 to L12 -> L15 [1] lasti
  L13 to L15 -> L15 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "app\services\ingestion\normalizers.py", line 370>:
370           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('payload')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object normalize_zapier_payload at 0x0000018C17ED7510, file "app\services\ingestion\normalizers.py", line 370>:
 370            RESUME                   0

 379            NOP

 380    L1:     LOAD_GLOBAL              1 (_build_lead_from_aliases + NULL)

 381            LOAD_FAST_BORROW         0 (payload)
                LOAD_CONST               1 ('zapier')

 380            LOAD_CONST               2 (('source',))
                CALL_KW                  2
                UNPACK_SEQUENCE          3
                STORE_FAST_STORE_FAST   18 (lead, warnings)
                STORE_FAST               3 (errors)

 383            LOAD_FAST_BORROW         3 (errors)
                TO_BOOL
                POP_JUMP_IF_TRUE         5 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (lead)
                POP_JUMP_IF_NOT_NONE    23 (to L7)
                NOT_TAKEN

 384    L2:     LOAD_GLOBAL              3 (_failed + NULL)
                LOAD_FAST                3 (errors)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         4 (to L5)
        L3:     NOT_TAKEN
        L4:     POP_TOP
                LOAD_CONST               4 ('normalize_failed')
                BUILD_LIST               1
        L5:     CALL                     1
        L6:     RETURN_VALUE

 386    L7:     LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (payload)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                EXTENDED_ARG             1
                POP_JUMP_IF_FALSE      392 (to L21)
                NOT_TAKEN

 387            LOAD_GLOBAL              9 (_first_present + NULL)
                LOAD_FAST_BORROW         0 (payload)
                LOAD_CONST              27 (('zap_id', 'zapId'))
                CALL                     2
                STORE_FAST               4 (zap_id)

 388            LOAD_GLOBAL              9 (_first_present + NULL)
                LOAD_FAST_BORROW         0 (payload)
                LOAD_CONST              28 (('zapier_step', 'step'))
                CALL                     2
                STORE_FAST               5 (step)

 389            LOAD_FAST_BORROW         4 (zap_id)
                TO_BOOL
                POP_JUMP_IF_TRUE        10 (to L9)
                NOT_TAKEN
                LOAD_FAST_BORROW         5 (step)
                TO_BOOL
                EXTENDED_ARG             1
                POP_JUMP_IF_FALSE      351 (to L21)
        L8:     NOT_TAKEN

 390    L9:     LOAD_CONST               5 ('zapier:')
                STORE_FAST               6 (ref)

 391            LOAD_FAST_BORROW         4 (zap_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L12)
       L10:     NOT_TAKEN

 392   L11:     LOAD_FAST_BORROW         6 (ref)
                LOAD_CONST               6 ('zap:')
                LOAD_FAST_BORROW         4 (zap_id)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BINARY_OP               13 (+=)
                STORE_FAST               6 (ref)

 393   L12:     LOAD_FAST_BORROW         5 (step)
                TO_BOOL
                POP_JUMP_IF_FALSE       29 (to L17)
       L13:     NOT_TAKEN

 394   L14:     LOAD_FAST_LOAD_FAST    100 (ref, zap_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       10 (to L15)
                NOT_TAKEN
                LOAD_CONST               7 (':step:')
                LOAD_FAST_BORROW         5 (step)
                BINARY_OP                0 (+)
                JUMP_FORWARD             4 (to L16)
       L15:     LOAD_CONST               8 ('step:')
                LOAD_FAST_BORROW         5 (step)
                FORMAT_SIMPLE
                BUILD_STRING             2
       L16:     BINARY_OP               13 (+=)
                STORE_FAST               6 (ref)

 396   L17:     LOAD_FAST_BORROW         1 (lead)
                LOAD_ATTR               11 (to_dict + NULL|self)
                CALL                     0
                STORE_FAST               7 (d)

 397            LOAD_GLOBAL             13 (NormalizedLead + NULL)
                LOAD_CONST              29 (())
                BUILD_MAP                0
                LOAD_CONST               9 ('phone')

 398            LOAD_FAST_BORROW         7 (d)
                LOAD_CONST               9 ('phone')
                BINARY_OP               26 ([])
                MAP_ADD                  1

 397            LOAD_CONST              10 ('source')

 399            LOAD_FAST_BORROW         7 (d)
                LOAD_CONST              10 ('source')
                BINARY_OP               26 ([])
                MAP_ADD                  1

 397            LOAD_CONST              11 ('lead_id')

 400            LOAD_FAST_BORROW         7 (d)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              11 ('lead_id')
                CALL                     1
                MAP_ADD                  1

 397            LOAD_CONST              12 ('full_name')

 401            LOAD_FAST_BORROW         7 (d)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              12 ('full_name')
                CALL                     1
                MAP_ADD                  1

 397            LOAD_CONST              13 ('first_name')

 402            LOAD_FAST_BORROW         7 (d)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              13 ('first_name')
                CALL                     1
                MAP_ADD                  1

 397            LOAD_CONST              14 ('last_name')

 403            LOAD_FAST_BORROW         7 (d)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              14 ('last_name')
                CALL                     1
                MAP_ADD                  1

 397            LOAD_CONST              15 ('email')

 404            LOAD_FAST_BORROW         7 (d)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              15 ('email')
                CALL                     1
                MAP_ADD                  1

 397            LOAD_CONST              16 ('intent')

 405            LOAD_FAST_BORROW         7 (d)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              16 ('intent')
                CALL                     1
                MAP_ADD                  1

 397            LOAD_CONST              17 ('property_address')

 406            LOAD_FAST_BORROW         7 (d)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              17 ('property_address')
                CALL                     1
                MAP_ADD                  1

 397            LOAD_CONST              18 ('city')

 407            LOAD_FAST_BORROW         7 (d)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              18 ('city')
                CALL                     1
                MAP_ADD                  1

 397            LOAD_CONST              19 ('state')

 408            LOAD_FAST_BORROW         7 (d)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              19 ('state')
                CALL                     1
                MAP_ADD                  1

 397            LOAD_CONST              20 ('budget')

 409            LOAD_FAST_BORROW         7 (d)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              20 ('budget')
                CALL                     1
                MAP_ADD                  1

 397            LOAD_CONST              21 ('timeline')

 410            LOAD_FAST_BORROW         7 (d)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              21 ('timeline')
                CALL                     1
                MAP_ADD                  1

 397            LOAD_CONST              22 ('notes')

 411            LOAD_FAST_BORROW         7 (d)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              22 ('notes')
                CALL                     1
                MAP_ADD                  1

 397            LOAD_CONST              23 ('raw_source_ref')

 412            LOAD_FAST_BORROW         6 (ref)
                MAP_ADD                  1

 397            LOAD_CONST              24 ('metadata')

 413            LOAD_FAST_BORROW         7 (d)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              24 ('metadata')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L20)
       L18:     NOT_TAKEN
       L19:     POP_TOP
                BUILD_MAP                0

  --   L20:     MAP_ADD                  1

 397            CALL_FUNCTION_EX
                STORE_FAST               1 (lead)

 415   L21:     LOAD_GLOBAL             17 (_ok + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (lead, warnings)
                CALL                     2
       L22:     RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 416            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       88 (to L28)
                NOT_TAKEN
                STORE_FAST               8 (e)

 417   L24:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 418            LOAD_CONST              25 ('normalize_zapier_payload unexpected error type=')

 419            LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE

 418            BUILD_STRING             2

 417            CALL                     1
                POP_TOP

 421            LOAD_GLOBAL              3 (_failed + NULL)
                LOAD_CONST              26 ('normalizer_exception:')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1
                CALL                     1
       L25:     SWAP                     2
       L26:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RETURN_VALUE

  --   L27:     LOAD_CONST               3 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 416   L28:     RERAISE                  0

  --   L29:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L23 [0]
  L4 to L6 -> L23 [0]
  L7 to L8 -> L23 [0]
  L9 to L10 -> L23 [0]
  L11 to L13 -> L23 [0]
  L14 to L18 -> L23 [0]
  L19 to L22 -> L23 [0]
  L23 to L24 -> L29 [1] lasti
  L24 to L25 -> L27 [1] lasti
  L25 to L26 -> L29 [1] lasti
  L27 to L29 -> L29 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "app\services\ingestion\normalizers.py", line 424>:
424           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('payload')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object normalize_followupboss_payload at 0x0000018C17D455D0, file "app\services\ingestion\normalizers.py", line 424>:
 424            RESUME                   0

 433            NOP

 434    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (payload)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        13 (to L3)
                NOT_TAKEN

 435            LOAD_GLOBAL              5 (_failed + NULL)
                LOAD_CONST               1 ('payload_not_a_dict')
                BUILD_LIST               1
                CALL                     1
        L2:     RETURN_VALUE

 440    L3:     LOAD_FAST                0 (payload)
                STORE_FAST               1 (body)

 441            LOAD_CONST              22 (('data', 'person', 'lead'))
                GET_ITER
        L4:     FOR_ITER                56 (to L9)
                STORE_FAST               2 (wrap)

 442            LOAD_FAST_BORROW         0 (payload)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_FAST_BORROW         2 (wrap)
                CALL                     1
                STORE_FAST               3 (inner)

 443            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (inner)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
        L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           44 (to L4)
        L6:     LOAD_FAST_BORROW         3 (inner)
                TO_BOOL
        L7:     POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           54 (to L4)

 444    L8:     LOAD_FAST                3 (inner)
                STORE_FAST               1 (body)

 445            POP_TOP
                JUMP_FORWARD             2 (to L10)

 441    L9:     END_FOR
                POP_ITER

 447   L10:     LOAD_GLOBAL              3 (dict + NULL)
                LOAD_FAST_BORROW         1 (body)
                CALL                     1
                STORE_FAST               4 (flat)

 451            LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               2 ('phones')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               3 ('phoneNumbers')
                CALL                     1
       L13:     STORE_FAST               5 (phones)

 452            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (phones)
                LOAD_GLOBAL              8 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       74 (to L20)
                NOT_TAKEN

 453            LOAD_FAST_BORROW         5 (phones)
                GET_ITER
       L14:     FOR_ITER                67 (to L19)
                STORE_FAST               6 (entry)

 454            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         6 (entry)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
       L15:     POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L14)

 455   L16:     LOAD_GLOBAL             11 (_safe_str + NULL)
                LOAD_FAST_BORROW         6 (entry)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               4 ('value')
                CALL                     1
                CALL                     1
                STORE_FAST               7 (v)

 456            LOAD_FAST_BORROW         7 (v)
                TO_BOOL
       L17:     POP_JUMP_IF_TRUE         3 (to L18)
                NOT_TAKEN
                JUMP_BACKWARD           63 (to L14)

 457   L18:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 116 (v, flat)
                LOAD_CONST               5 ('phone')
                STORE_SUBSCR

 458            POP_TOP
                JUMP_FORWARD             2 (to L20)

 453   L19:     END_FOR
                POP_ITER

 461   L20:     LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               6 ('emails')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L23)
       L21:     NOT_TAKEN
       L22:     POP_TOP
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               7 ('emailAddresses')
                CALL                     1
       L23:     STORE_FAST               8 (emails)

 462            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         8 (emails)
                LOAD_GLOBAL              8 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       74 (to L30)
                NOT_TAKEN

 463            LOAD_FAST_BORROW         8 (emails)
                GET_ITER
       L24:     FOR_ITER                67 (to L29)
                STORE_FAST               6 (entry)

 464            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         6 (entry)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
       L25:     POP_JUMP_IF_TRUE         3 (to L26)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L24)

 465   L26:     LOAD_GLOBAL             11 (_safe_str + NULL)
                LOAD_FAST_BORROW         6 (entry)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               4 ('value')
                CALL                     1
                CALL                     1
                STORE_FAST               7 (v)

 466            LOAD_FAST_BORROW         7 (v)
                TO_BOOL
       L27:     POP_JUMP_IF_TRUE         3 (to L28)
                NOT_TAKEN
                JUMP_BACKWARD           63 (to L24)

 467   L28:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 116 (v, flat)
                LOAD_CONST               8 ('email')
                STORE_SUBSCR

 468            POP_TOP
                JUMP_FORWARD             2 (to L30)

 463   L29:     END_FOR
                POP_ITER

 471   L30:     LOAD_FAST_BORROW         4 (flat)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               9 ('name')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE       116 (to L40)
       L31:     NOT_TAKEN
       L32:     LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST              10 ('firstName')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        24 (to L36)
       L33:     NOT_TAKEN
       L34:     LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST              11 ('lastName')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       70 (to L40)
       L35:     NOT_TAKEN

 472   L36:     LOAD_CONST              12 (' ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_CONST              13 (<code object <genexpr> at 0x0000018C17972550, file "app\services\ingestion\normalizers.py", line 472>)
                MAKE_FUNCTION

 473            LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST              10 ('firstName')
                CALL                     1
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST              11 ('lastName')
                CALL                     1
                BUILD_TUPLE              2
                GET_ITER

 472            CALL                     0
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L39)
       L37:     NOT_TAKEN
       L38:     POP_TOP

 475            LOAD_CONST              14 (None)

 472   L39:     LOAD_FAST_BORROW         4 (flat)
                LOAD_CONST               9 ('name')
                STORE_SUBSCR

 478   L40:     LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST              15 ('source')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       34 (to L43)
       L41:     NOT_TAKEN

 479   L42:     LOAD_FAST_BORROW         4 (flat)
                LOAD_ATTR               15 (setdefault + NULL|self)
                LOAD_CONST              16 ('lead_source')
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST              15 ('source')
                CALL                     1
                CALL                     2
                POP_TOP

 481   L43:     LOAD_GLOBAL             17 (_build_lead_from_aliases + NULL)

 482            LOAD_FAST_BORROW         4 (flat)
                LOAD_CONST              17 ('followupboss')

 481            LOAD_CONST              18 (('source',))
                CALL_KW                  2
                UNPACK_SEQUENCE          3
                STORE_FAST_STORE_FAST  154 (lead, warnings)
                STORE_FAST              11 (errors)

 484            LOAD_FAST_BORROW        11 (errors)
                TO_BOOL
                POP_JUMP_IF_TRUE         5 (to L44)
                NOT_TAKEN
                LOAD_FAST_BORROW         9 (lead)
                POP_JUMP_IF_NOT_NONE    23 (to L49)
                NOT_TAKEN

 485   L44:     LOAD_GLOBAL              5 (_failed + NULL)
                LOAD_FAST               11 (errors)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         4 (to L47)
       L45:     NOT_TAKEN
       L46:     POP_TOP
                LOAD_CONST              19 ('normalize_failed')
                BUILD_LIST               1
       L47:     CALL                     1
       L48:     RETURN_VALUE

 486   L49:     LOAD_GLOBAL             19 (_ok + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (lead, warnings)
                CALL                     2
       L50:     RETURN_VALUE

  --   L51:     PUSH_EXC_INFO

 487            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       88 (to L56)
                NOT_TAKEN
                STORE_FAST              12 (e)

 488   L52:     LOAD_GLOBAL             22 (logger)
                LOAD_ATTR               25 (warning + NULL|self)

 489            LOAD_CONST              20 ('normalize_followupboss_payload unexpected error type=')

 490            LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE

 489            BUILD_STRING             2

 488            CALL                     1
                POP_TOP

 492            LOAD_GLOBAL              5 (_failed + NULL)
                LOAD_CONST              21 ('normalizer_exception:')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1
                CALL                     1
       L53:     SWAP                     2
       L54:     POP_EXCEPT
                LOAD_CONST              14 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RETURN_VALUE

  --   L55:     LOAD_CONST              14 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RERAISE                  1

 487   L56:     RERAISE                  0

  --   L57:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L51 [0]
  L3 to L5 -> L51 [0]
  L6 to L7 -> L51 [0]
  L8 to L11 -> L51 [0]
  L12 to L15 -> L51 [0]
  L16 to L17 -> L51 [0]
  L18 to L21 -> L51 [0]
  L22 to L25 -> L51 [0]
  L26 to L27 -> L51 [0]
  L28 to L31 -> L51 [0]
  L32 to L33 -> L51 [0]
  L34 to L35 -> L51 [0]
  L36 to L37 -> L51 [0]
  L38 to L41 -> L51 [0]
  L42 to L45 -> L51 [0]
  L46 to L48 -> L51 [0]
  L49 to L50 -> L51 [0]
  L51 to L52 -> L57 [1] lasti
  L52 to L53 -> L55 [1] lasti
  L53 to L54 -> L57 [1] lasti
  L55 to L57 -> L57 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C17972550, file "app\services\ingestion\normalizers.py", line 472>:
 472           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 473   L2:     FOR_ITER                55 (to L7)
               STORE_FAST               1 (p)

 474           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (p)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL

 473   L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           27 (to L2)

 474   L4:     LOAD_FAST_BORROW         1 (p)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               TO_BOOL

 473   L5:     POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               JUMP_BACKWARD           51 (to L2)
       L6:     LOAD_FAST_BORROW         1 (p)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           57 (to L2)
       L7:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L8:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L8 [0] lasti
  L4 to L5 -> L8 [0] lasti
  L6 to L8 -> L8 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app\services\ingestion\normalizers.py", line 495>:
495           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('payload')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object normalize_gohighlevel_payload at 0x0000018C17ED7080, file "app\services\ingestion\normalizers.py", line 495>:
 495            RESUME                   0

 504            NOP

 505    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (payload)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        13 (to L3)
                NOT_TAKEN

 506            LOAD_GLOBAL              5 (_failed + NULL)
                LOAD_CONST               1 ('payload_not_a_dict')
                BUILD_LIST               1
                CALL                     1
        L2:     RETURN_VALUE

 508    L3:     LOAD_FAST                0 (payload)
                STORE_FAST               1 (body)

 509            LOAD_CONST              11 (('contact', 'data', 'lead'))
                GET_ITER
        L4:     FOR_ITER                56 (to L9)
                STORE_FAST               2 (wrap)

 510            LOAD_FAST_BORROW         0 (payload)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_FAST_BORROW         2 (wrap)
                CALL                     1
                STORE_FAST               3 (inner)

 511            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (inner)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
        L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           44 (to L4)
        L6:     LOAD_FAST_BORROW         3 (inner)
                TO_BOOL
        L7:     POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           54 (to L4)

 512    L8:     LOAD_FAST                3 (inner)
                STORE_FAST               1 (body)

 513            POP_TOP
                JUMP_FORWARD             2 (to L10)

 509    L9:     END_FOR
                POP_ITER

 515   L10:     LOAD_GLOBAL              3 (dict + NULL)
                LOAD_FAST_BORROW         1 (body)
                CALL                     1
                STORE_FAST               4 (flat)

 520            LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               2 ('leadSource')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       34 (to L11)
                NOT_TAKEN

 521            LOAD_FAST_BORROW         4 (flat)
                LOAD_ATTR                9 (setdefault + NULL|self)
                LOAD_CONST               3 ('lead_source')
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               2 ('leadSource')
                CALL                     1
                CALL                     2
                POP_TOP

 522   L11:     LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               4 ('campaign')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       34 (to L14)
       L12:     NOT_TAKEN

 523   L13:     LOAD_FAST_BORROW         4 (flat)
                LOAD_ATTR                9 (setdefault + NULL|self)
                LOAD_CONST               4 ('campaign')
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               4 ('campaign')
                CALL                     1
                CALL                     2
                POP_TOP

 525   L14:     LOAD_GLOBAL             11 (_build_lead_from_aliases + NULL)

 526            LOAD_FAST_BORROW         4 (flat)
                LOAD_CONST               5 ('gohighlevel')

 525            LOAD_CONST               6 (('source',))
                CALL_KW                  2
                UNPACK_SEQUENCE          3
                STORE_FAST_STORE_FAST   86 (lead, warnings)
                STORE_FAST               7 (errors)

 528            LOAD_FAST_BORROW         7 (errors)
                TO_BOOL
                POP_JUMP_IF_TRUE         5 (to L15)
                NOT_TAKEN
                LOAD_FAST_BORROW         5 (lead)
                POP_JUMP_IF_NOT_NONE    23 (to L20)
                NOT_TAKEN

 529   L15:     LOAD_GLOBAL              5 (_failed + NULL)
                LOAD_FAST                7 (errors)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         4 (to L18)
       L16:     NOT_TAKEN
       L17:     POP_TOP
                LOAD_CONST               8 ('normalize_failed')
                BUILD_LIST               1
       L18:     CALL                     1
       L19:     RETURN_VALUE

 530   L20:     LOAD_GLOBAL             13 (_ok + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (lead, warnings)
                CALL                     2
       L21:     RETURN_VALUE

  --   L22:     PUSH_EXC_INFO

 531            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       88 (to L27)
                NOT_TAKEN
                STORE_FAST               8 (e)

 532   L23:     LOAD_GLOBAL             16 (logger)
                LOAD_ATTR               19 (warning + NULL|self)

 533            LOAD_CONST               9 ('normalize_gohighlevel_payload unexpected error type=')

 534            LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE

 533            BUILD_STRING             2

 532            CALL                     1
                POP_TOP

 536            LOAD_GLOBAL              5 (_failed + NULL)
                LOAD_CONST              10 ('normalizer_exception:')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1
                CALL                     1
       L24:     SWAP                     2
       L25:     POP_EXCEPT
                LOAD_CONST               7 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RETURN_VALUE

  --   L26:     LOAD_CONST               7 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 531   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L22 [0]
  L3 to L5 -> L22 [0]
  L6 to L7 -> L22 [0]
  L8 to L12 -> L22 [0]
  L13 to L16 -> L22 [0]
  L17 to L19 -> L22 [0]
  L20 to L21 -> L22 [0]
  L22 to L23 -> L28 [1] lasti
  L23 to L24 -> L26 [1] lasti
  L24 to L25 -> L28 [1] lasti
  L26 to L28 -> L28 [1] lasti
```
