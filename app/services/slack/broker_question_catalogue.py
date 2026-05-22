"""
PAS204 — Broker question catalogue.

Closed catalogue of >= 300 realistic broker-style questions and
requests across 22 conversational intents. Every entry is a
plain-Python dict so the catalogue can be diff'd, audited, and
deterministically iterated; there is no I/O and no randomness
anywhere in this module.

The catalogue includes deliberately messy human phrasing:

  * typos                  ("how mny leeds today")
  * shorthand              ("hot leads pls")
  * unfinished context     ("zillow lead just came in")
  * casual phrasing        ("any new biz today")
  * confused-beginner      ("how do i even use this thing")
  * impatient-owner        ("just tell me what's important")

PAS204's classifier (broker_conversation_intents.match_broker_intent)
maps these into a closed intent set. The response voice
(broker_response_voice) translates technical PAS tokens into
human staff-style replies. The conversation surface
(broker_conversation_surface) ties them together.

This module is strictly read-only. It imports nothing, opens no
files, calls no external services, and never mutates anything.
"""

from __future__ import annotations

from typing import Dict, Tuple


# ──────────────────────────────────────────────────────────────────
# Category vocabulary (closed)
# ──────────────────────────────────────────────────────────────────

CATEGORY_LEADS_TODAY:           str = "leads_today"
CATEGORY_HOT_LEADS:             str = "hot_leads"
CATEGORY_MISSED_LEADS:          str = "missed_leads"
CATEGORY_STALE_LEADS:           str = "stale_leads"
CATEGORY_CALLBACK_REQUESTS:     str = "callback_requests"
CATEGORY_APPOINTMENTS:          str = "appointments"
CATEGORY_AGENT_ROUTING:         str = "agent_routing"
CATEGORY_RESPONSE_SPEED:        str = "response_speed"
CATEGORY_LEAD_SOURCE_QUALITY:   str = "lead_source_quality"
CATEGORY_CRM_SYNC:              str = "crm_sync"
CATEGORY_ZILLOW:                str = "zillow"
CATEGORY_REALTOR_COM:           str = "realtor_com"
CATEGORY_FACEBOOK:              str = "facebook"
CATEGORY_ISA_COMPARISON:        str = "isa_comparison"
CATEGORY_AFTER_HOURS:           str = "after_hours"
CATEGORY_TRAINING:              str = "training_pas"
CATEGORY_INTEGRATIONS:          str = "integrations"
CATEGORY_DASHBOARD:             str = "dashboard"
CATEGORY_EVIDENCE_DIGEST:       str = "evidence_digest"
CATEGORY_SAFETY_TRUST:          str = "safety_trust"
CATEGORY_WHAT_NEXT:             str = "what_next"
CATEGORY_ONBOARDING:            str = "onboarding"
CATEGORY_FALLBACK_FRAGMENT:     str = "fallback_fragment"


CATEGORIES: Tuple[str, ...] = (
    CATEGORY_LEADS_TODAY,
    CATEGORY_HOT_LEADS,
    CATEGORY_MISSED_LEADS,
    CATEGORY_STALE_LEADS,
    CATEGORY_CALLBACK_REQUESTS,
    CATEGORY_APPOINTMENTS,
    CATEGORY_AGENT_ROUTING,
    CATEGORY_RESPONSE_SPEED,
    CATEGORY_LEAD_SOURCE_QUALITY,
    CATEGORY_CRM_SYNC,
    CATEGORY_ZILLOW,
    CATEGORY_REALTOR_COM,
    CATEGORY_FACEBOOK,
    CATEGORY_ISA_COMPARISON,
    CATEGORY_AFTER_HOURS,
    CATEGORY_TRAINING,
    CATEGORY_INTEGRATIONS,
    CATEGORY_DASHBOARD,
    CATEGORY_EVIDENCE_DIGEST,
    CATEGORY_SAFETY_TRUST,
    CATEGORY_WHAT_NEXT,
    CATEGORY_ONBOARDING,
    CATEGORY_FALLBACK_FRAGMENT,
)


# ──────────────────────────────────────────────────────────────────
# Intent vocabulary (closed). Mirrored by
# broker_conversation_intents.INTENT_CODES.
# ──────────────────────────────────────────────────────────────────

