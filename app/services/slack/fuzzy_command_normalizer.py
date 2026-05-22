"""
PAS204-C — Deterministic fuzzy command normalizer.

Pre-classifier typo / shorthand normalization for the Slack
dispatcher. Pure function. No LLM, no network, no mutation, no
edit-distance "guessing" — only a bounded closed alias table.

The dispatcher applies `normalize_fuzzy_command(text)` to raw
operator input BEFORE PAS203 / PAS191 / PAS204 see it. The
normalizer:

  * lower-cases tokens during lookup but preserves case of any
    token not in the alias table;
  * only replaces tokens that exactly match a known typo alias
    (no fuzzy / probabilistic expansion);
  * never rewrites a token that is itself already a canonical
    keyword (e.g., "lead" stays "lead", not "leads");
  * never rewrites a mutation token (pause / resume / push /
    remove) — these are explicitly excluded so the existing
    PAS191 exact-command branch keeps owning them;
  * never removes or adds tokens — it is a 1-to-1 token map.

The alias table is intentionally small and hand-curated. Adding
a new alias is a deliberate code change with a test.
"""

from __future__ import annotations

from typing import Dict, Tuple


# Mutation tokens we must never accidentally rewrite. Includes
# common typo variants of those tokens defensively — they all
# stay as-is so the PAS191 exact-command branch keeps catching
# them (or rejecting them).
_PROTECTED_TOKENS: frozenset = frozenset((
    "pause", "resume", "push", "remove",
    "pasue", "resme", "psh", "rmv", "pase",
))


# Bounded typo / shorthand alias table. Every key MUST be a
# token that is unambiguously a typo of the value. Keys are
# checked lower-case; values are emitted lower-case (the rest
# of the dispatcher path normalises case already).
_TYPO_ALIASES: Dict[str, str] = {
    # ── leads ────────────────────────────────────────────────
    "leeds":     "leads",
    "leed":      "leads",
    "lds":       "leads",
    "leds":      "leads",
    "ledas":     "leads",

    # ── today ────────────────────────────────────────────────
    "tody":      "today",
    "tday":      "today",
    "todday":    "today",
    "todai":     "today",
    "toay":      "today",
    "toda":      "today",

    # ── hot ──────────────────────────────────────────────────
    "hott":      "hot",
    "hotte":     "hot",
    "hotz":      "hot",

    # ── callback ─────────────────────────────────────────────
    "callbak":   "callback",
    "cllbck":    "callback",
    "calback":   "callback",
    "calbak":    "callback",
    "callbck":   "callback",
    "callbcks":  "callbacks",
    "callbaks":  "callbacks",
    "cllbcks":   "callbacks",

    # ── appointments ─────────────────────────────────────────
    "appt":      "appointment",
    "appts":     "appointments",
    "apt":       "appointment",
    "apts":      "appointments",
    "appont":    "appointment",
    "apnt":      "appointment",
    "apntmnt":   "appointment",

    # ── safe / safety ────────────────────────────────────────
    "saafe":     "safe",
    "saef":      "safe",
    "safte":     "safety",
    "safty":     "safety",

    # ── use ──────────────────────────────────────────────────
    "uze":       "use",
    "uss":       "use",
    "ues":       "use",

    # ── thing ────────────────────────────────────────────────
    "thng":      "thing",
    "thingg":    "thing",
    "thin":      "thing",

    # ── zillow ───────────────────────────────────────────────
    "zillw":     "zillow",
    "zilo":      "zillow",
    "zilow":     "zillow",
    "zillo":     "zillow",
    "zilw":      "zillow",

    # ── stats / stat ─────────────────────────────────────────
    "stat":      "stats",
    "stts":      "stats",
    "satats":    "stats",

    # ── response / rate ──────────────────────────────────────
    "respnse":   "response",
    "responce":  "response",
    "respnce":   "response",
    "rspns":     "response",
    "rsp":       "response",
    "rat":       "rate",
    "rte":       "rate",
    "ratte":     "rate",

    # ── digest ───────────────────────────────────────────────
    "digst":     "digest",
    "diget":     "digest",
    "dgst":      "digest",
    "digets":    "digest",

    # ── showing / show ───────────────────────────────────────
    "shwing":    "showing",
    "shwings":   "showings",
    "shw":       "show",

    # ── booking ──────────────────────────────────────────────
    "bkg":       "booking",
    "bkgs":      "bookings",
    "bking":     "booking",
    "bkings":    "bookings",

    # ── source ───────────────────────────────────────────────
    "src":       "source",
    "srce":      "source",
    "sorce":     "source",
}


