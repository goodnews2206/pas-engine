# PAS Product Design Book

> Status: draft v1. Owner: ORVN Labs. Last updated: 2026-05-25.
> This document defines PAS as a product — its roles, modules, copy, and
> behaviour — *before* any frontend implementation. It is the source of
> truth that frontend, backend, and operations work back to. Any UI work
> must be reconciled against this book first.

---

## 0. How to read this book

This is a **product** document, not a UI document. It defines:

- what PAS is and is not,
- who uses it and what they can do,
- which modules exist and what each one is for,
- how PAS talks, listens, interrupts, and asks for approval,
- the words PAS uses when the data is missing, partial, or simulated,
- the order in which we build the surfaces.

Visual treatment, components, colour, typography, and motion are **out of
scope** here. Those are reconciled against `ui-ux-pro-max` (see §9) after
this book is approved.

---

## 1. Product thesis

### 1.1 What PAS is

PAS — *Performative AI SuperStaff* — is a real-time AI operating layer for
real estate brokerages. It sits across the brokerage's people, leads,
calls, callbacks, bookings, integrations, and tribal knowledge, and makes
the company:

- **queryable** — anyone with permission can ask the company a plain-English
  question and get an evidence-backed answer.
- **adaptive** — PAS learns the brokerage's tone, scripts, ideal customer,
  objection patterns, and rhythms over time. It does not arrive
  pre-baked.
- **operationally intelligent** — PAS notices what is about to fall through,
  proposes what to do about it, and either acts (within bounded, approved
  authority) or hands off to a human with the full context attached.

Every PAS surface produces structured decision-trace data. Nothing PAS
does is a black box.

### 1.2 What PAS is not

- **Not a chatbot.** Chatbots answer questions inside a bubble. PAS runs
  the company's operating surface and can pull up sections, render data,
  propose actions, and ask for approval.
- **Not a Slack bot.** Slack is the simplified surface where small,
  high-frequency interactions happen. The web app is the comprehensive
  surface where decisions get made with evidence in front of them.
- **Not a black-box autopilot.** PAS does not act without bounded,
  permissioned authority. Every action is explainable and, where possible,
  reversible.
- **Not a replacement for the agent.** PAS qualifies and routes; humans
  close.
- **Not a generic CRM.** PAS does not own the CRM data model. It reads
  from, writes to (when allowed), and reasons across CRM and adjacent
  systems.
- **Not an analytics dashboard.** Analytics describe the past. PAS
  proposes the next move.

### 1.3 Why the web app is the main operating surface

- Brokers, ops managers, and team leads run their day inside a browser.
  That is where evidence-backed decisions get made.
- The web surface supports richer affordances: tables, embedded
  conversations, side-by-side evidence, multi-pane review, audit
  trails, approval queues.
- It is the only surface where PAS can fully *show its work* before being
  trusted to act on the brokerage's behalf.
- It is persistent and shareable: a link is a workspace state, not a
  scrollback.

### 1.4 Why Slack is the simplified surface

- The team already lives there. Slack is where short, interrupt-driven
  moments happen ("approve this", "what's the next callback?").
- The needs-attention digest, evidence digest, and approval prompts fire
  in Slack because that is where the team can reply in seconds.
- Slack is **read-mostly + approve**. The web app is **read + act**.
- Slack must always be summarising the comprehensive surface, never
  replacing it.

### 1.5 The product promise

PAS turns a brokerage into a queryable, adaptive, operationally
intelligent business — without asking the broker to become a software
operator. Three rules govern every product decision:

1. **Extremely simple to use.** If a Team Lead needs a manual, we failed.
2. **Extremely functional.** If a critical decision takes more than two
   clicks from the Command Center, we failed.
3. **Extremely beautiful.** If the interface does not feel like premium
   software a broker would pay for, we failed.

---

## 2. Role-based workspace model

PAS workspaces have six built-in roles. A role is a **bundle of
defaults**: dashboard access, visible modules, default permission set,
approval authority, and notification posture. Each bundle can be
adjusted by a small set of named toggles — not by an enterprise RBAC
matrix.

### 2.1 Broker Owner / Super Admin

