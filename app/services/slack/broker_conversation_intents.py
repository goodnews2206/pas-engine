"""
PAS204 — Broker conversation intent classifier.

Deterministic, read-only classifier that maps messy human broker
phrases into the closed PAS204 intent set declared in
`broker_question_catalogue.INTENT_CODES`.

The classifier is:

  * Pure-function. Same input -> same output forever.
  * Closed-vocabulary. Output is always one of INTENT_CODES; the
    catch-all is INTENT_FALLBACK_CLARIFY.
  * Typo-tolerant via single-edit-distance keyword matching
    (deletions / insertions / substitutions). No LLM. No fuzzy ML.
  * No I/O. No network. No mutation. No imports beyond stdlib +
    the broker_question_catalogue module that owns the intent
    vocabulary.
"""

from __future__ import annotations

from typing import Dict, FrozenSet, Tuple

from app.services.slack.broker_question_catalogue import (
    INTENT_AFTER_HOURS_COVERAGE,
    INTENT_AGENT_ROUTING_STATUS,
    INTENT_APPOINTMENTS_TODAY,
    INTENT_CALLBACK_REQUESTS,
    INTENT_CODES,
    INTENT_CRM_SYNC_STATUS,
    INTENT_DASHBOARD_EXPLANATION,
    INTENT_EVIDENCE_DIGEST,
    INTENT_FACEBOOK_LEAD_HANDLING,
    INTENT_FALLBACK_CLARIFY,
    INTENT_HOT_LEADS_SUMMARY,
    INTENT_INTEGRATION_QUESTIONS,
    INTENT_ISA_COMPARISON,
    INTENT_LEAD_SOURCE_QUALITY,
    INTENT_LEADS_TODAY_COUNT,
    INTENT_MISSED_LEADS,
    INTENT_ONBOARDING_HELP,
    INTENT_REALTOR_LEAD_HANDLING,
    INTENT_RESPONSE_SPEED,
    INTENT_SAFETY_TRUST,
    INTENT_STALE_LEADS,
    INTENT_TRAINING_PAS,
    INTENT_WHAT_SHOULD_I_DO,
    INTENT_ZILLOW_LEAD_HANDLING,
)


# ──────────────────────────────────────────────────────────────────
# Keyword tables — primary tokens carry the strongest evidence
# for an intent; supporting tokens disambiguate similar phrases.
# ──────────────────────────────────────────────────────────────────

