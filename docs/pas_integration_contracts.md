# PAS Integration Contracts

> Status: draft v1. Owner: ORVN Labs. Last updated: 2026-05-25.
> Sibling to `docs/pas_product_design_book.md` (§7 — integration
> philosophy, future targets) and `docs/pas_system_architecture.md`
> (§8 — integration layer responsibilities and boundaries). This
> document defines the *contract* every connector implements:
> permissions, lifecycle, health, source-of-truth rules. No frontend
> implementation.

## 0. Scope and cross-cutting rules

The cross-cutting rules from `pas_system_architecture.md` §0 apply.
Integration-specific reinforcements:

- **No raw internal tokens in user-facing UI.** Connection details
  visible to the brokerage are: "Connected as <human-readable
  account>", scopes, health, last sync. Tokens and refresh secrets
  stay below the API surface.
- **No hidden automation.** A connector that has not been explicitly
  granted write authority cannot write. Period.
- **No fake certainty.** A degraded connector causes the layers above
  to label evidence "stale" — not to substitute plausible defaults.
- **PAS speaks like operations staff reporting to leadership** when
  it discusses an integration ("Last sync failed because the token
  expired — reconnect to keep PAS current").

---

## 1. Integration philosophy

A connector is a *sense organ*. It lets PAS perceive the brokerage's
external systems and, when explicitly invited, act on them. Two
principles govern every connector:

### 1.1 Read first, write later — always

- **Connecting** an integration grants PAS read access, scoped to
  named domains the user explicitly selects.
- **Writing** is a second, explicit opt-in step, per-integration,
  with its own named scopes.
- **Approval-required gating** sits on top of write — even an
  integration with write enabled does not perform a write without an
  operator approval (see Notification Architecture §9.2).

### 1.2 Health is part of the contract

Every connector must surface:
- **Status** — Healthy / Degraded / Disconnected.
- **Last sync** — absolute UTC timestamp and a relative phrasing.
- **Scopes read** — human-readable list.
- **Scopes write** — human-readable list, with default = empty.
- **What PAS can answer now** — derived from the granted scopes.
- **Last 24h errors** — counts + the most recent failure reason.

These six fields are non-negotiable. A connector that cannot expose
them cannot ship.

---

## 2. Read permissions

### 2.1 Scope model

A connector exposes its capabilities as **named scopes**, in plain
English. Examples (illustrative; final names per connector):

- "Read contacts and lead activity."
- "Read calendars and meeting details."
- "Read inbox metadata (subjects, senders, timestamps)."
- "Read message bodies for the past 30 days."
- "Read Drive files in the 'PAS Brain' folder."

### 2.2 Read rules

- **Default-deny.** No scope is auto-granted on connect; the user
  picks each one.
- **Named, not numbered.** OAuth scope strings are translated to
  human-readable labels; the user never sees `mail.readonly`.
- **Reversible.** Revoking a scope takes effect within the next
  sync cycle. The Audit Log records the revocation.
- **Scope drift is logged.** If the upstream system changes its scope
  semantics, the connector flags a "scopes need review" notification
  rather than silently absorbing the change.

### 2.3 What "read" actually means

- The connector ingests data from the upstream on a defined cadence
  (sync window per connector family).
- Ingested data is stored in a per-tenant cache, redacted per the
  integration's data-class policy (PII, secrets, financial — see
  §6).
- Layers above never query the upstream directly. They query the
  cache through the PAS API.

---

## 3. Write permissions

Write is the second class of capability. Granting write is a
**deliberate, named, two-step act**.

### 3.1 Write rules

- **Off by default**, even after read scopes are granted.
- **Granted per named write action**, not per integration as a whole.
  Examples: "Send re-engagement emails to opted-in leads."
  "Reschedule callbacks in the calendar." "Update lead status on
  confirmed booking."
- **Bounded by scope.** Each write action has explicit limits
  (volume per day, audience filter, allowed time windows).
- **Always pairs with an operator approval gate.** Even an
  authorised write action runs through Action Proposals — the
  permission unlocks the *capability*, the approval triggers the
  *execution*.
- **Reversible-where-possible.** Each write action declares its
  reversal path or carries an "irreversible" flag that forces a
  second confirmation at execution time.

### 3.2 Write action lifecycle

```
   capability granted → proposal composed → operator approval →
   bounded execution → audit emitted → reversal available (where
   declared)
```

This is the same lifecycle that governs `live_behavior_changed=True`
in the System Architecture doc — only the scope of *that single
action call* flips the gate.

---

## 4. Health status

A connector's runtime state.

### 4.1 The three states

| State | Definition | UI treatment |
|---|---|---|
| **Healthy** | Recent successful sync within the connector's freshness window; no auth issues; error rate below threshold. | Green dot, "Healthy". |
| **Degraded** | At least one of: stale sync (past freshness window), elevated error rate, partial scope failure. Still partially usable. | Amber dot, "Degraded — [specific reason]". |
| **Disconnected** | Auth invalid, refresh failed, manual revocation, or upstream unavailable for > grace window. | Red dot, "Disconnected — reconnect to restore". |