| Dimension | Definition |
|---|---|
| Dashboard access | Full — every module, every tenant view, every team. |
| Visible modules | All 20. |
| Default permissions | Configure brokerage, invite/remove users, manage integrations, manage billing, approve any action proposal, view every conversation, manage PAS Brain. |
| Removable permissions | None — Super Admin is by definition the floor. Individual notification toggles can be silenced. |
| Addable permissions | None — already at the ceiling. |
| Forbidden actions | Cannot remove their own Super Admin role while sole owner. Cannot delete the ORVN Internal Admin account on their tenant. Cannot bypass Critical-severity approval (still routed, but they sign it). |
| Approval authority | Top-level. Anything escalated lands here. |
| Notification defaults | FYI: off. Needs attention: 1× daily digest. Urgent: in-app + Slack push. Approval required: in-app + Slack. Critical: in-app + Slack + email + SMS. |
| Communication visibility | Every call, every agent conversation, every PAS in-app thread. |

### 2.2 Admin / Operations Manager

| Dimension | Definition |
|---|---|
| Dashboard access | Full except Billing and ORVN Admin Console. |
| Visible modules | All except Billing and ORVN Admin Console. |
| Default permissions | Configure agents, leads, callbacks, integrations, recommendations, action proposals; rotate API keys; manage PAS Brain entries. |
| Removable permissions | Action-proposal approval authority (can be downgraded to "request only"). Integrations write. |
| Addable permissions | Billing read-only. |
| Forbidden actions | Deleting the brokerage. Removing a Super Admin. Editing root integration credentials. Impersonation. |
| Approval authority | Approves most action proposals. Escalates anything that touches billing or that is flagged Critical. |
| Notification defaults | Same as Owner minus billing alerts. |
| Communication visibility | Every call by default; scopeable per team if requested. |

### 2.3 Team Lead / ISA Manager

| Dimension | Definition |
|---|---|
| Dashboard access | Scoped to their team(s). |
| Visible modules | Command Center, Leads, Calls, Callbacks, Bookings, Agents (their team), Pipeline Risks, Proactive Observer, Recommendations, Action Proposals (their team), Evidence Digest, In-App PAS, Notifications. |
| Default permissions | Assign leads, configure callback rules for their team, approve low- and medium-impact action proposals on their team, edit team-level scripts. |
| Removable permissions | Approval authority on action proposals (downgrade to "request only"). |
| Addable permissions | Scope expansion to additional teams. Limited Audit Log read for their team. |
| Forbidden actions | Integrations write, Billing, full Audit Log, ORVN Admin, cross-team views without explicit grant. |
| Approval authority | Medium-impact proposals within their team's scope. |
| Notification defaults | Urgent push, Needs attention digest, Critical push + email. |
| Communication visibility | Their team's calls and PAS conversations. |

### 2.4 Agent

| Dimension | Definition |
|---|---|
| Dashboard access | Their own work only. |
| Visible modules | Command Center (personal), Leads (assigned), Calls (own), Callbacks (own), Bookings (own), In-App PAS, Notifications. |
| Default permissions | Complete own bookings, log call notes, request callback reschedule, ask PAS for help. |
| Removable permissions | Ability to mark a lead as booked outside PAS (configurable per brokerage). |
| Addable permissions | Limited team-view (read) if promoted by a Team Lead. |
| Forbidden actions | Cross-agent visibility, integrations, billing, PAS Brain edits, ORVN admin. |
| Approval authority | None — only requests approvals. |
| Notification defaults | Own callbacks, own pipeline reminders, FYI throttled. |
| Communication visibility | Own calls only. |

### 2.5 Read-only Viewer

| Dimension | Definition |
|---|---|
| Dashboard access | Read-only across a configurable subset. |
| Visible modules | Default: Command Center, Calls, Bookings, Evidence Digest, Recommendations. Owner can widen. |
| Default permissions | Read-only. Every action button is disabled with a "read-only access" tooltip. |
| Removable permissions | Any module from view. |
| Addable permissions | More modules — but never write. |
| Forbidden actions | Anything that writes, sends, posts, or rotates. |
| Approval authority | None. |
| Notification defaults | Opt-in only; default off. |
| Communication visibility | Configurable; default summaries only. |

### 2.6 ORVN Internal Admin

| Dimension | Definition |
|---|---|
| Dashboard access | ORVN Admin Console + read access across every tenant for support. |
| Visible modules | Every module of every brokerage (read), plus ORVN Admin Console (write). |
| Default permissions | Brokerage onboarding, API key rotation, audited impersonation, PAS Brain corpus management, integration troubleshooting, incident response. |
| Removable permissions | Per-brokerage impersonation (revocable by a Super Admin from Advanced Settings — *future*). |
| Addable permissions | None — already a ceiling within ORVN scope. |
| Forbidden actions | Writing into a tenant's live conversation surface without Super Admin approval. Modifying tenant billing without consent. Triggering a live action on the tenant's behalf without a logged approval. |
| Approval authority | ORVN-internal incidents only. Cannot rubber-stamp tenant action proposals. |
| Notification defaults | ORVN ops channel — incidents, integrity-check failures, rate-limit anomalies, tenant SOS. |
| Communication visibility | All (read). Every impersonation event is audit-logged with reason. |

