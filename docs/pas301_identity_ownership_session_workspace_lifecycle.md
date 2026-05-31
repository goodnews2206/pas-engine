# PAS301 — Identity, Ownership, Session & Workspace Lifecycle

> Status: product + technical specification (planning only — no code, UI, backend, CORS, auth implementation, database migrations, or package changes).
> Replaces the narrower "Auth / Session / Workspace" framing carried in PAS300 §20.
> Owner: ORVN Labs.
> Anchored on: `main` @ `8e9b237` (PR #54 — PAS300 product direction reset), the verified head of the merged reset.
> Naming: **PAS = Proactive Assistant for Scale.**
> Depends on: PAS300 (doctrine, workspace model, agent-first thesis). Blocks: PAS302 (role UX), PAS303 (Agent Cockpit), PAS304 (configuration), PAS308 (pricing).

---

## 1. Executive summary

PAS300 scoped the next step as "Auth / Session / Workspace Model." The PAS301 pre-flight
doctrine review concluded that framing is **too narrow**: it covers getting *into* PAS but
not *who owns what* while inside, nor getting *out* cleanly. The single hardest collision in
the product — **a person owning their identity vs. a brokerage legally owning the client and
transaction records created under its license** — lives precisely in the gaps that an
"auth/session" charter would skip. Real-estate brokers are the legal data custodians and are
required to supervise agent communications and retain transaction records for years; agents
are independent professionals who will reject any tool that feels like it belongs to their
broker. A login spec cannot resolve that. An ownership-and-lifecycle spec must.

PAS301 therefore expands to cover six concerns as one coherent foundation:

1. **Identity** — one durable PAS identity per person, independent of any workspace.
2. **Ownership & portability** — an explicit taxonomy of what the person owns and carries
   versus what the workspace governs and retains.
3. **Workspace lifecycle** — creation, joining, switching, role-scoping, and dissolution of
   personal, team, brokerage, and ORVN-admin workspaces.
4. **Offboarding** — clean, instant, and fair departure that revokes tenant access, retains
   tenant records, and lets personal capital leave intact.
5. **Session** — how identity is held, timed, and re-verified without making the user think
   about authentication.
6. **Memory governance** — provenance and subject tagging so the Brain can be both
   tenant-isolated and person-portable at once.

This is **planning/spec only**. It defines direction, contracts, and the PAS301A–PAS301J
implementation sequence. It implements none of it — no auth, no UI, no backend, no CORS, no
migrations, no packages. PAS209 and the parked stash are untouched.

---

## 2. Product principles

Auth, session, and workspace are normally the most enterprise-clunky surfaces in software.
For PAS they must be the opposite, because they are the *first* thing every user touches and
the foundation of the morning-open habit. They must feel:

- **Welcome home.** Signing in returns you to your assistant, not to a security checkpoint.
- **Simple.** A person should understand "this is me, this is where I'm working, this is my
  role" without a manual.
- **Secure.** Real isolation and real enforcement underneath the calm surface.
- **Fast.** Sign-in and especially workspace switching are instant; latency kills the habit
  (PAS300 §17: speed is a feature).
- **Non-enterprise-clunky.** No SSO config walls, no role matrices, no provisioning ceremony
  in the agent's face.
- **Safe for agents.** Private by default; the agent can see exactly what their broker can and
  cannot see, and trusts it.
- **Reassuring for brokerages.** Client data stays with the brokerage, offboarding is clean,
  supervision and retention are guaranteed.
- **Scalable to teams/brokerages.** The same identity and the same feel carry from one agent
  to a thousand, with no re-platforming.

The governing tension PAS301 must hold: **maximum safety with minimum friction.** Every
security requirement is judged by whether it can be met without the user having to think about
authentication.

---

## 3. Core doctrine

> **A person owns their identity and professional self. A workspace governs the business
> records created within it.**

This single sentence resolves the central collision. It splits what PAS300's earlier language
("PAS history follows the person where appropriate") left dangerously fused:

- **The person owns their *self*** — their identity, credentials, profile, the name they gave
  PAS, their preferences and personal PAS configuration, the scripts and talk tracks they
  authored, their coaching history, and their personal style/skill profile. This is theirs,
  forever, and travels with them across every workspace and every career move.
- **The workspace governs the *record*** — the client PII, leads sourced under the brokerage,
  deals, transaction documents, call recordings made under the license, brokerage knowledge,
  integration credentials, and audit trails created inside it. These are tenant-owned,
  broker-supervisable, retention-bound, and **non-portable**.

"Workspaces borrow access to the person" — a workspace is granted scoped access to a person's
attention and labor for as long as the membership lasts; it never acquires the person. When
the membership ends, the borrowed access ends, the person leaves whole, and the records stay.

This is not a compromise between two parties — it is a guarantee to *both*. To the agent:
"Your assistant, coaching, and playbook are yours and leave with you." To the brokerage:
"Client data, compliance, and records stay with you, and departures are clean." The same
doctrine recruits agents and reassures brokerages, which is exactly why it is the foundation.

Supporting doctrine, restated as binding for PAS301:

- Tenant isolation is **inviolable** — never a configurable setting.
- **Memory follows subject and source**; ties resolve toward the tenant.
- **The floor is privacy.** Upward and lateral visibility is explicit and scoped, never default.
- **Supervisability without surveillance** — the line between aggregate oversight and
  individual monitoring is doctrine, not a toggle.
- **Clean offboarding is a trust guarantee**, owed to agent and brokerage alike.
- PAS must **never feel like management software** to an agent.

---

## 4. Ownership taxonomy

Six ownership classes. Each entry: examples · portability · visibility · deletion/export logic
· risk if mishandled.

### A. Person-owned / portable
- **Examples:** identity & login, profile (name, photo, timezone), preferences, the PAS name
  and tone the person chose, personal PAS configuration, self-authored scripts/talk tracks,
  personal coaching history, personal style/skill/habit profile, personal productivity trends
  (self-view).
- **Portability:** fully portable; follows the person across all workspaces and survives every
  departure.
- **Visibility:** the person, always. No workspace owner sees it unless the person explicitly
  shares a specific item.
- **Deletion/export:** the person can export and delete their own. Deleting their PAS account
  removes it (subject to legal holds on anything reclassified as tenant data).
- **Risk:** if accidentally classified as workspace data, the agent feels owned by the broker →
  adoption collapse. If it carries embedded client PII, portability becomes a leakage channel —
  so person-owned items must be PII-clean by construction.

### B. Personal workspace-owned
- **Examples:** the agent's own self-sourced leads/sphere, private notes, personal uploaded
  documents, personal Brain memories about their own book.
- **Portability:** owned by the person *as the controller of their own tenant*; stays in the
  personal workspace, which the person keeps when they join other workspaces.
- **Visibility:** the person only. A brokerage the person later joins **cannot see it.**
- **Deletion/export:** the person controls export and deletion entirely.
- **Risk:** bleed of personal-workspace client data into a brokerage query (or vice versa) — a
  privacy breach against the agent and a contamination risk for the brokerage.

### C. Team workspace-governed
- **Examples:** shared team pipeline, team commitments and callbacks, shared scripts, team
  standards, aggregated (non-individual) team operational health.
- **Portability:** non-portable; belongs to the team workspace (a context within the brokerage
  tenant). Members access it by role for the duration of membership.
- **Visibility:** team members per role; the team lead sees more breadth, never an individual
  agent's private workspace.
- **Deletion/export:** governed by the brokerage/team owner under tenant rules; individuals
  cannot export it on departure.
- **Risk:** team-lead knowledge *about other members* being treated as portable → leakage of
  third parties' data. It is never the departing lead's to keep.

### D. Brokerage workspace-governed
- **Examples:** client PII, brokerage-sourced leads, deals/transactions, call
  recordings/transcripts under the license, brokerage SOPs and knowledge, integration
  credentials, brand scripts, compliance records, full audit trail.
- **Portability:** **non-portable.** Tenant-owned, broker-supervisable, retention-bound.
- **Visibility:** by role within the brokerage; supervision roles see compliance-relevant
  records, never an agent's personal workspace.
- **Deletion/export:** the brokerage (as data controller) exports and retains per legal
  obligation; an agent **cannot** export tenant PII, and **cannot** delete records under
  retention.
- **Risk:** the brokerage's #1 fear — an agent walking out with the client book. Mishandling
  here makes PAS unsellable to brokerages.

### E. ORVN admin-governed
- **Examples:** cross-tenant platform health, provisioning state, support tooling, incident
  records, platform audit logs, billing metadata (later).
- **Portability:** non-portable; lives only in the ORVN-admin context.
- **Visibility:** ORVN internal staff at their scope only; strictly outside customer-facing
  surfaces.
- **Deletion/export:** governed by ORVN platform policy and internal audit.
- **Risk:** exposing tenant secrets through admin tooling, or any path by which a customer
  tenant could acquire ORVN-admin scope. Both are platform-integrity failures.

### F. Never portable
- **Examples (the hard floor):** client PII, transaction records, call recordings, brokerage
  proprietary knowledge, integration credentials, memory *about other people* (colleagues,
  team members), and anything the person did not originate that belongs to a tenant.
- **Portability:** never, under any flow, including account export and hostile departure.
- **Visibility:** by tenant role only.
- **Deletion/export:** tenant-controlled and retention-bound; the individual has no export path.
- **Risk:** any leak here is simultaneously a privacy violation, a compliance breach, and a
  competitive harm. This class is the bright line the whole product is built to never cross.

**The resolving rule for every disputed item:** classify by **subject** (about the person, or
about a client/deal/colleague?) and **source** (the person's own behavior, or tenant data?).
About the person, from the person → A/B (portable). About a client/deal/colleague, from tenant
data → C/D/F (governed). **When in doubt, the PII-bearing / regulated classification wins and
the item stays with the tenant.**

---

## 5. User identity model

- **One PAS identity per person.** A single durable identity object that is the person, not a
  per-workspace account.
- **One login.** The person authenticates once as themselves; they never maintain separate
  credentials per workspace (explicitly avoiding the fragmented multi-account pattern).
- **Membership in many workspaces.** One identity can belong to a personal workspace, one or
  more teams, one or more brokerages, and (for staff) the ORVN-admin context — concurrently.
- **Profile belongs to the person.** Name, photo, timezone, preferences, and personal PAS
  configuration are attributes of the identity, shared across workspaces, not owned by any one
  of them.
- **Role is workspace-specific.** Authorization is computed per workspace at the membership
  level, not globally.
- **Same identity, different roles.** The same person can be an Agent in Brokerage X, a Team
  Lead in Team Alpha, and an Owner of their own Brokerage Y — simultaneously, with each role
  scoped to its workspace and carrying no authority into the others.

Identity is the stable spine; workspaces and roles are the changing context around it. This is
what makes the 2026→2031 career lifecycle (PAS300 pre-flight) a continuous account rather than
a series of new ones.

---

## 6. Workspace types

Four types. Each: purpose · who creates it · who joins · default role model · what PAS shows
first · what it must never expose · what data belongs there.

### Personal Agent Workspace
- **Purpose:** the agent's private home and the seat of the morning-open habit.
- **Created by:** the person, automatically, on sign-up. Every identity has exactly one.
- **Joins:** no one. It is single-occupant by definition.
- **Default role:** Owner (the person).
- **Shows first:** the Agent Cockpit (PAS303) — what to do next, what was forgotten, what to
  improve.
- **Must never expose:** anything in it to any brokerage, team, or other person, unless the
  person explicitly shares a specific item.
- **Data:** self-sourced leads/sphere, private notes, personal documents, personal coaching,
  personal scripts, personal memory (classes A/B).

### Team Workspace
- **Purpose:** a shared operating context for a pod within a brokerage.
- **Created by:** a brokerage owner or an authorized team lead, *within* a brokerage tenant.
- **Joins:** agents invited into the team; membership is explicit and revocable.
- **Default role model:** Team Lead (manage + bounded visibility) and Member (participate).
- **Shows first:** the team's commitments, gaps, ramping agents, shared pipeline state.
- **Must never expose:** any member's personal workspace; individual-surveillance scorecards.
- **Data:** shared pipeline, shared callbacks, shared scripts, team standards, aggregate health
  (class C).

### Brokerage Workspace
- **Purpose:** the brokerage-wide operating layer and the legal custodian of business records.
- **Created by:** a broker owner.
- **Joins:** agents and staff invited by the owner/admin; teams nest within it.
- **Default role model:** Owner, Admin/Ops, Supervisor (compliance oversight), Team Lead,
  Agent, Read-only Viewer.
- **Shows first:** operation-wide state — pipeline health, attention queue, risk, integration
  health, standards adherence (the owner altitude, PAS300 §9).
- **Must never expose:** an agent's personal workspace; any other tenant's data.
- **Data:** client PII, brokerage-sourced leads, deals, transaction docs, call recordings,
  SOPs/knowledge, integration credentials, compliance records, audit trail (classes D/F).

### ORVN Admin Workspace
- **Purpose:** platform operations — cross-tenant health, provisioning, support, safety.
- **Created by:** ORVN internally; never by a customer action.
- **Joins:** ORVN staff only, minted internally.
- **Default role model:** internal admin scopes (support, provisioning, incident) under least
  privilege.
- **Shows first:** platform health and safety confirmation.
- **Must never expose:** tenant secrets beyond what a support task requires; nor be reachable
  or grantable by any customer tenant.
- **Data:** platform health, provisioning, incident records, platform audit (class E).

---

## 7. Workspace switching

- **Switcher UX.** A single, always-reachable switcher lists every workspace the identity
  belongs to, grouped (Personal · Teams · Brokerages · [ORVN]). One identity, many doors.
- **Persistent active-workspace indicator.** The active workspace is shown unambiguously and
  permanently (name + distinct color/avatar) so the user never guesses which tenant they are
  acting in. This is the single most important error-prevention control.
- **Current role/hat indicator.** Alongside the workspace, the current role is visible
  ("Agent in Brokerage X," "Team Lead in Team Alpha").
- **Personal ↔ team ↔ brokerage switching.** Free movement among the user's memberships; the
  personal workspace is always one click away (it is home).
- **Invited-workspace acceptance.** A pending invitation appears in the switcher as an
  accept/decline item; accepting adds the workspace, keeping the personal workspace intact.
- **No re-login on switch.** Switching re-scopes authorization within the existing session; it
  never asks the user to authenticate again.
- **Wrong-workspace prevention.** Sensitive, tenant-touching actions name the active context
  ("Acting as Team Lead in Brokerage X"); the chrome's color/name reinforces it everywhere.
- **Per-workspace notification labeling.** Every notification is tagged with its source
  workspace; there is no undifferentiated feed that hides which tenant pinged you.
- **Tenant-scoped search and Brain by default.** Search and PAS Brain queries operate only
  within the active workspace; results and citations never cross tenant boundaries.
- **One allowed cross-workspace view: "my obligations."** A personal roll-up of the *person's
  own* callbacks/follow-ups across all their workspaces. It may show *that* an obligation
  exists in Brokerage X, but it carries only the person's own items and **never** surfaces
  another tenant's client data into the personal layer or any other tenant.

---

## 8. Sign-up / onboarding paths

Five paths. Each: first screen · required info · default workspace · what PAS asks next · what
PAS must not ask yet · agent-friendly copy.

### A. Solo agent creates account
- **First screen:** "Meet your PAS." A single sign-up field set, no org questions.
- **Required:** email, password (or magic link), name.
- **Default workspace:** a Personal Agent Workspace, created automatically.
- **Asks next:** "What should I call you, and what do you want to call me?" then the first
  useful action (import a lead, set working hours).
- **Must not ask yet:** brokerage, team, billing, integrations, role.
- **Copy:** *"PAS is yours. Let's set up your assistant — this stays with you no matter where
  you work."*

### B. Agent invited by brokerage/team
- **First screen:** "Brokerage X invited you to PAS." Accept/decline, with what joining grants.
- **Required:** accept; if no account, minimal sign-up (email, name, password/magic link).
- **Default workspace:** their Personal Agent Workspace **plus** a seat in the inviting
  workspace; personal stays private.
- **Asks next:** "Here's your team space. Your personal space is separate and private."
- **Must not ask yet:** anything that implies the brokerage can see their personal workspace.
- **Copy:** *"You've been invited to Brokerage X. You'll get a shared space for that work —
  and your own private PAS stays yours."*

### C. Broker owner creates brokerage workspace
- **First screen:** "Set up your brokerage on PAS." Name the brokerage.
- **Required:** owner identity (sign-up if new), brokerage name.
- **Default workspace:** a Brokerage Workspace with the creator as Owner (plus their own
  Personal Workspace).
- **Asks next:** "Invite your first agents" and "Set your standards" (scripts, callback rules).
- **Must not ask yet:** deep integrations, billing tiers, complex role matrices.
- **Copy:** *"Stand up your brokerage's operating layer. Your agents keep their own private
  PAS — you standardize the work, not the person."*

### D. ORVN creates enterprise workspace
- **First screen:** internal provisioning console (not customer-facing).
- **Required:** internal authorization, enterprise tenant details, designated owner.
- **Default workspace:** a provisioned Brokerage/Enterprise Workspace handed to the customer
  owner; bespoke setup.
- **Asks next:** internal: configure limits, hand off ownership.
- **Must not ask yet (of the customer):** nothing self-serve; this path is manual by design.
- **Copy:** internal tooling; no agent-facing copy.

### E. Returning user signs in
- **First screen:** sign-in (see §9), then land in the **last active workspace**.
- **Required:** credentials / magic link / OAuth.
- **Default workspace:** last active; switcher available immediately.
- **Asks next:** nothing — welcome home, straight to "what to do next."
- **Must not ask yet:** re-onboarding, re-consent, setup repetition.
- **Copy:** *"Welcome back. Here's what needs you today."*

---

## 9. Sign-in flow

- **Email/password vs magic link.** Magic link minimizes friction and password risk and fits
  the "no thinking about auth" principle; password supports users who prefer it and offline
  password managers. Direction: support both, lead with whichever the chosen provider makes
  most frictionless (open question §26).
- **Google sign-in.** Strong candidate for the fastest agent onboarding (most agents have a
  Google identity). Consider as a first-class option from early.
- **Future SSO.** Brokerage/enterprise SSO (SAML/OIDC) is a *later* concern (PAS301 non-goal);
  the model must not preclude it.
- **Minimum viable flow:** identify (email) → verify (link/password/OAuth) → land in last
  active workspace. No org selection at sign-in; workspace context is resolved after.
- **Friendly copy:** *"Sign in to your PAS."* / *"We'll email you a secure link."*
- **Failure states:** wrong password (retry, no user enumeration), expired link (re-request),
  rate-limited (calm message, not alarming), unknown email (offer sign-up without confirming
  existence).
- **"One identity, many doors" metaphor.** Sign-in authenticates the *person*; the workspaces
  are doors that person can already open. The user signs in as themselves, then chooses where
  to work — never signs in "to a workspace."

---

## 10. Sign-out flow

- **Account menu.** A consistent account/avatar menu (top corner) is the home for sign-out,
  profile, and account settings.
- **Sign-out button.** Clearly present in that menu.
- **Confirmation.** Lightweight confirm ("Sign out of PAS?") to prevent accidental loss,
  especially mid-work.
- **After sign-out:** return to the sign-in screen; the active session is invalidated.
- **Unsaved work.** Warn before discarding unsaved input; PAS should favor auto-saving drafts
  so sign-out is never destructive.
- **Session invalidation.** Sign-out invalidates the session server-side, not just client-side
  (frontend clearing alone is not sign-out).
- **Demo/current placeholder.** The current demo scaffold has no real session; until the auth
  arc, the account menu and sign-out are **shells** that route to placeholder states and carry
  the demo-safety posture (no live behavior). This doc does not implement real sign-out.

---

## 11. Session behavior

Direction only — implemented in the later auth arc, not here.

- **Session lifetime.** A sensible default for a tool holding operational business data
  (proposed default an open question §26); long enough to feel like home, short enough to be
  safe.
- **Idle timeout.** Idle re-verification after a configurable period; absolute cap regardless
  of activity.
- **Remember device.** Trusted-device option to reduce repeat friction on the user's own
  machine.
- **Session limit.** Bounded concurrent sessions per user; excess prompts review.
- **Active device/session list.** The user can see and revoke their active sessions/devices
  (full UI is later; the model is defined now).
- **Forced sign-out.** Admins (at their scope) and the person can force-terminate sessions.
- **High-risk action re-auth.** Step-up verification for sensitive actions (changing security
  settings, exporting data, destructive operations) even within a live session.
- **Workspace switch without re-login.** Switching re-scopes authorization in-session (§7); it
  never re-authenticates.
- **Secure cookies / tokens.** Direction: httpOnly, secure, same-site cookies and/or short
  access tokens with refresh; exact scheme decided in PAS301D. No token scheme is chosen here.
- **Mobile considerations.** Sessions must behave well on mobile (longer practical lifetimes,
  biometric unlock as a later option); the morning-open habit is often a phone habit.

---

## 12. Security posture

- **No tenant leakage.** Tenant isolation is enforced at the data layer; no query, citation,
  notification, or search result crosses a workspace boundary.
- **Role-bound access.** Authorization is computed per workspace membership, never globally.
- **Server-side enforcement.** All authorization decisions are enforced on the server.
- **Frontend gating is not security.** Hiding or disabling UI is UX, not a control; every
  gated action is independently enforced server-side.
- **Audit logging.** Auth, session, and workspace events (sign-in, sign-out, switch, invite,
  role change, offboarding, export) are audit-logged within the relevant tenant.
- **ORVN admin minted internally only.** ORVN-admin scope is granted exclusively through
  internal provisioning.
- **Tenant cannot grant ORVN admin.** No customer-tenant action, role, or invite can confer
  ORVN-admin scope — a hard, non-configurable boundary.
- **Least privilege.** Every role gets the minimum scope needed; supervision roles get
  compliance-relevant access, not blanket visibility.
- **Inactive session handling.** Idle and abandoned sessions expire and are invalidated
  server-side per §11.

---

## 13. Role binding

- **Workspace-scoped roles.** A role exists only within a workspace membership; it confers no
  authority elsewhere.
- **Different roles across workspaces.** The same identity holds independent roles per
  workspace (Agent here, Team Lead there, Owner of their own brokerage).
- **Role changes are audited.** Every grant, change, or revocation is recorded in the tenant's
  audit trail with actor and time.
- **Invite grants role.** A role is conferred by an accepted invitation (§14), not assumed.
- **Tenant cannot grant ORVN Internal Admin.** Restated as a role rule: no tenant role can
  escalate to platform admin.
- **Broker supervision vs agent private roles.** Supervision is a distinct role with
  compliance-relevant visibility into *brokerage* work; it explicitly does **not** include
  access to any agent's personal workspace or personal coaching. The separation between
  "supervisor of brokerage records" and "owner of a private personal workspace" is structural.

---

## 14. Invitation model

- **Invite by email.** An owner/admin (or authorized team lead) invites a person by email.
- **Invite into a workspace** with a **specified role**.
- **Pending invite.** Visible to the inviter (status) and, once the recipient has/creates an
  account, in their switcher as accept/decline.
- **Accepted invite.** Adds a workspace membership with the granted role; the recipient keeps
  their personal workspace.
- **Expired invite.** Invitations expire after a bounded window and must be re-issued.
- **Revoked invite.** An owner/admin can revoke a pending invite before acceptance.
- **Invitee already has a PAS account.** The invite attaches to the existing identity; no new
  account, no duplicate profile — one identity, additional door.
- **Invitee has no PAS account.** Minimal sign-up flow (§8B) precedes acceptance; their
  personal workspace is created alongside.
- **Invite-abuse prevention.** Rate limits on invites, domain/role constraints, owner controls
  over who may invite, and no information leakage about whether an email already has an account
  (open question §26 for specific mechanism).
- **Workspace-owner controls.** Owners govern who can invite, into what roles, and can revoke
  memberships and pending invites.

---

## 15. Profile / account model

Belongs to the person (class A); deliberately *not overbuilt* at v1.

- **Name** — display identity across workspaces.
- **Photo/avatar** — optional; later (PAS300 §17).
- **Phone** — optional.
- **Timezone** — drives scheduling, working hours, callback timing.
- **Working hours** — when PAS acts and contacts on the person's behalf.
- **Notification preferences** — channels and quiet hours, per the calm doctrine.
- **PAS personal preferences** — the name they gave PAS, tone, response style (ties to PAS304).
- **Password / security** — credentials and security settings (step-up, sessions).
- **Connected accounts** — Google/OAuth links, future SSO identities.
- **Profile portability** — the profile is identity-level and follows the person across
  workspaces; it is never owned by a tenant.
- **Not overbuilt at v1.** The v1 profile is a shell with name, the PAS name/tone, timezone,
  and working hours; everything else is later.

---

## 16. Agent personal workspace

Strategically the most important workspace in PAS, because it is the adoption wedge.

- **Bottoms-up adoption.** An agent can sign up, get value, and form the morning-open habit
  alone — no brokerage required (PAS300 §6).
- **Agents can pay individually.** The personal workspace is a real self-serve customer; a
  revenue path that does not depend on enterprise sales.
- **Brings PAS into the brokerage later.** Agents who rely on PAS carry it into their teams and
  brokerages, flipping the enterprise conversation from "should we buy?" to "standardize what
  our people already love."
- **Stays theirs when invited to a brokerage.** Joining a brokerage adds a seat; it never
  absorbs, exposes, or transfers the personal workspace.
- **Personal data boundaries.** Self-sourced leads, private notes, and personal documents are
  visible only to the person.
- **Private coaching.** Coaching lives here, for the agent, never as a report to a broker.
- **Personal scripts.** The agent's authored talk tracks are theirs (class A) and portable.
- **Self-sourced leads.** Leads the agent brings themselves are personal-workspace data
  (class B) and do not become brokerage property by virtue of the agent also having a
  brokerage seat.

The personal workspace is where "PAS is on your side" is literally true — and that truth is
what makes the agent-first thesis work.

---

## 17. Brokerage / team workspace

- **Shared leads.** Brokerage-sourced leads are tenant-owned and shared by role.
- **Shared callbacks.** Team/brokerage callback commitments are visible and assignable per role.
- **Shared PAS Brain.** A tenant-scoped knowledge base (PAS306) the organization can query;
  isolated from every other tenant and from members' personal workspaces.
- **Shared PAS configuration.** Brokerage standards (scripts, callback strictness, approval
  rules) set the frame within which agents personalize (PAS304; PAS300 §11).
- **Team communication.** Operation-attached communication (PAS300 §14), not a Slack clone.
- **Role permissions.** Owner/Admin/Supervisor/Team Lead/Agent/Viewer per §13.
- **Member management.** Owners/admins invite, assign roles, and offboard members.
- **Approval policies.** What requires explicit approval vs. what is pre-authorized, within the
  approval-gated doctrine.
- **Broker supervisability.** Brokerage work is supervisable for compliance (license-law
  requirement) — *without* reaching into agents' personal workspaces (§22).
- **Compliance records.** Communication and transaction records are retained per legal
  obligation; agents cannot delete records under retention.
- **Offboarding continuity.** When a member leaves, in-flight obligations are reassigned within
  the tenant so clients are never dropped (§21).

---

## 18. ORVN Admin workspace

- **Internal-only.** Strictly outside customer-facing surfaces.
- **Tenant support.** Tools to help customers, scoped to the support task.
- **Tenant health.** Cross-tenant observability of platform health and safety.
- **Billing visibility (later).** Account/billing oversight in a later phase.
- **Provisioning.** Create/configure enterprise tenants and hand off ownership.
- **Incident response.** Detect, record, and respond to safety/security incidents.
- **No unnecessary secret exposure.** Admin tooling surfaces the minimum required; tenant
  secrets are not casually visible.
- **Not grantable by customer tenants.** A hard boundary (§§12–13): no tenant path mints
  ORVN-admin scope.
- **Internal audit required.** Every ORVN-admin action is audit-logged at the platform level.

---

## 19. Memory ownership + provenance

Every memory PAS forms must carry three pieces of metadata so it can be governed correctly:

- **Subject** — who/what the memory is *about* (the person, a client, a deal, a colleague, the
  organization).
- **Source workspace** — the tenant in which it was formed.
- **Provenance** — what evidence it came from (a call, a document, a record, observed behavior).

Classification, by subject + source (§4's resolving rule applied to memory):

- **Person-owned memories** — about the person, from the person's own behavior. Portable.
  *Example:* "Agent closes better after night-before prep."
- **Workspace-governed memories** — about a client/deal/standard, from tenant data.
  Non-portable. *Examples:* "Client prefers texts after 6pm." · "Team standard: callbacks
  within 15 minutes."
- **Shared memories** — workspace-governed, visible to the workspace by role (team standards,
  shared client context within the tenant).
- **Never-portable memories** — anything carrying client PII or about other people; never
  leaves the tenant under any flow.
- **Ties resolve toward the tenant.** Ambiguous memory (mixed subject, or person-derived but
  PII-bearing) is classified as workspace-governed and stays.

This metadata is foundational: tenant isolation (§§7, 20) and clean offboarding (§21) both
depend on every memory knowing its subject, source, and provenance from the moment it is
created.

---

## 20. PAS Brain across workspaces

- **Active-workspace scoped by default.** A query runs within the active workspace only.
- **No cross-tenant citations.** Every cited piece of evidence resolves inside the active
  tenant; a citation exposing another workspace's record would be a breach.
- **No data bleed.** Search, answers, and suggestions never mix data across tenants.
- **Personal coaching usable across workspaces — if non-PII.** The person's own coaching and
  authored craft (class A, PII-clean) are available to them wherever they work, because they
  are the person's. They never carry personal-workspace *client data* into a brokerage, nor
  brokerage data into the personal layer.
- **Brokerage data never leaks** into a personal workspace or into another brokerage workspace —
  even for an agent who belongs to both.
- **"My obligations" roll-up rules.** The one sanctioned cross-workspace view (§7) surfaces
  only the person's *own* obligations across workspaces; it never aggregates or exposes any
  tenant's client data, and it respects each tenant's rules about what the person's PAS may see.
- **Queryable company vs queryable person.** Two distinct surfaces: the *organization* querying
  its own tenant ("what callbacks does the brokerage owe today?") and the *person* querying
  their own workspace ("what did I forget?"). Each is scoped to its owner; neither reaches the
  other.

---

## 21. Clean offboarding lifecycle

The trust guarantee owed to agent and brokerage alike.

- **Agent removed from a workspace** — by the owner/admin, or by the agent leaving.
- **Tenant access revoked instantly.** The moment membership ends, access to all
  workspace-governed data ends — including any residual visibility a former Team Lead had into
  members.
- **Tenant records retained.** Client PII, deals, recordings, and compliance records stay with
  the tenant, intact, under retention.
- **Personal capital survives.** Identity, profile, preferences, personal PAS configuration,
  self-authored scripts, and personal coaching leave with the person, whole.
- **In-flight obligations reassigned.** Pending callbacks and live deals are reassigned within
  the tenant so clients are never dropped; nothing is exported to the departing agent.
- **Audit trail retained.** The record of who had access when stays with the tenant.
- **Brokerage can export governed records.** As data controller, the brokerage exports/retains
  its records per obligation.
- **Agent cannot export tenant PII.** No flow — including account export or hostile departure —
  lets the person take client PII or other never-portable data (§4F).
- **Agent retains personal scripts/coaching/preferences** (restated for emphasis: the person
  leaves whole on the person-owned axis).
- **Hostile-departure scenario.** Even when a departure is adversarial (for cause, or a
  poaching attempt), the split holds automatically: access dies instantly, tenant data stays,
  personal capital leaves clean. Neither side can weaponize the other's ownership.

---

## 22. Supervisability without surveillance

- **Broker can supervise brokerage work.** Compliance oversight of communications and
  transactions conducted under the brokerage license — a legal requirement, satisfied within
  the brokerage tenant.
- **Broker cannot read an agent's personal workspace.** Structurally impossible, not a setting.
- **Broker gets compliance oversight** of regulated brokerage records.
- **Broker gets aggregate operational health** — pipeline health, risk, standards adherence at
  the operation level.
- **Agent gets private coaching** — specific, kind, evidence-backed, for the agent only.
- **No productivity scorecards/leaderboards as defaults.** Ranking and individual scoring are
  not the default posture; the default is coaching and aggregate health.
- **Personal weaknesses are not management reports.** An agent's coaching content is never
  exposed upward. The line between *aggregate oversight* (allowed) and *individual
  surveillance* (forbidden) is doctrine, enforced by the ownership split, not left to a toggle.

This is what lets PAS satisfy the brokerage's legal supervision duty while remaining, to the
agent, unmistakably a personal assistant rather than a management instrument.

---

## 23. Data-controller / privacy responsibility

- **Personal workspace controller:** the **person**. They control export, deletion, and use of
  their personal-workspace data.
- **Brokerage workspace controller:** the **brokerage**. It is the data controller for client
  PII and transaction records, responsible for export, retention, and lawful processing.
- **Team workspace:** governed within the brokerage tenant; the brokerage is controller.
- **ORVN platform role:** **processor/platform** — ORVN operates the platform and processes
  data on behalf of the controllers; it is not the controller of customer business data.
- **Customer data boundaries.** Each controller's data is isolated; ORVN does not repurpose or
  cross-pollinate tenant data.
- **Deletion/export responsibility.** Falls to the controller of each class: the person for
  personal data, the brokerage for tenant records (subject to retention).
- **Retention responsibility.** The brokerage owns legal retention of brokerage records; the
  person owns retention of personal data; ORVN enforces the mechanisms.

(Specific regulatory mappings — CCPA, state real-estate retention windows, GDPR-style regimes —
are flagged as open questions §26 and resolved with counsel, not in this doc.)

---

## 24. UX requirements

- **Account menu location.** Consistent top-corner avatar/account menu — home for profile,
  account settings, sessions, and sign-out.
- **Workspace switcher location.** Persistent, always reachable, grouped by type.
- **Active-workspace indicator.** Always visible (name + color/avatar); the user never guesses
  their tenant.
- **Current role/hat indicator.** The active role is shown with the workspace.
- **Profile section.** Calm, sectionized; not a wall of fields (§15 is intentionally small).
- **Settings sectionization.** Settings are grouped into findable sections — **no endless
  settings scroll** (PAS300 §17).
- **Light/dark mode** — later.
- **Mobile auth considerations.** Sign-in, switching, and sessions must feel native and fast on
  mobile; the morning-open habit is often a phone habit.
- **Onboarding feels like welcome home.** First-run is warm and useful, not a setup gauntlet.
- **Non-technical explanation: "one you, many doors."** Avoid the words "workspace," "tenant,"
  "multi-tenant" in agent-facing copy; lead with the promise — *"PAS is yours and stays with
  you; your personal space is private; joining a brokerage gives you a shared space and keeps
  your own separate."* Make the privacy boundary visceral by naming what the broker cannot see.

---

## 25. MVP scope vs later

### MVP (this planning arc and its immediate shells — no real auth)
- Account menu **shell**.
- Sign-out **shell** (placeholder behavior, demo-safe).
- Profile **shell** (name, PAS name/tone, timezone, working hours).
- Workspace switcher **shell** with active-workspace and role indicators.
- Membership model **spec**.
- Invite model **spec**.
- Role-aware routing (frontend gating as UX only, not security).
- Workspace labels and per-workspace notification labeling (presentational).
- **Docs/spec only** until the dedicated implementation arc.

### Later
- Full real authentication.
- SSO (brokerage/enterprise).
- Device management UI.
- Session-limit UI.
- Advanced security (step-up, risk handling).
- Enterprise policies.
- Cross-workspace messaging.
- Billing-linked workspace limits.

---

## 26. Open questions

- **Magic link vs password first?** Which is the lead sign-in method for the agent funnel?
- **Google OAuth first?** Make Google a first-class day-one option?
- **Session lifetime defaults?** Idle and absolute timeout values for an operational-data tool.
- **Solo agent free trial?** Is the personal workspace free, trial, or freemium (ties to
  PAS308)?
- **Workspace naming rules?** Uniqueness, collisions, renaming, reserved names.
- **Invite-abuse prevention?** Specific rate limits, domain controls, anti-enumeration scheme.
- **Workspace deletion/export?** What deletion and export look like for a brokerage tenant
  under retention obligations.
- **Personal vs brokerage memory boundaries?** Exact rules for memory formed while an agent
  works brokerage leads in their brokerage seat vs. their own sphere.
- **Dual affiliation by state?** How to handle agents licensed/affiliated under two brokerages
  where state law varies (permitted vs. forbidden).
- **Estate / incapacity?** What happens to a personal workspace and in-flight client service on
  death or incapacity.

---

## 27. Implementation sequence proposal (PAS301A–PAS301J)

Each is a scoped effort; spec precedes build. Ordered by dependency.

- **PAS301A — Account/Profile Shell.** The account menu, profile section, and the
  identity-level profile model (shell; no real auth).
- **PAS301B — Workspace Switcher Shell.** The switcher, active-workspace indicator, role/hat
  indicator, and "my obligations" placeholder (presentational).
- **PAS301C — Ownership/Portability Data Model Spec.** The §4 taxonomy and §19 memory
  provenance as a concrete data-model specification (spec; the foundation everything else
  enforces).
- **PAS301D — Auth Provider Decision.** Resolve §9/§26: magic link vs password, Google OAuth,
  SSO path, token/cookie scheme direction.
- **PAS301E — Sign-in/Sign-out Frontend Flow.** The real sign-in/sign-out UX against the chosen
  provider.
- **PAS301F — Backend Auth Boundary.** Server-side identity, session, and the enforcement point
  (the line where frontend gating becomes real security).
- **PAS301G — Workspace Membership Model.** Memberships, roles, and tenant scoping enforced.
- **PAS301H — Invite Flow.** The §14 invitation lifecycle end to end.
- **PAS301I — Role Enforcement Server-Side.** Per-workspace role-bound authorization enforced on
  the server, with audit.
- **PAS301J — Offboarding Lifecycle.** The §21 clean-departure flow: instant revocation,
  retention, personal-capital survival, in-flight reassignment.

---

## 28. Non-goals

Explicitly **not** built in this arc:

- Full enterprise SSO.
- Billing enforcement.
- Real workspace deletion.
- Device risk scoring.
- Cross-workspace social graph.
- A complex RBAC matrix.
- An ORVN admin console rebuild.
- **Real auth in this doc PR** — this document changes no code, UI, backend, CORS, migrations,
  or packages.

---

## 29. Final standard

> **A user should feel that PAS knows who they are, where they are working, what role they
> hold, what they personally own, and what the workspace safely governs — without making them
> think about authentication.**

---

### Validation note

This document is **docs-only**. It makes **no** changes to code, UI, backend, CORS, auth
implementation, database migrations, packages, the PAS209 work, or the parked stash. It defines
the identity, ownership, session, and workspace-lifecycle direction and the PAS301A–PAS301J
implementation sequence; it implements none of it. Nothing is pushed.
