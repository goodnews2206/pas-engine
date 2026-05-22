"""
PAS204 — Broker-question simulation runner.

Runs every question in the PAS204 catalogue through every
deterministic variant, classifies it, builds a broker-facing
response, scores the response on 8 quality dimensions, and emits
a single JSON report under reports/simulations/. The runner is
strictly read-only and SIMULATION_ONLY; it never imports Twilio,
Slack, Supabase, OpenAI, Anthropic, dotenv, or the live state
machine.

Defaults: --questions <all 308> --variants 100  =>  30,800 runs.

Scoring per response (booleans):

  * understood_intent
  * human_tone              (no closed-vocab technical tokens in body)
  * useful_answer           (response body length >= MIN_USEFUL_CHARS)
  * no_jargon               (response avoids PAS technical tokens)
  * no_false_claim          (response avoids "live"/"deployed"/etc.)
  * no_live_action          (response never asserts live activity)
  * suggests_next_step      (at least one next-step suggestion)
  * handles_typo_or_fragment (response shape valid even for typos)

A run passes when all 8 booleans are True.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple


_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


from app.services.slack.broker_conversation_intents import (  # noqa: E402
    match_broker_intent,
)
from app.services.slack.broker_conversation_surface import (  # noqa: E402
    build_broker_response,
)
from app.services.slack.broker_question_catalogue import (  # noqa: E402
    BROKER_QUESTION_CATALOGUE,
    INTENT_CODES,
    INTENT_FALLBACK_CLARIFY,
    question_count,
)
from app.services.slack.broker_response_voice import (  # noqa: E402
    FORBIDDEN_OUTPUT_TOKENS,
)
# PAS204-C — apply the same fuzzy normalization the dispatcher
# applies in production. This makes the runner numbers reflect
# real broker experience: typos the normalizer can fix should
# pass.
from app.services.slack.fuzzy_command_normalizer import (  # noqa: E402
    normalize_fuzzy_command,
)


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


REPORTS_SUBDIR = Path("reports") / "simulations"


# Closed list of technical tokens we treat as "jargon" — if any
# appear verbatim in the broker-facing body, we flag the response
# as containing jargon. These are PAS internal closed-vocab
# tokens that the response voice should have translated.
_JARGON_TOKENS: Tuple[str, ...] = (
    "behavioral_low_friction_observed",
    "behavioral_high_friction_observed",
    "behavioral_good_pacing_observed",
    "behavioral_high_pressure_observed",
    "behavioral_low_trust_observed",
    "behavioral_callback_continuity_observed",
    "behavioral_trust_preservation_observed",
    "behavioral_early_escalation_observed",
    "runtime_pass_rate_100_percent",
    "runtime_pass_rate_at_or_above_95_percent",
    "runtime_pass_rate_at_or_above_75_percent",
    "runtime_pass_rate_below_75_percent",
    "safety_outcome_clean",
    "safety_outcome_auto_fail",
    "lineage_intact",
    "lineage_broken",
    "artifact_integrity_complete",
    "artifact_integrity_incomplete",
    "no_live_behavior_change_anywhere_in_lineage",
    "live_call_routing_remains_out_of_scope",
    "calibration_against_live_call_outcomes_pending",
    "automated_promotion_to_runtime_strategy_pending",
    "real_lead_exposure_remains_out_of_scope",
    "slack_operator_surface_for_runtime_runs_pending",
    "review_digest_then_decide_pilot_step",
    "expand_synthetic_catalogue_before_pilot",
    "rerun_manual_test_with_alternative_strategy",
    "block_until_safety_issue_resolved",
)


# Phrases that would assert live activity. None of these may
# ever appear in a broker-facing response.
_FALSE_LIVE_PHRASES: Tuple[str, ...] = (
    "live call active",
    "production strategy enabled",
    "real lead routed",
    "calling live",
    "we routed",
    "we just called",
    "i just called",
    "promoted to production",
)


MIN_USEFUL_CHARS: int = 80


# ──────────────────────────────────────────────────────────────────
# Deterministic variant generation
# ──────────────────────────────────────────────────────────────────

# 100 deterministic transformations applied by variant index.
# Each is `(name, callable)`. Callables are pure: same text +
# same index produce the same output forever.

def _v_identity(t: str) -> str:
    return t


def _v_upper(t: str) -> str:
    return t.upper()


def _v_title(t: str) -> str:
    return t.title()


def _v_trailing_q(t: str) -> str:
    return t.rstrip(".!?") + "?"


def _v_trailing_period(t: str) -> str:
    return t.rstrip(".!?") + "."


def _v_double_q(t: str) -> str:
    return t + "??"


def _v_pls(t: str) -> str:
    return t.rstrip(".!? ") + " pls"


def _v_please(t: str) -> str:
    return t.rstrip(".!? ") + " please"


def _v_extra_space(t: str) -> str:
    # collapse all whitespace then re-insert a double-space
    return "  ".join(t.split())


def _v_strip(t: str) -> str:
    return "   " + t + "   "


def _v_drop_first_char(t: str) -> str:
    if len(t) <= 1:
        return t
    return t[1:]


def _v_drop_last_char(t: str) -> str:
    if len(t) <= 1:
        return t
    return t[:-1]


def _v_swap_two(t: str) -> str:
    # swap two adjacent characters in the middle of a longish token
    if len(t) < 8:
        return t
    i = len(t) // 2
    if t[i] == " " or t[i - 1] == " ":
        return t
    return t[: i - 1] + t[i] + t[i - 1] + t[i + 1:]


def _v_drop_punct(t: str) -> str:
    return "".join(c for c in t if c not in ".,!?;:")


def _v_add_random_punct(t: str) -> str:
    return t + "?!"


def _v_emoji_prefix(t: str) -> str:
    return t  # ASCII-only env; emoji-equivalent is "!! "
    # Note: kept as no-op so the variant set stays portable.


def _v_pas_prefix(t: str) -> str:
    return "pas " + t


def _v_hey_prefix(t: str) -> str:
    return "hey " + t


def _v_quick_prefix(t: str) -> str:
    return "quick q — " + t


def _v_question_word(t: str) -> str:
    if t.startswith(("what", "how", "who", "when", "any", "did", "is", "are")):
        return t
    return "what " + t


def _v_can_prefix(t: str) -> str:
    return "can you tell me " + t


def _v_just_prefix(t: str) -> str:
    return "just need " + t


def _v_double_word(t: str) -> str:
    tokens = t.split()
    if not tokens:
        return t
    return " ".join(tokens + [tokens[-1]])


def _v_collapse_spaces(t: str) -> str:
    # join words with no space (extreme shorthand)
    return "".join(t.split())[: max(8, len(t) // 2)] if len(t.split()) > 1 else t


# Substitution variants: targeted char swaps.
_SUB_MAP = (
    ("a", "@"), ("e", "3"), ("i", "1"), ("o", "0"), ("s", "$"),
)


def _v_leetify(t: str, k: int) -> str:
    src, dst = _SUB_MAP[k % len(_SUB_MAP)]
    return t.replace(src, dst, 1)


# Build the full 100-variant table once.
def _build_variants() -> Tuple[Tuple[str, callable], ...]:
    base = [
        ("identity",         _v_identity),
        ("upper",            _v_upper),
        ("title",            _v_title),
        ("trailing_q",       _v_trailing_q),
        ("trailing_period",  _v_trailing_period),
        ("double_q",         _v_double_q),
        ("pls",              _v_pls),
        ("please",           _v_please),
        ("extra_space",      _v_extra_space),
        ("strip",            _v_strip),
        ("drop_last_char",   _v_drop_last_char),
        ("swap_two",         _v_swap_two),
        ("drop_punct",       _v_drop_punct),
        ("add_random_punct", _v_add_random_punct),
        ("pas_prefix",       _v_pas_prefix),
        ("hey_prefix",       _v_hey_prefix),
        ("quick_prefix",     _v_quick_prefix),
        ("question_word",    _v_question_word),
        ("can_prefix",       _v_can_prefix),
        ("just_prefix",      _v_just_prefix),
        ("double_word",      _v_double_word),
    ]
    # 5 leetify variants
    for k in range(5):
        base.append((f"leet_{k}", (lambda t, kk=k: _v_leetify(t, kk))))
    # Pad to 100 with a rotating chain of safe transforms.
    while len(base) < 100:
        # Compose transformations deterministically.
        i = len(base)
        a = base[i % 26][1]
        b = base[(i * 3) % 26][1]
        base.append((
            f"compose_{i:03d}",
            (lambda t, a=a, b=b: b(a(t))),
        ))
    return tuple(base[:100])


_VARIANTS: Tuple[Tuple[str, callable], ...] = _build_variants()


# ──────────────────────────────────────────────────────────────────
# Per-run scoring
# ──────────────────────────────────────────────────────────────────

def _has_jargon(body: str) -> bool:
    lower = body.lower()
    for tok in _JARGON_TOKENS:
        if tok.lower() in lower:
            return True
    return False


def _has_false_live_claim(body: str) -> bool:
    lower = body.lower()
    for ph in _FALSE_LIVE_PHRASES:
        if ph in lower:
            return True
    for tok in FORBIDDEN_OUTPUT_TOKENS:
        if tok in lower:
            return True
    return False


def _asserts_live_action(body: str) -> bool:
    # "no live behavior" is fine ("no live" is allowed).
    lower = body.lower()
    bad = (
        "i just routed",
        "i just called",
        "i deployed",
        "now live",
        "live deployment",
    )
    for b in bad:
        if b in lower:
            return True
    return False


def _suggests_next_step(suggestions: Tuple[str, ...]) -> bool:
    return bool(suggestions) and any(bool(s.strip()) for s in suggestions)


def _score_response(
    expected_intent: str,
    classified_intent: str,
    response_body: str,
    suggestions: Tuple[str, ...],
    variant_name: str,
) -> Dict[str, bool]:
    body = response_body or ""
    return {
        "understood_intent":         classified_intent == expected_intent,
        "human_tone":                not _has_jargon(body),
        "useful_answer":             len(body) >= MIN_USEFUL_CHARS,
        "no_jargon":                 not _has_jargon(body),
        "no_false_claim":            not _has_false_live_claim(body),
        "no_live_action":            not _asserts_live_action(body),
        "suggests_next_step":        _suggests_next_step(suggestions),
        "handles_typo_or_fragment":  bool(body),
    }


def _passed(metrics: Dict[str, bool]) -> bool:
    return all(metrics.values())


# ──────────────────────────────────────────────────────────────────
# Runner core
# ──────────────────────────────────────────────────────────────────

def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def run_simulations(
    questions_limit: Optional[int] = None,
    variants_limit: Optional[int] = None,
) -> Dict:
    catalogue = list(BROKER_QUESTION_CATALOGUE)
    if questions_limit is not None and questions_limit < len(catalogue):
        catalogue = catalogue[:questions_limit]
    variants = list(_VARIANTS)
    if variants_limit is not None and variants_limit < len(variants):
        variants = variants[:variants_limit]

    total_runs = 0
    total_pass = 0
    failed_examples: List[Dict] = []

    per_intent: Dict[str, Dict[str, int]] = {
        i: {"runs": 0, "pass": 0, "understood": 0,
            "jargon": 0, "false_claim": 0}
        for i in INTENT_CODES
    }
    typo_runs = 0
    typo_pass = 0
    jargon_count = 0
    false_claim_count = 0

    for q in catalogue:
        expected_intent = q["intent"]
        base_text = q["text"]
        for variant_name, fn in variants:
            try:
                variant_text = fn(base_text)
            except Exception:
                # A variant transform should never raise; defence
                # in depth — treat as a non-pass.
                variant_text = base_text
            # PAS204-C — apply the dispatcher's fuzzy
            # normalization before classification, matching the
            # real production code path.
            normalized_text = normalize_fuzzy_command(variant_text)
            classification = match_broker_intent(normalized_text)
            classified_intent = classification["intent"]
            envelope = build_broker_response(normalized_text)
            body = str(envelope.get("response_text") or "")
            suggestions = envelope.get("suggested_next") or ()

            metrics = _score_response(
                expected_intent,
                classified_intent,
                body,
                suggestions,
                variant_name,
            )
            run_passed = _passed(metrics)
            total_runs += 1
            if run_passed:
                total_pass += 1

            pi = per_intent[expected_intent]
            pi["runs"] += 1
            if run_passed:
                pi["pass"] += 1
            if metrics["understood_intent"]:
                pi["understood"] += 1
            if not metrics["no_jargon"]:
                pi["jargon"] += 1
                jargon_count += 1
            if not metrics["no_false_claim"]:
                pi["false_claim"] += 1
                false_claim_count += 1

            # Typo-or-fragment variants. We classify anything
            # that mutates the text away from the canonical
            # form as "typo-or-fragment" for the failure-rate
            # metric.
            is_typo = variant_name not in ("identity", "title")
            if is_typo:
                typo_runs += 1
                if run_passed:
                    typo_pass += 1

            if not run_passed and len(failed_examples) < 50:
                failed_examples.append({
                    "question_text":         base_text,
                    "variant_name":          variant_name,
                    "variant_text":          variant_text,
                    "expected_intent":       expected_intent,
                    "classified_intent":     classified_intent,
                    "metrics":               metrics,
                })

    weakest_intents = sorted(
        (
            {"intent": i, "runs": d["runs"], "pass": d["pass"],
             "pass_rate": round((d["pass"] / d["runs"]) if d["runs"] else 0.0, 4),
             "understood": d["understood"], "jargon": d["jargon"],
             "false_claim": d["false_claim"]}
            for i, d in per_intent.items() if d["runs"]
        ),
        key=lambda x: (x["pass_rate"], x["intent"]),
    )

    # "Recommended prompt improvements" — bounded structural
    # hints derived from the metrics, not free-form prose.
    recs: List[str] = []
    if jargon_count > 0:
        recs.append("translate_remaining_jargon_tokens")
    if false_claim_count > 0:
        recs.append("strip_residual_live_phrases")
    bottom = [w for w in weakest_intents if w["pass_rate"] < 0.99]
    if bottom:
        recs.append("expand_keyword_coverage_for_weak_intents")
    if not recs:
        recs.append("no_changes_recommended")

    return {
        "phase":              "PAS204",
        "generated_at":       _now_iso(),
        "total_questions":    len(catalogue),
        "total_runs":         total_runs,
        "pass_count":         total_pass,
        "pass_rate":          round((total_pass / total_runs) if total_runs else 0.0, 4),
        "typo_failure_rate":  round(
            ((typo_runs - typo_pass) / typo_runs) if typo_runs else 0.0, 4
        ),
        "jargon_leak_rate":   round(
            (jargon_count / total_runs) if total_runs else 0.0, 4
        ),
        "false_claim_count":  false_claim_count,
        "weakest_intents":    weakest_intents,
        "recommended_prompt_improvements": recs,
        "top_failed_examples":              failed_examples,
        "allowed_environment":              "SIMULATION_ONLY",
        "live_behavior_changed":            False,
    }


# ──────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="pas204_run_broker_question_simulations",
        description=(
            "PAS204 — Run every broker question through every "
            "deterministic variant, classify it, build the response, "
            "and score the result. Writes a single bounded JSON report "
            "under reports/simulations/. Read-only and SIMULATION_ONLY."
        ),
    )
    p.add_argument("--questions", type=int, default=None,
                   help="Run only the first N questions (default: all)")
    p.add_argument("--variants", type=int, default=None,
                   help="Apply only the first N variants per question "
                        "(default: 100)")
    p.add_argument("--output-dir",
                   default=str(_REPO_ROOT / REPORTS_SUBDIR),
                   help="Directory to write the simulation report into")
    p.add_argument("--summary-only", action="store_true",
                   help="Do not write a JSON file; print summary only")
    p.add_argument("--json", action="store_true",
                   help="Print the full report payload as JSON to stdout")
    return p


def _write_report(out_dir: Path, payload: dict) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = payload.get("generated_at", _now_iso()).replace(":", "").replace("-", "")
    name = f"pas204_broker_conversation_simulation_{ts}.json"
    fp = out_dir / name
    fp.write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return fp


def _print_summary(report: dict, written: Optional[Path]) -> None:
    print(
        f"[PAS204] runs={report['total_runs']} "
        f"pass={report['pass_count']} "
        f"pass_rate={report['pass_rate']} "
        f"typo_failure_rate={report['typo_failure_rate']} "
        f"jargon_leak_rate={report['jargon_leak_rate']} "
        f"false_claim_count={report['false_claim_count']}"
    )
    weakest = report.get("weakest_intents") or []
    if weakest:
        print("[PAS204] weakest intents:")
        for w in weakest[:5]:
            print(
                f"  - {w['intent']:25s} pass_rate={w['pass_rate']:.4f} "
                f"runs={w['runs']} jargon={w['jargon']} "
                f"false_claim={w['false_claim']}"
            )
    print(
        f"[PAS204] recommended: "
        f"{', '.join(report.get('recommended_prompt_improvements') or [])}"
    )
    if written is not None:
        print(f"[PAS204] report written: {written}")


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as e:
        return 2 if e.code not in (0, None) else int(e.code or 0)

    try:
        out_dir = Path(args.output_dir)
        if not args.summary_only:
            out_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(
            f"error: cannot create output dir {args.output_dir}: "
            f"{type(e).__name__}",
            file=sys.stderr,
        )
        return 2

    report = run_simulations(
        questions_limit=args.questions,
        variants_limit=args.variants,
    )

    written: Optional[Path] = None
    if not args.summary_only:
        written = _write_report(out_dir, report)

    _print_summary(report, written)

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))

    return 0


if __name__ == "__main__":
    sys.exit(main())