INTENT_LEADS_TODAY_COUNT:      str = "leads_today_count"
INTENT_HOT_LEADS_SUMMARY:      str = "hot_leads_summary"
INTENT_MISSED_LEADS:           str = "missed_leads"
INTENT_STALE_LEADS:            str = "stale_leads"
INTENT_CALLBACK_REQUESTS:      str = "callback_requests"
INTENT_APPOINTMENTS_TODAY:     str = "appointments_today"
INTENT_AGENT_ROUTING_STATUS:   str = "agent_routing_status"
INTENT_RESPONSE_SPEED:         str = "response_speed"
INTENT_LEAD_SOURCE_QUALITY:    str = "lead_source_quality"
INTENT_CRM_SYNC_STATUS:        str = "crm_sync_status"
INTENT_ZILLOW_LEAD_HANDLING:   str = "zillow_lead_handling"
INTENT_REALTOR_LEAD_HANDLING:  str = "realtor_lead_handling"
INTENT_FACEBOOK_LEAD_HANDLING: str = "facebook_lead_handling"
INTENT_ISA_COMPARISON:         str = "isa_comparison"
INTENT_AFTER_HOURS_COVERAGE:   str = "after_hours_coverage"
INTENT_TRAINING_PAS:           str = "training_pas"
INTENT_INTEGRATION_QUESTIONS:  str = "integration_questions"
INTENT_DASHBOARD_EXPLANATION:  str = "dashboard_explanation"
INTENT_EVIDENCE_DIGEST:        str = "evidence_digest_summary"
INTENT_SAFETY_TRUST:           str = "safety_trust"
INTENT_WHAT_SHOULD_I_DO:       str = "what_should_i_do"
INTENT_ONBOARDING_HELP:        str = "onboarding_help"
INTENT_FALLBACK_CLARIFY:       str = "fallback_clarify"


INTENT_CODES: Tuple[str, ...] = (
    INTENT_LEADS_TODAY_COUNT,
    INTENT_HOT_LEADS_SUMMARY,
    INTENT_MISSED_LEADS,
    INTENT_STALE_LEADS,
    INTENT_CALLBACK_REQUESTS,
    INTENT_APPOINTMENTS_TODAY,
    INTENT_AGENT_ROUTING_STATUS,
    INTENT_RESPONSE_SPEED,
    INTENT_LEAD_SOURCE_QUALITY,
    INTENT_CRM_SYNC_STATUS,
    INTENT_ZILLOW_LEAD_HANDLING,
    INTENT_REALTOR_LEAD_HANDLING,
    INTENT_FACEBOOK_LEAD_HANDLING,
    INTENT_ISA_COMPARISON,
    INTENT_AFTER_HOURS_COVERAGE,
    INTENT_TRAINING_PAS,
    INTENT_INTEGRATION_QUESTIONS,
    INTENT_DASHBOARD_EXPLANATION,
    INTENT_EVIDENCE_DIGEST,
    INTENT_SAFETY_TRUST,
    INTENT_WHAT_SHOULD_I_DO,
    INTENT_ONBOARDING_HELP,
    INTENT_FALLBACK_CLARIFY,
)


# ──────────────────────────────────────────────────────────────────
# Compact factory
# ──────────────────────────────────────────────────────────────────

def _q(text: str, intent: str, category: str) -> Dict[str, str]:
    return {"text": text, "intent": intent, "category": category}