_KW_LEAD          = frozenset(("lead", "leads", "leeds", "leed", "leeds", "lds"))
_KW_TODAY         = frozenset(("today", "todays", "today's", "tonite", "tonight"))
_KW_HOT           = frozenset(("hot", "warm", "engaged", "hottest", "fire", "ready"))
_KW_MISSED        = frozenset((
    "missed", "miss", "dropped", "drop", "slip", "slipped",
    "no-response", "noresponse", "didnt", "didn't", "never",
    "uncontacted",
))
_KW_STALE         = frozenset((
    "stale", "old", "cold", "aging", "aged", "forgotten",
    "dust", "gathering", "nudge", "revive", "havent", "haven't",
    "touched", "untouched", "while",
))
_KW_CALLBACK      = frozenset((
    "callback", "callbacks", "call-back", "call-backs",
    "callbk", "clb", "clbs", "cllbck", "cb", "cbs",
))
_KW_APPT          = frozenset((
    "booking", "bookings", "appt", "appts", "appointment",
    "appointments", "showing", "showings", "bkg", "bkgs",
    "scheduled", "book", "booked", "booking", "tour",
))
_KW_AGENT         = frozenset((
    "agent", "agents", "agnt", "agnts", "rotation", "routing",
    "assigned", "assignment", "routed",
))
_KW_RESPONSE_SPEED = frozenset((
    "speed", "fast", "quick", "latency", "rapid",
    "responding", "respond", "respnse", "reply", "replies",
    "replying", "response",
))
_KW_SOURCE        = frozenset((
    "source", "src", "sources", "channel", "channels",
))
_KW_CRM           = frozenset((
    "crm", "followup", "followupboss", "fub", "lofty",
    "sync", "synced", "syncing",
))
_KW_ZILLOW        = frozenset(("zillow", "zilow", "zillw", "flex"))
_KW_REALTOR       = frozenset(("realtor", "realtor.com", "rltr"))
_KW_FACEBOOK      = frozenset(("facebook", "fb", "meta"))
_KW_ISA           = frozenset(("isa", "isas", "human", "internal", "sales"))
_KW_AFTER_HOURS   = frozenset((
    "after", "after-hours", "after-hrs", "afterhours", "hrs",
    "overnight", "weekends", "weekend", "nights",
    "late",
))
_KW_TRAIN         = frozenset((
    "train", "training", "teach", "tune", "retrain",
    "improve", "fine", "tweak", "script", "scripts",
    "learn", "adjust", "tone",
))
# Verb tokens that mean "wire two systems together". These
# beat source-specific intents because they shift the question
# from "how does PAS handle X leads" to "how do I set X up".
_KW_INTEGRATION_VERB = frozenset((
    "connect", "integrate", "hook", "hookup", "setup",
    "set-up", "wire", "link",
))
# Noun tokens that *describe* an integration. These lose to
# source-specific intents when a source/CRM token is also
# present ("zillow integration" -> zillow; "set up integration"
# -> integration).
_KW_INTEGRATION_NOUN = frozenset((
    "integration", "integrations", "connection", "supported",
    "supports", "calendar",
))
_KW_DASHBOARD     = frozenset((
    "dashboard", "dashbord", "dash", "metrics", "metric",
    "numbers", "explain", "walkme", "tour", "green",
    "rate", "conversion", "mean",
))
_KW_DIGEST        = frozenset((
    "digest", "rehearsal", "simulation", "simulations",
    "evidence", "pas201", "proof", "prove", "proved", "proves",
    "showed",
))
_KW_SAFETY        = frozenset((
    "safe", "safety", "trust", "trusted", "risk", "risky",
    "embarrass", "embarrasses", "approved", "approve",
    "bad", "ok",
))
_KW_WHAT_NEXT     = frozenset((
    "what", "should", "do", "next", "priority", "priorities",
    "important", "focus", "attention", "matters", "next-action",
    "nextaction",
))


# Supporting / disambiguation tokens. These help separate
# similar-looking intents (e.g., "show me the digest" vs.
# "show me hot leads").
_KW_PAS           = frozenset(("pas", "p.a.s"))
_KW_HANDLING      = frozenset((
    "handling", "handled", "handle", "respond", "response",
    "responded", "pipeline", "treat", "routing", "answer",
    "answered",
))
_KW_COMPARE       = frozenset((
    "vs", "compare", "compared", "comparison", "replace",
    "replacement", "better", "benchmark", "benchmarks",
    "performance",
))


# ──────────────────────────────────────────────────────────────────
# Tokenisation + typo-tolerant matching
# ──────────────────────────────────────────────────────────────────

_PUNCT = set(".,!?;:()[]{}\"'`")


def _normalize(text: str) -> str:
    if not isinstance(text, str):
        return ""
    s = text.strip().lower()
    if not s:
        return ""
    s = " ".join(s.split())
    # Strip trailing punctuation.
    for _ in range(4):
        if s and s[-1] in "?.!,":
            s = s[:-1].rstrip()
        else:
            break
    return s


def _tokenize(text: str) -> Tuple[str, ...]:
    normalized = _normalize(text)
    if not normalized:
        return ()
    out = []
    for raw in normalized.split():
        # Strip leading/trailing punctuation but keep internal
        # tokens like "realtor.com" intact.
        t = raw.strip("".join(_PUNCT))
        if t:
            out.append(t)
    return tuple(out)


def _edit_distance_le_1(a: str, b: str) -> bool:
    """
    True iff Levenshtein distance between a and b is <= 1
    (substitution / insertion / deletion). Pure-python, O(len(a)).
    """
    if a == b:
        return True
    la, lb = len(a), len(b)
    if abs(la - lb) > 1:
        return False
    # Make `a` the shorter or equal one.
    if la > lb:
        a, b = b, a
        la, lb = lb, la
    # Now la <= lb.
    if la == lb:
        # substitution case
        diff = 0
        for x, y in zip(a, b):
            if x != y:
                diff += 1
                if diff > 1:
                    return False
        return True
    # la + 1 == lb: insertion in `b` relative to `a`.
    i = j = 0
    edited = False
    while i < la and j < lb:
        if a[i] == b[j]:
            i += 1
            j += 1
        elif edited:
            return False
        else:
            edited = True
            j += 1
    return True


