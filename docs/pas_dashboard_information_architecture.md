# PAS Dashboard Information Architecture

> Status: draft v1. Owner: ORVN Labs. Last updated: 2026-05-25.
> Sibling to `docs/pas_product_design_book.md` (modules, roles, copy)
> and `docs/pas_system_architecture.md` (layers, operating sequence).
> This document defines *where things live* on the dashboard — global
> navigation, role-shaped surfaces, persistence vs context, and the
> mobile counterpart. No frontend implementation.

## 0. Scope and cross-cutting rules

The same rules from `pas_system_architecture.md` §0 apply here. Three
get special emphasis for IA:

- **Extreme simplicity.** No more than five primary navigation areas
  visible to any single role at any time.
- **No raw internal tokens in user-facing UI.** Identifiers visible to
  users are human-readable labels; internal IDs stay behind copy
  affordances ("Copy ID" reveals a scoped ID, not an integration
  secret).
- **PAS speaks like operations staff reporting to leadership.** This
  governs which surfaces are persistent (PAS is always present) vs
  contextual (PAS shows up when invoked).

---

## 1. Global navigation

PAS has four persistent navigation primitives plus three contextual
ones. Every surface is built out of these.

### 1.1 The four persistent primitives

| Primitive | Position | Purpose |
|---|---|---|
| **Sidebar** | Left, collapsible | The module list, role-shaped. |
| **Top bar** | Top, full width | Search, command bar, presence, notifications bell, profile menu. |
| **PAS composer** | Bottom, full width, dockable | The in-app PAS communication entry point (Product Design Book §5). |
| **Tenant context strip** | Below top bar (ORVN admin only) | "Viewing brokerage: …" with explicit exit. |

These are present on every page. They never disappear in v1 — no
"focus mode" hides them. PAS is always reachable.

### 1.2 The three contextual primitives

| Primitive | When it appears | Purpose |
|---|---|---|
| **Peek pane** | When PAS is mid-thread | A right-side panel that follows you across modules. |
| **Module inspector** | When a row is opened | A slide-over with the full record (call transcript, lead history, etc.). |
| **Approval drawer** | When an approval is pending | A modal-style drawer with evidence + approve/decline/explain. |

These appear over the persistent navigation, never *under* it. They
do not require a route change.

### 1.3 What is persistent vs contextual

- **Persistent:** the four primitives above; the active tenant; the
  user's identity; PAS's presence ("PAS is observing" /
  "PAS is thinking"); the notifications bell with unread count.
- **Contextual:** the current module's content; the peek pane (only
  when an active PAS thread exists); the module inspector (only when
  a row is open); the approval drawer (only when something is pending
  the current user's signoff).

---

## 2. Module hierarchy

The 20 modules from Product Design Book §4 group into five families.
The sidebar renders the families as collapsible sections, with each
role only seeing the modules they have access to.

### 2.1 The five families

| Family | Modules | Rationale |
|---|---|---|
| **Operate** | Command Center · Leads · Calls · Callbacks · Bookings | The day-to-day work surface. Open by default. |
| **Notice** | Proactive Observer · Recommendations · Action Proposals · Pipeline Risks · Evidence Digest | The PAS-noticed surface. Open by default for Owner/Admin/Team Lead. |
| **People** | Agents · In-App Communication · Notifications | Who's here and how PAS talks to them. |
| **System** | Integrations · PAS Brain · Audit Logs · Settings · Billing · Simulation Lab | The configuration / receipts surface. Collapsed by default. |
| **ORVN** | ORVN Admin Console | Internal-only. Only visible if role = ORVN Internal Admin. |

### 2.2 Display rules

- Families with zero visible modules for a role are hidden entirely —
  no empty headers.
- The Command Center is the first item in the first visible family
  for every role. It is the default landing surface after sign-in.
- Modules a role does **not** have access to are never rendered in
  the sidebar — not greyed out, not "locked", just absent. Read-only
  Viewer is the one exception: items they can read but not write are
  rendered normally, with action buttons disabled at the row level.

---

## 3. Role-based navigation

The sidebar is composed from the role's module set (Product Design
Book §2). Defaults below; each is adjustable via named toggles in
Settings.

### 3.1 Broker Owner / Super Admin

- **Operate:** all five.
- **Notice:** all five.
- **People:** all three.
- **System:** all six.
- **ORVN:** absent.
- **Landing:** Command Center, owner scope (everything).

### 3.2 Admin / Operations Manager

- **Operate:** all five.
- **Notice:** all five.
- **People:** all three.
- **System:** Integrations · PAS Brain · Audit Logs · Settings ·
  Simulation Lab. *Billing absent by default; can be granted read.*
- **ORVN:** absent.
- **Landing:** Command Center, admin scope (everything except billing
  alerts).

### 3.3 Team Lead / ISA Manager

- **Operate:** Command Center · Leads · Calls · Callbacks · Bookings,
  all scoped to their team.
- **Notice:** Proactive Observer · Recommendations · Action Proposals
  · Pipeline Risks · Evidence Digest, all team-scoped.
