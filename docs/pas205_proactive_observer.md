# PAS205 — Read-Only Proactive Observer

## Purpose

PAS193–PAS204 made PAS evidence-rich, voice-aware, and operator-
readable. PAS is now fast at *answering*: inbound leads, Slack
operator questions, simulation rehearsals. It is still
fundamentally **reactive** — it responds to something a lead, an
operator, or a simulation triggers.

PAS205 is the first layer that begins to make PAS **see the whole
pipeline on its own**.

It does so in the smallest possible step:

  * It does not call anyone.
  * It does not text anyone.
  * It does not email anyone.
  * It does not post to Slack.
  * It does not write to the database.
  * It does not schedule itself to run.

It only **observes** an in-memory snapshot of brokerage pipeline
state and produces a deterministic "needs attention" digest. The
digest is what later PAS layers will turn into recommendations
(PAS208) and operator-approved actions (PAS209).

PAS205 is proactive visibility, **not autonomous action**.

## Research basis

Brokers consistently lose deals to four operational failure
modes:

  * **Late first contact.** Speed-to-lead falls off a cliff
    after 5 minutes; the brokerage that calls back first usually
    wins the listing.
  * **Dropped callbacks.** A promised callback that doesn't
    happen on time destroys the trust the first conversation
    built.
  * **Stale leads.** Leads that go quiet recover only with a
    soft, well-timed nudge — too aggressive and they're gone for
    good.
  * **Coverage gaps.** After-hours, weekends, holidays, and
    short-staffed mornings produce leads that nobody answered.

PAS205 turns each of those failure modes into a closed signal
type and detects them on a structured snapshot of brokerage
pipeline state, with deterministic rules and no LLM in the loop.

## Closed signal vocabulary

| Signal type                    | Meaning                                                                       |
| ------------------------------ | ----------------------------------------------------------------------------- |
| `callback_overdue`             | A pending callback's scheduled time has passed without completion.            |
| `lead_unassigned`              | A lead is sitting in the pipeline with no agent attached.                     |
| `stale_lead`                   | A lead has had no activity for an extended period.                            |
| `missed_first_response`        | A lead has been in the pipeline past the first-response target with no reply. |
| `failed_booking_confirmation`  | A booking attempt did not reach a confirmed state.                            |
| `no_agent_available`           | No agent is currently available while leads are waiting.                      |
| `repeated_failed_calls`        | A lead has accumulated multiple failed call attempts on the same number.     |
| `after_hours_lead_pending`     | A lead arrived after hours and has been waiting past the after-hours window.  |
| `high_value_lead_waiting`      | A lead marked high-value has not yet received first contact.                  |
| `needs_human_review`           | A lead was explicitly flagged for human review.                               |

Every signal carries:

  * `signal_id` — deterministic SHA-256-derived id.
  * `signal_type` — closed vocabulary above.
  * `severity` — `low` | `medium` | `high`.
  * `subject_type` — `lead` | `call` | `booking` | `callback` | `pipeline`.
  * `subject_ref` — the snapshot id of the affected entity.
  * `reason` — a plain-English explanation a broker can read.
  * `recommended_next_step` — what a *human* should do next. PAS205
    never recommends "PAS will call them"; the next step is always
    something a human owns.
  * `evidence` — a structured mapping with the timestamps and
    counts the rule used to fire.
  * `created_at` — UTC ISO 8601.
  * `live_behavior_changed` — always `False`. PAS205 cannot
    change live behavior by construction.

## What PAS205 proves

  * **Proactive visibility exists.** PAS can now look at a
    pipeline snapshot, identify the ten failure modes above, and
    explain each one in plain English.
  * **Deterministic detection.** Same snapshot, same rules, same
    output — forever. No LLM, no randomness, no clock drift.
  * **Honest scope.** Every recommended next step is phrased as
    advice to a human; PAS205 cannot dispatch anything.
  * **Closed vocabulary discipline.** The set of signals is
    fixed and asserted by tests; the readiness gate refuses any
    drift.
  * **Read-only by construction.** The production surface has no
    file I/O, no DB session, no network client, no Twilio /
    Slack outbound / LLM / Supabase / worker / scheduler imports.
    The readiness gate enforces this with AST checks.
  * **Bounded artefact footprint.** The demo runner writes one
    JSON under `reports/simulations/` and nothing else.
  * **No migrations.** PAS205 ships no SQL, touches no schema,
    leaves `combined_supabase_migration.sql` alone.