def _token_matches_keyword_set(token: str, kw_set: FrozenSet[str]) -> bool:
    if token in kw_set:
        return True
    # Typo-tolerant fallback for tokens >= 5 chars matched
    # against keywords >= 5 chars. The 5-char minimum on both
    # sides keeps the fuzzy matcher from collapsing short
    # near-homophones (`book` <-> `hook`, `rate` <-> `late`,
    # `look` <-> `hook`) which are different *concepts*.
    if len(token) < 5:
        return False
    for kw in kw_set:
        if len(kw) < 5:
            continue
        if _edit_distance_le_1(token, kw):
            return True
    return False


def _tokens_match_any(tokens: Tuple[str, ...], kw_set: FrozenSet[str]) -> bool:
    for t in tokens:
        if _token_matches_keyword_set(t, kw_set):
            return True
    return False


def _tokens_match_count(
    tokens: Tuple[str, ...], kw_set: FrozenSet[str],
) -> int:
    n = 0
    seen: set = set()
    for t in tokens:
        if t in seen:
            continue
        if _token_matches_keyword_set(t, kw_set):
            n += 1
            seen.add(t)
    return n


# ──────────────────────────────────────────────────────────────────
# Intent scoring
# ──────────────────────────────────────────────────────────────────
#
# Each intent has a `score(tokens)` function that returns an int.
# Higher = stronger evidence the intent matches. The classifier
# picks the highest-scoring intent that clears the minimum
# threshold; ties prefer the first intent in INTENT_PRIORITY_ORDER.
# Anything that scores zero falls back to INTENT_FALLBACK_CLARIFY.

_MIN_SCORE: int = 2


def _score_leads_today_count(tokens: Tuple[str, ...]) -> int:
    if not _tokens_match_any(tokens, _KW_LEAD):
        return 0
    if _tokens_match_any(tokens, _KW_TODAY):
        return 4
    # "new leads" / "lead count" without "today" still maps here.
    if "new" in tokens or "count" in tokens:
        return 3
    return 0


def _score_hot_leads(tokens: Tuple[str, ...]) -> int:
    if _tokens_match_any(tokens, _KW_HOT):
        if _tokens_match_any(tokens, _KW_LEAD) or "ones" in tokens or "first" in tokens:
            return 4
        return 2  # bare "hot" / "warm"
    # "which leads should i call first" - hot-ish without "hot".
    if _tokens_match_any(tokens, _KW_LEAD) and "first" in tokens and "call" in tokens:
        return 4
    return 0


def _score_missed_leads(tokens: Tuple[str, ...]) -> int:
    has_lead = _tokens_match_any(tokens, _KW_LEAD)
    if _tokens_match_any(tokens, _KW_MISSED):
        if has_lead or "anyone" in tokens or "through" in tokens:
            return 4
        return 2
    # "no response leads" / "leads with no response" /
    # "leads with no contact" / "leads we never called"
    if has_lead and (
        "no" in tokens
        or "contact" in tokens
        or "respond" in tokens
        or "response" in tokens
    ):
        return 4
    return 0


def _score_stale_leads(tokens: Tuple[str, ...]) -> int:
    if not _tokens_match_any(tokens, _KW_STALE):
        return 0
    if _tokens_match_any(tokens, _KW_LEAD):
        return 4
    return 2


def _score_callbacks(tokens: Tuple[str, ...]) -> int:
    if _tokens_match_any(tokens, _KW_CALLBACK):
        return 4
    # "call backs" — two-token form.
    if "call" in tokens and ("back" in tokens or "backs" in tokens):
        return 4
    return 0


def _score_appointments(tokens: Tuple[str, ...]) -> int:
    if not _tokens_match_any(tokens, _KW_APPT):
        return 0
    return 4


def _score_agent_routing(tokens: Tuple[str, ...]) -> int:
    if _tokens_match_any(tokens, _KW_AGENT):
        score = 2
        for k in ("rotation", "routing", "assigned", "assignment",
                  "coverage", "handling", "gets", "takes", "routed"):
            if k in tokens:
                score = 4
                break
        return score
    # "are leads being routed", "who takes the next lead"
    has_lead = _tokens_match_any(tokens, _KW_LEAD)
    if has_lead and ("routed" in tokens or "routing" in tokens
                     or "takes" in tokens):
        return 4
    return 0