### 2.7 Cross-role rules

- **One owner minimum.** A brokerage workspace always has at least one
  Super Admin. The system refuses to remove the last one.
- **No silent privilege.** Any addable permission shows up in the user's
  profile as a named line item ("Approves action proposals"), not as a
  hidden capability.
- **ORVN cannot be granted by tenant.** Only ORVN's own admin console
  can mint that role.

---

## 3. Permission philosophy

PAS does not ship enterprise RBAC. The mental model for an admin is:

1. **Invite by email.**
2. **Pick a role.** (Defaults flow from the role bundle.)
3. **Adjust 3–6 toggles** if needed.

Toggles read like statements, not flags:

- "Can approve action proposals."
- "Receives Critical SMS at 2 a.m."
- "Can see other teams' calls."
- "Can edit PAS Brain entries."
- "Can write to integrations."

Rules:

- **Default-deny on anything that writes outside the workspace** (Slack
  outbound, CRM write, billing, integrations write).
- **Default-allow on read** within the role's scope.
- **Role downgrades cascade.** Demoting a Team Lead to Agent strips the
  add-ons; the user is told what they will lose before confirmation.
- **No permission matrices in the UI.** If the right control needs a
  spreadsheet to explain, redesign the control.

---

## 4. Core dashboard modules

Twenty modules. For each: purpose, role access, data shown, allowed
actions, forbidden actions, empty-state copy, warning-state copy,
demo/rehearsal label copy, future dependencies.

> **Empty-state copy** is what PAS says when the module is enabled but
> has nothing to show yet.
> **Warning-state copy** is what PAS says when the data is partial,
> stale, or evidence-thin.
> **Demo/rehearsal label** is what PAS pins to the surface when the
> evidence comes from simulation, not live operation.

### 4.1 Command Center

- **Purpose:** the single landing surface — what needs your attention,
  what PAS proposes, what just happened.
- **Role access:** all roles. Scope is filtered by role.
- **Data shown:** at-a-glance: open recommendations, pending approvals,
  today's callbacks, today's bookings, pipeline risks, presence.
- **Allowed actions:** open any card, approve from card, dismiss with
  reason, ask PAS to explain.
- **Forbidden:** none beyond role defaults.
- **Empty state:** "Nothing needs your attention right now. Ask PAS
  anything, or open a module from the sidebar."
- **Warning:** "Some sources are stale — last synced 3 hours ago.
  PAS is working with what it has."
- **Demo label:** "Rehearsal mode — these cards are simulated."
- **Future deps:** Proactive Observer, Recommendations, Action
  Proposals, Notifications.

### 4.2 Leads

- **Purpose:** every lead, where it came from, who owns it, where it is
  in the pipeline.
- **Role access:** Owner, Admin, Team Lead (scoped), Agent (assigned),
  Viewer (read).
- **Data shown:** lead list with source, status, last touchpoint, owner,
  qualification score, next action.
- **Allowed actions:** reassign (Team Lead+), edit, archive, request PAS
  research, request a callback be scheduled.
- **Forbidden:** deleting leads with active bookings.
- **Empty state:** "No leads yet. Connect a lead source from
  Integrations, or PAS can simulate one so you can see how this looks."
- **Warning:** "12 leads haven't been touched in over 7 days. PAS has
  drafted a recommendation."
- **Demo label:** "Simulated lead — not a real prospect."
- **Future deps:** Integrations (Zillow, Realtor.com, FB), Recommendations.

### 4.3 Calls

- **Purpose:** every call, with transcript, outcome, state-trace, and
  redacted recording where allowed.
- **Role access:** Owner, Admin, Team Lead (scoped), Agent (own), Viewer
  (configurable).
- **Data shown:** call list, per-call transcript, FSM trace, outcome,
  objections, sentiment, duration, evidence panel.
- **Allowed actions:** open transcript, mark for review, request a
  callback, ask PAS to summarise.
- **Forbidden:** editing transcripts; deleting calls (only ORVN can,
  with reason).