# Convenience aliases to keep the table below readable. ALL CAPS
# variables shadow the long INTENT_/CATEGORY_ names.
_LT,  _C_LT  = INTENT_LEADS_TODAY_COUNT,      CATEGORY_LEADS_TODAY
_HL,  _C_HL  = INTENT_HOT_LEADS_SUMMARY,      CATEGORY_HOT_LEADS
_ML,  _C_ML  = INTENT_MISSED_LEADS,           CATEGORY_MISSED_LEADS
_SL,  _C_SL  = INTENT_STALE_LEADS,            CATEGORY_STALE_LEADS
_CB,  _C_CB  = INTENT_CALLBACK_REQUESTS,      CATEGORY_CALLBACK_REQUESTS
_AP,  _C_AP  = INTENT_APPOINTMENTS_TODAY,     CATEGORY_APPOINTMENTS
_AR,  _C_AR  = INTENT_AGENT_ROUTING_STATUS,   CATEGORY_AGENT_ROUTING
_RS,  _C_RS  = INTENT_RESPONSE_SPEED,         CATEGORY_RESPONSE_SPEED
_SQ,  _C_SQ  = INTENT_LEAD_SOURCE_QUALITY,    CATEGORY_LEAD_SOURCE_QUALITY
_CRM, _C_CRM = INTENT_CRM_SYNC_STATUS,        CATEGORY_CRM_SYNC
_ZL,  _C_ZL  = INTENT_ZILLOW_LEAD_HANDLING,   CATEGORY_ZILLOW
_RL,  _C_RL  = INTENT_REALTOR_LEAD_HANDLING,  CATEGORY_REALTOR_COM
_FB,  _C_FB  = INTENT_FACEBOOK_LEAD_HANDLING, CATEGORY_FACEBOOK
_IS,  _C_IS  = INTENT_ISA_COMPARISON,         CATEGORY_ISA_COMPARISON
_AH,  _C_AH  = INTENT_AFTER_HOURS_COVERAGE,   CATEGORY_AFTER_HOURS
_TR,  _C_TR  = INTENT_TRAINING_PAS,           CATEGORY_TRAINING
_IN,  _C_IN  = INTENT_INTEGRATION_QUESTIONS,  CATEGORY_INTEGRATIONS
_DB,  _C_DB  = INTENT_DASHBOARD_EXPLANATION,  CATEGORY_DASHBOARD
_ED,  _C_ED  = INTENT_EVIDENCE_DIGEST,        CATEGORY_EVIDENCE_DIGEST
_ST,  _C_ST  = INTENT_SAFETY_TRUST,           CATEGORY_SAFETY_TRUST
_WN,  _C_WN  = INTENT_WHAT_SHOULD_I_DO,       CATEGORY_WHAT_NEXT
_OB,  _C_OB  = INTENT_ONBOARDING_HELP,        CATEGORY_ONBOARDING
_FC,  _C_FC  = INTENT_FALLBACK_CLARIFY,       CATEGORY_FALLBACK_FRAGMENT


# ──────────────────────────────────────────────────────────────────
# Catalogue — >= 300 entries
# ──────────────────────────────────────────────────────────────────
# 22 intents × ~14 entries = 308.
# Entries are hand-written and span typos, shorthand, unfinished
# context, casual phrasing, beginner phrasing, and impatient-owner
# phrasing. Each entry is plain text — no PII, no real names, no
# real addresses, no production brokerage IDs.

