# PAS Notification Architecture

> Status: draft v1. Owner: ORVN Labs. Last updated: 2026-05-25.
> Sibling to `docs/pas_product_design_book.md` (notification copy,
> tone, severity philosophy) and `docs/pas_system_architecture.md`
> (operating sequence, audit layer). This document defines *how* PAS
> interrupts: presence, severity, channels, lifecycle, anti-spam.

## 0. Scope and cross-cutting rules

The rules from `pas_system_architecture.md` §0 apply. The ones that
matter most for notifications:

- **No fake certainty.** A notification says what PAS knows and what
  it doesn't.
- **No hidden automation.** Every notification is traceable to a
  rule, an event, or a proposal.
- **PAS speaks like operations staff reporting to leadership.** Calm,
  precise, operational. No marketing voice, no exclamation marks, no
  emoji.
- **Demo / rehearsal labels** propagate into notifications — a
  notification triggered by a simulated event is tagged in-line.
- **Role-based permissions** govern who is even eligible to receive
  each notification family.

---

## 1. The PAS Presence Layer

Presence is the ambient signal that PAS is alive, observing, and
honest about its state.

### 1.1 What the Presence Layer surfaces

| Signal | What it means | Where it appears |
|---|---|---|
| **PAS is observing** | The proactive layer is running over current snapshot data. | Top bar status, Command Center subtitle. |
| **PAS is thinking** | PAS is composing a response or evidence pull in your composer thread. | Composer + peek pane indicator. |
| **PAS is waiting on you** | An approval or input is required from this user. | Top bar bell badge, Command Center "Needs your attention". |
| **PAS is degraded** | An integration is offline / a sync failed / observer is on stale data. | Persistent banner on affected modules. |
| **PAS is in rehearsal mode** | The active brokerage is in demo / simulation mode. | Persistent banner site-wide. |

### 1.2 Presence rules

- Presence is **never invented**. If PAS does not know whether it has
  fresh data, the Presence Layer says "degraded" until verified —
  not "observing".
- Presence is **always honest**. "PAS is thinking" is shown for the
  full duration of the underlying work, including waits on external
  systems.
- Presence has its own copy library — see §7.

### 1.3 User presence

User presence (online / idle / away) is **deferred to v1.x**. It is
not part of the v1 surface. When it ships, it follows the same rules
as PAS's presence: honest, never silently wrong.

---

## 2. Severity model

PAS uses exactly five severity levels. Adding a sixth requires
revisiting this document.

### 2.1 The five levels

| Level | Definition | Examples |
|---|---|---|
| **FYI** | Something happened you might like to know. Not actionable today. | "Daily call volume normal." "PAS Brain learned a new objection phrasing." |
| **Needs attention** | Should be reviewed within the next few hours by someone. | "3 leads stalled this week." "Recommendation: re-engage the 'tour requested' cohort." |
| **Urgent** | Should be addressed within the hour by a named role. | "Pending approval expires in 45 minutes." "5 callbacks promised, 0 captured." |
| **Approval required** | PAS has drafted an action and is waiting on a human sign-off. | "PAS would like to send a re-engagement email to 7 leads." "PAS would like to reassign 2 callbacks." |
| **Critical** | Something is breaking, exposing data, or about to violate compliance. | "Cal.com auth expired — bookings failing." "Integrity check failed for brokerage X." "Suspicious API key activity." |

### 2.2 Severity rules

- **Severity is set by the producer, not the user.** A user can mute
  a *topic*, not downgrade a severity.
- **Critical cannot be globally silenced** by a non-Owner role.
- **Approval required has a TTL.** No approval lives forever; expiry
  is part of the producer contract.
- **Severity can be escalated** if the original level is not
  acknowledged in the escalation window (see §4).
- **Severity is never inferred from volume.** A flood of FYI does not
  become Urgent automatically.

---

## 3. Channel routing

Five channels in v1 (in-app + Slack live; email/SMS/push surfaces
defined but built later). Two more on the roadmap (WhatsApp /
iMessage).

### 3.1 Default routing matrix

| Severity | In-app | Slack | Email | SMS-style | Push |
|---|---|---|---|---|---|
| FYI | feed only (no badge) | weekly digest | off | off | off |
| Needs attention | feed + badge | daily digest | off (opt-in) | off | off |
| Urgent | feed + badge + toast | DM + thread | optional | off | optional |
| Approval required | feed + badge + drawer | DM + thread | optional | off | optional |
| Critical | feed + badge + persistent banner | DM + channel | always | always (Owner only by default) | always |

### 3.2 Channel rules

- **Defaults are role-aware.** Owner gets Critical SMS by default;
  Admin / Team Lead get Critical SMS only if opted in.
- **No notification fires twice on the same channel for the same
  event.** Dedup key is `(event_id, channel, recipient)`.
- **A single event may fan out across channels** only when Critical.
  Other severities pick one primary channel per recipient.
- **Slack is the simplified surface** — Slack notifications are
  summaries linking back to the web app for full evidence and
  multi-step actions.