# Leet substitutions — bounded, applied ONLY when the token
# already contains a leet character AND the de-leeted form maps
# to either a known typo alias OR a longer (>=4 char) plain
# letter token. Prevents accidental rewriting of legitimate
# tokens like "iso9001" → "isoOOOI".
_LEET_SUBSTITUTIONS: Dict[str, str] = {
    "0": "o",
    "3": "e",
    "1": "i",
    "$": "s",
    "@": "a",
}


def _de_leet(token: str) -> str:
    """Return the token with closed-set leet characters mapped
    back to letters. Pure, deterministic."""
    if not any(c in _LEET_SUBSTITUTIONS for c in token):
        return token
    return "".join(_LEET_SUBSTITUTIONS.get(c, c) for c in token)


def normalize_fuzzy_command(text: str) -> str:
    """
    Apply deterministic typo / shorthand normalization to a raw
    operator-typed command string.

    Returns a new string (same input -> same output forever).

    Rules:
      * Token boundary = whitespace.
      * Lower-case only the token used for lookup; if the
        original token has different case the canonical form
        replaces it.
      * Skip mutation tokens (pause / resume / push / remove)
        and their typo variants — they MUST flow unchanged to
        the PAS191 exact-command branch.
      * Skip tokens that are not in the alias table — no fuzzy
        expansion.
    """
    if not isinstance(text, str):
        return ""
    s = text.strip()
    if not s:
        return ""
    parts = s.split()
    out_parts = []
    # PAS204-C — leet substitution chars are NOT treated as
    # punctuation during the lead/tail strip, otherwise tokens
    # like "l3@d$" lose the trailing "$" before de-leet runs.
    _LEET_CHARS = set(_LEET_SUBSTITUTIONS.keys())
    for raw in parts:
        # Preserve internal punctuation in the token shape but
        # strip leading/trailing for the alias lookup.
        lead = ""
        tail = ""
        core = raw
        # peel leading non-alnum (but keep leet chars in core)
        i = 0
        while i < len(core) and not core[i].isalnum() and core[i] not in _LEET_CHARS:
            lead += core[i]
            i += 1
        core = core[i:]
        # peel trailing non-alnum (but keep leet chars in core)
        j = len(core)
        while j > 0 and not core[j - 1].isalnum() and core[j - 1] not in _LEET_CHARS:
            tail = core[j - 1] + tail
            j -= 1
        core = core[:j]

        if not core:
            out_parts.append(raw)
            continue

        lowered = core.lower()
        if lowered in _PROTECTED_TOKENS:
            out_parts.append(raw)
            continue

        # PAS204-C — opportunistic leet de-substitution. If the
        # token contains a closed-set leet character AND the
        # de-leeted form is a known typo alias OR a plausible
        # plain-letter word, prefer the de-leeted form.
        deleted = _de_leet(lowered)
        if deleted != lowered and deleted in _PROTECTED_TOKENS:
            out_parts.append(raw)
            continue
        if deleted != lowered and (
            deleted in _TYPO_ALIASES
            or (len(deleted) >= 4 and deleted.isalpha())
        ):
            lowered = deleted

        replacement = _TYPO_ALIASES.get(lowered)
        if replacement is None:
            if lowered != core.lower():
                # de-leet applied but no further alias — emit
                # the de-leeted form (lower-case) preserving
                # surrounding punctuation.
                out_parts.append(f"{lead}{lowered}{tail}")
                continue
            out_parts.append(raw)
            continue

        # Preserve original surrounding punctuation but emit the
        # replacement in lower-case (matches the canonical
        # casing the catalogue / classifier already use).
        out_parts.append(f"{lead}{replacement}{tail}")
    return " ".join(out_parts)


def alias_count() -> int:
    """Number of typo aliases registered (used by readiness gate)."""
    return len(_TYPO_ALIASES)


def list_aliases() -> Tuple[str, ...]:
    """Return the closed alias-key tuple (for readiness / docs)."""
    return tuple(sorted(_TYPO_ALIASES.keys()))


def is_protected_token(token: str) -> bool:
    """True iff `token` is a mutation-protected token that the
    normalizer must NOT rewrite."""
    return isinstance(token, str) and token.lower() in _PROTECTED_TOKENS
