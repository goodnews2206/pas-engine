# PAS208 — Operator approval for proactive recommendations

## What PAS208 proves

PAS208 turns each PAS205 attention signal into a bounded
`Recommendation` object that an operator can approve, reject, or
defer. It proves that:

* The proactive observer's signals can be transformed into a
  closed-vocabulary "operator approval" representation without
  any execution surface.
* The approval state machine has only four states and the only
  way to transition between them is the pure
  `apply_decision(rec, decision, operator_ref, …)` function,
  which returns a NEW frozen `Recommendation` value object.
  Nothing in the engine changes.
* Approval status is metadata. PAS208 carries
  `operator_required=True` and `live_behavior_changed=False` on
  every recommendation and every digest. The readiness gate
  asserts both invariants textually AND by runtime probe.
* Adding the approval layer required zero changes to PAS193–
  PAS207 contracts. PAS207's Slack surface and PAS205/PAS206
  remain untouched.

## What PAS208 does NOT prove

* PAS208 does not execute any approved recommendation.
* PAS208 does not call Twilio, send SMS, send email, post to
  Slack, write to the database, schedule a future action, or
  start a worker.
* PAS208 does not propose new signal types — it only maps the
  ten PAS205 signal types to ten matching recommended-action
  types.
* PAS208 does not surface itself in Slack yet. The CLI writes a
  local JSON artifact under `reports/recommendations/`; how
  operators see and act on approvals is a later wiring step.
* PAS208 does not introduce a new external vendor.

## Approval state machine

```
                  ┌──────────────────────────────┐
                  │                              │
                  │           CANDIDATE          │
                  │  (initial state, set by      │
                  │   build_recommendations)     │
                  │                              │
                  └──────┬─────────────┬─────────┘
                         │             │
                         ▼             ▼
                  ┌──────────────┐   ┌──────────────┐
                  │  DEFERRED    │   │   APPROVED   │
                  │  (re-entry   │   │ _FOR_MANUAL  │
                  │   point —    │   │   _REVIEW    │
                  │   can leave) │   │  (terminal)  │
                  └──────┬───────┘   └──────────────┘
                         │
                         ▼
                  ┌──────────────┐
                  │   REJECTED   │
                  │  (terminal)  │
                  └──────────────┘
```

* `CANDIDATE` is the only initial state. Every recommendation
  emerges from `build_recommendations()` in this state.
* `APPROVED_FOR_MANUAL_REVIEW` and `REJECTED` are terminal —
  `apply_decision()` refuses to transition out of them.
* `DEFERRED` is the only re-entry point. From `DEFERRED` an
  operator may apply any of the three terminal decisions later.
* `apply_decision()` requires a non-empty `operator_ref` and
  produces a new frozen `Recommendation` carrying
  `decided_at`, `decided_by`, and an optional `decision_reason`.
* `apply_decision()` never reads or writes the database, never
  sends a Slack message, never calls Twilio.

## Signal → action mapping

The closed mapping in `SIGNAL_TO_ACTION_TYPE`:

| PAS205 signal_type              | PAS208 recommended_action_type        |
|---------------------------------|---------------------------------------|
| `callback_overdue`              | `draft_callback_followup`             |
| `lead_unassigned`               | `draft_agent_assignment`              |
| `stale_lead`                    | `draft_soft_checkin`                  |
| `missed_first_response`         | `draft_first_contact`                 |
| `failed_booking_confirmation`   | `draft_booking_retry`                 |
| `no_agent_available`            | `draft_coverage_shift`                |
| `repeated_failed_calls`         | `draft_alternate_channel`             |
| `after_hours_lead_pending`      | `draft_after_hours_plan`              |
| `high_value_lead_waiting`       | `draft_senior_agent_handoff`          |
| `needs_human_review`            | `draft_human_review_request`          |

Every action type is a `draft_…` — never an `execute_…`. The
draft is a description of what the operator could approve doing,
not an instruction the engine will carry out.

## Recommendation envelope

| Field                       | Meaning                                                |
|-----------------------------|--------------------------------------------------------|
| `recommendation_id`         | deterministic SHA-256-derived id (signal_id + action)  |
| `signal_id`                 | source PAS205 signal id                                |
| `signal_type`               | PAS205 signal_type carried over                        |
| `severity`                  | PAS205 severity carried over                           |
| `subject_type`              | `lead` / `call` / `booking` / `callback` / `pipeline`  |
| `subject_ref`               | PAS205 subject_ref carried over                        |
| `recommended_action_type`   | one of `RECOMMENDED_ACTION_TYPES`                      |
| `approval_status`           | one of `APPROVAL_STATES`                               |
| `reason`                    | broker-voice description                               |
| `evidence`                  | PAS205 evidence carried over                           |
| `created_at`                | PAS205 created_at                                      |
| `decided_at`                | set by `apply_decision`                                |
| `decided_by`                | operator_ref recorded by `apply_decision`              |
| `decision_reason`           | optional free-text reason                              |
| `operator_required`         | **always True**                                        |
| `live_behavior_changed`     | **always False**                                       |

## CLI

```
python scripts/pas208_run_proactive_recommendations_demo.py
```

Builds recommendations from the same deterministic demo snapshot
PAS207 uses, exercises a fixed three-decision cycle (approve /
reject / defer) on the first three recommendations, leaves the
rest in `CANDIDATE`, and writes a JSON artifact under
`reports/recommendations/`. No Supabase calls, no Twilio, no
Slack outbound.

## How PAS208 moves PAS closer to proactive agents

| Phase  | Layer                                              |
|--------|----------------------------------------------------|
| PAS205 | Signal generation from in-memory snapshots         |
| PAS206 | Read-only snapshot from Supabase                   |
| PAS207 | Slack proactive digest surface (pull/read)         |
| **PAS208** | **Operator approval for proactive recommendations** |
| PAS209 | Bounded action proposals (still operator-gated)    |

Each step is additive and reversible. PAS208 in particular is
fully revertable by deleting one module, one CLI script, one
readiness script, one test file, and one doc.

## Safety doctrine

* **READ-ONLY.** No DB write, no Slack API write, no Twilio call.
* **NO EXECUTION.** No `execute / dispatch / send_real_ /
  auto_apply / auto_promote / post_to_slack / route_lead_live`
  identifiers in the module source.
* **NO MUTATION.** No `insert / update / delete / upsert / rpc`.
* **NO SCHEDULER, NO WORKER, NO CRON.**
* **NO MIGRATIONS.** No `combined_supabase_migration.sql`.
* **NO SECRETS.** Credentials never touched.
* **PARKED STASH UNTOUCHED.**
* **PAS193–PAS207 BEHAVIOR PRESERVED.**
