# PAS209 — Bounded action proposal packages

## What PAS209 proves

PAS209 turns each PAS208 recommendation that an operator has
explicitly **approved for manual review** into a strictly bounded
`ActionProposal` — a frozen value object containing a draft
message or instruction, a short list of safety notes, and a short
list of rollback notes. It proves that:

* PAS can compose an end-to-end proactive stack — observer →
  recommendations → operator approval → bounded proposal — without
  any execution surface anywhere along the path.
* The proposal stops at "what a human could read and send by
  hand." PAS never sends, calls, schedules, mutates, or queues.
* Every emitted proposal is constrained by three hard invariants
  that the readiness gate asserts both textually and via a runtime
  sanity probe:
    * `required_human_review = True`
    * `allowed_channel = "MANUAL_ONLY"`
    * `live_behavior_changed = False`
* Adding the proposal layer required zero changes to PAS193–
  PAS208 contracts.

## What PAS209 does NOT prove

* PAS209 does not execute anything. Even a proposal whose source
  recommendation is APPROVED does nothing on its own.
* PAS209 does not call Twilio, send SMS, send email, post to
  Slack, write to the database, schedule a future action, or
  start a worker.
* PAS209 does not propose new signal types or action types — it
  consumes the closed PAS208 vocabulary as-is.
* PAS209 does not surface itself in Slack or any operator UI yet.
  The CLI writes a local JSON artifact under
  `reports/proposals/`.
* PAS209 does not introduce a new external vendor.

## Why "MANUAL_ONLY" is the only allowed channel

`ALLOWED_CHANNELS = ("MANUAL_ONLY",)` — a closed tuple with exactly
one entry. The single allowed channel is metadata describing how
the operator may consume the proposal: by reading the draft and
sending it themselves. It is NOT an instruction PAS will honour
on its own. The readiness gate asserts this invariant directly
and also asserts that every emitted proposal carries this value.

A future phase that introduced a non-manual channel would need
to:

1. extend the tuple,
2. add explicit per-channel safety / rollback / approval logic,
3. and pass a much stricter readiness gate.

PAS209 deliberately ships with the smallest possible channel set.

## Proposal envelope

`build_proposal(rec)` returns `None` for any recommendation
whose `approval_status` is not `APPROVED_FOR_MANUAL_REVIEW`. For
approved recommendations it returns an `ActionProposal`:

| Field                          | Meaning                                                          |
|--------------------------------|------------------------------------------------------------------|
| `proposal_id`                  | deterministic SHA-256-derived id (recommendation_id + action)    |
| `recommendation_id`            | source PAS208 recommendation id                                  |
| `signal_id`                    | source PAS205 signal id (carried through)                        |
| `signal_type`                  | PAS205 signal_type                                               |
| `severity`                     | PAS205 severity                                                  |
| `subject_type`                 | `lead` / `call` / `booking` / `callback` / `pipeline`            |
| `subject_ref`                  | PAS205 subject_ref                                               |
| `proposed_action_type`         | the same closed PAS208 `draft_*` vocabulary                      |
| `draft_message_or_instruction` | plain text — the operator may copy and send manually             |
| `safety_notes`                 | bounded tuple — checks the operator should do before sending     |
| `rollback_notes`               | bounded tuple — how the operator can undo it if sent incorrectly |
| `evidence`                     | PAS205 evidence carried through                                  |
| `created_at`                   | PAS205 created_at                                                |
| `required_human_review`        | **always True**                                                  |
| `allowed_channel`              | **always `MANUAL_ONLY`**                                         |
| `live_behavior_changed`        | **always False**                                                 |

## Action type → draft template

| Action type                     | Draft kind                                            |
|---------------------------------|-------------------------------------------------------|
| `draft_callback_followup`       | Draft message to a lead whose callback was missed     |
| `draft_agent_assignment`        | Instruction to assign a lead to a specific agent      |
| `draft_soft_checkin`            | Draft soft check-in message for a quiet lead          |
| `draft_first_contact`           | Draft outreach message for first contact              |
| `draft_booking_retry`           | Draft message asking the lead to confirm / reschedule |
| `draft_coverage_shift`          | Instruction to bring a backup agent online            |
| `draft_alternate_channel`       | Draft message asking to switch contact channel        |
| `draft_after_hours_plan`        | Instruction to hand to next on-shift agent            |
| `draft_senior_agent_handoff`    | Instruction to hand high-value lead to a senior agent |
| `draft_human_review_request`    | Instruction to escalate for human / compliance review |

Every template ships with at least one safety note and at least
one rollback note. Drafts use Mustache-style placeholders like
`{{lead_name|there}}`; the operator fills them in before sending.

## CLI

```
python scripts/pas209_run_action_proposals_demo.py
```

Composes the full stack on the same deterministic demo snapshot
PAS207 / PAS208 use:

1. PAS205 observer runs over the seeded snapshot.
2. PAS208 `build_recommendations` produces a recommendation digest
   (all CANDIDATE).
3. The CLI approves the first `--approve-n` recommendations
   (default: 3) via `apply_decision`.
4. PAS209 `build_proposal_package` walks the digest and produces
   one `ActionProposal` per APPROVED recommendation.
5. The CLI writes a JSON artifact under `reports/proposals/`.

Nothing in step 4 calls Twilio, Slack, the database, or a
scheduler. Steps 1–4 are pure functions on frozen value objects.

## End-to-end proactive stack

| Phase  | Layer                                              |
|--------|----------------------------------------------------|
| PAS205 | Signal generation from in-memory snapshots         |
| PAS206 | Read-only snapshot from Supabase                   |
| PAS207 | Slack proactive digest surface (pull/read)         |
| PAS208 | Operator approval for proactive recommendations    |
| **PAS209** | **Bounded action proposals (manual review only)** |

Each step is additive and reversible. PAS209 is fully revertable
by deleting one module, one CLI script, one readiness script, one
test file, and one doc.

## Safety doctrine

* **READ-ONLY.** No DB write, no Slack API write, no Twilio call.
* **NO EXECUTION.** No `execute / dispatch / send_real_ /
  auto_apply / auto_promote / post_to_slack / route_lead_live`
  identifiers in the module source.
* **NO MUTATION.** No `insert / update / delete / upsert / rpc`.
* **NO SCHEDULER, NO WORKER, NO CRON.**
* **NO MIGRATIONS.** No `combined_supabase_migration.sql`.
* **NO NEW VENDORS.**
* **NO SECRETS.** Credentials never touched.
* **PARKED STASH UNTOUCHED.**
* **PAS193–PAS208 BEHAVIOR PRESERVED.**
* **MANUAL_ONLY ENFORCED.** Every proposal declares its only
  legal consumption channel as `MANUAL_ONLY`. A future phase
  that wants any other channel must extend the closed tuple and
  pass a stricter readiness gate first.
