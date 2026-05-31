# PAS302 — Role-Specific Experience Map

> Status: product direction document (planning only — no UI, backend, auth, CORS, or package changes).
> Owner: ORVN Labs.
> Anchored on: `main` @ `8e9b237`, with PAS301 and PAS301.5 authored on branch `pas301-identity-ownership-session-workspace-lifecycle`.
> Defines: the role-specific experience architecture PAS300 §9 pointed at. Influences PAS303 (Agent Cockpit), PAS304 (Configuration), PAS305 (Chat), PAS301A/B (Account/Switcher shells), and the direction for notifications, navigation, home screens, and onboarding.
> Naming: **PAS = Proactive Assistant for Scale.**

---

## 1. Executive summary

PAS300 moved the center of gravity of the product. The old center was a **brokerage
dashboard** — one surface, viewed from the top, that described a business to whoever logged in.
The new center is an **agent-first operating companion** — a product that runs a person's day
and earns the morning-open habit. That shift makes a single universal experience impossible.

PAS cannot have one experience because the four people who use it do fundamentally different
work, fear different things, and measure success differently. An agent opens PAS to be more
successful and less forgetful; a broker owner opens it to protect revenue and discipline; an
ORVN admin opens it to keep the platform healthy. A surface that serves all of them equally
serves none of them well — it becomes the generic dashboard PAS300 explicitly rejected
(PAS300 §5).

Role-specific experience is therefore required, not cosmetic. Roles must change the **altitude
and the verbs**, not merely hide buttons (PAS300 §9): an agent sees "do this next," an owner
sees "decide this," a viewer sees "this is the state." Each role gets a different operating
experience that happens to share one platform, one identity (PAS301), and one doctrine.

The **Agent experience is the strategic center of gravity** because of the distribution thesis
(PAS300 §6): *if agents accept PAS, brokerages have no choice; if agents reject PAS, enterprise
adoption is fragile.* Everything else — team, brokerage, even ORVN tooling — is built outward
from a beloved agent experience. PAS302 defines the experiences first so that PAS303–PAS305 and
the PAS301 shells build on a settled understanding of *who PAS is for, and what each person's
day actually is.*

---

## 2. Core principle

> **Every user should feel PAS was built primarily for them.**

The wrong mental model is *"one dashboard with different permissions"* — a single screen where
roles toggle visibility and everyone sees a diminished version of the same thing. That produces
software that feels generic to everyone and personal to no one.

The right mental model is **different operating experiences sharing one platform.** The agent's
PAS is a personal assistant. The team lead's PAS is a coaching and coverage instrument. The
owner's PAS is a business operating layer. The ORVN admin's PAS is a platform console. They
share identity, ownership doctrine, the Brain, and Chat — but the *experience* each opens is
shaped to their mission, not filtered from a common dashboard.

Permissions are a security mechanism (PAS301 §§12–13); they are not the experience. The
experience is defined by what PAS *leads with*, what it *does for you*, and what it *makes you
feel* — and those are role-specific by design.

---

## 3. Roles

Four roles at launch. Each: mission · what success means · why they open PAS · what PAS helps
them achieve.

### A. Agent
- **Mission:** close more deals and keep every promise to every client.
- **Success:** never dropping a lead or callback, sounding sharp, getting better, earning more.
- **Why they open PAS:** to know what to do next and what they forgot — to start the day in
  control rather than behind.
- **PAS helps them:** prioritize, remember, follow up on time, improve their craft, and feel
  supported rather than watched.

### B. Team Lead
- **Mission:** make a pod of agents reliable and rising without micromanaging them.
- **Success:** no commitments slipping across the team, agents ramping and improving, risk
  caught early.
- **Why they open PAS:** to see where the team needs help today and who to support.
- **PAS helps them:** spot accumulating risk, coach the right agent at the right moment, and
  keep team commitments intact — as a coach, not a monitor.

### C. Brokerage Owner
- **Mission:** run a healthy, growing brokerage where nothing falls through the cracks.
- **Success:** protected revenue, disciplined follow-up, consistent customer experience,
  growth without chaos.
- **Why they open PAS:** to see where the operation is at risk and what needs a leadership
  decision.