- **Empty state:** "No calls yet. Once Twilio is live or you run
  /simulate-call, calls will land here."
- **Warning:** "Recording redaction failed for 2 calls — flagged for
  review."
- **Demo label:** "Simulated call — no phone leg."
- **Future deps:** Twilio (live), Deepgram, ElevenLabs, PAS Brain.

### 4.4 Callbacks

- **Purpose:** every scheduled callback, owner, time, confirmation
  status, evidence of the original ask.
- **Role access:** Owner, Admin, Team Lead (scoped), Agent (own).
- **Data shown:** time, lead, owner, captured callback time, captured
  number, source call link, status.
- **Allowed actions:** reschedule (with reason), reassign, mark
  contacted, escalate.
- **Forbidden:** silent cancellation — every cancel needs a reason.
- **Empty state:** "No callbacks scheduled. PAS surfaces callback
  requests automatically when it hears them on a call."
- **Warning:** "A callback was promised but no time was captured.
  PAS will ask the lead on the next touch."
- **Demo label:** "Rehearsal callback — won't fire."
- **Future deps:** PAS128 capture flow (already shipped), Notifications.

### 4.5 Bookings

- **Purpose:** Cal.com-backed appointments, status, confirmation,
  reassignment.
- **Role access:** Owner, Admin, Team Lead (scoped), Agent (own).
- **Data shown:** booking time, lead, agent, channel, status, link.
- **Allowed actions:** reschedule, cancel with reason, reassign.
- **Forbidden:** silent overbook; double-book without confirmation.
- **Empty state:** "No bookings yet. Connect Cal.com and PAS will route
  qualified leads here."
- **Warning:** "Cal.com returned 404 for the demo event type — bookings
  for this brokerage are landing as not_booked. Fix in Integrations."
- **Demo label:** "Simulated booking — not on the agent's calendar."
- **Future deps:** Cal.com config, agent calendars.

### 4.6 Agents

- **Purpose:** roster, specialties, availability, performance, scoring
  weights.
- **Role access:** Owner, Admin, Team Lead (their team), Viewer.
- **Data shown:** agent, languages, areas, current load, last-active,
  booking conversion.
- **Allowed actions:** invite, deactivate, edit specialties, adjust
  routing weights.
- **Forbidden:** deleting agents with active bookings (must reassign first).
- **Empty state:** "No agents yet. Invite your first agent — PAS will
  start routing as soon as one is active."
- **Warning:** "2 agents have zero capacity set — they won't receive
  warm transfers."
- **Demo label:** "Demo agent — receives simulated leads only."
- **Future deps:** Calendars, presence.

### 4.7 Pipeline Risks

- **Purpose:** which deals/leads are at risk of stalling.
- **Role access:** Owner, Admin, Team Lead (scoped), Viewer.
- **Data shown:** at-risk leads, risk reason, last touch, suggested
  intervention.
- **Allowed actions:** assign a recovery action, dismiss with reason,
  ask PAS to propose.
- **Forbidden:** auto-acting on a risk flag without approval.
- **Empty state:** "No pipeline risks detected. PAS is watching."
- **Warning:** "PAS flagged 5 risks but evidence is thin (<3 touches).
  Treat as exploratory."
- **Demo label:** "Simulated risk — evidence from rehearsal."
- **Future deps:** Proactive Observer, PAS Brain.

### 4.8 Proactive Observer (PAS205)

- **Purpose:** read-only needs-attention surface — what PAS notices
  without acting.
- **Role access:** Owner, Admin, Team Lead.
- **Data shown:** observer signals, severity, evidence link, last seen.
- **Allowed actions:** acknowledge, ask PAS to explain, route to
  Recommendations.
- **Forbidden:** any live behaviour change — observer is, by
  construction, `live_behavior_changed=False`.
- **Empty state:** "Quiet hour — PAS isn't seeing anything that needs
  attention."
- **Warning:** "Observer ran with a stale snapshot (last sync 1h ago).
  Signals may be incomplete."
- **Demo label:** "Rehearsal signals — not from live calls."
- **Future deps:** Supabase snapshot adapter (PAS206).

### 4.9 Recommendations (PAS208)

- **Purpose:** operator-approved suggestions PAS would like to take.
- **Role access:** Owner, Admin, Team Lead (their team).
- **Data shown:** recommendation, evidence, who's affected, expected
  outcome, severity.
- **Allowed actions:** approve, decline (with reason), defer, ask PAS to
  explain.
