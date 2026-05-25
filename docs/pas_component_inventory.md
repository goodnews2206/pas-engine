# PAS Component Inventory

> Status: draft v1. Owner: ORVN Labs. Last updated: 2026-05-25.
> Sibling to the Reference Study, Design System Definition, and
> Frontend Foundation Plan. Inventory of every likely component the
> PAS web app will need, with priority, complexity, mobile, role, and
> realtime considerations. **No frontend code yet.**

## 0. How this inventory is organised

Components are grouped by family. For each component we list:

- **Purpose** — one line on what it does.
- **Priority** — `P0` (must exist before any module ships), `P1`
  (needed for the v1 module set), `P2` (v1.x), `P3` (future).
- **Interaction complexity** — low / medium / high.
- **Mobile considerations** — what changes ≤767 px.
- **Role considerations** — what gating or treatment changes by
  role.
- **Future realtime considerations** — what realtime concerns
  apply when the v1 realtime layer lands.

The numbers are intentionally fewer than "every conceivable atom".
This is an opinionated list, not a Storybook taxonomy.

---

## 1. Navigation systems

### 1.1 Sidebar (desktop)

- **Purpose:** module list, role-shaped, with family headers.
- **Priority:** P0.
- **Interaction complexity:** low.
- **Mobile:** replaced by bottom tab bar + "More" sheet.
- **Role:** every role sees a different list — see Dashboard IA §3.
- **Realtime:** badge count on items with pending approvals or
  unread notifications.

### 1.2 Top bar

- **Purpose:** tenant + scope strip, command bar entry, presence,
  notifications bell, profile.
- **Priority:** P0.
- **Interaction complexity:** medium.
- **Mobile:** condensed — tenant + bell + profile only; search
  routes to composer.
- **Role:** ORVN sees a tenant switcher; others see static tenant.
- **Realtime:** presence indicator + bell badge count.

### 1.3 Command bar (Cmd/Ctrl+K)

- **Purpose:** global search, recents, PAS entry — unified.
- **Priority:** P0.
- **Interaction complexity:** medium.
- **Mobile:** opens as a full-screen sheet.
- **Role:** results are scoped to what the role can reach.
- **Realtime:** not required for v1.

### 1.4 Bottom tab bar (mobile)

- **Purpose:** primary nav at ≤767 px.
- **Priority:** P1.
- **Interaction complexity:** low.
- **Mobile:** the default mobile nav surface.
- **Role:** items per Dashboard IA §9.1.
- **Realtime:** badge count per item.

### 1.5 "More" sheet (mobile)

- **Purpose:** full module list off-canvas on mobile.
- **Priority:** P1.
- **Interaction complexity:** low.
- **Mobile:** primary surface; swipe / drag to close.
- **Role:** same shape as desktop sidebar, scoped.
- **Realtime:** badge mirroring.

---

## 2. Command Center widgets

### 2.1 "Needs your attention" card

- **Purpose:** ordered list of items waiting on the viewing user.
- **Priority:** P0.
- **Interaction complexity:** low.
- **Mobile:** stacks; each row remains tappable.
- **Role:** scope filtered.
- **Realtime:** new items animate in via `anim-fast`.

### 2.2 "PAS proposes" card

- **Purpose:** pending recommendations + action proposals.
- **Priority:** P0.
- **Interaction complexity:** medium (inline approve / decline /
  ask PAS).
- **Mobile:** drawer opens full-screen on approve.
- **Role:** invisible to Agent + Viewer.
- **Realtime:** expiry countdown ticks live.

### 2.3 "Today" card

- **Purpose:** today's bookings + callbacks.
- **Priority:** P0.
- **Interaction complexity:** low.
- **Mobile:** stacks.
- **Role:** scope filtered (Agent = own; Team Lead = team).
- **Realtime:** new bookings / callbacks animate in.

### 2.4 "Recently" card

