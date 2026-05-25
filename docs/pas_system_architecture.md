# PAS System Architecture

> Status: draft v1. Owner: ORVN Labs. Last updated: 2026-05-25.
> Sibling to `docs/pas_product_design_book.md` (source of truth for
> product behaviour and language). This document defines *how* the PAS
> system is laid out — the layers, the boundaries, and the operating
> sequence. No frontend implementation; no production-code change.

## 0. Scope and cross-cutting rules

This document covers system structure: layers, responsibilities, and
how data and authority flow between them. Specific surfaces, copy, and
role bundles are governed by the Product Design Book and are referenced
here, not re-stated.

The following rules apply to every layer below. Any layer that would
violate one of them is, by definition, mis-designed:

- **Extreme simplicity.** Each layer has one job. If a layer needs a
  paragraph to explain its job, redesign it.
- **High functionality.** Every layer must serve a decision a real
  human needs to make.
- **Premium visual + interaction quality.** Architecture choices must
  not foreclose a premium experience on the surface above them.
- **No fake certainty.** If evidence is thin, the system surfaces that
  fact; it never papers over it.
- **No hidden automation.** Anything that takes a live action is
  named, bounded, approved, and audited.
- **Explainable, queryable, reversible-where-possible.** Every action
  the system takes can be explained, queried, and undone where the
  semantics allow.
- **Role-based permissions** govern every action — see Product Design
  Book §2.
- **Demo/rehearsal labels** are pinned to every artifact whose
  evidence comes from simulation.
- **No raw internal tokens in user-facing UI.** API keys, internal
  identifiers, integration secrets, and infra hostnames stay below the
  API surface.
- **PAS speaks like operations staff reporting to leadership.** See
  Product Design Book §8.7.

---

## 1. High-level architecture

PAS is composed of six layers and one core operating sequence. The
layers are vertical (top = closest to the user); the sequence is
horizontal (left = "we noticed something"; right = "we have receipts").

```
                          USER SURFACES
            ┌──────────────────────┬───────────────────┐
            │       Web app        │       Slack       │
            │ (comprehensive       │ (simplified,      │
            │   command surface)   │   read-mostly +   │
            │                      │   approve)        │
            └──────────────────────┴───────────────────┘
                                │
                  ┌─────────────┴──────────────┐
                  │  In-app PAS communication  │
                  │   (PAS-as-staff-member)    │
                  └─────────────┬──────────────┘
                                │
            ┌─────────────────────────────────────────┐
            │              PAS API surface            │
            │  (auth, role enforcement, scope guards) │
            └─────────────────────────────────────────┘
                                │
   ┌────────────────────┼──────────────────────┐
   │                    │                      │
┌──┴───────────┐ ┌──────┴────────────┐ ┌───────┴─────────┐
│  Backend     │ │  Proactive layer  │ │  Recommendation │
│  runtime     │ │  (Observer,       │ │  / approval /   │
│  (FSM, call  │ │   needs-attention,│ │  action-proposal│
│  engine,     │ │   read-only)      │ │   path          │
│  callbacks)  │ │                   │ │                 │
└──────┬───────┘ └─────────┬─────────┘ └────────┬────────┘
       │                   │                    │
       └────────┬──────────┴────────────────────┘
                │
        ┌───────┴────────────┐
        │  Integration layer │
        │  (read first,      │
        │   write later)     │
        └───────┬────────────┘
                │
        ┌───────┴───────────────┐
        │  Audit / logging      │
        │  (pas_events sink,    │
        │   audit surface)      │
        └───────┬───────────────┘
                │
        ┌───────┴───────────────┐
        │  Future execution     │
        │  layer (live actions, │
        │  bound + approved)    │
        └───────────────────────┘
```

### 1.1 The core operating sequence

> **Observe → Understand → Recommend → Approve → Execute → Audit**

Every PAS behaviour, end-to-end, walks this sequence. Surfaces, copy,
and approvals are designed around it. Each step has explicit gates:

| Step | What happens | Layer | Live-behavior gate |
|---|---|---|---|
| **Observe** | Read-only sensing across calls, integrations, events. | Proactive layer | `live_behavior_changed=False` |
| **Understand** | Compose signals into a digest with linked evidence. | Proactive + PAS Brain | `live_behavior_changed=False` |
| **Recommend** | Surface a recommendation to the right role. | Recommendation path (PAS208) | `live_behavior_changed=False`, `operator_required=True` |
| **Approve** | A human signs off (or declines, or modifies). | Web app + Slack | The gate is *the human*. |
| **Execute** | Bounded, named action runs against integrations. | Future execution layer | `live_behavior_changed=True` *for this named action only.* |
| **Audit** | Every step lands in `pas_events`; user-visible audit surface. | Audit layer | Append-only. |

The invariant **`live_behavior_changed=False`** holds across every
layer up to and including the recommendation surface. It is only flipped
inside a specific, named, operator-approved action — and only for the
scope of that action.

---

## 2. Backend runtime layer

The deterministic core that runs calls and engine logic.

### 2.1 Responsibilities

- **Call engine.** The 7-state FSM (GREETING → INTENT → BUDGET →
  TIMELINE → BOOKING → CLOSING → DONE), plus the callback-capture flow
  (PAS128) and outcome handling.
- **Simulation endpoint.** `/simulate-call` — text-in / text-out
  rehearsal without Twilio.
- **Routing logic.** Agent best-fit scoring; warm-transfer flag.
- **State persistence.** Writes structured decision-trace data to the
  database; emits to `pas_events`.

### 2.2 Boundaries

- The runtime does **not** decide whether to take a proactive action
  against external systems. That belongs to the recommendation /
  approval / action-proposal path.
- The runtime does **not** call Slack outbound, send email, or write
  to integrations beyond Cal.com booking. Any new external mutation
  point is a layer-3 (recommendation path) concern, not layer-2.
- The runtime exposes a stable contract to layers above. Layers above
  are forbidden from reaching past the API surface into the runtime
  internals.

### 2.3 Failure posture

- Runtime errors fall through to a graceful response and emit a
  `call.error` event. No surface above the API ever sees a stack trace.
- Failed integrations (Cal.com, etc.) degrade to documented fallback
  outcomes (see Product Design Book §4.5 warning copy).

---

## 3. Web app layer

The comprehensive command surface. Browser-only in v1.

### 3.1 Responsibilities

- **Render every module** defined in Product Design Book §4.
- **Enforce role bundles** from §2 of the design book — the navigation
  itself is role-shaped (see Dashboard IA doc).
- **Host the in-app PAS communication layer** (composer, peek pane,
  full thread).
- **Display evidence inline** rather than linking out — transcripts,
  observer signals, recommendation receipts.
- **Surface approvals** at the point of decision, not behind a tab.

### 3.2 Boundaries

- The web app holds **no business logic** that isn't also enforced at
  the API. UI is an opinionated view over the truth; the truth lives
  below the API.
- The web app does not talk to integrations directly. All external
  reads/writes go through the PAS API surface.
- The web app does not store secrets client-side. See cross-cutting
  rule on raw internal tokens.

### 3.3 Future deliverables (sequence governed by Product Design Book §10)

- Foundation / shell.
- Role-based navigation.
- PAS communication.
- PAS205–PAS208 read-only surfaces.
- Integrations framework.
- Notifications.
- Action approval flows.

---

## 4. Slack simplified surface

The interrupt-driven, short-attention surface where the team already
lives. Read-mostly + approve.

### 4.1 Responsibilities

- **Needs-attention digest** (PAS207) — daily, scoped, human-readable.
- **Approval prompts** for action proposals and recommendations — one
  click + reason.
- **Evidence digest** (PAS201–PAS203) — receipts on demand.
- **Reply-driven workflow** — replying to a Slack message routes
  through the same intent layer as the in-app composer (see Dashboard
  IA + Notification Architecture).

### 4.2 Boundaries

- Slack does **not** receive raw transcripts, raw lead PII beyond
  display name + masked phone, or integration tokens. Redaction rules
  match the runtime's `pas_events` policy.
- Slack does **not** support multi-step authoring (creating a new
  brokerage, editing PAS Brain) — those live on the web app only.