- **Forbidden:** silent execution — every recommendation is operator-
  required by construction (`live_behavior_changed=False`).
- **Empty state:** "Nothing to recommend. PAS is observing."
- **Warning:** "3 recommendations are >24h old — consider declining or
  asking PAS to refresh evidence."
- **Demo label:** "Rehearsal recommendation — won't execute."
- **Future deps:** Action Proposals (PAS209), Evidence Digest.

### 4.10 Action Proposals (PAS209 — in flight)

- **Purpose:** bounded, named actions PAS proposes to take on approval.
- **Role access:** Owner, Admin, Team Lead (their team scope).
- **Data shown:** action, scope, side-effects, evidence, requested
  approver, expiry.
- **Allowed actions:** approve (PAS executes within bound), decline,
  modify scope, ask PAS to explain.
- **Forbidden:** approving an action outside the proposer's bound.
- **Empty state:** "No action proposals pending."
- **Warning:** "1 proposal expires in 15 minutes — approve, decline, or
  it will lapse."
- **Demo label:** "Rehearsal proposal — won't execute even if approved."
- **Future deps:** PAS210+, integration write paths.

### 4.11 Simulation Lab

- **Purpose:** run a call, a scenario, or a recommendation without any
  live side effects.
- **Role access:** Owner, Admin, Team Lead, ORVN Internal Admin.
- **Data shown:** scenario list, last run output, evidence artifacts.
- **Allowed actions:** run scenario, export evidence, share link.
- **Forbidden:** simulations that mutate live data.
- **Empty state:** "No simulations run yet. PAS includes pre-built
  rehearsal scripts to help you onboard."
- **Warning:** "This scenario references a brokerage that no longer
  exists — re-bind or archive."
- **Demo label:** *(always on — every artifact is labelled "rehearsal".)*
- **Future deps:** Cal.com sim, voice sim.

### 4.12 Evidence Digest (PAS201–PAS203)

- **Purpose:** the receipts. Why PAS said what it said.
- **Role access:** Owner, Admin, Team Lead, Viewer.
- **Data shown:** linked transcripts, snapshot rows, observer signals,
  reasoning chain.
- **Allowed actions:** open, share, export, ask PAS to expand.
- **Forbidden:** editing evidence — it's append-only.
- **Empty state:** "No digest yet — PAS will compile evidence the moment
  there's something to explain."
- **Warning:** "Digest references a call with redaction pending — some
  fields hidden."
- **Demo label:** "Rehearsal digest — evidence from simulation only."
- **Future deps:** Audit Logs.

### 4.13 PAS Brain

- **Purpose:** the brokerage's adaptive knowledge — scripts, ICP,
  objection patterns, tone, banned phrases, escalation rules.
- **Role access:** Owner, Admin (write), Team Lead (suggest), ORVN
  Internal Admin (corpus management).
- **Data shown:** entries grouped by domain, source, last-trained date,
  confidence.
- **Allowed actions:** add entry, edit entry, retire entry, request
  PAS to re-learn after change.
- **Forbidden:** silent corpus changes — every edit is audited.
- **Empty state:** "Nothing in the brain yet. PAS will learn from your
  calls — or you can teach it directly."
- **Warning:** "An entry conflicts with a higher-priority script.
  PAS will follow the higher-priority one until you resolve it."
- **Demo label:** "Demo entry — not used in live routing."
- **Future deps:** Self-training loop, Audit Logs.

### 4.14 Integrations

- **Purpose:** connect external systems, see what PAS can read and
  write, see health.
- **Role access:** Owner, Admin (write), Team Lead (read), ORVN
  Internal Admin (troubleshoot).
- **Data shown:** connected integrations, scopes, last sync, health,
  what PAS can now answer.
- **Allowed actions:** connect, configure scopes, revoke, test, view
  recent sync errors.
- **Forbidden:** granting write before the brokerage explicitly opts in.
- **Empty state:** "PAS isn't connected to anything yet. Connect a
  source and PAS can start answering."
- **Warning:** "Last sync failed (auth expired). Reconnect to keep PAS
  current."
- **Demo label:** "Sandbox connection — reads demo data only."
- **Future deps:** see §7.

### 4.15 In-App Communication

- **Purpose:** message PAS like an internal staff member. See §5.
- **Role access:** all roles.
- **Data shown:** ongoing threads, pinned answers, recent queries.
- **Allowed actions:** ask, follow up, pin, share answer, approve from
  thread.