- **Purpose:** ambient awareness — last completed calls / bookings
  / approvals.
- **Priority:** P1.
- **Interaction complexity:** low.
- **Mobile:** collapsed by default.
- **Role:** scope filtered.
- **Realtime:** append on event.

### 2.5 "Ask PAS" prompt

- **Purpose:** invitation to open the composer with example
  queries.
- **Priority:** P0.
- **Interaction complexity:** low.
- **Mobile:** anchored above the tab bar.
- **Role:** every role; examples are role-aware.
- **Realtime:** not required.

---

## 3. Proactive Observer cards

### 3.1 Observer signal card

- **Purpose:** a single observer signal with severity, evidence,
  and "ack / route to recommendation" actions.
- **Priority:** P1.
- **Interaction complexity:** medium.
- **Mobile:** drawer for ack actions.
- **Role:** Owner / Admin / Team Lead only.
- **Realtime:** new signals animate in; stale ones gray-out after
  a window.

### 3.2 Observer empty state

- **Purpose:** the quiet state — "Quiet hour, PAS isn't seeing
  anything that needs attention."
- **Priority:** P1.
- **Interaction complexity:** low.
- **Mobile:** centered block.
- **Role:** same copy across roles.
- **Realtime:** transitions to active state on first signal.

---

## 4. Recommendation cards

### 4.1 Recommendation card

- **Purpose:** PAS208 surface — operator-approved suggestion.
- **Priority:** P0.
- **Interaction complexity:** medium (approve / decline / defer /
  ask PAS).
- **Mobile:** approve opens full-screen drawer.
- **Role:** Owner / Admin / Team Lead.
- **Realtime:** age indicator ("3h old"); expiry countdown.

### 4.2 Recommendation receipt (post-decision)

- **Purpose:** post-decision summary card — "Approved by X at
  14:02" / "Declined: reason".
- **Priority:** P1.
- **Interaction complexity:** low.
- **Mobile:** stacks.
- **Role:** Owner / Admin / Team Lead.
- **Realtime:** transitions from "pending" to "decided" inline.

---

## 5. Approval surfaces

### 5.1 Approval drawer

- **Purpose:** the canonical approval surface — evidence, scope,
  side-effects, approve / decline / ask PAS.
- **Priority:** P0.
- **Interaction complexity:** high.
- **Mobile:** full-screen.
- **Role:** approver bundle only; non-approvers see "request
  approval from <role>".
- **Realtime:** expiry countdown + lapse transition.

### 5.2 Inline approve affordance

- **Purpose:** approve from a card without opening the drawer.
- **Priority:** P0.
- **Interaction complexity:** low.
- **Mobile:** primary action button on the card.
- **Role:** approver bundle only.
- **Realtime:** state transitions on submit.

### 5.3 Slack approval prompt (out-of-app)

- **Purpose:** approval message in Slack — one click + reason.
- **Priority:** P1 (Slack already lives).
- **Interaction complexity:** low.
- **Mobile:** Slack handles it.
- **Role:** approver bundle only.
- **Realtime:** state synced via PAS API.

---

## 6. Timeline / event surfaces

### 6.1 Audit timeline

- **Purpose:** chronological list of audit events — actor, action,
  evidence link.
- **Priority:** P1.
- **Interaction complexity:** medium (filter, deep link, expand).
- **Mobile:** vertical stack; filters in a sheet.
- **Role:** Owner full; Admin scoped; Team Lead scoped; ORVN
  cross-tenant.
- **Realtime:** optional live-tail toggle (default off).

### 6.2 Call timeline

- **Purpose:** FSM state trace + transcript turns + events for a
  single call.
- **Priority:** P0.
- **Interaction complexity:** medium.
- **Mobile:** vertical; transcript in own scroll.
- **Role:** Owner / Admin / Team Lead (scoped) / Agent (own) /
  Viewer (configurable).
- **Realtime:** only for active calls (v1.x).