- **Future channels (WhatsApp / iMessage)** follow the same matrix
  shape; they are *additional* delivery surfaces, never the only
  surface for any severity.

### 3.3 Channel selection algorithm (per recipient, per event)

1. Resolve the recipient's role bundle and channel preferences.
2. Intersect with the event's severity routing.
3. Apply quiet hours (see §4).
4. Apply dedup (see §6).
5. Deliver on the resulting set of channels.

The algorithm is deterministic and replayable from the audit log.

---

## 4. Quiet hours and escalation

### 4.1 Quiet hours

- **Per-user.** Each user sets their own quiet window in Notification
  Settings. Defaults: 22:00–07:00 local.
- **Severity-aware.** Quiet hours apply to FYI, Needs attention,
  Urgent, and Approval required. **Critical overrides quiet hours.**
- **Replays on exit.** Notifications that fell into a quiet window
  arrive as a single "while you were away" digest the moment the
  window ends — not as a scroll of individual pings.
- **No global override** by a non-Owner role.

### 4.2 Escalation

| Severity | Escalation rule |
|---|---|
| FYI | No escalation. |
| Needs attention | If unacknowledged for 24h, batched into the next daily digest. No bump. |
| Urgent | If unacknowledged for 30 minutes, route to the secondary responder per role bundle. |
| Approval required | If unacknowledged before the proposal's TTL expires, mark the proposal "expired without decision" and emit an FYI to the requester. |
| Critical | If unacknowledged for 5 minutes, fan out to Owner + Admin via every available channel, ignoring quiet hours. |

- **Escalation never auto-takes an action.** It only re-routes the
  notification.
- **Escalation events are themselves audit-logged.** A late-night
  Critical fanout to the Owner is recoverable from the audit log,
  including which channels fired and which responders acked.

---

## 5. Reply-driven workflow

Notifications are not read-only. The user can reply to any of them in
plain English, and PAS routes the reply into the same intent layer
that powers the composer.

### 5.1 Reply surfaces

- **In-app:** click the notification → drawer with reply field.
- **Slack:** reply in the same thread; PAS reads it.
- **Email / SMS:** reply directly; PAS parses on inbound (subject to
  brokerage tenancy verification by message ID + signed token, not
  raw From address).
- **Push:** quick-action buttons for the canonical answers
  (approve / decline / "ask PAS"); long-text reply falls through to
  in-app.

### 5.2 Reply intents PAS recognises

| Reply pattern | PAS interpretation |
|---|---|
| "approve" / "yes" / "ok" / "go" | Approve the proposal in the thread. |
| "decline" / "no" / "not now" + optional reason | Decline. PAS captures the reason. |
| "later" / "in 1h" / "tomorrow" | Defer with explicit TTL. |
| "why?" / "evidence" / "what's the data" | Drop a structured evidence digest into the reply. |
| "who else?" / "show me others" | List related items in scope. |
| Free-form question | Route into the composer intent layer. |

### 5.3 Reply rules

- **Replies cannot exceed the user's role bundle.** A Read-only
  Viewer replying "approve" gets back "PAS can't act on that for you —
  here's who can."
- **Replies are audited** with the source channel and parsed intent.
- **Replies on rehearsal events** carry the demo label into PAS's
  own response.

---

## 6. Anti-spam rules

PAS interrupts rarely. Three families of guard:

### 6.1 Dedup

- **Same event, same channel, same recipient** — fires once. Re-firing
  requires a new event ID.
- **Acked events do not re-fire** to the same recipient unless their
  state changes (e.g. a deferred Urgent escalates to Critical).

### 6.2 Throttle

- **FYI:** at most one digest per topic per day per recipient.
- **Needs attention:** at most one daily digest per recipient,
  consolidating all topics.
- **Urgent:** no flood guard at severity-level, but per-topic guard
  caps at one Urgent per topic per 30 minutes per recipient.
- **Approval required:** one per proposal. No fan-out per attempt.
- **Critical:** no throttle. The system trusts the producer.

### 6.3 Batch

- **End-of-quiet-hours digest** (see §4.1).
- **Daily digest** (Needs attention).
- **Weekly digest** (FYI roll-up).
- **Per-module rollup** when a single module has more than 10 unread
  notifications in a 60-minute window — PAS condenses them into a
  single "X items in <module> need review" notification with a deep
  link.

---

## 7. Notification copy rules

PAS notifications follow Product Design Book §8 voice. A few extra
constraints unique to notifications:

### 7.1 Structure

Every notification has four lines, max:

1. **What** (one sentence).
2. **Why** (one sentence, evidence-anchored).
3. **What PAS suggests** (one sentence, optional).
4. **Action** (single button + "ask PAS" affordance).

If the situation requires more than four lines, link to the full
record in the web app — do not stretch the notification.

### 7.2 Concrete copy patterns

- **FYI:** "PAS Brain learned 'we'd love a quick chat' as a soft
  callback request. No action needed."