- **People:** Agents (their team) · In-App Communication ·
  Notifications.
- **System:** Simulation Lab only (read).
- **ORVN:** absent.
- **Landing:** Command Center, team scope.

### 3.4 Agent

- **Operate:** Command Center (personal) · Leads (assigned) · Calls
  (own) · Callbacks (own) · Bookings (own).
- **Notice:** *absent by default.* (Optional read-only Recommendations
  if the brokerage opts to share them.)
- **People:** In-App Communication · Notifications.
- **System:** absent.
- **ORVN:** absent.
- **Landing:** Command Center, agent scope (their own work).

### 3.5 Read-only Viewer

- **Operate:** Command Center · Calls · Bookings (read).
- **Notice:** Evidence Digest · Recommendations (read).
- **People:** In-App Communication (read, query-only) ·
  Notifications (opt-in).
- **System:** absent.
- **ORVN:** absent.
- **Landing:** Command Center, viewer scope (configurable).

### 3.6 ORVN Internal Admin

- **Operate:** all five (read across every tenant).
- **Notice:** all five (read across every tenant).
- **People:** all three (read).
- **System:** Integrations · PAS Brain · Audit Logs · Simulation Lab
  (read + ORVN-side write).
- **ORVN:** ORVN Admin Console (write).
- **Landing:** ORVN Admin Console.

### 3.7 Scope strip

When the active scope differs from the role's default scope (e.g. a
Team Lead viewing their team, or an ORVN admin viewing a tenant), a
**tenant/scope context strip** sits below the top bar:

> "Viewing brokerage: <name> · scope: <team> · [exit scope]"

Never silent. Never sticky beyond the session.

---

## 4. The Command Center

The single landing surface. Defines what every role sees first.

### 4.1 Layout sections (top to bottom)

1. **Needs your attention** — a small, ordered list of items currently
   waiting on the viewing user, by severity.
2. **PAS proposes** — pending Recommendations + Action Proposals the
   viewing user can approve / decline.
3. **Today** — today's bookings, today's callbacks (own scope first,
   then team if Team Lead+).
4. **Recently** — the last handful of completed calls / bookings /
   approvals, for ambient awareness.
5. **Ask PAS** — a prominent prompt that drops the user into the
   composer with example queries.

### 4.2 Card rules

- Every card has an evidence link ("Why this?").
- Every actionable card has at most two primary actions and one
  "ask PAS to explain".
- Demo / rehearsal cards are pinned with the demo label (Design
  Book §8.5).
- Cards with stale data carry the stale warning copy from §8.3.

### 4.3 What the Command Center is not

- It is not a dump of metrics. KPI tiles go inside their respective
  modules (Pipeline Risks, Agents, Calls).
- It is not configurable per-user beyond severity filtering — the
  shape is the same for everyone in the same role.

---

## 5. Where PAS communication lives

PAS is reachable from three places, in increasing depth:

| Surface | Trigger | What it shows |
|---|---|---|
| **Composer** (persistent, bottom) | Cmd/Ctrl + K or click | One-line input + last 3 replies. |
| **Peek pane** (contextual, right) | Auto-opens on active thread | Multi-turn thread with inline section embeds. |
| **Full thread page** | "Expand" from peek | Full conversation, pinned answers, evidence trail. |

Rules:

- Composer is **always visible** on every dashboard page.
- Peek pane only opens when there is an active thread; closing it
  pauses, never deletes, the thread.
- Full thread page is its own route, shareable inside the workspace
  (with role-permission redaction on shared view).
- Replying in Slack or in-app to a notification routes into the same
  intent layer as the composer.

---

## 6. Where alerts live

PAS surfaces alerts at four nested levels:

1. **Top bar notification bell.** Unread count badge. Click → drawer
   with all unread, grouped by severity.
2. **Command Center "Needs your attention" section.** The first
   thing the user sees on landing.