### 6.3 Notification lifecycle timeline

- **Purpose:** per-notification: detected → queued → delivered →
  acknowledged → resolved → archived.
- **Priority:** P2.
- **Interaction complexity:** low.
- **Mobile:** vertical.
- **Role:** Owner + ORVN.
- **Realtime:** state transitions stream in.

---

## 7. Lead surfaces

### 7.1 Lead card

- **Purpose:** lead row in the Leads list and embedded inline
  inside PAS threads.
- **Priority:** P0.
- **Interaction complexity:** low (inspector on click).
- **Mobile:** stacks; tap opens inspector.
- **Role:** scope filtered.
- **Realtime:** status changes animate in.

### 7.2 Lead inspector

- **Purpose:** full lead detail — source, history, calls, bookings,
  PAS suggestions.
- **Priority:** P0.
- **Interaction complexity:** medium.
- **Mobile:** full-screen.
- **Role:** scope filtered.
- **Realtime:** status badge updates.

### 7.3 Lead-source provenance chip

- **Purpose:** small chip indicating the originating source
  (Zillow / Realtor / FB / CRM / manual).
- **Priority:** P1.
- **Interaction complexity:** low.
- **Mobile:** preserved.
- **Role:** every role that can see leads.
- **Realtime:** not required.

---

## 8. Conversation panes

### 8.1 Call transcript pane

- **Purpose:** turn-by-turn transcript with state-trace overlay.
- **Priority:** P0.
- **Interaction complexity:** medium (search, jump-to-state).
- **Mobile:** full-screen; collapsible state overlay.
- **Role:** Owner / Admin / Team Lead (scoped) / Agent (own) /
  Viewer (configurable, redacted by default).
- **Realtime:** live transcript for active calls (v1.x).

### 8.2 PAS thread (peek pane embed)

- **Purpose:** PAS conversation in 360-px peek.
- **Priority:** P0.
- **Interaction complexity:** medium.
- **Mobile:** opens as full-screen sheet.
- **Role:** every role.
- **Realtime:** streaming responses; presence indicator.

### 8.3 PAS thread (full route)

- **Purpose:** dedicated route for a single PAS conversation.
- **Priority:** P1.
- **Interaction complexity:** medium.
- **Mobile:** standard full-screen route.
- **Role:** every role; share is scoped.
- **Realtime:** same as peek.

---

## 9. PAS chat surfaces

### 9.1 PAS composer (persistent)

- **Purpose:** the bottom-of-page input that lets a user message
  PAS from anywhere.
- **Priority:** P0.
- **Interaction complexity:** high (single instance, multi-mode,
  expands, streams).
- **Mobile:** pinned above tab bar; expands over module.
- **Role:** every role; PAS replies are scoped to the role bundle.
- **Realtime:** streaming, presence, cancel.

### 9.2 Inline section embed

- **Purpose:** PAS pulls a module section ("today's callbacks")
  inside a thread, rendered with the real module's spec.
- **Priority:** P0.
- **Interaction complexity:** high (reuses module components inside
  a thread).
- **Mobile:** stacks; same as the real module.
- **Role:** the embed obeys the role's scope.
- **Realtime:** if the section has live data, it streams the same
  way it would on its own route.

### 9.3 PAS suggestion chip