- **Forbidden:** actions outside the user's role bundle.
- **Empty state:** "Ask PAS anything. Plain English. Typos are fine."
- **Warning:** "PAS doesn't have the data to answer this yet.
  Connect Integrations or check back when sync completes."
- **Demo label:** "Rehearsal answer — based on simulation data."
- **Future deps:** Notifications, Evidence Digest.

### 4.16 Notifications / Presence

- **Purpose:** the rhythm at which PAS interrupts.
- **Role access:** all roles, each user controls their own.
- **Data shown:** severity preferences, channel preferences, quiet hours,
  presence.
- **Allowed actions:** edit own settings, mute a topic, set quiet hours.
- **Forbidden:** silencing Critical-severity by a non-Owner.
- **Empty state:** "All clear. PAS will only interrupt when something
  truly needs you."
- **Warning:** "You've muted Approval-required — proposals will expire
  silently until you un-mute."
- **Demo label:** "Rehearsal notification — won't fire externally."
- **Future deps:** Mobile push, SMS, email, Slack.

### 4.17 Audit Logs

- **Purpose:** the receipts on PAS itself — who did what, what PAS did,
  what was approved, by whom, with what evidence.
- **Role access:** Owner, ORVN Internal Admin. Admin and Team Lead see
  scoped slices.
- **Data shown:** event, actor, target, before/after, evidence link,
  timestamp.
- **Allowed actions:** filter, export, link to evidence, flag for
  review.
- **Forbidden:** editing or deleting audit entries — append-only.
- **Empty state:** "No audit events in this window."
- **Warning:** "Audit ingestion lagged by ~30s — events may appear
  out-of-order briefly."
- **Demo label:** "Rehearsal log — not retained beyond session."
- **Future deps:** ORVN compliance surface.

### 4.18 Settings

- **Purpose:** workspace configuration — brokerage profile, hours, tone,
  disclosure, default scripts.
- **Role access:** Owner, Admin.
- **Data shown:** brokerage profile, operational config, members.
- **Allowed actions:** edit operational config, rotate API keys, invite
  members, change role bundles.
- **Forbidden:** disabling Critical-severity notifications globally;
  disabling audit logging.
- **Empty state:** *(unreachable — settings always have a default.)*
- **Warning:** "Operational config conflicts with PAS Brain — PAS
  follows the higher-priority script."
- **Demo label:** "Demo brokerage — changes won't persist after restart."
- **Future deps:** Billing, Integrations.

### 4.19 Billing

- **Purpose:** plan, usage, invoices, payment method.
- **Role access:** Owner only (default). Admin can be granted read.
- **Data shown:** plan, included usage, current usage, next invoice,
  payment method.
- **Allowed actions:** upgrade/downgrade, update payment method, view
  invoices.
- **Forbidden:** anyone non-Owner from writing without explicit grant.
- **Empty state:** "On the free demo plan. Connect billing when you're
  ready to go live."
- **Warning:** "Payment method expires this month."
- **Demo label:** "Demo plan — no charges."
- **Future deps:** Stripe (or equivalent).

### 4.20 ORVN Admin Console

- **Purpose:** internal-only — brokerage onboarding, support, incident
  response.
- **Role access:** ORVN Internal Admin only.
- **Data shown:** tenant list, integrity check status, recent
  incidents, key rotation status, impersonation events.
- **Allowed actions:** onboard, rotate keys, audited impersonation,
  trigger integrity checks, manage PAS Brain corpus (global).
- **Forbidden:** writing to a tenant's live surface without their
  Super Admin's approval (logged).
- **Empty state:** "No incidents. No pending onboardings."
- **Warning:** "Integrity check failed on 1 tenant — investigate before
  rotation window."
- **Demo label:** *(does not apply — this surface is internal-only.)*
- **Future deps:** ORVN ops dashboard.

---

## 5. In-app PAS communication layer

PAS is not a chat bubble. PAS is a staff member you can message from
anywhere in the workspace.

**Surfaces:**
- Persistent composer at the bottom of every dashboard page.
- Top-right peek pane that follows you across modules.
- Full-page conversation view when context is heavy.

**Behaviours:**
- **Accepts typos, fragments, messy phrasing.** "callbacks today?",
  "wht happened on the demo lead?", "did we book that 3pm".
- **Pulls up sections inline.** Asking about callbacks renders an
  embedded callback view inside the thread. Asking about a specific
  call inlines the transcript pane.