3. **Module-level alerts.** An inline banner at the top of a module
   when something inside that module needs review (e.g. "3 leads
   stalled this week").
4. **Row-level alerts.** A small badge on individual rows (e.g. a
   call that needs review, a booking that's at risk).

Rules:

- A single alert is never shown at more than two levels at the same
  time. Anti-spam (see Notification Architecture §6).
- Critical-severity alerts always include the top-bar level, even if
  also surfaced at row level.
- Dismissing an alert always asks for a reason if it had associated
  evidence; FYI alerts dismiss silently.

---

## 7. Where approvals live

Approvals are first-class. They have three surfaces:

| Surface | Visibility | Action |
|---|---|---|
| **Command Center → PAS proposes** | Visible on landing | Approve / decline / ask PAS / open in drawer. |
| **Action Proposals module** | Full queue, filterable | Multi-item review, batch deferral. |
| **Approval drawer** | Slide-over from any surface that references the proposal | Single-item full context. |

Rules:

- Every approval surface shows the same five fields: action, scope,
  side-effects, evidence link, expiry.
- Approving never requires more than one click + an optional reason.
- Approval drawers stack — opening a second drawer pushes the first
  to a "back" stack, never closes it silently.

---

## 8. Where integrations live

Integrations have a dedicated System-family module (Product Design
Book §4.14). Cross-references:

- **From a module** ("This data came from Follow Up Boss") → click
  routes to the Integrations module, filtered to that connector.
- **From the composer** ("connect my CRM") → PAS replies with a
  bounded action proposal that opens the Integrations module with
  the connect flow pre-selected.
- **From a Critical alert** ("Cal.com auth expired") → the alert
  routes directly to the connector card with the reconnect button.

Tokens, secrets, internal IDs are never exposed on these surfaces.
What the user sees: "Connected as <account>", scopes, health, last
sync, "What PAS can answer now".

---

## 9. Mobile navigation

Mobile is v1.x territory — full mobile support is not promised in v1.
But the IA must not foreclose it.

### 9.1 Mobile layout

- **Bottom tab bar:** at most five items, role-shaped.
  - For Owner/Admin: Command Center · Notice · People · System · More.
  - For Team Lead: Command Center · Notice · People · More.
  - For Agent: Command Center · Calls · Callbacks · Bookings · More.
  - For Viewer: Command Center · Calls · Bookings · More.
  - For ORVN: ORVN Console · Tenants · Notice · System · More.
- **Persistent PAS composer:** docked above the bottom tab bar; full
  PAS surface available via the composer's expand handle.
- **Off-canvas full nav:** "More" opens a full-height sheet with every
  visible module grouped by family.
- **Top bar:** condensed — tenant + bell + profile only. Search routes
  through the composer.

### 9.2 Mobile rules

- No module is **mobile-only**. If a module is hidden on mobile, it is
  hidden on every breakpoint above as well.
- A module **may** be desktop-only in v1 (e.g. Simulation Lab, PAS
  Brain editing), but mobile must render a clear "open on desktop"
  hand-off rather than a broken layout.
- Approvals on mobile use the same approval drawer pattern, sized to
  the viewport.
- Critical-severity alerts on mobile bypass quiet hours per the
  Notification Architecture and use the device's push channel.

---

## 10. Touch points between modules

The IA must support cross-references without forcing the user to
restart their flow.

| From | To | How |
|---|---|---|
| Call row → Lead | Inspector slide-over | "Open lead" link inside the call inspector. |
| Lead row → Calls | Filtered Calls module | "All calls for this lead" filter. |
| Recommendation → Evidence | Evidence Digest inline | Embedded inside the recommendation card. |
| Recommendation → Approval | Approval drawer | "Approve" opens the drawer in-place. |
| Action Proposal → Audit | Audit Logs scoped to the action | "View audit" inside the proposal. |
| Composer → any module | Inline section render | PAS pulls up an embedded view inside the thread. |
| Notification → source | Direct deep link | Each notification routes to the row + drawer in one click. |

A user should rarely need to navigate by the sidebar — most of the
day is contextual hops.

---

## 11. State labels and demo/rehearsal IA

Demo and rehearsal state is a first-class IA concern, not a footer
disclaimer.

- A **brokerage in demo mode** has a persistent banner at the top of
  every page: "Rehearsal mode — nothing on this page reaches the
  outside world."
- A **simulated artifact** (call, lead, booking, recommendation) is
  rendered with a "Simulated" tag inline in the row, every time.
- A **simulated module** is one where every row in scope is
  simulated; the module shows the banner directly under its title.
- **PAS in demo mode** announces it in its first reply: "We're in
  rehearsal mode — nothing I do here is live."

---

## 12. Information architecture invariants (checklist)

The IA is correct only if every one of these holds:

1. Every role sees a sidebar shaped by their bundle, with no empty
   family headers.
2. The Command Center is the default landing surface for every role.
3. PAS is reachable from every dashboard page via the persistent
   composer.
4. Approvals are reachable in one click from Command Center,
   Notifications, and the relevant module — never buried.
5. No surface exposes raw secrets, raw integration tokens, or internal
   identifiers.
6. Demo/rehearsal state is labelled persistently *and* inline.
7. Mobile preserves the same modules a user has on desktop, even if
   some hand off to "open on desktop" for v1.
8. Cross-module flow is contextual — sidebar navigation is the
   fallback, not the primary path.
9. The scope strip is always present when scope differs from the
   role's default.
10. No module is reachable to a role that doesn't have its permission.

---

## 13. Open IA questions

Tracked for v2 of this doc. Not blockers for v1.

- **Command Center personalisation** — should a user be able to
  re-order sections, or do we hold the line on uniform shape per role?
- **Search vs composer** — keep them merged behind Cmd/Ctrl + K, or
  split? Premium feel suggests merged; familiarity argues split.
- **Approval batch UX** — multi-select inside Action Proposals, or
  always one-at-a-time?
- **ORVN tenant switcher** — sidebar dropdown or top-bar switcher?
  Implications for screen real estate.
- **Density** — comfortable vs compact toggle, or one opinionated
  density?
- **Sidebar collapse** — auto-collapse on narrower viewports, or only
  on explicit user action?

---

*End of v1.*