BROKER_QUESTION_CATALOGUE: Tuple[Dict[str, str], ...] = (
    # ── leads_today_count (14) ───────────────────────────────────
    _q("how many leads today",                            _LT,  _C_LT),
    _q("leads today?",                                    _LT,  _C_LT),
    _q("any new leads today",                             _LT,  _C_LT),
    _q("did we get any leads today",                      _LT,  _C_LT),
    _q("new leads",                                       _LT,  _C_LT),
    _q("how many lead today",                             _LT,  _C_LT),
    _q("leeds today",                                     _LT,  _C_LT),
    _q("show me todays leads",                            _LT,  _C_LT),
    _q("todays lead count",                               _LT,  _C_LT),
    _q("how many new leads came in today",                _LT,  _C_LT),
    _q("how many new leads did we get",                   _LT,  _C_LT),
    _q("lead count today pls",                            _LT,  _C_LT),
    _q("count of leads today",                            _LT,  _C_LT),
    _q("did any leads come in today",                     _LT,  _C_LT),

    # ── hot_leads_summary (14) ───────────────────────────────────
    _q("show me hot leads",                               _HL,  _C_HL),
    _q("hot leads",                                       _HL,  _C_HL),
    _q("hot leads pls",                                   _HL,  _C_HL),
    _q("any hot leads right now",                         _HL,  _C_HL),
    _q("whats hot today",                                 _HL,  _C_HL),
    _q("which leads are hot",                             _HL,  _C_HL),
    _q("hottest leads",                                   _HL,  _C_HL),
    _q("hot leeds",                                       _HL,  _C_HL),
    _q("show the hot ones",                               _HL,  _C_HL),
    _q("most engaged leads",                              _HL,  _C_HL),
    _q("ready to buy leads",                              _HL,  _C_HL),
    _q("warm leads",                                      _HL,  _C_HL),
    _q("hot lead summary",                                _HL,  _C_HL),
    _q("which leads should i call first",                 _HL,  _C_HL),

    # ── missed_leads (14) ────────────────────────────────────────
    _q("any leads we missed",                             _ML,  _C_ML),
    _q("missed leads",                                    _ML,  _C_ML),
    _q("did we miss any leads",                           _ML,  _C_ML),
    _q("leads we didnt respond to",                       _ML,  _C_ML),
    _q("any leads with no response",                      _ML,  _C_ML),
    _q("which leads were missed",                         _ML,  _C_ML),
    _q("missed lead list",                                _ML,  _C_ML),
    _q("leads we dropped",                                _ML,  _C_ML),
    _q("leads with no contact",                           _ML,  _C_ML),
    _q("leads we never called",                           _ML,  _C_ML),
    _q("did anyone slip through",                         _ML,  _C_ML),
    _q("did we drop any leads today",                     _ML,  _C_ML),
    _q("missed lead report",                              _ML,  _C_ML),
    _q("no response leads",                               _ML,  _C_ML),

    # ── stale_leads (14) ─────────────────────────────────────────
    _q("show stale leads",                                _SL,  _C_SL),
    _q("stale leads",                                     _SL,  _C_SL),
    _q("any old leads to follow up",                      _SL,  _C_SL),
    _q("which leads have gone cold",                      _SL,  _C_SL),
    _q("cold leads",                                      _SL,  _C_SL),
    _q("old leads",                                       _SL,  _C_SL),
    _q("leads that need a nudge",                         _SL,  _C_SL),
    _q("stale lead recovery",                             _SL,  _C_SL),
    _q("leads we havent touched in a while",              _SL,  _C_SL),
    _q("which leads are aging",                           _SL,  _C_SL),
    _q("forgotten leads",                                 _SL,  _C_SL),
    _q("leads gathering dust",                            _SL,  _C_SL),
    _q("revive cold leads",                               _SL,  _C_SL),
    _q("aging lead list",                                 _SL,  _C_SL),

    # ── callback_requests (14) ───────────────────────────────────
    _q("any callbacks owed",                              _CB,  _C_CB),
    _q("callbacks",                                       _CB,  _C_CB),
    _q("callback requests",                               _CB,  _C_CB),
    _q("who needs a callback",                            _CB,  _C_CB),
    _q("any pending callbacks",                           _CB,  _C_CB),
    _q("callbacks for today",                             _CB,  _C_CB),
    _q("call backs today",                                _CB,  _C_CB),
    _q("who do we owe a callback to",                     _CB,  _C_CB),
    _q("scheduled callbacks",                             _CB,  _C_CB),
    _q("clb owed",                                        _CB,  _C_CB),
    _q("clbs pls",                                        _CB,  _C_CB),
    _q("overdue callbacks",                               _CB,  _C_CB),
    _q("any callbacks waiting",                           _CB,  _C_CB),
    _q("callback list",                                   _CB,  _C_CB),

    # ── appointments_today (14) ──────────────────────────────────
    _q("any bookings today",                              _AP,  _C_AP),
    _q("appointments today",                              _AP,  _C_AP),
    _q("did we book anyone today",                        _AP,  _C_AP),
    _q("showings today",                                  _AP,  _C_AP),
    _q("bookings",                                        _AP,  _C_AP),
    _q("how many appts today",                            _AP,  _C_AP),
    _q("showings booked",                                 _AP,  _C_AP),
    _q("appointment count",                               _AP,  _C_AP),
    _q("did pas book any showings",                       _AP,  _C_AP),
    _q("bkg today",                                       _AP,  _C_AP),
    _q("appts pls",                                       _AP,  _C_AP),
    _q("any showings scheduled",                          _AP,  _C_AP),
    _q("did anyone book a showing today",                 _AP,  _C_AP),
    _q("booked clients today",                            _AP,  _C_AP),

    # ── agent_routing_status (14) ────────────────────────────────
    _q("which agent is handling leads",                   _AR,  _C_AR),
    _q("agent routing",                                   _AR,  _C_AR),
    _q("who is on call rotation",                         _AR,  _C_AR),
    _q("which agents are getting leads",                  _AR,  _C_AR),
    _q("agent assignment",                                _AR,  _C_AR),
    _q("who is assigned",                                 _AR,  _C_AR),
    _q("show agent routing",                              _AR,  _C_AR),
    _q("agent coverage",                                  _AR,  _C_AR),
    _q("who takes the next lead",                         _AR,  _C_AR),
    _q("agnt rotation",                                   _AR,  _C_AR),
    _q("agnt routing",                                    _AR,  _C_AR),
    _q("are leads being routed",                          _AR,  _C_AR),
    _q("which agent gets the next call",                  _AR,  _C_AR),
    _q("agent assignment status",                         _AR,  _C_AR),

    # ── response_speed (14) ──────────────────────────────────────
    _q("how fast are we responding",                      _RS,  _C_RS),
    _q("response time",                                   _RS,  _C_RS),
    _q("avg response speed",                              _RS,  _C_RS),
    _q("how quick are we replying",                       _RS,  _C_RS),
    _q("response speed",                                  _RS,  _C_RS),
    _q("time to first contact",                           _RS,  _C_RS),
    _q("how long to respond",                             _RS,  _C_RS),
    _q("are we responding fast enough",                   _RS,  _C_RS),
    _q("speed of reply",                                  _RS,  _C_RS),
    _q("respnse time",                                    _RS,  _C_RS),
    _q("first response time",                             _RS,  _C_RS),
    _q("average reply speed",                             _RS,  _C_RS),
    _q("response latency",                                _RS,  _C_RS),
    _q("speed to lead",                                   _RS,  _C_RS),

    # ── lead_source_quality (14) ─────────────────────────────────
    _q("which source converts best",                      _SQ,  _C_SQ),
    _q("best lead source",                                _SQ,  _C_SQ),
    _q("lead source quality",                             _SQ,  _C_SQ),
    _q("which source is worst",                           _SQ,  _C_SQ),
    _q("source conversion rates",                         _SQ,  _C_SQ),
    _q("where are leads coming from",                     _SQ,  _C_SQ),
    _q("best converting source",                          _SQ,  _C_SQ),
    _q("which lead source gives us bookings",             _SQ,  _C_SQ),
    _q("source breakdown",                                _SQ,  _C_SQ),
    _q("lead src qlty",                                   _SQ,  _C_SQ),
    _q("source quality",                                  _SQ,  _C_SQ),
    _q("conversion by source",                            _SQ,  _C_SQ),
    _q("which channel is converting",                     _SQ,  _C_SQ),
    _q("best lead channel",                               _SQ,  _C_SQ),

    # ── crm_sync_status (14) ─────────────────────────────────────
    _q("is the crm synced",                               _CRM, _C_CRM),
    _q("crm sync",                                        _CRM, _C_CRM),
    _q("are leads syncing to crm",                        _CRM, _C_CRM),
    _q("crm sync status",                                 _CRM, _C_CRM),
    _q("is the crm up to date",                           _CRM, _C_CRM),
    _q("did the crm sync today",                          _CRM, _C_CRM),
    _q("any crm sync errors",                             _CRM, _C_CRM),
    _q("crm health",                                      _CRM, _C_CRM),
    _q("is followup boss synced",                         _CRM, _C_CRM),
    _q("crm conn",                                        _CRM, _C_CRM),
    _q("crm connection",                                  _CRM, _C_CRM),
    _q("crm not syncing",                                 _CRM, _C_CRM),
    _q("did the sync run",                                _CRM, _C_CRM),
    _q("when was the last crm sync",                      _CRM, _C_CRM),

    # ── zillow_lead_handling (14) ────────────────────────────────
    _q("how do zillow leads get handled",                 _ZL,  _C_ZL),
    _q("zillow lead just came in",                        _ZL,  _C_ZL),
    _q("what does pas do with zillow leads",              _ZL,  _C_ZL),
    _q("zillow integration",                              _ZL,  _C_ZL),
    _q("zillow leads",                                    _ZL,  _C_ZL),
    _q("are zillow leads being answered",                 _ZL,  _C_ZL),
    _q("zilow leads",                                     _ZL,  _C_ZL),
    _q("zillow lead pipeline",                            _ZL,  _C_ZL),
    _q("how fast does pas reply to zillow",               _ZL,  _C_ZL),
    _q("zillow flex leads",                               _ZL,  _C_ZL),
    _q("zillow leads handling",                           _ZL,  _C_ZL),
    _q("how does pas treat zillow leads",                 _ZL,  _C_ZL),
    _q("did pas respond to that zillow lead",             _ZL,  _C_ZL),
    _q("zillow response time",                            _ZL,  _C_ZL),

    # ── realtor_lead_handling (14) ───────────────────────────────
    _q("how do realtor com leads get handled",            _RL,  _C_RL),
    _q("realtor com integration",                         _RL,  _C_RL),
    _q("realtor leads",                                   _RL,  _C_RL),
    _q("realtor.com leads",                               _RL,  _C_RL),
    _q("realtor com",                                     _RL,  _C_RL),
    _q("are realtor leads being answered",                _RL,  _C_RL),
    _q("realtor lead pipeline",                           _RL,  _C_RL),
    _q("realtor com response time",                       _RL,  _C_RL),
    _q("how fast does pas reply to realtor com",          _RL,  _C_RL),
    _q("realtor com lead handling",                       _RL,  _C_RL),
    _q("did pas respond to that realtor lead",            _RL,  _C_RL),
    _q("realtor.com response",                            _RL,  _C_RL),
    _q("rltr com leads",                                  _RL,  _C_RL),
    _q("realtor com lead routing",                        _RL,  _C_RL),

    # ── facebook_lead_handling (14) ──────────────────────────────
    _q("how are facebook leads handled",                  _FB,  _C_FB),
    _q("facebook lead just came in",                      _FB,  _C_FB),
    _q("fb leads",                                        _FB,  _C_FB),
    _q("facebook ads leads",                              _FB,  _C_FB),
    _q("facebook integration",                            _FB,  _C_FB),
    _q("are facebook leads being answered",               _FB,  _C_FB),
    _q("fb ad leads",                                     _FB,  _C_FB),
    _q("facebook lead pipeline",                          _FB,  _C_FB),
    _q("how fast does pas reply to facebook leads",       _FB,  _C_FB),
    _q("facebook lead handling",                          _FB,  _C_FB),
    _q("did pas respond to that facebook lead",           _FB,  _C_FB),
    _q("fb leads response time",                          _FB,  _C_FB),
    _q("facebook lead routing",                           _FB,  _C_FB),
    _q("meta ads leads",                                  _FB,  _C_FB),

    # ── isa_comparison (14) ──────────────────────────────────────
    _q("how does pas compare to an isa",                  _IS,  _C_IS),
    _q("pas vs isa",                                      _IS,  _C_IS),
    _q("is pas better than my isa",                       _IS,  _C_IS),
    _q("isa replacement",                                 _IS,  _C_IS),
    _q("isa comparison",                                  _IS,  _C_IS),
    _q("compared to a human isa",                         _IS,  _C_IS),
    _q("can pas replace my isa",                          _IS,  _C_IS),
    _q("isa vs ai",                                       _IS,  _C_IS),
    _q("pas vs human isa",                                _IS,  _C_IS),
    _q("does pas do what an isa does",                    _IS,  _C_IS),
    _q("isa benchmarks",                                  _IS,  _C_IS),
    _q("isa numbers vs pas",                              _IS,  _C_IS),
    _q("performance vs an isa",                           _IS,  _C_IS),
    _q("pas vs internal sales agent",                     _IS,  _C_IS),

    # ── after_hours_coverage (14) ────────────────────────────────
    _q("does pas work after hours",                       _AH,  _C_AH),
    _q("after hours coverage",                            _AH,  _C_AH),
    _q("nights and weekends",                             _AH,  _C_AH),
    _q("late night leads",                                _AH,  _C_AH),
    _q("weekend coverage",                                _AH,  _C_AH),
    _q("does pas respond at 2am",                         _AH,  _C_AH),
    _q("after hrs",                                       _AH,  _C_AH),
    _q("overnight coverage",                              _AH,  _C_AH),
    _q("do we get covered on weekends",                   _AH,  _C_AH),
    _q("after hours response",                            _AH,  _C_AH),
    _q("does pas answer after 6pm",                       _AH,  _C_AH),
    _q("after hours leads",                               _AH,  _C_AH),
    _q("late night coverage",                             _AH,  _C_AH),
    _q("weekend leads",                                   _AH,  _C_AH),

    # ── training_pas (14) ────────────────────────────────────────
    _q("how do i train pas",                              _TR,  _C_TR),
    _q("can i teach pas new responses",                   _TR,  _C_TR),
    _q("training pas",                                    _TR,  _C_TR),
    _q("how do i improve pas replies",                    _TR,  _C_TR),
    _q("teach pas",                                       _TR,  _C_TR),
    _q("retrain pas",                                     _TR,  _C_TR),
    _q("can i adjust pas tone",                           _TR,  _C_TR),
    _q("how do i fine tune pas",                          _TR,  _C_TR),
    _q("update pas script",                               _TR,  _C_TR),
    _q("how to teach pas a new pitch",                    _TR,  _C_TR),
    _q("training options",                                _TR,  _C_TR),
    _q("can pas learn from my calls",                     _TR,  _C_TR),
    _q("can i give pas a new script",                     _TR,  _C_TR),
    _q("how do i tweak pas",                              _TR,  _C_TR),

    # ── integration_questions (14) ───────────────────────────────
    _q("how do i connect followup boss",                  _IN,  _C_IN),
    _q("connect crm",                                     _IN,  _C_IN),
    _q("integrations",                                    _IN,  _C_IN),
    _q("how do i hook up zillow",                         _IN,  _C_IN),
    _q("integrate facebook ads",                          _IN,  _C_IN),
    _q("set up integration",                              _IN,  _C_IN),
    _q("how to connect realtor com",                      _IN,  _C_IN),
    _q("which crms does pas support",                     _IN,  _C_IN),
    _q("set up calendar integration",                     _IN,  _C_IN),
    _q("can i connect google calendar",                   _IN,  _C_IN),
    _q("integration list",                                _IN,  _C_IN),
    _q("supported integrations",                          _IN,  _C_IN),
    _q("connect lofty",                                   _IN,  _C_IN),
    _q("integration help",                                _IN,  _C_IN),

    # ── dashboard_explanation (14) ───────────────────────────────
    _q("what does the dashboard mean",                    _DB,  _C_DB),
    _q("explain the dashboard",                           _DB,  _C_DB),
    _q("how do i read the dashboard",                     _DB,  _C_DB),
    _q("what does response rate mean",                    _DB,  _C_DB),
    _q("dashboard explanation",                           _DB,  _C_DB),
    _q("what is conversion rate",                         _DB,  _C_DB),
    _q("walk me through the dashboard",                   _DB,  _C_DB),
    _q("explain the numbers",                             _DB,  _C_DB),
    _q("what does the green light mean",                  _DB,  _C_DB),
    _q("dashbord help",                                   _DB,  _C_DB),
    _q("dash help",                                       _DB,  _C_DB),
    _q("what am i looking at on the dashboard",           _DB,  _C_DB),
    _q("dashboard tour",                                  _DB,  _C_DB),
    _q("can you explain these metrics",                   _DB,  _C_DB),

    # ── evidence_digest_summary (14) ─────────────────────────────
    _q("show me the simulation digest",                   _ED,  _C_ED),
    _q("evidence digest",                                 _ED,  _C_ED),
    _q("simulation digest",                               _ED,  _C_ED),
    _q("what did the simulation prove",                   _ED,  _C_ED),
    _q("rehearsal evidence",                              _ED,  _C_ED),
    _q("strategy evidence",                               _ED,  _C_ED),
    _q("show the latest rehearsal results",               _ED,  _C_ED),
    _q("what does the latest test show",                  _ED,  _C_ED),
    _q("digest summary",                                  _ED,  _C_ED),
    _q("rehearsal report",                                _ED,  _C_ED),
    _q("simulation summary",                              _ED,  _C_ED),
    _q("simulation results pls",                          _ED,  _C_ED),
    _q("test results",                                    _ED,  _C_ED),
    _q("pas201 digest",                                   _ED,  _C_ED),

    # ── safety_trust (14) ────────────────────────────────────────
    _q("is pas safe to use",                              _ST,  _C_ST),
    _q("can i trust pas",                                 _ST,  _C_ST),
    _q("is this thing safe",                              _ST,  _C_ST),
    _q("safety check",                                    _ST,  _C_ST),
    _q("how safe is pas",                                 _ST,  _C_ST),
    _q("trust report",                                    _ST,  _C_ST),
    _q("is pas going to embarrass me",                    _ST,  _C_ST),
    _q("will pas say something bad",                      _ST,  _C_ST),
    _q("is pas approved for live calls",                  _ST,  _C_ST),
    _q("safety status",                                   _ST,  _C_ST),
    _q("are we ok to let pas talk to leads",              _ST,  _C_ST),
    _q("how risky is this",                               _ST,  _C_ST),
    _q("safety summary",                                  _ST,  _C_ST),
    _q("trust level",                                     _ST,  _C_ST),

    # ── what_should_i_do (14) ────────────────────────────────────
    _q("what should i do now",                            _WN,  _C_WN),
    _q("what should i focus on",                          _WN,  _C_WN),
    _q("what should i do next",                           _WN,  _C_WN),
    _q("whats important today",                           _WN,  _C_WN),
    _q("next action",                                     _WN,  _C_WN),
    _q("priorities",                                      _WN,  _C_WN),
    _q("what do i do",                                    _WN,  _C_WN),
    _q("just tell me whats important",                    _WN,  _C_WN),
    _q("whats the priority",                              _WN,  _C_WN),
    _q("what needs my attention",                         _WN,  _C_WN),
    _q("where should i look first",                       _WN,  _C_WN),
    _q("what should i tackle first",                      _WN,  _C_WN),
    _q("what matters right now",                          _WN,  _C_WN),
    _q("whats next",                                      _WN,  _C_WN),

    # ── onboarding_help (14) ─────────────────────────────────────
    # Broker-style "how do I use this thing" questions. These are
    # the first thing a new operator asks. They must never fall
    # through to the bare-fallback clarifier — instead they get
    # the friendly "start here" response.
    _q("how do i use this thing",                         _OB,  _C_OB),
    _q("how do i even use this thing",                    _OB,  _C_OB),
    _q("how do i use pas",                                _OB,  _C_OB),
    _q("what can pas do",                                 _OB,  _C_OB),
    _q("what can you do",                                 _OB,  _C_OB),
    _q("help me use pas",                                 _OB,  _C_OB),
    _q("where do i start",                                _OB,  _C_OB),
    _q("how should i start",                              _OB,  _C_OB),
    _q("how do i even fuckin use this thing",             _OB,  _C_OB),
    _q("i don't know what to ask",                        _OB,  _C_OB),
    _q("what should i ask you",                           _OB,  _C_OB),
    _q("how does this thing work",                        _OB,  _C_OB),
    _q("getting started",                                 _OB,  _C_OB),
    _q("how do i begin",                                  _OB,  _C_OB),

    # ── fallback_fragment (14) ───────────────────────────────────
    # These should map to the safe fallback intent. Fragmented,
    # truncated, single-token, or otherwise unclassifiable text.
    _q("uhhh",                                            _FC,  _C_FC),
    _q("hmm",                                             _FC,  _C_FC),
    _q("hello?",                                          _FC,  _C_FC),
    _q("hi",                                              _FC,  _C_FC),
    _q("?",                                               _FC,  _C_FC),
    _q("test",                                            _FC,  _C_FC),
    _q("idk",                                             _FC,  _C_FC),
    _q("?? what",                                         _FC,  _C_FC),
    _q("anything",                                        _FC,  _C_FC),
    _q("whats up",                                        _FC,  _C_FC),
    _q("yo",                                              _FC,  _C_FC),
    _q("pas",                                             _FC,  _C_FC),
    _q("hey",                                             _FC,  _C_FC),
    _q("...",                                             _FC,  _C_FC),
)


# ──────────────────────────────────────────────────────────────────
# Public helpers
# ──────────────────────────────────────────────────────────────────

def question_count() -> int:
    return len(BROKER_QUESTION_CATALOGUE)


def list_intents() -> Tuple[str, ...]:
    return INTENT_CODES


def list_categories() -> Tuple[str, ...]:
    return CATEGORIES


def questions_for_intent(intent_code: str) -> Tuple[Dict[str, str], ...]:
    return tuple(
        q for q in BROKER_QUESTION_CATALOGUE if q["intent"] == intent_code
    )


def questions_for_category(category_code: str) -> Tuple[Dict[str, str], ...]:
    return tuple(
        q for q in BROKER_QUESTION_CATALOGUE if q["category"] == category_code
    )