- **PAS helps them:** find where money leaks and discipline fails, standardize the work, and
  decide — without drowning in dashboard bloat.

### D. ORVN Admin
- **Mission:** keep PAS itself healthy, safe, and adopted across all tenants.
- **Success:** no safety incidents, healthy tenants, fast support, growing adoption.
- **Why they open PAS:** to confirm the platform is healthy and to act where it isn't.
- **PAS helps them:** see which customers need help, which tenants are unhealthy, and what is
  failing — proactively, not reactively.

---

## 4. Agent experience

The most important section in this document.

**Why would an agent open PAS every morning?** Because PAS already did the worrying for them
overnight. It opens to *"here's what needs you today, here's what you almost forgot, here's the
one thing worth doing first"* — the relief of starting the day in control. An agent returns
because PAS makes them money and saves them from the dropped-ball anxiety that defines the job.

**What should they see first?** The **Agent Cockpit** (full spec PAS303) — action-first, calm,
personal. Not a list of everything; the *next right things*, prioritized. The single most
valuable next action is always visible.

**What should PAS proactively surface?** Cooling leads, owed callbacks before they're overdue,
deals that are stuck, promises made and not yet kept, and one concrete improvement grounded in a
real call or outcome. Proactivity is the differentiator (PAS300 §6) — PAS tells you what changed
and what to do, rather than waiting to be read.

**What emotional outcome should PAS create?** *Welcome home* — calm, supported, on top of the
day, coached by something on your side. Never the report-card dread of management software.

Defined surfaces and flows:

- **Agent Cockpit** — the home that earns the habit; answers what-next / what-forgot /
  what-improve (PAS300 §10, PAS303).
- **Daily flow** — a rhythm, not a menu: morning → midday → end-of-day.
  - **Morning flow:** "Here's your day." The plan, the priorities, the at-risk items, the
    single best first action.
  - **Midday flow:** the working surface — owed actions surfaced before they slip, quick
    capture, "what should I do next" always one glance away.
  - **End-of-day flow:** a calm review — what got done, what to carry forward, what slipped and
    why; close the day in control.
- **Coaching** — specific, kind, evidence-backed guidance from real calls and outcomes; for the
  agent, never a report to the boss (PAS301 §22).
- **Accountability** — light reinforcement to the agent's *own* commitments (streaks as utility,
  not casino mechanics; PAS300 §17).
- **Opportunity discovery** — surfacing the lead worth re-engaging, the deal worth a push, the
  client worth a check-in — "what is worth doing."
- **Follow-up protection** — the queue of owed callbacks and follow-ups, with time pressure made
  obvious, so nothing is dropped. The callback wedge made personal (PAS300 §18).
- **Personal growth** — the agent's craft compounding over time: scripts improving, habits
  sharpening, a visible sense of getting better.

The questions PAS answers for an agent:
- **What should I do next?** — the single most valuable action, always available.
- **What did I forget?** — the dropped promise, the cold lead, the missed callback.
- **What is slipping?** — deals and commitments losing momentum.
- **What is worth doing?** — opportunity, not just obligation.
- **What should PAS handle?** — what can be proposed/prepared for approval so the agent doesn't
  have to (approval-gated; PAS300 §3).
- **How can I improve?** — one concrete, doable improvement grounded in evidence.

**What PAS becomes to an agent:** a personal assistant and quiet coach that makes them faster,
sharper, and more successful — unmistakably on their side. The thing they open first and trust
most. This is the relationship the entire business is built on.

---

## 5. Team Lead experience

**Why does a Team Lead open PAS?** To answer one question fast: *where does my team need me
today?* They open it to find the agent to help and the risk to catch before it becomes a lost
deal — not to police activity.

**What do they need?** A bounded view of the team's reality (PAS300 §9, §7 team workspace):

- **Team health** — is the pod on track, where is it strained.
- **Team coverage** — are leads and callbacks being handled; where are the gaps.
- **Team commitments** — what the team owes clients, and what's at risk of slipping.
- **Coaching opportunities** — which agent would benefit from a specific, timely nudge.
- **Risk visibility** — where risk is *accumulating*, surfaced early enough to act.