- **Explains data.** Every number has a "why" link to evidence.
- **Suggests next steps** as bounded action proposals (§4.10), not as
  imperatives.
- **Asks for approval** before any write. Approval is a single click
  with a reason field.
- **Acts only within role bundle.** If the user can't write to
  integrations, PAS will draft the action and route it to someone who
  can.

**Three non-negotiables on every action PAS takes:**

1. **Explainable.** PAS can show its reasoning, the evidence, and the
   policy.
2. **Queryable.** "Why did you do that?" returns a structured answer
   with links.
3. **Reversible where possible.** Reversible actions are flagged as
   such; irreversible ones require an explicit second confirmation.

PAS never claims certainty it does not have. If evidence is thin, PAS
says so before recommending.

---

## 6. Presence + notification philosophy

PAS feels like a trusted ops partner, not a CRM that pings.

**Channels (now and future):**
- In-app (live).
- Slack (live — needs-attention digest, approvals).
- Email (future).
- Mobile push (future).
- SMS-style (future — Critical only).
- WhatsApp / iMessage (future — exploratory).

**Severity levels:**

| Level | Meaning | Default channels | Reply behaviour |
|---|---|---|---|
| **FYI** | Something happened you might like to know. | In-app feed only, no push. | Reply optional; PAS treats as ack. |
| **Needs attention** | Someone should look at this in the next few hours. | In-app + Slack daily digest. | Reply in natural language; PAS routes the action. |
| **Urgent** | Should be addressed within the hour. | In-app push + Slack push. | Inline approve / decline / "ask PAS". |
| **Approval required** | PAS wants permission to act. | In-app push + Slack push. | One-click approve with reason. |
| **Critical** | Something is breaking or compliance is at risk. | All channels available, ignoring quiet hours. | Immediate ack required; escalates if unanswered. |

**Rules:**
- Quiet hours apply to FYI through Approval-required. Critical overrides.
- Users can reply naturally to any notification — Slack, email, in-app.
  PAS interprets and routes.
- No notification fires twice for the same event across channels unless
  Critical.
- A muted topic surfaces a weekly "you missed N" digest so silence is
  never invisible.

---

## 7. Integration philosophy

Integrations are PAS's senses. The connect flow is four steps:

1. **Connect** — OAuth or API key. One screen.
2. **Choose what PAS can read.** Named scopes, in plain English.
3. **Choose what PAS can write — later.** Write is always a second,
   explicit step. Defaults to off.
4. **See what PAS can now answer.** PAS lists the new questions it can
   answer the moment the connection lands.

Every integration card shows:
- **Status:** Healthy / Degraded / Disconnected.
- **Last sync:** absolute timestamp + relative.
- **Scopes:** what PAS reads, what PAS writes.
- **What PAS can answer now:** human-readable list.
- **Sync errors (last 24h):** with one-click reconnect.

**Future integration targets (priority order will be set per quarter):**

- **CRM** — generic adapter first, then Follow Up Boss, kvCORE, HubSpot.
- **Gmail / Google Workspace** — calendar, mail, drive.
- **Google Sheets / Drive** — for brokerages that run on spreadsheets.
- **Notion** — playbooks, scripts.
- **Asana** — task routing.
- **Slack** — already live for digest + approvals; expand to threads.
- **WhatsApp** — lead conversations.
- **iMessage** — exploratory.
- **Zapier / Make** — escape hatches for the long tail.
- **Lead sources** — Zillow, Realtor.com, Facebook lead ads.

---

## 8. Copy system

PAS copy is calm, human, precise, operational. No jargon. No fake
certainty. PAS reports to leadership; it does not perform.

### 8.1 Onboarding

- Welcome: "PAS is ready. Let's tell it about your brokerage."
- After invite: "You're in. PAS will start showing you what needs your
  attention as soon as it has data."
- After first call/sim: "First call captured. PAS is already learning
  your voice."

### 8.2 Empty states

- Module empty: "Nothing here yet. PAS will populate this as soon as
  there's something to show."
- Search empty: "PAS doesn't see anything that matches. Try a broader
  question, or check Integrations."
- Action queue empty: "All clear. PAS isn't proposing anything right now."

### 8.3 Warnings

- Stale data: "Last sync was {time} ago. PAS is working with what it
  has — answers may be incomplete."
- Thin evidence: "PAS has fewer than {n} signals on this — treat as
  exploratory."
- Conflicting source: "Two sources disagree on {field}. PAS is using
  {chosen} because {reason}."

### 8.4 Approvals