- Slack is always a *summary* of the web app. If a brokerage hits a
  capability ceiling on Slack, the message points them to the web app.

---

## 5. In-app PAS communication layer

PAS-as-staff-member. Plain English, typo-tolerant, inline-evidence.

### 5.1 Responsibilities

- **Composer** at the bottom of every dashboard page.
- **Peek pane** top-right that follows across modules.
- **Full thread** for heavy or pinned contexts.
- **Section-pulling.** Asking about callbacks renders an embedded
  callback view inside the thread, not a link out.
- **Intent → API call.** Plain-English requests resolve to bounded,
  permissioned API calls below.
- **Action proposal handoff.** Any "do X" intent that needs approval
  routes through the recommendation/approval path, not direct write.

### 5.2 Boundaries

- The communication layer never bypasses role bundles. If the user
  cannot write to integrations, PAS drafts the action and routes it
  to someone who can.
- It does not invent data. If the underlying data is missing, PAS
  says so (see Design Book §8 standard copy).
- It does not retain conversation outside the brokerage's tenant
  boundary.

### 5.3 PAS's three non-negotiables (recap from Design Book §5)

1. **Explainable.** Show the reasoning, the evidence, and the policy.
2. **Queryable.** "Why?" returns a structured answer with links.
3. **Reversible-where-possible.** Reversible actions flagged as such;
   irreversible ones need a second explicit confirmation.

---

## 6. Proactive observer layer

Read-only sensing. PAS205 (observer) + PAS206 (Supabase snapshot
adapter) + PAS207 (Slack needs-attention digest).

### 6.1 Responsibilities

- **Sense** what's about to fall through — stalled leads, missed
  callbacks, conversations needing review.
- **Snapshot** state from Supabase via the read-only adapter
  (PAS206).
- **Digest** signals into a needs-attention surface for Slack and the
  web app.

### 6.2 Hard invariants

- `live_behavior_changed=False` on every signal, by construction.
- No DB writes, no Twilio calls, no Slack outbound POST, no scheduler,
  no background workers, no autonomous execution. The proactive layer
  is a *function* over the snapshot, not an agent.
- Output is always either rendered in a digest or passed up to the
  recommendation/approval path.

---

## 7. Recommendation / approval / action-proposal path

The bridge from "PAS noticed" to "PAS may act". PAS208 (operator-
approval recommendations) + PAS209 (bounded action proposals, in
flight).

### 7.1 Responsibilities

- **Compose recommendations** from observer signals. Always carries
  evidence link, scope, severity, and proposed outcome.
- **Compose action proposals** (PAS209) — bounded, named, with
  side-effect declaration, requested approver, and expiry.
- **Route to the right approver** per role bundle.
- **Capture the decision** — approve / decline / modify / let expire.
- **Hand off to the future execution layer** *only* when a proposal
  is approved within its bound.

### 7.2 Hard invariants

- Recommendations: `live_behavior_changed=False`,
  `operator_required=True`. Always.
- Action proposals: `live_behavior_changed=False` until and unless a
  proposal is explicitly approved. Even then, only the named action
  for the named scope flips the gate, and only for the duration of
  the execution call.
- Expiry: every proposal has a TTL. A lapsed proposal is recorded as
  "expired without decision" — never silently re-fired.

---

## 8. Integration layer

PAS's senses. Read-first; write is always a second, explicit opt-in.

### 8.1 Responsibilities

- **Connect** to external systems (CRM, Gmail, Sheets, Notion, etc.).
- **Surface scopes** in plain English (Product Design Book §7).
- **Sync** state inbound; cache where appropriate.
- **Expose** read APIs to the layers above.
- **Gate** writes behind an explicit per-integration opt-in.
- **Report health** — Healthy / Degraded / Disconnected.

### 8.2 Boundaries

- The integration layer does **not** decide *what* to read or write —
  that's driven by the layers above and by the operator's stated
  scope.
- It does **not** keep tokens accessible to the surfaces above. Tokens
  live below the API. Surfaces see "Connected as <account>", never the
  token itself.