Questions PAS answers for a Team Lead:
- **Who needs help?** — the agent to support today.
- **Where is risk accumulating?** — the gap forming before it breaks.
- **What commitments are slipping?** — team obligations losing time.
- **Which agents need support?** — coaching targets, framed as support.

**Avoid surveillance framing.** The Team Lead sees *aggregate and coverage-level* signal and
coaching opportunities — never an individual agent's private coaching, personal workspace, or a
ranked leaderboard by default (PAS300 §22 boundary; PAS301 §22). The verb is *support*, not
*monitor*. A team lead who feels like a surveillance operator will use PAS to police, agents
will feel it, and the adoption engine breaks from the top.

---

## 6. Brokerage owner experience

**Why does a Broker Owner open PAS?** To see where the operation is at risk and what needs a
leadership decision — not to read rows. They open the **Brokerage Command Center** for the
state of the business and the few decisions that matter today.

Defined:

- **Operational intelligence** — the state of the operation expressed as attention and risk,
  not raw data.
- **Brokerage health** — pipeline health across teams, follow-up discipline, standards
  adherence.
- **Revenue protection** — where deals and money are leaking, surfaced as something to act on.
- **Follow-up discipline** — is the brokerage keeping its promises to clients, consistently.
- **System visibility** — integration health and operational integrity at a glance.

Questions PAS answers for a Broker Owner:
- **Where is money leaking?** — revenue at risk from dropped follow-up or stuck deals.
- **Where are commitments failing?** — discipline breaking down across teams.
- **What operational risks exist?** — the structural risks that need leadership.
- **What should leadership address?** — the short list of decisions worth their attention.

**Avoid dashboard bloat.** Lead with "where is the operation at risk and what needs a decision"
(PAS300 §9), not a wall of charts. The owner experience is a decision surface, not a reporting
warehouse — the failure mode here is recreating the very dashboard PAS300 left behind. Depth is
available on demand; the default is the decisive few.

---

## 7. ORVN Admin experience

Internal-only platform operations (PAS301 §18); strictly outside customer-facing surfaces.

Defined:

- **Tenant support** — tools to help customers, scoped to the support task.
- **Provisioning** — stand up and configure tenants; hand off ownership.
- **Tenant health** — cross-tenant observability of health, usage, and safety.
- **Incident management** — detect, record, and respond to safety/security incidents.
- **Product adoption** — which tenants and agents are adopting (or not), as a success signal.

Questions PAS answers for ORVN Admin:
- **Which customers need help?** — accounts at risk of churn or stuck in onboarding.
- **Which tenants are unhealthy?** — health/safety/usage anomalies.
- **What is failing?** — platform-level failures needing response.

The ORVN experience is about confidence and proactivity: a single place to confirm the platform
is healthy and safe, and to act when it isn't — without ever casually exposing tenant secrets
(PAS301 §18).

---

## 8. Landing experience

After sign-in (PAS301.5), the user lands in their **last active workspace**, and the *shape* of
that landing is role-specific:

- **Agent → Agent Cockpit.** Because the agent's first need is "what do I do next" — action,
  not overview. The cockpit is the morning-open habit (PAS303).
- **Team Lead → Team Cockpit.** Because the lead's first need is "where does my team need me" —
  coverage and coaching, a bounded team altitude. (A team lead also has their *own* agent
  cockpit, one switch away — PAS300 §9 blend.)
- **Broker Owner → Brokerage Command Center.** Because the owner's first need is "where is the
  operation at risk and what must I decide" — operation-wide altitude.
- **ORVN Admin → ORVN Console.** Because the admin's first need is "is the platform healthy and
  safe" — cross-tenant altitude, internal-only.

**Why:** the landing screen is the product's answer to "why did you open me?" Each role's
answer is different, so each role's first screen is different. Landing a broker on an agent
cockpit, or an agent on an operation dashboard, would make PAS feel like it wasn't built for
them — violating the core principle (§2).

---

## 9. Navigation strategy

Navigation should feel **role-aware, focused, and contextual** — a way to move through *your*
work, not a directory of the whole platform.

- **Role-aware:** the navigation an agent sees is built around their day (leads, callbacks,
  deals, coaching); the owner's is built around the operation. Same platform, different verbs
  and altitude.