### 4.2 Health rules

- **State transitions emit notifications** (Notification Architecture
  §9.3): Healthy → Degraded = Needs attention; Degraded →
  Disconnected = Critical; reconnect = auto-resolve.
- **Degraded does not silently substitute defaults.** Layers above
  receive a freshness flag and surface stale labels.
- **Disconnected does not block reads from the cache.** The cache
  serves until its own retention window expires; everything is
  labelled stale.
- **Auto-recovery on reconnect.** The next successful sync resets the
  state without manual intervention.

### 4.3 Freshness windows

Each connector family declares a freshness window — the maximum
acceptable age for sync data before "Degraded — stale" kicks in.
Defaults (illustrative):

| Family | Freshness window |
|---|---|
| CRM | 15 minutes |
| Calendar (Google) | 5 minutes |
| Inbox (Gmail) | 10 minutes |
| Sheets / Drive | 30 minutes |
| Notion / Asana | 30 minutes |
| Slack | 1 minute (real-time) |
| Lead sources (Zillow / Realtor / FB) | 5 minutes |
| WhatsApp / iMessage | 1 minute (real-time) |

Per-brokerage overrides require Owner approval and are recorded.

---

## 5. Connector lifecycle

Every connector walks the same five-state lifecycle.

### 5.1 The five states

```
   not connected → connected (read-only) → write-enabled (with approval)
                                            ↓
                                         degraded
                                            ↓
                                       disconnected
```

| State | Meaning | What PAS can do |
|---|---|---|
| **not connected** | No credential exists. | Nothing. PAS surfaces "Connect <integration> to enable …". |
| **connected (read-only)** | Credentials valid; read scopes granted; write off. | Read. Compose recommendations based on what it reads. |
| **write-enabled (with approval)** | At least one write capability granted; each execution still requires operator approval. | Read + propose + execute approved actions within bound. |
| **degraded** | Reachable but partial (stale, scope drift, elevated errors). | Reads from cache with stale label; writes paused until reconciled. |
| **disconnected** | Auth invalid or upstream unavailable. | Reads only from cache; writes blocked. |

### 5.2 Transition rules

- **not connected → connected (read-only):** OAuth or API key
  exchange; scope selection screen; first successful sync.
- **connected (read-only) → write-enabled:** explicit opt-in by an
  authorised role (Owner / Admin); per-action grants only.
- **any → degraded:** triggered by health monitors (freshness
  window, error rate, scope drift, partial auth).
- **any → disconnected:** triggered by auth failure that the
  connector cannot recover within the grace window, or by explicit
  revocation.
- **degraded → previous-state:** automatic on successful sync.
- **disconnected → connected (read-only):** explicit reconnect flow.
  Write scopes are not silently restored — they require re-affirmation
  if the disconnect was due to a credential change.

### 5.3 Tenant-isolation rules at the connector level

- Credentials are stored per tenant, never shared across tenants.
- A connector serving brokerage A cannot read into brokerage B even
  if both brokerages connect the same upstream account.
- ORVN Internal Admin can troubleshoot any tenant connector but
  cannot extract its credentials.

---

## 6. Source-of-truth rules

When PAS reads the same record from multiple integrations, who wins?

### 6.1 The default ladder

For lead / contact data:

1. **CRM** (Follow Up Boss, kvCORE, HubSpot, etc.) — authoritative
   for ownership, stage, and lifecycle.
2. **Lead source platform** (Zillow / Realtor / Facebook) —
   authoritative for the original lead payload.
3. **Inbox** (Gmail) — authoritative for the last contact timestamp
   and the subject thread.
4. **Sheets / Drive** — read-only mirror; never authoritative.
5. **Slack / Notion / Asana** — operational state, not record state.

For calendar / booking data:

1. **Calendar** (Google) — authoritative for booked-vs-free.
2. **Cal.com** — authoritative for what PAS scheduled.
3. **CRM** — secondary mirror, never overrides #1 or #2.

### 6.2 Conflict-resolution rules

- **PAS shows the conflict, not a guess.** A surfaced record displays
  the winning source and a "2 sources disagree on <field>" affordance.
- **Per-field overrides are configurable.** A brokerage can declare,
  for a named field family, that source X wins. Recorded in Settings;
  audit-logged.
- **PAS does not silently merge.** Merging requires an operator
  decision per record (or per rule).
- **Write-back follows the same ladder.** A write that PAS would
  perform lands in the authoritative system first; mirrors update on
  their own sync cycle.

---

## 7. Data-class redaction policy

Every connector declares which fields are PII, financial, secret, or
public. The layers above honour these classes when:

- emitting `pas_events` payloads (PII redacted from logs),
- rendering on Slack (lead PII reduced to display name + masked
  phone),