- **Purpose:** small inline suggestion ("Ask: 'What stalled this
  week?'").
- **Priority:** P1.
- **Interaction complexity:** low.
- **Mobile:** preserved.
- **Role:** every role; suggestions are role-aware.
- **Realtime:** not required.

---

## 10. Notification surfaces

### 10.1 Notification bell + badge

- **Purpose:** top-bar indicator with unread count.
- **Priority:** P0.
- **Interaction complexity:** low.
- **Mobile:** preserved.
- **Role:** every role.
- **Realtime:** new arrivals bump the badge.

### 10.2 Notification drawer

- **Purpose:** right-side drawer, severity-grouped, with
  reply-driven actions inline.
- **Priority:** P0.
- **Interaction complexity:** medium.
- **Mobile:** full-screen.
- **Role:** every role; content scoped.
- **Realtime:** items stream in; lifecycle states transition live.

### 10.3 Toast

- **Purpose:** Urgent + Approval Required surface; rare.
- **Priority:** P1.
- **Interaction complexity:** low.
- **Mobile:** anchored bottom-above-tab-bar.
- **Role:** every role.
- **Realtime:** appears on event; dismiss / auto-dismiss.

### 10.4 Persistent banner (Critical)

- **Purpose:** top-of-module banner for Critical state (auth
  expired, integrity check failed, outage).
- **Priority:** P0.
- **Interaction complexity:** low.
- **Mobile:** preserved; sticky.
- **Role:** every role that touches the affected module.
- **Realtime:** appears on Critical event; clears on resolve.

### 10.5 "While you were away" digest

- **Purpose:** single end-of-quiet-hours summary of what fell into
  the window.
- **Priority:** P1.
- **Interaction complexity:** low.
- **Mobile:** sheet.
- **Role:** every role.
- **Realtime:** computed on quiet-hours exit.

---

## 11. Integration health cards

### 11.1 Connector card

- **Purpose:** one card per connector — name, status, last sync,
  scopes, "what PAS can answer now".
- **Priority:** P0.
- **Interaction complexity:** medium (connect / disconnect /
  reauth / scope edit).
- **Mobile:** stacks; actions in sheets.
- **Role:** Owner / Admin (write); Team Lead (read); ORVN
  (troubleshoot).
- **Realtime:** health transitions stream in.

### 11.2 Connect flow

- **Purpose:** four-step connect: connect → read scopes → write
  scopes (later) → "what PAS can now answer".
- **Priority:** P0.
- **Interaction complexity:** high.
- **Mobile:** full-screen wizard.
- **Role:** Owner / Admin.
- **Realtime:** not required.

### 11.3 Last-sync detail

- **Purpose:** drill-down on the most recent sync — duration,
  errors, items synced.
- **Priority:** P1.
- **Interaction complexity:** low.
- **Mobile:** preserved.
- **Role:** Admin + ORVN.
- **Realtime:** updates during the next sync.

---

## 12. Agent workload surfaces

### 12.1 Agent capacity card

- **Purpose:** current load, queue, off-shift indicator.
- **Priority:** P1.
- **Interaction complexity:** low.
- **Mobile:** preserved.
- **Role:** Owner / Admin / Team Lead (their team).
- **Realtime:** load + presence update live.

### 12.2 Agent routing weights editor

- **Purpose:** tune specialty / area / language weights.
- **Priority:** P1.
- **Interaction complexity:** medium.
- **Mobile:** sheet.
- **Role:** Owner / Admin.
- **Realtime:** not required.

### 12.3 Agent best-fit preview

- **Purpose:** show the next routing decision PAS would make for a
  hypothetical lead.
- **Priority:** P2.
- **Interaction complexity:** medium.
- **Mobile:** sheet.
- **Role:** Owner / Admin.
- **Realtime:** not required.

---

## 13. Mobile cards (cross-module)

### 13.1 Mobile module-card baseline

- **Purpose:** a uniform card spec that every module reuses on
  mobile — title, secondary line, severity chip, primary action.
- **Priority:** P1.
- **Interaction complexity:** low.
- **Mobile:** *is* the mobile spec.
- **Role:** every role; content scoped.
- **Realtime:** as per the underlying module.

### 13.2 Pull-to-refresh

- **Purpose:** refresh server state on mobile lists.
- **Priority:** P2.
- **Interaction complexity:** low.
- **Mobile:** mobile-only affordance.
- **Role:** every role.
- **Realtime:** falls back to manual refresh when realtime is
  degraded.

---

## 14. Data tables

### 14.1 Data table

- **Purpose:** the canonical sortable, filterable, selectable
  table.
- **Priority:** P0.
- **Interaction complexity:** high.
- **Mobile:** converts to a stacked card list.
- **Role:** scope filtered.
- **Realtime:** optional; rows stream in for live feeds.

### 14.2 Filter chip rail

- **Purpose:** named filters above the table; URL-syncable.
- **Priority:** P0.
- **Interaction complexity:** medium.
- **Mobile:** sheet.
- **Role:** every role.
- **Realtime:** not required.

### 14.3 Bulk action bar

- **Purpose:** appears above the table when ≥1 row is selected.
- **Priority:** P1.
- **Interaction complexity:** medium.
- **Mobile:** sticky bottom-of-list.
- **Role:** scope filtered.
- **Realtime:** not required.

### 14.4 Column manager

- **Purpose:** show / hide / reorder visible columns.
- **Priority:** P2.
- **Interaction complexity:** medium.
- **Mobile:** sheet.
- **Role:** every role that can read the table.
- **Realtime:** not required.

---

## 15. Audit viewers

### 15.1 Audit log row

- **Purpose:** single audit entry — actor, action, target,
  evidence link.
- **Priority:** P1.
- **Interaction complexity:** low.
- **Mobile:** stacks.
- **Role:** Owner / Admin (scoped) / ORVN.
- **Realtime:** live-tail toggle.

### 15.2 Audit event detail

- **Purpose:** before / after diff for state-changing events.
- **Priority:** P1.
- **Interaction complexity:** medium.
- **Mobile:** full-screen.
- **Role:** same as 15.1.
- **Realtime:** static.

### 15.3 Audit export

- **Purpose:** export filtered range to CSV / JSON.
- **Priority:** P2.
- **Interaction complexity:** low.
- **Mobile:** initiates email-on-completion.
- **Role:** Owner + ORVN.
- **Realtime:** not required.

---

## 16. Filters and search

### 16.1 Global search (command bar)

- **Purpose:** search across modules from Cmd/Ctrl+K.
- **Priority:** P0.
- **Interaction complexity:** medium.
- **Mobile:** full-screen.
- **Role:** scope filtered.
- **Realtime:** not required.

### 16.2 Module search

- **Purpose:** in-module search input.
- **Priority:** P1.
- **Interaction complexity:** low.
- **Mobile:** anchored at the top of the module.
- **Role:** scope filtered.
- **Realtime:** debounced; no realtime.

### 16.3 Filter group editor

- **Purpose:** complex filter builder (rarely used; for power
  surfaces like Audit Logs and Calls).
- **Priority:** P2.
- **Interaction complexity:** high.
- **Mobile:** sheet.
- **Role:** scope filtered.
- **Realtime:** not required.

---

## 17. Severity chips

### 17.1 Severity chip

- **Purpose:** small pill labelling FYI / Needs / Urgent / Approval
  / Critical, with icon + colour + label.
- **Priority:** P0.
- **Interaction complexity:** low.
- **Mobile:** preserved.
- **Role:** every role.
- **Realtime:** not required.

### 17.2 Severity dot (compact)

- **Purpose:** colour + icon-only signal in dense rows.
- **Priority:** P1.
- **Interaction complexity:** low.
- **Mobile:** preserved.
- **Role:** every role.
- **Realtime:** not required.

---

## 18. Badges

### 18.1 Role badge

- **Purpose:** indicates a user's role next to their name.
- **Priority:** P0.
- **Interaction complexity:** low.
- **Mobile:** preserved.
- **Role:** every role; treatment differs per role token.
- **Realtime:** not required.

### 18.2 Status badge

- **Purpose:** lead status, booking status, connector status, etc.
- **Priority:** P0.
- **Interaction complexity:** low.
- **Mobile:** preserved.
- **Role:** every role.
- **Realtime:** updates live.

### 18.3 Demo / rehearsal pill

- **Purpose:** "Simulated" inline label.
- **Priority:** P0.
- **Interaction complexity:** low.
- **Mobile:** preserved.
- **Role:** every role; cannot be hidden by theme.
- **Realtime:** not required.

### 18.4 Scope badge

- **Purpose:** indicates a non-default scope view (e.g. "team:
  East").
- **Priority:** P1.
- **Interaction complexity:** low.
- **Mobile:** preserved.
- **Role:** Team Lead + ORVN primarily.
- **Realtime:** not required.

---

## 19. Empty states

### 19.1 Empty state (canonical)

- **Purpose:** the standard centered empty block.
- **Priority:** P0.
- **Interaction complexity:** low.
- **Mobile:** centered.
- **Role:** every role.
- **Realtime:** transitions to populated state on first event.

### 19.2 "Read-only" empty state

- **Purpose:** explains to a Read-only Viewer why a module shows
  nothing they can touch.
- **Priority:** P1.
- **Interaction complexity:** low.
- **Mobile:** centered.
- **Role:** Viewer.
- **Realtime:** not required.

---

## 20. Loaders

### 20.1 Skeleton

- **Purpose:** known-shape placeholder while content loads.
- **Priority:** P0.
- **Interaction complexity:** low.
- **Mobile:** preserved.
- **Role:** every role.
- **Realtime:** transitions out when content arrives.

### 20.2 "PAS is thinking" pill

- **Purpose:** PAS-presence indicator while a response composes.
- **Priority:** P0.
- **Interaction complexity:** low.
- **Mobile:** preserved.
- **Role:** every role.
- **Realtime:** required.

### 20.3 Calm progress indicator

- **Purpose:** unknown-shape responses; e.g. audit export.
- **Priority:** P1.
- **Interaction complexity:** low.
- **Mobile:** preserved.
- **Role:** every role.
- **Realtime:** not required.

---

## 21. Modals

### 21.1 Confirmation modal

- **Purpose:** explicit commit for irreversible destructive
  actions.
- **Priority:** P0.
- **Interaction complexity:** medium.
- **Mobile:** centered, full-width within the viewport.
- **Role:** restricted by the underlying action.
- **Realtime:** not required.

### 21.2 Sign-in / sign-out flow modals

- **Purpose:** auth entry / exit confirmation.
- **Priority:** P0.
- **Interaction complexity:** low.
- **Mobile:** full-screen.
- **Role:** every role.
- **Realtime:** not required.

---

## 22. Drawers

### 22.1 Peek pane

- **Purpose:** right-side panel for active PAS thread.
- **Priority:** P0.
- **Interaction complexity:** medium.
- **Mobile:** full-screen.
- **Role:** every role.
- **Realtime:** streams.

### 22.2 Inspector

- **Purpose:** right-side panel for a row's full detail.
- **Priority:** P0.
- **Interaction complexity:** medium.
- **Mobile:** full-screen.
- **Role:** scope filtered.
- **Realtime:** updates if the underlying record changes.

### 22.3 Approval drawer

- **Purpose:** stacked-above approval surface.
- **Priority:** P0.
- **Interaction complexity:** high.
- **Mobile:** full-screen.
- **Role:** approver bundle only.
- **Realtime:** expiry countdown + state transition.

### 22.4 Mobile sheet (generic)

- **Purpose:** bottom-up sheet for actions, filters, "More" nav.
- **Priority:** P1.
- **Interaction complexity:** low.
- **Mobile:** mobile-primary affordance.
- **Role:** every role.
- **Realtime:** not required.

---

## 23. Inspectors (record detail)

Same as 22.2 conceptually; listed separately because the inspector
contract is reused by Leads / Calls / Callbacks / Bookings / Agents /
Audit / PAS Brain.

- **Priority:** P0 per module.
- **Interaction complexity:** medium.
- **Mobile:** full-screen.
- **Role:** scope filtered per module.
- **Realtime:** record-level updates.

---

## 24. Onboarding flows

### 24.1 First-run onboarding

- **Purpose:** welcome, tenant setup, first invite, first integration
  prompt.
- **Priority:** P1.
- **Interaction complexity:** medium.
- **Mobile:** full-screen wizard.
- **Role:** Owner only.
- **Realtime:** not required.

### 24.2 User-invite onboarding

- **Purpose:** flow shown to a newly invited user — accept invite,
  set notification defaults, meet PAS.
- **Priority:** P1.
- **Interaction complexity:** medium.
- **Mobile:** full-screen.
- **Role:** every invited role; copy differs per role.
- **Realtime:** not required.

### 24.3 First-integration onboarding

- **Purpose:** the connect-flow surface for the first integration a
  brokerage attaches.
- **Priority:** P1.
- **Interaction complexity:** medium.
- **Mobile:** full-screen wizard.
- **Role:** Owner / Admin.
- **Realtime:** not required.

### 24.4 PAS Brain seed onboarding

- **Purpose:** prompt to seed scripts / objection language / tone.
- **Priority:** P2.
- **Interaction complexity:** medium.
- **Mobile:** full-screen.
- **Role:** Owner / Admin.
- **Realtime:** not required.

---

## 25. Priority roll-up

A quick tally of P0 components (must exist before any module ships):

- Sidebar, Top bar, Command bar, "Needs your attention" card,
  "PAS proposes" card, "Today" card, "Ask PAS" prompt,
  Recommendation card, Approval drawer, Inline approve, Call
  transcript pane, PAS thread (peek), PAS composer, Inline section
  embed, Notification bell, Notification drawer, Persistent banner
  (Critical), Connector card, Connect flow, Data table, Filter chip
  rail, Severity chip, Role badge, Status badge, Demo / rehearsal
  pill, Empty state, Skeleton, "PAS is thinking" pill, Confirmation
  modal, Sign-in / sign-out modal, Peek pane, Inspector, Lead card,
  Lead inspector.

**Total P0: ~33 components.** Every other module-specific record
view reuses these primitives.

---

## 26. Component-inventory invariants

The inventory is correct only if every one of these holds:

1. Every P0 component appears at least once in the v1
   implementation sequence (Frontend Foundation Plan §14).
2. No component carries business logic the API does not enforce.
3. Every component declares its mobile behaviour (no "desktop-
   only" P0s).
4. Severity, role, and demo treatment are uniform across every
   component family.
5. Streaming and realtime concerns are explicit per component;
   nothing is implicitly "live".
6. Empty / loading / error / success states exist for every P0
   component.
7. Every component obeys the pre-delivery checklist (Design System
   §29).
8. The composer + peek + full-thread surfaces share a single PAS
   thread service instance.
9. The approval drawer stacks above peek and inspector — by spec,
   not by accident.
10. No component renders raw tokens, raw integration secrets, or
    raw internal IDs.

---

## 27. Open inventory questions

- **Inline section embed mechanism** — does the embed import the
  real module component, or a thinner "embed mode" of it? Decision
  has implications for code reuse.
- **Approval-on-mobile UX** — full-screen drawer is the current
  call; should it instead be a stacked card flow with explicit
  forward/back?
- **Bulk approvals** — out-of-scope for v1 (one-at-a-time only)?
- **"PAS is thinking" granularity** — single global indicator vs
  per-thread vs per-section?
- **Inspector vs full route for heavy records** — call records can
  be very long; do we always inspect, or sometimes route?
- **Skeletons fidelity** — exact-shape skeletons (more work, more
  craft) vs simple bars (faster ship, lower polish)?
- **Severity dot vs severity chip** thresholds — at what density
  does a chip become a dot?
- **Density toggle scope** — whole product, or per-module
  preference?

---

*End of v1.*