def _score_response_speed(tokens: Tuple[str, ...]) -> int:
    if _tokens_match_any(tokens, _KW_RESPONSE_SPEED):
        if _tokens_match_any(tokens, _KW_LEAD) and "speed" in tokens:
            return 4
        if "time" in tokens or "latency" in tokens or "fast" in tokens:
            return 4
        return 3
    # "time to first contact" — no "respond" / "speed" / "fast"
    # token in itself, but the phrase is unambiguously about
    # response speed.
    if "time" in tokens and "first" in tokens and "contact" in tokens:
        return 4
    return 0


def _score_lead_source(tokens: Tuple[str, ...]) -> int:
    has_source = _tokens_match_any(tokens, _KW_SOURCE)
    has_lead = _tokens_match_any(tokens, _KW_LEAD)
    if "channel" in tokens or "channels" in tokens:
        return 5  # bump so it beats dashboard's "conversion"/"rate"
    if has_source:
        # source + (conversion / converts / best / worst /
        # rates) must beat dashboard's generic dashboard token
        # hits (priority + score).
        if (
            "best" in tokens or "worst" in tokens
            or "converts" in tokens or "conversion" in tokens
            or "rates" in tokens
        ):
            return 5
        if "from" in tokens and "where" in tokens:
            return 5
        if has_lead and ("source" in tokens or "src" in tokens):
            return 4
        return 3
    if has_lead and "where" in tokens and "from" in tokens:
        return 5
    return 0


def _score_crm(tokens: Tuple[str, ...]) -> int:
    if not _tokens_match_any(tokens, _KW_CRM):
        return 0
    return 4


def _score_zillow(tokens: Tuple[str, ...]) -> int:
    if _tokens_match_any(tokens, _KW_ZILLOW):
        return 5  # rare token, high signal
    return 0


def _score_realtor(tokens: Tuple[str, ...]) -> int:
    if _tokens_match_any(tokens, _KW_REALTOR):
        return 5
    return 0


def _score_facebook(tokens: Tuple[str, ...]) -> int:
    if _tokens_match_any(tokens, _KW_FACEBOOK):
        return 5
    return 0


def _score_isa(tokens: Tuple[str, ...]) -> int:
    if not _tokens_match_any(tokens, _KW_ISA):
        return 0
    if _tokens_match_any(tokens, _KW_COMPARE) or "replace" in tokens:
        return 5
    return 3


def _score_after_hours(tokens: Tuple[str, ...]) -> int:
    if not _tokens_match_any(tokens, _KW_AFTER_HOURS):
        if "2am" in tokens or "6pm" in tokens or "midnight" in tokens:
            return 4
        return 0
    return 4


def _score_training(tokens: Tuple[str, ...]) -> int:
    if not _tokens_match_any(tokens, _KW_TRAIN):
        return 0
    if _tokens_match_any(tokens, _KW_PAS) or "script" in tokens or "tone" in tokens:
        return 5
    return 3


def _score_integrations(tokens: Tuple[str, ...]) -> int:
    # Verb tokens always score 6 — they always mean "set this
    # up", regardless of which service is mentioned.
    if _tokens_match_any(tokens, _KW_INTEGRATION_VERB):
        return 6
    # Noun tokens only score when no source/CRM keyword is also
    # present. Otherwise the question is really about the
    # source ("zillow integration" -> zillow_lead_handling,
    # "crm connection" -> crm_sync_status).
    if _tokens_match_any(tokens, _KW_INTEGRATION_NOUN):
        if not (
            _tokens_match_any(tokens, _KW_ZILLOW)
            or _tokens_match_any(tokens, _KW_REALTOR)
            or _tokens_match_any(tokens, _KW_FACEBOOK)
            or _tokens_match_any(tokens, _KW_CRM)
        ):
            return 5
    return 0


def _score_dashboard(tokens: Tuple[str, ...]) -> int:
    if not _tokens_match_any(tokens, _KW_DASHBOARD):
        return 0
    # If a source token is also present, the question is really
    # about that source's conversion / rate — defer to
    # lead_source_quality.
    if _tokens_match_any(tokens, _KW_SOURCE):
        return 0
    return 4