- A degraded integration causes the layers above to label downstream
  evidence as stale; it does **not** silently substitute defaults.

### 8.3 Detail

See `docs/pas_integration_contracts.md`.

---

## 9. Audit / logging layer

The receipts. `pas_events` is the universal event sink (added pre-
PAS128). The user-facing Audit Log surface is the readable view over it.

### 9.1 Responsibilities

- **Ingest** events from every layer via `log_event_bg` (fire-and-
  forget, never raises).
- **Persist** in `pas_events` (soft cap ~8 KB per payload; FK
  constraints dropped in v6 so events land even when parent rows are
  absent).
- **Expose** an append-only read surface to the web app's Audit Logs
  module.
- **Redact** secrets — PAS125/PAS126 redaction must hold across every
  emitter.

### 9.2 Boundaries

- Audit entries are append-only. There is no delete or edit API.
- ORVN Internal Admin can read across tenants; tenant roles see
  scoped slices.
- Audit ingestion lag is acceptable; correctness is not. A late
  event is fine; a missing one is a bug.

---

## 10. Future execution layer

The layer that does not yet exist in any form that takes a live
action against external systems. This is **deliberate**.

### 10.1 Activation rules

- The execution layer is built **one named action at a time**. There
  is no generic "let PAS write" mode.
- Each named action has:
  - a declared scope (what it can touch),
  - declared side-effects (what changes externally),
  - a reversal path (or an explicit "irreversible" flag),
  - a required approver role,
  - a TTL,
  - an audit event spec emitted before, during, and after.
- An action only flips `live_behavior_changed=True` *for the duration
  of its run* and *only for the named action scope*. The gate snaps
  back to `False` immediately after.

### 10.2 Boundaries

- No background scheduler/cron lives in the execution layer in v1.
  Every execution is triggered by an operator approval.
- The execution layer can be physically the same process as the
  backend runtime, but its triggers are exclusively from the
  recommendation/approval path — never from the observer.

---

## 11. Cross-layer non-functional requirements

- **Tenant isolation.** Every API call carries an explicit tenant
  scope. Cross-tenant reads are ORVN-only and audit-logged.
- **Idempotency.** External writes carry idempotency keys; replaying a
  proposal does not duplicate an action.
- **Time discipline.** Every event carries UTC; surfaces render in the
  user's timezone with both absolute and relative formatting.
- **Backpressure.** Observer + recommendation passes are computed
  off the request path. The web app never blocks waiting on a sync.
- **Failure visibility.** Degraded sources are labelled as such on the
  surface above them. PAS never silently presents stale data as fresh.

---

## 12. Architectural invariants (checklist)

The system is correct only if every one of these holds at all times:

1. `live_behavior_changed=False` everywhere except inside a named,
   approved, bounded execution call.
2. No autonomous Slack outbound, DB write, Twilio mutation, or
   integration write occurs without an explicit operator approval.
3. No surface above the API holds raw secrets, tokens, or integration
   credentials.
4. Every action emits an audit event before, during (where
   applicable), and after.
5. Role bundles govern visibility *and* actions; surfaces never expose
   a button a role cannot use.
6. Demo/rehearsal evidence carries a label on every artifact.
7. Read-only roles literally cannot trigger a write — the API rejects,
   not just the UI.
8. Critical-severity notifications cannot be globally silenced by a
   non-Owner.
9. ORVN-internal capabilities cannot be granted from inside a tenant.
10. PAS never claims certainty it does not have.

---

## 13. Open architectural questions

Tracked here for v2 of this doc. None are blockers for v1.

- Multi-region: where does the runtime live for international
  brokerages? Latency to Twilio matters.
- Snapshot freshness: is per-event push viable, or is periodic
  snapshot sufficient for the proactive layer at brokerage scale?
- Execution layer process boundary: same FastAPI app, separate
  worker, or separate service?
- Action-proposal expiry defaults — uniform TTL, or per-action-family
  TTL?
- ORVN observability: which audit events surface to ORVN by default
  vs by request?
- Disaster recovery — RPO/RTO targets, audit-log replay, and how the
  execution layer is paused during recovery.

---

*End of v1.*