- Request: "PAS would like to {action}. Evidence: {link}. Approve?"
- Approved: "Done. Audit link: {link}."
- Declined: "Got it. PAS won't take this action. Want PAS to suggest
  alternatives?"
- Lapsed: "This proposal expired without a decision. PAS didn't act."

### 8.5 Demo / rehearsal labels

- Banner: "Rehearsal mode — nothing on this page reaches the outside
  world."
- Inline tag: "Simulated."
- Artifact footer: "Evidence from simulation. Not from a live call."

### 8.6 Standard PAS states

- **PAS has not acted yet:** "PAS is observing. Nothing has been done
  on your behalf."
- **Data not connected yet:** "PAS can't see this yet. Connect
  {integration} to give it access."
- **Needs human review:** "PAS isn't confident enough to act. Look
  here when you have a minute."
- **Approval required:** "PAS needs your sign-off before doing this."
- **Action completed:** "Done. Here's what changed and why."
- **Action blocked:** "PAS can't do this — {reason}. Here's what it
  would need to proceed."
- **Simulation-only evidence:** "This evidence comes from a rehearsal,
  not live operations. Treat as illustrative."

### 8.7 Voice rules

- Address the user, not the world. "You", not "the user".
- Past tense for what PAS did. Present tense for what PAS sees.
- Never apologise theatrically. State the situation, the cause, the
  next step.
- No exclamation marks. No emoji. No "great question!".
- Numbers and timestamps are always concrete (no "soon" / "a while ago").

---

## 9. UI/UX reference directive

Before any frontend implementation begins, inspect Daniel's forked
GitHub repo `ui-ux-pro-max`.

**Use it for:**
- layout quality (grid, spacing, hierarchy),
- component polish (form fields, tables, cards, modals),
- interaction patterns (loading, optimistic UI, error recovery),
- dashboard hierarchy (sidebar, top nav, command bar, overview),
- visual rhythm (whitespace, typography scale, density),
- mobile responsiveness (touch targets, breakpoints, off-canvas
  navigation).

**Do not copy blindly.** PAS has its own product semantics:
- evidence-first surfacing,
- bounded action proposals,
- severity-aware notifications,
- read/write split per integration,
- staff-member voice in copy.

Adapt patterns; do not import opinions that contradict this book.

**Deliverable from the UI study:** a short reconciliation note —
*"these patterns map to PAS, these need adjustment, these we discard"*
— before any component is built.

---

## 10. Future build sequence

In order. Each step lands before the next begins. Each step is a
separate branch and a separate review.

1. **Product Design Book** — *this document.* Owner: ORVN. Status:
   draft v1.
2. **UI/UX reference study** — read `ui-ux-pro-max`, produce
   reconciliation note.
3. **Web foundation** — framework, routing, auth shell, tenant
   awareness, design tokens. No business logic.
4. **Responsive dashboard shell** — sidebar, top nav, command bar,
   role-aware navigation skeleton. No real data yet.
5. **Role-based navigation** — wire role bundles into the navigation
   primitives.
6. **In-app PAS communication** — composer, peek pane, thread view.
   Connect to the existing simulate-call surface and PAS Brain reads.
7. **PAS205–PAS208 dashboard surfaces** — Proactive Observer,
   Recommendations, Evidence Digest, Action Proposals (read-only first).
8. **Integrations framework** — connect → read → write-later, health
   cards. Ship CRM-generic first.
9. **Presence / notifications** — severity routing, quiet hours,
   reply-to-PAS over in-app first, Slack second.
10. **Action approval flows** — wire PAS209 action proposals end-to-end
    behind explicit approval. `live_behavior_changed=False` invariant
    holds until this step explicitly relaxes it for a named, bounded
    action.

---

## 11. Open questions

These are flagged for the next iteration of this book. Not blockers for
review of v1.

- Single sign-on: Google-first, or wait for paying brokerages to demand
  it?
- Brokerage-of-brokerages (team-of-teams) workspaces — needed for
  franchise groups; how does the role bundle stack?
- Audit Log retention SLA — 90 days, 1 year, indefinite-with-cold-
  storage?
- Mobile: progressive web app first, or native shell at some point?
- ORVN-side "shadow" admin presence inside a tenant workspace — should
  the tenant see a presence indicator when ORVN is reading?
- How do we surface PAS-confidence in plain language without exposing
  raw probabilities the broker can't action?
- Billing model — per-seat, per-call, per-brokerage tier, or hybrid?

---

*End of v1.*