def _score_digest(tokens: Tuple[str, ...]) -> int:
    if _tokens_match_any(tokens, _KW_DIGEST):
        score = 3
        for k in ("digest", "evidence", "pas201", "rehearsal", "proof",
                  "proved", "prove", "proves", "results", "showed"):
            if k in tokens:
                score = 5
                break
        return score
    # "test results" / "latest test" / "what does the latest
    # test show" — `test` is too broad to put in the keyword set
    # on its own (collides with the `test`/`hi`/`yo` fallback
    # questions), but with a digest-y companion token it is
    # unambiguous.
    if ("test" in tokens or "tests" in tokens) and (
        "results" in tokens or "latest" in tokens
        or "show" in tokens or "showed" in tokens
    ):
        return 4
    return 0


def _score_safety(tokens: Tuple[str, ...]) -> int:
    if not _tokens_match_any(tokens, _KW_SAFETY):
        return 0
    return 4


_KW_ONBOARDING_VERBS = frozenset((
    "use", "start", "begin", "begun", "started", "starting",
    "use-pas", "started",
))


def _score_onboarding_help(tokens: Tuple[str, ...]) -> int:
    # Strict onboarding patterns only — avoid hijacking phrases
    # like "is pas safe to use" (safety_trust), "does pas do
    # what an isa does" (isa_comparison), or "which agents are
    # getting leads" (agent_routing_status).
    if not tokens:
        return 0
    # Disambiguator: if the phrase carries strong specific
    # signal for another intent, bail out.
    if _tokens_match_any(tokens, _KW_SAFETY):
        return 0
    if _tokens_match_any(tokens, _KW_ISA):
        return 0
    if _tokens_match_any(tokens, _KW_AGENT):
        return 0
    if _tokens_match_any(tokens, _KW_LEAD):
        return 0
    # "how do i use this thing" / "how do i even use this thing"
    # / "how do i even fuckin use this thing" / "how does this
    # thing work".
    if "thing" in tokens and (
        "use" in tokens or "work" in tokens
        or "fuckin" in tokens or "fucking" in tokens
    ):
        return 5
    # "what can pas do" / "what can you do"
    if (
        ("what" in tokens or "whats" in tokens or "what's" in tokens)
        and ("can" in tokens or "do" in tokens or "does" in tokens)
        and (_tokens_match_any(tokens, _KW_PAS) or "you" in tokens)
    ):
        return 5
    # "how do i use pas"
    if (
        "use" in tokens
        and _tokens_match_any(tokens, _KW_PAS)
        and ("how" in tokens or "i" in tokens)
    ):
        return 5
    # "help me use pas" / "help me get started"
    if (
        "help" in tokens and "me" in tokens
        and (
            _tokens_match_any(tokens, _KW_PAS) or "use" in tokens
            or "start" in tokens or "begin" in tokens
            or "started" in tokens
        )
    ):
        return 5
    # "where do i start" / "how should i start" / "getting
    # started" / "how do i begin"
    if ("start" in tokens or "begin" in tokens or "started" in tokens) and (
        "where" in tokens or "should" in tokens
        or "getting" in tokens or "begun" in tokens
        or ("how" in tokens and ("i" in tokens or "do" in tokens))
    ):
        return 5
    # "i don't know what to ask" / "what should i ask you"
    if "ask" in tokens and (
        "dont" in tokens or "don't" in tokens or "idk" in tokens
        or ("should" in tokens and "i" in tokens)
    ):
        return 5
    return 0


def _score_what_next(tokens: Tuple[str, ...]) -> int:
    # "what should i do now / next" — needs at least 2 of {what, do, next/priority/focus/important/matters}.
    score = 0
    if "what" in tokens or "whats" in tokens:
        score += 1
    if "do" in tokens or "should" in tokens:
        score += 1
    for k in ("next", "priority", "priorities", "important", "focus",
              "attention", "matters", "tackle", "where", "first"):
        if k in tokens:
            score += 2
            break
    if "what's" in tokens and "important" in tokens:
        score += 1
    return score