- **Focused:** few, meaningful destinations — not a sprawling module menu. The default is the
  thing you need now, with depth available, not demanded.
- **Contextual:** navigation responds to the active workspace and role (PAS301 §7); the active
  workspace and role/hat are always unambiguous (PAS301 §24).

**Avoid dashboard-first thinking** — navigation that presents "all the modules" and asks the
user to choose where to look. That is the wall-of-modules posture PAS300 §5 rejected.
Navigation should feel like the product already knows what you came to do and puts it first.

---

## 10. Notifications

Notifications differ by role because each role's "this needs you" is different. All are calm,
low-noise, and per-workspace labeled (PAS301 §7); none are alarm walls (PAS300 §17).

- **Agent — personal obligations.** "You owe a callback in 20 minutes." "This lead is going
  cold." Personal, actionable, on the agent's side.
- **Team Lead — coverage risks.** "Two callbacks in the team are unassigned." "An agent is
  underwater today." Coverage and support signals — never "Agent X is behind" framed as a
  report (PAS300 §22).
- **Broker Owner — operational risks.** "Follow-up discipline dropped in Team B this week."
  "A high-value deal is stalling." Operation-level risk worth a decision.
- **ORVN Admin — tenant risks.** "Tenant Y shows a health anomaly." "Onboarding stalled for a
  new brokerage." Platform and customer-success signals.

The doctrine: a notification exists to protect a commitment or surface a risk *the recipient can
act on at their altitude* — not to generate engagement through noise.

---

## 11. PAS Brain relationship

Each role queries a Brain scoped to their workspace and altitude (PAS301 §20 isolation rules):

- **Agent — personal coach.** Queries their own workspace: their leads, deals, scripts, and the
  coaching that compounds their craft. Their portable, PII-clean coaching follows them
  (PAS301 §20).
- **Team Lead — team intelligence.** Queries the team's shared knowledge and commitments;
  bounded to the team, never into members' personal workspaces.
- **Broker Owner — operational memory.** Queries the brokerage as an organization: standards,
  operational history, where discipline holds and fails — the *queryable company*.
- **ORVN Admin — platform intelligence.** Queries platform-level health and adoption across
  tenants, within strict isolation and least privilege.

The Brain's tenant-isolation and provenance rules (PAS301 §§19–20) make these four relationships
safe simultaneously: same engine, four scopes, zero bleed.

---

## 12. PAS Chat relationship

Chat is the operating surface (PAS305), shaped by role:

- **Agent — daily operating partner.** "Who should I call first?" "Draft a follow-up to the
  Johnsons." Chat runs the agent's day, grounded and approval-gated.
- **Team Lead — team assistant.** "Which of my agents has slipping callbacks?" "Summarize the
  team's at-risk deals." Bounded to the team.
- **Broker Owner — business operator.** "Where did follow-up discipline drop this month?"
  "Which teams are at risk?" Chat as a way to interrogate the operation.
- **ORVN Admin — platform operator.** "Which tenants are unhealthy?" "What's failing right now?"
  Chat as platform operations.

Every role's chat retrieves context, cites evidence, and proposes approval-gated actions
(PAS300 §13) — differing in scope and altitude, not in safety posture.

---

## 13. Adoption loops

Why each role *comes back* (the rational reason to return):

- **Agent — daily usefulness.** PAS saves them from dropped balls and makes them money every
  day; returning is in their direct self-interest.
- **Team Lead — team visibility.** PAS shows them where to help without chasing people; it makes
  leading easier.
- **Broker Owner — operational leverage.** PAS turns scattered operation into decisions; it
  multiplies the owner's reach.
- **ORVN Admin — customer success.** PAS surfaces which customers need help before they churn;
  it makes the platform's success legible.

Adoption loops are the *utility* reason to return. They are necessary but, on their own, not
enough to create a habit — that requires the addiction loop.

---

## 14. Addiction loops

Defined carefully: **habit formation through utility, never manipulation** (PAS300 §17 —
"addictive through utility, not gamification alone"). PAS does not use casino mechanics, dark
patterns, or manufactured urgency. The habit is built honestly:

- **A reliable morning payoff.** Every open delivers immediate value — "here's what needs you" —
  so opening PAS becomes the rational first move of the day.
