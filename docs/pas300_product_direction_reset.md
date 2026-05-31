# PAS300 — Product Direction Reset

> Status: strategic direction document (planning only — no code, UI, backend, CORS, auth, or PAS209 changes).
> Supersedes the implicit direction carried through the A–I operational demo arc.
> Owner: ORVN Labs.
> Anchored on: `main` @ `9f932da` (PR #53 — Command Center refinement), the head of the completed A–I arc deployed on Vercel.
> Naming reset: **PAS = Proactive Assistant for Scale.**

---

## 1. Executive summary

The A–I operational demo arc is complete and deployed. It did exactly what it was
scoped to do: it proved that PAS can be **structured** as an operating product —
navigation, modules, a Brain surface, a Room surface, an integrations model, a
typed demo data layer, and a consistent safety posture all hold together as one
coherent application shell.

But a product review of the deployed surface made one thing clear: **structure is
not dependency.** The current UI proves that the pieces exist and relate to one
another. It does not yet prove that anyone *needs* to open it. Several pages still
read as explanatory and dashboard-like — they describe state rather than drive a
day. They show a business; they do not yet *run* one.

This is the moment to reset direction before building deeper. The reset is not a
rewrite and not a repudiation of A–I. It is a **change of intent**: from proving
that PAS can be assembled, to proving that PAS becomes habitual. The product must
shift from a *brokerage dashboard* into a *daily operating companion* for agents,
teams, and brokerages — the first thing they open in the morning, trust through
the day, and review before they close it.

The naming reset captures the shift. PAS is **Proactive Assistant for Scale**: an
assistant first (personal, calm, on your side), proactive second (it surfaces what
matters before you ask), built for scale third (it grows from one agent to an
enterprise without changing what it feels like). This direction document defines
the doctrine, the user classes, the workspace and auth model, the agent-first
distribution thesis, and the next planning sequence (PAS301–PAS308) that turns the
reset into work.

---

## 2. New PAS definition

**PAS = Proactive Assistant for Scale.**

PAS is a proactive operating assistant that makes a real-estate business
**queryable, adaptive, and operationally intelligent** — and does so in a way that
an individual agent welcomes, a team relies on, and a brokerage standardizes.

Why this definition is stronger for distribution and agent adoption:

- **"Assistant" disarms.** Agents fear tools that watch, grade, and replace them.
  An *assistant* works for the agent. It frames PAS as something on the agent's
  side — remembering, preparing, following up — rather than a management instrument
  pointed at them.
- **"Proactive" is the differentiator.** A dashboard waits to be read. An assistant
  tells you what changed, what you forgot, and what to do next. Proactivity is the
  feature that creates the morning-open habit; it is the reason to return.
- **"for Scale" carries the business model.** The same product serves one agent and
  a thousand. Scale is the promise to brokerages (standardize and grow without
  chaos) and the ladder for solo agents (start alone, invite a team, become a
  brokerage) — without the product ever feeling like different software.

What PAS is explicitly **not** allowed to be called or positioned as:

- Not "Performative AI Superstaff" — performance theater, not utility.
- Not an "AI chatbot" — chat is a surface, not the identity.
- Not a "generic dashboard" — dashboards describe; PAS operates.
- Not a "CRM replacement" as a front-facing claim — even if it absorbs CRM jobs,
  leading with replacement triggers procurement fear and feature-checklist
  comparisons instead of adoption.

Preserved strategic doctrine (unchanged): **PAS makes the business queryable,
adaptive, and operationally intelligent.**

---

## 3. Core doctrine

Every surface, feature, and decision is measured against these seven principles.

1. **Queryable.** Any operator can ask the business a question in natural language
   and get a grounded answer — about leads, calls, callbacks, deals, scripts,
   documents, and history. The business stops being a pile of tools and becomes
   something you can interrogate.
2. **Adaptive.** PAS learns the operation — its language, its rules, its rhythms,
   its people — and adjusts. The same product feels different (correctly) for a
   solo agent and a 200-agent brokerage because it has adapted to each.
3. **Operationally intelligent.** PAS understands the *work*, not just the data:
   what a callback commitment means, when a lead is going cold, why a script is
   failing, what a good follow-up looks like. Intelligence is expressed as useful
   action, not as charts.
4. **Assistant-like.** PAS serves the user. Its default posture is help, not
   judgment; preparation, not surveillance; suggestion, not command.
5. **Approval-gated.** PAS proposes; humans dispose. Any action that touches the
   real world is gated behind explicit human approval until trust and configuration
   say otherwise. Nothing irreversible happens silently.
6. **Evidence-backed.** Every claim, answer, and recommendation can show its
   sources — the call, the document, the record, the memory it came from. PAS says
   what it knows, and is honest about what it does not.
7. **Human-safe.** PAS is calm, non-threatening, and privacy-respecting. It coaches
   rather than watches. It never weaponizes data against the people using it. Safety
   is a feeling agents can sense, not just a policy in a doc.

---

## 4. Three primary user classes

PAS is built for three core human roles. (The full role-to-UX map is PAS302; this
section defines the human truth each role lives in.)

### A. Individual Agent
- **Cares about:** closing more deals, never dropping a lead or a callback,
  remembering every promise, sounding sharp on calls, getting better over time,
  earning more.
- **Fears:** being watched, graded, ranked, and ultimately replaced; a tool that
  reports them to the broker; more admin work; looking bad.
- **PAS must feel like:** a personal assistant and a quiet coach that makes them
  faster and better and is unmistakably *on their side*.
- **PAS must never feel like:** a surveillance dashboard the broker uses to monitor
  them, or another data-entry chore.
- **Daily habit to create:** open PAS first thing to see "what should I do today,
  what did I forget, who's going cold" — and close the day reviewing it.

### B. Brokerage / Team Operator
- **Cares about:** pipeline health across the team, consistency of follow-up and
  scripts, nothing falling through the cracks, ramping new agents fast, growth that
  doesn't require more chaos.
- **Fears:** agents not adopting it (dead tool, wasted spend), losing visibility,
  inconsistent customer experience, key-person dependency, switching costs.
- **PAS must feel like:** an operating layer that makes the whole team reliable and
  legible without micromanaging individuals.
- **PAS must never feel like:** a spy console that demoralizes agents (which kills
  adoption and therefore the operator's own value from PAS).
- **Daily habit to create:** open PAS to see the operation's state — what needs
  attention, where the risk is, what the team committed to — and trust that the
  agents are already living in it.

### C. ORVN Admin
- **Cares about:** the health, safety, and correctness of PAS itself across all
  workspaces; provisioning, support, and the integrity of the platform.
- **Fears:** safety incidents, data leakage across workspaces, silent breakage,
  PAS taking unapproved real-world actions, reputational damage.
- **PAS must feel like:** a controllable, observable, auditable platform with clear
  boundaries and strong defaults.
- **PAS must never feel like:** an opaque black box, or a customer-facing surface
  they can accidentally pollute with internal tooling.
- **Daily habit to create:** confidence — a single place to confirm the platform is
  healthy, safe, and behaving, and to act when it isn't.

---

## 5. Strategic shift: broker dashboard → operating companion

**What is wrong with the current feel.** The deployed A–I surface, for all its
structural correctness, still behaves like a dashboard: it *presents* state and
waits to be read. Pages explain themselves. Modules describe what they contain.
The user is asked to look, interpret, and decide. That is the posture of reporting
software — useful occasionally, opened rarely, and easy to abandon. It proves the
business exists; it does not yet help anyone *run* it. A dashboard is a destination
you visit when you want a number. A companion is something you live inside.

**What the next UI must become.**

- **From describe to drive.** Lead with "here's what to do next / what you forgot /
  what changed," not "here's a panel of everything."
- **From read to act.** Every important screen offers a next action (approve,
  follow up, call back, fix the script) — proposed, evidence-backed, approval-gated.
- **From explanatory to operational.** Less instructional copy, more live operating
  state. The product should feel like it is already mid-work when you arrive, not
  waiting for you to figure it out.
- **From wall-of-modules to a daily flow.** A clear morning view, an in-day working
  surface, and an end-of-day review — a rhythm, not a menu.
- **From neutral tool to companion with a point of view.** Calm, useful, trusted; it
  has opinions about what matters today, and it is usually right.

The test: a dashboard is something you check; a companion is something you open
before you start and review before you stop. PAS must become the second thing.

---

## 6. Agent-first thesis

PAS wins by winning **agents**, not only broker owners. The distribution logic:

- **Agents decide fast.** An individual agent can try, adopt, and love a tool in
  days. A brokerage procurement decision takes months and committees.
- **Agents can pay individually.** A solo agent is a real, self-serve customer — a
  bottoms-up revenue path that doesn't depend on closing an enterprise deal.
- **Agents create bottoms-up distribution.** Agents who rely on PAS bring it into
  their teams and brokerages, and talk about it to other agents. Adoption spreads
  laterally and upward.
- **Agent adoption de-risks brokerage sales.** When agents already use and want PAS,
  the brokerage conversation flips from "should we buy this?" to "let's standardize
  what our people already love." **If agents accept PAS, brokerages have no choice.
  If agents reject PAS, enterprise adoption is fragile** — a top-down rollout into
  resistant agents dies as shelfware.

Therefore PAS must, concretely, help the **agent**:

- close more deals,
- remember more (every lead, promise, callback, detail),
- follow up better and on time,
- improve their scripts and their talk tracks,
- stay accountable to their own commitments,
- and **feel coached, not watched.**

Every agent-facing decision is judged by one question: *does this make the agent
more successful and more loyal, or does it make them feel monitored?* The first
builds the distribution engine; the second breaks it.

---

## 7. Workspace model

PAS is organized around **workspaces** — bounded operating contexts that carry their
own data, members, rules, and PAS configuration. (Implementation is PAS301; this
defines the model.)

- **Personal agent workspace.** Every agent has one. Their leads, callbacks, deals,
  follow-ups, scripts, coaching, memory, and documents. Private by default. This is
  the agent's home and the seat of the morning-open habit.
- **Team workspace.** A shared context for a team or pod — shared pipeline, shared
  rules, shared visibility appropriate to the team, with individual agent privacy
  preserved where it matters.
- **Brokerage workspace.** The brokerage-wide operating layer — standardized rules,
  scripts, integrations, knowledge, and aggregated operational state across teams.
- **ORVN admin workspace.** The platform-operations context — cross-tenant health,
  provisioning, safety, and support. Strictly separated from customer data surfaces.
- **Workspace switching.** A single user can switch between the workspaces they
  belong to without re-authenticating, with the active workspace always
  unambiguous, and with strict data isolation between them.
- **Invitation into a brokerage/team workspace.** A brokerage or team can invite an
  agent; the agent accepts and gains a seat while keeping their personal workspace.
  Membership is explicit and revocable.
- **Same user, multiple workspaces.** One identity can be a solo agent in their
  personal workspace *and* a member of a team and a brokerage. Roles and visibility
  are scoped per workspace.
- **Solo agent path to paid usage.** An agent can sign up alone, use PAS in their
  personal workspace, and pay — with no brokerage required. This is the bottoms-up
  funnel, and later the seed that grows into a team or brokerage workspace.

---

## 8. Auth and session direction

*Future requirements only — defined here, implemented in PAS301. Do not implement.*

- **Sign in.** Real authenticated identity (the demo arc had none).
- **Sign out.** Explicit, reliable session termination.
- **Session timeout.** Idle and absolute timeouts appropriate to a tool that holds
  operational business data.
- **Session limits.** Bounded concurrent sessions per user; visibility into active
  sessions.
- **Secure workspace switching.** Switching contexts must never leak data across
  workspaces and must re-scope authorization on every switch.
- **User identity.** A durable identity that can belong to multiple workspaces with
  distinct roles in each.
- **Role-bound access.** Authorization is enforced by role *within a workspace*, not
  globally — the same person may be an owner in one context and a viewer in another.
- **Device / session management.** Users (and admins, at their scope) can see and
  revoke devices and sessions.

This section is intentionally a requirements statement, not a design. No auth code,
no CORS, no token scheme is decided or touched here.

---

## 9. Role-defined UX direction

The UI must change shape by role, not just hide buttons. Direction per role (full
map is PAS302):

- **Broker Owner.** Operation-wide state: pipeline health, attention queue, risk,
  team commitments, integration health, standards adherence. Lead with "where is the
  operation at risk and what needs a decision," not raw rows.
- **Agent.** The Agent Cockpit (Section 10). Personal, calm, action-first: my day,
  my leads, my callbacks, my next action, my coaching. No surveillance framing.
- **Team Lead.** A blend: their own cockpit *plus* a bounded team view — the team's
  commitments, gaps, and ramping agents — without full brokerage-owner breadth.
- **Admin / Ops.** Configuration, rules, integrations, knowledge governance, and
  operational controls for a workspace. The "how PAS behaves here" surface.
- **ORVN Internal Admin.** Platform health, safety, provisioning, cross-tenant
  observability — strictly outside customer-facing surfaces.
- **Read-only Viewer.** See state, never act. Every action affordance is absent (not
  merely disabled-and-explained). Useful for stakeholders and audits.

Doctrine: roles change the *altitude and the verbs*, not just visibility. An agent
sees "do this next"; an owner sees "decide this"; a viewer sees "this is the state."

---

## 10. Agent Cockpit direction

The Agent Cockpit is the agent's home — the screen that earns the morning-open
habit. (Full spec is PAS303.) It is action-first, calm, and personal. It answers,
above all, three questions: *what should I do next, what did I forget, what can I
improve.*

Core surfaces:

- **My leads** — who's hot, who's cooling, who's new, prioritized by what to do, not
  just listed.
- **My callbacks** — every commitment to call back, with time pressure made obvious.
- **My deals** — pipeline by stage, what's moving, what's stuck, what needs a push.
- **My follow-ups** — the queue of owed actions, surfaced before they're overdue.
- **My scripts** — the agent's talk tracks, with PAS suggesting improvements.
- **My coaching** — specific, kind, evidence-backed guidance drawn from real calls
  and outcomes; coaching, never grading-for-the-boss.
- **My streaks** — light accountability to the agent's *own* commitments (utility,
  not casino mechanics).
- **My PAS memory** — what PAS remembers about the agent's clients, deals, and
  preferences, inspectable and correctable.
- **My documents** — the agent's contracts, listings, notes, and references, made
  queryable.
- **My daily plan** — the proposed shape of the day, assembled from the above.
- **What should I do next?** — the single most valuable next action, always available.
- **What did I forget?** — the dropped promise, the cold lead, the missed callback.
- **What can I improve?** — one concrete, doable improvement, grounded in evidence.

The cockpit must feel like *welcome home* — useful and on your side — never like a
report card.

---

## 11. PAS configuration direction

Operators and agents configure how PAS *behaves*, within safe defaults and role-
bound limits. (Spec is PAS304.) Configuration is the mechanism by which PAS becomes
adaptive (Doctrine §3). Direction — what must be configurable:

- **Give PAS a name** — a personal, ownable assistant identity per workspace/agent.
- **Tone configuration** — warm/formal/brief; the voice PAS uses.
- **Response style** — concise vs. thorough; how much PAS says.
- **Disclosure behavior** — how and when PAS reveals it is an assistant.
- **Escalation rules** — when PAS must hand off to a human and to whom.
- **Approval rules** — what requires explicit approval vs. what is pre-authorized
  (always within the approval-gated doctrine).
- **Working hours** — when PAS acts, follows up, and contacts.
- **Callback strictness** — how aggressively PAS enforces callback commitments.
- **Script preferences** — preferred talk tracks and language.
- **Skills enabled** — which capabilities are on (ties to PAS Skills, Section 15).
- **Knowledge uploaded** — what documents and knowledge PAS may use.
- **Brokerage-specific rules** — standards set at the brokerage that apply downward.
- **Agent-specific rules** — personal overrides within what the brokerage allows.

Configuration must be **sectionized and calm** (UX doctrine §17) — never an endless
settings scroll. Rules resolve predictably: brokerage standards set the frame,
agent preferences personalize within it.

---

## 12. PAS Brain + knowledge upload direction

PAS Brain is what makes the business *queryable*. (Spec is PAS306.) It turns
scattered operational reality into trusted, evidence-backed, queryable knowledge —
with a human always in the approval loop.

Direction:

- **Upload scattered business docs** — contracts, SOPs, scripts, policies, listings,
  notes; the stuff that currently lives in inboxes, drives, and people's heads.
- **Extract operational knowledge** — PAS reads and structures what matters out of
  the mess.
- **Memory candidates** — extracted facts and rules are *proposed*, not silently
  adopted.
- **Human approval** — a person promotes a candidate into trusted knowledge. Nothing
  enters the trusted layer unreviewed.
- **Trusted knowledge** — the approved, governed body of what PAS may rely on.
- **Queryable company** — the brokerage/team can ask the *organization* questions and
  get grounded answers.
- **Queryable agent workspace** — the agent can ask their *own* workspace questions.
- **Evidence-backed answers** — every answer cites its sources (which doc, record,
  call, or memory).
- **What PAS knows / does not know** — PAS is explicit about the boundary of its
  knowledge and never fabricates confidence it doesn't have.

Brain is the doctrine made concrete: queryable + evidence-backed + approval-gated +
human-safe, in one surface.

---

## 13. PAS Chat direction

Chat is the **operating surface**, not a chatbot gimmick. (Spec is PAS305.) It is
where messy human intent meets a system that can retrieve context, reason, and
propose action — always grounded and approval-gated. Direction:

- **Natural messy input** — users type how they think; PAS makes sense of it.
- **LLM fallback when needed** — structured paths handle the common cases; the model
  fills the gaps, grounded in retrieved context rather than free-floating.
- **Context retrieval** — chat pulls the relevant leads, deals, docs, and memory
  before answering.
- **Side context panels** — chat is flanked by the records and evidence it's using,
  so the operator sees *why*, not just *what*.
- **Action proposals** — chat proposes concrete, approval-gated actions inline.
- **Clarifying questions** — when intent is ambiguous, PAS asks rather than guesses.
- **Real-time monitoring** — chat reflects live operating state as it changes.
- **Memory updates** — conversations can produce memory candidates (approval-gated,
  per Brain).
- **Document references** — answers link to and cite the documents behind them.
- **Chat reconciliation** — threads are organized and reconciled to fight
  scatteredness, so the operating history stays coherent rather than fragmenting.
- **Cross-user communication (later)** — chat eventually connects people, not just
  person-and-PAS (ties to Section 14).

Chat must feel like talking to a capable operator who has the whole business in
front of them — not like a toy that answers trivia.

---

## 14. In-app communication direction

PAS will host communication that is **attached to the operation**, not a generic
chat app. (Later-phase; not the immediate arc.) Direction:

- **User-to-user messages** — direct messages between members.
- **Workspace messages** — communication scoped to a workspace.
- **Cross-workspace messaging (later)** — controlled communication across workspace
  boundaries, with isolation respected.
- **Share PAS chats** — hand a PAS conversation to a colleague with its context.
- **Share analytics** — share an operational view or result.
- **Share documents** — share knowledge with scope and permissions.
- **Object-attached threads** — discussions attached to a lead, deal, callback, or
  document, so context lives *with the thing it's about*.
- **Decision records** — durable, referenceable records of decisions made, with their
  evidence.
- **No noisy Slack clone** — explicitly *not* a firehose of channels and pings.
  Communication exists to keep the operation coherent, attached to objects and
  decisions — calm by design.

---

## 15. PAS Skills direction

Skills are PAS's path to a defensible, expanding capability set and a distribution
loop. (Direction is PAS307; do not implement.) Direction:

- **Future skills marketplace** — a catalog of operational capabilities agents and
  operators can enable.
- **Agents and operators can use/buy skills** — capability becomes a purchasable,
  self-serve unit of value.
- **Third parties can create/sell skills (later)** — an ecosystem where outside
  builders extend PAS and share in the value.
- **Skills as a distribution loop** — useful skills attract users; users attract
  skill builders; more skills attract more users.
- **Operational and defensible** — skills must do real operating work (not toys), and
  the marketplace + data + integration depth must be hard to copy.
- **Do not implement yet** — this is direction, not a build instruction.

---

## 16. Pricing / tiering placeholder

*No final prices. Likely tiers and their value boundaries only — to be set in PAS308.*

- **Individual Agent** — entry tier for a solo agent. Boundary: personal workspace,
  core cockpit, bounded knowledge/memory, limited skills, single user.
- **Agent Pro / Solo Operator** — the power solo agent. Boundary: deeper memory and
  knowledge, more skills, stronger automation within approval gates, higher limits.
- **Team / Small Brokerage** — first multi-seat tier. Boundary: team workspace,
  shared rules and scripts, team visibility, basic admin/config, seat-based.
- **Brokerage Growth** — scaling brokerage. Boundary: brokerage workspace,
  standardized rules across teams, broader integrations and knowledge governance,
  role-rich UX, more seats and skills.
- **Enterprise / Manual Setup** — largest, hands-on. Boundary: bespoke onboarding,
  custom rules and integrations, advanced admin/safety controls, dedicated support;
  priced and provisioned manually.

The ladder mirrors the workspace model (Section 7): a solo agent can start at the
bottom and grow into a brokerage tier without leaving PAS.

---

## 17. UX doctrine

**Simple, functional, beautiful.** And specifically:

- **Mature** — serious software for people running a business, not a flashy demo.
- **Comfortable** — a place you're happy to spend the day.
- **Fast** — speed is a feature; latency kills the morning-open habit.
- **Calm** — low noise, low anxiety; no alarm walls.
- **Trustworthy** — evidence-backed, honest about limits, never manipulative.
- **Addictive through utility, not gamification alone** — people return because it
  makes them money and saves them work; streaks are light reinforcement, never the
  point.
- **Less text, more operating state** — show the work, don't explain the software.
- **No endless settings scroll** — settings are **sectionized** and findable.
- **Micro-interactions reduce friction** — every interaction should make the next
  action easier, not add a step.
- **Light / dark mode (eventually).**
- **Profile, photo, preferences (eventually).**

The north star of the UX: it should feel like *welcome home* and *operational
companion* at once — calm enough to trust, useful enough to need.

---

## 18. What the A–I arc proved

Structurally validated by the deployed arc on `main` @ `9f932da`:

- **Main navigation** — the role-aware module navigation holds as a coherent app shell.
- **Operating modules** — leads, calls, callbacks, agents, integrations, settings,
  etc. exist as consistent, related modules.
- **PAS Brain concept** — a dedicated knowledge/intelligence surface is viable.
- **PAS Room concept** — a communication/operating room surface is viable.
- **Integrations model** — a marketplace framing for integrations works structurally.
- **Callback wedge** — callbacks as a sharp, high-value operational primitive land.
- **Demo data model** — a typed, `demoOnly` / `noLiveBehavior` data layer cleanly
  drives the whole UI.
- **Safety posture** — demo chips, "PAS has not changed live customer behavior"
  disclaimers, and the no-live-action stance are consistent and credible.

---

## 19. What the A–I arc did NOT prove

Open, unvalidated, and the reason for this reset:

- **Agent adoption** — that agents will actually open it daily and rely on it.
- **Auth** — there is no real authentication yet.
- **Workspace switching** — no multi-workspace identity or isolation.
- **Onboarding** — no path from sign-up to first value.
- **Role-specific UX** — UI does not yet meaningfully change shape by role.
- **Real PAS chat intelligence** — chat as a grounded operating surface is unproven.
- **PAS configuration** — behavior is not yet configurable.
- **Document upload** — no knowledge ingestion.
- **True workflow execution** — nothing real is executed (correctly, by design, so far).
- **Addiction loop** — no demonstrated reason to return every day.
- **Paid conversion** — no evidence anyone will pay.

A–I proved PAS *can be built as a product*. PAS300 onward must prove PAS *becomes a
habit people pay for*.

---

## 20. Next sequence proposal (PAS301–PAS308)

Each is a planning/spec effort first; build follows its spec. Ordered by dependency.

- **PAS301 — Auth / Session / Workspace Model.** The identity, session, and workspace
  foundation everything else stands on (Sections 7–8). First because role-specific
  UX, cockpit, config, and chat all assume a real user in a real workspace.
- **PAS302 — Role-Specific UX Map.** How the UI changes shape per role (Section 9).
  Depends on PAS301's roles and workspaces.
- **PAS303 — Agent Cockpit Product Spec.** The agent's home and the morning-open
  habit (Section 10). The agent-first thesis made concrete; the adoption wedge.
- **PAS304 — PAS Configuration Layer Spec.** How PAS behavior is configured
  (Section 11). Makes PAS adaptive per workspace and agent.
- **PAS305 — PAS Chat Operating Surface Spec.** Chat as the grounded operating
  surface (Section 13). Depends on Brain knowledge and configuration.
- **PAS306 — PAS Brain Knowledge Upload Spec.** Ingestion, extraction, approval, and
  queryable evidence-backed knowledge (Section 12).
- **PAS307 — PAS Skills Marketplace Direction.** The skills model and distribution
  loop (Section 15). Direction-level; not a build.
- **PAS308 — Pricing + Packaging Strategy.** Turn the tier placeholders (Section 16)
  into a real packaging and pricing strategy across the workspace ladder.

---

## 21. Non-goals for the next immediate arc

Explicitly **not** to be built in the immediate next arc:

- **Real integrations** — no live third-party wiring yet.
- **Real billing** — no payment processing yet.
- **MCP marketplace** — no third-party skill execution platform yet.
- **Full CRM replacement** — do not chase CRM feature parity, and never lead with it.
- **Heavy gamification** — no casino mechanics; utility first.
- **Enterprise admin complexity** — no premature enterprise control sprawl.
- **Slack clone** — no generic channel/ping firehose.
- **Open-ended social network** — communication stays attached to the operation.

Holding these as non-goals keeps the next arc focused on the one thing that matters:
proving agent adoption and the daily habit.

---

## 22. Final product standard

> **PAS should feel like the operating partner an agent or brokerage opens before
> the day starts, trusts during the day, and reviews before the day ends.**

---

### Validation note

This document is **docs-only**. It makes **no** changes to code, UI, backend, CORS,
auth implementation, the PAS209 work, the parked stash, package manifests, or any
API. It defines direction and the PAS301–PAS308 sequence; it does not implement any
of it. Nothing is pushed.