- sharing surfaces (Read-only Viewer sees redacted views of
  sensitive fields by default),
- showing in notifications (no raw secrets, no tokens, no internal
  IDs).

A connector that does not declare its data classes cannot ship.

---

## 8. Future connector families

The set declared in Product Design Book §7, with brief contract
notes. None of these is built in v1 of the architecture; their
contracts are pre-defined so that when they ship, they conform.

### 8.1 CRM

- **Generic adapter first.** A neutral CRM contract that downstream
  connectors map into. Avoids tight-coupling to any one CRM.
- **Targets (priority order set per quarter):** Follow Up Boss,
  kvCORE, HubSpot, then long tail via Zapier escape hatch.
- **Default read scopes:** contacts, lead activity, stages.
- **Default write scopes:** none. Common opt-ins: status update on
  confirmed booking; note attachment after a call.

### 8.2 Gmail / Google Workspace

- **Scope split:** inbox metadata vs message body; calendar vs
  drive; per scope opt-in.
- **Default write scopes:** none. Common opt-ins: send re-engagement
  email to opted-in leads; create calendar event.
- **PII handling:** email body access is gated on explicit scope
  grant; never enabled by default.

### 8.3 Google Sheets / Drive

- **Read-only mirror semantics** by default. Sheets-driven
  brokerages will exist; PAS reads, never authoritative.
- **Write scopes:** confined to PAS-managed sheets (e.g. a PAS
  Brain export sheet). Never writes into a brokerage's master
  sheet without scoped, named permission.

### 8.4 Slack

- **Live in v1.** Already shipping the simplified surface (digests,
  approvals).
- **Read scopes:** thread context for replies routed back into PAS;
  message metadata only.
- **Write scopes:** posting digests and approval prompts. No DMs to
  leads. No outbound posting to unrelated channels.

### 8.5 Notion

- **Read scopes:** playbooks, scripts, scheduling rules.
- **Write scopes:** off by default. Common opt-in: append a
  PAS-generated playbook draft for human review.

### 8.6 Asana

- **Read scopes:** task assignments, statuses, due dates.
- **Write scopes:** off by default. Common opt-in: create a task
  from a PAS recommendation.

### 8.7 WhatsApp

- **Read scopes:** lead conversation messages (per opt-in template
  flow).
- **Write scopes:** off by default. Common opt-in: send pre-approved
  templated outreach. Free-form replies route through Action
  Proposals.
- **Compliance gate.** Region-specific consent flows; cannot ship
  without a per-region compliance check.

### 8.8 iMessage

- **Exploratory.** Apple Business Messaging or a third-party bridge;
  contract identical in shape to WhatsApp.

### 8.9 Zapier / Make

- **Escape hatch for the long tail.** A trigger/action surface that
  exposes PAS events outbound and PAS API inbound.
- **Permission model:** treat the Zap user as a tenant user; same
  role bundle applies.

### 8.10 Lead sources (Zillow / Realtor.com / Facebook lead ads)

- **Inbound-only by family default.** PAS receives leads; PAS does
  not post to lead boards.
- **Source-of-truth role:** lead origin payload (§6).
- **Health rules:** lead-source feed staleness is treated as Critical
  (a stalled feed means leads are missed).

---

## 9. Connector contract checklist

A connector ships only when every one of these holds:

1. Exposes the six required health fields (§1.2).
2. Declares its scopes in human-readable English; never shows raw
   OAuth scope strings on user-facing UI.
3. Declares its data classes (§7) and honours them across emit paths.
4. Defaults write to off; opt-in is per-named-action, not per
   integration.
5. Walks the five-state lifecycle (§5) and emits health-transition
   notifications.
6. Declares its freshness window (§4.3).
7. Stores credentials per tenant; ORVN cannot extract them.
8. Surfaces stale labels on degraded reads; never silently
   substitutes defaults.
9. Respects source-of-truth ladder (§6); does not silently merge.
10. Emits a `pas_events` entry on every state transition and every
    write attempt (success or failure).

---

## 10. Open integration questions

Tracked for v2. None are blockers for v1.

- **Backfill semantics.** When a connector is granted a wider read
  scope, do we backfill historically or sync forward only?
- **Multi-account-per-tenant.** Some brokerages will connect more
  than one CRM (legacy + new). How are records reconciled?
- **PII residency.** Some upstream data is region-constrained; how
  does the PAS cache honour that without breaking the read API
  contract?
- **Rate-limit fairness.** When a connector's upstream rate-limits,
  do tenants share the limit or hold separate budgets?
- **Webhook vs poll.** Real-time channels (Slack, WhatsApp) prefer
  webhooks; others prefer poll. What's the minimum viable poll cadence
  per family before we declare a connector "real-time"?
- **Revocation symmetry.** When a brokerage revokes write scopes,
  do already-approved proposals execute or pause?

---

*End of v1.*