- **Relief, not anxiety.** PAS removes the dropped-ball dread; the feeling of being on top of
  the day is what people return for.
- **Compounding value.** The more an agent uses PAS, the more it knows and the more useful it
  gets — leaving is a real loss of accumulated leverage.
- **Closure rituals.** The end-of-day review creates a satisfying close; the morning view a
  confident open. A rhythm, not a slot machine.
- **Light, self-directed accountability.** Streaks reinforce the agent's *own* commitments
  (utility), never social ranking (manipulation).

What makes PAS *"the first tab opened every morning"*: it consistently answers "what needs me
today" better and faster than checking five tools, and it does so calmly enough to trust. The
habit is earned by being genuinely the best first move — not engineered by exploiting the user.

---

## 15. What must never happen

Role-specific failure modes — the experience-level mistakes that break each role:

- **Agent — feels monitored.** The moment PAS feels like a surveillance tool the broker uses
  against them, the agent disengages and the whole distribution thesis collapses (PAS300 §6).
  This is the cardinal failure.
- **Team Lead — feels blind.** If PAS hides the team's real state behind privacy or noise, the
  lead can't lead and abandons it. The challenge: visibility into *coverage and risk* without
  surveillance of *individuals* (§5).
- **Broker Owner — feels uninformed.** If PAS buries the few decisions that matter under
  dashboard bloat, the owner can't see where the operation is at risk and loses trust in it
  (§6).
- **ORVN Admin — feels reactive.** If PAS only shows problems after they've hurt a customer,
  the admin is firefighting instead of preventing — the platform feels out of control (§7).

Each failure mode is the inverse of that role's reason to open PAS. Avoiding them is the bar
PAS302 sets for every downstream spec.

---

## 16. Future expansion

PAS must be *role-extensible* — new roles slot into the same identity, workspace, and ownership
model (PAS301) without re-architecture. Future roles to remain compatible with (not designed
here):

- **ISA (Inside Sales Agent)** — high-volume lead qualification and appointment-setting.
- **Operations Manager** — process and workflow oversight across the brokerage.
- **Transaction Coordinator** — deal-closing logistics and compliance paperwork.
- **Recruiter** — agent recruiting and onboarding pipeline.
- **Coach** — dedicated coaching across agents (distinct from the team lead's coaching).
- **Franchise Operator** — multi-brokerage / franchise-level operation above a single brokerage.

**Future-compatibility requirements only:** each is a role scoped within a workspace, with its
own altitude/verbs, its own landing experience, its own Brain/Chat scope, and its own
notification profile — composing with the same doctrine. PAS302 reserves room for them; it does
not specify them.

---

## 17. Product hierarchy

Explicit ranking of importance:

1. **Agent** — the strategic center of gravity. Agent adoption is the distribution engine; if
   agents reject PAS, enterprise adoption is fragile (PAS300 §6). The agent experience is
   prioritized hardest and protected most.
2. **Team Lead** — the first multiplier of agent value and the bridge to the brokerage. A team
   lead who can support (not surveil) agents extends the agent's good experience upward.
3. **Brokerage Owner** — the economic buyer at scale, but a buyer whose decision is *de-risked*
   by agent adoption rather than driving it. Important, but built outward from the agent.
4. **ORVN Admin** — essential for platform health and safety, but internal and in service of the
   first three; it enables the customer experience rather than being one.

**Why this order:** it is the order of the distribution thesis. Value is created at the agent,
multiplied at the team, monetized at the brokerage, and safeguarded by ORVN. Build inside-out
from the agent, and every other role inherits a product that already works for the people whose
acceptance everything depends on. Invert the order — build owner-first — and you rebuild the
dashboard PAS300 left behind.

---

## 18. Final standard

> **Every role should feel PAS understands their day, protects their commitments, improves
> their decisions, and helps them scale without becoming another dashboard.**

---

### Validation note

This document is **docs-only**. It makes **no** changes to UI, backend, auth, CORS, packages,
the PAS209 work, or the parked stash. It defines the role-specific experience architecture and
the landing, navigation, notification, Brain, Chat, and adoption direction per role; it
implements none of it. Nothing is pushed.