- **Needs attention:** "3 leads from your Tuesday cohort haven't been
  touched in 5 days. PAS drafted a re-engagement recommendation —
  open in Command Center."
- **Urgent:** "An approval expires in 30 minutes. Sign off, decline,
  or it will lapse with no action taken."
- **Approval required:** "PAS would like to reassign 2 callbacks
  from Agent A to Agent B because A is off-shift. Evidence: 2
  promised callbacks within A's off-window. Approve / decline / ask
  PAS."
- **Critical:** "Cal.com auth expired at 14:02 UTC. New bookings are
  failing. Reconnect from Integrations."

### 7.3 Forbidden patterns

- No exclamation marks. No emoji. No "Heads up!" / "Hey!" openers.
- No raw IDs, raw tokens, raw secrets, or raw internal hostnames.
- No "PAS detected an opportunity!" framing — PAS reports, not sells.
- No fake certainty: "may" / "appears to" / "based on N signals" are
  preferred to "is" / "definitely" when the data is thin.
- No relative-only timestamps. Always pair "2 hours ago" with an
  absolute time on hover or in the body.

---

## 8. Notification lifecycle

Every notification walks a fixed lifecycle. The audit layer captures
each transition.

### 8.1 The six states

```
   detected → queued → delivered → acknowledged → resolved → archived
                                    ↑                ↓
                                    └── re-opened ──┘
```

| State | Meaning | Producer |
|---|---|---|
| **detected** | A rule, event, or proposal generated a notification candidate. | Originating layer (proactive, recommendation path, integration health). |
| **queued** | The candidate passed dedup + throttle + quiet-hours filtering and is pending channel delivery. | Notification service. |
| **delivered** | The notification was sent on at least one channel. | Notification service. |
| **acknowledged** | The recipient saw it (read receipt) or interacted (replied / clicked). | Recipient interaction. |
| **resolved** | The underlying situation no longer applies (proposal approved/declined, integration reconnected, lead touched). | Domain layer. |
| **archived** | Removed from active surfaces; still readable in Audit Logs. | Notification service (after retention window). |

### 8.2 Lifecycle rules

- **Every state transition is an audit event.** The audit layer can
  reconstruct any notification's full history.
- **A delivered notification cannot be un-delivered.** A correction
  is a *new* notification with explicit linkage to the original.
- **Re-opening** is allowed when a resolved situation recurs — the
  new instance is a fresh notification with a `related_to` link, not
  a resurrection of the old one.
- **Archival window** defaults to 90 days in active surfaces;
  indefinite in audit logs (subject to the open question in Product
  Design Book §11).

---

## 9. Integration of notifications with other layers

### 9.1 With the proactive layer

- Observer signals can produce Needs-attention notifications (only).
- Observer signals cannot produce Critical notifications. Critical
  requires explicit integration-health or compliance signal.

### 9.2 With the recommendation / approval path

- Every recommendation produces an Approval-required notification
  when first composed.
- The notification's TTL matches the proposal's TTL.
- Approval / decline / lapse transitions the notification through
  acknowledged → resolved.

### 9.3 With integrations

- Integration health transitions (Healthy → Degraded → Disconnected)
  produce Critical notifications when crossing into Disconnected,
  and Needs-attention when crossing into Degraded.
- Reconnect resolves the notification automatically (it is an
  observed state change, not a manual ack).

### 9.4 With the audit layer

- Every notification — produced, throttled, deduped, delivered,
  acked, escalated, resolved, archived — emits a `pas_events` entry
  with the original payload's redaction policy preserved.

---

## 10. Notification architecture invariants (checklist)

The system is correct only if every one of these holds:

1. Severity is set by the producer and cannot be silently downgraded
   by the user.
2. Critical overrides quiet hours and cannot be globally silenced by
   a non-Owner.
3. No dedup-violating duplicate ever reaches the same recipient on
   the same channel.
4. Every notification carries an explicit lifecycle and emits an
   audit event on every transition.
5. Replies are routed through the same intent layer as the composer,
   bounded by the role's permissions.
6. Demo / rehearsal evidence is labelled inside the notification
   body, not only in the surface that produced it.
7. No notification exposes secrets, tokens, or internal IDs.
8. Escalation never auto-acts — it only re-routes.
9. The notification service rejects any payload missing severity,
   audience role, or originating event ID.
10. PAS never claims certainty it does not have inside a notification.

---

## 11. Open notification questions

Tracked for v2. None are blockers for v1.

- **Per-team channel routing** — should Team Leads be able to set a
  team-default channel preference that members inherit?
- **Notification "summary mode"** for users who want a single end-of-
  day digest of everything except Critical — opt-in tier.
- **Delivery analytics** — surfaced to whom? Owner only, or also
  Admin?
- **Slack DM vs Slack channel** — when does a notification go to
  the user's DM versus a brokerage operations channel?
- **Notification sounds** on push — opinionated default, or per-
  severity customisable?
- **Cross-tenant notifications** for ORVN — what's the right
  ergonomics for an ORVN admin watching N tenants?

---

*End of v1.*