# Order matters when multiple intents tie — first wins.
# Integration tokens (connect/integrate/hook/setup/supported)
# must beat source-specific tokens — "connect zillow" is an
# integrations question, not a zillow lead-handling question.
# Likewise CRM tokens. We resolve this by scoring integrations
# at +6 and CRM-without-integration at +4, then picking max.
_INTENT_SCORERS: Tuple[Tuple[str, callable], ...] = (
    # Integration intent first — highest score (6) wins over
    # source-specific intents (5) when "connect"/"hook"/"setup"
    # tokens dominate.
    (INTENT_INTEGRATION_QUESTIONS,  _score_integrations),
    # Source-specific intents (rare tokens, high signal).
    (INTENT_ZILLOW_LEAD_HANDLING,   _score_zillow),
    (INTENT_REALTOR_LEAD_HANDLING,  _score_realtor),
    (INTENT_FACEBOOK_LEAD_HANDLING, _score_facebook),
    # Evidence digest is unambiguous when its keyword set hits.
    (INTENT_EVIDENCE_DIGEST,        _score_digest),
    # ISA comparison is rare-token, prefer over generic.
    (INTENT_ISA_COMPARISON,         _score_isa),
    # CRM is unambiguous.
    (INTENT_CRM_SYNC_STATUS,        _score_crm),
    # After-hours / dashboard / training / safety are unambiguous.
    (INTENT_AFTER_HOURS_COVERAGE,   _score_after_hours),
    (INTENT_DASHBOARD_EXPLANATION,  _score_dashboard),
    (INTENT_TRAINING_PAS,           _score_training),
    (INTENT_SAFETY_TRUST,           _score_safety),
    # Lead-source ordering before generic leads intents so
    # "best lead source" doesn't tie to "leads_today".
    (INTENT_LEAD_SOURCE_QUALITY,    _score_lead_source),
    (INTENT_CALLBACK_REQUESTS,      _score_callbacks),
    (INTENT_APPOINTMENTS_TODAY,     _score_appointments),
    (INTENT_AGENT_ROUTING_STATUS,   _score_agent_routing),
    (INTENT_RESPONSE_SPEED,         _score_response_speed),
    # Lead-state intents.
    (INTENT_MISSED_LEADS,           _score_missed_leads),
    (INTENT_STALE_LEADS,            _score_stale_leads),
    (INTENT_HOT_LEADS_SUMMARY,      _score_hot_leads),
    (INTENT_LEADS_TODAY_COUNT,      _score_leads_today_count),
    # Onboarding-help is a generic catch — placed near the end so
    # specific intents take precedence; but BEFORE what_should_i_do
    # so "what can pas do" doesn't get swallowed by the priorities
    # scorer.
    (INTENT_ONBOARDING_HELP,        _score_onboarding_help),
    # What-should-i-do is the most generic; goes last.
    (INTENT_WHAT_SHOULD_I_DO,       _score_what_next),
)


# ──────────────────────────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────────────────────────

def match_broker_intent(text: str) -> Dict[str, object]:
    """
    Classify operator-typed text into a closed PAS204 intent.

    Returns a closed envelope:

        {
            "intent":            <one of INTENT_CODES>,
            "score":             int,
            "normalized_phrase": str,
            "tokens":            Tuple[str, ...],
        }

    INTENT_FALLBACK_CLARIFY is returned for empty input, tokens
    that match no intent above the minimum threshold, or text that
    triggers no scorer at all.
    """
    tokens = _tokenize(text)
    normalized = _normalize(text)
    if not tokens:
        return {
            "intent":            INTENT_FALLBACK_CLARIFY,
            "score":             0,
            "normalized_phrase": normalized,
            "tokens":            tokens,
        }

    best_intent = INTENT_FALLBACK_CLARIFY
    best_score = 0
    for intent_code, scorer in _INTENT_SCORERS:
        s = scorer(tokens)
        if s > best_score:
            best_score = s
            best_intent = intent_code

    if best_score < _MIN_SCORE:
        return {
            "intent":            INTENT_FALLBACK_CLARIFY,
            "score":             best_score,
            "normalized_phrase": normalized,
            "tokens":            tokens,
        }
    return {
        "intent":            best_intent,
        "score":             best_score,
        "normalized_phrase": normalized,
        "tokens":            tokens,
    }


def list_supported_intents() -> Tuple[str, ...]:
    return INTENT_CODES