## What PAS205 does not prove

  * **It is not yet a true autonomous proactive agent.** PAS205
    has no scheduler, no worker, no live pipeline subscription.
    It produces signals only when something hands it a snapshot.
  * **It does not read from Supabase yet.** The demo runner uses
    a hand-crafted in-memory snapshot. PAS206 will add a
    read-only Supabase snapshot adapter; PAS207 will surface the
    digest through Slack; PAS208 will gate recommendations
    behind operator approval; PAS209 will introduce bounded
    action proposals.
  * **It does not validate or enforce TCPA / consent /
    quiet-hours / Twilio-trial state.** It produces *advice*
    only; the action layer must own all of that.
  * **It cannot prove the snapshot it observed is true.** That
    invariant belongs to the future PAS206 adapter and to the
    upstream PAS pipeline.
  * **It is not a real-time dashboard.** It is a deterministic
    function from snapshot to digest. PAS207 will be the place
    where periodic publication lives, with explicit operator
    consent.

## Safety doctrine

  * `phase=PAS205`, `allowed_environment=SIMULATION_ONLY`,
    `live_behavior_changed=False` on every digest.
  * Production surface (`observer_models.py`, `observer.py`,
    `observer_digest.py`) never imports `twilio`, `slack_sdk`,
    `openai`, `anthropic`, `dotenv`, `supabase`, the live state
    machine, outbound notifications, or workers.
  * Production surface declares no identifier named
    `apply_*`, `deploy_*`, `route_*_live`, `send_real_*`,
    `auto_apply`, `auto_promote`, `post_to_slack`,
    `place_call`, `start_worker`, `schedule_cron`.
  * The demo runner writes exclusively under
    `reports/simulations/`.
  * The readiness gate refuses any drift from the above.

## Tone

PAS205's human output sounds like a teammate, not a tool:

> "I found three things that need attention. One callback is
> overdue, two leads have no assigned agent, and one booking
> attempt did not confirm. One of these is time-sensitive —
> worth eyes on it first."

It avoids closed-vocab tokens like `callback_overdue` and
`live_behavior_changed` in user-facing output. Those tokens are
for machines; brokers and operators get sentences.

## How it relates to becoming a proactive agent

PAS205 is the **signal** layer. A proactive agent needs four more
layers on top of this one — and shipping them in this order is
how we avoid catastrophic premature autonomy:

  * **PAS206 — read-only Supabase snapshot adapter.** Replace
    the in-memory demo snapshot with a real, read-only adapter
    against the brokerage's Supabase. Still no writes, still no
    actions.

  * **PAS207 — proactive Slack digest surface.** Publish the
    digest through the existing PAS201/202/203 Slack surface,
    explicitly opt-in per brokerage, with quiet-hours and
    coverage settings.

  * **PAS208 — operator approval for proactive
    recommendations.** Turn signals into *candidate
    recommendations* (reusing the PAS195 candidate-recommendation
    shape) and route them through the PAS196 operator-review
    surface.

  * **PAS209 — bounded action proposals.** Only after PAS208 has
    been live and clean for an extended window does PAS gain the
    ability to *propose* an action with a clear default-off
    "DRY_RUN" mode, explicit consent / TCPA / quiet-hours /
    Twilio-trial gates, and an operator-controlled live toggle.

## Future path

  * **PAS206** — Read-only Supabase snapshot adapter.
  * **PAS207** — Proactive Slack digest surface (opt-in, quiet-
    hours aware).
  * **PAS208** — Operator approval for proactive recommendations.
  * **PAS209** — Bounded action proposals (dry-run by default,
    compliance-gated).

## Claimable

After PAS205 we can honestly say:

  * "PAS continuously inspects the brokerage pipeline against
    ten operational failure modes and explains each one in plain
    English."
  * "PAS produces a deterministic, evidence-bearing
    needs-attention digest for any pipeline snapshot."
  * "PAS recommends what a human should do — and only what a
    human should do."

## Still not claimable

We must **not** claim, today:

  * "PAS proactively reaches out to leads."
  * "PAS autonomously books appointments without operator
    involvement."
  * "PAS continuously watches the brokerage in real time."
  * "PAS acts on its own when nothing has been said to it."

Those claims belong to PAS207+ at earliest, and only after the
compliance, consent, and Twilio-trial gates are in place.
